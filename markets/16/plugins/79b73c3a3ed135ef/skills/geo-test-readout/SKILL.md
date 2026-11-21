---
name: geo-test-readout
description: Analyze a finished geo experiment or regional holdout from a CSV of KPI by region and day. Estimates the incremental effect with an interval, incremental CPA or ROAS, and runs robustness checks. Use when the user has run a geo test, regional go-dark, brand search blackout by region, or heavy-up and wants the result.
---

# Geo test readout

Estimates the effect of a geo experiment with the bundled script and reports it in a form a team can decide on.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

- The CSV with the KPI by geo and day, covering the pre-period and the test (and cooldown). Spend by geo if available, value if available.
- Treated geos, test start, and the last day to measure (end of cooldown).
- Test type, and the test plan if one exists.

Ask for whatever is missing. If there is a test plan, use its treated list, dates and decision rule exactly.

## Steps

1. Run `python scripts/geolift.py profile --data <file>` and check that the treated geos exist and the dates cover the window.
2. Run `python scripts/geolift.py readout --data <file> --treated <geos> --start <date> --end <date> --type <type> --out readout`.
   - Add `--exclude-controls` for neighboring geos with spillover risk if the plan named a buffer.
3. Read `references/reading-results.md` and apply it:
   - Report effect, lift and interval from `primary`. Note `interval_kind`.
   - Compare with `secondary` (the other estimator). Disagreement means a fragile result.
   - Go through `checks` and `warnings`, and say what each failed check means.
   - Compute or report iCPA or iROAS from `money`, and set them next to the platform-reported CPA or ROAS if the user has them.
4. Apply the decision rule from the plan. If there was no plan, apply the decision mapping in `references/reading-results.md` and say the rule was set after the fact.
5. Show the chart (`readout.png`) and offer the daily series (`readout_daily.csv`).
6. Write the readout with `assets/readout-template.md`.

## Output

- First line: effect and interval, and what it means for the decision.
- Incremental cost or return against the reported one.
- Robustness table.
- Limits: what the result does not cover.
- Next step.

## Rules

- Never report a point estimate without its interval.
- An interval that includes zero is not proof of no effect. Give the MDE context.
- Do not rerun with different dates, geos or methods until the result looks better. If a change is justified (a tracking outage, a geo that leaked spend), make it once, say why, and report both versions.
- A go-dark with spend leakage in treated geos underestimates the effect; report the leakage.

## Scripts and references

- `scripts/geolift.py`, documented in `references/script-reference.md`.
- If code execution is not available, give the user the exact command to run locally.
