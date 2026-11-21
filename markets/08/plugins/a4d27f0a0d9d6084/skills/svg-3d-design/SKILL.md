---
name: svg-3d-design
description: Use when a visual reference would improve an SVG illustration, custom icon or original 3D asset, or when creating functional 3D parts with dimensions, fit or parametric CAD.
---

# SVG & 3D Design

Start with the requested deliverable and the existing project. For custom icons or a family of icons, use the [icon guide](references/iconography.md) to choose the visual treatment and medium. Reuse an existing UI symbol when it fits.

- **SVG illustration or vector icon.** Build editable shapes, strokes and gradients. Choose the delivery dimensions before drawing. The uncompressed SVG must be no larger than its actual PNG export at those dimensions. Follow the [construction and export guide](references/svg-construction.md).
- **Visual 3D asset or rendered icon.** Prefer Blender unless the user specifies a tool. Model connected parts with real depth. Match the camera, materials and lighting, then inspect a second angle for floating parts, stretched textures or baked-in lighting. Bake procedural effects the export format cannot represent, then reopen it to check geometry and materials.
- **Functional part.** When dimensions, fit or motion define the object, follow [physical design](references/physical-design.md). Build directly from measurements when they specify the part. A sculpted figurine can stay in Blender and still use the [fabrication checks](references/physical-design.md#check-fabrication).
- **Raster image.** If the requested deliverable is a PNG or other bitmap and editable geometry is unnecessary, deliver the image directly.

## Develop a useful reference

Use the user's reference when supplied. For a photo of flat artwork, distinguish the design from the capture. Keep the object's bevels, contacts and material cues while removing paper edges and glare unless a literal facsimile is requested.

When a reference would resolve a visual choice, generate one at the level of detail the final medium can carry. For SVG, read [reference design](references/svg-reference-design.md) before generating. For Blender, choose a view that shows how the main parts connect. Keep the brief short. Use transparent backgrounds for cutouts and inspect their alpha on light and dark backgrounds before regenerating. Revise a generated reference when a consequential form or overlap is unclear. If a necessary reference is unavailable, ask for one.

## Build and compare

Start with silhouette, proportions and overlap. Build a defining feature in context before repeating the technique. Compare the actual render with the reference at matching scale and framing. For a reference-guided SVG, use the [fidelity rubric](references/svg-fidelity-rubric.md) to pick the first repair. A small prop, contact shadow or tapered line can explain the design more clearly than a large textured area.

Keep the last good render. Repair the feature that matters most, then recheck its neighbors and the whole asset at delivery size. Try a representative edit in the saved source. Deliver the requested asset and a useful preview, with any material limitation or unverified fit stated plainly.
