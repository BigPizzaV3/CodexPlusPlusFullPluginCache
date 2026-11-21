---
name: whiteboard-style
description: Style Whiteboard by Lumin drawings with Excalidraw's handwritten Excalifont, readable text, restrained color, and consistent strokes. Use for new diagrams or a requested visual polish; respect an existing board's style during small edits.
---

# Excalidraw style

Follow [Whiteboard operations](../whiteboard/SKILL.md) when writing a file. Use [Layout](../whiteboard-layout/SKILL.md) for spatial changes. Preserve the user's chosen palette and typography unless they ask for a redesign.

## Use the actual handwritten font

The bundled Excalidraw 0.18.1 uses `fontFamily: 5` for **Excalifont**, its current handwritten font. `1` is the older Virgil, `2` is Helvetica, and `3` is Cascadia. Use 5 by default for new diagrams; use a requested alternative deliberately. Set it on every text element and on every shape's `label`. This plugin's label conversion otherwise defaults to Helvetica. Setting a CSS font or only `appState.currentItemFontFamily` does not change existing element fonts.

For example, these editable skeletons set both kinds of text explicitly:

```json
[
  {"id":"title","type":"text","x":80,"y":40,"text":"From idea to draft","fontSize":32,"fontFamily":5,"strokeColor":"#1e1e1e"},
  {"id":"idea","type":"rectangle","x":80,"y":120,"width":240,"height":100,"strokeColor":"#1e1e1e","backgroundColor":"#dbeafe","fillStyle":"solid","strokeWidth":2,"roughness":1,"label":{"text":"Capture the idea","fontSize":22,"fontFamily":5}}
]
```

On a new board, `appState.currentItemFontFamily: 5` also makes subsequent manual text use Excalifont. Leave that preference alone on an existing board unless requested. Keep text editable; do not convert labels into images or outlines. Do not add a remote font service: the hosted editor supplies its own font assets.

## Keep the visual language small

Start with dark ink on a white or light canvas, a restrained accent, and pale fills. Use additional colors for actual categories or states, consistently across the drawing. Distinguish states with labels or shapes as well as color. Maintain strong text contrast in the current editor theme.

Use a short type scale: roughly 32 px for a title, 24 px for section headings, and 20–22 px for labels as a starting point. Make important ideas larger or give them space rather than making everything bold or brightly colored. Use approximately 2 px strokes and roughness 1 for a light hand-drawn feel; adapt to the user's style. Avoid decorative shadows, dense hatching behind text, and multiple competing accent treatments.

After changing a font, check wrapping, text dimensions, and bound label fit in the editor after fonts load. Increase container space before shrinking text. Finish by checking that the hierarchy remains clear at fit-to-content and text is readable at a useful viewing zoom. Report any unavailable visual verification rather than assuming font IDs alone prove the result.
