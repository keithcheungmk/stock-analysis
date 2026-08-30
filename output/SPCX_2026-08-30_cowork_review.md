# SPCX Cowork 執行筆記（重做，格式對齊 HIMS／NVDA 9 頁標準）

- **對住：** `output/SPCX_2026-08-21_*.md`（原有 Framework 1–7＋sector_overview／adversarial_review／report，非本輪重做範圍）
- **背景：** 用戶要求將 SPCX 重做成同 HIMS／NVDA 一致嘅 9 頁標準格式（Framework 1／2／3、Valuation、Peer Comparison、Catalyst Calendar、Thesis Tracker、One-Pager、Index），另外因為有實際持倉（827 股 + short put 195/170 @ 2026-09-18 到期）保留獨立 Options Overlay 頁面。已用 AskUserQuestion 確認：(1) 沿用已驗證 Q2 數字，只 refresh 現價/日期 + 查新聞；(2) Options 頁保留做額外頁面。

## 已完成

- `output/SPCX_2026-08-30_framework1.md` + `docs/spcx/framework1.html`（refresh 現價 US$135.86→US$141.50；13 維度／紅線判斷不變；WATCH 75/130）
- `output/SPCX_2026-08-30_framework2.md` + `docs/spcx/framework2.html`（重新排版，核心 KPI 數字不變）
- `output/SPCX_2026-08-30_framework3.md` + `docs/spcx/framework3.html` + `docs/spcx/valuation.html`（互動 SOTP／情景計算機，取代舊 `valuation-model.html`）
- `output/SPCX_2026-08-30_peer_comparison.md` + `docs/spcx/peer-comparison.html`（新增：RKLB／RDW 現價 refresh，發現兩者過去 1–2 週跌近 20%，SPCX 逆市升 4.2%）
- `output/SPCX_2026-08-30_catalyst_calendar.md` + `docs/spcx/catalyst-calendar.html`（新增：詳細鎖定期解禁時間表，由 P3 雜訊升級做 P1 具體事件）
- `output/SPCX_2026-08-30_thesis_tracker.md` + `docs/spcx/thesis-tracker.html`
- `output/SPCX_2026-08-30_one_pager.md` + `docs/spcx/one-pager.html`（取代舊 `interactive-brief.html`）
- `output/SPCX_2026-08-30_options_overlay.md` + `docs/spcx/options-overlay.html`（額外頁，跟用戶要求保留；更新到期倒數 19 日，assignment 風險升級為「近乎確定嘅基準情景」）

## 舊文件處理

- `output/SPCX_earnings_review.html`、`output/SPCX_interactive_brief.html`、`output/SPCX_valuation_model.html` 三個未帶日期嘅 HTML 來源已移除（`git rm`），因為佢哋分別被 one-pager／valuation／catalyst-calendar 等新頁面取代，避免 `docs/spcx/` 同時存在新舊兩套命名令人混淆。
- `output/SPCX_2026-08-16_*.md`、`output/SPCX_2026-08-21_*.md`（包括 sector_overview／adversarial_review／report／earnings_review／skill7_options 等舊 skill）**全部保留唔刪**，作為歷史存檔。
- `docs/spcx/index.html` 由 `publish_html_reports.py` 自動重新生成，會反映新嘅 9＋1 頁連結。

## 本輪 refresh 方法論

- 財務數字（Q2 2026）沿用 2026-08-21 已驗證版本，冇重新逐項 WebFetch SEC EDGAR（因為官方最新季度冇變）。
- 現價：SPCX／RKLB／RDW 三者均用 WebFetch 重新查核（2026-08-28 收市價），SPCX 由 US$135.86→US$141.50（+4.2%），RKLB US$80.10→US$64.39（-19.6%），RDW US$13.58→US$10.87（-19.9%）。
- 新聞面：WebSearch 查核 2026-08-21 之後有冇重大 8-K／新聞，未發現足以改變 F1 判斷嘅事項。
- **本輪最重要嘅新發現：** 具體、有日期有股數嘅 IPO 鎖定期分階段解禁時間表（2026-09-09 至 2027-06-12，多個波次），呢個之前喺舊版 Catalyst Calendar 只被歸類做「P3 未證實雜訊」，本輪查證後屬於已經公開、確定會發生嘅事件，已升級寫入 Catalyst Calendar、Thesis Tracker、Framework 3 同 Options Overlay 多個頁面，並標明 2026-09-09 解禁同 2026-09-18 put 到期兩件事相距僅 9 日，值得同時監察。

## 限制

- RKLB／RDW 嘅基本面數字（F1／F3）本身冇重新覆核，只 refresh 咗現價——如果想連基本面都重新驗證，需要另外再做。
- 鎖定期解禁時間表嘅股數上限來自第三方彙整文章（`purepowerpicks.com`），並非直接讀取 SEC S-1／424B4 原文條款，建議如果要用嚟做精確倉位決策，應該再對住招股書條款覆核一次確實嘅百分比同觸發條件。
- Sector overview／adversarial review／原有 report 呢三個舊 skill 冇喺本輪重做，維持 2026-08-16／08-21 原狀，未反映鎖定期解禁呢個新發現。

*此分析僅供研究參考，不構成投資建議。*
