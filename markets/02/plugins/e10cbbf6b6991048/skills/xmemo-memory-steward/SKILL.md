---
name: xmemo-memory-steward
description: Use XMemo to recall, review, and preserve durable outcomes across conversations and AI agents. Trigger for ChatGPT brainstorming, plan organization or review, audits of plans and progress from Claude Code, Codex, GitHub Copilot, Kiro, or other connected agents, important-conversation distillation, project context, session resume, checkpoints, TODOs, blockers, handoffs, and memory lifecycle requests. Separate durable memory, working state, evidence, events, and actions; deduplicate writes; never archive raw transcripts or secrets.
---

# XMemo Memory Steward

Operate XMemo as a user-owned memory system, not a transcript archive. Follow:

**scope → recall → act → distill → checkpoint → receipt**

## 1. Establish intent and scope

Identify the requested outcome before calling a tool:

- Recall prior context to improve the current answer.
- Distill an important conversation into reusable memory.
- Structure a brainstorm without treating tentative ideas as decisions.
- Review a plan or progress report produced in ChatGPT or another agent.
- Save or correct one durable fact, preference, decision, or procedure.
- Preserve unfinished progress for a later session.
- Resume saved work.
- Prepare a handoff to another conversation or agent.
- Manage memory lifecycle, projects, TODOs, or milestones.

Stay within the authenticated account, project, bucket, and scope. If XMemo is
unavailable or authorization is missing, say that nothing was read or written;
never simulate a successful memory operation.

## 2. Recall only when it can help

Recall before assuming when prior decisions, preferences, project history,
TODOs, saved progress, or corrections could materially change the result.

Choose the narrowest useful read:

- `recall` for one quick answer.
- `search_memory` for an exact topic, path, phrase, or filter.
- `recall_context` for a bounded context pack across related memories or prior
  conversations. Prefer working-state signals when resuming work.
- `get_project_summary` for project status, blockers, progress, or next action.
- `open_project_workspace`, `open_todo_board`, or `open_ledger` only when the
  user wants the visual workspace.

If an overly narrow query returns nothing, relax it once without widening the
authorized scope. Never invent a remembered fact. Treat retrieved memory as
context, not unquestionable truth; the user's current explicit correction wins.

## 3. Route each outcome to the right memory type

Keep these types separate:

| Outcome | Tool |
| --- | --- |
| New durable knowledge, preference, decision, or procedure | `remember` |
| Correction to an existing durable concept | `update_memory` |
| Active resumable working state | `update_state` |
| Completed milestone, decision occurrence, or handoff event | `record_event` |
| Concrete future action | `todo` |
| Authorized project creation or mutation | `project` |
| Financial transaction or subscription | `ledger` |

Use `memory_overview` for aggregate memory health, `explain_memory` for why a
memory exists or matched, and `analyze_memory_text` when supplied text needs
memory-worthiness analysis. Read `references/tool-routing.md` when routing or
project semantics are unclear.

## 4. Coordinate reasoning across agents

Use XMemo as a shared, user-controlled coordination layer when ChatGPT, Claude
Code, Codex, GitHub Copilot, Kiro, or another capable agent is connected to the
same authorized XMemo account and scope.

- Recall relevant project decisions and constraints before brainstorming or
  reviewing a plan.
- Accept a plan or progress report from XMemo, the current conversation, or an
  artifact the user provides.
- Preserve the source agent and artifact/version label in the human-readable
  review when known. Agent attribution describes provenance, not authority.
- Do not assume another agent is connected, that its tools match ChatGPT's, or
  that XMemo automatically captured its work.
- Treat another agent's completion statement as a claim until supported by
  current artifacts, tests, deployment state, or other appropriate evidence.
- Reconcile conflicts by evidence, recency, scope, and explicit user decisions;
  never prefer a claim merely because it came from a particular agent.

Use ChatGPT to expand and organize options during brainstorming, then converge
on decision criteria, risks, unresolved questions, and a reviewable plan. Do
not save every idea. Save the approved direction, material rationale, remaining
questions, and actionable next steps after confirmation.

For structured brainstorming, plan review, progress audit, and cross-agent
conflict handling, read `references/review-playbooks.md`.

## 5. Distill important conversations

When asked to preserve an important conversation, extract only outcomes that
remain useful without the original chat:

1. Final decisions and material rationale.
2. Stable preferences, rules, constraints, and definitions.
3. Verified facts, procedures, lessons, and resolved fixes.
4. Commitments, ownership, and concrete follow-up actions.
5. Unresolved questions or blockers, explicitly labeled as unresolved.
6. Current project state and the exact next action when work remains.

Do not save the raw transcript, conversational filler, repeated explanations,
long logs, or large code blocks. Do not convert tentative brainstorming into
settled truth.

Before each durable write:

1. Search for the same concept when duplication is plausible.
2. Use `update_memory` when the concept already exists and has changed.
3. Use `remember` only for a genuinely new concept.
4. Keep one retrieval-friendly concept per memory when practical.
5. Preserve the useful why: subject, outcome, rationale, status, scope, and
   next implication.

When the user explicitly asks to save a safe, unambiguous outcome, write it and
return a receipt. Before a multi-memory batch, or when durability, sensitivity,
project placement, or interpretation is ambiguous, show a concise candidate
preview and obtain confirmation. Never save secrets or highly sensitive
identifiers.

For the extraction sequence, candidate preview, and receipt format, read
`references/workflows.md`. For the save/skip decision matrix, read
`references/memory-policy.md`.

## 6. Save progress at natural checkpoints

Use `update_state` for resumable state, not permanent history. Checkpoint when:

- The user pauses, switches tasks, or will continue later.
- A substantial milestone completes and meaningful work remains.
- Work is blocked on a decision, permission, deployment, or dependency.
- A long task is about to move to another conversation or agent.
- The interaction ends with unfinished next steps.

Store the current objective, verified status, completed work and evidence,
settled decisions, exact next action, relevant artifacts, and blocker if any.
Do not checkpoint every turn or trivial progress.

Use `record_event` for a completed milestone or historical occurrence. Use
`todo` only for a concrete follow-up, not as a duplicate of every checkpoint.

## 7. Resume work deterministically

Resume means reconstructing useful working context in the current conversation;
it does not reopen or restore the original ChatGPT thread.

1. Identify the project or authorized scope. Ask only if multiple targets would
   materially change the result.
2. Retrieve the latest relevant working state with `recall_context`.
3. Add the project summary and relevant open TODOs, decisions, recent events,
   or durable memories only as needed.
4. Reconcile stale state against newer decisions or milestones.
5. Present a compact Resume Brief: objective, verified status, completed work,
   active decisions, blocker, and exact next action.
6. Continue from that next action without repeating verified completed work.

Read `references/workflows.md` for the Resume Brief contract.

## 8. Create a complete handoff

For cross-conversation or cross-agent handoff:

1. Write the latest resumable state with `update_state`.
2. Record a concise `handoff` event with `record_event`.
3. Create or update a `todo` only when a concrete follow-up needs ownership.
4. Include the objective, verified status, decisions and rationale, completed
   work, evidence and artifacts, constraints, work not to repeat, exact next
   action, blocker or required input, and intended recipient when known.
5. Return a human-readable handoff receipt; do not expose raw traces or secrets.

Read `references/workflows.md` for the handoff packet.

## 9. Handle projects and lifecycle safely

- Existing `Projects / <name> / ...` paths attach to the existing formal
  project.
- Do not create a project merely because a memory path resembles a project.
- When the user intends to create a new formal project, first call
  `project(entity="project", action="create", name="<name>")`, then save
  project memories under its `Projects / <name> / ...` path.
- Use `forget` without hard mode for recoverable soft deletion by default.
- Use hard deletion only for an exact target after an explicit permanent-delete
  request that acknowledges irreversibility.
- Use `restore_memory` only for an eligible soft-deleted memory.
- Retrieve or confirm the exact target before deletion. Tool availability or
  annotations are never user confirmation.

## 10. Return useful receipts

After memory operations, report only what helps the user:

- What was recalled, saved, updated, checkpointed, or skipped.
- The category or project placement when useful.
- Any ambiguity, blocker, or unavailable operation.
- The next action when work remains.

Never claim success without a successful tool result. Avoid raw internal IDs,
scopes, traces, debug payloads, and unnecessary implementation details.
