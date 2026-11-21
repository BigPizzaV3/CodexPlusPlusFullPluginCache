---
name: claim-tracks-with-pro
description: "Audit a catalog song by song against the public royalty registries (Songview, ASCAP, BMI, The MLC, SoundExchange), mark each as found, missing, wrong, or not checked, compare IDs and splits across sources, and plan recovery with labeled estimates. Use when the user asks 'am I missing royalties', 'unclaimed royalties', 'find my money', 'audit my catalog', or has older releases with no registration history."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Release
  group: "Publishing & PRO"
  display_name: "Unclaimed Royalties"
  website: https://www.artispreneur.com
---

# Unclaimed Royalties

> Find and claim royalties already owed to you.
> *Release desk · Publishing & PRO · about 30 minutes*

## When to use

- The artist released music before registering anywhere.
- A statement or registry shows missing or mismatched data.
- An annual catalog hygiene check.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Stage or writer display names and any alternate credit spellings (the artist checks their own legal name directly on official registry portals).
- Writer ID (IPI/CAE) if known, and past or current PRO, publisher, label, and union affiliations.
- Catalog: song titles, writers with shares, ISRCs, release dates, distributor.
- Which songs matter most (highest streams first).
- Any statements available for reality checks.

## Workflow

1. Confirm identity first. Most 'missing' money is a name or ID mismatch; record every spelling.
2. Rebuild the catalog: one row per song with writers, shares, ISRC, and release date. Mark anything unverified.
3. The artist searches each public registry by hand on the official portal and records the exact query and date (see `references/registry-search-worksheet.md`). This skill produces the plan and worksheet; it does not run automated lookups or scrape external sites.
4. Record FOUND, MISSING, WRONG, or NOT CHECKED for every song and registry.
5. Run the cross-registry pass: compare writers, shares, and IDs. Every disagreement is a lead.
6. For each MISSING or WRONG item give the fix route and the documents to have ready (split sheets, ISRCs, IPI/CAE).
7. Estimate value only with the artist's own numbers and labeled formulas (see `references/recovery-estimates.md`). Rank by deadline sensitivity first, then by value.
8. For large or tangled catalogs, mention that an administrator or royalty auditor is an option, with trade-offs.

## Deliverables

- Song-by-registry gap grid.
- Mismatch leads with both values, sources, and dates.
- Ranked recovery plan.
- Documents-to-have-ready list.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Every finding carries a source and a date checked.
- [ ] NOT CHECKED is used honestly where the artist did not run a search.
- [ ] Estimates are labeled ESTIMATE with formula and source.
- [ ] No claim that money was found or is owed.
- [ ] The artist files every claim themselves.

## Guardrails

- Never claim a lookup was run when it was not.
- Never ask for registry passwords.
- Only works the artist owns, co-owns, or performed on.
- Recommend an entertainment attorney or royalty auditor for disputes.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `register-tracks-with-pro`: register what is missing
- `royalty-readiness`: confirm the routes
- `track-royalties-on-dsps`: monitor payments after fixes

## Start with

> Audit my catalog for missing royalties. I'll give you my songs and what I've registered.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
