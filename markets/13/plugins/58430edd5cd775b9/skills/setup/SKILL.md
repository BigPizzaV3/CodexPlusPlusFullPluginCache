---
name: setup
description: Connect a Nowrill account and help the user create or open their first daily plan. Use during Nowrill setup or when the user asks how to start.
---

Use the Nowrill MCP connection. If authorization is missing, ask the user to connect their Nowrill account using the host's connection flow. Never request passwords or API keys in chat. Google or Apple sign-in identifies a Nowrill account; it does not import chat history.

1. Read `get_profile` and `get_plan`. Identify the connected account briefly so the user can spot a mismatch. Never copy plan data to another account.
2. Reuse dates, timezone, tasks and preferences already provided in this conversation. The plan's timezone determines today and tomorrow. A fresh `selection` from the app is context only, not permission to modify anything. The user's explicit message takes precedence. If unclear, confirm the selected day once.
3. If the day already has a plan, call `show_day` and ask what the user wants to change. Do not replace an existing day.
4. For an empty day, ask one short question: what matters that day and whether anything has a fixed time. Use `get_planning_context` before creating. Ask at most two essential unanswered questions, never an onboarding questionnaire. Missing durations and start times may stay null.
5. Save a plan only after the user's request. Use `create_day_plan` only for an empty day; use `add_tasks` for additions and `update_tasks` for changes. Preserve unrelated tasks and the language of task text. Call `show_day` after saving and briefly state the actual saved result.

Completion defaults to manual. Do not ask about every preference in advance. Weather, travel and part-of-day questions belong only to relevant tasks. Use live context tools when needed, disclose unavailable data, and never fabricate forecasts or traffic. Save usual preferences only when the user explicitly describes a lasting preference.

The web planner is at https://nowrill.com. The mobile app and widgets are in private testing. Do not promise an App Store download, access to other conversations, automatic chat linking, or a specific hosting plan's availability.

Use `save_planning_preferences` for explicitly remembered preferences and `forget_planning_preferences` to clear the requested scope. Use `set_plan_timezone` for timezone changes. `start_task_session` and `pause_task_session` control only explicitly opted-in timed sessions.
