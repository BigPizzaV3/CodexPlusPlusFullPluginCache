---
name: get-started
description: Get started with Chatfuel in ChatGPT. Picks the bot to work on, shows its channels and whether the AI replies there, and suggests a first task.
---

# Get started with Chatfuel

Use this right after the user connects Chatfuel, or when they say they are new to it.

## Steps

1. Call `get_playbook` with the name `onboarding` and follow it.
2. If that is not available, call `list_bots`. When the user has several bots, ask which one to work on, one question per message.
3. Call `get_bot` for the chosen bot. Tell the user in plain words which channels are connected and whether the AI is on for each one. Do not use field, enum or scope names.
   If no channel is connected, offer to connect one: `create_connection_link` gives a sign-in link for WhatsApp, Instagram, Facebook or TikTok. Give the link only to the user, and check the channel with `get_bot` after they say they are done.
4. Suggest one next step that fits what you found, for example: check why the bot is silent, review what the AI knows about the business, or add an FAQ answer.

## Rules

- Do not change anything during this check. Before any change, describe it and wait for the user's yes.
- If the connection is read-only, say that changes need the user to reconnect with full access.
- Flows are not available here; point the user to the Chatfuel dashboard at https://panel.chatfuel.com for them.
