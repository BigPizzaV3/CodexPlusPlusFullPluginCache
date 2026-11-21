---
name: get-started
description: How to answer questions about the user's own marketing, e-commerce, analytics and CRM data with the Detrics tools. Use when the user asks about their ad spend, campaigns, conversions, ROAS, sessions, sales, orders, email revenue or CRM metrics, or asks which platforms, accounts, metrics or dimensions are available in Detrics.
---

# Detrics: query the user's connected marketing data

Detrics exposes the user's own connected platform accounts (Meta Ads, Google Ads, GA4, TikTok Ads, LinkedIn Ads, Shopify, Klaviyo, HubSpot and 30+ more). Everything is read-only against accounts the user has already connected in their Detrics workspace.

## Typical flow

1. **Find the connection.** Call `list_connections` once to learn which platforms and accounts are connected. Reuse the result for the rest of the conversation. If the user has saved an AI Context, `list_contexts` / `get_context` give you a preset group of accounts to use instead.
2. **Find the field names.** Field names differ per platform. When unsure, call `list_fields` with the `platform_api` (for example `facebook-ads`, `google-ads`, `google-analytics-4`, `shopify-store`, `klaviyo`) and pick exact metric and dimension names from the response. Large catalogs return a category index first; narrow with `search` or `category`.
3. **Query.** Call `query_marketing_data` with the platform, the account ids, the metrics, the dimensions (add a date dimension for time series), the timeframe (presets such as `last_7_days`, `last_30_days`, `last_month`, `this_month`, or a custom start/end), and optional filters, sorting and limit.
4. **Present.** Return a compact table plus totals and a one or two sentence interpretation. State the date range and the account used.

## Rules of thumb

- One platform per `query_marketing_data` call. For cross-platform comparisons run one query per platform and combine the results yourself.
- Keep queries small: a few metrics, one or two dimensions, sorted and limited when the user asks for "top N".
- If a query returns `invalid_fields`, use the `did_you_mean` suggestions or call `list_fields` and retry; do not guess field names.
- If a connection needs re-authorization, the response includes a `connection_repair_url`; give it to the user.
- `connect_platform` starts an OAuth flow and returns a URL the user must open; use `check_connection_status` to poll until it completes. Only use these when the user explicitly wants to connect a new platform.
- Warehouse tools (`get_warehouse`, `manage_warehouse_*`) manage Detrics data transfers to BigQuery. The `manage_*` tools can change or delete transfers and tables; confirm with the user before any destructive action.
- Do not use Detrics for general marketing advice, for data about companies the user has not connected, or for anything unrelated to the user's own accounts.
