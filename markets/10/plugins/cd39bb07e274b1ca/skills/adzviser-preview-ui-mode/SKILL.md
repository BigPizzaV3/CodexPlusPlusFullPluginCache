---
name: adzviser-preview-ui-mode
description: Open an interactive report for the user's connected Shopify store so they can inspect, edit and run it. Use only for an explicit Preview UI, UI Mode, embedded or interactive report request. Use Data Mode for ordinary numeric questions and calculations.
---

# Shopify Preview UI

Use `preview_and_retrieve_reporting_data` only when the user explicitly asks for
an interactive report. Ordinary sales, order, product, audit and comparison
questions use `retrieve_reporting_data` through the Data Mode skill.

Call `list_workspace` and use the named Shopify workspace. Ask when none is named
and multiple suitable choices remain. Call `list_metrics_and_breakdowns_shopify`
for exact field labels. Request only the fields needed for the question. Resolve
relative dates from the current date: last month is the previous complete
calendar month and last week is the previous complete Monday-Sunday week unless
otherwise specified. Use the store's reporting timezone.

Send one `adzviser_request` with `workspace_name`, inclusive `date_ranges`,
optional `time_granularity`, and `assorted_requests.shopify_request` containing
`metrics` and optional `breakdowns`. Never include conversation history, the
raw prompt, unrelated context, credentials or caller-selected destinations.
Do not send `client_id`, `reporting_mode` or `_widget_action`; mode controls are
app-only. Do not invent filters, sorting, limits or other source keys.

Use Currency for money and preserve separate currency groups. Treat blank,
null or literal "None" currency as unspecified, not USD. Keep negative sales
and adjustments as returned. Gross sales, Net sales, Total sales, Items and
Orders are distinct measures. Include Product ID with Product title when needed.
Do not request customer contact details for aggregate reporting. Use
`time_granularity` for time series instead of invented time breakdowns.

Open the preview once and let the component handle editing, Run and mode controls.
The initial preview is not a completed report. Do not immediately follow it with
a direct retrieval or claim to have analyzed hidden component state. Analyze
only rows made visible to the model, use Data Mode for raw-data requests, and
preserve returned assumptions, no-data results and access errors.

This plugin does not edit the store, process refunds, delete records, place
purchases or send emails. Do not present a report as completing any such action.
