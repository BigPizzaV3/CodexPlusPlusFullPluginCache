# Core Camera Moves

114 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Ask the Shape and the Run Separately

**Also called:** the move selector, shape before run, two questions before the camera moves  
**What it is:** The card at the head of the `move.` shelf. It does not describe a move. It asks first **which of this shelf's two decisions you are making** — the shape the viewpoint takes, or the way that shape is run in time — and then the three questions that split whichever half you landed in, handing back a named shortlist for each answer. The axes were not invented. They were read off the shelf's own `Yields to:` conditions and its `Avoid when:` lines, and the conditions that repeated became the questions. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the move that does reach the screen was chosen against the space, the subject and the clock, instead of being the move that was remembered.  
**Used for and where it works best:** Answer the fork out loud first, then the three questions of that half, one sentence each, **before you open the shelf**. On the shape side the first question eliminates roughly half the file and the second and third leave three to six cards. On the run side the three questions do not intersect: each card answers exactly one of them, so you take one card from each and you have a complete instruction. If you cannot say what has to be different by the last frame, you are not choosing a move yet, you are still blocking the shot.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The camera is not yours to move.** A supplied plate, an archive frame, a locked reference still: there the move is an after-effect decision on material that already exists, and none of these questions has an answer. **Distrust the first shape question whenever your honest answer is its third value** — forty-two of the eighty-seven shape cards live under *the camera's standpoint changes*, so on any travelling shot this map has only two questions left and is doing two-thirds of the work it does elsewhere. **And the map stops at the floor.** The moment the answer is *the camera is off the ground*, the decision that mattered was made on `rig.` before this shelf opened — measured, not one `Yields to:` edge runs between `move.` and `rig.` in either direction, so this shelf has no field that can tell you so and will happily hand you a shortlist for a rig you do not have. It is also not a route to a signature move: seventeen edges run from `sig.` into this shelf and none run back, so this map is where you land when a named move is refused, never the way to reach one.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**The first fork — is the move already chosen, and you are deciding how it runs?**
Asked before anything else, and it is measured rather than assumed. `SHELVES.md` §2b requires it of every shelf and warns that a selector built on the wrong answer cannot be repaired by adding a question later. Split the shelf into **the cards that decide what the viewpoint does in space** and **the cards that decide how that is performed in time**, then count the within-shelf `Yields to:` edges across the seam: **forty-five edges stay inside the shape half, twelve stay inside the run half, and zero cross.** Not few — none. The pair graph is two disconnected components, and the readers who wrote those sixty edges never once offered a speed curve as an alternative to a camera path. That is the whole argument, and it survives because it does not depend on filing: this shelf is one file in one phase, so the usual tell is unavailable and the graph had to answer instead.

**And the two halves are not the same kind of shelf, which is why their maps are not the same shape.** Every shape card has an answer to all three shape questions — a move always changes something, is always meant to be felt by some amount, and always has a permitted register. The run half does not work that way: `move.ease_in_out` has no answer to *what fires it*, and `move.move_on_beat` states no rate. So SHAPE is intersected and RUN is partitioned, one card under one value of one question. **That difference is measurable and it is a second, independent argument for the fork.**

---

**SHAPE — you are deciding what the viewpoint does**

**Axis S1 — What actually has to be different by the last frame: where the camera aims, where it stands, what the lens is doing, or nothing?**
The condition the shape half repeats most, and it is mechanical rather than expressive. Eleven conditions turn on it: *"Connecting two things at different distances needs depth"* (`move.pan`) and its twin *"Carved relief, where a pan flattens the depth"* (`move.survey_pan`); *"When the shot must feel cinematic; zoom flattens"* (`move.zoom_in`); *"Emotional endings need the weight of departure"* (`move.zoom_out`); *"Serious drama; move the camera, do not zoom"* (`move.crash_zoom`); *"Designed drama, where zoom-pan reads as news television"* (`move.zoom_pan`); *"Cinematic work, where a zoom correction reads as mistake"* (`move.reframe_zoom`); *"You need approach but no angle change"* (`move.diagonal_dolly`); *"You need a pure vertical, no arc"* (`move.boom`); *"You need a tilt while climbing"* (`move.pedestal_up`); *"Emotional beat on a face needs closeness"* (`move.overhead_track`). **Six of the eleven are a card handing a reader from the optics to the standpoint and never the reverse** — the shelf argues in one direction about this, and that is worth knowing before you ask.

**Axis S2 — How much of the move is the viewer meant to feel: nothing, a move, or the whole point of the shot?**
Thirteen conditions turn on it, and they are stated as facts about what the frame contains and how long it has, not about feelings: *"A short shot, where a creep never registers"* (`move.creep_in`); *"Fast cutting, where the slow reverse zoom does nothing"* (`move.slow_zoom_out`); *"A fast scene, where a slow tilt kills rhythm"* (`move.reveal_tilt`) against *"A long quiet scene, which the snap breaks"* (`move.whip_tilt`); *"The context is predictable; no reversal to stage"* (`move.pullback_reveal`); *"An empty background, where the turn never registers"* (`move.arc`); *"Empty or repetitive background; profile walk reads motionless"* (`move.side_track_walk`); *"The empty frame says nothing; the wait dies"* (`move.stay_actor_leaves`) against *"The place or the distance is the point"* (`move.walk_with_actor`); *"Every still in a documentary getting the same zoom"* (`move.slow_zoom`); *"The shot must stay readable; rotation prevents reading"* (`move.orbit_360`); *"A rigorously designed or symmetrical composition"* (`move.nudge`) against *"AI clips and long takes, where perfect stillness reads synthetic"* (`move.lock_off`).

**Axis S3 — Whose hand may show: a person's, nobody's, or nobody who could exist?**
Fourteen conditions, the loudest block on the shelf, and they name the piece rather than the audience. One group forbids the impossible: *"Grounded drama, where a full roll shows off"* (`move.roll_360`); *"Grounded drama, where passing matter breaks world logic"* (`move.push_through`); *"Quiet or grieving scene, where the whip reads violent"* (`move.whip_pan`); *"A quiet or grieving scene the crash flattens"* (`move.crash_in`); *"A serious scene, where the snap overstates"* (`move.crash_zoom_out`); *"A calm scene, where the speed breaks mood"* (`move.snap_focus`); *"A realistic scene, where weightlessness looks purposeless"* (`move.float`); *"Serious documentary, where a close fast pass reads as marketing"* (`move.fly_by`); *"Grounded quiet scene, where the retreat reads as swagger"* (`move.reverse_dolly`). The other group forbids the visible operator, and it is a different set of cards rejected by a different kind of piece: *"A polished, precisely designed scene"* (`move.overshoot_correct`); *"A formal or polished scene; sway reads as error"* (`move.handheld_sway`); *"Rigorous symmetry or a polished commercial"* (`move.breathing`); *"A polished production, where hunting reads as incompetence"* (`move.searching_zoom`); *"A chaotic scene that stabilised smoothness contradicts"* (`move.floating_follow`). **Two opposite bans, and no card is caught by both, which is what makes this three values and not two.** Asked last, because it is the only axis that separates cards the first two have already put in one cell.

---

**RUN — you are deciding how the move is performed**

**Axis R1 — Does the rate change inside the shot, and if it does, where?**
Six conditions, every one naming a kind of scene rather than a feeling: *"A realistic scene, where stepped motion reads as fault"* (`move.stutter`); *"An emotional scene, where constant speed kills feeling"* (`move.linear_move`) against its exact reverse *"A machine, system or surveillance feel"* (`move.ease_in_out`); *"Grounded drama, where the hard curve shatters illusion"* (`move.snap_timing`); *"When the hit is the point, not arrival"* (`move.settle`); *"Escalation without a readable stop in the middle"* (`move.two_stage_move`).

**Axis R2 — What decides the instant the move begins?**
Four conditions, and they turn on where the trigger lives: *"Horror, where the camera needs its own agenda"* (`move.motivated_move`) against *"Comedy or family drama, odd for nothing"* (`move.unmotivated_move`); *"Vertical short-form, where a static head loses the viewer"* (`move.hold_then_move`) against *"Quiet or formal scenes, where it looks mistrimmed"* (`move.start_in_motion`). The four cue cards under this axis state theirs in `Avoid when:` instead, and it is the same question asked of the sound track: *"Start before the line and the camera admits it knows what is coming"* (`move.move_on_line`), *"If the move goes the other way from the glance the viewer loses the geography"* (`move.move_on_look`), *"If the camera moves before or exactly with the sound, cause and effect are lost"* (`move.move_on_sound`), *"If every move lands on every beat the piece becomes a metronome"* (`move.move_on_beat`).

**Axis R3 — How does the move meet the cut?**
The axis that lives almost entirely in `Avoid when:`, which is why it was nearly missed. Only two of its cards state a condition in `Yields to:` — *"Action, chases and short-form; cut on motion"* (`move.settle_before_cut`) and *"Building one continuous take from short AI clips"* (`move.move_then_hold`) — while the rest put the same question in their warnings: *"If direction or speed differ much between the two shots, the cut becomes more visible rather than less"* (`move.move_across_cut`), *"If the internal action is weak it hides nothing and exposes the camera instead"* (`move.masked_move`), *"The ending has to be a frame you can actually cut from"* (`move.three_part_move`), *"Any unmotivated change of direction destroys the geography of the scene"* (`move.screen_direction_move`).

---

**The map**

**Axis S1 — what has to be different by the last frame**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Only the aim — the camera holds its spot and turns** (seventeen) | `move.pan` · `move.survey_pan` · `move.follow_pan` · `move.reveal_pan` · `move.pan_and_settle` · `move.whip_pan` · `move.pan_handoff` · `move.pan_360` · `move.tilt_up` · `move.tilt_down` · `move.reveal_tilt` · `move.whip_tilt` · `move.pan_tilt_compound` · `move.roll_partial` · `move.roll_360` · `move.dutch_roll_tilt` · `move.overshoot_correct` |
| **Nothing arrives anywhere — what you are choosing is how still it is** (nine) | `move.lock_off` · `move.nudge` · `move.recoil` · `move.handheld_sway` · `move.breathing` · `move.hover` · `move.float` · `move.drift` · `move.impact_shake` |
| **The camera's standpoint — it travels** (forty-two) | `move.dolly_in` · `move.creep_in` · `move.crash_in` · `move.dolly_out` · `move.pullback_reveal` · `move.truck` · `move.lead_track` · `move.trail_track` · `move.side_track_walk` · `move.counter_track` · `move.diagonal_dolly` · `move.reverse_dolly` · `move.dolly_past` · `move.dolly_through` · `move.push_through` · `move.through_object` · `move.overhead_track` · `move.walk_with_actor` · `move.stay_actor_leaves` · `move.chase` · `move.floating_follow` · `move.lean_in` · `move.step_back` · `move.pendulum` · `move.pedestal_up` · `move.pedestal_down` · `move.boom` · `move.crane_up` · `move.crane_down` · `move.jib_arc` · `move.arc` · `move.orbit_360` · `move.spiral` · `move.corkscrew` · `move.vertical_drop` · `move.rise_reveal` · `move.fly_over` · `move.fly_through` · `move.fly_by` · `move.swoop` · `move.dive` · `move.climb` |
| **Only the optics — what is big and what is sharp** (nineteen) | `move.zoom_in` · `move.zoom_out` · `move.slow_zoom` · `move.slow_zoom_out` · `move.crash_zoom` · `move.crash_zoom_out` · `move.micro_zoom` · `move.zoom_pan` · `move.zoom_detail_cut` · `move.searching_zoom` · `move.reframe_zoom` · `move.rack_focus` · `move.snap_focus` · `move.focus_reveal` · `move.focus_loss` · `move.follow_focus` · `move.three_plane_rack` · `move.split_diopter_device` · `move.focus_breathing` |

**Axis S2 — how much of it the viewer is meant to feel**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Nothing — under the threshold, and spoiled the moment it is noticed** (seventeen) | `move.roll_partial` · `move.lock_off` · `move.nudge` · `move.breathing` · `move.hover` · `move.float` · `move.drift` · `move.creep_in` · `move.stay_actor_leaves` · `move.lean_in` · `move.step_back` · `move.slow_zoom` · `move.slow_zoom_out` · `move.micro_zoom` · `move.reframe_zoom` · `move.follow_focus` · `move.focus_breathing` |
| **As a move — the viewer feels the camera go and that is fine** (thirty-nine) | `move.pan` · `move.survey_pan` · `move.follow_pan` · `move.pan_and_settle` · `move.pan_handoff` · `move.tilt_up` · `move.tilt_down` · `move.pan_tilt_compound` · `move.overshoot_correct` · `move.handheld_sway` · `move.dolly_in` · `move.dolly_out` · `move.truck` · `move.lead_track` · `move.trail_track` · `move.side_track_walk` · `move.counter_track` · `move.diagonal_dolly` · `move.reverse_dolly` · `move.dolly_past` · `move.dolly_through` · `move.overhead_track` · `move.walk_with_actor` · `move.floating_follow` · `move.pendulum` · `move.pedestal_up` · `move.pedestal_down` · `move.boom` · `move.jib_arc` · `move.arc` · `move.fly_over` · `move.climb` · `move.zoom_in` · `move.zoom_out` · `move.zoom_pan` · `move.searching_zoom` · `move.rack_focus` · `move.three_plane_rack` · `move.split_diopter_device` |
| **The move is the event — it is what the shot is about** (thirty-one) | `move.reveal_pan` · `move.whip_pan` · `move.pan_360` · `move.reveal_tilt` · `move.whip_tilt` · `move.roll_360` · `move.dutch_roll_tilt` · `move.recoil` · `move.impact_shake` · `move.crash_in` · `move.pullback_reveal` · `move.push_through` · `move.through_object` · `move.chase` · `move.crane_up` · `move.crane_down` · `move.orbit_360` · `move.spiral` · `move.corkscrew` · `move.vertical_drop` · `move.rise_reveal` · `move.fly_through` · `move.fly_by` · `move.swoop` · `move.dive` · `move.crash_zoom` · `move.crash_zoom_out` · `move.zoom_detail_cut` · `move.snap_focus` · `move.focus_reveal` · `move.focus_loss` |

**Axis S3 — whose hand may show**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A person's — the camera has a body and may sway, hunt, overshoot or flinch** (twelve) | `move.overshoot_correct` · `move.nudge` · `move.recoil` · `move.handheld_sway` · `move.breathing` · `move.impact_shake` · `move.chase` · `move.zoom_pan` · `move.searching_zoom` · `move.reframe_zoom` · `move.follow_focus` · `move.focus_breathing` |
| **Nobody who could exist — no body, no gravity, no matter in the way** (nineteen) | `move.whip_pan` · `move.whip_tilt` · `move.roll_360` · `move.dutch_roll_tilt` · `move.float` · `move.crash_in` · `move.push_through` · `move.through_object` · `move.orbit_360` · `move.spiral` · `move.corkscrew` · `move.vertical_drop` · `move.fly_through` · `move.fly_by` · `move.swoop` · `move.dive` · `move.crash_zoom` · `move.crash_zoom_out` · `move.snap_focus` |
| **Nobody — the move is clean, and it reads as the world rather than as the camera** (fifty-six) | Every other card named in the two tables above. It is named by complement on purpose: writing out fifty-six ids here would make the map longer than the half it maps, which is the one thing the shape of a selector forbids. |

*On the shape side a card appears once per axis, and the answer is the intersection of the three shortlists, normally three to six cards wide.*

**RUN — one card under one value of one question**

| Axis | Answer | The cards, by id |
| :--- | :--- | :--- |
| **R1 rate** | One rate, first frame to last | `move.linear_move` |
| **R1 rate** | Soft at the ends only | `move.ease_in_out` · `move.settle` |
| **R1 rate** | It changes in the middle, and the change is the content | `move.two_stage_move` · `move.speed_break` · `move.snap_timing` · `move.stutter` |
| **R2 start** | The scene fired it — something moved and the camera answered | `move.motivated_move` |
| **R2 start** | Nothing in the scene fired it; the camera has its own agenda | `move.unmotivated_move` |
| **R2 start** | A cue on the track fired it | `move.move_on_line` · `move.move_on_look` · `move.move_on_sound` · `move.move_on_beat` |
| **R2 start** | The clip's own edge decides — already running, or not yet started | `move.start_in_motion` · `move.hold_then_move` |
| **R3 cut** | It stops first, and you cut from a still frame | `move.settle_before_cut` · `move.move_then_hold` |
| **R3 cut** | It does not stop, and the next shot carries it | `move.move_across_cut` · `move.masked_move` |
| **R3 cut** | It is a designed unit with its own ending | `move.three_part_move` |
| **R3 cut** | It carries the sequence's direction and may not reverse | `move.screen_direction_move` |

---

**The default, and the one against it**

**The default is `move.dolly_in`, run on `move.ease_in_out`, fired by `move.motivated_move` — and only the first of those three is measured.** `move.dolly_in` is the most-yielded-to card on the shelf: five inbound edges from inside it, seven counting the whole package, more than anything else here. What makes it a default rather than a door out of the shelf is that **the five conditions are five different conditions drawn from four different axes**: duration — *"A short shot, where a creep never registers"* (`move.creep_in`); mechanism — *"You need approach but no angle change"* (`move.diagonal_dolly`); subject — *"The subject is the point; passing reads as neglect"* (`move.dolly_past`); scene — *"Emotional beat on a face needs closeness"* (`move.overhead_track`); register — *"When the shot must feel cinematic; zoom flattens"* (`move.zoom_in`). Asked five times for five unrelated reasons, the shelf falls back to the same place.

**`move.ease_in_out` is named default on much weaker evidence, and this card says so rather than hiding it.** It takes three inbound edges and **all three are one condition wearing three coats** — *"A realistic scene, where stepped motion reads as fault"*, *"An emotional scene, where constant speed kills feeling"*, *"Grounded drama, where the hard curve shatters illusion"*. One condition, three doors: by the measure that earns `move.dolly_in` its place, that is a repair for *the scene must not show the machine*, not a fallback. It stands here only because nothing on the shelf argues against it on any other ground, which is a weaker claim, and **a half with no measured default is a real gap, not a tidy answer.**

**The one against it is `move.through_object`.** Nothing on this shelf routes to it and nothing anywhere in the package does either. It is the only card here whose content is **two unrelated spaces joined by one continuous move** — every other travelling card assumes the camera stays in the room it started in, which is the founding assumption of the whole shape half, and this one simply does not make it. Its only stated cost is staging: the material has to genuinely fill the frame at the moment of passage, which a designed keyframe pays for nothing while a real location pays for it dearly. Its near cousin against the grain is `move.masked_move`, likewise reached by nothing, which inverts the other assumption — every other card exists to make the move visible, and that one spends the whole move hiding a cut inside it.

---

**The unasked**

**Fifty-eight of the hundred and eight reachable cards are the target of no `Yields to:` field anywhere in the package.** They can be chosen and nothing ever sends you to them. By id:

`move.survey_pan` · `move.follow_pan` · `move.pan_handoff` · `move.pan_360` · `move.tilt_down` · `move.reveal_tilt` · `move.pan_tilt_compound` · `move.roll_360` · `move.dutch_roll_tilt` · `move.recoil` · `move.overshoot_correct` · `move.move_then_hold` · `move.settle` · `move.stutter` · `move.side_track_walk` · `move.counter_track` · `move.reverse_dolly` · `move.dolly_past` · `move.push_through` · `move.through_object` · `move.overhead_track` · `move.chase` · `move.lean_in` · `move.step_back` · `move.pendulum` · `move.pedestal_down` · `move.boom` · `move.crane_down` · `move.jib_arc` · `move.spiral` · `move.corkscrew` · `move.rise_reveal` · `move.fly_through` · `move.fly_by` · `move.swoop` · `move.dive` · `move.climb` · `move.hover` · `move.float` · `move.zoom_out` · `move.slow_zoom_out` · `move.crash_zoom` · `move.zoom_detail_cut` · `move.searching_zoom` · `move.reframe_zoom` · `move.snap_focus` · `move.focus_loss` · `move.follow_focus` · `move.three_plane_rack` · `move.focus_breathing` · `move.three_part_move` · `move.move_on_line` · `move.move_on_look` · `move.move_on_sound` · `move.move_on_beat` · `move.masked_move` · `move.settle_before_cut` · `move.screen_direction_move`

**And the shape of that list is the finding, not its length. Two shapes, in fact.**

**First: the shelf stops arguing the moment the camera leaves the ground.** Take every card whose move is lifted, craned or flown — twenty of them — and **fifteen are on this list**. Of the five that are ever routed to, three are reached only from another lifted card (`move.boom` → `move.pedestal_up`, `move.pedestal_up` → `move.crane_up`, `move.fly_by` → `move.fly_over`) and the remaining two, `move.orbit_360` and `move.vertical_drop`, are reached only from outside the shelf entirely. **Not one lifted card is reached from the ground.** Nothing here says *if the boom cannot climb, fly instead*, and nothing says the reverse. Put that beside the measurement in this card's own `Avoid when:` — zero edges between `move.` and `rig.` in either direction — and it is one fact, not two: getting the camera off the ground is settled on the rig shelf before this one opens, so by the time a reader arrives here that choice is already spent and the pair field has nothing left to say about it. **A move the production cannot physically make is not an alternative to one it can**, and this field cannot express that.

**Second: a run card is reached only when some other card is its exact opposite.** Every reached run card sits on one end of an opposed pair — `move.ease_in_out` against `move.linear_move`, `move.motivated_move` against `move.unmotivated_move`, `move.hold_then_move` against `move.start_in_motion`, `move.settle_before_cut` against `move.move_across_cut`. Every unreached one belongs to a set with no opposite in it. The four cue cards of axis R2 are **a choice set, not a pair**: a line, a look, a sound and a beat are four different things to key a move to, and none is the wrong version of any other. **A reader asked to name one alternative can answer for an opposed pair and cannot answer for a choice set**, so the whole cue block and most of R3 came through the audit silent. That is a property of the question the field asks, not a defect in these cards, and it is exactly why axis R3 had to be built out of `Avoid when:` instead.

**The new card this shelf wants** follows from the first shape. Every travelling card here assumes clear floor and open air; not one of them is about the room refusing the move. The nearest thing that exists is a warning buried inside `move.boom` — *in a cramped space or under a low ceiling the arc breaks halfway and the rig shows* — with its twin inside `move.dolly_through`, *a narrow opening taken at speed produces nausea rather than immersion*. **The shelf knows a space can defeat a move, and has no card that says so**, and nothing routes a reader to either warning. The missing card starts from the room's dimensions and hands back the moves that fit inside them.

`move.shape_then_run`

---

### Pan

**Also called:** pan left, pan right, horizontal pan  
**What it is:** The camera pivots left or right on its vertical axis while staying in one spot, the way you turn your head. Nothing travels through space; only the direction of the look changes.  
**Effect on the audience:** It ties two things to one place: this, and this with it. The viewer feels they turned to look, not that they moved closer.  
**Used for and where it works best:** Surveying a place, following someone who walks on a flat line, or revealing something beside the character inside the same room. In documentary and heritage work it is the proof that what you just saw and what comes next share one location, and in drama it carries a character's look to its target without a cut.  
**Best in:** formats: all | genres: all  
**Avoid when:** When you need to connect two things that sit at different distances. A pan gives width, not depth; use a track or a dolly instead. A pan with no motivation and no resting point becomes aimless wandering.  
**Prompt:** `slow pan right from the empty doorway across the room, even speed, coming to rest on his face`  
**Yields to:** `move.truck` — Connecting two things at different distances needs depth.  
`move.pan`

### Slow Survey Pan

**Also called:** landscape pan, scanning pan  
**What it is:** A slow, constant-speed pan across a landscape, a wall or a space, following nothing that moves. The place itself is the subject.  
**Effect on the audience:** It gives the eye time to read detail and tells the viewer this place is worth reading.  
**Used for and where it works best:** Opening a location in heritage documentary: a wall, a ruin, a city roofline at dawn — a carved relief goes to `move.truck`, whose track keeps the depth a pan flattens. In quiet drama it sweeps a room after its owner has gone. Best when narration or score runs over the shot and needs a long, unhurried bed.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Documentary Series, Feature Film, Video Essay, Travel / Real Estate / Hospitality, Title Sequence / Opening Credits, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Drama, Mythology / Ancient Epic, Science / Educational, Psychological / Arthouse  
**Avoid when:** When the place has no detail worth reading it turns into dead time. Any change of speed during the sweep breaks the spell and exposes the operator's hand.  
**Prompt:** `very slow steady pan left across the ruined city wall, constant speed throughout, ending on the last standing tower`  
**Yields to:** `move.truck` — Carved relief, where a pan flattens the depth.  
`move.survey_pan`

### Follow Pan

**Also called:** tracking pan, panning with the action  
**What it is:** A pan that follows a moving subject and holds it more or less fixed in frame: a person, a horse, a car, a bird. Its speed is dictated by the subject, not by a metronome.  
**Effect on the audience:** It locks your eye to the subject and lets the background streak behind it, so the speed reads as greater than it is.  
**Used for and where it works best:** Staying with a player, a rider or a car in sport and action, or with a person crossing a square in documentary. On a long lens it gets stronger, because the background sweeps faster and smears into streaks.  
**Best in:** formats: Sports Broadcast / Sports Film, Feature Film, Documentary Feature, Drama Series Episode, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Game Cinematic / Gameplay | genres: Action, Adventure, Sports Drama, War, Western, Thriller / Suspense, Nature / Wildlife, Shonen Battle (anime)  
**Avoid when:** When the subject changes direction unpredictably the pan turns into a failed chase. If the background is empty and featureless the move reads as no move at all.  
**Prompt:** `pan following him as he crosses the courtyard, holding him on the left third, decelerating as he stops at the gate`  
**Yields to:** `move.floating_follow` — Subject changes direction unpredictably; a fixed pivot fails.  
`move.follow_pan`

### Reveal Pan

**Also called:** revealing pan  
**What it is:** A pan that starts on something known and keeps going until it uncovers something that was not in frame: a figure in the corner, a body, an open door, an army.  
**Effect on the audience:** It makes the reveal happen in real time without a cut, so the viewer discovers at the same instant the character does.  
**Used for and where it works best:** In horror and suspense: pan off the sleeping face and keep going to the open door. In drama: pan from the speaker to the person who has been silent in the same room the whole time. In heritage work: pan off one small detail onto the whole structure.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Trailer / Teaser, Heritage / Historical Documentary, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Game Cinematic / Gameplay | genres: Horror, Thriller / Suspense, Mystery / Whodunit, Supernatural Horror, Drama, War, Heritage (civilisation-focused), Psychological Horror  
**Avoid when:** If the reveal arrives too fast nobody gets to want it. Keep the ground before it long enough for anticipation to build, and short enough that the viewer does not spot the trick coming.  
**Prompt:** `pan right off her face, continuing across the empty room, revealing a figure standing motionless in the corner, holding on him`  
`move.reveal_pan`

### Pan and Settle

**Also called:** pan to frame, settling pan  
**What it is:** A pan that decelerates softly into a composition you designed in advance and holds there until the cut. The ending, not the path, is the point.  
**Effect on the audience:** A feeling of arrival and decision. The viewer senses the shot has reached the place it was always going, and that something is about to happen.  
**Used for and where it works best:** Just before the key line in drama, just before the product lands in an ad, just before the first blow in action. Best when you intend to cut afterwards, because the final frame is stable and clean enough to cut from with confidence.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Product Video / Motion Design, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Anime (Japanese 2D), Documentary Feature | genres: Drama, Thriller / Suspense, Action, Crime / Procedural, Romance, Historical / Biopic, Heritage (civilisation-focused), Comedy  
**Avoid when:** If you never designed the end frame the whole move has no destination. Do not stop dead either; a hard stop reads as violence, not as arrival.  
**Prompt:** `pan left across the table, easing out and settling on the untouched glass, locked and still before the cut`  
`move.pan_and_settle`

### Whip Pan / Swish Pan

**Also called:** swish pan, flick pan, zip pan  
**What it is:** A pan so fast the middle of it smears into horizontal blur, snapping onto a new frame. The start and end read clean; the middle is deliberately destroyed.  
**Effect on the audience:** Pure energy and impact. The mind cannot read the middle, so it registers a jump, and that jump can hide a cut inside it.  
**Used for and where it works best:** Comedy, snapping between two people for the reaction; action, when something arrives from the side; vertical short-form, to change location without the viewer feeling a cut. The strongest use is a whip out of scene one and a whip in the same direction into scene two.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, Feature Film, Drama Series Episode, Commercial / TVC, Trailer / Teaser, Music Video, Anime (Japanese 2D), Game Cinematic / Gameplay, Vlog / YouTube Long-Form | genres: Comedy, Action, Dark Comedy / Satire, Thriller / Suspense, Adventure, Martial Arts / Wuxia, Shonen Battle (anime), Rom-Com  
**Avoid when:** In a quiet or grieving scene it lands as violence from another film. Repeat it every few seconds in a reel and the viewer tires of it and starts seeing the technique instead of the content.  
**Prompt:** `whip pan right with heavy horizontal motion blur, snapping to a hard stop on the second man already mid-sentence`  
**Yields to:** `move.pan` — Quiet or grieving scene, where the whip reads violent.  
`move.whip_pan`

### Pan Handoff / Character Handoff

**Also called:** handoff pan, passing the camera off  
**What it is:** The camera pans with one person until they cross a second person, then lets the first go and continues with the new one. The first subject walks out of frame; the second inherits it.  
**Effect on the audience:** It makes the scene feel like a world running on its own rather than a set of assembled shots. The viewer is handed from one story to the next without noticing the exchange.  
**Used for and where it works best:** Crowded scenes: a market, a restaurant kitchen, a hospital corridor, a workshop, a royal court. In series and documentary it buys you a rich establishing beat in one shot, and in advertising it links three products or three people on a single move.  
**Best in:** formats: Drama Series Episode, Feature Film, Documentary Feature, Documentary Series, Commercial / TVC, Heritage / Historical Documentary, Corporate / Training, Music Video, Game Cinematic / Gameplay | genres: Drama, Comedy, Crime / Procedural, Medical Drama, Historical / Biopic, Heritage (civilisation-focused), Slice of Life, Political Thriller  
**Avoid when:** A handoff with no dramatic reason is cold technical showing off. Both halves must travel in the same direction, otherwise the camera reads as hesitating.  
**Prompt:** `pan with the waiter crossing the kitchen, releasing him as he passes the chef, continuing right and settling on the chef's hands`  
`move.pan_handoff`

### Full 360 Pan

**Also called:** full rotation pan, in-place 360  
**What it is:** The camera turns a complete circle on its own axis from one fixed position, showing the entire space from a single point.  
**Effect on the audience:** It says: this is everything around you. Slow, it reads as being surrounded; fast, it reads as vertigo.  
**Used for and where it works best:** The moment a character realises they are surrounded: the middle of a battlefield after the fighting, the middle of a crowd, the middle of a ruin. In heritage documentary it presents a temple chamber or a whole courtyard in one honest unbroken shot.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, 360 / VR, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Music Video, AI-Generated Clip | genres: War, Horror, Heritage (civilisation-focused), Survival, Psychological / Arthouse, Dystopia / Post-Apocalyptic, Mythology / Ancient Epic, Thriller / Suspense  
**Avoid when:** In an empty or repetitive space it is a full circle with no information. Watch the start frame too: if you come back to exactly what you left and nothing has changed, the shot has no ending.  
**Prompt:** `full 360 degree pan from a fixed position in the centre of the ruined hall, slow and even, ending back on the broken doorway`  
`move.pan_360`

### Tilt Up

**Also called:** upward tilt, tilt to the sky  
**What it is:** The camera pivots upward on its horizontal axis from a fixed position, starting low on the ground or a base and ending on a summit or the sky.  
**Effect on the audience:** Awe and scale. The mind reads a rise in the frame as a rise in status: this thing is larger than you.  
**Used for and where it works best:** Revealing a building, a statue or a ziggurat from base to summit in heritage documentary, and introducing a character from boots to face in drama and westerns. In battle anime a brisk tilt up the opponent sets the fight before a blow is thrown.  
**Best in:** formats: Heritage / Historical Documentary, Feature Film, Documentary Feature, Trailer / Teaser, Anime (Japanese 2D), 3D CG Animation, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Fantasy / Epic, War, Drama, Western, Shonen Battle (anime), Faith / Biblical Epic  
**Avoid when:** If what waits at the top does not deserve the wait, the shot turns into an anticlimax. Do not use it on something short; a tilt needs real height to earn itself.  
**Prompt:** `slow tilt up from the base of the ziggurat, climbing the brick terraces, ending on the summit against an open sky`  
`move.tilt_up`

### Tilt Down

**Also called:** downward tilt  
**What it is:** The camera pivots downward from a fixed position, starting high on a sky, a face or a ceiling and ending on the ground or on something low.  
**Effect on the audience:** Descent and confrontation. A fall in the frame reads as a fall in state: from the idea to the fact, from the face to the blood.  
**Used for and where it works best:** From a character's face down to a shaking hand, from the sky down to a battlefield after the fighting, from a statue down to the offerings at its feet in heritage work. In crime: from the lit windows down to the body in the alley.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Trailer / Teaser, Anime (Japanese 2D), Short Film, AI-Generated Clip, Game Cinematic / Gameplay | genres: Crime / Procedural, Drama, War, Noir / Neo-Noir, Horror, Heritage (civilisation-focused), Mystery / Whodunit, Tragedy, Historical / Biopic  
**Avoid when:** With nothing worth finding at the bottom it is a descent into nowhere. Do not run it for shape alone; the descent must deliver new information.  
**Prompt:** `slow tilt down from his face to his hands, finding the blood on his knuckles, settling there`  
`move.tilt_down`

### Reveal Tilt

**Also called:** tilt reveal  
**What it is:** A tilt built so that its second half uncovers something completely hidden at the start: a body under a sheet, an army behind a ridge, a name on a headstone.  
**Effect on the audience:** The reveal arrives through time rather than through a cut, so it plays as honest. The viewer cannot get ahead of the camera.  
**Used for and where it works best:** The end of an investigation beat in crime, the victim reveal in horror, the scale of an army in epic, and the name or date on an inscription in heritage documentary, where the last character should be the last thing to enter frame.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Documentary Feature, Trailer / Teaser, Anime (Japanese 2D), Short Film, AI-Generated Clip | genres: Crime / Procedural, Horror, Mystery / Whodunit, War, Mythology / Ancient Epic, Heritage (civilisation-focused), Thriller / Suspense, True Crime, Historical / Biopic  
**Avoid when:** Leaking half of it at the top usually spends the reveal, because once the viewer glimpses the edge of the thing there is nothing left to find; the exception is when you want dread instead of surprise and the partial glimpse is the threat. In a fast scene a slow tilt kills the rhythm.  
**Prompt:** `tilt down the covered stretcher, moving past the folded sheet, revealing the bare foot and the tag, stopping on the name`  
**Yields to:** `move.whip_tilt` — A fast scene, where a slow tilt kills rhythm.  
`move.reveal_tilt`

### Whip Tilt

**Also called:** swish tilt, snap tilt  
**What it is:** A very fast tilt where the middle smears into vertical blur and the end stops hard. The same logic as a whip pan, turned ninety degrees.  
**Effect on the audience:** A sudden reaction upward or downward. The body lifts its head before the mind has understood.  
**Used for and where it works best:** Something flying or falling from above: a hawk, an arrow, a stone, a blast over a roof, or the instant a person drops from a height. In action and anime it is the camera's own flinch, and in vertical short-form it works as a first second hook.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Feature Film, Trailer / Teaser, Game Cinematic / Gameplay, Music Video, Commercial / TVC, Drama Series Episode | genres: Action, Horror, Shonen Battle (anime), Thriller / Suspense, Adventure, Monster / Kaiju, Fantasy / Epic, War  
**Avoid when:** With nothing visibly rising or falling to motivate it, the move is meaningless. Keep it out of long quiet scenes; it snaps them in half.  
**Prompt:** `whip tilt up from the courtyard floor, vertical motion blur, snapping to a stop on the hawk circling above the tower`  
**Yields to:** `move.tilt_up` — A long quiet scene, which the snap breaks.  
`move.whip_tilt`

### Compound Pan-Tilt

**Also called:** diagonal pan, pan with tilt  
**What it is:** A pan and a tilt running together from one position, so the frame travels on a diagonal: from high right down to low left, for example.  
**Effect on the audience:** It follows the real line of the action instead of splitting it into two separate moves, so it feels like a human eye rather than a machine.  
**Used for and where it works best:** Following anything that rises or falls on an arc: a bird landing, a person coming down stairs, an arrow up and over, a ball in sport. In heritage work it follows a carved register that runs diagonally across a wall.  
**Best in:** formats: Sports Broadcast / Sports Film, Feature Film, Documentary Feature, Heritage / Historical Documentary, Anime (Japanese 2D), Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation | genres: Action, Adventure, Nature / Wildlife, War, Heritage (civilisation-focused), Sports Drama, Fantasy / Epic, Shonen Battle (anime)  
**Avoid when:** If the subject travels in a straight line, a compound move reads as wobble and exposes the head. Any speed mismatch between the two axes produces an ugly weave.  
**Prompt:** `compound pan and tilt following the falcon down from the tower to the courtyard floor, one smooth diagonal, settling as it lands`  
**Yields to:** `move.pan` — Subject travels a straight line; compound reads as wobble.  
`move.pan_tilt_compound`

### Partial Roll / Rolling Cant

**Also called:** camera roll, canting roll  
**What it is:** The camera rotates around the lens axis through a limited angle, so the horizon tips during the shot while position and framing direction stay the same.  
**Effect on the audience:** A gradual loss of balance. The viewer senses something is going wrong before they can name it.  
**Used for and where it works best:** The onset of dizziness, poisoning or blackout, entering a cursed place in horror, and the bank of a plane or a ship in action. Best when you want tension to rise inside one continuous shot without a cut or a music cue.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), Game Cinematic / Gameplay, Trailer / Teaser, Music Video, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Horror, Thriller / Suspense, Psychological Horror, Action, Supernatural Horror, Surreal / Absurdist, Fantasy / Epic, War  
**Avoid when:** Push the angle too fast and it becomes a visible gimmick. A good roll is one the viewer only notices after it has finished.  
**Prompt:** `starts level on the corridor, slowly rolling clockwise to about twelve degrees over the shot, settling canted`  
`move.roll_partial`

### Full 360 Roll / Barrel Roll

**Also called:** barrel roll, full camera roll  
**What it is:** The camera turns a full circle around the lens axis, so the image rotates all the way over and comes back upright.  
**Effect on the audience:** The world turns over. Far stronger than a cant: gravity itself is now in question.  
**Used for and where it works best:** The blast that flips the car, aerial combat, the crossing into a dream or a spell, a character falling in fantasy. In music video and vertical short-form it lands as a hit on the beat.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Trailer / Teaser, Game Cinematic / Gameplay, Anime (Japanese 2D), 3D CG Animation, Commercial / TVC, AI-Generated Clip | genres: Action, Fantasy / Epic, Sci-Fi, Surreal / Absurdist, Superhero, Mecha (anime), Adventure, Horror  
**Avoid when:** In grounded drama it plays as showing off. Do not run it too slow either; a lazy full roll tires the eye and loses the punch.  
**Prompt:** `full 360 degree barrel roll around the lens axis as the blast hits, world rotating completely, returning level on the wrecked car`  
**Yields to:** `move.roll_partial` — Grounded drama, where a full roll shows off.  
`move.roll_360`

### Dutch Roll Into a Tilt

**Also called:** roll-to-tilt, cant and look up  
**What it is:** The camera cants around the lens axis and then hands the movement over to a tilt up or down, so the roll becomes the run-up to a reveal.  
**Effect on the audience:** It fuses disorientation with revelation: first the world tips, then you see why.  
**Used for and where it works best:** Horror, when something hanging or standing above is uncovered; fantasy, when a creature larger than the frame arrives; anime, when the opponent appears on the rooftop. Best when you want the reveal to land while the viewer is already off balance.  
**Best in:** formats: Feature Film, Anime (Japanese 2D), Trailer / Teaser, Game Cinematic / Gameplay, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, AI-Generated Clip | genres: Horror, Supernatural Horror, Fantasy / Epic, Monster / Kaiju, Thriller / Suspense, Shonen Battle (anime), Mecha (anime), Psychological Horror  
**Avoid when:** Running both at full strength at once produces unreadable mush. Let the roll finish first and then begin the tilt, or overlap them only slightly.  
**Prompt:** `camera cants right to twenty degrees, then tilts up along the canted axis, revealing the figure standing on the beam above`  
`move.dutch_roll_tilt`

### Locked-Off Shot

**Also called:** lock off, static frame, no move  
**What it is:** The camera is completely still on a locked head: no travel, no tilt, no breath. All movement comes from inside the frame.  
**Effect on the audience:** It turns the frame into a stage and the viewer into a witness. Absolute stillness reads as formal, cold or observational, and sometimes as frightening, because nobody appears to be holding the camera.  
**Used for and where it works best:** Deadpan comedy built on people entering and leaving frame, the serious interview, the contemplative beat, the surveillance shot in horror. It is also the rest shot between two moving shots, the one that gives the audience back their ability to feel movement at all.  
**Best in:** formats: all | genres: all  
**Avoid when:** With no movement inside the frame and no change in the performance, the shot dies. Stillness has to be a decision, not laziness.  
**Prompt:** `locked-off static shot on a tripod, absolutely no camera movement, the action entering and leaving the frame`  
**Yields to:** `move.nudge` — AI clips and long takes, where perfect stillness reads synthetic.  
`move.lock_off`

### The Nudge / Micro Reframe

**Also called:** reframe, frame correction, operator nudge  
**What it is:** A tiny correction inside the shot: a pan or tilt of a degree or two to put the composition back where it belongs after the actor has shifted.  
**Effect on the audience:** It keeps the frame alive and human. The viewer does not register the move, but senses that somebody behind the camera is paying attention.  
**Used for and where it works best:** Any long shot on an actor who talks and shifts: an interview, a monologue, a seated scene. It is also the single detail that keeps an AI-generated shot from feeling dead, because mathematically perfect stillness reads as synthetic.  
**Best in:** formats: Interview / Video Podcast, Documentary Feature, Drama Series Episode, Feature Film, Vlog / YouTube Long-Form, AI-Generated Clip, Corporate / Training, News Report / Reportage | genres: Drama, Verite / Observational, True Crime, Slice of Life, Comedy, Legal Drama, Medical Drama, Psychological / Arthouse  
**Avoid when:** Repeat the nudges every couple of seconds and the frame turns nervous and tiring. In a rigorously designed composition, perfect symmetry for instance, any nudge wrecks the geometry.  
**Prompt:** `near-static frame with a one degree reframe as he leans forward, correcting the headroom, then still again`  
**Yields to:** `move.lock_off` — A rigorously designed or symmetrical composition.  
`move.nudge`

### The Recoil / Camera Flinch

**Also called:** flinch, pull-back jolt  
**What it is:** A small fast move back or sideways, as if the camera itself were struck and flinched, then recovers or settles in a new position.  
**Effect on the audience:** It gives the camera a body and a reflex. The viewer flinches too, because the eye believes a reaction before it believes an image.  
**Used for and where it works best:** When something detonates, shatters or lunges at the lens in horror, as a reaction beat in comedy, and on the hit in action. In vertical short-form it lands right after the hook to deliver a physical jolt without a cut.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Anime (Japanese 2D), Trailer / Teaser, Game Cinematic / Gameplay, Meme / Comedy Edit, Drama Series Episode, Music Video | genres: Horror, Action, Comedy, Thriller / Suspense, Slasher, Monster / Kaiju, Shonen Battle (anime), Dark Comedy / Satire  
**Avoid when:** With no visible cause the flinch reads as a technical fault rather than a reaction. Do not repeat it; a camera that flinches constantly becomes a joke.  
**Prompt:** `static close on the door, sharp recoil backward as the hand slams against it, settling slightly wider than before`  
`move.recoil`

### Overshoot and Correct

**Also called:** overshoot, operator catch-up, search and find  
**What it is:** The camera moves, travels slightly past the subject, then comes back and settles on it, the way a human eye searches and finds.  
**Effect on the audience:** It suggests the camera does not know what is about to happen, which makes the scene feel observed rather than staged.  
**Used for and where it works best:** Documentary and reportage, grounded drama, and any scene you want to feel stolen or unsafe. In found-footage style work it is part of the language of authenticity itself.  
**Best in:** formats: Documentary Feature, Documentary Series, News Report / Reportage, Drama Series Episode, Feature Film, Vlog / YouTube Long-Form, Vertical Short-Form (Reels, Shorts, TikTok), Mockumentary | genres: Verite / Observational, True Crime, War, Thriller / Suspense, Horror, Found Footage, Drama, Crime / Procedural  
**Avoid when:** In a polished or precisely designed scene it looks like a mistake. Do not overdo the overshoot either; a large correction reads as performed clumsiness.  
**Prompt:** `handheld pan right overshooting past the doorway, swinging back to find him, settling roughly framed`  
**Yields to:** `move.pan_and_settle` — A polished, precisely designed scene.  
`move.overshoot_correct`

### Hold Then Move

**Also called:** static start, delayed move  
**What it is:** The shot starts completely still for a measured beat, one or two seconds or more, and only then begins to move, cued by a specific point in the performance or the sound.  
**Effect on the audience:** The instant the move begins becomes an event in itself. The viewer registers that something has changed even if they cannot say what.  
**Used for and where it works best:** When a character hears news or reads a letter: hold, then let a slow push start on the first word. In suspense: a long static frame on a door, with the move beginning the instant it opens. Best when sound gives the cue.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Trailer / Teaser, Anime (Japanese 2D), Documentary Feature, AI-Generated Clip | genres: Drama, Thriller / Suspense, Horror, Mystery / Whodunit, Psychological / Arthouse, Tragedy, Crime / Procedural, Historical / Biopic  
**Avoid when:** If the hold is long and the move unmotivated the shot turns heavy. There must be something worth looking at during the hold.  
**Prompt:** `static for two full seconds on his face, then a slow push begins on the first word of the line, continuing to a close-up`  
**Yields to:** `move.start_in_motion` — Vertical short-form, where a static head loses the viewer.  
`move.hold_then_move`

### Move Then Hold

**Also called:** move and lock off, arrive and hold  
**What it is:** The move happens in the first part of the shot, then the camera stops dead and holds the final framing until the cut.  
**Effect on the audience:** Arrival and decision. The stillness after the move carries weight and gives the viewer time to read the final frame.  
**Used for and where it works best:** Any shot that ends on information the audience must read: a face after the news, the product in an ad, an inscription in documentary. It is also the only clean way to cut out of a moving shot.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Trailer / Teaser, Explainer, AI-Generated Clip | genres: Drama, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), Science / Educational, Crime / Procedural, Romance, Action  
**Avoid when:** If the end frame is not designed, the stillness exposes it. Do not clip the hold short either; under half a second nobody feels it as a stop.  
**Prompt:** `push in from a medium to a tight close-up, then lock off completely, holding the final framing for the last two seconds`  
**Yields to:** `move.move_across_cut` — Building one continuous take from short AI clips.  
`move.move_then_hold`

### The Settle

**Also called:** ease to rest, decelerating stop  
**What it is:** The end of a move: the camera decelerates gradually and comes to rest with no bump and no rebound, the way a hand settles on a table.  
**Effect on the audience:** Rest and confidence. The shot feels finished and the viewer settles onto the frame instead of bracing for more movement.  
**Used for and where it works best:** The end of any pan, dolly or crane before the cut, the end of an ad move before the logo lands, the end of an establishing shot before dialogue starts. Without it every shot you cut will feel severed mid-gesture — unless the move is carried across the cut on purpose (`move.move_across_cut`), where shot one ends still travelling and the settle belongs to the end of the combined move.  
**Best in:** formats: all | genres: all  
**Avoid when:** A dead stop lands as a hit, which is only right when you want violence. An over-long rest before the cut leaves the shot feeling abandoned.  
**Prompt:** `the move decelerates smoothly over the last second and settles to a complete rest on the final framing, no rebound`  
**Yields to:** `move.snap_timing` — When the hit is the point, not arrival; and `move.move_across_cut` — when the move is carried across the cut and settles only at the end of the combined move.  
`move.settle`

### Stutter Move / Stepped Motion

**Also called:** stepped move, ratcheting camera, mechanical stutter  
**What it is:** The move is executed in small discrete steps instead of smoothly: travel, stop, travel, like a machine or a digital fault.  
**Effect on the audience:** Malfunction. The viewer senses that whatever is recording is not human and not working properly, which is usefully unsettling.  
**Used for and where it works best:** Digital horror and surveillance footage, the ghost apparition beat in anime and games, and electronic music video as a hit on the beat. In tech advertising it mimics a device glitching before the fix arrives.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Anime (Japanese 2D), Trailer / Teaser, Feature Film, Commercial / TVC, Experimental / Art Film, AI-Generated Clip | genres: Horror, Supernatural Horror, Cyberpunk, Sci-Fi, Psychological Horror, Surreal / Absurdist, Dystopia / Post-Apocalyptic, Thriller / Suspense  
**Avoid when:** In any realistic scene it reads as a recording fault, not a style. Keep it short; past about three seconds it is simply irritating.  
**Prompt:** `stepped stuttering push-in, moving in small mechanical increments with hard pauses between them, ending locked on the empty chair`  
**Yields to:** `move.ease_in_out` — A realistic scene, where stepped motion reads as fault.  
`move.stutter`

### Dolly In / Push In

**Also called:** push-in, track in, trucking in  
**What it is:** The whole camera travels through space toward the subject. The background shifts with it because the camera really moves; it is not a lens zoom.  
**Effect on the audience:** It pulls the viewer inside the character's head. A slow push reads as realisation or decision; a fast push reads as shock or danger.  
**Used for and where it works best:** The moment of realisation or decision in drama, the beat where the character understands something. In horror, the slow approach to a closed door or a motionless face. In documentary, on an archive photo or a carved relief under the key line of narration. Best in features, series and heritage documentary.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Documentary Feature, Heritage / Historical Documentary, Trailer / Teaser, Anime (Japanese 2D), 3D CG Animation | genres: Drama, Thriller / Suspense, Horror, Mystery / Whodunit, Historical / Biopic, Heritage (civilisation-focused)  
**Avoid when:** When nothing changes inside the character. A push with no reason is noise, and used on every shot it loses its value.  
**Prompt:** `slow dolly in from a medium shot to a close-up on his face, steady, ending framed on the eyes`  
**Example:** The Godfather, Michael at the restaurant table before the shooting.  
**Yields to:** `move.zoom_in` — Surveillance or distant-watcher beat.  
`move.dolly_in`

### Creep In

**Also called:** imperceptible push, slow creep, three percent push  
**What it is:** A push so slow the viewer never consciously registers it: a small distance spread evenly over the entire shot with no perceptible acceleration.  
**Effect on the audience:** Tension that accumulates below awareness. The viewer feels the scene closing in and cannot say why, because the cause never reached their eye.  
**Used for and where it works best:** The long monologue, the interrogation, the confession in a documentary interview, any extended shot on a face you do not want to cut away from. It is also one of the best moves for AI-generated shots, because it keeps the frame alive without disturbing the stability of the face; where the shot should ask for no travel through space at all, camera locked, `move.micro_zoom` does the same job.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Interview / Video Podcast, Documentary Feature, AI-Generated Clip, Heritage / Historical Documentary, Short Film | genres: Drama, Thriller / Suspense, Psychological Horror, Mystery / Whodunit, True Crime, Tragedy, Crime / Procedural, Historical / Biopic  
**Avoid when:** In a short shot nobody will ever feel it; it needs length. Speed it up even slightly and it becomes an ordinary push, which loses the entire point.  
**Prompt:** `almost imperceptible dolly creep toward her face, about three percent over five seconds, no acceleration, ending marginally tighter`  
**Yields to:** `move.dolly_in` — A short shot, where a creep never registers.  
`move.creep_in`

### Crash In / Impact Push

**Also called:** crash push, snap push-in, slam in, whip push  
**What it is:** A very fast push that stops dead on one precise point: an eye, a hand, a weapon, a face. The whole move lasts under half a second and the stop is hard, with no deceleration and no drift.  
**Effect on the audience:** A visual blow. The body braces, because the move outruns the eye's ability to read it.  
**Used for and where it works best:** The shock beat in horror, the first strike in action, the reveal in a trailer. In vertical short-form it is the first second hook: start wide and crash onto the detail that explains the whole video. In trailers it works between two shots because it supplies rhythm without sound, and in anime it stands in for speed lines.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Feature Film, Anime (Japanese 2D), Game Cinematic / Gameplay, Music Video, Commercial / TVC, Meme / Comedy Edit, AI-Generated Clip | genres: Horror, Action, Thriller / Suspense, Slasher, Shonen Battle (anime), Dark Comedy / Satire, Monster / Kaiju, Superhero  
**Avoid when:** More than twice in one piece and it turns into an irritating tic, and in a quiet or grieving scene it flattens the emotion completely. Without a sound accent to land on, the move also feels unfinished.  
**Prompt:** `rapid crash push-in from a wide shot, accelerating hard, stopping abruptly on his eye filling the frame`  
**Yields to:** `move.creep_in` — A quiet or grieving scene the crash flattens.  
`move.crash_in`

### Dolly Out / Pull Back

**Also called:** pull out, track back, dolly back  
**What it is:** The whole camera retreats backward away from the subject and the space opens up around it.  
**Effect on the audience:** Detachment and solitude. The viewer withdraws from the character, who shrinks and grows more isolated with every metre.  
**Used for and where it works best:** The end of a scene once the other party has gone, the moment of abandonment, the last shot of a film or an episode. In documentary you pull back from a speaker to reveal the place they work in; in drama you pull off a face until it is a small point in an empty room.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Documentary Feature, Heritage / Historical Documentary, Music Video, Trailer / Teaser, Anime (Japanese 2D), AI-Generated Clip | genres: Drama, Tragedy, Melodrama, Noir / Neo-Noir, War, Historical / Biopic, Heritage (civilisation-focused), Psychological / Arthouse, Romance  
**Avoid when:** If the retreat reveals nothing new the move is hollow. Pulling back into a busy or cluttered space scatters attention instead of isolating.  
**Prompt:** `slow dolly pull-back from her face to a wide shot, the empty room opening around her, settling as she becomes small in the frame`  
`move.dolly_out`

### Pull-Back Reveal / Contextual Reveal

**Also called:** contextual reveal, reveal pull-back  
**What it is:** A long retreat that starts on a tight frame and ends on a wide one, revealing that the context is nothing like what the viewer assumed.  
**Effect on the audience:** A reversal of meaning. What you saw in the first second means something else entirely by the last, and not one element of the image had to change.  
**Used for and where it works best:** The twist reveal, the closing shot of a documentary where a hand in the dirt turns out to sit in the middle of a whole graveyard, the advertising beat where the product turns out to be inside a factory or a city. In epic it is the opening shot: begin on one soldier's face and end on two armies.  
**Best in:** formats: Trailer / Teaser, Feature Film, Documentary Feature, Heritage / Historical Documentary, Commercial / TVC, Short Film, Music Video, Title Sequence / Opening Credits, AI-Generated Clip | genres: War, Mythology / Ancient Epic, Heritage (civilisation-focused), Drama, Thriller / Suspense, Mystery / Whodunit, Historical / Biopic, Dystopia / Post-Apocalyptic, Tragedy  
**Avoid when:** If the context is predictable the retreat is a long wait for nothing. Hide every clue in the tight frame; one leaked edge of the truth kills the reveal.  
**Prompt:** `begins tight on the hand in the dust, pulling back continuously and steadily to an extreme wide, revealing the whole battlefield of bodies, settling`  
**Yields to:** `move.dolly_out` — The context is predictable; no reversal to stage.  
`move.pullback_reveal`

### Truck / Track / Crab

**Also called:** crab left, crab right, lateral dolly, slide  
**What it is:** The camera travels left or right in a straight line parallel to the scene, without turning. Foreground passes faster than background.  
**Effect on the audience:** Accompaniment with depth. Unlike a pan, the world separates into layers and you feel yourself walking beside it rather than turning to look at it.  
**Used for and where it works best:** Walk and talk, a queue, a line of soldiers, a row of products in advertising, and a carved wall in heritage documentary, where a track gives the relief its depth and a pan flattens it. Best when you want to compare a series of things that sit on one plane.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Product Video / Motion Design, Heritage / Historical Documentary, Documentary Feature, Music Video, Anime (Japanese 2D), Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, War, Historical / Biopic, Heritage (civilisation-focused), Crime / Procedural, Comedy, Romance, Political Thriller  
**Avoid when:** With nothing in the foreground a track feels like a pan and loses its one advantage. In a cramped space it never covers enough distance for the effect to build. And where legible carved lettering is in frame the camera is locked (`ai.text_carved_geometry`): take the lateral coverage as separate locked setups, and use the track only on relief that carries figures and ornament but no inscription.  
**Prompt:** `lateral tracking shot moving left along the relief wall, foreground columns sliding past faster than the background, settling on the king's figure`  
**Yields to:** `ai.text_carved_geometry` — where legible carved lettering or inscription is in frame, in which case the camera is locked and the lateral coverage is taken as separate setups.  
`move.truck`

### Lead Tracking / Leading Shot

**Also called:** leading the subject, backward tracking, camera ahead  
**What it is:** The camera travels backward in front of the subject at their exact pace, so their face stays in frame while they advance.  
**Effect on the audience:** We see his face, so we know what he feels. The viewer travels in the same direction he does, which makes this the most sympathetic of all moving shots.  
**Used for and where it works best:** Walk and talk in political and medical series, a determined entrance before a confrontation, a character walking while thinking in drama. Best when the dialogue or the expression is the event and the corridor is only a backdrop.  
**Best in:** formats: Drama Series Episode, Feature Film, Documentary Feature, Interview / Video Podcast, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, Anime (Japanese 2D) | genres: Drama, Political Thriller, Medical Drama, Legal Drama, Crime / Procedural, Romance, Comedy, Sports Drama  
**Avoid when:** If the destination matters more than the feeling, the face steals the attention and a trailing shot serves better. Over a very long walk it turns monotonous unless the surroundings change.  
**Prompt:** `leading tracking shot, camera moving backward ahead of him at his walking pace, his face filling the frame, settling as he stops at the doors`  
**Example:** The West Wing, the corridor walk and talks with the camera leading the actors backwards.  
**Yields to:** `move.trail_track` — The destination matters more than the feeling.  
`move.lead_track`

### Trail Tracking / Following Shot

**Also called:** following shot, behind-the-back tracking, over-the-shoulder follow  
**What it is:** The camera travels behind the subject at their pace, so we see their back and what lies ahead of them at the same time.  
**Effect on the audience:** Subordination and the unknown. We follow him and know no more than he does, so everything that opens ahead of him opens ahead of us at the same instant.  
**Used for and where it works best:** Entering an unknown place in horror, the walk down a corridor before the event, exploration in documentary and games. Best when you want the viewer to feel they are walking behind someone they can neither stop nor warn.  
**Best in:** formats: Feature Film, Drama Series Episode, Game Cinematic / Gameplay, Documentary Feature, Short Film, 360 / VR, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Horror, Thriller / Suspense, Mystery / Whodunit, War, Survival, Crime / Procedural, Drama, Coming of Age  
**Avoid when:** If nothing opens up ahead of him it becomes a long shot of a back with no information. In an emotional beat, hiding the face cuts off the sympathy.  
**Prompt:** `trailing shot from directly behind him, camera following at his pace into the dark corridor, ending as he stops at the doorway`  
**Example:** Elephant (2003), Gus Van Sant, the long shots following students from behind through the school corridors.  
**Yields to:** `move.lead_track` — An emotional beat, where hiding the face kills sympathy.  
`move.trail_track`

### Side Tracking a Walk

**Also called:** profile tracking, walking two-shot, parallel track  
**What it is:** The camera moves alongside the characters at their pace and at a fixed distance, framing them in profile. Both stay in frame while the background streams behind them.  
**Effect on the audience:** It turns a walk into a scene. The viewer walks with them like a third person in the same line.  
**Used for and where it works best:** Two people talking as they walk a street, a market or a corridor, the silent walk after bad news, an army or a caravan on the march in period work. Best when you want the relationship between the two to stay fixed while the world behind them changes.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Music Video, Commercial / TVC, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), Travel / Real Estate / Hospitality | genres: Drama, Romance, Historical / Biopic, War, Heritage (civilisation-focused), Comedy, Crime / Procedural, Coming of Age, Road Movie  
**Avoid when:** With an empty or repetitive background nobody feels the movement at all. Any mismatch between camera speed and walking pace produces an ugly drift in the framing.  
**Prompt:** `parallel side tracking with the two of them walking, profile framing at a fixed distance, market stalls streaming behind, easing to a stop as they halt`  
**Yields to:** `move.lead_track` — Empty or repetitive background; profile walk reads motionless.  
`move.side_track_walk`

### Counter-Tracking

**Also called:** contra-track, opposing track, counter-move  
**What it is:** The camera travels in the opposite direction to the subject, so the relative speed doubles and the relationship between them flips fast.  
**Effect on the audience:** Tension and confrontation. World and character move against each other, so the viewer senses a collision coming.  
**Used for and where it works best:** Two people closing on each other before a confrontation, the villain crossing a crowd, a character walking against the flow of a street. Its strongest use is a counter-track around an interrogation table, where the whole room seems to turn against the suspect.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Anime (Japanese 2D), Game Cinematic / Gameplay, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Thriller / Suspense, Crime / Procedural, Action, Noir / Neo-Noir, Political Thriller, Horror, Martial Arts / Wuxia, Shonen Battle (anime)  
**Avoid when:** If the relative speed is too high the face stops reading. In a calm scene the move brings an aggression nothing has asked for.  
**Prompt:** `camera tracks left while he walks right, counter motion doubling the relative speed, the background sweeping, settling as they meet in the centre`  
`move.counter_track`

### Diagonal Dolly / Compound Dolly

**Also called:** compound move, oblique dolly, forty-five degree dolly  
**What it is:** The camera pushes forward and moves sideways at the same time, so the path is a diagonal rather than a single straight line.  
**Effect on the audience:** Richer than either component alone: you gain approach and a change of angle at once, and the world separates into layers as it closes in.  
**Used for and where it works best:** Moving in on a group when you need to go from a group frame to one face without cutting, or entering a room from the door toward a table. Best in drama and crime when the relationship between two people has to change inside a single shot.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Commercial / TVC, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, AI-Generated Clip | genres: Drama, Crime / Procedural, Thriller / Suspense, Noir / Neo-Noir, Mystery / Whodunit, Political Thriller, Historical / Biopic, Gangster  
**Avoid when:** Mismatched speeds on the two axes produce a broken, kinked path. Do not reach for it when you do not need the angle change; a straight push is cleaner.  
**Prompt:** `diagonal dolly moving forward and to the right at the same time, sliding off the group and closing on her face, settling in a clean single`  
**Yields to:** `move.dolly_in` — You need approach but no angle change.  
`move.diagonal_dolly`

### Reverse Dolly / Retreat

**Also called:** matched retreat, walking pull-back  
**What it is:** The subject advances and the camera retreats at exactly the same pace, so their size in frame never changes while the world slides away around them.  
**Effect on the audience:** Relentless purpose. The subject walks and never arrives, so walking becomes a state rather than a journey.  
**Used for and where it works best:** The hero walking in before a fight, the escape that never ends, the artist walking straight at the lens in music video and advertising. Best when the road is long and what you need is inevitability rather than distance.  
**Best in:** formats: Music Video, Commercial / TVC, Trailer / Teaser, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Game Cinematic / Gameplay, Fashion Film | genres: Action, Thriller / Suspense, Crime / Procedural, Gangster, Musical, Superhero, War, Martial Arts / Wuxia  
**Avoid when:** If the gap between them varies, the feeling turns into either a chase or hesitation. In grounded, quiet scenes it reads as swagger.  
**Prompt:** `reverse dolly, camera retreating at exactly his advancing pace, framing held constant, the corridor sliding away behind him, ending as he stops`  
**Yields to:** `move.lead_track` — Grounded quiet scene, where the retreat reads as swagger.  
`move.reverse_dolly`

### Dolly Past / Pass-By Move

**Also called:** pass-by, camera passes the subject, drive-by  
**What it is:** The camera travels past the subject instead of stopping at it, so the subject enters frame on one side and exits on the other.  
**Effect on the audience:** It makes the subject part of a larger world rather than the point of the shot. The viewer senses the camera is going somewhere else and this is merely what it saw on the way.  
**Used for and where it works best:** Moving through a crowd, a market or a battlefield: a face, another face, a detail, each leaving as the next arrives. In heritage documentary it presents a row of statues or successive reliefs. It is also a transition device: pass a close foreground object that fills frame and hide the cut behind it.  
**Best in:** formats: Feature Film, Documentary Feature, Heritage / Historical Documentary, Game Cinematic / Gameplay, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Anime (Japanese 2D), AI-Generated Clip | genres: War, Heritage (civilisation-focused), Historical / Biopic, Drama, Crime / Procedural, Dystopia / Post-Apocalyptic, Action, Mythology / Ancient Epic  
**Avoid when:** If the subject is the point of the scene, passing it reads as neglect. Too high a speed and none of the detail gets read.  
**Prompt:** `dolly moving right past the kneeling figure, he enters frame left and exits frame right as the camera continues, settling on the open gate ahead`  
**Yields to:** `move.dolly_in` — The subject is the point; passing reads as neglect.  
`move.dolly_past`

### Dolly Through / Move Through

**Also called:** through the doorway, through the crowd  
**What it is:** The camera travels through something physical: a doorway, an arch, a curtain, a gap between people, a row of columns. The obstacle passes the lens and leaves frame.  
**Effect on the audience:** It creates the sensation of entering. The viewer crosses from one space into another and the body believes it, because something physically passed them on the way.  
**Used for and where it works best:** Entering a room, a temple or a courtyard, and threading between people in a crowd to reach one person. In heritage work, moving from a dark doorway into a sunlit court states the difference between two worlds in one shot. In vertical short-form it is the cleanest location change you can make.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, 360 / VR, Music Video, Commercial / TVC, Anime (Japanese 2D), AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Drama, Horror, Mythology / Ancient Epic, Adventure, Thriller / Suspense  
**Avoid when:** A narrow opening taken at speed produces nausea rather than immersion. In a scene that needs no change of space it is a move with nothing to do.  
**Prompt:** `dolly forward through the open doorway, the dark frame passing the lens on both sides, emerging into the sunlit courtyard, settling on the well`  
`move.dolly_through`

### Push-Through / Impossible Move

**Also called:** through-the-wall move, penetrating move  
**What it is:** The camera pushes through something that should stop it: a wall, a chest, a screen, a map, a machine. The move continues and the matter opens or vanishes.  
**Effect on the audience:** A non-human power. The viewer understands at once that this is not a human eye, which licenses either explanation or magic.  
**Used for and where it works best:** Explainer and science documentary, pushing through a building wall to show the interior, into a body or into a machine; product advertising, moving inside the device; fantasy, entering a memory. In heritage work it cuts a section through a ziggurat from outside to inside in one move.  
**Best in:** formats: Explainer, Product Video / Motion Design, Commercial / TVC, Documentary Feature, Heritage / Historical Documentary, 3D CG Animation, Game Cinematic / Gameplay, Trailer / Teaser, Corporate / Training, AI-Generated Clip | genres: Science / Educational, Heritage (civilisation-focused), Sci-Fi, Fantasy / Epic, Superhero, Historical / Biopic, Mythology / Ancient Epic, Dystopia / Post-Apocalyptic  
**Avoid when:** In grounded drama it breaks the logic of the entire world. Do not stack more than one or two penetrations either; a chain of them loses the viewer.  
**Prompt:** `camera pushes forward and passes straight through the mud brick wall without stopping, continuing into the chamber, settling on the sealed jar`  
**Yields to:** `move.dolly_through` — Grounded drama, where passing matter breaks world logic.  
`move.push_through`

### Through-Object / Portal Move

**Also called:** portal move, through the window, match-through  
**What it is:** The camera passes through an existing opening or material, a window, fire, water, smoke, a press of bodies, and comes out in a different world or time.  
**Effect on the audience:** A transition with no cut. The viewer accepts the change because they watched the road between the two worlds with their own eyes.  
**Used for and where it works best:** Moving from present to past in heritage documentary, through fire or dust and out in the same place two thousand years earlier; entering a dream in fantasy; changing product or season in an ad. In vertical short-form it is the best known transition that needs no complex editing.  
**Best in:** formats: Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Trailer / Teaser, 3D CG Animation, Feature Film, AI-Generated Clip, Title Sequence / Opening Credits | genres: Heritage (civilisation-focused), Fantasy / Epic, Historical / Biopic, Mythology / Ancient Epic, Surreal / Absurdist, Sci-Fi, Adventure, Faith / Biblical Epic  
**Avoid when:** If the two worlds have no relationship the move is a trick with nothing to say. The material must genuinely fill the frame at the moment of passage, otherwise the cut shows.  
**Prompt:** `camera flies through the curtain of falling dust, frame fully obscured for a beat, emerging in the same courtyard restored and full of people`  
`move.through_object`

### Parallax Slide

**Also called:** slider move with foreground, foreground slide  
**What it is:** A short lateral track with something very close in the foreground, a column, a branch, an edge, a bottle, sliding past faster than the background.  
**Effect on the audience:** Real depth in a single shot. The speed difference between the layers tells the brain this is a three-dimensional space and not a picture.  
**Used for and where it works best:** Opening a product shot in advertising, opening a scene in documentary, and any AI-generated shot you need to feel physically real. A short slow move is enough, because what you want is the sensation, not the distance.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Heritage / Historical Documentary, Music Video, Corporate / Training, Travel / Real Estate / Hospitality | genres: Drama, Heritage (civilisation-focused), Nature / Wildlife, Science / Educational, Romance, Thriller / Suspense, Historical / Biopic, Slice of Life  
**Avoid when:** If the foreground element covers the subject for the whole shot it becomes an obstruction, not depth. Do not let it cross dead centre on the key line either.  
**Prompt:** `slow lateral slide left with a stone pillar passing close through the foreground, strong parallax against the distant wall, settling on the doorway`  
`move.parallax_slide`

### Overhead Tracking

**Also called:** top-down track, plan view move, god's eye track  
**What it is:** The camera sits directly above the subject looking straight down and travels in a straight line over it: over a table, a bed, a street.  
**Effect on the audience:** A view from above with no sympathy. People become shapes and patterns, and the event becomes a diagram.  
**Used for and where it works best:** Showing the steps of cooking, making or a craft, which is the backbone of food and vertical short-form content; laying out a crime scene; presenting a battle or a city as a plan in documentary. In drama it is the loneliness beat: one person lying alone as the camera slides over them.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Explainer, Documentary Feature, Feature Film, Drama Series Episode, Kids Content, Corporate / Training, AI-Generated Clip | genres: Crime / Procedural, Drama, Science / Educational, True Crime, Heritage (civilisation-focused), Comedy, Thriller / Suspense, Family, Slice of Life  
**Avoid when:** On a face in an emotional beat it pushes the viewer away instead of closer. On a subject with real depth the vertical view flattens it and every piece of height information is lost.  
**Prompt:** `overhead top-down shot sliding along the length of the workbench, tools passing beneath the lens, settling on the finished piece`  
**Yields to:** `move.dolly_in` — Emotional beat on a face needs closeness.  
`move.overhead_track`

### The Camera Walks With the Actor

**Also called:** travelling with the subject, constant-size follow  
**What it is:** A fundamental choice: the camera travels with the character for the whole distance and keeps their size in frame constant, instead of letting them cross the frame and leave. It is the opposite of holding the frame and letting the actor go.  
**Effect on the audience:** Companionship. The viewer belongs to the character and shares the road, and the place becomes secondary.  
**Used for and where it works best:** When the journey itself is the scene: the walk to a confrontation, the escape, the walk after a loss. Best in drama, war and road movies when you do not want the viewer to detach from the character for even a second.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Documentary Feature, Game Cinematic / Gameplay, Anime (Japanese 2D), Music Video, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Drama, War, Road Movie, Survival, Thriller / Suspense, Coming of Age, Crime / Procedural, Adventure  
**Avoid when:** If the place or the distance is the point, travelling with the subject erases both, because nothing in the framing changes. Over a long walk with an unchanging environment it turns monotonous.  
**Prompt:** `camera travels with him for the whole length of the bridge, holding him the same size in frame, ending as he reaches the far side and stops`  
**Yields to:** `move.stay_actor_leaves` — The place or the distance is the point.  
`move.walk_with_actor`

### The Camera Stays, the Actor Leaves

**Also called:** let them walk out of frame, hold on the empty frame  
**What it is:** The camera does not travel, or barely does, and lets the character walk away, shrink and exit frame, then holds on the place after they have gone.  
**Effect on the audience:** Departure. The emptiness left in frame says more than any shot of a face, because the viewer is left looking at a place with nobody in it.  
**Used for and where it works best:** The end of a scene after a goodbye, the death of a secondary character, the end of an episode, the last shot of a heritage documentary where the person leaves and the ruin remains. Best when you want loss to land without music or dialogue.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Documentary Feature, Heritage / Historical Documentary, Anime (Japanese 2D), Music Video, Limited Series | genres: Drama, Tragedy, Melodrama, War, Heritage (civilisation-focused), Romance, Historical / Biopic, Psychological / Arthouse, Slice of Life  
**Avoid when:** If the empty frame says nothing, the wait is dead weight. Cut too soon after the exit and you lose everything; the hold is the message.  
**Prompt:** `locked frame as he walks away down the road, growing smaller and exiting frame right, holding on the empty road for three more seconds`  
**Yields to:** `move.walk_with_actor` — The empty frame says nothing; the wait dies.  
`move.stay_actor_leaves`

### Chase Move

**Also called:** pursuit move, chasing camera, running follow  
**What it is:** The camera pursues a fast subject at speed with imperfect stability: it falls behind, catches up, loses the subject for a moment and finds it again, and stumbles at the corners.  
**Effect on the audience:** Urgency and risk. It is the imperfection of the pursuit that convinces the viewer the outcome is not yet decided.  
**Used for and where it works best:** A pursuit through alleys, markets and rooftops, an animal chase in wildlife documentary, a sprint in sport. Best when you want the fear of failure, because a perfect follow quietly says the camera is faster than both of them.  
**Best in:** formats: Feature Film, Drama Series Episode, Game Cinematic / Gameplay, Documentary Feature, Sports Broadcast / Sports Film, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Trailer / Teaser, AI-Generated Clip | genres: Action, Thriller / Suspense, Crime / Procedural, Survival, War, Nature / Wildlife, Adventure, Spy / Espionage, Shonen Battle (anime)  
**Avoid when:** A perfectly smooth follow removes all the danger. Shake it so hard that nothing reads and the viewer tires and leaves the scene.  
**Prompt:** `camera chases him at speed through the narrow alley, briefly losing him at the corner and catching up, ending as he bursts into the open square`  
`move.chase`

### Floating Follow

**Also called:** steadicam follow, gimbal follow, free follow  
**What it is:** A free follow off the rails, on a stabilised rig: it turns with the character, negotiates corners, closes and drops back, and stays smooth throughout.  
**Effect on the audience:** Presence. The viewer becomes a third person walking with them, neither a distant observer nor the character themselves.  
**Used for and where it works best:** Entering a building, a party or a hospital, moving through a complex space with several rooms, documentary work inside a market or a workshop. Best when the place is part of the story and has to be read while you pass through it.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Game Cinematic / Gameplay, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), 360 / VR, Wedding / Event Film, Anime (Japanese 2D) | genres: Drama, Crime / Procedural, Thriller / Suspense, Medical Drama, Verite / Observational, Comedy, War, Gangster, Horror  
**Avoid when:** In a small simple space nobody benefits from the freedom. Excessive smoothness in a chaotic scene contradicts the scene itself.  
**Prompt:** `smooth gimbal follow floating behind and slightly left of her, turning with her through two doorways, settling as she stops at the window`  
**Yields to:** `move.handheld_sway` — A chaotic scene that stabilised smoothness contradicts.  
`move.floating_follow`

### The Lean In

**Also called:** small push, camera leans, interest move  
**What it is:** A very small forward move with a limited travel, like a person leaning in to hear better, then stopping. Not a full push, just a lean.  
**Effect on the audience:** Interest. The camera has become a participant, as though it just noticed something.  
**Used for and where it works best:** When someone lowers their voice or says something dangerous in an interview or an interrogation, or when a child whispers in kids content. Best inside long static shots, because it delivers a change without breaking the stillness of the scene.  
**Best in:** formats: Interview / Video Podcast, Documentary Feature, Drama Series Episode, Feature Film, Kids Content, Corporate / Training, AI-Generated Clip, Vlog / YouTube Long-Form | genres: Drama, True Crime, Mystery / Whodunit, Comedy, Family, Thriller / Suspense, Verite / Observational, Preschool / Early Learning  
**Avoid when:** Push the distance too far and it becomes a full push with a heavier meaning than you wanted. Do not repeat it within a shot; a camera that leans and returns reads as indecisive.  
**Prompt:** `slight forward lean of about twenty centimetres as she lowers her voice, stopping immediately and holding the closer frame`  
`move.lean_in`

### The Step Back

**Also called:** small pull, camera retreats a step, recoil pull  
**What it is:** A small limited retreat on a specific beat, like a person taking one step back. It starts, finishes quickly and settles.  
**Effect on the audience:** Recoil, respect or fear. The camera has withdrawn because something became too much to stay close to.  
**Used for and where it works best:** When a character erupts in anger, or when something sacred or terrible is uncovered in horror and in heritage documentary. In dialogue it is at its best after a cruel line, where it makes the viewer feel they have moved away from the speaker.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Short Film, Anime (Japanese 2D), Interview / Video Podcast, AI-Generated Clip | genres: Drama, Horror, Thriller / Suspense, Heritage (civilisation-focused), Faith / Biblical Epic, Psychological Horror, Tragedy, Mythology / Ancient Epic  
**Avoid when:** With no clear cause it looks like an operating error rather than a decision. Do not pair it with a lean in inside one shot; together they cancel each other out.  
**Prompt:** `camera pulls back one short step as he raises his voice, quick and small, settling into the wider frame`  
`move.step_back`

### Pendulum Move

**Also called:** swinging camera, sway arc  
**What it is:** The camera swings back and forth on a repeating arc, like a pendulum, at the same speed and over the same distance each time.  
**Effect on the audience:** Passing time and rising unease. The repetition becomes a clock, and the viewer feels the waiting.  
**Used for and where it works best:** The long wait, outside an operating room, in a cell, at home before news arrives; the moment a character loses consciousness; surreal and experimental work. In music video it works on the beat if the period of the arc matches the pulse.  
**Best in:** formats: Music Video, Experimental / Art Film, Feature Film, Short Film, Anime (Japanese 2D), AI-Generated Clip, Drama Series Episode, Game Cinematic / Gameplay | genres: Psychological / Arthouse, Surreal / Absurdist, Horror, Drama, Tragedy, Supernatural Horror, Thriller / Suspense, Medical Drama  
**Avoid when:** Beyond two or three arcs it becomes tiring and slightly sickening. In a scene that must deliver clear information the repetition blurs the read.  
**Prompt:** `slow pendulum sway, camera arcing left and right over the bed twice, decelerating and settling level on the sleeping face`  
`move.pendulum`

### Pedestal Up

**Also called:** ped up, column up, vertical rise  
**What it is:** The camera rises vertically on the column of the head with no tilt at all: same angle, same direction, only the height changes.  
**Effect on the audience:** A change of viewpoint with no editorial. It is strangely neutral and strangely moving, because the world did not change, only your position in it.  
**Used for and where it works best:** Moving from a child's world to an adult's inside one shot, or rising from table level to the level of the faces in a family scene. In heritage documentary it climbs from floor level to the upper register of a carved wall at a constant angle, so the registers can be compared fairly.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Kids Content, 2D Animation (Western / Cartoon), Corporate / Training, Explainer, AI-Generated Clip | genres: Drama, Family, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Coming of Age, Slice of Life, Preschool / Early Learning  
**Avoid when:** A small rise registers with nobody and the move is wasted. If you need a tilt as you climb, you are no longer making a pedestal move; that is a crane.  
**Prompt:** `pedestal up from knee height to standing eye height, angle staying level throughout, settling at adult eye line`  
**Yields to:** `move.crane_up` — You need a tilt while climbing.  
`move.pedestal_up`

### Pedestal Down

**Also called:** ped down, column down, vertical descent  
**What it is:** The camera drops vertically with no tilt to a lower height: a child's eye line, an animal's, the floor's.  
**Effect on the audience:** It inverts the viewer's place in the world. Dropping to a low eye line makes you smaller, and everything upright now stands over you.  
**Used for and where it works best:** Dropping to a child's or an animal's eye line in kids and nature work, to a body or a wounded man in war and crime, to the offerings at the base of a statue in heritage work. Best when you want the shift in viewpoint to read as a shift in sympathy.  
**Best in:** formats: Kids Content, Documentary Feature, Feature Film, Drama Series Episode, Heritage / Historical Documentary, 2D Animation (Western / Cartoon), 3D CG Animation, AI-Generated Clip | genres: Family, Preschool / Early Learning, Nature / Wildlife, War, Crime / Procedural, Drama, Heritage (civilisation-focused), Tragedy  
**Avoid when:** Drop with no reason and the frame fills with legs and nothing else. A fast drop reads as a fall rather than a change of viewpoint.  
**Prompt:** `pedestal down from adult eye height to the child's eye line, angle level, settling as she looks up at the door handle`  
`move.pedestal_down`

### Boom Up / Boom Down

**Also called:** boom arm move, jib up, jib down  
**What it is:** The camera rises or falls on an arm, a jib or a crane head, so the path is a shallow arc: it gains height while creeping slightly forward or back. A bigger range than a pedestal, a smaller one than a full crane move.  
**Effect on the audience:** It gives height a liquid quality. The move breathes rather than riding an elevator.  
**Used for and where it works best:** Rising over a dinner table to reveal every plate, coming down from a window to a face, lifting above a crowd as the group grows. Best in advertising, wedding films and documentary when you want an expensive-looking move inside a small interior.  
**Best in:** formats: Commercial / TVC, Wedding / Event Film, Documentary Feature, Drama Series Episode, Feature Film, Product Video / Motion Design, Corporate / Training, Music Video, Travel / Real Estate / Hospitality | genres: Drama, Family, Romance, Heritage (civilisation-focused), Historical / Biopic, Comedy, Slice of Life, Melodrama  
**Avoid when:** In a cramped space or under a low ceiling the arc breaks halfway and the rig shows. Do not use a boom when you need a pure vertical; that is what a pedestal is for.  
**Prompt:** `boom up on a jib arm from the table top, arcing back and gaining height, revealing the whole laid table, settling above the centrepiece`  
**Yields to:** `move.pedestal_up` — You need a pure vertical, no arc.  
`move.boom`

### Crane Up

**Also called:** crane out, rising crane, lift and reveal  
**What it is:** The camera rises on a wide arc over a large distance, usually with an accompanying tilt down so the subject stays in frame as it shrinks.  
**Effect on the audience:** An announcement of scale or of an ending. Rising detaches the viewer from the character and places what just happened inside something larger than it.  
**Used for and where it works best:** The end of a scene or a film, the reveal of the true size of a city, an army or a crowd, the closing shot of a heritage documentary that starts on one person in the ruin and ends on the whole city. Best when the message is: what you have been watching was a small part of this.  
**Best in:** formats: Feature Film, Trailer / Teaser, Heritage / Historical Documentary, Documentary Feature, Music Video, Commercial / TVC, Title Sequence / Opening Credits, Drama Series Episode, 3D CG Animation | genres: War, Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, Drama, Fantasy / Epic, Tragedy, Faith / Biblical Epic, Adventure  
**Avoid when:** Used mid-scene it announces an ending that has not arrived. If what the height reveals is empty or unremarkable, all that rise buys you nothing.  
**Prompt:** `crane up and back from the two figures, rising steadily while tilting down to hold them, revealing the full ruined city around them, settling high and wide`  
**Example:** Gone with the Wind (1939), the crane rising over the wounded at the Atlanta depot.  
`move.crane_up`

### Crane Down

**Also called:** crane in, descending crane, lower and find  
**What it is:** The camera descends on a wide arc from height down to the level of a character or a detail, usually with an accompanying tilt up.  
**Effect on the audience:** An entrance into a world. The viewer drops from observer to participant, and reads the move as a choice: out of all this, let us look at this one.  
**Used for and where it works best:** Opening a scene or a film: start on the city or the roofline and come down to the person who will carry the story. In heritage documentary: from the top of the ziggurat down to the hand working in the dirt.  
**Best in:** formats: Feature Film, Title Sequence / Opening Credits, Heritage / Historical Documentary, Documentary Feature, Trailer / Teaser, Drama Series Episode, Commercial / TVC, Music Video, 3D CG Animation | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, War, Crime / Procedural, Fantasy / Epic, Political Thriller  
**Avoid when:** A long descent onto an unimportant subject promises something that never arrives. Taken fast it reads as a fall rather than an entrance.  
**Prompt:** `crane down from high above the rooftops, descending in a wide arc while tilting up, arriving at street level, settling on the boy at the stall`  
`move.crane_down`

### Jib Arc

**Also called:** jib sweep, arm arc  
**What it is:** The camera travels on an arc on the jib arm around a fixed point, gaining height and swinging round at the same time over a relatively short distance.  
**Effect on the audience:** It gives a move weight and gloss in a small space. The viewer senses a larger production than the one that exists.  
**Used for and where it works best:** Opening a party, a wedding or an event, arriving on the product in an ad, the opening of a show or an interview set. Best when the space is limited and you need a move that feels expensive within a few seconds.  
**Best in:** formats: Wedding / Event Film, Commercial / TVC, Concert / Live Event, Corporate / Training, Product Video / Motion Design, Music Video, Interview / Video Podcast, Drama Series Episode, Sports Broadcast / Sports Film | genres: Musical, Romance, Family, Comedy, Sports Drama, Drama, Melodrama  
**Avoid when:** Put every shot on a jib arc and the piece turns into an events video. In an intimate scene the gloss of the move pushes the viewer away.  
**Prompt:** `jib arc rising and sweeping right around the table, gaining a metre of height, settling framed on the cake and the couple behind it`  
`move.jib_arc`

### Arc / Partial Orbit

**Also called:** quarter orbit, half orbit, arcing shot  
**What it is:** The camera travels a partial circle around the subject, a quarter or a half, holding them centred while the background sweeps behind them.  
**Effect on the audience:** The subject becomes the centre of the world. The changing background says the world is moving around them while they hold their ground.  
**Used for and where it works best:** The decision beat, the entrance of an important character, a product or a car in advertising, a dress in a fashion film. In heritage work an arc around a statue or a cuneiform tablet lets the object read as a three-dimensional thing rather than a flat picture.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Fashion Film, Feature Film, Trailer / Teaser, Music Video, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Anime (Japanese 2D) | genres: Drama, Action, Historical / Biopic, Heritage (civilisation-focused), Superhero, Romance, Fantasy / Epic, Martial Arts / Wuxia, Shonen Battle (anime)  
**Avoid when:** Against an empty background the arc does not register at all. If every character gets one, none of them is special.  
**Prompt:** `slow ninety degree arc around him at a constant radius, subject held centred, background sweeping behind, easing to a stop in profile`  
**Yields to:** `move.parallax_orbit` — An empty background, where the turn never registers.  
`move.arc`

### 360 Orbit

**Also called:** full orbit, full circle, circling shot  
**What it is:** A complete circle around the subject at a constant radius, holding it dead centre from the first frame to the last.  
**Effect on the audience:** Either detachment from reality or absolute glorification, depending on speed. Slow it delivers awe; fast it delivers vertigo and collapse.  
**Used for and where it works best:** The kiss, the victory, the breakdown where the character stands still and the world turns around them, the product turn in advertising and vertical short-form. Best when the moment must step outside the time of the scene.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Feature Film, Trailer / Teaser, Game Cinematic / Gameplay, Anime (Japanese 2D), AI-Generated Clip, Fashion Film | genres: Romance, Action, Drama, Superhero, Musical, Psychological / Arthouse, Fantasy / Epic, Shonen Battle (anime)  
**Avoid when:** Used without reason it is now one of the most worn out moves in AI and short-form content. Keep it out of any shot that must deliver information; the rotation prevents reading.  
**Prompt:** `full 360 degree orbit around the two of them at a constant radius, subjects locked centre frame, background carousel behind, completing the circle and settling`  
**Example:** Vertigo (1958), the camera circling Scottie and Judy in the hotel room as the background changes.  
**Yields to:** `move.arc` — The shot must stay readable; rotation prevents reading.  
`move.orbit_360`

### Parallax Orbit

**Also called:** orbit with foreground, occluding orbit  
**What it is:** An ordinary orbit with something very close in the foreground, a column, a branch, a wall edge, a person, crossing frame during the turn and briefly hiding the subject.  
**Effect on the audience:** Genuine depth. The near layer travels far faster than the far one, so the brain accepts a real space rather than a rotating backdrop.  
**Used for and where it works best:** Almost everywhere, and it is the single best trick for making an AI-generated shot feel physically real. In heritage work, orbit a figure between temple columns and let the columns pass the lens. In advertising, orbit the product with a near element crossing frame.  
**Best in:** formats: AI-Generated Clip, Commercial / TVC, Product Video / Motion Design, Heritage / Historical Documentary, Feature Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, 3D CG Animation, Documentary Feature | genres: Heritage (civilisation-focused), Drama, Historical / Biopic, Action, Thriller / Suspense, Fantasy / Epic, Mythology / Ancient Epic, Romance  
**Avoid when:** If the foreground blocks the subject on the key line the shot is lost. If it sits too far back it produces no parallax at all; it has to be genuinely close to the lens.  
**Prompt:** `orbit right around him with a stone pillar passing close through the foreground mid-move, strong parallax separation, settling as the pillar clears frame`  
`move.parallax_orbit`

### Spiral Move

**Also called:** spiral in, spiral out, tightening orbit  
**What it is:** An orbit whose radius changes as it goes: the camera circles and closes in, or circles and widens out.  
**Effect on the audience:** Spiralling in traps; spiralling out releases. The move feels headed somewhere inevitable rather than merely turning.  
**Used for and where it works best:** Spiral in for a breakdown, a siege or the onset of madness; spiral out to end a scene after release or death. In horror and surreal work it is the loss of control expressed in one shot.  
**Best in:** formats: Feature Film, Music Video, Anime (Japanese 2D), Trailer / Teaser, Experimental / Art Film, Game Cinematic / Gameplay, 3D CG Animation, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Psychological Horror, Horror, Surreal / Absurdist, Drama, Fantasy / Epic, Tragedy, Thriller / Suspense, Psychological / Arthouse  
**Avoid when:** Too small a change in radius and it just looks like a wobbly orbit. Too large and it reads as a video game camera.  
**Prompt:** `spiral orbit tightening as it turns, circling her while closing from a wide to a medium, settling tight on her face after half a turn`  
`move.spiral`

### Corkscrew

**Also called:** helix move, rolling spiral, drone corkscrew  
**What it is:** The camera advances or climbs while rotating around its own axis of travel, so the image turns as it moves forward. Common in drone work and in virtual camera moves.  
**Effect on the audience:** Escape from gravity. Raw energy and the sense that up and down have stopped applying.  
**Used for and where it works best:** Openers and teasers, drone runs between buildings or columns, flight and falling beats in fantasy and games. In music video it belongs on the loudest section.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Game Cinematic / Gameplay, 3D CG Animation, Commercial / TVC, Travel / Real Estate / Hospitality, AI-Generated Clip, Experimental / Art Film | genres: Action, Fantasy / Epic, Sci-Fi, Adventure, Superhero, Cyberpunk, Musical, Space Opera  
**Avoid when:** Beyond a few seconds it is simply nauseating. In any dialogue or emotional scene it erases the meaning outright.  
**Prompt:** `corkscrew move flying forward between the columns while rolling clockwise, continuous rotation, straightening and settling level on the far gate`  
`move.corkscrew`

### Vertical Drop / Descend

**Also called:** top-down descent, drone drop, straight down move  
**What it is:** The camera descends vertically from height, looking down or forward, on a straight path with no rotation.  
**Effect on the audience:** A fated descent. You are landing on a place rather than approaching it, which gives the arrival weight and inevitability.  
**Used for and where it works best:** Opening a location from the sky down into a courtyard, a square or a rooftop, and moving from map to detail in documentary. In vertical short-form it is a strong hook, because the move itself matches the shape of the frame.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Heritage / Historical Documentary, Feature Film, Travel / Real Estate / Hospitality, Trailer / Teaser, Game Cinematic / Gameplay, 3D CG Animation, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Thriller / Suspense, Adventure, War, Dystopia / Post-Apocalyptic, Nature / Wildlife  
**Avoid when:** If the place you land on is unremarkable the descent is a broken promise. Dropping vertically onto a face in close-up distorts the features.  
**Prompt:** `vertical descent from high above the city, camera dropping straight down toward the courtyard, slowing as it arrives, settling just above the well`  
`move.vertical_drop`

### Rise Reveal

**Also called:** cresting rise, reveal over the ridge, boom-up reveal  
**What it is:** The camera rises from behind an obstruction, a ridge, a wall, a parapet, a rooftop edge, until the obstruction clears and what lies beyond is revealed.  
**Effect on the audience:** The moment the image opens. The obstruction builds the anticipation and the clearing delivers the payoff in one stroke.  
**Used for and where it works best:** Revealing a city, an army or a valley at the end of a journey, closing an exploration beat in adventure, and the strongest opening shot in heritage documentary: the ruins appearing from behind a dune. Best when the viewer should be struck at the same instant as the character.  
**Best in:** formats: Heritage / Historical Documentary, Feature Film, Trailer / Teaser, Documentary Feature, Travel / Real Estate / Hospitality, Game Cinematic / Gameplay, 3D CG Animation, Music Video, AI-Generated Clip | genres: Adventure, Fantasy / Epic, Heritage (civilisation-focused), Historical / Biopic, War, Mythology / Ancient Epic, Nature / Wildlife, Western  
**Avoid when:** A low obstruction or a partial reveal wastes the beat. What appears has to deserve the wait, otherwise the whole move is a build to nothing.  
**Prompt:** `camera rises from behind the ridge, the crest wiping down through frame, revealing the city on the plain below, settling wide`  
`move.rise_reveal`

### Fly-Over

**Also called:** flyover, overflight, aerial pass  
**What it is:** The camera passes over a place or a subject at a constant height and speed, usually looking down at an angle.  
**Effect on the audience:** An epic survey. The viewer understands the geography: what is next to what, how far apart, and how big.  
**Used for and where it works best:** Establishing a site in heritage documentary, passing over the ruins or the river, showing a route in travel and property films, crossing an army before a battle. Best when narration is explaining a place and needs an image to stand under it.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Travel / Real Estate / Hospitality, Documentary Series, Feature Film, Trailer / Teaser, Sports Broadcast / Sports Film, News Report / Reportage, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, War, Nature / Wildlife, Adventure, Science / Educational, Mythology / Ancient Epic, Political Thriller  
**Avoid when:** Over a place with no legible features from above it is an empty shot. A long flyover with no change in the landscape is where viewers skip.  
**Prompt:** `aerial fly-over at constant height passing across the ruined city, looking down at forty five degrees, continuing past the walls and settling over the river`  
`move.fly_over`

### Fly-Through

**Also called:** flythrough, FPV run, threading flight  
**What it is:** The camera flies and threads through tight openings: an arch, a window, a gap between columns or people, under a bridge, without cutting.  
**Effect on the audience:** Pure energy and impossibility. The viewer knows their own eye could never do this, which is exactly why they watch.  
**Used for and where it works best:** A one-shot tour of a place, a restaurant, a gym, a temple, an exhibition; the opening of a sports event; short-form and advertising. Best when you need to show an entire location in five seconds with no editing.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Travel / Real Estate / Hospitality, Sports Broadcast / Sports Film, Game Cinematic / Gameplay, Music Video, Product Video / Motion Design, Heritage / Historical Documentary, AI-Generated Clip, Corporate / Training | genres: Action, Adventure, Sports Drama, Heritage (civilisation-focused), Musical, Sci-Fi, Cyberpunk, Comedy  
**Avoid when:** Too many openings in a row and the piece becomes a technical competition with no story. It rarely suits a grieving or formal scene, because the flourish puts the camera above the feeling; the exception is when the ornate move exists to be broken by the stillness that follows.  
**Prompt:** `FPV flight at speed threading through the archway, dropping over the courtyard steps and out through the far gate, decelerating and settling on the plain`  
`move.fly_through`

### Fly-By

**Also called:** flyby, close pass, side pass  
**What it is:** The camera passes the subject at close range and speed: a building, a statue, an aircraft, a figure standing on an edge.  
**Effect on the audience:** Speed and scale. The proximity at the moment of passing makes the size read instantly, and the speed delivers a thrill.  
**Used for and where it works best:** Introducing a building or a landmark in travel and heritage work, flight and racing shots, and presenting a character standing on a height in a trailer. Best when you want scale and energy in the same shot.  
**Best in:** formats: Travel / Real Estate / Hospitality, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, Commercial / TVC, Game Cinematic / Gameplay, Heritage / Historical Documentary, Music Video, AI-Generated Clip | genres: Action, Adventure, Heritage (civilisation-focused), Sports Drama, Sci-Fi, War, Historical / Biopic, Superhero  
**Avoid when:** From far away the sense of speed disappears completely. In serious documentary a close fast pass reads as marketing.  
**Prompt:** `fast fly-by passing close along the face of the ziggurat, the terraces streaking past the lens, pulling away and settling wide on the whole structure`  
**Yields to:** `move.fly_over` — Serious documentary, where a close fast pass reads as marketing.  
`move.fly_by`

### Swoop

**Also called:** swooping move, dive and level, hawk move  
**What it is:** The camera drops on a fast arc from height to a low level, then levels out and continues forward, the way a bird stoops and pulls out.  
**Effect on the audience:** Rush and resolution. The falling arc supplies acceleration, the level-out supplies arrival.  
**Used for and where it works best:** Entering a battle or a crowd from above, opening a chase, the arrival of a flying creature in fantasy and anime. In sports advertising it is how you arrive on the athlete or the track.  
**Best in:** formats: Trailer / Teaser, Feature Film, Game Cinematic / Gameplay, Anime (Japanese 2D), 3D CG Animation, Commercial / TVC, Sports Broadcast / Sports Film, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, AI-Generated Clip | genres: Action, Fantasy / Epic, Adventure, War, Monster / Kaiju, Superhero, Sports Drama, Mythology / Ancient Epic  
**Avoid when:** If the move never levels out the viewer is left falling and lost. In grounded ground-level scenes it reads as a video game.  
**Prompt:** `camera swoops down from above the rooftops in a fast arc, levelling at head height, continuing forward through the crowd and settling on the rider`  
`move.swoop`

### Dive

**Also called:** nose-down dive, plunge, descent run  
**What it is:** The camera descends at a steep angle looking in the direction of travel, so the ground or the target grows fast in frame.  
**Effect on the audience:** Danger, speed and loss of control. The body braces, because the viewer feels an impact coming.  
**Used for and where it works best:** A fall from height, an air attack, a dive into water, a nightmare beat. In games and anime it is the leap from above before the strike.  
**Best in:** formats: Game Cinematic / Gameplay, Anime (Japanese 2D), Trailer / Teaser, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, Music Video, Sports Broadcast / Sports Film, AI-Generated Clip | genres: Action, Horror, Adventure, Fantasy / Epic, Survival, War, Shonen Battle (anime), Superhero, Disaster  
**Avoid when:** With no clear ending, an impact, an arrival or a level-out, the move is left hanging. Do not extend it either; a long dive becomes a journey instead of a threat.  
**Prompt:** `steep nose-down dive toward the courtyard, ground rushing up and filling frame, pulling out at the last moment and settling level above the paving`  
`move.dive`

### Climb

**Also called:** ascend, rise out, pull up  
**What it is:** The camera ascends over a large distance looking forward or down, so what filled the frame becomes a small point.  
**Effect on the audience:** A withdrawal from the event, leaving the character behind. It is the closest visual equivalent of an ending, a death or a deliverance.  
**Used for and where it works best:** The final shot of a film, an episode or a documentary, the last bar of a music video, the end of a travel spot. Best when you want the viewer to leave the place while they can still see it.  
**Best in:** formats: Feature Film, Documentary Feature, Heritage / Historical Documentary, Music Video, Travel / Real Estate / Hospitality, Trailer / Teaser, Drama Series Episode, Title Sequence / Opening Credits, AI-Generated Clip | genres: Drama, Tragedy, War, Heritage (civilisation-focused), Historical / Biopic, Survival, Nature / Wildlife, Road Movie, Faith / Biblical Epic  
**Avoid when:** In the middle of a scene it destroys involvement. If the area revealed by the height is empty, the climb reads as an escape from the shot.  
**Prompt:** `camera climbs steadily away from the two figures, rising high above the plain, they shrink to specks, settling on the wide empty landscape`  
`move.climb`

### Hover

**Also called:** hovering hold, aerial hold, static aerial  
**What it is:** The camera hangs in the air at a fixed height with almost no travel, carrying only the small natural instability of holding position.  
**Effect on the audience:** Silent observation. A non-human presence watching from above and not intervening.  
**Used for and where it works best:** The surveillance beat in thriller and crime, the archaeological site under narration, the pause between two aerial moves that lets the eye rest. Best when you want the viewer to read the geography calmly.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, News Report / Reportage, Feature Film, Drama Series Episode, Travel / Real Estate / Hospitality, Sports Broadcast / Sports Film, AI-Generated Clip, Game Cinematic / Gameplay | genres: Crime / Procedural, Thriller / Suspense, Heritage (civilisation-focused), Nature / Wildlife, War, Science / Educational, True Crime, Political Thriller  
**Avoid when:** Held too long with nothing happening inside the frame it is a dead shot. Perfect mathematical stillness looks synthetic; leave a little natural drift in it.  
**Prompt:** `aerial hover holding position above the excavation, barely any drift, faint natural instability, the crew working below, holding the frame`  
`move.hover`

### Float

**Also called:** floating camera, weightless move, untethered move  
**What it is:** A slow smooth move with no clear direction and no destination: the camera drifts through the space the way something floats in water.  
**Effect on the audience:** A departure from the real. Neither walking nor standing, so the viewer reads dream, memory or the state between sleeping and waking.  
**Used for and where it works best:** Dreams, memory and flashback in drama, afterlife and fantasy worlds, quiet passages in music video. In heritage documentary it carries the move from the present into an imagined past.  
**Best in:** formats: Music Video, Feature Film, Anime (Japanese 2D), Experimental / Art Film, Heritage / Historical Documentary, Short Film, 3D CG Animation, AI-Generated Clip, Title Sequence / Opening Credits | genres: Surreal / Absurdist, Psychological / Arthouse, Fantasy / Epic, Romance, Drama, Supernatural Horror, Mythology / Ancient Epic, Tragedy  
**Avoid when:** In a realistic scene it just looks like the camera has lost its purpose. Floated too long with nothing changing in frame it becomes soft boredom.  
**Prompt:** `weightless floating move drifting slowly forward and slightly left through the empty room, no fixed destination, easing to a stop near the window`  
**Yields to:** `move.drift` — A realistic scene, where weightlessness looks purposeless.  
`move.float`

### Drift

**Also called:** unmotivated drift, slow drift, creeping slide  
**What it is:** A very slow lateral or forward move with no visible motivation in the scene, continuing across the shot and arriving nowhere.  
**Effect on the audience:** Time passing. The frame feels alive and faintly restless, and the viewer senses that the shot is waiting for something.  
**Used for and where it works best:** The location beats between scenes, the montage shot under narration or score, contemplative passages in documentary and experimental work. The most practical use of all: it makes an AI-generated shot feel filmed rather than animated.  
**Best in:** formats: AI-Generated Clip, Documentary Feature, Video Essay, Feature Film, Music Video, Experimental / Art Film, Heritage / Historical Documentary, Title Sequence / Opening Credits, Drama Series Episode | genres: Psychological / Arthouse, Drama, Heritage (civilisation-focused), Nature / Wildlife, Surreal / Absurdist, Tragedy, Slice of Life, Science / Educational  
**Avoid when:** In a scene with an event and dialogue it distracts for nothing. Do not let it get fast either; any perceptible speed turns it into a move that now needs a reason.  
**Prompt:** `camera drifts slowly right across the empty courtyard with no motivation, constant creeping speed, still drifting as the shot ends`  
`move.drift`

### Handheld Sway

**Also called:** unmoored sway, loose handheld, drunk sway  
**What it is:** An irregular lateral wander on the shoulder: the camera leans and returns with no fixed rhythm and no quick correction, so the frame feels unmoored.  
**Effect on the audience:** Human unease. The viewer senses that whoever holds the camera is not steady, or that the character is not.  
**Used for and where it works best:** Drunkenness, exhaustion, illness, the minutes before a collapse. In grounded drama when you want the scene to feel like it is happening now, and in horror when the character walks while afraid.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Anime (Japanese 2D), Mockumentary, AI-Generated Clip | genres: Drama, Horror, Psychological Horror, Survival, War, Coming of Age, Verite / Observational, Thriller / Suspense  
**Avoid when:** Push it until the face stops reading and you lose the performance entirely. In a formal or polished scene it looks like an execution error.  
**Prompt:** `loose handheld sway, camera leaning left and right without rhythm, framing drifting off and coming back, ending roughly framed on his face`  
**Yields to:** `move.breathing` — A formal or polished scene; sway reads as error.  
`move.handheld_sway`

### Breathing Camera

**Also called:** breathing handheld, operator breath, living frame  
**What it is:** A small continuous movement on the shoulder or in the hand: not shake and not sway, just breath and tiny corrections that keep the frame from ever going dead still.  
**Effect on the audience:** Human presence. The viewer feels somebody is in the room watching, so the shot becomes testimony rather than photography.  
**Used for and where it works best:** Documentary and interview, grounded and family drama, war scenes seen from inside the event. It is also the first difference between a shot that feels recorded and one that feels assembled, which matters most in AI-generated work.  
**Best in:** formats: Documentary Feature, Documentary Series, Interview / Video Podcast, Feature Film, Drama Series Episode, News Report / Reportage, AI-Generated Clip, Short Film, Vlog / YouTube Long-Form | genres: Drama, Verite / Observational, War, True Crime, Slice of Life, Coming of Age, Medical Drama, Tragedy, Family  
**Avoid when:** In a rigorously symmetrical composition or a polished commercial it breaks the finish. Let the movement grow even slightly and it becomes sway, which means something else entirely.  
**Prompt:** `subtle handheld breathing, natural operator micro-corrections, no visible shake, the frame never completely still, holding on the interview subject`  
**Example:** Rosetta (1999), the Dardenne brothers, the whole film carried on a close breathing handheld camera.  
**Yields to:** `move.lock_off` — Rigorous symmetry or a polished commercial.  
`move.breathing`

### Zoom In

**Also called:** zoom, lens in, focal length change in  
**What it is:** The lens magnifies the image while the camera stays put. The relationship between foreground and background never changes; the whole frame simply crops in and enlarges.  
**Effect on the audience:** The feeling of being watched. As though someone is using binoculars or a news camera; it is deliberately artificial, and the artifice is the point.  
**Used for and where it works best:** Documentary, reportage and surveillance footage, the 1970s vocabulary in period work, and comedy when you want to point at a reaction. Best when you want the shot to feel recorded rather than photographed.  
**Best in:** formats: Documentary Feature, News Report / Reportage, Documentary Series, Mockumentary, Vlog / YouTube Long-Form, Drama Series Episode, Feature Film, Meme / Comedy Edit, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Verite / Observational, True Crime, Comedy, Dark Comedy / Satire, Crime / Procedural, Political Thriller, Found Footage, Thriller / Suspense  
**Avoid when:** When you want the shot to feel cinematic and expensive; a zoom flattens the space and removes depth. Use a dolly in instead.  
**Prompt:** `slow zoom in from a wide to a medium, camera locked in place, no parallax, background compressing, ending framed on the group`  
**Source:** assumption — the package's working figure, not a published standard; the 1970s is a period-style label, not a measured figure; check it against the period references being matched.  
**Yields to:** `move.dolly_in` — When the shot must feel cinematic; zoom flattens.  
`move.zoom_in`

### Zoom Out

**Also called:** zoom back, lens out  
**What it is:** The lens widens while the camera stays put, so the frame opens and takes in more surroundings with no change of perspective.  
**Effect on the audience:** A context reveal with a cold observational quality. Dramatically weaker than a pull back, because the viewer does not feel they moved away, only that someone widened the frame.  
**Used for and where it works best:** Documentary and reportage when you open out from a speaker to their surroundings, comedy when something ridiculous is revealed around a character. In educational work it goes from detail to whole while keeping the viewpoint identical.  
**Best in:** formats: Documentary Feature, News Report / Reportage, Explainer, Vlog / YouTube Long-Form, Drama Series Episode, Mockumentary, Video Essay, Corporate / Training, Meme / Comedy Edit | genres: Verite / Observational, Comedy, Science / Educational, True Crime, Dark Comedy / Satire, Political Thriller, Crime / Procedural  
**Avoid when:** For emotional endings use a dolly out instead; a zoom out has none of the weight of departure. If the revealed context does not matter, the move does nothing.  
**Prompt:** `slow zoom out from the detail to the full room, camera locked, perspective unchanged, ending on the wide frame`  
**Yields to:** `move.dolly_out` — Emotional endings need the weight of departure.  
`move.zoom_out`

### Slow Zoom

**Also called:** creeping zoom in, long zoom  
**What it is:** A slow continuous zoom in across the length of the shot: visible, but never insistent. Usually on a face or on a still image.  
**Effect on the audience:** Tightening attention. The viewer feels their focus narrowing onto one thing.  
**Used for and where it works best:** The documentary interview at the moment of confession, archive photographs, documents and inscriptions in heritage work, where it is the primary way of moving a still image, and the monologue in television drama. Best when the image is static and needs to be given time and life.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Documentary Series, Interview / Video Podcast, Video Essay, Drama Series Episode, News Report / Reportage, AI-Generated Clip, Explainer | genres: True Crime, Historical / Biopic, Heritage (civilisation-focused), Drama, Verite / Observational, Science / Educational, Political Thriller, Mystery / Whodunit  
**Avoid when:** Applied to every image in a documentary it becomes a monotonous tic. Do not forget the end point either; a zoom still running at the cut feels severed.  
**Prompt:** `slow steady zoom in on the archive photograph, from the full frame to the boy's face at the edge, easing to a stop`  
**Yields to:** `move.zoom_pan` — Every still in a documentary getting the same zoom.  
`move.slow_zoom`

### Slow Zoom Out / Reverse Zoom

**Also called:** slow reverse zoom, receding zoom  
**What it is:** A very slow zoom out that begins on a detail and ends on a wide formal composition, with the camera never moving at all.  
**Effect on the audience:** It turns a person into part of a painting. The viewer withdraws emotionally by degrees and becomes a cold witness to a composed tableau.  
**Used for and where it works best:** Historical and literary drama, and the end of a scene you want to feel fated and already written. In heritage documentary: from one carved detail out to the full wall, so the viewer understands the detail belongs to a larger system.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Drama Series Episode, Limited Series, Video Essay, Title Sequence / Opening Credits, AI-Generated Clip | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Tragedy, Psychological / Arthouse, Mythology / Ancient Epic, Faith / Biblical Epic, Melodrama  
**Avoid when:** It needs a long shot and a still scene; in fast cutting it does nothing. If the final composition is not rigorously designed the whole idea collapses.  
**Prompt:** `very slow zoom out from the candle on the table to the full symmetrical room, camera completely static, settling on the formal wide composition`  
**Example:** Barry Lyndon (1975), Stanley Kubrick, the slow reverse zooms from detail to landscape.  
**Yields to:** `move.crash_zoom_out` — Fast cutting, where the slow reverse zoom does nothing.  
`move.slow_zoom_out`

### Crash Zoom / Snap Zoom

**Also called:** snap zoom, whip zoom, punch zoom  
**What it is:** A zoom in taken at explosive speed, one or two frames from wide to tight, with a hard stop.  
**Effect on the audience:** Astonishment, shock or a joke. The move becomes punctuation: this, look at this.  
**Used for and where it works best:** Comedy, pointing at an absurd detail; action, when something appears; the what-just-happened beat in short-form and meme edits. In anime and martial arts it is the hit before the strike.  
**Best in:** formats: Meme / Comedy Edit, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Feature Film, Anime (Japanese 2D), Trailer / Teaser, Game Cinematic / Gameplay, Music Video, Vlog / YouTube Long-Form | genres: Comedy, Dark Comedy / Satire, Action, Horror, Martial Arts / Wuxia, Shonen Battle (anime), Thriller / Suspense, Slasher  
**Avoid when:** In serious drama it breaks the tone instantly. Repeated too often it stops being punctuation and becomes noise.  
**Prompt:** `crash zoom snapping instantly from the wide two-shot to a tight close-up on the empty glass, hard stop, holding`  
**Example:** Hot Fuzz (2007), Edgar Wright, crash zooms used as comic punctuation throughout.  
**Yields to:** `move.crash_in` — Serious drama; move the camera, do not zoom.  
`move.crash_zoom`

### Crash Zoom Out

**Also called:** snap zoom out, reverse crash zoom  
**What it is:** A zoom out at explosive speed, from tight to wide in a handful of frames, stopping hard on the wide frame.  
**Effect on the audience:** A sudden reveal of the size of the problem. The viewer is yanked back and sees the context before they can process it.  
**Used for and where it works best:** Comedy, snapping back to reveal the character is standing somewhere humiliating; action, snapping back to reveal the whole army behind him; short-form, revealing scale in one hit. Best when the reveal itself is the joke or the punch.  
**Best in:** formats: Meme / Comedy Edit, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Feature Film, Trailer / Teaser, Anime (Japanese 2D), Game Cinematic / Gameplay, Music Video | genres: Comedy, Dark Comedy / Satire, Action, Adventure, Horror, Shonen Battle (anime), Thriller / Suspense  
**Avoid when:** In a serious scene it plays as overstatement. If the revealed context is weak, the punch lands on nothing.  
**Prompt:** `crash zoom out from the tight close-up, snapping back to an extreme wide revealing the crowd around him, hard stop`  
**Yields to:** `move.pullback_reveal` — A serious scene, where the snap overstates.  
`move.crash_zoom_out`

### Micro Zoom / Creep Zoom

**Also called:** imperceptible zoom, five percent zoom  
**What it is:** A zoom so slow, under five percent across the whole shot, that the viewer never registers it happening.  
**Effect on the audience:** Tension accumulating below awareness. The frame closes in with no visible cause, which is exactly why it works.  
**Used for and where it works best:** The monologue, the interrogation, the long interview, slow horror on a motionless face. It is the stable choice for a flat still or AI-generated face because it asks for no travel through space; when the move must reveal perspective or parallax, use `move.creep_in`.
**Best in:** formats: Interview / Video Podcast, Documentary Feature, Drama Series Episode, Feature Film, AI-Generated Clip, Limited Series, Heritage / Historical Documentary, Short Film | genres: Psychological Horror, Thriller / Suspense, Drama, True Crime, Mystery / Whodunit, Horror, Tragedy, Crime / Procedural  
**Avoid when:** In a short shot there is not enough time for anyone to feel it. Increase the amount and it becomes an ordinary zoom, which gives the secret away.  
**Prompt:** `almost imperceptible zoom in, less than five percent over the whole shot, camera locked, tension building on his face, no visible end point`
**Yields to:** `move.creep_in` — The move must reveal real perspective or foreground-background parallax.
`move.micro_zoom`

### Zoom and Pan

**Also called:** zoom while panning, pan-zoom  
**What it is:** A zoom and a pan together: the lens magnifies while the camera turns, so the frame closes in and shifts onto a new subject in one gesture.  
**Effect on the audience:** Search and arrival. It feels like someone spotting something and instantly going in on it, the way a news operator finds a shot.  
**Used for and where it works best:** Documentary and live event coverage, sport when attention transfers to one player, and animating stills and maps in heritage work, closing in while moving onto another part of the relief. Best when you need two moves in the time of one.  
**Best in:** formats: Documentary Feature, News Report / Reportage, Sports Broadcast / Sports Film, Heritage / Historical Documentary, Video Essay, Documentary Series, Explainer, AI-Generated Clip, Vlog / YouTube Long-Form | genres: Verite / Observational, True Crime, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Sports Drama, Political Thriller, War  
**Avoid when:** Mismatched speeds on the two axes produce a stumbling frame. In designed drama it reads cheap, because it recalls news television.  
**Prompt:** `zoom in while panning right, moving off the map legend onto the river delta and tightening at the same time, settling on the city marker`  
**Yields to:** `move.diagonal_dolly` — Designed drama, where zoom-pan reads as news television.  
`move.zoom_pan`

### Zoom to Detail and Cut

**Also called:** zoom and cut, punch to detail  
**What it is:** A fast or medium zoom that lands on one small detail, a hand, a watch, a letter, an eye, with the cut arriving at the instant of arrival.  
**Effect on the audience:** It makes the detail feel like evidence. The viewer understands that this thing will come back later in the story.  
**Used for and where it works best:** Crime and investigation, product advertising where you punch to the detail and cut to the result, and short-form when you are stacking information fast. Best when the rhythm is quick and the information has to land in minimum time.  
**Best in:** formats: Drama Series Episode, Feature Film, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Trailer / Teaser, Meme / Comedy Edit, Anime (Japanese 2D), Explainer | genres: Crime / Procedural, True Crime, Thriller / Suspense, Mystery / Whodunit, Action, Comedy, Legal Drama, Noir / Neo-Noir  
**Avoid when:** If the detail plays no part in the story the zoom is a false promise. Delay the cut past the arrival and the punch dies.  
**Prompt:** `quick zoom in from the wide table to the watch on his wrist, stopping hard on the dial, cutting on the frame it lands`  
`move.zoom_detail_cut`

### Searching Zoom / Long Lens Hunt

**Also called:** hunting zoom, news zoom, found-footage zoom  
**What it is:** A handheld zoom on a long lens: it goes in, loses the subject, corrects and finds it again, the frame never settling.  
**Effect on the audience:** Raw authenticity. The viewer believes what they are seeing was not arranged, because the camera itself is struggling to see it.  
**Used for and where it works best:** War, protest and incident coverage in reportage, found-footage horror, and drama that imitates a news broadcast. Best when you want to say the operator is far away and not allowed any closer.  
**Best in:** formats: News Report / Reportage, Documentary Feature, Mockumentary, Feature Film, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Series, Vlog / YouTube Long-Form | genres: War, Verite / Observational, True Crime, Found Footage, Horror, Political Thriller, Thriller / Suspense, Crime / Procedural  
**Avoid when:** In a polished production it reads as incompetence. Do not use it when the operator would logically be close to the action; the pretext collapses.  
**Prompt:** `handheld long lens zoom pushing in on the distant figures, losing them briefly and correcting, unsteady frame, ending roughly held on the burning car`  
**Yields to:** `move.slow_zoom` — A polished production, where hunting reads as incompetence.  
`move.searching_zoom`

### Reframe Zoom

**Also called:** correction zoom, live zoom, tidy-up zoom  
**What it is:** A very small zoom mid-shot to correct the composition after the subject has shifted: a slight tighten or widen with no dramatic intent.  
**Effect on the audience:** It makes the frame feel operated in real time by someone making decisions. This is the language of live broadcast and events.  
**Used for and where it works best:** Live broadcast, concerts, sport and video podcasts, and multi-camera sitcom. In any content you want to feel live and unstaged, a small zoom correction supplies the sense of a real operator.  
**Best in:** formats: Concert / Live Event, Sports Broadcast / Sports Film, Interview / Video Podcast, Drama Series Episode, Sitcom / Multi-Cam Comedy, News Report / Reportage, Vlog / YouTube Long-Form, Corporate / Training, Wedding / Event Film | genres: Musical, Sports Drama, Comedy, Verite / Observational, Drama, Political Thriller, Family  
**Avoid when:** In cinematic work any zoom correction looks like a mistake. Repeated corrections make the image feel unstable and amateur.  
**Prompt:** `small correcting zoom in as he leans back, tightening the frame slightly to fix the headroom, holding steady after the correction`  
**Yields to:** `move.nudge` — Cinematic work, where a zoom correction reads as mistake.  
`move.reframe_zoom`

### Rack Focus / Pull Focus

**Also called:** pull focus, focus pull, focus shift  
**What it is:** Focus travels from one plane to another inside the same shot: foreground to background or the reverse. Nothing moves; only what is sharp changes.  
**Effect on the audience:** It moves the viewer's eye by force. This is a cut without a cut, and you decide where they look.  
**Used for and where it works best:** Transferring attention between two speakers in one frame, revealing something in the background that was there all along, the notice-this beat in suspense. In heritage documentary: from the artefact in the foreground to the site behind it, tying the object to its place.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Commercial / TVC, Product Video / Motion Design, Anime (Japanese 2D), Short Film, AI-Generated Clip | genres: Drama, Thriller / Suspense, Mystery / Whodunit, Crime / Procedural, Romance, Heritage (civilisation-focused), Noir / Neo-Noir, Horror, Historical / Biopic  
**Avoid when:** If the lens does not give you shallow enough depth the shift does not register. Used in every shot it becomes a distraction and tires the eye.  
**Prompt:** `rack focus from the knife in the foreground to his face in the background, single smooth shift, holding on his face`  
**Yields to:** `move.split_diopter_device` — Both planes matter equally; you refuse to choose.  
`move.rack_focus`

### Snap Focus / Focus Throw

**Also called:** focus throw, whip focus, fast rack  
**What it is:** A focus change taken at high speed, a handful of frames, from one plane to another in a single strike.  
**Effect on the audience:** A sudden alert. Like an eye snapping onto something that was already there, which makes the viewer sit up.  
**Used for and where it works best:** Hearing a sound from behind in horror, the opponent appearing in action, a hit on the beat in music video. Best when the event is fast and does not warrant a full cut.  
**Best in:** formats: Feature Film, Anime (Japanese 2D), Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Game Cinematic / Gameplay, Drama Series Episode, Commercial / TVC | genres: Horror, Thriller / Suspense, Action, Slasher, Martial Arts / Wuxia, Shonen Battle (anime), Supernatural Horror, Mystery / Whodunit  
**Avoid when:** Thrown on an unimportant beat it reads as technical twitchiness. In a calm scene the speed simply breaks the mood.  
**Prompt:** `snap focus, instant shift from her face to the figure in the doorway behind her, sharp and immediate, holding on the doorway`  
**Yields to:** `move.rack_focus` — A calm scene, where the speed breaks mood.  
`move.snap_focus`

### Focus Reveal

**Also called:** focus-in reveal, emerging from blur  
**What it is:** The shot opens completely out of focus, shapes and colour only, then resolves gradually until the subject becomes clear. It differs from the lens Focus Reveal, which stages two planes and carries sharpness from one to the other to uncover something else: here the whole frame starts dissolved and resolves onto the same subject.  
**Effect on the audience:** Waking up. The viewer comes to consciousness with the image and feels awareness returning.  
**Used for and where it works best:** Opening a scene after a blackout, sleep or a blow, opening a flashback, opening an ad where an abstract shape resolves into the product. In heritage work: from blur to a sharp relief as narration begins.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Feature Film, Music Video, Drama Series Episode, Trailer / Teaser, Title Sequence / Opening Credits, Heritage / Historical Documentary, AI-Generated Clip | genres: Drama, Thriller / Suspense, Psychological / Arthouse, Horror, Romance, Surreal / Absurdist, Heritage (civilisation-focused), Medical Drama  
**Avoid when:** Hold the blur past a second or two and the viewer reads it as a fault in the picture. Do not repeat it inside the same piece.  
**Prompt:** `shot opens fully defocused, soft shapes only, focus resolving gradually onto her open eye, sharp and holding`  
**Yields to:** `lens.focus_reveal` — The reveal is a planted second plane.  
`move.focus_reveal`

### Focus Loss / Defocus Out

**Also called:** defocus, pull to blur, focus fade  
**What it is:** Focus slips away until the whole image is a blur, usually with the cut or the transition arriving while it is soft.  
**Effect on the audience:** Consciousness withdrawing. Fainting, dying, or leaving a moment. It is the exact opposite of a focus reveal.  
**Used for and where it works best:** Fainting, dying or being sedated in medical drama, the end of a scene before a move into memory, the last bar of a music video. Best as an exit from a scene, because the blur gives you a natural transition into whatever follows.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Short Film, Anime (Japanese 2D), Trailer / Teaser, AI-Generated Clip, Title Sequence / Opening Credits | genres: Medical Drama, Drama, Tragedy, Psychological / Arthouse, Horror, Surreal / Absurdist, Romance, War  
**Avoid when:** Used on every transition it becomes an obvious editing crutch. In a shot that must deliver information it throws the whole thing away.  
**Prompt:** `focus slips away from her face, the image dissolving into soft blur over two seconds, holding fully defocused as the light fades`  
`move.focus_loss`

### Follow Focus

**Also called:** focus follow, tracking focus  
**What it is:** Focus adjusts continuously to stay on a subject moving toward or away from the camera. It is not a shift between two planes; it is one plane being chased.  
**Effect on the audience:** It makes movement in depth possible at all. Without it any approach or retreat goes soft and the viewer disconnects.  
**Used for and where it works best:** A character walking toward the lens at a wide aperture, walking and chase scenes shot shallow, food and product work when the object moves. Essential when movement in depth is the shot itself.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Product Video / Motion Design, Music Video, Documentary Feature, Fashion Film, Game Cinematic / Gameplay, AI-Generated Clip | genres: Drama, Action, Romance, Thriller / Suspense, Crime / Procedural, Comedy, Sports Drama, Slice of Life  
**Avoid when:** With very shallow depth and fast movement any lag is visible. In unpredictable documentary situations a deeper stop is safer than an impossible chase.  
**Prompt:** `follow focus holding him sharp as he walks from the far end of the corridor to a close-up at the lens, background falling away, ending sharp on his eyes`  
**Yields to:** `lens.hyperfocal` — Unpredictable documentary movement; a deeper stop beats a chase.  
`move.follow_focus`

### Three Plane Rack

**Also called:** A-B-C focus rack, multi-plane pull  
**What it is:** A focus pull with three marks inside one shot: foreground, middle, background, hit in a deliberate order and rhythm.  
**Effect on the audience:** It speaks a full sentence in one shot: this, then this, then this. The viewer reads a relationship between three things with no cut.  
**Used for and where it works best:** Revealing a chain of clues in crime, linking three characters in one room in drama, showing three details of one product in advertising. Best when you need to prove that all three things share a place and a moment.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Product Video / Motion Design, Documentary Feature, Heritage / Historical Documentary, Anime (Japanese 2D), Short Film | genres: Crime / Procedural, Thriller / Suspense, Mystery / Whodunit, Drama, Noir / Neo-Noir, Heritage (civilisation-focused), Legal Drama, Historical / Biopic  
**Avoid when:** If the marks are not clearly composed the viewer gets lost and the shot feels indecisive. Do not go past three; the fourth is just showing off.  
**Prompt:** `rack focus from the keys in the foreground to the letter on the table to the man in the doorway, three clear stops, holding on the man`  
`move.three_plane_rack`

### Split Diopter as a Focus Device

**Also called:** split focus, diopter shot  
**What it is:** A half lens element placed in front of the taking lens so that something very close and something very far are sharp at the same time, with a soft seam between them in the frame.  
**Effect on the audience:** A particular kind of tension: two things of equal importance that you cannot choose between, with the gap between them becoming the real subject.  
**Used for and where it works best:** Thriller and suspense when the danger sits in the background and the character does not know, interrogations and confrontations, any beat where both planes matter. It is a deliberate focus device, not an error, and it replaces a rack when you refuse to choose.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Short Film, Anime (Japanese 2D), Limited Series, AI-Generated Clip | genres: Thriller / Suspense, Noir / Neo-Noir, Crime / Procedural, Horror, Mystery / Whodunit, Psychological Horror, Spy / Espionage, Drama  
**Avoid when:** If the seam falls across clean open picture the trick shows. Hide it on the edge of a column, a door frame or a shadow.  
**Prompt:** `split diopter framing, the glass in the near foreground and the doorway across the room both held in sharp focus, static frame`  
**Example:** Blow Out (1981), Brian De Palma, split diopter used through the film.  
`move.split_diopter_device`

### Focus Breathing as a Device

**Also called:** breathing lens, focus pump  
**What it is:** A small change in angle of view that happens automatically when focus is changed on certain lenses, so the frame appears to breathe slightly in and out.  
**Effect on the audience:** It supplies the feel of a real lens and a physical body behind the camera. The image reads as recorded on equipment rather than generated.  
**Used for and where it works best:** Anything you want to read as real, archival or documentary, and shots that imitate an old camera or a surveillance feed. In AI-generated work it is a small detail that buys a lot of credibility when you ask for it alongside a focus change.  
**Best in:** formats: AI-Generated Clip, Documentary Feature, Mockumentary, Feature Film, Drama Series Episode, News Report / Reportage, Experimental / Art Film, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Verite / Observational, Found Footage, True Crime, Horror, Drama, Psychological / Arthouse, War, Crime / Procedural  
**Avoid when:** In polished advertising and precise photography it reads as a lens defect. In any frame with type or exact geometry the breathing unsettles the composition.  
**Prompt:** `visible focus breathing as the lens racks, the frame swelling very slightly with the focus change, settling on the sharp foreground`  
`move.focus_breathing`

### Impact Shake

**Also called:** camera jolt, concussion shake, hit shake  
**What it is:** A short violent jolt at the moment of a blow or a blast, after which the camera recovers and settles within a second or less.  
**Effect on the audience:** It connects the viewer's body to the event. The eye believes the force, because the recording device itself was affected by it.  
**Used for and where it works best:** An explosion, a heavy fall, a landed punch, an earthquake, a monster hitting the ground in kaiju and mecha. In sports advertising and games it lands on the collision. Best when you want a physical hit without a cut.  
**Best in:** formats: Feature Film, Game Cinematic / Gameplay, Anime (Japanese 2D), Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, Music Video, Commercial / TVC, AI-Generated Clip | genres: Action, War, Disaster, Monster / Kaiju, Horror, Superhero, Mecha (anime), Shonen Battle (anime), Survival  
**Avoid when:** If the shake continues after the impact is over it turns into generic wobble and means nothing. A jolt with no visible cause usually reads as a fault; the exception is when the cause is deliberately off screen and arrives a beat later, because then the jolt is the warning.  
**Prompt:** `sharp camera jolt on the impact, single hard shake with a small settle, recovering to a steady frame within half a second`  
**Example:** Saving Private Ryan (1998), the Omaha Beach landing, the camera jolting with each nearby blast.  
`move.impact_shake`

### The Three Part Move

**Also called:** start path end, the three parts of a move  
**What it is:** Every move has three parts: a start, where it begins and what is in frame, a path, its direction and speed, and an end, the frame it comes to rest on — or, in a move carried across the cut (`move.move_across_cut`), the frame it hands on still travelling. The third part is the one most people forget.  
**Effect on the audience:** A move with a designed ending reads as intentional. A move with no ending reads as interrupted, and the viewer senses something is missing even if they cannot name it.  
**Used for and where it works best:** This is the basis of every video prompt and every instruction to an operator: state the start, the path and the end, all three. In prompting it matters most, because there is no default speed and no default resting point unless you write them.  
**Best in:** formats: all | genres: all  
**Avoid when:** Writing only the name of a move, push, pan, orbit, with no start and no end usually gives you travel without purpose; the exception is an exploratory pass you do not intend to use. The ending has to be a frame you can actually cut from.  
**Prompt:** `starts on the closed door in a wide shot, pushes forward at a steady slow pace, ends framed tight on the handle and holds`  
`move.three_part_move`

### Motivated Move

**Also called:** motivated camera, justified move  
**What it is:** The move begins because something happened in the scene: someone stood up, a sound came from one side, a door opened, a look shifted. The scene is what starts the camera.  
**Effect on the audience:** The camera disappears. The viewer does not notice that it moved, only the event that moved it.  
**Used for and where it works best:** The default in drama, documentary and any grounded work. The practical rule: let the move start a fraction after the event rather than before it, because a camera that anticipates the action admits it has read the script.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Limited Series, Short Film, Anime (Japanese 2D), Heritage / Historical Documentary, Interview / Video Podcast | genres: Drama, Crime / Procedural, Verite / Observational, Historical / Biopic, Medical Drama, Legal Drama, Thriller / Suspense, Slice of Life, Family  
**Avoid when:** Do not justify every move mechanically, or the camera becomes a follower with no point of view. Sometimes the unmotivated move is precisely what the scene needs, especially in horror.  
**Prompt:** `static frame, then as he stands the camera rises with him, motivated by his movement, settling at his new eye height`  
**Yields to:** `move.unmotivated_move` — Horror, where the camera needs its own agenda.  
`move.motivated_move`

### Unmotivated Move

**Also called:** unjustified move, authorial camera  
**What it is:** A move that begins with no cause inside the scene: nobody moved, no sound came, and yet the camera travels.  
**Effect on the audience:** It makes the camera an independent entity. The viewer senses that something other than the characters is paying attention, which is inherently unsettling.  
**Used for and where it works best:** Horror, where the camera approaches and the character does not know; psychological thriller; experimental work. In heritage documentary a slow unmotivated drift over ruins gives the sense that the place is watching us.  
**Best in:** formats: Feature Film, Short Film, Experimental / Art Film, Heritage / Historical Documentary, Anime (Japanese 2D), AI-Generated Clip, Drama Series Episode, Music Video | genres: Horror, Psychological Horror, Supernatural Horror, Surreal / Absurdist, Thriller / Suspense, Psychological / Arthouse, Heritage (civilisation-focused), Gothic / Vampire  
**Avoid when:** In comedy or family drama it is simply odd for nothing. Use it often and the viewer acclimatises, which spends the entire effect.  
**Prompt:** `nothing moves in the scene, the camera begins a slow unmotivated push toward the sleeping man, no cause in frame, continuing as the shot ends`  
**Yields to:** `move.motivated_move` — Comedy or family drama, odd for nothing.  
`move.unmotivated_move`

### Move on the Line

**Also called:** move on dialogue, start on the word  
**What it is:** The move begins or ends on one specific word of dialogue, not at the top or the bottom of the shot.  
**Effect on the audience:** It welds the move to the meaning. The viewer does not see a move; they feel the line itself get closer or heavier.  
**Used for and where it works best:** The confession, the threat, the lie, the verdict in legal drama. The method: find the key word in the line, start the push on it and let it settle on the last word. In documentary narration, start the slow zoom on the king's name or the date.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Heritage / Historical Documentary, Interview / Video Podcast, Anime (Japanese 2D), Soap Opera / Telenovela | genres: Drama, Legal Drama, Crime / Procedural, Thriller / Suspense, Historical / Biopic, Melodrama, Political Thriller, Tragedy  
**Avoid when:** Start before the line and the camera admits it knows what is coming. Start too late and it reads as a delayed reaction.  
**Prompt:** `static on his face, the push begins exactly on the word he lies about, tightening slowly, settling as he finishes the sentence`  
`move.move_on_line`

### Move on the Look

**Also called:** move on the eyeline, follow the glance  
**What it is:** The move starts the instant a character shifts their gaze, and the camera travels in the direction of that look.  
**Effect on the audience:** The viewer feels they are seeing through the character's eyes without a separate point of view shot. The link becomes internal rather than editorial.  
**Used for and where it works best:** A smart alternative to cutting away to what a character sees in long scenes, and an essential tool inside a long take. In horror: she notices something, the camera goes there before she does, and the viewer is left one step ahead of her.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Anime (Japanese 2D), Documentary Feature, Limited Series, Game Cinematic / Gameplay, AI-Generated Clip | genres: Drama, Horror, Thriller / Suspense, Mystery / Whodunit, Crime / Procedural, Romance, Psychological / Arthouse, Supernatural Horror  
**Avoid when:** If the move goes the other way from the glance the viewer loses the geography. Do not use it if the character is looking at nothing; the glance itself has to be deliberate.  
**Prompt:** `she turns her eyes to the window, the camera begins moving left on that glance, travelling at her speed, settling on the window she is looking at`  
`move.move_on_look`

### Move on the Sound

**Also called:** sound-cued move, move on the off-screen noise  
**What it is:** A sound arrives from outside the frame, a knock, a break, a scream, a footstep, and the camera starts moving toward it or away from it.  
**Effect on the audience:** It makes the space outside the frame real. The viewer understands the world is larger than the screen and that something is happening out there.  
**Used for and where it works best:** Horror and suspense before the source appears, drama when a sound comes from another room, documentary when an event starts off frame. The rule: sound first, move a fraction later, because the ear is faster than the eye.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Short Film, Anime (Japanese 2D), Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), Limited Series, AI-Generated Clip | genres: Horror, Thriller / Suspense, Mystery / Whodunit, Supernatural Horror, Crime / Procedural, Drama, War, Psychological Horror  
**Avoid when:** If the camera moves before or exactly with the sound, cause and effect are lost. If the source is never shown, that has to be a decision, not an oversight.  
**Prompt:** `static on the kitchen, a crash sounds off frame, the camera starts panning right a beat later toward the hallway, settling on the empty doorway`  
`move.move_on_sound`

### Move on the Beat

**Also called:** beat-synced move, move to the music  
**What it is:** The move starts, ends or changes speed on a defined musical beat, and sometimes the whole move is cut to the length of a musical phrase.  
**Effect on the audience:** It makes the picture feel part of the song rather than laid over it. The viewer gets a physical pleasure from the match even when they never consciously notice it.  
**Used for and where it works best:** Music video, short-form, music-led advertising and trailers, where the move grows with the drum. The practical method: mark the beats first, then design the moves so their endings land on them.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Commercial / TVC, Lyric Video, Dance Film, Concert / Live Event, Title Sequence / Opening Credits, Kids Content | genres: Musical, Action, Comedy, Romance, Sports Drama, Fantasy / Epic, Superhero, Family  
**Avoid when:** If every move lands on every beat the piece becomes a metronome and tires the viewer. Let some moves break the grid so the matched ones keep their value.  
**Prompt:** `the push begins on the downbeat and reaches its tightest framing exactly on the next beat, holding through the bar`  
`move.move_on_beat`

### Masked Move

**Also called:** hiding the move in the action, covered move  
**What it is:** The move begins at the same instant as a strong movement inside the frame, someone standing, a door opening, a crowd shifting, so the eye is busy with the action and never notices the camera.  
**Effect on the audience:** You get a camera move the viewer never registers as one. It is the cleanest way there is to change a frame.  
**Used for and where it works best:** Grounded and documentary scenes that cannot carry a visible camera, and long shots that need several reframes. The same principle hides a cut: let a body cross the frame at the moment of the change.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Limited Series, Short Film, Anime (Japanese 2D), AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, Crime / Procedural, Verite / Observational, War, Historical / Biopic, Medical Drama, Thriller / Suspense, Slice of Life  
**Avoid when:** If the internal action is weak it hides nothing and exposes the camera instead. Do not lean on it for every transition either; some moves are meant to be seen.  
**Prompt:** `as he stands and turns, the camera uses his movement to start its own push, arriving at the tighter frame by the time he settles`  
`move.masked_move`

### Two Stage Move

**Also called:** staged move, move stop move  
**What it is:** The move starts, stops at an intermediate point and settles, then begins again on a new event and finishes somewhere else.  
**Effect on the audience:** It divides the scene into two acts inside one shot. The middle stop becomes punctuation: something changed here.  
**Used for and where it works best:** A dialogue scene that turns halfway, an interrogation that produces a confession, any long shot that has to develop without a cut. Best in long takes and documentary, because it gives you escalation in two steps.  
**Best in:** formats: Feature Film, Limited Series, Drama Series Episode, Documentary Feature, Short Film, Interview / Video Podcast, Anime (Japanese 2D), Heritage / Historical Documentary | genres: Drama, Crime / Procedural, Legal Drama, Thriller / Suspense, Mystery / Whodunit, Political Thriller, Historical / Biopic, Tragedy  
**Avoid when:** If the middle stop is too short it does not read as a stage; it reads as hesitation. More than two stages in one shot and the structure is lost.  
**Prompt:** `push in from wide to medium and hold, then on his admission push again from medium to a tight close-up, settling on his eyes`  
**Yields to:** `move.speed_break` — Escalation without a readable stop in the middle.  
`move.two_stage_move`

### Speed Break / Mid-Move Acceleration

**Also called:** speed change mid-move, accelerating move  
**What it is:** The move starts at one speed and changes it mid-travel on a specific event: a sudden acceleration or a sudden slowdown, without ever stopping.  
**Effect on the audience:** The change of speed becomes the event. The viewer feels the shot noticed something, or thought better of it.  
**Used for and where it works best:** The slow push that accelerates when the truth lands, the fast move that slows as it finds the body. Best in horror and thriller, and in trailers when you need escalation inside a single shot.  
**Best in:** formats: Trailer / Teaser, Feature Film, Drama Series Episode, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Music Video, AI-Generated Clip | genres: Horror, Thriller / Suspense, Action, Psychological Horror, Mystery / Whodunit, Supernatural Horror, Shonen Battle (anime), Crime / Procedural  
**Avoid when:** A change with no cause reads as an execution fault. Do not change speed more than once in a shot; a stuttering move loses all authority.  
**Prompt:** `slow push in, then accelerating sharply as the door opens behind her, continuing fast and stopping hard on her face`  
`move.speed_break`

### Ease In and Ease Out

**Also called:** ease in ease out, smooth acceleration curve  
**What it is:** A speed curve: the move accelerates from zero, runs, then decelerates into its rest. Not one constant speed from first frame to last.  
**Effect on the audience:** Human and natural. This is the curve our bodies and eyes actually move on, so the shot feels honest and comfortable to watch.  
**Used for and where it works best:** The default almost everywhere: drama, advertising, documentary, gentle music video. Write it explicitly in a prompt, because a move at one flat speed with no acceleration comes out mechanical and cold and exposes the machinery.  
**Best in:** formats: all | genres: all  
**Avoid when:** When you want a machine or a surveillance feel, a soft curve destroys it. An over-long deceleration makes the shot feel exhausted.  
**Prompt:** `dolly in with a gentle ease-in at the start and a long ease-out at the end, no abrupt changes, settling softly on the final framing`  
**Yields to:** `move.linear_move` — A machine, system or surveillance feel.  
`move.ease_in_out`

### Linear Move / Constant Speed

**Also called:** constant velocity move, motion control move  
**What it is:** A speed curve: the move runs at exactly one speed from the first frame to the last, with no acceleration and no deceleration.  
**Effect on the audience:** Mechanical, cold and precise. The viewer senses a machine, a system, or an eye that does not tire.  
**Used for and where it works best:** Psychological thriller and crime when you want cold observation, product and technology video with its even turntable rotation, science fiction interiors inside a ship or a facility. Also in comparison montage, because a constant speed repeats exactly.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Feature Film, Drama Series Episode, Corporate / Training, Explainer, 3D CG Animation, AI-Generated Clip, Experimental / Art Film | genres: Thriller / Suspense, Crime / Procedural, Sci-Fi, Cyberpunk, Dystopia / Post-Apocalyptic, Science / Educational, Noir / Neo-Noir, Psychological Horror  
**Avoid when:** In an emotional scene it kills the feeling and distances the viewer. If it ends at full speed with no settle, the cut feels amputated unless that is the intention.  
**Prompt:** `perfectly linear push at a constant speed, no acceleration or deceleration at any point, ending while still moving at the same rate`  
**Yields to:** `move.ease_in_out` — An emotional scene, where constant speed kills feeling.  
`move.linear_move`

### Snap Timing

**Also called:** snap curve, hard in hard out, instant start  
**What it is:** A speed curve: the move jumps from zero to full speed instantly and stops instantly, with no acceleration or deceleration at either end.  
**Effect on the audience:** Violence or comedy. The hardness itself is the meaning, because nothing in nature moves this way.  
**Used for and where it works best:** Precise deadpan comedy, anime and manga on the moment of the strike, short-form and meme edits, motion design and logo animation. Best when you want the shot to feel constructed, deliberate and exact.  
**Best in:** formats: Meme / Comedy Edit, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Commercial / TVC, Product Video / Motion Design, Title Sequence / Opening Credits, Trailer / Teaser, Kids Content, 2D Animation (Western / Cartoon) | genres: Comedy, Dark Comedy / Satire, Action, Shonen Battle (anime), Martial Arts / Wuxia, Family, Superhero, Surreal / Absurdist  
**Avoid when:** In grounded drama it shatters the illusion. Used repeatedly it turns a piece into a chain of hits with nowhere to breathe.  
**Prompt:** `instant snap pan to the left, full speed from the first frame, stopping dead on the new composition with no settle`  
**Yields to:** `move.ease_in_out` — Grounded drama, where the hard curve shatters illusion.  
`move.snap_timing`

### The Speed Ladder of a Push In

**Also called:** push speed scale, choosing the push speed  
**What it is:** The same push at four speeds gives four meanings: an imperceptible creep, slow, medium, and fast ending in a hard stop. The distance can be identical; the entire difference is time.  
**Effect on the audience:** The creep produces unexplained anxiety, slow produces realisation, medium produces decision, fast produces shock. The viewer reads the speed before they read the image.  
**Used for and where it works best:** This is the single most important choice in a dramatic scene. Decide what the viewer should feel, then pick the rung. In a prompt, name the rung explicitly, creep, slow, medium, fast with a hard stop, because the word push on its own carries no speed at all.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Trailer / Teaser, Anime (Japanese 2D), Heritage / Historical Documentary, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, Thriller / Suspense, Horror, Mystery / Whodunit, Crime / Procedural, Psychological Horror, Historical / Biopic, Tragedy  
**Avoid when:** Do not run the same speed in every scene or you lose the ability to escalate at all. Keep the fastest rung for one or two moments in the whole piece.  
**Prompt:** `medium speed push in from a medium shot to a close-up over four seconds, even pace, easing out and settling on his eyes`  
`move.speed_ladder`

### Settle Before the Cut

**Also called:** land the move before you cut, hold after the move  
**What it is:** A timing decision: the move finishes, settles and holds still for a few frames before the cut arrives, instead of cutting while the camera is still travelling.  
**Effect on the audience:** It gives the viewer a chance to read and absorb the final frame. Cutting on movement feels like an interruption; cutting on stillness feels like a completed sentence.  
**Used for and where it works best:** Any shot that ends on information, a face or a product, the end of a scene, the end of a documentary section. The practical rule in the edit: leave half a second to a second of stillness after the settle, and in a prompt ask the shot to end static so you have handles to cut on.  
**Best in:** formats: all | genres: all  
**Avoid when:** Sometimes cutting on the move is exactly right, in action, chases and short-form, because motion pulls the motion that follows. The rule is not sacred, but breaking it has to be a decision.  
**Prompt:** `the push completes and the frame locks off, holding completely still on the final composition for a full second before the shot ends`  
**Yields to:** `move.move_across_cut` — Action, chases and short-form; cut on motion.  
`move.settle_before_cut`

### Move Across the Cut

**Also called:** matched move across a cut, continuing motion  
**What it is:** Shot one ends while still moving and shot two starts already moving in the same direction at a similar speed, so the viewer reads one continuous move split across two shots.  
**Effect on the audience:** It hides the cut and makes the scene feel like one long take. Momentum crosses the join and pulls the viewer forward.  
**Used for and where it works best:** Assembling a long take out of short shots, and the practical way to build a continuous scene from short AI clips: have every clip start and end already travelling in the same direction. In action and short-form it builds a rhythm that never lets go.  
**Best in:** formats: AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Trailer / Teaser, Music Video, Game Cinematic / Gameplay, Drama Series Episode, Commercial / TVC, Anime (Japanese 2D) | genres: Action, Thriller / Suspense, Adventure, Musical, War, Superhero, Crime / Procedural, Martial Arts / Wuxia  
**Avoid when:** If direction or speed differ much between the two shots, the cut becomes more visible rather than less. Keep the shot sizes in a similar ratio too, or the viewer feels a jump.  
**Prompt:** `the shot begins already moving right at the same speed the previous shot ended, continuing without pause, settling at the end of the combined move`  
`move.move_across_cut`

### Starting in Motion

**Also called:** enter on the move, no static start  
**What it is:** The shot opens with the camera already travelling, with no static beat at the head, as if the viewer walked in on a move already running.  
**Effect on the audience:** It drops the viewer straight into the scene. No introduction, no breath, and the sense that events do not wait for anybody.  
**Used for and where it works best:** Scene openings in action and suspense, the first second of a vertical short where you cannot afford a static beat, and building pace in a trailer. Best when the previous shot ended moving and you want the momentum carried on.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Feature Film, Drama Series Episode, Music Video, Game Cinematic / Gameplay, Commercial / TVC, Meme / Comedy Edit, AI-Generated Clip | genres: Action, Thriller / Suspense, Crime / Procedural, Comedy, Adventure, Superhero, War, Spy / Espionage  
**Avoid when:** In quiet or formal scenes it looks like the shot was trimmed wrong. If every shot starts moving, the viewer is never given anywhere to rest.  
**Prompt:** `the shot opens already tracking left at speed, no static frame at the head, continuing through the crowd and settling on the stall`  
**Yields to:** `move.hold_then_move` — Quiet or formal scenes, where it looks mistrimmed.  
`move.start_in_motion`

### Matching Move Size to Shot Size

**Also called:** move scale, small move on a close-up  
**What it is:** A rule: the tighter the shot or the longer the lens, the smaller the move has to be, because the same distance produces a far larger change inside a narrow frame.  
**Effect on the audience:** It protects readability. A proportioned move reads as professional and an unproportioned one reads as amateur, even when the viewer cannot say why.  
**Used for and where it works best:** A daily rule in execution and in prompt writing: on a close-up ask for a very small push; on a wide you can ask for real distance. In AI-generated work it is the difference between a stable close-up and a close-up that comes apart.  
**Best in:** formats: all | genres: all  
**Avoid when:** Sometimes breaking it is the point: a large move on a very tight frame produces chaos and panic. Break it deliberately, not because you forgot the arithmetic.  
**Prompt:** `very small push on the close-up, a few centimetres only, the framing tightening slightly and settling on the eyes`  
`move.move_scale_rule`

### Foreground Parallax

**Also called:** foreground element, layered depth move, occlusion layer  
**What it is:** A rule: place something very close to the lens before starting any travelling move, so it crosses the frame during the move and travels far faster than the background.  
**Effect on the audience:** The speed difference between layers is what convinces the brain that the space is real. Without it even the strongest move feels like a picture sliding around.  
**Used for and where it works best:** Almost every travelling move: dolly, track, orbit, flight. In practice: a branch, a column, a table edge, a shoulder, a curtain, a bottle. It is also the single most valuable thing to ask for in a video prompt if you want the result to feel shot on a real lens.  
**Best in:** formats: AI-Generated Clip, Feature Film, Commercial / TVC, Product Video / Motion Design, Heritage / Historical Documentary, Music Video, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, 3D CG Animation | genres: Drama, Heritage (civilisation-focused), Action, Thriller / Suspense, Historical / Biopic, Romance, Nature / Wildlife, Fantasy / Epic  
**Avoid when:** If the foreground blocks the subject at the moment that carries the information, the shot is wasted. If it sits far from the lens it produces no speed difference at all; it has to be genuinely close.  
**Prompt:** `dolly forward with a hanging branch passing close across the lens in the first second, strong layer separation against the distant wall, settling on the doorway`  
`move.foreground_parallax`

### Screen Direction of a Move

**Also called:** left to right, right to left, direction grammar  
**What it is:** The direction of a move carries learned meaning: left to right reads as progress and departure for an audience that reads left to right, and the reverse reads as return or resistance.  
**Effect on the audience:** It gives the viewer the story's direction without a word. Reversing it inside a scene reads as a turn or a retreat.  
**Used for and where it works best:** Road movies, journeys and chases: send the outbound one way and the return the other, so the viewer follows without a map. In war and sport, the direction of attack must stay constant through a sequence. In heritage work, let the historical journey run one way for the whole film.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Sports Broadcast / Sports Film, Anime (Japanese 2D), Game Cinematic / Gameplay, Trailer / Teaser, Kids Content | genres: Road Movie, War, Adventure, Western, Historical / Biopic, Heritage (civilisation-focused), Sports Drama, Action  
**Avoid when:** Do not lean on this convention alone with an audience that reads right to left, where the effect is weaker or inverted; let the action itself carry the meaning. Any unmotivated change of direction destroys the geography of the scene.  
**Prompt:** `tracking move travelling left to right with him as he leaves the village, direction held consistently, settling as he reaches the road`  
**Yields to:** AUTHORITY the audience's reading direction — Right-to-left audiences; let the action carry meaning.  
`move.screen_direction_move`
