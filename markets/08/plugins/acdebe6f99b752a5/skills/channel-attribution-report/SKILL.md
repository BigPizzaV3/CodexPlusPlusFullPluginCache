---
name: channel-attribution-report
description: Report which traffic channels, campaigns, or ad creatives are producing leads and revenue in the user's LeadJourney workspace for a date range, and compare them.
---

Use this skill when the user asks where their leads come from, which channels or campaigns perform best, how marketing performance changed over a period, or wants a comparison between channels, campaigns, or creatives.

## Inputs to establish

1. **Workspace.** Call `get_current_workspace`. If the user names a different client or brand, call `list_workspaces` and `switch_workspace` before anything else.
2. **Date range.** If the user does not give one, default to the last 30 days and say so. If the user says "this month", use the current calendar month to date and state the exact dates used.
3. **Level of detail.** Channel → `get_traffic_channel_report`. Campaign → `get_campaign_report`. Creative → `get_ad_creative_report`. If the question spans two levels ("which Google Ads campaign brought the most leads"), start at the channel report and drill into the campaign report for that channel.

## Steps

1. Run the fixed report that matches the level of detail for the date range.
2. If the fixed reports do not contain the metric or dimension the user asked for (for example revenue per lead by landing page), call `describe_report_builder` first, then `run_report` with ids taken only from that response. Never invent metric or dimension ids; an invented id returns empty rows instead of an error.
3. Rank results by the metric the user cares about. Default to lead count; use revenue when the user mentions ROI, revenue, or value.
4. For comparisons, run the same report for both periods or both channels and present them side by side.

## Output

- A short table with the name (channel, campaign, or creative) and the metrics the report actually returns, such as leads and revenue. Only show columns that have data in the response; do not add empty columns.
- One to three sentences of interpretation: the leader, the biggest mover, and anything that looks off (a channel with traffic but zero leads, for example).
- State the date range and workspace name once at the top.

## Do not

- Do not invent numbers, fill gaps, or extrapolate trends beyond what the report returns.
- Do not present zero rows as "no leads" without first checking that the date range and workspace are the ones the user meant.
- Do not create dashboards, tags, or links from this skill; if the user wants the report saved, hand off to the dashboard-builder skill.

Explicit user instructions override these defaults.
