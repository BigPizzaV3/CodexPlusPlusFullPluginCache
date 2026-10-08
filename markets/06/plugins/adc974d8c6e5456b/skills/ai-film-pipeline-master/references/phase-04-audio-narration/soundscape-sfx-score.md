# Soundscape, SFX & Score Architecture

24 cards. The 4-Stem sonic architecture, foley design, documentary soundscape construction, and historical ambience engineering across civilisations.

> **Which stems exist, and what sound goes in each, is decided here — the levels are not.** The stem
> architecture, the foley and ambience content, and the historical sound world are production
> decisions: they determine what gets generated and recorded. Balance between the stems, ducking,
> and anything measured in dB is a mix move made by the owner in his own edit, against the actual
> material. Those cards below state the intent and hand it over; they do not set the number.

---

### Does It Run, or Does It Land

**Also called:** the soundscape selector, bed before hit, what is holding this scene up  
**What it is:** The card at the head of the `soundscape.` shelf. It does not describe a sound. It asks the three questions the shelf's own pair graph asks over and over — **does this run under the scene or land on one frame of it, is the source inside the film's world or is the film speaking, and does a period gate it** — and hands back a named shortlist for each answer. The axes were read off the shelf's `Yields to:` conditions and its `Avoid when:` boundaries, not invented. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the track. It exists so that the sound under a scene was chosen against the location, the clock and the century, rather than reached for because it was the last one used.  
**Used for and where it works best:** Answer the three questions **in order and out loud, one sentence each, before you open the shelf**. Question one splits the shelf almost in half; question two halves it again; question three usually settles it or sends you to the canon. **If your honest answer to question one is the fourth value — that what you are choosing is a rule about sounds rather than a sound — you have not chosen anything yet**, and the next thing to do is go back and name the sound. Where two answers fight for one scene, that is a bed and a spot effect, and this shelf has no grammar for that: see the warning below.  
**Best in:** formats: All video and audio production | genres: All  
**Avoid when:** **You are deciding whether the bed or the spot effect carries the moment.** The pair field on this shelf reads *instead of*, and fourteen of the edges that arrive here from `foley-and-sound-design.md` do not mean *instead of* — they mean *inside*. The bazaar contains the coppersmith, the battle bed already carries the horns, the sanctuary already carries the brazier, and every one of those cards says so in its own words. This map will hand you one card where the honest answer is two, so **distrust it the moment your shot has both a place and an object in it.** Also avoid it on the four stem cards as if they were options: they coexist, they are the addresses the other answers are delivered to, and a map that presents a container as a choice is offering you a box instead of a thing. And **distrust question three whenever your subject is Neo-Assyrian** — there the card does not answer, the canon does, and `soundscape.foley_clay_tablets` says so in its own `Yields to:`.  
**Example:** `[Selector — produces no cue. It returns card ids. The chosen card carries the cue.]`  

---

**The axes**

**Axis 1 — Does it run under the scene, or land on one frame of it?**
Asked first, because duration is what the shelf's conditions keep coming back to and it is the split the pair field handles worst. `soundscape.stem_ambience_bed` yields out of the shelf entirely on it — *"The drop to dead silence is the effect"* — and `soundscape.sfx_whoosh_transition` yields on its mirror image, *"A solemn or contemplative piece, the join must not be heard."* `soundscape.sfx_sub_bass_hit` yields on *"A minor informational transition."* The same boundary is written into the `Avoid when:` lines: the bed fails by *"Cutting the ambience bed abruptly on picture cuts"*, the whoosh by *"Solemn continuous drama scenes"*, the sub-bass by *"Minor informational transitions, which causes ear fatigue."* One edge into the shelf states it from outside in the plainest form there is — *"Continuous desert wind rather than a whirlwind event."*

**Axis 2 — Is the source inside the film's world, or is the film speaking?**
The second-strongest repeat, and the one that decides what a mistake here will sound like. A bed or a contact sound that is wrong is an anachronism the audience catches; a score or a sweep that is wrong is a tone the audience resents. The conditions sort cleanly: *"Marsh, canal or any wet setting"* (`soundscape.ancient_desert_ambience`), *"Arid plateau or mountain fortress"* (`soundscape.river_civilisation`), *"Desert ruin or desolate outpost"* (`soundscape.bazaar_marketplace`), *"A public market, not a sanctuary"* (`soundscape.temple_sacred_chant`), *"A court or diplomatic sequence"* (`soundscape.ancient_battlefield`) are all one side; *"A heritage subject that needs regional timbre"* (`soundscape.score_minimal_drone`), *"Contemporary corporate or sci-fi material"* (`soundscape.score_ethnic_instrumentation`), *"The song takes the film over, no voice to duck under"* (`soundscape.ducking_ratio`) and its exact reverse in `soundscape.narration_song_handover` are the other.

**Axis 3 — Does a period gate this, and who settles the gate?**
Asked last, and it is the only axis on this shelf whose strongest value is not a card. Six conditions turn on where and when the scene is, and one of them hands the decision away: `soundscape.foley_clay_tablets` yields **to the canon**, on any Neo-Assyrian subject, *the period rule outranks this card's scene list*. `soundscape.sfx_paper_parchment` yields on *"A pre-paper Mesopotamian era, where writing is clay"* and warns in its own `Avoid when:` against *"paper in 2000 BC Sumer before paper was invented."* `soundscape.foley_ancient_garments` draws its boundary at *"Synthetics, modern nylon swishes, or denim rustle."* The point of asking it last is that it does not narrow the shortlist — it tells you whether you are still allowed to choose.

---

**The map**

**Axis 1 — does it run, or does it land**

| Answer | The shortlist, by id |
| :--- | :--- |
| **It runs under the whole scene, and its failure is being cut** (eleven) | `soundscape.stem_ambience_bed` · `soundscape.ancient_desert_ambience` · `soundscape.ancient_palace_hall` · `soundscape.ancient_battlefield` · `soundscape.river_civilisation` · `soundscape.bazaar_marketplace` · `soundscape.temple_sacred_chant` · `soundscape.score_minimal_drone` · `soundscape.score_ethnic_instrumentation` · `soundscape.coast_and_storm` · `soundscape.worldised_device_playback` |
| **It follows a body and stops when the body stops** (three) | `soundscape.foley_ancient_garments` · `soundscape.foley_clay_tablets` · `soundscape.sfx_paper_parchment` |
| **It lands on one frame and is gone** (three) | `soundscape.sfx_whoosh_transition` · `soundscape.sfx_sub_bass_hit` · `soundscape.sonic_branding_signature` |
| **It is not a sound — it is a rule about how the sounds sit together** (five) | `soundscape.stem_master_architecture` · `soundscape.stem_dialogue_dry` · `soundscape.stem_music_score` · `soundscape.ducking_ratio` · `soundscape.narration_song_handover` |

**Axis 2 — whose sound is it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Inside the world — a microphone standing in that place would have caught it** (twelve) | `soundscape.ancient_desert_ambience` · `soundscape.ancient_palace_hall` · `soundscape.ancient_battlefield` · `soundscape.river_civilisation` · `soundscape.bazaar_marketplace` · `soundscape.temple_sacred_chant` · `soundscape.stem_ambience_bed` · `soundscape.foley_ancient_garments` · `soundscape.foley_clay_tablets` · `soundscape.sfx_paper_parchment` · `soundscape.coast_and_storm` · `soundscape.worldised_device_playback` |
| **The film speaking — nothing in the frame is making it** (six) | `soundscape.sfx_whoosh_transition` · `soundscape.sfx_sub_bass_hit` · `soundscape.sonic_branding_signature` · `soundscape.score_minimal_drone` · `soundscape.score_ethnic_instrumentation` · `soundscape.stem_music_score` |
| **The voice's own track, and what everything else must do around it** (four) | `soundscape.stem_dialogue_dry` · `soundscape.ducking_ratio` · `soundscape.narration_song_handover` · `soundscape.stem_master_architecture` |

**Axis 3 — who settles the period**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The canon settles it, and it outranks the card** (one) | `soundscape.foley_clay_tablets` |
| **The card's own era line settles it — get it wrong and the sound is an anachronism** (nine) | `soundscape.ancient_desert_ambience` · `soundscape.ancient_palace_hall` · `soundscape.ancient_battlefield` · `soundscape.river_civilisation` · `soundscape.bazaar_marketplace` · `soundscape.temple_sacred_chant` · `soundscape.foley_ancient_garments` · `soundscape.sfx_paper_parchment` · `soundscape.score_ethnic_instrumentation` |
| **Nothing gates it — no century made it, so no century forbids it** (twelve) | `soundscape.stem_master_architecture` · `soundscape.stem_dialogue_dry` · `soundscape.stem_ambience_bed` · `soundscape.stem_music_score` · `soundscape.ducking_ratio` · `soundscape.sfx_whoosh_transition` · `soundscape.sfx_sub_bass_hit` · `soundscape.score_minimal_drone` · `soundscape.sonic_branding_signature` · `soundscape.narration_song_handover` · `soundscape.coast_and_storm` · `soundscape.worldised_device_playback` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally one to three cards wide — which is narrower than this shelf deserves, and the reason the warning above exists.*

---

**The default, and the one against it**

**The default is `soundscape.stem_ambience_bed` running under `soundscape.ducking_ratio` — and the second half of that is measured, not asserted.** `soundscape.ducking_ratio` is the only card on the shelf reached by three genuinely *different* conditions: `mix.frequency_slot_carving` sends a reader here because *"Move the music out of the way instead of carving it"*, a second card in the same file because *"The music should move automatically, not sit at a level"*, and `soundscape.narration_song_handover` because *"The song stays underscore and never takes over."* Three readers, two files, three unrelated reasons. Compare `soundscape.ancient_battlefield`, which takes the same number of inbound edges and **all of them on one condition** — *massed combat rather than a single blade*, *massed chariot warfare rather than one cart*, *full battle bed, which already carries the horns*. That is not a fallback, it is a door out of the `foley.` shelf, and in-degree alone would have called it the default. `soundscape.stem_ambience_bed` supplies the other half because it is the card Phase 3 reaches for when *"The location's own tone is unusable"* — the only inbound edge on this shelf that means *there is nothing here, put something*.

**The one against it is `soundscape.narration_song_handover`.** Every other card on this shelf assumes the narrator owns the track and the sound is arranged around the voice — that is literally what axis 2's third value is. This card is the only one that **takes the track away from the narrator and gives it to the music for a stretch of film**, and it is written by somebody who noticed that the interesting half of that decision is not the drop but the return: *the drop into the song gets attention because it is the exciting one, and the return gets none, which is why the return is where these pieces fail*. Its cost is real and stated — a hard-cut piece whose whole grammar is abruptness does not want it, and a song that never stops being underscore does not need it. What it buys is the one thing the default can never buy: a passage where the film stops explaining itself. Its near cousin against the grain is `soundscape.sonic_branding_signature`, which nothing reaches and which reaches nothing, and which is the only card here that belongs to the channel rather than to the film.

---

**The unasked**

**Half the reachable shelf is the target of no `Yields to:` field from anywhere on this shelf.** By id:

`soundscape.stem_master_architecture` · `soundscape.stem_dialogue_dry` · `soundscape.stem_ambience_bed` · `soundscape.stem_music_score` · `soundscape.ancient_battlefield` · `soundscape.temple_sacred_chant` · `soundscape.foley_ancient_garments` · `soundscape.sfx_sub_bass_hit` · `soundscape.sfx_paper_parchment` · `soundscape.sonic_branding_signature` · `soundscape.coast_and_storm`

**And the shape of that list is the finding, not its length.** Two things are on it and both matter.

**First: every stem card is on it.** Not one card on this shelf ever sends a reader to a stem, because you do not choose a stem against anything — you choose what goes *in* one. The pair field records that as silence, and silence is indistinguishable from nobody having thought about it. `soundscape.stem_ambience_bed` is reached only from Phase 3 and only when a real location's tone has failed; `soundscape.stem_dialogue_dry` only from the mixing shelf; `soundscape.stem_master_architecture` from nowhere at all. **The shelf's own graph only ever compares beds to beds and scores to scores**, which is why it looks so tidy and covers so little.

**Second, and it is the larger one: this shelf receives far more than it chooses.** Its internal edges number thirteen; the edges arriving from outside it number twenty-two, and fourteen of those come from one shelf — `foley.` in `foley-and-sound-design.md`. That is a shelf that is a destination. And the fourteen do not say what the pair field claims they say. *"The whole sanctuary rather than one strike."* *"Whole-city background, not the artisan quarter."* *"The waterway bed rather than one hull."* *"Full battle bed, which already carries the horns."* *"The sanctuary bed already carries the brazier."* **Those are not alternatives. They are the same sound at two scales, and the larger one contains the smaller.** A reader sent from the coppersmith to the bazaar has not been offered a different sound; they have been told to stop pointing the microphone at one man. The traffic is one-directional — fourteen edges arrive, one leaves — which is exactly what containment looks like drawn as a graph, and is not what alternation looks like at all.

**So the card this shelf wants is the one that does not exist: the one that says a bed and a spot effect are both required, and the only question is which of them is carrying this particular second.** The nearest thing in the package is `soundscape.stem_master_architecture`, which knows the two live in different stems and is therefore filed as having no alternative — correctly, and uselessly, because knowing they are different files does not tell you which one the audience is listening to. Until that card exists, the pair field will keep writing *instead of* where the reader meant *inside*, and every selector built on this shelf will inherit it.

`soundscape.run_or_land`

---

### The 4-Stem Master Architecture

**Also called:** four-pillar audio mix, stem separation protocol  
**What it is:** Structuring all project audio into four isolated, independently controllable stems: Dialogue/VO, SFX/Foley, Ambience/Room Tone, and Score/Music.  
**Effect on the audience:** Delivers a clear, non-muddy acoustic environment where every sound occupies its own frequency band and spatial depth.  
**Used for and where it works best:** Universal standard across professional cinema, television, and high-end video production. Essential for global localization.  
**Best in:** formats: All video production | genres: All  
**Avoid when:** Dumping all audio into a single stereo scratch track where nothing can be adjusted later.  
**Example:** `stems: Stem_1_Dialogue | Stem_2_SFX | Stem_3_Ambience | Stem_4_Music — four separate files, all four generated, all four delivered; their balance against each other is set in the edit.`  
`soundscape.stem_master_architecture`

---

### Dry Dialogue Stem Processing

**Also called:** clean dialogue bus, vocal isolation, VO EQ carve  
**What it is:** The dialogue stem is delivered dry and clean — no reverb, no space, no effect printed into it — so that everything the mix wants to do to it is still possible. The processing order it will meet in the edit is settled craft: rumble off first, then sibilance, then gentle levelling, then presence. Where each of those sits, and how much of each, is set in the edit on the actual voice.  
**Effect on the audience:** Produces crystal-clear, intimate vocal intelligibility without harsh sibilance or low-end chest rumble.  
**Used for and where it works best:** All narration and dialogue tracks before they are mixed with foley and orchestral music.  
**Best in:** formats: All formats | genres: All  
**Avoid when:** Printing reverb or any creative effect into the delivered dialogue stem, which takes the decision away from the edit and cannot be undone.  
**Example:** `handover: dialogue stem is dry and unprocessed. In the edit: rumble out, sibilance tamed, levelled gently, presence lifted — in that order, by ear.`  
`soundscape.stem_dialogue_dry`

---

### Physical Foley & Action Effects Stem

**Also called:** practical foley, contact audio, tactile realism  
**What it is:** Specific sounds produced by physical human action and material interaction: footsteps, rustling cloth, weapon unsheathing, doors opening.  
**Effect on the audience:** Grounds AI-generated imagery in physical reality; the viewer believes what they see because they hear its physical weight.  
**Used for and where it works best:** Every on-screen movement: leather sandals on gravel, bronze sword drawn from scabbard, fingers touching stone carvings.  
**Best in:** formats: Film, Animation, Documentary | genres: All  
**Avoid when:** Generic canned stock sound effects that loop identically with every footstep.  
**Example:** `cue: [SFX] Heavy bronze door grinding on stone socket, followed by iron latch clinking.`  
`soundscape.stem_sfx_foley`

---

### Continuous Ambience & Room Tone Bed

**Also called:** background bed, environmental tone, acoustic envelope  
**What it is:** The continuous baseline sound of an environment: room resonance, wind through ruins, distant river flow, night insects.  
**Effect on the audience:** Subconsciously establishes the reality and geography of the scene; prevents jarring dead silence when dialogue pauses.  
**Used for and where it works best:** Lay continuously across entire scenes to bridge camera cuts and maintain acoustic spatial continuity.  
**Best in:** formats: All video and audio formats | genres: All  
**Avoid when:** Cutting the ambience bed abruptly on picture cuts, which causes audible room pops.  
**Example:** `bed: Low dry Mesopotamian desert wind with faint reed rustle along the distant Euphrates shore.`  
**Yields to:** `foley.acoustic_vacuum_drop` — The drop to dead silence is the effect.  
`soundscape.stem_ambience_bed`

---

### Worldised Playback: The Voice Inside the Device

**Also called:** worldizing, diegetic playback, futz, source music in the room, the radio in the scene  
**What it is:** A song or a voice that exists inside the scene (a cassette on a shelf, a radio in a car, a voice on a phone) heard through that device and through the room, instead of laid clean over the picture. Walter Murch's method on American Graffiti: play the clean recording through a speaker in a real space, record it from a distance while speaker and microphone move, and keep the clean track as well, so the mix can travel between them. Two things do the work: the device's band (a telephone carries about 300 to 3400 Hz, the band ITU-T calls telephone-band) and the room around the device (distance, reflections, direction).  
**Effect on the audience:** The sound belongs to the room, so the audience believes it without being told where it comes from. Murch describes the worn track as the sound equivalent of depth of field: dialogue stays sharp in front of a song that has no edges to catch the ear. When a character picks the device up, the sound comes to them, and the audience moves with the character's attention without a cut.  
**Used for and where it works best:** A dead parent's voice on an old cassette, a song on a café radio, a call the audience hears only from one end, a car radio in a period street. The pickup is the move: as the hand lifts the device, bring the room down (less reverb, less distance, level up to dialogue height) and keep the device's band, because a cassette in the hand is still a cassette and a phone at the ear is still telephone-band. Go from the device to the clean recording only when the story wants the listener inside the memory, and let that be its own cut.  
**Best in:** formats: Feature Film, Drama Series, Short Film, Music Video, Documentary | genres: Drama, Period, Family, Heritage (civilisation-focused), Mystery  
**Avoid when:** The music is score, not an object in the room, and the audience must hear it at full width.  
**Example:** `playback: source: 1980s cassette on a kitchen shelf | band: narrow, tape hiss, slight wow | room: tiled kitchen, 4 m away, off-axis | pickup at 0:12: room and distance fade over the lift, device band held, level to dialogue height | clean master held back for the memory cut`  
**Source:** reference — Lucas O. Seastrom, "'Music as Mist': Sound Designer Walter Murch Looks Back on American Graffiti, 50 Years Later", Lucasfilm.com, 2023-08-29, https://www.lucasfilm.com/news/walter-murch-american-graffiti/, checked 2026-09-24; supports the speaker-and-microphone re-recording in a real space, the clean program kept beside two atmospheric tracks in the mix, and Murch's depth-of-field comparison. ITU-T Recommendation P.310 (02/96), "Transmission characteristics for telephone-band (300-3400 Hz) digital telephones", https://www.itu.int/rec/T-REC-P.310-199602-S/en, checked 2026-09-24; supports the 300-3400 Hz telephone band (the recommendation is superseded; the band is the one its title names). The order of the pickup blend is the package's working method, set by ear on the mix.  
**Yields to:** `soundscape.stem_ambience_bed` — The device is never shown or touched and the song is only part of the room's bed.  
`soundscape.worldised_device_playback`

---

### Melodic & Harmonic Underscore Stem

**Also called:** dramatic score, emotional bed, musical underscore  
**What it is:** The composed music track providing thematic continuity, subtextual emotion, and rhythmic momentum beneath the scene.  
**Effect on the audience:** Tells the viewer how to feel about what they are seeing; prepares subconscious emotional responses seconds before visual climaxes.  
**Used for and where it works best:** Supporting narrative themes, building dramatic tension, and establishing cultural identity.  
**Best in:** formats: Film, Series, Documentary, Trailer | genres: All  
**Avoid when:** Mickey-Mousing (literally mimicking every on-screen action with musical hits), which insults the viewer's intelligence.  
**Example:** `cue: Solitary ancient Ney flute drone in D minor, accompanied by bowed bass viol holding sustained fifth.`  
`soundscape.stem_music_score`

---

### Dynamic Dialogue Ducking Ratio

**Also called:** sidechain ducking, music dips, speech priority curve  
**What it is:** The standing intent that music and ambience move *out of the way* of speech and come back when the speech stops — automatically, triggered by the voice itself, not ridden by hand line by line. **How far they move is a level, and it is set in the edit.** It is not one figure: a sparse drone under a calm read barely needs to move, and a full orchestral cue under the same read has to move a long way. This package carried two different figures for this one move for exactly that reason; the figure is now the editor's, and what is written down is the requirement.  
**Effect on the audience:** Guarantees full voiceover comprehension without sacrificing the perceived power and richness of the music track — on a cue written with a place for the voice (`sync.instrumental_break_dialogue_window`); a duck moves a cue out of the way, it cannot carve the hole a cue was built without.  
**Used for and where it works best:** Every mix with narration over music. The music bus is driven by the dialogue bus rather than automated by hand, so the duck follows the performance rather than a guess about it.  
**Best in:** formats: All video with voiceover | genres: All  
**Avoid when:** Abrupt, jagged ducking that pumps music noticeably like an EDM sidechain track — see `mix.ducking_release_curve` for how the return is shaped.  
**Example:** `handover: music and ambience duck to the voice, automatically, and recover on the pauses. Depth set by ear per cue — enough that no word has to be replayed, no more than that.`  
**Yields to:** `soundscape.narration_song_handover` — The song takes the film over, no voice to duck under.  
`soundscape.ducking_ratio`

---

### Arid Desert Wind Ambience

**Also called:** steppe atmosphere, ancient Mesopotamian plain, wasteland tone  
**What it is:** High-altitude, dry wind whistling through arid plains and scorched scrub, accompanied by fine sand sift against stone.  
**Effect on the audience:** Evokes vast emptiness, harsh climate, historical antiquity, and civilizational vulnerability.  
**Used for and where it works best:** Exterior shots of archaeological mounds (Tells), Sumerian plains, Babylonian desert approaches, and ruin surveys.  
**Best in:** formats: Heritage / Historical Documentary, Epic Film | genres: Heritage (civilisation-focused), History, Survival  
**Avoid when:** Modern urban scenes or dense lush tropical jungles. Also the rain-fed Assyrian north — Nineveh, Nimrud, Khorsabad — outside its dry summer months: that heartland was cereal plain with a wet winter, not desert (sourced on `meso_stage.winged_bull_gatekeeper_threshold`).  
**Example:** `ambience: Desolate hot wind blowing over dry clay mounds, faint grit pelting against weathered stone relief.`  
**Yields to:** `soundscape.river_civilisation` — Marsh, canal or any wet setting.  
`soundscape.ancient_desert_ambience`

---

### Ancient Palace Megaron Acoustics

**Also called:** throne room reverberation, royal hall acoustics  
**What it is:** Large acoustic space with high ceilings and heavy limestone or basalt walls: a long cold tail, a hard slap off glazed brick, and a low rumble underneath. The character is specified here; the impulse response chosen to produce it, its decay time and how wet it sits are set in the edit.  
**Effect on the audience:** Magnifies royal authority and power; makes human presence feel small inside monumental imperial architecture.  
**Used for and where it works best:** Scenes in Assyrian royal palaces (Nimrud, Nineveh), Persepolis, or Babylonian throne rooms.  
**Best in:** formats: Historical Epic, Documentary Feature | genres: Historical / Biopic, Heritage (civilisation-focused), Drama  
**Avoid when:** Intimate bedroom conversations or small mud-brick village huts.  
**Example:** `handover: throne-room scene — voice and footsteps belong to a huge cold stone hall, long tail, hard slap off glazed brick. Match it with a real hall IR in the edit.`  
**Yields to:** `sensory_sonic.voice_intimacy` — Small intimate room, no hall tail.  
`soundscape.ancient_palace_hall`

---

### Ancient Battlefield Soundscape

**Also called:** ancient combat field, chariot warfare acoustic  
**What it is:** Clash of blades on shields - which metal the blades are depends on the battle's period, so take it from the reference, not from this card - thundering two-wheeled chariot wheels, war horns, and guttural battle shouts.  
**Effect on the audience:** Delivers raw, terrifying visceral combat distinct from modern gunpowder or Hollywood stock steel sword ringing.  
**Used for and where it works best:** Battle sequences of Ashurbanipal, Ramesses II at Kadesh, or the fall of Nineveh, each with its own period's weapons from the reference.  
**Best in:** formats: Epic Film, Historical Animation | genres: War, Historical / Biopic, Action  
**Avoid when:** Romantic or diplomatic court sequences.  
**Example:** `foley: Heavy thud of spear tips against wooden shields; war horns blaring across dusty plain.`  
**Yields to:** `soundscape.ancient_palace_hall` — A court or diplomatic sequence.  
`soundscape.ancient_battlefield`

---

### Riverine Civilization Waterway Ambience

**Also called:** Euphrates waterscape, marsh reed bed, canal life  
**What it is:** Gentle lapping of fresh water against reed bundles (mashoof boats), rustling giant reeds (Phragmites), water birds, and wooden irrigation paddles.  
**Effect on the audience:** Evokes life, fertility, peace, and the cradle of civilization; provides acoustic contrast to harsh desert warfare.  
**Used for and where it works best:** Southern Mesopotamian marshlands (Ahwar), Sumerian city canals (Ur, Eridu), and agricultural scenes.  
**Best in:** formats: Cultural Documentary, Nature & Heritage | genres: Heritage (civilisation-focused), Nature  
**Avoid when:** Arid mountain fortresses or high desert plateaus.  
**Example:** `ambience: Rhythmic wooden oar stroke through quiet marsh water; rustle of tall papyrus reeds; distant water hen call.`  
**Yields to:** `soundscape.ancient_desert_ambience` — Arid plateau or mountain fortress.  
`soundscape.river_civilisation`


### Coast, Sea and Storm Ambience

**Also called:** shore bed, surf and wind, storm bed, harbour tone  
**What it is:** The continuous bed for sea, shore, coast and storm, and the spot sounds that live inside it: surf breaking and drawing back over sand or shingle, wind in rigging or around a tower, rain on glass, gulls, a distant foghorn, a door creaking in the wind, a cork drawn, a glass set down. The bed runs under the whole scene, inside the world; the spot sounds are lifted out of it when the picture goes to them. This card carries no era line: sea and wind sound the same in any century, and the made things on the list are chosen to fit the scene's own period, which the scene settles, not this card.  
**Effect on the audience:** Places the scene at the edge of the land before anything is shown, and puts the weather's pressure on everyone in it: a steady surf reads as isolation or calm, a rising wind as something coming, rain on glass as the inside of a shelter with the storm held outside it.  
**Used for and where it works best:** Lighthouse and harbour scenes, a cottage or a tavern on the shore in a storm, a ship's deck, a beach at night, a coastal town. Four rules. **Lay the bed first and run it across every cut** — how a bed is laid is `soundscape.stem_ambience_bed`'s craft. **Build the storm in the bed, not in spot hits**: the wind rises and the surf thickens across the scene, so the peak is a place the audience has been climbing toward. **Change the bed with the listening position**: inside a room the storm is muffled and the rain on the glass comes forward; outside, surf and wind are full and the glass is gone, so a cut between inside and outside is a change of bed, not only of level. **Lift one spot sound when the camera goes to its source** — the gull crossing frame, the door swinging, the cork, the glass — and return it to the bed when the camera leaves; `sound.perspective` ties the sound to the size of the shot. On an ancient coast keep the sea and the wind and take every made object on the list from the reference, not from this card.  
**Best in:** formats: Film, Short Film, Series, Documentary, Trailer / Teaser | genres: Drama, Mystery, Thriller, Adventure, Survival  
**Avoid when:** The water is a river, a canal or a marsh — that is lapping and reed, not surf, and a surf bed under a river scene puts the audience in the wrong place at once. Avoid a storm that arrives on a cut with no build in the bed: a storm dropped in at full level is a sound effect, not weather. And where the storm stops and the silence is the point, that is a drop, not a fade.  
**Example:** `bed: steady surf on shingle with a long draw-back, wind rising around a stone tower, rain starting on the lamp-room glass; spot, lifted on the close-up: a door creaking in the wind, then a cork drawn and a glass set down on wood.`  
**Yields to:** `soundscape.stem_ambience_bed` — how the bed is laid, carried across cuts and never cut abruptly: that card's rules govern any bed, and this one only says what is in it. `soundscape.river_civilisation` — the scene is ancient and the water is a river, a canal or a marsh rather than open sea: that bed is the one with an era line. `foley.acoustic_vacuum_drop` — the storm stops and the drop to dead silence is the effect.  
`soundscape.coast_and_storm`
---

### Ancient Bazaar Marketplace Hubbub

**Also called:** oriental souk acoustics, bronze craftsmen street, ancient trade hub  
**What it is:** A dense tapestry of acoustic life: coppersmith hammers clinking on anvils, donkey hooves on cobblestones, aroma sellers, and polyphonic haggling.  
**Effect on the audience:** Immerses the viewer in vibrant commercial prosperity; demonstrates the complexity of ancient urban life.  
**Used for and where it works best:** City center scenes in Babylon, Nineveh, Damascus, or Ur during harvest trade fairs.  
**Best in:** formats: Historical Film, Documentary | genres: Historical, Adventure, Heritage  
**Avoid when:** Desert ruin shots or desolate military outposts.  
**Example:** `sfx: Rhythmic rhythmic tap of small bronze hammer shaping copper bowls; distant chatter in Semitic dialect.`  
**Yields to:** `soundscape.ancient_desert_ambience` — Desert ruin or desolate outpost.  
`soundscape.bazaar_marketplace`

---

### Sacred Temple Sanctuary Drone

**Also called:** ziggurat holy of holies, incense chamber, temple hush  
**What it is:** Deep, subterranean resonance, crackle of cedar and frankincense coals in bronze braziers, low chanting, and clear bronze ceremonial bells.  
**Effect on the audience:** Evokes sacred fear, divine mystery, and ritual solemnity; silences casual modern thoughts.  
**Used for and where it works best:** High ziggurat sanctuaries (E-temen-an-ki), inner chambers of Ishtar temples, and divination rituals.  
**Best in:** formats: Historical Film, Mythological Epic | genres: Mythology, Faith / Biblical Epic, Mystery  
**Avoid when:** Public markets or fast action chase scenes.  
**Example:** `cue: Sub-bass 50Hz singing bowl drone; gentle crackle of olive oil lamps; single pure bronze chime at 2.4kHz.`  
**Yields to:** `soundscape.bazaar_marketplace` — A public market, not a sanctuary.  
`soundscape.temple_sacred_chant`

---

### Historical Garment & Textile Foley

**Also called:** linen and wool rustle, ceremonial fringed robes  
**What it is:** Tactile audio of heavy woven wool robes, pleated linen kilts, fringed shawls, and leather sandals creaking under movement.  
**Effect on the audience:** Communicates class, wealth, and physical reality without requiring dialogue explanation.  
**Used for and where it works best:** King walking down palace steps, high priestesses turning during ritual, soldiers marching in linen armor.  
**Best in:** formats: Cinematic Film, High-End Documentary | genres: Historical / Biopic, Heritage  
**Avoid when:** Synthetics, modern nylon swishes, or denim rustle.  
**Example:** `foley: Heavy wool friction with braided fringe tassels swinging against leather scabbard.`  
`soundscape.foley_ancient_garments`

---

### Cuneiform Scribe Clay & Stylus Foley

**Also called:** cuneiform writing audio, reed stylus on clay  
**What it is:** Wet suction and crisp wedge incisions of a cut reed stylus pressing into wet river clay, followed by the dry click of baked tablets.  
**Effect on the audience:** Connects the viewer intimately to the act of human literacy, archive creation, and preserving memory against oblivion.  
**Used for and where it works best:** Scenes in the Royal Library of Ashurbanipal, contract sealing, and scribal schools (edubba) **on Sumerian, Akkadian and Old Babylonian subjects only** — the two must not share a frame or a soundscape. By the seventh century BC Assyrian scribal training ran through the family and the palace, not a classroom, so the library and the edubba are a thousand years apart; see the box under entry 151 in [`../phase-07-image-prompt-engineering/mesopotamia-canon/clothing-10-neo-assyrian-by-station.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/clothing-10-neo-assyrian-by-station.md).  
**Best in:** formats: Heritage Documentary, Museum Video | genres: Heritage (civilisation-focused), Educational  
**Yields to:** the canon, on any Neo-Assyrian subject — the period rule outranks this card's scene list.  
**Avoid when:** Writing with modern feather quills or ink scratching on paper.  
**Example:** `foley: Moist indentation of triangular reed stylus pressing into pliable river clay tablet.`  
`soundscape.foley_clay_tablets`

---

### High-Impact Cinematic Whoosh Transition

**Also called:** camera whip whoosh, scene riser, velocity sweep  
**What it is:** A fast, textured audio sweep (air rush + low-end tail) aligned with rapid camera moves, whip pans, or fast scene cuts.  
**Effect on the audience:** Accentuates kinetic energy; makes fast visual cuts feel smooth, cohesive, and rhythmically propelled.  
**Used for and where it works best:** Dynamic social reels, fast documentary montages, and dramatic scene transitions.  
**Best in:** formats: Vertical Short-Form, Commercial, Trailer | genres: Action, Trailer, Modern Social  
**Avoid when:** Solemn continuous drama scenes or quiet contemplative documentaries.  
**Example:** `sfx: Textured organic wind whoosh with sub-bass drop on frame 0 of the incoming visual.`  
**Yields to:** `sensory_sonic.gradual_emergence` — A solemn or contemplative piece, the join must not be heard.  
`soundscape.sfx_whoosh_transition`

---

### Sub-Bass Revelation Impact

**Also called:** sub-drop, 50Hz cinematic thud, discovery impact  
**What it is:** A deep low-frequency impact that falls in pitch through the 40Hz to 60Hz band, the same falling sine `foley.sub_drop_50hz` sweeps, with rapid decay, hitting the listener's chest at the exact moment of a monumental discovery.  
**Effect on the audience:** Produces physical visceral weight; marks a plot point or archaeological discovery as an irreversible historic turning point.  
**Used for and where it works best:** The moment the lost tomb is opened, an ancient inscription is deciphered, or a kingdom falls.  
**Best in:** formats: Trailer / Teaser, Feature Documentary, Film | genres: Mystery, Epic, True Crime  
**Avoid when:** Minor informational transitions, which causes ear fatigue.  
**Example:** `cue: 50Hz sub-bass sine drop decaying over 1.2 seconds. It needs headroom underneath it — how much the rest of the mix gives way for it is set in the edit.`  
**Source:** reference — checked 2026-09-23: a sub drop is a sine that falls in pitch inside the sub-bass band, below about 60 to 70 Hz (Wikipedia, *Sub-bass*; Morphic, *Sub drop sound effects*, which adds that small speakers reproduce little down there); no reference fixes its start or end point, so the figures here are a design choice.  
**Yields to:** `soundscape.sfx_whoosh_transition` — A minor informational transition.  
`soundscape.sfx_sub_bass_hit`

---

### Parchment & Manuscript Tactile Foley

**Also called:** scroll unrolling, manuscript rustle, seal crack  
**What it is:** Crisp, dry tactile sounds of papyrus unrolling, vellum leaves turning, and clay/wax bulla seals cracking open.  
**Effect on the audience:** Transports the listener into the physical presence of primary historical documents.  
**Used for and where it works best:** Archival close-ups, reading ancient correspondence, legal verdicts, and secret letters.  
**Best in:** formats: Historical Documentary, Mystery | genres: Historical, Crime, Mystery  
**Avoid when:** Inappropriate eras (e.g. paper in 2000 BC Sumer before paper was invented).  
**Example:** `foley: Dry, stiff papyrus fiber unrolling with delicate fiber creak and clay seal breaking.`  
**Yields to:** `soundscape.foley_clay_tablets` — A pre-paper Mesopotamian era, where writing is clay.  
`soundscape.sfx_paper_parchment`

---

### Minimalist Cinematic Drone Underscore

**Also called:** suspense drone, Icelandic cello bed, atmospheric drone  
**What it is:** A sustained harmonic or dissonant drone (bowed upright bass, analog synth, or processed Tibetan horn) maintaining constant tension.  
**Effect on the audience:** Creates an unbroken undercurrent of suspense without dictating melody or cluttering vocal frequencies.  
**Used for and where it works best:** Underneath complex documentary voiceovers, investigative sequences, and ticking-clock timelines.  
**Best in:** formats: Documentary Series, True Crime, Thriller | genres: Thriller, Mystery, Documentary  
**Avoid when:** Uplifting celebratory montages or fast comedic sequences.  
**Example:** `score: Low C drone with subtle pitch-bend micro-variations and 80Hz resonant filter sweep.`  
**Yields to:** `soundscape.score_ethnic_instrumentation` — A heritage subject that needs regional timbre.  
`soundscape.score_minimal_drone`

---

### Mesopotamian & Mediterranean Regional Instrumentation

**Also called:** regional scoring, traditional timbre  
**What it is:** Scoring with the culturally rooted instruments of the region's living traditions: Oud, Ney flute, Qanun, Frame Drum (Daf/Riq), and Sistrum. Present them as the region's traditional sound, not as the instruments of any ancient period - this card does not vouch for that.  
**Effect on the audience:** Places the score in the region's own traditional sound; prevents Hollywood generic orchestral whitewashing.  
**Used for and where it works best:** Mesopotamian, Near Eastern and Mediterranean heritage documentaries and epics, as regional colour - on an ancient subject, credit and narrate it as a modern regional sound, never as period music.  
**Best in:** formats: Heritage / Historical Documentary, Cultural Feature | genres: Heritage (civilisation-focused), World  
**Avoid when:** Contemporary corporate explainers or futuristic sci-fi unless intentionally hybrid.  
**Example:** `instrumentation: Solo acoustic Oud playing Maqam Bayati melody over solitary frame drum pulse.`  
**Yields to:** `soundscape.score_minimal_drone` — Contemporary corporate or sci-fi material.  
`soundscape.score_ethnic_instrumentation`

---

### Signature Sonic Branding Ident

**Also called:** audio logo, channel sting, signature opening mark  
**What it is:** A distinct 1.0 to 2.5 second audio hallmark (e.g. ancient bronze bell chime + low sub hit) played at the start of every release.  
**Effect on the audience:** Triggers immediate brand recognition and anticipation across social media feeds before the viewer even reads the title.  
**Used for and where it works best:** Channel intros for YouTube channels, documentary production brands, and serialized social accounts.  
**Best in:** formats: All digital video channels | genres: All  
**Avoid when:** Theatrical feature films where the main studio ident already exists.  
**Example:** `ident: Resonant Sumerian temple bell chime (E4) fading into warm stereo sub-swell (duration: 1.8s).`  
**Source:** assumption — the package's working figure, not a published standard; set it by timing the rendered ident.  
`soundscape.sonic_branding_signature`

### The Handover Between Narration and Song

**Also called:** the song takes over, narration drop-out, the return to voice, the two-clock join  
**What it is:** The two moments in a piece where a **song stops being underscore and becomes the film** — the narration stops, the picture cuts to the music's structure — and where it hands back. Both are joins between two different clocks, and both are usually designed only in one direction: the drop into the song gets attention because it is the exciting one, and the return gets none, which is why the return is where these pieces fail.  
**Effect on the audience:** Done properly the audience does not experience a transition at all; they experience the film changing gear. Done badly the song sounds like it started, which turns a passage of film into an interruption, and the narrator's return sounds like an announcement that the nice part is over.  
**Used for and where it works best:** A documentary with a sung lament at its centre, a heritage piece built around an anthem, a drama that gives three minutes to a performance. Four decisions, and the last one is the one that gets forgotten.  
**1. Overlap, do not abut.** Start the music **under the last narrated sentence**, quietly, so the song is already present before it is noticed, and let the narration finish into it. A song that begins in silence after a full stop announces itself as a new section. Coming back, do the reverse: the narrator's first line lands over the song's final phrase, not after it.  
**2. Take the key and the room from the voice.** A narrator's voice has a pitch centre and a recorded space. Entering on a chord that fights that pitch, or in an acoustic several rooms larger, makes the join audible even when the level is right. Where a decision is needed, the song yields on the way in — meet the voice where it already is.  
**3. The return needs a reason in the picture.** The music should be arriving at a cadence *and* the picture at a shot that wants a voice — a face, a hand, a return to the place the film started. Coming back on a cut that has no reason is the single most common failure here, and no mixing fixes it.  
**4. What the level does is the edit's decision, written here as intent.** This card sets none: state that the music carries the section alone, that the narrator's return sits over its last phrase, and that the two overlap rather than butt — the numbers are found against the rendered files. `soundscape.ducking_ratio` covers the ordinary case of voice over music; **this is not that case**, because for the length of the sung section there is no voice to duck under.  
**What happens in between is `anime.insert_song_montage`**, which despite its name and its file is the package's only card for *the song taking the film over for a stretch* — cut to the musical phrase, no dialogue underneath — and applies to live action exactly as it does to anime. Record which clock each shot is on in the **Timing src** cell of the Phase 3 shot table.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Music Video, Film, Short Film, Video Essay | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Musical, Tragedy  
**Avoid when:** The song is underscore throughout and never takes the film over — then the ordinary ducking relationship holds and there is no handover to design. Also avoid engineering an elaborate join on a hard-cut piece whose whole grammar is abruptness; there the cut *is* the design, and it is stated rather than smoothed.  
**Example:** `handover: music enters under the final narrated sentence at 02:26, pitch centred on the narrator's own register, same room; narration returns at 05:28 over the lament's last phrase, on the cut back to the wall. Both boundaries provisional, pending_measured_duration.`  
**Yields to:** `soundscape.ducking_ratio` — The song stays underscore and never takes over.  
`soundscape.narration_song_handover`

*(Markers are defined in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set and the rule that each one closes two ways — resolved, or `unobtainable`, with what was done instead.)*
