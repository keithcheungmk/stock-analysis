#!/usr/bin/env python3
"""Download six-quarter official SEC/IR research packages with provenance."""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from lxml import html


PERIODIC_FORMS = {"10-Q", "10-K", "20-F"}
EVENT_FORMS = {"8-K", "6-K"}
ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "application/json",
    "application/xml",
    "application/xhtml+xml",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/octet-stream",
    "text/html",
    "text/plain",
    "text/xml",
}


@dataclass
class Filing:
    accession: str
    form: str
    filing_date: str
    report_date: str
    primary_document: str


class OfficialDownloader:
    def __init__(self, user_agent: str, requests_per_second: float = 2) -> None:
        if "@" not in user_agent:
            raise ValueError("SEC_USER_AGENT must contain a contact email")
        self.user_agent = user_agent
        self.minimum_interval = 1 / requests_per_second
        self.last_request = 0.0

    def fetch(
        self,
        url: str,
        timeout: int = 45,
        attempts: int = 4,
        user_agent: str | None = None,
    ) -> tuple[bytes, str]:
        elapsed = time.monotonic() - self.last_request
        if elapsed < self.minimum_interval:
            time.sleep(self.minimum_interval - elapsed)
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": self.user_agent,
                "Accept-Encoding": "identity",
                "Accept": "*/*",
            },
        )
        if user_agent:
            request.add_header("User-Agent", user_agent)
        last_error: Exception | None = None
        for attempt in range(attempts):
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    body = response.read()
                    content_type = response.headers.get_content_type()
                    self.last_request = time.monotonic()
                    if not body:
                        raise ValueError(f"empty response from {url}")
                    if b"Your Request Originates from an Undeclared Automated Tool" in body:
                        raise PermissionError("SEC rejected the declared User-Agent")
                    return body, content_type
            except (urllib.error.URLError, TimeoutError, ValueError) as exc:
                last_error = exc
                time.sleep(2**attempt)
        raise RuntimeError(f"failed to fetch {url}: {last_error}")

    def fetch_json(self, url: str) -> dict[str, Any]:
        body, _ = self.fetch(url)
        return json.loads(body)


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line or line.lstrip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip("\"'"))


def filing_rows(submissions: dict[str, Any]) -> list[Filing]:
    recent = submissions["filings"]["recent"]
    rows: list[Filing] = []
    for index, accession in enumerate(recent["accessionNumber"]):
        rows.append(
            Filing(
                accession=accession,
                form=recent["form"][index],
                filing_date=recent["filingDate"][index],
                report_date=recent["reportDate"][index],
                primary_document=recent["primaryDocument"][index],
            )
        )
    return rows


def date_distance(left: str, right: str) -> int:
    return abs((date.fromisoformat(left) - date.fromisoformat(right)).days)


def select_filings(rows: list[Filing], period: dict[str, Any]) -> list[Filing]:
    period_end = period["period_end"]
    periodic = [
        row
        for row in rows
        if row.form in PERIODIC_FORMS and row.report_date == period_end
    ]
    anchor = period.get("release_date")
    if not anchor and periodic:
        anchor = min(row.filing_date for row in periodic)
    events: list[Filing] = []
    if anchor:
        candidates = [
            row
            for row in rows
            if row.form in EVENT_FORMS and date_distance(row.filing_date, anchor) <= 7
        ]
        if candidates:
            nearest_distance = min(date_distance(row.filing_date, anchor) for row in candidates)
            events = [
                row
                for row in candidates
                if date_distance(row.filing_date, anchor) == nearest_distance
            ]
    selected = periodic + events
    unique: dict[str, Filing] = {row.accession: row for row in selected}
    return sorted(unique.values(), key=lambda row: (row.filing_date, row.form))


def accession_urls(cik: str, filing: Filing) -> tuple[str, str]:
    cik_number = str(int(cik))
    accession_plain = filing.accession.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{cik_number}/{accession_plain}"
    return base, f"{base}/{filing.accession}-index.html"


def normalize_sec_document_url(url: str) -> str:
    """Expand SEC ixviewer links to the underlying Archives document URL.

    `/ix?doc=/Archives/...` returns an XBRL viewer shell (~6KB), not the filing.
    """
    parsed = urllib.parse.urlparse(url)
    if parsed.path.rstrip("/") != "/ix":
        return url
    query = urllib.parse.parse_qs(parsed.query)
    doc = (query.get("doc") or [None])[0]
    if not doc:
        return url
    if doc.startswith("/"):
        return urllib.parse.urljoin("https://www.sec.gov", doc)
    return doc


def parse_filing_documents(index_body: bytes, index_url: str) -> list[dict[str, str]]:
    document = html.fromstring(index_body, base_url=index_url)
    results: list[dict[str, str]] = []
    for row in document.xpath("//table[contains(@class, 'tableFile')]//tr"):
        cells = row.xpath("./td")
        if len(cells) < 4:
            continue
        links = cells[2].xpath(".//a/@href")
        if not links:
            continue
        resolved = normalize_sec_document_url(
            urllib.parse.urljoin(index_url, links[0])
        )
        results.append(
            {
                "description": " ".join(cells[1].itertext()).strip(),
                "url": resolved,
                "name": Path(urllib.parse.urlparse(resolved).path).name,
                "type": " ".join(cells[3].itertext()).strip().upper(),
            }
        )
    return results


def classify_document(filing: Filing, document: dict[str, str]) -> str:
    description = document["description"].lower()
    name = document["name"].lower()
    if document["name"] == filing.primary_document or document["type"] == filing.form:
        return "regulatory_filing" if filing.form in PERIODIC_FORMS else "event_filing"
    if "transcript" in description or "transcript" in name:
        return "official_transcript"
    if any(term in description or term in name for term in ("presentation", "slides", "deck")):
        return "earnings_presentation"
    if any(
        term in description or term in name
        for term in ("shareholder", "quarterly update", "investor update")
    ):
        return "shareholder_update"
    if document["type"].startswith("EX-99") or any(
        term in description for term in ("earnings", "press release", "financial results")
    ):
        return "earnings_release"
    return "sec_exhibit"


def safe_name(value: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-").lower()
    return name or "document"


def extension_for(url: str, content_type: str) -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in {".htm", ".html", ".pdf", ".xml", ".xlsx", ".xls", ".txt"}:
        return ".html" if suffix == ".htm" else suffix
    guessed = mimetypes.guess_extension(content_type) or ".bin"
    return ".html" if guessed == ".htm" else guessed


def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def read_manifest(path: Path, company: dict[str, Any], period: dict[str, Any]) -> dict[str, Any]:
    if path.exists():
        manifest = json.loads(path.read_text(encoding="utf-8"))
    else:
        manifest = {
            "schema_version": 2,
            "company": company["name"],
            "ticker": company["ticker"],
            "fiscal_period": period["label"],
            "period_end": period["period_end"],
            "authority": "Official company IR and SEC EDGAR",
            "event_page": company["ir_url"],
            "files": [],
        }
    manifest.update(
        {
            "schema_version": 2,
            "company": company["name"],
            "ticker": company["ticker"],
            "fiscal_period": period["label"],
            "period_end": period["period_end"],
            "currency": company["currency"],
            "accounting_basis": period.get(
                "accounting_basis", company["accounting_basis"]
            ),
            "cik": company["cik"],
            "event_page": company["ir_url"],
        }
    )
    if period.get("release_date"):
        manifest["release_date"] = period["release_date"]
    return manifest


def merge_file_entry(manifest: dict[str, Any], entry: dict[str, Any]) -> None:
    for existing in manifest["files"]:
        if existing.get("sha256") == entry["sha256"]:
            existing.update(entry)
            entry["path"] = existing["path"]
            return
    manifest["files"].append(entry)


def unavailable_policy(ticker: str, period_label: str) -> list[dict[str, str]]:
    unavailable: list[dict[str, str]] = []
    if ticker in {"GOOG"}:
        unavailable.append(
            {
                "type": "earnings_presentation",
                "status": "not_part_of_standard_official_package",
                "substitute": "earnings_release",
            }
        )
    if ticker in {"DUOL"}:
        unavailable.append(
            {
                "type": "earnings_presentation",
                "status": "not_part_of_standard_official_package",
                "substitute": "shareholder_update",
            }
        )
    if ticker == "HIMS" and period_label == "2026-Q1":
        unavailable.append(
            {
                "type": "quarterly_shareholder_letter",
                "status": "company_changed_to_annual_shareholder_letters",
                "substitute": "earnings_release",
            }
        )
    if ticker not in {"CLSK", "GOOG"}:
        unavailable.append(
            {
                "type": "official_transcript",
                "status": "not_part_of_standard_official_package",
                "substitute": "webcast_metadata",
            }
        )
    return unavailable


def classify_ir_link(text: str) -> str | None:
    value = text.lower()
    if "transcript" in value:
        return "official_transcript"
    if any(term in value for term in ("presentation", "slides", "slide deck")):
        return "earnings_presentation"
    if any(term in value for term in ("shareholder letter", "quarterly update")):
        return "shareholder_update"
    if any(
        term in value
        for term in ("earnings release", "financial results", "interim report", "results report")
    ):
        return "earnings_release"
    if any(term in value for term in ("financial table", "fact sheet", "factsheet")):
        return "financial_tables"
    return None


def discover_ir_links(
    downloader: OfficialDownloader, ir_url: str
) -> list[dict[str, str]]:
    try:
        request = urllib.request.Request(
            ir_url,
            headers={
                "User-Agent": downloader.user_agent,
                "Accept-Encoding": "identity",
                "Accept": "text/html,*/*",
            },
        )
        with urllib.request.urlopen(request, timeout=12) as response:
            body = response.read()
    except Exception:
        return []
    document = html.fromstring(body, base_url=ir_url)
    links: list[dict[str, str]] = []
    seen: set[str] = set()
    for anchor in document.xpath("//a[@href]"):
        href = urllib.parse.urljoin(ir_url, anchor.get("href"))
        if href in seen or urllib.parse.urlparse(href).scheme not in {"http", "https"}:
            continue
        text = " ".join(anchor.itertext()).strip()
        combined = f"{text} {href}"
        document_type = classify_ir_link(combined)
        if not document_type:
            continue
        seen.add(href)
        links.append(
            {
                "url": href,
                "name": Path(urllib.parse.urlparse(href).path).name or document_type,
                "description": text,
                "type": "IR",
                "document_type": document_type,
            }
        )
    return links


def ir_links_for_period(
    links: list[dict[str, str]], period: dict[str, Any]
) -> list[dict[str, str]]:
    match = re.search(r"(20\d{2}).*Q([1-4])", period["label"], re.IGNORECASE)
    if not match:
        return []
    year, quarter = match.groups()
    short_year = year[-2:]
    quarter_words = {
        "1": ("first quarter",),
        "2": ("second quarter", "half year", "half-year"),
        "3": ("third quarter", "nine months"),
        "4": ("fourth quarter", "full year"),
    }[quarter]
    results = []
    for link in links:
        value = urllib.parse.unquote_plus(
            f"{link['description']} {link['url']}"
        ).lower()
        has_year = bool(
            re.search(rf"(?<!\d){year}(?!\d)", value)
            or re.search(rf"(?<![a-z0-9])fy[\s._-]*{short_year}(?!\d)", value)
        )
        quarter_pattern = (
            rf"(?<![a-z0-9])q[\s._-]*{quarter}(?![a-z0-9])|"
            rf"(?<![a-z0-9]){quarter}q(?![a-z0-9])"
        )
        has_quarter = bool(re.search(quarter_pattern, value)) or any(
            token in value for token in quarter_words
        )
        if quarter == "4":
            has_quarter = has_quarter or bool(
                re.search(
                    rf"(?<![a-z0-9])fy[\s._-]*(?:{year}|{short_year})(?!\d)",
                    value,
                )
            )
        if has_year and has_quarter:
            results.append(link)
    return results


def catalog_period(
    downloader: OfficialDownloader,
    company: dict[str, Any],
    period: dict[str, Any],
    filings: list[Filing],
    ir_links: list[dict[str, str]],
) -> dict[str, Any]:
    selected = select_filings(filings, period)
    catalog_filings: list[dict[str, Any]] = []
    for filing in selected:
        _, index_url = accession_urls(company["cik"], filing)
        index_body, _ = downloader.fetch(index_url)
        documents = parse_filing_documents(index_body, index_url)
        selected_documents = []
        for document in documents:
            is_primary = (
                document["name"] == filing.primary_document
                or document["type"] == filing.form
            )
            is_earnings_exhibit = document["type"].startswith("EX-99")
            if is_primary or is_earnings_exhibit:
                selected_documents.append(
                    {
                        **document,
                        "document_type": classify_document(filing, document),
                    }
                )
        catalog_filings.append(
            {
                "accession_number": filing.accession,
                "form": filing.form,
                "filing_date": filing.filing_date,
                "report_date": filing.report_date,
                "index_url": index_url,
                "documents": selected_documents,
            }
        )
    return {
        "label": period["label"],
        "period_end": period["period_end"],
        "release_date": period.get("release_date"),
        "filings": catalog_filings,
        "ir_documents": ir_links_for_period(ir_links, period),
        "ir_page": company["ir_url"],
        "unavailable_sources": unavailable_policy(company["ticker"], period["label"]),
    }


def build_catalog(
    downloader: OfficialDownloader,
    config: dict[str, Any],
    tickers: set[str] | None = None,
    labels: set[str] | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "schema_version": 1,
        "as_of": config["as_of"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "companies": {},
    }
    for ticker, raw_company in config["companies"].items():
        if tickers and ticker not in tickers:
            continue
        company = {**raw_company, "ticker": ticker}
        submissions_url = config["sec"]["submissions_url"].format(cik=company["cik"])
        submissions = downloader.fetch_json(submissions_url)
        filings = filing_rows(submissions)
        ir_links = discover_ir_links(downloader, company["ir_url"])
        periods = []
        for period in company["periods"]:
            if labels and period["label"] not in labels:
                continue
            periods.append(
                catalog_period(downloader, company, period, filings, ir_links)
            )
        result["companies"][ticker] = {
            "name": company["name"],
            "cik": company["cik"],
            "ir_url": company["ir_url"],
            "currency": company["currency"],
            "accounting_basis": company["accounting_basis"],
            "periods": periods,
        }
    return result


def download_catalog(
    downloader: OfficialDownloader,
    catalog: dict[str, Any],
    raw_root: Path,
) -> dict[str, int]:
    counts = {
        "downloaded": 0,
        "already_present": 0,
        "failed": 0,
        "periods": 0,
    }
    staging_root = raw_root.parent / ".official-download-staging"
    for ticker, company in catalog["companies"].items():
        company_config = {**company, "ticker": ticker}
        for period in company["periods"]:
            counts["periods"] += 1
            target_directory = raw_root / ticker / period["label"]
            manifest_path = target_directory / "manifest.json"
            manifest = read_manifest(manifest_path, company_config, period)
            manifest["retrieved_at"] = datetime.now(timezone.utc).isoformat()
            manifest["unavailable_sources"] = period["unavailable_sources"]
            manifest["pending_sources"] = []
            found_types: set[str] = set()
            period_filings = list(period["filings"])
            if period.get("ir_documents"):
                period_filings.append(
                    {
                        "accession_number": "official-ir",
                        "form": "IR",
                        "filing_date": period.get("release_date"),
                        "report_date": period["period_end"],
                        "index_url": company["ir_url"],
                        "documents": period["ir_documents"],
                    }
                )
            filing_forms = {filing["form"] for filing in period_filings}
            for filing in period_filings:
                for document in filing["documents"]:
                    document_url = normalize_sec_document_url(document["url"])
                    document_name = (
                        Path(urllib.parse.urlparse(document_url).path).name
                        or document.get("name")
                        or "document"
                    )
                    try:
                        existing_by_url = next(
                            (
                                entry
                                for entry in manifest["files"]
                                if entry.get("source_url")
                                in {document_url, document["url"]}
                            ),
                            None,
                        )
                        if existing_by_url:
                            existing_path = target_directory / existing_by_url["path"]
                            if (
                                existing_path.exists()
                                and sha256_bytes(existing_path.read_bytes())
                                == existing_by_url.get("sha256")
                                and existing_by_url.get("size_bytes", 0) >= 50_000
                            ):
                                existing_by_url["type"] = document["document_type"]
                                existing_by_url["source_url"] = document_url
                                found_types.add(document["document_type"])
                                counts["already_present"] += 1
                                continue
                        is_sec = (
                            urllib.parse.urlparse(document_url).hostname
                            in {"www.sec.gov", "data.sec.gov"}
                        )
                        body, content_type = downloader.fetch(
                            document_url,
                            timeout=45 if is_sec else 15,
                            attempts=4 if is_sec else 2,
                            user_agent=(
                                None
                                if is_sec
                                else "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                                "AppleWebKit/537.36 Chrome/140.0 Safari/537.36"
                            ),
                        )
                        if content_type not in ALLOWED_CONTENT_TYPES:
                            raise ValueError(f"unexpected MIME type {content_type}")
                        if (
                            is_sec
                            and content_type.startswith("text/html")
                            and len(body) < 50_000
                            and b"XBRL Viewer" in body
                        ):
                            raise ValueError(
                                "downloaded SEC ixviewer stub instead of filing body"
                            )
                        digest = sha256_bytes(body)
                        extension = extension_for(document_url, content_type)
                        authority_prefix = "ir" if filing["form"] == "IR" else "sec"
                        filename = safe_name(
                            f"{authority_prefix}-{filing['form']}-"
                            f"{filing['accession_number']}-"
                            f"{Path(document_name).stem}"
                        ) + extension
                        existing = next(
                            (
                                entry
                                for entry in manifest["files"]
                                if entry.get("sha256") == digest
                            ),
                            None,
                        )
                        if existing and (target_directory / existing["path"]).exists():
                            counts["already_present"] += 1
                            path_name = existing["path"]
                        else:
                            staged = staging_root / ticker / period["label"] / filename
                            staged.parent.mkdir(parents=True, exist_ok=True)
                            staged.write_bytes(body)
                            if sha256_bytes(staged.read_bytes()) != digest:
                                raise ValueError("staging SHA-256 mismatch")
                            target_directory.mkdir(parents=True, exist_ok=True)
                            destination = target_directory / filename
                            if destination.exists() and sha256_bytes(destination.read_bytes()) != digest:
                                destination = destination.with_name(
                                    f"{destination.stem}--{digest[:8]}{destination.suffix}"
                                )
                            os.replace(staged, destination)
                            path_name = destination.name
                            counts["downloaded"] += 1
                        document_type = document["document_type"]
                        found_types.add(document_type)
                        entry = {
                                "path": path_name,
                                "type": document_type,
                                "source_tier": "official",
                                "source_url": document_url,
                                "source_authority": (
                                    "Official company IR"
                                    if filing["form"] == "IR"
                                    else "SEC EDGAR"
                                ),
                                "sha256": digest,
                                "size_bytes": len(body),
                                "mime_type": content_type,
                                "period_end": period["period_end"],
                                "currency": company["currency"],
                                "accounting_basis": company["accounting_basis"],
                                "retrieved_at": manifest["retrieved_at"],
                                "validation_status": "verified",
                            }
                        if filing["form"] != "IR":
                            entry.update(
                                {
                                    "filing_form": filing["form"],
                                    "accession_number": filing["accession_number"],
                                    "filing_date": filing["filing_date"],
                                }
                            )
                        # Drop prior stub entries for the same filing role.
                        manifest["files"] = [
                            old
                            for old in manifest["files"]
                            if not (
                                old.get("type") == document_type
                                and old.get("accession_number")
                                == entry.get("accession_number")
                                and old.get("sha256") != digest
                                and old.get("size_bytes", 0) < 50_000
                            )
                        ]
                        merge_file_entry(manifest, entry)
                    except Exception as exc:
                        counts["failed"] += 1
                        manifest["pending_sources"].append(
                            {
                                "type": document["document_type"],
                                "status": "download_failed",
                                "source_url": document_url,
                                "error": str(exc),
                            }
                        )
            has_regulatory = "regulatory_filing" in found_types or "6-K" in filing_forms
            if not has_regulatory:
                manifest["pending_sources"].append(
                    {
                        "type": "regulatory_filing",
                        "status": "not_filed_or_not_located_as_of_catalog",
                    }
                )
            has_earnings_material = bool(
                found_types.intersection(
                {"earnings_release", "earnings_presentation", "shareholder_update"}
                )
            ) or "6-K" in filing_forms
            if not has_earnings_material:
                manifest["pending_sources"].append(
                    {
                        "type": "official_earnings_material",
                        "status": "not_located_in_sec_package",
                        "checked_url": company["ir_url"],
                    }
                )
            if ticker in {"CLSK", "GOOG"} and "official_transcript" not in found_types:
                manifest["pending_sources"].append(
                    {
                        "type": "official_transcript",
                        "status": "not_located_in_official_catalog",
                        "checked_url": company["ir_url"],
                    }
                )
            if (
                ticker in {"AMD", "CLSK", "IREN", "NOK", "RDW", "RKLB", "TSLA"}
                and not found_types.intersection(
                    {"earnings_presentation", "shareholder_update"}
                )
                and not any(
                    item.get("type")
                    in {"earnings_presentation", "earnings_presentation_or_update"}
                    for item in manifest["unavailable_sources"]
                )
            ):
                manifest["pending_sources"].append(
                    {
                        "type": "earnings_presentation_or_update",
                        "status": "not_located_in_official_catalog",
                        "checked_url": company["ir_url"],
                    }
                )
            manifest["files"] = sorted(
                manifest["files"], key=lambda entry: entry["path"].casefold()
            )
            manifest["validation_status"] = (
                "complete" if not manifest["pending_sources"] else "partial"
            )
            target_directory.mkdir(parents=True, exist_ok=True)
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    if staging_root.exists():
        shutil.rmtree(staging_root)
    return counts


def filter_catalog(
    catalog: dict[str, Any],
    tickers: set[str] | None,
    labels: set[str] | None,
) -> dict[str, Any]:
    if not tickers and not labels:
        return catalog
    filtered = {**catalog, "companies": {}}
    for ticker, company in catalog["companies"].items():
        if tickers and ticker not in tickers:
            continue
        periods = [
            period
            for period in company["periods"]
            if not labels or period["label"] in labels
        ]
        if periods:
            filtered["companies"][ticker] = {**company, "periods": periods}
    return filtered


def apply_ir_supplements(
    catalog: dict[str, Any], supplement_path: Path
) -> dict[str, Any]:
    if not supplement_path.exists():
        return catalog
    supplements = yaml.safe_load(supplement_path.read_text(encoding="utf-8"))
    for ticker, period_map in supplements.get("companies", {}).items():
        company = catalog.get("companies", {}).get(ticker)
        if not company:
            continue
        by_label = {period["label"]: period for period in company["periods"]}
        for label, additions in period_map.items():
            period = by_label.get(label)
            if not period:
                continue
            ir_documents = period.setdefault("ir_documents", [])
            known_urls = {document["url"] for document in ir_documents}
            for document in additions.get("documents", []):
                if document["url"] in known_urls:
                    continue
                ir_documents.append(
                    {
                        "url": document["url"],
                        "name": Path(
                            urllib.parse.urlparse(document["url"]).path
                        ).name
                        or document["type"],
                        "description": document["type"].replace("_", " "),
                        "type": "IR",
                        "document_type": document["type"],
                    }
                )
                known_urls.add(document["url"])
            for override in additions.get("overrides", []):
                for filing in period.get("filings", []):
                    for document in filing.get("documents", []):
                        if document["url"] == override["url"]:
                            document["document_type"] = override["type"]
                for document in ir_documents:
                    if document["url"] == override["url"]:
                        document["document_type"] = override["type"]
            existing_unavailable = {
                (item.get("type"), item.get("status"))
                for item in period.setdefault("unavailable_sources", [])
            }
            for unavailable in additions.get("unavailable", []):
                key = (unavailable.get("type"), unavailable.get("status"))
                if key not in existing_unavailable:
                    period["unavailable_sources"].append(unavailable)
                    existing_unavailable.add(key)
    return catalog


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("config/official_sources.yaml"))
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path("data/source-catalog/holdings-six-quarters.json"),
    )
    parser.add_argument("--root", type=Path, default=Path("data/raw"))
    parser.add_argument("--ticker", action="append", help="Limit to ticker; repeatable")
    parser.add_argument("--period", action="append", help="Limit to period label; repeatable")
    parser.add_argument(
        "--catalog-only", action="store_true", help="Build catalog without downloading documents"
    )
    parser.add_argument(
        "--use-existing-catalog", action="store_true", help="Skip SEC discovery"
    )
    parser.add_argument(
        "--refresh-ir-only",
        action="store_true",
        help="Refresh IR links in the existing catalog without querying SEC",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print scope without writing")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_root = Path(__file__).resolve().parents[1]
    load_dotenv(project_root / ".env")
    config = yaml.safe_load((project_root / args.config).read_text(encoding="utf-8"))
    tickers = set(args.ticker) if args.ticker else None
    labels = set(args.period) if args.period else None
    selected = {
        ticker: company
        for ticker, company in config["companies"].items()
        if not tickers or ticker in tickers
    }
    scope = sum(
        1
        for company in selected.values()
        for period in company["periods"]
        if not labels or period["label"] in labels
    )
    if args.dry_run:
        print(json.dumps({"tickers": sorted(selected), "periods": scope}, indent=2))
        return 0

    user_agent = os.environ.get("SEC_USER_AGENT", "")
    downloader = OfficialDownloader(
        user_agent, config["sec"].get("requests_per_second", 2)
    )
    catalog_path = project_root / args.catalog
    if args.refresh_ir_only:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        discovered = 0
        for ticker, company in catalog["companies"].items():
            if tickers and ticker not in tickers:
                continue
            links = discover_ir_links(downloader, company["ir_url"])
            for period in company["periods"]:
                if labels and period["label"] not in labels:
                    continue
                period["ir_documents"] = ir_links_for_period(links, period)
                discovered += len(period["ir_documents"])
        catalog = apply_ir_supplements(
            catalog, project_root / "config" / "ir_supplements.yaml"
        )
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Discovered {discovered} matching IR links in {catalog_path}")
        return 0
    if args.use_existing_catalog:
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog = apply_ir_supplements(
            catalog, project_root / "config" / "ir_supplements.yaml"
        )
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        catalog = filter_catalog(catalog, tickers, labels)
    else:
        catalog = build_catalog(downloader, config, tickers, labels)
        catalog = apply_ir_supplements(
            catalog, project_root / "config" / "ir_supplements.yaml"
        )
        catalog_path.parent.mkdir(parents=True, exist_ok=True)
        catalog_path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    if args.catalog_only:
        print(f"Cataloged {scope} periods at {catalog_path}")
        return 0
    counts = download_catalog(downloader, catalog, project_root / args.root)
    print(json.dumps(counts, indent=2))
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
