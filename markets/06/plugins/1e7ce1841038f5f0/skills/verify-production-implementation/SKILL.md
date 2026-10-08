---
name: verify-production-implementation
description: Verify a completed or staged implementation against its approved specification, real functionality, visual and perceptual targets, accessibility, performance, responsive behavior, supported environments, regression boundaries, release evidence, and rollback readiness. Use as a strict post-implementation release gate. Do not use for pre-development document auditing, implementation, defect repair, or redesign.
---

# Verify Production Implementation

Act as an independent post-implementation gatekeeper. Report evidence and verdicts; do not repair the implementation or rewrite its specification.

## Preserve independence

- Identify the implementation owner, decision owners, and proposed reviewers.
- Do not allow the same role to independently approve its own critical implementation or Class-2 decision.
- Inspect only accessible evidence and mark unavailable areas `NOT VERIFIABLE`.
- Do not deploy, publish, merge, release, alter code, update snapshots, waive failures, or change external state.
- Route pre-implementation document readiness to `$project-specification-auditor`, normal between-gate ratification to `$verify-implementation-checkpoint`, and repairs to the relevant implementation or defect skill. This skill remains the final release gate and does not absorb routine checkpoint verification.

## Establish the verification contract

1. Inventory approved specifications, source manifest and precedence, task execution contracts, Class-2 decisions, changed files, tests, environments, checkpoints, known deviations, and rollback.
2. Confirm the real build or staged environment corresponds to the claimed revision and configuration.
3. Trace each requirement and material observable to implementation evidence and acceptance.
4. Use the shared [risk-adaptive assurance model](../../shared/expert-system/risk-adaptive-assurance-model.md), [specialist review model](../../shared/expert-system/specialist-review-model.md), [observable ownership](../../shared/expert-system/observable-ownership.md), and [perceptual quality gates](../../shared/expert-system/perceptual-quality-gates.md).
5. Identify the direct acceptance oracle for each material claim, confirm the measurement-relevant acceptance environment, and reject circular proof where the candidate controls both expected and observed truth.
6. Apply the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md) only to relevant accepted requirements and observable release behavior; the principles do not add features or replace specialist evidence.

## Verification dimensions

Check as applicable:

- specification fidelity and explicitly approved deviations;
- real functional behavior, permissions, state transitions, user agency, cancellation/undo where required, destructive-action boundaries, failures, recovery, and data effects;
- architecture and interface compatibility;
- visual fidelity, composition, hierarchy, typography, materials, lighting, motion, interaction, and brand coherence;
- responsive behavior, browser, device, input context, theme, scope-relevant localization, and reduced motion;
- accessibility semantics, keyboard behavior, focus, contrast, assistive output, and target standard;
- performance, capacity, runtime resources, loading, and interaction budgets;
- security-relevant controls, privacy, secrets, logging, and abuse cases;
- migrations, deployment, monitoring, smoke tests, rollback, and operational readiness;
- interface-language clarity for consequential actions, states, errors and recovery, routing depth review to `$review-interface-language-and-naming` where required;
- final craft/detail across applicable technical and perceptual observables;
- regressions against protected behavior and last approved checkpoint.

Inspect the actual output. Do not award pass from a process log, test report, screenshot, or numeric metric that does not prove the target. Correct compliance with a defective specification is not success.

## Gate logic

Rate each applicable dimension `PASS`, `PASS WITH RISKS`, `FAIL`, or `NOT VERIFIABLE`.

- Any material technical, functional, accessibility, security, data, release, regression, or perceptual failure makes the overall result `FAIL`.
- Technical pass plus perceptual fail is `FAIL`.
- Perceptual pass plus technical fail is `FAIL`.
- A required dimension that is not verifiable blocks release.
- Non-blocking risks require owner, impact, evidence, and acceptance authority.

## Output

Return:

1. overall verdict: `RELEASE READY`, `READY WITH ACCEPTED RISKS`, or `NOT RELEASE READY`;
2. inspected revision, environment, sources, and evidence;
3. requirement and observable traceability;
4. dimension results;
5. failures, regressions, deviations, and unverified areas;
6. independent reviewer record;
7. rollback and operational readiness;
8. exact conditions for re-verification.

Never repair findings inside this skill.

Dedicated accessibility depth belongs to `$audit-accessibility-and-inclusive-design`; behavioral AI quality belongs to `$evaluate-ai-systems`. This final gate consumes their evidence when required instead of duplicating their specialist audits.
