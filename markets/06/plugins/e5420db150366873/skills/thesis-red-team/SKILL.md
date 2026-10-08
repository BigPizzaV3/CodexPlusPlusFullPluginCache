---
name: thesis-red-team
description: Use to independently challenge a long or neutral thesis without defending the base case. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Thesis Red Team

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M004
- M021-M025
- M031-M040
- M061-M065
- Appendix D

## Required workflow gates

1. steelman thesis
2. attack evidence lineage
3. attack accounting and forecast assumptions
4. alternative causal model
5. liquidity and valuation vulnerabilities
6. ranked unresolved objections
7. required thesis response

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
