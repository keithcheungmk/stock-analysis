---
name: analyze-stock
description: >-
  Run technical and fundamental stock analysis using the stock-analysis project.
  Fetches price data via yfinance, computes MA/RSI/MACD, compares peers, and
  writes Markdown reports. Use when the user asks to analyze a stock, ticker,
  股票分析, 技術分析, 基本面, Robotaxi, Optimus, Tesla AI, or mentions TSLA, AAPL.
---

# Stock Analysis

## Tesla AI mode (TSLA)

When analyzing **TSLA**, follow `docs/TESLA_AI_FRAMEWORK.md` in addition to the CLI.

**Locked preferences:** X 輕量 · 爆發定義 C（EPS / 股價分開報）· 同業 A

Read before summarizing:
- `config/tesla_milestones.yaml` — layers, watchlist, catalyst scores
- `config/tesla_peers.yaml` — 5 robotaxi + 5 humanoid peers
- `config/tesla_x_accounts.yaml` — X digest rules (≤5/week)

**TSLA report must include (Traditional Chinese):**
1. **雙軌結論** — `EPS 爆發壓力` | `股價爆發壓力`（分開，唔合併）
2. **四層快照** — L1 汽車能源 / L2 FSD / L3 Robotaxi / L4 Optimus
3. **技術面** — from CLI output (secondary weight)
4. **同業一頁** — robotaxi + humanoid tables from `tesla_peers.yaml`
5. **X 週 digest** — if user pasted links or `x_weekly_digest` populated; else note「待更新」
6. **Transcript diff** — if new earnings; else「待下季財報」
7. **Explosion Watchlist** — next 90 days, 3–5 verifiable events
8. **Catalyst Score** — five dimensions 0–10 from milestones file or reasoned estimate

**Explosion thresholds (definition C):**
- EPS: single-quarter beat vs consensus **> 15%**
- Price: **3-month** return **> +30%**
- Report whether each threshold is currently met; do not claim prediction.

For non-TSLA symbols, use the standard workflow below only.

## Project location

```
/Users/keith/Documents/stock-analysis/
```

## Workflow

Copy and track progress:

```
- [ ] Step 1: Validate and inspect official raw sources
- [ ] Step 2: Run analysis CLI
- [ ] Step 3: Read and reconcile generated outputs
- [ ] Step 4: Summarize in Traditional Chinese
- [ ] Step 5 (optional): Update Canvas dashboard
```

### Step 1: Validate and inspect raw sources

Before quoting financial figures:

```bash
cd /Users/keith/Documents/stock-analysis
source .venv/bin/activate
python scripts/validate_raw_manifests.py --root data/raw
```

1. Search `data/raw/{SYMBOL}/` for the requested fiscal period.
2. Read the nearest `manifest.json` before opening the source document.
3. Prefer `official` sources; treat `third_party` as commentary and `unverified`
   as a lead only.
4. Record period, currency, GAAP/non-GAAP basis and source. If a critical figure
   conflicts with an official filing or fails hash validation, stop and report
   the discrepancy instead of issuing a verdict.

For holdings listed in `config/official_sources.yaml`, also run:

```bash
python scripts/validate_raw_manifests.py \
  --root data/raw \
  --coverage-config config/official_sources.yaml
```

- Use the manifest's `fiscal_period` and `period_end`; do not infer a calendar
  quarter from a fiscal label.
- Prefer entries with `source_tier: official` and
  `validation_status: verified`.
- Check `unavailable_sources` and `pending_sources` before claiming the package
  is complete.
- IREN FY2025 IFRS and FY2026 US GAAP are not directly comparable. Nokia
  reports primarily in IFRS/EUR.

### Step 2: Run analysis

From project root, use the project venv:

```bash
cd /Users/keith/Documents/stock-analysis
source .venv/bin/activate
python src/main.py SYMBOL
```

- `SYMBOL` is uppercase ticker (e.g. `TSLA`, `AAPL`).
- Omit symbol to use `config.yaml` default (`TSLA`).
- Requires network for yfinance.

### Step 3: Read and reconcile outputs

After a successful run, read these files (newest date suffix):

| File | Purpose |
|------|---------|
| `output/{SYMBOL}_{date}_report.md` | Full Markdown report |
| `output/{SYMBOL}_summary.json` | Structured metrics for Canvas |
| `output/{SYMBOL}_chart.png` | Price + MA chart |
| `output/{SYMBOL}_history.csv` | Raw OHLCV cache |

Peers are configured in `config.yaml` under `peers`.

Reconcile yfinance figures against the validated official source. Aggregator
data must never overwrite an official figure; disclose unresolved differences.

### Step 4: Summarize for the user

Respond in **Traditional Chinese** unless asked otherwise. Include:

1. **一句話結論** — trend bias (偏多/偏空/中性) with reason
2. **技術面** — price vs MA20/50/200, RSI, MACD
3. **基本面** — market cap, P/E, margins, growth
4. **同業對比** — how symbol ranks vs peers in `config.yaml`
5. **風險提示** — volatility (beta), valuation, disclaimer

End with: *此分析僅供研究參考，不構成投資建議。*

For every material financial figure, state its fiscal period and source class.
Add a short data-validation status to the conclusion.

### Step 5: Canvas (optional)

When the user wants a visual dashboard:

1. Read `output/{SYMBOL}_summary.json`
2. Create or update a Cursor Canvas for `{symbol}-analysis`
3. Embed all data inline (no `fetch`)
4. Include: weekly price line chart, key stats, peer table

## Config changes

Edit `config.yaml` when the user wants different:

- `history_period`: `6mo`, `1y`, `2y`, `5y`
- `peers`: peer tickers for comparison
- `technical.ma_windows`, `rsi_period`, `macd`

Re-run `python src/main.py` after config changes.

## Troubleshooting

| Error | Fix |
|-------|-----|
| `No module named yfinance` | `pip install -r requirements.txt` in `.venv` |
| `No price history returned` | Check ticker symbol; retry (Yahoo rate limit) |
| Empty `info` | Symbol may be delisted or invalid |

## Example prompts

- 「分析 TSLA」→ run `python src/main.py TSLA`, summarize report
- 「比較 Tesla 同 GM」→ ensure both in peers, run, highlight comparison table
- 「更新 AAPL 儀表板」→ run analysis, refresh canvas from `AAPL_summary.json`
