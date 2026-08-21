"""Fetch stock price history and basic info via yfinance."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import yfinance as yf


def fetch_history(
    symbol: str,
    period: str = "1y",
    interval: str = "1d",
) -> pd.DataFrame:
    """Download OHLCV history for a symbol."""
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period, interval=interval)
    if hist.empty:
        raise ValueError(f"No price history returned for {symbol}")
    hist.index = pd.to_datetime(hist.index).tz_localize(None)
    return hist


def fetch_info(symbol: str) -> dict[str, Any]:
    """Download ticker metadata (market cap, P/E, etc.)."""
    ticker = yf.Ticker(symbol)
    info = ticker.info or {}
    if not info:
        raise ValueError(f"No info returned for {symbol}")
    return info


def fetch_peer_histories(
    symbols: list[str],
    period: str = "1y",
    interval: str = "1d",
) -> dict[str, pd.DataFrame]:
    """Download history for multiple symbols; skip failures."""
    results: dict[str, pd.DataFrame] = {}
    for symbol in symbols:
        try:
            results[symbol] = fetch_history(symbol, period=period, interval=interval)
        except ValueError:
            continue
    return results


def cache_history(
    df: pd.DataFrame,
    symbol: str,
    output_dir: Path,
) -> Path:
    """Save history CSV for reuse."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{symbol}_history.csv"
    df.to_csv(path)
    return path
