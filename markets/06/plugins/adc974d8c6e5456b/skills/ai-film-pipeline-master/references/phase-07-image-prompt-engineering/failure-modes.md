# Failure Modes and Rescues

10 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Hands That Fail

**Also called:** finger count, hand anatomy failure  
**What it is:** The most persistent generated fault: extra or missing fingers, fused joints, and hands that do not close around what they hold. It worsens when hands are small in frame, overlapping, or interacting with an object.  
**Effect on the audience:** An otherwise convincing image is destroyed at a glance, because a viewer checks hands without deciding to.  
**Used for and where it works best:** Any image with visible hands, which is most character work, and the first thing to inspect before a plate goes into a video stage. Best applied in character sheets and keyframe plates.  
**Best in:** formats: Generated Keyframe Feeding Video, Character Sheet / Turnaround, General Reference Plate, Poster / Static Design, Editorial / Magazine Image, Heritage / Historical Documentary, Product Still / Packshot, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually cannot be fixed by rerolling, because the same prompt reproduces the same failure. The exceptions that work are describing the grip explicitly, hiding the hand behind an object or a fold, or masking the region and repairing it alone.  
**Prompt:** `the right hand closes around the shaft with four fingers wrapped and the thumb across them, the left hand out of frame below the edge`  
**Yields to:** `kf.contact_points` — Describe the grip and contact explicitly.  
`rescue.hands`

### Crowd Faces Collapse

**Also called:** repeated faces, background face melt  
**What it is:** Secondary figures arrive with smeared, repeated or malformed faces, because the model spends its capacity on the principal subject and the crowd receives what is left.  
**Effect on the audience:** The scene fails on inspection. A viewer who looks past the foreground finds a field of wrong faces and stops believing the whole image.  
**Used for and where it works best:** Processions, markets, battles, audiences and any populated reconstruction. Best in heritage documentary and epic sequences.  
**Best in:** formats: Generated Keyframe Feeding Video, Heritage / Historical Documentary, Poster / Static Design, Documentary Feature, Brand Film, General Reference Plate, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: Heritage (civilisation-focused), Historical / Biopic, War, Mythology / Ancient Epic, Drama, Verite / Observational  
**Avoid when:** It usually worsens when the crowd is asked for in more facial detail, because the model spreads capacity instead of resolving faces. The fix is to make the crowd read, not to remove it: describe the figures by silhouette, posture and action rather than by face, give the crowd a single direction and a verb, and give each rank a distinct shape. Where full resolution is genuinely needed, generate the crowd as its own plate and composite it, or take the shot to an engine that holds crowds — an engine's weakness is a note for engine selection, never a reason to empty the frame. If the shot needs one readable face in the crowd, that is a second, tighter shot.  
**Prompt:** `forty figures on the terrace, all moving left toward the gate, spears at three different angles, three clear silhouette types — tall armoured, stooped bearers, robed priests — the two foreground figures fully resolved and the rest reading by posture and direction`  
**Yields to:** `comp.crowd_texture` — Let the crowd read by silhouette and direction.  
`rescue.faces_in_crowd`

### Text Comes Back Wrong

**Also called:** glyph salad, invented lettering  
**What it is:** Requested words return as plausible-looking but incorrect characters, with the failure worsening for longer strings and for non-Latin scripts.  
**Effect on the audience:** An error that survives review, because the shape looks right until someone actually reads it, which is usually after publication.  
**Used for and where it works best:** Any image carrying words, signage, packaging, posters and titles. Best applied in posters and product work.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Product Still / Packshot, Commercial / TVC, Title Sequence / Opening Credits, Editorial / Magazine Image, Heritage / Historical Documentary, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually cannot be corrected by rerolling, since the failure is structural. The exceptions, for a short Latin string, are quoting it exactly, describing the lettering as carved geometry, or setting the type as a layer afterwards, and whichever route is taken the result is read letter by letter before delivery; a non-Latin script takes `textimg.non_latin_script` — texture without legible content, or a typeset layer — whatever the description.  
**Prompt:** `no readable text in the generated plate; the wording will be typeset over it afterwards`  
**Yields to:** `textimg.repair_not_regenerate` — Set the wording as a layer, never reroll.  
`rescue.text_garble`

### Objects That Float

**Also called:** no contact, hovering props, missing ground  
**What it is:** Objects and figures sit slightly off their surface, without a contact shadow or with the wrong one, so nothing has weight.  
**Effect on the audience:** The image reads as a collage even when every element is individually convincing. Weight is carried entirely by the contact.  
**Used for and where it works best:** Product work, any object on a surface, and every figure standing, sitting or leaning. Best in product stills and keyframe plates.  
**Best in:** formats: Product Still / Packshot, Generated Keyframe Feeding Video, Props Sheet, General Reference Plate, Commercial / TVC, Poster / Static Design, Editorial / Magazine Image, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually persists through rerolls because the prompt never mentioned the ground. The exception is naming the contact explicitly, the shadow, the compression, the surface, which fixes it in one pass.  
**Prompt:** `the vessel rests on the stone with a tight dark contact shadow at its base, its weight visible where it meets the surface`  
**Yields to:** `material.contact_and_shadow` — Name the contact shadow and the surface.  
`rescue.floating_objects`

### Symmetry Drift

**Also called:** mismatched pairs, asymmetric duplication  
**What it is:** Things that should match do not: two eyes of different shape, two earrings of different design, two columns of different height, two sleeves cut differently.  
**Effect on the audience:** A quiet wrongness the viewer feels before finding. It is especially damaging in faces, where small mismatches read as uncanny rather than as character.  
**Used for and where it works best:** Portraits, architecture, costume with paired elements, and product work with symmetrical packaging. Best in character sheets and product stills.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, Product Still / Packshot, General Reference Plate, Poster / Static Design, Heritage / Historical Documentary, Editorial / Magazine Image, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually resists rerolling when the asymmetry comes from the pose rather than from the model. The exception is masking one side and regenerating it against the other, which forces the match.  
**Prompt:** `both earrings are identical in design and size, both columns the same height and spacing, the face symmetrical apart from the named scar`  
**Yields to:** `ai.inpaint_fix_keyframe` — Mask one side, regenerate against the other.  
`rescue.symmetry_drift`

### Scale Confusion

**Also called:** wrong size relationships, miniature effect  
**What it is:** Objects or architecture arrive at the wrong size relative to the figures, usually because no scale cue was given and the model chose one.  
**Effect on the audience:** A monumental building reads as a model, or a hand tool reads as furniture. The viewer cannot correct it because nothing in the frame tells them the truth.  
**Used for and where it works best:** Architectural and heritage reconstruction, any wide exterior, and any frame with no human figure for reference. Best in location sheets and heritage documentary.  
**Best in:** formats: Location Sheet / Master Plate, Generated Keyframe Feeding Video, Heritage / Historical Documentary, General Reference Plate, Travel / Real Estate / Hospitality, Poster / Static Design, Explainer, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Science / Educational, Adventure, Verite / Observational  
**Avoid when:** It usually persists when the correction only names dimensions in numbers, which the model does not measure. The exception is placing a known object in frame, a figure, a doorway, a brick course, which fixes the reading immediately.  
**Prompt:** `a standing figure at the base of the wall for scale, the brick courses at true hand-span height, the gateway three times the height of the figure`  
**Yields to:** `staging.scale_companion` — Put a known object in frame.  
`rescue.scale_confusion`

### Eyes and Gaze Failure

**Also called:** dead eyes, divergent gaze, missing catchlight  
**What it is:** The two eyes look in slightly different directions, or the eyes have no catchlight and read as flat, or the gaze does not land where the scene requires.  
**Effect on the audience:** The person appears absent. Gaze is the first thing a viewer reads in a face and the smallest error is immediately felt.  
**Used for and where it works best:** All portrait and character work, and any frame where a face is large enough to meet the viewer. Best in character sheets, portraits and keyframe plates.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Poster / Static Design, Editorial / Magazine Image, Brand Film, Thumbnail / Social Card, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually survives a reroll when the prompt never said where the eyes are looking. The exception is naming the target of the gaze and the catchlight source, which fixes both faults at once.  
**Prompt:** `both eyes fixed on the doorway at the left, a single small catchlight from the window in each eye at the same position, the gaze convergent`  
**Yields to:** `pose.eyeline_direction` — Name where the eyes land.  
`rescue.eye_failure`

### The Average Face

**Also called:** generic likeness, model default face  
**What it is:** Faces drift toward a symmetrical, youthful, conventionally attractive default whenever the description is general, regardless of what was asked for.  
**Effect on the audience:** Characters lose individuality and a cast begins to look related. It is the reason generated ensembles feel interchangeable.  
**Used for and where it works best:** All character work, particularly ensembles and any cast that should look like a real population. Best in character sheets and crowd plates.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Heritage / Historical Documentary, Poster / Static Design, Comics / Webtoon / Photo Essay, Editorial / Magazine Image, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually resists general instructions such as making a face more distinctive. The exceptions are naming specific structural features and at least one asymmetry or irregularity, which the default cannot absorb.  
**Prompt:** `a wide flat nose broken once and set slightly left, deep-set eyes with heavy lids, a receding chin, skin scarred across the right cheek, not a conventionally handsome face`  
**Yields to:** `ident.distinguishing_mark` — Give the face one specific irregularity.  
`rescue.average_face`

### Background Invention

**Also called:** unrequested detail, hallucinated setting  
**What it is:** The model fills unspecified areas with invented content, often anachronistic, which then has to be removed or accepted.  
**Effect on the audience:** Period work is contaminated by objects that did not exist, and product work gains competitors and clutter that were never briefed.  
**Used for and where it works best:** Heritage reconstruction, product work on clean grounds, and any image where the background must be controlled. Best in heritage documentary and product stills.  
**Best in:** formats: Heritage / Historical Documentary, Product Still / Packshot, General Reference Plate, Location Sheet / Master Plate, Generated Keyframe Feeding Video, Character Sheet / Turnaround, Poster / Static Design, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Verite / Observational, Science / Educational  
**Avoid when:** It usually continues when the background is simply left unmentioned, because silence is an invitation. The exception is describing the background positively, even if only as an empty ground, which removes the space for invention.  
**Prompt:** `the background is a plain mudbrick wall and nothing else: no windows, no vessels, no furniture, no vegetation, no people`  
**Yields to:** `staging.period_set_dressing` — Describe the background positively instead of leaving it silent.  
`rescue.background_invention`

### Count the Rerolls Before Spending

**Also called:** generation budget, reroll discipline  
**What it is:** Deciding in advance how many attempts an image is worth, and treating a third failure as a signal that the prompt is wrong rather than that the model is unlucky.  
**Effect on the audience:** Money and time stop disappearing into a plate that was never going to work. Three identical failures are information, not bad luck.  
**Used for and where it works best:** All paid generation, and especially long batches where a systematic fault multiplies across every image. Best in campaign and series production.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Thumbnail / Social Card, Product Still / Packshot, Character Sheet / Turnaround, Commercial / TVC, General Reference Plate, Portrait Photography, Street Photography, Food Photography, Architectural Photography, Still Life Photography, Wedding Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually stops too early on an image whose value genuinely justifies persistence, such as a hero frame. The exception is changing something specific between attempts rather than resubmitting the same prompt hoping for a different result.  
**Prompt:** `not a prompt line but a rule: after three failures of the same kind, change the prompt rather than the seed`  
**Yields to:** `ai.batch_and_select` — A hero frame whose value justifies persistence.  
`rescue.cost_before_reroll`
