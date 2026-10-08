# Photoshop playbook

> **Observe, never assume.** Panel positions depend on workspace, version and screen size.
> These are landmarks to find, not coordinates to click. Trust the screenshot over this file.

## Landmarks

| Task | Look for |
|---|---|
| Place an asset | **File > Place Embedded** |
| Layers | The **Layers** panel, usually right side |
| Add a mask | The **Add layer mask** button at the bottom of the Layers panel |
| Type | The **T** tool in the toolbar |
| Adjustments | **Layer > New Adjustment Layer**, or the Adjustments panel |
| Save | **File > Save As** for the PSD |
| Export | **File > Export > Export As** for PNG/JPEG |

## Layer discipline

Build bottom to top, name as you go:

```
Type / CTA          <- editable type layer
Type / Headline     <- editable type layer
Adjust / Curves     <- adjustment layer, clipped if it should affect one layer
Subject             <- placed cutout, with a layer mask
Background          <- placed generated artwork
```

**Place Embedded, not Linked.** Linked breaks the moment the file moves.

Placed assets arrive as **Smart Objects** — leave them that way. Scaling a Smart Object is
non-destructive; scaling rasterized pixels is not.

## Masking

- Add a layer mask, then paint black to hide and white to reveal.
- **Never use the Eraser** on a layer you may need back.
- For a cutout from `remove_background`, the transparency usually suffices — add a mask
  only when the edge needs refinement.

## Type

1. Select the Type tool, drag a text box, type the real copy.
2. Set the face, size and tracking in the Character panel.
3. **Never rasterize** — the whole point is a later edit.
4. Each distinct piece of copy gets its **own layer**, so one can change without the others.

## Generating artwork that leaves room for type

Prompt for deliberate empty space where the copy will sit, and forbid rendered text:

`{subject}, {setting}, clean unbroken negative space across the {top third}, even lighting
in the empty area so text will read, commercial photography, no text, no letters, no
watermarks`

If the empty area comes back busy or dark where light type must sit, regenerate rather
than fighting it with layer effects.

## Saving and exporting

1. **File > Save As** → `.psd`, a **new filename**. Never overwrite the user's original.
2. **File > Export > Export As** → PNG or JPEG for the flat deliverable.
3. Confirm both landed before reporting. A started save is not a finished one.

## Verification checklist

- [ ] Every layer named
- [ ] Type layers still editable, not rasterized
- [ ] Masks used instead of erased pixels
- [ ] Placed assets still Smart Objects
- [ ] Original document untouched
- [ ] PSD and export both written to disk

## Known failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Edits can't be undone later | Rasterized type or erased pixels | Redo with type layers and masks |
| PSD opens with missing art | Place Linked instead of Embedded | Re-place embedded |
| Type unreadable | Busy artwork behind it | Regenerate with cleaner negative space |
| User's work lost | Saved over the original | Always Save As a new filename |
