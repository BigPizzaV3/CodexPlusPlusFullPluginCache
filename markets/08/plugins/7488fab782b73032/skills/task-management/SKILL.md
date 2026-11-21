---
name: task-management
description: Review, create, and update Staffology tasks and assignments for the connected organisation.
---

# Task management

Use Staffology's task tools for task status and explicit task changes in the connected organisation.

- Use `list_tasks` for active tasks, optionally narrowed by priority; use `tasks_today_status` for tasks due today and `unfulfilled_tasks` for incomplete or overdue assignments by employee.
- Use `create_task` only for an explicit creation request. Map the requested name, description, priority, deadline, and assignee exactly. Read those details back before the call; if any detail is inferred or ambiguous, ask for clarification. Call it once and report the returned assignee-match result.
- Use `update_task` only when the target and requested fields are clear. It accepts a partial task name only when exactly one task matches; an ambiguous name is refused and changes nothing.
- Report only changes confirmed by the tool result. A repeated `create_task` call creates another task, and a renamed task cannot safely be retried through its old name.

The task tools cannot edit attendance, approve leave or change pay, and must never stand in for another write. Those operations have their own tools (for example `adjust_attendance_punch` or `approve_leave_request`); use the one that matches the request, or say that none does, and never perform an adjacent task change instead. Nothing on this connector moves money.
