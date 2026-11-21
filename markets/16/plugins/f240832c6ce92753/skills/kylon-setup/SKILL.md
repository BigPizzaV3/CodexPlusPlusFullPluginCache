---
name: kylon-setup
description: Gets a new Kylon user started after installing the plugin. Confirms the connected workspace and walks them through a first task, such as sharing a result from this chat with a teammate or catching up on their team.
---

Use this skill right after the user installs Kylon, or when they ask how to start.

1. Call `get_connection_context` and tell the user which workspace and account are connected.
2. Show what is there with `read_rooms` `list`. If the workspace has no Rooms or no other members yet, say so plainly.
3. Offer one first task that fits what you found, in one sentence each:
   - Share something from this chat with a teammate (kylon-share-with-team).
   - Start a Room for a project and invite people (kylon-start-team-project).
   - Catch up on what the team did this week (kylon-team-catch-up).
4. Run the task the user picks with that skill. Do not post, invite or create anything before the user chooses.
