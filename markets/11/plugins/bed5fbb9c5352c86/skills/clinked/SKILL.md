---
name: clinked
description: Manage Clinked groups, members, files, folders, notes, tasks, and events through its MCP tools. Use it for user-facing workspace work, especially when resolving names, reporting results, or changing file and folder sharing.
---

Use names in the conversation. The tools may need IDs, but users normally do not.

## IDs and actions

- Resolve a group, member, file, folder, note, task, or event by name before using its ID. If several results match, show the useful difference, such as path or date, and ask one short question.
- Do not show IDs in normal lists, confirmations, or success messages. Show them only when the user asks, during technical troubleshooting, or when identical results cannot otherwise be distinguished.
- Keep actions distinct. Creating, renaming, moving, replacing content, restoring, deleting, inviting people, and changing sharing are different operations.
- Ask only when the target or effect is unclear. Do not assume public access, extra recipients, child-item changes, overwriting, or permanent deletion.

## Sharing, invitations, and attendance

For content sharing:

- `MEMBERS`: share the item with every group member. The group permission controls whether they can view, edit, delete, or administer it.
- `NONE`: do not share the item with the whole group. Only the owner, group admins, and people with individual access can use it.
- `DEFAULT`: an internal state for drafts or existing content. Do not choose it for a normal request.

The MCP tools cannot create or change individual access. File and folder sharing changes preserve it.

Choose the lowest access level that meets the request. Do not show the internal numeric codes:

- `READ`: view.
- `WRITE`: view, download, and share externally where available. It does not allow editing.
- `CREATE`: view and edit, including uploading a new file version where available. The name is legacy.
- `DELETE`: view, edit, and delete.
- `ADMIN`: manage the item, including permissions.

Use the same sharing choices for notes, tasks, and events. New folders, notes, tasks, events, and URL uploads default to `MEMBERS`. A URL upload into a folder inherits that folder’s sharing and access level when neither is supplied. A draft note uses `DEFAULT`.

`updateGroupFileSharing` changes sharing on a file or folder. It does not email anyone, create a guest link, or make an item public. For a folder, ask whether the same change should apply to its contents when the user has not said. State that choice in the result.

Inviting people is separate: `inviteGroupMembers` emails invitations and grants the selected access level. Assigning a task or adding event attendees does not invite someone to the group. `assignAll` affects every group member.

Uploading from a URL can replace or version a matching file because update mode is on by default. Resolve the target folder and ask when a matching file makes the intended result unclear.

Report the useful outcome first, for example: “Updated sharing for `Budget` in `Q4 planning`; files inside the folder were unchanged.” State only what the tool response establishes.
