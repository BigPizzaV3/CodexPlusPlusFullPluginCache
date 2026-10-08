---
name: map
description: Use when the user describes a hypothetical outcome for the 2026 US Senate or House and wants to know what it does to control of the chamber — "what if Republicans sweep the toss-ups", "if Democrats hold Georgia and flip Texas, who has the Senate", "show me the House map if the leans all break one way". Translates the scenario into build_scenario parameters and reports the tally the tool returns, with an interactive chamber map.
---

# Build a scenario map

Turn the scenario the user described into a `build_scenario` call, then report what the
tool returns. **Do not do the seat arithmetic yourself, and do not guess at ratings you have
not read.** The same sentence produces different numbers as the ratings move — a race that
was a toss-up last month may be Lean D today, in which case "they lose it" changes nothing.

## Choosing the chamber

- The scenario names states → Senate. It names districts ("TX-18", "Texas 18th") → House.
- Genuinely ambiguous → ask which chamber rather than assume.
- The user asks for "the map" with no scenario → the Senate on the consensus baseline.

## Translating the scenario

| The user says | Parameter |
|---|---|
| "sweeps the toss-ups", "runs the table", "everything breaks their way" | `tossups: "democrat"` or `"republican"` |
| names individual races | `assignments`, e.g. `{ "race": "ME", "party": "democrat" }` |
| "from scratch", "a blank map" | `baseline: "empty"` (otherwise leave the consensus default) |
| wants a race left open | `{ "race": "...", "party": "none" }` |

Named races are applied last and win over the blanket toss-up rule.

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

## Reporting the result

- The tally, whether anyone reaches the number needed for control (51 in the Senate, 218
  in the House), and how many seats are still uncalled.
- The date the ratings were published.
- Everything in `unresolved`, said out loud. A tally for a scenario the user did not
  describe is worse than no tally.
- Independents are their own party. Never fold them into a majority, and never say a party
  holds the chamber unless it reaches the threshold on its own.

VoteMapper is a simulator. Ratings are forecasters' opinions about an election that has not
happened, so never describe a scenario's outcome as a result.
