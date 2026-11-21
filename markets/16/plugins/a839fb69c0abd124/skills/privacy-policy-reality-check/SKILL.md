---
name: privacy-policy-reality-check
description: Use when the user asks for a Privacy Policy Reality Check review based on supplied evidence.
---

# Privacy Policy Reality Check

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

Compare a privacy notice with the processing activities shown in the evidence you provide.

### What it helps with
- Identify supported statements and possible omissions.
- Distinguish notice wording from operational evidence.
- Request the records needed to resolve uncertainty.

### What to provide
The current notice, processing inventory, vendor records and relevant configurations or workflows.

### Limits
It does not make a legal compliance determination.

## Report format

```markdown
# Privacy Policy Reality Check — Evidence-Scoped Review

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
