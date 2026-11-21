# The cause tree for a sales decline

The top of the tree is arithmetic (units, price, mix, realisation), so it covers
the whole change by construction. Below the units effect, the causes follow the
path a unit takes to a sale: a shopper wants the category (demand), we carry a
line they want (range), it is in stock when they come (availability), they can
find it (visibility), and our offer holds up against our own past offers
(promotion) and everyone else's (competition). A lost unit fails at one step, so
it belongs to one cause.

Channel, supplier, store, sub-category and line are cuts applied to every cause.
They locate the fall; they are never a cause on their own.

## Arithmetic level

### Units
Fewer units sold. Test: units effect from the split. Carries the fall if it is
most of the change.

- **Orders** (needs order counts): fewer orders containing a line in scope.
  Points to availability, range, visibility, competition, demand.
- **Units per order** (needs order counts): smaller baskets. Points to
  promotion (multi-buys dropped) and range (add-on lines gone).
- Without order counts, ask: "Are you seeing fewer orders, or about the same
  number with fewer items in each?"

### Price
A lower average selling price on lines sold in both periods. Rule it out when
average price per unit is within a few percent of last year. If material:

- **Shelf price**: everyday prices were lowered. Test: shelf price history.
  Ask: "Did we change shelf prices on these lines?"
- **Discounting**: more volume sold on deeper discounts or markdowns. Test:
  promo sales / promo units against base price per unit, both periods.
  Ask: "Have we been marking these lines down or clearing them?"

### Mix
Units moved to cheaper lines, or lines that sold in only one period changed the
average. Mix has no causes of its own: a material mix effect hands over to range
(lines came or went) or demand (shoppers trading down).

### Realisation
More sales lost after the sale: returns, refunds, cancellations, failed
payments. Test: leakage as a share of gross sales, both periods. Rule out if
the share is flat. Locate a material effect by line or channel (one faulty
product, one channel's delivery or checkout). Ask: "Have returns or
cancellations gone up, or has anything changed at checkout or in delivery?"

## Causes under units

### Availability
Lines we carry were out of stock, in store or in the warehouse, more often than
last year.
- Test: in-stock weeks per line, both periods; units per in-stock week against
  units in out-of-stock weeks. Supported if the lost units sit in the weeks or
  lines with less stock.
- Without stock history: long gaps between deliveries on the top lines fit a
  supply problem. That can support availability but never rule it out.
- Rules it out: lines in stock every week fell by the same share as the rest.
  A similar fall at every supplier makes one supplier's supply problem unlikely,
  but not availability as a whole.
- Ask: "Were any of the main lines short or out of stock this period, from the
  supplier or in our warehouse?"

### Range
The lines on offer changed: best sellers deleted, last year's launch not
repeated, new lines not filling the gap.
- Test: lines with sales last year and none this year (gone), lines new this
  year, and how much of the fall the top ten lines carry.
- Rules it out: lines sold in both periods fell by about the same share as the
  whole category.
- Ask: "Did we delete or lose any lines, or was there a big launch last year
  that hasn't been repeated?"

### Promotion
We ran fewer, shorter or shallower promotions than last year.
- Test: promotional units and base units (total less promotional), both
  periods; the two promotion calendars side by side.
- Rules it out: base units fell as much as total units, or promotional units
  held or grew.
- Ask (also when there is no promo flag): "Did we run fewer or smaller
  promotions on these lines than last year?"

### Demand and market
Fewer people are buying the category anywhere: a trend, a gap in the product
cycle, a shift in when people buy.
- Test: this category's change against the rest of the business; the weekly
  shape (a steady slide is a trend, a step is an event, a spike last year is
  something being lapped). Continuing lines that were in stock and not on
  promotion still falling fits demand.
- With market data: split into market size (the market shrank and we fell with
  it) and our share (the market held and we lost share). If share carries the
  fall, test competition next.
- Rules it out: the fall sits in a few lines while the rest of the category held.
- Ask: "Are suppliers or the industry saying this category is down across the
  market? Are we between product cycles?"

### Competition
Rivals' offer got better against ours: lower prices, deeper promotions, a new
competitor or marketplace seller.
- Test: our price index against competitors on the top lines over the period,
  and how it moved.
- Rules it out: our index on these lines at or below parity and unchanged.
- Without competitor prices this stays a question. Never assert a competitor
  took share without data.
- Ask: "Has a competitor been cheaper or louder on these lines, or has a new one
  started selling them?"

### Visibility
Shoppers could not find the lines: less space, a worse position, a layout
change, a weaker online listing.
- Test: rarely in sales data. A fall in one channel or a few stores fits; the
  same fall everywhere makes a local problem unlikely (a change applied
  everywhere at once is still possible).
- Ask: "Did the space, position or online listing for these lines change?"

## Where a borderline case goes

| Case | Cause |
| --- | --- |
| Line no longer carried; last year's launch with no successor | Range |
| Line carried but out of stock; supplier cut our allocation | Availability |
| Our promotions (count, depth, timing) | Promotion |
| Our everyday price against rivals; rivals' promotions | Competition |
| Market fell | Demand |
| Market held, our share fell | One of ours, or competition |
| Our price move: effect on revenue per unit | Price (arithmetic) |
| Our price move: effect on units | Competition (we moved against the market) or demand (everyone moved) |
| Store traffic down | Demand, or visibility if it is one store |
| Recording or channel-coding change; calendar misalignment | The "is the fall real" checks |
| Pricing error | Price, or competition |

## Typical order, after the cheap kills

For a broad, unit-led fall at flat prices, where the goal is to win the sales
back: availability, range, promotion, competition, demand, then visibility. How
much the person can act on each:

| Cause | Ability to act |
| --- | --- |
| Availability | High: orders, supplier escalation |
| Promotion | High |
| Price | High |
| Realisation | Medium: a faulty line or checkout fault can be fixed; a returns policy is slower |
| Range | Medium: a successor line takes time |
| Competition | Medium: costs margin |
| Visibility | Medium |
| Demand | Low: decides whether to chase the sales or right-size to them |

If the goal is instead to free up stock the fall has left behind, reorder:
demand first (will it come back?), then price and promotion as the levers that
clear stock, then range (lines to exit or return). Availability drops to a check:
a line that was out of stock holds nothing to free.

## Options and what has to be true

| Cause | Option | Works if |
| --- | --- | --- |
| Availability | Fix supply on the lines that were out | The lost weeks were supply, not demand; stock can arrive in time |
| Range | Find successors for lines that left | Shoppers wanted the job the line did, not that exact line |
| Promotion | Restore the dropped promotions | Promo units were extra sales, not pulled forward |
| Competition | Close the price gap on top lines | Shoppers moved for price; the margin given up is less than the units won back |
| Demand | Buy and range to the lower level | The fall is lasting, not timing |
| Realisation | Fix what drives returns or cancellations | The leakage has a fixable cause |
| Any (freeing stock) | Clear lines with the most cover | Demand will not return before the stock ages |
