# AMD One-Pager（Update）

- **狀態：** F1 **PASS** 90／130 · Thesis **Mixed／Needs Monitoring** · F3 **高估**（現價已高過 Bull）
- **行動：** **僅觀察、唔好建倉、唔好新開賣 put**（持倉 **未確認**；唔寫減倉股數）
- **模式：** Update（相對 2026-08-27／09-03 舊一頁；用「What changed」，唔用 First 嘅五個全新事實）
- **數據截至：** 2026-09-27（Asia/Hong_Kong）。美股週末休市；HUD 現價沿用 F3 錨 **2026-09-24 收市**
- **最新官方季度：** 2026-Q2（期終 2026-06-27，USD，US GAAP／Non-GAAP，unaudited；8-K EX-99.1 accession `0000002488-26-000121`，filing 2026-08-04，`validation_status: verified`；Form 10-Q accession `0000002488-26-000123`，filing 2026-08-05，`verified`）
- **2026-Q3：** 會計期終約 **2026-09-26**，**尚未公布**。IR Calendar 截至 2026-09-27：**There are no upcoming events scheduled** → 業績日 **未官方確認**（第三方／yfinance 估約 **2026-11-03 盤後**，`unverified`）
- **現價：** US$629.26（yfinance delayed，2026-09-24 收市，America/New_York）；市值約 US$1.027T（普通股約 1,632m）。9/25 收 US$630.63、當日 High **US$639.00**＝52 週高（Skill 7；F3 寫過 delayed 638.00）。**HUD 現價／溢價 % 仍用 9/24 收市 US$629.26**，避免尺漂移
- **估值權威：** `output/AMD_2026-09-25_framework3.md`（PR #35）— Bear **US$180**／Base **US$360**／Bull **US$505**。現價對 Base **+74.8%**（629.26／360），已高過 Bull 約 **24.6%**。**本頁唔另估 target price。**
- **舊尺退役：** 2026-08-27／09-03 one-pager 同舊 F3 嘅 Bear **240**／Base **390**／Bull **620**（當時現價 US$458.11、對 Base +17%、F1 書面 95／130）**全部作廢**，唔再做活估值尺或 covered-call 閘
- **視覺交付：** `docs/amd/one-pager.html`（4 頁翻頁）。估值卡：`docs/amd/valuation.html`。雲端無 Mac Canvas 目錄，HTML 代替投影片主件
- **承接：** F1 PASS 90／130（PR #33）；F2 增長 **通過**、現金流／FCF／稀釋 **部分通過**（PR #34）；F3 高估、閘門「應減倉勿賣 put」（PR #35）；Skill 5 催化劑（PR #36）；Skill 6 Thesis Mixed（PR #37）；Skill 4 質量 NVDA ≫ AVGO > AMD > MRVL ≫ INTC，AMD 官方路徑估值最貴（PR #38）；Skill 7 有條件 10-23 備兌認購 700–705（PR #39）。**未跑 Skill 8 preview**（公布日未官宣）
- **持倉：** 未確認
- **閘門本輪：** **不變**（沿用 F3；Skill 4／6／7 已確認唔還原）

## 一句話結論

現價對 F3 官方路徑 Base **US$360 約 +74.8% 溢價**、已高過 Bull **US$505**；F1 PASS 90、增長通過、Thesis Mixed 證明嘅係質量，唔係買點 → **僅觀察、唔好建倉、唔好新開賣 put**。

## Decision HUD（引用 F3，禁止新 target）

權威：`output/AMD_2026-09-25_framework3.md`（PR #35）。同一截止日、同一現價／Base／溢價 %。本頁 **唔另起倍數**。

| 欄 | 數 | 來源 |
|---|---|---|
| 現價 | US$629.26 delayed（2026-09-24 收市，America/New_York）；9/25 收 630.63、High **639.00**；市值約 US$1.027T | yfinance；普通股約 1,632m；Q2 攤薄 1,659m |
| Bear / Base / Bull | **180 / 360 / 505** | F3 FY2027 公司 Non-GAAP P/E 中心。舊 240／390／620 **作廢** |
| 溢價／折讓 | 現價對 Base **+74.8%**（高估；已高過 Bull 約 24.6%） | 629.26／360 |
| 估值驅動 KPI | ① 總營收 US$11,536m（+50%）② Data Center US$6,718m（+107%）③ 官方 FCF US$1,558m（14%）④ Non-GAAP GM 56% ⑤ Helios $ **官方未量化** | F2／F3 ★ 列 |

**行動（第一句必須引用溢價／折讓）：** 現價對 Base 約 **+74.8% 溢價**，而且已經高過 Bull US$505 → **僅觀察、唔好建倉、唔好新開賣 put**。持倉閘 **維持應減倉，勿賣現金擔保認沽**；買認購閘 **維持合理或偏貴**。持倉未確認，唔寫減倉股數。

## 閘門兩項（本輪不變）

| 閘 | 狀態 | 來源 | 變咗？ |
|---|---|---|---|
| 持倉閘（covered call／減倉政策） | **應減倉，勿賣現金擔保認沽** | F3 PR #35 已改；Skill 4／6／7 維持 | **本輪否** |
| 買認購閘 | **合理或偏貴** | F3／Skill 7 | **本輪否** |

未確認持倉 → 行動 badge 只准 **僅觀察／唔好加倉**。模型「應減倉」係政策，**唔係**對未知倉位嘅股數指令。

## 1 · 結論

AMD 已經用已入帳 Data Center 證明自己唔再係 PC 周期股：2026-Q2 總營收 **US$11,536m**（+50% YoY）、Data Center **US$6,718m**（+107%、佔 58%、分部營業利潤 US$2,103m），近三季營收超自身指引中位。F1 **PASS 90／130**、F2 增長 **通過**、Skill 4 組內質量第三（NVDA ≫ AVGO > AMD）、Skill 6 **Mixed**——增長支柱 on track。08-27 到 09-27 **冇新一季損益表**，所以唔好因為股價由 US$458 抽到 US$629、又印 52 週高 US$639，就把 thesis 升級成 Intact。

仍未成立嘅路徑，係 Helios／Instinct **美元被 8-K 量化**，以及 FCF 質量由 Q2 **14%** 回到至少 18%。Q2 8-K 只寫 Helios「begins to ramp」；AAI 寫「in production」；9/8 CFO 口述「Q3 有收入、Q4 大級跳」屬 `unverified`，**冇改** Q3 指引約 US$13.0B ±0.3B。F3 Base 只用官方路徑 FY2027 收入 **US$56B**／EPS **US$7.63** × 47× → **US$360**；Street 平均約 US$88B／EPS US$15.57 **冇印喺 8-K**，唔入頁。

最大裂痕已經由「Helios 未入帳」擴到 **估值同時間表一齊過熱**：現價對 Base **+74.8%**，而且已經高過 Bull US$505 約 25%。Base 上行 −43%、Bear −71%、連 Bull 都低過現價約 20%。Skill 4：官方 TTM P/S **24.9×** 貴過 NVDA／AVGO 約 6–7 圈，組內對自身 Base 溢價最大。

對行動含義：Thesis Mixed 只回答「買它嘅理由部分成立」；F3 已經回答「值搏率極差」。現價對 Base 約 **+74.8% 溢價** → **僅觀察、唔好建倉、唔好新開賣 put**。持倉未確認。下一個最大閘係 **2026-Q3 財報**（估約 11/03 盤後，IR 未確認）；黑窗 **2026-10-27 至 11-03**。

## 2 · What changed（相對舊一頁 08-27／09-03）

來源：2026-Q2 8-K EX-99.1／10-Q（`verified`）；F3 PR #35；Skill 4–7（PR #36–39）。**無新一季帳面。** 舊 240／390／620 同現價 US$458 **退役**。

1. **估值尺同溢價已換檔，舊一頁唔好再用。** 舊 one-pager：現價 US$458.11、Bear 240／Base 390／Bull 620、對 Base **+17%**、F1 書面 95／130、行動「僅觀察／唔好加倉」。而家 HUD：US$629.26 vs **180／360／505**、對 Base **+74.8%**、已高過 Bull、F1 **90／130 PASS**。**唔因為股價由 458 升到 629 就上修 Base**——Q2 帳面同一個季度；Base 只用官方路徑，Helios 未量化。

2. **增長支柱維持、Helios 仍然零美元。** Q2 總營收 US$11,536m（+50%）、DC US$6,718m（+107%）**未被新申報改寫**。Helios 官方仍然無一美元。9/8、9/11 會議 **無** 8-K 入檔。8/31 HUMAIN go-live 係 **MI355X**，唔係 Helios／MI450。增長通過、第二曲線 at risk——同 F2／Skill 6。

3. **閘門已由「僅觀察勿新開」改為「應減倉勿賣 put」，本輪唔還原。** F3 因現價高過新 Bull、Helios $ 空白、FCF 14% 未修復而改閘。Skill 4／6／7 **無新官方帳面**，維持同一對閘。買認購閘 **合理或偏貴**。未確認持倉 → 唔寫減倉股數。

4. **現金流裂縫同稀釋工具未閉合，仲多咗票據同雙認股權證。** Q2 官方 FCF US$1,558m（OCF 2,366 − PPE 808；margin **14%** vs Q1 25%；`verified` · footnote 3）。TTM 官方 FCF US$7,736m、yield **0.75%**。Meta 認股權證最多 **160m** @ US$0.01（約 9.6% vs Q2 攤薄 1,659m）；OpenAI 另最多 160m（F3 Bull **只計 Meta**）。2026-08-17 關上 **US$4.75B** 高級票據——Q2 現金＋短投 US$13,111m／總債 US$3,226m＝4.06× **會過時**。

5. **催化劑、期權同同業位置而家先齊。** Q3 期終已過（約 09-26）、公布日估 **11-03 盤後**（`unverified`）、黑窗 **10-27 至 11-03**。Skill 7：只喺已確認持倉且決定減倉時，可賣 **2026-10-23** 備兌認購、行權價 **US$700–705**、張數 ≤ 持股×1/2÷100；被指派接受、不展期；**不賣現金擔保認沽、不買 call**。Skill 4：質量 **NVDA ≫ AVGO > AMD > MRVL ≫ INTC**，AMD 官方路徑估值最貴。

## 3 · 估值（只引用 Framework 3）

唔另起 compact 倍數。主方法：FY2027 公司 Non-GAAP P/E。輔助：分部 SOTP ＋ 官方 TTM FCF yield 0.75%。舊 240／390／620 **唔入表**。

| 情景 | 概率 | FY27 收入／DC | Non-GAAP EPS | P/E | 中心價 | vs 現價 |
|---|---:|---|---:|---:|---:|---:|
| Bear | 30% | US$46.0B／US$27.5B | US$5.60 | 32× | **US$180** | **−71.4%** |
| Base | 50% | US$56.0B／US$35.5B | US$7.63 | 47× | **US$360** | **−42.8%**（現價對 Base **+74.8%**） |
| Bull | 20% | US$68.0B／US$46.0B | US$9.22 | 55× | **US$505** | **−19.7%**（現價已高過 Bull 約 24.6%） |
| 概率加權 | — | — | — | — | US$335 | −46.8% |

Base 假設：Q3 按指引中位附近入帳（≥US$12.7B），Q4 只溫和順增（**唔用** Street Q4 約 US$16.1B）；Helios 開始有收入但 8-K **仍未**量化到足以改分子；股數 1.724B（研究假設第一 GW +40m）。Bull 收入 **仍然低過** Street 平均 US$88B，而且要扣滿額 Meta 160m。分析員目標價平均約 US$617 接近舊 Bull 620，**唔當估值**。

價格區（研究，唔係買賣指令）：現價喺 **≥US$505** 帶（含 US$629）——Bull 已過度 price in。建倉觀察區仍係 **US$280–360 而且要全部 F2 確認**——現價唔符合。可調驅動見估值卡。

## 4 · 催化劑與黑窗（未來 1–2 季）

窗口 2026-09-27 至約 2027-02。只列會改寫 F3 倍數或現金路徑嘅事件。沿用 Skill 5，唔另揀靚數。

| 時間 | 事件 | 要睇 |
|---|---|---|
| **已過（日曆錨）** | FY2026-Q3 會計期終約 **2026-09-26** | 入帳截止日，唔係公布日。`verified` 財政曆節奏 |
| **2026-10-27 至 11-03**（若估 11/03） | **期權黑窗**（財報前 5 個交易日） | **唔好新開備兌認購**。IR 確認日一出即平移。現價已高過 Bull → 黑窗外亦 **禁止新開賣 put**。研究規則，唔係經紀指令 |
| **約 2026-11-03 盤後**（yfinance／第三方；**IR 未確認**） | **2026-Q3 財報**（最大閘） | 入場券：營收 ≥**US$12.7B**。真正改 Base：8-K **首次量化** Helios 或 Instinct 美元／GW，兼 FCF margin ≥18%、DSO ≤58。日期 `unverified`；Q3 指引約 US$13.0B ±0.3B＝官方前瞻、**未入帳** |
| 同一份 Q3 8-K／隨後 10-Q | Helios $ 首次量化；票據 US$4.75B 入表 | 仍然無 $ **而且**把量產再推 Q4／2027＝失效。Q2 4.06× 現金／債會過時 |
| **2026 H2／Q4** | Meta／OpenAI 第一 GW 出貨 vs 認股權證第一檔 | 出貨入 8-K 兼有 $ 先算經營腿。現價已穿 US$600 門檻 ≠ 已歸屬 |
| **約 2027-02**（IR 未宣布） | Q4 暨全年業績 | 對質 F3 FY2026 橋約 US$48.4B vs Street Q4 約 US$16.1B／9/8「大級跳」 |

**失效兩卡（沿用 F2／F3／Skill 5／6，唔另創紅線）：**

1. Q3 營收明顯低過 US$12.7B，或管理層把差額歸因 Helios／Instinct 延後而無 EPYC 補上；或 Q3 8-K **仍然**無 Helios／Instinct 可核對美元，同時把量產再推去 Q4／2027。
2. 官方 FCF margin ≤14% **而且**應付較 Q2 回落超過約 US$1B，或單季 FCF 轉負；或 DC YoY < +40% 且 GAAP 毛利率跌穿 52%；或 Meta／OpenAI／Anthropic 其中一條官方 GW 協議被修訂／取消。

確認線：Q3 ≥US$12.7B ＋ 8-K 至少一條 Helios／Instinct $ ＋ FCF margin ≥18% ＋ DSO ≤58。全部過關先討論由觀察轉建倉——**而且**現價相對當時重算 Base 仍要有 ≥15% 折讓。而家一條都未齊。

## 5 · 主要風險

- **估值預支未入帳平台：** 現價若用 Base 47×，隱含 FY2027 收入約 US$98B——遠高過官方路徑 US$56B，接近 Street 上修版。Helios $ 空白時，倍數可以一次性壓縮。
- **FCF 14% 未證明一次性：** Q2 比 Q1 少 US$1,008m＝OCF 少 589 ＋ capex 多 419；10-Q 寫供應協議預付約 US$1.0B、應付時機把現金流整靚。再 ≤14% 兼應付回落 >US$1B → 結構性。
- **雙認股權證＋票據：** Meta／OpenAI 各最多 160m @ US$0.01；成功反而攤薄。US$4.75B 票據未入 Q2 表。
- **同業位置：** 官方 TTM P/S 24.9× 貴過 NVDA 17.9×／AVGO 18.9× 約 6–7 圈；對自身 Base 溢價係組內最大。CUDA 生態同 NVDA DC 一季 US$89B 仍喺另一數量級。
- **事件日未官宣：** Q3 公布日 `unverified`。黑窗跟第三方 11/03；IR 一改就要平移。

## 6 · 期權要點（只引用 Skill 7）

權威：`output/AMD_2026-09-27_skill7_option_strategy.md`（PR #39）。本頁 **唔另造 strike**。

- **預設：** 未確認持倉 → **唔好新開任何期權**。
- **有條件可新開備兌認購：** 只喺已確認持倉、**而且決定減倉**。到期 **2026-10-23**、行權價 **US$700–705**（高過 52 週高 639）、張數 **≤ 持股 × 1/2 ÷ 100**。被指派接受、**不展期**。若真正要即時削下行，**直接賣出部分現股更乾淨**。
- **硬禁：** **不賣現金擔保認沽。不買認購。不裸賣認購。不代下單。**
- **黑窗：** 2026-10-27 至 11-03（若估 11/03）唔好新開備兌認購。10-30 到期否決。
- **閘門：** 持倉閘／買認購閘 **本輪不變**。

## 7 · 各 Skill 頁（GitHub Pages）

| Skill | 狀態 | 頁 |
|---|---|---|
| Framework 1 | PASS 90／130（PR #33） | [初篩](https://keithcheungmk.github.io/stock-analysis/amd/framework1.html) |
| Framework 2 | 增長通過；現金流／FCF／稀釋部分通過（PR #34） | [深度增長](https://keithcheungmk.github.io/stock-analysis/amd/framework2.html) |
| Framework 3 | 高估；180／360／505（PR #35） | [估值](https://keithcheungmk.github.io/stock-analysis/amd/framework3.html) · [估值卡](https://keithcheungmk.github.io/stock-analysis/amd/valuation.html) |
| Skill 4 同業 | NVDA ≫ AVGO > AMD > MRVL ≫ INTC（PR #38） | [同業比較](https://keithcheungmk.github.io/stock-analysis/amd/peer-comparison.html) |
| Skill 5 催化劑 | Q3 估 11-03；黑窗 10-27 至 11-03（PR #36） | [催化劑日曆](https://keithcheungmk.github.io/stock-analysis/amd/catalyst-calendar.html) |
| Skill 6 Thesis | Mixed（PR #37） | [Thesis Tracker](https://keithcheungmk.github.io/stock-analysis/amd/thesis-tracker.html) |
| Skill 7 期權 | 有條件 10-23 CC 700–705（PR #39） | [期權策略](https://keithcheungmk.github.io/stock-analysis/amd/skill7-option-strategy.html) |
| Skill 8 財報 | **未跑 preview**（公布日未官宣） | [舊 Earnings Review](https://keithcheungmk.github.io/stock-analysis/amd/earnings-review.html)（08-27 尺，**已退役數字**） |
| Skill 9 本頁 | Update · 2026-09-27 | [one-pager](https://keithcheungmk.github.io/stock-analysis/amd/one-pager.html) · [Interactive Brief](https://keithcheungmk.github.io/stock-analysis/amd/interactive-brief.html) |

## 關鍵數字（財政期 · 幣種 · 會計基準 · 來源 · validation_status）

單位：USD million（另有標示除外）。會計基準：US GAAP／公司 Non-GAAP。貨幣：USD。

| 項目 | 數字 | 財政期 | 來源 | validation_status |
|---|---:|---|---|---|
| 總營收 | 11,536（+50% YoY） | 2026-Q2 期終 2026-06-27 | 8-K EX-99.1 | verified |
| Data Center／C+G／Embedded | 6,718／3,841／977 | 同上 | 分部表 | verified |
| DC 分部營業利潤 | 2,103（31%） | 同上 | 分部表 | verified |
| GAAP／Non-GAAP 攤薄 EPS | 1.38／1.66 | 同上 | 業績稿主表 | verified |
| GAAP／Non-GAAP 毛利率 | 54%／56% | 同上 | 簡明損益／調節 | verified |
| 官方 FCF | 1,558（OCF 2,366 − PPE 808；margin 14%） | Q2 | 調節表 footnote 3 | verified |
| H1 營收／官方 FCF | 21,789／4,124 | 2026 首兩季 | 同上 | verified |
| 現金＋短投／總債 | 13,111／3,226（4.06×） | 2026-06-27 | Selected Corporate Data | verified |
| 應收淨額／自算 DSO | 7,281／約 57 日 | 2026-06-27 | 資產負債表／自算 | verified／derived |
| 基本／攤薄加權股數 | 1,632m／1,659m | Q2 | 簡明損益 | verified |
| TTM 營收／官方 FCF | 41,305／7,736 | Q3'25–Q2'26 | 四季 EX-99.1 加總 | verified |
| Q3 營收指引 | 約 13,000 ±300 | 2026-Q3 | 業績稿 outlook | 官方前瞻，**未入帳** |
| Q3 Non-GAAP 毛利率指引 | 約 56% | 同上 | outlook | 官方前瞻，無 GAAP 對照 |
| Helios 已入帳收入 | **官方未量化** | 截至 2026-09-27 | 8-K／AAI IR | verified（空白本身係官方事實） |
| Meta 認股權證 | 最多 160m @ US$0.01 | event 2026-02-23 | 8-K `0000002488-26-000045` | verified 上限；歸屬前瞻 |
| 高級票據 | US$4.75B | 2026-08-17 關上 | 8-K `0001193125-26-354029` | verified；**未入 Q2 表** |
| 現價／52 週高 | 629.26／639.00 | 2026-09-24 收／09-25 High | yfinance delayed | 市況，第三方 |

## pending_sources／限制

- **pending：** Q3 業績日、Q3 8-K／10-Q、第一 GW 出貨、認股權證歸屬。catalog `pending_sources: 0`（六季包本身）。
- **官方前瞻、未入帳：** Q3 營收約 US$13.0B ±0.3B、Non-GAAP GM 約 56%；CFO「H2 Data Center sales accelerate」；Anthropic／OpenAI／Meta GW；Helios in production。
- **unverified：** Q3 業績約 2026-11-03；9/8、9/11 會議逐字稿；Street FY2027 US$88B／EPS US$15.57。
- **research assumption（沿用 F3，唔新造）：** Base 第一 GW 歸屬 40m 股；FY2027 收入／NM／倍數。
- **價格：** HUD 沿用 F3 同一錨：2026-09-24 收市 US$629.26。52 週高用 Skill 7 嘅 9/25 High **639.00**。
- **持倉：** 未確認。唔寫減倉股數。
- **raw 正文：** 呢個 cloud checkout 冇 `data/raw/AMD` 全文；數字對住已合併 `output/AMD_2026-09-25_*.md`／`AMD_2026-09-27_*.md` 同 SEC／IR 連結。**唔提交** raw 正文或私人經紀檔。
- **本 PR 停喺 Skill 9。** 唔重跑 F1–F8。Skill 8 preview 等 IR 宣布業績日。AMD 2026-09-25／27 全套刷新至此完成。

*此分析僅供研究參考，不構成投資建議。*
