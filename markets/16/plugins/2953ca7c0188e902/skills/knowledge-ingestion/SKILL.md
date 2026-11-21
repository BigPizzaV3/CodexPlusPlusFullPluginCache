---
name: knowledge-ingestion
description: "Extract durable facts from the artist's existing material (bios, EPKs, press, emails, contracts) into the artist profile with source, date, and confidence, and flag conflicts between documents. Use when the user pastes or attaches existing documents and asks 'learn from this', 'update my profile from my EPK', or 'remember these details'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Home Base
  group: "Build your own"
  display_name: "Teach Your Agent"
  website: https://www.artispreneur.com
---

# Teach Your Agent

> Teach your agent: turn your bios, contracts and past EPKs into facts it remembers.
> *Home Base desk · Build your own · about 20 minutes*

## When to use

- The artist has old bios, EPKs, press, or contracts and does not want to retype them.
- A profile exists but is out of date.
- Documents disagree and need reconciling.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- The documents (paste or attach) and what each is.
- Which facts matter most (identity, releases, business, proof points).
- Anything that should not be stored (private details, confidential terms).
- Which version wins when documents conflict.

## Workflow

1. Read each document and extract candidate facts into rows: fact, source document, date of the source, and confidence (confirmed by artist, from a document, or unclear).
2. Group by profile section (identity, music, business, proof points, team).
3. Detect conflicts (different release dates, name spellings, numbers) and list both values with sources.
4. Show the artist the proposed updates and get approval before changing `artist-profile.md`.
5. For contracts, store only the summary facts the artist wants (parties, term, key dates), not the text, and do not store confidential financial terms unless the artist asks.
6. Mark numbers as unverified until a source and date are recorded.

## Deliverables

- Fact table with source, date, and confidence.
- Conflict list.
- Proposed profile updates for approval.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Each fact has a source.
- [ ] Conflicts are shown, not silently resolved.
- [ ] Nothing sensitive was stored without the artist's say.
- [ ] The profile changes only after approval.

## Guardrails

- Never store passwords, tax IDs, account numbers, or ID numbers.
- Do not treat claims in a document as verified just because they appear there.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `artist-profile`: apply the approved facts
- `contract-intake`: if a contract needs a real explanation
- `create-an-epk`: rebuild the kit from the clean facts

## Start with

> Learn from these documents and update my artist profile. Show me what you'd change.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
