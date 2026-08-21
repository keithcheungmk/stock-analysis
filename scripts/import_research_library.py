#!/usr/bin/env python3
"""Safely migrate a research-library copy into the project raw-data layout."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import unicodedata
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


PRIVATE_FILES = {
    "ActivityStatement.20260529.pdf",
    "IB statement 260526.pdf",
}
LOOSE_TICKERS = {
    "CLPT": "CLPT",
    "CSIQ": "CSIQ",
    "GOOG": "GOOG",
}
FRAMEWORK_TERMS = (
    "framework",
    "skill",
    "thesis tracker",
    "valuation_model",
    "股票基本面",
    "成長股",
    "gu-piao",
)
SECTOR_TERMS = {
    "ai-datacenter": ("neocloud", "data centre", "situationalawareness"),
    "semiconductors": ("semi conductor", "semiconductor"),
    "macro": ("jpmorganoutlook", "investing opportunities"),
}
ANALYSIS_ARTIFACT_TERMS = ("dashboard", "deep_analysis", "catalyst_calendar")


@dataclass
class MigrationItem:
    source: str
    destination: str
    category: str
    ticker: str | None
    period: str | None
    period_confidence: str
    size_bytes: int
    sha256: str
    action: str
    duplicate_of: str | None = None
    status: str = "planned"
    error: str | None = None


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_filename(name: str) -> str:
    stem = unicodedata.normalize("NFKC", Path(name).stem).strip()
    suffix = Path(name).suffix.lower()
    stem = stem.replace("&", " and ")
    stem = re.sub(r"[^\w\u3400-\u9fff]+", "-", stem, flags=re.UNICODE)
    stem = re.sub(r"-{2,}", "-", stem).strip("-_.").lower()
    return f"{stem or 'document'}{suffix}"


def four_digit_year(value: str) -> int:
    year = int(value)
    return 2000 + year if year < 100 else year


def infer_period(name: str) -> tuple[str, str]:
    text = unicodedata.normalize("NFKC", name)
    quarter_patterns = (
        r"(?P<year>20\d{2})[\s._'-]*q(?P<quarter>[1-4])",
        r"q(?P<quarter>[1-4])[\s._'-]*(?:fy)?(?P<year>\d{2,4})",
        r"(?P<quarter>[1-4])q[\s._'-]*(?P<year>\d{2,4})",
        r"(?P<year>20\d{2})[\s._'-]*(?P<quarter>[1-4])q",
    )
    for pattern in quarter_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return (
                f"{four_digit_year(match.group('year'))}-Q{match.group('quarter')}",
                "high",
            )

    year_match = re.search(r"\b(20\d{2})\b", text)
    if year_match and re.search(r"\b(10[\s-]?k|annual|fy)\b", text, re.IGNORECASE):
        return f"FY{year_match.group(1)}", "medium"
    return "_unsorted", "low"


def classify(
    source: Path,
    source_root: Path,
    destination_root: Path,
    private_root: Path,
) -> tuple[Path, str, str | None, str | None, str]:
    relative = source.relative_to(source_root)
    parts = relative.parts
    basename = source.name
    lower_name = basename.lower()

    if basename in PRIVATE_FILES:
        return private_root / safe_filename(basename), "private", None, None, "high"

    if source.suffix.lower() in {".html", ".jsx"} and any(
        term in lower_name for term in ANALYSIS_ARTIFACT_TERMS
    ):
        ticker = parts[0].upper() if len(parts) > 1 else None
        output_name = f"{ticker.lower()}-{safe_filename(basename)}" if ticker else safe_filename(basename)
        return (
            destination_root.parent.parent / "output" / "imported" / output_name,
            "analysis_artifact",
            ticker,
            None,
            "high",
        )

    if any(term in lower_name for term in FRAMEWORK_TERMS):
        return (
            destination_root / "_framework" / "source-documents" / safe_filename(basename),
            "framework",
            None,
            None,
            "high",
        )

    if len(parts) == 1:
        for ticker_prefix, ticker in LOOSE_TICKERS.items():
            if basename.upper().startswith(ticker_prefix):
                period, confidence = infer_period(basename)
                return (
                    destination_root / ticker / period / safe_filename(basename),
                    "ticker",
                    ticker,
                    period,
                    confidence,
                )
        for sector, terms in SECTOR_TERMS.items():
            if any(term in lower_name for term in terms):
                return (
                    destination_root / "_sector" / sector / safe_filename(basename),
                    "sector",
                    None,
                    None,
                    "medium",
                )
        return (
            destination_root / "_unclassified" / safe_filename(basename),
            "unclassified",
            None,
            None,
            "low",
        )

    top = parts[0]
    if top == "CLSK-CRWV-IREN":
        if len(parts) > 2 and parts[1].upper() == "IREN":
            ticker = "IREN"
        elif lower_name.startswith("clsk"):
            ticker = "CLSK"
        elif lower_name.startswith("crwv"):
            ticker = "CRWV"
        elif lower_name.startswith("iren"):
            ticker = "IREN"
        else:
            return (
                destination_root
                / "_basket"
                / "neocloud-clsk-crwv-iren"
                / safe_filename(basename),
                "basket",
                None,
                None,
                "medium",
            )
    elif top == "Metaplanet":
        ticker = "3350.T"
    else:
        ticker = top.upper()

    if ticker == "HIMS" and "project location map" in lower_name:
        return (
            destination_root / "_unclassified" / "hims" / safe_filename(basename),
            "unclassified",
            ticker,
            None,
            "high",
        )

    period, confidence = infer_period(basename)
    return (
        destination_root / ticker / period / safe_filename(basename),
        "ticker",
        ticker,
        period,
        confidence,
    )


def resolve_collisions(items: list[MigrationItem]) -> None:
    by_destination: dict[str, list[MigrationItem]] = defaultdict(list)
    for item in items:
        if item.action != "deduplicate":
            by_destination[item.destination].append(item)

    for destination, conflicts in by_destination.items():
        hashes = {item.sha256 for item in conflicts}
        if len(conflicts) < 2 or len(hashes) == 1:
            continue
        path = Path(destination)
        for item in conflicts[1:]:
            item.destination = str(
                path.with_name(f"{path.stem}--{item.sha256[:8]}{path.suffix}")
            )


def build_inventory(
    source_root: Path, destination_root: Path, private_root: Path
) -> list[MigrationItem]:
    records: list[MigrationItem] = []
    canonical_by_hash: dict[str, MigrationItem] = {}
    files = sorted(
        (
            path
            for path in source_root.rglob("*")
            if path.is_file() and path.name != ".DS_Store"
        ),
        key=lambda path: str(path.relative_to(source_root)).casefold(),
    )

    for source in files:
        digest = sha256_file(source)
        destination, category, ticker, period, confidence = classify(
            source, source_root, destination_root, private_root
        )
        record = MigrationItem(
            source=str(source),
            destination=str(destination),
            category=category,
            ticker=ticker,
            period=period,
            period_confidence=confidence,
            size_bytes=source.stat().st_size,
            sha256=digest,
            action="move",
        )
        if digest in canonical_by_hash:
            canonical = canonical_by_hash[digest]
            record.action = "deduplicate"
            record.destination = canonical.destination
            record.duplicate_of = canonical.source
        else:
            canonical_by_hash[digest] = record
        records.append(record)

    resolve_collisions(records)
    return records


def write_ledger(records: list[MigrationItem], output_base: Path) -> tuple[Path, Path]:
    output_base.parent.mkdir(parents=True, exist_ok=True)
    json_path = output_base.with_suffix(".json")
    csv_path = output_base.with_suffix(".csv")
    payload = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": summarize(records),
        "files": [asdict(record) for record in records],
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MigrationItem.__dataclass_fields__)
        writer.writeheader()
        writer.writerows(asdict(record) for record in records)
    return json_path, csv_path


def summarize(records: list[MigrationItem]) -> dict[str, object]:
    statuses: dict[str, int] = defaultdict(int)
    categories: dict[str, int] = defaultdict(int)
    for record in records:
        statuses[record.status] += 1
        categories[record.category] += 1
    return {
        "file_count": len(records),
        "size_bytes": sum(record.size_bytes for record in records),
        "duplicate_count": sum(record.action == "deduplicate" for record in records),
        "status_counts": dict(sorted(statuses.items())),
        "category_counts": dict(sorted(categories.items())),
    }


def document_type(path: Path) -> str:
    name = path.name.lower()
    if re.search(r"10[\s-]?[qk]", name):
        return "regulatory_filing"
    if "transcript" in name:
        return "earnings_transcript"
    if "presentation" in name or "slides" in name:
        return "presentation"
    if "annual report" in name:
        return "annual_report"
    if "investing" in name and ("pro" in name or "research" in name):
        return "third_party_research"
    if "framework" in name or "skill" in name:
        return "research_framework"
    if path.suffix.lower() in {".jpeg", ".jpg", ".png"}:
        return "reference_image"
    return "research_document"


def source_tier(path: Path) -> str:
    name = path.name.lower()
    if "investing" in name or "research" in name:
        return "third_party"
    if re.search(r"10[\s-]?[qk]", name) or "annual report" in name:
        return "official"
    return "unverified"


def update_manifests(
    records: list[MigrationItem], destination_root: Path, source_root: Path
) -> None:
    grouped: dict[Path, list[MigrationItem]] = defaultdict(list)
    for record in records:
        destination = Path(record.destination)
        if (
            record.action != "deduplicate"
            and record.status in {"moved", "already_present"}
            and destination.is_relative_to(destination_root)
        ):
            grouped[destination.parent].append(record)

    timestamp = datetime.now(timezone.utc).isoformat()
    for directory, directory_records in grouped.items():
        manifest_path = directory / "manifest.json"
        if manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        else:
            relative_directory = directory.relative_to(destination_root)
            manifest = {
                "schema_version": 1,
                "collection": str(relative_directory),
                "generated_at": timestamp,
                "authority": "Migrated local research library",
                "files": [],
            }

        files = manifest.setdefault("files", [])
        known_hashes = {
            item.get("sha256") for item in files if isinstance(item, dict)
        }
        for record in directory_records:
            if record.sha256 in known_hashes:
                continue
            destination = Path(record.destination)
            source = Path(record.source)
            try:
                original_path = str(source.relative_to(source_root))
            except ValueError:
                original_path = source.name
            files.append(
                {
                    "path": destination.name,
                    "type": document_type(destination),
                    "source_tier": source_tier(destination),
                    "source_url": None,
                    "source_original_path": original_path,
                    "sha256": record.sha256,
                    "size_bytes": destination.stat().st_size,
                    "imported_at": timestamp,
                    "period_confidence": record.period_confidence,
                }
            )
            known_hashes.add(record.sha256)
        manifest["files"] = sorted(files, key=lambda item: item["path"].casefold())
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )


def verify_copy(source: Path, destination: Path, expected_hash: str) -> None:
    if destination.stat().st_size != source.stat().st_size:
        raise ValueError("copied file size does not match source")
    if sha256_file(destination) != expected_hash:
        raise ValueError("copied file SHA-256 does not match source")


def migrate(records: list[MigrationItem], destination_root: Path) -> None:
    staging_root = destination_root.parent / ".migration-staging"
    successful_hashes: set[str] = set()

    for record in records:
        source = Path(record.source)
        destination = Path(record.destination)
        try:
            if record.action == "deduplicate":
                if record.sha256 not in successful_hashes and (
                    not destination.exists()
                    or sha256_file(destination) != record.sha256
                ):
                    raise ValueError("canonical duplicate has not been verified")
                source.unlink()
                record.status = "deduplicated"
                continue

            if destination.exists():
                if sha256_file(destination) != record.sha256:
                    raise FileExistsError(f"destination conflict: {destination}")
                source.unlink()
                record.status = "already_present"
                successful_hashes.add(record.sha256)
                continue

            try:
                relative_destination = destination.relative_to(destination_root.parent.parent)
            except ValueError:
                relative_destination = Path("private") / destination.name
            staged = staging_root / relative_destination
            staged.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, staged)
            verify_copy(source, staged, record.sha256)
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.replace(staged, destination)
            verify_copy(source, destination, record.sha256)
            source.unlink()
            record.status = "moved"
            successful_hashes.add(record.sha256)
        except Exception as exc:  # preserve source on every failure
            record.status = "failed"
            record.error = str(exc)

    if staging_root.exists():
        shutil.rmtree(staging_root)


def remove_empty_source_directories(source_root: Path) -> None:
    for metadata_file in source_root.rglob(".DS_Store"):
        metadata_file.unlink(missing_ok=True)
    for directory in sorted(
        (path for path in source_root.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        try:
            directory.rmdir()
        except OSError:
            pass
    try:
        source_root.rmdir()
    except OSError:
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--private-destination", type=Path, required=True)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Copy, verify, delete source files, and remove empty source directories.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.expanduser().resolve()
    destination = args.destination.expanduser().resolve()
    private_destination = args.private_destination.expanduser().resolve()
    records = build_inventory(source, destination, private_destination)
    if args.execute:
        migrate(records, destination)
        update_manifests(records, destination, source)
        remove_empty_source_directories(source)
    json_path, csv_path = write_ledger(records, args.ledger.expanduser().resolve())
    print(json.dumps(summarize(records), ensure_ascii=False, indent=2))
    print(f"JSON ledger: {json_path}")
    print(f"CSV ledger: {csv_path}")
    return 1 if any(record.status == "failed" for record in records) else 0


if __name__ == "__main__":
    raise SystemExit(main())
