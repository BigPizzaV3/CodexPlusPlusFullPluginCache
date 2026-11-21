# Planner tool map

Use this map to choose a workflow. Follow the schemas and permissions currently advertised by the connected server. A deployment may expose fewer tools than the source inventory.

## Scheduling operations

| Task | Operations | Key inputs and behavior |
| --- | --- | --- |
| Open the workspace | `openPlanner` | `{}` opens the workspace without selecting a project. Optional `projectId` must be an accessible returned UUID. No view, route or token arguments are accepted. The UI uses a separately verified sign-in to the same Planner account as MCP. |
| Find a project | `listProjects`, `getProject` | Search with `search`; fetch using a returned `projectId`. |
| Read blocks | `listBlocks`, `getBlock` | `listBlocks` requires `projectId`; optional `startDate` and `endDate` filter overlapping ranges inclusively. `getBlock` takes `blockId`. |
| Create a block | `createBlock` | Requires `projectId`, `title`, `startDate`, `endDate`. Optional labels include `stage`, `episode`, `department`, `color`, `notes`, `location`. |
| Update a block | `updateBlock` | Requires `blockId`; change only requested fields. Read the block first. Do not treat the operation as a native ripple or notification sender. |
| Read schedule rules | `getProjectSettings`, `listNonWorkingDays`, `listProjectAxes` | Each uses `projectId`. Read rules and axis labels when they affect the task. |
| Change project settings | `updateProjectSettings` | Uses `projectId`; supported fields include working-week settings, deadline and display preferences. Only change settings the user requested. |
| Read crew records | `listCrewMembers`, `listCrewBlocks` | Both use `projectId`. Match member IDs from returned records. |
| Add a crew block | `createCrewBlock` | Requires project, title and dates, plus a resolvable crew member at runtime. Supply the resolved `crewMemberId`. |
| Update a crew block | `updateCrewBlock` | Requires `blockId`; use `crewMemberId` when changing the member. No fractional-allocation input is exposed in the source schema. |

Use dates in `YYYY-MM-DD` format. Tool input field names are camelCase; returned records may use snake_case. Do not send unsupported fields such as `dryRun`, `ripple`, `draftId` or `allocationFraction`.

The workspace can supply current-project context for requests such as “this project.” Confirm it with `getProject`; it is not a selected block or proof of permission. Read actual saved records after a manual UI edit. Keep private account-binding metadata out of conversation content and URLs.

## Related records

| Task | Available source operations |
| --- | --- |
| Project details | `createProject`, `updateProject`, `archiveProject`, `restoreProject` |
| Folders | `listFolders`, `getFolder`, `createFolder`, `updateFolder`, `moveFolder`, `moveProjectToFolder` |
| Folder access preview | `previewProjectMove` — previews access consequences of changing a project's folder, not schedule dates |
| Crew members | `createCrewMember`, `updateCrewMember` |
| Non-working days | `createNonWorkingDay` |
| Axes | `createAxis`, `updateAxisByPosition`, `updateAxis` |
| Block comments | `listBlockComments`, `createComment` |
| Project membership | `listMemberships`, `addMembership`, `updateMembershipRole` |
| Project invitations | `listInvites`, `createInvite` |
| Folder membership | `listFolderMemberships`, `addFolderMembership`, `updateFolderMembership` |
| Folder invitations | `listFolderInvites`, `createFolderInvite`, `resendFolderInvite` |

Use these operations only when the current connection exposes them and the user requests the corresponding action. Follow the live schema for required fields and side effects. Project invitations and folder invitations affect access; they are distinct from block calendar invitations.

Public spreadsheet fetchers may also be exposed. Use them only for a user-provided, publicly shared spreadsheet relevant to the requested Planner task. Do not treat them as access to the user's private Google or Microsoft account.

## Boundaries

The conversational tool inventory has no schedule dry run, ripple preview, atomic schedule proposal/commit, draft-version publication, or fractional crew-allocation input. The only preview operation concerns folder access. A manual feature in the full interface does not add a corresponding MCP operation. The default server mode excludes destructive and older UI-only action signals; the separately registered `openPlanner` launcher is available only when its UI deployment is enabled. Never assume that a tool exists or a write is permitted from this reference alone. Subscription checkout and contract changes are excluded from the embedded workspace.
