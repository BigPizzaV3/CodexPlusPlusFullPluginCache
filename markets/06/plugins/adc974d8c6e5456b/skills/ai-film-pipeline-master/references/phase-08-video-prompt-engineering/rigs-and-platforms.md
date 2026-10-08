# Rigs and Camera Platforms

52 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name the Support Before the Move

**Also called:** the rig selector, support before move, what is the camera standing on  
**What it is:** The card at the head of the `rig.` shelf. It does not describe a move. It asks the three questions the shelf's own pair graph asks over and over — **what is holding the camera up, is the camera's body allowed to be felt, and what does this day actually afford** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the thirty-six `Yields to:` conditions the cards carry, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the rig that does reach the screen was chosen against the floor, the schedule and the crew list, rather than picked because it was the one in the van.  
**Used for and where it works best:** Answer the three questions **in order and out loud, in one sentence each, before you open the shelf.** Question one is the only hard partition on this shelf — **a shot is on one support at a time** — so it eliminates by geometry rather than by taste, and the other two narrow what is left to two or three cards. If you cannot answer question one, you do not have a rig problem, you have a blocking problem, and the shot is not designed yet. Where two answers fight for one take, that is not two rigs on one shot, it is `rig.handoff`, and it is the only card here that says so.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The support is already fixed by something outside the shelf** — a volume already booked, a vehicle you have no permit to tow, a site that allows no rigging — because then the rig is a given and what you are choosing is a move, which is another shelf's decision. Also **distrust axis one whenever your honest answer is its first value**: half the shelf stands on the floor, so on an ordinary interior this map has two questions left and is doing rather less than half the work it does on a road, in the air or in the water. And the deepest warning is about the graph the map is built on: **every condition on this shelf is a subtraction** — no operator, no permit, no budget, no level floor, no rigging day — so the map is excellent at telling you what to fall back to and close to useless at telling you what to reach for. Read it as a map of retreats and choose the ambition yourself.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — What is holding the camera up, and can that thing be in this location?**
Asked first because it is the only question on the shelf whose answers cannot overlap, and because it is what the pair graph is actually made of. The graph is not one web: it is one large component and six islands, and the islands are exactly these regions — the camera in a car never yields to the camera in the air, and neither yields to the camera on rails. Eleven conditions turn on whether the support can physically be there: *"On location or uneven ground, where a ped cannot roll"* (`rig.pedestal`), *"Practical interiors and tight spaces that cannot take laid track"* (`rig.dolly_track`), *"A real location with no purpose-built set"* (`rig.rail_through_set`), *"A small or narrow location, no multi-cable rigging day"* (`rig.cable_cam`), *"Flying indoors or close to people, guarded props needed"* (`rig.fpv_drone`), *"Crew, sound and controlled light will not fit in the car"* (`rig.vehicle_interior`), *"Food shots, where downwash moves the set"* (`rig.micro_fpv_indoor`), *"Close sound must be recorded; no noise or downwash"* (`rig.drone`), *"Following someone walking, beyond a slider's travel"* (`rig.slider`), *"The move needs more height and reach than a jib has"* (`rig.jib`), *"A heavy camera package, or a floor needing laid track"* (`rig.doorway_dolly`).

**Axis 2 — Is the camera's own body allowed to be felt, and is the shake the content?**
Nine conditions turn on this, and they are stated as facts about the image rather than as feelings about it: *"Scenes of energy or pursuit, where stillness reads cold"* (`rig.tripod_locked`), *"The scene needs human presence, not machine smoothness"* (`rig.gimbal`), *"A clean float is wanted; easyrig removes weight, not shake"* (`rig.easyrig`), *"On long lenses, where free handheld becomes unreadable"* (`rig.handheld`), *"A long static shot, where breathing drift appears"* (`rig.monopod`), *"Emotional dialogue, where faces and expression must read"* (`rig.hi_hat_low_mode`), *"The character's face must be seen, not borrowed eyes"* (`rig.helmet_cam`), *"The shot is about where he looks, not what his hands do"* (`rig.chest_mount`), *"An object with no distinct sides, where rotation reveals nothing"* (`rig.turntable`). Note the shape of that list: it is the only axis where the two ends argue with each other in both directions.

**Axis 3 — What does the day afford: crew, permits, prep, ground?**
This is the condition the shelf repeats most — fifteen of the thirty-six — and it is also the one most likely to be mistaken for money, which it is not: *"A grab shot with no trained operator or setup time"* (`rig.steadicam`), *"No specialist operator or prep time for a hybrid rig"* (`rig.trinity`), *"A fast-moving scene with no time for the hybrid setup"* (`rig.gimbal_on_slider`), *"A small crew and budget, no safe footprint for a crane"* (`rig.crane`), *"Budget and crew cannot carry a telescoping arm"* (`rig.technocrane`), *"No closed road, permits or crew for a camera car"* (`rig.russian_arm`), *"No permits, road or budget; shoot the car on stage"* (`rig.process_trailer`), *"A driving scene with no finished 3D assets or volume budget"* (`rig.led_volume`), *"A product orbit on location or a short schedule"* (`rig.motion_control`), *"A tank or small water shot with no dive team"* (`rig.underwater_housing`), *"Long days, where back fatigue prints into the frame"* (`rig.shoulder_rig`), *"Low aerial work, where a drone is cheaper and more precise"* (`rig.helicopter`). It is asked last because it is the axis that most often overrules the other two, and a question that overrules should be asked after you know what it is overruling.

---

**The map**

**Axis 1 — what is holding the camera up**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The floor of the location — legs, wheels, rails, a column, a stage or an arm bolted down** (twenty-five) | `rig.tripod_locked` · `rig.fluid_head` · `rig.monopod` · `rig.pedestal` · `rig.hi_hat_low_mode` · `rig.slider` · `rig.gimbal_on_slider` · `rig.dolly_track` · `rig.doorway_dolly` · `rig.rail_through_set` · `rig.jib` · `rig.crane` · `rig.technocrane` · `rig.remote_head` · `rig.motion_control` · `rig.milo` · `rig.turntable` · `rig.overhead_rig` · `rig.probe_lens` · `rig.high_speed_camera` · `rig.crash_cam` · `rig.invisible_rig` · `rig.roll_rig` · `rig.led_volume` · `rig.camera_360` |
| **A person — hands, a shoulder, a vest, a sprung arm** (ten) | `rig.handheld` · `rig.shoulder_rig` · `rig.easyrig` · `rig.steadicam` · `rig.trinity` · `rig.gimbal` · `rig.body_stabiliser_dance` · `rig.phone_rig` · `rig.underwater_housing` · `rig.handoff` |
| **Something that drives — the camera travels because a vehicle does** (four) | `rig.russian_arm` · `rig.car_mount` · `rig.vehicle_interior` · `rig.process_trailer` |
| **The air, or a line strung above the space — nothing under the camera at all** (six) | `rig.cable_cam` · `rig.wire_cam_crowd` · `rig.drone` · `rig.fpv_drone` · `rig.micro_fpv_indoor` · `rig.helicopter` |
| **The thing being filmed — the mount rides the actor, the object or the set** (five) | `rig.snorricam` · `rig.chest_mount` · `rig.helmet_cam` · `rig.gopro_pov` · `rig.rotating_set` |
| **Nothing — the camera is a coordinate a person is driving** (one) | `rig.virtual_camera` |

**Axis 2 — is the camera's body allowed to be felt**

| Answer | The shortlist, by id |
| :--- | :--- |
| **No — the frame must read as a decision, and nothing in it may look carried** (twenty-eight) | `rig.tripod_locked` · `rig.fluid_head` · `rig.pedestal` · `rig.hi_hat_low_mode` · `rig.slider` · `rig.gimbal_on_slider` · `rig.dolly_track` · `rig.doorway_dolly` · `rig.rail_through_set` · `rig.jib` · `rig.crane` · `rig.technocrane` · `rig.remote_head` · `rig.motion_control` · `rig.milo` · `rig.turntable` · `rig.overhead_rig` · `rig.probe_lens` · `rig.high_speed_camera` · `rig.invisible_rig` · `rig.led_volume` · `rig.cable_cam` · `rig.wire_cam_crowd` · `rig.rotating_set` · `rig.virtual_camera` · `rig.camera_360` · `rig.process_trailer` · `rig.vehicle_interior` |
| **Yes, but paid for — a body is there and the rig is buying its steadiness back** (thirteen) | `rig.steadicam` · `rig.trinity` · `rig.gimbal` · `rig.easyrig` · `rig.shoulder_rig` · `rig.monopod` · `rig.body_stabiliser_dance` · `rig.phone_rig` · `rig.drone` · `rig.helicopter` · `rig.russian_arm` · `rig.underwater_housing` · `rig.handoff` |
| **Yes, and the movement is the content — the shake is the thing you are buying** (ten) | `rig.handheld` · `rig.snorricam` · `rig.chest_mount` · `rig.helmet_cam` · `rig.gopro_pov` · `rig.fpv_drone` · `rig.micro_fpv_indoor` · `rig.crash_cam` · `rig.roll_rig` · `rig.car_mount` |

**Axis 3 — what the day affords**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One person, now, with no notice** (nineteen) | `rig.tripod_locked` · `rig.fluid_head` · `rig.monopod` · `rig.handheld` · `rig.shoulder_rig` · `rig.gimbal` · `rig.slider` · `rig.hi_hat_low_mode` · `rig.phone_rig` · `rig.gopro_pov` · `rig.chest_mount` · `rig.helmet_cam` · `rig.camera_360` · `rig.roll_rig` · `rig.overhead_rig` · `rig.turntable` · `rig.drone` · `rig.micro_fpv_indoor` · `rig.crash_cam` |
| **A small crew and a prepared few hours — a level floor, a rehearsal, a permit you already hold** (eighteen) | `rig.easyrig` · `rig.steadicam` · `rig.gimbal_on_slider` · `rig.body_stabiliser_dance` · `rig.pedestal` · `rig.doorway_dolly` · `rig.dolly_track` · `rig.jib` · `rig.probe_lens` · `rig.motion_control` · `rig.remote_head` · `rig.car_mount` · `rig.vehicle_interior` · `rig.fpv_drone` · `rig.snorricam` · `rig.high_speed_camera` · `rig.virtual_camera` · `rig.underwater_housing` |
| **A rigging day, permits, a closed road, or a set built for the shot** (fourteen) | `rig.trinity` · `rig.rail_through_set` · `rig.crane` · `rig.technocrane` · `rig.milo` · `rig.invisible_rig` · `rig.russian_arm` · `rig.process_trailer` · `rig.led_volume` · `rig.cable_cam` · `rig.wire_cam_crowd` · `rig.helicopter` · `rig.rotating_set` · `rig.handoff` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and on this shelf it is normally one or two cards wide, because axis one has already thrown away most of the file.*

---

**The default, and the one against it**

**The default is `rig.dolly_track`, and it is measured rather than asserted — but the measurement had to be done twice, because the obvious answer is wrong.** Two cards tie for most-yielded-to, at three inbound edges each: `rig.gimbal` and `rig.dolly_track`. `rig.gimbal` looks like the fallback and is not one. Its three edges — `rig.steadicam` (*"A grab shot with no trained operator or setup time"*), `rig.trinity` (*"No specialist operator or prep time for a hybrid rig"*) and `rig.gimbal_on_slider` (*"A fast-moving scene with no time for the hybrid setup"*) — are **one condition stated three times: there is no operator and no prep**. That is a door out of the shelf on a bad day, not something the shelf falls back on. `rig.dolly_track` takes its three from three genuinely different places: `rig.hi_hat_low_mode` (*"Emotional dialogue, where faces and expression must read"*), `rig.slider` (*"Following someone walking, beyond a slider's travel"*) and `rig.doorway_dolly` (*"A heavy camera package, or a floor needing laid track"*) — the face, the distance and the weight. A card reached three times for one reason is an escape hatch; a card reached three times for three reasons is a default.

**The one against it is `rig.rotating_set`.** Nothing on the shelf yields to it, no condition names it, and it is the only card here that answers axis one with *the thing in the frame, and the thing in the frame is moving*. Every other support on this shelf accepts that the world is fixed and negotiates how to travel through it; `rig.rotating_set` fixes the camera and turns the world instead, which is the shelf's own premise inverted rather than varied. Its whole stated cost is construction, money and real risk to the performer — a cost that is paid, not argued with, and paid only by a shot the story turns on. Its near cousin against the grain is `rig.snorricam`, which rides the actor rather than the set and is reached exactly once, by `rig.helmet_cam`, for the narrow reason that the face must be visible. **Choosing the best rig is not a creative goal.** `rig.dolly_track` is also the most worn move in the medium, and a film assembled entirely out of defaults is a film nobody had to make.

---

**The unasked**

**Twenty-eight of the fifty-one cards are the target of no `Yields to:` field anywhere in the package.** They can be chosen, but nothing on any shelf ever sends you to them. By id:

`rig.fluid_head` · `rig.pedestal` · `rig.hi_hat_low_mode` · `rig.shoulder_rig` · `rig.trinity` · `rig.gimbal_on_slider` · `rig.body_stabiliser_dance` · `rig.rail_through_set` · `rig.technocrane` · `rig.remote_head` · `rig.milo` · `rig.overhead_rig` · `rig.russian_arm` · `rig.vehicle_interior` · `rig.crash_cam` · `rig.fpv_drone` · `rig.helicopter` · `rig.chest_mount` · `rig.gopro_pov` · `rig.underwater_housing` · `rig.high_speed_camera` · `rig.camera_360` · `rig.rotating_set` · `rig.roll_rig` · `rig.phone_rig` · `rig.handoff` · `rig.invisible_rig` · `rig.virtual_camera`

**And the shape of that list is the finding, not its length: it is the top of every ladder.** `rig.technocrane`, `rig.milo`, `rig.russian_arm`, `rig.helicopter`, `rig.rail_through_set`, `rig.rotating_set`, `rig.invisible_rig` and `rig.handoff` are the most capable and most expensive things on the shelf, and **not one of them is ever reached by a pair field**, while the cards they yield *to* — `rig.crane`, `rig.motion_control`, `rig.car_mount`, `rig.drone`, `rig.steadicam`, `rig.process_trailer` — are reached constantly. Every edge on this shelf runs downhill. That is not an oversight by the readers who wrote the fields: a `Yields to:` line is written from inside a difficulty, and a difficulty is always a subtraction. **The pair graph is a graph of compromises, so it can only ever route you toward the cheaper card.** Nothing in it is written from the position of having the road closed, and nothing ever will be, because no card's `Avoid when:` says *the trouble with this rig is that it is not ambitious enough*.

The second thing the list shows is a live hole, and it has a name. **`rig.handoff` is the one card on the shelf whose answer to axis one changes inside the take** — the support is handed from a body to an arm to a vehicle behind a wall — and it is unasked. So a reader who has just been told by `rig.rail_through_set` that there is no purpose-built set, and by `rig.cable_cam` that the location is too narrow, and who still needs one unbroken move across two physical regimes, is never sent to the only card that does it. The card this shelf wants is the inverse of `rig.handoff`: **the one that says which two supports hand over cleanly and which pairing always shows**, because the shelf currently records that a handover exists and records nothing at all about which handovers survive. The third thing is smaller and worth stating once: seven cards here are cameras and lenses rather than supports — `rig.probe_lens`, `rig.high_speed_camera`, `rig.camera_360`, `rig.gopro_pov`, `rig.phone_rig`, `rig.crash_cam`, `rig.virtual_camera` — and six of the seven are unasked, because a shelf built on *what is the camera on* has no natural condition for *what the camera is*.

`rig.support_before_move`

---

### Tripod / Locked-Off

**Also called:** sticks, locked off, static  
**What it is:** The camera sits on a tripod with the head locked, so it does not shift a millimetre during the take.  
**Effect on the audience:** The frame becomes a fixed window. Every movement inside it belongs to the actor and the world rather than the camera, and the stillness itself reads as calm or as waiting.  
**Used for and where it works best:** Interviews, establishing shots, comedy that needs a stable frame for the gag to land, and horror where the viewer must search the frame themselves. In heritage documentary it is the default, because carved stone does not need a shaking camera to be felt.  
**Best in:** formats: Interview / Video Podcast, Documentary Feature, Heritage / Historical Documentary, Feature Film, Sitcom / Multi-Cam Comedy, Corporate / Training, Explainer, News Report / Reportage | genres: Drama, Horror, Comedy, Heritage (civilisation-focused), Historical / Biopic, Verite / Observational, Mystery / Whodunit  
**Avoid when:** In scenes that need energy or pursuit, stillness turns into coldness and distance. In vertical short-form a dead frame loses attention fast — a frame where nothing moves; a talking head or a static piece whose subject carries the movement is the locked stand `rig.phone_rig` prescribes, and is not a dead frame.  
**Prompt:** `locked-off tripod shot, absolutely static frame, only the subject moves`  
**Yields to:** `rig.handheld` — Scenes of energy or pursuit, where stillness reads cold.  
`rig.tripod_locked`

### Fluid Head With Drag

**Also called:** fluid head pan and tilt, drag setting  
**What it is:** A head with fluid or friction damping so pans and tilts start and stop softly instead of snapping. The drag is dialled to the camera's weight and the speed of the move.  
**Effect on the audience:** The move reads as deliberate and controlled. The eye follows it without ever noticing the equipment.  
**Used for and where it works best:** Following a person walking through a scene, tracking a ball or a car in sport, and the slow reveal across a landscape or a carved wall in documentary. High drag for slow epic moves, light drag for fast sports following.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Sports Broadcast / Sports Film, News Report / Reportage, Interview / Video Podcast, Corporate / Training, Feature Film, Travel / Real Estate / Hospitality | genres: Heritage (civilisation-focused), Nature / Wildlife, Sports Drama, Historical / Biopic, Drama, Science / Educational  
**Avoid when:** With the wrong drag the pan wobbles at the start or snaps at the end and the move exposes itself. On long lenses every tremor is magnified.  
**Prompt:** `smooth damped pan on a fluid head, easing in and easing out, no snap at the end`  
`rig.fluid_head`

### Studio Pedestal

**Also called:** ped, TV pedestal, column dolly  
**What it is:** A pneumatic or spring-loaded column on wheels that raises and lowers the camera smoothly and rolls across a flat floor under one operator.  
**Effect on the audience:** Clean television movement: height and glide with no camera personality at all, so the attention stays on the presenter or the guest.  
**Used for and where it works best:** News and talk studios, multi-camera sitcom, and multi-camera video podcast. The slow ped move up or down changes the feel of a scene without a cut.  
**Best in:** formats: News Report / Reportage, Sitcom / Multi-Cam Comedy, Interview / Video Podcast, Corporate / Training, Concert / Live Event, Explainer, Soap Opera / Telenovela | genres: Comedy, Drama, Political Thriller, Science / Educational, Medical Drama  
**Avoid when:** It needs a perfectly flat floor, and it is useless on location or on any uneven ground.  
**Prompt:** `studio pedestal move, camera rising smoothly while gliding toward the desk`  
**Yields to:** `rig.jib` — On location or uneven ground, where a ped cannot roll.  
`rig.pedestal`

### Hi-Hat / Low Mode

**Also called:** low hat, ground level rig, baby legs  
**What it is:** A very short base set on the ground or on a board, or flipping the camera under the head on a Steadicam or gimbal so it can sit at knee height or lower.  
**Effect on the audience:** The world grows. From this height people tower, and the ground, the dust and the feet become the subject.  
**Used for and where it works best:** A hero entrance, feet on sand or marble, the eyeline of a child or an animal, and a product sitting on a table. In heritage work: ground level at the base of temple columns so the real scale reads.  
**Best in:** formats: Feature Film, Commercial / TVC, Product Video / Motion Design, Trailer / Teaser, Heritage / Historical Documentary, Kids Content, Music Video, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Action, Western, Heritage (civilisation-focused), Fantasy / Epic, Horror, Family, Mythology / Ancient Epic  
**Avoid when:** At low height you lose faces and expression, so keep it out of an emotional dialogue scene.  
**Prompt:** `hi-hat low mode shot at ground level, boots crossing frame, the wall towering above`  
**Yields to:** `rig.dolly_track` — Emotional dialogue, where faces and expression must read.  
`rig.hi_hat_low_mode`

### Handheld

**Also called:** hand-held, free camera  
**What it is:** The camera is carried in the operator's hands with no mechanical stabilisation, so every breath and step prints into the image.  
**Effect on the audience:** A human presence. The viewer senses that someone is standing in the scene watching with them, so the image reads as testimony rather than design.  
**Used for and where it works best:** Fights and chases, an emotional collapse, documentary and reportage, and horror scenes that must feel unsafe. In drama start locked off and move to handheld when the character breaks so the shift is felt.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, News Report / Reportage, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, Docudrama / Reenactment | genres: Drama, War, Horror, Crime / Procedural, Thriller / Suspense, Verite / Observational, Found Footage, Survival  
**Avoid when:** Shake for no reason tires the eye and reads as amateur. It works on wide lenses and becomes unreadable on long ones.  
**Prompt:** `handheld camera, natural breathing movement, slight reframing as she moves`  
**Yields to:** `rig.monopod` — On long lenses, where free handheld becomes unreadable.  
`rig.handheld`

### Shoulder Rig

**Also called:** shoulder mount, ENG style  
**What it is:** The camera rides on the shoulder with handles, a back pad and counterweight, which keeps it handheld but far steadier.  
**Effect on the audience:** A natural walk with weight. The movement stays human but settles, so the viewer feels presence without nausea.  
**Used for and where it works best:** Documentary and news, realist drama that walks with the character, and any long take that cannot survive free handheld. Ideal for covering a whole scene in one take alongside a moving actor.  
**Best in:** formats: Documentary Feature, News Report / Reportage, Documentary Series, Drama Series Episode, Feature Film, Corporate / Training, Docudrama / Reenactment, Vlog / YouTube Long-Form | genres: Drama, War, Crime / Procedural, Verite / Observational, True Crime, Political Thriller, Medical Drama  
**Avoid when:** It is heavy on the back over a long day and the fatigue shows in the frame. It also cannot drop low easily without wrecking the operator.  
**Prompt:** `shoulder-mounted camera, weighted steady handheld, walking with him down the corridor`  
**Yields to:** `rig.easyrig` — Long days, where back fatigue prints into the frame.  
`rig.shoulder_rig`

### Easyrig

**Also called:** body-mounted support arm, vest support  
**What it is:** A vest, a spring and a line carry the camera's weight off the arms and neck while the camera hangs at chest or eye height.  
**Effect on the audience:** It does not change the motion signature; it lets handheld last for hours at the same quality, so the movement stays intentional and never becomes fatigue.  
**Used for and where it works best:** Long shooting days on documentary and drama, following someone over a long walk, and heavy camera and lens packages. It is also paired with a big gimbal to carry its weight for the operator.  
**Best in:** formats: Documentary Feature, Documentary Series, Drama Series Episode, Feature Film, Corporate / Training, News Report / Reportage, Travel / Real Estate / Hospitality | genres: Drama, Verite / Observational, War, Nature / Wildlife, Historical / Biopic, Crime / Procedural  
**Avoid when:** It does not remove shake, so if you want a clean float you still need a Steadicam or a gimbal.  
**Prompt:** `handheld supported by a body rig, steady and sustained, no fatigue drift in the frame`  
**Yields to:** `rig.steadicam` — A clean float is wanted; easyrig removes weight, not shake.  
`rig.easyrig`

### Steadicam

**Also called:** stabilised body rig, Steadicam vest and arm  
**What it is:** A vest, a sprung arm and a balanced sled isolate the operator's body from the camera, so they can walk, run or climb stairs while the image floats.  
**Effect on the audience:** A human gait without human shake. The viewer feels like a spirit moving through the space: as free as handheld and as smooth as a dolly.  
**Used for and where it works best:** The long single take that comes through a door and circles a crowded room, following someone from behind down a corridor, and horror that chases a character between rooms. Its true signature shows when it passes through doorways and down stairs, which is exactly what a dolly cannot do.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Trailer / Teaser, Short Film, Concert / Live Event, Sports Broadcast / Sports Film, Commercial / TVC | genres: Drama, Horror, Crime / Procedural, Gangster, Thriller / Suspense, Action, Musical  
**Avoid when:** It needs a trained operator and setup time, so it is not a grab shot. Used in every scene, the contrast with stillness disappears.  
**Prompt:** `steadicam float following him through the doorway and down the stairs, human gait, no shake`  
**Example:** The Shining, the tricycle corridors operated by Garrett Brown.  
**Yields to:** `rig.gimbal` — A grab shot with no trained operator or setup time.  
`rig.steadicam`

### Trinity / Hybrid Stabiliser

**Also called:** ARRI Trinity, Ronin 4D style hybrid  
**What it is:** A rig that combines a Steadicam vest with three-axis electronic stabilisation, so the camera can travel from ground level to high overhead inside one continuous move.  
**Effect on the audience:** A move no other rig can make: a continuous float with a full change of height, so the scene seems to open out under the viewer's eye.  
**Used for and where it works best:** The single take that starts at someone's feet, rises to their face and travels on with them, the entrance from a tight corridor into a huge space, a music video following a dancer across levels. Very useful in heritage work: from the paving up to the temple facade in one move.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Drama Series Episode, Trailer / Teaser, Concert / Live Event, Travel / Real Estate / Hospitality, Heritage / Historical Documentary | genres: Drama, Action, Musical, Fantasy / Epic, Heritage (civilisation-focused), Historical / Biopic, Thriller / Suspense  
**Avoid when:** It is complex and needs a specialist operator and time. With no narrative reason behind the move, it reads as a technical showpiece.  
**Prompt:** `hybrid stabilised rig rising from ankle height to eye level while moving forward, one unbroken move`  
**Yields to:** `rig.gimbal` — No specialist operator or prep time for a hybrid rig.  
`rig.trinity`

### Gimbal

**Also called:** three-axis gimbal, MoVI, Ronin  
**What it is:** Motors on three axes correct the camera's tilt moment by moment, producing smooth movement with no vest and no arm.  
**Effect on the audience:** Machine smoothness: perfectly stable but weightless. It reads as gliding rather than walking, which gives a clean modern feel.  
**Used for and where it works best:** Most commercial, social and wedding work today, following a person between rooms, and coverage of kitchens, shops and showrooms. It is the fastest and cheapest route to smooth movement and it loves wide lenses.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Wedding / Event Film, Corporate / Training, Travel / Real Estate / Hospitality, Music Video, Vlog / YouTube Long-Form, Drama Series Episode | genres: Drama, Action, Romance, Slice of Life, Comedy, Sports Drama  
**Avoid when:** Too much smoothness strips the human feeling and leaves the scene sterile. On long lenses it produces an unnatural floating drift.  
**Prompt:** `gimbal-smooth tracking move, gliding beside her at constant height, no bounce`  
**Yields to:** `rig.handheld` — The scene needs human presence, not machine smoothness.  
`rig.gimbal`

### Gimbal on a Slider

**Also called:** slider with stabilised head, hybrid slide  
**What it is:** A gimbal is mounted on a slider, so the slider gives a precise straight path while the gimbal removes any vibration and allows a controlled rotation during the slide.  
**Effect on the audience:** A move neither device makes alone: a straight glide with a locked rotation around a point, which comes out designed and expensive looking.  
**Used for and where it works best:** Product and food shots, reliefs and artefacts in heritage documentary, and the reveal of a detail in a commercial. Use it when the object must stay centred while the entire background slides away behind it.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Heritage / Historical Documentary, Documentary Feature, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok), Fashion Film | genres: Heritage (civilisation-focused), Science / Educational, Drama, Historical / Biopic, Nature / Wildlife  
**Avoid when:** Setup is slower than a gimbal alone, so it does not suit a fast-moving scene. If the balance is off, a wobble appears at the end of the slide.  
**Prompt:** `slider move with a stabilised head, sliding sideways while orbiting the object locked in centre frame`  
**Yields to:** `rig.gimbal` — A fast-moving scene with no time for the hybrid setup.  
`rig.gimbal_on_slider`

### Body-Worn Stabiliser for Dance

**Also called:** dance camera rig, stabilised follow for choreography  
**What it is:** An operator wearing a Steadicam or a vest-supported gimbal moves with the dancers as if he were one of them, circling them in the rhythm of the choreography.  
**Effect on the audience:** The camera becomes a dancer. The viewer feels inside the formation rather than watching it from outside.  
**Used for and where it works best:** Dance films, music videos and musical numbers, plus one-take choreography reels that orbit the group. The rule: the camera must know the routine, so the moves are rehearsed exactly as the dancers rehearse.  
**Best in:** formats: Dance Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Commercial / TVC, Fashion Film, Title Sequence / Opening Credits | genres: Musical, Romance, Comedy, Action, Martial Arts / Wuxia  
**Avoid when:** Without rehearsal the camera gets in the dancers' way or misses the peak. In tight spaces it is dangerous for both.  
**Prompt:** `stabilised camera dancing with the group, orbiting them in rhythm, always facing the lead`  
`rig.body_stabiliser_dance`

### Slider

**Also called:** short track, mini dolly  
**What it is:** A short rail, half a metre to a metre, on which the camera slides left and right or in and out in a limited, precise move.  
**Effect on the audience:** Life without travel. A small move is enough to stop the image feeling dead and it reveals the depth layers inside the frame.  
**Used for and where it works best:** The interview that needs a touch of movement, product and food shots, the artefact in a documentary, and any insert. It works best with a foreground element so the parallax reads.  
**Best in:** formats: Interview / Video Podcast, Product Video / Motion Design, Documentary Feature, Heritage / Historical Documentary, Corporate / Training, Commercial / TVC, Explainer, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, Heritage (civilisation-focused), Science / Educational, Historical / Biopic, Nature / Wildlife  
**Avoid when:** The travel is short, so do not lean on it to follow someone walking. If every shot in the film slides, the piece starts to feel like a template.  
**Prompt:** `short slider move left to right past a foreground object, revealing the subject behind it`  
**Yields to:** `rig.dolly_track` — Following someone walking, beyond a slider's travel.  
`rig.slider`

### Dolly on Track

**Also called:** dolly and track, rails  
**What it is:** A heavy platform running on laid and levelled rails, pushed by a dolly grip at a constant speed that can be repeated exactly on every take.  
**Effect on the audience:** The smoothest and most disciplined move there is. It carries no human personality, so it reads as a directorial decision rather than a person being present.  
**Used for and where it works best:** The slow push on a face at the moment of realisation, a parallel track beside two people walking and talking, and any move that must repeat on the same timing with dialogue. It is the backbone of feature and premium series work.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Commercial / TVC, Music Video, Trailer / Teaser, Docudrama / Reenactment | genres: Drama, Historical / Biopic, Crime / Procedural, Noir / Neo-Noir, Thriller / Suspense, Romance, War  
**Avoid when:** It needs setup time, level ground and crew, so it does not fit a compressed schedule. If the track is not level, a bump prints into the image.  
**Prompt:** `smooth dolly on rails pushing in slowly from medium to close-up, perfectly steady`  
**Yields to:** `rig.doorway_dolly` — Practical interiors and tight spaces that cannot take laid track.  
`rig.dolly_track`

### Doorway Dolly

**Also called:** door dolly, narrow dolly  
**What it is:** A narrow dolly platform sized to pass through a standard doorway, running either on track or on pneumatic tyres straight on the floor.  
**Effect on the audience:** Dolly smoothness inside a real house. The move feels possible in a tight space, so the scene keeps its realism.  
**Used for and where it works best:** Interiors in apartments, corridors and shops, following someone from room to room, and practical locations that cannot take laid track. It is the default choice for drama shot inside real homes.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Soap Opera / Telenovela, Docudrama / Reenactment, Commercial / TVC, Limited Series | genres: Drama, Crime / Procedural, Romance, Thriller / Suspense, Comedy, Melodrama  
**Avoid when:** On uneven floors without track it judders. Its payload is also limited next to a full-size dolly.  
**Prompt:** `doorway dolly move following her from the hallway into the kitchen, smooth and low`  
**Yields to:** `rig.dolly_track` — A heavy camera package, or a floor needing laid track.  
`rig.doorway_dolly`

### Rail Through a Set

**Also called:** track through wild walls, built-in dolly path  
**What it is:** The track is designed into the set itself, with wild walls built to be pulled away so the camera can travel from room to room without stopping.  
**Effect on the audience:** The house becomes one continuous world. The viewer feels the walls are not there and that the whole story shares a single space.  
**Used for and where it works best:** The long single take that crosses several rooms and hands off between characters, party or family scenes in premium series, and any sequence meant to feel like one stage. The decision is made with the cinematographer and the production designer before the set is built, not on the shooting day.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Soap Opera / Telenovela, Music Video, Commercial / TVC | genres: Drama, Gangster, Crime / Procedural, Historical / Biopic, Melodrama, Comedy  
**Avoid when:** It needs a purpose-built, planned set and is impossible on a real location. Any delay pulling a wall ruins the whole take.  
**Prompt:** `the camera travels on hidden track straight through the wall line from the kitchen into the bedroom`  
**Yields to:** `rig.steadicam` — A real location with no purpose-built set.  
`rig.rail_through_set`

### Jib Arm

**Also called:** jib, small crane arm  
**What it is:** A counterweighted arm on a stand that lifts and lowers the camera in an arc. It is smaller than a crane and can be rigged by a small crew.  
**Effect on the audience:** It opens the space. Coming down from above to eye level says: this is the place, and this is the person inside it.  
**Used for and where it works best:** Opening or closing a scene, weddings and events, the establishing shot of a corporate or hotel film, and concert coverage. It is the way to buy a rich move on a small budget.  
**Best in:** formats: Wedding / Event Film, Corporate / Training, Travel / Real Estate / Hospitality, Concert / Live Event, Commercial / TVC, Drama Series Episode, Documentary Feature, Music Video | genres: Romance, Drama, Family, Musical, Heritage (civilisation-focused), Sports Drama  
**Avoid when:** Its reach is limited, and using it on every shot gives the piece a wedding-video signature. In strong wind it sways.  
**Prompt:** `jib arm descending from above the crowd down to eye level on the bride`  
**Yields to:** `rig.crane` — The move needs more height and reach than a jib has.  
`rig.jib`

### Crane

**Also called:** camera crane, boom  
**What it is:** A long heavy arm on a base or a vehicle that reaches serious height and carries the camera on a moving head, either with a rider or under remote control.  
**Effect on the audience:** A god's view. Height reads as fate and judgement: the person is small and the world is large, or the camera rises and leaves them behind.  
**Used for and where it works best:** The ending where the camera rises and leaves the character in the square, the arrival of an army or a crowd in an epic, and the opening sweep across a city or an archaeological site. In heritage work it shows the full plan of a temple or ziggurat.  
**Best in:** formats: Feature Film, Trailer / Teaser, Heritage / Historical Documentary, Commercial / TVC, Music Video, Concert / Live Event, Drama Series Episode, Sports Broadcast / Sports Film | genres: Historical / Biopic, War, Fantasy / Epic, Mythology / Ancient Epic, Heritage (civilisation-focused), Drama, Action, Musical  
**Avoid when:** Heavy rigging, time and cost, and it needs a safe footprint. If the move does not serve the story it just displays the budget.  
**Prompt:** `crane rising from ground level up over the courtyard, the figure shrinking below`  
**Yields to:** `rig.jib` — A small crew and budget, no safe footprint for a crane.  
`rig.crane`

### Technocrane

**Also called:** telescoping crane  
**What it is:** A crane whose arm telescopes in and out during the move, so the camera can rise, push in and pull back inside one shot with no cut.  
**Effect on the audience:** A move that feels impossible: the path curves and extends at once, so space itself feels pliable, as if the world is moving and not the camera.  
**Used for and where it works best:** The big opening that threads between obstacles and lands on a face, the chase that follows a car then climbs above it, the music video that crosses stage levels. Use it when one shot has to swallow several.  
**Best in:** formats: Feature Film, Commercial / TVC, Music Video, Trailer / Teaser, Drama Series Episode, Concert / Live Event, Sports Broadcast / Sports Film | genres: Action, Drama, Thriller / Suspense, Musical, Historical / Biopic, Spy / Espionage, Superhero  
**Avoid when:** It is expensive and needs crew, rigging and a carefully designed path. With no clear choreography it comes out as an elaborate shot that means nothing.  
**Prompt:** `telescoping crane extending mid-move, rising over the wall then pushing in to a close-up`  
**Yields to:** `rig.crane` — Budget and crew cannot carry a telescoping arm.  
`rig.technocrane`

### Remote Head

**Also called:** hot head, stabilised remote head  
**What it is:** A motorised head carried on a crane, a vehicle or a cable, with the operator panning, tilting and rolling from a control panel away from the camera.  
**Effect on the audience:** It frees the camera from the human body. You can put it where no operator can go, and the movement stays precise, smooth and repeatable.  
**Used for and where it works best:** The far end of a long crane, cars and chases, above a crowd, and dangerous positions such as a ledge, fire or water. It is essential for any move that needs full rotation no hand-held operator could manage.  
**Best in:** formats: Feature Film, Commercial / TVC, Sports Broadcast / Sports Film, Concert / Live Event, Trailer / Teaser, Music Video, Drama Series Episode | genres: Action, Thriller / Suspense, Spy / Espionage, Musical, War, Sports Drama  
**Avoid when:** The operator cannot feel the space, so framing needs rehearsal and a good monitor. Any signal lag wrecks the timing.  
**Prompt:** `remote head on the crane arm, panning and rolling smoothly while the arm sweeps over the crowd`  
`rig.remote_head`

### Motion Control / Robot Arm

**Also called:** Bolt arm, motion control rig, repeatable move  
**What it is:** A robotic arm programmed to a defined path that it repeats with absolute precision every time, at very high speeds, and it can run in sync with high-speed capture.  
**Effect on the audience:** Movement no human hand can make: fast, sharp and perfect. Because it repeats exactly, several passes can be layered into one shot.  
**Used for and where it works best:** Product, food and fragrance commercials, a fast orbit around an object, and repeating the identical move with changed lighting or contents, one pass for the product and one for the background. It is essential for anything that has to match frame by frame.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Title Sequence / Opening Credits, Music Video, Fashion Film, Corporate / Training, Trailer / Teaser | genres: Sci-Fi, Action, Musical, Science / Educational, Surreal / Absurdist  
**Avoid when:** It is expensive and needs a stage and programming time, so it does not fit location work or short schedules. In dramatic scenes its perfection feels cold.  
**Prompt:** `motion-control robotic arm executing a fast repeatable orbit around the bottle, identical every pass`  
**Yields to:** `rig.turntable` — A product orbit on location or a short schedule.  
`rig.motion_control`

### The Milo Rig

**Also called:** Milo motion control, telescoping motion control rig  
**What it is:** A motion-control platform on track with an arm that telescopes and rotates, carrying a full cinema camera to a longer reach and greater height than a short-arm robot.  
**Effect on the audience:** It joins robot precision to crane scale. You can make an extended move around a person or a set and repeat it exactly for effects work.  
**Used for and where it works best:** Effects shots that need two or more passes such as an actor meeting their double or something appearing and vanishing, large commercials, and virtual scenes inside a stage or LED wall. Use it when the subject is human and the move must be wider than a tabletop arm allows.  
**Best in:** formats: Commercial / TVC, Feature Film, Title Sequence / Opening Credits, Music Video, 3D CG Animation, Trailer / Teaser, Corporate / Training | genres: Sci-Fi, Fantasy / Epic, Superhero, Action, Surreal / Absurdist, Musical  
**Avoid when:** A full day of rigging and serious cost, so only plan it when the shot earns it. Any change in performance between passes ruins the composite.  
**Prompt:** `large motion-control rig on track, repeatable extending arc around the actor for a twin composite`  
**Yields to:** `rig.motion_control` — A tabletop-scale repeatable move needing no crane reach.  
`rig.milo`

### Turntable

**Also called:** product turntable, rotating platform, orbit table, spin shot  
**What it is:** A rotating platform that turns the object in front of a static camera, or the reverse, a circular path that carries the camera around the object at constant speed.  
**Effect on the audience:** A complete presentation without words. The viewer sees every side and decides they understand the object, and slow rotation reads as value.  
**Used for and where it works best:** Product, jewellery, car, watch and footwear films, sales pages, presenting an artefact in a documentary or museum piece, and e-commerce clips. Very slow rotation with a moving light is the default language of luxury, and a soft reflection underneath makes the object sit in a real space. Give it one full revolution at a constant speed.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Corporate / Training, Explainer, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Game Cinematic / Gameplay, AI-Generated Clip | genres: Science / Educational, Heritage (civilisation-focused), Historical / Biopic, Drama, Family, Slice of Life  
**Avoid when:** On an object with no distinct sides it is simply boring, and a fast spin loses the detail and cheapens the product. Do not go past one rotation either; the movement stops having a purpose.  
**Prompt:** `product on a slow turntable, camera locked off, a single moving highlight sweeping across the surface`  
**Yields to:** `rig.slider` — An object with no distinct sides, where rotation reveals nothing.  
`rig.turntable`

### Overhead Rig

**Also called:** top-down rig, bird rig, cooking overhead  
**What it is:** The camera is mounted directly above a table or floor on an arch, an arm or scaffolding, looking straight down at 90 degrees.  
**Effect on the audience:** It turns the scene into a flat readable plane. The hands become the performers and the materials become colour and shape, and the viewer understands each step instantly.  
**Used for and where it works best:** Cooking and recipe videos, crafts and handwork, unboxing, and step-by-step explainers. It is the base form of vertical food content because it works with the sound off and at any screen size.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Explainer, Product Video / Motion Design, Corporate / Training, Commercial / TVC, Vlog / YouTube Long-Form, Documentary Feature | genres: Family, Comedy, Science / Educational, Slice of Life, Preschool / Early Learning  
**Avoid when:** It carries no faces and builds no relationship with a person. Held for a whole piece it turns monotonous, so break it with a side angle.  
**Prompt:** `top-down overhead shot of the hands working on the table, locked off, even soft light`  
`rig.overhead_rig`

### Probe and Periscope Rigs

**Also called:** probe lens, snorkel lens, macro probe  
**What it is:** A long thin tube lens with a tiny front element that can enter narrow openings, go under water or pass between objects, with great depth of field and macro capability.  
**Effect on the audience:** A miniature world becomes vast. The viewer enters a place their body could never reach, and the familiar turns strange and thrilling.  
**Used for and where it works best:** Food and drink commercials where the camera travels into the glass or between ingredients, nature documentary among grass and insects, and the shot that enters a small opening into a large world. It also makes a superb transition: enter the hole and emerge in another scene.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Documentary Feature, Documentary Series, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Title Sequence / Opening Credits | genres: Nature / Wildlife, Science / Educational, Surreal / Absurdist, Comedy, Fantasy / Epic, Adventure  
**Avoid when:** It needs a great deal of light because it is slow, and every vibration is magnified by the close working distance.  
**Prompt:** `probe lens travelling low across the table and diving between the ingredients, deep focus macro`  
`rig.probe_lens`

### Russian Arm

**Also called:** car-mounted crane arm, gyro-stabilised vehicle crane  
**What it is:** A crane mounted on the roof of a fast camera car with a remote head, so the camera can fly around a moving vehicle while travelling at its speed.  
**Effect on the audience:** It turns the car into a hero. The camera orbits, rises and drops while everything is moving, so the viewer feels speed and weight at once.  
**Used for and where it works best:** Car commercials, chases, and the move that leaves the wheel and climbs to the driver's face. The signature move: start behind, sweep down the side, finish ahead of the vehicle.  
**Best in:** formats: Commercial / TVC, Feature Film, Trailer / Teaser, Music Video, Sports Broadcast / Sports Film, Drama Series Episode, Travel / Real Estate / Hospitality | genres: Action, Thriller / Suspense, Spy / Espionage, Road Movie, Crime / Procedural, Sports Drama  
**Avoid when:** It needs a closed road, crew, permits and safety, so it is not a run-and-gun tool. Without real speed in the scene the move feels empty.  
**Prompt:** `car-mounted crane arm sweeping from behind the vehicle along its side and up to the windscreen`  
**Yields to:** `rig.car_mount` — No closed road, permits or crew for a camera car.  
`rig.russian_arm`

### Car Mounts

**Also called:** hood mount, side mount, hostess tray, suction mounts  
**What it is:** Mounts fixed to the outside of the car: on the bonnet facing the driver, on the door as a side tray, or on the bumper and roof. The camera travels with the car and shares its vibration.  
**Effect on the audience:** The world streams past the face. The subject stays fixed in frame while the background moves, which reads as journey, escape, or confinement inside a moving box.  
**Used for and where it works best:** Driving scenes in drama and road movies, in-car dialogue, and exterior beauty shots for commercials. Bonnet mount for a single face, side tray for driver and passenger together, wheel-level mount for speed.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Music Video, Travel / Real Estate / Hospitality, Short Film, Docudrama / Reenactment, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Road Movie, Crime / Procedural, Drama, Thriller / Suspense, Action, Noir / Neo-Noir, Comedy  
**Avoid when:** Vibration, wind and windscreen reflections will ruin the shot if they are not planned for. Everything needs a double safety tether.  
**Prompt:** `hood-mounted camera locked on the driver, the road streaming past behind him`  
`rig.car_mount`

### Vehicle Interior Rig

**Also called:** in-car rig, doorless car rig, interior camera track  
**What it is:** Rigging the camera inside the vehicle itself: seats removed, doors taken off, mounts on the glass and roof, or a rotating head in the middle that turns between the passengers.  
**Effect on the audience:** The viewer becomes a passenger. The tight space and close faces make the scene intimate and claustrophobic at the same time.  
**Used for and where it works best:** Long driving dialogue, the tension scene before arrival, and the single take that rotates a full 360 degrees inside the car between characters. Its strongest use: a rotating head in the centre turning as the danger builds outside.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Commercial / TVC, Docudrama / Reenactment, Travel / Real Estate / Hospitality, Music Video | genres: Drama, Crime / Procedural, Thriller / Suspense, Road Movie, War, Noir / Neo-Noir, Comedy  
**Avoid when:** There is little room for crew, sound and light, and it needs safety planning ahead of the day. Without reflection control the crew appears in the glass.  
**Prompt:** `interior car rig, camera rotating between the driver and the passenger in one continuous move`  
**Example:** Children of Men, the single-take car ambush.  
**Yields to:** `rig.process_trailer` — Crew, sound and controlled light will not fit in the car.  
`rig.vehicle_interior`

### Process Trailer / Low Loader

**Also called:** low loader, tow rig, picture car trailer  
**What it is:** The picture car rides on a low trailer towed by a truck, with crew and lights rigged around it. The actor does not really drive, but everything outside is real.  
**Effect on the audience:** Full performance freedom with complete realism. The actor concentrates on the scene instead of the road, while the background and reflections stay honest.  
**Used for and where it works best:** Any long dialogue scene inside a moving car, night scenes that need controlled light, and any moment where the actor must cry or shout while driving. The cheaper alternative is a static car on stage with light passing across the faces.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Limited Series, Docudrama / Reenactment, Short Film | genres: Drama, Crime / Procedural, Thriller / Suspense, Road Movie, Romance, Noir / Neo-Noir  
**Avoid when:** It needs permits, a road and rigging time, and it is expensive for a short day. On any busy road it becomes a logistical nightmare.  
**Prompt:** `process trailer driving scene, real exteriors passing, controlled light on the faces inside`  
**Yields to:** `rig.led_volume` — No permits, road or budget; shoot the car on stage.  
`rig.process_trailer`

### Crash Cam

**Also called:** sacrificial camera, crash box, expendable rig  
**What it is:** A cheap or boxed camera placed where it is going to be hit: under a wheel, inside a blast, in the path of a fall. Sometimes it is destroyed in the take, and that is the plan.  
**Effect on the audience:** An angle nobody could otherwise shoot. The viewer sees from the place of danger itself, which makes the danger physical.  
**Used for and where it works best:** Explosions and crashes in action, hooves or feet passing over the lens, extreme sport. Its best use is one short shot inside a fast sequence so that it lands as a shock.  
**Best in:** formats: Feature Film, Commercial / TVC, Sports Broadcast / Sports Film, Trailer / Teaser, Music Video, Game Cinematic / Gameplay, Short Film | genres: Action, War, Disaster, Survival, Sports Drama, Thriller / Suspense  
**Avoid when:** It is no use for any shot that must match the image quality of the rest of the scene. And safety outranks the shot every time, because no frame is worth a person or a lens in the wrong place.  
**Prompt:** `low crash cam right in the path of the impact, dust and debris flying over the lens`  
**Yields to:** Tier 0 safety authority (in words, not a card) — Safety outranks the shot every time.  
`rig.crash_cam`

### Cable Cam / Spidercam

**Also called:** skycam, aerial cable system  
**What it is:** A camera suspended on several cables strung between high points, moving in three dimensions above a field or an arena on a remote head.  
**Effect on the audience:** Controlled flight above the event. Wide smooth movement with none of a drone's noise or downwash, and the viewer sees the full shape of the action.  
**Used for and where it works best:** Sports broadcast, above all football, concerts and festivals, and the big opening of an event. It earns its place when you need to drop close to the players and climb back over the stadium in one move.  
**Best in:** formats: Sports Broadcast / Sports Film, Concert / Live Event, Commercial / TVC, Trailer / Teaser, Music Video, News Report / Reportage, Documentary Feature | genres: Sports Drama, Musical, Action, Drama, Science / Educational  
**Avoid when:** A full day of rigging and high anchor points, so it is impossible in a small location. It has no place in an interior drama scene.  
**Prompt:** `cable-suspended camera flying over the arena, descending toward the players then climbing away`  
**Yields to:** `rig.wire_cam_crowd` — A small or narrow location, no multi-cable rigging day.  
`rig.cable_cam`

### Wire Cam Over a Crowd

**Also called:** single-line cable cam, zip cam, flying line  
**What it is:** A single line strung above a crowd or a street, with the camera running along it in a straight path at a speed controlled by a technician.  
**Effect on the audience:** A rush above the heads. The viewer crosses the crowd in two seconds and feels its density and energy without being inside it.  
**Used for and where it works best:** Concerts and festivals, street processions, and the opening shot of a music video with an audience. It is cheaper and faster than a multi-cable system and suits long narrow spaces.  
**Best in:** formats: Concert / Live Event, Music Video, Dance Film, Commercial / TVC, Documentary Feature, Sports Broadcast / Sports Film, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Musical, Drama, Action, Historical / Biopic, Sports Drama  
**Avoid when:** The path is straight and fixed, so there is little room to reframe during the move. Flying anything above people demands strict rigging safety.  
**Prompt:** `camera flying along a wire above the crowd, rushing forward over the raised hands toward the stage`  
**Yields to:** `rig.cable_cam` — The move must change path or reframe in flight.  
`rig.wire_cam_crowd`

### Cinema Drone

**Also called:** aerial drone, multirotor, heavy-lift drone  
**What it is:** A multirotor aircraft carrying a camera on a gimbal, able to climb, descend and orbit, flown by a pilot with a separate camera operator on the larger systems.  
**Effect on the audience:** It gives a location its scale. Height turns a place into a map, and the descent returns it to a human world.  
**Used for and where it works best:** The establishing shot of a place or a city, following a car across a desert road, and the sweep over an archaeological site that reveals its full plan. In heritage work it is the fastest way to give the viewer the scale of an ancient city in three seconds.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Travel / Real Estate / Hospitality, Commercial / TVC, Feature Film, Trailer / Teaser, Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Adventure, Drama, War, Road Movie  
**Avoid when:** It has become a cliche as the opening of every video. Its noise and downwash also destroy any close sound recording.  
**Prompt:** `cinema drone rising above the ruins and drifting forward, revealing the full layout below`  
**Yields to:** `rig.cable_cam` — Close sound must be recorded; no noise or downwash.  
`rig.drone`

### FPV Drone

**Also called:** first-person-view drone, racing drone, cinewhoop  
**What it is:** A fast drone flown through goggles in first person, capable of diving, rolling and threading gaps at high speed with total freedom of path.  
**Effect on the audience:** A physical rush. The viewer becomes a weightless flying body, and the unbroken movement makes the space feel connected and exciting.  
**Used for and where it works best:** A single-take tour of a venue such as a restaurant, a factory or a gym, chasing a bike or a skier, and the opening of a music video or a reel. The signature shot: in through a window, between the people, and out through a door.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Sports Broadcast / Sports Film, Travel / Real Estate / Hospitality, Corporate / Training, Trailer / Teaser, Concert / Live Event | genres: Action, Sports Drama, Musical, Adventure, Comedy, Cyberpunk  
**Avoid when:** It is hard to watch when it runs long, and too much speed makes detail unreadable. It also needs a skilled pilot and a safety plan around people.  
**Prompt:** `FPV drone diving through the window at speed, threading between the tables and out the far door`  
**Yields to:** `rig.micro_fpv_indoor` — Flying indoors or close to people, guarded props needed.  
`rig.fpv_drone`

### Micro FPV Indoor Drone

**Also called:** cinewhoop, ducted micro drone, tiny whoop  
**What it is:** A small drone with ducted, guarded propellers that can fly safely close to people and walls inside rooms and tight corridors.  
**Effect on the audience:** It passes where no human body can. The movement is relatively slow and smooth, so it feels like a dream wandering through the building.  
**Used for and where it works best:** A walkthrough of a property, a hotel or a restaurant, following a dish from the kitchen to the table, and a single take crossing floors or rooms. It has become the preferred form for venue content because it shows the whole space with no cuts.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Travel / Real Estate / Hospitality, Corporate / Training, Product Video / Motion Design, Music Video, Vlog / YouTube Long-Form, Documentary Feature | genres: Slice of Life, Comedy, Romance, Family, Science / Educational  
**Avoid when:** The props are loud, so sound has to be added later. The downwash also moves napkins and hair, which gives the drone away in food shots.  
**Prompt:** `micro FPV drone gliding slowly through the doorway, past the guests, settling on the plate`  
**Yields to:** `rig.probe_lens` — Food shots, where downwash moves the set.  
`rig.micro_fpv_indoor`

### Helicopter Aerial

**Also called:** Cineflex, Shotover, gyro-stabilised aerial mount  
**What it is:** A camera inside a gyro-stabilised ball mounted on a helicopter, working with long lenses at altitudes and speeds no drone can reach.  
**Effect on the audience:** Absolute steadiness across enormous distances. The image feels epic and formal, and on a long lens it reads as an eye watching from very far away.  
**Used for and where it works best:** Sweeps over mountains, desert and large cities, tracking a train, a convoy or an aircraft, and wildlife documentary. Use it when you need altitude, speed and endurance beyond a drone.  
**Best in:** formats: Feature Film, Documentary Feature, Documentary Series, Trailer / Teaser, Commercial / TVC, Travel / Real Estate / Hospitality, Sports Broadcast / Sports Film, Heritage / Historical Documentary | genres: War, Historical / Biopic, Nature / Wildlife, Adventure, Action, Heritage (civilisation-focused), Disaster  
**Avoid when:** High cost, permits and weather, and for most low work a drone is now cheaper and more precise.  
**Prompt:** `helicopter aerial on a long lens, rock steady, tracking the convoy across the desert`  
**Yields to:** `rig.drone` — Low aerial work, where a drone is cheaper and more precise.  
`rig.helicopter`

### Snorricam / Body Mount

**Also called:** body-mounted camera, chest rig facing the actor  
**What it is:** The camera is strapped to the actor's own body on a chest harness or frame, facing their face, so the face stays fixed while the entire world behind them lurches. This entry is the rig itself, its weight and its build, unlike the Snorricam in the signature moves chapter, which covers the shot and its dramatic function.  
**Effect on the audience:** Dissociation and isolation. The viewer is locked to the face while the world swings around it, which reads as psychological rather than physical dizziness.  
**Used for and where it works best:** Addiction, panic and breakdown, running in terror, the moment a character loses control of themselves. One shot is enough: use it twice in a film and the shock is gone.  
**Best in:** formats: Feature Film, Short Film, Music Video, Drama Series Episode, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Psychological / Arthouse, Psychological Horror, Crime / Procedural, Thriller / Suspense, Drama, Horror, Surreal / Absurdist  
**Avoid when:** It is tiring for the actor, needs rigging and safety, and in a scene that does not call for it the trick is naked.  
**Prompt:** `body-mounted rig facing his face, his head locked in frame while the street spins behind him`  
**Example:** Requiem for a Dream.  
`rig.snorricam`

### Chest Mount

**Also called:** chesty, body harness camera  
**What it is:** A small camera on a chest harness facing forward, so it sees the hands and the path from close to the wearer's own sightline.  
**Effect on the audience:** A first-person view with real weight. It differs from a head camera because it is steadier and shows the hands, so it reads as doing rather than looking.  
**Used for and where it works best:** Craft, cooking and repair content from the maker's point of view, corporate training and safety, and sports such as cycling and climbing. It is excellent for instructional reels because the hands stay in frame.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, Corporate / Training, Explainer, Sports Broadcast / Sports Film, Documentary Feature, Kids Content, Travel / Real Estate / Hospitality | genres: Science / Educational, Slice of Life, Adventure, Sports Drama, Family, Survival  
**Avoid when:** Breathing and footfall print into the image, and any bend changes the framing completely. It is not a dramatic camera.  
**Prompt:** `chest-mounted point of view, hands working in the lower frame, natural body sway`  
**Yields to:** `rig.helmet_cam` — The shot is about where he looks, not what his hands do.  
`rig.chest_mount`

### Helmet Cam

**Also called:** head mount, head rig, POV helmet, athlete POV, onboard cam  
**What it is:** A small camera on a helmet, a head strap, the body or the vehicle, moving exactly with the wearer's gaze and turning when they turn.  
**Effect on the audience:** The viewer borrows someone's eyes and receives the physical sensation rather than the view: the speed, the danger, the confusion. The sudden head turns read as searching and danger, and that is exactly what frightens.  
**Used for and where it works best:** Horror from the victim's point of view, found-footage films, extreme sports (motorsport, cycling, skiing, jumping, diving), and military, firefighting and training content. In games and simulation it is the base form of first-person capture, and in sports documentary it works as a short seasoning shot between wide angles to convey the athlete's private experience.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, Game Cinematic / Gameplay, Feature Film, Short Film, Documentary Feature, Documentary Series, Vlog / YouTube Long-Form, Corporate / Training, Trailer / Teaser, Commercial / TVC | genres: Found Footage, Horror, Action, Survival, Adventure, Sports Drama, War, Verite / Observational, Drama  
**Avoid when:** The nervous motion — the wearer's own head turns, which a stabilised action camera (`rig.gopro_pov`) mounted on a helmet still follows — tires the eye fast and can cause nausea, so keep the clip short, and it is useless for any shot where you want to see the character. It rarely explains the play or the space either, because it carries no context and no geography; the exception is a run where the path itself is the information.  
**Prompt:** `helmet-mounted point of view, the beam of the torch swinging as he turns his head`  
**Yields to:** `rig.snorricam` — The character's face must be seen, not borrowed eyes.  
`rig.helmet_cam`

### Action Cam POV

**Also called:** GoPro POV, action camera rig  
**What it is:** A very small, ultra-wide, tough camera whose mount and stabilisation profile are chosen for the object carrying it: a racket, board, handlebar, vehicle or piece of furniture. A head-locked mount whose gaze motion is the point is the separate `rig.helmet_cam` case.  
**Effect on the audience:** An impossible angle for almost nothing. The extreme width makes movement feel faster and closer, and the image reads as raw and honest.  
**Used for and where it works best:** Sport, adventure and travel, behind-the-scenes coverage, the point of view of a tool or a product, and social content generally. Use it as a spice shot inside normal coverage to break the rhythm.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, Vlog / YouTube Long-Form, Travel / Real Estate / Hospitality, Documentary Feature, Commercial / TVC, Game Cinematic / Gameplay, Meme / Comedy Edit | genres: Action, Adventure, Sports Drama, Comedy, Survival, Slice of Life  
**Avoid when:** Its edge distortion and processed colour do not match cinema cameras, so watch the intercutting. Up close it also distorts faces badly.  
**Yields to:** `rig.helmet_cam` — The camera must turn exactly with the wearer's head and preserve that nervous first-person motion.  
**Prompt:** `ultra-wide action camera mounted on the handlebar, extreme perspective, everything rushing past`  
**Example:** Hardcore Henry, shot entirely as point of view.  
`rig.gopro_pov`

### Underwater Housing

**Also called:** water housing, splash bag, dive housing  
**What it is:** A waterproof case holding the camera with external handles, controls and a dome port, used for diving or at the water's surface.  
**Effect on the audience:** A world with different laws. Movement turns heavy and slow and the light breaks into caustics on the floor, so the scene reads as dream, birth or death.  
**Used for and where it works best:** Drowning and rescue scenes, diving and marine life in documentary, and pool and sea shots in commercials, fashion and wedding films. Water is the best place for slow motion because the movement already has weight.  
**Best in:** formats: Feature Film, Documentary Feature, Commercial / TVC, Music Video, Fashion Film, Wedding / Event Film, Sports Broadcast / Sports Film, Travel / Real Estate / Hospitality | genres: Survival, Nature / Wildlife, Drama, Thriller / Suspense, Romance, Adventure, Horror  
**Avoid when:** It needs a safety team and training, and time in the water is limited. A single bubble or drop on the port ruins the shot.  
**Prompt:** `underwater housing shot, caustic light patterns on the body, slow heavy movement in blue water`  
**Yields to:** `rig.probe_lens` — A tank or small water shot with no dive team.  
`rig.underwater_housing`

### High-Speed Camera

**Also called:** Phantom, high frame rate body, slow-mo camera  
**What it is:** A camera body built to record hundreds or thousands of frames per second into fast internal memory, usually running a circular buffer with a trigger fired after the event.  
**Effect on the audience:** The rig itself dictates a method: enormous light, fast glass and a short recording window, so every shot becomes a prepared event.  
**Used for and where it works best:** Food, drink and liquid commercials, science and wildlife such as a wing, a tongue or a bullet, and sport. Use the post trigger when the moment cannot be predicted: let it happen, then save what the buffer already holds.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Documentary Feature, Documentary Series, Sports Broadcast / Sports Film, Music Video, Video Essay | genres: Science / Educational, Nature / Wildlife, Action, Thriller / Suspense, Surreal / Absurdist  
**Avoid when:** It drinks light and produces huge files, so it does not suit a light setup. It also records no usable sync sound.  
**Prompt:** `high-speed camera capture, the splash exploding upward in ultra slow motion, hard bright lighting`  
**Yields to:** `time.post_retime` — A light setup with no high-speed body; retime in post.  
`rig.high_speed_camera`

### 360 Camera

**Also called:** spherical camera, VR camera, insta-style dual lens  
**What it is:** A camera with two or more lenses recording the full sphere around it, from which you can later extract a normal frame or present the whole scene as a look-around experience.  
**Effect on the audience:** It moves the framing decision off the set and into the edit. In spherical playback the viewer becomes the director and chooses where to look.  
**Used for and where it works best:** Virtual reality and location tours, impossible angles with the camera in the middle of the action and no operator, and cutting vertical clips out of a single capture. It is useful in documentary for an event that will not repeat.  
**Best in:** formats: 360 / VR, Vertical Short-Form (Reels, Shorts, TikTok), Travel / Real Estate / Hospitality, Documentary Feature, Corporate / Training, Wedding / Event Film, Concert / Live Event, Game Cinematic / Gameplay | genres: Adventure, Science / Educational, Slice of Life, Nature / Wildlife, Family, Heritage (civilisation-focused)  
**Avoid when:** Image quality is lower than a normal camera at the same price, and the stitch line shows when anything is close. In spherical playback, fast cutting makes viewers ill.  
**Prompt:** `360 spherical capture from the centre of the circle, reframed later into a single moving shot`  
`rig.camera_360`

### Rotating Set Rig

**Also called:** gimbal set, rotating room, tumbling corridor  
**What it is:** The set itself, a room or a corridor, is built inside a rotating frame, with the camera fixed to the set and turning with it. The actor is the only element fighting gravity. This entry is the structure, its construction and its safety, unlike The Rotating Set Shot in the signature moves chapter, which covers the shot and its function in the story.  
**Effect on the audience:** Gravity collapses for real. Because everything is practical rather than computed, the viewer believes the wall has become the floor.  
**Used for and where it works best:** A fight without gravity, a dream or a reality flipping over, a spacecraft interior, and the music video where the singer walks up the wall. The rule: lock the camera to the set so the frame stays stable and it is the world that appears to turn.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Trailer / Teaser, 3D CG Animation, Short Film, Title Sequence / Opening Credits | genres: Sci-Fi, Fantasy / Epic, Action, Surreal / Absurdist, Psychological / Arthouse, Musical, Superhero  
**Avoid when:** Heavy construction, real cost and real risk to the performer, so only build it for a shot the story turns on.  
**Prompt:** `rotating room rig, the camera locked to the set as the whole corridor turns and he walks up the wall`  
**Example:** Inception, the rotating hotel corridor.  
`rig.rotating_set`

### Roll Rig

**Also called:** camera roll, barrel roll, dutch spin rig  
**What it is:** A head or mount that rotates the camera around its own lens axis during the take, so the horizon tilts and turns instead of staying level.  
**Effect on the audience:** The viewer loses the point of stability. A slow roll reads as fainting or falling, a fast one as chaos or an impact.  
**Used for and where it works best:** A faint, a drowning, a blast, a dream, or a character falling. In music video and trailers it is used as a short rhythmic hit on the beat.  
**Best in:** formats: Feature Film, Music Video, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, 3D CG Animation, Anime (Japanese 2D), Short Film | genres: Action, Horror, Psychological / Arthouse, Sci-Fi, Surreal / Absurdist, Thriller / Suspense, Musical  
**Avoid when:** A full roll with no reason reads as a toy, and on a small screen it makes viewers dizzy fast.  
**Prompt:** `the camera rolls slowly around the lens axis as he falls backward, horizon turning over`  
`rig.roll_rig`

### Phone Rig

**Also called:** phone cage, phone gimbal, vertical phone rig  
**What it is:** A cage, a grip or a small gimbal for a phone, often with an add-on lens and a small light, held in the hand or locked onto a stand in vertical orientation.  
**Effect on the audience:** Closeness and honesty. The phone reads as a shot from inside the event rather than outside it, and on social the viewer trusts it more than a polished image.  
**Used for and where it works best:** Vertical reels, micro-drama, instructional clips, shop and restaurant content. This card chooses the phone support: use the small gimbal to walk with a person and the cage on a stand for a talking head only when performance, demonstration or graphics keep changing inside the frame. A visually dead locked take still yields to movement under `rig.tripod_locked`.
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Vlog / YouTube Long-Form, Meme / Comedy Edit, Product Video / Motion Design, Corporate / Training, Kids Content, News Report / Reportage | genres: Comedy, Slice of Life, Melodrama, Family, Romance, True Crime  
**Avoid when:** In low light the image falls apart quickly, so do not rely on it for a night scene without added light.  
**Prompt:** `shot on a phone rig, vertical framing, close and immediate, natural handheld feel`  
`rig.phone_rig`

### Rig Handoff Inside a Oner

**Also called:** rig transfer, invisible rig change, one-take handover  
**What it is:** A long take begins on one rig and transfers to another mid-move: Steadicam to crane, to a vehicle, to a cable, to handheld, with the handover hidden behind a wall, a shadow or a passing body.  
**Effect on the audience:** It sells an impossible single shot. The space feels completely continuous so the tension never gets a break.  
**Used for and where it works best:** The long single-take sequences of war and battle, moving from a tight space into a huge one, and any sequence that must feel uncut. It has to be planned on paper with every department before the day: where the handover happens, who takes it, and what hides it.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Trailer / Teaser, Limited Series, Commercial / TVC, Short Film | genres: War, Action, Drama, Thriller / Suspense, Crime / Procedural, Historical / Biopic  
**Avoid when:** One mistake at the handover burns the entire take and sends you back to the top. Do not attempt it if the scene gains nothing from continuity.  
**Prompt:** `one continuous move handing from a stabilised rig to a crane behind the wall, no visible cut`  
**Example:** 1917, the continuous-take sequences.  
`rig.handoff`

### Virtual Camera

**Also called:** virtual production camera, game engine camera, vcam  
**What it is:** A camera-shaped device or a tracked tablet held in the hand whose position in the real room drives a camera inside a 3D scene in a game engine or an animation package. It differs from the Virtual Camera in the 3D chapter, which is the camera object inside the software: here the subject is the physical device a human operator drives it with.  
**Effect on the audience:** It returns human instinct to a generated image. The shake, the hesitation and the search for the frame all print through, so a virtual scene feels photographed rather than calculated.  
**Used for and where it works best:** Shooting 3D animation and game cinematics, scouting virtual locations before the shoot, and designing effects shots with the director. It is a planning gift: walk the virtual location and choose the shots before anything is built.  
**Best in:** formats: 3D CG Animation, Game Cinematic / Gameplay, AI-Generated Clip, Commercial / TVC, Feature Film, Trailer / Teaser, Title Sequence / Opening Credits, Anime (Japanese 2D) | genres: Sci-Fi, Fantasy / Epic, Action, Adventure, Superhero, Mythology / Ancient Epic, Space Opera  
**Avoid when:** Total freedom tempts you into moves that could never exist, and the result feels like a video game. Pick an imaginary rig and stay inside its limits.  
**Prompt:** `virtual camera operated by hand inside the 3D scene, subtle human handheld imperfection`  
**Example:** The Lion King, shot with a virtual camera system.  
`rig.virtual_camera`

### LED Volume Stage

**Also called:** virtual production wall, ICVFX, the volume  
**What it is:** A stage surrounded by huge LED screens playing a real-time 3D background that shifts with the tracked camera position, so the parallax is correct in camera.  
**Effect on the audience:** The actor stands inside the place instead of in front of green. The light and reflections from the wall fall on faces and metal, so the integration reads as real.  
**Used for and where it works best:** Car, aircraft and space interiors, distant or dangerous locations, and any scene that needs the same sunset to hold for ten hours. It is excellent for heritage work: rebuild the ancient city as the background and let the actor stand inside its light.  
**Best in:** formats: Drama Series Episode, Feature Film, Commercial / TVC, Trailer / Teaser, 3D CG Animation, Corporate / Training, Heritage / Historical Documentary, Music Video | genres: Sci-Fi, Space Opera, Fantasy / Epic, Western, Historical / Biopic, Heritage (civilisation-focused), Action  
**Avoid when:** It is expensive and needs finished 3D assets before the shoot day. The space is finite, so very wide shots expose the edge of the wall.  
**Prompt:** `virtual production on an LED volume, accurate reflections and correct parallax behind the actor`  
**Example:** The Mandalorian.  
**Yields to:** `rig.process_trailer` — A driving scene with no finished 3D assets or volume budget.  
`rig.led_volume`

### The Invisible Rig

**Also called:** rig removal, wire removal, painted-out support  
**What it is:** A support, an arm or a wire that is visible on set and then painted out in post using a clean plate of the background shot under identical light.  
**Effect on the audience:** An object flies or stands in space with no explanation. The viewer finds no physical cause, so the image reads as magic or a fault in reality.  
**Used for and where it works best:** The floating product in a commercial, suspended objects in fantasy, stop-motion puppets, and anything that needs a support that must not be seen. The golden rule: shoot a clean plate under the same light and with the same move before you strike the rig.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Feature Film, 3D CG Animation, Stop Motion, Music Video, Trailer / Teaser, Title Sequence / Opening Credits | genres: Fantasy / Epic, Sci-Fi, Surreal / Absurdist, Superhero, Fairy Tale, Action  
**Avoid when:** Without the clean plate shot on location the work multiplies and sometimes becomes impossible. The rig's shadow and reflection are harder to remove than the rig itself.  
**Prompt:** `the object hangs in mid-air with its support removed, clean background, matching shadows`  
`rig.invisible_rig`

### Monopod

**Also called:** unipod, single leg support  
**What it is:** A single column carrying the camera from below and resting on the ground, which removes vertical shake while leaving pan and tilt free. The operator stays standing and moves with one step.  
**Effect on the audience:** The image looks settled without looking locked, so the scene keeps the presence of a person behind the camera. The viewer feels live following rather than machinery.  
**Used for and where it works best:** Sports, demonstrations, weddings and festival coverage, long lens work where the weight wears out the arms, and locations where a tripod is not allowed. It shines in field documentary when you have to move fast between two positions and still deliver usable frames.  
**Best in:** formats: Sports Broadcast / Sports Film, News Report / Reportage, Documentary Feature, Wedding / Event Film, Concert / Live Event, Travel / Real Estate / Hospitality, Vlog / YouTube Long-Form, Documentary Series, Interview / Video Podcast | genres: Verite / Observational, Sports Drama, Social Drama, Political Thriller, Heritage (civilisation-focused), Nature / Wildlife, True Crime  
**Avoid when:** It usually falls short on a long static shot because the body sways with the breathing and an unintended drift appears. The exception is when that slight life is wanted, to give a reportage the feeling of a present witness.  
**Prompt:** `monopod supported shot, long lens following a runner across the field, stable vertically with a slight human sway, panning with the action`  
**Yields to:** `rig.tripod_locked` — A long static shot, where breathing drift appears.  
`rig.monopod`
