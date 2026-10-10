"""Lock SPCX October 2026 light refresh: F3 68/91/182 unchanged; Sept put window closed."""

from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "spcx"
OUTPUT = ROOT / "output"
P0 = (
    DOCS / "options-overlay.html",
    DOCS / "catalyst-calendar.html",
    DOCS / "one-pager.html",
)
F3_LOCKED = ("68 / 91 / 182", "US$68", "US$91", "US$182")


class SpcxOctRefreshTests(TestCase):
    def test_p0_pages_use_oct_spot_and_locked_f3(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$162.57", html, path.name)
            self.assertIn("68 / 91 / 182", html, path.name)
            self.assertIn("+78.6%", html, path.name)
            self.assertIn("溢價約 +79%", html, path.name)
            self.assertIn("2026-10-10", html, path.name)
            self.assertIn("decision-hud", html, path.name)

    def test_p0_pages_close_sept_put_window(self) -> None:
        for path in P0:
            html = path.read_text(encoding="utf-8")
            self.assertNotRegex(
                html,
                r"距到期只剩 19 日|到期 2026-09-18（19 日後）|09-18 · 15 日後",
                msg=f"{path.name} still has live Sept countdown",
            )
            self.assertIn("已到期", html, path.name)

    def test_options_overlay_no_new_csp(self) -> None:
        html = (DOCS / "options-overlay.html").read_text(encoding="utf-8")
        self.assertIn("唔開新 CSP", html)
        self.assertIn("待 Keith 確認", html)
        self.assertIn("要 Keith 確認", html)
        self.assertNotIn("優先買回兩張 put（優先）", html)

    def test_catalyst_elevates_oct_windows(self) -> None:
        html = (DOCS / "catalyst-calendar.html").read_text(encoding="utf-8")
        self.assertIn("Day 135", html)
        self.assertIn("2026-10-24", html)
        self.assertIn("2026-12-08", html)
        self.assertIn("Grain", html)
        self.assertIn("unverified", html)
        self.assertIn("退役 P0", html)
        self.assertIn("可賣 ≠ 必賣", html)

    def test_framework3_numbers_not_rewritten(self) -> None:
        html = (DOCS / "framework3.html").read_text(encoding="utf-8")
        self.assertIn("US$68", html)
        self.assertIn("US$91", html)
        self.assertIn("US$182", html)
        self.assertNotIn("US$254", html)
        self.assertNotIn("US$300", html)
        md = (OUTPUT / "SPCX_2026-08-30_framework3.md").read_text(encoding="utf-8")
        self.assertIn("US$68", md)
        self.assertIn("US$91", md)
        self.assertIn("US$182", md)

    def test_output_drafts_match_p0_locks(self) -> None:
        for name in (
            "SPCX_options_overlay.html",
            "SPCX_catalyst_calendar.html",
            "SPCX_one_pager.html",
        ):
            html = (OUTPUT / name).read_text(encoding="utf-8")
            self.assertIn("US$162.57", html, name)
            self.assertIn("68 / 91 / 182", html, name)
            self.assertNotIn("距到期只剩 19 日", html)
