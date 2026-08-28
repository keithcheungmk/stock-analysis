# MRVL Framework 1 初篩報告

- **結果：** **WATCH**
- **總分：** **65 / 130**
- **數據截至：** 2026-08-28（Asia/Hong_Kong）
- **最新官方季度：** FY2027-Q2（期終 2026-08-01，USD，US GAAP／Non-GAAP，unaudited；SEC 8-K EX-99.1 accession `0001835632-26-000022`，filing date 2026-08-27，`validation_status: verified`）
- **10-Q：** FY2027-Q2 Form 10-Q **未申報**（manifest `pending_sources: regulatory_filing`／`validation_status: partial`）。資產負債同現金流用同期 8-K 簡明表；唔當已審 10-Q。
- **現價：** US$241.45（yfinance delayed，2026-08-28 最近收市，America/New_York）；市值約 US$217.0B
- **持倉：** **未確認**
- **核心結論：** 最大亮點係 Data Center 已入帳 US$2.172B（+46% YoY、佔總營收 79%）同連續六季高過自身指引中位；最大風險係現金 US$3.93B 仍低過有息債務 US$4.96B、增速同需求 KPI 明顯慢過 NVDA／AMD 資料中心線，以及 2026-08-18 向 Google 發行最多約 5,897 萬股認股權證（約現有普通股 6.7%）帶來嘅稀釋。

## 數據驗證

- `python scripts/validate_raw_manifests.py --root data/raw/MRVL`：通過（6 manifests）
- `--coverage-config config/official_sources_mrvl.yaml` **唔跑**：個腳本假設持倉 10 隻／60 期；MRVL 係非持倉，跟 SPCX／ORCL 另開 `config/official_sources_mrvl.yaml`
- `pending_sources`：FY2027-Q2 缺 Form 10-Q（`not_filed_or_not_located_as_of_catalog`）
- `unavailable_sources`：官方電話會議逐字稿（`not_part_of_standard_official_package`）
- 季後官方事件：2026-08-18／19 Form 8-K items 1.01／3.02（accession `0001193125-26-356217`）Google custom 協議＋認股權證。Q2 期終 2026-08-01，**呢筆認股權證係期後事項**，未入 Q2 簡明表。
- 同業會計期唔齊，必須分開標：AMD 2026-Q2 8-K（2026-08-04，已有本倉 F1）；NVDA FY2027-Q2 8-K（2026-08-26，已有本倉 F1）；AVGO 用 yfinance `revenueGrowth` 作 **aggregator 對照**，唔覆寫 MRVL 官方數。
- yfinance 只用於現價、倍數、總回報、共識。**以下 aggregator 同官方衝突，棄用 aggregator：**

| 項目 | yfinance | 官方（用邊個） |
|---|---|---|
| 營收增速 | +27.6% | Q2 FY27 總營收 **+37% YoY**（EX-99.1） |
| 現金 | US$3.84B（似 Q1） | **US$3,932.8m**（2026-08-01 簡明資產負債） |
| 總債務 | US$5.28B | 短期 **US$0** + 長期 **US$4,962.9m** |
| 淨利率 | TTM 28.99% | Q2 GAAP **11.2%**；TTM GAAP ~28% **含 Q3 FY26 汽車乙太網出售一次性** |

第三方稿提到 FY2027／FY2028 約 US$12B／US$18B 指引 → **`source_tier: unverified`**，唔入評分。官方 8-K 只寫「再次上調 fiscal 2027 同 fiscal 2028 營收展望」，冇喺 EX-99.1 正文印出全年美元總數。

官方 TTM（Q3 FY26 + Q4 FY26 + Q1 FY27 + Q2 FY27，USD million）：

| 項目 | Q3 FY26 | Q4 FY26 | Q1 FY27 | Q2 FY27 | TTM |
|---|---:|---:|---:|---:|---:|
| 營收 | 2,075 | 2,219 | 2,417.8 | 2,739.3 | **9,451** |
| GAAP 淨利 | 1,901 | 396.1 | 34.5 | 308.0 | **2,640** |
| 經營現金流 | 582.3 | 373.7 | 638.8 | 605.5 | **2,200** |
| Data Center | n/a（見各季稿） | n/a | 1,832.7 | 2,171.5 | — |

Q3 FY26 GAAP 淨利 US$1.901B 含 2025-08-14 出售汽車乙太網業務予 Infineon、對價現金 US$2.5B（該季 8-K）。TTM 淨利率／ROE **被一次性項目抬高**，評分用最近季同調整後口徑。

## 致命紅線

### 1. 破產／流動性風險：**安全**

條件：現金低於總債務，**並且**自由現金流為負。兩項要同時成立。

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$3,932.8m（2026-08-01） | 8-K EX-99.1 簡明資產負債 |
| 短期債務 | US$0 | 同上（Q4 FY26 年結有短期 US$499.8m） |
| 長期債務 | US$4,962.9m | 同上 |
| **有息債務合計** | **US$4,962.9m** | 現金／債務 = **0.79×** |
| Q2 經營現金流 | US$605.5m | EX-99.1 現金流量表 |
| Q2 購置物業及設備 | US$126.7m | 同上 |
| **Q2 官方口徑 FCF（OCF−capex）** | **US$478.8m** | 自行相減；公司冇單列「FCF」一行 |

現金低過債務，但當季 FCF 為正 → **紅線 1 未觸發**。缺口約 US$1.03B。Celestial AI（2026-02-02）同 XConn（2026-02-10）收購後商譽由年結 US$11.06B 升到 US$13.87B，債務亦上咗。

### 2. 衰退陷阱：**安全**

條件：營收增速低於同業平均，**並且**淨利率為負或連續兩季下降。

- Q2 總營收 US$2,739.3m，YoY **+37%**、QoQ **+13%**（官方）
- 同業最近季營收增速：AMD 官方 +50%；AVGO yfinance +47.9%（aggregator）；NVDA yfinance +85.2%／本倉 NVDA F1 Data Center +117%
- MRVL 增速 **低過** 呢組平均，但 GAAP 淨利率 Q2 **+11.2%**（正），Q1 1.4% → Q2 11.2% **上升** 而非連跌兩季

第二項唔成立 → **紅線 2 未觸發**。增速落後會扣 13 維分數，唔構成即時 FAIL。

### 3. 估值泡沫：**未否決（觀察）**

- PEG（yfinance）**1.45** ＜ 2.5 機械門檻
- 官方 TTM 營收 US$9.45B → 現價隱含 **P/S 23.0×**（217.0／9.45）
- 同業 P/S（yfinance TTM）：AVGO 23.4×、NVDA 21.7×、AMD 18.8×。MRVL 同 AVGO 接近，高過 AMD 約 22%
- 有 +37% 已入帳增長同 DC +46% 支持，**唔係**「顯著高於行業歷史極值且無增長」

紅線 3 未觸發。PEG 相對 AVGO 0.40／NVDA 0.59 仍貴，列入 WATCH 而非 FAIL。

## 13 維度評分

非用戶型公司：「用戶增長」改用官方 **Data Center 已入帳營收增速** 作需求 KPI，並同 AMD／NVDA 資料中心線對照。

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金 US$3.93B；有息債 US$4.96B（0.79×） | 0 | 現金低於債務 | 8-K EX-99.1 2026-08-01 |
| 營收增長 | Q2 +37% YoY；同業 AMD +50%、AVGO ~+48%、NVDA ~+85% | 0 | 低於同業平均 | 官方 vs 同業稿／yfinance 標明 |
| 淨利潤率 | Q2 GAAP 11.2%；Non-GAAP 淨利 US$865.9m | 5 | 10%–25%；TTM ~28% 含出售一次性，唔畀 10 分 | EX-99.1 |
| 估值（PEG） | PEG 1.45；P/S 23.0× vs AVGO 23.4× | 5 | PEG 1–1.5；絕對 P/E trailing ~83× 貴但未到紅線 | yfinance PEG；官方營收計 P/S |
| TAM | AI 基建 custom silicon＋光通訊／交換 | 10 | 可觸及 > US$100B | 官方終端市場表（DC／通訊） |
| 需求 KPI | DC US$2.172B +46% YoY、佔比 79%；AMD DC +107%、NVDA DC +117% | 0 | 低於同行平均 | EX-99.1；本倉 AMD／NVDA F1 |
| ROE | 帳面 TTM ~14%（US$2.64B／權益 US$18.53B）；剔走 Q3 出售後約 7–8% | 0 | 一次性扭曲後低於 8% | EX-99.1；Q3 FY26 出售稿 |
| 自由現金流 | Q2 FCF US$478.8m；Q1 US$483.1m；H1 US$961.9m | 5 | 正但按季持平／微跌，唔算穩定增長 | OCF−PPE |
| 護城河 | custom／光模塊／交換；Google TPU-attach 協議 | 5 | 有客戶深度但面對 AVGO／內部自研 | 8-K 1.01；終端市場表 |
| 行業趨勢 | AI 叢集互联、custom XPU、1.6T 光學 | 10 | 符合核心趨勢 | 官方 Q1／Q2 管理層評論 |
| 管理層能力 | 六季高過指引中位；同時 Q1 GAAP 淨利只有 US$34.5m、優先股＋認股權證 | 5 | 有執行、亦有資本結構變複雜 | 各季 8-K；優先股 2026-03-31 |
| 相對 S&P 500 | 10 年約 +2012% vs SPY +315%（同一窗口） | 10 | 大幅跑贏 | yfinance 2016-08-29→2026-08-28 |
| 預期 vs 實際 | 最近六季全部高過自身指引中位；Q2 高過中位 US$39m | 10 | 連續多季超自身指引 | 各季 EX-99.1 |

**合計：65／130 → WATCH**

## 估值驅動 KPI（Decision HUD 共用；F3 pending）

未有 Framework 3，**禁止 target price／建倉區**。暫定規尺：

| KPI | 最新官方數 | 方向 | 點樣郁倍數 | 來源 |
|---|---|---|---|---|
| 現價 | US$241.45 delayed 8/28 | — | 市值 ~US$217B | yfinance |
| P/S（官方 TTM 營收） | **23.0×** | 持平 AVGO、貴過 AMD | 倍數尺 | 217.0／9.45 |
| PEG | 1.45 | 貴過 AVGO 0.40／NVDA 0.59 | 增長調整倍數 | yfinance |
| H1 官方 FCF vs 市值 | US$0.96B／US$217B ≈ **0.4% 半年**（年化約 0.9%） | 正但收益率極低 | FCF yield 尺 | OCF−PPE |
| Data Center 營收 | US$2,171.5m，+46% YoY，79% mix | 改善 | 增長能否撐 23× P/S | EX-99.1 |
| Q2 官方 FCF | US$478.8m（OCF 605.5 − capex 126.7） | 持平（Q1 483.1） | 去槓桿同 FCF yield | EX-99.1 |
| GAAP 淨利率 | 11.2%（Q1 1.4% → 改善） | 改善 | 盈利質量 vs PEG | EX-99.1 |
| Google 認股權證 | 最多 58,970,907 股、行使價 US$206.58；期後 8-K | 稀釋／訂單能見度 | 分子（股數）同 custom 收入確認 | 8-K 2026-08-19 |

**行動（第一句必須引用溢價／折讓）：** PEG 1.45 對 AVGO／NVDA 約 0.4–0.6 屬明顯溢價，P/S 23× 只同 AVGO 打平、貴過 AMD → **僅觀察，唔好加倉**。F3 pending，呢條唔係目標價。

## Adversarial check

- **最強支持：** 六季高過指引中位；Q2 紀錄營收 US$2.739B（+37%）；DC US$2.172B（+46%、79% mix）；Q3 指引中位 US$3.150B（+/-5%）；期後 Google custom 協議覆蓋 TPU 生態多條 attach 產品。
- **最強反證：** 現金 0.79× 債務；DC 增速大幅慢過 NVDA／AMD；Q1 GAAP 幾乎賺唔到錢；Google 認股權證若全數歸屬約稀釋 6.7% 現有普通股（行使價 US$206.58，現價已價內）；custom「下半年顯著加速」仍大部分未入 Q2 帳。
- **最可能令結論失效嘅假設：** 2H custom／Google 出貨慢過敘事，或者認股權證／優先股稀釋令每股增長對唔住 23× P/S；下一季 FCF 轉負會令紅線 1 重新可觸發（現金已經低過債）。

## 下一步

WATCH 升級至 PASS 嘅量化條件：

1. 最近一季官方簡明表：現金及等價物 **≥** 短期＋長期有息債務（而家缺口 ~US$1.03B），且 FCF 維持正。
2. 官方總營收 YoY 至少追近 custom／資料中心同業（唔再低過 AVGO／AMD 超過 10 個百分點），或 DC 已入帳增速明顯收窄同 NVDA／AMD 嘅差距。
3. 調整後（剔一次性出售）TTM GAAP 淨利率企穩雙位數、ROE >8%，同時 Google 認股權證歸屬同 custom 收入確認可以對得上。

最近催化（唔當 Skill 5 日曆）：FY2027-Q2 電話會議已於 2026-08-27 舉行；**Investor Day 2026-10-06**（官方新聞稿）；FY2027-Q2 10-Q 仍待申報。

Framework 2 必挖兩條問題：

1. **Google custom／TPU-attach 有幾多已經入帳？** Q2 只見到 DC +46% 同「下半年 custom 顯著加速」嘅前瞻句；認股權證歸屬同 US$500m 一檔嘅採購掛鈎，唔等於 Q2 收入。
2. **增長質素對唔住槓桿同稀釋？** 現金低過債、H1 FCF 年化對市值只有約 0.9%、優先股（2026-03-31）加 Google 認股權證。F2 要對現金流、淨負債同稀釋後每股。

*此分析僅供研究參考，不構成投資建議。*
