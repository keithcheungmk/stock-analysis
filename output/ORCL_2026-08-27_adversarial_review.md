# ORCL Adversarial Review Memo

- 覆核時間：2026-08-27（Asia/Hong_Kong）
- 報告 as-of：Framework 1 初稿同步覆核
- IR／SEC：已掃 CIK 0001341439 submissions（最近 10-K 2026-06-22；8-K EX-99.1 2026-06-10；424B5 2026-06-23）。Oracle IR 新聞稿與 EX-99.1 一致。其後至覆核日無新 8-K／10-Q。
- X：`x_access=degraded`（無 X API／登入；公開搜尋無可用具名原始帖）。唔包裝成完整 X 監察。
- Diff：OK / STALE / MISSING / CONFLICT / LEAD_ONLY
- 已 patch：`output/ORCL_2026-08-27_framework1.md`、`output/ORCL_framework1.html`（初稿已納入 ATM 424B5、S&P BBB− 第三方、官方 PEG 口徑）
- Verdict impact：維持 WATCH（85／130）；無停 verdict

## IR／SEC 掃描結果

| 日期 | 事件 | 標籤 | 對報告含義 |
|---|---|---|---|
| 2026-06-10 | 8-K EX-99.1：Q4 營收 US$19.18B（+21%）、IaaS +93%、FY FCF −US$23.69B、RPO US$638B、FY2027 營收 US$90B／EPS US$8.05、再籌約 US$40B | OK | 財務主表 |
| 2026-06-22 | Form 10-K：資產負債、票據 US$129.54B、現金 US$31.29B、RPO 確認節奏 12%／34%、無客戶佔營收 ≥10%、ATM 年結日尚未售股 | OK | 驗證 |
| 2026-06-23 | 424B5：最多 US$20B 普通股 ATM 補充說明書 | OK | 稀釋計劃仍有效；未證明已售 |
| 2026-06-23 之後 | submissions 無新 8-K／10-Q（只有 Form 4／144） | OK | 無漏官方財務事件 |
| 2026-07-09 | S&P 長期評級 BBB−（第三方） | LEAD_ONLY／第三方 | 無 8-K；唔覆寫帳面 |
| 2026-09-10 | FY2027-Q1 財報（yfinance 日曆） | OK | 最近催化；尚未發生 |

## X 摘要（degraded，≤5）

公開搜尋未取得可核對 handle／時間戳嘅原始帖。市場敘事改由具名傳媒／評級轉述（第三方）：

1. Q4 官方 IaaS +93%、RPO US$638B — 以 EX-99.1／10-K 為準（`confirmed`）
2. 財報後延時交易大跌、其後 52 週高位 US$345.72 回落到約 US$149（`confirmed` 市況；非官方財務）
3. S&P 2026-07-09 BBB−；傳媒指約一半 RPO 同 OpenAI 相關（`narrative`／`LEAD_ONLY`）
4. 對抗詞 capex／dilution／junk：官方已確認 FY capex US$55.7B、ATM US$20B、再籌約 US$40B（`confirmed`）；「junk」係評級敘事，尚未發生
5. 數據中心／天然氣管道延期等工地傳聞（`noise`／`LEAD_ONLY`，未寫入分數）

## Diff vs 初篩草稿

- `OK`：Q4／FY 財務、現金 vs 票據、IaaS、RPO、四季 EPS surprise、同業增速
- `CONFLICT`：yfinance `totalDebt` US$167.4B vs 官方票據 US$129.54B → **保留官方，棄用 aggregator 債務**；yfinance PEG 0.82 vs 官方口徑 ≈1.03–1.42 → **棄用 aggregator PEG**。未停 verdict
- `STALE`：無先前 ORCL Framework 1
- `LEAD_ONLY`：S&P OpenAI 佔比、工地／管道延期
- `MISSING`：無（本包為首次 Framework 1）

## 對 verdict 嘅影響

維持 **WATCH 85／130**。季後評級下調強化槓桿反證，但不是監管財務文件，唔足以把紅線改成 FAIL（最近一季推算 FCF 仍為正）。官方 PEG 已由高位壓縮到 1–1.5 帶，所以估值維度 5 分而非 0 分——呢個係 85 而唔係更低嘅原因。差 5 分到 PASS，關鍵閘係 TTM FCF 轉正，**唔升級 PASS**。

*此分析僅供研究參考，不構成投資建議。*
