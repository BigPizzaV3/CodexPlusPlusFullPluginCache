---
name: get-started
description: Help a person start using Magic in ChatGPT. Use when they first connect Magic, ask what Magic can do, or want to hand off their first task to Magic's 24/7 assistants.
---

# Get started with Magic

Magic's assistants are people who work on real tasks, such as research, scheduling, and bookings, at any hour. The Magic tools act on the user's own Magic account. Explicit instructions from the user take priority over this guide.

## First use

1. Call `get_profile` to confirm which Magic account is connected. Greet the user by name if the profile has one.
2. Explain in one or two sentences that you can hand off a task to Magic, list their recent tasks, or check the status of a task.
3. If the user already described a need, offer to turn it into a task.

## Hand off a task

1. Collect what Magic needs to do the work: the goal, any deadline, and limits such as budget, location, or times. Ask only for details that are missing and necessary. Don't invent details the user didn't give.
2. Write a short title and a clear description. Read them back and wait for the user to confirm, because assistants start working as soon as Magic receives the task.
3. Call `create_task` once with a new `requestId`. Pass `dueDate` only if the user gave a deadline.
4. If the result is `HANDOFF_FAILED` or the call fails, wait a minute, then retry with the same `requestId` and the same details. Never create a second task for the same request.
5. Tell the user that Magic received the task and that an assistant will pick it up. Don't promise when it will be done.

## Check on tasks

-   Use `list_tasks` for an overview and `get_task` for one task.
-   Report the status the tools return. Don't guess at progress beyond that.

## Stop or decline

-   If a tool returns `TEAM_SETUP_REQUIRED`, tell the user to finish setting up their Magic account in Magic Workspace.
-   These tools can't cancel tasks, message assistants, change plans, or take payments. Say so, and point the user to Magic Workspace.
