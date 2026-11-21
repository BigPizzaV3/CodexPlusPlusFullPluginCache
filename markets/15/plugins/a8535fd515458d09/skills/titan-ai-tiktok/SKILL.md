---
name: titan-ai-tiktok
description: Use when a member asks about their TikTok Shop and the Titan AI TikTok tools are available, for example which shops are linked, sales and profit for a period, best and worst products, catalogue prices and cost of goods, stock by warehouse, VAT and fulfilment fee settings, or what Titan teaches and members discuss about TikTok Shop. The tools only read TikTok Shop data through the member's Titan Tools account.
---

# Titan AI TikTok

Titan AI TikTok reads the TikTok Shops linked to the member's Titan Tools account, Titan's
TikTok Shop lessons, and two TikTok Shop spaces of the Titan community.

## Scope

- TikTok Shop data only. These tools have no Amazon data and no data for any other
  marketplace. If the member asks about one, say these tools have no data for it, and never
  present TikTok figures as figures of another marketplace.
- Read-only. No tool can change a price, a cost, a product, a listing, a setting, an ad or
  anything else in TikTok Shop or in Titan Tools. When the member asks for a change, say it
  cannot be made here and that they make it in TikTok Shop or Titan Tools themselves. Never
  say that a change was made.
- Only the shops the linked Titan Tools account reaches. Never present one shop's figures as
  another shop's.
- Every figure in an answer comes from a tool result. Do not estimate or fill in a missing
  figure. A figure you calculate from returned figures (a change between two periods, a
  share) is fine; say that you calculated it.

## Pick the tool

| The member wants | Tool |
| --- | --- |
| Which shops are linked, their currency, whether ads data is connected | `tiktok_list_shops` |
| Sales, profit, fees and ad spend of a shop for a period | `tiktok_account_summary` |
| Which brands, products or SKUs sold most, earned most or lost money | `tiktok_product_summary` |
| Catalogue, prices, cost of goods, unit margin, stock | `tiktok_products` |
| Where the stock of one brand, product or variant sits | `tiktok_inventory_breakdown` |
| Brand names, inactive brands | `tiktok_brands` |
| VAT and seller fulfilment fee settings, and why they change the figures | `tiktok_shop_settings` |
| What Titan teaches about TikTok Shop | `tiktok_lessons` |
| What members discuss in the TikTok Shop community spaces | `tiktok_community` |

A data question needs no lessons search, and a lessons question needs no shop tool.

## Shops

- Every shop tool takes an optional `shopId`. When the account reaches one shop, leave it out.
- When the account reaches several shops and the member did not name one, the tool answers
  `SHOP_SELECTION_REQUIRED` and lists the shops under `organizations`. Ask the member which
  shop they mean, then call again with its `shopId`. Do not choose a shop for them.
- Take a `shopId` only from `tiktok_list_shops` or from `organizations` in an error answer.
- Every successful shop tool answer carries `shop` with `name`, `shopId`, `countryCode`,
  `currency` and `timezone`. Name the shop in the answer.

## Dates (the two summary tools)

- Dates are inclusive UTC calendar days in YYYY-MM-DD form, not the shop's local days. The
  shop `timezone` is information only; the summaries do not use it.
- With no dates, a summary covers the 30 complete UTC days that end yesterday (UTC). Use that
  default when the member gives no period.
- The last day can be yesterday (UTC) at the latest. Today is not complete, so a range that
  ends today or later is refused with `INVALID_DATE_RANGE`. For "this week" or "this month",
  end the range yesterday (UTC) and say so. On the first UTC day of a week or month, no
  complete day of it exists yet: say so and offer the previous period.
- Turn a relative period ("last week", "last month", "Q3") into explicit `startDate` and
  `endDate` values before the call.
- Every summary answer carries `requested` with `currency`, `startDate`, `endDate`, `timezone`
  and `datesDefaulted`. Take the dates and the currency you report from `requested`.
- To compare periods, call the summary once per period, with periods of equal length.

## Currency

- Summary money fields are in the shop's own currency unless `currency` is passed. Pass
  `currency` only when the member asks for another currency, or after `CURRENCY_REQUIRED` or
  `CURRENCY_UNSUPPORTED`.
- The accepted display currencies are CAD, USD, MXN, BRL, EUR, GBP, SEK, ZAR, PLN, EGP, TRY,
  SAR, AED, INR, SGD, AUD, JPY, CNY, CHF and NZD.
- To add up or compare shops that sell in different currencies, pass the same `currency` to
  every call.
- `tiktok_products` takes no `currency`: each row is in its own `currency`, the currency the
  shop sells in.

## Reading the summary figures

- Signs: cost lines (`refunds`, `cogs`, `tiktokFees`, `shippingCost`, `marketing`,
  `affiliateCommission`, `samplesCost`) are negative. `adsSpend`, `ppcSpend` and
  `ppcSpendAuction` are positive. Report a cost as an amount spent, without a double negative.
- Margin chain: `totalNetRevenue` is net revenue after VAT. `cm1` is what is left after cost
  of goods. `cm2` is what is left after `tiktokFees`, the seller fulfilment fee and, when fees
  VAT is on, the VAT in those fees; the last two come only with `detail` true, so `cm1` plus
  `tiktokFees` need not equal `cm2`. `cm3` is what is left after marketing (ads, affiliates
  and samples): the bottom line. `cm1Pct`, `cm2Pct` and `cm3Pct` are percentages of
  `totalNetRevenue`.
- `tiktokFees` is more than TikTok's own charges: it also holds `shippingCost`, statement
  adjustments, and the multi-channel and other fulfilment costs the seller entered per SKU.
  Never subtract `shippingCost` a second time.
- `gmv`, `orders` and `units` count what settled in the period, so they can differ from the
  orders placed in it. `gmv` is what buyers paid for the goods, before fees and refunds.
  `aov` is `gmv` per order. `tacos` is `adsSpend` as a percentage of `totalNetRevenue`.
  `customers` cannot be added up across rows or periods, because one buyer can appear in
  several.
- The summaries leave out brands the shop has disabled. When `tiktok_brands` shows Inactive
  brands, say the figures exclude them.
- Null is not zero. A null figure means there is no data for it: say it is not available and
  why, and never show it as 0. A field that is absent from the answer was not sent.
- Advertising figures (`adsSpend`, `ppcSpend`, `ppcSpendAuction`, `ppcClicks`,
  `ppcImpressions`, `tacos`, `marketing`, `cm3`, `cm3Pct`, `roc3`) are null when the shop's
  advertising data is unavailable, for example when its Business (ads) API is not connected.
  `connections` in `tiktok_list_shops` shows that state. A `connected` value of false alone
  does not prove that the ads authorization was removed, because a failed lookup can show it
  too.
- There are two kinds of ads. GMV Max is `ppcSpend`, with `ppcClicks` and `ppcImpressions`;
  Auction is `ppcSpendAuction`. The unfiltered account summary's `adsSpend` adds both. Auction
  spend never reaches a product summary row, and `ppcSpendAuction` is null in a filtered
  account summary. When the unfiltered `ppcSpendAuction` is above 0, say that ad
  spend, `marketing`, `cm3` and `tacos` per brand or product leave Auction spend out, so
  their `cm3` reads too high.
- A cost per click or per impression divides `ppcSpend` by `ppcClicks` or `ppcImpressions`,
  never `adsSpend`. When `notes` says the clicks and impressions were not reported, do not
  calculate a click-through rate or a cost per click.
- Cost of goods coverage: `skusMissingCogs` above 0 means that many SKUs sold without a cost
  set, so `cogs` and every margin understate the cost. Say so next to the margins.
- `noResults` on a summary means orders, units and gmv are all zero: nothing sold in scope, or
  the filters matched nothing. Refunds, fees or ad spend can still be non-zero.
- A summary filtered by `brands`, `spus` or `skus` counts statement adjustments as 0, so a
  filtered figure can differ from the same part of the unfiltered total.
- `detail` true returns every field Titan Tools reports (over 100 per row). Use it only when
  the member asks for a figure the default answer does not carry.

## Filters, grains and paging

- Which tool takes which filter: the two summaries take `brands`, `spus` and `skus`.
  `tiktok_products` takes those and also `skuIds`, `search` and `hideInactive`.
  `tiktok_brands` takes `status` and `search`. A tool ignores an argument it does not take
  and answers unfiltered, with no error. So never pass `search` or `skuIds` to a summary:
  find the exact values with `tiktok_products` first.
- `brands`, `spus`, `skus` and `skuIds` are exact, case-sensitive filters, combined with AND.
  Copy their values from tool output: `brand` from `tiktok_brands`, `spu`, `sku` and `skuId`
  from `tiktok_products`. `search` is case-insensitive and matches a part of a name.
- Grains, from wide to narrow: `brand`, `spu` (one TikTok product), `sku`. To drill down,
  filter by the row's `key` at the next grain: `brands` with `groupBy` set to `spu`, then
  `spus` with `groupBy` set to `sku`.
- The `sku` grain differs between the tools. In `tiktok_products` a `sku` row is one TikTok
  variant and its `key` is the `skuId`, TikTok's variant id. In `tiktok_product_summary` a
  `sku` row is one seller SKU label, its `key` is that label, and it can cover several
  variants. To read a catalogue variant's sales, pass its `sku` (the seller label, not its
  `key`) in `skus`. `tiktok_product_summary` carries no `skuId`.
- Paged answers carry `total`, `page`, `pageSize`, `totalPages` and `hasNext`. When `hasNext`
  is true, say that more rows exist, or ask for the next `page` when the member needs every
  row. A page holds at most 100 rows.
- An empty page carries `noResults` and a `hint`. Follow the hint, for example drop a filter
  or ask for an earlier page.

## The tools

### `tiktok_list_shops`

- No inputs. Answers `shopCount` and `organizations`, each with `name`, `role` and `shops`.
  Each shop has `name`, `shopId`, `countryCode`, `currency`, `timezone` and `connections`
  with `shopApi` and `businessApi`, each of them with `connected` and `connectedAt`.
- `adsNote` is present when at least one shop's `businessApi` is not `connected`: for that
  shop the summaries answer advertising figures as null.
- Call it when the task needs a `shopId`, a shop's currency or the ads connection state. It
  is not needed before every call.

### `tiktok_account_summary`

- One flat object for the shop over the period, optionally filtered by `brands`, `spus` or
  `skus`. Default fields: `gmv`, `sales`, `orders`, `units`, `customers`, `aov`,
  `grossRevenue`, `netRevenueChain`, `refunds`, `refundCount`, `refundPct`,
  `totalNetRevenue`, `cogs`, `cm1`, `cm1Pct`, `cm2`, `cm2Pct`, `cm3`, `cm3Pct`, `tiktokFees`,
  `shippingCost`, `marketing`, `affiliateCommission`, `samplesCost`, `adsSpend`, `ppcSpend`,
  `ppcSpendAuction`, `ppcClicks`, `ppcImpressions`, `tacos`, `roc2`, `roc3`, `skusInScope`
  and `skusMissingCogs`, plus `requested` and, when there is something to say, `notes`.
- Use it for shop totals. Product summary rows can overlap, so their sum is not the total.

### `tiktok_product_summary`

- One row per `groupBy` value (`brand`, `spu` by default, or `sku`), sorted by `sortField`
  (`gmv` by default) in `sortDirection` (`desc` by default), 10 rows per page by default.
- Each row carries `rowType`, `key`, `brand`, `spu`, `sku`, `title`, `variantCount`,
  `productCount` and the figures `gmv`, `units`, `orders`, `customers`, `aov`,
  `grossRevenue`, `netRevenueChain`, `refunds`, `refundPct`, `totalNetRevenue`, `cogs`,
  `tiktokFees`, `shippingCost`, `marketing`, `affiliateCommission`, `cm1`, `cm1Pct`, `cm2`,
  `cm2Pct`, `cm3`, `cm3Pct`, `adsSpend`, `ppcSpend` and `tacos`, plus `requested`.
- Ad figures on a row count GMV Max ads only. They do not reach SKU rows: on `sku` rows
  `adsSpend`, `ppcSpend`, `tacos`, `marketing`, `cm3` and `cm3Pct` are null. For advertising
  by item, use `spu` or `brand`.
- Sorting: `desc` puts the largest value first. The cost columns (`cogs`, `tiktokFees`,
  `marketing`) are negative here, so for the largest cost sort them `asc`. For the lowest
  value of any other column, sort `asc`.
- A row with `cogs` 0 while its `units` are above 0 has no cost of goods entered for any of
  its SKUs, so its margins read too high. Say so, and do not rank it as a top earner on
  margin; its variants in
  `tiktok_products` show which costs are missing.
- Only keys with activity in the period come back; a row can show 0 `units` when the period
  holds only refunds. A product with no activity does not appear, so the lowest row is not
  the worst product of the catalogue.

### `tiktok_products`

- Catalogue rows at `groupBy` `sku` (the default), `spu` or `brand`, 50 per page by default,
  sorted by `sortField` (`title` by default; also `price`, `cogs`, `grossProfit`, `stock`,
  `status`, `vatRate`). `hideInactive` true drops variants TikTok does not list as active.
  Variants of disabled brands are not returned.
- A row with `skuCount` 1 carries `price`, `cogs` and `grossProfit`. A row that folds several
  variants carries `priceMin`, `priceMax`, `cogsMin`, `cogsMax`, `grossProfitMin` and
  `grossProfitMax` instead. Fields with no value are left out, and `imageUrl` comes only with
  `detail` true.
- `grossProfit` is the price minus the cost of goods for one unit, in the row `currency`,
  before fees and VAT. It is an amount, not a percentage.
- `cogs` 0 with an empty `cogsCurrencyCode` means the seller never entered a cost for that
  variant, so its `grossProfit` overstates profit. Say so.
- On a group row, a variant with no cost counts as 0 in `cogsMin`, so `grossProfitMax` can
  overstate profit. A group row sorts by the low end of its range (by its total for `stock`).
- `stock` is the sellable units on hand across all warehouses, without the units already
  reserved by orders (`committed` in `tiktok_inventory_breakdown`). A group row gives the
  total of its variants. `status` is TikTok's listing status of the variant; a group shows
  MIXED when its variants differ.
- Quote a VAT rate (`vatRatePercent`, `effectiveVatRatePercent`, `defaultVatRatePercent`)
  only when `vatEnabled` is true. When it is false, ignore every rate on the page.
- Rows under the brand SYSTEM_TEMPORARY_LISTINGS (`listingType` TEMPORARY_LISTING) are LIVE
  Auction temporary listings, priced 0, in a bucket Titan Tools assigns; it is not a real
  brand. Leave them out of price, margin and missing-cost lists.

### `tiktok_inventory_breakdown`

- Explains one row's `stock`: `rows`, one per warehouse that holds units, with `warehouseId`,
  `name`, `type`, `subType`, `region`, `available` and `committed`, most available first.
- Take `level` from the grain of a `tiktok_products` row and `key` from that row's `key`: a
  brand name at `brand`, an SPU at `spu`, or at `sku` the `skuId` (the `key` of a variant
  row), never the seller SKU label.
- Added up, `available` is the row's `stock`. `committed` units are reserved by orders and
  are part of neither. A null `name` is probably a warehouse TikTok manages; show its
  `warehouseId`.
- An empty answer (`noResults`) is also what a wrong `key` looks like. Check the key before
  you tell the member there is no stock.

### `tiktok_brands`

- `items` with `brand`, `status` (`Active` or `Inactive`) and `skuCount`, ordered by name,
  filtered by `status` or `search`. Inactive brands show only here; every other shop tool,
  the summaries included, hides them.
- SYSTEM_TEMPORARY_LISTINGS is not a real brand: it is a bucket Titan Tools assigns to LIVE
  Auction temporary listings. Say so when you list brands.

### `tiktok_shop_settings`

- Answers `salesVatActive`, `salesVatStartDate`, `salesVatDefaultRatePercent`,
  `feesVatActive`, `feesVatStartDate`, `feesVatRatePercent`, `countryStandardVatRatePercent`
  and `sellerFulfillmentFeePeriods`, each period with `effectiveFrom`, `feePerPackage` and
  `currency`.
- `salesVatActive` and `feesVatActive` say whether VAT is applied. Each needs its switch on
  and a start date, and fees VAT also needs sales VAT. Quote a VAT rate only when that VAT is
  active. A shop that never set VAT up shows its country's standard rate in
  `salesVatDefaultRatePercent`; that does not mean VAT is applied.
  `countryStandardVatRatePercent` is a reference rate only and is used in no figure.
- An empty `sellerFulfillmentFeePeriods` means no seller fulfilment fee, and a period with
  `feePerPackage` 0 has none in that period. A null `effectiveFrom` means from the start of
  the shop history. A fee change reaches the summary figures only after a recalculation.
- These dates are days in the shop's reporting timezone, not UTC days, so they can sit one day
  away from a summary period.
- Use it when net revenue or `cm2` from `tiktok_account_summary` looks different from what the
  member expects.

### `tiktok_lessons`

- Takes `query` in plain words and `maxResults` from 1 to 10 (5 by default). Searches Titan's
  TikTok Shop training: the TikTok Profit System course and the cross-platform Brand Workbook.
- Each result can carry `title`, `section`, `space`, `spaceGroup`, `lessonDate`, `text`,
  `url` and `score`. Base the answer on the returned `text` and name the lesson `title`.
- Give a link only from a returned `url`. Never build or guess a lesson link.
- `newestMatchDate` and `freshnessHint` give the newest dated item among the candidates the
  search retrieved, not a date for the whole library. If the member asks about something
  newer, say what was and was not found.
- An empty answer (`noResults`) means nothing matched these words, not that Titan has no
  material on the subject. Try other words once before you say nothing was found.

### `tiktok_community`

- Takes `query` and `maxResults` like `tiktok_lessons`. Searches only the two TikTok Shop
  spaces of the Titan community (TikTok Shop Feed and TikTok Shop Updates), not the
  community's general discussion.
- Each result carries `title`, `parent_post_title`, `space_name`, `created_at`, `post_type`,
  engagement counts (`like_count`, `comment_count`, `comments_count`, `reply_count`) and
  `score`. It carries no post text, no author and no link: do not quote a post, name an
  author or offer a post link.
- A community post is what a member wrote, not Titan guidance. Present it as community
  discussion, apart from lessons.

## Common tasks

- **Shop review for a period:** `tiktok_account_summary` for the period, then
  `tiktok_product_summary` at `spu` for the top rows. Report sales, refunds, costs, the three
  margins, advertising, the top products, and each data gap (missing cost of goods, no ads
  data, Auction spend left out of product rows, disabled brands left out).
- **Compare two periods:** two `tiktok_account_summary` calls of equal length. Give both
  periods and the change in amount and in percent.
- **Best or worst products:** `tiktok_product_summary` with the member's measure as
  `sortField`. Mind the sort direction of the negative cost columns, and flag rows with
  `cogs` 0.
- **Stock check:** `tiktok_products` sorted by `stock` (`asc` for the lowest, `desc` for the
  most), with `hideInactive` true when only live listings matter. For one row's warehouses,
  `tiktok_inventory_breakdown` with that row's grain as `level` and its `key`.
- **Unit margin and missing costs:** `tiktok_products` at `sku`, reading `price`, `cogs` and
  `grossProfit`, and listing the variants with no cost entered, without the temporary
  listings.

## When a tool answers an error

An error answer has `error` true, a `code`, a `message`, `retryable` and usually a `hint`.
Follow the hint. Retry only when `retryable` is true or the hint says to. Tell the member what
happened in plain words; do not paste the error, and do not guess another cause.

| `code` | What to do |
| --- | --- |
| `SHOP_SELECTION_REQUIRED` | Ask which shop, naming the shops in `organizations`, then call again with its `shopId`. |
| `SHOP_ACCESS_DENIED` | The linked account cannot read that shop. Offer the shops it does reach (from `organizations` or `tiktok_list_shops`). |
| `NO_SHOPS` | Retry once. If it stays, tell the member no TikTok Shop is visible to their Titan Tools account and to check in Titan Tools that the shop is connected. Do not say a connection was removed. |
| `LINK_REQUIRED` | The member removes Titan AI TikTok in their AI app and adds it again, which signs them in to Titan Tools afresh. |
| `ACCESS_DENIED` | The account is not allowed to read this data. If its permissions changed, removing and adding Titan AI TikTok again picks up the change. |
| `UPSTREAM_AUTH_UNAVAILABLE` | A temporary network problem. Retry shortly. Do not ask the member to link the account again. |
| `UPSTREAM_RATE_LIMIT` | Wait a few seconds (`retryAfterSeconds` when present) and retry once. |
| `UPSTREAM_TIMEOUT` | Narrow the request (a shorter period, a filter or a smaller page) instead of repeating it. |
| `UPSTREAM_UNAVAILABLE` | On a shop tool, retry once; if it fails again, say the data is unavailable right now. On the lessons or community search, retry once or answer without that source. |
| `INVALID_DATE_RANGE` | Correct the dates: YYYY-MM-DD, start on or before end, end no later than yesterday (UTC). |
| `CURRENCY_REQUIRED`, `CURRENCY_UNSUPPORTED` | Pass `currency` from the accepted list; ask the member which one if they named none. |
| `INVALID_ARGUMENTS`, `INVALID_REQUEST` | Correct the arguments against the tool's inputs and call once more. |
| `UPSTREAM_REJECTED` | Titan Tools refused the request. Do not repeat it unchanged; say it could not be read. |
| `BETA_ACCESS_REQUIRED` | The account has no access to Titan AI TikTok yet. Tell the member, with the way to ask for access from the hint. Do not retry. |
| `INTERNAL_ERROR` | A server problem. Nothing was changed. Say it is unavailable right now; do not retry. |
| `RATE_LIMIT` | The lessons or community search is rate limited. Retry once after a few seconds, or answer without that source. |
| `PROVIDER_OUTAGE`, `CONFIGURATION`, `AUTH_FAILURE`, `UNKNOWN` | The lessons or community search is unavailable. Do not call it again in this turn; answer without it and say so. |

## Answer format

- Lead with the answer to the question, then the figures behind it.
- Name the shop, the period (from `requested`) and the currency.
- Show money with its currency code and two decimals, percentages with one decimal, and
  counts as whole numbers.
- Use a table for several rows (products, warehouses, shops), in the order the tool returned.
- Give each data gap in one line: what is missing and why. Never show a missing figure as 0.
- Use plain words for figures (for example "contribution margin after fees" for cm2) and keep
  tool names, field names and error codes out of the answer unless the member asks for them.
