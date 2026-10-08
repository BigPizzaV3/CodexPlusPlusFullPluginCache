<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Module: 060 | Title: Alternative Data Validation -->

## PART XII - ALTERNATIVE DATA AND CHANNEL WORK | MODULE 060

# Alternative Data Validation

> Mission. Backtest data against reported outcomes and measure false positives, revisions, survivorship, and coverage bias.

## Decision output

Objective: Backtest data against reported outcomes and measure false positives, revisions, survivorship, and coverage bias. The completed work product must be reproducible from evidence, show the downstream financial or decision effect when material, state the strongest contrary case, and define a dated update rule.

## Explicit operating procedure

1. Write the data-generating process: population, sample, coverage, frequency, revision policy, missingness, survivorship, and how the signal should causally reach a company KPI.

1. Create historical features using only information that would have been available at each date to avoid look-ahead and revision bias.

1. Backtest against reported outcomes over enough periods and regimes to estimate correlation, predictive error, false positives, false negatives, and lead/lag stability.

1. Use holdouts, peer/control groups, and simple baselines before complex models; a signal must beat a naive forecast after transaction/research costs to deserve weight.

1. Track vendor methodology/coverage changes and rerun historical relationships when the dataset changes.

1. Set a retirement rule for signals whose predictive relationship, coverage, or economic mechanism deteriorates.

## Required evidence and model bridge

- Primary-source set: documented datasets, sampling frame, legal/compliance approval, backtests, source provenance. Preserve exact document/version, date, period, and source location for every material factual input used in alternative data validation.

- For each key concept - target KPI, frozen vintages, baseline, train/validation/holdout, robustness, false positives - state whether it is a reported fact, analyst calculation, management claim, external estimate, or judgment. Quantitative concepts must retain raw components and units; qualitative concepts must retain the specific evidence and counterevidence.

- Map only economically relevant findings into the model or decision record. Process-control modules such as alternative data validation may have no direct valuation line; in that case document the downstream error or governance risk the control prevents.

## Metrics and calculation controls

| Metric / concept | Construction | Required validation |
| --- | --- | --- |
| out-of-sample error | Forecast minus realized outcome on holdout periods, summarized with MAE, MAPE/RMSE as appropriate and compared with a simple benchmark. | out-of-sample error: Reperform the count from the defined population, inspect every material exception, and confirm the denominator/universe did not change between periods. |
| incremental explanatory power | Increase in out-of-sample R-squared, reduction in forecast error, or decision accuracy after adding the alternative signal to the baseline model. | incremental explanatory power: Recalculate independently from cited source data; verify definition, period, units, scope, signs, and any reconciliation to reported financial or operating totals. |
| false-positive rate | Negative/normal realized outcomes incorrectly flagged as positive/adverse signals divided by all truly negative/normal outcomes. | false-positive rate: Recalculate from same-scope numerator and denominator; confirm period, units, cohort/geography, and issuer definition; reconcile material differences to filings or operating data. |



## Worked application

> Case: revised vendor history looks predictive but real-time vintages were weak.

- Reconstruct the relevant reported fact from primary evidence before interpreting the case. For alternative data validation, show the raw components rather than only the resulting ratio or narrative.

- Build the causal chain through target KPI, frozen vintages, baseline, train/validation/holdout, then identify which link is directly observed and which link remains an assumption.

- Calculate out-of-sample error, incremental explanatory power, false-positive rate from sourced components under the reported/base interpretation and at least one skeptical alternative interpretation.

- Translate the difference between cases into the variable that matters for alternative data validation: evidence quality, revenue, operating profit/NOPAT, free cash flow, invested capital, financing/dilution, risk, or valuation. Mark non-applicable links instead of inventing them.

- Expert consistency test: approve a signal for production only after vintage-aware out-of-sample validation.

- Precommit the specific future filing, KPI, customer/supplier observation, regulator action, or market input that would materially invalidate the alternative data validation conclusion.

## Failure tests

- FAIL if target KPI cannot be defined and reproduced from the source pack.

- FAIL if a signal is backtested using revised data, look-ahead information, survivor-only samples, or in-sample correlation without false-positive and out-of-sample analysis.

- FAIL if the alternative data validation conclusion depends on an unstated assumption, unreconciled definition, or evidence that cannot be traced to its source/version.

- FAIL if evidence materially inconsistent with the alternative data validation conclusion is omitted, reclassified, or dismissed without a documented definition, materiality, causal, timing, and source-quality analysis.

## Completion test

A senior reviewer must be able to reproduce the alternative data validation conclusion, vary the most sensitive assumption independently, trace the change through the model, understand the strongest opposing case, and identify the next evidence that would force an update. If any link is missing, the module remains open.
