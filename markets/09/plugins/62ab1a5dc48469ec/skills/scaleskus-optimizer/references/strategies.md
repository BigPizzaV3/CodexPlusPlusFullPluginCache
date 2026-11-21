# The four strategies

Each strategy is a lens. Run all four, then synthesize. Every finding names the ASIN it affects and the search term, keyword or target that drives it. The thresholds below are working defaults: tune them to the user's target ACoS and objective, and say when you do.

Each strategy has a ScaleSKUs workflow (`run_workflow`) that returns a numbered, approvable plan with the numbers already checked, plus reads that supply the product-level evidence. Keep each plan's `plan_ref` and item numbers, because applying uses them later. Workflows scan weeks of data and can take 10–40 seconds each.

## Statistical floors (apply everywhere)

- **Bids:** at least ~10 clicks or 1 order in the window, and at least 7 days of data. Never move a bid on a handful of clicks.
- **Negatives:** spend of at least ~2× the target cost per order with zero orders, over at least 30 days (14 when volume is very high). Don't judge a term on the last ~2 days: late attribution regularly turns a "zero-sales" term into a seller.
- **Budgets:** at least 14 days. Act on sustained capping, not one capped day.
- **Reversibility:** when the impact is similar, prefer reversible levers (bid, budget, placement) over harder ones (negate, pause).

Anything below its floor goes on the watchlist ("not enough data yet"), not in the action list.

## A. Wasted spend

The fastest return is money already being spent that brings nothing back. Find it, stop it, redeploy it.

- **Plan:** `run_workflow` with `workflow="cut_waste"`. If the account runs Sponsored Brands, run it again with `ad_product="SB"`. Each negate item carries fit evidence (what the campaign sells, the price signal); judge it before recommending the item.
- **Evidence:** `get_waste_search_terms`, `get_negative_opportunities`, and `get_search_term_analysis` (match type and the keyword the term triggered on, so a negative lands at the right level). Confirm a term isn't already blocked with `check_negation_status`.
- **Spend on broken products:** `get_product_health`, or `run_workflow` with `workflow="stock_leak"`, finds ads still running on products that are out of stock, suppressed or without the buy box.

Classify each wasteful row, grouped by ASIN:

| Pattern | Signal | Action |
|---|---|---|
| Doesn't fit the product | the shopper is searching for something this ASIN isn't | negative exact on the term where it spends; a negative phrase when one word carries the mismatch |
| Fits, but no orders yet | relevant term past the spend floor with 0 orders | bid cut or watchlist first; negate only when the fit is doubtful |
| Converts, but too expensive | orders > 0, ACoS far above target | bid cut, not a negative; consider giving the term its own exact keyword at a controlled bid |
| Converts in another campaign | the term sells elsewhere in the account | campaign-level negative only where it wastes; an account-wide negative would also block the campaign where it sells |
| Self-competition | the same term or target is live in several campaigns | consolidate to one owner (`get_duplicate_targeting`) |

Output: `ASIN · search term · match · campaign · spend · orders · ACoS · action · spend saved per month`. The recoverable total is the budget that funds B and C.

Don't over-prune discovery. On a scale objective, negate only the clearest waste and leave marginal terms feeding auto and broad campaigns.

## B. Under-funded winners

The mirror image of waste: proven winners throttled by budget or bid. Every unit of budget held back here is sales left on the table.

- **Plans:** `run_workflow` with `workflow="uncap_budgets"` (raises for capped campaigns that are efficient and in stock) and `workflow="fix_bids"` (bid moves computed from the target ACoS, with the maths behind each).
- **Evidence:** `get_entity_tiers` (the winning products and targets), `get_budget_constrained_campaigns` (Amazon's missed-sales estimate), `get_budget_analysis` (the account's own utilization and days capped), `get_realtime_budget_usage` (capped right now), and `get_keyword_efficiency` / `get_target_efficiency` (current versus suggested bid). The three budget sources read different data and can legitimately disagree, so name the source of each number.

The scaling ladder, per winning ASIN and keyword:

1. **Un-cap the budget first.** A strong keyword in a campaign that runs out of budget stops showing after the cap. Raise the campaign budget, or move budget from over-target, under-used campaigns, before touching bids.
2. **Then bid into headroom.** Raise bids on keywords well under target ACoS toward the suggested bid, sized to the evidence rather than a flat percentage.
3. **Then placement.** If top of search converts clearly better than other placements (`get_placement_performance`, or `workflow="placements"`), raise that placement's adjustment instead of every bid.
4. **Then extend the winner.** A top product's best keywords should exist as exact keywords wherever they belong; the gaps become harvest candidates for strategy C.

Output: `ASIN · keyword or campaign · current → proposed bid or budget · ACoS · headroom evidence · estimated additional sales per month at current efficiency`. Never scale a product the Product Map marked `hold`, `fix-listing` or `wind-down`.

## C. Category search terms not advertised

Often the biggest hidden lever: high-demand searches the product already wins organically, or that define its category, with no active keyword behind them.

- **Plan:** `run_workflow` with `workflow="harvest_winners"`: converting search terms not yet targeted, each placed as an exact keyword (or an ASIN as a product target) in a manual ad group that advertises the matching product, with a starting bid. Items carry fit evidence (product match, price fit); judge it before recommending the item.
- **Evidence:** `get_sqp_share_of_voice` and `get_sqp_performance` (Search Query Performance: impression, click and purchase share per query, organic and paid together), `get_search_catalog_performance` (each ASIN's organic search funnel), `get_harvest_opportunities`, `get_keyword_competition` (demand, share, top rivals and suggested bid per keyword) and `get_asin_competitors`. `workflow="market_share"` summarizes search share against competitors.

Find the gap for each ASIN:

1. Take the category's top search queries by volume and by the ASIN's organic purchase share.
2. Remove the queries the ASIN already has an active, funded keyword for (`get_campaign_structure`, `find_entity`, `get_keyword_efficiency`).
3. What remains is category demand the account leaves uncaptured. Rank it by volume × the ASIN's organic conversion on the query. Queries the product already wins organically are the safest, highest-intent additions.

Action ladder: harvest converting auto and broad terms as exact keywords at a controlled bid; add new exact keywords for high-volume category queries the ASIN ranks for, starting conservatively; and map each query to the single ASIN that should own it, so the account's products don't bid against each other.

Output: `ASIN · query · search volume · ASIN organic share or conversion · why it fits · proposed match and bid · reachable demand`.

Search Query Performance and the other search-share data come from Amazon Brand Analytics, which not every account has. If those tools return nothing for the account, say so and base strategy C on the harvest data alone.

## D. Efficiency, structure and pacing

The connective work that makes A–C hold.

- **Bid right-sizing:** keywords near target ACoS (roughly 0.7× to 1.3×) move gently toward the suggested bid. Don't churn bids that already work.
- **Placement:** `get_placement_performance`: set top-of-search, rest-of-search and product-page adjustments where conversion actually is.
- **Duplicates:** `get_duplicate_targeting`: one owner per keyword or target.
- **Structure:** `get_campaign_structure`: too few keywords, missing negatives, several unrelated products in one campaign.
- **Budget balance:** `get_budget_analysis`: move budget from over-target, under-used campaigns to capped winners, keeping a floor for each campaign.
- **Weakest area:** `get_audit_scores`: the lowest sub-score says which of A–D to weight this cycle. `get_growth_audit_findings` adds money-ranked fixes.

## Objective tuning

- **Defend efficiency:** weight A and bid cuts; scale only the cleanest winners; skip most of C.
- **Scale revenue:** weight B and C; negate only the clearest waste; raise bids into headroom; harvest aggressively.
- **Recover from a drop:** start with `run_workflow` with `workflow="sales_drop"`, `get_sales_dips` and `get_optimization_history`. The usual cause is a recent change, a stock-out or unsettled data, not the need for a new plan. Don't pile on changes.
- **Full audit (the default):** run all four, report everything, and let the owner choose.
