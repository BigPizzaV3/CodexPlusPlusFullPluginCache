---
name: results-and-statistics
description: Extract outcomes, timepoints, numerical results, effect estimates, confidence intervals, p-values, statistical methods, and adverse events. Use when interpreting research results or calculating explicitly requested derived values.
---

# Results and statistics

Start from the exact supplied paper/table/figure. Apply `../research-data-extraction/references/statistical-rules.md` and the shared quality checks. Extraction is not independent statistical reanalysis unless requested.

## Define the result record

Before copying a number, identify: outcome and author-declared priority; definition/tool/unit; timepoint; group or contrast; analyzed denominator; analysis population (e.g., ITT/per-protocol); adjusted status/covariates; measure type; estimate and uncertainty; source location.

Create distinct records whenever outcome, timepoint, group/contrast, subgroup, analysis population, or adjustment changes. Keep baseline measurements separate from post-baseline outcomes. Separate primary, secondary, exploratory, safety, and patient-reported outcomes.

## Preserve statistical values

Record exactly what is reported: continuous (mean, median, SD, SE, IQR, range, difference); binary (events/total, RR, OR, risk difference); time-to-event (HR, CI, events, median survival, follow-up); diagnostic (sensitivity, specificity, PPV, NPV, AUC, TP/FP/TN/FN); ordinal/count/other named measures. Preserve inequality signs in p-values, CI limits, decimal precision, unit, denominator and model name. Do not convert measures unless asked.

## Interpret carefully

- A p-value above a threshold does not prove no effect; a low p-value does not establish clinical importance.
- Do not describe observational association as causation without design-appropriate support.
- Do not blend subgroup with overall findings or adjusted with unadjusted estimates.
- If text and tables conflict, present both with locations; do not select silently.
- Treat absent outcome values as `NR`, not zero.

## Calculations

Only calculate when asked and inputs are sufficient. Show formula/input and label the result `CALCULATED_FROM_REPORTED_DATA`; keep source-reported values separate. If ambiguity, rounding, denominator, model assumptions, or units make the result non-unique, ask or mark `UNCLEAR` instead of manufacturing precision.

## Suggested result table

| Outcome/status | Timepoint | Group/contrast | Analysis population / adjustment | N | Measure and estimate | CI / p-value | Source |
|---|---|---|---|---:|---|---|---|
