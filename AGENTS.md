# AGENTS.md — Cursor／手機 Cloud Agent

GitHub 係**唯一交接面**。一次任務只跑 **一個 Skill、一隻 ticker**。
Claude Cowork 負責審稿；唔好同 Cowork 平行改同一批未 push 嘅檔。

## 你係邊個

你係執行者：下載官方文件、跑 CLI、按 Skill 寫研究底稿、發佈互動頁、commit、push、開／更新 PR。
用戶可能用電話下指令。**永遠唔好把程式碼、檔案路徑清單當交付。** 完成後用繁體中文總結，**最後一句必須係 GitHub Pages 連結**，結尾免責。

## 開工前

1. `git pull` 最新 `main`（或用戶指定嘅 PR 分支）。若 Cowork 剛留咗 review，先讀最新 commit／PR 留言。
2. 一次一個 Skill。用戶講「全套」而冇指定順序 → 只做 Framework 1，並列出下一步，唔一次寫晒 Skill 0–9。
3. 新 ticker：未有 F1 就唔做 F2／F3／one-pager（除非用戶強制，並標「暫定」）。

## 交貨定義（未達呢三樣＝未完成）

1. 用戶可見 HTML **只喺** `docs/{ticker}/`。寫完 `output/{TICKER}_*.html` 草稿後必須跑  
   `python scripts/publish_html_reports.py`  
   把頁面同步去 `docs/`（含「← 報告目錄」同頁底意見區）。
2. 合併／推去 `main` 之後 GitHub Pages 先會更新。冇 Pages 連結＝未交貨。
3. 用戶總結最後一句用呢個格式：  
   `打開：https://keithcheungmk.github.io/stock-analysis/{ticker}/`  
   唔好貼 code、唔好叫用戶開 IDE。

## GitHub 有 vs Mac 全量副本

用戶 **Mac 永遠保留完整檔案庫**：git clone（報告、config、skills）＋ OneDrive `Stock research/raw`（所有 SEC／IR 原文）＋ 私人經紀檔。Cloud 從 SEC 重建文件只係為咗當次分析，**唔取代** Mac 副本。

| 上 GitHub | 留喺 Mac／OneDrive，唔好 commit |
|---|---|
| `output/*.md`（研究底稿）、`docs/**/*.html`（用戶可見頁） | `data/raw/` 原文 PDF／HTML 正文 |
| `config/`、`data/source-catalog/`、manifests | `.venv/`、`.env`、`output/*.csv|json|png` |
| skills、scripts、src | `~/Documents/stock-analysis-private/`（禁止讀／索引／貼出） |

Cloud 通常冇 OneDrive。用 `scripts/download_official_research.py` 從 SEC／官方 IR 重建，寫 manifest，再分析。持倉六季用 `config/official_sources.yaml`；非持倉另開 `config/official_sources_{ticker}.yaml` + catalog，唔好塞入持倉 10 隻名單。

Mac 收工：`git pull` 攞最新報告；OneDrive 自己 sync raw。唔好刪本機 raw。

## 用戶點評互動頁

用戶只會喺 Pages 頁底撳「寫意見」（GitHub Issue，標題 `[頁面意見]`）。  
指令「處理 XX 頁啲 comment」→ 搜 `gh issue list --search "[頁面意見]"`，**只改對應 `docs/` HTML**，再跑 publish script，回覆已修邊幾條。唔好重跑成套研究，除非意見要求重算數字。

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
| 互動 HTML | `.cursor/skills/interactive-research-report/SKILL.md` | `docs/{ticker}/*.html`（經 publish script） |

TSLA 另讀 `docs/TESLA_AI_FRAMEWORK.md` 同 `config/tesla_*.yaml`。

## 同 Cowork 點接力

1. 你寫檔 → commit → push → 開／更新 PR。PR body 寫清改咗邊啲 `output/` 路徑。
2. 用戶叫 Cowork 審完之後，會有 `output/{TICKER}_{date}_cowork_review.md` 或 PR 評語。
3. 用戶再說「按 Cowork review 改」→ **只 patch 列明嘅檔**，唔重跑成份研究、唔另開平行分支改同一批檔。
4. 未見到 Cowork review 上 GitHub 之前，唔好假設本機 OneDrive 改動存在。

## 電話指令（可原句用）

```
{TICKER} 做 Framework 1，官方優先，繁中，發佈互動頁並開 PR
{TICKER} 做 Framework 2，只深挖 F1 列出嘅兩條問題，發佈互動頁並開 PR
處理 GitHub 上面 [頁面意見] 嘅留言，改對應互動頁，發佈
按 output/{TICKER}_YYYY-MM-DD_cowork_review.md 改檔，唔重跑全套
```
