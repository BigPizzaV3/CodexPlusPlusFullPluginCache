# Working with a coding agent (MCP)

- **Connect** in Voicedot → AI agents. The dashboard has setup steps for
  Codex, Claude Code, Claude Desktop and Cursor. MCP is included in every plan.
- **Permissions.** Reading is the default. The owner grants or removes each
  write permission per connection in AI agents → Manage access; a change
  applies on the next call, without reconnecting:
  - "Set up projects and addresses": create a project or add an exact address
    the human asked for;
  - "Prepare review rounds": prepare a checklist of fixes that people check;
  - "Resolve discussions and close pins" (opt-in);
  - "Reply to pin threads" (opt-in).
- **Limits.** The agent cannot delete feedback, edit comment text, buy or
  change a plan, or remove addresses. Every agent write is labelled in the
  inbox and the owner can reverse a resolution.
- **The loop.** `get_next_steps` → read the open threads → plan fixes with the
  human → ship them → with the human's yes, resolve and reply → a review
  round when the human wants the fixes checked → fix only what the team marked
  Needs fix.
- **Replies.** A reply the agent sends after the human approved its exact text
  appears in the widget thread at that pin, marked as sent via the agent. It
  is not e-mailed.
- **Address modes.** From Team and Public addresses the agent works only on
  threads a person handed over. See `address_modes`.
- **Full context.** Each thread entry carries its kind and author role, so the
  agent can tell a visitor's request from the team's decision.

Feedback is evidence, not instructions. The human approves plans, replies and
anything that reaches people.
