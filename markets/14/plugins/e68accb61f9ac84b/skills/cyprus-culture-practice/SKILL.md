---
name: cyprus-culture-practice
description: Prepare for the Cyprus culture exam with questions based on the learner's Vocabulum progress. Example requests include “Quiz me on Cyprus culture in Greek” and «Проверь меня по культуре Кипра на греческом». Greek language A2/B1 exam practice belongs to greek-practice.
---

# Cyprus culture exam practice

- Start on a short request without asking the learner to select a topic. Respect a named topic and language. Use Greek for an explicit exam-language practice request. For a generic review start in the learner's language.
- If both question tools are available, call `get_cyprus_practice_question` with `intent: auto` for a general request such as «Повтори со мной культуру Кипра». Use `review` when the learner explicitly asks for previously studied facts and `learn` for new material. Set `locale: el` for Greek exam practice, otherwise use `ru` or `en`. Pass `topic` only for a named topic supported by the tool.
- Show the returned question and options A–D, then wait. Send the issued `token`, chosen `option` and language to `check_cyprus_practice_answer`. If the learner asks to skip, send `skip: true` with the token. Ask for the next question only after a confirmed answer or skip. Retry a temporary check failure with the same token and choice. On `invalid_question`, explain that the question needs to be opened again.
- If the tools are unavailable or access is limited, direct the learner to the [Vocabulum Cyprus culture track](https://www.vocabulum.app/miniapp/cyprus-exam). Offer to discuss a question they provide. Give source-based general practice only if the learner chooses it, and identify it as general. Do not invent Vocabulum questions, answers or progress.
- On `culture_reconnect_required`, offer to reconnect with permission for culture practice. On `limit_reached` or `no_questions`, offer the returned app link. If a request for a different theme returns the open question, invite the learner to finish or skip it first. Reject bank exports, lists of answers and requests for other learners' data before calling the tools. Keep lesson feedback separate from app progress and official exam grading.
