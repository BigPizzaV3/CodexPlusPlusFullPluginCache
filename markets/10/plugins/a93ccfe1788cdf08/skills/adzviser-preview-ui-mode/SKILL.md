---
name: adzviser-preview-ui-mode
description: Open an interactive report for the user's connected Meta Ads account so they can inspect, edit and run it. Use only for an explicit Preview UI, UI Mode, embedded or interactive report request. Use Data Mode for ordinary numeric questions and calculations. Do not use for previewing or applying account changes, connection permissions, or change receipts.
---

# Meta Ads Preview UI

Use `preview_and_retrieve_reporting_data` only for an explicitly requested
interactive report. Ordinary spend, purchase, audit and comparison questions
use `retrieve_reporting_data` through the Data Mode skill.

Call `list_workspace` and use the named workspace. If none is named and multiple
choices remain, ask. Call `list_metrics_and_breakdowns_fb_ads` with that workspace
for exact available labels and custom conversions. Request only the needed fields.
Resolve dates from the current date: last month is the previous complete calendar
month; last week is the previous complete Monday-Sunday week unless otherwise
specified. Use the advertising account's reporting timezone.

Send one `adzviser_request` with `workspace_name`, inclusive `date_ranges`,
optional `time_granularity`, and `assorted_requests.fb_ads_request` containing
`metrics` and optional `breakdowns`. No other source keys are supported. Never
include conversation history, the raw prompt, unrelated context, credentials,
email addresses or caller-selected destinations. Do not send `client_id`,
`reporting_mode` or `_widget_action`; the mode tool is app-only.

Use Account Currency for money and Campaign ID with Campaign Name when needed.
Preserve the requested conversion event: Website Purchases is not Actions or a
count of unique customers. Publisher Platform may include more than Facebook and
Instagram. Use `time_granularity` for time series and do not invent report filters.

Open the preview once and let its component handle editing, Run and mode controls.
The initial preview is not a completed report. Do not immediately follow it with
direct retrieval or claim to have analyzed hidden component state. Analyze only
rows made visible to the model; switch to Data Mode when the user asks for raw
data. Preserve returned assumptions and report no-data or access errors honestly.

For current settings, campaign or ad set renames and pauses, connection
permissions, or change receipts, use `adzviser-account-management` and
`source=fb_ads` for resource discovery. `preview_changes` previews an account
edit; `preview_and_retrieve_reporting_data` previews a report. Running a report
or changing its presentation mode does not approve an account edit.

This plugin cannot reveal individual audience members or search the public
Meta Ad Library. Explain unavailable actions without using a report as a
substitute for the requested action.
