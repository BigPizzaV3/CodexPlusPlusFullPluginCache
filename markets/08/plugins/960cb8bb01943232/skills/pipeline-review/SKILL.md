---
name: pipeline-review
description: Summarize how a Vixiees playbook is performing over a period — new, won and lost contacts, stage movement, and pending tasks. Use when the user asks how their pipeline, playbook, funnel or leads are doing, or wants a weekly/daily summary.
---

# Pipeline review

Give the user a short, numbers-first summary of one playbook.

## Steps

1. Pick the playbook. Call `list_playbooks_tool`. If there is exactly one, use it. If there are several and the user didn't name one, ask which — list them by name.
2. Pick the period. Default to `last_7_days` unless the user said otherwise ("this month", "yesterday", a date range → `custom` with `start_date`/`end_date`).
3. Call `get_dashboard_overview_tool` with the playbook and period for new, active, won and lost contacts and the 30-day trend.
4. Call `get_dashboard_status_transitions_tool` to see which stages contacts moved into and out of.
5. Call `get_dashboard_pending_tasks_tool` with `breakdown: "by_type"` to show where work is piling up.

## Output

- Lead with 3–4 headline numbers (new, won, lost, pending tasks) and the change versus the trend.
- Then one short paragraph on where contacts are getting stuck — the stage with the most entries and the fewest exits.
- Then the task types with the most pending tasks.
- Answer in the language the user wrote in.

## Rules

- Contacts are mostly consumers who expect a fast reply, often on WhatsApp. Frame bottlenecks around response speed and follow-up, not meetings or large deals.
- Tasks are assigned automatically by Vixiees. Never suggest reassigning tasks between agents.
- Don't invent numbers. If a tool returns no data for the period, say so and offer a longer period.
