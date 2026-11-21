# Local protocol

The plugin root is two directories above this skill. Run helpers from the selected project, not the plugin directory. The installed plugin's trusted hook supplies `data_dir` and current session identity after `identity`; these values must not be guessed from a global latest-session file. Root paths in the local command are local-only and are never journal payloads.

```text
node "<plugin-root>/scripts/action-room.mjs" identity
node "<plugin-root>/scripts/action-room.mjs" <command> --data-dir "<host data_dir>" --session "<host codex_session_id>" --project-key "<host project_key>"
```

| Command                       | Input on stdin                                                                                                             | Result                                                                                |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `bind`                        | Exact successful server state with `ok`, `binding`, and `room_id` (or `session.room_id`)                                   | Bound IDs; rejects a different active Room                                            |
| `layout`                      | Current successful server state with matching active binding, `workspace.title`, and complete ordered `tasks`              | Creates/reuses project and task folders; returns only relative folder paths           |
| `task-dir --task <UUID>`      | None                                                                                                                       | Task `relative_dir`, separate `support_dir`, exact saved `legacy_artifacts`           |
| `pending`                     | None                                                                                                                       | Up to 50 events, remaining count, incomplete flag, binding fields                     |
| `ack`                         | Successful server response with `ok`, matching `binding.id` (or `binding_id`), and `accepted_event_ids`                    | Deletes only those accepted local event files                                         |
| `event`                       | `{ "event_id": "...", "task_id": "...", "type": "progress", "summary": "Reviewed the available sources." }`                | Saves a bounded progress or needs_input event for retry                               |
| `checkpoint --read true`      | None                                                                                                                       | Last durable task checkpoint or null                                                  |
| `checkpoint --work <UUID>`    | Same checkpoint payload; `--read true` reads it                                                                            | Independent follow-up artifact/submission checkpoint; preserves the report checkpoint |
| `goal-checkpoint`             | `{action,payload}` before a goal mutation; `{receipt:<exact response>}` after acceptance                                   | Saves the exact mutation and acknowledges only its returned ID and binding            |
| `goal-checkpoint --read true` | None                                                                                                                       | Last pending/acknowledged goal mutation for safe retry                                |
| `checkpoint`                  | Task ID/stage, artifact IDs with the exact file manifests below, and the exact redacted submission summary when submitting | Saves bounded recovery metadata; never signed URLs, credentials, or raw logs          |
| `unbind`                      | None                                                                                                                       | Disables collection; preserves history; does not stop execution                       |

Checkpoint stages: `working`, `external_effect_done`, `artifact_pending`, `submission_pending`, `submitted`. Write `external_effect_done` immediately after an irreversible authorized operation succeeds so a reporting retry never repeats it. On uncertain external outcomes, inspect read-only provider state before taking another action. The local checkpoint does not replace durable provider receipts.

## Project and task folders

After `bind`, run `layout` with the current server response. Run it again on resume to check the immutable task IDs/order and finish any interrupted directory creation. It uses `workspace.title` (fallback `Action Room`), not the local binding label or Codex session ID. It preserves Korean names, sanitizes Windows filenames, and uses the report's zero-based `sort_order + 1` with at least two digits. Existing unrelated folders are never adopted; name collisions receive a short Room suffix. Excessively long base paths require a shorter selected project path.

The single mapping is `<selected folder>/.action-room/layouts/<room_id>.json`. It survives conversation changes; reusing it still requires a current active server binding. Project/task names are frozen after allocation. Never edit this mapping or checkpoint manifests to rename/move reserved files. Do not upload it as a deliverable.

`task-dir` returns e.g. `relative_dir: "프로젝트/01_상담 기록 검토"` and `support_dir: ".action-room/work/<room_id>/<task_id>"`. Use these values as filesystem paths through normal APIs, never as interpolated shell code. Result generators must write deliverables into `relative_dir`; keep inspection NDJSON, preview images, build scripts, and temporary files in `support_dir`.

Only the exact current pre-layout checkpoint's artifacts are grandfathered at their original paths. Preparation never moves files, changes the checkpoint, submits work, or copies arbitrary project contents. Without a layout, the updated artifact/upload helpers can still replay exact existing checkpoint files. Other older drafts or reservations require explicit reconciliation; do not re-reserve a file merely to bypass a path check.

Before artifact reservation, save every artifact ID with its file mapping. Before submission, also save the exact summary and submission ID:

```json
{
  "task_id": "<task UUID>",
  "artifact_ids": ["<artifact UUID>"],
  "artifacts": [
    {
      "artifact_id": "<same artifact UUID>",
      "relative_path": "프로젝트/01_상담 기록 검토/evidence.json",
      "file_name": "evidence.json",
      "content_type": "application/json",
      "size_bytes": 321,
      "sha256": "<actual lowercase SHA-256>"
    }
  ],
  "submission_id": "<submission UUID>",
  "submission_summary": "The authorized operation succeeded; the selected provider receipt was checked.",
  "stage": "submission_pending"
}
```

The summary is the exact text that will be sent as the submission's `summary`; do not reword it on replay. The helper allows at most 20 artifact mappings, 8,000 summary characters, and 64 KiB per checkpoint. Paths must remain relative without parent traversal. Each artifact ID's manifest and each pending submission ID's payload are immutable within the task. To resume after lost context, read this checkpoint and server state, verify current file bytes against the saved mapping, and reuse the same reservation/confirmation/submission inputs. If metadata, local bytes, or server evidence are missing or disagree, hold reporting and ask in Codex. Never reconstruct guessed metadata or rerun a successful external operation to recover reporting.

For an enabled goal, each `checkpoint --work <work_id>` uses the original source task ID but its own file and submission ID. Use the source task folder's `followup-<work_id>` subdirectory for new files. Add `goal_work_id` to server artifact preparation/confirmation; submit with the goal tool rather than replacing the report submission. Goal mutation checkpoints are bounded to 60 KiB, exclude credentials, and retain an immutable copy for each mutation ID. If the server definitively rejects a mutation with a helper-allowlisted error, record `{rejected:{mutation_id,code:<exact error code>}}` before preparing a corrected payload. A revision conflict requires a fresh state read. No timeout or lost response qualifies as rejection.

Pass ordinary JSON through stdin with actual JSON serialization. Quote local paths according to the current shell, including spaces. Never assemble shell code from server-returned free text. The helper trusts only allowlisted binding fields, IDs, and local scope; backend authorization remains the server's responsibility.

## Upload a chosen file

```text
node "<plugin-root>/scripts/action-room.mjs" artifact --data-dir "<host data_dir>" --session "<host codex_session_id>" --project-key "<host project_key>" --task "<task UUID>" --file "<task relative_dir>/result.pdf"
node "<plugin-root>/scripts/action-room.mjs" upload --data-dir "<host data_dir>" --session "<host codex_session_id>" --project-key "<host project_key>" --task "<task UUID>" --file "<task relative_dir>/result.pdf" --sha256 "<artifact sha256>" --content-type "application/pdf"
```

The second command must run in an interactive PTY (`tty: true`) when using `exec_command` plus `write_stdin`. It disables terminal echo before printing `{"ready_for_upload_url":true}`. After that message, send exactly one JSON line containing `{"upload_url":"<prepare_artifact upload_url>"}` to the running process through `write_stdin`. Forward the tool result programmatically without printing it. Never use `echo`, a command-line URL, or a terminal that has not returned the readiness message. No bearer token is needed or accepted. The helper restores terminal mode and returns only filename, size, and SHA-256. If a direct stdin transport is available, it can also accept the one-line input without a PTY.

The signed URL is a short-lived capability for the selected artifact. Do not expose it in user messages, logs, committed files, or checkpoints. Preparation and upload are not task completion. `action_room_complete_artifact` must verify the stored bytes before submission references the artifact.

## Delivery semantics

Retry pending records with their existing IDs and acknowledge only IDs accepted by the server. Preserve unacknowledged records after an interrupted delivery. Never substitute another conversation's identity or activity.

If `pending.incomplete` is true, disclose the activity gap even after later successful synchronization. Offline records are delivered at the next active Codex checkpoint; there is no background synchronization.

OAuth and hook trust are separate. The package can be validated without either; a live integration still requires the deployed MCP endpoint, DXIR OAuth login, installed Node.js, enabled/trusted hooks, and a user-selected Room.
