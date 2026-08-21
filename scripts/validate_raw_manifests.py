#!/usr/bin/env python3
"""Validate raw research manifests, file coverage, sizes, and SHA-256 hashes."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import urlparse

import yaml


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_manifest(manifest_path: Path) -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{manifest_path}: invalid JSON: {exc}"]

    files = manifest.get("files")
    if not isinstance(files, list):
        return [f"{manifest_path}: 'files' must be an array"]

    listed_paths: set[str] = set()
    listed_hashes: set[str] = set()
    for index, entry in enumerate(files):
        prefix = f"{manifest_path}: files[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix} must be an object")
            continue
        relative_path = entry.get("path")
        expected_hash = entry.get("sha256")
        if not isinstance(relative_path, str) or not relative_path:
            errors.append(f"{prefix}.path is required")
            continue
        if relative_path in listed_paths:
            errors.append(f"{prefix}.path is duplicated: {relative_path}")
        listed_paths.add(relative_path)

        target = (manifest_path.parent / relative_path).resolve()
        if not target.is_relative_to(manifest_path.parent.resolve()):
            errors.append(f"{prefix}.path escapes the manifest directory")
            continue
        if not target.is_file():
            errors.append(f"{prefix}.path does not exist: {relative_path}")
            continue

        if not isinstance(expected_hash, str) or len(expected_hash) != 64:
            errors.append(f"{prefix}.sha256 must be a 64-character digest")
        else:
            actual_hash = sha256_file(target)
            if actual_hash != expected_hash:
                errors.append(
                    f"{prefix}.sha256 mismatch: expected {expected_hash}, got {actual_hash}"
                )
            if expected_hash in listed_hashes:
                errors.append(f"{prefix}.sha256 is duplicated within this manifest")
            listed_hashes.add(expected_hash)

        expected_size = entry.get("size_bytes")
        if expected_size is not None and target.stat().st_size != expected_size:
            errors.append(
                f"{prefix}.size_bytes mismatch: expected {expected_size}, "
                f"got {target.stat().st_size}"
            )
        if entry.get("source_tier") == "official":
            source_url = entry.get("source_url")
            if not isinstance(source_url, str) or not source_url.startswith("https://"):
                errors.append(f"{prefix}.source_url is required for official files")
            elif not urlparse(source_url).hostname:
                errors.append(f"{prefix}.source_url has no valid hostname")
            if entry.get("validation_status") != "verified":
                errors.append(f"{prefix}.validation_status must be verified")
            if not entry.get("mime_type"):
                errors.append(f"{prefix}.mime_type is required for official files")

    actual_paths = {
        path.name
        for path in manifest_path.parent.iterdir()
        if path.is_file() and path.name != "manifest.json"
    }
    missing_entries = actual_paths - listed_paths
    for path in sorted(missing_entries):
        errors.append(f"{manifest_path}: unlisted file: {path}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root", type=Path, default=Path("data/raw"), help="Raw data root"
    )
    parser.add_argument(
        "--coverage-config",
        type=Path,
        help="Validate six-quarter official coverage from this YAML config",
    )
    return parser.parse_args()


def validate_coverage(root: Path, config_path: Path) -> list[str]:
    errors: list[str] = []
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    companies = config.get("companies", {})
    if len(companies) != 10:
        errors.append(f"{config_path}: expected 10 holdings, got {len(companies)}")
    target_count = sum(len(company.get("periods", [])) for company in companies.values())
    if target_count != 60:
        errors.append(f"{config_path}: expected 60 periods, got {target_count}")

    for ticker, company in companies.items():
        periods = company.get("periods", [])
        if len(periods) != 6:
            errors.append(f"{ticker}: expected 6 periods, got {len(periods)}")
        for period in periods:
            label = period["label"]
            manifest_path = root / ticker / label / "manifest.json"
            if not manifest_path.exists():
                errors.append(f"{ticker}/{label}: missing manifest.json")
                continue
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("period_end") != period["period_end"]:
                errors.append(
                    f"{ticker}/{label}: period_end mismatch "
                    f"({manifest.get('period_end')} != {period['period_end']})"
                )
            if manifest.get("currency") != company["currency"]:
                errors.append(f"{ticker}/{label}: currency mismatch")
            official_files = [
                entry
                for entry in manifest.get("files", [])
                if entry.get("source_tier") == "official"
                and entry.get("validation_status") == "verified"
            ]
            if not official_files:
                errors.append(f"{ticker}/{label}: no verified official file")
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    manifests = sorted(root.rglob("manifest.json"))
    errors: list[str] = []
    for manifest in manifests:
        errors.extend(validate_manifest(manifest))

    directories_with_files = {
        path.parent
        for path in root.rglob("*")
        if path.is_file()
        and path.name not in {"manifest.json", "README.md", ".DS_Store"}
        and "_manual-inbox" not in path.parts
    }
    manifest_directories = {path.parent for path in manifests}
    for directory in sorted(directories_with_files - manifest_directories):
        errors.append(f"{directory}: contains raw files but has no manifest.json")
    if args.coverage_config:
        errors.extend(
            validate_coverage(root, args.coverage_config.expanduser().resolve())
        )

    if errors:
        print(f"Validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(manifests)} manifests successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
