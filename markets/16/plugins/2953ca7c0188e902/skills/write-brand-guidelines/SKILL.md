---
name: write-brand-guidelines
description: "Create a concise brand guidelines document for an artist or music brand covering story, voice and tone, color palette, typography, logo usage, imagery, social and merch rules, with do and don't examples. Use when the user asks for brand guidelines, a style guide, 'brand bible', or needs consistency across designers, collaborators, or AI tools."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Studio"
  display_name: "Brand Guidelines"
  website: https://www.artispreneur.com
---

# Brand Guidelines

> Your brand bible: voice, visuals, and rules everyone follows.
> *Business desk · Studio · about 20 minutes*

## When to use

- Multiple people or tools produce content and the look or tone drifts.
- A logo or positioning was just chosen and needs to be locked in.
- Preparing for press, brand deals, or a team.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Positioning statement and tagline (or run `brand-positioning` first).
- Logo files, palette, and fonts already in use.
- Three words for the voice and three words it should never sound like.
- Where the brand shows up: socials, merch, video, stage, website.
- Anything legally fixed (name spelling, trademarks).

## Workflow

1. Write the brand story in under 120 words.
2. Define voice and tone: three adjectives, a sentence on each, and 'we say / we don't say' examples.
3. Lock the palette with hex values, roles (primary, accent, background, text), and contrast-safe pairings.
4. Set typography: heading and body fonts, sizes, and fallbacks.
5. Set logo rules: versions, clear space, minimum size, misuse examples in words.
6. Add imagery direction: photo style, lighting, subjects, what to avoid.
7. Add channel rules for social posts, captions, hashtags, and merch.
8. Add a one-page cheat sheet and a prompt block that tells AI tools how to write in the brand voice.

## Deliverables

- Brand guidelines document (Markdown or print-ready).
- One-page cheat sheet.
- AI voice prompt block the artist can paste into any tool.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Every rule includes a concrete example.
- [ ] Colors have hex codes and an intended use.
- [ ] The voice section has at least three 'we say / we don't say' pairs.
- [ ] The document fits one readable sitting; trim anything nobody will use.

## Guardrails

- Do not invent a brand history. Build only from what the artist states.
- Keep fonts to ones the artist has a license to use.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-brand-logo`: if the logo is not done
- `brand-positioning`: if positioning is missing
- `create-merch-designs`: apply the rules to merch
- `generate-social-media-content`: write posts in the locked voice

## Start with

> Create brand guidelines for me. Here is my logo, colors and how I want to sound.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
