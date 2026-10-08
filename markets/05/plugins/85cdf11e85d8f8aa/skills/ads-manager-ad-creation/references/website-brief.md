# Website Brief Details

Use when the user supplies a website or product URL.

Extract factual proposals for:

- the product, service, or offer;
- the destination URL;
- a concise value proposition;
- likely audience or use context;
- one recommended direct public image URL, plus a small number of materially different alternatives only when useful;
- factual brand, product, and visual constraints.

For image discovery, call `scrape_website_ad_images(website_url)` when available. It returns at most one best-effort source image URL and does not require an ad account. An empty `images` list means discovery produced no image, not that the website has no suitable images. If it is empty or the tool is unavailable, use other available browsing or search, or explain the limitation to the user. If the call fails, report the discovery failure and offer the same alternatives; do not describe an error as an empty successful result.

Inspect the returned candidate. If `chat_card` copy and a valid destination are already ready, call `preview_ad` with that copy and destination and the returned `image_url` as `creative.image_url`. Show the unsaved ad preview and ask the user to approve the image there; no separate image approval is needed before this candidate preview. Follow the existing campaign-panel handoff for an open campaign plan. If the copy is not ready or the preview tool is unavailable, show the candidate and source URL in chat. Keep image approval and the normal write confirmation before any upload or ad creation.

When using other browsing or search, inspect visible product or hero images, public image metadata such as `og:image`, and directly linked same-origin image assets. Prefer a direct public HTTP(S) image URL where the approved product, service, or offer is recognizable, prominent, unclipped, and not embedded in browser UI, a platform mockup, a CTA, a price badge, or an invented claim. Do not silently select or upload it: show the exact recommended candidate and source URL and ask the user to approve it.
