---
name: weekly-performance-report
description: "Builds a weekly multi-platform advertising report through the Pilot MCP server: consolidated spend and results across Google Ads and Meta Ads, week-over-week changes, budget pacing and the traffic seen in Google Analytics 4. Use when the user asks for a weekly report, a weekly recap or last week's performance. Triggers: weekly report, weekly recap, how did last week go. Déclencheurs : rapport hebdomadaire, bilan de la semaine, récap hebdo, point de la semaine dernière."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with at least one ad platform attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_data_freshness pilot_cross_platform_overview pilot_budget_pacing google_list_accounts google_get_campaign_performance meta_list_accounts meta_get_account_performance_summary meta_compare_periods_performance google_analytics_run_report"
  pilot-mcp-read-only: "true"
---

# Weekly performance report

Produce a one-page weekly report across the ad platforms of the workspace: what was spent, what it brought, what changed against the previous week, and what to watch. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace to report on.
- **Optional MCP servers:** a file storage server to save the report, a team messaging server to post it to a channel, a note-taking server to archive it. None is needed to build the report.
- **Read-only:** never call a tool that creates, updates, pauses or deletes anything, on Pilot or on any other server.

## Tools

- `pilot_data_freshness`: whether the collected data covers the week.
- `pilot_cross_platform_overview`: spend and results consolidated across platforms, ratios computed on totals.
- `pilot_budget_pacing`: campaigns capped by their budget, and budgets left idle.
- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_get_campaign_performance`: Google Ads campaigns over the week.
- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_get_account_performance_summary`: Meta account KPIs over the week.
- `meta_compare_periods_performance`: Meta results this week against the previous week.
- `google_analytics_run_report`: sessions and key events by channel in Google Analytics 4.

## Steps

1. Call `pilot_data_freshness`. If a platform is stale, say so at the top and treat its figures as partial.
2. Call `pilot_cross_platform_overview` with `days: 7`, then with `days: 14`; derive the previous week as the difference. If the tool refuses a money total because currencies differ, report each currency separately.
3. Google Ads: call `google_list_accounts`, then `google_get_campaign_performance` with `date_range: "LAST_7_DAYS"` for each attached account. Keep the five campaigns with the most spend and the largest changes.
4. Meta Ads: call `meta_list_accounts`, then `meta_get_account_performance_summary` with `date_preset: "last_7d"` and `meta_compare_periods_performance` with `period1: "last_7d"` and `period2: "last_14d"`. The second period contains the first: the previous week is the difference.
5. Call `pilot_budget_pacing` with `days: 7` to flag capped and idle budgets.
6. If a Google Analytics 4 property is attached, call `google_analytics_run_report` with `dateRanges` for the last 7 days and the 7 days before, `dimensions: ["sessionDefaultChannelGroup"]` and `metrics: ["sessions", "keyEvents"]`.
7. Write the report.

## Output

1. **Headline**: total spend, total conversions or value, and the change against last week, in one sentence.
2. **By platform**: a table with spend, conversions, cost per conversion and the week-over-week change.
3. **What moved**: the three largest changes, with their likely cause when the data shows it.
4. **Budget**: capped and idle budgets.
5. **To watch next week**: two or three points.

## Rules

- State the dates covered and the currency of every amount.
- Never add amounts in different currencies.
- A ratio with an empty denominator is not available, not zero.
- Skip a platform the workspace has not attached, without treating it as an error.

## Examples

- "Give me the weekly report for this workspace."
- "Fais-moi le rapport hebdomadaire Google Ads et Meta, avec les variations."
- "How did last week go compared with the week before?"
