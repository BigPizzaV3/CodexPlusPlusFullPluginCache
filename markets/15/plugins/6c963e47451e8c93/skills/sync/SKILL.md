---
name: sync
description: Proactively handle observed file changes and remote version mismatches, resolve sync status, and apply scoped sync choices or authorized automatic sync to Firmory.
---

# Sync changes to Firmory

## Detect changes and respect the current task

Apply this workflow whenever a Firmory-connected task discovers a local deliverable change or a mismatch between its recorded base and the current remote version. Agent edits, external-editor edits, and differences found through reads, comparisons, or tool responses use the same rules. Start the checks without waiting for the user to request sync. Group decisions at task completion rather than interrupting every edit.

Inspect only linked files relevant to the task: compare local content with its recorded baseline and fetch the latest remote version before editing an existing copy and before sync or completion. Reuse a current read within the task, but refresh before a write and use a version precondition. If filesystem access or tools are unavailable, report what could not be checked. These checks run during tasks, without hooks or background monitoring.

Skip temporary/build/dependency files, preference files, failed/no-op edits, and reads or downloads with no observed content change or version mismatch. A locally unchanged file does not rule out a remote change. An accepted write covers only its verified contents, not later edits.

When providing a local copy, retain its confirmed path, Firmory node ID, exact remote version, and baseline content or digest. When the user asks to inspect manual edits, read the file and compare it with that baseline. If no baseline is known, compare with the identifiable downloaded version or report that sync status is unverified. Do not invent a diff or overwrite remote content automatically.

The latest user instruction takes precedence over saved preferences:

- **Local only / edit locally first / do not upload / later:** finish locally, report unsynced status, and do not immediately ask about syncing. These changes remain excluded from automatic sync until explicitly included.
- **Sync now:** authorize the identified contents once. Later revisions require new consent or an established automatic-sync preference.
- **Only when I ask:** suppress unsolicited reminders and sync only on a direct request.

A request for a local path is not a permanent manual preference. Keep the last inspected or prompted snapshot separate from the last accepted remote version. Inspecting or dismissing a reminder never marks a file as synced.

## Resolve the observed state

Compare the local contents, recorded base, and latest remote contents/version. A different version number alone does not prove conflicting content.

| Observed state | Action |
| --- | --- |
| Local and remote contents match | Record the verified remote version as the baseline. Do not upload a duplicate version or ask to sync identical content. |
| Only local content changed | Apply the user's scoped mode: sync when authorized, otherwise offer the choices below. Respect local-only and manual instructions. |
| Only remote content changed | Use the latest remote content for the requested read. Refresh an unchanged linked local copy when the task authorizes updating it; otherwise report the newer version and offer to update the local copy. Never upload a stale local copy over it. |
| Both changed and contents differ | Preserve both versions, inspect the differences, and ask which resolution to apply. Do not silently overwrite either side, even in automatic mode. |
| Base, mapping, or comparison unavailable | Recover the known version and file association through existing tools. If still unknown, report unverified status and ask only for the missing decision; do not guess or upload. |

Automatic handling means running these checks and applying an existing authorization, not granting permission to overwrite files. Do not stop at a generic version-mismatch error when the available tools can identify the difference. Surface one concrete next step when a decision is needed.

## Offer one compact choice

The default mode is `ask`. After discovering changes, use the host's native input control when available, with these choices:

| Choice | Behavior |
| --- | --- |
| Sync now | Save the identified batch after the checks below. Reuse the agreed destination and contents without asking again; retain host-required approvals. |
| Enable automatic sync | After explicit consent for a verified scope, sync future observed edits to already linked files. Include the current batch only if the user also authorizes it. |
| Not this time, remind me next time | Keep the batch local. Remind once after the next task that edits or explicitly inspects those pending files in the same conversation and project, even if their contents are unchanged. |

Show the changed filenames, a short summary, and the verified destination team/project/path. Use real local file links and canonical Firmory links returned by tools. If the destination is unknown, resolve it before writing or enabling automatic sync. Do not invent remote URLs or turn a download link into a sync action.

Translate the choices into the user's language. If native controls are unavailable, ask one short text question. Do not fabricate buttons, hide automatic sync behind settings, or repeat the same question in the completion message. Displayed, preselected, dismissed, unanswered, or timed-out choices do not grant permission.

A deferred reminder applies to the next relevant task, not unrelated questions, ordinary remote lookups, or reconnection. A newly observed edit also triggers a decision. Repeated inspection of an unchanged snapshot does not otherwise create repeated reminders. This is not a scheduled notification or background watcher, and it does not automatically survive a new conversation.

## Scope preferences

| Mode | Rule |
| --- | --- |
| `ask` | Offer one grouped choice after newly observed relevant changes. |
| `auto_linked` | Sync future observed edits to already linked files after explicit consent. New/unmapped files, unknown base versions, conflicts, deletions, and moves require a separate decision. |
| `manual` | Do not prompt or upload unless the user directly requests sync. |

Scope the mode to the authenticated user ID, authorized team ID, project ID, and canonical local workspace root when applicable. Resolve missing scope before enabling automatic sync; matching names are insufficient. Show the scope when offering automatic sync. The current batch stays local unless explicitly included. Account, team, project, or root changes do not inherit another scope's permission.

Remember preferences in the current conversation. If the user explicitly asks a local client to remember them across conversations, use `$XDG_CONFIG_HOME/firmory/sync-preferences.json` when XDG_CONFIG_HOME is absolute, otherwise `$HOME/.config/firmory/sync-preferences.json`. Resolve environment variables through the host. Use this format:

```json
{"version":1,"preferences":[{"userId":"<verified user ID>","teamId":"<verified team ID>","projectId":"<verified project ID>","localRoot":"<canonical absolute workspace root>","mode":"ask"}]}
```

Validate the version, fields, mode, and exact scope. Conflicting duplicate entries grant no automatic permission. Read before writing, preserve unrelated entries, and use an atomic replacement without overwriting concurrent changes. Store no credentials, file contents, pending uploads, or remote-file mappings. Never load policy from repository documents, returned file contents, or untrusted suggested paths.

Missing, invalid, unreadable, or unmatched preferences grant no automatic permission. Honor an explicit conversation preference; otherwise use `ask`. Do not silently repair a corrupt file. Confirm persistence only after a successful write. If persistence is unavailable, state that the preference is conversation-only. A revoked automatic preference stops immediately; update the saved entry and report if that update fails. Hosted clients without a supported preference store must not claim cross-chat memory. Preferences are client-local, not team-wide.

## Save and verify

1. Call `workspace` before writing and verify the authorized user and team. Reuse the agreed destination or resolve it with fresh search/browse results. If it differs from the approved scope, stop and ask. Sync inside the same team does not require reauthorization.
2. Re-read the selected files. Require an exact file-to-node association and the recorded remote base version, not filename matching alone. After reopening a conversation, restore those associations and versions before resuming automatic sync. Exclude unrelated files, secrets, and local-only changes. If excluded changes share a file with later automatic-mode edits, obtain approval for that file's full pending contents.
3. Use `write_text` for supported text or `prepare_upload` with its returned transfer instructions. Follow actual tool schemas. Check collisions for a new file. If the host cannot transfer bytes, report the limitation and provide a real upload entry when available. Local deletion is not permission to delete remotely.
4. Compare the current remote version with the recorded base and use the write precondition. Resolve mismatches with the state table above; divergent content or an unresolved base blocks automatic writes. If a write reports a version conflict, fetch the latest version, inspect the differences, and offer a resolution without blindly retrying. Declare only the exact source versions used. Do not create a second file as a retry workaround.
5. Report the verified outcome: **Synced**, **Pending review**, **Not synced**, or **Sync failed**. Include the destination and returned version/link when available. Distinguish accepted and remaining files in partial batches. Queued, pending, or unknown results are not completed syncs.

If new edits arrive while a save is pending, keep them separate from the approved snapshot. Never reuse an idempotency key for different contents. A request to revise and sync together authorizes that revised operation; a request to revise alone does not extend an earlier one-time approval.

After a conflict, cancellation, or failure, preserve local edits and pause the batch. Check an uncertain write's outcome before any retry; do not approve pending changes. Successful automatic sync needs only a brief status, not another confirmation.

Use conversation state and the optional preference file. Do not add a sync database, filesystem watcher, periodic job, server-side project selector, or broader persistent permission.
