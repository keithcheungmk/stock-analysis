from pathlib import Path
from unittest import TestCase

from scripts.publish_html_reports import (
    comment_script_src,
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
            slug_and_label("RDW_earnings_review_q2_2026", "RDW")[0],
            "earnings-review",
        )

    def test_comment_script_depth(self) -> None:
        docs = Path(__file__).resolve().parents[1] / "docs"
        self.assertEqual(comment_script_src(docs / "index.html"), "assets/page-comments.js")
        self.assertEqual(
            comment_script_src(docs / "spcx" / "valuation-model.html"),
            "../assets/page-comments.js",
        )

    def test_inject_comments_idempotent(self) -> None:
        docs = Path(__file__).resolve().parents[1] / "docs"
        dest = docs / "spcx" / "valuation-model.html"
        html = "<html><body>hi</body></html>"
        once = inject_comments(html, dest)
        twice = inject_comments(once, dest)
        self.assertEqual(once, twice)
        self.assertIn("page-comments", once)
        self.assertIn("../assets/page-comments.js", once)
