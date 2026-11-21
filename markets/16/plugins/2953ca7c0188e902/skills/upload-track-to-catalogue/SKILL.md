---
name: upload-track-to-catalogue
description: "Log each track once in a master catalog sheet with credits, splits, IDs, ownership, registration status, and file locations, so every other task reuses the same data. Use when the user asks to organize their catalog, 'create a song database', 'log my tracks', or before registrations, pitching, or distribution."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Release
  group: "Catalogue"
  display_name: "Catalog Upload"
  website: https://www.artispreneur.com
---

# Catalog Upload

> Every track logged once, reused by every other tool.
> *Release desk · Catalogue · about 15 minutes*

## When to use

- The artist has unlabelled or scattered songs and files.
- Starting registrations, sync pitching, or distribution.
- A new track is finished.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Track title and version (original, radio edit, instrumental, remix).
- Artists, writers, producers, and splits.
- IDs known so far: ISRC, ISWC, UPC.
- Ownership of composition and master.
- File locations and registration status.

## Workflow

1. Create or open `catalog.csv` using the columns below. One row per track version.
2. Fill the row from artist input. Unknown values stay blank, not guessed.
3. Check for duplicates (same title and version) and for missing ownership or split data.
4. Link the signed split sheet and the lyrics file.
5. Update registration status per route (PRO, MLC, SoundExchange, copyright).
6. Report completeness per track and list what blocks each next step.

## Deliverables

- `catalog.csv` with one row per track version.
- Completeness report per track.
- Blocked-steps list.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Columns: track_id, title, version, primary_artist, featured_artists, writers_and_shares, producers, composition_owner, master_owner, publisher, ISRC, ISWC, UPC, release_date, label_or_distributor, duration, BPM, key, genre, language, explicit, lyrics_file, split_sheet_file, audio_file, artwork_file, sample_clearance, PRO_status, MLC_status, SoundExchange_status, copyright_status, notes

## Quality checks (run before handing over)

- [ ] No duplicate rows.
- [ ] Writer shares total 100% where listed.
- [ ] Blank means unknown, and unknown is listed in the report.
- [ ] Every row has a file location.

## Guardrails

- Do not invent ISRC, ISWC, or UPC codes. They come from the distributor or the PRO.
- No financial account numbers in the sheet.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `extract-metadata-from-track`: complete the technical fields
- `register-tracks-with-pro`: register what is ready
- `license-music`: use the catalog for sync briefs

## Start with

> Create my master catalog sheet. I'll add my tracks and what I know about each.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
