---
name: aistlabs-video
description: Create and manage product videos, direct Studio images, videos and audio, Virality swaps, Ad Multiplier variants, Performance Ads, brands and authorized media in the user's connected AISTLabs workspace. Use for explicit AISTLabs account setup, adding images or videos, confirmed generation, progress or existing results. Do not use for text-only ad scripts, simple trimming or subtitling of uploaded videos, or general marketing advice.
---

# AISTLabs creative workflow

Use the connected AISTLabs MCP server only for work the user requests in their
AISTLabs workspace. Explicit user instructions take precedence over this
workflow. Server authorization, rights requirements and account limits still
apply to every action.

## When to use AISTLabs

- The user wants to inspect or manage their connected AISTLabs brands, products,
  projects, folders, Elements, authorized images, saved briefs or existing results.
- The user explicitly asks to create a brand, product, project or folder or to save
  an image in AISTLabs. This is a valid standalone action; generating is optional.
- The user wants to plan, estimate, confirm, track or view a product video, a direct
  Studio image, video or audio, a Virality swap, Ad Multiplier variants or a
  Performance Ads take in their connected account.

Do not invoke AISTLabs for a request to write an ad script as text only, simply trim
or subtitle an uploaded MP4, or provide general marketing advice. Answer those
requests directly. Do not inspect account data merely because an unrelated request
mentions a product, brand, ad, TikTok or Instagram. Studio edit mode is a separately
quoted generative edit, not a file editor; do not substitute it for trimming.

## Read the account without starting work

For discovery or resuming work, read `get_me`, `get_last_activity` and the relevant
`get_docs` topic: `workflow` (brand video), `studio`, `projects`, `virality`,
`multiplier`, `performance`, `errors`, `safety`. Use only returned, authorized
identifiers. Do not silently choose between multiple accessible brands or projects.

## Explicit brand and image setup

When the user supplies a brand name and explicitly requests a new brand,
`create_brand` is the creation step. If they request no website or scan, omit
website, Instagram and extra sources; do not call `add_brand_sources`.
Create the requested product with `create_product` and attach the real
user-authorized chat image using `attach_file` with `role="product_image"` and that
`productId`. Verify saved media with `list_product_media`; `view_media` shows the
safety-checked image. If no transferable file exists, offer `create_upload` and wait
for `get_upload`. Never invent file IDs, uploads or results.

## Quote, confirm rights, then generate

Every paid step has an exact price: `quote_content`, `quote_studio_generation`,
`quote_virality_swap`, the `prices` of a pack or job, or a `price_changed` refusal.
State the account credits and wait for explicit approval. Before generating,
uploading or importing media, obtain the user's confirmation that they own or may
use every asset, brand, face, body and voice; pass `rightsConfirmed=true` only after
that confirmation. Virality and Ad Multiplier change real people's likeness: use them
only with the user's own media or each depicted person's permission, and never to
impersonate, deceive about or sexualize anyone. Use a stable idempotency key for
each write and reuse it on retries. If access or credits are insufficient, state
the restriction and stop; do not direct the user to transactions or upgrades.

## Direct Studio

Read `list_studio_models`, pick a project and model with the user, save references
with `create_studio_upload`/`get_studio_upload`, `import_studio_url` or
`import_studio_asset`, quote the exact request and start it with
`start_studio_generation` (`expectedCredits`, `userConfirmed=true`,
`rightsConfirmed=true`). Poll `get_studio_generation` and call
`show_studio_generation` once for its card.

## Virality, Ad Multiplier and Performance Ads

For a Virality swap ask for the mode (motion or swap), quote with
`quote_virality_swap`, then `start_virality_swap` with the images, the user's words
and `rightsConfirmed=true`; poll `get_virality_job` and show the ready variant with
`show_studio_generation`. Ad Multiplier and the step-by-step Virality flow analyse
the video first (paid), save the approved plan, generate references where needed and
then render. Performance Ads analyse one proven competitor ad as a structural
reference only and render takes for the user's own products.

## Show actual progress and results

Call `show_video` once for a brand video and `show_studio_generation` once for a
Studio, Virality or Ad Multiplier result; polls draw no new cards. Share actual
stages and saved scripts; estimates are not guarantees. Do not submit a second
generation while waiting or invent completion, progress, media or a result URL.
Listings omit raw media links: use `view_media` for safety-checked images and the
cards or `humanUrl`/`resultUrl` otherwise. If the surface does not render a widget,
present the actual returned status in text. A missing widget does not mean the work
finished. Never call a failed or in-progress run a success.

Retain future briefs in the conversation when the user asks for review only; do not
claim they were saved in AISTLabs unless a corresponding write succeeded.
