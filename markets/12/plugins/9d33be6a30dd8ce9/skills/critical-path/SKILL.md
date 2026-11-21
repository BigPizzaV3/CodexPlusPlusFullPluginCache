---
name: critical-path
description: Compute project critical paths, earliest and latest offsets, total and free slack, and CSV schedules from explicit task durations and finish-to-start dependencies.
---
Call calculate_critical_path with unique task IDs, durations, dependency IDs and a single elapsed-time unit. Inputs can be unsorted. Zero durations are milestones. Use provided durations; do not infer missing estimates. Report project duration, critical tasks and the illustrative longest chain. Explain that offsets start at zero and resources, calendars and lags are not modeled. The widget edits durations and exports the complete schedule. Downloads expire in about one hour. Do not use for calendar scheduling or Gantt charts.
