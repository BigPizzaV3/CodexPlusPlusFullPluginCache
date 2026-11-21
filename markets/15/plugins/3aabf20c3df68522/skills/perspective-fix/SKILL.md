---
name: perspective-fix
description: "Rectify an explicit planar quadrilateral in supplied artwork to chosen pixel dimensions, with annotated source corners, exact transform JSON and real PNG exports."
---

# Perspective Fix

Require an actual JPEG/PNG/WebP attachment or HTTPS source, at most 20 MB and 16 megapixels. Inspect actual auto-oriented source dimensions before choosing corners when needed. Require explicit zero-based x,y corners in order top-left, top-right, bottom-right, bottom-left and explicit output dimensions 64–2048 pixels per side. Clarify ambiguous corner order or intended ratio instead of silently choosing different geometry. Never infer calibrated physical dimensions from a photo. The tool rejects crossed, concave, out-of-bounds or degenerate corners rather than rearranging them. It uses a four-point homography and premultiplied-alpha bilinear interpolation, not an image generator. Output dimensions can magnify or stretch source pixels; never call this recovered detail or guaranteed true proportions. Show the actual corner-overlay preview and corrected PNG, plus transform JSON. Curved pages, lens distortion, hidden content recovery and OCR are unsupported. The annotated source preview and corrected copy are derived exports stored publicly; anyone holding their links can view them. The original file is read without rehosting. Preserve successful PNG and exact returned transformDocument if optional storage fails. Reopen actual saved URLs instead of resampling again. If connected tools are unavailable, report that instead of simulating results.
