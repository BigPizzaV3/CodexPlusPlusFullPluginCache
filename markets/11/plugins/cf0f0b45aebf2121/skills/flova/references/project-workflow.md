# Project Workflow

Read after choosing the project workflow or when continuing an existing project. Give Flova Agent the creative goal and necessary constraints so it can plan, organize, and advance production within the project.

## 1. Select a Project and Read Context

Continue an existing project in that project. Find it with `creation_project_list` when needed, retaining the same `scope` and returned `next_cursor` across pages; do not mix page and cursor.

Use the returned `api_version` to select matching tools, or `creation_project_runtime` when the version is unknown. Do not infer it from a project ID or migrate implicitly. If the matching legacy tools are unavailable, explain the limitation and let the user choose whether to migrate; see the tool reference for explicit migration.

When a new project is needed and the goal is clear, call `creation_project_create` with a concise `name`; keep the default `permission_mode` unless the user chooses otherwise.

For V3, call `creation_project_info` first for permissions, epoch, and necessary context. Locate content with `creation_project_graph` or `creation_project_search`, inspect exact nodes with `creation_project_nodes`, and read text through `creation_document_search` / `creation_project_document`. V3 Documents are selected by `node_id`, not a fixed `final_video_spec` entry point. Read Asset candidates through `creation_asset_resources` and final-video timelines through `creation_composition_get`.

Follow pagination and preserve revisions; a partial read cannot serve as a full replacement payload. On conflict, reread authoritative state before deciding whether to retry.

Projects may have multiple conversations with independent discussion histories and shared documents, assets, and edits. Select one with `creation_conversation_list`, or use `creation_conversation_create` for an independent request. Retain `conversation_id` in supported run, history, status, result, and interaction calls; continue each run and its pending actions in their original conversation.

## 2. Delegate Creation and Ordinary Revisions

Use `creation_run` to give Flova Agent the first creative goal and ordinary revision feedback. Pass `project_id`, the selected `conversation_id`, `content` or structured `parts`, and uploaded materials in `files`.

Express the goal, reference uses, feedback, and what to preserve or change, retaining the user's model choices and review checkpoints. Retry the same submission with the same request ID and input; query the original run after a timeout.

For staged project work, follow the applicable stages in order: storyboard, key elements and visual references, keyframes, video shots and audio, timeline assembly, then export. Review at agreed checkpoints; for one-pass delivery, let Flova Agent advance within the user's authorization without adding default stage-by-stage pauses.

Server-side Flova creative Skills are distinct from the installed plugin Skill, local helpers, and inspiration IDs. Find and read a suitable server-side Skill through the list, feed, categories, or detail tools; bind its verified `skill_id` or `skill_share_code`, not both. Preserve that binding on ordinary revisions unless the user requests a change.

## 3. Track the Run and Its Resources

After `creation_run` or `creation_run_resume` returns `stream_chat_id`, keep tracking that same run:

1. Call `creation_run_status` first with the project, conversation, and stream IDs, without `from_message_id`. V3 has no legacy event, preview, or resource-link switches.
2. Save `next_event_id`, pass it as `from_message_id` on the next call, and replace it with the newly returned cursor.
3. Follow actual run state and `terminal`, respecting polling intervals. Quiet progress or an empty increment is not completion or a reason to resubmit.
4. Independently refresh observed unfinished media tasks with `creation_resource_status`, up to 100 task IDs per call, regardless of event cursors. Use `creation_resource_info` for individual media details and permitted URLs. Preserve epoch, node, and content revisions where required.
5. When the first resource succeeds, present it under the main Skill's host-specific delivery rules, continuing to track the run and later resources. In Claude Code and other hosts, use `creation_resource_status` and `creation_resource_info` to obtain actual media or permitted URLs. In Codex, when `creation_media_preview` is exposed, an existing card can discover later tasks, or additional cards can show new results and meaningful production stages; there is no one-card-per-run limit. Do not repeatedly present unchanged media.
6. At a paused or terminal state, call `creation_run_result` for results, errors, resources, and pending actions. Use `creation_chat_pending_actions` if the current decision is unclear; do not ignore a V3 decision just because it lacks a `blocking` field.

Deduplicate by resource ID, state version, and media type, falling back to resource ID and media type when no state version exists. Retain unsuccessful deliveries. Across interruptions, preserve the project, conversation, stream, cursor, media tasks, and preview state and recover the original run.

## 4. User Answers and Service Approvals

For a server-issued pending question, call `creation_run_resume` with its exact `action_id` and supported `option_id`, `free_text`, or ordered `answers`. Each ordered answer uses `selected_values` and/or `free_text`; do not mix ordered and single-answer fields.

Submit service approvals through `creation_interaction_submit` with the returned `interaction_id`, the user's actual response, and a stable `client_request_id`. Obtain the user's answer before submitting either questions or approvals; ordinary revision feedback still goes through `creation_run`.

## 5. Select a Project Preview Source (Codex Only)

Use this section only in Codex when `creation_media_preview` is exposed. In Claude Code and other hosts, present resources from the normal status and resource-detail tools, then continue to review, timeline assembly, or export. Do not wait for a card to proceed with an authorized workflow.

Once resources have succeeded, call `creation_media_preview` with `source="project"`:

Use identifiers returned by the service, not creative instructions, arbitrary URLs, or generation request IDs.

- For a card that follows an active run, prefer its exact `project_id`, `conversation_id`, and `stream_chat_id` so the card can discover later tasks. Add previously observed `task_ids` when needed, including pending tasks.
- For a separate card focused on a group of existing resources or a production stage, use the project ID and that group's observed task/resource IDs without a run selector that would expand the selection. Resource IDs are not asset node or inspiration IDs. Explicit task and resource IDs combined are limited to 100. This selection does not replace ordinary run-status tracking.
- Retain `expected_epoch` when supplied. Preserve observed task/resource IDs if events have expired rather than silently selecting another run or project.
- `from_message_id` and `next_event_id` belong only to ordinary progress queries, not preview. Run-scoped preview uses its own event-reading range.
- Project previews may return both `resource_states[]` and `resources[]`; check both. Follow the main Skill for display and refresh; preview does not replace progress polling or approval.

## 6. Review, Timeline, and Export

Present actual resources at agreed checkpoints, obtain feedback, and continue revisions through `creation_run`. Partial resource success is not a successful creative run.

Flova Agent can assemble or revise the timeline after the required resources are ready. Read tracks, clips, settings, and diagnostics with `creation_composition_get`; Sequence order alone is not the final-video timeline. Retain `expected_node_revision` across pages until the read is complete.

When the creative run succeeds, pending decisions are resolved, and export is within the user's authorized goal, call `creation_export_readiness` for the target Composition. Only when `ready=true`, pass its exact `composition_node_id`, `expected_node_revision`, and a stable `client_request_id` to `creation_export_video`.

Save the export `task_id` and track `creation_export_status` to terminal. Retry the same export with the original revision and request ID. Recover a lost response with either the task ID or client request ID, not both. Acceptance is not completion.

For a user-requested project-resource archive, use `creation_download_all` and `creation_download_status` with the same request-ID and recovery rules. An archive does not replace final-video export; individual asset delivery needs no export.

Only after export or download returns `status="done"` and an output URL, deliver that actual output. In Claude Code and other hosts, use the returned playback or download link. In Codex, when `creation_media_preview` is exposed, open a preview using its existing task: `source="export"` or `source="download"`, plus the project ID and operation's `task_id`. Preview submits no new export or archive; do not resubmit to show a card.

Deliver the service-returned project link and a brief summary alongside the media or links supported by the current host, explaining whether the user can review, revise, continue production, or download. Follow the main Skill's host-specific display rules for links and display failures. Obtain a missing project link through a project read rather than constructing one.

## 7. Cancellation, History Restore, and Branching

On user-requested cancellation, call `creation_run_cancel` for the exact run and track it to terminal. Cancellation does not undo completed work or consumed credits.

For a requested restore, have the user select the historical message and restore mode, call `creation_project_restore_preview`, explain its impact and obtain confirmation, then call `creation_project_restore` with the matching `preview_token`. Obtain a new preview if it expires or the project changes.

`creation_project_branch` creates another project; `creation_conversation_branch` creates another conversation in the same project. Choose according to the user's request. Authentication, quota, and failure handling follow the main Skill's shared rules.
