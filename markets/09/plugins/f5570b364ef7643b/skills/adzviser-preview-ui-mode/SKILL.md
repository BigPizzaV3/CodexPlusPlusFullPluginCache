---
name: adzviser-preview-ui-mode
description: Open Adzviser's interactive Pipedrive report preview when the user explicitly asks to inspect, edit, or run a report in the widget. Use Data Mode for ordinary questions, raw rows, calculations, comparisons, or analysis.
---

# Pipedrive Preview UI Mode

Call `preview_and_retrieve_reporting_data` only for an explicitly requested
interactive report. This plugin supports Pipedrive only. Use
`retrieve_reporting_data` when the user wants the model to analyze numbers.

## Prepare the preview

1. Call `list_workspace` and choose the user's requested Pipedrive workspace.
   Report unavailable access rather than silently switching workspaces.
2. Call `list_metrics_and_breakdowns_pipedrive` and use exact supported labels.
3. Resolve relative dates into inclusive YYYY-MM-DD date pairs using the current
   date. Use all requested periods in one `date_ranges` list.
4. Build `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and the object `assorted_requests.pipedrive_request` with
   `metrics` and optional `breakdowns`.
5. Open the preview once and let the user operate its controls. Do not call the
   data tool merely to duplicate the widget's Run action.

Never pass `client_id`, `reporting_mode` or `_widget_action`, and do not call the
app-only `set_reporting_mode` control from the conversation.

## Preserve the report's meaning

Date ranges select deals and leads by creation date. Status, stage and value are
current returned attributes, not historical snapshots. Do not turn a request
for deals closed during a period into a creation-date report without explaining
the limitation and agreeing on the changed scope when needed.

Discover deal and lead metrics independently and use matching breakdowns. Use
`Deal status` for current deal states, `Deal currency` for deal amounts and
`Lead currency` for lead amounts. Pipeline, stage and owner fields return IDs,
not names. Use `time_granularity` for Date, Week, Month or Quarter rather than
placing those labels in breakdowns. Do not invent sorting or filter parameters.
Only request contact fields when they are relevant to the user's task.

## Respect the preview result

The preview response configures the widget; it is not proof that a report has
run or that rows are available for analysis. If the component later publishes
model-visible rows, inspect the separate Deals and Leads tables under
`structuredContent.reportingData.Pipedrive.data`. Do not use hidden `_meta` as
report data. Keep currency amounts separate and describe an empty table honestly.
If the user changes to analysis or raw rows, switch to `retrieve_reporting_data`.
