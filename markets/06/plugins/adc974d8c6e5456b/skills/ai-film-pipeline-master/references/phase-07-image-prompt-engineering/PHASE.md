---
name: phase-07-image-prompt-engineering
description: "Phase 7: Image Prompt Engineering & Visual Canon. Directs 7-slot universal image prompt construction, frozen identity sentences, optical lens physics, lighting styles, and the complete Mesopotamia Canon across 889 standardized craft cards, the Mesopotamia Canon included. Use when generating still keyframes, concept art plates, character model sheets, or Midjourney/Flux visual prompts. Trigger on: image prompt, keyframe prompt, Midjourney prompt, Flux prompt, character sheet, frozen identity, برومت صور، توليد صور، كي فريم، تصميم شخصية، مكنون بلاد الرافدين، صورة سينمائية."
---

# Phase 7: Image Prompt Engineering & Keyframe Synthesis

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

Phase 7 provides the comprehensive creative, optical, and technical framework for transforming visual storyboards (Phase 6), character continuity records, and production design rules into high-fidelity, model-ready **Image Prompts**. It enforces the 7-Slot Universal Prompt Syntax Order, eliminates quality buzzword pollution, provides reference turnaround sheet templates, and integrates the complete Mesopotamia Canon for ancient Near Eastern historical accuracy.

---


<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The contract for this phase](#the-contract-for-this-phase)
- [Before the first prompt](#before-the-first-prompt)
- [When to Use This Skill](#when-to-use-this-skill)
- [The Knowledge Base (889 Craft Cards)](#the-knowledge-base-889-craft-cards)
- [Operational Execution Pipeline](#operational-execution-pipeline)
- [Reference Navigation](#reference-navigation)
- [Files in this phase](#files-in-this-phase)

<!-- /GENERATED:toc -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `render_mode`, `looks`, `forbidden_global`, `engine_record` |
| **One-of read groups** | `shot_table` or `still_brief` or `story_brief` |
| **Optional reads** | `branch_map`, `size_angle`, `panels`, `blocking`, `composition`, `durations`, `mode` |
| **External inputs allowed** | `still_brief`, `story_brief`, `branch_map`, `shot_table`, `size_angle`, `panels`, `blocking`, `composition` |
| **Writes** | `frozen_sentence`, `frozen_sentence_status`, `palette`, `keyframe_prompts` |
| **May not re-decide** | `branch_map`, `shot_table`, `size_angle`, `render_mode`, `looks`, `durations`, `panels` |
| **Execution gate** | `paid_generation_approved_by` |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `narrated_documentary` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `music_video` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `commercial` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `commercial_narrated` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `storyboard_only` | `phase-06-storyboard-layout` | `delivery / edit` |
| `one_still` | `phase-01-story-generation` | `delivery / edit` |
| `audio_with_cover` | `phase-04-audio-narration` | `delivery / edit` |
| `interactive_branching_silent` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `interactive_branching_audio` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |
| `data_led_built` | `phase-06-storyboard-layout` | `phase-08-video-prompt-engineering` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

---

## Before the first prompt

This phase needs the engine record from [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) — the native tile, the
clip ceiling, whether an end frame is accepted. Fill it at the start of the project. If it is not
filled, write the prompt in full anyway and mark the resolution and clip-length cells
`pending_engine_check`. **A limit is a reason to change the engine, not the shot.**

---

## When to Use This Skill

Activate `phase-07-image-prompt-engineering` whenever a project requires:
1. Formulating self-contained, model-ready textual prompts for AI image generators (the engine the project's record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) names).
2. Generating master reference sheets: Character Model Turnarounds (`sheet-character.md`), Location Environment Plates (`sheet-location.md`), or a Props & Set-Dressing Sheet for a location (`sheet-props.md`; a single recurring object uses `ident.object_card`).
3. Conditioning Start-Frame and End-Frame image pairs for downstream video diffusion interpolation (Phase 8).
4. Engineering realistic optical camera parameters (anamorphic vs spherical lenses, f-stops, depth of field, optical breathing).
5. Directing professional lighting architectures (Key/fill ratios, Kelvin color temperatures, Rembrandt, chiaroscuro, volumetric god rays).
6. Conditioning historically authentic Mesopotamian, Assyrian, Babylonian, or Sumerian visuals using the integrated `mesopotamia-canon`.

---

## The Knowledge Base (889 Craft Cards)

The phase count in the heading above covers **this folder and the Mesopotamia Canon together**. The
canon lives in [`./mesopotamia-canon/`](./mesopotamia-canon/) and is indexed separately, because it has
its own router and its own audience, so **the generated file registry further down this page counts
only this folder** and states the canon's share beside it. Where the two numbers differ, the
difference is the canon — it is not drift, and both are measured from the cards on every build.

*(No card count is typed by hand on this page. The first draft of this paragraph spelled all three
figures out, and they were stale one build later, which is the defect this note exists to explain.)*

1. **[lighting.md](./lighting.md)** (90 cards): Key/fill ratios, Rembrandt, volumetrics, golden hour, chiaroscuro, neon noir, candlelit intimate.
2. **[image-format-texture.md](./image-format-texture.md)** (64 cards): 35mm film grain, 70mm IMAX clarity, medium format, wet plate collodion, halation.
3. **[anime-2d.md](./anime-2d.md)** (59 cards): Cel-shading, line weight, sakuga animation keys, background art, mecha mechanics.
4. **[colour-grading.md](./colour-grading.md)** (58 cards): Teal-orange split, bleach bypass, 3-strip Technicolor, Kodak Vision3 250D/500T.
5. **[lens-focus-depth.md](./lens-focus-depth.md)** (53 cards): Anamorphic oval bokeh, Cooke prime character, shallow DOF, macro, tilt-shift.
6. **[cg-vfx.md](./cg-vfx.md)** (32 cards): Subsurface scattering, fluid dynamics, particles, procedural volumetrics.
7. **[vertical-short-form.md](./vertical-short-form.md)** (25 cards): 9:16 vertical composition, safe areas, hero framing, mobile retention.
8. **[still-photography.md](./still-photography.md)** (18 cards): Studio strobes, beauty dish diffusion, butterfly lighting, environmental portraits.
9. **[render-style.md](./render-style.md)** (19 cards): Oil painting impasto, charcoal sketches, watercolor washes, woodcut prints.
10. **[kids-content.md](./kids-content.md)** (16 cards): Children's visual clarity, joyful saturated palettes, non-threatening silhouettes.
11. **[still-life-product.md](./still-life-product.md)** (16 cards): Commercial tabletop staging, rim lighting on glass, micro-refractions, droplets.
12. **[materials-surfaces.md](./materials-surfaces.md)** (16 cards): Weathered bronze patina, hammered gold, raw linen, wet asphalt.
13. **[pose-static.md](./pose-static.md)** (16 cards): Heroic contrapposto, royal enthroned posture, dynamic tension hold.
14. **[reference-roles.md](./reference-roles.md)** (16 cards): IP-Adapter face conditioning, ControlNet depth/canny guides, style weights.
15. **[documentary.md](./documentary.md)** (15 cards): Observational realism, historical authenticity, unposed field photography.
16. **[identity-consistency.md](./identity-consistency.md)** (14 cards): Frozen character sentence, turnaround models, face anchor preservation.
17. **[music-video.md](./music-video.md)** (14 cards): Stylized visual hooks, performance lighting, rhythmic visual motifs.
18. **[ads-trailers.md](./ads-trailers.md)** (13 cards): Commercial hero framing, packshots, key art, high-impact billboard lighting.
19. **[keyframe-craft.md](./keyframe-craft.md)** (14 cards): Video-ready keyframes, motion reserves, start/end frame alignment.
20. **[retouching.md](./retouching.md)** (13 cards): Frequency separation, dodge & burn, digital cleanup, skin texture preservation.
21. **[in-frame-text.md](./in-frame-text.md)** (16 cards): Ancient cuneiform wedge incisions, stone engravings, neon signage.
22. **[print-delivery.md](./print-delivery.md)** (13 cards): resolution computed from physical size and viewing distance rather than from a default, colour spaces and gamut, bleed and trim, stock, proofing, fixed-panel and projection surfaces, finishes and lifespan.
23. **[restoration.md](./restoration.md)** (10 cards): Archival historical photograph repair, scratch removal, chemical silvering recovery.
24. **[failure-modes.md](./failure-modes.md)** (10 cards): Anatomy hallucinations, extra limbs, plastic skin, buzzword contamination.
25. **[data-visualisation.md](./data-visualisation.md)** (17 cards): Charts, maps and counters as the picture — chart choice, zero baselines, animated change, uncertainty, and why a chart is built rather than generated.

### Master Templates & Directorial Guides:
- **[how-to-write-an-image-prompt.md](./how-to-write-an-image-prompt.md)**: The 9 Laws of Image Prompting & 7-Slot Universal Syntax Guide.
- **[sheet-character.md](./sheet-character.md)**: Master Character Turnaround Sheet layout & prompt template.
- **[sheet-location.md](./sheet-location.md)**: Master Location Environment Plate layout & prompt template.
- **[sheet-props.md](./sheet-props.md)**: Props & Set-Dressing Sheet (one location's objects) layout & prompt template.
- **[still-image-design-record.md](./still-image-design-record.md)**: Still-Image Design Record & Continuity Lock.

### Mesopotamia Historical & Cultural Canon:
- **[mesopotamia-canon/canon-rules.md](./mesopotamia-canon/canon-rules.md)**: The 330 BC Hellenistic cutoff, house canon authority, verbatim quotation mandate, and canon scope.
- **[mesopotamia-canon/INDEX.md](./mesopotamia-canon/INDEX.md)** and **[mesopotamia-canon/CANON-LOOKUP.md](./mesopotamia-canon/CANON-LOOKUP.md)**: the canon's routers — `INDEX.md` takes a period or a date to the right file in one hop, and `CANON-LOOKUP.md` is the id table, searched rather than read. Open them before any canon file.
- **mesopotamia-canon/`clothing-01` … `clothing-11`**: The wardrobe (its garment count is generated on `clothing-00-about.md`) — royal garments, beards, crowns, hairstyles, authentic footwear, shawls, jewelry — one file per Part.
- **mesopotamia-canon/`grimoire-01` … `grimoire-20`**: The architectural and material encyclopedia (ziggurats, gates, weapons) — one file per civilisation.
- **[mesopotamia-canon/heritage-rules.md](./mesopotamia-canon/heritage-rules.md)**: Modern cultural flags, authentic faces, and non-destructive subtitle rules.

---

## Operational Execution Pipeline

### Phase Inputs & Continuity Producers
- Visual Storyboard Layout & Panel Breakdown (from Phase 6).
- Character Continuity Locks & Verbatim Sentences: produced at the Phase 6 → 7 boundary via **[identity-consistency.md:ident.frozen_sentence](./identity-consistency.md)** and **[sheet-character.md](./sheet-character.md)**.
- World Environment & 3 Locked Palette Hex Tones: produced via **[sheet-location.md](./sheet-location.md)** and Phase 6 Color Script (**[storyboard-deck-template.md](../phase-06-storyboard-layout/storyboard-deck-template.md)**).
- Mesopotamia Historical Canon (when applicable, pre-330 BC).

### Phase Outputs
1. **Master Character / Location / Prop Reference Sheets**: Generated turnaround plates ensuring downstream model consistency.
2. **Production Keyframe Stills**: High-resolution, self-contained prompts formatted in the 7-Slot Universal Order.
3. **Dual-Frame Conditioning Pairs**: Paired Start Frames and End Frames for video interpolation engines.
4. **Targeted Negative Exclusions**: Focused negative prompt blocks of 15 to 30 words per risk class, mitigating specific shot risks.

---

## Reference Navigation
- **[HOW-PHASE-7-WORKS.md](./HOW-PHASE-7-WORKS.md)**: Deep operational walkthrough, 7-slot syntax compiler, and Phase 8 handoff.
- **[INDEX.md](./INDEX.md)**: Complete catalog of the craft cards in this folder, with the templates and the module list. The canon has its own index in [`./mesopotamia-canon/`](./mesopotamia-canon/); every id in the package, from either, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).
- **[LOOKUP.md](./LOOKUP.md)**: Master ID lookup table for fast card retrieval.

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**34 craft files, 674 cards** in this phase directory, every one linked below, so nothing is more than one hop away. A further **215** are in [`mesopotamia-canon/`](mesopotamia-canon/), which has its own index because it has its own audience. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md). Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`lighting.md`](lighting.md) | **Lighting** — Lighting Architecture, Contrast & Kelvin Physics <br>*Cards scoped to: any format* | 90 |
| [`image-format-texture.md`](image-format-texture.md) | **Image Format and Texture** — Image Formats, Film Stocks & Sensor Textures <br>*Cards scoped to: any format* | 64 |
| [`anime-2d.md`](anime-2d.md) | **Anime and 2D Animation Techniques** — 2D Anime, Cel Animation & Stylized Renderings <br>*Cards scoped to: any format* | 59 |
| [`colour-grading.md`](colour-grading.md) | **Colour and Grading** — Colour Palettes, Contrast Ratios & Cinema Grades <br>*Cards scoped to: any format* | 58 |
| [`lens-focus-depth.md`](lens-focus-depth.md) | **Lens, Focus and Depth** — Optical Lenses, Apertures & Depth of Field <br>*Cards scoped to: any format* | 53 |
| [`cg-vfx.md`](cg-vfx.md) | **3D CG, VFX and Virtual Production** — CGI, Visual Effects & Volumetric Simulations <br>*Cards scoped to: any format* | 32 |
| [`vertical-short-form.md`](vertical-short-form.md) | **Vertical Short-Form** — Vertical Short-Form Composition (9:16 Reels/Shorts) <br>*Cards scoped to: mostly Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Commercial / TVC, Vlog / YouTube Long-Form, among 22 formats* | 25 |
| [`still-photography.md`](still-photography.md) | **Still Photography and Static Visual Arts** — Studio & Commercial Still Photography <br>*Cards scoped to: any format* | 18 |
| [`render-style.md`](render-style.md) | **Medium, Style and Render Register** — Fine Art, Traditional Painting & Illustration Styles <br>*Cards scoped to: any format* | 19 |
| [`kids-content.md`](kids-content.md) | **Kids Content** — Children Content, High Clarity & Joyful Aesthetics <br>*Cards scoped to: mostly 2D Animation (Western / Cartoon), Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, among 10 formats* | 16 |
| [`still-life-product.md`](still-life-product.md) | **Still-Life, Product and Set Staging** — Product Photography & Macro Tabletop Staging <br>*Cards scoped to: any format* | 16 |
| [`materials-surfaces.md`](materials-surfaces.md) | **Materials and Surface Physics** — Surface Physics, Textures & Material Shaders <br>*Cards scoped to: any format* | 16 |
| [`pose-static.md`](pose-static.md) | **Pose and Static Performance** — Static Posing, Weight Distribution & Body Silhouette <br>*Cards scoped to: any format* | 16 |
| [`reference-roles.md`](reference-roles.md) | **Reference Roles and Multi-Reference Assembly** — Reference Image Routing & Multimodal Control Weights <br>*Cards scoped to: any format* | 16 |
| [`documentary.md`](documentary.md) | **Documentary, Interview and Reportage** — Documentary Realism, Archival & Observational Stills <br>*Cards scoped to: mostly Documentary Feature, Video Essay, Documentary Series, News Report / Reportage, among 26 formats* | 15 |
| [`identity-consistency.md`](identity-consistency.md) | **Identity Consistency Across Images** — Character Identity Consistency Across Generations <br>*Cards scoped to: mostly Character Sheet / Turnaround, Documentary Photography, Editorial / Magazine Image, Event Photography, among 23 formats* | 14 |
| [`music-video.md`](music-video.md) | **Music Video and Performance** — Music Video Keyframes & Rhythmic Stylization <br>*Cards scoped to: mostly Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Concert / Live Event, among 18 formats* | 14 |
| [`ads-trailers.md`](ads-trailers.md) | **Ads, Trailers and Motion Design** — Advertising, Key Art & High-Impact Promo Stills <br>*Cards scoped to: mostly Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Explainer, among 22 formats* | 13 |
| [`keyframe-craft.md`](keyframe-craft.md) | **Keyframe Craft, Single and Paired** — Keyframe Extraction & Motion-Ready Composition <br>*Cards scoped to: any format* | 14 |
| [`retouching.md`](retouching.md) | **Retouching and Post-Capture Treatment** — High-End Retouching & Clean Plate Inpainting <br>*Cards scoped to: any format* | 13 |
| [`in-frame-text.md`](in-frame-text.md) | **In-Frame Text and Typography** — In-Frame Typography, Ancient Glyphs & Signage <br>*Cards scoped to: any format* | 16 |
| [`print-delivery.md`](print-delivery.md) | **Print and Physical Delivery** — High-Resolution Print Delivery & Aspect Scaling <br>*Cards scoped to: mostly Poster / Static Design, Editorial / Magazine Image, Fine Art Photography, Abstract Photography, among 23 formats* | 13 |
| [`restoration.md`](restoration.md) | **Correction, Restoration and Extension** — Historical Archive Restoration & Damage Recovery <br>*Cards scoped to: mostly Architectural Photography, Documentary Photography, Editorial / Magazine Image, Fine Art Photography, among 23 formats* | 10 |
| [`failure-modes.md`](failure-modes.md) | **Failure Modes and Rescues** — Visual Artifacts, Prompt Bloat & Model Failure Mitigation <br>*Cards scoped to: mostly Architectural Photography, Documentary Photography, Food Photography, Portrait Photography, among 25 formats* | 10 |
| [`data-visualisation.md`](data-visualisation.md) | **Data Visualisation and Information Graphics** — Designing the frame when the subject is a number <br>*Cards scoped to: mostly Explainer, Documentary Feature, News Report / Reportage, Vertical Short-Form (Reels, Shorts, TikTok), among 9 formats* | 17 |
| [`how-to-write-an-image-prompt.md`](how-to-write-an-image-prompt.md) | **How an image prompt is written** — How an image prompt is written — Every rule here is craft: what a generative model does with a prompt, and what it does with a careless one. | 22 |
| [`sheet-character.md`](sheet-character.md) | **CHARACTER SHEET TEXT-VISUAL TEMPLATE** — CHARACTER SHEET TEXT-VISUAL TEMPLATE — This is the **written/visual template** of the character sheet reference (Gilgamesh style). | 4 |
| [`still-image-design-record.md`](still-image-design-record.md) | **Still-image design record** — Still-image design record — What is decided about a frame, as opposed to a shot. This is the record behind every keyframe, reference sheet, poster and thumbnail, and it is filled b <br>*Cards scoped to: mostly Editorial / Magazine Image, Museum Installation, Podcast, Poster / Static Design, among 6 formats* | 1 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`sheet-location.md`](sheet-location.md) | LOCATION SHEET TEXT-VISUAL TEMPLATE — This is the **written/visual template** of the location sheet reference (Uruk Streets style). |
| [`sheet-props.md`](sheet-props.md) | PROPS / SET DRESSING SHEET TEXT-VISUAL TEMPLATE — This is the **written/visual template** of the props and set dressing sheet (Gilgamesh Palace style). |
| [`vlb-formats.md`](vlb-formats.md) | Formats — From the Visual Language Bible. Start from `../phase-03-shooting-script/vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, a |
| [`vlb-genres.md`](vlb-genres.md) | Genres — From the Visual Language Bible. Start from `../phase-03-shooting-script/vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, an |
| [`vlb-lens-focus-depth.md`](vlb-lens-focus-depth.md) | Lens, Focus and Depth — From the Visual Language Bible. Start from `../phase-03-shooting-script/vlb-decision-tables.md`: name the change you want in the scene, take the technique i |
| [`vlb-light-and-colour.md`](vlb-light-and-colour.md) | Light and Colour — From the Visual Language Bible. Start from `../phase-03-shooting-script/vlb-decision-tables.md`: name the change you want in the scene, take the technique it han |

<!-- /GENERATED:file-registry -->
