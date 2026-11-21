# Diagnosing a performance change

## The chain

```
eligible impressions (demand) x impression share = impressions
impressions x CTR = clicks
clicks x CVR = conversions
cost / conversions = CPA = CPC / CVR
```

Each identity must close. If it does not, the data pull is wrong.

Walk the chain from the top and find the link that moved:

- **CPA up, CVR flat**: it is CPC, the auction price. Not the landing page or the funnel. Look at position, competitors, targets, budget.
- **CPA up, CPC flat**: it is CVR. Look at traffic quality (search terms, geo, device, audience), the landing page, the offer, and tracking.
- **Conversions down, CVR flat**: it is volume. Split it into demand (eligible impressions), share (impression share) and CTR.

## Demand versus share

Eligible impressions = impressions / search impression share, summed by campaign. Impression share itself is not additive; never average it.

| Impression share | Eligible impressions | Reading |
|---|---|---|
| Up | Down | The market shrank. You hold more of a smaller pie. Volume loss is demand, not management |
| Down | Up | The market grew and you lost share: budget, rank or competition |
| Up | Up | Healthy: growing with the market |
| Down | Down | Losing on both |

Caveat: eligible impressions also fall when the account narrows its own reach (paused keywords, tighter match types, removed geos). Check change history before calling it demand.

## Lost impression share

- **Lost to budget** high: the campaign is capped. More budget recovers volume at a similar CPA, until rank becomes the limit.
- **Lost to rank** high: bids, targets or quality. More budget does not help. Raising targets or bids buys position at a higher CPC.
- Lost to budget near zero: the campaign is not budget-constrained. Adding budget changes nothing.

## Position: top and absolute top share

When CPC rises or CTR falls, check top impression share and absolute top impression share week over week, weighted by impressions.

- Falling top share explains lower CTR (lower positions get fewer clicks) and higher CPC (getting back up costs more).
- Top share lost to rank: competitors bid more, or our targets or quality dropped.
- If position loss is rank-driven and CPA is already high (expensive season), buying position back worsens CPA. Waiting is often the better call.

## Conversion maturity

- Conversions arrive late: lead to sale, trial to subscription, offline imports, conversion value updated after the click. The latest days always look worse.
- Traffic metrics (impressions, CTR, CPC, impression share) do not mature: week over week is reliable.
- Compare conversions at the same age: the last 7 days against the same 7 days a year or a month earlier, measured the same number of days after they ended.

## Mix

- An account CPA can rise with every campaign's CPA flat, because spend shifted toward higher-CPA campaigns. Split the account change into "within campaigns" and "mix shift" before calling it a performance problem.
- App campaigns, view-through and secondary conversions are different units. Do not add them to web leads in one CPA.

## What to ask for

To diagnose, ask for a campaign report with a Day (or Week) segment and these columns: Campaign, Campaign type, Impr., Clicks, Cost, Conversions, Conv. value, Search impr. share, Search lost IS (rank), Search lost IS (budget). Plus the change history for the period. The `performance-triage` skill reads that export directly.
