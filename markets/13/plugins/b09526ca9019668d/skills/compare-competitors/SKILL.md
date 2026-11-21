---
name: compare-competitors
description: Compare a site with its SEO competitors in Sight AI: who they are, the keywords they rank for that the site does not, their top pages, share of voice and SERP features, and turn the gaps into tracked keywords. Use when the user asks who their competitors are, what competitors rank for, or how they compare in Google.
---

Use this skill when the user wants to understand or act on competitors. Reads need no confirmation; changing the competitor list, adding keywords and uncached domain lookups do.

## Pick the site

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.

## Who the competitors are

2. Call `get_seo_competitors` for the current list (up to ten domains) and the side-by-side numbers from the latest snapshots: organic keywords and traffic, top 3 and top 10 counts, domain rank, backlinks, referring domains.
3. If the list is empty or the user wants suggestions, tell them it is a paid lookup, then call `suggest_seo_competitors`: domains that share the site's search results, with how many keywords they share.
4. To change the list, confirm the domains and call `add_seo_competitor` or `remove_seo_competitor` with the `domain`, or `set_seo_competitors` with the whole list to replace it. New domains get their keywords pulled in the background; say the comparison fills in over the next minutes.

## What they rank for

5. Call `get_competitor_keywords` with `view` "summary" for the headline numbers, per-competitor stats, article groups (keywords grouped by the competitor page that covers them) and brand plays such as "competitor alternatives" or "competitor pricing" articles.
6. For rows, call it with `view` "keywords" and filter: `kind` "missing" (the site does not rank), "behind" (ranks worse) or "ahead"; `competitorDomain` for one competitor; `minVolume` and `maxDifficulty` for the easy wins; `brand` "exclude" to drop branded searches.
7. Call `get_competitor_pages` for each competitor's top pages by estimated traffic, flagged when new since the previous refresh.
8. Call `get_seo_serp_features` to see who owns the AI Overview, featured snippet, People also ask and other features, and `get_seo_visibility` for the visibility index and share of voice over time.
9. For any domain not on the list, `explore_domain` gives the organic overview, top keywords, backlink summary and top pages. It is served from a seven-day cache when one exists; an uncached lookup is paid and capped per day, so check `get_seo_explore_recent` first and confirm before a fresh one.

## Act on the gaps

10. To track gap keywords, confirm the picks and call `add_competitor_keywords` with the rows' `opportunityIds` (up to 100). Use `dismiss_competitor_keyword` for a row the user rejects. To pull fresh competitor data, call `refresh_competitor_keywords` (queued; `force` ignores the 24-hour freshness window).

## Do not

- Do not call `suggest_seo_competitors`, `explore_domain` with `refresh`, or a competitor refresh without saying it spends the site's lookup budget.
- Do not change the competitor list without naming the domains and getting a yes.
- Do not rank competitors by anything other than the numbers the tools return.
