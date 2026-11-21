---
name: pixel-art
description: Use the Sprite Fusion API to generate, edit, style-match, create eight directional views of, and animate pixel art, retrieve saved assets, and check credits. Follows the Sprite Fusion Pixel Art Generator documentation.
---

# Sprite Fusion Pixel Art

The guide below is copied from Sprite Fusion's [Agent Guide](https://www.spritefusion.com/docs/pixel-art-generator/api/agent-guide). Only documentation links have been made absolute.

Read and follow this guide before making a Sprite Fusion API request. Treat the public API documentation as the complete contract: use documented operations and fields, preserve the user's intent, and do not invent implementation details.

## Check authentication first

Use `SPRITE_FUSION_API_KEY` from the agent's environment, or use a Sprite Fusion API key supplied by the user in the conversation directly as the Bearer token. Either source is sufficient. Immediately make the API request without asking the user to configure the other source.

Only when neither source contains a key, respond with this short setup guide:

> **Quick setup**
>
> 1. [Create your Sprite Fusion account](https://www.spritefusion.com/auth/sign-up?next=%2Faccount%2Fapi-keys).
> 2. [Create and copy an API key](https://www.spritefusion.com/account/api-keys).
> 3. Add it to your agent's environment as `SPRITE_FUSION_API_KEY`, or provide it in your next message.
>
> Once the key is available, I will continue your request.

As soon as a key is available from either source, continue the user's original request without asking them to repeat it or configure the other source.

## Choose the right operation

| User goal | Operation |
| --- | --- |
| Create a new sprite without an input image | `generate` |
| Make a targeted change to an existing sprite | `edit` |
| Create a new sprite guided by one or more visual examples | `style-reference` |
| Create eight directional views from one sprite | `direction-set` |
| Animate one sprite | `animate` |

Do not substitute a different operation when the requested result clearly maps to one of these. In particular, use `edit` for a targeted change that should preserve the primary image, and `style-reference` when the examples should guide a new sprite.

Before animating, make sure the source sprite has a pose suited to the requested motion. For walking, running, attacking, jumping, and similar actions, first use `edit` to create an appropriate starting pose, then animate that edited asset. Idle and other subtle animations can usually use the original sprite directly.

## Keep results available for follow-up work

Keep a small local record per request: request ID, operation, prompt, and every output's index, asset ID, URL, and local path when downloaded. When presenting choices, use stable labels tied to that request and asset.

Find saved results with [`GET /assets?limit=10`](https://www.spritefusion.com/docs/pixel-art-generator/api/api-reference#get-assets), or `GET /assets/{assetId}` when you know the ID. For more results, pass `nextCursor` as the URL-encoded `cursor` parameter; stop when it is `null`.

For edits and animations, use the version the user means and record new results alongside their source, preserving earlier entries. If that version was edited locally, send the current file as input. Continue without a selection step when the user's intent is clear.

## Ask only what is necessary

Ask the user a short question when a missing choice would materially change the result, such as:

- what should be created or changed
- which image is the primary subject when several images are provided
- what role each supporting image should have
- which output size to use when it cannot be inferred from the request
- what motion an animation should perform

If the request and inputs already answer those questions, proceed without asking for confirmation. Do not ask the user to choose undocumented technical or implementation details.

## Write useful prompts

- Describe the desired visual result directly.
- Avoid noisy phrases such as "transparent background," "crisp pixel art," or "pixel-perfect pixel art." Focus on the subject and the visual details that matter.
- Set the target size with the request's `size` field when the operation supports it. Do not include pixel dimensions in the prompt.
- Do not add visual requirements that conflict with the user's request.

Each operation has additional guidance in [Generate and Transform Sprites](https://www.spritefusion.com/docs/pixel-art-generator/api/generate-and-transform-images).

## Bundled documentation

The following files contain the corresponding Sprite Fusion documentation. Read the relevant pages for the requested operation:

- [Generate and Transform Sprites](references/generate-and-transform-images.md): instructions and examples for all five operations.
- [API Reference](references/api-reference.md): endpoints, request fields, responses, and errors.
- [Input Images](references/input-images-and-temporary-uploads.md): input formats, limits, and uploads.
- [Streaming, Errors, and Credits](references/streaming-errors-and-credits.md): collecting outputs, completion, retries, and credits.
- [Tips for Animations](references/animation-tips.mdx): read before animating a new source, as directed by Generate and Transform Sprites.

## Bundled client

[Client usage](references/client.md) documents the optional Python helper's command syntax and local output format. The Sprite Fusion documentation above defines generation behavior.
