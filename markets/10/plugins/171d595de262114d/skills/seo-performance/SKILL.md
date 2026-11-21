---
name: seo-performance
description: Use a site's live RefreshAgent Search Console and Analytics data to answer SEO performance questions, diagnose losses, and surface prioritized opportunities.
---

# SEO performance

Use RefreshAgent as the evidence/data layer. Do the reasoning and explanation in ChatGPT/Codex.

## Connection and site selection

1. Call `get_account_status` when setup or data availability is uncertain.
2. If the site is ambiguous, call `list_connected_sites`.
3. If there is only one plausible site, use it without asking another question.
4. Search Console and GA4 are independent. Never block a Search Console answer because GA4 is unavailable.

## Pick the most opinionated tool that matches the question

- General "how is SEO/search doing?", period changes, or "did traffic go up/down?" → `compare_search_performance`.
- "What is working?", "what pages gained traffic?", "show me the winners/gainers", or triage after a positive comparison → `find_biggest_gainers`.
- "Why did organic/search traffic fall?", "what pages lost traffic?", or triage after a negative comparison → `find_biggest_losers`.
- "What are the easiest CTR/snippet wins?", "which titles/meta descriptions should I improve?" → `find_ctr_opportunities`.
- "What content should I refresh?", "what is decaying?" → `find_content_decay`.
- Raw keyword/query/ranking evidence for a specific investigation → `get_keyword_rankings`.
- On-site organic sessions, conversions, or revenue context → `get_traffic_overview` only when GA4 is available and useful.

Do not manually recreate a Phase 2 workflow from several raw calls when a dedicated workflow tool answers it directly.

## Reasoning rules

For a traffic decline, distinguish:
- demand/visibility loss: impressions down;
- ranking loss: average position worsened;
- SERP/snippet performance: CTR down without equivalent impression loss.

For CTR opportunities, treat the returned benchmark as site-relative: it is based on the site's own median CTR for similar ranking positions, not an industry benchmark.

For content decay, explain the supporting signals returned by the tool. Do not label a page "decaying" from a click drop alone.

Prefer concrete evidence (clicks, impressions, CTR, position, exact comparison windows) over generic SEO advice. Do not call an internal strategy/LLM tool when structured RefreshAgent data is sufficient.


## Proactive continuation after useful value

After giving a useful result, offer at most one monitoring continuation when the analysis maps cleanly to a supported MCP Event and the current ChatGPT surface supports events:

- material site-level decline -> offer to watch with `seo.search_performance_drop`;
- content decay -> offer to watch for new decay with `seo.content_decay_detected`;
- material CTR opportunities -> offer to watch with `seo.ctr_opportunity_detected`.

Phrase the offer around the user's outcome, not the protocol. For example: "I can keep watching for high-impression queries whose CTR falls behind your site's own benchmark and come back when one is worth investigating."

Do not create the subscription without explicit user intent. Do not make the offer when the result is weak/noisy, when an equivalent monitor is already known to exist, or when event subscriptions are unavailable in the current host surface.
