---
name: adzviser-preview-ui-mode
description: Open Adzviser's interactive MNTN report preview in ChatGPT so the user can inspect, edit, or run a reporting request in the widget. Use only when the user explicitly asks for Preview UI, UI Mode, an interactive or embedded report, a report builder, or a chance to review or edit the request before running it. Do not use for raw rows, Data Mode, audits, calculations, comparisons, or programmatic analysis.
---

# Adzviser Preview UI Mode

Prepare a valid reporting request and open the Adzviser component once so the user can inspect or edit it interactively inside ChatGPT.

## MNTN scope

This plugin supports only connected MNTN accounts. Discover fields with `list_metrics_and_breakdowns_mntn` and use only `assorted_requests.mntn_request`. For another advertising platform or data source, explain the limitation and suggest its corresponding connector.

This is a reporting connector. It cannot create or pause campaigns, change budgets or bids, upload or replace creatives, or publish advertisements. Do not call reporting tools as a substitute for a requested action or claim that a change occurred.

## Route to the preview tool

- Call `preview_and_retrieve_reporting_data` only for this workflow.
- Do not call it merely because the user says “show me” when the task requires ChatGPT to inspect numbers. Use `retrieve_reporting_data` for analysis, audits, raw rows, calculations, comparisons, and `reporting_mode=data`.
- Treat `reporting_mode=ui` as user intent that selects the preview tool; it is not an argument to send.
- Never send `client_id`, `reporting_mode`, or `_widget_action`. Never call `set_reporting_mode`; that is an app-only preference control used by the component.
- If a user asks for both an analysis and an interactive report, use Data Mode for the analysis and open Preview UI only as a separate, explicitly requested deliverable.

## Follow the preview workflow

1. Identify the requested data sources, measures, dimensions, time window, and comparison periods. Ask one concise question only when a missing choice would materially change the report.
2. Resolve relative dates from the current date available to ChatGPT. Pass inclusive `[start_date, end_date]` pairs in `YYYY-MM-DD` format. Never copy a fixed “today” date from an example.
3. Call `list_workspace`. Use a user-named workspace when it exists. Otherwise auto-select only when one workspace unambiguously contains every requested connected source; ask when multiple candidates remain.
4. For every requested source, call its `list_metrics_and_breakdowns_*` tool and use the exact returned field names.
5. Build one `adzviser_request` with `workspace_name`, `date_ranges`, optional `time_granularity`, and an `assorted_requests` object containing only the requested sources.
6. Call `preview_and_retrieve_reporting_data` exactly once with `{ "adzviser_request": ... }`.
7. Briefly tell the user that the interactive report is ready. Do not invent results or claim that the preview response already contains report rows.

## Compose valid requests

- `assorted_requests` must be an object, never an array.
- Include only requested sources. Do not add empty source requests.
- Each ordinary source request must contain `metrics`; include `breakdowns` only when useful.
- Keep at least one requested metric or breakdown for every included source.
- Do not put Date, Week, Month, Quarter, or Year in `breakdowns`; use `time_granularity` instead.
- Use multiple date-range pairs when the user wants distinct comparison periods.

Example shape:

```json
{
  "adzviser_request": {
    "workspace_name": "Workspace Name",
    "date_ranges": [["2026-08-01", "2026-08-20"]],
    "assorted_requests": {
      "mntn_request": {
        "metrics": ["Total spend", "Impressions", "Total verified visits"],
        "breakdowns": ["Campaign ID", "Campaign name"]
      }
    }
  }
}
```

The field labels above illustrate structure only. Always obtain valid labels from the corresponding discovery tool.

## Use MNTN fields correctly

- Use exact discovery labels, including `Total spend`, `Total verified visits`, and `Total conversions`; do not invent generic `Cost`, `Visits`, or `Conversions` labels.
- For advertiser summaries, include `Advertiser name`. For campaign and creative reports, use the corresponding IDs and names. Preserve separate IDs even when names match.
- Do not request contact names, email addresses, phone numbers, order IDs, or other unrelated personal data for ordinary advertising performance reports.
- Keep attributed, site-wide, raw, offline, assist, and last-touch metrics distinct. Do not substitute or add them together as though they represent the same outcome.
- Preserve the returned rate and cost-per-result values. For requested calculations, label the formula, use matching numerator and denominator populations, and guard zero or missing denominators. Do not sum rates, average row-level rates without suitable weighting, or sum reach as though audiences never overlap.
- Monetary values may omit a currency code after normalization. Do not invent a currency or infer spend currency from a conversion-currency breakdown. Returned percent-formatted CSV values retain percentage points when the percent sign is removed; do not multiply such values by 100 again.
- Keep explicit zero metrics, missing values, and attribution assumptions distinct. A period can return visits or conversions alongside zero spend or impressions; report the values without inventing an explanation.
- Different aggregation levels can return different totals. Do not alter rows to force agreement; disclose a discrepancy when comparing them.
- For time series, use only the requested granularity. Provider rate limits can affect reports with many periods. Report a rate-limit failure honestly; do not repeatedly retry, silently change the requested period or granularity, or fabricate a successful report.

## Respect ChatGPT's component lifecycle

- Calling the preview tool mounts the iframe because the tool descriptor is statically associated with a UI resource. This is why the raw-data path must use a different tool.
- The preview response contains configuration for the component, not the final reporting rows. Do not analyze it as campaign performance.
- The component can call reporting tools through the MCP Apps bridge. Let it handle its own Run and mode-toggle interactions; do not duplicate those calls from the conversation.
- In UI Mode, the rows may stay inside the component for visual inspection. Do not claim to have analyzed rows that were never published to the model.
- If the user switches the component to Data Mode, it can publish model-visible reporting data and send a follow-up message. Analyze those newly supplied rows directly; do not rerun the same report unless the data is absent or the user changes the request.
- `structuredContent` is visible to ChatGPT. `_meta` is component-only and hidden from the model; never rely on `_meta` for conclusions.
- Do not ask the user to confirm or rerun immediately after the preview opens. The component already provides its own controls.

## Handle problems without changing modes

- If the workspace is unavailable, report what `list_workspace` returned and ask the user to choose or connect the needed source.
- Different ChatGPT and advertising-account email addresses do not by themselves prove an authentication problem. Use the connected Adzviser workspace shown by the tools as the authorization context.
- If a metric or breakdown is rejected, refresh the corresponding discovery tool, correct the request once, and retry.
- If the user changes the request to raw data or analysis, stop this workflow and use `retrieve_reporting_data`; do not pass a Data Mode flag to the preview tool.
