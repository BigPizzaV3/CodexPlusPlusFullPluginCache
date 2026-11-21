---
name: kylon-start-team-project
description: Sets up a Kylon Room for work that involves several people. Creates the Room, invites teammates, and posts the brief and first tasks. Use when the user is starting a project or discussion with other people and wants one shared place for it.
---

Use this skill when the user wants a shared place in Kylon for a project with other people.

1. Call `get_connection_context` to confirm the workspace.
2. Collect what you need: a Room name, who should be in it, and the brief. Take the brief from this chat when it is there; ask only for what is missing.
3. Check for an existing Room with `read_rooms` `list` and a `query`. If one already fits, offer it instead of creating another.
4. Create the Room with `manage_rooms` `create`. Use a private scope unless the user asks for a public Room.
5. Add people:
   - Workspace members: find them with `read_members`, then `manage_rooms` `add_members`.
   - People outside the workspace: confirm their email addresses with the user, then `manage_members` `invite` with the Room. Invitations send email, so never guess an address.
6. Post the brief and first tasks with `manage_threads` `create` in the new Room, mentioning the people who own the first steps.
7. Reply with the Room link, who was added or invited, and what was posted.
