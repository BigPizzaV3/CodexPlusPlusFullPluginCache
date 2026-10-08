---
name: phase-04-audio-narration
description: "Phase 4: Audio Narration & Voice Direction. Directs voiceover casting, ElevenLabs vocal delivery, speech pacing (WPM), breath pauses, LUFS audio mastering, and acoustic soundscapes across 260 standardized craft cards. Use when recording or generating narration, voice acting, audio cleanup, or dialogue delivery. Trigger on: voiceover, narration, voice casting, ElevenLabs, vocal delivery, audio mastering, تعليق صوتي، فويس اوفر، تسجيل صوت، هندسة صوت، نبرة صوت، ممثل صوتي."
---

# Phase 4: Audio & Narration Breakdown (ElevenLabs Ready)

> **Where this phase stops.** Phase 4 produces **directed voice, written intent, and the stems the
> edit will need** — casting, performance, pacing, pronunciation, the sound world, and four separate,
> unmastered audio files with their headroom intact. It does not mix. **Levels, ducking, loudness and
> the final mix are set in the edit**, by hand, against the actual material. A card here names the
> move and says what it is for; the value — the gain, the ratio, the threshold, the ceiling, the
> length of a silence measured on a timeline — is set by the person making it, who is not reading
> this card. This is the same boundary already drawn around montage and subtitles: the phase
> specifies, the edit decides.

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Inputs](#inputs)
- [Workflow Steps](#workflow-steps)
- [Reference Architecture](#reference-architecture)
- [Error Handling & Warnings](#error-handling-warnings)
- [Files in this phase](#files-in-this-phase)
- [The contract for this phase](#the-contract-for-this-phase)

<!-- /GENERATED:toc -->

## Overview
Phase 4 transforms written screenplays, dialogue, and scene cues from [Phase 2](../phase-02-screenplay-dialogue/PHASE.md) — and from [Phase 3](../phase-03-shooting-script/PHASE.md) only where it ran first; on a narrated piece this phase runs before it — into professionally engineered vocal performances and multi-layered soundscapes. It pairs **260 specialized craft cards** across its modules with the ElevenLabs directing craft (current model names and settings live in the dated adapter in `ENGINE-CHECK.md` §7), subtext directing, the 4-stem audio architecture, foley design, and the mix intent the edit works to.

```
phase-04-audio-narration/
├── PHASE.md                          # Antigravity skill manifest
├── HOW-PHASE-4-WORKS.md              # Complete 8-step audio pipeline guide
├── INDEX.md                          # Full catalog of 260 craft cards
├── LOOKUP.md                         # Stable ID routing table
├── elevenlabs-engine-craft.md        # 16 cards: TTS parameters, models, directing tags
├── voice-casting-profiles.md         # 19 cards: Archetypal vocal profiles & casting
├── voice-acting-subtext.md           # 23 cards: Suppressed rage, grief fracture, cold smiles
├── pacing-cadence-wpm.md             # 21 cards: Speaking rates, pauses, breath marks
├── soundscape-sfx-score.md           # 24 cards: 4-stem mix, foley, historical ambience
├── foley-and-sound-design.md         # 26 cards: Bronze blades, mud-brick steps, braams, sub-drops
├── pronunciation-and-accents.md      # 17 cards: Phonetic spelling, ancient names, accents
├── multilingual-dubbing-lipsync.md   # 21 cards: Syllable ratios, bilabial sync, voice clones
├── audio-mixing-mastering.md         # 23 cards: mix intent handed to the edit (carving, ducking, loudness, M/S)
├── audio-restoration-cleanup.md      # 19 cards: Mouth de-clicking, de-essing, DC offset
├── score-composition-dynamics.md     # 21 cards: Leitmotifs, Maqam scales, BPM sync, drones
├── ../phase-03-shooting-script/sound-as-visual.md                # 26 cards: J-Cut, L-Cut, Sound Bridges, active silence
├── ../phase-02-screenplay-dialogue/cat-voice.md                      # 32 cards: Voice persona & narrative authority
├── ../phase-02-screenplay-dialogue/cat-voice-2.md                    # 41 cards: Register families, diction & dialect
├── production-recording.md           # 9 cards: Live & generative recording sessions
├── realization-sound.md              # 8 cards: Sonic event maps & listening matrices
├── sensory-sonic.md                  # 13 cards: Acoustic intimacy & horizons
└── formats-audio.md                  # 5 format kits: Narrative Podcast, Interview Podcast, Radio and Audio Drama, Audiobook Narration, Voiceover Script
```

---

## When to Use
Use Phase 4 whenever:
- Directing spoken narration, character dialogue, or voiceover for video production.
- Directing nuanced vocal subtext (suppressed fury, grief cracking, deceptive smiles).
- Choosing and setting a voice engine's model tier (written for ElevenLabs; the current models and settings are in its dated adapter in `ENGINE-CHECK.md` §7).
- Calibrating video speaking rates (WPM) and frame-accurate timing from audio.
- Directing pronunciation for ancient Mesopotamian, Akkadian, Sumerian, or foreign historical terms.
- Designing soundscapes, foley cues, and documentary background score beds across 4 isolated stems.
- Writing the mix intent the edit will work to, and naming the loudness standard the destination platform enforces — without setting the figure, which is looked up and applied at master time.
- Preparing clean, dry dialogue stems for AI video lip-sync models.

---

## Inputs
1. **Screenplay Audio Column:** The right-hand column from Phase 2 containing dialogue, narration text, and speaker names.
2. **Shooting Script Beat Timings:** Target scene durations and cuts from Phase 3 — only where Phase 3 ran first. On a narrated piece taken in route order it has not: this phase measures the audio, and Phase 3 builds its table to that measurement.
3. **Format & Genre Constraints:** Video type (e.g. 60s Reel, 15m Documentary, 3m Music Video).
4. **Economic Mode Preference:** Free text-only prompt markup vs paid ElevenLabs API synthesis.

---

## Workflow Steps
1. **Voice Casting & Subtext:** Select archetype from [voice-casting-profiles.md](voice-casting-profiles.md) and apply emotional subtext from [voice-acting-subtext.md](voice-acting-subtext.md).
2. **Pacing Calibration:** Calculate exact WPM and insert punctuation breath marks from [pacing-cadence-wpm.md](pacing-cadence-wpm.md).
3. **Phonetic Sanitization:** Convert historical names to phonetic syllables using [pronunciation-and-accents.md](pronunciation-and-accents.md).
4. **4-Stem Soundscape Layout:** Map Dialogue, SFX, Ambience, and Music using [soundscape-sfx-score.md](soundscape-sfx-score.md) and [foley-and-sound-design.md](foley-and-sound-design.md).
5. **Voice Engine Directing:** Set steadiness, likeness, the style amplifier and delivery direction, per the engine's adapter in `ENGINE-CHECK.md` §7, via [elevenlabs-engine-craft.md](elevenlabs-engine-craft.md).
6. **Restoration Diagnosis:** Identify saliva clicks, neural sibilance and generation artefacts and flag them for the edit via [audio-restoration-cleanup.md](audio-restoration-cleanup.md). The pre-flight cleaning of voice-cloning samples is done *here*, because it decides what the clone sounds like.
7. **Mix Intent:** Write the handover notes the edit will work to — what sits under what, where speech has to stay clear, which spaces the voice belongs in, which loudness standard the destination enforces — via [audio-mixing-mastering.md](audio-mixing-mastering.md). The mix itself happens in the edit.
8. **Handoff:** Pass the unmastered stems, the mix-intent notes, the timed subtitle file where the brief or the genre kit asks for subtitles or captions, and locked audio duration measurements to the route-specific successor in the generated table below. The table, from `PROJECT-STATE.md`, is the only place that names it.

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `phase-02-screenplay-dialogue` | `phase-03-shooting-script` |
| `narrated_documentary` | `phase-02-screenplay-dialogue` | `phase-03-shooting-script` |
| `commercial_narrated` | `phase-02-screenplay-dialogue` | `phase-03-shooting-script` |
| `audio_only` | `phase-02-screenplay-dialogue` | `delivery / edit` |
| `audio_with_cover` | `phase-02-screenplay-dialogue` | `phase-07-image-prompt-engineering` |
| `supplied_script_voiceover` | `external / intake` | `delivery / edit` |
| `supplied_audio_cleanup` | `external / intake` | `delivery / edit` |
| `interactive_branching_audio` | `phase-02-screenplay-dialogue` | `phase-03-shooting-script` |
| `data_led_built` | `phase-02-screenplay-dialogue` | `phase-03-shooting-script` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

For full step-by-step guidance, see [HOW-PHASE-4-WORKS.md](HOW-PHASE-4-WORKS.md).

---

## Reference Architecture
- Master Catalog: [INDEX.md](INDEX.md)
- Routing Table: [LOOKUP.md](LOOKUP.md)
- Route authority: [`PROJECT-STATE.md`](../PROJECT-STATE.md), rendered in the generated handoff table above.

---

## Error Handling & Warnings
- **TTS Mispronunciation:** If the synthesizer mispronounces a name, never repeat the raw spelling; consult [pronounce.phonetic_spelling_tts](pronunciation-and-accents.md) and hyphenate.
- **Vocal Instability / Pitch Drift:** Raise Stability and lower Style Exaggeration via [elevenlabs.stability_tuning](elevenlabs-engine-craft.md); the settings and what the vendor documents about them are in the ElevenLabs adapter, [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §7.
- **Acoustic Mud:** If music drowns speech, the repair is in the edit, and it is two moves: carve the music where it collides with the voice ([mix.frequency_slot_carving](audio-mixing-mastering.md)) and duck it to the voice ([soundscape.ducking_ratio](soundscape-sfx-score.md)). Both are set by ear against the actual cue.
- **Saliva Clicks:** Apply high-frequency spectral de-clicking via [restore.mouth_de_clicking](audio-restoration-cleanup.md).

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**15 craft files, 260 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md). Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`voice-casting-profiles.md`](voice-casting-profiles.md) | **Voice Casting & Archetypal Profiles** — Voice Casting & Archetypal Profiles <br>*Cards scoped to: mostly Feature Film, Audio Fiction / Audio Drama, Drama Series, Short Film, among 39 formats* | 19 |
| [`voice-acting-subtext.md`](voice-acting-subtext.md) | **Voice Acting Subtext & Covert Emotional Delivery** — Voice Acting Subtext & Covert Emotional Delivery <br>*Cards scoped to: mostly Drama Series, Feature Film, Historical Drama, Historical Epic, among 46 formats* | 23 |
| [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) | **Pacing, Cadence & WPM Calibration** — Pacing, Cadence & WPM Calibration <br>*Cards scoped to: any format* | 21 |
| [`pronunciation-and-accents.md`](pronunciation-and-accents.md) | **Pronunciation, Accents & Phonetic Directing** — Pronunciation, Accents & Phonetic Directing <br>*Cards scoped to: any format* | 17 |
| [`soundscape-sfx-score.md`](soundscape-sfx-score.md) | **Soundscape, SFX & Score Architecture** — Soundscape, SFX & 4-Stem Score Architecture <br>*Cards scoped to: any format* | 24 |
| [`foley-and-sound-design.md`](foley-and-sound-design.md) | **Foley & Historical Cinematic Sound Design** — Foley & Historical Cinematic Sound Design <br>*Cards scoped to: any format* | 26 |
| [`elevenlabs-engine-craft.md`](elevenlabs-engine-craft.md) | **ElevenLabs Engine & Directing Craft** — ElevenLabs Engine & Parameter Tuning <br>*Cards scoped to: any format* | 16 |
| [`audio-restoration-cleanup.md`](audio-restoration-cleanup.md) | **AI Audio Restoration, Cleanup & Artifact Elimination** — AI Audio Restoration, Cleanup & Artifact Elimination <br>*Cards scoped to: any format* | 19 |
| [`audio-mixing-mastering.md`](audio-mixing-mastering.md) | **Audio Mixing, Mastering & Post-Production for AI Video** — Audio Mixing, Mastering & Post-Production <br>*Cards scoped to: any format* | 23 |
| [`multilingual-dubbing-lipsync.md`](multilingual-dubbing-lipsync.md) | **Multilingual Dubbing, Lip-Sync & Localization Craft** — Multilingual Dubbing, Lip-Sync & Localization <br>*Cards scoped to: any format* | 21 |
| [`score-composition-dynamics.md`](score-composition-dynamics.md) | **Score Composition Dynamics, Leitmotifs & Underscore** — Score Composition Dynamics, Leitmotifs & Underscore <br>*Cards scoped to: any format* | 21 |
| [`production-recording.md`](production-recording.md) | **Production Execution: Audio, Voice & Recording** — Production Execution: Live & Generative Recording <br>*Cards scoped to: mostly Documentary Feature, Feature Film, Audio Drama, Commercial, among 23 formats* | 9 |
| [`realization-sound.md`](realization-sound.md) | **Realization: Sound, Voice & Silence** — Realization: Sound, Voice & Silence Architecture <br>*Cards scoped to: any format* | 8 |
| [`sensory-sonic.md`](sensory-sonic.md) | **Sensory Sonic Palette: Voice, Music & Silence** — Sensory Sonic Palette: Intimacy & Acoustic Horizons <br>*Cards scoped to: any format* | 13 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`formats-audio.md`](formats-audio.md) | Formats — audio — Entry point into the database. Each kit is a ranked short list; open the `cat-*.md` named in the row for the full card. Covers: Narrative Podcast, Interview Podcast, Radio and Audio Drama, Audiobook Narration, Voiceover Script, On the visual kit. |

<!-- /GENERATED:file-registry -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `language`, `audio_profile`, `rate_wpm`, `engine_record` |
| **One-of read groups** | `script` or `source_audio` |
| **Optional reads** | `branch_map`, `speaker_map`, `child_voice_clone_consent`, `dialect`, `subtitle_language` |
| **External inputs allowed** | `script`, `branch_map`, `speaker_map`, `source_audio` |
| **Writes** | `measured_duration`, `voice_cast`, `mix_intent` |
| **May not re-decide** | `script`, `branch_map`, `speaker_map` |
| **Execution gate** | `paid_generation_approved_by` |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

---
