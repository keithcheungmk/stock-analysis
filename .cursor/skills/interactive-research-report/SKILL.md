---
name: interactive-research-report
description: >-
  Renders stock research (Thesis Tracker, Framework 1/2, earnings reviews) as
  Claude-style interactive HTML card pages plus matching Canvas and Markdown.
  Use when the user asks for interactive HTML, Claude-style reports, box/card
  layout, thesis tracker UI, evidence cards, filterable evidence, or visual
  research pages instead of plain tables.
---

# Interactive Research Report（Claude 卡片風格）

## When to use

產出 **Thesis Tracker、Framework、earnings review、one-pager** 等研究報告的用戶可視版面時套用。
預設交付：HTML（主視覺）+ Canvas + Markdown。One-pager 用 4 頁投影片翻頁，見 `.cursor/skills/one-pager/SKILL.md`。

## Non-negotiable content depth

1. **Thesis 結論**：至少 **3–4 句**完整解釋（唔好一句收尾）。必須同時寫清：
   - 邊啲支柱／證據正在被驗證
   - 邊條路徑仍未成立
   - 最大裂痕係咩
   - 對行動嘅含義（例如僅觀察／唔好加倉）
2. **證據卡描述**：每張卡 **2–4 句**（約 60–120 字），唔好一句標語。每張須交代：數字含義、對 thesis 邊條支柱、條件／風險或為咩未算通過。
3. **禁止**把「紀錄營收／單季 beat」寫成 thesis 全面通過；稀釋改善流動性 ≠ 經營自我融資。

## HTML layout（Claude box style）

參考範本：`output/RDW_thesis_tracker.html`。

| 區塊 | 規則 |
|---|---|
| 背景 | 淺米色＋輕微 radial 氣氛；白／米白大圓角卡片 |
| Hero | 左：狀態盒（Mixed／PASS／FAIL 色）；右：標題＋行動 badge |
| KPI 列 | 4 個關鍵數字，支持綠／削弱紅／警示橙 |
| Thesis | 獨立 panel；內層 highlight callout（橙底細邊）放 **3–4 段**結論 |
| 支柱 | 彩色左邊框卡片（改善綠、削弱紅）；唔用沉悶大表做主視覺 |
| 證據 | **卡片網格**（非主表）；可篩選：全部／支持／中性／削弱；左色條對應影響 |
| 圖表／裂痕 | FCF 棒圖或同級時間序列；支持 vs 裂痕分欄 |
| 分頁 | **唔用 tabs 隱藏內容**；一次顯示全部主要 section |
| 免責 | 頁尾：僅供研究參考，不構成投資建議 |

### Evidence card 欄位

- 類型（財報／KPI／分部／指引／現金流／資本結構…）
- 影響 pill：支持｜中性｜削弱
- 標題：硬數字 + YoY／對照
- 描述：長文（見上）

## Canvas 同步

路徑：`~/.cursor/projects/.../canvases/{TICKER}-*.canvas.tsx`  
跟 canvas skill：無 gradient／box-shadow／emoji；用 `Callout`／`Card`／`Stat`／左邊框。Thesis 用多段 `Text`；證據 `note` 與 HTML 同等長度。

## 手機要睇到網頁，唔係代碼

GitHub／Cursor 檔案檢視會把 `.html` 當原始碼。真正互動頁靠 **GitHub Pages**（`docs/`）。

寫完 `output/{TICKER}_*.html` 之後必須跑：

```bash
python scripts/publish_html_reports.py
```

呢條指令會複製報告去 `docs/{ticker}/` 並更新 `docs/index.html`。合併到 `main` 之後手機用瀏覽器打開：

https://keithcheungmk.github.io/stock-analysis/

唔好叫用戶喺 GitHub App 入面「打開檔案」嚟睇 HTML。

## Markdown 同步

`output/{TICKER}_YYYY-MM-DD_*.md` 的「結論」同「解讀」欄必須與 HTML／Canvas 同深度，唔好只留短句。

## Official-first

數字優先 `data/raw/{TICKER}/` 同官方 IR；標明期間、幣種、來源。關鍵數字爭議時停 verdict。
