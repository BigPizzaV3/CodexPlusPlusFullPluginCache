---
name: get-started
description: First steps with APIgency Hourly Earnings — check the user's projects, see what is running, and start tracking client work.
---

# Getting started

Use this when the user connects the plugin for the first time or asks how to begin.

1. Call `list_projects` to see the user's client projects, their hourly rates and currencies.
2. If there are no projects, offer to create one with `create_project`. Ask for the project name, the hourly rate and the currency; do not guess them.
3. Call `current_work` to show anything that is already running or paused, so the user does not start a duplicate.
4. To begin tracking, use `start_task` with the project and a short task name the user gives.

Things to tell the user once:

- Timers run on the server. Closing the chat does not stop them; a task stops only when it is paused or finished.
- Finishing a task records the work permanently. Confirm with the user before calling `finish_task`.
- Time can only be reduced with `trim_task_time` on a paused, unfinished task. It can never be added.
