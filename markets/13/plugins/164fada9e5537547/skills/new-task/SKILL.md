---
name: new-task
description: Create a task from a title, e.g. "/writesonic-agents:new-task Refresh the pricing page for AI search". Assigns it to you unless told otherwise.
disable-model-invocation: true
---
`whoami` first. Show the task you are about to create from "$ARGUMENTS" (title, project, assignee = the current user unless another is named) and ask for confirmation. On yes: `create_task`, then `update_task` with action="assign". Report the created task id.
