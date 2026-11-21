# Directional methods

For teams that cannot run a geo experiment, or need a read on a change that already happened. These methods give a direction and a rough size. They do not isolate the cause, and every output says so.

## Pre/post with comparators (`prepost`)

Compares the KPI in a window with three baselines, each built only from data outside the window:

| Comparator | Baseline | Breaks when |
|---|---|---|
| prior_weeks | Same weekday average over the previous 4 weeks (`--weeks`) | Seasonality changes inside the window (holidays, month start) |
| yoy | Same weekday-aligned window last year, scaled by this year's growth in the 28 days before | Less than a year of history, or last year had an unusual event |
| control_ratio | Ratio of KPI to a control series before the window, applied to the control during the window | The control was also affected, or the ratio drifts |

What makes it more than a guess: the script runs the same comparison on every past window of the same length, where nothing changed. It reports how much the comparison moves by chance (`noise_band_90_pct`). It also reports how often past windows moved more than this one (`share_of_history_with_bigger_move`). A change inside the normal band is indistinguishable from a normal period.

Verdicts:

- **directional signal**: all comparators agree on the direction and all are outside their normal band.
- **weak signal**: same direction, only some outside the band.
- **no signal**: within the normal movement.
- **inconclusive**: comparators disagree on the direction.

Use it for:

- A pause or budget change that already happened.
- A quick read before proposing a proper test.
- Checking a claim like "we paused it and nothing changed".

## Switchback (`switchback`)

Alternate on and off blocks in one market, for example 1 week on and 1 week off over 8 weeks. The script regresses the KPI on an off indicator, weekday effects and a trend. It drops a washout at the start of each block. It then tests the effect against all relabelings of which blocks were off.

- At least 4 blocks (2 on, 2 off). 6 to 8 blocks give a usable p-value.
- Block length of 1 to 2 weeks, so each block covers every weekday.
- Washout of 2 to 3 days for search and retargeting.
- Not for channels with long carryover (TV, YouTube, brand awareness): the off blocks still benefit from earlier on blocks.
- Decide the schedule before starting, ideally by coin flip for which block starts off.

## Brand search pause, the most common case

1. Prefer a geo go-dark if the country has regions, or a switchback if not.
2. KPI = total conversions from the backend, not paid search conversions. The question is how many conversions move to organic and direct when ads stop.
3. Track organic clicks on brand queries from Search Console during the test: their increase is the mechanism.
4. Watch competitor activity on the brand terms. Competitors bidding on the brand is the main reason brand ads can be incremental; check auction insights before and during.

Evidence to set expectations:

- eBay switched off brand search ads: 99.5% of the lost clicks came back through organic results (Blake, Nosko and Tadelis 2015).
- Across thousands of brands on Bing, brand ads added 1% to 4% of clicks with no competitors present. When competitors bid and the brand did not, competitors took 18% to 42% of clicks (Simonov, Nosko and Rao 2018).
- So the answer depends on the competitive situation of each brand, which is why it needs a test and not a rule.

## Quick sizing without data (`quick`)

`python scripts/geolift.py quick --baseline-per-day 120 --residual-cv 0.15` gives an MDE per test length from three numbers:

- Daily KPI in the treated group.
- Its day-to-day noise after the control explains what it can: 0.05 to 0.15 for large aggregates, 0.2 to 0.4 for small ones.
- Its autocorrelation.

Use it to tell a team whether a test is feasible before they export data.

## What these methods do not do

- Separate the change from promotions, competitor moves, seasonality shifts, PR or tracking changes that happened in the same window.
- Give a causal number for a budget decision of material size. For that, run a geo experiment or a platform lift study.
