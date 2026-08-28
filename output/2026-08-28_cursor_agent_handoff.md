# Cursor Cloud Agent 交接筆記 — 2026-08-28

給 Claude Cowork／本機 Mac 用。GitHub 係唯一交接面；請 `git pull` 後讀本檔同對應 PR。

---

## 1. RKLB 對齊 NVDA 8 頁 GitHub Pages

**分支**：`cursor/rklb-nvda-pages-1bc6`  
**PR**：https://github.com/keithcheungmk/stock-analysis/pull/17（draft）  
**Base**：`origin/main`（當時 tip `d16ac67` 附近；與後續 ORCL merge 無衝突設計）

### 做咗咩

- 將 `docs/rklb/` 對齊 NVDA／TSLA **8 頁**互動目錄（hub 卡 8 粒 teal 按鈕）。
- **冇重跑** Framework 1／2／3；用既有 `output/` 底稿合成 HTML，再 `python3 scripts/publish_html_reports.py` 發佈。

### 新增 `output/` → `docs/rklb/`

| 檔 | 內容來源 |
|---|---|
| `RKLB_catalyst_calendar.html` | thesis／one-pager 催化劑（9/24 投票、Q3 業績、Neutron 送墊、ATM／S-4） |
| `RKLB_framework3.html` | `output/RKLB_2026-08-14_framework3.md`（Bear/Base/Bull 28／56／101） |
| `RKLB_valuation.html` | 估值卡（價格尺、可點情景） |
| `RKLB_peer_comparison.html` | RKLB vs RDW／SPCX（參考錨，唔硬比 P/S） |
| `RKLB_one_pager.html` | 四頁翻頁 Update（**US$66.18**，取代過時 8/14 US$80.10 稿） |

### 補 Decision HUD（8 頁同一組數）

- 現價 **US$66.18** delayed（2026-08-26 close）
- Bear／Base／Bull：**28 / 56 / 101**
- 相對 Base **+18%** → 行動：**唔好加倉**
- 驅動 KPI：Q2 營收 US$234.1M；backlog US$2.36B；Q3 GAAP GM 指引 29–31%；H1 OCF −US$134.4M；Neutron Q4 2026 送墊
- 註：ATM／bridge 未入 Skill 3 639.1M 股假設

已 patch HUD 入：`RKLB_framework1.html`、`RKLB_framework2.html`、`RKLB_thesis_tracker.html`（**冇改** WATCH 70/130、Mixed 結論）。

### 刻意冇做

- 唔改 NVDA／TSLA／IREN／ORCL 頁
- 唔改 `CLAUDE.md`
- `RKLB_2026-08-14_one-pager.html` 留底；publish 用 `RKLB_one_pager.html` 覆蓋 `docs/rklb/one-pager.html`

### 合併後 Pages

`https://keithcheungmk.github.io/stock-analysis/rklb/`

---

## 2. Transcript QoQ 排序 + pytest CI

**分支**：`cursor/fix-transcript-qoq-ordering`  
**PR**：https://github.com/keithcheungmk/stock-analysis/pull/18（draft）  
**來源**：port 本機 **未 push** commit `45766ba` 嘅**程式修復**（Cloud 睇唔到該 commit，按用戶描述手動套用）

### 做咗咩

| 檔 | 變更 |
|---|---|
| `src/transcript.py` | `load_previous_analysis()` 按 JSON 內 `(fiscal_year, quarter_number)` 排序，唔再用檔名 string（會把 Q4 2024 排到 Q1 2025 之後）。新增 `exclude_quarter`／`exclude_fiscal_year`。 |
| `src/tesla_ai_report.py` | 呼叫時傳入當季 exclude，避免同季舊檔當「上期」。 |
| `src/explosion.py` | `last_quarter` 已是 `YYYY-MM`，移除錯誤 `Q` 前綴（避免 `Q2026-07`）。 |
| `requirements-dev.txt` | `pytest>=8.0.0` |
| `.github/workflows/tests.yml` | push／PR 跑 `python -m pytest tests -q` |

### 刻意冇帶

- **`45766ba` 入面嘅 `CLAUDE.md`** — `origin/main` 上 PR #5 版本較新，冇動。

### 測試

```bash
python -m pytest tests -q
# 14 passed
```

---

## 3. 本機 Mac 三個未 push commit（用戶指示）

| Commit | 處理 |
|---|---|
| `45766ba` transcript fix | → 已 port 到 PR #18 |
| `cb6d058` merge origin/main（IREN） | **唔 push**；與已 merge PR #15 重疊 |
| `36f7d4b` IREN Q4 Pages | **唔 push**；內容已在 `origin/main`（`87842c2` merge `cursor/iren-q4-pages`） |

建議 Mac：`git fetch origin` 後 `git diff origin/main cb6d058`／`36f7d4b` 確認無獨有改動，再考慮 `git reset --hard origin/main`（先備份其他本機改動）。

`.git/index.lock`：Cloud 無此檔；Mac 上確認無其他 git 進行中再刪。

---

## 4. Cloud vs Mac 數據檔

- Cloud workspace **冇** `data/raw/`（0 檔）；`.gitignore` 設計 raw 留 OneDrive／本機。
- RKLB 8 頁係合成 **GitHub 已有** `output/*.md`／html 底稿，**冇**在 Cloud 重新下載 Q2 earnings／presentation PDF。
- Cowork 核數請用 Mac OneDrive `data/raw/{TICKER}/` 或 GitHub 已引用嘅 SEC／IR 連結。

---

## 5. Cowork 可選下一步

- **RKLB PR #17**：審 8 頁 HUD 數字一致性、催化劑日期、peer 表數字；出 `output/RKLB_*_cowork_review.md` 若需要 patch。
- **Transcript PR #18**：若 Cowork 有本機 `45766ba` 完整 diff，可對照確認 port 無漏。
- 兩 PR 可獨立 merge；無硬性依賴。

---

*此分析僅供研究參考，不構成投資建議。*
