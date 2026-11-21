---
name: transcribe-lyrics
description: "Format the artist's own lyrics into clean, sectioned text and (when timings are provided) a timed LRC or SRT file, with explicit and clean flags, ready for streaming lyric services, lyric videos, and liner notes. Use when the user asks to 'format my lyrics', 'lyrics for Spotify or Apple Music', 'make an SRT or LRC file', or 'clean up my lyric sheet'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Content
  group: "Catalogue"
  display_name: "Lyric Transcriber"
  website: https://www.artispreneur.com
---

# Lyric Transcriber

> Clean, formatted lyrics ready for DSPs, videos, and liner notes.
> *Content desk · Catalogue · about 15 minutes*

## When to use

- The artist needs lyrics in a platform-ready format.
- A lyric video or captions need timing.
- Lyrics exist as scattered notes or a rough transcript.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- The lyrics text (pasted), or confirmation that the artist will paste the transcript.
- Section names if known (verse, chorus, bridge).
- Explicit content flag and whether a clean version exists.
- Timing source if a timed file is wanted (timestamps, or a tool that can produce them).
- Credit line and copyright line.

## Workflow

1. Confirm the lyrics are the artist's own or licensed for this use.
2. Clean the text: one idea per line, consistent punctuation, correct spelling of names, and repeated lines written out.
3. Label sections (`[Verse 1]`, `[Chorus]`, `[Bridge]`).
4. Mark explicit words according to the platform's rules and prepare a clean version if requested.
5. If timestamps are provided, produce `.lrc` or `.srt`. If audio is attached and the environment has transcription tools, transcribe and have the artist correct it. Otherwise ask the artist to paste the lyrics; do not guess at words.
6. Add the credit and copyright line.
7. Check against platform lyric guidelines; the artist confirms the submission route with their distributor or lyric service.

## Deliverables

- Clean sectioned lyrics (`lyrics.md`).
- Explicit and clean flags.
- Timed `.lrc` or `.srt` when timings exist.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Every line matches what is sung; mishearings are flagged `[CONFIRM]`.
- [ ] Section labels and line breaks follow one style.
- [ ] Timing format is valid (monotonic timestamps).
- [ ] Credit and copyright line present.

## Guardrails

- Only handle lyrics the artist wrote or has permission to use. Never reproduce another artist's copyrighted lyrics.
- Do not guess at unclear words.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-lyric-video`: use timed lyrics for the video
- `extract-metadata-from-track`: store lyrics status in the catalog
- `upload-track-to-catalogue`: link the file

## Start with

> Format my lyrics for streaming platforms. Here they are.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
