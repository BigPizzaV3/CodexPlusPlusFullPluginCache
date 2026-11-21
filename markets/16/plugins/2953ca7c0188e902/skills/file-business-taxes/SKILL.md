---
name: file-business-taxes
description: "Help a US-based artist prepare for tax season: identify which forms likely apply to their structure, list documents to gather, set up estimated-tax planning, and prepare questions for a tax professional. Use when the user asks 'how do I file taxes as a musician', 'what forms do I need', '1099', 'quarterly taxes', or 'self-employment tax'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Finance"
  display_name: "Business Tax Filing"
  website: https://www.artispreneur.com
---

# Business Tax Filing

> Get organized for tax season instead of panicking through it.
> *Business desk · Finance · about 20 minutes*

## When to use

- Tax season is near and the artist has music income.
- The artist received 1099 forms for the first time.
- The artist wants to understand estimated quarterly payments.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Country (this skill is US-focused; for other countries, build the checklist and defer forms to the local authority).
- Business structure: sole proprietor, single-member LLC, multi-member LLC, S-corp, or C-corp.
- Income sources: shows, streaming, royalties, sync, merch, teaching, day job.
- Forms or statements already received (1099-NEC, 1099-MISC, 1099-K, W-2).
- Whether the artist has a tax professional.

## Workflow

1. Map structure to the usual forms so the artist knows what to expect: sole proprietors and single-member LLCs usually report on Schedule C and Schedule SE with their personal return; multi-member LLCs and partnerships file Form 1065 with K-1s; S-corps file 1120-S; C-corps file 1120. Confirm current requirements with the IRS or a professional.
2. List documents to gather: income forms, platform and distributor statements, bank and card statements, the expense tracker, mileage log, asset purchases, and prior-year return.
3. Explain estimated taxes: people with self-employment income often pay quarterly through Form 1040-ES. Show the formula to set aside a percentage and have the artist pick a reserve rate with their tax professional.
4. Merch and sales tax: ask whether the artist sells merch and flag that state sales-tax rules apply and vary.
5. Compile the question list for the tax professional.
6. Create a dated calendar of the filing and payment deadlines to confirm on irs.gov.

## Deliverables

- Likely-forms map for the artist's structure.
- Documents checklist.
- Estimated-tax reserve worksheet (with formula and assumptions).
- Tax calendar with dates to confirm.
- Questions for the tax professional.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Forms are described as 'usually applies', with a prompt to confirm.
- [ ] No dollar amount of tax is stated as owed.
- [ ] Deadlines are marked to confirm on irs.gov.
- [ ] Sales-tax and state-return items are included.

## Guardrails

- Never calculate or state a tax liability as final.
- Do not recommend deductions or filing positions.
- Do not accept SSNs or tax IDs in chat.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `manage-business-expenses`: feed the records
- `get-ein`: if an EIN is needed
- `track-royalties-on-dsps`: income by source

## Start with

> Help me get ready for tax season. I'm a US artist with this kind of income.

---
General information to help you prepare, not tax or legal advice. Rules and fees change, so confirm on the official site or with a tax professional.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
