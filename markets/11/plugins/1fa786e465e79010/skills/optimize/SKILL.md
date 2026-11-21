---
name: optimize
description: Find and fix wasted ad spend with Opus Growth - search terms and keywords that spend without converting, placements and audiences that never convert, budget pacing, and moving budget to what works across Google Ads, Meta, TikTok, LinkedIn and Microsoft. Proposes each change with its evidence and applies it only after the user agrees to that change.
---

# Optimizing spend

Follow the `opus-growth` skill. This skill proposes; the user decides. Each change gets its own
preview and approval.

## Before cutting anything

1. **Check tracking first.** A campaign that "converts nothing" often converts and reports
   nothing. Run the platform's tracking check (`google_ads_conversion_tracking_health`,
   `list_meta_pixels`, `list_tiktok_pixels`, `list_microsoft_uet_tags`,
   `list_linkedin_conversions`, `chatgpt_ads_conversion_setup`) and look for a conversion count
   that fell to zero on one day. Pausing a working campaign because of a broken tag is the most
   expensive mistake in this work.
2. **Check volume.** Ten clicks without a conversion is not evidence. Judge a keyword, ad or ad
   set only after spend of about three times the target cost per conversion, or about 100 clicks.
3. **Check its role.** An upper-funnel campaign may convert through other campaigns later; look
   at view-through or assisted conversions before cutting it.
4. **Check learning.** Changing a campaign or ad set that is still learning restarts it.

## Where waste hides

| Platform | Look at |
|---|---|
| Google Ads | `google_ads_instant_audit`, `google_ads_search_terms_report`, `google_ads_negative_keyword_suggestions`, `google_ads_account_audit`, `google_ads_keyword_opportunities` |
| Meta | `meta_insights_query` by placement, age and region; ads with high frequency and falling link CTR |
| TikTok | `tiktok_report_query` by placement and audience; ads with low 6-second view rate |
| LinkedIn | `linkedin_campaign_analytics` by creative and company size; audience expansion and Audience Network delivery |
| Microsoft | `microsoft_search_terms_report`, `microsoft_entity_performance_report` |

Shapes of waste:
- Spend with no conversions (after the volume check).
- Conversions far above the target cost: worse than none, because it looks like it works.
- Searches never intended to buy: "free", "jobs", "how to", "DIY", competitor brands, unrelated
  meanings of the keyword. Exclude with negatives (`keywords` skill).
- Brand searches inside a non-brand campaign: not waste; route them (negative in the non-brand
  campaign, keyword in the brand campaign).
- Placements, ages or regions that take budget and never convert (Meta, TikTok, Display).
- Locations outside the service area: Google "presence or interest" targeting, Meta location
  expansion.

## Fixes, from least to most disruptive

1. Negatives and exclusions.
2. Pause the clearly losing keyword, ad or ad set.
3. Bid or target adjustments in small steps.
4. Budget moves: from the campaign with the worst cost per result to the one that is limited by
   budget and converts well (`google_ads_impression_share_analysis` shows "lost to budget").
   Respect the +50% per change and +100% per 24 hours limits.
5. Restructure only when the above are done.

## Pacing

`google_ads_budget_pacing_alerts` projects month-end spend for Google Ads. For other platforms
compare month-to-date spend with the daily budget times days elapsed. An account-level spending
limit can stop everything regardless of campaign budgets.

## Presenting

For each proposal: what, why (the numbers and period), expected effect, and the exact tool call
you will make. Then preview with `confirm=false`, wait for the user's approval of that item, and
apply. Afterwards, read back and set a date to check the effect (usually 7-14 days).
