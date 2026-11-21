---
name: review-search-performance
description: Review a site's Google rankings and Search Console performance in Sight AI and explain what changed. Use when the user asks how their SEO or organic traffic is doing, which keywords moved, why traffic dropped or grew, or what to fix next.
---

Use this skill when the user wants to know how a site is doing in Google search or why its traffic changed. Every tool here only reads data, so none of them needs confirmation.

## Pick the site

1. Call `list_sites`. If the account has one site, use it. If it has several and the user did not name one, ask which site before calling anything else. Every other tool takes that site's `siteId`.

## Read the data

2. Call `get_seo_overview` for the health tiles, the ranked fix-next actions and the striking-distance keywords. This is the best single summary; start the answer from it.
3. Call `get_seo_rankings` for the tracked keywords with their latest Google position, the 7-day and 30-day change, the ranking URL and competitor positions. Page through with `page` and `limit` when the user wants the whole list.
4. For traffic, call `get_search_overview` with the window the user asked for (`days`), then `get_search_queries` and `get_search_pages` for the queries and landing pages behind it. These come from the site's Google Search Console data.
5. When the user asks why traffic or rankings changed, call `explain_search_change` with the window in `days` (7 to 90, default 28). It compares the window with the same length before it and returns the queries and pages that moved most, lined up with rank moves, lost backlinks, audit error changes and lost Google AI Mode citations, plus a ranked list of likely causes with the numbers behind each. Report those causes in the tool's order.
6. For the alert feed (rank drops, lost page-one positions, lost backlinks, audit errors), call `get_seo_alerts` with `view` set to `feed`.
7. For one keyword's day-by-day history, call `get_seo_keyword_history` with its `keywordId` or `keyword` text.

## Presenting results

- Lead with the change, then the cause, then the suggested action. Quote positions, clicks and impressions exactly as the tools return them, with the window they cover.
- A keyword that "dropped out of the top ten" is one whose latest position is above 10 and whose 7-day change is negative; say both numbers.
- If the SEO module is not on the user's plan, the tool says so and names the plan that includes it. Pass that on and use the Search Console tools, which every plan has.

## Do not

- Do not invent a reason for a change that `explain_search_change` did not return; say the data does not show one.
- Do not estimate traffic value or forecasts from these numbers yourself; `get_seo_forecast`, `get_seo_what_if` and `get_seo_traffic_value` exist for that.
