---
name: adzviser-data-mode
description: Retrieve and analyze reporting from the user's connected Google Ads accounts with Adzviser. Use for spend, clicks, conversions, campaign comparisons, trends, raw rows and Data Mode. Use the account-management skill for current settings, edits, permissions and receipts. Public competitor ad-library searches are not supported.
---

# Google Ads Data Mode

Call `retrieve_reporting_data` for questions about numbers. Use the preview
skill only for an explicitly requested interactive report; do not open a widget
after a successful direct retrieval merely to display the same request.

## Minimal report request

1. Call `list_workspace` without arguments. Use the user's named workspace. If
   it is unavailable, explain the access problem rather than substituting one.
   When multiple suitable workspaces exist and none was named, ask which to use.
   Reports include all connected Google Ads accounts in that workspace; account
   selection for an edit is a separate step in the management workflow.
2. Call `list_metrics_and_breakdowns_google_ads` without arguments and use the
   exact returned field labels. Request only metrics and dimensions needed for
   the user's question; do not select an entire catalog or default to all data.
3. Resolve inclusive YYYY-MM-DD date pairs using the current date. Last month is
   the previous complete calendar month; last week is the previous complete
   Monday-Sunday week unless the user specifies otherwise. Report dates follow
   the source account's reporting timezone, not an invented UTC conversion.
4. Send `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.google_ads_request` containing
   `metrics` and optional `breakdowns`. Include both periods in one comparison
   request. No other source keys are supported by this plugin.
5. Inspect each header and row under
   `structuredContent.reportingData.GoogleAds.data`. Results are grouped into
   tables such as Account or Campaign; `data` is not itself a single flat table.
   Surface relevant `note_of_assumption` text.

Never send the full conversation, chat history, raw user prompt, unrelated
context, credentials, email addresses or session tokens as report inputs. Select
field names and dates from the question instead. `reporting_mode=data` is routing
intent, not a tool argument. Do not send `client_id`, `reporting_mode` or
`_widget_action`; `set_reporting_mode` is an app-only preference control.

## Google Ads interpretation

- Cost, Clicks, Impressions and Conversions are valid examples; confirm current
  labels through discovery. Do not guess similar labels or invent filters,
  query text, sorting, limits, arbitrary URLs or a natural-language input field.
- Include Account Currency Code when reporting monetary amounts. Keep currencies
  separate. Cost can be returned as `$ Cost`; use the actual column header and
  currency, and do not divide an already formatted amount by a million again.
- Use Campaign ID with Campaign Name to distinguish campaigns. Additional source
  context columns may be returned; summarize only what answers the question.
- Conversions can be fractional due to attribution. Do not round them to whole
  people, substitute All Conversions, or call conversion value collected revenue.
- For CTR, request Clicks and Impressions and calculate clicks / impressions × 100.
  Use N/A for a zero denominator; aggregate from totals rather than averaging
  percentages. Use the returned units for other rates and ROAS.
- Use `time_granularity` for Date, Week, Month or Quarter rather than adding those
  labels to breakdowns. Daily dates may be returned in a Date Range column.
- Empty/header-only tables mean no matching returned rows. Do not invent zero
  rows for missing dates or groups. A zero comparison baseline has no finite
  percentage change. Distinguish a partial period from a complete one.
- Never use `google_ads_transparency_request` here. The plugin supports connected
  account reporting and supported management, not competitor or public-ad searches.
- Preserve returned account IDs and names when comparing campaigns. Keep duplicate
  campaign names in different accounts distinct; never combine currencies. Do
  not invent account identifiers if a legacy report omits them.

For an unsupported field, refresh discovery and correct the request once. For
an authentication or access error, explain the returned issue without claiming
the report succeeded. Reuse successful rows instead of repeating the request.

## Continue from analysis to an account edit

For supported Google Ads edits, resource settings, access permissions or saved
change receipts, use `adzviser-account-management`. Do not describe all budget
and bid changes as unsupported. Discover current support with `get_resources`
using `source=google_ads` and the intended workspace and advertiser.

A performance question or recommendation does not authorize preparing changes,
enabling write access, or applying edits. When the user requests an edit, match
the selected account and campaign to discovered resource references and inspect
current settings. Use `preview_changes`, show its actual effects, and apply only
after confirmation of that exact saved preview. A reporting result or report
preview is not an account-change preview. Reuse available reporting evidence
rather than fetching the same report again.
