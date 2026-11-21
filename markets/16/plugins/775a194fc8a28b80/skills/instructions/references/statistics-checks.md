# Statistical appraisal and effect interpretation

## Extraction before analysis
Check study design, n randomized/enrolled/analyzed, exclusions and loss-to-follow-up, unit of analysis (person, site, sample, episode), endpoint scale, time horizon, allocation ratio, subgroup definitions, denominators, missingness, paired/cluster/repeated measures and duplicate observations. Do not silently treat person-years or repeated episodes as individual participants.

## Frequent statistical mismatches
- Outcome and estimand vs statistical model; adjusted vs unadjusted; baseline imbalances and confounding.
- Continuous outcomes: mean (SD) vs median (IQR), distribution, change-score assumptions and paired nature of data.
- Binary outcomes: absolute risks, risk difference (RD), risk ratio (RR), odds ratio (OR), context of baseline risk; OR is not a RR for common outcomes.
- Time-to-event: hazard ratio (HR) interpretation, censoring assumptions, proportional hazards, competing risks; do not call HR a risk ratio.
- Diagnostic tests: 2x2 counts, sensitivity, specificity, LR+/LR− and predictive values conditional on prevalence, verification/reference-standard bias, confidence intervals.
- Meta-analysis: effect scale and direction, heterogeneity/tau²/I² interpretation, prediction intervals when appropriate, small-study effects and selection/publication bias limitations, sensitivity analysis.
- Multiple testing: primary vs post hoc, multiplicity, overinterpretation of nominal p values, unplanned subgroup claims, data-derived cutoffs.
- CIs: distinguish estimation precision from statistical significance; wide CI may admit harm and benefit. Never interpret “not significant” as equivalence.
- Sample size: distinguish reported sample size planning from achieved precision and power; do not use post-hoc observed power as a substitute for uncertainty intervals.
- Causal inference: confounding, reverse causation, immortal-time bias, selection bias, positivity and target-trial emulation as appropriate.

## Calculating from user-provided data
Calculate only with an available and permitted computation tool or transparent manually verified arithmetic. Record numerator and denominator and show formula, assumptions and any rounding. Use appropriate confidence intervals and continuity handling for zero cells; avoid naive normal approximations for sparse counts. Verify 2x2 cell conventions before reporting test accuracy. Do not invent an unreported standard error, correlation for paired samples, SD, adjusted model, missing imputation method or raw row-level data.

## Reporting a suspected error
Use one row per issue: **where found → observed numbers/text → cross-check or recomputation → consequence → requested clarification**. Confidence codes: confirmed arithmetic inconsistency, likely methodological concern, insufficient detail, or not assessable. Never accuse authors of misconduct or data fabrication from an isolated inconsistency.

## Examples of defensible cautions
- “P=0.07 alone cannot establish no clinically relevant effect; inspect CI and a prespecified margin.”
- “The model reports adjusted OR while the conclusion states a risk reduction; effect-scale correction is required.”
- “Sensitivity in the manuscript is not reproducible because TP/FN cells are unavailable.”
