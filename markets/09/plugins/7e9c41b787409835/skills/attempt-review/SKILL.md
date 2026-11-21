---
name: attempt-review
description: Review one or a small bounded set of the user's authorized TCFCAN attempts or current listening/reading wrong-book entries. Use when the user asks why an answer was wrong, requests evidence from a specific attempt, or wants a small wrong-answer review; do not use for general progress diagnosis alone.
---

Review only records that TCFCAN returns for the connected account, within one module. Use the selected attempt's module; otherwise ask the user to choose one module before an unspecified or all-module review.

1. If the user selected a recent record, obtain its `attemptRef` from `get_recent_attempts`. For the current listening or reading wrong book, call `get_wrong_book`; do not infer membership from recent attempts.
2. Call `get_attempt_detail` only for the selected reference or a small number needed for the requested review. With no requested quantity, read at most five details.
3. Report current total, list entries returned, details successfully read, and the actual analysis scope as different quantities. Fetch another wrong-book page only when the user asks to continue.
4. For listening and reading, treat only `verified_answer_evidence` as stored evidence supporting the correct answer. A distractor does not need and must not be given a fabricated locator sentence. Treat `question_context` as context, not answer evidence.
5. For writing and speaking, distinguish the user's response, stored TCFCAN feedback, and your new interpretation. Respect every coverage and truncation field; missing feedback or evidence does not prove there was no error.
6. Explain the selected attempts in text and label every new explanation as AI interpretation. Do not automatically request a whole-module diagnosis card after a review.

For a listening or reading error classification, use the same bounded taxonomy as `learning-diagnosis`. Text-visible signals may support a candidate such as number, negation, contrast, scope, relation, synonym, viewpoint, main idea, detail, or over-inference only when the exact relationship can be explained from returned context. The selected option and correct-answer evidence alone cannot establish whether the user knew a word, recognized it in audio, parsed a sentence, or found the source location. Ask one concise question for those distinctions or mark the cause as insufficient evidence. Never turn one classified item into a stable learner weakness.

`attemptRef` is only for attempt detail and `questionRef` is only for practice-question retrieval. Never interchange them. Stop on `RATE_LIMITED`, disclose unread scope, and do not loop, bulk-fetch, or claim a whole-book review from paginated results.
