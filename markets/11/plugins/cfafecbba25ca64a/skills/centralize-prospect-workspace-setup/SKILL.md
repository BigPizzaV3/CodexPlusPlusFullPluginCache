---
name: centralize-prospect-workspace-setup
description: 'Set up supported account maps, buyer personas, and account views in the connected Centralize workspace. Use for a requested prospect workspace setup after the intended workspace is established.'
---

# Set up the connected workspace

Read [workspace and write boundaries](../../references/workspace-safety.md) first.
This workflow adapts Hunter's prospect setup to the operations available through this plugin.
It cannot administer another workspace or complete browser-only settings.

## Establish the requested setup

Call `whoami` and compare the returned workspace with the user's intended workspace.
If they differ, stop before writes. Ask the user to connect the intended workspace.
Do not assume that the connector belongs to Centralize's internal sales workspace or to the prospect.

Ask only for missing account names and domains, target buyers, and requested saved account views.
Read existing accounts and account context before proposing additions.
Show the setup plan and its effects before confirmation. Account creation can activate accounts, consume capacity, and start background work.
Keep account activation, deep research, notifications, and workspace-wide defaults outside the plan unless specifically requested.

## Apply supported steps

1. For an approved new account, call `addAccounts` with the confirmed name and domain. Inspect results before dependent steps.
2. For buyer definitions, use [the persona workflow](../centralize-persona-functions-creation/SKILL.md). Reuse definitions before creation.
3. For each requested account map, use [the chart workflow](../centralize-org-chart/SKILL.md). Confirm proposed changes before writes.
4. For a requested saved accounts list, use `createAccountView` with filters supported by its current schema.

Each saved view must match the requested owner and sharing scope. Use a resolved owner rather than a viewer-relative filter for a named person's view.
Do not guess user identifiers. If the available tools cannot resolve a required owner or sharing setting, report that limitation before creation.
Do not activate an existing account merely because it is absent from a search result.

## Report remaining setup

The plugin does not support workspace switching, edits to existing functions or personas, default stakeholder filters, or account starring.
It also cannot create saved views for Home, Contacts, Connections, Opportunities, or Job Changes through `createAccountView`.
Do not replace these missing operations with browser automation or another connector.
Give the user a concise list of remaining settings to complete in Centralize.

Read back accounts and charts with the available read tools. Use a returned view link to report successful view creation.
Do not claim an unverified default, sharing setting, or saved view is complete.
Report completed steps, failed steps, user-approved inferences, and remaining setup separately.
