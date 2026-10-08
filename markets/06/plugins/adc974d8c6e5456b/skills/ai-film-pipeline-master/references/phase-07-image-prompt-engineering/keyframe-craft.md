# Keyframe Craft, Single and Paired

14 cards. Also in the other stage: a shot has a frame too. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Settle the Frame Before the Motion

**Also called:** the keyframe selector, how many frames does this shot need, the still side of the handoff  
**What it is:** The card at the head of the `kf.` shelf. It asks the three questions this shelf's own cards keep asking — **how many frames does this shot need, what will the video stage refuse to invent, and does this frame have to serve anything besides its own clip** — and hands back a named shortlist for each answer. The axes were read off the shelf's `Avoid when:` lines and the conditions its cards use to redirect a reader. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the still was designed against the clip it is about to become, rather than admired on its own and then handed over.  
**Used for and where it works best:** Answer question one **before you write the still prompt**, because it decides how many prompts you are writing. Answer question two before you accept the still, because it is the list of things that will not improve later and will usually get worse. Answer question three before you generate, because two of its answers mean the image you are making is not one image. **This shelf stops where the clock starts**: everything here is settled while nothing is moving, and the moment the answer would change once time runs, the question belongs to the video-directing shelf and not to this one.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The shot is a direct text-to-video pass and nothing about it was researched.** `kf.complexity_first` concedes that case in its own `Avoid when:` — a simple shot generated straight to video is adequate and faster, and a map that insists on a still stage is selling overhead. Also avoid it where the still is the deliverable and no clip follows; every axis here is phrased against a motion stage that is not going to happen, and a poster asked these three questions gets three wrong answers. And **distrust axis two above all the others**: it is the axis this shelf never argues about with itself, four of its five cards are reached by nothing at all, and the fifth is reached only by two named failures arriving from outside — so the map is stating that population, not routing it.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — How many frames does this shot need: one, a pair, or a chain?**
Every internal argument on this shelf is this one. *"Two simultaneous changes; chain two clips, one change each"* (`kf.readable_delta`). *"Shot inside the engine ceiling; start and end frames serve better"* (`kf.chain_frame`). *"The emotional turn must happen on camera"* (`kf.loaded_expression`). *"The same image must also work as a poster"* (`kf.motion_headroom`). *"Small budget; one deliberately asymmetric frame serves both"* (`kf.role_separation`). Asked first because it is the only question on the shelf whose answer changes how many things you generate, and because the cards disagree with each other about it in both directions — the chain card and the pair card each name the other as the better answer under a stated condition, which is what a real fork looks like.

**Axis 2 — What will the video stage refuse to invent, so it has to be in the still already?**
Stated as facts about engines rather than as preferences. *Asking the video engine to invent a crowd, an intricate costume, precise architecture or a specific face* (`kf.complexity_first`). *The video stage will not fix a wrong hand and usually makes it worse* (`kf.contact_points`). *Camera movement across a flat plate produces a pan across a picture, not parallax* (`kf.parallax_staging`). *The light rotates between shots unless the key is named and repeated* (`kf.light_state`). *A subject centred in a tight crop has nowhere to go, so the generation pushes the camera or invents a wider scene* (`kf.motion_headroom`). This is the axis that justifies the shelf existing at all.

**Axis 3 — Does this frame have to serve anything besides its own clip?**
Four answers and three of them cost you a second generation. *The same image must also work as a poster* (`kf.motion_headroom`, to `kf.role_separation`). *Several ratios are needed* (`kf.native_ratio`, out to the reframe control). *Any multi-shot sequence in one location, where the joins would expose a lighting change* (`kf.light_state`). *The join becomes invisible because it is literally the same image* (`kf.chain_frame`). Asked last because it is the only axis that can turn a settled answer to axis one back into an open question.

---

**The map**

**Axis 1 — how many frames**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One — the clip starts here and the engine takes it from there** (seven) | `kf.motion_headroom` · `kf.complexity_first` · `kf.weak_engine_anchor` · `kf.native_ratio` · `kf.parallax_staging` · `kf.contact_points` · `kf.loaded_expression` |
| **A pair — you fix both ends and the engine fills the middle** (two) | `kf.first_last_pair` · `kf.readable_delta` |
| **A chain — the shot is longer than one generation** (three) | `kf.chain_frame` · `kf.settled_join` · `kf.light_state` |
| **Two frames that are not a pair — the same moment made twice for two different jobs** (one) | `kf.role_separation` |

**Axis 2 — what the video stage will not invent**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Detail and population — it will not build what was never there** (two) | `kf.complexity_first` · `kf.weak_engine_anchor` |
| **Contact and performance — it will not fix a wrong hand or load a blank face** (two) | `kf.contact_points` · `kf.loaded_expression` |
| **Depth and room to move — it will not manufacture either from a flat crop** (two) | `kf.parallax_staging` · `kf.motion_headroom` |
| **Continuity — it will not hold the light or the shape of the frame across shots** (three) | `kf.light_state` · `kf.native_ratio` · `kf.role_separation` |
| **The path between two states — it will interpolate, but it will not decide** (four) | `kf.first_last_pair` · `kf.readable_delta` · `kf.chain_frame` · `kf.settled_join` |

**Axis 3 — who else is this frame for**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Nobody — this clip only** (six) | `kf.complexity_first` · `kf.weak_engine_anchor` · `kf.contact_points` · `kf.loaded_expression` · `kf.parallax_staging` · `kf.motion_headroom` |
| **The next clip** (four) | `kf.chain_frame` · `kf.settled_join` · `kf.first_last_pair` · `kf.readable_delta` |
| **The rest of the sequence** (one) | `kf.light_state` |
| **Something that is not a clip at all** (two) | `kf.role_separation` · `kf.native_ratio` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and on this shelf it is normally one or two cards wide.*

---

**Where this shelf stops and the video-directing shelf starts**

The two shelves carry three pairs of cards that look like duplicates and are not. `kf.first_last_pair` and `ai.first_last_frame` both describe giving an engine two images. `kf.native_ratio` and `ai.aspect_native` both say generate at the delivery ratio rather than cropping to it. `kf.chain_frame` and `ai.scene_bridge_end_to_start` both describe using one clip's last frame as the next clip's first — and both forbid the same thing in almost the same words, that the frame must be generated from the references and never extracted from the finished clip, because the extracted frame carries compression and motion blur that the engine reads as the intended look and continues from, so each link degrades the next.

**They agree. That makes them a boundary, not a contradiction.** The line they draw is a clock:

> **If the answer is settled while nothing is moving, it belongs to `kf.`. If the answer changes once time starts running, it belongs to the video-directing shelf.**

Read that against the three pairs and it holds each time. `kf.first_last_pair` composes two frames and then hands the motion off by name, conceding that the prompt still has to write the kinetic path between them — it designs the boundary states and declines to design the journey. `ai.first_last_frame` is the journey. `kf.native_ratio` decides the shape of a composition; `ai.aspect_native` decides what the engine is asked to render and what the platform interface will sit on top of. `kf.chain_frame` decides what the joining image must contain; the bridge card decides what the engine may be fed. The same subject, the two sides of one handoff — which is also why every outward edge from this shelf lands on a conditioning, control, cut, light or motion card, and never on a second still.

**The practical test, when a new card could go either way:** ask whether you could satisfy it with a still and no engine at all. A hand that closes properly round a staff can be judged in a single frame; a hand that closes properly *while the arm swings* cannot. The first is `kf.`. The second was never this shelf's.

---

**The default, and the one against it**

**The most-reached card on this shelf is `kf.contact_points`, and it is not the default — it is a repair destination.** Both edges into it arrive from outside the shelf and both start at a named failure: a garbled-hands rescue procedure, and a limb-drift failure mode from the video side. Both fire on one condition — *the hands came back wrong*. **A repair edge points into the map from outside it rather than across it**, and a card reached twice by two failures for one reason is where you land after a mistake, not where you start.

**The measured default is `kf.first_last_pair`, with `kf.readable_delta` making it work.** Two cards send a reader to the pair for two genuinely different reasons — *the shot is inside the engine ceiling, so a start and an end frame serve better than a chain* (`kf.chain_frame`), and *the emotional turn has to happen on camera rather than in the still* (`kf.loaded_expression`) — and the card's own text says it is the dominant control method on current engines. A card reached twice for two reasons is a default. `kf.readable_delta` is bound to it because a pair with more than one change between its frames is not a pair, it is a smear.

**The stated runner-up, so the ranking is not silent:** `kf.motion_headroom`, reached twice for two distinct conditions — a budget too small for two images, and a start frame that will be animated laterally — one from this shelf and one from the composition shelf. It is second because it answers a narrower question: it is the right card only once you already know the clip moves sideways.

**The one against it is `kf.complexity_first`.** Nothing routes to it, and it inverts the shelf's economics. The rest of this shelf treats the still as a cheap, well-aimed starting position and spends the budget on the motion; this card spends everything on the still — the whole crowd on the steps, every figure placed, the architecture complete — and reduces the engine to a translator that moves what it was given and invents nothing. Its only stated cost is over-investment on a shot that was simple anyway. **Its near cousin is `kf.weak_engine_anchor`**, which reaches the same conclusion from the opposite premise: not that the still deserves the work, but that the image engine available is simply better than the video engine available, which its own text calls the normal condition.

---

**The unasked**

**Seven of the thirteen cards are the target of no pair condition anywhere in the package.** By id:

`kf.readable_delta` · `kf.settled_join` · `kf.complexity_first` · `kf.weak_engine_anchor` · `kf.light_state` · `kf.parallax_staging` · `kf.loaded_expression`

**And the shape of that list is the finding.** Four of the five cards under axis two are on it, and the fifth, `kf.contact_points`, is reached **only from outside the shelf, by two named failures**. So: nothing inside this shelf ever sends a reader to a card about what the engine cannot do. Every internal edge on this shelf is frame arithmetic — one frame, two frames, a chain, two frames that are not a pair — and not one of them is about what goes inside a frame. **The shelf argues with itself about counting and never about content.**

That has a consequence worth stating plainly. The only route in the package to *put the hands right* arrives after the hands came out wrong. A reader who never generates a broken hand is never told to think about contact at all, and `kf.contact_points` calls itself the single highest-value check before sending a still into a video stage. **A check that is only reachable by failing it is not a check, it is a diagnosis.** The same is true of `kf.light_state`, which prevents a lighting rotation that nothing in the package will route you to prevent, and of `kf.parallax_staging`, which prevents a flat pan the same way.

The second thing the list shows: **the whole engine-capability region is unasked, and it is the region that dates fastest.** `kf.weak_engine_anchor` exists because the best image engine is substantially better than the best video engine; `kf.chain_frame` names a clip ceiling of about ten seconds and says a chained take is now the rare case; `kf.complexity_first` assumes the video stage cannot invent a crowd. Those are measurements, and every one of them is a measurement of a moving target. The card this shelf wants and does not have is the one that says **the still-first decision has a date on it**: it is not a craft principle, it is an arbitrage between two engines, and the day the video engine catches up, half this shelf becomes overhead rather than technique. Nothing here carries that date, and nothing routes a reader to check it.

`kf.frame_before_motion`

---

### Motion Headroom

**Also called:** leave-room composition, travel space, movement allowance  
**What it is:** Composing the start frame so the space the action will move into is already in frame and already empty. A subject centred in a tight crop has nowhere to go and the generation either pushes the camera or invents a wider scene.  
**Effect on the audience:** Motion that develops inside a stable frame rather than motion that drags the camera along behind it. The shot feels directed rather than chased.  
**Used for and where it works best:** Every image-to-video start frame with lateral or forward movement. Most valuable in walk-ins, entrances, reveals and any shot where a subject crosses the frame. Best in commercials, brand films and vertical short-form where the first second decides whether the viewer stays.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Commercial / TVC, Brand Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually weakens the still when the same image must also work as a poster, because the empty side that serves the motion reads as dead space in a static frame. The exception is a deliberate asymmetry that serves both, with the weight carried by the subject rather than by the centre.  
**Prompt:** `still frame, the figure stands at the right third facing left, the left half of the frame open corridor, camera locked, composed so the figure can cross into the empty space`  
**Yields to:** `kf.role_separation` — The same image must also work as a poster.  
`kf.motion_headroom`

### First and Last Frame Pair

**Also called:** start-end pair, bookend frames, dual-frame conditioning  
**What it is:** Generating two images, the exact opening and the exact closing state, and handing both to the engine, which interpolates between them. The two frames fix the boundary states, but the prompt still writes the kinetic path between them (`cond.start_end_frame_pair`); motion left to interpolation alone morphs and drifts.  
**Effect on the audience:** The clip lands where it was meant to land. Ordinary image-to-video controls only the beginning; the end is whatever the model drifts into.  
**Used for and where it works best:** Transformations, reveals, loops, any shot that has to chain into the next one, and any case where the final composition matters as much as the first. Best in commercials, title sequences and music video, and it is the dominant control method on current engines.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Commercial / TVC, Music Video, Title Sequence / Opening Credits, Brand Film, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually produces a morph rather than a movement when the two frames are too far apart, because the engine has no physical path between them and invents one. The exception is when the morph is the intent, such as a transformation or a dream logic.  
**Prompt:** `start frame: the hall is empty, dust in the shaft of light. end frame: the same hall, same camera, the figure now standing in the shaft, dust disturbed around them`  
**Yields to:** `cond.start_end_frame_pair` — on every paired-frame generation: the prompt still writes the kinetic path between the two frames.  
`kf.first_last_pair`

### The Difference Is the Direction

**Also called:** readable delta, one-change rule for frame pairs  
**What it is:** Designing a start and end pair so exactly one thing has changed, and that change describes the motion unambiguously. Camera, light, wardrobe and background stay identical between the two frames unless their change is itself the shot.  
**Effect on the audience:** Clean interpolation. When several attributes differ at once, the engine distributes the change across all of them and everything drifts together.  
**Used for and where it works best:** All paired-frame work, and the first thing to check when a dual-frame generation comes back as a smear. Best in commercials, product motion and title work where the move must be exact.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Commercial / TVC, Music Video, Product Video / Motion Design, Title Sequence / Opening Credits, Brand Film, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually under-serves a shot that genuinely contains two simultaneous changes, such as a subject turning while the light shifts. The exception is generating that shot as two chained clips, one change each, and joining them.  
**Prompt:** `between the two frames only the head position changes, identical camera, identical light, identical wardrobe, identical background`  
**Yields to:** `kf.chain_frame` — Two simultaneous changes; chain two clips, one change each.  
`kf.readable_delta`

### End Frame as the Next Start

**Also called:** chain frame, handoff frame, clip stitching  
**What it is:** Composing the closing frame of one clip so it is usable as the opening frame of the next, and then using it as exactly that. The join becomes invisible because it is literally the same image.  
**Effect on the audience:** A shot longer than any single generation, with no visible seam at the joins. This is how an action longer than any one clip survives the engine's clip ceiling.  
**Used for and where it works best:** Long takes assembled from several generations, developing camera moves, and any sequence where the clip ceiling of the engine is shorter than the shot. Best in brand films, documentary sequences and music video.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Brand Film, Music Video, Commercial / TVC, Documentary Feature, Heritage / Historical Documentary, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** **The chain frame is always generated from the references, never extracted from the
finished clip.** An extracted frame carries the clip's compression and motion blur; the engine reads
that softness as the intended look and continues from it, so each link degrades the next. Compose
and generate the chain frame as its own image, exactly as you would any keyframe. Note also that
current engines reach about ten seconds and a real shot rarely runs longer without a cut, so a
chained take is now the rare case rather than the normal one — and where it is genuinely needed, a
start keyframe and an end keyframe from the references usually serve better than a chain.  
**Shelf life:** dated — review 2027-03. The ten-second engine ceiling is a product limit, not a craft fact; check the engine's own current page before relying on it.  
**Prompt:** `this frame closes clip 2 and opens clip 3 — generate it from the reference sheets, not from the previous clip. A stable held moment with the subject settled, no limb mid-swing, no motion blur`  
**Yields to:** `kf.first_last_pair` — Shot inside the engine ceiling; start and end frames serve better.  
`kf.chain_frame`

### Settled Pose at the Join

**Also called:** stable handoff, no-mid-motion rule  
**What it is:** Making sure any frame that will be used as a chain point shows the subject at rest or at the top of a movement, never mid-stride or mid-gesture. A frozen mid-motion pose carries no information about which direction the motion was going.  
**Effect on the audience:** The next clip continues rather than restarting. A mid-stride handoff frequently produces a subject who takes the same step twice or reverses direction.  
**Used for and where it works best:** Every chained generation, and the first fix to try when a joined sequence stutters at the seam. Best in brand films, music video and any long take built from several clips.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Brand Film, Music Video, Commercial / TVC, Documentary Feature, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually costs energy in a fast action sequence where every frame is mid-motion by design. The exception is placing the join inside a cut rather than inside a continuous move, where a hard cut hides what a settled pose would have protected.  
**Prompt:** `end frame: the figure has completed the turn and is still, weight on both feet, hands at rest, eyes on the door`  
**Yields to:** `cut.hard` — Fast action; put the join inside a cut.  
`kf.settled_join`

### Complexity Belongs in the Frame

**Also called:** front-load the difficulty, still-first complexity  
**What it is:** Putting anything hard, a crowd, an intricate costume, many objects, precise architecture or a specific face, into the generated still where it can be regenerated cheaply until correct, rather than asking the video engine to invent it.  
**Effect on the audience:** Complex scenes that hold together. A video engine asked to invent a crowd produces a shifting crowd; the same crowd rendered once as a still and then animated stays put.  
**Used for and where it works best:** Crowd scenes, processions, battles, markets, detailed heritage reconstruction, anything with architecture, and any shot whose subject took research to get right. Best in heritage documentary, epic work and brand films.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Heritage / Historical Documentary, Documentary Feature, Brand Film, Commercial / TVC, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, War, Drama, Verite / Observational, Fantasy / Epic  
**Avoid when:** It usually over-invests when the shot is simple and a direct text-to-video pass would have been adequate and faster. The exception is a series where every shot goes through a still stage for consistency, and the uniformity is worth the overhead.  
**Prompt:** `generate the full scene as a still first: the forty figures on the ziggurat steps, each in place, the architecture complete, the animation stage will only move them, not invent them`  
`kf.complexity_first`

### Weak-Engine Anchor

**Also called:** still rescue, image-to-video fallback  
**What it is:** Using a generated still as the start frame specifically because the available video engine is not strong enough to build the scene from text. The image carries the quality and the engine only has to add motion.  
**Effect on the audience:** Output far above what the video engine would produce alone, because the hardest half of the work was done where the tools are strongest.  
**Used for and where it works best:** Any production where the best available image engine is substantially better than the best available video engine, which is the normal condition. Also the standard route for complex or researched scenes. Best in heritage work, brand films and any commissioned piece.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Heritage / Historical Documentary, Brand Film, Commercial / TVC, Music Video, Documentary Feature, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually constrains the shot when the still locks a composition the motion then wants to leave. The exception is combining it with motion headroom, so the anchor and the movement are designed together rather than in sequence.  
**Prompt:** `the still carries the scene quality; the video stage adds only a slow push and the movement of the cloth`  
`kf.weak_engine_anchor`

### Aspect Ratio Set at the Still

**Also called:** native ratio discipline, no-crop rule for stills  
**What it is:** Generating the keyframe at the delivery ratio natively rather than producing a wider frame and cropping to vertical. The composition is designed for the shape it will be seen in.  
**Effect on the audience:** Proper vertical or square composition instead of a cropped horizontal with the head of the subject near the top edge. A cropped frame also carries fewer pixels into the video stage.  
**Used for and where it works best:** All vertical and square delivery, which is most social and short-form work. Any project delivering to more than one ratio should generate each natively rather than crop from one master. Best in vertical short-form, social cards and thumbnails.  
**Best in:** formats: Generated Keyframe Feeding Video, Vertical Short-Form (Reels, Shorts, TikTok), Thumbnail / Social Card, Poster / Static Design, Commercial / TVC, AI-Generated Clip, Vertical Micro-Drama, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually costs time when several ratios are needed and the subject allows a safe centre. The exception is a deliberate multi-ratio master built with protected zones, designed from the start to survive its crops.  
**Prompt:** `generate natively at 9:16, composed for vertical, the figure occupying the lower two thirds, the architecture rising through the upper third`  
**Yields to:** `control.aspect_reframe` — Several ratios needed; one planned master, shared action area.  
`kf.native_ratio`

### Light State Declared for Continuity

**Also called:** lighting lock, key direction hold  
**What it is:** Naming the direction, quality and colour temperature of the key light in the keyframe prompt, and repeating the same statement in every frame of the sequence, so the light does not rotate between shots.  
**Effect on the audience:** A scene that stays in one place at one hour. Drifting key direction is one of the fastest ways a generated sequence stops reading as a real space.  
**Used for and where it works best:** Any multi-shot sequence in one location, and any chained clip set where the joins would expose a lighting change. Best in heritage documentary, drama sequences and brand films.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Brand Film, Heritage / Historical Documentary, Documentary Feature, Commercial / TVC, Music Video, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually fights the story when the passage of time is the point and the light is supposed to move. The exception is declaring the change of light as deliberately as its constancy, with each shot naming its own hour.  
**Prompt:** `key light from camera left, low and warm, hard shadows falling right, identical in every frame of this sequence`  
**Yields to:** `light.light_change` — Time is passing and the light is meant to move.  
`kf.light_state`

### Depth Staged for Parallax

**Also called:** layered depth, parallax preparation  
**What it is:** Composing the still with distinct foreground, middle and background elements so that camera movement in the video stage produces real parallax instead of a flat pan across a picture.  
**Effect on the audience:** Depth that behaves. Without separated layers, a push on a flat still reads as a zoom on a photograph, which is exactly what it is.  
**Used for and where it works best:** All shots with camera movement, particularly pushes, tracks and crane moves. Essential for establishing shots that need to feel like a place rather than a painting. Best in heritage work, travel films and documentary openings.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Documentary Feature, Brand Film, Music Video, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually adds clutter in a tight portrait or a graphic composition where flatness is the design. The exception is a deliberately flat frame animated with light or texture rather than with camera movement.  
**Prompt:** `foreground: the carved doorframe at the left edge, close and dark. middle: the figure at the threshold. background: the lit courtyard and the wall beyond, three clearly separated depth planes`  
**Yields to:** `ai.motion_brush` — Flat graphic frame; animate elements, not the camera.  
`kf.parallax_staging`

### Hands and Contact Points Resolved

**Also called:** contact discipline, grip lock  
**What it is:** Making sure every point where the subject touches something, a hand on a hilt, a foot on a step, a shoulder against a wall, is correct and unambiguous in the still, because the video stage will not fix it and usually makes it worse.  
**Effect on the audience:** Objects that are held rather than hovering. A hand that is approximately on a handle in the still becomes a hand that passes through the handle in motion.  
**Used for and where it works best:** Any shot where the subject holds, carries, leans or climbs, and the single highest-value check before sending a still into a video stage. Best in heritage reconstruction, product work and action sequences.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Heritage / Historical Documentary, Product Still / Packshot, Commercial / TVC, Brand Film, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually costs regenerations when the contact is small in frame and will not be visible at delivery size. The exception is a shot that will be seen large or held long, where the audience has time to find the error.  
**Prompt:** `the right hand closes fully around the staff with the fingers wrapped and the thumb across, the staff base planted on the stone with the shadow confirming contact`  
`kf.contact_points`

### Expression Held, Not Neutral

**Also called:** performance in the still, loaded face  
**What it is:** Giving the keyframe a specific facial and bodily state that the coming motion will develop from, rather than a neutral resting face. The still carries the beat before the action.  
**Effect on the audience:** Performance rather than animation. A neutral face animated produces a person who begins to feel something for no reason; a loaded face animated produces a person continuing to feel it.  
**Used for and where it works best:** Any character shot with emotional content, dialogue frames and reaction frames. Best in drama, biography and any piece where the face carries the story.  
**Best in:** formats: Generated Keyframe Feeding Video, AI-Generated Clip, Brand Film, Commercial / TVC, Music Video, Documentary Feature, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: Drama, Historical / Biopic, Tragedy, Thriller / Suspense, Romance, Comedy, Heritage (civilisation-focused)  
**Avoid when:** It usually over-commits when the emotional turn of the shot is supposed to happen on camera and the still has already spent it. The exception is designing the pair, where the start frame holds the state before and the end frame holds the state after.  
**Prompt:** `the jaw is set, the eyes already on the door, breath held, not a neutral expression, the moment just before deciding`  
**Yields to:** `kf.first_last_pair` — The emotional turn must happen on camera.  
`kf.loaded_expression`

### Poster Frame Versus Start Frame

**Also called:** dual-purpose warning, still-role separation  
**What it is:** Recognising that an image built to open a clip and an image built to stand alone are different images, and generating them separately rather than trying to serve both from one file.  
**Effect on the audience:** Both artefacts work. A start frame reused as a poster reads as under-composed; a poster reused as a start frame gives the motion nowhere to go.  
**Used for and where it works best:** Any project delivering both a film and its key art, which is most commissioned work. Best in campaigns, brand films and anything with a social rollout beside the film.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Thumbnail / Social Card, Commercial / TVC, Brand Film, Music Video, Title Sequence / Opening Credits, Portrait Photography, Landscape Photography, Street Photography, Still Life Photography, Travel Photography, Sports Photography, Documentary Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually over-produces on a small piece where one adequate image beats two good ones inside the budget. The exception is when the poster is the primary deliverable and the film supports it, where the poster is generated first and the start frame is derived from its world.  
**Prompt:** `generate two frames of this moment: one composed closed and balanced for the poster, one composed with left-side travel space for the clip`  
**Yields to:** `kf.motion_headroom` — Small budget; one deliberately asymmetric frame serves both.  
`kf.role_separation`
