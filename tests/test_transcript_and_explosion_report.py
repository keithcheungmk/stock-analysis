"""Regression tests for transcript QoQ loading and Tesla AI report formatting."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

import pandas as pd

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from explosion import ExplosionStatus
from tesla_ai_report import build_tesla_ai_report
from transcript import load_previous_analysis


def _sample_transcript_json(
    quarter: str,
    fiscal_year: int,
    suffix: str = "",
) -> dict:
    return {
        "symbol": "TSLA",
        "quarter": quarter,
        "fiscal_year": fiscal_year,
        "date": "2026-08-28",
        "source": "manual",
        "raw_text": f"robotaxi mention {suffix}",
        "keywords": [],
        "robotaxi_mentions": [],
        "fsd_mentions": [],
        "optimus_mentions": [],
        "margin_mentions": [],
        "guidance_summary": "",
    }


class TeslaAiReportExplosionLabelTests(TestCase):
    def test_dual_track_eps_line_does_not_prefix_last_quarter_with_q(self) -> None:
        status = ExplosionStatus(
            symbol="TSLA",
            as_of_date="2026-08-28",
            last_quarter="2026-07",
            last_actual_eps=0.52,
            last_consensus_eps=0.45,
            last_surprise_pct=15.6,
            eps_explosion_triggered=True,
            price_3m_return_pct=10.0,
            price_3m_start=200.0,
            price_3m_end=220.0,
            price_explosion_triggered=False,
            eps_explosion_pressure="high",
            price_explosion_pressure="moderate",
            next_earnings_estimate=None,
            explanation="",
        )
        hist = pd.DataFrame({"Close": [200.0, 210.0], "Volume": [1_000_000, 1_100_000]})
        technical = {
            "close": 210.0,
            "volume": 1_100_000,
            "rsi": 50.0,
            "rsi_signal": "neutral",
            "macd": 1.0,
            "macd_signal_line": 0.5,
            "macd_bullish": True,
        }
        fundamentals = {"market_cap": 1e12, "trailing_pe": 50.0}
        peers_df = pd.DataFrame()
        project_root = Path(__file__).resolve().parents[1]

        with patch("tesla_ai_report.detect_explosion", return_value=status):
            report = build_tesla_ai_report(
                "TSLA",
                hist,
                fundamentals,
                technical,
                peers_df,
                [20, 50],
                project_root,
            )

        self.assertIn("2026-07 actual", report)
        self.assertNotRegex(report, r"Q20\d{2}")


class LoadPreviousAnalysisTests(TestCase):
    def test_skips_malformed_transcript_json(self) -> None:
        with TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            (output_dir / "tsla_corrupt_transcript.json").write_text("{ not json", encoding="utf-8")
            good = _sample_transcript_json("Q4 2024", 2024)
            (output_dir / "tsla_q42024_transcript.json").write_text(
                json.dumps(good),
                encoding="utf-8",
            )

            loaded = load_previous_analysis("TSLA", output_dir)

        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.quarter, "Q4 2024")
        self.assertEqual(loaded.fiscal_year, 2024)

    def test_orders_by_fiscal_year_and_quarter_not_filename(self) -> None:
        with TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            q4_2024 = _sample_transcript_json("Q4 2024", 2024, "older")
            q1_2025 = _sample_transcript_json("Q1 2025", 2025, "newer")
            # Filename sort would prefer q1_2025 before q4_2024 lexically in some cases;
            # here we ensure Q1 2025 wins on calendar order when excluding nothing.
            (output_dir / "tsla_aaa_q42024_transcript.json").write_text(
                json.dumps(q4_2024),
                encoding="utf-8",
            )
            (output_dir / "tsla_zzz_q12025_transcript.json").write_text(
                json.dumps(q1_2025),
                encoding="utf-8",
            )

            loaded = load_previous_analysis("TSLA", output_dir)

        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.fiscal_year, 2025)
        self.assertEqual(loaded.quarter, "Q1 2025")

    def test_exclude_current_quarter_returns_prior(self) -> None:
        with TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            q4_2024 = _sample_transcript_json("Q4 2024", 2024)
            q1_2025 = _sample_transcript_json("Q1 2025", 2025)
            (output_dir / "tsla_q42024_transcript.json").write_text(
                json.dumps(q4_2024),
                encoding="utf-8",
            )
            (output_dir / "tsla_q12025_transcript.json").write_text(
                json.dumps(q1_2025),
                encoding="utf-8",
            )

            loaded = load_previous_analysis(
                "TSLA",
                output_dir,
                exclude_quarter="Q1 2025",
                exclude_fiscal_year=2025,
            )

        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.fiscal_year, 2024)
        self.assertEqual(loaded.quarter, "Q4 2024")
