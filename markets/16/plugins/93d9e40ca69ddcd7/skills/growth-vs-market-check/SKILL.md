---
name: growth-vs-market-check
description: Compares a company's actual or forecast revenue growth by segment and country with the growth of the corresponding external market, computes the gap in percentage points and the implied market-share change, flags forecasts that outrun their market, and drafts commentary for forecast reviews and monthly reports. Use whenever a user asks "are we growing faster than the market", needs market context for variance commentary, wants to sanity-check a budget or forecast against market growth, or provides revenue by segment and asks how it compares externally.
---

# Growth-vs-Market Check

## Purpose

Add an external driver to forecast review and monthly reporting. A forecast that outgrows its market for several years is the most common sign of over-optimism. The check turns it into a question for the unit owner, not a verdict.

## Inputs

| Input | Required | Default |
| --- | --- | --- |
| Internal revenue CSV: `segment,country,year,revenue,type` with type `actual` or `forecast` | Yes | — |
| Mapping of internal segments to market segments | No | Proposed by the skill, confirmed by the user |
| Flag thresholds | No | Gap above +5 points in a forecast year; gap above +3 points in three consecutive years ending in a forecast year |
| Currency basis (reported or constant) | No | Reported |

## Workflow

1. Validate the internal file: list the segment-country pairs and years, and confirm each pair has at least two consecutive years.
2. Propose a mapping from each internal segment to a market segment available in the data connector, with a confidence of exact, close or loose. Show the mapping table and wait for confirmation; taxonomy mismatch is the main cause of a wrong conclusion.
3. For each confirmed pair, fetch the market revenue series for the same years. Save all pairs in one CSV with columns `segment,country,year,market_revenue`, using the internal segment names.
4. Run `scripts/growth_gap.py --internal <internal.csv> --market <market.csv>`; pass `--gap-threshold`, `--run-gap` or `--run-years` when the user changed the defaults.
5. Write the commentary: one line per unflagged pair. For each flagged pair, write a short paragraph with the gap, the implied share change and the question for the owner, such as which initiatives or pricing actions support growth above the market.

## Output format

```
# Growth versus market: <scope>, <period>

## Mapping used
| Internal segment | Market segment | Confidence |

## Results
Table from growth_gap.py.

## Commentary

## Caveats
Mapping confidence, currency basis, source and release date of each market series.
```

## Data rules

- A share computed against a market estimate is itself an estimate; say so where it is quoted.
- Compare like with like: growth in reported currency includes exchange-rate effects the market series may not.
- A flag on a loosely mapped row means fix the mapping first.
- The internal file stays with the user; the skill reads it for the run and reproduces it only in the results table.
