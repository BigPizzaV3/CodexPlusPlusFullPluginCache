# Commercial Sync and Music Supervision

Music supervision standards, broadcast sync licensing formulas, trailer cue architecture, stem delivery packages, dialogue sidechain ducking, and commercial edit-point engineering.

---

### The Picture Before the Cue

**Also called:** the sync selector, picture before cue, what is this music being asked to sit under  
**What it is:** The card at the head of the `sync.` shelf. It describes no cue. It asks the questions the shelf's own pair graph asks over and over — **are you choosing the music or specifying the file, how much force can the picture absorb, and does the cue hold, build, turn or land** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the twenty-two `Yields to:` conditions the cards carry and the `Avoid when:` boundary on every one of them, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the cue that does reach the screen was chosen against the picture, the voice and the destination, rather than picked because it matched the brief's adjective.  
**Used for and where it works best:** Answer question one **out loud before you open the shelf**, because it decides which half of the shelf you are in and the two halves share no card and no edge. If you are choosing the music, questions two and three leave a shortlist of two to five. If you are specifying the deliverable, there is no second question — there is a list, and it is read against the destination's own written spec, not against this card.  
**Best in:** formats: Commercial Ad, TV Promo, Movie Trailer, Broadcast Bumper, Social Campaign, Film/TV Post-Production Deliverable | genres: all sync genres  
**Avoid when:** **The music is already chosen.** A needle-drop, a licensed master or a client-supplied track is a rights decision made before you arrived, and this map will cheerfully talk you out of the thing you are contractually holding. Also avoid it where **the music is the content** — a music video, a lyric video, an artist release — because half of this map asks what the cue should stay out of the way of, and there is nothing for it to stay out of the way of. And **distrust question one whenever your honest answer is the deliverable half.** Those cards never cite each other: not one of them names another as an alternative, so on that branch this is a list, not a fork, and the list is doing none of the sorting work it does on the cue branch. That branch is also where the package disagrees with itself most sharply — **stem delivery is specified four different ways across four cards, one of them on this shelf** — so what you take off it must be checked against the destination's own spec before anything is rendered.  
**Example:** `[Selector — produces no cue and no prompt. It returns card ids. The chosen card carries the Example.]`  

---

**The axes**

**Axis 1 — Are you choosing the music, or specifying the file you hand over?**
Asked first because this shelf is **two decisions, and the pair graph proves it rather than suggesting it**. Eleven of the shelf's internal edges run between cue cards. The delivery cards hold **zero** internal edges — every one of them either yields outside the shelf entirely (`sync.sync_stems_deliverables_package`, `sync.modular_cutdown_edit_points`, `sync.tempo_locked_cut_point_grid`, `sync.one_stop_licensing_metadata_tagging`, `sync.broadcast_lufs_sync_mastering`) or carries no pair at all (`sync.zero_crossing_split_tail_reverb`, `sync.underscore_dialogue_sidechain_ducking`). **Not one edge crosses between the two halves in either direction.** The clearest tell is the pair `sync.instrumental_break_dialogue_window` and `sync.underscore_dialogue_sidechain_ducking`: one move — get the voice through the music — written twice, once as a composition decision and once as a mix handover, and the shelf never routes between them because they are answers to two different questions asked months apart.

**Axis 2 — How much force can the picture absorb? (asked of the cue half only)**
This is the condition the cue graph repeats most, and every reciprocal pair on the shelf turns on it: `sync.sports_anthem_hyped_stomp_clap_cue` ⇄ `sync.luxury_brand_minimalist_chic` (*"Monster truck rally or budget retail sale"* against *"Delicate luxury jewellery ad"*), `sync.high_octane_action_chase_percussion` ⇄ `sync.heartfelt_non_profit_piano_swells` (*"Wedding vows or peaceful pastoral scene"* against *"High-speed chase or aggressive gaming promo"*), `sync.braam_low_end_cinematic_impact` → `sync.comedy_quirky_pizzicato_bassoon` (*"Romcom, cooking show, children's daytime"*), `sync.horror_thriller_dissonant_drone` → `sync.comedy_quirky_pizzicato_bassoon` (*"Comedy slapstick"*), `sync.tech_innovation_pulsing_arpeggio` → `sync.horror_thriller_dissonant_drone` (*"Dark horror or grimy crime drama"*), `sync.stripped_acoustic_sync_reimagining` → `sync.sports_anthem_hyped_stomp_clap_cue` (*"Fast-paced sports highlight reel"*). **Note what the axis merges and do not repair it:** the comic cue and the luxury cue land on the same value from opposite directions. They feel nothing alike and they permit the same amount of force, and force is the thing the boundaries are actually stated in.

**Axis 3 — Does the cue hold, build, turn, or land? (asked of the cue half only)**
Six conditions are about shape over time rather than tone, and four of them are the same refusal: *"Steady documentary bed, no three-act arc"* (`sync.trailer_three_act_build_structure`), *"Continuous lobby or retail bed, no turn"* (`sync.mood_shift_mid_cue_pivot`), *"Short social loop: key instability confuses listeners"* (`sync.key_and_tempo_shift_act_divider`), *"Club track must mix out: fade, not a button"* (`sync.sync_button_ending_sting`), *"Delicate or comic pivot: practical cue, not a sub drop"* (`sync.sub_drop_and_riser_hit_transition`), *"Quiet contemplative end credits"* (`sync.epic_hybrid_crescendo_sync_finale`). It is asked last because it is the only axis that reaches the shelf's hits, builds and endings at all, and — see **The unasked** — the pair graph reaches almost none of them.

---

**The map**

**Axis 1 — which decision is this**

| Answer | The branch |
| :--- | :--- |
| **You are choosing what the music is** (eighteen) | Go on to Axis 2 and Axis 3 |
| **You are specifying what the file must satisfy** (seven) | Read the delivery table below against the destination's written spec — the brief's, or the destination's published one, searched |

**Axis 2 — how much force can the picture absorb** *(cue half)*

| Answer | The shortlist, by id |
| :--- | :--- |
| **All of it — the picture is already loud and the music is expected to match** (seven) | `sync.braam_low_end_cinematic_impact` · `sync.sub_drop_and_riser_hit_transition` · `sync.high_octane_action_chase_percussion` · `sync.sports_anthem_hyped_stomp_clap_cue` · `sync.epic_hybrid_crescendo_sync_finale` · `sync.trailer_three_act_build_structure` · `sync.mood_shift_mid_cue_pivot` |
| **Some — the picture is grave or tense but quiet, and force would answer a question nobody asked** (six) | `sync.horror_thriller_dissonant_drone` · `sync.heartfelt_non_profit_piano_swells` · `sync.stripped_acoustic_sync_reimagining` · `sync.percussive_ticking_clock_tension` · `sync.sync_button_ending_sting` · `sync.key_and_tempo_shift_act_divider` |
| **None — force would break the thing it is sitting on** (five) | `sync.comedy_quirky_pizzicato_bassoon` · `sync.luxury_brand_minimalist_chic` · `sync.tech_innovation_pulsing_arpeggio` · `sync.instrumental_break_dialogue_window` · `sync.lyrical_ambiguity_broad_licensing` |

**Axis 3 — does it hold, build, turn, or land** *(cue half)*

| Answer | The shortlist, by id |
| :--- | :--- |
| **It holds — a bed that has to survive the whole spot** (eleven) | `sync.instrumental_break_dialogue_window` · `sync.horror_thriller_dissonant_drone` · `sync.heartfelt_non_profit_piano_swells` · `sync.luxury_brand_minimalist_chic` · `sync.tech_innovation_pulsing_arpeggio` · `sync.comedy_quirky_pizzicato_bassoon` · `sync.percussive_ticking_clock_tension` · `sync.stripped_acoustic_sync_reimagining` · `sync.sports_anthem_hyped_stomp_clap_cue` · `sync.high_octane_action_chase_percussion` · `sync.lyrical_ambiguity_broad_licensing` |
| **It builds — the whole cue is one arc and the end is the point** (two) | `sync.trailer_three_act_build_structure` · `sync.epic_hybrid_crescendo_sync_finale` |
| **It turns — one moment where the piece becomes something else** (two) | `sync.mood_shift_mid_cue_pivot` · `sync.key_and_tempo_shift_act_divider` |
| **It lands — a single event, and the rest of the cue is context for it** (three) | `sync.braam_low_end_cinematic_impact` · `sync.sub_drop_and_riser_hit_transition` · `sync.sync_button_ending_sting` |

**Axis 1's second branch — what the receiver is going to do to this file** *(delivery half; this table is the whole map for that branch)*

| What happens to it | The cards, by id |
| :--- | :--- |
| **They will re-cut it to a length you were not told** | `sync.modular_cutdown_edit_points` · `sync.tempo_locked_cut_point_grid` · `sync.zero_crossing_split_tail_reverb` |
| **They will re-balance it underneath something else** | `sync.sync_stems_deliverables_package` · `sync.underscore_dialogue_sidechain_ducking` |
| **They will play it out as it stands, and a machine measures it first** | `sync.broadcast_lufs_sync_mastering` |
| **They will file it, and a stranger has to find and clear it later** | `sync.one_stop_licensing_metadata_tagging` |

**And one thing on that branch is not settled anywhere, so do not let this table pretend it is.** How many stems a sync deliverable consists of is stated in four places in this package and the four do not agree: `sync.sync_stems_deliverables_package` names six groups, `score.four_way_score_stems` names four and binds the handoff from an AI music engine to that number, `song_handoff.stem_separation_protocol` names two, and `lyria.native_multitrack_stems` now says the engine may return none (its adapter in ENGINE-CHECK.md §7). **The number is not corrected here and no winner is picked.** What this card does is name the card that owns the decision: **`sync.sync_stems_deliverables_package`**, because it is the only one of the four whose own `Yields to:` branches on the fact that decides the answer — *no multitrack session to render from* — and routes you out of a stem count you cannot produce. The other three assert a number without asking what generated the music. Ask that question, then read the destination's spec, then render.

*A cue card appears once under Axis 2 and once under Axis 3. The answer is the intersection of the two shortlists, and it is normally two to five cards wide.*

---

**The default, and the one against it**

**The default is `sync.instrumental_break_dialogue_window` shaping the cue and `sync.heartfelt_non_profit_piano_swells` filling it — and the second half of that is measured, while the first half is argued.**

`sync.heartfelt_non_profit_piano_swells` is one of only three cards on the shelf reached on **two distinct conditions**, and it is the only one reached from **opposite ends of Axis 2**: `sync.comedy_quirky_pizzicato_bassoon` sends a reader here when the scene turns out to be grief rather than mischief, and `sync.high_octane_action_chase_percussion` sends one here when the scene turns out to be wedding vows rather than a chase. The loud end and the light end of the shelf both fall back to the same place, and nothing else on the shelf is reached from both. That is what a default looks like under the measure.

**It is worth saying what the measure could not do here.** The highest in-degree on this shelf is two, shared by four cards, because the cue graph is a ring of reciprocal pairs rather than a hub — `sync.sports_anthem_hyped_stomp_clap_cue` and `sync.luxury_brand_minimalist_chic` name each other, `sync.high_octane_action_chase_percussion` and `sync.heartfelt_non_profit_piano_swells` name each other. In-degree alone would have produced a four-way tie. Counting the **conditions** rather than the edges broke it.

`sync.instrumental_break_dialogue_window` is the argued half, and the argument is irreversibility rather than popularity: its own body says a cue written without the hole **cannot be rescued by a mixer afterwards**. It is the one cue-side decision on this shelf that a later stage cannot undo, which is exactly what a default should be — the choice you make when you do not yet know enough to choose, because it is the one that keeps the others open.

**The one against it is `sync.horror_thriller_dissonant_drone`**, and the case for it is structural rather than tonal. Its own Example says *no tempo*. It is the only card on this shelf that cannot be tempo-locked at all — which means choosing it **destroys the shelf's entire delivery branch**: there are no modular cutdown blocks, no frame-aligned grid, no beat for a video editor to cut on. Every other cue here quietly accepts that commercial music is a grid with feeling laid over it. This one refuses the grid, and it is reached exactly once, from `sync.tech_innovation_pulsing_arpeggio` — the shelf's most optimistic, most griddable card. **The shelf's own single route to it is the longest possible jump on it**, which is the shape of a choice nobody makes by drifting. Its near cousin against the grain is `sync.stripped_acoustic_sync_reimagining`, the one card here whose power comes from something the audience already knows rather than from anything the cue does.

---

**The unasked**

**Thirteen of the twenty-five cards are the target of no `Yields to:` field anywhere in the package.** They can be chosen but nothing ever sends you to them. By id:

`sync.sync_button_ending_sting` · `sync.trailer_three_act_build_structure` · `sync.sub_drop_and_riser_hit_transition` · `sync.modular_cutdown_edit_points` · `sync.sync_stems_deliverables_package` · `sync.braam_low_end_cinematic_impact` · `sync.stripped_acoustic_sync_reimagining` · `sync.tempo_locked_cut_point_grid` · `sync.zero_crossing_split_tail_reverb` · `sync.underscore_dialogue_sidechain_ducking` · `sync.key_and_tempo_shift_act_divider` · `sync.one_stop_licensing_metadata_tagging` · `sync.epic_hybrid_crescendo_sync_finale`

**And the shape of that list is the finding, not its length.** Every card under Axis 3's *builds* and *lands* values is on it — all five of them. The only card outside the *holds* value that anything reaches at all is `sync.mood_shift_mid_cue_pivot`, and **both of its inbound edges start at the other two non-bed cards**, `sync.sub_drop_and_riser_hit_transition` and `sync.key_and_tempo_shift_act_divider`. So the pair graph on this shelf routes between beds, and the one time it reaches something that is not a bed, it is a card that is not a bed doing the reaching. **Nothing on this shelf ever says: you have written a bed, and what this spot needs is a single hit.** A cue that happens is not an alternative to a cue that plays; the readers who wrote these fields were each holding one thirty-second bed, and the pair field cannot express a moment. That is why Axis 3 is on this card and why it is asked last rather than not at all.

The second thing the list shows is heavier, and it is where the stem disagreement came from. **Six of the seven delivery cards are on the list, and the seventh is reached only from outside the shelf** — `song_handoff.platform_loudness_mastering` names `sync.broadcast_lufs_sync_mastering`, and that is the only inbound edge the whole delivery branch has. Combined with its zero internal edges, this means **no reader anywhere in the package has ever compared two ways of handing a sync file over.** Every one of those cards was written and audited alone. That is precisely how the same package came to carry four different stem counts without a single `Yields to:` field noticing, and it is why the delivery branch of this map is a list rather than a fork. **The card this shelf wants and does not have is the one that says what you are allowed to deliver is decided by what generated the music** — a session, a stem-capable engine, or a finished stereo file — and that card is the missing head of the branch, not a missing row in it.

`sync.picture_before_the_cue`

---

### Sync Button Ending and Reverb Sting

**Also called:** Button Outro, Clean Tail Ending, Sync Stinger  
**What it is:** Ending a commercial or trailer music track with a decisive, razor-sharp musical hit ("button") followed by a pure, unclouded reverb tail that rings out into silence. Best practice uses a staccato orchestral hit, single acoustic guitar strum with open ringing strings, or sub-boom, strictly avoiding fade-outs.  
**Effect on the audience:** Provides instant finality and visual synchronization for a final brand logo reveal or punchline.  
**Used for and where it works best:** 15s/30s/60s commercial spots, movie trailer ends, and TV show segment bumpers.  
**Best in:** formats: Commercial Ad (15s/30s/60s), TV Promo, Movie Trailer, Broadcast Bumper | genres: Action, Drama, Corporate, Cinematic Rock  
**Avoid when:** Club dance tracks designed for seamless DJ crossfading.  
**Example:** `[Ending: Decisive crisp button hit on final beat, followed by an expansive 4-second natural reverb tail fading cleanly into dead silence]`  
**Source:** assumption — the package's working figure, not a published standard; set the tail length by ear against the logo; the 15s/30s/60s spot lengths are the delivery lengths the client specifies.  
**Yields to:** `suno.outro_and_ending_tags` — Club track must mix out: fade, not a button.  
`sync.sync_button_ending_sting`

---

### Trailer Three-Act Build Structure

**Also called:** Epic Trailer Arc, The Golden 2.5-Minute Cut  
**What it is:** The industry-standard music cue structure: Act 1 (Mystery/Intro with sparse piano/drone), Act 2 (Rhythm entry, escalating percussion/brass), Act 3 (Massive full-orchestral climax, braams, choir, and sudden stop before title stinger). Standard trailer timing cues: Act 1 (0:00-0:45), Act 2 (0:45-1:30), Act 3 (1:30-2:15), and Stinger/Logo (2:15-2:30).    
**Effect on the audience:** Creates a cinematic rollercoaster that builds unbearable hype, drama, and emotional investment.  
**Used for and where it works best:** Theatrical film trailers, video game reveal trailers, and high-stakes cinematic teasers.  
**Best in:** formats: Theatrical Movie Trailer, Video Game Cinematic Teaser, Epic TV Promo | genres: Action, Sci-Fi, Epic Hybrid Orchestral, Thriller    
**Avoid when:** Short 10-second social ads or steady background documentary beds.  
**Example:** `[Structure: Trailer 3-Act structure: Act 1 minimalist haunting piano, Act 2 driving percussion and cello pulse, Act 3 colossal hybrid orchestra and choir climax, final stinger hit]`  
**Yields to:** `soundscape.score_minimal_drone` — Steady documentary bed, no three-act arc.  
`sync.trailer_three_act_build_structure`

---

### Instrumental Break Dialogue Window

**Also called:** The Speech Pocket, Sync Mid-Frequency Notch  
**What it is:** Writing the passage so that it has a hole in it where the voice goes: mid frequencies thinned, percussion density dropped, melodic leads kept out of the speech register. This is a **composition** decision and it shapes what gets generated — a cue built this way needs almost nothing done to it later, and a cue built without the hole cannot be rescued by a mixer. Whatever ducking the mix then applies on top is set in the edit (`soundscape.ducking_ratio`).    
**Effect on the audience:** Allows the audience to hear every word of narration effortlessly while still feeling the underlying emotional rhythm.  
**Used for and where it works best:** Car commercials with voiceover, narrative film scenes, and documentary interview backdrops.  
**Best in:** formats: Narrative Commercial, Documentary Voiceover, Dialogue-Heavy Film Scene | genres: Drama, Documentary, Cinematic Ambient, Acoustic    
**Avoid when:** Lyric-driven music videos where the vocal music is the sole star.  
**Example:** `[Arrangement: Dialogue-friendly arrangement, wide EQ scoop between 1kHz and 3kHz, warm sub bass and ambient pads leaving clear space for actor voiceover]`  
`sync.instrumental_break_dialogue_window`

---

### Sub Drop and Pitch Riser Transition

**Also called:** Cinematic Impact FX, The Whoosh Hit  
**What it is:** A pairing of a rising white-noise or string pitch sweep ("riser") that resolves into a colossal low-frequency sine wave impact (40-60 Hz "sub drop") on the downbeat. Typically positioned on the downbeat of Act 2 or Act 3, ensuring the sub drop is mono-centered to eliminate phase cancellation in theater sound systems.    
**Effect on the audience:** Rattles the cinema seats, grabs physical attention, and marks major visual scene transitions.  
**Used for and where it works best:** Scene pivots in action trailers, dramatic reveals, and high-energy product launch spots.  
**Best in:** formats: Action Trailer, Video Game Teaser, High-Impact Commercial Spot | genres: Action, Sci-Fi, Electronic, Hybrid Trailer    
**Avoid when:** Delicate period dramas, intimate romantic whispering, or lighthearted comedy.  
**Example:** `[Transition: Intense 2-bar Shepard tone pitch riser peaking at transition, exploding into massive 50Hz sub drop impact and orchestral hit]`  
**Yields to:** `sync.mood_shift_mid_cue_pivot` — Delicate or comic pivot: practical cue, not a sub drop.  
`sync.sub_drop_and_riser_hit_transition`

---

### Modular Cutdown Edit Points

**Also called:** Grid-Aligned Stems, 15s/30s/60s Broadcast Bins  
**What it is:** Composing music in exact 4-bar or 8-bar self-contained modules with identical tempos, allowing video editors to cleanly cut the track into 15-second, 30-second, or 60-second commercials without awkward edits. Compose at tempos divisible by broadcast video frames (e.g. 120 BPM = 2 beats per second) with each section terminating on a clean transient.    
**Effect on the audience:** Ensures musical phrasing feels custom-tailored to the commercial runtime without sloppy crossfades.  
**Used for and where it works best:** Commercial advertising campaigns requiring broadcast cutdowns across TV, web, and social platforms.  
**Best in:** formats: Broadcast TV Commercial (:15/:30/:60 cutdowns), Social Media Ad Campaign, Promo Bumper | genres: Commercial Pop, Rock, Electronic, Hip-Hop    
**Avoid when:** Freely improvisational jazz or fluctuating rubato classical recordings.  
**Example:** `[Structure: Modular 4-bar blocks, strict 120 BPM tempo grid, natural cut-down edit points every 16 seconds (two 4-bar blocks at 120 BPM), flawless broadcast sync timing]`  
**Source:** assumption — the package's working figure, not a published standard; set the edit points against the rendered track.  
**Yields to:** `lyria.controllable_tempo_curves` — Rubato or improvised material cannot be modularised.  
`sync.modular_cutdown_edit_points`

---

### Sync Stems Deliverables Package

**Also called:** Music Delivery Package, 4-to-8 Stem Split  
**What it is:** Delivering the final composition split into isolated, time-aligned stem groups: Drums/Percussion, Bass, Guitars/Melodic Leads, Pads/Synths, Vocals/Choir, and FX/Hits. All stem groups must be rendered from time 0:00:00 with identical start and end timecodes, printing all reverb tails and delay rings.    
**Effect on the audience:** Enables re-recording mixers to re-balance the music underneath explosions or dialogue, preserving mix clarity.  
**Used for and where it works best:** All professional film, television, video game, and commercial sync licensing agreements.  
**Best in:** formats: Film/TV Post-Production Deliverable, Video Game Audio Implementation, Theatrical Trailer Library | genres: Cinematic, Pop, Electronic, Rock, Orchestral    
**Avoid when:** Delivering a simple un-editable single MP3 file for high-budget commercial production.  
**Example:** `[Stems: Isolated 6-stem deliverable package: (1) Drums & Taikos, (2) Sub & Bass, (3) Lead Strings & Horns, (4) Ambient Pads, (5) Choir Vocals, (6) Riser & Boom FX]`  
**Yields to:** `song_handoff.stem_separation_protocol` — No multitrack session to render from.  
`sync.sync_stems_deliverables_package`

---

### Broadcast LUFS Sync Mastering Standard

**Also called:** EBU R128, ATSC A/85, Streaming Target  
**What it is:** The fact that a sync placement lands somewhere with a **published, enforced loudness standard** — broadcast television and the streaming platforms each run their own — and that a track delivered outside it will be turned down or rejected rather than admired. Which standard applies is a delivery fact and is declared here with the destination; the figure belongs to that body on the day, is looked up then, and is set at master time in the edit. These standards are revised, so a figure copied out of this card is a figure that has stopped being checked.    
**Effect on the audience:** Prevents harsh, jarring volume spikes during commercial breaks, ensuring crystal-clear playback without distortion.  
**Used for and where it works best:** Television broadcast advertising, theatrical film mixing, and YouTube/Spotify sync placements.  
**Best in:** formats: Broadcast Television Ad, Streaming Platform Promo (Netflix/Hulu/Amazon), Theatrical Feature | genres: Cinematic, Commercial, Pop, Electronic, Hip-Hop    
**Avoid when:** Squashing the track for loudness before delivery — a destination that normalises will simply undo it, and the dynamics do not come back.  
**Example:** `handover: sync destination is <broadcast body / platform> — master to that body's current published loudness standard with true-peak headroom, checked on the day of delivery.`  
**Yields to:** The destination broadcast body's or platform's current published loudness standard (not a card) — Figure is theirs, checked on the day.  
`sync.broadcast_lufs_sync_mastering`

---

### Lyrical Ambiguity for Broad Licensing

**Also called:** Sync-Friendly Lyrics, Universal Theme Writing  
**What it is:** Writing song lyrics that focus on universal emotional archetypes (overcoming obstacles, homecoming, rising up, unstoppable joy) while strictly avoiding specific names, places, dates, or explicit brands. Lean into universal anthemic phrases such as "We are rising", "Coming home", "Nothing can stop us now", and "Hold on to the light".    
**Effect on the audience:** Allows the music supervisor to place the song across dozens of different brands (automotive, sports, telecomm, healthcare).  
**Used for and where it works best:** Commercial sync songwriting, brand campaign themes, and movie credits licensing.  
**Best in:** formats: Commercial Sync Licensing, TV Episode Placement, Brand Campaign Theme | genres: Indie Pop, Folk, Anthem Rock, Uplifting Pop    
**Avoid when:** Ultra-specific autobiographical stories naming specific ex-partners, street addresses, or obscure niche brands.  
**Example:** `[Lyrics: Universal sync themes: 'Stand tall through the storm / We were made to break through / Here comes the sunrise', broadly licensable inspirational hook]`  
**Yields to:** `hook_psych.lyrical_specificity_anchoring` — Autobiographical specificity wanted over licensability.  
`sync.lyrical_ambiguity_broad_licensing`

---

### Braam Low-End Cinematic Impact

**Also called:** Inception Horn, Foghorn Hit, Trailer Braam  
**What it is:** An aggressive, heavily distorted hybrid sound combining brass instruments (trombones, tubas) with detuned analog synthesizer saw waves, processed through extreme saturation and cavernous reverb. Pitch the impact note between F0 and C1, spacing successive braams at least 4 to 8 bars apart to retain maximum shock value.    
**Effect on the audience:** Delivers terrifying physical weight, impending doom, and jaw-dropping cinematic scale.  
**Used for and where it works best:** Sci-fi trailers, monster movie reveals, dark psychological thrillers, and post-apocalyptic teasers.  
**Best in:** formats: Blockbuster Theatrical Trailer, Dark Thriller Promo, Epic Sci-Fi Teaser | genres: Cinematic, Sci-Fi, Thriller, Action    
**Avoid when:** Delicate romantic comedies, lighthearted cooking shows, or daytime children's programming.  
**Example:** `[Sound FX: Massive cinematic trailer Braam hit, distorted French horn layered with analog saw bass, earth-shaking sub resonance, vast hall reverb tail]`  
**Yields to:** `sync.comedy_quirky_pizzicato_bassoon` — Romcom, cooking show, children's daytime.  
`sync.braam_low_end_cinematic_impact`

---

### Percussive Ticking Clock Tension Cue

**Also called:** The Time Bomb Motif, Countdown Bed  
**What it is:** A steady, relentless 16th-note or 8th-note ticking percussion element (metallic clock, watch escapement, woodblock, muted guitar click) that underpins an escalating orchestral or synth cue. Pan ticking elements slightly off-center and apply subtle pitch modulation or acceleration as narrative deadlines approach.    
**Effect on the audience:** Generates unbearable psychological urgency, reminding the audience that time is running out.  
**Used for and where it works best:** Heist scenes, bomb defusal sequences, countdown trailers, and courtroom thriller climaxes.  
**Best in:** formats: Investigative Documentary, Crime Thriller Scene, Time-Bomb Heist Sequence | genres: Thriller, Drama, Mystery, Suspense Underscore    
**Avoid when:** Relaxed pastoral scenes, carefree beach vacations, or nostalgic slow dance scenes.  
**Example:** `[Percussion: Relentless mechanical clock ticking rhythm at 130 BPM, layered with low staccato cello ostinato and rising synth pulse, maximum psychological tension]`  
**Yields to:** `genre.bossa_nova_smooth_jazz_nylon` — Carefree beach or relaxed pastoral scene.  
`sync.percussive_ticking_clock_tension`

---

### Stripped Acoustic Sync Reimagining

**Also called:** Melancholic Cover, The Trailerized Slowdown  
**What it is:** Taking a world-famous, upbeat classic pop or rock song and re-recording it as a haunting, slow-tempo ballad featuring only a solo piano, weeping cello, and intimate whisper vocals. Re-track at half-time tempo using minor chord substitutions on familiar major melodies and close-miked breathy vocals.    
**Effect on the audience:** Leverages massive cultural recognition while reinterpreting it with dark, haunting emotional gravity.  
**Used for and where it works best:** Dystopian action trailers, psychological horror game reveals, and prestige drama teasers.  
**Best in:** formats: Dramatic Film Trailer, Melodrama Climax, Haunting Character Promo | genres: Indie Acoustic, Cinematic Folk, Dark Ballad, Minimal Piano    
**Avoid when:** Lighthearted party commercials or fast-paced sports highlight reels.  
**Example:** `[Style: Haunting slow acoustic trailer reimagining of classic anthem, 60 BPM, sparse melancholic piano chords, solo weeping cello, intimate whispered female vocal, cinematic pathos]`  
**Yields to:** `sync.sports_anthem_hyped_stomp_clap_cue` — Fast-paced sports highlight reel.  
`sync.stripped_acoustic_sync_reimagining`

---

### Tempo-Locked Cut-Point Grid

**Also called:** Frame-Rate Beat Sync, Quantized Video Editing  
**What it is:** Composing music at tempos that align mathematically with standard video frame rates (24 fps, 30 fps, 60 fps), ensuring that musical beats hit exact integer video frames. Lock to standard frame rates: 120 BPM (1 beat = 12 frames at 24fps, 15 frames at 30fps) or 90 BPM (1 beat = 16 frames at 24fps, 20 frames at 30fps).    
**Effect on the audience:** Video cuts and musical transients line up with microsecond perfection, eliminating jittery off-beat editing.  
**Used for and where it works best:** High-end TV commercial editing, music video production, and dance choreography video cuts.  
**Best in:** formats: Fast-Paced Action Commercial, Rhythm-Cut Montage, Broadcast Promo | genres: Electronic, Hip-Hop, Action Percussion, Industrial    
**Avoid when:** Organic acoustic rubato scoring where tempo breathes freely without click.  
**Example:** `[Production: Strictly quantized 120 BPM tempo grid, mathematically aligning every quarter note to exactly 12 video frames at 24fps for surgical edit synchronization]`  
**Source:** assumption — the package's working figure, not a published standard; the frame counts are arithmetic (60 ÷ BPM × fps) and the tempo choice is craft; check it on the edit timeline.  
**Yields to:** `lyria.controllable_tempo_curves` — Organic acoustic scoring without a click.  
`sync.tempo_locked_cut_point_grid`

---

### Mood-Shift Mid-Cue Pivot

**Also called:** The 30-Second Turn, The Narrative Switch  
**What it is:** Composing a track that begins in one emotional state (e.g. peaceful, tranquil morning) and pivots abruptly at the 15-second or 30-second mark into a totally different mood (high-octane action or dark tragedy). Bridge the genre pivot with an abrupt practical audio cue: vinyl scratch, tape stop, phone drop, or sub-drop transient.    
**Effect on the audience:** Drives powerful storytelling in 30-second commercials, taking the viewer from problem to solution or calm to catastrophe.  
**Used for and where it works best:** Problem-solution TV commercials (insurance, cybersecurity, automotive safety) and dramatic teasers.  
**Best in:** formats: Narrative Commercial with Twist, Comedy/Drama Promo, Viral Social Campaign | genres: Quirky Comedy, Commercial Pop, Dramatic Tension    
**Avoid when:** Continuous background mood music for hotel lobbies or retail stores.  
**Example:** `[Arrangement: 0:00-0:15 serene acoustic guitar and birdsong, abrupt vinyl stop sound effect at 0:15, bursting into 0:16-0:30 furious high-octane rock guitar chase]`  
**Yields to:** `genre.ambient_drone_ethereal_soundscape` — Continuous lobby or retail bed, no turn.  
`sync.mood_shift_mid_cue_pivot`

---

### Sports Anthem Hyped Stomp-Clap Cue

**Also called:** Stadium Rock, Jock Jam, Arena Stomp  
**What it is:** Energetic, driving cue built on thundering foot stomps, hand claps, distorted blues-rock guitar riffs, pounding acoustic toms, and shouted group vocal chants ("Hey!", "Yeah!"). Drive at 100-115 BPM with four-on-the-floor kick, gritty distorted bass riffs, and cavernous room reverb on stomps and claps.    
**Effect on the audience:** Sparks adrenaline, stadium solidarity, athletic determination, and physical excitement.  
**Used for and where it works best:** NFL/Premier League sports broadcasts, truck commercials, beer ads, and competitive workout montages.  
**Best in:** formats: Sports Hype Reel, Athletic Apparel Commercial, Stadium Game Intro | genres: Blues Rock, Stomp Rock, Urban Anthem, High-Energy Rock    
**Avoid when:** Delicate luxury jewelry ads, quiet nature documentaries, or somber historical retrospectives.  
**Example:** `[Style: Arena Sports Rock, 108 BPM, thundering stadium stomps and claps, gritty distorted blues-rock guitar riff, heavy tom groove, shouting group crowd vocals, explosive hype]`  
**Yields to:** `sync.luxury_brand_minimalist_chic` — Delicate luxury jewellery ad.  
`sync.sports_anthem_hyped_stomp_clap_cue`

---

### Luxury Brand Minimalist Chic Cue

**Also called:** Haute Couture Sound, Minimalist Electronic Chic  
**What it is:** Restrained, elegant production featuring sparse sub-bass pulses, clicking rimshots, filtered warm electric piano chords, subtle tape hiss, and cool, breathy, understated vocal adlibs. Set tempo at 110-120 BPM, emphasizing expansive negative space, crisp dry transients, and zero melodic clutter.    
**Effect on the audience:** Exudes wealth, exclusivity, modern sophistication, and effortless cosmopolitan cool.  
**Used for and where it works best:** High-fashion runway commercials, luxury perfume ads, high-end architecture walk-throughs, and luxury watch showcases.  
**Best in:** formats: High-Fashion Runway Commercial, Luxury Perfume Ad, Premium Automotive Spot | genres: Minimalist Deep House, Nu-Disco, Ambient Electro, Chic Downtempo    
**Avoid when:** Budget retail discount sales, noisy monster truck rallies, or children's toy ads.  
**Example:** `[Style: Luxury Minimalist Chic, 116 BPM, elegant deep sub-bass pulse, crisp clicking percussion, filtered Rhodes chords, whisper-cool female vocal adlib, spacious haute couture elegance]`  
**Yields to:** `sync.sports_anthem_hyped_stomp_clap_cue` — Monster truck rally or budget retail sale.  
`sync.luxury_brand_minimalist_chic`

---

### Tech Innovation Pulsing Arpeggio Cue

**Also called:** Silicon Valley Sound, Modern Corporate Innovation  
**What it is:** Crisp, forward-moving synthesizer arpeggios (in pristine digital or analog synth tones), accompanied by light acoustic guitar plucks, warm bass pulses, and energetic, polite modern electronic percussion. Pulse at 120-128 BPM with bright ping-pong delay synthesizer arpeggios, warm sub sine bass, and forward-looking major harmonies.    
**Effect on the audience:** Inspires optimism, technological progress, clean efficiency, and human-centered intelligence.  
**Used for and where it works best:** Tech keynotes, AI software product demos, smartphone commercials, and clean energy presentations.  
**Best in:** formats: Silicon Valley Tech Keynote, SaaS Explainer Video, EV Automotive Launch | genres: Organic Ambient, Synthwave, Modern Electronic, Future Tech    
**Avoid when:** Grimy street crime dramas, dark horror films, or rustic antique restorations.  
**Example:** `[Style: Modern Tech Corporate Innovation, 124 BPM, sparkling analog synthesizer arpeggio, light acoustic guitar harmonics, clean punchy electronic kick, optimistic progressive atmosphere]`  
**Yields to:** `sync.horror_thriller_dissonant_drone` — Dark horror or grimy crime drama.  
`sync.tech_innovation_pulsing_arpeggio`

---

### Horror Thriller Dissonant Drone Cue

**Also called:** Creepy Sound Design, Dissonant String Cluster  
**What it is:** Unsettling, atmospheric sonic beds featuring screeching violin glissandos, dissonant microtonal clusters (Penderecki style), low rumbling sub drones, and sudden metallic scrape sound effects. Compose in unmetered free time, layering bowed cymbal scrapes, waterphone harmonics, and low-frequency rumble below 40 Hz.    
**Effect on the audience:** Triggers physical goosebumps, claustrophobic dread, and psychological terror.  
**Used for and where it works best:** Psychological horror films, supernatural thriller reveals, haunted location scenes, and true crime documentaries.  
**Best in:** formats: Psychological Horror Feature, Crime Thriller Teaser, Haunting Mystery Episode | genres: Dark Ambient, Industrial Drone, Avant-Garde Dissonance, Horror Score    
**Avoid when:** Cheerful family reunions, comedy slapstick, or fitness workouts.  
**Example:** `[Style: Psychological Horror Underscore, no tempo, screeching dissonant string clusters, bowed metallic waterphone scrapes, deep subterranean sub drone, claustrophobic dread atmosphere]`  
**Yields to:** `sync.comedy_quirky_pizzicato_bassoon` — Comedy slapstick.  
`sync.horror_thriller_dissonant_drone`

---

### Heartfelt Non-Profit Piano Swells Cue

**Also called:** Humanitarian Score, Empathy Piano  
**What it is:** Simple, deeply emotional upright piano chords played with gentle pedal action, accompanied by warm, swelling acoustic string quartets and a soaring, melancholic cello solo. Set at 65-75 BPM with delicate velocity-sensitive upright piano, warm room acoustics, and swelling chamber strings.    
**Effect on the audience:** Melts emotional defenses, evokes deep empathy, compassion, and motivates charitable action.  
**Used for and where it works best:** Humanitarian charity appeals, emotional hospital recovery stories, environmental conservation spots, and poignant family reunions.  
**Best in:** formats: Humanitarian Charity Appeal, Emotional Brand Storytelling, Biographical Documentary | genres: Neo-Classical, Emotional Piano, Cinematic Chamber, Acoustic Heartfelt    
**Avoid when:** High-speed car chases, aggressive gaming promos, or satirical black comedies.  
**Example:** `[Style: Heartfelt Cinematic Empathy, 70 BPM, delicate upright piano melody with pedal noise, warm acoustic cello and violin swells, tender emotional build, humanitarian warmth]`  
**Yields to:** `sync.high_octane_action_chase_percussion` — High-speed chase or aggressive gaming promo.  
`sync.heartfelt_non_profit_piano_swells`

---

### Comedy Quirky Pizzicato and Bassoon Cue

**Also called:** Sneaky Whimsical Cue, Mischief Bed  
**What it is:** Playful, tiptoeing rhythm played on plucked violin strings (pizzicato), staccato bassoon, xylophone, and muted tuba, featuring quirky chromatic walk-downs. Bounce at 110-125 BPM with swinging pizzicato violins, dry close-mic bassoon, and strategic comedic rests.    
**Effect on the audience:** Signals mischief, lighthearted humor, awkward blunders, and comedic curiosity.  
**Used for and where it works best:** Comedy sketches, awkward romantic situations, curious pet commercials, and animated shorts.  
**Best in:** formats: Family Comedy Feature, Lighthearted Commercial, Animated Short | genres: Quirky Orchestral, Pizzicato Pop, Cartoon Acoustic, Whimsical Comedy    
**Avoid when:** Serious political debates, tragic grief scenes, or intense action shootouts.  
**Example:** `[Style: Quirky Comedy Pizzicato, 118 BPM, plucked staccato violins, bouncy whimsical bassoon, playful xylophone accents, sneaky tiptoe rhythm, humorous mischief]`  
**Yields to:** `sync.heartfelt_non_profit_piano_swells` — Tragic grief scene, not mischief.  
`sync.comedy_quirky_pizzicato_bassoon`

---

### High-Octane Action Chase Percussion Cue

**Also called:** Tactical Drum Ensemble, Pursuit Score  
**What it is:** Relentless, fast-paced percussion-only or heavy-industrial cue featuring Japanese taikos, orchestral bass drums, metal trash cans, anvil clangs, and fast syncopated 16th-note shakers. Drive at 140-160 BPM with heavily compressed room mics, accelerating polyrhythmic percussion, and sub-boom visual accents.    
**Effect on the audience:** Pushes adrenaline to the redline, conveying breathless pursuit, physical danger, and kinetic velocity.  
**Used for and where it works best:** Rooftop chases, military tactical breaches, car pursuit sequences, and intense action gaming trailers.  
**Best in:** formats: Action Movie Chase Sequence, High-Speed Thriller, Video Game Combat Cue | genres: Hybrid Orchestral Percussion, Action Industrial, Cinematic Taiko    
**Avoid when:** Peaceful pastoral picnics, wedding vows, or quiet library study scenes.  
**Example:** `[Style: Massive Action Chase Percussion, 150 BPM, thundering taiko drums, metallic anvil strikes, aggressive syncopated tom fills, driving pursuit rhythm, intense adrenaline rush]`  
**Yields to:** `sync.heartfelt_non_profit_piano_swells` — Wedding vows or peaceful pastoral scene.  
`sync.high_octane_action_chase_percussion`

---

### Zero-Crossing Split-Tail Reverb Engineering

**Also called:** Clean Stems Splice, Reverb Isolation  
**What it is:** The engineering standard of cutting music audio files precisely at zero-crossing points on the waveform and printing separate reverb tail audio files ("ring-outs") that video editors can place across scene cuts. Cut strictly at sample-accurate zero crossings and export a dedicated 5-to-6 second isolated reverb ring-out tail file.    
**Effect on the audience:** Eliminates ugly digital clicks and pop glitches when music is cut or rearranged on the timeline.  
**Used for and where it works best:** Professional DAW and NLE audio handoffs (Premiere Pro, DaVinci Resolve, Final Cut).  
**Best in:** formats: Trailer Music Library Deliverable, NLE Video Editor Asset Pack, Game Audio Stems | genres: All sync genres (Cinematic, Rock, Electronic, Trailer)    
**Avoid when:** Rough demo mp3 exports where professional delivery standards are not required.  
**Example:** `[Audio Engineering: Sample-accurate zero-crossing audio cut, accompanied by an isolated 6-second natural reverb tail stem for smooth video editor crossfades]`  
**Source:** assumption — the package's working figure, not a published standard; set the tail length from the reverb's measured decay in the rendered stem.  
`sync.zero_crossing_split_tail_reverb`

---

### Underscore Dialogue Sidechain Ducking

**Also called:** Automatic Speech Ducking, Voiceover Priority Mix  
**What it is:** A handover note about the *shape* of the duck rather than its size. Instead of pulling the whole music bus down when the voice arrives, the duck is made **narrow** — it opens only the mid band the speech actually occupies, so the bass and the top of the cue keep their weight and the music never appears to shrink. Which band, how deep, how fast it opens and how slowly it recovers are all set in the edit against the actual cue and the actual voice. **No figure is written here on purpose:** this card and `soundscape.ducking_ratio` used to carry different numbers for the same move, which is what happens when a card tries to settle a level it will never hear.    
**Effect on the audience:** Keeps dialogue fully intelligible while allowing the music to surge up in energy during dramatic pauses without perceived loss of bass or high-end impact.  
**Used for and where it works best:** Feature film post-production, commercial broadcasting, and podcast narrative scoring.  
**Best in:** formats: Feature Film Dialogue Scene, Documentary Narrative Underscore, Commercial Voiceover Bed | genres: Cinematic Ambient, Minimal Acoustic, Drama Underscore    
**Avoid when:** Pure music listening releases without dialogue.  
**Example:** `handover: duck the music narrow, in the speech band only, triggered by the voice — not the whole bus. Depth and timing by ear in the edit; the overall speech-priority balance is mix.dialogue_to_music_ratio.`  
`sync.underscore_dialogue_sidechain_ducking`

---

### Key and Tempo Shift Act Divider

**Also called:** The Modulation Bridge, Scene Transposition  
**What it is:** Shifting the key signature up by a half-step or minor third (e.g. D minor to F minor) while modulating the tempo from half-time to double-time across a visual act transition. Execute key and tempo modulations over a masking transitional FX hit (sub drop, whoosh, or heavy percussion roll).    
**Effect on the audience:** Subconsciously signals that the story has advanced into a higher gear or a new location.  
**Used for and where it works best:** Multi-scene commercials, montage sequence bridges, and video game phase transitions.  
**Best in:** formats: Multi-Scene Commercial, Act 2 to Act 3 Film Climax, Video Game Phase Transition | genres: Hybrid Orchestral, Epic Electronic, Dynamic Rock    
**Avoid when:** Short static social loops where key instability confuses listeners.  
**Example:** `[Composition: Act 1 in D minor at 75 BPM half-time, transitioning via cymbal swell into Act 2 in F minor at 150 BPM double-time, dramatic emotional escalation]`  
**Yields to:** `sync.mood_shift_mid_cue_pivot` — Short social loop: turn it without key instability.  
`sync.key_and_tempo_shift_act_divider`

---

### One-Stop Licensing Metadata Tagging

**Also called:** Sync Metadata Standard, ID3 Sync Tagging  
**What it is:** Embedding comprehensive sync licensing metadata directly inside the audio file header: Master Owner, Publishing Owner, Contact Email, BPM, Key, Mood, Genre, Instrument List, and "100% Pre-Cleared One-Stop". Embed complete ID3v2 tags and Broadcast WAV (BWF) chunks with contact phone, email, and 100% pre-cleared rights verification.    
**Effect on the audience:** Enables music supervisors to license and clear the track in under 5 minutes without legal red tape.  
**Used for and where it works best:** Submitting music to TV/film supervisors, sync libraries, and advertising agency databases.  
**Best in:** formats: Commercial Sync Pitch Submission, Trailer House Catalog, Music Supervisor Pitch Deck | genres: All sync genres and commercial music    
**Avoid when:** Pitching tracks with uncleared samples or disputed co-writer splits.  
**Example:** `[Metadata: Tagged BWF/MP3: Title, Artist, 124 BPM, Key: A Minor, Moods: Heroic/Determined, Instruments: Taiko/Brass/Synth, 100% Pre-Cleared One-Stop Sync Licensee Contact]`  
**Yields to:** `lyric.music_clearance_constraint` — Uncleared sample: it is a two-licence problem.  
`sync.one_stop_licensing_metadata_tagging`

---

### Epic Hybrid Crescendo Sync Finale

**Also called:** The Climax Wall, Final Sync Slammer  
**What it is:** The ultimate 15-to-30-second climax of a commercial or trailer cue where every layer (choir, brass, synth braams, live drums, foley impacts) plays at maximum intensity before abruptly cutting to a solitary button stinger. Layer three octaves of thematic melody (soprano choir + violins 8va, cellos + horns unison, sub bass below) before cutting to a dry stinger.    
**Effect on the audience:** Leaves the audience breathless, heart pounding, with the brand or movie title etched into their memory.  
**Used for and where it works best:** Final 30 seconds of movie trailers, high-stakes seasonal commercial finales, and epic gaming campaign climaxes.  
**Best in:** formats: Blockbuster Theatrical Trailer Climax, Video Game Boss Battle, Olympic Sports Campaign | genres: Hybrid Epic Orchestral, Cinematic Choir, Trailer Brass    
**Avoid when:** Quiet contemplative end credits or gentle acoustic sign-offs.  
**Example:** `[Finale: Colossal epic hybrid orchestral crescendo, full choir, thundering taiko percussion, piercing brass fanfare, sweeping strings peaking at maximum power, sudden stop into reverberant stinger]`  
**Source:** assumption — the package's working figure, not a published standard; set the climax length against the cut and the rendered audio.  
**Yields to:** `harmony.wordless_vocalise_anthem` — Quiet contemplative end credits.  
`sync.epic_hybrid_crescendo_sync_finale`
