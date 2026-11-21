---
name: create-merch-designs
description: "Plan an artist's merch line and write a design brief for each item: product mix, concepts rooted in the artist's identity, print specifications, placement, color limits, pricing and margin math, and a drop plan. Use when the user asks for merch ideas, T-shirt or hoodie designs, a merch line, or 'what should I sell'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Content
  group: "Merch"
  display_name: "Merch Designs"
  website: https://www.artispreneur.com
---

# Merch Designs

> Merch your fans actually want to wear.
> *Content desk · Merch · about 25 minutes*

## When to use

- The artist is starting a merch line or refreshing one.
- A release or tour needs merch.
- Designs exist but the artist is unsure what to produce.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Brand guidelines, logo files, and visual identity.
- Audience: what fans wear and buy, and what they say they want.
- Budget and production method (print-on-demand or short runs).
- Moments to tie to: release, tour, anniversary, inside joke.
- Pricing comfort and shipping plans.

## Workflow

1. Pick 3 to 5 products from what fans would realistically wear or use (for example tee, hoodie, hat, poster, sticker, tote). Start small.
2. Write one concept per product: idea, tie to the artist's story, and why a fan would want it.
3. Write the design brief per item: artwork description, placement, size, color count, garment color, and file specs (vector or high-resolution, transparent background).
4. Do the margin math: price = cost of goods plus fulfillment plus fees plus target profit. Show the formula and let the artist pick the price.
5. Plan the drop: limited vs evergreen, timing with release, preorder option.
6. Rights check: no samples of others' logos, lyrics, or characters; fonts and images are licensed.
7. Plan sample orders to check quality before launch.

## Deliverables

- Merch line plan.
- Design brief per product.
- Pricing and margin table.
- Drop plan.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Output template

Margin formula: profit per unit = selling price - (production cost + fulfillment + payment fees + platform fees).

## Quality checks (run before handing over)

- [ ] Every design is original or licensed.
- [ ] Margin is positive at the chosen price.
- [ ] File specs are stated for each product.
- [ ] The line is small enough to launch.

## Guardrails

- Do not use others' trademarks, characters, or lyrics.
- Costs are quotes or labeled estimates.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `set-up-merch-drop-shipping`: set up fulfillment
- `write-brand-guidelines`: keep the look consistent
- `budget-planning`: fund the first run

## Start with

> Plan my merch line and write design briefs. Here's my logo and what my fans are like.

---
*Artispreneur · Art Means Business · https://www.artispreneur.com*
