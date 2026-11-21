---
name: keywords
description: Keyword research, search-term mining and negative keywords with Opus Growth for Google Ads and Microsoft Advertising - Keyword Planner ideas and volumes, match types, which search terms to add or exclude, shared negative lists and keyword cleanup. Use when the user asks for keywords, negatives, search terms, or why ads show for the wrong searches.
---

# Keywords and search terms

Follow the `opus-growth` skill. Keep two sources apart:
- **Planner data** (what could be searched): `google_ads_keyword_planner` for new ideas with
  volumes and competition, `google_ads_keyword_historical_metrics` for month-by-month volume of
  known keywords. Set the location and language; without them volumes are global.
- **Search terms** (what people actually typed and clicked): `google_ads_search_terms_report`,
  `microsoft_search_terms_report`. This is where money leaks.

Do not pad a short planner result with invented keywords, and do not present planner volume as
traffic the account will get.

## Building a keyword set

- Group by intent: one ad group per theme, so the ad text can match the search.
- Match types: exact for the proven money terms, phrase for the main themes, broad only with
  conversion tracking and Smart Bidding that has data. Broad match without good conversion data
  buys irrelevant traffic.
- Add per-item match types in one call: `google_ads_add_keywords` with `text|EXACT`.
- Existing converting search terms that are not keywords yet: `google_ads_keyword_opportunities`.

## Mining search terms

1. Pull 30-90 days (`google_ads_search_terms_report`; `only=waste_candidates` or sort by cost).
2. Converting terms → add as exact or phrase keywords.
3. Clearly irrelevant terms → negatives. Ranked candidates: `google_ads_negative_keyword_suggestions`.
4. Unclear terms with little data → leave them; check again later.

Rows marked `already_negative` are already blocked: do not add them again.

## Negative keywords

- Negatives do not match close variants or synonyms. Add singular and plural, common
  misspellings and both spellings with and without accents.
- Phrase negative "free" blocks any search containing "free"; exact negative [free trial] blocks
  only that search; broad negative blocks searches containing all its words in any order.
- Never add a negative that also blocks the converting searches: compare each candidate with the
  converting terms before adding (a dealer that sells used cars must not add "used" as a
  negative just because "used tyres" wasted money).
- Level: campaign level for a whole campaign, ad group level to route traffic between ad groups,
  shared list (`google_ads_manage_shared_negative_list`) for exclusions that apply everywhere
  (jobs, careers, free, DIY, competitors when the user wants).
- Brand campaigns: add the brand as a negative in non-brand campaigns so each campaign gets its
  own traffic.
- Bulk: one `google_ads_add_negative_keywords` call takes a whole list; preview it, show the list,
  then apply.

Microsoft: `add_microsoft_negative_keywords`, `remove_microsoft_negative_keywords`.
TikTok search ads: `manage_tiktok_search_negative_keywords`.

## Cleaning up keywords

- Low Quality Score keywords: `google_ads_keyword_report` shows the three components (expected
  CTR, ad relevance, landing page experience). Fix the weakest component; deleting is the last
  resort.
- Moving keywords: add on the target ad group, then remove from the old one
  (`google_ads_manage_keywords` action remove).
- Keyword "Eligible" is not the same as serving: low search volume or a paused ad group means it
  shows nothing.
