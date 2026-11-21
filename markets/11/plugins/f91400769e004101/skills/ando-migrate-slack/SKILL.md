---
name: ando-migrate-slack
description: Plan and guide a move from Slack to Ando using native Slack sync, verified channel and identity mappings, a pilot, and cutover checks. Use for Slack migration or history-backfill requests.
---

# Migrate from Slack

Read the [shared migration workflow](../../references/migration-workflow.md).
Use the current [Slack import and sync guide](https://docs.ando.so/docs/importing-from-slack)
to verify setup, supported channels, history coverage, and message support.

## Choose the supported path

Ando's documented native route is **Settings → Slack sync**: connect the
authorized Slack workspace, select accessible public or private channels
(including Slack Connect channels), and map them to new or existing Ando
channels. Private channels require the private-channel consent scopes and the
viewing member's own Slack access; review the destination membership before
enabling private sync. DMs are not selectable. The documented backfill is up to
180 days and runs in the background. Verify current behavior and access before
quoting these limits; do not promise a whole-workspace or unlimited-history import.

If the user needs history beyond native backfill or unsupported DMs, assess an authorized
export and a supported history-import route separately. Do not imply Slack
admin rights, export availability, or an existing ZIP importer without evidence.
If no supported executor is available, produce the mapping and explain the
specific manual/operator step instead of inventing an MCP migration tool.

## Pilot and read back

Start with a selected public channel when authorized. Review its target
membership before mapping a Slack Connect channel; shared-channel history
must not become visible to unintended people. Check identity matches, source
links, representative history, and channel-level sync/backfill progress in
Settings. Verify new-message delivery separately from historical coverage.

Outbound posting is workspace-dependent. Check availability and the sending
member's Slack connection before testing it. The documented outbound route
supports new human text messages, not all edits, deletes, files, reactions, or
agent-authored messages. Do not infer two-way fidelity from inbound sync.

Keep existing mappings and checkpoints for resume. Disconnecting stops sync
but retains synced messages, members, and paused mappings; it is not an undo.
Guide the requested cutover only after coverage and gaps are understood.
