# ElevenLabs Engine & Directing Craft

16 cards. Model tier, steadiness against expressiveness, delivery direction, pronunciation control, seeds and voice-cloning hygiene for an AI voice engine. Written for ElevenLabs; its current models, settings and ranges are in its adapter in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §7.

---

### Long-Form Expressive Narration Model

**Also called:** Eleven Multilingual v2, conversational nuance engine, emotional model, long-form narration model  
**What it is:** Choosing, within the voice engine, the model built to hold one voice steady across a long read while keeping natural pauses, cultural accents and dramatic range, in every language the project needs. Confirm the project's language against the languages-offered line of the audio engine record; which ElevenLabs model fills this role today is in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** Conveys subtext, human vulnerability, and nuanced breath patterns that prevent the listener from detecting synthetic origin.  
**Used for and where it works best:** Long-form narration, historical documentaries, character dialogue, and dramatic podcasts where emotional range outweighs raw speed.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Audio Drama, Feature Film, Narrative Podcast | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Tragedy, Mystery / Whodunit  
**Avoid when:** Ultra-low latency real-time voice agents or fast high-volume social reel batch runs where cost and generation latency must be minimized.  
**Example:** `model: the engine's long-form narration model | settings: the engine's defaults, moved only after a test read of this segment` — the model name and the setting names are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `elevenlabs.model_turbo_v2_5` — High-volume reel batches where latency and cost dominate.  
`elevenlabs.model_multilingual_v2`

---

### High-Throughput Voice Tier

**Also called:** Eleven Turbo v2.5, fast render model, short-form voice engine, high-volume tier  
**What it is:** Choosing a faster, cheaper model tier of the voice engine for volume work and rapid iterations, and accepting a narrower emotional range in exchange. The model this card was first written for has since been deprecated by its vendor in favour of its low-latency model, so check what fills the role today in its adapter in ENGINE-CHECK.md before choosing one.  
**Effect on the audience:** Delivers crisp, punchy, and highly intelligible speech that maintains momentum without lag or sluggish pacing.  
**Used for and where it works best:** Vertical short-form videos (Reels, TikTok, Shorts), fast news recaps, commercial promos, and rapid scratch track auditioning.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Corporate / Explainer, Social Media Video | genres: Action, Educational / Science, News / Analysis, Comedy, Commercial  
**Avoid when:** Deeply dramatic scenes requiring complex weeping, subtle emotional breaks, or archaic poetic rhythms.  
**Example:** `model: the engine's fast, low-cost tier | settings: the engine's defaults, held steadier than the drama read` — the current model name and its cost per character are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `elevenlabs.model_multilingual_v2` — Weeping, subtle emotional breaks, archaic poetic rhythm.  
`elevenlabs.model_turbo_v2_5`

---

### Draft-Speed Voice Model

**Also called:** Eleven Flash v2.5, real-time draft engine, scratch voice model  
**What it is:** Using the voice engine's lowest-latency model for high-volume test generation — scratch reads and timing drafts where speed matters more than performance. Its current latency and per-call limits are in its adapter in ENGINE-CHECK.md; check them before building a schedule around it.  
**Effect on the audience:** Snappy, immediate delivery with consistent tonal flatline, useful for rapid information scanning.  
**Used for and where it works best:** Scratch track creation for animatics, rapid script length testing, and bulk pre-visualization of timing.  
**Best in:** formats: Animatics / Storyboard Previz, Fast Social Video, Scratch Track Audition | genres: Tech / Tutorial, Informational, Rapid Prototyping  
**Avoid when:** Final theatrical mix, hero documentary narration, or emotionally vulnerable drama.  
**Example:** `model: the engine's lowest-latency model | settings: the engine's defaults; this read is a timing draft, not a performance` — the model name is in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `elevenlabs.model_multilingual_v2` — Final mix, hero narration, emotionally vulnerable drama.  
`elevenlabs.model_flash_v2_5`

---

### Expressive Range Versus Consistency Control

**Also called:** stability slider, voice consistency vs expressiveness, monotone prevention  
**What it is:** The voice engine's control that trades performance variation against consistency: lower settings widen the emotional range, higher settings hold the read steady and, pushed too far, flatten it into monotone. The control's name, scale and default for the engine in use are in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** Set well, organic human variation; too high, stiff and monotonous; too low, erratic and rushed.  
**Used for and where it works best:** From the engine's default, a step lower for passionate drama and storytelling, a step higher for calm encyclopedic documentaries and corporate tutorials — judged on a test read, not a number, changing one control at a time; the chosen setting is kept with the take's metadata.  
**Best in:** formats: All audio formats | genres: All genres  
**Avoid when:** Leaving at default without testing the emotional weight of the specific script segment.  
**Example:** `consistency: a step below the engine's default, so the narrator's voice can crack slightly on tragic historical defeats` — the setting's name and scale are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.stability_tuning`

---

### Clone Fidelity Control

**Also called:** similarity boost, voice cloning fidelity, artifact suppression  
**What it is:** The voice engine's control dictating how closely the generation adheres to the original cloned voice sample versus allowing generative leeway. Its name, default, and which models offer it at all are in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** High settings lock the exact timbre of the original voice actor; pushed too high on an imperfect source, they also reproduce its background hum, noise and microphone artifacts.  
**Used for and where it works best:** Leave it at the engine's default for a clean professional clone; ease it down only when the source carries minor background noise — a stopgap, since the real fix is a cleaner source.  
**Best in:** formats: Cloned Actor Narration, Branded Voiceover, Continuity Series | genres: Documentary, Series, Corporate  
**Avoid when:** Setting it to its maximum on a source file that has room reverb or compression artifacts.  
**Example:** `fidelity: the engine's default — preserves the deep baritone timbre without carrying the training hiss` — the setting's name and default are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `elevenlabs.voice_cloning_hygiene` — The source carries reverb or compression artifacts.  
`elevenlabs.similarity_boost`

---

### Delivery Intensity Amplifier

**Also called:** style exaggeration, dramatic amplification, expression booster  
**What it is:** A control some voice engines offer that amplifies the original speaker's style beyond what the text carries, at a cost in stability. Whether the engine offers one, and its vendor's advice on it, is in its adapter in ENGINE-CHECK.md — read that before raising it.  
**Effect on the audience:** Brings theatrical intensity, heightened indignation, joy, or terror to the delivery; forced through the amplifier, it costs pronunciation and stability.  
**Used for and where it works best:** Dramatic monologues, battle speeches, horror climaxes, and energetic trailer hooks. Build intensity from the script, direction and casting first; start with the amplifier off and raise it only if a test read falls short, one change at a time, keeping the neutral take for comparison.  
**Best in:** formats: Trailer / Teaser, Epic Drama, Horror Short, Action Promo | genres: Epic, Fantasy, Horror, Action, Trailer  
**Avoid when:** Understated historical documentaries, news reports, or factual educational explainers where zero style exaggeration is required.  
**Example:** `intensity: carried by the line and the casting of an ancient warrior's challenge; amplifier off, consistency a step below the default to unlock raw cinematic fury` — the setting names are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `elevenlabs.stability_tuning` — Understated documentary; style at zero, stability carries the read.  
`elevenlabs.style_exaggeration`

---

### Speaker Similarity Toggle

**Also called:** speaker boost, presence boost, volume & clarity normalizer  
**What it is:** A toggle some voice engines offer that pushes the output closer to the original speaker's identity. Its effect is subtle, and it is not a presence control: presence is made in the mix. Its name, default and the models that offer it are in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** Keeps a voice recognisably itself from take to take; the sense of a speaker right at the listener's ear, cutting through score and foley, comes from the mix.  
**Used for and where it works best:** Leave it at the engine's default for modern video production, podcasting, and social media reels, and build dialogue clarity over the score in the mix (`mix.frequency_slot_carving`, `mix.dialogue_to_music_ratio`).  
**Best in:** formats: All formats | genres: All genres  
**Avoid when:** Expecting it to place the voice: a distant, diegetic, in-world shout or radio-filtered speaker effect is made with a space in the mix, not with this toggle.  
**Example:** `speaker similarity: the engine's default — the voice's presence over heavy orchestral war drums is built in the mix; where it actually sits against them is set in the edit.` — the toggle's name and default are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `mix.convolution_ir_matching` — A distant, in-world or radio-filtered voice needs a space, not presence.  
`elevenlabs.speaker_boost`

---

### Voice Cloning Hygiene

**Also called:** source audio cleaning, master sample curation, Instant / Professional Voice Cloning (ElevenLabs)  
**What it is:** The strict protocol for selecting and preparing training audio for whichever voice-cloning tier the engine offers — a quick clone built from a short sample, or a trained clone built from hours of speech: dry, clean, reverb-free speech from one speaker. The sample length, recording level and file format each tier asks for are the vendor's figures and are in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** Prevents phase cancellation, room echo coloration, and phantom mouth clicks in the generated output.  
**Used for and where it works best:** Before enrolling any voice in the pipeline: strip background music, apply gentle noise gate, remove plosives, and bring the sample to a steady level inside the recording window the engine asks for.  
**Best in:** formats: Custom Voice Cloning, Historical Figure Reconstruction | genres: All  
**Avoid when:** Uploading audio pulled directly from movie clips with music score or explosions behind the dialogue. And before any of this: cloning the voice of a real adult, living or recorded long ago, waits at the cloning step alone for that person's consent, or the consent of whoever can speak for them, recorded with their name and the date in `project.yaml` (root SKILL.md §0); everything else in the work carries on. **A real, named child's voice is different, and it does not stop the work**: everything else carries on, and only the cloning step waits until the parent's or guardian's consent is recorded, with their name and the date, in `child_voice_clone_consent` in `project.yaml` — the voice platforms require it.  
**Example:** `spec: completely dry, no reverb, no compression pumping, continuous speech from one speaker, at the length, level and file format the engine's current guidance names for the chosen tier` — those figures are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `restore.voice_training_decontamination` — A contaminated sample must be cleaned before enrolment.  
`elevenlabs.voice_cloning_hygiene`

---

### Emotional Direction for the Voice Engine

**Also called:** performance brackets, emotive cue insertion, audio tags (ElevenLabs)  
**What it is:** Carrying emotional direction into synthesis: narrative context or a prelude line the model reads the mood from, or inline delivery tags where the model documents them — which models do, and the syntax, is in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** Guides the AI model's prosody, inducing hushed awe, trembling hesitation, or triumphant proclamation — without altering the spoken text once any spoken direction is cut from the take.  
**Used for and where it works best:** Emotional prelude sentences and narrative context, on any model; inline tags only where documented, and each tag auditioned with the selected voice before it is relied on. Any direction the model speaks aloud is cut in the edit.  
**Best in:** formats: Audio Drama, Cinematic Narration, Short-Form Storytelling | genres: Mystery, Drama, Horror, Epic  
**Avoid when:** Over-tagging every three words, or tagging for a model that does not read tags — either way the model can pronounce the direction as text.  
**Example:** `line: "The city did not fall to iron... it fell to famine." | direction: solemn and quiet` — how the direction is passed, as a prelude sentence or as the engine's own tag, is in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.prompt_tags_emotion`

---

### Pacing Punctuation Control

**Also called:** punctuation cadencing, micro-pause engineering  
**What it is:** Using typographical marks (ellipses `...`, em-dashes `—`, commas, periods and line breaks) to shape breath and pause in generative TTS. Punctuation shapes a pause; it does not time it, and another model or version can read the same mark differently.  
**Effect on the audience:** Creates natural rhetorical pauses, allowing critical information to sink in before moving to the next revelation.  
**Used for and where it works best:** An ellipsis gives a hesitant, thoughtful pause; an em-dash an abrupt thought-interruption; a full stop or a paragraph break a larger reset. Where a pause must be an exact length, use the engine's explicit pause control if it offers one, or place the silence in the edit (`nar.pause_written`).  
**Best in:** formats: All voiceover and dialogue scripts | genres: All  
**Avoid when:** Writing long run-on sentences without punctuation, which forces the model to rush breathless to the end.  
**Example:** `text: "They dug for seven months. Nothing. Then — beneath thirty cubits of clay... the gold of Ur."` — the engine's explicit pause syntax, for a pause that must be timed, is in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.prompt_tags_pacing`

---

### Breath and Inhalation Insertion

**Also called:** biological breath simulation, humanization markers  
**What it is:** Deliberately inserting breath sounds and natural vocal imperfections into the script flow to destroy synthetic sterility.  
**Effect on the audience:** Signals to the listener's subconscious that a living, breathing human being is delivering the words.  
**Used for and where it works best:** Moments of intense intimacy, terror, exhaustion, or before delivering monumental, grief-stricken news. Write the breath into the script as a direction beside the line; use an inline tag only where the model documents one, otherwise lay a breath in the edit.  
**Best in:** formats: Cinematic Voiceover, Audio Drama, First-Person Memoir | genres: Horror, War, Tragedy, Personal Essay  
**Avoid when:** Fast corporate announcements, upbeat commercial tags, or technical software tutorials; and inline tags on a model that does not read them, which may speak them aloud.  
**Example:** `line: "We were the last ones left inside the temple gates." | direction: a sharp intake of breath before the line` — whether the engine takes this as an inline tag, and its syntax, is in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.breath_insertion`

---

### Phonetic Override for Hard Names

**Also called:** SSML and phonetic override, phoneme correction, foreign name guide  
**What it is:** The fallback strategy for forcing correct pronunciation of ancient, foreign, or complex mythological terms: phonetic respelling in the text first, and a phoneme-level override (IPA, a phoneme tag, or a pronunciation dictionary) only where the model in use supports one. Which model accepts which override is in its adapter in ENGINE-CHECK.md.  
**Effect on the audience:** Eliminates distracting mispronunciations of culturally sacred or historical names (e.g. Ashurbanipal, Enheduanna).  
**Used for and where it works best:** Replace tricky cuneiform and Semitic transliterations with phonetic syllables in the prompt text (e.g., `ash-ur-BAH-nee-pahl`).  
**Best in:** formats: Heritage / Historical Documentary, Factual Essay | genres: Heritage (civilisation-focused), History, Mythology  
**Avoid when:** Standard dictionary words that the model already knows natively.  
**Example:** `text: "The high priestess En-hed-oo-AN-na placed her bronze seal upon the vessel."`  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.ssml_phoneme_fallback`

---

### Seed Pinning for Pick-Ups

**Also called:** deterministic seed locking, audio seed preservation, patch regeneration  
**What it is:** Pinning the generation seed, where the voice engine offers one, so that a regenerated line comes back as close as possible to the takes around it. It is best effort, not a guarantee, so every pick-up is auditioned against its neighbours, at both edit boundaries, before it is cut in; one that still drifts needs a boundary crossfade or a larger regenerated block.  
**Effect on the audience:** Makes surgical replacement of a single misspoken sentence possible with less drift in the pitch, rhythm, or tone of adjacent dialogue. This holds only when the sentence is regenerated inside its surrounding sentences rather than alone: a pinned seed helps hold the voice, but an isolated line still gets the wrong pitch curve (`elevenlabs.chunking_strategy`).  
**Used for and where it works best:** Pick-up takes, fixing typos in long documentary sequences, and matching dialogue lines across multi-take scenes.  
**Best in:** formats: Long-Form Documentary, Narrative Series, Audiobooks | genres: All  
**Avoid when:** Exploring initial creative performances or seeking alternative dramatic options.  
**Example:** `pick-up: "The gates of Nineveh remained shut." | same voice, same model, same settings, seed pinned to the original take's value` — sent with its neighbouring sentences, not alone, per `elevenlabs.chunking_strategy`; the seed parameter is in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.seed_locking`

---

### Paragraph Context Chunking

**Also called:** contextual window flow, multi-sentence coherence  
**What it is:** Feeding text to the synthesizer in cohesive 2-to-3 sentence blocks rather than isolated lines, allowing the model to understand sentence relationships.  
**Effect on the audience:** Produces fluid pitch contours where sentence endings anticipate the following clause instead of falling into repetitive cadence loops.  
**Used for and where it works best:** All narrative voiceover. Send each paragraph whole where it fits in one call; where a line must be generated on its own, pass the sentences before and after it — or the earlier takes — as context if the engine accepts them, so each sentence's pitch curve is set by its neighbours.  
**Best in:** formats: Feature Documentary, Video Essays, Podcasts | genres: Historical, Essay, True Crime  
**Avoid when:** Generating sentence-by-sentence in isolation and stitching them together mechanically, which causes disjointed pitch jumps, or assuming a pinned seed will hide the join: a changed sentence needs its surrounding context or a larger regenerated block, and is approved only after listening across both boundaries.  
**Example:** `chunk: one paragraph per call, split only at a paragraph break; the preceding sentence passed as context for pitch continuity` — the per-call ceiling and the engine's context fields are in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.chunking_strategy`

---

### Audio Mastering and Bitrate Standard

**Also called:** delivery export standard, 48kHz broadcast alignment  
**What it is:** The technical delivery format this phase hands to the edit: 24-bit 48kHz uncompressed WAV, unmastered. The format is the project's choice, fixed here because it decides whether the file can be worked on at all; it is not a claim about what the engine renders — where the engine's output differs, the file is converted once, at delivery, and a file converted to a higher bit depth carries no more detail than the render it came from. **The loudness is not set here** — the take is delivered with its headroom intact and is mastered on the timeline, where the whole piece and its destination are known.  
**Effect on the audience:** Ensures pristine sonic fidelity with zero lossy transcoding artifacts when layered over cinema soundtracks and foley.  
**Used for and where it works best:** Always deliver audio at 48kHz for video timeline synchronization (matching video 24fps/30fps timebases), so the file drops onto the timeline without resampling. Request the engine's uncompressed output at that rate where it offers one; its output formats, and the plan each needs, are in its adapter in ENGINE-CHECK.md.  
**Best in:** formats: Video Production, Film, Broadcast | genres: All  
**Avoid when:** Exporting at 22.05kHz or 128kbps MP3 which causes high-end robotic phase smearing — including by accepting the engine's default output format unchecked. Also avoid delivering a take already normalised or limited to a loudness target — it takes the decision away from the master and cannot be undone.  
**Example:** `export_spec: format: WAV, sample_rate: 48000Hz, bit_depth: 24-bit, headroom intact, loudness set at master time in the edit.`  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
**Yields to:** `mix.lufs_loudness_targets` — Loudness is decided at master time, not at delivery from this phase.  
`elevenlabs.bitrate_and_mastering`

---

### Economic Generation Gateway

**Also called:** free vs paid mode, credit conservation gate  
**What it is:** The pipeline decision gate separating zero-cost script markup from paid API audio synthesis.  
**Effect on the audience:** Allows unlimited creative refinement of timing, WPM, and directing marks without burning generation budget prematurely.  
**Used for and where it works best:** Default to text-only mode: outputs locked script with timing and direction tags. Only trigger the voice engine's paid synthesis when the user explicitly enables paid voice generation — the authorisation is the paid_generation_approved_by line beside the engine record in ENGINE-CHECK.md, and a single test sample is a generation.  
**Best in:** formats: All projects | genres: All  
**Avoid when:** Auto-calling audio generation APIs on rough early drafts.  
**Example:** `mode: "prompts_only" -> returns directed script with marked pauses and WPM; "paid" -> executes the voice engine's synthesis call, only after the user has enabled paid voice generation.` — which calls cost credits, and whether any free allowance exists, is in its adapter in ENGINE-CHECK.md.  
**Source:** reference — the vendor facts behind this card were checked 2026-09-23 and are in the adapter in ENGINE-CHECK.md.  
`elevenlabs.free_vs_paid_gateway`
