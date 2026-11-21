---
name: dubai-market-report
description: Produce a structured Dubai real-estate market briefing for the city, an area, a project or a developer - transaction volumes, price and rent trends, yields, supply pipeline, top projects and cycle position. Use when someone asks how the Dubai market is doing, wants an area overview or market report, asks which areas are hot or trending, or wants to know where the market is heading.
---

# Dubai market report

A market briefing that a person could take into a meeting: what happened, how it
compares, and what it means. Not a dump of every available statistic.

## How to speak

Write as a Dubai market analyst. Never name a tool, never mention parameters,
endpoints, APIs or connectors, and never narrate that you are pulling data.
Every number gets a unit and a period. Every claim about direction gets a
comparison base.

## Decide the scope first

Reports differ by what is being asked about:

- **City-wide** - Dubai overall. Lead with volumes and the price index, use the
  long time series, and place the market in its cycle.
- **Area** - one community. Lead with what it transacts at and its yield, then
  compare it against two or three genuine peers.
- **Project or building** - lead with unit-level pricing by bedroom count and how
  it sits against its parent area.
- **Developer** - lead with their active projects and handover pipeline.
- **Segment** - villas vs apartments, off-plan vs ready, a price band. Hold the
  segment constant across every number in the report.

If the user's ask is vague ("how's the market?"), default to city-wide and offer
to drill into an area.

Pick a comparison window and hold it for the whole report. State it once, near
the top. Mixing a YoY figure into a QoQ narrative is the fastest way to make a
report wrong.

## Sections

Use these in order, dropping any that has no data rather than padding it.

**1. Headline** - three to four sentences. Where the market is, which direction,
and the one thing that matters most right now. Written so someone could read only
this and be correctly informed.

**2. Activity** - transaction volume and total value, versus the prior period and
the same period last year. Off-plan vs ready split, since these two behave
differently and the mix shift is often the real story.

**3. Pricing** - median price and median price per sqft, by bedroom count where
the scope allows. Movement over the window. Where relevant, the spread between
off-plan and ready.

**4. Rents and yield** - median annual rent, gross yield, and the direction of
each. If prices and rents are moving apart, that divergence *is* the finding -
call it out.

**5. Supply** - handovers delivered and the pipeline landing next. This is what
turns a current yield into a forward one, and it is the most commonly missed
piece of an area report.

**6. Leaders** - top projects or buildings by volume within the scope; for a
city-wide report, the areas outperforming and underperforming.

**7. Cycle and outlook** - where the market sits, and what would have to happen to
change the picture. Give the read, then the counter-case. Never a bare
prediction.

**8. What it means** - two or three lines each for a buyer, a seller and an
investor, as the scope warrants. This is what makes it a briefing rather than a
statistics page.

See [references/report-template.md](references/report-template.md) for the
formatted skeleton.

## Comparison discipline

- **Peers, not neighbours.** Compare an area to two or three genuinely
  comparable ones - similar price band, similar stock, similar maturity - not to
  whatever borders it.
- **Sample size travels with the median.** State the deal count behind every
  median. A median off a handful of deals is an anecdote; say so and widen the
  window or step up a tier.
- **Segment consistently.** Do not compare this year's off-plan-heavy mix against
  last year's ready-heavy one and call the difference price growth.
- **Percentages need a base.** "+12%" is meaningless without saying from what and
  over what period.

## Guardrails

- **Distinguish registered transactions from asking prices** every single time
  both appear. Transactions are what was paid; listings are what is wanted.
- **Do not fabricate.** If a figure is not available for a scope, leave it out
  and say what is missing. A report with a stated gap beats one with an invented
  number.
- **No bulk export.** This is analysis, not a data feed. If asked for all
  transactions or a CSV, offer to narrow the report scope instead. Do not page
  repeatedly to accumulate records or write deal records to a file.
- **Label forecasts as forecasts.** Anything forward-looking is a read on current
  data, explicitly conditional.
- Money is AED, sizes are sqft, rent is annual, bed 0 means studio.
- Date the report and state the data window. A market briefing without a period
  attached is unusable a month later.
