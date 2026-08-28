"""Earnings call transcript analysis for Tesla AI framework.

Phase 3b: Manual or API-driven transcript ingestion with QoQ keyword diff.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


# Tesla AI keywords to track across quarters
TESLA_AI_KEYWORDS = [
    # Layer 2: FSD/AI
    "fsd", "full self-driving", "supervised", "unsupervised",
    "end-to-end", "neural network", "training compute", "dojo", "hw4", "hw5",
    # Layer 3: Robotaxi
    "robotaxi", "cybercab", "autonomous fleet", "ride-hailing",
    "austin", "california", "regulatory", "nhtsa", "dmv",
    "safety driver", "driverless", "million miles",
    # Layer 4: Optimus
    "optimus", "humanoid", "gen2", "bipedal",
    "factory deployment", "manufacturing line", "units produced",
    # Financial keywords
    "margin expansion", "software revenue", "subscription", "defer",
    "capex", "ramp", "production rate", "volumes",
]


@dataclass
class KeywordMetrics:
    """Keyword occurrence and context metrics."""
    keyword: str
    count: int
    contexts: list[str]  # surrounding sentences (truncated)
    sentiment_hint: str = "neutral"  # simple: positive/negative/neutral from surrounding words


@dataclass
class QuarterTranscript:
    """Parsed transcript for a single quarter."""
    symbol: str
    quarter: str  # e.g., "Q4 2024"
    fiscal_year: int
    date: str  # ISO format
    source: str  # "manual", "seeking_alpha", "fool"
    raw_text: str
    keywords: list[KeywordMetrics]
    robotaxi_mentions: list[str]  # sentences mentioning robotaxi
    fsd_mentions: list[str]
    optimus_mentions: list[str]
    margin_mentions: list[str]
    guidance_summary: str = ""  # extracted forward-looking statements


def extract_sentences_with_keyword(text: str, keyword: str, window: int = 100) -> list[str]:
    """Extract sentences containing keyword with surrounding context."""
    pattern = re.compile(r'[^.!?]*\b' + re.escape(keyword) + r'\b[^.!?]*[.!?]', re.IGNORECASE)
    matches = pattern.findall(text)
    # Truncate very long matches
    return [m[:window*2] + "..." if len(m) > window*2 else m for m in matches[:5]]


def simple_sentiment(text: str) -> str:
    """Naive sentiment based on positive/negative words."""
    positive = ["growth", "expand", "ramp", "accelerate", "improve", "positive", "milestone",
                "on track", "ahead", "exceeded", "strong", "robust"]
    negative = ["delay", "challenge", "headwind", "pressure", "below", "miss", "concern",
                "cautious", "difficult", "uncertain", "paused", "slower"]
    text_lower = text.lower()
    pos_count = sum(1 for p in positive if p in text_lower)
    neg_count = sum(1 for n in negative if n in text_lower)
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    return "neutral"


def analyze_transcript(symbol: str, quarter: str, fiscal_year: int, text: str, source: str = "manual") -> QuarterTranscript:
    """Analyze a single quarter's transcript."""
    text_lower = text.lower()
    
    keyword_metrics = []
    for kw in TESLA_AI_KEYWORDS:
        count = len(re.findall(r'\b' + re.escape(kw) + r'\b', text_lower))
        if count > 0:
            contexts = extract_sentences_with_keyword(text, kw)
            sentiment = simple_sentiment(" ".join(contexts)) if contexts else "neutral"
            keyword_metrics.append(KeywordMetrics(
                keyword=kw,
                count=count,
                contexts=contexts,
                sentiment_hint=sentiment
            ))
    
    # Extract special mentions
    robotaxi_sents = extract_sentences_with_keyword(text, "robotaxi", window=150)
    fsd_sents = extract_sentences_with_keyword(text, "fsd", window=150)
    optimus_sents = extract_sentences_with_keyword(text, "optimus", window=150)
    margin_sents = extract_sentences_with_keyword(text, "margin", window=150)
    
    # Extract guidance section (looking for Q&A or forward-looking)
    guidance_patterns = [
        r'(?:guidance|outlook|forward|expect|anticipate).*?(?:\n\n|\Z)',
        r'(?:next quarter|next year|fiscal \d{4}).*?(?:\n\n|\Z)',
    ]
    guidance = ""
    for pattern in guidance_patterns:
        matches = re.findall(pattern, text_lower[:10000], re.DOTALL)
        if matches:
            guidance = matches[0][:500]
            break
    
    return QuarterTranscript(
        symbol=symbol.upper(),
        quarter=quarter,
        fiscal_year=fiscal_year,
        date=datetime.now().strftime("%Y-%m-%d"),
        source=source,
        raw_text=text[:5000] + "..." if len(text) > 5000 else text,  # Truncate for storage
        keywords=keyword_metrics,
        robotaxi_mentions=robotaxi_sents[:10],
        fsd_mentions=fsd_sents[:10],
        optimus_mentions=optimus_sents[:10],
        margin_mentions=margin_sents[:10],
        guidance_summary=guidance[:300]
    )


def _quarter_number(quarter: str) -> int:
    """Parse quarter index (1–4) from labels like 'Q4' or 'Q4 2024'."""
    match = re.search(r"Q(\d+)", quarter, re.IGNORECASE)
    return int(match.group(1)) if match else 0


def _transcript_sort_key(data: dict) -> tuple[int, int]:
    """Sort key from transcript JSON: (fiscal_year, quarter_number)."""
    fiscal_year = int(data.get("fiscal_year", 0))
    quarter_number = _quarter_number(str(data.get("quarter", "")))
    return (fiscal_year, quarter_number)


def _transcript_is_excluded(
    data: dict,
    exclude_quarter: str | None,
    exclude_fiscal_year: int | None,
) -> bool:
    if exclude_quarter is None or exclude_fiscal_year is None:
        return False
    if int(data.get("fiscal_year", 0)) != exclude_fiscal_year:
        return False
    return _quarter_number(str(data.get("quarter", ""))) == _quarter_number(exclude_quarter)


def _transcript_from_json(data: dict) -> QuarterTranscript:
    return QuarterTranscript(
        symbol=data["symbol"],
        quarter=data["quarter"],
        fiscal_year=data["fiscal_year"],
        date=data["date"],
        source=data["source"],
        raw_text=data["raw_text"],
        keywords=[KeywordMetrics(**k) for k in data["keywords"]],
        robotaxi_mentions=data.get("robotaxi_mentions", []),
        fsd_mentions=data.get("fsd_mentions", []),
        optimus_mentions=data.get("optimus_mentions", []),
        margin_mentions=data.get("margin_mentions", []),
        guidance_summary=data.get("guidance_summary", ""),
    )


def load_previous_analysis(
    symbol: str,
    output_dir: Path,
    exclude_quarter: str | None = None,
    exclude_fiscal_year: int | None = None,
) -> QuarterTranscript | None:
    """Load the most recent prior quarter's analysis for QoQ comparison.

    Candidates are ordered by (fiscal_year, quarter_number) parsed from each
    file's JSON, not by filename string order (which mis-orders year boundaries).
    """
    symbol_lower = symbol.lower()
    pattern = f"{symbol_lower}_*_transcript.json"
    candidates: list[tuple[tuple[int, int], dict]] = []

    for path in output_dir.glob(pattern):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError):
            continue
        if _transcript_is_excluded(data, exclude_quarter, exclude_fiscal_year):
            continue
        candidates.append((_transcript_sort_key(data), data))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0])
    _, latest_data = candidates[-1]
    return _transcript_from_json(latest_data)


@dataclass
class QoQDiff:
    """Quarter-over-quarter comparison result."""
    keyword_changes: dict[str, dict]  # keyword -> {prev_count, curr_count, change_pct}
    new_keywords: list[str]
    dropped_keywords: list[str]
    robotaxi_sentiment_shift: str  # "more_specific", "less_specific", "similar"
    fsd_sentiment_shift: str
    optimus_sentiment_shift: str
    key_quotes_comparison: list[dict]  # side-by-side notable quotes


def compare_qoq(current: QuarterTranscript, previous: QuarterTranscript | None) -> QoQDiff:
    """Compare current vs previous quarter."""
    if previous is None:
        return QoQDiff(
            keyword_changes={},
            new_keywords=[k.keyword for k in current.keywords],
            dropped_keywords=[],
            robotaxi_sentiment_shift="first_analysis",
            fsd_sentiment_shift="first_analysis",
            optimus_sentiment_shift="first_analysis",
            key_quotes_comparison=[]
        )
    
    # Build keyword count maps
    prev_counts = {k.keyword: k.count for k in previous.keywords}
    curr_counts = {k.keyword: k.count for k in current.keywords}
    
    all_keywords = set(prev_counts.keys()) | set(curr_counts.keys())
    
    changes = {}
    new_kws = []
    dropped_kws = []
    
    for kw in all_keywords:
        prev_c = prev_counts.get(kw, 0)
        curr_c = curr_counts.get(kw, 0)
        
        if prev_c == 0 and curr_c > 0:
            new_kws.append(kw)
        elif prev_c > 0 and curr_c == 0:
            dropped_kws.append(kw)
        elif prev_c > 0:
            change_pct = ((curr_c - prev_c) / prev_c) * 100
            changes[kw] = {
                "prev_count": prev_c,
                "curr_count": curr_c,
                "change_pct": round(change_pct, 1)
            }
    
    # Simple sentiment comparison
    def compare_sentiment(current_sents: list[str], prev_sents: list[str]) -> str:
        if not current_sents and not prev_sents:
            return "no_mentions"
        if not prev_sents and current_sents:
            return "new_mentions"
        curr_pos = sum(1 for s in current_sents if simple_sentiment(s) == "positive")
        prev_pos = sum(1 for s in prev_sents if simple_sentiment(s) == "positive")
        if curr_pos > prev_pos:
            return "more_positive"
        elif curr_pos < prev_pos:
            return "less_positive"
        return "similar"
    
    # Extract key quotes for comparison
    comparison = []
    if current.robotaxi_mentions:
        comparison.append({
            "topic": "robotaxi",
            "current": current.robotaxi_mentions[0][:200],
            "previous": previous.robotaxi_mentions[0][:200] if previous.robotaxi_mentions else "(none)"
        })
    
    return QoQDiff(
        keyword_changes=changes,
        new_keywords=new_kws,
        dropped_keywords=dropped_kws,
        robotaxi_sentiment_shift=compare_sentiment(current.robotaxi_mentions, previous.robotaxi_mentions),
        fsd_sentiment_shift=compare_sentiment(current.fsd_mentions, previous.fsd_mentions),
        optimus_sentiment_shift=compare_sentiment(current.optimus_mentions, previous.optimus_mentions),
        key_quotes_comparison=comparison
    )


def save_transcript_analysis(transcript: QuarterTranscript, output_dir: Path) -> Path:
    """Save transcript analysis as JSON."""
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{transcript.symbol.lower()}_{transcript.quarter.replace(' ', '').lower()}_transcript.json"
    path = output_dir / filename
    
    data = asdict(transcript)
    # Convert dataclass list to dict
    data["keywords"] = [asdict(k) for k in transcript.keywords]
    
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def format_transcript_summary(transcript: QuarterTranscript, diff: QoQDiff | None = None) -> str:
    """Format transcript analysis as markdown."""
    lines = [
        f"## Earnings Call Analysis: {transcript.symbol} {transcript.quarter} FY{transcript.fiscal_year}",
        "",
        f"**Source:** {transcript.source} | **Analyzed:** {transcript.date}",
        "",
    ]
    
    # Layer-specific keyword counts
    l2_count = sum(k.count for k in transcript.keywords if any(x in k.keyword for x in ["fsd", "neural", "training", "hw"]))
    l3_count = sum(k.count for k in transcript.keywords if any(x in k.keyword for x in ["robotaxi", "cybercab", "ride", "fleet"]))
    l4_count = sum(k.count for k in transcript.keywords if any(x in k.keyword for x in ["optimus", "humanoid"]))
    
    lines.extend([
        "### Layer Keyword Intensity",
        "",
        f"| Layer | Mentions |",
        f"|-------|----------|",
        f"| L2 FSD/AI | {l2_count} |",
        f"| L3 Robotaxi | {l3_count} |",
        f"| L4 Optimus | {l4_count} |",
        "",
    ])
    
    # Key mentions
    lines.extend([
        "### Notable Mentions",
        "",
    ])
    
    if transcript.robotaxi_mentions:
        lines.extend([
            "**Robotaxi (top mention):**",
            f"> {transcript.robotaxi_mentions[0][:250]}",
            "",
        ])
    
    if transcript.fsd_mentions:
        lines.extend([
            "**FSD (top mention):**",
            f"> {transcript.fsd_mentions[0][:250]}",
            "",
        ])
    
    if transcript.optimus_mentions:
        lines.extend([
            "**Optimus (top mention):**",
            f"> {transcript.optimus_mentions[0][:250]}",
            "",
        ])
    
    # QoQ Diff section
    if diff:
        lines.extend([
            "### QoQ Comparison",
            "",
        ])
        
        if diff.new_keywords:
            lines.extend([
                "**New keywords this quarter:** " + ", ".join(diff.new_keywords[:8]),
                "",
            ])
        
        if diff.keyword_changes:
            significant_changes = {
                k: v for k, v in diff.keyword_changes.items() 
                if abs(v["change_pct"]) > 50
            }
            if significant_changes:
                lines.extend([
                    "**Significant keyword changes (>50%):**",
                    "",
                    "| Keyword | Prev | Curr | Change |",
                    "|---------|------|------|--------|",
                ])
                for kw, vals in list(significant_changes.items())[:10]:
                    change_str = f"+{vals['change_pct']:.0f}%" if vals['change_pct'] > 0 else f"{vals['change_pct']:.0f}%"
                    lines.append(f"| {kw} | {vals['prev_count']} | {vals['curr_count']} | {change_str} |")
                lines.append("")
        
        lines.extend([
            f"**Sentiment shift — Robotaxi:** {diff.robotaxi_sentiment_shift}",
            f"**Sentiment shift — FSD:** {diff.fsd_sentiment_shift}",
            f"**Sentiment shift — Optimus:** {diff.optimus_sentiment_shift}",
            "",
        ])
    
    return "\n".join(lines)


def load_transcript_text_from_file(path: Path) -> str:
    """Load transcript from text file (manual input)."""
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    # Example usage demonstration
    print("Tesla AI Transcript Analysis Module")
    print("Usage: analyze_transcript(symbol, quarter, fiscal_year, text)")
