---
name: harmonize-palette
description: Diagnose and repair an existing color palette that feels clashing, muddy, repetitive, unbalanced, too warm or cool, or otherwise incoherent while preserving its intent and specified anchor colors. Use for making supplied colors more cohesive or revising a current palette. Do not trigger for creating a palette from scratch unless the user provides a clear starting palette.
---

# Harmonize a palette

## Diagnose before changing

1. Identify the supplied or current palette and any colors that must remain unchanged.
2. Infer the intended mood and use from the prompt. If neither is clear, optimize for general visual cohesion without pretending to know a specific application.
3. Locate the smallest set of problems: competing undertones, uneven lightness, excessive saturation, redundant hues, weak anchors, or an accent with the wrong visual weight.

## Revise conservatively

- Preserve anchor colors exactly unless the user permits changes.
- Change as few colors as needed. Prefer modest hue, saturation, or lightness adjustments over replacing the palette wholesale.
- Maintain useful separation between colors; harmony does not mean making every swatch similar.
- Preserve the requested temperature, energy, and contrast. When goals conflict, prioritize explicit user constraints and name the tradeoff.
- Do not claim accessibility based on harmony. Flag any intended text/background combinations for separate contrast checking.

## Show the revision

- Summarize the diagnosis and describe material changes with before-and-after hex values.
- Invoke `palette-picker` with the revised ordered uppercase `#RRGGBB` colors and a `reason` describing preserved anchors and the harmonization strategy.
- If multiple directions are equally valid, choose the best-supported one first rather than overcrowding one palette; mention that alternatives can be generated on request.

