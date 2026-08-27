# Stock Analysis Assistant

以 Python、yfinance 與 Cursor Agent Skill 執行股票技術面、基本面及同業比較。TSLA 另設 Tesla AI 分析模式，追蹤 FSD、Robotaxi、Optimus、爆發條件及催化劑。

## 安裝

```bash
cd /Users/keith/Documents/stock-analysis
python3 -m pip install --user uv
python3 -m uv python install 3.12
python3 -m uv venv .venv --python 3.12
python3 -m uv pip install --python .venv/bin/python -r requirements.txt
source .venv/bin/activate
```

## 執行分析

```bash
source .venv/bin/activate
python src/main.py TSLA
python src/main.py AAPL
```

省略股票代號時，程式會使用 `config.yaml` 的 `default_symbol`。

產出檔案會寫入 `output/`：

- `{SYMBOL}_{date}_report.md`：一般分析報告
- `TSLA_{date}_ai_report.md`：Tesla AI 專用報告
- `{SYMBOL}_summary.json`：結構化摘要
- `{SYMBOL}_chart.png`：價格及移動平均線圖
- `{SYMBOL}_history.csv`：歷史 OHLCV 快取

## 已驗證研究資料庫

`data/raw/` 保存公司 IR、監管文件、簡報、逐字稿及第三方研究。每個文件目錄
都有 `manifest.json`，記錄 SHA-256、來源層級、原始路徑、期別及匯入時間。
分析時應先使用官方且 hash 驗證通過的 raw 文件，再以 yfinance 補充市場數據。

```bash
# 驗證所有 raw 文件與 manifests
python scripts/validate_raw_manifests.py --root data/raw

# 預演另一批研究文件的分類與去重
python scripts/import_research_library.py \
  --source "/path/to/research-copy" \
  --destination data/raw \
  --private-destination "$HOME/Documents/stock-analysis-private/portfolio" \
  --ledger output/migration/research-dry-run
```

目錄、manifest 欄位及安全匯入流程詳見 `data/raw/README.md`。

### 持倉最近六季官方文件

`config/official_sources.yaml` 定義持倉、CIK、官方 IR 入口、財政季度、
會計基準及最近六個已公布季度。首次執行前在本機 `.env` 設定：

```bash
SEC_USER_AGENT=stock-analysis research your-email@example.com
```

建立 SEC accession／附件目錄及下載已驗證文件：

```bash
python scripts/download_official_research.py --catalog-only
python scripts/download_official_research.py --use-existing-catalog
python scripts/validate_raw_manifests.py \
  --root data/raw \
  --coverage-config config/official_sources.yaml
```

可重複使用 `--ticker AMD` 或 `--period 2026-Q2` 縮窄範圍。下載器採
2 requests/s、staging、MIME 檢查及 SHA-256 驗證；官方沒有提供的 slides
或 transcript 會明確記入 manifest，不以第三方文件代替。

經人工核實的動態 IR／CDN 直連位於 `config/ir_supplements.yaml`；下載器
會自動合併到 source catalog。Coverage 報告可用以下命令重建：

```bash
python scripts/report_official_coverage.py
```

## Agent 交接（手機 Cursor × Claude Cowork）

GitHub 係唯一交接。一次一個 Skill、一隻 ticker。

- **Cursor／手機 Cloud Agent** 讀 [`AGENTS.md`](AGENTS.md)：下載官方來源、寫 `output/`、開 PR。
- **Claude Cowork** 讀 [`CLAUDE.md`](CLAUDE.md)：審已有報告，寫 `output/{TICKER}_{date}_cowork_review.md`，唔同 Cursor 平行改同一批未 push 嘅檔。

電話可直接貼：`{TICKER} 做 Framework 1，官方優先，繁中，寫入 output/ 並開 PR`。F1 之後：`{TICKER} 做 Framework 2，只深挖 F1 列出嘅兩條問題`。

## 在 Cursor 使用

專案 Skill 位於 `.cursor/skills/analyze-stock/SKILL.md`，專案規則位於 `.cursor/rules/stock-analysis.mdc`。可在 Cursor Agent 對話輸入：

```text
分析 TSLA，使用 Tesla AI 框架，並用繁體中文總結。
```

或：

```text
比較 AAPL 與 config.yaml 內的同業。
```

Cursor 會執行 CLI、讀取最新輸出，並按 Skill 指示整理報告。TSLA 分析亦會讀取 `docs/TESLA_AI_FRAMEWORK.md` 及 `config/tesla_*.yaml`。

### 建議 chat 結構

- 一個 repo；每隻股票一個長期主 chat，命名 `{TICKER} — 全套分析`
- 同一 ticker 嘅 Framework 1 → 2 → 3、Thesis、財報等沿用同一 chat，但每次只跑一個 Skill
- 新 ticker、跨股票／組合比較、純網站／repo 維修先另開 chat
- Chat 唔係正式記憶庫；以已 commit 嘅 `output/`、source catalog 同 PR 為準
- 一個股票 chat 可以先後用多條短期 branch／PR；唔好將 chat 同永久 branch 綁死
- 一次性 README／repo 導覽或已完成維修 chat 可以封存

詳細 agent 規則見 `AGENTS.md`；Claude Cowork 見 `CLAUDE.md`。

## 設定

編輯 `config.yaml` 可調整：

- 預設股票代號及歷史期間
- 同業代號
- MA、RSI、MACD 參數
- 輸出目錄

Tesla 專用追蹤資料位於：

- `config/tesla_milestones.yaml`
- `config/tesla_peers.yaml`
- `config/tesla_x_accounts.yaml`

## 專案結構

```text
.cursor/          Cursor Skill 與專案規則
config/           Tesla AI 追蹤設定
data/raw/         已驗證原始研究文件及 manifests
docs/             分析框架
schema/           Raw manifest JSON Schema
scripts/          匯入、去重及驗證工具
tests/            下載器及匯入器單元／mock HTTP 測試
src/              資料、指標及報告模組
output/           產出報告與快取
config.yaml       通用分析設定
requirements.txt  Python 套件
```

## 注意

yfinance 資料可能延遲、缺漏或受供應商限制，不適合作即時交易依據。

此專案及其報告僅供研究與教育用途，不構成投資建議。
