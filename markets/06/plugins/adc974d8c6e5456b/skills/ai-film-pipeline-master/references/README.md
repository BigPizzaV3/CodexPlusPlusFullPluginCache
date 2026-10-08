# Autonomous AI Video & Film Production Pipeline ("New skill By Gemini")

The most comprehensive, rigorous, and modular end-to-end AI film and video production framework engineered for autonomous AI agents and creative directors.

Operating across **8 sequential production phases**, this skill contains **4,762 standardized craft cards** (and **5,386 total searchable headings**), **100% unique backticked IDs**, zero broken internal links, and strict compliance with the `agy-customizations` agent specification.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The 8-Phase Production Architecture](#the-8-phase-production-architecture)
- [Execution Modes: Express Auto vs. Director Review](#execution-modes-express-auto-vs-director-review)
- [Pipeline Overview by Phase](#pipeline-overview-by-phase)
- [The Unified Craft Card Standard](#the-unified-craft-card-standard)
- [Precedence — When Two Cards Disagree](#precedence-when-two-cards-disagree)
- [The engine record — before the first prompt](#the-engine-record-before-the-first-prompt)
- [Technical Metrics & Verification Guarantees](#technical-metrics-verification-guarantees)

<!-- /GENERATED:toc -->

## The 8-Phase Production Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────┐
│                      THE 8-PHASE AI FILM PRODUCTION PIPELINE                       │
├────────────────────────────────────────────────────────────────────────────────────┤
│  Phase 1: Story Generation         │ 1,332 Craft Cards │ Dramatic Architecture     │
│  Phase 2: Screenplay & Dialogue    │   585 Craft Cards │ Script & Character Voice  │
│  Phase 3: Shooting Script          │   768 Craft Cards │ Shot Breakdown & Audio    │
│  Phase 4: Audio Narration & Voice  │   260 Craft Cards │ Voiceover & Performance   │
│  Phase 5: Song & Music Generation  │   340 Craft Cards │ Suno / Lyria              │
│  Phase 6: Storyboard Layout        │   194 Craft Cards │ Staging, Panels, Timing   │
│  Phase 7: Image Prompt Engineering │   889 Craft Cards │ Optical Stills & Canon    │
│  Phase 8: Video Prompt Engineering │   394 Craft Cards │ Temporal Motion Vectors   │
├────────────────────────────────────────────────────────────────────────────────────┤
│  TOTAL: 4,762 CORE CRAFT CARDS (5,386 TOTAL SEARCHABLE HEADINGS)                   │
└────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Execution Modes: Express Auto vs. Director Review

The pipeline supports two distinct operational modes:
1. **Express Auto Modes (1-4)**: Designed for high-speed automated workflows. The engine provides an upfront credit estimate (*"This project will generate [X] images and [Y] video clips"*), the user confirms once, and generation executes seamlessly.
2. **Interactive Director Review Mode (5)**: Review pauses the owner opted into at each milestone (Script, Audio, Storyboard, and Stills) — not gates; with the owner absent the run falls back to prompts only (HOW-1 Q1). The one gate, in every mode, is the **Keyframe Approval Gate**: still keyframes from Phase 7 are reviewed and approved before Phase 8 video motion synthesis is unlocked. Beside it, only the spend approval and a real person's consent before their voice or likeness is cloned wait for anyone (root `SKILL.md` §0).

## Pipeline Overview by Phase

### 1. [Phase 1: Story Generation](./phase-01-story-generation/) (1,332 Craft Cards)
- **Manifest**: [PHASE.md](./phase-01-story-generation/PHASE.md) | [HOW-PHASE-1-WORKS.md](./phase-01-story-generation/HOW-PHASE-1-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-01-story-generation/INDEX.md) | [LOOKUP.md](./phase-01-story-generation/LOOKUP.md)
- **Scope**: Core narrative architecture, genre bibles (16 genres), world building, character arc engines, thematic engines, narrative hooks, conflict matrices, and archetypal structures.

### 2. [Phase 2: Screenplay & Dialogue](./phase-02-screenplay-dialogue/) (585 Craft Cards)
- **Manifest**: [PHASE.md](./phase-02-screenplay-dialogue/PHASE.md) | [HOW-PHASE-2-WORKS.md](./phase-02-screenplay-dialogue/HOW-PHASE-2-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-02-screenplay-dialogue/INDEX.md) | [LOOKUP.md](./phase-02-screenplay-dialogue/LOOKUP.md)
- **Scope**: Screenplay formatting, dialogue rhythms, subtext layers, argument dynamics, linguistic registers, silence and pauses, character speech mannerisms, and dialect fidelity.

### 3. [Phase 3: Shooting Script](./phase-03-shooting-script/) (768 Craft Cards)
- **Manifest**: [PHASE.md](./phase-03-shooting-script/PHASE.md) | [HOW-PHASE-3-WORKS.md](./phase-03-shooting-script/HOW-PHASE-3-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-03-shooting-script/INDEX.md) | [LOOKUP.md](./phase-03-shooting-script/LOOKUP.md)
- **Scope**: Two-column AV shooting script, shot numbers, coverage strategy, camera setups, transition grammar, dialogue-to-visual bridges, and sound design queues.

### 4. [Phase 4: Audio Narration & Voice](./phase-04-audio-narration/) (260 Craft Cards)
- **Manifest**: [PHASE.md](./phase-04-audio-narration/PHASE.md) | [HOW-PHASE-4-WORKS.md](./phase-04-audio-narration/HOW-PHASE-4-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-04-audio-narration/INDEX.md) | [LOOKUP.md](./phase-04-audio-narration/LOOKUP.md)
- **Scope**: Voiceover delivery styles, documentary narration, pacing/meter, breathing pauses, emotional resonance, voice timbre casting, and TTS/AI voice prompts (ElevenLabs, Cartesia).

### 5. [Phase 5: Song & Music Generation](./phase-05-song-generation/) (340 Craft Cards)
- **Manifest**: [PHASE.md](./phase-05-song-generation/PHASE.md) | [HOW-PHASE-5-WORKS.md](./phase-05-song-generation/HOW-PHASE-5-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-05-song-generation/INDEX.md) | [LOOKUP.md](./phase-05-song-generation/LOOKUP.md)
- **Scope**: Song-engine audio prompt engineering (Suno v6 and Lyria 3.5: their syntax and vendor facts live on the `suno.` and `lyria.` cards with sources; other engines in the dated adapters of `ENGINE-CHECK.md` §7). Covers structural section tags (`[Verse]`, `[Chorus]`), global maqam systems, Near Eastern heritage instrumentation (oud, qanun, nay, santur, riqq), Mesopotamian/Assyrian/Syriac liturgical and folk modes, cinematic orchestration, modern urban beats, and vocal delivery modifiers.

### 6. [Phase 6: Storyboard Layout](./phase-06-storyboard-layout/) (194 Craft Cards)
- **Manifest**: [PHASE.md](./phase-06-storyboard-layout/PHASE.md) | [HOW-PHASE-6-WORKS.md](./phase-06-storyboard-layout/HOW-PHASE-6-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-06-storyboard-layout/INDEX.md) | [LOOKUP.md](./phase-06-storyboard-layout/LOOKUP.md)
- **Scope**: Multi-panel deck architecture, spatial composition, 180-degree rule blocking, character eyelines, shot sizes (EWS to ECU), Dutch angles, animatic beat timing grid, identity consistency rules, and Mesopotamian heritage staging.

### 7. [Phase 7: Image Prompt Engineering](./phase-07-image-prompt-engineering/) (889 Craft Cards)
- **Manifest**: [PHASE.md](./phase-07-image-prompt-engineering/PHASE.md) | [HOW-PHASE-7-WORKS.md](./phase-07-image-prompt-engineering/HOW-PHASE-7-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-07-image-prompt-engineering/INDEX.md) | [LOOKUP.md](./phase-07-image-prompt-engineering/LOOKUP.md)
- **Specialized Assets**: Master character turnaround sheets, location plates, prop references, and the authoritative **Mesopotamia Canon** — `canon-rules.md` and `heritage-rules.md`, the router `CANON-LOOKUP.md`, the world in `grimoire-01` … `grimoire-20` and the wardrobe in `clothing-01` … `clothing-11`.
- **Scope**: The 7-Slot Universal Prompt Order, physical sensor optics, Panavision/Cooke lenses, Kelvin lighting physics, film stocks (Kodak Vision3, Fuji Eterna), material surface micro-geometry, and model syntax by prompt family, with each engine's dated syntax in `ENGINE-CHECK.md` §7.

### 8. [Phase 8: Video Prompt Engineering](./phase-08-video-prompt-engineering/) (394 Craft Cards)
- **Manifest**: [PHASE.md](./phase-08-video-prompt-engineering/PHASE.md) | [HOW-PHASE-8-WORKS.md](./phase-08-video-prompt-engineering/HOW-PHASE-8-WORKS.md)
- **Catalogs**: [INDEX.md](./phase-08-video-prompt-engineering/INDEX.md) | [LOOKUP.md](./phase-08-video-prompt-engineering/LOOKUP.md)
- **Specialized Assets**: [how-to-write-a-video-prompt.md](./phase-08-video-prompt-engineering/how-to-write-a-video-prompt.md) (51.6 KB).
- **Scope**: The 9 Laws of Video Prompting, 6-axis camera kinematics (Translate X/Y/Z, Rotate Pitch/Yaw/Roll), First-Frame to Last-Frame (F2L) conditioning pairs, speed ramping, temporal continuity checks, and frontier engine prompt syntax (Kling 1.5/2.0, Runway Gen-3 Alpha/Turbo, Minimax Hailuo Video-01, Luma Ray 2, OpenAI Sora, Wan 2.1/3.0, ComfyUI).

---

## The Unified Craft Card Standard

Every single one of the 4,762 craft cards conforms strictly to the unified 8-field schema:
```markdown
### Title

**Also called:** [Alternative names, cinema terms, industry synonyms]
**What it is:** [Clear, rigorous mechanical or computational definition]
**Effect on the audience:** [Psychological, emotional, and cognitive impact]
**Used for and where it works best:** [Narrative context, scene placement, optimal use]
**Best in:** [Formats: ... | Genres: ...]
**Avoid when:** [Misuse warnings, failure conditions, negative prompts]
**Prompt:** [Prompt syntax string for visual/audio/kinematic phases] OR **Example:** [Full script lines or illustrative dialogue for writing/narrative phases]
**Outranks:** [Optional. Card ids this card beats, and in what case]
**Yields to:** [Optional. Card ids that beat this card, and in what case]
`prefix.unique_card_id`
```

Every card in the package has been read for the second of those two fields, and the result is
[`PAIR-AUDIT.md`](PAIR-AUDIT.md): a card either has an alternative and carries `**Yields to:**`,
or it has none and is listed there with the reason. The check `card-pair-unaudited` fails on a
card in neither state, which is what makes *every card was read* arithmetic rather than a claim.

`**Outranks:**` and `**Yields to:**` are optional and appear on only a small number of cards. They
record a collision that has actually been found and settled between two named cards, and each one
names the case in which it applies. Most cards carry neither.

---

## Precedence — When Two Cards Disagree

When two cards in hand cannot both be obeyed in the same shot, **[PRECEDENCE.md](./PRECEDENCE.md)**
at the package root states which one wins and why: evidence and truth, then delivery reality, then
audience fit, then locked upstream material, then craft preference. It also states how to tier a
card you find there, and what to do when both sides land on the same tier. It is for genuine
collisions only — two techniques offered as a choice are not a collision.

**Looking for one card by its id?** [`CARD-INDEX.md`](./CARD-INDEX.md) lists every id in the
package and the file that holds it. It is generated from the cards, so it cannot fall behind
them. Search it; do not read it.

---

**And the other one.** [`FORBIDDEN-GLOBAL.md`](./FORBIDDEN-GLOBAL.md) holds what must never
appear anywhere in this piece, decided once for the whole project. It is Tier 0 of every negative
block. Phase 1 fills it from the brief and the canon, and a project that forbids nothing writes `none, per the project brief`, because a decided-nothing
and an unsupplied-nothing must not look the same.

---

## The engine record — before the first prompt

**[ENGINE-CHECK.md](./ENGINE-CHECK.md)** holds the one input the prompt phases cannot supply
themselves: what the selected engine can do today. Fill it at the start of a project; where the brief names no
engine, the agent chooses one and fills the row from its own pages. Prompts are written in full either
way, and only a value no search gives carries `pending_engine_check`. A limit is a reason to change the engine, not the shot.

---

## Technical Metrics & Verification Guarantees

- **100% Pure English Documentation**: All markdown modules, indices, craft cards, and prompt examples are authored in standard, professional English.
- **Zero Duplicate IDs**: Every craft card identifier in the package is globally unique — measured on disk by the source package's build tools, with zero genuine collisions (the one repeat is `prefix.unique_card_id`, the schema's own placeholder in this file and in `SKILL.md`).
- **On the totals in this file**: they measure how much craft is in the box, not a contract. See the note under the table in [`SKILL.md`](../SKILL.md) for why a strict re-count comes back higher.
- **Zero Broken Internal Links**: Every markdown link across all 8 phases resolves directly to an existing local file.
- **Universal Toolchain Support**: Compatible with native Antigravity subagent invocation, prompt pipelines, and multi-agent workflows.
