---
version: 1
---

# Price analysis: Patina evidence fields

Your evidence is one `get_market_snapshot` result. The `comps` section holds the comp pools, the `context` section holds the market context, and the `estimate` section holds the display estimate. A section that failed alone is `null` with an entry in `warnings`: say that part of the read is unavailable and work with the rest.

**Sold comps.** The sold pool is `comps.sold_comps`. Each row has `price`, `sold_at`, `source`, `title` and `url`.

**Active asks.** The private-ask pool is the rows of `comps.active_asks` with `source_type: "marketplace"`.

**Dealer asks.** The dealer-ask pool is the rows of `comps.active_asks` with `source_type: "dealer"`. Read them as the top of the retail band, never as comps.

**Best-offer ceilings.** A row flagged as a best-offer ceiling is a sold comp with `best_offer_accepted: true`. Its `price` is the seller's ask: eBay hid the accepted amount, and Patina shows the ask unchanged. The buyer paid at or below it. `false` or `null` means a realized price. `sale_type` does not carry this; read `best_offer_accepted` only.

**Auction results.** A row flagged as an auction result is a sold comp with `auction_house` set, or whose `source` is `bonhams`, `antiquorum`, `watches_of_knightsbridge`, `fellows`, `jones_and_horan` or `invaluable`; `auction_house` can be empty on an `invaluable` row. Its `price` is the winning bidder's all-in figure: hammer plus the house's buyer's premium. Jones & Horan charges no premium, so its price is the hammer and also the all-in. `lot_number` names the lot. `sale_type: "auction"` on an eBay row means an eBay auction-format sale: a realized eBay price with no premium, not an auction result.

**Market of sale.** `source_currency` on a sold comp is its market of sale. `"USD"` also covers rows whose origin was never recorded, so it is not proof of a US sale. Active asks carry no market of sale: treat their geography as unknown.

**Currency.** Every `price` is an object with `value` and `currency`, converted into the currency of the request (the user's Patina display currency unless one was passed). You never convert. Say the currency when it is not the user's display currency.

**Provenance and condition.** Sold comps and both kinds of active ask carry `has_box` and `has_papers`. Only sold comps carry `condition_grade`. `null` means unknown, not no.

**Evidence depth.** The depth read is `context.sample_size.band`: `thin`, `moderate` or `deep`. On `thin`, say so plainly.

**Pool counts.** `coverage.returned_sold_comps` and `coverage.returned_active_asks` are pool sizes. Never state them.

**Trend and liquidity.** The trend copy is `context.trend.description` and the liquidity copy is `context.liquidity.description`. Pass them through as written; never sharpen them. A `null` trend means no trend to report.

**Display estimate.** The display estimate is the `estimate` section of the same snapshot: `market_value` as `{ amount, low, high, currency }`, an optional `list_for` band, `confidence`, `basis` and named `adjustments`. It comes in the same call as the comps: one call, one charge.
