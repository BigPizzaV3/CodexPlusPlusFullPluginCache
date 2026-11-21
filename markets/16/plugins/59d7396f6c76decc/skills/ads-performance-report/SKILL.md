---
name: ads-performance-report
description: Use when the user asks for a report or analysis of paid advertising performance (Google Ads and/or Meta Ads, i.e. Facebook and Instagram ads) for a brand: spend, conversions, ROAS, campaigns or search terms.
---

Analyze a brand's advertising performance and suggest improvements. Read-only flow: nothing is changed in the ad accounts. Reply in the user's language.

1. Call `list_brands`, confirm the brand and the period (`start_date` and `end_date` as `YYYY-MM-DD`; by default the last 30 full days).
2. **Google Ads** (if connected):
   - `ads_compare` for the period totals and the change against the previous period.
   - `ads_campaigns` for the per-campaign breakdown, sorted by cost.
   - `ads_search_terms` with `order_by = "cost"` to find searches that spend without converting (covers Search and Shopping campaigns only).
   - For more detail: `ads_ad_groups` and `ads_ads` (live query), or `ads_timeseries` to locate a spike.
3. **Meta Ads** (if connected):
   - `meta_ads_compare` for the totals and the change.
   - `meta_ads_campaigns` for the per-campaign breakdown.
   - `meta_ads_structure` with a `campaign_id` to see ad sets, ads and creatives.
   - Messaging campaigns report their result in `messaging_conversations`, which is not included in `conversions`.
4. Write the report:
   - Summary per platform: spend, clicks, CTR, CPC, conversions, ROAS and change.
   - Best and worst performing campaigns, with the reason.
   - Wasted spend: terms or campaigns with cost and no conversions.
   - Concrete recommendations (budget, negative keywords, creatives, targeting), noting that changes are made in the ad account itself.

Rules:
- Make MCP calls one at a time.
- Never add Google Ads and Meta Ads into a single figure: present them separately, each in its own currency.
- Do not invent metrics; if a platform is not connected, say so.
