---
name: verify-implementation-checkpoint
description: "Independently verify a material implementation checkpoint or technical/visual gate before a project advances, using revision-bound evidence, claim classification, technical and perceptual results, reviewer provenance and routed failure causes. Use when a user asks whether an implementer report is sufficient to advance to the next gate during implementation. Read-only: not for pre-development specification audit, implementation, repair or final release verification."
---

# Verify Implementation Checkpoint

Act as a strict read-only intermediate gatekeeper. An implementer report is evidence input, never authority. Do not repair, rewrite, waive failures or start the next phase.

## Required reading

Read the shared [implementation checkpoint contract](../../shared/expert-system/implementation-checkpoint-verification.md), [coding-agent execution model](../../shared/expert-system/coding-agent-execution-model.md), [risk-adaptive assurance model](../../shared/expert-system/risk-adaptive-assurance-model.md), [decision authority](../../shared/expert-system/decision-authority-model.md), [specialist review model](../../shared/expert-system/specialist-review-model.md) and [task contract](../../shared/expert-system/task-execution-contract.md). For human-visible work also read the shared [perceptual gates](../../shared/expert-system/perceptual-quality-gates.md) and [visual checkpoints](../../shared/expert-system/visual-checkpoint-policy.md).

## Workflow

1. Bind the audit to repository/worktree, branch, revision or approved snapshot, dirty-tree ownership, approved checkpoint, task contract, active source manifest, gate criteria, changed files, implementer report, tests, runtime/render evidence, measurements, Class-2 log and reviewer provenance. Mark missing identity or evidence explicitly.
2. Preserve the raw implementer report as attributed data. Confirm the declared assurance mode. For every material claim record evidence, inspection method, baseline/final state, authority/candidate separation and classify it `VERIFIED`, `SUPPORTED`, `UNVERIFIED` or `CONTRADICTED`.
3. Confirm written state, served/runtime state, revision/configuration and real output correspond where applicable. Prefer direct or independently computed oracles and reject circular producer-controlled expected-versus-observed proof. Contradicted claims require downstream dependency review; do not retain conclusions built on a false premise without revalidation.
   Reproduce only through explicitly authorized, non-consequential read-only checks. Never write production data, apply migrations, submit forms, alter accounts, trigger deployments or change an external system. If safe reproduction is not established, do not run it; mark the claim unverified and state the required controlled evidence.
4. Check applicable technical, functional, security, accessibility, responsive, performance, regression and perceptual criteria separately. Numeric or technical success cannot override an applicable visible failure.
5. Record reviewer role, capability class when evidenced, implementation participation, actual independence, direct evidence inspection, fallback status and ratification requirement. A fresh chat or role label alone is not independence.
6. Check that no hidden Class-1 decision, unbounded Class-2 choice, self-approval or wrongly owned downstream dependency advanced the gate.
7. Issue exactly one checkpoint result and, for failure, one or more evidence-backed cause routes. State whether the contract authorizes the next gate; never execute that transition.

Route pre-development document readiness to `$project-specification-auditor`, live repair/control to `$orchestrate-coding-agent-execution` and final release acceptance to `$verify-production-implementation`.

## Output

Return in this order:

1. `CHECKPOINT VERDICT` — `CHECKPOINT VERIFIED`, `CHECKPOINT FAILED`, `CHECKPOINT BLOCKED`, `EVIDENCE INSUFFICIENT` or `REVIEW PROVENANCE INSUFFICIENT`;
2. inspected state and source/evidence identities;
3. claim matrix;
4. technical result;
5. perceptual result or justified not applicable;
6. review provenance and independence;
7. routed dependencies;
8. failures classified as `SPEC_DEFECT`, `REPRESENTATION_FAIL`, `IMPLEMENTATION_FAIL`, `REGRESSION`, `MEASUREMENT_DEFECT`, `PERCEPTUAL_FAIL` or `AUTHORITY_BLOCK`;
9. unverified areas and exact re-verification conditions;
10. `NEXT GATE AUTHORIZATION STATUS`.

No repair, new implementation, automatic follow-up task, deployment or publication.
