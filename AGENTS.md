# AGENTS.md — Cursor／手機 Cloud Agent

GitHub 係**唯一交接面**。一次任務只跑 **一個 Skill、一隻 ticker**。
Claude Cowork 負責審稿；唔好同 Cowork 平行改同一批未 push 嘅檔。

## Chat／研究工作區規則

- **一個 repo；每隻股票一個長期主 chat。** 同一 ticker 嘅 Framework 1 → 2 → 3、同業、催化劑、Thesis、期權、財報同 one-pager，盡量沿用同一個 chat，唔好每個 Skill 開新 chat。
- 「一次一個 Skill」仍然生效：同一主 chat 係延續研究脈絡，**唔代表一次過跑晒全套**。
- 建議 chat 名：`{TICKER} — 全套分析`。例如 `NVDA — 全套分析`、`SPCX — 全套分析`。
- 只有以下工作另開 chat：新 ticker；跨股票／組合比較；純 repo／網站／CI 維修；舊 chat 已過長而要重開。
- 重開同 ticker chat 時，先讀 GitHub 上最新 `output/{TICKER}_*`、source catalog、open PR／最新 commit，再繼續；**唔靠舊 chat 記憶重估數字**。
- 跨股票 chat 唔應該成為任何單一 ticker 嘅主研究紀錄；結果要分別回寫適當 `output/` 或獨立 portfolio／peer report。
- 一個 chat 唔等於一條永久 branch。每個邏輯改動仍用獨立 branch／PR；合併後，下次任務先同步最新 `main`，避免長期 branch 漂移。
- 可封存一次性 repo 導覽、README 摘要、已完成網站修復等 chat；**唔刪研究記憶，因為正式記錄必須落 GitHub**。

## 你係邊個

你係執行者：下載官方文件、跑 CLI、按 Skill 寫 `output/`、commit、push、開／更新 PR。
用戶可能用電話下指令。完成後用繁體中文總結，結尾免責。

## 開工前

1. `git pull` 最新 `main`（或用戶指定嘅 PR 分支）。若 Cowork 剛留咗 review，先讀最新 commit／PR 留言。
2. 一次一個 Skill。用戶講「全套」而冇指定順序 → 只做 Framework 1，並列出下一步，唔一次寫晒 Skill 0–9。
3. 新 ticker：未有 F1 就唔做 F2／F3／one-pager（除非用戶強制，並標「暫定」）。

## GitHub 有 vs 本機先有

| 上 GitHub | 唔好 commit |
|---|---|
| `output/*.md`、`output/*.html` | `data/raw/` 原文（PDF／HTML 正文） |
| `config/`、`data/source-catalog/` | `.venv/`、`.env`、`output/*.csv|json|png` |
| skills、scripts、src | `~/Documents/stock-analysis-private/`（禁止讀／索引／貼出） |

Cloud 環境通常**冇** OneDrive `data/raw`。用 `scripts/download_official_research.py` 或等同方式從 SEC／官方 IR 重建，寫 manifest，再分析。持倉六季用 `config/official_sources.yaml`；非持倉另開 `config/official_sources_{ticker}.yaml` + catalog，唔好塞入持倉 10 隻名單。

## 必守研究規則

- 來源優先：監管／官方 IR > 官方簡報 > 第三方 > yfinance。aggregator **唔可覆寫**官方數字；衝突就表列並棄用 aggregator。
- 關鍵數字標：財政期、幣種、會計基準、來源、`validation_status`。關鍵數爭議 → **停 verdict**。
- `source_tier: unverified` 同 X 帖只當線索。
- 用戶可見總結：繁體中文。報告結尾：*此分析僅供研究參考，不構成投資建議。*

## Skill 地圖（只跑用戶點名嗰個）

| 用戶講 | 讀邊份 | 產出 |
|---|---|---|
| 賽道／Skill 0 | `.cursor/skills/Skill 0_ Sector Overview.txt` | `output/{TICKER_or_SECTOR}_{date}_sector_overview.md` |
| Framework 1／初篩 | `.cursor/skills/framework-1/SKILL.md` + `SCORING.md` | `output/{TICKER}_{date}_framework1.md`（可加 HTML） |
| Framework 2／深度增長 | `.cursor/skills/framework-2/SKILL.md` + `DIMENSIONS.md` | `output/{TICKER}_{date}_framework2.md` |
| Framework 3／估值 | `.cursor/skills/Skill 3：Framework 3 - Valuation Model & Positioning.txt` | `output/{TICKER}_{date}_framework3.md` |
| 同業／Skill 4 | `.cursor/skills/Skill 4：Peer Comparison.txt` | `output/{TICKER}_{date}_peer_comparison.md` |
| 催化劑／Skill 5 | `.cursor/skills/Skill 5：Catalyst Calendar.txt` | `output/{TICKER}_{date}_catalyst_calendar.md` |
| Thesis／Skill 6 | `.cursor/skills/Skill 6：Thesis Tracker.txt` | `output/{TICKER}_{date}_thesis_tracker.md` |
| 期權／Skill 7 | `.cursor/skills/Skill 7：Option Trading Strategy.txt` | `output/{TICKER}_{date}_skill7_*.md` |
| 財報／Skill 8 | `.cursor/skills/Skill 8：Earnings Preview _ Review.txt` | `output/{TICKER}_{date}_earnings_review.md` |
| One-pager／Skill 9 | `.cursor/skills/one-pager/SKILL.md` | Canvas／對應 HTML；缺 F3 先跑 Skill 3 |
| 技術面 CLI | `.cursor/skills/analyze-stock/SKILL.md` | `python src/main.py TICKER`（專用 peers 用 `config/{ticker}_cli.yaml`） |
| Adversarial／X review | `.cursor/skills/x-adversarial-review/SKILL.md` | `output/{TICKER}_{date}_adversarial_review.md`；交貨前修過時催化劑 |
| 互動 HTML | `.cursor/skills/interactive-research-report/SKILL.md` | `output/{TICKER}_*.html` |

TSLA 另讀 `docs/TESLA_AI_FRAMEWORK.md` 同 `config/tesla_*.yaml`。

## 同 Cowork 點接力

1. 你寫檔 → commit → push → 開／更新 PR。PR body 寫清改咗邊啲 `output/` 路徑。
2. 用戶叫 Cowork 審完之後，會有 `output/{TICKER}_{date}_cowork_review.md` 或 PR 評語。
3. 用戶再說「按 Cowork review 改」→ **只 patch 列明嘅檔**，唔重跑成份研究、唔另開平行分支改同一批檔。
4. 未見到 Cowork review 上 GitHub 之前，唔好假設本機 OneDrive 改動存在。

## 電話指令（可原句用）

```
{TICKER} 做 Framework 1，官方優先，繁中，寫入 output/ 並開 PR
{TICKER} 做 Framework 2，只深挖 F1 列出嘅兩條問題，寫入 output/ 並開 PR
審 output/{TICKER}_YYYY-MM-DD_framework1.md，跑 adversarial，只改過時催化劑
按 output/{TICKER}_YYYY-MM-DD_cowork_review.md 改檔，唔重跑全套
```
