# Record and evidence contract

Use this contract for every critical document, register entry, system record, decision, recovery step, and manifest item.

## Required metadata

- stable record ID;
- human-readable title;
- purpose and decisions supported;
- scope: company, project, product, client, environment, location, or system;
- truth status;
- canonical source and accessible locator;
- source type and provenance;
- owner and backup owner;
- created and last-verified dates with timezone;
- update trigger and review date;
- sensitivity: public, internal, confidential, restricted;
- retention and archive rule;
- dependencies and dependents;
- current version or revision;
- supersedes / superseded-by relationship;
- evidence or verification method;
- gaps, conflicts, assumptions, and professional-review requirement;
- recovery importance: critical, high, normal, low;
- permitted audience and authority boundary.

## Truth statuses

`VERIFIED_CURRENT` requires direct current evidence. `USER_CONFIRMED` is attributable but not independently verified. `PROPOSED` and `ASSUMED` can guide planning but cannot be presented as current truth. `CONFLICTING`, `STALE`, and `INACCESSIBLE` remain visible until resolved. Never silently convert an unknown into an assumption.

## Source-of-truth rules

1. Name exactly one canonical source for each controlled fact or artifact when possible.
2. If authority is distributed, define which system owns each field and how conflicts are resolved.
3. Working copies must link back to the canonical record and state their refresh method.
4. Preserve historical evidence without allowing it to masquerade as current truth.
5. Use absolute paths only for a known local environment; also provide portable relative paths or stable system identifiers.
6. Record provider, workspace/organization, account owner, and recovery custodian for cloud sources, but not authentication material.
7. For URLs and vendor systems, record verified access date and export/exit route.

## Secret-reference schema

Allowed fields:

- system or secret purpose;
- approved secret manager;
- vault/collection and item label;
- account or role owner;
- recovery custodian;
- MFA method category without seed or code;
- lawful recovery URL or support channel;
- last access review date;
- last recovery-route review date;
- rotation responsibility and due date;
- break-glass approval process;
- status and gaps.

Forbidden content includes passwords, tokens, private keys, seed phrases, recovery codes, session cookies, security answers, unredacted identity documents, and full payment data.

## Decision record minimum

Record ID, date, decision owner, context, options considered, selected option, rationale, evidence, consequences, reversibility, dependencies, review trigger, superseded decision, and implementation status.

## Current-state record minimum

Record verified timestamp, environment, version/release/commit, live and degraded capabilities, open work, incidents, blockers, pending approvals, known defects, data freshness, last successful operation, and exact next safe action.

## Recovery-step minimum

Record trigger, authorization, prerequisites, dependencies, ordered action, stop conditions, escalation, expected result, verification, rollback, evidence to retain, owner, and last test result. A document-only procedure is `UNTESTED` until exercised or independently validated.

