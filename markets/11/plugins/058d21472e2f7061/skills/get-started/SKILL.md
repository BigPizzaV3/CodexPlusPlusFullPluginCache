---
name: get-started
description: Run once after the primaTime plugin is installed, or when the user asks how to start, to verify the connection, confirm the organization and show what they can do.
---

Use this skill when the user runs setup for primaTime or asks how to get
started with it. Read-only: do not create, change or delete anything.

1. Call `whoami`. If it fails with an authentication error, tell the user to
   connect the plugin and sign in with their primaTime account, then stop.
2. Tell the user who they are signed in as (name, email), which organization
   is connected (`organizationTitle`) and which timezone primaTime uses for
   dates (`organizationTimezone`). If `recentProjects` is non-empty, mention
   up to three by title and code. Link to the app with the returned `links`;
   never invent a URL.
3. If `access` is `VIEW_ONLY`, say that this account can read data but not
   change it, and that an organization admin can grant full access.
4. If the user expected a different organization, explain that the
   organization is chosen on the sign-in screen: they must disconnect and
   reconnect the plugin to switch. There is no tool that switches it.
5. Offer three things to try, in the user's own terms:
   - "Show my TODO list and the time I tracked this week"
     (`my_todo_list`, `time_summary`)
   - "Start a timer on <task>" (`start_timer`)
   - "Time report for last week by project" (`time_report_by`)

Facts not to infer:

- Never guess project, task, client or user ids. Resolve names with
  `resolve_project`, `resolve_task`, `resolve_client` or `resolve_user`; if
  several match, ask the user which one.
- Do not assume whether the organization requires a time-tracking tag on every
  record. Before logging time, list valid tags with `list_time_tracking_tags`
  for the chosen project.
- Dates and times without an offset are interpreted in the organization
  timezone, not the user's device timezone.
