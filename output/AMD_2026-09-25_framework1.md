# AMD Framework 1 初篩報告

- **結果：** **PASS**
- **總分：** **90 / 130**
- **數據截至：** 2026-09-25（Asia/Hong_Kong 覆核）
- **最新官方季度：** 2026-Q2（期終 2026-06-27，USD，US GAAP／Non-GAAP，unaudited；SEC 8-K EX-99.1 accession `0000002488-26-000121`，filing date 2026-08-04，[EX-99.1](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/q22026991.htm)；Form 10-Q accession `0000002488-26-000123`，filing date 2026-08-05，[10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm)；`validation_status: verified`）
- **2026-Q3：** 會計期終約 2026-09-26，**尚未公布**。今次刷新唔改 Q2 帳面，只加入季後官方 IR 事件同現價倍數。
- **現價：** US$629.26（yfinance delayed，2026-09-24 收市，America/New_York）；前收 US$614.61（2026-09-23）。市值約 **US$1.027T**（yfinance `marketCap`）；Q2 官方攤薄加權 **1,659m** 股
- **持倉：** **未確認**
- **Framework 3：** `output/AMD_2026-08-27_framework3.md` 嘅 Bear 240／Base 390／Bull 620（約 2026-09-03 現價校準）**已過期**。本頁 HUD 標 **`F3 pending` refresh**，**唔寫新 target price**。
- **核心結論：** 最大亮點仍係 Data Center 已入帳 US$6,718m（+107% YoY）同三條紅線未觸發；最大風險係現價對同業／自身歷史倍數明顯溢價（官方 TTM P/S 約 24.9×），而且 Helios rack-scale **仍未有官方美元收入／時間表量化**。

## 數據驗證

- `python scripts/validate_raw_manifests.py --root data/raw/AMD`：**通過**（6 manifests；2025-Q1–2026-Q2 complete）
- `--coverage-config config/official_sources.yaml`：呢個 cloud checkout **冇**其餘 9 隻持倉 `data/raw/` 正文，60 期覆蓋檢查唔可當通過。AMD 自身六季包 `pending_sources: 0`
- `unavailable_sources`：官方電話會議逐字稿（`not_part_of_standard_official_package`）
- 2026-09-08 Citi／2026-09-11 Goldman 第三方逐字稿：`source_tier: unverified`，只當線索，**唔覆寫**官方數字、**唔當** Helios 已入帳
- 同業會計期唔齊，必須分開標：NVDA FY2027-Q2（期終 2026-07-26）；AVGO FY2026-Q3（期終 2026-08-02）；MRVL FY2027-Q2（期終 2026-08-01）；TSMC 2026-Q2；INTC 2026-Q2
- yfinance 只用於現價、市值、共識 EPS、歷史總回報、PEG 對照、RSI。**以下 aggregator 同官方衝突，一律棄用 aggregator：**

| 項目 | yfinance | 官方（用邊個） |
|---|---|---|
| 總債務 | US$4.276B | 流動長期債 US$875m + 長期債 US$2,351m = **US$3,226m**（8-K Selected Corporate Data） |
| TTM FCF | US$8.84B | 四季官方 FCF 加總 **US$7,736m** |
| Trailing EPS | US$3.93 | GAAP 攤薄 0.75＋0.92＋0.84＋1.38 = **US$3.89** |
| 營收增速 | +50.1%（接近） | Q2 **+50%**（US$11,536m／US$7,685m） |

官方 TTM（2025-Q3 + 2025-Q4 + 2026-Q1 + 2026-Q2，USD million）：

| 項目 | Q3'25 | Q4'25 | Q1'26 | Q2'26 | TTM |
|---|---:|---:|---:|---:|---:|
| 營收 | 9,246 | 10,270 | 10,253 | 11,536 | **41,305** |
| GAAP 淨利 | 1,243 | 1,511 | 1,383 | 2,297 | **6,434** |
| 官方 FCF | 1,530 | 2,082 | 2,566 | 1,558 | **7,736** |
| Data Center | 4,341 | 5,380 | 5,775 | 6,718 | **22,214** |

來源：各季 8-K EX-99.1（Q3'25 [q32025991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248825000163/q32025991.htm)；Q4'25 [q42025991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000014/q42025991.htm)；Q1'26 [q12026991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000072/q12026991.htm)；Q2'26 [q22026991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/q22026991.htm)）。Q3'25 FCF US$1,530m 嚟自同期 EX-99.2 調節表。IR 業績頁：https://ir.amd.com/financial-information/financial-results

## 相對 2026-08-27 F1 嘅分數變化

上份書面寫 **95／130 PASS**，但表內 9 項 10 分 + 4 項 5 分加總其實係 **110**（算術唔一致）。今次**只跟 `SCORING.md`** 重評：

| 維度 | 08-27 表內 | 今次 | 原因 |
|---|---:|---:|---|
| 營收增長 | 10 | **5** | +50% 對 AI／DC 同業公司平均約 +58%，唔夠「高過均值 10pp」 |
| 淨利潤率 | 10 | **5** | GAAP Q2 19.9%、TTM 15.6%，落喺 10%–25% |
| 估值（PEG） | 5 | **0** | 官方 trailing PEG ≈ 3.2；TTM P/S 24.9× 明顯貴過 NVDA／AVGO |
| 需求 KPI | 10 | **5** | DC +107% 高過 NVDA+INTC 平均約 19pp，未到 20pp；唔再用「純 CPU」作對照 |
| ROE | 10 | **5** | TTM 9.6%，落喺 8%–15% |
| 預期 vs 實際 | 5 | **10** | 近四季 Non-GAAP EPS 全 beat 共識；近三季營收超自身指引中位 |
| **合計（書面）** | **95（表內 110）** | **90** | 書面 −5；若按上份表內加總則 −20 |

門檻：PASS 90–130。90 仍係 PASS，但估值維度已扣到零，再貴一截就會跌入 WATCH。

## 致命紅線

### 1. 破產／流動性風險：**安全**

條件：現金低於總債務，**並且**自由現金流為負。兩項要同時成立。

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$5,086m（2026-06-27） | 10-Q／8-K 資產負債表 |
| 短期投資 | US$8,025m | 同上 |
| **現金＋短投（公司 Selected Data）** | **US$13,111m** | 8-K EX-99.1 Selected Corporate Data |
| 流動長期債 | US$875m | 資產負債表 |
| 長期債 | US$2,351m | 同上 |
| **總債務** | **US$3,226m** | 8-K Selected Data；現金＋短投／債務 = **4.06×** |
| Q2 持續經營 OCF | US$2,366m（margin 21%） | EX-99.1 FCF 調節 |
| Q2 capex（購置 PPE） | US$808m | 同上 |
| **Q2 官方 FCF** | **US$1,558m**（margin **14%**） | 同上 |
| Q1 官方 FCF | US$2,566m（margin 25%） | 同上 |
| H1 官方 FCF | US$4,124m（margin 19%） | 同上 |
| TTM 官方 FCF | US$7,736m（margin 18.7%） | 四季 8-K 加總 |

現金遠高於債務，FCF 為正 → **紅線 1 未觸發**。yfinance 總債 US$4.28B 棄用。

### 2. 衰退陷阱：**安全**

條件：營收增速低於同業平均，**並且**淨利潤率為負或連續兩季下降。

| 公司 | 最近季營收 | YoY | 期終／基準 | 來源 |
|---|---:|---:|---|---|
| **AMD** | US$11,536m | **+50%** | 2026-Q2 期終 2026-06-27；US GAAP | AMD 8-K EX-99.1 2026-08-04 |
| NVDA | US$96,221m | **+106%** | FY2027-Q2 期終 2026-07-26 | 本倉 NVDA F1；8-K EX-99.1 |
| AVGO | US$29,591m | **+86%** | FY2026-Q3 期終 2026-08-02 | 本倉 AVGO F1；8-K EX-99.1 |
| MRVL | US$2,739m | **+37%** | FY2027-Q2 期終 2026-08-01 | 本倉 MRVL F1 |
| TSM | US$40.20B | **+33.7% USD** | 2026-Q2；TIFRS | 本倉 NVDA F1 引用 TSMC 6-K |
| INTC | US$16.1B | **+25%** | 2026-Q2；US GAAP | 本倉 NVDA F1 引用 INTC 8-K |

同業五間公司營收增速平均約 **+57.5%**。AMD +50% 略低約 7.5 個百分點，但遠未倒退。GAAP 淨利率：Q4'25 14.7%、Q1'26 13.5%、Q2'26 **19.9%**——Q2 回升，**唔係**「負或連續兩季下降」。兩項條件都不成立 → **不觸發。**

### 3. 估值泡沫：**未否決（觀察）**

規則要「PEG > 2.5 **或** P/S 顯著高於歷史／同業極值」**並且**缺乏相應高增長。本倉 NVDA／TSLA F1 都係咁解讀。

- 官方 trailing P/E ≈ **161.8×**（US$629.26／TTM GAAP EPS US$3.89）。配官方營收增速 +50% → 近似 trailing PEG **3.24**（> 2.5）。
- yfinance PEG／trailingPegRatio **0.63**（第三方；配合 forward EPS 約 US$15.57）。呢個增長假設把 Helios／2027 盈利預支，**Helios 美元收入尚未官方量化** → 增長估算**不可靠**，唔可用嚟否決「貴」，亦唔可用嚟打 10 分。
- 官方 TTM P/S ≈ **24.9×**（市值 US$1.027T／TTM 營收 US$41.305B）。同業（yfinance delayed 2026-09-24）：NVDA 17.9×、AVGO 18.8×、INTC 11.8×。AMD 貴過最近 AI／DC 對照約 **6–7 圈**。
- 增長支持仍然存在：單季 +50%、DC +107%、Q3 官方指引約 US$13.0B ±0.3B（+41% YoY）。「缺乏相應高增長」**不成立**。

因此紅線 3 **不觸發**。倍數已經貴到 PEG 維度 0 分，但規則要無增長先機械 FAIL。

## 13 維度評分

非用戶型公司：「用戶增長」改用官方 **Data Center 已入帳營收增速** 作需求 KPI，並同 NVDA Data Center／Intel DCAI 對照。AVGO AI 半導體（客製 ASIC）另列，唔併入平均。

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金＋短投 US$13.1B；總債 US$3.2B（4.06×）。單計現金 US$5.1B 都高過債 | 10 | 現金至少為債務 2 倍 | 8-K EX-99.1 2026-06-27 Selected Data |
| 營收增長 | Q2 +50%；同業五間平均約 +58% | 5 | 與行業均值大致持平（差約 7.5pp），未高過 10pp | AMD／NVDA／AVGO／MRVL／TSM／INTC 官方稿 |
| 淨利潤率 | Q2 GAAP 19.9%；TTM 15.6%。Non-GAAP Q2 淨利 US$2,760m（23.9%） | 5 | 10%–25%，未到 25% | EX-99.1 |
| 估值（PEG） | 官方 trailing PEG ≈ 3.24；TTM P/S 24.9× vs NVDA 17.9×／AVGO 18.8×。yfinance PEG 0.63 用不可靠前瞻盈利 | 0 | PEG > 1.5 **或**估值嚴重透支 | 官方 TTM；市況 yfinance 2026-09-24 |
| TAM | 官方 AAI 2026：AMD total compute TAM 2030 約 **US$2T**（2025 US$365B）。用公司已公布 TAM，唔另估 | 10 | 可觸及 > US$100B | IR／Newsroom 2026-07-23 AAI 稿 |
| 需求 KPI（Data Center） | AMD DC +107%（US$6,718m）；NVDA DC +117%；INTC DCAI +59%。兩同業平均約 +88%，AMD 高約 **19pp**。AVGO AI +221% 係客製 ASIC，另列 | 5 | 高於同行平均超過 10pp，未到 20pp | AMD EX-99.1；本倉 NVDA F1 |
| ROE | TTM 淨利 US$6,434m／期末權益 US$67,224m ≈ **9.6%**；平均權益約 9.9% | 5 | 8%–15% | 10-Q；四季 8-K |
| 自由現金流 | TTM US$7.7B 為正；Q4→Q1→Q2：2.08／2.57／1.56，Q2 回落 | 5 | 有波動但為正，未當「穩定增長」 | 各季 EX-99.1 FCF |
| 護城河 | EPYC x86 伺服器＋Instinct／Helios 開放 rack。反證：CUDA 生態仍厚、AI 軟件／系統仍追 NVDA | 5 | 有壁壘但唔係行業最寬 | 8-K Lisa Su 評論；AAI 稿 |
| 行業趨勢 | AI 基建、資料中心 capex、rack-scale、agentic AI | 10 | 完全符合未來核心趨勢 | EX-99.1；AAI 2026 IR |
| 管理層能力 | Lisa Su 多年份額提升；近三季超自身指引。瑕疵：Helios 已講 ramp 兩個月仍無美元數 | 10 | 行業領先執行，Helios 空白記入 adversarial | IR／8-K |
| 相對 S&P 500 | 1Y +291% vs SPY +17%。1993-01-29 起（SPY 可對齊）AMD 約 +6,612% vs SPY +3,089%，超額約 +3,523pp | 10 | 遠高於 +20pp | yfinance 調整後收市（含股息近似） |
| 市場預期 vs 實際 | 近四季 Non-GAAP EPS 全 beat 共識：Q3'25 +2.5%、Q4'25 +16.0%、Q1'26 +5.8%、Q2'26 +3.2%。近三季營收超自身指引中位 | 10 | 連續多季超預期 | 官方指引／實際來自 8-K；共識 yfinance（第三方） |

**合計：90／130 → PASS**（門檻：PASS 90–130；WATCH 65–85；FAIL 0–60）

分數結構：10 分 6 項；5 分 6 項；0 分 1 項（估值 PEG）。

### 近四季 actual vs 自身指引／共識

| 季度 | 官方營收 | 自身指引中位（±0.3B） | vs 指引 | 官方 Non-GAAP EPS | yfinance 共識 | Surprise |
|---|---:|---:|---|---:|---:|---:|
| 2025-Q3 | 9,246 | （上季指引；本輪以 Q4 起連續核對） | — | 1.20 | 1.17 | +2.5% |
| 2025-Q4 | 10,270 | **9.6**（Q3'25 outlook） | **高過上限 9.9** | 1.53 | 1.32 | +16.0% |
| 2026-Q1 | 10,253 | **9.8**（Q4'25 outlook，含約 US$100m 對華 MI308） | **高過上限 10.1** | 1.37 | 1.29 | +5.8% |
| 2026-Q2 | 11,536 | **11.2**（Q1'26 outlook） | **略高過上限 11.5** | 1.66 | 1.61 | +3.2% |
| 2026-Q3 指引 | — | **13.0**（Q2'26 outlook） | 未公布 | — | 1.93（未報） | — |

Q3 2026 業績 yfinance 估 2026-11-03，**未見官方確認日期**。

## 季後必須記入嘅官方發展（唔改變 Q2 帳面）

### 官方確認嘅兩場 9 月 IR 活動

AMD 2026-07-08 IR 新聞稿同 IR Calendar **正式確認**參加：

1. **2026-09-08 09:30 EDT — Citi’s 2026 Global TMT Conference**（出席：CFO Jean Hu、CVP IR Matt Ramsay；第三方逐字稿）  
   官方出席確認：[2026-07-08 IR 稿](https://ir.amd.com/news-events/press-releases/detail/1289/amd-to-report-fiscal-second-quarter-2026-financial-results)＋[IR Calendar](https://ir.amd.com/news-events/ir-calendar/detail/20260908-citis-2026-global-tmt-conference)
2. **2026-09-11 08:50 PDT — Goldman Sachs Communacopia + Technology Conference**（出席：SVP Dan McNamara、Matt Ramsay；第三方逐字稿）  
   官方出席確認：同上 7/8 稿＋[IR Calendar](https://ir.amd.com/news-events/ir-calendar/detail/20260911-goldman-sachs-communacopia-technology-conference)

官方披露層級：IR 確認出席＋webcast 入口。**冇**對應 Form 8-K 把會議內容入檔。以下會議內容除非另註，一律 `unverified` 第三方逐字稿。

**Citi 9/8（unverified，CFO 口述線索）：** Helios／MI450 ramp「very well」；Q3 係量產出貨**最初期**，預期 **Q3 有收入**，Q4「very significant step up」，2027-Q1 再上一級；2027 需求／數量高過最初預期。**冇講 Helios 美元數、冇改 Q3 US$13B 指引。** 錨點客戶口述為 Meta、OpenAI、Anthropic（多 GW、跨代）。MI350 對其他 model builder／NeoCloud／企業「tremendous demand」。伺服器 CPU：下半年 YoY >80%、明年 >70%（供應受限）——**唔當已入帳**。毛利率：Q3 官方指引 Non-GAAP **56%**；口述 MI450 ramp 會令 2027 毛利率「略低過 Q3 指引」，靠 EPYC／Embedded 組合對沖。

**Goldman 9/11（unverified）：** 公司由「多條硅產品線」轉做 **full rack-scale system provider**；而家最大焦點係 Helios 對頭部客戶落地。強調 tokens per dollar／TCO，**同樣冇 Helios 收入數字**。

### Helios 狀態（官方 vs 未量化）

| 聲明 | 層級 | 含義 |
|---|---|---|
| Q2 8-K：Helios「begins to ramp」；Lisa Su：Instinct deployments scale and Helios begins to ramp | 官方 8-K EX-99.1 2026-08-04 | Q2 **幾乎未入帳**；無美元數 |
| AAI 2026（2026-07-23 IR）：Helios「now in production to be deployed by leading AI companies at gigawatt scale」；72× MI455X + 18× 6th Gen EPYC Venice + Pensando + ROCm | 官方 IR [AAI 稿](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) | 產品／架構已發布；**收入未量化** |
| 官方 Helios 客戶名單（AAI／Q2 8-K）：Anthropic、Cirrascale、HUMAIN、Meta、Microsoft、OpenAI、Oracle、Tensorwave、Vultr 等 | 官方 | 部署敘事，唔係已入帳 GW |
| 9/8 CFO：Q3 開始量產、Q3 預期有收入、Q4 大級跳 | 第三方逐字稿 | 時間線索；**仍無 $** |

**結論：Helios rack-scale 收入／出貨美元數，截至 2026-09-25，官方仍未量化。** 唔可把「in production／begins to ramp」寫成已入帳。

### MI 系列客戶（官方或公司確認）

| 客戶 | 官方內容 | 時間／來源 | 入帳狀態 |
|---|---|---|---|
| **Anthropic** | 最多 **2 GW** MI450 Series（MI455X）配 Helios；第一 GW 由 **2027 上半年**開始；已用 MI355X；AMD 承諾最多 **US$5B** 戰略股權投資 | [2026-07-22 IR](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) | 前瞻部署，**未入帳** |
| **OpenAI** | 2025-10-06 已公布最多 **6 GW**，第一 GW 2026 下半年；AAI：Helios 預期 **2026-Q4** 起上線、2027 加速 | [2025-10-06 IR](https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)＋[AAI 2026-07-23](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) | 兩篇官方時間略有 Q4 vs 2H 表述差，**都係前瞻** |
| **Meta** | 最多 **6 GW** Instinct；第一 GW **2026 下半年**，客製 **MI450 架構** GPU + Venice + Helios；Form 8-K 另披露最多 **1.60 億股**績效認股權證（US$0.01） | [2026-02-24 IR](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)；8-K accession `0000002488-26-000045` | 前瞻；Q2 仍未拆 Helios $；認股權證官方已入檔 |
| **Microsoft Azure** | 擴展合作，Azure 規模部署 Helios 做前沿模型推理；新 EPYC VM＋Pensando DPU | Q2 8-K Recent Highlights | 敘事，無 $ |
| **Cerebras** | Helios 同 Wafer-Scale Engine 一齊做超低延遲推理 | Q2 8-K | 合作，無 $ |
| **MI350／MI350P／MI355X** | Q3'25 DC 增長已寫 MI350 Series；Q2 再發 MI350P；Anthropic 已用 MI355X | 各季 8-K／Anthropic 稿 | Instinct 已喺 DC 入帳，**無官方拆 MI350 美元** |
| **MI400／MI450／MI455X／MI430X** | AAI 發布 MI400 家族；Helios 用 MI455X；MI430X 主打 HPC／主權 AI | AAI／Q2 8-K | 產品已發布；出貨 $ 待 Q3 |

第三方會議把「三大錨點客戶」講成 Meta／OpenAI／Anthropic，同官方名單一致，但 **GW 同 $ 仍然係前瞻**。Meta **績效認股權證**最多 **1.60 億股**（行使價 US$0.01）係 **2026-02-24 Form 8-K** 官方披露（accession `0000002488-26-000045`）：第一 GW 出貨開始歸屬，滿 6 GW 先全數歸屬，另有股價門檻（最後一檔至 US$600）。對照 Q2 攤薄加權 1,659m 股，全數歸屬約 **9.6%** 潛在攤薄。呢條係 covered-call／股本旗標，**唔入 130 分**，亦**唔當** Helios 已入帳。

## 估值驅動 KPI（Decision HUD 共用；**F3 pending refresh**）

舊 F3（2026-08-27／現價校準約 9/03）：Bear **US$240**／Base **US$390**／Bull **US$620**。**已過期，唔當活估值尺。** 現價 US$629.26 對舊 Base 約 **+61%**、對舊 Bull 約 **+1.5%**——只用來標「舊圖已穿」，**唔用來出新目標價**。

| KPI | 最新官方／可核對數 | 方向 | 點樣郁倍數 | 來源 |
|---|---|---|---|---|
| 現價 | US$629.26 delayed 9/24（9/23 收 614.61） | 急升；RSI 72.5 | 市值 ~US$1.027T | yfinance |
| 暫定規尺（非 target） | TTM P/S **24.9×**；trailing P/E **162×**；官方 FCF yield **0.75%** | 倍數擴張 | F3 pending | 官方 TTM＋市況 |
| 溢價／折讓 | P/S 較 NVDA 17.9×／AVGO 18.8× 貴約 **6–7 圈** | 溢價 | 行動第一句 | yfinance 同業 9/24；官方 TTM 營收 |
| ★ Data Center 已入帳 | US$6,718m，+107% YoY，+16% QoQ，佔季收 58% | 改善 | 決定 P/S 分子增速 | EX-99.1 |
| ★ 總營收／Q3 指引 | Q2 US$11,536m（+50%）；Q3 指引 ~US$13.0B ±0.3B | 改善（指引唔入帳） | 約束分子 | EX-99.1 |
| ★ 官方 FCF | Q2 US$1,558m（OCF 2,366 − capex 808）；margin 14% vs Q1 25% | 惡化（仍正） | 約束 FCF yield | EX-99.1 調節 |
| ★ GAAP／Non-GAAP 毛利率 | GAAP 54%；Non-GAAP 56%；Q3 Non-GAAP 指引 ~56% | 高位持平 | 約束盈利倍數 | EX-99.1 |
| ★ Helios 已入帳收入 | **官方未量化**（Q2 begins to ramp） | 未入帳 | 而家 P/S 已預支呢條 | 8-K；9/8 會議 unverified |

**行動（第一句必須引用溢價／折讓）：** 現價 TTM P/S 約 **24.9×**，較 NVDA 約 17.9×／AVGO 約 18.8× **貴約 6–7 圈** → **僅觀察／唔好加倉**。舊 F3 Bull 620 已過期，唔好把 F1 PASS 當成建倉區或 covered-call 活閘。

### 對 covered-call hold gate 嘅旗標（唔另開 Skill 7）

舊 F3 行動表：減倉／鎖定區 **≥ US$620** 或接近 Bull。現價 **US$629.26 已高過舊 Bull**。同時 RSI（14，自算）9/22 **73.6**、9/23 **70.7**、9/24 **72.5**。呢兩條會觸及**舊圖**嘅持倉／沽 call 閘，但 F3 **過期**，本輪**禁止**用 240／390／620 做 live strike 或新目標價。要等 Framework 3 刷新先可以重畫 hold gate。其他會影響閘位嘅旗標：Helios $ 仍空白、Q2 FCF margin 14% 未修復、PEG 維度已 0 分、Meta 績效認股權證最多 1.60 億股（官方 8-K `0000002488-26-000045`，潛在攤薄）。

## Adversarial check

- **最強支持：** Data Center 單季 US$6,718m、+107% YoY；總營收 US$11,536m、+50%；近三季營收超自身指引、近四季 Non-GAAP EPS beat 共識；現金 4× 債務且 TTM FCF US$7.7B；官方客戶名單（Anthropic 2 GW、OpenAI 6 GW、Meta 6 GW）同 Q3 指引 US$13B 仍然完整。
- **最強反證：** 現價 US$629.26、TTM P/S 24.9×，較 8 月底 F1 用嘅 US$458／約 18× 大幅擴張；Helios 從 7 月 AAI「in production」講到 9 月會議「Q3 開始出貨」，**官方仍然無一美元**；Q2 FCF margin 14%（Q1 25%）、capex 由 US$389m 跳到 US$808m；yfinance PEG 0.63 靠前瞻 EPS US$15.6，等於把未入帳 Helios 預支晒。
- **最可能令結論失效嘅假設：** Q3 營收 miss US$12.7B 指引下限，同時 Helios 再無量化、FCF margin 再滑——24.9× P/S 會一次性壓縮；或者 Instinct ASP／毛利率被 NVDA／客製 ASIC 壓穿 56% 指引。

## 下一步（PASS → Framework 2）

Framework 2 必須深挖嘅兩個問題（承接 08-27，用 9 月事件更新，**唔重跑 F2**）：

1. **Helios／Instinct 收入確認節奏 vs 敘事：** Q2 官方只得「begins to ramp」；9/8 第三方話 Q3 開始有收入、Q4 大級跳。F2 要對住 **Q3 8-K 有冇 Helios 或 Instinct 可核對美元／GW**，而唔好再信會議形容詞。
2. **FCF margin 回落係一次性定結構性：** Q1 25% → Q2 14%，OCF margin 29%→21%，PPE US$389m→US$808m，應收 US$7,281m。要拆工作資本同 Helios 備貨，判斷 14% 會唔會變成新常態。

技術面（次要權重，yfinance delayed 2026-09-24）：收市 US$629.26，9/21–9/24 由 559 抽到 629；RSI 72.5 超買；1 年回報 +291%，大幅跑贏 SPY +17%。價格行為支持「基本面 PASS、估值貴」——**唔抵消**倍數風險。

互動報告：`output/AMD_framework1.html`

*此分析僅供研究參考，不構成投資建議。*
