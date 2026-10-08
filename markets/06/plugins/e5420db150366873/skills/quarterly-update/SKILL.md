---
name: quarterly-update
description: Use to update an existing thesis, model, evidence graph, and valuation after a quarter. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Quarterly Update

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M008
- M042-M052
- M061-M068
- Appendix I

## Required workflow gates

1. load prior state
2. retrieve new filings and earnings materials
3. definition and restatement diff
4. forecast error attribution
5. model and valuation update
6. thesis delta
7. audits

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
