---
name: ando-migrate-messaging
description: Assess and carry out a bounded move from another messaging platform into Ando, selecting a maintained importer, history API adapter, or attributed forwarding route. Use when no dedicated platform migration skill applies.
---

# Migrate from another messaging platform

Read the [shared migration workflow](../../references/migration-workflow.md).
For Slack use [Migrate from Slack](../ando-migrate-slack/SKILL.md); for Buzz use
[Migrate from Buzz](../ando-migrate-buzz/SKILL.md). Identify the exact source
product, workspace, supported export/API, and desired history or live-sync
outcome before choosing a route. Verify source-provider export restrictions
and permissions through current official documentation.

## Pick the route by the required result

- **Maintained importer:** prefer a documented platform-specific importer when
  it meets the requested coverage and fidelity.
- **History import API:** use the current
  [import contract](https://docs.ando.so/developers/api-reference#import-history)
  for original authors, timestamps, and import behavior. A source adapter is
  required; the existence of the API does not mean one already exists for this
  platform. If adapter work is needed, explain it and implement only within
  the user's requested scope.
- **Attributed forwarding:** use the
  [other messaging platforms guide](https://docs.ando.so/docs/other-messaging-platforms)
  for a bounded backfill or ongoing bridge when ordinary messages are acceptable.
  `send_message` creates messages as the authenticated sender at the current
  time; attribution text does not preserve original authorship or timestamps
  as native message metadata. It may notify people or create unread state.

Do not silently downgrade a requested history import to forwarding. Explain
the observable difference and resolve the choice before executing the writes.

## History import

Inspect the current OpenAPI schemas, limits, required owner/admin role, and
`imports:write` scope. Preserve stable source-workspace and record IDs. Import
in dependency order: members, conversations, messages with thread roots before
replies, then reactions. Verify source-to-target IDs and original timestamps
instead of reconstructing them from display text.

For uploaded attachments, verify `files:write`, complete the supported upload
lifecycle, and attach ready file IDs under the current import schema. Retain
source file IDs for deduplication. Check skipped records and readback before
marking an import complete. Reopen a completed import through the documented
route before resuming writes; do not change source IDs to evade a conflict.

## Forwarding or a live bridge

Resolve the target conversation and its membership from the verified Ando
connection. Preserve author, source channel, original time, and source link
in the message text. Inspect the current `send_message` schema; do not copy
legacy flat arguments into a different catalog.

Use a durable checkpoint keyed by source workspace/channel/message ID and
supported target idempotency. Read back uncertain sends before retrying. Verify
pagination and a bounded date window before claiming historical completeness.
Define how edits/deletes, bot messages, files, and duplicates are handled.

An ongoing bridge needs an actual supported event receiver or scheduled
runtime, an owner, and a stop mechanism. Verify it is installed and delivering
authorized events before claiming it is live. Prevent feedback loops when
messages can flow both ways. Keep private-source access aligned with target
membership, and report unsupported features and partial coverage explicitly.
