# Phrasing structure sentences

The router (`route_deck`, `find_layout`) matches on **structure and counts**, not on topic. A good sentence names the evidence form, the counts and the element types. Topic words, client names and the figures themselves don't help routing.

The examples below show the pattern for each kind of evidence. **Don't reuse them verbatim.** Write the sentence from your own slide: your counts, your chart type, your elements. Two decks about different companies should not produce the same sentences.

The gate and top hit are shown (most routed on 2026-09-27, the rest on 2026-09-23) so you can see what kind of phrasing reaches what.

## Trend over time

| Example phrasing | Gate → hit |
| --- | --- |
| `column chart of revenue over 6 years with data labels and a side panel of 4 icon-labelled drivers` | exact → ref 26-2 |
| `line chart of two indicators over 25 years with shaded recession bands and 2 callouts` | exact → ref 193-1 |
| `stacked column chart over 10 years with 5 components and 2 summary rows beneath the axis` | exact → ref 193-5 |
| `two growth column charts side by side with CAGR badges and a row of numbers under each chart` | exact → ref 64-11 |

## Ranking and benchmark

| Example phrasing | Gate → hit |
| --- | --- |
| `ranking bar chart of 10 players with a flag or logo under each bar and a share-of-total row beneath` | exact → ref 26-1 |
| `peer benchmark: two ranked column charts of 7 companies with text callouts, and an insights table of rating and outlook on the right` | exact → ref 167-3 |
| `100% stacked columns: mix by region for 6 companies with a logo under each column` | exact → ref 70-3 |
| `bubble chart comparing competitors on two multiples, bubble size = market cap` | exact → ref 138-2 |

## Decomposition and drivers

| Example phrasing | Gate → hit |
| --- | --- |
| `market value decomposed into its drivers: 5 small column charts linked by multiplication signs, with a commentary panel` | exact → ref 44-6 |
| `driver tree: profitability broken down into revenue and cost drivers over 4 levels` | exact → ref 70-7 |
| `value at stake: 4 levers as rows, each with a large figure, a category label, 2 lever bullets and a share of total, no chart` | exact → ref 9-22 |

A bridge from one value to another is a `waterfall` in the core chart layouts (up to 12 steps): name the chart type in the sentence, e.g. `waterfall bridge from 2024 to 2026 EBIT with 5 levers and a takeaway panel`. A decomposition into multiplied drivers stays a driver chart like the ones above.

## Matrix, scoring and assessment

| Example phrasing | Gate → hit |
| --- | --- |
| `matrix of 9 initiatives checked against 6 strategic options with check marks` | exact → ref 42-10 |
| `harvey ball matrix: 9 locations as rows scored on 10 criteria as columns` | exact → ref 63-1 |
| `maturity assessment: 9 capabilities as rows on a 5-stage scale, current and target positions plotted as connected dots` | exact → ref 189-5 |
| `evaluation of 3 options against 5 criteria scored 1-5 with a total score row` | exact → core |
| `SWOT: 4 quadrants as tables, each with 4 items and a count column` | exact → ref 66-1 |
| `4 risks in rows with likelihood, impact and a mitigation column` | approximate → core `risk-mitigation` |

## Process, structure and plan

| Example phrasing | Gate → hit |
| --- | --- |
| `value chain: 7 stages as arrows with an icon, a description and key stakeholders per stage` | approximate → ref 202-6 |
| `pyramid with 5 levels and a description beside each level` | exact → ref 178-15 |
| `timeline of 10 years as numbered circles on a line with an event box above or below each year` | approximate → ref 171-1 |
| `approach: exactly 5 sequential steps, each with an icon, a heading and a box of what was done` | exact → ref 9-18 |
| `3 strategic pillars as columns with 3 rows each and an enablers band` | approximate → ref 61-1 |
| `project plan: 3 phases with 3 workstreams each on a week grid over 12 weeks` | exact → core |
| `Gantt over 12 quarters: 3 phases with 3 activity bars each, and 3 milestones` | exact → core (2026-10-26) |

## People and proof

| Example phrasing | Gate → hit |
| --- | --- |
| `team page: 3 people side by side with photo, name, role, experience bullets and selected clients` | exact → ref 67-3 |
| `3 customer quotes stacked, each with a headshot, name and role, and a core-purpose circle on the right` | exact → ref 172-2 |

## Openers and closers

| Example phrasing | Gate → hit |
| --- | --- |
| `executive summary: 4 topics as rows, each a short label with 2 bullets` | exact → core `executive-summary-with-topic-boxes` |
| `executive summary with problem, solution, recommendation and 3 next steps` | exact → core |
| `next steps: 5 actions listed in a grey box beside the headline` | exact → core `next-steps-grey-box` |
| `simple text table with 4 rows and 3 columns: decision, owner, date` | exact → core `table` (no dedicated decision log exists) |
| `numbered agenda with 6 sections` | exact → core |

## Phrasing rules

- Lead with the evidence form (`ranking bar chart`, `driver tree`, `matrix`, `value chain`), then the counts, then the extras (`side panel`, `callouts`, `logos`, `summary row`).
- Name the element types the slide must contain: `icons`, `harvey balls`, `check marks`, `native chart`, `table`, `number balls`, `photo`.
- Say `no chart` or `no image` when you specifically don't want one. Many reference slides have charts or photos and will otherwise compete.
- Probabilities move a few points between runs, so a sentence near 0.5 can flip to `none`. Tighten the counts rather than falling back to a generic text layout.
