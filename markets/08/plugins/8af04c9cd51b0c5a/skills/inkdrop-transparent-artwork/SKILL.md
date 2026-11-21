---
name: inkdrop-transparent-artwork
description: Prepare standalone artwork with a transparent background before applying it to an Inkdrop product. Use for isolated print graphics, background removal, or correcting an unwanted rectangle in an Inkdrop mockup; preserve backgrounds the user intentionally wants printed.
---

# Prepare transparent Inkdrop artwork

Prepare the actual design image before importing or applying it. Explicit user instructions take priority over these defaults. This skill guides available image tools and Inkdrop tools; it does not itself remove backgrounds or create images.

## Choose the right source

- Use the user's intended standalone artwork. Preserve its subject, colors, lettering, composition, and details unless the requested edit changes them.
- For an existing Inkdrop preview, use `get_artwork_for_edit` when the original source needs identification. A shirt mockup, catalog photo, product-card screenshot, or flattened screenshot is not the original artwork.
- Preserve an already suitable transparent image instead of regenerating it. If multiple images could be intended, resolve which one before editing or importing.
- Prefer a transparent background for isolated logos, lettering, and illustrations intended to sit directly on the fabric. Preserve a requested photograph, poster rectangle, full scene, or intentional background. Ask only when removing the background would materially change an ambiguous design.

## Prepare and inspect the image

For new isolated artwork, request a standalone design on a genuinely transparent background using the host's available image tool. For an existing image, use an available editing or background-removal tool, retaining the original as the reference. Enable the tool's transparency option when available. Do not substitute a white canvas or a drawn checkerboard for transparency.

Remove only the unwanted background. Preserve white lettering, white illustration details, intentional outlines, internal shapes, and semitransparent effects that belong to the design. Keep edges clean, avoid clipping the subject, and preserve useful resolution and the intended aspect ratio. Do not add product photography, fabric textures, or decorative shadows to the artwork.

Prefer PNG with real alpha transparency. Inspect the finished image for missing details, changed spelling, opaque background remnants, halos, and excessive empty margins. If file inspection is available, verify that the intended background contains transparent pixels; an alpha channel alone is not proof. A checkerboard visible in an image is not proof either. Check against light and dark backgrounds when that inspection is available. Disclose any inability to verify transparency rather than claiming it is confirmed.

If the host cannot edit the actual source or return a usable transparent image, explain the limitation and request the original or an exported transparent PNG. Do not apply the old opaque image as though background removal succeeded. Do not claim the file meets a product's print requirements without checking its actual dimensions and the applicable product requirements.

Example editing brief:

> Remove only the unwanted background and return a transparent PNG. Preserve the design, exact lettering, colors, white ink details, and composition. Keep clean edges; do not add a shirt mockup, white rectangle, checkerboard pattern, or new elements.

## Continue to Inkdrop

Show the finished standalone artwork for review. When continuing into product selection, import, or an existing preview edit, follow [Inkdrop handoff](references/inkdrop-handoff.md). Use the current tools' schemas and returned state. A completed image edit alone does not authorize importing, applying, publishing, or ordering it.
