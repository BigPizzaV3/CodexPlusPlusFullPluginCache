# Multilingual Dubbing, Lip-Sync & Localization Craft

21 cards. Advanced localization engineering for AI video: syllable expansion ratios, bilabial mouth shape synchronization, voice cloning cross-lingual consistency, and cultural idioms.

---

### The Mouth Is the Only Fork

**Also called:** the dubbing selector, the mouth question, what the camera can see of the mouth
**What it is:** The card at the head of the `dubbing.` shelf, and the first thing it has to say is what the shelf actually is. **Most of this family is not a set of alternatives. It is a procedure.** *Lock the name ledger before a line is written*, *clean the archival source before it is cloned*, *export the voice track dry before the lip-sync model sees it* — those are steps, done in order, by whoever is doing them, and a handover is not a choice. Only a small number of these cards fork at all, every one of them on the same subject, and this card maps those and names the rest as the ordered block they are. The two questions were read off the shelf's `Yields to:` conditions and its `Avoid when:` lines. Every card cited here is cited by id.
**Effect on the audience:** None. This card is never heard. It exists so that the one real decision on this shelf — what the camera can see of the mouth, and whether that mouth is one the closure rules can describe — is made before the line is written, rather than discovered at the lip-sync pass when the translation is already locked.
**Used for and where it works best:** Ask the two questions **per shot, not per project**, before the localized line is written. The first eliminates almost everything: a line landing on a mouth the camera is watching is a different craft problem from a line landing anywhere else, and the difference is a rewrite, not a setting. The second is anatomy and it is asked once per character. **Then run the procedural block in its stated order**, which is what the rest of the shelf is. A selector that pretended those were options would be offering a choice where the work has none.
**Best in:** formats: All localized and dubbed video | genres: All
**Avoid when:** **The shot you need does not exist.** Both of the off-the-mouth answers below assume there is somewhere to put the line — a reaction, a wide, a turned head — and when the sequence is an unbroken close-up there is no third value and this map has nothing to offer. There the answer is upstream, in the rewrite that makes the line shorter, and nothing on this shelf routes you to it. **Also distrust this map on anything that is read rather than heard**: the subtitle card's own fork leaves the shelf entirely, and every figure it governs belongs to a destination rather than to a mouth. And **do not read the procedural block as a ranking** — it is an order, and skipping a step in it is not a stylistic choice, it is a step skipped.
**Example:** `[Selector — produces no handover note. It returns card ids. The chosen card carries the note.]`

---

**The axes**

**Axis 1 — Where does the localized line have to land: on a mouth the camera is watching, on a mouth it is not, or on the screen as text?**
Asked first because every fork on this shelf turns on it and nothing else does. The conditions are on the cards and they say the same thing three times over: *"The line must land on a tight close-up of moving lips"* (`dubbing.off_screen_dialogue_freedom`), *"Tight front-facing close-up, mouth fully visible"* (`dubbing.wild_line_ambiguous_visuals`), *"Singing, or a close-up on the mouth"* — that one from another phase entirely, routing inward. And the negative case is stated as plainly: *"Forcing an intricate cultural explanation into a tight one-second extreme close-up of moving lips"* (`dubbing.off_screen_dialogue_freedom`), *"Tight direct front-facing close-up shots"* (`dubbing.wild_line_ambiguous_visuals`). The third value is not a mouth at all: it is the written channel, where the constraint is a reading rate and a line length rather than a closure.

**Axis 2 — Is this a mouth the closure rules can describe?**
Asked second and asked once per character, not per shot. *"The mouth has no lips: beak, hinged jaw, mask, machine"* (`dubbing.bilabial_lipsync_alignment`), *"The character has an ordinary human mouth"* (`dubbing.lipsync_no_lips`), *"The singing character has a beak or a rigid jaw"* — again from another phase, routing inward. This is the only axis on the shelf that is about the subject rather than the shot, and it **inverts the first one's craft rather than refining it**: on a lipped face the closures are the moments you must hit, and on a beak or a rigid jaw they are the moments that cannot be shown at all, so a line whose meaning sits on them will not read whatever you do to the timing.

---

**The map**

**Axis 1 — where the line has to land**

| Answer | The shortlist, by id |
| :--- | :--- |
| **On a mouth the camera is watching — front-facing, close, lips or aperture visible** | `dubbing.bilabial_lipsync_alignment` · `dubbing.lipsync_no_lips` |
| **On a mouth the camera is not watching — off-screen, in profile, turned away, wide, in shadow, in a crowd** | `dubbing.off_screen_dialogue_freedom` · `dubbing.wild_line_ambiguous_visuals` |
| **Not in a mouth at all — the line is read rather than heard** | `dubbing.subtitle_vs_spoken_rate` · `dubbing.arabic_subtitle_rate` |

**Axis 2 — is it a mouth the closure rules can describe**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Lips, and the closures are visible** | `dubbing.bilabial_lipsync_alignment` · `dubbing.off_screen_dialogue_freedom` · `dubbing.wild_line_ambiguous_visuals` |
| **No lips — a beak, a hinged jaw, a mask, a helmet, an animal, a machine** | `dubbing.lipsync_no_lips` |
| **The question does not arise — nothing is being matched to a mouth** | `dubbing.subtitle_vs_spoken_rate` · `dubbing.arabic_subtitle_rate` |

*The answer is the intersection of the two shortlists and it is normally one card. That is not a weakness of the map; it is the size of the decision.*

**And the rest of the shelf, which is not a map.** These carry no fork — twelve of them filed `execution-note`, one `format-exclusion`, one `companion-only` — and they are given here in the order the work does them, because that is the only ordering they have:

| Stage | The cards, by id |
| :--- | :--- |
| **Before a word is translated** — settled once, at project setup | `dubbing.multilingual_naming_consistency` · `dubbing.arabic_english_syllable_ratio` · `dubbing.cultural_idiom_localization` · `dubbing.fusha_vs_dialect_cadence` |
| **Casting and building the voice** — settled once per character | `dubbing.cross_lingual_timbre_locking` · `dubbing.pitch_profile_alignment` · `dubbing.formant_shifting_calibration` · `dubbing.emotional_congruence_dub` |
| **Preparing the audio for the engine** — run per source file | `dubbing.lipsync_audio_hygiene` · `dubbing.archival_voice_pre_translation` · `dubbing.automated_studio_pipeline` |
| **On the timeline, and at delivery** — run per sequence | `dubbing.visual_breath_sync` · `dubbing.lip_flap_tolerance_window` · `dubbing.dual_language_parallel_release_architecture` |

**None of these is an alternative to any other. Choosing between them is not a thing the work ever asks.**

---

**The default, and the one against it**

**The default is `dubbing.bilabial_lipsync_alignment`, and it is measured rather than asserted.** It is the target of four inbound edges, three from this shelf and one from another phase, and — this is the test that matters — **the conditions behind them are not one condition repeated.** *The line must land on a tight close-up of moving lips.* *The shot is front-facing and the mouth is fully visible.* *The character has an ordinary human mouth.* *The line is sung, or the camera is on the mouth.* Two of those are framing, one is anatomy, one is performance. **Three distinct conditions behind four edges** is a fallback. Set against it, `dubbing.lipsync_no_lips` takes two inbound edges and both fire on the identical condition — *no lips* — which makes it an escape hatch for a subject the rest of the shelf cannot describe, not a second default. Counting edges would have made them look comparable; counting conditions separates them cleanly.

**The one against it is `dubbing.off_screen_dialogue_freedom`.** Every other forking card on this shelf takes the shot as given and bends the audio to it — align the closure, neutralise the vowels, match the aperture, hold the drift inside a window. This is the only one that refuses the problem instead of solving it: it moves the line to a shot where there is no mouth to fight, and comes back with the translation it actually wanted rather than the translation that fitted. **On Arabic that is not a luxury, it is the structural fix**, because the shelf's own first procedural card records that the translated line runs longer than the original and a mouth that was timed to English has nowhere to put the difference. The cost is stated and it is real — it needs a cutaway that has to exist, and on a single unbroken close-up it does not — but on a documentary, a heritage series or any piece with B-roll, it always does. Its near cousin against the grain is `dubbing.wild_line_ambiguous_visuals`, which does the same trick one step earlier, at the script, by choosing which shot the difficult sentence will be written for.

---

**The unasked**

**All but two cards on this shelf are the target of no `Yields to:` field anywhere in the package.** Only `dubbing.bilabial_lipsync_alignment` and `dubbing.lipsync_no_lips` are ever routed to. Everything else can be chosen and nothing sends you there.

**And the shape of that list is the finding.** Most of it is expected and means nothing: **nothing routes to a procedure**, so the fourteen cards of the block above were never going to appear, and their absence from the graph is correct rather than a gap. But one card on the unasked list is not a procedure and should not be there: `dubbing.subtitle_vs_spoken_rate`. That card states in its own body that it **owns the subtitle line length for the whole package**, and that any other file needing it cites it by id instead of restating a number. **The package's most deferred-to card on this shelf looks, in the pair graph, like an orphan** — because the pair field records *alternatives*, and it has no way at all to say *this one is the authority and the others must cite it*. An ownership edge and an alternative edge are different relations, and only one of them has a field. Any map built purely on inbound edges would file the shelf's single most load-bearing card as unreachable.

The second thing the list shows: **the shelf forks on the mouth and on nothing else, and the commonest failure in the work it describes is not about the mouth.** The line that will not fit is. Every one of the off-the-mouth answers assumes a hiding place exists; when the sequence is an unbroken close-up and the Arabic runs long, the shelf has no card. The nearest thing that exists is the syllable-expansion card, which is filed as procedure, is settled at the top of the project, and offers a rewrite for conciseness that nothing routes a reader to at the moment they need it. **The card this shelf wants is the one that says: the line does not fit, there is no cutaway, and here is what you cut.**

`dubbing.the_mouth_is_the_only_fork`

---

### Arabic-to-English Syllable Expansion Ratio

**Also called:** translation duration stretch, syllable compensation factor  
**What it is:** Calibrating script duration for the natural 15% to 20% syllable length expansion when translating English into Classical or Modern Arabic.  
**Effect on the audience:** Prevents rushed, frantic Arabic voiceover crammed into English shot lengths, or awkward empty visual holds in English cuts.  
**Used for and where it works best:** Pre-scripting bilingual releases (Arabic/English) for historical documentaries and heritage series.  
**Best in:** formats: Documentary Feature, Vertical Short-Form, Heritage Series | genres: Heritage (civilisation-focused), History  
**Avoid when:** Forcing Arabic translation to match English word counts 1:1 without rewriting for conciseness.  
**Example:** `formula: English_words * 0.82 = Target_Arabic_words to guarantee identical spoken airtime.`  
`dubbing.arabic_english_syllable_ratio`

---

### Bilabial Consonant Lip-Sync Alignment

**Also called:** M-B-P mouth closure alignment, visual sync markers  
**What it is:** Aligning bilabial consonants (M, B, P) in the audio track to exact video frames where the on-screen character's lips are visibly closed.  
**Effect on the audience:** Convinces the human subconscious that the character is truly speaking the words, eliminating uncanny valley skepticism.  
**Used for and where it works best:** Pre-processing audio for AI lip-sync models (SyncLabs, HeyGen, LivePortrait, Runway).  
**Best in:** formats: Film Dubbing, Cinematic Animation, AI Avatar | genres: All  
**Avoid when:** Shifting audio tracks so that an 'M' sound plays over a wide open mouth visual.  
**Example:** `sync_spec: Frame 42: actor lips shut -> Audio: line starts with "Babylon" exactly on frame 42.`  
**Yields to:** `dubbing.lipsync_no_lips` — The mouth has no lips: beak, hinged jaw, mask, machine.  
`dubbing.bilabial_lipsync_alignment`

---

### Cross-Lingual Voice Clone Timbre Locking

**Also called:** multilingual voice identity preservation, universal clone  
**What it is:** Maintaining the identical fundamental vocal frequency, chest resonance, and personality timbre across multiple target languages using ElevenLabs.  
**Effect on the audience:** The global audience experiences the same actor's authentic voice whether watching in English, Arabic, Spanish, or French.  
**Used for and where it works best:** Global documentary releases, international celebrity avatars, and historical figure reconstructions.  
**Best in:** formats: Global Series, International Feature | genres: All  
**Avoid when:** Switching to a generic default foreign voice model that sounds nothing like the original character. And before any of this: cloning the voice of a real person, living or recorded long ago, waits at the cloning step alone for that person's consent, or the consent of whoever can speak for them, recorded with their name and the date in `project.yaml` (root SKILL.md §0); everything else in the work carries on.  
**Example:** `clone_spec: voice_id locked across EN, AR, and FR pipelines; steadiness: medium, likeness to the source voice: high (the engine's own settings are in its adapter in ENGINE-CHECK.md §7).`  
`dubbing.cross_lingual_timbre_locking`

---

### Classical Arabic (Fusha) Cadence vs Dialects

**Also called:** Fusha register calibration, dialectal authenticity  
**What it is:** Consciously choosing between elevated Classical Arabic (Fusha) for monumental imperial history and Mesopotamian Iraqi dialect for folklore.  
**Effect on the audience:** Fusha communicates royal majesty, religious gravitas, and pan-Arab authority; Iraqi dialect brings intimate ancestral warmth.  
**Used for and where it works best:** King decrees in Fusha; folk tales of the southern marshes in authentic Iraqi/Mesopotamian vernacular.  
**Best in:** formats: Heritage Documentary, Cultural Feature | genres: Heritage (civilisation-focused), History, Folklore  
**Avoid when:** Mixing street slang into a solemn 7th-century BC Assyrian royal proclamation.  
**Example:** `casting_rule: Imperial decrees: Fusha with pristine I'rab; Oral folklore: Southern Iraqi rural dialect.`  
`dubbing.fusha_vs_dialect_cadence`

---

### Subtitle Reading Speed vs Spoken Rate

**Also called:** CPS limit, subtitle duration constraint, 17-char rule  
**What it is:** Limiting on-screen subtitles to a reading-rate ceiling and a line length. **This card owns the subtitle line length for the whole package**; the reading rate is owned by `tens.subtitle_preempt`, and the Arabic figures by `dubbing.arabic_subtitle_rate`. Where another file needs a line length, it cites this id rather than restating a number. The line length depends on the destination and is the value most often written from memory: **42 characters is the common streaming maximum, 37 the stricter broadcast convention**, and a piece takes the one its destination actually enforces. Reading rate is the platform's current figure — see `tens.subtitle_preempt` for why that number moves and why the platform's own page is the only safe source. **Arabic is the one language with its own card:** Netflix's published Arabic reading rates, line length and line count, with the guide's version date, are on `dubbing.arabic_subtitle_rate`, and a file that needs an Arabic figure cites that id. **These numbers govern how much text and for how long; none of them is a size.** How large the type actually is, as a fraction of frame height, is a separate decision and it is owned by `textimg.subtitle_size_in_frame` in Phase 7 - a cue that obeys every figure here is still unreadable if it is set too small for the screen it lands on.  
**Effect on the audience:** Allows viewers to read comfortably without their eyes being glued to the bottom of the screen, preserving visual engagement.  
**Used for and where it works best:** All bilingual and localized video deliveries.  
**Best in:** formats: All subtitled video | genres: All  
**Avoid when:** Cramming three lines of 50 characters each on screen for a 1.5-second fast spoken line.  
**Example:** `subtitle_limit: Max 2 lines; Max 37 chars/line; Minimum duration 1.2s; Maximum CPS: the destination's current figure, from its own page (`tens.subtitle_preempt`).`  
**Source:** reference — the 42-character streaming and 37-character broadcast line lengths are the Netflix and BBC figures `tens.subtitle_preempt` names; the 1.2 s minimum duration in the example is an assumption, untested  
**Yields to:** `textimg.subtitling_a_sung_line` — The line is sung, so reading-rate rules do not transfer.  
`dubbing.subtitle_vs_spoken_rate`


### Arabic Subtitle Reading Rate and Line Length

**Also called:** Arabic CPS, Arabic subtitle limits, the Netflix Arabic figures  
**What it is:** The published limits for an Arabic subtitle, from the only Arabic-specific guide this package has found: Netflix's Arabic Timed Text Style Guide, whose latest change-log entry is 2025-12-19. **Reading speed: up to 20 characters per second for adult programs and up to 17 for children's programs. Line length: 42 characters per line. Lines: two at most**, and ideally one — the guide keeps text to one line unless it exceeds the character limit, and recommends bottom-heavy pyramid subtitles when a second line is needed. At those ceilings a full 42-character line needs 2.1 seconds on screen for adults and about 2.5 for children, and a full two-line cue of 84 characters needs 4.2 and about 4.9. **This card owns the Arabic subtitle figures for the package**, and `dubbing.subtitle_vs_spoken_rate` owns the general rule and everything this card does not state. **The destination's own current guide governs**: these are Netflix's figures for Netflix, and a broadcaster, festival or platform with an Arabic guide of its own is timed to that guide. Where the destination publishes nothing for Arabic — a burned subtitle on a page's own reel — these are the published figures to plan against, named as Netflix's and not as a standard.  
**Effect on the audience:** An Arabic viewer who finishes every cue before it leaves the screen, and keeps their eyes on the picture instead of chasing the text.  
**Used for and where it works best:** Any Arabic subtitle: an English voiceover with burned Arabic subtitles, an Arabic translation track, a children's piece subtitled in Arabic. Time each cue against the ceiling for its audience — the children's figure for anything made for children. Break a two-line cue where `rhythm.arabic_rtl_rhythm` says, at the syntactic joint, and never simply at the 42nd character. On a vertical piece `vertical.text_safe_zone` keeps Arabic to one centred line, which is also the guide's own preference; how large the line is set is `textimg.subtitle_size_in_frame`'s decision, not this card's.  
**Best in:** formats: All subtitled video, Documentary Series, Heritage Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Feature Film | genres: All  
**Avoid when:** The subtitle is not Arabic: other languages have their own figures, and the general rule is on `dubbing.subtitle_vs_spoken_rate`. Do not treat a ceiling as a target — 20 characters per second is the most the guide allows for adults, not a pace to fill, and a cue that can be shorter is shorter. And do not quote these figures without the guide's name and version beside them: a number that has lost its source cannot be re-checked, and the next copy of it will be wrong.  
**Example:** `subtitle_limit (Arabic, adult): max 2 lines, one preferred; max 42 chars/line; max 20 CPS (children's programs: 17); a full 42-character line holds at least 2.1s; the destination's own current guide overrides every figure here.`  
**Source:** reference — Netflix Partner Help Center, "Arabic Timed Text Style Guide" (partnerhelp.netflixstudios.com/hc/en-us/articles/215517947-Arabic-Timed-Text-Style-Guide): section 4, Character Limitation; section 15, Reading Speed Limits; and the Line Treatment and Line Breaks section. Latest change-log entry 2025-12-19, and the reading-speed and line-length sections are not in that entry's change list; read 2026-09-23. The seconds-per-line figures are this card's arithmetic  
**Shelf life:** dated — review 2027-03. A platform's style guide is revised on the platform's schedule; its change log is the thing to check.  
**Yields to:** `dubbing.subtitle_vs_spoken_rate` — the subtitle is not Arabic, or the question is one this card does not state, such as the minimum cue duration: that card owns the general rule. `rhythm.arabic_rtl_rhythm` — where an Arabic cue breaks: at the syntactic joint that card names, not at the character count. `textimg.subtitling_a_sung_line` — the line is sung, so reading-rate rules do not transfer.  
`dubbing.arabic_subtitle_rate`
---

### Lip-Sync Audio Pre-Processing Hygiene

**Also called:** clean audio for video models, lip-sync source prep  
**What it is:** Exporting completely dry, ultra-clean voice tracks with zero reverb, zero delay, and zero background music before feeding to AI lip-sync models.  
**Effect on the audience:** Prevents AI lip-sync models from hallucinating weird mouth twitches caused by background instruments or room echo.  
**Used for and where it works best:** Mandatory pre-processing step before SyncLabs, HeyGen, or SadTalker API calls.  
**Best in:** formats: AI Video Generation, Automated Dubbing | genres: All  
**Avoid when:** Feeding a full music-and-dialogue mixed stereo track into a video lip-sync tool.  
**Example:** `prep_spec: 24-bit 48kHz WAV, 100% dry, gated silence between words, peak normalized to -3dBFS.`  
**Source:** assumption — the package's working prep figures, not a published standard or a lip-sync vendor's specification; check them against the chosen engine's own input requirements.  
`dubbing.lipsync_audio_hygiene`

---

### Off-Screen Dialogue Freedom Protocol

**Also called:** OS line flexibility, free translation beats  
**What it is:** Concentrating difficult localized translations and explanatory clauses on shots where the speaking character is off-screen (OS) or facing away.  
**Effect on the audience:** Enables natural, unhurried cultural explanation without being constrained by on-screen mouth flap timing.  
**Used for and where it works best:** Localizing complex historical documentaries and multi-character dramas.  
**Best in:** formats: Film Dubbing, Documentary Adaptation | genres: All  
**Avoid when:** Forcing an intricate cultural explanation into a tight 1-second extreme close-up of moving lips.  
**Example:** `editorial: Cut to reaction shot of listener or wide city vista -> insert extended 4-second Arabic translation line.`  
**Yields to:** `dubbing.bilabial_lipsync_alignment` — The line must land on a tight close-up of moving lips.  
`dubbing.off_screen_dialogue_freedom`

---

### Cultural Idiom Functional Localization

**Also called:** intent translation, idiom adaptation, dynamic equivalence  
**What it is:** Translating the emotional and psychological intent of cultural metaphors rather than literal word-for-word rendering.  
**Effect on the audience:** Connects instantly with local cultural emotions; avoids bizarre, comical literal translations that break immersion.  
**Used for and where it works best:** Translating idiomatic expressions, proverbs, and battle curses between Arabic, English, and other languages.  
**Best in:** formats: All localized media | genres: All  
**Avoid when:** Translating English slang literally into formal Arabic or vice versa.  
**Example:** `translation: English "Bite the bullet" -> Arabic "تجشّم الصعاب" or Mesopotamian "اشرب المرّ", not literal teeth on lead.`  
`dubbing.cultural_idiom_localization`

---

### Biological Breath Matching to Video

**Also called:** visual breath sync, chest inhalation alignment  
**What it is:** Synchronizing audio breath sounds exactly with the visual expansion of the on-screen actor's chest or shoulders before they speak.  
**Effect on the audience:** Cementing the illusion of physical life; the viewer perceives the voice as emerging organically from the body on screen.  
**Used for and where it works best:** High-end AI avatar animation, theatrical film dubbing, and intimate drama.  
**Best in:** formats: Feature Film, Cinematic AI Video | genres: Drama, Psychological  
**Avoid when:** Audio breath triggers while the character on screen is holding their breath or looking down.  
**Example:** `timeline: Frame 12-18: character chest rises -> Audio: [inhale sound effect] -> Frame 19: dialogue line begins.`  
`dubbing.visual_breath_sync`

---

### Pitch Profile Alignment Across Dubs

**Also called:** pitch matching, foreign voice fundamental alignment  
**What it is:** Ensuring the dubbed voice matches the fundamental vocal pitch (within ±10Hz) of the original on-screen actor (e.g. 110Hz baritone).  
**Effect on the audience:** Prevents the absurd disconnect of seeing a colossal muscular king speaking with a thin, high-pitched foreign voice.  
**Used for and where it works best:** Casting voice models for multilingual localization.  
**Best in:** formats: Film Dubbing, Series Localization | genres: All  
**Avoid when:** Assigning tenor voice models to heavy elderly characters.  
**Example:** `casting_rule: Visual: 6ft broad-shouldered warrior -> Cast: deep baritone (90Hz-120Hz fundamental) across all languages.`  
`dubbing.pitch_profile_alignment`

---

### Emotional Congruence Across Languages

**Also called:** affective matching, performance parity  
**What it is:** Matching the exact emotional energy, volume envelope, and stress markers between the original take and the translated take.  
**Effect on the audience:** Preserves director's dramatic vision; prevents a tragic mourning scene from sounding like a cheerful morning radio broadcast.  
**Used for and where it works best:** Directing generative voice models across international versions.  
**Best in:** formats: Feature Film, Drama Series, Animation | genres: All  
**Avoid when:** Allowing foreign TTS models to read high-stakes dramatic lines with flat informational inflection.  
**Example:** `parity_check: Original take has a grief crack at second 3; ensure Arabic dub model utilizes [voice cracks] at second 3.`  
`dubbing.emotional_congruence_dub`

---

### Formant Shifting for Age & Character Calibration

**Also called:** formant throat size adjustment, vocal tract tuning  
**What it is:** Shifting vocal formants up (+1 to +3 semitones for youthful/smaller throats) or down (-1 to -3 semitones for older/larger bodies).  
**Effect on the audience:** Adjusts the perceived anatomical size and age of the speaker without altering musical pitch or speaking speed.  
**Used for and where it works best:** Adapting a single voice model to play multiple distinct characters across an epic narrative.  
**Best in:** formats: Audio Drama, Animation, Multi-Character Series | genres: Fantasy, History, Drama  
**Avoid when:** Extreme formant shifts (>4 semitones) that result in cartoon chipmunk or demon monster artifacts.  
**Example:** `processing: Formant -2 semitones, pitch 0: transforms 30-year-old voice model into a 60-year-old weathered general.`  
`dubbing.formant_shifting_calibration`

---

### Lip Flap Tolerance Window

**Also called:** sync window, visual sync tolerance, frame drift limit  
**What it is:** Holding audio onset and mouth movement close enough together that the viewer stops noticing the join. **The window is not symmetric, and this card used to say it was.** Sound running *ahead* of the picture is noticed markedly sooner than sound running *behind* it, because nothing in the physical world arrives before the event that makes it: a door slams and the bang travels, so a late sound is ordinary experience and an early one is impossible. The tolerance is therefore **tighter on the lead side than on the lag side**, and a symmetric window spends its allowance in the wrong direction.  
**Effect on the audience:** Sync failure is rarely noticed as sync failure. The viewer reads it as bad acting, a cheap dub, or something indefinably wrong with the performance, which is why it survives a QC pass that a real fault would not.  
**Used for and where it works best:** Final lip-sync quality control on every dubbed sequence. **Set the two sides separately and write both numbers down**, then judge the lead side first because it is the one that breaks earliest. Check the tightest shot in the sequence, not an average one: a close-up shows a drift that a wide hides completely.  
**Best in:** formats: Film, Television, Commercial | genres: All  
**Avoid when:** A symmetric tolerance is the failure mode this card exists to name — it passes an audio lead the viewer will notice while rejecting a lag they would not. Treating one figure as governing both directions is the same error in a different dress.  
**Example:** `qc_gate: lead tolerance and lag tolerance recorded separately, lead judged first, checked on the tightest shot in the sequence.`  
**Source:** reference — **no figure is stated here on purpose.** The ±2 frames this card carried until September 2026 was trade convention with no document behind it, and it was the wrong *shape* as well as unattributed. The named broadcast recommendation for sound-to-vision timing is **ITU-R BT.1359**; take both sides of the window from it, and confirm the document and its current edition before quoting a number to a client.  
`dubbing.lip_flap_tolerance_window`

---

### Wild Line Scripting for Ambiguous Visuals

**Also called:** filler phrase dubbing, mouth-neutral lines  
**What it is:** Scripting dialogue lines using neutral, open-vowel phrasing for visual shots where the actor's mouth is partially obscured or in profile.  
**Effect on the audience:** Allows smooth narrative bridging and translation flexibility without fighting visible lip movements.  
**Used for and where it works best:** Profile shots, shadows, wide shots, and crowds.  
**Best in:** formats: Dubbed Features, Documentary Dramatizations | genres: All  
**Avoid when:** Tight direct front-facing close-up shots.  
**Example:** `line_placement: Place complex translation sentence over shot 4 (medium wide tracking shot, actor head turned 45 degrees).`  
**Yields to:** `dubbing.bilabial_lipsync_alignment` — Tight front-facing close-up, mouth fully visible.  
`dubbing.wild_line_ambiguous_visuals`

---

### ElevenLabs Dubbing Studio Integration

**Also called:** automated video dubbing pipeline, cross-language stem sync  
**What it is:** Leveraging AI dubbing workflows that automatically separate background audio, translate dialogue, and synthesize matching voice clones.  
**Effect on the audience:** Delivers rapid, high-quality international releases within hours rather than weeks of manual studio recording.  
**Used for and where it works best:** High-volume educational channels, news updates, and rapid social media international scaling.  
**Best in:** formats: Vertical Short-Form, Educational Video, Documentary Series | genres: Informational, History, News  
**Avoid when:** High-end theatrical feature films requiring bespoke human dialect coaching. And before any of this: cloning the voice of a real person, living or recorded long ago, waits at the cloning step alone for that person's consent, or the consent of whoever can speak for them, recorded with their name and the date in `project.yaml` (root SKILL.md §0); everything else in the work carries on.  
**Example:** `workflow: Ingest source MP4 -> ElevenLabs Dubbing API (target: AR) -> export isolated Arabic dialogue stem -> remux.`  
`dubbing.automated_studio_pipeline`

---

### Multilingual Character Name Consistency

**Also called:** cross-lingual naming glossary, unified translation ledger  
**What it is:** Locking the exact phonetic transliteration and spelling of all character names across all translated language packages.  
**Effect on the audience:** Prevents confusing discrepancies where a character is called one name in the English subs and another in the Arabic voiceover.  
**Used for and where it works best:** Project setup: create master bilingual name ledger before writing a single localized line.  
**Best in:** formats: All localized multi-language releases | genres: All  
**Avoid when:** Translators independently improvising different Arabic spellings for ancient Sumerian deities.  
**Example:** `ledger: Gilgamesh -> كلكامش | Enkidu -> إنكيدو | Ashurbanipal -> آشوربانيبال | Ishtar -> عشتار.`  
`dubbing.multilingual_naming_consistency`

---

### Dual-Language Parallel Release Architecture

**Also called:** bilingual simultaneous drop, multi-track audio release  
**What it is:** Structuring the master video container with multi-track audio (Track 1: English stereo; Track 2: Arabic stereo) or parallel video renders.  
**Effect on the audience:** Maximizes global reach on YouTube (via multi-language audio track feature) without splitting audience metrics across separate uploads.  
**Used for and where it works best:** YouTube documentary channels, educational platforms, and international brand releases.  
**Best in:** formats: YouTube Long-Form, Educational, Heritage | genres: All  
**Avoid when:** Creating separate low-reach channels when single-video multi-track audio is supported natively.  
**Example:** `export_spec: Master MP4 with Track 1: English (AAC 320k) | Track 2: Arabic (AAC 320k) | Subtitle stream: bilingual.`  
`dubbing.dual_language_parallel_release_architecture`

---

### Archival Voice Cleaning Before Translation

**Also called:** historical source restoration, archival pre-dub  
**What it is:** Cleaning crackles, 78 RPM record hiss, and muffled frequencies from rare historical recordings before feeding into voice cloning for translation.  
**Effect on the audience:** Produces pristine translated speech that sounds like the historical figure is speaking live today, without vintage crackle artifacts.  
**Used for and where it works best:** Historical figure AI speech recreation (e.g. recreating 1920s Iraqi poets or British archaeological pioneers).  
**Best in:** formats: Historical Documentary, Heritage Archive | genres: History, Biography  
**Avoid when:** Feeding degraded 8kHz phone recordings directly into voice cloning models. And before any of this: cloning the voice of a real person, living or recorded long ago, waits at the cloning step alone for that person's consent, or the consent of whoever can speak for them, recorded with their name and the date in `project.yaml` (root SKILL.md §0); everything else in the work carries on.  
**Example:** `restoration: Spectral denoiser (-18dB hiss) -> De-clicker -> Voice clone model -> translated output.`  
**Source:** assumption — the package's working figure, not a published standard; set the hiss reduction by ear against the source recording; the 1920s poets are an illustrative example.  
`dubbing.archival_voice_pre_translation`

### Lip-Sync for a Mouth That Has No Lips

**Also called:** beak sync, aperture sync, puppet mouth, non-human lip-sync  
**What it is:** **Every lip-sync rule in this package assumes lips, and a great many speaking characters do not have them** — a bird with a beak, a puppet with a hinged jaw, a mask, a creature, a helmet, an animal, a machine. The craft still applies; the unit changes. Instead of matching the bilabial closures — `/p/`, `/b/`, `/m/`, the sounds made by two lips meeting — you match the **aperture**: how far the mouth is open, at what moment, and what shape.  
**Effect on the audience:** They stop asking whether it is talking. Aperture mismatch reads as badly as lip mismatch and in the same way — as a voice laid over a face rather than coming out of it.  
**Used for and where it works best:** **Three states carry nearly all of it.** *Closed*, *part open*, *wide*. Map the vowels to open and the stops to closed, and give the transitions a frame or two rather than snapping. **The bilabial problem inverts**: on a lipped face `/p/`, `/b/` and `/m/` are the ones you must hit; on a beak or a rigid jaw they are the ones that **cannot** be shown at all, so a line whose meaning sits on them will not read — move the stressed word, or accept that the mouth carries none of it and let the body do the work. That last option is real craft rather than a concession: a beak that simply opens on the stressed syllable, with the head and shoulders doing the phrasing, reads as speech to any audience that has watched a puppet before. Check what the lip-sync engine has actually been trained on, because a model trained on human faces may find nothing to drive on a beak — that is a field in the engine record.  
**Best in:** formats: Animated Series, Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Museum Installation, Anime (Japanese 2D), 3D CG Animation | genres: Children's, Comedy, Educational, Fantasy, Heritage (civilisation-focused)  
**Avoid when:** The character has an ordinary human mouth — `rhythm.lip_sync_adaptation` and `dubbing.bilabial_lipsync_alignment` govern there, and the closure rules genuinely apply.  
**Example:** `mouth: three-state aperture — closed / part / wide. Open on stressed vowels, closed on stops, two-frame transitions. Line's stressed word moved off the initial /b/, which the beak cannot show.`  
**Yields to:** `dubbing.bilabial_lipsync_alignment` — The character has an ordinary human mouth.  
`dubbing.lipsync_no_lips`
