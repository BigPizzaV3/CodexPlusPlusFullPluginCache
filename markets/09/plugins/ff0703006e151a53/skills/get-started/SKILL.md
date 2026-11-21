---
name: get-started
description: Give a first overview of the user's Make Agent Fast agents — which are live on the website, recent conversations and leads — and suggest the next useful step.
---

Use this when the user has just connected Make Agent Fast or asks what it can do.

1. Call `list_agents`. If the company has no agents, offer to build one: ask for the business website address and call `create_agent_from_website`, or, if the business has no website (only Telegram or Instagram, for example), ask for its products, prices, hours, location and how customers order, and call `create_agent_from_notes`.
2. For each agent (at most three), call `get_report` with `days: "30"` and summarize in one short paragraph: conversations, leads, whether the website widget is on, and the most asked questions.
3. Call `list_unanswered_questions` for the busiest agent. If there are any, say how many and offer to fix them together (see the `fix-agent-answers` skill).
4. End with two or three concrete next steps the user can ask for, for example "read the latest WhatsApp conversation" or "list this week's leads".

Rules:
- Every agent tool needs the `agent_id` from `list_agents`; never guess one.
- Report only what the tools return. If a number is zero, say so plainly.
- Ask before any tool that changes data or reaches a customer: `create_agent_from_website`, `create_agent_from_notes`, `add_knowledge`, `save_answer`, `reply_to_customer`, `update_lead`, `set_website_widget`, and `test_agent` (it uses credits).
