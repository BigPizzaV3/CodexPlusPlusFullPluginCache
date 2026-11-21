---
name: get-started
description: Help a connected Rowzz user find the right workspace and dashboard, then use the real MCP tools without inventing capabilities.
---

# Get started with Rowzz

Use this skill after the user connects Rowzz. Work only with the connected account and the workspaces that account granted. Do not invent tools, dashboards, rows, or access.

## First step

1. Call `list_workspaces` to see the granted workspaces (id, name, role, can_write).
2. If there is more than one workspace, ask which one to use. Do not pick silently.
3. For dashboard work, call `list_dashboards` with that `workspace_id`, then ask which dashboard when several exist.
4. Call `list_columns` before reading or writing rows so field keys match.

Forms are different: `create_form` does not require a workspace. For a form-only request, skip `list_workspaces` and omit `workspace_id` unless the user explicitly wants the form in a workspace.

## What this plugin can do

Read tools: `list_workspaces`, `list_dashboards`, `list_columns`, `list_records`, `get_record`, `list_forms`, `get_form`, `list_automations`, `get_automation`.

Write tools (owner, admin, or editor on the workspace, except personal forms): `create_workspace`, `update_workspace`, `create_dashboard`, `update_dashboard`, `create_column`, `update_column`, `create_record`, `create_records`, `update_record`, `update_records`, `reorder_columns`, `reorder_records`, `create_form`, `update_form`, `create_automation`, `update_automation`, `set_automation_active`, `delete_automation`, `delete_dashboard`.

## Limits

- Guests invited from Share never appear in `list_workspaces` and cannot use this connector.
- Formula and linked columns are read-only.
- `delete_dashboard` permanently deletes one dashboard by `dashboard_id`. Use it only when the user explicitly asks to delete that dashboard. Never delete by name, pattern, or several ids.
- This plugin does not process payments, sell subscriptions, draw charts, or change billing.
- Native automations can be listed and configured. Creating or updating a rule does not run it immediately.
- If the user is vague about the workspace, dashboard, or row, ask a clarifying question before writing.

## After a successful write

Confirm briefly that the change is in Rowzz. When `create_dashboard` returns a url, present it as "Open your dashboard in Rowzz".
