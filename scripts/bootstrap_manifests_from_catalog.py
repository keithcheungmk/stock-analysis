#!/usr/bin/env python3
"""Bootstrap manifest.json from a six-quarter catalog when SEC download is unavailable.

Writes manifest metadata and SEC/IR source URLs. Local HTML bodies are not
fetched; run download_official_research.py on a machine with SEC_USER_AGENT
to populate files on disk and refresh sha256 hashes.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import yaml


def safe_name(value: str) -> str:
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", value).strip("-") or "document"


def file_entry(filing: dict, document: dict) -> dict:
    url = document["url"]
    name = document.get("name") or Path(urlparse(url).path).name or "document"
    authority = "ir" if filing.get("form") == "IR" else "sec"
    stem = Path(name).stem
    filename = safe_name(
        f"{authority}-{filing.get('form', 'DOC')}-{filing.get('accession_number', 'na')}-{stem}"
    ) + ".html"
    return {
        "path": filename,
        "type": document.get("document_type", "regulatory_filing"),
        "source_tier": "official",
        "source_url": url,
        "source_authority": "SEC EDGAR" if authority == "sec" else "Company IR",
        "validation_status": "verified",
        "mime_type": "text/html",
        "period_end": filing.get("report_date"),
        "filing_form": filing.get("form"),
        "accession_number": filing.get("accession_number"),
        "filing_date": filing.get("filing_date"),
        "catalog_note": "URL catalog snapshot; run download_official_research.py to fetch body and sha256",
    }


def bootstrap(catalog_path: Path, config_path: Path, root: Path) -> int:
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).isoformat()
    written = 0

    for ticker, company in catalog["companies"].items():
        company_cfg = config["companies"].get(ticker, {})
        periods_cfg = {
            p["label"]: p for p in company_cfg.get("periods", company["periods"])
        }
        for period in company["periods"]:
            label = period["label"]
            cfg_period = periods_cfg.get(label, period)
            target = root / ticker / label
            target.mkdir(parents=True, exist_ok=True)
            files: list[dict] = []
            filings = list(period.get("filings", []))
            if period.get("ir_documents"):
                filings.append(
                    {
                        "accession_number": "official-ir",
                        "form": "IR",
                        "filing_date": cfg_period.get("release_date"),
                        "report_date": period["period_end"],
                        "documents": period["ir_documents"],
                    }
                )
            for filing in filings:
                for document in filing.get("documents", []):
                    files.append(file_entry(filing, document))

            manifest = {
                "schema_version": 2,
                "company": company["name"],
                "ticker": ticker,
                "fiscal_period": label,
                "period_end": period["period_end"],
                "currency": company["currency"],
                "accounting_basis": company.get("accounting_basis", []),
                "cik": company["cik"],
                "authority": "Official company IR and SEC EDGAR",
                "event_page": company["ir_url"],
                "retrieved_at": now,
                "validation_status": "partial",
                "bootstrap": "catalog_snapshot",
                "files": sorted(files, key=lambda e: e["path"].casefold()),
                "unavailable_sources": period.get("unavailable_sources", []),
                "pending_sources": [
                    {
                        "reason": "local_body_not_fetched_in_bootstrap",
                        "hint": "Run scripts/download_official_research.py with SEC_USER_AGENT",
                    }
                ],
            }
            if cfg_period.get("release_date"):
                manifest["release_date"] = cfg_period["release_date"]

            (target / "manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            written += 1
    return written


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path("data/raw"))
    args = parser.parse_args()
    count = bootstrap(args.catalog, args.config, args.root)
    print(f"Bootstrapped {count} manifests under {args.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
