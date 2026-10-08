# Handoff Protocol: Storyboard Layout to Image Keyframes (Phase 6 → Phase 7)

This document governs the operational handoff from Phase 6 (Storyboard Layout & Blocking) to Phase 7 (Image Prompt Engineering & Keyframes). 

The primary rule of the pipeline: **downstream stages build upon upstream approvals and may never silently redesign them.** An approved storyboard panel establishes composition, aspect ratio, actor blocking, and depth layers. Phase 7 translates these spatial staging decisions into optical prompts and surface shaders without altering the core staging.

---

## 1. Primary Invariants Transferred to Phase 7

For every storyboard panel transitioning to image generation, Phase 6 hands down:
1. **Panel ID & Shot Index**: Stable ID mapping directly to the Phase 3 Shooting Script table.
2. **Shot Scale & Framing**: Preserved optical scale (EWS, WS, MS, MCU, CU, ECU) established in Phase 3/6.
3. **Subject Blocking & Screen Direction**: Exact positions of actors within the frame (left, center, right) and eyeline vectors (180° rule).
4. **Depth Planes & Occlusion Hierarchy**: Foreground, midground, and background relationships.
5. **Locked Aspect Ratio & Safe Areas**: Native generation tile at the ratio Phase 1 Question 4 recorded for this deliverable (9:16, 16:9, 1:1, 4:5, or the stated other), with that surface's margin clearances.
6. **Color Script & Palette Accents**: the dominant 60:30:10 palette tones, authored here by `board_arch.color_palette_swatch_footer`. This is the colour script; Phase 7 turns it into the exact values it locks as `palette` in `project.yaml` (`PROJECT-STATE.md` names Phase 7 as the writer), and no later phase re-decides them.
   **Kelvin is not handed forward from this phase** — Phase 6 does not author colour temperature and has no card that produces it. Lighting temperature is Phase 7's, under its law 8 (motivated origin and Kelvin). What travels from here is the palette and the intent of the light — hard or soft, warm or cool, where it comes from — and Phase 7 sets the number.

---

## 2. Character & Environment Continuity Locks

- **Frozen Identity Sentence**: Phase 7 authors the 30-to-45-word character description (`ident.frozen_sentence`, in `../phase-07-image-prompt-engineering/identity-consistency.md`) and quotes it verbatim into Slot 1 (a panel that shows only part of the character — hands, a back — carries only its visible parts, never the face clauses: `HOW-PHASE-7-WORKS.md` law 4); Phase 6 lists what it must hold — role, wardrobe and what must not change — from the panels. Wardrobe travels as its own line beside the frozen sentence, not inside its word count, and is written only into the image and character-sheet prompts, never into a video prompt.
- **Reference Asset Binding**: Attach verified character turnaround sheets (`sheet-character.md`) and location master plates (`sheet-location.md`).
- **Wardrobe State Continuity**: The prompt must explicitly state the approved costume and distress state (clean, travelled, torn, wet).
- **Render Mode**: carry the panel's render mode across with it, from the set below.

<!-- GENERATED:render-modes — do not edit by hand. Generated in the source package -->

**The render modes.** Every value this field takes, and what each one means. Generated from the table in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which is the authority — widen a definition there and it widens everywhere, which is the failure this block replaces.

| Value | What it means |
| :--- | :--- |
| `photoreal` | Made to read as photographed. Real optical values: focal length, aperture, depth of field, Kelvin, and a film stock or sensor look where one is wanted. |
| `rendered_cg` | 3D / rendered CG: rendered geometry with a virtual camera, so the optical values apply — but no film gate, so grain is an added effect rather than a property. State the **surface** as well as the optics: what the thing is made of. |
| `flat_2d` | Flat 2D / cel: drawn or painted: cel, ink, watercolour, gouache, a painterly animated look. No lens, no aperture, no Kelvin, no stock. The art style, line weight, ink and colour treatment replace them, and the light direction and palette temperature are stated in words. |
| `stop_motion` | Stop motion / physically made: photographed objects moved frame by frame. Real optics, handmade surface, and a motion signature of its own — uneven cadence, held extremes, no true motion blur. |
| `built` | **Assembled in a graphics or motion layer rather than generated at all** — a chart, map, counter or diagram built from real values; an animated diagram; **a typographic or kinetic-text sequence**; a title card. It reaches no image or video engine, carries no optical values and no art style, and a prompt written for it returns plausible nonsense. Where a shot is `built`, the engine record reads `engine: none - built`. |
| `multi_look` | Two or more looks: the piece deliberately alternates. Declare each constituent look by its machine value, say what the cut between them means, and tag every row and every prompt with the one it is in. |

<!-- /GENERATED:render-modes --> On a piece that alternates two looks, carry the panel's **MODE** cell, not a project value. It decides which vocabulary Phase 7 fills every optical slot with and which branch of the negative tiers applies, so a handoff that omits it makes the next phase guess, silently and per shot.

---

## 3. Dual-Frame Keyframe Conditioning (For Video Routes)

When the downstream video model (Phase 8) utilizes first-and-last-frame interpolation:
1. **Start Frame (Frame A @ 0.0s)**: Built from the storyboard panel's initial composition.
2. **End Frame (Frame B @ the clip's verified duration)**: built with exactly ONE primary physical transformation or spatial displacement across that interval. The duration is the value the engine-selection step verified for this run — never a number carried from a previous project.
3. **Held Invariants**: Lighting angles, subject identity, wardrobe, and environment must remain identical between Frame A and Frame B.
4. **Single Frame Fallback**: For engines that only support single-image start frames, provide a single hero keyframe with motion reserve headroom.

---

## 4. Discrepancy & Redesign Protocol

- Phase 7 prompt engineers may not alter character wardrobe, change camera angles, or shift the narrative event established in Phase 6.
- Where a generation will not hold an element of the approved panel — a face at distance, a crowd, a carved inscription — the first remedy is the prompt (silhouette-and-action description, a tighter conditioning reference, a separate plate composited in) and the second is a different engine. Changing the film to suit the tool is the last resort, never the default: a figure is not removed, turned away or reduced to a silhouette to make a generation succeed. If the shot genuinely must be reframed, the agent chooses the reframe that best keeps the shot's intent, on that one shot, records it under `decisions` as an explicit override with its reason, and continues — not a batch-level workaround.
