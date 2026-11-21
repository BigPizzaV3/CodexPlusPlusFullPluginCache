# Worked example: a category down 16.9%

A buyer says: "Sales in my category are down about 17% on last year for the
quarter. Why?" They share a CSV with one row per line per quarter, sales ex GST,
plus promotional units, returns, order counts and weeks in stock.

## The data

13 aligned weeks this year against the same 13 weeks last year, both ex GST.

| Line | Units LY | Price LY | Gross LY | Units TY | Price TY | Gross TY | Weeks in stock LY | Weeks in stock TY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | 1,000 | $20.00 | $20,000 | 800 | $19.00 | $15,200 | 13 | 10 |
| B | 400 | $50.00 | $20,000 | 380 | $50.00 | $19,000 | 13 | 13 |
| C | 600 | $10.00 | $6,000 | 0 | | $0 | 13 | (deleted) |
| D | 0 | | $0 | 400 | $12.00 | $4,800 | (new) | 13 |
| **Total** | **2,000** | | **$46,000** | **1,580** | | **$39,000** | | |

Other columns: returns $1,000 last year, $1,600 this year. Orders 1,600 last
year, 1,400 this year. Promotional units 400 last year, 380 this year. The rest
of the business fell 3% over the same weeks.

## Is the fall real?

Both periods are 13 complete, aligned weeks, same tax basis, no recoding
reported. The category fell well beyond the rest of the business (-3%), so it is
a category problem, not a whole-business one.

## Step 1: the split

```
Net LY  = 46,000 - 1,000 = 45,000
Net TY  = 39,000 - 1,600 = 37,400
Change in net sales = 37,400 - 45,000 = -7,600   (-7,600 / 45,000 = -16.9%)

P0 = 46,000 / 2,000 = $23.00 per unit

Units effect   = (1,580 - 2,000) x 23.00            = -9,660
Price effect   = A: (19.00 - 20.00) x 800 = -800
                 B: (50.00 - 50.00) x 380 =    0     = -800
Gross change   = 39,000 - 46,000                     = -7,000
Mix effect     = -7,000 - (-9,660) - (-800)          = +3,460
Realisation    = -(1,600 - 1,000)                    = -600

Check: -9,660 - 800 + 3,460 - 600 = -7,600  (matches the change)
```

Reading it: units carry more than the whole fall (-9,660 against -7,600). Mix
is positive (+3,460) because the cheapest line, C at $10.00, left and the units
that remain sit on dearer lines on average. Price (-800) is one line's $1
reduction. Realisation (-600) is small but real: returns rose from
1,000 / 46,000 = 2.2% of gross to 1,600 / 39,000 = 4.1%.

### Units split by orders and basket

```
Units per order LY = 2,000 / 1,600 = 1.25
Units per order TY = 1,580 / 1,400 = 1.1286

Orders effect = (1,400 - 1,600) x 1.25 x 23.00          = -250 units x 23.00 = -5,750
Basket effect = (1.1286 - 1.25) x 1,400 x 23.00         = -170 units x 23.00 = -3,910

Check: -5,750 + -3,910 = -9,660  (matches the units effect)
```

Both fell; fewer orders is the larger part.

## Step 2: locate it

Units change by line: A -200, B -20, C -600, D +400.
Check: -200 - 20 - 600 + 400 = -420 (matches 1,580 - 2,000).

The fall sits in a few lines (A, and C against D), so demand is unlikely to be
the main cause.

## Step 3 and 4: the causes

**Promotion: ruled out as the main cause.**
Base units LY = 2,000 - 400 = 1,600; TY = 1,580 - 380 = 1,200.
Base change = (1,200 - 1,600) / 1,600 = -25%. Promo change = (380 - 400) / 400 = -5%.
Base units fell far more than promotional units, so fewer promotions do not
explain it.

**Availability: supported on line A.**
A sold 1,000 / 13 = 76.9 units per in-stock week last year and 800 / 10 = 80.0
this year. In the weeks it was in stock it sold at last year's rate. Three weeks
out of stock at last year's rate is 3 x 76.9 = 231 units, more than A's 200-unit
fall. A's decline is consistent with the stock-outs, not with weaker demand.

**Range: supported.**
C (600 units) was deleted; D was launched and sold 400. Net range effect on
units = -600 + 400 = -200. Whether D took C's shoppers or found new ones is not
visible without basket data.

**Demand: a small part at most.**
B was in stock every week, not deleted, and its price did not change; it fell
(380 - 400) / 400 = -5%, close to the rest of the business at -3%. That fits a
mild market softening, about 20 units here.

**Competition and visibility: unknown.** No competitor prices or space data were
supplied.

## The answer

> The category is down $7,600 (-16.9%) on the same 13 weeks last year, ex GST,
> and it is a volume problem: units account for -$9,660, partly offset by a
> better price mix (+$3,460) after the $10 line C was deleted.
>
> Two things carry the lost units. Line A was out of stock for 3 of 13 weeks;
> when it was in stock it sold at last year's rate (80 a week against 77), and
> the lost weeks cover its whole 200-unit fall. And line C's deletion lost 600
> units that the new line D only partly replaced (400 units).
>
> Ruled out: promotions (base units fell 25%, promo units only 5%) and a large
> price effect (one $1 cut on A, -$800). Returns rose from 2.2% to 4.1% of gross
> (-$600), worth a look by line.
>
> Unknown: whether a competitor moved on A or B (no competitor prices), and
> whether space changed (no space data). Did any competitor cut price on these
> lines this quarter? Did the shelf or online listing change?
>
> Options: secure supply on A (works if the stock-outs were supply, not a
> forecast miss that will recur); look for a second successor to C (works if
> C's buyers wanted its price point, which D at $12 does not fully meet); check
> which line drives the returns (works if one faulty line explains them).
