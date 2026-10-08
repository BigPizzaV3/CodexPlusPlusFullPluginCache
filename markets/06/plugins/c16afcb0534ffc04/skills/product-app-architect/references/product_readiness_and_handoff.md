# Product Readiness and Handoff

## Purpose

Use this file to turn an approved product direction into an incremental build plan and to review whether a product is ready for wider use.

# 1. Delivery strategy

Prefer a usable vertical slice over building every layer separately.

A useful default:

## Phase 0 — Decisions and setup
- unresolved product decisions;
- repository/project setup;
- design foundations if needed;
- environments;
- core data/schema decisions.

## Phase 1 — Smallest usable loop
Implement one real end-to-end user outcome, including UI, backend/data, validation, basic errors, and a test.

## Phase 2 — Core experience
Add the remaining MVP capabilities.

## Phase 3 — Hardening
Add the reliability, security, accessibility, performance, analytics, and operational work required for intended usage.

## Phase 4 — Launch
Validate deployment, monitoring, support, rollback, documentation, and release requirements.

Adapt phases to project size.

# 2. Build-plan item

For each work item define:
- objective;
- affected components;
- dependencies;
- product behavior;
- acceptance criteria;
- validation/tests;
- migration/data impact;
- risks;
- rollback/disable path when relevant.

Do not specify file names that have not been verified in an existing repository.

# 3. Handoff to coding agent or engineer

Provide:

## Product context
What is being built and why.

## Current state
What already exists.

## Requested change
Exact scope.

## Required behavior
Observable product behavior.

## Constraints
Stack, design, compatibility, security, performance, or platform constraints.

## Acceptance criteria
How completion will be judged.

## Non-goals
What should not change.

## Validation
Tests/checks expected.

Avoid dumping unrelated product history.

# 4. Product readiness review

Review only categories relevant to intended launch.

## Product
- core value works end to end;
- scope matches stated MVP;
- critical states are designed;
- analytics/support needs are defined.

## UX/accessibility
- loading/empty/error states;
- keyboard/screen reader where applicable;
- responsive/adaptive behavior;
- text/contrast/target usability;
- destructive-action recovery.

## Correctness/data
- data ownership/source of truth;
- migrations;
- validation;
- backup/recovery where needed;
- retention/deletion behavior.

## Security/privacy
- authentication/authorization;
- least privilege;
- secrets;
- sensitive data;
- abuse cases;
- logging/audit;
- privacy disclosures/consent where applicable.

## Reliability/operations
- monitoring;
- error reporting;
- dependency failure behavior;
- deployment/rollback;
- backups/restore where relevant;
- ownership/runbook.

## Performance/cost
- major bottlenecks tested;
- expensive external services understood;
- scale assumptions documented;
- budget/usage limits where needed.

## Platform/distribution
- app-store/web requirements;
- browser/device support;
- SEO where relevant;
- legal/content/licensing constraints;
- third-party API terms.

# 5. Launch decision

Use:

**Ready** — no material blocker for intended scope.

**Ready with known limitations** — limitations are explicit, bounded, and acceptable.

**Not ready** — a correctness, security, data-loss, accessibility, platform, or core-product blocker remains.

Do not declare a prototype production-ready merely because it builds successfully.

# 6. Post-launch learning

Define:
- primary success signal;
- support/error signal;
- major drop-off point;
- qualitative feedback source;
- technical health signal;
- cost signal if relevant.

Use evidence to decide the next change rather than automatically expanding scope.
