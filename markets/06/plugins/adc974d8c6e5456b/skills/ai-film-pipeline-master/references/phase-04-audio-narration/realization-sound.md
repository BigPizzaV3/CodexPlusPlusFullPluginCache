# Realization: Sound, Voice & Silence

8 cards. Translating conceptual sonic intent into structured audio architecture, stems, listening environments, and silence relationships.

---

### Sonic Event & Silence Map

**Also called:** sound cue map, audio architecture blueprint, P10V-AUD-01  
**What it is:** Placing voice, music, ambience, effects, and designed silence in structured relation to visual scenes, dramatic beats, and viewer emotional states.  
**Effect on the audience:** Orchestrates audience focus so audio never overwhelms the senses, treating quietness as a powerful narrative tool.  
**Used for and where it works best:** Pre-production audio planning: map where music swells, where silence drops, and where voice carries alone.  
**Best in:** formats: Feature Film, Documentary Feature, Limited Series | genres: Drama, Thriller, Historical  
**Avoid when:** Filling every single millisecond with loud sound, treating silence as empty dead air.  
**Example:** `timeline_map: Beat 1: Wind ambience -> Beat 2: Voiceover enters solo -> Beat 3: Absolute silence on reveal.`  
`sound_realize.event_silence_map`

---

### Stem, Layer & Object Architecture

**Also called:** modular audio stems, non-destructive mix architecture, P10V-AUD-02  
**What it is:** Preserving independent sonic components (stems) across the entire pipeline for localized adaptation, revision, and dynamic ducking.  
**Effect on the audience:** Delivers a balanced, transparent acoustic landscape that adapts cleanly across phone speakers, soundbars, and headphones.  
**Used for and where it works best:** Multi-platform delivery where dialogue clarity must be guaranteed across noisy mobile and quiet home environments.  
**Best in:** formats: All digital video and film | genres: All  
**Avoid when:** Baking music, foley, and voice into a single unalterable stereo track before final picture lock.  
**Example:** `mix_spec: stem isolation maintained: [DX], [FX], [BG], [MX], delivered separately so the destination's own loudness target can be met at the mix.`  

> **This card sets no loudness number, and the example above used to.** It carried `-24 LKFS`, which
> is the US broadcast television figure, and the point of keeping stems separate is precisely that
> the target is a property of the *destination*, not of the architecture: broadcast, cinema, a
> podcast platform and a phone feed all want different numbers, and a podcast delivered at the
> broadcast figure is audibly quiet against everything around it. `mix.lufs_loudness_targets` in
> [`audio-mixing-mastering.md`](audio-mixing-mastering.md) owns every loudness figure in the package.
> Take it from there, for the destination you are actually delivering to, at the mix — which is also
> where this phase says it sets no mixing numbers.

**Yields to:** `mix.lufs_loudness_targets` — Any loudness figure: the card stands down and names that card as the owner of every number.  
`sound_realize.stem_architecture`

---

### Voice Performance Blueprint

**Also called:** vocal intent blueprint, directing framework, P10V-AUD-03  
**What it is:** Translating dramatic or factual intent into actionable vocal parameters: objective, distance, pace range, and pronunciation authority.  
**Effect on the audience:** Ensures vocal performance reinforces dramatic subtext rather than merely reading literal words off a script.  
**Used for and where it works best:** Giving precise directing notes to voice actors or configuring generative AI voice prompts.  
**Best in:** formats: All voice-driven media | genres: All  
**Avoid when:** Giving vague, contradictory notes like "sound exciting but also solemn and funny."  
**Example:** `blueprint: speaker_role: solemn archaeological witness; objective: convey irreversible loss; pace: 115 WPM; distance: intimate.`  
**Source:** assumption — the package's working figure, not a published standard; set it against the rendered audio, measured.  
`sound_realize.voice_blueprint`

---

### Listening-Environment Matrix

**Also called:** device translation test, multi-speaker audit, P10V-AUD-04  
**What it is:** Testing and verifying that audio remains fully intelligible across mobile phone speakers, cheap earbuds, television sets, and studio monitors.  
**Effect on the audience:** Guarantees that a user watching a reel on a noisy commuter train understands the narration as clearly as an editor in a studio.  
**Used for and where it works best:** Quality assurance on final audio masters, run in the edit on the finished mix — checks the mix must pass, like the gate in `mix.mono_compatibility_audit`, not values this phase sets: check mono compatibility and speech intelligibility on each named playback class, and record pass or fail by device. EQ, loudness and playback-level numbers belong to the mix and the destination specification.  
**Best in:** formats: Vertical Short-Form, Web Video, Broadcast | genres: All  
**Avoid when:** Mixing exclusively on $2,000 studio monitors without ever checking playback on an iPhone speaker.  
**Example:** `audit (run in the edit): sum-to-mono test passes; speech remains intelligible on the named smartphone, earbud, television and monitor checks at one documented, repeatable listening level.`  
`sound_realize.listening_matrix`

---

### Spatial Audio Behavior Sketch

**Also called:** spatial staging, 3D panning map, P10V-AUD-05  
**What it is:** Pre-visualizing position, movement, depth, enclosure, proximity, and listener acoustic relation before rendering the final mix.  
**Effect on the audience:** Creates a convincing illusion of physical space; sounds move naturally to mirror visual blocking on screen.  
**Used for and where it works best:** Chariot passes, arrows flying across the stereo field, and off-screen character calls.  
**Best in:** formats: Feature Film, Action Short, XR | genres: Action, Historical, Sci-Fi  
**Avoid when:** Panning dialogue wildly around the stereo spectrum, which disorients the viewer and breaks focus.  
**Example:** `spatial_cue: Chariot approaches from far left off-screen, sweeps through center, decays in wide stereo right.`  
`sound_realize.spatial_behavior`

---

### Audio-to-Visual Counterpoint Test

**Also called:** sonic counterpoint, irony check, P10V-AUD-06  
**What it is:** Deliberately testing whether audio reinforces, contradicts, leads, lags, reveals, or conceals what the visual channel is showing.  
**Effect on the audience:** Generates rich dramatic subtext and irony; prevents boring duplication where sound merely describes what is seen.  
**Used for and where it works best:** High-level narrative cinema and hard-hitting documentary storytelling.  
**Best in:** formats: Film, Documentary, Art Cinema | genres: Drama, Tragedy, Psychological  
**Avoid when:** Accidental dissonance where mismatched sound confuses the audience without dramatic purpose.  
**Example:** `test: Visual: brutal burning of ancient city; Audio: gentle, serene lullaby sung in archaic dialect.`  
`sound_realize.counterpoint_test`

---

### Dynamic & Fatigue Envelope

**Also called:** listener fatigue prevention, loudness dynamics, P10V-AUD-07  
**What it is:** Modeling perceived intensity, acoustic density, rest intervals, and listener ear fatigue across an entire video or series.  
**Effect on the audience:** Prevents acoustic exhaustion; preserves listener emotional responsiveness by providing quiet valleys between dynamic peaks.  
**Used for and where it works best:** Action movies, long historical epics, and high-energy social channels.  
**Best in:** formats: Feature Film, Long-Form Documentary, Series | genres: Action, War, Epic  
**Avoid when:** Brickwall limiting an entire 20-minute video at maximum volume without a single quiet moment.  
**Example:** `handover: 3 minutes of dense battle audio, then 45 seconds of solitary wind whisper. The contrast between the two is the point; how wide it is set in the edit.`  
**Source:** assumption — the package's working figure, not a published standard; set the length of the quiet valley by ear in the edit.  
`sound_realize.fatigue_envelope`

---

### Silent & Textual Sonic Materialization

**Also called:** implied sound, textual cadence, silent rhythm, P10V-AUD-08  
**What it is:** Engineering cadence, breath, pause, and implied sound into visual typography, subtitles, and silent moments that produce auditory sensations in the mind.  
**Effect on the audience:** Triggers the brain's internal auditory cortex; the viewer "hears" the impact or the scream even in complete silence.  
**Used for and where it works best:** Silent cinema sequences, muted video playback with kinetic typography, and poetic art films.  
**Best in:** formats: Silent Video, Social Video (Sound-Off mode), Art Cinema | genres: Poetry, Drama, Horror  
**Avoid when:** Forcing generic synthetic audio onto scenes that achieve tenfold greater power through absolute silence.  
**Example:** `visual: Extreme close-up of heavy hammer smashing anvil; Audio: complete silence for 3 frames, mind fills the crack.`  
**Source:** assumption — the package's working figure, not a published standard; set the silence length on the timeline in the edit.  
`sound_realize.silent_materialization`
