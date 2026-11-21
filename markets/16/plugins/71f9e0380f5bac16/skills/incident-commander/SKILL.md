---
name: incident-commander
description: Use when the user asks for a Incident Commander review based on supplied evidence.
---

# Incident Commander

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

Organize incident facts, decisions and next actions as a response unfolds.

### What it helps with
- Build a sourced incident timeline.
- Track containment, recovery and decision owners.
- Draft qualified updates and a post-incident review.

### What to provide
Incident reports, alerts, logs, action records and the relevant response roles.

### Limits
It does not establish impact, root cause or notification obligations without evidence and review.

## Report format

```markdown
# Incident Commander — Evidence-Scoped Review

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
