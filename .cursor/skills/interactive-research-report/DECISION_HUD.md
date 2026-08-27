# Decision HUD — KPI 對住估值（買賣前必睇）

所有寫入 `docs/{ticker}/*.html` 嘅互動頁都要有呢條尺。Interactive Brief 係合成頁，**唔係唯一**放 HUD 嘅地方。估值權威來源係 Framework 3；未有 F3 就標 `F3 pending`，禁止假裝有 target price。

寫 HTML 前讀本檔。版面風格仍跟 [SKILL.md](SKILL.md)。

## 點解要有

買賣／僅觀察唔可以只靠敘事或單季 beat。用戶要喺每頁頂部同時見到：

1. 現價（delayed）對住估值區間
2. 邊 3–5 個官方 KPI 會郁呢個區間

## 必有四欄（順序固定）

放喺 Hero／狀態盒**之後**、行動 badge **之前**（或同一 vis 帶內：左狀態、中 HUD、右先唔放行動）。行動第一句必須引用 HUD 嘅溢價／折讓。

| 欄 | 未有 Framework 3（`F3 pending`） | 已有 Framework 3 |
|---|---|---|
| 現價 | delayed／previous close、日期、時區 | 同上 |
| 估值尺 | **唔寫** Bear／Base／Bull 目標價。改用官方可核對倍數：P/S、PEG（若 EPS 可用）、FCF yield 或官方 FCF vs 市值。標明「暫定規尺，非 target price」 | 現價 vs Bear／Base／Bull（每股或市值，同 F3 單位一致） |
| 溢價／折讓 | 相對同業或公司自身歷史倍數（一句 + 來源） | **現價相對 Base 嘅 %**。買／賣／僅觀察嘅第一句必須引用呢個數 |
| 估值驅動 KPI | 3–5 個；見下 | 必須係 F3 敏感度用嗰批，數字同 F3／當季官方包一致 |

## 估值驅動 KPI（3–5 個）

每個 KPI 寫：最新官方數、財政期、方向（改善／惡化／持平）、**點樣郁倍數或 SOTP**、來源。禁止用 contracted ARR、指引、未入帳英里當成已入帳收入。

揀 KPI 用商業模式，唔好用「最靚嘅四個數」：

| 類型 | 優先驅動（例） |
|---|---|
| 賣車 + AI 可選性（TSLA） | 交付或汽車 GM／ASP、FSD 訂閱、官方 FCF（OCF−capex）、Robotaxi 已入帳收入或官方付費英里（標清未入帳） |
| 訂閱／連接 | 用戶、ARPU、分部營業利潤、官方 FCF |
| 多分部平台 | 各分部已入帳收入 + 合計 FCF |
| 未盈利高增長 | 已入帳收入增速、毛利率軌跡、現金消耗 |

TSLA 另讀 `docs/TESLA_AI_FRAMEWORK.md`：HUD 可加爆發定義 C 兩欄（EPS beat>15%｜3 個月股價>+30%），**唔合併**成一個看多分，亦唔代替估值尺。

## 數字一致性

- 同一 ticker、同一數據截止日：各頁 HUD 嘅現價、Base、溢價 %、KPI 必須相同。F3 完成後，回頭把 `F3 pending` 頁換成正式區間。
- 官方 IR／SEC > 簡報 > 第三方 > yfinance。yfinance 只用於現價同共識；衝突就表列並棄用 aggregator。
- 關鍵數爭議 → 停 action badge，HUD 寫「估值尺暫停」。

## 互動估值頁（`valuation-model.html`）

有 F3 就應有一頁可調驅動 KPI 嘅模型（參考 `docs/spcx/valuation-model.html`）：官方錨點 → 滑桿 → 重算 vs 現價。HUD 嘅 Base／Bull／Bear 必須同呢頁預設情景一致。

## Interactive Brief

`output/{TICKER}_interactive_brief.html` 係 Skill 9 + 本 skill 嘅合成投影片，**唔另估倍數**。Brief 必須重用 F3 HUD；未有 F3 就整頁標暫定。唔好把 Brief 當成獨立研究 Skill。

## 禁止

- 未有 F3 就寫「合理價值 US$xx」或建倉區
- 行動 badge 出現喺 HUD 之前，或行動句唔提溢價／折讓
- 各頁 HUD 用唔同現價日期或唔同 Base
- 用第三方 transcript 覆寫官方 KPI
