---
name: ads-all-clients-overview
description: Use when the user wants an overview of Google Ads and Meta Ads across several or all of their clients or brands, for example to see which accounts spend the most, which ones dropped or which need attention this week.
---

Give an agency a cross-client view of its ad accounts. Read-only: nothing is changed in the ad accounts. Reply in the user's language.

1. Call `list_brands` and keep the brands whose `connected_platforms` show `google_ads` or `meta_ads`. If none do, say so and stop.
2. Confirm the period (`start_date` and `end_date` as `YYYY-MM-DD`; by default the last 7 full days compared with the previous 7).
3. For each brand, one call at a time:
   - Google Ads connected: `ads_compare`.
   - Meta Ads connected: `meta_ads_compare`.
4. Build one table per platform with a row per brand: spend, clicks, conversions, cost per conversion, ROAS when there is conversion value, and the change against the previous period.
5. Flag what needs attention: spend up with conversions down, accounts with spend and no conversions, sharp drops in delivery, and any account whose data could not be read.
6. Offer to go deeper on a flagged brand with `ads_campaigns`, `ads_search_terms`, `meta_ads_campaigns` or `meta_ads_structure`.

Rules:
- Make MCP calls one at a time, never in parallel.
- Never add Google Ads and Meta Ads into one figure, and never add brands that use different currencies: keep each in its own currency.
- Meta "conversions" are the events each campaign optimizes for (leads, purchases, sign-ups...), not necessarily sales; say which when you can.
- Do not invent metrics; if a brand's platform is not connected or returns an error, say so in its row.
