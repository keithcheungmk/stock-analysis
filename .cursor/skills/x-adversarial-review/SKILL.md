---
name: x-adversarial-review
description: >-
  Pre-delivery adversarial fact-check gate: refresh company IR / SEC for latest
  developments, then scan X (Twitter) for progress claims and disconfirming
  narrative. Patches stale catalysts before the user-facing summary. Use after
  Framework / Skill drafts are written and before final chat delivery; also when
  the user asks for X review, IR refresh, fact-check latest progress, or
  adversarial pass on a research package.
---

# X／IR Adversarial Review（交付前閘）

## Purpose

喺交用戶總結之前，做一次**對抗式新鮮度覆核**：

1. **官方 IR／SEC**：公司最新發展有冇令報告過時  
2. **X（Twitter）**：市場最新進度敘事、反證、催化劑噪音  

呢一閘**唔取代** `data/raw` 官方數字；係防止「交貨時仍寫未交割／未發生」類錯誤（例如 Cursor 已交割但仍寫「預期 Q3」）。

## When（必須跑）

- 全套分析（Skill 0→one-pager）寫完、**chat 最終總結之前**
- 用戶要求：X review、IR refresh、fact-check latest、adversarial pass
- 更新 one-pager／catalyst／thesis 前若距上次覆核超過 **7 日**，再跑一次

## Non-negotiable evidence order

1. SEC／官方 IR／公司新聞稿（可寫入 `data/raw/{TICKER}/`）  
2. 官方 earnings materials 已驗證 manifests  
3. 具名可靠行業報導（只作交叉）  
4. **X 帖文** — 一律 `unverified` 研究線索，**不可覆寫**官方財務數字  

若 X／網媒同官方衝突：保留官方，並列衝突；關鍵數字爭議則**停 verdict**。

## Checklist（複製追蹤）

```
- [ ] Step 0: Scope（ticker、報告 as-of、覆核時區）
- [ ] Step 1: IR／SEC latest developments
- [ ] Step 2: X latest progress + adversarial scan
- [ ] Step 3: Diff vs drafted reports（過時／遺漏／衝突）
- [ ] Step 4: Patch deliverables（MD／HTML／Canvas）
- [ ] Step 5: Emit Review Memo；先交用戶
```

### Step 0：Scope

記錄：

- Ticker、公司正式名、IR URL（`config/official_sources*.yaml` 或公司 IR）
- 研究報告 `as_of` 日期
- 覆核時間（Asia/Hong_Kong）同 freshness 窗口：**自上份已分析財報期終日起**，至少再掃 **最近 14 日** 事件

### Step 1：IR／SEC latest（必做）

最少做齊：

1. 打開公司 **Investor Relations**（新聞／releases／events／filings）  
2. 查 SEC submissions／近期 **8-K、6-K、S-1/A、424B、10-Q/K** 有冇報告未寫嘅事件  
3. 對住草稿嘅 **Catalyst／Thesis／One-pager** 逐條問：狀態仍係「預期／未發生」定已完成／告吹／延期？

**必擷取嘅發展類型：** 併購交割／告吹、鎖定期、重大合約、指引更新、股數／稀釋、產品里程碑（如 Starship）、監管裁決、分拆／債券／二次發行。

若發現新官方文件：下載入 `data/raw/{TICKER}/`（合適 period 或 `_events/`），寫 manifest，`source_tier: official`，再跑：

```bash
source .venv/bin/activate
python scripts/validate_raw_manifests.py --root data/raw
```

持倉六季包股票另加 coverage-config（見專案規則）。

### Step 2：X latest progress（必做；工具降級可接受）

目標：**fact-check 目前為止最新進度敘事**，同搵反證——唔係做情緒儀表板。

**搜尋優先序：**

1. 公司官方／IR 相關 handle（若有 `config/{ticker}_x_accounts.yaml` 或本 skill 附錄）  
2. CEO／主要發言人（高噪音；需官方交叉）  
3. 關鍵字：`{TICKER}`、公司名、核心 KPI 詞（如 Starlink、Starship）、草稿 catalyst 專名（如 Cursor）  
4. 對抗詞：lockup、dilution、miss、delay、capex、lawsuit、SEC、investigation（只當線索）

**每條採納規則：**

| 標籤 | 條件 | 用途 |
|---|---|---|
| `confirmed` | 其後／同時有官方 IR／SEC 證實 | 可更新報告狀態 |
| `narrative` | 合理但未證實 | 只寫入 Review Memo／市場在賭什麼 |
| `noise` | 無日期、無來源、純情緒／政治玩笑 | 丟棄 |

限制：摘要 **≤ 8 條** 有用項目；標 handle、日期／大約時間、一句內容、標籤。

**無 X API／登入時：** 用公開 web 搜尋 `site:x.com`／新聞轉述 X 帖，並喺 Memo 寫明 `x_access: degraded`。**唔可以**因為無 API 就跳過整閘——IR／SEC 步仍然強制。

### Step 3：Diff vs 草稿

對每個 material claim 標：

- `OK` — 仍然正確  
- `STALE` — 狀態已變（必須改報告）  
- `MISSING` — 新發展未寫入  
- `CONFLICT` — 來源互斥（停 verdict 或降級）  
- `LEAD_ONLY` — 僅 X／傳聞  

**典型 STALE：** 「預期交割」但其實已交割；「未公布」但其實已出 8-K；用戶數／指引已被更新。

### Step 4：Patch before delivery

`STALE`／`MISSING`（官方證實）→ **先改** 相關：

- `output/{TICKER}_*_catalyst*.md`／thesis／earnings／sector  
- 對應 HTML（如有）  
- Canvas：尤其 **one-pager 催化劑頁**、catalyst-calendar、thesis-tracker  

唔好只喺 chat 口頭更正而檔案仍錯。

### Step 5：Review Memo（交用戶前必出）

繁中，短篇：

```markdown
# {TICKER} Adversarial Review Memo
- 覆核時間：（Asia/Hong_Kong）
- IR／SEC：掃過邊啲頁／accession；有／無新事件
- X：x_access=full|degraded；≤8 條摘要（標籤）
- Diff：OK / STALE / MISSING / CONFLICT 列表
- 已 patch 嘅檔案路徑
- Verdict impact：維持 / 微調文字 / 停 verdict
```

然後先出用戶總結。結尾仍要：*此分析僅供研究參考，不構成投資建議。*

## Do not

- 用 X 帖覆寫營收、利潤、現金、用戶等官方數字  
- 無 IR／SEC 掃描就宣稱「已 fact-check」  
- 把 degraded X 搜尋包裝成「已完整監察 X」  
- 為通過閘而忽略明顯 STALE catalyst  
- 索引或暴露 `stock-analysis-private/`

## Wire-in

`stock-analyst` 全套流程：one-pager 完成後、最終 chat 前，必須跑本 skill。

## Account hints（可擴）

可選 `config/{ticker}_x_accounts.yaml`（參考 `config/tesla_x_accounts.yaml`）。SPCX 起步建議追：官方 SpaceX／Starlink／IR 相關帳、主要管理層發言；一律高噪音過濾。
