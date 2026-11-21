---
name: open-business-bank-account
description: "Prepare an artist to open a business bank account: required documents for their structure, how to compare banks, questions to ask, and a simple account setup (operating, tax reserve, savings). Use when the user asks 'how do I open a business bank account', 'separate my music money', or has just formed an LLC or got an EIN."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Finance"
  display_name: "Business Bank Account"
  website: https://www.artispreneur.com
---

# Business Bank Account

> Walk into the bank (or app) with everything they'll ask for.
> *Business desk · Finance · about 15 minutes*

## When to use

- A business entity or EIN was just created.
- Personal and music money are mixed.
- A distributor, PRO, or payer needs a payout account.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Business structure (sole proprietor, LLC, corporation) and state.
- Which documents they already have (formation papers, EIN letter, operating agreement, DBA).
- Expected monthly deposits and payments, and how often they handle cash.
- Needs: debit card, sub-accounts, card payments, international transfers.
- Bank or app preferences.

## Workflow

1. List the documents the artist needs for their structure: government ID, formation documents or DBA, EIN confirmation letter, operating agreement or corporate resolution, and ownership details.
2. Give a comparison checklist: monthly fees and how to waive them, minimum balance, transaction limits, wire and ACH costs, mobile deposit, sub-accounts, integrations with accounting tools, FDIC or NCUA coverage, in-person vs online.
3. Provide questions to ask the bank, so the artist compares offers on the same terms. Fees must be confirmed on the bank's own site.
4. Recommend a simple structure: one operating account, one tax-reserve account, and one savings or runway account.
5. Plan the changeover: update the distributor, PRO, payment processors, and invoices with the new account (entered by the artist on those sites).
6. Set a habit: pay the artist a fixed owner draw instead of mixing personal spending into the business.

## Deliverables

- Document checklist for the artist's structure.
- Bank comparison sheet.
- Question list for the bank.
- Account structure and changeover checklist.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] The document list matches the entity type.
- [ ] All fees are marked `[CONFIRM]` with the source to check.
- [ ] The artist has a clear plan for owner draws and tax reserve.
- [ ] No account numbers or logins were requested.

## Guardrails

- Never ask for or store account or routing numbers.
- Do not recommend a specific bank as best; compare on the artist's stated needs.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `get-ein`: needed first
- `manage-business-expenses`: start tracking right away
- `file-business-taxes`: tax-reserve planning

## Start with

> Help me get ready to open a business bank account. I have an LLC and an EIN.

---
General information and planning help, not financial advice. Every figure is an estimate built from the numbers you provide.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
