---
name: phase-02-screenplay-dialogue
description: "Phase 2: Screenplay & Dialogue Craft. Directs dramatic scene construction, subtext, character dialogue idioms, pacing, and comedy escalation across 585 core craft cards (781 total headings). Use when turning an approved story outline into a production-ready screenplay, formatting dialogue, writing banter, or diagnosing flat dialogue. Trigger on: write screenplay, script, dialogue, scene writing, subtext, سيناريو، كتابة حوار، نص فيلم، مشاهد، كلام شخصيات، مشهد درامي."
---

# Phase 02: Screenplay, Dialogue & Narration Engine

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Overview](#overview)
- [Inputs](#inputs)
- [Routing Gate: Dramatic vs Music Bypass](#routing-gate-dramatic-vs-music-bypass)
- [Table Formats & Standards](#table-formats-standards)
- [Core Script Laws](#core-script-laws)
- [Workflow Steps](#workflow-steps)
- [Reference Architecture (Progressive Disclosure)](#reference-architecture-progressive-disclosure)
- [Files in this phase](#files-in-this-phase)
- [The contract for this phase](#the-contract-for-this-phase)

<!-- /GENERATED:toc -->

## Overview
Phase 02 translates the narrative beats of the Story Foundation Brief into a disciplined, line-by-line screenplay or voiceover script. It enforces strict synchronization between visual events and acoustic lines, ensures observable actions without premature camera directing, and provides a direct bypass for music-only projects.

## Inputs
- `Story Foundation Brief` from Phase 01.
- Locked audio/music stem (if applicable).

## Routing Gate: Dramatic vs Music Bypass
- **If Dramatic Reel / Documentary / Short Film:** Proceed through standard screenplay drafting.
- **If Song / Audio-Only Music Project:** **BYPASS Phase 02 entirely.** Phase 2 is not on the song-led routes (`music_video`, `score_existing_film`); the route profile in `PROJECT-STATE.md` names the next phase. A sign, caption or end card the brief names on a song-led route does not bring Phase 2 back: its words come from the brief or the lyric and go straight to [`in-frame-text.md`](../phase-07-image-prompt-engineering/in-frame-text.md) (root `SKILL.md` §1, question 5).

## Table Formats & Standards

### Pipeline A: Standard Screenplay (Dialogue / Narration)
Uses the strict **Two-Column Table**. Every line must have both columns filled.

| Visual, what is seen | Audio, what is heard |
|---|---|
| A sand-covered hand brushes silt off a blackened limestone block. | **NARRATOR (V.O.):**<br>"This wall stood thirty feet high before the river broke it." |
| Two soldiers stare silently through the breach at dawn. | *[Deliberate silence: desert wind and distant river rush]* |

### Pipeline B: Music & Locked Audio (Three-Column Table)
When locked audio or a Suno track is present, activate the **Third Column (Time)** measured from the file:

| Time | Visual, what is seen | Audio / Lyrics, what is heard |
|---|---|---|
| `0:00 - 0:04` | Sun rises over the Adad gate; stone lions cast long shadows. | *[Musical intro: acoustic oud arpeggio with subtle drone]* |
| `0:04 - 0:12` | Children race along the palace terrace carrying clay figurines. | **VOCALS:**<br>"Under the shadow of the lion's wing..." |

## Core Script Laws
1. **Observable Only (`act.observable_only`):** Action lines describe only what a camera could record. No unfilmable internal feelings or thoughts.
2. **No Camera in Script (`act.no_camera_in_script`):** Visual column carries dramatic intent; it never dictates camera framing, lenses, or angles.
3. **No Say Cow, See Cow (`nar.say_cow`):** Narration must never state what the visual is already displaying.
4. **Deliberate Silence Written:** Acoustic pauses must be explicitly written (*[Deliberate silence]*).
5. **Speech Cadence:** no rate is written here. Every speaking rate is owned by one pacing card per register in [`../phase-04-audio-narration/pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md) — `pacing.wpm_dramatic_dialogue` for scene dialogue, `pacing.wpm_documentary`, `pacing.wpm_vertical_heritage`, `pacing.wpm_social_reels` and the rest, with `pacing.wpm_arabic` for Arabic word counts; the full list is the generated table in [`HOW-PHASE-2-WORKS.md`](HOW-PHASE-2-WORKS.md) §2. Where no card holds a band for the language and register, take the nearest figure and record the choice. Every one of them is a planning estimate; the duration comes from the rendered file, measured.

## Workflow Steps
1. **Intake Validation:** Read `Story Foundation Brief` from Phase 01. Check project route (Screenplay vs Music Bypass).
2. **Beat-to-Scene Mapping:** Convert each narrative beat into one or more sequential script units.
3. **Drafting the Master Table:** Populate the 2-column or 3-column table line by line.
4. **Dialogue & Voice Refinement:** Consult craft cards for subtext, status shifts, rhythm, and cadence.
5. **Cut Test:** Strip redundant words, throat-clearing, and non-essential syllables.
6. **Deliverable Handoff:** Output the finalized `Screenplay & Dialogue Script` to the next stage in the generated route table below. The table, from `PROJECT-STATE.md`, is the only place that names it.

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `phase-01-story-generation` | `phase-04-audio-narration` |
| `narrated_documentary` | `phase-01-story-generation` | `phase-04-audio-narration` |
| `commercial` | `phase-01-story-generation` | `phase-03-shooting-script` |
| `commercial_narrated` | `phase-01-story-generation` | `phase-04-audio-narration` |
| `storyboard_only` | `phase-01-story-generation` | `phase-03-shooting-script` |
| `audio_only` | `phase-01-story-generation` | `phase-04-audio-narration` |
| `audio_with_cover` | `phase-01-story-generation` | `phase-04-audio-narration` |
| `interactive_branching_silent` | `phase-01-story-generation` | `phase-03-shooting-script` |
| `interactive_branching_audio` | `phase-01-story-generation` | `phase-04-audio-narration` |
| `data_led_built` | `phase-01-story-generation` | `phase-04-audio-narration` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

## Reference Architecture (Progressive Disclosure)
- Master Index: [`INDEX.md`](INDEX.md)
- Card Search Directory: [`LOOKUP.md`](LOOKUP.md) (585 cards)
- Detailed Specification: [`HOW-PHASE-2-WORKS.md`](HOW-PHASE-2-WORKS.md)
- Dialogue Craft: [`cat-dial.md`](cat-dial.md), [`cat-dial-2.md`](cat-dial-2.md)
- Scene Construction: [`cat-scene.md`](cat-scene.md), [`scenes.md`](scenes.md)
- Script Craft: [`script-craft/narration-craft.md`](script-craft/narration-craft.md), [`script-craft/action-lines-craft.md`](script-craft/action-lines-craft.md)

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**33 craft files, 585 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md), with 8 per-family shards beside it, generated from the same source. Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`cat-dial.md`](cat-dial.md) | **Dialogue Technique** — Dialogue basics: subtext vs text, dialogue compression, character idiom, and banter <br>*Cards scoped to: any format* | 31 |
| [`cat-dial-2.md`](cat-dial-2.md) | **Dialogue Technique — Part 2** — Advanced dialogue: deflection, weaponized subtext, interrogation, and strategic silence <br>*Cards scoped to: any format* | 40 |
| [`cat-scene.md`](cat-scene.md) | **Scene Construction and the Value Turn** — Core scene construction: scene question, arrival on defense, departure on change <br>*Cards scoped to: any format* | 31 |
| [`cat-scene-2.md`](cat-scene-2.md) | **Scene Construction — Part 2** — Scene escalation: micro-turns, shifting power leverage, and reverse scene climaxes <br>*Cards scoped to: any format* | 40 |
| [`cat-scene-3.md`](cat-scene-3.md) | **Scene Construction — Part 3** — Contributor and real-speech scenes: renewed consent, approval conversations, failed interviews, reenactment, negotiation, apology, and responsibility handoff <br>*Cards scoped to: mostly Documentary, One-Hour Drama, Stage Play, Feature Film, among 24 formats* | 14 |
| [`script-craft/narration-craft.md`](script-craft/narration-craft.md) | **Narration and Voiceover** — Voiceover and narration craft: documentary VO, ironic counterpoint, and memory echo <br>*Cards scoped to: mostly Documentary Feature, Drama Series, Feature Film, Heritage / Historical Documentary, among 5 formats* | 9 |
| [`script-craft/action-lines-craft.md`](script-craft/action-lines-craft.md) | **Action Lines** — Screenplay action lines: lean descriptions, visual active verbs, and whitespace control <br>*Cards scoped to: mostly Documentary Feature, Drama Series, Feature Film, Heritage / Historical Documentary, among 5 formats* | 4 |
| [`cat-comedy.md`](cat-comedy.md) | **Comedy, Gag Architecture and Escalation** — Comic fundamentals: joke units, status drop, incongruity, exaggeration, and comic timing <br>*Cards scoped to: mostly sitcom, sketch, short-form video, prose, among 38 formats* | 32 |
| [`cat-comedy-2.md`](cat-comedy-2.md) | **Comedy — Part 2** — Comedy escalation: comic engines, the rule of three, callback architecture, and farce <br>*Cards scoped to: any format* | 39 |
| [`cat-emo.md`](cat-emo.md) | **Emotion, Grief, Love and Catharsis** — Emotional expression: visceral sensations, vulnerability, emotional truth, and release <br>*Cards scoped to: any format* | 27 |
| [`cat-emo-2.md`](cat-emo-2.md) | **Emotion — Part 2** — Complex emotion: conflicting feelings, delayed grief, survivor guilt, and quiet devastation <br>*Cards scoped to: any format* | 34 |
| [`cat-emo-3.md`](cat-emo-3.md) | **Emotion — Part 3** — Euphoria, bittersweet joy, transcendent awe, and quiet resolution emotions <br>*Cards scoped to: mostly Essay, Memoir, Feature Film, Monologue, among 36 formats* | 12 |
| [`cat-pov.md`](cat-pov.md) | **Point of View and Narrative Distance** — Point of view craft: first/third person distance, psychic proximity, and narrator reliability <br>*Cards scoped to: any format* | 33 |
| [`cat-pov-2.md`](cat-pov-2.md) | **Point of View and Narrative Distance — Part 2** — Complex POV: shifting perspectives, cinematic free indirect discourse, and objective camera <br>*Cards scoped to: mostly Novel, Short Story, Feature Film, Audio Drama, among 50 formats* | 23 |
| [`cat-rhythm.md`](cat-rhythm.md) | **Sentence Rhythm, Prose Line and Pace** — Prose rhythm: Motivation-Reaction Units (MRU), sentence beats, and paragraph flow <br>*Cards scoped to: any format* | 32 |
| [`cat-rhythm-2.md`](cat-rhythm-2.md) | **Prose Rhythm — Part 2** — Advanced rhythmic pacing: pause punctuation, sentence acceleration, and staccato cadence <br>*Cards scoped to: any format* | 41 |
| [`cat-rhythm-3.md`](cat-rhythm-3.md) | **Prose Rhythm — Part 3** — Lyrical prose, poetic cadence, rhythm under extreme panic, and hypnotic lullabies <br>*Cards scoped to: mostly Advertising, Explainer, Brand Film, Motion Graphics, among 33 formats* | 10 |
| [`cat-sub.md`](cat-sub.md) | **Subtext, Silence and the Unsaid** — Subtext craft: iceberg principle, physical action masking speech, and deliberate omission <br>*Cards scoped to: mostly screenplay, stage play, novel, series drama, among 21 formats* | 32 |
| [`cat-sub-2.md`](cat-sub-2.md) | **Subtext — Part 2** — Societal and polite subtext: dinner party hostility, institutional coded language <br>*Cards scoped to: any format* | 24 |
| [`cat-voice.md`](cat-voice.md) | **Voice, Register and Narrative Authority** — Narrative persona, vocal authority, speaker-audience relationship, and register choices <br>*Cards scoped to: any format* | 32 |
| [`cat-voice-2.md`](cat-voice-2.md) | **Voice and Register — Part 2** — Register families: essayistic voice, borrowed authority, comic delivery, and direct address <br>*Cards scoped to: any format* | 41 |
| [`script-craft/short-form-lines.md`](script-craft/short-form-lines.md) | **Short-Form Scripting Lines** — Short-form scriptwriting: compressed hooks, fast dialogue snaps, and caption economy <br>*Cards scoped to: mostly Documentary Feature, Drama Series, Feature Film, Heritage / Historical Documentary, among 5 formats* | 4 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`scenes-2.md`](scenes-2.md) | Advanced scene types: negotiation scenes, confession scenes, confrontation scenes |
| [`scenes.md`](scenes.md) | Fundamental scene architecture: objectives, obstacles, tactics, and the dramatic value turn |
| [`symptoms-comedy.md`](symptoms-comedy.md) | Comedy diagnostic: jokes falling flat, telegraphing punchlines, and tone clashes |
| [`symptoms-dialogue.md`](symptoms-dialogue.md) | Dialogue diagnostic: characters sounding identical, speechifying, and chit-chat filler |
| [`symptoms-emotion.md`](symptoms-emotion.md) | Emotion diagnostic: melodramatic excess, unearned tears, and emotional numbness |
| [`symptoms-point-of-view.md`](symptoms-point-of-view.md) | POV diagnostic: head-hopping, arbitrary knowledge leaks, and distant narration |
| [`symptoms-prose-and-rhythm.md`](symptoms-prose-and-rhythm.md) | Prose diagnostic: monotone cadence, clunky syntax, and bloated descriptions |
| [`symptoms-scene-level.md`](symptoms-scene-level.md) | Scene-level diagnostic: scenes without a value turn or emotional polarity change |
| [`symptoms-scene-shape.md`](symptoms-scene-shape.md) | Scene shape diagnostic: scenes starting too early, ending too late, or wandering |
| [`symptoms-subtext.md`](symptoms-subtext.md) | Subtext diagnostic: on-the-nose dialogue, excessive exposition, and missing friction |
| [`symptoms-voice.md`](symptoms-voice.md) | Voice diagnostic: inconsistent narrator tone, preachy attitude, and fake authority |

<!-- /GENERATED:file-registry -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `story_brief`, `language`, `audio_profile` |
| **One-of read groups** | — |
| **Optional reads** | `branch_map`, `render_mode`, `rate_wpm`, `dialect` |
| **External inputs allowed** | `story_brief`, `branch_map` |
| **Writes** | `script`, `speaker_map` |
| **May not re-decide** | `story_brief`, `branch_map`, `render_mode`, `looks` |
| **Execution gate** | — |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

---
