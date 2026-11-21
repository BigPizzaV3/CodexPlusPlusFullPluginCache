# Typography production and QC

## Production order

1. Review the untouched Raw at natural speed and mute.
2. Compare every intended integrated keyword with the approved `typographyPlan`.
3. Keep generated typography only when all glyphs, order, timing, contrast, and meaning pass.
4. Repair the smallest possible surface using provider edit/remix, inpainting, tracked replacement, a perspective-aware typographic plate, or a native End Card.
5. Add captions only when the approved caption policy is `selective` or `full_accessibility`.

## Integrated-keyword PASS

PASS only when:

- the exact intended characters are present;
- the phrase is readable once at natural speed without pausing;
- it enters when the related visual event happens;
- contrast survives the mobile crop and platform overlays;
- its type, depth, material, lighting, occlusion, and motion belong to the scene;
- no accidental background text competes with it.

Wrong Japanese, partial glyphs, plausible-looking nonsense, or a phrase that needs freeze-frame reading is not a PASS.

## Repair routing

- Use `provider_edit` when the composition is excellent and only the generated letters are wrong.
- Use `tracked_in_world` when a stable surface can carry perspective, blur, grain, light, and occlusion convincingly.
- Use `native_end_card` for exact brand, CTA, price, legal copy, or a stable closing action.
- Use `selective_caption` only for silent comprehension or accessibility, not to compensate for a weak visual concept.
- Use `regenerate` when text is structurally fused into a broken picture or repair would cover a large fraction of the frame or timeline.

## Caption Taste gate

Reject a finish when captions:

- repeat every narrated sentence without a declared accessibility need;
- use a generic pill, thick outline, drop shadow, bounce, or bottom-center template unrelated to the film;
- obscure a face, product, causal action, generated hero typography, or platform UI;
- introduce a second visual language;
- force most of the viewer's attention away from the generated picture.

Approve captions when they are few, glance-readable, safe-zone aware, and visually derived from the film's existing type, palette, material, rhythm, and spatial logic.

## Required review record

Record `typographyReview` in `one-shot-review.json` with:

- `integratedKeywords`: `PASS`, `REPAIRABLE`, `FAIL`, or `NOT_APPLICABLE`;
- `exactSurfaces`: the same values;
- `captionTaste`: the same values;
- `cheapOverlayRisk`: boolean;
- `selectedRepairMode`: `none`, `provider_edit`, `tracked_in_world`, `native_end_card`, `selective_caption`, or `regenerate`;
- `notes`: the specific evidence.

`ACCEPT_PICTURE` requires all typography review fields to pass or be not applicable. `SURGICAL_FINISH` may use `REPAIRABLE`, but `cheapOverlayRisk` must remain false in the final QC.
