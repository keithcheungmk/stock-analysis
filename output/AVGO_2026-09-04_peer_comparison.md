# Skill 4：AVGO / NVDA / AMD / MRVL（＋TSM／INTC）同業比較

- **一句話：** Broadcom 而家係組內 **AI 增速同單季 FCF 轉換最好嘅非 NVIDIA**，但 NVIDIA 仍然係唯一百億級季度利潤平台；市場最易看錯嘅，係把 AVGO AI +221% 當成已經可以平替 CUDA 現金機器，或者把「AVGO 比 NVDA 貴少少嘅 TTM P/S」當成 AVGO 更抵買。
- **數據截至：** 2026-09-04（Asia/Hong_Kong）。AVGO 用 FY2026-Q3（期終 2026-08-02）8-K EX-99.1 accession `0001730168-26-000076`，filing 2026-09-02，USD，US GAAP／Non-GAAP，unaudited，`validation_status: verified`（業績稿）。**FY2026-Q3 Form 10-Q 截至 2026-09-04 仍未申報。**
- **承接：** F1 PASS 120／130；F2 增長 **通過**、現金流 **部分通過**；F3 Base **US$355**，現價對 Base **+0.6% 溢價**，**僅觀察**（PR #26 已 squash-merge 入 `main`，`e224413`）。本頁 **唔另起 Skill 3 模型**。
- **價格錨（HUD 同 F3 一致）：** AVGO US$357.16（NASDAQ 2026-09-03 收市；yfinance delayed，America/New_York）。同業 delayed 收市同一日：NVDA US$228.45、AMD US$456.16、MRVL US$208.83、TSM US$417.01、INTC US$91.67。delayed 唔覆寫官方財務。
- **持倉：** 未確認 AVGO 持倉。排序係研究配置，唔係買賣指令。

## 數據驗證同會計期

官方優先。yfinance 只用於 delayed 現價、市值同 forward P/E **溫度計**。**以下 aggregator 同官方衝突，一律棄用 aggregator：**

| 項目 | yfinance（2026-09-04 拉） | 官方（用邊個） |
|---|---|---|
| AVGO TTM FCF | US$27.2B | 四季 EX-99.1 加總 **US$39,403m** |
| NVDA TTM FCF | US$41.8B | 四季 8-K 加總 **US$126,886m** |
| AVGO 最近季增速 | 曾停留喺 Q2 +47.9%（F1 已棄） | Q3 FY26 **+86% YoY** |

財政日曆 **唔對齊**。AVGO／NVDA／MRVL 期終集中喺 7 月底至 8 月初；AMD／TSM／INTC 仍係 6 月底日曆季。只可比方向同質量，**唔可硬串成同一季**。

| 公司 | 最新官方季 | 期終 | 申報 | 會計基準 | validation_status |
|---|---|---|---|---|---|
| **AVGO** | FY2026-Q3 | 2026-08-02 | 8-K 2026-09-02 | US GAAP／Non-GAAP | verified（10-Q pending） |
| **NVDA** | FY2027-Q2 | 2026-07-26 | 8-K／10-Q 2026-08-26 | US GAAP；Non-GAAP **含 SBC** | verified（本倉 F1） |
| **MRVL** | FY2027-Q2 | 2026-08-01 | 8-K 2026-08-27；**10-Q 2026-08-28 已申報** | US GAAP／Non-GAAP | verified（本輪覆核 10-Q 客戶表） |
| **AMD** | CY2026-Q2 | 2026-06-27 | 8-K 2026-08-04／10-Q 2026-08-05 | US GAAP／Non-GAAP | verified（本倉 F1） |
| **TSM** | CY2026-Q2 | 2026-06-30 | 6-K EX-99.1 2026-07-16 | **TIFRS**；另報 USD | verified（本輪重讀 EX-99.1） |
| **INTC** | CY2026-Q2 | 2026-06-27 | 8-K EX-99.1 2026-07-23 | US GAAP／Non-GAAP | verified（本輪重讀 EX-99.1） |

期後官方事件（**唔覆寫**已入帳季度）：

- **NVDA** 8-K Item 8.01（filing 2026-09-03，accession `0001045810-26-000078`）：2026-09-02 簽訂協議收購 Hugging Face；對股東代價約 **US$11.9B**，另設最多約 **US$1.0B** 員工留任股權；預期 **2027 上半年**交割，須監管批准。NVIDIA 承諾維持平台開放，並繼續支援其他矽供應商。
- **INTC** 8-K（filing 2026-08-12）：2026-08-10 承銷協議發行 **210,526,315** 股普通股、每股 **US$95**；包銷商 2026-08-11 全數行使額外 **31,578,947** 股。呢筆係 Q2 期後稀釋，唔入 Q2 簡明表。
- **TSM** 6-K（2026-08-10）：**2026 年 7 月**合併營收約 **NT$467.58B**（較 6 月 +5.6%、較 2025 年 7 月 +44.7%）。呢個係月報，**唔當**新一季 GAAP／TIFRS 對照。
- **AMD** 8-K（2026-08-19）：委任董事，唔改財務表。
- **MRVL** Google 認股權證仍係 2026-08-18／19 期後事項（F1 已記）；Q2 10-Q 確認 Distributor A 佔淨營收 **44%**（上年同期 34%）、Direct Customer A **16%**。

舊 NVDA Skill 4 用過「TSMC HPC 佔營收 66%」。本輪重讀 TSMC EX-99.1 **冇**印出 HPC 平台佔比（簡報圖表擷取唔到）→ **唔沿用**。改用 EX-99.1 已印：**7nm 及更先進製程佔晶圓營收 77%**。Intel 毛利率用官方 GAAP **40.4%**／Non-GAAP **41.8%**（舊 NVDA 同業表把 41.8% 寫成 GAAP，本輪更正）。

## Decision HUD（沿用 F3，唔另估）

權威：`output/AVGO_2026-09-04_framework3.md`。同一截止日、同一現價／Base／溢價 %。

| 欄 | 數 | 來源 |
|---|---|---|
| 現價 | US$357.16 delayed（2026-09-03 收市）；市值約 US$1.699T | yfinance；普通股約 4,758m |
| Bear / Base / Bull | **205 / 355 / 545** | F3 FY2027 公司 Non-GAAP P/E 中心 |
| 溢價／折讓 | 現價對 Base **+0.6%**（持平） | 357.16／355 |
| 估值驅動 KPI | ① 總營收 US$29,591m（+86%）② AI 半導體 US$16.7B（+221%、+54% QoQ）③ 官方 FCF US$13,665m（收入 46%）④ GAAP 毛利率 69.1% ⑤ 應收 US$13,707m／自算 DSO ~42 日 | F2／F3 ★ 列 |

**行動（第一句必須引用溢價／折讓）：** 現價對 Base 約 **+0.6% 溢價** → **僅觀察、唔好建倉**。Skill 4 證明 AVGO 質量排組內第二，**唔證明**而家係買點。

## 🧭 Peer Group 一句話結論

最大分野係 **平台規模 × 現金機器 × 客製矽增速**：NVIDIA Data Center 一季 US$89.0B，仍約係 Broadcom AI 半導體 US$16.7B 嘅 **5.3 倍**、AMD Data Center 嘅 **13 倍**。市場最容易看錯嘅地方，係用 AVGO +221% 或 AMD DC +107% 去否定 NVIDIA +117%——增速輸咗，但美元增量、75% 毛利同 TTM FCF US$126.9B 仍然喺另一個數量級；另一邊，把 AVGO 官方 TTM P/S 19.1× 同 NVDA 18.2× 看成「差不多貴」，忽略咗 AVGO 已經 **貼住自己 F3 Base**，而 NVDA delayed 價對自身 F3 Base US$300 仍有約 **24% 折讓**。

## 🧩 可比性判斷

**可以直接比：** AI／Data Center／客製加速器已入帳規模同 YoY；毛利率方向；FCF 是否為正同轉換率方向；客戶／經銷商集中度；現價相對**各自已有 F3 Base** 嘅溢價／折讓。

**只能參考：** 倍數絕對值（財政年、Non-GAAP 是否含 SBC、產品 mix 全部唔同）。AVGO 市場語言係 **剔除 SBC 嘅公司 Non-GAAP EPS**；NVIDIA 由 FY2027-Q1 起 Non-GAAP **含 SBC**——**唔好把兩家 forward P/E 直接平均**。TSMC 用 TIFRS；Intel Foundry 收入含大量內部轉撥。

**不宜硬比：** TSMC 代工毛利 67.7% 對 NVIDIA 賣系統／GPU 毛利 75%，或對 AVGO 客製 XPU＋網絡＋VMware 軟件。AMD Instinct／Helios 對 CUDA 通用加速器。MRVL custom／TPU-attach 未入帳敘事對 AVGO 已入帳 AI US$16.7B。Intel GAAP 單季虧損 US$11.0B 對任何一家嘅 trailing P/E。FCF 定義各異：NVIDIA 官方 FCF 含 PPE／無形資產本金還款；AMD 用 capex；Broadcom 自列 FCF＝OCF−PPE；Intel 另有「adjusted FCF」（扣政府誘因同 partner contributions）——現金流列只比 **正／負同轉換方向**。

## 🏷️ 角色定位

| 公司 | 賽道角色 | 商業模式 | 市場通常給的估值語言 | 一句話定位 |
|---|---|---|---|---|
| **AVGO** | 綜合型大廠／客製矽平台 | 客製 AI 加速器＋乙太網交換／連接＋基礎設施軟件（VMware 等） | 公司 Non-GAAP P/E、EV/EBITDA、FCF yield | 超大規模自研 ASIC 嘅最大已入帳贏家；軟件做緩衝 |
| **NVDA** | 平台型龍頭 | GPU／網絡／CUDA；期後加 Hugging Face 開放模型社群（未交割） | Forward P/E（含 SBC 新口徑）、P/S、FCF yield | 唯一百億級季度利潤嘅 AI factory |
| **AMD** | 純種高增長挑戰者 | EPYC CPU ＋ Instinct GPU；Helios 仍在 ramp | Forward P/E、DC 增速 | 增速夠快，規模同現金仍細一個零 |
| **MRVL** | 轉折股／窄口徑連接＋custom | Data Center 連接／custom silicon；Google warrant 期後稀釋 | EV/Sales、P/S | 體量最細、槓桿未解；custom 大部分未入帳 |
| **TSM**（可選對照） | 重資產製造／鏟子 | 先進製程代工（TIFRS） | P/E、先進製程 mix、capex | AI 供應瓶頸，兩邊通食，唔係產品替代倉 |
| **INTC**（可選對照） | 轉折股 | Xeon／Client ＋ 虧損中嘅 foundry | 選擇權、non-GAAP EPS | CPU 復甦已見；GAAP 大虧同期後增發未過關 |

## 📊 同業核心比較表

最新官方季度（曆法唔對齊）。現價除註明外為 2026-09-03 yfinance delayed。

| 公司 | 商業質量 | 增長質量 | 現金流質量 | 估值吸引力 | 最大亮點 | 最大風險 |
|---|---|---|---|---|---|---|
| **AVGO** | **高**：GAAP GM 69.1%、營業利潤率 53.9%；軟件 Q3 US$8.752B（+29%）佔 30% | **高**：總營收 +86%；AI 半導體 **US$16.7B、+221%、+54% QoQ**（beat 上季指引 US$16.0B） | **高（單季）／中（結構）**：Q3 官方 FCF US$13.665B（收入 46%）；TTM US$39.4B。現金仍只係有息債 **0.40×** | **中（對自身 F3）**：現價對 Base **+0.6%**，合理但唔平 | 組內最快已入帳 AI 線；FCF 轉換高；非 AI 半導體約 US$4.1B 持平證明增量幾乎全係 AI | 客製客戶集中（Q2 10-Q 頭五名終端 ~45%、單一經銷商 42%）；Q3 10-Q 未出；紅線 1 保險絲仍裸露 |
| **NVDA** | **最高**：GAAP／Non-GAAP GM **75.0%**；DC US$89.023B | **高（規模）**：總營收 US$96.221B +106%；DC +117%。增速%輸 AVGO，美元增量仍大一個數量級 | **中高**：TTM 官方 FCF US$126.9B；Q2 單季 US$21.341B 對 Q1 US$48.554B 腰斬；應收 US$63.1B | **中高（對自身 F3）**：delayed US$228.45 對 Base US$300 約 **−24% 折讓**；F2 現金流仍只部分通過，所以折讓≠即時買點 | 平台＋75% 毛利＋TTM 現金機器；期後 Hugging Face 協議加強軟件層 | DSO／PORTS；ASIC 被 AVGO 搶增量；Q3 指引 US$108.0B ±2% 不含中國 DC compute |
| **AMD** | **中高**：GAAP GM 54%、Non-GAAP 56%；GAAP 淨利 US$2.3B（約 20% NM） | **高但基數細**：總營收 US$11.536B +50%；DC **US$6.718B +107%** | **中**：Q2 FCF US$1,558m（收入 14%）對 Q1 US$2,566m（25%）回落；現金＋短投 US$13.1B > 債 US$3.2B | **低**：delayed US$456.16 對自身 F3 Base US$390 約 **+17% 溢價** | DC 翻倍；Q3 指引約 US$13B ±0.3B（+41% YoY） | Helios Q2 幾乎未入帳；Gaming 線下滑；CUDA 生態 |
| **MRVL** | **中**：GAAP GM 53.1%、Non-GAAP 58.9%；GAAP NM 11.2% | **中**：總營收 US$2.739B +37%；DC US$2,171.5m +46%（mix 79%） | **中低**：OCF US$605.5m − PPE US$126.7m → FCF US$478.8m；現金 US$3.93B < 債 US$4.96B（0.79×） | **表面中、質量折價**：delayed US$208.83 對自身 F3 Base US$271 約 **−23%**；折讓有理由（WATCH 65／130、槓桿、custom 未入帳） | 六季高過指引中位；Q3 指引中位 US$3.15B | Distributor A **44%**；Google warrant 稀釋；紅線 1 保險絲同 AVGO 同類但現金機器細兩個零 |
| **TSM** | **高（代工）**：TIFRS GM **67.7%**、營業利潤率 60.3%、淨利率 55.6% | **中**：USD 營收 US$40.20B +33.7%；先進製程佔晶圓營收 **77%** | **中高**：Q2 capex NT$496.0B（EX-99.2）；仍係經營現金機器，但重資產。本報告唔用 yfinance 新台幣 FCF | **中**：fwd P/E ~19× 只係溫度計；本倉無 TSM F3 | Q3 指引 **US$44.6–45.8B**；7 月月報 NT$467.58B +44.7% YoY | 地緣；產能過建；唔係 NVDA／AVGO 產品替代 |
| **INTC** | **低**：GAAP GM **40.4%**（Non-GAAP 41.8%）；Foundry 經營虧損 **US$2.089B** | **中（復甦）**：總營收 US$16.128B +25%；DCAI US$6.262B +59% | **低**：Q2 OCF US$7.0B，但公司 adjusted FCF **−US$8.419B**（partner contributions）；GAAP 淨虧 **US$11.033B**（含 Escrowed Shares 公允價值） | **表面低、實際陷阱**：fwd P/E ~45× 無意義；期後 US$95 增發 | 15 年最快收入增速；Xeon 6 | Foundry 未過關；期後最多約 2.42 億股增發 |

質量排序：**NVDA ≫ AVGO ≈ TSM > AMD > MRVL ≫ INTC**  
增長質量（已入帳 AI／DC 線）：**AVGO 增速 > NVDA 規模增長 > AMD DC > INTC DCAI > MRVL DC > TSM 代工斜率**  
現金流質量：**AVGO 單季轉換 ≈ NVDA TTM 機器 > TSM（代工現金）> AMD > MRVL > INTC**  
估值吸引力（對**自己**已有 F3／官方錨，唔係誰倍數最低）：**NVDA 對自身 Base 折讓最大；MRVL 折讓有結構理由；AVGO 持平；AMD 溢價；INTC 便宜係假象**

### 官方規模快照（曆法唔對齊）

| 公司 | 總營收 | YoY | AI／DC／先進製程線 | 毛利率 | 官方／自算 FCF |
|---|---:|---:|---|---|---|
| AVGO | US$29,591m | +86% | AI 半導體 US$16.7B +221% | GAAP 69.1% | US$13,665m（46% of sales） |
| NVDA | US$96,221m | +106% | DC US$89,023m +117% | GAAP 75.0% | US$21,341m（Q2；TTM 126.9B） |
| AMD | US$11,536m | +50% | DC US$6,718m +107% | GAAP 54% | US$1,558m（14%） |
| MRVL | US$2,739.3m | +37% | DC US$2,171.5m +46% | GAAP 53.1% | US$478.8m（OCF−PPE） |
| TSM | US$40.20B／NT$1,270.38B | +33.7% USD／+36.0% NT$ | 先進製程 77% of wafer rev | TIFRS 67.7% | 重 capex；唔引用未核對 USD FCF |
| INTC | US$16,128m | +25% | DCAI US$6,262m +59% | GAAP 40.4% | OCF US$7.0B；adjusted FCF −US$8.4B |

官方 TTM P/S（市值用 9/03 delayed；營收用已驗證 TTM，**唔用** yfinance TTM）：AVGO **19.1×**（US$1.699T／US$89.104B）；NVDA **18.2×**（US$5.516T／US$302.969B）；MRVL **19.9×**（US$187.7B／US$9.451B）。三個倍數接近，**質量差好遠**——呢個就係市場最易看錯嘅地方。

現價相對**各自 F3 Base**（研究溫度計，唔另建模型）：

| 公司 | delayed 9/03 | 本倉 F3 Base | vs Base |
|---|---:|---:|---:|
| AVGO | 357.16 | **355** | **+0.6%** |
| NVDA | 228.45 | 300（錨價曾用 8/26 收市 209.66） | **約 −24%** |
| AMD | 456.16 | 390 | **約 +17%** |
| MRVL | 208.83 | 271（錨價曾用 8/28 嘅 241.45） | **約 −23%** |

## ⚖️ 誰該享有溢價

- **最值得 higher multiple：NVIDIA。** 75% 毛利、DC 一季 US$89B、TTM 官方 FCF 約 US$127B，係組內唯一「平台溢價」有現金對得住嘅公司。期後 Hugging Face 協議（約 US$11.9B，2027 H1 先交割）加強軟件／社群層，但 NVIDIA **承諾繼續支援其他矽供應商**——所以呢筆收購 **唔等於**封殺 AVGO，亦唔好當成已入帳協同。NVDA 自身 F3 Base 仍用 24× FY2028 normalized EPS。現價對該 Base 仍折讓，係質量溢價未完全 price in，而唔係「便宜到可以無視 DSO」。
- **AVGO 值得 ASIC／網絡溢價，但唔值得再加一層「取代 CUDA」溢價。** +221% 同 46% FCF 轉換證明客製線係真嘅已入帳生意；VMware 等軟件提供緩衝。F3 已經用 24× FY2027 公司 Non-GAAP EPS 畀咗高盈利複合增長走廊中間——現價 **+0.6%** 表示呢層溢價 **已經畀完**。再追，係在買 Street FY2027 平均收入 US$173B 嗰條 **未有官方全年指引** 嘅加速。
- **看似最便宜、折價有理由：Intel，其次係 MRVL。** Intel GAAP 虧 US$11.0B、Foundry 仍燒 US$2.1B、期後 US$95 增發——低價買嘅係轉折期權。MRVL delayed 價對自身 Base 有約 23% 折讓，但現金低過債、Distributor A 44%、custom 未入帳，F1 只係 WATCH；折讓補償嘅係尚未閉合嘅紅線保險絲，唔係「平買 AVGO 同級質量」。
- **增速溢價最容易被吹捧：AMD，以及把 AVGO AI +221% 外推成 FY2027 TAM。** AMD DC +107% 係真，但 US$6.7B 配 +17% vs 自身 Base，係用挑戰者故事買現在。AVGO 第三方 FY2027／FY2028 AI 約 US$115B／US$230B 屬 `unverified`，F3 已拒絕做輸入——Skill 4 同樣拒絕。

## 🥇 投資排序

中線 12–24 個月、以「AI 計算／客製矽曝險」為題、未確認持倉。排序係 **質量＋相對自身估值**，唔係市值大小，亦唔係誰增速最快：

1. **第一名：NVDA** — 質量同規模第一；F1 PASS 115／130、F2 增長通過。delayed 價對自身 F3 Base 仍有約 24% 折讓，但 DSO／Q2 FCF 裂縫未過關，所以排第一係**質量＋值博率**，唔係「而家追 US$228」。
2. **第二名：AVGO** — 組內最好嘅非 NVIDIA：AI 已入帳增速同單季 FCF 轉換都係第一。F1 120／130、F2 增長通過。現價對 **自己** Base +0.6%，所以上行幾乎係零——排第二係質量，**唔係買點**。
3. **第三名：TSM** — 鏟子邏輯最乾淨，Q3 指引 US$44.6–45.8B；代價係 capex、地緣同會計基準唔同。唔好當成 AVGO／NVDA 替代倉。
4. **第四名：AMD** — DC 質變進行中，Helios／Instinct 係進攻型題材；現價同倍數要求執行零失誤，值博率差過前三。
5. **第五名：MRVL** — 折讓吸引眼球，但 WATCH、槓桿同 Distributor A 集中令佢只宜觀察名單。
6. **第六名：INTC** — 只宜觀察。CPU 復甦可以當 NVDA／AMD 主機 CPU 需求嘅旁證，唔好當核心 AI 倉。

## 🎯 配置建議

- **核心持股首選（質量）：** NVIDIA。未確認持倉、F2 現金流只部分通過 → 研究結論同樣係**僅觀察、唔好加倉**，唔係「即時建成核心倉」。
- **進攻型配置首選：** Broadcom（押客製 ASIC＋AI 網絡份額）。前提係價格先離開「已反映 Base」——F3 建倉觀察區大約 US$250–300，而且要 F2 確認（Q4 AI ≥US$20B、官方 FCF ≥US$10B、DSO ≤48、頭五名 ≤50%）。**現價 US$357 唔符合。**
- **估值／值博率最佳：** 對各自已有 F3，仍係 **NVDA**（delayed 約 −24% vs Base）。AVGO 係合理、唔係值博。MRVL 嘅 −23% 唔算值博，因為質量同槓桿配唔上。
- **只宜觀察、不宜追高：** AVGO 現價（對 Base +0.6%）；AMD（對 Base +17%）；Intel；MRVL（thesis 未驗證）。
- **若只能選一間長持：** **NVIDIA**。理由：唯一同時通過規模、單位經濟同（TTM）現金機器嘅平台，而且現價相對自身 Base 仍有折讓。AVGO 係最好嘅 ASIC 衛星，唔係「平價 NVDA」。TSM 係供應鏈。AMD／MRVL／INTC 分別係挑戰者、轉折、復甦期權。

## 💡 顧問下一步建議

- AVGO 已完成 F1／F2／F3 → 本包停喺 Skill 4。**唔重做目標價。** 最近改估值中樞嘅官方事件仍係 **FY2026-Q4 財報**（期終 2026-11-01；Q4 指引總營收約 US$34.8B、AI 半導體 US$21.7B **未入帳**）同遲來嘅 **Q3 10-Q**（保理／客戶集中）。
- 催化劑日曆或財報預覽交 **Skill 5／Skill 8**（用戶未點名，本輪唔寫）。
- NVDA／AMD／MRVL 已有本倉 F1／F3，唔為同業比較重跑完整 Framework 2。TSM／INTC 唔值得而家各自開完整 F1，除非用戶要獨立研究倉。
- 把 Hugging Face 協議同 Intel 增發寫入後續 NVDA／INTC 頁嘅期後事項即可；**唔好**用呢兩件事覆寫任何一家已入帳季度。

*此分析僅供研究參考，不構成投資建議。*
