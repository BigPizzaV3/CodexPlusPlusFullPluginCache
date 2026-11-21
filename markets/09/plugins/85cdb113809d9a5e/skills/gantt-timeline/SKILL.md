---
name: gantt-timeline
description: Gantt chart maker and critical path calculator. Use plan_project_timeline to schedule a task list (durations, dependencies, milestones) into a Gantt chart with early/late dates, float, the critical path, the end date and CSV, .ics and SVG files; use compare_timeline_scenarios for what-if slips.
---

# Zovo Project Timeline

Use `plan_project_timeline` when the user wants a Gantt chart, a project timeline or schedule, a project plan with milestones, the critical path, the project end date, or early/late start and finish dates and float for a task list.

1. Pass every task in `tasks` with a `name` and a `duration` (days by default; set `duration_unit` to weeks for weeks). Use short `id`s when names are long. Put predecessors in `depends_on` by id or name; write a lag as "Design+2" and a lead as "Build-3". Milestones (Launch, Sign-off, Submission) get `milestone: true` and no duration.
2. Pass `start_date` as YYYY-MM-DD. If the user gives none, ask once or let it default to today and say so.
3. `calendar` is business_days by default (Monday to Friday). Add `country` (and `subdivision`) when the user mentions a country or region so its public holidays are skipped, and `non_working_dates` for shutdowns or vacations. Use calendar_days only when the user counts every day (for example a personal or student plan that includes weekends).
4. Use `start_no_earlier_than` for fixed dates such as a delivery or kickoff that cannot move earlier.

Use `compare_timeline_scenarios` when the user asks "what if X slips N days", "what if X takes longer", or "what if the vendor delivers later". Pass the same plan plus 1 to 4 `scenarios` with `changes` (`extra_days`, `duration`, or `start_no_earlier_than`).

After a result, state the end date, the critical path and any task with notable float in one or two sentences, mention that the chart is interactive, and give the CSV, calendar (.ics) and SVG links. If the tool reports a dependency loop or an unknown task, repeat its message and ask which link to change.

Do not use these tools for software how-to questions (Excel, MS Project), for a single date difference, or for daily to-do lists. They do not save plans, sync with project tools, track progress, or level resources; only finish-to-start dependencies are supported.
