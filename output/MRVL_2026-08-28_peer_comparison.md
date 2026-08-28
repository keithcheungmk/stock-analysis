# MRVL Peer Comparison（同業橫向比較：MRVL／AVGO／NVDA／AMD）

- **數據截至：** 2026-08-28（Asia/Hong_Kong）
- **Peer group：** 沿用 `config/mrvl_cli.yaml` 指定 peers（AVGO、NVDA、AMD），全部屬 AI 基建／半導體賽道但商業模式差異大
- **資料狀態：** NVDA／AMD 引用本倉已有 F1／F3（`NVDA_2026-08-27_framework1.md`／`framework3.md`、`AMD_2026-08-27_framework1.md`／`framework3.md`）；AVGO 本倉未有獨立 F1，數字重新對住官方 2026-06-03 Q2 FY2026 業績稿覆核（Broadcom IR），估值倍數沿用本倉已引用嘅 yfinance TTM P/S（23.4×，同 NVDA／MRVL F1 一致），**AVGO 現價未能喺本輪重新核實**（嘗試查詢嘅報價頁面日期唔可靠），只用相對倍數比較，唔另計 AVGO 自己嘅 Bull/Base/Bear。

## 🧭 Peer Group 一句話結論

四間都食緊 AI 基建呢條大浪，但角色完全唔同：NVDA 係定價者、AVGO 係最賺錢兼最多元化嘅「隱形冠軍」、AMD 係追趕者、MRVL 係體量最細、槓桿最高、custom-silicon thesis 仍未入帳驗證嘅轉折股。市場最容易睇錯嘅地方係將 MRVL 嘅 P/S（23.0×）同 AVGO（23.4×）睇齊，忽略咗 AVGO 嘅盈利質量同資產負債表遠遠強過 MRVL。

## 🧩 可比性判斷

- **可直接比較：** AI 相關收入增速（YoY）、毛利／淨利率方向、現金流轉化能力、P/S 倍數
- **只可參考：** 絕對規模（NVDA／AVGO 市值以萬億美元計，AMD／MRVL 以百億至數千億計，量級唔同）、trailing P/E（GAAP 淨利受一次性項目扭曲程度各異，MRVL／AMD 尤其唔穩定）
- **不宜硬比：** 商業模式——NVDA 係全棧 AI compute 平台（自家 GPU／NVLink／CUDA 生態）；AVGO 係多元化半導體＋軟件（AI 半導體only 係佢幾條業務線之一，仲有網絡、寬頻、VMware 軟件等非 AI 收入做緩衝）；AMD 係 CPU＋GPU 雙引擎追趕者；MRVL 係窄口徑 custom silicon／連接 ASIC 供應商，冇軟件或消費業務分散風險，AI 敘事集中度最高但驗證程度最低。

## 🏷️ 角色定位

| 公司 | 賽道角色 | 商業模式 | 市場通常給的估值語言 | 一句話定位 |
|---|---|---|---|---|
| NVDA | 平台型龍頭 | 全棧 AI compute（GPU＋NVLink＋CUDA 生態） | Forward P/E、EV/Sales | AI 基建嘅定價者，規模最大但增速開始邊際放緩 |
| AVGO | 綜合型成熟大廠 | AI 半導體（custom XPU／網絡晶片）＋軟件（VMware）＋傳統半導體多元組合 | EV/EBITDA、P/S | 最賺錢嘅「隱形冠軍」，AI 引擎增速最快兼有非 AI 業務緩衝 |
| AMD | 挑戰者／追趕者 | EPYC 伺服器 CPU＋Instinct AI 加速器雙引擎 | Forward P/E、PEG | 份額提升故事已部分兌現，但估值已跑贏自身 Base 情景 |
| MRVL | 轉折股／敘事股 | 窄口徑 custom silicon／連接 ASIC（單一大客戶 Google TPU-attach 敘事） | P/S、PEG | 體量最細、槓桿最高，custom thesis 高上限但未入帳驗證 |

## 📊 同業核心比較表

| 公司 | 商業質量 | 增長質量 | 現金流質量 | 估值吸引力 | 最大亮點 | 最大風險 |
|---|---|---|---|---|---|---|
| NVDA | 高——75% GAAP 毛利率、Data Center 單季 US$89.0B | 高——DC +117% YoY，但 DSO 由 45 日拉到 60 日 | 高——TTM 官方 FCF US$126.9B，惟 Q2 FCF 對 Q1 腰斬（US$21.3B vs US$48.6B） | 中高——F3 Base US$300 對現價 US$209.66 有顯著折讓 | AI compute 定價者，規模效應同生態壁壘最強 | 客戶集中（5 大客戶佔應收 70%）、ASIC 競爭、PORTS 擔保把公司綁入單一場地/客戶 |
| AVGO | 高——GAAP 淨利率 41.9%，遠超其餘三間 | 高——AI 半導體 +143% YoY，Q3 guide 再加速至 >200% YoY 至 US$16.0B | 高——單季 FCF US$10.26B，OCF／FCF 轉化率接近 100% | 中——P/S 23.4×（yfinance TTM）同 MRVL 相若，但盈利質量遠勝，現價本輪未獨立核實 | 非 AI 業務（軟件／網絡／寬頻）提供收入緩衝，AI 半導體增速全組最快 | 高槓桿（總債務 US$64.9B）、VMware 整合風險、對現價嘅獨立驗證本輪不足 |
| AMD | 中高——Data Center +107% YoY，GAAP 淨利率約 20% | 高——但 F2 顯示 Helios／FCF margin 部分通過（Q2 FCF margin 回落至 14%） | 中——Q2 FCF US$1,558m，margin 14%，唔算穩定 | 低——現價 US$480.93 對自身 F3 Base US$390 有 **+23% 溢價**，估值已偏貴 | EPYC CPU 份額持續搶佔 Intel，AI 加速器第二供應商敘事漸兌現 | Helios 新平台出貨節奏、CUDA 生態壓力、現價已跑贏基本面 |
| MRVL | 中——Data Center +46% YoY（Q2 FY27），但 GAAP 淨利率五季波動大（1.4%→11.2%） | 中——F2 判定「部分通過」，custom／Google 敘事未入帳 | 中低——官方 FCF 正但無單調上升（US$259m–US$509m／季），現金仍低過總債 US$1.03B | 中——P/S 23.0× 同 AVGO 相若，但盈利質量／資產負債表明顯較弱，PEG 1.45 貴過 AVGO 隱含（yfinance PEG 0.40）／NVDA（0.59） | Google warrant 覆蓋 TPU 生態多條 attach 產品，理論上限對應 US$120B 累計 Custom Products 收入 | 現金低於債務未解決（F1 紅線 1 觀察）、diluted 股數擴張快過 FCF、custom 收入仍未有已入帳數字驗證 |

## ⚖️ 誰該享有溢價

- **AVGO 最值得 higher multiple：** GAAP 淨利率 41.9% 係四間之冠，AI 半導體增速（+143% YoY，guide 再加速）同 NVDA／AMD Data Center 相若甚至更快，但盈利質量同 FCF 轉化遠勝，卻用同 MRVL 相近嘅 P/S 定價——結構性睇，AVGO 而家嘅倍數相對佢嘅質量偏低。
- **MRVL 睇似同 AVGO 打平，但折價有其合理性：** P/S 相若唔代表質量相若——MRVL 現金低過債、GAAP 淨利率波動大、custom 敘事未有已入帳數字，折價（相對佢應有嘅倍數）合理。
- **AMD 最容易被市場過度追捧：** 現價已經跑贏自身 F3 Base 情景 23%，Helios 出貨仍待驗證，呢種「先畀晒溢價，後兌現」嘅定價方式，一旦 Helios 延遲最容易被重新定價。

## 🥇 投資排序

1. **第一名：AVGO** — 全組最高 GAAP 淨利率（41.9%）、最快 AI 半導體增速（+143% YoY，guide 再加速至 >200%）、非 AI 業務分散風險，而估值倍數同體質最弱嘅 MRVL 相近，相對質量嚟講最有吸引力（惟現價本輪未獨立核實，實際入場價要另行confirm）。
2. **第二名：NVDA** — 規模同生態壁壘最強，F3 Base 對現價有顯著折讓（PASS 115/130，全組最高分），但客戶集中同 DSO 惡化係要持續盯嘅裂痕。
3. **第三名：AMD** — Data Center 增長質量紮實（PASS 95/130），但現價已跑贏自身估值模型 Base 23%，短期唔算好嘅入場點。
4. **第四名：MRVL** — 增長故事（Data Center +46%、Google warrant 高上限）真實但未驗證，現金結構最弱（F1 紅線 1 未解決），四間之中風險回報最唔對稱，屬觀察名單而非核心持股。

## 🎯 配置建議

- **核心持股首選：** NVDA——規模、生態、F3 折讓兼備，適合長線核心持股。
- **進攻型配置首選：** AVGO——AI 半導體增速全組最快，若現價經獨立核實後仍有折讓，進攻型配置吸引力最高。
- **估值／值博率最佳：** NVDA（F3 Base 對現價折讓最明確、有本倉完整驗證嘅估值模型撐住）。
- **只宜觀察、不宜追高：** AMD（已跑贏自身 Base）同 MRVL（thesis 未驗證、槓桿未解決）。
- **若只能選一間長持：** **NVDA**——原因係四間入面淨係佢有本倉完整、近期覆核過嘅 F3 模型清楚顯示現價對 Base 有折讓，兼且商業質量（毛利率、生態壁壘、規模）四間最強，AVGO 雖然質量同樣吸引但本輪冇獨立驗證現價，唔可以喺冇核實估值嘅情況下定為首選長持。

## 💡 顧問下一步建議

- **AVGO 最值得進一步做完整 Framework 1／3**——本輪淨係用官方 Q2 FY2026 業績稿覆核咗基本面，冇做紅線評分同獨立估值模型，而佢嘅質量／估值錯配睇落最值得深挖。
- **MRVL 最值得留意 Skill 5 Catalyst Calendar**（下一份交付）——custom／Google 收入何時開始入帳將直接改變佢喺呢個排序入面嘅位置。
- 若想再細化 NVDA／AMD／MRVL 估值敏感度，可以喺各自 F3 基礎上加一頁互動 valuation-model.html（NVDA／MRVL 已有／將有）。

*此分析僅供研究參考，不構成投資建議。*
