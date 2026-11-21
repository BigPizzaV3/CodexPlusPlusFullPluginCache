---
name: range-review
description: Run a retail range review on a category from a spreadsheet, CSV or pasted product list. Scores each line on rate of sale, trend, contribution and return on stock, groups lines by the shopper need they serve, estimates where a cut line's buyers would go, and recommends keep, cut, fix stock depth or add, with the net effect on category contribution shown as a calculation. Handles supplier proposals, slow sellers, end-of-life stock and gaps in the range. Use when someone asks "which lines should I delist", "review my range", "rationalise the tail", "what should I cut from this category", "is this slow line worth keeping", "the supplier wants us to range X and drop Y", "how deep should we range this", or shares a product sales export and wants range decisions. Not for diagnosing a sales fall, setting a price, or building a planogram.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: general
---

# Range review

Decide which lines stay, which go and where the range has gaps, judged on what
happens to the whole category, not on each line's own sales. A slow line whose
buyers switch to a better-margin neighbour can be a good cut. An average line
whose buyers would leave the store is an expensive one.

A complete worked example with numbers is in
[references/worked-example.md](references/worked-example.md). Guidance on
estimating where demand goes, when there is no clean data, is in
[references/transferable-demand.md](references/transferable-demand.md).

## The data

One row per line, ideally for the last 52 weeks with the last 13 weeks split out.

| Column | Needed | Used for |
| --- | --- | --- |
| Product ID, name, sub-category | Required | Grouping |
| Supplier and brand | Required | Supplier proposals; concentration |
| Units sold and sales value (one tax basis) | Required | Rate of sale, share |
| Unit cost (what it costs to buy or reorder one more) | Required | Contribution |
| Units in the last 13 weeks and prior 13 (or same 13 last year) | Strongly wanted | Trend |
| Stores ranged, and weeks in stock | Strongly wanted | Fair rate of sale |
| Average stock at cost, stock on hand | Strongly wanted | Return on stock, cover |
| Attributes (size, price tier, format, use) | Wanted | Need states |
| Returnable to supplier, reorderable | Wanted | Exit stock |
| Basket data, or past out-of-stock weeks | Optional | Where demand goes |
| Space or facings | Optional | What a freed slot is worth |

Missing cost: you can rank on sales, but cannot judge contribution or return on
stock; say every cut is provisional. Missing stores or weeks in stock: rate of
sale will understate lines that were ranged late, ranged narrowly or out of
stock; flag those lines rather than cutting them. Missing basket or stock-out
history: transfer of demand is an assumption; run it as a range (below).

## Step 1: set the frame

Ask what the category is for before scoring any line. The answer sets how deep
to range.

- **Destination**: the reason shoppers come; earns depth and a longer tail.
- **Routine**: bought often and price-checked; mainstream depth, sharp pricing.
- **Occasional or seasonal**: depth in season, thin out of season.
- **Convenience**: completes the trip; the best sellers only.

Also ask what it should deliver: traffic, profit, cash, or image. This is the
person's call. Infer a suggestion from the data (share of store sales, how often
it is bought, how price-checked it is) and confirm it; do not silently treat a
high-volume category as a destination.

## Step 2: group lines by need

Group lines by the job they do for the shopper (for example everyday, premium,
gifting, bulk) using attributes and, where available, what is bought together or
instead of each other. Every need state keeps at least one line. A thin seller
that is the only line in its need state is not a tail line.

## Step 3: score each line

```
Rate of sale (ROS)   = units / (stores ranged x weeks in stock)
Trend                = ROS last 13 weeks / ROS prior 13 weeks   (or same weeks last year)
Unit contribution    = sell price ex tax - unit cost
Contribution         = units x unit contribution
Margin %             = contribution / sales
Return on stock      = annual contribution / average stock at cost   (GMROI)
Weeks of cover       = stock on hand in units / average weekly units
Share of category    = line sales / category sales, ranked and accumulated
```

Use only costs that change with the decision. Allocated overheads stay whether
the line does or not; leave them out.

Return on stock earns its place in ranges bought upfront where turns vary a lot
(toys, games, apparel, hardware, auto parts, general merchandise). In ranges
replenished just in time, owned stock is thin and similar across lines, so
contribution and rate of sale lead. Never compare a slow, structural category's
return on stock with a fast one's, and read the ratio next to the dollars: a
high return on a tiny base is still a small contributor.

## Step 4: gates before any line is flagged

Hold these lines out of the cut screen and say why:

- The only line in a need state.
- A traffic driver or a line shoppers price-check.
- A basket anchor, bought alongside many other lines.
- A line with a loyal base that would leave rather than switch (common in baby,
  health, specialist and enthusiast categories).
- A seasonal line: judge it on its season, not 52 weeks.
- A new line still building: judge it on its time in range, not against mature
  lines.

## Step 5: flag candidates

Flag a line when it is weak within its own need state on all three: low rate of
sale, flat or falling trend, low contribution. Do not flag on a category-wide
ranking alone; a rule like "cut the bottom 20% of sales" can strand a whole
need state. A flag is a signal for the review, not a decision.

## Step 6: where would its buyers go?

For each flagged line, estimate how its units would split when it is gone:
switch to a line you keep, or walk.

```
Recovered contribution = sum over receiving lines of
                         (share of cut units moving to that line) x cut units x receiver's unit contribution
Net annual effect      = recovered contribution - cut line's contribution
                         + contribution of whatever takes the freed space
```

Separately, as a one-off: the cash released from the cut line's stock (at what it
will actually clear for).

Only credit a receiver that is staying in the range and has the supply and space
to absorb the extra units. Out-of-stock history is the best evidence of
switching, but treat it as an upper bound: a permanent delist loses more
shoppers than a temporary gap. With no evidence, run a low and a high share; if
the decision flips between them, it is a question, not a recommendation. See
[references/transferable-demand.md](references/transferable-demand.md).

## Step 7: stock already bought

Decide keep or cut on future contribution. What the existing stock cost is spent
either way.

- Returnable: compare the supplier's credit with what clearance would recover.
- Not returnable and not reorderable (a season, a limited run, a discontinued
  line): set the clearance price that recovers the most cash before the stock
  ages. "Never sell below cost" does not apply; the cost is already sunk. Do not
  apply this to core lines you will reorder.
- A weak line with too much stock may need less depth, not deletion. Cut cover
  before you cut the line.

## Step 8: supplier proposals

Judge a supplier's range proposal on the whole category: total units and
contribution before and after, and how much of the featured line's gain comes
out of your other lines. A supplier pitches the same plan to every retailer and
rarely proposes cutting its own lines. Use their data as input; keep your own
read.

## Step 9: gaps

Look for need states with few lines against the demand they carry, and price
tiers with no line. A new line enters on merit when it is expected to beat what
it replaces; otherwise give it a defined trial slot and a date to judge it.

## Answer shape

1. **The recommendation**: the changes and the net effect on category
   contribution, with the calculation.
2. **Line table**: line, need state, ROS, trend, contribution, return on stock,
   call (keep, keep and cut depth, review terms, seasonal, cut, add), one-line reason.
3. **Protected lines**: what the gates kept and why.
4. **Assumptions and unknowns**: transfer shares and where each came from; what
   data would firm them up.
5. **Next steps**: supplier notices, checks on receivers' supply, a plan for exit
   stock, and when to review the result.

Show every derived figure as a calculation. Say which figures are estimates.

## With Twelfth connected

If the person has the Twelfth MCP server connected (twelfth.ai), these tools
replace most of the spreadsheet. Start with `twelfth_get_workspace` for currency
and timezone, and resolve names first: `twelfth_list_category_settings` for
category IDs, `find_supplier` for suppliers, `search_catalogue` for products.

- Line figures: `twelfth_list_products`, filtered by category or supplier and
  sorted by recent units, last year's units, rate-of-sale trend, GP%, cover or
  days since sold. `twelfth_get_products` fills figures for a list of SKUs.
- Supply and exit options: `get_supplier_constraints` (lead time, carton,
  on order), `compare_supplier_offer_history` (lines a supplier has dropped or
  run down), `recall_decisions` (past exits and end-of-life marks, with reasons).
- Price-checked lines: `price_intel_lookup` and `twelfth_compare_pricing_skus`.
  Daily stock history from `price_intel_history` shows past out-of-stock windows
  on tracked lines, which feed Step 6.
- Playbook guidance on ranging: `get_methodology`.

`find_similar_products`, `get_product_ranking` and the other `get_*` line tools
read only the lines in the open work unit. Use them for substitutes and ranking
among those lines; for the whole category, use `twelfth_list_products`.
