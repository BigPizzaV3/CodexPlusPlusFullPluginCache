---
name: valuation
description: Use for DCF, multiples, reverse DCF, market-implied expectations, sum-of-the-parts, valuation sensitivities, scenarios, and probability weighting.
---

# Valuation

Use this skill when the request matches the description above. Explicit user instructions determine scope and output format. Do not silently weaken source, calculation, falsification, or completion controls required by the loaded manual references.

## Mandatory references

- Modules: M046, M047, M048, M049, M050
- Appendices: Appendix C
- Master Labs: Master Lab 03, Master Lab 14
- Operating rules: `references/operating-rules.md`

The bundled DOCX is the canonical methodology. The Markdown files in `references/` are retrieval-oriented mirrors generated from that source. If an extracted reference appears malformed or ambiguous, consult the canonical DOCX when available rather than inventing missing content.

## Valuation workflow

1. Establish a clean valuation date, market capitalization or enterprise-value bridge, diluted share count, and capital structure.
2. Read all bundled valuation references before choosing methods.
3. Use operating-driver forecasts underneath intrinsic valuation. Normalize peer definitions before relative valuation.
4. Use at least two economically appropriate methods for deep work and include reverse expectations when public market price is available.
5. Run deterministic valuation math in `scripts/finance_engine.py` where applicable. Reconcile enterprise-to-equity adjustments and dilution.
6. Present scenario ranges, key sensitivities, market-implied assumptions, and the evidence that would falsify the valuation thesis.

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
