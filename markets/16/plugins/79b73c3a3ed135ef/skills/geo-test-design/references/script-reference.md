# geolift.py reference

Self-contained Python (numpy, pandas, scipy; matplotlib optional for charts). Run from the skill folder:

```bash
python scripts/geolift.py <command> --data file.csv [options] --out results/name
```

Each command prints JSON to stdout. With `--out`, it also writes `name.json` and `name.md`, and for readout a chart `name.png` and a daily series `name_daily.csv`.

## Commands

| Command | Use | Key options |
|---|---|---|
| profile | Check a geo panel before anything else | `--exclude` geos to drop |
| quick | Size a test from summary numbers | `--baseline-per-day`, `--residual-cv`, `--autocorrelation`, `--days` |
| design | Choose treated geos, MDE, duration curve, cost | `--test-days`, `--type go_dark|holdback|heavy_up`, `--intensity`, `--treated-share`, `--must-treat`, `--never-treat`, `--treated` (evaluate a fixed group), `--draws`, `--method tbr|sc`, `--alpha`, `--power`, `--seed` |
| readout | Estimate the effect of a test that ran | `--treated`, `--start`, `--end` (include cooldown), `--type`, `--method`, `--exclude-controls`, `--conf`, `--in-space-draws` |
| prepost | Directional before/during comparison on one series | `--start`, `--end`, `--control-col`, `--weeks`, `--exclude-windows` |
| switchback | Alternating on/off blocks in one market | `--off-periods start:end ...`, `--start`, `--end`, `--washout-days` |

## Methods

- **TBR** (time-based regression, Kerman, Wang and Vaver 2017): treated aggregate regressed on control aggregate in the pre-period, with a non-negative slope as in Meridian GeoX; the fit predicts the counterfactual during the test. Default primary method: simple, stable, and well calibrated in our simulations.
- **SC** (synthetic control, Abadie, Diamond and Hainmueller 2010): weighted combination of individual control geos, with intercept, non-negative weights and a ridge penalty chosen by rolling-origin validation. Reported as the secondary method; if TBR and SC disagree, the result is fragile.
- **In-time placebos**: the estimator applied to past windows of the same length, where no change happened. Their errors give the interval and `p_in_time`. They absorb autocorrelation and model misfit, which the textbook TBR interval ignores.
- **In-space placebos**: fake treated groups of the same size drawn from control geos with the same stratified rule (the approach of Abadie et al. 2010 and Meridian GeoX). Gives `p_in_space`.
- **Short histories**: with fewer than 10 placebo windows, the interval is the wider of the placebo-based one and an AR(1)-corrected parametric one (`interval_kind: short_history_conservative`).
- **Design search**: stratified random draws of treated geos; each is scored on older placebo windows, and the best is re-scored on the most recent windows it was not chosen on (`mde_pct_validation`). Plan on the validation number.

## Validation

See `validation.md` in this folder. It reports the false positive rate in A/A tests, coverage of the true effect, and power at the predicted MDE. Panels are simulated with autocorrelated shocks and Poisson noise.

## Main output fields

Design: `recommended.treated`, `recommended.mde_pct_validation`, `recommended.kpi_share`, `recommended.pre_fit.r2`, `duration_curve[]`, `cost.*`, `alternatives[]`, `warnings[]`.

Readout: `primary.effect`, `primary.lift`, `primary.interval_lift`, `primary.interval_kind`, `primary.p_in_time`, `primary.p_in_space`, `secondary.lift`, `significant`, `money.icpa`, `money.iroas`, `money.spend_delta`, `checks[]`, `warnings[]`.

Prepost: `comparators[].change_pct`, `comparators[].noise_band_90_pct`, `comparators[].share_of_history_with_bigger_move`, `verdict`.

Switchback: `effect_pct_when_off`, `permutation_p`, `min_possible_p`, `blocks[]`.
