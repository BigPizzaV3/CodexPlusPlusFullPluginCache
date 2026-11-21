---
name: register-tracks-with-pro
description: "Build a registration sheet for each song (titles, writers, roles, splits, writer IDs, publisher, ISRC, release date) and walk the artist through registering with their PRO, The MLC, and SoundExchange, with a tracker for confirmations. Use when the user asks 'register my songs', 'add my songs to my PRO', 'register with the MLC', or has released or is about to release music."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Release
  group: "Publishing & PRO"
  display_name: "Track Registration"
  website: https://www.artispreneur.com
---

# Track Registration

> Register every song so royalties can actually find you.
> *Release desk · Publishing & PRO · about 15 minutes*

## When to use

- A song is finished or released and not yet registered.
- A co-written song has signed splits.
- The artist joined a PRO and now needs to add works.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- For each song: title, alternate titles, and writers with roles and percentages.
- Each writer's PRO and IPI/CAE number (if known) and publisher.
- Release date and ISRC for each recording (from the distributor).
- Whether any part is a sample or interpolation.
- Which registrations are already done.

## Workflow

1. Collect each work's data. If splits are undocumented, send the artist to `create-split-sheet-agreement` first.
2. Verify the writer shares total exactly 100% per song. Stop and resolve any mismatch before registering anything.
3. Complete the registration sheet for each work (template below).
4. Walk the PRO work-registration form field by field. The artist enters and submits it on the PRO's site.
5. The MLC (US streaming mechanicals): register the works and match recordings by ISRC, directly or confirm an administrator is doing it.
6. SoundExchange (digital performance of recordings): register recordings by ISRC as rights owner and, where applicable, as featured artist.
7. Build the tracker: song, date submitted, destination, confirmation or work ID, status, and follow-up date.

## Deliverables

- Registration sheet per song.
- Split and ID verification.
- Walkthrough for the artist's PRO.
- Registration tracker.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

```markdown
# Registration Sheet: [Song title]
Alternate titles:
Writers: [legal name | role | % | PRO | IPI/CAE | publisher]  (total must be 100%)
Recording: [artist | ISRC | release date | label or distributor | master owner]
Sample or interpolation: [none / details]
Registered with: PRO [date, work ID] / The MLC [date] / SoundExchange [date]
```

## Quality checks (run before handing over)

- [ ] Writer shares total exactly 100% for every song.
- [ ] Legal names match what each writer uses at their PRO.
- [ ] Every recording has an ISRC from the distributor.
- [ ] The tracker shows a follow-up date for each pending confirmation.

## Guardrails

- Never register splits that do not total 100%.
- Only register works the artist wrote, co-wrote, or owns.
- Registry data can lag by weeks; record the date checked.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-split-sheet-agreement`: write the splits down first
- `royalty-readiness`: confirm all four routes are set
- `claim-tracks-with-pro`: audit older songs

## Start with

> Help me register my songs. Ask me for each song's title, writers, and splits.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
