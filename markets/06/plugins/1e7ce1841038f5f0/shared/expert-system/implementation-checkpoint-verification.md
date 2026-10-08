# Implementation checkpoint verification contract

Version 1.1. Read-only gate between implementation phases. Apply the shared [risk-adaptive assurance model](risk-adaptive-assurance-model.md). It does not replace pre-implementation readiness or final release verification and grants no repair, next-task, deployment or publication authority.

## Identity and evidence

Bind the review to project, checkpoint/gate, repository/worktree, branch, revision or approved snapshot, dirty-tree ownership, task contract, active source-manifest version/hash, changed files, implementer report, evidence IDs, test/runtime environment and last approved checkpoint. A report is attributed data, not truth.

Classify every material claim:

- `VERIFIED` — directly inspected or reproduced evidence establishes the scoped claim for the inspected state.
- `SUPPORTED` — relevant but incomplete, indirect or insufficiently fresh evidence.
- `UNVERIFIED` — no adequate evidence inspected.
- `CONTRADICTED` — inspected evidence conflicts with the claim.

If a claim is contradicted, identify downstream conclusions that relied on it and mark `DEPENDENCY_REVIEW_REQUIRED` until revalidated. Evidence must correspond to the claimed revision/configuration/runtime. Prefer direct real-system or independently computed oracles; a producer must not control both the expected and observed truth for a material gate. Where applicable use the shared write/read-back/runtime/revision/real-output sequence; do not extrapolate beyond what a test, log, screenshot or measurement proves.

Reproduction remains read-only and non-consequential. Run only explicitly authorized checks that do not write production data, apply migrations, submit forms, create or alter accounts, trigger deployments, send messages, purchase anything or otherwise change an external system. If safe reproduction cannot be established, do not run it; record the claim as unverified and state the exact evidence or controlled environment required.

## Review provenance

Record reviewer role, capability class when relevant and evidenced, implementation participation, independence, direct evidence inspection, fallback/reduced-capability status and whether ratification is required. A fresh session or different role label does not establish independence. A fallback reviewer receives only the authority justified by the gate contract; required full-capability ratification remains pending.

## Gate checks and result

Check the declared assurance mode and applicable technical, functional, security, accessibility, responsive, performance, perceptual and regression criteria separately. Confirm the acceptance environment and oracle identity where they materially affect the result, Class-1 decisions were not hidden in implementation, Class-2 decisions stayed within contract, routed dependencies belong to the named downstream gate, and no self-review is represented as independent acceptance.

Use exactly one result:

- `CHECKPOINT VERIFIED`
- `CHECKPOINT FAILED`
- `CHECKPOINT BLOCKED`
- `EVIDENCE INSUFFICIENT`
- `REVIEW PROVENANCE INSUFFICIENT`

Choose the result deterministically:

- `CHECKPOINT VERIFIED` only when every required dimension passes for the bound state and the required reviewer provenance is established;
- `CHECKPOINT FAILED` when inspected evidence proves a required criterion failed or contradicts a material pass claim;
- `CHECKPOINT BLOCKED` when an authority, source-precedence, task-contract or gate-definition blocker prevents a valid decision;
- `EVIDENCE INSUFFICIENT` when required state identity, logs, tests, runtime/render evidence or measurements are missing, inaccessible, stale or not bound to the inspected state;
- `REVIEW PROVENANCE INSUFFICIENT` when the work evidence may otherwise support a decision but required reviewer independence, capability or ratification is not established.

Route a failure cause as `SPEC_DEFECT`, `REPRESENTATION_FAIL`, `IMPLEMENTATION_FAIL`, `REGRESSION`, `MEASUREMENT_DEFECT`, `PERCEPTUAL_FAIL` or `AUTHORITY_BLOCK`. Verification authorizes the next gate only when the checkpoint contract makes that transition explicit and every required dimension and reviewer passes. It never starts the next phase automatically.
