# HIMS Cowork 執行筆記（本輪由 Cowork 直接執行 Skill 2–9，非審稿）

- **對住：** `output/HIMS_2026-08-28_framework1.md`（Cursor 原有 F1，**FAIL** — 紅線 1／流動性同時觸發兩個條件，13 維度評分已跳過）+ 本輪新增 Framework 2／3、peer comparison、catalyst calendar、thesis tracker、one-pager（markdown + `docs/hims/*.html`）
- **背景：** 跟 MRVL 果次一樣，用戶要求 Cowork 呢個 session 越過平時「審稿角色」做執行者，一次過起晒 HIMS 剩低嘅 7 個 Skill／頁面。

## ⚠️ 最重要嘅一點：F1 = FAIL，本輪所有內容都唔翻案

F1 紅線 1（流動性）同時觸發兩個條件：官方流動性（現金 $609.8m + 短債 AFS $231.2m = $841.0m）對可轉換債面值（$1,365.3m）覆蓋率 0.62×，**同時** Q2 2026 官方 FCF 為負（-$68.2m）。跟規矩，13 維度評分完全跳過，唔畀 PASS／WATCH 分數。

本輪 Framework 2 深挖之後，**判斷未有被推翻，反而獲得進一步確認**：
1. Headline +38% YoY 增長大部分來自 Eucalyptus 併購併表，美國自然增長實際只有 +16%，較 2025 全年 +59% 明顯放緩。
2. 毛利率連跌四季（74%→72%→65%→64%）。
3. Eucalyptus 收購仲有 $683.9m 遞延付款需要喺未來 18 個月分期支付，會持續消耗本已緊張嘅流動性，公司本身都要另開 $400m 應收帳款融資頂住。

Framework 3（估值）、peer comparison、thesis tracker、one-pager 全部跟 `RDW_2026-08-06_framework2.md` 嘅先例處理（F1 FAIL 但用戶要求深挖，可以跑但唔可以翻案）——每一頁嘅 Decision HUD／結論／status badge 都明確標示 FAIL，估值目標價明確標明「僅供參考，唔係持倉建議工具」，**冇任何一頁將呢個折讓包裝成「值得進場」嘅訊號**。

## 已完成

- `output/HIMS_2026-08-28_framework2.md` + `docs/hims/framework2.html`
- `output/HIMS_2026-08-28_framework3.md` + `docs/hims/framework3.html` + `docs/hims/valuation.html`（互動 P/S 情景計算機）
- `output/HIMS_2026-08-28_peer_comparison.md` + `docs/hims/peer-comparison.html`
- `output/HIMS_2026-08-28_catalyst_calendar.md` + `docs/hims/catalyst-calendar.html`
- `output/HIMS_2026-08-28_thesis_tracker.md` + `docs/hims/thesis-tracker.html`
- `output/HIMS_2026-08-28_one_pager.md` + `docs/hims/one-pager.html`（見下方格式偏離）
- 回頭更新咗 `docs/hims/framework1.html` 嘅 Decision HUD，由 `F3 pending` 換成 `F3 已完成 · FAIL 維持`，加入正式 Bear／Base／Bull 區間，同時保留 FAIL 結論不變，符合 `DECISION_HUD.md` 「F3 完成後回頭換走 pending 頁」嘅要求。

## 必須知道嘅偏離／限制（請 Cursor 或用戶覆核）

1. **One-pager 冇做到 Canvas PPT。** 同 MRVL 果次一樣，Cowork 呢個 session 冇 Cursor canvas 工具鏈，改用 markdown＋互動 HTML 代替。
2. **Framework 3 嘅估值情景（Bear/Base/Bull 攤薄股數同 P/S 倍數）係 Cowork 自行推算，唔係官方指引。** 公司只公布咗 FY2026 全年營收指引（$2.7B–$2.9B），冇提供攤薄股數或估值倍數指引。Bear 情景嘅「+10% 攤薄」假設係基於流動性缺口邏輯推斷，唔係任何官方或分析師預測，建議 Cursor／用戶覆核呢個假設是否過於保守或過於樂觀。
3. **同業比較入面嘅 TDOC／LFMD／GDRX 數字全部係本輪新查，冇喺呢個 repo 之前出現過**（同 MRVL 果次可以直接重用 NVDA／AMD 已有 F1／F3 唔同）——已逐一用 WebFetch 對住各自 2026-07 底至 2026-08 初嘅官方業績稿覆核，可信度應該同 HIMS 本身數字一致。
4. **`data/raw/HIMS` manifest 情況未有檢查**——跟 NVDA／MRVL 同一個已知 gap 模式，本輪官方數字全部直接用 WebFetch 對住 SEC EDGAR 原文（CIK 1773751 之 8-K EX-99.1）覆核，唔係倚賴本機 manifest，數字本身可信，但冇本機 SHA-256／manifest 記錄。
5. **`docs/hims/valuation.html` 嘅互動計算機只係簡化模型**（P/S × 自行推算營收 ÷ 攤薄股數，股數用線性假設，冇按情景細拆攤薄嘅具體發行機制），已喺頁腳標明。
6. **HIMS 現價 US$31.66 取自 F1（2026-08-27 收市）。** 本輪搜尋到一個 2026-08-21 嘅 $33.78 報價（更舊），為咗同 F1／全部頁面 Decision HUD 保持一致，本輪全部新頁面統一沿用 F1 嘅 $31.66 基準，冇重新獨立核實最新現價。

## 資料來源方法論

Framework 2 嘅五季 KPI 全部逐季用 WebFetch 直接讀 SEC EDGAR 原文覆核（Q3 2025 至 Q2 2026 共 5 份 8-K EX-99.1，其中 Q4 2025／FY2025 業績稿係本輪新搜尋到，accession `0001773751-26-000019`）。同業比較入面 TDOC／LFMD／GDRX 數字分別對住 Teladoc Health IR（2026-07-29 press release）、LifeMD IR（2026-Q2 業績稿）、GoodRx IR（2026-Q2 業績稿）官方原文覆核。

## 未做

- 冇再重新驗證 F1 本身嘅數字（假設 F1 已經係準確嘅，本輪淨係喺佢基礎上加建）。
- 冇跑 `x-adversarial-review`。
- HIMS Q4/FY2025 8-K 嘅確實 EX-99.1 URL 搵咗幾次先搵到（`hims-20251231x8xkearningsr.htm`），過程中排除咗兩個唔啱嘅 accession（FY2025 10-K 本身、Eucalyptus 收購協議 8-K），呢個搜尋過程本身冇留低正式記錄，建議日後補做 manifest 時一併記低。

*此分析僅供研究參考，不構成投資建議。*
