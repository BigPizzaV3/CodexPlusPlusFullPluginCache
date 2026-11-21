---
name: fix-agent-answers
description: Find questions a Make Agent Fast agent answered wrongly or could not answer, agree the correct answer with the user, save it, and confirm the agent now uses it.
---

Use this when the user says the agent gave a wrong answer, or wants to fix unanswered questions.

1. Call `list_agents` to get the `agent_id`.
2. If the user quotes a wrong answer, find that conversation with `list_conversations` (use `search` with words from the question) and read it with `get_conversation`. Otherwise call `list_unanswered_questions`.
3. For each question, ask the user for the correct answer, or draft one from facts they give you. Never invent prices, hours, addresses or policies.
4. Show the final wording. Explain that saving supersedes the previous answer and can send replies to customers waiting for it on connected channels. Use `save_answer` only after the user approves those effects and the wording.
5. Confirm the fix with `test_agent`, asking the same question, and show the user the agent's new answer and its source.
6. If the answer needs a whole page of information rather than one reply, offer `add_knowledge` with the page address or the text.

Each `save_answer` call creates a new knowledge source and uses embedding credits; do not retry a successful save. `test_agent` uses credits, so test each fixed question once.
