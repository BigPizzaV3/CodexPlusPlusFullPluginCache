---
name: search-console-analysis
description: "Analyzes Google Search Console data through the Pilot MCP server: queries and pages that gain or lose clicks, pages competing for the same query (cannibalization), click-through rate against position, indexing status of key URLs and sitemaps. Use when the user asks about organic search, SEO performance, Search Console queries or pages. Triggers: Search Console analysis, SEO performance, cannibalization, organic clicks. Déclencheurs : analyse Search Console, requêtes SEO, pages qui perdent des clics, cannibalisation, référencement naturel."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with a Search Console site attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "google_search_console_list_sites google_search_console_get_search_analytics google_search_console_get_url_inspection google_search_console_get_sitemaps"
  pilot-mcp-read-only: "true"
---

# Search Console analysis

Read a site's organic search performance and turn it into a short list of pages and queries to work on. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace where the site is attached.
- **Optional MCP servers:** a file storage server to save the tables, a note-taking server to keep the action list. None is needed.
- **Read-only:** never submit a sitemap or request indexing. Actions are for a person to take.

## Tools

- `google_search_console_list_sites`: the sites attached to the workspace.
- `google_search_console_get_search_analytics`: clicks, impressions, click-through rate and position, by query, page, country, device or date.
- `google_search_console_get_url_inspection`: indexing and coverage status of one URL.
- `google_search_console_get_sitemaps`: submitted sitemaps and their state.

## Steps

1. Call `google_search_console_list_sites`. If several sites are attached, ask which one; pass it as `site_url`. With one site, `site_url` can be left out.
2. Set two periods of equal length, by default the last 28 days and the 28 days before. Search Console data lags by about two days: end the recent period two days ago.
3. Call `google_search_console_get_search_analytics` with `dimensions: ["query"]` for both periods; then with `dimensions: ["page"]`.
4. Call it again with `dimensions: ["query", "page"]` on the recent period to find cannibalization: one query whose clicks split across several pages of the site.
5. Find the pages with many impressions and a click-through rate well below what their position suggests: their title and description deserve work.
6. For the top pages that lost clicks, call `google_search_console_get_url_inspection` with `inspection_url`. Call `google_search_console_get_sitemaps` once.

## Output

1. **Summary**: clicks and impressions for both periods, and the change.
2. **Winners and losers**: queries and pages with the largest changes in clicks.
3. **Cannibalization**: queries split across pages, with the page to keep.
4. **Low click-through rate**: pages to rewrite, with position and impressions.
5. **Indexing**: anything wrong found in inspected URLs or sitemaps.
6. **Action list**: ordered for a person to apply.

## Rules

- Use `row_limit` and narrow the dimensions on large sites: responses over 100,000 characters are cut.
- Position is an average: compare it only between periods of the same length.
- Name the period and the search type (`web` by default).

## Examples

- "Which queries lost clicks over the last 28 days?"
- "Analyse la Search Console du site : pages en baisse et cannibalisation."
- "Quelles pages ont beaucoup d'impressions mais peu de clics ?"
