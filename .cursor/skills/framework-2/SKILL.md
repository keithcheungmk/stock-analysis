---
name: framework-2
description: >-
  Run Framework 2 five-quarter growth-quality analysis. Answer the two
  questions Framework 1 listed, score five dimensions as 通過 / 部分通過 /
  未通過, and write confirmation versus invalidation tests. Use when the
  user asks for Framework 2, 深度增長, time-series quality, unit economics,
  FCF path, or whether a PASS/WATCH name deserves Framework 3.
---

# Framework 2：深度增長質量

## Purpose

唔再打分 130 分。用**最近五個已公布季度**驗證成長係咪真、單位經濟係咪改善、現金流係咪跟住收入走。
只深挖 Framework 1 列出嘅 **兩條必挖問題**（可再加用戶今次指定嘅第三條）。唔重跑紅線計分，亦唔做估值區間（交 Framework 3）。

分析前讀 [DIMENSIONS.md](DIMENSIONS.md)，唔好自創維度或改「通過／部分通過／未通過」用語。

## When

- 用戶講 Framework 2、深度增長、時間序列、單位經濟、FCF 路徑
- F1 已 PASS／WATCH，問值唔值得入 Framework 3
- F1 FAIL 但用戶仍要深挖執行拐點（例如 RDW）→ 可以跑，但開頭必須寫明紅線已 FAIL，F2 唔翻案

唔用嚟做：Skill 0 賽道、F1 13 維評分、F3 target price、期權、one-pager。互動頁仍要有 Decision HUD（`F3 pending` 倍數尺），但**唔准**喺 F2 計出 Bear／Base／Bull 目標價。

## 開工前

1. 讀最新 `output/{TICKER}_*_framework1.md`。冇 F1 → 停，叫用戶先跑 Framework 1（AGENTS.md：一次一個 Skill）。
2. 抽出 F1「下一步」嘅兩條必挖問題。冇寫明 → 用 F1 adversarial 最易失效假設拆成兩條可量化問題，並標「由 F1 裂縫推斷」。
3. 官方數據：`data/raw/{TICKER}/` manifests。持倉另跑 coverage-config。Cloud 冇 raw 就用 catalog／SEC 重建，同 F1 一樣。
4. 五季窗口：最近五個**已公布**財政季度，用公司自己嘅 fiscal label（例如 NVDA `FY2026-Q2`）。缺季就留空並寫原因，唔好用 yfinance 填洞。

## Step 1：數據同核心 KPI

每個問題揀可驗證 KPI。成份報告 **8–12 行** 五季表，必須包括：

- 總營收同 YoY
- **一條需求 KPI**（對應商業模式：Data Center 收入、backlog、subscribers、已入帳 AI 收入…）
- 毛利率或最能代表單位經濟嘅 margin
- OCF 同官方定義 FCF（公司點定義就點用；自行 OCF−PPE 要寫明）
- 現金或稀釋（股數／債務／股本融資）— 若 F1 裂縫涉及流動性或回購／發債

禁止：把 contracted ARR、指引、訂單意向當成已入帳收入；把融資現金當成經營自我融資。

五季表須標明邊 3–5 行係 **估值驅動 KPI**（後續 F3／HUD 用呢批，唔另揀靚數）。互動頁跟 `.cursor/skills/interactive-research-report/DECISION_HUD.md`：現價 + `F3 pending` 倍數尺 + 呢 3–5 個 KPI；行動第一句引用倍數位置。

## Step 2：回答兩條必挖問題

用表：問題 | 發現（硬數字 + 五季方向 + 來源）。
每條發現要寫清：而家證明到邊一步、仲差邊個可驗證門檻。

## Step 3：五大維度

按 `DIMENSIONS.md` 逐項判定 **通過 / 部分通過 / 未通過**，各附一句證據。唔好全部「部分通過」充數；現金流同單位經濟尤其要硬。

## Step 4：判定同行動

總判定拆條，唔好一句「整體通過」掩蓋裂縫。格式：

- `{主業／增長} thesis` 通過｜部分通過｜未通過
- `{現金流／稀釋／價格紀律}` 通過｜部分通過｜未通過

行動只准：`僅觀察`、`續抱`、`唔好加倉`、`加入觀察名單`。冇用戶確認持倉，唔好寫加倉／減倉。

## Step 5：確認／失效

各 2–4 條，必須可量化、有時間窗（下兩季／下一次指引）。禁止空話「執行變差」。

交貨前若距 F1 已超過 7 日，跑 `.cursor/skills/x-adversarial-review/SKILL.md` 再出 memo。

## 產出

繁體中文、廣東話語氣；ticker 同技術詞保留英文；縮寫首次寫全名。

寫入 `output/{TICKER}_{YYYY-MM-DD}_framework2.md`。用戶要互動頁就跟 interactive-research-report（含 `DECISION_HUD.md`），參考 `output/IREN_framework2.html` 或 `docs/spcx/framework2.html`。

### 必備區塊

```markdown
# {TICKER} Framework 2 深度增長分析

- **判定：** … thesis 通過／部分通過／未通過；現金流／… 通過／部分通過／未通過
- **行動：** …
- **五季窗口：** …
- **數據截至：** …
- **核心 KPI：** …（一句定義，避免用錯代理變數）

## 一句結論
（業務拐點 + 未通過嘅硬約束，各半句）

## 承接 Framework 1
| 必挖問題 | 發現 |

## 8–12 KPI 五季摘要
（缺數留空 + 註；標明估值驅動列）

## Decision HUD（F3 pending 或引用已有 F3）
現價 · 倍數尺或 vs Base · 3–5 驅動 KPI

## 五大維度
1. 敘事 2. 單位經濟 3. 護城河 4. 營運槓桿 5. 現金流

## Bull / Bear / 行動

## 確認／失效

互動報告：`output/{TICKER}_framework2.html`（若有）
```

結尾：*此分析僅供研究參考，不構成投資建議。*

### 下一步

- 增長質量至少一條主線 **通過** 或 **部分通過**，且現金流唔係唯一仍未 dig 嘅未知 → 可入 Framework 3。
- 兩條必挖都 **未通過** → 唔入 F3；列可量化重跑條件。
- 列出 F3 最敏感嘅 1–2 個變數（收入、margin、FCF 或 multiple），唔好當場計 target price。估值驅動 KPI 清單交俾 F3 做 SOTP／倍數敏感度，數字必須同 F2 五季表一致。
