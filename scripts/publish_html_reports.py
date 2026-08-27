#!/usr/bin/env python3
"""Copy output/*.html into docs/ so GitHub Pages can render them on phones.

GitHub / Cursor file views show HTML as source. Pages serves docs/ as a website.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
DOCS = ROOT / "docs"

SKIP_OVERWRITE = {
    DOCS / "spcx" / "index.html",
    DOCS / "spcx" / "valuation-model.html",
}

LABELS = (
    ("framework1", "Framework 1 初篩"),
    ("framework2", "Framework 2 深度增長"),
    ("framework3", "Framework 3 估值"),
    ("thesis_tracker", "Thesis Tracker"),
    ("earnings_review", "Earnings Review"),
    ("valuation_model", "估值模型"),
    ("valuation", "估值卡"),
    ("peer_comparison", "同業比較"),
    ("catalyst_calendar", "催化劑日曆"),
    ("interactive_brief", "Interactive Brief"),
    ("one-pager", "One-pager"),
)

HOME_LINK = """<a href="../" style="position:sticky;top:8px;z-index:50;display:inline-flex;margin:8px 0 0 12px;padding:8px 12px;border-radius:999px;background:#fff;border:1px solid #e7e0d5;color:#0f766e;font:700 13px/1 Avenir Next,PingFang TC,sans-serif;text-decoration:none;box-shadow:0 8px 24px rgba(28,25,23,.08)">← 報告目錄</a>
"""


def slug_and_label(stem: str, ticker: str) -> tuple[str, str]:
    rest = stem[len(ticker) + 1 :] if stem.upper().startswith(ticker.upper() + "_") else stem
    for key, label in LABELS:
        if rest == key or rest.endswith("_" + key) or rest.startswith(key):
            return key.replace("_", "-"), label
    slug = re.sub(r"[^a-z0-9]+", "-", rest.lower()).strip("-")
    return slug or "report", rest.replace("_", " ")


def inject_home_link(html: str) -> str:
    if "報告目錄" in html:
        return html
    if "<body>" in html:
        return html.replace("<body>", "<body>\n" + HOME_LINK, 1)
    if "<body " in html:
        return re.sub(r"<body[^>]*>", lambda m: m.group(0) + "\n" + HOME_LINK, html, count=1)
    return html


def collect_pages() -> dict[str, list[dict[str, str]]]:
    pages: dict[str, list[dict[str, str]]] = {}
    for src in sorted(OUTPUT.glob("*.html")):
        match = re.match(r"^([A-Z]{1,6})_(.+)$", src.stem)
        if not match:
            continue
        ticker = match.group(1)
        slug, label = slug_and_label(src.stem, ticker)
        dest_dir = DOCS / ticker.lower()
        dest = dest_dir / f"{slug}.html"
        pages.setdefault(ticker, []).append(
            {
                "src": str(src),
                "dest": str(dest),
                "href": f"./{ticker.lower()}/{slug}.html",
                "label": label,
                "ticker": ticker,
            }
        )
    return pages


def ticker_index_html(ticker: str, items: list[dict[str, str]]) -> str:
    links = "\n".join(
        f'    <a href="./{Path(item["dest"]).name}">{item["label"]}</a>' for item in items
    )
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{ticker} · 互動報告</title>
<style>
  body {{ margin:0; min-height:100vh; font-family:"Iowan Old Style","Songti TC","PingFang TC",serif;
    background:radial-gradient(circle at 12% 0%,#dff7f3 0,transparent 28%),#f4f1ea; color:#1c1917;
    padding:24px 16px 64px; }}
  .wrap {{ max-width:440px; margin:0 auto; }}
  h1 {{ font-family:"Avenir Next","PingFang TC",sans-serif; font-size:1.4rem; margin:0 0 8px; }}
  p {{ color:#78716c; line-height:1.5; }}
  a {{ display:block; margin-top:12px; text-decoration:none; color:#fff; background:#0f766e;
    border-radius:999px; padding:14px 16px; font-weight:800; text-align:center;
    font-family:"Avenir Next","PingFang TC",sans-serif; }}
  a.secondary {{ background:#fff; color:#0f766e; border:1px solid #e7e0d5; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>{ticker} 互動報告</h1>
  <p>喺手機瀏覽器打開呢頁，唔好用 GitHub 檔案檢視（會顯示原始碼）。</p>
{links}
  <a class="secondary" href="../">全部報告目錄</a>
  <p style="margin-top:24px;font-size:.82rem;color:#78716c">此分析僅供研究參考，不構成投資建議。</p>
</div>
</body>
</html>
"""


def hub_html(pages: dict[str, list[dict[str, str]]]) -> str:
    cards = []
    extra = {
        "SPCX": [("./spcx/", "Position Brief（手機投影片）")],
    }
    preferred = ("NVDA", "SPCX", "IREN", "RKLB", "RDW", "MRNA")
    tickers = [t for t in preferred if t in pages] + [
        t for t in pages if t not in preferred
    ]
    for ticker in tickers:
        items = pages[ticker]
        links: list[tuple[str, str]] = list(extra.get(ticker, []))
        links.extend((item["href"], item["label"]) for item in items)
        seen: set[str] = set()
        unique: list[tuple[str, str]] = []
        for href, label in links:
            if href in seen:
                continue
            seen.add(href)
            unique.append((href, label))
        anchors = "\n".join(
            f'      <a href="{href}">{label}</a>' for href, label in unique
        )
        cards.append(
            f"""    <article class="card">
      <h2>{ticker}</h2>
{anchors}
    </article>"""
        )
    body = "\n".join(cards)
    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Stock Analysis · 手機互動報告</title>
<style>
  body {{ margin:0; min-height:100vh; font-family:"Iowan Old Style","Songti TC","PingFang TC",serif;
    background:radial-gradient(circle at 12% 0%,#dff7f3 0,transparent 28%),
      radial-gradient(circle at 88% 8%,#dbeafe 0,transparent 24%),#f4f1ea;
    color:#1c1917; padding:24px 16px 72px; }}
  .wrap {{ max-width:720px; margin:0 auto; }}
  h1 {{ font-family:"Avenir Next","PingFang TC",sans-serif; font-size:1.55rem; margin:0 0 8px; }}
  .lede {{ color:#78716c; line-height:1.55; margin:0 0 22px; }}
  .grid {{ display:grid; gap:14px; }}
  .card {{ background:#fffdf8; border:1px solid #e7e0d5; border-radius:22px; padding:18px 16px;
    box-shadow:0 12px 40px rgba(28,25,23,.08); }}
  h2 {{ font-family:"Avenir Next","PingFang TC",sans-serif; margin:0 0 8px; font-size:1.05rem; }}
  a {{ display:block; margin-top:10px; text-decoration:none; color:#fff; background:#0f766e;
    border-radius:999px; padding:12px 16px; font-weight:800; text-align:center;
    font-family:"Avenir Next","PingFang TC",sans-serif; }}
  .note {{ margin-top:22px; color:#78716c; font-size:.82rem; font-family:"Avenir Next","PingFang TC",sans-serif; }}
</style>
</head>
<body>
  <div class="wrap">
    <h1>手機互動報告</h1>
    <p class="lede">GitHub／Cursor 檔案頁會顯示 HTML 原始碼。用瀏覽器打開呢個 GitHub Pages 目錄，先可以撳、篩選、睇卡片。</p>
    <div class="grid">
{body}
    </div>
    <p class="note">網址：https://keithcheungmk.github.io/stock-analysis/ · 合併到 main 之後先會更新。此分析僅供研究參考，不構成投資建議。</p>
  </div>
</body>
</html>
"""


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    pages = collect_pages()
    copied = 0
    for ticker, items in pages.items():
        dest_dir = DOCS / ticker.lower()
        dest_dir.mkdir(parents=True, exist_ok=True)
        kept: list[dict[str, str]] = []
        for item in items:
            dest = Path(item["dest"])
            if dest in SKIP_OVERWRITE:
                kept.append(item)
                continue
            html = Path(item["src"]).read_text(encoding="utf-8")
            dest.write_text(inject_home_link(html), encoding="utf-8")
            kept.append(item)
            copied += 1
        pages[ticker] = kept
        ticker_index = dest_dir / "index.html"
        if ticker_index not in SKIP_OVERWRITE:
            ticker_index.write_text(ticker_index_html(ticker, kept), encoding="utf-8")
    (DOCS / "index.html").write_text(hub_html(pages), encoding="utf-8")
    print(f"published {copied} html pages into {DOCS}")


if __name__ == "__main__":
    main()
