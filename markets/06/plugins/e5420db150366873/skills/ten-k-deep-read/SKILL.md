---
name: ten-k-deep-read
description: Use to perform a complete 10-K and footnote deep read with cross-filing comparisons. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Ten K Deep Read

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M006-M007
- M011-M025
- Appendices D-E

## Required workflow gates

1. document identity and amendments
2. statement and footnote map
3. accounting policy changes
4. commitments and contingencies
5. risk-factor and disclosure drift
6. numerical reconciliation
7. open questions

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
