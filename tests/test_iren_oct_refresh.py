"""Lock IREN November 2026 Framework 3 refresh: F3 5/19/50; Q1 FY27 BS anchors."""

from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "iren"
OUTPUT = ROOT / "output"
P0 = (
    DOCS / "index.html",
    DOCS / "framework3.html",
    DOCS / "valuation.html",
    DOCS / "balance-sheet.html",
)
F3_LOCKED = ("5 / 19 / 50", "US$5", "US$19", "US$50")


class IrenNovF3RefreshTests(TestCase):
    def test_p0_pages_use_nov_spot_and_locked_f3(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$12.95", html, path.name)
            self.assertIn("5 / 19 / 50", html, path.name)
            self.assertIn("−33%", html, path.name)
            self.assertIn("2026-11-25", html, path.name)
            self.assertIn("decision-hud", html, path.name)
            self.assertIn("續抱", html, path.name)
            self.assertIn("唔好", html, path.name)
            self.assertIn("加倉", html, path.name)

    def test_gate_is_hold_not_forced_trim(self) -> None:
        html = (DOCS / "index.html").read_text(encoding="utf-8")
        self.assertIn("續抱", html)
        self.assertIn("唔好大幅加倉", html)
        self.assertNotIn("應減倉", html)

    def test_no_new_covered_option_recommendation(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("開新 covered call", html, path.name)
            self.assertNotIn("covered put", html, path.name)

    def test_redline_one_still_fail_q1(self) -> None:
        for name in ("index.html", "framework3.html", "balance-sheet.html"):
            html = (DOCS / name).read_text(encoding="utf-8")
            self.assertIn("3.52", html, name)
            self.assertIn("10.21", html, name)
            self.assertTrue("FAIL" in html or "紅線" in html, name)

    def test_framework3_nov_numbers(self) -> None:
        html = (DOCS / "framework3.html").read_text(encoding="utf-8")
        for token in F3_LOCKED:
            self.assertIn(token, html)
        self.assertIn("US$12.95", html)
        self.assertNotIn("US$35.19", html)
        md = (OUTPUT / "IREN_2026-11-25_framework3.md").read_text(encoding="utf-8")
        self.assertIn("US$19", md)
        self.assertIn("US$5", md)
        self.assertIn("US$50", md)
        self.assertIn("US$12.95", md)

    def test_balance_sheet_page_present(self) -> None:
        html = (DOCS / "balance-sheet.html").read_text(encoding="utf-8")
        self.assertIn("1.07×", html)
        self.assertIn("4,430", html)
        self.assertIn("12,344", html)
