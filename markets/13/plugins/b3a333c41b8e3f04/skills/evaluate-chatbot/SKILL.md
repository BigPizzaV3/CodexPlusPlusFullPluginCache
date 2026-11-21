---
name: evaluate-chatbot
description: Check topic coverage, launch readiness, customer role-play, follow-up answers and language quality for a new or existing ChatbotGen chatbot.
---

## Select the chatbot first

Use the active chatbot from this conversation unless the user names another or asks to create a new one. For an existing chatbot without an active selection, call `list_chatbots`; match the name and website, or show the choices if ambiguous. Connect the account when prompted. Never create a new chatbot as a substitute for finding an existing one. If listing is unavailable, explain that account connection is needed; do not guess IDs.

State the selected name and website briefly, keep its ID for subsequent calls, and switch only when requested. A newly created chatbot becomes the active selection. Demo tokens work until expiry or claim, and only while no account is connected. If the user connects while working on a demo, tell them which chatbot it is, ask whether to keep it in their account, and after a yes call `claim_chatbot` with its token and `confirmed: true`; use the returned `chatbot_id` from then on. Never create a replacement for a demo: it can use up the account's only chatbot slot. If they keep it through the claim link instead, list the account's bots. Do not assume selection persists into a new conversation. Keep test-session state tied to the selected chatbot, scenario and language; switching bots clears the previous test conversation ID. Start a fresh scenario with necessary context when the user asks the same follow-up on a different bot.

Inspect `get_chatbot` and source inventory first. Inspect `training.pages_failed` and individual source statuses: processed pages may include failures. If training is pending or essential sources failed, report the limitation and avoid presenting tests as a final verdict.

For each requested topic, use `search_knowledge` and inspect source content when needed, then call `test_chatbot` with representative customer questions. A source title, retrieved match or ready status alone does not prove coverage. Classify topics as covered, partial, missing, conflicting, or not yet verified, with evidence and an actual tested answer.

For readiness, cover the business's core customer questions, unclear requests, questions outside its knowledge, and requests to speak with a person. For role-play, start a fresh test conversation for each persona/scenario and use the returned conversation_id for follow-ups. For language checks, ask equivalent questions in requested languages and compare factual consistency, terminology and configured language behavior. State which scenarios and languages were actually tested.

Tests consume the bot's message allowance. Read `usage.messages_remaining` and `usage.gate` before testing. Budget across this conversation, reuse still-valid evidence, and normally reserve two demo messages for the owner to try interactively. Start with 1–3 high-value questions on a demo, expanding only when the requested scope and allowance justify it. An explicit user request to spend the remaining allowance takes precedence over that reserve. Prioritize requested languages and count follow-ups and before/after checks in the same budget. A null remaining count with unlimited=true is not zero. Use the updated usage returned by every test; stop at quota errors. The test path uses real retrieval, instructions and model, but does not execute external tools, bookings or handoffs. Do not claim those integrations are verified; use the returned chat link for interactive checks of those actions.

Summarize failures and specific remedies. If the user also authorized improvements, use train-chatbot, wait for training status to settle, and retest the failures. Otherwise report suggested changes without writing them. Never guarantee universal correctness from a sample.

Present a compact result per topic/scenario: tested question, answer outcome, supporting source, and remaining gap. Separate verified answer behavior from integrations that still need an interactive check. State what remains unverified when the budget cannot cover the requested scope. After a useful result, offer one concrete next action or the returned keep/dashboard link if capacity prevents continuing.
