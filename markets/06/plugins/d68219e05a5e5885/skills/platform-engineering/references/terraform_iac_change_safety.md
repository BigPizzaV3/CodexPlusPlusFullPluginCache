# Terraform / IaC Change Safety

## Standard workflow

1. `terraform fmt`
2. `terraform validate`
3. initialize with intended backend/providers
4. `terraform plan`
5. inspect plan
6. policy/security checks
7. approval
8. apply the reviewed plan
9. verify infrastructure and workload behavior

In automation, applying the exact saved/approved plan can reduce plan/apply drift.

## Plan review

Classify:
- create;
- in-place update;
- replacement;
- destroy;
- data-source read;
- unknown-at-plan-time.

High-risk signals:
- broad replacement;
- network/IAM changes;
- stateful resources;
- database/storage deletion;
- region/account move;
- policy changes;
- unexpectedly large plan.

## State

Treat state as sensitive operational data.

Use:
- remote backend appropriate to environment;
- encryption;
- access control;
- versioning/backup;
- locking where supported.

Do not:
- commit state;
- casually disable state locking;
- force-unlock without proving a stale lock and correct workspace;
- edit state manually unless the exact recovery procedure requires it.

## Secrets

Avoid secrets in:
- committed tfvars;
- outputs;
- plan artifacts where exposure matters;
- CI logs.

Use provider/workload identity or secret managers where appropriate.

## Versions

Pin:
- Terraform version range;
- provider versions;
- module versions;

to avoid accidental uncontrolled upgrades.

Commit the dependency lock file when appropriate to the workflow.

## Module design

Prefer:
- clear inputs/outputs;
- typed variables;
- documented ownership;
- focused module responsibility;
- tests/validation;
- low surprise.

Do not make one universal module with dozens of switches.

## Destructive changes

Before destroy/replace:
- verify exact resource and environment;
- identify dependent workloads;
- ensure data backup/recovery;
- plan sequencing;
- define rollback/forward recovery;
- use lifecycle protections when justified.

## Drift

Detect drift through regular plan/reconciliation.

Do not automatically "fix" drift until you know whether:
- infrastructure changed out of band accidentally;
- emergency/manual change was intentional;
- desired configuration should be updated.
