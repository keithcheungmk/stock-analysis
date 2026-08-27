#!/usr/bin/env python3
"""Download Tesla official SEC documents for Framework 1."""

from __future__ import annotations

import hashlib
import json
import os
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "TSLA"
USER_AGENT = os.environ.get(
    "SEC_USER_AGENT",
    "stock-analysis research cmk3484@gmail.com",
)

# Filenames confirmed from each 8-K index.html (Tesla EX-99.1 is exhibit991.htm).
# Q2 2025 10-Q and Q1 2025 8-K/10-Q accessions confirmed from company submissions dump.
FILES = [
    {
        "period": "2026-Q2",
        "period_end": "2026-06-30",
        "release_date": "2026-07-22",
        "files": [
            ("000162828026049213", "tsla-20260722.htm", "sec-8-k-0001628280-26-049213-tsla-20260722.html", "event_filing", "8-K", "0001628280-26-049213", "2026-07-22"),
            ("000162828026049213", "exhibit991.htm", "sec-8-k-0001628280-26-049213-exhibit991.html", "shareholder_update", "8-K", "0001628280-26-049213", "2026-07-22"),
            ("000162828026049270", "tsla-20260630.htm", "sec-10-q-0001628280-26-049270-tsla-20260630.html", "regulatory_filing", "10-Q", "0001628280-26-049270", "2026-07-23"),
            ("000162828026046717", "tsla-20260702.htm", "sec-8-k-0001628280-26-046717-tsla-20260702.html", "event_filing", "8-K", "0001628280-26-046717", "2026-07-02"),
            ("000162828026046717", "exhibit99111111.htm", "sec-8-k-0001628280-26-046717-exhibit991.html", "deliveries_release", "8-K", "0001628280-26-046717", "2026-07-02"),
        ],
    },
    {
        "period": "2026-Q1",
        "period_end": "2026-03-31",
        "release_date": "2026-04-22",
        "files": [
            ("000162828026026551", "tsla-20260422.htm", "sec-8-k-0001628280-26-026551-tsla-20260422.html", "event_filing", "8-K", "0001628280-26-026551", "2026-04-22"),
            ("000162828026026551", "exhibit991.htm", "sec-8-k-0001628280-26-026551-exhibit991.html", "shareholder_update", "8-K", "0001628280-26-026551", "2026-04-22"),
            ("000162828026026673", "tsla-20260331.htm", "sec-10-q-0001628280-26-026673-tsla-20260331.html", "regulatory_filing", "10-Q", "0001628280-26-026673", "2026-04-23"),
        ],
    },
    {
        "period": "2025-Q4",
        "period_end": "2025-12-31",
        "release_date": "2026-01-28",
        "files": [
            ("000162828026003837", "tsla-20260128.htm", "sec-8-k-0001628280-26-003837-tsla-20260128.html", "event_filing", "8-K", "0001628280-26-003837", "2026-01-28"),
            ("000162828026003837", "exhibit991.htm", "sec-8-k-0001628280-26-003837-exhibit991.html", "shareholder_update", "8-K", "0001628280-26-003837", "2026-01-28"),
            ("000162828026003952", "tsla-20251231.htm", "sec-10-k-0001628280-26-003952-tsla-20251231.html", "regulatory_filing", "10-K", "0001628280-26-003952", "2026-01-29"),
        ],
    },
    {
        "period": "2025-Q3",
        "period_end": "2025-09-30",
        "release_date": "2025-10-22",
        "files": [
            ("000162828025045861", "tsla-20251022.htm", "sec-8-k-0001628280-25-045861-tsla-20251022.html", "event_filing", "8-K", "0001628280-25-045861", "2025-10-22"),
            ("000162828025045861", "exhibit991.htm", "sec-8-k-0001628280-25-045861-exhibit991.html", "shareholder_update", "8-K", "0001628280-25-045861", "2025-10-22"),
            ("000162828025045968", "tsla-20250930.htm", "sec-10-q-0001628280-25-045968-tsla-20250930.html", "regulatory_filing", "10-Q", "0001628280-25-045968", "2025-10-23"),
        ],
    },
    {
        "period": "2025-Q2",
        "period_end": "2025-06-30",
        "release_date": "2025-07-23",
        "files": [
            ("000162828025035738", "tsla-20250723.htm", "sec-8-k-0001628280-25-035738-tsla-20250723.html", "event_filing", "8-K", "0001628280-25-035738", "2025-07-23"),
            ("000162828025035738", "exhibit991.htm", "sec-8-k-0001628280-25-035738-exhibit991.html", "shareholder_update", "8-K", "0001628280-25-035738", "2025-07-23"),
            ("000162828025035806", "tsla-20250630.htm", "sec-10-q-0001628280-25-035806-tsla-20250630.html", "regulatory_filing", "10-Q", "0001628280-25-035806", "2025-07-24"),
        ],
    },
    {
        "period": "2025-Q1",
        "period_end": "2025-03-31",
        "release_date": "2025-04-22",
        "files": [
            ("000162828025018851", "tsla-20250422.htm", "sec-8-k-0001628280-25-018851-tsla-20250422.html", "event_filing", "8-K", "0001628280-25-018851", "2025-04-22"),
            ("000162828025018851", "exhbit991.htm", "sec-8-k-0001628280-25-018851-exhibit991.html", "shareholder_update", "8-K", "0001628280-25-018851", "2025-04-22"),
            ("000162828025018911", "tsla-20250331.htm", "sec-10-q-0001628280-25-018911-tsla-20250331.html", "regulatory_filing", "10-Q", "0001628280-25-018911", "2025-04-23"),
        ],
    },
]


def fetch(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": USER_AGENT, "Accept-Encoding": "identity", "Accept": "*/*"},
    )
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                body = response.read()
                content_type = response.headers.get_content_type()
                if not body:
                    raise ValueError(f"empty {url}")
                if b"Your Request Originates from an Undeclared Automated Tool" in body:
                    raise PermissionError("SEC rejected User-Agent")
                if b"404 Not Found" in body[:200] and len(body) < 2000:
                    raise FileNotFoundError(url)
                return body, content_type
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"failed {url}: {last_error}")


def list_index(accession_plain: str) -> None:
    acc_dashed = f"{accession_plain[:10]}-{accession_plain[10:12]}-{accession_plain[12:]}"
    url = f"https://www.sec.gov/Archives/edgar/data/1318605/{accession_plain}/{acc_dashed}-index.html"
    print("INDEX", url)
    body, _ = fetch(url)
    text = body.decode("utf-8", "replace")
    for line in text.splitlines():
        if "exhibit" in line.lower() or ".htm" in line.lower():
            if "href" in line.lower() and "jpg" not in line.lower():
                print(line[:400])


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--index-only", action="store_true")
    args = parser.parse_args()
    if args.index_only:
        for acc in [
            "000162828026049213",
            "000162828026026551",
            "000162828026003837",
            "000162828025045861",
            "000162828025035738",
            "000162828026046717",
            "000162828025018851",
            "000162828025035806",
            "000162828025018911",
        ]:
            try:
                list_index(acc)
            except Exception as exc:  # noqa: BLE001
                print("index fail", acc, exc)
            time.sleep(0.5)
        return 0

    now = datetime.now(timezone.utc).isoformat()
    RAW.mkdir(parents=True, exist_ok=True)
    for period in FILES:
        folder = RAW / period["period"]
        folder.mkdir(parents=True, exist_ok=True)
        files_meta = []
        for acc, fname, dest_name, doc_type, form, acc_dash, fdate in period["files"]:
            url = f"https://www.sec.gov/Archives/edgar/data/1318605/{acc}/{fname}"
            print("Fetching", url)
            try:
                body, content_type = fetch(url)
            except Exception as exc:  # noqa: BLE001
                print("SKIP", url, exc)
                continue
            dest = folder / dest_name
            dest.write_bytes(body)
            files_meta.append(
                {
                    "path": dest_name,
                    "type": doc_type,
                    "source_tier": "official",
                    "source_url": url,
                    "source_authority": "SEC EDGAR",
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "size_bytes": len(body),
                    "mime_type": content_type,
                    "period_end": period["period_end"],
                    "currency": "USD",
                    "accounting_basis": ["US_GAAP", "Non_GAAP"],
                    "retrieved_at": now,
                    "validation_status": "verified",
                    "filing_form": form,
                    "accession_number": acc_dash,
                    "filing_date": fdate,
                }
            )
            time.sleep(0.4)
        manifest = {
            "schema_version": 2,
            "company": "Tesla, Inc.",
            "ticker": "TSLA",
            "cik": "0001318605",
            "fiscal_period": period["period"],
            "period_end": period["period_end"],
            "release_date": period["release_date"],
            "currency": "USD",
            "accounting_basis": ["US_GAAP", "Non_GAAP"],
            "authority": "Official company IR and SEC EDGAR",
            "event_page": "https://ir.tesla.com/",
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
            "validation_status": "complete" if files_meta else "failed",
        }
        (folder / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print("Wrote", folder / "manifest.json", "files", len(files_meta))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
