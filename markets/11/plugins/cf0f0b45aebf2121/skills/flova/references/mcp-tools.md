# Creation V3 MCP Tool Reference

Read only the category relevant to the current task. Tool names below omit host-added connector namespaces. The connected schema is authoritative for parameters and capabilities; do not assume the deployed backend exposes every tool listed here. Creation modes and shared operating rules are described in the [main Skill](../SKILL.md).

## Differences from the Legacy Plugin Contract

- Tool names use the `creation_` prefix. Read project content through graphs, nodes, search, Documents, Assets, and Compositions.
- `creation_project_create` accepts `name` and optional `permission_mode`.
- `creation_run` accepts either `content` or `parts`, plus files, conversation, Skill selection, and `client_request_id` as supported.
- Pass the previous `next_event_id` as `from_message_id` for progress. Use `terminal` to identify completion; media tasks may need independent refreshes.
- Answer questions with `creation_run_resume`; submit approvals and other interactions with `creation_interaction_submit`.
- Export requires the exact Composition ID, node revision, and `client_request_id`.
- Restore requires a preview token matching the selected message and mode.

## Entry Points, Account, and Projects

| Tool | Behavior and constraints |
| --- | --- |
| `creation_open_home` | Codex-only UI entry point when exposed. Open Flova home without creating a project or starting generation. In Claude Code and other hosts, use the exposed list or feed tools instead. |
| `creation_account_user` | Read identity, subscription, and credits before generation or export when entitlement is unknown. Follow the packaged quota and no-upsell policy in SKILL.md; stop blocked operations without automatic retry. |
| `creation_project_create` | Create a V3 workspace when the project workflow has been selected and a new project is needed. Keep the default permission_mode unless the user chooses another mode. |
| `creation_project_list` | List accessible projects with scope all, v2, or v3. Retain scope while following next_cursor; do not mix cursor and page. Use each project's api_version to select its tool family; never migrate implicitly. |
| `creation_project_runtime` | Resolve an existing project's API version when it is not known, before choosing the matching exposed tool family. This read never migrates the project. |
| `creation_project_migrate` | Only when the user chooses project migration, use mode="reuse" with a stable client_request_id and the source project ID. Reimport requires an explicit request; retry a failed job with its migration_job_id. Do not use migration as an automatic fallback for missing legacy tools. |
| `creation_project_migration_status` | Track migration and use the returned V3 project ID after success. |
| `creation_project_info` | Read project metadata, epoch, revision, permission mode, and required approvals. |

## Models and Quick Generation

| Tool | Behavior and constraints |
| --- | --- |
| `creation_generation_models` | Discover executable image, video, audio, or music models. Use detail=full to check parameters, capabilities, input roles, and access requirements before generation. |
| `creation_quick_generate` | Preferred entry point for directly generating media with a selected model or revising a prior quick output, without creating a project. Pass prompt, model, capability, supported params, and inputs[].file_ref for uploads or inputs[].resource_id for observed outputs, with supported roles. The calling agent can organize multiple steps and review checkpoints. An observed source_task_id or source_resource_id supplies omitted recipe fields. Reuse client_request_id for the same submission; a new revision gets a new ID. Follow required preparation and server-issued confirmation before retrying that same submission. |
| `creation_quick_status` | Read by batch_id, task_ids, or the original client_request_id. Respect poll_after_seconds and check terminal plus each task's status and resources. Accepted or processing is not success. Present successful resources without waiting for all tasks to finish: in Claude Code and other hosts, use the actual media or links in tasks[].resources[]; only in Codex with the preview tool exposed, use creation_media_preview with the batch or a selected task group. This status query does not open a card on the updated server. |
| `creation_quick_history` | Read paginated quick history with unchanged filters. First use may require preparation; preserve returned task/resource IDs for subsequent generation or revisions. |
| `creation_quick_cancel` | Cancel the exact batch when requested. Completed outputs stay available; charges follow actual settlement. |
| `creation_quick_migration_status` | Observe the preparation job identified by migration_job_id. This never starts generation; on success retry the original quick operation with the original request ID. |
| `creation_quick_migration_retry` | Explicitly retry failed or cancelled quick history preparation when requested by the user. Reuse the request ID if its response is lost; do not automatically loop. |

## Media Preview

| Tool | Behavior and constraints |
| --- | --- |
| `creation_media_preview` | Codex only, when exposed. Claude Code and other hosts use normal status/resource results and returned links instead. Query readiness first and open after the first resource succeeds. Multiple cards per batch/run may show newly available results, production stages, requested groups, or display recovery. Use run/batch selectors for ongoing discovery or observed task/resource IDs for a focused group. Supports quick, project, export, and download sources; the card refreshes through data.refresh and merges by ID. Do not reopen unchanged results on every poll. It does not start generation, approve, or resume a run. Shared display and refresh rules are in the main Skill; source selectors are in the quick-generation and project-workflow references. |

Ordinary media and status queries no longer declare media UI on the updated server. The connected schema remains authoritative; older deployments may not expose the explicit action.

## Conversations and the Project Graph

| Tool | Behavior and constraints |
| --- | --- |
| `creation_conversation_list` | List conversations to select the one to continue. |
| `creation_conversation_create` | Create a conversation for another independent creative request. |
| `creation_conversation_branch` | Branch from a specified message into a new conversation in the same project. |
| `creation_chat_history` | Page through the selected conversation's history; verify restore anchors through restore preview. |
| `creation_chat_pending_actions` | Read only currently valid questions or approvals in the selected conversation. |
| `creation_project_graph` | Read a bounded graph overview, follow page.continuation, and expand boundary nodes as needed. |
| `creation_project_search` | Locate nodes by text, type, or scope. Keep search parameters unchanged when paging. |
| `creation_project_nodes` | Read up to 10 exact nodes, including details, members, revisions, default resources, candidates, drafts, and execution state. |
| `creation_document_search` | Search Document text for bounded excerpts, node IDs, line numbers, and content revisions. |
| `creation_project_document` | Read an exact Document node by line range; retain expected_content_revision when paging. |
| `creation_asset_resources` | Read Asset candidates, default selection, and visibility; pass as_of_seq as expected_graph_revision when paging. |
| `creation_resource_info` | Read one resource and its permitted media URL. |
| `creation_resource_status` | Independently refresh up to 100 explicitly observed media task IDs, regardless of run event cursors. |
| `creation_composition_get` | Read Composition settings, tracks, clips, and diagnostics. Follow next_offset with expected_node_revision until has_more=false; a partial view is not a full replacement payload. |
| `creation_sequence_move` | Reorder one Sequence member with the current container revision without changing Composition clip timing. |

## Materials, Runs, and User Decisions

| Tool | Behavior and constraints |
| --- | --- |
| `creation_upload_ticket` | Prepare direct upload using file name, byte size, and media metadata. For video, probe actual width, height, duration in seconds, and has_audio first. Transfer bytes using the returned transport; do not send the legacy scene field. |
| `creation_upload_complete` | Confirm upload after bytes have been transferred. Return an opaque, expiring file_ref for creation_run.files or creation_quick_generate.inputs[].file_ref. This neither transfers bytes nor automatically attaches a file to a project. |
| `creation_run` | Delegate creative planning, production, or revisions to Flova Agent within a selected project, using either content or parts, uploaded files, and the selected conversation. Bind a verified Skill using skill_id or skill_share_code as supported; preserve the binding on ordinary revisions. Reuse client_request_id for the same submission. Use supersede_pause_id only when replacing a pending question with a new request, not to bypass approval. Retain conversation and stream IDs. |
| `creation_run_status` | Read all available progress after from_message_id. Pass returned next_event_id on the next call, retaining project, conversation, and stream IDs. |
| `creation_run_result` | Read final events, resource states, recent messages, and pending actions at a terminal or paused state. |
| `creation_run_resume` | After an explicit user answer, pass the real action_id with option_id, free_text, or ordered answers using selected_values/free_text. Do not mix answer formats or pass legacy resume_message_id. Keep the original conversation_id; use creation_run for ordinary feedback. |
| `creation_interaction_submit` | Submit the user's explicit response to a server-issued interaction_id with a stable request ID. Never approve for the user. |
| `creation_run_cancel` | Request cancellation of the exact stream, then keep checking until terminal. Completed work and consumed credits are not undone. |

## Server-side Creative Skills

| Tool | Behavior and constraints |
| --- | --- |
| `creation_skill_categories` | List public Skill categories. |
| `creation_skill_feed` | Browse public Skills by category and page; do not treat this as keyword search. |
| `creation_skill_list` | List the user's created, saved, draft, used, or all Skills. Follow returned pagination when further lookup is needed. |
| `creation_skill_get` | Read an accessible online Skill, an owned draft, or a privately shared Skill. |
| `creation_skill_install` | Install an accessible Skill only on explicit user request. |
| `creation_skill_uninstall` | Disable an installed Skill for the caller when requested. It does not delete the Skill content or remove library membership; creation_skill_install can enable it again. |
| `creation_skill_document_get` | Read an owned Skill's editable Markdown and revision. |
| `creation_skill_reference_list` | List Reference summaries in an owned Skill draft. |
| `creation_skill_reference_get` | Read an owned draft Reference by node ID and content revision. |
| `creation_skill_reference_read_live` | Read a named online Reference from an accessible Skill, optionally pinned to a version. |

## Inspirations and External Agent Sessions

| Tool | Behavior and constraints |
| --- | --- |
| `creation_inspiration_categories` | List enabled categories for the requested locale. |
| `creation_inspiration_categor_items` | Find published cards by locale, Agent, category, name, or key. Follow next_cursor with unchanged filters; a name can match several cards. |
| `creation_inspiration_batch_get` | Retrieve full published instructions for up to 50 exact inspiration IDs. Reading instructions does not start or authorize generation. Read [Using inspirations](inspirations.md) before executing the selected workflow. |
| `creation_inspiration_config` | Read supported inspiration tools, Agents, and localized installation instructions. |
| `creation_recent_sessions` | List the user's recent external Agent chats, including quick and project work. Keep the Agent filter unchanged while paging. |
| `creation_session_delete` | Only on user request, remove the exact Agent/session pair from Flova recent sessions. This does not delete the external chat, project, messages, or media, or cancel tasks. |

## Export, Download, Restore, and Branch

| Tool | Behavior and constraints |
| --- | --- |
| `creation_export_readiness` | Select and check the target Composition before final-video export. |
| `creation_export_video` | Export the exact ready Composition with its expected node revision and a stable request ID. Preserve all values on retries of the same export. |
| `creation_export_status` | Query by task ID or recover by request ID. Omit both for the latest export; never pass both. |
| `creation_download_all` | Archive visible media and Documents with a stable request ID; this does not replace final-video export. |
| `creation_download_status` | Query by task ID or recover by request ID. Omit both for the latest archive; never pass both. |
| `creation_project_restore_preview` | Preview the impact of restoring a specified message and obtain a preview token without modifying the project. |
| `creation_project_restore` | After explicit confirmation, restore with the matching preview token, message, and mode. |
| `creation_project_branch` | Copy to a new project at a specified message, with selected/all conversation scope as requested. |
