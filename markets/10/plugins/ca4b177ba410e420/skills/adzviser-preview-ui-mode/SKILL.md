---
name: adzviser-preview-ui-mode
description: Open an interactive Amazon Ads report so the user can inspect, edit and run the reporting request. Use only for an explicit Preview UI, UI Mode, embedded or interactive report request. Use Data Mode for ordinary numeric questions, calculations and comparisons.
---

# Amazon Ads Preview UI

Use `preview_and_retrieve_reporting_data` only for an explicitly requested
interactive report. Ordinary spend, clicks, campaign and trend questions use
`retrieve_reporting_data` through the Data Mode skill.

Call `list_workspace` and select the named Amazon Ads workspace. Ask when no
workspace is named and multiple suitable choices remain. Call
`list_metrics_and_breakdowns_amazon_ads` for exact fields and request only what
is necessary. Resolve relative dates from the current date: last week is the
previous complete Monday-Sunday week unless otherwise specified. Respect the
source reporting timezone and the current 60-day start-date lookback limit.
Explain unsupported dates instead of silently changing the requested period.

When the user asks for an N-day period ending two days ago, let D be the current
date in the user's timezone and use [D-(N+1), D-2], inclusive. For seven days use
[D-8, D-2]; its preceding comparison period is [D-15, D-9]. Exclude yesterday
and today, state the actual dates, and do not substitute a calendar week.

Send one `adzviser_request` with `workspace_name`, inclusive `date_ranges`,
optional `time_granularity`, and `assorted_requests.amazon_ads_request` containing
`metrics` and optional `breakdowns`. No other data-source keys are supported.
Do not include conversation history, the raw prompt, unrelated context,
credentials, personal identifiers or caller-selected destinations. Do not send
`client_id`, `reporting_mode` or `_widget_action`; mode controls are app-only.
Do not invent filter, sorting, limit or other undeclared arguments.

Keep monetary values in their reported currencies, distinguish campaigns with
IDs when names repeat, and retain attribution windows for purchases, sales,
ACOS and ROAS. Use `time_granularity` for a time series. Preserve missing data
and assumptions rather than inventing zeros or complete coverage.

Open the preview once and let the component handle editing, Run and mode controls.
The initial preview is not a completed report. Do not immediately follow it with
direct retrieval or claim to analyze hidden component state. Analyze only rows
made visible to the model and use Data Mode when the user asks for raw data.
If reporting is still being prepared, surface that state honestly; opening the
preview does not bypass backend data availability.

The plugin does not edit campaigns, bids or budgets, purchase ads or products,
change store listings, or reveal individual shoppers' names or contact details.
A reporting preview must not be presented as completing any such action.
