---
name: brainstorm
description: Put ideas onto a Builderii board as sticky notes grouped by theme, such as the ideas from this conversation, a list the user gives, research findings, or a fresh brainstorm on a topic. Use when the user says "brainstorm", "put this on a board", "add these to Builderii", "make sticky notes" or similar.
---

# Brainstorm onto a Builderii board

1. **What goes up.** If the user gave ideas or a topic, use those. Otherwise take the ideas, options, risks and questions from the conversation so far, without the back-and-forth.
2. **Which board.** If the user named a board, find it with `search` or `list_boards`. Otherwise make one with `create_board` (kind `whiteboard`) and a specific name, such as "Onboarding ideas, Oct 29", never "Brainstorm".
3. **Group by theme.** Two to six themes, each a short title. Each note is one idea in a few words to one sentence. Aim for 3 to 10 notes a theme, and drop duplicates.
4. **Add** them in one `create_brainstorm` call: `groups`, each with its `title` and `notes` (each group gets its own colour).
5. **More later?** Add to the same brainstorm with `update_brainstorm` (`list_diagrams` gives its ref, `get_diagram` its group ids), or let Builderii's AI sort loose notes into themes with `cluster_stickies`, or grow one idea with `expand_ideas`.
6. **Confirm** in one or two lines: how many notes under which themes, with the board's link.
