---
name: etsy-keyword-opportunity-research
description: Research and compare Etsy keywords with eRank data, including keyword statistics, side-by-side comparisons of up to 20 keywords, related searches, top-ranking listings, Trend Buzz trends, and saved keyword lists. Use when the user wants to evaluate keywords for a product or niche, find related search terms, see which listings rank for a keyword, or explore trending keywords.
---

# Etsy keyword opportunity research

Help the user find and compare Etsy keywords using eRank data.

The user's explicit instructions take priority over this guidance. If they name keywords, tools, a country, a marketplace, a number of results, or an output format, follow that. Use the defaults below only for what they leave open.

## Choose the market

- Default to Etsy in the United States: `marketplace` `etsy` and `country` `usa`. Trend Buzz uses uppercase country codes, so its default is `USA`.
- If the user names a country or region, pass its code. eRank's Etsy keyword data covers `usa`, `gbr`, `aus`, `can`, `fra`, `deu`, `ind`, `eea` (European Economic Area), and `glo` (global). Trend Buzz accepts codes such as `USA`, `GBR`, `CAN`, `EEA`, and `GLOBAL`.
- Use the same country and marketplace for every call in a comparison so the numbers are comparable.
- If the market matters and the user hasn't said, use the default and state which market the numbers cover. Ask only if the answer would change their decision.
- If a tool rejects a country, marketplace, or period, tell the user. Don't switch to another market without saying so.

## Workflow

1. Identify the seed keyword or product niche. Ask for it only if it's missing.
2. Get keyword data:
   - One keyword: `get_keyword_stats`.
   - Two or more keywords: `get_bulk_keyword_stats`, up to 20 per request. Split longer lists into batches.
3. Expand with `list_related_keywords` when the user wants more ideas or the seed is too broad or too narrow. Use its filters (exact, phrase, or broad match; required or excluded terms) when the user asks for them.
4. Check competition with `list_keyword_top_listings` for the most promising keywords. It returns up to 100 listings in Etsy search rank order, each with its price, shop, and processing time, plus price and processing-time distributions.
5. Use `list_trend_buzz_keywords` when the user asks about trends, seasonality, or what's rising. Periods are `one` (default for Etsy), `seven`, `thirty`, or a past month as `YYYYMM`.
6. If the user mentions a saved eRank keyword list, find it with `list_keyword_lists` and read its terms with `list_keyword_list_terms`.

Searches with the keyword tools count against the account's shared daily keyword search allowance. Repeating the same search on the same day doesn't count again. Don't run searches the user didn't ask for or that won't change the answer.

## Partial and missing data

- Some values can be unavailable on the user's plan. These come back as `null` with a `restrictions` entry marked `plan_limited`. Describe them as "not available on your current plan," never as zero, low, or missing data.
- On plans where `get_bulk_keyword_stats` returns full metrics only for the first keyword:
  - Give the full metrics for that keyword.
  - For the other keywords, report only the fields that came back, such as search trend and character count, and say which metrics are unavailable.
  - Don't rank keywords on metrics that some rows lack. Say that a full comparison isn't possible with the returned data, and offer to look up specific keywords one at a time with `get_keyword_stats`. Each counts as a separate daily search.
- `usage_limited` means the daily allowance is used up: new searches fail until it resets, but searches already run that day can still be repeated. Report the limit and reset time if returned. If a tool says Keyword Tool isn't included in the plan, report that instead of a used-up allowance.
- A `status` of `no_data`, or an empty result, means eRank has no data for that request. Say so instead of estimating.
- Don't recommend upgrading or describe plans or prices.

## Present the results

Unless the user asked for a different format:

- A short summary of the main finding
- A comparison of the strongest candidates, using the returned metrics
- Useful related terms
- What the top-ranking listings have in common
- Suggested next steps

Keep eRank data and your own interpretation clearly separate. Never invent metrics or fill in missing values. Don't promise traffic, rankings, views, or sales.
