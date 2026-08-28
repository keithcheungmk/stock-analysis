# MRVL Cowork 執行筆記（本輪由 Cowork 直接執行 Skill 2–9，非審稿）

- **對住：** `output/MRVL_2026-08-28_framework1.md`（Cursor 原有 F1，WATCH 65/130）+ 本輪新增 Framework 2／3、peer comparison、catalyst calendar、thesis tracker、one-pager（markdown + `docs/mrvl/*.html`）
- **背景：** 用戶因為 Cursor 冇 token 可用，直接要求 Cowork 呢個 session 越過平時「審稿角色」做執行者，一次過起晒 MRVL 剩低嘅 7 個 Skill／頁面。已用 AskUserQuestion 確認用戶明確 override AGENTS.md「一次一個 Skill」嘅規矩。

## 已完成

- `output/MRVL_2026-08-28_framework2.md` + `docs/mrvl/framework2.html`
- `output/MRVL_2026-08-28_framework3.md` + `docs/mrvl/framework3.html` + `docs/mrvl/valuation.html`（互動滑桿）
- `output/MRVL_2026-08-28_peer_comparison.md` + `docs/mrvl/peer-comparison.html`
- `output/MRVL_2026-08-28_catalyst_calendar.md` + `docs/mrvl/catalyst-calendar.html`
- `output/MRVL_2026-08-28_thesis_tracker.md` + `docs/mrvl/thesis-tracker.html`
- `output/MRVL_2026-08-28_one_pager.md` + `docs/mrvl/one-pager.html`（見下方格式偏離）
- 回頭更新咗 `docs/mrvl/framework1.html`（同 `output/MRVL_framework1.html`）嘅 Decision HUD，由 `F3 pending` 換成正式 Bear／Base／Bull 區間，符合 `DECISION_HUD.md`「F3 完成後回頭換走 pending 頁」嘅要求。

## 必須知道嘅偏離／限制（請 Cursor 或用戶覆核）

1. **One-pager 冇做到 Canvas PPT。** Skill 9 規定主交付係 Cursor 專屬嘅 `.canvas.tsx`（`~/.cursor/projects/.../canvases/`），Cowork 呢個 session 冇呢個工具鏈，改用 markdown＋互動 HTML（`docs/mrvl/one-pager.html`）代替，內容已喺檔內用 notice 講明。如果想要正牌 Canvas，需要喺 Cursor 度另外補做。
2. **Framework 3 嘅 FY2027 全年營收（Bear/Base/Bull 情景嘅 US$10.5B／11.8B／13.0B）係 Cowork 自行外推，唔係官方指引。** 公司只公布咗 H1 FY27 實際數同 Q3 FY27 指引中位（US$3,150m），未有全年美元指引。呢個喺 `framework3.md` 已經清楚標示方法論，但由於呢類外推帶主觀判斷，建議 Cursor／用戶覆核呢組假設是否合理，尤其係 Q4 FY27 按季增速假設。
3. **同業比較入面嘅 AVGO 現價未能獨立核實。** 嘗試查詢嘅報價頁面（Google Finance／CNBC）返嘅係唔可靠或過時數據，所以 `peer_comparison.md`／HTML 淨係用咗 AVGO 已喺本倉出現過嘅 yfinance TTM P/S（23.4×）做參考倍數，冇獨立核實 AVGO 現價本身，亦冇幫 AVGO 做完整 F1／F3。呢點喺文件入面已經明確標示，但如果用戶想用呢份比較做決策，建議先自行核實 AVGO 現價。
4. **`data/raw/MRVL` manifest 喺呢個 Mac 本機／git 完全唔存在**（同之前 NVDA review 揭發嘅同一個 gap 模式）——F1 文件話「6 manifests 驗證通過」，但呢批 raw 檔案顯然淨係存在過 Cursor Cloud 嘅 sandbox，從未同步落嚟用戶個 Mac 或者 push 落 git（`data/raw` 本身喺 `.gitignore`，要靠 force-add 先會入 git，NVDA 用 `scripts/bootstrap_manifests_from_catalog.py` 解決過，MRVL 未做）。本輪 Framework 2–9 嘅官方數字改用 WebSearch／WebFetch 直接重新對住 SEC EDGAR 原文（8-K EX-99.1）覆核，唔係倚賴呢批唔存在嘅本機 manifest，所以數字本身可信，但**冇本機 SHA-256／manifest 記錄**，同呢個 repo 一貫嘅 provenance 標準有落差。建議同 NVDA 一樣，跑一次 bootstrap／`download_official_research.py` 幫 MRVL 補返 manifest。
5. **`docs/mrvl/valuation.html` 嘅互動滑桿只係簡化模型**（EV/Sales × 自行外推營收 − 固定淨債，股數用現時基準未按情景拆細稀釋），唔係精確模型，已喺頁腳同 markdown 標明。

## 資料來源方法論（本輪新增內容點樣拎數）

Framework 2 嘅五季 KPI 全部逐季用 WebFetch 直接讀 SEC EDGAR 原文覆核（Q2 FY26 至 Q2 FY27 共 5 份 8-K EX-99.1，URL 已列喺 `framework2.md` 頁尾），Google warrant 條款讀咗 8-K（accession `0001193125-26-356217`）原文。Peer comparison 入面 NVDA／AMD 數字引用本倉已有、近期覆核過嘅 F1／F3；AVGO 數字對住 Broadcom IR 官方 2026-06-03 Q2 FY2026 press release 覆核。

## 未做

- 冇再重新驗證 F1 本身嘅數字（假設 F1 已經係準確嘅，本輪淨係喺佢基礎上加建）。
- 冇跑 `x-adversarial-review`（F2 skill 話距 F1 少過 7 日可以唔跑，已喺 framework2.md 註明）。
- 3 條舊 NVDA branch（`framework1-1209`／`framework3-1209`／`remaining-skills-1209`）仍未關閉，呢個同今次 MRVL 工作無關，之前已經提過。

*此分析僅供研究參考，不構成投資建議。*
