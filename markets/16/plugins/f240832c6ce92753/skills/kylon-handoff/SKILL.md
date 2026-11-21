---
name: kylon-handoff
description: Writes a handoff from this chat and Kylon context (status, decisions, open questions, next owner) and posts it to the right Room or thread for a teammate or an AI agent to pick up. Use when the user is handing work to someone else.
---

Use this skill when the user hands work to a teammate or to an AI agent in Kylon.

1. Call `get_connection_context` to confirm the workspace.
2. Find the work's existing Room or thread with `search` or `read_messages` `search`, and read it with `read_threads` `get` so the handoff reflects what the team already knows.
3. Write the handoff with four short parts: where it stands, what was decided, what is still open, and who owns the next step and by when. Use only facts from this chat and from Kylon; mark anything unknown as open.
4. Confirm the receiver. For a person, find them with `read_members`. For an AI agent, check the Room's members with `read_rooms` `list_members`.
5. Post it with `manage_threads` `reply` in the existing thread, or `manage_threads` `create` in the Room, and mention the receiver. Mentioning an AI agent can start it working; tell the user when that will happen.
6. Reply with a link to the handoff and who received it.
