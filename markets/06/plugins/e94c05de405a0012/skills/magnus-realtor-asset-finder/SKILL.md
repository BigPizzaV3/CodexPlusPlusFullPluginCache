---
name: magnus-realtor-asset-finder
description: Find and verify public realtor headshots and brokerage logos for closing-congratulations graphics. Use when someone asks to research image assets for a named realtor.
---

# Magnus Realtor Asset Finder

Find professional image candidates quickly while keeping identity and final asset selection under human review.

## Gather identifying context

Use all context the user provides: full name, brokerage, market or state, email, phone, and Magnus contact ID. If the user refers to a visible MagnusHub row, inspect that row with the available browser and use its values. Do not require every field, but ask for another identifier before searching when the name alone is ambiguous.

Never treat facial resemblance alone as proof of identity.

## Research

Search public professional sources in this order:

1. The realtor's own professional website.
2. The brokerage's official agent roster or profile.
3. Realtor association, team, or established professional profiles.
4. Public business-oriented social profiles.
5. Reputable real-estate portals or aggregators as supporting evidence only.

Open the source page behind a search result. Confirm the candidate against at least two useful identifiers whenever possible, such as exact email, phone, brokerage, city, or state. Do not bypass logins, access controls, paywalls, or anti-bot measures.

For brokerage logos, prefer the brokerage's official site or brand resources. Verify that the logo represents the realtor's current brokerage rather than an old affiliation or a similarly named company.

Before ranking assets, read [quality and verification](references/quality-and-verification.md).

## Return proposals

Return one recommended headshot and one recommended logo when confidence is high. Include up to two alternatives when they are materially useful. For every candidate provide:

- A preview when the interface supports it.
- The page where it was found and the direct asset link when available.
- Confidence: High, Medium, or Low.
- The identifiers that support the match.
- Dimensions, format, watermark, crop, and background concerns when observable.
- A concise recommendation.

If identity confidence is not high, say so prominently and ask the user to choose or provide another identifier. Never present a low-confidence person as the correct realtor.

If no suitable asset is found, report that plainly and list the most useful next human lead instead of substituting an unrelated image.

## Approval boundary

Research and proposals are read-only. Do not download, edit, remove a background, upload to MagnusHub, or change a client record until the user explicitly selects a candidate and asks for that action.

When the user approves a download, keep the source image unchanged and save it non-destructively with a source note. When the user asks for image preparation, preserve the person's identity and make only the requested crop, background, sizing, or format changes. Do not synthesize a replacement face or remove a watermark.

Uploading to MagnusHub is outside version one of this workflow and always requires a separate explicit request.
