---
name: framework-1
description: >-
  Run Serenity Alpha Framework 1 fundamental screening with three fatal
  red-line vetoes and a 13-dimension, 130-point score. Use before deep analysis
  when the user asks for Framework 1, fundamental screening, initial stock
  screening, PASS/WATCH/FAIL, fatal red lines, or whether a stock deserves
  Framework 2 analysis.
---

# Framework 1：基本面初篩

## Purpose

以客觀、量化及 adversarial 的方式，判斷股票是否值得進入 Framework 2。
先做致命紅線掃描；只有完全通過才可進行 13 維度評分。

分析前先讀取 [SCORING.md](SCORING.md)，不可自行增加、刪除或改寫維度。

## Step 1：確認數據

收集並標明來源、日期、幣種及單位：

- 最近季度及 TTM 營收、增速、淨利潤率、自由現金流及 ROE
- 現金、總債務、PEG、P/S 及其他適用估值
- 至少 3 個可比同業的營收及需求 KPI 增速
- TAM 估算及估算方法
- 最近四季 actual vs consensus、guidance 紀錄
- 管理層執行及誠信紀錄
- 公司上市至今與同期 S&P 500 total return

優先採用監管申報、公司財報及官方投資者資料。新聞、sell-side 或市場研究的
估算必須與官方數據分開標示。

## Step 2：致命紅線

依次檢查：

1. **破產／流動性風險**  
   現金低於總債務，並且自由現金流為負。
2. **衰退陷阱**  
   營收增速低於同業平均，並且淨利潤率為負或連續兩季下降。
3. **估值泡沫**  
   PEG > 2.5 或 P/S 顯著高於行業歷史極值，並且缺乏相應高增長支持。

任何一項觸發：

- 立即判定 `FAIL`
- 列出觸發數據、計算及來源
- 停止 13 維度評分
- 提供可量化的重新評估條件

「P/S 顯著高於歷史極值」必須提供公司或可比同業的歷史區間，不可只憑直覺。

## Step 3：13 維度評分

完全按 `SCORING.md` 逐項給予 10、5 或 0 分。

- 客觀指標使用最近季度及 TTM。
- 定性指標必須列出支持及反證。
- 不得把缺失數據當成正面證據。
- 關鍵數據不足時，報告 provisional score，但不可給最終 PASS。
- 總分後按 `SCORING.md` 的門檻判定 PASS、WATCH 或 FAIL。

## Step 4：輸出

使用繁體中文及廣東話語氣，保留 ticker 與英文技術詞。技術縮寫首次出現時寫出
全名。

### Framework 1 初篩結論

- **結果：** PASS / WATCH / FAIL
- **總分：** XX / 130，或因紅線觸發而不評分
- **數據截至：** 日期、主要來源
- **核心結論：** 最大亮點及最大風險各一句

### 致命紅線

逐項顯示：

- 安全／觸發／資料不足
- 使用的數據與計算
- 來源及日期

### 13 維度評分

| 維度 | 實際數據／證據 | 分數 | 評分依據 | 來源 |
|---|---|---:|---|---|
| 逐項列出 |  | 0/5/10 | 一句話 | 日期及連結／文件 |

### Adversarial check

- 最強支持證據
- 最強反證
- 哪一項假設最可能令結論失效

### Decision HUD（互動頁必填；唔改 130 分邏輯）

寫 HTML 時跟 `.cursor/skills/interactive-research-report/DECISION_HUD.md`。F1 通常未有 F3 → HUD 標 **`F3 pending`**：

- 現價（delayed）+ P/S、PEG（若可用）、官方 FCF vs 市值；標明暫定規尺、非 target price
- 3–5 個**估值驅動** KPI（唔係最靚嘅四個數）。例如 TSLA：交付或汽車 GM、FSD 訂閱、官方 FCF、Robotaxi 已入帳／官方英里（標清未入帳）
- 行動第一句引用倍數相對同業／歷史嘅位置；禁止喺 F1 寫建倉區

Markdown 報告亦應有同等「估值驅動 KPI」小節，方便後續頁共用數字。

### 下一步

- `PASS`：列出 Framework 2 必須深挖的兩個問題。用戶其後叫 Framework 2 時，跟 `.cursor/skills/framework-2/SKILL.md`。
- `WATCH`：列出升級至 PASS 所需的量化條件及最近催化日期。
- `FAIL`：列出紅線解除或重新評估的量化條件。

結尾必須包括：

*此分析僅供研究參考，不構成投資建議。*
