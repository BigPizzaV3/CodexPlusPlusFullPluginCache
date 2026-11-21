---
name: altodocs-workspace
description: Organise AltoDocs projects, folders and native files from chat. Use for discovering destinations, creating or copying projects, renaming or moving files, making copies, and recoverable Trash or restore operations.
---

# Projects, folders and files

Use available AltoDocs tools to carry out the user's requested organisation
change. Keep the requested file type and preserve content/history. Do not turn a
simple file operation into new content creation or expand access to work around
a denial. Tool availability depends on the host and grant.

## Discovery and project creation

Use `list_projects` and `list_documents` for consented projects/files; follow
`nextCursor` pagination. Use `get_project` for a project's saved identity/state
and `get_document_info` for a file's type, folder, content and properties versions.
Ask if a name resolves to multiple plausible targets. Never guess an ID.

Use `list_workspaces` to choose `organizationId` for `create_project` when the
user requests a project. Require an identified/unambiguous organisation, new
project/request UUIDs and a meaningful name. The tool needs `projects:create`
consent and native organisation editing access. It adds only the newly created
project to this connection; it does not grant access to existing projects.
`duplicate_project` copies a selected project's live files/history/media with
creator-only sharing, not its old memberships. Keep a clearly requested copy
distinct from the original. Verify the resulting project with `get_project`.

An older grant may lack project-creation permission. Use the host's native
reconnection/consent flow when needed; token refresh cannot broaden permissions.
Never request a password/token in chat or silently grant another project.

## Versioned folder/project changes

For `rename_project`, `create_folder`, `rename_folder` and `remove_empty_folder`,
read `get_project` immediately before the write and pass its exact `state` as
`expectedState`. Use relative slash-separated folder paths without empty, dot
or parent segments. Folder creation includes parents. A subtree rename must
preserve descendant file locations; do not recreate files as a workaround.
Removing an empty folder must fail if it contains files, including Trash.

Read back the project/folder state. Do not claim a folder operation moved,
deleted or copied document contents when it did not.

## File lifecycle

Before each `rename_document`, `duplicate_document`, `move_document`,
`trash_document` or `restore_document`, read `get_document_info` and supply both
`expectedVersion` and `expectedPropertiesVersion`. For a trashed file use
`includeTrashed: true`; `list_trash` discovers recoverable files.

Renaming and moving retain the file's ID/content/history. Duplication needs a
new copy UUID and produces a distinct file; its destination project must be
accessible. Do not copy sharing or membership. Trash is recoverable, not a
permanent deletion. Restore retains content and folder. There is no permanent
delete, project deletion, membership, billing or sharing administration tool.
Respect the user's authorised operation; do not clean up additional files.

On a lost response reuse the exact request UUID and payload. On a version/state
conflict re-read and reconsider rather than replaying against a newer version.
Honour Retry-After when rate-limited; preserve the pending request and avoid
creating duplicate files/projects as a workaround.
Verify the returned metadata and read the affected content through its native
reader when content preservation matters. Return the actual saved URL, including
the correct native route for MathCanvas, reports, spreadsheets or CAD.

Create content through the relevant standalone MathCanvas, engineering report,
spreadsheet, markup or CAD skill. This workflow organises existing native files;
it does not import arbitrary host attachments into storage.
