---
name: eventhex-agenda
description: Speakers and sessions — bulk creation, breaks, sub-sessions, speaker roles, ordering, photos.
---

# Agenda — speakers & sessions

## Speakers

- `create_speakers(eventId, speakers:[{name, designation, company, about, photo}])` — always an array; one item for a single speaker, many for a lineup. Each item is created independently; report per-item results.
- Photos from third-party URLs: pass the URL as `photo` — it is copied onto EventHex CDN and the internal key is saved. `upload_speaker_photo_from_url` does the same for an existing speaker.
- `update_speaker` / `delete_speaker` / `listSpeakers`.
- Ordering: `reorder_speakers(eventId, speakers:[{speakerId, position}])` — lower positions first.
- `generateSpeakerProfile` writes AI bio copy for a speaker.

## Sessions

`create_sessions(eventId, sessions:[{title, start, end, stage, description, …}])` — always an array. Supports:

- Breaks: `isBreak:true`.
- Nested sub-sessions: `isSubSession:true` + `parentSession`.
- Role-aware speakers: `sessionSpeakers:[{speakerId, role, order}]` for roles like Moderator or Keynote Speaker; the plain `speakers` id array is filled automatically for compatibility.

Also: `updateSession`, `deleteSession` (destructive — explicit request only), `listSessions`, `assignSpeakerToSession`, `removeSpeakerFromSession`, `createAgendaBatch` (speakers + sessions in one call), `checkConflicts(eventId)` to catch overlapping times/stages after bulk edits.

## Flow for "here is my full schedule"

1. `create_speakers` with the whole lineup (dedupe against `listSpeakers` first).
2. `create_sessions` with the whole schedule, wiring `sessionSpeakers` by the returned speaker ids.
3. `checkConflicts`, then report per-item successes and any failures.

Session times use the event's timezone.
