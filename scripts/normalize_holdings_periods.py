#!/usr/bin/env python3
"""Normalize known fiscal-period mistakes in the migrated holdings library."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_manifest(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def merge_period(source: Path, target: Path, ticker: str, label: str) -> None:
    if not source.exists():
        return
    source_manifest_path = source / "manifest.json"
    source_manifest = read_manifest(source_manifest_path)
    target.mkdir(parents=True, exist_ok=True)
    target_manifest_path = target / "manifest.json"
    if target_manifest_path.exists():
        target_manifest = read_manifest(target_manifest_path)
    else:
        target_manifest = {
            "schema_version": 1,
            "collection": f"{ticker}/{label}",
            "ticker": ticker,
            "fiscal_period": label,
            "authority": "Migrated local research library",
            "files": [],
        }
    known_hashes = {
        entry.get("sha256") for entry in target_manifest.get("files", [])
    }
    for entry in source_manifest.get("files", []):
        source_file = source / entry["path"]
        if entry.get("sha256") in known_hashes:
            source_file.unlink(missing_ok=True)
            continue
        destination = target / entry["path"]
        if destination.exists() and sha256_file(destination) != entry["sha256"]:
            destination = destination.with_name(
                f"{destination.stem}--{entry['sha256'][:8]}{destination.suffix}"
            )
            entry["path"] = destination.name
        os.replace(source_file, destination)
        target_manifest.setdefault("files", []).append(entry)
        known_hashes.add(entry.get("sha256"))
    target_manifest["collection"] = f"{ticker}/{label}"
    target_manifest["ticker"] = ticker
    target_manifest["fiscal_period"] = label
    target_manifest["files"] = sorted(
        target_manifest["files"], key=lambda entry: entry["path"].casefold()
    )
    target_manifest_path.write_text(
        json.dumps(target_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    source_manifest_path.unlink()
    source.rmdir()


def downgrade_unverifiable_official_entries(root: Path) -> int:
    changed_entries = 0
    for manifest_path in root.rglob("manifest.json"):
        manifest = read_manifest(manifest_path)
        changed = False
        for entry in manifest.get("files", []):
            if entry.get("source_tier") != "official":
                continue
            if (
                entry.get("source_url")
                and entry.get("validation_status") == "verified"
                and entry.get("mime_type")
            ):
                continue
            entry["source_tier"] = "unverified"
            entry["provenance_note"] = (
                "Legacy import lacked an official URL, MIME type, or verified status."
            )
            changed = True
            changed_entries += 1
        if changed:
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
    return changed_entries


def move_matching_entries(
    source: Path,
    target: Path,
    ticker: str,
    label: str,
    predicate,
) -> int:
    source_manifest_path = source / "manifest.json"
    if not source_manifest_path.exists():
        return 0
    source_manifest = read_manifest(source_manifest_path)
    selected = [entry for entry in source_manifest.get("files", []) if predicate(entry)]
    if not selected:
        return 0
    target.mkdir(parents=True, exist_ok=True)
    target_manifest_path = target / "manifest.json"
    if target_manifest_path.exists():
        target_manifest = read_manifest(target_manifest_path)
    else:
        target_manifest = {
            "schema_version": 1,
            "collection": f"{ticker}/{label}",
            "ticker": ticker,
            "fiscal_period": label,
            "authority": "Migrated local research library",
            "files": [],
        }
    known_hashes = {
        entry.get("sha256") for entry in target_manifest.get("files", [])
    }
    for entry in selected:
        source_file = source / entry["path"]
        if entry.get("sha256") in known_hashes:
            source_file.unlink(missing_ok=True)
        else:
            destination = target / entry["path"]
            if destination.exists() and sha256_file(destination) != entry["sha256"]:
                destination = destination.with_name(
                    f"{destination.stem}--{entry['sha256'][:8]}{destination.suffix}"
                )
                entry["path"] = destination.name
            os.replace(source_file, destination)
            target_manifest.setdefault("files", []).append(entry)
            known_hashes.add(entry.get("sha256"))
    selected_hashes = {entry.get("sha256") for entry in selected}
    source_manifest["files"] = [
        entry
        for entry in source_manifest.get("files", [])
        if entry.get("sha256") not in selected_hashes
    ]
    target_manifest["collection"] = f"{ticker}/{label}"
    target_manifest["ticker"] = ticker
    target_manifest["fiscal_period"] = label
    target_manifest["files"] = sorted(
        target_manifest["files"], key=lambda entry: entry["path"].casefold()
    )
    source_manifest_path.write_text(
        json.dumps(source_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    target_manifest_path.write_text(
        json.dumps(target_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return len(selected)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("data/raw"))
    args = parser.parse_args()
    root = args.root.resolve()

    for calendar_label, fiscal_label in {
        "2025-Q1": "FY2025-Q1",
        "2025-Q2": "FY2025-Q2",
        "2025-Q3": "FY2025-Q3",
        "2025-Q4": "FY2025-Q4",
        "2026-Q1": "FY2026-Q1",
        "2026-Q2": "FY2026-Q2",
        "2026-Q3": "FY2026-Q3",
    }.items():
        merge_period(
            root / "IREN" / calendar_label,
            root / "IREN" / fiscal_label,
            "IREN",
            fiscal_label,
        )

    merge_period(
        root / "HIMS" / "FY2025",
        root / "HIMS" / "2025-Q4",
        "HIMS",
        "2025-Q4",
    )
    repaired_duol = move_matching_entries(
        root / "DUOL" / "2024-Q3",
        root / "DUOL" / "2025-Q4",
        "DUOL",
        "2025-Q4",
        lambda entry: entry.get("period_end") == "2025-12-31",
    )
    moved_legacy_duol = move_matching_entries(
        root / "DUOL" / "2025-Q4",
        root / "DUOL" / "2024-Q3",
        "DUOL",
        "2024-Q3",
        lambda entry: entry.get("path")
        == "q4fy25-duolingo-09-30-24-shareholder-letter.pdf",
    )
    downgraded = downgrade_unverifiable_official_entries(root)
    print(
        "Normalized IREN fiscal labels, HIMS Q4/FY, and DUOL 2024-Q3; "
        f"repaired {repaired_duol} DUOL official entries, moved "
        f"{moved_legacy_duol} legacy DUOL entry, and downgraded {downgraded} "
        "legacy entries without complete provenance."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
