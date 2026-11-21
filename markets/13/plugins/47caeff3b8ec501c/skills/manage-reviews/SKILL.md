---
name: manage-reviews
description: Manage BugSmash visual review workflows through the hosted BugSmash MCP tools. Use when a user asks to create or find projects, manage versions or folders, read or summarize feedback, update comments, manage replies, or manage webhooks.
---

# Manage BugSmash Reviews

Use the BugSmash MCP tools for live data and actions. Do not call the REST API when an MCP tool covers the request. If the MCP server needs authentication, ask the user to connect their BugSmash account through the browser OAuth flow.

## Workflow

1. Call `list_workspaces` before workspace-specific work.
2. Resolve names to IDs with list or detail tools.
3. Read current state before a write when the target is not exact.
4. Use the smallest write that completes the request.
5. Return the relevant project, version, folder, comment, reply, or webhook ID and any review link.

For feedback summaries, request plain text and location metadata. Show active comments before resolved comments. Preserve comment numbers and IDs so the user can act on the result.

When `list_comments` returns a non-null `meta.nextCursor`, call it again with the same arguments and `cursor` set to that value. Continue until `meta.nextCursor` is null before you summarize or report that no comments remain.

For a local file or chat attachment, call `prepare_file_upload` with the correct purpose. Upload the file to the returned short-lived URL, then pass its `uploadId` to `create_project`, `create_version`, or `update_comment`. A supported public file URL can be passed directly instead. Never display the private upload URL.

## Safety

- Do not ask for or display a BugSmash API key. The MCP server uses OAuth.
- Before a delete, state the exact target. Ask for confirmation unless the user already gave a clear delete instruction for that target. Pass `confirmDeletion: true` only after confirmation.
- Treat project, version, comment, reply, folder, and webhook deletes as destructive.
- Before deleting a folder, state that its nested folders and all projects in the folder subtree will also be permanently deleted. The confirmation must cover the full subtree.
- Tell the user when a write creates or changes a public review link.
- Never display an OAuth token or webhook signing secret.
- Do not retry a write automatically after a timeout. Read current state first to prevent a duplicate write.

## Errors

- `401`: Ask the user to reconnect BugSmash through the browser OAuth flow.
- `403`: Explain that the workspace role, plan, usage limit, or OAuth scope does not permit the action. Guests and collaborators cannot access a workspace through MCP.
- `404`: Verify the ID and confirm that the user connected the correct workspace.
- `422`: Correct the input from the response message. Do not change field names without evidence.
- `429`: Report the limit. Do not retry until the limit resets or the account changes.
- `5xx`: Report a BugSmash service error. Do not claim that the write failed if the result is uncertain.
