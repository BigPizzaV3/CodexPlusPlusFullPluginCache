---
name: period-comparison
description: "Compares two periods across ad platforms and analytics through the Pilot MCP server: spend, results and ratios for Google Ads and Meta Ads, sessions and key events in Google Analytics 4, clicks in Search Console, with the change for each and its main drivers. Use when the user asks to compare two weeks, months, quarters, or this year against last year. Triggers: compare periods, month over month, year over year. Déclencheurs : comparer deux périodes, ce mois contre le mois dernier, évolution sur un an, comparaison de périodes."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with at least one platform attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_cross_platform_overview google_list_accounts google_get_campaign_performance meta_list_accounts meta_compare_periods_performance google_analytics_run_report google_search_console_get_search_analytics"
  pilot-mcp-read-only: "true"
---

# Period comparison

Put two periods side by side, platform by platform, and explain what drove the difference. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace concerned.
- **Optional MCP servers:** a file storage server or spreadsheet server to keep the table. None is needed.
- **Read-only:** never call a tool that creates, updates, pauses or deletes anything.

## Tools

- `pilot_cross_platform_overview`: consolidated spend and results for a window of days.
- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_get_campaign_performance`: Google Ads campaigns for any start and end dates.
- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_compare_periods_performance`: Meta results for two preset periods.
- `google_analytics_run_report`: GA4 figures for two date ranges in one call.
- `google_search_console_get_search_analytics`: organic clicks and impressions for a date range.

## Steps

1. Fix the two periods with exact dates. They should have the same length; if not, say so and compare daily averages.
2. Google Ads: `google_list_accounts`, then `google_get_campaign_performance` with `start_date` and `end_date` for each period.
3. Meta Ads: `meta_list_accounts`, then `meta_compare_periods_performance` with the closest presets (for example `last_7d`, `last_30d`, `last_month`); say when a preset does not match the dates exactly.
4. GA4: `google_analytics_run_report` with both periods in `dateRanges` and the metrics that matter (`sessions`, `keyEvents`, `totalRevenue`).
5. Search Console: `google_search_console_get_search_analytics` for each period, ending two days ago at most.
6. Use `pilot_cross_platform_overview` for a consolidated view when the periods end today.

## Output

1. **Table**: one row per platform and metric, with period A, period B, the change in value and in percent.
2. **Drivers**: the campaigns, channels or queries behind the largest changes.
3. **Caveats**: unequal lengths, presets that differ from the dates, data delays.

## Rules

- Never add amounts in different currencies.
- A change on an empty base is not a percentage: write the values instead.
- Name the exact dates of both periods.

## Examples

- "Compare September with August across Google Ads and Meta."
- "Compare ce trimestre au même trimestre l'an dernier."
- "Qu'est-ce qui explique l'écart entre les deux dernières semaines ?"
