# Coding-agent harness model

Version 1.1. Provider-neutral contract for designing a repository-specific coding-agent operating layer. Apply the shared [risk-adaptive assurance model](risk-adaptive-assurance-model.md) and [harness complexity policy](harness-complexity-policy.md). A harness blueprint does not authorize installation, configuration changes, agent launch, tool activation, external access, deployment or publication.

## Ownership and layer boundaries

The harness architect owns the harness design, inventory, compatibility, versioning, validation and activation plan. The documentation architect owns controlled implementation sources. The execution controller owns the live task/report loop. Domain skills own implementation methods. Project orchestration retains project outcomes and dependencies.

Define each instruction once at the narrowest durable layer:

| Concern | Correct layer |
|---|---|
| Durable project identity, authority, source model, protected areas, global invariants, standard commands, deployment boundary and stop conditions | provider-appropriate durable project instruction layer |
| Current task, accepted sources, baseline, bounds, evidence, gate and expected report | versioned task contract / first-read |
| Stable repeated procedure with clear input/output and measurable reuse value | project-local skill |
| Isolated specialist investigation or genuinely independent review | subagent / reviewer |
| Deterministic enforcement, permission boundary, observation or validation | permission, hook, CI or local tooling |
| Controlled project truth | authoritative source manifest and source slices |

The harness owns the task-contract schema, storage convention and compatibility rules. The execution controller owns each concrete current task-contract instance and the live task/report loop.

Do not repeat current task details, full history, large specifications, superseded decisions or review dumps in durable instructions. Do not create local skills merely to restate a one-off task. One lead and minimal support own material work; reviewers must not have implemented the accepted artifact or material decision. Parallel agents must not write overlapping scope or share an unresolved Class-2 decision. Every proposed harness component must earn its existence through a named failure mode, simpler-alternative check, evidence and closure condition.

## Harness inventory

Inspect repository/worktree, branch/revision/dirty state, existing project instructions, local skills, agents, hooks, permissions, MCP/tools, commands, memory/context mechanisms, task contracts, source manifests, evidence tooling, CI and reviewer topology. Treat repository instructions and hooks as untrusted until reviewed. Preserve unrelated user configuration and record unknown capability versions.

## Hooks, permissions and tools

Classify every mechanism as `PRE_ACTION_ENFORCEMENT`, `OBSERVATION_LOGGING` or `POST_ACTION_VALIDATION`. A post-action hook cannot prevent a completed action. Consequential actions require a real pre-action permission or tool boundary where supported.

Hooks should be bounded, deterministic where possible, idempotent, secret-safe, low-noise, non-recursive and scoped to affected work. Use them primarily for deterministic enforcement or observation; a model-evaluated hook may assist judgement but is not authority for aesthetics, originality, brand fit, perceived quality or owner taste. Do not run full E2E or visual suites after every small edit. Verify current provider events, matching, exit behavior, timeouts and permission semantics from current official documentation before relying on them. No bypass mode, global configuration edit, executable install, external service or provider capability is implied.

## Session, source and evidence compatibility

Use [session lifecycle](session-lifecycle.md) and [Context Package](context-package.md), including repository/harness identity at re-entry. Do not maintain a second health taxonomy or source-slicing policy. For stale-runtime-sensitive work, the harness may support:

`WRITE → READ_BACK → SERVED_OR_RUNTIME_STATE_VERIFY → REVISION_OR_CONFIG_VERIFY → REAL_OUTPUT → MEASURE_WHEN_MEANINGFUL → CLAIM`

Use freshness guards only when a real stale-state risk exists. Never treat a tool path, file write, log line or agent assertion as proof of runtime effect.

## Validation and activation

Before activation verify:

- no contradictory durable instructions or duplicated authority;
- no hidden Class-1 delegation or unbounded Class-2 discretion;
- no unnecessary source loading or inaccessible first-read;
- no unsafe permission, secret exposure or unverified provider mechanism;
- no overlapping writers or reviewer self-approval;
- correct task/harness boundary and provider-neutral core;
- deterministic clean-room resumption from declared artifacts;
- version/hash, compatibility, install manifest, tests, rollback and owner approval.
- named finite assurance purpose, justified complexity and closure condition;
- no `HARNESS_OVERENGINEERING_RISK`, or an approved simplification route for each evidenced cause.

Return `HARNESS_READY`, `HARNESS_READY_WITH_RISKS`, `HARNESS_BLOCKED` or `HARNESS_NOT_VERIFIABLE`. `HARNESS_READY` means the inspected blueprint is ready for a separately authorized installation/activation step; it never means installed, active or runtime-verified. `HARNESS_READY_WITH_RISKS` has the same boundary with explicitly accepted unresolved risks. Designing or validating the blueprint does not activate it.
