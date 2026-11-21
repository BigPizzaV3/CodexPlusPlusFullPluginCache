# Keyword research and niche evidence

Start with product fit, not the largest volume. Return a sourced shortlist, then positioning and copy. Research does not authorize listing changes.

## Evidence types

| Source | What it supports | Limitation |
| --- | --- | --- |
| Seller query/traffic/order reports | How this shop was discovered or converted | Period and sample size matter |
| MakeBox/eRank/supplied dataset | Available demand, competition, opportunity and other defined metrics | Label source/date/region; database figures are not inherently live Etsy counts |
| Public Etsy sample | Seller language, visible offers, ordering returned at capture time | No proof of per-listing sales, causation or universal rank |
| Semantic hypothesis | Product-fitting phrases to test | Unmeasured; no invented percentages |

Without MCP use CSVs or pasted stats. Browse relevant public samples if available and authorized. Without metrics, still produce a useful relevance-based shortlist and label it unmeasured.

## Workflow

1. Extract exact item, confirmed traits/materials, use, customization and buyer language.
2. Build candidate intent groups; reject mismatches, IP ambiguity and impossible claims before scoring.
3. Gather exact-phrase metrics, retaining missing values. With 10,000 CSV terms, deduplicate/filter locally by product and attributes, then shortlist. Do not send ten thousand terms to a forty-term tool.
4. Choose coherent primary intent; compare relevance, specificity, evidence, demand/competition and coverage. Provider opportunity is a signal, never sale probability.
5. Assign phrases to title/prose/tags. A phrase over 20 characters can remain in prose; choose natural tag chunks, not mutilated abbreviations.
6. Explain rejected popular mismatches and validate the final tags after revision.

## Connected tools

- `search_keywords`: `query`, optional `limit` up to 100, `min_searches`, `max_competition`; inspect live schema for other options.
- `check_keywords`: `keywords` array up to 40 phrases. Found/missing are distinct; missing is not zero.
- `competitor_tags`: inspect current schema. Tag frequency in a retrieved sample is not demand.
- `search_top_listings`: inspect schema and record sample size. Shop lifetime sales are not per-listing sales; returned ordering is not a stable rank for every buyer.
- `analyze_competitor_listing`: inspect listing-ID/URL schema. Learn offer patterns and unanswered questions; write original copy.
- Public direct reads: `etsy_find_all_listings_active`, `etsy_get_listing`, `etsy_get_reviews_by_listing`; see [operation index](etsy-operation-index.md). Never request private competitor orders.

Do not invoke internal paid generation for an audit unless requested with its allowance. Research quotas may differ from direct reads.

## Output and niche decisions

Use [evidence table](../templates/keyword-evidence.md): phrase, fit, intent, available metrics, source/date, placement/reason. Preserve supplied trends/clicks/seasonality with their definitions; do not invent unavailable columns. Any self-created numeric fit score is an explicit editorial rubric, not measured Etsy relevance or chance of top placement.

Compare like-for-like material, quantity, customization and product type. Total delivered price requires known destination/shipping; unknown shipping remains unknown. Reviews may reveal unanswered questions, not permission to copy designs or buyer data. Finish with supported opportunities, production constraints and a small measurement plan, not a guaranteed profitable niche.
