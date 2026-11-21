---
name: creative-workflow
description: Build, edit, run, and review an AI image, video, or audio workflow in the user's connected YouArt workspace.
---

Use this skill when the user wants to create media with YouArt, continue an
existing YouArt project, or change and run a visual workflow.

Use only the bundled MCP dependency named `youart-plugin`. If it is unavailable
or unauthenticated, stop and ask the user to connect it. Never fall back to
another YouArt-looking MCP server, a global MCP entry, or any localhost URL.

1. Clarify only choices that materially affect the result, such as the intended
   project, source asset, output medium, aspect ratio, or whether paid generation
   should start now.
2. Use `list_projects` to find a project or `create_project` to start one.
3. Before project-specific edits, call `download_project_canvas`. Treat that
   snapshot and its `canvas_version` as the source of truth.
4. Before adding or editing a node class, read `schemas://index`, then the
   matching `schemas://node/<class_type>` resource. Follow its restrictions,
   writable parameters, handles, and `agent_notes`.
5. If the user supplied a ChatGPT file, identify the intended upload node and
   call `import_asset_to_upload_node`. If more than one node is plausible, ask
   the user to choose by display name and class label.
6. Chain each successful write's returned `canvas_version` into the next write.
   On `canvas_version_changed`, download the canvas again before retrying.
7. Before a paid run, check `list_active_workflow_runs`. If relevant nodes are
   still running, ask whether to wait or cancel. Never start overlapping runs
   without explicit consent.
8. Use a fresh `idempotency_key` for each intentional run and reuse it only for
   a network retry of that same launch. Never blind-retry a failed generation.
9. Wait with `get_workflow_run(wait_seconds=25)` instead of tight polling.
10. After completion, call `list_workflow_run_results` and give the user every
    generated asset URL plus a concise summary directly in the conversation.

Do not expose internal provider payloads, infrastructure details, signed
credentials, or one-time website sign-in links. The ordinary `editor_url` is
safe to share; the user may need to sign in on YouArt when opening it.
