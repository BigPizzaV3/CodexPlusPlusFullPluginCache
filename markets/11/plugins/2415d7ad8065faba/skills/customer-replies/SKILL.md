---
name: customer-replies
description: Use when the owner wants to read what a customer said and answer them through AssistantLabs.
---

# Replying to a customer

No conversations yet because there is no agent or no channel connected: say so in one line and go to the start skill (**Build the agent**, or **The connect link**).

1. Read the conversation with `get_conversation` first, so the reply answers what was said. It shows the most recent 200 messages, and `partial` says when there were more. In its messages, `customer` is the person who wrote to the business.
2. Draft the reply and show it to the owner in their language.
3. Send it with `send_message_to_customer` only after the owner approves that exact text.
4. Tell the owner what the result says. `sent` means the channel accepted it for delivery, though on WhatsApp it can still fail to arrive afterwards. `failed` means it did not go out, and `recorded` means it is saved on the conversation but nothing confirms the channel took it.

Sending pauses the AI agent on that conversation, so tell the owner a person now handles what comes next.

To reply to someone found by name, `get_contact` gives the `threadIds` of their conversations.

On WhatsApp, a plain message only delivers within 24 hours of the customer's last message. After that, use `list_whatsapp_templates` to find an approved template and `send_whatsapp_template` to send it, with a value for every placeholder the template lists. A template marked `fromAppOnly` has header or button variables and goes out from the AssistantLabs app. A template reaches the customer at once and can't be taken back, so confirm with the owner before sending.

If a send fails, check the conversation before trying again, because a timed-out send may still have gone out.

Phone numbers and emails in common formats are automatically hidden in conversations, and a search can't find them. `get_contact` takes a `threadId`, which is how to reach a customer with no name. Set `includePhoneAndEmail` or `includeNotes` only when the owner asks for that detail. Card numbers, ID numbers and passwords stay hidden either way.
