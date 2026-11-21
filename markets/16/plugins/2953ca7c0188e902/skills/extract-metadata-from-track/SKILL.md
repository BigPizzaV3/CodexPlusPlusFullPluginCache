---
name: extract-metadata-from-track
description: "Produce a normalized metadata sheet for a track and a missing-field report: title, version, artists, credits, ISRC, writers, genre, BPM, key, language, explicit flag, and lyrics status, ready for distribution and registration. Use when the user asks for track metadata, 'what metadata do I need', 'fix my metadata', or before delivery to a distributor."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Release
  group: "Catalogue"
  display_name: "Metadata Extractor"
  website: https://www.artispreneur.com
---

# Metadata Extractor

> Clean, complete metadata for every track in your catalog.
> *Release desk · Catalogue · about 15 minutes*

## When to use

- Preparing a release for a distributor.
- Registering songs or pitching to sync.
- Metadata is inconsistent across platforms.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Track title, version, and primary and featured artists.
- Writers, producers, and other credits with roles.
- Any file tags or analysis available (BPM, key, duration).
- Genre, language, and explicit status.
- IDs: ISRC, UPC, ISWC.

## Workflow

1. Collect what the artist knows and any file tag data they paste or attach.
2. If the environment can analyze audio, use it only for objective fields (duration, and tempo and key as estimates). Otherwise ask the artist; free tools such as Audacity or a DJ app can read BPM and key.
3. Normalize: consistent capitalization, one spelling per name, feature credits in the standard form, and version in the title field only when it is a distinct version.
4. Fill the metadata sheet.
5. Produce the missing-field report: required fields still blank, with who can supply each (artist, distributor, PRO).
6. Check consistency with the catalog and the registrations.

## Deliverables

- Normalized metadata sheet per track.
- Missing-field report.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Names are identical across title, credits, and registrations.
- [ ] Required distributor fields are all filled or listed as missing.
- [ ] Estimated BPM or key are labeled estimates.
- [ ] No codes were invented.

## Guardrails

- Never fabricate ISRC, UPC, ISWC, or credits.
- Treat audio-derived BPM and key as estimates.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `upload-track-to-catalogue`: store the sheet in the catalog
- `distribution-readiness`: deliver to a distributor
- `transcribe-lyrics`: add lyrics

## Start with

> Build the metadata sheet for this track and tell me what's missing.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
