---
name: iso27001-gap-assessment
description: Use when the user asks to assess ISO 27001:2022 policies, procedures, records, screenshots, exports, or other evidence for gaps, readiness, or audit preparation.
---

# Compliance Gap Hunter

Perform an evidence-scoped ISO 27001:2022 gap assessment. Produce a defensible
working report, not a certification decision.

## Scope and safety boundaries

- Assess only material supplied by the user or an explicitly provided authoritative reference.
- Never invent a clause number, Annex A control number, title, or requirement.
- If the exact mapping is not supported, label it `unverified mapping` and request the authoritative source.
- Treat missing, inaccessible, stale, ambiguous, simulated, or contradictory evidence as unverified; never treat it as proof of non-compliance or compliance.
- Do not claim certification, conformity, audit completion, legal compliance, or operating effectiveness from documents alone.
- Do not expose secrets, credentials, tokens, unnecessary personal identifiers, or confidential material in the report.

## Evidence model

For every finding, preserve an evidence pointer: filename, section, page, record ID,
timestamp, or short quoted fragment. Use stable IDs such as `CGH-001`.

Classify evidence as:

- `verified`: directly supplied, attributable, current enough for scope, and consistent.
- `partially verified`: some required elements are present but material elements are missing or ambiguous.
- `unverified`: asserted, inaccessible, stale, simulated, or dependent on an untested assumption.
- `contradicted`: supplied evidence conflicts; cite both sources and do not silently resolve it.

## Keep gap categories separate

1. `document_gap`: required policy, procedure, scope, objective, responsibility, criterion, record format, or documented information is absent or incomplete.
2. `implementation_gap`: documentation or an assertion exists, but deployment or operating practice is not shown.
3. `operating_effectiveness_gap`: implementation is evidenced, but recurring records, sampling, monitoring, review, results, or corrective action do not demonstrate that the process works over time.
4. `mapping_or_evidence_gap`: exact requirement mapping or source is not established. Do not convert this into a substantive control failure.

## Assessment method

1. Inventory supplied artifacts and state scope, exclusions, evidence date and limitations.
2. Extract only explicit requirements, identifiers, claims, records, approvals, timestamps, owners and review results.
3. Map evidence only when the mapping is supported; otherwise use `unverified mapping`.
4. Test design/documentation, implementation and operating effectiveness separately.
5. Record positive evidence and distinguish `verified`, `prepared but unverified`, `blocked`, and `not assessed`.
6. Assign practical priority (`critical`, `high`, `medium`, `low`, or `observation`) with a plain-language basis.
7. End with the smallest evidence requests and an action plan that states closure evidence.

## Required report

```markdown
# ISO 27001:2022 Evidence-Scoped Gap Assessment

## Status
- Overall assessment status:
- Assessment scope:
- Evidence reviewed:
- Evidence date / freshness:
- Exclusions and limitations:
- Standard source and mapping confidence:

## Executive summary

## Findings
| ID | Category | Requirement/control mapping | Conclusion | Evidence pointer | Evidence quality | Priority | Closure evidence |
|---|---|---|---|---|---|---|---|

## Positive evidence

## Uncertainty and blockers

## Evidence request list

## Audit-ready action plan
| Action | Owner | Target evidence | Dependency | Acceptance condition |
|---|---|---|---|---|

## Assessor notes
```

## Evidence interpretation rules

- A policy supports design/documentation claims only. It does not prove implementation or operating effectiveness.
- A configuration or deployment record may support implementation, but recurring records and review results are still needed for effectiveness.
- If evidence conflicts, create a contradiction finding and cite both sources.
- If the user provides only narrative, provide a preliminary assessment and evidence request list; do not fabricate a complete matrix.
