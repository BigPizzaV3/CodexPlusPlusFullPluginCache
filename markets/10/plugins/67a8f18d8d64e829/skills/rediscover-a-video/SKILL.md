---
name: rediscover-a-video
description: Find a vaguely remembered YouTube video by reconstructing clues, refining searches, comparing returned metadata, and asking the user to confirm a candidate. Use when the title, channel, or link is forgotten or uncertain. Keep possible matches tentative until confirmed. Do not use for generic recommendations, an exact-ID display request, watch-history access, or guaranteed identification from an unseen scene.
---

# Rediscover a Video

## Inputs

Collect clues already present in the conversation: subject, remembered title
words, creator, language, approximate period, and distinctive details. Separate
confident clues from uncertain memories. Ask at most one high-value question
before searching when a missing clue would meaningfully narrow the results.
Clarify whether a remembered date means upload date or when the user watched.

## Workflow

1. If an exact ID or usable YouTube URL is supplied, extract the ID and skip
   discovery. Otherwise, summarize the strongest clues briefly and form a query
   combining the topic with distinctive title words or a creator clue.
2. Call `search-videos` with `{ query, reason? }` and read `results`. Compare
   returned titles, descriptions, channels, and publication dates with the clues.
   Treat a remembered scene as a search hint, not as something confirmed by the
   metadata. Do not assume upload date equals the user's viewing date.
3. Present at most three plausible candidates with their titles, channels,
   returned `watchUrl` values, supported matches, and unresolved or conflicting
   clues. Mark the candidates tentative. Do not claim an exact match from
   search rank or similarity alone.
4. Ask which candidate looks familiar or request one discriminating clue. Use
   the reply to refine the next query: keep strong clues, relax an uncertain
   one, and avoid repeating the same failed search. Deduplicate IDs across rounds.
   Limit discovery to three rounds before offering the best remaining shortlist
   and the specific missing clue that would help continue.
5. Call `display-video` with `{ videoId, reason? }` for a candidate the user
   chooses, an unambiguous metadata match offered for verification, or a supplied
   exact ID when viewing is wanted. Do not display every tentative candidate.
   Accept only `status: ready` with a video. Explain `invalid_video_id`,
   `video_not_found`, or a tool error; offer another actual candidate or request
   a corrected link without declaring the search resolved.
6. Invite the user to verify by watching. Mark the video confirmed only after
   they explicitly recognize it. If rejected, record the useful exclusion in
   the conversation and continue within the search limit or with a new clue.

## Deliverable

Provide either a user-confirmed video with its title, channel, and watch link,
or a clearly tentative shortlist with matched clues, conflicts, and the most
useful next question. State honestly when no plausible match was found.

## Boundaries

- Do not access or claim access to YouTube accounts, viewing history, saved
  playlists, private widget state, or playback events.
- Do not rely on tagging, transcripts, or automatic scene recognition. Use the
  user's remembered details as clues without inventing corroborating content.
- Do not claim an absent result proves deletion or that all of YouTube has been
  searched. A limited search cannot establish either conclusion.
- Use only the registered tool arguments; channel and date words in `query`
  are search hints, not enforced filters. Keep clue tracking in the conversation.
- If the user explicitly requests text only or no video display, call neither
  tool; help reconstruct clues from their supplied material instead.
