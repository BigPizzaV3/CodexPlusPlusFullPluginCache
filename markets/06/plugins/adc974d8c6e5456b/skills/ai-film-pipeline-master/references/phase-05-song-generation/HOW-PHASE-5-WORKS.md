# How Phase 5 Works: AI Song Generation & Lyric Production

Phase 5 produces broadcast-grade audio songs and technically structured lyrics, serving either as a **standalone audio track** or as the **locked timing and musical foundation** for subsequent video phases (Phase 3 Shooting Script, then Phase 6 Storyboards, Phase 7 Image Prompts, and Phase 8 Video Prompts).

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Pipeline Position & Core Purpose](#1-pipeline-position-core-purpose)
- [2. The 6-Step Song Production Protocol](#2-the-6-step-song-production-protocol)
- [The craft files in this phase - 16 files, 340 cards](#the-craft-files-in-this-phase---16-files-340-cards)

<!-- /GENERATED:toc -->

## 1. Pipeline Position & Core Purpose

```
Phase 1: Story (and Phase 2 where the route runs it)
   │
Phase 5: Song Generation ───► [Standalone Song Audio File (.wav/.flac)]  (Route A ends here)
   │ (Measured Audio Timing Map & Stems)
   ▼
Phase 3: Shooting Script (the shot table, cut to the measured track)
   │
Phase 6: Storyboard Layout (Music Video Bridge)
   │
Phase 7: Image Prompts (Visual Keyframes)
   │
Phase 8: Video Prompts (Cinematic Motion & Sync)
```

**That is the running order on a song route; the phase numbers are only file numbers.** On anything music-led or
narration-led the measured audio comes *first* and the shot table is cut to it, so the real order
is Phase 1 (and Phase 2 where the route runs it) → Phase 5 or Phase 4 → Phase 3 → Phase 6, which is what routing questions 2 and 3 in
the root [`SKILL.md`](../../SKILL.md) decide. Reading the phase numbers as the order is how a shot table gets
built to an estimated duration and then re-cut when the vocal comes back a different length. Until
the audio exists and has been measured, the runtime carries `pending_measured_duration` and is not
written into the shot table as a number.

Phase 5 answers three distinct production routes:
1. **Route A: Audio-Only Song Release**: The project goal is an audio single, album track, jingle, or cultural hymn. The output of Phase 5 is the final master audio file, complete lyrics, and mixed stems.
2. **Route B: Music Video Production**: The project will proceed into AI video generation. The song generated here establishes non-negotiable fixed timing, emotional milestones, chorus turns, and beat drops that Phase 3 (the shot table), then Phase 6 (Storyboard Layout), cut to.
   - **A song inside the story** — sung or played in a scene, on the extended route in [`../PROJECT-STATE.md`](../PROJECT-STATE.md) §2 — runs this route for the stretch of picture it plays under; Step 4 applies only as far as the story wants the song polished.
   - **A character who sings on camera makes the lip-sync engine structural now, not at Phase 8.** Choose it before Phase 3 cuts the shot table — the brief's engine, or the one that best fits the piece after a search of its current documentation — fill the lip-sync lines of the engine record in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §2, record the choice under `decisions`, and hand the take length it allows to Phase 3 with the timing map.
3. **Route C: Score direction — no song**: The piece is a documentary, an ad or a narrative short, and what it needs from this phase is score direction — mood, instrumentation, where the music enters and where it gets out of the narration's way — not a song. Run **Steps 1, 2, 3 and 5**; there are no lyrics, and the timing comes from the piece rather than from the track — **from the measured narration where the piece has speech, and from the designed shot durations where it does not.** A silent film scored to picture is the standard case for this route and it has no narration to measure; naming the narration as the only source sends it looking for a file that does not exist. This is the route a documentary takes when the master route list appears to skip Phase 5 altogether: scoring a film opens this phase, it just opens a smaller part of it.
   - **The cue craft is on the score shelf, and this route opens it first:** [`../phase-04-audio-narration/score-composition-dynamics.md`](../phase-04-audio-narration/score-composition-dynamics.md), whose head card `score.span_before_the_sound` routes a cue by how long it has to hold and what the scene is doing. Step 3 then adds a cultural mode only where the subject has one; a fiction or any piece with no cultural locus takes its colour from the score shelf alone.
   - **Where Route C hands on.** Step 6 does not run, so the cue map is handed at Step 5: where each cue enters, what it does, and where it gets out of the narration's way goes to **Phase 3** under `decisions` in `project.yaml` as `score_cue_map` (a path), and `timing_map` stays null on this route — a cue map is not a beat grid and is not the clock. **Where Phase 4's measured voice sets the runtime, the shot table follows the voice and the cue map is advisory:** Phase 3 reads it to know where the music sits, and the cues are fitted to the cut in the edit, never the cut to the cues. The stems go to the edit.
   - **Step 3 is not optional on a heritage or culturally located subject.** It is *Cultural & Genre Heritage Infusion*, and it is where the mode and the instruments come from — the maqam cards, the oud, santur and joza. On a Mesopotamian subject that is not decoration, it is the entire instrumentation answer, and a score written without it defaults to generic orchestral, which is the commonest failure of this route. **On a history piece the user wants realistic**, the instruments keep to the period: where the canon dates an instrument later than the piece, the sound heard inside the scene keeps to that boundary the way the image would, and the score does too — found in the canon, used; not found, searched; nothing found, the closest period sound, noted under `decisions`. **On any other piece** — a contemporary retelling, a stylised animation, an advert that only borrows the colour — the score takes whatever serves it and the choice goes under `decisions`. Whatever the project itself has put on its own list in `FORBIDDEN-GLOBAL.md` §1 is kept on every piece ("appear" includes what is heard). This route used to list Steps 1, 2 and 5 and send a heritage score straight past the only step carrying its musicology.
   - **Step 1 is read for form only on this route.** It is *Song Architecture & Metric Scansion*, and half of it — metric scansion, open-vowel belting, singability — is about fitting words to notes, which a cue with no singer does not have. What Step 1 gives a score is shape: **through-composed (`lyric.through_composed`) is the normal answer for a cue**, because a score follows the film's structure rather than a verse-chorus one. Take the form, skip the scansion.

4. **Route D: Music that already exists, which this phase did not make.** A recorded performance, a
   commissioned composer's cue, a licensed track, a piece of liturgical chant sung live. **Nothing is
   generated here and the phase still runs**, because the decisions it owns are still live: which
   piece goes where, what it is doing to the scene, where it enters and gets out of the way, and —
   the part only this phase knows — **what the music actually is**, named correctly. Run **Step 3**
   for the cultural and repertoire questions and **Step 6** for the timing map, and skip the
   generation steps entirely. The timing comes from the recording, measured, and until it exists the
   cells read `pending_measured_duration`.
   - **Naming it correctly is not a formality on culturally located material.** The repertoire cards
     in [`assyrian-syriac-music-craft.md`](./assyrian-syriac-music-craft.md) distinguish traditions
     that look alike from outside and are not — the East Syriac Ḥudra and the West Syriac Beth Gazo
     are different books of different churches. Getting that wrong in a caption is the kind of error
     the audience it was made for notices immediately and nobody else notices at all.
   - **And it gets its credit.** A recording or a composition the project did not make is credited by
     name, performer and source. Where the source is not known, search, take the closest attribution,
     note it under `decisions` (with `pending_archive_source` travelling in the handoff if it still wants
     confirming) and continue. There is no rights or clearance step here (root [`SKILL.md`](../../SKILL.md) §0).

**A note on what this phase needs from upstream.** The music-video route starts here, but the format kits in [`formats-music.md`](./formats-music.md) rank cards that live in Phase 1 and Phase 2 — structure, theme, endings, subtext — and each one carries its path. A music video with no story spine behind it is where the "illustrating the lyric line by line" failure comes from. Spend ten minutes in Phase 1 on the spine before writing the lyric; the route skips the *deliverables* of Phases 1 and 2, not their craft.

---

## 2. The 6-Step Song Production Protocol

### Step 1: Song Architecture & Metric Scansion
Select the song form based on narrative requirements:
- **Verse-Chorus-Bridge Spine (`lyric.verse_chorus_bridge`)**: Modern pop/commercial standard.
- **AABA 32-Bar Form (`lyric.aaba_form`)**: Intimate jazz, soul, or character-driven ballads.
- **Through-Composed (`lyric.through_composed`)**: Continuous cinematic journeys with no repeated choruses.
- Apply **Metric Scansion (`rhyme.syllable_count_balance`)** and **Open Vowel Belting (`rhyme.open_vowel_high_belts`)** to guarantee natural singability.

### Step 2: Generative Engine Selection & Directing
Direct the chosen generative AI music engine using exact technical parameters. **The brief names the engine; where it names none, choose the one that fits the piece** — Suno for a tag-directed song with your own lyric, Lyria 3.5 for a prose-directed cue or where the Gemini app is the surface — search its current documentation, record the choice under `decisions`, and write for it. The lyric and the musical description are the same whichever engine takes them; only the tags and the field layout below change:
- **Suno v6 (`suno.v6_engine_architecture` for the release render on v6, `suno.v55_fast_iteration` for drafts on v6-mini)** — Suno's models, fields, tags and vendor facts live on the `suno.` cards in [`suno-engine-craft.md`](suno-engine-craft.md), each with its official source and date:
  - Enclose every section in Suno's structure tags in the Lyrics field (`suno.structural_metatags` lists the ones Suno documents); chorus-lift modifiers such as [Power Chorus] are community practice that Suno does not document (`suno.dynamic_energy_chorus`).
  - Use precise instrumentation styling in the Styles field (`suno.style_prompt_formula`) and exclusions in the Exclude field (`suno.negative_style_tags`), with solo sections placed per `suno.instrumental_solo_tags`.
  - Prevent repetitive lyrical hallucination (`suno.hallucination_prevention`).
- **Google DeepMind Lyria 3.5, in the Gemini app first (`lyria.foundational_architecture`)** — its surfaces, lengths, limits and syntax are on its cards in [`gemini-lyria-engine-craft.md`](gemini-lyria-engine-craft.md), each with its official source and date:
  - Write the prompt in Google's order, primary genre first, with your own lyrics under `Lyrics:` and section tags (`lyria.semantic_natural_prompting`, `lyria.syllable_timing_sync`).
  - Direct semantic mood and expressive rubato in words (`lyria.controllable_tempo_curves`).
  - Command the microtonal and modal pitch in the prompt, and check the take by ear, since Google documents no microtonal control (`score.microtonal_quarter_tone_tension`).
  - Lyria 3.5 returns no stems, so separate afterwards (`lyria.native_multitrack_stems`, `song_handoff.stem_separation_protocol`).

### The Song Engine Record — What Phase 5 Needs Written Down

The package keeps its model numbers in one file, [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md), dated,
so that a limit which moves every few months is never baked into a craft guide. Its picture block
records image and video engines — native generation tile by aspect, maximum clip length, frame
rate, whether a start or end frame is accepted — and its audio blocks record voice and music engines.

**Phase 5 needs one number that only the song engine record supplies: what a song engine actually returns, and
at what length.** Everything this phase hands to Phase 3 and Phase 6 stands on it. A verse-chorus-bridge spine
written for 3:10 is a different song from one written for an engine that returns 2:00 and extends in
chunks, and the timing map in Step 6 cannot be trusted at all until the length is a measured fact
rather than a plan.

**The block itself is `SONG ENGINE RECORD` in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) §2**, beside the
audio fields, and it is not repeated here: copy it from there into the project folder and fill it,
per project.

**What to do when it has not been filled — and the answer is not to stop.** The same rule that
governs a missing image record governs this one: nothing is left out and nothing is redesigned.

- **The lyric is written in full.** Every section, every line, at the metre chosen in Step 1. A
  lyric is not shortened to fit a length nobody has measured.
- **The style prompt is written in full.** Genre, instrumentation, tempo, vocal character, the
  structural metatags — all of it, exactly as it would be written for an engine whose limits are
  known.
- **The timing map is marked provisional.** Every cell in the Step 6 blueprint that depends on a
  length the record owns carries the marker rather than a guess:

```
song_length:   pending_engine_check
section_map:   pending_measured_duration (planning grid at ___ BPM; free-rhythm song such as a mawal: planning grid by phrase, ___ s per phrase)
```

  and the marker travels with the handoff, so Phase 3 and Phase 6 see immediately which cells are still open.
  An unfilled cell is a visible gap that costs a minute to close. A guessed one is an invisible gap
  that costs a re-render of every shot cut to it.

- **The map stays provisional until the rendered track is measured.** Not until the engine's
  documentation is read, not until the generation is queued — until the returned audio file exists
  and has been measured. `song_handoff.locked_audio_measurement` is the card that says so, and the
  same rule holds here as in Phase 4: the arithmetic is an estimate and the waveform is the fact.

And the rule in [§4 of ENGINE-CHECK.md](../ENGINE-CHECK.md#4-the-rule-that-governs-all-of-this) applies unchanged: **a limit is a reason to change the
engine, not the song.** If the record comes back and the engine cannot return the length the piece
needs, find one that can, or plan the extension deliberately with its seam on a bar line. What must
never happen is a song quietly shortened around a machine, because nobody downstream can see the
verse that was never written.

---

### Step 3: Cultural & Genre Heritage Infusion
Inject deep heritage musicology when required:
- **Mesopotamian & Iraqi Maqam (`maqam.bayati_river_mode`, `maqam.hijaz_desert_majesty`, `maqam.iraqi_mawal_improvisation`)**: Utilize authentic quarter-tone maqamat, free-meter Mawal vocal intros, and acoustic Oud/Santur/Joza arrangements. For a bright Arabic children's melody meant to be sung back, `maqam.ajam_bright_major_mode`.
- **Assyrian & Syriac Traditions (`assyrian.khigga_dance_rhythm`, `assyrian.sheikhani_martial_rhythm`, `assyrian.beth_gazo_eight_modes`, `assyrian_exp.mamer_mountain_dance`)**: Direct authentic folk dance meters (Khigga, Sheikhani, Bagiyeh, Mamer, Tolama), liturgical Beth Gazo cadences, and piercing Zurna/Davula acoustic dynamics.
- **Ancient Mesopotamian music (before 330 BC) — the empire, not the living tradition**: the `assyrian.` and `assyrian_exp.` shelves are modern folk and Syriac liturgy, so the period instruments come from the canon — for Neo-Assyria, [`grimoire-16-neo-assyrian.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/grimoire-16-neo-assyrian.md) heading 6, its Music bullet (harps, lyres, lutes, drums, cymbals, double pipes) — and the mode from the deep-antiquity value of `maqam.era_before_mode`.
- **Film score with no cultural locus** — fiction, fantasy, drama, any cue whose colour is orchestral, chamber or electronic rather than a tradition's: the score shelf, [`../phase-04-audio-narration/score-composition-dynamics.md`](../phase-04-audio-narration/score-composition-dynamics.md), from its head card `score.span_before_the_sound`.
- **Modern Genre Blueprints (`genre.hyperpop_glitch_maximalism`, `genre.synthwave_outrun_retrofuturism_blueprint`, `genre.drill_sub_glide_syncopation`, `genre.afrobeats_log_drum_groove`)**: Deploy industry-standard tempo grids, sub-bass design, and rhythmic pockets across 25 contemporary styles. A song that teaches takes its tempo from `genre.kids_teaching_tempo`.

### Step 4: Hook Psychology & Dopamine Engineering
Maximize memorability and viral retention:
- Structure the main hook around the **Earworm Interval Contour (`hook_psych.earworm_interval_contour`)**.
- Inject a secondary **Post-Chorus Ear Candy Loop (`hook_psych.the_post_chorus_earcandy_loop`)**.
- Build tension using the **Cognitive Anticipation & Delayed Payoff (`hook_psych.cognitive_anticipation_payoff`)** and **Sudden Silence Punch Drop (`hook_psych.sudden_silence_punch_drop`)**.
- **On children's work this step answers to the kids shelf.** Its frightened-or-agitated set (`kids.gentle_moves`, `kids.no_fast_cuts` and the rest of that row in [`../phase-03-shooting-script/kids-content.md`](../phase-03-shooting-script/kids-content.md)) is obeyed, not chosen, and outranks every device above: judge a punch drop against it, and where the silence would startle rather than delight, take the card's own `Yields to:`.
- **A song inside the story takes this step only as far as the story wants it polished** (Route B): one meant to sound unperformed — sung under the breath, off a worn cassette — keeps none of the devices above, and the agent records that choice under `decisions`.

### Step 5: Stem Isolation & Handoff to the Edit
Separate the generative output and hand it over; the mix and the master are made in the edit, by hand, against the actual material.
- Separate generated audio into 4-to-6 clean stems: Vocals, Drums/Percussion, Bass, Harmony/Pads, and Lead Instruments (`song_handoff.stem_separation_protocol`, `sync.sync_stems_deliverables_package`). Deliver them unmastered, with headroom intact.
- **Done here, because it shapes what gets generated:** write the cue with a hole in it where the voice goes — mids thinned, percussion dropped, leads out of the speech register (`sync.instrumental_break_dialogue_window`). A cue built this way needs almost nothing from the mixer; one built without it cannot be rescued.
- **Named here, set in the edit:** which loudness standard the destination enforces (`sync.broadcast_lufs_sync_mastering`, `song_handoff.platform_loudness_mastering`), and where a dialogue window opens in the song (`song_handoff.dialogue_insertion_ducking`). The figures behind both are looked up and dialled at master time.

### Step 6: Locked Audio Timing Map & the Phase 3 / Phase 6 Bridge
If proceeding to a Music Video:
- Generate a sample-accurate **Time-Coded Song Blueprint (`song_handoff.locked_audio_measurement`)**.
- Map downbeats, chorus hits, bridge pivots, and reverb tails into an EDL/CSV cue sheet (`song_handoff.beat_grid_detection`, `song_handoff.music_video_bridge_phase_6`).
- Hand off the timing grid to **Phase 3 (the shot table), then Phase 6: Storyboard Layout**, locking shot lengths to musical measures.
- **Nothing here is locked until the returned track has been measured.** If the song engine record is
  unfilled — see *The Song Engine Record* above — the blueprint still gets written, and every cell
  that depends on the track's length carries `pending_measured_duration`, with the planning BPM (on a free-rhythm song, the planning phrase lengths) beside it, rather than a guess.
  Phase 3 and Phase 6 can cut to a provisional grid; it cannot recover from a grid that was guessed and looked
  measured.

---

<!-- GENERATED:module-catalog — do not edit by hand. Generated in the source package -->

## The craft files in this phase - 16 files, 340 cards

Generated from the cards, so a file whose cards change scope changes here too. The same table with the full card lists is in [`INDEX.md`](./INDEX.md); the searchable id table is in [`LOOKUP.md`](./LOOKUP.md).

| File | What it covers | Cards scoped to | Cards |
| :--- | :--- | :--- | ---: |
| [`cat-lyric.md`](cat-lyric.md) | **Lyric, Verse, Refrain and Song Structure** — Lyric Architecture & Form (Part 1) | mostly musical theatre, kids song, song lyric, single, among 32 formats | 32 |
| [`cat-lyric-2.md`](cat-lyric-2.md) | **Lyric, Verse, Refrain and Song Structure — Part 2** — Lyric Form & Sound Craft (Part 2) | mostly Song Lyric, Musical Theatre, Live Event, Animation Feature, among 28 formats | 34 |
| [`cat-lyric-3.md`](cat-lyric-3.md) | **Lyric, Verse, Refrain and Song Structure — Part 3** — Lyric Advanced Form & Voice (Part 3) | mostly Live Event, Audio Drama, Feature Film, Podcast, among 19 formats | 10 |
| [`cat-lyric-4.md`](cat-lyric-4.md) | **Lyric, Verse, Refrain and Song Structure — Part 4** — Lyric Genre Refinements (Part 4) | mostly Essay, Memoir, Poetry, Prose Poem, among 5 formats | 1 |
| [`lyric-craft.md`](lyric-craft.md) | **Lyric Craft & Song-to-Visual Architecture** — Lyric Mechanics & Meter Dynamics | mostly Song Lyric, Music Video, Ballad, Children's Song, among 16 formats | 8 |
| [`suno-engine-craft.md`](suno-engine-craft.md) | **Tag-and-Style Song Engine Craft** — Tag-and-Style Song Engine (written for Suno) | any format | 19 |
| [`gemini-lyria-engine-craft.md`](gemini-lyria-engine-craft.md) | **Google Lyria 3.5 Engine Craft** — Google Lyria 3.5 Engine Craft: the Gemini app first, with ready-to-paste prompts | any format | 14 |
| [`assyrian-syriac-music-craft.md`](assyrian-syriac-music-craft.md) | **Assyrian & Syriac Songcraft, Rhythms & Liturgical Heritage** — Assyrian & Syriac Folk & Liturgical Suite | any format | 22 |
| [`mesopotamian-arabic-maqam-craft.md`](mesopotamian-arabic-maqam-craft.md) | **Mesopotamian & Arabic Maqam Craft & Poetic Forms** — Mesopotamian & Iraqi Maqam Heritage | any format | 25 |
| [`song-stems-and-timing-handoff.md`](song-stems-and-timing-handoff.md) | **Song Stems, Locked Audio Timing & Video Handoff** — Song Stems, Timing Grid & Phase 3 / Phase 6 Handoff | any format | 18 |
| [`rhyme-prosody-phonetics.md`](rhyme-prosody-phonetics.md) | **Songwriting Rhyme Schemes, Prosody & Vocal Phonetics** — Rhyme Schemes, Prosody & Vocal Phonetics | any format | 26 |
| [`vocal-arrangement-harmonies.md`](vocal-arrangement-harmonies.md) | **Vocal Arrangement, Choral Textures & Multi-Part Harmonies** — Vocal Arrangement & Multi-Part Harmonies | mostly Epic Anthem, Musical Theatre, Art Song, Film Soundtrack, among 67 formats | 26 |
| [`assyrian-syriac-expanded.md`](assyrian-syriac-expanded.md) | **Assyrian & Syriac Expanded Folk, Epic & Classical Traditions** — Assyrian & Syriac Expanded Folk & Epics | any format | 26 |
| [`modern-genre-production-blueprints.md`](modern-genre-production-blueprints.md) | **Modern Genre Production Blueprints** — Modern Genre Production Blueprints | any format | 27 |
| [`songwriting-psychology-hooks.md`](songwriting-psychology-hooks.md) | **Songwriting Psychology and Catchy Hooks** — Songwriting Psychology & Catchy Hooks | any format | 26 |
| [`commercial-sync-music-supervision.md`](commercial-sync-music-supervision.md) | **Commercial Sync and Music Supervision** — Commercial Sync & Music Supervision | mostly Broadcast Bumper, Film/TV Post-Production Deliverable, Movie Trailer, TV Promo, among 78 formats | 26 |

<!-- /GENERATED:module-catalog -->

