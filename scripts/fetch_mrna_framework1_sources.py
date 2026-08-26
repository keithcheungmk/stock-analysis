#!/usr/bin/env python3
"""Download Moderna official SEC/IR documents for Framework 1 and write manifests."""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "MRNA"
USER_AGENT = os.environ.get(
    "SEC_USER_AGENT",
    "stock-analysis research cmk3484@gmail.com",
)

DOCUMENTS = [
    {
        "period": "2026-Q2",
        "period_end": "2026-06-30",
        "release_date": "2026-07-31",
        "files": [
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000147/mrna-20260731.htm",
                "path": "sec-8-k-0001682852-26-000147-mrna-20260731.html",
                "type": "event_filing",
                "form": "8-K",
                "accession": "0001682852-26-000147",
                "filing_date": "2026-07-31",
            },
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000147/exhibit9912026q2pressrelea.htm",
                "path": "sec-8-k-0001682852-26-000147-exhibit9912026q2pressrelea.html",
                "type": "earnings_release",
                "form": "8-K",
                "accession": "0001682852-26-000147",
                "filing_date": "2026-07-31",
            },
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000150/mrna-20260630.htm",
                "path": "sec-10-q-0001682852-26-000150-mrna-20260630.html",
                "type": "regulatory_filing",
                "form": "10-Q",
                "accession": "0001682852-26-000150",
                "filing_date": "2026-07-31",
            },
        ],
    },
    {
        "period": "2026-Q1",
        "period_end": "2026-03-31",
        "release_date": "2026-05-01",
        "files": [
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000057/exhibit9912026q1pressrelea.htm",
                "path": "sec-8-k-0001682852-26-000057-exhibit9912026q1pressrelea.html",
                "type": "earnings_release",
                "form": "8-K",
                "accession": "0001682852-26-000057",
                "filing_date": "2026-05-01",
            },
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000060/mrna-20260331.htm",
                "path": "sec-10-q-0001682852-26-000060-mrna-20260331.html",
                "type": "regulatory_filing",
                "form": "10-Q",
                "accession": "0001682852-26-000060",
                "filing_date": "2026-05-01",
            },
        ],
    },
    {
        "period": "2025-Q4",
        "period_end": "2025-12-31",
        "release_date": "2026-02-13",
        "files": [
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000015/exhibit9912025q4pressrelea.htm",
                "path": "sec-8-k-0001682852-26-000015-exhibit9912025q4pressrelea.html",
                "type": "earnings_release",
                "form": "8-K",
                "accession": "0001682852-26-000015",
                "filing_date": "2026-02-13",
            },
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285226000033/mrna-20251231.htm",
                "path": "sec-10-k-0001682852-26-000033-mrna-20251231.html",
                "type": "regulatory_filing",
                "form": "10-K",
                "accession": "0001682852-26-000033",
                "filing_date": "2026-02-20",
            },
        ],
    },
    {
        "period": "2025-Q3",
        "period_end": "2025-09-30",
        "release_date": "2025-11-06",
        "files": [
            {
                "url": "https://www.sec.gov/Archives/edgar/data/1682852/000168285225000073/exhibit9912025q3pressrelea.htm",
                "path": "sec-8-k-0001682852-25-000073-exhibit9912025q3pressrelea.html",
                "type": "earnings_release",
                "form": "8-K",
                "accession": "0001682852-25-000073",
                "filing_date": "2025-11-06",
            },
        ],
    },
    {
        "period": "_events",
        "period_end": "2026-08-05",
        "release_date": "2026-08-05",
        "files": [
            {
                "url": "https://www.modernatx.com/ir-insights-mflusiva",
                "path": "ir-mflusiva-fda-approval-2026-08-05.html",
                "type": "ir_event",
                "form": None,
                "accession": None,
                "filing_date": "2026-08-05",
            },
            {
                "url": "https://www.merck.com/news/merck-and-moderna-announce-phase-3-interpath-001-trial-of-intismeran-autogene-plus-keytruda-met-endpoints-of-recurrence-free-survival-rfs-and-distant-metastasis-free-survival-dmfs-in-patient/",
                "path": "ir-merck-moderna-interpath-001-phase3-2026-08-19.html",
                "type": "ir_event",
                "form": None,
                "accession": None,
                "filing_date": "2026-08-19",
            },
        ],
    },
]


def fetch(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Encoding": "identity",
            "Accept": "*/*",
        },
    )
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                body = response.read()
                content_type = response.headers.get_content_type()
                if not body:
                    raise ValueError(f"empty response from {url}")
                if b"Your Request Originates from an Undeclared Automated Tool" in body:
                    raise PermissionError("SEC rejected the declared User-Agent")
                return body, content_type
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    now = datetime.now(timezone.utc).isoformat()
    RAW.mkdir(parents=True, exist_ok=True)
    for period in DOCUMENTS:
        folder = RAW / period["period"]
        folder.mkdir(parents=True, exist_ok=True)
        files_meta = []
        for item in period["files"]:
            print(f"Fetching {item['url']}")
            body, content_type = fetch(item["url"])
            dest = folder / item["path"]
            dest.write_bytes(body)
            meta = {
                "path": item["path"],
                "type": item["type"],
                "source_tier": "official",
                "source_url": item["url"],
                "source_authority": (
                    "Official company IR" if "modernatx.com" in item["url"] else "SEC EDGAR"
                ),
                "sha256": sha256_bytes(body),
                "size_bytes": len(body),
                "mime_type": content_type,
                "period_end": period["period_end"],
                "currency": "USD",
                "accounting_basis": ["US_GAAP"],
                "retrieved_at": now,
                "validation_status": "verified",
            }
            if item.get("form"):
                meta["filing_form"] = item["form"]
            if item.get("accession"):
                meta["accession_number"] = item["accession"]
            if item.get("filing_date"):
                meta["filing_date"] = item["filing_date"]
            files_meta.append(meta)
            time.sleep(0.6)
        manifest = {
            "schema_version": 2,
            "company": "Moderna, Inc.",
            "ticker": "MRNA",
            "cik": "0001682852",
            "fiscal_period": period["period"],
            "period_end": period["period_end"],
            "release_date": period["release_date"],
            "currency": "USD",
            "accounting_basis": ["US_GAAP"],
            "authority": "Official company IR and SEC EDGAR",
            "event_page": "https://investors.modernatx.com/",
            "retrieved_at": now,
            "files": files_meta,
            "pending_sources": [],
            "unavailable_sources": [
                {
                    "type": "official_transcript",
                    "status": "not_part_of_standard_official_package",
                    "substitute": "webcast_metadata",
                }
            ],
            "validation_status": "complete" if period["period"] != "2025-Q3" else "partial",
        }
        (folder / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote {folder / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
