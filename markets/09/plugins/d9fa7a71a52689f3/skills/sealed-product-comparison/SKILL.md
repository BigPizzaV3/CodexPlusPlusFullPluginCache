---
name: sealed-product-comparison
description: Compare exact trading-card boxes, displays or decks using fee-adjusted opened EV, break-even landed cost and dated marketplace low prices when the user is choosing between products.
---

Use `query_daily_ev` to resolve each exact product, followed by
`compare_sealed_products` for the arithmetic. Pricing research requires eligible
account linking; the comparison does not read Manafolio or execute purchases.
Explicit user choices take precedence over workflow defaults.

1. Resolve the requested game, set and physical SKU. Keep language, edition,
   box/display/deck and contents distinct. Obtain each record's `id` and its
   page using only game/set filters, since the comparison repeats those filters.
   If multiple identities remain plausible, ask which product they mean.
2. Establish one opened-singles basis, one sealed marketplace, and seller plus
   payment percentages. Use values the user supplied or already approved. If
   missing, ask a focused question; zero fees describe an explicitly gross
   scenario, never an inferred personal fee setting. For an offer the user
   supplies, use their per-unit landed cost including tax/shipping in the
   selected basis currency; clarify unknown costs instead of inventing them.
3. Pass one to six exact products to `compare_sealed_products`. Preserve the
   tool's marketplace low price, currency, observation dates, fee basis,
   model version, exclusions and coverage. The tool preserves existing model
   construction and does not reroll or backfill rejected cards.
4. Show product, observed low price or supplied landed cost, fee-adjusted opened
   EV, break-even landed cost, expected surplus and P/E. Describe the returned
   ranking as limited to these products with complete coverage. Leave partial,
   missing, stale or currency-mismatched products unranked. A partial EV figure
   is an incomplete estimate, not a full-product total.

Opened-card EV deducts only seller plus payment percentages. Do not subtract
fixed transaction fees or shipping from it; purchase tax/shipping belongs in the
separate landed cost. Break-even is model-based, not a guaranteed sale price or
profit. Marketplace observations and supplied offers do not verify inventory.

If the user also asks how quickly opened Magic cards might sell, use
`search_magic_sell_through`, then `magic_product_sell_through` for the selected
product key. Report coverage, dates and stock-sharing assumptions; modeled
recovery is not a seller guarantee or a forecast of price appreciation.
