# AVGO Framework 1 初篩報告

- **結果：** PASS
- **總分：** 120 / 130
- **數據截至：** 2026-09-04（Asia/Hong_Kong 覆核）
- **最新官方季度：** FY2026-Q3（期終 2026-08-02，USD，US GAAP／Non-GAAP，unaudited；SEC 8-K EX-99.1 accession `0001730168-26-000076`，filing date 2026-09-02，`validation_status: verified` 業績稿）
- **10-Q：** FY2026-Q3 Form 10-Q **未申報**（catalog／manifest `pending_sources: regulatory_filing`／`validation_status: partial`）。資產負債同現金流用同期 8-K 簡明表；唔當已審 10-Q。
- **現價：** US$357.16（yfinance delayed，2026-09-03 收市，America/New_York）；市值約 US$1.699T；普通股約 4,758m 股（yfinance shares outstanding）；Q3 GAAP 攤薄加權 4,887m 股（官方）
- **持倉：** **未確認**
- **核心結論：** 最大亮點係 Q3 已入帳營收 US$29.591B（+86% YoY）同 AI 半導體 US$16.7B（+221% YoY、+54% QoQ），官方自由現金流（FCF，Free Cash Flow）單季 US$13.665B；最大風險係現金 US$24.0B 只有有息債務 US$59.4B 嘅 0.40 倍，以及客製加速器／超大規模客戶集中度。

## 數據驗證

- 非持倉：另開 `config/official_sources_avgo.yaml` + `data/source-catalog/avgo-six-quarters.json`。**冇**塞入持倉 `config/official_sources.yaml`。
- `data/raw/AVGO/`：六季 bootstrap manifests（FY2025-Q2 至 FY2026-Q3）。Cloud 只提交 `manifest.json` URL 目錄，**唔提交** SEC HTML／PDF 正文。
- `python scripts/validate_raw_manifests.py --root data/raw/AVGO`：**唔跑本地 hash 通過**——bootstrap 註明 `local_body_not_fetched_in_bootstrap`；本輪數字係直接讀 SEC EX-99.1（2026-09-04 拉取），唔經 aggregator。
- `--coverage-config` **唔跑**持倉 60 期腳本；AVGO 跟 NVDA／MRVL／ORCL 非持倉模式。
- `pending_sources`：FY2026-Q3 缺 Form 10-Q（`not_filed_or_not_located_as_of_catalog`）；六季皆 `local_body_not_fetched_in_bootstrap`。
- `unavailable_sources`：官方電話會議逐字稿（`not_part_of_standard_official_package`）。Hock Tan／CFO 評論只引用 8-K EX-99.1 正文已印出嘅句子。
- 同業會計期唔齊，必須分開標：NVDA FY2027-Q2（期終 2026-07-26，本倉 F1）；AMD 2026-Q2（期終 2026-06-27，本倉 F1）；MRVL FY2027-Q2（期終 2026-08-01，本倉 F1）；TSMC 2026-Q2 6-K（本倉 NVDA F1 引用）；INTC 2026-Q2（同上）。
- yfinance 只用於現價、市值、共識 EPS、歷史總回報、PEG 對照。**以下 aggregator 同官方衝突，一律棄用 aggregator：**

| 項目 | yfinance | 官方（用邊個） |
|---|---|---|
| 最近季營收增速 | +47.9%（停留喺 Q2） | Q3 FY26 **+86% YoY**（EX-99.1） |
| TTM P/S | 22.52× | 市值 US$1.699T／官方 TTM 營收 US$89.104B ≈ **19.1×** |
| 現金 | US$19.6B（似 Q2） | **US$23,975m**（2026-08-02 簡明資產負債） |
| 總債務 | US$64.9B | 短期 **US$2,252m** + 長期 **US$57,167m** = **US$59,419m** |
| TTM FCF | US$27.2B | 四季官方 FCF 加總 **US$39,403m** |
| Q3 已報 EPS | Reported = NaN（未入庫） | GAAP 攤薄 **US$2.68**；Non-GAAP **US$3.32** |

第三方稿提到 FY2027／FY2028 AI 營收約 US$115B／US$230B、Q4 指引「略低過街貨」→ **`source_tier: unverified`**，唔入評分、唔覆寫官方 Q4 指引 **約 US$34.8B**。

官方 TTM（Q4 FY2025 + Q1 FY2026 + Q2 FY2026 + Q3 FY2026，USD million）：

| 項目 | Q4 FY25 | Q1 FY26 | Q2 FY26 | Q3 FY26 | TTM |
|---|---:|---:|---:|---:|---:|
| 營收 | 18,015 | 19,311 | 22,187 | 29,591 | **89,104** |
| GAAP 淨利 | 8,518 | 7,349 | 9,310 | 13,088 | **38,265** |
| 官方 FCF | 7,466 | 8,010 | 10,262 | 13,665 | **39,403** |
| Semiconductor solutions | 11,072 | 12,515 | 15,009 | 20,839 | **59,435** |
| Infrastructure software | 6,943 | 6,796 | 7,178 | 8,752 | **29,669** |

來源：各季 8-K EX-99.1。Q3 分部 70%／30% mix 來自同期業績稿。AI 半導體係 CEO 已入帳評論（唔係獨立分部列），Q1 US$8.4B、Q2 US$10.8B、Q3 US$16.7B；Q4 FY25 CEO 稱 AI 半導體約 US$8.2B。

## 致命紅線

### 1. 破產／流動性風險：**安全**

條件：現金低於總債務，**並且**自由現金流為負。兩項要同時成立。

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$23,975m（2026-08-02） | 8-K EX-99.1 簡明資產負債 |
| 短期債務 | US$2,252m | 同上 |
| 長期債務 | US$57,167m | 同上 |
| **有息債務合計** | **US$59,419m** | 現金／債務 = **0.40×** |
| Q3 經營現金流 | US$14,197m | EX-99.1 |
| Q3 購置物業及設備 | US$532m | 簡明現金流量表 |
| **Q3 官方 FCF** | **US$13,665m**（收入 46%） | EX-99.1 已單列 Free cash flow |
| 九個月官方 FCF | US$31,937m | 同上（三個財政季） |

現金低過債務，但當季同 TTM FCF 大額為正 → **紅線 1 未觸發**。淨負債約 US$35.4B。FY2025 年結長期債 US$61,984m → Q3 US$57,167m，有在還。10-Q 未出，唔用 yfinance 債務。

### 2. 衰退陷阱：**安全**

條件：營收增速低於同業平均，**並且**淨利潤率為負或連續兩季下降。

| 公司 | 最近季營收 | YoY | 期終／基準 | 來源 |
|---|---:|---:|---|---|
| **AVGO** | US$29,591m | **+86%** | FY2026-Q3 期終 2026-08-02；US GAAP | AVGO 8-K EX-99.1 2026-09-02 |
| NVDA | US$96,221m | **+106%** | FY2027-Q2 期終 2026-07-26 | 本倉 NVDA F1；8-K EX-99.1 |
| AMD | US$11,536m | **+50%** | 2026-Q2 期終 2026-06-27 | 本倉 AMD F1；8-K EX-99.1 |
| MRVL | US$2,739m | **+37%** | FY2027-Q2 期終 2026-08-01 | 本倉 MRVL F1；8-K EX-99.1 |
| TSM | US$40.20B | **+33.7% USD** | 2026-Q2；TIFRS | 本倉 NVDA F1 引用 TSMC 6-K |
| INTC | US$16.1B | **+25%** | 2026-Q2；US GAAP | 本倉 NVDA F1 引用 INTC 8-K |

同業五間公司營收增速平均約 **+50.3%**。AVGO 高過同業約 **36 個百分點**。Q3 GAAP 淨利率 **44.2%**（US$13,088m／US$29,591m）；Q2 42.0%、Q1 38.1%、Q4 FY25 47.3%——Q4→Q1 曾跌，之後兩季回升，**唔係**「負或連續兩季下降」。兩項條件都不成立 → **不觸發。**

### 3. 估值泡沫：**未否決**

- 官方 TTM GAAP EPS ≈ US$7.83（1.74＋1.50＋1.91＋2.68）；現價 US$357.16 → trailing P/E ≈ **45.6×**。配官方營收增速 +86% → 近似 PEG **0.53**。yfinance PEG **0.42**／trailingPegRatio 0.42（第三方）同樣 < 1，遠低於 2.5 紅線。
- 官方 TTM P/S ≈ **19.1×**（US$1.699T／US$89.104B）。yfinance 22.5× 用少一季 TTM，棄用。
- 同業倍數語境（唔當 target）：NVDA F1 官方 TTM P/S 16.8×（截至 2026-08-26）；而家 NVDA yfinance ~18.2×。AMD yfinance ~18.0×。MRVL F1 當時 23.0×，而家 yfinance ~19.9×。AVGO 19.1× **唔係**「顯著高於行業歷史極值且無增長」。
- 增長支持充分：單季 +86%、AI 半導體 +221%、Q4 官方指引約 US$34.8B（+93% YoY）。「缺乏相應高增長」不成立。

因此紅線 3 **不觸發**。倍數絕對唔平，但規則要 PEG>2.5 或 P/S 極值**加上**無增長。

## 13 維度評分

非用戶型公司：「用戶增長」改用官方 **AI 半導體已入帳營收增速** 作需求 KPI，並同 NVDA／AMD／MRVL 資料中心線對照。

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金 US$24.0B；有息債 US$59.4B（0.40×） | 0 | 現金低於債務 | 8-K EX-99.1 2026-08-02 簡明表 |
| 營收增長 | Q3 +86% YoY；同業五間平均約 +50% | 10 | 高於同業超過 10pp（實際約 +36pp） | AVGO EX-99.1；本倉 NVDA／AMD／MRVL F1 |
| 淨利潤率 | Q3 GAAP 44.2%；TTM 43.0%。Non-GAAP 淨利 US$16.372B | 10 | 遠高於 25% | EX-99.1 |
| 估值（PEG） | 官方近似 PEG 0.53；yfinance 0.42。P/S 19.1× 有 +86% 支持 | 10 | PEG < 1 | 官方 TTM；市況 yfinance |
| TAM | TTM 已入帳 US$89.1B；Q4 指引年化約 US$139B。用公司已實現／已指引做下限，唔另估未證實 TAM | 10 | 可觸及 > US$100B | EX-99.1 |
| 需求 KPI（AI 半導體） | AVGO AI 半導體 +221%（US$16.7B）；NVDA DC +117%；AMD DC +107%；MRVL DC +46%。AI／DC 同業平均約 +90%，AVGO 高約 131pp | 10 | 高於同行平均超過 20pp | AVGO CEO 評論（EX-99.1）；本倉 F1 |
| ROE | TTM 淨利 US$38.3B／期末權益 US$99.7B ≈ 38%；平均權益約 42% | 10 | 遠高於 15% | 簡明資產負債；四季 8-K |
| 自由現金流 | TTM US$39.4B；Q4→Q1→Q2→Q3：7.5／8.0／10.3／13.7，四季連升 | 10 | 穩定增長且為正 | 各季 EX-99.1 FCF |
| 護城河 | 客製 AI 加速器＋乙太網交換／連接；Infrastructure software（VMware 等）佔 Q3 30%、+29% YoY。反證：超大規模客戶集中、NVDA 訓練份額仍大 | 10 | 顯著設計／軟件壁壘，集中度記入 adversarial | EX-99.1 分部表 |
| 行業趨勢 | 客製 XPU、AI 叢集網絡、基礎設施軟件 | 10 | 完全符合未來核心趨勢 | EX-99.1 Hock Tan 評論 |
| 管理層能力 | 連續多年 Non-GAAP EPS beat；Q3 再創新高營收／FCF；長期債較年結下降。瑕疵：槓桿仍高、Q3 後一日大成交量下跌 | 10 | 行業領先執行，槓桿記入現金維度已扣 0 分 | EX-99.1；yfinance 共識 |
| 相對 S&P 500 | 2009-08-06 Avago／AVGO 上市起總回報約 +31,352%；同期 SPY 約 +948%；超額約 +30,404pp | 10 | 遠高於 +20pp | yfinance 調整後收市（含股息近似） |
| 市場預期 vs 實際 | 近四季 Non-GAAP EPS 全 beat：Q4 FY25 +4.4%、Q1 +1.3%、Q2 +1.7%；Q3 官方 US$3.32 vs yfinance 估計 US$3.24（約 +2.5%；yfinance 尚未寫入 Reported） | 10 | 連續多季超預期 | yfinance earnings_dates（第三方共識）；實際來自 8-K |

**合計：120／130 → PASS**（門檻：PASS 90–130；WATCH 65–85；FAIL 0–60）

分數結構：10 分 12 項；5 分 0 項；0 分 1 項（現金 vs 債務）。

## 估值驅動 KPI（Decision HUD 共用；F3 pending）

未有 Framework 3，**禁止 target price／建倉區**。暫定規尺：

| KPI | 最新官方數 | 方向 | 點樣郁倍數 | 來源 |
|---|---|---|---|---|
| 現價 | US$357.16 delayed 9/03 | 業績後兩日由 367.24 跌到 357.16 | 市值 ~US$1.699T | yfinance |
| P/S（官方 TTM 營收） | **19.1×** | 略高過 NVDA／AMD ~18× | 倍數尺；非 target | 1,699／89.104 |
| PEG | 0.42（yfinance）／0.53（官方 trailing） | 遠低於 2.5 | 增長調整倍數 | yfinance；官方增速 |
| TTM 官方 FCF vs 市值 | US$39.4B／US$1.699T ≈ **2.3%** | 改善（四季 FCF 連升） | FCF yield 尺 | 四季 EX-99.1 |
| AI 半導體營收 | US$16.7B，+221% YoY，+54% QoQ | 改善 | 增長能否撐 19× P/S | EX-99.1 CEO |
| Q3 官方 FCF | US$13.665B（OCF 14,197 − capex 532） | 改善 | 去槓桿同 FCF yield | EX-99.1 |
| GAAP 淨利率 | 44.2%（Q2 42.0% → 改善） | 改善 | 盈利質量 vs PEG | EX-99.1 |
| 現金／有息債 | 0.40×（US$24.0B／US$59.4B） | 覆蓋弱、但 FCF 正 | 槓桿折讓 | 簡明資產負債 |

**行動（第一句必須引用溢價／折讓）：** 官方 TTM P/S 19.1× 對 NVDA／AMD 近期約 18× 有約 **5% 溢價**（對本倉 NVDA F1 當時 16.8× 溢價更大），PEG 0.4–0.5 並無泡沫紅線 → **僅觀察，唔好把 F1 PASS 當成建倉區**。F3 pending，呢條唔係目標價。

## Adversarial check

- **最強支持：** Q3 已入帳 US$29.591B（+86%）；AI 半導體 US$16.7B（+221%、+54% QoQ）；官方 FCF US$13.665B（46% of revenue）；半導體分部 +127%；連續多季 Non-GAAP EPS beat；Q4 官方指引約 US$34.8B（+93%）、AI 半導體指引 US$21.7B（+236% YoY）——指引唔當已入帳。
- **最強反證：** 現金只有債務 0.40 倍，紅線 1 只係因為 FCF 為正先未觸發；應收由年結 US$7.1B 去到 US$13.7B，增長有一部分係賬期；客製 XPU 客戶極集中，任何一間超大規模 Capex 轉向都會令 +54% QoQ 唔可持續；Q3 公布後 9/03 成交 6,014 萬股、收市跌至 US$357.16，市場已經喺消化 Q4 指引同供應約束（第三方敘事，`unverified`）。
- **最可能令結論失效嘅假設：** 一至兩間客製加速器客戶把增量轉去自研／對手，同時應收再脹令單季 FCF 轉負——現金已經低過債，紅線 1 會重新可觸發；或者 19× P/S 喺增速由 86% 回落到同業平均時一次性壓縮。

## 下一步（PASS → Framework 2）

Framework 2 必須深挖嘅兩個問題：

1. **客製 AI 加速器入帳質素同客戶集中：** Q3 AI 半導體 US$16.7B、+54% QoQ，有幾多已經係可重複 XPU 出貨、幾多係網絡／一次性增量？要按客戶／產品拆（8-K 冇拆），並對 Q4 指引 US$21.7B 係延續定係預支。
2. **槓桿同工作資本會唔會食咗 FCF：** 現金 0.40× 債務、應收 US$13.7B（年結 US$7.1B）、九個月回購 US$8.45B 加每季股息約 US$3.1B。F2 要對淨負債軌跡、DSO、同「FCF 轉負會立即激活紅線 1」嘅情景。

技術面（次要權重，yfinance delayed 2026-09-03）：收市 US$357.16，業績日（9/02）收 367.24 之後第二日放量下跌；1 年回報約 +19.0%，略輸 SPY 約 +21.4%——符合「beat 之後 sell-the-news」，**唔抵消**基本面 PASS。

互動報告：`output/AVGO_framework1.html`

*此分析僅供研究參考，不構成投資建議。*
