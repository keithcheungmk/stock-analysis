"""Lock TSLA/RKLB October 2026 light refresh: F3 numbers unchanged; expired events retired."""

from pathlib import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[1]
DOCS_TSLA = ROOT / "docs" / "tsla"
DOCS_RKLB = ROOT / "docs" / "rklb"
OUTPUT = ROOT / "output"

TSLA_P0 = (
    DOCS_TSLA / "catalyst-calendar.html",
    DOCS_TSLA / "one-pager.html",
)
RKLB_P0 = (
    DOCS_RKLB / "catalyst-calendar.html",
    DOCS_RKLB / "one-pager.html",
)
TSLA_OUTPUT = (
    OUTPUT / "TSLA_catalyst_calendar.html",
    OUTPUT / "TSLA_one_pager.html",
)
RKLB_OUTPUT = (
    OUTPUT / "RKLB_catalyst_calendar.html",
    OUTPUT / "RKLB_one_pager.html",
)


class TslaOctRefreshTests(TestCase):
    def test_p0_pages_use_oct_spot_and_locked_f3(self) -> None:
        for path in TSLA_P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$382.70", html, path.name)
            self.assertIn("63 / 157 / 402", html, path.name)
            self.assertIn("+143.8%", html, path.name)
            self.assertIn("溢價約 +144%", html, path.name)
            self.assertIn("2026-10-11", html, path.name)
            self.assertIn("decision-hud", html, path.name)
            self.assertIn("僅觀察／勿加倉", html, path.name)

    def test_catalyst_retires_sept_event_and_notes_blackout(self) -> None:
        html = (DOCS_TSLA / "catalyst-calendar.html").read_text(encoding="utf-8")
        self.assertIn("退役 P0", html)
        self.assertIn("486,532", html)
        self.assertIn("黑窗約 10/16", html)
        self.assertIn("2026-10-21 AMC", html)
        self.assertIn("唔開新 CSP", html)
        self.assertIn("Keith 確認 trim", html)
        self.assertNotIn("等 9/3", html)
        self.assertNotIn("9/3 硬件閘<br>Base 仍然 157", html)

    def test_gate_is_observe_not_trim(self) -> None:
        for path in TSLA_P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("未到 trim", html, path.name)
            self.assertIn("唔寫減倉", html, path.name)
            self.assertNotIn("應減倉", html, path.name)

    def test_framework3_numbers_not_rewritten(self) -> None:
        html = (DOCS_TSLA / "framework3.html").read_text(encoding="utf-8")
        self.assertIn("US$63", html)
        self.assertIn("US$157", html)
        self.assertIn("US$402", html)
        self.assertIn("US$365.83", html)
        self.assertNotIn("US$382.70", html)
        md = (OUTPUT / "TSLA_2026-08-27_framework3.md").read_text(encoding="utf-8")
        self.assertIn("US$63／US$157／US$402", md)

    def test_output_drafts_match_p0_locks(self) -> None:
        for path in TSLA_OUTPUT:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$382.70", html, path.name)
            self.assertIn("63 / 157 / 402", html, path.name)
            self.assertIn("僅觀察／勿加倉", html, path.name)


class RklbOctRefreshTests(TestCase):
    def test_p0_pages_use_oct_spot_and_locked_f3(self) -> None:
        for path in RKLB_P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$68.21", html, path.name)
            self.assertIn("28 / 56 / 101", html, path.name)
            self.assertIn("+21.8%", html, path.name)
            self.assertIn("2026-10-11", html, path.name)
            self.assertIn("decision-hud", html, path.name)
            self.assertIn("僅觀察／勿加倉", html, path.name)

    def test_iridium_vote_not_listed_as_upcoming(self) -> None:
        for path in RKLB_P0:
            html = path.read_text(encoding="utf-8")
            self.assertNotIn("等 9/24 投票", html, path.name)
            self.assertNotIn("等 9/24", html, path.name)
            self.assertIn("已通過", html, path.name)
            self.assertIn("2027 中", html, path.name)
            self.assertIn("唔係即將投票", html, path.name)

    def test_catalyst_adds_synspective_and_keeps_cash_burn(self) -> None:
        html = (DOCS_RKLB / "catalyst-calendar.html").read_text(encoding="utf-8")
        self.assertIn("Synspective", html)
        self.assertIn("20 Electron", html)
        self.assertIn("&gt;100", html)
        self.assertIn("−US$134.4M", html)
        self.assertIn("Neutron", html)
        self.assertIn("Q4", html)
        self.assertIn("唔開新 CSP", html)
        self.assertIn("1/3", html)

    def test_gate_is_observe_not_trim(self) -> None:
        for path in RKLB_P0:
            html = path.read_text(encoding="utf-8")
            self.assertIn("未到 trim", html, path.name)
            self.assertIn("唔寫減倉", html, path.name)

    def test_framework3_numbers_not_rewritten(self) -> None:
        html = (DOCS_RKLB / "framework3.html").read_text(encoding="utf-8")
        self.assertIn("US$28", html)
        self.assertIn("US$56", html)
        self.assertIn("US$101", html)
        self.assertIn("US$66.18", html)
        self.assertNotIn("US$68.21", html)
        md = (OUTPUT / "RKLB_2026-08-14_framework3.md").read_text(encoding="utf-8")
        self.assertIn("US$56", md)
        self.assertIn("US$28", md)
        self.assertIn("US$101", md)

    def test_output_drafts_match_p0_locks(self) -> None:
        for path in RKLB_OUTPUT:
            html = path.read_text(encoding="utf-8")
            self.assertIn("US$68.21", html, path.name)
            self.assertIn("28 / 56 / 101", html, path.name)
            self.assertNotIn("等 9/24 投票", html, path.name)
