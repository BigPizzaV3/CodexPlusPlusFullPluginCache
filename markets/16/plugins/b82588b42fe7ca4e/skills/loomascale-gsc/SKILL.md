---
name: loomascale-gsc
description: Analyze the user's connected Google Search Console (GSC) properties with LoomaScale. Use for SEO reports, organic traffic drops, search queries, keyword opportunities, low click-through rate (CTR), average position, URL indexing status and sitemap errors. Read-only. Do not invoke for general SEO definitions, live rank tracking, website crawling, requesting indexing, or Google Ads and Google Analytics reports.
---

# Google Search Console with LoomaScale

Answer SEO and organic search questions with evidence from the user's connected
Google Search Console (GSC) account: traffic changes, keyword and page opportunities,
low CTR, indexing status and sitemap errors. This package connects to
`https://api.loomascale.com/mcp/gsc`. Inspect
available tool descriptions and input schemas; a client may add a namespace to
the tool names used here.

## Resolve the property

Reuse a property already verified in the conversation. Otherwise call
`gsc_list_sites` and pass `site_url` exactly as listed (`sc-domain:example.com` or a
URL-prefix property). It can be omitted when exactly one property is reachable. If
several fit and the task does not identify one, ask which to use.

## Choose the tool that answers the question

| Question | Tool |
| --- | --- |
| Which properties can I access? | `gsc_list_sites` |
| Why did organic traffic change? | `gsc_compare_periods` |
| Which queries or pages should I improve first? | `gsc_find_keyword_opportunities`, `gsc_find_page_opportunities` |
| Clicks, impressions, CTR or position by query, page, country, device or date | `gsc_query_search_analytics` |
| Is this URL indexed, and which canonical did Google pick? | `gsc_inspect_url` |
| Were my sitemaps processed? | `gsc_list_sitemaps` |

Read [Search Console tools](references/search-console.md) for date windows,
filters, pagination and coverage limits.

## Stay read-only

Every tool reads. Nothing requests indexing, submits or deletes a sitemap, or
changes a setting; say so when the user asks, and point to Search Console.

## Handle access and helper tools accurately

- If authorization is missing, expired or lacks a permission, use the link the
  tool returns or the [LoomaScale connections dashboard](https://loomascale.com/dashboard/connections).
  A refusal that names the user's role is Google judging the login's access, not
  something reconnecting fixes.
- For a usage-limit refusal, call `loomascale_check_quota` once and explain the
  allowance or reset it reports. A usage allowance is not an ad budget.
- `loomascale_request_feature` sends a message to the LoomaScale team. Call it
  only when the user asks to send a feature request.

## Return a result the user can assess

Name the property and exact dates (Pacific time). Say whether recent partial days are included. Separate observed changes from possible causes, and label click potential as an estimate.
