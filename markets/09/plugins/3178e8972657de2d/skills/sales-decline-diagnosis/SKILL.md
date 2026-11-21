---
name: sales-decline-diagnosis
description: Diagnose why sales of a category, supplier, brand, range or product fell, working from a spreadsheet, CSV or pasted figures. Splits the change into units, price, mix and returns effects that add up exactly to the fall, then works through the possible causes (availability, range changes, promotions, market demand, competition, visibility), checking the cheapest decisive facts first and saying plainly what is ruled out and what the data cannot show. Use when someone asks "why are sales down", "why did this category drop", "what's driving the decline", "explain the fall versus last year", "is it price or volume", "sales are down 12%, why?", or shares a sales export and wants the drop explained. Not for a plain lookup of last week's sales, a margin-only question, or a forecast.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: general
---

# Sales decline diagnosis

Answer "why did sales fall" the way a retail analyst would. First prove the fall
is real, then split it with arithmetic that sums exactly to the change, then test
possible causes in the order that rules the most out for the least effort. Say
what you ruled out and what you could not see, not only what fits.

The full list of possible causes, with the test and the question for each, is in
[references/hypothesis-tree.md](references/hypothesis-tree.md). A complete worked
example with numbers is in [references/worked-example.md](references/worked-example.md).

## The data

Ask for, or look for, one row per product per period (week or month), covering
the period that fell and the same weeks a year earlier.

| Column | Needed | Used for |
| --- | --- | --- |
| Period (week or date) | Required | Lining up this year against last year |
| Product ID and name | Required | Price and mix split; which lines carry the fall |
| Units sold | Required | Units effect |
| Sales value, one tax basis | Required | Every effect |
| Category, supplier or brand | Strongly wanted | Locating the fall |
| Promotional units (or a promo flag) | Optional | Promotion |
| Returns, refunds or cancellations value | Optional | Realisation |
| Order or transaction count | Optional | Orders against basket size |
| In stock flag, or stock on hand per week | Optional | Availability |
| Channel, store or region | Optional | Locating the fall |
| Shelf price and competitor price | Optional | Price and competition |

If the person only has totals for each period, you can still split units from
average price, but not price from mix. Say so.

## Before anything: is the fall real?

Check these before you explain anything. A failure here is the answer.

- The latest week is complete, and both periods have the same number of weeks.
- The weeks line up: Easter, a school holiday, a sale event or a 53rd week can
  move sales between periods without any change in demand. Compare aligned weeks.
- Same tax basis (both ex GST, or both inc) and same currency on both sides.
- Nothing changed in how sales are recorded: a channel recoded, a store or
  supplier reassigned, a category remapped.
- Compare the category's change with the rest of the business. If everything
  fell by the same share, the problem is bigger than this category; say that first.

## Step 1: split the change

Use per-line figures. Subscript 0 is last year, 1 is this year.

```
Change in net sales      = Net1 - Net0
Last year's price/unit P0 = Gross0 / Units0
Units effect             = (Units1 - Units0) x P0
Price effect             = sum over lines sold in both periods of (price1 - price0) x units1
Mix effect               = (Gross1 - Gross0) - Units effect - Price effect
Realisation effect       = -(Leakage1 - Leakage0), where Leakage = Gross - Net
```

The four effects add up to the change by construction (mix is the remainder).
Show the sum check before quoting any of them. Mix covers units moving between
cheaper and dearer lines, and lines that sold in only one period.

If returns are already netted out of the data, run units, price and mix on net
sales and treat realisation as unknown.

If order counts exist, split the units effect again:

```
Units per order  = Units / Orders
Orders effect    = (Orders1 - Orders0) x UnitsPerOrder0 x P0
Basket effect    = (UnitsPerOrder1 - UnitsPerOrder0) x Orders1 x P0
```

These two add up to the units effect. Fewer orders points at reasons a shopper
did not buy at all (availability, range, competition, demand). Smaller baskets
point first at promotions (multi-buys dropped) and range (add-on lines gone).

## Step 2: locate it

Cut the change by supplier, channel, store, sub-category and line. Cuts tell you
where the fall sits, never why. Read them for what they rule out:

- Same fall in every channel: not a channel-specific problem.
- Every major supplier down by a similar share: not one supplier's problem.
- Most of the fall in a few lines: range or availability on those lines.
- A broad, even fall: demand, promotion, competition, or category-wide availability.

## Step 3: work the causes

Below the arithmetic, a lost unit fails at one step on the way to a sale. That
gives six causes, each with one home:

| Cause | The unit was lost because | Cheapest test |
| --- | --- | --- |
| Availability | A line we carry was out of stock more than last year | Units in weeks in stock against weeks out |
| Range | Lines left, or last year's launch has no successor | Lines sold in one period only; continuing lines' change |
| Promotion | We ran fewer, shallower or shorter promotions | Base units (total less promo) against last year |
| Demand and market | Fewer people are buying the category anywhere | Category change against the rest of the business; weekly shape |
| Competition | Rivals got cheaper or louder, or a new seller arrived | Our price against competitors' on the top lines |
| Visibility | Shoppers could not find the line (space, position, listing) | Usually not in the data; ask |

Boundary rules, so a unit is not counted twice:

- A line no longer carried is range. A line carried but out of stock is
  availability. A supplier cutting our allocation is availability.
- Our own promotions are promotion. Our everyday price against rivals, and their
  promotions, are competition.
- If the market fell, it is demand. If the market held and we lost share, it is
  one of ours or competition. Without market data this boundary is a question.

## Step 4: rule out cheapest first

Use the figures already in hand to rule causes out, then order the rest by size
of the effect times how much the person can do about it.

| Fact | Rules out | Points to |
| --- | --- | --- |
| Average price per unit within a few percent of last year | A large price effect | Units |
| Base units fell as much as total units | Promotion | Other unit causes |
| Lines in stock every week fell by the same share as the rest | Availability | Other unit causes |
| Lines sold in both periods fell by the same share as the category | Range | Demand, promotion, competition |
| Category fell no more than the rest of the business | Category-specific causes | Demand, business-wide; reframe |
| Our price index on top lines at or below parity and flat | Competition on price | Other causes |
| Fall sits in a few lines | Demand as the main cause | Range, availability on those lines |

Then look for evidence against your leading explanation: the lines it does not
cover, the weeks it was absent and sales still fell. Two things moving together
is not a cause.

## Missing data: say what you cannot rule out

| Missing | What stays open |
| --- | --- |
| Per-line data (totals only) | Price and mix cannot be separated; range cannot be tested |
| Promo flag | Promotion is a question for the person |
| Stock history | Availability cannot be ruled out; long gaps between deliveries can only suggest it |
| Returns | Realisation is unknown; other effects are read on net |
| Order counts | Fewer orders against smaller baskets is unknown |
| Competitor prices | Competition is a question; never claim a rival took share without it |
| Market or panel data | Demand against lost share is a question |
| Space or listing changes | Visibility is a question |

Turn each gap into one direct question ("Were any of the top five lines out of
stock in August?"). What the person tells you is their account: attribute it
("you said the range didn't change") and never present it as a measured figure.

## How to word it

- An arithmetic effect is a contribution: "units account for most of the fall".
  Never "because".
- A cause is "the cause" only when the data supports it and every rival beside it
  has been ruled out by data. Otherwise "consistent with", and name the rival
  still open.
- State the period, comparison and tax basis once.
- Show every derived figure as a calculation, for example
  "units effect = (1,580 - 2,000) x $23.00 = -$9,660".

## Answer shape

1. **The answer in one or two sentences**, reframed if the data changed the
   question ("this is a volume problem across the whole business, not a price
   problem in this category").
2. **The split**: the four effects with their calculation and the sum check.
3. **What the evidence shows**: the causes that fit, with the figure for each.
4. **Ruled out**: each with the figure that ruled it out.
5. **Still unknown**: each with the one question or data extract that would settle it.
6. **Options**: two or three things the person could do, each with what has to be
   true for it to work ("restore the dropped promotion; works if those promo
   units were extra sales, not pulled forward"). Keep the first reply short.

## With Twelfth connected

If the person has the Twelfth MCP server connected (twelfth.ai), these tools fill
in what a spreadsheet usually lacks. Call `twelfth_get_workspace` first for
currency and timezone, and resolve names before filtering:
`search_catalogue` for products, `find_supplier` for suppliers,
`twelfth_list_category_settings` for category IDs.

- Line figures: `twelfth_list_products` (filter by category or supplier, sort by
  recent units, last year's units or rate-of-sale trend) or `twelfth_get_products`
  for a column of SKUs. These are current figures, not a weekly two-period series,
  so the exact split in Step 1 still needs the person's own period extract.
- Availability: stock and cover from `twelfth_list_products`; daily stock
  history for tracked lines from `price_intel_history`; supplier depletions from
  `compare_supplier_offer_history`; lead times from `get_supplier_constraints`.
- Range and our own price moves: `recall_decisions` (exits, end-of-life marks,
  price changes, with the reasons recorded at the time).
- Promotion: `get_planning_calendar` with type promo for both windows.
- Competition: `price_intel_summary`, `price_intel_lookup`,
  `price_intel_observations` and `twelfth_compare_pricing_skus`.
- Playbook guidance on a cause: `get_methodology`.

`get_entity_profile`, `get_sales_metrics`, `get_inventory_position` and the
other `get_*` line tools read only the lines in the open work unit; an empty
result there is not proof a line is unranged or unsold.
