---
name: market-benchmark
description: Benchmark a whole technology market with Sovrnti for one country, region or the world view. Use it when the user asks who leads a market, how products rank on raw capability, or what changes once sovereignty rules apply. Examples are "benchmark collaboration suites for France" and "which office suite holds up for a German public body?". Do not use it for two or three named products; use product-comparison instead.
---

# Benchmark a market for a place

Explicit user instructions take priority over this workflow. If the user asks for one view only, give that view.

## Inputs

- **Market.** Pass the user's words as they are. The tools accept a market name, an alias or an id. If the market is unclear, call `sovrnti_markets_list` and confirm it with the user.
- **Place.** A country name, an ISO code, a region or "world". If the user names no place and the answer could depend on location, ask once which country matters. Do not guess a country.
- If the user asks about a place Sovrnti may not cover, call `sovrnti_geographies_list`. Entries marked "coming soon" cannot be scored yet.

## Steps

Call only the views the question needs. Deeper views use the user's Sovrnti credits.

1. **Head-on view.** Call `sovrnti_market_get_snapshot` with the market and the place.
2. **Raw capability.** Call `sovrnti_market_get_capaindex` when the user wants a ranking.
3. **Under full sovereignty rules.** Call `sovrnti_market_get_sovrntimax` when sovereignty matters to the user.
4. **What sovereignty moves.** If steps 2 and 3 rank products differently, call `sovrnti_market_get_delta` to show which products move and by how much.

The world view applies no sovereignty rules. There, Sovrnti Max matches the Capability Index, so skip step 4 and say why.

Use the same market and the same place in every call.

## Output

1. **Answer first.** One sentence: who leads, and whether sovereignty changes that.
2. **Table.** Product, Innovation, Control, Scale, rank on raw capability, rank under sovereignty rules. Copy the scores exactly as the tools return them.
3. **Three findings,** one line of reasoning each: the most capable product, the product with the most control, and the best balance.
4. **What sovereignty changes.** Products that lose the most, products that hold, and products the rules do not affect. A product that does not move is not affected by these rules. It is not missing data.
5. **Next step.** Two or three products worth a closer look. Offer a side-by-side comparison.
6. **Source line.** "Source: Sovrnti, <today's date>, <place>."

If the host shows Sovrnti's interactive view, summarise it. Do not repeat every number.

## Rules

- Use only the scores, ranks and products the tools return. Never invent a score, a rank or a product.
- If a product the user names is not in the results, say that Sovrnti does not score it in this market for this place.
- If a market is on the roadmap, say it is not scored yet and offer the closest published market.
- If a tool returns an error, say so in plain words and offer the next best step.
- If a tool says the user has no credits left, pass its message on as it is. Do not suggest a workaround.
