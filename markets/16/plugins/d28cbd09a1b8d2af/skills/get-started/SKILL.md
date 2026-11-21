---
name: get-started
description: Give a first look at the user's Benetics construction projects. Use it when the user sets up Benetics, asks what Benetics can do here, or wants an overview of a project's open and overdue tasks.
---

Use this skill to show the user their jobsite data and explain how changes
work. It only reads: don't call `create_project`, `update_project`, or a
`propose_*` tool unless the user asks for a change.

1. Call `list_projects` and show the projects by name. If there are none, say
   that the account has no projects yet, offer to create one, and stop.
2. If there is one project, use it. Otherwise ask which project the user
   wants to look at; don't pick one for them.
3. Call `get_project` for that project.
4. Call `list_tasks` for it twice, both with `state` set to `open`: once as
   is, and once with `due_before` set to the end of yesterday, to find the
   overdue tasks.
   `total_count` is how many tasks match in all: use it for the counts, and
   don't fetch further pages unless the user asks for more.
5. Summarize in a few lines: the project's name and address, how many tasks
   are open and how many are overdue, and up to five overdue tasks with their
   title, assignees, due date, and link.
6. Explain what the user can do next:
   - ask about tasks, plans, documents, and photos;
   - ask for changes, such as a new task or a new due date. These are saved
     as drafts that only they see, and nothing changes for their team until
     they review and publish the drafts in the Benetics app;
   - create a project, or rename, re-address, archive, or restore one. These
     changes are not drafts: they take effect right away, for everyone on the
     project.
7. Offer one next step that fits what you found, such as listing the overdue
   tasks of one person.

Report only what the tools return. Don't invent tasks, people, or dates, and
if a tool returns an error, say so rather than guessing.
