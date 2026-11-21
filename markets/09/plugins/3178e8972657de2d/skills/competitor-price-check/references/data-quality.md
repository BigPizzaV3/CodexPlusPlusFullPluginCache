# Competitor price data: checks before the index

Each check below catches an input that produces a confident, wrong answer.
Run them in order; record how many rows each removes.

## 1. Identity: the same product, not a lookalike

- **GTIN first.** The barcode identifies the exact product, size and variant.
- **Brand plus manufacturer part number** is the fallback. Part numbers are
  reused across brands, so never match on part number alone.
- **Titles only suggest.** "Similar" products differ in size, colour, model
  year, region, pack count or included accessories. A title match is a
  candidate for a person to confirm.
- **Report the match rate.** An index on 40% of the range describes 40% of
  the range. Say which lines it covers.

## 2. Pack size and bundles

- Compare per unit of measure (per item, per 100 g, per litre) when pack
  sizes differ, and say the comparison is normalised. A twin pack at a lower
  unit price is a different offer: a shopper must buy two.
- **Read pack counts from explicit wording**: "pack of 24", "24 pack",
  "box of 24", "x24", or a quantity field. Do not infer a pack count from a
  number at the end of a part number. In practice that suffix is usually a
  specification: an electrode gap, an opening temperature, a volume, a size.
  When unsure, leave pack size unknown and exclude the row, rather than guess:
  a wrong pack size breaks a correct match.
- A listing that names a multi-pack but charges the single-unit price is
  usually a listing error on the competitor's side (see check 5), not a
  bargain to match.
- Bundles and gift-with-purchase offers are excluded unless the user asks to
  price the bundle.

## 3. Price types

| Type | What it is | How to use it |
| --- | --- | --- |
| Shelf | The price anyone pays at checkout without signing up | Default basis for the index |
| Promo | A temporary reduction, often with a was-price | Compare, noting the end date if known |
| Member or loyalty | A price available only to members of a scheme | Report separately; compare only with our own member price |
| Clearance | Run-out stock | Usually ignore for pricing; it will not last |

- Member prices are often gated or published unevenly. Some retailers show
  member offers only at certain times of day or rotate them overnight, so an
  observation taken at an off time can show no member price. A missing member
  price is not proof the offer ended; check when the observation was taken.
- Never compare our shelf price with their member price, or the reverse,
  without saying so.

## 4. Who is selling, and can you buy it

- **Marketplace sellers.** Third-party sellers on a retailer's marketplace
  set their own prices and often sit far below the retailer's own listing.
  Exclude them from the retailer's index and report them on a separate line.
- **Parallel imports.** Exclude listings that declare themselves grey stock
  ("international version", "no local warranty", "parallel import"). Being a
  marketplace seller alone does not make a listing grey.
- **Out of stock.** A price nobody can buy at is not competing. Exclude
  out-of-stock rows from the index; their last-seen price can be shown for
  reference.

## 5. Listing errors versus genuine cuts

A competitor's typo can look exactly like an aggressive price cut. Matching a
typo is the worst response, so test before reporting a cut.

A price is a **suspected listing error** when all of these hold:

1. at least two other retailers price the same product on the same day;
2. those others agree: every one within 25% of their median;
3. this price sits below 0.5 × or above 2 × that median.

Example: three retailers at 40.00, 41.50 and 42.00 (median 41.50; range
42.00 − 40.00 = 2.00, which is 2.00 ÷ 41.50 = 4.8% of the median, so they
agree). A fourth at 4.20 is 4.20 ÷ 41.50 = 0.10 × the median, well below
0.5 ×: suspected error. Do not match; recheck in a day or two.

Rules:

- **Magnitude is not the test.** Clearance at 70% off is legitimate. If the
  rest of the market moves with the cut, it is real.
- **A dispersed market proves nothing.** When competitors sit at 40.00,
  95.00 and 150.00, the cheapest is simply the cheapest.
- **One observation is not a fact.** Require the price to hold across at
  least two observations before treating any large move as real.
- **Keep suspect prices out of baselines too.** If a suspect price sits in
  last week's average, the return to normal will look like a price rise.

## 6. Freshness and basis

- **Last seen** is the most recent observation of that listing. It is not a
  live lookup and may be days old. State its date.
- **Window average** (4, 8 or 12 weeks) smooths short promotions and is the
  fairer read of where a competitor usually sits. It is the better basis for
  an index; last seen is better for "what is a shopper seeing".
- Never put a figure on one basis beside a figure on the other without
  labelling both.
- Set a freshness limit with the user (default 7 days for fast-moving lines)
  and exclude older rows from a last-seen index.

## 7. Collected data can be complete and still wrong

A full set of prices is not the same as a correct set. Before relying on a
newly collected source, look at the price distribution: count rows under
2.00, 2.00 to 10.00, 10.00 to 50.00 and over 50.00. If a premium range shows
mostly prices under 2.00, the collection picked up a quantity or a code, not a
price. Spot-check a dozen prices against the retailer's own page.

## 8. Not found is not exclusive

A product not found at a competitor has three possible states: **matched**,
**not found after a complete search of that retailer**, and **not assessed**.
Only the second supports "we are the only seller". A partial search supports
nothing; report it as not assessed.
