---
name: selling-slide-composition
description: "For a set of two or more marketplace slides that must read as one series: shared palette, lettering, label rhythm and grid, with each slide's layout following its purpose. Not needed for a single slide."
metadata:
  version: skill-render-ea6bd93365667f6d
---

# Selling slide composition

Composition follows the content of the specific slide, the marketplace's conditions and the
available visual material. Choose the structure and the number of text blocks for the current
task. In a set, the per-slide rules below apply to every slide, and the set rules keep the series
together.

## Attention hierarchy

Decide what the viewer should notice first, and build the other elements around that priority.
Choose the scale of the product, the text, the details and the free space by the slide's purpose
and the brief you were given.

## Where to put text

- Leave a clean field for the lettering: do not put text on a busy or occupied part of the photo,
  where it gets lost.
- Do not cover the product with text: lettering and labels go around the product, not over its
  key details (logo, shape, texture).
- Keep a safe margin from the edges of the frame, because the marketplace may crop the image or
  overlay its own UI.

## Text in the frame

Match the amount of text to the frame size and the confirmed capabilities of the model. Pass the
exact text and its role explicitly; if the brief is overloaded, suggest a suitable split without
changing the meaning.

## One style across the set

For a coherent series, set a shared visual direction and keep only the truly important traits:

- **palette** — consistent base and accent colors;
- **lettering character** — one tone for all the lettering (for example, a dense grotesque for
  the offer), described in words in the prompt rather than by picking a font in a builder;
- **label rhythm** — the same position and shape of the text labels from slide to slide;
- **composition grid** — the product and the text in similar zones on every slide of the set.

Vary the composition by each slide's purpose while keeping a recognizable link between the
slides.

## Adaptation

- Take the format and dimensions from the request, the marketplace's current requirements and the
  values the chosen model supports.
- When micro-parameters are missing, choose a consistent style from the product, the niche and the
  brand, and state the decisions you made.
- For text in the frame, choose the model by the current catalog and its confirmed ability to
  reproduce lettering.
