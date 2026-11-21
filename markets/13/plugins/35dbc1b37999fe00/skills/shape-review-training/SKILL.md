---
name: shape-review-training
description: Review the user's recorded Shape workouts, training load, readiness and daily health trends. Use for questions about pacing, interval execution, planned versus completed training, weekly mileage, sleep, HRV, recovery or fitness trends. This workflow reviews data without changing the account.
---

# Review training and recovery in Shape

Use the connected Shape tools and their current schemas. Follow the user's question and unit preferences. Do not request API tokens. If Shape is unavailable, explain how to connect it without claiming to have inspected the account. If a tool answers that no device is connected or nothing is synced, offer `connect_device` (see the shape-setup skill) instead of reviewing an empty account.

## Choose the relevant data

| Question | Tools and scope |
| --- | --- |
| What is on my calendar or what did I complete? | `list_activities` over the relevant date range, with the appropriate sport and completed filter |
| What was prescribed for this completed workout? | `get_activity` for its `plannedActivityId` |
| How did I pace the workout or execute the intervals? | `get_activity_details` for the selected completed activity |
| How recovered am I, why is readiness low, or how does the plan affect load? | `get_training_status` with no `from` or `to` |
| How did fitness, fatigue or morning readiness change over a past period? | `get_training_status` with both `from` and `to` |
| What were the recorded daily sleep, HRV or other health measurements? | `list_health_metrics` with a bounded date range and an optional metric whitelist |

Use the athlete's local calendar for relative dates. Ask for clarification if the date range or selected workout is ambiguous. Do not retrieve a year of history for a question about this week.

## Calendar and planned-versus-completed comparisons

- Activities are returned newest first. Use `limit` and `offset` to page through `total` before reporting complete totals; the default page has at most 50 entries, with a maximum requested page of 200.
- `completed: true` selects performed workouts; `false` selects plans. Omit it only when both are relevant.
- A fulfilled plan is hidden from the default list, leaving its completed counterpart. That completed row does not contain the planned prescription or steps. Fetch `plannedActivityId` with `get_activity` for a comparison.
- `includePaired: true` can expose both rows. Do not add both halves to volume or load totals. Distinguish performed training from planned training and missed sessions.
- Show dates, workout titles, sport and readable distance/duration. Convert meters and seconds for display; do not treat absent values as recorded zeros.

## Recordings, laps and zones

Use `get_activity_details` for questions summaries cannot answer. Prefer returned `laps` and `zones` when those summaries are sufficient. Ask only for necessary channels such as `heartRate`, `speed`, `power` or `cadence`; the schema lists all supported names.

`points` controls detail from 10 to 2000. Begin with the default or a modest value and raise it only when interval detail is insufficient. Channels are parallel arrays indexed against `time` in seconds from the activity start. Read `units` and `resolutionSeconds` before interpreting values. Laps and zones reflect the full recording even when channels are reduced. Do not invent exact spikes or transitions between returned points.

`detailFrom` identifies the selected recording when it came from another connected source. Explain the returned source rather than assuming it is the activity's displayed source. If details are missing, relay the tool's `message` and `reason`; a planned workout, a manual entry and a missing device recording are different cases.

Routes are omitted by default. Use recorded `lat`/`lng` only when the user asks about a route. Request `get_activity` with `includeMap: true` only when drawing a map requires its encoded route; an encoded route string does not answer an effort question.

## Readiness and load

- Use Shape's `get_training_status` results rather than rebuilding readiness or training load from activity and health lists.
- Explain a readiness score with its returned `drivers`, their values and their baselines. Read `basis`: the current snapshot includes completed training today; historical series readiness represents the morning before that day's training.
- Fitness, fatigue, form and load ratio are separate measures. Explain the returned relationship and trend in the athlete's terms. A ratio above 1.5 is labeled High by Shape; it is a training-load flag, not proof of an injury or a diagnosis.
- The default `series` includes today and the next seven days of projected load, with `projection` reporting that week's peak. Readiness cannot be projected. Distinguish planned/projected values from recorded results.
- When a score or projection is absent, explain the returned missing-data reason. Do not prescribe a fixed waiting period or a connection change unless the result supports it. A missing projection may mean no upcoming planned workout carries a load value.
- Let the athlete's current symptoms or stated restrictions take precedence over a favorable score. Answer training-data questions without diagnosing illness or replacing clinical advice.

## Daily health trends

Metric ids must match the input schema. Examples include `restingHR`, `hrvMs`, `sleepDurationSec`, `sleepScore`, `vo2max`, `steps`, `bodyBatteryCharged` and `bodyBatteryDrained`. Omit `metrics` when the relevant recorded fields are unknown. Without `from`, only the last 90 days are returned; provide it explicitly for older questions.

Use each value's reported source and units. Keep differing HRV methods separate: Garmin RMSSD and Apple SDNN are not directly interchangeable, even though both use milliseconds. `bodyBatteryCharged` and `bodyBatteryDrained` are daily totals, not the watch's instantaneous 0–100 level. Convert sleep seconds to hours/minutes for the athlete. Explain gaps instead of interpreting missing values as a deterioration.

## Deliver the review

Lead with the answer, then the few observations that support it. Keep completed work, future plans and any uncertainty distinct. When a comparison cannot be made, say which data is missing. Do not move workouts or delete data during a read-only review unless the user adds a request for that action.
