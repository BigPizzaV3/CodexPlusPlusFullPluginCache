---
name: track-royalties-on-dsps
description: "Map every royalty stream an artist can earn (master streams, PRO performance, MLC mechanicals, SoundExchange, neighboring rights, YouTube, sync, merch, live) and build a monthly tracker with reconciliation and anomaly flags. Use when the user asks 'track my royalties', 'where does my money come from', 'my statements don't add up', or after a release goes live."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Release
  group: "Finance"
  display_name: "Royalty Tracker"
  website: https://www.artispreneur.com
---

# Royalty Tracker

> Every royalty stream in one tracker, so nothing slips through.
> *Release desk · Finance · about 20 minutes*

## When to use

- Money is arriving from several places and nobody tracks it.
- A release just went live and statements will start arriving.
- The artist suspects a stream is missing or underpaid.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Distributor, PRO, publisher or admin, and label (if any).
- Whether The MLC and SoundExchange registrations exist.
- Statements or dashboards available to export.
- Other income: sync, YouTube, Patreon, merch, live shows.
- Months to cover.

## Workflow

1. Map the streams and who pays each: **master streams and downloads** (distributor or label), **songwriting performance** (PRO), **US streaming mechanicals** (The MLC or an administrator), **digital performance of recordings on non-interactive services** (SoundExchange), **neighboring rights outside the US** (the local organization), **YouTube and other user-generated platforms** (distributor, publisher, or admin), **sync**, **merch**, and **live**.
2. Build the monthly tracker with one row per source per period (columns below).
3. Set expectations on timing: statements usually arrive weeks to months after the usage month, and each payer follows its own cycle.
4. Reconcile: compare each statement total against the deposit that hit the bank and note any difference.
5. Flag anomalies: a stream with zero income despite usage, a sharp drop, duplicate charges, or a deposit with no statement.
6. For each anomaly give the check to run and where (see `royalty-readiness` and `claim-tracks-with-pro`).

## Deliverables

- Royalty stream map for this artist.
- Monthly tracker template.
- Reconciliation checklist.
- Anomaly list with next checks.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Tracker columns: period, source, stream type, units (streams, spins, sales), gross, fees or commission, net, statement reference, payment date, bank deposit match (Y/N), notes.

## Quality checks (run before handing over)

- [ ] Every stream the artist could earn is listed, even if currently zero.
- [ ] Gross, fees, and net reconcile to the deposit.
- [ ] Anomalies have a named next check.
- [ ] No figures were assumed; blanks stay blank.

## Guardrails

- Do not estimate unreported income as received.
- Report only numbers from statements the artist supplies.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `royalty-readiness`: confirm each stream is registered
- `claim-tracks-with-pro`: chase missing money
- `file-business-taxes`: pass income by source to taxes

## Start with

> Build me a royalty tracker. Here are my distributor, PRO, and the statements I have.

---
General information and planning help, not financial advice. Every figure is an estimate built from the numbers you provide.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
