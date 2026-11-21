---
name: adzviser-data-mode
description: Retrieve and analyze model-visible, row-level AdRoll advertising data with Adzviser. Use when the user asks for Data Mode, reporting_mode=data, raw rows, an audit, calculations, comparisons, trends, insights, optimization recommendations, or any answer that requires ChatGPT to inspect the underlying numbers. Do not use when the user explicitly wants only the interactive Preview UI.
---

# Adzviser Data Mode

Use Adzviser as the source of truth for connected AdRoll advertising data. Retrieve the actual rows, inspect them, and answer the user's question with evidence from those rows.

## AdRoll scope

This plugin supports only connected AdRoll accounts. Discover fields with `list_metrics_and_breakdowns_adroll` and use only `assorted_requests.adroll_request`. For another advertising platform or data source, explain the limitation and suggest its corresponding connector.

This is a reporting connector. It cannot create or pause campaigns, change budgets or bids, upload or replace creatives, or publish advertisements. Do not call reporting tools as a substitute for a requested action or claim that a change occurred.

## Route to the data tool

- Call `retrieve_reporting_data` for this workflow.
- Never call `preview_and_retrieve_reporting_data` for Data Mode. That tool is bound to an iframe and will render the embedded report instead of serving as the raw-data path.
- Treat `reporting_mode=data` as user intent that selects `retrieve_reporting_data`; it is not an argument to send.
- Never send `client_id`, `reporting_mode`, or `_widget_action`. They are internal compatibility fields, not model inputs.
- If a user asks for both analysis and an interactive report, retrieve and analyze the rows first. Open Preview UI afterward only if the user explicitly requested that additional deliverable.

## Follow the reporting workflow

1. Interpret the question and identify the requested data sources, measures, dimensions, time window, and comparison periods. Ask one concise question only when a missing choice would materially change the report.
2. Resolve relative dates from the current date available to ChatGPT. Pass inclusive `[start_date, end_date]` pairs in `YYYY-MM-DD` format. Never reuse a fixed date from an example or an older conversation.
3. Call `list_workspace`. Use a user-named workspace when it exists. Otherwise auto-select only when one workspace unambiguously contains every requested connected source; ask when multiple candidates remain.
4. For every requested source, call its `list_metrics_and_breakdowns_*` tool. Use the exact returned field names. Do not guess close variants.
5. Build one `adzviser_request` with:
   - `workspace_name`, except for a documented source that does not require it;
   - `date_ranges` containing every requested period;
   - optional `time_granularity` when the user requests a time series;
   - `assorted_requests` as an object keyed by source request name, `adroll_request` for this plugin.
6. Call `retrieve_reporting_data` once with `{ "adzviser_request": ... }`.
7. Inspect all data sources, date-range segments, headers, rows, and `note_of_assumption` values in `structuredContent.reportingData`. Use the text/CSV content only as a fallback when structured content is absent.
8. Answer with the requested numbers first, then material patterns and practical recommendations supported by the data. State the workspace, sources, and exact date ranges used when they help the user verify the result.

## Compose valid requests

- `assorted_requests` must be an object, never an array.
- Include only requested sources. Do not add empty source requests.
- Each ordinary source request must contain `metrics`; include `breakdowns` only when useful.
- Keep at least one requested metric or breakdown for every included source.
- Do not put Date, Week, Month, Quarter, or Year in `breakdowns`; use `time_granularity` instead.
- Use multiple date-range pairs in one call when the user asks for several periods, including overlapping windows such as the last 30, 14, and 7 days.
- Adzviser does not apply arbitrary report filters. Retrieve the fields needed to identify rows, then filter or calculate from the returned data.

Example shape:

```json
{
  "adzviser_request": {
    "workspace_name": "Workspace Name",
    "date_ranges": [["2026-08-01", "2026-08-20"]],
    "time_granularity": "Date",
    "assorted_requests": {
      "adroll_request": {
        "metrics": ["Cost (USD)", "Impressions", "Clicks"],
        "breakdowns": ["Advertiser name"]
      }
    }
  }
}
```

The field labels above illustrate structure only. Always obtain valid labels from the corresponding discovery tool.

## Use AdRoll fields correctly

- Use exact discovery labels. Spend is `Cost (USD)` or `Cost (account currency)`, not a guessed `Spend` field. Ad group labels are `Adgroup EID` and `Adgroup name`.
- Keep `Cost (USD)` in USD regardless of the advertiser's account currency. Use an explicit currency label for account-currency metrics; do not assume two monetary fields share a currency.
- Preserve campaign, ad group, and ad EIDs even when names match. For advertiser summaries, include `Advertiser name` and, when useful, `Advertiser currency`.
- Keep `Conversions`, `Attributed conversions`, `Click-through conversions`, and `View-through conversions` distinct. Use the requested definition; do not silently substitute or add overlapping measures.
- For calculated CTR use `100 * Clicks / Impressions`; for calculated CPC use `Cost (USD) / Clicks` and label USD. Calculate aggregate rates from aggregate counts, not averages of row-level rates. Mark zero or missing denominators as N/A.
- Do not relabel `ROI` as ROAS or invent a `ROAS` metric. When asked to calculate revenue divided by spend, first establish that the returned revenue and spend use the same currency and period, label the formula, and guard zero or missing spend.
- Keep explicit zero metrics, missing values, and attribution assumptions distinct. A response with headers but no rows does not prove zero spend or zero activity. State that no rows were returned for that request and disclose the limitation.
- Request only performance fields needed for the user's question. Do not request conversion cookies, external conversion data, individual visitor identifiers, or other unrelated personal data for aggregate advertising reports.
- For time series, use `time_granularity`. Retain exact returned dates and check that they cover the requested inclusive range. Do not invent missing dates, relabel an incomplete period as complete, or silently extend the user's date range to work around a server error.
- Report upstream errors or rate limits honestly. Do not repeatedly retry or silently switch workspace, currency, period, or granularity to manufacture a successful report.

## Respect ChatGPT's result boundaries

- `structuredContent` is model-visible and is the preferred basis for analysis. Do not claim the rows are inaccessible when they are present there.
- `_meta` is hidden from the model. Never depend on it for analysis or describe it as returned report data.
- Do not call the preview tool after a successful retrieval merely to display the same request.
- Do not repeat an identical retrieval because a widget or follow-up message appears. Reuse model-visible rows already present in the conversation.
- If a response has headers but no data rows, say that no rows were returned for the requested fields and period. Do not conclude that activity or spend was zero, silently switch modes, or invent values.
- If a field or request is rejected, refresh the relevant discovery tool output, correct the request once, and retry. Do not work around schema errors by adding internal parameters.

## Produce a useful analysis

- Distinguish facts in the rows from interpretations and recommendations.
- For audits, check totals and the requested entity-level breakdowns before recommending changes.
- For comparisons, calculate both absolute and percentage changes when denominators are valid; flag zero or missing baselines.
- Preserve units and currency as returned. Do not assume currencies match across accounts or sources.
- Mention assumptions supplied by Adzviser and any material limitations such as missing rows, partial periods, or unavailable fields.
