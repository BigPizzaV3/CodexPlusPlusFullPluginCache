# Choosing an editable composition

Before coordinates, decide the visual idea, type hierarchy, photo treatment and role of each slide. Keep this working plan outside carousel.yaml. Adapt to the user's supplied copy, references and existing design; do not require an approval step just to choose a layout.

When writing or revising copy, read `get_carousel_spec(section: "writing")` or `WRITING_GUIDE.md` beside this guide. Choose an angle grounded in supplied facts and visible details before layout. Avoid interchangeable mood slogans and invented personal stories. Each slide should add information or a new view; a photo-only slide is valid. Subtitles and footers are optional, not spaces that must be filled with extra slogans. Preserve exact copy when only layout was requested. Composition examples demonstrate geometry, not recommended wording.

Choose native elements by purpose:

| Purpose | Prefer | Important limits |
|---|---|---|
| Polaroid, film, stamp, torn-paper photo treatment | frame with a real catalog preset | Fixed aspect and window geometry; retain every photo slot |
| Aligned photo gallery or contact sheet | grid.cells from a complete grid recipe | Photos only; no text children, rotation or layer shadow |
| White or dark photo outline | image.border | Only FFFFFF and 1F1F1F survive editor save as intended |
| Geometric outline | shape with fill: null and stroke | Stroke extends outside the contour |
| Custom colored mat, shadow, independent tilted card | shape plus image when needed | Preserve the reason in the working plan; this can be a valid design |
| Freely overlapping photos with independent rotations | Separate image/frame layers | Do not force these into a grid |
| Double exposure with two photos sharing one crop | image.blend | Second source has no independent transform |
| Mix independently positioned photos or whole compositions | blender between groups | Region and layer order determine the operands; end the effect with a normal blender for an unaffected heading |
| Photograph or gradient inside letters/a silhouette | mask between stencil and texture | Texture is consumed; use a separate copy if it must also remain visible outside the mask |
| Mix a single photo, text block or shape with its backdrop | blendMode on that layer | Different mode list from blender; not available on every layer type |
| Type-led slide | Native text and appropriate shapes | A photo grid or decorative frame is optional |

A photo grid is not a typography grid. Plan text alignment, margins and rhythm independently. For frame or grid, obtain a complete catalog entry and ready coordinates before composing; never invent grid.preset. Use null for intentional empty photo slots, and real supplied asset keys otherwise.

When several visual styles are requested, vary composition, type hierarchy, photo scale/crop, density and decorative language. Palette changes alone do not establish distinct styles. Repeated brand templates and explicit user references take priority over novelty. Do not maximize layer-type counts or add effects merely to demonstrate DSL coverage.

Choose fonts from the actual catalog and consider their available weights and language coverage. Insert explicit line breaks. Actual font measurement is needed for reliable bounds; character-count estimates are not a verified layout.

Validate the document and review its warnings. A warning is a reason to inspect, not permission to flatten content or remove intentional overlap. Preserve legitimate shadows, rotated cards, panoramas, masks and cross-slide layers. Resolve missing assets before packaging; draft validation does not verify image bytes.

When capabilities.native_renderer is true, create_carousel returns native previews automatically. Show the returned contact-sheet image in chat and inspect all slides; render_carousel is available for iteration. Report preview failures explicitly. If an auxiliary renderer cannot handle a layer or font, report that limitation and retain the intended native content. Do not simplify the design merely to fit an incomplete preview. Structural validation and layout examples are not visual verification. Keep text and photo slots editable and inspect all rendered slides before claiming a visual check.
