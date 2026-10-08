---
name: risk-decision
description: Use for risk registers, balance-sheet stress, liquidity and covenant analysis, research sizing inputs, pre-mortems, decision journals, post-mortems, and error taxonomy.
---

# Risk and Decision Process

Use this skill when the request matches the description above. Explicit user instructions determine scope and output format. Do not silently weaken source, calculation, falsification, or completion controls required by the loaded manual references.

## Mandatory references

- Modules: M061, M062, M063, M064, M065
- Appendices: None
- Master Labs: Master Lab 09
- Operating rules: `references/operating-rules.md`

The bundled DOCX is the canonical methodology. The Markdown files in `references/` are retrieval-oriented mirrors generated from that source. If an extracted reference appears malformed or ambiguous, consult the canonical DOCX when available rather than inventing missing content.

## Risk workflow

1. Build risk chains, not a generic risk list. Each material risk needs an event, transmission mechanism, exposed metric, leading indicator, time horizon, severity or range, model line, mitigant, and thesis-break threshold.
2. Stress operating drivers first, then working capital, liquidity, covenants, refinancing, dilution, and valuation.
3. Use `scripts/finance_engine.py` for deterministic liquidity and scenario aggregation when definitions match.
4. Model correlated risks coherently rather than adding isolated worst cases.
5. Preserve a dated decision journal and state what future evidence changes the base, bear, stress, or thesis-break state.

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
