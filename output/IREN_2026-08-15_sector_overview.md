# Skill 0：電力鎖定 AI Cloud × Bitcoin Mining 賽道地圖

- **賽道：** 擁有電網接入同土地嘅運算基礎設施，將電力轉成 Bitcoin hashrate 或 GPU／AI Cloud
- **焦點公司：** IREN（今次研究對象）；對照 CLSK、CRWV、CIFR
- **數據截至：** 2026-08-15；現價為 yfinance delayed／previous close（2026-08-14，America/New_York）
- **下一步：** IREN 值得入 Framework 1；CRWV 係質量標尺但唔係同質對手

## 一句話定義

呢個賽道賣嘅唔係「幣」本身，而係**已接電、可快速上架嘅運算產能**：一邊用 ASIC 挖 Bitcoin 變現電力，一邊把同一塊電力改造成 GPU cluster，賣俾 hyperscaler 同 AI 雲客戶。

## TAM / SAM / SOM

| 口徑 | 合理範圍 | 容易誇大嘅地方 |
|---|---|---|
| TAM | 全球 AI 數據中心／GPU 雲未來數年資本開支以千億美元計；Bitcoin mining 只係細好多嘅周期市場 | 把成個「AI 經濟」當成交收；5GW 電力 ≠ 5GW 收入 |
| SAM | 北美（尤其 Texas／ERCOT）同可再生電力密集區，有大規模負載接入資格嘅獨立運算營運商 | 把 Google／Microsoft／Amazon 自建容量當成獨立 neocloud 可搶市場 |
| SOM（3–5 年） | 能真正交付、接電、上架 GPU 並收到租金／雲費嘅 MW；IREN 官方講 2026 年 480MW、2027 年 1,210MW 在建，但係目標唔係已確認收入 | 把「under contract ARR」當成已入帳營收 |

**管理層 TAM 風險：** IREN 講 5GW 全球 pipeline、$3.1bn ARR under contract、$3.7bn CY26 目標。官方自己註明 $3.7bn **並非全部已簽約**，而且要等 GPU 交付、調試、上線。合理投資口徑係：**已簽約且開始計費嘅 AI Cloud 收入**，而唔係 GW 口號。

## 產業鏈同價值捕獲

1. **電力／接入（grid interconnection）** — 最稀缺、最有護城河；受 ERCOT 大批次審批、電壓／頻率要求、社區同政策影響。
2. **土地＋數據中心殼（powered shell / liquid cooling）** — 資本密集、容易超支延誤；一旦建成轉換成本高。
3. **GPU／ASIC 硬件** — NVIDIA 有定價權；硬件最容易商品化同報廢（IREN Q3 已對 mining 硬件提減值 US$140.4m）。
4. **雲軟件／編排／客戶關係** — 毛利率可以高，但 IREN 仍早期；CRWV 喺呢層領先。
5. **融資（可轉債、GPU lease、客戶預付款）** — 決定邊個先上架；呢層而家決定生死，唔係錦上添花。

| 問題 | 答案 |
|---|---|
| 邊層毛利最高 | 已簽約、高利用率 GPU 雲（IREN AI Cloud 銷貨成本率遠低於 mining） |
| 邊層最易商品化 | ASIC mining、上一代 GPU 租賃 |
| 邊層最有定價權 | NVIDIA、hyperscaler 客戶、電網營運商 |
| 邊層最易形成護城河 | 已接通嘅大規模電力同液冷廠房 |
| 邊層最受周期／CAPEX／政策打擊 | Mining 受 Bitcoin 價；整條鏈受 GPU 供應、利率、ERCOT 規則 |

## 主要 peers 分組

| 分組 | 公司 | 角色 |
|---|---|---|
| 平台型 AI 雲 | CRWV | 純種 neocloud；Q2 2026 營收 US$2.58B、backlog ~US$104B（官方 IR，截至 2026-06-30） |
| 轉型中（mining → GPU 雲） | **IREN** | 已有 Microsoft US$9.7bn、NVIDIA US$3.4bn 官方合約；Q3 FY26 AI 收入仍只 US$33.6m |
| 轉型中（mining → 租賃數據中心） | CLSK、CIFR | CLSK：Sandersville 20 年 US$6.6bn triple-net lease；CIFR：Black Pearl HPC 租賃已開始計租 |
| 純 mining／落後轉型 | MARA、RIOT、HUT | 電力資產有價值，但 AI 合約密度通常低過 IREN |
| 傳統數據中心 | EQIX、DLR | 護城河強、增長慢；唔好同 neocloud 用同一倍數硬比 |

## 商業模式比較（今次四隻）

| | IREN | CLSK | CRWV | CIFR |
|---|---|---|---|---|
| 收費 | Bitcoin 產量＋GPU 雲訂閱／合約 | 仍以 mining 為主，HPC 租賃起步 | GPU 雲 usage／合約 | Mining 收縮，hyperscale 租賃 |
| 客戶 | Microsoft、NVIDIA、Together AI 等 | 租賃租戶＋現貨 BTC | Anthropic、Meta 等企業／模型公司 | 投資級 hyperscale 租戶 |
| 收入可預測性 | 合約 ARR 高、**當期收入仍低** | 低（BTC）→ 租賃後提高 | 高（backlog） | 租賃 NOI 高可見度，當期收入仍細 |
| 毛利結構 | AI Cloud 銷貨成本低；mining 仍佔大部分收入 | Mining 毛利受電費／BTC | 高毛利但利息同折舊很重 | 過渡期 Adj. EBITDA 負 |
| CAPEX | 極高（Q3 單季 PPE＋硬件 > US$1.3B） | 高，但 Sandersville 股權部分稱已籌足 | 極高（FY2026 capex 指引 US$35–39B） | 項目債為主（Stingray US$810m） |
| 第二曲線 | GPU 雲（官方主敘事） | 數據中心租賃 | 已係主業 | 數據中心開發平台 |

## 板塊核心 KPI（8 個）

1. **已計費 AI Cloud／HPC 收入** — 唯一能證明「轉型完成」嘅數字；口頭 ARR 唔算。
2. **Contracted ARR vs 已上線 MW** — 合約係期權，上線先係現金。
3. **GPU 交付／調試進度** — 供應鏈同融資綁死時間表。
4. **客戶集中度** — IREN 對 Microsoft／NVIDIA 極集中。
5. **FCF（OCF − 硬件 − 廠房）** — 轉型期幾乎必然負；要睇燒幾快、靠邊種融資。
6. **淨負債／可轉債／稀釋股數** — 電力再好都會被股本攤薄食咗。
7. **Bitcoin hashrate 同 mining 收入** — 過渡期現金牛定係正在被拆走嘅舊引擎。
8. **電網接入里程碑（substation、ERCOT batch）** — 物理 irreversibility，高過新聞稿。

## 市場三個錯判

1. **把 miner 當 AI 平台股估值。** Trailing P/S 20×（IREN TTM 營收 US$757m）係用未來 ARR 去買而家仍以 Bitcoin 為主嘅損益表。
2. **把 contracted ARR 當成今年盈利能力。** IREN 官方寫明 ARR under contract 包括尚未產生收入嘅 GPU。
3. **忽略融資同報廢。** 正 FCF 嘅 mining 季度，唔代表轉 GPU 之後仍然自我融資；ASIC 減值同可轉債係結構成本。

## 投資行動

- **而家適合搵：** 有**已簽約、可驗證交付**嘅電力資產，而唔係純 hashrate 故事。
- **最值得入 Framework 1：** **IREN**（合約質量最高嘅 miner 轉型股）、**CRWV**（純 AI 雲質量標尺；已過初篩階段）、CLSK（租賃路徑清晰但當期 mining 差）。
- **暫時觀察：** CIFR（HPC 租賃剛開始計租，當期收入同倍數極不相配）；純 mining 冇大型 AI 合約者。
- **若只能深挖一間轉型股：** IREN。合約同官方披露完整度高過 CLSK／CIFR；最大問題係現金流同稀釋，正正係 F1／F2 要驗嘅。

*此分析僅供研究參考，不構成投資建議。*
