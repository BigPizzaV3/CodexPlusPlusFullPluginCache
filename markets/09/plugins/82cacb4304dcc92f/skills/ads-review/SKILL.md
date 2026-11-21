---
name: ads-review
description: Prioritize Apple Ads investigations and proposed improvements from Stora spend and search-term evidence, accounting for hidden queries and reporting gaps.
---

Select the app, storefront and period. Read `get_ads_connection`, `get_ads_state`, `get_ads_summary`, `get_ads_campaigns` and relevant pages of `get_ads_terms`. Preserve the returned reporting window, timezone, currency and install basis. Use `get_ads_impression_share` or `get_ads_demand` only with their source and support status.

Distinguish campaign totals, keyword or Search Match delivery, and actual visible user query text. Hidden query spend is not an extra spending bucket to add to keyword totals. Reconcile reported spend and disclose coverage gaps. A null query text does not prove zero queries, and no connection or no import does not prove zero campaign spend.

Report supported metrics and their denominators. Rank popularity, paid installs and organic visibility are different evidence. Do not invent revenue, ROAS, LTV, purchases or user-level attribution from these reports. Do not recommend blanket country or bid cuts solely from aggregate CPI or incomplete query data.

Offer concrete, evidence-supported investigations or campaign proposals when requested. Stora cannot change bids, budgets, targeting, negatives or campaign state. `trigger_ads_sync` imports reports when an administrator authorizes it; a queued import is not fresh completed data. Credential setup belongs in Stora settings, never in chat.
