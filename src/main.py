#!/usr/bin/env python3
"""Stock analysis CLI — fetch data, compute indicators, write report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

# Allow running as script from project root or src/
SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from data_fetcher import cache_history, fetch_history, fetch_info, fetch_peer_histories
from fundamental import compare_peers, extract_fundamentals
from report import build_markdown_report, export_summary_json, plot_price_chart, save_report
from tesla_ai_report import build_tesla_ai_report, save_tesla_ai_report
from technical import latest_technical_snapshot, run_technical_analysis


def load_config(config_path: Path) -> dict:
    with config_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def analyze(symbol: str, config: dict, project_root: Path) -> dict:
    output_dir = project_root / config.get("output_dir", "output")
    period = config.get("history_period", "1y")
    interval = config.get("history_interval", "1d")
    ma_windows = config["technical"]["ma_windows"]
    rsi_period = config["technical"]["rsi_period"]
    macd_params = config["technical"]["macd"]
    peers = config.get("peers", [])

    print(f"Fetching {symbol} price history ({period})...")
    hist = fetch_history(symbol, period=period, interval=interval)
    cache_history(hist, symbol, output_dir)

    print("Fetching fundamentals...")
    info = fetch_info(symbol)
    fundamentals = extract_fundamentals(info)

    print("Running technical analysis...")
    analyzed = run_technical_analysis(
        hist,
        ma_windows=ma_windows,
        rsi_period=rsi_period,
        macd_params=macd_params,
    )
    technical = latest_technical_snapshot(analyzed, ma_windows)

    all_symbols = [symbol] + [p for p in peers if p != symbol]
    print(f"Comparing peers: {', '.join(all_symbols)}...")
    peers_df = compare_peers(all_symbols)

    # TSLA AI Mode: Use specialized report with explosion detection and transcript analysis
    if symbol.upper() == "TSLA":
        print("Generating TESLA AI report (Phase 3b: Explosion + Transcript)...")
        report_md = build_tesla_ai_report(
            symbol=symbol,
            hist=analyzed,
            fundamentals=fundamentals,
            technical=technical,
            peers_df=peers_df,
            ma_windows=ma_windows,
            project_root=project_root,
            # Transcript inputs - currently None, can be passed via CLI in Phase 3c
            transcript_text=None,
            transcript_quarter=None,
            transcript_year=None,
        )
        report_path = save_tesla_ai_report(report_md, symbol, output_dir)
    else:
        print("Generating standard report...")
        report_md = build_markdown_report(
            symbol=symbol,
            hist=analyzed,
            fundamentals=fundamentals,
            technical=technical,
            peers_df=peers_df,
            ma_windows=ma_windows,
        )
        report_path = save_report(report_md, symbol, output_dir)

    print("Saving chart...")
    chart_path = plot_price_chart(analyzed, symbol, ma_windows, output_dir)

    print("Exporting JSON summary...")
    json_path = export_summary_json(
        symbol=symbol,
        hist=analyzed,
        fundamentals=fundamentals,
        technical=technical,
        peers_df=peers_df,
        output_dir=output_dir,
    )

    # Cache peer histories (optional, for future use)
    fetch_peer_histories(peers, period=period, interval=interval)

    return {
        "symbol": symbol,
        "close": technical["close"],
        "report": report_path,
        "chart": chart_path,
        "json": json_path,
        "history_rows": len(analyzed),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run stock analysis for a given symbol.")
    parser.add_argument(
        "symbol",
        nargs="?",
        default=None,
        help="Ticker symbol (e.g. TSLA). Defaults to config default_symbol.",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to config.yaml",
    )
    args = parser.parse_args()

    project_root = SRC_DIR.parent
    config_path = args.config or (project_root / "config.yaml")
    if not config_path.exists():
        print(f"Config not found: {config_path}", file=sys.stderr)
        return 1

    config = load_config(config_path)
    symbol = (args.symbol or config.get("default_symbol", "TSLA")).upper()

    try:
        result = analyze(symbol, config, project_root)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print()
    print(f"Done — {result['symbol']} @ ${result['close']:.2f}")
    print(f"  Report: {result['report']}")
    print(f"  Chart:  {result['chart']}")
    print(f"  JSON:   {result['json']}")
    print(f"  Bars:   {result['history_rows']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
