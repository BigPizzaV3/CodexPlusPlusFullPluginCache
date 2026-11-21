---
name: adzviser-preview-ui-mode
description: Open an interactive report for the user's connected Google Analytics 4 property so they can inspect, edit and run it. Use only for an explicit Preview UI, UI Mode, embedded or interactive report request. Use Data Mode for ordinary numeric questions and calculations.
---

# Google Analytics Preview UI

Use `preview_and_retrieve_reporting_data` only for an explicitly requested
interactive report. Ordinary traffic, user, session and comparison questions
use `retrieve_reporting_data` through the Data Mode skill.

Call `list_workspace` and use the named Google Analytics workspace. Ask when no
workspace is named and multiple suitable choices remain. Call
`list_metrics_and_breakdowns_ga4` for exact field names and request only necessary
fields. Resolve relative dates using the current date: last month is the previous
complete calendar month and last week is the previous complete Monday-Sunday
week unless otherwise specified. Use the property's reporting timezone.

Send one `adzviser_request` with `workspace_name`, inclusive `date_ranges`,
optional `time_granularity`, and `assorted_requests.ga4_request` containing
`metrics` and optional `breakdowns`. No other source keys are supported. Do not
include conversation history, the raw prompt, unrelated context, credentials,
personal identifiers or caller-selected destinations. Do not send `client_id`,
`reporting_mode` or `_widget_action`; mode controls are app-only. Do not invent
filter, sorting, limit or other undeclared arguments.

Keep Active users, New users, Total users and Sessions distinct. Use session
dimensions for session acquisition questions. Avoid time grouping when the user
wants the distinct user total for an entire period. Use `time_granularity` for
requested time series, and preserve unknown groups, missing data and assumptions.
Do not force grouped and ungrouped totals to agree or invent a cause for a
discrepancy. Never infer visitor identities from aggregate reporting.

Open the preview once and let the component handle editing, Run and mode controls.
The initial preview is not a completed report. Do not immediately follow it with
direct retrieval or claim to analyze hidden component state. Analyze only rows
made visible to the model and use Data Mode when the user asks for raw data.

This plugin does not edit analytics settings, change key events, install tracking,
delete collected data or reveal individual visitors' contact details. A reporting
preview must not be presented as completing any such action.
