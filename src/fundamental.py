"""Fundamental metrics from yfinance info and peer comparison."""

from __future__ import annotations

from typing import Any

import pandas as pd

import yfinance as yf


def _safe_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def extract_fundamentals(info: dict[str, Any]) -> dict[str, Any]:
    """Pull key fundamental fields from ticker info."""
    return {
        "name": info.get("longName") or info.get("shortName"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "market_cap": _safe_float(info.get("marketCap")),
        "enterprise_value": _safe_float(info.get("enterpriseValue")),
        "trailing_pe": _safe_float(info.get("trailingPE")),
        "forward_pe": _safe_float(info.get("forwardPE")),
        "peg_ratio": _safe_float(info.get("pegRatio")),
        "price_to_book": _safe_float(info.get("priceToBook")),
        "profit_margin": _safe_float(info.get("profitMargins")),
        "revenue_growth": _safe_float(info.get("revenueGrowth")),
        "earnings_growth": _safe_float(info.get("earningsGrowth")),
        "free_cashflow": _safe_float(info.get("freeCashflow")),
        "total_revenue": _safe_float(info.get("totalRevenue")),
        "gross_margin": _safe_float(info.get("grossMargins")),
        "operating_margin": _safe_float(info.get("operatingMargins")),
        "beta": _safe_float(info.get("beta")),
        "52w_high": _safe_float(info.get("fiftyTwoWeekHigh")),
        "52w_low": _safe_float(info.get("fiftyTwoWeekLow")),
        "dividend_yield": _safe_float(info.get("dividendYield")),
    }


def format_large_number(value: float | None) -> str:
    if value is None:
        return "N/A"
    abs_val = abs(value)
    if abs_val >= 1e12:
        return f"{value / 1e12:.2f}T"
    if abs_val >= 1e9:
        return f"{value / 1e9:.2f}B"
    if abs_val >= 1e6:
        return f"{value / 1e6:.2f}M"
    return f"{value:,.0f}"


def format_percent(value: float | None, decimals: int = 2) -> str:
    if value is None:
        return "N/A"
    return f"{value * 100:.{decimals}f}%"


def compare_peers(symbols: list[str]) -> pd.DataFrame:
    """Build peer comparison table."""
    rows = []
    for symbol in symbols:
        try:
            info = yf.Ticker(symbol).info or {}
        except Exception:
            continue
        if not info:
            continue
        hist = yf.Ticker(symbol).history(period="1y")
        ytd_return = None
        if len(hist) >= 2:
            ytd_return = (hist["Close"].iloc[-1] / hist["Close"].iloc[0]) - 1

        rows.append(
            {
                "symbol": symbol,
                "name": info.get("shortName") or symbol,
                "price": _safe_float(info.get("currentPrice") or info.get("regularMarketPrice")),
                "market_cap": _safe_float(info.get("marketCap")),
                "trailing_pe": _safe_float(info.get("trailingPE")),
                "forward_pe": _safe_float(info.get("forwardPE")),
                "beta": _safe_float(info.get("beta")),
                "1y_return": ytd_return,
            }
        )

    return pd.DataFrame(rows)
