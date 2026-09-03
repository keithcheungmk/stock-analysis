import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from scripts.import_manual_official import archive_inbox_file


class ImportManualOfficialTests(TestCase):
    def test_archive_inbox_file_moves_pdf_and_updates_manifest(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            raw_root = Path(temporary_directory) / "raw"
            target = raw_root / "RKLB" / "_events"
            target.mkdir(parents=True)
            manifest_path = target / "manifest.json"
            manifest_path.write_text(
                json.dumps(
                    {
                        "schema_version": 2,
                        "ticker": "RKLB",
                        "currency": "USD",
                        "accounting_basis": ["US_GAAP"],
                        "files": [],
                    }
                ),
                encoding="utf-8",
            )
            source = raw_root / "_manual-inbox" / "presentation.pdf"
            source.parent.mkdir()
            source.write_bytes(b"%PDF-1.7\nmanual test")
            mapping = {
                "ticker": "RKLB",
                "period": "_events",
                "destination": "ir-presentation.pdf",
                "document_type": "investor_presentation",
                "source_tier": "official",
                "source_authority": "Official company IR",
                "filing_form": None,
                "filing_date": "2026-06-29",
                "source_url": "https://example.com/presentation.pdf",
            }

            status = archive_inbox_file(source, raw_root, mapping)

            self.assertEqual(status, "imported")
            self.assertFalse(source.exists())
            self.assertTrue((target / "ir-presentation.pdf").exists())
            entry = json.loads(manifest_path.read_text(encoding="utf-8"))["files"][0]
            self.assertEqual(entry["source_tier"], "official")
            self.assertNotIn("period_end", entry)

