---
name: create-an-epk
description: "Build an electronic press kit (EPK) tailored to one audience (booking, press, brand partnership, festival, or general), with bios, sourced stats, discography, media list, and a clear call to action. Use when the user asks for an EPK, press kit, one-sheet, or 'something to send bookers and journalists'. Every stat must be sourced or removed."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Press
  group: "Studio"
  display_name: "EPK Builder"
  website: https://www.artispreneur.com
---

# EPK Builder

> A press kit built for the person reading it: booker, press, brand, or festival.
> *Press desk · Studio · about 25 minutes*

## When to use

- The artist needs something to send to bookers, press, brands, festivals, or playlist curators.
- An existing EPK is out of date (use the freshness check at the end).
- A new release or milestone should be reflected in the kit.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Who will read this: booker, press, brand, festival, or general?
- Links to music, videos, social profiles, and any existing EPK or bio.
- Proof points the artist can source: shows played, press mentions, playlist adds, notable collaborators, streaming or social numbers.
- Photos and videos available (and who holds the rights), plus the contact email.
- The one action the reader should take after reading.

## Workflow

1. Pick the audience. It decides section order, length, and emphasis: bookers want live proof and logistics; press wants a story and a hook; brands want audience fit; festivals want draw and stage readiness.
2. Gather facts from the artist and links. Build a fact sheet; anything unsourced is marked `[CONFIRM]`.
3. Write the bios at three lengths from supported facts only (use `create-an-artist-bio` if the artist wants the full set).
4. Assemble sections in the order for that audience (see layouts below). Keep it to one screen of scrolling or two printed pages.
5. Run the claim check: for every stat, quote, and credit, confirm a source and a date. Remove anything that cannot be backed up.
6. Produce the kit as web-ready HTML or Markdown plus a print-ready version, and a short cover email.
7. Maintenance: before each outreach round, re-check that numbers, 'latest release', and press links are still current.

## Deliverables

- EPK in the requested format (HTML or Markdown, print-ready).
- One-line pitch and a 3-sentence cover email.
- Claim-check table: every stat with source and date.
- List of missing assets and facts.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Section order by audience:
- **Booking:** one-line pitch, live video, upcoming/past shows, draw and venues played, tech rider summary, contact.
- **Press:** hook/story, short and long bio, latest release with a listening link, press quotes, high-res photos, contact.
- **Brand:** audience description, content examples, past partnerships, values fit, contact.
- **Festival:** live video, set length options, draw proof, stage plot and input list, contact.
- **General:** tagline, 50-word bio, best song/video, three proof points, links, contact.

Claim-check table:
| Claim | Source URL | Date checked | Status (kept / removed / confirm) |

## Quality checks (run before handing over)

- [ ] Every stat, quote, and credit is in the claim-check table with a source and date.
- [ ] Section order matches the chosen audience.
- [ ] No placeholder text, no sample numbers, no lorem ipsum remains.
- [ ] Exactly one call to action.
- [ ] Contact email is correct and appears twice (top and bottom).

## Guardrails

- Never invent shows, draw numbers, chart positions, certifications, press quotes, or partnerships.
- Only use photos and video the artist has rights to publish.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-an-artist-bio`: bios at every length
- `brand-positioning`: if the story is unclear
- `booking-outreach`: send the kit to venues
- `pr-campaign`: send the kit to press

## Start with

> Build my EPK for booking venues. Here are my links and what I can prove.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
