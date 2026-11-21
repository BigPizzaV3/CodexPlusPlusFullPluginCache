---
name: watch-and-apply
description: Turn one YouTube tutorial into a practical learning cycle with a viewing goal, a user-reported takeaway, a small exercise, and feedback on the user's attempt. Use when the user wants to practise or apply something learned from a video. Ground video-specific work in text or takeaways shared in chat. Do not use for an ordered curriculum, automatic video analysis, or observation-panel coaching.
---

# Watch and Apply

## Inputs

Establish the skill the user wants to practise and what a successful small result
would look like. Reuse the current video or a supplied link when available.
Account for the user's starting level, available materials, and time for practice.
Ask a focused question only if these details materially affect the exercise.

## Workflow

1. Define one achievable learning goal. If discovery is needed, call
   `search-videos` with `{ query, reason? }`, read its `results`, and choose a
   tutorial whose title and description plausibly support that goal. Explain
   the metadata basis without claiming the tutorial's method has been verified.
   Refine an unsuitable search once before asking for a link or narrower goal.
2. Call `display-video` with `{ videoId, reason? }` for the selected or supplied
   video. Extract the ID from a YouTube link when needed. Continue the viewing
   step only for `status: ready` with a video. For `invalid_video_id`,
   `video_not_found`, or a tool error, explain the issue and offer another returned
   candidate or work from material the user provides.
3. Give a short viewing brief: the goal and two things to pay attention to.
   Frame these as questions for the learner, not claims about scenes or steps
   that the model has seen. Invite the user to return with their main takeaway,
   one unclear point, or the method they want to try. End the response here.
4. Resume when the user supplies that input. Separate their account of the video
   from general subject knowledge. Ask for a missing step or pasted excerpt if
   reproducing the specific method would otherwise require guessing.
5. Design one small exercise using the reported method and the user's constraints.
   State the task, a concrete completion criterion, and what result the user can
   share for feedback. Label any exercise devised from general knowledge as an
   assistant-proposed exercise rather than something taken from the video.
6. Review the user's attempt against the stated criterion. Explain one useful
   correction and offer one retry or extension. Base feedback only on the work
   they share; do not claim to observe their practice or the video's demonstration.

## Deliverable

Provide a viewing brief, then a practical exercise, then focused feedback as the
user supplies the needed information. Preserve the learning goal across turns
without inventing takeaways, attempts, or completion.

## Boundaries

- Use ordinary playback and chat. Do not require tagging, observation logs,
  transcripts, private widget state, or a playback-completion signal.
- Do not watch, pause, seek, or advance the player on the user's behalf. A
  displayed video is not evidence that the user watched or understood it.
- Treat the discussion button as a title-only handoff; ask for the user's
  takeaway when it provides no account of the content.
- Use only the registered tool arguments; do not add exercise, duration, or
  playback parameters. Keep the exercise in chat, without promising saved progress.
- If the user explicitly requests text only or no video display, call neither
  tool and build the practice cycle from the information they supply.
