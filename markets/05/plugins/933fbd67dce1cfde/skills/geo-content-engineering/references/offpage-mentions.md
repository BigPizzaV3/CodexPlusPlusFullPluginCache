# Mentions, sentiment, and consistency

External mentions on trusted platforms as a grounding source for generative
answers. Your own page is not enough; systems check claims against external
sources.

## The mechanic

LLM systems base answers on sources they already treat as reliable. Without a
strong external presence a model may leave a brand out of the answer even when
the on-page content is flawless. External mentions feed the same grounding logic
as on-page citation-worthiness (see `citation-worthiness.md`).

## Requirements

1. **Mentions on trust platforms.** Build mentions on news sites, industry media,
   and established forums (such as Reddit). They create indirect citations: the
   model cites the external source, which points to the brand.

2. **Steer sentiment.** The context of a mention matters. Build systematic review
   activity on relevant rating platforms, because AI systems actively read
   reviews for recommendations.

3. **Data consistency.** Product names, prices, feature scope, and company data
   must be identical across all external surfaces (directories, Wikidata, app
   stores, social profiles). Contradictory data lowers model trust in every
   source tied to the brand.

4. **Presence in listicles.** Transactional prompts ("best tool for X") are often
   answered from external rankings and top lists. The brand has to appear in the
   relevant external comparisons.
