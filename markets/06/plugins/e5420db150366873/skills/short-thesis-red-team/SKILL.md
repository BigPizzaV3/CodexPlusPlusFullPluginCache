---
name: short-thesis-red-team
description: Use to challenge a proposed short thesis, identify squeeze and timing risks, and separate bad business from bad short. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Short Thesis Red Team

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
- M053-M055
- M061-M065

## Required workflow gates

1. borrow and catalyst assumptions
2. liquidity and solvency distinction
3. bull-case disconfirmation
4. crowding and timing
5. refinancing and strategic options
6. valuation asymmetry
7. thesis breaks

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
