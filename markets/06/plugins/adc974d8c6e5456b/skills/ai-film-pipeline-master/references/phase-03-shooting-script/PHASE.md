---
name: phase-03-shooting-script
description: "Phase 3: Shooting Script & AV Directing. Sole decision owner of camera setups, shot sizes, elevation angles, transitions, J-cuts, L-cuts, and two-column audio/video scripts across 768 core shooting craft cards (773 total headings). Use when converting a screenplay into an exact shot-by-shot visual and auditory shooting plan. Trigger on: shooting script, shot list, camera shots, shot sizes, camera angles, J-cut, L-cut, شوت لست، سكريبت تصوير، لقطات كاميرا، زوايا تصوير، احجام اللقطات، انتقالات مشهدية."
---

# Phase 3: Shooting Script & Technical Breakdown

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

Welcome to **Phase 3: Shooting Script & Technical Breakdown**, backed by **768 core craft cards (773 total headings)**.

Phase 3 is the exclusive decision owner for Camera Setups, Shot Scale, and Camera Angles. It converts the dramatic screenplay into an exact, numbered Two-Column AV Technical Shooting Script that feeds directly into Storyboarding (Phase 6) and Image Prompting (Phase 7).

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The contract for this phase](#the-contract-for-this-phase)
- [Master Documentation](#master-documentation)
- [Primary Camera Setup Bibles (Owned by Phase 3)](#primary-camera-setup-bibles-owned-by-phase-3)
- [Inter-Phase Cross-Links](#inter-phase-cross-links)
- [Files in this phase](#files-in-this-phase)

<!-- /GENERATED:toc -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `render_mode`, `looks`, `audio_profile`, `duration_s` |
| **One-of read groups** | `script` or `timing_map` or `existing_picture_timing`; `timing_map` or `measured_duration` or `durations` or `existing_picture_timing` or `duration_s` |
| **Optional reads** | `branch_map`, `lyrics`, `speaker_map` |
| **External inputs allowed** | `script`, `branch_map`, `timing_map`, `existing_picture_timing`, `durations` |
| **Writes** | `shot_table`, `size_angle`, `timing_src`, `durations` |
| **May not re-decide** | `script`, `branch_map`, `render_mode`, `looks` |
| **Execution gate** | — |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `phase-04-audio-narration` | `phase-06-storyboard-layout` |
| `narrated_documentary` | `phase-04-audio-narration` | `phase-06-storyboard-layout` |
| `music_video` | `phase-05-song-generation` | `phase-06-storyboard-layout` |
| `commercial` | `phase-02-screenplay-dialogue` | `phase-06-storyboard-layout` |
| `commercial_narrated` | `phase-04-audio-narration` | `phase-06-storyboard-layout` |
| `storyboard_only` | `phase-02-screenplay-dialogue` | `phase-06-storyboard-layout` |
| `interactive_branching_silent` | `phase-02-screenplay-dialogue` | `phase-06-storyboard-layout` |
| `interactive_branching_audio` | `phase-04-audio-narration` | `phase-06-storyboard-layout` |
| `data_led_built` | `phase-04-audio-narration` | `phase-06-storyboard-layout` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

---

## Master Documentation
- **[HOW-PHASE-3-WORKS.md](./HOW-PHASE-3-WORKS.md)**: Operational guide to single decision ownership, AV script tables, and downstream inheritance.
- **[INDEX.md](./INDEX.md)**: Categorized catalog of all 768 core craft cards (773 total headings).
- **[LOOKUP.md](./LOOKUP.md)**: Master alphabetical ID lookup table.

## Primary Camera Setup Bibles (Owned by Phase 3)
- **[shot-sizes.md](./shot-sizes.md)**: 21 cards on shot scale (EWS, WS, MS, MCU, CU, ECU).
- **[angle-height.md](./angle-height.md)**: 58 cards on camera elevation (Eye-level, Low angle, High angle, Dutch tilt).
- **[framing-named-shots.md](./framing-named-shots.md)**: 61 cards on named cinematic framing.
- **[cuts-in-scene.md](./cuts-in-scene.md)**: 69 cards on in-scene cuts.
- **[scene-transitions.md](./scene-transitions.md)**: 134 cards on scene transitions.

## Inter-Phase Cross-Links
- **[Phase 6 Storyboard Layout](../phase-06-storyboard-layout/PHASE.md)**: Inherits locked shot sizes and angles to stage composition and actor blocking.
- **[Phase 7 Image Prompt Engineering](../phase-07-image-prompt-engineering/PHASE.md)**: Inherits shot sizes into Slot 3; adds optical lens focal lengths.

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**23 craft files, 768 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md). Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`shot-sizes.md`](shot-sizes.md) | **Shot Sizes** — Shot Sizes & Camera Scale Hierarchy <br>*Cards scoped to: any format* | 21 |
| [`angle-height.md`](angle-height.md) | **Angle, Height and Azimuth** — Camera Angles, Elevations & Geometric Perspectives <br>*Cards scoped to: any format* | 58 |
| [`framing-named-shots.md`](framing-named-shots.md) | **Framing, Relational and Named Shots** — Named Framing Setups & Cinematic Composition <br>*Cards scoped to: any format* | 61 |
| [`cuts-in-scene.md`](cuts-in-scene.md) | **Cuts Within a Scene** — In-Scene Editorial Cuts & Spatial Grammar <br>*Cards scoped to: any format* | 69 |
| [`scene-transitions.md`](scene-transitions.md) | **Scene-to-Scene Transitions and Visual Structure** — Inter-Scene Transitions & Temporal Shifts <br>*Cards scoped to: any format* | 134 |
| [`shot-transitions.md`](shot-transitions.md) | **Shot-to-Shot Transitions** — Micro Shot-to-Shot Transitions & Optical Bridges <br>*Cards scoped to: any format* | 67 |
| [`documentary.md`](documentary.md) | **Documentary, Interview and Reportage** — Documentary Coverage, Realism & Observational Grammar <br>*Cards scoped to: any format* | 123 |
| [`vertical-short-form.md`](vertical-short-form.md) | **Vertical Short-Form** — Vertical Short-Form (9:16 Reels/Shorts) Shot Grammar <br>*Cards scoped to: mostly Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Explainer, Meme / Comedy Edit, among 30 formats* | 46 |
| [`ads-trailers.md`](ads-trailers.md) | **Ads, Trailers and Motion Design** — Commercial TVC & High-Impact Trailer Shot Grammar <br>*Cards scoped to: mostly Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Corporate / Training, among 23 formats* | 59 |
| [`music-video.md`](music-video.md) | **Music Video and Performance** — Music Video Rhythmic Cutting & Performance Grammar <br>*Cards scoped to: mostly Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Dance Film, among 20 formats* | 31 |
| [`kids-content.md`](kids-content.md) | **Kids Content** — Children Content Visual Clarity & Pacing Grammar <br>*Cards scoped to: mostly Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), 2D Animation (Western / Cartoon), 3D CG Animation, among 13 formats* | 27 |
| [`sound-as-visual.md`](sound-as-visual.md) | **Sound as a Visual Tool** — Sound-as-Visual Sync & Sonic Cutting Points <br>*Cards scoped to: any format* | 26 |
| [`vlb-ten-laws.md`](vlb-ten-laws.md) | **1 — The Ten Laws of Visual Craft** — The Ten Laws of Visual Craft — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and re | 1 |
| [`vlb-formats.md`](vlb-formats.md) | **12 — Formats** — Formats — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and read its card here. | 20 |
| [`vlb-genres.md`](vlb-genres.md) | **13 — Genres** — Genres — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and read its card here. | 23 |
| [`vlb-shot-sizes.md`](vlb-shot-sizes.md) | **2 — Shot Sizes** — Shot Sizes — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and read its card here. | 1 |
| [`vlb-cuts-in-scene.md`](vlb-cuts-in-scene.md) | **10 — Cuts and In-Scene Transitions** — Cuts and In-Scene Transitions — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and r | 1 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`cinema-modes.md`](cinema-modes.md) | The five cinema modes — A camera grammar, picked once per sequence and then applied to every shot in it. |
| [`shot-plan.md`](shot-plan.md) | Technical Shot Planning & Directorial Breakdown — The work plan for shots, established after the screenplay and before any visual generation begins. |
| [`vlb-angle-height.md`](vlb-angle-height.md) | Angle, Height and Azimuth — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and read  |
| [`vlb-decision-tables.md`](vlb-decision-tables.md) | Decision Tables — From the Visual Language Bible. Name the change you want in the scene, take the technique it hands you, and read its card in the matching craft file. |
| [`vlb-scene-transitions.md`](vlb-scene-transitions.md) | Scene-to-Scene Transitions — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and read |
| [`vlb-speed-timing.md`](vlb-speed-timing.md) | 4.6 Speed and Timing — the Dial Everyone Forgets — From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique  |

<!-- /GENERATED:file-registry -->
