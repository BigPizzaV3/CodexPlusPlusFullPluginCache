---
name: full-company-initiation
description: Use to full institutional public-company initiation research and complete underwriting. Produces a source-traceable workflow with deterministic calculations, explicit open gates, and an auditable decision layer.
---

# Full Company Initiation

Use this workflow only when it matches the user's requested scope. The original manual in ../../canonical is authoritative and must not be condensed away.

## Read first

- ../../references/v2/source-policy.md
- ../../references/v2/evidence-system.md
- ../../references/v2/state-and-gates.md
- ../../references/v2/audit-protocol.md
- ../../references/v2/confidence-scoring.md when scoring confidence
- ../../references/v2/research-budget-evoi.md for deep prioritization

## Canonical routing

- M001-M070
- primary M071-M106 sector playbook
- Appendices A-M
- applicable Master Labs 01-14

## Required workflow gates

1. scope and cutoff
2. mandatory live source set
3. historical reconstruction
4. driver model
5. valuation and reverse DCF
6. risk and red team
7. all audits
8. Appendix M

Use the schemas in ../../schemas/v2, applicable deterministic scripts in ../../scripts, and the relevant sector model in ../../sector-models. For a current company, browsing and primary-source retrieval are mandatory. Classify each material statement, retain contrary evidence, and state the research cutoff. Run ../../scripts/research_audit.py before a completion claim. Failed mandatory gates require RESEARCH INCOMPLETE, with the missing evidence and decision impact named explicitly.

Do not execute securities transactions or present research confidence as a guarantee of investment outcome.
