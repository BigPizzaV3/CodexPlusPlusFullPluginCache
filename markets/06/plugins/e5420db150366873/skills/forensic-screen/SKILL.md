---
name: forensic-screen
description: Use to run an accounting-forensics and earnings-quality screen before deeper underwriting. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Forensic Screen

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M011-M025
- Appendix D
- Master Lab 04

## Required workflow gates

1. source and period normalization
2. accruals and cash conversion
3. Beneish diagnostics
4. working-capital anomalies
5. non-GAAP and estimate review
6. disclosure drift
7. false-positive review

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
