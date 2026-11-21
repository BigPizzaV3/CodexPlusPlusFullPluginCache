---
name: phrase-review
description: Review an owned Contexta Phrase Bank item using today, due/needs-practice, random, or an explicit phrase selection, with truthful context and selection reason. Use for phrase review, not general vocabulary quizzes or automatic reminders.
---

# Review a saved phrase

Keep the reply focused on the learner’s result and next action. Do not show phrase, task, operation or request IDs, raw status fields, or tool/rendering diagnostics. Use titles and returned website links. Do not announce that a native widget was rendered or reopened; the widget already presents the result.

Native Contexta UI is required when available: use the card returned by `get_phrase_review_card` as specified in the shared workflow. Text supplements it; do not repeat selection or render the same card twice.

Help the learner revisit their own expressions with useful context. Read and apply [the shared workflow](../../references/workflow.md) before replying or calling the service.

Call `get_phrase_review_card` with:

- `selector="today"` for “What should I review today?” or unspecified review intent. The service uses the account's timezone and keeps today's selection stable; do not inject a host timezone or invent a schedule.
- `selector="due"` for scheduled/needs-practice review.
- `selector="random"` only for an explicit random/surprise request.
- `phrase_text` for a phrase the learner names. Use the exact requested expression; a missing result does not authorize trying today, due, or random cards, saving it, or substituting another phrase.
- An actual returned `word_id` for a specific owned phrase. Never guess an ID. For another due/random item use actual previously seen IDs in bounded `exclude_word_ids`; do not add exclusions to today's stable selection.

Make one random lookup per learner request. Keep its returned `word_id` for subsequent explicit practice or resume; do not select a second phrase to replace, confirm or redisplay the first. A phrase-only request shows its card and does not authorize preparing audio practice. Another random selection requires the learner to explicitly ask for another phrase. Recover uncertain outcomes using an existing returned identity, without silently drawing a substitute.

Show the actual phrase, supplied meaning if available, full saved context and the service's selection reason. Label original, chat and generated context distinctly. A fallback saved item is not necessarily overdue; do not rename a “can practise today” reason into a measured weakness.

The card's primary **Practise phrase** action assesses the expression itself: use `start_phrase_practice` with its real `word_id`, `mode="reading"`, `practice_target="phrase"` and a stable idempotency key. **Read aloud** reads its complete saved context using `practice_target="context"`; **Speak with this phrase** uses `mode="speaking"` for a free answer containing the expression. Never describe these as the same task. If `ready_practice_tasks` supplies the matching owned task, resume it with `show_practice_widget(task_id=...)` instead of starting another. Otherwise let the learner choose; do not submit a fabricated answer. Full practice and detailed bank/history remain on the returned website link.

Automatic Today/Due/Random cards contain actual phrase entries and exclude historical single-word records. Keep the service's exact phrase and canonical saved contexts. A missing or oversized saved context does not authorize inventing a reading passage; offer exact-expression practice or the website instead.

Retrieval, seeing a phrase or listening to its reference is not mastery or productive-use evidence. A read-aloud score is pronunciation evidence; productive use requires the service's actual eligible recognized phrase use. Do not mark learned, advance a review interval, or declare improvement from viewing/retrying a card.

For empty/unavailable/due-empty results, explain the actual state. Offer to save a selected expression or, on request, show a clearly labeled chat example. Do not silently add sample phrases to the bank or invent personal history. Daily retrieval works without notifications; create no reminder unless the learner separately asks and the host supports it.
