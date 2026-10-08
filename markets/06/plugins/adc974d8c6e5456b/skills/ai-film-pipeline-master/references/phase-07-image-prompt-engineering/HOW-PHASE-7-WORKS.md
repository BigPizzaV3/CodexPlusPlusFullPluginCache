# How Phase 7 Works: Image Prompt Engineering & Keyframe Synthesis

Phase 7 translates the visual storyboard layout (from Phase 6), character identities, location designs, and historical canon rules into model-ready, self-contained **Image Prompts** for the image engine the project's record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) names.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Pipeline Position & Core Purpose](#1-pipeline-position-core-purpose)
- [2. The 9 Laws of Image Prompting (Never Broken)](#2-the-9-laws-of-image-prompting-never-broken)
- [3. The Seven-Slot Universal Syntax Order](#3-the-seven-slot-universal-syntax-order)
- [4. Master Reference Sheets](#4-master-reference-sheets)
- [5. Mesopotamia Historical Canon Integration](#5-mesopotamia-historical-canon-integration)
- [6. When the deliverable is one finished still](#6-when-the-deliverable-is-one-finished-still)
- [The craft files in this phase - 28 files, 674 cards](#the-craft-files-in-this-phase---28-files-674-cards)

<!-- /GENERATED:toc -->

## 1. Pipeline Position & Core Purpose

```
Phase 6: Storyboard Layout (194 cards)
   │ (Panel Compositions, Blocking, Framing, Animatic Timing)
   ▼
Phase 7: Image Prompt Engineering, plus the Mesopotamia Canon
   ├── The Seven-Slot Universal Prompt Order
   ├── Master Character, Location & Prop Reference Sheets
   ├── Dual-Frame Conditioning Keyframes (Start Frame & End Frame)
   └── Banishment of Quality Buzzwords & Optical Grounding
   ▼
Phase 8: Video Prompt Engineering (Temporal Motion, Camera Paths & Physics)
```

---

## 2. The 9 Laws of Image Prompting (Never Broken)

1. **Every Prompt Is Completely Self-Contained**: Generative vision models share zero conversational memory; each prompt must independently state subject identity, lighting, **the framing values for its render mode** (lens optics on photoreal and 3D work, the drawn equivalents on flat 2D — law 5 governs which), environment, and render style. *(This law enumerates what a prompt must carry, and enumerating "lens optics" flatly told a drawn piece to supply a value law 5 four lines below says it does not have. A law that lists required fields is a field list, and a field list branches.)*
2. **Prompts Enforce the Seven-Slot Universal Syntax Order**:
   `[Subject & Identity]` + `[Action & Pose]` + `[Framing, Elevation & Optics]` + `[Lighting Architecture]` + `[Environment & Palette]` + `[Surface Material Physics]` + `[Technical Specifications & Exclusions]`.
3. **Order Beats Length**: The head carries the immutable character lock; the tail carries affordable decorative detail that weak models may safely truncate.
4. **Mandatory Verbatim Character Sentences Are Immutable**: When character continuity is open, quote its frozen 30-to-45-word sentence verbatim in Slot 1. The sentence is explicitly produced at the Phase 6 → Phase 7 boundary via **[identity-consistency.md:ident.frozen_sentence](./identity-consistency.md)** and **[sheet-character.md](./sheet-character.md)**. If unspecified, apply the fallback in [how-to-write-an-image-prompt.md §4.11](./how-to-write-an-image-prompt.md). **The wardrobe line sits beside the sentence, never inside its 30 to 45 words**, and it is written only in image prompts and character-sheet prompts; a video prompt takes the wardrobe from the keyframe. **A shot that shows only part of a character** (hands only, from behind) **quotes only the parts that are visible** — the clauses of the sentence the frame shows, verbatim (build, skin, the age of the hands), and the wardrobe on them — **never the face clauses**; write `face out of frame`, and quote the whole sentence again the moment the face can be seen. Phase 8 applies the same rule to the clip ([`how-to-write-a-video-prompt.md`](../phase-08-video-prompt-engineering/how-to-write-a-video-prompt.md) §4.3).
5. **Banish Quality Buzzwords & Abstractions**: Terms like *"photorealistic"*, *"hyperrealistic"*, *"ultra detailed"*, *"8K"*, or *"cinematic"* pollute latent space and trigger plastic skin. Replace them with specific focal lengths (Panavision 55mm anamorphic T2.3) and physical lighting ratios. A camera body (ARRI Alexa 35, Hasselblad H6D) may be named as an optional texture reference, never as the replacement itself — the body is a reference for the grade, not a requirement, as Phase 3's lens column says. *(Animation Rule: On **flat 2D, cel-shaded or cartoon** projects, the render-style modules — [anime-2d.md](./anime-2d.md) for cel and anime (its vocabulary, not the words "anime style" on a piece that is not anime), [render-style.md](./render-style.md) for painterly and illustrative registers — replace **every optical and photographic value in this law and in law 8** — camera bodies, film stocks, sensor formats, focal lengths, apertures and f-stops, depth-of-field calls, and Kelvin colour temperatures — with explicit art styles, line weights, ink and colour treatments, a **drawn light direction stated in words** (key from upper frame-left, rim along the right shoulder), and a **palette temperature stated in words** (a warm amber key against cool blue shadow). None of the replaced values exists in flat animation: there is no lens to set an aperture on and no emitter to measure in Kelvin, so a number written there is a photographic instruction landing on line art. The requirement itself does not relax — the frame still declares where its light comes from and what colour it is; only the units change from measurements to described ones. **On 3D and rendered-CG work the optical values do apply** — focal length, aperture, depth of field, Kelvin — because there is a virtual camera with a real focal length behind the frame. That is the whole of the difference: this rule splits on whether there is a camera, not on whether the work is animated, and 3D animation has one. **Film stock, grain and gate artefacts are the exception within the exception.** A render has no film gate, so those are not properties of the medium there but effects added on top; take them when you want the shot to read as photographed and leave them out otherwise, and never let a default supply them. And a render's **surface** is a separate decision from its optics: state what the thing is made of — matte unglazed clay with visible thumb-marks, brushed anodised metal, felt — because a 3D prompt that specifies only the lens returns the default plastic-and-gloss look of the model, which is the single most common way a stylised render is destroyed. See law 8's negative tiers for the matching carve-out. **And a shot whose render mode is `built` takes none of this and never reaches a generator at all** — a chart, map, counter or diagram is assembled from real values as a graphics layer, so it has no lens, no art style and no surface, and a prompt written for it produces an invented chart with plausible wrong numbers on it (`dataviz.build_do_not_generate`).)*
6. **Negative Prompts Must Be Budgeted & Targeted**: Restrict negative exclusions to 15 to 30 words per risk class, targeted specifically to the shot's failure risks (Tier 0 is copied whole, outside the budget); never dump generic copy-paste blocks.
7. **Ratios Use the Verified Model's Native Generation Tile**: Never render a square image and crop. **The exact width and height come only from the dated record for the selected model in [ENGINE-CHECK.md](../ENGINE-CHECK.md)**; no dimensions are written into this file. If that record has not been filled, the prompt is written in full anyway and the resolution cell reads `pending_engine_check` (see [how-to-write-an-image-prompt.md](./how-to-write-an-image-prompt.md) law 7).
8. **Lighting Must Declare Motivated Origin & Kelvin Temperature**: State exact light source, angle, and color temperature (e.g., *5600K key from high camera left with 3200K warm tungsten bounce*). **Both of those figures, and every other one, come from `light.kelvin_reference` in [`lighting.md`](lighting.md)** - one number, one place, so a series does not drift. **Where the card's row gives a range, choose one figure inside it, record it under `decisions` in `project.yaml`, and hold it for the scene**; *exact* means one stated number, not the range. *(The Animation Rule in law 5 governs here too: on flat 2D, cel-shaded or cartoon work the Kelvin figure is replaced by the drawn light direction and the palette temperature in words — the origin and the angle are still declared, the number is not.)*
9. **Engine Choice and Spend**: This module engineers prompt strings and negative exclusions. The engine is the brief's; where the brief names none, the agent chooses the most suitable current one by the order in the root `SKILL.md` §0 and records it under `decisions` in `project.yaml`. Spend authorization belongs to the user spend gate (`paid_generation_approved_by`).

---

## 3. The Seven-Slot Universal Syntax Order

Every production keyframe prompt must be assembled strictly in this seven-slot sequence:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Slot 1: SUBJECT & IDENTITY LOCK                                                        │
│ Quoted frozen character sentence, anatomical features, age, facial structure, skin tone.│
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Slot 2: ACTION & POSE                                                                  │
│ Specific physical verbs, body orientation, hand gesture, eye gaze vector, expression.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Slot 3: FRAMING, ELEVATION & OPTICS (INHERITED FROM PHASE 3 & PHASE 6)                │
│ Transcribes [Inherited Shot Size] + [Inherited Angle] + Adds Optical Lens & F-Stop.   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Slot 4: LIGHTING ARCHITECTURE                                                          │
│ Key light angle, fill ratio, Kelvin color temperature, volumetric rays, shadow depth.  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Slot 5: ENVIRONMENT & PALETTE                                                          │
│ Architectural background, atmospheric weather, depth planes, 60:30:10 color palette.   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Slot 6: SURFACE MATERIAL PHYSICS                                                       │
│ Subsurface scattering skin, fabric weave, weathered bronze patina, glass reflections. │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Slot 7: TECHNICAL SPECIFICATIONS & EXCLUSIONS                                          │
│ Film stock emulation (Kodak Vision3 250D) or animation render style, aspect ratio, and targeted negative tokens. │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---


### The Inheritance Law for Slot 3 (Zero Redundant Decisions)
- **On a shot that feeds a sequence, Slot 3 does NOT decide shot size or camera height.**
- Shot Size is inherited directly from the **[Phase 3 Shooting Script Table](../phase-03-shooting-script/HOW-PHASE-3-WORKS.md)** and **[Phase 6 Storyboard Deck](../phase-06-storyboard-layout/HOW-PHASE-6-WORKS.md)**.
- Slot 3's sole creative responsibility is adding the **Optical Lens & Sensor Physics** from Phase 7's [lens-focus-depth.md](./lens-focus-depth.md) (e.g. 24mm Panavision Ultra Vintage anamorphic, T2.3, shallow depth of field).
- **When the deliverable is a single finished still, Slot 3 is authored here instead** — see §6 below. There is no shot table upstream to inherit from, and asking for one is how a one-image job gets stuck.

## 4. Master Reference Sheets

Before generating full scenes, Phase 7 produces the reference sheets the piece needs — one per recurring character, location or prop set, and none where nothing recurs — to ensure downstream visual consistency across AI models:
- **[sheet-character.md](./sheet-character.md)**: Multi-angle character turnaround: four full-body views (front, back, left side, right side), four face close-ups (front neutral, smile showing the teeth, three-quarter left, three-quarter right), then accessories and colour swatches.
- **[sheet-location.md](./sheet-location.md)**: Architectural master environment plates (Exterior establishing, Interior wide, Key prop details, Lighting variations).
- **[sheet-props.md](./sheet-props.md)**: A props and set-dressing sheet for one location's objects. A single recurring object uses `ident.object_card` instead.

---

## 5. Mesopotamia Historical Canon Integration

On any Near Eastern, Mesopotamian, Assyrian, Babylonian, or Sumerian project dating before 330 BC, Phase 7 consults the **Mesopotamia Canon**, and **[mesopotamia-canon/heritage-rules.md](./mesopotamia-canon/heritage-rules.md)** exactly as that file scopes it under *Which of these apply*: Part A on the owner's own work and wherever a brief asks for it, Part B only on a history piece the user wants realistic and only for its historical frames. A present-day setting in the same piece, a modern Assyrian family included, is shown as the brief wants it. After 330 BC the canon is shut and the real period is searched (`canon-rules.md` §1).
- **[mesopotamia-canon/canon-rules.md](./mesopotamia-canon/canon-rules.md)**: The 330 BC Hellenistic cutoff, house canon rules, verbatim quotation mandate, and canon scope.
- **[mesopotamia-canon/INDEX.md](./mesopotamia-canon/INDEX.md)** and **[mesopotamia-canon/CANON-LOOKUP.md](./mesopotamia-canon/CANON-LOOKUP.md)**: the canon's two routers. Open them after `canon-rules.md` and before anything else: `INDEX.md` lists every chapter and wardrobe file with its period and dates and turns a period into the one or two files to read, and `CANON-LOOKUP.md` is the id table for a card you already have a name for, so no canon file is read whole.
- **mesopotamia-canon/`clothing-01` … `clothing-11`**: The wardrobe (its garment count is generated on `clothing-00-about.md`) — royal garments, beards, crowns, hairstyles, authentic footwear, fringed tunics and armlets — one file per Part, 23–26 KB each.
- **mesopotamia-canon/`grimoire-01` … `grimoire-20`**: The architectural and material encyclopedia covering palace reliefs, ziggurats and weapons — one file per civilisation, 7–10 KB each, each carrying the same eight headings.
- **[mesopotamia-canon/heritage-rules.md](./mesopotamia-canon/heritage-rules.md)**: Cultural sensitivities, modern Assyrian work (post-330 BC / modern era), modern flags, authentic faces, and burned text guidelines.

---

## 6. When the deliverable is one finished still

A poster, key art, a thumbnail, a podcast or album cover, a packshot, an exhibition panel — anything
delivered **as an image** rather than as a frame feeding a shot — opens
[`still-image-design-record.md`](./still-image-design-record.md) **instead of** inheriting Slot 3 from
Phases 3 and 6. Fill that record first; it carries what a shot card has no room for — which
references contribute and which must not, what may vary and what may never drift, where the safe
areas are — and on this route the still's framing, elevation and optics are **decisions of this
phase**, because nothing upstream made them.

Everything else is unchanged. Laws 1 to 9 all apply, the seven slots are assembled in the same order,
and law 7 still takes the generation tile from [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) — a 1:1 cover
is a native tile like any other, not a square crop of a wide frame.

This section exists because the route was reachable only by accident: this guide is what the root
`SKILL.md` tells you to read before executing the phase, and it routed every reader to the shot-fed
path and never named the record. A one-still job followed the instruction correctly and was told to
inherit a shot size from a storyboard deck it does not have.

<!-- GENERATED:module-catalog — do not edit by hand. Generated in the source package -->

## The craft files in this phase - 28 files, 674 cards

Generated from the cards, so a file whose cards change scope changes here too. The same table with the full card lists is in [`INDEX.md`](./INDEX.md); the searchable id table is in [`LOOKUP.md`](./LOOKUP.md).

| File | What it covers | Cards scoped to | Cards |
| :--- | :--- | :--- | ---: |
| [`lighting.md`](lighting.md) | **Lighting** — Lighting Architecture, Contrast & Kelvin Physics | any format | 90 |
| [`image-format-texture.md`](image-format-texture.md) | **Image Format and Texture** — Image Formats, Film Stocks & Sensor Textures | any format | 64 |
| [`anime-2d.md`](anime-2d.md) | **Anime and 2D Animation Techniques** — 2D Anime, Cel Animation & Stylized Renderings | any format | 59 |
| [`colour-grading.md`](colour-grading.md) | **Colour and Grading** — Colour Palettes, Contrast Ratios & Cinema Grades | any format | 58 |
| [`lens-focus-depth.md`](lens-focus-depth.md) | **Lens, Focus and Depth** — Optical Lenses, Apertures & Depth of Field | any format | 53 |
| [`cg-vfx.md`](cg-vfx.md) | **3D CG, VFX and Virtual Production** — CGI, Visual Effects & Volumetric Simulations | any format | 32 |
| [`vertical-short-form.md`](vertical-short-form.md) | **Vertical Short-Form** — Vertical Short-Form Composition (9:16 Reels/Shorts) | mostly Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Commercial / TVC, Vlog / YouTube Long-Form, among 22 formats | 25 |
| [`still-photography.md`](still-photography.md) | **Still Photography and Static Visual Arts** — Studio & Commercial Still Photography | any format | 18 |
| [`render-style.md`](render-style.md) | **Medium, Style and Render Register** — Fine Art, Traditional Painting & Illustration Styles | any format | 19 |
| [`kids-content.md`](kids-content.md) | **Kids Content** — Children Content, High Clarity & Joyful Aesthetics | mostly 2D Animation (Western / Cartoon), Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, among 10 formats | 16 |
| [`still-life-product.md`](still-life-product.md) | **Still-Life, Product and Set Staging** — Product Photography & Macro Tabletop Staging | any format | 16 |
| [`materials-surfaces.md`](materials-surfaces.md) | **Materials and Surface Physics** — Surface Physics, Textures & Material Shaders | any format | 16 |
| [`pose-static.md`](pose-static.md) | **Pose and Static Performance** — Static Posing, Weight Distribution & Body Silhouette | any format | 16 |
| [`reference-roles.md`](reference-roles.md) | **Reference Roles and Multi-Reference Assembly** — Reference Image Routing & Multimodal Control Weights | any format | 16 |
| [`documentary.md`](documentary.md) | **Documentary, Interview and Reportage** — Documentary Realism, Archival & Observational Stills | mostly Documentary Feature, Video Essay, Documentary Series, News Report / Reportage, among 26 formats | 15 |
| [`identity-consistency.md`](identity-consistency.md) | **Identity Consistency Across Images** — Character Identity Consistency Across Generations | mostly Character Sheet / Turnaround, Documentary Photography, Editorial / Magazine Image, Event Photography, among 23 formats | 14 |
| [`music-video.md`](music-video.md) | **Music Video and Performance** — Music Video Keyframes & Rhythmic Stylization | mostly Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Concert / Live Event, among 18 formats | 14 |
| [`ads-trailers.md`](ads-trailers.md) | **Ads, Trailers and Motion Design** — Advertising, Key Art & High-Impact Promo Stills | mostly Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Explainer, among 22 formats | 13 |
| [`keyframe-craft.md`](keyframe-craft.md) | **Keyframe Craft, Single and Paired** — Keyframe Extraction & Motion-Ready Composition | any format | 14 |
| [`retouching.md`](retouching.md) | **Retouching and Post-Capture Treatment** — High-End Retouching & Clean Plate Inpainting | any format | 13 |
| [`in-frame-text.md`](in-frame-text.md) | **In-Frame Text and Typography** — In-Frame Typography, Ancient Glyphs & Signage | any format | 16 |
| [`print-delivery.md`](print-delivery.md) | **Print and Physical Delivery** — High-Resolution Print Delivery & Aspect Scaling | mostly Poster / Static Design, Editorial / Magazine Image, Fine Art Photography, Abstract Photography, among 23 formats | 13 |
| [`restoration.md`](restoration.md) | **Correction, Restoration and Extension** — Historical Archive Restoration & Damage Recovery | mostly Architectural Photography, Documentary Photography, Editorial / Magazine Image, Fine Art Photography, among 23 formats | 10 |
| [`failure-modes.md`](failure-modes.md) | **Failure Modes and Rescues** — Visual Artifacts, Prompt Bloat & Model Failure Mitigation | mostly Architectural Photography, Documentary Photography, Food Photography, Portrait Photography, among 25 formats | 10 |
| [`data-visualisation.md`](data-visualisation.md) | **Data Visualisation and Information Graphics** — Designing the frame when the subject is a number | mostly Explainer, Documentary Feature, News Report / Reportage, Vertical Short-Form (Reels, Shorts, TikTok), among 9 formats | 17 |
| [`how-to-write-an-image-prompt.md`](how-to-write-an-image-prompt.md) | **How an image prompt is written** — How an image prompt is written — Every rule here is craft: what a generative model does with a prompt, and what it does with a careless one. | — | 22 |
| [`sheet-character.md`](sheet-character.md) | **CHARACTER SHEET TEXT-VISUAL TEMPLATE** — CHARACTER SHEET TEXT-VISUAL TEMPLATE — This is the **written/visual template** of the character sheet reference (Gilgamesh style). | — | 4 |
| [`still-image-design-record.md`](still-image-design-record.md) | **Still-image design record** — Still-image design record — What is decided about a frame, as opposed to a shot. This is the record behind every keyframe, reference sheet, poster and thumbnail, and it is filled b | mostly Editorial / Magazine Image, Museum Installation, Podcast, Poster / Static Design, among 6 formats | 1 |

<!-- /GENERATED:module-catalog -->

