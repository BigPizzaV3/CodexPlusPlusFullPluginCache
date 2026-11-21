---
name: keyword-research
description: Use when the user wants to research keywords, find content ideas, analyze a competitor or decide which keywords to track for a brand.
---

Research keywords with real data and turn them into a plan. Each research call uses the brand's monthly plan quota: be efficient. Reply in the user's language.

1. Call `list_brands` and confirm the brand. Call `get_brand` for its sector and saved competitors.
2. Depending on the question:
   - **Ideas from a topic:** `keywords_search` with `seed_keyword` (optional filters for volume, competition and intent) or `keywords_suggestions`.
   - **Validating a list:** `keywords_search_volume` and `keywords_difficulty` with the list of `keywords`.
   - **Competitors:** `keywords_analyze_competitor` with the competitor's `domain` (shared keywords and gaps) or `keywords_for_site` to see what a domain ranks for.
   - **What already works:** `keywords_gsc_opportunities` (the brand's own Search Console data, no quota used).
3. Group the results by intent and topic. Prioritize by volume, difficulty and business relevance.
4. Propose the plan: which pages to create or improve for each keyword group.
5. If the user wants to track them, confirm the list and call `keywords_tracked_add` (it respects the plan limit). `keywords_generate_clusters` groups the already tracked keywords with AI.

Rules:
- Avoid repeating identical searches: every research call counts against the quota.
- Do not add keywords to tracking without confirmation.
- State the market (country and language) of the data; if it is not the brand's market, ask.
