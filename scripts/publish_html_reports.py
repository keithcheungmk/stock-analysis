#!/usr/bin/env python3
"""Publish interactive HTML into docs/ for GitHub Pages (phone / MacBook Air).

User-facing HTML lives only in docs/. output/*.html is a draft copy.
Always run this after writing a report. Delivery is the Pages URL, never source code.
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
DOCS = ROOT / "docs"

SKIP_OVERWRITE = {
    DOCS / "spcx" / "index.html",
    DOCS / "spcx" / "valuation-model.html",
    DOCS / "tsla" / "index.html",
}

LABELS = (
    ("framework1", "Framework 1 初篩"),
    ("framework2", "Framework 2 深度增長"),
    ("framework3", "Framework 3 估值"),
    ("thesis_tracker", "Thesis Tracker"),
    ("earnings_review", "Earnings Review"),
    ("valuation_model", "估值模型"),
    ("interactive_brief", "Interactive Brief"),
    ("one-pager", "One-pager"),
    ("index", "報告目錄"),
)

HOME_LINK = """<a href="../" style="position:sticky;top:8px;z-index:50;display:inline-flex;margin:8px 0 0 12px;padding:8px 12px;border-radius:999px;background:#fff;border:1px solid #e7e0d5;color:#0f766e;font:700 13px/1 Avenir Next,PingFang TC,sans-serif;text-decoration:none;box-shadow:0 8px 24px rgba(28,25,23,.08)">← 報告目錄</a>
"""

COMMENT_MARK = "id=\"page-comments\""


def slug_and_label(stem: str, ticker: str) -> tuple[str, str]:
    rest = stem[len(ticker) + 1 :] if stem.upper().startswith(ticker.upper() + "_") else stem
    for key, label in LABELS:
        if rest == key or rest.endswith("_" + key) or rest.startswith(key):
            return key.replace("_", "-"), label
    slug = re.sub(r"[^a-z0-9]+", "-", rest.lower()).strip("-")
    return slug or "report", rest.replace("_", " ")


def file_updated(path: Path) -> str:
    if not path.exists():
        return dt.date.today().isoformat()
    return dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.timezone.utc).date().isoformat()


def comment_script_src(html_path: Path) -> str:
    rel = html_path.relative_to(DOCS)
    depth = len(rel.parts) - 1
    return "../" * depth + "assets/page-comments.js"


def comment_mount(html_path: Path) -> str:
    page = "/" + html_path.relative_to(DOCS).as_posix()
    src = comment_script_src(html_path)
    return (
        f'<section id="page-comments" data-page="{page}"></section>\n'
        f'<script src="{src}" defer></script>\n'
    )


def inject_home_link(html: str) -> str:
    if "報告目錄" in html:
        return html
    if "<body>" in html:
        return html.replace("<body>", "<body>\n" + HOME_LINK, 1)
    if "<body " in html:
        return re.sub(r"<body[^>]*>", lambda m: m.group(0) + "\n" + HOME_LINK, html, count=1)
    return html


def inject_comments(html: str, html_path: Path) -> str:
    if COMMENT_MARK in html:
        return html
    mount = comment_mount(html_path)
    if "</body>" in html:
        return html.replace("</body>", mount + "</body>", 1)
    return html + "\n" + mount


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


def scan_docs_pages() -> dict[str, list[dict[str, str]]]:
    """List what is actually live under docs/{ticker}/, including hand-maintained pages."""
    live: dict[str, list[dict[str, str]]] = {}
    for ticker_dir in sorted(p for p in DOCS.iterdir() if p.is_dir() and p.name != "assets"):
        ticker = ticker_dir.name.upper()
        items: list[dict[str, str]] = []
        for html in sorted(ticker_dir.glob("*.html")):
            slug = html.stem
            if slug == "index":
                label = "報告目錄"
                href = f"./{ticker_dir.name}/"
            else:
                _, label = slug_and_label(f"{ticker}_{slug.replace('-', '_')}", ticker)
                if label == slug.replace("-", "_"):
                    label = slug.replace("-", " ").title()
                href = f"./{ticker_dir.name}/{html.name}"
            items.append(
                {
                    "dest": str(html),
                    "href": href,
                    "label": label,
                    "ticker": ticker,
                    "updated": file_updated(html),
                }
            )
        if items:
            live[ticker] = items
    return live


def ticker_index_html(ticker: str, items: list[dict[str, str]], updated: str) -> str:
    links = "\n".join(
        f'    <a href="./{Path(item["dest"]).name}">{item["label"]}</a>'
        for item in items
        if Path(item["dest"]).stem != "index"
    )
    dest = DOCS / ticker.lower() / "index.html"
    html = f"""<!DOCTYPE html>
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
  .badge {{ display:inline-block; margin-left:6px; font-size:.72rem; font-weight:800;
    font-family:"Avenir Next","PingFang TC",sans-serif; background:#0f766e; color:#fff;
    border-radius:999px; padding:3px 8px; vertical-align:middle; }}
  a {{ display:block; margin-top:12px; text-decoration:none; color:#fff; background:#0f766e;
    border-radius:999px; padding:14px 16px; font-weight:800; text-align:center;
    font-family:"Avenir Next","PingFang TC",sans-serif; }}
  a.secondary {{ background:#fff; color:#0f766e; border:1px solid #e7e0d5; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>{ticker} 互動報告 <span class="badge">更新 {updated}</span></h1>
  <p>用瀏覽器打開。頁底可以留意見，下次會跟住改。</p>
{links}
  <a class="secondary" href="../">全部報告目錄</a>
  <p style="margin-top:24px;font-size:.82rem;color:#78716c">此分析僅供研究參考，不構成投資建議。</p>
</div>
</body>
</html>
"""
    return inject_comments(html, dest)


def hub_html(pages: dict[str, list[dict[str, str]]]) -> str:
    extra = {
        "SPCX": [("./spcx/", "Position Brief（手機投影片）")],
        "TSLA": [("./tsla/", "Position Brief（手機投影片）")],
    }
    preferred = ("TSLA", "NVDA", "SPCX", "IREN", "RKLB", "RDW", "MRNA")
    tickers = [t for t in preferred if t in pages] + [t for t in pages if t not in preferred]
    cards = []
    for ticker in tickers:
        items = pages[ticker]
        updated = max((item.get("updated") or "2000-01-01") for item in items)
        links: list[tuple[str, str]] = list(extra.get(ticker, []))
        links.extend((item["href"], item["label"]) for item in items if Path(item["dest"]).stem != "index")
        seen: set[str] = set()
        unique: list[tuple[str, str]] = []
        for href, label in links:
            if href in seen:
                continue
            seen.add(href)
            unique.append((href, label))
        anchors = "\n".join(f'      <a href="{href}">{label}</a>' for href, label in unique)
        cards.append(
            f"""    <article class="card">
      <h2>{ticker} <span class="badge">更新 {updated}</span></h2>
{anchors}
    </article>"""
        )
    body = "\n".join(cards)
    hub_path = DOCS / "index.html"
    html = f"""<!DOCTYPE html>
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
  .badge {{ display:inline-block; margin-left:6px; font-size:.72rem; font-weight:800;
    background:#0f766e; color:#fff; border-radius:999px; padding:3px 8px; vertical-align:middle; }}
  a {{ display:block; margin-top:10px; text-decoration:none; color:#fff; background:#0f766e;
    border-radius:999px; padding:12px 16px; font-weight:800; text-align:center;
    font-family:"Avenir Next","PingFang TC",sans-serif; }}
  .note {{ margin-top:22px; color:#78716c; font-size:.82rem; font-family:"Avenir Next","PingFang TC",sans-serif; }}
</style>
</head>
<body>
  <div class="wrap">
    <h1>手機互動報告</h1>
    <p class="lede">用 Safari／Chrome 打開呢頁。每張報告頁底可以留意見；下次分析會跟住改。唔使睇任何程式碼。</p>
    <div class="grid">
{body}
    </div>
    <p class="note">網址：https://keithcheungmk.github.io/stock-analysis/ · 合併到 main 之後先會更新。<br>Mac 保留完整研究檔案（git pull + OneDrive raw）。此分析僅供研究參考，不構成投資建議。</p>
  </div>
</body>
</html>
"""
    return inject_comments(html, hub_path)


def sweep_inject_comments() -> int:
    n = 0
    for html_path in DOCS.rglob("*.html"):
        if "assets" in html_path.parts:
            continue
        original = html_path.read_text(encoding="utf-8")
        updated = inject_comments(original, html_path)
        if updated != original:
            html_path.write_text(updated, encoding="utf-8")
            n += 1
    return n


def main() -> None:
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS / "assets").mkdir(exist_ok=True)
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
            html = inject_home_link(html)
            html = inject_comments(html, dest)
            dest.write_text(html, encoding="utf-8")
            kept.append(item)
            copied += 1
        pages[ticker] = kept
        ticker_index = dest_dir / "index.html"
        if ticker_index not in SKIP_OVERWRITE:
            updated = max((file_updated(Path(i["dest"])) for i in kept), default=dt.date.today().isoformat())
            ticker_index.write_text(ticker_index_html(ticker, kept, updated), encoding="utf-8")
    n_comments = sweep_inject_comments()
    live = scan_docs_pages()
    (DOCS / "index.html").write_text(hub_html(live), encoding="utf-8")
    print(f"published {copied} html pages into {DOCS}; comment widgets {n_comments}")


if __name__ == "__main__":
    main()
