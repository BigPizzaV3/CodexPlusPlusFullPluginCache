# Collaboration and Sharing

## MCP

### Collaborator roles

| Capability | Co-owner | Editor | Viewer Uploader | Previewer Uploader | Viewer | Previewer | Uploader |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Upload | ✓ | ✓ | ✓ | ✓ | — | — | ✓ |
| Download | ✓ | ✓ | ✓ | — | ✓ | — | — |
| Preview | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Edit & rename | ✓ | ✓ | — | — | — | — | — |
| Delete & move | ✓ | ✓ | — | — | — | — | — |
| Invite collaborators | ✓ | ✓ | — | — | — | — | — |
| Advanced folder settings | ✓ | — | — | — | — | — | — |

**Plan note:** Editor and Viewer are available on all accounts. All other roles require Business/Enterprise and apply to folders only.

**Co-owner** cannot be set via MCP and must be set in browser.

### Access and sharing rules

Always prefer the narrowest role that satisfies the request.

When the user explicitly specifies the external audience and access level, proceed through the MCP tool controls. Ask only when the audience or access is ambiguous, or the action would widen exposure beyond the request.

Before overwriting a shared link, read its current settings. Ask only if the requested update does not resolve a consequential setting or would widen access beyond what the user authorized.

When creating open shared links, confirm with the user whether they want a password or expiration before creating. Treat folder shared links with extra caution since they expose everything inside, including content added after link creation.

### Shared links

If the user asks to update a shared link, you can call `add_file_shared_link` or `add_folder_shared_link` again — it's a PUT under the hood, is idempotent, and will overwrite the current shared link settings.

### File comments

When the user provides a file ID and explicitly asks to post comments already drafted in the conversation, treat the target and posting intent as resolved: post them without reconfirming the file ID or comment text. Ask only when the target is ambiguous or the drafts are unavailable. Create each comment once, retain the returned IDs, and verify them with `list_file_comments`; comments are visible to all file collaborators.

### Group collaborations

Resolve the `group_id` ahead of time (the tool takes an ID, not a group name).

`create_collaboration` with `collaborator_type: "group"`, `collaborator_id`, the appropriate `target_type`/`target_id`, and `role`.

Role changes via `update_collaboration` on a group apply to every member at once. Ask only when the requested scope or role is ambiguous.

### Open shared-link expiration

When creating open shared links, the `unshared_at` time has to be within 90 days. If the user wants to generate a permanent open shared link, direct them to do so in the browser and provide them with a link to Box for the object they were trying to modify.

## Codex-only CLI / REST

### Invite collaborators

- Primary docs:
  - https://developer.box.com/reference/post-collaborations/
- Use for team, vendor, or customer access to a shared workspace.
- Prefer folder collaboration when multiple files should inherit the same access.
- Choose the narrowest role that satisfies the request.
- Verify the acting identity is allowed to invite collaborators before coding the flow.
- Minimal smoke check:
  - Create the collaboration, then fetch or list collaborations to confirm the collaborator and role.

### Create or update a shared link

- Primary docs:
  - https://developer.box.com/reference/put-files-id/
  - https://developer.box.com/reference/put-folders-id/
- Use for external sharing, customer handoff, or quick verification outside the app.
- Add or update `shared_link` on the target file or folder, not on an unrelated object.
- Set access level, download permissions, and expiration intentionally.
- Confirm the user explicitly wants the audience widened before enabling or broadening sharing.
- Minimal smoke check:
  - Read the file or folder after the update and confirm the resulting `shared_link` fields.
