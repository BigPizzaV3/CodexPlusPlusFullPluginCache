# Choosing statistical methods responsibly

## Frame the problem first
Specify study design, unit/independence, exposure/outcome scales, estimand, number of groups, missing data, sample size, clustering and any pre-specified plan. Do not choose a test by name similarity. This is a teaching map, not automated statistical certification.

| Scenario | Candidate approach (when assumptions fit) | Check carefully |
|---|---|---|
| Independent continuous outcome, two groups | Estimate mean difference with 95% CI; Welch t-test for suitable conditions; robust/nonparametric method for skew/ordinal data as justified | Sampling design, shape, outliers, unequal variance; nonparametric test targets differ |
| Paired continuous before/after | Paired differences with CI, paired t-test if appropriate; signed-rank or other method as justified | Preserve pairing, difference distribution, time trends and regression to mean |
| >2 groups continuous | Regression/ANOVA or robust alternatives; planned contrasts and multiplicity | Confounding, heteroscedasticity, independent observations |
| Independent binary proportion | Risk difference, risk ratio, odds ratio with CIs; chi-square or exact method if sparse | Counts, zero cells, risk vs odds, denominators and adjustment |
| Matched binary outcome | Paired binary methods such as McNemar, matched regression as appropriate | Discordant pairs, matching |
| Continuous association | Scatterplot, regression, Pearson or Spearman as justified | Nonlinearity, influential outliers, common causes, repeated measures |
| Time-to-event outcome | Kaplan–Meier, Cox model or competing-risk approach if appropriate | Censoring, proportional hazards, competing events and time zero |
| Repeated/clustered data | Mixed effects, GEE or cluster-aware design-specific methods | ICC, small cluster counts, within-subject correlation |
| Multivariable prediction | Transparent model, internal validation, discrimination and calibration | Overfitting, leakage, missingness, transportability, no causal interpretation |
| Diagnostic accuracy | Sensitivity, specificity, likelihood ratios and CIs; 2×2 table/ROC where appropriate | Reference standard, threshold selection, spectrum and verification bias |

## Interpretation pitfalls
- **p-value**: probability under the null/model of results as extreme or more extreme; not P(null true), not effect size and not a proof of clinically relevant differences.
- **95% confidence interval**: uncertainty procedure with nominal long-run coverage under assumptions; not probability that a fixed parameter is in a specific interval.
- **RR = [a/(a+b)] / [c/(c+d)]** and **OR = ad/(bc)** with a=event exposed, b=non-event exposed, c=event control, d=non-event control. These differ especially for common events; never claim OR=RR. For zero cells use a stated method and caveat.
- **NNT** requires an appropriate absolute risk difference, defined population and time horizon; do not compute from OR alone without further justified assumptions.
- **Likelihood ratios**: LR+ = sensitivity/(1-specificity), LR−=(1-sensitivity)/specificity. Distinguish diagnostic test accuracy from prediction scoring.
- **ROC AUC** measures discrimination, not calibration or clinical utility; test-set selection can exaggerate results.
- **Correlation** is not causation. Observational estimates may reflect selection bias, confounding and reverse causality; randomized designs still require attrition/analysis checks.
- **Multiplicity**: many outcomes/subgroups/time points increase risk of false positive findings. Separate exploratory and confirmatory analyses and state whether multiplicity adjustment was pre-specified.

## Missing data and causal claims
- Characterize missingness amount/pattern and assumptions for complete-case, imputation, inverse weighting or sensitivity analyses. Never assert MCAR, MAR or MNAR can be confirmed from a single table.
- Regression adjustment does not automatically establish causality. Pre/post without control should not be framed as an RCT.
- Trial reports: clarify allocation, intention-to-treat versus per-protocol, primary outcome and analysis set. Do not infer actual allocation or trial registration from a label.

## Calculation confidence
- Source (observed values), transformation, formula and units must be traceable. Round as appropriate while retaining precision for intermediate values.
- Simple transparent arithmetic may be done manually if checkable; for statistical inferential procedures that need software, execute with a real tool if available or provide code clearly labeled NOT EXECUTED.
- When providing code, show required packages and input variable names; do not fabricate output or claim to have tested code unless executed.
