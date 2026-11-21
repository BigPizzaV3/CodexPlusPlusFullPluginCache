---
name: analyze-marketing-metrics
description: Query Kipify marketing metrics and inventory across Meta Ads, Google Ads, GA4, Search Console, Shopify, Magento, and blended Kipify metrics via the connected Kipify MCP server.
---

# Analyze marketing metrics with Kipify

Use this skill when the user asks about ads performance, ecommerce metrics, SEO search demand, inventory restock / score, or cross-channel marketing results available through their Kipify account.

## Prerequisites

- The Kipify MCP server must be connected and authorized.
- Prefer tools that match the granted OAuth scopes. If a tool returns authentication or insufficient-scope errors, ask the user to reconnect Kipify and grant the needed connectors.

## Workflow

1. Call `list_my_connectors` to see which connectors the user authorized.
2. **If the user asks about inventory, restock, riassortimento, score, markup, stock, or scorte: call `query_inventory` first** (needs `mcp:shopify` or `mcp:magento`). Do **not** invent a custom priority score. Do **not** rebuild ranking from `query_metrics`.
   - Prefer **one** `view=products` call: for "last 30/7/90 days" **omit** `start_date`/`end_date` (server matches Kipify UI and ends yesterday — do not invent a today-ending calendar range). Pass dates only for explicit calendar windows. `low_stock_only=true`, `limit=15`. Sorted by `dailySalesRate`. Paginate with `offset`/`next_offset` if needed.
   - Optional: `view=replenishments` (same dateRange filters `restockedDate`), `limit=20`, paginate if `has_more`.
   - Add `include_variants=true` only if sizes/SKU are needed.
   - **Kipify score = markup (revenue/COGS)** — context; keep the returned order (sales/day, like Kipify). Default window = last 30 days ending yesterday. Never drop rows by score/median unless the user asked a threshold (`min_score`); never invent reorder quantities. Prefer a short markdown table + top images via `![title](imageUrl)`.
3. For ads/analytics (not inventory score): call `list_accounts`, then `list_metrics_catalog`, then `query_metrics`.
4. If `has_more` is true, paginate with `offset` / `next_offset` until complete or the user asks for a summary of the first page.
5. For Google Search Console SEO deep-dives, use `analyze_search_console` with `opportunities`, `cannibalization`, or `search_appearance` when that fits better than a raw metric query.
6. For database connectors with SQL access, use `list_schema` / `profile_table` before `run_readonly_sql`. Prefer catalog/query_metrics when virtual metrics exist.

## Output rules

- Cite the connector, account, date range, and metric keys used.
- Do not invent metrics or account IDs that were not returned by tools.
- Surface sampling, thresholding, or compatibility warnings from the tool response when present.
- For inventory, cite score as markup, state scoreQuality/scoreTone (Kipify red→green vs store median), and show product images when `imageUrl` is returned.
- Refuse destructive, write, payment, or out-of-scope account access requests.
