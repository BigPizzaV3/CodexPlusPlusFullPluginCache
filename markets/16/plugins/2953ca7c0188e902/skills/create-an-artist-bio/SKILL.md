---
name: create-an-artist-bio
description: "Write an artist tagline plus 50-word, 150-word, and 400-word bios in one consistent voice from supported facts only, ready for Spotify, press, EPKs, and festival programs. Use when the user asks for a bio, 'about me', artist description, or 'write my Spotify bio'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Press
  group: "Studio"
  display_name: "Artist Bio Writer"
  website: https://www.artispreneur.com
---

# Artist Bio Writer

> One story, told at every length you'll ever need.
> *Press desk · Studio · about 10 minutes*

## When to use

- No bio exists, or the current one is dated or generic.
- A platform asks for a specific length.
- A release or milestone changes the story.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Where the artist is from and where they are based now.
- Genre and the feeling or point of view of the music.
- Three to five verifiable facts: releases, shows, collaborators, press, milestones.
- Voice preference: formal, conversational, or edgy. Third person is the default.
- Where the bio will appear (Spotify, press, festival, website).

## Workflow

1. Find the angle: the single most specific, true thing about the artist. Generic claims ('unique sound') are cut.
2. Write the tagline (one line, under 12 words).
3. Write the 50-word bio: who, what they make, one proof point, one current thing.
4. Write the 150-word bio: add origin, influences stated by the artist, and a notable release or moment.
5. Write the 400-word bio in a simple arc: origin, development, breakthrough or current project, what's next.
6. Check every sentence against the fact sheet. Delete or mark `[CONFIRM]` anything not supported.
7. Offer first-person versions on request.

## Deliverables

- Tagline.
- 50-, 150-, and 400-word bios in one voice.
- Fact-check list showing which fact backs each claim.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Word counts are within 10% of target.
- [ ] Every claim maps to a fact the artist supplied.
- [ ] No superlatives without proof ('best', 'biggest', 'most-streamed').
- [ ] Names, places, and release titles are spelled exactly as the artist spells them.
- [ ] Bios read as the same voice at every length.

## Guardrails

- Never invent origin stories, awards, or collaborators to make the bio more exciting.
- Do not describe the music by comparing to famous artists unless the artist said it themselves.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-an-epk`: put the bios into a full kit
- `brand-positioning`: if the angle is hard to find
- `generate-social-media-content`: adapt the bio for social profiles

## Start with

> Write my artist bio at 50, 150 and 400 words. I'll give you my facts.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
