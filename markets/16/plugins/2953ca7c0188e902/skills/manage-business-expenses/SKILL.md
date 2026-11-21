---
name: manage-business-expenses
description: "Set up musician-specific expense categories, a tracking template, and a monthly close routine so receipts, mileage, and income are organized for taxes and budgeting. Use when the user asks 'what can I write off', 'track my music expenses', 'organize my receipts', or is preparing for tax season or opening books for a new business."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Finance"
  display_name: "Expense Manager"
  website: https://www.artispreneur.com
---

# Expense Manager

> Know where every dollar goes, and keep the receipts that save you taxes.
> *Business desk · Finance · about 20 minutes*

## When to use

- The artist has no system for tracking music spending.
- Tax season is approaching and records are scattered.
- A new business account or entity was just set up.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Business structure and whether the artist uses accounting software or spreadsheets.
- Typical expense types this year (studio, gear, ads, travel, merch, distribution, software).
- Whether the artist drives for gigs and tracks mileage.
- How receipts are collected today (email, photos, paper).
- Tax country and filing method if known.

## Workflow

1. Build the category list for a working musician (see below). Keep it to 12 to 18 categories.
2. Create the tracking template with these columns: date, vendor, amount, category, payment method, business purpose, receipt link, and notes.
3. Set capture habits: photograph or forward every receipt the day it happens, and name files `YYYY-MM-DD_vendor_amount`.
4. Set a monthly close: reconcile with the bank statement, categorize, flag unknowns, and total by category.
5. Add a mileage log (date, start, end, miles, purpose).
6. List questions for a tax professional: gear purchases and how they are treated, home-studio use, and what documentation they want. Do not assert what is deductible.

## Deliverables

- Category list.
- Expense tracker template (CSV or table).
- Monthly close checklist.
- Mileage log template.
- Questions for the tax professional.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Starter categories: studio and recording, production and beats, mixing and mastering, distribution and registration fees, marketing and ads, PR and publicity, gear and equipment, software and subscriptions, travel and lodging, vehicle and mileage, merch cost of goods, rehearsal space, video production, professional fees (legal, accounting), insurance, website and hosting, education, bank and processing fees, other.

## Quality checks (run before handing over)

- [ ] Every row has a business purpose and a receipt link.
- [ ] The monthly total by category matches the bank statement.
- [ ] Personal and business spending are not mixed.
- [ ] The deductibility questions are routed to a tax professional.

## Guardrails

- Do not declare any expense deductible. Say 'ask your tax professional' and explain what documentation to keep.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `file-business-taxes`: turn the records into a tax-prep package
- `budget-planning`: use real spend to plan the next budget
- `open-business-bank-account`: separate accounts make this easy

## Start with

> Set up an expense tracker for my music business and tell me what receipts to keep.

---
General information to help you prepare, not tax or legal advice. Rules and fees change, so confirm on the official site or with a tax professional.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
