---
name: set-up-team
description: Use when an admin wants to invite teammates to Ciarem, create teams, or decide who receives the conversations the AI hands over to people.
---

# Set up the team

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can manage the team.

1. Call `get_team_setup` to see the members, the pending invitations and the teams.
2. **Invite people.** `invite_member` once per email. Ask the role when it isn't clear: an agent answers customers in the Inbox, a viewer looks things up and changes nothing. Admin invitations are sent from the Ciarem web app; when the tool says it can't send one from here, share the link it returns.
3. **Create teams** when conversations should reach different groups (sales, support): `create_team` with a name, a one-line `description` of what the team handles, and `member_ids` from `get_team_setup` (admins and agents; a viewer can't be on a team). A team with nobody on it receives nothing.
4. **Decide who gets a handed-over chat.** Call `get_ai_routing` to show the current rules, then `save_assignment_rule` with only what changes: `prioritize_owner` (the contact's owner first), `strategy` (round_robin or random), and what happens when nobody replies (`reassign_enabled`, `reassign_value` with `reassign_unit`, `reassign_max`). Omit `team_id` for the general rule; pass it for one team's own rule.
5. Sending certain conversations to a team is a transfer rule, not an assignment rule: `create_transfer_rule` (the `tune-ai-agent` skill).
6. Say what changed and which invitations are still pending.
