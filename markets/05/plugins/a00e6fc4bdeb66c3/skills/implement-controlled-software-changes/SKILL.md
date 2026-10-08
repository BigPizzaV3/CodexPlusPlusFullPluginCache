---
name: implement-controlled-software-changes
description: Implement an approved software feature or change in an existing repository through evidence-based preflight, bounded decision authority, reversible edits, tests, regression checks, independent review, and a verified change report. Use when the user asks to implement a specification, execute a coding task, or change code under controlled scope. Do not use to invent product requirements, create the specification, conduct a read-only audit, perform a broad migration, or diagnose an unknown defect as the primary task.
---

# Implement Controlled Software Changes

Implement approved scope without silently changing the product, architecture, design, interfaces, data, security posture, or surrounding code.

## Preflight

1. Inspect repository instructions, working-tree state, relevant source, tests, configuration, and the controlling specification.
2. Identify source versions, precedence, protected areas, permitted files or modules, environment, required commands, and rollback path.
3. Convert the assignment into the shared [task execution contract](../../shared/expert-system/task-execution-contract.md).
4. Route the smallest expert set using the [expert routing model](../../shared/expert-system/expert-routing-model.md). Assign an independent reviewer when risk warrants it.
5. Classify choices with the [decision-authority model](../../shared/expert-system/decision-authority-model.md).

Stop before editing when a required source is missing, controlled sources conflict, the repository differs materially from the specification, acceptance cannot be tested, or a Class-1 decision is unresolved. Report the exact blocker instead of inventing a solution.

## Controlled implementation

1. Establish a recoverable before-state through existing version control or an approved checkpoint. Preserve user changes and unrelated work.
2. Implement the smallest coherent change that satisfies the approved contract.
3. Make Class-3 engineering choices within repository conventions and record only material ones.
4. Exercise Class-2 judgment only when role, target, bounds, reversibility, evidence, review, and stop condition are explicit. Log the decision.
5. Do not introduce a dependency, tool, framework, service, migration, feature, redesign, or unrelated refactor without authority.
6. Keep external mutations, deployment, publication, messages, purchases, and destructive operations behind their own approvals.

## Verification

- Run the specified focused tests first, then applicable type, lint, build, integration, regression, security, accessibility, performance, and smoke checks.
- Inspect the real changed behavior. A passing command is not proof of user-visible correctness.
- Compare before and after for protected behavior and connected interfaces.
- Route visual acceptance to `$verify-production-implementation` or `$audit-premium-digital-experience` checkpoint mode when applicable.
- Apply the [specialist review model](../../shared/expert-system/specialist-review-model.md) for critical work.

Correct compliance with a defective specification is not success. If implementation exposes a specification defect, stop the affected path, preserve evidence, and return it to the responsible author or owner.

## Output

Return the implemented outcome, exact change manifest, material decisions by class, test commands and actual results, regression evidence, reviewer result, deviations, rollback instructions, residual risks, and remaining approvals. Commit only when the project gate explicitly requires or the user authorizes it.
