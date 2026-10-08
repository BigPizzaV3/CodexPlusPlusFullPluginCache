# 3D CG, VFX and Virtual Production

32 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Commit the Register Before the Craft

**Also called:** the CG selector, register before craft, what is this image made of  
**What it is:** The card at the head of the `cg.` shelf. It does not describe an effect. It asks the three questions the shelf's own pair graph and its own `Avoid when:` boundaries ask over and over — **what is this image made of, is there a plate it has to disappear into, and what in it has to be believed** — and hands back a named shortlist for each answer. The questions were read off the shelf, not invented: eight of the conditions the cards yield on turn on register, and twelve of the boundaries they refuse on turn on a seam. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so the register was decided before anyone budgeted a simulation, rather than after — which is the order the shelf's own traffic runs in.  
**Used for and where it works best:** Answer the three questions **out loud, in one sentence each, before you open the shelf, and answer the first one before the shot is budgeted.** Every edge on this shelf that crosses from craft to look runs one way: the register decides and the craft obeys. Decide it last and you will have paid for flesh scattering on a character the design was never going to allow. Where two registers fight for one frame, that is two pieces and not one shot — the only card here that permits the mix names it as its single exception, and every other card that touches it calls the result a broken image.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The look is measured off an existing plate, a reference frame or a locked grade.** There the register is not chosen, it is matched, and the shelf's own seam cards say so in their own `Avoid when:` — one anamorphic-looking shot announces itself as synthetic when the rest of the film was shot spherical. Also **distrust axis one whenever your honest answer is its first value**: eighteen of the thirty reachable cards live under *photographic*, so on a live-action-matched piece the fork has barely moved and the other two axes carry the whole map. And **the hardest warning is about what this map is not**: it is a map of registers, because that is all the pair graph on this shelf contains. It cannot tell you **whether** you need cloth, hair, a crowd, a roto or a sky — those cards coexist in one frame, nothing on the shelf routes between them, and a reader who asks this card *which simulation* gets an answer it has no right to give. Ask it *which register*, then take the craft block as a checklist.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — What is this image made of, and has the piece committed to it?**
Asked first, because it is the condition the shelf repeats most and the only one anything on the shelf yields on. Eight conditions turn on it, five of them pointing at one card: *"Budget or time will not carry believable realism"* (`cg.photoreal_render`), *"No painters and no hours for hand-painted texture"* (`cg.arcane_painterly`), *"A strongly stylised character, where flesh realism breaks the design"* (`cg.sss_skin`), *"The story needs facial emotion in close-up"* (`cg.low_poly_retro`), *"The story depends on facial expression"* (`cg.voxel`). Three more arrive from the drawn shelf next door and run in the same direction — a flat register giving way when the work needs material, a drawn register giving way when the water has to behave — and `cg.mocap` yields straight out of the shelf when the character is a cartoon that needs exaggeration. It is asked first for a second reason too: answering it *photographic* closes the fork and opens nothing, so you want to know that before you spend a question.

**Axis 2 — Is there a plate, and must the seam hold?**
Only one card yields on this — `cg.anamorphic_sim`, *"The rest of the film was shot spherical"* — and that scarcity is the finding rather than a weakness. The condition is stated a dozen times instead as a refusal: *"The seam between real and added has to hide behind something natural"* (`cg.set_extension`), *"If you do not regrade the ground to the new sky the shot lies out loud"* (`cg.sky_replacement`), *"The moment the viewer notices it, it is no longer invisible"* (`cg.invisible_vfx`), *"With no reflection, no glow and no finger shadow the screen looks like a paper sticker"* (`cg.screen_replacement`), *"If it was captured at a different hour than the plate, every reflection lies"* (`cg.hdri_ibl`), *"A mismatch in head shape between the double and the actor ruins it"* (`cg.face_replacement`), *"Treat the whole scene, not only the face"* (`cg.deaging`). **The field that forbids is doing the entire job here**, because a comp card has nothing to yield to — it has a plate or it does not.

**Axis 3 — What has to be believed: a face, a mass in motion, or a place?**
Five conditions turn on it and they are the sharpest on the shelf, because each one names what its card cannot do: *"The story needs facial emotion in close-up"*, *"The story depends on facial expression"*, *"The scene needs intimate emotion or tension"* (`cg.isometric_diorama`, which leaves the shelf entirely to find it), *"Creature design sits too far from the actor's face"* (`cg.performance_capture`), *"Gait, weight and body still read old"* (`cg.deaging` — the face was fixed and the body was not). Asked last, because it narrows a register to two or three cards rather than picking the register.

---

**The map**

**Axis 1 — what the image is made of**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Photographic — it has to be taken for a record** (eighteen) | `cg.photoreal_render` · `cg.unreal_cinematic` · `cg.lens_artifacts` · `cg.anamorphic_sim` · `cg.sss_skin` · `cg.hair_fur_sim` · `cg.cloth_sim` · `cg.crowd_sim` · `cg.fluid_sim` · `cg.mocap` · `cg.performance_capture` · `cg.deaging` · `cg.face_replacement` · `cg.set_extension` · `cg.sky_replacement` · `cg.roto` · `cg.screen_replacement` · `cg.invisible_vfx` |
| **Drawn or painted — a hand made it and the image says so** (three) | `cg.npr_toon` · `cg.cel_shaded_3d` · `cg.arcane_painterly` |
| **Made of one substance or one unit — clay, cubes, facets, a flattened plane, a corruption** (five) | `cg.clay_stopmo_sim` · `cg.voxel` · `cg.low_poly_retro` · `cg.isometric_diorama` · `cg.glitch_3d` |
| **Graphic — the addition is information and is meant to be read** (four) | `cg.hologram_ui` · `cg.xray_body` · `cg.assembly_build_up` · `cg.morph_3d` |

**Axis 2 — is there a plate**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Yes, and the seam is the whole job** (nine) | `cg.set_extension` · `cg.sky_replacement` · `cg.roto` · `cg.screen_replacement` · `cg.invisible_vfx` · `cg.deaging` · `cg.face_replacement` · `cg.lens_artifacts` · `cg.anamorphic_sim` |
| **No — the frame is generated whole and the only match required is with itself** (sixteen) | `cg.photoreal_render` · `cg.npr_toon` · `cg.cel_shaded_3d` · `cg.arcane_painterly` · `cg.unreal_cinematic` · `cg.clay_stopmo_sim` · `cg.low_poly_retro` · `cg.voxel` · `cg.isometric_diorama` · `cg.sss_skin` · `cg.hair_fur_sim` · `cg.cloth_sim` · `cg.crowd_sim` · `cg.fluid_sim` · `cg.mocap` · `cg.performance_capture` |
| **Yes, and the addition announces itself — it fails by being unreadable, not by being noticed** (five) | `cg.hologram_ui` · `cg.xray_body` · `cg.assembly_build_up` · `cg.morph_3d` · `cg.glitch_3d` |

**Axis 3 — what has to be believed**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A face, close, and the eye will study it** (eight) | `cg.sss_skin` · `cg.hair_fur_sim` · `cg.performance_capture` · `cg.deaging` · `cg.face_replacement` · `cg.npr_toon` · `cg.cel_shaded_3d` · `cg.arcane_painterly` |
| **A body or a mass in motion — weight, speed and behaviour over time** (seven) | `cg.mocap` · `cg.cloth_sim` · `cg.crowd_sim` · `cg.fluid_sim` · `cg.morph_3d` · `cg.assembly_build_up` · `cg.glitch_3d` |
| **A place, a surface or a system, with nobody in it who has to be believed** (fifteen) | `cg.set_extension` · `cg.sky_replacement` · `cg.roto` · `cg.screen_replacement` · `cg.invisible_vfx` · `cg.isometric_diorama` · `cg.voxel` · `cg.low_poly_retro` · `cg.clay_stopmo_sim` · `cg.photoreal_render` · `cg.unreal_cinematic` · `cg.lens_artifacts` · `cg.anamorphic_sim` · `cg.hologram_ui` · `cg.xray_body` |

*A card appears once per axis. The answer is the intersection of the three shortlists. Under the second axis's first value the intersection is normally the whole comp block at once, because those cards are a list of jobs rather than a choice between them.*

---

**The default, and the one against it**

**The default is `cg.npr_toon`, and the trap was checked before it was named.** It takes five inbound edges, more than anything else on the shelf, and in-degree alone measures how often a shelf runs out of room rather than what it falls back on. So the conditions behind those five were counted instead of the edges, and there are **three distinct ones**: the design is already stylised and flesh realism contradicts it (`cg.sss_skin`); the work cannot be afforded, which `cg.photoreal_render` and `cg.arcane_painterly` state from opposite ends in the same breath — no budget for realism, no painters for the alternative to it; and a face has to carry a close-up while the register chosen cannot build one, which `cg.low_poly_retro` and `cg.voxel` state in almost identical words. Five edges, three reasons, arriving from both halves of the shelf. **That is a fallback and not a door out** — the shelf, asked where to retreat to, retreats here.

**And the default argues against itself, which is why the field is earned rather than filled.** `cg.npr_toon`'s own `Avoid when:` says the style *has to be a full decision, not a filter dropped over a realistic scene, or it lands half way between the two.* The shelf's most-reached card is the one card that warns you not to arrive at it by retreat — and two of its three inbound conditions are exactly a retreat. A reader who follows the graph honestly lands on a card telling him to go back and choose it on purpose.

**The one against it is `cg.clay_stopmo_sim`.** Nothing routes to it and it routes to nothing, and the reason is structural rather than accidental: it is the only card here whose law binds the **whole frame** instead of one element. *Everything in the world also has to be made of a material, a fabric sky and gelatin water, because a photoreal sky above a clay character breaks the rule the shot is built on.* Every other register is a treatment you can put on one subject and leave the rest of the plate alone; this one is a contract signed before the first asset exists, and **a card you must commit to in advance cannot be anything's fallback** — which is precisely why the pair graph has no way to reach it. It carries its own single exception in prose rather than in a pair field, a story about a handmade figure inside a real world, and that is the only permitted mix on the shelf. Choose it against the grain on heritage and on children's work, where it buys a warmth the photographic register cannot be paid to produce, and where its total discipline removes the failure every other register invites: the half-committed image. Its near cousin against the grain is `cg.isometric_diorama`, the only card that leaves the shelf altogether rather than yield to a sibling, and likewise never yielded to by anything.

---

**The unasked**

**Twenty-five of the thirty reachable cards are the target of no `Yields to:` field anywhere in the package.** Only five are ever routed to: `cg.npr_toon`, `cg.arcane_painterly`, `cg.fluid_sim`, `cg.mocap` and `cg.face_replacement`. The rest can be chosen and nothing ever sends you to them. By id:

`cg.morph_3d` · `cg.set_extension` · `cg.sky_replacement` · `cg.deaging` · `cg.crowd_sim` · `cg.cloth_sim` · `cg.hair_fur_sim` · `cg.performance_capture` · `cg.roto` · `cg.screen_replacement` · `cg.invisible_vfx` · `cg.sss_skin` · `cg.lens_artifacts` · `cg.photoreal_render` · `cg.cel_shaded_3d` · `cg.unreal_cinematic` · `cg.clay_stopmo_sim` · `cg.low_poly_retro` · `cg.voxel` · `cg.isometric_diorama` · `cg.glitch_3d` · `cg.hologram_ui` · `cg.xray_body` · `cg.assembly_build_up` · `cg.anamorphic_sim`

**And the shape of that list is the finding, not its length.** Every card under the second axis's first value is on it — all nine of the seam cards, without exception — and so is every card under its third value, all five of the announced ones. **Nothing in the package has ever routed a reader to a compositing card, and nothing ever could**, because a pair field says *in situation X, not this card — that one*, and a comp card has no *that one*. You do not choose a sky replacement instead of a roto; the plate decides whether you owe both, and then you owe both. The same holds across the simulation block: only `cg.fluid_sim` is reached at all, and both edges that reach it come from the drawn shelf choosing against a flat register — which is the look decision again, arriving from outside. **The pair graph on this shelf is a graph of registers and nothing else.** Every reader who filled a field here was holding one frame and asking what it was made of; none was holding a shot list and asking what it would cost. That is why axis two had to be read off refusals, and why the craft block is a checklist under an answer rather than a fork.

The second thing the list shows is a hole with a name. **`cg.roto`'s own `Avoid when:` sends the reader at a card that does not exist**: *do not commit to a long roto shot if a green screen could have covered it.* Its `What it is:` names the same absence again — hand tracing is what you do *when there was no green screen*. So the shelf's most expensive card defines itself twice by the cheaper technique, and the package has no chroma-key craft card to define it against: the only green screen anywhere in it is a vertical-format card about a creator standing over a product page, which is a shape of video and not a way of pulling a matte. **The card this shelf wants is the one that says what has to be true on the day for a key to be possible** — spill, separation from the screen, distance, hair, glass, smoke, and what it costs to get any of them wrong — because that is the decision `cg.roto` is the consequence of, and it is currently made by nobody, before anyone reaches this shelf at all. `cg.roto` names the second half of the same hole in the same line: *soft edges such as hair and haze are never solved by hand tracing alone*, and nothing on the shelf says what does solve them.

`cg.register_before_craft`

---

### 3D Morph Transition

**Also called:** geometry morph, shape transformation  
**What it is:** One 3D form transforms into another in a continuous move: the geometry itself stretches and reshapes, rather than two pictures cross-fading over each other.  
**Effect on the audience:** It states that the two things are one thing in two states. The brain accepts the relationship without a word of explanation.  
**Used for and where it works best:** Linking a child to the man he becomes, a map to the city, wet clay to an inscribed tablet. In advertising for turning the old generation of a product into the new one, and in titles or science documentary to show an evolution in five seconds.  
**Best in:** formats: Title Sequence / Opening Credits, Commercial / TVC, Product Video / Motion Design, Explainer, 3D CG Animation, Heritage / Historical Documentary, Music Video, Trailer / Teaser | genres: Science / Educational, Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Sci-Fi, Drama, Surreal / Absurdist  
**Avoid when:** If the two forms are unrelated the morph is a software trick with nothing behind it. Do not stretch it either; a slow morph invites the eye to study the errors instead of enjoying the idea.  
**Prompt:** `seamless 3D morph, the clay tablet reshaping into a standing statue, geometry flowing rather than cross-fading`  
**Yields to:** `trans.dissolve` — The two forms are unrelated; cross-fade instead of morphing.  
`cg.morph_3d`

### Set Extension

**Also called:** digital set extension, partial set build  
**What it is:** You build a small real portion of the location (a wall, a staircase, two columns) and continue the rest in CG on top of the plate. The actor touches something real while the world extends digitally.  
**Effect on the audience:** It marries the honesty of a real set to the scale of an impossible one. The actor plays against real stone so the performance stays true, while the viewer sees a whole city.  
**Used for and where it works best:** Any historical reconstruction: build one row of columns and extend the temple, build a section of wall and extend the city. In period series it is the economic answer, and in heritage documentary it lets you shoot the real site and return it to its own century.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Docudrama / Reenactment, Limited Series, Commercial / TVC, 3D CG Animation, Trailer / Teaser | genres: Historical / Biopic, Heritage (civilisation-focused), Fantasy / Epic, War, Mythology / Ancient Epic, Sci-Fi, Faith / Biblical Epic, Drama  
**Avoid when:** The seam between real and added has to hide behind something natural, a ceiling line, a shadow, a wall edge, or the eye finds it. Avoid extending upward when the location light is flat, because the addition will read brighter than the build.  
**Prompt:** `practical stone colonnade in the foreground with the rest of the temple extended in CG above and behind, seamless light match`  
**Example:** Gladiator (2000), where the upper tiers of the arena are a digital extension of a partially built set.  
`cg.set_extension`

### Sky Replacement

**Also called:** sky comp, cloud replacement  
**What it is:** You remove the blown out or grey sky from the plate and replace it with another one: epic cloud, sunset, storm, a night full of stars. The critical part is regrading the scene so its light matches the new sky.  
**Effect on the audience:** It changes the mood of the entire shot in one stroke. The same location becomes hope, threat or the end of the world depending on what you put above it.  
**Used for and where it works best:** Heritage documentary when you shot the site on a dead overcast day and need it epic. In advertising, travel and wedding films it is the standard rescue, and in drama it unifies shots filmed on different days under one sky.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Commercial / TVC, Travel / Real Estate / Hospitality, Wedding / Event Film, Feature Film, Drama Series Episode, Product Video / Motion Design | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Adventure, Romance, Disaster, Faith / Biblical Epic  
**Avoid when:** If you do not regrade the ground to the new sky the shot lies out loud: overcast land under a sunlit heaven. Watch shadow direction too, because a sunset on one side and shadows falling the other way exposes everything.  
**Prompt:** `dramatic replaced sky above the ruins, layered clouds catching low sun, ground light regraded to match the new sky direction`  
`cg.sky_replacement`

### Digital De-Aging

**Also called:** youthification, digital rejuvenation  
**What it is:** You modify the actor's face in CG and comp so he reads twenty or thirty years younger: skin tension, wrinkle reduction, reshaped bone and eye. Sometimes the whole face is rebuilt and tracked onto the original performance.  
**Effect on the audience:** It lets one actor carry an entire lifetime in the same film, so the viewer stays bound to that character across time. When it falls short the character turns subtly wrong and unsettling for no nameable reason.  
**Used for and where it works best:** Biopics, family sagas and crime epics that span decades, and the flashback you do not want to break by casting a second actor. In dramatised documentary it can present a real figure in his youth.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Docudrama / Reenactment, Trailer / Teaser, Commercial / TVC, 3D CG Animation | genres: Crime / Procedural, Gangster, Drama, Historical / Biopic, Sci-Fi, Superhero, Tragedy  
**Avoid when:** The face can get younger while the body and the movement still show the age: gait, weight, voice. Treat the whole scene, not only the face, or you get a young mask on an old body.  
**Prompt:** `the actor's face de-aged by about twenty five years, softer skin and tighter jawline, performance and lighting unchanged`  
**Example:** The Irishman (2019), which de-ages its leads across several decades.  
**Yields to:** `cg.face_replacement` — Gait, weight and body still read old.  
`cg.deaging`

### Crowd Simulation

**Also called:** digital crowd, agent-based crowd  
**What it is:** You generate thousands of figures, each with simple behaviour: walk, avoid the one in front, follow a goal, flee. The sum behaves like a real crowd without anyone animating each body by hand.  
**Effect on the audience:** It delivers scale and history. An army, a market, a pilgrimage or a battle becomes the measure of the event, showing how far it exceeds any single person.  
**Used for and where it works best:** Battles, ancient cities, stadiums and demonstrations. In heritage documentary it is the only practical way to show a Babylonian market or a new year procession, and in a trailer one crowd shot sells the scale of the film in two seconds.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Drama Series Episode, Trailer / Teaser, 3D CG Animation, Game Cinematic / Gameplay, Docudrama / Reenactment, Commercial / TVC | genres: War, Historical / Biopic, Heritage (civilisation-focused), Fantasy / Epic, Mythology / Ancient Epic, Disaster, Faith / Biblical Epic, Action  
**Avoid when:** A repeated crowd exposes itself: the same costume and the same walk lined up in a row. Vary wardrobe, height and speed, and let some figures stop or turn, because a real crowd never all moves one way.  
**Prompt:** `large simulated crowd filling the temple square, varied clothing and heights, individuals stopping and turning inside the flow`  
**Example:** The Lord of the Rings trilogy (2001 to 2003), whose armies were built with agent-based crowd software.  
`cg.crowd_sim`

### Fluid Simulation

**Also called:** water sim, liquid simulation, smoke and fire sim  
**What it is:** The motion of water, smoke or fire is computed physically from pressure, velocity and viscosity, and the wave, the splash and the vortex come out of that. The same solver drives fire, smoke and dust.  
**Effect on the audience:** Liquid is the hardest thing to fake because everyone knows how water behaves. When it is convincing, the whole shot inherits that credibility.  
**Used for and where it works best:** Floods, rivers and seas in epics and heritage documentary (the two rivers, the deluge), plus rain and storm. In food and beverage advertising it is the hero itself: the splash, the pour, the drop landing in milk.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Commercial / TVC, Product Video / Motion Design, 3D CG Animation, Trailer / Teaser, Game Cinematic / Gameplay, Documentary Feature | genres: Disaster, Mythology / Ancient Epic, Heritage (civilisation-focused), Faith / Biblical Epic, Adventure, Survival, Nature / Wildlife, Fantasy / Epic  
**Avoid when:** Get the scale wrong and the ocean becomes a sink: tiny droplets and fast motion betray the size. Smoke that does not interact with wind and objects also reads as a pasted layer.  
**Prompt:** `physically simulated river surge breaking against the embankment, heavy spray, correct scale so the water reads as a full sized river`  
**Example:** Moana (2016), whose ocean is a character built on water simulation.  
`cg.fluid_sim`

### Cloth Simulation

**Also called:** garment sim, fabric dynamics  
**What it is:** You give the garment material properties: weight, thickness, friction, how far it stretches. Motion, wind and the body then move the fabric on their own instead of being animated frame by frame.  
**Effect on the audience:** Fabric is what tells the eye the weight of a character and the speed of a move. A heavy robe grants gravity and authority; a light cloth in the wind grants speed and lightness.  
**Used for and where it works best:** Any character in loose clothing: the king in his robe, the priest in his mantle, the warrior's cloak as he runs. In heritage work it is what makes ancient dress read as woven cloth rather than a texture printed on the body.  
**Best in:** formats: 3D CG Animation, Feature Film, Heritage / Historical Documentary, Anime (Japanese 2D), Game Cinematic / Gameplay, Fashion Film, Commercial / TVC, Trailer / Teaser | genres: Historical / Biopic, Heritage (civilisation-focused), Fantasy / Epic, Mythology / Ancient Epic, Faith / Biblical Epic, Drama, Action, Samurai / Chanbara  
**Avoid when:** Fabric that penetrates the body or jitters at high frequency destroys the shot. Clothing that never moves at all makes the character look like a plastic figure.  
**Prompt:** `heavy woollen robe simulated with real weight, trailing behind him as he turns, wind catching the hem`  
`cg.cloth_sim`

### Hair and Fur Simulation

**Also called:** groom simulation, fur dynamics  
**What it is:** Hair is built as thousands of strands with length, softness and curl, then moved by physics with the head and the wind. Designing the shape is the groom; making it move is the simulation.  
**Effect on the audience:** After the eyes, hair is the first thing the eye reads on a face, so its movement decides whether a character feels alive. Fur is what gives an animal warmth, weight and reality.  
**Used for and where it works best:** Any 3D character with long hair, any furred animal, and every shot with wind, running or water. In kids content soft hair and fur read as instant warmth and pull the child toward the character.  
**Best in:** formats: 3D CG Animation, Kids Content, Feature Film, Game Cinematic / Gameplay, Anime (Japanese 2D), Commercial / TVC, Product Video / Motion Design, AI-Generated Clip | genres: Family, Preschool / Early Learning, Fantasy / Epic, Adventure, Nature / Wildlife, Fairy Tale, Drama  
**Avoid when:** Hair that never moves makes a corpse; hair that flies constantly puts the character in a permanent storm. Let it collide with shoulders and clothing, or it passes through them and gives itself away.  
**Prompt:** `long curly hair simulated strand by strand, moving with her turn and settling a beat after the head stops`  
**Example:** Brave (2012), built around a hair simulation system created for its lead character.  
`cg.hair_fur_sim`

### Motion Capture

**Also called:** mocap, performance recording  
**What it is:** You record a real human body with cameras or sensors and transfer the data onto a 3D character's skeleton. The result carries weight and micro detail that are hard to animate by hand.  
**Effect on the audience:** The motion becomes human at once: the small hesitation, the weight shift, the intake of breath before a line. The eye recognises human movement even when the body on screen is a monster.  
**Used for and where it works best:** Games, cinematics and realistic animation, and any fight or dance sequence. In heritage documentary it drives the craftsman, the scribe or the soldier so the figures move like people rather than puppets.  
**Best in:** formats: Game Cinematic / Gameplay, 3D CG Animation, Feature Film, Heritage / Historical Documentary, Drama Series Episode, Dance Film, Commercial / TVC, AI-Generated Clip | genres: Action, War, Historical / Biopic, Heritage (civilisation-focused), Sci-Fi, Martial Arts / Wuxia, Sports Drama, Fantasy / Epic  
**Avoid when:** Captured motion retargeted onto a body of different proportions goes wrong: a giant that walks like a man of average height. Adjust timing and scale, and keep it away from cartoon characters that need exaggeration.  
**Prompt:** `character animated from captured human motion, natural weight shifts and micro hesitations, grounded contact with the floor`  
**Yields to:** `anime.squash_stretch` — A cartoon character whose motion needs exaggeration.  
`cg.mocap`

### Performance Capture

**Also called:** facial performance capture, full performance capture  
**What it is:** Wider than motion capture: body, face, fingers and voice are recorded in the same take, so a complete acting performance transfers onto a built character. The actor plays the scene exactly as he would play any scene.  
**Effect on the audience:** A built character inherits a human soul: the look in the eye, the tremble of the lip, timing no one could reproduce. That is what lets an invented creature earn real sympathy.  
**Used for and where it works best:** The creature the audience must love or pity, and the non-human character who has to carry a dramatic scene. In realistic animation and large games it is how a face acts instead of merely moving.  
**Best in:** formats: Feature Film, 3D CG Animation, Game Cinematic / Gameplay, Drama Series Episode, Trailer / Teaser, 360 / VR, AI-Generated Clip | genres: Fantasy / Epic, Sci-Fi, Drama, Adventure, Monster / Kaiju, Tragedy, Superhero, Mythology / Ancient Epic  
**Avoid when:** If the eyes are not built properly the character reads dead no matter how good the performance was. And avoid it for a design too far from the actor's face, because the nuance does not survive the transfer.  
**Prompt:** `fully performance captured character, facial acting and eye line preserved from the actor, subtle expression changes on the close-up`  
**Example:** The Lord of the Rings: The Two Towers (2002), the first full performance captured lead character in a feature.  
**Yields to:** `cg.mocap` — Creature design sits too far from the actor's face.  
`cg.performance_capture`

### Rotoscoping

**Also called:** roto, hand-drawn matte  
**What it is:** You trace the outline of a subject by hand, frame after frame, to separate it from its background when there was no green screen. The result is an animated matte you can work against in comp.  
**Effect on the audience:** It gives total control over any shot filmed on a street with no preparation. It is the silent labour nobody ever sees when it is done right.  
**Used for and where it works best:** Grading a person separately, removing something behind them, placing an element between them and the background, or fixing a failed track. In heritage documentary it separates a presenter from the site so you can build behind him.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Commercial / TVC, Music Video, Video Essay, AI-Generated Clip | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Action, Thriller / Suspense, Science / Educational, True Crime  
**Avoid when:** The time cost is brutal, so do not commit to a long roto shot if a green screen could have covered it. Soft edges such as hair and haze are never solved by hand tracing alone.  
**Prompt:** `subject isolated from the background with a hand traced matte, clean edges, background replaced behind him`  
`cg.roto`

### Screen Replacement

**Also called:** screen comp, phone screen insert, UI replacement  
**What it is:** You shoot the phone or monitor blank or with tracking markers, then comp the real content onto it afterwards with reflection, glow and the shadow of a finger.  
**Effect on the audience:** It gives you control over the most important information in the scene without a reshoot. The viewer reads the screen easily because it was designed to be read, not to bounce studio light back.  
**Used for and where it works best:** Any scene with a message, a call or an app, and commercials whose screen content changes by market or version. In corporate video it updates an interface without reshooting anything.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Corporate / Training, Drama Series Episode, Feature Film, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama | genres: Drama, Comedy, Thriller / Suspense, Crime / Procedural, Romance, Sci-Fi, Mystery / Whodunit  
**Avoid when:** With no reflection, no glow and no finger shadow the screen looks like a paper sticker. Watch the brightness too: a screen brighter than the whole scene pulls the eye and wrecks the composition.  
**Prompt:** `phone screen replaced with clean readable content, soft reflection of the room on the glass, slight glow on the fingers`  
`cg.screen_replacement`

### Invisible VFX

**Also called:** hidden effects, seamless VFX  
**What it is:** Effects the audience is never meant to notice: erasing a modern building, adding breath in cold air, fixing the weather, changing how many people are present, or splicing the best performance from two takes.  
**Effect on the audience:** They serve the story silently. The viewer stays inside the scene and never thinks about technique, which is the highest level of the craft rather than the lowest.  
**Used for and where it works best:** Drama, documentary and period film use them more than science fiction does. In heritage documentary most of your work is exactly this: clearing the modern century out of the frame so the period stays honest.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Documentary Feature, Docudrama / Reenactment, Limited Series, Commercial / TVC, Interview / Video Podcast | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Crime / Procedural, True Crime, War, Verite / Observational  
**Avoid when:** Do not fix what is not broken; every intervention costs time and can soften the image. The rule is simple: the moment the viewer notices it, it is no longer invisible.  
**Prompt:** `clean modern elements removed from the historic street, period accurate frame, no visible retouching`  
**Example:** Forrest Gump (1994), whose invisible work includes removing an actor's legs in plain sight.  
`cg.invisible_vfx`

### HDRI Lighting / Image-Based Lighting

**Also called:** IBL, environment lighting, HDRI dome  
**What it is:** You capture a spherical high dynamic range image of the real location and use it as the light source for the 3D scene. Every reflection, colour and shadow then comes from the same light that was on set.  
**Effect on the audience:** Integration becomes almost automatic, because the added element is lit by the same sky and the same walls. The eye believes it since the reflections describe a place that actually exists.  
**Used for and where it works best:** Any CG element inside a live-action plate: a car, a statue, a creature, a product. In heritage work, capture the environment inside the real site and light the reconstructed piece with it so it feels genuinely present.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, 3D CG Animation, Heritage / Historical Documentary, Feature Film, Drama Series Episode, Corporate / Training, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, Sci-Fi, Drama, Action, Science / Educational, Fantasy / Epic  
**Avoid when:** An HDRI alone gives soft directionless light, so add a key when you want a hard shadow and drama. And if it was captured at a different hour than the plate, every reflection lies.  
**Prompt:** `CG element lit by the captured environment of the location, real sky reflections and matching shadow direction`  
`cg.hdri_ibl`

### Subsurface Scattering for Skin

**Also called:** SSS, skin shader, translucency  
**What it is:** Skin does not stop light at its surface; light enters, scatters inside and leaves slightly red. The shader computes that scattering, so a face gains fleshy depth instead of reading as plastic.  
**Effect on the audience:** It is the difference between a living face and a doll. The eye recognises flesh from that faint glow in the ear, the nose and the fingers when light passes through them.  
**Used for and where it works best:** Every close-up on a 3D character, and any material with flesh, wax, marble or milk in it. In kids content it is what makes a character read as warm, soft and huggable.  
**Best in:** formats: 3D CG Animation, Kids Content, Feature Film, Game Cinematic / Gameplay, Commercial / TVC, Product Video / Motion Design, Anime (Japanese 2D), AI-Generated Clip | genres: Family, Preschool / Early Learning, Drama, Fantasy / Epic, Horror, Sci-Fi, Fairy Tale  
**Avoid when:** Overdone, the face glows like a candle lit from inside, especially in backlight. On a strongly stylised character, that realism can also break the design.  
**Prompt:** `realistic skin shading with light scattering through the ears and fingers in backlight, soft fleshy warmth, no plastic sheen`  
**Yields to:** `cg.npr_toon` — A strongly stylised character, where flesh realism breaks the design.  
`cg.sss_skin`

### Simulated Lens Artifacts

**Also called:** lens imperfection pass, flare and aberration, gate weave  
**What it is:** You add the flaws of a real lens to a clean render: flare, chromatic fringing at the edges, vignette, distortion, a little gate weave and grain. All of it is what a real camera does without meaning to.  
**Effect on the audience:** The flaws are what persuade the eye that a person photographed this with a physical device. Total cleanliness feels manufactured and cold.  
**Used for and where it works best:** Any 3D shot cut against live action, and any animation chasing a filmic feel. Keep it restrained in premium advertising, and push flare and distortion in horror and sci-fi where an older, harsher lens sells the world.  
**Best in:** formats: 3D CG Animation, Feature Film, Commercial / TVC, Trailer / Teaser, Game Cinematic / Gameplay, Anime (Japanese 2D), Music Video, AI-Generated Clip | genres: Sci-Fi, Horror, Action, Drama, Historical / Biopic, Heritage (civilisation-focused), Fantasy / Epic  
**Avoid when:** Flare in every shot becomes a cheap trend that buries the image. And artifacts never rescue weak lighting: if the base is flat, grain will not save it.  
**Prompt:** `subtle lens imperfections on the render, faint chromatic fringing at the edges, gentle vignette, fine film grain, one soft flare`  
`cg.lens_artifacts`

### Photoreal Render

**Also called:** photorealistic CG, physically based rendering  
**What it is:** The render aims to sit next to a live-action plate and go unnoticed: physically based light, materials with correct roughness and reflectance, and a camera with real specifications. Everything is computed the way the world behaves.  
**Effect on the audience:** The image inherits the authority of a photograph. The viewer believes the thing exists, and that changes how he receives the information: it stops being an illustration and becomes testimony.  
**Used for and where it works best:** A creature inside a live-action film, a product film, and site reconstruction in heritage documentary when the viewer must believe the temple really stood like that. In advertising it sells, because the eye treats the image as evidence.  
**Best in:** formats: Feature Film, Commercial / TVC, Product Video / Motion Design, Heritage / Historical Documentary, 3D CG Animation, Drama Series Episode, Documentary Feature, Corporate / Training | genres: Heritage (civilisation-focused), Historical / Biopic, Sci-Fi, Action, Science / Educational, Nature / Wildlife, Drama, Fantasy / Epic  
**Avoid when:** Failed realism is worse than committed stylisation: something reaching for real and missing becomes uncomfortable to look at. When budget or time will not carry it, choose a clear style from the start.  
**Prompt:** `physically based render, materials with accurate roughness and reflections, the camera body and focal length stated as for a real shoot, natural light, indistinguishable from a photograph`  
**Example:** Jurassic Park (1993), whose CG dinosaurs set the modern standard for photoreal creatures.  
**Yields to:** `cg.npr_toon` — Budget or time will not carry believable realism.  
`cg.photoreal_render`

### Non-Photorealistic Render / Toon Render

**Also called:** NPR, stylised render, illustrative rendering  
**What it is:** The render imitates drawing rather than photography: outlines, banded shading, ink, flat colour, paper or canvas texture. The form is 3D while the presentation is illustration.  
**Effect on the audience:** It frees the image from comparison with reality, so the eye judges it as art rather than as a failed copy. It also gives an identity you remember from a single frame.  
**Used for and where it works best:** Independent animation, kids content, games and music videos, and any project whose budget cannot carry full realism. In documentary it serves the parts you have no footage for, quietly telling the viewer this is an interpretation and not a record.  
**Best in:** formats: 3D CG Animation, Kids Content, 2D Animation (Western / Cartoon), Game Cinematic / Gameplay, Music Video, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: Family, Preschool / Early Learning, Fantasy / Epic, Fairy Tale, Comedy, Adventure, Surreal / Absurdist, Science / Educational  
**Avoid when:** The style has to be a full decision, not a filter dropped over a realistic scene, or it lands half way between the two. Watch outlines on complex shapes as well, where they turn into noise and destroy readability.  
**Prompt:** `non photorealistic render, clean ink outlines, flat banded shading, illustrated look with paper texture`  
`cg.npr_toon`

### Cel-Shaded 3D

**Also called:** toon shading, anime shading on 3D, 2.5D, cel look CG  
**What it is:** A specific case of NPR: lighting collapses into two or three flat bands (light, shadow, deep shadow) with no gradient, exactly as anime was painted on cels. Lines are drawn around the silhouette and around the interior detail.  
**Effect on the audience:** A three dimensional form can move freely while still reading as hand drawn. That makes 3D action possible inside anime language without losing the identity of the drawing.  
**Used for and where it works best:** Modern anime mixing 2D and 3D, plus mecha, cars, ships and crowds that are impractical to draw by hand, fighting games and youth music videos. Step the frame rate down to twos so the seam between the drawn character and the generated machine disappears, and in kids content it delivers bold, clear colour that reads on any screen size.  
**Best in:** formats: Anime (Japanese 2D), 3D CG Animation, Drama Series Episode, Feature Film, Game Cinematic / Gameplay, Kids Content, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, AI-Generated Clip | genres: Shonen Battle (anime), Mecha (anime), Isekai (anime), Magical Girl (anime), Action, Fantasy / Epic, Family, Comedy, Sci-Fi, Sports Anime, Superhero  
**Avoid when:** Leaving realistic lighting running underneath cel shading makes the image contradict itself. Line weight also has to read consistently on screen - which means scaling it with distance, as `anime.toon_shading` does - and leaving the CG on ones inside a scene of characters on twos exposes the seam instantly and breaks the world.  
**Prompt:** `cel shaded 3D character, two tone flat shading with a hard shadow edge, clean outline scaled with distance so it reads consistently, anime colour palette`  
`cg.cel_shaded_3d`

### The Painterly 3D Look

**Also called:** Arcane look, hand-painted texture over CG  
**What it is:** Characters and environments are built in 3D, but every texture is hand painted with visible brushwork, and further painted passes are added after the render. The final image reads as a moving painting.  
**Effect on the audience:** It combines the consistency of 3D, where the face holds from every angle, with the warmth of hand painting. The viewer senses that someone laboured over every frame, which reads as high value.  
**Used for and where it works best:** Mature fantasy and drama series, premium title sequences, and any music video that wants to read as art rather than product. In heritage work it can be the smart choice, evoking manuscript and wall painting instead of chasing photographic imitation.  
**Best in:** formats: 3D CG Animation, Drama Series Episode, Title Sequence / Opening Credits, Music Video, Trailer / Teaser, Anime (Japanese 2D), Heritage / Historical Documentary, Short Film | genres: Fantasy / Epic, Drama, Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, Cyberpunk, Tragedy, Psychological / Arthouse  
**Avoid when:** It is expensive in hours and in hand skill, so do not commit without painters and time. Too much painted detail on close-ups can also dissolve the features once the character moves fast.  
**Prompt:** `painterly 3D look, hand painted textures with visible brush strokes, soft painted light, moving illustration feel`  
**Example:** Arcane (2021), built on 3D with hand painted texture and post paint work.  
**Yields to:** `cg.npr_toon` — No painters and no hours for hand-painted texture.  
`cg.arcane_painterly`

### The Real-Time Engine Cinematic Look

**Also called:** Unreal Engine cinematic, real-time rendered film look  
**What it is:** The shot is produced inside an engine that renders in real time instead of the slow traditional path. You see the light, the camera and the near final image while you work, and you export quickly.  
**Effect on the audience:** It changes how decisions get made: you try ten lighting setups in an hour instead of waiting a night per render. The image has its own signature too, rich light, live reflections, and sometimes an excess of cleanliness.  
**Used for and where it works best:** The small team that needs a large shot count in a short time: a heritage series, game cinematics, a commercial, an explainer. It is also the engine behind LED volume virtual production.  
**Best in:** formats: Game Cinematic / Gameplay, 3D CG Animation, Heritage / Historical Documentary, Commercial / TVC, Trailer / Teaser, Corporate / Training, Explainer, Drama Series Episode | genres: Sci-Fi, Fantasy / Epic, Heritage (civilisation-focused), Historical / Biopic, Action, Adventure, Science / Educational, Cyberpunk  
**Avoid when:** Excess cleanliness and stock global lighting make everything look the same. Add lens imperfection, atmosphere and real shadow to break the out-of-the-box signature.  
**Prompt:** `real-time engine render, rich dynamic lighting and live reflections, filmic grade with added grain and lens imperfection`  
`cg.unreal_cinematic`

### Simulated Stop Motion in 3D

**Also called:** fake stop motion, CG claymation look  
**What it is:** You make 3D look handmade: clay, felt and fingerprint textures, motion stepped on twos, and a shallow depth of field like a camera close to a small set. Sometimes a tiny wobble is added to a character that should be still.  
**Effect on the audience:** It carries the warmth of a toy and of handwork, and makes the world feel small, friendly and made with love. Children attach to it because it resembles their own toys.  
**Used for and where it works best:** Kids content, family commercials and holiday films, and any story you want to feel like an old tale. In music videos it delivers strong nostalgic identity without the cost of real stop motion.  
**Best in:** formats: Kids Content, Commercial / TVC, 3D CG Animation, Stop Motion, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Explainer | genres: Family, Preschool / Early Learning, Fairy Tale, Comedy, Fantasy / Epic, Slice of Life, Adventure  
**Avoid when:** Keep the motion fully smooth and the illusion dies instantly. Everything in the world also has to be made of a material, a fabric sky and gelatin water, because a photoreal sky above a clay character breaks the rule the shot is built on; the exception is a story about a handmade figure inside a real world.  
**Prompt:** `3D animated to look like stop motion, clay and felt materials with visible fingerprints, animation on twos, tiny handmade set with shallow focus`  
**Example:** The Lego Movie (2014), CG built to imitate brick built stop motion.  
`cg.clay_stopmo_sim`

### Low-Poly Retro Look

**Also called:** low poly, retro 3D, PS1 aesthetic  
**What it is:** You deliberately reduce polygon count and resolution: faceted shapes with visible edges, tiny pixelated textures, and sometimes the vertex jitter of nineties hardware. The form becomes a symbol rather than a copy.  
**Effect on the audience:** Instant nostalgia for a whole generation, and the feel of an old game or a degraded digital memory. It also gives strong silhouette clarity, precisely because there is so little detail.  
**Used for and where it works best:** Music videos, indie games and comedy content, and any story about the internet, memory or the nineties. It also works for fast explainers because it is light, clear and quick to produce.  
**Best in:** formats: Music Video, Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, Explainer, 3D CG Animation, Title Sequence / Opening Credits, Experimental / Art Film | genres: Comedy, Surreal / Absurdist, Cyberpunk, Sci-Fi, Coming of Age, Horror, Dark Comedy / Satire  
**Avoid when:** If the story needs emotion in a close-up, the style cannot deliver it because the features are not there. Do not mix it with high realism in the same frame unless the clash is the point.  
**Prompt:** `low poly retro 3D, faceted geometry with hard edges, small pixelated textures, slight vertex jitter, nineties game aesthetic`  
**Yields to:** `cg.npr_toon` — The story needs facial emotion in close-up.  
`cg.low_poly_retro`

### Voxel Art

**Also called:** voxel, cube-based 3D  
**What it is:** The entire world is built from small cubes instead of free polygons, the way you build with blocks. Everything, a character, a tree, water, is made of the same unit.  
**Effect on the audience:** It creates an orderly, friendly world that feels like building with blocks and suggests construction and assembly. Children grasp its rules instantly because they already play by them.  
**Used for and where it works best:** Kids content, games and simple explainers, and any idea about building, layers or units. In heritage work it can show how a ziggurat rose level by level in a form a child understands.  
**Best in:** formats: Kids Content, Game Cinematic / Gameplay, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, Music Video, Meme / Comedy Edit, AI-Generated Clip | genres: Preschool / Early Learning, Family, Comedy, Adventure, Science / Educational, Fantasy / Epic, Heritage (civilisation-focused)  
**Avoid when:** Fine detail is impossible here, so do not choose it for a story that depends on facial expression. Raise the cube count too far and you lose the simplicity that was the reason to pick it.  
**Prompt:** `voxel art style, whole scene built from small cubes, clean bright colours, playful block world`  
**Yields to:** `cg.npr_toon` — The story depends on facial expression.  
`cg.voxel`

### Isometric Diorama

**Also called:** isometric view, diorama shot, axonometric  
**What it is:** The camera sits at a fixed high angle with perspective removed, so parallel lines stay parallel instead of converging. The place reads as a small open diorama seen from above.  
**Effect on the audience:** It delivers order and control: the whole place is legible at a glance and its relationships are clear. It also feels like a toy, because it resembles a doll's house.  
**Used for and where it works best:** Explaining how a place or a system works: a house, a factory, a city, the steps of a process. In heritage documentary it is excellent for showing a city or temple plan, and in kids content it makes the world feel like a safe toy.  
**Best in:** formats: Explainer, Kids Content, Game Cinematic / Gameplay, Corporate / Training, Heritage / Historical Documentary, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation | genres: Science / Educational, Preschool / Early Learning, Family, Heritage (civilisation-focused), Historical / Biopic, Comedy, Adventure  
**Avoid when:** With a fixed distant camera, intimate emotion does not land. Avoid it for a scene that needs tension as well, since total visibility removes any fear of the unknown.  
**Prompt:** `isometric diorama view, parallel projection with no perspective convergence, small detailed world seen from a fixed high angle`  
**Example:** Monument Valley (2014), a game built entirely on isometric construction.  
**Yields to:** `size.cu` — The scene needs intimate emotion or tension.  
`cg.isometric_diorama`

### The Glitch Aesthetic in 3D

**Also called:** datamosh look, corrupted mesh, digital artifact style  
**What it is:** Computer errors are used as a style: geometry stretching to infinity, textures dropping out, colour channels separating, the form breaking into triangles and rebuilding. You author them deliberately rather than leaving them to chance.  
**Effect on the audience:** It conveys collapse, intrusion and loss of control, or the idea that the world itself is software that can break. It creates anxiety without showing any violence.  
**Used for and where it works best:** Cyberpunk, psychological horror and music video, and the beat where a character breaks or an illusion is exposed. In a trailer place it on the final audio hit, and in vertical short-form it works as a hard hook.  
**Best in:** formats: Music Video, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Game Cinematic / Gameplay, 3D CG Animation, Experimental / Art Film, AI-Generated Clip | genres: Cyberpunk, Sci-Fi, Psychological Horror, Horror, Dystopia / Post-Apocalyptic, Surreal / Absurdist, Thriller / Suspense  
**Avoid when:** With no narrative reason behind it, the glitch becomes teenage decoration. Do not stretch it either: a second or two lands, and anything longer tires the eye and dilutes the meaning.  
**Prompt:** `controlled digital glitch on the 3D render, mesh tearing into stretched triangles, texture dropouts and channel separation for a few frames`  
`cg.glitch_3d`

### Hologram and UI Overlay

**Also called:** HUD graphics, holographic display, motion graphics overlay  
**What it is:** Graphic elements, dimensional or flat, added over or inside the scene: a map hanging in the air, data around a face, markers tracking a moving object. They are built in CG and motion graphics and locked to the camera move.  
**Effect on the audience:** It signals advanced technology and control, and turns information into part of the world rather than text laid on top of it. It also lets the viewer read and watch in the same instant.  
**Used for and where it works best:** Sci-fi, action and investigation work, technology product films and corporate explainers. In heritage documentary use it quietly: site names or building dimensions appearing in space beside the reconstruction.  
**Best in:** formats: Feature Film, Commercial / TVC, Product Video / Motion Design, Explainer, Corporate / Training, Game Cinematic / Gameplay, Drama Series Episode, Heritage / Historical Documentary | genres: Sci-Fi, Action, Cyberpunk, Spy / Espionage, Crime / Procedural, Science / Educational, Thriller / Suspense, Heritage (civilisation-focused)  
**Avoid when:** An interface that cannot be read in two seconds serves nothing. Crowds of transparent blue elements are also a cliche: cut the count and make every element carry information the story needs.  
**Prompt:** `holographic interface floating in the air beside him, clean readable graphics locked in 3D space, soft glow and thin scan lines`  
**Example:** Iron Man (2008), whose holographic workshop interface defined the modern look.  
`cg.hologram_ui`

### X-Ray and Inside-the-Body Shot

**Also called:** see-through render, anatomical camera, medical visualisation  
**What it is:** The surface turns transparent and reveals what lies inside: bone, muscle, vessels, or the interior of a machine. Sometimes the camera keeps going, enters and travels the passage itself.  
**Effect on the audience:** It delivers the feeling of complete knowledge: we now see what cannot be seen. In horror the same device creates dread, because the body is exposed without consent.  
**Used for and where it works best:** Medical and science explainers, educational kids content, and sports or pharmaceutical product films. In medical drama it is the shot that moves from dialogue to what is actually happening inside the patient.  
**Best in:** formats: Explainer, Kids Content, Documentary Feature, Commercial / TVC, Product Video / Motion Design, Corporate / Training, Drama Series Episode, 3D CG Animation | genres: Science / Educational, Medical Drama, Family, Preschool / Early Learning, Sci-Fi, Horror, Body Horror, Drama  
**Avoid when:** Excess anatomical detail buries the message: keep the relevant layer bright and let the rest of the body fall back. In kids content keep it far from blood and fear.  
**Prompt:** `the skin turns transparent revealing the bone and muscle beneath, clean anatomical render with the key layer highlighted`  
`cg.xray_body`

### Assembly Build-Up

**Also called:** build-on animation, construction reveal  
**What it is:** The object builds itself on screen piece by piece: foundation, walls, roof, detail, colour. It is the reverse of the exploded view, which separates, while this one gathers in chronological or logical order.  
**Effect on the audience:** It delivers achievement and comprehension together. The eye follows the order of construction and remembers it, and the completion gives a small satisfaction because something finished in front of us.  
**Used for and where it works best:** Heritage documentary explaining how a temple, a wall or a canal was raised across centuries. Also industrial, architectural and advertising work presenting a product assembling from its parts.  
**Best in:** formats: Heritage / Historical Documentary, Explainer, Corporate / Training, Product Video / Motion Design, Documentary Feature, Commercial / TVC, Title Sequence / Opening Credits, 3D CG Animation | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Mythology / Ancient Epic, Adventure, Faith / Biblical Epic  
**Avoid when:** A build with no sound and no weight is a cold diagram: let the pieces land with mass and dust. Do not build everything at one speed either; small detail should arrive faster than the large masses.  
**Prompt:** `the temple builds itself course by course, stone blocks settling into place with dust, detail and colour arriving last`  
`cg.assembly_build_up`

### Simulated Anamorphic Lens

**Also called:** anamorphic look in CG, oval bokeh, blue streak flare  
**What it is:** The render imitates anamorphic behaviour: oval bokeh, a horizontal blue streak flare, edge distortion, and a depth that feels wider than the focal length suggests. The image lands in a wide ratio with an instantly recognisable film signature.  
**Effect on the audience:** The eye connects that signature to big cinema at once, so the scene inherits weight and budget without adding anything to the story.  
**Used for and where it works best:** Trailers, premium advertising and cinematics, plus any CG shot that must cut against footage actually captured on anamorphic glass. In heritage work it gives the epic shot the character of a feature film.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, 3D CG Animation, Feature Film, Music Video, Game Cinematic / Gameplay, Product Video / Motion Design, AI-Generated Clip | genres: Sci-Fi, Action, Drama, Historical / Biopic, Heritage (civilisation-focused), Western, Thriller / Suspense, Fantasy / Epic  
**Avoid when:** A blue streak in every shot is a tired cliche. And if the rest of the film was shot on spherical glass, one anamorphic looking CG shot announces itself as synthetic.  
**Prompt:** `anamorphic lens simulation, oval bokeh, horizontal blue streak flare, slight edge distortion, wide anamorphic aspect framing`  
**Yields to:** `lens.spherical` — The rest of the film was shot spherical.  
`cg.anamorphic_sim`

### Digital Face Replacement

**Also called:** head replacement, face swap in VFX  
**What it is:** You take the body of a double or a stunt performer and place the lead actor's face onto it in CG and comp, matching light and head motion. It is sometimes used for a face that no longer exists to be filmed.  
**Effect on the audience:** It keeps a dangerous shot personal, because the viewer sees his hero inside the danger. When it misses, the face reads as a mask and the scene breaks.  
**Used for and where it works best:** Stunt and fight coverage, and scenes that need actors who were never on set at the same time. In historical biography it can present a real figure with a familiar face.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Commercial / TVC, 3D CG Animation, Docudrama / Reenactment, Game Cinematic / Gameplay, AI-Generated Clip | genres: Action, War, Historical / Biopic, Crime / Procedural, Superhero, Thriller / Suspense, Spy / Espionage, Drama  
**Avoid when:** A mismatch in head shape between the double and the actor ruins it no matter how good the face is. Avoid it in a long quiet shot as well, where the eye studies the face and catches every flaw.  
**Prompt:** `the stunt performer's head replaced with the lead actor's face, lighting and head motion matched exactly, no mask edge`  
**Example:** Rogue One: A Star Wars Story (2016), which rebuilt a lead face digitally onto a performer.  
`cg.face_replacement`
