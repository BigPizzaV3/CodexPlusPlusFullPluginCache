---
name: get-started
description: Get oriented in a Reos user-research workspace. Confirms which Reos organisation is connected, lists the projects the user can access with where each one is in the research process, and suggests a first question to ask about one of them.
---

Use this when the user is new to Reos in this conversation or asks what they can do with it.

1. Call `list_organizations` to confirm which Reos organisation the connection uses, and tell the user its name.
2. Call `list_projects`, then `get_project_status` for up to three of them, and show each project's name with how much raw data, observations, insights and solutions it has.
3. Ask which project the user wants to work in, and suggest one question they could ask about it, for example "What are the top insights, with the quotes behind them?"

Only read during setup. Do not create, edit or delete anything unless the user asks for it.
