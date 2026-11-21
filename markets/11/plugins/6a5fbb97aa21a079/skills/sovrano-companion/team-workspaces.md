# Teams and workspaces

## Selection

One active workspace may be selected automatically by the server. With several workspaces, use `list_workspaces` with the user's exact company or client wording and present bounded candidates when needed, then call `get_sovrano_profile` with the chosen `workspace_id`. Sovrano remembers that explicit choice for later chats. Similar names, partial matches and recency never authorize selection.

Carry the selected `workspace_id` through every situation, research, context and decision call. A readable human name is for conversation; the server-issued identifier is the authority boundary.

## Creating a workspace

Before `create_workspace`, establish:

- workspace name;
- kind: brand, property, agency or other;
- the creator's member type; and
- explicit approval to create the shared record.

Use a fresh idempotency key and `confirmed: true` only after that approval. The creator becomes owner with a decision right. Workspace creation is not situation creation.

## Roles and decision rights

Roles and decision rights come from `get_sovrano_profile` or `get_workspace_team`.

- Owners govern the workspace and hold decision rights.
- Admins administer and hold decision rights.
- Members contribute; their decision right is explicit rather than inferred.
- Viewers read and cannot write or decide.

An agent can draft and explain but does not gain authority from the host, conversation or another member. Expired or removed access stops on the next server check.

## Invited users

For pending access, direct the person to the secure invitation flow. Possession of a link alone reveals nothing. After acceptance, summarize only workspace purpose, role, member type, decision right, visible data categories and the most useful active or assigned work. Avoid replaying a general product introduction.

The onboarding receipt records that the versioned briefing was shown. Before the first contribution, state allowed reversible work and prohibited confirmation, finalization and external action together. A writable contributor without decision rights may add evidence, comments and drafts and move outputs to `in_review`, but cannot confirm a Frame or decision or mark an output `final_internal`. Sovrano never sends, publishes, signs, pays or contacts a counterparty. Acknowledgement is a separate web action; chat text does not manufacture that receipt.

## Collaboration and stale work

Read current situation version before a save. If another member changed the record, preserve the rejected contribution through the server recovery path when available. Reload, explain the changed sections, then choose one closed merge mode with the user. Never use force, last-write-wins or a reconstructed version number.

Comments, assignments and activity support coordination but do not confirm a phase, approve a decision or replace authoritative situation sections.
