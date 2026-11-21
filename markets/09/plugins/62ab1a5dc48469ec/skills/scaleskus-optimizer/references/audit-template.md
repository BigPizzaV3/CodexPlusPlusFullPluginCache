# The audit write-up

Owner-readable, money first, grounded in products. Use the account's own currency throughout, give every number its window, and keep jargon in the tables. Render the audit as Markdown in the conversation, and produce a shareable document only if the user asks for one.

Use this skeleton:

```
# Amazon Ads optimization audit: <account> (<ad products>), <date window>

## Executive summary
- Account health: <one line: spend, ad sales, ACoS vs target, TACoS, trend>
- Recoverable waste: <amount per month> across <N> search terms and targets (A)
- Sales held back: <amount per month> from <N> under-funded winners (B)
- Uncaptured category demand: <N> leading search queries, about <searches per month> reachable (C)
- Top 3 moves this week: <one line each: ASIN + keyword + expected effect>

## Product map
<ASIN · what it is · tier · ad sales · ACoS/TACoS · stock · health · posture>

## A. Wasted spend (recoverable: <amount per month>)
<table: ASIN · search term · match · campaign · spend · orders · ACoS · action · saved per month>
<one or two sentences: where the waste concentrates and the single biggest fix>

## B. Under-funded winners (additional: <amount per month> at current efficiency)
<table: ASIN · keyword or campaign · current → proposed · ACoS · headroom evidence · estimated additional sales per month>
<which winners are held back by budget, by bid, or by coverage>

## C. Category search terms not advertised (about <searches per month> reachable)
<table: ASIN · query · search volume · organic share or conversion · proposed match and bid · reachable demand>
<where the account under-owns its own category demand>

## D. Efficiency, structure and pacing
<bullets: bid right-sizing, placements, duplicates, budget balance, weakest audit area; each with its ASIN or keyword and the number>

## Action list
| # | Move | ASIN | Keyword / target / campaign | Current → proposed | Est. impact per month | Confidence | Reversible |
|---|------|------|----------------------------|--------------------|-----------------------|------------|------------|
| 1 | negate | B0… | "<term>" | live → negative exact | <amount> saved | high | harder |
| 2 | raise budget | B0… | <campaign> | <A> → <B> | <amount> more sales | medium | yes |
| 3 | harvest | B0… | "<term>" | none → exact at <bid> | <amount> more sales | medium | yes |
<sorted by impact × confidence; note each item's workflow and plan item number>

## Watchlist: not enough data yet
<items below the statistical floors, and what would make each one actionable>

## Assumptions and data notes
<target ACoS and where it came from; windows; data freshness; tools that were not available; provisional days; stock and health gates applied>

## Next step
<for example: "Reply 'queue 1-5' to add them to ScaleSKUs Tasks for approval, or 'queue the negatives only'." Then when to review again.>
```

## Rules for the write-up

- Every row names an ASIN and a search term, keyword, target or campaign. No account-level hand-waving.
- Every number carries its window and respects the statistical floors. Anything below them goes to the watchlist.
- Stay consistent with the Product Map: never propose scaling a product marked `hold`, `fix-listing` or `wind-down`.
- Money leads; tactics follow. Keep savings (waste cut) and growth (additional sales) as separate figures; never add them into one total.
- "Estimated impact" is a projection at current efficiency. Label it as an estimate, never as a promise.
- Profit, margin and fee figures are estimates (Amazon's fee estimates can differ from settlement). Say whether product costs were included, and state that the figures are not financial or tax advice.
