---
name: kylon-team-second-brain
description: Saves decisions, how-tos and FAQs from this chat as Kylon knowledge pages or shared files, so the whole team and its AI agents can find them later. Use when the user wants to keep something for the team, not only for themselves.
---

Use this skill when the user wants to keep knowledge from this chat for their team in Kylon.

1. Call `get_connection_context` to confirm the workspace.
2. Choose the form:
   - Lasting team knowledge, such as a decision, process or FAQ: a knowledge page.
   - A document for one project or Room, such as a plan or report: a file in that Room.
3. Check for an existing page or file on the same topic with `read_knowledge` or `search`. Update it rather than create a duplicate.
4. Write it as a short, self-contained page: a clear title, the content, and the source (this chat, plus links to Kylon threads used).
5. Save it with `manage_knowledge` `add_entry` or `update_entry`, or with `manage_files` `write` for a Room file. Knowledge pages are visible across the workspace; say so before saving anything sensitive.
6. Reply with the link and where it was saved.
