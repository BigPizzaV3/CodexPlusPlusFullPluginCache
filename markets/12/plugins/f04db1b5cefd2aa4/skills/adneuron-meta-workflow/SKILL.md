---
name: adneuron-meta-workflow
description: Use AdNeuron to read stored Meta and Google Ads account and campaign reports, summarize performance, and rank campaign spend. This release is reporting-only.
---

# AdNeuron reporting
Use the configured remote MCP connection at https://mcp.adneuron.ai/mcp. Let the host complete OAuth sign-in and workspace selection. Never request passwords, tokens, or client secrets in chat. Request read-only access; never request or use write permissions for this release.

## Scope
Read stored data using documented tools. Discover current gateway catalogs before using a platform operation. Only use operations documented as read-only and currently available. This reporting-only package does not authorize platform connections, account synchronization, campaign or budget modifications, publishing, billing changes, or scheduled tasks, even if the server exposes such tools. Explain that those actions are outside this release. Do not use another integration to perform them under this plugin.

## Workflow
- Use list_accounts to resolve actual account IDs and their platform, currency, source, timezone, connection state and freshness. Respect the host-selected authenticated connection. An email in a prompt does not select an account or prove identity. If returned data contradicts the requested workspace, stop and ask the user to select the correct connection in the host.
- Use get_performance_summary for account and platform reports, with supported lookback_days values 7, 30, 60 or 90.
- Use list_top_performers for spend rankings; specify sort_by=spend and the requested limit and lookback_days. This is a spend ranking, not evidence of business effectiveness.
- Use meta_ads and google_ads with action=list_tools to discover available read operations and argument contracts. Execute only necessary read operations against returned IDs.
- For Meta campaigns, list_campaigns and get_campaign_performance can return stored status, budget and metrics.
- For Google campaigns, resolve campaign IDs from returned stored listings and use get_campaign_detail. A top-N result is not necessarily a complete campaign inventory; disclose coverage limits.

## Reporting integrity
Use exact tool-returned complete account-local dates excluding today. Show dates, timezone, currency and data source. A lookback count alone does not establish exact date boundaries. If boundaries are absent, explicitly state that period alignment is unverified; do not silently supply assumed dates.
Distinguish recorded zero from null, missing or unverified metrics. Preserve unavailable Meta conversions and conversion value; do not invent mapping or report a complete combined conversion total when any included outcomes are unavailable.
Aggregate only compatible currencies and identical reporting windows. Withhold mixed-currency totals rather than implicitly converting. Platform conversions may measure different outcomes and do not establish comparable customers, revenue or attribution.
Label sample/fictional records from returned source flags and never describe them as provider-synced live results. No provider sync timestamp is not evidence of fresh live data.
Reconcile campaign/account totals only for the same dates, scope and currency. Disclose excluded campaigns, incomplete coverage or differences. Do not alter values to force reconciliation.
If impressions are zero, CTR is undefined/not meaningful even if the server returns zero. If conversions are unavailable or zero, do not present a meaningful CPA. Do not invent causal explanations, optimization claims or revenue.
State no changes were made only when no mutating operations were called.

## Boundaries
For a nonexistent campaign, report no match without substitution or invented performance. Unsupported platforms such as TikTok are not represented by Google or Meta data. Customer email sending and other unrelated actions are unavailable through this plugin. Clearly distinguish a written draft from a sent message.
On tool failure, describe the actual error and affected scope. Do not claim successful authentication, complete reporting, server-side read-only enforcement, or validation without supporting evidence.
