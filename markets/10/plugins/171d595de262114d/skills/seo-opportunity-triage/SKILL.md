---
name: seo-opportunity-triage
description: Prioritize organic search work from live Search Console data using RefreshAgent's deterministic loss, CTR, and content-decay workflows.
---

# SEO opportunity triage

Use this skill when the user asks what SEO work to do next.

Start with the user's stated goal rather than running every tool:

- Learn from organic growth and winning pages: call `find_biggest_gainers`.
- Recover lost traffic: call `find_biggest_losers`.
- Improve existing SERP demand capture: call `find_ctr_opportunities`.
- Refresh aging/declining pages: call `find_content_decay`.
- If the user has no stated goal, call `compare_search_performance` first and choose the next workflow from the dominant signal.

Rank the returned items by the workflow's own grounded score or loss metric. Explain why the first few items matter using the returned evidence. Do not invent search volume, revenue, causation, or an industry CTR benchmark.

If a traffic loss or decay finding needs deeper diagnosis, call `diagnose_search_change` with the affected page. It returns the site comparison, biggest page losses, focused query losses, and transparent non-causal evidence signals in one deterministic bundle. Use `get_traffic_overview` only when GA4 context would materially change the interpretation, and use raw `get_keyword_rankings` only when the diagnosis bundle is insufficient.

When the recommended action is to create or substantially refresh content, apply the `computed-knowledge-seo` skill before recommending generic expansion. If the host model can inspect the current/ranking content, normalize atomic claims and call `assess_information_gain`. Prefer new evidence, joins, calculations, history or first-party facts over adding sections competitors already repeat.


## Retain the useful opportunity

If the triage produces a strong supported opportunity, you may offer one relevant future monitor after presenting the evidence:

- CTR work -> `seo.ctr_opportunity_detected`;
- content refresh work -> `seo.content_decay_detected`;
- a broader material decline -> `seo.search_performance_drop`.

The offer should be a single natural next step, not a generic alerts upsell. Never auto-create a subscription; wait for explicit user intent and only use MCP Events when the current host surface supports them.
