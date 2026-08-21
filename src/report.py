"""Generate Markdown reports, price charts, and JSON summaries."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

from fundamental import compare_peers, extract_fundamentals, format_large_number, format_percent
from technical import latest_technical_snapshot


def _pct_change(current: float, reference: float) -> str:
    if reference == 0:
        return "N/A"
    return f"{((current / reference) - 1) * 100:+.2f}%"


def build_markdown_report(
    symbol: str,
    hist: pd.DataFrame,
    fundamentals: dict,
    technical: dict,
    peers_df: pd.DataFrame,
    ma_windows: list[int],
) -> str:
    """Assemble full analysis report as Markdown."""
    latest = hist.iloc[-1]
    close = float(latest["Close"])
    start_close = float(hist["Close"].iloc[0])
    high_52w = fundamentals.get("52w_high")
    low_52w = fundamentals.get("52w_low")

    lines = [
        f"# {symbol} Stock Analysis Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- **Company:** {fundamentals.get('name', symbol)}",
        f"- **Sector / Industry:** {fundamentals.get('sector', 'N/A')} / {fundamentals.get('industry', 'N/A')}",
        f"- **Latest Close:** ${close:.2f}",
        f"- **Period Return ({len(hist)} sessions):** {_pct_change(close, start_close)}",
        "",
        "---",
        "",
        "## Technical Analysis",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Close | ${technical['close']:.2f} |",
        f"| Volume | {technical['volume']:,} |",
    ]

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

    lines.extend(
        [
            "",
            "---",
            "",
            "## Fundamentals",
            "",
            "| Metric | Value |",
            "|--------|-------|",
            f"| Market Cap | {format_large_number(fundamentals.get('market_cap'))} |",
            f"| Trailing P/E | {fundamentals.get('trailing_pe') or 'N/A'} |",
            f"| Forward P/E | {fundamentals.get('forward_pe') or 'N/A'} |",
            f"| PEG Ratio | {fundamentals.get('peg_ratio') or 'N/A'} |",
            f"| Profit Margin | {format_percent(fundamentals.get('profit_margin'))} |",
            f"| Gross Margin | {format_percent(fundamentals.get('gross_margin'))} |",
            f"| Revenue Growth | {format_percent(fundamentals.get('revenue_growth'))} |",
            f"| Free Cash Flow | {format_large_number(fundamentals.get('free_cashflow'))} |",
            f"| Beta | {fundamentals.get('beta') or 'N/A'} |",
            f"| 52-Week Range | ${low_52w or 'N/A'} – ${high_52w or 'N/A'} |",
            "",
            "---",
            "",
            "## Peer Comparison",
            "",
            "| Symbol | Price | Market Cap | Trailing P/E | Forward P/E | Beta | 1Y Return |",
            "|--------|-------|------------|--------------|-------------|------|-----------|",
        ]
    )

    for _, row in peers_df.iterrows():
        ret = row.get("1y_return")
        ret_str = format_percent(ret) if pd.notna(ret) else "N/A"
        lines.append(
            f"| {row['symbol']} | ${row['price']:.2f} | {format_large_number(row['market_cap'])} "
            f"| {row['trailing_pe'] or 'N/A'} | {row['forward_pe'] or 'N/A'} "
            f"| {row['beta'] or 'N/A'} | {ret_str} |"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "*Disclaimer: This report is for research and educational purposes only. "
            "It is not investment advice.*",
            "",
        ]
    )

    return "\n".join(lines)


def save_report(content: str, symbol: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    path = output_dir / f"{symbol}_{date_str}_report.md"
    path.write_text(content, encoding="utf-8")
    return path


def plot_price_chart(
    df: pd.DataFrame,
    symbol: str,
    ma_windows: list[int],
    output_dir: Path,
) -> Path:
    """Save price + MA chart and volume subplot."""
    output_dir.mkdir(parents=True, exist_ok=True)
    fig, (ax_price, ax_vol) = plt.subplots(
        2, 1, figsize=(12, 7), sharex=True, gridspec_kw={"height_ratios": [3, 1]}
    )

    dates = df.index
    ax_price.plot(dates, df["Close"], label="Close", color="#1f77b4", linewidth=1.5)
    colors = ["#ff7f0e", "#2ca02c", "#d62728"]
    for i, w in enumerate(ma_windows):
        col = f"MA{w}"
        if col in df.columns:
            ax_price.plot(dates, df[col], label=col, color=colors[i % len(colors)], linewidth=1, alpha=0.85)

    ax_price.set_title(f"{symbol} — Price & Moving Averages (1Y)")
    ax_price.set_ylabel("Price (USD)")
    ax_price.legend(loc="upper left")
    ax_price.grid(True, alpha=0.3)

    ax_vol.bar(dates, df["Volume"], color="#9467bd", alpha=0.5, width=1.0)
    ax_vol.set_ylabel("Volume")
    ax_vol.set_xlabel("Date")
    ax_vol.grid(True, alpha=0.3)

    ax_vol.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    fig.autofmt_xdate()
    fig.tight_layout()

    path = output_dir / f"{symbol}_chart.png"
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def export_summary_json(
    symbol: str,
    hist: pd.DataFrame,
    fundamentals: dict,
    technical: dict,
    peers_df: pd.DataFrame,
    output_dir: Path,
) -> Path:
    """Export structured summary for Cursor Skill / Canvas."""
    weekly_close = hist["Close"].resample("W").last().dropna()
    price_series = [
        {"date": d.strftime("%Y-%m-%d"), "close": round(float(v), 2)}
        for d, v in weekly_close.items()
    ]

    period_return = None
    if len(hist) >= 2:
        period_return = round(
            (float(hist["Close"].iloc[-1]) / float(hist["Close"].iloc[0]) - 1) * 100, 2
        )

    peers = []
    for _, row in peers_df.iterrows():
        ret = row.get("1y_return")
        peers.append(
            {
                "symbol": row["symbol"],
                "price": round(float(row["price"]), 2) if pd.notna(row["price"]) else None,
                "market_cap_b": round(float(row["market_cap"]) / 1e9, 2)
                if pd.notna(row["market_cap"])
                else None,
                "trailing_pe": round(float(row["trailing_pe"]), 2)
                if pd.notna(row["trailing_pe"])
                else None,
                "beta": round(float(row["beta"]), 2) if pd.notna(row["beta"]) else None,
                "return_1y_pct": round(float(ret) * 100, 2) if pd.notna(ret) else None,
            }
        )

    payload = {
        "symbol": symbol,
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "summary": {
            "name": fundamentals.get("name"),
            "close": round(technical["close"], 2),
            "period_return_pct": period_return,
            "rsi": technical.get("rsi"),
            "rsi_signal": technical.get("rsi_signal"),
            "macd_bullish": technical.get("macd_bullish"),
            "above_ma20": technical.get("above_ma20"),
            "above_ma50": technical.get("above_ma50"),
            "above_ma200": technical.get("above_ma200"),
        },
        "fundamentals": {
            "market_cap_b": round(fundamentals["market_cap"] / 1e9, 2)
            if fundamentals.get("market_cap")
            else None,
            "trailing_pe": fundamentals.get("trailing_pe"),
            "forward_pe": fundamentals.get("forward_pe"),
            "beta": fundamentals.get("beta"),
            "profit_margin_pct": round(fundamentals["profit_margin"] * 100, 2)
            if fundamentals.get("profit_margin")
            else None,
            "revenue_growth_pct": round(fundamentals["revenue_growth"] * 100, 2)
            if fundamentals.get("revenue_growth")
            else None,
            "52w_low": fundamentals.get("52w_low"),
            "52w_high": fundamentals.get("52w_high"),
        },
        "price_series_weekly": price_series,
        "peers": peers,
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{symbol}_summary.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path
