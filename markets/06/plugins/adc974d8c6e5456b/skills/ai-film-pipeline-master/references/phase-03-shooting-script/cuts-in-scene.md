# Cuts Within a Scene

69 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name What Fires the Cut

**Also called:** the cut selector, why the cut falls here, what supplies the cut point  
**What it is:** The card at the head of the `cut.` shelf. It does not describe an edit. It asks the three questions the shelf's own pair graph asks over and over — **what supplies the cut point, what the join has to do to the viewer, and where it falls against the beat** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the forty-eight `Yields to:` conditions the cards carry, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so the cut that does reach the screen was chosen against the movement, the track and the beat, rather than placed where the last one was placed.  
**Used for and where it works best:** Answer the three questions **in order and out loud, in one sentence each, before you open the shelf**. Question one eliminates most of the file; questions two and three leave a shortlist of three to six. **And before any of that, settle which shelf you are on.** `cut.` decides *why the cut falls here*; `trans.` decides *how you get across*. The line runs at the frame boundary: **if your answer can be written as a frame number, it is a `cut.` card; if the join needs a duration of its own — even a few frames of mix, cover or move — it is a `trans.` card.** Every edge that crosses between the two shelves obeys that line, and nearly all of them run one way, from duration back to frame: a transition that cannot be afforded collapses into a cut, while only one card here ever buys an interval instead. **So when you cannot tell which question you are asking, ask this one first** — the fallback lives on this shelf, not the other one.  
**Best in:** formats: all | genres: all  
**Avoid when:** **You are not choosing where to cut, you are choosing what goes between two shots** — a mix, a cover, a camera move, a layer. That is the neighbouring shelf and this map will send you to a frame when you needed a passage. Also avoid it when the coverage was never shot: this shelf assumes two usable angles exist, and `cut.withheld` says in its own `Avoid when:` that a missing setup is not a style. And **distrust axis one whenever your honest answer is its fifth value** — nearly half the reachable shelf lives there, so on a scene where nothing in the picture, the track, the face or the coverage geometry hands you the frame, this map has only two questions left and is doing rather less than it looks like it is doing.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis one — What supplies the cut point?**
Asked first, because it is the condition the shelf repeats most and the only one that reorganises the whole file. The cards state it as a rivalry between signals, never as a feeling: *"Fast action, where movement leads instead of thought"* (`cut.on_blink`), *"Emotional dialogue, where the face decides, not sound"* (`cut.on_sound`), *"A dialogue scene, where speech leads not music"* (`cut.rhythmic`), *"When the head or eye moves, ride it"* (`cut.eyeline`), *"A slow deliberate turn must finish uncut"* (`cut.on_look`), *"Documentary with two cameras; cover the seam instead"* (`cut.thirty_degree`), *"The mismatched element carries story information"* (`cut.cheat`). Every one of those is a boundary, not a recommendation: it says which signal loses.

**Axis two — What must the join do: vanish, rhyme, carry, or hit?**
The second most repeated condition, and it is always stated as a demand on the viewer rather than a mood: *"When the viewer should notice the place changed"* (`cut.motion_match`), *"Inside a scene, where the match must conceal"* (`cut.graphic_match`), *"When the match is poetry between acts"* (`cut.form`), *"When the join must register, not slip past"* (`cut.texture_match`), *"When the join must be inaudible, one real sound"* (`cut.sound_match`), *"When the cut itself should hit the viewer"* (`cut.on_action`), *"A static frame with no motion or darkness"* (`cut.invisible`). Two cards on this shelf disagree about the same pair of images in opposite directions — `cut.graphic_match` and `cut.form` point at each other, one asking the match to conceal and one asking it to sing — which is the clearest possible proof that this is a fork and not a preference.

**Axis three — Where does it fall against the beat: early, on it, late, or is the beat gone?**
Asked last, because it is the only axis that reaches the cards that take time out rather than place it: *"At an emotional peak, hold the face instead"* (`cut.cutaway`), *"Grief and confession need the opposite, a late cut"* (`cut.preemptive`), *"Action and reels, where every extra frame costs"* (`cut.late`), *"A sad beat, whose residue the hit erases"* (`cut.on_slam`), *"An ordinary beat, where time compresses not expands"* (`cut.overlap`), *"A waiting scene, whose subject the ellipsis destroys"* (`cut.elliptical`), *"Fast rhythms and reels; cut before they exit"* (`cut.clear_frame`), *"An action film that promised the event itself"* (`cut.aftermath`).

---

**The map**

**Axis one — what supplies the cut point**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A movement or an event in the picture** — a body, a gesture, an impact, an exit, a flash | `cut.on_action` · `cut.match_action` · `cut.on_impact` · `cut.in_whip` · `cut.motion_match` · `cut.invisible` · `cut.clear_frame` · `cut.overlap` · `cut.on_flash` · `cut.substitution` |
| **Something on the track** — a word, a beat, a bang, a silence | `cut.on_sound` · `cut.on_word` · `cut.on_slam` · `cut.rhythmic` · `cut.beat_drop` · `cut.to_silence` · `cut.sound_match` · `cut.jump_vlog` |
| **A face, and what is behind it** — a look, a blink, a reaction, a listener | `cut.eyeline` · `cut.pov` · `cut.on_look` · `cut.on_blink` · `cut.reaction` · `cut.reaction_first` · `cut.listener` · `cut.kuleshov` · `cut.double_take` · `cut.withheld` |
| **The geometry of the coverage** — the line, the angle, the direction, the position on screen | `cut.thirty_degree` · `cut.keep_180` · `cut.cross_line` · `cut.neutral` · `cut.screen_direction` · `cut.screen_position` · `cut.cheat` · `cut.axial` · `cut.double_angle` |
| **Nothing in the shot — you are deciding between two ideas, two rhythms or two durations** | `cut.hard` · `cut.cutaway` · `cut.insert` · `cut.hands` · `cut.screen_insert` · `cut.jump` · `cut.smash` · `cut.cross` · `cut.contrast` · `cut.graphic_match` · `cut.match_idea` · `cut.colour_match` · `cut.form` · `cut.texture_match` · `cut.elliptical` · `cut.preemptive` · `cut.late` · `cut.two_frame` · `cut.accelerate` · `cut.hold_then_fast` · `cut.srs_accel` · `cut.subliminal` · `cut.flash_frame` · `cut.to_black` · `cut.to_white` · `cut.wide_joke` · `cut.tight_fear` · `cut.tighten` · `cut.scale_reveal` · `cut.aftermath` |

**Axis two — what the join must do**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Vanish — the viewer must not feel that a cut happened** | `cut.on_action` · `cut.match_action` · `cut.invisible` · `cut.cheat` · `cut.thirty_degree` · `cut.keep_180` · `cut.screen_position` · `cut.screen_direction` · `cut.neutral` · `cut.eyeline` · `cut.on_look` · `cut.on_blink` · `cut.in_whip` · `cut.motion_match` · `cut.clear_frame` · `cut.two_frame` · `cut.form` · `cut.texture_match` · `cut.substitution` · `cut.jump_vlog` · `cut.on_word` · `cut.overlap` · `cut.elliptical` |
| **Rhyme — the viewer must notice a likeness and enjoy finding it** | `cut.graphic_match` · `cut.match_idea` · `cut.colour_match` · `cut.sound_match` · `cut.kuleshov` · `cut.contrast` · `cut.cross` · `cut.scale_reveal` · `cut.aftermath` · `cut.wide_joke` · `cut.double_take` · `cut.reaction_first` · `cut.subliminal` |
| **Carry — it says "and then" and claims nothing of its own** | `cut.hard` · `cut.cutaway` · `cut.insert` · `cut.hands` · `cut.screen_insert` · `cut.listener` · `cut.reaction` · `cut.pov` · `cut.tighten` · `cut.srs_accel` · `cut.accelerate` · `cut.rhythmic` · `cut.beat_drop` · `cut.late` · `cut.preemptive` · `cut.withheld` · `cut.hold_then_fast` · `cut.jump` · `cut.on_sound` |
| **Hit — the cut is the event and the viewer is meant to feel struck** | `cut.smash` · `cut.on_impact` · `cut.on_slam` · `cut.on_flash` · `cut.axial` · `cut.double_angle` · `cut.flash_frame` · `cut.to_black` · `cut.to_white` · `cut.to_silence` · `cut.tight_fear` · `cut.cross_line` |

**Axis three — where it falls against the beat**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Early — it lands before the beat has finished** | `cut.preemptive` · `cut.smash` · `cut.subliminal` · `cut.flash_frame` · `cut.two_frame` · `cut.tight_fear` · `cut.accelerate` · `cut.srs_accel` · `cut.double_angle` · `cut.axial` · `cut.beat_drop` · `cut.reaction_first` · `cut.on_flash` · `cut.clear_frame` · `cut.in_whip` |
| **Late — it is held past its cue and the holding is the content** | `cut.late` · `cut.withheld` · `cut.hold_then_fast` · `cut.cutaway` |
| **The beat is gone — the join is where the missing time went** | `cut.elliptical` · `cut.aftermath` · `cut.overlap` · `cut.jump` |
| **On the beat — it lands exactly on the event** | Every other card named in the two tables above. It is named by complement on purpose: naming forty-odd ids here would make the map longer than the shelf, which is the one thing the template forbids. |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally three to six cards wide.*

---

**The default, and the one against it**

**The default is `cut.hard` for the join with `cut.on_action` for the frame — and it is argued off the cards, not off the graph, because on this shelf the graph gives the wrong answer three separate ways.**

`cut.hard` and `cut.on_action` are two of only five cards here that read `Best in: formats: all | genres: all`. `cut.hard` is the only card on the shelf whose `Avoid when:` says it is never wrong in itself — its warning is not about the cut but about the intention behind it, *the decision is not whether to cut, it is exactly where*, which is precisely the question this card exists to make you answer. `cut.on_action` is what makes that frame invisible whenever a body is moving, and it is the only card on the shelf whose own text calls itself the core equation of the craft.

**Now the three ways in-degree lies here, because they are worth more than the default is.**

*The most-yielded-to card in the whole neighbourhood is `cut.hard`, and almost none of that traffic is about `cut.`* Nearly all of its inbound edges arrive from the other shelf, and seven of those fire on a single condition — the piece is serious and a visible device would be read as a device — while the remaining two say the neighbouring thing, that the scene has energy or tension any interval would drain. Inside this shelf `cut.hard` takes exactly one inbound edge. **Count the distinct conditions and the number collapses**: that in-degree measures how often the neighbouring shelf is too loud for the film, not what this shelf falls back on.

*The card this shelf actually defaults to, measured properly, is `cut.graphic_match`.* Four cards send a reader there and they give four unrelated reasons — `cut.match_idea` (*"Shapes match but the two ideas do not"*), `cut.colour_match` (*"Grade not built on colours; match shape instead"*), `cut.form` (*"When the match is poetry between acts"*) and `cut.texture_match` (*"When the join must register, not slip past"*). A card reached four times for four reasons is a floor. But it is the floor **of one region only**: a reader who is not building a match between two images never arrives there at all, which is why it is not the shelf's default and is named here instead.

*And `cut.late` is the clean counter-example.* Three cards yield to it and all three say the same thing — the beat has emotional residue and cutting it off destroys it. **Three edges, one condition: a door out of a region, not a fallback.** `cut.reaction` is the same shape, with three of its four inbound edges saying *the face is already doing the work*.

**The one against it is `cut.overlap`.** Nothing on the shelf routes to it; it is the target of no `Yields to:` anywhere in the package; and it is the only card here that makes an event **longer than it was**. Every other timing card on this shelf removes frames or moves them — `cut.elliptical` compresses, `cut.preemptive` trims, `cut.aftermath` deletes the event outright, and even `cut.late` is only refusing to cut yet. `cut.overlap` repeats the same action across two angles so the blow lands twice, which inverts the arithmetic the whole shelf is built on. Its only stated cost is that on an ordinary beat it overstates something that carries nothing — a cost a moment that genuinely deserves weight simply does not incur. Its near cousin against the grain is `cut.listener`, likewise never yielded to, and the only card on the shelf whose subject is a person doing nothing.

---

**The unasked**

**Just under half the reachable shelf is the target of no `Yields to:` field anywhere in the package.** They can be chosen but nothing ever sends you to them. By id:

`cut.accelerate` · `cut.aftermath` · `cut.beat_drop` · `cut.cheat` · `cut.clear_frame` · `cut.colour_match` · `cut.contrast` · `cut.double_angle` · `cut.double_take` · `cut.hands` · `cut.hold_then_fast` · `cut.invisible` · `cut.jump_vlog` · `cut.keep_180` · `cut.listener` · `cut.match_idea` · `cut.on_flash` · `cut.on_slam` · `cut.on_sound` · `cut.overlap` · `cut.pov` · `cut.rhythmic` · `cut.screen_direction` · `cut.screen_insert` · `cut.screen_position` · `cut.subliminal` · `cut.texture_match` · `cut.thirty_degree` · `cut.tight_fear` · `cut.to_white` · `cut.two_frame` · `cut.wide_joke`

**And the shape of that list is the finding, not its length.**

**First: the coverage-geometry region is almost entirely unasked.** `cut.keep_180`, `cut.thirty_degree`, `cut.screen_direction`, `cut.screen_position`, `cut.cheat` and `cut.double_angle` are all on the list — six of the nine cards under axis one's fourth value. Only `cut.cross_line` and `cut.neutral` are ever yielded to, and they yield to each other, which is one closed argument about whether to cross the line rather than a region anybody routes into. **Nobody on this shelf ever writes *instead of that, use the hundred-and-eighty line*, because the line is not an alternative to anything — it is the condition the other answers are measured against.** That is a second instrument reaching the same place a blind reading of the neighbouring `angle.` shelf reached, and it did so from the pair graph rather than from a banner. The dispute it touches is open and is not settled here; this shelf is routed as the package currently carries it, and the geometry cards are offered as choices because on this shelf they carry no line forbidding it.

**Second: the sound-led block yields outward and nothing yields inward.** `cut.on_sound`, `cut.on_slam`, `cut.rhythmic`, `cut.beat_drop` and `cut.jump_vlog` are all unasked, while `cut.to_silence` and `cut.sound_match` both leave the shelf entirely to reach a sound card. **The pair graph is a graph of pictures.** The readers who wrote these fields were comparing two things they could see; a cut decided by the ear is not an alternative to a cut decided by the eye, it is a different kind of answer, and the pair field has no way to say so. That is why axis one names the track as its own value rather than folding it into the picture, and why axis one is asked first.

**Third, and it is the new card this shelf wants.** The unasked list holds `cut.thirty_degree`, `cut.keep_180`, `cut.screen_direction` and `cut.cheat` — every card that assumes coverage exists — and the shelf has no card at all for the commonest real condition in generated work and in two-camera documentary: **the second angle was never shot.** The shelf can keep the line and it can cross it; it cannot tell you what to do when there is no line because there is only one setup. The nearest thing that exists records the gap in its own `Avoid when:` — `cut.withheld` says a cut you did not shoot the coverage for is not a style — and nothing routes a reader there to read it.

`cut.why_the_cut_falls_here`

---

### Standard Cut / Hard Cut

**Also called:** straight cut, butt cut  
**What it is:** An instant change from one shot to the next in a single frame, with no effect and no overlap between them.  
**Effect on the audience:** It says "and then" and imposes no feeling of its own. The viewer stops noticing it within the first minute because it is the natural language of moving pictures.  
**Used for and where it works best:** It carries more than ninety percent of any project: dialogue, coverage, action, documentary, all of it. Use it whenever you do not want the edit to speak and you want the faces and the story to do the work alone. In vertical short-form it is the backbone, because any effect between two shots costs attention you cannot spare.  
**Best in:** formats: all | genres: all  
**Avoid when:** It is never wrong in itself, but if every cut in the film is a plain cut with no intention behind it the edit ends up with no point of view. The decision is not whether to cut, it is exactly where.  
**Prompt:** `editor: plain straight cut with no transition, and pick the frame so the incoming shot opens on the next piece of information`  
`cut.hard`

### Cut on Action

**Also called:** cutting on movement, action cut  
**What it is:** You cut while a movement is still running in frame, a stand, a turn, a throw, a door opening, rather than after the movement settles.  
**Effect on the audience:** The cut disappears because the eye is busy following the movement and finishes it in the new shot instead of registering the change. This is the core equation of invisible editing.  
**Used for and where it works best:** The golden rule for any scene with a body in motion: rising from a chair, drawing a blade, knocking on a door, throwing a ball. In action and fight work it is what keeps a fight readable instead of chaotic, and in documentary it lets you cut an interview on the guest's gesture so the trim never reads as a jump. The trick is to cut two or three frames after the movement starts, not before it and not after it ends.  
**Best in:** formats: all | genres: all  
**Avoid when:** Do not use it when you want the cut itself to hit the viewer, as in a smash cut. And if the movement has already finished before you cut, the cover is gone and the cut reads as a jump.  
**Prompt:** `editor: cut two to three frames after the movement begins, never after it settles, so the eye rides the motion across the cut`  
**Yields to:** `cut.smash` — When the cut itself should hit the viewer.  
`cut.on_action`

### Match on Action

**Also called:** matching action, action match, continuity cut  
**What it is:** The same action is covered in full from two angles and the cut lands mid-movement so the hand, the speed and the direction continue exactly in the second shot.  
**Effect on the audience:** It makes the event feel single and unbroken, and the new angle reads as a second pair of eyes on the same moment rather than a new moment.  
**Used for and where it works best:** This is the difference between a clean cut and a sloppy one in any dialogue or action scene covered with more than one setup. Ask the actor to repeat the move at the same speed in every angle and keep half a second of overlap on both heads and tails. It matters most in drama, series and action, and with AI clips you design the last frame of the first clip and the first frame of the second on the same body position.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Commercial / TVC, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, AI-Generated Clip | genres: Drama, Action, Thriller / Suspense, Crime / Procedural, Historical / Biopic, Heritage (civilisation-focused), War, Martial Arts / Wuxia, Shonen Battle (anime)  
**Avoid when:** If the speed changes between the two angles the match breaks and the cut becomes louder than no cut at all. Cutting on action decides the timing, matching on action decides the accuracy, so do not confuse the two.  
**Prompt:** `editor: overlap the same action in both angles, match speed and hand position, and place the cut mid-gesture so the movement completes in the new shot`  
`cut.match_action`

### The Thirty Degree Rule

**Also called:** 30 degree rule  
**What it is:** When you cut back to the same subject the camera angle must move at least thirty degrees, or the shot size must change by two clear steps.  
**Effect on the audience:** Less than that and the eye feels a small slip, as if the picture slid rather than the camera moved. Respect the rule and the cut reads as a decision instead of an accident.  
**Used for and where it works best:** It is a shooting rule before it is an editing rule: when you lay out coverage for a dialogue scene or a documentary setup, place every angle far enough from the last one. Break it on purpose and you get a nervous jump, which is a style choice and not a mistake as long as it is intended.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Documentary Feature, Documentary Series, Interview / Video Podcast, Commercial / TVC, Anime (Japanese 2D), 3D CG Animation | genres: Drama, Thriller / Suspense, Crime / Procedural, Mystery / Whodunit, Historical / Biopic, Heritage (civilisation-focused), Verite / Observational, Comedy  
**Avoid when:** Do not treat it as sacred in documentary when you only have two cameras; cover the seam with a cutaway instead. In a deliberately jumpy style it is the first rule you break on purpose.  
**Prompt:** `editor: when returning to the same subject change the angle by at least thirty degrees or jump two shot sizes, otherwise the cut reads as a slip`  
**Yields to:** `cut.cutaway` — Documentary with two cameras; cover the seam instead.  
`cut.thirty_degree`

### Eyeline Match

**Also called:** eyeline match cut  
**What it is:** A shot of someone looking off screen, then a cut to the thing they are looking at, respecting the same direction and roughly the same height.  
**Effect on the audience:** It bolts the viewer's mind to the character's mind without a word. You do not simply see the object, you see it because she saw it.  
**Used for and where it works best:** Any beat of discovery, noticing or fear: the character turns toward the door, spots a note, catches a face in a crowd. In horror it also works in reverse, you cut to what she is looking at and find nothing, then cut back. In heritage documentary it gives you the face looking, then the carving or the wall it is looking at.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Anime (Japanese 2D), 3D CG Animation, Heritage / Historical Documentary, Documentary Feature, Game Cinematic / Gameplay, AI-Generated Clip | genres: Drama, Thriller / Suspense, Horror, Mystery / Whodunit, Romance, Heritage (civilisation-focused), Historical / Biopic, Shonen Battle (anime), Psychological Horror  
**Avoid when:** If the direction flips, she looks left and the object also comes from the left, the eye senses something wrong without knowing why. And do not repeat it every beat or the scene becomes a dead chain of look and see.  
**Prompt:** `editor: cut from the look to the object on the matching screen direction and eye height, holding the look one beat longer than feels natural`  
**Yields to:** `cut.on_look` — When the head or eye moves, ride it.  
`cut.eyeline`

### POV Cut / Point of View Cut

**Also called:** subjective cut, POV insert  
**What it is:** Instead of cutting to the object from a neutral angle, the camera becomes the character's own eyes: same height, same distance, sometimes the same breathing and shake.  
**Effect on the audience:** It moves the viewer from watching to being. Far stronger than a plain eyeline match but heavier, because it removes the distance completely.  
**Used for and where it works best:** The beat of fear, desire or concentration: looking through a keyhole, a sniper's eye, a child looking up at adults. In horror, in game cinematics and in first person storytelling it is the backbone of the style, and in advertising it makes the viewer feel the product is in their own hands.  
**Best in:** formats: Feature Film, Short Film, Drama Series Episode, Game Cinematic / Gameplay, 360 / VR, Anime (Japanese 2D), Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Horror, Thriller / Suspense, Psychological Horror, Action, Mystery / Whodunit, Slasher, Romance, Sci-Fi, Found Footage  
**Avoid when:** Used without a reason it becomes a gimmick and loses its power in the scene that actually needs it. It also needs a face shot before or after it, otherwise the viewer does not know whose eyes these are.  
**Prompt:** `editor: cut to a true point of view frame at the character's eye height with her breathing and micro shake, then cut back to her face to close the loop`  
**Yields to:** `cut.eyeline` — When removing the distance is too heavy.  
`cut.pov`

### Reaction Cut

**Also called:** cut to the reaction  
**What it is:** Instead of staying on the event you cut to the face receiving it: the one who saw, the one who heard, the one who was hit by it.  
**Effect on the audience:** The face tells the viewer what to feel, and most of the time the reaction is stronger than the event itself because imagination fills the rest.  
**Used for and where it works best:** After bad news, after the blow, after the reveal, and in comedy immediately after the line. In horror it is the cheapest and strongest solution: do not show the creature, show the face that saw it. In documentary and interview a cut to the listener's face gives you a clean exit out of any long answer.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Short Film, Documentary Feature, Interview / Video Podcast, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), 3D CG Animation, Commercial / TVC | genres: Drama, Comedy, Horror, Thriller / Suspense, Romance, Melodrama, Mystery / Whodunit, Family, Shonen Battle (anime)  
**Avoid when:** Cut to the face too late and the reaction reads as acting. Cut just before the expression starts so the viewer watches it form.  
**Prompt:** `editor: cut to the listening face one beat before the expression lands, and hold it two beats longer than the line needs`  
`cut.reaction`

### Cut to the Listener

**Also called:** staying on the listener, off-speaker cut  
**What it is:** In a dialogue scene you hold the picture on the person listening instead of the person talking, and the voice continues from off screen.  
**Effect on the audience:** It turns dialogue from an exchange of words into the effect of words. The viewer stops hearing the line and starts watching what the line does.  
**Used for and where it works best:** It is the single most important edit decision in any confession, bad news or threat scene: keep the camera on the one who is about to break, not on the one talking. In drama, legal and crime work it is where the real information lives, and in documentary interviews it gives you the one cut that never breaks continuity.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Soap Opera / Telenovela, Interview / Video Podcast, Documentary Feature, Documentary Series, Short Film, Anime (Japanese 2D) | genres: Drama, Melodrama, Crime / Procedural, Legal Drama, Political Thriller, Mystery / Whodunit, Romance, Tragedy, Medical Drama  
**Avoid when:** If the line itself is the event, a threat, a joke, an announcement, stay on the speaker. And cutting to the listener on every single line makes the scene slow and soft.  
**Prompt:** `editor: hold on the listening face while the other voice continues off screen, and cut back to the speaker only on the word that changes the scene`  
**Yields to:** `frame.shot_reverse_shot` — When the line itself is the event.  
`cut.listener`

### Cut on the Look

**Also called:** cut on the turn, cut on the glance  
**What it is:** You cut on the exact frame where the eye or the head moves, not after the look has settled.  
**Effect on the audience:** The fast movement of the eye covers the cut completely, and the viewer feels the second shot arrived because the character called for it.  
**Used for and where it works best:** Tense dialogue scenes where the character turns to someone else in the room, and the alert beat in horror and suspense. It is the cleanest version of an eyeline match because it uses movement as cover. It works beautifully in anime and in fast advertising because it delivers energy without any camera move.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Anime (Japanese 2D), 3D CG Animation, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, AI-Generated Clip | genres: Thriller / Suspense, Horror, Drama, Crime / Procedural, Action, Mystery / Whodunit, Shonen Battle (anime), Romance  
**Avoid when:** If the turn is slow and dramatically deliberate, cutting on it kills it. Let a slow turn finish inside the same shot.  
**Prompt:** `editor: place the cut on the first frames of the head or eye movement so the turn completes in the next angle`  
**Yields to:** `cut.withheld` — A slow deliberate turn must finish uncut.  
`cut.on_look`

### Cut on the Blink

**Also called:** Murch blink point  
**What it is:** Walter Murch's observation: a person blinks when a thought ends, so the blink is where the cut naturally belongs. You cut on the frame where the actor blinks, or on the moment the viewer would blink.  
**Effect on the audience:** The cut syncs with the breathing of the thought itself, so it is never felt. It is the softest way to cut on a still face with no movement to cover you.  
**Used for and where it works best:** Face scenes, confessions, monologues, and documentary interviews where the guest thinks before answering. When you have no body movement to cover the cut, the blink is your movement. It is at its best in slow drama, documentary and portrait work.  
**Best in:** formats: Feature Film, Limited Series, Documentary Feature, Documentary Series, Interview / Video Podcast, Short Film, Drama Series Episode, Heritage / Historical Documentary | genres: Drama, Tragedy, Mystery / Whodunit, Psychological / Arthouse, Verite / Observational, Historical / Biopic, Melodrama, True Crime  
**Avoid when:** It is no use in fast action, where movement leads instead of thought. And do not chase it on every cut; it is a tool for still scenes.  
**Prompt:** `editor: find the actor's blink at the end of the thought and cut on that frame, letting the idea close before the new shot starts`  
**Example:** Walter Murch describes this blink point in his editing book In the Blink of an Eye.  
**Yields to:** `cut.on_action` — Fast action, where movement leads instead of thought.  
`cut.on_blink`

### Cutaway

**Also called:** B-roll cut, insert away, cutaway shot  
**What it is:** A cut to something outside the main action, a hand, a window, a clock, another face, the location, and then back to the action.  
**Effect on the audience:** It removes dead time, hides a continuity problem and adds information or mood without stopping the scene. It also builds meaning by juxtaposition: a face, then a clock, means time is running out.  
**Used for and where it works best:** The editor's safety net: whenever you need to shorten an interview, remove an actor's hesitation, join two answers that were never next to each other, or stretch a scene of waiting and tension. In documentary it is half the job, the hand or the location over the guest's voice, and in heritage work it moves from the narrator to the relief, the map or the ruins. In sitcom the cut to something else is the joke itself.  
**Best in:** formats: all | genres: all  
**Avoid when:** A cutaway that does not serve the meaning becomes filler and advertises that you are hiding a mistake, and holding one longer than needed breaks the rhythm of the speech. Cutting away at an emotional peak usually throws away the face you spent the scene building; the exception is when looking away is itself the emotion, because the audience needs somewhere to put it.  
**Prompt:** `editor: cover the seam with a two second cutaway that adds information, cutting away before the seam and returning after it`  
**Yields to:** `cut.late` — At an emotional peak, hold the face instead.  
`cut.cutaway`

### Cut-In / Insert

**Also called:** insert shot, detail cut, cut in  
**What it is:** A cut to a detail inside the same action and the same space: the watch on his wrist, the knife on the table, the letter, the lock. The same subject that was in the master, in a tighter size.  
**Effect on the audience:** It forces the viewer's attention onto one object and says "this matters", and it creates tension by giving information the character does not have yet. It also gives a long take a pulse in the cut.  
**Used for and where it works best:** Planting the information before the scene needs it: the key before the escape, the pills before the attack, the name on the paper before the phone call. In crime and suspense it is the investigation tool, in advertising it is the shot that sells the product, and in a documentary interview it is the cut to the hands on the sensitive line. In heritage documentary it is the detail in the relief a beat before the narration explains it.  
**Best in:** formats: all | genres: all  
**Avoid when:** Insert every detail and the device loses its value, the scene becomes a catalogue, and a detail that never pays off later is a lie to the viewer. Do not cut in on the same axis without enough size change either, or it reads as a jump.  
**Prompt:** `editor: cut in to a tight detail of the object for about one second, then return to the wider angle on the same axis`  
`cut.insert`

### Cut to the Hands

**Also called:** hands insert  
**What it is:** A short cut to the hands doing something: shaking, turning a ring, drawing a weapon, making something, touching an old stone.  
**Effect on the audience:** Hands reveal what the face is hiding. Fear, lying and desire all show up in the hands before they reach the eyes.  
**Used for and where it works best:** Interrogation, confession and waiting scenes, where the face is calm and the hands give it away. In craft and heritage documentary it is the single most valuable shot, because the whole trade lives in the fingers. In advertising and product work the hand gives the object scale and texture without a word.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Documentary Series, Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Anime (Japanese 2D) | genres: Drama, Thriller / Suspense, Crime / Procedural, Heritage (civilisation-focused), Historical / Biopic, Romance, Mystery / Whodunit, Tragedy, Science / Educational  
**Avoid when:** If the hand is empty and doing nothing the shot is filler. And do not cut to the hands in a beat where the face is carrying everything.  
**Prompt:** `editor: cut to a tight shot of the hands at the moment they betray the character, hold it for one beat, then cut back to the face`  
**Yields to:** `cut.reaction` — When the face is carrying the whole beat.  
`cut.hands`

### Jump Cut

**Also called:** jump  
**What it is:** A cut inside what is almost the same shot: same angle, same size, but time has suddenly jumped. The frame has not changed enough to justify the cut.  
**Effect on the audience:** It breaks continuity in the viewer's face, producing a nervous, glitching feeling and the sense of torn time or a disturbed mind.  
**Used for and where it works best:** The beat of anxiety, waiting or psychological collapse, and compressing time inside one shot, hours of waiting in four seconds. It became a language with Jean-Luc Godard in Breathless, and today it is the native style of fast content and reels. In advertising it delivers a young, restless energy.  
**Best in:** formats: Feature Film, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, Meme / Comedy Edit, Music Video, Commercial / TVC, Video Essay, Vertical Micro-Drama, Experimental / Art Film | genres: Psychological / Arthouse, Comedy, Dark Comedy / Satire, Thriller / Suspense, Drama, Surreal / Absurdist, Coming of Age, Crime / Procedural  
**Avoid when:** Letting it happen by accident is what costs you: if it is not intentional it reads as an editing mistake and takes the viewer's trust with it. In classical drama and serious heritage work it lands as noise.  
**Prompt:** `editor: cut out a chunk of time from the same framing so the subject snaps to a new position, keeping the angle and size identical`  
**Example:** Breathless by Jean-Luc Godard, the car scenes where the jump cuts became a style.  
`cut.jump`

### Talking Head Jump Cut

**Also called:** filler cut, vlog jump cut  
**What it is:** The same mechanic as a jump cut but with a practical goal: you remove hesitations, pauses and filler words from someone talking to camera, and you leave the jump visible. It differs from The Visible Jump Cut in an Interview in documentary, where the exposed jump is an honesty signal that the answer was condensed: here the aim is density and pace, not a declaration.  
**Effect on the audience:** It raises the density of information per second and makes the speech sound confident and quick. Audiences are used to it now, so they do not read it as an error.  
**Used for and where it works best:** Vlogs, Shorts, TikTok and explainer video, where every sentence lands with no air between them. The trick to keep it from getting ugly: nudge the framing slightly between cuts, or drop a cutaway every third jump. In short ads it lets you fit three sentences into five seconds.  
**Best in:** formats: Vlog / YouTube Long-Form, Vertical Short-Form (Reels, Shorts, TikTok), Video Essay, Explainer, Corporate / Training, Meme / Comedy Edit, News Report / Reportage, Interview / Video Podcast, Kids Content | genres: Comedy, Science / Educational, Dark Comedy / Satire, Slice of Life, Family, Verite / Observational  
**Avoid when:** Twenty jumps in a row with no size change tires the eye and makes the speaker look chopped up. In a serious interview or a documentary testimony a jump cut made for pace damages the speaker's credibility; an exposed jump that tells the viewer the answer was condensed is a different decision, `doc.interview_jump_cut`.  
**Prompt:** `editor: remove every pause and filler word, nudge the frame scale by five percent between cuts, and drop a cutaway every third jump`  
**Yields to:** `doc.interview_jump_cut` — When the exposed jump signals honesty, not pace.  
`cut.jump_vlog`

### Smash Cut

**Also called:** shock cut  
**What it is:** A cut from total calm straight into violence or loud sound, or the reverse, with no visual or audio preparation at all.  
**Effect on the audience:** A hit to the nervous system. The impact comes from the gap between the calm and what follows, not from the shot itself.  
**Used for and where it works best:** Horror, silence then the scream; action, sleep then the explosion; and comedy, the character says "nothing can go wrong" and you cut to the disaster. In trailers and reels it is the hook tool in the first second. The trick is to make the shot before it longer and quieter than feels natural so the hit doubles.  
**Best in:** formats: Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Short Film, Drama Series Episode, Commercial / TVC, Meme / Comedy Edit, Anime (Japanese 2D), Music Video, AI-Generated Clip | genres: Horror, Thriller / Suspense, Action, Comedy, Dark Comedy / Satire, Slasher, Psychological Horror, War, Shonen Battle (anime)  
**Avoid when:** Use it more than twice in one scene and it loses every bit of power and becomes noise. In quiet drama and reflective documentary it lands as cheap.  
**Prompt:** `editor: hold the quiet shot two seconds longer than comfortable, then hard cut straight into the loudest frame of the next shot with full level`  
`cut.smash`

### Cross Cutting / Parallel Editing

**Also called:** intercutting, parallel cut  
**What it is:** Alternating between two or more actions in different places at the same time, each one continuing from where it stopped.  
**Effect on the audience:** Mathematical tension: the viewer knows something one of the two characters does not, and the mind keeps measuring the distance still left between them.  
**Used for and where it works best:** Chases, heists, countdowns, a birth against a death, and any climax that needs two lines to converge. The trick is to shorten each block progressively as they close in, the standard climax equation of every action film. In documentary and heritage work you can intercut the excavation line with the ancient story line.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Trailer / Teaser, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Documentary Feature, Heritage / Historical Documentary | genres: Action, Thriller / Suspense, Heist, Crime / Procedural, War, Drama, Adventure, Spy / Espionage, Disaster, Shonen Battle (anime)  
**Avoid when:** If the two lines have no dramatic relationship the switching is just an irritation and kills focus. And do not start shortening from the beginning or you leave yourself nowhere to escalate.  
**Prompt:** `editor: alternate the two locations in blocks, shortening each block as they converge, and land the last cut on the moment they meet`  
**Example:** The Godfather, the baptism intercut with the murders.  
**Yields to:** `seq.crosscut_sequence` — The intercutting runs across whole sequences, not inside one scene.  
`cut.cross`

### Contrast Cut

**Also called:** juxtaposition cut  
**What it is:** A cut straight between two opposites: a feast and a famine, laughing and crying, a palace and a tent, a party and a funeral.  
**Effect on the audience:** The cut itself becomes a comment. Here the editor is the one speaking, not the characters, and the viewer reaches the verdict alone.  
**Used for and where it works best:** Social and political documentary, charity advertising, and any film comparing two classes or two eras. In heritage work: the civilisation at its peak, then the same place in ruins. The two shots should share a composition so the difference hits harder.  
**Best in:** formats: Documentary Feature, Documentary Series, Heritage / Historical Documentary, Video Essay, Commercial / TVC, News Report / Reportage, Feature Film, Music Video, Short Film, Trailer / Teaser | genres: Political Thriller, Drama, Heritage (civilisation-focused), Historical / Biopic, War, Tragedy, Dark Comedy / Satire, Science / Educational, Dystopia / Post-Apocalyptic  
**Avoid when:** If the contrast is too obvious it turns into preaching and the viewer pushes back. In character driven drama it reminds you the director is there and breaks the immersion.  
**Prompt:** `editor: cut directly between two shots that share the same composition but carry opposite meanings, with no transition and no music change`  
`cut.contrast`

### Kuleshov Cut

**Also called:** Kuleshov effect  
**What it is:** The same neutral face is cut against food, then a coffin, then a child, and every time the viewer swears the expression changed. This is Lev Kuleshov's experiment.  
**Effect on the audience:** It proves that meaning is born between two shots, not inside them. The viewer fills the gap, and that is the cheapest and strongest source of emotion you have.  
**Used for and where it works best:** When you do not have a strong performance or a budget: shoot a calm face and let the next cut do the acting. It is the backbone of anime, documentary and AI generated shots, where the face cannot deliver a complex expression. In heritage work: the still face of a statue, then a burning city.  
**Best in:** formats: AI-Generated Clip, Anime (Japanese 2D), Documentary Feature, Heritage / Historical Documentary, Short Film, Feature Film, Experimental / Art Film, 3D CG Animation, Music Video | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Psychological / Arthouse, Tragedy, Horror, Mythology / Ancient Epic, War  
**Avoid when:** If the face is already acting hard the cut becomes redundant and fights the performance. And do not rely on it to build a complex relationship, it is a moment tool, not a story tool.  
**Prompt:** `editor: hold a neutral face for two seconds, cut to the object that defines the emotion, then cut back to the identical face`  
**Yields to:** `cut.reaction` — When the face is already acting hard.  
`cut.kuleshov`

### Graphic Match

**Also called:** graphic cut, shape match  
**What it is:** Two similar shapes in frame: the disc of the sun then the circle of an eye, a wheel then a clock, a dome then an egg. Shape, position and size are close across the cut.  
**Effect on the audience:** It builds a poetic link between two things with no logical relationship, and the eye relaxes because it does not have to travel.  
**Used for and where it works best:** Chapter transitions, documentary, music video and heritage work, a shape in an ancient carving and then the same shape in something modern. It shines in music video where images work by rhythm rather than logic. With generated clips you design the last frame and the first frame around the same circle or the same line.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Music Video, Title Sequence / Opening Credits, Video Essay, Feature Film, Trailer / Teaser, Experimental / Art Film, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, Psychological / Arthouse, Drama, Mythology / Ancient Epic, Surreal / Absurdist, Science / Educational, Fantasy / Epic  
**Avoid when:** If the resemblance is weak it simply fails and looks like a try that missed. And do not drop it inside a tense scene, it stops the tension and pulls the viewer a step back.  
**Prompt:** `editor: match the dominant shape, its size and its screen position across the cut so the form stays put while the subject changes`  
**Example:** Psycho, the shower drain matched to the eye.  
**Yields to:** `cut.form` — Inside a scene, where the match must conceal; and `cut.match_idea` — the shape holds and the meaning transforms too.  
`cut.graphic_match`

### Match Cut

**Also called:** idea match cut, conceptual match  
**What it is:** Stronger than a graphic match: the shape holds but the meaning, the time and the place change completely, like a bone thrown into the sky becoming a spacecraft.  
**Effect on the audience:** It jumps thousands of years or thousands of miles in a single frame, and makes the viewer feel the two ideas are one idea.  
**Used for and where it works best:** The epic transition between two acts, historical documentary, and the big time jump in heritage work, a hand shaping clay then a hand on a keyboard. It has to land on a structural moment, not just anywhere. With generated clips you write the last frame and the first frame with the same motion and the same placement.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Trailer / Teaser, Title Sequence / Opening Credits, Music Video, Video Essay, Short Film, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Sci-Fi, Drama, Fantasy / Epic, War, Psychological / Arthouse  
**Avoid when:** Repeated as a trick it loses its scale. And built between two shots with no conceptual link it usually reads as editing showing off; the exception is a purely rhythmic piece such as a music video, where the shape of the cut is the idea.  
**Prompt:** `editor: design the outgoing last frame and the incoming first frame to share the same shape and motion, then cut on the peak of the movement`  
**Example:** 2001 A Space Odyssey, the bone thrown up and matched to the orbiting craft.  
**Yields to:** `cut.graphic_match` — Shapes match but the two ideas do not.  
`cut.match_idea`

### Motion Match Cut

**Also called:** movement match, directional match cut  
**What it is:** It is not the shape that matches but the direction and speed of the movement: a car crossing left to right, then a train crossing in the same direction at the same speed.  
**Effect on the audience:** The energy never drops. The viewer moves between two worlds while keeping exactly the same momentum.  
**Used for and where it works best:** Moving from one action scene to another, sports montage and fast music video. In advertising: a hand opening a door then a hand opening the product along the same arc. In reels it is the cleanest transition of all because it needs no effect whatsoever.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Trailer / Teaser, Sports Broadcast / Sports Film, Feature Film, Anime (Japanese 2D), 3D CG Animation, Product Video / Motion Design, AI-Generated Clip | genres: Action, Sports Drama, Musical, Adventure, Thriller / Suspense, Martial Arts / Wuxia, Shonen Battle (anime), Sports Anime  
**Avoid when:** If the two speeds differ the viewer feels a stumble instead of a flow. And do not use it when you want the viewer to notice that the place has changed.  
**Prompt:** `editor: match the direction and the speed of the movement across the cut so the motion continues unbroken into the new location`  
**Yields to:** `cut.hard` — When the viewer should notice the place changed.  
`cut.motion_match`

### Colour Match Cut

**Also called:** colour bridge cut  
**What it is:** Both shots share a dominant colour, or a block of colour in the same part of the frame: the red of blood then the red of a dress, the blue of the sea then the blue of a wall.  
**Effect on the audience:** The eye holds on to the colour and misses the change of place, and one shared feeling keeps linking the two scenes even after the subject changes.  
**Used for and where it works best:** Music video, fashion film and advertising, where mood outranks logic. In drama it lets you link two characters with one recurring colour across the whole film, so every return of the red returns the idea. In heritage work: the blue of the glazed brick, then the blue of the sky over the city.  
**Best in:** formats: Music Video, Fashion Film, Commercial / TVC, Product Video / Motion Design, Title Sequence / Opening Credits, Feature Film, Heritage / Historical Documentary, Experimental / Art Film, AI-Generated Clip | genres: Romance, Drama, Musical, Psychological / Arthouse, Surreal / Absurdist, Heritage (civilisation-focused), Fantasy / Epic, Melodrama  
**Avoid when:** If the film's grade is not built on clear colours the match will not register. And do not force a shot into a colour that is not its own, it will look painted.  
**Prompt:** `editor: cut between two shots that share the same dominant colour in the same area of frame, keeping the grade consistent across the cut`  
**Yields to:** `cut.graphic_match` — Grade not built on colours; match shape instead.  
`cut.colour_match`

### Form Cut

**Also called:** form match, disguised cut  
**What it is:** A cut inside the same scene between two objects that share the same mass or line in the same part of the frame, made to hide the cut rather than to build a poetic meaning.  
**Effect on the audience:** The eye never travels, so the cut passes as if it never happened. It is the oldest invisible editing method, older than the spread of cutting on action.  
**Used for and where it works best:** For cutting inside a still scene with no movement to cover you: a dark shoulder into a dark wall, the edge of a table into the edge of a window. It is very useful in heritage documentary where the shots are static, and with generated clips because it lets you join two pieces that have no real continuity.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, AI-Generated Clip, Experimental / Art Film, Feature Film, Short Film, Title Sequence / Opening Credits, Video Essay | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Psychological / Arthouse, Mythology / Ancient Epic, Science / Educational, Mystery / Whodunit  
**Avoid when:** It differs from a graphic match: this one serves concealment inside a scene, that one serves poetry between acts, so do not confuse the intentions. And if the two masses are not in exactly the same position the cut becomes more visible, not less.  
**Prompt:** `editor: align the dominant mass or line of both shots in the same screen position, then cut on the frame where their edges overlap`  
**Yields to:** `cut.graphic_match` — When the match is poetry between acts.  
`cut.form`

### Invisible Cut / Hidden Cut

**Also called:** stitched cut, seamless cut, whip-pan cut, wipe-by cut, morph cut  
**What it is:** The cut is buried behind something that fills the frame completely: a body passing the lens, total darkness, a pass behind a column, or a whip pan that smears the image — though in serious drama and heritage documentary the whip plays as juvenile (`cut.in_whip`), so there the cover is a body, darkness or a column. The motion continues from the first shot into the second at the same direction and speed.  
**Effect on the audience:** The viewer believes the shot is one long unbroken take, which delivers real time and continuous pressure.  
**Used for and where it works best:** Building a long single take, the magic move between two rooms or two eras, and moving between two locations in vertical short-form. It is your single most important tool in AI video: you build a long shot out of five second clips by having each clip start and end on an object that fills the frame or on darkness. Ask the model to pass a shoulder, a wall or a cloak across the lens in the final second.  
**Best in:** formats: Feature Film, Short Film, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Trailer / Teaser, Title Sequence / Opening Credits, Game Cinematic / Gameplay, 3D CG Animation, 360 / VR, AI-Generated Clip | genres: Thriller / Suspense, Drama, Action, Horror, Fantasy / Epic, War, Sci-Fi, Mystery / Whodunit, Heritage (civilisation-focused), Comedy, Adventure, Surreal / Absurdist  
**Avoid when:** If the light, the movement or its direction does not match on both sides the seam shows more than a plain cut would, and it does not belong in a scene that needs a fast cutting rhythm, because it is a tool for continuity, not for pace. Hiding a cut on a static frame rarely works either, because the cover needs motion or darkness to carry it.  
**Prompt:** `editor: hide the cut behind a full frame wipe, a body passing the lens or two frames of darkness, matching light and motion speed on both sides`  
**Example:** Rope by Alfred Hitchcock, the cuts hidden on a back filling the lens.  
**Yields to:** `cut.form` — A static frame with no motion or darkness.  
`cut.invisible`

### Axial Cut

**Also called:** concentration cut, cut along the lens axis  
**What it is:** A cut to the same subject on exactly the same angle but a closer or wider size, so the camera jumps along the lens axis instead of moving around it.  
**Effect on the audience:** It delivers a sudden intrusion, as if the film grabs the viewer's head and pushes it forward one step at a time.  
**Used for and where it works best:** The beat of realisation, rage or dread: three axial cuts in a row on the same face or the same door build pressure with no camera movement at all. It is excellent in anime, in horror and in heritage work, wide on the ziggurat then closer then closer again. With generated clips it is the cheapest escalation you have because it needs no motion.  
**Best in:** formats: Anime (Japanese 2D), Feature Film, Short Film, Heritage / Historical Documentary, AI-Generated Clip, 3D CG Animation, Trailer / Teaser, Drama Series Episode, Game Cinematic / Gameplay | genres: Horror, Thriller / Suspense, Shonen Battle (anime), Drama, Mythology / Ancient Epic, Heritage (civilisation-focused), Psychological Horror, Samurai / Chanbara, War  
**Avoid when:** If the size difference between the two shots is small you get a jump instead of an intrusion. Make every step change the size clearly.  
**Prompt:** `editor: cut straight down the same lens axis to a clearly tighter size, repeating twice more for a three step push without moving the camera`  
`cut.axial`

### Overlapping Edit

**Also called:** expanded time cut, repeated action edit  
**What it is:** A portion of the action is repeated in the second shot instead of continuing, so the event takes longer than its real duration. This is Sergei Eisenstein's method on the Odessa steps.  
**Effect on the audience:** It stretches the moment and makes it bigger than life. The viewer feels time thicken, which is the feeling of catastrophe and of epic.  
**Used for and where it works best:** The fall, the explosion, the knockout blow, the arrival of the army. The more important the moment, the more you stretch it by repeating a slice of the action from another angle. It is the backbone of epic action and anime montage, and in heritage work it carries the moment a wall falls or a king arrives.  
**Best in:** formats: Feature Film, Anime (Japanese 2D), 3D CG Animation, Trailer / Teaser, Music Video, Short Film, Game Cinematic / Gameplay, Heritage / Historical Documentary, AI-Generated Clip | genres: War, Action, Mythology / Ancient Epic, Historical / Biopic, Heritage (civilisation-focused), Tragedy, Disaster, Shonen Battle (anime), Martial Arts / Wuxia  
**Avoid when:** Applied to an ordinary beat it makes the edit overstate something that carries nothing. In comedy and observational documentary it destroys credibility on the spot.  
**Prompt:** `editor: repeat the last third of the action at the head of the next angle so the movement happens twice and the moment expands`  
**Example:** Battleship Potemkin, the Odessa steps sequence.  
**Yields to:** `cut.elliptical` — An ordinary beat, where time compresses not expands.  
`cut.overlap`

### Elliptical Edit

**Also called:** ellipsis, compression cut  
**What it is:** You remove a chunk of the event and let the viewer complete it: a hand reaching for the handle, cut, and he is already inside the room. The opening and the entering are gone.  
**Effect on the audience:** It speeds the film up and respects the viewer's intelligence. What is removed becomes stronger than what is shown, because imagination does the work.  
**Used for and where it works best:** Every everyday transition: walking, arriving, opening a door, eating, travelling. The working rule is to enter the scene late and leave it early. In vertical micro drama and reels it is a survival requirement, because there is no time for any redundant movement.  
**Best in:** formats: Feature Film, Drama Series Episode, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Commercial / TVC, Trailer / Teaser, Anime (Japanese 2D), Limited Series, Vlog / YouTube Long-Form | genres: Drama, Thriller / Suspense, Crime / Procedural, Comedy, Action, Romance, Mystery / Whodunit, Heist, Coming of Age  
**Avoid when:** Cut out necessary information and the viewer gets lost and starts reasoning instead of watching. In scenes whose subject is waiting, the ellipsis destroys the subject itself.  
**Prompt:** `editor: cut out the middle of the action, start the new shot at the result, and trust the viewer to fill the gap`  
**Yields to:** `cut.cutaway` — A waiting scene, whose subject the ellipsis destroys.  
`cut.elliptical`

### Cut to the Aftermath

**Also called:** skip the event cut, off-screen event cut  
**What it is:** You never show the event: you cut just before it and come back after it on the result, the broken door, the blood on the floor, the empty face.  
**Effect on the audience:** The viewer's imagination builds a version worse than anything you could shoot. The gap between the two shots becomes the horror.  
**Used for and where it works best:** Violence, death, scandal, and anything your budget cannot afford to shoot. In horror, crime and serious drama it is the strongest option, not the cheapest one. In heritage and documentary work it is also the ethical solution: the result of the battle instead of the battle, the ruins instead of the fire.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Heritage / Historical Documentary, Documentary Feature, Docudrama / Reenactment, Anime (Japanese 2D), AI-Generated Clip | genres: Horror, Crime / Procedural, Drama, Thriller / Suspense, War, Tragedy, Historical / Biopic, Heritage (civilisation-focused), True Crime, Psychological Horror  
**Avoid when:** If the event itself is what the film promised the audience, as in an action film, skipping it reads as a betrayal. And do not use it every time or it becomes a habit of avoidance.  
**Prompt:** `editor: cut away one beat before the event and return on the stillness after it, letting sound carry what the picture refuses to show`  
**Example:** No Country for Old Men, the killing of Llewelyn Moss happens off screen and we arrive after.  
**Yields to:** `cut.on_impact` — An action film that promised the event itself.  
`cut.aftermath`

### Pre-emptive Cut / Cutting Early

**Also called:** anticipatory cut  
**What it is:** You cut a touch before the viewer is finished with the current shot, so the cut arrives before the mind asks for it.  
**Effect on the audience:** It makes the film feel faster than the viewer and pulls them forward. The overall feeling is "I had not finished that one and the next arrived", which keeps attention permanently switched on.  
**Used for and where it works best:** Trailers, reels, openings and any scene you want to run. In modern series it is what stops the viewer leaving the episode. If you cut after the answer has already arrived, you have lost the forward pull.  
**Best in:** formats: Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Commercial / TVC, Vertical Micro-Drama, Music Video, Meme / Comedy Edit, Product Video / Motion Design, Short Film | genres: Thriller / Suspense, Action, Crime / Procedural, Comedy, Mystery / Whodunit, Spy / Espionage, Heist, Political Thriller  
**Avoid when:** In emotional scenes cutting early kills the feeling before it lands. Grief and confession need the opposite: a late cut.  
**Prompt:** `editor: trim each shot so it ends a few frames before the viewer is satisfied, and let the next shot answer the unfinished thought`  
**Yields to:** `cut.late` — Grief and confession need the opposite, a late cut.  
`cut.preemptive`

### The Late Cut / Holding Past the Cut

**Also called:** holding the shot, delayed cut  
**What it is:** You stay in the shot after its job is finished: the event is over, the line has been said, and the camera is still on the face or on the empty room.  
**Effect on the audience:** The extra time creates discomfort or grief, because the viewer is left face to face with the consequence of what just happened.  
**Used for and where it works best:** After a death, after the news, after the character has left the frame, and in cringe comedy where the shot runs long until the silence becomes the joke. In slow drama, tragedy and reflective documentary, two extra seconds make the whole difference.  
**Best in:** formats: Feature Film, Limited Series, Short Film, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Sitcom / Multi-Cam Comedy, Experimental / Art Film | genres: Tragedy, Drama, Psychological / Arthouse, Dark Comedy / Satire, Melodrama, Heritage (civilisation-focused), Horror, Verite / Observational, Slice of Life  
**Avoid when:** With no meaning behind it you get dead slowness and the viewer leaves. In action and in reels it is suicide, where every extra frame costs you viewers.  
**Prompt:** `editor: hold the shot two to four seconds after the action ends, staying on the stillness until the discomfort registers, then cut`  
**Yields to:** `cut.preemptive` — Action and reels, where every extra frame costs.  
`cut.late`

### The Two Frame Trim

**Also called:** two frame cut, frame level trim  
**What it is:** Adjusting a cut by two or three frames forward or back. The same shots and the same angles, only the cut point has moved by a fraction of a second.  
**Effect on the audience:** Two frames turn a joke from funny to flat and a punch from painful to fake. This is the level at which a professional editor separates from an amateur.  
**Used for and where it works best:** Every important cut in the film deserves a test at two frames earlier, two frames later, and a comparison of all three. In comedy the timing is the joke itself, and in action two frames before impact is the difference between a hit you feel and a hit you see. In music video, two frames on the beat separate locked from nearly locked.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Commercial / TVC, Music Video, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Short Film, Meme / Comedy Edit | genres: Comedy, Action, Thriller / Suspense, Musical, Horror, Dark Comedy / Satire, Martial Arts / Wuxia, Rom-Com  
**Avoid when:** Do not burn hours on a cut that carries no weight in the scene. And frame accuracy will not save a cut that is in the wrong place to begin with: change the shot, not the two frames.  
**Prompt:** `editor: test the same cut two frames earlier and two frames later, then keep the version that changes the feeling, not the one that looks smoothest`  
`cut.two_frame`

### The Eye Trace Rule

**Also called:** eye trace, visual attention rule  
**What it is:** Before you cut, work out exactly where the viewer's eye is on the last frame of the outgoing shot, and decide where you want it on the first frame of the incoming one.  
**Effect on the audience:** If the eye stays where it was the cut smooths out and disappears. If it has to travel a long way you get a jolt, and that jolt is exactly what you use when you want a shock.  
**Used for and where it works best:** This is the governing rule above every other cutting rule: dialogue, action, anime, documentary. In complex action, a battle or a crowd, it is what keeps the scene readable. In vertical nine by sixteen it matters most of all, because the frame is narrow and the eye has nowhere to go.  
**Best in:** formats: all | genres: all  
**Avoid when:** Forget the eye and cut to a reversed composition and the viewer spends half a second hunting for the subject, and that half second is what ruins the scene. Equally, do not make every cut smooth; some moments need the jolt.  
**Prompt:** `editor: mark where the eye rests on the outgoing frame, place the new subject in that same area for a smooth cut or far from it for a shock`  
`cut.eye_trace`

### Screen Position Match

**Also called:** same position cut, centre framing cut  
**What it is:** The important element keeps the same place in frame before and after the cut: centre to centre, or right third to right third.  
**Effect on the audience:** The eye does not move a millimetre, so you can cut far faster without losing the viewer. This is what lets you cut every half second in a chase and still be understood.  
**Used for and where it works best:** Chases, battles, fast montage and music video. The working rule is to keep the point of interest centred across every shot of a fast sequence. In reels and vertical it is the only solution, because the viewer always looks at the centre of the screen.  
**Best in:** formats: Feature Film, Trailer / Teaser, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Commercial / TVC, Sports Broadcast / Sports Film, AI-Generated Clip | genres: Action, Thriller / Suspense, Martial Arts / Wuxia, War, Adventure, Musical, Shonen Battle (anime), Sports Drama, Heist  
**Avoid when:** If every shot is dead centred in a quiet scene the compositions go flat and lifeless. This is a tool for speed, not for beauty.  
**Prompt:** `editor: keep the subject in the same screen position across every cut of the sequence so the eye never has to search`  
**Example:** Mad Max Fury Road, the action kept centred so the eye never leaves the middle of the frame.  
**Yields to:** `cut.eye_trace` — A quiet scene, where dead centring goes flat.  
`cut.screen_position`

### Screen Direction Match

**Also called:** directional continuity cut  
**What it is:** Whatever moves right in the first shot must keep moving right in the second, even if the place and the time have changed.  
**Effect on the audience:** Direction is the viewer's map. Keep it and they understand a chase or a journey with no map at all; break it and they feel the character has turned back the way they came.  
**Used for and where it works best:** Every journey, chase or two sided battle: our army moves right and theirs moves left, and the viewer is never lost. In heritage and war work it is the most important rule of a march scene. With AI generated video, write the direction of travel into every clip so it does not flip between shots.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Heritage / Historical Documentary, Docudrama / Reenactment, Trailer / Teaser, AI-Generated Clip, Sports Broadcast / Sports Film | genres: War, Action, Adventure, Historical / Biopic, Heritage (civilisation-focused), Western, Fantasy / Epic, Thriller / Suspense, Shonen Battle (anime)  
**Avoid when:** If the direction flips for no reason the viewer feels lost and blames himself rather than the film. If you want the flip on purpose, for a retreat, a defeat or disorientation, signal it with a neutral shot or a visible turn.  
**Prompt:** `editor: keep every moving subject travelling in the same screen direction across the sequence, and mark any reversal with a neutral head on shot`  
**Yields to:** `cut.neutral` — When the direction must reverse on purpose.  
`cut.screen_direction`

### Line Preserving Cut / The 180 Line

**Also called:** axis of action, the line  
**What it is:** You imagine a line between the two characters or along the path of movement and keep every camera angle on one side of it, so each person stays on the same side of the screen.  
**Effect on the audience:** The space stays legible: he is on the right, she is on the left, and they are looking at each other. This is the basis of belief in any dialogue scene.  
**Used for and where it works best:** Every dialogue, confrontation or match. Plan the line before you shoot: where the master sits, where the reverse sits, and where the line moves when a third person enters. In series, sitcom and sports it is the rule that keeps fast work clean.  
**Best in:** formats: Drama Series Episode, Sitcom / Multi-Cam Comedy, Soap Opera / Telenovela, Feature Film, Sports Broadcast / Sports Film, Short Film, Anime (Japanese 2D), 3D CG Animation, Interview / Video Podcast, AI-Generated Clip | genres: Drama, Comedy, Romance, Crime / Procedural, Legal Drama, Melodrama, Sports Drama, Medical Drama, Action  
**Avoid when:** When you want disorientation or madness, strict obedience to the line keeps the scene too polite. And in field documentary the line is worth less than the moment, because losing the event while you work out which side to stand on costs you the only take there is.  
**Prompt:** `editor: keep every angle on one side of the imaginary line between the two subjects so their screen positions and eyelines stay consistent`  
**Yields to:** `cut.cross_line` — When disorientation or madness is the point.  
`cut.keep_180`

### Deliberate Line Crossing Cut

**Also called:** crossing the axis, breaking the line  
**What it is:** You deliberately cut to an angle on the other side of the line, so the two characters swap screen positions and suddenly look as if they are not facing each other.  
**Effect on the audience:** A subconscious disturbance: the viewer cannot name what happened but feels something has broken, in the relationship or in the mind.  
**Used for and where it works best:** The beat of betrayal, of the lie, of psychological collapse, or the moment a character's real face appears. In psychological horror and thriller it is a silent tool that needs no music. Use it once or twice in an entire film, on a specific moment, so it reads as a statement and not as a mistake.  
**Best in:** formats: Feature Film, Limited Series, Short Film, Drama Series Episode, Anime (Japanese 2D), Experimental / Art Film, AI-Generated Clip, Trailer / Teaser | genres: Psychological Horror, Thriller / Suspense, Drama, Horror, Mystery / Whodunit, Noir / Neo-Noir, Psychological / Arthouse, Crime / Procedural, Surreal / Absurdist  
**Avoid when:** Done without a reason it is simply a coverage error, not a style. And broken inside complex action it usually costs the viewer the geography; the exception is when losing that orientation is the experience you are after.  
**Prompt:** `editor: cut to a reverse angle from the wrong side of the line so the characters swap screen sides at the exact moment the trust breaks`  
**Yields to:** `cut.neutral` — Crossing for coverage rather than as a statement.  
`cut.cross_line`

### The Neutral Shot

**Also called:** neutral cutaway, head on shot  
**What it is:** A head on shot with no left or right direction, a face straight to camera or a walk toward the lens, placed between two shots so you can cross the line without a jolt.  
**Effect on the audience:** It resets the eye's memory of direction, so any angle after it is accepted. It is the engineering solution to the line problem.  
**Used for and where it works best:** When you need to move coverage to the other side in a long scene, or when an actor's direction has to reverse inside a chase. In sports and documentary it is the safety net when your cameras are not all on one side. Always shoot one on location even if you do not plan to use it.  
**Best in:** formats: Feature Film, Drama Series Episode, Sports Broadcast / Sports Film, Documentary Feature, Documentary Series, News Report / Reportage, Short Film, 3D CG Animation, Game Cinematic / Gameplay | genres: Action, Drama, Sports Drama, War, Adventure, Thriller / Suspense, Verite / Observational, Crime / Procedural  
**Avoid when:** Used without need it is a dead shot that stalls the rhythm. And it fails if it is too short, the eye needs close to a second to reset its sense of direction.  
**Prompt:** `editor: insert a head on neutral shot with no screen direction, hold it about one second, then cut to the angle on the other side of the line`  
**Yields to:** `cut.cross_line` — When the disturbance of crossing is the point.  
`cut.neutral`

### Cheat Cut

**Also called:** cheating the cut, cheated continuity  
**What it is:** You accept a small continuity break on purpose in exchange for a better frame: a hand in a different place, a glass at a different level, the two characters closer together in the tight shot than in the wide.  
**Effect on the audience:** The viewer does not notice, because the eye tracks emotion rather than measurements. The better composition works on them far more than the accuracy does.  
**Used for and where it works best:** Intimate dialogue, where you bring the two faces closer in the tight shot than they really were, food and product shots, and scenes shot on different days. It is daily practice in series and advertising. The rule is simple: the cheat is allowed whenever the emotion wins.  
**Best in:** formats: Drama Series Episode, Soap Opera / Telenovela, Sitcom / Multi-Cam Comedy, Feature Film, Commercial / TVC, Product Video / Motion Design, Short Film, Vertical Micro-Drama, Kids Content | genres: Drama, Romance, Melodrama, Comedy, Rom-Com, Family, Crime / Procedural, Medical Drama  
**Avoid when:** Cheating anything that carries story information, a weapon, a wound, a watch, the presence of a person, usually breaks the scene, because the audience is tracking exactly those things; the exception is an object the story has already finished with. And viewers do notice objects that appear to move on their own, even when they miss distances.  
**Prompt:** `editor: accept the small mismatch and keep the stronger frame, as long as nothing that carries story information has changed`  
**Yields to:** `cut.match_action` — The mismatched element carries story information.  
`cut.cheat`

### Clearing Frame Cut

**Also called:** clean exit and entrance, clear frame edit  
**What it is:** You let the character leave the frame completely before you cut, and the new shot starts empty and then she walks into it.  
**Effect on the audience:** It gives a feeling of real distance and real time: something travelled between the exit and the entrance. It is a classical, calm and dignified rhythm.  
**Used for and where it works best:** Westerns, epics, heritage films and contemplative work. Use it when you want the location to breathe and the viewer to feel the size of the distance the character crossed. In heritage documentary it also gives you a beat to see the architecture before a human enters it.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Short Film, Documentary Feature, Drama Series Episode, Travel / Real Estate / Hospitality, Experimental / Art Film, 3D CG Animation, AI-Generated Clip | genres: Western, Historical / Biopic, Heritage (civilisation-focused), Drama, Mythology / Ancient Epic, Road Movie, Adventure, Tragedy, Faith / Biblical Epic  
**Avoid when:** In fast rhythms and reels this is fatal: two seconds of empty frame means a viewer gone. Contemporary style prefers cutting while the character is still in frame.  
**Prompt:** `editor: hold until the subject fully exits frame, cut to an empty frame of the next location, and let them enter it after a beat`  
**Yields to:** `cut.elliptical` — Fast rhythms and reels; cut before they exit.  
`cut.clear_frame`

### Double Cut / Two Angle Punch

**Also called:** double punch-in, two angle hit  
**What it is:** The same instant is shown twice in a row from two clearly different angles, or the same subject is hit with two quick cuts at two different sizes.  
**Effect on the audience:** The hit doubles. The viewer receives the same information twice within half a second, so it registers much harder.  
**Used for and where it works best:** The impact, the reveal or the hero's entrance in action, anime and trailers. In advertising the product is struck with two consecutive cuts right before the logo. In music video it sits naturally across two consecutive beats.  
**Best in:** formats: Trailer / Teaser, Anime (Japanese 2D), Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Game Cinematic / Gameplay, 3D CG Animation, Product Video / Motion Design, AI-Generated Clip | genres: Action, Shonen Battle (anime), Martial Arts / Wuxia, Superhero, Thriller / Suspense, Musical, War, Adventure  
**Avoid when:** If the two angles are close it reads as a dirty jump instead of a punch. And do not use it in quiet drama, it makes the scene look like a commercial.  
**Prompt:** `editor: show the same instant twice from two clearly different angles, each held under half a second, then continue the scene`  
`cut.double_angle`

### The Double Take Cut

**Also called:** double take edit  
**What it is:** Three cuts: the character glances with no interest, cut to the thing, cut back as she snaps around having understood.  
**Effect on the audience:** The timing is the joke, or the horror. The gap between the first look and the second is what makes it funny or frightening.  
**Used for and where it works best:** Almost all comedy, and horror beats where something is wrong in the background. Keep the shot of the thing short and make the return to the character the longest beat. It is excellent in sitcom, reels and cartoons.  
**Best in:** formats: Sitcom / Multi-Cam Comedy, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, 2D Animation (Western / Cartoon), Kids Content, Feature Film, Drama Series Episode, Commercial / TVC, Anime (Japanese 2D) | genres: Comedy, Dark Comedy / Satire, Rom-Com, Family, Horror, Fairy Tale, Slice of Life, Preschool / Early Learning  
**Avoid when:** If the character reacts on the first look the device is dead. And do not use it in serious drama, it plays as broad and naive.  
**Prompt:** `editor: cut from the disinterested glance to the object for half a second, then back to the character as she snaps around and sees it properly`  
**Yields to:** `cut.reaction_first` — Serious drama, where the comic snap-back plays naive.  
`cut.double_take`

### Cut on Impact

**Also called:** impact cut, contact cut  
**What it is:** You cut on the exact frame where the punch, the bullet or the car arrives, so half the blow lives in one shot and half in the next.  
**Effect on the audience:** The brain assembles the blow itself and feels it harder than any hit shown in full. It is what makes a punch that never landed look painful.  
**Used for and where it works best:** Every fight or crash: the shot of the hand starting to move, the cut on the frame of contact, the cut to the reaction. In martial arts and anime it is the core equation. With AI generated clips it is the answer, because the model never has to render the complete blow.  
**Best in:** formats: Feature Film, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Trailer / Teaser, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, AI-Generated Clip, Short Film | genres: Action, Martial Arts / Wuxia, Shonen Battle (anime), Superhero, War, Thriller / Suspense, Samurai / Chanbara, Sports Drama, Monster / Kaiju  
**Avoid when:** Cut two frames after contact and the blow instantly looks fake. And too many cuts in a fight leave the viewer with no idea who is winning.  
**Prompt:** `editor: cut on the exact frame of contact, then cut again to the reaction, never showing the full blow in one continuous shot`  
`cut.on_impact`

### Cut on the Door Slam

**Also called:** cut on the bang, percussive cut  
**What it is:** You place the cut on the same frame where a door closes, an object strikes or a case snaps shut, so the sonic hit covers the cut.  
**Effect on the audience:** The hit becomes punctuation, a full stop at the end of a sentence. The viewer feels the scene ended by decision rather than by fading out.  
**Used for and where it works best:** The end of any scene with an angry exit or a decision: the door slams and you cut. In drama, crime and thriller work it is a clean exit from a heavy scene. In advertising: the lid snaps shut, then the logo.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Commercial / TVC, Short Film, Sitcom / Multi-Cam Comedy, Anime (Japanese 2D), Music Video, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, Crime / Procedural, Thriller / Suspense, Comedy, Dark Comedy / Satire, Action, Melodrama, Noir / Neo-Noir  
**Avoid when:** As a habit at the end of every scene it shows that the film needs a bang to finish anything. And do not use it on a sad beat, the hit erases the emotional residue.  
**Prompt:** `editor: land the cut on the exact frame of the slam so the sound hit and the picture change happen together`  
**Yields to:** `cut.late` — A sad beat, whose residue the hit erases.  
`cut.on_slam`

### Cut on the Flash

**Also called:** lightning cut, muzzle flash cut  
**What it is:** You use a flash that already exists in the scene, lightning, a camera flash, a gunshot, a welder, a police light, and place the cut on the frame of that flash.  
**Effect on the audience:** The viewer's eye is blinded for a fraction of a second and never registers the cut, which gives you a transition that is violent and clean at once.  
**Used for and where it works best:** Storm and horror scenes, red carpets with press flashes, night battles. In music video it is a free transition on the drum hit. With generated clips, ask for a lightning flash in the last second of the first clip and the first second of the second.  
**Best in:** formats: Music Video, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Anime (Japanese 2D), Commercial / TVC, Short Film, AI-Generated Clip, Game Cinematic / Gameplay | genres: Horror, Thriller / Suspense, Action, Crime / Procedural, Noir / Neo-Noir, Musical, War, Supernatural Horror, Gothic / Vampire  
**Avoid when:** With no logical source for the flash in the scene it becomes a cheap added effect. And once the flash repeats — a storm sequence, a press line, a night firefight — it stops being an edit decision and becomes a photosensitivity one: `safety.photosensitive_flash`.  
**Prompt:** `editor: place the cut inside the brightest frame of the practical flash so the blink of light hides the change of shot`  
**Yields to:** `safety.photosensitive_flash` — Once the flash repeats; yields to tier 0.  
`cut.on_flash`

### Cut Inside a Whip Pan

**Also called:** whip cut, blurred pan cut  
**What it is:** The camera whips fast until the image is nothing but streaks, the cut lands on the most blurred frame, and the new shot starts moving in the same direction and settles.  
**Effect on the audience:** Continuous energy and motion between two places. The viewer feels the camera travelled rather than that you cut.  
**Used for and where it works best:** Fast comedy, advertising, music video and reels, and the signature style of Edgar Wright and Wes Anderson. With AI video: ask for a very fast horizontal camera move at the end of the first clip and at the head of the second, same direction and same speed.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Feature Film, Meme / Comedy Edit, Trailer / Teaser, Vlog / YouTube Long-Form, Anime (Japanese 2D), AI-Generated Clip, Product Video / Motion Design | genres: Comedy, Action, Rom-Com, Musical, Dark Comedy / Satire, Adventure, Spy / Espionage, Heist  
**Avoid when:** If the direction reverses between the two shots the transition breaks and reads as an error. In serious drama and heritage documentary it plays as juvenile.  
**Prompt:** `editor: cut on the most blurred frame of the whip and start the next shot already whipping in the same direction before it settles`  
**Example:** Citizen Kane, the breakfast table montage bridged by swish pans.  
**Yields to:** `cut.motion_match` — Serious drama and heritage, where the blur plays juvenile.  
`cut.in_whip`

### Cut on Sound

**Also called:** sound motivated cut, hard effect cut  
**What it is:** The sound decides where the cut goes: a shot, a slam, a bell, a glass hitting a table, a scream. The picture changes on the same frame as the sound.  
**Effect on the audience:** The ear is faster than the eye, so when they land together the viewer feels the cut is correct without knowing why.  
**Used for and where it works best:** Any scene with a sharp sound: action, a kitchen in a commercial, a craftsman's workshop in documentary, a chisel on stone in heritage work. When you do not know where to cut, play the audio alone and listen for where you want the picture to change. It is the backbone of trailers, reels and music video.  
**Best in:** formats: Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Feature Film, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Anime (Japanese 2D), Product Video / Motion Design | genres: Action, Thriller / Suspense, Crime / Procedural, Musical, Heritage (civilisation-focused), Horror, War, Science / Educational, Martial Arts / Wuxia  
**Avoid when:** If every cut in the film sits on a sound the edit becomes mechanical and loses its dramatic breathing. In emotional dialogue the sound does not decide, the face does.  
**Prompt:** `editor: lay the audio first, mark the sharp transients, and place every picture cut on the frame of the hit`  
**Yields to:** `cut.on_blink` — Emotional dialogue, where the face decides, not sound.  
`cut.on_sound`

### Cut on the Word

**Also called:** cutting on the line, word timed cut  
**What it is:** You pick one specific word in the line and land the cut exactly on it: on the name, on the "no", on the word that turns the scene.  
**Effect on the audience:** The cut doubles the weight of that word and it feels as if the film is pointing at it.  
**Used for and where it works best:** Pivotal dialogue, documentary narration where the picture changes on the very word that names it, and lyric video on the key word of the hook. In heritage work the king's name lands in the narration and the picture changes on that syllable.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Documentary Series, Lyric Video, Music Video, Feature Film, Drama Series Episode, Video Essay, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Political Thriller, Musical, Crime / Procedural, Mystery / Whodunit, Science / Educational, Tragedy  
**Avoid when:** Cut on every important word and the narration starts driving the picture and the viewer tires. Sometimes a cut one or two frames before the word is stronger than landing on it exactly, so test both.  
**Prompt:** `editor: mark the exact frame of the key word in the waveform and place the picture change on that syllable`  
`cut.on_word`

### Rhythmic Cut / Beat Cut

**Also called:** cutting to the beat, music cut  
**What it is:** Every cut lands on a musical beat: every four beats, every two, or every single beat in the fastest sections.  
**Effect on the audience:** The viewer feels physical pleasure because the picture breathes on the same pulse as the music. The body nods before the mind thinks.  
**Used for and where it works best:** Music video, reels, advertising and montage inside a feature. The method is to mark the beats before you pull a single shot and build a grid from them. The strongest move is to break that grid once, on an important moment, so the viewer looks up.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Trailer / Teaser, Dance Film, Lyric Video, Meme / Comedy Edit, Product Video / Motion Design, Concert / Live Event, Title Sequence / Opening Credits | genres: Musical, Action, Comedy, Sports Drama, Romance, Adventure, Fantasy / Epic, Heritage (civilisation-focused)  
**Avoid when:** Cutting on every beat from start to finish tires the eye and destroys any escalation. And in a dialogue scene the music does not lead, the speech does.  
**Prompt:** `editor: mark the beat grid first, cut on every fourth beat in the verse and every beat in the chorus, breaking the grid once on the key moment`  
**Example:** Baby Driver, the whole film cut to the music tracks.  
**Yields to:** `cut.on_word` — A dialogue scene, where speech leads not music; and `kids.no_fast_cuts` — children's content, where the 1.5-second floor outranks the beat.  
`cut.rhythmic`

### Cut on the Beat Drop

**Also called:** the drop cut  
**What it is:** One big cut placed exactly on the moment the main beat enters the track, after a build or a silence.  
**Effect on the audience:** An explosion of energy. Everything before it becomes preparation, and the shot that lands on it burns into the viewer's memory.  
**Used for and where it works best:** The peak of a music video, the end of a trailer, the hook of a reel. Save your single strongest shot for this exact moment and never spend it earlier. In advertising this is where the product or the logo lands.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Commercial / TVC, Dance Film, Concert / Live Event, Lyric Video, Product Video / Motion Design, Meme / Comedy Edit | genres: Musical, Action, Superhero, Adventure, Sports Drama, Fantasy / Epic, Comedy, Heist  
**Avoid when:** If the shot on the drop is ordinary the audience feels a bigger let down than if you had done nothing. And do not repeat the trick more than twice in one piece.  
**Prompt:** `editor: hold the build with minimal cutting, then land your strongest shot on the exact frame of the drop`  
`cut.beat_drop`

### Accelerating Cut Rhythm

**Also called:** cutting every N frames, compression of shot length  
**What it is:** You shorten every shot progressively: six seconds, three, a second and a half, half a second, twelve frames, six frames.  
**Effect on the audience:** The viewer's pulse climbs with the rhythm, because the body responds to acceleration involuntarily. It is the cheapest way to build a climax.  
**Used for and where it works best:** The climax, the chase, the battle, the training montage and the last third of a trailer. Combine it with cross cutting so the two story lines converge at the same rate as the shot lengths. In reels an acceleration in the last ten seconds stops the viewer swiping away.  
**Best in:** formats: Trailer / Teaser, Feature Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Game Cinematic / Gameplay, Sports Broadcast / Sports Film, Commercial / TVC, 3D CG Animation, Short Film | genres: Action, Thriller / Suspense, War, Sports Drama, Heist, Horror, Martial Arts / Wuxia, Adventure, Shonen Battle (anime), Disaster  
**Avoid when:** If you start short you have nowhere left to climb, so keep the opening long and patient. And after the climax you must lengthen again, otherwise the viewer never feels the difference.  
**Prompt:** `editor: halve the length of every shot as the sequence climbs, ending on cuts of six to twelve frames at the peak`  
`cut.accelerate`

### Long Hold Then Burst

**Also called:** stillness then rapid cuts, hold and burst  
**What it is:** One very long still shot with no cut, five to twenty seconds, and then immediately five or ten cuts inside less than two seconds.  
**Effect on the audience:** Contrast is the weapon. The stillness builds pressure and the burst releases it all at once, so the hit feels far stronger than continuous fast cutting ever could.  
**Used for and where it works best:** Horror, anime and art film, and the moment rage breaks in drama. In anime it is a known signature: a long motionless shot on a face, then an explosion of movement. In heritage work: a long stillness on the temple, then a burst of carved details.  
**Best in:** formats: Anime (Japanese 2D), Feature Film, Short Film, Experimental / Art Film, Heritage / Historical Documentary, Music Video, Drama Series Episode, Trailer / Teaser, AI-Generated Clip | genres: Horror, Psychological Horror, Drama, Shonen Battle (anime), Mecha (anime), Seinen (mature anime), Tragedy, War, Surreal / Absurdist, Heritage (civilisation-focused)  
**Avoid when:** If the stillness carries no tension it becomes boredom and the viewer leaves before the burst. And avoid it in reels unless the still shot itself contains a visual hook.  
**Prompt:** `editor: hold one motionless shot far longer than comfortable, then cut five to ten times inside two seconds`  
`cut.hold_then_fast`

### Accelerating Shot Reverse Shot

**Also called:** tightening shot reverse shot, showdown rhythm  
**What it is:** The exchange between two faces gets shorter and tighter with every round: wide and long, then medium and shorter, then very tight and only a few frames, sometimes ending on the eye.  
**Effect on the audience:** Tension accumulates geometrically with no music and no dialogue. The viewer knows the decision is coming because the rhythm itself says so.  
**Used for and where it works best:** The standoff, the duel, the moment before the shot, the interrogation. It is the confrontation equation of the western, the samurai film and battle anime. In debates and legal drama it works the same way with words.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), Short Film, Game Cinematic / Gameplay, Trailer / Teaser, 3D CG Animation, Limited Series, AI-Generated Clip | genres: Western, Samurai / Chanbara, Thriller / Suspense, Action, Martial Arts / Wuxia, Crime / Procedural, Legal Drama, Shonen Battle (anime), Noir / Neo-Noir, Drama  
**Avoid when:** If you start on tight sizes you have nothing left to escalate to. And do not stretch the acceleration past its need; it must end in a decision or it turns comic.  
**Prompt:** `editor: shorten and tighten each exchange between the two faces, ending on a few frames of the eye before the action breaks`  
**Example:** The Good the Bad and the Ugly, the three way standoff in the cemetery.  
`cut.srs_accel`

### Subliminal Frame / Flash Cut

**Also called:** single frame insert, subliminal insert  
**What it is:** An image inserted for one to three frames inside a normal shot: a face, a memory, a symbol, something horrible. Fast enough that the viewer is not sure they saw it.  
**Effect on the audience:** It plants a feeling without clear information. The viewer is disturbed and senses something hidden, which is exactly the point.  
**Used for and where it works best:** Psychological horror, broken memory, addiction, mental collapse and trailers. Increase the length gradually across the film until the flash finally becomes a full scene at the end. It is excellent in music video and experimental work.  
**Best in:** formats: Feature Film, Trailer / Teaser, Music Video, Experimental / Art Film, Short Film, Drama Series Episode, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Psychological Horror, Horror, Thriller / Suspense, Psychological / Arthouse, Surreal / Absurdist, Mystery / Whodunit, Supernatural Horror, Cyberpunk  
**Avoid when:** With no story behind it, it is an empty trick. And it is usually the wrong carrier for information the audience must have, because they will not catch it consciously; the exception is information you want them to feel now and understand only on a second viewing.  
**Prompt:** `editor: insert a one to three frame image inside the shot, too fast to read, and repeat it longer each time it returns`  
**Example:** Fight Club, the single frames of Tyler Durden before he appears in the story.  
**Yields to:** `cut.insert` — When the audience must actually receive the information.  
`cut.subliminal`

### Flash Frame

**Also called:** white frame, blank frame punctuation  
**What it is:** One or two white or blown out frames placed exactly on the cut. It began as a camera artefact in the film era and became a deliberate device.  
**Effect on the audience:** A small optical hit that says "look". It separates the two shots and adds a charge of electricity and mild violence.  
**Used for and where it works best:** Trailers, music video and sports advertising, and the shock or memory beat in drama. It is cleaner than a ramped flash because it is a single frame and never slows the rhythm. In reels it punctuates between segments with no heavy effect.  
**Best in:** formats: Trailer / Teaser, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, Feature Film, Title Sequence / Opening Credits, Meme / Comedy Edit, Title Sequence / Opening Credits, AI-Generated Clip | genres: Action, Thriller / Suspense, Musical, Sports Drama, Horror, Psychological / Arthouse, Superhero, War  
**Avoid when:** Repeated on every cut it makes the piece look like a preset. In serious documentary and quiet drama it has no place. And the phrase this card used to end on — *punishes the eye* — was a harm named and then answered with taste: once white frames repeat, they are repeated flashing, and the rate and the stopping point are `safety.photosensitive_flash`, exactly as `cut.on_flash` already says.  
**Prompt:** `editor: place one or two pure white frames exactly on the cut point, no ramp and no glow, then continue at normal exposure`  
**Yields to:** `cut.to_black` — Serious documentary and quiet drama; punctuate with black.  
`cut.flash_frame`

### Cut to Black

**Also called:** hard cut to black  
**What it is:** A sudden cut from picture to complete black with no ramp, sometimes taking the sound with it and sometimes letting the sound continue.  
**Effect on the audience:** It stops the film by force. With the sound cut too it reads as death or shock; with the sound continuing it turns to dread, because the viewer can hear but cannot see.  
**Used for and where it works best:** The end of an episode or a film on an open question, the moment of death, the loss of consciousness. In horror, cut to black and leave the breathing or the knocking running. In trailers, short blacks between blocks let every block land on its own.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Trailer / Teaser, Short Film, Anime (Japanese 2D), Title Sequence / Opening Credits, Title Sequence / Opening Credits, Vertical Micro-Drama | genres: Thriller / Suspense, Drama, Horror, Crime / Procedural, Tragedy, Psychological Horror, Mystery / Whodunit, War, Gangster  
**Avoid when:** Used at the end of every scene it loses all its weight; it is a full stop, not a comma. And in vertical content a long black simply means the viewer is gone.  
**Prompt:** `editor: hard cut from the last frame straight to full black, and decide deliberately whether the sound cuts with it or keeps running`  
**Example:** The Sopranos, the final cut to black with the sound gone.  
**Yields to:** `cut.flash_frame` — Vertical, where a long black loses the viewer.  
`cut.to_black`

### Cut to White

**Also called:** hard cut to white, white out  
**What it is:** A sudden cut to a fully white screen, usually with a sound hit or with total silence.  
**Effect on the audience:** The opposite of black: black is absence, white is excess. It reads as an explosion, a blackout, a birth, a revelation or a spiritual crossing.  
**Used for and where it works best:** The blast or the electric shock, the entry into a flashback, and the hopeful or shocking ending. In advertising and product work it is a clean doorway into a logo on white. In heritage and faith work it carries the crossing from darkness into light at the moment of a vision.  
**Best in:** formats: Feature Film, Commercial / TVC, Product Video / Motion Design, Trailer / Teaser, Music Video, Short Film, Anime (Japanese 2D), Drama Series Episode, Title Sequence / Opening Credits, AI-Generated Clip | genres: Sci-Fi, Fantasy / Epic, Faith / Biblical Epic, Drama, Horror, Psychological / Arthouse, Mythology / Ancient Epic, Supernatural Horror, Melodrama  
**Avoid when:** Full white is punishing on modern screens if it lasts more than a moment. And avoid it on sad endings, it delivers deliverance rather than loss.  
**Prompt:** `editor: hard cut to pure white for a few frames with a single sound hit, then open on the new scene already running`  
**Yields to:** `cut.to_black` — A sad ending, where loss not deliverance.  
`cut.to_white`

### Hard Cut to Silence

**Also called:** silent cut, audio drop cut  
**What it is:** Picture and sound change on the same frame: you cut to the new shot and all audio disappears while the picture keeps running.  
**Effect on the audience:** A sensory shock. The ear registers the vacuum instantly and reads it as danger, or as a moment standing outside time.  
**Used for and where it works best:** The inner explosion, the deafness after the blast, the delayed realisation, the entry to a dream. In war, horror and psychological drama it is the strongest free tension tool you have. In reels it works as a hook, because sudden silence makes the viewer turn the volume up.  
**Best in:** formats: Feature Film, Short Film, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Anime (Japanese 2D), Music Video, AI-Generated Clip, Experimental / Art Film | genres: War, Horror, Psychological Horror, Thriller / Suspense, Drama, Tragedy, Sci-Fi, Psychological / Arthouse, Supernatural Horror  
**Avoid when:** If the silence runs beyond three or four seconds the viewer suspects the file is broken. It also differs from the pre-cut silence, where the sound drops before the cut; here it drops exactly with it.  
**Prompt:** `editor: cut picture and audio on the same frame into complete silence, keep the picture moving, and hold the silence under three seconds`  
**Yields to:** `sound.silence_before` — When the silence must arrive before the cut.  
`cut.to_silence`

### Cut Wide for the Joke

**Also called:** comedy wide, the reveal wide  
**What it is:** Instead of staying tight on the face you cut wide and reveal the whole situation: the character alone in a ridiculous place, or the disaster at its full scale.  
**Effect on the audience:** Comedy lives in distance. Seeing the character small inside the mess he made is funnier than any close up could be.  
**Used for and where it works best:** The punchline of a comic scene, the end of an embarrassing situation, the reveal of how big the disaster really is. The rule is simple: tight for tension, wide for laughs. It is excellent in sitcom, reels, cartoons and dark comedy.  
**Best in:** formats: Sitcom / Multi-Cam Comedy, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, 2D Animation (Western / Cartoon), Feature Film, Drama Series Episode, Short Film, Commercial / TVC, Kids Content, Vlog / YouTube Long-Form | genres: Comedy, Dark Comedy / Satire, Rom-Com, Family, Slice of Life, Surreal / Absurdist, Fairy Tale, Preschool / Early Learning  
**Avoid when:** Reveal the wide too early and you burn the joke before its time. And a wide in an emotional scene chills the feeling instead of raising a laugh.  
**Prompt:** `editor: hold the tight shot through the setup, then cut wide on the punchline to reveal the full situation at once`  
**Yields to:** `cut.tighten` — An emotional scene, where the wide chills it.  
`cut.wide_joke`

### Cut Tight for the Fear

**Also called:** claustrophobic cut, tight coverage  
**What it is:** The more the danger grows the tighter the sizes get: medium to close to extreme close, and you remove the wide from the scene entirely.  
**Effect on the audience:** The viewer loses the geography and therefore loses safety. He no longer knows where the thing will come from, which is exactly what fear is.  
**Used for and where it works best:** Horror, suspense, and the beat of being cornered, suffocated or interrogated. The working rule is never to give the viewer a reassuring wide before the climax. In vertical micro drama it is the default, because the frame is narrow to begin with.  
**Best in:** formats: Feature Film, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Short Film, Anime (Japanese 2D), Game Cinematic / Gameplay, AI-Generated Clip, Trailer / Teaser | genres: Horror, Thriller / Suspense, Psychological Horror, Slasher, Survival, Crime / Procedural, Supernatural Horror, Mystery / Whodunit, Body Horror  
**Avoid when:** Tighten from the first shot and you have nowhere to escalate and no contrast left. And in an action scene that needs geography, tightness turns it into unreadable chaos.  
**Prompt:** `editor: remove every wide from the sequence and step the sizes tighter with each cut until only faces and details remain`  
**Yields to:** `size.reestablishing` — An action scene that still needs its geography.  
`cut.tight_fear`

### Screen Insert Cut

**Also called:** phone screen cut, device insert  
**What it is:** A short cut to a phone, a laptop or a message, either shot practically or composited, so the viewer reads the information for himself.  
**Effect on the audience:** It delivers written information fast and creates tension, because text reads quicker than dialogue and because a caller's name alone can turn a whole scene.  
**Used for and where it works best:** Modern drama, crime and thriller, and vertical micro drama where half the story happens inside a phone. Keep the text large, short and on screen for at least three seconds. In vertical, place it in the upper third so the platform interface does not cover it.  
**Best in:** formats: Drama Series Episode, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Short Film, Soap Opera / Telenovela, Commercial / TVC, Video Essay, Explainer | genres: Crime / Procedural, Thriller / Suspense, Drama, Romance, Mystery / Whodunit, Comedy, Coming of Age, Horror, Political Thriller  
**Avoid when:** If the text is long or small the viewer cannot read it and gets frustrated. And do not cut to the screen if the actor can deliver the same information with a look.  
**Prompt:** `editor: cut to a legible screen insert with short large text, hold three seconds, then cut back to the reaction`  
**Yields to:** `cut.reaction` — When a look can carry the same information.  
`cut.screen_insert`

### Reaction Before the Reveal

**Also called:** reaction first cut, delayed reveal cut  
**What it is:** You reverse the natural order: you show the terrified or stunned face first, and only one or two seconds later you cut to what caused it.  
**Effect on the audience:** The gap between the expression and its cause is what makes the tension. The viewer's mind builds possibilities worse than the truth before you reveal it.  
**Used for and where it works best:** Horror and comedy run on exactly the same mechanism: a terrified face then the monster, or a stunned face then the silly thing. In suspense it lets you delay the reveal without losing attention. With generated clips it also saves you money, because a face is cheaper than a creature.  
**Best in:** formats: Feature Film, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Anime (Japanese 2D), Trailer / Teaser, AI-Generated Clip, Sitcom / Multi-Cam Comedy, Meme / Comedy Edit | genres: Horror, Comedy, Thriller / Suspense, Dark Comedy / Satire, Supernatural Horror, Mystery / Whodunit, Slasher, Family  
**Avoid when:** Delay it too long and the viewer tires and guesses the answer before you. And in scenes where the event matters more than the reaction, reversing the order only weakens it.  
**Prompt:** `editor: open on the reaction face, hold one to two seconds of unexplained fear, then cut to the cause`  
**Yields to:** `cut.reaction` — When the event matters more than the reaction.  
`cut.reaction_first`

### Progressive Tightening

**Also called:** escalating coverage, sizes stepping in  
**What it is:** With every round of the dialogue the size is closer than the last: medium wide, medium, medium close, close, extreme close.  
**Effect on the audience:** The viewer never notices the steps but feels the scene closing in. The escalation is felt in the body before it is understood in the mind.  
**Used for and where it works best:** Any dialogue that escalates: a confession, an argument, an interrogation, a negotiation. Shoot at least three sizes of coverage on each character so you have a ladder to climb. It is the foundation of television drama, legal and medical work.  
**Best in:** formats: Drama Series Episode, Feature Film, Limited Series, Soap Opera / Telenovela, Short Film, Vertical Micro-Drama, Anime (Japanese 2D), AI-Generated Clip, Interview / Video Podcast | genres: Drama, Crime / Procedural, Legal Drama, Medical Drama, Thriller / Suspense, Melodrama, Political Thriller, Romance, Tragedy  
**Avoid when:** Return to a wide in the middle of the climb without a reason and the ladder breaks and the tension drops. And if you reach the extreme close too early there is nothing beyond it.  
**Prompt:** `editor: step the shot size closer with every exchange and never return to a wider size until the scene resolves`  
`cut.tighten`

### The Withheld Cut

**Also called:** refusing to cut, holding the take  
**What it is:** An editorial decision not to cut: you stay in one shot even though the coverage exists and the rhythm is asking for a change.  
**Effect on the audience:** Pressure builds because the viewer is denied the relief a cut provides. The longer you withhold, the more the next cut costs and the harder it lands.  
**Used for and where it works best:** Threat, confession, dance, birth and breakdown scenes. In horror, refuse to cut while the background is visible and let the viewer search it alone. In documentary, let the witness finish uncut so the audience feels nothing was manipulated.  
**Best in:** formats: Feature Film, Limited Series, Documentary Feature, Short Film, Drama Series Episode, Experimental / Art Film, Heritage / Historical Documentary, Interview / Video Podcast, Dance Film | genres: Thriller / Suspense, Horror, Drama, Tragedy, Psychological / Arthouse, Verite / Observational, True Crime, War, Psychological Horror  
**Avoid when:** If the shot carries no tension of its own, withholding is pure boredom. And it has to be a decision, not laziness: if the coverage was never shot, this is not a style.  
**Prompt:** `editor: refuse the obvious cut and hold the single shot through the whole beat, then cut only when the tension breaks`  
`cut.withheld`

### Cut to Reveal Scale

**Also called:** tight to extreme wide cut, scale reveal  
**What it is:** A direct cut from an extreme detail to an extreme wide that reveals the scale of the place, the crowd or the structure.  
**Effect on the audience:** The jump in scale shocks the eye and delivers awe and helplessness. The viewer feels the world is far larger than the character.  
**Used for and where it works best:** Epic and heritage work: a hand laying one brick, cut, the entire ziggurat. Or one soldier's face, cut, the whole army. In trailers it is the reveal beat of the second third. With generated clips it works perfectly, because each shot is created on its own with no continuity to maintain.  
**Best in:** formats: Heritage / Historical Documentary, Feature Film, Trailer / Teaser, Documentary Feature, 3D CG Animation, AI-Generated Clip, Travel / Real Estate / Hospitality, Anime (Japanese 2D), Game Cinematic / Gameplay, Music Video | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, War, Fantasy / Epic, Adventure, Faith / Biblical Epic, Disaster, Sci-Fi  
**Avoid when:** If the wide is not genuinely impressive the reveal fails and becomes a meaningless cut. And do not repeat it often, awe is consumed fast.  
**Prompt:** `editor: cut straight from an extreme close detail to an extreme wide of the full structure, with no intermediate size between them`  
`cut.scale_reveal`

### The Substitution Cut / The Stop Trick

**Also called:** stop trick, substitution splice, in camera vanish  
**What it is:** Stopping the camera with the framing and the light untouched, changing or removing something inside the scene, then resuming and joining the two pieces. The result is an instant vanish, appearance or transformation in a single frame.  
**Effect on the audience:** The magic happens in front of a steady eye that does not lie, so the viewer believes it more than any smooth effect. The simplicity itself is where the delight comes from.  
**Used for and where it works best:** Visual comedy, kids content and fairy tale work, and product commercials where one thing becomes another. It is a staple of reels and short form: the same frame, one step out of shot, and the wardrobe or the background has changed. In generated clips you ask for a matching first and last frame that differ only in the element that changes.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Commercial / TVC, Product Video / Motion Design, Short Film, Comics / Webtoon / Photo Essay, Stop Motion, Meme / Comedy Edit, 2D Animation (Western / Cartoon), AI-Generated Clip | genres: Comedy, Fairy Tale, Family, Fantasy / Epic, Physical Comedy / Slapstick, Preschool / Early Learning, Surreal / Absurdist, Magical Realism  
**Avoid when:** The join usually gives itself away through any change in the light or in the position of side objects, and then it reads as an edit mistake instead of a trick. The exception is when the mismatch is the joke, with something else in the background changing while nobody in the scene notices.  
**Prompt:** `locked camera, identical framing and light in both halves, the woman standing at the table then gone in the next frame with only the chair moved, in camera substitution, no dissolve`  
**Example:** Georges Melies built his trick films on this join from 1896 onward.  
**Yields to:** `trans.morph` — When light and side objects cannot stay identical.  
`cut.substitution`

### Texture Match Cut

**Also called:** surface match, material match cut  
**What it is:** A cut between two shots whose surface texture matches rather than their shape: grains of sand then grains of sugar, tree bark then the skin of a hand, cracked mud then a cracked wall. Scale, light and angle stay close across the join.  
**Effect on the audience:** The eye carries the join without registering it, and the meaning arrives a fraction of a second later. The viewer infers a kinship between two distant things and enjoys finding it themselves.  
**Used for and where it works best:** Heritage documentary linking a human body to the ground of a place, food montage in advertising, and a science series moving from one scale to another. It is strongest in close-ups where the surface fills the frame, so there is no context left to expose the swap.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Commercial / TVC, Video Essay, Food Video, Title Sequence / Opening Credits, Music Video, Product Video / Motion Design, Experimental / Art Film | genres: Heritage (civilisation-focused), Science / Educational, Nature / Wildlife, Historical / Biopic, Psychological / Arthouse, Social Drama, Tragedy, Surreal / Absurdist  
**Avoid when:** It usually slips past unnoticed when the two textures are too alike and the viewer takes it for the same shot continuing. The exception is when that blur is the intent, in a sequence built to dissolve the borders between things.  
**Prompt:** `editor: match the surface grain, its scale, its light direction and the camera distance across the cut, so the material continues while the subject changes`  
**Yields to:** `cut.graphic_match` — When the join must register, not slip past.  
`cut.texture_match`

### Sound Match Cut

**Also called:** audio match cut, matched sound join  
**What it is:** A cut between two scenes where the sound does the job that shape does in a graphic match: a sound at the end of the first shot resembles a sound at the head of the second, so it seems to continue. The two sounds come from entirely different sources.  
**Effect on the audience:** The ear stitches the join before the eye catches up, so the viewer arrives in the new scene convinced they never left. The difference then lands as a joke or as a shock.  
**Used for and where it works best:** Jumping across time in a biopic or a historical film, moving between two parallel lines in a thriller, and the punchline in dark comedy. In heritage work, a chisel striking stone becomes a hammer in a workshop today, linking two eras with no narration.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Trailer / Teaser, Drama Series Episode, Video Essay, Limited Series, Short Film, Music Video | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Dark Comedy / Satire, Thriller / Suspense, War, Mystery / Whodunit, Tragedy  
**Avoid when:** The difference in timbre is usually audible, so the viewer notices the trick instead of forgetting it. The exception is when the reveal is the point, a satirical move that wants the laugh at the instant the swap is understood.  
**Prompt:** `editor: end the outgoing scene on a sharp sound and open the incoming one on a sound of similar pitch and attack, overlapping them by a few frames across the picture cut`  
**Example:** The 39 Steps, Alfred Hitchcock, the landlady's scream carried into the whistle of a train.  
**Yields to:** `sound.bridge` — When the join must be inaudible, one real sound.  
`cut.sound_match`
