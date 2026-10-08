---
name: phase-08-video-prompt-engineering
description: "Phase 8: Video Prompt Engineering & Universal Kinematics. Directs 6-axis camera movements, optical speed ramps, temporal continuity physics, and model-agnostic video prompts across 394 standardized craft cards (414 total headings). Use when animating keyframes into dynamic video clips across any frontier AI video engine. Trigger on: video prompt, AI video, camera motion, 6-axis kinematics, speed ramp, برومت فيديو، حركة كاميرا، تحريك الصورة، فيديو سينمائي، كينماتيكس، توليد فيديو بالذكاء الاصطناعي."
---

# Phase 8: Video Prompt Engineering & Model-Agnostic Kinematics

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

Welcome to **Phase 8: Video Prompt Engineering**, the eighth and final phase of the comprehensive AI Film Production Pipeline.

Phase 8 transforms the frozen photorealistic keyframes generated in Phase 7 into dynamic, physically coherent, and cinematic moving shots. Operating under the **Law of Model-Agnostic Creative Sovereignty**, it direct camera kinematics, temporal motion vectors, speed qualifiers, and physical momentum without constraining decisions to any specific provider.

---


<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The contract for this phase](#the-contract-for-this-phase)
- [Before the first prompt](#before-the-first-prompt)
- [Master Documentation & Directing Manuals](#master-documentation-directing-manuals)
- [Modular Kinematic Bibles (394 Craft Cards)](#modular-kinematic-bibles-394-craft-cards)
- [Inter-Phase Cross-Links](#inter-phase-cross-links)
- [Files in this phase](#files-in-this-phase)

<!-- /GENERATED:toc -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `render_mode`, `looks`, `forbidden_global`, `engine_record`, `keyframes_approved_by` |
| **One-of read groups** | `keyframe_prompts` or `source_stills`; `durations` or `timing_map` or `measured_duration` or `existing_picture_timing` |
| **Optional reads** | `branch_map`, `shot_table`, `timing_src`, `voice_cast`, `frozen_sentence`, `frozen_sentence_status`, `palette`, `motion_brief`, `mode` |
| **External inputs allowed** | `source_stills`, `motion_brief`, `branch_map`, `durations`, `existing_picture_timing`, `render_mode`, `looks`, `forbidden_global` |
| **Writes** | `clip_prompts` |
| **May not re-decide** | `branch_map`, `shot_table`, `durations`, `frozen_sentence`, `palette`, `render_mode`, `looks`, `size_angle` |
| **Execution gate** | `paid_generation_approved_by` |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `narrated_documentary` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `music_video` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `commercial` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `commercial_narrated` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `supplied_stills_video` | `external / intake` | `delivery / edit` |
| `interactive_branching_silent` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `interactive_branching_audio` | `phase-07-image-prompt-engineering` | `delivery / edit` |
| `data_led_built` | `phase-07-image-prompt-engineering` | `delivery / edit` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

---

## Before the first prompt

**First, the keyframe gate.** Read `keyframes_approved_by` in `project.yaml` (`../PROJECT-STATE.md`).
If it is null, stop here and write nothing: say that the keyframe deck is waiting for the owner's
approval, and that the owner records it by writing their name and the date in that field. In
prompts-only mode the owner approves the keyframe *prompt* deck (`<name>, prompts-only, <date>`), and
every clip prompt then carries `pending_keyframe_render` until its still exists. Never
fill it yourself, and never read approval from silence, an Express run or the spend field.

This phase needs the engine record from [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) — the native tile, the
clip ceiling, whether an end frame is accepted. Fill it at the start of the project. If it is not
filled, write the prompt in full anyway and mark the resolution and clip-length cells
`pending_engine_check`. **A limit is a reason to change the engine, not the shot.**

---

## Master Documentation & Directing Manuals
- **[how-to-write-a-video-prompt.md](./how-to-write-a-video-prompt.md)**: Master Video Prompt Engineering Guide (Single authoritative construction standard). Directs kinematics, camera trajectories, and conditioning locks without vendor lock-in.
- **[HOW-PHASE-8-WORKS.md](./HOW-PHASE-8-WORKS.md)**: Master operational manual on 6-axis camera vector coordinates, dual-image start/end frame conditioning, and artifact mitigation.
- **[INDEX.md](./INDEX.md)**: Categorized catalog of all 394 craft cards (414 total headings) across all its modules.
- **[LOOKUP.md](./LOOKUP.md)**: Master alphabetical ID lookup table.

---

## Modular Kinematic Bibles (394 Craft Cards)
1. **[camera-moves.md](./camera-moves.md)** (114 cards): Pan, tilt, track, pedestal, zoom, roll, orbit, arc, push-in, pull-out, and spatial translation vectors.
2. **[signature-moves.md](./signature-moves.md)** (97 cards): Iconic cinematic shots (Vertigo dolly-zoom, bullet time, crash zoom, snorricam, whip pan, dutch tilt track).
3. **[ai-video-directing.md](./ai-video-directing.md)** (47 cards): Keyframe-first workflows, I2V, F2L dual-frame interpolation, character locks, and wardrobe locks.
4. **[rigs-and-platforms.md](./rigs-and-platforms.md)** (52 cards): Technocrane, Steadicam, heavy-lift drones, cable cams, 3-axis gimbals, handheld setups, and vehicle tracking mounts.
5. **[time-and-speed.md](./time-and-speed.md)** (49 cards): High-speed 120fps/240fps slow motion, speed ramping, timelapse, hyperlapse, time freezes, and reverse playback.
6. **[temporal-continuity-checks.md](./temporal-continuity-checks.md)** (19 cards): Motion vector consistency, limb trajectory tracking, lighting continuity, and silhouette preservation.
7. **[../phase-03-shooting-script/sound-as-visual.md](../phase-03-shooting-script/sound-as-visual.md)** (26 cards): Visual rhythm, cut on sonic impact, motion synchrony, and acoustic camera rumble.
8. **[video-failure-modes.md](./video-failure-modes.md)** (8 cards): Temporal morphing, limb duplication, camera jitter/flicker, geometric melting, style bleed, pattern breakdown, impossible pose, and dropped late instructions.

---

## Inter-Phase Cross-Links
- **[Phase 3 Shooting Script](../phase-03-shooting-script/PHASE.md)**: Source of locked shot numbers, shot scales, and camera angles.
- **[Phase 6 Storyboard Layout](../phase-06-storyboard-layout/PHASE.md)**: Source of animatic beat timing grid and actor blocking.
- **[Phase 7 Image Prompt Engineering](../phase-07-image-prompt-engineering/PHASE.md)**: Source of approved Still Keyframes (Start Frame and End Frame) feeding video generation.

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**10 craft files, 394 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md). Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`camera-moves.md`](camera-moves.md) | **Core Camera Moves** — Core Camera Moves & Dynamic Trajectories <br>*Cards scoped to: any format* | 114 |
| [`signature-moves.md`](signature-moves.md) | **Signature and Compound Moves** — Iconic Cinematic & Signature Camera Moves <br>*Cards scoped to: any format* | 97 |
| [`ai-video-directing.md`](ai-video-directing.md) | **AI Video Techniques** — AI Video Directing Techniques & Keyframe Conditioning <br>*Cards scoped to: any format* | 47 |
| [`rigs-and-platforms.md`](rigs-and-platforms.md) | **Rigs and Camera Platforms** — Camera Rigs, Mounts & Mechanical Platforms <br>*Cards scoped to: any format* | 52 |
| [`time-and-speed.md`](time-and-speed.md) | **Time and Speed** — Temporal Speed, Frame Rates & Speed Ramps <br>*Cards scoped to: any format* | 49 |
| [`temporal-continuity-checks.md`](temporal-continuity-checks.md) | **Control and Continuity Checks** — Temporal Continuity & Inter-Frame Physics Checks <br>*Cards scoped to: mostly Trailer / Teaser, AI-Generated Clip, Commercial / TVC, Music Video, among 40 formats* | 19 |
| [`video-failure-modes.md`](video-failure-modes.md) | **Failure Modes and Rescues** — Video Diffusion Failure Modes & Distortion Mitigation <br>*Cards scoped to: any format* | 8 |
| [`the-notes-round.md`](the-notes-round.md) | **What happens after the first delivery.** Reading what a note actually asks for - a note is a symptom stated as a prescription - and triaging notes by which locked layer they reach back into, because the cost of a note is how far upstream it lands, not how big it sounds. <br>*Cards scoped to: mostly Brand Film, Commercial / TVC, Corporate / Training, Documentary Feature, among 10 formats* | 2 |
| [`video-conditioning-modalities.md`](video-conditioning-modalities.md) | **Universal Video Conditioning Modalities** — Universal Video Conditioning Modalities — Department: **Video Prompt Engineering (Phase 8)** <br>*Cards scoped to: mostly Music Video, Action Feature, Action Short, Animation, among 18 formats* | 6 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`how-to-write-a-video-prompt.md`](how-to-write-a-video-prompt.md) | How a video prompt is written — Every rule here is craft: what a generative model does with a prompt, and what it does with a careless one. |

<!-- /GENERATED:file-registry -->
