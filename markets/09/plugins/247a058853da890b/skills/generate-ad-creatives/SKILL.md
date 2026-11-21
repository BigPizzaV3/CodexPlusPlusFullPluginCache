---
name: generate-ad-creatives
description: Generate AI image or video ad creatives in an AdStellar team, confirm before spending credits, and poll until the assets are ready. Use when the user asks to create, make, or generate ad images, video ads, UGC videos, or talking-actor videos.
---

Use this skill when the user wants new ad creatives (images or videos) produced in their AdStellar account. Generation spends AI credits from the team's balance, so the user must confirm before any generation call.

## Before generating

1. Establish the product or brand kit with `list_products` and `get_brand_kit`. Ask which product if it is ambiguous. If the team has neither yet, offer to create them from the user's website with `create_brand_kit_from_url` and `create_product_from_url` before generating. For image references, find asset ids with `search_assets`.
2. Call `get_credit_balance` so you can tell the user what they have available.
3. Work out the exact request:
   - Images: `aspectRatios` (one or more of `1:1`, `4:5`, `9:16`, `16:9`), `variationCount`, `instructions` (required unless `referenceAssetIds` are given), optional `renderMode` (`express` or `studio`). One image is generated per aspect ratio per variation, and each image costs a fixed number of credits. There is no model choice for images.
   - Video: `approach` (`exact` for a talking actor reading `scriptText`, `realistic` for cinematic UGC from a `scenePrompt`), `aspectRatio` (default `9:16`), `durationSeconds` (default 15), `variationCount`. Optionally call `list_models` with `capability: "video"` and pass a returned id as `model`; omit it to let AdStellar choose.
4. State the plan in one short message: what will be generated, how many outputs, and that it will spend AI credits from the balance you just reported. Do not quote an exact credit figure unless a tool returned one. Wait for the user to confirm before generating.

## Generating

- Images: call `generate_image`. It returns a `batchId` and `creditsConsumed`.
- Video with `approach: "exact"`: call `list_avatars` so the user can pick an `actorId`. Call `list_voices`; if it returns voices let the user pick a `voiceId`, and if it returns none, omit `voiceId` and the actor's default voice is used. Then call `generate_video`.
- Video with `approach: "realistic"`: call `generate_video` with `scenePrompt`, plus `productId` or `productImageUrl` when featuring a product.
- `generate_video` returns a `projectId` and does not report credits; tell the user the charge appears in their balance.
- Poll `get_generation_status` with the `batchId` or `projectId` every 10 to 20 seconds until every generation is `completed` or `failed`. Image batches usually finish within a minute; video can take several minutes. Tell the user roughly how long to expect.

## Presenting results

- Show each completed generation's asset or video URL as returned by `get_generation_status`. For images, report the `creditsConsumed` value from `generate_image`.
- If a generation failed, report the tool's error message as given and offer to retry with adjusted instructions. Do not retry automatically; a retry spends credits again.

## Do not

- Do not call `generate_image` or `generate_video` without explicit confirmation of the request.
- Do not pass a `model` to `generate_image` (it has none) or invent a video model id; only use ids returned by `list_models`.
- Do not describe an asset before `get_generation_status` reports it complete, and do not invent dimensions or file sizes the tool did not return.
