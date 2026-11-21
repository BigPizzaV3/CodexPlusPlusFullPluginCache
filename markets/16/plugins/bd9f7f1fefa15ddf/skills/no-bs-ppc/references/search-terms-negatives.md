# Search terms and negatives

## Judging a search term

A search term is never relevant or irrelevant on its own. Judge it in three dimensions:

1. **The keyword that matched it**: match type and intent.
2. **The ad group**: its theme and the ads shown.
3. **The campaign**: brand or non-brand, product line, geo, bidding goal.

The same term can be right in one ad group and wrong in another. Before adding a negative, decide where the traffic should go, not only where it should stop.

## Classify before negating

| Type | Example | Action |
|---|---|---|
| Wrong intent | "video editor jobs" for a video editing tool | Negative, phrase, at the widest level where it is always wrong |
| Wrong product or audience | job seekers on the employer side | Negative in the campaigns of the wrong side only |
| Competitor name | "[competitor] pricing" | Routing decision: own competitor campaign or not. Not a blanket negative |
| Geo modifier | "jobs madrid" | Usually fine. A geo with zero conversions is a reporting fact, not a negative, unless the business does not serve it |
| Brand misspelling or navigational | "[brand] login" | Route to brand. Negate in non-brand if brand has its own campaign |
| Free / cheap | "free", "gratis" | Depends on the offer. Mixed intent: segment before negating |

## Levels and scope

- Negatives live in a scope: ad group, campaign, a shared list linked to specific campaigns, or the account-level list.
- A shared list only blocks the campaigns it is linked to. Check the links; the list name does not tell you.
- Put a negative at the narrowest level where it is always wrong. Too wide a negative blocks good traffic in another product or campaign.
- When negating to route traffic to another campaign, make sure the destination has a keyword that can match it. Otherwise the traffic dies between the two.
- Multi-product accounts need negatives separated by product.

## Match types for negatives

- Negative keywords block misspellings (since June 2024) but not close variants, synonyms or singular and plural forms. Add those separately. An exact negative blocks only that query and its misspellings.
- A phrase or broad negative on a short n-gram blocks every query containing it. Check that no converting query contains it.
- Severity: a phrase or broad negative that contains a positive keyword's text stops that keyword completely; an exact negative only removes one query.

## N-gram analysis

- One negative on a bad n-gram beats hundreds of exact negatives. Group search terms into 1, 2 and 3 word n-grams and sum cost and conversions.
- Run it on Search and Performance Max search terms.
- A zero-conversion n-gram is a candidate only when its cost is large enough to have expected a conversion (at least one target CPA, with enough clicks).
- Before adding, check it against converting n-grams: negating "editor" kills "video editor online".
- The `search-terms-cleanup` skill does this from a search terms report export.

## Broad match

- Broad match with Smart Bidding is the standard way to scale non-brand search, with guardrails: reliable conversion tracking, dense negatives in place, and weekly search term reviews.
- Keep exact or phrase on expensive, high-intent core terms where exploration is not wanted.
- Consolidate thin themes: ad groups with a few hundred impressions a week give Smart Bidding no signal. Themed ad groups of 3 to 20 keywords beat single-keyword ad groups.

## Before deleting negatives in bulk

Export the full list first (text, match type, level, list) so it can be restored.
