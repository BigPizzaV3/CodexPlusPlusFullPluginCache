---
name: eligibility
description: >-
  Use this skill to explain whether/why a security passes or fails MSCI index eligibility screens, including free float, foreign inclusion factor/foreign room, liquidity (ATVR/frequency of trading), market-cap and size-segment cutoffs, or current GIMI/index eligibility. Trigger for "why isn't this stock in the index?", "what would it take to qualify?", or "which size segment does it fit?".
---

# MSCI index eligibility screen

Compare MSCI-measured security values with MSCI inclusion-monitor cutoffs and flags. Passing quantitative screens is necessary but not proof of a future index addition.

## Output

Present one row per relevant screen: test, measured value, cutoff/bound if available, and pass/fail/flag. Then identify the binding screen or, if every test passes, the narrowest margin. Include calculation date and the exact mandatory inclusion disclaimer from `constraints.notes`.

## Workflow

1. Resolve the security with `search_index_securities`.
2. Use `search_index_datapoints` to discover the relevant inclusion-monitor fields. Search only the families needed for the question:
   - free float / rounded free float
   - foreign inclusion factor / investability factor
   - foreign room and lower/upper bounds
   - ATVR and frequency-of-trading liquidity
   - full/float-adjusted market cap
   - standard/IMI/large/mid/small cutoffs and assignment flags
   - overall eligibility/current membership flags
3. Read `constraints.notes` on every selected datapoint. Follow the monitor publication-date rule and reproduce the mandatory disclaimer exactly.
4. Fetch with `fetch_index_data` on the required date.
5. For China A-share questions, also discover and include any Stock Connect/access fields needed to interpret eligibility.
6. If the user asks for the rule itself rather than the measured value, use the methodology workflow or methodology-stack search instead of inventing the rule from raw datapoints.

## Interpretation

- Treat `_fg`/flag fields as authoritative reported indicators, not percentages.
- Treat `_pct` and `_musd` fields according to their documented units.
- If an overall eligibility flag conflicts with a manual reading of components, report both and note the discrepancy. Do not override the MSCI flag with your own arithmetic.
- Cutoffs are point-in-time and can move with market conditions, so date every result.

## Guardrails

- Never say a security "will be added" merely because it passes screens.
- Missing data is not a pass.
- Foreign room/FIF interactions may require methodology text; do not infer the governing rule from raw values alone.
- Reproduce the Index Inclusion disclaimer from `constraints.notes` verbatim.
