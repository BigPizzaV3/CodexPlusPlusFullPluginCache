---
name: helena-get-started
description: Help someone setting up the main Helena plugin in ChatGPT choose and try a first task using their connected marketing platforms.
---

Briefly welcome the user to Helena. Use the plugin's `get_connected_integrations` tool to identify which platforms this Helena account has connected.

- If a connected platform has an available read tool, suggest one concrete task the user can start with. Use any platform or goal they already mentioned. For example, offer to review recent Instagram posts and suggest what to post next, or show which channels drove the most sessions in Google Analytics. Match the suggestion to the tools and access available in this conversation.
- If none of the connected platforms has a usable read tool, offer to open the Helena workspace so the user can see their calendar and files. If the user wants to connect a platform, point them to [Helena integrations](https://agent.enrichlabs.ai/marketing/integrations). If Helena reports an account setup or plan requirement, show the link from the tool response and explain what it asks them to do.
- Run the proposed read after the user chooses it. Summarize what the data shows and suggest one next step. If the requested data is missing, explain what is needed to fetch it.

Keep this setup workflow read-only. Avoid publishing, scheduling, sending, editing, or saving anything during setup.
