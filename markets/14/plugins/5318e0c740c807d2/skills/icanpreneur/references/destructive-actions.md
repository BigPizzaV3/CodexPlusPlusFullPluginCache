# Deleting, restoring and permissions

## Authorization and outcomes

Explain the requested action and its known consequences. Proceed within a specific delete/removal/revoke request already authorized by the user; ask only when the target or consequential scope is unclear. Do not delete extra resources, delete to repair something an update can fix, or delete research to run it again.

The implementation soft-deletes and recovers saved records. Restore tools require the original IDs; there is no deleted-items listing. If the ID is unavailable, ask for it. After an uncertain delete/restore, read saved state before taking another action. A missing record can also mean insufficient access; do not infer a successful deletion from a read failure alone.

| Resource/action                           | Known effect                                                                                                                                                                                   | Recovery tool                                           |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Workspace                                 | Member access to the workspace is removed. Dependent contents become inaccessible through it.                                                                                                  | `restore_idea` (Administrator; restore before children) |
| Canvas item, including a customer segment | Saved item is soft-deleted. A segment has linked research/contacts/Canvas items: explain that dependent work can be affected; do not promise a complete cascade or external-artifact deletion. | `restore_canvas_item`                                   |
| Research                                  | Saved research is soft-deleted. Interviews are independent records; do not delete them. BuyerPersona work is linked to its source research and may become inaccessible.                        | `restore_research`                                      |
| Interview                                 | Any stage can be deleted; related analysis/personas can refresh. Saved persona documents do not regenerate.                                                                                    | `restore_interview`                                     |
| Contact                                   | Contact record is soft-deleted; interviews are retained. Do not promise detachment or erasure of the saved interviewee name.                                                                   | `restore_contact`                                       |
| Reusable script                           | Deletion is rejected while active research or interviews use it.                                                                                                                               | `restore_interview_script`                              |
| Persona document                          | Saved document is soft-deleted. Do not promise that public preview URLs or Google Slides files are removed. Derived pages/decks are separate records.                                          | `restore_buyer_persona_document`                        |
| Note                                      | Saved note is soft-deleted.                                                                                                                                                                    | `restore_note`                                          |
| Member/invitation                         | Removes access or revokes an unaccepted invitation; actually sends emails when reinviting.                                                                                                     | No restore tool; invite again only when authorized.     |

No MCP tool deletes a Buyer Persona directly. No restore window, purge policy, or external-artifact recovery guarantee is exposed. Restore returns retained data; separately deleted children can require their own restore calls. Do not promise that every relationship or remote artifact is recovered. Restoring interviews can trigger billable analysis/persona work, so a restore is not guaranteed free of follow-on charges.

## Workspace permissions

Read operations generally require workspace membership. Content creation, editing, deletion, restoration, AI generation and persona questions require Editor or Administrator. Workspace detail updates, workspace deletion/restoration, invitation management and member-role/removal changes require Administrator. Inviting a Viewer/Editor is allowed for Editor or Administrator; invitations cannot grant Administrator. Promote an existing member only when requested.

Use `list_idea_members` to inspect `members[].user.userId` and `members[].role`. Idea summaries/details do not identify the caller's role; do not invent it or promise a per-tool permission field. Archived workspaces reject normal content writes. If an action is refused, report it and stop the dependent step; do not bypass authorization.

An Administrator cannot demote themselves. The account owner cannot leave; another Administrator may leave only when an Administrator remains. A Viewer/Editor can leave. These membership changes are distinct from license seats and the shared AI-credit pool.
