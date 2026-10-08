<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Module: 042 | Title: Historical Data Normalization -->

## PART IX - MODEL BUILDING | MODULE 042

# Historical Data Normalization

> Mission. Recast reported data into consistent periods, segments, KPIs, and economic definitions.

## Decision output

Objective: Recast reported data into consistent periods, segments, KPIs, and economic definitions. The completed work product must be reproducible from evidence, show the downstream financial or decision effect when material, state the strongest contrary case, and define a dated update rule.

## Explicit operating procedure

1. Build a reported historical layer exactly as filed before creating any normalized series. Preserve amendments and document which filing version is authoritative.

1. Create a mapping from filing rows/footnotes and XBRL concepts to model rows, including units, signs, fiscal period, segment, and scope.

1. Bridge acquisitions, divestitures, discontinued operations, fiscal-year changes, stock splits, segment reorganizations, accounting-standard adoption, and definition changes.

1. Normalize nonrecurring items only in a separate layer, preserving both GAAP/reporting history and the analyst adjustment with rationale.

1. Reconcile segment totals, KPI history, share count, cash, debt, and equity to consolidated statements and footnotes.

1. Use the normalized history to calculate driver relationships only after confirming the series is comparable over time.

## Required evidence and model bridge

- Primary-source set: normalized historicals, KPI bridges, driver assumptions, debt/share schedules, source notes. Preserve exact document/version, date, period, and source location for every material factual input used in historical data normalization.

- For each key concept - reported history, restatements, recasts, M&A, discontinued ops, FX - state whether it is a reported fact, analyst calculation, management claim, external estimate, or judgment. Quantitative concepts must retain raw components and units; qualitative concepts must retain the specific evidence and counterevidence.

- Map only economically relevant findings into the model or decision record. Process-control modules such as historical data normalization may have no direct valuation line; in that case document the downstream error or governance risk the control prevents.

## Metrics and calculation controls

| Metric / concept | Construction | Required validation |
| --- | --- | --- |
| normalization bridge | Reported historical metric plus/minus explicitly itemized accounting, one-time, acquisition, FX, and definition adjustments to reach the normalized series. | normalization bridge: Tie opening/closing balances or total change to primary-source financials; verify components sum exactly with no overlap, omission, or sign error. |
| organic growth | organic growth = current period / comparable prior period - 1; decompose organic, price, volume, mix, FX, and M&A where material. | organic growth: Recalculate organic growth from cited inputs; reconcile definition, period, units, signs, and source version; investigate and document any variance before use. |
| history integrity | % of historical periods that tie to filed/reported data after restatements and definition changes, with zero unexplained gaps in material series. | history integrity: Recalculate independently from cited source data; verify definition, period, units, scope, signs, and any reconciliation to reported financial or operating totals. |



## Historical normalization laboratory

- Create a reported layer that exactly matches filings before creating an adjusted layer. Never overwrite reported history with analyst normalization.

- Bridge acquisitions, divestitures, discontinued operations, fiscal-calendar changes, segment reorganizations, stock splits, accounting-standard adoption, and definition changes explicitly.

- Preserve a mapping table from each modeled row to filing statement/footnote and source date so another analyst can reproduce the history.

## Worked application

> Case: segment definitions change after an acquisition and only two years are recast.

- Reconstruct the relevant reported fact from primary evidence before interpreting the case. For historical data normalization, show the raw components rather than only the resulting ratio or narrative.

- Build the causal chain through reported history, restatements, recasts, M&A, then identify which link is directly observed and which link remains an assumption.

- Calculate normalization bridge, organic growth, history integrity from sourced components under the reported/base interpretation and at least one skeptical alternative interpretation.

- Translate the difference between cases into the variable that matters for historical data normalization: evidence quality, revenue, operating profit/NOPAT, free cash flow, invested capital, financing/dilution, risk, or valuation. Mark non-applicable links instead of inventing them.

- Expert consistency test: preserve raw reported history and make every normalization reversible.

- Precommit the specific future filing, KPI, customer/supplier observation, regulator action, or market input that would materially invalidate the historical data normalization conclusion.

## Failure tests

- FAIL if reported history cannot be defined and reproduced from the source pack.

- FAIL if reported history is overwritten by adjusted data or comparability changes are made without a reversible bridge to original filings.

- FAIL if the historical data normalization conclusion depends on an unstated assumption, unreconciled definition, or evidence that cannot be traced to its source/version.

- FAIL if evidence materially inconsistent with the historical data normalization conclusion is omitted, reclassified, or dismissed without a documented definition, materiality, causal, timing, and source-quality analysis.

## Completion test

A senior reviewer must be able to reproduce the historical data normalization conclusion, vary the most sensitive assumption independently, trace the change through the model, understand the strongest opposing case, and identify the next evidence that would force an update. If any link is missing, the module remains open.
