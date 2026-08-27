# NVDA Adversarial Review Memo

- **覆核時間：** 2026-08-27 Asia/Hong_Kong（財報出咗約 16 小時）
- **Ticker／IR：** NVIDIA Corporation（NASDAQ: NVDA）；IR 入口 `investor.nvidia.com` 本環境 Cloudflare 403，改用 SEC EDGAR + `nvidianews.nvidia.com`
- **報告 as-of：** FY2027-Q2 期終 2026-07-26；8-K／10-Q filing date 2026-08-26
- **Freshness 窗口：** 自期終日起掃到覆核日，重點最近 14 日

## IR／SEC

掃過：

- SEC submissions CIK `0001045810`（至 2026-08-26 10-Q／earnings 8-K）
- Q2 FY27 8-K `0001045810-26-000073` EX-99.1／EX-99.2；10-Q `0001045810-26-000075`
- 季後 8-K `0001045810-26-000069`（2026-08-17，items 1.01／2.03／7.01）PORTS-Pike／SB Energy
- NVIDIA Newsroom Q2 FY27 業績稿（同 EX-99.1 一致）
- 同業官方：AMD 8-K 2026-08-04、AVGO 8-K 2026-06-03、TSMC 6-K 2026-07-16、INTC 8-K 2026-07-23

有／無新事件：

- **有（已寫入 Framework 1）：** 2026-08-17 剩餘價值擔保上限 US$105B、OpenAI 為租戶、投資 SB Energy US$1.5B；Q2 已公布 Vera Rubin 量產、Groq 3 LPX 量產、Q3 指引 US$108.0B 不含中國 DC compute。
- **無：** 未見財報後另發修正 8-K 或下修指引。

## X

- `x_access: degraded`（公開 `site:x.com` 搜尋無可用結果；無 X API）
- 唔可以宣稱已完整監察 X
- 第三方敘事（HTX／FT 轉述，`unverified`）：「四季 beat 後仍然 sell-the-news」；H200 對華小量出貨。**官方 Q3 指引仍然寫「不假設任何中國 Data Center compute」——以官方為準，H200 傳聞只作線索。**

有用項目（≤8；無一手 X 帖）：

1. NVIDIA Newsroom 2026-08-26 — Q2 US$96.2B、DC US$89.0B、Rubin 量產 — `confirmed`
2. SEC 8-K 2026-08-17 — PORTS 擔保上限 US$105B — `confirmed`
3. HTX 2026-08 前後 — 連續四季公布後股價回吐 — `narrative`（價格行為，唔改財務）
4. FT 轉述 H200 對華 — `LEAD_ONLY`／`unverified`

## Diff

| 項目 | 狀態 | 說明 |
|---|---|---|
| Q2 營收／DC／EPS／FCF | OK | 對住 EX-99.1／EX-99.2／10-Q |
| Q3 指引 US$108B、毛利率 74%、中國 = 0 | OK | 官方 outlook |
| Vera Rubin「即將」 | OK／已更新 | 官方已寫 full production，庫存為 Q3 導入 |
| US$500B 第三方資本 | OK | 報告標「有待最終協議」，未當交割 |
| PORTS／US$105B 擔保 | MISSING→已 patch | 寫入 Framework 1 季後事件同 adversarial |
| yfinance FCF／債務／TTM | CONFLICT→已棄用 aggregator | CLI 報告加咗官方對帳表 |
| H200 中國出貨已入指引 | LEAD_ONLY | 官方明確唔計 |

## 已 patch 嘅檔案

- `output/NVDA_2026-08-27_framework1.md`
- `output/NVDA_framework1.html`
- `output/NVDA_2026-08-27_report.md`（官方對帳）
- `output/NVDA_2026-08-27_framework2.md`
- `output/NVDA_framework2.html`
- 本 memo

## Verdict impact

**維持 PASS 115／130。** 無關鍵數字爭議需要停 verdict。PORTS 擔保改變嘅係 2028 年起或有負債同客戶集中度，唔改當前紅線 1（FCF 為正且官方流動性 > 債務）。

## Framework 2 同日覆核（2026-08-27）

- SEC submissions 至覆核時最新仍係 2026-08-26 10-Q／earnings 8-K；無財報後修正 8-K。
- F2 用 10-Q／CFO 把 PORTS 首期 ready-for-service 寫成 **財政年度 2029**（約 2028 日曆年），九期；毛風險含其他場地擔保共 US$108.5B。F1「2028 年起」同財政日曆大致相容，F2 用更精確嘅 fiscal label。
- 10-Q Note 7：IG 大型 data center 建設付款條款可 90 日至一年；五個直接客戶佔應收 70%。呢兩條喺 F1 未展開，已寫入 F2。
- `x_access: degraded` 維持；無一手 X 帖覆寫官方數字。

F2 判定：增長 thesis **通過**；現金流／應收 **部分通過**。無關鍵數字爭議需停 verdict。

## Remaining skills 覆核（2026-08-27 稍後；Asia/Hong_Kong）

- **IR／SEC：** IR filings 頁最新仍係 2026-08-26 10-Q／earnings 8-K；2026-08-24 係 Form 4（Ajay Puri 退休），唔係新 8-K。無財報後修正稿。
- **官方 Newsroom 補漏（已寫入 Skill 5／6／one-pager，唔改 F3 目標價）：**
  1. 2026-08-26 AWS 額外約 200 萬顆 GPU（2027–2028 部署 Blackwell Ultra／Rubin／Rubin Ultra；另規劃 10 萬顆聯邦安全區）— `confirmed` 新聞稿，**未入帳**。標 MISSING→已 patch 催化劑／thesis；唔當 Q3 P&L。
  2. 2026-08-24 Groq 3 LPX 量產、SpaceXAI 採用 Vera CPU — `confirmed` 產品新聞，近端財務影響低。
- **同業官方（Skill 4）：** AMD 8-K／Newsroom 2026-08-04；AVGO 8-K 2026-06-03（Q3 指引 AI US$16.0B 仍未入帳；IR 排期 2026-09-02 公布）；TSMC 2026-07-16；INTC 2026-07-23。曆法唔對齊。
- **價格：** F3 錨維持 US$209.66（08-26 收市）。yfinance 2026-08-27 delayed 約 US$225.51（IR 頁曾顯示 ~225.47）。估值卡提供切換，**唔重寫 F3 目標價**。
- **X：** `x_access: degraded` 維持；公開 web 無可用一手帖。唔宣稱已完整監察 X。

| 項目 | 狀態 | 說明 |
|---|---|---|
| F3 Bear／Base／Bull | OK | 剩餘技能只引用，無另起 22／26／30 模型 |
| AWS 200 萬顆 | MISSING→已 patch | Skill 5／6／one-pager；近端 P&L 低 |
| Form 4 退休 | LEAD_ONLY／雜訊 | 唔寫進財務 thesis |
| H200 對華 | LEAD_ONLY | 官方 Q3 指引仍寫中國 DC = 0 |
| delayed US$225 vs 錨 209.66 | OK | 展示層標 delayed；行動仍唔追 |

**Verdict impact：維持。** F1 PASS、F2 增長通過／現金部分通過、F3 對 Base 低估（暫定）。無關鍵數字爭議需停 verdict。

已 patch：`output/NVDA_2026-08-27_peer_comparison.md`、`catalyst_calendar.md`、`thesis_tracker.md` 及對應 HTML、估值卡、one-pager、`NVDA_framework3.html`。

*此分析僅供研究參考，不構成投資建議。*
