---
name: compare-explainers
description: Guide a comparison of two YouTube explanations of the same topic using a shared viewing checklist and the user's reported takeaways. Use when the user asks to compare explainers, teaching approaches, examples, or understanding across videos. Keep metadata-based selection separate from content comparison. Do not use for automatic video summaries, unsupported claims about a video's viewpoint, or a simple single-video recommendation.
---

# Compare Explainers

## Inputs

Establish the topic, the user's starting level, and what they want the comparison
to resolve. Reuse supplied links or an existing selection. Default to two videos;
include a third only when requested or needed to address a specific remaining gap.

## Workflow

1. Define a common comparison question and a short checklist: the main idea,
   examples used, assumptions or prerequisites, and what remains unclear.
   Adapt these dimensions to the user's goal.
2. Discover missing candidates with `search-videos({ query, reason? })` and read
   `results`. Select videos covering the same question, preferably with different
   formats suggested by their titles or descriptions. Deduplicate IDs and explain
   the apparent differences without asserting that the actual content differs.
   If results are unsuitable, refine the query once or ask for another link.
3. Provide each selected title, channel, returned `watchUrl`, and metadata-based
   reason for inclusion. Call `display-video({ videoId, reason? })` for the first
   selection when viewing is wanted. Extract IDs from supplied YouTube URLs.
   Accept only `status: ready` with a video; handle `invalid_video_id`,
   `video_not_found`, or a tool error by explaining the issue and offering a
   returned alternative. Do not render every candidate as a browsing gallery.
4. Invite the user to share takeaways against the checklist after each video.
   Open the next selection individually when requested. Wait for the user's
   account instead of assuming playback, understanding, or specific claims.
5. Build a comparison matrix from the supplied takeaways or pasted excerpts.
   Attribute each observation to its source, mark missing dimensions unknown,
   and distinguish a shared idea from a difference in presentation or a reported
   disagreement. Ask for the relevant excerpt before interpreting an ambiguous
   disagreement.
6. Recommend which explanation appears more useful for this user's goal based
   on their reported experience. List any unresolved question and one focused
   next step; do not manufacture a winner when the evidence is incomplete.

## Deliverable

Return a two-video selection and shared viewing checklist, followed by a
comparison matrix and a goal-specific recommendation once the user provides
content. Keep selection evidence and user-reported content clearly attributed.

## Boundaries

- Do not require annotations, access private widget state, or claim to watch or
  transcribe either video. A title-only discussion handoff supplies no takeaways.
- Do not treat channel variety, popularity, or a title as proof of accuracy,
  opposing viewpoints, independent sources, or teaching quality.
- Leave reported factual disagreements unresolved unless supporting evidence
  is available. Distinguish comparing explanations from verifying their claims.
- Use only the registered tool arguments. Keep the matrix in chat; do not
  promise synchronized players, automatic seeking, or a saved comparison board.
- If the user explicitly requests text only or no video display, call neither
  tool and compare only the material already provided.
