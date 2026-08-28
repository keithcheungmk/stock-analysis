# IREN Adversarial Review Memo

- **覆核時間：** 2026-08-28（Asia/Hong_Kong）
- **報告 as-of：** 2026-08-28；最新官方財報期終 2026-06-30，8-K／10-K 2026-08-27
- **IR／SEC：** `https://www.iren.com/investors/reports`、`iren.gcs-web.com`、SEC submissions CIK 0001878848。新包：8-K `0001878848-26-000051`、10-K `0001878848-26-000052`、IR presentation `1ca5b6f0-4b4d-4710-a7e2-69435e112b60`
- **X：** `x_access=degraded`（無 API；用公開搜尋／新聞轉述）。未用 X 覆寫任何官方數字

## X／公開敘事（≤8，線索 only）

| 標籤 | 內容 |
|---|---|
| confirmed | Horizon 1 交付 Microsoft（8/13 新聞稿 + 8/27 8-K） |
| confirmed | Mirantis 收購完成（8/04 官方） |
| confirmed | Q4 AI US$70.5m、ARR US$4bn／operating US$1bn（8-K） |
| narrative | 電話會議轉述：年底好多產能遲上線，GAAP 收入主要落喺之後嗰季（本地無官方逐字稿） |
| narrative | 第三方標題強調稀釋（founder RSU、發股）— 同官方融資表方向一致 |
| noise | 把 US$4bn ARR 直接當成已入帳收入 |

## Diff vs 8/15 草稿

| 狀態 | 項目 |
|---|---|
| STALE | 「Q4 約 8/28 先出」→ 已出 |
| STALE | 「Horizon 1–4 year-end on track／未交付」→ Horizon 1 **已交付** |
| STALE | contracted ARR US$3.1bn → **US$4bn**；operating ARR **US$1bn**（8/26） |
| STALE | 現金 US$2.21B／有息負債 ~US$3.96B → US$5.90B／US$7.84B |
| STALE | 股數 357.4M（yfinance 仍錯）→ 官方 **394.1M** |
| STALE | Mirantis／Nostrum pending → **已完成** |
| MISSING（已補） | Q4 發股 US$2.11bn、可轉債 US$3.00bn、減值 US$450.4m |
| OK | F1 紅線 1 仍 FAIL；行動仍係續抱唔加倉 |
| LEAD_ONLY | 業績會「收入落後一季」細節 |

## 已 patch

- `output/IREN_2026-08-28_{earnings_review,framework1,framework2,framework3,thesis_tracker,catalyst_calendar}.md`
- `output/IREN_{earnings_review,framework1,framework2,thesis_tracker}.html`
- canvases：earnings、F1、F2、F3、thesis、catalyst

## Verdict impact

**維持行動（續抱、唔好加倉）；微調文字同估值中樞。** 不停 verdict：官方數字內部一致；yfinance 股數／現金同 10-K 衝突時以 10-K 為準。

*此分析僅供研究參考，不構成投資建議。*
