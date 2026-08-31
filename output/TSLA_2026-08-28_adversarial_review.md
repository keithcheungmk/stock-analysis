# TSLA Adversarial Review Memo

- 覆核時間：2026-08-31（Asia/Hong_Kong）
- Ticker：TSLA／Tesla, Inc.；IR `https://ir.tesla.com/`
- 報告 as-of：財務 2026-Q2；催化劑刷新至 2026-09-03 發佈會

## IR／SEC

- EDGAR 最近 Tesla 10-Q 仍係 **2026-07-23**（`0001628280-26-049270`）；Q2 EX-99.1 **2026-07-22**（`0001628280-26-049213`）。**無**更新 8-K 宣布 9/3 Cybercab 發佈會。
- IR 新聞頁（公開索引）：最新仍係 2026-07-22 Q2 業績；其後未見 Cybercab 新聞稿。本環境 `ir.tesla.com/press` 同 `tesla.com/robotaxi` **403**，產品頁未能直讀。
- 官方包：`data/raw/TSLA/2026-Q2/manifest.json` `validation_status: complete`；`pending_sources: []`；`unavailable_sources`: official transcript。
- EX-99.1 已有：Cybercab began production at Giga Texas；公共道路工程試駕；7 月員工校園試乘；Texas Cybercab 表列產能 >125,000；Robotaxi 七城表；Las Vegas = Preparations Underway；累計付費英里只有圖軸。

## X（x_access=degraded）

無 X API。用新聞轉述官方帳：

| Handle | 約日期 | 內容 | 標籤 |
|---|---|---|---|
| @Tesla | 2026-08-22 | Exclusive Access: Cybercab；9/3 Austin | narrative（事件日期；非 8-K） |
| @robotaxi | 2026-08-18 | 8/23 前搭 Robotaxi 抽獎入場 | narrative |
| @robotaxi | 2026-08-26 | 6am–10pm；fleet「a lot bigger」；無車隊數 | narrative |
| @Teslarati | 2026-08-22 | 公開邀請函相片 | noise／交叉 |

Electrek／We Talk Tesla／Motor1 交叉：邀請場、21+、RSVP 8/30、直播、1 Tesla Road。**未**證明 9/3 公眾付款叫車。

## Diff vs 2026-08-27 草稿

| Claim | 狀態 |
|---|---|
| Cybercab 車隊「Outlook 未定量」 | **STALE** → 發佈會已定量 2026-09-03；規模／入帳仍未定量 |
| Q2 財務／F3 Base US$157 | **OK** |
| Robotaxi 已入帳 US$0 | **OK** |
| 爆發定義 C 兩欄未觸發 | **OK** |
| 7 城／Cybercab 投產 | **OK**（官方） |
| tesla.com Cybercab「將來先有」 | **LEAD_ONLY**（第三方引產品頁；本環境 403） |
| unsupervised 20–30 輛；380k miles | **LEAD_ONLY**（Electrek／業績會轉述；唔覆寫官方包） |
| Nevada 5,000 輛上限 | **LEAD_ONLY**（NTA／第三方；官方 Q2 仍 Preparations） |
| 中國 ~297.6 萬輛召回 | **MISSING** → 已寫入催化劑頁作 L1 噪音；唔改 Base |
| JPM v15／Optimus 2027 H2 | **OK** 維持 unverified |

## 已 patch

- `config/tesla_milestones.yaml`
- `output/TSLA_catalyst_calendar.html`、`output/TSLA_2026-08-28_catalyst_calendar.md`
- `output/TSLA_one_pager.html`、`output/TSLA_2026-08-27_one_pager.md`
- `output/TSLA_interactive_brief.html`（Pages 隱藏）
- `output/TSLA_2026-08-28_adversarial_review.md`
- `scripts/publish_html_reports.py`（鎖 `docs/tsla/index.html` 唔重排）

## Verdict impact

**維持。** 微調催化劑日期同 Street／SOTP 分軌；輕量 refresh 現價 US$365.83（8/31 delayed）、vs Base **+133%**（Base US$157 唔改）。行動維持僅觀察／唔好加倉。

*此分析僅供研究參考，不構成投資建議。*
