---
name: get-started
description: Set up Shape after installing it. Confirms the Shape sign-in works, lists the user's Shape projects, and agrees which project to focus on. Use when the user installs Shape or asks how to start using it.
---

# Get started with Shape

Shape gives read-only access to the user's construction projects in Shape. It
cannot create, change or delete anything.

1. Call `list_projects` to confirm the sign-in works and to see which projects
   the user can open.
   - If the call fails with an authentication error, ask the user to reconnect
     Shape and sign in with their Shape account.
   - If the list is empty, tell the user their Shape account has no projects
     yet and stop.
2. Show the projects as a short list: name, status and region. Mention that
   archived projects are included.
3. Ask which project they want to work on. If there is only one active
   project, propose it.
4. Suggest three things to try on that project, for example:
   - "What issues are still open, and which are critical?"
   - "Summarise the latest shift report."
   - "Which photos show the problem in the lobby?"

Keep the setup short. Don't read project data beyond `list_projects` until the
user picks a project.
