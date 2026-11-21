---
name: geo-test-design
description: Design a geo experiment (geo lift, matched market, regional holdout, go-dark, holdback or heavy-up) from a CSV of KPI by region and day. Chooses treated regions, estimates the minimum detectable effect, test length and cost, and writes the test plan. Use when the user uploads or describes geo-level data and wants to set up a test.
---

# Geo test design

Designs a geo experiment from the user's data with the bundled script, then writes a plan the team can approve before launch.

The user's explicit instructions take priority over this guidance. Reply in the user's language.

## Inputs

- A CSV with one row per geo and day: date, geo, KPI, and ideally spend and value. Format in `references/data-format.md`.
- Test type: go-dark, holdback (with the share cut) or heavy-up (with the share added). Default go-dark if the question is "is it incremental"; heavy-up if the question is "should we spend more".
- Test length in days. If unknown, start with 28 and use the duration curve.
- Constraints: geos that must stay on, geos that must be treated, maximum share of KPI at risk.

If the file is missing, ask for it and say exactly what to export. If the file has the wrong shape (wide format, weekly totals only, no geo), reshape it with pandas before running the script. Tell the user what was changed.

## Steps

1. Run `python scripts/geolift.py profile --data <file> --out profile`. Read the warnings. Stop and ask when the panel cannot support a test: fewer than 6 geos, under 8 weeks of history, a geo with over a third of the KPI, broken tracking periods.
2. Run `python scripts/geolift.py design --data <file> --test-days <n> --type <type> [--intensity x] [--treated-share s] [--must-treat ...] [--never-treat ...] --out design`.
   - Default treated share 0.2. Raise it when the MDE is too high and the business accepts more risk.
   - If the user already chose the treated geos, pass `--treated` to evaluate their choice, and also run the search to show the alternative.
3. Read `recommended.mde_pct_validation`, not the selection MDE. Compare it with the effect the decision needs. Use `duration_curve` to propose a length.
4. If the MDE is too large, try in this order: longer test, larger treated share, finer geos, heavy-up instead of holdback. Rerun and report the change.
5. Fill `assets/test-plan-template.md` with the design output and the execution checklist from `references/geo-design-rules.md`, adapted to the platforms in scope.

## Output

- The treated geos, their share of KPI, and the MDE at the proposed length.
- The duration curve as a short table.
- Cost: spend withheld or added, and KPI at risk under two or three plausible effect sizes.
- Warnings from the script, translated into what they mean for this test.
- The filled test plan.
- Keep the seed and the full treated list in the plan: the readout needs them.

## Rules

- Never fabricate data or results. Every number comes from the user's file or the script output.
- Do not present the MDE as the expected effect. It is the smallest effect the test can see.
- The plan is written before launch and not changed after the data comes in.
- Platform settings that matter: Presence-only location targeting in Google Ads, exclusions in every automated campaign type, a freeze on other changes. Include them in the checklist.

## Scripts and references

- `scripts/geolift.py`, documented in `references/script-reference.md`.
- `references/geo-design-rules.md` for test types, units, duration, spillover and execution.
- `references/literature.md` for the methods (TBR, synthetic control, GeoLift, Meridian GeoX) and their published requirements.
- If code execution is not available, give the user the exact commands to run locally.
