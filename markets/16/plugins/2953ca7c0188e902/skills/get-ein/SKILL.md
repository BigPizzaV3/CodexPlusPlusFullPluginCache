---
name: get-ein
description: "Walk a US artist or music business through getting an Employer Identification Number (EIN) directly from the IRS: readiness checklist, question-by-question guide to the IRS online application, and where to store the confirmation letter. Use when the user asks 'how do I get an EIN', 'tax ID for my music business', or is opening a business bank account, forming an LLC, or filling a W-9."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Legal entity"
  display_name: "EIN Registration"
  website: https://www.artispreneur.com
---

# EIN Registration

> Your federal tax ID directly from the IRS, done step by step.
> *Business desk · Legal entity · about 15 minutes*

## When to use

- The artist formed or is forming an LLC or corporation.
- A bank, distributor, or payer asks for a tax ID and the artist wants to avoid sharing a personal SSN.
- The artist is a sole proprietor who wants a separate business identifier.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Business structure: sole proprietor, single-member LLC, multi-member LLC, S-corp, or C-corp.
- Proposed or registered business entity name and state of formation (use a `[BUSINESS_NAME]` placeholder if preferred).
- Business start date and a one-line description of activity (for example 'music recording and performance').
- Whether the business will hire employees in the next 12 months.
- Role of the 'responsible party' (the individual who controls or manages the business, e.g., sole proprietor or managing member). Never ask for or collect their SSN, ITIN, legal ID number, or home street address.

## Workflow

1. Confirm the artist needs one. A sole proprietor with no employees can use an SSN, but an EIN keeps the SSN off W-9s and invoices.
2. State the rule: the IRS issues EINs directly on irs.gov at no government fee. Warn the artist to avoid third-party look-alike filing sites.
3. Prepare the non-sensitive worksheet fields (business structure, start date, primary music activity, expected employee count, closing month of the tax year) and insert `[LEGAL_NAME_ON_FORM]` and `[BUSINESS_ADDRESS_ON_FORM]` placeholders so the artist can enter their legal name and street address directly on irs.gov.
4. Walk through the IRS online application section by section on irs.gov (search 'Apply for an EIN'). The artist types the responsible party's SSN or ITIN themselves. The application has limited hours, so check them on the site.
5. Tell the artist to download and save the confirmation letter (CP 575) at the end of the session as a PDF, and to back it up.
6. Give the next steps: open a business bank account, update the distributor, PRO publisher account, and payers with the EIN.

## Deliverables

- `ein-readiness-checklist.md`: every answer prepared before applying.
- Screen-by-screen walkthrough of the IRS application.
- Post-EIN checklist (bank, distributor, PRO, W-9).

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] The artist's answers match the formation documents exactly (name spelling, state).
- [ ] The guidance tells the artist to apply only on irs.gov.
- [ ] No SSN, ITIN, or EIN digits were requested or written in chat.
- [ ] The confirmation-letter storage step is included.

## Guardrails

- Do not ask for or repeat SSNs, ITINs, or EINs.
- Direct the artist only to official irs.gov pages and warn against third-party fee-charging intermediaries.
- US-only guidance. For other countries, direct the artist to their national tax authority.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-llc`: if the entity is not formed yet
- `open-business-bank-account`: next step once the EIN exists
- `legal-business-checklist`: see where this sits in the full setup

## Start with

> Walk me through getting an EIN. Tell me what to prepare first.

---
General information to help you prepare, not tax or legal advice. Rules and fees change, so confirm on the official site or with a tax professional.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
