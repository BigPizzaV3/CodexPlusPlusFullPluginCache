---
name: get-started
description: Help a new user get started with Flying Donut in ChatGPT or Codex and run their first useful request about projects, sprints and backlog.
---

# Get started with Flying Donut

Use this when the user has just connected Flying Donut or asks what it can do.
Use the plugin's connected MCP tools in either ChatGPT or Codex; no local API token is needed.
If the tools require authentication, ask the user to connect Flying Donut through the host's
connection flow, then resume. Never ask for a password or token in chat or store one in a repository.

1. Call `flying_donut_list_projects` and show the projects the connection can see.
   - If none are listed, explain that projects are chosen on the Flying Donut consent screen.
     The user can reconnect the app and select projects, or ask a project admin for access.
2. Ask which project to work in, unless only one is listed.
3. Offer two or three starting points that fit that project, for example:
   - "Summarize what's still open in the current sprint and who's working on it."
   - "Turn these meeting notes into backlog cards."
   - "Which cards are blocked, and why?"
4. Refer to cards and tasks by their number (for example `WEB-12`), and look them up with
   `flying_donut_get_card_by_cid` or `flying_donut_get_task_by_cid`.

In Codex, when the user wants to implement a card, read its description and tasks first.
Use the repository's instructions and acceptance criteria to guide the code changes and tests.
Only update the card's state, assignees, time or comments when the user authorizes those changes;
finishing a code edit alone does not authorize moving the card to Done.

Guidelines:

- Read before you write: look up the project, sprint, bucket, lane or member before changing anything.
- Before creating, changing or deleting work, say what you are about to do and get the user's OK.
- Deleting needs the "delete work" permission. If a tool is refused for lack of permission,
  say which permission is missing; the user can grant it by reconnecting the app.
- Flying Donut cannot delete projects or manage billing through this app; point the user
  to the Flying Donut web app (https://www.flyingdonut.io) for those.
