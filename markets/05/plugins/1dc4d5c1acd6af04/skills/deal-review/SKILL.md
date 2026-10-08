---
name: deal-review
description: Use when a concrete material offer or proposed agreement is being considered for acceptance, especially where targets, BATNA, liability, future obligations, pre-commitment criteria, or implementation risk matter.
---

# Independent Deal Review

## Overview

Test a material offer independently before the orchestrator recommends acceptance. The research basis is Freeman's I FORESAW IT offer tests, Measures of Success and 2026 Deal Dashboard pre-commitment concept. [F03][F07][F08]

**Interface:** accept a versioned specialist request and return `schemas/DEAL_REVIEW_RESULT.md`.

## Independence rule

Review the offer against the canonical criteria, not the orchestrator's enthusiasm, negotiating effort, sunk cost or desire for closure. Agreement itself is not success. [F07]

## Tests

Run each relevant test transparently:

1. **Interests** — does the offer serve critical user interests?
2. **BATNA** — is it better than the realistic alternative on current evidence?
3. **Independent criteria** — can important terms be defended against credible external standards?
4. **Hidden time bombs** — are there ambiguous future obligations, dependencies or latent risks?
5. **Priority topics** — are critical/high-priority TTT outcomes acceptable?
6. **Relationship** — is the required working relationship viable?
7. **Implementation** — can the agreement actually be delivered/enforced as understood?
8. **Pre-commitment** — does it satisfy criteria recorded before deal momentum? [F08]

If material information is missing, use `INSUFFICIENT_INFORMATION` rather than guessing.

For each test, a `PASS` requires affirmative supplied evidence supporting that test. If its material evidence is not supplied, mark it `UNKNOWN` (`NOT_APPLICABLE` only where the schema permits and non-applicability is established). Absence of an identified failure is not evidence of a pass. If an unresolved `UNKNOWN` can change acceptance, the overall gate is `INSUFFICIENT_INFORMATION`.

## Gate

Return only:
- `PASS` — no unresolved critical failure;
- `CONDITIONAL` — potentially acceptable if explicit conditions are resolved;
- `FAIL` — at least one critical criterion fails;
- `INSUFFICIENT_INFORMATION` — a material acceptance question cannot be assessed.

A critical-topic failure can outweigh gains on several lower-priority topics. Do not use arbitrary percentages, utility totals or a pseudo-scientific Freeman/Deal Dashboard score.

## Safeguards

- Self-asserted “fairness” is not independent criteria.
- Do not silently change targets, BATNA or pre-commitment criteria to make the deal pass.
- A later user override does not relabel the original `FAIL` as `PASS`.
- Counter-package design belongs to F02; final wording to F07.
- The 2026 Deal Dashboard is decision discipline, not a validated predictive algorithm. [F08]

## Stop condition

Stop when the offer has a supported gate result and all critical conditions/unknowns are explicit.
