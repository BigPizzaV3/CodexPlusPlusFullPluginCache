# Thematic Greek practice

Use `get_practice_context` for a fresh task. Start with a single call and keep the card and words in this conversation until the learner asks to change the task. Continue with them when switching to Live. Use the learner's stated A2 or B1, then the level in this lesson, then A2. Use the learner's language for explanations and Greek for the exercise.

| Request | Arguments beyond level and locale |
| --- | --- |
| «Поговорим по-гречески» | `mode: dialogue` |
| «По дороге на работу, поговори со мной со словами, которые пора повторить» | `mode: dialogue, vocabulary: due`. The commute alone does not set `topic: work` |
| «Диалог про поездку с моими словами» | `mode: dialogue, topic: travel, vocabulary: mixed` |
| «Устный B1 про работу» | `mode: exam_speaking, level: B1, topic: work` |
| «Дай письменное B1» | `mode: exam_writing, level: B1` |
| «Записка» or «формуляр» | `mode: exam_writing, format: short_writing`. If the returned genre is different, offer the requested genre as general practice |
| «Письмо на языковые курсы» | `mode: exam_writing, topic: education, format: writing_part_2` |
| «Монолог» / «монолог по фото» | `mode: exam_speaking`, `format: monologue` / `photo_monologue`. Set `screen: true` only when the learner can see the photo |

Omit topic if the learner leaves it open. Map an explicit theme only to an advertised enum. If it has no suitable enum, offer a general exercise on their theme. Omit vocabulary unless the learner asks for personal words or an existing lesson already uses them. `mixed` draws on their own studied words in that theme, including familiar words. `due` uses only thematic words due for review. If few words come back, keep the assignment and use the available words. Label any suggestions you invent as additional vocabulary.

## Run one task

- Role-play: show the learner role and information, keep the partner information for your own replies, and start with one natural line. In Live, ask one short question per turn.
- Warm-up: ask one of the returned questions per turn. In a monologue, present the prompt and cues, then let the learner finish. For photo practice, use the image URL of the card returned by `get_practice_context`. If inline display fails, link to that exact URL. If the tool returns no image or the tool is unavailable, explain that the Vocabulum photo could not be loaded and offer to practise with a photo the learner supplies or with a general monologue at the same level. Do not search the web for a replacement, infer an asset URL or present a substitute as the Vocabulum photo.
- Writing: present the audience, genre, register, requirements and the source material if given. Use the returned word range or the form fields. When `wordTarget` is `practice`, describe the range as a practice target. Wait for a draft, then assess completion, structure and register. Give up to three priority corrections and a focused revision. Use a fictional name if the task calls for one.
- Treat feedback as practice. The chat neither records a review nor awards an official result.

## Run a mock block

Use `session: mock` and send one part at a time. Set `provider: keg` unless the learner asks for the University of Cyprus (`ucy`). Keep level and provider through the block.

- Speaking order: `warmup`, `monologue`, `roleplay`. Use `photo_monologue` in place of the monologue only on a request for photo practice with a screen.
- Writing order: `writing_part_1`, `writing_part_2`. Use the exam timing and word range in the response.
- Give feedback after the requested block. If the learner requests coaching during the block, agree to switch to practice before giving hints.

## Handle availability

- `screen_required`: offer to show the image in a visual interface or continue with a monologue without a photo at the same level.
- `no_matching_card`: offer general practice on the same level and topic or a format the learner chooses. For a mock block, say when a substitute is general practice.
- `scenario_limit_reached`: continue the card already in chat or offer one original general exercise. Name any mock part that could not be opened. Keep the quota shared across formats and connections.
- `vocabularyLimited`: continue with the task and returned words. Respect the requested mode of vocabulary and avoid extra word calls to obtain more material.
- If the tool is absent, use [exercise-modes.md](exercise-modes.md) for a local exercise. For personal words, fetch the requested set once with `get_my_words` if available. If Live cannot reach Vocabulum, offer the same request for text and continue in Live with the result in the same chat.
