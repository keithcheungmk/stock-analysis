#!/usr/bin/env python3
"""Publish interactive HTML into docs/ for GitHub Pages (phone / MacBook Air).

User-facing HTML lives only in docs/. output/*.html is a draft copy.
Always run this after writing a report. Delivery is the Pages URL, never source code.
"""

from __future__ import annotations

import datetime as dt
import html as html_lib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
DOCS = ROOT / "docs"

# Ticker index pages are always regenerated. Hand-written summary blocks survive between
# these markers; AMD／IREN／ORCL legacy pages are migrated into markers on first run.
CURATED_START = "<!-- curated:start -->"
CURATED_END = "<!-- curated:end -->"
LEGACY_CURATED_TICKERS = {"AMD", "IREN", "ORCL"}
SKIP_OVERWRITE: set[Path] = set()

REPORT_ORDER = (
    "one-pager",
    "valuation",
    "framework3",
    "framework1",
    "framework2",
    "thesis-tracker",
    "catalyst-calendar",
    "peer-comparison",
    "skill7-option-strategy",
    "options-overlay",
    "interactive-brief",
    "valuation-model",
    "earnings-review",
)
# Most authoritative page wins when several HUDs share the latest commit date.
HUD_PRIORITY = (
    "valuation",
    "one-pager",
    "framework3",
    "thesis-tracker",
    "catalyst-calendar",
    "framework1",
    "framework2",
    "peer-comparison",
)
LABEL_OVERRIDES = {
    ("ORCL", "earnings-review"): "FY2027-Q1 財報複盤",
    ("AMD", "earnings-review"): "Earnings Review（舊尺，已退役）",
    ("SPCX", "options-overlay"): "期權 Overlay",
}
HUB_ORDER = ("TSLA", "NVDA", "SPCX", "IREN", "RKLB", "RDW", "MRNA")

# Tesla／IREN／SPCX 目錄對齊 NVDA／HIMS：只露出同一套標準頁。底稿仍留喺 output/。
# SPCX 2026-08-30 重做：移除舊版 SKIP_OVERWRITE（docs/spcx/index.html 同 valuation-model.html
# 之前係手動維護嘅自訂 slide-deck 首頁），改用同 TSLA/IREN 一致嘅自動生成 hub + HIDE_DOCS_SLUGS 機制。
HIDE_DOCS_SLUGS = {
    "TSLA": {
        "earnings-review",
        "interactive-brief",
        "valuation-model",
    },
    "IREN": {
        "earnings-review",
        "interactive-brief",
        "valuation-model",
    },
    "SPCX": {
        "earnings-review",
        "interactive-brief",
        "valuation-model",
    },
}

LABELS = (
    ("framework1", "Framework 1 初篩"),
    ("framework2", "Framework 2 深度增長"),
    ("framework3", "Framework 3 估值"),
    ("thesis_tracker", "Thesis Tracker"),
    ("earnings_review", "Earnings Review"),
    ("valuation_model", "估值模型"),
    ("interactive_brief", "Interactive Brief"),
    ("one_pager", "one pager"),
    ("one-pager", "one pager"),
    ("valuation", "估值卡"),
    ("peer_comparison", "同業比較"),
    ("catalyst_calendar", "催化劑日曆"),
    ("skill7_option_strategy", "期權策略"),
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


_GIT_DATES: dict[str, str] | None = None


def _git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return ""


def git_dates(refresh: bool = False) -> dict[str, str]:
    """Last commit date per docs/ file; uncommitted changes count as today.

    File mtimes are unreliable (fresh clones / OneDrive sync reset them), so the
    "更新" badges come from git history instead.
    """
    global _GIT_DATES
    if _GIT_DATES is not None and not refresh:
        return _GIT_DATES
    dates: dict[str, str] = {}
    current = ""
    for line in _git("log", "--format=@%cs", "--name-only", "--", "docs").splitlines():
        if line.startswith("@"):
            current = line[1:]
        elif line and line not in dates:
            dates[line] = current
    today = dt.date.today().isoformat()
    for line in _git("status", "--porcelain", "--untracked-files=all", "--", "docs").splitlines():
        path = line[3:].strip().strip('"')
        if path:
            dates[path] = today
    _GIT_DATES = dates
    return dates


def file_updated(path: Path) -> str:
    if not path.exists():
        return dt.date.today().isoformat()
    try:
        rel = path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        rel = ""
    found = git_dates().get(rel)
    if found:
        return found
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
                label = LABEL_OVERRIDES.get((ticker, slug), label)
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


def _text(fragment: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def extract_hud(html: str) -> dict | None:
    """Pull the Decision HUD (tag + label/value/sub cells) out of a report page."""
    match = re.search(
        r'<section[^>]*(?:id="decision-hud"|class="hud[" ])[^>]*>(.*?)</section>', html, re.S
    )
    if not match:
        return None
    section = match.group(1)
    tag = re.search(r'class="hud-tag"[^>]*>(.*?)</span>', section, re.S)
    cells = []
    for cell in re.finditer(
        r'class="l">(.*?)</div>\s*<div class="v">(.*?)</div>(?:\s*<div class="s">(.*?)</div>)?',
        section,
        re.S,
    ):
        cells.append(
            {"l": _text(cell.group(1)), "v": _text(cell.group(2)), "s": _text(cell.group(3) or "")}
        )
    if not cells:
        return None
    return {"tag": _text(tag.group(1)) if tag else "", "cells": cells[:4]}


_PCT = re.compile(r"([+−-])\s?(\d+(?:\.\d+)?)%")


def hud_premium(hud: dict | None) -> tuple[str, float] | None:
    """Return (display text, signed value) for 現價 vs Base, if the HUD states one."""
    if not hud:
        return None
    candidates = [c["v"] for c in hud["cells"] if re.search(r"Base|溢價|折讓", c["l"] + c["v"])]
    candidates.append(hud["tag"])
    for text in candidates:
        found = _PCT.search(text)
        if found:
            sign, number = found.groups()
            value = float(number) * (-1 if sign in "−-" else 1)
            shown = f"{'+' if value >= 0 else '−'}{number}%"
            return shown, value
    return None


def hud_price(hud: dict | None) -> str:
    if not hud:
        return ""
    for cell in hud["cells"]:
        if "現價" in cell["l"] and "vs" not in cell["l"]:
            return cell["v"]
    return ""


def extract_f1(ticker_dir: Path) -> tuple[str, str]:
    page = ticker_dir / "framework1.html"
    if not page.exists():
        return "", ""
    html = page.read_text(encoding="utf-8")
    verdict = re.search(r">\s*(PASS|WATCH|FAIL)\s*<", html)
    score = re.search(r"(?<![\d/] )(?<![\d/])(\d{1,3})\s*[/／]\s*130(?!\s*[/／])", html)
    return (verdict.group(1) if verdict else "", score.group(1) if score else "")


def read_curated(ticker: str, index_path: Path) -> str:
    if not index_path.exists():
        return ""
    html = index_path.read_text(encoding="utf-8")
    if CURATED_START in html and CURATED_END in html:
        return html.split(CURATED_START, 1)[1].split(CURATED_END, 1)[0].lstrip("\n").rstrip()
    if ticker in LEGACY_CURATED_TICKERS and "</h1>" in html:
        body = html.split("</h1>", 1)[1]
        cut = re.search(r"\n\s*<a [^>]*href=\"\./", body)
        return body[: cut.start()].strip("\n") if cut else ""
    return ""


def pick_hud(items: list[dict[str, str]]) -> tuple[dict, dict[str, str]] | None:
    """Newest HUD wins; ties go to the more authoritative page."""
    best = None
    for item in items:
        slug = Path(item["dest"]).stem
        if slug == "index":
            continue
        hud = extract_hud(Path(item["dest"]).read_text(encoding="utf-8"))
        if not hud:
            continue
        rank = HUD_PRIORITY.index(slug) if slug in HUD_PRIORITY else len(HUD_PRIORITY)
        key = (item.get("updated", ""), -rank)
        if best is None or key > best[0]:
            best = (key, hud, item)
    return (best[1], best[2]) if best else None


def ordered_reports(items: list[dict[str, str]]) -> list[dict[str, str]]:
    reports = [i for i in items if Path(i["dest"]).stem != "index"]

    def key(item: dict[str, str]) -> tuple[int, str]:
        slug = Path(item["dest"]).stem
        return (REPORT_ORDER.index(slug) if slug in REPORT_ORDER else len(REPORT_ORDER), slug)

    return sorted(reports, key=key)


def ticker_summary(ticker: str, items: list[dict[str, str]]) -> dict:
    ticker_dir = DOCS / ticker.lower()
    index_path = ticker_dir / "index.html"
    curated = read_curated(ticker, index_path)
    curated_hud = extract_hud(curated) if curated else None
    picked = pick_hud(items)
    hud = curated_hud or (picked[0] if picked else None)
    verdict, score = extract_f1(ticker_dir)
    reports = ordered_reports(items)
    updated = max((r.get("updated") or "2000-01-01") for r in reports) if reports else ""
    return {
        "ticker": ticker,
        "curated": curated,
        "curated_has_hud": bool(curated_hud),
        "hud": hud,
        "hud_source": None if curated_hud or not picked else picked[1],
        "verdict": verdict,
        "score": score,
        "updated": updated,
        "reports": reports,
        "premium": hud_premium(hud),
        "price": hud_price(hud),
    }


def premium_class(premium: tuple[str, float] | None) -> str:
    if not premium:
        return "na"
    value = premium[1]
    if value >= 50:
        return "hot"
    if value >= 10:
        return "warm"
    if value <= -10:
        return "cool"
    return "fair"


BASE_CSS = """
  *{box-sizing:border-box}
  body{margin:0;min-height:100vh;font-family:"Iowan Old Style","Songti TC","PingFang TC",serif;
    background:radial-gradient(circle at 12% 0%,#dff7f3 0,transparent 28%),
      radial-gradient(circle at 88% 8%,#dbeafe 0,transparent 24%),#f4f1ea;
    color:#1c1917;padding:24px 16px 72px}
  .sans,h1,h2,.pill,.tk,.px,.prem,.upd,.legend,.reports a,.back{font-family:"Avenir Next","PingFang TC",sans-serif}
  h1{font-size:1.5rem;margin:0 0 6px}
  .lede{color:#78716c;line-height:1.55;margin:0 0 18px}
  .pill{display:inline-flex;align-items:center;font-size:.72rem;font-weight:800;border-radius:999px;padding:3px 9px;
    vertical-align:middle;background:#e7e5e4;color:#44403c}
  .pill.v-pass{background:#dcfce7;color:#15803d}.pill.v-watch{background:#ffedd5;color:#c2410c}
  .pill.v-fail{background:#fee2e2;color:#b91c1c}.pill.date{background:#0f766e;color:#fff}
  .prem.hot{color:#b91c1c}.prem.warm{color:#c2410c}.prem.cool{color:#15803d}.prem.fair{color:#44403c}.prem.na{color:#a8a29e}
  .note{margin-top:22px;color:#78716c;font-size:.82rem;font-family:"Avenir Next","PingFang TC",sans-serif;line-height:1.5}
"""


def verdict_pill(verdict: str, score: str) -> str:
    if not verdict:
        return '<span class="pill">F1 未做</span>'
    if score:
        text = f"F1 {verdict} {score}"
    elif verdict == "FAIL":
        text = "F1 FAIL · 紅線"
    else:
        text = f"F1 {verdict}"
    return f'<span class="pill v-{verdict.lower()}">{text}</span>'


def hud_block(summary: dict) -> str:
    hud = summary["hud"]
    if not hud:
        return (
            '  <section class="hud" id="decision-hud">\n'
            '    <h2>估值 <span class="hud-tag">未有 Decision HUD</span></h2>\n'
            '    <p class="src">呢隻股票嘅報告頁未有估值尺，請睇下面「估值卡」或 Framework 3。</p>\n'
            "  </section>"
        )
    cells = "\n".join(
        f'      <div class="cell"><div class="l">{html_lib.escape(c["l"])}</div>'
        f'<div class="v">{html_lib.escape(c["v"])}</div>'
        + (f'<div class="s">{html_lib.escape(c["s"])}</div>' if c["s"] else "")
        + "</div>"
        for c in hud["cells"]
    )
    source = summary["hud_source"]
    src = ""
    if source:
        name = Path(source["dest"]).name
        src = (
            f'\n    <p class="src">估值數字來自 <a href="./{name}">{html_lib.escape(source["label"])}</a>'
            f'（更新 {source.get("updated", "")}）。</p>'
        )
    tag = f' <span class="hud-tag">{html_lib.escape(hud["tag"])}</span>' if hud["tag"] else ""
    return (
        '  <section class="hud" id="decision-hud">\n'
        f"    <h2>估值{tag}</h2>\n"
        f'    <div class="grid">\n{cells}\n    </div>{src}\n'
        "  </section>"
    )


def ticker_index_html(ticker: str, summary: dict) -> str:
    dest = DOCS / ticker.lower() / "index.html"
    curated = summary["curated"]
    blocks = []
    if curated:
        blocks.append(f"  {CURATED_START}\n{curated}\n  {CURATED_END}")
    if not summary["curated_has_hud"]:
        blocks.append(hud_block(summary))
    reports = "\n".join(
        f'    <a href="./{Path(r["dest"]).name}"><span class="name">{html_lib.escape(r["label"])}</span>'
        f'<span class="when">更新 {r.get("updated", "")}</span></a>'
        for r in summary["reports"]
    )
    page = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{ticker} · 互動報告</title>
<style>{BASE_CSS}
  .wrap{{max-width:980px;margin:0 auto}}
  .back{{display:inline-flex;margin-bottom:14px;padding:8px 12px;border-radius:999px;background:#fff;border:1px solid #e7e0d5;
    color:#0f766e;font-weight:700;font-size:.85rem;text-decoration:none}}
  .head{{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:14px}}
  .head h1{{margin:0 6px 0 0}}
  .hud{{background:#fffdf8;border:1px solid #e7e0d5;border-radius:20px;padding:16px;margin:0 0 16px;
    box-shadow:0 12px 40px rgba(28,25,23,.08)}}
  .hud h2{{font-size:1rem;margin:0 0 10px}}
  .hud-tag{{display:inline-flex;font-size:.7rem;font-weight:800;color:#9a3412;background:#ffedd5;border-radius:999px;
    padding:2px 9px;margin-left:6px;font-family:"Avenir Next","PingFang TC",sans-serif}}
  .hud .grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}
  @media(max-width:760px){{.hud .grid{{grid-template-columns:1fr 1fr}}}}
  .cell{{border:1px solid #e7e0d5;border-top:3px solid #0f766e;border-radius:12px;padding:10px 12px;background:#fff}}
  .cell .l{{font-size:.72rem;color:#78716c;font-weight:700;font-family:"Avenir Next","PingFang TC",sans-serif}}
  .cell .v{{font-weight:800;font-size:1.05rem;margin-top:3px;font-family:"Avenir Next","PingFang TC",sans-serif}}
  .cell .s{{font-size:.74rem;color:#78716c;margin-top:3px}}
  .action{{margin-top:10px;font-family:"Avenir Next","PingFang TC",sans-serif;font-weight:800;font-size:.86rem;color:#134e4a;
    background:#ccfbf1;border-radius:12px;padding:9px 12px}}
  .fail{{background:#fee2e2;border:1px solid #fca5a5;border-radius:16px;padding:12px 14px;color:#7f1d1d;
    font-family:"Avenir Next","PingFang TC",sans-serif;font-size:.88rem;margin:0 0 16px}}
  .src{{margin:10px 0 0;font-size:.8rem;color:#78716c;font-family:"Avenir Next","PingFang TC",sans-serif}}
  .src a{{color:#0f766e;font-weight:700}}
  .curated > p, .wrap > p{{color:#78716c;line-height:1.5}}
  h2.sec{{font-size:1rem;margin:20px 0 10px}}
  .reports{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:10px}}
  .reports a{{display:flex;flex-direction:column;gap:3px;text-decoration:none;color:#fff;background:#0f766e;border-radius:16px;
    padding:12px 14px;font-weight:800}}
  .reports a:hover{{background:#115e59}}
  .reports .when{{font-size:.72rem;font-weight:600;opacity:.8}}
</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="../">← 全部股票</a>
  <div class="head"><h1>{ticker}</h1>{verdict_pill(summary["verdict"], summary["score"])}<span class="pill date">更新 {summary["updated"]}</span></div>
{chr(10).join(blocks)}
  <h2 class="sec">報告</h2>
  <div class="reports">
{reports}
  </div>
  <p class="note">此分析僅供研究參考，不構成投資建議。</p>
</div>
</body>
</html>
"""
    return inject_comments(page, dest)


def hub_html(summaries: list[dict]) -> str:
    tiles = []
    for s in summaries:
        premium = s["premium"]
        prem_text = f"現價 vs Base {premium[0]}" if premium else ("估值見估值卡" if not s["hud"] else s["hud"]["tag"] or "估值見報告")
        price = f'<div class="px">{html_lib.escape(s["price"])}</div>' if s["price"] else '<div class="px muted">—</div>'
        tiles.append(
            f"""      <a class="tile" href="./{s["ticker"].lower()}/">
        <div class="row"><span class="tk">{s["ticker"]}</span>{verdict_pill(s["verdict"], s["score"])}</div>
        {price}
        <div class="prem {premium_class(premium)}">{html_lib.escape(prem_text)}</div>
        <div class="upd">更新 {s["updated"]} · {len(s["reports"])} 份報告</div>
      </a>"""
        )
    hub_path = DOCS / "index.html"
    page = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Stock Analysis · 互動報告</title>
<style>{BASE_CSS}
  .wrap{{max-width:1120px;margin:0 auto}}
  .legend{{color:#78716c;font-size:.8rem;margin:-8px 0 16px}}
  .tiles{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}}
  @media(max-width:480px){{.tiles{{grid-template-columns:1fr 1fr;gap:10px}}}}
  .tile{{display:flex;flex-direction:column;gap:6px;text-decoration:none;color:inherit;background:#fffdf8;border:1px solid #e7e0d5;
    border-radius:18px;padding:14px;box-shadow:0 10px 30px rgba(28,25,23,.07);transition:transform .12s,box-shadow .12s}}
  .tile:hover{{transform:translateY(-2px);box-shadow:0 14px 36px rgba(28,25,23,.12);border-color:#99f6e4}}
  .row{{display:flex;align-items:center;justify-content:space-between;gap:6px}}
  .tk{{font-size:1.25rem;font-weight:800;color:#0f766e}}
  .px{{font-size:1.05rem;font-weight:800}}
  .px.muted{{color:#a8a29e}}
  .prem{{font-size:.86rem;font-weight:800}}
  .upd{{font-size:.72rem;color:#78716c}}
</style>
</head>
<body>
  <div class="wrap">
    <h1>互動報告</h1>
    <p class="lede">撳入任何一隻股票，先睇估值同全部報告。每張報告頁底可以留意見。</p>
    <p class="legend">顏色：綠＝現價低過 Base（折讓）· 橙／紅＝現價高過 Base（溢價）· 灰＝接近 Base 或未有估值尺</p>
    <div class="tiles">
{chr(10).join(tiles)}
    </div>
    <p class="note">網址：https://keithcheungmk.github.io/stock-analysis/ · 合併到 main 之後先會更新。<br>Mac 保留完整研究檔案（git pull + OneDrive raw）。此分析僅供研究參考，不構成投資建議。</p>
  </div>
</body>
</html>
"""
    return inject_comments(page, hub_path)


def build_summaries(live: dict[str, list[dict[str, str]]]) -> list[dict]:
    tickers = [t for t in HUB_ORDER if t in live] + sorted(t for t in live if t not in HUB_ORDER)
    return [ticker_summary(t, live[t]) for t in tickers]


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
        hide = HIDE_DOCS_SLUGS.get(ticker.upper(), set())
        for item in items:
            dest = Path(item["dest"])
            if dest.stem == "index":
                continue
            if dest.stem in hide:
                if dest.exists():
                    dest.unlink()
                continue
            if dest in SKIP_OVERWRITE:
                continue
            html = Path(item["src"]).read_text(encoding="utf-8")
            html = inject_home_link(html)
            html = inject_comments(html, dest)
            dest.write_text(html, encoding="utf-8")
            copied += 1
    n_comments = sweep_inject_comments()
    git_dates(refresh=True)
    live = scan_docs_pages()
    summaries = build_summaries(live)
    for summary in summaries:
        index_path = DOCS / summary["ticker"].lower() / "index.html"
        index_path.write_text(ticker_index_html(summary["ticker"], summary), encoding="utf-8")
    (DOCS / "index.html").write_text(hub_html(summaries), encoding="utf-8")
    print(f"published {copied} html pages into {DOCS}; comment widgets {n_comments}; tickers {len(summaries)}")


if __name__ == "__main__":
    main()
