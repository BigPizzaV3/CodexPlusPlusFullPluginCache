---
name: vaiz-workspace
description: Manage the Vaiz session and people context — introduce Vaiz with get_started, check connection and current user, list and switch spaces, show or query members, invite people and change roles, look up activity, review and mark notifications, and log or query time-tracking entries.
---

# Vaiz workspace, members, and activity

Use this skill to establish who you are, which space you are working in, who else is on the team, and what has been happening.

## Prerequisite

The Vaiz MCP server (`https://api.vaiz.com/mcp`) must be available through the installed Vaiz plugin and authorized with OAuth. If tools are missing or return an authorization error, open the Vaiz connection and complete OAuth sign-in. This skill does not replace that step.

Vaiz tools can appear under different names depending on how Vaiz is connected: `mcp__Vaiz__query_tasks` for a directly configured MCP server, or `mcp__codex_apps__vaiz_query_tasks` (sometimes with a longer app prefix such as `vaiz_testing_`) when Vaiz is installed as an app. Match tool names case-insensitively and by the tool suffix (`query_tasks`, `show_tasks`, …), not by an exact `Vaiz` prefix. Tools may also be loaded lazily: a Vaiz tool that is not in the current tool list is not missing — load it through tool search (for example `Vaiz query_tasks`) before concluding it is unavailable. Work with Vaiz only through these tools: do not open app.vaiz.com in a browser or drive the Vaiz desktop app with Computer Use, even if the user's `@Vaiz` mention also resolves to that app.

## Getting started

- The user's message is just "Vaiz", or they ask how to get started or what they can do → call `get_started` first and show its answer. If the intro card was rendered as a widget, reply with one short sentence instead of repeating it.
- A tool result starts with `[vaiz_onboarding] status=not_started` → do exactly what that line says (either call `get_started` now, or answer first and then offer the introduction in one sentence).
- The user declines the introduction → `get_started` with `dismiss: true`. Call it at most once per conversation.
- `variant: "no_space"` → call `list_spaces`, let the user pick, `select_space`, then `get_started` again.
- Import from Jira, Trello, Asana, Notion, or CSV is not available over MCP; give the user the `importUrl` from the `get_started` result.

When the user describes a project to set up, follow the structure flow in `vaiz-projects-milestones` (`setup_space`).

## Connection and identity

- `ping_server` — health check; use it first when something looks broken.
- `get_current_user` — the authenticated user and the current space context. Returns your member id, which `query_tasks(assignees: [...])` and other filters need.
- `get_space_info` — details of the selected space and your permissions in it.

## Spaces

A user may belong to several spaces (workspaces). The MCP session has one selected space at a time.

- `list_spaces` — all spaces available to you, with ids.
- `select_space(spaceId)` — switch the session to another space.

Most tools also accept an optional `spaceId` argument that overrides the session space for that single call. Pass it when the user is clearly working across spaces or when you cannot rely on session state.

When a space is read-only (trial ended without a subscription), every write fails with "This space is read-only…". Do not retry or look for another tool; tell the user a space owner can upgrade the plan.

## Members

- `show_members` — the user wants to see the team; renders a widget and the rows are not returned to you. Do not repeat rows the user already sees.
- `query_members` — you need the rows: resolve a name to a member id, count, or prepare another call.
- `get_member(memberId)` — one member in detail.
- `search_space(entityType: "user", query)` — find a member by name.
- `get_user_history(memberId)` — that member's activity across the workspace. Narrow with `dateRangeStart` / `dateRangeEnd`, `projectIds`, `boardIds`, `taskIds`, `entityTypes`, or event `keys`; paginate with `limit` and `page.nextCursor`.

Member ids are what `assignees`, `createdBy`, `set_followers`, and mention syntax (`@[Name](user:id)`) expect. Members with `isAgent: true` are AI agents, not people — see `vaiz-agents`.

## Managing people

These change who can see the space; confirm the people and the role with the user before calling them. All need Manager rights on the space.

- `invite_members` — sends an invitation email to each address right away. Use only addresses the user gave you; the default role is `member` (`guest` and `manager` only on request). If the user wants to invite people but named nobody, call it without `emails` to get a link to the invite dialog. Report each outcome: invited, already in the space, no free seats, or failed.
- `set_member_role` — change a member's role to `guest`, `member`, `manager`, or `owner`. You cannot change your own role or the space creator's, or grant a role higher than your own.
- `set_member_deactivated` — deactivate (`true`) or reactivate (`false`) a member. Deactivation removes access and frees a seat; their work stays. Reactivation fails when there are no free seats.

## Notifications

- `get_notifications` returns your notifications with `readStatus` (`"All"`, `"Read"`, `"Unread"`), `groups`, `pinned`, and `limit`. Paginate with `lastLoadedDate` (Unix ms of the newest loaded notification). Use it to answer "what needs my attention" questions.
- `mark_notifications_read` — mark `notificationIds` as read (`read: true`, default) or unread (`read: false`), or pass `all: true` to mark everything read. Do it only when the user asks.

## Time tracking

- `get_time_entries` returns completed time-tracking entries with task, member, and project data plus exact totals. Filters: `dateFrom` / `dateTo`, `projectIds`, `taskIds` (ids or HRIDs), `memberIds`, `billable` (`"all"`, `"billable"`, `"non_billable"`), `isManual`, `statuses`. Sort with `sortBy` (`"startTime"`, `"duration"`) and `sortOrder`; aggregate with `groupBy` (`"member"`, `"task"`, `"project"`). Available to space owners and managers only — if the call is denied, say so rather than retrying.
- `create_time_entry` — log time on a task for yourself: `durationMinutes` (optionally with `workDate`) or `startTime` + `endTime`, plus optional `comment` and `hourlyRate`. Time cannot be logged on behalf of another member.
- `edit_time_entry` — change the hourly rate of your own running or paused timer. A completed entry cannot be edited: delete it and log it again.
- `delete_time_entry` — permanently delete one of your own entries; confirm first.

## Good habits

- Resolve the space and your member id once at the start of a session.
- Do not paste other members' personal data into Space Memory or documents beyond what the task needs.
- Use `get_user_history` and `get_project_history` (see `vaiz-projects-milestones`) for summaries instead of scanning tasks one by one.

Further reading: https://vaiz.com/help/tutorials/how-to-connect-vaiz-to-mcp · https://vaiz.com
