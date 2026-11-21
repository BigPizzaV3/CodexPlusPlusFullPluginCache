# Generative typography strategy

## Purpose

Make on-screen words feel native to the film without asking a video model to become a deterministic typesetter. Separate visual impact from exactness.

## Three text layers

### 1. Integrated generated keywords

Use for one to three short Hook, Reframe, offer, or Payoff phrases when the words should participate in the image.

- Keep each unit short enough to read in one glance, normally 24 characters or fewer.
- Describe scale, material, depth, entrance, occlusion, parallax, and relation to the causal event.
- Reserve negative space and contrast in the prompt.
- Let the model choreograph micro-motion while preserving copy order and meaning.
- Require natural-speed review of every glyph. Generated text is provisional until reviewed.

Examples of useful roles include a headline slamming down with a document, a keyword emerging from debris, or a promise locking into the final composition. Do not prescribe one recurring style.

### 2. Exact finishing surfaces

Use deterministic or reviewed provider-edit surfaces for brand names, CTA actions, prices, quantified claims, legal copy, and sourced proof. Prefer a native End Card, tracked replacement, inpainting, or a typographic plate that belongs to the scene. Avoid a flat box pasted over unrelated motion.

### 3. Captions

Use captions only when they materially improve silent comprehension or accessibility. Choose `none`, `selective`, or `full_accessibility` deliberately.

- Do not duplicate every narrated sentence by habit.
- Prefer selective emphasis of the few words that carry the turn.
- Match the generated film's type family, spacing, color, depth, and motion language.
- Keep captions out of faces, products, causal action, and platform UI zones.
- Reject generic pill boxes, thick outline wallpaper, and template subtitle motion when they lower perceived production value.

## Planning contract

Record `typographyPlan` in the One-shot brief:

- `strategy`: `integrated_keyword_first`, `exact_finish_first`, or `no_on_screen_text`;
- `integratedKeywords`: zero to three short copy units with semantic role and source references;
- `exactSurfaces`: the words that must be deterministic in final delivery;
- `captionPolicy`: `none`, `selective`, or `full_accessibility`, plus a reason;
- `fallback`: the repair path if generated typography fails.

`integrated_keyword_first` requires at least one integrated keyword. `no_on_screen_text` requires an empty integrated-keyword list. Keep CTA and other action-critical text in `exactSurfaces` unless the final surface is separately verified.

## Route effect

- Use `one_shot_first` when integrated keywords are short, non-regulated, and small deviations are repairable.
- Use `one_shot_plus_finish` when the generated picture and typography can own the look but exact brand/CTA surfaces need finishing.
- Use a controlled route when several exact sentences or documents must be read in sequence.

Do not downgrade a strong generated film into a generic caption template. If the required repair dominates the frame or most of the timeline, return to generation or concept routing.
