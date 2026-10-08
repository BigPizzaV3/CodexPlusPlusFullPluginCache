# Manifest 契約

`## Calculation Contract` 內的唯一 JSON 程式碼區塊，是黃金基線管理系統後端可編譯的機器契約。Markdown 其餘內容用於人員理解與稽核，不能取代 Manifest。

## 標準結構

```json
{
  "schema_version": "golden-baseline-declarative-pipeline/v1",
  "pipeline_id": "same_as_frontmatter_algorithm_id",
  "pipeline_version": "same_as_frontmatter_version",
  "engine_api_version": "deterministic-feature-api/v1",
  "signal_roles": [
    {
      "role": "power",
      "aliases": ["power", "功率", "有功功率"],
      "compatible_units": ["W", "kW", "MW"],
      "required": true
    }
  ],
  "execution_profiles": {
    "historical_closed_event": [
      "time_alignment",
      "missing_deviation",
      "value_deviation"
    ],
    "realtime_open_event": [
      "time_alignment",
      "missing_deviation",
      "value_deviation"
    ]
  },
  "quality_gates": {
    "minimum_completeness": 0.9,
    "maximum_missing_rate": 0.2,
    "minimum_points": 30,
    "maximum_gap_multiplier": 6.0,
    "require_monotonic_timestamps": true,
    "require_compatible_units": true,
    "require_confirmed_event_start": true
  },
  "threshold_overrides": {},
  "fixtures": [
    {
      "fixture_id": "normal_case",
      "category": "normal",
      "execution_mode": "historical_closed_event",
      "unit": "kW",
      "sample_interval_ms": 10000,
      "baseline_values": [0, 10, 30, 50, 30, 10, 0],
      "observed_values": [0, 10, 30, 50, 30, 10, 0],
      "data_completeness": 1.0,
      "expected_status": "normal"
    }
  ],
  "proposed_algorithms": []
}
```

## 允許算法識別碼

- `time_alignment`
- `missing_deviation`
- `value_deviation`
- `time_deviation`
- `waveform_deviation`
- `slope_deviation`
- `area_deviation`
- `stability_deviation`

不在清單內的能力只能列入 `proposed_algorithms`，每項至少包含識別碼、業務目的、需要的輸入及尚未支援的原因。

## 執行模式

- `historical_closed_event`：事件已有可信起點與終點，可使用全部適用算法。
- `realtime_open_event`：事件終點尚未確定，不得使用依賴完整事件長度或整段積分的 `time_deviation`、`area_deviation`。事件結束後由後端重新執行歷史設定。

## 品質欄位範圍

- `minimum_completeness`：`0.5` 至 `1.0`。
- `maximum_missing_rate`：`0.0` 至 `0.5`。
- `minimum_points`：`3` 至 `100000`。
- `maximum_gap_multiplier`：`1.0` 至 `100.0`。
- 三個 `require_*` 欄位必須為布林值。

`minimum_completeness + maximum_missing_rate` 不得小於 `1.0`。門檻放寬時必須在 Skill 說明業務理由，不得為了讓案例通過而調低品質要求。

## 固定案例

`fixtures` 至少各有一個：

- `category: normal` 且 `expected_status: normal`
- `category: abnormal` 且 `expected_status: abnormal`
- `category: insufficient_data` 且 `expected_status: insufficient_data`

案例只能包含純資料，不得包含程式碼、公式求值字串、檔案路徑、網路位置或憑證。每個案例都必須有唯一 `fixture_id`、合法執行模式、相容單位、正數採樣間隔，以及數字陣列。資料不足案例可以使用短陣列、低完整率或明確缺口，但必須與品質閘門相符。

## 一致性要求

- Manifest 的 `pipeline_id` 等於 frontmatter `metadata.algorithm_id`。
- Manifest 的 `pipeline_version` 等於 frontmatter `metadata.version`。
- Manifest 與 frontmatter 的 `engine_api_version` 相同。
- `signal_roles` 至少一項且角色不可重複。
- 每個 execution profile 至少包含 `missing_deviation`；跨來源或圖層對齊時也包含 `time_alignment`。
- `threshold_overrides` 只能使用後端已公開的門檻鍵；不確定時保持空物件。

外掛只能產生候選規格。後端編譯與固定案例全部通過前，不得宣告 `executable`。
