# SHELVES — what a shelf is, what is not one, and the inventory

A **shelf** is a decision you must make from many candidates. The candidates are the cards, and this
file says which families are shelves, which are not, and why. **The inventory at the foot is
generated from the card ids** — nothing here is counted by hand.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. The counting rule](#1-the-counting-rule)
- [2. The exclusion rule](#2-the-exclusion-rule)
- [2b. Before any selector: is this family one decision, or two?](#2b-before-any-selector-is-this-family-one-decision-or-two)
- [3. What the inventory and selectors enforce](#3-what-the-inventory-and-selectors-enforce)
- [4. The inventory](#4-the-inventory)

<!-- /GENERATED:toc -->

## 1. The counting rule

**One rule, written here and implemented in the source package's build tools. The number is whatever the rule
produces.**

> **A shelf is a card-id family whose cards are alternatives to one another at a single moment of the
> work.** Assembled by id prefix wherever the cards live, across files and across phases.

**There is no size threshold, and the absence of one is deliberate.** The shelf count was stated
three different ways in one discussion — *about 15*, *about 45*, *78* — and all three were honest,
because the threshold moved each time. A family of four alternatives is as much a shelf as a family
of two hundred; it simply needs a smaller selector. Any cutoff would be a number somebody chose, and
a number somebody chose is the `706 → 838` defect looking for a new home.

**A family is assembled by id, never by folder.** *Which cut* has its candidates in four files —
`cuts-in-scene.md`, `shot-transitions.md`, `vlb-cuts-in-scene.md`, `vlb-scene-transitions.md` — and
an agent sent to the first of them takes what it finds and leaves believing it saw the shelf. Eight
families live across two phases at once. **A family split across four files takes one selector, not
four.**

## 2. The exclusion rule

Three kinds of family are **not** shelves. The test is not size and not usefulness — it is whether
the cards are *alternatives*:

| Kind | The test | Why a selector there is noise |
| :--- | :--- | :--- |
| **Reference** | You look a fact up in it | The canon does not offer you a choice between two Babylons. You need the one that is true |
| **Rules and procedure** | You obey them, in order | A failure-mode list, a clearance rule, a continuity check. Choosing one over another is not a thing anyone does |
| **Dated engine settings** | You read them off a record | A parameter is whatever the engine says today. The selector is the record, and it already exists |

**Write the exclusion down rather than re-deriving it**, so the next pass does not re-litigate what
was already settled. The table below is the authority; the generator reads it and everything else
becomes a shelf by default. **A family that is neither listed here nor produced as a shelf is a
finding** — which is how a newly added prefix gets classified deliberately instead of drifting in.

<!-- The table below is hand-written and is the authority. Add a row to exclude a family. -->

| Family | Kind | Why |
| :--- | :--- | :--- |
| `meso` | reference | The Mesopotamia canon — grimoires and clothing. Looked up, never chosen between |
| `vlb` | reference | The Visual Language Bible bridge: its own format and genre profiles, the only place the package gives a format's ratio and pace or a genre's visual grammar. Its copies of other shelves' cards were retired to pointers on 2026-09-23 |
| `prompt` | rules | The image guide's own laws |
| `control` | rules | Continuity checks, run in order |
| `fail` | rules | Named failure modes |
| `rescue` | rules | Image repair procedures |
| `repair` | rules | Restoration procedures |
| `rights` | rules | Optional rights craft, for when a brief itself raises rights; never a step |
| `access` | rules | Accessibility rules |
| `notes` | rules | The notes round |
| `safety` | rules | Tier 0: a deliberate strobe or rapid flash sequence only |
| `still` | rules | The still design record |
| `record` | rules | The recording record |
| `act` | rules | Action-line rules |
| `nar` | rules | Narration rules |
| `ident` | rules | Identity locks, applied rather than chosen |
| `sheet` | rules | Sheet layouts |
| `world` | rules | Secondary-world rules |
| `sfl` | rules | Short-form line rules |
| `audio_exec` | rules | Recording execution |
| `sound_realize` | rules | Sound realisation |
| `song_handoff` | rules | The stems and timing handoff |
| `anim_time` | rules | Frame arithmetic |
| `print` | rules | Print delivery specifications |
| `dataviz` | rules | Carries its own selector already — `dataviz.chart_from_the_question` |
| `elevenlabs` | engine | Dated engine settings |
| `suno` | engine | Dated engine settings |
| `lyria` | engine | Dated engine settings |
| `cond` | engine | Conditioning modalities |
| `pacing` | engine | Owned rates, read rather than chosen |
| `pronounce` | rules | Pre-flight passes over the audio column, and name keys looked up per word. Applied to every script, not chosen between. Its one real choice - a casting pair - is routed from the `voice.` selector |
| `sit.propp_` | rules | The Propp functions: read in order, not chosen between. The first sub-prefix row - `sit.` stays a shelf, and these cards come off it. Not one `sit.` condition crosses into Propp and no Propp card names anything outside it; the file itself says *use them as a checklist, not a template* |

## 2b. Before any selector: is this family one decision, or two?

**`scene.` taught this and it is now the first question asked of every shelf.** Its cards, across four
files in two phases, looked like the worst scatter in the package. It was not scatter: **the Phase 2
cards build a scene and the Phase 3 cards join two scenes together**, and those are different
decisions made at different moments by different phases. The file
split was not an accident of filing, it was the two decisions showing through.

**So the test is not "how many files is it in" but "how many questions does it answer".** A family in
four files answering one question is one shelf. A family in one file answering two is two shelves, and
the first thing anything built on top of it has to ask is *which of the two are you making*.

*(This paragraph used to point at a selector card, scene.choose_the_move, as the worked example. That card and its two
siblings were removed on 2026-09-20: they sorted their shelves by `Effect on the audience`, which
measurement showed to be the least discriminating field on a card, and they were designed while the
package believed the visual shelves held three card-to-card pairs in six hundred cards. The real
figure on those shelves is 383. The counting rule below is unaffected — it never depended on them.)*

**`time.` is the same shape and it is confirmed, not suspected.** Its 114 cards split 65 in Phase 1
and 49 in Phase 8, and the two halves share nothing but the word:

```
Phase 1   linear_spine · in_medias_res · nonlinear_assembly · reverse_chronology · frame_narrative
          · dual_timeline · flashback_trigger · unreliable_memory      when does this happen in the story
Phase 8   real_time_playback · slow_motion · overcrank · post_retime · timelapse · hyperlapse
          · speed_ramp_up · ramp_to_beat                              how fast does this clip run
```

**Two decisions, made in two phases, months apart.** A single selector over them would be asking one
question of two unrelated shelves. `time.` takes the `scene.` treatment: one selector whose first fork
is which of the two you are making.

**The rest were swept with the same question and they are settled.**

**`voice.` is two decisions, like `time.`** — 73 cards in Phase 2 and 16 in Phase 4, and the halves do
not answer the same thing: `voice.advertising_register`, `voice.free_indirect_style` and
`voice.dialect_by_syntax` decide **what register this is written in**, while
`voice.cast_authoritative_historian` and `voice.cast_ancient_ruler` decide **who performs it and
how**. One is settled while writing, the other at casting, and a single map over them would ask one
question of two unrelated shelves.

**`doc.`, `promo.`, `vertical.`, `mv.` and `kids.` are one decision each.** Their split has a tell
that the other two do not: **the same filename appears in both phases** — `documentary.md` in Phase 3
and Phase 7, `vertical-short-form.md` in both, and so on. That is one subject split by
**deliverable**, moving picture in one phase and still in the other, not by decision. A documentary
move is the same move whether it ends in a clip or a frame, and one selector governs it.

**The tell is worth keeping:** *two files with the same name in two phases* usually means one
decision and two outputs; *two differently named files in two phases* is where a second decision
hides. **Ask before writing the selector, not after**, because a selector built on the assumption of
one decision cannot be repaired by adding a question later; its whole map is laid out wrong.

**The opposite case: two shelves that are coordinates of one picture.** Two families can describe the
same frame without being alternatives to each other, and then the right move is to take one card
from each, never one instead of the other. Two such boundaries are measured:

- **`size.` and `frame.`** — how much of the subject, and which named setup. Zero pair edges cross
  between them, and that zero is the separation being correct. The one place they genuinely compete
  is the coverage decision, and `frame.coverage_plan` asks it across both.
- **`comp.` and `block.`** — `block.` is where the body is in the space, `comp.` is what the rectangle
  does with it. Nine subjects appear on both, as twins rather than rivals: `comp.triangle` and
  `block.three_actor_triangle`, `comp.grouping` and `block.the_line`, `comp.two_faces_one_away` and
  `block.shoulder_to_shoulder`, `comp.dirty_frame` and `block.body_occlusion_reveal`,
  `comp.depth_layers` and `block.depth_staging`, `comp.shooting_through` and `block.behind_glass`,
  `comp.frame_within_frame` and `block.doorway_threshold`, `comp.vertical_bars` and
  `block.barrier_between`, `comp.empty_chair` and `block.empty_half_bed`. Stage it with the `block.`
  card, then frame it with the `comp.` card. These are not entries in `COLLISIONS.md`: a collision is
  two cards that cannot both be obeyed, and these can always both be obeyed.

**And two cards on a shelf may not be of it.** Two kinds turned up in the first three selectors, and
each carries its own mark on the card itself:

- **Geometry every answer obeys** — marked with a `**Not a choice:**` line. Three `angle.` cards —
  the 180 line, the 30-degree rule, the eyeline match — are not alternatives to each other or to
  anything. Every shot has them. `light.key` and `light.ratio` stand in the same relation to the
  lighting shelf.
- **A named failure** — marked with the line `**This is a named failure, not a recommendation.**`,
  which is what the package's named failures actually carry, on every shelf that has them. The first
  ones were found on `scene.`; they describe what goes wrong, not what to do. They are reached by the
  **Avoid when** of the card you did choose. A selector that listed them would be offering to fail.

*(This section used to say both kinds carry `**Not a choice:**`. Measured, that phrase marked
geometry and a handful of others, while the named-failure line marked the failures - and the
reachability check had already learned to read both. The documentation now names the mark the cards
carry.)*

## 3. What the inventory and selectors enforce

This file **freezes the candidate sets**: for every decision in the package, which cards belong to
the shelf. Every shelf in the generated inventory below has a selector at its head, which asks the
decision questions, eliminates on the cards' `Avoid when:` fields, and reaches every card that
remains a genuine choice; geometry, named failures, additive parts and reference records are
classified on the cards (`**Not a choice:**`) rather than quietly left out.

**When a selector returns nothing usable.** Where the intersection is empty, or every card in it
fails its own `Avoid when:`, relax the last axis and take the intersection of the others, and record
that under `decisions`. A selector that says what its own empty cell means (an empty cell that is a
finding, or a plain card that is the answer) keeps its own reading.

Two checks guard that claim. `card-pair-unaudited` requires every card family to appear in the pair
audit, and `shelf-card-unreachable` fails when a selector cannot reach a card on its own shelf and the
card carries no non-choice classification. `PAIR-AUDIT.md` is the generated current accounting.

## 4. The inventory

<!-- GENERATED:shelf-inventory — do not edit by hand. Generated in the source package -->

**77 shelves, 4,175 cards.** 31 families and 555 cards are excluded by §2. `sit.propp_` takes 32 cards off its shelf - a sub-prefix row, for a procedure filed inside a family of alternatives. Every number in this block is produced by the rule in §1 and none of it is typed.

| Shelf | Cards | Files | Phase |
| :--- | ---: | ---: | :--- |
| `scene.` | 219 | 4 | P2 P3 |
| `doc.` | 138 | 2 | P3 P7 |
| `char.` | 129 | 4 | P1 |
| `move.` | 114 | 1 | P8 |
| `time.` | 114 | 3 | P1 P8 |
| `struct.` | 113 | 2 | P1 |
| `tens.` | 105 | 5 | P1 |
| `sig.` | 97 | 1 | P8 |
| `voice.` | 92 | 3 | P2 P4 |
| `light.` | 90 | 1 | P7 |
| `sf.` | 87 | 1 | P1 |
| `info.` | 84 | 4 | P1 |
| `rhythm.` | 83 | 3 | P2 |
| `lyric.` | 77 | 4 | P5 |
| `expo.` | 75 | 4 | P1 |
| `inter.` | 74 | 1 | P1 |
| `emo.` | 73 | 3 | P2 |
| `promo.` | 72 | 2 | P3 P7 |
| `beat.` | 71 | 2 | P1 |
| `comedy.` | 71 | 2 | P2 |
| `dial.` | 71 | 2 | P2 |
| `vertical.` | 71 | 2 | P3 P7 |
| `comp.` | 69 | 1 | P6 |
| `cut.` | 69 | 1 | P3 |
| `open.` | 68 | 3 | P1 |
| `trans.` | 67 | 1 | P3 |
| `sit.` | 66 | 1 | P1 |
| `end.` | 65 | 3 | P1 |
| `block.` | 64 | 1 | P6 |
| `look.` | 64 | 1 | P7 |
| `frame.` | 61 | 1 | P3 |
| `rel.` | 61 | 2 | P1 |
| `seq.` | 61 | 2 | P1 |
| `anime.` | 59 | 1 | P7 |
| `angle.` | 58 | 1 | P3 |
| `anta.` | 58 | 2 | P1 |
| `color.` | 57 | 1 | P7 |
| `pov.` | 56 | 2 | P2 |
| `sub.` | 56 | 2 | P2 |
| `theme.` | 56 | 2 | P1 |
| `arc.` | 53 | 2 | P1 |
| `lens.` | 53 | 1 | P7 |
| `rig.` | 52 | 1 | P8 |
| `ai.` | 47 | 1 | P8 |
| `mv.` | 45 | 2 | P3 P7 |
| `kids.` | 43 | 2 | P3 P7 |
| `cg.` | 32 | 1 | P7 |
| `genre.` | 27 | 1 | P5 |
| `assyrian_exp.` | 26 | 1 | P5 |
| `foley.` | 26 | 1 | P4 |
| `harmony.` | 26 | 1 | P5 |
| `hook_psych.` | 26 | 1 | P5 |
| `rhyme.` | 26 | 1 | P5 |
| `sound.` | 26 | 1 | P3 |
| `sync.` | 26 | 1 | P5 |
| `maqam.` | 25 | 1 | P5 |
| `soundscape.` | 24 | 1 | P4 |
| `mix.` | 23 | 1 | P4 |
| `vocal_subtext.` | 23 | 1 | P4 |
| `assyrian.` | 22 | 1 | P5 |
| `meso_stage.` | 22 | 1 | P6 |
| `board_arch.` | 21 | 1 | P6 |
| `dubbing.` | 21 | 1 | P4 |
| `score.` | 21 | 1 | P4 |
| `size.` | 21 | 1 | P3 |
| `medium.` | 19 | 1 | P7 |
| `restore.` | 19 | 1 | P4 |
| `photo.` | 18 | 1 | P7 |
| `material.` | 16 | 1 | P7 |
| `pose.` | 16 | 1 | P7 |
| `ref.` | 16 | 1 | P7 |
| `staging.` | 16 | 1 | P7 |
| `textimg.` | 15 | 1 | P7 |
| `kf.` | 14 | 1 | P7 |
| `retouch.` | 13 | 1 | P7 |
| `sensory_sonic.` | 13 | 1 | P4 |
| `lyr.` | 8 | 1 | P5 |

**28 shelves are split across more than one file** and **8 span more than one phase.** Each of those takes one selector, not one per file.

<!-- /GENERATED:shelf-inventory -->
