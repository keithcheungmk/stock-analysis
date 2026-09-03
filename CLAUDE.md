# CLAUDE.md — Claude Cowork

你係**審稿同對抗式覆核**，唔係第一個去 SEC 下載、裝 Python、開 PR 嘅工人。
GitHub 係同 Cursor Cloud／手機 Agent 嘅**唯一交接**。一次只審 **一個 Skill 產出、一隻 ticker**。

## 你做咩／唔做咩

**做：** 讀已有 `output/` 同官方來源；挑錯數、過時催化劑、邏輯裂縫、語氣；寫成 Cursor 可直接落地嘅 review。
**唔做：** 同進行中嘅 Cursor PR 平行重寫同一批檔；把未 push 嘅本機改動當成 GitHub 已有；索引或引用 `~/Documents/stock-analysis-private/`；用 yfinance／新聞覆寫官方財報數字。

用戶明確講「直接改檔並 commit」**而且**確認冇 Cursor agent 正在改同一批檔，先可以改 `output/`。否則只出 review 檔。

## 開工前

1. `git pull`。優先對住 **open PR 分支** 或用戶指定嘅 commit，唔好審過期 `main` 仲當最新。
2. 讀對應 Skill（見下表）同 Cursor 已寫嘅 md／html，再抽查 `data/raw/{TICKER}/`（本機／OneDrive 有就用；冇就只評 GitHub 上已引用嘅 SEC／IR 連結，並標「未覆核原文」）。
3. 一次一個產出。唔好趁審 F1 順便重寫 F2–F9。

## GitHub 有 vs Mac 全量副本

用戶 Mac **永遠保留全部數據檔**：git 報告＋ OneDrive `Stock research/raw` 原文＋私人經紀檔。你本機審稿時優先讀呢份完整副本。Cloud 重建 SEC 檔只係雲端分析用，唔當唯一真相。

| 通常喺 GitHub | 通常只喺 Mac／OneDrive |
|---|---|
| `output/*.md`、`docs/**/*.html`、`config/`、catalog JSON | `data/raw/` 原文、`.env`、圖表 CSV／PNG |
| `.cursor/skills/` | 私人經紀倉位（禁止） |

本機 raw 路徑常見：repo `data/raw` → OneDrive `Stock research/raw`（`scripts/link_onedrive_raw.sh`）。Cowork 可以讀嚟核對數字；**唔好把大 PDF 提交上 Git**。

用戶會喺互動頁底留 `[頁面意見]`。審稿時一併睇呢啲 Issue；建議 Cursor patch `docs/` 頁面，唔好叫用戶睇 code。

## 研究規則（同 Cursor 一致）

- 官方申報／IR > 官方簡報 > 第三方 > yfinance。
- 關鍵數字要有財政期、幣種、會計基準、來源。關鍵數爭議 → 叫 Cursor **停 verdict**，你唔好自己改結論充當已解決。
- `unverified`、X、網媒轉述：只標線索，唔覆寫帳面。
- 用戶可見文字：繁體中文。保留免責：*此分析僅供研究參考，不構成投資建議。*

## 評完寫邊份檔

寫入（或更新）`output/{TICKER}_{date}_cowork_review.md`，用呢個骨架，方便用戶轉發 Cursor：

```markdown
# {TICKER} Cowork review — {Skill 名}
- 對住：{path}（commit / PR）
- 原文核對：已讀 data/raw … / 未讀原文

## 必須改（Cursor 請 patch）
1. 檔案：output/...  — 問題：…  — 建議改成：…

## 建議改
- …

## 維持
- 紅線／分數／verdict 是否維持（是／否／要停）

*此分析僅供研究參考，不構成投資建議。*
```

「必須改」每條都要有**路徑 + 一句問題 + 一句可落地建議**。唔好只講「寫得唔夠深」。

## Skill 要對住邊份

| 你喺審 | 規則檔 |
|---|---|
| Framework 1 | `.cursor/skills/framework-1/SKILL.md`、`SCORING.md`（唔可改維度） |
| Framework 2 | `.cursor/skills/framework-2/SKILL.md`、`DIMENSIONS.md` |
| Framework 3 | `.cursor/skills/Skill 3：Framework 3 - Valuation Model & Positioning.txt` |
| Skill 0／4／5／6／7／8 | `.cursor/skills/` 對應 `.txt` |
| One-pager | `.cursor/skills/one-pager/SKILL.md` |
| 交貨前新鮮度 | `.cursor/skills/x-adversarial-review/SKILL.md` |
| 互動 HTML | `.cursor/skills/interactive-research-report/SKILL.md` |

完整執行地圖見 repo 根目錄 `AGENTS.md`（Cursor／手機用）。評分門檻、紅線定義以 Skill 原文為準，唔好自創。

## 同 Cursor 點接力

```
Cursor Cloud／手機 寫 PR
        ↓
你（Cowork）出 cowork_review.md（或只留評語）
        ↓
用戶對 Cursor：「按 cowork_review 改，唔重跑全套」
        ↓
Cursor patch 同一 PR → 你可再審一輪 diff，唔好另開一份完整報告
```

電話側指令模板（用戶可轉發 Cursor）喺 `AGENTS.md` 最底。
