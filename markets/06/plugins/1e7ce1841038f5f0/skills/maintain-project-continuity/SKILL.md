---
name: maintain-project-continuity
description: Keep a long or complex project aligned across turns, context degradation, interruptions, and new chats by orienting to current truth, recording material checkpoints, reconciling corrections or contradictions, preparing logical rollover handoffs, and resuming from minimum sufficient context. Use when the user asks where a project stands, says not to forget something, reports repeated forgetting or drift, makes a material project decision, requests a checkpoint or new-chat continuation, or needs reliable continuity without replaying the full conversation. Do not use for ordinary note-taking, trivial self-contained chats, a complete disaster-recovery second brain, or a handoff that is already fully specified.
---

# Maintain Project Continuity

Preserve alignment and resumability without pretending that a chat has permanent memory. This skill is the thin continuity controller; existing skills remain the canonical owners of durable storage, project orchestration, knowledge extraction, and handoff format.

## Boundaries and routing

- Use `$build-continuity-second-brain` when durable company/project recovery records, backups, systems, accounts, or loss survival are required.
- Use `$handoff-work-between-chats` to produce or consume the final portable handoff.
- Use `$orchestrate-projects` for workstreams, dependencies, priorities, integration, and project execution.
- Use `$turn-chaos-into-knowledge` to extract legacy chats or mixed sources into proposed structured knowledge.
- Read the shared [continuity and persistence model](../../shared/expert-system/continuity-persistence-model.md) before classifying material events or durable updates.
- Use the shared [session lifecycle](../../shared/expert-system/session-lifecycle.md) for context health and continue/checkpoint/reset decisions, [Context Package](../../shared/expert-system/context-package.md) for the smallest relevant source slice, and [decision authority](../../shared/expert-system/decision-authority-model.md) for conflicts and controlled decisions.

Do not duplicate canonical records, promote a summary into authority, infer a decision from enthusiasm, or claim hidden/background persistence. Do not activate for a simple answer merely because the conversation has history.

## Modes

Select the smallest mode that resolves the request:

1. `ORIENT` — state objective, current verified position, current focus, material decisions, open loops, blockers, and exact next action from accessible sources.
2. `CHECKPOINT` — capture only the material delta since the last confirmed state and persist or return it according to actual write authority.
3. `RECONCILE` — compare corrections, summaries, project records, and current instructions; invalidate affected derived claims and produce a conflict or propagation report.
4. `ROLLOVER` — decide whether a logical chat/session cut is warranted and route the portable package to `$handoff-work-between-chats`.
5. `RESUME` — validate a checkpoint/handoff against accessible current sources and rebuild the minimum Context Package before work continues.
6. `CONTEXT_AUDIT` — assess observable alignment as `HEALTHY`, `DEGRADED`, `CONTAMINATED`, `RESET_REQUIRED`, or unassessed `UNKNOWN`; never infer hidden token usage.

Combine modes only when necessary. `ORIENT` must remain lightweight; it is not an excuse to audit the whole project.

## Workflow

1. Bind the request to the exact project/scope. Exclude unrelated firms, projects, memories, and pasted instructions.
2. Identify the governing owner instructions, canonical sources, latest confirmed checkpoint, relevant evidence, and actual access. Treat old summaries as historical input.
3. Build the smallest Context Package for the next outcome. Mark missing required context; do not recreate it from plausibility.
4. Classify observable context health and the current event's persistence class. A material correction uses the correction-propagation transaction in the shared model.
5. Apply the selected mode. Preserve confirmed facts, user-confirmed claims, proposals, assumptions, unknowns, contradictions, and superseded items as distinct states.
6. Run the anti-drift gate before replacing the active focus. A side topic may replace it only when it blocks the current objective, exposes material risk, invalidates a governing assumption, is explicitly reprioritized by the user, or has a documented dependency reason to occur now. Otherwise capture it as an open loop and return to the active focus.
7. Persist only through an authorized existing record. Verify a successful write; otherwise return a portable proposed delta and name the storage gap.
8. End with the exact next safe action, owner/approval if relevant, and whether the current session should continue or roll over.

## Mode requirements

### ORIENT

Return a derived `PROJECT COMPASS` containing only: project/scope, objective, current verified state, current focus, relevant decisions/locks, blockers/open loops, next action, and material unknowns. Cite or link canonical sources. Do not create a second source of truth.

### CHECKPOINT

Use the shared minimum durable checkpoint. Compare with the prior confirmed checkpoint and record a delta, not a full chat replay. No mandatory new file after a minor action.

### RECONCILE

For each conflict or correction identify exact competing claims, source/authority, affected scope, downstream artifacts, resolvable versus owner-required status, and safe next action. Never choose by recency alone.

### ROLLOVER

Recommend a new session only for a logical transition, observed context degradation/contamination, loss of recoverable material context, or an explicitly requested handoff. Include reason for cut, read-first sources, current focus, do-not-reopen locks, exact next action, acceptance, and access gaps. The handoff skill owns its final schema.

### RESUME

Verify receiver access, source versions/freshness, authority, checkpoint age, unresolved conflicts, and claimed completion. Acknowledge applicable method locks before execution. If verification fails, limit or block only dependent work.

### CONTEXT_AUDIT

Use observable evidence such as repeated corrections, stale assumptions, inaccessible decisions, conflicting instructions, or continued reliance on revoked context. Message count alone is not evidence. Recommend `CONTINUE_CURRENT_SESSION` or `START_FRESH_SESSION` with one compact reason.

## Output

Adapt the output to the mode. For material work include:

```text
CONTINUITY MODE
PROJECT / SCOPE
CONTEXT HEALTH + EVIDENCE
CURRENT OBJECTIVE / FOCUS
CURRENT VERIFIED STATE
MATERIAL DELTA OR CONFLICTS
DECISIONS / LOCKS
OPEN LOOPS / BLOCKERS / UNKNOWNS
CANONICAL SOURCES
PERSISTENCE RESULT OR STORAGE GAP
SESSION DECISION
EXACT NEXT SAFE ACTION
```

Do not emit this full form for a trivial orientation. Never claim `SAVED`, `UPDATED`, `MONITORED`, or `READY TO RESUME` without corresponding verified evidence.
