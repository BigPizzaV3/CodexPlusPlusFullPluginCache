---
name: workforce-briefing
description: Summarize Staffology attendance, hours, overtime, task progress, and workforce anomalies for the connected organisation.
---

# Workforce briefing

Use Staffology's live records to answer workforce-status and performance questions for the connected organisation.

- Use `who_is_present` for the live clocked-in, on-break, and clocked-out state.
- Use `employee_activity` for one employee on one day and `employee_monthly` for one employee's calendar month.
- Use `late_arrivals`, `attendance_trends`, or `overtime_summary` for the corresponding measured period. Treat overtime cost as an estimate, not payroll output.
- Use `weekly_digest` for a current-week overview and add `red_flags` only when the user asks for risks or anomalies.
- Use `productivity_ranking` only for requests that explicitly compare task completion. Describe its completion-rate and tasks-per-hour measures without presenting them as work quality.
- Use `daily_report_pdf` or `detailed_report_pdf` only when the user asks for a downloadable report. Each call stores a new file and returns a link valid for two hours.

Choose the narrowest tool that answers the request. Do not infer a location from a punch `source`; it identifies a device type, not where the employee was. Never invent data about another organisation, GPS coordinates, photographs, or face embeddings because the connector does not expose them.
