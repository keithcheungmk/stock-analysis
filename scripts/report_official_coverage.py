#!/usr/bin/env python3
"""Write a machine-readable six-quarter official coverage report."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("data/raw"))
    parser.add_argument(
        "--config", type=Path, default=Path("config/official_sources.yaml")
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        default=Path("data/source-catalog/holdings-six-quarters.json"),
    )
    parser.add_argument(
        "--supplements",
        type=Path,
        default=Path("config/ir_supplements.yaml"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/official-six-quarter-coverage.json"),
    )
    args = parser.parse_args()

    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    json.loads(args.catalog.read_text(encoding="utf-8"))
    supplements = yaml.safe_load(args.supplements.read_text(encoding="utf-8"))
    companies: dict[str, dict[str, object]] = {}
    totals = {
        "tickers": 0,
        "periods": 0,
        "verified_official_files": 0,
        "pending_sources": 0,
        "unavailable_sources": 0,
        "supplement_documents_not_downloaded": 0,
    }

    for ticker, company in config["companies"].items():
        result = {
            "periods": 0,
            "complete_periods": 0,
            "partial_periods": 0,
            "verified_official_files": 0,
            "pending_sources": 0,
            "unavailable_sources": 0,
            "supplement_documents_not_downloaded": 0,
        }
        for period in company["periods"]:
            manifest_path = args.root / ticker / period["label"] / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            result["periods"] += 1
            status_key = (
                "complete_periods"
                if manifest.get("validation_status") == "complete"
                else "partial_periods"
            )
            result[status_key] += 1
            official_urls = {
                entry.get("source_url")
                for entry in manifest.get("files", [])
                if entry.get("source_tier") == "official"
                and entry.get("validation_status") == "verified"
            }
            result["verified_official_files"] += len(official_urls)
            result["pending_sources"] += len(manifest.get("pending_sources", []))
            result["unavailable_sources"] += len(
                manifest.get("unavailable_sources", [])
            )
            supplement_period = (
                supplements.get("companies", {})
                .get(ticker, {})
                .get(period["label"], {})
            )
            expected_urls = {
                document["url"]
                for document in supplement_period.get("documents", [])
                if not document.get("optional", False)
            }
            result["supplement_documents_not_downloaded"] += len(
                expected_urls - official_urls
            )
        companies[ticker] = result
        totals["tickers"] += 1
        for key in totals:
            if key != "tickers":
                totals[key] += result[key]

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of": config["as_of"],
        "totals": totals,
        "companies": companies,
        "disclaimer": "Research only; not investment advice.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(totals, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
