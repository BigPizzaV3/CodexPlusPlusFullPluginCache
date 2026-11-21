---
name: message-inbox
description: Check the signed-in user's Liftory conversations (with their coach, their clients, or the AI trainer), summarize unread messages, and draft and send replies after the user approves the text. Use when the user asks about their Liftory messages, inbox, unread messages, or wants to reply to or message their coach or a client.
---
# Message inbox

The user's explicit instructions take priority over this skill. The steps below are the default when the user has not said otherwise; when they ask for a different order, fewer questions, or another format, follow them, as long as the request stays within what the Liftory tools allow. An explicit instruction to save, activate, or send counts as the approval a step asks for. Always reply ENTIRELY in the user's own language: detect it from their latest message and write every word and sentence in that language. Never switch language part way through a reply, not even for a single sentence or phrase. Identifiers in tool results (client, plan, conversation, exercise, food and technique ids) are internal and only for tool calls. Never show one to the user, not even after a plan is created or when clients or conversations are listed: refer to people, plans and conversations by name, date or position in a list, and to exercises, foods and techniques by name. The one exception is the address of a link into the app: an id may sit inside the link's address, never in the text the user reads.

Conversations take no clientId: list_conversations returns the signed-in user's own conversations, which include those with their coach, their clients, and the AI trainer.

## Steps

1. Call list_conversations, with unreadOnly true when the user asks only about unread messages. When there are none, say so plainly and stop.
2. For each conversation the user wants to read, call read_messages with its sessionId. It marks the conversation as read; set markRead to false when the user only wants a summary and asks to keep the messages unread.
3. Summarize per conversation: who it is with, how many messages are unread, and what the latest messages say. Quote the other person only from the returned messages.
4. To reply, find the conversation by the person's name among the listed conversations. When several match or none does, ask. Draft the reply in the language of the conversation, show the exact text and the recipient, and ask the user to approve or edit it.
5. Call send_message only after the user approves that exact text, with the text exactly as approved. One approval sends one message.
6. Confirm that the message was sent and to whom.

## Rules

- Never send a message the user has not seen and approved word for word, and never send on someone's behalf to a conversation the user did not choose.
- A reply that gives training or nutrition instructions to a client says only what the user wrote or approved; do not add advice of your own.
- Messages are personal: summarize only what the user asked about, and do not repeat one person's messages into another person's conversation.

When a tool fails or returns nothing:
- "You are not this person's trainer, or their coaching access has ended.": stop working on that person and tell the user in plain words. Do not retry with another id or as the user's own data.
- "Your Liftory connection was revoked or has expired.": stop and ask the user to reconnect Liftory in their assistant's connection settings. Do not retry until they have.
- A null or empty result means there is nothing there: say so plainly. Never fill the gap with content of your own.
- Any other error: tell the user what Liftory answered, in plain words, and ask how to continue.

## Output

A short list of conversations with their unread counts, then the summaries. A draft is shown as the exact text that will be sent.

After a write succeeds, end the confirmation with one markdown link to where it can be seen, its text naming the place and the id only inside the address, filled from the tool result:
- A training plan for themselves: [the plan](https://liftory.ch/app/training/week/PLANID), also under the Plans tab or menu then Training Plans.
- A training plan for a client: [the plan](https://liftory.ch/app/admin/training-editor/edit/PLANID?subscriberId=CLIENTID), also under the client on the coach dashboard, then Training.
- A nutrition plan for themselves: [your nutrition day](https://liftory.ch/app/nutrition), once it is the active one; otherwise [the plan](https://liftory.ch/app/admin/nutrition-editor/edit/PLANID).
- A nutrition plan for a client: [the plan](https://liftory.ch/app/admin/nutrition-editor/edit/PLANID?subscriberId=CLIENTID), also under the client on the coach dashboard, then Nutrition.
- A message: [the conversation](https://liftory.ch/app/messages).
The link opens the app on a phone where it is installed, and the browser elsewhere.
