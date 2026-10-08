---
name: knowledge-steward
description: Use whenever creating, editing, migrating, reorganizing, superseding, archiving, or otherwise changing durable knowledge in the receiving project's knowledge base.
---

# Knowledge Steward Skill

## Goal
Keep the receiving project's knowledge current, non-contradictory, traceable, portable across AI agents, and cheap to load. Persist durable project truth in canonical project artifacts instead of relying on chat history or assistant memory.

Apply the [receiving-project contract](../../references/project-context.md) when resolving paths, authority, language, and companion skills.

## Trigger
Activate this skill when a task will change durable KB knowledge, governance, lifecycle, indexes, context, decisions, backlog, or work-state artifacts. Do not activate merely to answer a transient question that causes no durable KB change.

## Core rules
1. Source of Truth over chat history.
2. Discussion is not a decision.
3. Confirmed durable decisions are persisted.
4. One canonical home per fact; link instead of copying.
5. Current-state notes contain current truth, not accumulated history.
6. Preserve historical rationale without preserving contradictions in active context.
7. Structured/numeric data stays in its designated live source; KB stores meaning, intent, methodology, assumptions, constraints, and accepted decisions.
8. Prefer updating an existing canonical owner over creating a competing note.
9. Keep lifecycle state separate from evidence/validation state.
10. Read the minimum sufficient context; expand only when uncertainty or validation requires it.

## Required workflow
1. Read the receiving project's available agent guide and current-state artifact if not already loaded; use the equivalents resolved by the project contract.
2. Identify the task domain and read its available context/index. Missing source-KB filenames do not require creating a new taxonomy.
3. Determine the canonical owner using the project's Source of Truth or relevant domain index. Use the bundled [authority reference](../../references/source-of-truth.md) for reusable distinctions when no project equivalent exists.
4. Read only the canonical notes needed for the change.
5. Classify incoming information as discussion, proposal, decision, temporary decision, open question, deprecated, or superseded.
6. For a substantial or ambiguous write, consolidate material facts, decisions, trade-offs, temporary assumptions, unresolved blockers, and exact artifacts to be changed before writing. Obtain owner confirmation when required by scope or uncertainty.
7. Update the smallest canonical artifact set once using the accepted final state.
8. Add/update a durable decision record only when rationale/history has future value; routine edits do not require one.
9. When replacing an older decision or document, mark it superseded/deprecated and point to the replacement; remove it from active/default indexes.
10. Update relevant `_Context.md`, `PROJECT_STATE.md`, active Work state, backlog, and indexes only when their current-state meaning changes.
11. Read back every changed artifact.
12. Run deterministic validation/lint when available.
13. Report what changed and any remaining uncertainty or revisit trigger.

## Context discipline
Default loading order is Hot → Warm → Cold.

**Hot:** `AGENTS.md`, `PROJECT_STATE.md`, relevant domain `_Context.md`.

**Warm:** triggered skills, active canonical GDD/technical docs, active decisions, active work state.

**Cold:** legacy GDD, superseded decisions, historical audits, completed work/session artifacts, raw research, `99_Archive/`.

Never scan Cold knowledge by default. Access it only for migration, history/rationale recovery, conflict investigation, evidence verification, or explicit audit.

## Lifecycle and cleanup
Canonical documents may use `draft`, `review`, `active`, `temporary`, `deprecated`, `superseded`, `archived`. Validation/evidence state is separate. A `review_after` date triggers maintenance review; it does not automatically invalidate a document.

Prefer retain/supersede/archive when historical value exists. Destructive deletion is appropriate only for clear duplicates, empty/stub notes, accidental copies, or intermediate artifacts whose unique evidence/rationale has already been compiled into a canonical owner. Ambiguous destructive deletion requires owner approval.

## Working-state rule
Long or multi-session work must maintain a compact working-state artifact with: goal, completed work, confirmed decisions, current findings, changed artifacts, open issues/blockers, next step. When work completes, move it out of the active path.

## Language
Follow the receiving project's writing policy; default to English for canonical knowledge and the user's language for conversation. Preserve exact IDs, code/config identifiers, paths, and localized player-facing strings when relevant.

## Project governance
This packaged skill supplies the operational method. The receiving project's agent guide and active governance records own local policy and migration state. If a legacy Knowledge Steward document is still active there, reconcile it against that authority rather than assuming it was retired by installing this plugin.
