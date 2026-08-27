# TSLA Adversarial Review Memo

- 覆核時間：2026-08-27（Asia/Hong_Kong）
- 報告 as-of：Framework 1 初稿同步覆核
- IR／SEC：已掃 CIK 0001318605 submissions（最近 10-Q／8-K 至 2026-07-23）；Q2 8-K EX-99.1、Q2 10-Q、交付 8-K、Q1 10-Q、FY2025 10-K。Tesla IR 首頁 403，改用 EDGAR 原文。
- X：`x_access=degraded`（無 X API／登入；公開搜尋無可用具名原始帖）。唔包裝成完整 X 監察。鎖定偏好：只追 Elon＋Tesla 官方，每週 ≤5 條。
- Diff：OK / STALE / MISSING / CONFLICT / LEAD_ONLY
- 已 patch：`output/TSLA_2026-08-27_framework1.md`、`output/TSLA_framework1.html`（初稿已納入官方七城 Robotaxi、Cybercab 投產、FSD 1.48m；8 月 JPMorgan 參觀列 `LEAD_ONLY`）
- Verdict impact：維持 WATCH（75／130）；無停 verdict

## IR／SEC 掃描結果

| 日期 | 事件 | 標籤 | 對報告含義 |
|---|---|---|---|
| 2026-07-02 | 交付 8-K：480,126 輛、產能 451,758、儲能 13.5 GWh | OK | 需求 KPI |
| 2026-07-22 | Q2 EX-99.1：營收 US$28.24B、FCF −US$1.09B、現金＋投資 US$43.52B、FSD 1.48m | OK | 財務主表 |
| 2026-07-23 | Form 10-Q：iXBRL 同 EX-99.1 一致；capex 2026「超過 US$25B」 | OK | 驗證 |
| 2026-07-23 之後 | submissions 無更新 8-K／10-Q | OK | 無漏官方事件 |
| 2026-07（期後） | 佛州三城 unsupervised Robotaxi；Cybercab 員工試乘 | OK | EX-99.1 已寫，標期後 |
| 2026-08 中旬 | JPMorgan Fremont 參觀紀要（FSD v15、Optimus 2027 H2） | LEAD_ONLY | 第三方，唔覆寫 Outlook |

## X 摘要（degraded，≤5）

公開搜尋未取得可核對 handle／時間戳嘅原始帖。市場敘事改由具名傳媒轉述（第三方，`LEAD_ONLY`／`narrative`）：

1. Tesla@Tesla 2026-07-22 股東信重點（Cybercab 投產、Semi 年內、Optimus 產線）— 官方帖被 Digg 轉載；以 EX-99.1 為準（`confirmed`）
2. Sawyer Merritt 轉發 JPMorgan Fremont note（`narrative`／`LEAD_ONLY`）
3. Electrek／Benzinga 2026-08-20：FSD v15 step-change、刻意放慢 Model Y robotaxi（`narrative`）
4. 對抗詞（delay／capex／margin）：Q2 官方已確認經營利潤 −57%、FCF 轉負、capex +142%（`confirmed`）
5. 未見新嘅 SEC investigation 官方文件

## Diff vs 初篩草稿

- `OK`：Q2 財務、現金 vs 債務、交付、FSD 訂閱、四季 EPS surprise、同業增速
- `CONFLICT`：yfinance `totalDebt` US$16.1B vs 官方有息＋融資租賃 US$9.34B → **保留官方，棄用 aggregator 債務**；yfinance TTM FCF US$4.84B vs 官方 TTM FCF US$5.76B → **保留官方定義**。未停 verdict
- `STALE`：`output/TSLA_2026-08-05_ai_report.md` 仍寫 Q2026-10 EPS `$nan`、現價約 US$327 — **唔採用**；本包取代
- `LEAD_ONLY`：JPMorgan 2027 H2 Optimus 外售；The Verge／tracker 稱 Austin 近兩週 unsupervised（未寫入分數）
- `MISSING`：無（本包為首次 Framework 1）

## 對 verdict 嘅影響

維持 **WATCH 75／130**。季後 JPMorgan 參觀強化 L3／L4 敘事，但不是監管文件，唔足以把淨利率、FCF、估值三項 0 分拉上去。Q2 EPS 大 miss 同 3 個月股價 −21% 令定義 C 兩條爆發軌道都未觸發，所以 **唔升級 PASS**。

*此分析僅供研究參考，不構成投資建議。*
