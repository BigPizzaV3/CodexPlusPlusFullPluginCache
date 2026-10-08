---
name: peer-comparison
description: Use to build a definition-normalized operating, accounting, valuation, and risk peer comparison. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Peer Comparison

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M034
- M042
- M047
- sector playbooks

## Required workflow gates

1. peer rationale
2. definition register
3. accounting and calendar normalization
4. KPI comparison
5. valuation bridge
6. quality and risk adjustments
7. outliers and caveats

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
