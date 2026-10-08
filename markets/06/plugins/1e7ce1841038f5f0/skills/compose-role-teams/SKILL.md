---
name: compose-role-teams
description: Create or audit a reusable expert-role blueprint or role prompt with responsibilities, decision rights, conflicts, handoffs, and quality criteria. Use when the deliverable itself is a role team, department simulation, AI persona configuration, or repair of a prompt containing vague or overlapping roles. Do not use for live multi-phase project orchestration, where expert roles must be routed dynamically by task.
---

# Compose Role Teams

Turn an objective into a functional team, not a theatrical list of titles.

## Workflow

1. Extract the objective, deliverable, domain, audience, risk, research need, execution stages, and final decision owner.
2. List required capabilities before naming roles.
3. Group related capabilities. Create a role only when it owns a distinct decision, artifact, evidence source, or quality gate.
4. Default to three to five roles: lead, domain specialist, researcher/analyst when evidence matters, executor/designer, and critic/compliance reviewer when risk warrants it.
5. Define for each role: mission, inputs, outputs, authority, prohibitions, success criteria, and handoff.
6. Define disagreement priority. The lead integrates; safety, law, verified evidence, and explicit user constraints outrank style or optimization.
7. Run the tests in `references/role-tests.md`. Merge redundant roles and add missing ownership.
8. Deliver either a role blueprint, a copy-ready role prompt, or an audit of an existing role list.

## Rules

- Prefer responsibilities over claims such as “world-class expert.”
- Never imply professional licensure. Require qualified human review in regulated or high-stakes contexts.
- Do not create a role solely to repeat another role's review.
- Keep research, creation, approval, and criticism separate only when that separation improves reliability.
- Avoid role-play that obscures uncertainty or source limitations.
- Preserve explicit exclusions and tool/permission boundaries.
- Apply the shared [expert standard](../../shared/expert-system/expert-standard.md), [role registry](../../shared/expert-system/expert-role-registry.md), and [decision-authority model](../../shared/expert-system/decision-authority-model.md) when they fit the requested blueprint.
- Route live project, phase, and task expert selection to `$orchestrate-projects`; this skill produces the reusable team contract and does not manage project execution.

## Output

Return:

1. Objective and assumptions
2. Capability map
3. Role table: role, ownership, inputs, output, authority, handoff
4. Conflict and escalation rules
5. Copy-ready team instruction when requested
6. Lean-team check: roles merged, omitted, or conditional

Read `references/role-tests.md` when building or auditing a team.
