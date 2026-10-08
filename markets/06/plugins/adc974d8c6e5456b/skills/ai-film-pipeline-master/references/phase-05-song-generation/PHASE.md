---
name: phase-05-song-generation
description: "Phase 5: Song & Music Generation. Directs musical composition, Suno & Lyria 3.5 prompt architecture, Iraqi Maqamat, Near Eastern microtonal modes, and score dynamics across 340 standardized craft cards. Use when scoring a film, generating background soundtrack, composing lyrical songs, or creating ethnic/heritage music. Trigger on: Suno prompt, AI song, film score, soundtrack, Maqam, musical theme, اغنية، موسيقى تصويرية، سونو، مقامات عراقية، لحن، ساوند تراك، اغنية فيلم."
---

# Phase 5: AI Song Generation & Lyric Production

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

Phase 5 provides the complete creative and technical framework for composing, arranging, prompting, and mastering full-length songs. It governs lyrics writing, vocal harmonies, AI engine directing (Suno v6, whose models and syntax are on the `suno.` cards in `suno-engine-craft.md`, and Google's Lyria 3.5, used first in the Gemini app, whose surfaces, limits and syntax are on the `lyria.` cards in `gemini-lyria-engine-craft.md`), authentic cultural musicology (Assyrian/Syriac and Iraqi Maqam), modern genre production blueprints, and the non-negotiable timing bridge for AI music video pipelines.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [When to Use This Skill](#when-to-use-this-skill)
- [The Knowledge Base (340 Craft Cards)](#the-knowledge-base-340-craft-cards)
- [Operational Execution Pipeline](#operational-execution-pipeline)
- [Reference Navigation](#reference-navigation)
- [Files in this phase](#files-in-this-phase)
- [The contract for this phase](#the-contract-for-this-phase)

<!-- /GENERATED:toc -->

## When to Use This Skill

Activate `phase-05-song-generation` whenever a project requires:
1. Writing complete, singable song lyrics with professional prosody, rhyme schemes, and structural balance.
2. Prompting generative AI music engines (a tag-and-style engine such as Suno v6, or a prose-directed model such as Lyria 3.5) with section markers and style descriptors — Suno's models and syntax are on the `suno.` cards in `suno-engine-craft.md`; Lyria 3.5's are on the `lyria.` cards in `gemini-lyria-engine-craft.md`.
3. Composing authentic Middle Eastern, Mesopotamian (Iraqi Maqam), or Assyrian/Syriac folk and liturgical music (Khigga, Sheikhani, Beth Gazo).
4. Producing songs across modern global genres (Hyperpop, Synthwave, Drill, Afrobeats, Amapiano, Djent, Liquid DnB, etc.).
5. Isolating audio stems (Vocals, Drums, Bass, Instruments) and naming the loudness standard the destination enforces, so the master can be made to it in the edit.
6. Creating a locked audio timing map and cue sheet to drive **Phase 3 (the shot table), then Phase 6: Storyboard Layout** in an AI music video workflow.

---

## The Knowledge Base (340 Craft Cards)

The skill contains **340 craft cards** organized into 16 specialized modules:

1. **[cat-lyric.md](./cat-lyric.md)** (32 cards): Lyric architecture, Verse-Chorus-Bridge spines, AABA, and foundational songwriting rules.
2. **[cat-lyric-2.md](./cat-lyric-2.md)** (34 cards): Advanced prosody, hook craft, multi-syllabic rhyming, and named songwriting failures.
3. **[cat-lyric-3.md](./cat-lyric-3.md)** (10 cards): Dramatic songs, musical theatre, character voice, and through-composed narratives.
4. **[cat-lyric-4.md](./cat-lyric-4.md)** (1 card): High-density lyrical compression and specialized genre rules.
5. **[lyric-craft.md](./lyric-craft.md)** (8 cards): Meter scansion, stress alignment, vowel casting, and emotional energy ramps.
6. **[suno-engine-craft.md](./suno-engine-craft.md)** (19 cards): Suno v6 craft with Suno's own syntax and dated vendor facts: section tags, the Styles and Exclude fields, vocal direction, extension and persona workflows.
7. **[gemini-lyria-engine-craft.md](./gemini-lyria-engine-craft.md)** (14 cards): Google Lyria 3.5 craft with Google's own syntax and dated vendor facts, Gemini app first: runtime and limits, the prompt formula, lyrics and languages (Arabic status), tempo, dynamics, modal colour, output formats.
8. **[assyrian-syriac-music-craft.md](./assyrian-syriac-music-craft.md)** (22 cards): Traditional Assyrian dance meters (Khigga, Sheikhani, Bagiyeh), Beth Gazo liturgical modes, and acoustic Zurna/Davula directing.
9. **[mesopotamian-arabic-maqam-craft.md](./mesopotamian-arabic-maqam-craft.md)** (25 cards): Iraqi Maqamat (Bayati, Hijaz, Saba, Rast), Mawal improvisations, Bastah rhythms, and authentic Oud/Santur arrangements.
10. **[song-stems-and-timing-handoff.md](./song-stems-and-timing-handoff.md)** (18 cards): Stem isolation, locked audio timing maps, beat grids, and video production handoff.
11. **[rhyme-prosody-phonetics.md](./rhyme-prosody-phonetics.md)** (26 cards): Slant rhymes, mosaic rhymes, vowel belting placement, and consonant softening.
12. **[vocal-arrangement-harmonies.md](./vocal-arrangement-harmonies.md)** (26 cards): Vocal doubling, parallel thirds, choral counterpoint, and whisper sizzle tracks.
13. **[assyrian-syriac-expanded.md](./assyrian-syriac-expanded.md)** (26 cards): Rare mountain circle dances (Mamer, Tolama, Jani, Chobi), classical Syriac poetic meters (Mor Afrem), and diaspora masters.
14. **[modern-genre-production-blueprints.md](./modern-genre-production-blueprints.md)** (27 cards): Complete sound design blueprints for 25 contemporary music styles.
15. **[songwriting-psychology-hooks.md](./songwriting-psychology-hooks.md)** (26 cards): Cognitive earworms, tension-release cycles, dopamine loops, and hook architecture.
16. **[commercial-sync-music-supervision.md](./commercial-sync-music-supervision.md)** (26 cards): Trailer 3-act builds, broadcast loudness compliance, dialogue ducking windows, and sync stingers.

---

## Operational Execution Pipeline

### Phase Input
- Story outline or screenplay brief (from Phase 1 / Phase 2). On the music-video route this is a spine rather than a full Phase 1 deliverable — but it is not optional, because the format kit in `formats-music.md` is built on Phase 1 and Phase 2 cards.
- Target genre, musical style, vocal language, and target runtime.
- Generative engine selection — the brief's, or chosen by this phase where the brief names none and recorded under `decisions` (a tag-and-style engine such as Suno v6, whose models and syntax are on the `suno.` cards; or a prose-directed model such as Lyria 3.5, whose surfaces, limits and syntax are on the `lyria.` cards).

### Phase Output
1. **Master Lyric Sheet**: Complete lyrics with bracketed structural metatags, rhyme scansion notations, and vocal harmony markers.
2. **Engine Generation Prompt**: Fully assembled prompt ready for Suno or Lyria 3.5 (Style string, BPM, metatags, vocal instructions; for Lyria 3.5, one prose prompt with `Lyrics:` and section tags).
3. **Audio Files**: Isolated stems (.wav) and the full mix (.wav / .flac), delivered **unmastered with headroom intact**, together with a note naming the loudness standard the destination enforces. The master is made in the edit.
4. **Locked Audio Timing Map**: Time-coded cue sheet mapping every downbeat, section transition, and emotional turn to guide **Phase 3 (the shot table), then Phase 6: Storyboard Layout**.

---

## Reference Navigation
- **[HOW-PHASE-5-WORKS.md](./HOW-PHASE-5-WORKS.md)**: Deep technical walkthrough and operational directing protocol.
- **[INDEX.md](./INDEX.md)**: Full catalog of all 340 craft cards categorized by functional domain.
- **[LOOKUP.md](./LOOKUP.md)**: Master ID lookup table for quick card retrieval.
- **[formats-music.md](./formats-music.md)**: Format constraints and ranked kits for songs and music videos.

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**17 craft files, 340 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md), with 1 per-family shards beside it, generated from the same source. Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`cat-lyric.md`](cat-lyric.md) | **Lyric, Verse, Refrain and Song Structure** — Lyric Architecture & Form (Part 1) <br>*Cards scoped to: mostly musical theatre, kids song, song lyric, single, among 32 formats* | 32 |
| [`cat-lyric-2.md`](cat-lyric-2.md) | **Lyric, Verse, Refrain and Song Structure — Part 2** — Lyric Form & Sound Craft (Part 2) <br>*Cards scoped to: mostly Song Lyric, Musical Theatre, Live Event, Animation Feature, among 28 formats* | 34 |
| [`cat-lyric-3.md`](cat-lyric-3.md) | **Lyric, Verse, Refrain and Song Structure — Part 3** — Lyric Advanced Form & Voice (Part 3) <br>*Cards scoped to: mostly Live Event, Audio Drama, Feature Film, Podcast, among 19 formats* | 10 |
| [`cat-lyric-4.md`](cat-lyric-4.md) | **Lyric, Verse, Refrain and Song Structure — Part 4** — Lyric Genre Refinements (Part 4) <br>*Cards scoped to: mostly Essay, Memoir, Poetry, Prose Poem, among 5 formats* | 1 |
| [`lyric-craft.md`](lyric-craft.md) | **Lyric Craft & Song-to-Visual Architecture** — Lyric Mechanics & Meter Dynamics <br>*Cards scoped to: mostly Song Lyric, Music Video, Ballad, Children's Song, among 16 formats* | 8 |
| [`suno-engine-craft.md`](suno-engine-craft.md) | **Tag-and-Style Song Engine Craft** — Tag-and-Style Song Engine (written for Suno) <br>*Cards scoped to: any format* | 19 |
| [`gemini-lyria-engine-craft.md`](gemini-lyria-engine-craft.md) | **Google Lyria 3.5 Engine Craft** — Google Lyria 3.5 Engine Craft: the Gemini app first, with ready-to-paste prompts <br>*Cards scoped to: any format* | 14 |
| [`assyrian-syriac-music-craft.md`](assyrian-syriac-music-craft.md) | **Assyrian & Syriac Songcraft, Rhythms & Liturgical Heritage** — Assyrian & Syriac Folk & Liturgical Suite <br>*Cards scoped to: any format* | 22 |
| [`mesopotamian-arabic-maqam-craft.md`](mesopotamian-arabic-maqam-craft.md) | **Mesopotamian & Arabic Maqam Craft & Poetic Forms** — Mesopotamian & Iraqi Maqam Heritage <br>*Cards scoped to: any format* | 25 |
| [`song-stems-and-timing-handoff.md`](song-stems-and-timing-handoff.md) | **Song Stems, Locked Audio Timing & Video Handoff** — Song Stems, Timing Grid & Phase 3 / Phase 6 Handoff <br>*Cards scoped to: any format* | 18 |
| [`rhyme-prosody-phonetics.md`](rhyme-prosody-phonetics.md) | **Songwriting Rhyme Schemes, Prosody & Vocal Phonetics** — Rhyme Schemes, Prosody & Vocal Phonetics <br>*Cards scoped to: any format* | 26 |
| [`vocal-arrangement-harmonies.md`](vocal-arrangement-harmonies.md) | **Vocal Arrangement, Choral Textures & Multi-Part Harmonies** — Vocal Arrangement & Multi-Part Harmonies <br>*Cards scoped to: mostly Epic Anthem, Musical Theatre, Art Song, Film Soundtrack, among 67 formats* | 26 |
| [`assyrian-syriac-expanded.md`](assyrian-syriac-expanded.md) | **Assyrian & Syriac Expanded Folk, Epic & Classical Traditions** — Assyrian & Syriac Expanded Folk & Epics <br>*Cards scoped to: any format* | 26 |
| [`modern-genre-production-blueprints.md`](modern-genre-production-blueprints.md) | **Modern Genre Production Blueprints** — Modern Genre Production Blueprints <br>*Cards scoped to: any format* | 27 |
| [`songwriting-psychology-hooks.md`](songwriting-psychology-hooks.md) | **Songwriting Psychology and Catchy Hooks** — Songwriting Psychology & Catchy Hooks <br>*Cards scoped to: any format* | 26 |
| [`commercial-sync-music-supervision.md`](commercial-sync-music-supervision.md) | **Commercial Sync and Music Supervision** — Commercial Sync & Music Supervision <br>*Cards scoped to: mostly Broadcast Bumper, Film/TV Post-Production Deliverable, Movie Trailer, TV Promo, among 78 formats* | 26 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`formats-music.md`](formats-music.md) | Formats — music and song — Entry point into the database. Each kit lists technique ids; open the matching `cat-*.md` for the full card. Covers: Music Video — Narrative, Music Video — Teaching Song, Music Video — Concept and Performance, Lyric Video, Song Lyric, Concert and Performance Film, The Musical Number in Film and Theatre, The Character Song and the "I Want" Song, The Album as a Structure, The Score-Led Sequence, The Needle-Drop, Music in Advertising. |

<!-- /GENERATED:file-registry -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `genre`, `duration_s`, `engine_record` |
| **One-of read groups** | `story_brief` or `existing_picture_timing` or `source_audio` |
| **Optional reads** | `script` |
| **External inputs allowed** | `story_brief`, `existing_picture_timing`, `source_audio` |
| **Writes** | `timing_map`, `lyrics`, `stems` |
| **May not re-decide** | `story_brief`, `genre` |
| **Execution gate** | `paid_generation_approved_by` |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `music_video` | `phase-01-story-generation` | `phase-03-shooting-script` |
| `score_existing_film` | `external / intake` | `delivery / edit` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

---
