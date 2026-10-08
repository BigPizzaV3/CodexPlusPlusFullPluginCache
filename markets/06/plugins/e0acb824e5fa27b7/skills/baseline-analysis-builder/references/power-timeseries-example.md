# 功率時序算法範例

這是感應爐或其他工業設備功率曲線的參考，不是固定配方。建立實際 Skill 時，必須依設備階段、採樣間隔、額定範圍、事件錨點及資料品質調整。

## 適用意圖

- 比較實際功率曲線與黃金基線圖層。
- 在人工、PLC、批次或 Tagger 確認起點後才開始對齊。
- 歷史事件評估數值、時長、形狀、斜率、面積、穩定度及缺失。
- 即時事件只啟動不依賴終點的算法，事件完成後補算完整結果。

## 參考 Manifest

```json
{
  "schema_version": "golden-baseline-declarative-pipeline/v1",
  "pipeline_id": "industrial_power_profile",
  "pipeline_version": "1.0.0",
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
      "value_deviation",
      "time_deviation",
      "waveform_deviation",
      "slope_deviation",
      "area_deviation",
      "stability_deviation"
    ],
    "realtime_open_event": [
      "time_alignment",
      "missing_deviation",
      "value_deviation",
      "waveform_deviation",
      "slope_deviation",
      "stability_deviation"
    ]
  },
  "quality_gates": {
    "minimum_completeness": 0.9,
    "maximum_missing_rate": 0.2,
    "minimum_points": 7,
    "maximum_gap_multiplier": 6.0,
    "require_monotonic_timestamps": true,
    "require_compatible_units": true,
    "require_confirmed_event_start": true
  },
  "threshold_overrides": {},
  "fixtures": [
    {
      "fixture_id": "power_normal",
      "category": "normal",
      "execution_mode": "historical_closed_event",
      "unit": "kW",
      "sample_interval_ms": 10000,
      "baseline_values": [0, 100, 300, 500, 300, 100, 0],
      "observed_values": [0, 100, 300, 500, 300, 100, 0],
      "data_completeness": 1.0,
      "expected_status": "normal"
    },
    {
      "fixture_id": "power_abnormal_high",
      "category": "abnormal",
      "execution_mode": "historical_closed_event",
      "unit": "kW",
      "sample_interval_ms": 10000,
      "baseline_values": [0, 100, 300, 500, 300, 100, 0],
      "observed_values": [25, 125, 325, 525, 325, 125, 25],
      "data_completeness": 1.0,
      "expected_status": "abnormal"
    },
    {
      "fixture_id": "power_insufficient",
      "category": "insufficient_data",
      "execution_mode": "historical_closed_event",
      "unit": "kW",
      "sample_interval_ms": 10000,
      "baseline_values": [0, 100, 300, 500, 300, 100, 0],
      "observed_values": [0, 100],
      "data_completeness": 0.28,
      "expected_status": "insufficient_data"
    }
  ],
  "proposed_algorithms": []
}
```

## 改用其他工藝時

1. 把 `power` 改成實際訊號角色，例如溫度、壓力、流量、振動或速度。
2. 改用實際相容單位，不得混用無法換算的量綱。
3. 依事件長度及採樣間隔設定最少點數。
4. 只選與工藝偏差有關的算法；平台穩定度不適用於持續升降段，面積偏差也不是所有訊號都有物理意義。
5. 保留三類固定案例，並讓異常案例對應使用者真正關心的偏差。
6. 新需求超出允許算法時列入 `proposed_algorithms`，交由後端及管理員建立新版本，不能假裝已經支援。
