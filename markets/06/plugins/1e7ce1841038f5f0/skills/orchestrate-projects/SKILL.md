---
name: orchestrate-projects
description: Turn broad or ambiguous objectives into executable, verified projects by isolating context, classifying the project, routing the smallest relevant skill and expert team, sequencing dependencies, governing decisions, and integrating results. Use when a user says start this project, handle everything, coordinate multiple specialties, decide which skills or experts are needed, or manage a complex task from idea to verified deliverable.
---

# Orchestrate Projects

Own coordination and integration while keeping specialist work within explicit scope and authority.

## Workflow

1. Establish the objective, user value, deliverables, acceptance criteria, deadline, constraints, exclusions, risk, and authorization boundary.
2. Separate confirmed facts, assumptions, unknowns, and excluded approaches. For material source selection use the shared [Context Package](../../shared/expert-system/context-package.md); for interrupted or drifting sessions use [session lifecycle](../../shared/expert-system/session-lifecycle.md). Ask only material blocking questions.
   When the project depends on external factual research, web/database search, current/disputed claims, or only-confirmed-facts requirements, route claim validation through `$control-deep-research`. Domain specialists retain their decisions; research evidence does not become project authority.
3. Build a dependency map and identify the critical path.
4. Select the smallest useful capabilities. Use relevant available skills when their triggers match; do not pretend missing skills or tools exist. For cross-provider work apply [provider capability routing](../../shared/expert-system/provider-capability-routing.md) and route toolchain design to `$design-optimal-ai-workflow` when needed. Keep worker, capability and execution surface separate; choose a hybrid route only when distinct acceptance dimensions need it. Current availability may affect a tie but is not durable project truth.
   At relevant task start/re-entry apply the shared [session start decision](../../shared/expert-system/session-lifecycle.md): resolve the method, target-environment prerequisites and freshness before dependent execution. Carry its compact outcome in the existing task record; do not add a workstream or report for trivial work.
5. Define workstreams, owners, inputs, outputs, dependencies, approval gates, and integration tests using `references/orchestration-model.md`.
6. Execute or coordinate in reversible increments. Parallelize independent work only when authorized and supported.
7. Maintain a decision log for material assumptions, tradeoffs, scope changes, and unresolved risks.
   Before allowing a side issue to replace the active focus, require at least one evidenced reason: it blocks the objective, exposes material risk, invalidates a governing assumption, the user explicitly reprioritizes it, or a documented dependency makes it materially better to resolve now. Otherwise capture it as an open loop and continue the active focus. Do not turn this gate into a visible form for trivial work.
8. Integrate outputs into one coherent deliverable. Resolve contradictions by objective, evidence, explicit constraints, and decision ownership.
9. Verify acceptance criteria and red-team the integrated result.
10. Report outcome, deliverables, decisions, remaining risks, and the next safe action.

## Expert routing responsibility

For complex projects, read the shared [expert standard](../../shared/expert-system/expert-standard.md), [role registry](../../shared/expert-system/expert-role-registry.md), [routing model](../../shared/expert-system/expert-routing-model.md), and [decision-authority model](../../shared/expert-system/decision-authority-model.md).

- Maintain a `PROJECT EXPERT MATRIX`, phase expert matrix, and task expert configuration when different disciplines lead different decisions.
- For each material task assign one lead, only necessary support roles, and an independent reviewer when consequences or perceptual quality warrant it.
- Ask: **Which discipline must lead this decision, which supports it, and who independently accepts it?**
- Route roles dynamically from capability need; do not produce role theater or activate every plausible title.
- Classify material decisions as Class 1, 2, or 3. Stop dependent work on unresolved Class-1 authority.
- For implementation tasks, issue the shared [task execution contract](../../shared/expert-system/task-execution-contract.md) and route to the narrowest execution skill.
- Use `$compose-role-teams` only when the deliverable itself is a reusable role team or prompt. This skill owns live project routing.

Normal chat is usually sufficient for decisions, short analysis and small text work. Route substantial file-heavy, cross-source or long-running artifact work to an actually available suitable worker such as ChatGPT Work or Claude Cowork only when its capabilities materially help. Such a worker may discover, analyze, structure, reconcile, verify or propose, but does not become Project, Product, Design or Owner Authority. Its generated package is derived and bounded unless explicit applicable authority promotes it; record artifact type separately from truth/authority and lifecycle status.

## Boundaries

When this project controller coordinates ongoing implementation by an external coding agent, route the operational loop to `$orchestrate-coding-agent-execution` using the shared [coding-agent execution model](../../shared/expert-system/coding-agent-execution-model.md). If the reusable repository harness must be created, restructured or repaired, route it to `$architect-coding-agent-harness`; do not bury harness architecture in the live loop. Material intermediate ratification may route read-only to `$verify-implementation-checkpoint`, while final release remains `$verify-production-implementation`. Retain project/dependency ownership here; domain skills own implementation. No automatic agent dispatch, harness installation, phase transition or deployment is implied.

- Coordination does not expand authorization. External messages, purchases, publication, deployment, deletion, or high-impact actions require appropriate permission.
- Do not create workstreams for cosmetic completeness.
- Do not hide blockers behind a plan; exhaust safe alternatives, then ask.
- Prefer execution over planning when the requested action is safe, authorized, and sufficiently defined.
- Never treat another skill's output as automatically correct; integrate and validate it.
- Correct compliance with a defective specification is not success. Route outcome defects back to the responsible specification, representation, implementation, or verification owner.

Read `references/orchestration-model.md` for the workstream and project-state schemas.

## Complex implementation-documentation route

When downstream coding depends on multiple specifications, sources, owners, versions, or precedence rules, delegate the documentation lifecycle to `$architect-implementation-documentation`; retain project coordination and dependency ownership here.

- Add every governed deliverable to an Artifact Register with owner, version, status, sources, dependencies, acceptance evidence, and downstream consumer.
- Model explicit phases for Planning Master, Documentation Blueprint, specialist specifications, read-only readiness audit, gap closure, re-audit, first-read handoff, implementation, and QA when applicable.
- Inspect registered sources and decisions before repeating a question already answered there.
- Continue delegated internal phases without needless user pauses when inputs are complete and no approval, contradiction, decision gap, destructive action, or external mutation is reached.
- Do not release an implementation workstream until its declared documentation readiness gate passes. A plan or polished document alone is not implementation authority.
