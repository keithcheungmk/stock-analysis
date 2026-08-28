# AMD Framework 1 初篩報告

- **結果：** **PASS**
- **總分：** **95 / 130**
- **數據截至：** 2026-08-27
- **最新官方季度：** 2026-Q2（期終 2026-06-27，USD，US GAAP／Non-GAAP；SEC 8-K EX-99.1＋Form 10-Q，2026-08-04，`validation_status: verified`）
- **現價：** US$480.93（yfinance delayed，2026-08-27 close，America/New_York）；市值約 US$778B（yfinance）
- **持倉：** **未確認**（用戶未提供股數／成本）
- **核心結論：** Data Center 翻倍（US$6.7B，+107% YoY）驗證 AI＋伺服器主線；三條紅線未觸發。但現價對 Skill 3 Base US$390 仍有溢價，且 Q2 FCF margin 回落至 14%（Q1 25%），行動上**僅觀察／唔好加倉**（待確認持倉）。

## 數據驗證

- `validate_raw_manifests.py --root data/raw/AMD`：通過（6 manifests；2025-Q1–2026-Q2 complete）
- `pending_sources: 0`；`unavailable_sources`：官方電話會議逐字稿（`not_part_of_standard_official_package`）
- 電話會議第三方逐字稿：`unverified`，唔覆寫官方數字

## 致命紅線

### 1. 破產／流動性風險：**安全**

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$5,086m（2026-06-27） | 10-Q 資產負債表 |
| 短期投資 | US$8,025m | 同上 |
| 流動資產合計 | US$31,522m | 同上 |
| 總債務 | US$3,226m | 10-Q 債務附註 |
| Q2 自由現金流 | US$1,558m | 8-K EX-99.1 Non-GAAP |
| Q2 FCF margin | 14% | 同上 |

現金遠高於債務，FCF 為正 → **紅線 1 未觸發**。

### 2. 衰退陷阱：**安全**

Q2 總營收 US$11.5B，YoY **+50%**（對比 2025-Q2 US$7.7B 級）。淨利潤率 GAAP 約 20%（淨利 US$2.3B）。增速遠高於同業平均 → **紅線 2 未觸發**。

### 3. 估值泡沫：**未否決（觀察）**

- PEG（yfinance）約 **1.03** → 低於 2.5 機械門檻
- Trailing P/E 極高（~121×），但配合 50%+ 營收增速同 Data Center 翻倍
- 現價 US$480.93 對 F3 Base US$390 約 **+23% 溢價** → 列入估值風險，唔構成紅線 FAIL

## 13 維度評分

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金＋短投 ~US$13.1B；債務 US$3.2B | 10 | 現金遠超債務 2 倍 | 10-Q 2026-06-27 |
| 營收增長 | Q2 YoY +50%；DC +107% | 10 | 明顯高於半導體同業平均 | 8-K EX-99.1 |
| 淨利潤率 | GAAP ~20%；Non-GAAP 更高 | 10 | 雙位數盈利 | 8-K |
| 估值（PEG） | PEG ~1.03；P/E trailing 高 | 5 | PEG 合理但絕對倍數貴 | yfinance；官方增速 |
| TAM | AI 加速器＋伺服器 CPU | 10 | 可觸及 > US$100B | Skill 0 |
| 需求 KPI | DC US$6.7B +107%；EPYC＋Instinct 強需求 | 10 | 遠高於同業 CPU 增速 | 8-K |
| ROE | 盈利且 ROE 雙位數（TTM） | 10 | 高於 8% | 10-Q |
| 自由現金流 | Q2 FCF US$1.56B；margin 14%（Q1 25%） | 5 | 正但 margin 回落 | 8-K |
| 護城河 | x86 伺服器＋Instinct；仍追 NVDA CUDA | 5 | 有壁壘但 AI 軟件次於 NVDA | 官方＋同業 |
| 行業趨勢 | AI 基建、資料中心 capex | 10 | 符合主題 | Skill 0 |
| 管理層能力 | Lisa Su 執行紀錄；Helios 路線清晰 | 10 | 多年份額提升 | IR／8-K |
| 相對 S&P 500 | 1Y return ~+183%（yfinance） | 10 | 大幅跑贏大盤 | yfinance delayed |
| 預期 vs 實際 | Q2 beat 指引；Q3 guide ~US$13B | 5 | 連續 beat 但估值已 price in 部分 | 8-K |

**合計：95／130 → PASS**

## Adversarial check

- **最強支持：** Data Center US$6.7B（+107%）；總營收 US$11.5B；Q3 指引 US$13B ±0.3B（+41% YoY）
- **最強反證：** 現價高於 F3 Base ~23%；Q2 FCF margin 13.5–14% vs Q1 25%；Helios Q2 幾乎未入帳
- **最可能令結論失效嘅假設：** Instinct 出貨不及 NVDA 節奏、Helios 延遲、毛利率被競爭壓縮

## 下一步

- PASS 維持條件：（1）Q3 營收接近 US$13B 指引；（2）Helios 開始可驗證出貨；（3）FCF margin 唔持續下滑
- Framework 2 必挖：（1）Helios／Instinct 收入確認節奏 vs 敘事；（2）FCF margin 回落係一次性還是結構性

*此分析僅供研究參考，不構成投資建議。*
