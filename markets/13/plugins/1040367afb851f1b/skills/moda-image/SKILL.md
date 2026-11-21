---
name: moda-image
description: >-
  Generate, edit, outpaint, upscale or remove backgrounds from imagery inside an editable design. Requires an existing canvas shape. Shared prompt and model guidance; canvas-bound delivery. Metered.
---

# moda-image

**PREREQUISITE — `load_skill("moda-core")` once per session** (step-0, write
contract, free/metered map). Already loaded? Skip ahead. If you cannot load
it, the non-negotiables: call `moda_bootstrap` before anything; `brand_list`
before creating; revision-guarded writes use `expected_revision` from your last read.
`canvas_edit_image` captures its own target state and has no revision argument.
On `stale_revision`, re-read and retry once; send the canvas link
the moment it exists; stuck or failed? `ask_expert("<question>")` — free and
fast, never guess.

## When this skill owns the ask

Use this image craft alongside the format skill when a design needs generated or edited imagery. It operates on an existing canvas shape. Standalone image delivery is unavailable. Logo/mark design belongs to moda-social; keep brand marks and exact type editable.

## The operations

Create the layout and a neutral shape, read its node id, then call canvas_edit_image(canvas_ref, node, operation). The operation object selects kind=generate, edit, outpaint, remove_background or upscale. Generate/edit accepts prompt, model, reference_images and supported model controls. Edit and transforms use the target's current image. Generate defaults to the standard model. Call `load_skill("omni-and-media")` for the live model capability cards before choosing optional controls.

## Rules that make the call land

1. **Cards before knobs.** Load omni-and-media for live model capabilities. Copy supported ratios, resolution and model_params exactly.
2. **The prompt goes to the model VERBATIM** — nothing is added or rewritten.
   Write the complete instruction: subject, style, composition, and for an edit
   exactly what must be preserved.
3. **Source vs reference.** The target’s current image is the content being modified;
   `reference_images` steer style, palette or composition.
4. **Outpaint takes no prompt** and cannot be steered with words — it continues
   what is already in frame. Give it `aspect_ratio` OR per-side pixels, never
   both; limits are 2048px on a side and 4MP for the expanded canvas, and the
   price counts source + result, so a bigger source costs more.
5. **Look at the result with your own vision** before describing it. Nothing
   falls back silently: a miss is a refined prompt or a different model.
6. Brand in play? `brand_show(brand_kit_ref='[KIT]')`, then prompt to its
   palette and mood — the kit's colors, never hex from memory. Kit work
   itself: moda-brand.

## Delivering

The image call waits for placement; complete means the image is placed in the design. If it returns working or the connection times out, repeat the identical canvas_edit_image call to wait on the same job without requesting another generation. task_status is an optional recovery check. Inspect with canvas_screenshot, refine if needed, and deliver the canvas/editor link or requested design export.

Repeating an identical edit returns the earlier operation, including its completed result; a fresh repeat_token runs it again for a new charge. Reattachment receipts say whether the earlier result was returned or the existing work resumed. Resuming and placement recovery do not consume the new-generation rate limit.

If a paid image could not be placed, read the design and use operation.kind=retry_placement with operation.task_ref and the intended node on the same canvas. Choose the original element or a valid replacement if it was deleted. Omit repeat_token; recovery reuses the saved image without another generation charge and checks the destination before placement. Active and completed operations cannot be redirected. Paid results stay within this design workflow, with no standalone fallback delivery.



## Errors

Any typed error → moda-core's recovery reference. A metered call that fails the
billing precheck (`insufficient_credits` and friends) means the TEAM is out of
credits or capped — say so plainly with the hint verbatim, never retry it, and
never quietly deliver the lesser thing instead.

See also: moda-core — contract, routing ladder, everything Moda can do.

## References

| Doc | Load when |
|---|---|
| references/omni-and-media.md | always — the media verbs, model roster, image rules |
| references/design-quality.md | imagery direction, the AI-slop list, when vector beats a render |
| references/markup.md, references/edit-code.md, references/charts.md, references/gotchas.md | placing a result on a canvas; anything surprising |
