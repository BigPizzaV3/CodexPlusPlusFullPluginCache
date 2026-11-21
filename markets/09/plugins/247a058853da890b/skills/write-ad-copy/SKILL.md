---
name: write-ad-copy
description: Write on-brand Meta ad copy (primary text, headlines, descriptions, CTAs) for an AdStellar team using its brand kit and products. Use when the user asks for ad copy, headlines, hooks, CTAs, or copy variants for Facebook or Instagram ads.
---

Use this skill when the user wants ad copy for Meta (Facebook or Instagram) ads and their AdStellar account is connected.

## Inputs to establish

1. Which product or brand kit the copy is for. Call `list_products` and `get_brand_kit`; if the team has several products and the user did not name one, ask which one before generating.
2. The goal of the ad (for example trial signups, purchases, lead capture) and the tone. If the user gives neither, use the brand kit's tone of voice and ask for the goal in one short question.
3. How many variants they want (`count`, default 5, maximum 10) and the `length` (`short`, `medium`, or `long`).

## Steps

1. Call `generate_ad_copy` once with `productId` or `brandKitId`, `count`, `tone`, `length`, `adGoal`, and any `customInstructions` the user gave. This tool is free and does not use AI credits.
2. Each variant comes back with `headline`, `primaryText` (the long-form Meta primary text), an optional `description` (short link description), and `cta`. Present the variants as a numbered list with those fields on separate lines. Keep the copy exactly as returned; do not silently rewrite it.
3. Offer one round of refinement (different tone, shorter, a specific angle) and re-run the tool with updated `customInstructions` instead of editing the copy yourself.

## Do not

- Do not invent brand facts, prices, offers, or claims that are not in the brand kit, the product record, or the user's message.
- Do not promise results or compliance with Meta's advertising policies; suggest the user review claims before launch.
- Do not call `generate_image` or `generate_video` from this skill unless the user explicitly asks for creatives; use the generate-ad-creatives skill for that.
