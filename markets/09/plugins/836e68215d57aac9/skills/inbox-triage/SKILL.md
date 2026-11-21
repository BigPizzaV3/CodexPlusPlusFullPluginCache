---
name: inbox-triage
description: Use when the user asks what needs their attention in Ciarem, which customers are waiting, or wants help catching up on their inbox.
---

# Inbox triage

1. Call `list_conversations` with `status: "open"` and `assigned_to_me: true` (limit 25). If the user is an admin and asks about the whole team, also call it with `unassigned: true`.
2. Rank by who has waited longest: `last_inbound_at` older than `last_message_at` of our reply, oldest first, then `unread_count`.
3. For the top 5, call `get_conversation` (limit 15) and write one line each: who, channel, what they want, how long they've waited.
4. Under each line, draft a short reply in the customer's language and tone. Say it is a draft: Ciarem's tools can't send messages from here. Link the conversation's `url` so the user can send it from Ciarem.
5. Skip conversations `handled_by: "ai"` unless the customer asked for a human; mention how many the AI is covering.

Never invent order numbers, prices or policies in a draft. If the answer needs a fact, call `search_knowledge` first; if it isn't there, say the draft needs that fact filled in.
