# IREN Framework 1 初篩報告

- **結果：** FAIL（致命紅線 1 觸發，停止正式 13 維度評分）
- **總分：** 不評分（紅線否決）
- **非正式參考分：** 55 / 130（僅供 F2 討論，**唔係**正式 PASS／WATCH 分數）
- **數據截至：** 2026-08-15
- **最新官方季度：** FY2026-Q3（期終 2026-03-31，USD，US GAAP，unaudited；SEC 8-K EX-99.1，2026-05-07，`validation_status: verified`）
- **現價：** US$44.06（yfinance delayed，2026-08-14 close，America/New_York）；市值約 US$15.75B；流通／已發行約 357.4M 股
- **持倉（用戶今次確認）：** 1,080 股，成本約 US$60（浮虧約 27%）
- **核心結論：** 最大亮點係 Microsoft US$9.7bn 同 NVIDIA US$3.4bn 已喺官方 8-K 確認；最大風險係現金 US$2.21B 低於有息負債約 US$3.96B，而且單季 FCF 約 −US$1.28B。

## 數據驗證

- `validate_raw_manifests.py --coverage-config config/official_sources.yaml`：通過（137 manifests）
- IREN 六季包：6/6 complete；22 verified official files；`pending_sources: 0`；`unavailable_sources: 12`（多數係官方 transcript 同 optional financial tables）
- FY2025 早期季曾用 IFRS；FY2025-Q4 起 10-K／8-K 以 US GAAP 為準。**IFRS 同 US GAAP 唔好直接串成一條趨勢。**
- 電話會議逐字稿 `source_tier: unverified`，唔覆寫官方數字。
- Microsoft 合約：官方 Q1／Q3 FY26 8-K 已寫「US$9.7bn contract with Microsoft」。`_unsorted` 簡報原先 unverified，**而家以 8-K 為準，當作官方事實。**

## 致命紅線

### 1. 破產／流動性風險：**觸發**

條件：現金低於總債務，**並且**自由現金流為負。

| 項目 | 數字 | 來源 |
|---|---:|---|
| 現金及等價物 | US$2,213.3m（2026-03-31） | 官方 8-K EX-99.1 |
| 其後現金（未經審計） | US$2.6bn（2026-04-30） | 同一份 8-K 附註 4 |
| 可轉債 | US$3,687.8m | 官方資產負債表 |
| 融資租賃（流動＋非流動） | US$274.3m（122.2+152.1） | 官方資產負債表 |
| 有息負債合計 | 約 US$3,962m | 以上加總 |
| yfinance totalDebt | US$3.96B | 延遲彙總，同官方方向一致 |
| Q3 經營現金流 | US$75.3m | 官方現金流量表 |
| Q3 PPE 支出 | US$949.2m | 官方現金流量表 |
| Q3 硬件支出 | US$406.1m | 官方現金流量表 |
| Q3 FCF（OCF−PPE−硬件） | 約 **−US$1,280m** | 研究計算 |

現金 US$2.21B < 有息負債 US$3.96B，FCF 大額為負 → **紅線 1 觸發 → FAIL。**

語境（唔改變規則）：短期流動資產 US$2.42B > 流動負債 US$651m；負債主體係可轉債同增長 capex，唔係即時銀行擠兌。但 Framework 1 規則係機械否決，唔可以「因為係成長股」豁免。

**重新評估條件：** 現金（含等價物）至少等於有息負債，**或** 季度 FCF 轉正（同一會計基礎）。預計要等 AI Cloud 開始大規模計費，或者大幅再融資／NVIDIA US$2.1bn 認股權實際行使。

### 2. 衰退陷阱：**安全**

條件：營收增速低於同業平均，**並且**淨利率為負或連續兩季下降。

- IREN Q3 FY26 總營收 US$144.8m，對上一年同期 US$144.8m（FY2025 10-K 季度表）→ **YoY 約 0%**
- CLSK FY2026-Q3（期終 2026-06-30）營收 US$138.0m，YoY **−30.5%**（官方 8-K，2026-08-06）
- CIFR 2026-Q2 營收 US$24.8m，YoY 明顯倒退（官方 8-K／業績稿）
- CRWV 2026-Q2 營收 US$2,575m，YoY **+112%**（官方 IR，2026-08-11）

對 **miner 轉型組**（CLSK／CIFR），IREN 增速唔低於同業。淨利率 Q2、Q3 連續虧損，但紅線要兩項同時成立。第一項未成立 → **不觸發。**

### 3. 估值泡沫：**未否決**

- yfinance PEG 3.11 > 2.5，但 Forward P/E 為負，盈利被 Q1 未實現金融工具收益嚴重扭曲，PEG **不可靠**
- Trailing P/S 約 20.8×（市值 US$15.75B / TTM 營收 US$757m）
- 同業：CLSK 約 4.6×、CRWV 約 7.6×、CIFR 約 38.8×（yfinance TTM，2026-08-14）
- IREN 官方 contracted ARR US$3.1bn（尚未全部計費）。用呢個前瞻口徑，P／ARR 約 5×，**有高增長敘事支持**，唔構成「無增長硬泡沫」機械觸發

P/S 高過 CLSK／CRWV，但 CIFR 更高，而且有官方大型合約 → **紅線 3 不觸發。**

## 非正式 13 維度（紅線後僅供討論）

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 現金 vs 債務 | 現金 US$2.21B < 有息負債 US$3.96B | 0 | 現金低於債務 | 8-K 2026-05-07 |
| 營收增長 | Q3 YoY ~0%；AI Cloud +833% YoY（33.6 vs 3.6） | 5 | 總營收持平，結構改善；未拋離 10pp | 8-K；FY25 10-K 季度表 |
| 淨利潤率 | Q3 −171%；TTM ~21% 被 Q1 未實現收益扭曲 | 0 | 近兩季 GAAP 虧損 | 8-K |
| 估值（PEG） | PEG 3.11 不可靠；P/S 20.8× | 0 | 估值透支 trailing 盈利 | yfinance 2026-08-14 |
| TAM | AI 基礎設施 > US$100B | 10 | 可觸及市場夠大 | Skill 0 |
| 需求 KPI（AI Cloud 收入） | US$7.0 → 7.3 → 17.3 → 33.6m；ARR 合約 US$3.1bn | 10 | 遠高過 miner 同業需求 | 官方 8-K |
| ROE | 約 7.7%（yfinance）；近季虧損 | 0 | 低於 8% | yfinance；8-K |
| 自由現金流 | Q1〜Q3 FCF 皆負，Q3 約 −US$1.28B | 0 | 不穩定且為負 | 官方現金流量表 |
| 護城河 | 已接電廠房＋MSFT／NVIDIA 合約；客戶極集中 | 5 | 有壁壘但非壟斷 | 8-K |
| 行業趨勢 | AI 算力短缺 | 10 | 核心主線 | 官方業務描述 |
| 管理層 | 簽到超大型合約；同時大額減值、稀釋、可轉債 | 5 | 有成果，資本紀律有爭議 | 8-K |
| 相對 S&P 500 | 上市以來約 +80% vs SPY +77%（2021-11-17 起） | 5 | 累計跑贏 0–20pp | yfinance |
| 預期 vs 實際 | Q3 總營收連跌；AI 超預期、mining 主動拆產能 | 5 | 結構轉型令 headline 難用 beat／miss | 8-K；共識資料不足 |

非正式合計 **55 / 130**（FAIL 區間）。即使豁免紅線，分數都未到 WATCH（65）。

## Adversarial check

- **最強支持：** 官方 Microsoft US$9.7bn、NVIDIA US$3.4bn、5GW NVIDIA 合作；AI Cloud 收入兩季翻倍；Q3 Adj. EBITDA 仍有 US$59.5m（margin 41%）。
- **最強反證：** 現金少於可轉債；Q3 FCF −US$1.28B；總營收因為拆 ASIC 而下跌；GAAP 連虧；股數同可轉債持續擴張。
- **最易令結論失效：** GPU 交付／Childress Horizon 延誤，令 contracted ARR 無法喺 2026 下半年開始計費，同時 mining 現金牛已經拆走。

## 下一步

紅線 FAIL 嘅量化解除條件：

1. 季度現金 ≥ 有息負債，**或**
2. 單季 FCF ≥ 0（OCF − PPE − 硬件，同一 US GAAP 口徑）

非正式分數要升到 WATCH（≥65），至少還要：淨利率或 ROE 其中一項脫離 0 分，或者 trailing 估值不再用 20× P/S 買仍以 Bitcoin 為主嘅損益表。

按你要求全套繼續：Framework 2 會深挖（1）AI ARR 有幾多已經變成現金收入；（2）FCF／稀釋路徑。

互動報告：`output/IREN_framework1.html`

*此分析僅供研究參考，不構成投資建議。*
