---
name: support-queue
description: Work through the Aide support queue. Use when the user wants to find conversations that need a person, read them with the customer's orders, and prepare a note or reply for the user to approve.
---

Use the Aide tools to help the user work their support queue. The user's explicit instructions take priority over these steps.

1. Find conversations with find_conversation, using the view `needs_a_person` or the filters the user names.
2. For each conversation the user picks, read it with get_conversation and list_messages, and check get_draft for Aide's draft reply.
3. If the customer asks about an order, read get_conversation_orders. For returns, use check_return_eligibility.
4. Answer policy questions from the workspace's knowledge with search_knowledge, and name the article you used.
5. Show the user the reply or note you propose. Send it with reply_to_conversation or add_note only after the user approves the exact text.

Do not refund, cancel, or approve or reject an order change unless the user asks for that action on a specific order. If a tool returns an error or no result, tell the user what it said instead of guessing.
