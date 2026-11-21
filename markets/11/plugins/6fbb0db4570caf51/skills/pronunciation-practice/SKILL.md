---
name: pronunciation-practice
description: Try Contexta with one standalone Speaking answer and real feedback, or start short read-aloud, free-speaking or saved-phrase audio practice. Use for Try the plugin and explicit speaking/pronunciation practice; typed or voice-dictated chat alone is not audio assessment.
---

# Short pronunciation practice

Keep the reply focused on the learner’s result and next action. Do not show phrase, task, operation or request IDs, raw status fields, or tool/rendering diagnostics. Use titles and returned website links. Do not announce that a native widget was rendered or reopened; the widget already presents the result.

Native Contexta UI is required when available: use the actual task widget returned by the start/resume tool as specified in the shared workflow. Text does not replace the recorder; a blocked host uses the honest website fallback.

Give the learner one bounded speaking task and real feedback. Read and apply [the shared workflow](../../references/workflow.md) before replying or calling the service.

## Primary Try Contexta action

For “try Contexta,” “try the plugin,” “try a short answer” or a demo request with
no material, call `start_quick_exercise(mode="speaking", purpose="intro_speaking", idempotency_key=...)`.
This explicit request starts or resumes one saved standalone Speaking exercise.
Its question and Record control appear directly in the returned native widget.
Do not create a project, request a résumé or passage, show a mode picker, or send
the learner through project planning. The service uses the saved profile level
or its disclosed default; never infer proficiency from this chat.

For “continue my Speaking demo,” use
`show_practice_widget(entry="speaking_demo")` to reopen the same ready attempt,
pending analysis or saved feedback. On an expired unused introduction, an
explicit restart uses the same introductory purpose. Never substitute a general
quick sample or lose the previous accepted recording.

Recording requires the learner to choose **Record answer** and then **Get feedback**.
The returned introductory component is the complete learner-facing answer in
ready, processing, feedback and retry states. Do not add recorder steps or a
second question, summary, feedback suggestion or website link below it.
If the host microphone is blocked, use the same-task website recovery to record from the microphone. Audio-file selection is not available. Never record or assess audio automatically.
If the component is unavailable or fails to display, give a concise fallback
with the actual returned question, actual controls and exact returned website
URL for that same standalone exercise; it is not a text/session page or catalog.
For an explicitly named existing project, use the owned project continuation.
An ordinary standalone sample with a specifically chosen mode keeps the normal
`start_quick_exercise` call without the introductory purpose.

## Reply at each stage

The standalone Speaking introduction follows the complete-component rule above; no additional recorder sentence is needed. For other prepared or resumed recordings, any accompanying reply is one short action sentence, for example: “Press **Record answer**, say ‘the intended benefit’, then **Get feedback**.” Substitute only the actual returned phrase or task instruction. The recording component already carries the task, status and controls; do not append a receipt, identifier, status list or a sentence about opening the component.

For those other exercises, processing text says only that the submitted recording is being assessed. Saved-feedback text gives one useful suggestion supported by that assessment; its scores are already in the component. Retry text points to one actual correction and the recording action. When the component itself is unavailable, use its returned website link with the real limitation.


Choose only the requested mode:

- Practise phrase: `mode="reading", practice_target="phrase"`; the exact saved expression, assessed with sound and letter colors.
- Read aloud: `mode="reading"`; a short exact reference sentence or saved context.
- Speak in your own words: `mode="speaking"`; a brief spoken response to the actual returned situation.

For a saved phrase, use its actual `word_id` with `start_phrase_practice`. For context reading pass `practice_target="context"` (the compatible default). If the learner names an unidentified phrase, retrieve a card with `get_phrase_review_card(phrase_text=...)`. Never search today/due/random cards for a named expression, guess IDs, silently save it, or substitute another phrase. Explain a missing result and let the learner choose the next step. Resume a matching returned `ready_practice_tasks` ID using `show_practice_widget` rather than creating another task. For a general short sample use `start_quick_exercise`. Reuse stable idempotency keys after an uncertain start. `show_practice_widget` can prepare the minimal connector when the learner asks to open Contexta but has not chosen a task. If unused practice has expired, retrieve a fresh phrase card or sample; do not submit audio into the expired task.

Present the actual returned task and its reference audio when available. A request to practice does not authorize an automatic audio upload. The widget requests microphone permission only on a click. Microphone recordings stay local until the learner chooses **Get feedback**. When the host microphone is blocked, the exact returned website link continues that same task for microphone recording. Do not invent a separate picker, automatically select or send a file, or claim an in-chat microphone works because an API is present.

Accepted audio is limited to 60 seconds and 512 KiB. The server validates encoding and duration. Do not convert a typed answer or voice-dictated chat transcript into invented audio, phoneme scores or a saved assessment.

After explicit submission use the owned task and `submit_exercise` audio parameters, then bounded `get_exercise_feedback` polling. Processing means the recording was accepted, not that assessment has finished. On failure show the actual safe error/recovery option; do not generate a substitute score. Reuse the same task/submission identity when the outcome is uncertain.

Explain available actual scores, colored assessed words and specific corrections. Recognition-uncertain and missing-score words remain neutral/unscored, never zero. Keep genuine zero scores distinct. Use the actual pronunciation evidence and supplied wording suggestions; do not invent an overall metric, CEFR level, certified ability or an improvement trend from one attempt.

On requested retry use `retry_exercise` with the original task and a stable key. Briefly point to one useful change grounded in the returned feedback. Full website sessions, listening/comprehension quizzes and long writing are not reproduced in this widget.
