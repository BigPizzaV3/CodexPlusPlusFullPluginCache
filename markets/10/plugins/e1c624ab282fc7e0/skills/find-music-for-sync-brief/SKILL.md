---
name: find-music-for-sync-brief
description: Find music in the PICA public directory for a sync brief — translate a mood/vibe/scene description into audio search parameters, run the search, and return a rights-aware shortlist with credit details for licensing.
triggers:
  - find music for a sync brief
  - find me a track for a film scene
  - music for this brief
  - find an uplifting indie folk track
  - I need music that sounds like
audience: sync supervisor / music library / ad agency / film & TV music team
tools_required:
  - directory_search_recordings
  - directory_lookup_work
  - directory_lookup_person
output: A rights-aware shortlist — each result with title, artist, audio characteristics (BPM, key, energy), credits summary for licensing contact, and any flags (unattested credits, low registration score, missing ISRC).
---

_Copyright (c) 2025-2026 Withpica Ltd. All rights reserved._

# find-music-for-sync-brief

Help the user find music in PICA's public directory for a sync brief. Translate their description (mood, vibe, scene, era, vocal style) into search parameters, run the search, and return a shortlist that includes the information they need to license — not just the track.

This is a public skill — any AI agent connected to the directory MCP can use it. The directory only contains songs listed by their owner or a confirmed writer.

## Step 1 — Translate the brief

Most sync briefs are described in natural language. Translate before searching:

| User says | Search parameters |
|---|---|
| upbeat / uplifting / driving | `min_energy: 0.6`, `min_danceability: 0.5` |
| dark / moody / brooding | `max_energy: 0.4`, `key_mode: minor` |
| chill / ambient / background | `max_energy: 0.4`, `max_bpm: 100` |
| epic / cinematic | `min_energy: 0.7`, often longer durations |
| specific BPM ("around 120bpm") | `min_bpm: 115`, `max_bpm: 125` |
| acoustic / sparse | typically lower `danceability` and `energy` |
| vocal / instrumental | filter on `has_vocals` if available |

If the user gives an artist or song reference ("something like X"), look up that reference first via `directory_lookup_work` or `directory_search_recordings` by title — then mimic its audio profile in the new search.

## Step 2 — Search

Call `directory_search_recordings` with the parameters from step 1. Default limit is fine for an initial scan.

If the brief is vague, do two searches with slightly different parameters and compare. If too many results, narrow on BPM or key. If too few, widen the BPM range first, then drop key_mode.

## Step 3 — Lookup full details

For the top 5-10 promising results, call `directory_lookup_work` to get:

- **Who wrote it** — credits with IPI numbers (essential for the licensing contact path)
- **Whether credits are attested** — an unattested credit means the ownership claim hasn't been verified; flag this
- **DSP links** (Spotify, Apple Music) — the user wants to listen before shortlisting
- **Registration score** — higher score = cleaner rights chain = easier to license

For high-value matches where the user wants to know more about the creator, call `directory_lookup_person` with the IPI (or the credit's `global_creator_id`) to see how many of the writer's songs are listed and who they work with on them; `directory_list_works` with their name lists the songs themselves.

## Step 4 — Present the shortlist

Present each shortlisted track with:

- **Title, artist** — what the user listens for
- **Audio profile** — BPM, key, energy (one line, the supervisor's quick filter)
- **Credits summary** — writers with IPI, publisher if known (this is the licensing path)
- **DSP links** — so the user can listen
- **Flags** — unattested credits, low registration score, missing ISRC, multiple writers (= multi-party clearance needed)

If a track has all green flags (attested credits, high registration score, ISRC present, single or low-count writers), call it out as "clean to clear."

## Step 5 — If no results

If the search returns nothing, walk the user back through the brief:
- Widen the BPM range first (most supervisors don't actually mind ±10 BPM)
- Drop the key filter (key matching matters less than mood for most placements)
- Drop the energy bounds and search by genre/mood text only
- Suggest the user expand to adjacent moods ("uplifting" → also try "warm" or "hopeful")

Be honest if the directory is small for a specific style — PICA's directory grows as songs are listed; some niches are sparse.

An empty search comes back with a short note and a link for sharing PICA with the creators. Pass it on once in the conversation, in your own words. If the user knows who makes the music they're after, that link is how it ends up in the directory.

## What not to do

- Don't claim to license tracks — this skill returns a shortlist, not a license. When the user wants to approach an owner, offer `directory_send_licensing_enquiry`, and send it only once they say yes and give their own name, email and project description. Never invent those details.
- Don't speculate about pricing — sync fees are negotiated per-placement
- Don't return results from outside the directory (no general web search, no Spotify metadata directly) — the directory is the source of truth for this skill
- Don't return tracks with no attested credits without flagging them as "rights chain unverified"

## Follow-on skills

- `due-diligence-on-creator` (Stage 2 candidate) — for deeper research on a specific writer before reaching out
