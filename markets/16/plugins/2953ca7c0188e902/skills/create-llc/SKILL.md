---
name: create-llc
description: "Plan an LLC for a musician or music business: choose the state, check the name, pick a registered agent, outline the filing, draft an operating agreement outline, and finish setup (EIN, bank, music rights). Use when the user asks 'should I form an LLC', 'how do I start an LLC for my music', or wants liability protection and cleaner finances."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Legal entity"
  display_name: "LLC Formation"
  website: https://www.artispreneur.com
---

# LLC Formation

> Separate your music money from your personal money.
> *Business desk · Legal entity · about 25 minutes*

## When to use

- The artist earns or spends real money and wants it separate from personal finances.
- The artist has bandmates or co-owners and needs an agreement.
- Contracts, brand deals, or bookings are starting to carry risk.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Home state and any other states where the artist works regularly.
- Number of owners and ownership percentages.
- Desired business name (and two backups).
- Whether the artist wants to rent or use a registered agent service.
- Expected annual revenue range, to frame the tax conversation.

## Workflow

1. Explain what an LLC does and does not do: it separates business liability from personal assets in many situations, but it is not a shield from your own wrongdoing, and it does not replace insurance or contracts.
2. Pick the state. The artist's home state is the default; compare filing fees and recurring costs (annual report, franchise or minimum taxes) on the Secretary of State site, and check whether the state requires publication.
3. Run a name check on the state business registry and a basic trademark search. Add the required LLC designator.
4. Choose a registered agent (the artist, if allowed, or a service).
5. Outline the filing (called Articles of Organization or Certificate of Formation depending on state): entity name, `[BUSINESS_ADDRESS_ON_STATE_FORM]` and `[REGISTERED_AGENT_ADDRESS]` placeholders (the artist enters physical addresses directly on the official state portal), and management structure.
6. Draft an operating agreement outline: owners and percentages, capital contributions, decision rules, profit distributions, what happens if someone leaves, and IP ownership.
7. Post-filing: get an EIN (`get-ein`), open a bank account, apply for local licenses or a DBA if needed, and calendar the annual report. Check the federal Beneficial Ownership Information (BOI) requirements on fincen.gov, since they have changed.
8. Music-specific: assign the artist's existing songs and masters to the LLC in a written assignment, update the PRO publisher entity, and point the distributor to the LLC. Ask a tax professional whether an S-corp tax election makes sense.

## Deliverables

- State comparison and recommendation with open costs flagged `[CONFIRM on state site]`.
- Filing worksheet with every field pre-answered.
- Operating agreement outline.
- Post-filing checklist including music-rights steps.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Fees and deadlines are marked to confirm on the official state site, not stated from memory.
- [ ] The ownership table totals 100%.
- [ ] The checklist includes rights assignment, EIN, bank, annual report, and BOI check.
- [ ] The artist knows what the LLC does not protect against.

## Guardrails

- Do not quote filing fees or tax rates as facts; direct to the state site.
- Do not tell the artist an LLC makes them immune from liability.
- An operating agreement with multiple owners should be reviewed by an attorney.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `get-ein`: tax ID right after filing
- `open-business-bank-account`: separate the money
- `create-split-sheet-agreement`: document song ownership
- `create-c-corp`: if investors or scale are the plan

## Start with

> Help me decide on and set up an LLC for my music. I'm in this state.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
