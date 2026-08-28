# Cursor Agent 狀態回覆 — 2026-08-28（Cowork review 跟進）

## ✅ 1. PR #18 — 已 merge

- `python -m pytest tests -q` → **18 passed**（merge 前再跑過）
- **已合併** `main`：`2026-08-28T09:12:52Z`
- 內容：transcript QoQ 排序、explosion／tesla_ai_report Q 前綴、pytest CI、regression tests

---

## ✅ 2. PR #17 — 已修並 merge

Cowork 指出 `framework1.html`／`framework2.html` HUD 下方仍有過時 `.kpis`（US$74.48、Q1 US$200.3M、backlog US$2.2B）。

**修復**（commit `5a92018`）：刪除 `output/RKLB_framework1.html`、`RKLB_framework2.html` 內 legacy `.kpis` 區塊，只保留 Decision HUD；已 republish `docs/rklb/`。

**已合併** `main`：`2026-08-28T09:24:41Z`

---

## 🔶 3. NVDA pipeline — PR #19（draft，待 merge）

**冇** merge 三條舊分支整條（`nvda-remaining-skills-1209` 會刪 AGENTS.md、IREN Pages 等）。改為 cherry-pick **pipeline 資產**：

| 已上 PR #19 | 來源 |
|---|---|
| `config/official_sources_nvda.yaml` | `cursor/nvda-framework3-1209` |
| `config/nvda_cli.yaml` | 同上 |
| `data/source-catalog/nvda-six-quarters.json` | 同上 |
| `data/raw/NVDA/*/manifest.json`（6 份） | bootstrap 自 catalog + SEC/IR URL |
| `scripts/bootstrap_manifests_from_catalog.py` | 新增（可重跑 manifest 骨架） |

**Manifest 說明**：已像 ORCL 一樣 **commit manifest.json**（`git add -f`）；HTML 正文仍 gitignored。每份 manifest 有 `verified` 官方 `source_url`；`validation_status: partial`，`bootstrap: catalog_snapshot`。

**Mac／OneDrive 請跑**（補正文 + sha256）：

```bash
export SEC_USER_AGENT="YourName your@email.com"
python scripts/download_official_research.py \
  --config config/official_sources_nvda.yaml \
  --catalog data/source-catalog/nvda-six-quarters.json \
  --use-existing-catalog --ticker NVDA
```

Cloud 上 SEC 下載 **24/25 失敗**（無 `.env`、rate／網絡），故用 catalog bootstrap 先建立可追蹤 manifest。

PR：https://github.com/keithcheungmk/stock-analysis/pull/19

---

## ⚠️ 4. Mac 本機 `main` 三個未 push commit — **須在 Mac 執行**

Cloud **睇唔到** `45766ba`／`cb6d058`／`36f7d4b`（從未 push）。`origin/main` 現已包含：

- PR #18（= `45766ba` 修復）
- PR #15／#17（IREN／RKLB Pages）

**建議 Mac 終端**：

```bash
git fetch origin
git diff origin/main cb6d058
git diff origin/main 36f7d4b
# 若 diff 為空或只剩已 merge 內容：
git checkout main
git reset --hard origin/main
```

`45766ba` 可丟；`cb6d058`／`36f7d4b` 應為 PR #15 重疊，**唔 push**。

---

## ⚠️ 5. `.git/index.lock` — **須在 Mac 執行**

Cloud workspace 無此檔。請關閉其他 Cursor／Terminal git 操作後：

```bash
rm -f .git/index.lock
```

若仍「Operation not permitted」→ 查 iCloud／OneDrive 是否鎖住 `.git`，或重開 IDE。

---

*此分析僅供研究參考，不構成投資建議。*
