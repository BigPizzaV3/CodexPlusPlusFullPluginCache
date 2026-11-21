---
name: daily-brief
description: Use when the owner asks for a summary of today in their AssistantLabs workspace, such as who is waiting for a reply and what is booked.
---

# Daily brief

Give the owner a short picture of today. This only reports: it sends nothing, changes nothing and does not offer to act on its own.

1. `list_conversations` for the last few days. `waiting` means the last message came from the customer and has not been answered. The list holds no message text, so use `get_conversation` for what someone said.
2. `list_appointments` with today's date as both `from` and `to`.
3. `list_helpdesk_tickets` for what is open. `waiting` means the same here.
4. `list_tasks` with `scheduled` set to `today`, and again set to `overdue`.

Report it in plain words, most urgent first. Lead with who is waiting and how long. Leave out anything that is empty.

**A new workspace** (no agent yet, or nothing connected, so every list is empty): don't report an empty day. Say in one line that there is nothing to brief yet because the agent and channels aren't set up, and go to the start skill: **Build the agent** when `get_workspace_setup` shows none, else **The connect link**. Never make a second agent.

If a tool says this isn't available for this workspace, or that it needs a permission that wasn't ticked when AssistantLabs was connected, say so in one line and carry on with the rest.
