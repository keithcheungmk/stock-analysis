# Tesla AI 分析框架 v2

> 定位：Tesla 作為「AI 實體世界」股票，追蹤 Robotaxi、Optimus 與 FSD，
> 並分開評估 **EPS 爆發** 與 **股價爆發**。

**已確認設定（2026-06-29）**
- X：**輕量** — 只追 Elon + Tesla 官方，每週 ≤5 條摘要
- 爆發定義：**C** — EPS beat >15% 與 3 個月股價 >30% **分開報告**
- 同業：**A** — 5 間 Robotaxi + 5 間 Humanoid，一頁精簡表

---

## 1. 價值四層（Value Stack）

| 層級 | 內容 | 主要 KPI | 爆發類型 |
|------|------|----------|----------|
| **L1** 汽車 + 能源 | 現金流基本盤 | 交付、ASP、汽車毛利、儲能增速 | EPS |
| **L2** FSD / AI 軟件 | 數據飛輪 | 訂閱滲透、版本、監管、軟件收入 | EPS → 敘事 |
| **L3** Robotaxi | 第一個大規模 AI 變現 | 城市、車隊、無安全員、單英里經濟 | 股價 → EPS |
| **L4** Optimus | 長期期權 | 階段、內部部署、成本曲線 | 股價 |

---

## 2. 情報四線（Intelligence Feeds）

### 2.1 Earnings Call Transcripts（骨幹 · 高信噪）

- **頻率**：每季必跑
- **做法**：關鍵詞抽取 + **QoQ 用詞 diff**（唔只摘錄）
- **追蹤詞庫**：robotaxi, FSD, Optimus, margin, guidance, regulatory, fleet, deployment, subscription, defer
- **映射**：L1–L4 全層；EPS 爆發最主要來源

### 2.2 X 輕量（領先 · 需驗證）

- **帳號**：見 `config/tesla_x_accounts.yaml`
- **頻率**：每週 ≤5 條摘要
- **分級**：
  - `confirmed` — 其後財報/官方證實
  - `narrative` — 敘事升溫，未證實
  - `noise` — 忽略，不計入 Catalyst Score
- **規則**：單獨 X 帖 **不可** 作為交易依據；只餵 `confirmed` + 高質素 `narrative` 入評分

### 2.3 同業精簡表 A（相對進度）

- **Robotaxi ×5**：見 `config/tesla_peers.yaml`
- **Humanoid ×5**：見 `config/tesla_peers.yaml`
- **頻率**：每月更新一頁表（里程碑一句 + 最後更新日期）
- **用途**：Tesla 領先/落後 → 估值敘事壓力，唔直接預測 EPS

### 2.4 外部 CEO 發言（板塊放大器）

- **首選**：Jensen Huang（GTC、NVDA 財報）— Physical AI、推理成本、capex
- **頻率**：每季一節，只摘與自駕/機器人/邊緣 AI 相關句
- **映射**：L2 為主，間接 L3/L4；解釋 **板塊同步波動**，非 Tesla 專屬催化劑

---

## 3. 爆發定義 C（分開報告）

### 3.1 EPS 爆發

| 條件 | 說明 |
|------|------|
| 觸發 | 單季 EPS vs consensus **beat > 15%** |
| 數據源 | 財報、yfinance、共識預期（需標註來源） |
| 常見驅動 | 交付 beat、毛利 inflection、FSD/能源收入、一次性項目（要剔除） |

### 3.2 股價爆發

| 條件 | 說明 |
|------|------|
| 觸發 | **3 個月**總回報 **> +30%** |
| 數據源 | 歷史收盤價 |
| 常見驅動 | Robotaxi/Optimus 里程碑、監管批准、Elon 敘事、AI 板塊 beta |

### 3.3 報告呈現

- 結論 **兩欄**：`EPS 爆發壓力` | `股價爆發壓力`
- 唔合併成一個「看多/看空」分數

---

## 4. Catalyst Score（0–10，每維度獨立）

| 維度 | 含義 |
|------|------|
| `eps_upside` | 未來 1–2 季 EPS surprise 概率 |
| `rerating_upside` | 估值重估（L3/L4 敘事）概率 |
| `execution_risk` | 承諾 vs 進度落差（越高越差） |
| `regulatory_risk` | 監管延遲或調查 |
| `peer_pressure` | 同業相對落後程度（越高壓力越大） |

**Explosion Watchlist** = 未來 90 天內、可驗證、且會移動 `eps_upside` 或 `rerating_upside` 的 3–5 個事件。

---

## 5. 報告章節模板（Tesla 專用）

1. **雙軌結論** — EPS 壓力 / 股價壓力（各一句）
2. **四層快照** — L1–L4 各 3 個 KPI
3. **Transcript Diff** — 本季 vs 上季（若有新財報）
4. **X 週 digest** — ≤5 條，附分級
5. **同業一頁表** — Robotaxi + Humanoid
6. **Macro AI** — Jensen 等相關摘句（若有）
7. **Explosion Watchlist** — 90 天事件
8. **Catalyst Score** — 五維表格
9. **風險與免責**

---

## 6. 實作路線圖

| 階段 | 內容 | 狀態 |
|------|------|------|
| Phase 1 | 通用技術/基本面 CLI | ✅ 完成 |
| Phase 2 | Cursor Skill + Canvas | ✅ 完成 |
| Phase 3a | 本框架 + 配置骨架 | ✅ 進行中 |
| Phase 3b | Transcript 抓取與 QoQ diff | 待做 |
| Phase 3c | X 輕量 digest（手動或 API） | 待做 |
| Phase 3d | 同業表自動/半自動更新 | 待做 |
| Phase 3e | EPS/股價爆發偵測 + Watchlist | 待做 |

---

## 7. 免責

本框架用於研究與追蹤，不構成投資建議。無法可靠「預測」股價或 EPS 爆發，僅能標註催化劑概率與可驗證里程碑。
