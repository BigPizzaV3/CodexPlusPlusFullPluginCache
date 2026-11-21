---
name: adzviser-preview-ui-mode
description: Open an interactive report for the user's connected Google Ads account so they can inspect, edit and run it. Use only for an explicit Preview UI, UI Mode, embedded or interactive report request. Use Data Mode for ordinary numeric questions and calculations. Use account management for previewing or applying account edits, permissions or change receipts.
---

# Google Ads Preview UI

Use `preview_and_retrieve_reporting_data` only when the user explicitly wants
an interactive report. Ordinary spend, performance, audit and comparison
questions use `retrieve_reporting_data` through the Data Mode skill.

Call `list_workspace` and `list_metrics_and_breakdowns_google_ads` without
arguments. Select the named workspace and exact requested metric/breakdown
labels. If access is unavailable, explain the problem without substituting a
different workspace. Resolve dates from the current date: last month is the
previous complete calendar month; last week is the previous complete
Monday-Sunday week unless otherwise requested.

Send one `adzviser_request` with `workspace_name`, inclusive `date_ranges`,
optional `time_granularity`, and `assorted_requests.google_ads_request` containing
`metrics` and optional `breakdowns`. Include only fields and dates needed for
the report. Never include the full conversation, raw prompt, chat history,
unrelated context, credentials or caller-selected destinations. Do not send
`client_id`, `reporting_mode` or `_widget_action`; the mode tool is app-only.

Use Account Currency Code for money and keep currencies separate. Cost can be
returned as `$ Cost` and is already formatted; do not convert it from micros
again. Conversions may be fractional. Include Campaign ID when distinguishing
campaigns. Use `time_granularity` for daily/weekly/monthly/quarterly reports,
not an invented time breakdown. Do not invent arbitrary filters or source keys.

Open the preview once and let the component handle editing, Run and mode
controls. The initial preview is not a completed report. Do not immediately
follow it with a direct retrieval or claim to have analyzed hidden component
state. Analyze only rows actually published to the model; if the user asks for
raw data, use Data Mode. Preserve returned assumptions and no-data results.

For changes to Google Ads settings, use `adzviser-account-management` and
`get_resources` with `source=google_ads` to discover supported edits and targets.
`preview_changes` previews an account edit; `preview_and_retrieve_reporting_data`
previews a report. Never use the report widget or its Run button as approval of
an advertising-account or permission change. Apply only an exactly confirmed
saved change and inspect its receipt. Do not describe all budget and bid changes
as unsupported. Billing, campaign deletion and public competitor-ad searches
remain outside this plugin's supported workflows.
