---
name: category-review
description: Runs a category review on retail sales, margin and stock data the user brings as a spreadsheet, CSV or pasted table. Builds a scorecard (sales, units, gross margin, GMROI, availability) against a comparison period, separates a demand problem from an execution problem, reads the range and promotions, and recommends next steps that fit the category's role. Use when someone asks to "review this category", "how is this category performing", "why is this category down", "is this category earning its keep", "which lines should we cut", "range review", "category health check", "GMROI", "margin versus turns", or "what should we do with this category". Works without any connected system; all figures come from the data supplied.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: general
---

# Category review

Read a category's performance from the user's own data and say what to do
about it. The output is decision support for a buyer or category manager,
not a verdict: every figure is shown as a calculation, and anything the data
cannot settle is named as unknown.

The principles behind each step are in
[references/principles.md](references/principles.md). Read it before the
first review in a session.

## Data you need

One row per product per period. Column names vary; map them and say how.

| Column | Needed for | Required? |
| --- | --- | --- |
| Product ID (SKU) and description | everything | yes |
| Category, subcategory | grouping | yes |
| Period (week or month) | trend, comparison | yes |
| Units sold | volume, rate of sale | yes |
| Sales revenue | everything | yes |
| Cost of goods sold, or unit cost | gross margin | strongly recommended |
| Same figures for a comparison period (same weeks last year, or prior period) | trend | strongly recommended |
| Stock on hand at cost (average, or opening and closing) | GMROI, turns | recommended |
| Days in stock, or an out-of-stock flag per period | demand vs execution | recommended |
| Promotional units or revenue, or a promo flag | base vs promoted | optional |
| Lifecycle (core, seasonal, discontinued) and whether it can be reordered | clearance logic | optional |
| Customer or basket counts | buyers, frequency, spend per trip | optional |

Also ask for two things the data cannot hold: the **category role** (what the
category is for: destination, routine, occasional or seasonal, convenience)
and the **store's positioning** (price leader, mainstream, premium,
specialist). If the user does not know, propose a role from the data (see
step 1) and mark it as a proposal.

## Missing data: what changes

| Missing | Do this | Do not |
| --- | --- | --- |
| Cost | Report sales and units only; say margin is unknown | Assume a typical margin % |
| Comparison period | Report shares, mix and ratios; no trend claims | Call a figure "down" or "up" |
| Stock | Skip GMROI and turns | Estimate stock from sales |
| Availability | Label any decline "cause unconfirmed" | Call a sales drop a demand drop |
| Basket or customer data | Use stockout windows as the substitution read | Claim where lost demand went |
| Tax basis unclear or mixed | Ask, or normalise every figure to ex tax (ex GST in Australia) | Compare inc-tax with ex-tax figures |
| Some stores or channels absent | State the coverage on every headline | Present a partial as the whole |

A blank cell is unknown, not zero. Returns booked as negative units should be
netted deliberately and the treatment stated.

## Steps

1. **Frame it.** State the period, the comparison period, currency, tax basis
   and coverage. A year-on-year comparison should match weekdays (the same
   weeks 364 days earlier), not calendar dates. Confirm or propose the role:
   high penetration and frequency suggest routine or destination; sales
   concentrated in a few weeks suggest seasonal; low share of sales with high
   margin suggests convenience. A high-volume category is not a destination
   unless the store actually differentiates in it.
2. **Clean.** Remove duplicate rows, separate promotional from base sales if
   flagged, and list rows dropped and why.
3. **Scorecard.** For the category and each subcategory: sales, units, GM$,
   GM%, change vs comparison, share of category. Sales and GM$ changes are
   percentages; GM% changes are percentage points. Read sales growth with GM$
   growth: sales bought with margin are not progress.
4. **Demand or execution.** Before treating any decline as weak demand, check
   availability. Low sales with poor in-stock is an execution problem: fix the
   shelf, not the plan. Low sales while fully stocked is a demand problem;
   decompose it into price, volume and mix, or with basket data into buyers ×
   trips per buyer × spend per trip, because each points to a different fix.
   Periods when a line was out of stock understate its demand; treat them as
   censored, not as low demand.
5. **Return on stock.** Calculate GMROI and turns per subcategory and for lines
   holding the most stock. Gross margin % alone misleads: a high-margin line
   that sits on the shelf can return less than a thin-margin fast mover. Only
   compare within like formats (a slow structural category should not be
   benchmarked against a fast-turning one). In supplier-funded or
   just-in-time categories, owned stock is thin and GMROI separates little.
6. **Range.** Rank lines by sales, calculate cumulative share, and identify the
   tail. A slow line is a candidate to cut only after asking what it does for
   the trip (is it the only option for a need or a loyal group?) and where its
   buyers would go. Score a cut on category profit after substitution, not on
   the line's own sales. Past out-of-stock periods give a first read on
   substitution; a permanent delist loses more than a stockout did.
7. **Promotions.** Compare base and promoted sales. In categories that are
   promoted most of the time, promoted sales are real demand; do not discount
   them. Elsewhere, check whether a promotion grew the category or moved
   shoppers from a larger pack or a dearer line, and look for a post-promotion
   dip (pull-forward).
8. **Price.** If the review touches price, weigh cost, competitor prices and
   what shoppers value together; a price defended on one of these alone is
   incomplete. Stock that cannot be reordered or returned (end of season,
   discontinued) is priced to recover the most revenue, not to protect a cost
   that is already spent.
9. **Recommend.** Tie each action to the role and positioning. Say what it
   costs or risks, who would decide, and how to tell in four to eight weeks
   whether it worked. Any modelled uplift is a range with its assumptions, not
   a single number.

## Formulas

- Gross margin $ (GM$) = revenue − cost of goods sold
- GM% = GM$ ÷ revenue
- Change % = (this period − comparison) ÷ comparison
- Margin change (points) = GM% this period − GM% comparison
- GMROI = annualised GM$ ÷ average stock at cost
  (annualise a 13-week figure by × 52 ÷ 13 = × 4)
- Stock turns = annualised cost of goods sold ÷ average stock at cost
- Rate of sale while in stock = units ÷ share of days in stock
- Sales lost to availability (upper bound) = rate of sale while in stock ×
  normal in-stock share − actual sales
- Share of category = line revenue ÷ category revenue

## Worked example

Thirteen weeks, ex GST, all stores, against the same 13 weeks last year.

| Line | Revenue | COGS | GM$ | GM% | Avg stock at cost | In stock | Revenue LY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 40,000 | 26,000 | 14,000 | 35.0% | 6,000 | 98% | 41,000 |
| B | 25,000 | 15,000 | 10,000 | 40.0% | 12,000 | 97% | 24,000 |
| C | 12,000 | 9,000 | 3,000 | 25.0% | 1,500 | 71% (LY 97%) | 19,000 |
| D | 3,000 | 1,500 | 1,500 | 50.0% | 4,000 | 99% | 4,000 |
| Total | 80,000 | 51,500 | 28,500 | 35.6% | 23,500 | | 88,000 |

- Sales change: (80,000 − 88,000) ÷ 88,000 = −9.1%.
- GM% last year was 31,000 ÷ 88,000 = 35.2%; now 28,500 ÷ 80,000 = 35.6%;
  change 35.6 − 35.2 = +0.4 points.
- Line C accounts for 19,000 − 12,000 = 7,000 of the 8,000 decline, and its
  in-stock fell from 97% to 71%.
- C's rate of sale while in stock: 12,000 ÷ 0.71 = 16,901. At last year's
  97% availability: 16,901 × 0.97 = 16,394. Upper bound on sales lost to
  availability: 16,394 − 12,000 = 4,394, or 4,394 ÷ 8,000 = 55% of the
  decline. Last year's in-stock rate was 19,000 ÷ 0.97 = 19,588, so C's
  in-stock rate of sale is also down (16,901 − 19,588) ÷ 19,588 = −13.7%:
  part execution, part demand.
- GMROI (× 4 to annualise): A 56,000 ÷ 6,000 = 9.33; B 40,000 ÷ 12,000 =
  3.33; C 12,000 ÷ 1,500 = 8.00; D 6,000 ÷ 4,000 = 1.50; category
  114,000 ÷ 23,500 = 4.85. D has the best GM% and the worst return on stock.
- D's share of category sales: 3,000 ÷ 80,000 = 3.8%.

**Reading:** the decline is mostly an availability failure on C, with a
smaller real drop in C's demand. Fix C's supply first. D ties up 4,000 of
stock at cost for 1,500 of GM$ a quarter; cut its stock depth before
considering a delist, and only delist if its buyers would move to B.

## Answer shape

1. **Answer first.** Two or three sentences: how the category is doing, the
   main reason, and the action.
2. **Evidence.** The scorecard table, then each derived figure as a
   calculation (inputs → result), with period, tax basis and coverage stated.
3. **Unknowns.** What the data could not settle, the assumptions made (role,
   annualisation, treatment of returns), and what data would close each gap.
4. **Next steps.** Ranked actions, each with its owner type, cost or risk,
   and the measure that shows whether it worked.

Keep the language plain. Say "we cannot tell from this data" rather than
guessing.

## With Twelfth connected

When the user's workspace is connected to Twelfth (twelfth.ai) over MCP, the
spreadsheet is not needed:

- `twelfth_list_category_settings` maps category names to IDs and owners.
- `twelfth_list_products` replaces the product table: stock, velocity, cover,
  sales, GP%, price and supplier per product, filterable by category.
- `get_entity_profile` reads every measure for one named category, brand,
  supplier or product.
- `get_methodology` returns the full category-management playbook for the
  situation (slow sales, stock pressure, ranging, pricing) to ground the
  recommendation.
- `recall_decisions` shows what was decided about this category before, and
  why.
- `price_intel_summary` supplies the competitor price index for step 8.
