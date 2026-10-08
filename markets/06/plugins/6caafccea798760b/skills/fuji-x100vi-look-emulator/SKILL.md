---
name: fuji-x100vi-look-emulator
description: Use when the user asks to transform an image so it resembles a Fujifilm X100VI photograph while preserving the
  scene, composition, and subject identity.
---

# Fuji X100VI Look Emulator

## Host capability adaptation

1. **Native host capability:** when ChatGPT/Codex exposes a native tool or connected source that satisfies this task, use it.
2. **Original external runtime:** when the upstream runtime named by this skill is actually available, use it as documented below.
3. **Instruction-only fallback:** when neither is available, perform only the reasoning/instruction portion that remains valid, state the limitation, and never fabricate tool output, successful execution, or persisted state.

Use an equivalent native host capability when available; otherwise perform only the instruction-based portion and clearly disclose the unavailable runtime.

Use this skill only when there is an actual user-provided image available to edit. If the image target is missing, ask the user to upload or identify it before attempting any transformation.

## Core rule

Preserve composition, framing, geometry, perspective, subject placement, object placement, environment identity, and important readable text when possible. Do not redesign the scene or replace its identity.

## Scene modes

- `auto`: infer the most suitable profile from the scene.
- `indoor`: warmer practical-light rendering, softer highlights, deeper mood.
- `outdoor`: control harsh sunlight, reduce artificial greens, preserve believable daylight.
- `tabletop`: emphasize material texture, refined tonal separation, balanced warmth.
- `low_light`: preserve night mood, protect light sources, avoid aggressive denoising.

## Strength

- `subtle`: light intervention.
- `balanced`: default; visible but natural.
- `strong`: more pronounced treatment without sacrificing realism.

## Rendering direction

When the host provides **native image** editing or generation, use that capability to edit the supplied image. Aim for reduced smartphone HDR, deeper clean shadows, softer highlight roll-off, warm organic color, richer reds/oranges/wood tones, slightly subdued natural greens, less aggressive digital sharpening, organic microcontrast, subtle realistic texture or grain when appropriate, and lens-like photographic depth.

Do not apply a heavy fake-retro filter. Do not convert the image into an illustration. Do not invent unnecessary elements. Do not significantly alter people, objects, scene layout, or identity.

If native image editing is unavailable in the host, say that the image cannot be transformed in the current environment rather than pretending that an edit was performed.
