---
name: youtube-learning-path
description: Build an ordered YouTube learning path for a topic, starting level, and practical goal. Use when the user asks for a sequence of videos, a beginner progression, or a small video curriculum. Select and sequence videos using returned metadata, and adjust the path using the learner's feedback. Do not use for a single-video lookup, automatic video summaries, or timestamped coaching.
---

# YouTube Learning Path

## Inputs

Establish the topic, starting knowledge, and desired outcome from the conversation.
Use any stated language, preferred format, video count, or time budget. Ask one
focused question only when a missing goal or level would change the sequence.
Default to three stages when the user gives no preferred length.

## Workflow

1. Translate the goal into a short progression: foundations, a worked example,
   and independent application. Adapt these stages to the topic and learner.
2. Call `search-videos` with `{ query, reason? }` for stages needing discovery.
   Reuse supplied videos and known IDs instead of searching for them again.
   Read candidates from the returned `results`; compare titles, descriptions,
   channels, and publication dates against each stage's objective.
3. Select one candidate per stage, remove duplicate IDs, and explain its apparent
   fit using metadata. Describe the planned learning objective separately from
   any coverage explicitly supported by the description. Refine an empty or
   unsuitable search once; leave a stage unfilled if no defensible match appears.
4. Return the ordered path with each selected title, channel, returned `watchUrl`,
   stage objective, and reason for its position. Mark any inferred level or
   coverage as tentative. Add one short question to guide watching at each stage.
5. Call `display-video` with `{ videoId, reason? }` for the first selected video
   when the user wants to watch. Extract an ID from a supplied YouTube URL rather
   than passing the URL as `videoId`. Treat only `status: ready` with a video as
   loaded; explain `invalid_video_id`, `video_not_found`, or a tool error plainly
   and offer another returned candidate without claiming playback succeeded.
6. On the learner's next message, use their reported understanding or difficulty
   to revise the next stage. Open subsequent videos individually when requested;
   do not assume a video has finished or advance the sequence automatically.

## Deliverable

Provide a compact numbered learning path and the requested playable selection.
Keep revisions in the conversation, and explain how each revision serves the
learner's stated goal.

## Boundaries

- Work with ordinary playback and chat; do not require observations or tags.
- Do not claim to have watched videos, obtained transcripts, or verified that
  the videos teach every planned objective. Use user-supplied takeaways or text
  for content-specific follow-up.
- Read a verified duration only from a ready `display-video` result's
  `video.contentDetails.duration`. Mark other lengths unknown; do not promise
  that the full path fits a time budget using search metadata alone.
- Do not create a YouTube playlist, autoplay queue, persistent progress record,
  or reminder. The path is a list in chat, and displaying a video renders a widget.
- Use only the registered arguments; express search preferences in `query`
  without claiming they are enforced filters. If the user explicitly requests
  text only or no video display, call neither tool and organize supplied material.
