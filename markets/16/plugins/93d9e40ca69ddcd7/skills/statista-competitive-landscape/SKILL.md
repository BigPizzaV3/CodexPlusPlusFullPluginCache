---
name: statista-competitive-landscape
description: Analyses competitors from Statista data covering market share, concentration, share momentum and brand standing. Use for competitor analysis, market share, brand health comparisons, positioning and single-competitor profiles.
---

# Statista Competitive Landscape

## Data

- Figures only from fetch calls (`fetch-market-insights`, `fetch-consumer-insights`, `get-chart-data-by-id`). Search returns IDs, not values. Statista only: no web, no model knowledge.
- IDs and geography codes exactly as returned. Reuse figures already fetched in this conversation.
- Cite bucket and year per figure. Label calculated figures with their inputs.

## Method

1. Fix the peer set before retrieving: category, geography, segment, period. No players added after seeing the data.
2. Share of market from one consistent share series. CR3/CR5 from that series, "other" kept.
3. Share of mind from one named brand metric: awareness, consideration, usage, loyalty.
4. Index both to the peer-set mean = 100. High share + low mind = vulnerable incumbent. Low share + high mind = emerging challenger.
5. Read movement where ≥2 periods exist. Rising consideration with flat share signals a challenger. One share vintage only: report structure, not momentum; list multi-period share as an open item.

## Inputs

| Input | Bucket |
|---|---|
| Market share, revenue by company, category revenue | Market Insights |
| Single-company revenue, number of players | Statistics |
| Awareness, consideration, usage, loyalty | Consumer Insights |

No share data: a brand landscape, not a ranking. No brand data: share and structure only.

## Single competitor

Share and movement, revenue trend, brand funnel vs peer mean, segments where it over- or under-indexes. Strategy, products and partnerships are not in Statista: list as open items.

## Exhibits

Show who leads and how concentrated the market is, how share compares with brand standing, and how positions moved. Chart only when the reader needs a shape.

## Output

1. Headline: who holds power, how it is moving
2. Share and concentration
3. Share vs brand standing
4. Who is exposed, who is emerging
5. Implication for entry, defence or positioning

## Gotchas

- Shares from different market definitions cannot be ranked together.
- Awareness is not demand or loyalty.
