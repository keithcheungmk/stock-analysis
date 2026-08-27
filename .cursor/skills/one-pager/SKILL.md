---
name: one-pager
description: >-
  Produce a one-stock buy-side one-pager as a Canvas PPT slide deck: thesis,
  latest-quarter KPIs, Skill 3 valuation summary, and a 1–2 quarter catalyst
  calendar. Defaults to Update mode when a prior one-pager exists; otherwise
  First. Use when the user asks for a one pager, one-pager, 一頁更新, position
  brief, 更新一頁, Skill 9, Canvas, PPT, or投影片.
---

# One-Pager（Canvas PPT）

一次一隻股票。合成已有分析 + 最新官方數據。唔重做 Framework 2。

**估值：** 若未有該 ticker 嘅 Skill 3／Framework 3 報告，**先跑 Skill 3**（`.cursor/skills/Skill 3：Framework 3 - Valuation Model & Positioning.txt`），再把結論摘要進 one-pager。禁止喺 one-pager 即場另起 compact 倍數模型充當估值。有 Skill 3 就只引用其 Base／Bull／Bear、現價隱含、建倉區間。

**Decision HUD：** GitHub Pages／Interactive Brief HTML 跟 `.cursor/skills/interactive-research-report/DECISION_HUD.md`。合成 F3 嘅現價 vs Base 溢價／折讓 + 3–5 個估值驅動 KPI；**唔另估倍數**。行動第一句引用相對 Base 嘅 %。Canvas 第 3 頁估值尺必須同 HUD 數字一致。Interactive Brief（`output/{TICKER}_interactive_brief.html`）係本 skill + interactive-research-report 嘅合成頁，唔係獨立研究 Skill。

**主交付係 Canvas 投影片**（翻頁 PPT，唔係一頁死板表格，亦唔係 HTML）。Chat 只留一句結論、Canvas 連結、免責。

## When to use

- `one pager` / `one-pager` / `一頁更新` / `position brief` / `更新 {TICKER} 一頁` / Skill 9
- `canvas` / `PPT` / `投影片`
- `stock-analyst` 流程第 6 步（底層分析完成後）

唔用嚟做：F1 計分、完整 thesis tracker、earnings memo、10 隻一次過。

## Mode

預設 **Update**。搵上一份 `{TICKER}-one-pager.canvas.tsx`；搵到就只強調 What changed。搵唔到就 **First**（「而家最重要嘅 5 個事實」取代 What changed）。

底層未做過 F1／thesis：仍可出頁，但標「暫定」；缺關鍵官方數字就停 verdict。

## Data

1. 讀 `data/raw/{TICKER}/` 最新季度 manifests；持倉股票跑  
   `python scripts/validate_raw_manifests.py --root data/raw --coverage-config config/official_sources.yaml`
2. 官方 IR／SEC > presentation > 第三方 > yfinance
3. `source_tier: unverified` 只可當電話會議／研究線索，唔可覆寫官方業績
4. 標明財政期間、幣種、會計基礎、來源、validation status
5. `pending_sources` 必須喺頁尾寫出，唔好當齊
6. 現價標 delayed／previous close；唔好當 live
7. 持倉只可用用戶今次確認或最新 dated IB statement

必讀 `~/.cursor/skills-cursor/canvas/SKILL.md`（禁止 gradient／emoji／shadow／彩虹色）。

## Action badge

冇持倉確認，只准：`僅觀察`、`續抱`、`唔好加倉`。  
確認倉位之後先可以加：`加倉`、`減倉`。

## Canvas PPT（主件）

**Path：** `/Users/keith/.cursor/projects/Users-keith-Documents-stock-analysis/canvases/{TICKER}-one-pager.canvas.tsx`  
參考：`RKLB-one-pager.canvas.tsx`

4 頁投影片，頂部 pills + 上一頁／下一頁翻頁（`useCanvasState` 記頁碼）。唔用 tabs 藏內容、唔用全頁 Table 做主視覺。

1. **結論** — 左狀態盒（WATCH／PASS／FAIL）+ Decision HUD（現價 vs Bear／Base／Bull + 驅動 KPI）+ 行動（HUD 之後）+ thesis 3–4 段
2. **事實** — KPI 頂條 + 5 張左邊框事實卡
3. **估值** — Skill 3 四個數字 + 價格位置尺 + 可點 Bear／Base／Bull 卡
4. **催化劑** — 1–2 季時間線卡 + 失效兩卡

## Chat output

1. 一句結論
2. Canvas 連結
3. `*此分析僅供研究參考，不構成投資建議。*`

## Do not

- 一次做多過一隻股票
- 重跑 Framework 2
- 喺 one-pager 即場估倍數充當 Skill 3
- 用第三方 transcript 覆寫官方數字
- 用沉悶全頁表格當主視覺
- 以 HTML 當主交付
