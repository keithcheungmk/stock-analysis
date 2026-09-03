#!/usr/bin/env python3
"""Import manually downloaded official PDFs into verified quarter manifests."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


MAPPINGS = {
    "Q2 FY25 Results Presentation_iren.pdf": (
        "IREN",
        "FY2025-Q2",
        "earnings_presentation",
        "https://iren.gcs-web.com/static-files/a18dd174-516f-4896-bb2e-51254cff7d84",
    ),
    "Q3 FY25 Presentation_iren.pdf": (
        "IREN",
        "FY2025-Q3",
        "earnings_presentation",
        "https://iren.gcs-web.com/static-files/2de566f1-d74a-4164-b9c9-a40241ef81ce",
    ),
    "FY25 Results Presentation_iren.pdf": (
        "IREN",
        "FY2025-Q4",
        "earnings_presentation",
        "https://iren.gcs-web.com/static-files/d958d6f0-e143-4508-af15-da6c7e540598",
    ),
    "Q1 FY26 Results Presentation_iren.pdf": (
        "IREN",
        "FY2026-Q1",
        "earnings_presentation",
        "https://iren.gcs-web.com/static-files/e66d1f70-087a-43d4-9c06-4df25f119936",
    ),
    "Q2 FY26 Results Presentation_iren.pdf": (
        "IREN",
        "FY2026-Q2",
        "earnings_presentation",
        "https://iren.gcs-web.com/static-files/07e0b197-cf31-4158-a124-8ff0b70203c3",
    ),
    "Q3 FY26 Results Presentation_iren.pdf": (
        "IREN",
        "FY2026-Q3",
        "earnings_presentation",
        "https://iren.gcs-web.com/static-files/2289f56f-f0f8-4673-a7d4-2359afe93eb6",
    ),
    "Q2 2025 Earnings Presentation.pdf_with links.pdf": (
        "RKLB",
        "2025-Q2",
        "earnings_presentation",
        "https://investors.rocketlabcorp.com/static-files/815a4786-20f5-4f20-be8a-2bbfc8d75449",
    ),
    "Q3 2025 Earnings Presentation JpegSlides HR.pdf": (
        "RKLB",
        "2025-Q3",
        "earnings_presentation",
        "https://investors.rocketlabcorp.com/static-files/f2e2847c-5660-4b81-8bf7-709f61289898",
    ),
    "Q4 2025 Earnings Presentation_FINAL.pdf": (
        "RKLB",
        "2025-Q4",
        "earnings_presentation",
        "https://investors.rocketlabcorp.com/static-files/be9441ad-c07f-49c2-ad50-531fd77180ee",
    ),
    "RKLB Q1 2026 Earnings Presentation.pdf": (
        "RKLB",
        "2026-Q1",
        "earnings_presentation",
        "https://investors.rocketlabcorp.com/static-files/c0bd4327-c3ff-4843-8eae-8b0d8a4d4b82",
    ),
}

EXISTING_MAPPINGS = {
    "RKLB/2024-Q4/q4-2024-presentation.pdf": (
        "RKLB",
        "2024-Q4",
        "earnings_presentation",
        "https://investors.rocketlabcorp.com/static-files/16817498-fc1c-4f35-903e-7bdd7d421d8e",
    ),
    "RKLB/2025-Q1/q1-2025-presentation.pdf": (
        "RKLB",
        "2025-Q1",
        "earnings_presentation",
        "https://investors.rocketlabcorp.com/static-files/bbf2962a-dc50-4fe1-90e9-75caa0b8e68d",
    ),
}


# Files manually saved in the OneDrive inbox. Kaleidoscope PDFs are convenient
# rendered copies of SEC filings, so keep them as third-party copies rather than
# incorrectly promoting them above the canonical SEC HTML already in each period.
ARCHIVE_MAPPINGS = {
    "10q iren 08-28-2025.pdf": {
        "ticker": "IREN", "period": "FY2025-Q4", "destination": "third-party-filing-copy-10-k-2025-08-28.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-K", "filing_date": "2025-08-28", "source_url": None,
    },
    "10q iren 11-06-2025.pdf": {
        "ticker": "IREN", "period": "FY2026-Q1", "destination": "third-party-filing-copy-10-q-2025-11-06.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2025-11-06", "source_url": None,
    },
    "10q iren 02-05-2026.pdf": {
        "ticker": "IREN", "period": "FY2026-Q2", "destination": "third-party-filing-copy-10-q-2026-02-05.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2026-02-05", "source_url": None,
    },
    "10q iren 05-08-2026.pdf": {
        "ticker": "IREN", "period": "FY2026-Q3", "destination": "third-party-filing-copy-10-q-2026-05-08.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2026-05-08", "source_url": None,
    },
    "10q rklb 05-08-2025.pdf": {
        "ticker": "RKLB", "period": "2025-Q1", "destination": "third-party-filing-copy-10-q-2025-05-08.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2025-05-08", "source_url": None,
    },
    "10Q rklb 08-07-2025.pdf": {
        "ticker": "RKLB", "period": "2025-Q2", "destination": "third-party-filing-copy-10-q-2025-08-07.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2025-08-07", "source_url": None,
    },
    "form 10Q rklb 11-10-2025.pdf": {
        "ticker": "RKLB", "period": "2025-Q3", "destination": "third-party-filing-copy-10-q-2025-11-10.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2025-11-10", "source_url": None,
    },
    "form 10K rklb 26-02-2026.pdf": {
        "ticker": "RKLB", "period": "2025-Q4", "destination": "third-party-filing-copy-10-k-2026-02-26.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-K", "filing_date": "2026-02-26", "source_url": None,
    },
    "rklb_10Q filled 5-07-2026.pdf": {
        "ticker": "RKLB", "period": "2026-Q1", "destination": "third-party-filing-copy-10-q-2026-05-07.pdf",
        "document_type": "filing_copy", "source_tier": "third_party", "source_authority": "Kaleidoscope (kscope.io)",
        "filing_form": "10-Q", "filing_date": "2026-05-07", "source_url": None,
    },
    "Rocket Lab Announces First Quarter 2026 Financial Results_ Surpasses All Guidance Metrics Including Revenue, Margin, and Adjusted EBITDA; Posts Record $200M Quarterly Revenue and over $2.2B Backlog; Guides Another Record Revenue.pdf": {
        "ticker": "RKLB", "period": "2026-Q1", "destination": "ir-q1-2026-earnings-release.pdf",
        "document_type": "earnings_release", "source_tier": "official", "source_authority": "Official company IR",
        "filing_form": None, "filing_date": "2026-05-07", "source_url": "https://investors.rocketlabcorp.com/node/12416/pdf",
    },
    "Rocket Lab Iridium Acquisition Investor Presentation PDF.pdf": {
        "ticker": "RKLB", "period": "_events", "destination": "ir-iridium-acquisition-investor-presentation.pdf",
        "document_type": "investor_presentation", "source_tier": "official", "source_authority": "Official company IR",
        "filing_form": None, "filing_date": "2026-06-29", "source_url": "https://investors.rocketlabcorp.com/static-files/70a090f6-58db-4893-bfc0-c31396b152b1",
    },
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_pdf(path: Path) -> bool:
    with path.open("rb") as handle:
        return handle.read(5) == b"%PDF-"


def remove_resolved_pending(
    manifest: dict[str, Any], document_type: str, source_url: str
) -> None:
    manifest["pending_sources"] = [
        item
        for item in manifest.get("pending_sources", [])
        if not (
            item.get("source_url") == source_url
            or (
                document_type == "earnings_presentation"
                and item.get("type") == "earnings_presentation_or_update"
            )
        )
    ]


def import_file(
    source: Path,
    raw_root: Path,
    ticker: str,
    period: str,
    document_type: str,
    source_url: str,
) -> str:
    if not is_pdf(source):
        raise ValueError(f"{source.name}: not a valid PDF header")
    if source.stat().st_size < 1024:
        raise ValueError(f"{source.name}: PDF is unexpectedly small")
    digest = sha256_file(source)
    target_directory = raw_root / ticker / period
    manifest_path = target_directory / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    timestamp = datetime.now(timezone.utc).isoformat()

    existing = next(
        (entry for entry in manifest["files"] if entry.get("sha256") == digest),
        None,
    )
    if existing:
        destination = target_directory / existing["path"]
        source.unlink()
        status = "matched_existing"
    else:
        destination = target_directory / f"ir-{document_type}.pdf"
        if destination.exists() and sha256_file(destination) != digest:
            destination = destination.with_name(
                f"{destination.stem}--{digest[:8]}{destination.suffix}"
            )
        os.replace(source, destination)
        existing = {"path": destination.name}
        manifest["files"].append(existing)
        status = "imported"

    existing.update(
        {
            "type": document_type,
            "source_tier": "official",
            "source_url": source_url,
            "source_authority": "Official company IR",
            "sha256": digest,
            "size_bytes": destination.stat().st_size,
            "mime_type": "application/pdf",
            "period_end": manifest["period_end"],
            "currency": manifest["currency"],
            "accounting_basis": manifest["accounting_basis"],
            "retrieved_at": timestamp,
            "ingestion_method": "manual_browser_download",
            "validation_status": "verified",
        }
    )
    remove_resolved_pending(manifest, document_type, source_url)
    manifest["retrieved_at"] = timestamp
    manifest["validation_status"] = (
        "complete" if not manifest.get("pending_sources") else "partial"
    )
    manifest["files"] = sorted(
        manifest["files"], key=lambda entry: entry["path"].casefold()
    )
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return status


def archive_inbox_file(source: Path, raw_root: Path, mapping: dict[str, Any]) -> str:
    if not is_pdf(source):
        raise ValueError(f"{source.name}: not a valid PDF header")
    digest = sha256_file(source)
    target_directory = raw_root / mapping["ticker"] / mapping["period"]
    manifest_path = target_directory / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    timestamp = datetime.now(timezone.utc).isoformat()

    existing = next(
        (entry for entry in manifest["files"] if entry.get("sha256") == digest),
        None,
    )
    if existing:
        source.unlink()
        return "matched_existing"

    destination = target_directory / mapping["destination"]
    if destination.exists() and sha256_file(destination) != digest:
        destination = destination.with_name(
            f"{destination.stem}--{digest[:8]}{destination.suffix}"
        )
    os.replace(source, destination)
    entry = {
        "path": destination.name,
        "type": mapping["document_type"],
        "source_tier": mapping["source_tier"],
        "source_url": mapping["source_url"],
        "source_authority": mapping["source_authority"],
        "source_original_path": f"_manual-inbox/{source.name}",
        "sha256": digest,
        "size_bytes": destination.stat().st_size,
        "mime_type": "application/pdf",
        "filing_date": mapping["filing_date"],
        "imported_at": timestamp,
        "ingestion_method": "manual_inbox_reviewed",
        "validation_status": "verified",
    }
    for key in ("period_end", "currency", "accounting_basis"):
        if manifest.get(key) is not None:
            entry[key] = manifest[key]
    if mapping["filing_form"]:
        entry["filing_form"] = mapping["filing_form"]
    manifest["files"].append(entry)
    manifest["files"] = sorted(
        manifest["files"], key=lambda item: item["path"].casefold()
    )
    manifest["retrieved_at"] = timestamp
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return "imported"


def promote_existing(
    path: Path,
    raw_root: Path,
    ticker: str,
    period: str,
    document_type: str,
    source_url: str,
) -> bool:
    if not path.exists() or not is_pdf(path):
        return False
    manifest_path = raw_root / ticker / period / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    digest = sha256_file(path)
    entry = next(
        (
            item
            for item in manifest["files"]
            if item.get("path") == path.name or item.get("sha256") == digest
        ),
        None,
    )
    if not entry:
        return False
    timestamp = datetime.now(timezone.utc).isoformat()
    entry.update(
        {
            "type": document_type,
            "source_tier": "official",
            "source_url": source_url,
            "source_authority": "Official company IR",
            "sha256": digest,
            "size_bytes": path.stat().st_size,
            "mime_type": "application/pdf",
            "period_end": manifest["period_end"],
            "currency": manifest["currency"],
            "accounting_basis": manifest["accounting_basis"],
            "retrieved_at": timestamp,
            "ingestion_method": "existing_manual_download_reviewed",
            "validation_status": "verified",
        }
    )
    remove_resolved_pending(manifest, document_type, source_url)
    manifest["retrieved_at"] = timestamp
    manifest["validation_status"] = (
        "complete" if not manifest.get("pending_sources") else "partial"
    )
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return True


def reconcile_optional_sources(raw_root: Path, supplements_path: Path) -> int:
    supplements = yaml.safe_load(supplements_path.read_text(encoding="utf-8"))
    reconciled = 0
    for ticker, periods in supplements.get("companies", {}).items():
        for period, settings in periods.items():
            optional_documents = [
                document
                for document in settings.get("documents", [])
                if document.get("optional", False)
            ]
            if not optional_documents:
                continue
            manifest_path = raw_root / ticker / period / "manifest.json"
            if not manifest_path.exists():
                continue
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            optional_urls = {document["url"] for document in optional_documents}
            before = len(manifest.get("pending_sources", []))
            manifest["pending_sources"] = [
                item
                for item in manifest.get("pending_sources", [])
                if item.get("source_url") not in optional_urls
            ]
            reconciled += before - len(manifest["pending_sources"])
            known = {
                (item.get("type"), item.get("source_url"))
                for item in manifest.get("unavailable_sources", [])
            }
            for document in optional_documents:
                key = (document["type"], document["url"])
                if key not in known:
                    manifest.setdefault("unavailable_sources", []).append(
                        {
                            "type": document["type"],
                            "status": "optional_substituted_by_sec_filing_and_earnings_release",
                            "source_url": document["url"],
                        }
                    )
            manifest["validation_status"] = (
                "complete" if not manifest["pending_sources"] else "partial"
            )
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    return reconciled


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inbox", type=Path, default=Path("data/raw/_manual-inbox")
    )
    parser.add_argument("--root", type=Path, default=Path("data/raw"))
    parser.add_argument(
        "--supplements",
        type=Path,
        default=Path("config/ir_supplements.yaml"),
    )
    args = parser.parse_args()

    counts = {
        "imported": 0,
        "matched_existing": 0,
        "archived": 0,
        "promoted_existing": 0,
        "unmapped": 0,
    }
    for relative_path, mapping in EXISTING_MAPPINGS.items():
        if promote_existing(args.root / relative_path, args.root, *mapping):
            counts["promoted_existing"] += 1
            print(f"promoted_existing: {relative_path}")
    for source in sorted(args.inbox.glob("*.pdf")):
        archive_mapping = ARCHIVE_MAPPINGS.get(source.name)
        if archive_mapping:
            status = archive_inbox_file(source, args.root, archive_mapping)
            counts["archived" if status == "imported" else status] += 1
            print(
                f"{status}: {source.name} -> "
                f"{archive_mapping['ticker']}/{archive_mapping['period']}"
            )
            continue
        mapping = MAPPINGS.get(source.name)
        if not mapping:
            counts["unmapped"] += 1
            continue
        status = import_file(source, args.root, *mapping)
        counts[status] += 1
        print(f"{status}: {source.name} -> {mapping[0]}/{mapping[1]}")
    counts["optional_pending_reconciled"] = reconcile_optional_sources(
        args.root, args.supplements
    )
    print(json.dumps(counts, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
