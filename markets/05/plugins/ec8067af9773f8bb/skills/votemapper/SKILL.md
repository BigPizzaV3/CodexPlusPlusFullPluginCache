---
name: votemapper
description: Use when answering questions about US elections on a map — 2026 midterm race ratings, which races are competitive, what has changed in the forecast, what a described scenario does to control of a chamber, checking and scoring a sealed VoteMapper forecast, or any presidential election from 1788 to 2024. Covers the ratings taxonomy, the seat arithmetic, and what this data is and is not.
---

# VoteMapper

VoteMapper answers questions about US elections from published, dated datasets, and
answers them on a map.

**The 2026 midterms**: the consensus competitiveness rating for any Senate race or House
district, which races are genuinely in play, what forecasters have changed their minds
about, and what a described scenario does to control of a chamber.

**Presidential history, 1788–2024**: how any past election went, what changed between two
of them, and how a single state has voted over time. That half has its own skill — see
[history](../history/SKILL.md) for which of the three tools answers which question, and for
the boundary that matters most there: the historical data holds electoral votes, never
popular-vote totals, margins, turnout or anything at county level.

Which half a question belongs to is usually obvious from the year. 2026 is congressional
and belongs to `build_scenario`, `lookup_race` and `list_races_by_rating`; a presidential
year is historical. Nothing here covers 2028 — there is no forecast for an election with no
ratings published, and saying so is the right answer.

## The boundary, first

**VoteMapper is a simulator. It never reports live vote counts, returns, or called races.**

A rating is a forecaster's opinion about a race that has not happened. A rating moving from
Lean R to Toss-up is Cook and Sabato revising their view — it is not a result, and saying
"North Carolina moved to Toss-up" must never be phrased as though something happened in
North Carolina.

The one exception is `score_forecast`, which reads race calls published from the Associated
Press in order to score a sealed forecast. Even there, the tool reports whether a forecast's
picks were right; it does not report vote totals and calls nothing itself. For live results,
use a results source.

## The ratings taxonomy

Seven ratings, one scale, safest Democratic to safest Republican:

`safeD` · `likelyD` · `leanD` · `tossup` · `leanR` · `likelyR` · `safeR`

- **Competitive** means `leanD`, `tossup` and `leanR` together. When someone asks which
  races "matter", "are in play" or "are close", that is the filter they want — not `tossup`
  alone, which is narrower than the question.
- **A toss-up has no favourite.** It is not a half-seat for each party and it is not a lean.
  Under a consensus baseline it stays uncalled.
- Ratings are a **consensus of Cook Political Report and Sabato's Crystal Ball**, and every
  answer carries the date they were published. Quote that date; a rating without one invites
  the reader to assume it is current when it may not be.

## The seat arithmetic

This is the part worth deferring to the tools rather than doing in your head.

**The Senate has 100 seats and only 35 are on the 2026 ballot.** The other 65 are held over
and already counted — 32 Democratic, 31 Republican and 2 independent as of the current data.
A Senate tally built from the contested races alone is wrong by 65 seats. Control needs 51.

**The House is all 435 districts**, every one on the ballot, and control needs 218. Most
districts are not individually rated: an unrated district is treated as safe for whoever
holds it, which is why the House map is nearly full before anyone calls anything.

**Independents are their own party.** Two sitting senators are independents. Do not fold
them into a party's total, and do not describe a party as holding the chamber unless it
reaches the threshold on its own.

## Turning a sentence into a scenario

`build_scenario` exists because models read scenarios well and count them badly. Your job is
the translation; let the tool do the arithmetic and quote what it returns.

> "Republicans hold every toss-up but lose North Carolina and Maine"

```json
{
  "chamber": "senate",
  "tossups": "republican",
  "assignments": [
    { "race": "NC", "party": "democrat" },
    { "race": "ME", "party": "democrat" }
  ]
}
```

The pieces:

- `baseline` — `consensus` (default) starts every race at its forecaster favourite and
  leaves toss-ups uncalled. `empty` starts from an uncalled map.
- `tossups` — hands every toss-up to one party. Use it for "sweeps the toss-ups", "runs the
  table", "everything breaks their way".
- `assignments` — individual races, applied last, beating the blanket rule. `"none"` returns
  a race to uncalled.

**Do not compute the result yourself.** The same sentence produces different arithmetic as
ratings move: a race that was a toss-up last month may be Lean D today, in which case
"they lose it" changes nothing. The tool resolves against the ratings in effect; you do not
know them.

Races are addressed by id or name: `GA` and `TX-18`, or `Georgia Senate` and `Texas 18th`.
Anything the tool could not apply comes back in `unresolved` — say so rather than reporting
a tally for a scenario the user did not describe.

## Sealed forecasts

A user can declare a forecast in the VoteMapper app, which seals it with a SHA-256
fingerprint. `verify_forecast` says whether a fingerprint is on the record and what it was
sealed over; `score_forecast` scores it against published calls.

**Accuracy is counted over called races only.** An uncalled race is not a miss. Before
election night there is nothing to score, and the honest answer is that — never a zero.

**Sealing happens in the app.** These tools read the registry; they cannot create or seal a
forecast, and you should not imply otherwise.

## Staying even-handed

Both parties are treated symmetrically by the data and should be by you. Use both directions
in examples, attach no adjectives to either party's position, and let the numbers carry the
answer. Every rating is sourced and dated; say where it came from.
