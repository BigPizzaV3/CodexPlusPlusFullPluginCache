---
name: refactor-and-migrate-codebases
description: Transform an existing codebase through a controlled refactor, framework or platform migration, architecture transition, dependency replacement, or legacy modernization while preserving explicit invariants, salvageable value, compatibility, evidence, and rollback. Use when structural transformation is the primary task. Do not use for a small feature, an isolated defect, routine cleanup, or speculative rewrite without an approved migration objective.
---

# Refactor and Migrate Codebases

Transform structure without blindly rebuilding valuable legacy behavior or carrying defects forward.

## Establish migration authority

1. Inspect the real repository, architecture, runtime, deployment, tests, data, interfaces, dependencies, operational constraints, and migration specification.
2. Define the approved before/after boundary, invariants, compatibility obligations, downtime or rollout constraints, protected behavior, success metrics, and rollback point.
3. Use the shared [decision-authority model](../../shared/expert-system/decision-authority-model.md). Framework, architecture, data semantics, public interfaces, security, product behavior, and deletion are Class 1 unless already authorized.
4. Route architecture, domain, migration, data, testing, release, security, and independent review roles only as required.

Stop when the target architecture, migration scope, data authority, compatibility policy, or rollback path is unresolved.

## Salvage matrix

Classify every relevant element as:

- `KEEP` — retain unchanged and protect with regression evidence.
- `ADAPT` — preserve purpose while changing implementation.
- `REPLACE` — substitute through an approved target and compatibility plan.
- `DELETE` — remove only with explicit authority and dependency proof.
- `HISTORICAL` — preserve for traceability but do not execute.

For each record reason, evidence, dependencies, consumers, compatibility, migration action, test, rollback, and owner. A weaker replacement must not win merely because it is newer.

## Migration design and execution

- Choose big-bang, strangler, parallel run, branch-by-abstraction, dual write/read, compatibility adapter, or another strategy from actual risk and constraints; label an unapproved choice as proposed.
- Define phase entry/exit gates, data and schema migration, backfill, version skew, feature flags, observability, rollback, and old-path retirement.
- Establish baseline behavior and performance before structural edits.
- Execute in reversible slices with explicit checkpoints and source-control recovery.
- Preserve public contracts unless the approved migration changes them.
- Do not combine unrelated cleanup with migration work.

## Verification

Prove required equivalence or intentional difference through unit, integration, contract, end-to-end, migration, data-integrity, performance, security, deployment, and rollback tests as applicable. Compare old and new paths using deterministic fixtures or shadow evidence when feasible. Run independent architecture and release review for material migrations.

Correct compliance with a defective target architecture is not success. Stop and escalate when the proposed target is demonstrably weaker, incompatible, or operationally unsafe.

## Output

Return the salvage matrix, phased migration plan, implemented slices, compatibility and data evidence, test results, deviations, retired and preserved elements, rollback procedure, independent review, unresolved risks, and next gate.
