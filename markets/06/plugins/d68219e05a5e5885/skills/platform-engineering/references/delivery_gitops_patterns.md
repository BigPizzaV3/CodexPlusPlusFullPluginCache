# CI/CD and GitOps Patterns

## Delivery invariants

Know:
- source revision;
- build;
- artifact digest/version;
- test evidence;
- deployment environment;
- config version;
- approver/policy result;
- rollout result.

## Build once, promote

Prefer promoting the same tested immutable artifact between environments rather than rebuilding different artifacts per environment.

## Pipeline stages

Typical shape:

`commit → build → unit/static checks → package/sign → integration → deploy lower env → acceptance → approval/policy → production rollout → verification`

Only include stages that serve a real risk/control.

## Credentials

Prefer:
- short-lived federation/workload identity;
- environment-scoped permissions;
- no long-lived cloud keys in repositories;
- no production credential available to unrelated CI jobs.

## GitOps

Desired state lives in Git.

A reconciler:
- compares desired vs actual;
- applies changes;
- reports sync/health.

Define:
- repo ownership;
- application vs configuration separation;
- environment promotion;
- secret approach;
- emergency change policy;
- reconciliation after imperative fixes.

## Progressive delivery

For high-risk changes consider:
- canary;
- blue/green;
- percentage rollout;
- feature flag;
- region/tenant subset.

Define:
- success metric;
- observation window;
- automated/manual promotion;
- rollback trigger.

## Rollback

A rollback should be operationally possible, not just theoretically available.

Check:
- application backward compatibility;
- schema changes;
- config compatibility;
- artifact availability;
- data migrations;
- traffic control.

Sometimes forward-fix is safer than rollback; state the reason.

## Supply chain

When relevant include:
- dependency provenance;
- artifact signing/verification;
- image scanning;
- SBOM;
- protected branches;
- review;
- immutable tags/digests.

Do not equate one scanner with complete supply-chain security.
