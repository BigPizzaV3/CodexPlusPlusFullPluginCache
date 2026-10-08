# Phase 02: Screenplay, Dialogue & Narration Engine — Specification & Instructions

Written directly from the core rules, stage instructions, and craft bibles of the system.
Governs the drafting of line-by-line screenplays, character dialogue, voiceover narration, and action lines, backed by 585 core craft cards (781 total headings).

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Core Operating Principles](#1-core-operating-principles)
- [2. Table Formats (The Three Pipelines)](#2-table-formats-the-three-pipelines)
- [3. The Music & Song Bypass Route](#3-the-music-song-bypass-route)
- [4. Craft Bible & Card Architecture (585 Cards)](#4-craft-bible-card-architecture-585-cards)
- [5. Phase 2 Deliverable (The Handoff)](#5-phase-2-deliverable-the-handoff)

<!-- /GENERATED:toc -->

## 1. Core Operating Principles

1. **A Bridge, Not Mutual Coupling:**  
   Phase 2 receives the `Story Foundation Brief` from Phase 1 and produces a standalone, self-contained `Screenplay & Dialogue Script`. It does not guess the story; it executes the narrative beats.
2. **Observable Actions Only (`act.observable_only`):**  
   Action lines describe only what a camera could see or record. Interior feelings, thoughts, and memories must be externalized into physical behavior.
3. **No Camera in the Script (`act.no_camera_in_script`):**  
   The visual column describes dramatic action and intent (*"He stops at the carving and runs his fingers across the broken cuneiform"*). It NEVER dictates camera angles, lens sizes, or framing (*"Close on hand, 35mm low angle"*). The shot plan in Phase 3 owns the camera.
4. **No Say Cow, See Cow (`nar.say_cow`):**  
   Narration must never state what the viewer is already looking at. If the visual shows a burning wall, the voiceover explains who built it or what was lost inside it.
5. **Language Governance:**  
   The script metadata, document headers, and structural notes are written in English. The actual spoken dialogue or voiceover lines inside the Audio column are written in the user's requested language (English, Arabic, Assyrian/Sureth, etc.), in the dialect the brief asked for, as asked. **Before writing lines in a dialect, open that dialect's casting card first** — for Iraqi Arabic, `voice.cast_regional_iraqi_dialect` in Phase 4, which says which forms each community uses — so the script is written in the speaker's own forms the first time rather than corrected at casting.

---

## 2. Table Formats (The Three Pipelines)

Pick by what the finished piece is: **A** for anything with a picture and no locked audio, **B** when
a song or a recorded track already exists and its timing governs, **C** when there is no picture at
all and the piece is not a song.

### Pipeline A: Standard Screenplay (Dialogue / Narration)
Uses the strict **Two-Column Table**. Every line must have both columns filled. **On a bilingual piece — spoken in one language, subtitled in another — add an optional third column, *Subtitle (target language)*,** so the translation is written here beside its line rather than improvised at the edit; Phase 4 times it (its Step 8).

| Visual, what is seen | Audio, what is heard |
|---|---|
| A sand-covered hand brushes silt off a blackened limestone block. | **NARRATOR (V.O.):**<br>"This wall stood thirty feet high before the river broke it." |
| Two soldiers stare silently through the breach at dawn. | *[Deliberate silence: desert wind and distant river rush]* |
| King Sin-shar-ishkun turns his back to the palace gates. | **SIN-SHAR-ISHKUN:**<br>"Bar the doors. Let the fire bake what they came to take." |

- **Deliberate silence is written:** Never leave an Audio cell empty; state the intentional acoustic presence.
- **On-screen text that is not a subtitle is written in the Visual cell** as `TEXT: "…"` — hook copy,
  a lower third, a label, a title — so it has a home before Phase 3 times it. Subtitles of
  the spoken words are not written this way; the optional third column carries a translation.
- **The end of an advert is recorded as what it must carry, not as a card.** Write one `TEXT:` item
  on the last row naming the logo, the name and the phone number, and anything else the brief names
  for the end (a clearly marked placeholder, `[LOGO]`, `[PHONE]`, where the client has not supplied
  it), and no separate end-card row. Its form — a separate static card, or the logo and number
  folded into the last live shot on a feed advert — is Phase 3's decision under `promo.end_card` in
  [`../phase-03-shooting-script/ads-trailers.md`](../phase-03-shooting-script/ads-trailers.md).
- **A song the story contains that is not written yet** (the extended route: Phase 5 after this phase, before Phase 3 — [`../PROJECT-STATE.md`](../PROJECT-STATE.md) §2): cue it in the Audio cell as `SONG: <cue>` — where it enters, who sings or plays it, what it does in the scene. Phase 5 writes its lyric, and its timing then governs the shot table.
- **Pacing Standard: no rate is written on this page.** Phase 4 owns every speaking rate in the
  package, one card per register, all in
  [`../phase-04-audio-narration/pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md).
  Open the card for the register you are in and take the figure from there:
<!-- GENERATED:rate-cards — do not edit by hand. Generated in the source package -->

**Every speaking rate in the package, and the register each one owns.** Generated from the cards in [`pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md); a figure quoted elsewhere cites its owner here rather than standing alone.

| Card | Register | Best in |
| :--- | :--- | :--- |
| `pacing.wpm_arabic` | Arabic Narration Rate | Documentary, Heritage Reel, Commercial, Podcast |
| `pacing.wpm_children` | Children's Narration Rate | Kids Content, Educational, Museum Family Track |
| `pacing.wpm_commercial_promo` | Commercial Promotional Cadence | Commercial / TVC, Radio Promo |
| `pacing.wpm_documentary` | Documentary Baseline Tempo | Documentary Feature, Heritage / Historical Documentary, Video Essay |
| `pacing.wpm_dramatic_dialogue` | Dramatic Scene Dialogue Cadence | Feature Film, Drama Series Episode, Short Film |
| `pacing.wpm_epic_mythology` | Ancient Epic & Hymnal Gravitas | Feature Film Prologue, Heritage Audio Experience |
| `pacing.wpm_narrated_fiction` | Narrated Fiction Rate | Short Film, Narrative Podcast, Audio Drama, Vertical Short-Form (Reels, Shorts,  |
| `pacing.wpm_social_reels` | Social Media High-Retention Pacing | Vertical Short-Form (Reels, Shorts, TikTok) |
| `pacing.wpm_to_camera` | To-Camera Dialogue Rate | Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Kids Content, Museum Ins |
| `pacing.wpm_vertical_heritage` | Vertical Heritage Reel Cadence | Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary |

<!-- /GENERATED:rate-cards -->

  This page used to carry its own band, and it disagreed with the card that declares itself the only
  place in the package holding a documentary rate — while this phase's own manifest already said no
  rate is written here. Three numbers for one fact, inside one phase; on a 22-minute episode the
  spread was about 880 words of script. Every rate on those cards is a planning estimate in any case,
  and the real duration comes from the rendered audio file, measured.

---

### Pipeline B: Music & Locked Audio (Three-Column Table)
When pre-recorded audio, a Suno track, or locked song timing is present, the table activates the **Third Column (Time)** measured directly from the audio stem:

| Time | Visual, what is seen | Audio / Lyrics, what is heard |
|---|---|---|
| `0:00 - 0:04` | Sun rises over the Adad gate; stone lions cast long shadows. | *[Musical intro: acoustic oud arpeggio with subtle drone]* |
| `0:04 - 0:12` | Children race along the palace terrace carrying clay figurines. | **VOCALS:**<br>"Under the shadow of the lion's wing, we learned to sing..." |

---

### Pipeline C: Audio-Only Script (Two-Column, No Picture)

For a piece that is **heard and never seen** and is not a song — a podcast episode, an audio
documentary, an audio drama, a museum listening post, a guided audio walk. The song bypass in §3
below does not cover these: it routes a *song* past this phase, and skipping Phase 2 for a scripted
22-minute episode would skip the narration craft, the dialogue craft and the structure work, which is
most of what such a piece is made of.

Pipeline A cannot be used here. It requires both columns filled and one of them is what is seen, so
an audio-only writer is asked for a value that does not exist — and the honest answers, an empty cell
or an invented one, are both wrong.

The columns are **what the listener hears** and **what they should picture**, and the second is a
writer's note, never a shot:

| Sound, what is heard | Image in the ear, what the listener should picture |
|---|---|
| *[Reed stylus pressing wet clay, close, unhurried — three strokes then a pause]* | The hand is a boy's, and the pause is him checking the master's face. |
| **NARRATOR:**<br>"He is eleven. He will do this for four more years before anyone lets him sign anything." | — |
| **TABLET VOICE** *(second voice, dry, close, no room)*:<br>"I am the one who copied this. Do not erase my name." | A different acoustic entirely: the room drops away. |

Three rules specific to this pipeline, and they replace nothing in §1 — the say-cow rule, the
language-governance rule and the deliberate-silence rule all still apply. **The source notes inside
rule 3 are not specific to it**, and they apply only on a history piece the user wants realistic or a
piece that states a figure as fact (root `SKILL.md` §0); where they apply, Phase 8's closing check
lists any still open, as notes.

1. **The right-hand column is optional per row and is never a camera instruction.** It exists because
   an audio writer is still directing an image; it is a note to the performer and the sound designer,
   and a row may leave it as `—`.
2. **Every sound is written, including the absence of one.** In a piece with no picture the sound
   design is not decoration on top of the script, it is half the script, so ambience, foley and the
   deliberate silences are written as lines here and not left to the mix.
3. **A second voice is declared at its first line and never by name alone.** Quoted source text — a
   tablet, a letter, a document — is a different speaker with a different acoustic, and the script
   marks it: the speaker label, a bracketed treatment note on the first line, and the attribution the
   listener needs to know whose words these are. A listener cannot see quotation marks. See
   `rhythm.quotation_weight` for what the marking is carrying.
   **On a history piece the user wants realistic, the source goes beside the line.** An ancient line
   put in a mouth is searched for first: found, it is the real line with its publication beside it;
   not found, the closest attested wording is written and marked `pending_quote_source`, a note that
   travels with the handoff ([`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §3). The line is never cut for
   want of a source. **A number the script states as fact** is treated the same way: searched, cited
   when found, and otherwise the closest supported figure is used and marked `pending_figure_source`.
   On any other piece a figure is the brief's or the writer's and carries no marker.

Timing comes from the rendered narration, measured, exactly as on the narrated video route — take the
planning rate from the owner card for the register, never from this page.

---

## 3. The Music & Song Bypass Route

```
[Phase 1: Story Brief]
         │
         ├── If Dramatic Reel / Doc / Short ────────> [Phase 2: Screenplay Table] ──> [Phase 3: Shooting Script]
         │
         └── If Song / Music Video (Audio-Only) ────> [BYPASS PHASE 2] ────────────> [Phase 5: the song, then Phase 3]
```

- If the user intake specifies an **Audio Song**, Phase 2 is bypassed entirely. Phase 2 is not on the song-led routes (`music_video`, `score_existing_film`); the route profile in `PROJECT-STATE.md` names the next phase.
- A **Music Video** is treated as a visual adaptation project that starts from the locked audio output of the song project.
- **A sign, caption or end card the brief names on a song-led route does not bring Phase 2 back.** Its words come from the brief or the lyric sheet and go straight to [`../phase-07-image-prompt-engineering/in-frame-text.md`](../phase-07-image-prompt-engineering/in-frame-text.md); root `SKILL.md` §1, question 5, says the same.

---

## 4. Craft Bible & Card Architecture (585 Cards)

Phase 2 is powered by 585 dedicated craft cards covering:
- **`cat-dial` (Dialogue):** Subtext, status maneuvers, interruptions, conversational bait, rhythmic phrasing.
- **`cat-scene` & `scenes` (Scene Construction):** 61 dramatic scene types, value turns, late entries, early exits.
- **`cat-voice` & `narration-craft`:** Narrator persona, documentary authority, perspective proximity.
- **`action-lines-craft`:** Action lines that describe intent without camera directing.
- **`cat-sub` (Subtext):** The unspoken, physical micro-behaviors, contradiction between word and deed.
- **`cat-rhythm`:** Line cadence, staccato delivery, tempo shifts.
- **`cat-emo` & `cat-comedy`:** Emotional scene arcs, humor, timing, and children's slapstick.

---

## 5. Phase 2 Deliverable (The Handoff)

The destination is route data, not prose. The generated table below is read from the same route
profiles the validator executes, so a picture-less Pipeline C script cannot silently inherit
Pipeline A's next phase, and a narrated script reaches Phase 4, which measures the runtime, before
Phase 3 builds a shot table to it.

Phase 2 concludes by outputting the completed **Screenplay & Dialogue Script**:
- **Script Metadata:** Project Title, Mode, Duration, Audio Profile.
- **Master Script Table:** 2-Column or 3-Column table detailing every visual event and acoustic line.
- **Dialogue / Voice Stems:** Extracted clean text for downstream recording.
- **Speaker Map (`speaker_map`):** each speaker, a casting note for them (age, register, dialect —
  Phase 4 casts the actual voice), and whether each of their lines is spoken on camera or off camera.
  The on-camera lines are the ones a lip-sync engine has to carry. A character in frame with a line or
  two defaults to off camera — the line over a reaction, a back or a cutaway — unless the brief wants
  the mouth seen; the choice is written here.
- **Warning List:** Any non-blocking observations (e.g. dense word count for duration).

This document forms the direct, uncoupled input for the next phase the generated route table names for the active route.

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
