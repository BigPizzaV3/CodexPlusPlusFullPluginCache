---
name: get-started
description: Set up AssistLoop in ChatGPT. Find the user's organizations and agents, say what the plugin can do for each, and suggest a first task.
metadata:
  short-description: Find your agents and pick a first task
---

Help the user start using AssistLoop.

1. Call `list_organizations`. If the user belongs to more than one, ask which one to use.
   If none can use the tools, say that their AssistLoop plan does not include this
   access and stop. Do not suggest buying or upgrading anything.
2. Call `list_agents` for that organization and show each agent's name, and whether
   tickets are turned on for it.
3. Tell the user what they can ask for, in one short list:
   - read recent conversations and reply to a customer;
   - list, update and comment on support tickets;
   - add text or Q&A training and check its progress;
   - crawl a website and train the agent on its pages;
   - rename an agent, change its AI model, or hand chats over to the team.
4. Explain that replies to customers and ticket emails are sent for real, so ChatGPT
   asks before sending them.
5. Suggest one first task based on what you found, for example: "Show the open
   high-priority tickets for Support agent."

Use only the data the tools return. Do not guess ids: take them from the list tools.
