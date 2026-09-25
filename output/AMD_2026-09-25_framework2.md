# AMD Framework 2 深度增長分析

- **判定：** Data Center／增長 thesis **通過**；現金流／FCF 質量／稀釋 thesis **部分通過**
- **行動：** **僅觀察**、**唔好加倉**（持倉未確認；唔寫加倉／減倉）
- **五季窗口：** 2025-Q2 → 2026-Q2（期終 2025-06-28、2025-09-27、2025-12-27、2026-03-28、2026-06-27）
- **數據截至：** 2026-09-25（Asia/Hong_Kong）；最新官方季 2026-Q2，USD，US GAAP／Non-GAAP，unaudited
- **核心 KPI：** Data Center 已入帳分部營收（需求代理；**唔係** Helios／Instinct 子項，公司未拆）＋官方自由現金流（FCF = 持續經營 OCF − 購置 PPE）
- **承接 F1：** PASS 90／130（PR #33 已併入 `main`）。必挖兩題：Helios／Instinct 收入確認節奏；FCF margin 14% 係一次性定結構性。
- **Framework 3：** 舊 Bear 240／Base 390／Bull 620 **已過期**。本頁 HUD 標 **`F3 pending` refresh**，**唔寫新 target price**，亦**唔用** 240／390／620 做 covered-call 活閘。

## 一句結論

Data Center 已喺損益表證明質變（五季 US$3,240m → US$6,718m，最新季 +107% YoY、佔總營收 58%、分部營業利潤 US$2,103m），但 Helios rack-scale **官方仍然無一美元**；Q2 官方 FCF margin 由 25% 跌到 14%，主要係 capex 跳到 US$808m、應收同供應協議預付款脹，而應付款項時機把現金流「整靚」——增長線夠入 Framework 3，現金流未閉合前唔好加倉。

## 數據驗證

- 官方優先：各季 8-K EX-99.1。2026-Q2 accession `0000002488-26-000121`，filing date 2026-08-04，[EX-99.1](https://www.sec.gov/Archives/edgar/data/2488/000000248826000121/q22026991.htm)；Form 10-Q accession `0000002488-26-000123`，filing date 2026-08-05，[10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000123/amd-20260627.htm)。`validation_status: verified`（損益／分部／FCF 用 8-K；應收歸因、供應預付、融資用 10-Q MD&A）。
- 其餘四季 EX-99.1：2025-Q2 [q22025991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248825000106/q22025991.htm)；2025-Q3 [q32025991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248825000163/q32025991.htm)；2025-Q4 [q42025991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000014/q42025991.htm)；2026-Q1 [q12026991.htm](https://www.sec.gov/Archives/edgar/data/2488/000000248826000072/q12026991.htm)。
- 官方 FCF 定義（各季 EX-99.1 footnote 3）：GAAP 持續經營經營現金流 − purchases of property and equipment。Q2：OCF US$2,366m − capex US$808m = **US$1,558m**（margin **14%**）。
- Helios／Instinct **冇**獨立分部列；需求 KPI 用 Data Center 已入帳。禁止把 GW 意向、Q3 指引、會議形容詞當成已入帳。
- 2026-09-08 Citi／2026-09-11 Goldman：官方只確認出席（[7/8 IR 稿](https://ir.amd.com/news-events/press-releases/detail/1289/amd-to-report-fiscal-second-quarter-2026-financial-results)＋IR Calendar）。**冇**對應 8-K 把會議內容入檔。第三方逐字稿 `source_tier: unverified`，只當時間線索。
- 2026-08-19 Form 8-K accession `0000002488-26-000163`：董事退休／任命（Joe Householder → Tim Ryan），**無**新財務數、無 Helios $。
- SEC submissions（CIK 0000002488，覆核 2026-09-25）：Q2 10-Q 之後最新業績相關 8-K 仍係 8/04；其後主要係 Form 4／144 同 8/19 董事 8-K。2026-Q3 **尚未公布**（期終約 2026-09-26）。
- yfinance 只用於現價、市值、同業 P/S。F1 已棄用嘅 aggregator（總債 US$4.28B、TTM FCF US$8.84B、trailing EPS US$3.93）本 F2 **同樣棄用**。
- 呢個 cloud checkout **冇** `data/raw/AMD` 正文；數字對住 SEC 原文。catalog `data/source-catalog/amd-six-quarters.json`：`pending_sources: 0`。持倉覆蓋檢查（其餘 9 隻 raw）唔可跑。
- 交貨距 F1 0 日，未超過 7 日，唔另跑 x-adversarial-review。

## 承接 Framework 1

| 必挖問題 | 發現（而家證明到邊；仲差邊個門檻） |
|---|---|
| **1. Helios／Instinct 收入確認節奏 vs 敘事：** Q2 官方只得「begins to ramp」；9/8 第三方話 Q3 開始有收入、Q4 大級跳。要對住 **有冇可核對美元／GW**，而唔好再信會議形容詞。 | **Instinct 已入帳一截；Helios $ 未通過。** Data Center 五季 US$3,240m → **US$6,718m**（+107% YoY、+16% QoQ、佔季收 **58%**）。官方句子一路升級：Q2'25 已入帳主要係 EPYC（Instinct MI308 對華受出口管制、另錄約 US$800m 存貨相關費用）；Q3'25 DC +22% YoY 已寫 **MI350 Series**；Q1'26「Instinct GPU shipments continued ramp」；Q2'26 Lisa Su：「Instinct deployments scale **and Helios begins to ramp**」。Helios 喺 Q2'25 AAI 仲係「next-generation」簡報；Q2'26 8-K 改口「Launched the AMD Helios rackscale solution」，客戶名單 Anthropic／Meta／Microsoft／OpenAI／Oracle 等——**全部無美元、無 GW 已入帳。** [AAI 2026-07-23 IR](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) 寫 in production、gigawatt scale，同樣無 $。Anthropic 最多 2 GW（第一 GW **2027 H1**）、OpenAI 6 GW、Meta 6 GW（第一 GW 2026 H2）都係前瞻 IR。9/8 CFO 口述「Q3 有收入、Q4 step up」屬 unverified，**冇改** Q3 指引 US$13.0B ±0.3B。**仲差：** 下一次（2026-Q3）8-K／10-Q 能量化 Helios 或 Instinct 美元／GW；否則 24.9× P/S 繼續預支未入帳平台。 |
| **2. FCF margin 回落係一次性定結構性：** Q1 25% → Q2 14%，OCF 29%→21%，PPE US$389m→US$808m，應收 US$7,281m。 | **而家證明：五季 FCF 全正，Q2 轉換惡化可以拆開，未證明 14% 係新常態，亦未證明一次性。** 官方 FCF：1,180 → 1,530 → 2,082 → 2,566 → **1,558**（margin 15% → 17% → 20% → 25% → **14%**）。Q2 比 Q1 少 US$1,008m，剛好 = OCF 少 US$589m ＋ capex 多 US$419m。10-Q MD&A（H1）：應收 +US$966m「primarily by higher revenue」；預付同其他資產 +US$1.0B「primarily due to **prepayments of supply agreements**」；應付 +US$2.2B「primarily due to **timing of payment obligations**」。Q2 單季應收 +US$1,246m、存貨 +US$423m、應付 +US$2,274m——應付時機把 OCF 托住；供應協議預付同 PPE（淨額 YE US$2,312m → Q2 **US$3,439m**）睇落係 Instinct／Helios 備貨，**唔似**純季節性。自算 DSO（應收／（營收／91 日），**唔係**公司披露）：YE 約 56 日 → Q1 約 54 日 → Q2 約 **57 日**，未失控。現金＋短投 US$13,111m／總債 US$3,226m = **4.06×**；H1 融資淨**流出** US$365m（回購 US$221m + 稅扣 US$341m − 員工認股 US$205m），**唔係**靠新股本／新債續命。Q2 GAAP 淨利 US$2,297m 含長期投資收益約 **US$483m**（Non-GAAP 已剔除）——盈利質量要睇分部同 FCF，唔好只睇淨利。**仲差：** Q3 官方 FCF margin 回升到 ≥18%，而且應付／預付唔再單向膨脹；若 margin 再 ≤14% 同時應付回落，14% 就變成結構性。 |

## 8–12 KPI 五季摘要

單位：US$ million（另有標示除外）。來源：各季 8-K EX-99.1 Selected Corporate Data／分部表／FCF 調節；Q2 應收、存貨、PPE、應付嚟自 8-K 資產負債表同 10-Q。DSO 同 Q1 應收係自算／由現金流加回，**唔係**公司披露。

*估值驅動 KPI 用 ★ 標示（後續 F3／HUD 沿用同一批，唔另揀靚數）。*

| KPI | 25Q2<br>(2025-06-28) | 25Q3<br>(2025-09-27) | 25Q4<br>(2025-12-27) | 26Q1<br>(2026-03-28) | 26Q2<br>(2026-06-27) | 趨勢 |
|---|---:|---:|---:|---:|---:|---|
| ★ 總營收 | 7,685 | 9,246 | 10,270 | 10,253 | 11,536 | **改善** |
| 營收 YoY | +32% | +36% | +34% | +38% | +50% | **改善** |
| ★ Data Center（需求 KPI） | 3,240 | 4,341 | 5,380 | 5,775 | 6,718 | **改善** |
| DC YoY／佔比 | +14%／42% | +22%／47% | +39%／52% | +57%／56% | +107%／58% | **改善** |
| Client + Gaming | 3,621 | 4,048 | 3,940 | 3,605 | 3,841 | 高位波動 |
| Embedded | 824 | 857 | 950 | 873 | 977 | 改善 |
| GAAP／Non-GAAP 毛利率 | 40%／43% | 52%／54% | 54%／57% | 53%／55% | 54%／56% | 高位持平（Q2'25 扭曲） |
| DC 分部營業利潤（率） | −155（−5%） | 1,074（25%） | 1,752（33%） | 1,599（28%） | 2,103（31%） | **改善** |
| GAAP 營業利潤率 | −2% | 14% | 17% | 14% | 17% | 改善 |
| OCF（持續經營）／margin | 1,462／19% | 1,788／19% | 2,304／22% | 2,955／29% | 2,366／21% | Q2 回落、仍正 |
| ★ 官方 FCF／margin | 1,180／15% | 1,530／17% | 2,082／20% | 2,566／25% | 1,558／14% | **惡化（仍正）** |
| ★ 應收／自算 DSO | — | — | 6,315／56 日 | ~6,035／54 日 | 7,281／57 日 | 金額脹、DSO 未失控 |
| 現金＋短投／總債 | 5,867／3,218（1.8×） | 7,243／3,220（2.3×） | 10,552／3,222（3.3×） | 12,347／3,224（3.8×） | 13,111／3,226（4.1×） | **改善** |
| 攤薄加權股數（百萬） | 1,630 | — | — | 1,650 | 1,659 | 緩升（員工股） |

註：

1. Q2'25 GAAP／Non-GAAP 毛利率被約 **US$800m** MI308 出口管制存貨相關費用壓低；官方：撇除後 Non-GAAP 毛利率約 **54%**。之後四季 GAAP 毛利率企喺 52–54%。
2. Q4'25 另有約 US$360m MI308 存貨準備回撥、對華 MI308 收入約 US$390m；官方：撇除後 Q4 Non-GAAP 毛利率約 55%。**唔把回撥當成核心單位經濟改善。**
3. Q1 應收 ~US$6,035m = YE US$6,315m −（H1 應收增加 966 − Q2 單季增加 1,246）。`validation_status: derived`，用官方現金流同期末應收加回。
4. Helios 已入帳收入：五季官方 **全部未量化**。Q3 指引約 US$13.0B ±0.3B、Non-GAAP 毛利率約 56%——**唔入五季表、唔當已入帳**。
5. TTM（25Q3–26Q2，同 F1）：營收 **US$41,305m**；Data Center **US$22,214m**；官方 FCF **US$7,736m**（margin 18.7%）；GAAP 淨利 **US$6,434m**。
6. Q2 融資幾乎持平（−US$15m）；H1 融資淨流出 US$365m。現金上升主要係經營造血再泊入短投，**唔係**新股本。
7. Meta 績效認股權證最多 **1.60 億股**（行使價 US$0.01；8-K `0000002488-26-000045`）未反映喺上表攤薄股數。對照 Q2 攤薄 1,659m，全數歸屬約 **9.6%**。

## Decision HUD（F3 pending refresh）

數字同 F1、同一截止日。**唔引用**舊 Bear 240／Base 390／Bull 620 做活估值尺。

| 欄 | 數 | 來源 |
|---|---|---|
| 現價 | US$629.26 delayed（2026-09-24 收市，America/New_York）；前收 US$614.61（9/23）；市值約 US$1.027T | yfinance；Q2 攤薄加權 1,659m |
| 暫定規尺（非 target） | TTM P/S **24.9×**；trailing P/E **162×**；官方 FCF yield **0.75%** | 市值／官方 TTM 營收 US$41,305m、EPS US$3.89、FCF US$7,736m |
| 溢價／折讓 | P/S 較 NVDA 約 17.9×／AVGO 約 18.8× **貴約 6–7 圈** | yfinance 同業 9/24；官方 TTM |
| 估值驅動 KPI | ① Data Center US$6,718m（+107%）② 總營收 US$11,536m（+50%）③ 官方 FCF US$1,558m（margin 14%）④ Non-GAAP 毛利率 56% ⑤ Helios $ **官方未量化** | 五季表 ★ 列 |

**行動（第一句必須引用溢價／折讓）：** 現價 TTM P/S 約 **24.9×**，較 NVDA 約 17.9×／AVGO 約 18.8× **貴約 6–7 圈** → **僅觀察、唔好加倉**。

### 對 covered-call hold gate 嘅旗標（唔另開 Skill 7）

舊 F3 減倉／鎖定區 ≥ US$620 或接近 Bull。現價 **US$629.26 已高過舊 Bull**，RSI（14）9/24 **72.5**。呢兩條會觸及**舊圖**閘位，但 F3 **過期**——**禁止**用 240／390／620 做 live strike 或新目標價。要等 Framework 3 刷新先重畫 hold gate。其他會影響閘位嘅旗標（本 F2 量化）：

1. Helios $ 仍空白——而家 24.9× 已預支 Q3／Q4 ramp。
2. Q2 FCF margin **14%** 未修復；應付時機同供應預付可以喺下兩季反向。
3. Meta 認股權證最多 1.60 億股（潛在攤薄約 9.6%）——沽 call／續抱要計稀釋，唔好當 1,659m 股係終局。
4. F1 PEG 維度已 0 分；yfinance PEG 0.63 靠前瞻 EPS，Helios 未量化，**唔可用**嚟放寬閘。

## 五大維度

1. **敘事：通過。** 唔再係「未來先有 Data Center」。五季 DC 由 US$3.24B 去到 US$6.72B，佔比 42%→58%，YoY 14%→107%，分部營業利潤由 −US$155m 去到 **US$2,103m**。通過係因為已入帳美元、mix 同分部利潤同步喺損益表，唔係因為單季 beat 或者 Helios 簡報。Helios 本身仍係故事——呢條裂縫記入問題 1 同護城河，**唔夠**把整條 DC 敘事打回「簡報」。Q3 指引 US$13B 仍然係前瞻。

2. **單位經濟：通過。** 撇除 Q2'25 嗰筆 US$800m 管制費用之後，Non-GAAP 毛利率企喺 **54–57%**；Q2 GAAP 54%、Non-GAAP 56%，Q3 指引 Non-GAAP 約 56%。DC 分部營業利潤率由負數去到 **31%**（US$2,103m／US$6,718m），規模已經有意義。Q1→Q2 毛利率再加 1ppt，唔係「高毛利只存在於未入帳 ARR」。Q2 GAAP 淨利被約 US$483m 投資收益托高，所以單位經濟唔用淨利率做主證；主證係毛利率同 DC 分部貢獻。9/8 unverified 口述話 2027 毛利率可能「略低過 Q3 指引」——只當裂縫線索，唔改本窗判定。

3. **護城河：部分通過。** 可觀察壁壘：EPYC 伺服器份額（官方連續多季寫 strong demand）、開放 Helios rack（72× MI455X + Venice + Pensando + ROCm）、ROCm.ai。反證同樣硬：Instinct 仍係 NVDA 之後嘅第二供應商敘事；CUDA／軟件生態未翻盤；官方錨點客戶（Meta／OpenAI／Anthropic）把增量集中喺少數超大規模，而且 Meta 認股權證把「客戶轉換成本」寫成潛在 **9.6%** 攤薄。Helios 客戶名單長，但 **零美元入帳**，所以生態壁壘仲未喺損益表封頂。

4. **營運槓桿：通過。** GAAP 營業利潤率 −2% → **17%**；Non-GAAP 12% → **27%**。GAAP OpEx／營收約 42% → **37%**（Q2 US$4,213m／US$11,536m）。營業費用絕對值上升（研發 Q2 US$2,528m），但慢過收入。Q2 capex 跳到 US$808m（收入 7.0%）係現金流裂縫，唔係 OpEx 失控。

5. **現金流：部分通過。** 五季官方 FCF **全部為正**，現金／債由 1.8× 去到 **4.1×**，H1 融資淨流出——**唔符合「未通過」**（未通過要五季惡化或現金主要靠融資）。部分通過係因為路徑唔單調：15%→25%→**14%**；Q2 少咗嘅 US$1.0B 可以拆成 capex + 應收／供應預付，再被應付時機對沖。10-Q 自己把預付寫成 supply agreements、應付寫成 timing——前者偏結構（Helios／Instinct 備貨），後者可以反轉。TTM FCF US$7.7B、yield 只有 **0.75%**，對住 24.9× P/S，轉換質量而家係估值約束而唔係生存約束。

## Bull / Bear / 行動

- **Bull：** Q3 已入帳 ≥ US$12.7B（指引下限）而且 8-K 首次量化 Helios 或 Instinct 美元／GW；官方 FCF margin 回到 ≥18%；自算 DSO ≤58 日、應付唔大幅回落；Non-GAAP 毛利率守住約 56%；EPYC／DC 增速唔跌穿 +50% YoY。
- **Bear：** Q3 miss US$12.7B 同時 Helios 再無 $；FCF margin 再 ≤14% 而且應付回落、預付再脹；DC 增速跌至 < +50% YoY 且毛利率跌穿 52%；Instinct ASP 被 NVDA／客製 ASIC 壓穿；Meta 認股權證開始歸屬而 Helios 仍未入帳。
- **行動：** **僅觀察、唔好加倉。** 現價 TTM P/S 約 **24.9×**，較 NVDA／AVGO **貴約 6–7 圈**。增長 thesis 通過，可入 Framework 3；現金流同 Helios $ 未閉合，唔把 F1 PASS／F2 增長通過當成建倉區或 covered-call 活閘。無確認持倉，唔寫減倉。

## 確認／失效

以 **2026-Q3 財報／指引**（期終約 2026-09-26；下一次已公布季度；yfinance 估 2026-11-03，**未見官方確認日期**）為時間窗：

**確認**

1. Q3 營收 ≥ US$12.7B（守住指引下限），且 8-K／10-Q **至少**量化 Helios 或 Instinct 其中一條已入帳美元（或官方 GW 出貨），唔再只得「begins to ramp／in production」。
2. Q3 官方 FCF 仍正，而且 FCF margin ≥ **18%**（或 capex 回落到 ≤ US$500m 而 OCF margin ≥24%）。
3. 自算 DSO ≤58 日；應收 QoQ 增量低於營收 QoQ 增量；供應協議預付唔再單季再脹超過約 US$0.5B。
4. Data Center YoY 仍 ≥ +50%，GAAP 毛利率 ≥53%。

**失效**

1. Q3 營收明顯低過 US$12.7B，或管理層把差額歸因 Helios／Instinct 延後，而無 EPYC 補上。
2. Q3 8-K **仍然**無 Helios／Instinct 可核對美元，同時把量產再推去 Q4／2027——本 F2「Helios 只係未入帳、唔係假敘事」嘅假設過時。
3. 官方 FCF margin ≤14% **而且**應付較 Q2 回落超過約 US$1B（時機反轉），或單季 FCF 轉負。
4. DC YoY < +40% 且 GAAP 毛利率跌穿 52%，或 Meta／OpenAI／Anthropic 其中一條官方 GW 協議被修訂／取消。

## 可入 Framework 3

增長 thesis **通過**、現金流 **部分通過**（Q2 14% 已拆開，唔係唯一未 dig 嘅未知）→ **可以入 Framework 3**。舊 F3（2026-08-27）區間已穿、已過期，**必須重跑**，唔好沿用 240／390／620。最敏感嘅兩條變數（數字必須同本表一致）：

1. **Data Center 已入帳增速／Helios mix**（Q2 US$6,718m、+107%；Helios $ 仍空白——決定 P/S 分子同可不可以維持 20× 以上倍數）
2. **FCF 轉換**（Q2 US$1,558m、margin 14%；TTM US$7,736m、yield 0.75%——決定 FCF yield 同稀釋後每股現金）

互動報告（Markdown）：`output/AMD_2026-09-25_framework2.md`  
互動報告（HTML）：`output/AMD_framework2.html`  
手機網頁（GitHub Pages，合併 main 後）：https://keithcheungmk.github.io/stock-analysis/amd/framework2.html

*此分析僅供研究參考，不構成投資建議。*
