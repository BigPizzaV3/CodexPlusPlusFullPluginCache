# Technical Shot Planning & Directorial Breakdown

The work plan for shots, established after the screenplay and before any visual generation begins. It decides what each shot accomplishes, its visual scale, angle, camera movement motivation, and duration. It does not write image or video prompts; those belong to Phase 7 and Phase 8, which ingest this plan.

> [!IMPORTANT]
> **Master Deliverable Standard**:
> The authoritative, required production deliverable of Phase 3 is the **[Technical Shooting Script Table](./HOW-PHASE-3-WORKS.md#4-the-technical-shooting-script-table-format)** (specifying Shot ID, Script/Audio Ref, Mode, Scale & Angle, Camera Movement & Motivation, Time In / Time Out, Duration, Lyric / Audio Cue, and Transition).
> The sixteen technical fields below serve as the underlying cinematography design checklist when expanding complex setups or verifying shot completeness.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Scope and Tiered Requirements](#1-scope-and-tiered-requirements)
- [2. Scene and Shot Unit Map](#2-scene-and-shot-unit-map)
- [3. The 16 Cinematography Design Fields](#3-the-16-cinematography-design-fields)
- [4. Coverage and Scene Grammar](#4-coverage-and-scene-grammar)
- [5. Continuity, Motif and Variation](#5-continuity-motif-and-variation)
- [6. Route-Native Design](#6-route-native-design)

<!-- /GENERATED:toc -->

## 1. Scope and Tiered Requirements

An industry shot list carries eight basic fields: scene, shot, size, angle, movement, lens, action, dialogue. That suffices for a live-action human crew where a director makes on-set adjustments. In generative pipelines, AI models render what is specified and hallucinate what is omitted. The sixteen fields below ensure complete creative sovereignty.

**Tier 1: Mandatory on Every Shot (6 Core Fields)**
- Shot ID and narrative function
- Scale and framing (`shot-sizes.md`)
- Angle and elevation (`angle-height.md`)
- Focal attention and visual target (fine panel composition is finalized in Phase 6)
- Duration and internal rhythm
- Camera movement and physical motivation

*A short-form 15-to-60-second video completes these six fields inside the Shooting Script Table.*

**How many shots?** This phase owns the numbered table and this is its first question, so the answer
belongs here rather than downstream. The count comes from
`board_arch.panel_count_runtime_formula` in
[`../phase-06-storyboard-layout/storyboard-panel-architecture.md`](../phase-06-storyboard-layout/storyboard-panel-architecture.md),
and it is the same arithmetic whether you are counting shots or panels:

| Runtime | Shots |
|---|---|
| 15 s commercial | 6 to 9 |
| 30 s commercial | 9 to 14 |
| 60 s reel | 18 to 24 |
| 60 s to 5 min | one per 2.5 to 4 s, unless a genre ASL applies (below) |
| feature scene | one per dramatic beat |

**A genre's own average shot length outranks the table.** Where the piece takes a genre card in
[`vlb-genres.md`](vlb-genres.md) — `vlb.genre.drama`, for one — divide the runtime by that card's ASL;
the table is the fallback when no genre ASL applies.

**When two ASL cards disagree** — a genre card and a format card (`vlb.genre.drama` against
`vlb.format.short_film`), or two format cards (`vlb.format.commercial_ad` against
`vlb.format.animation`) — the genre card wins, because it describes what the viewer is watching, and
the format card's band is the reference it bends. Where no genre card applies, take the format card
for how the piece is delivered. On a narrated piece the narration bound below comes first either way.
All of these figures are references, never limits: a brief that names its own length or shot count
is built as asked. Record the band chosen under `decisions` and continue.

Two things bend it. **Children's content has a floor**: `kids.no_fast_cuts` holds the shortest shot at
1.5 seconds, which caps the count regardless of the row. And **a narrated piece is bound by the
narration** — a shot cannot be shorter than the line it carries, so on the narrated route the count
falls out of the script before it falls out of the table.

**And where do the timecodes come from?** The second question this phase is asked at the same moment,
because the table has a Time In / Time Out column and it has to be filled with something. The answer
depends on the route, and on **every** route the source of truth runs *after* this phase — so the
first pass is always provisional and should be marked as such.

| Route | Where Time In / Time Out comes from | Before that source exists |
|---|---|---|
| **Music** | The locked song, measured — the Phase 5 timing map | The BPM and metre grid |
| **Narrated** | The rendered narration, measured — the Phase 4 audio file | `words ÷ rate`, with the rate taken from the Phase 4 card for the register, never restated here |
| **No audio at all** | Nothing upstream; the durations are the designed durations | — quantise them to whole frames at the delivery frame rate |

Two rules govern all three rows. **An estimate is never the answer**: a word count divided by a rate
is how you decide roughly how long a shot should be, and the rendered audio file is how you learn
how long it is. Re-cut the cells against the measured file the moment it exists, and build the
picture to what was measured rather than the reverse. And **mark a provisional row as provisional** —
a timecode nobody flagged as an estimate is indistinguishable from a measured one, and that is how a
shot list survives into an edit it does not fit.

The long form of both answers, with the table format they land in, is
[§4 of HOW-PHASE-3-WORKS.md](./HOW-PHASE-3-WORKS.md#4-the-technical-shooting-script-table-format).

**Tier 2: Multi-Shot Sequences & Continuity (5 Extended Fields)**
- Lens optics and focal depth — **noted here, decided in Phase 7** ([`../phase-07-image-prompt-engineering/lens-focus-depth.md`](../phase-07-image-prompt-engineering/lens-focus-depth.md)). Write the intent if the shot has one ("long lens, subject separated"); the focal length and the glass are Phase 7's to set.
- Blocking vectors and subject trajectories
- Lead or trail camera relationship
- Eyeline axis and spatial 180° screen direction
- Edit handles and transition intent (`scene-transitions.md`, `shot-transitions.md`)

**Tier 3: Recurring Productions & Complex Narratives (5 Advanced Fields)**
- Protected invariants vs flexible choices
- Source technique IDs
- Failure, fallback, and rescue mitigation
- Sound dependency and audio transient sync (`sound-as-visual.md`)
- Camera support, tracking path, and kinetic momentum

---

## 2. Scene and Shot Unit Map

For every narrative unit, record:
- Stable scene ID and shot ID
- Upstream script line or song section reference
- Narrative dramatic event and audience psychological effect
- Visual start state, internal turn, and end state
- Downstream dependencies

---

## 3. The 16 Cinematography Design Fields

When conducting a deep technical breakdown for a complex shot, document:

1. **Shot ID and function**: Unique identifier (`SH-001`) and narrative purpose.
2. **Scale and framing**: Standardized scale (`size.mcu`, `size.ws`, etc.).
3. **Angle, height, and orientation**: Elevation and tilt (`angle.low`, `angle.high`, and for a canted frame one of `angle.subtle_dutch`, `angle.hard_dutch`, `angle.dutch_settle` or `angle.dutch_roll` — there is no bare angle.dutch id, and the four differ in how far the horizon goes over and whether it comes back).
4. **Lens optics and depth**: Equivalent focal length and aperture depth of field.
5. **Focal attention and visual priority**: Subject hierarchy and eye trace (panel composition refined in Phase 6).
6. **Blocking, performance, and vectors**: Subject motion trajectories across frame.
7. **Camera placement, support, and path**: Tripod, dolly, gimbal, Steadicam, crane, or handheld.
8. **Tracking relation**: Lead, trail, or lateral profile pacing.
9. **Duration and speed**: Exact runtime in seconds and velocity curve.
10. **Reveal and occlusion**: What information is withheld and when it becomes visible.
11. **Eyeline and action axis**: 180-degree line preservation and gaze direction.
12. **Audio-visual dependency**: Music beat, lyric line, or SFX impact tied to this frame.
13. **Transition in / out**: Cut type, match cut, or optical transition.
14. **Protected invariants**: Elements that must never drift across the shots (lighting direction, screen direction, a prop's place in the set). Wardrobe and faces are held in the image and character-sheet prompts, not here.
15. **Source craft IDs**: Referenced technique IDs from Phase 3 modules.
16. **Failure fallback**: Backup framing if dynamic motion introduces generative artifacts.

---

## 4. Coverage and Scene Grammar

- **Irreducible event**: The single core action that must be legibly captured.
- **Coverage logic**: Master shot, shot-reverse-shot, inserts, or continuous oner.
- **Distinct function of each view**: Why each cut exists rather than holding the previous angle.
- **Oner logic & safety recovery**: Fallback cutaways if long continuous generations drift.
- **Deliberately omitted coverage**: Angles rejected to preserve narrative economy.

---

## 5. Continuity, Motif and Variation

- **Visual baseline**: Established camera mode (M1–M6) and visual tone.
- **Motif progression**: Recurring shot sizes or angles that evolve with the protagonist's arc.
- **Stable vs variable properties**: What changes (lighting intensity, framing tightness) vs what holds.
- **Axis & screen direction**: Maintaining left-to-right momentum across cuts.
- **Permitted disorientation**: Controlled breaks in continuity for dramatic shock or nightmare logic.

---

## 6. Route-Native Design

- **Active route profile**: Cinematic Film, Express Short, Music Video, Commercial Ad, or Heritage Documentary.
- **Platform-native conventions**: Adapting grammar for 9:16 mobile feeds vs 2.39:1 widescreen cinema.
- **Engine limits, recorded — never designed down to**: Record the engine's limits against each complex camera move; where one cannot be held, change the engine or split the move across keyframes, and never reduce the shot ([`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §4).
