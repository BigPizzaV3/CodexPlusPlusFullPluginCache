---
name: povtori-learning
description: Use when an authenticated Povtori learner asks to configure their language pair, manage saved phrases, view progress, or start, continue, and complete a lesson. Do not use for unrelated general language tutoring.
---

# Povtori learning

Use Povtori's authenticated tools as the source of truth for the learner's settings, saved phrases, lesson state, and progress. Start every Povtori workflow by calling `get_learning_settings`.

## Tool failure policy

- If a logical tool call fails or returns an empty, malformed, or incomplete response, make at most two additional attempts with the same payload.
- The MCP tool itself performs one backend request per attempt. Do not invent a successful result while retrying.
- After three failed attempts in total, stop that operation and tell the learner that its result was not confirmed.
- Never repeat a successful `lesson_results` call or claim that a mutation succeeded before the tool confirms it.

## Establish the language pair

1. Call `get_learning_settings` and read `base_language`, `target_language`, and `learning_data_counts`.
2. If either language is `null`, ask which language the learner speaks and which language they want to practice. For example: Russian to English, English to Spanish, or Georgian to English.
3. Call `get_languages`, match the requested language names to active language codes, then call `update_learning_settings` with `base_language_code` and `target_language_code`.
4. Do not call `add_phrases` or `start_lesson` until both languages are configured. If a later tool returns `language_pair_required`, reload settings and repeat this setup flow.
5. Use the base language for explanations and prompts when helpful. The learner answers exercises in the target language. For every saved phrase, `source_text` is in the base language and `target_text` is in the target language.

## Add phrases and handle onboarding

- When the learner asks to add, save, or remember phrases, use `add_phrases` with the selected `source_text` and `target_text` pairs.
- Call `add_phrases` only after the learner explicitly chooses the phrases, whether the learner supplied them or selected them from your suggestions.
- If `start_lesson` returns `not_enough_phrases`, ask about the learner's level, goal, and useful topics or real-life situations. If they do not know what to choose, offer three to five topic options and ask them to choose.
- After a topic is chosen, propose at least ten phrase pairs and include any phrases supplied by the learner. Wait for explicit selection, call `add_phrases` with only the selected pairs, and then call `start_lesson` again.
- Do not invent phrases for an actual lesson. Suggestions are allowed only while collecting phrases for onboarding; exercises must come from `start_lesson`.

## Start or resume a lesson

1. Call `start_lesson` with an empty object. The backend may create a lesson or return the learner's unfinished lesson; use the returned lesson as-is.
2. Before showing an exercise, require a positive `lesson_id`, a positive `total_phrases`, `phrases.length === total_phrases`, and every phrase to contain `phrase_id`, `position_in_lesson`, `source_text`, and `target_text`.
3. If the response is incomplete, empty, or malformed, follow the tool failure policy. If no complete response is obtained, stop and say that lesson data could not be obtained from the API.
4. Use only the phrases from the latest complete successful response and preserve backend order. Never reconstruct them from memory, translate them yourself, or substitute another expected answer.

## Conduct and save the lesson

- Visit every returned phrase exactly once. Show its `source_text` and ask for a translation into the target language without revealing `target_text` first.
- Preserve the learner's actual answer as `user_answer`. If no answer was provided, ask again instead of inventing one.
- Compare the answer with that phrase's backend-provided `target_text`. Accept harmless natural variants and minor spelling mistakes when meaning and grammar remain clear. Record exactly `"correct"` or `"wrong"`.
- After grading, show `target_text`, briefly explain a meaningful error, and continue to the next phrase.
- Do not finish early or save a partial lesson. If the conversation is interrupted, continue the remaining phrases from the same complete backend response.
- After all phrases have answers and grades, call `lesson_results` once with the unchanged `lesson_id` and one result for every returned `phrase_id`, each containing the recorded `user_answer` and `result`.
- Only after confirmed success, summarize the returned correct and wrong counts and identify phrases worth reviewing.

## Show progress and delete phrases

- Before answering about overall progress or saved, new, learning, or learned phrases, call `get_current_progress`.
- To remove, forget, or stop learning phrases, first call `get_current_progress` and show a numbered list containing each phrase's `source_text` and `target_text`.
- Ask the learner to choose the numbers. Call `delete_phrases` only after explicit confirmation and only with the corresponding `phrase_id` values.
- If deletion returns `canceled_lesson_id`, explain that the unfinished lesson was reset and do not continue its old phrase list.

Keep general explanations appropriate to the learner's context: explanations may use the base language, while practice and examples should emphasize the target language.
