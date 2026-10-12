"""Lock IREN October 2026 light refresh: F3 16/40/80 unchanged; Anthropic unverified."""

from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "iren"
OUTPUT = ROOT / "output"
P0 = (
    DOCS / "catalyst-calendar.html",
    DOCS / "thesis-tracker.html",
    DOCS / "one-pager.html",
    DOCS / "index.html",
)
F3_LOCKED = ("16 / 40 / 80", "US$16", "US$40", "US$80")


class IrenOctRefreshTests(TestCase):
    def test_p0_pages_use_oct_spot_and_locked_f3(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$35.19", html, path.name)
            self.assertIn("16 / 40 / 80", html, path.name)
            self.assertIn("−12%", html, path.name)
            self.assertIn("2026-10-12", html, path.name)
            self.assertIn("decision-hud", html, path.name)
            self.assertIn("續抱", html, path.name)
            self.assertIn("唔好加倉", html, path.name)

    def test_anthropic_is_unverified_not_confirmed(self) -> None:
        for name in ("catalyst-calendar.html", "thesis-tracker.html", "one-pager.html"):
            html = (DOCS / name).read_text(encoding="utf-8")
            self.assertIn("Anthropic", html, name)
            self.assertIn("unverified", html, name)
            self.assertIn("未確認", html, name)

    def test_gate_is_hold_not_trim(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("未到 trim", html, path.name)
            self.assertIn("唔寫減倉", html, path.name)
            self.assertNotIn("應減倉", html, path.name)

    def test_no_new_covered_option_recommendation(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("開新 covered call", html, path.name)
            self.assertNotIn("covered put", html, path.name)

    def test_redline_one_still_fail(self) -> None:
        for name in ("thesis-tracker.html", "one-pager.html", "index.html"):
            html = (DOCS / name).read_text(encoding="utf-8")
            self.assertIn("5.90", html, name)
            self.assertIn("7.84", html, name)
            self.assertIn("167", html, name)

    def test_next_real_catalysts_on_calendar(self) -> None:
        html = (DOCS / "catalyst-calendar.html").read_text(encoding="utf-8")
        self.assertIn("Horizon 2–4", html)
        self.assertIn("FY2027-Q1", html)
        self.assertIn("未官方確認", html)

    def test_framework3_numbers_not_rewritten(self) -> None:
        html = (DOCS / "framework3.html").read_text(encoding="utf-8")
        self.assertIn("US$16", html)
        self.assertIn("US$40", html)
        self.assertIn("US$80", html)
        self.assertIn("US$40.53", html)
        self.assertNotIn("US$35.19", html)
        md = (OUTPUT / "IREN_2026-08-28_framework3.md").read_text(encoding="utf-8")
        self.assertIn("US$40", md)
        self.assertIn("US$16", md)
        self.assertIn("US$80", md)
        self.assertIn("US$40.53", md)

    def test_output_drafts_match_p0_locks(self) -> None:
        for name in (
            "IREN_catalyst_calendar.html",
            "IREN_thesis_tracker.html",
            "IREN_one-pager.html",
        ):
            html = (OUTPUT / name).read_text(encoding="utf-8")
            self.assertIn("US$35.19", html, name)
            self.assertIn("16 / 40 / 80", html, name)
            self.assertIn("unverified", html, name)
            self.assertIn("Anthropic", html, name)
            self.assertNotIn("應減倉", html)
