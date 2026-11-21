---
name: google-ai-overview-research
description: Retrieve the Google AI Overview box for a query, check whether it appeared, or inspect its cited sources with HasData. Use full SERP then a returned token if needed, not Google AI Mode.
---

# Read the AI Overview on a Google results page

Read `../hasdata-research/SKILL.md` and `../hasdata-research/references/tool-contract.md`.

Reuse a fresh full-SERP response for the exact same query and search context when available. Otherwise call `hasdata_google_serp_serp_getSearchResults` with q and relevant supplied localization. Light and AI Mode are not substitutes for the full-SERP Overview lookup.

Inspect aiOverview. If the inline answer and citations already satisfy the request, return them without another paid call. If expansion is needed, immediately pass its exact pageToken to `hasdata_google_serp_ai_overview_getAiOverviewResponse`. The continuation accepts pageToken, not q. A fresh lookup plus expansion needs at most two requests; respect a smaller explicit limit.

A successful SERP with no Overview is source-specific absence, not an API failure. An incomplete block without a token cannot be expanded. The advertised token lifetime is about one minute. Never fabricate a token or automatically pay for a new SERP after expiry. Explain the unavailable branch; do not substitute AI Mode or another provider.

Return actual Overview text or the requested summary with original source links and explicit citation indexes. Missing source entries stay missing. Do not ask for a target brand unless the user requested a brand check; use `../ai-search-visibility/SKILL.md` for that analysis.
