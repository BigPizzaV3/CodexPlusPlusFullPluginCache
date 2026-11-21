# Worked example: a six-line range review

A buyer shares a 52-week export for a small household category and asks: "Which
of these should I cut? The supplier of A and B also wants us to add their new 2L
everyday line." All figures are ex GST. Every line was ranged in 20 stores and in
stock all 52 weeks. It is January.

The buyer confirms the category is a routine one (bought often, price-checked)
and that the aim is profit.

## The data and the scores

```
ROS              = units / (20 stores x 52 weeks) = units / 1,040
Unit contribution = price - unit cost
Contribution      = units x unit contribution
Return on stock   = contribution / average stock at cost
```

| Line | Need state | Units | Price | Unit cost | Unit contr. | Sales | Contribution | Margin % | Avg stock at cost | Return on stock | ROS | Trend (13 wk vs prior 13) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A Everyday 500ml | Everyday | 5,200 | $8.00 | $4.80 | $3.20 | $41,600 | $16,640 | 40.0% | $2,400 | 6.93 | 5.00 | 1.02 |
| B Everyday 1L | Everyday | 3,900 | $12.00 | $7.20 | $4.80 | $46,800 | $18,720 | 40.0% | $2,700 | 6.93 | 3.75 | 1.05 |
| C Everyday 1L, second brand | Everyday | 1,040 | $11.50 | $8.10 | $3.40 | $11,960 | $3,536 | 29.6% | $2,250 | 1.57 | 1.00 | 0.80 |
| D Premium 500ml | Premium | 1,560 | $18.00 | $9.00 | $9.00 | $28,080 | $14,040 | 50.0% | $3,000 | 4.68 | 1.50 | 1.10 |
| E Premium 1L | Premium | 520 | $26.00 | $14.30 | $11.70 | $13,520 | $6,084 | 45.0% | $3,900 | 1.56 | 0.50 | 0.95 |
| F Gift set | Gifting | 260 | $40.00 | $22.00 | $18.00 | $10,400 | $4,680 | 45.0% | $4,400 | 1.06 | 0.25 | seasonal |
| **Category** | | | | | | **$152,360** | **$63,700** | 41.8% | **$18,650** | **3.42** | | |

Sample calculations: C contribution = 1,040 x (11.50 - 8.10) = 1,040 x 3.40 =
$3,536; C margin = 3,536 / 11,960 = 29.6%; C return on stock = 3,536 / 2,250 =
1.57. Category return on stock = 63,700 / 18,650 = 3.42. Category margin =
63,700 / 152,360 = 41.8%.

## What a naive rule would do

"Cut the bottom three by sales" removes F, C and E: 10,400 + 11,960 + 13,520 =
$35,880, or 35,880 / 152,360 = 23.5% of sales. It would delete the only gifting
line and half the premium range. The steps below reach a different answer.

## Gates

- **F** is the only line in gifting, and 60% of its units sell in November and
  December. Protected; judge it as a seasonal line.
- No line is a known traffic driver or price-checked line beyond A and B, which
  are strong anyway.

## Flags

Within each need state, weak on rate of sale, trend and contribution together:

- **C** (everyday): ROS 1.00 against 5.00 and 3.75, trend 0.80, lowest
  contribution and margin in the category. Flagged.
- **E** (premium): ROS 0.50 against D's 1.50, trend 0.95, but contribution of
  $6,084 is the fourth highest. Flagged for review, mainly on its 1.56 return on
  stock.

## Where would their buyers go?

**C.** It was out of stock for 6 weeks last year, and B rose from 75 to 92 units a
week while it was out. Switching share to B, upper bound = (92 - 75) / 20 = 0.85
(C's normal rate is 1,040 / 52 = 20 a week). Planning share 0.75.

```
Recovered = 0.75 x 1,040 x $4.80 = 780 x 4.80 = $3,744
Lost      = $3,536
Net       = 3,744 - 3,536 = +$208 a year
Break-even share = 3,536 / (1,040 x 4.80) = 0.71
```

Cutting C adds a little contribution before the freed slot is even reused,
because its buyers move to a line that earns $1.40 more per unit. B must carry
780 / 52 = 15 more units a week (75 to 90): check B's cover and lead time.

**E.** No out-of-stock history. Run a low and high share of buyers moving to D:

```
30%: 0.30 x 520 x $9.00 = 156 x 9.00 = $1,404 recovered; net 1,404 - 6,084 = -$4,680
60%: 0.60 x 520 x $9.00 = 312 x 9.00 = $2,808 recovered; net 2,808 - 6,084 = -$3,276
```

Cutting E loses money at either end. Keep it. Its problem is stock depth:

```
Units held  = 3,900 / 14.30 = 273
Weekly sale = 520 / 52 = 10
Cover       = 273 / 10 = 27 weeks
At 10 weeks of cover: 100 x 14.30 = $1,430 of stock
Return on stock = 6,084 / 1,430 = 4.25 (from 1.56)
Stock released over time = 3,900 - 1,430 = $2,470
```

Check the supplier's lead time fits inside 10 weeks of cover before cutting depth.

## Stock already bought

**C** has 250 units on hand at $8.10 = $2,025. The supplier offers 80% credit:
0.80 x 2,025 = $1,620 now. Clearing at $7.00 would bring 250 x 7.00 = $1,750
over about 10 weeks, but would pull sales from B while it runs. Take the credit.

**F** has 110 units on hand at $22.00 = $2,420. The packaging is dated, it cannot
be returned, and it is worth about $5 a unit after June. The $2,420 is spent
whatever happens; compare the cash each option brings in from here (sell-through
rates are estimates):

| Option | Calculation | Cash |
| --- | --- | --- |
| Hold at $40 to June, salvage the rest | 1.5 a week x 22 weeks = 33 units x 40 = 1,320; 77 x 5 = 385 | $1,705 |
| Mark down to $28, clear in about 10 weeks | 110 x 28 | $3,080 |
| Mark down to $20 (below cost), clear in about 4 weeks | 110 x 20 | $2,200 |

$28 recovers the most. Even $20, below what the stock cost, beats holding at full
price. Going forward, range F only from October to December and buy to the season.

## The supplier's 2L proposal

The supplier forecasts 1,500 units a year at $5.50 contribution. Assume half its
units come from B buyers trading up, at B's $4.80 contribution:

```
Supplier volume: 1,500 x 5.50 = 8,250; less 750 x 4.80 = 3,600; net +$4,650
Half that volume: 750 x 5.50 = 4,125; less 375 x 4.80 = 1,800; net +$2,325
```

Positive at both volumes, so it is worth a trial in C's slot. Judge it on
category contribution after 13 weeks, not on the 2L line's own sales, and note
that B gains from C's exit and loses to 2L at the same time: read B's units in
the review.

## The answer

> Cut C, keep E with less stock, keep F as a seasonal line, and trial the 2L line
> in C's slot. Estimated effect on annual contribution: +$208 from cutting C plus
> +$2,325 to +$4,650 from the 2L trial, so +$2,533 to +$4,858 on $63,700
> (2,533 / 63,700 = 4.0% to 4,858 / 63,700 = 7.6%).
>
> C goes because about 75% of its buyers moved to B when it was last out of stock
> (85% at the peak; the cut pays above 71%), and B earns $1.40 more per unit. E
> stays: even if 60% of its buyers moved to D, cutting it would cost $3,276 a
> year. Its weakness is 27 weeks of cover; at 10 weeks its return on stock rises
> from 1.56 to 4.25 and releases $2,470. F is the only gifting line and sells
> 60% of its units in November and December.
>
> Assumed, not measured: C's switching share (from one 6-week stock-out), the 2L
> line's volume and how much of it comes from B, and the markdown sell-through
> on F.
>
> Next: take the supplier's credit on C's 250 units; check B can supply 15 more
> units a week; confirm E's lead time before reducing depth; mark F down to $28;
> review the 2L line and B's units after 13 weeks.
