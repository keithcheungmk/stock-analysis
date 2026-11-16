# ANT Framework 1 初篩報告（Anthropic, PBC · 預上市）

- **結果：** WATCH（**provisional** — 未上市，缺 S&P 相對回報同公開共識／guidance 歷史；按規則不可給最終 PASS）
- **總分：** 65 / 130
- **數據截至：** 2026-11-16（Asia/Hong_Kong）
- **最新官方財務：** 2026-Q3（期終 2026-09-30，USD，US GAAP／Non-GAAP，unaudited；載於 Form **S-1/A Amendment No. 2**，filed 2026-11-10，accession `0001628280-26-072484`，`validation_status: partial`／`_ipo` substitute）
- **擬掛牌：** Nasdaq Global Select · 代號 **ANT** · 公司招股區間 **US$70.00–78.00**；S-1 資本表用假設價 **US$74**（區間中位）
- **IPO 日程（公司／媒體交叉，以招股書為準）：** 定價預期 2026-11-18；開始交易預期 2026-11-19（分析日仍**無公開成交價**）
- **核心結論：** 最大亮點係 Q3’26 GAAP 營收 **US$16,956m（+1,127% YoY）** 同 ≥US$100k TTM 客戶由約 950 增至超過 **11,900**；最大風險係約 **US$900.9B** compute／基建承諾（未來 12 個月約 **US$70.7B** 到期）疊加 IPO 區間隱含 **~27× TTM P/S**，而且 GAAP 仍大額虧損、投票權由 Founder Class F／LTBT 主導。

## 數據驗證

- `validate_raw_manifests.py --root data/raw/ANT`：通過（7 manifests：`_ipo` + 六季 partial）
- 權威來源：SEC S-1/A-2；輔證 Anthropic 官方 S-1 公告（2026-10-26）、IPO fact sheet、Series H 新聞稿（估值／融資敘事，**唔覆寫** S-1 損益）
- 各季無 Form 10-Q／10-K → `validation_status: partial`；財務以 `_ipo` S-1/A substitute
- 未跑 `python src/main.py ANT`（未上市／無 Yahoo 歷史）
- 持倉 coverage-config **不適用**（ANT 非持倉 10 隻；用 `config/official_sources_ant.yaml`）

## 關鍵財務快照（USD millions，除非另註）

| 項目 | 數字 | 財政期／口徑 | 來源 |
|---|---:|---|---|
| 營收 | 16,956 | 2026-Q3 · GAAP | S-1/A-2 |
| 營收 YoY | **+1,127%** | vs 2025-Q3 | S-1/A-2 |
| 營收 QoQ | **+47%** | vs 2026-Q2 US$11,555 | S-1/A-2（研究計算） |
| 9M 營收 | 33,242 | 9M’26 · GAAP | S-1/A-2（Revenue $2,545 → $33,242） |
| TTM 營收（研究加總） | **~35,282** | Q4’25 2,040 + Q1–Q3’26 | S-1/A 季度表／fact sheet 對照 |
| Run-Rate Revenue | ~**US$81B** | as of 2026-10-31 | S-1/A-2（**operating metric**，唔當 GAAP） |
| GAAP 營業損益 | (567) / 9M (1,260) | Q3／9M’26 | S-1/A-2 |
| GAAP 淨虧損 | 9M **(104,039)** | 主因 convertible／SAFE 公允價值變動 | S-1/A-2 |
| Adjusted Operating Income | 9M **4,081**；Adj. OM **12%** | Non-GAAP | S-1/A-2 reconciliation |
| 經營現金流 | 9M **+6,569** | GAAP | S-1/A-2 |
| 購置 PPE | 9M **(925)** | GAAP | S-1/A-2 |
| 近似 FCF（OCF−PPE） | 9M **~+5,644** | 研究計算 | 同上 |
| 現金及等價物 | **95,600** | 2026-09-30 | S-1/A-2 正文 |
| 短期投資 | **36,300** | 2026-09-30 | S-1/A-2 正文 |
| 現金＋短投 | **131,845** | 資產負債表 | S-1/A-2 capitalization |
| Notes payable | **130,502** | 2026-09-30 actual | S-1/A-2 |
| 總負債 | **146,683** | 2026-09-30 actual | S-1/A-2 |
| Compute 承諾合計 | **~900,900** | as of／subsequent to 2026-09-30 | S-1/A-2 |
| 未來 12 個月到期承諾 | **~70,700** | following 2026-09-30 | S-1/A-2 |
| ≥US$100k TTM 客戶 | **>11,900**（vs >950 a year earlier） | 2026-09-30 | S-1/A-2 |
| ≥US$1M / ≥US$10M TTM 客戶 | **>1,900** / **~250** | 2026-09-30 | S-1/A-2 |
| Net Revenue Retention | **~900%** | 2026-09-30 | S-1/A-2 |
| IPO 發行 | 825,000,000 Class A（公司 801,351,354 + 售股股東 23,648,646） | 招股書封面 | S-1/A-2 |
| 上市後 Class A／Class N（假設） | **7,427,991,791** / **5,658,680,800** | after offering + concurrent private placement | S-1/A-2 |
| 研究用市值（A+N × US$74） | **~US$968B** | 暫定，非成交價 | 研究計算 |
| 研究用 TTM P/S | **~27.5×** | 968B / 35.282B | 研究計算 |
| 媒體報全面攤薄市值 | 約 **US$1.3–1.45T**（區間） | 口徑異於 A+N；更高 → P/S 更貴 | 第三方（`unverified` 對股本定義；唔覆寫 S-1） |

季度營收（US$m，S-1/A／fact sheet 一致口徑）：

| Q1’25 | Q2’25 | Q3’25 | Q4’25 | Q1’26 | Q2’26 | Q3’26 |
|---:|---:|---:|---:|---:|---:|---:|
| 376 | 787 | 1,382 | 2,040 | 4,731 | 11,555 | **16,956** |

## 致命紅線

### 1. 破產／流動性風險：**安全**

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金＋短期投資 | US$131.8B | S-1/A-2，2026-09-30 |
| Notes payable | US$130.5B | 同上 |
| 9M 近似 FCF（OCF−PPE） | ~**+US$5.6B** | 研究計算 |

紅線要「現金低於總債務 **並且** 自由現金流為負」同時成立。現金＋短投略高過 notes payable；9M 近似 FCF 為正 → **未觸發**。  
**觀察：** 單看現金等價物 US$95.6B 低過 notes；IPO 後 pro forma as adjusted 現金＋短投升至約 **US$212.7B**（假設 US$74）。另有約 **US$70.7B** 承諾於未來 12 個月到期——入主風險，但唔構成機械紅線 1。

### 2. 衰退陷阱：**安全**

Q3 營收 YoY **+1,127%**，遠高過可比公開同業需求增速（Microsoft Azure and other cloud services 約 **+40–43%**；本倉 AMD Data Center **+107%**／NVDA Data Center 語境約 **+117%**）。GAAP 淨利率雖深度為負，但「增速低於同業」第一項不成立 → **未觸發**。

### 3. 估值泡沫：**未否決（高風險觀察）**

- GAAP／調整後盈利路徑仍受大額非現金公允價值項目扭曲 → **PEG 不可用**（唔虛構）
- 假設 IPO 中位市值 ~US$968B（Class A+N × US$74）／TTM ~US$35.3B → **P/S ~27.5×**；相對 Q3 年化（×4）約 **14.3×**；相對 Run-Rate US$81B 約 **12.0×**（後者係 operating metric）
- 對照：成熟雲／半導體平台 TTM P/S 常見低過呢個水平，但 ANT 有 **四位數 YoY** 增長 → 唔符合「缺乏相應高增長支持」嘅機械否決
- 結論：**未否決**；估值透支列入主風險，留給 Framework 3

## 13 維度評分

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金＋短投 US$131.8B vs notes US$130.5B（約 1.01×，未達 2×） | 5 | 高過債務但未達兩倍 | S-1/A-2 2026-09-30 |
| 營收增長 | Q3 +1,127% YoY vs Azure ~40–43%、AMD DC +107% | 10 | 高過行業均值超過 10pp | S-1/A-2；MSFT FY26；本倉 AMD F1 |
| 淨利潤率 | 9M GAAP 淨虧損 US$104.0B；營業虧損 US$1.26B | 0 | 虧損 | S-1/A-2 |
| 估值（PEG） | PEG 不可用；TTM P/S ~27.5×（IPO 中位假設） | 0 | 倍數透支／PEG 不可用按 0 | 研究計算；S-1/A-2 |
| 潛在市場規模（TAM） | 公司稱知識工作經濟價值 >US$40T（2025）；生命科學相關 >US$2T | 10 | 遠超 US$100B | S-1/A-2／IPO fact sheet（公司估算） |
| 用戶增長（同業對比） | ≥US$100k TTM 客戶 >11,900 vs >950（約 **12.5×** YoY）；NRR ~900% | 10 | 遠高過同業雙位數增速；以客戶 KPI 替代「用戶」並披露 | S-1/A-2 |
| ROE | Accumulated deficit ~US$156–171B；實際股東權益赤字 | 0 | 低於 8%／負權益 | S-1/A-2 |
| 自由現金流 | 9M OCF +US$6.6B、近似 FCF 正；但 FY23–25 OCF 長期為負、投資現金流大額負 | 5 | 有波動但最近一期為正 | S-1/A-2 |
| 護城河 | Claude 企業採用、安全／PBC 品牌、模型能力；同時面對 OpenAI／Google／開源激烈競爭 | 5 | 有壁壘但非無爭議壟斷 | S-1/A-2 Risk Factors |
| 行業趨勢 | 前沿 AI／企業代理工作流係資本市場主線 | 10 | 完全符合核心趨勢 | S-1/A-2 |
| 管理層能力 | 由研究實驗室做到 Q3 單季 ~US$17B 營收；同時 PBC＋LTBT＋Founder Class F（50.1% 投票）治理非常規 | 10 | 執行紀錄強；治理另列 adversarial | S-1/A-2 |
| 相對 S&P 500 表現 | **未上市**，無公開 total return | 0 | 資料不足；不可猜正面 | — |
| 市場預期 vs 實際表現 | 無公開共識／官方 quarterly guidance 歷史 | 0 | 資料不足；不可猜正面 | — |
| **合計** |  | **65** | WATCH 門檻 65–85 |  |

## Adversarial check

- **最強支持：** Q3 GAAP 營收 US$16.956B、+1,127% YoY；≥US$100k 客戶約 12.5×；NRR ~900%；9M Adjusted Operating Income 轉正（US$4.081B，margin 12%）；帳上現金＋短投 >US$130B。
- **最強反證：** ~US$900.9B compute 承諾（12 個月內 ~US$70.7B）；Q3 QoQ 營收增速由 Q2 的 ~+144% 減速至 **+47%**；GAAP 營業再轉虧（Q2 營業利潤 US$974m → Q3 虧損 US$567m，含短期 compute 承諾費用同非現金項目）；消費型收入 vs 多年期承諾期限錯配；雙層／多類股票令公眾 Class A 經濟權益同投票權分離。
- **最可能令結論失效嘅假設：** IPO 後公開市場拒絕 ~27× TTM P/S，或者營收增速繼續 QoQ 減速同時近端 compute 現金流出加速，令「高增長撐住倍數」故事破裂。

## 估值驅動 KPI（Decision HUD 共用 · F3 pending）

| KPI | 最新官方數 | 方向 | 點樣郁倍數 | 來源 |
|---|---|---|---|---|
| ★ Q3 GAAP 營收／YoY | US$16,956m · **+1,127%** | 改善（絕對額） | 決定 P/S 分子 | S-1/A-2 |
| ★ QoQ 營收增速 | **+47%**（前季 ~+144%） | 惡化（增速） | 若繼續減速，壓縮給出嘅增長溢價 | 研究計算 |
| ★ 近似 FCF／現金消耗 | 9M OCF +US$6.6B；PPE US$0.9B；但投資現金流 −US$36.5B | 混合 | 決定能否自我融資近端承諾 | S-1/A-2 |
| ★ Compute 承諾（12 個月） | **~US$70.7B** due | 壓力 | 現金／再融資敘事；拖累 FCF yield | S-1/A-2 |
| ★ ≥US$1M TTM 客戶／NRR | >1,900 · NRR ~900% | 改善 | 企業擴張能否撐住消費收入 | S-1/A-2 |

**HUD 尺（暫定，非 target price）：** IPO 假設價 US$74；市值 ~US$968B；TTM P/S ~27.5×；PEG 不可用；9M 近似 FCF ~US$5.6B vs 市值 → FCF yield ~0.6%（極低）。相對成熟雲平台倍數：**明顯溢價**，靠四位數增長辯護。

**行動（唔寫建倉區）：** 相對同業／成熟軟件歷史，IPO 中位隱含 TTM P/S 約 **27.5×** 屬高溢價 → **僅觀察**；等上市後真實成交價、首份 10-Q、同 Framework 3 先討論倉位。

## 下一步

**WATCH → 升級 PASS 需要（量化）：**

1. 上市後有可核對成交價／全面攤薄市值，且至少補齊「市場預期 vs 實際」其中一季（首份 earnings vs 共識或自設 guidance）。
2. 下一季 GAAP 營收維持高 YoY，同時 QoQ 不再大幅失速（研究觀察閘：QoQ 唔好再腰斬式下跌），同／或近端 compute 現金流出同 OCF 路徑對得上。
3. Framework 2 建議深挖兩條（若維持 WATCH／日後升 PASS）：
   - **問題 A：** 消費收入期限 vs ~US$900B 承諾嘅現金錯配，會唔會喺 2027 前迫使再融資／稀釋？
   - **問題 B：** Q3 QoQ 減速同營業再轉虧，係一次性 compute 費用，定係單位經濟轉弱？

最近催化：**2026-11-18／19 IPO 定價與開售**；其後首份 Form 10-Q。

*此分析僅供研究參考，不構成投資建議。*
