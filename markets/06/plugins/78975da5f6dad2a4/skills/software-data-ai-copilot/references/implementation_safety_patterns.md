# Implementation Safety Patterns

## Purpose

Use this file when a code change can affect public contracts, persistent data, deployments, runtime compatibility, or recovery.

# 1. Contract-preserving change

Prefer additive changes when compatibility matters.

Examples:
- add optional API field before removing old field;
- accept old and new formats during migration;
- deploy consumer support before producer switch;
- feature-flag behavior change.

Define the compatibility window and removal plan.

# 2. Feature flags

Use when:
- behavior is risky;
- rollout should be gradual;
- fast disable is valuable.

A flag should have:
- owner;
- default;
- rollout plan;
- observability;
- removal condition.

Do not create permanent flag debt.

# 3. Database migration

For material schema changes:

1. add compatible schema;
2. deploy code that can handle both states;
3. backfill if needed;
4. validate;
5. switch reads/writes;
6. remove old schema later.

Avoid one-step destructive migrations when data or old application versions still depend on the old shape.

# 4. Data backfill

Define:
- target scope;
- source of truth;
- idempotency;
- concurrent-write behavior;
- batch/rate limits;
- validation;
- rollback/repair;
- downstream impact.

Do not run an unbounded backfill against a live system without scope and observability.

# 5. API migration

Check:
- clients;
- versioning;
- required vs optional fields;
- default behavior;
- error codes;
- ordering;
- pagination;
- idempotency;
- deprecation notice.

Prefer tolerant readers and explicit migration windows when possible.

# 6. Dependency/runtime upgrade

Before upgrade:
- inspect current and target versions;
- read official migration/breaking-change docs;
- identify transitive impact;
- check runtime/toolchain compatibility;
- run targeted tests;
- stage rollout when risk is material.

Do not mix a major upgrade with unrelated feature work if it can be separated.

# 7. Rollback vs forward fix

Rollback is appropriate when:
- previous artifact is compatible;
- schema/data changes are reversible;
- dependency state supports it.

Use a forward fix when rollback would corrupt or misinterpret newer persisted state.

State which applies before high-risk deployment.

# 8. Destructive operations

Before delete/drop/truncate/broad rewrite:
- verify target/scope;
- preview affected records/resources;
- confirm backup/restore or regeneration path;
- define rollback;
- isolate permissions;
- log/audit if relevant.

Never hide destructive behavior inside a “cleanup” change.

# 9. External side effects

For email, payments, notifications, files, webhooks, or third-party APIs:
- make retries safe;
- use idempotency keys/ledgers when supported;
- separate computation from side effects;
- avoid duplicate action after partial failure;
- log outcome without secrets.

# 10. Deployment validation

Define:
- pre-deploy check;
- deployment order;
- health signal;
- smoke test;
- rollout threshold;
- rollback trigger;
- post-deploy observation window.

A successful build is not proof of a safe deployment.
