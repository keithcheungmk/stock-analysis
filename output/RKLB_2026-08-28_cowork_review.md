# RKLB Cowork review — GitHub Pages 8-page alignment (PR #17)

- 對住：`cursor/rklb-nvda-pages-1bc6`（commit `e915ded`，未 merge，PR #17 draft）
- 原文核對：更正——查核之後發現 `data/raw/RKLB/*/manifest.json` 同 NVDA 一樣，喺成個
  git history 都未 track 過。分別在於 RKLB 嘅原始 raw 文件（2023-Q4 至 2026-Q2，多個
  quarter 資料夾）確實存在你 Mac OneDrive `Stock research/raw/RKLB/`，可以本機獨立
  核對；NVDA 就連 OneDrive 呢份都冇。兩者共通問題係：manifest.json 都冇 commit 落
  git，即係冇一個喺 GitHub 度就睇到嘅、可重現嘅驗證紀錄。報告本身冇重新驗證 raw
  文件，純粹合成已有 `output/` 底稿做 HTML，跟 handoff note 講法一致。

## 必須改（Cursor 請 patch）

1. 檔案：`docs/rklb/framework1.html` — 問題：新增嘅 Decision HUD 寫緊 **現價
   US$66.18（2026-08-26 delayed）、Q2 營收 US$234.1M**，但頁面下面舊嘅
   `.kpis` 條（呢個 PR 冇改過）仍然顯示 **股價（延遲）US$74.48、Q1 2026 營收
   US$200.3M、Backlog US$2.2B**——同一版頁面出現兩個唔同股價、兩個唔同季度營收，
   使用者打開個頁會見到自相矛盾嘅數字。呢個係新 HUD 直接疊喺舊內容上面、冇刪走
   舊 KPI 條所致。— 建議改成：刪走或者更新舊嗰四粒 `.kpis`（股價 74.48 →
   66.18、Q1 200.3M → Q2 234.1M、Backlog 2.2B → 2.36B、P/S 68x 需要重新計），
   或者索性刪走成個舊 `.kpis` block，淨係留新 HUD。
2. 檔案：`docs/rklb/framework2.html` — 問題：同上，舊 `.kpis` 條仍然顯示
   Q1 2026 營收 US$200.3M、Backlog US$2.2B（YoY/QoQ 百分比都跟舊數），新 HUD
   就寫 Q2 US$234.1M／US$2.36B——同一頁兩組矛盾數字。— 建議改成：同 framework1.html
   一樣，刪走或更新舊 `.kpis`。
3. 已核對冇呢個問題嘅頁：`catalyst-calendar.html`、`framework3.html`、
   `index.html`、`one-pager.html`、`peer-comparison.html`、`thesis-tracker.html`、
   `valuation.html`——呢 7 頁全部搜過 "74.48" 同 "200.3M" 都係 0 命中，係乾淨嘅
   全新內容，唔使改。

## 建議改

- 冇。

## 維持

- Decision HUD 本身數字（US$66.18、Bear/Base/Bull 28/56/101、+18% 溢價 → 唔好加倉）
  同 `output/RKLB_2026-08-14_framework3.md` 對得上，冇問題，**維持**。
- Framework 1／Framework 2 底層紅線／分數呢個 PR 冇改動（只加咗 HUD 同 action bar），
  **維持**，唔需要停 verdict——但上面兩點嘅頁面矛盾數字要 patch 咗先可以 merge。

*此分析僅供研究參考，不構成投資建議。*
