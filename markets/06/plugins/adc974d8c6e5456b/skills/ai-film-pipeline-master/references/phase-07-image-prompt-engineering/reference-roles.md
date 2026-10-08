# Reference Roles and Multi-Reference Assembly

16 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name the Role Before the Reference

**Also called:** the reference selector, role before upload, what is this picture for  
**What it is:** The card at the head of the `ref.` shelf. It does not describe a technique. It asks the three questions this shelf's own cards ask over and over — **what does this reference govern, how many can be switched on at once, and is there a real thing behind it** — and hands back a named shortlist for each answer. The axes were read off the shelf's `Avoid when:` lines and its pair conditions, not invented. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that the picture you attach was attached for a stated reason, rather than because it was open in another window.  
**Used for and where it works best:** Answer the three questions **before you attach anything**, one sentence each, in order. The first names what the image is allowed to govern; the second decides what gets switched off to make room; the third decides whether a description in words may stand in for a picture at all. If you cannot answer question one for an image you are about to supply, you are not short of a reference — you are short of a decision about the frame, and the model will make it for you.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The piece is historical and a real find, relief, site plan or excavation photograph exists.** On a history piece the user wants realistic, the reference is looked for rather than selected (the canon, then the web) and attached when found; when none is found, the closest thing is generated and the work carries on (heritage-rules rule 1). Also **distrust axis one whenever your honest answer is its last value** — six of the fourteen cards here are not about any picture in the frame at all but about the set of pictures, so on a first generation with a single reference this card has one real question and is doing a third of the work it does on a built library. And **do not read the map's order as a ranking**: this shelf has no card that anything reaches for two different reasons, so it has no measured default and this card's own default is argued rather than counted.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — What is this reference allowed to govern, and what will it drag in behind that?**
Asked first because it is the condition the shelf states most often. Nearly every card's `Avoid when:` is the same accident wearing a different coat: the reference arrives carrying something you never asked it for. *Its studio light, its grey backdrop, its shoulder crop, its cool colour cast* (`ref.negative_role`). *The body and the pose the garment was photographed on* (`ref.wardrobe_material`). *A pose the animal's skeleton will not leave* (`ref.animal`). *The body proportions of whoever performed the movement* (`ref.video_motion`). *A recognisable subject of its own that reappears in the output* (`ref.style_separate`). *A perspective that fights the intended lens and height* (`ref.environment_plate`). *The room tone and recording character of the take* (`ref.audio`). Naming the role is how you name the residue.

**Axis 2 — How many can actually be active, and what happens to the ones that do not fit?**
The shelf's only internal argument. `ref.budget_ranking` states the constraint — endpoints accept a small number of active references and the weakest dilute the strongest — and two cards send a reader there on it: *"Exclusions outgrow the direction; cut the reference instead"* (`ref.negative_role`) and *"Irrelevant views waste a tight reference budget"* (`ref.no_crop`). `ref.conflict_resolution` is the same pressure from the other end, *two photographs of the same person both claiming to be the face*, and `ref.sheet_grouping` is what happens when several views arrive as one file.

**Axis 3 — Is there a real thing behind this, and may a description in words stand in for it?**
The axis that carries this project's firm rule, and the one that finds the shelf's own collision. `ref.prop_object` exists because *in heritage work this is the difference between a researched artefact and a plausible-looking invention*. `ref.wardrobe_material` exists because a garment *has been researched and must be reproduced*. `ref.provenance` exists because a reference may depict *a real identifiable person*. And `ref.identity_only` carries the carve-out in its own words: where the subject's appearance is undocumented — any pre-330 BC figure, or any historical person with no surviving likeness — **the card does not apply**, the face is not shown, and extraction is limited to build, colouring, dress and silhouette. Asked last, because it decides whether the first two answers were allowed.

---

**The map**

**Axis 1 — what the reference governs**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Who — a living subject, and only who they are** (two) | `ref.identity_only` · `ref.animal` |
| **What — a thing, its material and its construction** (two) | `ref.wardrobe_material` · `ref.prop_object` |
| **Where — the place, its scale and its ground** (one) | `ref.environment_plate` |
| **How it is made — the register, not the content** (one) | `ref.style_separate` |
| **Something that runs in time rather than sits still** (two) | `ref.audio` · `ref.video_motion` |
| **Nothing in the frame — the reference set itself** (six) | `ref.negative_role` · `ref.budget_ranking` · `ref.sheet_grouping` · `ref.no_crop` · `ref.conflict_resolution` · `ref.provenance` |

**Axis 2 — how many are active, and what falls off the end**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One at a time, and it must not bring its own light** (nine) | `ref.negative_role` · `ref.identity_only` · `ref.wardrobe_material` · `ref.environment_plate` · `ref.prop_object` · `ref.animal` · `ref.style_separate` · `ref.audio` · `ref.video_motion` |
| **Several, but they are views of one thing** (two) | `ref.sheet_grouping` · `ref.no_crop` |
| **More than fit — something is ranked, cut or retired** (two) | `ref.budget_ranking` · `ref.conflict_resolution` |
| **However many, and somebody may later ask where they came from** (one) | `ref.provenance` |

**Axis 3 — is there a real thing behind it**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A real find, a real garment, a real place — words may not stand in** (four) | `ref.prop_object` · `ref.wardrobe_material` · `ref.environment_plate` · `ref.provenance` |
| **A real subject, and whether the face may be shown is a separate question** (two) | `ref.identity_only` · `ref.animal` |
| **A made image, a record of nothing** (five) | `ref.style_separate` · `ref.sheet_grouping` · `ref.no_crop` · `ref.conflict_resolution` · `ref.negative_role` |
| **A recording rather than a picture** (two) | `ref.audio` · `ref.video_motion` |
| **Words are being let in to replace a picture — and this answer is a collision, not a route** (one) | `ref.budget_ranking` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and on this shelf it is normally one or two cards wide, because the first axis is already narrow.*

**The collision on axis three, recorded and not corrected.** `ref.budget_ranking` carries, as its own prompt line, *"Props are described in words this time rather than referenced"* — a prop demoted from a picture to a sentence to free a slot. That is the exact trade `ref.prop_object` exists to refuse, and on a history piece the user wants realistic it is the trade the reference-first rule steers against: a found reference takes the slot. The two cards are both correct about their own subject and they disagree about this one. **Nothing here is edited to hide that**: the value is named on the map as a collision so that a reader who lands on it knows they have arrived at a dispute rather than at an answer, and the arithmetic below records it.

---

**The default, and the one against it**

**This shelf has no measured default, and that is the first honest thing to say about it.** Counting distinct conditions behind inbound edges, rather than edges: `ref.budget_ranking` is reached twice and both edges fire on the same condition — *there is not room for everything*. That makes it the door out of the shelf, not the thing the shelf falls back on. `ref.style_separate` and `ref.wardrobe_material` are reached once each, and the second of those arrives from another shelf entirely. Nothing here is reached twice for two reasons.

**The card the file itself calls the base technique is `ref.role_declared`, and the map may not offer it** — the package files it as coexisting with its neighbours rather than competing with them, which is correct: it is not an alternative to anything, it is the sentence every other card is written inside. **A shelf whose default is not a choice is a shelf whose selector has to argue one.**

**So the argued default is `ref.negative_role`.** Seven of this shelf's `Avoid when:` lines describe one accident, and `ref.negative_role` is the only card on the shelf that is a clause against it. Everything else names what a reference is *for*; this is the only card that names what it must not be allowed to do, and the field that forbids is the field that decides.

**The one against it is `ref.provenance`.** Nothing routes to it. Its own effect line concedes that nothing appears in the image. It is the only card here that is about a person who is not in the frame and may never see the result, and the only one whose value is realised entirely after publication, at the moment somebody asks a question the rest of the shelf has no way of answering. Its stated cost is the smallest on the shelf — it feels like overhead on a private study — and a habit that costs nothing to keep and cannot be reconstructed later is the definition of a thing worth doing against the grain. **Its near cousin is `ref.audio`**, the only card on this shelf that is not an image at all, likewise never routed to, and the one that asks the question the rest of the file never thinks to ask: *what else in this piece is a reference?*

**The stated runner-up, so the ranking is not silent:** `ref.identity_only`, which is the card the most projects actually open on, and which is second only because its own text hands the undocumented case straight out of the shelf.

---

**The unasked**

**Eleven of the fourteen reachable cards are the target of no pair condition anywhere in the package.** By id:

`ref.negative_role` · `ref.identity_only` · `ref.environment_plate` · `ref.prop_object` · `ref.animal` · `ref.audio` · `ref.video_motion` · `ref.sheet_grouping` · `ref.no_crop` · `ref.conflict_resolution` · `ref.provenance`

**And the shape of that list is the finding.** Every card under the first five values of axis one is on it except two — and the only route into a role card at all arrives **from another shelf**, where a materials card sends a reader to `ref.wardrobe_material` because mood outranked surface. Inside the shelf, no role ever yields to another role. That is not an omission. **A set of references is an AND, and the pair field can only say OR.** Identity, wardrobe, place and object are not alternatives to one another; they are slots filled at the same time by different pictures, which is exactly why the package files the role-declaring card as additive. The only place the shelf is forced to turn its AND into an OR is when the endpoint runs out of slots — and that is precisely where both of its internal edges land.

The second thing the list shows: **the whole custody region is unasked.** `ref.provenance`, `ref.conflict_resolution` and `ref.no_crop` describe what happens to a reference library over months — a superseded face, a sheet nobody cropped, a source nobody logged — and nothing in the package sends a reader to any of them. The shelf is written by people holding one generation, and a reference library is not a generation, it is an archive. The card this shelf wants and does not have is the one that says **a reference has a lifespan**: it was made for a shot, it is being reused on a shot it was not made for, and the drift that follows has no name here. The nearest thing that exists, `ref.conflict_resolution`, records that failure in its own `Avoid when:` — *when a precedence rule is needed on every generation, the real fix is retiring the superseded reference* — with nothing routing a reader there to read it.

`ref.role_before_the_reference`

---

### Role-Declared Reference

**Also called:** labelled reference, scoped reference, role-tagged input  
**What it is:** Each supplied image is named with the single thing it governs, identity, wardrobe, pose, environment, palette or object, and the prompt states that role in words beside the tag. Nothing is left for the model to infer from the picture alone.  
**Effect on the audience:** The result reads as one coherent photograph rather than an average of several. Faces stay recognisable, clothing stays correct, and the location does not leak its lighting onto a subject shot elsewhere.  
**Used for and where it works best:** Any generation with more than one reference. It is the base technique of this whole category and every other card assumes it. Essential for series work where the same character appears across dozens of images made weeks apart. Best in character sheets, keyframe plates and campaign work.  
**Best in:** formats: General Reference Plate, Generated Keyframe Feeding Video, Character Sheet / Turnaround, Poster / Static Design, Commercial / TVC, Comics / Webtoon / Photo Essay, Brand Film, AI-Generated Clip, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually adds nothing when a single reference supplies everything and the prompt is short, where naming the role is a formality. The exception is a house style built on declared roles, where the consistency of the record is worth more than the words saved.  
**Prompt:** `reference A supplies facial identity only; reference B supplies the coat and its worn leather texture; reference C supplies the courtyard and its stone; do not take lighting or colour from any reference`  
`ref.role_declared`

### Negative Role Statement

**Also called:** do-not-copy line, exclusion clause, reference fencing  
**What it is:** Beside each positive role, a second clause naming what that reference must not contribute. Usually the strongest attributes of the source image that are not wanted: its lighting, its background, its crop, its colour cast.  
**Effect on the audience:** Removes the tell-tale signs of borrowed material. Without it the subject arrives carrying the source photograph's light and the composite looks assembled.  
**Used for and where it works best:** Whenever a reference is a real photograph with strong lighting of its own, which is nearly always. Critical when a character reference was shot in daylight and the target scene is a night interior. Best in keyframe plates, product work and heritage reconstruction.  
**Best in:** formats: General Reference Plate, Generated Keyframe Feeding Video, Character Sheet / Turnaround, Product Still / Packshot, Poster / Static Design, Commercial / TVC, Editorial / Magazine Image, Heritage / Historical Documentary, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually over-constrains when the exclusion list grows longer than the positive description, at which point the model has more prohibitions than direction. The exception is a strict brand or heritage piece where a wrong element costs more than a weak image.  
**Prompt:** `reference A: take the face and hair only, do not take its studio lighting, its grey backdrop, its shoulder crop, or its cool colour cast`  
**Yields to:** `ref.budget_ranking` — Exclusions outgrow the direction; cut the reference instead.  
`ref.negative_role`

### Identity-Only Extraction

**Also called:** face lock, likeness isolation, identity reference  
**What it is:** A reference used for nothing but who the person is, bone structure, features and proportions, with every other attribute explicitly reassigned to the prompt or to another reference.  
**Effect on the audience:** The person is recognisably themselves in a situation the reference never depicted. This is what makes a character survive a costume change, an age change, or a change of century.  
**Used for and where it works best:** Series and episodic work, heritage reconstruction where a modern face must wear an ancient identity, and any piece where the same person appears in wardrobe the reference does not contain. Best in character sheets and keyframe plates.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, Poster / Static Design, Comics / Webtoon / Photo Essay, Heritage / Historical Documentary, Brand Film, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Mythology / Ancient Epic, Tragedy  
**Avoid when:** It usually fails when the reference is a low-resolution or heavily stylised image, because there is not enough structure to extract and the model substitutes a generic face. The exception is deliberate stylisation, where an approximate likeness is the intent. Where the subject's appearance is undocumented — any pre-330 BC figure and any historical person with no surviving likeness — this card does not apply: the face is not shown at all (`doc.faceless_reenactment`, `light.hidden_faces`), and identity extraction is limited to build, colouring, dress and silhouette.  
**Prompt:** `reference A supplies facial identity only: bone structure, eye shape, nose, jaw and hairline. Wardrobe, age, lighting, expression and setting come from this prompt, not from the reference`  
**Yields to:** `doc.faceless_reenactment`, `light.hidden_faces` — where the subject's appearance is undocumented: any pre-330 BC figure, or any historical person with no surviving likeness. The face is not shown, and extraction is limited to build, colouring, dress and silhouette.  
`ref.identity_only`

### Wardrobe and Material Reference

**Also called:** garment reference, costume plate, fabric lock  
**What it is:** A reference supplied purely for what is worn and how the material behaves, weave, drape, wear and weight, separated from whoever is wearing it in the source image.  
**Effect on the audience:** Clothing reads as a real garment with a history rather than a generic costume. The weave and the wear are the difference between a person in period dress and a person in a rental.  
**Used for and where it works best:** Heritage and historical work where a garment has been researched and must be reproduced, brand and fashion work where a specific product must be exact, and any series where wardrobe continuity carries the story. Best in character sheets and heritage plates.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, Product Still / Packshot, Fashion Film, Editorial / Magazine Image, Heritage / Historical Documentary, Poster / Static Design, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Fantasy / Epic, Mythology / Ancient Epic, Verite / Observational  
**Avoid when:** It usually drags the source body shape and pose along with the garment when the reference shows the garment worn. The exception is a flat-lay or mannequin reference, where there is no body to inherit.  
**Prompt:** `reference B supplies the garment only: the coarse undyed wool, the fringed hem, the bronze pin at the shoulder, and how the cloth falls with weight, not the body, the pose, or the background it was photographed against`  
**Yields to:** `frame.flat_lay` — A worn-garment reference drags its body and pose.  
`ref.wardrobe_material`

### Environment Plate Reference

**Also called:** location reference, background plate, setting lock  
**What it is:** A reference supplying the place and nothing else, architecture, ground, horizon, vegetation and scale, with the subject, the light and the time of day set by the prompt.  
**Effect on the audience:** A consistent world across many images. The viewer recognises the courtyard from three images ago even though the hour and the weather changed.  
**Used for and where it works best:** Any project that returns to the same location, documentary and heritage reconstruction built on a real site, and series work where the world is a character. Best in location sheets and keyframe plates.  
**Best in:** formats: Location Sheet / Master Plate, General Reference Plate, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Comics / Webtoon / Photo Essay, Poster / Static Design, Brand Film, Portrait Photography, Character Sheet / Turnaround, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Verite / Observational, Drama, Adventure, Mystery / Whodunit  
**Avoid when:** It usually flattens the scene when the plate perspective fights the intended lens and height of the shot, and the model splits the difference into a place that does not exist. The exception is when the plate was made for this purpose at the viewpoint of the shot itself.  
**Prompt:** `reference C supplies the location only: the mudbrick courtyard, the packed-earth floor, the palm line beyond the wall, and the scale of the doorway. Time of day, weather and light come from this prompt`  
`ref.environment_plate`

### Prop and Object Reference

**Also called:** object lock, prop plate, artefact reference  
**What it is:** A reference for a single object that must be correct, a weapon, a vessel, a relief or a product, kept separate from the character and environment references so its detail is not averaged away. In historical work the reference is mandatory evidence: if the endpoint cannot carry it, generate a dedicated insert, composite it, or mark the result as reconstruction rather than waiving the object reference.  
**Effect on the audience:** The object survives as itself. In heritage work this is the difference between a researched artefact and a plausible-looking invention.  
**Used for and where it works best:** Museum and heritage pieces where an object was researched from a real find, product work where the item is the subject, and any story where a specific object recurs and must be the same object every time. Best in props sheets and product stills.  
**Best in:** formats: Props Sheet, Product Still / Packshot, General Reference Plate, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Poster / Static Design, Commercial / TVC, Editorial / Magazine Image, Portrait Photography, Character Sheet / Turnaround, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Verite / Observational, Mystery / Whodunit, Fantasy / Epic, Mythology / Ancient Epic  
**Avoid when:** It usually loses the object when it occupies a small part of the frame, because reference weight follows frame area. The exception is a dedicated insert image where the object is the whole composition, generated separately and composited later.  
**Prompt:** `reference D supplies the vessel only: its bulbous body, the two lug handles, the incised chevron band, and the fired clay surface, do not take its museum lighting or its neutral backdrop`  
**Yields to:** `size.insert` — Object too small in frame to hold reference weight.  
`ref.prop_object`

### Animal Reference

**Also called:** creature reference, fauna lock  
**What it is:** A reference for an animal treated with the same role discipline as a human character: species, markings, build and coat isolated from the pose, the setting and the light of the source photograph.  
**Effect on the audience:** The animal reads as a specific individual rather than a stock species. In a series the same horse or the same lion returns and the audience recognises it.  
**Used for and where it works best:** Heritage work where the breed must be period-correct, wildlife and nature pieces, and any story where an animal is a recurring character rather than set dressing. Best in character sheets and keyframe plates.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Poster / Static Design, Comics / Webtoon / Photo Essay, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: Nature / Wildlife, Heritage (civilisation-focused), Historical / Biopic, Adventure, Fantasy / Epic, Family  
**Avoid when:** It usually produces anatomical drift when the target pose is far from the reference pose, because animal skeletons tolerate less invention than the model assumes. The exception is a stylised or illustrated register where anatomical exactness is not the standard.  
**Prompt:** `reference E supplies the animal only: the bay coat with the dark points, the heavy build, the short mane, not the stable it stands in, the halter it wears, or its side-on pose`  
**Yields to:** `ref.style_separate` — Stylised register where anatomical exactness is not the standard.  
`ref.animal`

### Audio Reference

**Also called:** voice reference, sound reference, audio conditioning  
**What it is:** An audio file supplied to condition a generation, a voice sample that sets delivery, a music bed that sets tempo, or a line of dialogue that drives lip movement. It is a reference in the same sense as an image and needs the same role declaration.  
**Effect on the audience:** Speech and performance that belong to the same person across every clip, and movement that sits on the beat rather than near it.  
**Used for and where it works best:** Any piece with speech, musical work where motion must land on the beat, and series work where a voice must not drift between episodes. Best in music video, commercial and documentary work.  
**Best in:** formats: Music Video, Commercial / TVC, Brand Film, Documentary Feature, AI-Generated Clip, Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Portrait Photography, Character Sheet / Turnaround, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: Musical, Verite / Observational, Drama, Historical / Biopic, Comedy  
**Avoid when:** It usually clashes when the room tone and recording character of the reference arrive with the voice and fight the acoustic of the scene. The exception is when the recorded space is the point, such as an archival voice deliberately kept as archive.  
**Prompt:** `audio reference supplies the voice character and cadence only, the delivery of the line, not its room tone or its background`  
`ref.audio`

### Video Reference and Motion Transfer

**Also called:** motion reference, driving video, movement transfer  
**What it is:** A short video supplied so its movement, not its appearance, drives a generation. The subject, wardrobe and setting come from elsewhere; only the trajectory, timing and weight of the motion are taken.  
**Effect on the audience:** Motion that has real physical weight, because it was performed rather than described. Gait, gesture and the way a body settles are the hardest things to write in words.  
**Used for and where it works best:** Performance-led pieces, dance and ritual sequences, and any shot where a specific movement was captured and must be reproduced with a different subject. Best in music video and brand work.  
**Best in:** formats: Music Video, Brand Film, Commercial / TVC, Dance Film, Experimental / Art Film, Title Sequence / Opening Credits, AI-Generated Clip | genres: Musical, Drama, Action, Surreal / Absurdist, Heritage (civilisation-focused)  
**Avoid when:** It usually imports the body proportions of the reference along with its motion, so a movement performed by a different build arrives distorted. The exception is when the proportions are close enough that the transfer is invisible.  
**Prompt:** `video reference supplies the movement only: the walking rhythm, the weight shift at each step, and the moment the head turns, not the person, the clothing, or the corridor it was shot in`  
**Yields to:** `ai.motion_prompt` — Reference build differs; write the movement instead.  
`ref.video_motion`

### Reference Budget and Ranking

**Also called:** reference triage, active-reference limit, priority ordering  
**What it is:** Choosing which references are active for a given generation, in priority order, rather than supplying everything held. How many active references an endpoint accepts, and how it weighs them, are endpoint facts rechecked at execution against its adapter in ENGINE-CHECK.md §7; within that limit the weakest references dilute the strongest.  
**Effect on the audience:** The attributes that matter survive. Adding more references can make the face less like the face, not more, and that is tested on the endpoint rather than assumed.  
**Used for and where it works best:** Every multi-reference generation once a project has accumulated a library. Especially where a character sheet, a location plate and three props all exist and only some can be active. A researched artefact is never the reference that drops to words: where it is in the shot it holds a slot, or it goes to its own insert, per `ref.prop_object`. Best in keyframe and campaign work.  
**Best in:** formats: General Reference Plate, Generated Keyframe Feeding Video, Character Sheet / Turnaround, Poster / Static Design, Commercial / TVC, Comics / Webtoon / Photo Essay, AI-Generated Clip, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually costs an attribute that mattered when the ranking is decided once and reused across shots with different needs. The exception is a locked series style where the same ranking is itself the consistency mechanism.  
**Prompt:** `active references in priority order: 1 facial identity, 2 wardrobe, 3 environment. Props are described in words this time rather than referenced, none of them a researched artefact`  
**Yields to:** `ident.frozen_sentence` — Too few active slots; carry the attribute in words.  
`ref.budget_ranking`

### Sheet-as-One-Subject Grouping

**Also called:** panel grouping, sheet framing, multi-view binding  
**What it is:** When a reference is a multi-panel sheet, a turnaround, an expression set or a props board, the prompt states that the panels are views of one subject, not several subjects and not a sequence. Without this the model reads the panel boundaries as composition.  
**Effect on the audience:** The subject arrives whole. Without the grouping statement, generations return either a collage or a frame that has inherited the grid of the sheet.  
**Used for and where it works best:** Any project that works from character sheets and turnarounds, which is the standard way of holding identity across a long production. Best in character sheets, props sheets and keyframe plates.  
**Best in:** formats: Character Sheet / Turnaround, Props Sheet, Location Sheet / Master Plate, General Reference Plate, Generated Keyframe Feeding Video, Comics / Webtoon / Photo Essay, Poster / Static Design, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually does nothing when the reference is a single clean portrait, where there are no panels to misread. The exception is a reference that merely looks like a sheet, such as a contact strip, which still benefits from the statement.  
**Prompt:** `the reference sheet shows one single character from several angles, treat all panels as the same person, do not reproduce the panel grid, the separating lines, or more than one figure`  
`ref.sheet_grouping`

### Never Crop the Sheet

**Also called:** whole-sheet rule, uncropped reference  
**What it is:** Supplying a reference sheet complete rather than cropping out the one view that seems relevant. The full sheet carries three-dimensional information that a single view cannot.  
**Effect on the audience:** Consistency holds when the shot needs an angle the crop did not contain. A profile generated from a front-only crop is invention.  
**Used for and where it works best:** All turnaround and model-sheet work. Most valuable when a sequence will need the subject from angles decided later, which is the normal case in episodic production. Best in character sheets and animation.  
**Best in:** formats: Character Sheet / Turnaround, Props Sheet, Location Sheet / Master Plate, General Reference Plate, Generated Keyframe Feeding Video, 2D Animation (Western / Cartoon), 3D CG Animation, Comics / Webtoon / Photo Essay, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually wastes reference weight when the sheet contains views irrelevant to every shot in the piece and the reference budget of the endpoint is tight. The exception is a purpose-built reduced sheet produced as its own artefact rather than cropped from the full one.  
**Prompt:** `supply the complete character sheet as one reference, uncropped, all views included`  
**Yields to:** `ref.budget_ranking` — Irrelevant views waste a tight reference budget.  
`ref.no_crop`

### Reference Conflict Resolution

**Also called:** precedence rule, conflict order, reference arbitration  
**What it is:** Stating, in the prompt, which reference wins when two supply the same attribute. Two photographs of the same person from different years both claim to be the face; the prompt says which one is current.  
**Effect on the audience:** Stable output across a batch. Without a precedence rule the model resolves the conflict differently on each generation and the character ages and de-ages across a sequence.  
**Used for and where it works best:** Any library that has grown past a single reference per subject, which happens to every project by the second week. Best in long-form series and campaign work.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, Poster / Static Design, Comics / Webtoon / Photo Essay, Brand Film, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually indicates a library problem when a precedence rule is needed on every generation, and the real fix is retiring the superseded reference. The exception is a deliberate dual-state subject, such as a character shown at two ages within the same piece.  
**Prompt:** `where reference A and reference B disagree on the face, reference A governs; reference B is present only for the wardrobe`  
**Yields to:** `ident.canonical_promotion` — Precedence needed every time; promote one, retire the superseded.  
`ref.conflict_resolution`

### Style Reference Held Separate

**Also called:** look reference, render-register reference, aesthetic plate  
**What it is:** A reference supplied for how the image is made rather than what it contains, brush behaviour, grain, palette discipline and edge quality, with an explicit statement that none of its content transfers.  
**Effect on the audience:** A consistent visual register across a body of work made from very different subjects. The pieces look like one hand made them.  
**Used for and where it works best:** Series and campaign work with a defined house look, illustrated and painted registers, and any project where the medium is part of the meaning. Best in posters, comics and social sets.  
**Best in:** formats: General Reference Plate, Poster / Static Design, Comics / Webtoon / Photo Essay, Editorial / Magazine Image, Brand Film, Thumbnail / Social Card, 2D Animation (Western / Cartoon), Generated Keyframe Feeding Video, Portrait Photography, Character Sheet / Turnaround, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography | genres: all  
**Avoid when:** It usually smuggles content across when the style reference has a strong recognisable subject of its own, and that subject reappears in the output. The exception is an abstract or texture-only style plate with no subject to leak.  
**Prompt:** `reference F supplies the render register only: the visible brush direction, the muted earth palette, the soft edges. None of its content, subject or composition transfers`  
**Yields to:** `ident.render_register` — The style image has a subject that leaks.  
`ref.style_separate`

### Reference Provenance Record

**Also called:** rights record, source log, reference custody  
**What it is:** Recording, for every reference in use, where it came from and when, and whether a person depicted is identifiable. The record is kept beside the reference, not in memory. Optional craft: it is never a required step, and it carries rights only where the brief itself raises them.  
**Effect on the audience:** Nothing visible in the image. Its value appears only when a piece is published and a source is questioned, at which point the record is the difference between an answer and a problem.  
**Used for and where it works best:** Heritage pieces built on museum and archive images, any brief that raises sourcing, and any reference depicting a real identifiable person. Best in commissioned and broadcast work.  
**Best in:** formats: General Reference Plate, Character Sheet / Turnaround, Props Sheet, Location Sheet / Master Plate, Heritage / Historical Documentary, Commercial / TVC, Brand Film, Editorial / Magazine Image, Portrait Photography, Still Life Photography, Fashion Photography, Architectural Photography, Documentary Photography, Travel Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually feels like overhead on a private study that will never leave the machine, and even there the habit is cheaper than reconstructing the chain later. The exception is a throwaway test with no identifiable person and no third-party source.  
**Prompt:** `not a prompt line but a record kept beside the reference set: source, date, and whether the depicted person is identifiable`  
`ref.provenance`
