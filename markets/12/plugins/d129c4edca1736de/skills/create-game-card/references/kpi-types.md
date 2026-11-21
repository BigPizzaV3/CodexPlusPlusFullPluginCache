# KPI type shapes for `preview_gamecard`

Every metric has `name`, `category`, `weightage`. Core KPIs also need `kpi_type`. The server rejects anything not listed here and tells you the fix.
A complete valid gamecard is in `examples/retail-sales-executive.json`.

## Fixed categories (no `kpi_type`)

```json
{ "name": "Attendance", "category": "Attendance", "weightage": 10 }
{ "name": "Timing", "category": "Timing", "weightage": 10 }
{ "name": "Reports", "category": "Reports", "weightage": 10 }
```

Normally 10 points each; Reports last. `attendance_rules` is optional and only for a user who wants non-standard leave or late penalties.

## Goal-ProRata: a monthly target, scored in proportion

Needs `target_value` and a `dkr_field` (the number the Team Member enters every day). `goal_config.mqr_threshold` (percent) is optional; sales roles commonly use 70.

```json
{ "name": "Monthly Sales", "category": "Core KPIs", "kpi_type": "Goal-ProRata", "weightage": 20,
  "target_value": 500000, "unit": "INR",
  "dkr_field": { "name": "Sales today" }, "goal_config": { "mqr_threshold": 70 } }
```

## Goal-Slab and Goal-Average: stepped points

Need `goal_config.slabs` (target and points, highest first) and a `dkr_field`. Goal-Slab scores the month total (new customers, breakthroughs); Goal-Average scores the daily average. A slab's `points` can never exceed the KPI `weightage`.

```json
{ "name": "New Customers", "category": "Core KPIs", "kpi_type": "Goal-Slab", "weightage": 10, "target_value": 20,
  "dkr_field": { "name": "New customers today" },
  "goal_config": { "slabs": [ { "target": 20, "points": 10 }, { "target": 12, "points": 6 }, { "target": 6, "points": 3 } ] } }
```

## Conversion: A to B as a percentage

Needs `conversion_config` with `input_a_label`, `input_b_label` and `slabs` over the percentage, plus `target_value` and a `dkr_field`.

## Occurrence: errors or incidents, fewer is better

Needs `occurrence_config` (`tolerance`, `deduction_per_occurrence`, optional `occurrence_levels`) and a `dkr_field`.

## Checklist: recurring tasks

**List size: 5 to 15 tasks** (the server rejects fewer or more).

`checklist_config.tasks` is required. Task points must add up to **exactly** the KPI weightage. `frequency` is one of `daily`, `weekly`, `bi-weekly`, `monthly`. Use a mix of frequencies; ask the user for the real tasks.

## Audit-Feedback: scored parameters from an audit or customer feedback

`audit_feedback_config`: `type` (`internal` for audits of the Team Member's work, `external` for customer feedback), `rating_scale` (5 or 10), `frequency` (`daily`, `weekly`, `bi-weekly`, `monthly`, `on_demand`), optional `audit_count`, and `parameters` (**5 to 10 questions**) whose weightages add up to **exactly** the KPI weightage.

## Productivity: tasks with a standard time (SAM)

**List size: 10 to 30 tasks or steps** for Productivity and for Cycle Time (the server rejects fewer or more). Name them plainly ("Ticket Resolution"), without "(per ticket)".

`productivity_config.productivity_type` is `productivity` (minutes) or `cycle_time` (seconds).

- `productivity`: each task has `sam_minutes` (at least 0.5); optional `daily_goal_minutes: { min, max }`.
- `cycle_time`: each task has `sam_seconds` (at least 10); optional `daily_goal_seconds: { min, max }`.

SAM is the standard allowed time to do one unit of the task. Ask the user for it or propose and confirm. Never present a guessed SAM as measured.

## ToDo-List and Leadership

`ToDo-List` needs nothing more than the weightage. `Leadership` has an optional `leadership_config` (`calculation_method` of `team_average`, `team_sum` or `team_median`, `team_performance_threshold`, `minimum_team_size`, `include_manager_performance`); it measures the team a lead looks after.

## Common server errors and their fix

| Error path | Meaning | Fix |
|---|---|---|
| `metrics` total | Weightages do not add up to 100 | Adjust points, keep multiples of 5 |
| `...goal_config.slabs` | Slab type without slabs, or a slab above the weightage | Add slabs; cap points at the weightage |
| `...checklist_config.tasks` | Task points do not equal the weightage | Rebalance the task points |
| `...audit_feedback_config.parameters` | Parameter weightages do not equal the weightage | Rebalance |
| `...dkr_field` | A Goal, Conversion or Occurrence KPI has no daily field | Add `dkr_field` |
| `...tasks[n].sam_minutes` | SAM below the minimum | Use at least 0.5 minutes (10 seconds for cycle time) |
