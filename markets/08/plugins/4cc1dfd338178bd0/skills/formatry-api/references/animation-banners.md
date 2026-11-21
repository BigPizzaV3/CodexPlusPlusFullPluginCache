# Animated Banners

New creatives start as Images. To make an animated banner, read the current creative, call `formatry_set_studio_workspace_mode` with the canonical `set_workspace_mode` operation for `animation`, then call `formatry_set_studio_delivery_spec` with `set_delivery_spec`. Use `version: 2`, `kind: animation`, one of `webp-pack`, `gif-pack`, `mp4-pack`, and the complete `animation` settings required by that tool's current schema. Retain each returned revision. Use `formatry_set_studio_size_override` for an authorized per-size motion override. Read schemas rather than inventing fields; the legacy generic command is retained for raster compatibility, not Animation configuration.

Images and Animation share the design's canvas, text and assets while retaining independent output settings. Changing workspace alone does not configure the requested output; read back the active delivery kind, profile, timing and selected sizes before the exact-revision moving preview and export quote.

## Previewing and exporting animation

1. Preview the animation using `formatry_create_studio_animation_preview` at the exact saved revision. Animation returns a protected moving WebP. Inspect actual frames, including the reveal, readable hold and loop boundary.
2. Call `formatry_create_studio_export_quote` with the exact saved revision to quote the requested Animation delivery.
3. Show the server's quoted ordinary credit cost and funding source (`fundingSource: account_balance`). Animation exports use the ordinary account credit balance; the free-image allowance does not cover Animation.
4. After approval of that exact cost, call `formatry_confirm_credit_export` with matching `approvedUnits` and a stable idempotency key.
5. Wait for success with `formatry_wait_for_generation_job`, read the ready manifest with `formatry_get_artifact_manifest`, and save the actual requested WebP/GIF/MP4 through the normal file helper (or `formatry_download_artifact_file`). MP4 here is an Animation delivery format; it does not enable the separate Video workspace.

If the existing account balance cannot cover the quote, explain the insufficient balance. Do not display plans, promote upgrades, sell credits, create subscriptions, initiate checkout or link to transactional billing pages. Buying new access is not part of this plugin.
