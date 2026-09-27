# Skill 4：AMD / NVDA / AVGO / MRVL / INTC 同業比較

- **一句話：** AMD 喺組內係 **已入帳 Data Center 增速第二快嘅挑戰者**，但官方路徑估值最貴；市場最易看錯嘅，係用 DC +107% 或 Street FY2027 收入約 US$88B 去證明現價對 F3 Base **+74.8%** 合理，或者把 AMD 24.9× TTM P/S 當成「同 MRVL 一樣貴所以一樣抵買」。
- **數據截至：** 2026-09-27（Asia/Hong_Kong）。最新官方季仍然係各家已公布嘅上一季——**AMD 2026-Q3 尚未公布**（會計期終約 2026-09-26）。
- **焦點組：** NVDA、AVGO、INTC、MRVL（用戶指定）。**唔納入 TSM 做正式排序**：代工鏟子、TIFRS、唔係產品替代倉；本倉 AVGO Skill 4（2026-09-04）已列作可選對照。
- **承接：** F1 PASS 90／130（PR #33）；F2 增長 **通過**、現金流／FCF／稀釋 **部分通過**（PR #34）；F3 **高估**、Bear **US$180**／Base **US$360**／Bull **US$505**（PR #35）；Skill 5 催化劑（PR #36）；Skill 6 Thesis Mixed／Needs Monitoring（PR #37）。**本頁唔另起 Skill 3 模型、唔改目標價。**
- **價格錨（HUD 同 F3／Thesis 一致）：** AMD US$629.26（NASDAQ 2026-09-24 收市；yfinance delayed，America/New_York）。9/25 正式收市 US$630.63、當日 High **US$639.00**（yfinance）；F3 寫過 9/25 delayed 634.76／52 週高 US$638.00——**HUD 現價／溢價 % 仍用 9/24 收市 US$629.26**，避免同已合併頁尺漂移。同業 delayed **9/25 收市**：NVDA US$225.07、AVGO US$352.81、MRVL US$261.94、INTC US$123.00。delayed 唔覆寫官方財務。
- **持倉：** 未確認。排序係研究配置，**唔寫減倉股數**。
- **閘門：** 持倉閘 **應減倉勿賣 put**；買 call 閘 **合理或偏貴**。本輪 **不變**。

## 數據驗證同會計期

官方優先。yfinance 只用於 delayed 現價、市值同 forward P/E **溫度計**。**以下 aggregator 同官方衝突，一律棄用 aggregator：**

| 項目 | yfinance（2026-09-27 拉） | 官方（用邊個） |
|---|---|---|
| AMD 總債 | US$4.28B | 流動長期債＋長期債 **US$3,226m**（Q2 Selected Data；**未計** 8/17 關上嘅 US$4.75B 票據） |
| AMD TTM FCF | US$8.84B | 四季官方 FCF 加總 **US$7,736m** |
| AMD trailing EPS | US$3.93 | GAAP 攤薄 0.75＋0.92＋0.84＋1.38 = **US$3.89** |
| AMD PEG | 0.63（配合 forward EPS ~US$15.57） | 官方 trailing PEG ≈ **3.2**（Helios $ 未量化，前瞻增長不可靠） |
| NVDA TTM FCF | 曾報遠低於官方 | 四季 8-K 加總 **US$126,886m**（本倉 NVDA F1，2026-08-27） |
| AVGO TTM FCF | 曾報遠低於官方 | 四季 EX-99.1 加總 **US$39,403m**（本倉 AVGO F3，2026-09-04） |

財政日曆 **唔對齊**。AMD／INTC 仍係 6 月底日曆季；NVDA 期終 7/26；MRVL 8/1；AVGO 8/2。只可比方向同質量，**唔可硬串成同一季**。

| 公司 | 最新官方季 | 期終 | 申報 | 會計基準 | validation_status |
|---|---|---|---|---|---|
| **AMD** | CY2026-Q2 | 2026-06-27 | 8-K 2026-08-04／10-Q 2026-08-05 | US GAAP／Non-GAAP | verified（本倉 F1–F3） |
| **NVDA** | FY2027-Q2 | 2026-07-26 | 8-K／10-Q 2026-08-26 | US GAAP；Non-GAAP **含 SBC** | verified（本倉 F1／F3，2026-08-27） |
| **AVGO** | FY2026-Q3 | 2026-08-02 | 8-K 2026-09-02；**10-Q 2026-09-09／10** accession `0001730168-26-000080` | US GAAP／Non-GAAP（**剔除 SBC**） | verified（業績稿本倉 F3；10-Q 本輪重讀客戶／Backstop） |
| **MRVL** | FY2027-Q2 | 2026-08-01 | 8-K 2026-08-27；10-Q 2026-08-28 | US GAAP／Non-GAAP | verified（本倉 F1／F3，2026-08-28；Pages 可引） |
| **INTC** | CY2026-Q2 | 2026-06-27 | 8-K EX-99.1 2026-07-23 | US GAAP／Non-GAAP | verified（本輪重讀 Intel IR／EX-99.1）；**本倉無獨立 F1／F3** |

期後官方事件（**唔覆寫**已入帳季度）：

- **AMD：** IR Calendar 2026-09-27 仍寫「There are no upcoming events scheduled」→ Q3 業績日 **未官方確認**（第三方／yfinance 估約 2026-11-03 盤後，`unverified`）。8/17 關上 US$4.75B 高級票據；Meta／OpenAI 認股權證各最多 160m 股。Helios $ **仍然空白**。
- **AVGO：** Q3 10-Q 已申報（舊 AVGO Skill 4 寫 pending，本輪更新）。單一經銷商佔季收 **50%**（上年 32%）；頭五名終端客戶約 **55%**（上年約 40%）。AI rack Backstop 最大潛在負債約 **US$29B**（未折現；未付款）；另有條件可轉換票據上限約 **US$42B**。
- **NVDA：** 8-K 2026-09-03 協議收購 Hugging Face（代價約 US$11.9B，2027 上半年交割，未入帳）。PORTS 擔保上限 US$105B 仍係或有。
- **INTC：** 8-K 2026-08-12 期後增發最多約 2.42 億股、每股 US$95。
- **MRVL：** Google 認股權證（最多約 5,897 萬股）係 Q2 期後事項。

引用本倉 Pages／output（標日期，唔重跑）：

| 公司 | 本倉最新包 | Pages |
|---|---|---|
| AMD | F1–F3／Skill 5／6：2026-09-25 | https://keithcheungmk.github.io/stock-analysis/amd/ |
| NVDA | F1／F3：2026-08-27；Skill 4：2026-08-27 | https://keithcheungmk.github.io/stock-analysis/nvda/ |
| AVGO | 全套至 Skill 9：2026-09-04；F3 Base **355**／Bull **545** | https://keithcheungmk.github.io/stock-analysis/avgo/ |
| MRVL | F1／F3：2026-08-28 | https://keithcheungmk.github.io/stock-analysis/mrvl/ |
| INTC | 無獨立包；數字對住官方 8-K 同 AVGO Skill 4（2026-09-04）交叉 | 無 |

## Decision HUD（沿用 F3，唔另估）

權威：`output/AMD_2026-09-25_framework3.md`（PR #35）。同一現價／Base／溢價 %。

| 欄 | 數 | 來源 |
|---|---|---|
| 現價 | US$629.26 delayed（2026-09-24 收市）；9/25 收 US$630.63、High US$639.00；市值約 US$1.029T | yfinance；普通股約 1,632m；Q2 攤薄 1,659m |
| Bear / Base / Bull | **180 / 360 / 505** | F3 FY2027 公司 Non-GAAP P/E 中心 |
| 溢價／折讓 | 現價對 Base **+74.8%**（高估；已高過 Bull 約 24.6%） | 629.26／360 |
| 估值驅動 KPI | ① 總營收 US$11,536m（+50%）② Data Center US$6,718m（+107%）③ 官方 FCF US$1,558m（14%）④ Non-GAAP GM 56% ⑤ Helios $ **官方未量化** | F2／F3 ★ 列 |

**行動（第一句必須引用溢價／折讓）：** 現價對 Base 約 **+74.8% 溢價**，而且已經高過 Bull US$505 → **僅觀察、唔好建倉、唔好新開賣 put**。Skill 4 證明 AMD **質量排組內第三、估值吸引力最低**，**唔證明**而家係買點。持倉閘 **維持應減倉勿賣 put**；買 call 閘 **維持合理或偏貴**。持倉未確認，唔寫減倉股數。

## 🧭 Peer Group 一句話結論

最大分野係 **平台現金機器 × 已入帳 AI／DC 美元 × 對自身 F3 嘅位置**：NVIDIA Data Center 一季 US$89.0B，仍約係 Broadcom AI 半導體 US$16.7B 嘅 **5.3 倍**、AMD Data Center 嘅 **13 倍**。市場最容易看錯兩點：用 AMD DC +107% 去否定 NVDA +117%——增速接近，但美元增量、75% 毛利同 TTM FCF US$126.9B 仍喺另一個數量級；又把 AMD 官方 TTM P/S **24.9×** 同 MRVL **24.9×** 看成「一樣貴」，忽略咗 delayed 價對**各自 F3 Base** 係 AMD **+74.8%**、MRVL 約 **−3%**、AVGO 約 **−0.6%**、NVDA 約 **−25%**。

## 🧩 可比性判斷

**可以直接比：** AI／Data Center／客製加速器已入帳規模同 YoY；毛利率方向；FCF 是否為正同轉換率方向；客戶／經銷商集中度；現價相對**各自已有 F3 Base** 嘅溢價／折讓；官方 TTM P/S（市值用 delayed、營收用已驗證 TTM）。

**只能參考：** 倍數絕對值（財政年、Non-GAAP 是否含 SBC、產品 mix 全部唔同）。AVGO 市場語言係 **剔除 SBC 嘅公司 Non-GAAP EPS**；NVIDIA 由 FY2027-Q1 起 Non-GAAP **含 SBC**——**唔好把兩家 forward P/E 直接平均**。Intel Foundry 收入含大量內部轉撥。yfinance forward P/E／PEG 只係溫度計。

**不宜硬比：** AMD Instinct／Helios 對 CUDA 通用加速器。AVGO 客製 XPU＋網絡＋VMware 軟件對 AMD 開放 rack。MRVL custom／TPU-attach 未入帳敘事對 AVGO 已入帳 AI US$16.7B。Intel GAAP 單季虧損 US$11.0B 對任何一家 trailing P/E。FCF 定義各異：NVIDIA 官方 FCF 含 PPE／無形資產本金還款；AMD／AVGO 用 OCF−PPE；MRVL 自算 OCF−PPE；Intel 另有「adjusted FCF」（扣政府誘因同 partner contributions）——現金流列只比 **正／負同轉換方向**。

## 🏷️ 角色定位

| 公司 | 賽道角色 | 商業模式 | 市場通常給的估值語言 | 一句話定位 |
|---|---|---|---|---|
| **AMD** | 純種高增長挑戰者 | EPYC CPU ＋ Instinct GPU；Helios 仍在 ramp | Forward P/E、DC 增速、P/S | 增速夠快，規模同現金仍細一個零；現價已高過自身 Bull |
| **NVDA** | 平台型龍頭 | GPU／網絡／CUDA；期後加 Hugging Face（未交割） | Forward P/E（含 SBC 新口徑）、P/S、FCF yield | 唯一百億級季度利潤嘅 AI factory |
| **AVGO** | 綜合型大廠／客製矽平台 | 客製 AI 加速器＋乙太網＋基礎設施軟件 | 公司 Non-GAAP P/E、FCF yield | 超大規模自研 ASIC 嘅最大已入帳贏家；集中度上升 |
| **MRVL** | 轉折股／窄口徑連接＋custom | Data Center 連接／custom silicon；Google warrant | EV/Sales、P/S | 體量最細、槓桿未解；custom 大部分未入帳 |
| **INTC** | 轉折股／復甦期權 | Xeon／Client ＋ 虧損中嘅 foundry | 選擇權、non-GAAP EPS | CPU 復甦已見；GAAP 大虧同期後增發未過關 |

## 📊 同業核心比較表

最新官方季度（曆法唔對齊）。AMD HUD 現價用 9/24；同業 snapshot 用 9/25 收市。

| 公司 | 商業質量 | 增長質量 | 現金流質量 | 估值吸引力 | 最大亮點 | 最大風險 |
|---|---|---|---|---|---|---|
| **AMD** | **中高**：GAAP GM 54%、Non-GAAP 56%；GAAP 營業利潤率 17%、Non-GAAP 27%；GAAP 淨利 US$2.3B（約 20% NM，含投資收益 US$483m） | **高但基數細**：總營收 US$11,536m +50%；DC **US$6,718m +107%**（佔 58%、分部營業利潤 US$2,103m） | **中**：Q2 FCF US$1,558m（收入 **14%**）對 Q1 25% 回落；TTM US$7,736m。Q2 現金＋短投 4.06× 債——**未計** 8/17 票據 | **最低（對自身 F3）**：現價對 Base **+74.8%**，已高過 Bull 約 25% | DC 翻倍；近三季超自身指引；Q3 指引約 US$13B ±0.3B（**未入帳**） | Helios Q2 幾乎未入帳；FCF 14%；Meta／OpenAI 雙 160m 認股權證；CUDA 生態 |
| **NVDA** | **最高**：GAAP／Non-GAAP GM **75.0%**；GAAP 營業利潤率 66.2%；DC US$89.023B | **高（規模）**：總營收 US$96,221m +106%；DC +117%。增速%略快過 AMD DC，美元增量大一個數量級 | **中高**：TTM 官方 FCF US$126.9B；Q2 單季 US$21.341B 對 Q1 US$48.554B 腰斬；應收 US$63.1B | **最高（對自身 F3）**：delayed US$225.07 對 Base US$300 約 **−25%**；F2 現金流仍只部分通過，所以折讓≠即時買點 | 平台＋75% 毛利＋TTM 現金機器 | DSO／PORTS；ASIC 被 AVGO 搶增量；Q3 指引 US$108.0B ±2% 不含中國 DC compute |
| **AVGO** | **高**：GAAP GM 69.1%、營業利潤率 53.9%；軟件 Q3 US$8.752B（+29%）佔 30% | **高**：總營收 +86%；AI 半導體 **US$16.7B、+221%、+54% QoQ** | **高（單季）／中（結構）**：Q3 官方 FCF US$13.665B（收入 46%）；TTM US$39.4B。現金仍只係有息債 **0.40×** | **中（對自身 F3）**：9/25 收 US$352.81 對 Base **355** 約 **−0.6%**，貼住合理 | 組內最快已入帳 AI 線；FCF 轉換高 | Q3 10-Q：經銷商 **50%**、頭五名終端約 **55%**（已到 AVGO 包「≥55%」警戒）；Backstop 約 US$29B |
| **MRVL** | **中**：GAAP GM 53.1%、Non-GAAP 58.9%；GAAP NM 11.2% | **中**：總營收 US$2,739m +37%；DC US$2,171.5m +46%（mix 79%） | **中低**：OCF US$605.5m − PPE US$126.7m → FCF US$478.8m；現金 US$3.93B < 債 US$4.96B（0.79×） | **中（折讓已收窄）**：9/25 收 US$261.94 對自身 F3 Base US$271 約 **−3.3%**（9/3 仲約 −23%） | 六季高過指引中位；DC mix 79% | Distributor A **44%**；Google warrant 稀釋；F1 只係 WATCH 65／130 |
| **INTC** | **低**：GAAP GM **40.4%**（Non-GAAP 41.8%）；GAAP 營業利潤率 11.1%；Foundry 經營虧損 **US$2.089B** | **中（復甦）**：總營收 US$16,128m +25%；DCAI US$6.262B +59% | **低**：Q2 OCF US$7.0B，但公司 adjusted FCF **−US$8.419B**；GAAP 淨虧 **US$11.033B** | **表面低、實際陷阱**：fwd P/E ~60× 無意義；本倉無 F3 | 15 年最快收入增速；Xeon 6 | Foundry 未過關；期後最多約 2.42 億股增發 |

質量排序：**NVDA ≫ AVGO > AMD > MRVL ≫ INTC**  
增長質量（已入帳 AI／DC 線）：**AVGO 增速 > NVDA 規模增長 > AMD DC > INTC DCAI > MRVL DC**  
現金流質量：**AVGO 單季轉換 ≈ NVDA TTM 機器 > AMD > MRVL > INTC**  
估值吸引力（對**自己**已有 F3／官方錨，唔係誰倍數最低）：**NVDA 對自身 Base 折讓最大；AVGO 貼住；MRVL 折讓已幾乎收完；AMD 溢價最大；INTC 便宜係假象**

### 官方規模快照（曆法唔對齊）

| 公司 | 總營收 | YoY | AI／DC 線 | 毛利率 | 營業利益率 | 官方／自算 FCF | DC／AI 曝險 |
|---|---:|---:|---|---|---|---|---|
| AMD | US$11,536m | +50% | DC US$6,718m +107% | GAAP 54%／Non-GAAP 56% | GAAP 17%／Non-GAAP 27% | US$1,558m（14%） | DC 佔季收 **58%** |
| NVDA | US$96,221m | +106% | DC US$89,023m +117% | GAAP 75.0% | GAAP 66.2% | US$21,341m（Q2；TTM 126.9B） | DC 佔季收 **92.5%** |
| AVGO | US$29,591m | +86% | AI 半導體 US$16.7B +221% | GAAP 69.1% | GAAP 53.9% | US$13,665m（46%） | AI 佔季收 **56%**（非 ASC 280） |
| MRVL | US$2,739.3m | +37% | DC US$2,171.5m +46% | GAAP 53.1% | GAAP NM 11.2%（OP 未單列本頁） | US$478.8m（OCF−PPE） | DC 佔季收 **79%** |
| INTC | US$16,128m | +25% | DCAI US$6,262m +59% | GAAP 40.4% | GAAP 11.1%／Non-GAAP 17.2% | OCF US$7.0B；adjusted FCF −US$8.4B | DCAI 佔季收 **39%**（含 CPU） |

所有金額 USD；會計基準見上表。AMD／NVDA／AVGO／MRVL 主列 `verified`。INTC 主列對住 2026-07-23 EX-99.1，`verified`。

### 官方 TTM 倍數（市值用 9/25 delayed；營收／FCF 用已驗證 TTM）

| 公司 | 市值 | 官方 TTM 營收 | TTM P/S | EV/Sales（約） | TTM 官方 FCF | FCF yield | yfinance fwd P/E |
|---|---:|---:|---:|---:|---:|---:|---:|
| **AMD** | US$1.029T | US$41.305B | **24.9×** | **24.7×**（未計 8/17 票據） | US$7,736m | **0.75%** | 40.5×（Street FY27 EPS，**棄用做輸入**） |
| NVDA | US$5.435T | US$302.969B | **17.9×** | **17.8×** | US$126,886m | **2.33%** | 14.4×（含 SBC 新口徑） |
| AVGO | US$1.684T | US$89.104B | **18.9×** | **19.3×** | US$39,403m | **2.34%** | 18.2×（剔 SBC） |
| MRVL | US$235.4B | US$9.451B | **24.9×** | **24.4×** | TTM OCF US$2.20B；唔引用未核對 TTM FCF | Q2 轉換 17.5% | 38.8× |
| INTC | US$650.2B | 約 **US$57.0B**（四季官方稿加總：13.65＋13.67＋13.58＋16.13） | **約 11.4×** | 約 **11.5×** | adjusted FCF 近季為負 | n/m | 59.6×（無意義） |

AMD 官方 TTM P/S 較 NVDA **貴約 7.0 圈（+39%）**、較 AVGO **貴約 6.0 圈（+32%）**，同 MRVL **打平**——但 MRVL 係 WATCH、現金低過債。**倍數接近 ≠ 值博率接近。** EV 用 9/25 市值 ± 各家最新官方現金／有息債；AMD 票據未入 Q2 表，EV/S 略低估槓桿。

現價相對**各自 F3 Base**（研究溫度計，唔另建模型）：

| 公司 | delayed | 本倉 F3 Base | vs Base | F3 日期 |
|---|---:|---:|---:|---|
| **AMD** | 629.26（HUD 9/24） | **360** | **+74.8%** | 2026-09-25 |
| NVDA | 225.07（9/25） | 300 | **約 −25.0%** | 2026-08-27 |
| AVGO | 352.81（9/25） | **355** | **約 −0.6%** | 2026-09-04 |
| MRVL | 261.94（9/25） | 271 | **約 −3.3%** | 2026-08-28 |
| INTC | 123.00（9/25） | 本倉無 F3 | 便宜係假象 | — |

### 稀釋／資本結構（橫向）

| 公司 | 已入帳攤薄 | 或有稀釋／槓桿 | 含義 |
|---|---|---|---|
| **AMD** | Q2 攤薄 1,659m | Meta 認股權證最多 **160m** @ US$0.01（約 9.6%）；OpenAI 另最多 160m（F3 Bull **只計 Meta**）；8/17 票據 US$4.75B | 經營成功反而攤薄；現金 4.06× 快照會過時 |
| NVDA | Q2 攤薄約 24.3B | 回購；PORTS 擔保 US$105B（2028 起，唔係當前債） | 股數趨穩；或有風險喺擔保唔喺認股權證 |
| AVGO | Non-GAAP 攤薄 4,937m | 現金 0.40× 有息債；Backstop 約 US$29B；可轉票據上限約 US$42B | 槓桿＋客戶集中係折讓理由 |
| MRVL | 攤薄導向 921m | Google warrant 最多約 59m（約 6.7%）；現金 0.79× 債 | 同 AMD 一樣「成功即稀釋」，但質量低一截 |
| INTC | Q2 後增發最多約 242m @ US$95 | Foundry 仍燒現金 | 低價買嘅係轉折期權 |

## ⚖️ 誰該享有溢價

- **最值得 higher multiple：NVIDIA。** 75% 毛利、DC 一季 US$89B、TTM 官方 FCF 約 US$127B，係組內唯一「平台溢價」有現金對得住嘅公司。現價對自身 F3 Base 仍約 **−25%**——質量溢價未完全 price in，而唔係「便宜到可以無視 DSO」。
- **AVGO 值得 ASIC／網絡溢價，但唔值得再加「取代 CUDA」一層。** +221% 同 46% FCF 轉換證明客製線係真生意。Q3 10-Q 把頭五名終端推到約 **55%**、單一經銷商 **50%**——集中度惡化，F3 24× 已經畀完溢價。9/25 價對 Base **−0.6%**＝貼住合理，唔係撈底。
- **看似最便宜、折價有理由：Intel。** GAAP 虧 US$11.0B、Foundry 仍燒 US$2.1B、期後 US$95 增發——低價買嘅係轉折期權，唔好當 AI 核心倉，亦唔好用來否定 AMD／NVDA 倍數。
- **MRVL 嘅「平」已經收得七七八八。** 9/3 對自身 Base 約 −23%；9/25 只剩約 **−3%**。WATCH、槓桿、Distributor A 44%、custom 未入帳——剩餘折讓補償嘅係尚未閉合嘅保險絲，唔係「平買 AMD 同級質量」。
- **增速溢價最容易被吹捧：AMD。** DC +107% 係真，但 US$6.7B 配 **+74.8% vs 自身 Base**、官方 TTM P/S 24.9×（貴過 NVDA／AVGO 約 6–7 圈）、FCF yield 0.75%（NVDA／AVGO 約 2.3%）。市場用 40× Street FY2027 EPS 睇落「只係貴一截」，但嗰個平建立喺未入帳 Helios 同約 US$88B 收入之上。F3 Base 只用官方路徑 FY2027 **US$56B**。**溢價不合理。**

## 🥇 投資排序

中線 12–24 個月、以「AI 計算／客製矽曝險」為題、未確認持倉。排序係 **質量＋相對自身估值**，唔係市值大小，亦唔係誰增速最快：

1. **第一名：NVDA** — 質量同規模第一；本倉 F1 PASS 115／130（2026-08-27）。delayed 價對自身 F3 Base 仍有約 25% 折讓，但 DSO／Q2 FCF 裂縫未過關，所以排第一係**質量＋值博率**，唔係「而家追 US$225」。
2. **第二名：AVGO** — 組內最好嘅非 NVIDIA：AI 已入帳增速同單季 FCF 轉換都係第一。F1 PASS 120／130。現價對 **自己** Base 約 −0.6%，合理但上行幾乎係零；Q3 10-Q 集中度升到 55%／50% 令質量扣分，**仍然高過 AMD 嘅單位經濟同現金轉換**。
3. **第三名：AMD** — DC 質變進行中，Helios／Instinct 係進攻型題材；F1 PASS 90／130、F2 增長通過。現價同倍數要求執行零失誤，值博率差過前兩名，亦差過一個月前（當時對舊 Base 只 +17%）。
4. **第四名：MRVL** — 折讓吸引眼球嘅窗口（−23%）已經收窄到約 −3%；WATCH、槓桿同 Distributor A 集中令佢只宜觀察名單。
5. **第五名：INTC** — 只宜觀察。CPU 復甦可以當 NVDA／AMD 主機 CPU 需求嘅旁證，唔好當核心 AI 倉。

## 🎯 配置建議

- **核心持股首選（質量）：** NVIDIA。未確認持倉、F2 現金流只部分通過 → 研究結論同樣係**僅觀察、唔好加倉**，唔係「即時建成核心倉」。
- **進攻型配置首選（題材）：** AMD——**前提**係 Helios／Instinct 美元被 8-K 量化，**而且**現價回到當時重算 Base 附近（F3 建倉觀察區約 US$280–360）。**現價 US$629 唔符合。** 若只想要已入帳 ASIC 進攻倉，AVGO 質量更好，但現價已貼住自身 Base。
- **估值／值博率最佳：** 對各自已有 F3，仍係 **NVDA**（約 −25% vs Base）。AVGO 合理、唔係值博。MRVL 嘅 −3% 唔算值博。AMD **+74.8% 係組內最差值博**。
- **只宜觀察、不宜追高：** **AMD 現價**（對 Base +74.8%、已高過 Bull）；INTC；MRVL（thesis 未驗證且折讓已收）。AVGO 貼住 Base → 同樣僅觀察。
- **若只能選一間長持：** **NVIDIA**。理由：唯一同時通過規模、單位經濟同（TTM）現金機器嘅平台，而且現價相對自身 Base 仍有折讓。AMD 係最好嘅 CPU＋GPU 挑戰者，**唔係平價 NVDA**。AVGO 係最好嘅 ASIC 衛星。MRVL／INTC 分別係轉折同復甦期權。

## 💡 顧問下一步建議

- AMD 已完成 F1／F2／F3／Skill 5／6 → 本包停喺 Skill 4。**唔重做目標價。**
- 同 F3 閘門嘅張力：**無方向衝突**——Skill 4 確認「相對同業亦貴」，支持而唔推翻「應減倉勿賣 put」。若 Q3 8-K 量化 Helios $ 或官方下修路徑，先交 **Skill 3** 重估 Base／Bull，**唔由本頁改尺**。
- 最近改估值中樞嘅官方事件仍係 **2026-Q3 財報**（期終 2026-09-26；公布日以 IR 為準，第三方估 2026-11-03 盤後；黑窗 2026-10-27 至 11-03）。
- 催化劑／Thesis 已完成。臨近 IR 宣布業績日再交 Skill 8。期權結構交 Skill 7。one-pager 交 Skill 9。
- NVDA／AVGO／MRVL 已有本倉 F1／F3，唔為同業比較重跑完整 Framework 2。INTC 唔值得而家開完整 F1，除非用戶要獨立研究倉。
- AVGO Q3 10-Q 集中度同 Backstop 應回寫 AVGO 後續頁；**唔好**用呢兩件事覆寫 AVGO 已入帳季度，亦**唔改** AMD F3。

## 同 F3 閘門對照（本輪唔改）

| 閘 | F3／Skill 6 | Skill 4 之後 | 變咗？ |
|---|---|---|---|
| 持倉閘（covered call） | 應減倉勿賣 put | **維持** | **否** |
| 買 call 閘 | 合理或偏貴 | **維持** | **否** |
| AMD 目標價 | Bear 180／Base 360／Bull 505 | **唔改** | **否** |
| 行動 | 僅觀察、唔好建倉、唔好新開賣 put | **維持** | **否** |

Skill 4 新增嘅係橫向位置：AMD 官方 TTM P/S 貴過 NVDA／AVGO 約 6–7 圈；對自身 Base 溢價係組內最大。呢個係 F3「高估」嘅同業證據，**唔係**另造目標價嘅理由。

## 來源與限制

- **官方、verified：** AMD 2026-Q2 8-K EX-99.1 `0000002488-26-000121`（filed 2026-08-04，期終 2026-06-27，USD，US GAAP／Non-GAAP，unaudited）；10-Q `0000002488-26-000123`。NVDA FY2027-Q2 8-K／10-Q 2026-08-26（本倉 F1）。AVGO FY2026-Q3 8-K EX-99.1 `0001730168-26-000076`；10-Q `0001730168-26-000080`（filed 2026-09-09／10）。MRVL FY2027-Q2 8-K／10-Q 2026-08-27／28（本倉 F1）。INTC CY2026-Q2 EX-99.1 2026-07-23。
- **官方前瞻、未入帳：** AMD Q3 約 US$13.0B ±0.3B；NVDA Q3 約 US$108.0B ±2%；AVGO Q4 約 US$34.8B／AI US$21.7B；各 GW 協議。
- **市況／共識、第三方：** yfinance 2026-09-27 拉（9/24 AMD HUD 錨、9/25 同業收市、市值、fwd P/E）。Street FY2027 AMD 收入約 US$88B／EPS 約 US$15.57 = `unverified` 鏡子。
- **research assumption（沿用 F3，唔新造）：** AMD Base FY2027 收入 US$56B／EPS US$7.63。
- **資料衝突：** aggregator 唔覆寫官方；Street 唔覆寫官方指引；未證實 Helios $ 唔入收入分子。關鍵帳面 **無爭議**——爭議喺「未入帳 Helios 值幾多」，已停用 Street 做輸入，**唔停 verdict**。
- **持倉：** 未確認。
- **raw 正文：** 呢個 cloud checkout 唔提交 `data/raw` 正文。AVGO 10-Q 對住 SEC HTML。catalog 唔塞入持倉 10 隻名單。

## Adversarial Review Memo（交付前閘 · 同日）

- 覆核時間：2026-09-27（Asia/Hong_Kong）
- IR／SEC：AMD IR Calendar **仍然空白**；最新業績包仍係 8/04–8/05。Q3 未公布。AVGO Q3 10-Q **已出**（舊 AVGO 包寫 pending）——本頁已補集中度 55%／50% 同 Backstop 約 US$29B。NVDA／MRVL／INTC 無新一季損益表。
- X：`x_access: degraded`（無 API）。公開第三方日曆：AMD Q3 業績多寫 11/03 盤後。標籤：`unverified` 日期／`confirmed` Q2 數字同 IR 空白。
- Diff：舊 AMD Skill 4（08-27）用舊 F3 240／390／620 同現價 US$458——估值尺 **作廢並替換**。補上 AVGO 全套（Base 355／Bull 545）、NVDA／MRVL Pages 日期、INTC 官方 Q2。無把已發生會議當未來催化。
- Verdict impact：**維持高估／僅觀察**；持倉閘 **維持應減倉勿賣 put**；**唔停** verdict；**唔改** F3 目標價。

*此分析僅供研究參考，不構成投資建議。*
