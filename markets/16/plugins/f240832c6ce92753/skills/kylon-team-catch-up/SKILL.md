---
name: kylon-team-catch-up
description: Summarizes what a team discussed, decided and left open across Kylon Rooms and threads, with links to the source. Use when the user asks what they missed, what the team decided, or for a weekly team update.
---

Use this skill when the user wants to catch up on team activity in Kylon.

1. Call `get_connection_context` to confirm the workspace.
2. Set the scope: the Rooms or topic the user named, and the time window. Default to the last 7 days when no window is given.
3. Gather activity with `read_messages` `recent` or `search` (with `room`, `since` and `until`), and open the threads that matter with `read_threads` `get`. Use `read_feed` `list` for what needs the user's own attention.
4. Write the summary in three parts: decisions, open questions and blockers, and items that need the user. Link every item to its thread or message.
5. Do not state a decision unless the source shows it was made. Say when a Room had no activity in the window.
6. If the user asks to share the summary, use the kylon-share-with-team skill.
