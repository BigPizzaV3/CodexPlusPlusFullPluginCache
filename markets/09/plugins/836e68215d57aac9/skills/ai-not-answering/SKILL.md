---
name: ai-not-answering
description: Use when an admin says the Ciarem AI agent stopped answering, isn't replying to a customer, or asks which chats are paused.
---

# The AI is not answering

Admins only: if a tool answers `requires_admin`, tell the user only workspace admins can check this.

1. For one customer, call `get_paused_conversations` with `query` set to their name or phone. For all of them, call it with no query.
2. Explain each `reason`. `rule`: a transfer rule paused the AI (name the `rule`), and it resumes by itself when the customer sends a genuine request. `reply_limit`: the AI sent 100 messages in 24 hours, usually a loop with another bot, and it resumes at `resumes_at`.
3. **Not paused?** Call `explain_ai_decisions` for that contact. It shows whether the AI transferred the chat to a person, declined to answer, or a rule fired. When a teammate is handling the chat, the AI stays out of it.
4. **Nobody gets an answer?** Call `get_account_health`: the AI may be switched off, a channel disconnected, or a readiness check failing. Report what fails. Never switch the AI on with `set_ai_active` unless the user asks.
5. **Resume one chat** only when the user asks and confirms: `resume_ai`. The AI answers the customer's next message, not the ones already sent.
6. If the same rule keeps pausing chats it shouldn't, fix the rule with `update_transfer_rule` (the `tune-ai-agent` skill).
