---
name: royalty-readiness
description: "Confirm an artist is set up to collect all four royalty routes (PRO performance, US streaming mechanicals via The MLC, SoundExchange digital performance, and distributor master royalties), flag release-blocking gaps, and give the registration order. Use when the user asks 'am I registered everywhere', 'what royalties am I missing', 'how do I get paid from streams', or before or soon after a release."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Publishing & PRO"
  display_name: "Royalty Readiness"
  website: https://www.artispreneur.com
---

# Royalty Readiness

> Make sure every royalty stream you're owed has somewhere to land.
> *Business desk · Publishing & PRO · about 15 minutes*

## When to use

- Before or just after a release.
- The artist has never checked registrations.
- A new artist asks where streaming money comes from.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Which PRO (or none) and whether songs are registered.
- Whether The MLC and SoundExchange registrations exist or an administrator handles them.
- Distributor and release status.
- Whether the artist plays on other people's recordings (session work).
- Country (the routes below are US-centered; other countries have local equivalents).

## Workflow

1. Explain that one song earns from separate places, and each needs its own setup.
2. **Songwriting performance (the composition) goes to a PRO.** Join as a writer, then register every song as a work.
3. **US streaming mechanicals (the composition) go to The MLC.** Register directly, or confirm a publisher or administrator does it.
4. **Digital performance of the recording goes to SoundExchange.** It covers non-interactive services such as satellite, internet, and cable radio. It does not collect on-demand Spotify or Apple Music streams.
5. **Master royalties from streams and downloads go through the distributor** to the recording owner.
6. Check each against the artist's answers. For every gap, give the steps and mark it release-blocking (before release) or post-release.
7. Add situational routes when they apply: the AFM and SAG-AFTRA Intellectual Property Rights Distribution Fund for non-featured performers, and PPL or PRS in the UK and other local societies abroad.
8. Give the first missing registration as the next action.

## Deliverables

- Four-route status table (Done / Missing / Unsure).
- Release-blocking vs post-release list.
- Ordered registration plan with what to have ready for each.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

| Route | Pays | Collects | Status | Next step |
|---|---|---|---|---|
| PRO | Writer and publisher share of public performance | Composition | | |
| The MLC | US streaming mechanicals | Composition | | |
| SoundExchange | Digital performance of recordings (non-interactive) | Recording | | |
| Distributor | Master streaming and download income | Recording | | |

## Quality checks (run before handing over)

- [ ] All four routes appear with an honest status.
- [ ] SoundExchange is not described as a PRO or as the source of Spotify royalties.
- [ ] Fees are marked to confirm; none stated from memory.
- [ ] The first missing item is named as the next action.

## Guardrails

- Do not state fees, rates, or payout schedules as fact.
- Only works the artist owns or co-owns may be registered or claimed.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `register-with-pro`: join a PRO
- `register-tracks-with-pro`: add the songs
- `claim-tracks-with-pro`: audit what exists and recover what's missing
- `track-royalties-on-dsps`: track the money once it flows

## Start with

> Check my royalty setup. Here's what I've registered and where I distribute.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
