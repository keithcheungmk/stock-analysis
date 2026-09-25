# AMD Framework 3 估值模型與倉位決策

- **判定結果：** **高估**
- **Base Case 目標價：** **US$360**（合理區間 US$330–390）
- **Bull / Bear 區間：** **US$180–505**（中心情景：Bear US$180／Bull US$505）
- **現價相對 Base：** **+74.8% 溢價**（Decision HUD；US$629.26／US$360）
- **主要價格錨：** US$629.26（NASDAQ 2026-09-24 收市；yfinance delayed，America/New_York）。9/25 delayed 收 US$634.76、當日 High **US$638.00**＝52 週高（yfinance daily High，截至 2026-09-25）
- **市值：** 約 US$1.027T（普通股約 1,632m × 現價；yfinance `sharesOutstanding`／`marketCap`）。Q2 官方攤薄加權 **1,659m**
- **估值期：** FY2027（公司財政年，約 2026-12 至 2027-12）；12 個月目標時點約 2027-09；USD
- **持倉閘（covered call）：** **應減倉勿賣 put** — **已改**（舊閘「僅觀察勿新開」）
- **買 call 閘：** **合理或偏貴**
- **行動：** **僅觀察、唔好建倉、唔好新開賣 put**（持倉未確認，唔寫具體減倉股數）
- **官方驗證：** 2026-Q2 8-K EX-99.1 accession `0000002488-26-000121`，filing date 2026-08-04，USD，US GAAP／Non-GAAP，unaudited，`validation_status: verified`（[EX-99.1](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/q22026991.htm)）。Form 10-Q accession `0000002488-26-000123`，filing date 2026-08-05，`validation_status: verified`（[10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm)）。FY2025 全年 8-K EX-99.1 accession `0000002488-26-000014`，`validation_status: verified`（[q42025991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000014/q42025991.htm)）。Meta 認股權證 8-K accession `0000002488-26-000045`，event date 2026-02-23，`validation_status: verified`（[amd-20260223.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm)）
- **承接：** F1 PASS 90／130（PR #33）；F2 增長 **通過**、現金流／FCF／稀釋 **部分通過**（PR #34）。舊 F3 Bear 240／Base 390／Bull 620（約 2026-09-03）**作廢**
- **持倉：** **未確認**

## 🎯 Framework 3 估值結論

- **判定結果：** 高估
- **Base Case 目標價：** US$360
- **Bull / Bear 區間：** US$180 – US$505
- **現價相對 Base：** **+74.8%**（US$629.26／US$360）
- **估值驅動 KPI（沿用 F2 ★，唔另揀靚數）：**
  1. **總營收** US$11,536m（2026-Q2，+50% YoY）→ 定 FY2026 橋同 FY2027 起點
  2. **Data Center 已入帳** US$6,718m（+107% YoY、佔季收 58%；分部營業利潤 US$2,103m）→ 分拆 Bear／Base／Bull 嘅 DC 桶
  3. **官方 FCF** US$1,558m（OCF 2,366 − capex 808；margin **14%** vs Q1 25%）→ 交叉驗證 FCF yield，約束倍數
  4. **GAAP／Non-GAAP 毛利率** 54%／56%（Q3 Non-GAAP 指引約 56%，**未入帳**）→ 約束 Non-GAAP 淨利率假設
  5. **Helios 已入帳收入** **官方未量化**（Q2「begins to ramp」）→ 禁止把 GW 協議寫進收入分子
- **核心結論：** 上行只喺「Helios／Instinct 美元被 Q3 8-K 量化、而且市場肯繼續畀 50×+ FY2027 P/E」——呢條路徑未證明。最大估值風險係把 Street FY2027 收入約 US$88B／EPS 約 US$15.57（範圍收入 US$61–116B）當成已經官方化；嗰個共識低端已經高過本報告 Base，唔可以當 Base。

現價 US$629.26 對 Base US$360 約 **+74.8% 溢價** → **高估；僅觀察、唔好建倉、唔好新開賣 put**。F1 PASS 同 F2 增長通過證明嘅係質量，唔係買點。持倉未確認。

## 🧠 估值前提

承接 Framework 1／2：

1. **資產類型：** 已大額盈利嘅高增長半導體平台：EPYC 伺服器 CPU ＋ Instinct AI 加速器第二供應商 ＋ Helios rack-scale（未入帳）。適合用 **forward Non-GAAP P/E** 做市場語言，但要用官方 FCF yield 同分部 P/S（SOTP）交叉；唔再係未盈利概念股。
2. **最強質量：** Q2 已入帳營收 US$11,536m（+50%）；Data Center US$6,718m（+107%、佔 58%）；DC 分部營業利潤 US$2,103m（31%）；現金＋短投 US$13,111m／總債 US$3,226m = **4.06×**；TTM 官方 FCF US$7,736m。近三季營收超自身指引中位。
3. **最大裂痕：** Helios rack-scale **官方仍然無一美元**；Q2 FCF margin 14%（Q1 25%），10-Q 寫明約 US$1.0B 供應協議預付 ＋ 應付款項時機；Meta 績效認股權證最多 **1.60 億股**（行使價 US$0.01，潛在攤薄約 9.6%）。9/8、9/11 投資者會議**冇** 8-K 把內容入檔。
4. **官方有、第三方無：** 公司只指引下一季（Q3 約 US$13.0B ±0.3B、Non-GAAP 毛利率約 56%）。CFO 正式講「Data Center sales to accelerate in the second half of 2026」——**官方前瞻，無美元拆**。**冇** FY2026／FY2027 全年指引。Anthropic／OpenAI／Meta GW 協議全部前瞻。第三方 FY2027 收入平均 US$88.1B／EPS US$15.57 屬 `source_tier: unverified`，**唔入模型**。

估值最敏感三個變數（同 F2 交棒）：

1. **FY2027 Data Center 已入帳規模／Helios mix**（唔係 TAM、唔係 GW 意向）：Q2 DC 年化約 US$26.9B；Helios $ 空白，所以 Base 唔把「Q4 大級跳」寫成已發生。
2. **Non-GAAP 淨利率 vs MI450 mix：** Q2 Non-GAAP NM **23.9%**（US$2,760m／US$11,536m）；Q3 毛利率指引 56% 持平。9/8 unverified 口述「2027 毛利率略低過 Q3 指引」只當裂縫線索，**唔改**官方 Q2 錨。
3. **攤薄股數（Meta 認股權證）：** 官方攤薄 1,659m 唔係終局。成功（Bull）反而攤薄更多。

## 📏 估值方法選擇

### 主估值方法：FY2027 公司 Non-GAAP P/E

- AMD 已大額盈利，市場交易語言係 **Non-GAAP diluted EPS**（業績稿主列；Q2 US$1.66 vs GAAP US$1.38）。
- 用 **FY2027** 而唔只用 FY2026：H1 已入帳 US$21,789m ＋ Q3 官方指引約 US$13.0B 已經把「今年」收窄到研究橋約 US$48B——現價約 **83× Street 今年 EPS US$7.58**，真正在交易嘅係明年 Helios／Instinct 能否由未量化變成數十億美元。
- 本模型 Non-GAAP EPS 定義為：**FY2027 研究收入 × Non-GAAP 淨利率 ÷ 預計攤薄加權平均股數**。Non-GAAP 口徑跟公司 EX-99.1：剔除股票薪酬、收購無形資產攤銷、收購相關成本、法律或有損失、長期投資損益、權益法收益、以及 Non-GAAP 稅項調整。Q2 已剔除長期投資收益 US$483m。
- GAAP 淨利可用作交叉，但投資收益同攤銷令 GAAP EPS 系統性扭 Semi 週期，唔單獨做主錨。

### 輔助驗證：分部 SOTP（P/S）＋ 官方 FCF yield

- 三分部：Data Center（高增長 AI＋CPU）、Client + Gaming（周期）、Embedded。唔好用單一公司 P/S 掩蓋 DC mix。
- 官方 TTM FCF US$7,736m／市值 US$1.027T → FCF yield 約 **0.75%**（Price/FCF 約 133×）。FCF 定義跟各季 EX-99.1 footnote 3：GAAP 持續經營 OCF − 購置 PPE。
- 企業價值：市值 US$1.027T ＋ 總債 US$3.226B − 現金＋短投 US$13.111B ≈ **US$1.017T**；官方 TTM 營收 US$41.305B → EV/S 約 **24.6×**。
- 情景 FCF margin 刻意 **低過或等於** TTM 18.7%，避免把 Q1 25% 當成永久結構（Q2 已返 14%）。

### 不採用

- **完整 DCF：** Helios 未量化、Q2 供應預付／應付時機主導 WC，terminal 假設會主導答案，現階段假精確。
- **單一 trailing GAAP P/E：** 官方 TTM GAAP EPS US$3.89、現價約 **162×**，反映唔到 Q3 指引同 FY2027 DC run-rate。
- **把 Street FY2027 收入／EPS 當模型輸入：** yfinance 平均收入 US$88.1B（低 US$61.3B／高 US$116.1B；約 50 位）同 EPS US$15.57（低 US$9.60／高 US$20.25）。低端已經高過本報告 Base 收入 US$56B。只作 **市場隱含預期鏡子**，唔覆寫官方。
- **分析員目標價：** 平均約 US$617／中位 US$616（50 位）——接近現價同舊 Bull 620，**唔當估值**。
- **未證實 Helios／GW 美元：** Anthropic 2 GW、OpenAI 6 GW、Meta 6 GW 全部前瞻 IR。9/8、9/11 會議內容無 8-K，`unverified`，禁止做收入驅動。

## 官方錨（verified）vs 研究橋（非指引）

單位：USD million（另有標示除外）。會計基準：US GAAP／公司 Non-GAAP。貨幣：USD。

| 項目 | 數字 | 財政期 | 來源 | validation_status |
|---|---:|---|---|---|
| 總營收 | 11,536 | 2026-Q2 期終 2026-06-27 | 8-K EX-99.1 | verified |
| Data Center／Client+Gaming／Embedded | 6,718／3,841／977 | 同上 | 分部表 | verified |
| GAAP／Non-GAAP 攤薄 EPS | 1.38／1.66 | 同上 | 業績稿主表 | verified |
| GAAP／Non-GAAP 淨利 | 2,297／2,760 | 同上 | 同上 | verified |
| 基本／攤薄加權股數 | 1,632m／1,659m | 同上 | 簡明損益 | verified |
| H1 營收／攤薄股數 | 21,789／1,655m | 2026 首兩季 | 同上 | verified |
| 官方 FCF | 1,558（OCF 2,366 − PPE 808） | Q2 | 調節表 footnote 3 | verified |
| H1 官方 FCF | 4,124 | 2026 首兩季 | 同上 | verified |
| GAAP／Non-GAAP 毛利率 | 54%／56% | Q2 | 簡明損益／調節 | verified |
| Non-GAAP 營業／淨利率 | 27%／23.9% | Q2 | 調節／自算（2,760／11,536） | verified／derived |
| 現金＋短投／總債 | 13,111／3,226 | 2026-06-27 | Selected Corporate Data | verified |
| 應收淨額 | 7,281 | 2026-06-27 | 資產負債表 | verified |
| Q3 營收指引 | 約 13,000 ±300（+41% YoY、+13% QoQ） | 2026-Q3 | 業績稿 outlook | 官方前瞻，**未入帳** |
| Q3 Non-GAAP 毛利率指引 | 約 56% | 同上 | outlook | 官方前瞻，無 GAAP 對照 |
| FY2025 營收／Non-GAAP EPS | 34,639／4.17 | FY2025 期終 2025-12-27 | Q4'25 EX-99.1 | verified |
| FY2025 Data Center | 16,600 | FY2025 | 同上 Lisa Su／分部評論 | verified |
| TTM 營收／GAAP 淨利／官方 FCF | 41,305／6,434／7,736 | Q3'25–Q2'26 | 四季 EX-99.1 加總 | verified |
| TTM GAAP EPS | 3.89（0.75+0.92+0.84+1.38） | 同上 | 四季攤薄 EPS 加總 | verified |
| TTM Non-GAAP EPS | 5.76（1.20+1.53+1.37+1.66） | 同上 | 四季 Non-GAAP EPS 加總 | verified |
| Meta 認股權證 | 最多 160m 股 @ US$0.01 | 2026-02-23 | 8-K Item 1.01 | verified |
| 現價／普通股／市值 | 629.26／1,632m／約 1.027T | 2026-09-24 收市 | yfinance delayed | 市況，第三方 |
| 52 週高 | **638.00**（當日 High） | **2026-09-25** | yfinance daily High | 市況，第三方 |

**FY2026 近官方橋（研究加總，非公司全年指引）：** H1 已入帳 US$21,789m ＋ Q3 指引中位 US$13.0B = **US$34.8B** 先至第三季。Q4 **冇**官方數字。Base 用 Q4 US$13.6B（較 Q3 中位 +4.6% QoQ，承認 H2 DC 加速呢句官方前瞻，但**唔用** Street Q4 約 US$16.1B 同 unverified「Q4 大級跳」）：FY2026 Base ≈ **US$48.4B**（+40% vs FY2025 US$34.6B）。Street FY2026 收入平均 US$50.9B／EPS US$7.58 **高過**呢條官方橋——差距幾乎全部喺未指引嘅 Q4。

## Street 共識快照（第三方，只作鏡子）

| 財政年度 | 收入共識 | YoY | Non-GAAP EPS 共識 | YoY | 來源／狀態 |
|---|---:|---:|---:|---:|---|
| FY2026（0y） | US$50.9B（48.3–52.7） | 約 +47% | US$7.58（7.00–8.20） | 約 +82% | yfinance，2026-09-25；49 位 |
| FY2027（+1y） | US$88.1B（**61.3–116.1**） | 約 +73% | US$15.57（9.60–20.25） | 約 +106% | 同上；50 位 |
| Q3（0q） | US$13.00B（12.1–14.0） | 約 +41% | US$1.93（1.72–2.03） | 約 +60% | 同官方 Q3 營收指引中位對齊 |
| Q4（+1q） | US$16.11B（13.3–17.8） | 約 +57% | US$2.65（1.93–3.22） | 約 +73% | **無官方 Q4 指引** |

yfinance forward P/E 40.8× 用 forwardEps US$15.57（≈Street FY2027）。分析員目標價平均 US$617 **只係情緒交叉**。yfinance trailing EPS US$3.93、PEG 0.63、總債 US$4.28B、TTM FCF US$8.84B：**繼續棄用**（F1 已表列衝突）。

## 📊 Bull / Base / Bear 情景表

每個情景都由 **官方能見到嘅桶** 砌：Data Center 已入帳 ＋ Client + Gaming ＋ Embedded。**禁止**用 GW 意向、Helios 簡報、Street US$88B 填空。FY2027 全年數字係研究假設，**唔係公司指引**。

| 情景 | 核心經營假設 | 估值方法 | 倍數／參數 | 目標價 |
|---|---|---|---|---:|
| **Bear（30%）** | Q3 miss US$12.7B 下限或 Helios 再無 $；DC 增速回落到 Q2 年化附近不再加速；FCF margin ≤14% 且應付回落；GAAP GM 跌穿 52%。FY2026 橋約 US$46.0B。FY2027：**DC US$27.5B** ＋ C+G US$14.8B ＋ Embedded US$3.7B = 收入 **US$46.0B**（約持平 vs FY2026 Bear）。Non-GAAP NM **20.5%**。攤薄股數 **1.684B**（SBC +25m；認股權證 **0**，因為出貨里程碑未達）。FCF 約 **US$5.5B**（12% margin）。 | FY2027 Non-GAAP P/E | **32×**；遠期 P/S 約 6.6×；SOTP 交叉約 US$175 | **US$180**；區間 US$150–210 |
| **Base（50%）** | Q3 按指引中位附近入帳（≥US$12.7B），Q4 只係溫和順增（**唔假設** Street Q4 US$16.1B）；Helios 開始有收入但 8-K **仍未**量化到足以改分子；FCF margin 回升到 16% 但仍低過 TTM 18.7%。FY2026 橋約 US$48.4B。FY2027：**DC US$35.5B**（約 +26% vs FY2026 DC 橋 ~US$28.3B）＋ C+G US$16.2B ＋ Embedded US$4.3B = 收入 **US$56.0B**（約 +16% vs FY2026 Base）。Non-GAAP NM **23.5%**（略低過 Q2 23.9%，預留 MI450 mix）。股數 **1.724B**（SBC +25m ＋ **研究假設**第一 GW 歸屬約 40m；官方**未披露**首檔股數）。FCF 約 **US$9.0B**（16% margin）。 | FY2027 Non-GAAP P/E | **47×**；遠期 P/S 約 11.0×；SOTP 交叉約 US$309 | **US$360**；區間 US$330–390 |
| **Bull（20%）** | Q3 貼近上限、Q4 Helios／Instinct **首次**被 8-K 量化；DC 再加速但收入 **仍然低過** Street 平均 US$88B；FCF margin 回到約 20%；Meta 認股權證因出貨成功而大幅歸屬。FY2026 橋約 US$50.3B。FY2027：**DC US$46.0B** ＋ C+G US$17.5B ＋ Embedded US$4.5B = 收入 **US$68.0B**（約 +35% vs FY2026 Bull；約 +21% vs Street FY2027 低端 US$61B，**低過**平均 US$88B）。Non-GAAP NM **25.0%**。股數 **1.844B**（SBC +25m ＋ **全數 160m** 認股權證）。FCF 約 **US$13.6B**（20% margin）。 | FY2027 Non-GAAP P/E | **55×**；遠期 P/S 約 13.8×；SOTP 交叉約 US$418 | **US$505**；區間 US$460–550 |

財務橋接：

| 情景 | FY27 收入 | 其中 DC | NM | 股數 | Non-GAAP EPS | FCF | P/E | 中心價 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Bear | US$46.0B | US$27.5B | 20.5% | 1.684B | **US$5.60** | US$5.5B | 32× | **US$180** |
| Base | US$56.0B | US$35.5B | 23.5% | 1.724B | **US$7.63** | US$9.0B | 47× | **US$360** |
| Bull | US$68.0B | US$46.0B | 25.0% | 1.844B | **US$9.22** | US$13.6B | 55× | **US$505** |

EPS = 收入 × NM ÷ 預計攤薄加權平均股數。Base 未捨入：US$56.0B × 23.5% ÷ 1.724B = US$7.633；× 47 = US$358.8 → **中心 US$360**（五美元捨入）。Bear：US$46.0B × 20.5% ÷ 1.684B = US$5.600；× 32 = US$179.2 → **US$180**。Bull：US$68.0B × 25.0% ÷ 1.844B = US$9.219；× 55 = US$507.0 → **US$505**（寧願唔向上加）。

### 股數同 Meta 認股權證（必須分開標）

| 層 | 股數 | 來源 | validation_status |
|---|---:|---|---|
| Q2 基本／攤薄 | 1,632m／1,659m | 8-K 簡明損益 | verified |
| 12 個月 SBC 漂移 | +25m → 1,684m | 研究；Q2'25 攤薄 1,630m → Q2'26 1,659m（+29m／年） | derived |
| 第一 GW 歸屬（Base） | **+40m** → 1,724m | **研究假設**。8-K 只寫「first tranche vests upon shipment of the initial 1 GW」；**未披露**首檔股數（Exhibit 4.1 有 redact） | research assumption |
| 滿 6 GW（Bull） | +160m → 1,844m | 官方上限 160m @ US$0.01；另有股價門檻，最後一檔至 **US$600** | 上限 verified；歸屬時機前瞻 |
| 對照 Q2 攤薄 | 160／1,659 ≈ **9.6%** | F1／F2 已標 | derived |

現價 US$629.26 **已經高過**最後一檔股價門檻 US$600——價格條件可能已接近或達成，但歸屬仍要出貨／採購里程碑同「technical and commercial conditions」。Bull 經營成功 **必須**把 160m 算入，唔可以一面把 Helios 寫成爆發、一面用 1,659m 股。

### 倍數理據

- 現價若用 Street FY2027 EPS US$15.57 → **40.4×**；用本報告 Base EPS US$7.63 → **82.5×**。同一股價對應兩套完全唔同嘅盈利假設——F3 嘅工作就係揀邊套有官方錨。
- Base **47×** 留喺「高增長半導體」走廊上沿：承認 DC +107% 同 23%+ 淨利率，但扣 F2 未閉合嘅 Helios $、FCF 14%、9.6% 認股權證。唔用 55–70× 官方路徑 EPS，除非 Helios 美元同 FCF margin 先通過 F2 確認測試。
- Bear **32×** 仍係成長股倍數，唔係周期股 15×——即使 Helios 延遲，EPYC／已入帳 Instinct 仍然喺損益表。
- Bull **55×** 需要重新評級（第二供應商溢價），仍然遠低過而家 82× 官方路徑。Bull 嘅 US$505 係 **經營上修＋倍數上修一齊發生、再扣滿額認股權證** 先合理。
- FCF 交叉：現價 TTM yield **0.75%**。Base 目標市值約 US$360 × 1.724B ≈ US$621B，配 FCF US$9.0B → yield 約 **1.4%**，仍然貴，但比而家 0.75% 誠實一截。
- SOTP 交叉（DC 12×／C+G 4.5×／Embedded 5.5× ＋淨現金）：Base 約 **US$309**，低過 P/E 中心 US$360——P/E 已經多給咗增長溢價。Bull SOTP 約 US$418，低過 P/E US$505。

概率加權中心：

`30% × 180 + 50% × 360 + 20% × 505 = US$335`

呢個只係情景期望值，唔代表價格會線性走到 US$335。對現價約 **−46.8%**。

### 相對舊 F3（240／390／620）點樣改

| | 舊 F3（約 9/03，現價 US$458） | 今次（9/25，現價 US$629.26） | 點解唔照抄 |
|---|---:|---:|---|
| Bear | 240 | **180** | 認股權證同 FCF 14% 寫入；舊 Bear 對 $458 只 −48%，對而家 $629 會假裝仲有緩衝 |
| Base | 390 | **360** | 官方路徑 EPS 只有約 US$7.6，唔係 Street US$15.6；股數 1.62B → 1.72B |
| Bull | 620 | **505** | Bull 要扣滿額 160m；舊 US$1.0T／1.62B 未計稀釋。現價已穿舊 Bull |

舊 F3 內部仲有 SOTP 表約 US$416B vs Base 市值 US$630B 嘅裂縫。今次主錨改用可重現 P/E 橋，SOTP 只交叉。**唔因為股價由 458 升到 629 就上修 Base。** Q2 帳面同一個季度。

## 🪞 市場隱含預期

用正式收市 **US$629.26**、Base 攤薄股數 1.724B：

- 官方 TTM P/S：**24.9×**（US$1.027T／US$41.305B）。FY2026 橋約 US$48.4B → 約 **21.2×**。FY2027 若做到 Base US$56B → 約 **18.3×**。
- Street FY2026 Non-GAAP P/E：約 **83×**（629.26／7.58）。Street FY2027：約 **40.4×**（629.26／15.57）。yfinance forwardPE 40.8×。
- TTM Non-GAAP P/E：約 **109×**（629.26／5.76）。TTM GAAP P/E：約 **162×**。
- **若市場畀本報告 Base 47×：** 現價隱含 FY2027 EPS 約 **US$13.39**，即 Non-GAAP 淨利約 US$23.1B。套 Base NM 23.5%，隱含收入約 **US$98B**——接近 Street 平均 US$88B 嘅上修版，**遠高過**本報告 Base US$56B，亦高過 Street 低端 US$61B。
- **若市場畀 Street 40.4×：** 隱含 EPS 約 **US$15.57**、淨利約 US$26.8B。套 25% NM 要收入約 **US$107B**，接近 Street 高位 US$116B。呢條路徑 **冇官方全年指引**，而且要把 Helios／14 GW 意向大量入帳。
- **若市場長期只畀 47× 而收入做到 Base US$56B：** 隱含 EPS US$13.39 對唔上 US$7.63——即要 NM 去到 41% 先圓，或者股數大幅收縮。兩者都唔係 8-K 基線。更合理讀法：市場用 40× 係因為佢哋假設嘅 EPS 已經係 US$15+，**唔係**因為佢哋覺得官方路徑值得 40×。
- 分析員目標價平均 US$617 已經**低過**現價，亦接近舊 Bull 620。現價高過 Street target **唔等於**更便宜——target 用咗我哋拒絕做輸入嘅 FY2027 共識，仍然追唔上呢段由 US$458 到 US$629 嘅升幅。

**市場有冇過度 price in 樂觀敘事？** 對 **Base（官方路徑 FY2027 US$56B／EPS US$7.63）**：**是，溢價約 75%。** 對 **Street 平均（收入 +73% 到 US$88B）**：現價用 40× 看起來「只係貴一截」，但嗰個平係建立喺未入帳 Helios 之上。F3 唔把後者當成已經發生。9/16–9/25 由 US$512 抽到 US$635、並喺 9/25 印 52 週高 US$638，比較像倍數擴張，而唔係 Q2 之後有新嘅已入帳美元。

## ⚖️ 風險回報分析

由 US$629.26 正式收市計：

| 情景 | 中心價 | vs 收市 |
|---|---:|---:|
| Bear | US$180 | **−71.4%** |
| Base | US$360 | **−42.8%** |
| Bull | US$505 | **−19.7%** |
| 概率加權 | US$335 | **−46.8%** |

Base upside／Bear downside 中心約 **負**（要跌 43% 先返到 Base）。即使只睇 Bull，現價仍然**高過 Bull 約 24.6%**。Reward／Risk **唔吸引**。

**目前更像「質量高但價格已超過 Bull」。** 值搏率極差。好公司 ≠ 好買點。唔因為 F1 90／130 或 DC +107% 就忽略 R/R。

最大下行唔係少 5 圈倍數，而係 FY2027 EPS 由 US$7.63 跌向 US$5.60 **同時** P/E 壓到 32×（Bear 中心 US$180；下沿 US$150 約 −76%）。觸發器：Q3 明顯低過 US$12.7B，或 Helios 再無 $ 兼 FCF margin 再 ≤14%。

## 🚪 持倉閘（covered call）同買 call 閘

### 持倉閘：**應減倉勿賣 put**（**已改**）

舊閘（F1／F2／舊 F3 行動）：**僅觀察勿新開**。  
新閘：**應減倉勿賣 put**。

| | 舊 | 新 | 變咗？ |
|---|---|---|---|
| 持倉閘 | 僅觀察勿新開 | **應減倉勿賣 put** | **是** |
| 買 call 閘 | （舊 F3 未單列；隱含偏貴） | **合理或偏貴** | 維持偏貴側 |

改閘原因（全部要同時成立先維持新閘）：

1. 現價 US$629.26 對新 Base **+74.8%**，而且已經**高過新 Bull US$505 約 24.6%**——舊圖「Base–Bull 之間先觀察」呢條帶已經被穿。
2. 現價亦已穿舊 Bull US$620；52 週高 **US$638.00（2026-09-25）** 幾乎就係而家呢段。
3. Helios $ 仍空白、Q2 FCF margin 14% 未修復——倍數擴張冇新嘅已入帳美元支撐。
4. 新開賣 put ＝喺高過 Bull 嘅位置加槓桿做多；covered call 若只為「續抱收息」會把僅餘嘅（已經係負嘅）Bull 上行再 cap 掉。閘嘅主動作係**減倉／唔再加長倉**，唔係 overwrite 續抱。

三檔定義（本報告沿用）：

| 閘 | 何時用 | 期權含義 |
|---|---|---|
| 續抱可賣 | 現價 ≤ Base，而且 F2 增長通過、FCF 未失效 | 可續抱；covered call strike 用 Bull／52w 高做參考 |
| 僅觀察勿新開 | Base < 現價 < Bull，或質量裂縫未閉 | 唔好新開 covered call／賣 put |
| 應減倉勿賣 put | 現價 ≥ Bull，或對 Base 溢價過大 | 模型建議減倉；**禁止**賣 put；唔好為收息而新開 call 去「續抱」 |

**Strike 參考（唔構成 Skill 7 建議）：** Base **US$360**（2026-09-25 F3）；Bull **US$505**（2026-09-25 F3）；52 週高 **US$638.00**（2026-09-25，yfinance daily High）。期權結構交 Skill 7。

### 買 call 閘：**合理或偏貴**

- **嚴重低估：** 現價對 Base 折讓足夠大、而且 Helios／FCF 確認——**不符合**。
- **合理或偏貴：** 現價對 Base +75%、高過 Bull——**符合（偏貴／高估）**。
- **資料不足：** 關鍵數爭議要停 verdict——**不符合**。Helios $ 空白係估值扣減，唔係「冇足夠資料做閘」。Q2 帳面、Q3 指引、認股權證條款都有官方錨。

## 🧭 倉位與價格策略

用戶 **未確認 AMD 持倉**。以下係研究價格區，**唔係**對未知倉位嘅加倉／減倉股數指令。持倉閘「應減倉勿賣 put」係模型政策；未確認前只准觀察。

| 價格區 | 研究動作 | 必要條件 |
|---|---|---|
| **≤ US$280** | 深度觀察；價格本身唔自動觸發買入 | 先確認無 F2 失效（Q3 ≥US$12.7B 或有 Helios $、FCF 仍正、DSO 未爆）。若只係市場錯殺而確認測試過，先討論細注研究倉 |
| **US$280–360** | 較佳 **建倉觀察區**（靠近／低過 Base） | **全部** F2 確認先由觀察轉建倉：Q3 ≥US$12.7B；8-K 至少量化 Helios 或 Instinct 美元／GW；官方 FCF margin ≥18%；自算 DSO ≤58 |
| **US$360–505** | **僅觀察** | Base–Bull 帶。而家 **唔喺**呢條帶（現價已高過 Bull） |
| **≥ US$505（含現價 US$629）** | Bull 已大致／過度 price in | 要見到 FY2027 官方路徑升向 US$68B 兼 Helios $ 入帳，先討論係咪重估。模型持倉閘：**應減倉勿賣 put** |

- **分批框架（若用戶之後確認要建倉）：** 三段約 US$360／300／230。每段要重查 Helios $、官方 FCF、認股權證歸屬，唔以價格單獨觸發。US$230 只容許喺無失效而屬錯殺時建立小型研究倉。
- **倉位上限（研究，非經紀指令）：** 未確認持倉 → 新資金權重 **0**。若日後確認持倉：現價高過 Bull 時，模型建議把研究權重收斂到 **0–0.5 個單位**（唔發明股數）；只有現價回到 Base 以下且 F2 確認，先討論 1 個單位。
- **加倉條件（只係未來持倉框架）：** Q3 已入帳 ≥US$12.7B、Helios 或 Instinct 至少一條官方美元、FCF margin ≥18%、DSO ≤58，**而且**現價相對當時重算 Base 仍有 ≥15% 折讓。未確認前維持「唔好加倉」。
- **減倉／止賺模型（只喺日後確認持倉先適用）：** 現價已高過 Bull US$505。模型政策係先減；高過 52 週高 US$638 而 Helios 仍無 $，餘倉另做完整 position review。呢個係模型政策，**唔係即時指令**。
- **Thesis invalidation：** （a）Q3 營收明顯低過 US$12.7B，或管理層把差額歸因 Helios／Instinct 延後而無 EPYC 補上；（b）Q3 8-K **仍然**無 Helios／Instinct 可核對美元，同時把量產再推去 Q4／2027；（c）官方 FCF margin ≤14% **而且**應付較 Q2 回落超過約 US$1B，或單季 FCF 轉負；（d）DC YoY < +40% 且 GAAP 毛利率跌穿 52%，或 Meta／OpenAI／Anthropic 其中一條官方 GW 協議被修訂／取消。任一觸發就要同時下修盈利 **同** multiple。
- **技術輔助（唔凌駕估值）：** 9/24 收 US$629.26；9/25 delayed 收 US$634.76、High US$638.00（52 週高）。9/16–9/25 由 US$512 抽到 US$635。RSI（F1 自算，9/24）72.5 超買。52 週低約 US$155–157（2025-09-25 附近）。現價印新高 **唔構成**獨立買點。

## 💡 顧問下一步建議

**僅觀察、唔好建倉、唔好新開賣 put。** 現價對 Base 約 **+74.8% 溢價**，而且已經高過 Bull 約 25%。Base 上行係負數、Bear 下行約 71%，值搏率唔吸引。持倉閘由「僅觀察勿新開」**改為「應減倉勿賣 put」**；買 call 閘 **合理或偏貴**。最可能改估值中樞嘅下一件事係 **2026-Q3 財報**（期終約 2026-09-26；yfinance 估 2026-11-03，**未見官方確認日期**）：營收會唔會 ≥US$12.7B、8-K 會唔會首次量化 Helios 或 Instinct 美元、官方 FCF margin 會唔會 ≥18%。在此之前，F1 PASS／F2 增長通過 **唔構成** 建倉，亦唔構成 covered-call 續抱閘。

互動頁：`docs/amd/framework3.html`；估值卡（官方錨 → 滑桿 → 重算）：`docs/amd/valuation.html`。卡片只係 F3 展示層，預設 = 本報告 Base／Bull／Bear，**唔另起一套倍數**。

期權進場或收益增強交 **Skill 7**；同業相對估值交 **Skill 4**。本 PR 停喺 Framework 3。

## 來源與限制

- **官方、verified：** AMD 2026-Q2 8-K EX-99.1（期終 2026-06-27；filed 2026-08-04；accession `0000002488-26-000121`；USD；US GAAP／Non-GAAP；unaudited）。Form 10-Q accession `0000002488-26-000123`。FY2025 EX-99.1 accession `0000002488-26-000014`。Meta 認股權證 8-K `0000002488-26-000045`。FCF = 持續經營 OCF − PPE。
- **官方前瞻、未入帳：** Q3 2026 營收約 US$13.0B ±0.3B、Non-GAAP 毛利率約 56%；CFO「H2 Data Center sales accelerate」；Anthropic／OpenAI／Meta GW 協議。
- **research assumption：** Base 第一 GW 歸屬 40m 股（官方未披露首檔股數）；FY2027 收入／NM／倍數。
- **市況／共識、第三方：** yfinance（擷取 2026-09-25；9/24 收市作 HUD 錨、9/25 delayed、52 週高、EPS／收入估計、目標價）。**棄用** yfinance 過期／衝突 TTM FCF、總債、trailing EPS US$3.93、PEG 0.63。
- **資料衝突處理：** aggregator 唔覆寫官方 Q2 數字；Street FY2027 唔覆寫官方 Q3 指引；未證實 Helios $ 唔入情景收入。
- **估值情景：** FY2027 收入、EPS、FCF、倍數係研究假設。關鍵數（Q2 帳面 vs Street）**無爭議**——爭議喺「未入帳 Helios 值幾多」，已停用 Street 做輸入，**唔停 verdict**。
- **持倉：** 未確認。
- **raw 正文：** 呢個 cloud checkout 冇 `data/raw/AMD` 全文；數字對住 SEC HTML。catalog `pending_sources: 0`。唔提交 raw 正文。

*此分析僅供研究參考，不構成投資建議。*
