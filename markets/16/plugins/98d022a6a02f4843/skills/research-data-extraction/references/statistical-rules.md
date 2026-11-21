# Statistical extraction rules

## Preserve, do not normalize away

- Record exact estimate, measure name, units, group/contrast, analysis population, timepoint, adjustment status, CI limits, p-value and inequality sign, sample denominator, and location.
- Distinguish mean from median; SD from SE; IQR from range; count from percentage; absolute from relative effect; crude from adjusted model; and point estimate from interval.
- Keep the authors' precision. Do not round, convert, reconstruct, or replace values unless asked. Note when a confidence level is not explicit.
- Never infer a zero from omitted outcome data or assume a p-value threshold establishes no effect or clinical importance.

## Measure families to recognize

- Continuous: mean/SD, mean/SE, median/IQR, range, mean difference, standardized mean difference.
- Binary: events/total, risk ratio, odds ratio, risk difference, and reported absolute/relative percentages.
- Time-to-event: hazard ratio, CI, event count, median survival, follow-up duration; keep censoring/analysis notes if reported.
- Diagnostic accuracy: sensitivity, specificity, PPV, NPV, AUC, TP/FP/TN/FN; preserve threshold, reference standard, and denominator when available.
- Count/ordinal/other: retain the source's named model and scale; do not coerce to a binary/continuous measure.

## Separate result records

Never mix different outcomes, follow-ups, groups, subgroup and overall estimates, ITT and per-protocol populations, or adjusted and unadjusted results. Each distinct result receives its own row and source location. If a paper reports different analysis populations across sections, record them separately and flag apparent conflicts.

## Calculations only on request

Default: do not derive unreported statistics. When explicitly requested and inputs are sufficient, label every derived value `CALCULATED_FROM_REPORTED_DATA`, show formula/inputs and any assumptions, retain the author-reported value separately, and check denominator, units, rounding, and compatibility. Potentially allowed calculations include event percentage from events/denominator, mean difference, compatible unit conversion, risk ratio, odds ratio, risk difference, and simple confidence-related calculations only when assumptions and inputs are valid. If the calculation cannot be uniquely determined, ask or mark `UNCLEAR`; never back-solve a precise participant count from a rounded percentage unless the permitted bounds are demonstrable and clearly labeled as an estimate.

## Interpretation boundary

Report what the authors say and what the numerical result shows as distinct fields. Do not call a result clinically important or causal solely because it is statistically significant. For observational evidence, describe associations as associations unless the design and justified causal analysis support stronger wording.
