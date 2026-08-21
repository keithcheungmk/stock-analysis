from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from scripts.import_research_library import classify, infer_period, safe_filename


class ImportResearchLibraryTests(TestCase):
    def test_infer_quarter_periods(self) -> None:
        self.assertEqual(infer_period("AMD Q1'26 Earnings Slides.pdf"), ("2026-Q1", "high"))
        self.assertEqual(infer_period("TSLA-2025-Q3-10Q.pdf"), ("2025-Q3", "high"))
        self.assertEqual(infer_period("Q3 FY25 Presentation.pdf"), ("2025-Q3", "high"))

    def test_unknown_period_is_not_guessed(self) -> None:
        self.assertEqual(infer_period("Investing Pro Research.pdf"), ("_unsorted", "low"))

    def test_filename_normalization(self) -> None:
        self.assertEqual(
            safe_filename("  Earnings Slides FINAL .PDF"),
            "earnings-slides-final.pdf",
        )

    def test_private_statement_is_kept_outside_repo(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            source_root = Path(temporary_directory)
            source = source_root / "IB statement 260526.pdf"
            destination_root = source_root / "repo" / "data" / "raw"
            private_root = source_root / "private"
            destination, category, ticker, period, confidence = classify(
                source, source_root, destination_root, private_root
            )
            self.assertEqual(destination, private_root / "ib-statement-260526.pdf")
            self.assertEqual(category, "private")
            self.assertIsNone(ticker)
            self.assertIsNone(period)
            self.assertEqual(confidence, "high")

    def test_metaplanet_maps_to_japanese_ticker(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            source_root = Path(temporary_directory)
            source = source_root / "Metaplanet" / "Research.pdf"
            destination_root = source_root / "repo" / "data" / "raw"
            destination, category, ticker, period, confidence = classify(
                source, source_root, destination_root, source_root / "private"
            )
            self.assertEqual(destination, destination_root / "3350.T" / "_unsorted" / "research.pdf")
            self.assertEqual(category, "ticker")
            self.assertEqual(ticker, "3350.T")
            self.assertEqual(period, "_unsorted")
            self.assertEqual(confidence, "low")
