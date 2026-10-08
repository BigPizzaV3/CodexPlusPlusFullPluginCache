---
name: extract-image-palette
description: Extract a purposeful editable color palette from an attached photo, logo, screenshot, artwork, mood board, or other visible reference. Use when users ask for colors from an image, a visual-reference palette, dominant or accent colors, or a palette inspired by an attachment. Do not trigger when no image is available or when the user wants the image edited rather than its colors analyzed.
---

# Extract a palette from an image

## Inspect the reference

1. Confirm that the target image is available in the conversation. If several images are present, infer the intended one from the prompt or ask which to use.
2. Analyze the visible image directly. Do not invent precision beyond what rendering, lighting, compression, or transparency permits.
3. Distinguish visually important colors from merely frequent pixels. Give weight to focal subjects, characteristic accents, and the user's intended use.

## Select colors

- Choose a compact set, normally five to eight colors, spanning dominant, supporting, neutral, dark, light, and accent roles where the image supports them.
- Merge colors that are perceptually redundant. Preserve a small but meaningful accent even when it occupies little area.
- Prefer representative, usable colors over noisy highlights, deep photographic shadows, anti-aliased edge pixels, or compression artifacts.
- If the user requests literal sampling, stay close to visible source colors. If they request inspiration, allow restrained adjustments for harmony and usability and say that the palette is interpretive.
- For multiple images, identify common threads instead of allocating an equal quota to every image.

## Deliver

- State whether the result is extracted closely or interpreted, and label the colors by visual role or source element.
- Invoke `palette-picker` with ordered uppercase `#RRGGBB` colors and a `reason` naming the reference and selection approach.
- Do not claim exact sampled pixel values unless a deterministic sampling tool actually supplied them.

