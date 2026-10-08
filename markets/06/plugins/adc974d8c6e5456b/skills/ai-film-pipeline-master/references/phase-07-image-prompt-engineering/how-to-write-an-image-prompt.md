# How an image prompt is written

Every rule here is craft: what a generative model does with a prompt, and what it does with a careless one. Nothing in it routes to another module, so it can be read on its own.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [0. The 9 Laws Of Image Prompt (Never Broken)](#0-the-9-laws-of-image-prompt-never-broken)
- [1. Purpose](#1-purpose)
- [2. When It Opens, When It Is Skipped](#2-when-it-opens-when-it-is-skipped)
- [3. Inputs](#3-inputs)
- [4. Method](#4-method)
- [5. Decision Rules](#5-decision-rules)
- [6. Research Protocol](#6-research-protocol)
- [7. Output Contract](#7-output-contract)
- [8. Quality Bar And Failure Modes](#8-quality-bar-and-failure-modes)
- [9. Worked Example](#9-worked-example)
- [Fast path](#fast-path)

<!-- /GENERATED:toc -->

## 0. The 9 Laws Of Image Prompt (Never Broken)

Prioritised. When two laws collide the lower-numbered one wins, and you sacrifice from the bottom.

Laws marked **** restate a rule that already governs the whole package — one of the owner's standing rules in [`heritage-rules.md`](./mesopotamia-canon/heritage-rules.md) Part A, or an order set in [`PRECEDENCE.md`](../PRECEDENCE.md) — repeated here so it is visible where it bites. The unmarked laws are the ones only this module can break, and they are what this module's depth is measured by.

1. **Every prompt is completely self-contained.** Generative image models share zero memory between generation calls; every prompt must independently declare subject identity, lighting, camera lens, environment, and render style without relying on previous prompts.
2. **Prompts enforce the seven-slot Universal Syntax Order.** Every keyframe prompt must assemble exactly these slots in order: `[Subject & Identity]` + `[Action & Pose]` + `[Framing, Elevation & Optics]` + `[Lighting Architecture]` + `[Environment & Palette]` + `[Surface Material Physics]` + `[Technical Specifications & Exclusions]`.
3. **Order beats length. There is no word cap.** Write the prompt the image actually needs, for the
   **most capable model available**, and order it so a weaker one degrades well: the verbatim lock
   first, then subject and action, then frame, then light and palette, then the exclusions. Late
   instructions are what a weak model drops, so **the tail is where the affordable detail goes and
   the head is where the lock goes, always.** A concise prompt is usually a better prompt - vagueness
   and padding genuinely dilute - but that is a reason to **cut the words that say nothing**, never
   to cut a described element out of the image. A genuinely complex frame is written at the length it
   needs. **Nothing is removed from the image to satisfy a word count**, and the lock is never
   shortened.
4. **Mandatory verbatim character sentences are immutable.** When the continuity record is open, copy its frozen 30 to 45-word sentence into Slot 1. When the route legitimately operates without an upstream identity record, copy the character record's exact `project_scoped` sentence instead. Neither source may be omitted or paraphrased. **The wardrobe line sits beside the sentence, not inside its 30 to 45 words**: it follows the sentence in Slot 1, verbatim, in image prompts and character-sheet prompts only. **A shot that shows only part of a character** (hands only, from behind) **quotes only the parts that are visible** — the clauses the frame shows, verbatim (build, skin, the age of the hands), and the wardrobe on them — **never the face clauses**; write `face out of frame`, and quote the whole sentence again the moment the face can be seen. The video guide applies the same rule to the clip (§4.3 there). **In a group shot the agent decides, without asking:** when one character is drawn out of the group, identity comes from the reference images and only that character's sentence is quoted; when the group is shown as a group, the group's own reference carries it and the sentences travel with it as one block. Read `frozen_sentence_status` in `project.yaml` first: only `locked` or `project_scoped` is quotable, and `lockable` is a sentence that has not been frozen yet. **The one person this law does not apply to is a person who must not be recognisable.** Where a contributor was promised protection, a frozen 30-to-45-word description of their face and build is the exact artefact you must not create, and copying one into Slot 1 asks a generator to produce a recognisable likeness of somebody who was promised the opposite. For them, Slot 1 describes **the concealment** — the silhouette, the framing, the hands, the out-of-uniform clothing — and carries no identifying feature at all, deliberately and on the record. That is tier 0 in [`../PRECEDENCE.md`](../PRECEDENCE.md) and it outranks this law.

5. **Banish quality buzzwords and literary abstractions.** Terms like "photorealistic", "ultra detailed", "hyperrealistic", "8K", or "cinematic" trigger The Quality Buzzword Pollution; replace them with concrete optical lens names, f-stops, lighting ratios, and sensor formats. **On flat 2D, cel-shaded or cartoon work the whole optical and photographic vocabulary is replaced, not only the camera body and the stock** — lens names, f-stops and apertures, sensor formats, depth-of-field calls, and the Kelvin figure law 8 asks for. None of them exists in drawn animation, and writing one there is a photographic instruction landing on line art. What goes in their place comes from [`anime-2d.md`](./anime-2d.md) — its drawing vocabulary, not the words "anime style" unless the piece is anime: the art style, the line weight, the ink and colour treatment, the **drawn light direction in words** — key from upper frame-left, rim along the right shoulder — and the **palette temperature in words** — a warm amber key against cool blue shadow. The requirement does not relax; the units change. 3D and rendered-CG work keeps the photographic values, because there is a virtual camera with a real focal length behind the frame. **And a shot whose render mode is `built` takes none of this and never reaches a generator at all** — a chart, map, counter or diagram is assembled from real values as a graphics layer, so it has no lens, no art style and no surface, and a prompt written for it produces an invented chart with plausible wrong numbers on it (`dataviz.build_do_not_generate`).
6. **Negative prompts must be budgeted and targeted.** Restrict negative exclusions to 15 to 30 words selected only from risks that apply to the shot; dumping generic negatives triggers The Negative Prompt Overload and distorts image color balance. **The budget is per risk class, not a total across tiers.** Tier 0 is exempt, and where a shot genuinely carries three classes at once — a stylised render, a period boundary and a clean canvas — **the block will run to 50, 60 or more words and that is correct**, because the tiers' own lists are written at that length and three of them apply. Measured on real prompts it lands between about 50 and 70. **Never reach the number by cutting the anatomy half of Tier 1** — that is the half that prevents the failures nobody can repair, and trimming it to satisfy a word count is the exact trade law 3 forbids. What the budget forbids is the generic dump: every token must name a risk that applies to *this* shot. A tier that cannot be shortened without losing a real risk is kept and the overrun recorded, on exactly the reasoning law 3 gives — nothing is removed from the image to satisfy a word count.
7. **Ratios use the verified model's native generation tile.** Never render a square image and crop to vertical. The exact width and height come from the dated record for the selected model in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) — never from memory and never from this file. If that record has not been filled yet, the prompt is still written in full and the resolution cell carries `pending_engine_check`, which travels with the handoff. An open cell costs a minute; a guessed one costs a re-render.
8. **Lighting must declare motivated origin and Kelvin temperature.** Every prompt must state light source, angle, and color temperature; neglecting lighting triggers The Neglected Lighting Defect and results in flat CGI lighting. **The figure comes from `light.kelvin_reference` in [`lighting.md`](./lighting.md), which is the only place in the package a colour temperature is written as a number** - and it is the only place, because until September 2026 this law demanded a figure that no card supplied, so it was invented at each prompt and the film drifted in colour between shots that were each written correctly. **Where that card's row gives a range, choose one figure inside it, record it under `decisions` in `project.yaml`, and hold it for the scene.** That card also carries the four sources that have no colour temperature at all, which this law does not mention. **On animated work the animation carve-out in law 5 applies here too**: the source and the angle are still declared, and the Kelvin figure is replaced by the palette temperature in words. A cel frame has no emitter to measure.
9. **This module does not authorize spend.** It engineers prompt strings and negative exclusions. Which engine runs is settled at the top of the project in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md): the brief's engine where it names one; otherwise the agent chooses the most suitable current one (root `SKILL.md` §0) and records it under `decisions`. What it costs waits for the spend approval (`paid_generation_approved_by`) before anything is generated.

**Every marker closes two ways.** *Resolved* — the answer arrived — or *`unobtainable — why, and what was done instead`*, which is a finished answer and not an open one. [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) carries the rule and a worked case for each marker. What is never acceptable is deleting a marker because it could not be resolved.

## 1. Purpose

The Image Prompt skill engineers self-contained, model-ready textual prompts for character model sheets, location master plates, prop turnaround cards, wardrobe manifests, storyboard keyframes, marketing key art, and conditioning stills. It translates abstract world design rules from the production design record, character psychological physiognomy from the character record, shot design from the shot plan, panel design from the storyboard, or an approved reference-sheet layout into precise linguistic syntax that latent diffusion and transformer vision models execute without ambiguity. This skill enforces The Self-Containment Law: every prompt is completely autonomous, quoting the Mandatory Verbatim Character Sentence and the Three-Color Palette without relying on conversational memory. It establishes structured negative prompt taxonomies, permissive narrative generation guardrails, and universal English-only prompt syntax.

## 2. When It Opens, When It Is Skipped

### Router Opening Conditions

> **The conditions below describe when this guide is needed. Nothing outside this file overrides
> them, and a project that thinks it needs an exception records the reason rather than assuming
> one.**
This skill opens across any workflow phase that requires the generation, refinement, or conditioning of static 2D imagery:
- **Character Model Sheets:** Generating multi-angle turnarounds, expression matrices, and anatomical reference portraits for downstream consistency.
- **Location Master Plates:** Establishing architectural master environments, environmental lighting plates, and spatial backdrops.
- **Prop and Wardrobe Reference Sheets:** Rendering isolated historical artifacts, weapons, ceremonial regalia, tools, and textured fabric swatches.
- **Conditioning Keyframes for Video:** Formulating the high-resolution Start Frame and End Frame stills required by image-to-video diffusion engines.
- **Marketing, Key Art & Covers:** Designing posters, thumbnails, album artwork, and promotional stills with integrated negative prompts. This includes a cover for every aspect the project delivers: a 9:16 piece needs a 9:16 cover of its own, generated at the engine's native tile for that aspect ([`ENGINE-CHECK.md`](../ENGINE-CHECK.md)), and it is a separate asset from the 16:9 thumbnail, never a crop of it. The delivery spec names which covers are needed, this module writes the prompt for each, and each is generated as its own batch.


`prompt.rule.router_opening_conditions`

### Router Skip Conditions
This skill is strictly skipped only under the following conditions:
- Pure audio, podcast, musical composition, or sound design pipelines with zero visual components.
- Direct video generation that bypasses static image conditioning entirely (prompt-to-video mode), although frame-anchored workflows always require this skill.
- Raw text screenplay breakdowns, script formatting, or budget scheduling documentation.


**Yields to:** `ai.prompt_anatomy` — Prompt-to-video work that skips static conditioning.  
`prompt.rule.router_skip_conditions`

## 3. Inputs

| What the prompt needs | Where it comes from | When it is missing |
|---|---|---|
| The visual world: materials, palette, period, weather | The production design record for this project | Decide it from the story and, for a historical world, the canon, and record it under `decisions` |
| The character specification, and whether its sentence is approved | The character record | Not needed for a piece with no character in it. A sentence the agent wrote is not left waiting: on an Express run the agent locks it (`locked`) and carries on; otherwise it is `project_scoped`, quoted in every prompt, and marked pending the owner's approval, which the keyframe approval gives (`keyframes_approved_by`, either form): it locks every `project_scoped` sentence it covers — the faceless default of §4.11 applies only where no sentence exists at all. A look the brief leaves open does not wait either: the agent decides it (the brief, the skill, the web, then its own best choice), writes it as the `project_scoped` sentence, records the choice under `decisions`, and carries on |
| Continuity locks | The continuity record, or the production design locks | A lock that exists only in someone's head is not a lock |
| Composition, or the panel design | The storyboard, or the shot plan when there is no storyboard. For a reference sheet, the approved sheet layout and the asset specification | For a poster, thumbnail, key art or free composition, an accepted static-composition brief. If that brief is absent, compose it from the story and record it under `decisions` |
| The model, its syntax, and its native resolution | The dated record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) | The prompt is written in full either way; without the record the resolution cell reads `pending_engine_check` and travels with the handoff. A guessed resolution is a re-render |
| The project's standing prohibitions, `forbidden_global` — what Tier 0 of every negative block is copied from | The list at the root of the project brief, defined in [`FORBIDDEN-GLOBAL.md`](../FORBIDDEN-GLOBAL.md) | The prompt is written in full either way; Tier 0 reads `pending_forbidden_global` and travels with the handoff. A project that genuinely forbids nothing says so, and Tier 0 reads `none, per the project brief` — an empty Tier 0 is never left to look like an absent one |

**Where these records live.** None of the three records named above is a separate file: *the
production design record* is `story_brief` and `palette` in `project.yaml`; *the character record*
is `frozen_sentence` and `frozen_sentence_status`; *the continuity record* is the yaml's `locks`
block together with the Phase 6 handoff list in
[`../phase-06-storyboard-layout/handoff-to-stills.md`](../phase-06-storyboard-layout/handoff-to-stills.md).

The prompt is compiled from the brief the project record carries. The engine's limits should be known by then
too, and if they are not, the prompt still gets written — see `ENGINE-CHECK.md` §3. What the engine
can do never decides what the shot is; if a limit gets in the way, the engine changes, not the shot.
Every applicable row must be filled by its source or by a stated substitute. A source that does
not apply to this project is not a blocker; a source that applies and is empty is.

## 4. Method

### 4.0 The jobs, in order

| # | The job | You are doing this when | Sections | It produces |
|---|---|---|---|---|
| J1 | Configure model syntax adapters, aspect tiles, and ethical guardrails | Initializing prompt generation parameters for the verified target engine and canvas ratio | 4.5, 4.6, 4.10 | delivery_aspect_ratio |
| J2 | Calibrate asset types, optical lenses, and focal depth physics | Staging reference model sheets, location plates, or shot keyframes with physical camera optics | 4.3, 4.7 | prompt_type |
| J3 | Structure self-contained positive prompts and resolve pipeline defaults | Authoring the seven-slot prompt payload and embedding verbatim identity locks | 4.1, 4.2, 4.11 | prompt_slots |
| J4 | Compile tiered negative exclusion token blocks | Filtering anatomical defects, modern historical anachronisms, and non-diegetic overlays | 4.4 | negative_prompt_block |
| J5 | Engineer dual-frame end keyframes and apply recovery remedies | Designing start-and-end frame interpolation pairs or repairing observable latent artifacts | 4.8, 4.9 | full_positive_prompt |


`prompt.rule.the_jobs_in_order`

### 4.0b The Mesopotamia canon

On a Mesopotamian project the canon at the Mesopotamia canon is open. It opens only on a Mesopotamian subject.

**What this module needs from it:** concrete nouns. "Ancient Mesopotamian palace" wastes the
strongest tokens in the prompt; the canon gives the gypsum alabaster orthostat, the five-legged
lamassu, the cedar door bound in hammered bronze.


**Yields to:** The project's Mesopotamia canon — Concrete nouns come from the canon, not from here.  
`prompt.rule.b_the_mesopotamia_canon`

### 4.1 Prompt Anatomy And Universal Syntax Order
Generative vision models respond best to structured, hierarchical information order. Prompts must be organized in descending order of compositional weight:

```text
+-----------------------------------------------------------------------------------+
| THE SEVEN-SLOT PROMPT ORDER                                                       |
+-----------------------------------------------------------------------------------+
| 1. SUBJECT & IDENTITY SENTENCE:                                                   |
|    The primary character or focal entity. Quote the approved character sentence, or    |
|    the project-scoped sentence when no continuity record was opened.          |
|                                                                                   |
| 2. ACTION & POSE:                                                                 |
|    Exact physical posture, spatial orientation, gesture, and gaze direction.       |
|    Specify where the subject sits on the framing grid (e.g., left third).         |
|                                                                                   |
| 3. FRAMING, ELEVATION & OPTICS:                                                   |
|    Cinematographic shot size (WES, WS, MS, MCU, CU, ECU), camera height (seated,  |
|    eye-level, low angle), and THEN, by render mode:                               |
|      photoreal / 3D / CG - lens focal length (28mm, 50mm, 85mm) and aperture      |
|        depth of field (f/1.8 shallow focus, f/8 deep focus).                      |
|      flat 2D / cel / cartoon - NO lens and NO aperture. Depth is written as tonal |
|        separation and dropped detail. See law 5.                                  |
|                                                                                   |
| 4. LIGHTING ARCHITECTURE:                                                         |
|    Key light source and angle, fill ratio, practical sources, shadow quality,     |
|    and THEN, by render mode:                                                      |
|      photoreal / 3D / CG - colour temperature in Kelvin.                          |
|      flat 2D / cel / cartoon - palette temperature IN WORDS (a warm amber key     |
|        against cool blue shadow). A cel frame has no emitter to measure. Law 8.   |
|                                                                                   |
| 5. ENVIRONMENT & THREE-COLOR PALETTE:                                             |
|    Architectural space, ground plane, background elements, and the locked         |
|    hex palette tones - usually three; a colour-coded cast adds one accent         |
|    per character (from sheet-location.md & the Phase 6 color script).             |
|                                                                                   |
| 6. SURFACE MATERIAL PHYSICS:                                                      |
|    What the thing is MADE OF, in the register the piece is made in.               |
|    photoreal: micro-textures, specular highlights, weave coarseness, skin pores,   |
|      distress, patina, dust motes, moisture.                                      |
|    3D / rendered CG: the material and its imperfections - matte unglazed clay with |
|      thumb-marks, felt fibre, painted wood, brushed metal. NOT skin pores.         |
|    flat 2D / cel: fill treatment and edge - flat fills, a single shadow step,      |
|      visible brush or ink edge, paper grain in the background art. NO photographic |
|      texture of any kind.                                                         |
|                                                                                   |
| 7. TECHNICAL SPECIFICATIONS & EXCLUSIONS:                                         |
|    Delivery aspect ratio (per engine record), clean-plate constraints (no text     |
|      the scene does not carry, no watermarks, no split frame), and the negative    |
|      block for THIS render mode.                                                   |
|    film stock or sensor look: photoreal only. A render has no film gate and a      |
|      drawing has no emulsion - on those, grain is an added effect or nothing.      |
+-----------------------------------------------------------------------------------+
```

**Slots 6 and 7 branch by render mode, and they used to contradict each other on it.** Slot 6 asked
every subject for skin pores and specular highlights, which is a photographic instruction that
flattens a clay render into plastic; Slot 7 asked every prompt for a film stock, which a render and a
drawing do not have. Meanwhile law 5 said the opposite, correctly, three sections earlier. **A slot is
where the value is filled, so a carve-out that lives only in a law does not reach it** — the same
lesson as the optical fields, applied one slot later. Phase 8's equivalent field already branched;
these two now agree with it.

**Slot 1 when the subject is not a person.** The box above is written for a face, and most of this
module is, but the route table sends product advertising, commercial and promo work down this same
phase — and a great deal of heritage work is a tablet, a relief or a vessel with nobody in the frame
at all. On those shots Slot 1 is still Slot 1: it is the identity slot, and it still goes first and
still carries the thing that must come back the same in every frame. What changes is what identity
*means*.

For a pack, a bottle, a tool or an artifact, write these four, in this order, and write them as
concretely as a frozen character sentence is written:

1. **The form.** The silhouette and the proportion, in real measurements where they are known: a
   250ml squat amber glass bottle, shoulders sloping to a short neck, roughly twice as tall as it is
   wide. A product read wrong in the silhouette is read wrong in every panel, exactly as a face is.
2. **The label geometry.** Where the label sits on the form, how far it wraps, its shape, and how the
   type is ranged on it — a cream rectangular label across the middle third, wrapping about half the
   circumference, brand wordmark centred in the upper band with two lines of small caps beneath. The
   *words* on it are in-frame text and are governed as in-frame text, per
   [`in-frame-text.md`](./in-frame-text.md); the *geometry* belongs here, because it is what makes
   the object recognisable at a glance and from the back of a shelf.
3. **The material.** What the object is made of and how it behaves under light: unpolished hammered
   brass, matte uncoated board, cold-rolled steel with a brushed grain, glazed earthenware with a
   crazed surface. This is the line that decides whether the render looks like the product or like a
   3D model of the product, and it is worth more words than any other in the slot.
4. **The one feature that must be recognisable.** Every object has a single detail a buyer or a
   curator identifies it by — the ribbed cap, the notched shoulder, the chipped rim, the seam down
   the left side, the hallmark stamped below the handle. Name it explicitly and name it every time.
   It is the product's equivalent of the character lock's one unmistakable feature, and it is the
   first thing an engine drops.

**A product has no `ident.frozen_sentence`, and it needs none.** The frozen sentence exists because a
human face cannot be specified exhaustively and has to be held by one agreed form of words instead. A
product *can* be specified exhaustively — the four items above are its specification, they come from
the brand's own reference material rather than from a continuity record, and they are quoted from the
approved product sheet the same way for every frame. So law 4 does not apply to a product-only shot,
and a prompt writer who cannot find a frozen sentence for a bottle is not missing an input. Where a
person and a product are both in frame, the character lock comes first in Slot 1 and the product
specification follows it in the same slot, in that order, because the face is the harder thing to
hold. The craft of lighting and staging the object itself is in
[`still-life-product.md`](./still-life-product.md); this is only what Slot 1 owes it.


**Yields to:** `ident.object_card` — The subject is a product or artifact, not a face.  
`prompt.rule.prompt_anatomy_and_universal_syntax_order`

### 4.2 The Self-Containment Law
Generative image models maintain zero memory across independent API requests or prompt runs. A model rendering Shot 4 does not remember Shot 1, 2, or 3:

```text
+-----------------------------------------------------------------------------------+
| THE SELF-CONTAINMENT LAW                                                          |
+-----------------------------------------------------------------------------------+
| 1. Zero Relative Descriptions:                                                    |
|    Never write "the same man as earlier", "Marcus in a new room", or "she looks   |
|    angrier". The model will hallucinate a brand new person every time.            |
|                                                                                   |
| 2. Verbatim Sentence Insertion:                                                   |
|    Every prompt depicting a recurring character must copy-paste their locked      |
|    Mandatory Verbatim Prompt Sentence in its exact 30 to 45-word entirety.         |
|    Part of a character in frame: visible parts only, never the face (law 4).       |
|                                                                                   |
| 3. Autonomous Environment Staging:                                                |
|    Every prompt must restate the architectural room geometry, lighting angle,     |
|    and three-color anchor palette. Treat every single prompt as if it were the     |
|    first and only image the AI model will ever render.                            |
+-----------------------------------------------------------------------------------+
```


**Yields to:** `ai.image_to_video` — The shot is conditioned on an approved keyframe.  
`prompt.rule.the_self_containment_law`

### 4.3 Asset Types: Keyframes Versus Reference Sheets
Different production stages require distinct prompt architectures:
- **Character Model Sheet:** Two cases. A bare turnaround with no layout is rendered against a clean neutral mid-gray studio background (#808080) with balanced, non-directional softbox lighting. A sheet built on one of the layout templates — [`sheet-character.md`](./sheet-character.md), [`sheet-location.md`](./sheet-location.md), [`sheet-props.md`](./sheet-props.md) — takes that template's ground, header and labels instead, because the lettering is the point of the sheet. Where the template and this line disagree, the template wins. Either way the character is isolated in a neutral A-pose or relaxed stance, to capture clean facial features and full costume proportion without environmental contamination.
- **Location Master Plate:** Rendered as an expansive wide establishing shot devoid of human actors. Sets the baseline architecture, natural sunlight angle, atmospheric depth, and material textures. Subsequent shot prompts reference this plate to maintain spatial fidelity.
- **Dual-Frame End Keyframe:** For shots requiring start-and-end frame video interpolation, the End Keyframe prompt is constructed by cloning the Start Keyframe prompt and modifying only the subject pose, eye gaze, and camera distance, preserving all lighting and background tokens identically.


**Yields to:** `sheet.char.what_this_sheet_is_for` — A sheet built on the template: the template wins.  
`prompt.rule.asset_types_keyframes_versus_reference_sheets`

### 4.4 Negative Prompting Taxonomy
Negative prompts prevent known failure modes in diffusion latent space. Organize negative tokens into functional tiers — Tier 0 first, then Tier 0b where the project has more than one deliverable, then the three below:
- **Tier 0: the project's own prohibitions.** Before the three tiers below, pull every entry from
  the top-level `forbidden_global`, the craft prohibition list owned by the canon and world rules, that
  could plausibly appear in THIS shot. Those come first and they are not optional. They also do not
  count against the 15 to 30 word budget, because they are the project's standing rules rather than
  this shot's risk assessment: a wristwatch in a Nineveh frame is not a judgement call.
  **What that list is, where it lives and who writes it is defined in
  [`FORBIDDEN-GLOBAL.md`](../FORBIDDEN-GLOBAL.md)** — it sits at the root of the project brief, it is
  owned jointly by the canon and by the piece's own editorial rules, and it is append-only.
  **When it does not exist yet, the prompt is still written in full** and Tier 0 reads
  `pending_forbidden_global`, which travels with the handoff the same way `pending_engine_check`
  does. Nothing stops for it. What must never happen is Tier 0 coming out blank with no marker,
  because a blank Tier 0 and a project that truly forbids nothing look identical on the page and are
  not the same thing at all — a project that forbids nothing writes that down, and Tier 0 then reads
  `none, per the project brief`. Both the marker and that note live on the prompt record and the
  handoff line, never in the negative string pasted into the engine (`FORBIDDEN-GLOBAL.md` §5).
- **Tier 0b: what this deliverable forbids that the others do not.** Tier 0 is project-wide and every
  deliverable inherits it unchanged. Tier 0b is the same idea one level down, and it exists because a
  campaign delivering the same design as a wide film, a vertical cutdown, a square still and a
  printed poster has **four different sets of things that must not appear** — and every other tier is
  identical across all four, so without this one the differences have nowhere to go. It is written
  per row of the deliverables table. Typical entries, and they are not interchangeable: the vertical
  cutdown forbids anything important inside the reserved bands; the poster forbids the fine texture
  and thin strokes that survive a screen and disappear in ink, and forbids RGB-only colour it cannot
  print; the square forbids a composition that only reads as a crop of something wider; a muted
  autoplay deliverable forbids anything that depends on being heard. **Omit the tier when the project
  has one deliverable** — most do — and write it the moment it has two that differ in surface.
- **Tier 1: Anatomy & Artifacts — the list depends on the render mode, because half of it names
  photographic failure.** Tier 1 is the one tier that has always been written as a constant, and it is
  not one: several of its tokens describe a photoreal frame going wrong, and on a deliberately
  rendered or drawn piece those same tokens fight the brief.
  - **Photoreal and live-action work** (the default): `bad anatomy, deformed limbs, extra fingers,
    missing fingers, fused hands, distorted eyes, cross-eyed, plastic skin, wax figure, CGI 3D sheen,
    over-smoothed, oversaturated, chromatic aberration`.
  - **3D and rendered-CG work:** keep the anatomy half — `bad anatomy, deformed limbs, extra fingers,
    missing fingers, fused hands, distorted eyes, cross-eyed` — and replace the photographic half with
    what actually spoils a stylised render: `default plastic shader, uniform glossy specular,
    over-smoothed surface, sterile symmetry, oversaturated` — and **keep `CGI 3D sheen`**, which names
    that same failure in the words most models respond to. What comes out is `plastic skin` and `wax
    figure`, and only those: they describe a *human face* going waxy, and on a puppet or a figure whose
    surface is deliberately matte and handmade they name the wrong fault. **Everything that describes
    the glossy, over-smooth default stays**, because that default is the single most common way a
    stylised render is destroyed — which is exactly what law 5 says three sections above.
    *(This branch previously removed `CGI 3D sheen` too, on the reasoning that the piece "is" CG so
    the token fights it. That reading is wrong and the rest of this file contradicts it: the token
    does not mean "looks computer-made", it means "has the glossy CG sheen", and suppressing that
    sheen is the whole job on a clay, felt or carved surface.)*
  - **Flat 2D, cel-shaded and cartoon work:** keep the anatomy half and replace the rest with
    `photographic texture, skin pores, lens blur, film grain, 3D shading on line art, gradient mesh
    shading`. There is no skin to go plastic and no lens to smooth, and the real failure is a
    photographic quality leaking into the drawing. **Where the design's hands are stylised — a mitten
    hand, four fingers — drop `extra fingers, missing fingers, fused hands` as well**, because on that
    design they fight the brief; the same holds on the 3D branch for a stylised figure.
  - **On a frame with no figure** — an object, a relief, a tablet, a landscape — drop the anatomy half
    on every branch and keep the render-mode half (law 6: only risks that apply to the shot).
- **Tier 2: Period anachronisms — only on a pre-modern subject.** Include this tier when the piece is
  set before the modern era, and take the list from the project's own period boundary rather than from
  this card: `modern clothing, wristwatches, synthetic zipper, denim, polyester, plastic, modern
  eyeglasses, bleached teeth, modern dentistry, asphalt roads, electrical wires, neon signs,
  automobiles`. **On a modern-set piece — an advert, an anthem, a contemporary music video, a kids
  song — this tier is omitted entirely**, and anything genuinely unwanted in that frame is a Tier 0
  project prohibition instead.
  **On a piece that alternates two looks or two periods, this tier is decided per sequence, not per
  project.** A reconstruction documentary cutting between a present-day excavation and an ancient
  rebuild is the standard case: the reconstruction shots want the full anachronism list, and the
  modern site shots want none of it — a wristwatch on an archaeologist's arm is the subject, not an
  error, and a prompt carrying the project's Tier 2 will fight to remove it. Take the tier from the
  row's own look and period, which is what the **Mode & Look** cell in the Phase 3 shot table records.
  Tier 0 stays project-wide; Tier 2 is the tier that travels with the sequence.
- **Tier 3: Framing & Clean Canvas:** `split screen, collage, diptych, multiple panels, borders, letterbox, pillarbox, text, typography, watermark, signature, artist logo, camera arrows, UI overlays`. **Drop `text, typography` when the treatment recorded from [`in-frame-text.md`](in-frame-text.md) has the generator render the lettering** — `textimg.carved_not_text`, `textimg.quote_the_string`, `textimg.period_lettering` or `textimg.invented_script` — because on that shot the lettering is part of the object; the rest of Tier 3 stays. A reference sheet has its own exemption in 4.10b.

**When the engine has no negative field at all, phrase the tiers as positives in the prompt body.**
Several frontier still engines take a single prompt and nothing else, and a writer who has built four
tiers then has nowhere to put them — which reads as the work being wasted, and usually ends with the
negatives pasted into the prompt as a list of things not to do, where they act as a list of things to
draw. They are rewritten instead: *"correct anatomy, five fingers on each visible hand"* rather than
`bad anatomy, extra fingers`; *"matte unglazed surface"* rather than `glossy plastic shader`;
*"bare limestone wall, no signage"* rather than `text, watermark`. Tier 0 is the one that must
survive this translation intact, because it is the project's own prohibition — if a forbidden thing
cannot be excluded positively, say so in the handoff rather than dropping it silently. Phase 8 has
carried this rule for its own engines for some time; it belongs here too, and the two phases now say
the same thing.


**Yields to:** `prompt.rule.b_a_reference_sheet_is_not_a_shot` — A reference sheet, where the text and layout negatives cancel the brief.  
`prompt.rule.negative_prompting_taxonomy`

### 4.5 Permissive Generation Guardrails And Strict Ethics
Creative storytelling encompasses realistic human conflict, diverse historical cultures, and full lifespans:
- **Permissive Creative Scope:** Prompts depicting characters across all natural age groups and life stages (infants, children, adults, elderly), realistic historical warfare, verified cultural and religious practices, authentic period wardrobe, and photorealistic fictional children in narrative and family contexts are fully authorized and encouraged.
- **The Absolute Ethical Boundary:** The non-consensual synthesis, imitation, or sexualized generation of real living minors from photographs, personal identities, or private datasets is strictly and unconditionally prohibited.
- **Language Mandate:** All prompt strings, camera commands, negative token blocks, and technical parameters must be authored exclusively in English to match the primary training distribution of foundation vision models, except on-screen text the audience reads, whose treatment is routed through [`in-frame-text.md`](in-frame-text.md) (root `SKILL.md` §4, rules 5 and 6).


`prompt.rule.permissive_generation_guardrails_and_strict_ethics`

### 4.6 Model-Specific Syntax Adapters
Image models read a prompt through different text encoders, and each maker documents its own syntax: whether weights are accepted and in what range, whether there is a separate negative field, and how on-image wording is marked. Those are vendor facts that change with each release, so none is written here; the encoder, the syntax and the date they were checked are in its adapter in ENGINE-CHECK.md §7. Write the prompt for the family, then format the payload with the adapter:

```text
+-----------------------------------------------------------------------------------+
| SYNTAX ADAPTER TAXONOMY: FOUR PROMPT FAMILIES, NOT FOUR PRODUCTS                  |
+-----------------------------------------------------------------------------------+
| This module never names a model. The engine selection step chooses the model and  |
| reports which family it belongs to, in `prompt_family`. Write the prompt for the  |
| family selected, then dress it with that engine's adapter in ENGINE-CHECK.md §7.  |
| A model name, an encoder name, a weight range or a flag written here would be a   |
| capability claim, and the engine-selection step and its adapters own those.       |
+---------------+------------------------------+------------------------------------+
| Family        | Optimal Text Structure       | Parameters and Syntax Rules        |
+---------------+------------------------------+------------------------------------+
| natural_prose | Cohesive natural language    | Full sentences over comma tag      |
|               | descriptive paragraphs       | lists. Flags, weights and          |
|               |                              | exclusions only as its adapter     |
|               |                              | lists them.                        |
| keyword_mix   | Keyword clusters plus prose  | Weighting and flags only where its |
|               |                              | adapter lists them, in the syntax  |
|               |                              | and range written there.           |
| dual_encoder  | Prompt for an open-weight    | Weight syntax, weight range and    |
|               | model with more than one     | the negative field exactly as its  |
|               | text encoder                 | adapter lists them.                |
| typographic   | Graphic design typography    | Exact on-image wording (the sign   |
|               | and environmental layout     | reads ROMAN EMPIRE) marked the way |
|               |                              | its adapter says.                  |
+---------------+------------------------------+------------------------------------+
```

#### 1. The Natural Language Rule (the `natural_prose` family)
A model in this family reads a described scene, with its grammar and the relations between things, better than a list of isolated tags; which models its maker documents this for is in its adapter in ENGINE-CHECK.md §7. Writing `man, warrior, chainmail, sword, mud, cinematic, 8k, photorealistic` produces inferior results compared to:
`"A weathered 50-year-old warrior in riveted iron chainmail rests both hands on his broadsword pommel, standing ankle-deep in black mud under heavy overcast skies."`


**Shelf life:** dated — review 2027-03. The family traits in the table — which encoders, token weighting, weight syntax, separate negative slots — are vendor behaviour and move with each release; they are kept in its adapter in ENGINE-CHECK.md §7, not here, and the research-recency section of this file gives model syntax the shortest life in the package.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** The dated engine record in ENGINE-CHECK.md — Model name, version and flag syntax are owned there.  
`prompt.rule.model_specific_syntax_adapters`

### 4.7 Lens Optics, Sensor Simulation, And Focal Depth Mathematics
Amateur prompts use generic buzzwords like "cinematic depth of field" or "ultra-realistic camera". Professional prompts specify physical optics, focal lengths, and aperture settings:

1. **Focal Length Taxonomy (35mm Equivalent):**
   - *24mm Wide Angle:* Expansive environmental context, dynamic spatial volume, slight peripheral keystoning. Use for monumental architecture and battlefield panoramas.
   - *35mm Environmental Portrait:* Natural human field of view with balanced subject-to-surrounding proportions. Use for domestic interiors and master establishing setups.
   - *50mm Standard Prime:* Flawless, undistorted perspective matching human eye vision. Use for narrative two-shots and medium coverage.
   - *85mm Portrait Telephoto:* Flattens facial facial depth, eliminates nose distortion, compresses background layers, and isolates the subject. The gold standard for hero close-ups.
   - *100mm Macro Probe:* Microscopic tactile resolution on small objects (water drops on papyrus, stylus engraving clay, fingertips tracing an iron scar).
2. **Aperture & Depth of Field Calibration:**
   - `f/1.4 to f/2.0 (Shallow Focus):` Razor-thin focal plane anchored strictly to the iris of the hero eye; creamy spherical bokeh obscuring messy background extras.
   - `f/5.6 to f/8.0 (Deep Field):` Crisp architectural clarity across foreground, midground, and background planes; mandatory for location master plates.
3. **On flat 2D, cel-shaded or cartoon work, none of the above is written at all.** There is no lens
   and no aperture in drawn animation, so a focal length and an f-stop are instructions to a camera
   that is not in the room — at best ignored, at worst returned as a photographic blur laid over line
   art. The animation carve-out in law 5 governs: the frame still says how deep it reads and where
   its light comes from, in the language the medium actually has. **Focal length is replaced by the
   drawn framing and the background treatment** — how much of the world the panel holds, and whether
   the background is a detailed plate or a flat tonal field. **Aperture and depth of field are
   replaced by tonal separation and detail drop** — the background held one flat step back from the
   subject, foreground elements simplified. **Kelvin, per law 8, is replaced by the palette
   temperature in words.** 3D and rendered-CG work keeps the whole table above, because a virtual
   camera has a genuine focal length and a genuine aperture.


**Yields to:** `anime.dof_2d` — Flat 2D or cel work: no lens, tonal separation instead.  
`prompt.rule.lens_optics_sensor_simulation_and_focal_depth_mathematics`

### 4.8 Dual-Frame End Keyframe Engineering
A dual-frame video model interpolates motion between two static image keyframes. Whether the model on this project is one is a fact the dated engine record establishes and writes down — [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), the `end frame accepted` line and the resolutions beside it; do not assume it from a model name, and do not name a model here. Generating an End Keyframe requires strict clone-and-modify discipline:

1. **Step 1: Clone the Start Frame Prompt:** Copy the approved Start Keyframe prompt in its exact entirety.
2. **Step 2: Modify Strictly the Dynamic Motion Vectors:**
   - *Subject Pose:* Alter only the terminal physical pose (e.g., change `right hand resting on desk` to `right hand raised holding papyrus scroll 30 centimeters above desk`).
   - *Eyeline:* Shift gaze direction (e.g., change `gaze screen-left` to `gaze locked directly into camera lens`).
   - *Kinetic Environment:* Adjust progressive environmental effects (e.g., change `smoke rising from candle` to `candle blown out, thin smoke tendril curling upward`).
3. **Step 3: Freeze Immutable Tokens:** Never alter lighting Kelvin, room architecture, wall color hex codes, or character wardrobe tokens between Start and End keyframes. **A value can only be held constant if it came from somewhere**: take the Kelvin figure from `light.kelvin_reference` once, for the scene, and write the same figure into both frames. Any discrepancy causes the video model to warp and boil the background during motion interpolation.
4. **Step 4: Name the pair.** The two files are `kf-start` and `kf-end` at the same scene-shot coordinates: `nineveh-reel_kf-start_S01-SH05_a_v1.png` and `nineveh-reel_kf-end_S01-SH05_a_v1.png`. They share the variant letter and the version, because they are one shot's two ends and not two attempts at one image. Never `a` and `a2`: that is the role-first rule, and the video stage reads them by role into `start_frame_asset_id` and `end_frame_asset_id`.


**Yields to:** `ai.image_to_video` — The engine record does not accept an end frame.  
`prompt.rule.dual_frame_end_keyframe_engineering`

### 4.8b Every example in this module is bound by Law 3
The worked prompts below and in section 9 are illustrations of slot order and vocabulary. Two of them
run near 150 words. **That is fine** - law 3 sets no cap, and a frame carrying a 45-word verbatim
lock plus seven slots needs the room. What whoever reviews the batch rejects is a paraphrased lock
or a missing element, never a long prompt.

**Order wins over length, always.** Before dispatching any prompt, check the lock is first and whole.

**There is nothing to cut** (law 3). A long prompt is a long prompt. Where a prompt is genuinely
padded, remove **words that carry no
information** - starting at Slot 7 and working up, never Slot 1 - but **never remove an element of
the image to reach a number.** The lock sentence is quoted whole (a shot that shows only part of the character quotes its
visible parts, never the face clauses — law 4); a prompt that lost it is
rewritten with it before it leaves this module.


`prompt.rule.b_every_example_in_this_module_is_bound_by_law_3`

### 4.9 Prompt Generation Failure Recoveries And Troubleshooting

| Observable Generation Defect | Root Latent Cause | Immediate Craft Recovery Protocol |
|---|---|---|
| The Wax Museum Face | Over-smoothed skin texture caused by generic beauty tokens | On photoreal work, inject tactile dermal tokens: `visible open pores, fine vellus facial hair, micro-wrinkles, natural skin mottling`. On rendered-CG or flat drawn work there are no pores to add: the waxy face is the glossy default, answered by the Tier 1 list for that render mode in `prompt.rule.negative_prompting_taxonomy`, never by skin tokens |
| Comma Soup Glitch | Model ignores subject directives due to disorganized comma tags | Reconstruct prompt into the Seven-Slot Order: Subject -> Pose -> Optics -> Light -> Room -> Material -> Spec |
| The Six-Finger Hand Anomaly | Hand position unspecified or described vaguely as "holding object" | Lock anatomy explicitly: `calloused five-fingered hand firmly grasping the wooden shaft with individual distinct knuckles` |
| Background Hallucinations | Model fills empty background space with modern clutter or fantasy runes | Explicitly specify background geometry: `bare flat mudbrick wall, zero decorative shelving, single wooden lintel doorway` |


`prompt.rule.prompt_generation_failure_recoveries_and_troubleshooting`

### 4.10 Negative Sizing and Aspect Resolution

Two of the three things this section used to size are genuinely determined — the negative budget is a
range, and the resolution is read from a dated record. **The third was not, and it is gone.**

#### 1. Prompt Word Budget and Seven-Slot Allocation

**There is no word budget formula, and there never was a usable one.** This section used to carry
three `clamp()` expressions built on a `Scene_Complexity_Index` that **nothing in this package
defined** — not its scale, not its inputs, not how to compute it — under a sentence claiming the
budgets were computed deterministically. An agent meeting that formula invented the index, which
made the arithmetic look precise and made it arbitrary. It also contradicted law 3, which wins:
**there is no cap**, and nothing is removed from the image to reach a number.

What survives is the allocation, which is a real instruction:

- `Slot 1 (Subject & Verbatim Identity)`: copy the complete 30 to 45-word lock sentence — or, where the shot shows only part of the character, its visible parts and never the face clauses (law 4). For a non-character focal subject, describe it directly.
- `Slots 2 through 7`: divide the rest of the prompt across Action & Pose; Framing, Elevation & Optics; Lighting Architecture; Environment & Palette; Surface Material Physics; and Technical Specifications & Exclusions. Each slot must contain at least three concrete words.
- **The length is whatever those seven slots need.** A tight prompt is usually a better one, so cut words that carry no information — but the lock is quoted whole whatever the count (a shot showing only part of the character quotes its visible parts, law 4), and no described element leaves the image to shorten it.

#### 2. Negative Exclusion Budget
```text
Negative_Word_Budget = 15 to 30 words per risk class
```
Select only shot-relevant exclusions, ordered by tier priority: **Tier 0 the project's own prohibitions**, then Tier 1 Anatomy, Tier 2 Anachronisms, then Tier 3 Artifacts. The range is per risk class, not a total across tiers, as the negative-budget law at the head of this file states: a class below 15 words is under-specified, and a class above 30 words is cut back to the risks this shot carries — a tier that cannot be shortened without losing a real risk is kept and the overrun recorded, so a shot carrying three classes runs longer, and that is correct.

**Tier 0 is outside this budget and is never omitted.** The 15-to-30 range applies to each of Tiers 1 to 3 in turn, which are this shot's risk assessment. Tier 0 is the project's standing rules - see 4.4 and [`FORBIDDEN-GLOBAL.md`](../FORBIDDEN-GLOBAL.md) - and it is copied in whole whatever the count reaches. This paragraph exists because the assembly order here once listed Tiers 1 to 3 only: a writer following this section and not 4.4 shipped every prompt in the project with no canon and no heritage rules in it, and nothing told them.

#### 3. Verified Native Resolution Table

This guide never fills this table from memory. It copies the row for the selected model from the dated record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md):

| Selected model (engine selection) | Delivery aspect | Native width px | Native height px | Evidence rung | Verified at | Evidence reference |
|---|---:|---:|---:|---|---|---|
| `selected_model` | `delivery_aspect_ratio` | `verified_px` | `verified_px` | `[OFFICIAL]`, `[CACHED]`, or `[BENCH]` | ISO-8601 timestamp | vendor URL plus response artifact or dated cache record |

The row is complete only when all seven cells come from the dated record. If the record has not been filled, or the selected model has no verified native tile for the requested aspect, set `pending_engine_check` and carry it forward — but do not crop, pad, upscale or invent a resolution, and do not reshape the image to suit a tile the engine happens to offer. If no engine offers the aspect this piece needs, choose the engine whose native tile is closest, generate at that tile and extend the frame to the brief's aspect with an outpaint pass (never a crop), record the choice under `decisions`, and carry on. The aspect is the brief's and does not change.


**Yields to:** `prompt.rule.b_a_reference_sheet_is_not_a_shot` — The target is a sheet, not a shot.  
`prompt.rule.negative_sizing_and_aspect_resolution`

### 4.10b A reference sheet is not a shot, and its rules are different

Section 4.10 and the Tier 3 negatives below assume a shot: a clean neutral mid-gray ground, no text,
no typography, because a shot with a caption in it is ruined.

A reference sheet is the opposite kind of image. The templates in [`sheet-character.md`](./sheet-character.md), [`sheet-location.md`](./sheet-location.md) and [`sheet-props.md`](./sheet-props.md) are laid out on
a cream museum-catalog ground with a header, pose labels, an accessories grid and a colour strip.
That lettering is the point of the sheet, not contamination.

So when the target is a character, location or props sheet:

- Follow the template's ground and layout, not 4.10's neutral gray.
- Do not add `text, typography` to the negatives; the sheet needs its labels.
- Drop the Tier 3 layout negatives as well, `multiple panels, borders, collage`. Those three words
  describe what a reference sheet is, so on a sheet they cancel the brief. They stay in force on
  every shot.
- The faceless rule in 4.11 still applies: a sheet for a character the identity record left undecided shows the body,
  the wardrobe and the silhouette, and no face.

For every other image, 4.10 governs and the template is irrelevant.


**Yields to:** `prompt.rule.negative_sizing_and_aspect_resolution` — Any image that is not a sheet.  
`prompt.rule.b_a_reference_sheet_is_not_a_shot`

### 4.11 Stated Defaults for Middle-Pipeline Stall Points

When upstream prompt components are missing during prompt engineering, apply these stated defaults immediately:

```text
IF character verbatim identity sentence has not been supplied by the character record or the continuity record
  THEN do NOT synthesize a face. A missing sentence usually means the production plan deliberately left the face
       undecided, which is the normal case on heritage work where figures are shot from behind, at
       distance or occluded. Inventing one here overrides that decision silently and puts a stranger
       in the plate.
  THEN instead frame the figure without a face: from behind, in silhouette, at distance, occluded by
       an object, or cropped below the eyeline. Slot 1 carries the body, the wardrobe and the posture,
       and no face words at all. Record `face: not_specified_by_director` in the prompt record.
  AND if the shot genuinely requires a readable face, the agent writes the face itself: the brief, the canon and the
       skill, the web, then its own best choice, as a `project_scoped` sentence recorded under `decisions`. No shot and
       no batch stops for it.

IF camera lens focal length and aperture are unspecified
  AND the render mode is photoreal, 3D or rendered CG
  THEN default to `50mm prime lens, f/2.8 aperture, natural optical depth of field with sharp subject focus and soft background falloff`, recorded as `assumed`
  AND must be verified against cinematography design in the shot plan.
  ELSE the render mode is flat 2D, cel-shaded or cartoon, and the lens field is empty BY DESIGN, not
       by omission - there is no lens. Write nothing optical. Put the drawn equivalent in its place:
       `background held one flat tonal step back from the subject, foreground detail simplified`, and
       record `optics: not applicable, drawn render mode` rather than `assumed`.
       **Never default a drawn frame to a focal length.** On animated work this field is always
       empty, so a default written without this branch fires on every single shot - which is the one
       way the animation carve-out in law 5 gets silently reversed.

IF aspect ratio parameter is unspecified in project identity
  THEN default to a 16:9 frame for horizontal video or 9:16 for vertical social video, recorded as `assumed`;
       the engine record's adapter for the selected family decides whether that is written as a flag, a field or a UI selection
  AND must never be converted by post-render cropping.

IF image texture and film medium are unspecified
  THEN branch on the project's render mode, recorded as `assumed`:
       - live-action / photoreal -> `35mm photochemical film texture, fine organic grain structure,
         Kodak Vision3 250D color negative tone, zero digital noise reduction, zero plastic skin smoothing`
       - 2D / 3D / cel-shaded / cartoon -> the project's declared art style from `anime-2d.md` and
         `render-style.md` (line weight, ink treatment, colour handling); no film stock and no grain
       - product, packshot or clean studio -> `clean digital capture, no grain, no halation`
  AND must be applied to prompt suffix, and must be verified against the shot plan.
```


**Yields to:** `ident.frozen_sentence` — The shot genuinely needs a readable face.  
`prompt.rule.stated_defaults_for_middle_pipeline_stall_points`

## 5. Decision Rules

| Generation Need | Latent Risk | Mandatory Prompt Engineering Rule |
|---|---|---|
| Recurring lead character across multiple camera angles | Model alters facial features, hair length, and eye color | Quote the approved character sentence's frozen Mandatory Verbatim Sentence word-for-word in every prompt; specify camera height and lens to isolate angle |
| Close-up shot of hands holding a historic prop | Model produces six fingers, fused knuckles, or distorted palms | Explicitly specify hand pose ("calloused right hand firmly gripping the bone handle with five distinct fingers"); place prop in focal sweet spot |
| Ancient historical setting (e.g., 500 BC to 100 AD) | Model inserts modern elements (bleached teeth, zippers, glass windows) | Inject Tier 2 historical negative tokens; explicitly specify period materials (unbleached wool, iron rivets, oiled parchment, tallow candles) |
| Two or more characters in one frame | Model merges both faces into identical clones or swaps costumes | **Separate them, do not remove one.** The failure mode is sameness, so the fix is difference: one face sharp and the other turned or in profile, over-the-shoulder with the near figure as a soft silhouette, one backlit against the other, one in motion blur, distinct silhouettes, clearly different heights, builds, wardrobe colours and hair, and a separate reference image per character. Give each a distinct action verb. Single-character coverage is one option among these, never the automatic answer: a confrontation, a two-hander, a duel and a reunion all need two people in the frame |
| End frame for dual-frame video interpolation | Background shifts or lighting changes during motion interpolation | Duplicate the exact Start Frame prompt; change only the action verb and subject terminal pose; keep lighting and environment text identical |
| Wide panoramic landscape with small human figures | Characters render as featureless blurs or mutilated blobs | Keep the people and make them read. Describe them by silhouette, posture and action rather than by face, since at that scale the face was never going to carry anyway: a raised spear line, hunched runners, a rank breaking, banners leaning in one wind. Give the crowd a direction and a verb. If the shot truly needs a readable face, that is a second, tighter shot, not a reason to empty this one |

## 6. Research Protocol

When drafting prompts for authentic historical, technical, or specialized visual subjects, execute targeted research queries:
- `authentic fabric weave {historical_period} {culture} macro`: Discover precise tactile terminology for textiles (e.g., herringbone twill, raw flax slub, fulled wool).
- `optical characteristics {lens_brand_or_focal_length} portraiture`: Identify authentic bokeh shape, barrel distortion, and field curvature terms.
- `negative prompt tokens artifact prevention {target_model}`: Identify model-specific negative triggers and token weighting rules.
- `historical footwear boots {region} {date_BC_or_AD}`: Verify period-accurate footwear descriptions to avoid modern leather shoe soles.

### 6.1 Research Recency and Shelf Life Mandates
- **Domain Shelf Life:** Model-specific prompt syntax, negative token limits, aspect ratio flags, and parameter weights carry a 30-day shelf life. Optical lens characteristics and lighting principles endure across 24 months. Historical textile, costume, and material evidence endures permanently unless updated by primary archaeological findings (dated in BC or AD).
- **Date-Stamping:** Every technical query and model prompt syntax profile recorded in the prompt deliverable under this stage must include an explicit verification date.
- **Re-Verification Requirement:** Expired prompt parameters or model token weights must be queried anew against vendor documentation; never rely on stale model assumptions.
- **Capability Verification:** Never assert an undocumented parameter, aspect ratio flag, or negative prompt weight; search the engine's current documentation first; a flag it does not document is left out, the prompt is written without depending on it, and the choice is noted under `decisions`.


`prompt.rule.research_recency_and_shelf_life_mandates`

## 7. Output Contract

**Where the `asset_id` values below come from.** They are illustrative tracking tokens assigned when keyframe still assets land on disk. This module specifies the prompt structure and tracks assigned asset references.


This skill outputs structured prompt specifications to the Phase 7 Image Prompt deliverable (Markdown / Keyframe Stills Plan).

```json
{
  "status": "submitted",
  "produced": [
    "phase_07_image_prompt_deliverable"
  ],
  "locked": {
    "target_model": "as selected in the engine capability profile; this example leaves it unquoted on purpose",
    "prompt_family": "natural_prose",
    "delivery_aspect_ratio": "16:9",
    "render_modes": {
      "A": "photoreal"
    },
    "prompt_batch": [
      {
        "shot_id": "S03-SH15",
        "render_mode": "A",
        "canonical_filename": "roma_kf_S03-SH15_a_v1.png", "asset_id": "AST-000042",
        "prompt_type": "cinematic_keyframe_start",
        "full_positive_prompt": "Medium Close-Up eye-level shot of 60-year-old patrician Roman male, gaunt aristocratic face, hollow sunken cheeks, sharp aquiline hooked nose, receding thin silver-white hair combed forward, clean-shaven, pale fatigued skin, sharp dark-brown eyes with dark circles under eyes, wearing heavy off-white wool toga praetexta with purple border. He sits behind a weathered oak desk in the right third of the frame, both hands resting on an unrolled wax tablet, his intense gaze directed toward screen-left. Low-ceiling tablinum chamber, rough dressed limestone walls (#C8B89A), terracotta tile floor (#8B4513), bronze oil lamp on desk casting warm 1900K amber glow on his right cheekbone, cool morning daylight entering doorway from left. Rich surface micro-texture of porous stone, visible coarse wool weave, skin pores, and deep worry lines between brows. Shot on 65mm anamorphic prime lens, f/2.8 shallow depth of field, natural film grain. [16:9 aspect and exclusions, written in the selected family's verified syntax: text, watermark, modern clothing, bleached teeth, plastic]",
        "prompt_slots": {
          "subject_verbatim": "60-year-old patrician Roman male, gaunt aristocratic face, hollow sunken cheeks, sharp aquiline hooked nose, receding thin silver-white hair combed forward, clean-shaven, pale fatigued skin, sharp dark-brown eyes with dark circles under eyes, wearing heavy off-white wool toga praetexta with purple border.",
          "action_and_pose": "Seated behind weathered oak desk, right third of frame, hands on wax tablet, looking screen-left.",
          "framing_and_optics": "Medium Close-Up, eye-level 1.3m, 65mm lens, f/2.8 shallow depth of field.",
          "lighting": "Key warm 1900K amber oil lamp right, cool morning daylight fill left.",
          "environment_and_palette": "Limestone walls (#C8B89A), terracotta floor (#8B4513), oak desk (#3E2723).",
          "material_physics": "Porous stone texture, coarse woolen twill, skin pores, aged wood grain.",
          "technical_specifications_and_exclusions": "16:9 native tile from the verified model record; no text, watermark, modern clothing, bleached teeth, or plastic skin."
        },
        "negative_prompt_block": "bad anatomy, extra fingers, fused hands, crossed eyes, plastic skin, modern clothing, wristwatch, zippers, modern eyeglasses, bleached teeth, modern dentistry, text, watermark, border, split screen"
      }
    ]
  },
  "_render_modes_note": "`render_modes` names every look the piece uses and `render_mode` on each prompt says which one that prompt is in. A single-look piece writes one entry and tags every prompt with it, which costs a line and makes the value explicit rather than assumed. A piece that alternates - a reconstruction documentary cutting between photographed footage and drawn rebuilds - writes two, and the tag is what carries the Mode & Look cell from the Phase 3 shot table through to Phase 8. Without this field the mode does not survive the handoff at all: the optics, the depth cue and Tier 1 and Tier 2 of the negative block each answer differently per look, and the next phase has to guess.",
  "open": [
    "verify_aspect_ratio_flag_compatibility_with_target_api"
  ],
  "forbidden": [
    "No relative references to earlier prompts ('same man', 'earlier room')",
    "No omission of the Mandatory Verbatim Character Sentence",
    "Use BC and AD dating only",
    "No non-English prompt text, except on-screen text the audience reads, whose treatment is routed through in-frame-text.md"
  ],
  "assumptions": [
    "Model API accepts comma-delimited positive prompt strings and dedicated negative prompt payloads"
  ],
  "research_used": [
    {
      "claim": "Diffusion foundation models suppress plastic skin artifacts when prompt specifies natural pores and fine fabric weave",
      "source": "assumption — illustrative worked example; no source was read for this claim",
      "read_at": "2026-09-07T08:00:00.000Z",
      "domain": "ai_tool_limits",
      "shelf_life_days": 30,
      "status": "fresh"
    }
  ],
  "declared_decisions": [],
  "_decisions_note": "Creative choices this stage made where nothing dictated one. Each entry is {what, why, alternative_offered}. Whoever reviews the batch reads this field to tell a declared decision from an unsourced claim: a choice listed here is never a finding, and a choice nobody listed looks exactly like an invention nobody sourced. A stage that made real choices and declared none has removed the only evidence it was creating rather than guessing. One line per decision.",
  "updated_at": "2026-09-07T09:40:00.000Z"
}
```

## 8. Quality Bar And Failure Modes

### What High Quality Looks Like
- **Total Independence:** Every prompt functions as a completely self-contained generation unit without external dependencies.
- **Physical Precision:** Prompts describe measurable physical attributes, optical focal lengths, and lighting physics rather than literary sentiment.
- **Strict Verbatim Discipline:** Recurring characters carry their locked descriptive sentence at its frozen length, without alteration or abbreviation; a shot that shows only part of a character carries its visible parts, never the face clauses (law 4).
- **Flawless Heritage Integrity:** Modern synthetic materials, contemporary dental aesthetics, and anachronisms are rigorously barred through targeted positive phrasing and negative exclusions.


`prompt.rule.what_high_quality_looks_like`

### Failure Modes And Immediate Remedies

| Failure Mode | Observable Defect | Immediate Craft Remedy |
|---|---|---|
| The Relative Prompt Fallacy | Writing "Marcus stands up angrily from the table in the previous shot" | Re-insert the full Mandatory Verbatim Sentence; specify current room coordinates and standing pose |
| The Romantic Literary Fluff | Writing "A noble warrior whose eyes hold the tragic sorrow of a broken empire" | Replace with physical metrics: "Downcast hooded hazel eyes, furrowed brow, tightened jaw muscles, mouth turned downward" |
| The Anachronistic Smile | Ancient historical character displays sparkling white porcelain dental veneers | Add negative tokens: `bleached teeth, modern dentistry, veneers, cosmetic smile`; specify neutral closed mouth |
| The Multi-Character Identity Melt | Prompting two named heroes in the same frame, causing faces and clothes to merge | Separate them, do not remove one: make the two different — silhouette, build, wardrobe, action, a reference image each — as the Decision Rules table does for the same case; two single OTS or hero close-up prompts are one option among these, never the automatic answer — split to that coverage only when the beat does not need a shared frame, or when separation still fails after one controlled retry |
| The Missing Optics Specification | Omitting focal length, resulting in distorted wide-angle perspective on facial close-ups | On photoreal and rendered-CG work, lock explicit focal length: `Shot on 85mm portrait telephoto lens, flat eye-level perspective`. On flat drawn, cel or cartoon work there is no lens: state the drawn framing in words instead, per `prompt.rule.lens_optics_sensor_simulation_and_focal_depth_mathematics` |


`prompt.rule.failure_modes_and_immediate_remedies`

## 9. Worked Example

### Context
Developing conditioning keyframe prompts for a dramatic sequence set in 701 BC during the Neo-Assyrian siege of Lachish: King Hezekiah's royal scribe Eliakim inspecting fortress walls at sunrise.


`prompt.rule.context`

### Prompt Manifest & Execution

#### 1. Asset 1: Character Model Sheet (Pre-Production Reference Plate)
- **Objective:** Establish baseline anatomical and costume reference for downstream consistency.
- **Which of the two cases this is:** a bare turnaround, no template. So 4.10's neutral ground
  applies and the text negatives stay. Read 4.10b before copying this: **a sheet built on a template
  from one of the sheet templates is the other case**, and it takes the template's cream ground, its header,
  its pose labels and its accessories grid, with `text, typography` and the Tier 3 layout negatives
  `multiple panels, borders, collage` all dropped. Copying this prompt for a template sheet returns
  one unlabelled figure and none of the layout that makes a sheet useful.
- **Prompt, bare turnaround case:**
  `"Full-body studio character reference sheet of 45-year-old Judean male royal scribe, lean contemplative face, prominent straight nose, trimmed dark-brown beard with streaks of silver, intelligent dark-brown eyes, olive skin weathered by desert wind, shoulder-length dark wavy hair bound by thin leather cord. Wearing long ankle-length unbleached off-white linen tunic with blue-dyed wool fringe at hem, woven brown leather girdle at waist holding ink horn and bronze stylus, leather thong sandals on feet. Neutral relaxed stance, front-facing, standing against uniform flat neutral gray background (#808080). Soft balanced diffused studio illumination, zero harsh shadows. Shot on 85mm prime lens, f/8 deep focus, ultra-fine fabric weave texture, visible skin pores. [1:1 aspect and exclusions, written in the selected family's verified syntax: modern clothing, eyeglasses, bleached teeth, text, watermark]"`
- **Length:** this example runs about 150 words, well past the figure in 4.10. **That is not a
  defect** - law 3 sets no cap, and a frame carrying a full verbatim lock plus seven slots needs the
  room. Order it lock-first so a weaker model drops the tail rather than the identity, and **cut
  only words that carry no information, never an element of the image.**

#### 2. Asset 2: Scene Keyframe Start Frame (Shot 01 Conditioning Still)
- **Objective:** First conditioning keyframe for a 4.0-second push-in shot atop the fortress ramparts.
- **Prompt:**
  `"Medium Close-Up eye-level shot of 45-year-old Judean male royal scribe, lean contemplative face, prominent straight nose, trimmed dark-brown beard with streaks of silver, intelligent dark-brown eyes, olive skin weathered by desert wind, shoulder-length dark wavy hair bound by thin leather cord, wearing unbleached off-white linen tunic with blue wool fringe. He stands at the parapet of a mudbrick fortress wall in the left third of the frame, right hand resting on weathered limestone battlement, gaze fixed pensively toward the distant horizon screen-right. Early sunrise light casting long dramatic golden-hour shadows at 15-degree angle, warm 3500K golden-hour sunlight illuminating his profile, cool ambient dawn sky filling shadows. In the background right, distant rolling hills of the Judean Shephelah under pale morning mist. Tactile surface micro-texture of sun-baked mudbrick (#B58A63), coarse linen weave, and weathered stone. Shot on 50mm cinematic prime lens, f/2.8 shallow depth of field. [16:9 aspect and exclusions, written in the selected family's verified syntax: modern military equipment, text, watermark, signature, wristwatch, asphalt, sunglasses]"`

#### 3. Asset 3: Negative Prompt Block (Shot-Specific Execution Payload)
- **Payload:**
  `bad anatomy, extra fingers, fused hands, crossed eyes, plastic skin, modern clothing, wristwatch, synthetic zipper, modern eyeglasses, bleached teeth, modern dentistry, asphalt roads, electrical wires, text, watermark, border`


**Yields to:** `prompt.rule.b_a_reference_sheet_is_not_a_shot` — The sheet is built on a template, not bare.  
`prompt.rule.prompt_manifest_execution`

## Fast path

For rapid single-shot keyframe or concept image prompt generation:
1. **Minimum inputs:** the approved character sentence or the project-scoped character sentence when a character appears; location environment; composition from the Phase 3 shot plan or Phase 6 storyboard layout, an approved layout for reference-sheet work, or an accepted static-composition brief on the image-driven route; delivery aspect ratio; and the model record's selected model, syntax profile, and dated native-resolution row.
2. **Steps:**
   - Hold the seven-slot schema from 4.1 and order it lock-first. The word figures in 4.10 are the
     shape of a tight prompt, not a ceiling: a complex frame is written at the length it needs, and
     nothing is dropped from the image to hit a number (law 3).
   - Inject the complete 30 to 45-word mandatory character sentence into Slot 1 without alteration, then reserve at least three words for each remaining slot.
   - Build one shot-specific negative block, 15 to 30 words per risk class it carries (Tier 0 copied whole, outside the budget).
   - Copy the exact native width and height from the verified resolution row. If that row is absent, write `pending_engine_check` in its place and carry on — see [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) §3.
3. **Produces:** Fully rendered, model-ready positive prompt string, negative prompt string, and exact tile resolution parameters.
4. **Deliberately skips:** Camera velocity vectors, motion trajectories, and video frame interpolation; these must be authored by the video prompt guide before video rendering in the spend gate.
