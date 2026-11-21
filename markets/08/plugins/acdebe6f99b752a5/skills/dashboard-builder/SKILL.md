---
name: dashboard-builder
description: Create or update a LeadJourney dashboard with report cards (channel, campaign, creative, or custom reports) so the user has a recurring view of marketing performance.
---

Use this skill when the user wants a dashboard, wants a report "saved" or "pinned", asks for a weekly/monthly overview they can return to, or wants to add a chart to an existing dashboard.

## Inputs to establish

1. **Workspace.** `get_current_workspace`; switch if needed.
2. **New or existing dashboard.** Call `list_dashboards`. If a dashboard with a matching name exists, add to it rather than creating a duplicate. Confirm with the user when the match is only approximate.
3. **Which reports.** Each card is a report. Clarify the date range behaviour (rolling last 30 days vs fixed period) and the metric the user cares about.

## Steps

1. Call `describe_report_builder` once to get the valid metric and dimension ids. A card takes the same arguments as `run_report`, so every id must come from this response.
2. For each requested card, call `run_report` first and check that it returns rows. A card built from a report that returns nothing renders as an empty tile; fix the arguments before adding it.
3. If creating: call `create_dashboard` with a clear name. If adding: use the existing dashboard id.
4. Call `add_dashboard_report` once per card, with the verified `run_report` arguments and a card title the user will understand.
5. Only call `remove_dashboard_report` or `delete_dashboard` when the user explicitly asks to remove or delete, and confirm the target by name before doing so. Deletion cannot be undone.

## Output

- Dashboard name and a list of the cards added, each as `title — metric by dimension, date range`.
- If any requested card could not be built (metric not available, empty results), say which one and why, and suggest the closest alternative from `describe_report_builder`.

## Do not

- Do not guess metric or dimension ids.
- Do not delete or remove anything without an explicit instruction naming the dashboard or card.
- Do not add more than the user asked for; suggest extra cards in one line instead of creating them.

Explicit user instructions override these defaults.
