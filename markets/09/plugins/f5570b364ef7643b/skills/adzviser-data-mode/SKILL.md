---
name: adzviser-data-mode
description: Retrieve and analyze Pipedrive deal and lead data with Adzviser. Use for Data Mode, raw rows, counts, comparisons, trends, or calculations requiring the underlying records. Use the preview skill only for an explicitly requested interactive report.
---

# Pipedrive Data Mode

Use `retrieve_reporting_data` to obtain model-visible rows. This plugin supports
Pipedrive only. Do not call `preview_and_retrieve_reporting_data` for an ordinary
question about numbers or as a follow-up to a successful data retrieval.

## Build the report

1. Call `list_workspace` and use the user's named Pipedrive workspace. If it is
   unavailable, explain the access problem. Do not silently substitute a workspace.
2. Call `list_metrics_and_breakdowns_pipedrive` and use the exact returned labels.
3. Resolve dates from the current date, using inclusive YYYY-MM-DD start/end pairs.
   Last month means the previous complete calendar month; last week means the
   previous complete Monday-Sunday week unless the user specifies otherwise.
4. Send one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.pipedrive_request` containing
   `metrics` and optional `breakdowns`. Include all comparison periods in that call.
5. Read each header and row in `structuredContent.reportingData.Pipedrive.data`.
   Deals and leads are separate tables under `Deals` and `Leads`; do not assume
   `data` itself is one flat table. Surface `note_of_assumption` when present.

Treat `reporting_mode=data` as a routing preference, not an argument. Never send
`client_id`, `reporting_mode` or `_widget_action`. The `set_reporting_mode` tool
is an app-only presentation control. Do not invent server-side filters, sorting
or limit fields. Retrieve needed fields and calculate from returned rows.

## Interpret Pipedrive correctly

- **Date ranges select creation dates.** Current status, stage and value do not
  establish their values at the end of a historical period. A creation cohort
  grouped by won/lost status does not count every deal closed during that period.
  Explain this limitation when the question asks for close-date reporting; ask
  for a revised scope if that distinction changes the answer. Including a close
  timestamp breakdown does not change the creation-date filter.
- Deal metrics include `Deals`, `Deal value` and `Deal probability`. Lead metrics
  include `Leads` and `Lead value`. Confirm these with discovery rather than
  inventing `Deals Won`, `Revenue`, `Activities` or a conversion-rate metric.
- Use `Deal status` to group deal counts by current status. `Deal value` is a
  summed CRM amount, not recognized revenue or money collected.
- Include `Deal currency` for deal amounts and `Lead currency` for lead amounts.
  Keep currencies separate. Counts can be summed; monetary amounts cannot be
  added across currencies without an explicit supported conversion.
- Use deal fields with deal metrics and lead fields with lead metrics. If both
  entities are requested, process their returned tables separately.
- `Pipeline ID`, `Stage ID` and `Owner ID` are identifiers. Do not invent names
  for them. A table grouped by stage or owner should label the IDs clearly.
- Use `time_granularity` for Date, Week, Month or Quarter. These are not breakdowns.
  Daily tables return a `Date` header; non-daily reports include `Date Range`.
- `Deal probability` averages available probability values. Do not add grouped
  averages or interpret it as an observed conversion rate. A reported zero alone
  does not establish that probabilities were populated.
- Request contact data only when needed for the user's task. `Person email` is
  the linked contact address. `Organization Smart Bcc email` and `Lead CC email`
  are email-logging addresses, not customer contact addresses.

## Check and answer

Keep the requested scope, creation dates and units clear. For comparisons,
calculate changes within each currency and distinguish missing values from zero.
A zero baseline has no finite percentage change. Empty or header-only tables
mean no matching data; do not invent zeros or switch to a widget.

If a field is rejected, refresh discovery and correct the request once. Do not
repeat a successful query simply because a follow-up message appears. Reuse the
returned rows. Pipedrive record edits, deletions, messages and payments are not
provided by this reporting plugin; explain those limits without claiming action.
