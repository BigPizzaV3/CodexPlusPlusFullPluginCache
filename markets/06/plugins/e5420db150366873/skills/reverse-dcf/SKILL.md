---
name: reverse-dcf
description: Use to solve for market-implied operating expectations and test their plausibility. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Reverse Dcf

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M046-M050
- Appendix C
- Master Labs 03 and 14

## Required workflow gates

1. valuation-date EV bridge
2. clean cash-flow definition
3. solve implied growth or margin
4. translate into operational requirements
5. history and peer comparison
6. variant and falsification

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
