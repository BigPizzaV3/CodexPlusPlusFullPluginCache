---
name: traffic-sources
description: Rank OpenRevenue referrers, pages, or countries for a site. Use when the user asks about sources, channels, referrers, landing pages, or geographic breakdown. Do not use for headline traffic totals, funnels, goals, visitors, or performance.
---

# Traffic sources

Use this skill when the user wants where visitors come from, which pages perform, or the country mix for a site they can access.

1. Resolve `domain` (ask, or call `list_projects` if needed).
2. Default period `7d` unless the user specifies otherwise.
3. Call the matching read tools:
   - Sources: `get_referrers`
   - Pages: `get_pages`
   - Geography: `get_countries` (and `get_cities` only if asked)
4. Cite only tool results. Rank by the metrics returned.
5. Do not invent referrer names, pages, countries, or percentages.

If a tool errors or access is denied, say so and stop.
