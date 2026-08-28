"""Tesla AI-specific report builder integrating explosion detection and transcript analysis.

Phase 3b: Combines standard technical/fundamental with AI framework layers.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from explosion import ExplosionStatus, detect_explosion, format_explosion_report
from transcript import (
    QuarterTranscript,
    QoQDiff,
    analyze_transcript,
    compare_qoq,
    format_transcript_summary,
    load_previous_analysis,
    save_transcript_analysis,
)


def load_tesla_milestones(project_root: Path) -> dict:
    """Load milestones config."""
    path = project_root / "config" / "tesla_milestones.yaml"
    if path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return {}


def load_tesla_peers(project_root: Path) -> dict:
    """Load AI peers config."""
    path = project_root / "config" / "tesla_peers.yaml"
    if path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    return {"robotaxi": [], "humanoid": [], "auto_anchors": []}


def format_peer_table(peers_config: dict) -> str:
    """Format AI peers as markdown table."""
    lines = ["### Robotaxi Peers", "", "| Company | Focus | Track |", "|---------|-------|-------|"]
    
    for p in peers_config.get("robotaxi", []):
        focus = p.get("focus", "")
        track = p.get("track", "")
        lines.append(f"| {p['name']} ({p['symbol'] or 'N/A'}) | {focus} | {track} |")
    
    lines.extend(["", "### Humanoid Peers", "", "| Company | Focus | Track |", "|---------|-------|-------|"])
    
    for p in peers_config.get("humanoid", []):
        parent = f"({p.get('parent')})" if p.get('parent') else ""
        focus = p.get("focus", "")
        track = p.get("track", "")
        lines.append(f"| {p['name']} {parent} | {focus} | {track} |")
    
    return "\n".join(lines)


def build_tesla_ai_report(
    symbol: str,
    hist: Any,  # pd.DataFrame
    fundamentals: dict,
    technical: dict,
    peers_df: Any,  # pd.DataFrame
    ma_windows: list[int],
    project_root: Path,
    # Optional AI-specific inputs
    transcript_text: str | None = None,
    transcript_quarter: str | None = None,
    transcript_year: int | None = None,
) -> str:
    """Build comprehensive Tesla AI report following TESLA_AI_FRAMEWORK."""
    
    from report import _pct_change, format_large_number, format_percent
    
    output_dir = project_root / "output"
    milestones = load_tesla_milestones(project_root)
    peers_config = load_tesla_peers(project_root)
    
    # Get explosion detection
    explosion_status = detect_explosion(symbol)
    
    # Process transcript if provided
    transcript_section = ""
    if transcript_text and transcript_quarter and transcript_year:
        transcript = analyze_transcript(symbol, transcript_quarter, transcript_year, transcript_text)
        prev = load_previous_analysis(
            symbol,
            output_dir,
            exclude_quarter=transcript_quarter,
            exclude_fiscal_year=transcript_year,
        )
        diff = compare_qoq(transcript, prev)
        save_transcript_analysis(transcript, output_dir)
        transcript_section = format_transcript_summary(transcript, diff)
    else:
        transcript_section = """## Earnings Call Analysis

*No transcript provided for this run. To enable transcript analysis:*
1. Save transcript as `input/tsla_qX_fyYYYY.txt`
2. Re-run with `--transcript` flag (Phase 3c)

*Or manually populate `config/tesla_milestones.yaml` with key quotes.*
"""
    
    # Standard technical/fundamental sections
    latest = hist.iloc[-1]
    close = float(latest["Close"])
    start_close = float(hist["Close"].iloc[0])
    high_52w = fundamentals.get("52w_high")
    low_52w = fundamentals.get("52w_low")
    
    # Layer keyword counts from milestones if available
    milestones_meta = milestones.get("meta", {})
    
    lines = [
        f"# {symbol} AI Analysis Report (Tesla Framework)",
        "",
        f"**Generated:** {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## 雙軌結論 (Dual-Track Summary)",
        "",
    ]
    
    # Dual-track conclusions
    eps_status = "🔥 已觸發" if explosion_status.eps_explosion_triggered else f"壓力: {explosion_status.eps_explosion_pressure}"
    price_status = "🔥 已觸發" if explosion_status.price_explosion_triggered else f"壓力: {explosion_status.price_explosion_pressure}"
    
    lines.extend([
        f"**EPS 爆發壓力:** {eps_status}",
        "",
        f"- 定義: 單季 EPS vs consensus > 15% beat",
        f"- 最新: Q{explosion_status.last_quarter or 'N/A'} actual ${explosion_status.last_actual_eps or 'N/A'} vs consensus ${explosion_status.last_consensus_eps or 'N/A'}" if explosion_status.last_quarter else "- 最新數據: 從 yfinance 取得",
        "",
        f"**股價爆發壓力:** {price_status}",
        "",
        f"- 定義: 3 個月回報 > +30%",
        f"- 最新: {explosion_status.price_3m_return_pct:+.1f}%" if explosion_status.price_3m_return_pct else "- 最新數據: 計算中",
        "",
        "---",
        "",
        "## 四層價值快照 (Value Stack Snapshot)",
        "",
        "| Layer | Status | Key Metrics |",
        "|-------|--------|-------------|",
        f"| L1 Auto+Energy | Active | Close ${close:.2f}, 1Y Return {_pct_change(close, start_close)} |",
        f"| L2 FSD/AI | Monitoring | RSI {technical.get('rsi', 'N/A')}, MACD {'bullish' if technical.get('macd_bullish') else 'bearish'} |",
        "| L3 Robotaxi | Narrative | See transcript section below |",
        "| L4 Optimus | Early | Pre-commercial, milestone tracking |",
        "",
        "---",
        "",
    ])
    
    # Explosion detection section
    lines.append(format_explosion_report(explosion_status))
    lines.extend(["", "---", ""])
    
    # Technical Analysis
    lines.extend([
        "## 技術面 (Secondary Weight for AI Valuation)",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Close | ${technical['close']:.2f} |",
        f"| Volume | {technical['volume']:,} |",
    ])
    
    for w in ma_windows:
        key = f"ma{w}"
        if key in technical:
            above = "above" if technical.get(f"above_ma{w}") else "below"
            lines.append(f"| MA{w} | ${technical[key]:.2f} ({above}) |")
    
    if "rsi" in technical:
        lines.append(f"| RSI | {technical['rsi']} ({technical.get('rsi_signal', '')}) |")
    if "macd" in technical:
        macd_trend = "bullish" if technical.get("macd_bullish") else "bearish"
        lines.append(f"| MACD | {technical['macd']} / signal {technical['macd_signal_line']} ({macd_trend}) |")
    
    lines.extend(["", "---", ""])
    
    # Fundamentals
    lines.extend([
        "## 基本面 (L1 Cash Flow Base)",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Market Cap | {format_large_number(fundamentals.get('market_cap'))} |",
        f"| Trailing P/E | {fundamentals.get('trailing_pe') or 'N/A'} |",
        f"| Forward P/E | {fundamentals.get('forward_pe') or 'N/A'} |",
        f"| Profit Margin | {format_percent(fundamentals.get('profit_margin'))} |",
        f"| Revenue Growth | {format_percent(fundamentals.get('revenue_growth'))} |",
        f"| Beta | {fundamentals.get('beta') or 'N/A'} |",
        f"| 52-Week Range | ${low_52w or 'N/A'} – ${high_52w or 'N/A'} |",
        "",
        "---",
        "",
    ])
    
    # Transcript section
    lines.extend([
        transcript_section,
        "",
        "---",
        "",
    ])
    
    # AI Peers section
    lines.extend([
        "## 同業一頁表 (AI Peers)",
        "",
        format_peer_table(peers_config),
        "",
        "---",
        "",
    ])
    
    # Explosion Watchlist
    watchlist = milestones.get("explosion_watchlist", [])
    lines.extend([
        "## Explosion Watchlist (90 Days)",
        "",
    ])
    
    if watchlist and any(w.get("date") for w in watchlist):
        lines.extend([
            "| Date | Event | Layer | Moves |",
            "|------|-------|-------|-------|",
        ])
        for w in watchlist[:5]:
            if w.get("date"):
                lines.append(f"| {w['date']} | {w.get('event', 'TBD')} | {w.get('layer', '-')} | {w.get('moves', '-')} |")
    else:
        lines.extend([
            "*待填入 `config/tesla_milestones.yaml` 的 `explosion_watchlist` 欄位*",
            "",
            "建議追蹤事件類型:",
            "- Q3 財報發布 (EPS)",
            "- Robotaxi 商業化里程碑 (股價)",
            "- FSD v13+ 重大更新 (兩者)",
            "- Optimus 量產時間表 (股價)",
        ])
    
    lines.extend(["", "---", ""])
    
    # Catalyst Score
    scores = milestones.get("catalyst_scores", {})
    lines.extend([
        "## Catalyst Score (0–10)",
        "",
        "| Dimension | Score | Notes |",
        "|-----------|-------|-------|",
    ])
    
    dimensions = [
        ("eps_upside", "EPS 上行壓力"),
        ("rerating_upside", "估值重估壓力"),
        ("execution_risk", "執行風險 (高=差)"),
        ("regulatory_risk", "監管風險 (高=差)"),
        ("peer_pressure", "同業壓力 (高=落後)"),
    ]
    
    for key, label in dimensions:
        score = scores.get(key, "—")
        note = ""
        if key == "eps_upside" and explosion_status.eps_explosion_pressure != "unknown":
            note = f"基於最新 surprise {explosion_status.last_surprise_pct:+.1f}%" if explosion_status.last_surprise_pct else ""
        elif key == "rerating_upside" and explosion_status.price_explosion_pressure != "unknown":
            note = f"3M return {explosion_status.price_3m_return_pct:+.1f}%" if explosion_status.price_3m_return_pct else ""
        lines.append(f"| {label} | {score} | {note} |")
    
    lines.extend([
        "",
        "*評分標準: 0=無壓力/風險極低, 10=極高壓力/風險*",
        "",
        "---",
        "",
        "*Disclaimer: This report is for research and educational purposes only. "
        "It is not investment advice. Explosion detection uses thresholds "
        f"(EPS beat ±{__import__('explosion').EPS_BEAT_THRESHOLD_PCT}%, 3M return +{__import__('explosion').PRICE_3M_RETURN_THRESHOLD_PCT}%) "
        "but does not predict future performance.*",
        "",
    ])
    
    return "\n".join(lines)


def save_tesla_ai_report(content: str, symbol: str, output_dir: Path) -> Path:
    """Save Tesla AI report."""
    from datetime import datetime
    output_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = output_dir / f"{symbol}_{date_str}_ai_report.md"
    path.write_text(content, encoding="utf-8")
    return path
