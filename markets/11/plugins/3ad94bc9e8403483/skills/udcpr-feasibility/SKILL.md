---
name: udcpr-feasibility
description: What UDCPR 2020 allows on a plot in Maharashtra, from Citiwise. Built-up area with and without TDR, the building that fits, margins on every side, height, parking by unit mix, approvals, and a printable report, each with its UDCPR clause. Use for any question about building on a plot in Maharashtra, checking a design against UDCPR, or reading a UDCPR clause.
---

# UDCPR feasibility

Citiwise answers. You collect the facts, ask Citiwise and write the result. Never compute, recall
or estimate a rule, a number or a clause yourself.

## Before you start

The Citiwise tools (`feasibility`, `compare_uses`, `check_design`, `draw_plot`, `clause`,
`search_udcpr`, `search`, `fetch`, `towns`) come from the Citiwise MCP server at `https://citiwise.in/mcp`, which needs no sign-in.
If they are not available, tell the user in one line that the Citiwise plugin needs to be connected,
then stop. Do not answer from memory.

## Where Citiwise applies

UDCPR 2020 governs every city, town and village in Maharashtra except Greater Mumbai. Citiwise does
not cover Greater Mumbai (the MCGM area, including places such as Bandra, Andheri, Dadar, Colaba,
Borivali and Mulund), which has its own regulations. For a plot there, say in one sentence that
Citiwise does not cover Greater Mumbai, and do not call Citiwise or offer to run it. Places outside
Greater Mumbai, such as Thane, Navi Mumbai, Mira-Bhayandar, Vasai-Virar and Kalyan-Dombivli, are
covered; ask `towns` when unsure.

## Facts

Needed: town, plot area, every side and what lies beyond it (a road and its DP width, a
neighbouring plot, open space, a nallah, a river or a railway), congested area or not, land use
zone, any road widening or reservation and whether it is handed over, and the use.

Useful: side lengths or corners, stilt or not, floor heights, the ASR land rate, the user's sale rate, construction cost, TDR rate and required margin (for an appraisal, the most to pay for the land and the landowner's share in a joint development; never assume them), and the unit mix:
each type with its number and carpet area, passed as `units`, for example
`[{"type":"2 BHK","count":12,"carpet":60},{"type":"3 BHK","count":8,"carpet":85}]`. Parking takes
each type in its own Table 8-B row. When a count is left out, Citiwise works it out from the
building; say so when you report it.

Pass the area and the road widths as the user gave them: `area_unit` sqft, guntha, acre or hectare,
and `road_unit` ft. Citiwise converts them and says what it read in `units`; say that back to the
user. Never convert them yourself.

People ask in Marathi, Hindi or a mix with English ("majhya 4 guntha jagevar kiti majle?"). Read the
facts from what they wrote and answer in the language they used, keeping the figures and clauses
exactly as Citiwise gives them.

Basements: pass `basements` (levels) and `basement_flush` when the user mentions them. Citiwise
returns the basement area a level, the parking it holds and the ramp, each with its clause.

When the plot comes as a sketch or a measurement sheet, read the sides in order round the boundary with
their lengths and the angles or diagonals marked on it, and call `draw_plot`; it fixes the exact shape,
checks the measurements and returns the polygon and sides to pass to `feasibility`. Never work out
corners yourself. If a needed angle or diagonal is not on the sketch, ask for it.

If the user attaches a 7/12, a measurement sheet, a zone certificate, a DP remark or a plan, read
it and pull these facts out. Show them in one short list and ask the user to confirm. Ask only for
what is missing. Never assume a road width, a zone or whether the area is congested. Plot area is
the least of the 7/12, the measurement sheet and the site.

## Ask

- `towns` for the exact town name.
- `feasibility` for one use. It returns `report_url`, the full printable report.
- `compare_uses` for every use on the same land, in a fixed order.
- `check_design` for a proposal, item by item.
- `clause` and `search_udcpr` for the regulation's own words; `search` and `fetch` to find a regulation
  or table by topic and read it in full. When you quote a regulation, link its page:
  `https://citiwise.in/udcpr/6-2-6` for 6.2.6, `https://citiwise.in/udcpr/table-6-g` for Table 6-G.

## Write

Write like a feasibility note from a serious practice: exact, quiet and complete.

1. Open with the answer: `brief.headline` says it in one sentence, then any flag marked stop.
   The built-up area allowed with and without TDR, and the building that fits.
2. Then one table of the numbers that decide the design: FSI, built-up, height and its limit, the
   margin on each side, the floor plate, parking, lifts, and where they apply, the refuge area,
   open space and approvals. Put each number's clause in brackets, for example (6.2.6). Cite
   UDCPR clauses only.
3. Then at most three facts to confirm, only the ones that would change the numbers.
4. When the user wants a document, give the report link: "Full report: <report_url>". When they want a
   file to keep, send or print, give `report_pdf_url` (the study as a PDF). It is the one document, and it carries the site plan.
5. Close with one sentence: this checks feasibility, and the planning authority has the final say.

Rules:

- The answer and the report must agree. `report_url` carries the case passed to `feasibility`, so
  every figure you write (built-up, floors such as Stilt + 6, height, margins, parking) comes from
  that same call, in the words it returns. Do not mix in figures from `compare_uses` or any call made
  with different inputs, such as with or without stilt parking. If you show another case, name it
  as a separate case and give its own report link.

- Never recommend a use or a design. `compare_uses` is a list in a fixed order, not a ranking.
- A proposal gets one row per item: allowed, proposed, and whether it passes.
- Add any margin, height, lift, parking or fire tank note Citiwise returns as one line under the
  table. Fire tank figures are indicative; the Chief Fire Officer decides.
- No preamble and no description of how the answer was made. The user sees UDCPR and their plot.
- If Citiwise cannot answer, say in one line what is missing.
- Write in full, plain sentences. No em dashes.

