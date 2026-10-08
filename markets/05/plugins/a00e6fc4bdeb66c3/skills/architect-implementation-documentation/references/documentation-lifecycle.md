# Documentation lifecycle and artifact contract

## Status semantics

| Status | Meaning | May implementation rely on it? |
|---|---|---|
| DRAFT | Incomplete working material; proposals and gaps may remain. | No. |
| IN REVIEW | Candidate content under named review. | No, except an explicitly authorized prototype. |
| APPROVED | Content decisions are approved, but suite dependencies or readiness may still be pending. | Only within explicitly approved limited use. |
| FINAL | Approved, decision-complete for declared scope, consistent, resolvable, and document-level verified. | Yes, subject to suite precedence and readiness. |
| PARTIAL USE | Only named sections are authorized; all others are excluded. | Only named sections. |
| HISTORICAL | Evidence of a prior state or decision. | No. |
| OVERRIDDEN | A higher-precedence artifact controls a stated scope. | Only outside the overridden scope. |
| SUPERSEDED | Fully replaced by a named artifact/version. | No. |
| DO NOT IMPLEMENT | Retained for reference but expressly forbidden as implementation input. | No. |

`FINAL` is not a visual label. It requires approval evidence, completed dependencies, resolvable references, no unauthorized Class-1 gap, controlled Class-2 and Class-3 space, and document-level acceptance. It may contain approved targets, bounds, calibration, runtime verification, and perceptual acceptance. Suite readiness is a separate gate.

## Mandatory metadata

Each controlled artifact records:

- `artifact_id`
- `title`
- `version`
- `status`
- `usage_class`
- `owner`
- `authors_or_authoring_skill`
- `created_at`
- `last_reviewed_at`
- `approval_evidence`
- `source_ids`
- `extends`
- `overrides`
- `supersedes`
- `downstream_dependencies`
- `scope`
- `acceptance_evidence`

Use `NONE` or `UNKNOWN` explicitly; do not omit a relationship silently.

## Required registers

- Artifact Register: identity, location, version, status, usage, owner, dependencies.
- Source Register: source identity, location, accessibility, authority, freshness, evidence classification.
- Decision Register: decision ID, question, outcome, owner, basis, affected artifacts, date, status.
- Dependency Register: provider, consumer, required version/status, failure impact.
- Change Log: before/after, reason, author, approval, affected artifacts, rollback or prior version.
- Gap Register: missing decision/specification, severity, owner, dependencies blocked, closure evidence.

Do not overload lifecycle status to represent source truth. Evidence classifications such as `VERIFIED`, `USER DECISION`, `PROPOSED`, `ASSUMED`, `UNKNOWN`, and `CONFLICTING` remain attached to claims.
