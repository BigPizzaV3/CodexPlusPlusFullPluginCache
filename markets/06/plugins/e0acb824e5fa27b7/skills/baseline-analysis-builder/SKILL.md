---
name: baseline-analysis-builder
description: Create, upgrade, or repair a safe declarative time-series analysis SKILL.md with a machine-readable pipeline Manifest and fixed fixtures for the Golden Baseline Management System. Use when users describe a new process, need a newer algorithm version, or provide backend compilation errors; never self-certify runtime execution.
---

# 黃金基線時序分析算法建置器

把設備與工藝需求轉成黃金基線管理系統可編譯、可測試、可版本化與可稽核的宣告式算法 Skill。使用者只需說明設備、工藝及希望識別的偏差，不需要自己挑選數學模型。

## 工作模式

- **建立**：從自然語言需求建立完整 `SKILL.md`、Manifest 與固定案例。
- **升級**：讀取既有 Skill，保留 `algorithm_id`，依相容性提高語意版本並補齊新契約。
- **修復**：讀取後端的編譯、固定案例、相容性或版本錯誤報告，修正 Skill；不得隱藏、忽略或繞過錯誤。

只詢問缺少的工藝事實：設備、階段、訊號意義與單位、採樣間隔、預期偏差、事件錨點及期望判斷。不得要求使用者命名 RMSE、DTW、Cross-correlation 或其他數學方法。

## 必讀契約

- 建立或修復前先讀 [Manifest 契約](references/manifest-contract.md)。
- 功率類時序需求先讀 [功率時序範例](references/power-timeseries-example.md)，再依實際設備調整，不得直接複製不適用的門檻。

## 必要 Frontmatter

```yaml
---
name: readable-skill-name
description: Clear trigger description for this analysis algorithm.
metadata:
  schema_version: golden-baseline-analysis-algorithm/v1
  skill_role: analysis-algorithm
  algorithm_id: stable_lowercase_identifier
  version: 1.0.0
  engine_api_version: deterministic-feature-api/v1
  implementation_kind: declarative_pipeline
---
```

- `algorithm_id` 必須符合 `^[a-z][a-z0-9_]{2,63}$`。
- `version` 必須是嚴格的 `MAJOR.MINOR.PATCH`。
- 新算法使用 `declarative_pipeline`；只有系統登錄且後端確認可執行的算法可以使用 `builtin_reference`。

## 必要章節

每個章節必須且只能出現一次：

1. `# <Algorithm Name>`
2. `## Purpose`
3. `## Inputs`
4. `## Applicability`
5. `## Calculation Contract`
6. `## Quality Gates`
7. `## Output Contract`
8. `## Golden Fixtures`
9. `## Safety`

## Manifest 要求

`## Calculation Contract` 必須包含且只能包含一個 JSON 程式碼區塊，其內容符合 `golden-baseline-declarative-pipeline/v1`：

- `pipeline_id` 與 `pipeline_version` 必須與 frontmatter 的 `algorithm_id`、`version` 完全一致。
- `signal_roles` 使用角色及相容單位，不得綁定固定 EDC 位址、帳號、SUID 或 CUID。
- `execution_profiles` 分別定義 `historical_closed_event` 與 `realtime_open_event`；即時模式不得使用依賴事件終點的算法。
- `quality_gates` 必須包含完整率、缺值率、最少點數、最大缺口、時間單調性、單位相容及已確認起點。
- `fixtures` 必須包含 `normal`、`abnormal`、`insufficient_data` 三類純資料案例，並聲明 `expected_status`。
- 系統尚未提供的能力必須放入 `proposed_algorithms`，不得假裝已可執行。

完整欄位、允許算法與數值範圍以 Manifest 契約為準。

## 判斷與品質原則

- 使用滿足需求的最小確定性算法組合；不要每次啟動全部算法。
- 缺值與時間對齊是前置品質檢查；品質不足時不得輸出正常結論。
- 歷史封閉事件可以計算完整時長與面積；即時開放事件只執行不依賴終點的分支，事件結束後再重算完整結果。
- `Output Contract` 至少包含 `algorithm_id`、`algorithm_version`、`status`、`score`、`unit`、`evidence_range`、`quality` 與可讀證據。
- 狀態只可為 `normal`、`attention`、`abnormal`、`insufficient_data`、`not_applicable`。

## 編譯與執行邊界

ChatGPT 與本 Skill 負責產生或修復候選規格，不負責宣告候選版本已可執行。唯一有效狀態流程為：

`specification_only → compiled → fixtures_passed → executable`

任一步失敗時只能標示 `requires_revision` 或 `rejected`，並保留後端錯誤證據。只有黃金基線管理系統後端完成 schema 驗證、Manifest 編譯、固定案例執行、版本相容檢查及管理員核准後，才可標示 `executable`。

不得輸出 patch、Python、SQL、Shell、JavaScript、網址、安裝指令或任何可執行內容。不得存取網路或憑證、修改 EDC 資料，且結果不能取代安全關鍵工程判斷。

## 版本規則

- PATCH：文字、案例或相容門檻修正，不改必要輸入與結果語意。
- MINOR：向下相容的新能力、可選輸入或新增執行設定。
- MAJOR：輸入、計算、輸出、單位或判斷語意不相容。
- 不得降低版本，也不得以相同版本承載不同內容。

## 最終檢查與輸出

輸出前確認 frontmatter、九個必要章節、穩定算法識別碼、語意版本、唯一 Manifest、歷史／即時設定、品質閘門、三類固定案例、安全邊界與未實作能力清單一致。

建立或升級時只輸出一份完整 `SKILL.md`。修復時先用簡短文字列出已處理的後端錯誤，再輸出完整 `SKILL.md`；不得聲稱已通過後端編譯或已可執行。
