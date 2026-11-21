---
name: get-started
description: Set up Scripe after installing the plugin. Check the connection, pick the workspace and profile to work on, and suggest a first task.
---

Help the user start working with Scripe, their LinkedIn content system.

1. Call `workspace_read` with `action: "get_workspace_context"`. It returns the
   active Scripe workspace, its plan and the profiles in it (personal profiles
   and company pages), each with whether LinkedIn is connected.
2. Tell the user, in one or two sentences, which workspace is active and which
   profiles it holds. If `workspace_read` with `action: "list_workspaces"`
   shows more than one workspace, ask which one to use and switch with
   `workspace_write` and `action: "switch_workspace"`.
3. If a profile shows LinkedIn as not connected, say that Scripe can still
   plan and write for it, and that publishing and analytics need the
   connection, which the user makes in the Scripe dashboard at
   https://scripe.io.
4. Offer three first tasks and let the user choose:
   - plan the next period's posts for their profiles (start with
     `get_planning_overview`),
   - write a post in their own voice about something they name
     (`posts_write`, `action: "generate_post"`),
   - see how their posts performed lately (`analytics_read`,
     `action: "get_analytics_overview"`).

Never publish, schedule, delete or send anything during setup. Those actions
always need the user's explicit yes.
