# Reading competitor price data

## Listing errors look exactly like price cuts

A retailer that lists a product at the wrong price, and leaves it there for days,
produces the same pattern as a genuine cut: a large move that holds. The right
response to a cut (consider matching it) is the wrong response to a typo.

Size of the move does not separate them. Clearance at 70% off is real. What
separates them is whether the rest of the market agrees:

1. The **other retailers on the same product agree with each other** (their
   prices sit close together), and
2. this one retailer sits **far outside** them: below half or above double their
   typical price.

Both must hold. In a spread-out market (say $40, $95 and $150) the cheapest is
simply the cheapest, not an error. You need at least two other retailers for
"they agree" to mean anything, and at least two days of the odd price for it to
be more than a single reading.

When a price looks like an error, say so with the evidence (the peer prices and
dates) and recommend checking the listing before acting. If other retailers move
with it over the following days, it is a real market move.

A suspect low price also distorts averages. If the 4-week average dropped
because of it, the later return to normal can read as a price rise. Check
`price_intel_history` before reporting a rise straight after a suspected error.

## Pack sizes and part codes

A listing for a box of 24 priced like a single unit is a common retailer
mistake, and the reverse (a single matched to a multi-pack) is a common matching
mistake. Either makes the gap meaningless.

A trailing number in a part code (`XYZ100-24`) is not reliably a pack size. In
many ranges it is a specification: a gap in millimetres, a temperature, a volume.
Only an explicit phrase ("box of 24", "2 pack", "twin pack") or a pack field
establishes pack size. If the titles on each side suggest different packs, flag
the comparison as unsafe rather than computing a per-unit price from a guess.

## Basis

- **Last seen** is the latest observation for that listing, which may be days
  old. Give its date.
- **4/8/12-week average** smooths promotions and errors and is the basis of the
  index. It lags a recent move.
- When a person asks "what is their price now", give last seen with its date, and
  say a live check is on the retailer's site.
- When a person asks "where do we sit", use the average and the index.

## Other things that change the read

- **Stock.** An out-of-stock competitor at a low price is not taking sales today.
- **Marketplace sellers.** A third-party seller on a retailer's marketplace is
  not the retailer's own price. Name the seller where the tool returns it.
- **Member or club prices.** Some retailers show a members-only price. Check
  whether the observation is the member or the public price before comparing.
- **Promotions.** A price that drops for a week and returns is a promotion. Read
  the history before calling it a permanent repositioning.
- **Match status.** `matched_without_price` means the listing was found but no
  price was read; `unmatched` means no listing is matched. Neither is a price.

## Worked example

`twelfth_compare_pricing_skus` (window 4, as of 19 Oct 2026 08:00 AEDT) returns
our price $49.95, Retailer A $46.00, Retailer B $47.50, Retailer C $19.95, all in
stock.

- A and B agree (within about 3% of each other). C is below half their typical
  price.
- `price_intel_history` shows C at $19.95 for 2 days, previously $47.95.
- Read: C is likely a listing error. Gap to the agreeing market is 5% to 9%
  ($49.95 vs $46.00 to $47.50). Recommend checking C's listing and reviewing
  against A, not matching C.
