---
name: bilt
description: Build and edit mobile apps with the Bilt agent. Use when the user asks to create, change, check on, or review a Bilt project.
---

- Find projects with `bilt_list_projects` before acting on one by name.
- Send build or change requests with `bilt_send_message`. If the agent pauses with questions, relay them and send the user's answers back.
- Use `bilt_get_session` to check whether a build is queued, running or paused, and `bilt_get_messages` to summarise history.
- Only call `bilt_cancel_workflow` when the user explicitly asks to stop a build.
- Never pass API keys or other secrets through `bilt_send_message`; tell the user to add them in the project's secrets settings on app.bilt.me.
- Deleting projects isn't supported here; point the user to app.bilt.me.
- Always include the project link from the tool result.
