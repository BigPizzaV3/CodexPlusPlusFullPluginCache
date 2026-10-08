<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Module: 041 | Title: Model Architecture and Standards -->

## PART IX - MODEL BUILDING | MODULE 041

# Model Architecture and Standards

> Mission. Build models that are transparent, auditable, modular, scenario-ready, and resistant to hard-coded errors.

## Decision output

Objective: Build models that are transparent, auditable, modular, scenario-ready, and resistant to hard-coded errors. The completed work product must be reproducible from evidence, show the downstream financial or decision effect when material, state the strongest contrary case, and define a dated update rule.

## Explicit operating procedure

1. Design the workbook/data model in a one-way flow from sources and historicals to assumptions, operating schedules, integrated statements, scenarios, valuation, dashboard, and checks.

1. Separate reported data, analyst normalization, forecast assumptions, formulas, and outputs visually and structurally. Every material input needs source/date/comment.

1. Use dedicated schedules for revenue drivers, costs, fixed assets, working capital, debt/interest, taxes, shares/dilution, acquisitions, and other material mechanics.

1. Eliminate unexplained plugs and accidental circularity. Document intentional circular calculations and use algebraic or controlled iterative solutions where necessary.

1. Build visible error checks for statement balance, cash roll-forward, segment totals, share roll-forward, debt maturities, signs/units, scenario selection, and stale inputs.

1. Optimize for auditability and change control, not clever formula compression. A reviewer should trace any output to its source and assumption quickly.

## Required evidence and model bridge

- Primary-source set: normalized historicals, KPI bridges, driver assumptions, debt/share schedules, source notes. Preserve exact document/version, date, period, and source location for every material factual input used in model architecture and standards.

- For each key concept - raw data, normalized history, assumptions, calculations, statements, schedules - state whether it is a reported fact, analyst calculation, management claim, external estimate, or judgment. Quantitative concepts must retain raw components and units; qualitative concepts must retain the specific evidence and counterevidence.

- Map only economically relevant findings into the model or decision record. Process-control modules such as model architecture and standards may have no direct valuation line; in that case document the downstream error or governance risk the control prevents.

## Metrics and calculation controls

| Metric / concept | Construction | Required validation |
| --- | --- | --- |
| unexplained hardcode count | Count of forecast/model cells containing hard-coded values without an identified source, assumption label, or documented rationale. | unexplained hardcode count: Reperform the count from the defined population, inspect every material exception, and confirm the denominator/universe did not change between periods. |
| check coverage | % of material model linkages and outputs covered by automated balance, cash, share-count, debt, tax, scenario, and valuation error checks. | check coverage: Recalculate from same-scope numerator and denominator; confirm period, units, cohort/geography, and issuer definition; reconcile material differences to filings or operating data. |
| trace depth | Number of auditable steps from a decision output back to primary-source data; lower and fully documented is better, with no hidden transformations. | trace depth: Audit a sample back to dated evidence and decision records; verify the stated threshold/score is reproducible by an independent reviewer and tied to a defined decision consequence. |



## Model architecture standard

- Recommended workbook flow: Cover/Control -> Sources -> Historical statements -> KPI/segments -> Assumptions -> Operating forecast -> IS -> BS -> CF -> Debt/interest -> Shares -> Taxes -> Scenarios -> Valuation -> Dashboard -> Checks.

- Inputs must be visually and structurally separated from formulas. Each input needs source/date/comment. Never bury an assumption inside a formula that reviewers cannot identify.

- Add error flags for balance-sheet balance, cash roll-forward, segment-consolidated reconciliation, share roll-forward, debt maturity, circularity, sign conventions, scenario selection, and valuation bridge.

## Worked application

> Case: revenue is hardcoded independently in three places and silently diverges.

- Reconstruct the relevant reported fact from primary evidence before interpreting the case. For model architecture and standards, show the raw components rather than only the resulting ratio or narrative.

- Build the causal chain through raw data, normalized history, assumptions, calculations, then identify which link is directly observed and which link remains an assumption.

- Calculate unexplained hardcode count, check coverage, trace depth from sourced components under the reported/base interpretation and at least one skeptical alternative interpretation.

- Translate the difference between cases into the variable that matters for model architecture and standards: evidence quality, revenue, operating profit/NOPAT, free cash flow, invested capital, financing/dilution, risk, or valuation. Mark non-applicable links instead of inventing them.

- Expert consistency test: one driver should flow through all downstream schedules and outputs.

- Precommit the specific future filing, KPI, customer/supplier observation, regulator action, or market input that would materially invalidate the model architecture and standards conclusion.

## Failure tests

- FAIL if raw data cannot be defined and reproduced from the source pack.

- FAIL if source data, assumptions, formulas, outputs, scenarios, and checks are mixed so a reviewer cannot trace or safely change the model.

- FAIL if the model architecture and standards conclusion depends on an unstated assumption, unreconciled definition, or evidence that cannot be traced to its source/version.

- FAIL if evidence materially inconsistent with the model architecture and standards conclusion is omitted, reclassified, or dismissed without a documented definition, materiality, causal, timing, and source-quality analysis.

## Completion test

A senior reviewer must be able to reproduce the model architecture and standards conclusion, vary the most sensitive assumption independently, trace the change through the model, understand the strongest opposing case, and identify the next evidence that would force an update. If any link is missing, the module remains open.
