# Product intelligence

The same ACoS means opposite things on different products. Build a picture of the catalog before judging its ads, so that every recommendation fits the product's role, stock and listing health.

## Read the catalog

- `get_product_performance` and `get_asin_traffic`: ad sales and spend per ASIN, sessions, conversion (unit session percentage), buy-box share, and each ASIN's share of the account. Sponsored Brands has no ASIN-level report, so ad totals from `get_product_performance` exclude Sponsored Brands.
- `get_entity_tiers`: each product's tier (Super Hero, Hero, Challenger, New Launch), based on its contribution to the last 90 days of sales. Use the tier the tool returns; don't recompute it.
- `get_inventory`: sellable units, days of cover and stock-out risk per SKU.
- `get_product_health`: advertised products that are out of stock, suppressed, unbuyable or without the buy box while their ads keep spending.
- `get_product_taxonomy`: department, category and sub-category, for grouping products and comparing like with like (`get_taxonomy_benchmarks`).
- Product titles, where the results carry them, are enough to say in one line what each product is. If a title is missing, write "title not available" rather than guessing.

## Turn rows into understanding

Answer four questions for each meaningful ASIN:

1. **What is it?** One line from the title: category, form, key attribute. This is what makes fit judgments possible. You can only say whether a search term fits a product if you know the product.
2. **What is its job?** Tier and share: a flagship to defend, a winner to scale, a challenger to grow, or a new launch to seed.
3. **Can it take more traffic?** Stock and health. A top product with a week of cover should not be scaled into a stock-out; protect its rank instead. A product with weak conversion or no buy box can't convert new traffic, so fix the listing before adding spend.
4. **What margin can it afford?** If the user has entered product costs, `get_profit_loss` gives profit per ASIN, and a thin-margin product tolerates less ACoS. Without costs, use the target ACoS as the ceiling and say so. When quoting profit figures, read the result's `bottom_line` and `profit_state`: without product costs, the figure is a contribution before product cost, not profit.

## The Product Map

A compact table that the rest of the audit refers back to. Illustrative rows:

| ASIN | What it is | Tier | Ad sales | ACoS / TACoS | Stock (days) | Health | Posture |
|---|---|---|---|---|---|---|---|
| B0… | 20 oz insulated steel bottle | Super Hero | … | … | 41 | OK | **defend** |
| B0… | replacement straw lids | Hero | … | … | 8 | OK | **hold** (low stock) |
| B0… | new travel mug | New Launch | … | … | 60 | few reviews | **seed** |

Postures: `scale` · `defend` · `hold` · `fix-listing` · `wind-down` · `seed` (new launches).

Every later recommendation must agree with the product's posture. Never recommend scaling a product marked `hold`, `fix-listing` or `wind-down`. When big waste sits on such a product, say that the stock or the listing is the real fix.

## Parent and child ASINs

Ads run on the child product (the SKU), while shoppers and categories think in parents. Roll children up to the parent to judge size and role, but keep keyword and bid recommendations on the child that carries the ad. For profit by variation family, `get_profit_loss` can group results by parent ASIN.
