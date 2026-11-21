---
name: customer-conversations
description: Review and answer an AssistLoop agent's customer conversations. Use when the user asks what customers said, wants a conversation summarized, wants to reply to a customer as a teammate, or wants to hand a conversation back to the AI, close it or reopen it.
metadata:
  short-description: Read, summarize and reply to customer chats
---

Help the user handle the conversations customers have with one AssistLoop agent, on the
website chat widget, WhatsApp, Instagram, Messenger, Telegram or email.

1. Find the agent. If the user did not name one, call `list_agents` and ask which agent
   to use.
2. Call `list_conversations` to see the most recently active ones. Each shows the
   customer, the channel, the last message, `status` (open or closed) and
   `response_mode` (ai: the AI answers; human: teammates answer).
3. For one conversation, call `list_conversation_messages` (and `get_conversation` for
   its details). Summarize what the customer asked and what is still unanswered. Quote
   the customer's words; do not invent details.
4. To answer the customer, first make sure you have the right conversation. If more than
   one conversation matches the customer the user named, list them (customer, channel,
   last message) and ask which one.
   - If the user's message contains the reply itself, after a colon or in quotes (for
     example "Reply to Lena: ..."), call `reply_to_conversation` right away with exactly
     that text. Do not add a greeting or sign-off or change its wording; if you would
     change anything, use the next case instead.
   - Otherwise (the user asked you to write the reply, or said what it should say, as in
     "tell Lena it ships Friday"), show your draft and call `reply_to_conversation` only
     after they approve the exact text.
   The reply reaches the customer at once and cannot be taken back. It also switches the
   conversation to human mode, so the AI stops answering it; tell the user who it went
   to, on which channel, and that the AI has stopped answering.
5. To hand the conversation back to the AI, call `update_conversation` with
   `response_mode` ai. To close or reopen it, send `status` closed or open. A closed
   conversation must be reopened before its mode can change.

Plain text only in replies. If the customer can no longer be reached on their channel
(for example the WhatsApp reply window has closed), the reply tool refuses: say what it
said and do not retry.
