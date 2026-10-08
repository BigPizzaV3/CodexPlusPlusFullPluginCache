# AI Audio Restoration, Cleanup & Artifact Elimination

19 cards. What goes wrong in generative and archival audio, how to recognise it, and what to hand the edit so it gets repaired — plus the pre-flight cleaning that decides what a cloned voice will sound like.

> **This phase does not do the restoration pass.** Cleaning a take on a timeline is a mix move, made
> by the owner in his own edit against the actual material: the amount of reduction, the threshold,
> the sensitivity, the depth of a notch. What belongs here is the *diagnosis* — which artefact this
> is, why it happens, what it costs, and how far is too far. Those cards name the fault and hand it
> over; they do not set the dial.
>
> Three cards are different and keep their figures: the cleaning applied to a sample **before** it is
> enrolled in a voice clone (`restore.spectral_hiss_suppression`,
> `restore.resonant_room_decluttering`, `restore.voice_training_decontamination`). That pass happens
> upstream of generation and decides what the cloned voice *is*, so it shapes what this pipeline
> produces rather than what the edit does with it afterwards.

---

### Name the Damage Before the Tool

**Also called:** the restoration selector, damage before tool, who made this fault
**What it is:** The card at the head of the `restore.` shelf. It does not name a plug-in. It asks the three questions this shelf turns on — **who made the damage, is the fault continuous or a handful of moments, and is this file going to a listener or into a voice clone** — and hands back a named shortlist for each answer. **The axes could not be read off the pair graph here and that is a finding rather than an omission**: this shelf holds almost no card-to-card edges, because a repair is not something you fall back to, it is something a fault sends you to, and the fault is not a card. So the axes were read off each card's own statement of what went wrong and off the `Avoid when:` lines that say how far is too far. Every card cited here is cited by id.
**Effect on the audience:** None. This card is never heard. It exists so that the repair reached for was chosen against the damage that is actually present, rather than against the tool that is already open on the timeline.
**Used for and where it works best:** **Name the fault out loud before opening the shelf.** If you cannot say what is wrong in one sentence — *mains hum*, *a plosive on the hard P*, *the take wanders in pitch*, *two voices slightly out of phase* — you are not restoring, you are mixing, and the wrong shelf is open. The first answer eliminates most of the file; the second decides the *shape* of the repair and is where this shelf's own arguments live; the third decides the tolerance, because a fault left in a sample before enrolment is a fault in every line the clone will ever speak. **And read the exits as exits.** Most of this shelf's edges do not point at another card here: they point upstream, out of the shelf, at regenerating the line, re-recording the capture, or going and fetching the uncompressed original. Those are the best answers when they are available, and they are answers this shelf is glad to lose to.
**Best in:** formats: All audio post-production | genres: All
**Avoid when:** **You cannot name the damage.** This map sorts faults, and given no fault it will hand you a plausible tool for a problem you have not diagnosed, which is how a take gets processed by habit — a thing one card here forbids in its own words. **Also: it routes a live argument and does not settle it, on purpose.** (A second one, the whole-file high-pass, is now closed by the two cards themselves: the rumble cut of `mix.sub_80hz_high_pass` sits below the chest and stays, and plosives are repaired syllable by syllable by `restore.plosive_pop_elimination`, never by raising that corner.) The de-reverberation depth for a cloning sample was stated twice, in two different figures; both cards now set it by ear against the artefacts, in light passes, because no reference publishes a depth and the unit differs from tool to tool. **It is routed here and it is not this card's to close.** Finally, distrust this map wherever the take is generated rather than captured: most of these faults were described by readers holding a recording, and a model's output can be wrong in ways none of them has a word for.
**Example:** `[Selector — produces no handover note. It returns card ids. The chosen card carries the note.]`

---

**The axes**

**Axis 1 — Who made this damage: the generator, the microphone, a file you were handed, or you?**
Asked first because it eliminates most of the shelf and because it is the question each card answers in its own *where it works best* line. The generator block is explicit — *expect it on every neural speech generation take*, *expect it on all synthesized voices*, *repairing rare digital glitches in long generation batches*, *auditing rare vocal glitch takes*. The microphone block is equally explicit — *cheap microphone preamp self-noise*, *field recordings from archaeological sites*, *live voice actor recordings*, *clipped the preamp converter*, *home offices and standard bedrooms*. The handed-a-file block names its own limit in `Avoid when:` — *"Original uncompressed WAV masters are available — go and get them instead"* (`restore.lossy_artifact_recovery`). **And the fourth value is the one no reader wrote down: the damage you made yourself**, at the layer or at the splice, which has no external source at all and cannot be escalated away from.

**Axis 2 — Is the fault continuous, or is it a handful of moments?**
The axis this shelf argues about, and the arguments are in `Avoid when:` rather than in `Yields to:`. *"High-passing the whole file to fix a handful of plosives, which permanently ruins the warmth of the speaker's chest resonance"* (`restore.plosive_pop_elimination`) — that is the boundary stated as a prohibition: **do not treat an event fault with a continuous tool.** And the other direction is stated just as plainly: *"Notching frequencies where the fundamental pitch of a deep male voice lives, which thins out the vocal body"* (`restore.ground_loop_hum_removal`), *"Setting reduction higher than the point where bubbly, watery artifacts appear"* (`restore.spectral_hiss_suppression`), *"Cutting more than three or four frequencies, which hollows out the core human vocal formants"* (`restore.resonant_room_decluttering`). A continuous fault is profiled once and subtracted across everything, and it costs you the material that shares its footprint. An event fault is repaired one instance at a time, and it costs you time. The third value is neither: a join you made, where the repair is laid under the seam rather than taken out of the file.

**Axis 3 — Is this file going to a listener, or into a voice clone?**
Asked last, and it changes the tolerance rather than the tool. The shelf's own opening block says that three of these cards keep their figures precisely because that pass happens *upstream of generation and decides what the cloned voice is*, and the cards agree — *preparing clean reference samples for voice cloning*, *cleaning voice cloning training files recorded in home offices*, *mandatory step before enrolling any voice*, *imperfect cloned training samples*. **A fault left in a take reaches one listener once; a fault left in a sample reaches every line the voice will ever speak.** It is asked last because it never changes which card you reach for, only how far you are allowed to push it — and it is the only axis on this shelf where the package currently disagrees with itself about the number.

---

**The map**

**Axis 1 — who made the damage**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The generator — a model produced it and it was never in the room** | `restore.mouth_de_clicking` · `restore.neural_sibilance_de_essing` · `restore.flange_tts_despeckling` · `restore.glitch_dropout_interpolation` |
| **The microphone — it was captured, in a room, by a person** | `restore.plosive_pop_elimination` · `restore.breath_noise_attenuation` · `restore.ground_loop_hum_removal` · `restore.spectral_hiss_suppression` · `restore.resonant_room_decluttering` · `restore.true_peak_declipping` · `restore.voice_training_decontamination` |
| **A file you were handed — archival, encoded, downloaded, off a worn transport** | `restore.harmonic_regeneration` · `restore.lossy_artifact_recovery` · `restore.warble_flutter_stabilization` |
| **You did — it is a property of the file, or of the join you just made** | `restore.phase_alignment_stems` · `restore.room_tone_matching` · `restore.dc_offset_removal` |

**Axis 2 — continuous, or a handful of moments**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Continuous — profiled once and subtracted across the whole file** | `restore.ground_loop_hum_removal` · `restore.spectral_hiss_suppression` · `restore.resonant_room_decluttering` · `restore.neural_sibilance_de_essing` · `restore.flange_tts_despeckling` · `restore.harmonic_regeneration` · `restore.lossy_artifact_recovery` · `restore.warble_flutter_stabilization` · `restore.dc_offset_removal` · `restore.voice_training_decontamination` |
| **A handful of moments — each one found and repaired on its own** | `restore.mouth_de_clicking` · `restore.plosive_pop_elimination` · `restore.glitch_dropout_interpolation` · `restore.breath_noise_attenuation` · `restore.true_peak_declipping` |
| **Neither — it is a join, and the repair goes under the seam** | `restore.phase_alignment_stems` · `restore.room_tone_matching` |

**Axis 3 — listener, or clone**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Into a voice clone, before enrolment — the tolerance is tighter and the figures here are live** | `restore.voice_training_decontamination` · `restore.spectral_hiss_suppression` · `restore.resonant_room_decluttering` · `restore.plosive_pop_elimination` |
| **To a listener, on the timeline** | Every other card named in the tables above. Named by complement, because listing them again would make this table longer than the shelf. |

**And the exits, which are on the map but not of the shelf.** Three of this shelf's four edges leave it, upstream, and each one is the better answer when it is available:

| When | Go here instead |
| :--- | :--- |
| The dropout has swallowed part of a word, not a few samples | regenerate the line — the edge names a card in the voice-engine family |
| The capture can still be made again with headroom | re-record it — the edge names a card in the capture family |
| An unencoded original exists somewhere | go and get it — the edge names no card at all, only the original master, in words |

---

**The default, and the one against it**

**There is no measured default here and there cannot be one.** Counting distinct conditions behind inbound edges rather than edges: **no card on this shelf is named twice by anything, anywhere in the package.** The whole family takes two inbound edges — one from inside, one from another phase — and each fires once. The reason is structural rather than an oversight: **you do not fall back to a repair, you are sent to one by a fault**, and on this shelf the fault is never a card. It is the artefact described inside each card's own body — the hum, the click, the blast, the dropout, the flattened peak, the wander. The named failure that starts every repair edge here is a sentence, not an id, so the graph has nothing to point from. Any map built on these four edges would have put three of its nodes outside the shelf.

**And the direction is worth recording, because it inverts between the two sides.** Every edge that *leaves* this shelf is a genuine pair: a repair card naming the working alternative — repair the glitch or regenerate the line, reconstruct the peak or shoot it again, reclaim the encoded file or fetch the original, add the missing top or tame the top that is already there. **The single edge that *enters* is a pointer**: a working card in the voice-engine family naming the damage it turns into, sending a contaminated sample here to be cleaned before enrolment. Same field, opposite meanings, and a builder reading `Yields to:` at face value would have laid the shelf out backwards.

**So the default is argued, not counted, and it is `restore.voice_training_decontamination`.** It is the one card the package points *into* this shelf for; it is the only one that calls itself mandatory in its own body; and it sits upstream of everything else here, because a fault enrolled into a clone is present in every line that clone will ever speak. **Most of the rest of this shelf is repairing, one take at a time, a symptom of skipping this one.** That is an argument from position in the pipeline, which is the only kind of argument a repair shelf can make.

**The one against it is `restore.lossy_artifact_recovery`.** Every other card here assumes the good version exists somewhere and the shelf's own edges say so out loud — regenerate it, re-record it, clean it before it becomes a voice. **This is the one card that says the good version does not exist and never will.** Its own yield names the alternative in plain words — go and get the uncompressed original — which means it is the only card on the shelf that is admissible *only* once the better answer has been refused. Choosing it is choosing to work with material you did not make and cannot remake: the interview that exists in one bad encode, the phone recording of somebody who has died, the clip that is the only footage there is. **That is not a compromise, it is the working condition of archival and heritage documentary**, and a shelf whose every other card presumes a retake is a shelf built for people who own their source. Its near cousin against the grain is `restore.harmonic_regeneration`, which likewise invents what was never captured rather than removing what should not have been.

---

**The unasked**

**All but two cards on this shelf are the target of no `Yields to:` field anywhere in the package.** Only `restore.neural_sibilance_de_essing` and `restore.voice_training_decontamination` are ever routed to, and each of them once. Everything else can be chosen, and nothing sends you there.

**And the shape of that list is the finding.** It is not scattered. **Every card whose fault is a handful of moments is on it** — the mouth clicks, the plosives, the dropouts, the heavy breaths, the flattened peaks — without exception. **And every card whose damage you made yourself is on it too** — the layered pair, the splice, the offset waveform. The two cards that *are* reached are both continuous and broadband, and both were reached by somebody asking a comparison question: *is this take dull or is it already bright*, *is this sample clean enough to enrol*. **A pair field can only carry the edges that a comparison makes**, and you compare states, not events. Nobody compares a click to anything: you hear it, you name it, you repair it. So the pair graph on a repair shelf is not a partial map of the shelf — it is a map of the only two questions on it that have two defensible answers, and the map that is actually needed has to be built from the damage instead. **That is why axis one asks who made the fault rather than which card yields to which.**

The second thing the list shows: **this shelf has no card for the fault you cannot name.** Every card here starts from a named artefact with a known cause and a known repair. Nothing covers the generated take that is simply wrong and the listener cannot say why — not hum, not hiss, not sibilance, not a click, just a read that a person would not have given. That is the ordinary condition of synthetic speech and it is the commonest reason a take is thrown away. The nearest thing that exists, `restore.flange_tts_despeckling`, catches exactly one case of it, the one where the wrongness happens to be two voices slightly out of phase, and it names that case so specifically that it cannot generalise. **The card this shelf wants is the one that says: the fault is in the performance, not in the signal, and no amount of repair will reach it — the decision is regenerate or reperform**, and the shelf's own exits already know how to say that for a dropout, a clip and an encode, and have no way to say it for a bad read.

`restore.name_the_damage_first`

---

### AI Mouth Saliva De-Clicking

**Also called:** mouth noise removal, saliva click repair, spectral de-click  
**What it is:** The high-frequency saliva clicks that high-resolution neural TTS reproduces faithfully because they were in the training voice — dozens per sentence, inaudible on laptop speakers and unbearable on headphones. Spectral de-click is the repair; the sensitivity is set on the actual take in the edit, because too much of it starts eating consonants.  
**Effect on the audience:** Removes repulsive subconscious wet mouth sounds; makes the voice sound pristine, polished, and dignified.  
**Used for and where it works best:** Expect it on every ElevenLabs and neural speech generation take. Audit on closed-back headphones, not speakers, or it will not be heard until after delivery.  
**Best in:** formats: All voiceover and audiobooks | genres: All  
**Avoid when:** Leaving raw TTS outputs uninspected in close-mic headphones.  
**Example:** `handover: this TTS take clicks on headphones — de-click it, and back off before the consonants soften.`  
`restore.mouth_de_clicking`

---

### Neural Sibilance De-Essing

**Also called:** split-band de-esser, digital S taming  
**What it is:** The metallic, over-bright sibilance that generative speech models produce in the upper-treble band — a different fault from a human's natural sibilance, and sharper. It is compressed split-band so only the offending sound moves; the band and the amount belong to the individual voice and are found by ear in the edit.  
**Effect on the audience:** Eliminates ear-bleeding harshness when listeners turn up the volume on phone speakers or earbuds.  
**Used for and where it works best:** Expect it on all AI-synthesized female and bright male voices.  
**Best in:** formats: All TTS outputs | genres: All  
**Avoid when:** Wideband compression that ducks the entire vocal volume instead of only the offending 's' frequency.  
**Example:** `handover: this voice has metallic 's' sounds — de-ess split-band only; do not duck the whole voice to fix them.`  
`restore.neural_sibilance_de_essing`

---

### Ground Loop Hum & Mains Removal

**Also called:** 50Hz/60Hz notch filter, hum eliminator  
**What it is:** Continuous electrical hum from the mains — at the local mains frequency and its harmonics, so 50Hz in Iraq, the UK and the EU, 60Hz in the US — sitting under archival and field recordings. Narrow notches at the fundamental and its harmonics are the repair; how narrow and how deep is judged in the edit, on the actual recording.  
**Effect on the audience:** Removes annoying continuous electrical buzzing from archival or live field recordings.  
**Used for and where it works best:** Cleaning archival interviews, field recordings from archaeological sites, and generator noise.  
**Best in:** formats: Documentary Feature, Archival Restoration | genres: History, Science  
**Avoid when:** Notching frequencies where the fundamental pitch of a deep male voice lives, which thins out the vocal body.  
**Example:** `handover: mains hum under this archival interview at the local mains frequency and its harmonics — notch narrow, and stop before the voice thins.`  
`restore.ground_loop_hum_removal`

---

### Spectral Hiss Suppression

**Also called:** broadband denoiser, room hiss removal  
**What it is:** Building a noise profile of pure background hiss during a pause, and selectively subtracting that spectral footprint across the audio.  
**Effect on the audience:** Silences room air conditioner hiss, tape hiss, and cheap microphone preamp self-noise without deadening the voice.  
**Used for and where it works best:** Preparing clean reference samples for voice cloning; cleaning historical archival tape.  
**Best in:** formats: Voice Cloning Preparation, Archival Film | genres: All  
**Avoid when:** Setting reduction higher than 12dB, which introduces bubbly, watery "underwater" phase artifacts.  
**Example:** `spec: Spectral Denoiser, Noise Learn: 500ms room tone, Reduction: 9dB, Artifact recovery: 65%.`  
**Source:** assumption — the package's working figure, not a published standard; set it by ear on the take, listening for artifacts.  
`restore.spectral_hiss_suppression`

---

### Phase Alignment Across Layered Stems

**Also called:** comb filtering prevention, phase correlation lock  
**What it is:** Time-aligning layered waveforms — two mics on one source, doubled foley, parallel vocal takes — so they reinforce instead of cancelling. The nudge is measured against the transients themselves on the timeline, so it is made in the edit; what belongs here is knowing that any layered pair has to be checked before it is mixed.  
**Effect on the audience:** Restores full, rich bass and crisp presence; prevents the hollow, thin sound of comb filtering.  
**Used for and where it works best:** Layering multiple generated voice takes, combining lapel and boom mics, and doubling foley tracks.  
**Best in:** formats: Film, Series, Animation | genres: All  
**Avoid when:** Layering identical audio tracks without checking phase correlation at all.  
**Example:** `handover: these two takes are layered — check phase before mixing them, or the pair will sound thinner than either one alone.`  
`restore.phase_alignment_stems`

---

### Plosive Pop Elimination

**Also called:** pop filter correction, P-thump repair, blast removal  
**What it is:** The low-frequency air blast a "P" or "B" puts into a microphone diaphragm, repaired surgically on the offending syllable rather than by filtering the whole file. Which syllables, how wide a window and how far down are decided on the waveform in the edit.  
**Effect on the audience:** Eliminates sudden speaker-rattling thuds that pull the listener out of dramatic immersion.  
**Used for and where it works best:** Cleaning live voice actor recordings and imperfect cloned training samples.  
**Best in:** formats: Podcast, Voiceover, Dialogue | genres: All  
**Avoid when:** High-passing the whole file to fix a handful of plosives, which permanently ruins the warmth of the speaker's chest resonance. The routine rumble cut of `mix.sub_80hz_high_pass`, set below the chest, is a different move and stays; what ruins the voice is raising that corner far enough to catch the plosives.  
**Example:** `handover: plosives on the hard P's — repair them one by one, do not high-pass the whole read to catch them.`  
`restore.plosive_pop_elimination`

---

### Glitch & Dropout Interpolation

**Also called:** sample interpolation, digital pop repair, click fix  
**What it is:** Replacing a handful of corrupted or dropped digital samples with interpolated waveform, so a buffer glitch in the middle of a good long take does not cost a regeneration. The judgement that matters is the one made in the edit: a glitch small enough to interpolate, or a gap large enough that a word is missing and the take has to be generated again.  
**Effect on the audience:** Eliminates jarring digital ticks, pops, and buffer dropouts caused by CPU spikes or streaming audio glitches.  
**Used for and where it works best:** Repairing rare digital glitches in long AI audio generation batches without regenerating the whole file.  
**Best in:** formats: Long-Form Narration, Audiobooks | genres: All  
**Avoid when:** The dropout has swallowed part of a word — that is a regeneration, not a repair.  
**Example:** `handover: single-sample spikes in this batch — interpolate them; anything that ate a syllable comes back for regeneration.`  
**Yields to:** `elevenlabs.seed_locking` — The dropout ate a word; regenerate the line instead.  
`restore.glitch_dropout_interpolation`

---

### Involuntary Breath Attenuation

**Also called:** breath leveling, gasp taming, breath automation  
**What it is:** Bringing heavy pre-sentence inhalations *down* rather than cutting them out, so the read keeps its human biology without the gasps dominating. How far down, and over how long a window, is automation drawn on the timeline in the edit — the point is the direction, not the figure.  
**Effect on the audience:** Preserves natural human biology while eliminating distracting, asthmatic gasps that dominate the mix.  
**Used for and where it works best:** Post-processing voiceover and podcast narration.  
**Best in:** formats: Documentary, Narrative Podcast, Commercial | genres: All  
**Avoid when:** Cutting breaths to absolute digital silence, which creates an unnatural, robotic vacuum between sentences.  
**Example:** `handover: heavy breaths before lines — ride them down, do not cut them out; a read with no breath in it sounds like a machine.`  
`restore.breath_noise_attenuation`

---

### High-Frequency Harmonic Regeneration

**Also called:** audio exciter, dull audio restoration, spectral synthesis  
**What it is:** Synthesising the upper harmonics a muffled, low-bitrate or vintage recording no longer has, generated from the fundamentals that survive. This is enhancement, not recovery of the lost waveform: preserve the untouched source, work on a derivative, and record the process in the provenance log. How much is added is set by ear in the edit, and the failure is always the same one: too much, and the repair is louder than the recording.  
**Effect on the audience:** Adds air and presence to a listening copy of a muffled, low-bitrate or vintage recording, while the original stays unchanged.  
**Used for and where it works best:** Restoring vintage historical recordings or low-sample-rate archival voices, as a disclosed access copy or remaster whose synthetic top end cannot be mistaken for recorded evidence.  
**Best in:** formats: Historical Documentary, Archival Restoration | genres: History, Biography  
**Avoid when:** Applying it to already bright, crispy modern TTS audio, which creates harsh ice-pick treble. And a better copy of the recording exists somewhere, an earlier transfer or the original medium: go and get it first, as `restore.lossy_artifact_recovery` does for an encode, because what this card adds was never recorded.  
**Example:** `handover: this archival voice is muffled — keep the original untouched, regenerate the top end on a disclosed copy, and stop while it still sounds like an old recording.`  
**Yields to:** `restore.neural_sibilance_de_essing` — The take is already bright, not dull.  
`restore.harmonic_regeneration`

---

### Room Tone Matching for Seamless Edits

**Also called:** room tone fill, acoustic patch generator  
**What it is:** Extracting clean room tone from the recording and laying it under every dialogue splice, so a comped take reads as one continuous performance instead of a series of joins. This is made on the timeline where the splices are, so it is an edit move; what belongs here is the rule that no dialogue gap is ever left as digital silence.  
**Effect on the audience:** Makes edited dialogue sound like one continuous, unbroken take; eliminates audible room tone dropouts on cuts.  
**Used for and where it works best:** Splicing different audio takes together, fixing flubbed lines, and editing podcast dialogue.  
**Best in:** formats: All dialogue editing | genres: All  
**Avoid when:** Leaving dead digital silence between spliced sentences, which sounds like the audio cut out completely.  
**Example:** `handover: room tone under every splice and every gap in this scene — no bare digital silence between lines.`  
`restore.room_tone_matching`

---

### Resonant Room Mode De-Cluttering

**Also called:** boxiness removal, resonant peak notch  
**What it is:** Sweeping a narrow parametric EQ (Q=8) to find and cut stationary acoustic room ringing (typically between 300Hz and 700Hz) from untreated recording spaces.  
**Effect on the audience:** Removes the cheap "closet / bedroom" resonance, making the voice sound like it was recorded in a million-dollar treated studio.  
**Used for and where it works best:** Cleaning voice cloning training files recorded in home offices or standard bedrooms.  
**Best in:** formats: Voice Cloning Prep, Indie Production | genres: All  
**Avoid when:** Cutting more than three or four frequencies, which hollows out the core human vocal formants, or when the resonance appears only on particular syllables or levels; that moving flare belongs to `mix.dynamic_resonance_taming`. This card is only for a stationary room mode present across the take.  
**Example:** `notch_cuts: -4dB @ 430Hz (room standing wave) and -3dB @ 680Hz (closet resonance).`  
**Source:** assumption — the package's working figure, not a published standard; set each cut by ear against the take, after sweeping for the room's own modes.  
`restore.resonant_room_decluttering`

---

### Level Matching Across Multi-Take TTS

**Also called:** LUFS take normalization, vocal volume matching  
**What it is:** Bringing every generated take to the same perceived loudness before they are comped together, so the scene does not jump in volume between sentences that came from different API calls. Perceived loudness, not peak — peak normalisation does not hear the way a listener does. The target is whatever the edit is working to, and is set there.  
**Effect on the audience:** Eliminates jarring volume jumps between sentences generated in different API calls.  
**Used for and where it works best:** Comping dialogue from multiple generative takes into a single cohesive scene.  
**Best in:** formats: Audio Drama, Feature Film, Documentary | genres: All  
**Avoid when:** Relying on peak normalization, which ignores perceived human loudness.  
**Example:** `handover: these takes come from separate generations — match them on perceived loudness before comping, not on peak.`  
`restore.take_level_matching`

---

### Lossy Compression Artifact Reclamation

**Also called:** MP3 de-compression, phase smear recovery  
**What it is:** Filtering the swishing "metallic bird" artefacts and smeared high-frequency phase that low-bitrate encoding leaves behind in a clip you did not record and cannot re-record. How much is taken out is a judgement made in the edit; the rule that belongs here is that you do it only when no uncompressed original exists.  
**Effect on the audience:** Restores professional acoustic credibility to compressed internet audio clips or historical phone recordings.  
**Used for and where it works best:** Incorporating user-submitted audio clips, historical phone interviews, and web downloads.  
**Best in:** formats: Documentary, True Crime | genres: Documentary, Journalism  
**Avoid when:** Original uncompressed WAV masters are available — go and get them instead.  
**Example:** `handover: this clip is off the web and carries encoder swish — reclaim what you can; there is no uncompressed original.`  
**Yields to:** The uncompressed original master, source-first — An unencoded original exists; go and get it (authority target written in words, not a card).  
`restore.lossy_artifact_recovery`

---

### Flange & Chorus TTS Despeckling

**Also called:** robotic phase cancellation fix, mono summation check  
**What it is:** The comb-filtered, double-voiced artefact a neural model occasionally emits when it outputs two voices slightly out of phase with each other. The repair is to find the clean channel and keep it; the decision of which channel is clean is made by listening, in the edit.  
**Effect on the audience:** Restores solitary human presence; removes the weird robotic double-voice effect.  
**Used for and where it works best:** Auditing and repairing rare ElevenLabs or Suno vocal glitch takes.  
**Best in:** formats: All AI audio production | genres: All  
**Avoid when:** Creative chorus effects on background vocal pads where doubling is intended.  
**Example:** `handover: this take has a phasey double-voice — split it, keep the clean channel, discard the other.`  
`restore.flange_tts_despeckling`

---

### DC Offset Removal

**Also called:** zero-crossing correction, DC bias centering  
**What it is:** Removing the direct-current bias that sits the waveform off the zero line, costing headroom and putting a click on every slice. It is a standard pre-master pass on recorded and generated audio, and it is run in the edit on the actual files.  
**Effect on the audience:** Restores maximum dynamic headroom for mastering and prevents audible clicks when slicing audio clips.  
**Used for and where it works best:** A pre-mastering cleanup pass on all recorded or generated audio files.  
**Best in:** formats: All audio engineering | genres: All  
**Avoid when:** Audio already centers on the zero line — check before processing rather than processing by habit.  
**Example:** `handover: check these files for DC offset before mastering; it is what is putting clicks on the slices.`  
`restore.dc_offset_removal`

---

### True-Peak De-Clipping & Waveform Reconstruction

**Also called:** analog clipping repair, peak reconstruction  
**What it is:** Reconstructing the rounded shape of a waveform whose peaks were flattened by a converter, when the take is irreplaceable and re-recording is not an option. The missing peak is estimated, not recovered as fact: preserve the clipped original and work on a logged derivative. Whether a clipped take is worth reconstructing, and how far the reconstruction is pushed, is judged in the edit against the take.  
**Effect on the audience:** Eliminates harsh, buzzy digital distortion from loud shouts or explosive sound effects.  
**Used for and where it works best:** Salvaging irreplaceable field recordings or explosive audio takes that clipped the preamp converter, as a disclosed listening or editorial copy. Where the recording is evidence — news, war, archive — the untouched original stays authoritative and reconstructed peaks are never measured as fact.  
**Best in:** formats: Archival Restoration, Field Recording | genres: War, Documentary, News  
**Avoid when:** The take was recorded with proper headroom and nothing is actually clipped. Or an unclipped copy of the same recording exists somewhere: go and get it first, as `restore.lossy_artifact_recovery` does for an encode, because the reconstruction writes waveform the take never held — the take is irreplaceable only once that search has come back empty.  
**Example:** `handover: this field recording clipped on the shout and cannot be re-recorded — keep the clipped original, reconstruct the peaks on a logged copy.`  
**Yields to:** `record.live_capture` — The capture can still be made again with headroom.  
`restore.true_peak_declipping`

---

### Voice Training Sample Decontamination

**Also called:** cloning sample purification, reference audio prep  
**What it is:** The complete pre-flight cleaning protocol for any audio file intended for a voice engine's instant or professional cloning (the vendor's terms and windows are in its adapter in ENGINE-CHECK.md §7).  
**Effect on the audience:** Prevents the clone from inheriting room reverb, mouth clicks, traffic hum, and plosive pops permanently into its synthetic DNA.  
**Used for and where it works best:** Mandatory step before enrolling any voice in the production voice library. The high-pass here is the rumble cut of `mix.sub_80hz_high_pass`, set below the chest; plosives are repaired syllable by syllable per `restore.plosive_pop_elimination`, not by pushing that filter up.  
**Best in:** formats: Voice Cloning Setup | genres: All  
**Avoid when:** Uploading raw cell phone voice memos directly into voice cloning engines. And before any of this: cloning the voice of a real person, living or recorded long ago, waits at the cloning step alone for that person's consent, or the consent of whoever can speak for them, recorded with their name and the date in `project.yaml` (root SKILL.md §0); everything else in the work carries on.  
**Example:** `cleaning_pipeline: 80Hz High-Pass -> Plosive Repair (per syllable) -> Spectral Denoise (-9dB) -> De-Click -> De-Reverb (light passes, each stopped just before artefacts begin) -> Normalize to the level the engine's cloning page asks for (its adapter in ENGINE-CHECK.md §7).`  
**Source:** reference — checked 2026-09-23: neither ElevenLabs' voice-cloning documentation nor iZotope's RX manuals publish a de-reverb depth. ElevenLabs asks for a dry recording and light processing; iZotope's advice is to raise the reduction until artefacts begin, back off, and prefer several light passes. The unit is also tool-specific: one RX module states it in dB of gain on the separated reverb, another as a unitless amount.  
`restore.voice_training_decontamination`

---

### Spectral Warble & Flutter Stabilization

**Also called:** tape wow and flutter fix, pitch drift stabilizer  
**What it is:** Correcting cyclical pitch wander — the wow and flutter of a worn tape transport, or the pitch drift a low-stability generative take produces. The repair locks the pitch back to a stable centre; how much smoothing before the performance goes lifeless is a call made by ear in the edit.  
**Effect on the audience:** Locks the speaker's vocal pitch to steady acoustic stability; prevents seasick pitch wavering.  
**Used for and where it works best:** Restoring vintage tape archives and fixing unstable low-stability generative TTS takes.  
**Best in:** formats: Archival Documentary, Audio Drama | genres: History, Biography  
**Avoid when:** Musical vibrato deliberately sung by a vocalist — that is a performance, not a fault.  
**Example:** `handover: this take wanders in pitch — stabilise it, and stop before the delivery goes flat.`  
`restore.warble_flutter_stabilization`
