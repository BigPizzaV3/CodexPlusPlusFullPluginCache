---
name: create-ad-creatives
description: Create product ad image concepts in a connected Melius account, or plan them without generation. Use for Melius product-photo ad workflows and checking their existing results. Not for checkout, subscription upgrades, or access to another team's private work.
---

# Create product ad creatives

Use the plugin's connected Melius tools. Follow the server's current instructions and schemas; do not guess tool arguments, model names, account IDs, prices, or asset IDs.

## Establish the brief and authorization

1. For direct canvas work, call `get_guide` with topic `getting-started` before other canvas tools. If Melius is not connected, use the host's account connection flow. Never ask for passwords, API keys, payment details, or email codes in chat.
2. Use the team authorized for the connection. `team_list` may identify accessible teams, but does not switch the connection's team. Ask the user to reconnect with the intended team if necessary; never attempt access outside the authorized scope.
3. Establish the product reference, number of images, aspect ratio, and creative direction. Use an existing authorized reference when supplied. Ask for missing information that affects fidelity or paid scope. Do not invent a missing photo or unsupported product claim.
4. Distinguish planning from generation. For draft, estimate-only, or review requests, provide concepts without submitting jobs or creating a canvas. Before generation, confirm the requested scope unless the user has already explicitly approved that exact scope. Honor any budget; use a genuine server estimate if available, and never invent an exact price.

## Generate the approved images

1. Discover available image models with `model_list`, including their required reference inputs and supported settings. Honor an explicitly chosen supported model. Do not select Cast video tools for an image-only request.
2. Use the chosen accessible project and create a canvas when requested. Follow the server guide for layout and presence before mutating canvas content.
3. For a supplied public image URL or product-page URL, use `url_to_canvas`; do not download and re-upload it. For a chat attachment, use `file_upload` and any required `file_upload_complete` handshake only when the host supplies an authorized file reference the tool can actually read. Never pass a guessed filesystem path. If the host cannot transfer the attachment, ask for an accessible image URL instead of claiming an upload succeeded.
4. Create the image nodes and reference edges required by the selected model. Preserve the product appearance and user-specified brand requirements. Use `bulk_run_start` for multiple images and `run_start` for one standalone image, following the current tool descriptions.
5. Retain every accepted run reference. Do not retry an ambiguous start, switch tools to bypass a denied call, or exceed the approved count. Inspect the existing run before deciding what remains. Stop on account, feature, or credit denial; do not initiate a purchase or promote an upgrade.

## Return and inspect results

Use `bulk_run_wait` or `run_wait` within the server's supported time budget, retaining references when work is still pending. For a later status request, inspect the existing runs rather than submitting replacements. Use `display_canvas` when available and return actual output links and the Melius canvas link from tool results. A text-only host still needs a useful status and links.

Report failed or partial generations explicitly. Never label a pending job as finished or a failed operation as successful. Follow the server's presence-release rule before ending the task. Never publish or share a private canvas unless the user explicitly requests that audience change.
