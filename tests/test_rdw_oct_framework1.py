"""Lock RDW October 2026 Framework 1 rerun: 60/130 FAIL, Q3 red-line-2 warning, F3 08-30 HUD."""

from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    ROOT / "docs" / "rdw" / "framework1.html",
    ROOT / "output" / "RDW_framework1.html",
)
MD = ROOT / "output" / "RDW_2026-10-14_framework1.md"


class RdwOctFramework1Tests(TestCase):
    def test_pages_have_hud_with_oct_spot_and_locked_f3(self) -> None:
        for path in PAGES:
            html = path.read_text(encoding="utf-8")
            self.assertIn("decision-hud", html, path.name)
            self.assertIn("US$9.16", html, path.name)
            self.assertIn("7.06 / 11.40 / 19.15", html, path.name)
            self.assertIn("−19.6%", html, path.name)
            self.assertIn("唔好加倉", html, path.name)
            self.assertLess(html.index("decision-hud"), html.index('class="action"'), path.name)

    def test_score_and_verdict(self) -> None:
        for path in (*PAGES, MD):
            text = path.read_text(encoding="utf-8")
            self.assertIn("60 / 130", text, path.name)
            self.assertIn("FAIL", text, path.name)
            self.assertIn("門檻未達型", text, path.name)

    def test_q3_red_line_two_warning(self) -> None:
        for path in (*PAGES, MD):
            text = path.read_text(encoding="utf-8")
            self.assertIn("US$137M", text, path.name)
            self.assertIn("+11%～+35%", text, path.name)
            self.assertIn("−2.6%", text, path.name)

    def test_official_q2_figures(self) -> None:
        text = MD.read_text(encoding="utf-8")
        for figure in ("US$117.1M", "27.8%", "US$542.1M", "US$557.7M", "−US$106.0M", "5.37×"):
            self.assertIn(figure, text, figure)

    def test_idiq_not_counted_as_revenue(self) -> None:
        for path in (*PAGES, MD):
            self.assertIn("無保證收入", path.read_text(encoding="utf-8"), path.name)

    def test_disclaimer(self) -> None:
        for path in (*PAGES, MD):
            self.assertIn("此分析僅供研究參考，不構成投資建議", path.read_text(encoding="utf-8"), path.name)
