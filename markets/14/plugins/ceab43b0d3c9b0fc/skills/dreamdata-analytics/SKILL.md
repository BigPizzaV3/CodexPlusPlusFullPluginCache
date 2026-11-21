---
name: dreamdata-analytics
description: Analyze and build Dreamdata reports and dashboards, inspect company journeys, and drill into report metrics. Excludes audience discovery, querying, and saving; use dreamdata-activation for those workflows.
---

# Dreamdata analytics

Use the connected Dreamdata MCP tools. Tool names below are suffixes; their host namespace can vary. If the connection is unavailable, follow the bundled [setup skill](../setup/SKILL.md) to help the user authenticate and verify access.

Audience workflows belong to the separate [activation skill](../dreamdata-activation/SKILL.md). For mixed requests, use each skill for its relevant portion.

## Account and analysis context

Use `list_my_accounts` when the intended account is unknown. Select the account from the user's context; ask if several accounts remain plausible. Keep its slug consistent throughout the analysis. One-account users can omit the slug.

Make the account, reporting period, filters, metric definitions, and attribution model clear where they affect the answer. Preserve the user's chosen scope. Distinguish attributed revenue from causal impact, missing data from zero, and a partial result page from the complete population. Link returned source URLs when available; do not invent report links.

## Saved reports

Discover report IDs with `list_saved_reports`; resolve ambiguous names before running. Use `run_saved_report` for the saved period or `run_saved_report_for_date_range` for a requested date override, which does not persist changes. Omit `output_type` initially to discover supported slices.

For entities contributing to a specific metric, use `list_report_metric_drilldown_entities`. A report-defined company/contact view is not the same as a metric drilldown.

Report responses may contain `nextPageTokens` by slice or `nextPageToken`. Continue a slice by passing its token as `page_token` together with the same `slug` as the call that returned it, and no other arguments; later responses use `next_page_token`. Without the slug, users with several accounts get an account-selection error instead of the next page. Fetch enough pages to support the requested conclusion and disclose any incomplete coverage. Do not compute population totals or rankings from an incomplete slice.

## New reports

Start with `report_builder_start` and follow its ordered workflow. Discover the analysis type, subject, and components using the returned tools. Use only returned metric, property, subject, and attribution-model IDs. Request an exact metric group when stage-specific filter properties are needed.

Pipeline outcomes are the account's own stages, listed by `report_builder_list_subjects`; names vary between accounts (one has Closed Won, another NewBiz). Map the user's outcome to one of those stages before choosing metrics. Loose terms such as "new companies", "new customers", "leads" or "deals" don't name a metric: if exactly one stage clearly matches, use it and say which; if several could (for example Closed Won and NewBiz), or none does, ask which stage the user means. Never substitute a different metric silently, and if no report offers what was asked, say so and offer the closest stage-based alternative.

Validate user-named filter values with `report_builder_search_property_values`; use `report_builder_list_property_values` for browsing. Resolve named calendar periods and rolling windows using the corresponding `report_builder_resolve_calendar_period` or `report_builder_resolve_rolling_window` tool. Use the returned time filter instead of hand-calculating those windows.

Run with `report_builder_run_config`, initially omitting `output_type` to discover supported slices. Correct structured validation errors using the discovered components. If the same unresolved error repeats, report the limitation instead of looping. Running validates the config but does not save it.

Only use `report_builder_save_report` when the user explicitly requests saving. Pass the exact config last run successfully. Follow the server's confirmation protocol: present the preview's name, description, and folder; obtain the user's confirmation; then submit the same arguments with the returned confirmation token. If the server handles confirmation through elicitation, let it do so. Never invent a token or confirm for the user. Saved reports are visible to others on the account.

## Company journeys

Use `search_companies` to resolve a company and its opaque ID. For stage-specific analysis, discover stage instances with `list_company_journey_stages`; repeated stage names can have different timestamps and IDs. Fetch the journey with `get_company_journey` using the selected instance where relevant.

The journey's `sessions_grouped` is compressed, not sampled. A group has a timestamps array and a touchpoint count; sparse quantity/conversion/signal maps refer to timestamp indices. Do not count groups as individual touches. A bare date represents midnight UTC. Describe observed touchpoints and stage timing without implying that sequence alone proves causation.

## Currency
When get_account_currency is available, use it before attaching currency symbols to report amounts. Report values use the account currency; do not infer it from the user's location. If currency cannot be established, show amounts without an assumed symbol and explain the limitation.

## Dashboards

When create_dashboard is exposed and the user requests a dashboard, follow its current schema and preview/confirmation flow. It requires the optional dashboards:write grant. Show the proposed layout and widgets before saving. Use the live tool descriptions as the authority for these operations.
