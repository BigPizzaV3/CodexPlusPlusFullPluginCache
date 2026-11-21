# Estimating where a cut line's buyers go

When a line leaves the range, each of its buyers does one of three things:
buys another line you still carry, buys something else entirely in your store,
or buys it elsewhere (or not at all). Only the first is recovered for the
category. The share that switches decides whether a cut gains or loses money.

## Sources of evidence, best first

1. **Past out-of-stock windows.** When the line was unavailable for a few weeks,
   how much did its neighbours gain?

   ```
   Weekly units lost while out = cut line's normal weekly units
   Neighbour gain              = neighbour's weekly units during the gap - its normal weekly units
   Switching share to that neighbour = neighbour gain / weekly units lost
   ```

   Use windows of at least two weeks, outside promotions on either line, and
   compare against the same neighbour's normal rate (the weeks either side, or
   the same weeks last year). Treat the result as the most you could hope to
   recover: during a temporary gap shoppers know the line will come back, so a
   permanent delist loses more of them. An out-of-stock week also costs some
   whole trips, so the category's dip mixes lost switching with lost visits.

2. **Basket data.** If the cut line's buyers already buy a neighbour on other
   trips, they are more likely to switch to it. A line that is often the only
   item from the category in the basket is a walk-out risk.

3. **Close substitutes in the range.** Same need, similar size and price tier,
   different brand: switching tends to be high. Different tier or format, or a
   category where shoppers are loyal to one product: switching tends to be low.

4. **Judgement, as a range.** With none of the above, run a low and a high
   share (for example 20% and 60%). If the call is the same at both ends,
   proceed and say the share is assumed. If it flips, the decision rests on the
   share: say so, and propose a way to find out (a trial removal in a few
   stores, or waiting for the next stock-out).

## Rules for crediting a transfer

- The receiver must stay in the range. Credit given to a line that is also
  being cut is not real.
- The receiver needs the supply and the space to take the extra units. Check its
  cover and lead time against the added weekly units.
- Switching is not symmetric: buyers of A may move to B while buyers of B would
  not move to A.
- Cutting several lines in one need state removes second choices too. Cutting a
  whole need state loses far more than the same number of scattered lines.
- In categories with loyal buyers, or where the shopper came for that one item,
  expect more walking and less switching.
- Demand that walks to another retailer cannot be seen in your own data. Name
  that gap rather than guessing it.

## A worked transfer

Line C sells 1,040 units a year at $3.40 contribution per unit. It was out of
stock for 6 weeks last year. Its normal rate is 1,040 / 52 = 20 units a week.
During the gap, line B rose from 75 to 92 units a week.

```
Switching share to B (upper bound) = (92 - 75) / 20 = 0.85
Planning share                      = 0.75   (allowing for extra loss on a permanent cut)
Units moving to B                   = 0.75 x 1,040 = 780
Recovered contribution              = 780 x $4.80 (B's unit contribution) = $3,744
C's contribution                    = 1,040 x $3.40 = $3,536
Net annual effect of cutting C      = 3,744 - 3,536 = +$208
```

At the upper bound the gain is (0.85 x 1,040 x 4.80) - 3,536 = 4,243 - 3,536 =
+$707. The cut pays at any share above 3,536 / (1,040 x 4.80) = 0.71, so the
decision rests on whether at least 71% of C's buyers switch. The out-of-stock
evidence (0.85) clears that, with a modest margin.
