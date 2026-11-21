---
name: legal-business-checklist
description: "Produce an ordered business-setup checklist for an independent artist (name, entity, EIN, bank, split sheets, copyright, PRO, MLC, SoundExchange, distributor, trademark, contracts, insurance, taxes) with a status for each and the next best action. Use when the user asks 'what do I need to set up', 'am I set up legally', or 'business basics for an artist'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Legal entity"
  display_name: "Business Setup Checklist"
  website: https://www.artispreneur.com
---

# Business Setup Checklist

> The business basics (entity, copyright, licensing, PRO) in the right order.
> *Business desk · Legal entity · about 15 minutes*

## When to use

- The artist is starting out and does not know where to begin.
- Before a first release or first paid booking.
- As an annual business health check.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Which items are already done (entity, EIN, bank, PRO, MLC, SoundExchange, distributor)?
- Country and state.
- Solo artist or band, and whether co-writers or producers are involved.
- Release date or first paid job coming up, if any.

## Workflow

1. Read `artist-profile.md` and mark each checklist item Done, In progress, Not started, or Not needed.
2. Order the open items using the sequence below, adjusted for the artist's deadlines.
3. For each open item give: why it matters, what it needs, cost to confirm, time to finish, and the skill that does it.
4. Mark release-blocking items clearly (anything that must exist before the music goes live).
5. Give the next three actions.

## Deliverables

- `business-checklist.md` with status per item.
- Release-blocking list.
- Next three actions.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Recommended order:
1. Name and handle check (state registry, domain, social handles, basic trademark search)
2. Entity decision (sole proprietorship, LLC, corporation) -> `create-llc` / `create-c-corp`
3. EIN -> `get-ein`
4. Business bank account -> `open-business-bank-account`
5. Split sheets for every co-written song -> `create-split-sheet-agreement`
6. Copyright: composition and sound recording are separate copyrights; registration is optional but valuable
7. PRO membership as writer, plus a publisher entity if you want to collect the publisher share -> `register-with-pro`
8. Register works with the PRO, The MLC, and SoundExchange -> `register-tracks-with-pro`
9. Distributor chosen and release delivered -> `distribution-readiness`
10. Contracts in place with producers, features, engineers, and designers (work-for-hire or licenses); sample clearances
11. Insurance for gear and liability where relevant
12. Bookkeeping and taxes -> `manage-business-expenses`, `file-business-taxes`

## Quality checks (run before handing over)

- [ ] Every item has a status and a next action.
- [ ] Release-blocking items are flagged.
- [ ] Fees are marked to confirm on official sites.
- [ ] Items that do not apply are marked Not needed, not silently dropped.

## Guardrails

- Do not tell the artist they are 'legally compliant'. Say which common steps are done and which are open.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-llc`: entity
- `register-with-pro`: royalty collection
- `create-split-sheet-agreement`: song ownership
- `contract-intake`: review any contract before signing

## Start with

> Run the business setup checklist for me. Here is what I've done so far.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
