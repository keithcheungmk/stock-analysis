# ORCL Adversarial Review Memo

- 覆核時間：2026-08-27（Asia/Hong_Kong）
- 報告 as-of：全套 Skill 0→9 交貨閘（含 F1 紅線更正）
- IR／SEC：已掃 CIK 0001341439。最近 10-K 2026-06-22；8-K EX-99.1 2026-06-10；424B5 2026-06-23。其後至覆核日無新 8-K／10-Q。Oracle IR 首頁無獨立 Q1「sets the date」新聞稿。
- X：`x_access=degraded`（無 X API／登入）。唔包裝成完整 X 監察。
- Diff：OK / STALE / MISSING / CONFLICT / LEAD_ONLY
- 已 patch：F1 由 WATCH 85 改為 **FAIL**（單季 FCF 方法更正）；其餘技能全部按 FAIL 約束撰寫
- Verdict impact：**停用 13 維分數**；維持 FAIL，無改回 WATCH

## IR／SEC 掃描結果

| 日期 | 事件 | 標籤 | 對報告含義 |
|---|---|---|---|
| 2026-06-10 | 8-K EX-99.1：IaaS +93%、RPO US$638B、FY FCF −US$23.69B、預付／BYOH US$75B、FY27 US$90B／EPS US$8.05、再籌約 US$40B | OK | 財務主表 |
| 2026-06-22 | 10-K：票據 US$129.54B、現金 US$31.29B、RPO 12%／34%、無客戶佔營收 ≥10% | OK | 驗證 |
| 2026-06-23 | 424B5 ATM 最多 US$20B | OK | 稀釋計劃；未證明已售 |
| 2026-06-23 之後 | 無新 8-K／10-Q | OK | 無漏官方財務事件 |
| 2026-07-09 | S&P BBB− | LEAD_ONLY | 無 8-K |
| 2026-08-26 | Deutsche Bank TMT 會議（第三方 transcript） | LEAD_ONLY | 唔覆寫帳面 |
| 2026-09-10 | FY2027-Q1（yfinance 日曆） | OK／時點 unverified | IR 未見獨立定日稿 |

## 方法 CONFLICT（已修）

- **CONFLICT：** 初稿用 trailing-four-quarter 表 TTM_Q4−TTM_Q3 ≈ +US$1.05B 當「Q4 FCF」。正確口徑係 10-Q／10-K 年累計差額 → Q4 約 **−US$1.87B**。
- **STALE：** 任何仍寫「紅線全過／WATCH 85／Q4 FCF 轉正」嘅句子 → 已改 FAIL。
- **OK：** IaaS、RPO、營收、同業增速、ATM 未售、官方 PEG 棄用 yfinance。
- **LEAD_ONLY：** OpenAI 佔 RPO、FY27 淨 capex US$70B／毛 capex US$90–95B（電話會／傳媒）、工地傳聞。
- **MISSING：** 無（Q1 尚未發生）。

## X 摘要（degraded，≤5）

1. IaaS +93%、RPO US$638B — 官方 `confirmed`
2. 股價自 52 週高 US$345.72 回落至約 US$148 — 市況 `confirmed`
3. S&P BBB−、大客戶集中 — `narrative`／第三方
4. capex／dilution／junk — 官方已確認 capex、ATM、再籌 US$40B（`confirmed`）；junk 未發生
5. 數據中心工期傳聞 — `noise`／LEAD_ONLY

## 對 verdict 嘅影響

**FAIL，停 13 維評分。** 增長叙事仍然硬，但唔可以再靠錯誤嘅單季 FCF 避開紅線 1。其餘技能（F2–F9）全部標明唔翻案、只觀察。

*此分析僅供研究參考，不構成投資建議。*
