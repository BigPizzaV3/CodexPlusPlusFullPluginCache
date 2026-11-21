---
name: create-brand-logo
description: "Produce a complete logo brief for a musician or music brand: positioning summary, three described logo concepts, wordmark type and color recommendations, usage rules, and file-format checklist, ready to hand to a designer or build in a design tool. Use when the user asks for a logo, wordmark, brand mark, or 'logo ideas'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Studio"
  display_name: "Brand Logo"
  website: https://www.artispreneur.com
---

# Brand Logo

> A logo brief a designer (or Canva) can execute on day one.
> *Business desk · Studio · about 15 minutes*

## When to use

- The artist has no logo or an inconsistent one.
- A rebrand is planned for a new era or release.
- A designer or design tool needs clear direction.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Artist or brand name (exact spelling and capitalization).
- Genre, mood, and three adjectives for how it should feel.
- Where the logo will appear: avatar, cover art, merch, stage visuals, video.
- Existing colors, fonts, or logos to keep or avoid.
- Budget and whether a designer is involved.

## Workflow

1. Summarize the brand in one paragraph (audience, feeling, differentiator).
2. Describe three distinct concepts: wordmark, monogram/symbol, and a combination mark. For each: the idea, shape language, type style, and why it fits.
3. Recommend color palette (hex values) and one or two typefaces, with legibility notes at avatar size.
4. Specify usage: minimum size, clear space, one-color and reversed versions, and what never to do.
5. List required files: SVG, PNG with transparency, a square avatar crop, and a monochrome version.
6. Write a one-page designer brief and, if building in a design tool, the exact first prompt or layout.

## Deliverables

- Brand positioning summary.
- Three logo concept descriptions.
- Palette and type recommendations.
- Usage rules and file checklist.
- One-page designer brief.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Each concept is visibly different, not three variations of one idea.
- [ ] The logo still reads at 40 pixels and in one color.
- [ ] Colors pass a basic contrast check against the background they will sit on.
- [ ] Nothing imitates a known logo or trademark.

## Guardrails

- Do not copy or closely imitate another brand's mark.
- Recommend a basic trademark search (USPTO or the artist's national office) before the artist commits to a name or mark.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `write-brand-guidelines`: turn the chosen logo into a full brand system
- `brand-positioning`: if the positioning is not set
- `create-merch-designs`: apply the logo to merch

## Start with

> Write me a logo brief. My name is spelled like this and the vibe is this.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
