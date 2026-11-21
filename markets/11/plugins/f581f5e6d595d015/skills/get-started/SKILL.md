---
name: get-started
description: First-run setup for Reachype in ChatGPT. Confirms the connected Reachype workspace, shows which projects (brands) it contains, and helps the user pick the project to work on.
---

# Get started with Reachype

Use this right after the user connects Reachype.

1. Look up the connected workspace overview. Tell the user, in their language, which workspace is
   connected, their role in it, and the projects it contains (by name).
2. If the workspace has more than one project, ask which one they want to work on, and use that
   project's id for the rest of the conversation. If it has exactly one, say which one will be used.
3. Tell the user what they granted at sign-in (read, edit, generate) only if they ask; do not list
   tools by name.
4. Offer two or three things they can ask next, chosen from what the workspace actually contains —
   for example the content calendar for the coming weeks, the brand voice, or recent performance.

Do not start any generation, edit anything, or quote credit figures as prices during setup.
If the overview returns an error, repeat its message to the user as it is: it says what to do.
