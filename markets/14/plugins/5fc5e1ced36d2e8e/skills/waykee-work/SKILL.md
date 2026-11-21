---
name: waykee-work
description: Work with the user's own Waykee account through the Waykee MCP tools - find and update tasks, read and reply to task conversations, and search project documentation. Use when the user asks about their Waykee tasks, bugs, projects, conversations or docs.
---

# Working with Waykee

Waykee is a work-management platform where every task, bug, project and document is also a conversation. Documentation is organized as System > Module > Screen, and tasks hang under those items. The Waykee tools only return and change data the signed-in user can already access.

## Find work

- Use `SearchTasks` to find tasks by text, status, assignee or due date. Exclude completed tasks when the user asks what is pending or overdue.
- Use `GetStatuses` or `GetWaykeeTypes` when you need the id of a status or task type.
- Use `GetDashboard` for a quick overview of the user's workload and `GetPendingQuestions` for questions waiting on the user.

## Get context

- Resolve the task first with `SearchTasks`, then call `GetTaskDetails` for status, dates, people and latest messages.
- Use `GetMessages` to read the full conversation of a task or project, and `GetConversations` to list recent conversations.
- Use `GetRelations` to see the parent and child items of a task, project or document.

## Search knowledge

- Use `RagSearch` for natural-language questions across projects, tasks and documentation.
- Use `SearchDocumentation` when the user names a document, then `GetDocumentation` to read it.
- Quote the source item (its subject) when you answer from documentation.

## Make changes

- `CreateTask`, `UpdateTask`, `SendMessage`, `CreateDocumentation` and `UpdateDocumentation` change the user's workspace. Before calling them, restate what will change (item, field, new value or message text) and get the user's confirmation.
- Resolve the target item with a search first; never guess ids.
- After a change, report the result with the item's subject and id.

## Limits

- There is no tool to delete items, list other users of the platform, or read credentials, API keys or passwords. Decline those requests and offer what the tools can do instead.
- Do not call Waykee tools for general questions that are not about the user's Waykee data.
