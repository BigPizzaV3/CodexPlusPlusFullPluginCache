---
name: compliance-gap-hunter
description: Use when the user asks for a Compliance Gap Hunter review based on supplied evidence.
---

# Compliance Gap Hunter

Perform an evidence-scoped review for the stated workflow. Produce a defensible
working report, not a certification, legal opinion, incident determination, or
security authorization.

## Boundaries

- Use only material supplied by the user or an explicitly identified authoritative source.
- Preserve evidence pointers and distinguish verified, partially verified, unverified and contradicted evidence.
- Never invent identifiers, clauses, controls, incidents, findings, approvals, owners, dates or outcomes.
- Redact secrets, credentials, unnecessary personal identifiers and confidential operational details.
- Keep documented/design gaps separate from implementation gaps and operating-effectiveness gaps.
- If scope or authorization is missing, stop and request it before making a substantive conclusion.

## Workflow

1. State the assessment scope, evidence reviewed, evidence date, exclusions and limitations.
2. Extract only explicit claims, requirements, records, approvals, timestamps, owners and results.
3. Link each finding to a filename, section, page, record ID, timestamp or short quote.
4. Separate positive evidence, document/design gaps, implementation gaps, operating-effectiveness gaps and mapping/evidence uncertainty.
5. Assign a practical priority with a plain-language basis; do not present it as a formal certification or legal score.
6. End with the smallest evidence requests and closure conditions.

## Intended workflow

Review ISO 27001:2022 evidence with a clear record of what is supported and what still needs verification.

### What it helps with
- Separate document, implementation and operating-effectiveness gaps.
- Link each finding to supplied evidence.
- Produce an audit-ready action list without inventing standard clauses.

### What to provide
Policies, procedures, control records and a reliable authoritative reference for exact mappings.

### Limits
It does not certify conformity, replace an audit, or provide legal advice.

## Report format

```markdown
# Compliance Gap Hunter — Evidence-Scoped Review

## Status
- Overall status:
- Scope:
- Evidence reviewed:
- Evidence date / freshness:
- Exclusions and limitations:

## Executive summary

## Findings
| ID | Category | Mapping or subject | Conclusion | Evidence pointer | Evidence quality | Priority | Closure evidence |
|---|---|---|---|---|---|---|---|

## Positive evidence

## Uncertainty and blockers

## Evidence request list

## Action plan
| Action | Owner | Target evidence | Dependency | Acceptance condition |
|---|---|---|---|---|

## Assessor notes
```
