---
name: workflow-recovery
description: Plan mutation identities, recover interrupted tool workflows, and distinguish a retry from a new edit without duplicating work.
---

Use this before a multi-step editing job or after a mutation times out. Tabularia
has durable action receipts for specific tools, not a universal transaction for
an assistant's whole task. A JSON-RPC request ID alone is not an idempotency key. Do not infer a failure from silence.

## Before changing anything

Record the chosen project, transport, and caller identity. Name the source Draft
and revision, read the targets, and keep their stable IDs. Save the intended
steps and each returned receipt in a durable record your host can resume. If
your host has no durable task record, say that resuming the whole plan is not
established even when individual Tabularia actions are recoverable.

For every logical operation, generate a fresh requestId before the FIRST call
when the tool supports it. Keep that same ID and the same payload on retries.
Use a DIFFERENT requestId for an intentionally separate operation, even when its
wording is identical. Content equality cannot tell those intentions apart.
Reusing one identity for changed input is refused by the recoverable action
owners. Omitting an optional ID forfeits the reliable caller identity needed
when the first reply is lost.

## Prefer the recoverable owner

- Named-Draft `tabularia_write_draft`, `tabularia_bulk_insert_blocks`, and
  supported bulk deletion return action IDs. Supply requestId from the start.
  Direct Base paragraph rewrites use their existing Snapshot recovery; do not
  describe them as the named-Draft action protocol.
- `tabularia_set_block_style` supports optional requestId and targeted recovery.
- `tabularia_write_sheets`, `tabularia_assign_paragraph_style`, and batch Draft
  filing require requestId. Prefer a Sheet batch over legacy single-Sheet writes
  for a job that needs replay and targeted undo.
- Annotation batches, Anchor batch edits, and story-structure placement require
  requestId and stable entry keys. Prefer these to legacy single comments or
  markers when recovery matters.
- `tabularia_undo_action` uses the original actionId on the same account and
  connector. Call it only when the Writer asks to reverse that action.

Other tools do not inherit these guarantees merely because the storage layer
has Operation IDs. Project creation, import, media addition, and older annotation
or proposal tools have no general caller-provided retry identity. Read their
current state after a timeout; do not blindly repeat them. Name reuse and
setting a value twice are narrower behaviors than durable request deduplication.

## Recover one step

1. Retain requestId, exact payload, entry keys, actionId, and every returned
   revision. Read status fields from reply text or structuredContent.
2. A confirmed durable receipt proves that step was stored. A failed notification
   or optional location lookup does not erase it or prove another device applied
   it. Do not repeat confirmed entries under new IDs.
3. An uncertain outcome means the write may have committed. For a recoverable
   tool, repeat the original request identity to inspect/recover its receipts.
   A tokenless batch retry stays a preview; it does not resume pending writes.
4. Inspect succeeded, partial, failed, uncertain, and unattempted entries and
   their stage IDs. Some hosted actions commit per item or stage. Never call a
   partial batch atomic or pretend later steps ran after an unconfirmed one.
5. Obtain any required fresh preview and conversational confirmation before
   resuming still-pending writes. Expired tokens or changed targets require a
   new preview. A token is a fingerprint, not independent human authorization.
6. Re-read on a revision or affected-field conflict. Never replace the expected
   revision with the latest one just to force stale intent through.

An action retry and task restart are different. Tabularia retains the action's
journal/receipts; your host must retain which actions the larger plan intended
and which step comes next. A Snapshot is a recovery cut, not a workflow cursor,
and restoring it can discard unrelated work. Prefer selective action undo.

## Keep reading sessions separate

`tabularia_read_next_published_sentence` advances an ephemeral reading position
on each call. It is annotated read-only for the voice loop, but repeating the
call is not a replay guarantee: it can fetch the following sentence. Do not
speculatively retry a lost sentence response as though it had a requestId.
Session position/seekVersion can be inspected; that does not establish exactly
which audio the external host spoke. Never invent audio progress to fill a gap.
