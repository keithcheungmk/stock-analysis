"""Explosion detection for Tesla AI framework.

Detects EPS and Price explosion conditions per TESLA_AI_FRAMEWORK.md definition C.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import pandas as pd
import yfinance as yf


# Thresholds from framework definition C
EPS_BEAT_THRESHOLD_PCT = 15.0  # Single quarter EPS vs consensus beat > 15%
PRICE_3M_RETURN_THRESHOLD_PCT = 30.0  # 3-month return > 30%


@dataclass
class EPSConsensus:
    """EPS consensus estimate and actual."""
    quarter: str
    fiscal_year: int
    consensus_eps: float | None  # from analysts
    actual_eps: float | None  # reported
    surprise_pct: float | None  # (actual - consensus) / abs(consensus) * 100
    source: str = "yfinance"  # or "manual"


@dataclass
class ExplosionStatus:
    """Current explosion detection status."""
    symbol: str
    as_of_date: str
    
    # EPS explosion metrics
    last_quarter: str | None
    last_actual_eps: float | None
    last_consensus_eps: float | None
    last_surprise_pct: float | None
    eps_explosion_triggered: bool  # |beat| > 15%
    
    # Price explosion metrics
    price_3m_return_pct: float | None
    price_3m_start: float | None
    price_3m_end: float | None
    price_explosion_triggered: bool  # > 30%
    
    # Combined assessment
    eps_explosion_pressure: str  # "high", "moderate", "low", "unknown"
    price_explosion_pressure: str  # "high", "moderate", "low", "unknown"
    
    # Context
    next_earnings_estimate: str | None
    explanation: str = ""


def fetch_earnings_history(symbol: str) -> list[dict]:
    """Fetch earnings history from yfinance."""
    try:
        ticker = yf.Ticker(symbol)
        earnings = ticker.earnings_dates
        if earnings is None or earnings.empty:
            return []
        
        results = []
        for idx, row in earnings.iterrows():
            results.append({
                "date": idx.strftime("%Y-%m-%d") if hasattr(idx, 'strftime') else str(idx),
                "eps_estimate": row.get("EPS Estimate") if isinstance(row, pd.Series) else None,
                "reported_eps": row.get("Reported EPS") if isinstance(row, pd.Series) else None,
                "surprise_pct": row.get("Surprise(%)") if isinstance(row, pd.Series) else None,
            })
        return results
    except Exception as e:
        print(f"Warning: Could not fetch earnings history: {e}")
        return []


def get_last_quarter_eps_data(symbol: str) -> EPSConsensus | None:
    """Get most recent quarter EPS vs consensus."""
    history = fetch_earnings_history(symbol)
    
    # Find most recent with actual reported EPS
    for entry in history:
        if entry.get("reported_eps") is not None and entry.get("eps_estimate") is not None:
            actual = float(entry["reported_eps"])
            consensus = float(entry["eps_estimate"])
            surprise = ((actual - consensus) / abs(consensus)) * 100 if consensus != 0 else None
            
            return EPSConsensus(
                quarter=entry["date"][:7],  # YYYY-MM as proxy for quarter
                fiscal_year=int(entry["date"][:4]),
                consensus_eps=consensus,
                actual_eps=actual,
                surprise_pct=surprise,
                source="yfinance"
            )
    
    return None


def calculate_3m_return(symbol: str) -> tuple[float, float, float] | None:
    """Calculate 3-month price return. Returns (start_price, end_price, return_pct)."""
    try:
        ticker = yf.Ticker(symbol)
        # Get ~3 months of daily data
        hist = ticker.history(period="3mo", interval="1d")
        
        if len(hist) < 30:
            return None
        
        start_price = float(hist["Close"].iloc[0])
        end_price = float(hist["Close"].iloc[-1])
        return_pct = ((end_price - start_price) / start_price) * 100
        
        return (start_price, end_price, return_pct)
    except Exception as e:
        print(f"Warning: Could not calculate 3M return: {e}")
        return None


def detect_explosion(
    symbol: str,
    milestones_config: dict | None = None
) -> ExplosionStatus:
    """Main explosion detection function."""
    symbol = symbol.upper()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Fetch EPS data
    eps_data = get_last_quarter_eps_data(symbol)
    
    # Fetch 3M return
    return_data = calculate_3m_return(symbol)
    
    # Determine EPS explosion status
    eps_explosion = False
    eps_pressure = "unknown"
    last_q = None
    last_actual = None
    last_consensus = None
    last_surprise = None
    
    if eps_data and eps_data.surprise_pct is not None:
        last_q = eps_data.quarter
        last_actual = eps_data.actual_eps
        last_consensus = eps_data.consensus_eps
        last_surprise = eps_data.surprise_pct
        eps_explosion = abs(eps_data.surprise_pct) > EPS_BEAT_THRESHOLD_PCT
        
        # Pressure assessment (not current explosion, but potential)
        if eps_data.surprise_pct > 10:
            eps_pressure = "high"
        elif eps_data.surprise_pct > 0:
            eps_pressure = "moderate"
        elif eps_data.surprise_pct > -10:
            eps_pressure = "low"
        else:
            eps_pressure = "negative"
    
    # Determine Price explosion status
    price_explosion = False
    price_pressure = "unknown"
    start_3m = None
    end_3m = None
    ret_3m = None
    
    if return_data:
        start_3m, end_3m, ret_3m = return_data
        price_explosion = ret_3m > PRICE_3M_RETURN_THRESHOLD_PCT
        
        if ret_3m > 25:
            price_pressure = "high"
        elif ret_3m > 15:
            price_pressure = "moderate"
        elif ret_3m > 0:
            price_pressure = "low"
        else:
            price_pressure = "negative"
    
    # Build explanation
    explanation_parts = []
    
    if eps_explosion:
        explanation_parts.append(
            f"EPS explosion TRIGGERED: {last_q} actual ${last_actual:.2f} vs consensus ${last_consensus:.2f} "
            f"({last_surprise:+.1f}% surprise, threshold ±{EPS_BEAT_THRESHOLD_PCT}%)"
        )
    elif eps_data:
        explanation_parts.append(
            f"EPS: {last_q} surprise {last_surprise:+.1f}% (below {EPS_BEAT_THRESHOLD_PCT}% threshold)"
        )
    else:
        explanation_parts.append("EPS data unavailable from yfinance")
    
    if price_explosion:
        explanation_parts.append(
            f"Price explosion TRIGGERED: 3M return +{ret_3m:.1f}% (threshold +{PRICE_3M_RETURN_THRESHOLD_PCT}%)"
        )
    elif return_data:
        direction = "+" if ret_3m and ret_3m > 0 else ""
        explanation_parts.append(
            f"Price: 3M return {direction}{ret_3m:.1f}% (below {PRICE_3M_RETURN_THRESHOLD_PCT}% threshold)"
        )
    else:
        explanation_parts.append("Price data unavailable")
    
    return ExplosionStatus(
        symbol=symbol,
        as_of_date=today,
        last_quarter=last_q,
        last_actual_eps=last_actual,
        last_consensus_eps=last_consensus,
        last_surprise_pct=last_surprise,
        eps_explosion_triggered=eps_explosion,
        price_3m_return_pct=ret_3m,
        price_3m_start=start_3m,
        price_3m_end=end_3m,
        price_explosion_triggered=price_explosion,
        eps_explosion_pressure=eps_pressure,
        price_explosion_pressure=price_pressure,
        next_earnings_estimate=None,  # Would need calendar API
        explanation="; ".join(explanation_parts)
    )


def format_explosion_report(status: ExplosionStatus) -> str:
    """Format explosion status as markdown report section."""
    lines = [
        "## Explosion Detection (Definition C)",
        "",
        f"**As of:** {status.as_of_date}",
        "",
        "### EPS Explosion (Single quarter vs consensus > 15%)",
        "",
    ]
    
    if status.last_quarter:
        triggered = "🔥 **TRIGGERED**" if status.eps_explosion_triggered else "Not triggered"
        lines.extend([
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Last quarter | {status.last_quarter} |",
            f"| Actual EPS | ${status.last_actual_eps:.2f}" if status.last_actual_eps else "| Actual EPS | N/A |",
            f"| Consensus EPS | ${status.last_consensus_eps:.2f}" if status.last_consensus_eps else "| Consensus EPS | N/A |",
            f"| Surprise | {status.last_surprise_pct:+.1f}% |" if status.last_surprise_pct else "| Surprise | N/A |",
            f"| Status | {triggered} |",
            "",
            f"**Pressure assessment:** {status.eps_explosion_pressure}",
            "",
        ])
    else:
        lines.extend([
            "*EPS data unavailable from yfinance. Consider manual input or alternative source.*",
            "",
        ])
    
    lines.extend([
        "### Price Explosion (3-month return > 30%)",
        "",
    ])
    
    if status.price_3m_return_pct is not None:
        triggered = "🔥 **TRIGGERED**" if status.price_explosion_triggered else "Not triggered"
        lines.extend([
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| 3M start price | ${status.price_3m_start:.2f}" if status.price_3m_start else "| 3M start price | N/A |",
            f"| Current price | ${status.price_3m_end:.2f}" if status.price_3m_end else "| Current price | N/A |",
            f"| 3M return | {status.price_3m_return_pct:+.1f}% |",
            f"| Status | {triggered} |",
            "",
            f"**Pressure assessment:** {status.price_explosion_pressure}",
            "",
        ])
    else:
        lines.extend([
            "*Price data unavailable.*",
            "",
        ])
    
    lines.extend([
        "### Summary",
        "",
        f"{status.explanation}",
        "",
    ])
    
    return "\n".join(lines)


def save_explosion_status(status: ExplosionStatus, output_dir: Path) -> Path:
    """Save explosion status as JSON."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{status.symbol.lower()}_explosion.json"
    path = output_dir / filename
    
    path.write_text(json.dumps(asdict(status), indent=2), encoding="utf-8")
    return path


def load_explosion_history(symbol: str, output_dir: Path) -> list[dict]:
    """Load historical explosion detection results."""
    pattern = f"{symbol.lower()}_*_explosion.json"
    files = sorted(output_dir.glob(pattern))
    
    history = []
    for f in files[-10:]:  # Last 10
        data = json.loads(f.read_text(encoding="utf-8"))
        history.append(data)
    
    return history


if __name__ == "__main__":
    # Demo
    print("Explosion Detection Module")
    print("Usage: detect_explosion(symbol)")
