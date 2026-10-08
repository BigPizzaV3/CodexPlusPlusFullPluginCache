# Production Execution: Audio, Voice & Recording

9 cards. Execution standards for live and generative audio sessions, studio capture, voice isolation, foley performance, and spatial audio capture.

---

### Narration Recording Session

**Also called:** voiceover capture session, narrator recording, P13X-AUD-01  
**What it is:** Conducting an approved narration recording with controlled performance, pronunciation, timing, and clean acoustic source quality.  
**Effect on the audience:** Delivers a pristine, intelligible voice track with organic performance continuity and zero technical distractions.  
**Used for and where it works best:** Final locked scripts where pronunciation guides, character authority, and delivery targets are fully defined.  
**Best in:** formats: Feature Film, Documentary Feature, Narrative Podcast, Commercial | genres: All  
**Avoid when:** Performance is forced to fit an unmeasured time estimate, or script revisions are being improvised during recording.  
**Example:** `session: dry booth capture at 24-bit 48kHz, script revision locked, phonetic guide active for all foreign names.`  
**Yields to:** `record.live_capture` — The spoken source happens once, a lecture or a liturgy, and cannot be re-taken.  
`audio_exec.narration_session`

---

### Dialogue & Ensemble Recording

**Also called:** cast ensemble session, multi-mic dialogue tracking, P13X-AUD-02  
**What it is:** Capturing interaction, emotional overlap, spatial relation, and performance continuity across several distinct voices.  
**Effect on the audience:** Creates living conversational chemistry where characters genuinely listen, interrupt, and react to one another.  
**Used for and where it works best:** Multi-character narrative drama, comedic banter scenes, and podcast roundtables.  
**Best in:** formats: Audio Drama, Feature Film, Drama Series Episode | genres: Drama, Comedy, Thriller  
**Avoid when:** Over-isolation kills character interaction, or uncontrolled microphone bleed destroys the possibility of editing.  
**Example:** `setup: matched large-diaphragm condensers with optical baffles, tracking simultaneous live character dialogue.`  
**Yields to:** `record.live_capture` — The performance is a one-time live event rather than a directed take.  
`audio_exec.dialogue_ensemble`

---

### Music Tracking & Stem Session

**Also called:** score tracking session, instrument tracking, P13X-AUD-03  
**What it is:** Recording instruments or voices in discrete layers or ensembles while preserving musical timing, tone, and emotional intent.  
**Effect on the audience:** Provides a rich, dynamic musical underscore that can be ducked or shaped dynamically without competing with speech.  
**Used for and where it works best:** Composing and tracking original acoustic or hybrid scores with independent melodic and drone stems.  
**Best in:** formats: Feature Film, High-End Documentary, Trailer | genres: All  
**Avoid when:** Click track rigidity destroys natural human rubato, or irreversible reverb is baked into the recorded master.  
**Example:** `arrangement: recording solo Oud and frame drum on separate tracks at 96kHz for dynamic post-mix ducking.`  
**Yields to:** `record.live_capture` — The music is a concert or ceremony that will not be performed again.  
`audio_exec.music_tracking`

---

### Field & Environmental Ambience Recording

**Also called:** wild track recording, location atmosphere capture, P13X-AUD-04  
**What it is:** Capturing location sound, atmosphere, acoustic impulse, texture, or environmental evidence directly at the real-world source.  
**Effect on the audience:** Imparts documentary truth and geographic specificity that library stock sounds cannot replicate.  
**Used for and where it works best:** Archaeological excavation sites, marshlands, desert winds, and historic architectural spaces.  
**Best in:** formats: Documentary Feature, Heritage Film, Travel Essay | genres: Heritage (civilisation-focused), Nature  
**Avoid when:** Wind buffeting or handling noise destroys the recording, or uncontrolled background traffic contaminates an ancient setting.  
**Example:** `field_rig: stereo binaural microphones with Rycote wind protection, recording dawn breeze across Euphrates reed beds.`  
`audio_exec.field_ambience`

---

### Foley & Designed Effects Performance

**Also called:** practical foley performance, tactile effect creation, P13X-AUD-05  
**What it is:** Creating custom physical sound through performed action with real props, textured surfaces, and specialized acoustic materials.  
**Effect on the audience:** Gives every on-screen action believable weight, tactile presence, and emotional consequence.  
**Used for and where it works best:** Footsteps, textile movements, weapon handling, ancient tool manipulation, and door mechanics.  
**Best in:** formats: Film, Series, Animation, Documentary | genres: All  
**Avoid when:** Literal imitation replaces expressive dramatic function, or effects are performed without reference to image sync.  
**Example:** `props: cut reeds pressing into soft river clay, matching on-screen cuneiform scribe stylus movements.`  
`audio_exec.foley_performance`

---

### Spatial Audio & Binaural Capture

**Also called:** 3D audio recording, ambisonics capture, P13X-AUD-06  
**What it is:** Recording or constructing directional, ambisonic, binaural, or multichannel sound fields for immersive headphone and theater playback.  
**Effect on the audience:** Places the listener inside a three-dimensional acoustic world where sounds originate from precise coordinates and distances.  
**Used for and where it works best:** VR/XR experiences, museum sound installations, high-end headphone podcasts, and cinematic set-pieces.  
**Best in:** formats: Interactive / XR, Spatial Exhibition, Audio Drama | genres: Horror, Sci-Fi, Heritage  
**Avoid when:** Channel order or head-tracking assumptions fail, or spatial movement is used as a gimmicky distraction.  
**Example:** `spec: 1st-order ambisonic B-format capture converted to binaural HRTF for immersive historical walk-through.`  
`audio_exec.spatial_capture`

---

### Remote Distributed Recording Chain

**Also called:** remote voice session, source-connect recording, P13X-AUD-07  
**What it is:** Capturing voice talent in separate global studios with pristine local lossless recording and synchronized guide feeds.  
**Effect on the audience:** Enables international casting of native speakers and dialects without sacrificing studio acoustic quality.  
**Used for and where it works best:** Directing voice actors across time zones for documentary translation, multilingual dubbing, and voice casting.  
**Best in:** formats: Global Documentary, Commercial, Multi-Voice Drama | genres: All  
**Avoid when:** Recording low-bitrate Zoom/Teams calls instead of uncompressed local WAV stems.  
**Example:** `protocol: talent records 24-bit 48kHz WAV locally while directed via ultra-low-latency monitoring link.`  
**Yields to:** `audio_exec.dialogue_ensemble` — The cast is co-located and must hear, interrupt and react to each other.  
`audio_exec.remote_recording`

---

### Live & Synthetic Hybrid Audio Session

**Also called:** AI-human audio hybrid, vocal synthesis integration, P13X-AUD-08  
**What it is:** Combining live recorded human vocal performances with generative AI speech layers, background extensions, and sound design.  
**Effect on the audience:** Blends human emotional authenticity with the infinite scale and rapid revision capabilities of AI generation.  
**Used for and where it works best:** Reconstructing deceased historical figures, multilingual auto-dubbing, and creating otherworldly chorus layers.  
**Best in:** formats: Modern AI Video Pipeline, Historical Recreation | genres: Sci-Fi, Heritage, Epic  
**Avoid when:** Synthetic elements sound visibly disjointed from live audio without acoustic and EQ matching.  
**Example:** `workflow: live actor records core narrative anchor; ElevenLabs generates auxiliary crowd murmurs and translated passes.`  
`audio_exec.hybrid_synthetic`

### Recording a Live Event You Cannot Stop

**Also called:** live capture, one-take recording, concert and ceremony sound  
**What it is:** **Recording something that happens once, at its own speed, whether you are ready or not** — a concert, a liturgy, a ceremony, a lecture, a performance. Every other card in this file assumes a take can be repeated; this one assumes it cannot, and that changes what the plan is for.  
**Effect on the audience:** Presence. A live recording carries a room and an audience that no assembled version reproduces — and it carries every mistake too, which is part of the same bargain.  
**Used for and where it works best:** **Plan for redundancy rather than for control.** Record more sources than you need — a main pair for the room, close sources for what must be legible, and an independent backup running the whole time on its own power and its own card — because the cheapest insurance is another recorder and the most expensive discovery is a single failed file. **Set levels for the loudest thing that will happen, not the thing happening now**, and leave real headroom: an unexpected fortissimo clips permanently and a quiet passage can be lifted. **Roll early and stop late**, continuously; a recording started on a cue misses the breath before it. Get the room's own sound before anyone arrives, because that is what covers every join later. And **write down what happened as it happens** — running order, what went wrong, where the door banged — since nothing can be recreated afterwards and a timed note is worth an hour of listening.  
**Best in:** formats: Concert / Live Event, Documentary Feature, Heritage Documentary, Museum Installation | genres: Heritage (civilisation-focused), Religious, Musical, Verite / Observational  
**Avoid when:** The material can be performed again. A studio or booth session takes the directed-take cards above, where the value is in the direction rather than in the redundancy.  
**Example:** `capture: main pair + 3 close sources + independent backup on separate power; levels set for the loudest expected passage; rolling continuously from 20 minutes before; room tone captured empty; timed log kept during.`  
**Yields to:** `audio_exec.music_tracking` — The material can be performed again in a directed take.  
`record.live_capture`
