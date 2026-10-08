# XMemo memory policy

Use this reference to decide whether to save, update, checkpoint, preview, or
skip information.

## Contents

- [Decision matrix](#decision-matrix)
- [Durable memory quality](#durable-memory-quality)
- [Batch-write consent](#batch-write-consent)
- [Progress checkpoint quality](#progress-checkpoint-quality)
- [Conflict and correction rules](#conflict-and-correction-rules)
- [Always skip](#always-skip)

## Decision matrix

| Signal | Action |
| --- | --- |
| Explicit request to remember one safe, unambiguous fact | Save with `remember`, or update the existing memory |
| Stable preference likely useful in future conversations | Save and give a short receipt |
| Final project decision with rationale | Save durable memory; record a milestone only when the decision occurrence matters |
| Brainstorm options before a decision | Organize and review them, but do not save each option as durable truth |
| Approved plan that will guide future work | Save the plan outcome, rationale, scope, and acceptance gate |
| Plan review with a durable verdict | Save or update the governing decision; record the review event when history matters |
| Progress claim from another agent | Preserve provenance, but update verified state only after reconciling suitable evidence |
| Corrected version of an existing fact | Find and update the existing concept |
| Multiple durable candidates extracted from a conversation | Preview the proposed set and confirm before batch writes |
| Ambiguous durability, sensitivity, interpretation, or project placement | Ask before writing |
| Tentative option or brainstorming | Do not save as settled truth; skip or label unresolved |
| Task pauses with meaningful work remaining | Save a resumable `update_state` checkpoint |
| Completed milestone | Use `record_event`; update working state only if work remains |
| Concrete future action | Create or update a `todo` |
| Casual chat or one-turn detail | Skip |
| Secret, credential, or highly sensitive identifier | Never save |
| Financial transaction or subscription | Use `ledger`, not generic memory |

## Durable memory quality

A durable memory must:

- Stand alone without the original conversation.
- Describe one concept when practical.
- State whether it is approved, active, pending, superseded, or unresolved.
- Preserve rationale when it changes future behavior.
- Name the relevant subject or project.
- Avoid absolute claims when the source is uncertain.
- Preserve the source agent or artifact label when it materially helps future
  review, without treating that label as authority.

Preferred shape:

```text
Subject: <project, preference, or decision>
Durable outcome: <what should be remembered>
Rationale: <why it matters>
Status: <approved, active, superseded, pending, or unresolved>
Next implication: <what future work should do>
```

Natural one- or two-sentence prose is preferable when it remains equally clear.

## Batch-write consent

Do not interrupt an explicit request to save one safe memory with redundant
confirmation. Show a candidate preview before writing when:

- A conversation yields several independent memories.
- Some candidates may be personal, sensitive, or short-lived.
- The project or path is uncertain.
- A candidate could overwrite or supersede an existing decision.
- A review would promote an agent-generated draft or progress claim to approved
  or verified status.
- The distinction between a settled decision and an unresolved idea is unclear.

Preview with compact categories:

```text
Proposed XMemo update
- 2 decisions
- 1 working-state checkpoint
- 3 TODOs
- 1 unresolved question (labeled unresolved)
Skipped: raw transcript and transient details
```

## Progress checkpoint quality

```text
Current task: <one concrete objective>
Status: <verified current state>
Completed: <material finished work and evidence>
Decisions: <settled choices>
Next action: <one exact resumable step>
Blocked by: <only when blocked>
Artifacts: <stable references, never secrets or raw traces>
```

Replace the same scoped working-state slot as progress changes. Do not create a
new permanent memory for every intermediate step.

## Conflict and correction rules

- Prefer the user's current explicit correction over retrieved memory.
- Update a changed concept instead of creating a competing duplicate.
- Preserve material rationale and supersession status when history matters.
- Do not merge unrelated concepts merely because they share keywords.
- If two sources conflict and neither is authoritative, report the conflict and
  ask rather than choosing silently.
- Do not let an unverified progress report overwrite a verified checkpoint.

## Always skip

- Raw transcripts and verbatim conversation archives.
- Long terminal output, stack traces, or code dumps.
- Passwords, API keys, bearer tokens, cookies, authorization or MFA codes.
- Payment identifiers, government identifiers, or unrelated personal data.
- Unconfirmed claims presented as verified facts.
