---
name: computed-knowledge-seo
description: Use RefreshAgent as a data and deterministic-compute substrate to create novel, defensible SEO/AEO knowledge instead of generic LLM summaries. Use for programmatic SEO, research, information-gain analysis, data-led content and refresh decisions.
---

# Computed Knowledge SEO

RefreshAgent should provide evidence and deterministic computation. ChatGPT should do semantic reasoning with its own tokens.

Core rule:

> Compute, don't summarize. Create facts the model could not know without the connected data.

## When to use this skill

Use it when the user asks what to add to a page, how to refresh declining content, how to differentiate from ranking competitors, how to build programmatic SEO pages, or how to turn datasets into SEO/AEO content.

Do not invoke it for a simple performance lookup when the user only needs clicks, impressions, CTR, rankings, or a traffic explanation.

## Workflow

1. Start from a valuable user/search question.
2. Inventory independent datasets and identify the common entity/time/geography model.
3. Separate observed facts, deterministic derived facts, and bounded inferred claims.
4. Prefer joins, calculations, comparisons, trends, history, and first-party observations over generic prose.
5. Maintain provenance for factual claims.
6. Before proposing a scaled page family, state the new fact, comparison, trend, or decision each page exposes. If the answer is only “another row exists”, do not scale it.
7. When evaluating an existing or proposed page against competing coverage, use the `information-gain` skill and `assess_information_gain` operator.
8. Separate table-stakes competitor coverage from genuine differentiation.
9. Prefer novel derived facts, independent source joins, historical evidence, and first-party data.

## RefreshAgent execution rule

Do not ask RefreshAgent to run another LLM for an external-agent workflow. Use RefreshAgent tools for data and deterministic operators, then reason in ChatGPT.

For a content refresh discovered from Search Console, a strong default chain is:

`find_content_decay` or `find_biggest_losers` → page/query evidence → `collect_information_gain_evidence` → normalize atomic claims → `assess_information_gain` → recommend genuinely new computed knowledge.

Never recommend “add more content” merely because a page is thin. Identify the new fact, comparison, calculation, historical observation, first-party evidence, or cross-dataset insight the update will add.
