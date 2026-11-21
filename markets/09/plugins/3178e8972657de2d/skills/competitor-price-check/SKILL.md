---
name: competitor-price-check
description: Compares a retailer's prices with competitors' using a price list and competitor prices the user brings as a spreadsheet, CSV or pasted table. Matches identical products, normalises pack sizes, separates shelf, promotional and member prices, sets aside marketplace sellers, out-of-stock rows, stale observations and likely listing errors, calculates a weighted price index, and recommends match, hold or ignore per line by KVI status and category role. Use when someone asks "are we competitive", "check our prices against a competitor", "a competitor has undercut us", "what is our price index", "should we match this price", "where are we too expensive", "KVI price check" or "is this competitor price real". Works without any connected system; all figures come from the data supplied.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: general
---

# Competitor price check

Compare our prices with competitors' on identical products, measure the gap
as an index, and say which gaps deserve a response. Most wrong answers in
price comparison come from bad inputs (a lookalike product, a twin pack, a
member-only price, a typo on a competitor's site) rather than bad arithmetic,
so the checks come before the index.

The detail behind each check, with examples, is in
[references/data-quality.md](references/data-quality.md).

## Data you need

**Our lines**

| Column | Required? |
| --- | --- |
| SKU, description, brand | yes |
| GTIN (barcode) or manufacturer part number | yes, for matching |
| Pack size and unit of measure | yes |
| Our shelf price (and promo price, if any) | yes |
| Units sold or revenue over a recent period (the weight) | yes, for an index |
| Unit cost | for a match decision |
| KVI flag (a known-value item shoppers price-check) and category role | for a recommendation |

**Competitor observations**, one row per product per retailer per date

| Column | Required? |
| --- | --- |
| Retailer, product title, and GTIN or part number | yes |
| Pack size | yes |
| Observed price and its type: shelf, promo, member or loyalty, clearance | yes |
| Observation date | yes |
| Seller: the retailer itself or a third-party marketplace seller | recommended |
| In stock or out of stock | recommended |
| Was-price or promo end date | optional |

If a column is missing, keep going and say what it costs: no observation date
means every price is "last seen, date unknown"; no seller column means
marketplace listings may be in the index; no stock flag means the index may
include prices nobody can buy at; no weights means an unweighted index, which
lets a slow line move the result as much as a best seller.

## Steps

1. **Match identical products only.** Match on GTIN. Without one, use brand
   plus manufacturer part number. A similar title is a candidate for a person
   to confirm, never a match. Different size, colour, model year, variant or
   bundle is a different product. Report the match rate per competitor:
   matched lines ÷ our lines.
2. **Normalise pack sizes.** Compare price per unit of measure when packs
   differ, and say so. Read pack size from an explicit statement ("pack of
   24", "24 pack", "x24", a quantity field). A trailing number in a part
   number is usually a specification (a size, a gap, a rating), not a pack
   count. Bundles and gift-with-purchase offers are excluded unless the user
   wants them priced.
3. **Separate price types.** The default comparison is shelf price against
   shelf price: the price anyone pays at checkout. Promotional prices are
   compared with a note of when they end. Member or loyalty prices are
   reported separately and never mixed with shelf prices on the other side.
4. **Set aside rows that are not competing.** Exclude from the index:
   out-of-stock rows, third-party marketplace sellers (report them on their
   own line), parallel imports where the listing says so ("international
   version", "no local warranty"), and observations older than the user's
   freshness limit (default 7 days for fast-moving lines).
5. **Flag likely listing errors.** A price is suspect when the other
   retailers agree with each other (all within 25% of their median) and this
   one sits below half or above double that median. It needs at least two
   other retailers and the price holding on at least two observations before
   it counts as real. Size alone is not the test: a deep cut that the rest of
   the market also shows is genuine.
6. **State the basis.** Say whether each competitor price is the last one
   seen (with its date) or an average over a window (4, 8 or 12 weeks). A
   last-seen price is the latest observation, not a live price; never call it
   "today's price". Do not compare a figure on one basis with a figure on the
   other.
7. **Calculate the index** (below), per line and per competitor, on lines that
   survived steps 1 to 6.
8. **Recommend** match, hold or ignore per line (below).

## Price index

Index = our price ÷ competitor price. 1.00 (or 100) is parity; above 1.00
means we are dearer. Some teams invert this; state the convention.

- **Per line:** our price ÷ competitor price.
- **Category or basket, units-weighted (preferred):**
  Σ(units × our price) ÷ Σ(units × competitor price). This is what the same
  basket costs at each retailer.
- **Revenue-weighted alternative:** Σ(our revenue × line index) ÷ Σ(our
  revenue).
- **Coverage:** an index covers only the lines matched at that competitor.
  Two competitors' indices over different lines are not comparable; for a
  head-to-head, use lines matched at both.

## Worked example

Four lines, four weeks of our unit sales as weights, shelf prices last seen
within 2 days, all first-party sellers.

| Line | Our price | Units | Unit cost | KVI | Competitor X | Competitor Y |
| --- | --- | --- | --- | --- | --- | --- |
| A | 49.00 | 300 | 30.00 | yes | 45.00 | 47.00 |
| B | 19.95 | 500 | 11.00 | no | 19.95 | 36.00 for a twin pack |
| C | 12.00 | 200 | 7.00 | no | 12.50 | 13.00 shelf, 9.00 member |
| D | 25.00 | 100 | 15.00 | no | 24.00, out of stock | 23.50 |

Adjustments: Y's line B is 36.00 ÷ 2 = 18.00 per unit. Y's line C uses the
13.00 shelf price; the 9.00 member price is reported separately. X's line D
is out of stock and excluded.

- **Index vs X** (lines A, B, C):
  ours 300 × 49.00 + 500 × 19.95 + 200 × 12.00 = 14,700 + 9,975 + 2,400 =
  27,075; X 300 × 45.00 + 500 × 19.95 + 200 × 12.50 = 13,500 + 9,975 + 2,500
  = 25,975; index 27,075 ÷ 25,975 = 1.042. We are 4.2% dearer.
- **Index vs Y** (lines A to D):
  ours 27,075 + 100 × 25.00 = 29,575; Y 300 × 47.00 + 500 × 18.00 +
  200 × 13.00 + 100 × 23.50 = 14,100 + 9,000 + 2,600 + 2,350 = 28,050; index
  29,575 ÷ 28,050 = 1.054. On the three lines both carry: 27,075 ÷ 25,700 =
  1.054.
- **Line A** vs X: 49.00 ÷ 45.00 = 1.089, a gap of 4.00. Matching cuts unit
  margin from 49.00 − 30.00 = 19.00 to 45.00 − 30.00 = 15.00. To hold GM$
  of 300 × 19.00 = 5,700, units must reach 5,700 ÷ 15.00 = 380, an uplift of
  19.00 ÷ 15.00 − 1 = 26.7%.

**Reading:** A is a KVI and both competitors sit below us (47.00 ÷ 45.00
shows they are within 4.4% of each other), so the gap is likely real.
Check X's price history: if 45.00 is a promotion ending this week, hold;
if it has held for weeks, close the gap, accepting that it needs about 27%
more units to break even on GM$. B's gap against Y exists only for
shoppers buying two: hold. C is cheaper than both on shelf (12.00 ÷ 12.50 =
0.96); Y's member price is a loyalty decision, not a shelf one. D is a
non-KVI 6.4% dearer than Y (25.00 ÷ 23.50 = 1.064): hold.

## Match, hold or ignore

| Situation | Response |
| --- | --- |
| KVI in a destination or routine category, gap beyond the user's band (default 3%), clean evidence (identical product, shelf price, in stock, first-party, recent, confirmed by a second retailer or held for weeks) | **Match** or close the gap, after the contribution check |
| Same, but the competitor price is a promotion ending soon | **Hold** and recheck after it ends |
| Non-KVI or tail line with a gap | **Hold** unless the gap is large and sustained on the 4-week average; tail margin pays for KVI investment |
| Evidence is weak: single observation, member-only, marketplace seller, stale, out of stock, pack mismatch, suspected listing error | **Ignore** for pricing; flag for a check |
| We are much cheaper than the whole market on a non-KVI | Consider a **rise**; check volume after |

Contribution check before any match: break-even uplift = current unit margin
÷ new unit margin − 1. Never recommend a price below unit cost on a line that
is reordered, and keep any automated repricing inside floors and ceilings.
Competitor prices are one input; cost and what shoppers value matter too.

## Answer shape

1. **Answer first.** Where we sit (index per competitor, with coverage) and
   the two or three lines that need a decision.
2. **Evidence.** Line table with the basis and date of each price, and every
   index or margin figure as a calculation.
3. **Unknowns.** Rows excluded and why (counts per reason), unmatched lines,
   assumptions about pack sizes or price types.
4. **Next steps.** Match, hold or ignore per flagged line, with the
   contribution check and what to recheck and when.

## With Twelfth connected

When the user's workspace is connected to Twelfth (twelfth.ai) over MCP,
competitor prices are already matched and collected:

- `price_intel_summary` gives the whole-market index over 4, 8 or 12 weeks
  and the tracked competitors.
- `twelfth_list_tracked_sets` and `twelfth_get_tracked_set` read a saved set
  of products with competitor prices, on a last-seen or 4/8/12-week basis.
- `twelfth_compare_pricing_skus` compares up to 8 named SKUs with gaps, match
  and stock states.
- `price_intel_lookup` finds SKUs a competitor undercuts.
- `price_intel_history` shows daily price and stock for one SKU, to tell a
  held cut from a short promotion or a listing error.
- `price_intel_observations` lists this week's competitor moves.
- `get_methodology` returns the pricing principles for the recommendation.
