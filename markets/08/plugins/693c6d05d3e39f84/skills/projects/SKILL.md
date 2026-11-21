---
name: projects
description: Find or manage eHour clients, projects, tasks, and assignments. Use for project setup, project changes, and assigning people or teams to work in eHour.
---

# Manage eHour projects

Use the connected eHour MCP tools and their live schemas.
Project searches do not authorize changes.
Use returned IDs and disambiguation candidates rather than guessing which record the user means.
An assignment ID identifies a user or team assignment; it is not a project ID.

## Find and create work

Use `listClients`, `listProjects`, and `listTasks` for the requested records.
Results depend on the caller's role and may not cover the whole organization.
Use `listAssignments` to inspect assignment state; `getAssignments` is limited to the current user.
Use `runReport` for tracked hours rather than inferring activity from project or assignment settings.

`createProject` requires an existing client and a project name.
`createTask` requires an existing project.
Resolve the parent before creating the child; a missing parent is not permission to create one.
Use `createClient` only when the user has requested a new client.
The server can generate a code when it is omitted; preserve a code supplied by the user.

For project budgets, `budgetMinutes` represents minutes and `budgetCents` represents minor currency units.
Do not pass decimal hours as minutes or whole currency amounts as cents.
Confirm an ambiguous currency, amount, or enforcement setting before applying it.
Do not add rates or budgets merely because those fields are available.

## Update and assign

`updateClient`, `updateProject`, `updateTask`, and `updateAssignment` apply only the fields supplied.
Send the requested changes, without filling other fields with guessed defaults or empty values.
Resolve the target record before changing its name or code.

`assignToProject` and `assignToTask` accept exactly one user or one team.
Resolve the person or team with `listUsers` or `listTeams` when needed.
Keep assignment dates, rates, and budgets within the user's request.
An assignment's `role` is a work label, not a user access role.
Do not change account permissions to make an assignment succeed.

Team assignment synchronization can remove or archive existing assignments for former members.
Task creation can also trigger blueprint assignments and this cleanup.
Explain this effect when relevant to the requested operation; do not describe these operations as guaranteed to only add data.

Use `unassign` only for an explicit removal request, with the returned assignment ID.
Depending on tracked time, the server deletes or archives the assignment.
Do not move or delete time records as an automatic cleanup step.

## Verify the result

Report only the changes confirmed by tool results.
After an uncertain create or assignment response, inspect the current records before retrying to avoid duplicates.
If a request has several steps and a later one fails, report the completed steps and the failure.
Do not undo completed work unless the user requests it.
Respect scope and role denials; do not use another account or a direct API as a fallback.
