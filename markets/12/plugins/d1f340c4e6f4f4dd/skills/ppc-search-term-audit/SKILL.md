---
name: ppc-search-term-audit
description: Audit Amazon PPC search terms in Sotrics to find wasted spend, negative keyword candidates and terms worth scaling.
---

Use this when the user asks about wasted ad spend, ACOS, search terms, negatives or PPC performance.

1. Call `get_ppc_overview` for the period (default: last 30 days) for spend, ad sales, ACOS and TACOS.
2. Call `get_search_terms` for the same period.
3. Report three short lists:
   - Wasted spend: terms with clicks and spend but no orders, highest spend first.
   - Negative keyword candidates: wasted terms with at least 10 clicks; check `get_negative_keywords` so you do not suggest terms that are already negatives.
   - Winners: terms with orders and an ACOS below the account average, which could get more budget or their own exact-match target.
4. Give totals (how much spend the wasted terms cost) and keep recommendations as suggestions; Sotrics is read only and cannot change campaigns.
5. If the tools say the Amazon Ads connection is pending or not connected, explain that PPC data is not available for this account yet instead of guessing.
