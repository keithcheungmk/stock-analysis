# NVDA Framework 1 初篩報告

- **結果：** PASS
- **總分：** 115 / 130
- **數據截至：** 2026-08-27（Asia/Hong_Kong 覆核）
- **最新官方季度：** FY2027-Q2（期終 2026-07-26，USD，US GAAP，unaudited；SEC 8-K EX-99.1／EX-99.2 + Form 10-Q，accession `0001045810-26-000073`／`0001045810-26-000075`，filing date 2026-08-26，`validation_status: verified`）
- **現價：** US$209.66（yfinance delayed，2026-08-26 收市，America/New_York）；市值約 US$5.08T；攤薄加權約 24,285m 股（官方 Q2）
- **核心結論：** 最大亮點係 Data Center 單季 US$89.0B（+117% YoY）同 TTM 官方自由現金流約 US$126.9B，仍然係 AI 基建嘅定價者；最大風險係客製化 ASIC 增速已經追過／超過 NVIDIA 主線、應收賬款 DSO 由 45 日拉到 60 日，以及 8 月 17 日 Ohio PORTS 剩餘價值擔保上限 US$105B 把公司更深綁入單一客戶／場地。

## 數據驗證

- `data/raw/NVDA/` manifests：6 個通過（FY2026-Q1 至 FY2027-Q2）；`python scripts/validate_raw_manifests.py --root data/raw/NVDA`
- 官方優先：Q2 8-K EX-99.1 業績稿、EX-99.2 CFO commentary、Form 10-Q iXBRL（2026-08-26）
- 季後官方事件：2026-08-17 Form 8-K（items 1.01／2.03／7.01）SB Energy PORTS-Pike 剩餘價值擔保，上限 **US$105B**，OpenAI 為租戶，預計 2028 年起分階段 ready-for-service；另投資 SB Energy US$1.5B。**呢筆擔保唔計入當前有息債務。**
- 同業（最近已公布季，會計期唔完全對齊，必須分開標）：AMD 2026-Q2 8-K EX-99.1（2026-08-04，US GAAP）；Broadcom fiscal Q2 FY2026 8-K EX-99.1（期終 2026-05-03，US GAAP）；TSMC 2026-Q2 6-K EX-99.1（2026-07-16，TIFRS／NT$ 為主，另報 USD）；Intel 2026-Q2 8-K EX-99.1（2026-07-23，US GAAP）
- yfinance 只用於市況、歷史總回報、共識 EPS。**以下 aggregator 數字同官方衝突，一律棄用 aggregator：** TTM 營收 US$253.5B（官方 TTM US$303.0B）、FCF US$46.3B（官方 TTM US$126.9B）、總債務 US$12.8B（官方有息債務 US$33.4B）、trailing P/E 32.6×（官方 TTM 約 26.4×）。

官方 TTM（FY2026-Q3 + FY2026-Q4 + FY2027-Q1 + FY2027-Q2，USD million）：

| 項目 | Q3 FY26 | Q4 FY26 | Q1 FY27 | Q2 FY27 | TTM |
|---|---:|---:|---:|---:|---:|
| 營收 | 57,006 | 68,127 | 81,615 | 96,221 | **302,969** |
| GAAP 淨利 | 31,910 | 42,960 | 58,321 | 59,688 | **192,879** |
| 官方 FCF | 22,089 | 34,902 | 48,554 | 21,341 | **126,886** |
| Data Center | 51,200 | 62,300 | 75,246 | 89,023 | **277,769** |

來源：各季 8-K EX-99.1；Q2 Data Center US$89,023m 來自 EX-99.2。Q3／Q4 Data Center 用業績稿整數十億（US$51.2B／US$62.3B）。

## 致命紅線

### 1. 破產／流動性風險：**安全**

條件：現金低於總債務，**並且**自由現金流為負。

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$22,443m（2026-07-26） | 10-Q／8-K 資產負債表 |
| 可出售債務證券 | US$34,143m | 同上 |
| **官方流動性（現金＋可出售債務證券）** | **US$56,586m** | 10-Q Liquidity and Capital Resources（公司自己嘅定義） |
| 可出售股本證券（**唔計入官方流動性**） | US$42,783m | 資產負債表 |
| 非上市證券 | US$51,157m | 同上 |
| 短期債務 | US$1,000m | 同上 |
| 長期債務 | US$32,366m | 同上 |
| **有息債務合計** | **US$33,366m** | 10-Q Note 9；6 月新發高級無抵押票據面值 US$25.0B |
| Q2 官方 FCF | **US$21,341m** | 8-K EX-99.1 調節表 |
| H1 官方 FCF | **US$69,895m** | 同上 |
| TTM 官方 FCF | **US$126,886m** | 四季 8-K 加總 |

官方流動性 US$56.6B > 債務 US$33.4B（約 1.70×）；FCF 大額為正。即使只用現金等價物 US$22.4B < 債務，紅線要兩項同時成立 → **不觸發。**

其後事項：2026-08-17 剩餘價值擔保上限 US$105B（2028 年起、須滿足 ready-for-service）**唔係當前債務**，唔改紅線 1，但係 Framework 2 必須量化嘅或有支出。

### 2. 衰退陷阱：**安全**

條件：營收增速低於同業平均，**並且**淨利潤率為負或連續兩季下降。

| 公司 | 最近季營收 | YoY | 期終／基準 | 來源 |
|---|---:|---:|---|---|
| NVDA | US$96,221m | **+106%** | 2026-07-26；US GAAP | NVDA 8-K EX-99.1 |
| AMD | US$11,536m | **+50%** | 2026-Q2；US GAAP | AMD 8-K EX-99.1 2026-08-04 |
| AVGO | US$22,187m | **+48%** | FY2026-Q2 期終 2026-05-03；US GAAP | AVGO 8-K EX-99.1 2026-06-03 |
| TSM | US$40.20B / NT$1,270.38B | **+33.7% USD／+36.0% NT$** | 2026-06-30；TIFRS | TSMC 6-K EX-99.1 2026-07-16 |
| INTC | US$16.1B | **+25%** | 2026-Q2；US GAAP | INTC 8-K EX-99.1 2026-07-23 |

同業公司營收增速平均約 **+39.7%**（AMD／AVGO／TSM-USD／INTC）。NVDA 高過同業約 66 個百分點。Q2 GAAP 淨利率 62.0%，Q1 71.5%（含大額股本投資收益）、Q4 FY26 63.1%——利潤率極高且並非「負或連續兩季轉負」。兩項條件都不成立 → **不觸發。**

### 3. 估值泡沫：**未否決**

- 官方 TTM PEG 近似：trailing P/E ≈ 26.4×（US$209.66 / TTM GAAP EPS US$7.94），營收增速 +106% → PEG ≈ 0.25；yfinance PEG 0.59（第三方）同樣 < 1，遠低於 2.5 紅線。
- 官方 TTM P/S ≈ **16.8×**（市值 US$5.08T / TTM 營收 US$303.0B）。yfinance 20.0× 用咗少一季嘅 TTM，棄用。
- 增長支持充分：單季 +106%、Data Center +117%、Q3 指引 US$108.0B ±2%。「缺乏相應高增長」不成立。
- 歷史語境：AI 週期內 NVDA 自身 P/S 曾經更高；而家 17× 配 100%+ 增長唔構成「顯著高於歷史極值且無增長」嘅機械泡沫。

因此紅線 3 **不觸發**。估值仍貴，但規則要 PEG>2.5 或 P/S 極值**加上**無增長。

## 13 維度評分

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 官方流動性 US$56.6B；有息債務 US$33.4B（≈1.70×）。股本證券 US$42.8B 按 10-Q 流動性定義唔計入 | 5 | 現金高於債務但未達 2 倍 | 10-Q 2026-07-26 Liquidity；Note 9 |
| 營收增長 | Q2 +106%；同業公司營收平均約 +40% | 10 | 高於同業超過 10pp（實際約 +66pp） | NVDA／AMD／AVGO／TSM／INTC 官方稿 |
| 淨利潤率 | Q2 GAAP 62.0%；TTM 63.7%。Q2 含股本投資收益 US$7.8B；非 GAAP 淨利 US$54.0B，淨利率仍 56.1% | 10 | 遠高於 25% | 8-K EX-99.1 |
| 估值（PEG） | 官方近似 PEG 0.25；yfinance PEG 0.59。P/S 16.8× 有 +106% 增長支持 | 10 | PEG < 1 | 官方 TTM；市況 yfinance |
| TAM | Data Center TTM 已 US$277.8B；Q3 指引年化約 US$432B。公司自身服務市場已 > US$100B | 10 | 可觸及 > US$100B（用公司已實現營收做下限，唔另估未證實 TAM） | EX-99.1／EX-99.2 |
| 需求 KPI（Data Center） | NVDA DC +117%；AMD DC +107%（US$6.7B）；AVGO AI 半導體 +143%（US$10.8B）；INTC DCAI +59%。AI／DC 同業平均約 +103%，NVDA 高約 14pp | 5 | 高於同業平均超過 10pp，未到 20pp；AVGO AI 增速更快 | 各官方稿；NVDA EX-99.2 |
| ROE | TTM 淨利 US$192.9B / 期末權益 US$229.0B ≈ 84%；平均權益約 100% | 10 | 遠高於 15% | 10-Q；四季 8-K |
| 自由現金流 | TTM US$126.9B；H1 +77% YoY。但 Q2 US$21.3B 對 Q1 US$48.6B 腰斬，主因應收同稅金 | 5 | 為正但有明顯波動，未當「穩定增長」 | 四季 8-K FCF 調節 |
| 護城河 | CUDA／NVLink／Spectrum 生態；Vera Rubin 已量產。反證：AVGO 客製 ASIC +143%、中國 DC compute <1% | 10 | 仍係行業最寬加速運算壁壘，但唔再係無競爭 | EX-99.1；AVGO 8-K |
| 行業趨勢 | AI factory／agentic AI／推理代幣經濟學；公司稱 Vera Rubin 為此時而建 | 10 | 完全符合未來核心趨勢 | EX-99.1 Jensen 評論 |
| 管理層能力 | 連續四季營收／EPS beat、Blackwell Ultra 已佔絕大部分、Rubin 導入 Q3。同時發債 US$25B 做回購、DSO 拉長、中國指引持續為零 | 10 | 行業領先執行，瑕疵記入 adversarial 而非降到「普通」 | EX-99.1／10-Q／yfinance 共識 |
| 相對 S&P 500 | 1999-01-22 IPO 起 NVDA 總回報約 +558,114%；同期 SPY 約 +908%；超額約 +557,206pp | 10 | 遠高於 +20pp | yfinance 調整後收市（含股息近似） |
| 市場預期 vs 實際 | 近四季非 GAAP EPS 全 beat：+3.5%／+5.3%／+5.5%／+6.2%。Q2 營收 US$96.2B 高過自身指引 US$91.0B ±2% | 10 | 連續多季超預期 | yfinance earnings_dates（第三方共識）；指引／實際來自 8-K |

**合計：115／130 → PASS**（門檻：PASS 90–130；WATCH 65–85；FAIL 0–60）

分數結構：10 分 10 項；5 分 3 項（現金／債務、需求 KPI、FCF）；0 分 0 項。

## 季後必須記入嘅官方發展（唔改變 Q2 帳面數字）

1. **2026-08-17 PORTS-Pike／SB Energy（Form 8-K items 1.01／2.03／7.01）：** 俄亥俄 Pike County AI 校園。NVIDIA 為約 4.25 GW IT load 提供剩餘價值擔保，另可選擇再支持約 3.8 GW；初始承諾累計付款上限 **US$105B**，須 Lessor 達 ready-for-service（預期 2028 年起）。OpenAI 為租戶，部署 NVIDIA DSX 全棧。另投資 SB Energy **US$1.5B**。來源：SEC accession `0001045810-26-000069`；NVIDIA Newsroom 2026-08-17。
2. **Vera Rubin：** 官方稱已進入量產，Q3 開始出貨；庫存升至 US$31.6B「為 Rubin 導入做準備」。Q3 毛利率指引 74.0% ±50bps，較 Q2 75.0% 低約 100bps。
3. **中國：** CFO commentary：本季 Hopper 對中國出貨 <1% of Data Center；Q3 指引**不假設任何**中國 Data Center compute 收入。第三方 FT 轉述 H200 對華出口屬 `unverified` 線索，**不可覆寫**官方「指引不含中國 DC compute」。
4. **US$500B 第三方融資平台：** 與 Apollo／BlackRock／Blackstone／Brookfield／Goldman／KKR 等「有待最終協議」。**未交割，唔當已落袋資本。**

## Adversarial check

- **最強支持：** Data Center 單季 US$89.0B、+117% YoY；TTM FCF US$126.9B；連續四季 beat 自身營收指引同共識 EPS；Rubin 已量產且 Q3 指引再加速到 US$108B。
- **最強反證：** Broadcom AI 半導體 +143%，客製 ASIC 正在用更快增速搶訓練／推理增量；DSO 45→60 日、應收 US$63.1B 意味住增長有一部分係延長付款條款「借」回來；6 月發債 US$25.0B 同時單季回購＋股息約 US$26.0B，資本結構由淨現金堡壘改成「邊賺邊槓桿回購」；Ohio 擔保上限 US$105B 把 2028 年後嘅或有負債同 OpenAI 集中度一齊放大。
- **最可能令結論失效嘅假設：** 超大規模客戶把增量 Capex 轉去自研／Broadcom ASIC，同時 Rubin 導入令毛利率跌穿 74% 指引下限，而延長賬期令 FCF 再弱一季，市場把 17× P/S 一次性壓縮。

## 下一步（PASS → Framework 2）

Framework 2 必須深挖嘅兩個問題：

1. **應收同客戶融資：** DSO 由 45 日去到 60 日、應收 US$63.1B，係投資級客戶真實多年期合約，定係變相供應商融資？要按客戶／合約年期拆開，並對 Q3 會唔會再升。
2. **ASIC 替代 × PORTS 擔保：** AVGO AI +143% 對 NVIDIA DC +117% 嘅增量份額；US$105B 剩餘價值擔保同 OpenAI 8 GW 綁定，係護城河定係集中度／或有負債？要情景量化 2028 年起嘅現金峰值。

技術面（CLI，次要權重，yfinance delayed 2026-08-26）：收市 US$209.66，低於 MA20（US$215.56）、高於 MA50／MA200；RSI 46.3 中性；MACD 空頭。1 年回報 +15.6%，明顯落後 AMD／INTC／TSM——符合「四季 beat 仍然 sell-the-news」嘅價格行為，**唔抵消**基本面 PASS。

互動報告：`output/NVDA_framework1.html`  
CLI 報告：`output/NVDA_2026-08-27_report.md`

*此分析僅供研究參考，不構成投資建議。*
