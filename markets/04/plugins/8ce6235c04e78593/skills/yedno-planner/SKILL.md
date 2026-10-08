---
name: yedno-planner
description: Plan, create, update, and track private Yedno tasks or recurring obligations when the user asks what to do now or to manage their Yedno plan. Do not use for calendars, meetings, or unrelated productivity systems.
---

# Yedno Planner

Use the connected Yedno tools only for the user's private planning data. Reply in Polish by default unless the user uses another language.

## Recommend the next action

When the user asks what to do now, first call `get_execution_profiles`. Select the profile explicitly named by the user; otherwise choose the active profile. Then call `get_now_recommendations` with the chosen profile and the context the user supplied, such as available time or energy.

Present the best recommendation with a short reason. If no task fits, say so and suggest the missing context instead of inventing a task.

## Manage tasks safely

- Before creating or editing a task that uses an area, requirement, or trait, call `list_task_classifications`; never guess their IDs.
- Before updating, completing, reopening, archiving, or changing the remaining effort of a task, call `get_task` to obtain its current `version`.
- If a tool reports a version conflict, retrieve the task again, explain the changed state briefly, and retry only if the requested change is still unambiguous.
- Treat an `area` as where the task belongs, a `requirement` as what is needed to do it, and a `trait` as the kind of work it is. Do not substitute one for another.
- Preserve a user's effort estimate as either one duration or a series of sessions. Do not introduce a permanent numeric priority.

## Obligations, relations, and work sessions

- For a recurring obligation, call `preview_obligation_recurrence` before `create_obligation`. An obligation is one recurring rule with occurrence state; do not create a separate endless list of tasks.
- Create task relations only when the user states the intended relation. Use task graph information to explain dependencies, but do not infer new relations.
- Before starting work, call `get_current_work_session`. Do not start a parallel session when another one is running or paused.

## Scope and confirmations

Use read tools for questions about existing data. Call a write tool only when the user explicitly asks for that change. State what was changed and include any important resulting status or next step.

Yedno does not manage calendar meetings, email, or third-party task systems. For those requests, do not invoke Yedno tools.
