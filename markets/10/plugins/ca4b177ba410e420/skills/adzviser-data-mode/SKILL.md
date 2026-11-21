---
name: adzviser-data-mode
description: Retrieve and analyze reports from the user's connected Amazon Ads accounts with Adzviser. Use for spend, impressions, clicks, campaign reporting, comparisons, trends, raw rows and Data Mode. This plugin cannot change campaigns, bids or budgets, or identify individual shoppers.
---

# Amazon Ads Data Mode

Use `retrieve_reporting_data` for reporting and analysis. Use the preview skill
only when the user explicitly requests an interactive report. Do not open a
widget after direct retrieval merely to display the same request.

## Minimal reporting workflow

1. Call `list_workspace` and use the user's named Amazon Ads workspace. Explain
   missing access instead of substituting another account. Ask which workspace
   to use when none is named and several suitable choices remain.
2. Call `list_metrics_and_breakdowns_amazon_ads`. Use the exact returned metric
   and breakdown names, requesting only fields necessary for the question.
3. Resolve inclusive YYYY-MM-DD date pairs from the current date. Last week
   means the previous complete Monday-Sunday week unless otherwise specified.
   For the review and starter prompts ending two days ago, let D be the current
   date in the user's timezone: an N-day period is [D-(N+1), D-2], inclusive.
   Seven days therefore means [D-8, D-2]; the preceding seven days are
   [D-15, D-9]. Exclude yesterday and today. State the actual dates and do not
   reinterpret these prompts as last calendar week or freeze an example date.
   Respect the source reporting timezone. The current connector rejects start
   dates more than 60 days ago; do not silently shorten a requested period or
   substitute another period. Explain the limit and ask for a supported range.
4. Send one `adzviser_request` with `workspace_name`, `date_ranges`, optional
   `time_granularity`, and `assorted_requests.amazon_ads_request` containing
   `metrics` and optional `breakdowns`. Include both date pairs in a comparison
   request. No other data-source request keys are supported by this plugin.
5. Inspect every returned source/date segment and its actual headers and rows
   in `structuredContent.reportingData`, including `note_of_assumption` values.
   Use text/CSV content only as a fallback when structured data is absent.
6. Answer with the requested numbers, exact dates, workspace, units and material
   limitations. Reuse successful results instead of repeating identical queries.

Do not send conversation history, the raw prompt, unrelated context, credentials,
personal identifiers, session tokens or arbitrary destinations as report inputs.
`reporting_mode=data` selects this workflow; it is not a tool argument. Do not
send `client_id`, `reporting_mode` or `_widget_action`. `set_reporting_mode` is
an app-only preference control. Do not invent filters, sorting or limits; sort
or calculate from returned rows locally when needed.

## Interpret Amazon Ads reports

- Use `Spend` for ad costs and preserve the returned currency. Include `Currency`
  for monetary reports when it is needed to distinguish account currencies.
  Never add different currencies together or infer USD from an unlabeled amount.
- Use `Campaign ID` alongside `Campaign name` to distinguish campaigns with the
  same name. Include other account identifiers only when needed for the question.
- Use `time_granularity` for requested Date, Week, Month or Quarter series. Do
  not add those time labels to `breakdowns`. Sort returned dates chronologically.
- Calculate CTR from Clicks / Impressions * 100. A zero impressions denominator
  makes CTR unavailable. Do not average group-level percentages to get a total.
- Keep attribution windows explicit for sales, purchases, ACOS and ROAS. Use
  catalog fields with the requested window; do not mix 7-day and 14-day measures
  or confuse attributed sales with all store revenue. Do not invent unavailable
  combinations of ad products, metrics or breakdowns.
- Preserve the units returned for rates and ratios. For derived ACOS or ROAS,
  use matching attribution scope and currency, label the calculation, and handle
  zero denominators. Do not multiply an already percentage-valued rate again.
- For comparisons, calculate recent minus earlier and percentage change using
  the earlier value as the denominator. Zero baselines have no finite percentage
  change. Compare like-for-like currencies and report scope.
- Do not treat missing dates or empty results as proven zero activity. Explain
  partial coverage, assumptions and unavailable data without inventing rows.

If the server reports that Amazon Ads data is still being prepared, explain that
reporting is temporarily unavailable until background reporting completes.
This response is not successful retrieval and does not establish zero spend.
Do not repeatedly poll the same failed query, silently narrow its dates, switch
into Preview UI as a workaround, or claim to have refreshed the backend. Retry
when the user requests it or new evidence indicates the data is ready.

For an unsupported field, refresh discovery, correct the request once and retry.
Explain authentication, access, date-limit or compatibility errors honestly.

This connector retrieves reports. It cannot create or pause campaigns, edit
bids or budgets, purchase ads or products, change store listings, or reveal the
names or contact details of individual ad viewers, clickers or buyers. Explain
unsupported requests without calling reporting tools to simulate those actions.
