# MRNA Adversarial Review Memo

- 覆核時間：2026-08-26（Asia/Hong_Kong）
- 報告 as-of：Framework 1 初稿同步覆核
- IR／SEC：已掃 CIK 0001682852 submissions（最近 8-K／10-Q／10-K 至 2026-08-12）；Q2 8-K EX-99.1、Q2 10-Q、Q1 8-K、FY2025 10-K、Q3 2025 8-K EX-99.1；公司 IR Insights mFLUSIVA（2026-08-05）；Merck／Moderna 聯合官方稿 INTerpath-001（2026-08-19）；CDC ACIP 會議頁
- X：`x_access=degraded`（無 X API／登入；公開 `site:x.com` 搜尋無可用具名帖）。唔包裝成完整 X 監察。
- Diff：OK / STALE / MISSING / CONFLICT / LEAD_ONLY
- 已 patch：`output/MRNA_2026-08-26_framework1.md`、`output/MRNA_framework1.html`（初稿已納入季後官方事件，無需事後口頭更正）
- Verdict impact：維持 WATCH（75／130）；無停 verdict

## IR／SEC 掃描結果

| 日期 | 事件 | 標籤 | 對報告含義 |
|---|---|---|---|
| 2026-07-31 | Q2 8-K／10-Q：營收 US$145m、淨虧 US$782m、現金＋投資 US$6.9B | OK | 財務主表 |
| 2026-07 月（期後） | 支付訴訟和解 US$950m | OK | 現金下修，紅線 1 仍安全 |
| 2026-08-05 | FDA 批准 mFLUSIVA（50+；65+ 加速批准） | MISSING→已寫入 | 第五產品；覆蓋仍取決 ACIP |
| 2026-08-12 止 | EDGAR 未見 mFLUSIVA／Phase 3 對應 8-K | OK | 用公司／聯合 IR，唔當未發生 |
| 2026-08-19 | INTerpath-001 Phase 3 RFS／DMFS 達標 | MISSING→已寫入 | 平台支柱驗證；效應量未披露 |
| 2026-10-21–23 | 下一次 ACIP 會議（3 月／6 月已取消） | OK | 流感商業關鍵催化 |

## X 摘要（degraded，≤8）

公開搜尋未取得可核對 handle／時間戳嘅原始帖。市場敘事改由具名傳媒轉述（第三方，`LEAD_ONLY`／`narrative`）：

1. Reuters／CNBC／CBS：8/19 股價盤中一度 +145% 至 +177%（`narrative`，以 yfinance OHLC 交叉：高位 US$176.66）
2. 傳媒指 Wall Street 對 mFLUSIVA 2026–27 季銷售預期偏低，主因 ACIP（`narrative`）
3. 對抗詞（dilution／lawsuit／delay）：Q2 已官方確認 US$950m 和解（`confirmed`）；未見新嘅 SEC investigation 官方文件

## Diff vs 初篩草稿

- `OK`：Q2 財務、現金 vs 債務、同業增速、四季 beat
- `MISSING→patched`：mFLUSIVA 批准；INTerpath-001 Phase 3 達標；ACIP 凍結
- `CONFLICT`：yfinance TTM FCF 正值 vs 官方 H1 FCF 大額為負 → **保留官方，棄用 aggregator FCF**；未停 verdict
- `STALE`：無（本包為首次 Framework 1）
- `LEAD_ONLY`：股價單日漲幅傳媒數字；Barclays 黑色素瘤銷售估算未採用

## 對 verdict 嘅影響

維持 **WATCH 75／130**。季後兩件官方好事強化「行業趨勢／護城河／管理層」嘅定性支持，但 Phase 3 未入帳、未披露 HR，唔足以把淨利率、FCF、估值三項 0 分拉上去。股價急升反而令估值維度更透支，所以 **唔升級 PASS**。

*此分析僅供研究參考，不構成投資建議。*
