"""Technical indicators: moving averages, RSI, MACD."""

from __future__ import annotations

import pandas as pd


def add_moving_averages(
    df: pd.DataFrame,
    windows: list[int],
    price_col: str = "Close",
) -> pd.DataFrame:
    """Add SMA columns for each window."""
    out = df.copy()
    for w in windows:
        out[f"MA{w}"] = out[price_col].rolling(window=w, min_periods=w).mean()
    return out


def compute_rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """Relative Strength Index."""
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)
    avg_gain = gain.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, min_periods=period, adjust=False).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    return 100 - (100 / (1 + rs))


def add_rsi(df: pd.DataFrame, period: int = 14, price_col: str = "Close") -> pd.DataFrame:
    out = df.copy()
    out[f"RSI{period}"] = compute_rsi(out[price_col], period=period)
    return out


def add_macd(
    df: pd.DataFrame,
    fast: int = 12,
    slow: int = 26,
    signal: int = 9,
    price_col: str = "Close",
) -> pd.DataFrame:
    """MACD line, signal line, and histogram."""
    out = df.copy()
    ema_fast = out[price_col].ewm(span=fast, adjust=False).mean()
    ema_slow = out[price_col].ewm(span=slow, adjust=False).mean()
    out["MACD"] = ema_fast - ema_slow
    out["MACD_signal"] = out["MACD"].ewm(span=signal, adjust=False).mean()
    out["MACD_hist"] = out["MACD"] - out["MACD_signal"]
    return out


def run_technical_analysis(
    df: pd.DataFrame,
    ma_windows: list[int],
    rsi_period: int = 14,
    macd_params: dict | None = None,
) -> pd.DataFrame:
    """Apply all technical indicators."""
    macd_params = macd_params or {"fast": 12, "slow": 26, "signal": 9}
    out = add_moving_averages(df, ma_windows)
    out = add_rsi(out, period=rsi_period)
    out = add_macd(out, **macd_params)
    return out


def latest_technical_snapshot(df: pd.DataFrame, ma_windows: list[int]) -> dict:
    """Summary of latest technical readings."""
    row = df.iloc[-1]
    close = float(row["Close"])
    snapshot: dict = {
        "close": close,
        "volume": int(row["Volume"]),
    }

    for w in ma_windows:
        col = f"MA{w}"
        if col in df.columns and pd.notna(row[col]):
            ma_val = float(row[col])
            snapshot[f"ma{w}"] = ma_val
            snapshot[f"above_ma{w}"] = close > ma_val

    rsi_cols = [c for c in df.columns if c.startswith("RSI")]
    if rsi_cols:
        rsi = float(row[rsi_cols[0]])
        snapshot["rsi"] = round(rsi, 2)
        if rsi >= 70:
            snapshot["rsi_signal"] = "overbought"
        elif rsi <= 30:
            snapshot["rsi_signal"] = "oversold"
        else:
            snapshot["rsi_signal"] = "neutral"

    if "MACD" in df.columns and pd.notna(row["MACD"]):
        snapshot["macd"] = round(float(row["MACD"]), 4)
        snapshot["macd_signal_line"] = round(float(row["MACD_signal"]), 4)
        snapshot["macd_hist"] = round(float(row["MACD_hist"]), 4)
        snapshot["macd_bullish"] = float(row["MACD"]) > float(row["MACD_signal"])

    return snapshot
