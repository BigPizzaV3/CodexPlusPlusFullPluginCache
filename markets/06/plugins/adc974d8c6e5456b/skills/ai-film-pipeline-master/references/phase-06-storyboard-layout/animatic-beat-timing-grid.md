# Animatic & Beat-Timing Synchronization Grid

18 cards. Mathematical frame quantization, panel hold calculations, cutting on musical downbeats, speech pauses, and rhythmic pacing curves bridging the static storyboard to locked audio.

---

### Frame-Rate Math Quantization

**Also called:** integer frame calculation, 24fps/30fps grid, timeline quantization  
**What it is:** Calculating every storyboard panel duration in exact integer video frames based on production frame rates: 24fps (1 second = 24 frames) or 30fps (1 second = 30 frames).  
**Effect on the audience:** Eliminates micro-stutters and off-frame audio phasing when storyboard panels are assembled into a video animatic timeline.  
**Used for and where it works best:** All animatics, editorial rough cuts, and music video timing breakdowns.  
**Best in:** formats: All video production | genres: All  
**Avoid when:** Non-quantized rough timing that uses fractional frames like 1.33 seconds, which causes editing NLE software to slip frames.  
**Example:** `timing_calc: 2.5 seconds @ 24fps = exactly 60 frames. 1.75 seconds @ 24fps = exactly 42 frames.`  
**Source:** assumption — the package's working figure, not a published standard; the frame counts are arithmetic at the stated rate; set the rate from the delivery spec.  
`anim_time.frame_rate_math_quantization`

---

### Rapid Montage Micro-Pacing

**Also called:** quick-cut timing, staccato montage hold, visual burst pacing  
**What it is:** Assigning storyboard panel hold durations between 12 and 36 frames (0.5 to 1.5 seconds per panel), creating breathless velocity and sensory density.  
**Effect on the audience:** Spikes adrenaline, conveys chaos, athletic intensity, or sensory overload; forces the viewer's brain into hyper-alertness.  
**Used for and where it works best:** Action climaxes, chase sequences, sports hype videos, trailer escalations, and psychological panic scenes.  
**Best in:** formats: Action Trailer, Sports Promo, Music Video Drop | genres: Action, Thriller, Sports  
**Avoid when:** Complex emotional dialogue or detailed expository explanations where panels cut away before being read. Ordinary light inside the shots — fire, candles, a lamp, a sunset, a bulb flickering in the scene — is never a flash question. These holds set editorial pace, not a safe flash rate: if the images form a repeated dark-to-bright run, its rate and stopping point belong to `safety.photosensitive_flash`, with the open marker governed by [`ENGINE-CHECK.md`](../ENGINE-CHECK.md).  
**Example:** `panel_timing: Shot 04 (0.75s / 18 frames) -> Shot 05 (0.5s / 12 frames) -> Shot 06 (0.5s / 12 frames) -> Shot 07 (1.0s / 24 frames); safety_note: any repeated dark-to-bright run remains pending_photosensitivity_check.`  
**Source:** assumption — the package's working figure, not a published standard; the frame counts are arithmetic at 24 fps; set the holds on the animatic timeline against the measured audio.  
**Yields to:** `anim_time.dialogue_breathing_pace` — Complex emotional dialogue, panels must be read.  
`anim_time.rapid_montage_micro_pacing`

---

### Dialogue Breathing Pace

**Also called:** conversational hold, natural dialogue timing, sentence pacing  
**What it is:** Setting panel durations to match human speech cadences, typically holding for 60 to 96 frames (2.5 to 4.0 seconds) per spoken sentence.  
**Effect on the audience:** Creates natural, immersive human realism; allows the audience to register facial expression, vocal tone, and subtext simultaneously.  
**Used for and where it works best:** Dramatic conversations, documentary interviews, narrative scenes, and character monologues. A panel carrying a spoken line holds for the real length of that line plus its reaction tail (`pacing.wpm_dramatic_dialogue`); the 2.5–4.0 s band applies only to panels with no line on them — in practice a sentence of about eight words or fewer.  
**Best in:** formats: Feature Film, Drama Series, Documentary | genres: Drama, Biopic, Romance  
**Avoid when:** High-energy musical dance montages where 3-second static holds kill rhythmic momentum.  
**Example:** `dialogue_sync: Character line "I never told him" runs 2.8 seconds; panel holds for 72 frames (3.0s) to include character looking down after speech.`  
**Yields to:** `pacing.wpm_dramatic_dialogue` — on any panel carrying a spoken line, where the real measured length of the line plus its reaction tail sets the hold.  
**Source:** assumption — a working hold derived from the speaking-rate cards; the real hold comes from the rendered line, measured  
`anim_time.dialogue_breathing_pace`

*(Speaking rates are owned by [`../phase-04-audio-narration/pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md); this file cites them and does not restate them.)*

---

### Contemplative Held Tableau

**Also called:** cinematic hold, atmospheric tableau pace, wide landscape freeze  
**What it is:** Sustaining a single wide environmental or character panel for 120 to 240 frames (5.0 to 10.0 seconds) with subtle atmospheric movement (dust, smoke, wind).  
**Effect on the audience:** Induces profound serenity, meditative awe, existential weight, or heavy dramatic loneliness.  
**Used for and where it works best:** Opening establishing shots, post-battle grief sequences, desert wilderness crossings, and art-house codas.  
**Best in:** formats: Arthouse Film, Historical Epic, Nature Documentary | genres: Arthouse, Epic, Heritage, Western  
**Avoid when:** Fast-paced 15-second social media reels where a 5-second hold causes viewers to swipe away.  
**Example:** `tableau_hold: Wide shot of ruined Nineveh walls under stormy sky, held for exactly 168 frames (7.0 seconds) as low drone music sustains.`  
**Source:** assumption — the package's working figure, not a published standard; set the hold by timing the animatic against the rendered audio.  
**Yields to:** `anim_time.staccato_jump_cut_rhythm` — Fast vertical short-form, where a long hold loses the viewer.  
`anim_time.contemplative_held_tableau`

---

### Downbeat Transient Cutting

**Also called:** beat-matching cuts, kick-drum sync, musical hit alignment  
**What it is:** Aligning panel transitions precisely on the downbeat of musical bars (beat 1 of a 4/4 measure) or on heavy kick-drum/snare transients.  
**Effect on the audience:** Creates a visceral, dance-like somatic connection where the eyes and ears experience visual impact simultaneously.  
**Used for and where it works best:** Music videos, dance choreography, commercial hype edits, and action montages.  
**Best in:** formats: Music Video, Commercial / TVC, Dance Film | genres: Pop, Electronic, Hip-Hop, Rock  
**Avoid when:** Realistic dialogue scenes where cutting exactly on drum beats feels mechanical, distracting, and gimmicky.  
**Example:** `cut_point: Music tempo 120 BPM (1 beat = 12 frames @ 24fps). Cut lands exactly on frame 48 (downbeat of measure 2).`  
**Source:** assumption — the package's working figure, not a published standard; the 12 frames is arithmetic from the example tempo (120 BPM = 0.5 s = 12 frames at 24 fps); measure the real tempo from the track.  
**Yields to:** `anim_time.dialogue_breathing_pace` — Realistic dialogue, where beat-locked cuts read as gimmick.  
`anim_time.downbeat_transient_cutting`

---

### Pre-Chorus Rhythmic Acceleration

**Also called:** build-up tempo ramp, accelerating cut rate, tension ramp timing  
**What it is:** Progressively shortening panel durations as the pre-chorus music builds toward the drop (e.g., Panel 1: 3.0s -> Panel 2: 2.0s -> Panel 3: 1.5s -> Panel 4: 1.0s -> Panel 5: 0.5s).  
**Effect on the audience:** Induces mounting psychological anxiety and breathlessness, perfectly priming the audience for the explosive chorus release.  
**Used for and where it works best:** Music video pre-choruses, trailer Act 2 escalation, and pre-battle mobilization sequences.  
**Best in:** formats: Music Video, Trailer, Action Climax | genres: Action, Pop, Epic  
**Avoid when:** Somber acoustic ballads or peaceful pastoral scenes. This ramp sets editorial pace, not a safe flash rate: if it creates a repeated dark-to-bright run, its rate and stopping point belong to `safety.photosensitive_flash`.  
**Example:** `ramp_math: Measure 1: 4 beats (48f) -> Measure 2: 3 beats (36f) -> Measure 3: 2 beats (24f) -> Measure 4: 1 beat (12f) -> CHORUS DROP; safety_note: any repeated dark-to-bright run remains pending_photosensitivity_check.`  
**Source:** assumption — the package's working figure, not a published standard; set the durations against the track's measured tempo.  
**Yields to:** `anim_time.tempo_drift_rubato_alignment` — Somber acoustic, unmetered material with no build.  
`anim_time.pre_chorus_rhythmic_acceleration`

---

### Riser Climax Panel Density

**Also called:** whoosh-cut density, pitch-riser visual stutter, trailer riser sync  
**What it is:** Cutting through rapid-fire flashes of imagery during the final 2 seconds of a cinematic white-noise or string pitch riser. How rapid, and the point at which it has to stop, are not set here - see `safety.photosensitive_flash`, which owns them.  
**Effect on the audience:** Creates an overwhelming visual crescendo that matches auditory frequency saturation, delivering immense sensory payoff.  
**Used for and where it works best:** Theatrical trailer climaxes, sci-fi wormhole jumps, and horror jump-scare builds.  
**Best in:** formats: Movie Trailer, Sci-Fi Teaser, Horror Climax | genres: Horror, Sci-Fi, Action  
**Avoid when:** Standard conversational television episodes. And note what this card is actually describing when its panels run short into a blackout: not a pacing choice but an alternation between bright and dark, held. **That is the shape `safety.photosensitive_flash` exists for** — how fast it may run and when it has to stop are there, and this card sets neither. It was written in the vocabulary of panel density rather than of flashing, which is the only reason it sat outside that rule for so long.  
**Example:** `riser_sync: Final 2 seconds of string riser, four panels ending on a blackout, held at the rate safety.photosensitive_flash permits: (1) Eye wide, (2) Gun cocking, (3) Door slamming, (4) Blackout.`  
**Source:** assumption — the package's working figure, not a published standard; set it against the riser as measured in the rendered audio.  
**Yields to:** `safety.photosensitive_flash` — The rate and the stopping point of the flashing run.  
`anim_time.riser_climax_panel_density`

---

### Dialogue Reaction Offset Timing

**Also called:** delayed reaction cut, speech-trailing hold, L-cut reaction beat  
**What it is:** Holding the camera on the listening character for 12 to 24 frames (0.5 to 1.0 second) AFTER the speaking character finishes their line.  
**Effect on the audience:** Allows the emotional truth of the words to sink in, capturing the listener's internal processing, vulnerability, or deceit.  
**Used for and where it works best:** High-stakes dramatic confrontations, romantic confessions, and courtroom verdicts.  
**Best in:** formats: Feature Drama, Courtroom Thriller, Romance | genres: Drama, Romance, Thriller  
**Avoid when:** Fast rapid-fire banter where immediate verbal counter-attacks are required.  
**Example:** `reaction_hold: Speaker finishes line at 0:03.2; panel holds on listener's stunned expression until 0:04.0 before cutting.`  
**Source:** assumption — the package's working figure, not a published standard; set the hold by timing the animatic against the rendered dialogue.  
**Yields to:** `dial.rapid_fire` — Rapid-fire banter needing immediate verbal counter-attack.  
`anim_time.dialogue_reaction_offset_timing`

---

### Subconscious Anticipatory Cut

**Also called:** pre-impact cut, 3-frame early cut, psychological anticipation  
**What it is:** Executing the cut to an explosion, punch, or gun firing exactly 2 to 4 frames BEFORE the auditory sound effect hits.  
**Effect on the audience:** Subconsciously prepares the visual cortex, making the subsequent physical impact feel twice as brutal, massive, and real.  
**Used for and where it works best:** Heavy combat impacts, explosions, vehicle crashes, and sudden thunderclaps.  
**Best in:** formats: Action Feature, War Film, Trailer | genres: Action, War, Martial Arts  
**Avoid when:** Slow comedy timing or gentle acoustic storytelling. One isolated impact is the scope here; if explosions, gunfire or impact frames repeat into a dark-to-bright run, the rate and stopping point belong to `safety.photosensitive_flash`.  
**Example:** `cut_point: one isolated visual cuts to an incoming cannonball at frame 34; audio cannon blast hits frame 37. A repeated impact series remains pending_photosensitivity_check.`  
**Source:** assumption — the package's working figure, not a published standard; set the lead on the timeline by eye against the sound hit.  
**Yields to:** `comedy.timing_on_the_page` — Slow comedy, where the timing is written not pre-cut.  
`anim_time.subconscious_anticipatory_cut`

---

### Silence Stretching Tension Hold

**Also called:** audio dead-drop hold, silence freeze, negative space timing  
**What it is:** Holding a completely static storyboard panel during an abrupt 1-to-2 second drop into total auditory silence right before a massive explosion.  
**Effect on the audience:** Creates deafening dramatic tension; forces the audience to hold their collective breath in suspense.  
**Used for and where it works best:** Bomb defusal scenes, standoffs in westerns, and before the drop in heavy electronic tracks.  
**Best in:** formats: Western Duel, Crime Standoff, EDM Music Video | genres: Thriller, Western, Crime  
**Avoid when:** High-speed dialogue scenes where awkward silence sounds like an audio editing mistake.  
**Example:** `hold_spec: Panel 8 (Standoff) holds for 36 frames of complete dead digital silence; Panel 9 drops with deafening gun blast on frame 37.`  
**Source:** assumption — the package's working figure, not a published standard; set the hold by ear against the animatic.  
**Yields to:** `pacing.interruption_overlap` — High-speed dialogue, where a gap reads as an edit fault.  
`anim_time.silence_stretching_tension_hold`

---

### Compound Six-Eight and Waltz Meter Sync

**Also called:** 6/8 swing cutting, triplet sync, folk meter animatic timing  
**What it is:** Timing cuts to 6/8 or 3/4 time signatures, cutting on the primary dotted-quarter pulses (beats 1 and 4 in 6/8) rather than rigid 4/4 downbeats.  
**Effect on the audience:** Imparts a rolling, circular, hypnotic folk dance momentum that feels organic and fluid.  
**Used for and where it works best:** Assyrian Tolama and Khigga folk dances, Celtic waltzes, and sea shanties.  
**Best in:** formats: Folk Music Video, Heritage Documentary, Period Romance | genres: Folk, Heritage, Romance  
**Avoid when:** Modern trap or four-on-the-floor electronic dance tracks.  
**Example:** `timing_6_8: Tempo 116 BPM in 6/8; cut lands on beat 1 (dotted quarter) every 18.6 frames at 24 fps - alternate 18 and 19 frames so the cuts do not drift - matching foot stomps.`  
**Source:** assumption — the package's working figure, not a published standard; set it against the measured beat grid of the track.  
**Yields to:** `anim_time.downbeat_transient_cutting` — Four-on-the-floor or trap, a rigid 4/4 grid.  
`anim_time.waltz_and_compound_meter_sync`

---

### Voiceover Pause Window Hold

**Also called:** narrator breath hold, vocal cadence padding, voiceover window  
**What it is:** Extending wide landscape or establishing panels by 24 to 48 frames (1.0 to 2.0s) during natural paragraphs or breath pauses in narration.  
**Effect on the audience:** Gives the viewer's brain time to digest historical or emotional information without being rushed to the next image.  
**Used for and where it works best:** Heritage documentaries, educational history videos, and nature documentaries.  
**Best in:** formats: Documentary Feature, Educational Reel | genres: Heritage, Documentary, Science  
**Avoid when:** Fast promotional sales pitches where pauses cause viewer drop-off.  
**Example:** `narration_gap: Narrator says "...and then Babylon fell." 2.0-second silence follows; panel holds on smoking ruins for 48 frames before music swells.`  
**Source:** assumption — the package's working figure, not a published standard; set the hold by timing the animatic against the rendered narration.  
**Yields to:** `anim_time.b_roll_coverage_density_ratio` — Fast promotional narration, where a pause loses viewers.  
`anim_time.voiceover_pause_window_hold`

---

### Rubato and Free-Meter Acoustic Alignment

**Also called:** unmetered vocal sync, free-tempo alignment, mawal pacing  
**What it is:** Abandoning fixed BPM grids during unmetered vocal solos (e.g., Iraqi Mawal, Assyrian Rawe, opera recitative), anchoring cuts to vocal pitch transitions and melodic ornamentation.  
**Effect on the audience:** Deeply expressive, emotional, and authentic; honors the organic freedom of traditional Middle Eastern and classical music.  
**Used for and where it works best:** Mesopotamian prologue scenes, funeral laments, and expressive acoustic solos.  
**Best in:** formats: Cultural Memoir, Epic Prologue, Sacred Liturgy | genres: Heritage, Classical, Folk  
**Avoid when:** Quantized electronic dance music.  
**Example:** `free_sync: Singer improvises Bayati vocal run; cut to Panel 2 occurs precisely when the voice resolves down to the tonic root note.`  
**Yields to:** `anim_time.downbeat_transient_cutting` — Quantized electronic music with a fixed BPM grid.  
`anim_time.tempo_drift_rubato_alignment`

---

### Staccato Jump-Cut Rhythm

**Also called:** metric jump cuts, beat-locked angle snap, pop jump rhythm  
**What it is:** Cutting between multiple angles of the same subject on successive eighth-note or quarter-note beats without changing camera distance or screen direction.  
**Effect on the audience:** Injects quirky, playful, modern pop kinetic energy; breaks classical continuity to emphasize frantic speed or wit.  
**Used for and where it works best:** Fast fashion reels, comedy routines, modern pop music videos, and creative DIY cooking montages.  
**Best in:** formats: Vertical Short-Form, Pop Music Video, Commercial | genres: Comedy, Pop, Fashion  
**Avoid when:** Serious historical biopics or solemn funeral scenes. And note where the repetition rate here actually comes from: the track's tempo, which this card does not set and cannot see. Where successive cuts on one subject stop reading as cuts and start reading as a bright/dark alternation, the rate and the stopping point are `safety.photosensitive_flash`.  
**Example:** `jump_cuts: Panel 1 Front medium (12f) -> Panel 2 45-degree medium (12f) -> Panel 3 Profile medium (12f), cutting on consecutive snare hits; keep brightness stable, or leave the run pending_photosensitivity_check.`  
**Yields to:** `anim_time.contemplative_held_tableau` — Solemn historical or funeral material.  
`anim_time.staccato_jump_cut_rhythm`

---

### High-Speed Slow-Motion Multiplier

**Also called:** overcrank timing math, slow-mo hold expansion, 96fps stretch  
**What it is:** Multiplying standard panel duration by the overcrank factor (4x for 96fps, 5x for 120fps) when an impact or graceful motion is filmed in slow-motion.  
**Effect on the audience:** Stretches dramatic time, revealing micro-expressions, fluid dynamics, and heroic grace that normal time conceals.  
**Used for and where it works best:** Sports athletic leaps, explosions, sword clashes, and fashion fabric fluttering.  
**Best in:** formats: Action Feature, High-End Commercial, Sports Highlight | genres: Action, Sports, Fashion  
**Avoid when:** Conversational dialogue where slow motion makes actors look intoxicated.  
**Example:** `slowmo_calc: Real-world 0.5s sword strike filmed at 96fps (4x slowdown) = 2.0s panel duration (48 frames @ 24fps playback).`  
**Source:** assumption — the package's working figure, not a published standard; the multipliers are arithmetic (capture rate / 24 fps playback: 96/24 = 4, 120/24 = 5; 0.5 s x 4 = 2.0 s = 48 frames); set the panel against the project's real playback rate.  
**Yields to:** `anim_time.dialogue_breathing_pace` — Conversational dialogue, where slow motion distorts the read.  
`anim_time.slow_motion_overcrank_multiplier`

---

### B-Roll Coverage Density Ratio

**Also called:** cutaway density, montage coverage ratio, detail insert frequency  
**What it is:** Enforcing a ratio of 3 to 4 short B-roll cutaway panels (0.75s to 1.5s each) for every 1 primary master dialogue or narration panel.  
**Effect on the audience:** Keeps documentary and commercial montages visually dynamic, preventing visual boredom during long spoken passages.  
**Used for and where it works best:** Corporate documentaries, travel vlogs, cooking shows, and technical explainers.  
**Best in:** formats: Documentary, Commercial, Travel Video | genres: Documentary, Lifestyle  
**Avoid when:** Intimate dramatic confessions where cutting away to scenery ruins actor emotional intensity.  
**Example:** `b_roll_ratio: Narrator speaks for 6 seconds; storyboard shows 1 master interview shot (2s) followed by 3 rapid cutaways (1.3s each).`  
**Source:** assumption — the package's working figure, not a published standard; set the ratio against the edit.  
**Yields to:** `anim_time.dialogue_reaction_offset_timing` — Intimate confession, where cutting away kills intensity.  
`anim_time.b_roll_coverage_density_ratio`

---

### Sound Bridge J-Cut Timing

**Also called:** audio advance lead, pre-visual sound, J-cut sync  
**What it is:** Allowing the audio (dialogue, sound effect, or new music) of the upcoming panel to start 18 to 24 frames BEFORE the visual cut actually occurs.  
**Effect on the audience:** Creates seamless visual transitions; leads the viewer's subconscious into the next scene without jarring hard cuts.  
**Used for and where it works best:** Major scene transitions, entering memory flashbacks, and dialogue scene cutting.  
**Best in:** formats: All narrative films and documentaries | genres: All  
**Avoid when:** Sudden shock cuts or surprise horror jump-scares, where the sound must not lead the picture; the impact timing there belongs to `anim_time.subconscious_anticipatory_cut`.  
**Example:** `j_cut: Panel 1 (Bedroom) holds visually while sound of church bells from Panel 2 enters 24 frames early.`  
**Source:** assumption — the package's working figure, not a published standard; set it by ear on the edit timeline.  
**Yields to:** `anim_time.sound_bridge_l_cut_timing` — The outgoing sound should trail instead of the incoming leading. `anim_time.subconscious_anticipatory_cut` — An isolated shock or impact, where the sound must not lead the picture.  
`anim_time.sound_bridge_j_cut_timing`

---

### Sound Bridge L-Cut Timing

**Also called:** audio trailing sustain, post-visual sound, L-cut bleed  
**What it is:** Letting the dialogue or sound effect from the previous panel continue playing for 18 to 36 frames after the visuals have already transitioned to the new panel.  
**Effect on the audience:** Ties disparate locations together; reinforces thematic continuity and emotional lingering across scene breaks.  
**Used for and where it works best:** Concluding emotional speeches, moving into aftermath scenes, and montage sequences.  
**Best in:** formats: All narrative films and documentaries | genres: All  
**Avoid when:** High-speed combat where previous gunfire bleeding into quiet rooms creates geographic confusion.  
**Example:** `l_cut: Visual cuts to empty courtroom (Panel 2) while judge's voice from Panel 1 finishes echoing for 30 frames.`  
**Source:** assumption — the package's working figure, not a published standard; set the overlap by ear on the cut.  
**Yields to:** `anim_time.sound_bridge_j_cut_timing` — The incoming sound should lead instead of the outgoing trailing.  
`anim_time.sound_bridge_l_cut_timing`
