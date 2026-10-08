---
name: aims360-dashboard
description: Data contract for rendering AIMS360 connector results visually — what every dashboard, report or chart built from orders/invoices data must state, qualify or suppress, plus the embedded AIMS360 brand palette, type and motifs in assets/aims360-brand.css. Defers to dataviz for chart craft. Use whenever visualising, charting, reporting, or dashboarding ANY AIMS360 orders/invoices output — even if the user doesn't say "dashboard".
---

# AIMS360 data contract

This skill does not prescribe **layout** — composition and hierarchy are a design decision. Palette,
type and the brand motifs are not: they ship in `assets/aims360-brand.css` as constants (see **The
brand asset**), because they are not judgement calls.

It also sets **ambition** — see *Aim for a showpiece*. Layout stays free; look and reach do not.

What no design brief can know: **which AIMS360 numbers are trustworthy, and what must travel
alongside them.** Every rule below was learned from a live wrong answer.

## The governing rule

A dashboard makes numbers look authoritative — that is its job, and its hazard. The connector already
qualifies its output; a visual layer must carry those qualifications, not quietly drop them for a
cleaner composition.

**If a figure arrives qualified and the design has nowhere to put the qualification, the design is
wrong. Change the design, never the figure.**

## Read the right fields

- Totals, coverage and scope come from `structuredContent.resultSummary` and the answer text.
- **`previewRows` is a sample, not the population** — 25 rows for a grouped result, 10 for a raw
  list (`buildPreviewRows`, `result-formatter.ts`). Never sum it, never rank from it, never infer a
  total from it. If you need a number that isn't in `resultSummary`, ask the connector again.
- A metric's label comes from `totalBookedAmountLabel`, not from the metric key you asked for — the
  server may have resolved it to a different one and it says so.

## What must appear

**Scope.** Population, window *with its date field*, and coverage — `complete`, `top N of M`, or
`partial`. A ranking's subtotal is not the population: "4,417" was the parent count of fifteen
groups where the filter matched 4,908.

**Exclusions.** If anything was removed — `LOOPOFFSET`, a bulk style, a DTC channel — say so. Silent
exclusion is non-negotiable here.

**Both sides of a comparison.** `+37.9%` alone is unreadable. Show current, prior, and the change,
with both periods labelled.

## What must be qualified

Render the value, then a marker resolving to a plain-English note — never a bare confident number,
never silent omission.

Known-bad right now:

- **Any 2026 margin or cost figure.** Cost data is largely absent — one style's `totalCost` fell from
  $62,344 to $804 on comparable volume. Margin is overstated and not comparable year over year.
- **`fill_rate`.** Held upstream pending `pickQuantity` at a totalable grain.
- **Anything described as "wholesale".** No such field exists — `retailInvoice` catches Shopify but
  not Global-E (DTC, flagged `false`). Don't invent a definition unasked.
- **Margin %** is measured over *costed* revenue, not all revenue. Say so wherever it appears.

Two rules this generalises to: **a ratio across two different cohorts is not a conversion rate** —
invoiced ÷ booked mixes orders entered this period with invoices billed this period; call it
throughput, not a funnel. And **a known-missing metric earns a visible tile, not only a sentence** —
show a dash in the KPI row with "not exposed," so the gap is seen, not scrolled past. **That KPI row
is the page's default view** — not a secondary tab. Observed live: fulfilment time and discounts were
both explicitly asked for, both correctly declined, and both landed only in a "Data Quality" tab
nobody sees by default. The honest answer existed and was still effectively hidden.

## What must be suppressed

A ratio the connector returned as `null` is **undefined or impossible**, not zero — render an em dash
with the reason reachable. Zero is a measurement; `—` is the absence of one.

Both states occur live: a group with no cost data at all (undefined), and a $1 net sale carrying
−$43 of margin (impossible — a share cannot exceed the whole it is a share of).

## A bar's length is a claim about its number

A number and the mark beside it are two renderings of the same fact — when they disagree, the reader
believes the mark.

**Length maps to the label's scale.** A row reading 73.6% fills 73.6% of its track — normalising to
the row maximum makes the largest full-width by construction, a rank chart that must not carry
percentage labels. Observed live: a row labelled 73.6% rendered at width 100%.

**One page, one rule — a chart done right does not exempt its neighbour.** Observed live, on a page
built under this very rule: a status chart correctly matched width to label; an order-source chart
five lines below it, on the same page, independently re-derived width from its own row maximum and
reproduced the identical bug. Getting it right once is not the same as making it structural — use one
shared computation for every bar chart on the page, not a bespoke one per section.

**A row with two numbers still gets one bar.** Observed live: a growth chart's bar tracked dollar
magnitude while its label printed percentage change — a +1108% row rendered shorter than a +49% row.
The code's own comment reasoned "the bar matches what these rows rank by, not what's printed" — that
justification *is* the bug. Pick one number to be both the bar's basis and the label; if both matter,
print both as text and let neither alone drive a bar it only half explains.

**Zero draws nothing.** A minimum-width floor fabricates a mark for an empty row. Observed live: `$0`
and `$1,182` both rendered at 0.60%. If the row must stay visible, the label carries the zero; the
track stays empty.

`—` and `0` both draw no bar — the label still tells them apart: one is a measurement, the other is
the absence of one.

## Never invent a visual that reads as data

A colour swatch, a fabric thumbnail or a category icon derived from a *code* is a guess rendered as
fact. AIMS360 carries colour **codes and descriptions** — `SAM` / "Sage Multi" — and **no hex
values**. A merchandiser reading a sage-green chip will believe that is the fabric.

Observed live: a dashboard mapped `Sage #A8B49A`, `Midnight #232C46`, `Powder Blue #B7CBDD` from
nothing but the code names. Names read as data; colour felt like design. It is not.

Show the code and description, or derive tints from the brand palette.

The same applies to any visual implying a measurement the data doesn't contain — a trend arrow on
two points, a target line with no target behind it, a forecast band.

## Beware a trend drawn from a handful of units

Small absolute numbers make dramatic percentages — "Amazon fell from 237 units in May to 108 in
July" is a 54% decline and also plain noise. State the absolute figures beside any rate, and flag a
movement too small to read.

## What the payload licenses

Interaction is bounded by what the connector returned, not by what looks fetchable —
`answer.shape` says which:

| `answer.shape` | rows carried | interaction licensed |
|---|---|---|
| `single_total` | none | hero figure only — no control; nothing behind it |
| `rollup_by_time`, `all_groups` (≤30 groups) | complete | full client-side sort / filter / drill |
| `top_n_with_tail` (>30 groups) | top 30 only | a re-sort re-orders 30, not the catalogue — render `tail` as "+N more" |
| `raw_list`, `line_items` | bounded by `limit` | the richest surface: sort, multi-facet filter, type-ahead |

**Row budget:** the host's ~150,000-character tool result is the real ceiling — roughly 200–400
bytes/row, so ≈300 rows/section across the page.

`answer.rows` is the only interactive source; `previewRows` stays forbidden regardless of row count.

## A control is a claim

A control is a claim about what this page can do, like a swatch is a claim about the data — the
failure is never that it exists, but that its claim isn't true.

- **A re-sort claims a re-ranking** — ranked server-side on one metric, re-sorted to another, the
  toggle re-orders *that subset*. Say it plainly: *"ranks are server-side by units — switching to
  Net $ re-sorts these 25, not the full catalog."*
- **A filter claims a search** — over an embedded subset it searches what was fetched; name what it
  covers.
- **A refresh claims new data** — let it re-query (see *The page should answer back*). A "Refresh
  live" button that re-renders the same JSON stays wrong.
- **Every state-changing interaction has a way back** — a filter, sort or drill-in needs a visible
  undo.
- **Styling something to look interactive is also a claim.** A `:hover` state or a caption promising
  "click to sort" with no listener behind it lies in CSS instead of prose. Observed live: three
  sentences described sortable columns; the script wired zero `<th>` listeners.

A control that would lie needs a control that tells the truth, not a page without controls. A page
nobody can interrogate has not passed this test.

## The brand asset

`assets/aims360-brand.css` ships beside this file, embedded as `data:` URIs — Montserrat, the
wordmark, colour tokens, dark-ground lifts, banded surfaces, the AIMS360 motifs, and the
measure-to-colour assignment. **Inline its contents**; never link it or re-fetch the font or logo.

**Draw the wordmark itself somewhere — typed text is not a substitute for it.** `--aims-logo` is the
real embedded PNG, not a colour or a font; defining the token and never consuming it (`var(--aims-logo)`
must appear at least once, typically as the nav's background-image) means the actual asset never
renders. Observed live: a build declared the token, then hand-typed "AIMS360" in Montserrat as the nav
mark instead — the true wordmark sat inlined and unused the entire time.

**A motif is a constant; a composition is a decision.** The hero gradient, dot diamond, eyebrow
signature and pill button are brand identity — use as shipped.

- **Colour from a token, never a hex you chose** — `--aims-white`, `--aims-charcoal`,
  `--aims-purple`, `--aims-pink`, `--aims-black`, `--aims-platinum`.
- **`--aims-logo-grey` is not `--aims-platinum`** — 26 apart; substituting collapses the logo into
  the chrome.
- **On a dark ground, substitute `--aims-purple-on-dark` / `--aims-pink-on-dark`** — book values
  measure 1.44:1 / 3.62:1 on `#151920`; purple's lift is mandatory, pink's a choice. Both defined.
- **No positive/negative pair, no ramp past three.** Pink is the accent — "bad" misreads. A fourth
  series needs a decision, not an invented tint.
- **Artifacts block requests, not code.** A font CDN link, script, remote image or third-party
  `fetch()` is silently dropped — no error. (Google Fonts was observed blocked here 2026-08-03 —
  keep embedding.) Inline `<script>` runs; `claude.use(...)` is not third-party.

## Chart craft comes from `dataviz`

Do not re-derive chart craft here — the built-in **`dataviz`** skill governs form, marks, colour and
tooltips; read it first (loaded in Claude Code; UNKNOWN on plain claude.ai — the clause below covers
that gap).

- **Palette is ours** — `assets/aims360-brand.css`, dark-ground lifts included; three series, no
  positive/negative pair.
- **A tooltip may not carry a qualification alone** — `dataviz` says tooltips enhance, never gate;
  binds hardest on caveats.
- **A filter over an embedded subset scopes the fetch, not the catalogue** — layered on `dataviz`'s
  layout rule.
- **Refetch holds the previous render at reduced opacity**, scope line included.
- **Chart form, compressed:** ranking → bars; composition → stacked or ring; movement → area with an
  emphasised endpoint.

`dataviz` decides how a chart is drawn; this file decides what a number is allowed to claim.

## Aim for a showpiece

Being **trusted** and being **worth looking at** are separate jobs. Treat an AIMS360 dashboard as
**editorial work** — someone will present it — but none of the honesty rules bend.

Levers, in rough order of effect — reach for what the data supports:

- **One hero moment** — a figure at a scale nothing else competes with, the most consequential thing
  in the data. Four equal tiles is no argument.
- **Use the whole palette** — six values plus the dark-ground lifts. Three reads as unfinished.
- **The emblem is a ring** — a power button, four dots, already a gauge: draw coverage and
  share-of-total in the brand's own geometry, not a generic donut.
- **Compose densely** — tight grids, aligned baselines, real contrast between a headline figure and
  its label.
- **Consider the dark ground** — the lifted pink and purple on `--aims-surface-inverse` read more
  striking than white, and are brand-legitimate.
- **The nav is its own decision, not an extension of the hero.** Committing the hero to
  `--aims-surface-inverse` doesn't obligate the nav to match it — a light nav over a dark hero reads
  as considered contrast, not inconsistency.

**If a qualification has nowhere to sit, the design is wrong** — a constraint on the composition, not
a ceiling on it: the next section is about giving qualifications more places to sit.

## The page should answer back

These readers are AIMS360's customers — brand owners and merchandisers, not analysts handed a
report. A page that can't answer sends them back to chat.

An HTML page is interactive by default: the hover layer is part of the deliverable, not an upgrade.
Inline `<script>` runs — the CSP blocks *requests*, not code. Four levers, ascending cost:

- **Explore what's shown** — every mark answers pointer and keyboard focus alike (covers touch too).
  `dataviz` covers the rest: crosshair, per-mark tooltip, ≥24px hit targets, `textContent` never
  `innerHTML`.
- **Move around the page** — sticky nav, `scroll-behavior: smooth`, native `<details>`. Pure CSS.
  Give it room to breathe: a cramped logo against the links reads as an afterthought, not a decision
  — size the bar to the wordmark, not the other way round. **One sticky layer, not two.** A page's
  own sticky nav is enough; do not also make table headers sticky. Observed live: a
  `thead th{position:sticky}` offset to clear the nav still visually sliced through the first body row
  as it scrolled past — the row was one of the tallest on the page, and no offset reliably reserves
  clearance for whatever row is mid-transition. This can't be verified before publishing, so don't
  stack it. Two sticky bars of page CHROME (a nav, then a filter toolbar) are fine — neither competes
  with scrolling rows. The risk is specifically a second sticky layer that has to coordinate with
  per-row CONTENT scrolling past it, not stacking sticky bars in general.
- **Change the question** — `claude.use("mcp")`, then `watchTool` for anything displayed, `callTool`
  for a one-shot (read **`artifact-capabilities`** first; `null` is normal). **The scope line derives
  from the response, never typed in** — a stale caption over live numbers is the worst bug here.
- **Move a little** — 150ms transitions on hover/open; the emblem ring drawing once on load. Honour
  `prefers-reduced-motion`.

A disclosure is *somewhere to put a qualification* — a still page has the least room of any page you
can build. **Scope, coverage, exclusions and known-bad notes stay visible while any disclosure is
collapsed**; methodology or an em-dash's reason may live inside `<details>`, since the visible
summary — or the dash — is the marker. A qualification only reachable on hover has been dropped, not
placed.

## At scale, organize — don't just stack

Many parallel cuts (top / growing / declining / new / lapsed accounts, a dozen breakdowns, this-year
and comparison views) don't have to become one long scroll.

- **Group parallel cohorts as tabs, not stacked cards.** State the TRUE population even when a subset
  renders — "131 accounts qualify; top 12 shown," not just "top 12."
- **One filter rail can scope several already-fetched visuals** — a tier between filtering one
  embedded subset and re-querying the connector. Show a live count: "N of M rows · K filters on." A
  filter wired to nothing is the sortable-header lie again, just harder to notice.
- **One consolidated coverage section, alongside per-section captions, not instead of them.** Seven
  scattered notes get missed; state coverage once, completely — available / partial / not exposed.
  Any claim in it is computed, not typed — a hand-written "these lists are complete" is a bug the
  moment one row of the underlying data disagrees; derive it from the same total the per-cut captions
  already compute, never assert it separately.

A tab hiding a caveat, or a filter count that lies, is the governing rule broken at a larger scale.

## Before publishing

- [ ] Scope stated — population, window and date field, coverage — from the response, never typed
      in.
- [ ] Exclusions named.
- [ ] Every known-bad figure is qualified, readable without a pointer; scope stays visible while any
      disclosure is collapsed.
- [ ] No null rendered as zero, no zero drawing a mark.
- [ ] Every bar, on every chart on the page, agrees length with its printed number — checked per
      chart, not assumed from the first one.
- [ ] Comparisons show both periods.
- [ ] Nothing recomputed from `previewRows`; interactive data comes from `answer.rows`.
- [ ] Every control's claim is true; a re-sorting toggle says what it re-sorts.
- [ ] Every chart with marks answers hover and keyboard focus alike.
- [ ] The page still argues as a static screenshot before any interaction.
- [ ] Every headline figure carries its unit and period.
- [ ] No invented swatch, thumbnail or icon standing in for data.
- [ ] Every font, image and script embedded — **no external request anywhere**.
- [ ] A subtotal is never sitting where a reader expects a total.
- [ ] One thing is unmistakably the headline, more than three brand colours work, and the page
      responds when pointed at — else revisit *Aim for a showpiece*.
- [ ] Every claimed control (sortable header, filter, toggle) has a real listener behind it — a hover
      style and confident copy are not enough.
- [ ] Every "top N of M" / "X of Y" sentence — and any claim like "these lists are complete" —
      matches the actual data, not a hand-typed guess.
- [ ] Every explicitly-asked-for, known-missing metric has a dash tile in the DEFAULT-visible KPI
      row — not only a sentence in a secondary tab.
