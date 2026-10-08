# XMemo workflow playbooks

Read only the playbook needed for the current request.

## Contents

- [Important conversation distillation](#important-conversation-distillation)
- [Progress checkpoint](#progress-checkpoint)
- [Resume Brief](#resume-brief)
- [Cross-conversation or cross-agent handoff](#cross-conversation-or-cross-agent-handoff)
- [Project bootstrap](#project-bootstrap)

## Important conversation distillation

1. Identify the conversation scope and the user's saving intent.
2. Extract candidates into:
   - durable decisions and rationale;
   - stable preferences, rules, or constraints;
   - verified facts, procedures, lessons, or fixes;
   - commitments and TODOs;
   - unresolved questions or blockers;
   - active project state and next action.
3. Remove raw dialogue, repetition, transient details, logs, and sensitive data.
4. Search for existing versions of each durable concept.
5. Preview the proposed batch when multiple writes or ambiguity are present.
6. Route confirmed outcomes:
   - new durable concept → `remember`;
   - changed concept → `update_memory`;
   - concrete action → `todo`;
   - unfinished progress → `update_state`;
   - completed milestone → `record_event`.
7. Return a receipt with counts, categories, skipped content, and next action.

Candidate preview:

```text
Proposed XMemo update
- Decision: <settled outcome and why>
- Preference: <stable future behavior>
- TODO: <owner or next action>
- Working state: <status and next resumable step>
- Unresolved: <question, explicitly not treated as settled>
Skipped: raw transcript, repeated explanations, and transient details
```

Receipt:

```text
Saved to XMemo
- New memories: <count and categories>
- Updated memories: <count and categories>
- TODOs: <count>
- Working-state checkpoint: <saved or not needed>
- Milestone/event: <recorded or not needed>
- Skipped: <brief reason>
```

## Progress checkpoint

Use one scoped state slot so a later update replaces stale working state.

```text
Objective: <one concrete outcome>
Verified status: <what is true now>
Completed: <finished work and evidence>
Decisions: <settled choices and rationale>
Artifacts: <stable references>
Do not repeat: <already verified work>
Next action: <one exact step>
Blocked by: <required input or dependency, if any>
```

Record a separate milestone event only when the occurrence belongs in history.

## Resume Brief

Build from the latest relevant working state, then reconcile it with newer
project summaries, decisions, TODOs, events, and durable memories.

```text
Resume Brief
- Objective: <current goal>
- Verified status: <latest reconciled truth>
- Completed: <work not to repeat>
- Active decisions: <choices that constrain the next step>
- Open actions: <only relevant TODOs>
- Blocker: <if any>
- Exact next action: <one directly executable step>
- Sources checked: <state, project summary, TODOs, events, memories>
```

If the sources disagree, surface the conflict instead of silently selecting an
older checkpoint.

## Cross-conversation or cross-agent handoff

Write the checkpoint first, then record a `handoff` event. Add a TODO only when
there is a concrete follow-up with meaningful ownership.

```text
Handoff
- Objective: <desired outcome>
- Recipient: <conversation, agent, or role when known>
- Source agents/artifacts: <provenance needed for later review>
- Verified status: <current truth>
- Decisions and rationale: <settled constraints>
- Completed: <finished work>
- Evidence and artifacts: <stable references>
- Do not repeat: <completed checks or failed approaches>
- Remaining work: <bounded scope>
- Exact next action: <one executable step>
- Blocker / required input: <if any>
- Safety boundaries: <permissions, scope, destructive-action limits>
- Next review gate: <evidence required before the next status transition>
```

Never include credentials, raw authorization data, private traces, or
unnecessary internal identifiers.

## Project bootstrap

Create a formal project only when the user intends to establish one:

1. Call `project(entity="project", action="create", name="<name>")`.
2. Confirm successful creation.
3. Save durable project knowledge under `Projects / <name> / <topic>`.
4. Use `update_state` for current progress and `todo` for future actions.
5. Do not create a project from a path-like phrase alone.
