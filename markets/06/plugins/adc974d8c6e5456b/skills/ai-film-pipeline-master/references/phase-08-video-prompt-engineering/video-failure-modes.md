# Failure Modes and Rescues

8 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Style Bleed From a Reference

**Also called:** unwanted transfer, reference contamination  
**What it is:** A reference supplied for one attribute contributes others as well: its lighting arrives with the face, its background arrives with the garment, its palette arrives with everything.  
**Effect on the audience:** A composite that does not sit in its own scene. The subject looks lit by a different room than the one it stands in.  
**Used for and where it works best:** Every multi-reference generation, and the usual explanation when a carefully described scene comes back looking like the reference photograph. Best in keyframe plates and character work.  
**Best in:** formats: General Reference Plate, Generated Keyframe Feeding Video, Character Sheet / Turnaround, Poster / Static Design, Product Still / Packshot, Editorial / Magazine Image, Comics / Webtoon / Photo Essay, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually cannot be fixed by weakening the reference, which costs the attribute that was wanted. The exception is an explicit negative role statement naming what must not transfer, which is the designed remedy.  
**Prompt:** `reference A supplies the face only: do not take its lighting, its background, its colour cast or its crop`  
**Yields to:** `ai.negative_guards` — State explicitly what must not transfer.  
`rescue.style_bleed`

---

### Pattern and Repetition Breakdown

**Also called:** tiling failure, ornament collapse  
**What it is:** Repeating decorative elements, tiles, brickwork, embroidery, columns and relief bands, lose their rhythm and become irregular noise across the frame.  
**Effect on the audience:** Architecture and textile that looked researched become decorative approximation, which is the fastest way a heritage image loses authority.  
**Used for and where it works best:** Heritage reconstruction with ornament, textile and carpet work, architectural facades, and any repeated motif. Best in heritage documentary and location plates.  
**Best in:** formats: Location Sheet / Master Plate, Heritage / Historical Documentary, Generated Keyframe Feeding Video, General Reference Plate, Product Still / Packshot, Editorial / Magazine Image, Poster / Static Design, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, Drama  
**Avoid when:** It usually worsens when the pattern is described in more detail, because the model spreads detail instead of enforcing rhythm. The remedy that keeps the ornament is generating an accurate tile separately and repeating it in a design tool, or taking the shot to an engine that holds repetition; keeping the pattern small in frame or letting shadow cover most of it is for a shot whose design already wants it there, never a way of emptying the frame for the engine's sake, as `rescue.faces_in_crowd` puts it.  
**Prompt:** `the relief band runs along the upper wall in the shadow the scene's own light already casts, its rhythm suggested rather than resolved; the detailed panel will be generated separately`  
`rescue.pattern_breakdown`

---

### Impossible Pose and Joint Failure

**Also called:** broken anatomy, twisted limbs  
**What it is:** Limbs bend where they cannot, torsos twist beyond human range, or a figure carries weight on a leg that is not under it.  
**Effect on the audience:** The body reads as wrong even when the viewer cannot name the fault, because everyone knows human movement without being able to describe it.  
**Used for and where it works best:** Any figure in an active or unusual pose, dance, combat, climbing, carrying. Best in character sheets and keyframe plates.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Poster / Static Design, Heritage / Historical Documentary, Music Video, Editorial / Magazine Image, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually persists when the pose is described in adjectives rather than in mechanics. The exceptions are naming the weight-bearing foot and the direction each joint bends, or supplying a pose reference and letting it carry the mechanics.  
**Prompt:** `the weight is entirely on the left foot, the right heel lifted, the torso rotated no more than forty-five degrees from the hips, the right arm raised with the elbow bending backward`  
**Yields to:** `pose.weight_shift` — Name the weight-bearing foot.  
`rescue.pose_impossible`

---

### Late Instructions Dropped

**Also called:** positional decay, tail truncation  
**What it is:** Instructions placed late in a long prompt are followed weakly or not at all, while the opening of the prompt is obeyed closely.  
**Effect on the audience:** A careful requirement silently disappears, and the loss is invisible because the image looks fine. Only a comparison against the brief reveals it.  
**Used for and where it works best:** Every long prompt, and the usual explanation when a specific requirement never appears in any generation. Best across all still work.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Character Sheet / Turnaround, General Reference Plate, Product Still / Packshot, Editorial / Magazine Image, Thumbnail / Social Card, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually gets treated as a length problem and answered by cutting the prompt, which loses the shot instead of the risk. The exception is reordering so that identity and the protected requirements come first and the disposable description comes last.  
**Prompt:** `identity lock first, then the protected requirements, then the scene, then the finish; nothing important placed after the halfway point`  
**Yields to:** `ai.prompt_anatomy` — Reorder the prompt rather than cutting it.  
`rescue.prompt_length_collapse`

---

### Temporal Geometric Morphing

**Also called:** object morphing, topological shifting, shape instability  
**What it is:** The camera or subject moves and solid geometry transforms into a different object (e.g. a chariot wheel warping into a shield, an architectural arch bending into an organic curve). Occurs on wide camera displacement across ambiguous geometry interpolated between frames. The arc at which a given engine starts to morph is a measured, dated value per engine — check it at project start rather than carrying a number.  
**Effect on the audience:** Destroys physical immersion instantly; the scene reads as a surreal AI hallucination rather than a solid cinematic world.  
**Used for and where it works best:** High-motion action shots, rapid panning across complex geometry, and rotating subject views across all video generation engines.  
**Best in:** formats: all | genres: all  
**Avoid when:** This failure appears on wide rotational moves across ambiguous geometry. The remedy is conditioning, not a smaller move. Lock the move with start-and-end frames, name the rigid geometry explicitly, describe the arc as one continuous trajectory with a stated start and end bearing, and where the move is large, split it across joined clips at the verified clip length. On current engines a wide orbit is routine; an engine that cannot hold the arc is an engine-selection note, never a reason to shorten the move or straighten it into a linear vector.  
**Prompt:** `rigid physical geometry, invariant solid structure, perfectly constant architecture and objects throughout motion, zero topological deformation`  
**Yields to:** `ai.first_last_frame` — Wide rotational move across ambiguous geometry.  
`fail.morphing`

---

### Limb Drift and Phantom Duplication

**Also called:** extra limbs, floating hands, anatomical cloning under motion  
**What it is:** Characters in motion generate third arms, split fingers, or duplicate legs during walking cycles or weapon handling, especially when limbs cross in front of the torso.  
**Effect on the audience:** Severe uncanny valley shock; breaks emotional connection with the character and ruins narrative drama.  
**Used for and where it works best:** Character performance shots, walking cycles, fight choreography, sword draws, and hand gestures.  
**Best in:** formats: all | genres: all  
**Avoid when:** Avoid loose poses in the starting keyframe where fingers or hands are partially occluded or blurred. Enforce clenched fists, resting hands, or clear physical contact with objects, and direct limb vectors along clear physical planes.  
**Prompt:** `anatomically locked skeleton, exactly two arms and two legs, constant hand count with five fingers per hand, stable joints with zero phantom limb duplication`  
**Yields to:** `kf.contact_points` — Limbs crossing the torso from a loose keyframe.  
`fail.limb_drift`

---

### High-Frequency Camera Jitter and Temporal Flicker

**Also called:** frame flicker, lighting strobing, micro-jitter  
**What it is:** High-frequency luminance strobing across frame boundaries, micro-vibrations in camera trajectories, or rapid texture boiling on fine patterns (chainmail, leaves, sand, water).  
**Effect on the audience:** Visual fatigue and headache; signals cheap generative synthesis rather than stable cinema camera stabilization.  
**Used for and where it works best:** Shots with intricate high-frequency textures, firelight, water reflections, and handheld camera simulations.  
**Best in:** formats: all | genres: all  
**Avoid when:** Avoid unspecified camera mounts or noisy prompts containing buzzwords. Mandate rigid dolly tracking, fluid-head tripod locks, or calibrated 3-axis Steadicam motion, and **hold the frame rate the piece was designed in rather than changing it here** — this line used to mandate a locked 24fps, which is the rate that strobes worst on a fast horizontal move and is not enough for sports or live broadcast at all (`look.fps_24` says both). The rate is a delivery decision owned by the `look.fps_*` cards; the jitter is fixed in the mount and the move.  
**Prompt:** `smooth steady camera tracking on rigid hydraulic dolly tracks, temporal luminance stability, zero frame flicker, zero micro-jitter, cinema shutter cadence`  
**Source:** reference — standard camera-support practice; the figures named are the rigs', not a threshold of ours  
**Yields to:** `look.fps_24` — The frame-rate decision, owned by the look.fps_* cards.  
`fail.flicker_jitter`

---

### Geometric Melting and Structural Dissolution

**Also called:** edge melting, background liquefaction, substance dissolution  
**What it is:** Solid background surfaces (stone walls, fortress gates, tables, terrain) lose edge definition and liquefy or melt into liquid mud or smoke as the subject moves across them.  
**Effect on the audience:** The physical environment feels like watercolor paint washing away, destroying the weight and historical permanence of the setting.  
**Used for and where it works best:** Tracking shots past foreground pillars, subjects running past fortress walls, and heavy atmospheric scenes (smoke, fog, dust).  
**Best in:** formats: all | genres: all  
**Avoid when:** Avoid weak contrast between foreground subject and background environment. Explicitly separate subject motion vectors from stationary background geometry in the prompt hierarchy.  
**Prompt:** `rock-solid architectural boundaries, sharp immutable stone masonry, immovable background geometry, zero edge melting, zero background dissolution`  
**Yields to:** `color.contrast_separation` — Weak foreground-to-background separation under a tracking move.  
`fail.geometric_melting`
