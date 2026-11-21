---
name: triage-support-inbox
description: Triage open Weav support conversations, draft replies grounded in the workspace's training data, and send or update conversations only after the user confirms. Use when the user asks to review, prioritize, or reply to their Weav support inbox.
---

# Triage the Weav support inbox

Use the Weav MCP tools for the connected workspace only.

1. Call `search_conversations` for open conversations. Sort the results by priority (urgent, high, normal, low), then by oldest last message.
2. For each conversation the user wants to handle, call `get_conversation` to read the full thread and `get_customer` if customer context helps.
3. Before drafting an answer, call `search_training_data` with the customer's question. Base the reply only on what the training data says. If nothing relevant is found, say so and ask the user how to answer instead of guessing.
4. Show the draft reply to the user. Call `send_reply` only after the user explicitly approves the exact text, because the reply is delivered to the customer.
5. Call `update_conversation` to change status, priority, or assignee only when the user asks for it.
6. If the user gives you a new answer that should be reused, offer to save it with `add_training_data` as a Q&A.

Do not delete training data or Help Center content as part of triage. Do not message customers in bulk.
