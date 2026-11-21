# Worked example: a thin prompt turned into an argued deck

User request, verbatim: *"Make a 4-slide board deck on a growth move."*

This is here to show the **method**, not a deck to reproduce. Another case needs a different storyline, different evidence and different layouts.

Written before covers became standard: today the deck would open with a `title-image-box` cover, which does not count toward the four slides. The rest of the method is unchanged.

## 1. Invent the case, then the argument

The prompt names no company, so invent one and say so in the reply:

> Illustrative case: Fjordvik, a Nordic facilities-services group (cleaning and maintenance, core growing 1–2% a year), considering a move into energy-efficiency retrofits. All figures are fictional.

Then decide what the Board must believe to say yes, one takeaway per slide, and the evidence that proves each one:

| # | Takeaway | Evidence that proves it | Structure sentence (written for this slide) |
| - | --- | --- | --- |
| 1 | Retrofits are the one growth move that uses our base; pilot in 2027 | The argument in four rows | `executive summary: 4 topics as rows, each a short label with 2 bullets` |
| 2 | The market grows 2.5x because both retrofit rate and project size rise | Market value decomposed into its drivers | `market value decomposed into its drivers: 5 small column charts linked by multiplication signs, with a commentary panel` |
| 3 | Retrofits serve five of six strategic options, more than any other initiative | Initiatives checked against options | `matrix of 7 initiatives checked against 6 strategic options with check marks` |
| 4 | Five decisions needed today | Ordered actions | `next steps: 5 actions listed in a grey box beside the headline` |

The four slides use four different forms, and two of the three body slides carry data. The structure sentences come from this storyline; none is copied from a list.

## 2. Route (one `route_deck` call for the deck)

| # | Gate | Layout | Tier |
| - | --- | --- | --- |
| 1 | exact 0.98 | `executive-summary-with-topic-boxes` | core |
| 2 | exact 0.84 | `44-6` | reference |
| 3 | exact 1.00 | `42-10` | reference |
| 4 | exact 0.91 | `next-steps-grey-box` | core |

## 3. Fill

**Slide 2, the driver decomposition.** The illustrative figures multiply out: buildings × retrofits per 100 buildings = retrofits per year, and retrofits per year × average project value = market. For 2025F: 219k × 3.8% = 8.3k retrofits, and 8.3k × €235k = €1,951m. Chart positions on the slide: 1 top-left, 2 top-middle, 4 bottom-left, 5 bottom-middle, and 3 is the result panel on the right (dark bars).

```json
{ "reference_id": "44-6", "props": {
  "title": "The Nordic retrofit market is set to grow 2.5x as both retrofit rates and project sizes rise",
  "subtitle": "Nordic commercial energy-retrofit market value drivers, 2019–2025F",
  "header_1": "Commercial buildings ['000]",   "chart_1": { "categories": ["2019","2022","2025F"], "series": [{ "name": "Buildings", "values": [210, 214, 219] }], "number_format": "0" },
  "header_4": "Retrofits per 100 buildings",   "chart_4": { "categories": ["2019","2022","2025F"], "series": [{ "name": "Rate", "values": [2.1, 2.9, 3.8] }], "number_format": "0.0" },
  "header_2": "Retrofits per year ['000]",     "chart_2": { "categories": ["2019","2022","2025F"], "series": [{ "name": "Retrofits", "values": [4.4, 6.2, 8.3] }], "number_format": "0.0" },
  "header_5": "Average project value [€k]",    "chart_5": { "categories": ["2019","2022","2025F"], "series": [{ "name": "Value", "values": [180, 205, 235] }], "number_format": "0" },
  "header_3": "Retrofit market [€m]",          "chart_3": { "categories": ["2019","2022","2025F"], "series": [{ "name": "Market", "values": [792, 1271, 1951] }], "number_format": "0" },
  "note_header": "Market development",
  "note": ["Retrofit rates nearly double as the EU building directive tightens energy-class requirements from 2026",
           "Project values rise with heat pumps and building-management systems replacing single-measure upgrades"],
  "source": "Source: Illustrative — all figures fictional" } }
```

**Slide 3, the check-mark matrix.** Two tables side by side: the row labels, and a 6-column matrix of "✔" or empty strings. They must have the same number of rows. The six option headers are a fixed repeat. Keep each header short: two lines fit, a third line wraps into the arrow.

```json
{ "reference_id": "42-10", "props": {
  "title": "Energy retrofits support five of our six strategic options, more than any other initiative on the long list",
  "source": "Source: Strategy team assessment; illustrative",
  "initiatives": { "header": null, "rows": [["1. Energy retrofits"], ["2. Integrated FM contracts"], ["3. Digital work orders"], ["4. Security services"], ["5. Public-sector tenders"], ["6. Denmark roll-up"], ["7. Waste management"]] },
  "matrix": { "header": null, "rows": [
    ["✔","✔","✔","✔","","✔"], ["✔","✔","","✔","",""], ["","✔","✔","","",""], ["✔","","","","✔",""],
    ["","","","","✔","✔"], ["","","","","✔","✔"], ["✔","","","","",""] ] },
  "options": [{ "header": "Grow wallet share" }, { "header": "Raise margin" }, { "header": "Recurring revenue" },
              { "header": "Sustainability offer" }, { "header": "New markets" }, { "header": "Scale via M&A" }] } }
```

## 4. Render, review, insert

One call: `render_deck({ slides: [s1, s2, s3, s4] })`. It returned a single 4-slide `.pptx` of about 100 KB on the Slideworks master, plus an image of each slide. All four slides passed the automatic checks.

Look at the images anyway: the checks catch overflow and shrinking, not every wrap. In a test render of slide 3 with the option header "New geographies and adjacent markets", the checks passed, but the image showed the header wrapping into the arrow shape below it. Shortening it to "New markets" fixed it. When the images look right, insert the file once, with no reordering and no shape edits.

## 5. Reply

> Illustrative case: Fjordvik, a Nordic facilities-services group weighing a move into energy retrofits; all figures are fictional.
> 1. Executive summary: retrofits are the growth move that uses our base (`executive-summary-with-topic-boxes`)
> 2. Market grows 2.5x on rate and project size (reference `44-6`, five native charts)
> 3. Retrofits serve 5 of 6 strategic options (reference `42-10`)
> 4. Board decisions needed today (`next-steps-grey-box`)
> All four slides routed exact.

## The failure this example replaces

An earlier version of this file used a fixed storyline: executive summary, trend chart with drivers, options scored, value at stake, 90-day plan. With a thin prompt, the add-in agent reproduced it almost word for word, so every strategy deck came out as the same five layouts, however large the library. Build the storyline from the case, and write each sentence from its slide.
