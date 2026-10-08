# Shared VideoGen ChatGPT rules

Follow these on every skill run.

1. Call `get_me` before spending credits if this chat has not already confirmed a linked VideoGen account.
2. Tell the user generation takes time before you start: images about 15–60 seconds; clips about 1–3 minutes; full workflows several minutes. Hosted calls may return a still-running snapshot within about 90 seconds. Keep polling `get_workflow_run`, `get_tool_execution`, or `get_project_export` until `succeeded`, `failed`, or `cancelled`.
3. Never invent `vg_proj_...`, `vg_file_...`, `vg_enti_...`, `vg_work_...`, or export ids. Use values returned by tools.
4. After a workflow succeeds, keep `projectId`. Optionally call `remix_project` with at least two of `CAPTIONS`, `TRANSITIONS`, `ANIMATE_IMAGES`, `ZOOM`. Then `export_project` and poll until `succeeded`. Share the `downloadUrl`.
5. If a tool fails because of credits or account access, tell the user to open https://app.videogen.io and manage their VideoGen account, then retry. Do not name pricing or plan-change flows.
6. Prefer `open_uploader` when the user needs to attach a file in ChatGPT.
7. Do not name internal model vendors. Describe VideoGen workflows, quality, and style.
8. For about one minute of narrated or informational video from text, prefer `script_to_video`. Use `storyboard_to_video` only for short shot lists, and never more than 3 scenes unless the user explicitly asks for more.
