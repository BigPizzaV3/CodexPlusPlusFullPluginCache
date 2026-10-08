---
name: phase-06-storyboard-layout
description: "Phase 6: Storyboard Layout & Staging. Directs visual deck paneling, 180-degree actor blocking, spatial composition geometry, and animatic beat timing grids across 194 standardized craft cards. Use when laying out multi-panel visual decks, planning character blocking, or timing an animatic before image generation. Trigger on: storyboard, storyboard deck, panel layout, actor blocking, animatic grid, 180 degree rule, ستوري بورد، تخطيط مشاهد، بانيل، توزيع ممثلين، انيماتيك، رسم المشاهد."
---

# Phase 6: Storyboard Layout & Visual Staging

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

Welcome to **Phase 6: Storyboard Layout & Visual Staging**, backed by **194 craft cards**.

Phase 6 visually stages each shot onto storyboard panels. Operating under the **Inheritance Rule**, it takes the locked shot scale and camera angle from Phase 3 and applies spatial composition, rule of thirds, and actor blocking.


<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The contract for this phase](#the-contract-for-this-phase)
- [Before the first prompt](#before-the-first-prompt)
- [Master Documentation](#master-documentation)
- [Primary Craft Bibles (Owned by Phase 6)](#primary-craft-bibles-owned-by-phase-6)
- [Inter-Phase Cross-Links](#inter-phase-cross-links)
- [Files in this phase](#files-in-this-phase)

<!-- /GENERATED:toc -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `shot_table`, `size_angle`, `timing_src`, `render_mode`, `looks` |
| **One-of read groups** | `timing_map` or `measured_duration` or `durations` |
| **Optional reads** | `branch_map` |
| **External inputs allowed** | `branch_map`, `shot_table`, `size_angle`, `timing_src`, `durations` |
| **Writes** | `panels`, `blocking`, `composition` |
| **May not re-decide** | `branch_map`, `shot_table`, `size_angle`, `render_mode`, `looks`, `durations` |
| **Execution gate** | — |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `narrated_documentary` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `music_video` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `commercial` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `commercial_narrated` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `storyboard_only` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `interactive_branching_silent` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `interactive_branching_audio` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |
| `data_led_built` | `phase-03-shooting-script` | `phase-07-image-prompt-engineering` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

---

## Before the first prompt

This phase needs the engine record from [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) — the native tile, the
clip ceiling, whether an end frame is accepted. Fill it at the start of the project from the brief's engine, or, where the brief names none,
from the engine that best fits the piece, chosen after a search of its current documentation and
recorded under `decisions`. A cell still unconfirmed is written in full anyway and carries
`pending_engine_check` as a note in the handoff, never a stop. **A limit is a reason to change the engine, not the shot.**

---

## Master Documentation
- **[HOW-PHASE-6-WORKS.md](./HOW-PHASE-6-WORKS.md)**: The Inheritance Rule, Staging Workflow, and Panel Grids.
- **[INDEX.md](./INDEX.md)**: Categorized catalog of all 194 craft cards.
- **[LOOKUP.md](./LOOKUP.md)**: Master alphabetical ID table.

## Primary Craft Bibles (Owned by Phase 6)
- **[composition.md](./composition.md)**: 69 cards on visual geometry, leading lines, rule of thirds.
- **[blocking-staging.md](./blocking-staging.md)**: 64 cards on actor blocking, 180-degree rule, eyelines.
- **[mesopotamian-heritage-staging.md](./mesopotamian-heritage-staging.md)**: 22 cards on historical architectural staging.
- **[storyboard-panel-architecture.md](./storyboard-panel-architecture.md)**: 21 cards on deck layouts.
- **[animatic-beat-timing-grid.md](./animatic-beat-timing-grid.md)**: 18 cards on beat alignment.

## Inter-Phase Cross-Links
- **[Phase 3 Camera Setup Bibles](../phase-03-shooting-script/PHASE.md)**: Source of locked shot sizes ([shot-sizes.md](../phase-03-shooting-script/shot-sizes.md)) and camera angles ([angle-height.md](../phase-03-shooting-script/angle-height.md)).
- **[Phase 7 Image Prompt Engineering](../phase-07-image-prompt-engineering/PHASE.md)**: Receives approved panel staging to synthesize keyframes.

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**8 craft files, 194 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md). Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`composition.md`](composition.md) | **Composition** — Visual geometry, rule of thirds, leading lines, golden ratio, symmetry, frame within a frame. <br>*Cards scoped to: any format* | 69 |
| [`blocking-staging.md`](blocking-staging.md) | **Blocking and Staging** — Actor placement, 180° rule, eyeline matching, triangle blocking, power dynamics. <br>*Cards scoped to: any format* | 64 |
| [`mesopotamian-heritage-staging.md`](mesopotamian-heritage-staging.md) | **Mesopotamian & Near Eastern Heritage Staging** — Historical architectural staging, royal throne elevation, temple courtyards. <br>*Cards scoped to: mostly Historical Epic, Heritage Film, Historical Documentary, Heritage Documentary, among 36 formats* | 22 |
| [`storyboard-panel-architecture.md`](storyboard-panel-architecture.md) | **Storyboard Panel Architecture & Presentation Decks** — Multi-panel grid layout, 3x3 contact sheets, panel reading flow. <br>*Cards scoped to: any format* | 21 |
| [`animatic-beat-timing-grid.md`](animatic-beat-timing-grid.md) | **Animatic & Beat-Timing Synchronization Grid** — Temporal beat alignment with Phase 4 narration and Phase 5 music stems. <br>*Cards scoped to: any format* | 18 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`handoff-to-stills.md`](handoff-to-stills.md) | Handoff Protocol: Storyboard Layout to Image Keyframes (Phase 6 → Phase 7) — This document governs the operational handoff from Phase 6 (Storyboard Layout & Blocking) to Phase 7 (I |
| [`storyboard-deck-template.md`](storyboard-deck-template.md) | Storyboard deck template — The poster: one image showing every panel in a grid, with cinematic stills, captions, camera |
| [`vlb-composition.md`](vlb-composition.md) | Composition — From the Visual Language Bible. Start from `../phase-03-shooting-script/vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands yo |

<!-- /GENERATED:file-registry -->
