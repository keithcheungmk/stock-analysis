# IREN Framework 1 初篩報告

- **結果：** FAIL（致命紅線 1 觸發，停止正式 13 維度評分）
- **總分：** 不評分（紅線否決）
- **非正式參考分：** 50 / 130（僅供討論，**唔係**正式 PASS／WATCH）
- **數據截至：** 2026-08-28
- **最新官方期間：** FY2026-Q4／FY26（期終 2026-06-30，USD，US GAAP；8-K EX-99.1 unaudited 季度；10-K audited 全年；filing 2026-08-27，`validation_status: verified`）
- **現價：** US$40.53（yfinance delayed，2026-08-28 擷取）；官方普通股 394.1M → 約 US$16.0B 市值（**唔用** yfinance 357.4M 股數）
- **持倉：** 1,080 股 @ ~US$60（浮虧約 32%）
- **核心結論：** 最大亮點係 Q4 AI Cloud US$70.5m 首次超過 Bitcoin，同 Horizon 1 已交付 Microsoft；最大風險係現金 US$5.90B 仍低於有息負債 US$7.84B，而且單季 FCF 約 −US$167m。

## 數據驗證

- `validate_raw_manifests.py --coverage-config config/official_sources.yaml`：通過（147 manifests）
- IREN 滾動六季包而家去到 **FY2026-Q4**（dropped coverage 中嘅 FY2025-Q2，檔案仍留喺 `data/raw`）
- FY2026-Q4：8-K、10-K、IR presentation、IR 業績 PDF 均 `official`／`verified`；`pending_sources: 0`；`unavailable_sources`：官方 transcript 仍非標準包
- Microsoft Horizon 1 交付：官方 8-K EX-99.1（2026-08-27）同 2026-08-13 公司新聞稿
- ARR US$4bn／operating US$1bn：官方 8-K 腳註明確 **非 GAAP**；operating ARR 截至 **2026-08-26**

## 致命紅線

### 1. 破產／流動性風險：**觸發**

條件：現金低於總債務，**並且**自由現金流為負。

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$5,895.6m（2026-06-30） | 8-K EX-99.1 資產負債表 |
| 受限現金（流動＋非流動） | US$1,724.0m（1,670.3+53.7） | 同一張表 |
| 現金＋受限（現金流量表期末） | US$7,619.5m | 同一份 8-K |
| 債務（流動＋非流動） | US$7,593.0m（169.4+7,423.6） | 資產負債表 |
| 融資租賃（流動＋非流動） | US$243.8m（125.3+118.5） | 資產負債表 |
| 有息負債合計 | **US$7,836.8m** | 以上加總 |
| Q4 OCF | US$1,811.1m（其中遞延收入 +US$1,722.2m） | 現金流量表 |
| Q4 PPE | US$1,328.9m | 現金流量表 |
| Q4 硬件 | US$649.3m | 現金流量表 |
| Q4 FCF（OCF−PPE−硬件） | 約 **−US$167m** | 研究計算 |

無受限現金 US$5.90B < 有息負債 US$7.84B；即使把受限現金加埋 US$7.62B **仍然略低於** US$7.84B。FCF 仍負 → **紅線 1 觸發 → FAIL。**

語境（唔改變規則）：流動資產 US$7.89B > 流動負債 US$2.22B；OCF 被客戶預付撐大。Q4 相對 Q3，現金同 FCF **都改善**，但機械條件未解除。稀釋換嚟嘅現金 **唔等於** 紅線過關。

**重新評估條件：** 現金及等價物（研究主口徑：唔計受限）≥ 有息負債，**或** 單季 FCF ≥ 0（同一 US GAAP 加減）。

### 2. 衰退陷阱：**安全**（沿用 miner 轉型組口徑）

Q4 總營收 YoY −26.7%（137.2 vs FY25 Q4 187.3），FY26 全年 +41%（707.0 vs 501.0）。淨利率 Q3、Q4 連續大額虧損。紅線要「增速低於同業 **並且** 淨利率為負／連跌」。對 CLSK／CIFR 呢類 miner 轉型組，上份官方包顯示同業亦在倒退或更弱；**今次未重拉 CLSK／CIFR 官方包**，故不把 CRWV 超高增速拉入呢條機械閘去新觸發。淨利率為負單獨唔夠。→ **不觸發。**

### 3. 估值泡沫：**未否決**

- Forward P/E 為負，PEG **不可用**
- Trailing P/S：市值約 US$16.0B／FY26 營收 US$707.0m ≈ **22.6×**
- 官方 contracted ARR US$4bn → 市值／ARR ≈ **4.0×**（假設 100% 準時計費，過於樂觀）
- Operating ARR US$1bn（8/26）→ 市值／operating ARR ≈ **16×**

有官方大型合約同已開始嘅計費 → **唔構成「無增長硬泡沫」機械觸發。**

## 非正式 13 維度（紅線後僅供討論）

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金 US$5.90B < 有息負債 US$7.84B | 0 | 現金低於債務 | 8-K 2026-08-27 |
| 營收增長 | Q4 YoY −27%；FY26 +41% | 0 | 最新季倒退 | 8-K |
| 淨利潤率 | Q4 −498%；FY26 −99% | 0 | GAAP 虧損 | 8-K |
| 估值（PEG） | PEG 不可用；P/S 22.6× | 0 | trailing 貴 | 股數 10-K；價 yfinance |
| TAM | AI 基礎設施 > US$100B | 10 | 可觸及市場夠大 | Skill 0 |
| 需求 KPI | AI US$70.5m；operating ARR US$1bn | 10 | 遠高過 miner 同業需求 | 8-K |
| ROE | FY26 大額虧損 | 0 | 低於 8% | 8-K |
| 自由現金流 | Q4 約 −US$167m；全年投資現金流 −US$4.72B | 0 | 仍負 | 8-K |
| 護城河 | 已接電＋MSFT 已交付 Horizon 1；客戶仍集中 | 5 | 有壁壘非壟斷 | 8-K |
| 行業趨勢 | AI 算力短缺 | 10 | 核心主線 | 官方業務描述 |
| 管理層 | Horizon 1 準時交付；同時大減值、發股、可轉債 | 5 | 執行有成果，資本紀律有爭議 | 8-K |
| 相對 S&P 500 | 維持上份量級：上市以來累計輕微跑贏 | 5 | 0–20pp | 上份 yfinance；今次未重算 |
| 預期 vs 實際 | AI 達 Preview Bullish；headline 平；大額融資 | 5 | 結構轉型令 beat／miss 難用 | 8-K；yfinance 日曆 |

非正式合計 **50 / 130**（FAIL 區間）。即使豁免紅線，分數都未到 WATCH（65）。

## Adversarial check

- **最強支持：** Q4 AI 收入翻倍並超過 mining；Horizon 1 已交付；contracted ARR 上修到 US$4bn；GPU 融資覆蓋大部分硬件 capex。
- **最強反證：** 現金仍低於有息負債；FCF 仍負；Q4 發股 US$2.11bn＋可轉債 US$3.00bn；減值 US$450.4m；Adj. EBITDA margin 由 41% 跌到 14%。
- **最易令結論失效：** Horizon 2–4 滑出 2026 年曆 Q4，operating ARR 到年底明顯低過 US$4bn，同時再來一輪大型普通股融資。

## 下一步

紅線 FAIL 解除條件不變：現金 ≥ 有息負債，**或** 單季 FCF ≥ 0。

Framework 2 深挖：（1）US$1bn operating ARR 有幾多已經係 GAAP 收入；（2）預收款同發股之後嘅 FCF／稀釋路徑。

互動報告：`output/IREN_framework1.html`

*此分析僅供研究參考，不構成投資建議。*
