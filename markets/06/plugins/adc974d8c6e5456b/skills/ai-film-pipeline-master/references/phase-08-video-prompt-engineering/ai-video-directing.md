# AI Video Techniques

47 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name What You Are Handing Over

**Also called:** the AI video selector, what goes in besides the words, choose the conditioning first  
**What it is:** The card at the head of the `ai.` shelf. It does not describe a technique. It asks the three questions the shelf's own pair graph asks over and over — **what are you handing the engine besides the words, who is allowed to move inside the clip, and does anything outside this clip have the right to contradict it** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the forty-one `Yields to:` conditions the cards carry, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the technique that does reach the screen was chosen against what you already have on disk, rather than reached for because it was the last one that worked.  
**Used for and where it works best:** Answer the three questions **in order and out loud, in one sentence each, before you open the shelf.** Question one is asked first because it is not a preference, it is an inventory: you either have an approved still or you do not, and half the shelf becomes irrelevant the moment you say which. Question three is asked last and is the only one that can veto the other two. If your answer to question one is *words only* and the shot contains a person, a period or a place, stop — you are not choosing a technique, you are choosing to generate a keyframe, and that is the previous phase's decision.  
**Best in:** formats: all | genres: all  
**Avoid when:** **You are deciding what the frame contains rather than what is asked of the engine.** Composition, headroom, contact points and the declared light state are settled on the still, one phase earlier, and this map has nothing to say about any of them. Also **distrust axis two whenever your honest answer is its last value**: more than a quarter of the shelf decides no motion at all, so on a locking or reference card this map is really two questions, not three. And the warning that matters most is about the pair graph itself: **this shelf's fields compare one shot with another shot.** Anything on it that is a decision about the whole run rather than about one clip is invisible to the graph — nothing routes to it, and the map will therefore never remind you of it. Read the unasked list below before you trust a shortlist, because the card you needed may be one the graph structurally cannot offer.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — What are you handing the engine, besides the words?**
Asked first because it is the condition the shelf repeats most, and because it is an inventory rather than a judgement: fourteen of the forty-one conditions turn on what already exists — *"The shot starts from an approved keyframe"* (`ai.prompt_anatomy`), *"The shot already exists in the wrong ratio"* (`ai.aspect_native`), *"The real site exists and can be photographed"* (`ai.establishing_pass`), *"Photographs do not cover the place from every side"* (`ai.scene_3d_from_images`), *"The intrusion is already in a finished frame"* (`ai.negative_guards`), *"You begin from a still portrait, not footage"* (`ai.lipsync_pass`), *"A calm beat needs to breathe past one clip"* (`ai.one_clip_one_beat`), *"The fault is composition or pose, not detail"* (`ai.inpaint_fix_keyframe`), *"A world already researched and written down"* (`ai.reference_first_heritage`), *"Face leaves and re-enters, or text-weighted engine"* (`ai.image_to_video`).

**Axis 2 — Who is allowed to move inside the clip, and is the move a travel or a change?**
Ten conditions turn on this, and they are stated as facts about the frame rather than as effects on the viewer: *"The subject transforms instead of the camera moving"* (`ai.first_last_frame`), *"Scene holds people, water or fire"* (`ai.camera_only_prompt`), *"The action is too small for a locked frame"* (`ai.action_only_prompt`), *"One small region must move; words are imprecise"* (`ai.motion_prompt`), *"Several things move, or motion is a path"* (`ai.motion_brush`), *"The named move has no narrative reason"* (`ai.camera_presets`), *"The two compositions differ and cannot be locked"* (`ai.keyframe_morph_transition`), *"No event inside the shot to slow"* (`ai.slowmo_retime`), *"Accent the beat with time, not a tighter frame"* (`ai.insert_pass`), *"You need exact control of the cut timing"* (`ai.multi_shot_prompt`).

**Axis 3 — Does anything outside this clip have the right to contradict it?**
Eleven conditions turn on this and they are the only conditions on the shelf that are not about craft at all: *"Historical content claiming accuracy"* (`ai.anime_style_transfer`), *"Period content; light must be motivated by period sources"* (`ai.relight_pass`), *"Historical material where new area must not be invented"* (`ai.outpaint_reframe`), *"Text carries a name, date or number"* (`ai.text_carved_geometry`), *"One clip came back off-colour; fix that clip"* (`ai.colour_grade_lock`), *"One character recurring across a series or episode"* (`ai.character_consistency_refs`), *"The scene has drifted; restart from the source"* (`ai.extend_continue`), *"The output is weak; go back to source"* (`ai.batch_and_select`), *"The beat earns a revealed face"* (`ai.hidden_faces`), *"The audio phrase outruns the base clip length"* (`ai.audio_first_timing`), and the two fields on this shelf that name no card at all and answer to nothing inside the package — `ai.voice_to_face` yielding to *"Documentary honesty / consent"* and `ai.archive_photo_animation` yielding to *"Documentary integrity of the record"*. It is asked last and it overrules, because an error inside a clip is correctable and a falsified record is not.

---

**The map**

**Axis 1 — what you are handing the engine**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Words only — there is no image yet** (eighteen) | `ai.keyframe_first` · `ai.prompt_anatomy` · `ai.negative_guards` · `ai.seed_variation` · `ai.batch_and_select` · `ai.one_clip_one_beat` · `ai.multi_shot_prompt` · `ai.camera_presets` · `ai.aspect_native` · `ai.audio_first_timing` · `ai.establishing_pass` · `ai.broll_pass` · `ai.insert_pass` · `ai.transition_plate` · `ai.prompted_inclip_transition` · `ai.text_carved_geometry` · `ai.count_lock` · `ai.hidden_faces` |
| **One approved still** (seven) | `ai.image_to_video` · `ai.motion_prompt` · `ai.motion_brush` · `ai.camera_only_prompt` · `ai.action_only_prompt` · `ai.inpaint_fix_keyframe` · `ai.voice_to_face` |
| **Two stills, a start and an end** (three) | `ai.first_last_frame` · `ai.keyframe_morph_transition` · `ai.scene_bridge_end_to_start` |
| **A clip that already exists** (ten) | `ai.extend_continue` · `ai.video_to_video_restyle` · `ai.anime_style_transfer` · `ai.lipsync_pass` · `ai.upscale_pass` · `ai.slowmo_retime` · `ai.outpaint_reframe` · `ai.relight_pass` · `ai.mirrored_clone_colour_match` · `ai.silent_clip_sound_design` |
| **A real photograph, or a set of them** (three) | `ai.archive_photo_animation` · `ai.scene_3d_from_images` · `ai.reference_first_heritage` |
| **A sheet or a fixed line you will hand over on every shot** (five) | `ai.reference_sheet_lock` · `ai.character_consistency_refs` · `ai.wardrobe_lock` · `ai.colour_grade_lock` · `ai.style_reference_image` |

**Axis 2 — who is allowed to move**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The camera, and the world holds still** (seven) | `ai.camera_only_prompt` · `ai.camera_presets` · `ai.prompt_anatomy` · `ai.establishing_pass` · `ai.broll_pass` · `ai.text_carved_geometry` · `ai.archive_photo_animation` |
| **The world, and the camera holds still** (five) | `ai.action_only_prompt` · `ai.motion_brush` · `ai.count_lock` · `ai.insert_pass` · `ai.silent_clip_sound_design` |
| **Both, written as one path with a stated ending** (eight) | `ai.image_to_video` · `ai.motion_prompt` · `ai.first_last_frame` · `ai.one_clip_one_beat` · `ai.extend_continue` · `ai.audio_first_timing` · `ai.multi_shot_prompt` · `ai.scene_bridge_end_to_start` |
| **Neither — the change is a transformation, not a travel** (thirteen) | `ai.keyframe_morph_transition` · `ai.prompted_inclip_transition` · `ai.transition_plate` · `ai.video_to_video_restyle` · `ai.anime_style_transfer` · `ai.relight_pass` · `ai.slowmo_retime` · `ai.outpaint_reframe` · `ai.mirrored_clone_colour_match` · `ai.upscale_pass` · `ai.inpaint_fix_keyframe` · `ai.lipsync_pass` · `ai.voice_to_face` |
| **No motion is decided here at all — the card fixes something that must not move** (thirteen) | `ai.keyframe_first` · `ai.reference_sheet_lock` · `ai.character_consistency_refs` · `ai.wardrobe_lock` · `ai.colour_grade_lock` · `ai.style_reference_image` · `ai.hidden_faces` · `ai.reference_first_heritage` · `ai.negative_guards` · `ai.seed_variation` · `ai.batch_and_select` · `ai.aspect_native` · `ai.scene_3d_from_images` |

**Axis 3 — what has the right to contradict this clip**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A document, a period or a real place — the frame can be wrong about the world** (ten) | `ai.reference_first_heritage` · `ai.archive_photo_animation` · `ai.voice_to_face` · `ai.scene_3d_from_images` · `ai.relight_pass` · `ai.outpaint_reframe` · `ai.anime_style_transfer` · `ai.text_carved_geometry` · `ai.count_lock` · `ai.negative_guards` |
| **An earlier shot of your own film — the frame can be wrong against itself** (twenty) | `ai.keyframe_first` · `ai.image_to_video` · `ai.first_last_frame` · `ai.keyframe_morph_transition` · `ai.scene_bridge_end_to_start` · `ai.reference_sheet_lock` · `ai.character_consistency_refs` · `ai.wardrobe_lock` · `ai.colour_grade_lock` · `ai.style_reference_image` · `ai.extend_continue` · `ai.insert_pass` · `ai.broll_pass` · `ai.aspect_native` · `ai.upscale_pass` · `ai.mirrored_clone_colour_match` · `ai.inpaint_fix_keyframe` · `ai.transition_plate` · `ai.lipsync_pass` · `ai.audio_first_timing` |
| **Nothing — the clip answers only to itself** (sixteen) | `ai.prompt_anatomy` · `ai.motion_prompt` · `ai.motion_brush` · `ai.camera_only_prompt` · `ai.action_only_prompt` · `ai.camera_presets` · `ai.multi_shot_prompt` · `ai.one_clip_one_beat` · `ai.seed_variation` · `ai.batch_and_select` · `ai.prompted_inclip_transition` · `ai.video_to_video_restyle` · `ai.slowmo_retime` · `ai.establishing_pass` · `ai.silent_clip_sound_design` · `ai.hidden_faces` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally two to four cards wide.*

*And the map has an edge, which is part of the map.* `ai.` has three twins on the `kf.` shelf and they **agree with it**, which is a boundary rather than a contradiction and has to be said plainly or somebody will file it as a defect. `ai.first_last_frame` and `kf.first_last_pair` are the same technique. `ai.aspect_native` and `kf.native_ratio` are the same rule. `ai.scene_bridge_end_to_start` and `kf.chain_frame` are the same deprecation, down to the same sentence about an extracted frame carrying compression and motion blur and the engine reading that softness as the intended look.

They agree because they are one handover described from both ends. **`kf.` decides the still: what must be true of the image before anybody hands it over** — where the empty space is, whether the pose is settled, whether the light state is declared, whether the contact points resolve. **`ai.` decides what is asked of the engine once the still exists** — what goes in beside it, what is allowed to move, what may not drift. `ai.` stops at the content of the frame: nothing on this shelf may tell you how to compose one. `kf.` stops at the moment the frame leaves the stills stage: nothing on that shelf may tell you how many clips to chain or which pass to run afterwards. Where the twins overlap, **the earlier shelf owns the decision and this one owns its consequences** — a builder who reads the three pairs as duplicates and deletes one half will remove either the composition rule or the generation rule, and both are load-bearing.

---

**The default, and the one against it**

**The default is `ai.motion_prompt`, and it is measured.** It takes four inbound edges, more than any other card on the shelf, and — unlike the shelf's other high scorers — **no two of the four are the same condition**: `ai.prompt_anatomy` (*"The shot starts from an approved keyframe"*), `ai.motion_brush` (*"Several things move, or motion is a path"*), `ai.camera_presets` (*"The named move has no narrative reason"*) and, from another shelf entirely, `ref.video_motion` (*"Reference build differs; write the movement instead"*). Four cards, three families, four different reasons: a structure exists, a mechanism is too clumsy, a shortcut is unmotivated, a reference does not match. That is what a fallback looks like. Compare `ai.reference_sheet_lock`, `ai.outpaint_reframe`, `ai.motion_brush` and `ai.colour_grade_lock`, which take three each — `ai.colour_grade_lock`'s three are two restatements of one condition (`color.arc` and `color.drain` both arrive as *the mechanism*, worded identically) plus one real fork. In-degree measures how often the shelf runs out of room. Distinct conditions measure what it falls back on.

**The one against it is `ai.action_only_prompt`.** Nothing routes to it — not one card, not one law, not one failure — and it is the exact inverse of everything the shelf habitually does. Every other card here adds something: a move, a pass, a lock, a reference, a transformation. `ai.action_only_prompt` subtracts the camera entirely and spends the whole description on what happens inside a frame that never changes. Its mirror twin `ai.camera_only_prompt` — freeze the world, move the camera — is reached twice, by `ai.action_only_prompt` itself and by `ai.broll_pass`; the locked camera is reached never, and the traffic between the twins runs one way only. The shelf routes to stillness in the world and never to stillness in the camera, which is a real asymmetry and not an accident: an engine sells motion, so a reader writing a pair field reaches for motion. Its one stated cost is that a locked frame pinned to a very small action goes lifeless — paid by choosing an action large enough to carry the frame, which is a writing problem rather than a generation problem. It is also, and nobody on the shelf says this, the only frame that survives a burned subtitle intact. **Choosing the best technique is not a creative goal**: `ai.motion_prompt` on an approved keyframe is the correct answer to almost every shot and the reason so much generated work looks like the same slow push.

---

**The unasked**

**Fifteen of the forty-six cards are the target of no `Yields to:` field anywhere in the package.** By id:

`ai.keyframe_first` · `ai.scene_bridge_end_to_start` · `ai.count_lock` · `ai.seed_variation` · `ai.multi_shot_prompt` · `ai.action_only_prompt` · `ai.video_to_video_restyle` · `ai.style_reference_image` · `ai.camera_presets` · `ai.lipsync_pass` · `ai.upscale_pass` · `ai.insert_pass` · `ai.broll_pass` · `ai.relight_pass` · `ai.audio_first_timing`

**And the shape of that list is the finding, not its length: nine of the fifteen are decisions about the run rather than about a shot.** `ai.keyframe_first` is a pipeline. `ai.audio_first_timing` is a schedule. `ai.style_reference_image` is a project-wide reference chosen once. `ai.seed_variation` is an experimental method. `ai.broll_pass`, `ai.insert_pass`, `ai.upscale_pass`, `ai.relight_pass` and `ai.lipsync_pass` are all *passes* — batches run as a stage of the work, with dozens of clips inside them. A `Yields to:` field is written by a reader holding two shots side by side and asking which one to make, and **that reader cannot see a stage.** The shelf's own graph therefore cannot route anyone to the largest decisions on it, and the map above is the only place they appear at all. That is why axis one asks about the run's inventory rather than about the shot's intention. The remaining six are shot decisions and each is unreached for its own reason worth naming: `ai.scene_bridge_end_to_start` is deprecated in its own text, so nobody would route to it; `ai.count_lock` is filed a companion rather than a fork; `ai.camera_presets` and `ai.multi_shot_prompt` are both cards the shelf yields *away* from and never toward; `ai.video_to_video_restyle` is the entrance to the existing-footage region and an entrance has nothing above it; and `ai.action_only_prompt` is the one argued against the default above.

The second thing the list shows is narrower and sharper. **Four cards on this shelf are reachable only because a named failure points at them**, and the failures are on other shelves entirely: `fail.morphing` → `ai.first_last_frame`, `rescue.style_bleed` → `ai.negative_guards`, `rescue.symmetry_drift` → `ai.inpaint_fix_keyframe`, `rescue.prompt_length_collapse` → `ai.prompt_anatomy`. Those are repair edges, and a repair edge starts outside the map and points in, which means those four are not reached by the shelf's own reasoning at all — they are reached by having already gone wrong. A builder reading in-degree at face value would have counted them as popular. They are not popular; they are remedies.

The third thing is a hole with a name, and it sits at the root of the shelf. **Nothing here helps you choose an engine, and one card assumes one.** `ai.scene_bridge_end_to_start` is deprecated in its own `Avoid when:` on the strength of a capability figure — that current engines reach about ten seconds — and it is the only capability figure on the shelf, stated with no date, no source and no review line, in a family that carries no dated line anywhere. Its twin on the neighbouring shelf repeats that figure and then states a different one in the same card. So the card this shelf actually wants is the one it cannot have while every technique here is written as though there were one engine: **the card that says which of these techniques a given engine can run at all**, kept dated and separate, so that a craft rule is never again retired by an undated number.

`ai.what_you_hand_the_engine`

---

### The Keyframe-First Pipeline

**Also called:** stills first, approve the frame then animate  
**What it is:** You generate the still frame for the shot first, review it and fix it until it is right, and only then animate it. The creative decision is closed on the still before time ever enters the picture.  
**Effect on the audience:** It lets you see the whole film as stills before spending anything on motion. The result is a unified look across shots, because every choice was made at the same stage.  
**Used for and where it works best:** Any project with dozens of shots: a heritage documentary, a kids song, an episodic series. Show the keyframes to the client, get approval, and then every shot animates with confidence and no surprises.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Trailer / Teaser, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Family, Preschool / Early Learning, Mythology / Ancient Epic, Drama, Science / Educational, Fantasy / Epic  
**Avoid when:** Moving to animation while you are unhappy with the still usually wastes the generation, because motion does not repair weak composition; the exception is a test clip run to learn how the model reads the frame. Inside this pipeline, any change of style belongs to the stills stage, not after the shots are moving; footage filmed or generated outside it is restyled by `ai.video_to_video_restyle`.  
**Prompt:** `generate the shot as a finished still first, full composition, final lighting and wardrobe, then use that exact frame as the start of the clip`  
`ai.keyframe_first`

### Image-to-Video from an Approved Keyframe

**Also called:** I2V, animate the still, start frame animation  
**What it is:** You hand the approved still to the shot as its starting point, so the text describes only movement. Look, wardrobe and lighting are already settled inside the frame, and every word of the prompt goes to motion.  
**Effect on the audience:** Visual consistency between shots becomes reliable, because all of them grew out of approved frames. The result reads as a film instead of a pile of unrelated clips.  
**Used for and where it works best:** This is the default method for any serious work: heritage, kids, advertising, music video. It matters most when one character must stay the same across twenty shots, or when period costume has to stay accurate.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Product Video / Motion Design | genres: Heritage (civilisation-focused), Historical / Biopic, Family, Preschool / Early Learning, Mythology / Ancient Epic, Drama, Fantasy / Epic, Faith / Biblical Epic  
**Avoid when:** Do not re-describe what is already visible in the frame; repeated description pulls attention away from the motion. Write a clear ending too, or the move stops somewhere arbitrary.  
**Outranks:** re-describing the scene, the wardrobe and the light in the motion prompt, whenever the
shot is conditioned on an approved keyframe. The keyframe has already settled them; restating them in
words gives the engine a second, weaker description to reconcile against the image, and it spends
prompt budget that the motion needs. **An approved keyframe is a closed shot: it needs a camera, not a
scene description.** The identity lock (`ident.frozen_sentence`) is still quoted whole and first, as
the video guide's law 2 requires: it is short, and it holds the face when the head turns or leaves
frame and returns. A clip that shows only part of the character quotes only its visible parts, never the
face clauses (the video guide, [`how-to-write-a-video-prompt.md`](how-to-write-a-video-prompt.md) §4.3).
**The same holds for a start-and-end keyframe pair:** both frames are settled, so the prompt
describes the transition between them — the camera path, the speed, what changes — and not the
subject.  
**Prompt:** `animate from this exact frame, subject and lighting unchanged, slow push in, ending framed on her hands`  
**Yields to:** `ident.frozen_sentence` — Face leaves and re-enters, or text-weighted engine.  
`ai.image_to_video`

### First-Frame plus Last-Frame Generation

**Also called:** start and end frame, keyframe pair, F2L  
**What it is:** You give the shot two images, the first frame and the last frame, and the motion is built between them. You decide where it starts and where it settles, and the middle is filled in.  
**Effect on the audience:** It gives you control over the ending, which is the most important part of any move because the next cut is built on it. The transition becomes designed rather than accidental.  
**Used for and where it works best:** Every camera move that must land on a specific composition, and every change inside a shot: day to night, an empty hand to a full one, far to near. In heritage work it lets you travel from ruins to the standing building inside one shot.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Music Video, Kids Content, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Mythology / Ancient Epic, Drama, Science / Educational, Family  
**Avoid when:** If the two frames sit too far apart in composition, what happens between them reads as a jump rather than a move. Close the gap or split the shot into two stages.  
**Prompt:** `use the first image as the opening frame and the second as the final frame, smooth continuous move between them, no cut`  
**Yields to:** `ai.keyframe_morph_transition` — The subject transforms instead of the camera moving.  
`ai.first_last_frame`

### The Keyframe Morph Transition

**Also called:** morph between two generated frames, in-shot transformation  
**What it is:** The same first and last frame idea, but the goal is not a camera move; it is a transformation of the subject: clay becomes a tablet, a child becomes a man, ruins become a living city. The two frames share the same composition so the change can flow.  
**Effect on the audience:** It states a meaning with no words: this became that. The viewer links the two states automatically, because his eye never left the frame.  
**Used for and where it works best:** Crossing between eras in heritage documentary, growth and time in kids content, and product transformation in advertising. In music video it is a clean way to move scenes without cutting.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Title Sequence / Opening Credits | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Science / Educational, Family, Preschool / Early Learning, Mythology / Ancient Epic  
**Avoid when:** If the composition differs between the two frames, the transformation turns to mush in the middle. Lock the angle, the scale and the light across both, and let only one thing change.  
**Prompt:** `morph smoothly from the first frame to the second, camera locked and composition identical, only the subject transforming`  
**Yields to:** `ai.prompted_inclip_transition` — The two compositions differ and cannot be locked.  
`ai.keyframe_morph_transition`

### The End-to-Start Scene Bridge

**Also called:** last frame becomes the next first frame, chained shots  
**What it is:** You take the final frame of one clip and use it as the opening frame of the next. In the edit the two join with no jump, because the last image and the first image are literally the same.  
**Effect on the audience:** It delivers the feel of one long continuous shot even though it was assembled from parts. The viewer senses that time never broke.  
**Used for and where it works best:** Building a long take with generated clips: down the corridor, through the door, out onto the roof, all as chained segments. In heritage documentary it carries you through a large site without a cut.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Music Video, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Commercial / TVC, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Thriller / Suspense, Fantasy / Epic, Drama, Mythology / Ancient Epic, Adventure  
**Avoid when:** **The extracted frame is not a keyframe and must not be used as one.** A frame pulled
out of a finished clip carries that clip's compression and its motion blur, so it arrives softer and
less detailed than anything generated from the references. Feed it back in and the engine reads that
softness as the intended look and continues from it, so every link is a degradation of the last: by
the third the face has drifted and the palette has moved. Also note that current engines reach about
ten seconds, and a real shot rarely holds longer than that without a cut, so the case this technique
was invented for is rarer than it was - and where a long held shot is genuinely wanted, a calm opening or a long walk under narration, `ai.extend_continue` builds it from the clean source.  
**Shelf life:** dated — review 2027-03. The ten-second engine ceiling is a product limit, not a craft fact; check the engine's own current page before relying on it.  
**Yields to:** `ident.clean_source`, always. Where a move genuinely needs more than one clip,
generate a start keyframe **and** an end keyframe from the references and let the engine interpolate
between them — two frames of equal quality, and no inherited drift.  
**Prompt:** `start keyframe and end keyframe both generated from the reference sheets; interpolate the move between them, same lighting and same camera speed throughout`  
`ai.scene_bridge_end_to_start`

### Reference Sheet Identity Lock

**Also called:** character sheet lock, model sheet reference  
**What it is:** You build a reference sheet for the character with several body views and close-ups carrying different expressions, and you feed that sheet as the reference on every shot. The sheet is the character's official document.  
**Effect on the audience:** Face, body and wardrobe stay themselves from shot to shot, so the viewer recognises the character instantly. Without a sheet the character drifts between shots and identification is lost.  
**Used for and where it works best:** Any series, episode or song with a recurring character, and kids content above all, because a child bonds to the look before the name. In heritage work the sheet also carries the correct dress, jewellery and hairstyle and stops them drifting.  
**Best in:** formats: AI-Generated Clip, Kids Content, Music Video, Heritage / Historical Documentary, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Anime (Japanese 2D) | genres: Family, Preschool / Early Learning, Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Fairy Tale, Mythology / Ancient Epic, Adventure  
**Avoid when:** Do not cut the sheet into pieces or feed half of it; the complete set is what carries the identity. Any change to the character belongs in the sheet first, because a change made inside a single shot lives only in that shot and the next one contradicts it.  
**Prompt:** `use the attached character sheet as the identity reference, same face, same hair, same costume, treat the sheet as one single character`  
**Yields to:** `ai.character_consistency_refs` — The shot needs an angle-matched reference, not the sheet.  
`ai.reference_sheet_lock`

### Character Consistency Through References

**Also called:** identity references, multi-image reference  
**What it is:** With every shot you supply one or more images of the same character, ideally close to the angle the shot needs. The references work the way a continuity photograph works for a crew.  
**Effect on the audience:** It makes the viewer feel this is the same person even in a new shot and a new place. Continuity is what creates a character; written description alone does not.  
**Used for and where it works best:** Every narrative project: an episode, a song, a commercial with a lead, a documentary with a historical figure. Supply the reference from an angle close to the one you need, so the features read the way you intend.  
**Best in:** formats: AI-Generated Clip, Kids Content, Music Video, Heritage / Historical Documentary, Commercial / TVC, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser | genres: Family, Preschool / Early Learning, Heritage (civilisation-focused), Historical / Biopic, Drama, Fantasy / Epic, Mythology / Ancient Epic, Faith / Biblical Epic  
**Avoid when:** Do not mix references from different styles in one shot, or you get a third character who resembles neither. And if you change the reference mid project, go back and regenerate the earlier shots. When the shot is animated from an approved keyframe, `ai.image_to_video` outranks re-describing the skin tone and the costume in the motion prompt; the identity sentence is still quoted whole (the video guide's law 2).  
**Prompt:** `keyframe or reference generation: keep the character identical to the attached reference images, same facial structure, same skin tone, same costume details in every shot | image-to-video: attach the approved keyframe and describe motion only; verify identity against the same references in QA`  
**Yields to:** `ai.reference_sheet_lock` — One character recurring across a series or episode.  
`ai.character_consistency_refs`

### The Wardrobe Lock

**Also called:** costume lock, garment continuity  
**What it is:** You fix the wardrobe as one written line, copy it into every image prompt and character-sheet prompt without changing a character, and pair it with a reference image of the costume. It is not written into a video prompt: the clip takes the wardrobe from the keyframe or the attached sheet. Colour, fabric, jewellery, belt and footwear are written once and repeated.  
**Effect on the audience:** It stops wardrobe drifting between shots, which is the single most visible giveaway in generated work and the fastest way to break the feeling of one continuous scene.  
**Used for and where it works best:** Heritage and period work above all: the robe, the belt and the jewellery must hold across the whole episode. In advertising it holds the model's outfit, and in kids content it holds the shirt a child recognises.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Drama Series Episode, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Fashion Film | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Family, Preschool / Early Learning, Drama, Faith / Biblical Epic, Fantasy / Epic  
**Avoid when:** A costume described in vague terms like ancient clothing usually comes back as a different garment every shot, so write the colour, the fabric and the pieces. And any change to the wardrobe belongs in the fixed line and goes back to every shot, not to one of them. The lock line belongs to the keyframe's and the sheet's prompts, never the motion prompt: the frame already carries the wardrobe (`ai.image_to_video`).  
**Prompt:** `keyframe or character-sheet prompt: wardrobe locked, cream wool robe with a red woven belt, bronze arm ring on the right arm, leather sandals, identical in every shot | video: verify those same items against the record, never restate them in the motion prompt`  
`ai.wardrobe_lock`

### The Colour-Grade Lock

**Also called:** palette lock, look consistency line  
**What it is:** You write one fixed line about light and colour and use it on every shot: time of day, direction of light, colour temperature, dominant hues. Keep one approved still of the look beside the line; later clips are checked against it. Whatever remains is unified by the final grade in the edit.  
**Effect on the audience:** Shots read as belonging to the same film even when they were generated on different days. Colour is the fastest signal that tells a viewer he is in one world.  
**Used for and where it works best:** Any project with more than one shot, especially a heritage documentary or a song with thirty clips. Decide the palette at the start, low golden sun or cool overcast daylight, and hold it.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Music Video, Kids Content, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Drama Series Episode | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Family, Mythology / Ancient Epic, Romance, Faith / Biblical Epic, Fantasy / Epic  
**Avoid when:** Do not change the time of day between shots of the same scene unless story time is genuinely moving. And when one clip comes back oddly coloured, fix it in the grade rather than breaking the unity of the rest. When the shot is animated from an approved keyframe, `ai.image_to_video` outranks this: the frame already carries the light and colour, and restating it in the motion prompt is the second, weaker description its `Outranks:` field rules out. The lock line then belongs to the keyframe's prompt, not the motion prompt.  
**Prompt:** `keyframe or text-only generation: consistent look across shots, low golden late afternoon sun from the left, warm highlights, cool shadows, soft dust in the air | image-to-video: attach the approved keyframe, describe motion only, then match the result beside the reference still in QA`  
**Yields to:** `repair.colour_match_pass` — One clip came back off-colour; fix that clip.  
`ai.colour_grade_lock`

### The Count Lock

**Also called:** exact number lock, counted objects  
**What it is:** When the number carries meaning, you write it as a digit and as a word and describe each item by its place: three ducklings, one left, one centre, one right. Then you confirm it on the still before animating.  
**Effect on the audience:** The correct count is what makes teaching content honest. A child counts along with the screen, and a wrong number breaks the entire lesson in a second.  
**Used for and where it works best:** Counting songs and preschool content, explainers built on quantities, and any commercial showing how many pieces are in the box. Lock the number in the keyframe and do not let the animation add or remove anything.  
**Best in:** formats: Kids Content, Explainer, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Music Video, Corporate / Training | genres: Preschool / Early Learning, Family, Science / Educational, Comedy, Fairy Tale  
**Avoid when:** Left to a vague word like several or a group, the count drifts from shot to shot, so write the number and the position of each item. Check the frame with your own eyes before animating, because a miscount is the first thing an audience notices.  
**Prompt:** `exactly three ducklings, one on the left, one in the centre, one on the right, no other animals in frame`  
`ai.count_lock`

### The Hidden-Face Identity Trick

**Also called:** silhouettes and back views, faceless figures  
**What it is:** You build the shot so the face is never seen: from behind, as a silhouette against the light, shadowed under a headdress, framed off at the shoulders, or with the hands carrying the beat. The figure is present without a face.  
**Effect on the audience:** It strengthens identification rather than weakening it: with no face to look at, the viewer puts himself in that place. It also grants mystery and stature, and lets the body and the costume do the talking.  
**Used for and where it works best:** Heritage and myth, where you do not want a contemporary face pinned onto a king or a priest. In any long series it also reduces the burden of facial continuity across dozens of shots, and in horror and thriller it raises tension.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Trailer / Teaser, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Short Film, Drama Series Episode | genres: Heritage (civilisation-focused), Mythology / Ancient Epic, Historical / Biopic, Horror, Thriller / Suspense, Faith / Biblical Epic, Mystery / Whodunit, Tragedy  
**Avoid when:** If every shot hides the face the piece turns cold and loses its emotion. Let the face be revealed in the beat that earns it and keep the rest in shadow.  
**Prompt:** `the figure seen from behind against the doorway light, face never visible, silhouette and robe reading against the bright background`  
**Yields to:** `ai.reference_sheet_lock` — The beat earns a revealed face.  
`ai.hidden_faces`

### The Reference-First Rule for Heritage

**Also called:** source before prompt, documented accuracy  
**What it is:** On a history piece the user wants realistic, you look for a real reference for the historical element (the canon first, then the web): a relief, a museum object, a site plan, an excavation photograph. Then you describe what the reference shows, not what you remember.  
**Effect on the audience:** It prevents the blending of civilisations, which is the most common failure in historical content. Accuracy is what gives the work authority and turns it into a reference rather than decoration.  
**Used for and where it works best:** Every heritage project: dress, crown, weapon, temple form, ornament. Attach the reference as an image alongside the prompt, and pin the decisive details in words (the beard type, the belt form, the number of horns on the crown). Write its source beside it.  
**Best in:** formats: Heritage / Historical Documentary, AI-Generated Clip, Documentary Feature, Documentary Series, Kids Content, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, Science / Educational, Drama  
**Avoid when:** A historical description written from memory usually goes wrong, because memory blends centuries and cultures; the exception is a world you have already researched and written down, which is no longer memory. If no reference turns up for a detail, generate the closest thing the canon and the period support and note it; it never holds the shot.  
**Prompt:** `match the attached relief reference exactly, same beard style, same fringed shawl, same bracelet form, no elements from other periods`  
**Yields to:** `prompt.rule.b_the_mesopotamia_canon` — A world already researched and written down.  
`ai.reference_first_heritage`

### Seed and Variation Strategy

**Also called:** seed control, variation batch  
**What it is:** The seed is the number that fixes the random starting point. You hold it when you want to change one word and see exactly what that word did, and you change it when you want different ideas from the same description.  
**Effect on the audience:** It turns generation from gambling into a controlled experiment. You learn what each word actually does instead of guessing.  
**Used for and where it works best:** When dialling in an important shot: hold the seed and test the lighting, then hold it again and test the move. When hunting for a fresh idea for an opening shot: same description, different seeds, then choose.  
**Best in:** formats: AI-Generated Clip, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Heritage / Historical Documentary, Product Video / Motion Design, Trailer / Teaser | genres: Heritage (civilisation-focused), Family, Drama, Fantasy / Epic, Science / Educational, Comedy, Action  
**Avoid when:** Changing the seed and the wording in the same pass usually wastes the test, because you will not know which one moved the result; the exception is an early exploratory round where you are still hunting for a direction. And do not hunt for a seed that rescues a weak description; fix the description.  
**Prompt:** `same prompt, fixed seed, change only the lighting line, generate four variations to compare`  
**Yields to:** `ai.batch_and_select` — Early exploratory round still hunting a direction.  
`ai.seed_variation`

### Negative-Prompt Guards

**Also called:** negative prompt, exclusion list  
**What it is:** A short list of what you do not want in frame: text and lettering, extra people, modern objects, logos, extra hands. It goes in the dedicated field or as a clear exclusion line.  
**Effect on the audience:** It cuts the number of wasted attempts and protects period scenes from modern contamination. The shot comes back clean on the first pass instead of the fifth.  
**Used for and where it works best:** Heritage and period work (no cars, no cables, no wristwatches, no modern lettering), kids content (nothing frightening), and advertising (no competing logos). Keep the list short and aimed at what this particular scene is likely to attract.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Explainer, Product Video / Motion Design | genres: Heritage (civilisation-focused), Historical / Biopic, Preschool / Early Learning, Family, Mythology / Ancient Epic, Faith / Biblical Epic, Science / Educational  
**Avoid when:** A very long list pulls weight away from the main description, so exclude only what is relevant to this scene. Do not guard against something the scene would never produce; every extra word has a cost.  
**Prompt:** `negative: text, watermark, extra people, modern clothing, cars, wristwatches, plastic objects`  
**Yields to:** `repair.artefact_removal` — The intrusion is already in a finished frame.  
`ai.negative_guards`

### Prompt Anatomy

**Also called:** prompt structure, the five part prompt  
**What it is:** A structured prompt has five parts in a fixed order: subject, action, camera with its start, path and end, light and place, then exclusions. Each part is one short line. The delivery ratio belongs to the request rather than to these lines: set it with the request and let `control.prompt_anatomy` check it before sending.  
**Effect on the audience:** A fixed order makes your results predictable and repeatable, and tells you which part to edit when something needs to change. It also lets a whole team write the same way.  
**Used for and where it works best:** Every shot in every project. The most important part is the end of the camera move, because it sets the final frame, and that frame is what you will cut from.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Explainer | genres: all  
**Avoid when:** Do not cram everything into one long sentence, where the parts drown each other. And skipping the end of the move usually costs you the last frame, because the shot settles somewhere you did not choose; the exception is a clip you intend to cut mid motion.  
**Prompt:** `subject, then action, then camera with start and path and end, then light and place, then the exclusion line`  
**Yields to:** `ai.motion_prompt` — The shot starts from an approved keyframe.  
`ai.prompt_anatomy`

### The Motion Prompt

**Also called:** describe motion not scene, action-led prompting  
**What it is:** When you start from an approved still, the text describes only movement: who moves, where to, at what speed, and what the camera does and where it stops. The scene itself is already solved by the image.  
**Effect on the audience:** Every word goes to the motion, so the clip moves the way you pictured it. Re-describing the scene dilutes attention and leaves the movement generic.  
**Used for and where it works best:** Every shot that starts from a keyframe, which is most of your work. Give the subject a real path, from where to where and what happens at the end, instead of a word like moving.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Trailer / Teaser | genres: all  
**Avoid when:** Do not describe ten movements in one shot; keep the subject's move and the camera's move clear and limited. A generic description of motion returns generic motion.  
**Prompt:** `she lifts the lamp from the table to eye level while the camera pushes in slowly, ending on the flame`  
**Yields to:** `ai.motion_brush` — One small region must move; words are imprecise.  
`ai.motion_prompt`

### One Clip, One Beat

**Also called:** single beat per clip, one idea per shot  
**What it is:** Each generated clip is designed around a single idea: one move, one action or one change, and then it settles. The story is assembled from those units in the edit.  
**Effect on the audience:** It produces a clean edit and a rhythm you control rather than inherit. Each clip also becomes replaceable without collapsing the shots around it.  
**Used for and where it works best:** Any narrative project assembled in the edit: a kids song, a documentary, a commercial, a vertical short. It is also the most economical way to work, because you can regenerate one clip without redoing the scene.  
**Best in:** formats: AI-Generated Clip, Kids Content, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Heritage / Historical Documentary, Explainer, Trailer / Teaser | genres: all  
**Avoid when:** Do not compress a whole scene into one clip, where the story is squeezed and stops reading. At the same time do not chop everything: if a beat needs to breathe, let one calm shot carry it.  
**Prompt:** `one single beat: he sets the tablet down on the table and lifts his hand away, camera static, nothing else happens`  
**Yields to:** `ai.extend_continue` — A calm beat needs to breathe past one clip.  
`ai.one_clip_one_beat`

### The Camera-Only Prompt

**Also called:** frozen scene moving camera, camera-led clip  
**What it is:** You ask for the scene to hold still while only the camera moves: no character motion, no wind, no change in light. One clear move along a defined path.  
**Effect on the audience:** It yields a clean, calm shot in which the viewer can actually read detail. It is the ideal treatment for architecture, artefacts and products.  
**Used for and where it works best:** Heritage documentary on a relief, a statue or a temple facade, product film, and the beats between scenes. It is also an excellent bed for a long stretch of narration.  
**Best in:** formats: Heritage / Historical Documentary, AI-Generated Clip, Product Video / Motion Design, Documentary Feature, Explainer, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Mythology / Ancient Epic, Faith / Biblical Epic, Nature / Wildlife, Drama  
**Avoid when:** If the scene contains people, water or fire and you demand total stillness, the result feels dead. Reserve the freeze for scenes that are already still.  
**Prompt:** `the scene is completely still, nothing moves except the camera, slow dolly in from the wide to the carved panel, ending centred on the inscription` Text treatment: the inscription is described as carved geometry, not as text (`textimg.carved_not_text`).  
**Yields to:** `ai.motion_brush` — Scene holds people, water or fire.  
`ai.camera_only_prompt`

### The Action-Only Prompt

**Also called:** locked camera moving subject  
**What it is:** The reverse: the camera is locked with no move and no push, and the whole description goes to what moves inside the frame.  
**Effect on the audience:** A locked camera reads as composure and lets the eye study the action without distraction. The action becomes the subject, because nothing else in the frame is moving.  
**Used for and where it works best:** Craft and handwork beats in heritage work (hands working clay, a scribe cutting a tablet), comedy, and simple kids content. It is also the cleanest frame to place titles or subtitles over.  
**Best in:** formats: Heritage / Historical Documentary, Kids Content, AI-Generated Clip, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Documentary Feature, Commercial / TVC | genres: Heritage (civilisation-focused), Historical / Biopic, Preschool / Early Learning, Family, Comedy, Science / Educational, Drama  
**Avoid when:** Do not pair a locked camera with a very small action, or the shot goes lifeless. And if the action is large and fast, a locked frame can let part of it escape the edges.  
**Prompt:** `camera completely locked on a tripod, no movement and no zoom, only his hands move as they press the seal into the wet clay`  
**Yields to:** `ai.camera_only_prompt` — The action is too small for a locked frame.  
`ai.action_only_prompt`

### The Multi-Shot Prompt

**Also called:** two-shot clip, built-in cut  
**What it is:** Inside one clip you ask for more than one shot with a cut between them: a wide and then a close-up, or a face and then what that face is looking at. You write the shots in order and say where the cut falls.  
**Effect on the audience:** It hands you a small complete scene in a single file, which saves time and keeps lighting and character identical across both shots.  
**Used for and where it works best:** Teasers, vertical shorts and fast segments that must deliver two pieces of information in two seconds. In documentary use it to link a face to what it sees without generating two separate clips.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, AI-Generated Clip, Commercial / TVC, Music Video, Meme / Comedy Edit, Kids Content, Explainer | genres: Action, Comedy, Thriller / Suspense, Drama, Family, Adventure, Heritage (civilisation-focused)  
**Avoid when:** Do not ask for more than two cuts inside a short clip, where the story crowds itself and stops reading. And when you need exact control of timing, generate the two shots separately and cut them yourself.  
**Prompt:** `two shots in one clip: first a wide of the gate with the crowd, then cut to a close-up of the boy's face looking up`  
**Yields to:** `ai.one_clip_one_beat` — You need exact control of the cut timing.  
`ai.multi_shot_prompt`

### Extend / Continue Generation

**Also called:** continue the clip, extension pass  
**What it is:** You take an existing clip and ask for a continuation, which returns additional seconds carrying the same move and the same scene forward. You can repeat it, but each repeat compounds drift, so it is a fast extension rather than the method for a continuity-critical long take.  
**Effect on the audience:** It gives you longer shots without losing continuity, and that changes the rhythm of the whole edit: you can hold one breathing shot instead of cutting three short ones.  
**Used for and where it works best:** The calm opening shot, the long walking beat in a documentary, and any scene that must run under a long line of narration. In music video it covers a musical phrase longer than the base clip. Compare each extension against the source before approval and stop at the first failed identity, geometry or motion check.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Documentary Feature, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Explainer, Trailer / Teaser | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Nature / Wildlife, Mythology / Ancient Epic, Science / Educational, Faith / Biblical Epic  
**Avoid when:** Each extension builds on the one before it, so a weak first segment compounds. Extend from your cleanest version, and if the scene drifts, go back to the original keyframe and start again. Use it where the same move simply carries on; where the shot develops, the next segment starts from a frame generated from the references, never from a frame pulled out of the finished clip (`kf.chain_frame`).  
**Prompt:** `continue this clip forward with the same camera speed and the same light, he keeps walking away down the corridor`  
**Yields to:** `ident.clean_source` — The scene has drifted; restart from the source. `kf.chain_frame` — The take is continuity-critical or develops beyond the same move.  
`ai.extend_continue`

### Lettering Described as Carved Geometry

**Also called:** carved text trick, engraved lettering prompt  
**What it is:** When you need lettering to hold in a shot, you describe it as carved or embossed geometry in stone or metal rather than as words, and you lock the camera completely. The letters become part of the material instead of a text layer on top of it.  
**Effect on the audience:** The lettering holds and genuinely reads as cut into the surface, with light travelling across it the way it travels over any relief. It looks excavated rather than added.  
**Used for and where it works best:** Inscriptions, tablets, seals and stone signage in heritage work, and an engraved logo in premium advertising. When the text must be perfectly legible, set it in the edit over a clean plate instead.  
**Best in:** formats: Heritage / Historical Documentary, AI-Generated Clip, Commercial / TVC, Product Video / Motion Design, Title Sequence / Opening Credits, Trailer / Teaser, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, Science / Educational, Drama  
**Avoid when:** Do not ask for a big camera move across the lettering; keep the frame locked or move it very little. And when the text carries decisive information such as a name, a date or a number, do not rely on the image alone: set it in the edit.  
**Prompt:** `deeply carved cuneiform wedges cut into the stone surface, described as engraved geometry not as text, camera locked, raking light across the grooves`  
**Yields to:** `textimg.repair_not_regenerate` — Text carries a name, date or number.  
`ai.text_carved_geometry`

### Video-to-Video Restyle

**Also called:** V2V, style transfer on footage, restyle pass  
**What it is:** You supply existing footage, filmed or generated, and ask for the same motion in another style: illustration, anime, painting, a different material. The movement and timing stay; the surface changes.  
**Effect on the audience:** It lets you act the motion with a real body and then dress it in any look. That solves the hardest thing in animation: natural timing and honest weight.  
**Used for and where it works best:** Music videos and stylistic transitions, and turning a simple reference take into a fantasy world. In heritage work you can film a real hand shaping clay and restyle it into the look of the film.  
**Best in:** formats: Music Video, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Trailer / Teaser, Experimental / Art Film, Kids Content, Anime (Japanese 2D) | genres: Fantasy / Epic, Surreal / Absurdist, Comedy, Action, Psychological / Arthouse, Heritage (civilisation-focused), Family, Sci-Fi  
**Avoid when:** If the source take is shaky or badly framed, style will not rescue it. State one clear style as well, because blending two returns something that belongs to neither.  
**Prompt:** `restyle this footage, keep the exact motion and timing, render it as hand painted illustration with visible brush strokes`  
**Yields to:** `ai.anime_style_transfer` — The target look is specifically anime.  
`ai.video_to_video_restyle`

### Style Transfer to Anime

**Also called:** anime restyle, 2D look pass  
**What it is:** A specific case of restyling: you convert live-action or generated footage into anime language, flat colour, line work, large eyes, painted backgrounds. You pin the style with an anime reference frame.  
**Effect on the audience:** It changes the rules of belief: the viewer accepts exaggeration and big emotion because he is inside a drawn world. It also pulls one specific audience instantly.  
**Used for and where it works best:** Music videos, youth content and teasers, and stories built on heroism and large emotion. In advertising aimed at a young audience it stands out sharply against realistic content.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Trailer / Teaser, Anime (Japanese 2D), Commercial / TVC, Title Sequence / Opening Credits, Meme / Comedy Edit | genres: Shonen Battle (anime), Shojo (anime romance), Isekai (anime), Action, Romance, Fantasy / Epic, Coming of Age, Magical Girl (anime)  
**Avoid when:** The style must run across the whole piece, not one shot, or that shot reads as a stranger. Avoid it in historical content claiming accuracy, because the style announces that this is fiction.  
**Prompt:** `convert to anime style, flat cel colour with clean line work, painted background, keep the original motion and framing`  
**Yields to:** `ai.reference_first_heritage` — Historical content claiming accuracy.  
`ai.anime_style_transfer`

### The Style Reference Image

**Also called:** style ref, look reference, aesthetic anchor  
**What it is:** You attach one image that embodies the look you want, its lighting, palette, texture and degree of realism, and keep it as the fixed reference across the project. The picture says what words cannot.  
**Effect on the audience:** It unifies dozens of shots without rewriting the same paragraph every time. The image is also more precise than any sentence, because style is a visual matter to begin with.  
**Used for and where it works best:** The start of any project: pick one frame that represents the whole film and show it to the client as the mood board. From then on every shot is generated against that same reference.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Product Video / Motion Design | genres: all  
**Avoid when:** Do not swap the style reference mid project, or the shots split into two worlds. Choose an image close to the kind of shots you need as well, since a close-up reference will not set the look of a wide.  
**Prompt:** `match the attached style reference exactly, same palette, same light quality, same level of realism and texture`  
**Yields to:** `ai.colour_grade_lock` — No single image suits every shot size.  
`ai.style_reference_image`

### Painted Motion Areas

**Also called:** motion painting, directed motion areas, motion brush and motion control (the names two vendors sell it under)  
**What it is:** You paint directly on the image to mark which area should move and in which direction, leaving the rest still. Instead of describing motion in words, you point at it.  
**Effect on the audience:** It gives precision that words cannot: this flag moves, this water travels left, everything else holds. The result lands much closer to what you pictured.  
**Used for and where it works best:** Shots that need one small deliberate movement: smoke from a censer, a banner on the wall, a curtain, a river, hair in the wind. In heritage work it is ideal for bringing an architectural frame to life through one moving element.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Commercial / TVC, Music Video, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Nature / Wildlife, Family, Mythology / Ancient Epic, Faith / Biblical Epic  
**Avoid when:** Do not paint many regions in one shot, or the motion fragments and the scene turns restless. Start with one or two areas and let the rest stay still.  
**Prompt:** `only the banner and the rising smoke move, everything else in the frame stays completely still`  
**Yields to:** `ai.motion_prompt` — Several things move, or motion is a path.  
`ai.motion_brush`

### Camera Preset Moves

**Also called:** camera presets, named move library  
**What it is:** A library of ready camera moves with known names: crash zoom, bullet time, snorricam, FPV flight, dolly zoom, crane. You call the move by name instead of describing it.  
**Effect on the audience:** It returns a clean, predictable move, which saves time and makes the same behaviour repeatable across ten shots. The names are also a shared language with any crew.  
**Used for and where it works best:** Vertical shorts, teasers and commercials that need high energy fast: a crash zoom onto a face, an FPV flight through a space, an orbit around a product. In heritage work stay with the calm moves and hold to them.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Trailer / Teaser, AI-Generated Clip, Music Video, Product Video / Motion Design, Game Cinematic / Gameplay, Kids Content | genres: Action, Comedy, Thriller / Suspense, Sports Drama, Sci-Fi, Adventure, Superhero  
**Avoid when:** A preset with no narrative reason is showmanship, and a whole piece of it reads as a capability demo. Choose the move from the meaning of the scene, not from the menu.  
**Prompt:** `crash zoom in on his face, fast push with slight motion blur, hard stop framed on the eyes`  
**Yields to:** `ai.motion_prompt` — The named move has no narrative reason.  
`ai.camera_presets`

### The Lip-Sync Pass

**Also called:** lipsync, dialogue sync pass  
**What it is:** You take the finished shot and the audio file and run a pass that drives the lips and jaw with the speech. It happens after both the image and the voice track are approved.  
**Effect on the audience:** It turns a moving picture into a person speaking to you. Speech binds a viewer to a character faster than any camera move can.  
**Used for and where it works best:** A presenter, a character telling the story, a testimonial in an ad, a talking animal in kids content. In multilingual work it is what lets you reissue the same shot in another language.  
**Best in:** formats: Commercial / TVC, Kids Content, Explainer, Corporate / Training, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Interview / Video Podcast | genres: Family, Preschool / Early Learning, Comedy, Drama, Science / Educational, Romance  
**Avoid when:** Give the face enough size and keep it toward the lens so the mouth reads. Record the voice first and build the shot to its length, so the line is never squeezed into a shorter clip.  
**Prompt:** `lip sync this character to the attached voice track, natural jaw movement, small head motion while speaking, eyes staying with the lens`  
**Yields to:** `ai.voice_to_face` — You begin from a still portrait, not footage.  
`ai.lipsync_pass`

### Voice-Driven Portrait Animation

**Also called:** audio to face, talking portrait  
**What it is:** You start from a still face, a portrait, an archive photograph or a drawing, and drive it with audio so the whole face moves: mouth, brows and head. It differs from a lip-sync pass in that you begin with a picture, not with footage.  
**Effect on the audience:** It feels as though an old photograph has woken and spoken. The emotional charge is high, because the viewer knows the person in that picture has been silent for a long time.  
**Used for and where it works best:** Documentary and oral history: a soldier's letter, a poet's notebook, a grandfather's testimony. In education a historical figure introduces himself, and in kids content a drawing speaks and tells the story.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Explainer, Kids Content, Video Essay, AI-Generated Clip, Corporate / Training, Interview / Video Podcast | genres: Historical / Biopic, Heritage (civilisation-focused), Science / Educational, Family, Preschool / Early Learning, Tragedy, True Crime, Faith / Biblical Epic  
**Avoid when:** Making a real, identifiable person say words he did not say has no honest use, because honesty is the ground documentary stands on. Tell the viewer he is watching a written text performed when you use it on historical material.  
**Prompt:** `animate this portrait to the attached voice, natural mouth and brow movement, slight head motion, the rest of the image unchanged`  
**Yields to:** Documentary honesty / consent — A real identifiable person saying unsaid words.  
`ai.voice_to_face`

### The Upscale Pass

**Also called:** upres, resolution pass, detail enhancement  
**What it is:** A final pass that raises the resolution of a clip and rebuilds its detail: cleaner texture, tighter edges, less noise. It is run after the shot is locked, never before.  
**Effect on the audience:** It lets a clip survive a large screen and sit beside filmed material. Side by side, the upscaled version simply reads as more expensive even though the image is the same.  
**Used for and where it works best:** Every final delivery: high resolution upload, screen projection, a commercial. In heritage work it matters most on reliefs and materials, because the small detail is what makes stone feel like stone.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Commercial / TVC, Music Video, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Documentary Feature | genres: all  
**Avoid when:** Do not upscale a shot whose framing or motion is wrong; you will simply get a sharper mistake. Upscale once at the end as well, because repeated passes push the image toward a synthetic look.  
**Prompt:** `upscale the final clip to high resolution, recover fine texture detail, keep the original grain character and colour`  
`ai.upscale_pass`

### The Mirrored-Clone Colour Match

**Also called:** mirrored surround, video-to-video colour trick  
**What it is:** When a video has to blend with a surround or another shot, you frame it with muted mirrored copies of itself running in sync, instead of trying to match its colour with a flat static fill.  
**Effect on the audience:** The colours match themselves automatically, because it is literally the same image, so no seam appears between the centre and the edges. The result reads as designed rather than patched.  
**Used for and where it works best:** Filling the space when a horizontal video sits inside a vertical frame, backgrounds on presentation pages, and anywhere a video must fill the screen without cropping the composition.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Product Video / Motion Design, Corporate / Training, Explainer, AI-Generated Clip, Commercial / TVC, Title Sequence / Opening Credits | genres: all  
**Avoid when:** Keep the surrounding copies quiet, blurred or dimmed, so they never pull the eye off the centre. And if the source has strong motion, the mirrored copies become a distraction.  
**Prompt:** `the same clip mirrored and blurred on both sides of the frame, playing in sync, filling the vertical format without cropping the centre`  
**Yields to:** `ai.outpaint_reframe` — The source carries strong motion.  
`ai.mirrored_clone_colour_match`

### The Prompted In-Clip Transition

**Also called:** in-shot transition, generated wipe  
**What it is:** You ask for the transition to happen inside the clip: the camera passes behind a column and the scene has changed, dust fills the frame and reveals another place, water crosses the lens.  
**Effect on the audience:** The transition belongs to the world instead of being an effect added in the edit. The viewer feels time moved inside the shot rather than being cut.  
**Used for and where it works best:** Heritage documentary crossing between periods, music video, and vertical shorts that need continuity with no cuts. In advertising it moves from the problem to the solution in one shot.  
**Best in:** formats: Heritage / Historical Documentary, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, AI-Generated Clip, Trailer / Teaser, Title Sequence / Opening Credits, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Drama, Comedy, Adventure, Mythology / Ancient Epic  
**Avoid when:** If the wiping element does not fully cover the frame, the join is exposed and the transition turns messy. Choose something that passes close to the lens: a column, a wall, thick dust, a body crossing.  
**Prompt:** `the camera tracks right behind a thick stone column that fills the frame, and when it clears the column the same place is now a living city`  
**Yields to:** `ai.transition_plate` — No element can fully cover the frame.  
`ai.prompted_inclip_transition`

### The Generated Transition Plate

**Also called:** transition element, generated wipe element  
**What it is:** You generate the transition element on its own against black or white: a dust pass, sparks, water, smoke, a sweep of light. Then you lay it over the cut in the edit.  
**Effect on the audience:** It builds you a transition library in the film's own style instead of stock wipes that always look imported. The transition ends up sharing the project's colour and material.  
**Used for and where it works best:** A series that needs consistent interstitials, heritage documentary (clay dust, sand, sparks from a kiln), and advertising. Generate three or four and keep them as the project's library.  
**Best in:** formats: Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Commercial / TVC, Trailer / Teaser, Title Sequence / Opening Credits, AI-Generated Clip, Drama Series Episode | genres: Heritage (civilisation-focused), Historical / Biopic, Action, Fantasy / Epic, Mythology / Ancient Epic, Drama  
**Avoid when:** Do not use an element unrelated to the material of the scene; sand across a sea shot looks imported. Keep the pass fast as well, because a long transition stalls the rhythm.  
**Prompt:** `thick dust sweeping across the frame from right to left on a pure black background, no other elements, for use as an overlay`  
**Yields to:** `ai.prompted_inclip_transition` — The transition must belong to the world.  
`ai.transition_plate`

### The AI B-Roll Pass

**Also called:** b-roll generation, coverage pass  
**What it is:** You generate a batch of short supporting shots covering the same subject: details, hands, sky, movement in the space, small objects. They are produced as one set in a single look and light.  
**Effect on the audience:** It gives the edit room to breathe and lets narration run without tiring the eye on a single frame. Sufficient coverage is what lets an editor actually work.  
**Used for and where it works best:** Documentary, corporate video and interview work, where two minutes of narration need images over it. In heritage work generate site details, tools and hands to carry the long stretches of commentary.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Corporate / Training, Interview / Video Podcast, Explainer, Video Essay, AI-Generated Clip, News Report / Reportage | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, True Crime, Nature / Wildlife, Drama, Faith / Biblical Epic  
**Avoid when:** Do not generate coverage without knowing which line it sits under, or you end up with pretty images that do no work. Tie every shot to a specific line of narration.  
**Prompt:** `short supporting detail shot in the same style and light as the main scene, hands working the clay, shallow focus, no camera move`  
**Yields to:** `ai.camera_only_prompt` — One calm move can bed long narration.  
`ai.broll_pass`

### The AI Establishing-Shot Pass

**Also called:** establisher generation, opening wide pass  
**What it is:** You generate the wide that establishes the place: the city, the valley, the temple from outside, the house from the street. It is produced at the same hour and in the same weather as the rest of the scene.  
**Effect on the audience:** It gives the viewer a map before you take him into detail, so he never gets lost. The wide is also the most expensive shot in traditional production and the cheapest one to generate.  
**Used for and where it works best:** The top of every scene in heritage documentary and drama, and the opening of an episode. In travel and real estate it frames the context before you go inside.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, AI-Generated Clip, Drama Series Episode, Trailer / Teaser, Travel / Real Estate / Hospitality, Explainer, Documentary Series | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Drama, Adventure, Faith / Biblical Epic, Nature / Wildlife, War  
**Avoid when:** A wide with no life in it, no people, smoke, birds or movement, reads as dead and synthetic. Keep its details matched to the close shots as well, or the viewer feels he is in two different places.  
**Prompt:** `wide establishing shot of the river city at the same golden hour as the scene, smoke rising from rooftops, small figures moving on the quay`  
**Yields to:** `ai.scene_3d_from_images` — The real site exists and can be photographed.  
`ai.establishing_pass`

### The AI Insert / Detail Pass

**Also called:** insert shots, macro detail pass  
**What it is:** Very tight shots on a single detail: a hand closing, an eye moving, a seal pressing into clay, a drop falling. Each one runs a second or two with a small movement.  
**Effect on the audience:** A tight detail makes the viewer feel the object in his own hand and gives the edit its accents. They are also the easiest shots to make convincing, because the frame is narrow and carries few peripheral details.  
**Used for and where it works best:** Heritage, craft, food and product work, and any beat you want to accent in the edit. Generate three or four versions of the same detail so you can choose while cutting.  
**Best in:** formats: Heritage / Historical Documentary, Commercial / TVC, Product Video / Motion Design, Documentary Feature, Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Family, Romance, Drama, Thriller / Suspense  
**Avoid when:** Do not generate details unrelated to the story; they become beautiful filler. Keep the light and the material identical to the wide, or the cut looks like it came from another scene.  
**Prompt:** `extreme close-up insert, the seal rolling across wet clay leaving the impression, shallow focus, tiny move only`  
**Yields to:** `ai.slowmo_retime` — Accent the beat with time, not a tighter frame.  
`ai.insert_pass`

### AI Slow-Motion Re-Time

**Also called:** frame interpolation, retime pass, generated slow motion  
**What it is:** A pass that creates additional frames between the existing ones, so a clip can be slowed without the motion stuttering. It is applied to the locked shot before delivery.  
**Effect on the audience:** Slow motion grants a moment weight and lyricism and lets the eye study what it cannot catch at normal speed. After sound it is the strongest accent tool you have.  
**Used for and where it works best:** The peak beat in a music video or commercial, and the touch, the fall or the look in drama. In heritage work slow the craftsman's hand so the viewer can actually see how the work is done.  
**Best in:** formats: Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Heritage / Historical Documentary, Sports Broadcast / Sports Film, Trailer / Teaser, Dance Film | genres: Drama, Romance, Action, Sports Drama, Heritage (civilisation-focused), Tragedy, Fantasy / Epic  
**Avoid when:** Slowing a shot with no event inside it kills the shot. Push the slow too far and you also expose detail you never wanted the viewer to study.  
**Prompt:** `retime this clip to fifty percent speed with smooth interpolated frames, no stutter, motion staying fluid`  
**Yields to:** `ai.silent_clip_sound_design` — No event inside the shot to slow.  
`ai.slowmo_retime`

### AI Outpaint Reframe

**Also called:** reframe, aspect conversion, generative extend  
**What it is:** You extend the image or clip beyond its original borders to fill another aspect ratio, horizontal to vertical or the reverse. The new areas are built from the context of the picture itself.  
**Effect on the audience:** It lets you publish one shot across platforms without cropping faces or destroying composition. The result reads as framed for the new ratio rather than cut down to it.  
**Used for and where it works best:** Turning a horizontal project into vertical shorts, and the reverse when vertical material has to go to a wide platform. In heritage work it extends an archive photograph to fill the screen without black bars.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Commercial / TVC, AI-Generated Clip, Heritage / Historical Documentary, Product Video / Motion Design, Trailer / Teaser, Documentary Feature | genres: all  
**Avoid when:** The generated areas can add something that never existed in the original scene, so review them by eye, above all in historical content. And when the camera moves a lot, the new edges hold less steadily.  
**Prompt:** `extend this horizontal frame to a vertical 9:16 format, continuing the sky above and the ground below, keep the subject centred`  
**Yields to:** `ai.mirrored_clone_colour_match` — Historical material where new area must not be invented.  
`ai.outpaint_reframe`

### AI Relight Pass

**Also called:** relighting, light direction change  
**What it is:** You change the lighting of an existing image or clip: turn day into dusk, move the key to another side, add a candle or a window. Form and composition stay as they were.  
**Effect on the audience:** Light is the fastest way to change the mood of a shot, so you get a new scene without rebuilding anything. It also lets you unify shots that were generated at different times.  
**Used for and where it works best:** Unifying a scene when one shot came back in different light, and moving the same location from day to night in the story. In product work it tests several lighting ideas on one shot before you commit.  
**Best in:** formats: AI-Generated Clip, Product Video / Motion Design, Commercial / TVC, Heritage / Historical Documentary, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Corporate / Training | genres: Heritage (civilisation-focused), Drama, Romance, Thriller / Suspense, Historical / Biopic, Horror, Science / Educational  
**Avoid when:** Change the light direction without moving the shadows with it and the image contradicts itself, feeling wrong for reasons the viewer cannot name. In period content keep the light motivated by sources that existed in that century.  
**Prompt:** `relight this shot as late golden hour from camera left, warm key on his face, shadows falling to the right, everything else unchanged`  
**Yields to:** `ai.reference_first_heritage` — Period content; light must be motivated by period sources.  
`ai.relight_pass`

### AI 3D Scene from Images

**Also called:** generated 3D scene, neural scene reconstruction  
**What it is:** You supply a set of photographs of the same place from different angles, and a 3D scene is reconstructed from them in which you can move a new camera to angles nobody ever shot.  
**Effect on the audience:** It converts stills into a place you can enter. Instead of presenting photographs you present the experience of a location, which is a large difference in documentary.  
**Used for and where it works best:** Heritage documentation: photograph the site from every side, then move a camera through it in shots no crew could have taken. Also real estate, museums and education, for presenting a place without a complex shoot.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, 360 / VR, Explainer, Travel / Real Estate / Hospitality, Corporate / Training, AI-Generated Clip, Video Essay | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Nature / Wildlife, Mythology / Ancient Epic, Faith / Biblical Epic, Adventure  
**Avoid when:** If the photographs do not cover the place from every side, the new angles come back incomplete. Shoot in steady light with nothing moving in the scene so the reconstruction stays clean.  
**Prompt:** `reconstruct the site from the supplied photographs and fly a new camera through the central courtyard at eye height`  
**Yields to:** `ai.establishing_pass` — Photographs do not cover the place from every side.  
`ai.scene_3d_from_images`

### Audio-First Timing

**Also called:** cut to the real audio, sound-led assembly  
**What it is:** You finish the audio first, narration, song or dialogue, extract the real timings from it, and only then set the length of each shot and generate to that length.  
**Effect on the audience:** The edit moves with the music instead of fighting it, and you avoid regeneration because every shot was made at its correct length from the start.  
**Used for and where it works best:** Kids songs, music videos and narrated documentary, and anything with a rhythm. Read the timing from the audio file itself and not from the script, because the performance never matches the page.  
**Best in:** formats: Kids Content, Music Video, Lyric Video, Heritage / Historical Documentary, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Explainer | genres: Preschool / Early Learning, Family, Musical, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Drama  
**Avoid when:** Do not trust a generated subtitle file without checking the timing against the audio itself, because the openings drift. And do not generate shots before the audio is locked, or you lose all of them when the performance changes.  
**Prompt:** `shot length cut to the audio, three seconds ending exactly on the drum hit, motion resolving on the last beat`  
**Yields to:** `ai.extend_continue` — The audio phrase outruns the base clip length.  
`ai.audio_first_timing`

### Batch and Select

**Also called:** multiple takes, generate several and choose  
**What it is:** You generate several versions of the same shot from the same description and treat them as takes: you screen them all and cut with the best one.  
**Effect on the audience:** It raises the level of the whole film, because every shot is chosen rather than tolerated. Comparing versions also teaches you what actually works in that scene.  
**Used for and where it works best:** The shots that matter: the opening, the peak, and any close-up on a face. On large projects run a batch while you work on something else, then select in one sitting.  
**Best in:** formats: AI-Generated Clip, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary, Kids Content, Trailer / Teaser, Product Video / Motion Design | genres: all  
**Avoid when:** Regenerating from a weak output usually multiplies the fault, so go back to the original source, the keyframe or the reference, and start from there. A large batch on a weak description also burns time and money for nothing.  
**Prompt:** `same prompt, same references, four takes of this shot for selection in the edit`  
**Yields to:** `ident.clean_source` — The output is weak; go back to source.  
`ai.batch_and_select`

### Inpainting a Keyframe Fix

**Also called:** inpaint, local repair, patch the frame  
**What it is:** You repair one region of a frame instead of regenerating the whole shot: a wrong hand, a modern object in the background, unwanted lettering, a flawed face. You mark the area and describe what belongs there.  
**Effect on the audience:** It preserves everything that was already right and fixes the one thing that was not. Compared with regenerating and hoping, the time saved is enormous.  
**Used for and where it works best:** Any keyframe with excellent composition and a single mistake, and clearing modern intrusions out of period scenes. In kids content it corrects a count or a colour before the shot is animated.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Preschool / Early Learning, Family, Science / Educational, Drama, Faith / Biblical Epic  
**Avoid when:** Do not patch a large region, because it comes back lit differently from the rest of the frame. And if the error is in the composition rather than a detail, patching will not help: generate the shot again.  
**Prompt:** `repair only the marked region, replace the modern sign with plain plastered wall, keep the lighting and texture identical to the surrounding area`  
**Yields to:** `repair.regenerate_vs_repair` — The fault is composition or pose, not detail.  
`ai.inpaint_fix_keyframe`

### Archive Photo Animation

**Also called:** bringing a photograph to life, historical still animation  
**What it is:** You take a genuine historical photograph and give it a small amount of life: people breathing, dust drifting, a banner shifting, the camera easing across. The content stays as it is and only motion is added.  
**Effect on the audience:** Motion collapses the distance of time. The viewer stops looking at a document and starts looking at people who lived.  
**Used for and where it works best:** Historical and heritage documentary, family and memory pieces, and openings. Put the motion into the secondary elements, smoke, cloth, light, and keep the faces as still as possible. Archive the untouched source separately.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Documentary Series, Video Essay, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Interview / Video Podcast, News Report / Reportage | genres: Historical / Biopic, Heritage (civilisation-focused), Tragedy, True Crime, Drama, War, Faith / Biblical Epic, Science / Educational  
**Avoid when:** Altering the faces in the photograph or adding people who were not there falsifies the document, and no shot is worth that. Keep the motion very small as well, because exaggeration makes the image read as fake. Never use generated frames as evidence of what the camera originally recorded. Motion the photograph could not have held — figures walking, a crowd turning — is `trans.still_to_motion`'s case, and keeps documentary standing only when declared as an interpretation.  
**Prompt:** `animate this historical photograph with minimal motion, drifting dust and a slight shift of cloth, faces unchanged, gentle push in`  
**Yields to:** Documentary integrity of the record — Altering faces or adding people not there.  
`ai.archive_photo_animation`

### Native Aspect Generation

**Also called:** generate in the delivery ratio, native vertical  
**What it is:** You generate the shot in its delivery ratio from the start, vertical for shorts, wide for cinema, instead of generating one ratio and cropping later. The composition is built for the final frame.  
**Effect on the audience:** The composition becomes deliberate: the face sits where it should and the empty space is reserved for captions. Cropping afterwards always costs you part of the image and part of the meaning.  
**Used for and where it works best:** Vertical shorts, platform-specific advertising, and anything delivered in two formats. When two versions are needed, generate both rather than cropping one.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Music Video, Commercial / TVC, AI-Generated Clip, Kids Content, Product Video / Motion Design, Meme / Comedy Edit | genres: all  
**Avoid when:** Do not forget the platform interface zones when you generate vertical: keep heads and key information away from the top and bottom edges. And a hard crop from wide to vertical cuts the composition in half.  
**Prompt:** `generate natively in 9:16 vertical, subject centred with headroom, clear empty space in the lower third for captions`  
**Yields to:** `ai.outpaint_reframe` — The shot already exists in the wrong ratio.  
`ai.aspect_native`

### Sound Design for a Generated Clip

**Also called:** sound pass on AI footage, silent clip workflow  
**What it is:** A generated clip arrives in the edit without a built sound world, so you construct it in layers: the room or place, the movement of the body, whatever is touched, and one accent on the key moment.  
**Effect on the audience:** Sound convinces a viewer that a shot is real more effectively than the picture does. A footstep on stone and the reverb of a hall bring the place into existence.  
**Used for and where it works best:** Every generated shot in every project, and heritage work above all: the reverb of a hall, wind, clay, fire, so the viewer feels the place exists rather than having been drawn.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Kids Content, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Trailer / Teaser | genres: Heritage (civilisation-focused), Historical / Biopic, Horror, Drama, Mythology / Ancient Epic, Family, Thriller / Suspense, Faith / Biblical Epic  
**Avoid when:** Do not lean on music to cover everything, because without the sounds of the place the shot still feels hollow. Keep the accent to one moment as well: if everything is accented, nothing is important.  
**Prompt:** `designed with layered sound, room tone of the stone hall, footsteps on gravel, cloth movement, one low accent on the reveal`  
`ai.silent_clip_sound_design`
