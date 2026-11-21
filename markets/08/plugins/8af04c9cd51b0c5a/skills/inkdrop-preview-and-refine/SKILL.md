---
name: inkdrop-preview-and-refine
description: Show the real finished Inkdrop product mockup and refine it creatively through user-requested adjustments. Use when the user asks to see the result, compare requested variants, or change artwork, product options, or print scale and preview the update again.
---

# Show, refine, and show again

Make the finished product visible, then help the user improve it through focused creative changes. Explicit user instructions take priority over these defaults. A description of the result is not a substitute for the actual mockup.

## Show the actual end result

- After an authorized `apply_design` operation, follow that same operation with `get_operation` while pending, using its returned ID and supported timing. Do not start another render to check progress. Keep the user informed during a long wait. Stop on a terminal failure, cancellation, or a concrete blocker and report the actual state.
- Call a preview finished only after `READY` with a real mockup image. A receipt, a queued operation, and a standalone artwork image are not a finished product preview.
- Use the initiating card when it watches the exact workflow revision. For a direct creation or a later direct-chat edit without a newly reserved waiting card, call `get_preview` once with the new completed preview ID. An older card or an existing workflow ID alone does not mean the revised result is being displayed.
- Present the real mockup through the supported card or inline image surface, and include the exact returned preview link. If the host cannot display the image inline, provide the real image/preview link and say that inline display was unavailable. Never substitute an AI-imagined product, an older preview, or a fabricated URL.
- Briefly identify the relevant product and visible design choices. After an adjustment, say what changed and show the new version. Do not claim to have visually inspected an image that the host has not made available for inspection.

## Offer useful creative direction

Respond to what the user likes and dislikes. Preserve the successful elements and propose changes connected to their goal: a smaller graphic for a quieter look, a stronger contrast for readability, a more playful palette, or a simpler composition for clearer visual hierarchy. These are examples, not a mandatory style.

When the user is exploring, suggest up to two or three distinct directions in natural language, with the visual effect of each. Keep suggestions optional and brief. Do not turn every preview into a questionnaire or generate extra variants without a request. When the user has already specified the change, carry it out within the existing authorization instead of asking them to repeat it.

Distinguish recommendations from product capabilities. Use current catalog data for available colors, sizes, sides, and scale. If a requested placement or print technique is unsupported, explain what is available. Arbitrary movement on the garment is not established by a tool that exposes only print side and scale. Artwork composition can be edited when that matches the user's intent, but do not silently substitute it for unsupported placement controls.

## Make the requested adjustment

For artwork changes, keep the chosen product, variant, print side, and scale unless the user changes them. Use the standalone source, not a product mockup. Follow `inkdrop-transparent-artwork` when available for source preparation and image review. Otherwise follow the current Inkdrop edit-tool descriptions: reuse a fresh card reservation, or use `prepare_artwork_edit` for a direct-chat edit without one; preserve the exact reserved workflow pair. After the user explicitly continues with the finished edited image, import that new image and apply its new `artworkId`.

For product or scale changes, retain the intended artwork. Use the existing product card's supported adjustment flow or model-visible tools with verified current options. Do not call app-only state tools from the model or invent a guarded workflow revision. If the card must supply updated selection or request context, direct the user to those controls. Browse new products only when requested. A request to show a changed mockup establishes mockup intent; browsing alone does not.

Keep the media-sharing agreement required by Inkdrop intact; reuse it within the same ongoing workflow unless revoked. Reuse an unchanged original `sourcePreviewId` only when its artwork is still the intended artwork. Never use it as the result of a new edit. Start one render per requested change, with a stable idempotency key for identical retries. Honor cancellation through the supported cancellation flow without recreating canceled work.

## Close the loop

Follow the new operation to its real result and display the updated mockup again. If the user requested comparison, retain and clearly label the actual earlier and later images, or the explicitly requested variants. Otherwise focus on the latest result rather than accumulating duplicate cards.

If an edit or render fails, say so and keep the last successful preview clearly labeled as the previous version. Never present it as the requested update. Continue with further refinements when the user asks, and stop revising when they are satisfied. A successful preview or approval of its appearance does not place an order.
