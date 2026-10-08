# Audio Mixing, Mastering & Post-Production for AI Video

23 cards. What the mix has to achieve, written as notes the edit can act on: what sits under what, where speech has to stay clear, which spaces the voice belongs in, and how the master has to behave on the platform it lands on.

> **This phase does not mix.** Montage, levels, loudness and the final mix are made by the owner in
> his own edit, by hand, against the actual material and with his own ears. Every card below keeps
> its craft and states the intent; the value — the gain, the ratio, the threshold, the ceiling, the
> carve depth — is set on the timeline by the person making the move, and is not written here. A
> figure fixed in advance, against material that does not exist yet, can only be wrong, and the
> person who will make the move is not reading this card.

---

### Name What Is in the Way First

**Also called:** the mixing selector, the collision before the tool, what is this move operating on
**What it is:** The card at the head of the `mix.` shelf. It does not describe a sound. It asks the three questions this shelf's own pair graph repeats — **what is this move operating on, does the fault sit at one setting or only exist while it flares, and is the value decided by the material or by the destination** — and hands back a named shortlist for each answer. The axes were read off the shelf's `Yields to:` conditions and its `Avoid when:` lines, not invented. Every card cited here is cited by id.
**Effect on the audience:** None. This card never reaches the screen or the speaker. It exists so that the move made on the timeline was chosen against the collision, the material and the destination, rather than reached for out of habit.
**Used for and where it works best:** Answer the three questions **in order and out loud, one sentence each, before you open the shelf**. The first answer is the one that eliminates: it separates a move made to one voice from a move made to two things fighting from a move made to the finished whole, and those are three different moments in a pass, not three options at one moment. **This shelf is not additive and it was expected to be.** Most of it is built from opposed techniques — de-essing against dynamic resonance taming, carving against ducking, one standing compressor against band-by-band levelling, the mono fold-down audit against the surround fold-down. Where two answers fight for one track, that is two passes, not one setting.
**Best in:** formats: All video production | genres: All
**Avoid when:** **Axis one and axis three agree on most of their heaviest values**, so once you are past the voice and into the master this map is really asking two questions rather than three, and it does a smaller share of the work than it looks like it is doing. **It also cannot express order, and a mix is an order.** The pair field on this shelf says *not this one, that one* — it has no way to say *and then this*, which is why nothing routes to `mix.sub_80hz_high_pass`, the one card that calls itself the first move on every speech track, and nothing routes to any of the master-stage checks either. The graph is a set of swaps laid over a sequence. And **do not use this map to settle the whole-file high-pass argument**: `mix.sub_80hz_high_pass` calls that filter the first move on every dialogue track, and a card on the restoration shelf forbids exactly that move as a way of catching plosives. Both are routed here and neither is settled here.
**Example:** `[Selector — produces no handover note. It returns card ids. The chosen card carries the note.]`

---

**The axes**

**Axis 1 — What is this move operating on: one voice, two things that collide, or the finished whole?**
Asked first, because it is the condition the shelf repeats most and because it is the only one that recovers the order the pair field cannot state. The conditions are on the cards: *"One voice swinging whisper to shout"* (`mix.compression_topologies`), *"Fragile poetic reads that must keep their swings"* (`mix.multiband_speech_leveling`), *"The offending band is not sibilance"* (`mix.de_essing_smoothing`) and *"The flare is sibilance on a fixed band"* (`mix.dynamic_resonance_taming`) all turn on one voice alone. *"Gentle water and wind, where boosted attack clicks"* (`mix.transient_shaping_foley`), *"Foley must cut through without a level gap"* (`mix.ambience_foley_layering`), *"Move the music out of the way instead of carving it"* (`mix.frequency_slot_carving`) and *"The music should move automatically, not sit at a level"* (`mix.dialogue_to_music_ratio`) all turn on two things wanting the same moment. The rest are made once, to everything, at the end.

**Axis 2 — Does the fault sit at one setting, or does it only exist while it flares?**
This is the axis the shelf argues about most openly, and it is argued in `Avoid when:` rather than in `Yields to:`. *"Static notch filtering that hollows out the entire vocal spectrum when the offending frequency is not playing"* (`mix.dynamic_resonance_taming`). *"Applying fast limiting to soft poetic meditation reads, which creates pumping artifacts"* (`mix.compression_topologies`). *"Recoveries so fast that the music pumps audibly every time the narrator breathes"* (`mix.ducking_release_curve`). *"Over-de-essing, which causes the speaker to sound like they have a severe speech lisp"* (`mix.de_essing_smoothing`). A standing setting is cheap, survives a re-cut and costs you the moments it is wrong in; a tracking move is expensive, has to be re-judged on every take and audibly fails when its timing is wrong. The third value is not a compromise between them: it is the block of cards that change nothing at all and only tell you whether to.

**Axis 3 — Is the value decided by the material in front of you, or by the destination it is going to?**
Asked last because it reaches the cards the other two leave sitting at the end of the pass. *"Mastering for maximum loudness on a platform that normalises"* (`mix.lufs_loudness_targets`). *"Mastering to full scale, which guarantees clipping across mobile devices once the file has been re-encoded"* (`mix.true_peak_ceiling`). *"Ignoring phase, resulting in lead vocals or kick drums completely vanishing on mobile phones"* (`mix.mono_compatibility_audit`). *"Dropping surround channels completely"* (`mix.surround_downmix_protocol`). *"Leaving stereo widening plugins active across the low end, which smears the bottom and collapses in mono"* (`mix.low_end_management`). *"Spreading the voiceover into the side channels"* (`mix.mid_side_processing`). *"Mixing exclusively on open-back studio reference headphones in a dead-silent room"* (`mix.headphone_translation_test`). *"Exporting stems starting from arbitrary visual cut points"* (`mix.stems_export_standard`). A destination-decided value changes when the upload target changes and nothing else about the piece does.

---

**The map**

**Axis 1 — what the move is operating on**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One voice, by itself, before it meets anything** | `mix.sub_80hz_high_pass` · `mix.compression_topologies` · `mix.multiband_speech_leveling` · `mix.dynamic_resonance_taming` · `mix.de_essing_smoothing` · `mix.voice_de_reverberation` · `mix.convolution_ir_matching` |
| **Two things that want the same moment** | `mix.frequency_slot_carving` · `mix.dialogue_to_music_ratio` · `mix.ducking_release_curve` · `mix.transient_shaping_foley` · `mix.ambience_foley_layering` · `mix.mid_side_processing` · `mix.low_end_management` |
| **The finished whole, after everything else is settled** | `mix.lufs_loudness_targets` · `mix.true_peak_ceiling` · `mix.mono_compatibility_audit` · `mix.headphone_translation_test` · `mix.reference_track_matching` · `mix.surround_downmix_protocol` · `mix.tape_saturation_master` · `mix.stems_export_standard` |

**Axis 2 — does it sit still, or does it track**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A standing setting — dialled once against the material and left alone** | `mix.sub_80hz_high_pass` · `mix.frequency_slot_carving` · `mix.convolution_ir_matching` · `mix.voice_de_reverberation` · `mix.mid_side_processing` · `mix.low_end_management` · `mix.dialogue_to_music_ratio` · `mix.ambience_foley_layering` · `mix.tape_saturation_master` · `mix.true_peak_ceiling` · `mix.lufs_loudness_targets` · `mix.surround_downmix_protocol` · `mix.stems_export_standard` |
| **A tracking move — it only acts while the fault is there, and its timing is audible** | `mix.compression_topologies` · `mix.multiband_speech_leveling` · `mix.dynamic_resonance_taming` · `mix.de_essing_smoothing` · `mix.ducking_release_curve` · `mix.transient_shaping_foley` |
| **Neither — it changes nothing, it only tells you whether to** | `mix.mono_compatibility_audit` · `mix.headphone_translation_test` · `mix.reference_track_matching` |

**Axis 3 — material or destination**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The destination decides it — change the upload target and this value changes with it** | `mix.lufs_loudness_targets` · `mix.true_peak_ceiling` · `mix.mono_compatibility_audit` · `mix.surround_downmix_protocol` · `mix.low_end_management` · `mix.mid_side_processing` · `mix.headphone_translation_test` · `mix.stems_export_standard` |
| **The material decides it — the destination is irrelevant to the setting** | Every other card named in the two tables above. Named by complement, because listing them again would make this table longer than the shelf. |

*A card appears once per axis. The answer is the intersection of the three shortlists, and on this shelf it is normally one or two cards wide — which is the tell that these are steps in a pass, not options at a moment.*

---

**The default, and the one against it**

**There is no measured default on this shelf, and that is the first finding.** Counting distinct conditions behind inbound edges rather than edges: the most-yielded-to card here is `mix.lufs_loudness_targets`, named from three other files — but all three fire on the same condition, *a loudness figure is wanted and this card owns it*. It is an authority hub, not a fallback. `mix.mono_compatibility_audit` is next, named twice, and both conditions are the same condition twice over: **one speaker**. It is a delivery escape hatch. `mix.convolution_ir_matching` and `mix.transient_shaping_foley` are each named twice for two genuinely different reasons, and nothing on this shelf is named for three. **The shelf, asked sixteen times where to go instead, never falls back to the same place twice for two different reasons.** That is because most of its edges are reciprocal: de-essing and dynamic resonance taming name each other, one standing compressor and band-by-band levelling name each other, transient shaping and ambience layering name each other, the mono audit and the surround fold-down name each other. **A pair that points both ways cancels its own in-degree**, and a shelf built of such pairs cannot elect a default by counting.

**So the default is argued, not counted, and it is `mix.frequency_slot_carving`.** Every piece that reaches this shelf has the same problem — speech underneath something — and this is the only card that states a preference in its own description rather than a technique: *make room by taking something out of what is in the way, rather than pushing the voice louder.* It is also the only card the shelf argues about from two directions at once: both it and `mix.dialogue_to_music_ratio` name the same off-shelf rival, the move that ducks the music automatically instead. **A card the shelf has argued about is a default; a card nothing argues about is a habit.**

**The one against it is `mix.tape_saturation_master`.** The grain of this shelf is subtraction: carve it out, filter it off, tame it down, duck it, limit it, check what vanished. This is the only card that deliberately adds a fault — harmonic distortion — and it is the only one that answers the actual condition of generated audio, which is not that the voice is too quiet but that four separately generated stems do not sound like one recording. No amount of carving fixes that; nothing on the shelf routes to it and it routes to nothing, so it sits outside the argument entirely. Its cost is stated and it is honest — past a point it stops being glue and becomes an effect — and it is refused outright by clean corporate and clinical work, which is a real boundary rather than a taste. Its near cousin against the grain is `mix.convolution_ir_matching`, which likewise adds rather than removes, putting a room back into a voice that was recorded without one.

---

**The unasked**

**Half the shelf is the target of no `Yields to:` field anywhere in the package.** They can be chosen but nothing ever sends you to them. By id:

`mix.frequency_slot_carving` · `mix.sub_80hz_high_pass` · `mix.true_peak_ceiling` · `mix.mid_side_processing` · `mix.ducking_release_curve` · `mix.headphone_translation_test` · `mix.voice_de_reverberation` · `mix.tape_saturation_master` · `mix.dialogue_to_music_ratio` · `mix.stems_export_standard` · `mix.reference_track_matching`

**And the shape of that list is the finding, not its length.** Every master-stage check is on it — the true-peak ceiling, the headphone and phone-speaker pass, the reference comparison, the stems handoff, the tape glue — and so is `mix.sub_80hz_high_pass`, which describes itself as the first move on every speech track before anything else is done to it. **The shelf never routes to its own beginning and never routes to its own end. It only routes in the middle, between two techniques that could do the same job at the same moment.** The pair field can say *not this one, that one*; it cannot say *and then this*. Every reader who wrote one of these fields was holding one problem and comparing two tools for it, and none of them was holding a pass from first track to final master. A mix is a sequence, and a sequence has no alternatives — which is precisely why axis one had to be asked first, and asked in the language of *what is this operating on* rather than *which tool*.

The second thing the list shows: **the room is unasked from one side only.** `mix.convolution_ir_matching` is reached twice, both times from off this shelf, by readers asking how to put a voice into a space. `mix.voice_de_reverberation`, which takes a space back out, is reached by nothing. They are a matched pair — one adds a room, one strips one — and the shelf holds no edge between them and no question that asks which way round you are going. The card this shelf wants is the one that asks, before either is reached for, **whether the room already in the take is the room in the picture** — because if it is, both cards are wrong. And the nearest thing that exists disagrees with the restoration shelf about how far to strip a cloning sample, in a figure each states plainly and differently, with nothing routing a reader to either one to notice.

`mix.what_is_in_the_way`

---

### Frequency Slot Carving

**Also called:** spectral unmasking, mud cleanup, EQ bracket carve  
**What it is:** Making room for speech by taking something out of the music and foley in the low-mid band where the two collide, rather than pushing the voice louder. Which band, and how deep the carve, is found by ear against the actual cue, in the edit.  
**Effect on the audience:** Speech cuts through effortlessly without needing to raise the voiceover volume, preventing ear fatigue and mud.  
**Used for and where it works best:** Every mix where dialogue or narration must coexist with heavy orchestral music, war soundscapes, or synth drones.  
**Best in:** formats: All video production | genres: All  
**Avoid when:** Acoustic solo voiceover pieces where there is no competing music.  
**Example:** `handover: music and foley are crowding the narration in the low-mids — carve space for the voice rather than raising it.`  
**Yields to:** `soundscape.ducking_ratio` — Move the music out of the way instead of carving it.  
`mix.frequency_slot_carving`

---

### Sub-80Hz High-Pass Filtering

**Also called:** low-cut rumble removal, voice high-pass filter  
**What it is:** Rolling off the inaudible bottom end of every speech track — mic handling noise, room rumble, plosive thump — before anything else is done to it. The corner frequency and the slope are set in the edit against the actual take: above the rumble, below the chest.  
**Effect on the audience:** Eliminates inaudible mic handling noise, room rumble, and plosive thumps that distort mobile phone speakers.  
**Used for and where it works best:** The first move on every human and AI dialogue track, before any compression. It does not replace the plosive repair: a thump that survives the corner is fixed on its syllable by `restore.plosive_pop_elimination`, never by raising the corner into the chest.  
**Best in:** formats: All voiceover and dialogue | genres: All  
**Avoid when:** Deep sub-bass monster voices or cinematic explosions intended for subwoofers.  
**Example:** `handover: high-pass every speech track before compression; take the rumble without taking the chest.`  
**Yields to:** `mix.low_end_management` — Deep sub voices and explosions that must keep their bottom.  
`mix.sub_80hz_high_pass`

---

### Optical vs FET Speech Compression Topologies

**Also called:** compressor matching, vocal leveling dynamics  
**What it is:** Choosing the *character* of the speech compression: a slow, transparent one that leaves breathing intact, or a fast one that seizes transients and holds shouting down. The choice belongs to the piece and is named here; the ratio, attack and release are dialled in the edit.  
**Effect on the audience:** Optical preserves transparent human breathing; FET grabs transients and keeps loud battle shouting completely under control.  
**Used for and where it works best:** Transparent and slow for documentaries and memoirs. Fast and gripped for action trailers and aggressive character speeches.  
**Best in:** formats: Documentary vs Action Trailer | genres: Drama vs Action  
**Avoid when:** Applying fast limiting to soft poetic meditation reads, which creates pumping artifacts.  
**Example:** `handover: documentary read — transparent, slow, breathing left in. Trailer read — fast, gripped, nothing allowed to jump.`  
**Yields to:** `mix.multiband_speech_leveling` — One voice swinging whisper to shout.  
`mix.compression_topologies`

---

### LUFS Loudness Target Compliance

**Also called:** broadcast loudness standards, platform LUFS calibration  
**What it is:** Knowing, before the master is made, that the destination normalises loudness and will simply turn a hot master down rather than reward it. Which destination the piece is going to is a production fact and is declared here; the target figure belongs to that platform on the day, is looked up then, and is set at master time in the edit. These figures are not constants — they have changed more than once, and a number copied out of a card is a number that has stopped being checked.  
**Effect on the audience:** Prevents video platforms from applying destructive automatic volume attenuation to the upload.  
**Used for and where it works best:** The final mastering step before publishing to any social or broadcast platform.  
**Best in:** formats: All digital video platforms | genres: All  
**Avoid when:** Mastering for maximum loudness on a platform that normalises, or trusting a loudness figure written down months ago without re-checking it.  
**Example:** `handover: destination is <platform> — master to that platform's current published integrated target, checked on the day, not to the loudest master that will fit.`  
**Yields to:** AUTHORITY, in words: the destination platform's current published loudness spec, looked up on the day — The card states outright that the figure is not its own and that a number copied from a card has stopped being checked.  
`mix.lufs_loudness_targets`

---

### True Peak Ceiling Protection

**Also called:** inter-sample peak prevention, true peak limiting  
**What it is:** Leaving headroom under the master limiter's ceiling so that the platform's lossy transcode does not push inter-sample peaks into audible clipping. How much headroom is set at master time, against the codec the piece is actually going through.  
**Effect on the audience:** Prevents harsh digital clipping distortion when platforms transcode a high-res WAV into lossy AAC, Opus, or MP3.  
**Used for and where it works best:** Every final audio render destined for YouTube, Instagram, TikTok, or streaming platforms.  
**Best in:** formats: All digital video | genres: All  
**Avoid when:** Mastering to full scale, which guarantees clipping across mobile devices once the file has been re-encoded.  
**Example:** `handover: leave true-peak headroom under the limiter; this file gets re-encoded after upload and a master that just fits will not fit afterwards.`  
`mix.true_peak_ceiling`

---

### Mid-Side Spatial Field Processing

**Also called:** M/S processing, center channel dialogue isolation  
**What it is:** Splitting the stereo field into Mid (mono centre) and Side (width), keeping dialogue mono and anchored dead centre while reverb, music and air take the width. How wide, and any tonal move inside mid or side, is set in the edit.  
**Effect on the audience:** Creates a massive, cinematic widescreen listening field where the voiceover sits anchored dead-center without fighting stereo synths.  
**Used for and where it works best:** Cinematic trailers, epic documentaries, and music videos.  
**Best in:** formats: Feature Film, Cinematic Documentary, Trailer | genres: Epic, Sci-Fi, Action  
**Avoid when:** Spreading the voiceover into the side channels, which causes phase cancellation and makes speech sound disembodied.  
**Example:** `handover: the voice stays mono and centred throughout; width belongs to the music and the air, never to the voice.`  
**Yields to:** `mix.mono_compatibility_audit` — Mono or phone-speaker delivery, where width collapses.  
`mix.mid_side_processing`

---

### Convolution Impulse Response Reverb Matching

**Also called:** space impulse matching, acoustic environment match  
**What it is:** Putting the dialogue inside the space the picture is showing, using a convolution reverb built from a real impulse response of a room like it — an ancient stone hall, a mud-brick room, an open desert — instead of a generic plate. Which impulse response, and how much of it, is chosen in the edit against the picture.  
**Effect on the audience:** Eliminates the cognitive dissonance of hearing a bone-dry studio voiceover while looking at a character inside a monumental temple.  
**Used for and where it works best:** Diegetic dialogue and realistic dramatizations where the visual environment demands accurate acoustic reflections.  
**Best in:** formats: Feature Film, Historical Drama, Animation | genres: Historical / Biopic, Heritage  
**Avoid when:** Slapping generic synthetic plate reverb on an exterior desert scene.  
**Example:** `handover: this line is spoken inside a monumental stone throne room — match the voice to that space, do not leave it studio-dry.`  
**Yields to:** `sound.perspective` — Distance and shot size, not a room, set the space.  
`mix.convolution_ir_matching`

---

### Dynamic Resonance Taming

**Also called:** dynamic EQ, harshness suppression, Soothe calibration  
**What it is:** Ducking an offending resonance only while it flares — the ear-piercing peak on a shout, the boxy honk on a close line — instead of notching it out permanently and hollowing the voice. The frequency and the depth are found by sweeping the actual take, in the edit.  
**Effect on the audience:** Delivers a silky, polished, pleasant vocal tone that never stabs the listener's eardrums during emotional shouts or high frequencies.  
**Used for and where it works best:** AI voice synthesis outputs and aggressive dialogue takes that possess sharp digital resonances.  
**Best in:** formats: All TTS and dialogue tracks | genres: All  
**Avoid when:** Static notch filtering that hollows out the entire vocal spectrum when the offending frequency is not playing. A room mode that rings under every word is always playing, and takes the fixed cut of `restore.resonant_room_decluttering`.  
**Example:** `handover: this TTS voice has a hard resonance that stabs on shouted lines — tame it dynamically, not with a fixed notch.`  
**Yields to:** `mix.de_essing_smoothing` — The flare is sibilance on a fixed band.  
`mix.dynamic_resonance_taming`

---

### Sidechain Ducking Release Curve Shaping

**Also called:** smooth music dipping, ducking release envelope  
**What it is:** Shaping how the music comes *back* after it has ducked — a curved, unhurried recovery rather than a snap — so the return reads as an orchestra breathing rather than a gate opening. The release time and the shape of the curve are set in the edit, against the actual rhythm of the read.  
**Effect on the audience:** Music swells back naturally during vocal pauses like a living orchestra rather than jarringly jumping in volume.  
**Used for and where it works best:** Underneath all documentary voiceovers and podcast narration.  
**Best in:** formats: Documentary Feature, Narrative Podcast, Video Essay | genres: All  
**Avoid when:** Recoveries so fast that the music pumps audibly every time the narrator breathes.  
**Example:** `handover: music returns between lines on a curve, not a snap; if it pumps on the narrator's breaths the recovery is too quick.`  
`mix.ducking_release_curve`

---

### Transient Shaping for Kinetic Foley

**Also called:** punch enhancement, transient designer, attack sculpting  
**What it is:** Sharpening the initial attack on footsteps, blade impacts and arrow strikes while pulling back their muddy tail, so physical action reads through a dense bed without being made louder. How much attack, and how much tail, is set in the edit against the bed it has to cut through.  
**Effect on the audience:** Makes physical actions feel immediate, sharp, and physically impactful, cutting through dense musical beds.  
**Used for and where it works best:** Action scenes, martial combat, chariot chases, and kinetic social media hooks.  
**Best in:** formats: Action Short, Trailer, Vertical Short-Form | genres: Action, Historical, Thriller  
**Avoid when:** Gentle ambient sounds (water, wind) where boosted attack introduces harsh digital clicks.  
**Example:** `handover: these impacts have to read through the score — sharpen their attack rather than raising their level.`  
**Yields to:** `mix.ambience_foley_layering` — Gentle water and wind, where boosted attack clicks.  
`mix.transient_shaping_foley`

---

### Mono Compatibility Phase Auditing

**Also called:** mono fold-down check, phase correlation audit  
**What it is:** Summing the finished mix to mono and listening for what disappears, because most of this audience is on one phone speaker. A correlation meter is the instrument; what reading is acceptable, and what has to be repaired, is judged in the edit on the actual mix.  
**Effect on the audience:** Guarantees that users listening on single-speaker smartphones or smart displays hear every sound and every word.  
**Used for and where it works best:** A quality gate before the master is signed off on any digital video.  
**Best in:** formats: Vertical Short-Form, Mobile Video, Broadcast | genres: All  
**Avoid when:** Ignoring phase, resulting in lead vocals or kick drums completely vanishing on mobile phones.  
**Example:** `handover: check the mix in mono before it goes out — if a voice or a drum thins or vanishes, something in the stereo field is fighting itself.`  
**Yields to:** `mix.surround_downmix_protocol` — A 5.1 source, folded down by standard coefficients.  
`mix.mono_compatibility_audit`

---

### Headphone vs Studio Monitor Calibration

**Also called:** earbud translation test, mobile acoustic translation  
**What it is:** Signing the mix off on more than one system — reference monitors, ordinary consumer earbuds, and a bare phone speaker — because the overwhelming majority of this audience will never hear it on anything calibrated. What gets changed after each pass is decided in the edit.  
**Effect on the audience:** Ensures the mix sounds balanced for the viewers who will consume the content on mobile earbuds rather than calibrated speakers.  
**Used for and where it works best:** The final balance check, with particular attention to whether the bass overwhelms on bass-heavy consumer headphones.  
**Best in:** formats: All web and social video | genres: All  
**Avoid when:** Mixing exclusively on open-back studio reference headphones in a dead-silent room.  
**Example:** `handover: sign this off on cheap earbuds and a phone speaker as well as the monitors; the monitors are not where it will be heard.`  
`mix.headphone_translation_test`

---

### De-Reverberation of Voice Training Samples

**Also called:** room echo stripping, dry voice reclamation  
**What it is:** Applying AI de-reverberation algorithms to remove room reflections from vocal samples before feeding them into voice cloning engines.  
**Effect on the audience:** Eliminates metallic phase coloration and synthetic "bathroom echo" in the generated ElevenLabs clone.  
**Used for and where it works best:** Pre-processing historical interviews, archival recordings, or voice talent recorded in untreated rooms.  
**Best in:** formats: Voice Cloning Pre-Production, Archival Restoration | genres: All  
**Avoid when:** Over-processing to the point where speech consonants sound watery and robotic.  
**Example:** `tool: AI de-reverb in light passes, each raised until consonants begin to go watery and then backed off, preserving dry direct vocal transients.`  
**Source:** reference — checked 2026-09-23: neither ElevenLabs' voice-cloning documentation nor iZotope's RX manuals publish a de-reverb depth. ElevenLabs asks for a dry recording and light processing; iZotope's advice is to raise the reduction until artefacts begin, back off, and prefer several light passes. The unit is also tool-specific: one RX module states it in dB of gain on the separated reverb, another as a unitless amount.  
**Yields to:** `soundscape.stem_dialogue_dry` — The take can be delivered dry instead of stripped.  
`mix.voice_de_reverberation`

---

### Master Bus Analog Tape Saturation

**Also called:** tape warmth, harmonic glue, vintage saturation  
**What it is:** Gluing the stems together with gentle analog-style saturation so that separately generated AI audio reads as one recording rather than four. How much drive is set in the edit; past a point it stops being glue and becomes an effect.  
**Effect on the audience:** Rounds off harsh digital highs, thickens low-mid body, and provides cinematic filmic cohesion across disparate AI audio stems.  
**Used for and where it works best:** Historical documentaries, period dramas, and retro cinematic pieces.  
**Best in:** formats: Feature Film, Heritage Documentary, Period Piece | genres: Historical, Drama, Noir  
**Avoid when:** Modern clean corporate explainers or clinical tech product showcases.  
**Example:** `handover: this piece wants filmic warmth across the whole master, not a clean digital finish.`  
`mix.tape_saturation_master`

---

### Low-End Bass Management & Crossover

**Also called:** 80Hz subwoofer crossover, bass steering  
**What it is:** Deciding what owns the bottom of the mix, and summing the low band to mono so sub impacts and low score notes are not competing for the same air. Where the crossover sits and what gets high-passed above it is set in the edit.  
**Effect on the audience:** Delivers clean, earth-shaking low-end impacts on soundbars and home theaters without rattling or muddy distortion.  
**Used for and where it works best:** Theatrical mixes, cinematic trailers, and dramatic bass drops.  
**Best in:** formats: Theatrical Feature, Cinematic Trailer | genres: Action, Epic, Sci-Fi  
**Avoid when:** Leaving stereo widening plugins active across the low end, which smears the bottom and collapses in mono.  
**Example:** `handover: the sub hits and the low score notes are fighting for the bottom — clear the low band and give it to the hits.`  
`mix.low_end_management`

---

### Dialog-to-Music Level Calibration

**Also called:** DX/MX balance ratio, dialogue priority standard  
**What it is:** The standing intent that speech reads clearly over whatever is underneath it, everywhere in the piece, for a listener on a phone in a noisy room. *How far* above is a level, set in the edit by ear against the actual cue — it is not a constant, it moves between a sparse drone and a full orchestral climax, and a fixed figure written into a card is how this package ended up carrying two different ones.  
**Effect on the audience:** Ensures senior listeners and non-native speakers understand every word without having to rewind.  
**Used for and where it works best:** Educational, historical, and factual documentary productions.  
**Best in:** formats: Documentary Feature, Educational Video, Heritage Series | genres: Documentary, History  
**Avoid when:** Burying voiceover inside thick orchestral climaxes and expecting the subtitles to carry the meaning instead.  
**Example:** `handover: narration is the priority stem from first frame to last; if a word has to be replayed to be caught, the music is too high.`  
**Yields to:** `soundscape.ducking_ratio` — The music should move automatically, not sit at a level.  
`mix.dialogue_to_music_ratio`

---

### Ambience-to-Foley Spatial Layering

**Also called:** FX bus depth separation, soundscape foreground/background  
**What it is:** Keeping the continuous ambience bed clearly *behind* the physical foley, so the on-screen action stays in the foreground and the atmosphere stays unbroken underneath it. How much separation between the two is set in the edit.  
**Effect on the audience:** Accentuates on-screen physical action while maintaining unbroken atmospheric spatial presence.  
**Used for and where it works best:** World-building in historical cities, ancient palaces, and battle aftermath scenes.  
**Best in:** formats: Film, Series, Animation | genres: All  
**Avoid when:** Mixing foley and ambience at identical levels, creating a confusing, undifferentiated wall of noise.  
**Example:** `handover: ambience sits behind the foley, never level with it — the room should be felt and the footsteps heard.`  
**Yields to:** `mix.transient_shaping_foley` — Foley must cut through without a level gap.  
`mix.ambience_foley_layering`

---

### Stems Export Standard for DAW Handoff

**Also called:** delivery stem naming, post-production audio bundle  
**What it is:** Exporting uncompressed 24-bit 48kHz WAV stems strictly aligned to timeline frame 0 with standardized naming codes.  
**Effect on the audience:** Guarantees zero audio drift, missing cues, or sync mismatch when collaborating with external audio engineers.  
**Used for and where it works best:** Standard pipeline handoff to sound designer, re-recording mixer, or video editor.  
**Best in:** formats: All professional production | genres: All  
**Avoid when:** Exporting stems starting from arbitrary visual cut points rather than project timecode 00:00:00:00.  
**Example:** `stems: {PROJECT}_STEM_DX_48k24b.wav, {PROJECT}_STEM_FX_48k24b.wav, {PROJECT}_STEM_BG_48k24b.wav, {PROJECT}_STEM_MX_48k24b.wav.`  
**Yields to:** `score.four_way_score_stems` — The score itself must be handed off split four ways.  
`mix.stems_export_standard`

---

### Surround 5.1 Downmix Protocol

**Also called:** surround fold-down, Lo/Ro downmixing  
**What it is:** Downmixing 5.1 surround tracks to stereo using the ITU-R BS.775 coefficients (Center: -3dB, Surrounds: -3dB); the -6dB surround level is the alternative an AC-3 (ATSC A/52) stream may signal, not a BS.775 value.  
**Effect on the audience:** Preserves center dialogue clarity and surround atmosphere when a multichannel mix is played on standard stereo devices.  
**Used for and where it works best:** Theatrical or broadcast films being adapted for YouTube or social media release.  
**Best in:** formats: Broadcast Film, Web Adaptation | genres: All  
**Avoid when:** Dropping surround channels completely, which erases rear ambient sound design.  
**Example:** `formula: Left_Total = Left + 0.707*Center + 0.707*Left_Surround; Right_Total = Right + 0.707*Center + 0.707*Right_Surround.`  
**Source:** reference — ITU-R, Recommendation BS.775-4 (12/2022), Multichannel stereophonic sound system with and without accompanying picture, Annex 4 Table 2, https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.775-4-202212-I!!PDF-E.pdf, checked 2026-09-24; supports the 2/0 downmix L = L + 0.7071 C + 0.7071 LS and R = R + 0.7071 C + 0.7071 RS, centre and surrounds both at -3dB. ATSC, A/52:2018 Digital Audio Compression (AC-3, E-AC-3), section 5.4.2.5 Table 5.10, https://www.atsc.org/wp-content/uploads/2021/04/A52-2018.pdf, checked 2026-09-24; supports the surround mix levels an AC-3 stream may signal: 0.707 (-3 dB), 0.500 (-6 dB) or 0.  
**Yields to:** `mix.mono_compatibility_audit` — Single-speaker phones, where stereo is still one step too many.  
`mix.surround_downmix_protocol`

---

### De-Essing High-Frequency Smoothing

**Also called:** sibilance reduction, 6kHz vocal split-band de-esser  
**What it is:** Compressing the narrow high band where a voice's sibilants live, so that "s", "sh" and "ch" stop piercing, without touching the rest of the voice. Which band and how much reduction depends entirely on the individual voice, and is found by ear on the actual take in the edit.  
**Effect on the audience:** Prevents painful high-frequency piercing when listening through mobile earbuds at elevated volumes.  
**Used for and where it works best:** Expect to need it on ElevenLabs and other neural TTS voices, which naturally over-emphasise crisp sibilance.  
**Best in:** formats: All voiceover and TTS | genres: All  
**Avoid when:** Over-de-essing, which causes the speaker to sound like they have a severe speech lisp ("th" instead of "s").  
**Example:** `handover: this voice sibilates hard — de-ess it split-band, and stop before the "s" turns into a "th".`  
**Yields to:** `mix.dynamic_resonance_taming` — The offending band is not sibilance.  
`mix.de_essing_smoothing`

---

### Multi-Band Speech Leveling

**Also called:** multiband dynamics for voice, broadcast voice compressor  
**What it is:** Levelling the voice band by band rather than as a whole, so a whisper and a shout in the same scene stay tonally the same person instead of one going thin and the other going boomy. The bands and the ratios are set in the edit against that performer's actual range.  
**Effect on the audience:** Keeps the speaker's vocal tone consistent regardless of whether they whisper close to the mic or shout in anger.  
**Used for and where it works best:** Dynamic dramatic scenes with wild volume swings between lines.  
**Best in:** formats: Audio Drama, Feature Film, Action Series | genres: Drama, Action  
**Avoid when:** Poetic, fragile reads where dynamic volume swings are the intended emotional payload.  
**Example:** `handover: this performance swings from whisper to shout — level it band by band so it stays one voice, and leave the poetry alone.`  
**Yields to:** `mix.compression_topologies` — Fragile poetic reads that must keep their swings.  
`mix.multiband_speech_leveling`

---

### Reference Track Acoustic Matching

**Also called:** A/B mix reference, professional benchmark comparison  
**What it is:** Judging the mix against a known professional reference of the same kind, loudness-matched so the comparison is honest, rather than judging it in a vacuum. Which reference is a production choice and can be named here; the comparison and everything it changes happen in the edit.  
**Effect on the audience:** Prevents mixing in an acoustic vacuum; keeps the piece in the same world as the productions it will be watched alongside.  
**Used for and where it works best:** Before final sign-off on any mastering session.  
**Best in:** formats: All video productions | genres: All  
**Avoid when:** Comparing un-normalized tracks, where the louder one always falsely sounds better.  
**Example:** `handover: reference this mix against <named benchmark production> at matched loudness before signing it off.`  
`mix.reference_track_matching`
