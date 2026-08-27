from unittest import TestCase

from scripts.publish_html_reports import slug_and_label


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
