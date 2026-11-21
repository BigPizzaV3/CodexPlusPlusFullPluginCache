---
name: save-to-phrase-bank
description: Save an explicitly selected English word or expression to Contexta with its original, chat, or labeled generated context. Also use when asked to extract and save a useful expression from a supplied sentence; do not auto-save every unfamiliar word.
---

# Save to Phrase Bank

Keep the reply focused on the learner’s result and next action. Do not show phrase, task, operation or request IDs, raw status fields, or tool/rendering diagnostics. Use titles and returned website links. Do not announce that a native widget was rendered or reopened; the widget already presents the result.

Native Contexta UI is required when available: after saving, display the exact saved item's passive card as specified in the shared workflow. Do not start audio or choose another phrase just to show the interface.

Save one explicitly requested expression and its provenance. Read and apply [the shared workflow](../../references/workflow.md) before replying or calling the service.

## Choose the expression and keep its context

- For an exact word or phrase, keep the learner's selected surface form. Do not silently replace it with a synonym, infinitive or different expression.
- When asked to save a useful expression from a full sentence, select the smallest reusable collocation or functional expression. Keep essential prepositions and negation that defines the intended expression, such as “can't rule out.” Sentence polarity can remain in its exact source context: from “We did not get the ball rolling until Monday,” save `phrase="get the ball rolling"` and retain that complete negated sentence in both `context` and `original_sentence`, with `context_source="original"`. Never rewrite the source sentence into a positive claim.
- If multiple materially different cores are plausible, offer a small choice before saving. Do not automatically mine all unfamiliar expressions or send the entire chat.
- Preserve the exact supplied source sentence in `original_sentence`. Prefer that sentence as `context` with `context_source="original"`.
- If there is no supplied source sentence, relevant actual chat wording can be `context_source="chat"`. Otherwise an optional neutral practice example can use `context_source="generated"`; clearly label it as generated and never present invented facts as the learner's biography or a source quotation.
- A phrase without context can still be saved. Generated examples are not evidence that the learner has used the phrase.

## Save once

Call `save_phrase` with the chosen `phrase`, optional `context`, `context_source` and exact `original_sentence` when supplied. Explicit save intent authorizes this additive save; no extra project, trial or generic confirmation is required.

Return the actual expression, short context and provenance, `saved`/`already_saved` result and exact Phrase Bank URL. A repeated save must not be described as a new entry or new learning progress. Preserve existing learned state. Do not promise morphology-aware deduplication or automatic mastery.

After saving, offer review or short pronunciation only when useful to the learner's request. Do not start an audio task, new project or reminder automatically.
