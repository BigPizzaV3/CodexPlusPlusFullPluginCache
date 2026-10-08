# Google Lyria 3.5 Engine Craft

14 cards. Directing Google's Lyria 3.5: what to type in the Gemini app, prompt syntax, lengths, lyrics and language, dynamics, modal colour, what comes out and how to deliver it. The Gemini app is the first surface on every card; Gemini API, AI Studio, Flow Music and Vertex AI facts are labelled by surface, and a fact true only of an older Lyria (Lyria 3 / 3 Pro, Lyria 2, Lyria RealTime) is labelled with that model's name.

**Where the facts live (checked 2026-09-23):** each vendor fact is written once, on the card it belongs to, with its official source URL and the date it was read. Access, surfaces, models, length, limits, price and terms of use are on `lyria.foundational_architecture`; prompt syntax on `lyria.semantic_natural_prompting`; lyrics, timestamps and languages (Arabic included) on `lyria.syllable_timing_sync`; tempo on `lyria.controllable_tempo_curves`; inputs on `lyria.conditioning_audio_input`; stems on `lyria.native_multitrack_stems`; output files on `lyria.high_res_broadcast_delivery`; seeds, repeat runs and batching on `lyria.api_batch_synthesis`. The dated verification record is the Lyria adapter in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §7. Every provider figure here is expected to go stale: re-check it against its source before a paid run and at least every 30 days.

---

### Lyria 3.5 Runtime Selection

**Also called:** Lyria 3.5 (Google DeepMind), Google Lyria model adapter, Lyria runtime, full-song music model, text-to-music engine, choosing a full-song music engine for complex scores  
**What it is:** Selecting the Lyria model that is actually available on the surface the project uses, then recording its exact name and verified limits before the first prompt (the engine record, ENGINE-CHECK.md §2). The surfaces are not one runtime: the Gemini app, the Gemini API, Flow Music and Vertex AI offer different Lyria models with different lengths and outputs, and this card does not pretend they are one.  
**Effect on the audience:** Produces musically coherent, emotionally sophisticated compositions that respect formal music theory and subtle instrumental nuances. Google's own claim for 3.5 is "richer, more complex melodic structures", and no Google page documents music-theory correctness, so the result is checked by ear, never assumed from the engine's reputation.  
**Used for and where it works best:** Complex orchestral scores, intricate traditional modal scales, bespoke film compositions, and dynamic video adaptive music.
- **Gemini app (the owner's surface).** The model is Lyria 3.5 (Gemini launch blog, 2026-09-04); the app's Help page calls it only "Lyria". Web and mobile, in every country where the Gemini app works, for users 18 or older, signed in with a personal Google Account or a supported work or school account, with Keep Activity on. Steps: at the bottom of the text box tap **Upload & tools**, then **Create music**; to get a full track, **switch the model to "Pro"**; choose the length, **short (about 1 minute)** or **full (about 2-3 minutes)**; choose vocals or no vocals; optionally pick a genre and instruments from the dropdowns and upload images or videos for context. Each track comes with cover art made by Nano Banana. The Gemini overview page says tracks run "up to three minutes". There is no extend or edit feature in the app (see `lyria.dynamic_energy_progression`).
- **Gemini app limits.** Music generation is ticked for No plan, Google AI Plus, AI Pro and AI Ultra. Google publishes no per-plan track count: the Help page says only that "there are limits" and shows a notice when one is reached. The Lyria 3 launch (2026-02-18) said paid plans get "higher limits". Google does not say which plans can select the Pro model for music. The owner, on Google AI Pro, reports that the Pro model and the Full length work there (2026-09-23).
- **Gemini API and AI Studio.** Model `lyria-3.5`, stable, generally available since 2026-09-03 (API changelog), the model page updated September 2026: tracks of "a couple of minutes", length set only by writing it in the prompt, no duration parameter and no published maximum. `lyria-3-clip-preview` always returns exactly 30 s. Price: `lyria-3.5` $0.08 per song, `lyria-3-pro-preview` $0.08, `lyria-3-clip-preview` $0.04, no free tier. "gemini-lyria-3.5" is not a model name.
- **Flow Music (Google Labs).** Lyria 3.5 launched here first, on 2026-07-29. It takes text, image and audio prompts (upload, or record with the microphone), has the Remix tools Extend, Cover and Replace, and downloads several songs as a .zip. The Lyria 3.5 model card (2026-07-29) lists Flow Music, plus API access for downstream providers, as its channels; it predates the Gemini launch, which added the Gemini app, the API, AI Studio and Google Vids, so the two pages disagree.
- **Vertex AI: no Lyria 3.5.** Vertex offers `lyria-3-pro-preview` (maximum 184 s) and `lyria-3-clip-preview` (30 s), both Preview since 2026-03-25, and `lyria-002` (Lyria 2, generally available): 30-s instrumental clips, prompts in US English only.
- **Lyria RealTime** (`models/lyria-realtime-exp`, experimental, Gemini API) streams instrumental music and has its own fields: `bpm` 60-200, `density` and `brightness` 0.0-1.0, `scale` (12 values plus unspecified), `guidance` 0-6 (default 4.0), `temperature` 0-3 (default 1.1), `top_k` 1-1000 (default 40), `seed`, `mute_bass`, `mute_drums`, `only_bass_and_drums`, and `music_generation_mode` QUALITY / DIVERSITY / VOCALIZATION (wordless voice as an instrument). These are RealTime fields only, not Lyria 3.5 settings.
- **Not the same model.** Lyria 3.5 is not Lyria 3 Pro: Google says 3.5 adds more expressive vocals, better pronunciation and lyrics, and control over tempo and duration. The model card describes the architecture as "latent diffusion, applied to temporal audio latents".
- **Watermark and rights.** Every Lyria 3.x track carries a SynthID watermark; in the Gemini app you can upload a file and ask whether it was made with Google AI. Vertex Lyria 3 also adds C2PA content credentials. Google's Terms say Google "won't claim ownership" of original content you generate, and forbid using AI output to build machine-learning models. The Gemini app pages say nothing about commercial use or monetising the music; Vertex Lyria 3 Preview terms explicitly allow production and commercial use. Naming an artist is treated as broad creative inspiration, not imitation; the API blocks prompts that ask for "specific artist voices or the generation of copyrighted lyrics"; the Generative AI Prohibited Use Policy forbids IP infringement, deceptive impersonation of a real person, passing AI output off as solely human-made to deceive, and sexual content made for gratification.  
**Best in:** formats: Film Score, Heritage Epic, Documentary Soundtrack, Classical / World | genres: All  
**Avoid when:** Quick, formulaic 3-chord commercial pop loops where simple engines suffice. And do not carry a figure from one surface to another: the 30-s clip, the 184-s Pro preview and the Gemini app's 1-minute and 2-3-minute lengths belong to different models.  
**Prompt:** `Create a full song (about 3 minutes): monumental Mesopotamian orchestral score in Maqam Bayati colour, solo acoustic oud leading over low strings and frame drums, 88 BPM, instrumental only.` (Gemini app: Create music, model set to Pro, length Full, vocals off.)  
**Example:** `engine record: Lyria 3.5, Gemini app, model Pro, length Full, vocals off, checked 2026-09-23 | API equivalent: model="lyria-3.5", the same prompt text.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Gemini launch blog https://blog.google/innovation-and-ai/products/gemini-app/better-tracks-lyria-gemini/ ; Flow Music launch blog https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/ ; Gemini overview https://gemini.google/overview/music-generation/ ; Gemini Apps Help https://support.google.com/gemini/answer/16901237 ; Gemini plan limits https://support.google.com/gemini/answer/16275805 ; Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; model page https://ai.google.dev/gemini-api/docs/models/lyria-3.5 ; API changelog https://ai.google.dev/gemini-api/docs/changelog ; pricing https://ai.google.dev/gemini-api/docs/pricing ; Flow Music Help https://support.google.com/flow/answer/17084348 ; Lyria 3.5 model card https://deepmind.google/models/model-cards/lyria-3-5/ ; Vertex Lyria 3 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3 ; Vertex Lyria 2 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-002 ; Lyria RealTime https://ai.google.dev/gemini-api/docs/realtime-music-generation ; Lyria 3 in Gemini blog https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/ ; Lyria 3 Pro blog https://blog.google/innovation-and-ai/technology/ai/lyria-3-pro/ ; Google Terms https://policies.google.com/terms ; Prohibited Use Policy https://policies.google.com/terms/generative-ai/use-policy  
**Shelf life:** dated — an engine claim, checked 2026-09-23; re-check against the sources before a paid run and at least every 30 days; review 2027-03.  
`lyria.foundational_architecture`

---

### Semantic Natural Language Music Prompting

**Also called:** natural language music directing, emotional descriptor prompt, directing music by the scene's meaning, Lyria prompt formula  
**What it is:** Translating the approved music brief into descriptive language for Lyria 3.5 — which instrument, what mood, how it changes over time — in specific words rather than a string of empty adjectives. The scene arc and the musical choices stay with the generic craft cards; this card dresses them in Lyria's own prompt shape.  
**Effect on the audience:** The music captures deep psychological nuances, shifting organically like a bespoke live film score tailored to the scene's emotional subtext.  
**Used for and where it works best:** Directing Lyria to mirror complex scene arcs (e.g. "A slow, mournful flute melody that gradually gathers hope as dawn breaks over the ancient city").
- **Google's formula** (Vertex prompt guide and the Lyria 3 Pro prompting guide): genre and style, then mood, instrumentation, tempo and rhythm, vocal style and language, then the lyrics. Optional additions: arrangement ("starts with solo piano, then strings enter"), soundscape ("rain falling"), production quality ("vintage recording", "clean mix").
- **Gemini API guide for 3.5:** "Mention instruments, BPM, key, mood, and structure for the best output"; use section tags; separate the lyrics from the musical instructions; prompt in the language you want the lyrics in; iterate on the Clip model first. The Lyria prompt guide: "Both short and detailed prompts produce strong results"; "Lead your prompt with the primary genre"; it gives its own genre, instrument and mood keyword lists.
- **Gemini app tips** (Help page and Google's 6 tips for Lyria 3, 2026-02-23): start with "write", "compose" or "create"; name a genre and an era; describe the voice — gender, range, timbre such as "breathy" or "gravelly"; describe the dynamics; give your own lyrics after `Lyrics:` or let Gemini write them.
- **Exclusions are written in the prompt.** There is no negative-prompt setting on Lyria 3.x: Vertex lists Lyria 3 "Negative prompting: Not supported", and Lyria 3.5 documents none. Only `lyria-002` (Lyria 2, Vertex) takes a `negative_prompt` field. The Vertex prompt guide still shows a negative-prompt section under general Lyria, so Google's pages disagree; for 3.5 write what you want ("Instrumental only", "no drums").  
**Best in:** formats: Film Score, Documentary Feature, Drama Series | genres: Drama, History, Epic  
**Avoid when:** Using robotic keyword spam (e.g. "epic, cool, music, nice, drums, best") which produces generic stock music. The fault is vagueness, not the list form: Google publishes keyword lists and says short and detailed prompts both work, so a specific list that names instrument, mode, tempo and change is fine.  
**Prompt:** `Compose a cinematic Near Eastern score: a solitary reed ney flute improvises over an unhurried, warm cello drone, evoking centuries of desert memory, slow tempo around 72 BPM, in D minor, building to a majestic cadence. Instrumental only.`  
**Example:** `prompt: "A solitary reed Ney flute improvises over an unhurried, warm cello drone, evoking centuries of desert memory, building to a majestic cadence."`  
**Source:** vendor — Google's official pages, read 2026-09-23: Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide ; Vertex prompt guide https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide ; Lyria 3 Pro prompting guide https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-lyria-3-pro ; Gemini Apps Help https://support.google.com/gemini/answer/16901237 ; 6 tips for Lyria 3 https://blog.google/products-and-platforms/products/gemini/tips-prompting-lyria-3/ ; Vertex Lyria 3 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3 ; Vertex Lyria 2 reference https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/lyria-music-generation  
**Shelf life:** provider syntax verified 2026-09-23; re-check the prompt guides before execution and at least every 30 days.  
`lyria.semantic_natural_prompting`

---

### Conditioning Audio & Hum-to-Score

**Also called:** audio conditioning, melody humming input, reference audio seed, carrying a melody the director already has  
**What it is:** Supplying an owned reference-audio input only when the exact selected model and interface officially accept audio input. Record the supported MIME type and duration at execution; otherwise route the melody to notation or a text description rather than inventing a hum-to-score endpoint. Record the melody first either way: it is the reference the result is judged against.  
**Effect on the audience:** Turns an intuitive human melodic idea into a fully orchestrated, world-class symphonic or folk arrangement that still carries the director's tune.  
**Used for and where it works best:** When the director has a specific original melody in mind that text prompts cannot adequately describe.
- **Gemini app:** no audio input. The Help page offers images or videos "for added context"; the Gemini overview page for 3.5 names text, photo or a template, and does not mention video, so the two pages disagree on video. (Lyria 3 in Gemini, February 2026, took a photo or a video.)
- **Gemini API `lyria-3.5`:** inputs are "Text and Image", up to 10 images; no audio. **Vertex Lyria 3:** text plus up to 10 images or PDFs; no audio.
- **Flow Music is the surface that takes audio:** a microphone recording or your own audio file, and the Remix tools Extend, Cover and Replace act on a selected section of a song. Google's page does not say what each Remix tool does, the accepted formats or a maximum duration, so record those at execution.
- Where audio is not accepted, write the melody out as notes and rhythm in the prompt (`score.character_leitmotif_binding`) or have a player record it (`audio_exec.music_tracking`).  
**Best in:** formats: Original Theme Songs, Leitmotif Creation, Bespoke Score | genres: All  
**Avoid when:** Feeding distorted, noisy cell phone audio with screaming background noise as the conditioning input.  
**Prompt:** `Gemini app or API: Create a song for full Near Eastern chamber ensemble built on this melody: D E-half-flat F G A, G F E-half-flat D, in 6/8, each phrase ending on a long D. Keep this tune as the main theme.`  
**Example:** `capability_check: audio input supported by selected model and interface (Flow Music: yes, microphone or upload; Gemini app and API: no) | reference: 10-second hummed recording, kept on file | input: the owned melody in the documented format; otherwise notation plus text.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Gemini Apps Help https://support.google.com/gemini/answer/16901237 ; Gemini overview https://gemini.google/overview/music-generation/ ; model page https://ai.google.dev/gemini-api/docs/models/lyria-3.5 ; Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; Vertex Lyria 3 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3 ; Flow Music Help https://support.google.com/flow/answer/17084348 ; Lyria 3 in Gemini blog https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/  
**Shelf life:** provider capability verified 2026-09-23; recheck official model and API documentation immediately before execution.  
**Yields to:** `lyria.semantic_natural_prompting` — The only reference audio is too noisy to seed.  
`lyria.conditioning_audio_input`

---

### Stem Delivery Handoff

**Also called:** isolated-track delivery, post-generation stem route, discrete stem output, isolated instrument tracks, multitrack music delivery  
**What it is:** Getting the music out as separate stems (Drums/Percussion, Bass, Lead Melody, Harmony/Pads, Vocals), in phase with each other, rather than as one flattened stereo file. Request stems only when the selected Lyria interface explicitly documents native stem output. Current official model cards do not establish a universal `multi_stem_output` flag; otherwise export the documented mix and route an approved derivative through a disclosed stem-separation or DAW workflow.  
**Effect on the audience:** Allows surgical mixing and dynamic ducking in video post-production; music elements never clash with voiceover.  
**Used for and where it works best:** Professional video post-production, interactive video games, and film re-recording mixes. **Lyria 3.5 returns no stems on any surface** — no official page for any Lyria version offers stems or multitrack output; the Gemini app gives one MP3 or MP4 and the API one audio file plus the lyrics text. The nearest thing is Lyria RealTime's `mute_bass`, `mute_drums` and `only_bass_and_drums` (listed on `lyria.foundational_architecture`), which steer a live stream and are not stems. So separate the mix (`song_handoff.stem_separation_protocol`) or track the parts live (`audio_exec.music_tracking`), and say in the handoff how each stem was made.  
**Best in:** formats: All video production | genres: All  
**Avoid when:** Treating inferred stems as lossless original tracks or promising phase-perfect isolation before the endpoint proves it. And do not export a single flattened file when independent stems are genuinely available.  
**Example:** `capability_check: native stems documented? Lyria 3.5, 2026-09-23: no | deliver: the source mix plus labelled derived stems (lead, bass, percussion, chords) from the approved separation stage, each file named with how it was made.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; model page https://ai.google.dev/gemini-api/docs/models/lyria-3.5 ; Gemini Apps Help https://support.google.com/gemini/answer/16901237 ; Lyria RealTime https://ai.google.dev/gemini-api/docs/realtime-music-generation  
**Shelf life:** provider capability verified 2026-09-23; recheck before promising deliverables.  
`lyria.native_multitrack_stems`

---

### Zero-Shot Stylistic Hybridization

**Also called:** cross-genre fusion, stylistic collision, genre blending  
**What it is:** Blending two historically disparate musical traditions (e.g. Ancient Sumerian temple chants + Modern ambient downtempo electronic) with organic coherence.  
**Effect on the audience:** Creates a striking, unforgettable contemporary aesthetic that appeals to modern global audiences while honoring ancient roots.  
**Used for and where it works best:** Cutting-edge heritage campaigns, museum experiential exhibits, and modern cinematic trailers. Google's Lyria prompt guide documents genre fusion in plain words, for example "A fusion of metal and hip-hop" and "Classical chamber music with dark electronic drone elements"; put the primary genre first.  
**Best in:** formats: Modern Trailer, Artistic Video, High-Impact Reel | genres: Hybrid, Electronic Folk, Epic  
**Avoid when:** Pure archaeological historical reconstructions aiming for strict textbook accuracy.  
**Prompt:** `Create a trip-hop track: seamless fusion of authentic 7th century BC Assyrian frame drum rhythms with modern ambient trip-hop basslines and analog synth pads, 90 BPM, instrumental only.`  
**Example:** `fusion_prompt: "Seamless fusion of authentic 7th century BC Assyrian frame drum rhythms with modern ambient trip-hop basslines and analog synth pads."`  
**Source:** vendor — Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide , read 2026-09-23.  
**Shelf life:** provider vocabulary verified 2026-09-23; re-check the prompt guide before execution and at least every 30 days.  
**Yields to:** `score.microtonal_quarter_tone_tension` — Strict period reconstruction, no modern layer.  
`lyria.stylistic_hybridization`

---

### Syllable Timing & Metric Synchronization

**Also called:** metric lyric mapping, text-to-vocal synchronization, Lyria lyrics and language  
**What it is:** Directing Lyria to bind specific lyric syllables to exact musical timecode positions, preventing rushed or dragged vocal lines — won in the lyric sheet and checked in the take.  
**Effect on the audience:** Ensures pristine poetic prosody; every rhyme and metric foot lands on the musical downbeat with absolute naturalness.  
**Used for and where it works best:** Setting classical Arabic poems (Qasida), Mesopotamian hymns, or complex multi-meter lyrics to music. Mark the stresses in the writing (`lyr.prosody`).
- **Lyrics.** Lyria 3.5 sings and structures songs into verses, choruses and bridges. Give your own words under a `Lyrics:` line with section tags — the guides show `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Verse 2]`, `[Bridge]`, `[Outro]` — and backing vocals in (parentheses), kept clearly apart from the musical direction; or let the model write them (the API returns them as text in `output_text`). The Gemini overview page says your own text can carry structure tags like `[Verse 1]`.
- **Timing.** Google documents section-level timing: timestamps such as `[0:00 - 0:10] Intro: ...` or `[mm:ss]`, and phrases such as "Chorus kicks in at 22 seconds"; the Vertex guide also shows intensity as `Intensity: 1/10 (Very Low)`. All of it is prompt text, not a setting. Binding single syllables to beats is not documented by Google, so check the take line by line.
- **Languages.** "Lyria 3.5 generates lyrics in the language of your prompt" (API guide, example French); Google publishes no language list for 3.5. Lyria 3 / 3 Pro name eight: English, German, Spanish, French, Hindi, Japanese, Korean, Portuguese. The long language menu on the Gemini Help page is the Help Center's own page-language menu, not a Lyria list.
- **Arabic.** Google's MENA blog (2026-02-19) says Lyria 3 in Gemini was "available in Arabic (beta version)", for 30-s tracks. No Lyria 3.5 page and neither the API nor the Vertex language list mentions Arabic. The owner reports that Lyria 3.5 in the Gemini app takes the prompt in English or in Arabic and sings the Arabic lyrics it is given (2026-09-23): a tested fact, not a documented one, so each take is still checked by ear like any language. None of the Google pages checked names Sureth or Syriac.  
**Best in:** formats: Traditional Song, Opera, Classical Choral | genres: Classical, Heritage, Hymn  
**Avoid when:** Casual improvisational jazz scatting where loose timing is intended.  
**Prompt:** `Create a slow classical Arabic song in 6/8, solo male voice, oud and qanun. [0:00 - 0:15] Intro: solo oud. [0:15 - 1:00] Verse 1: voice enters, one syllable per beat. Lyrics: [Verse 1] (the qasida lines, stressed syllables in capitals) [Chorus] (the refrain lines)`  
**Example:** `metric_map: Syllables matched to 6/8 rhythmic meter, with stressed consonants landing on beats 1 and 4; section timings written as [0:15 - 1:00] Verse 1.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide ; Vertex prompt guide https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide ; Gemini overview https://gemini.google/overview/music-generation/ ; Vertex Lyria 3 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3 ; Lyria 3 in Gemini blog https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/ ; Google MENA blog https://blog.google/intl/en-mena/product-updates/explore-get-answers/lyria-3-arabic-google-gemini-ramadan/  
**Shelf life:** provider language and syntax verified 2026-09-23, Arabic tested by the owner the same day; re-check at least every 30 days and whenever the model changes.  
**Yields to:** `lyria.controllable_tempo_curves` — The timing is meant to float, improvised.  
`lyria.syllable_timing_sync`

---

### Controllable Tempo Curves & Rubato

**Also called:** tempo rubato, dynamic accelerando, organic human timing  
**What it is:** Directing Lyria to introduce natural human tempo flexibility (rubato, accelerando, ritardando) rather than locking to a rigid, mechanical digital click track.  
**Effect on the audience:** Infuses the music with deep human soul and breath; feels like a live master musician speeding up with passion and slowing with sorrow.  
**Used for and where it works best:** Solo instrumental improvisations (Taqsim), emotional opera arias, and dramatic scene transitions. Tempo is written in the prompt, not set by a control: "Set the tempo directly (e.g. 120 BPM)" (Flow Music launch blog), "slow tempo around 72 BPM" (Lyria prompt guide); Google lists tempo control among 3.5's improvements. A changing tempo is not documented by Google, so ask for the curve and listen; where the take holds one tempo, write the curve as timed sections and join them (`song_handoff.extended_suite_linking`), or record the free-time solo with a player (`audio_exec.music_tracking`). A numeric `bpm` field exists only on Lyria RealTime.  
**Best in:** formats: Instrumental Solo, Film Drama, Heritage Piece | genres: Classical, Folk, Drama  
**Avoid when:** High-energy electronic dance tracks requiring locked quantization for DJ mixing.  
**Prompt:** `Compose a solo oud taqsim with free, breathing timing: start at a contemplative 72 BPM rubato; gradually accelerate to 108 BPM during the central celebration; decelerate to 68 BPM at close. Instrumental only.`  
**Example:** `tempo_curve: "Start at a contemplative 72 BPM rubato; gradually accelerate to 108 BPM during the central celebration; decelerate to 68 BPM at close." — fallback: the same three tempos as three timed sections, joined.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Flow Music launch blog https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/ ; Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide ; Lyria RealTime https://ai.google.dev/gemini-api/docs/realtime-music-generation  
**Shelf life:** provider syntax verified 2026-09-23; re-check before execution and at least every 30 days.  
`lyria.controllable_tempo_curves`

---

### Spatial Acoustic Staging & Placement

**Also called:** virtual room acoustics, 3D orchestra placement, soundstage depth  
**What it is:** Specifying the simulated acoustic environment: room volume, reverberation time, microphone distance, and virtual instrument stage positions.  
**Effect on the audience:** Gives the track tangible physical reality; the viewer can close their eyes and point to where the Oud player and the drum are sitting.  
**Used for and where it works best:** Ancient palace simulations, multi-source intimate campfire folk recordings, and grand cathedral performances. For intimate folk, stage the direct close-mic signal first and add only the short natural ambience needed to locate the other performers; this does not require a long artificial reverb tail. Google's guides show space as texture words ("reverb-soaked vocals", a "vintage recording" or "clean mix"); exact decay times and distances are not documented, so write them, listen, and set any figure the take misses in the mix (`mix.convolution_ir_matching`).  
**Best in:** formats: Theatrical Feature, Heritage Documentary, VR/XR | genres: Heritage, Classical, Ambient  
**Avoid when:** Flat, bone-dry modern pop radio mixes with zero acoustic depth.  
**Prompt:** `Create a sacred instrumental piece recorded in a large stone temple: 2.8s natural decay, solo oud 3 meters front-center, choir wide at the rear, reverb-soaked and distant.`  
**Example:** `acoustic_spec: "Large stone temple: 2.8s natural decay, solo Oud 3 meters front-center, choir wide rear." Intimate branch: "close direct Oud at the soundboard, other players one meter around it, short outdoor or small-room ambience, no added digital reverb tail."`  
**Source:** vendor — Google's official pages, read 2026-09-23: Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide ; Vertex prompt guide https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide  
**Shelf life:** provider syntax verified 2026-09-23; re-check before execution and at least every 30 days.  
`lyria.spatial_acoustic_staging`

---

### Dynamic Energy Progression Prompting

**Also called:** dynamic arc directing, symphonic crescendo, energy envelope  
**What it is:** Structuring the prompt to govern musical density and volume across time: intimate solo -> gradual string entry -> monumental brass climax -> quiet decay.  
**Effect on the audience:** Synchronizes the musical score perfectly with the 3-act narrative arc of the video; multiplies emotional catharsis tenfold.  
**Used for and where it works best:** Composing the master score for short films, documentaries, and trailer climaxes. The timings are the cue's, set by the picture. Google documents the arc in words — "Gradual crescendo throughout the song, adding one instrument per section" — and in timestamped sections (syntax on `lyria.syllable_timing_sync`). The length one generation returns is on `lyria.foundational_architecture`; a cue longer than that is built in sections and joined (`song_handoff.extended_suite_linking`). **Extending a track is a Flow Music feature only** (Remix, Extend): the Gemini app Help page names no extend or edit feature, and the API says "Music generation is a single-turn process".  
**Best in:** formats: Film Score, Trailer, Documentary Feature | genres: Epic, Drama, Action  
**Avoid when:** Uniform background music beds that need to maintain constant low-level volume throughout.  
**Prompt:** `Create a full-length orchestral score (about 3 minutes). [0:00 - 1:00] whispered solo flute. [1:00 - 2:15] rhythmic war drums join. [2:15 - 2:45] massive full orchestral climax. [2:45 - 3:00] solitary fading cello. Gradual crescendo, adding one instrument per section. Instrumental only.`  
**Example:** `energy_arc: "Minutes 0:00-1:00: Whispered solo flute; Minutes 1:00-2:30: Rhythmic war drums join; Minutes 2:30-3:15: Massive full orchestral climax; 3:15-3:40: Solitary fading cello." — a 3:40 cue is longer than the Gemini app's full length, so it is built in two joined sections or extended in Flow Music.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide ; Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; Gemini Apps Help https://support.google.com/gemini/answer/16901237 ; Flow Music Help https://support.google.com/flow/answer/17084348  
**Shelf life:** provider capability verified 2026-09-23; re-check before execution and at least every 30 days.  
**Yields to:** `score.minimalist_suspense_drone` — The cue must hold one level under narration.  
`lyria.dynamic_energy_progression`

---

### High-Resolution Broadcast Delivery

**Also called:** broadcast export standard, uncompressed master output, Lyria output formats  
**What it is:** Taking the music from Lyria in the best form it offers and delivering it at the project's chosen master format, with no further lossy encode anywhere in between.  
**Effect on the audience:** Delivers pristine audiophile clarity, massive dynamic range, and clean high frequencies that shine on high-end theater sound systems.  
**Used for and where it works best:** Theatrical cinema releases, broadcast television compliance, and professional Blu-ray mastering.
- **Gemini app:** download the MP4 video with cover art, or the MP3 audio only; no WAV option is mentioned. Take the MP3.
- **Gemini API `lyria-3.5`:** 44.1 kHz stereo, MP3 by default; the guide says WAV is available "for Lyria 3.5" through `response_format`, while the model page lists MP3 output only, so the two pages disagree — ask for WAV and check what arrives.
- **Vertex Lyria 3:** audio/mp3, 44.1 kHz, 192 kbps (the AI Studio page for 3 Pro says 48 kHz, a disagreement). **Lyria 2 (`lyria-002`):** WAV at 48 kHz. **Lyria RealTime:** raw 16-bit PCM at 48 kHz.
- **Flow Music:** a file-format choice at download; Google's page does not list the formats.
- Bit depth is not documented for Lyria 3.5, and no page mentions 96 kHz. A compressed engine file is the quality ceiling, and converting it upward adds nothing, so say so in the handoff; the project's delivery format is reached in the edit (`mix.stems_export_standard`).  
**Best in:** formats: All professional production | genres: All  
**Avoid when:** Exporting low-bitrate compressed preview files for final release.  
**Example:** `delivery: Gemini app — the MP3, flagged "lossy source"; API — response_format WAV where it arrives, otherwise the MP3 flagged "lossy source"; project master: WAV, 48000Hz, 24-bit, uncompressed PCM — the project's delivery choice, converted in the edit; headroom intact — the peak ceiling is set at master time in the edit.`  
**Source:** vendor — Google's official pages, read 2026-09-23: Gemini Apps Help https://support.google.com/gemini/answer/16901237 ; Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; model page https://ai.google.dev/gemini-api/docs/models/lyria-3.5 ; Vertex Lyria 3 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3 ; AI Studio Lyria 3 Pro page https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview ; Vertex Lyria 2 reference https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/lyria-music-generation ; Lyria RealTime https://ai.google.dev/gemini-api/docs/realtime-music-generation ; Flow Music Help https://support.google.com/flow/answer/17084348  
**Shelf life:** provider export snapshot verified 2026-09-23; re-verify available bit depth, sample rates and formats against current provider documentation before execution and at least every 30 days.  
`lyria.high_res_broadcast_delivery`

---

### Intimate Acoustic Folk Proximity

**Also called:** campfire acoustics, porch recording feel, living room folk  
**What it is:** Prompting Lyria to simulate close-mic, un-produced, organic acoustic performances with audible finger squeaks, wood taps, and breath warmth.  
**Effect on the audience:** Creates an overwhelming sense of human honesty, vulnerability, and ancient oral tradition; strips away synthetic artifice.  
**Used for and where it works best:** Intimate personal memoirs, ancestral folk songs, and humble village scenes. Google's own example of this texture is "dry, intimate acoustic guitar"; fret squeaks are not in its guide, so listen for them in the take.  
**Best in:** formats: Cultural Documentary, Folk Album, Memoir Short | genres: Folk, Heritage, Acoustic  
**Avoid when:** Massive high-tech industrial action blockbusters.  
**Prompt:** `Create an intimate folk instrumental: solo wooden oud, dry and intimate, recorded close to the soundboard with warm wood resonance and subtle fret squeaks, zero digital reverb, slow tempo around 66 BPM.`  
**Example:** `prompt: "Intimate acoustic solo wooden Oud, recorded close to the soundboard with warm wood resonance and subtle fret squeaks, zero digital reverb."`  
**Source:** vendor — Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide , read 2026-09-23.  
**Shelf life:** provider vocabulary verified 2026-09-23; re-check the prompt guide before execution and at least every 30 days.  
`lyria.intimate_acoustic_proximity`

---

### Classical Arabic Qasida Orchestration

**Also called:** formal Arabic ode, classical qasida score, courtly orchestra  
**What it is:** Composing an elevated, majestic orchestral arrangement to accompany formal Arabic poetry (Qasida) in classical meters.  
**Effect on the audience:** Commands royal dignity, literary prestige, and deep cultural reverence across the Arab world.  
**Used for and where it works best:** Recitations of classic pre-Islamic and Abbasid poetry, royal historical drama, and national cultural anthems. No maqam and no Arabic percussion appear in Google's Lyria keyword lists, and its key guidance is Western ("in G major", "in D minor"), so name the maqam and instruments and describe how they should sound too; where the mode is missing from the take, `score.microtonal_quarter_tone_tension` routes it. Sung Arabic works on Lyria 3.5 in the Gemini app by the owner's test, though Google does not document it (the language facts are on `lyria.syllable_timing_sync`).  
**Best in:** formats: Historical Epic, Cultural Celebration, Literary Feature | genres: Heritage (civilisation-focused), Classical, Literature  
**Avoid when:** Casual modern street slang or contemporary pop songs.  
**Prompt:** `Compose a grand classical Arabic orchestral accompaniment in Maqam Rast, majestic strings, qanun and oud, traditional percussion (riq and mazhar), solemn and regal, 76 BPM. Instrumental only.`  
**Example:** `prompt: "Grand classical Arabic orchestral accompaniment in Maqam Rast, majestic strings, traditional percussion (Riq and Mazhar), solemn and regal."`  
**Source:** vendor — Lyria prompt guide https://ai.google.dev/gemini-api/docs/lyria-prompt-guide , read 2026-09-23.  
**Shelf life:** provider vocabulary verified 2026-09-23; re-check the prompt guide before execution and at least every 30 days.  
`lyria.qasida_orchestration`

---

### Epic Battle Choral Invocations

**Also called:** war choir, epic choral brass, battle liturgy  
**What it is:** Massive polyphonic choral chants sung in low registers, doubled by heavy brass and booming bronze percussion.  
**Effect on the audience:** Evokes terrifying epic scale, clash of empires, and cosmic historical struggle.  
**Used for and where it works best:** Monumental battle scenes, army mobilization, and catastrophic civilizational turning points. The tempo goes into the prompt as text (`lyria.controllable_tempo_curves`).  
**Best in:** formats: Feature Film, Cinematic Trailer, Action Game | genres: War, Epic, Action  
**Avoid when:** Quiet domestic dialogue or comedic scenes.  
**Prompt:** `Create an epic battle choral piece: deep male choir chanting in archaic syllables over thunderous frame drums, low brass stabs, and rising dissonant strings, 108 BPM, in D minor.`  
**Example:** `prompt: "Deep male choir chanting in archaic syllables over thunderous frame drums, low brass stabs, and rising dissonant strings, tempo: 108 BPM."`  
**Yields to:** `score.minimalist_suspense_drone` — The scene is quiet, domestic or comic.  
`lyria.battle_choral_invocations`

---

### Batch Music Generation & Audition

**Also called:** programmatic music generation, batch audition pipeline, API batch music synthesis and iteration  
**What it is:** Generating several contrasting interpretations of one cue as separate runs, after spend approval (ENGINE-CHECK.md §2), and auditioning them side by side before choosing the master.  
**Effect on the audience:** Enables the creative team to audition 5 completely different musical interpretations of a scene before choosing the definitive master.  
**Used for and where it works best:** Professional production pipelines requiring fast, high-volume creative iteration. Each option is its own full request with the target length written into it.
- **Gemini app:** the Help page documents no seed and no batch option; each Create music run is its own request.
- **Gemini API `lyria-3.5`:** "Batch API", "Flex inference" and "Priority inference" are all "Not supported" (model page), so each option is a separate call; no seed is documented, and "Results may vary between calls, even with the same prompt"; generation is single-turn, so an earlier result cannot be refined. Google advises iterating on `lyria-3-clip-preview` (30 s, cheaper; prices on `lyria.foundational_architecture`) before the full model. **Vertex Lyria 3:** 1 clip per prompt. **Lyria 2 (`lyria-002`):** `sample_count` up to 4 clips and a `seed`, which cannot be combined.
- Save each chosen run with its prompt and date at once, since a rerun will not reproduce it.  
**Best in:** formats: Commercial Production, Fast Turnaround Digital Video | genres: All  
**Avoid when:** Manual one-off acoustic studio recordings.  
**Example:** `audition: separate runs of one cue brief — variation_folk, variation_orchestral, variation_ambient — each a full request to model="lyria-3.5" (or one Create music run each in the Gemini app), target length written into each prompt, spend approved, each kept take saved with its prompt and date.`  
**Source:** vendor — Google's official pages, read 2026-09-23: model page https://ai.google.dev/gemini-api/docs/models/lyria-3.5 ; Gemini API guide https://ai.google.dev/gemini-api/docs/music-generation ; Vertex Lyria 3 https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3 ; Vertex Lyria 2 reference https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/lyria-music-generation  
**Shelf life:** provider API snapshot verified 2026-09-23; recheck the official request schema immediately before execution.  
`lyria.api_batch_synthesis`
