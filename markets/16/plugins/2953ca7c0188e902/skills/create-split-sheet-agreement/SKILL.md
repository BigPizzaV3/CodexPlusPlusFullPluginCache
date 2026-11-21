---
name: create-split-sheet-agreement
description: "Draft a songwriting split sheet recording each writer's role and percentage of the composition (checked to total exactly 100%), with PRO, IPI, publisher, contact, and signature fields, and a separate section for master ownership and producer terms. Use when the user co-writes a song, asks 'how do we split this', 'write a split sheet', or needs ownership documented before release."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Contracts"
  display_name: "Split Sheet Agreement"
  website: https://www.artispreneur.com
---

# Split Sheet Agreement

> Everyone's share, in writing, before the song blows up.
> *Business desk · Contracts · about 15 minutes*

## When to use

- Two or more people contributed to a song.
- A producer, topliner, or featured artist needs terms in writing.
- A release or registration is coming and ownership is undocumented.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Song title and date written.
- Each contributor's writer/stage name (or `[WRITER_LEGAL_NAME]` placeholder for the offline signature copy), role (lyrics, melody, beat or production, arrangement), PRO, public IPI number if known, and publisher if any.
- The agreed percentage per writer, or the contribution details so a fair proposal can be made.
- Who owns the master recording and how master income is shared (separate from the writing split).
- Any samples or interpolations used.

## Workflow

1. Separate the two questions: who owns the composition (writing split) and who owns the master (recording split). They are separate decisions with separate owners.
2. If shares are not yet agreed, lay out common approaches (equal split, split by contribution) and let the writers decide. Do not impose.
3. Fill the sheet. Check the arithmetic: the composition shares must total exactly 100%. Reject and fix any sheet that does not.
4. Capture PRO and IPI per writer and each writer's publisher entity (or 'self-published').
5. Add the sample and interpolation disclosure, producer terms, and how disagreements will be handled.
6. Add signature and date lines for every writer and tell the artist to get every signature, ideally the same day as the session, and to store the signed PDF with the song's catalog entry.

## Deliverables

- Completed split sheet (Markdown or print-ready).
- Arithmetic check showing the total.
- Separate master-ownership note.
- Missing-signatures checklist.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

```markdown
# Split Sheet: [Song title]
Date written: / Location:
| Writer (legal name) | Role | Composition % | PRO | IPI/CAE | Publisher | Contact |
|---|---|---|---|---|---|---|
Total: 100%
Master recording ownership: [owner(s) and %] / Producer terms: [fee, points, credit]
Samples or interpolations: [none / list and clearance status]
Signatures: ______ date ______ (one per writer)
```

## Quality checks (run before handing over)

- [ ] Composition percentages total exactly 100%.
- [ ] Every writer's legal name matches what they use at their PRO.
- [ ] Samples are disclosed or explicitly 'none'.
- [ ] Every writer has a signature line, and the sheet says master ownership is handled separately.

## Guardrails

- Do not decide splits for the writers.
- If the writers disagree, stop and recommend a neutral party or attorney instead of drafting around the dispute.
- Never register a song whose splits do not total 100%.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `register-tracks-with-pro`: register the song once splits are signed
- `upload-track-to-catalogue`: store the signed sheet with the track
- `contract-intake`: if a producer or label sends their own agreement

## Start with

> Make a split sheet for my song. Here are the writers and what each did.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
