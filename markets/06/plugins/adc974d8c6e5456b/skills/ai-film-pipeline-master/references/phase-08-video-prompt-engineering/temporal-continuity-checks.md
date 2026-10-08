# Control and Continuity Checks

19 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Movement Speed and Acceleration Check

**Also called:** velocity curve check, move pacing check  
**What it is:** Separating three things that a description usually blurs together: the distance the camera travels, the time it takes, and the velocity curve between them. A slow move is not necessarily a small move, and a short move can be violent.  
**Effect on the audience:** Once all three are fixed, the viewer gets the intended feeling instead of one near it. An eased start reads as contemplation, a hard start reads as a reaction.  
**Used for and where it works best:** Before writing any movement line in a generation request, and before setting the move on the timeline in an edit. Ask how far, in how many seconds, whether it starts soft or sudden, and whether it settles or is cut at its peak. It matters most in generated clips and motion design, where the curve is written rather than felt.  
**Best in:** formats: AI-Generated Clip, Product Video / Motion Design, Trailer / Teaser, Commercial / TVC, Title Sequence / Opening Credits, 3D CG Animation, Feature Film, Music Video, Explainer | genres: Action, Thriller / Suspense, Drama, Sci-Fi, Heritage (civilisation-focused), Fantasy / Epic, Horror, Musical  
**Avoid when:** The check usually hardens into numbers carried from one project to the next, so a duration that worked in a trailer lands on a dialogue scene. The exception is a series built on one rhythm, where keeping the numbers fixed is the identity.  
**Prompt:** `brief: state the start pose, the path, the distance, the duration in seconds, the easing at each end, and the final hold, then change one of them per test`  
`control.movement_speed`

### Shutter and Motion Blur Design

**Also called:** shutter angle check, blur design, strobe check  
**What it is:** Choosing the exposure duration inside each single frame, which is entirely separate from the frame rate and from the final playback speed. A narrow shutter gives hard edges and a stuttered feel, a wide shutter gives soft trails.  
**Effect on the audience:** The same movement reads as harsh or as fluid on the strength of the shutter alone. The viewer cannot name the cause but feels either violence or flow.  
**Used for and where it works best:** Before shooting any fight, run or explosion, and before asking a generative model for a fast shot. Battle and war material gains from a narrow shutter, while dance, dream states and soft transitions gain from a wide one. Judge the result at the final playback speed, not at the capture speed.  
**Best in:** formats: Feature Film, AI-Generated Clip, Trailer / Teaser, Music Video, Anime (Japanese 2D), 3D CG Animation, Sports Broadcast / Sports Film, Game Cinematic / Gameplay, Dance Film | genres: Action, War, Chase, Martial Arts / Wuxia, Horror, Musical, Sci-Fi, Samurai / Chanbara  
**Avoid when:** One setting is usually locked across a whole film, so scenes with different energies end up feeling identical. The exception is when that consistency is a declared style, a piece that wants one texture from beginning to end.  
**Prompt:** `brief: state the frame rate and the shutter treatment together, narrow for staccato impacts or wide for smeared motion, and review the motion at final playback speed`  
`control.shutter_blur`

### Aspect Ratio and Reframing Plan

**Also called:** ratio plan, multi-ratio delivery check  
**What it is:** Fixing the final ratio of every deliverable before shooting, and fixing what has to remain inside the frame in each of them. Ratio is independent of lens, of resolution and of genre.  
**Effect on the audience:** With the ratios planned in advance, the film is not blindly trimmed later. On every platform the viewer sees an intended composition rather than the leftovers of another one.  
**Used for and where it works best:** In any project delivered horizontally, vertically and square at once: the commercial, the heritage campaign, the music video. Put the important action inside the area shared by the ratios, or shoot a second pass composed natively for vertical. In generated clips ask for the ratio inside the request rather than cropping afterwards.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Product Video / Motion Design, Brand Film, AI-Generated Clip, Trailer / Teaser, Vertical Micro-Drama, Explainer | genres: Drama, Comedy, Heritage (civilisation-focused), Action, Musical, Romance, Science / Educational, Family  
**Avoid when:** Planning for every ratio at once usually produces a compromise composition that serves none of them. The exception is a budget that allows a native pass per ratio, where each one is then designed on its own.  
**Prompt:** `brief: name the delivery ratios, compose natively for the primary one, keep the key action inside the shared area, and never assume a centre crop will work`  
**Yields to:** `ai.aspect_native` — Budget for a native pass per ratio instead of one shared composition.  
`control.aspect_reframe`

### The Transition Contract

**Also called:** cut contract, in and out declaration  
**What it is:** A written statement of what leaves the outgoing shot and what enters with the incoming one: the final pose, the direction of the movement, where the dominant shape sits in frame, the light, and the sound that crosses. It is written before either shot is filmed or generated.  
**Effect on the audience:** The transition becomes designed rather than lucky. The viewer crosses from one shot to the next without feeling the seam.  
**Used for and where it works best:** Before every match cut, every hidden transition, and every join between two generated clips. Write it as two lines: out, then in. In generative work this contract is the only reliable way to make the last frame and the first frame meet.  
**Best in:** formats: AI-Generated Clip, Feature Film, Trailer / Teaser, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), 3D CG Animation, Title Sequence / Opening Credits | genres: Action, Fantasy / Epic, Heritage (civilisation-focused), Thriller / Suspense, Musical, Sci-Fi, Drama, Historical / Biopic  
**Avoid when:** The contract is usually written after the clips exist, so it becomes a rescue job in the edit. The exception is two shots already filmed and impossible to redo, where the gap is then bridged with a move or a crossing sound.  
**Prompt:** `brief: OUT, the final pose, motion direction and light of the outgoing shot; IN, the matching opening pose, direction and light of the incoming shot; name what may change and what the sound does across the join`  
**Yields to:** `anim_time.sound_bridge_j_cut_timing` — Two shots already filmed, bridged by a crossing sound.  
`control.transition_contract`

### Exposure and White Balance Continuity

**Also called:** brightness continuity, colour temperature match  
**What it is:** Confirming that face brightness and colour temperature stay close across adjacent shots, and that any change between them has a reason inside the scene. It is judged on the face and on a neutral reference, not on a general impression.  
**Effect on the audience:** An unmotivated jump in brightness or colour pulls the viewer's attention onto the craft. Remove it and the attention stays on the performer.  
**Used for and where it works best:** Any scene that stretches across hours of daylight, anything shot by windows or under mixed sources, and all generative work where each clip comes from an independent run. Shoot a grey reference at the head of every setup, and in generation repeat the same light description word for word in every request.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, AI-Generated Clip, Heritage / Historical Documentary, Interview / Video Podcast, Corporate / Training, Docudrama / Reenactment | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Verite / Observational, Social Drama, Thriller / Suspense, Romance, Medical Drama  
**Avoid when:** It is usually left to the grade at the end, so a large jump gets corrected at the cost of image quality. The exception is a change that is intended and visibly motivated, such as a character stepping from sunlight into a room.  
**Prompt:** `brief: hold the same key direction, subject exposure and colour temperature across the join, and allow a change only when something inside the scene causes it`  
`control.exposure_wb_continuity`

### Rolling Shutter and Flicker Check

**Also called:** skew check, banding check, jello test  
**What it is:** Two separate checks on the same material: one for vertical lines skewing during fast movement, one for brightness banding caused by pulsing light or a filmed display. They have different causes and different remedies.  
**Effect on the audience:** Skew and banding read as a digital fault, so the viewer doubts the quality of the whole piece even when everything else is solid.  
**Used for and where it works best:** Before any fast pan, before filming a display, a billboard or concert lighting, and before high speed work. Test with the real setup rather than a similar one, and watch the test at the size it will be shown.  
**Best in:** formats: Concert / Live Event, Sports Broadcast / Sports Film, Drama Series Episode, Feature Film, Corporate / Training, Music Video, News Report / Reportage, Game Cinematic / Gameplay, Vlog / YouTube Long-Form | genres: Action, Musical, Thriller / Suspense, Drama, Sports Drama, Crime / Procedural, Science / Educational  
**Avoid when:** The problem is usually found after the shoot, when the fix is expensive or impossible. The exception is when the banding is wanted, a scene reaching for an old screen or a corrupted memory - and banding kept on purpose is a brightness pulse that somebody chose, not a fault, so its rate and stopping point stop being questions for the test pass and become `safety.photosensitive_flash`.  
**Prompt:** `brief: run the fastest planned pan and the real practical lights through one test take, then inspect vertical lines for skew and flat walls for banding at final size`  
**Yields to:** `look.crt_scanlines` — The banding is wanted, an old screen or a corrupted memory.  
`control.rolling_shutter_flicker`

### Flashing That Can Injure a Viewer

**Also called:** photosensitive sequence, the flash that is not a taste question, tier 0 flashing  
**What it is:** **A repeated flash, a strobe, a fast alternation between very dark and very bright frames, or a moving high-contrast pattern can trigger a seizure in a viewer who is photosensitive** — including one who has never had a seizure before and does not know they are at risk. This is not eye strain, not fatigue and not an accessibility preference. It is an injury that happens to a person in their own room while the piece is playing, with no chance to stop it in time, which is why it sits at **tier 0 of [`PRECEDENCE.md`](../PRECEDENCE.md) and not at tier 5 with the craft**: it outranks the drop, the trailer's charge, the director's intent and the client's approval, and it is the one note in this package that is not weighed against effect.  
**Effect on the audience:** To almost everyone, nothing at all — which is exactly the problem, because the room where the piece is reviewed will almost never contain the person it hurts, and no test screening the maker attends will report it. To the viewer it does reach, a sequence they cannot finish and sometimes a hospital.  
**Used for and where it works best:** The moment any repeated flash, strobe, explosion series, saturated red pulse, rapid dark-to-bright cutting or fine moving stripe or grid pattern enters the shot table — not at delivery, when the sequence has been approved and paid for. Three things, in order. **First, what raises the risk:** how often the change repeats, how large the brightness swing is, how much of the frame it covers, whether the colour is a saturated red, and whether a high-contrast pattern is involved. All five matter and they compound. **Second, what this package does not write.** Whether a specific sequence is safe is a **measurement** — made with an analyser built for it, against the published standard the destination enforces, by whoever is qualified to run it. This package does not carry the thresholds, does not carry a test procedure, and cannot be used to clear a sequence; an eyeball judgement is not a check, and neither is *it looked fine to us*. That refusal is deliberate and it is the same one as [`SKILL.md`](../../SKILL.md) §0: a half-method here would be followed and believed, and the numbers involved are not ours to invent. **Third, what happens instead of stopping the work:** the shot carries `pending_photosensitivity_check` with its timecode, exactly as every other unanswered input carries a marker (see [`ENGINE-CHECK.md`](../ENGINE-CHECK.md)), and the marker travels in the handoff to whoever delivers, who closes it one of two ways: measured and passed, or **the flashing changed until the question no longer arises**. It never holds the work. A warning card at the head is something some broadcasters require *in addition* to a passed measurement. It is not a substitute for one: a piece that ships the warning instead of the check has told the viewer at risk to leave rather than made the piece safe for them.  
**Best in:** formats: Music Video, Trailer / Teaser, Concert / Live Event, Kids Content, Game Cinematic / Gameplay, Commercial / TVC, Projection Mapping, Multi-Screen Installation, Museum Installation, 360 / VR, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film | genres: all  
**Avoid when:** **Ordinary light is never this question**: firelight, candles, a lamp, a sunset, a flickering bulb or a turning emergency light in a scene; this card covers only a deliberate strobe or rapid flash sequence. A single flash that does not repeat, and a slow pulse, are not what this is about — treating every bright frame as a hazard drains the rule of force and gets it waved through where it matters. What it does not excuse is a *short* sequence: the danger lives in the rate and the repetition rather than in the length, so a few seconds is not automatically safe, and a piece for a small briefed audience is not exempt because the room is never as closed as it was described.  
**Prompt:** `brief: list every repeated flash, strobe, dark-to-bright cut run and moving high-contrast pattern with its timecode, mark each pending_photosensitivity_check, and put the list in the handoff for whoever delivers to have measured`  
`safety.photosensitive_flash`

### Comfort and Flashing Review

**Also called:** photosensitivity review, motion comfort pass  
**What it is:** Reviewing rapid brightness changes and the motion imposed on the viewer, on the screen where the piece will actually be shown. The whole sequence is reviewed rather than isolated frames, because it is the accumulation that does the damage. **This is the comfort pass and it is not the safety one** — it covers motion sickness, eye fatigue and the viewer who leaves because watching is unpleasant. Whether the flashing can injure somebody is a different question with a different answer, owned by `safety.photosensitive_flash`, and passing this review does not answer it.  
**Effect on the audience:** The work reaches a wider audience without hurting anyone. A viewer sensitive to light or motion finishes watching instead of leaving.  
**Used for and where it works best:** Before delivering any trailer with flashes, any music piece with a light pulse, any 360 or VR experience, and anything for a large screen. Prepare a reduced flash and reduced motion alternative whenever the audience is general or made of children.  
**Best in:** formats: Trailer / Teaser, Music Video, 360 / VR, Multi-Screen Installation, Projection Mapping, Kids Content, Game Cinematic / Gameplay, Commercial / TVC, Concert / Live Event | genres: Horror, Action, Musical, Sci-Fi, Thriller / Suspense, Preschool / Early Learning, Family, Cyberpunk  
**Avoid when:** The flashing is usually softened until the trailer loses its charge. The exception is to deliver two versions: one at full intensity and one reduced for general platforms — and **the full-intensity version is the one that still has to pass the measurement**, because a warning at the head is a comfort measure, not a safety one.  
**Prompt:** `brief: review the full sequence on the delivery screen for rapid brightness changes and forced motion, and prepare a reduced flash and reduced motion variant`  
**Yields to:** `safety.photosensitive_flash` — wherever the question is whether a flash can injure a viewer rather than whether it is uncomfortable. Comfort is traded against effect; that one is not.  
`control.comfort_flashing`

### Spatial and 360 Composition Check

**Also called:** VR staging check, attention path check  
**What it is:** Confirming that the important event in a 360 scene sits in a direction the viewer can reach, and that something leads them there: a sound, a light, a movement, or a person looking. Composition still exists even with no rectangular frame.  
**Effect on the audience:** The viewer feels free without getting lost. With no cues they spend their time searching, miss the event, and lose trust in the experience.  
**Used for and where it works best:** Before shooting any 360 scene, building any VR moment, or mounting a multi screen installation. Place the event near the starting view direction, cue it with spatial sound two seconds ahead, and do not force the viewer's head to turn.  
**Best in:** formats: 360 / VR, Multi-Screen Installation, Projection Mapping, AR Experience, Game Cinematic / Gameplay, Interactive Film / Playable Experience, Concert / Live Event, Experimental / Art Film | genres: Adventure, Heritage (civilisation-focused), Science / Educational, Horror, Fantasy / Epic, Drama, Nature / Wildlife  
**Avoid when:** The scene is usually designed like a proscenium stage, the rear hemisphere is neglected, and the viewer feels they are in a half empty room. The exception is when the emptiness behind is the intent, as when the viewer stands at an edge.  
**Prompt:** `brief: mark the starting view direction, place the key event within reach of it, cue it with light or spatial sound before it happens, and leave the rear hemisphere composed`  
`control.spatial_360`

### Animation Timing and Held Poses Check

**Also called:** spacing check, pose hold check, exposure cadence  
**What it is:** Reviewing pose spacing, the length of the holds, and changes in drawing cadence inside one shot. Timing is an authored decision, not a single technical setting applied to everything.  
**Effect on the audience:** A long hold gives the image weight and the burst after it gives the image force. The viewer feels heaviness and release as if they were real physics.  
**Used for and where it works best:** Before executing any anime or 2D shot, and before animating a logo in motion design. Decide where the image stops, for how many frames it stops, and what erupts after it. In kids content keep the poses longer and clearer so the action reads on the first pass.  
**Best in:** formats: Anime (Japanese 2D), 2D Animation (Western / Cartoon), 3D CG Animation, Kids Content, Title Sequence / Opening Credits, Product Video / Motion Design, Game Cinematic / Gameplay, Explainer, Stop Motion | genres: Shonen Battle (anime), Mecha (anime), Preschool / Early Learning, Family, Comedy, Action, Fantasy / Epic, Magical Girl (anime)  
**Avoid when:** Timing is usually spread evenly across the whole action, which comes out mechanical and weightless. The exception is when regularity is the point: a machine, an army, or a fixed musical pulse.  
**Prompt:** `brief: name the key poses, the number of frames each one holds, and the accelerated burst between them, so the silhouette reads at every hold`  
**Yields to:** `anim_time.downbeat_transient_cutting` — A fixed musical pulse, not authored spacing, sets the holds.  
`control.animation_timing`

### The Generative Continuity Contract

**Also called:** consistency contract, reference sheet contract  
**What it is:** Fixing what must not change across every generated clip: the same character, the same wardrobe, the same lens, the same light direction and the same grade. The visual reference sheet is the contract, and words alone do not hold it.  
**Effect on the audience:** The viewer believes the clips come from one world. Any drift in the face, the wardrobe or the light breaks the illusion at once and exposes how the piece was made.  
**Used for and where it works best:** Before generating any sequence longer than two clips. Prepare a character sheet with four body views and four face close-ups, and repeat the light, lens and grade sentence word for word in every request. Inspect the actual outputs rather than assuming the sentence did the job.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Trailer / Teaser, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Kids Content, Explainer | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Drama, Mythology / Ancient Epic, Sci-Fi, Family, Action  
**Avoid when:** The contract is usually tightened until every clip comes out identical and cold with no development. The exception is when change is part of the story, and then the permitted change is written out: the wardrobe after the battle, or the light moving from dawn to noon.  
**Prompt:** `brief: keep the approved character, wardrobe, lens, light direction, grade and object count from the reference sheet, and change only the named action`  
`control.generative_continuity`

### The Geography Check

**Also called:** spatial clarity check, where is everyone check  
**What it is:** One question asked of a scene once it is assembled: does the audience know where each person stands relative to the others and to the place. It is measured by an establishing shot or a substitute for it, and by positions staying consistent on screen.  
**Effect on the audience:** With the geography clear, the viewer is free to follow the feelings. Without it they spend the scene trying to assemble the room in their head and miss the dialogue.  
**Used for and where it works best:** After assembling any scene with three or more people, and any fight, chase or battle. The substitute for an establishing shot is a camera move that links two positions, or a character crossing from one to the other inside a single shot. Re-establish after every large change of position.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Docudrama / Reenactment, AI-Generated Clip, Short Film, Trailer / Teaser | genres: Action, War, Crime / Procedural, Thriller / Suspense, Martial Arts / Wuxia, Fantasy / Epic, Chase, Mystery / Whodunit, Samurai / Chanbara  
**Avoid when:** It is usually overdone until every scene in the film opens on a wide and the rhythm turns predictable. The exception is when confusion is the intent, in a horror beat or a blast where losing the geography is the experience.  
**Prompt:** `brief: after the assembly, ask whether the audience can draw the room from memory, and if not add one linking move, one crossing action or one wide before the scene turns`  
**Yields to:** `sig.chaos_handheld` — Losing the geography is the experience, a horror beat or a blast.  
`control.geography_check`

### The Eyeline and Axis Check

**Also called:** line check, screen direction check, 180 check  
**What it is:** Matching each character's look direction and look height to the position of the person they are looking at, and confirming the camera stayed on one side of the line between them or that the crossing was shown. The check covers direction and height together, not direction alone.  
**Effect on the audience:** When the eyelines match, the viewer believes the two are in the same room even when they were filmed on different days. A wrong eyeline leaves them talking into empty air.  
**Used for and where it works best:** Before shooting any shot and reverse pair, when assembling a two camera interview, and in generated clips where every shot is requested separately. Write into the request that the character looks off frame to the left, then ask for the opposing shot looking right.  
**Best in:** formats: Feature Film, Drama Series Episode, Interview / Video Podcast, Anime (Japanese 2D), AI-Generated Clip, Docudrama / Reenactment, Sitcom / Multi-Cam Comedy, Soap Opera / Telenovela, Short Film | genres: Drama, Crime / Procedural, Legal Drama, Romance, Thriller / Suspense, Mystery / Whodunit, Family Drama, Medical Drama  
**Avoid when:** The mistake is usually patched with a quick cutaway, which hides it without fixing it and leaves the viewer uneasy. The exception is a deliberate break at the moment a scene turns, where the crossing is shown or a neutral on axis shot carries the move.  
**Prompt:** `brief: map the two positions, fix the look direction and look height for each side, keep the camera on one side of the line, and show the crossing if the line is broken`  
**Yields to:** `angle.crossing_the_line` — A deliberate break at the moment the scene turns.  
`control.eyeline_axis`

### The Sound and Picture Handshake

**Also called:** who leads the cut, audio lead check  
**What it is:** Deciding who leads each cut: whether the sound arrives before the picture, continues after it, or both change on the same frame. It is decided cut by cut rather than once for the whole scene.  
**Effect on the audience:** Sound arriving early pulls the viewer forward into anticipation, sound lingering after the cut keeps them in the previous scene and leaves a residue. A simultaneous cut reads as a decision.  
**Used for and where it works best:** When assembling any dialogue scene or any scene to scene move, and in trailers where sound drives the whole build. Ask of every cut whether the ear or the eye goes in first. In a fast edit, letting the sound lead by a few frames makes the cut feel softer.  
**Best in:** formats: Feature Film, Trailer / Teaser, Drama Series Episode, Documentary Feature, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary, Video Essay, Commercial / TVC | genres: Drama, Thriller / Suspense, Horror, Heritage (civilisation-focused), Crime / Procedural, Musical, War, Mystery / Whodunit  
**Avoid when:** The same treatment is usually applied to every cut, so the scene turns uniformly soft with no joints. The exception is when total softness is intended, in a memory or a dream that wants no edges.  
**Prompt:** `editor: mark for each cut whether the audio leads, trails or lands with the picture, then place the picture cut against that decision`  
`control.sound_picture_handshake`

### The Prompt Anatomy Check

**Also called:** prompt completeness check, request audit  
**What it is:** Checking that a generation request carries all of its parts: the subject, the action, the camera start, path and end, the light and its direction, the material and the place, the ratio, and what you do not want. Anything missing is filled in by the model as it pleases. For an image-to-video request, a visible fact the approved keyframe already carries counts as present and is not restated in the motion prompt (`ai.image_to_video`).  
**Effect on the audience:** A complete request gives a repeatable result. An incomplete one gives something attractive once and something entirely different the next time.  
**Used for and where it works best:** Before sending any image or video generation request, and above all in heritage work where a wrong garment or a wrong wall destroys the credibility. Read the request back and confirm each is there: who, doing what, camera from where to where, light from which side, in what place, at what ratio, and what is excluded.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Kids Content, Trailer / Teaser, Explainer, Product Video / Motion Design | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Mythology / Ancient Epic, Drama, Sci-Fi, Family, Action  
**Avoid when:** The request usually grows until it contradicts itself, the instructions compete and the most important one gets lost. The exception is a genuinely complex shot, where the request is split into ordered layers instead of one long sentence.  
**Prompt:** `brief: read the request back and confirm it names the subject, the action, the camera start path and end, the light direction, the location, the ratio and the exclusions`  
`control.prompt_anatomy`

### The Count Check

**Also called:** number check, quantity lock  
**What it is:** Stating the exact number of everything countable in the scene: how many people, how many candles, how many columns, how many hands on the table. The count is written as a figure and held across every clip in the sequence.  
**Effect on the audience:** A count that changes between shots reads as a continuity error even when the viewer does not consciously catch it, and it leaves a feeling that something is off.  
**Used for and where it works best:** In every generative request with more than one person or object, and in preparing any scene that will be filmed across several days. In heritage work: the number of columns in the hall, the guards at the gate and the arches, because the building recurs across many shots. Also write a count of zero for what must not appear.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, 3D CG Animation, Commercial / TVC, Product Video / Motion Design, Anime (Japanese 2D), Kids Content, Explainer, Trailer / Teaser | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Fantasy / Epic, Family, Science / Educational, War, Preschool / Early Learning  
**Avoid when:** The request is usually loaded with counts for things that are never visible, so precision is spent outside the frame. The exception is when the background is the subject, a row of statues or an army that has to stay the same size.  
**Prompt:** `brief: state every visible count as a figure, hold it across all clips, and add a count of zero for anything that must not appear`  
`control.count_check`

### The Safe Area Check

**Also called:** title safe check, UI overlay check  
**What it is:** Confirming that the type and the important elements stay clear of the frame edges and of the zones covered by the platform interface: the handle, the caption and the buttons at the bottom, the icons down the side. The check is run on the platform itself, not inside the edit software.  
**Effect on the audience:** Readable type delivers the message, while clipped or covered type reads as carelessness and lowers trust in the account or the brand.  
**Used for and where it works best:** Before exporting any vertical video or anything with titles, and before delivering an advert that will run on several platforms. Leave a margin at the top and the bottom of the frame, lift the subtitles off the edge, and review the result on a phone before publishing.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Commercial / TVC, Product Video / Motion Design, Explainer, Title Sequence / Opening Credits, Kids Content, Trailer / Teaser, Corporate / Training | genres: Comedy, Family, Science / Educational, Heritage (civilisation-focused), Drama, Preschool / Early Learning, Musical, True Crime  
**Avoid when:** Following the margins too literally usually stacks everything into the middle and weakens the composition. The exception is a piece made for one known screen, where the full frame can be used with confidence.  
**Prompt:** `brief: keep titles and key action inside the safe margins, allow for the platform interface at the bottom and the side, and review the export on the target device`  
`control.safe_area`

### The Frame Rate and Delivery Check

**Also called:** delivery spec check, codec and rate check  
**What it is:** Fixing the frame rate, the resolution, the file format and the colour space at the start of the project, and confirming every source agrees with them. Generated, archive and filmed material usually arrive at different rates.  
**Effect on the audience:** A frame rate mismatch shows up as a light stutter in movement, a fault the viewer registers as cheapness without knowing what caused it.  
**Used for and where it works best:** At the start of any project that mixes sources: filmed material, generated clips, archive and graphics. Conform everything to one rate before the edit rather than after, and export a short test and watch it on the delivery screen before finishing the whole piece.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, AI-Generated Clip, Drama Series Episode, Commercial / TVC, Music Video, Corporate / Training, Documentary Series, Feature Film | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Drama, Verite / Observational, True Crime, War  
**Avoid when:** The conversion is usually left to the edit software, which invents blended frames that ruin the edges in movement. The exception is when the stutter is wanted, as with archive material whose old feel is being preserved.  
**Prompt:** `brief: fix one frame rate, resolution, format and colour space for the project, conform every source to them before editing, and test the export on the delivery screen`  
**Yields to:** `doc.archive_format_frame` — Archive whose old feel is preserved instead of conformed.  
`control.frame_rate_delivery`

### The Colour Grade Lock

**Also called:** look lock, grade consistency check  
**What it is:** Fixing one colour reference for the whole piece: skin tone, light temperature, shadow colour and the saturation ceiling, then matching every shot to it before it is approved. The reference you match against at review is an approved still image, not a verbal description; the written light-and-colour line of `ai.colour_grade_lock` is what goes into the prompts, and it is checked against this frame, not the other way round.  
**Effect on the audience:** Colour consistency makes the shots read as one piece. A slight difference between two adjacent clips makes the viewer feel a dissonance before they can name its source.  
**Used for and where it works best:** In any piece assembling shots from different sources, days or models, and in a series whose episodes have to feel like one world. Approve one reference frame at the start and place it beside every new shot at review instead of comparing against memory.  
**Best in:** formats: AI-Generated Clip, Heritage / Historical Documentary, Drama Series Episode, Feature Film, Music Video, Commercial / TVC, Documentary Series, Trailer / Teaser, Brand Film | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Fantasy / Epic, Noir / Neo-Noir, Thriller / Suspense, Sci-Fi, War  
**Avoid when:** The same grade is usually applied to scenes set in different times and places, erasing the difference between day and night. The exception is when the flattening is intended, in a piece that wants to feel like one continuous memory.  
**Prompt:** `brief: approve one reference frame for skin tone, light temperature, shadow colour and saturation, then match every shot beside it before the shot is signed off`  
`control.grade_lock`
