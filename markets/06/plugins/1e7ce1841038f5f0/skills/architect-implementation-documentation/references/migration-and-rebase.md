# MIGRATE_REBASE — controlled corpus migration

Use for many overrides, historical drift, unsupported precision or changed governance/architecture requiring a new controlled suite. New architecture/governance must already have relevant owner approval; this mode does not authorize making those decisions. Preserve project files outside the explicitly authorized target. A project example grants no write permission.

## Sequence and gates

1. INVENTORY: exact corpus roots, file IDs/paths, versions/status, byte hashes, formats, access and owner. Preserve a verified snapshot before approved writes. Unreadable content is missing evidence, not covered.
2. AUTHORITY MAP: sources/approvals, precedence, overrides, fixed decisions and conflicts. Stop affected decisions on unresolved Class 1; do not pick the newest file automatically.
3. DECISION EXTRACTION: extract every in-scope decision, requirement, material observable, interface, asset obligation, test and acceptance condition with stable ID and exact source locator. Inventory alone is not coverage. Account for files with no extracted requirements using a checked reason.
4. MIGRATION CLASSIFICATION: classify each extracted item using the table below, with rationale, owner, dependencies and required approval.
5. OBSERVABLE OWNERSHIP: one primary source owner per material observable; preserve relationships and detect competing definitions.
6. NEW SUITE BLUEPRINT: propose boundaries, dependencies, precedence, owners and first-read for a candidate suite. Preserve legitimate Class-2/3 discretion; remove false precision only through the approved classification/authoring path.
7. CONTENT MIGRATION: specialist authors populate candidate documents from approved decisions. No new product/architecture/brand solution invented to fill a gap. Maintain bidirectional source-to-target links and changed/deferred decisions.
8. COVERAGE VALIDATION: reconcile inventory, extracted IDs and mappings; inspect targets and approvals, not counts alone. No unclassified item, orphan source requirement, unsupported target requirement, unresolved conflict or unapproved replacement/drop affecting activation may remain. Scope exclusions must be explicit and approved.
9. READINESS + CLEAN ROOM: read-only audit of candidate, migration register, coverage matrix and risk-based historical samples. First-read clean-room test from accessible candidate sources. Report actual evidence; absence of an independent reader is pending, not PASS.
10. CONTROLLED ACTIVATION: only after all gates and explicit owner activation approval, switch the controlling manifest. Mark former active documents historical in the registry/sidecar; preserve bytes, hashes and replacement links. New suite becomes active read set. Do not move/delete originals or rewrite content to change status without separate authority.

On failed gates the previous approved source set remains controlling, but affected known-defective work stays blocked. Keep candidate inactive. Recheck source and candidate hashes before activation. Changes invalidate affected coverage/audits; log a new version and re-audit. Record rollback manifest, activation owner/time and verified restoration procedure; restoring documents does not roll back code, data or external actions.

## Classification

| Class | Meaning | Required evidence |
|---|---|---|
| KEEP_EXACT | Preserve confirmed decision/value and meaning. | Source/target locators, equality/semantic check, fixed boundary. |
| KEEP_PRINCIPLE | Preserve approved intent with documented discretion. | Intent, invariants, bounds, authority and target evidence; no silent weakening of exact requirements. |
| REVALIDATE | Validity unresolved. | Owner, reason, validation method; not implementation authority until resolved. |
| REPLACE | Approved new decision replaces old one. | Approval, old/new IDs, rationale, dependency impact. |
| DROP | Exclude from active scope, not delete evidence. | Owner approval or authoritative exclusion, rationale, impact/coverage disposition. |
| HISTORICAL_ONLY | Retain non-operative history. | Proven status/authority and absence of active obligations. |
| NOT_APPLICABLE | Outside declared migration scope. | Scope evidence and disposition; no silent omissions. |

## Registers and enum compatibility

Migration register fields: MIGRATION_ID, source snapshot, item ID/type, source path/version/hash/locator, authority/approval, classification, rationale, target document/version/locator, observable owner, dependencies, disposition owner/approval, validation evidence, outstanding blocker, activation state.

Coverage matrix supports source → target/disposition AND target → approved source. Include retained, replaced, dropped, deferred and excluded counts plus all unresolved items. Report denominator and scope; never claim whole-corpus coverage from a sample.

Preserve existing enums: old source `status=HISTORICAL`, `usage_class=HISTORICAL`, `usage_detail=MIGRATION_EVIDENCE`, `active_implementation=false`. MIGRATION_EVIDENCE is a purpose field, not a new usage enum. Store annotations in register/sidecar to preserve original bytes. Active artifacts retain existing approved/final/full/partial semantics.

## Historical read policy

After accepted coverage, coding agents consume the active suite and current task slice, not all superseded documents. Historical evidence remains accessible through the register. Reopen relevant historical items for missing coverage, source/owner conflict, suspicious omission, active reference, sample mismatch or explicit full historical audit. Mismatch expands affected review and blocks affected readiness; never repair evidence to make a mapping pass.
