# NVDA Framework 3 估值模型與倉位決策

- **判定結果：** **低估（對 Base、暫定）**；財報後 Street 共識仍在更新，唔可以把低 forward P/E 當無條件便宜
- **Base Case 目標價：** **US$300**（合理區間 US$275–330）
- **Bull / Bear 區間：** **US$152–510**（中心情景：Bear US$170／Bull US$450）
- **主要價格錨：** US$209.66（NASDAQ 2026-08-26 收市；yfinance／StockAnalysis 第三方市場數據）
- **盤前敏感度：** US$222.90（StockAnalysis，2026-08-27 07:19 EDT，盤前、可快速變動，唔當正式收市）
- **估值期：** FY2028（公司52／53週財政日曆預計期終 2028-01-30；aggregator 常用 2028-01-31 月底標籤）；USD
- **行動：** **等待確認／唔好追盤前升幅**；無確認持倉，唔提供減倉指令
- **官方驗證：** FY2026-Q1 至 FY2027-Q2 共 6 個 raw manifests 驗證通過；最新 FY2027-Q2 為 USD、US GAAP、unaudited，SEC 8-K／10-Q filed 2026-08-26

## 🎯 Framework 3 估值結論

NVDA 喺 US$209.66 只係約 **23.2× FY2027**、**16.0× FY2028** 第三方 adjusted EPS 共識，表面上相對 +83%／+44% 收入增長預期偏平；但呢個折讓其實係市場對三件事打折：FY2028 共識分散、ASIC／自研晶片搶增量，以及應收／PORTS 把 NVIDIA 由賣晶片商推向客戶融資同基建擔保。Base 用低過 Street FY2028 收入／EPS 嘅假設，仍然得出約 US$300，對收市有約 43% 空間。

不過，Q2 財報出咗不足一日：yfinance 季度收入共識 US$104.4B 仲低過公司最新 Q3 指引 US$108.0B，顯示部分 feed 未收齊。盤前 US$222.90 已經把 Base 上行收窄到約 35%，而 F2 要求嘅 DSO ≤55 日、FCF ≥US$30B、Rubin 毛利率 ≥73.5% 尚未驗證。因此研究判定係「對 Base 低估」，行動仍係等待確認／唔追價，唔把 analyst target 當估值。

## 🧠 估值前提

承接 Framework 1／2：

1. **資產類型：** 高盈利、超高增長、週期風險逐步上升嘅 AI compute 平台；唔再係未盈利概念股，適合用 forward adjusted P/E，但要用 FCF 同 EV/Sales 交叉。
2. **最強質量：** FY2027-Q2 Data Center US$89.0B（+117% YoY）；五季 Data Center US$41.1B → US$89.0B；GAAP 毛利率 75.0%、營業利潤率 66.2%；Rubin 已 full production。
3. **最大裂痕：** DSO 45 → 60 日、應收 US$63.1B；Q2 FCF US$21.3B 對 Q1 US$48.6B 腰斬；五個直接客戶佔應收 70%。AVGO AI 半導體 +143% 快過 NVDA DC +117%。
4. **或有風險：** PORTS／SB Energy 擔保 cap US$105B（連其他土地／電力／殼擔保毛風險 US$108.5B），OpenAI 為租戶，首期預計 FY2029 生效；唔係當前有息債務，但會影響合理倍數。

估值最敏感三個變數：

1. **FY2028 normalized EPS：** Street「adjusted」約 US$13.04–13.13，但 yfinance 51 位分析員範圍約 US$9.65–19.10，分歧極大；第三方未證明同公司新 non-GAAP 口徑完全一致，所以本模型自建可重現 normalized EPS。
2. **Rubin 毛利率：** 公司 FY2027-Q3 指引 74.0% ±50bps；低過 73.5% 兼再下修會直接壓 EPS 同 multiple。
3. **FCF 轉換／DSO：** TTM FCF US$126.9B 係硬數字，但 Q2 單季轉換斷裂；延長 90 日至一年付款條款若常態化，P/E「便宜」未必等於現金便宜。

## 📏 估值方法選擇

### 主估值方法：FY2028 normalized P/E

- NVIDIA 已大額盈利，P/E 係市場最常用、亦最易同成長預期連結嘅語言。
- 用 FY2028 而唔只用 FY2027，因為 FY2027 已過兩季，現價主要交易 Rubin 同下一財年盈利。
- 本模型 normalized EPS 定義為：**收入 × normalized net margin ÷ 預計攤薄加權平均股數**。Normalized net margin 以公司 FY2027 新 non-GAAP 口徑為起點：包括 stock-based compensation，剔除股本證券收益及公司列明嘅 acquisition-related／other adjustments。呢個係研究口徑，唔聲稱同 Yahoo／StockAnalysis「adjusted EPS」完全一致。
- 公司由 FY2027-Q1 起 non-GAAP **不再剔除 stock-based compensation**，較舊年度 non-GAAP 已重列。GAAP 淨利受股本證券未實現收益扭曲，唔單獨做主錨。

### 輔助驗證：官方 FCF yield＋forward EV/Sales

- 官方 TTM FCF US$126.886B／市值約 US$5.08T → FCF yield 約 **2.5%**（Price/FCF 約 40×）。
- 只用官方流動性 US$56.586B、官方有息債務 US$33.366B校準，當前 EV／官方 TTM 收入約 **16.7×**；唔用 yfinance 過期收入計出嘅 19.9×。
- 情景 FCF margin 刻意低過／接近 TTM 41.9%，避免把 Q1 提前收款同股本投資收益誤當永久結構。

### 不採用

- **完整 DCF：** AI capex 週期、90日至一年賬期、US$279B供應承諾同PORTS擔保令 terminal／working-capital 假設主導答案，現階段會製造假精確。
- **單一 trailing P/E：** 官方 TTM GAAP約26.4×，但包含大額股本證券收益，亦無法反映 FY2028 Rubin。
- **analyst target price：** 只作市場情緒交叉，唔係估值輸入。

## Street 共識快照（第三方，財報後未完全穩定）

| 財政年度 | 收入共識 | YoY | 第三方 adjusted EPS | YoY | 來源／狀態 |
|---|---:|---:|---:|---:|---|
| FY2027 | US$395.7–397.0B | 約 +83% | US$9.02–9.05 | 約 +89% | StockAnalysis／yfinance，2026-08-27；49–54位 EPS 分析員 |
| FY2028 | US$570.0–573.6B | 約 +44% | US$13.04–13.13 | 約 +45% | 同上；51位 EPS／55位收入分析員；範圍極闊 |

兩個來源年度中位接近，但 yfinance FY2027-Q3 收入共識仍約 US$104.4B，低過公司 8月26日最新官方指引 US$108.0B ±2%，所以本報告標 **post-earnings refresh pending**。官方只指引下一季，冇指引 FY2027／FY2028全年 EPS；全年數全部係第三方估算。

## 📊 Bull / Base / Bear 情景

| 情景 | FY2028 核心經營假設（研究假設，非公司指引） | 財務橋接 | 估值方法 | 倍數／交叉驗證 | 目標價 |
|---|---|---|---|---|---:|
| **Bear（30%）** | 收入約 US$450B；Rubin 增長明顯低過 Street；GAAP GM 70–72%；ASIC／自研搶增量；DSO ≥60、PORTS風險溢價上升 | Normalized NI約US$242B（53.8% margin）÷24.2B預計攤薄加權平均股數 = EPS **US$10.0**；FCF約 **US$125B**（27.8% margin） | FY2028 normalized P/E | **17×**；約9.1× P/S；目標 FCF yield 約3.0% | **US$170**；區間US$152–189（EPS US$9.5–10.5 × 16–18×） |
| **Base（50%）** | 收入約 US$550B（略低過Street）；Rubin正常導入；GM 73–75%；中國收入唔作必要前提；DSO回落、FCF恢復但低過TTM margin | Normalized NI約US$300B（54.5% margin）÷24.0B預計攤薄加權平均股數 = EPS **US$12.5**；FCF約 **US$190B**（34.5% margin） | FY2028 normalized P/E | **24×**；約13.1× P/S；目標 FCF yield 約2.6% | **US$300**；區間US$275–330（EPS US$12.5–13.2 × 22–25×） |
| **Bull（20%）** | 收入約 US$650B；Rubin／networking超預期；GM 75–76%；ACIE分散客戶；ASIC只食部分TAM，PORTS不觸發 | Normalized NI約US$357B（54.9% margin）÷23.8B預計攤薄加權平均股數 = EPS **US$15.0**；FCF約 **US$250B**（38.5% margin） | FY2028 normalized P/E | **30×**；約16.5× P/S；目標 FCF yield 約2.3% | **US$450**；區間US$420–510（EPS US$15–17 × 28–30×） |

財務橋接由收入開始，先套 normalized net margin，再除預計攤薄加權平均股數；FCF 另外用 FCF margin 估。Net margin 53.8–54.9%低過 FY2027-H1 公司新口徑 non-GAAP 約56%，反映規模放慢、稅率同競爭，避免 EPS 只靠倍數「生出嚟」。股數假設由 Bear 24.2B、Base 24.0B、Bull 23.8B，反映回購但唔假設大幅縮股。

### 倍數理據

- Motley Fool 2026-06-13 引述 2026年 forward P/E 主要走廊約 **18–25×**；Yahoo Finance 2026-08-25／26 財報前約24×，並指出2023–2025經常高過40×。樣本係第三方圖表／報道，唔係完整逐日自算歷史，故只作倍數語境，唔當精準 percentile。
- yfinance 同日 peer forward P/E：AVGO約18.2×、TSM約19.2×、AMD約31.1×、INTC約43.3×；財政期、產品mix同數據口徑唔一致，只可校準，唔可直接平均。
- Bear 17× 係跌穿2026主要走廊；Base 24× 留喺走廊上端，反映平台質量但扣除應收／擔保；Bull 30× 需要重新評級，仍低過2023–2025常見40×以上敘事倍數。

概率加權中心：

`30% × 170 + 50% × 300 + 20% × 450 = US$291`

呢個只係情景期望值，唔代表價格會線性走到 US$291。

## 🪞 市場隱含預期

### 用正式收市 US$209.66

- FY2027 adjusted P/E：約 **23.2×**（EPS約US$9.03）
- FY2028 adjusted P/E：約 **16.0×**（EPS約US$13.08）
- 若市場畀 Base 24×，現價隱含 FY2028 EPS 約 **US$8.74**，即 normalized NI約US$210B。套本報告 Base normalized net margin 54.5%，隱含收入約 **US$385B**，只比官方TTM US$303B高約27%，低過本報告 Base US$550B。
- 若收入真係做到 Base US$550B而市場畀24×，現價反而隱含 normalized net margin約 **38%**，遠低過本報告Base 54.5%同FY2027-H1公司新口徑non-GAAP約56%。
- 若市場長期只畀18×，現價隱含 EPS約 **US$11.65**、normalized NI約US$280B；對US$550B收入即約51% net margin。即市場可以係假設業務大致做到，但NVDA永久去評級，唔一定只係EPS大幅下修。

### 用盤前 US$222.90（只作敏感度）

- FY2027／FY2028 adjusted P/E約 **24.7×／17.0×**
- Base 上行由43%收窄至約35%；Bear中心下行由19%擴到24%。
- 用戶提供嘅第三方卡曾顯示US$225.66；盤前價快速變動，唔應用一個截圖取代正式價格錨。

市場唔係單純「漏咗計增長」。佢實際 price in：（1）FY2028共識會下修；（2）超高增長不能維持；（3）GPU同ASIC/XPU份額趨向接近；（4）供應承諾、應收同擔保會吞掉一部分現金質量。要rerate，唔係再一次 beat 就夠，而係 DSO／FCF同Rubin margin一齊通過。

## ⚖️ 風險回報分析

由 US$209.66 正式收市計：

| 情景 | 中心價 | vs 收市 |
|---|---:|---:|
| Bear | US$170 | **−18.9%** |
| Base | US$300 | **+43.1%** |
| Bull | US$450 | **+114.6%** |
| 概率加權 | US$291 | **+38.8%** |

由 US$222.90 盤前計：Bear −23.7%、Base +34.6%、Bull +101.9%、概率加權 +30.6%。

對正式收市，Base upside／Bear downside 中心約 **2.3×**，數學上吸引；但 Bear 下沿 US$152 代表約 −27%，盤前追入會擴闊至約 −32%。最大風險唔係倍數少2圈，而係 FY2028 EPS由US$13附近跌向US$10，同時P/E壓到16–18×。

## 🧭 倉位與價格策略

用戶未確認 NVDA 持倉，以下係研究價格區，唔假設要加／減現有倉：

| 價格區 | 研究動作 | 必要條件 |
|---|---|---|
| **≤ US$180** | 深度觀察；唔由價格自動觸發買入 | 先確認無任何F2失效條件；若未有新財報，只可等事件／分小注研究倉，唔可以見平就攤 |
| **US$180–205** | 較佳建倉觀察區 | 下一季 DSO ≤55、官方 FCF ≥US$30B或FCF margin ≥35%、GM ≥73.5%，而且DC增長仍高過同業；**全部確認**先由觀察轉建倉 |
| **US$205–240** | **等待確認；唔追盤前** | 現價區；技術面8月26日低過MA20 US$215.56、但高過MA50 US$207.75／MA200 US$195.37，唔等於估值安全 |
| **US$275–330** | Base合理值；新資金值博率下降 | 要有 FY2028 EPS約US$12.5可見度先合理 |
| **≥ US$420** | Bull已大致price in | 只有EPS上修到≥US$15兼FCF恢復先支持；持倉者另做position review |

- **分批框架：** 若用戶之後確認要建倉，可用三段（約US$200／185／170）；US$200／185要等全部確認條件，US$170只容許喺無失效而屬市場錯殺時建立小型研究倉。每段都要重查F2，唔以價格單獨觸發。
- **加倉條件（只係未來持倉框架）：** DSO ≤55、FCF ≥US$30B、GM ≥73.5%，而且Data Center增長仍高過同業AI／DC平均；未確認前維持「唔好加倉」。
- **減倉／止賺模型（只喺日後確認持倉先適用）：** US$420–450而FY2028 normalized EPS仍低過US$15，模型建議先減25%；US$450–510再減25%；高過US$510而EPS／FCF無同步上修，餘倉另做完整position review。呢個係模型政策，唔係對未知持倉嘅即時指令。
- **Thesis invalidation：** 未來兩季任一季（a）DSO再≥60，**或**（b）應收再快過DC；Rubin令GM <73.5%兼再下修；DC增長跌到同業或以下而無mix解釋；PORTS重述為即期類債務。任一核心條件觸發就要下修盈利同multiple，唔只調低目標價。

## 💡 顧問下一步建議

**等待確認／只觀察，唔追財報後盤前升幅。** 現價對Base有折讓，但Street共識未收齊，最重要嘅下一個估值中樞事件係 FY2027-Q3：Rubin收入、74%毛利指引、DSO同FCF轉換。下一步可把本報告嘅情景做成 `NVDA valuation card`；卡片只係F3展示層，唔另起一套22／26／30倍模型。

如用戶要正式建倉／持倉策略，先確認現有股數、成本、風險預算；期權交 Skill 7，唔喺F3混入 strike／expiry。

## 來源與限制

- **官方、verified：** NVIDIA FY2027-Q2 8-K EX-99.1／EX-99.2及Form 10-Q（期終2026-07-26；filed 2026-08-26；USD；US GAAP）；FY2026-Q1至FY2027-Q2共6個manifests驗證通過。
- **市場／共識、第三方：** yfinance（擷取2026-08-27；EPS／收入分析員表、收市、技術指標、peers）；StockAnalysis（2026-08-27 07:19 EDT盤前及S&P Global analyst aggregation）；Yahoo Finance市場評論。
- **資料衝突處理：** yfinance TTM收入、FCF、債務、trailing P/E落後一季，全部以官方TTM／10-Q覆寫；第三方共識唔覆寫官方Q3指引。
- **估值情景：** FY2028收入、EPS、FCF同倍數係研究假設，唔係公司指引；Street數字財報後仍可能顯著修訂。
- **X：** `x_access: degraded`；無一手X帖用作估值輸入。

*此分析僅供研究參考，不構成投資建議。*
