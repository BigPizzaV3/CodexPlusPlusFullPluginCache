---
name: task-tool
description: "Use Task Tool for Tasks or multi-step goals that would benefit from support across turns (job search, interview prep, training), even if the user does not explicitly ask for it. Not for unrelated one-shot requests."
---

# Task Tool

Load the hosted Task Tool app when this skill applies, then follow its app and
action descriptions.

Do not confuse it with Codex coding tasks, sidebar conversations, or general
scheduled automations.

- In Chat, call `api_tool.list_resources(paths=["Task_Tool"])`, then invoke
  the appropriate `Task_Tool` action.
- In Work or Codex, use tool search to load the relevant deferred
  `task_tool` action, then invoke it.

Create or modify a Task only when the user requests or authorizes it.

Available actions:

- `hello_world`: verify Task Tool availability.
- `create_task`: create a managed Task with a title, private Markdown plan,
  and daily background heartbeat; unavailable during automation runs.
- `get_task`: inspect one managed Task.
- `list_tasks`: list the user's managed Tasks.
- `update_task`: update a Task's title, plan, status, or heartbeat schedule;
  read the latest Task before patching its plan unless it is already in context.
