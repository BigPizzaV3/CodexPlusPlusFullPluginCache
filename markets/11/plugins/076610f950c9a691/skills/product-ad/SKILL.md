---
name: product-ad
description: Create a poster, ad, banner, social image or image-generation composition based on the current Artboard canvas, mockup, scene, 3D model or animation frame. Export the real canvas and preserve its artwork, colors, geometry and view while generating its surroundings.
---

# Creative built around the actual Artboard canvas

Use this workflow whenever the user says "use this", "based on my canvas", "make a
poster/banner/ad" or asks the ChatGPT image model to build on an Artboard project.
An image model can redraw even an attached reference. A preservation prompt alone
cannot guarantee fidelity. The final product layer must come from Artboard's export.

## Keep the user's current work

1. Reuse the active project's latest `editor_context`; call `get_open_project`.
   Do not search for a replacement, reopen a different product, ask for the logo
   again, reset the background/aspect ratio, or change a 3D pose/keyframes merely
   to make an ad. If no current project is known, use the project's exact openPath.
   Only create a new project when the user asks for one.
2. Finish only requested edits. For an existing 3D view or animation, preserve its
   current camera, pose and frame; export a still PNG rather than a video for an ad.
3. Call `export_project` explicitly with `format: "png"` after the latest edits.
   Wait with `check_export` if needed. Retain the completed result's `sourceExportId`.
   A pending command's `export_id` is a different identifier. Never use a catalog
   thumbnail, editor screenshot, old export or small JPEG preview as the final source.

## Give the image model the actual reference

4. `originalReference.availableInToolResult: true` means the assistant can inspect
   the actual full-resolution PNG. It DOES NOT mean the image-generation tool has
   received an image input. Never infer a generator reference ID from an MCP image,
   a file name, `sourceExportId`, base64 text, or a URL mentioned in the prompt.
   If `hostImageReference` is returned, the exact bytes have been uploaded as a
   ChatGPT file and its file ID registered as image context for the NEXT user message.
   Wait for that message. Likewise, a composer attachment arrives only after sending.
   If it has not arrived, say: "The exact canvas image
   is attached below. Send it with 'continue' and I'll build the poster around it."
   Stop until the original attachment arrives. If sharing was unavailable or the
   image exceeded the host attachment limit, obtain the original from the download
   link through an available file tool, or ask the user to attach that downloaded PNG.
   Do not start generation from a preview while waiting for the original. Before
   generation, verify the received image visually matches the canvas's actual artwork
   and product. If the generator's supported image-input mechanism cannot accept that
   real file/image reference, stop and explain the missing handoff. A plausible
   generated garment is not evidence that the reference was supplied.
5. Use ChatGPT's image-generation tool with that actual PNG as an image input, using
   its supported reference-image mechanism. Merely mentioning a file name or URL in
   the prompt is not supplying the image. Include this preservation instruction:

   "Generate a BACKGROUND AND TYPOGRAPHY ONLY. The attached PNG is the authoritative
   product reference for a separate protected layer that Artboard adds afterward.
   Use it only to coordinate palette and spacing. Your generated output must contain
   ZERO garments, devices, product photography, copied products, logos or printed
   artwork, anywhere. Do not render the reference product in the background.
   Leave the specified product rectangle empty; keep all typography outside it.
   Artboard will place the original canvas in that rectangle afterward, preserving
   its silhouette, proportions, material, seams, zippers, folds, shadows, colors,
   logo, artwork, screen content, camera angle and pose."

6. Plan the output size and empty rectangle before generation. Reserve enough space
   for the original canvas at its existing aspect ratio. Match the generated
   background's aspect ratio to the output. Headline and CTA must stay outside the
   rectangle. The complete source canvas, including its background, is retained:
   use it as an intentional image panel when opaque; transparent pixels reveal the
   new background. Never silently remove the original background or cut out the product.
   Inspect the generated background before composition. For a solid product panel,
   use `panel_background` (e.g. `#ffffff` for a white panel). Artboard clears ALL
   generated content inside that reserved rectangle before placing the original,
   including margins outside its aspect-fit bounds. A generated placeholder entirely
   within that panel will be removed and need not trigger repeated generation.
   Reject invented products/logos OUTSIDE the cleared panel. Without a solid panel,
   reject any visible duplicate. Do not run endless retries asking the generator to
   erase a reference product; use the compositor's real original layer instead.

## Finish with the original layer

7. Call `compose_product_ad` with the fresh `source_export_id`, the generated
   background's actual image/file reference, output width/height, and placement
   `{x, y, width, height}`, plus `panel_background` when the planned panel is solid.
   This works through Artboard in Chat; no local code or
   mandatory Work handoff is needed. The source is fitted without cropping or
   stretching, with uniform scaling when necessary. Do not place the generated
   background on the logo surface or mutate the original project.
8. If composition is rendering, use `check_export`. Show the composed Artboard
   download, not the raw generated background. Inspect the result against the source:
   garment/3D geometry, logo/artwork, color, pose, complete framing, and text layout.
   Also check the entire image for an unwanted second product or invented logo. Open
   the completed composition for inspection; never mistake the native image-generation
   preview for the final composed output. Artboard opens its existing Preview dialog
   with the exact composed PNG and Download. Identify that Preview as the final output;
   native image-generation variations are intermediate and can be wrong. Do not label
   a native variation as the finished ad or claim it was replaced in ChatGPT's gallery.
   Correct a failed visual check before presenting the final ad.
   Say "original render preserved" only after composition succeeds. Say "pixel
   identical" only if an unscaled opaque source region was actually compared.

If the image-generation tool or generated image's file reference is unavailable,
say precisely which step is blocked. Keep the export available and resume from it
once the reference is accessible. Do not substitute a generated product, promise
exact preservation from prompting, or silently switch to Work. Respect the user's
choice to stay in Chat; a host-proposed handoff is optional when these tools suffice.

## Natural editing before composition
Apply every requested edit to the actual canvas first, through the design tools and current live selection/state. A logo placement, surface recolor or timeline change is not an image-generation request. Export the current real canvas only after those edits render. Native host download and the editor's Download action are preferred to asking the user to copy a URL. Keep the original export reference and use the existing protected-layer composition workflow for an explicitly requested generated surrounding design.


Native edits now return real rendered visual feedback. Inspect it before claiming
success; `inspect_project` captures a read-only frame without an export allowance.
Use a new `begin_project_edit` group for a multi-tool user request, and pass its
`history_group` so one undo restores that request. All three editors support
recorded native undo/redo across reopening. Exports have a persistent Download control for the original rendered file. Existing artwork placement remains a real editor
operation; native AI generation is for explicitly requested creative assets only.
