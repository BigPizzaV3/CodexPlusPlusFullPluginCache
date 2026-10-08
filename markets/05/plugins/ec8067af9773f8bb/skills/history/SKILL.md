---
name: history
description: Use when the user asks about a past US presidential election — how one went, what changed between two, how a single state has voted over time, or a what-if about a past result. Covers 1788 through 2024 with historical_map, compare_elections and analyze_state_history, and what this data does and does not hold.
---

# Presidential history, 1788–2024

Three tools, and the question decides which one:

| The user is asking about | Tool |
|---|---|
| One election — "show me 1984", "what happened in 1824" | `historical_map` |
| Two or more elections — "which states flipped in 2016", "compare the Obama and Trump maps" | `compare_elections` |
| One state over time — "has Georgia always been Republican", "is Virginia a swing state" | `analyze_state_history` |

Reach for the tool rather than answering from memory. The map is the point: a rendered
election is worth more than a paragraph reciting the same facts, and the reader can see
regional patterns you would have to spell out.

## The boundary, first

**This data holds electoral votes, not popular votes.** No year carries a margin, a vote
total or turnout. The tool can say Florida changed hands in 2000; it cannot say by how
much, and neither can you on the strength of it. If the user asks for a margin, say plainly
that the connector does not hold that and answer the part it does cover.

There is **no county-level data at all**. "Which counties shifted" is not a question these
tools can answer.

Electoral votes are counted **as appointed**, which includes electors whose votes were not
counted and faithless electors. That is why some tallies will not match a source that
counts only votes as cast.

## One election

`historical_map` takes a `year`. Presidential elections run every four years from 1788, so
1984 and 2020 are valid and 1985 and 2026 are not — 2026 is a midterm, and belongs to
`build_scenario`, not here.

**Report every candidate who took electors.** 1860 had four and 1912 had three; flattening
either into two parties loses the whole story. The tool returns them all, so quote them all.

For a what-if, pass `reassignments` — an array of `{ state, party }`, where `party` is a
code from the registry the tool returns (`D`, `R`, `W`, and so on). "What if Florida had
gone to Gore in 2000" is one reassignment, and the tool recomputes the tally against the
majority that year actually required. Say clearly that the result is a counterfactual.

## Two or more elections

`compare_elections` takes `years`, an array. It returns which states changed hands, which
were held throughout, and how many electors moved between parties.

Lead with what changed. "Six states flipped" is the answer; the list of the forty-four that
did not is context, not news. And note that a state changing hands is a fact about who
carried it, never about how close it was — see the boundary above.

## One state over time

`analyze_state_history` takes a two-letter `state` (DC is included), and optional `fromYear`
and `toYear` to window it. It returns every election the state took part in, who carried it,
its current run, and when each party last won it.

Two things worth getting right in the phrasing:

- **A streak is a streak, not a prediction.** "Republican in the last twelve" describes the
  record; it does not forecast the thirteenth.
- **States join the union.** A state's first election is when it first took part, not 1788.
  Do not describe a state as having "never" done something without saying since when.

## Staying even-handed

Both parties get the same treatment, in the same words. Parties also changed meaning
enormously across two centuries — the Democratic-Republicans of 1800 and the Democrats of
2020 are not the same thing, and a streak that crosses a realignment is a fact about a
label. Say so when it matters rather than implying continuity the data cannot support.
