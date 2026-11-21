---
name: distribution-readiness
description: "Check masters, artwork, metadata, rights, and registrations before delivery to a distributor, and compare distributors against the artist's needs (pricing model, payout terms, publishing admin, YouTube, promotion tools, exit terms). Use when the user asks 'am I ready to release', 'which distributor should I use', 'what do I need to upload my song', or before any delivery."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Release
  group: "Release & DSP"
  display_name: "Distribution Readiness"
  website: https://www.artispreneur.com
---

# Distribution Readiness

> Everything checked before you upload, and the right distributor for you.
> *Release desk · Release & DSP · about 20 minutes*

## When to use

- A release is within weeks of delivery.
- The artist is choosing or switching distributors.
- A previous delivery was rejected or delayed.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Release type (single, EP, album) and planned release date.
- Master format and whether it is final; cover art status.
- ISRC and UPC: assigned by the distributor or by the artist?
- Rights: all samples cleared, splits signed, cover songs licensed?
- Needs: speed, cost, publishing admin, YouTube, label services, other territories.

## Workflow

1. Run the six-checkpoint check: **master**, **artwork**, **metadata**, **rights**, **distribution**, **promotion**. Mark each Ready, Missing, or Unknown.
2. For each gap give the next action and the skill that fixes it.
3. Check the delivery spec with the distributor: audio format and sample rate, artwork size and format, required fields, explicit flags, and language. Specs vary, so the artist confirms them on the distributor's site.
4. Compare distributors on the artist's stated needs: pricing model (annual, per release, or revenue share), payout terms and thresholds, share of revenue, publishing administration add-on, YouTube and Content ID, pre-save and promotion tools, delivery speed, support, and what happens to the catalog if the artist leaves. Examples to evaluate include DistroKid, TuneCore, CD Baby, and others; confirm current terms on their sites.
5. Recommend the lead time: deliver at least a few weeks before release so there is time to fix issues and pitch playlists.
6. Produce the go/no-go summary.

## Deliverables

- Six-checkpoint readiness table.
- Gap list with next actions.
- Distributor comparison on the artist's criteria.
- Go/no-go summary.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] Statuses are the artist's own reports; unknown is allowed.
- [ ] No claim that a distributor accepted the release or that rights are cleared.
- [ ] Distributor terms are marked to confirm.
- [ ] Samples and covers are explicitly addressed.

## Guardrails

- Do not state any distributor's pricing as fact.
- Do not verify rights; ask and mark.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `extract-metadata-from-track`: fix missing metadata
- `create-split-sheet-agreement`: fix open splits
- `release-music-with-dsp`: plan the rollout
- `set-up-dsp`: claim the artist profiles

## Start with

> Am I ready to deliver my single? Here's where I am on each checkpoint.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*
