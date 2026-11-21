---
name: palette-extractor
description: "Extract and export sampled image palettes as CSS/GPL/JSON/PNG, inspect exact coordinate pixels and compare opaque black/white contrast ratios."
---

# Palette Extractor

Require one actual JPEG/PNG/WebP attachment or HTTPS image, at most 20 MB and 16 megapixels. Use extract for a read-only palette and create only when exports are requested. Choose 2–12 colors, default six, and alpha threshold 1–255, default 128. Explain that deterministic sampling uses at most 65536 pixels, quantized bins and eight weighted k-means iterations: swatches are approximate cluster means, not guaranteed exact source colors. Percentages describe included samples, not exact full-image area. Low-alpha samples are ignored, without compositing; GPL exports opaque 8-bit sRGB only. Use sample only with explicit zero-based x,y coordinates in the auto-oriented source; never invent the coordinate. RGB under alpha is not its displayed appearance on a background. Show actual swatches and flat opaque contrast ratios against pure black/white, without certifying brand identity, Pantone, full accessibility or real-world print color. Export real ZIP/CSS/GPL/PNG files and preserve the ZIP if optional standalone saves fail. Originals are processed without rehosting and export URLs are public. Reopen exact saved URLs instead of reprocessing. If tools are unavailable, report the missing connection rather than simulating findings.
