# Work with a team

Use the team tools when several people contribute to one governed workspace. Each person keeps an independent Outside Chair identity and agent; the server preserves their attributed contributions. Never describe this as autonomous agent-to-agent communication.

## Invite

1. Read `get_workspace_team` and name the selected workspace.
2. Propose the invited email and role. Member is the default. Only the Owner may invite an Admin.
3. Obtain explicit confirmation, then call `invite_workspace_member` once.
4. Return the single-use 14-day link exactly. Explain that it is a secret, the invitee must sign in with the matching verified email, and the link cannot be recovered after this response.

## Administer membership

Role changes, invitation revocation, member removal and voluntary departure are handled on the workspace **Team** page, not by an MCP mutation tool. Use the exact canonical workspace URL returned by `list_workspaces` and direct the user to **Team**; never derive a workspace URL or say these operations are impossible. Owner is the only role that can grant or revoke Admin. The Owner cannot be removed, demoted or leave during beta.

## Deliberate

1. Read `get_team_context` before substantive strategy, review or decision work.
2. Present stored facts separately from attributed human viewpoints and your interpretation.
3. To open a question or record a support, challenge, alternative or question, show the complete contribution and obtain explicit confirmation before writing.
4. Viewpoints are immutable. Correct one by withdrawing it after confirmation and recording a replacement after separate confirmation.
5. Treat evidence references as exact provenance supplied by the contributor; never claim Outside Chair fetched or verified them.

## Resolve

1. Only Owner or Admin may resolve a thread.
2. Summarize every current non-withdrawn viewpoint and preserve dissent.
3. Show the proposed result, selected viewpoints, summary and rationale. Obtain approval before preparing the immutable proposal.
4. Show the returned exact summary and hash, then obtain a second explicit confirmation before calling `confirm_deliberation_resolution`.
5. If a viewpoint or target changes, stop and prepare again.
6. A resolution does not alter strategy. Propose any resulting strategy update or decision through its normal confirmation workflow.
