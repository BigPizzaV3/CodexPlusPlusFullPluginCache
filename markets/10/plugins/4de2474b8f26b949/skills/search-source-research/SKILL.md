---
name: search-source-research
description: Retrieve Bing or DuckDuckGo results with HasData, or compare those explicitly requested search engines. Use for engine-specific web results, not Google News, Trends, Scholar, Images or organic rank tracking.
---

# Research Bing and DuckDuckGo results

Read `../hasdata-research/SKILL.md` and the Search sources section of `../hasdata-research/references/tool-catalog.md`.

Use `hasdata_bing_serp_getSearchResults` or `hasdata_duckduckgo_serp_getSearchResults` with q for the explicitly requested engine. Despite DuckDuckGo's empty required array, keyword discovery still needs a query. Do not substitute Google for a named engine or call both when only one was requested.

Keep source-specific localization: Bing exposes location and its own market/language fields; DuckDuckGo has its own kl/country/language options. Inspect the live schema rather than sending Google's location/uule/gl parameters to another engine. Omit first/nextPageToken for an initial page.

Return actual original URLs, titles, snippets and source context. Use returned positions only where present; display order is not necessarily a published rank field. If comparing engines, keep their query and localization differences visible and do not assume identical inventories or ranking systems.

For Google sources, use the focused News, Trends, Scholar, Images, short-video or event skill through `../hasdata-research/SKILL.md`. Further pages use supported offsets or actual returned tokens within the agreed budget.
