---
name: video-discussion-club
description: Organize a group discussion around a YouTube video with an audience-aware selection, facilitator agenda, open questions, and a synthesis of participant responses shared in chat. Use for a video club, classroom discussion, team viewing session, or moderated group conversation. Do not use for automatic video summaries, participant messaging, meeting scheduling, or a solo tutorial exercise.
---

# Video Discussion Club

## Inputs

Establish the topic, audience, discussion purpose, and available discussion time.
Reuse a supplied video or previous selection. Ask one focused question if the
audience or purpose is unclear enough to change the selection or agenda.
Distinguish time for watching from time for discussion.

## Workflow

1. Turn the purpose into one central discussion question. If a video is needed,
   call `search-videos` with `{ query, reason? }`, read `results`, and shortlist
   two or three candidates using titles, descriptions, channels, and publication
   dates. Explain their apparent fit and recommend one. Refine an unsuitable
   search once; ask for a link if a suitable selection remains unavailable.
2. Call `display-video` with `{ videoId, reason? }` for the chosen video when
   viewing is wanted. Extract an ID from a supplied YouTube URL. Use only a
   `status: ready` result with a video as the loaded selection. Explain
   `invalid_video_id`, `video_not_found`, or a tool error and offer an alternative
   from actual results rather than presenting an unavailable video as playable.
3. Provide a facilitator agenda: a brief opening question, individual viewing,
   an initial round of reactions, focused discussion, and a closing takeaway.
   Allocate discussion time separately. Include video runtime only when returned
   in `video.contentDetails.duration`; leave unverified watch time unknown.
4. Prepare three to five open questions grounded in the topic and the stated
   purpose. Frame video-specific points as things for participants to identify,
   rather than scenes or claims the model has inspected. Include a prompt for
   participants to distinguish what they saw from how they interpreted it.
5. Invite the facilitator to share participant responses in chat. End the
   preparation response with the agenda; do not invent a discussion or assume
   participants have watched. During facilitation, ask one question at a time
   and adapt to the responses actually provided.
6. Synthesize the shared responses into areas of agreement, differing
   interpretations, open questions, and one closing takeaway. Preserve meaningful
   disagreement and attribute contributions only as the facilitator identifies
   them; do not infer attendance or individual opinions.

## Deliverable

Provide the selected video, a timed discussion agenda, and facilitator questions.
After responses arrive, provide a concise discussion recap grounded in those
responses, with unresolved points left open.

## Boundaries

- Use ordinary viewing and chat; do not require observations, transcripts,
  private widget state, or automatic playback tracking.
- Treat the discussion button as a title-only handoff. Request participant
  responses before producing a content-specific recap.
- Do not claim metadata verifies the full content, suitability for the audience,
  caption availability, or factual accuracy. Identify uncertain fit plainly.
- Keep coordination in chat. Do not send invitations, schedule meetings, control
  shared playback, or claim persistent attendance or discussion storage.
- Use only the registered tool arguments. If the user explicitly requests text
  only or no video display, call neither tool and prepare from supplied material.
