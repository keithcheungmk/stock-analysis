from unittest import TestCase
from unittest.mock import patch

from scripts.download_official_research import (
    Filing,
    OfficialDownloader,
    classify_document,
    parse_filing_documents,
    select_filings,
)


class OfficialResearchDownloaderTests(TestCase):
    def test_user_agent_requires_contact_email(self) -> None:
        with self.assertRaises(ValueError):
            OfficialDownloader("stock-analysis")

    @patch("scripts.download_official_research.urllib.request.urlopen")
    def test_fetch_uses_mock_http_response(self, urlopen) -> None:
        class Headers:
            @staticmethod
            def get_content_type() -> str:
                return "application/json"

        class Response:
            headers = Headers()

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return None

            @staticmethod
            def read() -> bytes:
                return b'{"ok": true}'

        urlopen.return_value = Response()
        downloader = OfficialDownloader("stock-analysis test@example.com", 1000)
        self.assertEqual(
            downloader.fetch_json("https://data.sec.gov/example.json"),
            {"ok": True},
        )

    def test_selects_periodic_and_nearest_event_filing(self) -> None:
        rows = [
            Filing("0001-25-000001", "10-Q", "2025-05-08", "2025-03-31", "q.htm"),
            Filing("0001-25-000002", "8-K", "2025-05-07", "2025-05-07", "event.htm"),
            Filing("0001-25-000003", "8-K", "2025-04-01", "2025-04-01", "other.htm"),
        ]
        selected = select_filings(
            rows,
            {
                "label": "2025-Q1",
                "period_end": "2025-03-31",
                "release_date": "2025-05-07",
            },
        )
        self.assertEqual(
            {filing.form for filing in selected},
            {"10-Q", "8-K"},
        )

    def test_parses_sec_document_table(self) -> None:
        body = b"""
        <table class="tableFile">
          <tr><th>Seq</th><th>Description</th><th>Document</th><th>Type</th></tr>
          <tr><td>1</td><td>Quarterly report</td><td><a href="q.htm">q.htm</a></td><td>10-Q</td></tr>
          <tr><td>2</td><td>Earnings release</td><td><a href="ex991.htm">ex991.htm</a></td><td>EX-99.1</td></tr>
        </table>
        """
        documents = parse_filing_documents(body, "https://www.sec.gov/example/index.html")
        self.assertEqual(len(documents), 2)
        self.assertEqual(documents[1]["type"], "EX-99.1")
        self.assertEqual(
            documents[1]["url"],
            "https://www.sec.gov/example/ex991.htm",
        )

    def test_classifies_shareholder_update(self) -> None:
        filing = Filing("0001", "8-K", "2025-05-07", "2025-05-07", "event.htm")
        document = {
            "name": "letter.pdf",
            "description": "Quarterly shareholder letter",
            "type": "EX-99.1",
            "url": "https://example.com/letter.pdf",
        }
        self.assertEqual(classify_document(filing, document), "shareholder_update")
