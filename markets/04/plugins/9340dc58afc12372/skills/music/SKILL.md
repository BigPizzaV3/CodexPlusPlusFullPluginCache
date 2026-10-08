---
name: music
description: Music, jingles and soundtracks. Use when the user wants audio generated — a track, a background bed, a jingle for an ad. Not for adding captions or subtitles to a video (use Social Studio).
---

# Sound

## Tokens

`/music` `/soundtrack` `/jingle` `/bed`

## Workflow

`generate_music`. The audio widget polls itself — don't call `fetch_music_status`. On a
text-only host, poll it with `sync: true` until `complete` or `error`.

## Ask for the three things that matter

**Genre, mood, and length.** Length matters most — a bed for a 15-second ad and a track
for a three-minute video are different requests.

If they're scoring something they already generated, **match its duration** rather than
asking. Look it up rather than making them tell you.

## Useful defaults

- Scoring an ad → instrumental, no vocals, a clear build in the last third
- Background bed → low-dynamic, nothing that competes with a voiceover
- Jingle → short, hook-forward, memorable in under 10 seconds

## Paywall

Music generation requires a paid organization. Relay subscription refusals verbatim —
they carry the upgrade link.

## Conventions

Never print `org_id`, `folder_id`, or raw asset uuids.

## When something fails

Read `references/errors.md`. Identify the kind of failure before responding: pending jobs
are waited on, technical errors retried at most twice, unsupported capabilities stated
plainly, safety refusals never routed around, and every material change disclosed.

## QA before delivery

Run `references/qa.md` before calling this finished. Inspect the actual output — never
claim quality you have not observed, and say plainly what you could not verify.
