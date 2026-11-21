---
name: budget-allocation
description: Recommend how to split budget across ad platforms and campaigns with Toffu. Use when the user asks where to put more budget, what to cut, or how to rebalance spend between channels. Compares return per platform and campaign and proposes budget changes the user confirms.
---

Use the Toffu tools. Never apply a change the user has not confirmed.

1. Call `get_account_context`. If a platform has several accounts, ask which one. Pass the ids as `account_ids` to `query_campaign_performance`, and as `account_id` to the other tools.
2. Read data with `query_campaign_performance` (daily rows: `time_increment` "1"), `list_campaigns`, `list_ad_sets` and `list_ads`.
3. To change something, call `propose_update_campaign`, `propose_update_ad_set` or `propose_update_ad`, and show the preview. Call `apply_change` only after the user confirms that change.

# Cross-Channel Budget Allocation

## Portfolio Budget Approach
- Treat total paid media budget as a single portfolio, not siloed channel budgets.
- Allocate based on marginal ROAS: shift dollars from channels with declining returns to channels with headroom.
- Rebalance monthly at minimum, weekly during peak periods or launches.

## Diminishing Returns Curves
- Every channel hits diminishing returns. Plot spend vs conversions to identify the inflection point.
- Below the inflection: scale aggressively. Above it: diminishing returns set in.
- Channels with steep curves (branded search) reach saturation faster than broad channels (Meta prospecting).

## Incrementality Testing
- ROAS alone is misleading — it conflates correlation with causation.
- Run **geo-holdout tests**: pause a channel in select markets, measure conversion lift in active vs holdout.
- Run **conversion lift studies** (available in Meta, Google) to measure incremental impact.
- Reallocate budget away from channels with low incrementality, regardless of last-click ROAS.

## Channel-Level ROAS Targets
- Set targets by channel AND funnel stage. Prospecting has lower ROAS than retargeting — that's expected.
- Branded search: 5-10x+ ROAS target.
- Non-branded search: 2-4x ROAS target.
- Meta prospecting: 1.5-3x ROAS target.
- Retargeting (all channels): 4-8x ROAS target.
- Adjust targets based on customer LTV, not just first-purchase value.

## Seasonal Budget Shifts
- Build a **seasonal budget calendar** based on historical conversion data.
- Increase budgets 2-4 weeks before peak periods (Q4, industry events) to warm algorithms.
- Reduce budgets gradually post-peak — sudden drops destabilize bidding algorithms.

## New vs Proven Channel Allocation (70/20/10)
- **70%**: proven, scaled channels with predictable returns.
- **20%**: growing channels with promising early data. Invest to validate scale.
- **10%**: experimental channels or tactics. Accept that some will fail — that's the point.
- Promote from 10% -> 20% -> 70% as data confirms viability. Cut what doesn't graduate.
