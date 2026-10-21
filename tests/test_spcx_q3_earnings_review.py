"""Lock SPCX Q3 FY2026 Skill 8 earnings review: official 8-K numbers, F3 68/91/182 unchanged."""

from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "spcx"
OUTPUT = ROOT / "output"
F3_MD = OUTPUT / "SPCX_2026-08-30_framework3.md"
REVIEW_MD = OUTPUT / "SPCX_2026-10-21_earnings_review.md"
REVIEW_HTML = OUTPUT / "SPCX_earnings_review.html"
PUBLISHED = DOCS / "earnings-review.html"
P0 = (
    DOCS / "options-overlay.html",
    DOCS / "catalyst-calendar.html",
    DOCS / "one-pager.html",
)


class SpcxQ3EarningsReviewTests(TestCase):
    def test_skill8_markdown_uses_official_q3(self) -> None:
        md = REVIEW_MD.read_text(encoding="utf-8")
        self.assertIn("US$14,575m", md)
        self.assertIn("+161%", md)
        self.assertIn("US$4,404m", md)
        self.assertIn("US$8,809m", md)
        self.assertIn("US$7,560m", md)
        self.assertIn("US$5,248m", md)
        self.assertIn("0001628280-26-066482", md)
        self.assertIn("2026-10-20", md)
        self.assertIn("續抱", md)
        self.assertIn("勿新開賣認沽", md)
        self.assertIn("68／91／182", md)
        self.assertIn("eligible ≠ must sell", md)
        self.assertIn("unverified", md)
        self.assertIn("Mixed", md)
        self.assertIn("而家作廢", md)
        self.assertIn("官方公布日係 2026-10-20", md)

    def test_html_hud_and_gate(self) -> None:
        for path in (REVIEW_HTML, PUBLISHED):
            html = path.read_text(encoding="utf-8")
            self.assertIn('id="decision-hud"', html, path.name)
            self.assertIn("US$147.79", html, path.name)
            self.assertIn("68 / 91 / 182", html, path.name)
            self.assertIn("+62.4%", html, path.name)
            self.assertIn("US$14.575B", html, path.name)
            self.assertIn("US$4.404B", html, path.name)
            self.assertIn("7.56", html, path.name)
            self.assertIn("5.25", html, path.name)
            self.assertIn("續抱現股；勿新開賣認沽", html, path.name)
            self.assertIn("1.3B", html, path.name)
            self.assertIn("eligible ≠ must sell", html, path.name)
            self.assertIn("unverified", html, path.name)
            self.assertIn("此分析僅供研究參考，不構成投資建議。", html, path.name)
            self.assertNotIn("US$254", html, path.name)

    def test_framework3_numbers_untouched(self) -> None:
        md = F3_MD.read_text(encoding="utf-8")
        self.assertIn("~US$68", md)
        self.assertIn("~US$91", md)
        self.assertIn("~US$182", md)
        html = (DOCS / "framework3.html").read_text(encoding="utf-8")
        self.assertIn("US$68", html)
        self.assertIn("US$91", html)
        self.assertIn("US$182", html)
        self.assertNotIn("US$254", html)

    def test_other_p0_pages_not_rewritten_this_pr(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$162.57", html, path.name)
            self.assertIn("68 / 91 / 182", html, path.name)
            self.assertIn("+78.6%", html, path.name)
