---
name: artist-profile
description: "Build or update a complete artist profile (identity, genre, links, catalog, business setup, sourced proof points) and rate the career stage with reasons. Use at the start of any music-career work, when the user says 'set up my artist profile', 'who am I as an artist', 'update my info', or when another skill needs facts that are missing."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Career"
  display_name: "Artist Profile"
  website: https://www.artispreneur.com
---

# Artist Profile

> Your artist record, set up once. Every other skill reads from it.
> *Home Base desk · Career · about 10 minutes*

## When to use

- The artist is new to this toolkit and no profile exists yet.
- Facts changed: new release, new link, new entity, new PRO, new team member.
- Any other skill reports missing facts and the artist wants them filled in once.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Stage or project name, coarse region/country (no street addresses or GPS coordinates), genres, and roles (writer, performer, producer). Keep legal names as `[LEGAL_NAME]` placeholders unless needed for a local draft.
- Links: Spotify, Apple Music, YouTube, Instagram, TikTok, website, existing EPK.
- Releases so far: titles, dates, and which are the latest.
- Business setup: entity type if any, PRO, distributor, publisher or admin, label, manager, attorney.
- Any numbers they want to use publicly (listeners, followers, shows), and where each can be checked.

## Workflow

1. Collect the facts above. Accept pasted bios, links, or a prior EPK and extract from them instead of re-asking.
2. Fill the profile template. Leave unknowns as `[CONFIRM]`; never guess.
3. For every number, record source and date checked. A number with no source goes in a separate 'unverified' list and stays out of public-facing work.
4. Rate the career stage using the rubric below and give three evidence-based reasons.
5. List the missing facts in priority order: the ones that block the most other skills first.
6. Offer the single most useful next skill based on the gaps.

## Deliverables

- `artist-profile.md`: the complete profile, ready to reuse by every other skill.
- Career-stage assessment with three reasons.
- Missing-facts list, ranked by what it unblocks.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

```markdown
# Artist Profile: [Stage name]
Last updated: YYYY-MM-DD

## Identity
- Stage name / `[LEGAL_NAME_ON_REGISTRATIONS]` / region / genres / roles
## Links
- Spotify / Apple Music / YouTube / Instagram / TikTok / website / EPK
## Music
- Releases (title, date, format) / latest release / approximate catalog size
## Business setup
- Entity: / PRO: / MLC: / SoundExchange: / Distributor: / Publisher or admin: / Label: / Manager: / Attorney:
## Proof points (sourced)
| Claim | Value | Source | Date checked |
## Team and collaborators
## Goals (from artist-goals)
## Career stage
- Stage: Starting | Building | Growing | Established
- Reasons: 1) 2) 3)
## Missing facts
```

Career-stage rubric (judge by evidence, not by follower counts alone):
- **Starting:** pre-release or first releases; no steady audience data yet.
- **Building:** regular releases; an audience is forming locally or online; business basics partly done.
- **Growing:** consistent audience plus outside validation (paid shows, press, playlist adds, collaborators); some revenue streams active.
- **Established:** several revenue streams, repeat bookings or placements, a working team, and registrations complete.

## Quality checks (run before handing over)

- [ ] Every proof point has a source and a date, or sits in the unverified list.
- [ ] A reminder is included that legal name spelling must match across PRO, MLC, and distributor portals when the artist files.
- [ ] No SSN, bank, or password data appears anywhere in the file.
- [ ] The stage rating cites evidence from the profile, not a feeling.

## Guardrails

- Store identification only as yes/no or public IDs (e.g. IPI number). Never store tax IDs or account numbers.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `artist-goals`: turn the profile into 1 to 3 dated goals
- `knowledge-ingestion`: extract facts from bios, contracts, and old EPKs
- `legal-business-checklist`: close business-setup gaps

## Start with

> Set up my artist profile. Ask me what you need, or I'll paste my bio and links.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
