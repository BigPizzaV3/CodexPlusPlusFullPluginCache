---
name: workbranch
description: Use when the user wants to keep the outcome of the conversation (tasks, decisions, open questions, ideas, next steps) in Workbranch, asks what's open, overdue or decided in a Workbranch project, says something is done or moves a date. Works through the Workbranch tools.
---
# Workbranch

Workbranch keeps the results of AI conversations: tasks, decisions, questions only the user can answer, and parked ideas, filed into the user's projects and folders, with dates on their calendar. The Workbranch tools (`list_projects`, `get_brief`, `save_chat`, `update_items`, `search`, `read_thread`) come with this plugin.

## Saving
- Save when the user asks, and offer it once when a long session ends with decisions or next steps that aren't saved yet. Never save without the user's go-ahead.
- Call `list_projects` and pick the project that fits. If nothing fits, ask, or create one by passing `projectName`.
- Split the session into topics, one per subject, in a single `save_chat` call. Give each topic the date it was mainly discussed when the session spans days. Saving again with the same topic titles only adds new items.
- Tasks are concrete next actions starting with a verb, with a due date only if one was agreed and an owner if it's clear ("ChatGPT" for your own). Decisions are settled choices, with the reason. Questions are open points only the user can decide. Ideas are parked suggestions. Recurring work gets `repeat` (and `times` for several per period).
- Only what the session actually contains. Never invent dates, owners or decisions. Never include passwords, keys, tokens or other secrets.
- Afterwards, tell the user what was saved per topic and give the links.

## Resuming and updating
- "What's open?": `list_projects`, then `get_brief`. Lead with overdue items and questions waiting on the user.
- Items with a thread were discussed in Workbranch: call `read_thread` before acting on them.
- When the user says something is done, moves a date or answers a question, call `update_items` (`done`, `due`, or `decision`).
