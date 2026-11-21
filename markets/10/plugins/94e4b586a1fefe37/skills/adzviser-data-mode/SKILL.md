---
name: adzviser-data-mode
description: Retrieve and analyze reporting from the user's connected Google Analytics 4 properties with Adzviser. Use for active users, sessions, traffic channels, devices, comparisons, trends, raw rows and Data Mode. This plugin does not edit analytics settings, delete collected data or identify individual visitors.
---

# Google Analytics Data Mode

Use `retrieve_reporting_data` for reporting and analysis. Use the preview skill
only when the user explicitly requests an interactive report. Do not open a
widget after direct retrieval merely to display the same request.

## Minimal reporting workflow

1. Call `list_workspace` and select the user's named Google Analytics workspace.
   Explain missing access instead of substituting a different property. If no
   workspace is named and several choices remain, ask which to use.
2. Call `list_metrics_and_breakdowns_ga4` and use the exact returned metric and
   breakdown names. Request only fields necessary for the question.
3. Resolve inclusive YYYY-MM-DD date pairs using the current date. Last month
   means the previous complete calendar month; last week means the previous
   complete Monday-Sunday week unless otherwise specified. Use the property's
   reporting timezone, not an assumed UTC conversion.
4. Send `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.ga4_request` containing `metrics`
   and optional `breakdowns`. Include both periods in one comparison request.
   No other source keys are supported by this plugin.
5. Read `structuredContent.reportingData.GA4.data`, a header-first row array,
   and relevant `note_of_assumption` values. Use actual headers and returned
   shape rather than hard-coded column positions from an example.
6. Answer with the requested figures, workspace, exact dates and material
   limitations. Reuse successful results instead of repeating identical queries.

Do not send conversation history, the raw prompt, unrelated context, credentials,
personal identifiers, session tokens or arbitrary destinations as report inputs.
`reporting_mode=data` selects this workflow; it is not a tool argument. Do not
send `client_id`, `reporting_mode` or `_widget_action`. `set_reporting_mode` is
an app-only preference control. Do not invent filters, sorting or limits; sort
returned rows locally when needed.

## Interpret GA4 reporting

- Active users, Total users, New users and Sessions are distinct measures. Use
  the one requested. For active users last week, request Active users over the
  full week without time_granularity; do not substitute the 7-day active users
  metric or sum daily users into a supposedly deduplicated weekly total.
- Users can appear across dates or groups. Do not sum device, channel or daily
  user counts and label the result as distinct property-wide users. Request the
  relevant ungrouped period when a distinct total is needed.
- Use Session default channel group for session-channel reporting. First-user,
  session and conversion-attributed dimensions describe different scopes; do not
  substitute them silently. Retain Unassigned, (not set), unknown and other
  returned groups rather than dropping them.
- Present the source's device categories as returned. An absent tablet row is
  not a retrieved zero. Do not infer individual identities from aggregate data.
- Check totals when comparing grouped and ungrouped reports. If they differ,
  show the difference and the relevant report scopes. Do not alter a row, invent
  a balancing category, or silently claim equality. Do not attribute a discrepancy
  to sampling, thresholds, privacy controls or a server bug without evidence.
- Use `time_granularity` for Date, Week, Month or Quarter, not invented time
  breakdowns. Daily rows may be sorted by metric value; sort them by actual date
  for a timeline. Missing dates are not evidence of zero traffic.
- Preserve the exact metric definition and units for rates, engagement durations
  and conversions. Do not treat Conversions, Event count, purchase counts and
  user counts as interchangeable. Clarify an ambiguous conversion/event request.
- Do not average percentages across groups. Use the correct numerator and
  denominator for a derived rate. A zero comparison baseline has no finite
  percentage change. Never invent a currency for revenue or advertising costs.
- Distinguish observed reporting from interpretation. No rows means no returned
  data, not proven zero activity. Surface supplied assumptions and limitations.

For an unsupported field, refresh discovery, correct the request once and retry.
Explain authentication, access or compatibility errors without inventing success.

The connector provides reports. It cannot create or alter key events, change
tracking or property settings, install tags, grant access, delete collected data,
or reveal names, email addresses or physical addresses of individual visitors.
Explain unsupported requests without calling reporting tools to simulate those
actions or inventing personal data.
