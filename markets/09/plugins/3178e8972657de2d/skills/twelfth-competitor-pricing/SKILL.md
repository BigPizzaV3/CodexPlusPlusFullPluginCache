---
name: twelfth-competitor-pricing
description: Answer competitor pricing questions from a Twelfth workspace using the Twelfth MCP pricing tools - where we sit against each competitor, which SKUs a competitor undercuts, how a tracked set reads, what moved this week, when and how one SKU's price changed, and which of our SKUs a retailer's product page is. Reads observed prices on a last-seen or 4/8/12-week basis and flags likely listing errors and pack mismatches. Use when someone asks "are we competitive on X", "who is cheaper", "check competitor prices", "what did competitors do this week", "price index", "review my tracked set", "when did they drop the price" or shares a retailer's product page. Needs the Twelfth MCP server connected.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: twelfth
  requires: pricing
---

# Competitor pricing with Twelfth

Twelfth tracks a workspace's SKUs against approved competitor retailers and
records what each listing showed, day by day. These tools read those
observations. They never fetch a price live and never change one.

For first-time setup and general workspace questions, see the
`twelfth-workspace` skill.

## Before you start

- Call `twelfth_get_workspace` for the currency and timezone. Quote prices in
  that currency and as-of times in that timezone.
- **The tool list varies by workspace and connection.** Use what is offered and
  say which tool is missing if a step needs it.
- **Empty can mean no access.** A connection reads only its remits. A set marked
  `scopedOut`, or a SKU returned as `not_readable_or_not_tracked`, is outside
  this connection's reach or not tracked; say that, not "no competitor sells it".

## Pick the tool by question

| Question | Route |
| --- | --- |
| Where do we sit overall, per competitor? | `price_intel_summary` (window 4, 8 or 12 weeks) |
| What moved in the market this week? | `price_intel_observations` |
| Which SKUs is a competitor undercutting? | `price_intel_lookup` with `over_index` (e.g. 105), plus `retailer` or `category` |
| How does my saved set read? | `twelfth_list_tracked_sets` → `twelfth_get_tracked_set` (page with `limit`/`offset`) |
| Compare these named SKUs | `twelfth_list_pricing_retailers` → `twelfth_compare_pricing_skus` (1 to 8 SKUs) |
| When and how did the price move? | `price_intel_history` (default 90 days, up to 365) |
| Which of our SKUs is this retailer page? | `twelfth_match_pricing_page` with GTIN, retailer SKU or exact URL |
| I only have a product name | `price_intel_lookup` with `query`, or `search_catalogue` |

Typical flows:

- **Set review:** list sets → read the set (window 4) → pick SKUs with an index
  above the person's threshold (5% dearer if none given) → compare them by name →
  history for the ones that moved.
- **Spot check:** compare SKUs → for any competitor more than 5% below us, read
  history to see if it is a new move, a promotion or a long-standing gap.
- **From a product page:** match the page → compare that SKU → history.

Use the exact identity a tool returns. If a name resolves to several SKUs, ask
which.

## Read the basis before the number

Every competitor price is on one of two bases, and they answer different
questions:

- **Last seen** (`window: "live"`, `basis: "live"`, `priceBasis: last_observed`):
  the most recent price observed for that listing. It is what a shopper last saw,
  not a live lookup. Call it "last seen on <date>", never "current" or "today's".
- **Rolling average** (window 4, 8 or 12 weeks): the mean over the window. The
  index is built on this, and it is the fairer read of where a competitor sits.

State the basis with every figure. Never compare a last-seen price with an
average, or our average with their last seen.

**Index** = our price ÷ their price × 100. 100 is parity; 105 means we are 5%
dearer; 95 means we are 5% cheaper. **Gap %** = (ours − theirs) ÷ theirs.

## Before calling it a price cut

A low competitor price is not always a move to respond to. Check:

- **Listing error.** One retailer far below (less than half, or more than double)
  while the other retailers agree with each other is more likely a mistake than
  a promotion. A deep cut that other retailers follow is real.
- **One observation.** A single day's low price is one reading. Look for it
  holding two or more days in `price_intel_history`.
- **Pack or variant mismatch.** A listing for a multi-pack priced like a single,
  or the reverse. A number at the end of a part code is often a specification,
  not a pack size.
- **Stock state.** A cheap price on an out-of-stock listing does not take sales.
- **Match state.** `matched_without_price` and `unmatched` are not prices.
  Leave them out of the cheapest-competitor figure and say how many there were.

Detail and examples are in `references/reading-price-data.md`.

## Answer shape

1. **Answer first.** For example: "We are dearer than the cheapest competitor on
   3 of 8 SKUs by more than 5%; the largest gap is 12% on <SKU>."
2. **Table.** SKU, product, our price, cheapest competitor, their price, gap %,
   their stock, basis, as of.
3. **Evidence.** Which tool, which set or SKUs, which window, the `asOf` time.
4. **Unknowns.** Unmatched or unpriced retailers, SKUs not readable, suspected
   listing errors, mismatched packs.
5. **Next steps.** Which SKUs need a pricing decision and why, which need a
   match checked, which are noise.

Report only this workspace's own data. Do not speculate about how a competitor
sets prices.

## Making changes

No tool changes a price. Price changes are made in the Twelfth app; say so when
asked to reprice.

If the person ticked **Allow changes**, and only when they ask:
`twelfth_create_action` logs a follow-up (for example "review price on <SKU>").
`twelfth_complete_action` on a price review task closes it as reviewed; it does
not change the price. Never claim a change no tool made.

More: https://twelfth.ai/developers/mcp
