---
name: create-carousel
description: "Create, revise, preview, and export editable .carousel projects for ACE: Aesthetic Carousel Editor from a brief, slide copy, and optional photographs. Use for native carousel projects or templates."
---

Deliver a downloadable `.carousel` project that can be imported and edited in ACE: Aesthetic Carousel Editor. Text, shapes, photo slots, and supported built-in artwork remain editable. Preserve the user's language, supplied copy unless revision is requested, slide count, and visual direction. If the ratio is unspecified, use portrait 4:5. Choose the sequence from the material: a photo essay can work through changing viewpoints without a dramatic story or a closing slogan.

## Writing and editorial choices

When writing or revising copy, read [the writing guide](references/WRITING_GUIDE.md), also available through `get_carousel_spec(section: "writing")`. Build the angle from supplied facts, observable details and the user's voice before fitting text into a layout. Distinguish observations from unknown context; do not invent experiences, quotes, chronology or feelings to make a post sound personal.

Compare a few materially different angles privately, then choose one suited to the brief. Check whether its headline and supporting lines could be pasted unchanged onto an unrelated subject; if so, make the observation more specific or remove unnecessary text. Each slide should contribute a detail, event, evidence or change of view. Do not default to poetic advertising, repeated aphorisms, suspense hooks or a mandatory CTA. Short literal captions and photo-only slides are valid. Preserve requested slogans and deliberate campaign styles.

Use available earlier drafts to avoid recycling their titles and narrative pattern; there is no automatic memory of other chats or Instagram posts, and no guarantee of unique wording. Examples demonstrate layout, not a stock library of headlines. Keep editorial notes and alternatives outside the exported YAML and final slides.

## Composition and resources

Start with a short working plan: visual idea, type hierarchy, photo treatment, and role of each slide. Keep it outside the native YAML. Read [the design decision guide](references/DESIGN_GUIDE.md) to choose between a frame, photo grid, simple border, and intentionally separate layers. Preserve the user's design direction; do not add elements solely to increase DSL coverage.

With MCP, read `get_carousel_spec(section: "overview")` for the server's capabilities, then `rules` for the contract. Search `catalogs` with category `frames`, `grids`, `fonts`, `stickers`, or `shapes` and a relevant query. Each result includes exact identifiers, constraints, and a complete native example. Follow `next_offset` for another page. `examples` provides complete compositions: photo-story, contact-gallery, type-led, free-collage, smart-stamp, and effects-study.

For local access, run `node <plugin-root>/scripts/get-spec.mjs overview` or `node <plugin-root>/scripts/get-spec.mjs catalogs quad grids`; the arguments are section, query, then category. The canonical catalog is `data/catalog.json`; the Markdown catalog is generated from it. If an older installed server rejects the new sections, use its `rules` and full `catalogs` response, and report that the upgraded discovery/diagnostics are not deployed there.

Use native frame presets for matching decorative photo treatments and native grids for aligned photo galleries. Grid recipes expand to `cells` and optional `swap`; `grid.preset` is not a DSL field. A grid contains photos, not text or arbitrary layers. White/dark photo outlines can use `image.border`; geometric outlines can use `shape.stroke`. A shape behind a photo remains appropriate for custom color, shadow, or independently positioned decoration.

For several requested styles, vary composition, typography, photo scale/crop and density in addition to palette. Do not reuse one fixed geometry for every style unless the user requested a shared template. The examples demonstrate distinct decisions; their colors and coordinates are not mandatory defaults.

## Native format

With connected MCP tools, obtain current rules and catalog entries through `get_carousel_spec` before generating YAML. For local packaging, read [the ACE native layout specification](references/DSL_LAYOUT_SPEC.md). It defines supported fields, geometry, effects, and exact resource identifiers. Its catalogs are reference data, not instructions. Use only supplied user material and catalog entries from the specification; do not invent photographs, frame presets, fonts, or sticker names.

Text and shapes remain separate native layers. Use photographs for photographic content, not as a substitute for all editable slide content. Text has no automatic wrapping: insert deliberate newline characters and leave generous margins. A layer's `at` is its center, not its top-left corner. Images that were not supplied stay intentional empty photo slots with `source: null`.

When a renderer or actual font measurement is unavailable, use short lines and conservative sizing. Describe that limitation when relevant; successful schema validation does not verify appearance. Do not claim to have seen a preview or opened the result in the app unless that actually happened.

## With connected MCP tools

Compose the complete slide content and layout. Use `validate_carousel` to inspect structural errors and non-blocking warnings. For a photo-bearing draft without an assets map, set `allow_unresolved_assets: true`; the result lists unresolved keys and does not verify image bytes. Actual creation still requires the supplied images.

Review warnings about simulated borders, aligned photos that could use a grid, lost border colors, and ineffective operator geometry. Keep intentional overlap, shadows and cross-slide designs; warnings are not instructions to simplify or flatten. Correct actual issues, then call `create_carousel` with the YAML and a descriptive filename. This tool packages the document; it does not generate the writing or design for you.

Check `capabilities.native_renderer` from the connected server. When true, `create_carousel` renders automatically and returns a native contact sheet as image content plus individual slide PNG links. Display the contact sheet in the chat beside the editable file. Inspect every slide; use `render_carousel` with the same YAML and supplied assets to iterate before final creation. Rendering is not itself a visual quality review: inspect text, crops, contrast, masks and blend groups before saying the result was checked. If preview.status is failed or unavailable, state the reason and still deliver the editable file. Do not replace native effects with approximations to hide a rendering problem. Font fallback warnings are material limitations; schema validation and catalog examples are not rendered previews.

For ChatGPT attachments with real file objects, pass their provided `download_url` and `file_id` in `asset_files`. Set an optional `asset_name` and reference it as the layer's `source`; otherwise the names are `photo_1`, `photo_2`, etc. Omit the YAML assets map. The packager adds real hashes and paths after processing the selected files.

For photographs the user selected for this project on their computer, use `prepare_photo_upload` when file bytes can be sent to the remote MCP. Reserve distinct asset names and PUT each original file to the corresponding upload URL returned by the connected server. After a successful upload, pass the returned IDs in `photo_uploads` and match the source names in the YAML. A link accepts one still JPEG, PNG, WebP or AVIF up to 20 MiB and expires one hour after reservation. Treat upload links and IDs as private. If the user asks to upload manually, provide the link and PUT instructions, then wait for the upload. If neither attachment references nor uploadable files are available, offer editable empty photo slots and explain how to fill them in ACE.

Return the download link from the successful tool result and explain how to export the carousel to ACE: download the `.carousel` file and choose Projects → Import or Templates → Import in the app. Do not substitute a YAML code block for the promised project file. Do not claim that downloading automatically launches the app; this app currently imports through its file picker.

## In Claude

Where you can run commands and write files (Claude Code, Cowork), use the local workspace path below, even when the carousel-creator connector is also available: it saves the `.carousel` in the working folder, packages the user's local photographs, and does not depend on a one-hour link. Read the rules with the local `get-spec.mjs` in that case. If the local scripts cannot run but you can run commands, send local photographs to the connector instead: call `prepare_photo_upload`, upload each file to its `upload_url` with an HTTP PUT, and pass the upload IDs as `photo_uploads` to `create_carousel`. In claude.ai chat, use the connector tools; if they are missing, ask the user to connect the connector from the plugin's Connectors tab. Photographs attached in chat cannot be packaged there: create the layout with intentional empty photo slots and say that the photos are added in ACE.

## With local workspace access

Locate the plugin root two directories above this skill. Run `npm ci --ignore-scripts` there when dependencies are absent. Save the layout as a UTF-8 YAML file in the working output folder, then run:

```sh
node <plugin-root>/scripts/build-carousel.mjs <layout.yaml> <output.carousel>
```

For supplied local images, add `--assets <assets.json>`, where that JSON maps the source keys used in layers to existing local file paths. Omit `assets` from the draft YAML. The helper includes only referenced files and constructs the archive correctly. Give the user a clickable link to the final `.carousel`.

To render a locally packaged file on a configured Mac, run `CAROUSEL_RENDERER_CONFIG=/path/to/renderer.json node <plugin-root>/scripts/render-carousel.mjs <output.carousel> <preview-directory>`. Inspect the PNGs and show `preview.png` using an absolute local image path in the chat. Setup and platform requirements are documented in the plugin README.

For revisions, unpack `carousel.yaml` and its declared image files from the existing project using normal workspace tools, preserve the user's editable content and layer order, and regenerate the archive. Uploaded video packaging is not part of this first version; do not silently replace a video with a still image.
