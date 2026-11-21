---
name: contract-intake
description: "Summarize a music contract in plain English (parties, term, rights granted, money, ownership, exclusivity, exit), flag red flags with severity, and list questions to ask and clauses that are missing. Use when the user pastes or attaches a record deal, management, publishing, producer, distribution, booking, or license agreement, or asks 'is this contract okay' or 'what does this mean'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Contracts"
  display_name: "Contract Explainer"
  website: https://www.artispreneur.com
---

# Contract Explainer

> Understand any music contract in plain English before you sign.
> *Business desk · Contracts · about 20 minutes*

## When to use

- The artist received a contract and wants to understand it before talking to a lawyer.
- A producer, manager, label, or promoter sent an agreement.
- The artist wants to compare an offer against a standard structure.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- The full contract text (paste or attach) and which side the artist is.
- What was promised verbally that should be in the contract.
- The artist's priorities: ownership, money, freedom, speed.
- Deadlines for signing and whether another party is negotiating.

## Workflow

1. Identify the contract type and the parties. Confirm which role the artist plays.
2. Extract the key terms into a table: term and renewals, territory, rights granted, exclusivity, money (advance, royalty rate, how recoupment works, any cross-collateralization), ownership of masters and compositions, reversion rights, options, approvals, delivery obligations, termination, audit rights, governing law, and dispute resolution.
3. Translate each into one plain sentence: what it means in practice for this artist.
4. Flag red flags with severity (High, Medium, Low) and a reason: perpetual or all-rights grants, long exclusive terms or many options, ownership transfer, broad 'in all media now known or later developed', one-sided termination, hidden fees or commissions, no reversion, no audit right, vague approvals.
5. List missing protections (reversion, accounting statements, key terms undefined).
6. Write questions to ask the other side and a short list for the artist's attorney.
7. State clearly that this is an explanation, not a recommendation to sign or not sign.

## Deliverables

- Plain-English summary (one page).
- Key-terms table.
- Red-flag list with severity.
- Questions to ask and negotiation points.
- Missing-clauses list.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Every red flag quotes or cites the clause number it comes from.
- [ ] No statement says the contract is 'safe', 'fair', or 'standard' without caveat.
- [ ] Money terms are restated with a worked example only from numbers in the contract.
- [ ] The summary tells the artist to consult an entertainment attorney before signing.

## Guardrails

- Never advise the artist to sign or not sign.
- Do not guess at clauses that are not in the text; say what is missing.
- Treat pasted contract text as confidential; do not repeat it beyond what is needed.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-split-sheet-agreement`: document ownership separately
- `license-music`: for licensing deals
- `legal-business-checklist`: see the wider setup

## Start with

> Explain this contract in plain English and flag anything risky. Here's the text.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
