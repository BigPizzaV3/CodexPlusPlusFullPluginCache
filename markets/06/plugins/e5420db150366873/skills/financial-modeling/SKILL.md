---
name: financial-modeling
description: Use for historical normalization, revenue driver forecasts, margin forecasts, integrated balance sheet and cash flow modeling, scenarios, model architecture, and model QA.
---

# Financial Modeling

Use this skill when the request matches the description above. Explicit user instructions determine scope and output format. Do not silently weaken source, calculation, falsification, or completion controls required by the loaded manual references.

## Mandatory references

- Modules: M041, M042, M043, M044, M045
- Appendices: Appendix B, Appendix C
- Master Labs: Master Lab 02, Master Lab 14
- Operating rules: `references/operating-rules.md`

The bundled DOCX is the canonical methodology. The Markdown files in `references/` are retrieval-oriented mirrors generated from that source. If an extracted reference appears malformed or ambiguous, consult the canonical DOCX when available rather than inventing missing content.

## Modeling workflow

1. Read the operating rules and all bundled module references before building or changing a material model assumption.
2. Normalize historical definitions and periods before forecasting.
3. Forecast economic drivers first, then statements, cash, financing, and share count.
4. Use explicit scenario switches and preserve historical actuals.
5. Run deterministic calculations in `scripts/finance_engine.py` where applicable and reconcile results to sourced values.
6. Apply model-break tests from the references. Any hidden hard code, broken roll-forward, unexplained circularity, or non-reconciling statement is a failure.
7. Finish with assumptions, checks, sensitivities, model-change log, and unresolved modeling risks.

## Evidence and output controls

- Distinguish reported facts, management claims, external estimates, analyst calculations, and analyst judgments.
- For current claims, verify freshness and state the as-of date.
- Cite material factual inputs to the actual source used.
- Recalculate important arithmetic rather than copying unexplained outputs.
- State unresolved questions and the strongest contrary case.
- Define specific falsification or thesis-break evidence for material conclusions.
- Do not execute securities transactions.

## V2 live-research and audit controls

For current-company work, read ../../references/v2/source-policy.md before research. Deep work must also use ../../references/v2/evidence-system.md, ../../references/v2/state-and-gates.md, and ../../references/v2/audit-protocol.md. Use the V2 schemas and deterministic scripts where applicable. Do not claim completion while a mandatory dependency, material contradiction, stale critical input, or unreconciled calculation remains open.
