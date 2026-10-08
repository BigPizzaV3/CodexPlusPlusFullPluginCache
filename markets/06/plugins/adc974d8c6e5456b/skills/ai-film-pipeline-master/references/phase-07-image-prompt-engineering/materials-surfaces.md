# Materials and Surface Physics

16 cards. Also in the other stage: a shot has a frame too. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name the Distance Before the Substance

**Also called:** the materials selector, distance before substance, how close will this be seen  
**What it is:** The card at the head of the `material.` shelf. It does not describe a surface. It asks the three questions this shelf asks of itself over and over — **how close will this be read, does the surface appear on its own or only under a light chosen for it, and are you naming the substance or proving it** — and hands back a named shortlist for each answer. The axes were read off the shelf's own escape conditions and off the boundary clause every card carries; they were not invented. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so the surface that does reach the screen was described at the distance it will be read, under a light that reveals it, and once — rather than every surface in the frame being described at equal detail, which is what this shelf spends most of its boundary clauses warning against.  
**Used for and where it works best:** Answer the three questions **out loud, in order, in one sentence each, before a word of surface description is written**. The first eliminates two thirds of the shelf. The third is not optional and it is not a fork between equals: whatever the first two return, at least one card from the third axis' second value has to come with it, because a described surface that the frame never proves was a wasted sentence. **Then spend the description budget on one surface** — the commonest failure this shelf names, in card after card, is every surface in the frame being given the same attention.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The state of a surface — moisture, freshness, wetness — is the question, because this shelf and the staging shelf disagree about who owns it and neither has conceded.** A card here says the difference between fresh and plastic is almost entirely moisture and edge light; a card on the staging shelf says the same state is almost entirely a staging decision and not a lighting one. Route to both and settle it yourself. Also **distrust the first axis when your honest answer is *close*** — nearly half the shelf lives there, so on a close frame this map has only two questions left and is doing a third of the work it does on a wide one. And **this card cannot tell you how many surfaces you may describe**, only which card describes each; the budget is the third axis' warning and it is the thing this shelf is worst at enforcing on itself.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — At what distance will this surface be read?**
Asked first, because it is the only condition on this shelf that eliminates cards outright rather than re-routing them. *"Too distant to resolve weave; the fall still reads"* (`material.weave_scale`), *"Small scale; one named loose strand instead"* (`material.hair_behaviour`), *"Even haze goes milky; layer it with distance"* (`material.dust_air`), and a wall that *could be a model or a monument* without a known grain beside it (`material.scale_cue`). A surface described finer than the frame can resolve is words spent on nothing, and the shelf says so in its own first card.

**Axis 2 — Does this surface appear on its own, or only under a light chosen for it?**
Nine of the fifteen cards make a light part of their own answer, and four of them escape the shelf through the lighting family when the light is wrong: *"Busy environment; one controlled source describes the curve"* (`material.metal_behaviour`), *"Detail only where the light rakes across it"* (`material.stone_masonry`), *"Hard direct sun, where the contact really is abrupt"* (`material.contact_and_shadow`), *"Mood outranks surface; carry the material in a plate"* (`material.light_response_pairing`). The other six describe structure — thread, fall, grain, wear, damage, known grain size — and hold under any light at all. **This is the axis the shelf argues with its neighbour about**, and it is why that argument is in this card's `Avoid when:`.

**Axis 3 — Are you naming the substance, or proving it?**
Eleven cards say what a thing is made of. Four say the frame must show that the naming was true — the air carrying the distance, the light chosen for the surface, the dark line where an object meets its ground, a known grain declaring the scale of everything near it. **Those four are the target of no pointer from the eleven, and the eleven are the target of no pointer from the four.** That is not two shelves; it is the second half of one sentence. The four cannot be chosen until the eleven have been answered, which is exactly why the pair graph never puts them in competition and exactly why this axis is asked last.

---

**The map**

**Axis 1 — at what distance it will be read**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Close enough to count threads, pores, crumb and tool marks** | `material.weave_scale` · `material.skin_surface` · `material.food_surface` · `material.wear_history` · `material.wood_grain` · `material.blood_wound_restraint` · `material.light_response_pairing` |
| **At figure or object distance, where mass, fall and reflection read but grain does not** | `material.drape_weight` · `material.hair_behaviour` · `material.metal_behaviour` · `material.water_glass` · `material.contact_and_shadow` |
| **Across a distance, where only courses, air and scale survive** | `material.stone_masonry` · `material.dust_air` · `material.scale_cue` |

**Axis 2 — whether it needs a light chosen for it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Only under a chosen light — name the source in the same breath or the words are wasted** | `material.skin_surface` · `material.hair_behaviour` · `material.metal_behaviour` · `material.water_glass` · `material.stone_masonry` · `material.food_surface` · `material.contact_and_shadow` · `material.light_response_pairing` · `material.dust_air` |
| **On its own, from its own structure — the light can be anything** | `material.weave_scale` · `material.drape_weight` · `material.wear_history` · `material.wood_grain` · `material.blood_wound_restraint` · `material.scale_cue` |

**Axis 3 — naming the substance, or proving it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Naming — what the thing is made of** | `material.weave_scale` · `material.drape_weight` · `material.wear_history` · `material.metal_behaviour` · `material.skin_surface` · `material.hair_behaviour` · `material.stone_masonry` · `material.wood_grain` · `material.water_glass` · `material.food_surface` · `material.blood_wound_restraint` |
| **Proving — the frame must show the naming was true** | `material.dust_air` · `material.light_response_pairing` · `material.contact_and_shadow` · `material.scale_cue` |

*A card appears once per axis. The answer is the intersection of the first two shortlists — normally two to four cards — plus at least one card from the second value of the third.*

---

**The default, and the one against it**

**In-degree cannot choose a default on this shelf and it is not close.** Nothing here takes more than one inbound pointer from anywhere in the package, and one of the five inbound edges starts at a named failure on the repair family — a floating object being told to name its contact shadow — which is an instruction pointing into the map from outside rather than a route across it. Discount that and four cards are reached once each, on four unrelated conditions. **A shelf whose most-reached card is reached once has no measurable fallback, and the default has to be argued.**

**The default is `material.light_response_pairing`, taken with whichever substance card the first two axes returned.** The argument is that it is the only card on this shelf whose job is to stop the other fourteen being wasted. Every card here writes a sentence about a surface; this is the one that asks whether the frame will ever show it. Its own statement of the problem is the shelf's commonest complaint in one line — a weave described but flatly lit is invisible, and the words were spent for nothing — and the failure it names is the one that sends people back to reroll a prompt that was already correct. **And it has a real cost, which it admits: the light that best reveals a surface is often wrong for the scene.** A shelf that defaults here produces images that are about their own surfaces. That cost is the argument for what comes next.

**The one against it is `material.blood_wound_restraint`, and the argument is that it is the only card here that tells you to describe less.** Fourteen cards on this shelf add: threads, pores, patina, caustics, courses, strands, air. This one decides *how much is shown rather than defaulting to maximum*, and its measure of success is that the audience does not notice the craft — overstated damage reads as effect and the viewer stops believing. It is also the only card that treats a surface as something that happened to a person rather than something an object is made of, the only one that needs no light and no distance and no companion surface, and the only one whose boundary clause names the rest of the shelf's instinct as the fault: damage at full intensity in a frame whose subject is something else. Against a default whose reflex is *reveal it*, this is the card that says the frame can be spent elsewhere. Its near cousin against the grain is `material.dust_air`, which is the only card here whose material is not a thing at all.

---

**The unasked**

**Ten of the fifteen cards are the target of no pointer anywhere in the package.** By id:

`material.weave_scale` · `material.metal_behaviour` · `material.skin_surface` · `material.hair_behaviour` · `material.stone_masonry` · `material.wood_grain` · `material.water_glass` · `material.dust_air` · `material.blood_wound_restraint` · `material.light_response_pairing`

**And the shape of that list is the finding, not its length.** Lay it against the second axis and it is almost exact: **seven of the nine cards that need a light chosen for them are the target of nothing.** The two exceptions are reached from off the shelf entirely — one from a staging card weighing whether to cut a fruit open, one from a named failure about objects that float. **Not one reader, anywhere in this package, ever wrote *not that surface — this one, lit differently*.** They compared substances: wool against linen, bronze against iron, mudbrick against ashlar. The pair graph here is a graph of materials, and the entire lighting half of the shelf is invisible to it — which is why the second axis had to be built by hand, and why the card whose whole purpose is that comparison is pointed at by nothing in four thousand cards. **A citation-counting measure of this shelf would have reported that the lighting question does not exist.**

The second thing the list shows: **nothing on this shelf changes while you look at it.** Steam rises in one prompt and condensation runs in one clause on the neighbouring shelf, and neither has a clock. There is no card for wax cooling, ice melting, blood drying between two frames of the same sequence, paint still wet, bread going stale under the lights — the continuity problem that arrives the moment a plate is fed into a video stage, which is a format almost every card here lists. The nearest card is about wear, which is time already finished and cannot be re-run. **The card this shelf wants is the one that says a surface has a state and a rate, and that two frames of the same object have to agree about both.** Its own boundary clause records the near miss — everything equally distressed reads as a costume prop — and nothing routes a reader there to read it.

`material.distance_before_substance`

---

### Weave and Thread Scale

**Also called:** fabric grain, textile scale, cloth resolution  
**What it is:** Naming how coarse or fine the cloth is at the scale it will be seen, the thread thickness, the weave pattern and whether individual fibres are visible at that distance.  
**Effect on the audience:** Cloth that belongs to a period and a class. Coarse undyed wool and fine bleached linen say completely different things about a person before their face is read.  
**Used for and where it works best:** Heritage and historical work where textile is the main class marker, fashion and product work where the fabric is the subject, and any close portrait where clothing fills the frame. Best in heritage documentary, fashion and product stills.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Product Still / Packshot, Fashion Film, Heritage / Historical Documentary, Editorial / Magazine Image, Generated Keyframe Feeding Video, Poster / Static Design, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Mythology / Ancient Epic, War, Verite / Observational  
**Avoid when:** It usually wastes words at a distance where no weave can be resolved. The exception is naming it anyway on a wide shot when the same garment will be seen close later, so the two images agree.  
**Prompt:** `coarse undyed wool, thick uneven threads visible at this distance, a simple over-under weave, slubs and irregularities left in`  
**Yields to:** `material.drape_weight` — Too distant to resolve weave; the fall still reads.  
`material.weave_scale`

### Drape and Cloth Weight

**Also called:** fall, hang, fabric body  
**What it is:** Describing how the cloth falls under its own weight, where it gathers, how sharp its folds are and whether it clings or stands away from the body.  
**Effect on the audience:** Garments that are worn rather than painted on. Weight is what separates a real robe from a texture wrapped around a figure.  
**Used for and where it works best:** All costume and heritage work, fashion, and any full-figure image where the garment describes the body. Best in character sheets, fashion and heritage plates.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Fashion Film, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Poster / Static Design, Editorial / Magazine Image, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Fantasy / Epic, Mythology / Ancient Epic, Tragedy  
**Avoid when:** It usually contradicts the pose when heavy drape is described on a figure in fast motion. The exception is the instant of arrest, where heavy cloth still carries the shape of the movement that just stopped.  
**Prompt:** `heavy wool that hangs straight with deep soft folds, gathering at the belt and falling in a column to the ankle, no clinging, no flutter`  
**Yields to:** `pose.action_arrested` — Heavy drape described on a figure in fast motion.  
`material.drape_weight`

### Wear, Patina and Use History

**Also called:** ageing, distress, evidence of use  
**What it is:** Describing where a surface has been worn by use, the polished edge of a handle, the thin place at a knee, the darkened rim of a cup, so the damage follows function rather than being scattered.  
**Effect on the audience:** Objects with a past. Random distress reads as dirt; wear placed where hands and bodies actually touch reads as history.  
**Used for and where it works best:** Heritage reconstruction, props and artefact work, and any story where the age of a thing carries meaning. Best in props sheets, product stills and heritage documentary.  
**Best in:** formats: Props Sheet, Product Still / Packshot, General Reference Plate, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Editorial / Magazine Image, Poster / Static Design, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Adventure, War, Survival, Mythology / Ancient Epic  
**Avoid when:** It usually cheapens a hero object when every surface is equally distressed, which reads as a costume prop. The exception is deliberate ruin, where uniform decay is the subject rather than the character of the object.  
**Prompt:** `the bronze handle polished bright where the hand grips it, the rest darkened with patina, the base scratched from being set down on stone`  
**Yields to:** `staging.human_trace` — Hero object must stay clean; carry use in the staging.  
`material.wear_history`

### Metal and Specular Behaviour

**Also called:** reflectivity, metalness, sheen  
**What it is:** Naming which metal, how polished it is, and what it is reflecting, because a metal surface shows its environment rather than its own colour.  
**Effect on the audience:** Metal that reads as metal. Without naming the reflection, generated metal arrives as grey plastic with a highlight painted on it.  
**Used for and where it works best:** Product and packaging work, weapon and armour reconstruction, jewellery, and any heritage object in bronze, gold or iron. Best in product stills, props sheets and heritage work.  
**Best in:** formats: Product Still / Packshot, Props Sheet, General Reference Plate, Commercial / TVC, Heritage / Historical Documentary, Editorial / Magazine Image, Generated Keyframe Feeding Video, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Heritage (civilisation-focused), Historical / Biopic, War, Fantasy / Epic, Mythology / Ancient Epic, Sci-Fi, Action  
**Avoid when:** It usually confuses the read when a highly polished object sits in a busy environment and the reflections compete with the form. The exception is a controlled reflection, a single bright card or window placed to describe the curve.  
**Prompt:** `cast bronze, low polish, reflecting the warm wall and the single window as soft broad shapes rather than sharp points, darker in the recesses where light cannot reach`  
**Yields to:** `light.softbox` — Busy environment; one controlled source describes the curve.  
`material.metal_behaviour`

### Skin Surface and Subsurface

**Also called:** skin texture, pores, subsurface scattering  
**What it is:** Describing skin as a translucent layered surface with pores, fine hair, unevenness and light that enters and scatters, rather than as a smooth coloured shape.  
**Effect on the audience:** Faces that are alive. In a close frame, perfectly smooth skin is the single strongest signal that an image was generated — in a composed pose it is perfect symmetry, which `pose.the_small_asymmetry` breaks — and adding real surface is the fastest fix.  
**Used for and where it works best:** All portrait and character work, heritage reconstruction of faces, and any close frame where a person fills the image. Best in character sheets, keyframe plates and editorial portraits.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Editorial / Magazine Image, Poster / Static Design, Heritage / Historical Documentary, Brand Film, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: all  
**Avoid when:** It usually fights a stylised or illustrated register where smoothness is the convention. The exception is a hybrid where the face carries surface while the rest of the image stays stylised, which draws the eye to the face.  
**Prompt:** `real skin surface, visible pores across the nose and cheeks, fine vellus hair catching the rim light, uneven colour with warmth at the ears and nose, light entering the skin at the thin edges`  
**Yields to:** `anime.flat_cel_shading` — Stylised register where smoothness is the convention.  
`material.skin_surface`

### Hair Mass and Strand Behaviour

**Also called:** hair grouping, strand clumping, hair light response  
**What it is:** Describing hair as grouped masses with a few loose strands rather than as individual fibres, and naming how it catches light at the rim and absorbs it in the mass.  
**Effect on the audience:** Hair that has weight and a direction of growth. Hair generated without mass reads as a helmet or as noise.  
**Used for and where it works best:** All character and portrait work, historical styles where the arrangement is period evidence, and any image with backlight where hair carries the edge. Best in character sheets and portraits.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Editorial / Magazine Image, Poster / Static Design, Fashion Film, Heritage / Historical Documentary, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: all  
**Avoid when:** It usually over-describes at small scale where the mass is all that can be seen. The exception is a single named loose strand, which reads as a deliberate detail rather than as rendering effort.  
**Prompt:** `thick dark hair in heavy grouped masses with a few strands loose at the temple, the rim light catching only the outer edge, the interior mass absorbing light into near black`  
**Yields to:** `pose.the_small_asymmetry` — Small scale; one named loose strand instead.  
`material.hair_behaviour`

### Stone, Brick and Masonry

**Also called:** mudbrick, ashlar, rubble, stone surface  
**What it is:** Naming the stone or brick type, how it was cut or moulded, the joint width, and what weather has done to the exposed faces.  
**Effect on the audience:** Architecture that belongs to a place and a technology. Mudbrick, limestone ashlar and fired brick are each a different civilisation before a single ornament is added.  
**Used for and where it works best:** Heritage and archaeological reconstruction, location plates, and any exterior where the building is the evidence. Best in location sheets and heritage documentary.  
**Best in:** formats: Location Sheet / Master Plate, General Reference Plate, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Travel / Real Estate / Hospitality, Poster / Static Design, Editorial / Magazine Image, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, War, Adventure, Verite / Observational, Faith / Biblical Epic  
**Avoid when:** It usually turns into texture noise when every surface is described at equal detail. The exception is placing detail only where light rakes across it, letting the shadowed walls stay simple.  
**Prompt:** `sun-dried mudbrick laid in regular courses with thick mud mortar, faces eroded soft by wind, the lower courses darker where damp has risen`  
**Yields to:** `light.side_raking` — Detail only where the light rakes across it.  
`material.stone_masonry`

### Wood, Grain and Joinery

**Also called:** timber, carved wood, grain direction  
**What it is:** Naming the species, the grain direction relative to the object, how it was worked, and whether it is oiled, painted, weathered or raw.  
**Effect on the audience:** Wooden objects that were made rather than moulded. Grain direction tells the eye how the piece was cut, which is what makes furniture and tools convincing.  
**Used for and where it works best:** Props and furniture work, heritage reconstruction of doors, boats, ploughs and instruments, and product work in wood. Best in props sheets and product stills.  
**Best in:** formats: Props Sheet, Product Still / Packshot, General Reference Plate, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Editorial / Magazine Image, Travel / Real Estate / Hospitality, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Slice of Life, Adventure, Family, Drama  
**Avoid when:** It usually looks wrong when the grain runs against the way the object would actually have been cut. The exception is deliberately reused timber, where a contrary grain is evidence of a second life.  
**Prompt:** `dark oiled cedar, grain running the length of the plank, hand-planed surface with shallow tool ripples, joints pegged rather than nailed`  
**Yields to:** `material.wear_history` — Reused timber: contrary grain is evidence of a second life.  
`material.wood_grain`

### Water, Glass and Transparency

**Also called:** refraction, caustics, transparent media  
**What it is:** Describing what is seen through the material as well as the material itself, the distortion, the edge brightening, the caustic patterns thrown onto surfaces beyond.  
**Effect on the audience:** Transparency that behaves optically instead of looking like a grey overlay. The give-away of generated glass is that nothing behind it bends.  
**Used for and where it works best:** Product work with bottles and vessels, heritage reconstruction with water channels and vessels, and any interior with a window as a subject. Best in product stills and location plates.  
**Best in:** formats: Product Still / Packshot, Props Sheet, General Reference Plate, Location Sheet / Master Plate, Commercial / TVC, Editorial / Magazine Image, Generated Keyframe Feeding Video, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: all  
**Avoid when:** It usually complicates the read when transparency sits in front of a busy background and the subject is lost in the distortion. The exception is a controlled clean ground behind the glass, which lets the refraction describe the form.  
**Prompt:** `clear glass vessel, the wall behind it visibly bent and displaced through the body, bright at the rim where the glass thickens, a bright caustic pool cast on the table beside it`  
**Yields to:** `photo.packshot` — Busy background behind glass; use a clean controlled ground.  
`material.water_glass`

### Dust, Haze and Particulate Air

**Also called:** atmosphere, airborne particles, air density  
**What it is:** Treating the air itself as a material with density, so light has something to travel through and distance visibly desaturates.  
**Effect on the audience:** Depth and heat. Air is what makes a wide exterior read as a real distance rather than as a flat backdrop.  
**Used for and where it works best:** Exteriors in dry climates, interiors with shafts of light, battle and market scenes, and any wide establishing frame that needs depth. Best in heritage work, travel and epic sequences.  
**Best in:** formats: Generated Keyframe Feeding Video, Location Sheet / Master Plate, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Poster / Static Design, Brand Film, General Reference Plate, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Heritage (civilisation-focused), Historical / Biopic, War, Adventure, Western, Mythology / Ancient Epic, Nature / Wildlife  
**Avoid when:** It usually flattens contrast when applied evenly across the whole frame, leaving the image milky. The exception is layered haze that increases with distance, which separates planes instead of veiling them.  
**Prompt:** `dry dusty air, fine particles visible in the shaft of light, the far wall clearly hazed and desaturated while the foreground stays clear and saturated`  
**Yields to:** `comp.aerial_perspective` — Even haze goes milky; layer it with distance.  
`material.dust_air`

### Food Surface and Freshness

**Also called:** food texture, appetite appeal, moisture  
**What it is:** Describing the specific surface state that signals freshness, the steam, the crumb, the gloss on a cut face, the condensation, and where the light must sit to reveal it.  
**Effect on the audience:** Appetite. Food photographed or generated without a specific surface state reads as plastic: staging supplies the moisture state, and edge or raking light makes that state visible.
**Used for and where it works best:** Food and hospitality work, packaging, heritage reconstruction of meals and markets. Best in product stills, editorial and advertising.  
**Best in:** formats: Product Still / Packshot, Food Video, Editorial / Magazine Image, Commercial / TVC, Thumbnail / Social Card, Poster / Static Design, Generated Keyframe Feeding Video, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Slice of Life, Family, Heritage (civilisation-focused), Historical / Biopic, Comedy  
**Avoid when:** It usually reads as artificial when every surface is glossy at once, which is the signature of over-styled food photography. The exception is a deliberately stylised commercial register where that excess is the convention.  
**Prompt:** `fresh flatbread torn open, visible open crumb, steam rising from the break, a matte floured crust against the soft moist interior, raking light from the left to catch the texture`  
`material.food_surface`

### Blood, Wound and Physical Damage

**Also called:** injury, gore restraint, damage state  
**What it is:** Describing damage by its physical state, colour by age, wet or dried, swelling and staining, and deciding how much is shown rather than defaulting to maximum.  
**Effect on the audience:** Injury that reads as real and lands emotionally. Overstated damage reads as effect and the viewer stops believing.  
**Used for and where it works best:** War, historical and survival narratives, and any story where physical cost must register. Best in historical drama and documentary reconstruction.  
**Best in:** formats: Generated Keyframe Feeding Video, Character Sheet / Turnaround, Heritage / Historical Documentary, Poster / Static Design, Brand Film, General Reference Plate, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: War, Historical / Biopic, Tragedy, Survival, Action, Drama, Heritage (civilisation-focused)  
**Avoid when:** It usually overwhelms the scene when damage is rendered at full intensity in a frame whose subject is something else. The exception is a single shot where the damage is the subject and the restraint has been spent elsewhere.  
**Prompt:** `a day-old wound, dried dark at the edges with dulled swelling around it, cloth stained stiff rather than wet, no fresh bright red`  
`material.blood_wound_restraint`

### Pair the Material With Its Light

**Also called:** material and light together, surface-led lighting  
**What it is:** Choosing the lighting that reveals the named material rather than lighting the scene first and hoping the surface survives. Raking light for texture, broad soft light for gloss, backlight for translucency.  
**Effect on the audience:** The material actually appears. A weave described but flatly lit is invisible, and the words were wasted.  
**Used for and where it works best:** Every image where a material matters, and the usual fix when a described texture does not show up in the output. Best in product stills, heritage work and portraits.  
**Best in:** formats: Product Still / Packshot, Props Sheet, General Reference Plate, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Editorial / Magazine Image, Heritage / Historical Documentary, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: all  
**Avoid when:** It usually costs the mood when the lighting that best reveals a surface is wrong for the scene. The exception is revealing the material in a dedicated reference plate and lighting the story frame for the story.  
**Prompt:** `hard raking light from the left at a shallow angle, chosen so the coarse weave and the tool marks are visible; a broad soft source would have erased both`  
**Yields to:** `ref.wardrobe_material` — Mood outranks surface; carry the material in a plate.  
`material.light_response_pairing`

### Contact Shadow and Ground Truth

**Also called:** occlusion shadow, grounding, contact darkening  
**What it is:** Naming the dark contact line where an object meets its surface, and how it softens with distance from the point of touch.  
**Effect on the audience:** Objects that sit on the ground instead of floating above it. Missing contact shadow is the most common reason a generated object looks pasted in.  
**Used for and where it works best:** All product work, any object placed in an environment, and every keyframe where a figure stands, sits or leans. Best in product stills and keyframe plates.  
**Best in:** formats: Product Still / Packshot, Generated Keyframe Feeding Video, Props Sheet, General Reference Plate, Commercial / TVC, Editorial / Magazine Image, Poster / Static Design, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: all  
**Avoid when:** It usually looks heavy when the contact shadow is drawn as a hard band rather than as a gradient that opens away from the touch. The exception is hard direct sun, where the contact really is abrupt.  
**Prompt:** `a dark tight contact shadow where the base meets the stone, opening and softening within a hand's width, confirming the object rests on the surface rather than hovering`  
**Yields to:** `light.hard` — Hard direct sun, where the contact really is abrupt.  
`material.contact_and_shadow`

### Scale Cue Inside the Material

**Also called:** size reference, grain as ruler  
**What it is:** Using a material whose grain size the viewer already knows, brick courses, floorboards, fabric weave or sand, to declare the scale of everything around it.  
**Effect on the audience:** The image stops being ambiguous about size. Without a known grain, a wall could be a model or a monument.  
**Used for and where it works best:** Architectural and heritage reconstruction, miniature and model work, and any wide frame with no human figure. Best in location sheets and heritage documentary.  
**Best in:** formats: Location Sheet / Master Plate, General Reference Plate, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Travel / Real Estate / Hospitality, Poster / Static Design, Explainer, Still Life Photography, Food Photography, Fashion Photography, Architectural Photography, Interior Photography, Nature and Botanical Photography, Travel Photography, Portrait Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Mythology / Ancient Epic, Adventure, Verite / Observational  
**Avoid when:** It usually contradicts itself when two materials in the same frame imply different scales. The exception is deliberate forced perspective, where the contradiction is the trick being played.  
**Prompt:** `mudbrick courses at a true hand-span height running along the wall, declaring the scale of the doorway and the figure who would pass through it`  
**Yields to:** `comp.forced_perspective` — Two materials imply different scales deliberately.  
`material.scale_cue`
