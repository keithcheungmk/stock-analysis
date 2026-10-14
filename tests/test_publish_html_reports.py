import tempfile
from pathlib import Path
from unittest import TestCase

from scripts.publish_html_reports import (
    CURATED_END,
    CURATED_START,
    SKIP_OVERWRITE,
    comment_script_src,
    extract_f1,
    extract_hud,
    hud_premium,
    hud_price,
    inject_comments,
    slug_and_label,
)


class PublishHtmlReportsTests(TestCase):
    def test_framework_slugs(self) -> None:
        self.assertEqual(slug_and_label("NVDA_framework2", "NVDA"), ("framework2", "Framework 2 深度增長"))
        self.assertEqual(slug_and_label("NVDA_framework1", "NVDA"), ("framework1", "Framework 1 初篩"))

    def test_one_pager_and_earnings_review(self) -> None:
        self.assertEqual(
            slug_and_label("RKLB_2026-08-14_one-pager", "RKLB")[0],
            "one-pager",
        )
        self.assertEqual(
            slug_and_label("AMD_one_pager", "AMD"),
            ("one-pager", "one pager"),
        )
        self.assertEqual(
            slug_and_label("AMD_2026-09-27_one_pager", "AMD")[0],
            "one-pager",
        )
        self.assertEqual(
            slug_and_label("RDW_earnings_review_q2_2026", "RDW")[0],
            "earnings-review",
        )

    def test_skill7_option_strategy_slug(self) -> None:
        self.assertEqual(
            slug_and_label("AMD_skill7_option_strategy", "AMD"),
            ("skill7-option-strategy", "期權策略"),
        )
        self.assertEqual(
            slug_and_label("AMD_2026-09-27_skill7_option_strategy", "AMD")[0],
            "skill7-option-strategy",
        )

    def test_comment_script_depth(self) -> None:
        docs = Path(__file__).resolve().parents[1] / "docs"
        self.assertEqual(comment_script_src(docs / "index.html"), "assets/page-comments.js")
        self.assertEqual(
            comment_script_src(docs / "spcx" / "valuation-model.html"),
            "../assets/page-comments.js",
        )

    def test_amd_index_curated_hud_survives_regeneration(self) -> None:
        docs = Path(__file__).resolve().parents[1] / "docs"
        amd_index = docs / "amd" / "index.html"
        self.assertNotIn(amd_index, SKIP_OVERWRITE)
        html = amd_index.read_text(encoding="utf-8")
        self.assertIn(CURATED_START, html)
        self.assertIn(CURATED_END, html)
        self.assertIn("US$629.26", html)
        self.assertIn("180 / 360 / 505", html)
        self.assertIn("+74.8%", html)
        self.assertIn("舊 240／390／620 作廢", html)
        self.assertEqual(html.count('id="decision-hud"'), 1)

    def test_hud_extraction_and_premium(self) -> None:
        html = (
            '<section class="hud" id="decision-hud"><h2>Decision HUD '
            '<span class="hud-tag">現價 vs Base −19.6%</span></h2>'
            '<div class="hud-cell"><div class="l">現價（延遲）</div><div class="v">US$9.16</div></div>'
            '<div class="hud-cell"><div class="l">Bear / Base / Bull</div><div class="v">7.06 / 11.40 / 19.15</div></div>'
            '<div class="hud-cell"><div class="l">現價相對 Base</div><div class="v">-11.0%</div></div>'
            "</section>"
        )
        hud = extract_hud(html)
        self.assertIsNotNone(hud)
        self.assertEqual(hud_price(hud), "US$9.16")
        self.assertEqual(hud_premium(hud), ("−11.0%", -11.0))
        self.assertIsNone(extract_hud("<p>no hud</p>"))

    def test_f1_score_ignores_valuation_ladder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "framework1.html"
            page.write_text(
                '<div class="v">80 / 130 / 180</div><div class="score-num">FAIL</div>', encoding="utf-8"
            )
            self.assertEqual(extract_f1(Path(tmp)), ("FAIL", ""))
            page.write_text('<div class="score-num">FAIL</div> 60 / 130 · 差 5 分', encoding="utf-8")
            self.assertEqual(extract_f1(Path(tmp)), ("FAIL", "60"))

    def test_hub_is_compact_tile_grid_linking_to_ticker_pages(self) -> None:
        docs = Path(__file__).resolve().parents[1] / "docs"
        hub = (docs / "index.html").read_text(encoding="utf-8")
        tickers = [p.name for p in docs.iterdir() if p.is_dir() and p.name != "assets"]
        self.assertEqual(hub.count('class="tile"'), len(tickers))
        for name in tickers:
            self.assertIn(f'href="./{name}/"', hub)
            ticker_html = (docs / name / "index.html").read_text(encoding="utf-8")
            self.assertIn('id="decision-hud"', ticker_html, name)
            self.assertIn('class="reports"', ticker_html, name)
        self.assertNotIn("/framework1.html", hub)
        self.assertIn("現價 vs Base −19.6%", hub)

    def test_inject_comments_idempotent(self) -> None:
        docs = Path(__file__).resolve().parents[1] / "docs"
        dest = docs / "spcx" / "valuation-model.html"
        html = "<html><body>hi</body></html>"
        once = inject_comments(html, dest)
        twice = inject_comments(once, dest)
        self.assertEqual(once, twice)
        self.assertIn("page-comments", once)
        self.assertIn("../assets/page-comments.js", once)
