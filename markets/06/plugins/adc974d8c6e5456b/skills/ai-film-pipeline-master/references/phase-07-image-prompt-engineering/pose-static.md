# Pose and Static Performance

16 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name Who the Pose Is For

**Also called:** the pose selector, address before attitude, who is this body talking to  
**What it is:** The card at the head of the `pose.` shelf. It does not describe a stance. It asks the three questions this shelf asks of itself over and over — **who is this body addressed to, how much of it is in the frame and which part is carrying it, and are you designing a pose or repairing one an engine handed you** — and hands back a named shortlist for each answer. The axes were read off the shelf's own escape conditions and off the boundary clause every card carries; they were not invented. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so the body that does reach the screen was placed against an address, a crop and a starting point, rather than posed the way bodies are usually posed.  
**Used for and where it works best:** Answer the three questions **out loud, in order, in one sentence each, before the figure is described**. The first eliminates two thirds of the shelf; the second and third leave a shortlist of two to four. Question three is the one people skip and it changes the answer completely: a pose you are designing and a pose you are rescuing are not the same problem, and three cards on this shelf each claim to be the first thing to reach for when a figure comes back stiff. **They are three different first fixes for three different symptoms, and this card routes them without ruling between them.**  
**Best in:** formats: all | genres: all  
**Avoid when:** **Two bodies are touching.** The shelf handles one figure, or three and more by head height, and it has nothing at all for a hand on a shoulder, a lean against another person or weight shared between two — so this map will confidently return a card for a problem it does not cover. Also **distrust the third value of axis two**, which holds only two cards: the moment the frame contains more than one person or a person and an object, this shelf sends you off it, and the map is thinner there than it looks. And **do not read the second axis as a crop instruction** — it says which part of the body is carrying the frame, which is a different question from how tight the lens is, and a card chosen on crop alone will fight the address chosen in question one.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Who is this body addressed to: an institution, the viewer, or nobody?**
Asked first, because formality is the condition this shelf repeats more than any other, and it is stated as fact rather than feeling. *"The meaning is rigidity: attention, formal address"* (`pose.weight_shift`), *"A character study needs a moment, not an announcement"* (`pose.hero_stance`), *"Every figure formal at once reads as a tableau"* (`pose.period_body_language`), *"A ceremonial occasion required the child to be still"* (`pose.child_pose_truth`), *"Formal group portrait where regularity is the convention"* (`pose.group_triangle`), *"The pose must stay closed: grief, cold, fear"* (`pose.negative_space_in_the_body`). **Four of the shelf's six internal pointers fire on exactly this**, which makes it the shelf's own spine: the body is either performing a rank, performing a relationship with whoever is looking, or being caught not performing at all.

**Axis 2 — How much of the body is in frame, and which part is carrying it?**
The second repeated condition, and the one the boundary clauses turn on: *"Offset too large to be comfortable; turn the eyes only"* (`pose.head_body_offset`), *"The lean crowds the head against the frame edge"* (`pose.seated_forward`), *"The push reads aggressive; take the jaw from camera height"* (`pose.chin_forward_down`), *"The thinker cliche; give the hand a specific job"* (`pose.hands_on_face_restraint`), and a silhouette that *loses its shape and reads as a blob at small size* (`pose.negative_space_in_the_body`). Each of these gives way not because the pose was wrong but because the wrong part of the body was doing the work at that distance.

**Axis 3 — Are you designing this pose, or repairing one that came back?**
Five cards describe themselves inside their own text as a correction to a figure an engine already produced: the default correction when a generated figure looks stiff (`pose.weight_shift`), the first fix when a generated figure looks uncomfortable (`pose.hands_have_a_job`), the cheapest single improvement to a stiff generated figure (`pose.the_small_asymmetry`), a common generated failure (`pose.child_pose_truth`), and the reason generated gazes so often land nowhere (`pose.eyeline_direction`). The remaining ten are written for a body that does not exist yet. Asked last because it is the only axis that changes which of two otherwise identical shortlists you should read.

---

**The map**

**Axis 1 — who the body is addressed to**

| Answer | The shortlist, by id |
| :--- | :--- |
| **An institution or an era — the body performs a rank, a period or a convention** | `pose.hero_stance` · `pose.period_body_language` · `pose.group_triangle` · `pose.child_pose_truth` |
| **The viewer — the body performs a relationship with whoever is looking** | `pose.eyeline_direction` · `pose.chin_forward_down` · `pose.seated_forward` · `pose.back_to_camera` · `pose.hands_on_face_restraint` |
| **Nobody — the body is caught being itself** | `pose.weight_shift` · `pose.head_body_offset` · `pose.negative_space_in_the_body` · `pose.hands_have_a_job` · `pose.action_arrested` · `pose.the_small_asymmetry` |

**Axis 2 — which part of the body is carrying the frame**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The whole figure, read as one shape at any size** | `pose.weight_shift` · `pose.hero_stance` · `pose.negative_space_in_the_body` · `pose.back_to_camera` · `pose.action_arrested` · `pose.period_body_language` · `pose.child_pose_truth` |
| **The head and whatever is near it** | `pose.chin_forward_down` · `pose.eyeline_direction` · `pose.head_body_offset` · `pose.hands_on_face_restraint` · `pose.the_small_asymmetry` · `pose.seated_forward` |
| **More than one body, or a body and an object** | `pose.group_triangle` · `pose.hands_have_a_job` |

**Axis 3 — designing or repairing**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Designing — no figure exists yet** | `pose.hero_stance` · `pose.group_triangle` · `pose.seated_forward` · `pose.back_to_camera` · `pose.action_arrested` · `pose.period_body_language` · `pose.head_body_offset` · `pose.hands_on_face_restraint` · `pose.chin_forward_down` · `pose.negative_space_in_the_body` |
| **Repairing — a figure came back stiff, blank or wrong** | `pose.weight_shift` · `pose.hands_have_a_job` · `pose.the_small_asymmetry` · `pose.child_pose_truth` · `pose.eyeline_direction` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally two to four cards wide.*

**Three cards claim to be the first fix, and this map routes them rather than ranking them.** `pose.weight_shift` is the only one that changes the spine, so it is first when the figure is standing and squared. `pose.hands_have_a_job` is the only one that changes the hands, so it is first when the hands are loose in the frame — which the package's own failure family calls the most persistent generated fault of all. `pose.the_small_asymmetry` changes one detail anywhere, so it is first when the figure is already anatomically correct and still reads synthetic. **Three symptoms, three fixes; the word *first* is doing no work in any of them.** The collision is recorded here and left open, because a superlative is not an axis and three cards cannot all be first.

---

**The default, and the one against it**

**In-degree is nearly silent on this shelf, and what it does say has to be read carefully.** No card here takes more than two inbound pointers from anywhere in the package. Two of the eight inbound edges start at named failures on the repair family — one telling a reader to name where the eyes land, one telling them to name the weight-bearing foot — and by the rule that every repair edge starts outside the map, those are instructions pointing in rather than routes across. Discount them and exactly one card is reached twice **on two genuinely different conditions from two different shelves**: `pose.the_small_asymmetry`, reached because a room of formally-held figures reads as a tableau, and reached again because a head at small scale cannot carry described hair and wants one named loose strand instead. **That is the shape of a fallback rather than a hatch, and it is the only one on the shelf.**

**The default is therefore `pose.weight_shift` under a named eyeline, with `pose.the_small_asymmetry` laid over the top.** The argument is not the count. It is that the weight shift is the only card here that changes the spine, which every other single-figure card on the shelf then sits on; that it is the only card the package reaches into this shelf for from another phase entirely; and that without a named eyeline the gaze lands nowhere, which the shelf says of itself. **And it is ordinary, which is the point of naming it.** Contrapposto is four centuries old, every stock portrait on earth is in it, and a shelf asked no questions will produce a relaxed standing figure with occupied hands and one strand of hair out of place, forever.

**The one against it is `pose.back_to_camera`, and the argument is that it removes the thing every other card here is protecting.** Fourteen cards on this shelf manage a face — lengthen its jaw, aim its eyes, keep a hand off it, stop it looking generated, offset it from the torso. This one deletes it, and by doing so it is the only card that cannot be compared with the rest on any axis they share. Nothing on the shelf routes to it; its only alternative lives on the lighting shelf, which means the shelf holds no in-family argument against it at all. And it turns the shelf's largest standing liability — a generated face — from a risk to be managed into the subject of the frame. Its cost is stated and finite: it withholds too much when the audience needs to know who this is, which a series pays off later by arriving at the face. Its near cousin against the grain is `pose.action_arrested`, likewise routed to by nothing here and likewise the only card that asks a still frame to carry a movement.

---

**The unasked**

**Seven of the fifteen cards are the target of no pointer anywhere in the package.** By id:

`pose.chin_forward_down` · `pose.negative_space_in_the_body` · `pose.seated_forward` · `pose.group_triangle` · `pose.back_to_camera` · `pose.hands_on_face_restraint` · `pose.child_pose_truth`

**And the shape of that list is the finding, not its length.** Every one of them belongs to an **occasion**: the headshot, the interview, the wedding or team portrait, the editorial thinking portrait, the heritage figure whose identity is deliberately unspecified, the child, the image that must survive at thumbnail size. Every card that *is* reached applies to any figure at all — a spine, a pair of eyes, a pair of hands, one detail out of place, a body that has stopped moving. **The pair graph on this shelf routes only between generic bodies. The moment a card belongs to a job, nothing sends anybody to it.** The readers who wrote these fields were each holding one anonymous figure, not a commission, and the pair field has no way to say *this is the right pose because of what the picture is for*. That is why the first axis on this card asks who the body is addressed to, and why it is asked first rather than not at all.

The second thing the list shows: **the whole region where two bodies touch is missing, not merely unasked.** One card handles three or more people by head height and immediately yields off the shelf when the occasion is formal; one card handles a body and an object. Between them there is nothing for a hand on a shoulder, a lean, an arm taken, a child carried, weight shared between two figures — the pose every portrait of a couple, a parent and child, or a pair of mourners needs. The nearest card records its own failure in its boundary clause, where regular height differences turn a group into a staircase, and nothing routes a reader there to read it. **The card this shelf wants is the one that says the pose is a decision made between two people, not one.**

`pose.address_before_attitude`

---

### Weight on One Leg

**Also called:** contrapposto, S-curve stance, weighted stance  
**What it is:** The body takes its weight on one leg so the hips tilt one way and the shoulders counter, producing an S through the spine instead of a vertical line.  
**Effect on the audience:** The figure reads as alive and at ease. A body squared with weight on both feet reads as standing to attention or as a shop mannequin.  
**Used for and where it works best:** Standing figures whose stiffness begins in the weight-bearing base. It is the first structural correction for the stance; after that, use `pose.hands_have_a_job` for idle hands and `pose.the_small_asymmetry` for an over-perfect surface.
**Best in:** formats: Portrait Photography, Fashion Photography, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Poster / Static Design, Heritage / Historical Documentary, Editorial / Magazine Image, Headshot, Wedding Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: all  
**Avoid when:** It usually works against a subject whose meaning is rigidity: a soldier at attention, a ruler in formal address, a figure in fear. The exception is a small weight shift that keeps the formality while removing the mannequin quality.  
**Prompt:** `weight carried entirely on the left leg, the right knee softened and turned slightly out, hips tilted left, shoulders countering right`  
**Yields to:** `pose.hero_stance` — The meaning is rigidity: attention, formal address.  
`pose.weight_shift`

### Head and Body on Different Axes

**Also called:** head turn, off-axis head, three-quarter body full-face head  
**What it is:** The torso faces one direction and the head turns toward another, usually toward the camera or toward what the subject is attending to.  
**Effect on the audience:** Attention becomes visible. The body says where the person was and the head says what caught them, which implies a moment rather than a pose.  
**Used for and where it works best:** Portraits that need to feel caught rather than arranged, character sheets, and any frame where the subject has just been interrupted. Best in portraits and keyframe plates.  
**Best in:** formats: Portrait Photography, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Editorial / Magazine Image, Fashion Photography, Poster / Static Design, Heritage / Historical Documentary, Headshot, Wedding Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: all  
**Avoid when:** It usually strains when the offset is large enough to look uncomfortable, which the viewer reads as a pose rather than a moment. The exception is deliberate tension, where the discomfort is the subject.  
**Prompt:** `torso turned three-quarters away to the right, head turned back toward camera, chin slightly down, eyes direct`  
**Yields to:** `pose.eyeline_direction` — Offset too large to be comfortable; turn the eyes only.  
`pose.head_body_offset`

### Chin Forward and Down

**Also called:** the push, jaw extension, portrait chin  
**What it is:** The subject pushes the chin slightly toward the camera and then lowers it a fraction, which lengthens the jawline and separates it from the neck.  
**Effect on the audience:** A defined jaw and no double chin, from any body type. It is the single most reliable portrait correction there is.  
**Used for and where it works best:** All portrait and headshot work, and any close frame where the jaw line matters. Best in headshots, portraits and beauty work.  
**Best in:** formats: Portrait Photography, Headshot, Beauty Photography, Character Sheet / Turnaround, Editorial / Magazine Image, Fashion Photography, Wedding Photography, Event Photography, Sports Photography, Documentary Photography | genres: all  
**Avoid when:** It usually reads as aggressive when the chin comes too far forward, which changes the character of the subject. The exception is a deliberately confrontational portrait, where the aggression is wanted.  
**Prompt:** `chin pushed slightly forward toward the lens then lowered a little, jawline separated from the neck, no compression under the chin`  
**Yields to:** `angle.slight_high` — The push reads aggressive; take the jaw from camera height.  
`pose.chin_forward_down`

### Give the Hands Something to Do

**Also called:** hand occupation, purposeful hands  
**What it is:** Placing the hands on, in or around something, a pocket, a tool, a sleeve, a rail, rather than leaving them hanging or floating in the frame.  
**Effect on the audience:** The hands stop being a problem and become information. Unoccupied hands are the most common reason a portrait looks awkward, and in generated images they are also the most likely to fail.  
**Used for and where it works best:** Standing and seated portraits where the awkwardness is specifically in an idle hand. Diagnose the body first: use `pose.weight_shift` for a rigid standing base, this card for unmotivated hands, and `pose.the_small_asymmetry` only after the structure works.
**Best in:** formats: Portrait Photography, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Editorial / Magazine Image, Poster / Static Design, Fashion Photography, Headshot, Wedding Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: all  
**Avoid when:** It usually clutters when the object is unrelated to the subject and reads as a prop handed to them. The exception is an object that carries story, which turns an awkward hand into a character detail.  
**Prompt:** `the left hand rests in the coat pocket with the thumb outside, the right hand closed around the strap at the shoulder`  
**Yields to:** `staging.props_earn_place` — The object must carry story, not be handed over.  
`pose.hands_have_a_job`

### Open the Gaps Inside the Figure

**Also called:** body negative space, arm separation  
**What it is:** Keeping small visible gaps between the arms and the torso, and between the legs, so the silhouette reads as a body rather than as a mass.  
**Effect on the audience:** The figure separates from itself and from the background. A silhouette with no internal gaps loses its shape and reads as a blob at small size.  
**Used for and where it works best:** Full-figure portraits, fashion, character sheets, and any image that must survive at thumbnail size. Best in fashion, character sheets and posters.  
**Best in:** formats: Fashion Photography, Character Sheet / Turnaround, Portrait Photography, Poster / Static Design, Thumbnail / Social Card, Editorial / Magazine Image, Generated Keyframe Feeding Video, Headshot, Wedding Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: all  
**Avoid when:** It usually fights a pose whose meaning is being closed: grief, cold, fear, self-protection. The exception is one small gap kept open, which preserves legibility without breaking the closure.  
**Prompt:** `a visible gap of light between the upper arm and the ribs on both sides, the feet apart so the legs read separately against the ground`  
**Yields to:** `light.backlight_rim` — The pose must stay closed: grief, cold, fear.  
`pose.negative_space_in_the_body`

### Seated and Leaning Forward

**Also called:** forward lean, engaged sitting, elbows on knees  
**What it is:** A seated subject brought forward from the back of the chair, weight on the forearms or elbows, spine angled toward the camera.  
**Effect on the audience:** Engagement and immediacy. A subject sitting back reads as withdrawn or as being interviewed; a subject leaning forward reads as talking to you.  
**Used for and where it works best:** Interview and editorial portraits, corporate and documentary work, and any seated frame that must not feel passive. Best in editorial portraits and documentary.  
**Best in:** formats: Portrait Photography, Editorial / Magazine Image, Documentary Photography, Headshot, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Fashion Photography, Wedding Photography, Event Photography, Sports Photography, Beauty Photography | genres: all  
**Avoid when:** It usually cramps the composition when the lean brings the head too close to the frame edge. The exception is a deliberately tight frame where the crowding is the point.  
**Prompt:** `seated forward on the edge of the chair, forearms on the thighs, hands loosely joined, spine angled toward the lens, shoulders down`  
**Yields to:** `comp.headroom` — The lean crowds the head against the frame edge.  
`pose.seated_forward`

### Decide Where the Eyes Go

**Also called:** gaze direction, eyeline choice  
**What it is:** Choosing deliberately whether the subject looks into the lens, just past it, at something inside the frame or out of it, and naming that choice.  
**Effect on the audience:** The relationship with the viewer is set by this one decision. Into the lens is address, past it is thought, out of frame is elsewhere.  
**Used for and where it works best:** Every portrait and character image. It is also the most common unstated decision, which is why generated gazes so often land nowhere. Best in portraits and keyframe plates.  
**Best in:** formats: Portrait Photography, Headshot, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Editorial / Magazine Image, Poster / Static Design, Documentary Photography, Fashion Photography, Wedding Photography, Event Photography, Sports Photography, Beauty Photography | genres: all  
**Avoid when:** It usually weakens a direct-address portrait when the eyes drift a few degrees off the lens, which reads as evasion rather than as thought. The exception is a deliberate near-miss, which is a recognised device for discomfort.  
**Prompt:** `eyes directly into the lens, both pupils converging on the camera, nothing else in the frame competing for the gaze`  
`pose.eyeline_direction`

### Build Groups in Triangles

**Also called:** group staging, head-height variation  
**What it is:** Arranging several people so their heads sit at different heights and form triangular relationships rather than a straight row.  
**Effect on the audience:** The group reads as people who know each other rather than as a queue. Equal head heights flatten a group into a line.  
**Used for and where it works best:** Family, team, wedding and cast portraits, and any frame with three or more people. Best in event, wedding and editorial work.  
**Best in:** formats: Portrait Photography, Wedding Photography, Event Photography, Editorial / Magazine Image, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Poster / Static Design, Headshot, Fashion Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: all  
**Avoid when:** It usually looks arranged when the height differences are too regular, producing a staircase. The exception is a formal group portrait where the regularity is the convention.  
**Prompt:** `five figures with no two heads at the same height, the tallest set back at the left, two seated forward at the right, the group reading as overlapping triangles`  
**Yields to:** `frame.group_shot` — Formal group portrait where regularity is the convention.  
`pose.group_triangle`

### The Arrested Action

**Also called:** frozen motion, the moment of stillness inside movement  
**What it is:** Posing the body at the top or the end of a movement, where a real body would naturally pause, rather than in the middle of a swing.  
**Effect on the audience:** Motion implied without blur. The viewer reconstructs the movement from the frozen instant, which is stronger than seeing it.  
**Used for and where it works best:** Sports, dance, action and heritage reconstruction, and any still that must suggest movement. Best in sports, dance and keyframe plates.  
**Best in:** formats: Sports Photography, Generated Keyframe Feeding Video, Fashion Photography, Poster / Static Design, Editorial / Magazine Image, Heritage / Historical Documentary, Portrait Photography, Headshot, Wedding Photography, Event Photography, Beauty Photography, Documentary Photography | genres: Action, Sports Drama, War, Adventure, Musical, Historical / Biopic, Heritage (civilisation-focused)  
**Avoid when:** It usually reads as a stumble when the arrest lands mid-stride, because a body caught between steps has no stable reading. The exception is deliberate instability, where the fall is the subject.  
**Prompt:** `caught at the top of the throw, arm fully extended, weight forward on the front foot, the body still for the instant before release`  
**Yields to:** `photo.panning` — Continuous motion mid-stride; carry it with blur.  
`pose.action_arrested`

### Restraint With Hands Near the Face

**Also called:** face-touching, thoughtful hands  
**What it is:** Bringing a hand toward the face for thought or emotion, while keeping the hand from covering the features that carry the expression.  
**Effect on the audience:** Interiority. A hand near the face signals thinking, but a hand across it removes the performance the frame exists for.  
**Used for and where it works best:** Editorial and thoughtful portraits, biography and documentary work. Best in editorial portraits.  
**Best in:** formats: Portrait Photography, Editorial / Magazine Image, Headshot, Documentary Photography, Generated Keyframe Feeding Video, Beauty Photography, Fashion Photography, Wedding Photography, Event Photography, Sports Photography | genres: Drama, Historical / Biopic, Psychological / Arthouse, Tragedy, Romance, Verite / Observational  
**Avoid when:** It usually becomes a cliche when the chin rests on the knuckles in the standard thinker position. The exception is a hand doing something specific, adjusting glasses, touching a scar, which is a gesture rather than a pose.  
**Prompt:** `the right hand raised to the jaw with the fingers below the cheekbone, not covering the mouth or the eyes, the expression fully visible`  
**Yields to:** `pose.hands_have_a_job` — The thinker cliche; give the hand a specific job.  
`pose.hands_on_face_restraint`

### Turned Away From Camera

**Also called:** the back view, anonymous figure  
**What it is:** Placing the subject with their back or three-quarter back to the lens, so the figure carries the frame without a face.  
**Effect on the audience:** The viewer projects themselves into the figure rather than reading a specific person. It also removes every face-related generation risk in one decision.  
**Used for and where it works best:** Heritage work where identity is deliberately unspecified, travel and landscape images with a figure, and any frame where a face would be a liability. Best in heritage documentary and travel.  
**Best in:** formats: Heritage / Historical Documentary, Travel Photography, Landscape Photography, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Editorial / Magazine Image, Portrait Photography, Headshot, Fashion Photography, Wedding Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Adventure, Tragedy, Mythology / Ancient Epic, Nature / Wildlife  
**Avoid when:** It usually withholds too much when the piece needs the audience to know who this is. The exception is a series where the face arrives later, and the withholding builds toward it.  
**Prompt:** `the figure seen from behind at three-quarter angle, head turned just enough to show the jaw line, face not visible`  
**Yields to:** `light.hidden_faces` — The figure must face camera but the face is a liability.  
`pose.back_to_camera`

### Period-Truthful Body Language

**Also called:** historical posture, era-specific gesture  
**What it is:** Posing the body the way the period and culture actually held itself, in its own conventions of deference, address, rest and formality, rather than in modern casual posture.  
**Effect on the audience:** The reconstruction survives inspection. Modern posture on period clothing is the fastest way a careful heritage image reads as costume.  
**Used for and where it works best:** All heritage and historical reconstruction, museum and exhibition work. Best in heritage documentary and historical drama plates.  
**Best in:** formats: Heritage / Historical Documentary, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Poster / Static Design, Editorial / Magazine Image, Documentary Photography, Portrait Photography, Headshot, Fashion Photography, Wedding Photography, Event Photography, Sports Photography, Beauty Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, War, Tragedy  
**Avoid when:** It usually stiffens the image when every figure holds a formal attitude at once, which reads as a tableau. The exception is a formal occasion where the tableau is historically correct.  
**Prompt:** `standing in the posture of the period, arms held close and hands crossed at the waist, shoulders squared, chin level, no modern relaxed slouch`  
**Yields to:** `pose.the_small_asymmetry` — Every figure formal at once reads as a tableau.  
`pose.period_body_language`

### Children Posed as Children

**Also called:** child body language, unposed child  
**What it is:** Letting a child figure hold a child posture, weight uneven, limbs loose, attention elsewhere, rather than a scaled-down adult pose.  
**Effect on the audience:** The child reads as a child. Adult posture on a small body is immediately wrong and is a common generated failure.  
**Used for and where it works best:** Family, kids content, heritage work with families, and any image with a young figure. Best in kids content and family portraits.  
**Best in:** formats: Kids Content, Portrait Photography, Wedding Photography, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Editorial / Magazine Image, Poster / Static Design, Headshot, Fashion Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: Family, Preschool / Early Learning, Fairy Tale, Slice of Life, Drama, Heritage (civilisation-focused)  
**Avoid when:** It usually loses formality where the occasion genuinely required a child to be still, such as a ceremonial portrait. The exception is a child holding formality imperfectly, which is both truthful and more affecting.  
**Prompt:** `a child standing with weight on one foot and the other turned inward, one shoulder higher, attention on something outside the frame, not posed for the camera`  
**Yields to:** `pose.period_body_language` — A ceremonial occasion required the child to be still.  
`pose.child_pose_truth`

### The Hero Stance

**Also called:** key art pose, power stance  
**What it is:** A frontal or near-frontal stance with weight low and even, shoulders open, head level, occupying the maximum silhouette the frame allows.  
**Effect on the audience:** Authority and arrival. It is the pose of key art because it reads instantly at any size and from any distance.  
**Used for and where it works best:** Posters, key art, campaign and title work, and any image whose job is announcement. Best in posters and campaign work.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Generated Keyframe Feeding Video, Title Sequence / Opening Credits, Fashion Photography, Sports Photography, Brand Film, Portrait Photography, Headshot, Wedding Photography, Event Photography, Beauty Photography, Documentary Photography | genres: Action, Fantasy / Epic, Superhero, War, Adventure, Sports Drama, Mythology / Ancient Epic  
**Avoid when:** It usually flattens a character study, because a pose built for legibility removes ambiguity. The exception is a hero stance undercut by the face, where the body claims one thing and the expression admits another.  
**Prompt:** `frontal stance, feet apart at shoulder width, weight low and even, shoulders open and square, head level, filling the vertical of the frame`  
**Yields to:** `pose.head_body_offset` — A character study needs a moment, not an announcement.  
`pose.hero_stance`

### One Thing Out of Place

**Also called:** imperfection, humanising detail  
**What it is:** Introducing one small deliberate irregularity into an otherwise controlled pose: a loose strand, a rolled sleeve, a shirt not quite straight, a hand slightly turned.  
**Effect on the audience:** The image stops looking generated. Perfect symmetry and perfect arrangement are the strongest signals of synthesis in a composed figure — on a close face, smooth skin is (`material.skin_surface`) — and one irregularity defeats both.  
**Used for and where it works best:** Controlled portraits and character images whose stance and hands already work but whose surface arrangement looks synthetic: it is the cheapest finishing correction to a stiff generated figure, not a substitute for fixing the stance or the hands; where the stiffness is the whole standing body held in a vertical line, `pose.weight_shift` is the first fix, and where it is hands left hanging, `pose.hands_have_a_job` is. Best across all still portrait work.  
**Best in:** formats: Portrait Photography, Character Sheet / Turnaround, Generated Keyframe Feeding Video, Editorial / Magazine Image, Fashion Photography, Heritage / Historical Documentary, Poster / Static Design, Headshot, Wedding Photography, Event Photography, Sports Photography, Beauty Photography, Documentary Photography | genres: all  
**Avoid when:** It usually reads as sloppiness when several irregularities appear at once and the image looks unfinished rather than alive. The exception is deliberate dishevelment, where the state of the subject is the story.  
**Prompt:** `everything composed and controlled except one detail: the left collar turned under, and a single strand of hair fallen across the temple`  
`pose.the_small_asymmetry`
