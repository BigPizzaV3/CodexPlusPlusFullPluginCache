# Music Video and Performance

31 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### What Is On Screen, And What Makes It Change

**Also called:** the music video selector, the mv fork, who is in frame and what moves  
**What it is:** The card at the head of the `mv.` shelf. It describes no shot. It asks the three questions the shelf's own pair graph asks over and over — **what is on screen at all, where the change on the beat comes from, and which part of the song it is for** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the shelf's `Yields to:` conditions, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the shot which does reach the screen was chosen against the performer, the room and the structure of the song, rather than picked because the drop needed something and something was to hand.  
**Used for and where it works best:** Answer the three questions **in order and out loud, one sentence each, before you open the shelf**. Answer one is a fact about the artist and the deal and eliminates most of the file. Answer two is the one this shelf actually turns on, and it is a question about your **production capability**, not your taste — nearly every condition on this shelf is a sentence beginning *you do not have*. Answer three stops you spending a peak device twice. Where the honest answer to question two is *all three at once*, you are not designing a shot, you are designing a set-up, and it will have to be lit, shot and cut by three people who each think they own the beat.  
**Best in:** formats: Music Video, Lyric Video, Concert / Live Event, Dance Film, Vertical Short-Form (Reels, Shorts, TikTok), Fashion Film | genres: all  
**Avoid when:** **The piece is a children's song.** The cut floor for children's content outranks every beat multiple on this shelf, `mv.cut_on_beat` says so in its own pair field and hands the decision to `kids.no_fast_cuts`, and a map organised around *what changes on the beat* will keep offering you devices the floor has already refused. Also **do not read axis two as permission.** Three of its four regions can produce a repeated bright/dark run — the light, the edit, and a moving camera under passing sources — and the cards that can produce one do not decide how fast it may go or when it must stop. **Five cards on this shelf hand that question outward to `safety.photosensitive_flash`, which owns it. This selector states no rate, no threshold and no safe value, and neither may you infer one from the fact that a card appears in the map.** A card being on a shelf is not a clearance.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — What is on screen at all?**
Asked first because it is the shelf's own opening question and the only one that survives every budget. The conditions state it as a fact about the artist and the deal, not a feeling: *"No performer, or the face must not be shown"* (`mv.performance_shot`), *"Performance-free video, artist deliberately anonymous"* (`mv.concept_shot`), *"The face must not be readable"* (`mv.lipsync_framing`), *"The song is about a specific person; hiding them defeats it"* (`mv.hidden_face`), *"The story needs spoken dialogue the song blocks"* (`mv.narrative_shot`), *"Serious song; literalism kills the poetry"* (`mv.lyric_visual_pun`), *"Extras will not engage; give them one synchronised action"* (`mv.handheld_party`), *"Singers unconvincing; use movement, not mouths"* (`mv.crowd_sing_back`).

**Axis 2 — Where does the change on the beat come from: the light, the lens, or the edit?**
The largest and most repeated condition cluster on the shelf, and the one that makes it unlike every other shelf in this batch. **Almost every `mv.` condition is a statement about what the production can supply**: *"No programmable rig; take colour from visible sources"* (`mv.stage_light_cues`), *"Room cannot be darkened; colour the performer with light"* (`mv.projection`), *"Sources overpower the face; control colour off-camera"* (`mv.practical_lights`), *"No practicals or backlight; fire light on the moment"* (`mv.confetti_smoke`), *"The void turns cold; build a place from visible sources"* (`mv.white_void_band`), *"Camera cannot be locked for separate passes"* (`mv.multi_clone`), *"No high-frame-rate source; mark the drop in the edit"* (`mv.speed_ramp_drop`), *"No rig height or no designed formation"* (`mv.top_down_formation`), *"No tow rig; take the passing light on foot"* (`mv.car_performance`), *"Locked setup needs a real event, not a pulse"* (`mv.zoom_pulse_beat`), *"Performer cannot sing the line backwards"* (`mv.reverse_walk`), *"No city behind; make placelessness deliberate"* (`mv.rooftop_performance`). Read the list again and notice what is absent: hardly any of these is an argument about what the song deserves. **This shelf's fork is what you can afford and what the room will do.**

**Axis 3 — Which part of the song, and can it be spent twice?**
Seven conditions are about structure rather than look: *"A third chorus needs a new axis, not a third palette"* (`mv.colour_flip_chorus`), *"Nothing to fill the chorus wide"* (`mv.verse_tight_chorus_wide`), *"The song is full of shifts the single take cannot serve"* (`mv.one_take`), *"No second world available; vary the bridge in the edit"* (`mv.bridge_other_world`), *"Short-form; any intro at all is a straight loss"* (`mv.cold_open_intro`), *"Vertical cut; loop instead of a tail"* (`mv.outro_tag`), *"Fast song; ramp instead of a held slow shot"* (`mv.slowmo_hair_fabric`). Asked last because it does not change what you can build — it decides how many times you are allowed to use what you built, and the peak group is a group of cards whose own `Avoid when:` lines say *once*.

---

**The map**

**Axis 1 — what is on screen**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The performer, performing** (seventeen) | `mv.performance_shot` · `mv.singer_walk` · `mv.one_take` · `mv.slowmo_hair_fabric` · `mv.rain_performance` · `mv.car_performance` · `mv.rooftop_performance` · `mv.white_void_band` · `mv.lipsync_framing` · `mv.hidden_face` · `mv.multi_clone` · `mv.reverse_walk` · `mv.projection` · `mv.look_change_cut` · `mv.verse_tight_chorus_wide` · `mv.playback_speed_trick` · `mv.instrument_closeup` |
| **Other bodies — a crowd, dancers, a room full of people** (six) | `mv.dance_wide_detail` · `mv.handheld_party` · `mv.crowd_sing_back` · `mv.crowd_energy_wide` · `mv.top_down_formation` · `mv.camera_dancer` |
| **A story running beside the song** (five) | `mv.narrative_shot` · `mv.perf_narrative_match` · `mv.cold_open_intro` · `mv.outro_tag` · `mv.bridge_other_world` |
| **Neither — the frame is an idea, a surface or the words themselves** (fifteen) | `mv.concept_shot` · `mv.lyric_video_bg` · `mv.lyrics_on_screen` · `mv.lyric_visual_pun` · `mv.mirror_kaleidoscope` · `mv.stage_light_cues` · `mv.practical_lights` · `mv.confetti_smoke` · `mv.colour_flip_chorus` · `mv.strobe_drop` · `mv.flash_frames` · `mv.cut_on_beat` · `mv.speed_ramp_drop` · `mv.whip_pan_beat` · `mv.zoom_pulse_beat` |

**Axis 2 — where the change comes from**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The light in the room** (eight) | `mv.stage_light_cues` · `mv.practical_lights` · `mv.projection` · `mv.strobe_drop` · `mv.white_void_band` · `mv.confetti_smoke` · `mv.rain_performance` · `mv.rooftop_performance` |
| **The lens, and what is put in front of it** (nineteen) | `mv.performance_shot` · `mv.narrative_shot` · `mv.concept_shot` · `mv.singer_walk` · `mv.car_performance` · `mv.one_take` · `mv.dance_wide_detail` · `mv.slowmo_hair_fabric` · `mv.whip_pan_beat` · `mv.zoom_pulse_beat` · `mv.handheld_party` · `mv.crowd_sing_back` · `mv.crowd_energy_wide` · `mv.verse_tight_chorus_wide` · `mv.camera_dancer` · `mv.top_down_formation` · `mv.lipsync_framing` · `mv.hidden_face` · `mv.instrument_closeup` |
| **The edit** (sixteen) | `mv.cut_on_beat` · `mv.flash_frames` · `mv.colour_flip_chorus` · `mv.look_change_cut` · `mv.mirror_kaleidoscope` · `mv.multi_clone` · `mv.playback_speed_trick` · `mv.reverse_walk` · `mv.perf_narrative_match` · `mv.speed_ramp_drop` · `mv.cold_open_intro` · `mv.outro_tag` · `mv.bridge_other_world` · `mv.lyrics_on_screen` · `mv.lyric_video_bg` · `mv.lyric_visual_pun` |

**Axis 3 — which part of the song**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The whole song — it governs every shot** (seventeen) | `mv.performance_shot` · `mv.narrative_shot` · `mv.concept_shot` · `mv.cut_on_beat` · `mv.lipsync_framing` · `mv.hidden_face` · `mv.stage_light_cues` · `mv.practical_lights` · `mv.lyrics_on_screen` · `mv.lyric_video_bg` · `mv.one_take` · `mv.verse_tight_chorus_wide` · `mv.perf_narrative_match` · `mv.colour_flip_chorus` · `mv.white_void_band` · `mv.mirror_kaleidoscope` · `mv.projection` |
| **A verse or a held stretch — it can run and keep running** (sixteen) | `mv.singer_walk` · `mv.car_performance` · `mv.slowmo_hair_fabric` · `mv.zoom_pulse_beat` · `mv.instrument_closeup` · `mv.lyric_visual_pun` · `mv.reverse_walk` · `mv.playback_speed_trick` · `mv.multi_clone` · `mv.look_change_cut` · `mv.rain_performance` · `mv.rooftop_performance` · `mv.dance_wide_detail` · `mv.camera_dancer` · `mv.top_down_formation` · `mv.handheld_party` |
| **The chorus or the drop — spend it once** (seven) | `mv.speed_ramp_drop` · `mv.strobe_drop` · `mv.flash_frames` · `mv.confetti_smoke` · `mv.crowd_energy_wide` · `mv.crowd_sing_back` · `mv.whip_pan_beat` |
| **The ends and the bridge — outside the body of the song** (three) | `mv.cold_open_intro` · `mv.outro_tag` · `mv.bridge_other_world` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally three to six cards wide.*

**A note the map carries and does not resolve.** Axis two's first and third values both contain cards that can produce a repeated bright/dark run, and the shelf has already been repaired once on exactly this. Five cards now hand the rate and the stopping point outward to the card that owns them: `mv.strobe_drop` and `mv.flash_frames` do it in their pair fields, and `mv.projection`, `mv.car_performance` and `mv.white_void_band` do it in their `Avoid when:` lines — the last two describing the effect rather than naming it, one as passing lamp posts across a face and one as fast cutting on a full-white frame. **Read the effect, not the vocabulary.** If a set-up you are building produces a repeated alternation between bright and dark, the question belongs to `safety.photosensitive_flash` whatever the card you got it from calls the device. **This map supplies no rate and no limit, and being on it is not a clearance.**

---

**The default, and the one against it**

**The default is `mv.stage_light_cues` — programmed light changing with the structure of the song — and it is measured, not asserted.** Three cards send a reader here and they send them for three unrelated reasons: `mv.confetti_smoke` (*"No practicals or backlight; fire light on the moment"*), `mv.projection` (*"Room cannot be darkened; colour the performer with light"*) and `mv.practical_lights` (*"Sources overpower the face; control colour off-camera"*). No sources at all, a room that will not go dark, and sources that are too strong — three different ways for a location to fail, one destination. **The shelf, asked where to go when the place will not give you the picture, goes to the light.** That is worth saying out loud, because it means this shelf's real fallback is not a shot: `mv.performance_shot`, which every reader assumes is the default, is the target of nothing at all.

**The card that looks like the default is not one.** `mv.hidden_face` also takes three inbound edges, and **all three are the same condition**: `mv.performance_shot` (*"No performer, or the face must not be shown"*), `mv.concept_shot` (*"Performance-free video, artist deliberately anonymous"*) and `mv.lipsync_framing` (*"The face must not be readable"*) are one sentence in three wordings. Three edges, one condition. It is an anonymity escape hatch — a door out of the shelf when the artist will not appear — and a builder counting edges rather than conditions would have made it the default and told every reader to hide the singer. `mv.crowd_energy_wide` collapses less badly but still collapses: its three conditions are all *the crowd cannot do the specific thing you wanted*.

**The one against it is `mv.zoom_pulse_beat`.** Nothing routes to it; it is named by no `Yields to:` on the shelf; and it is the only card here that **puts the beat inside a continuous take instead of at a cut.** Every other card that answers the music answers it by changing something — the shot, the grade, the light, the speed. This one leaves everything where it is and lets the frame breathe by a few per cent, which is both the cheapest device on the shelf and the only one available at all when the cut rate is governed from somewhere else: on children's content the floor `kids.no_fast_cuts` carries outranks every beat multiple, and `mv.cut_on_beat` hands the decision straight to it. **On a piece where you are not allowed to cut on the beat, this is how you are on the beat.** Its cost is stated and exact — keep the pulse small, and a large one makes the image feel rubbery. **Its near cousin against the grain is `mv.reverse_walk`**, likewise never yielded to, and the only card on the shelf where the performer has to execute something the camera will afterwards undo.

---

**The unasked**

**Twenty of the forty-three reachable cards are the target of no `Yields to:` field anywhere on this shelf** — very nearly half. They can be chosen but nothing ever sends you to them. By id:

`mv.bridge_other_world` · `mv.colour_flip_chorus` · `mv.confetti_smoke` · `mv.instrument_closeup` · `mv.lyric_video_bg` · `mv.lyric_visual_pun` · `mv.lyrics_on_screen` · `mv.multi_clone` · `mv.narrative_shot` · `mv.one_take` · `mv.outro_tag` · `mv.performance_shot` · `mv.projection` · `mv.rain_performance` · `mv.reverse_walk` · `mv.rooftop_performance` · `mv.strobe_drop` · `mv.top_down_formation` · `mv.verse_tight_chorus_wide` · `mv.zoom_pulse_beat`

**And the shape of that list is the finding, not its length. All three of the shelf's own opening cards are on it.** `mv.performance_shot`, `mv.narrative_shot` and `mv.concept_shot` are the triad the entire shelf is organised around — they are the first three cards in the file and they are the whole of axis one's substance — and **not one of them is ever the destination of a yield.** They point outward and nothing points inward. The reason is structural and it is the same reason axis one had to be asked first: a reader writing a `Yields to:` field is holding two shots and comparing them, and *which kind of video is this* is not a comparison between two shots. It is the decision that was made before any shot existed. **The pair graph cannot express the shelf's own first question**, which is exactly why a selector is needed here and why a map built only by following edges would have started in the middle.

The second thing the list shows: **every card whose subject is the song's architecture rather than a frame is unasked** — `mv.verse_tight_chorus_wide`, `mv.colour_flip_chorus`, `mv.outro_tag`, `mv.bridge_other_world`, `mv.one_take`. A reader comparing two cards is holding one moment of the song; a decision about the shape of the whole arc has no second moment to be compared against, so nothing ever routes to it.

The third, and it is the one to act on: **both cards that hand the photosensitivity question outward are in the thin part of the graph.** `mv.strobe_drop` is on this list and is reached by nothing; `mv.flash_frames` is reached exactly once. **The two cards that carry the handover are among the hardest on the shelf to arrive at.** A reader who gets to either of them did so by browsing the file, not by being sent, and the three cards that produce the same effect while calling it something else — a location, a void, a projection — were only repaired because somebody went looking for the effect rather than the word. The new card this shelf wants is not a device at all: it is the one that asks, before any of axis two is answered, *does this set-up alternate between bright and dark, whatever we are calling it* — and hands the answer to the card that owns it. **This selector will not supply that rule and does not contain one.**

`mv.choose_what_changes`

---

### Performance Shot

**Also called:** sync shot, playback performance  
**What it is:** The singer or the band perform the song to camera over playback, with the lips locked to the original recording.  
**Effect on the audience:** It ties the voice to a face, and without it the viewer never learns whose song this is. It is the spine that carries the whole video.  
**Used for and where it works best:** Shoot it at several sizes for the same section so you can cut between them on the beat: wider in the verse, closer in the chorus. Push the energy above natural level because the camera eats performance energy. Play the track loud on location so the sync stays honest.  
**Best in:** formats: Music Video, Concert / Live Event, Dance Film, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Kids Content | genres: Musical, Romance, Drama, Comedy, Family, Action  
**Avoid when:** A low energy performance makes the video feel dead no matter how good the image is. If the lips are out of sync the viewer notices instantly and stops believing it.  
**Prompt:** `singer performing to camera over playback, medium and close sizes of the same verse, lip sync locked, energetic delivery`  
**Yields to:** `mv.hidden_face` — No performer, or the face must not be shown.  
`mv.performance_shot`

### Narrative Shot

**Also called:** story shot, drama insert  
**What it is:** Shots from a story running parallel to the song: characters, events and actors, with no singing and no lip sync.  
**Effect on the audience:** They give the song a specific meaning and give the viewer a fate to follow, so they stay to the end even if the song is not for them.  
**Used for and where it works best:** Keep the story extremely simple: a relationship, a parting, a journey, a wait. Distribute it so each verse advances one step and each chorus returns to performance. In Arabic and Turkish music video the story often occupies half the running time.  
**Best in:** formats: Music Video, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Lyric Video | genres: Romance, Drama, Melodrama, Tragedy, Crime / Procedural, Coming of Age, Musical  
**Avoid when:** A complex story in four minutes is not understood and it damages the song. A story that needs dialogue usually cannot be told here, because the song occupies the audio; the exception is a short spoken intro before the track begins.  
**Prompt:** `silent narrative scene of the couple parting at the station, no lip sync, cut to the rhythm of the verse`  
**Yields to:** `mv.cold_open_intro` — The story needs spoken dialogue the song blocks.  
`mv.narrative_shot`

### Concept Shot

**Also called:** abstract shot, visual idea  
**What it is:** A symbolic image serving neither story nor performance: a geometric form, a body in water, cloth flying, colour spreading, a mass of fire.  
**Effect on the audience:** It gives the video a visual identity and a mood, and makes the song feel larger than its literal subject.  
**Used for and where it works best:** Use it in the bridge, in the instrumental intro and between chorus and verse. Keep one idea returning in variations rather than scattered images. It suits AI generation very well because it needs no character consistency.  
**Best in:** formats: Music Video, Lyric Video, Experimental / Art Film, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, AI-Generated Clip | genres: Musical, Surreal / Absurdist, Psychological / Arthouse, Romance, Drama, Fantasy / Epic  
**Avoid when:** Random symbols with no thread make the video feel empty and pretentious. Do not build a whole video on concept with no performance unless the artist is deliberately kept anonymous.  
**Prompt:** `red ink spreading through clear water in slow motion against a black background, one continuous abstract movement`  
**Yields to:** `mv.hidden_face` — Performance-free video, artist deliberately anonymous.  
`mv.concept_shot`

### Cut On The Beat

**Also called:** rhythmic cutting, on the one  
**What it is:** Every cut in the video lands on a beat of the track, and the rule holds even for the calm shots.  
**Effect on the audience:** It fuses picture and sound into one body. When a cut sits off the beat the viewer senses something wrong even if they cannot name it.  
**Used for and where it works best:** This is the first law of music video. Mark the beats before you lay a shot, and keep shot lengths in multiples: two beats, four, eight. On children's content, the 1.5-second floor (`kids.no_fast_cuts`) strictly outranks the beat multiple: at 120 BPM, cut on four beats (2.0s) or eight, never two beats (1.0s). Break the rule once only, at a deliberate moment, so the break is felt.  
**Best in:** formats: Music Video, Dance Film, Concert / Live Event, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Commercial / TVC, Trailer / Teaser | genres: Musical, Romance, Action, Comedy, Sports Drama, Slice of Life  
**Avoid when:** Cutting on every single beat with no exception makes the video mechanical and tiring. Do not cut in the middle of a sung word; it severs the musical phrase. And note what the beat sets when the cuts alternate dark and bright frames: a repetition rate taken from the track's tempo, which this card does not judge — that run and the point where it has to stop are `safety.photosensitive_flash`.  
**Prompt:** `every cut lands on the beat, shot lengths in multiples of two beats, one deliberate off beat cut at the bridge`  
**Source:** assumption — the package's working figure, not a published standard; the 1.0s and 2.0s values are arithmetic at 120 BPM (beats × 60 ÷ BPM); set the shot lengths against the measured beat grid of the track.  
**Yields to:** `kids.no_fast_cuts` — Children's content; the floor outranks the beat multiple; and `safety.photosensitive_flash` — a beat-cut run that alternates dark and bright frames.  
`mv.cut_on_beat`

### The Chorus Change

**Also called:** chorus shift, hook variation  
**What it is:** With every chorus something large changes and is seen at once: the location, the wardrobe, the colour, or the number of people in frame.  
**Effect on the audience:** It tells the viewer without thinking that the chorus has returned, and creates escalation instead of repetition.  
**Used for and where it works best:** This is the structural secret of the form: one person in the first chorus, two in the second, a group in the third. Or white light, then red, then night. Plan the change before the shoot because it dictates wardrobe and locations.  
**Best in:** formats: Music Video, Lyric Video, Dance Film, Concert / Live Event, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content | genres: Musical, Romance, Family, Comedy, Drama, Slice of Life  
**Avoid when:** A chorus that looks identical three times makes the video feel underwritten. Do not change everything at once either; the song's own identity gets lost — and the other chorus cards count toward that everything: the grade flip (`mv.colour_flip_chorus`), the size opening (`mv.verse_tight_chorus_wide`) and the crowd (`mv.crowd_energy_wide`) each spend a change on the same beat, so choose which of them this chorus carries rather than stacking all of them.  
**Prompt:** `same chorus staged three times, first alone in white light, then two people in red, then a full group at night`  
`mv.chorus_change`

### The Singer Walk

**Also called:** walking performance, tracking sync  
**What it is:** The singer walks toward the camera or alongside it while performing, with the camera retreating or travelling beside them at the same speed.  
**Effect on the audience:** It delivers energy and constant forward motion, and keeps a long take alive because the background keeps changing.  
**Used for and where it works best:** Ideal for carrying a whole verse in one take, and ideal in vertical because the body and the motion fill the frame. Choose a street or a corridor with lights passing across the face. Keep the speed constant and let the singer arrive at a marked point by the end of the verse.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Dance Film, Concert / Live Event, Fashion Film | genres: Musical, Romance, Drama, Coming of Age, Slice of Life, Action  
**Avoid when:** An aimless walk through an empty space makes the take feel long for nothing. Camera wobble while retreating ruins the shot entirely.  
**Prompt:** `singer walking straight toward a retreating camera down a lit corridor, constant speed, one continuous verse long take`  
**Yields to:** `mv.car_performance` — No street or corridor supplying passing detail.  
`mv.singer_walk`

### One-Take Music Video

**Also called:** single shot video, oner  
**What it is:** The whole song is shot in one continuous take with no cuts, and all the change happens inside the frame through movement, set and performers.  
**Effect on the audience:** It delivers a real sense of achievement: the viewer knows this actually happened, and the tension that any mistake restarts everything is part of the pleasure.  
**Used for and where it works best:** It needs more rehearsal than shooting: every camera move and every performer entrance is timed to the second. Design the route so it passes through different spaces and creates a sense of progress. Best for a song with steady rather than shifting energy.  
**Best in:** formats: Music Video, Dance Film, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event | genres: Musical, Romance, Comedy, Drama, Slice of Life, Action  
**Avoid when:** One take in one unchanging space is boredom, not achievement. If the song is full of shifts the single take stops you from serving them.  
**Prompt:** `one continuous take following the performer through four connected spaces for the length of the song, no cuts`  
**Example:** OK Go, Here It Goes Again, performed on treadmills in a single continuous take.  
**Yields to:** `mv.cut_on_beat` — The song is full of shifts the single take cannot serve.  
`mv.one_take`

### Dance Wide Plus Detail

**Also called:** choreography coverage, full body plus insert  
**What it is:** The choreography is covered in a wide that shows the full body, cut with detail shots of the feet, the hands or the face.  
**Effect on the audience:** The wide preserves the choreography and the detail carries the feeling; together they make the dance both legible and exciting.  
**Used for and where it works best:** Cut to the detail on musical endings and return to the wide at the top of every eight. Never cut in the middle of a complex move; keep the whole body in frame for it. In vertical shoot the wide along the height and let the dancer fill it.  
**Best in:** formats: Dance Film, Music Video, Concert / Live Event, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content | genres: Musical, Family, Romance, Comedy, Sports Drama  
**Avoid when:** Chopping dance into close-ups destroys the choreography. A single static wide for the whole song makes the performance look recorded rather than filmed.  
**Prompt:** `wide full body dance shot cut with inserts of the feet and hands, returning to the wide at the top of each eight count`  
**Yields to:** `mv.camera_dancer` — A static wide reads as recorded, not filmed.  
`mv.dance_wide_detail`

### Slow-Motion Hair And Fabric

**Also called:** beauty slow motion, fabric flow  
**What it is:** A slow motion shot focused on hair, a dress or a robe turning and spreading through the air.  
**Effect on the audience:** It delivers beauty and flow, turning an ordinary movement into a mood. It works with calm and emotional songs.  
**Used for and where it works best:** Shoot at a high frame rate with a fan and a backlight so the edges glow. Ideal in a slow chorus and in the bridge. In heritage music video it works beautifully with long fabrics and traditional dress.  
**Best in:** formats: Music Video, Fashion Film, Vertical Short-Form (Reels, Shorts, TikTok), Dance Film, Wedding / Event Film, Lyric Video | genres: Romance, Musical, Drama, Heritage (civilisation-focused), Fantasy / Epic, Melodrama  
**Avoid when:** Slow motion in a fast song breaks the rhythm and the shot feels out of place. Too many slow shots and the video turns into a perfume commercial.  
**Prompt:** `high frame rate slow motion of hair and fabric spreading as the performer turns, strong backlight, fan from the side`  
**Yields to:** `mv.speed_ramp_drop` — Fast song; ramp instead of a held slow shot.  
`mv.slowmo_hair_fabric`

### Speed Ramp On The Drop

**Also called:** time ramp, drop ramp  
**What it is:** The shot runs slow through the build then snaps to full speed exactly at the drop or the entry of the chorus.  
**Effect on the audience:** It makes the musical turn visible in the picture, and the viewer feels the release in the body rather than only in the ear.  
**Used for and where it works best:** Choose a shot with a large movement: a jump, a turn, a run, arms opening. Start the slow section two seconds before the drop. It is even stronger in vertical because energy compensates for the lack of space.  
**Best in:** formats: Music Video, Dance Film, Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, Trailer / Teaser, Commercial / TVC | genres: Musical, Action, Sports Drama, Romance, Adventure  
**Avoid when:** A ramp on every shot robs the drop of its distinction. If the take was not shot at a high frame rate the slow section stutters and exposes the trick.  
**Prompt:** `shot ramps from quarter speed to full speed hitting normal playback exactly on the drop, high frame rate source`  
**Yields to:** `mv.flash_frames` — No high-frame-rate source; mark the drop in the edit.  
`mv.speed_ramp_drop`

### Whip Pan On The Beat

**Also called:** swish pan cut, beat whip  
**What it is:** The camera whips at very high speed at the end of the shot, and the cut lands on the blurred frame exactly on the beat.  
**Effect on the audience:** It ties two different shots into one movement and adds a rhythmic push that makes the transition part of the song.  
**Used for and where it works best:** Match the whip direction at the end of one shot to the start of the next. Ideal for moving between performance and narrative or between chorus locations. It differs from the vertical whip transition in that it is locked to a musical beat rather than a change of scene.  
**Best in:** formats: Music Video, Dance Film, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Commercial / TVC, Trailer / Teaser | genres: Musical, Action, Comedy, Romance, Sports Drama  
**Avoid when:** A whip in a calm song wrecks the mood. If the directions do not match, the transition reads as a broken cut rather than a movement.  
**Prompt:** `fast whip pan right at the end of the shot cutting on the blur into a matching whip that settles on the new location`  
**Yields to:** `mv.perf_narrative_match` — Calm song; join the worlds by match, not whip.  
`mv.whip_pan_beat`

### Zoom Pulse On The Beat

**Also called:** beat pulse, punch zoom rhythm  
**What it is:** A very small zoom pulses inside the shot on each beat only, by a small percentage, with no cut.  
**Effect on the audience:** It makes a static shot breathe with the music and delivers a pulse without breaking the continuity of the take.  
**Used for and where it works best:** Ideal for long performance takes, for lyric video and for content built from stills. Keep the pulse to three to five percent only. It works best in a calm verse where you do not want many cuts.  
**Best in:** formats: Music Video, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Concert / Live Event, AI-Generated Clip | genres: Musical, Romance, Slice of Life, Family, Drama  
**Avoid when:** A large pulse makes the image feel rubbery and irritating. Do not run it through the whole song; the eye tires of it.  
**Prompt:** `subtle four percent zoom pulse on every beat inside a locked performance shot, no cuts`  
**Yields to:** `mv.look_change_cut` — Locked setup needs a real event, not a pulse.  
`mv.zoom_pulse_beat`

### Colour Flip On The Chorus

**Also called:** grade change, palette switch  
**What it is:** The entire grade changes at the instant the chorus enters: cool to warm, natural to monochrome, muted to saturated.  
**Effect on the audience:** It announces the musical turn to the eye before the ear and gives the chorus a visual identity that sticks.  
**Used for and where it works best:** Decide two palettes: the verse colour and the chorus colour. Switch exactly on the first beat of the chorus with no gradual blend. In heritage music video use earth tones for the verse and gold for the chorus.  
**Best in:** formats: Music Video, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Dance Film, Commercial / TVC, Concert / Live Event | genres: Musical, Romance, Drama, Heritage (civilisation-focused), Fantasy / Epic, Comedy  
**Avoid when:** A gradual colour change is not felt; the power is in the abrupt flip. More than two palettes makes the video feel ungraded.  
**Prompt:** `the grade flips from cool desaturated to warm saturated exactly on the first beat of the chorus, no transition`  
**Yields to:** `mv.chorus_change` — A third chorus needs a new axis, not a third palette.  
`mv.colour_flip_chorus`

### Multi-Clone Performer

**Also called:** cloned performer, multiplied singer  
**What it is:** The performer appears several times in the same frame on a locked camera, each copy doing something different or singing the same line.  
**Effect on the audience:** It presents the person as multiple or divided, a strong visual idea for songs about internal conflict.  
**Used for and where it works best:** Lock the camera completely and shoot each copy as a separate pass under the same light. Let the copies interact: one looking at another. It suits the chorus, where the vocal is layered but the performer is one.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Experimental / Art Film, Commercial / TVC, AI-Generated Clip | genres: Musical, Psychological / Arthouse, Drama, Surreal / Absurdist, Romance, Fantasy / Epic  
**Avoid when:** If the light changes between passes the mask shows. Do not add too many copies; a vertical frame holds three at most.  
**Prompt:** `locked camera, three copies of the same performer in one frame singing the same line, identical lighting in every pass`  
**Yields to:** `mv.mirror_kaleidoscope` — Camera cannot be locked for separate passes.  
`mv.multi_clone`

### Reverse Walk

**Also called:** reversed motion, backwards performance  
**What it is:** The shot is filmed normally and played backwards, or the performance is staged in reverse so it plays forward with an uncanny quality.  
**Effect on the audience:** It suggests time running backwards, and the movement becomes unnaturally graceful in a way that holds the eye.  
**Used for and where it works best:** Ideal for songs about regret, return and memory: objects return to their places and the person walks backwards. Have the performer sing the line phonetically backwards so the sync works on the reversed playback. Use it in the bridge or one verse.  
**Best in:** formats: Music Video, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Experimental / Art Film, Short Film | genres: Musical, Romance, Drama, Psychological / Arthouse, Surreal / Absurdist, Tragedy  
**Avoid when:** Using it through the whole video is disorienting and makes the song hard to follow. If the reversed lip sync is wrong it is exposed instantly.  
**Prompt:** `reversed playback of the performer walking backwards while spilled objects return to the table, one continuous take`  
**Yields to:** `mv.playback_speed_trick` — Performer cannot sing the line backwards.  
`mv.reverse_walk`

### Rain / Water Performance

**Also called:** wet performance, rain machine shot  
**What it is:** The performer sings under artificial rain or in water, with the droplets picked out by a backlight.  
**Effect on the audience:** It provides a visible emotional peak: water on the face reads as tears, as collapse or as cleansing.  
**Used for and where it works best:** Reserve it for the final chorus or the collapse moment in a sad song. Put a strong backlight behind the rain or the drops will not read on camera. Let the clothes and hair get progressively wetter so the continuity holds.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Fashion Film, Short Film, Concert / Live Event | genres: Romance, Melodrama, Drama, Tragedy, Musical, Psychological / Arthouse  
**Avoid when:** Rain without a backlight does not read and the whole effort is wasted. Do not place it at the top of the video; you leave yourself nowhere to escalate.  
**Prompt:** `performer singing under heavy artificial rain with a hard backlight making every droplet visible, slow push in`  
**Yields to:** `mv.crowd_sing_back` — No rig or backlight to make water read at the peak.  
`mv.rain_performance`

### Car Performance

**Also called:** driving shot, in car sync  
**What it is:** The performer sings inside a moving car, with the camera rigged to the bonnet or placed in the opposite seat.  
**Effect on the audience:** It delivers continuous movement and a sense of travel or escape, and the lights passing across the face give a free visual rhythm.  
**Used for and where it works best:** The backbone of road and night videos: shoot at night on a street with lamp posts so the light pulses across the face. Cover it from the passenger seat and from the bonnet. In vertical it is an excellent solution because a car interior fills the frame.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Lyric Video, Short Film, Travel / Real Estate / Hospitality | genres: Romance, Road Movie, Drama, Musical, Crime / Procedural, Coming of Age  
**Avoid when:** A stationary car with motionless trees outside exposes the fake. Real driving while performing is dangerous; use a tow rig or a low loader. And note what the lamp posts actually produce: a repeated bright/dark run across the face, whose rate is lamp spacing against road speed. This card chooses the location, not that rate or the point where it has to stop - those are `safety.photosensitive_flash`.  
**Prompt:** `night interior car shot from the passenger seat, street lamps sweeping across the singer's face`  
*(the rate is deliberately not specified here. This field used to say "at a steady rhythm" — the repeated bright/dark run the Avoid when above hands to `safety.photosensitive_flash`, still being copied into the generator.)*  
**Yields to:** `mv.singer_walk` — No tow rig; take the passing light on foot; and `safety.photosensitive_flash` — the rate of the lamp run across the face and the point where it has to stop.  
`mv.car_performance`

### Rooftop Performance

**Also called:** rooftop set, skyline performance  
**What it is:** The performance is staged on a rooftop with the city or the sky behind the performer, usually at sunset or at night.  
**Effect on the audience:** It gives height, freedom and openness, and the open background makes the performer look both larger and alone.  
**Used for and where it works best:** Ideal for the final chorus and for songs about ambition or solitude. Shoot at golden hour or at night with the city lights thrown out of focus. In vertical let the performer fill the height with the city reading at the sides.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Fashion Film, Lyric Video | genres: Musical, Romance, Drama, Coming of Age, Slice of Life, Action  
**Avoid when:** A rooftop with an empty background and no city wastes the entire reason for being there. Midday sun there gives hard light that ruins the face.  
**Prompt:** `rooftop performance at golden hour, city skyline out of focus behind, slow orbit around the singer on the chorus`  
**Yields to:** `mv.white_void_band` — No city behind; make placelessness deliberate.  
`mv.rooftop_performance`

### Band In A White Void

**Also called:** infinity cove, limbo set  
**What it is:** The performer or band stand inside a white or black space with no visible edges or corners, floor and wall merging.  
**Effect on the audience:** It removes all context so only the performance, the wardrobe and the colour remain, which makes the look itself the message.  
**Used for and where it works best:** Ideal for introducing a new artist, for fashion-led videos and for dance sections. Light it evenly with no shadow falling on the background, and dress the performer in strong colour so they do not disappear. Hold the full-white field steadily; any sequence that alternates it with materially darker full frames transfers rate and stopping-point authority to `safety.photosensitive_flash`.  
**Best in:** formats: Music Video, Fashion Film, Dance Film, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Title Sequence / Opening Credits, AI-Generated Clip | genres: Musical, Romance, Comedy, Slice of Life, Family  
**Avoid when:** A white void with uneven light exposes the corners and looks cheap. A whole video in the void turns cold and placeless. And the line above recommends fast cutting on a full-white frame, which is a bright/dark alternation at the scale of the whole image however it was arrived at: the cut rate at which that stops being an edit and becomes a dosage is not this card's to judge, and belongs to `safety.photosensitive_flash`.  
**Prompt:** `performer isolated in a seamless white infinity space, even shadowless lighting, bold coloured wardrobe, locked camera`  
**Yields to:** `mv.practical_lights` — The void turns cold; build a place from visible sources.  
`mv.white_void_band`

### Hand-Held Party

**Also called:** party camera, inside the crowd  
**What it is:** A handheld camera moves among people inside a party or a gathering, pushing close to faces, turning with them, stumbling slightly.  
**Effect on the audience:** It makes you present at the party rather than watching it, and the measured chaos delivers authenticity and energy.  
**Used for and where it works best:** Ideal for dance, celebration and wedding songs. Shoot on a wide lens close to people and let them play to the camera. Use the real light sources in the room: neon, candles, a phone flash.  
**Best in:** formats: Music Video, Wedding / Event Film, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Dance Film, Vlog / YouTube Long-Form | genres: Musical, Romance, Comedy, Family, Slice of Life, Coming of Age  
**Avoid when:** Violent aimless shake tires the eye and loses the faces. A party of extras who do not engage comes out cold and exposes the staging.  
**Prompt:** `handheld wide lens moving through a crowded party, close to faces, practical neon and phone light, natural sway`  
**Yields to:** `mv.crowd_energy_wide` — Extras will not engage; give them one synchronised action.  
`mv.handheld_party`

### Crowd Singing Back

**Also called:** sing along shot, audience chorus  
**What it is:** Shots of ordinary people or an audience singing the same words, in different places or in the same room as the performer.  
**Effect on the audience:** It turns the song from a solo into something collective and gives visual proof that people know it and love it.  
**Used for and where it works best:** Save it for the final chorus so it lands as an emotional peak. Shoot faces that differ in age and place so the reach reads. In patriotic and heritage songs this is the moment that ties the song to the people.  
**Best in:** formats: Music Video, Concert / Live Event, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Lyric Video, Documentary Series | genres: Musical, Family, Heritage (civilisation-focused), Romance, Slice of Life, Faith / Biblical Epic, Sports Drama  
**Avoid when:** People singing without conviction produce the opposite effect and make the song look unloved. Do not place it in the first verse; it spends the peak.  
**Prompt:** `cut between different people in different places singing the same chorus line straight to camera, natural light`  
**Yields to:** `mv.crowd_energy_wide` — Singers unconvincing; use movement, not mouths.  
`mv.crowd_sing_back`

### Verse Tight, Chorus Wide

**Also called:** size structure, open on the hook  
**What it is:** Every verse shot is close and tight, and when the chorus enters the sizes open up to wides with bigger movement. On vertical (9:16) mobile screens where wide shots lose facial detail, the chorus opens to Medium-Wide (Cowboy/Knee framing) rather than an extreme wide, satisfying `vertical.fill_frame` while delivering acoustic release.  
**Effect on the audience:** It produces a physical sense of opening at the exact moment the melody opens, so the viewer feels the chorus before they register it.  
**Used for and where it works best:** A structural rule that works on any song: close for the secret and the confession in the verse, wide for the declaration and the release in the chorus (on 9:16, medium-wide). Invert it when the song inverts: a bleak chorus earns a suffocating close-up after an open verse.  
**Best in:** formats: Music Video, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Dance Film, Kids Content | genres: Musical, Romance, Drama, Melodrama, Family, Tragedy  
**Avoid when:** The same size in verse and chorus makes the song look visually flat. Do not open onto an empty wide; the chorus needs something to fill the space.  
**Prompt:** `tight close-ups through the verse opening to medium-wide shots with bigger movement on the first beat of the chorus`  
**Yields to:** `mv.crowd_energy_wide` — Nothing to fill the chorus wide.  
`mv.verse_tight_chorus_wide`

### Playback Speed Trick

**Also called:** double time playback, overcranked sync  
**What it is:** The track is played back at double speed on location and the performer sings along to it, then the take is slowed in the edit, producing correct lip sync in slow motion.  
**Effect on the audience:** It gives a slow, fluid performance while the lips stay locked, a look that ordinary shooting cannot produce.  
**Used for and where it works best:** Ideal for a slow chorus and for emotional songs: hair, fabric and movement all turn fluid. Shoot at a high frame rate with the track at double speed. You can invert it: play at half speed and speed the take up for an uncanny fast movement.  
**Best in:** formats: Music Video, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Fashion Film, Dance Film, Experimental / Art Film | genres: Musical, Romance, Psychological / Arthouse, Surreal / Absurdist, Drama, Fantasy / Epic  
**Avoid when:** It needs rehearsal; a performer who cannot sing at double speed comes out distorted. Do not use it on a line already crowded with fast words.  
**Prompt:** `track played at double speed on set, performance filmed at high frame rate and slowed in post for fluid locked sync`  
**Yields to:** `mv.slowmo_hair_fabric` — Performer cannot sing at double speed; drop the sync.  
`mv.playback_speed_trick`

### Confetti And Smoke Hits

**Also called:** atmospheric hits, practical effects timing  
**What it is:** Physical effects fire on an exact moment: coloured paper, smoke, sparks, feathers, dust, timed to the chorus or the drop.  
**Effect on the audience:** They give a real visual burst inside the frame, and the flying material fills the space and turns the moment into an event.  
**Used for and where it works best:** Shoot at a high frame rate with a backlight so the material reads. Fire the effect a fraction before the beat so the peak of the burst matches. Ideal in the final chorus and in celebration and wedding videos.  
**Best in:** formats: Music Video, Concert / Live Event, Dance Film, Wedding / Event Film, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Kids Content | genres: Musical, Family, Romance, Comedy, Sports Drama, Slice of Life  
**Avoid when:** Effects with no backlight disappear in the image and the effort is wasted. Bad timing breaks the moment and it reads as random.  
**Prompt:** `confetti burst released a fraction before the downbeat, backlit against a dark stage, high frame rate slow motion`  
**Yields to:** `mv.stage_light_cues` — No practicals or backlight; fire light on the moment.  
`mv.confetti_smoke`

### Look-Change Cut

**Also called:** wardrobe cut, outfit switch on the beat  
**What it is:** The identical framing, and on the beat the wardrobe, the hair or the make-up changes on a straight cut.  
**Effect on the audience:** It delivers rhythmic satisfaction and a sense of abundance and production value, and lets one static setup carry a whole section.  
**Used for and where it works best:** Lock the camera, shoot the same performance in every look, then switch on the beats. It differs from the vertical outfit spin in that there is no covering movement: the cut itself is the event. Ideal in up-tempo songs and fashion-led videos.  
**Best in:** formats: Music Video, Fashion Film, Vertical Short-Form (Reels, Shorts, TikTok), Dance Film, Commercial / TVC, Kids Content | genres: Musical, Romance, Comedy, Slice of Life, Family  
**Avoid when:** Changing the body position between looks breaks the trick and it becomes an ordinary cut. More than four looks and the viewer remembers none. On children's content the cut floor (`kids.no_fast_cuts`) outranks the beat interval here exactly as it does for `mv.cut_on_beat`: space the looks to the floor, not to the beat.  
**Prompt:** `locked frame, the performer holds the same pose while the outfit changes on every second beat (on children's content, on the longer beat multiple the kids cut floor allows), identical lighting`  
**Yields to:** `trans.outfit_spin` — Performer cannot hold the pose; cover the change; and `kids.no_fast_cuts` — children's content, where the floor outranks the beat interval.  
`mv.look_change_cut`

### Camera As A Dancer

**Also called:** choreographed camera, operator in the formation  
**What it is:** The camera moves to the choreography itself: turning with the turn, dropping with the drop, travelling between the dancers.  
**Effect on the audience:** It puts the viewer inside the dance rather than in front of it, and the energy rises because the frame itself is dancing.  
**Used for and where it works best:** It needs the camera rehearsed with the dancers as if it were another dancer. Ideal in the dance section and in vertical, where movement compensates for the narrow frame. Use a light gimbal or a small camera so you can move between bodies.  
**Best in:** formats: Dance Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Kids Content, Sports Broadcast / Sports Film | genres: Musical, Action, Family, Romance, Sports Drama  
**Avoid when:** Camera movement that disagrees with the choreography ruins both. If the camera is faster than the dancer the choreography stops reading.  
**Prompt:** `gimbal camera moving through the dance formation, turning with the dancers and dropping on the beat with them`  
**Yields to:** `mv.dance_wide_detail` — Camera outruns the dance; hold the wide.  
`mv.camera_dancer`

### Pre-Song Cold Open

**Also called:** intro scene, spoken intro  
**What it is:** A short scene before the song begins: dialogue, room tone, or a silent shot, and then the music enters.  
**Effect on the audience:** It provides context for the story and makes the music's entry feel like an event, because the silence before it makes it bigger.  
**Used for and where it works best:** Keep it under fifteen seconds because the viewer came for the song. Ideal for a video with a story or one tied to a film. For a vertical cut, drop it by default, or reduce it to three seconds only when that moment is itself the hook and the song enters straight after it.  
**Best in:** formats: Music Video, Short Film, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser | genres: Drama, Romance, Crime / Procedural, Musical, Tragedy, Thriller / Suspense  
**Avoid when:** A long intro loses the viewer before they hear the song. On short-form platforms any intro beyond the reduced stub the line above allows is a straight loss: drop it or cut it to that stub, and otherwise open cold (`vertical.cold_cut`).  
**Prompt:** `ten second silent scene with room tone only, ending on a held look as the first chord of the song enters`  
**Yields to:** `vertical.cold_cut` — Short-form; any intro beyond the reduced stub is a straight loss.  
`mv.cold_open_intro`

### Post-Song Outro Tag

**Also called:** the tag, closing beat  
**What it is:** One or two shots after the song ends: silence, a final movement, a line, or the closing of the story.  
**Effect on the audience:** It provides a complete ending and turns the video from a music clip into a work with a beginning and an end.  
**Used for and where it works best:** Use it to close the story: the letter is read, the door shuts, the person turns. Keep it under ten seconds. In vertical replace it with a loop point rather than an open ending.  
**Best in:** formats: Music Video, Short Film, Lyric Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser | genres: Drama, Romance, Tragedy, Musical, Crime / Procedural, Melodrama  
**Avoid when:** A long tail after the music ends loses the viewer before they see it. If you have nothing to say, end on the last note.  
**Prompt:** `two shots after the final chord in silence, the character reads the letter and closes the door, then cut to black`  
**Yields to:** `vertical.loop_point` — Vertical cut; loop instead of a tail.  
`mv.outro_tag`

### Lyric Video Background

**Also called:** text video bed, lyric backdrop  
**What it is:** A background with one slow continuous movement (grain, light, a landscape, drifting colour) with the synced text on top as the real subject.  
**Effect on the audience:** The text stays readable and the background supplies mood without competing, so the ear and the eye cooperate instead of fighting.  
**Used for and where it works best:** The law of lyric video: one slow movement is enough, with high contrast between the text colour and the background. Ideal for a new release before the real video is shot and for educational children's songs. Keep the typeface and size consistent throughout.  
**Best in:** formats: Lyric Video, Music Video, Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), Explainer, AI-Generated Clip | genres: Musical, Family, Preschool / Early Learning, Romance, Faith / Biblical Epic, Slice of Life  
**Avoid when:** A busy or fast background makes the text unreadable and defeats the purpose. Changing the typeface in every section makes the video look undesigned.  
**Prompt:** `slow drifting grain and light background at low contrast with large legible lyrics synced on top, one continuous movement`  
`mv.lyric_video_bg`

### Top-Down Dance Formation

**Also called:** overhead formation, kaleidoscopic staging  
**What it is:** The camera is directly above the dancers shooting straight down, turning their bodies into geometric shapes that open and close.  
**Effect on the audience:** It visually removes gravity and turns the dance into pattern, so the eye reads the shape rather than the individuals.  
**Used for and where it works best:** Ideal for the final chorus and for group numbers. Design the formation so it opens from a single point or rotates. In vertical build the formation along its length rather than as a circle so it fills the frame.  
**Best in:** formats: Dance Film, Music Video, Concert / Live Event, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Sports Broadcast / Sports Film | genres: Musical, Family, Sports Drama, Romance, Comedy  
**Avoid when:** An overhead with no designed formation is just people on a floor. Too low a height tilts the perspective and ruins the symmetry.  
**Prompt:** `camera directly overhead looking straight down as the dancers open from a single point into a symmetrical pattern`  
**Yields to:** `mv.dance_wide_detail` — No rig height or no designed formation.  
`mv.top_down_formation`
