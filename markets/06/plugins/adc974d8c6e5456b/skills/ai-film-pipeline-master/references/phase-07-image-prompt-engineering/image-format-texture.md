# Image Format and Texture

64 cards. Also in the other stage: a shot has a frame too. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Settle the Frame Before the Shot

**Also called:** the format selector, the three settlements, container before material before motion
**What it is:** The card at the head of the `look.` shelf. It does not describe a texture. It asks the three questions the shelf's own pair graph asks over and over — **which of the three settlements you are making, what the frame claims to have been recorded on, and whether it governs every frame or is a dose** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the fifty-two `Yields to:` conditions the cards carry and the rows `PAIR-AUDIT.md` files for the eleven that carry none. Every card cited here is cited by id.
**Effect on the audience:** None. This card never reaches the screen. It exists so that the container, the material and the motion were each settled against the subject, the claim and the clock, rather than inherited whole from the last project.
**Used for and where it works best:** **Answer question one first, and answer it three times.** This shelf is not one decision. Its own pair graph runs forty-six edges between its own cards and **not one of them crosses** between the container, the material and the motion — nothing here ever offers a stock as an alternative to a frame shape, or a rate as an alternative to a stock. So question one is not a filter, it is a fork, and you walk it three times in one sitting: what shape is the frame, what is the image made of, how does it move. Then answer two and three inside the settlement you are on; they leave a shortlist of two to nine. Where question three's honest answer is *a dose*, you have two states of the piece, and the other state is whatever you settled for the rest of it.
**Best in:** formats: all | genres: all
**Avoid when:** **The container question is a ladder, not a fork, and this map cannot climb it.** Ask it and you get the widest cell on the shelf, and the other two axes will not cut it further, because the shape region's pair graph runs one way only — downhill, toward the middle — and `look.ratio_scope` sits at the foot of seven of those runs. On *which ratio*, this map can tell you when the frame you are holding is wrong and it cannot tell you which to take instead; the two things that actually decide it, the shape of the subject and the surface it plays on, live in the cards' own `Avoid when:` lines and in no axis here. Also avoid it **on a single still** — a poster, a keyframe, a cover — where question three has no meaning at all and the map is down to two questions. And avoid it **when the deliverable already names the spec**: a broadcast master, a platform master, a shot matched to an existing plate. There the container and the rate are measured off the deliverable rather than chosen from a shelf, and `look.interlaced` says so in its own `Avoid when:`.
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Which of the three settlements is this: the container, the material, or the motion?**
Asked first because the shelf's own map says it must be. Forty-six of its `Yields to:` fields point at another card on this shelf, and every single one stays inside one of the three regions: `look.ratio_276` yields to `look.ratio_200`, `look.imax_1570` to `look.film_65_70`, `look.fps_120` to `look.hfr_48`, and nothing anywhere crosses a region line. Six more fields leave the shelf entirely — `look.ratio_switch` to `color.flashback_tint`, `look.letterbox` to `vertical.reframe_169`, `look.black_white` to `color.accent`, `look.vhs` and `look.light_leak` and `look.datamosh` into the `trans.` family — and not one of those crosses either. A family whose regions never cite each other is not one decision. It is three, made at one sitting and locked before the first frame.

**Axis 2 — What does the frame claim to have been recorded on, and must the rest of the shot stay consistent with it?**
Nineteen conditions turn on this and they are stated as facts, not feelings: *"The scene is set today"* (`look.kodachrome`), *"The subject is past the collodion era"* (`look.wet_plate`), *"The photograph predates instant film"* (`look.polaroid`), *"A contemporary piece, where ortho reads as a mistake"* (`look.orthochromatic`), *"The home recording belongs to the tape era"* (`look.film_super8`), *"The screen inside the story is modern, not a tube"* (`look.crt_scanlines`), *"No convincing reason for a character to keep filming"* (`look.found_footage`), *"The watcher is a machine or predator, not human"* (`look.night_vision`) and its exact reverse in `look.thermal`, *"Period scenes and memory, where cleanliness works against you"* (`look.digital_cinema`). The three values are the three answers the cards themselves give: a real technology, somebody's device inside the story, or nothing at all.

**Axis 3 — Does it govern every frame, or is it a dose?**
The question this shelf was expected to be shaped by, and it is not the first one — it is the third, and it is the only axis that reaches the overlay cards at all. Seventeen conditions are about duration and mixing rather than look: *"The whole piece is shot on the phone"* (`look.phone_footage`), *"The whole piece is narrow; commit, do not column it"* (`look.pillarbox`), *"The change marks two time periods, not one release beat"* (`look.letterbox_reveal`), plus the `Avoid when:` lines that say it outright — *do not run it through the whole video* (`look.fake_letterbox`), *keep it short, a minute is plenty* (`look.film_super8`), *used for a whole piece it stops working as a signal* (`look.phone_footage`), *held for a long sequence it tires the eye* (`look.sepia`), *use it in doses* (`look.shutter_45`), *held long it becomes exhausting* (`look.shutter_360`), *do not intercut it with twenty four frame material inside one scene* (`look.fps_60`), *mixing rates in one timeline produces stuttering motion* (`look.fps_25_30`), *do not repeat it, once in a piece is enough* (`look.letterbox_reveal`).

---

**The map**

**Axis 1 — which settlement**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The container — what shape the frame is, and what is laid over it** (nineteen) | `look.ratio_119` · `look.ratio_133` · `look.ratio_137` · `look.ratio_143` · `look.ratio_166` · `look.ratio_178` · `look.ratio_185` · `look.ratio_200` · `look.ratio_220` · `look.ratio_scope` · `look.ratio_276` · `look.ratio_square` · `look.ratio_4x5` · `look.ratio_9x16` · `look.ratio_switch` · `look.letterbox` · `look.pillarbox` · `look.fake_letterbox` · `look.letterbox_reveal` |
| **The material — what the image is made of** (twenty-eight) | `look.film_35mm` · `look.film_16mm` · `look.film_super8` · `look.film_65_70` · `look.imax_1570` · `look.digital_cinema` · `look.shot_on_iphone` · `look.light_leak` · `look.vhs` · `look.crt_scanlines` · `look.interlaced` · `look.cctv` · `look.phone_footage` · `look.found_footage` · `look.screenlife` · `look.actioncam` · `look.night_vision` · `look.thermal` · `look.datamosh` · `look.black_white` · `look.orthochromatic` · `look.sepia` · `look.technicolor` · `look.kodachrome` · `look.polaroid` · `look.wet_plate` · `look.hand_cranked` · `look.hdr_sdr` |
| **The motion — how fast it is captured and how long the shutter stays open** (eight) | `look.fps_24` · `look.fps_25_30` · `look.hfr_48` · `look.fps_60` · `look.fps_120` · `look.shutter_180` · `look.shutter_45` · `look.shutter_360` |

**Axis 2 — what the frame claims**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A real camera, stock, process or release format, and the rest of the shot has to obey it** (thirty) | `look.ratio_119` · `look.ratio_133` · `look.ratio_137` · `look.ratio_143` · `look.ratio_166` · `look.ratio_220` · `look.ratio_276` · `look.ratio_scope` · `look.letterbox` · `look.pillarbox` · `look.fake_letterbox` · `look.film_35mm` · `look.film_16mm` · `look.film_super8` · `look.film_65_70` · `look.imax_1570` · `look.shot_on_iphone` · `look.light_leak` · `look.vhs` · `look.crt_scanlines` · `look.interlaced` · `look.technicolor` · `look.kodachrome` · `look.polaroid` · `look.wet_plate` · `look.orthochromatic` · `look.hand_cranked` · `look.sepia` · `look.fps_25_30` · `look.fps_60` |
| **A device belonging to somebody inside the story — the frame is their footage** (seven) | `look.cctv` · `look.phone_footage` · `look.found_footage` · `look.screenlife` · `look.actioncam` · `look.night_vision` · `look.thermal` |
| **Nothing — the image makes no claim about how it was made** (eighteen) | `look.ratio_178` · `look.ratio_185` · `look.ratio_200` · `look.ratio_square` · `look.ratio_4x5` · `look.ratio_9x16` · `look.ratio_switch` · `look.letterbox_reveal` · `look.digital_cinema` · `look.black_white` · `look.datamosh` · `look.hdr_sdr` · `look.fps_24` · `look.hfr_48` · `look.fps_120` · `look.shutter_180` · `look.shutter_45` · `look.shutter_360` |

**Axis 3 — does it govern, or is it a dose**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A dose — a beat, an insert, a section, and the piece returns to something else afterwards** (twenty) | `look.ratio_switch` · `look.letterbox_reveal` · `look.pillarbox` · `look.fake_letterbox` · `look.film_super8` · `look.light_leak` · `look.vhs` · `look.crt_scanlines` · `look.interlaced` · `look.cctv` · `look.phone_footage` · `look.actioncam` · `look.night_vision` · `look.thermal` · `look.datamosh` · `look.sepia` · `look.polaroid` · `look.hand_cranked` · `look.shutter_45` · `look.shutter_360` |
| **It governs — settled before the first shot, and it survives every reverse, every cut and the whole running time** (thirty-five) | Every other card named in the two tables above. It is named by complement on purpose: naming thirty-five ids here would make the map longer than the shelf, which is the one thing the template forbids. |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it runs from two cards wide to nine — except under the container's first value, where it does not narrow at all and the warning above applies.*

---

**The default, and the one against it**

**The default is the whole third column: `look.ratio_185` for the container, `look.digital_cinema` for the material, `look.fps_24` with `look.shutter_180` for the motion — the four cards that sit under *makes no claim* and *governs*. Each of them is measured, not asserted.**

`look.ratio_scope` is the most-yielded-to card on the shelf by a wide margin — seven cards send a reader to it, more than twice anything else. **It is not the default, and counting edges is how you would get that wrong.** Count the distinct conditions instead and the seven collapse to two: *the scene is horizontally wide* (`look.ratio_119`, `look.ratio_133`, `look.ratio_square`) and *the piece wants a cinema register rather than neutrality* (`look.ratio_178`, `look.ratio_185`, `look.ratio_200`, `look.ratio_220`). Seven doors, two reasons — that is the shelf's widest exit, not its floor. And scope itself yields back, to `look.ratio_185`, whenever the scene is built on something vertical. `look.ratio_185` is reached twice on two genuinely unlike conditions — *no reason to differ, pick the familiar one* from `look.ratio_166`, and *a scene built on a vertical* from scope — and one of those two comes from the card everything else runs to. `look.digital_cinema` is the clearest of the four: three inbound edges on three unrelated grounds, register (`look.film_35mm` — *explainer and corporate work, where film adds nothing*), production reality (`look.shot_on_iphone` — *low-light work, where phone processing ruins skin*) and period (`look.kodachrome` — *the scene is set today*). `look.fps_24` takes three inbound edges and nothing on the rate ladder yields away from it, and `look.shutter_180` is the only card on the shelf whose own text calls itself the baseline.

**The one against it is `look.ratio_119`.** Nothing routes to it; it is named by no `Yields to:` anywhere on the shelf; and it is the only container card that runs against the whole region's direction of travel. Every other narrow frame is a rung on a ladder that slides toward the middle, and that gradient is one-way — `look.ratio_119` yields outward to scope and scope never yields back. Choosing it is choosing the single direction the shelf's own graph will not recommend, and the reason to is exactly the reason nothing recommends it: a frame with no lateral escape in it is the only frame that can make a room feel like a cell. Its stated cost is narrow and specific — it is *useless for any scene with breadth, a crowd or wide architecture*, and on a phone the picture ends up tiny — so a piece with no breadth in it and no phone delivery pays nothing at all. Its cousin against the grain is `look.shutter_360`, likewise yielded to by nothing, which inverts the entire motion region: every other card there buys clarity, and this one destroys it on purpose and admits in its own `Avoid when:` that the smear has to be the information or the shot cannot be read.

---

**The unasked**

**Twenty-eight of the fifty-five reachable cards are the target of no `Yields to:` field anywhere on this shelf.** They can be chosen but nothing ever sends you to them. By id:

`look.ratio_119` · `look.ratio_137` · `look.ratio_143` · `look.ratio_166` · `look.ratio_220` · `look.ratio_276` · `look.ratio_square` · `look.letterbox` · `look.pillarbox` · `look.fake_letterbox` · `look.letterbox_reveal` · `look.film_super8` · `look.imax_1570` · `look.light_leak` · `look.crt_scanlines` · `look.interlaced` · `look.cctv` · `look.found_footage` · `look.actioncam` · `look.datamosh` · `look.sepia` · `look.technicolor` · `look.polaroid` · `look.hand_cranked` · `look.fps_25_30` · `look.fps_120` · `look.shutter_360` · `look.hdr_sdr`

**And the shape of that list is the finding, not its length. Every end of every ladder is on it.** The narrowest container `look.ratio_119`, the widest `look.ratio_276`, the largest negative `look.imax_1570`, the highest rate `look.fps_120`, the longest shutter `look.shutter_360` — each of them yields *inward*, toward the middle of its own region, and nothing yields back out. The pair graph is a gradient with one direction. **A reader holding a moderate answer will never be sent to an extreme; this shelf can talk you out of one and has no way of talking you into one.** That is not a gap in the fields, it is what a pair field is: it was written by a reader asking *where does my card stop*, and an extreme stops everywhere except the single place it was chosen for, so its neighbours have no condition under which they would hand it over.

**The second thing the list shows: all four overlay cards are on it** — `look.letterbox`, `look.pillarbox`, `look.fake_letterbox`, `look.letterbox_reveal`. Nothing on this shelf ever says *instead of choosing a container, lay one over the one you have*. They are arrivals from the delivery, and a graph of choices has no entrance for a repair. **And three cards are isolated points, reached by nothing and reaching nothing**: `look.cctv`, `look.actioncam` and `look.hdr_sdr` carry no pair field in either direction.

**The card this shelf wants is a material that changes while the piece runs.** The container region has two — `look.ratio_switch` and `look.letterbox_reveal` — and the map reaches both. The material region has none, and it does not merely lack one: it **exports** its only two changes off the shelf. `look.light_leak` and `look.datamosh` both yield into the `trans.` family, so the moment a material stops holding still, this shelf hands it to the cut. Nothing here says *the tape is wearing out as we watch*, *the stock runs short in the middle of the take*, *the image coarsens across the third act* — a material with a direction rather than a value. The nearest thing that exists is `look.dust_scratches`, and `PAIR-AUDIT.md` files it `additive`, which means by construction it can never be an alternative to anything, only a layer over whatever you already chose.

`look.settle_before_the_shot`

---

### 1.19:1

**Also called:** Movietone ratio, early sound ratio  
**What it is:** An almost square frame, marginally wider than it is tall, inherited from the first sound films when the optical track ate part of the picture width. It is the narrowest ratio cinema has genuinely used.  
**Effect on the audience:** It suffocates. The character is jammed into a narrow column with no visual escape left anywhere in frame.  
**Used for and where it works best:** Psychological horror, madness and isolation, the lighthouse, the cell, the room with no horizon in it. Ideal when you want a period register that feels older than black and white itself.  
**Best in:** formats: Feature Film, Short Film, Experimental / Art Film, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography, Night and Astrophotography | genres: Psychological Horror, Horror, Gothic / Vampire, Tragedy, Historical / Biopic, Surreal / Absurdist, Drama  
**Avoid when:** It is useless for any scene with breadth, a crowd or wide architecture. On a phone the picture ends up tiny.  
**Prompt:** `framed in a narrow 1.19:1 aspect ratio, tall boxed composition, vertical black bars on both sides, claustrophobic`  
**Example:** The Lighthouse (2019), shot in 1.19:1.  
**Yields to:** `look.ratio_scope` — Scene has breadth, a crowd or wide architecture.  
`look.ratio_119`

### 4:3 / 1.33:1

**Also called:** full frame, silent ratio, classic television ratio  
**What it is:** The classic frame of silent cinema and later of television. Only slightly wider than it is tall, so it leans vertical compared with any modern cinema ratio.  
**Effect on the audience:** It brings the viewer close to the human body: a standing or seated figure fills it naturally. It also carries archive and memory.  
**Used for and where it works best:** The flashback and the older period inside a modern film, plus the intimate drama that follows one person from behind the shoulder. Very strong in heritage documentary when you present real archive material in its own ratio rather than stretching it.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Drama Series Episode, Short Film, Video Essay, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Coming of Age, Psychological / Arthouse, Tragedy, Verite / Observational, Family  
**Avoid when:** On an epic wide scene it strangles the image and costs you the horizon. On a widescreen display it leaves big black columns at the sides.  
**Prompt:** `4:3 aspect ratio, boxy vertical leaning frame, single figure filling the height, archival feeling`  
**Yields to:** `look.ratio_scope` — Epic wide scene; 4:3 costs you the horizon.  
`look.ratio_133`

### Academy Ratio 1.37:1

**Also called:** Academy, 1.37, classic sound ratio  
**What it is:** The standard of pre widescreen sound cinema once the optical track was added. It feels like 4:3 but carries an explicit cinema history: this is the shape of films from the thirties to the fifties.  
**Effect on the audience:** Formality and seriousness. The narrow frame forces vertical, disciplined composition and brings faces closer.  
**Used for and where it works best:** The contemporary film that deliberately chooses a classical shape: a story of faith, a portrait of a single life, a drama about a man boxed in by his own morality. Ideal when you want the viewer to feel they are watching a film, not content.  
**Best in:** formats: Feature Film, Short Film, Limited Series, Title Sequence / Opening Credits, Experimental / Art Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography | genres: Drama, Faith / Biblical Epic, Tragedy, Historical / Biopic, Psychological / Arthouse, Gothic / Vampire, Coming of Age, Mystery / Whodunit  
**Avoid when:** When the piece needs landscape or horizontally spreading action. On vertical platforms it offers nothing that 4:3 does not.  
**Prompt:** `Academy ratio 1.37:1, vertical disciplined composition, classic film framing, centred figure`  
**Example:** First Reformed (2017), presented in 1.37:1.  
**Yields to:** `look.ratio_133` — Vertical platforms, where Academy adds nothing over 4:3.  
`look.ratio_137`

### IMAX 1.43:1

**Also called:** IMAX full frame, 15/70 ratio  
**What it is:** The ratio of the true IMAX photographic frame: exceptionally tall compared with any other cinema shape. On a real IMAX screen it fills the viewer's entire field of view.  
**Effect on the audience:** It abolishes the edges of the screen. The viewer feels inside the place rather than looking at it, because the frame reaches past their peripheral vision.  
**Used for and where it works best:** The overwhelming shots: flight, mountain, monument from above, the vast hall, the wide detonation. It is normally used as sequences inside a film shot at another ratio, so the jump in scale becomes an event in itself.  
**Best in:** formats: Feature Film, Documentary Feature, Trailer / Teaser, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography | genres: Adventure, Sci-Fi, War, Historical / Biopic, Heritage (civilisation-focused), Nature / Wildlife, Disaster, Space Opera, Action  
**Avoid when:** On a television or a phone it means nothing, the difference simply disappears. In interior dialogue it adds nothing worth its cost.  
**Prompt:** `IMAX 1.43:1 tall frame, immersive scale, enormous landscape filling the full height of the image`  
**Example:** Oppenheimer (2023), the IMAX 1.43:1 sequences.  
**Yields to:** `look.ratio_178` — Delivery is television or phone, not a giant screen.  
`look.ratio_143`

### 1.66:1

**Also called:** European widescreen, Super 16 ratio  
**What it is:** A European shape sitting between Academy and standard flat. It gives enough width without giving up height, and it is the native ratio of Super 16.  
**Effect on the audience:** Intimacy with room to breathe. It reads as more interested in the person than in the landscape.  
**Used for and where it works best:** European drama, short film and hand drawn animation, and the scene where a standing figure needs both ceiling and floor in frame. Right when you want a cinema shape without the epic tone of scope.  
**Best in:** formats: Feature Film, Short Film, 2D Animation (Western / Cartoon), Drama Series Episode, Documentary Feature, Experimental / Art Film, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Coming of Age, Slice of Life, Romance, Tragedy, Family, Psychological / Arthouse, Fairy Tale  
**Avoid when:** Most viewers will not read it as different from 1.85, so without a reason pick the familiar one. On streaming platforms it ends up pillarboxed.  
**Prompt:** `1.66:1 aspect ratio, slightly taller than standard widescreen, intimate room framing with ceiling and floor both visible`  
**Example:** Barry Lyndon (1975), composed for 1.66:1.  
**Yields to:** `look.ratio_185` — No reason to differ; pick the familiar one.  
`look.ratio_166`

### 16:9 / 1.78:1

**Also called:** HD ratio, widescreen television, YouTube ratio  
**What it is:** The standard widescreen shape of television, YouTube and every display. Almost every camera and every platform treats it as the default.  
**Effect on the audience:** Total neutrality. It says nothing about itself, so the viewer attends to the content rather than the frame.  
**Used for and where it works best:** Television, YouTube, explainers, corporate work and documentary destined for screens, plus anything that must play uncropped. Choose it when reach matters more than style and when the viewing happens on a small screen.  
**Best in:** formats: Drama Series Episode, Documentary Feature, Documentary Series, Explainer, Corporate / Training, Vlog / YouTube Long-Form, News Report / Reportage, Interview / Video Podcast, Game Cinematic / Gameplay, Sports Broadcast / Sports Film, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography | genres: Science / Educational, Verite / Observational, Drama, Comedy, Family, Sports Drama, True Crime, Political Thriller  
**Avoid when:** If the goal is a distinctive cinematic feel, 16:9 gives you no signature. In a vertical feed it lands as a small strip in the middle.  
**Prompt:** `16:9 widescreen frame, clean neutral composition, standard television and streaming format`  
**Yields to:** `look.ratio_scope` — You want a distinctive cinematic signature, not neutrality.  
`look.ratio_178`

### 1.85:1

**Also called:** flat, US widescreen, theatrical flat  
**What it is:** The standard American flat cinema ratio: a touch wider than 16:9 and far shorter than scope. Most drama, comedy and feature animation is shot in it.  
**Effect on the audience:** Cinema without a claim. It delivers a film shape while keeping enough height for the human body and for architecture.  
**Used for and where it works best:** Drama, comedy, horror and family animation, and any scene where vertical elements matter: trees, columns, doorways, a standing figure. Right when the piece must play in a cinema and at home.  
**Best in:** formats: Feature Film, Short Film, 2D Animation (Western / Cartoon), 3D CG Animation, Drama Series Episode, Stop Motion, Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Comedy, Horror, Family, Fairy Tale, Coming of Age, Romance, Mystery / Whodunit, Fantasy / Epic  
**Avoid when:** It will not give you the epic register scope delivers. On vertical platforms it needs a heavy crop.  
**Prompt:** `1.85:1 theatrical flat framing, balanced cinematic composition with generous height`  
**Example:** Spirited Away (2001), presented in 1.85:1.  
**Yields to:** `look.ratio_scope` — The piece needs the epic register.  
`look.ratio_185`

### 2.00:1 / Univisium

**Also called:** Univisium, 2:1, streaming widescreen  
**What it is:** A middle shape between 1.85 and scope, proposed by the Italian cinematographer Vittorio Storaro as a single unified standard. It has become common on streaming work.  
**Effect on the audience:** It gives a cinematic width without sacrificing the height of faces. It carries a quiet prestige.  
**Used for and where it works best:** Prestige series, modern documentary and any film headed for home screens, because the bars stay thin and acceptable. Right when one project needs width for landscape and height for dialogue.  
**Best in:** formats: Drama Series Episode, Limited Series, Documentary Feature, Documentary Series, Feature Film, Heritage / Historical Documentary, Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Crime / Procedural, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), Sci-Fi, Mystery / Whodunit, Political Thriller  
**Avoid when:** It delivers neither the epic punch of scope nor the intimacy of Academy, so when the subject needs a clear position pick an extreme. On a big screen it can feel undecided.  
**Prompt:** `2.00:1 aspect ratio, modern widescreen framing, thin letterbox bars, balanced landscape and portrait space`  
**Yields to:** `look.ratio_scope` — The subject needs an extreme, not a compromise.  
`look.ratio_200`

### 2.20:1

**Also called:** 70mm ratio, Todd-AO, roadshow ratio  
**What it is:** The classic ratio of 70mm presentation. Wider than 1.85 and less extreme than scope, with enough height left for architecture and sky.  
**Effect on the audience:** Grandeur with balance. It feels built for a big screen and an audience that came for an occasion.  
**Used for and where it works best:** The historical epic, the desert, the long journey, and any work whose huge architecture must stay in frame from ground to sky. Strong in heritage work when the ziggurat has to be whole and the horizon with it.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Trailer / Teaser, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, War, Adventure, Western, Faith / Biblical Epic, Drama  
**Avoid when:** The average viewer will not separate it from 2.35, so use it when the presentation itself matters. On a small screen the difference vanishes.  
**Prompt:** `2.20:1 wide frame, epic landscape with full sky and ground retained, classic 70mm presentation feeling`  
**Example:** Lawrence of Arabia (1962), presented in 2.20:1.  
**Yields to:** `look.ratio_scope` — Presentation itself does not matter; viewers cannot separate them.  
`look.ratio_220`

### Scope 2.35 to 2.40:1

**Also called:** CinemaScope, Panavision, anamorphic widescreen, 2.39:1  
**What it is:** The classic wide cinema frame, born from anamorphic lenses. The historical variants 2.35, 2.39 and 2.40 are barely separable by eye.  
**Effect on the audience:** It expands the world horizontally and makes everything feel larger than the character. The lateral emptiness becomes a tool: one figure at an edge and nothing beside them.  
**Used for and where it works best:** Epic, western, science fiction, desert and battle, plus the two hander with the figures at opposite edges and a tense emptiness between them. In trailers and music videos it buys instant size.  
**Best in:** formats: Feature Film, Trailer / Teaser, Music Video, Title Sequence / Opening Credits, Game Cinematic / Gameplay, 3D CG Animation, Heritage / Historical Documentary, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Western, Sci-Fi, Space Opera, Fantasy / Epic, Mythology / Ancient Epic, War, Action, Historical / Biopic, Heritage (civilisation-focused), Noir / Neo-Noir  
**Avoid when:** In a scene built on something vertical, a standing figure, a tower, a waterfall, it cuts off the top and the bottom. Inside a 9:16 vertical it becomes a useless thin strip.  
**Prompt:** `2.39:1 anamorphic widescreen, two figures pushed to opposite edges, wide empty space between them`  
**Example:** Once Upon a Time in the West (1968), the widescreen standoffs.  
**Yields to:** `look.ratio_185` — Scene built on a vertical: tower, waterfall, standing figure.  
`look.ratio_scope`

### 2.76:1 / Ultra Panavision 70

**Also called:** Ultra Panavision, MGM Camera 65, widest scope  
**What it is:** The widest ratio ever used for commercial release, produced by 65mm photography with a mild anamorphic squeeze. The frame becomes an extremely long horizontal band.  
**Effect on the audience:** It forces you to work entirely across: a row of faces, the gap between two enemies, or infinite emptiness. Height becomes a luxury.  
**Used for and where it works best:** The room where many people must all be in frame at once, the chariot race or the lined up armies, and the standoff whose subject is the distance itself. Strong in the historical epic and the western.  
**Best in:** formats: Feature Film, Trailer / Teaser, Title Sequence / Opening Credits, Heritage / Historical Documentary, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography, Night and Astrophotography | genres: Western, Historical / Biopic, War, Mythology / Ancient Epic, Heritage (civilisation-focused), Adventure, Action, Drama  
**Avoid when:** Close-ups are hard because a face leaves a huge void on either side. On any home screen it produces enormous black bars.  
**Prompt:** `ultra wide 2.76:1 frame, a long horizontal line of figures across the whole image, vast lateral space`  
**Example:** The Hateful Eight (2015), shot in Ultra Panavision 70.  
**Yields to:** `look.ratio_200` — Close-ups and home screens; the bars stay thin.  
`look.ratio_276`

### 1:1 Square

**Also called:** square format, Instagram square  
**What it is:** A frame equal in height and width. It leans neither vertical nor horizontal, so composition naturally becomes centred.  
**Effect on the audience:** Stillness, formality and containment. It feels like a hung photograph rather than a scene continuing beyond the edges.  
**Used for and where it works best:** Portraiture, product and social work when one video must serve several placements. Narratively, the character locked into a routine or a cell, or the shape of an old photograph inside a modern piece.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Music Video, Title Sequence / Opening Credits, Experimental / Art Film, Corporate / Training, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Psychological / Arthouse, Romance, Comedy, Family, Surreal / Absurdist, Melodrama  
**Avoid when:** It fails on wide scenes and on a two hander with real distance in it. In a cinema context it looks odd without a reason.  
**Prompt:** `1:1 square frame, centred subject, formal balanced composition, contained space`  
**Yields to:** `look.ratio_scope` — A two-hander with real distance in it.  
`look.ratio_square`

### 4:5 Vertical

**Also called:** portrait ratio, feed ratio, 0.8:1  
**What it is:** A moderate vertical: taller than square and shorter than 9:16. It occupies the largest area the feed allows on most platforms.  
**Effect on the audience:** It gives strong presence in the feed without losing all the context around the subject.  
**Used for and where it works best:** The feed post, the short ad, the product in someone's hand, and any case where you want the face and the place together in a vertical space. It is also a forgiving crop out of existing 16:9 material.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Product Video / Motion Design, Music Video, Corporate / Training, Explainer, Kids Content, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Comedy, Family, Drama, Romance, Science / Educational, Slice of Life, Preschool / Early Learning  
**Avoid when:** On a full screen vertical surface like stories or TikTok it plays with bars. On a horizontal display it is wrong from the start.  
**Prompt:** `4:5 vertical frame, subject centred with some environment left around them, social feed composition`  
**Yields to:** `look.ratio_9x16` — Full-screen vertical surfaces like Stories or TikTok.  
`look.ratio_4x5`

### 9:16 Full Vertical

**Also called:** vertical, full screen mobile, story ratio  
**What it is:** The full vertical frame that fills a phone screen. Its width is so tight that it accepts only one thing across: a face, a body or a line of text.  
**Effect on the audience:** It removes context and leaves only the direct relationship between viewer and face. Forced intimacy.  
**Used for and where it works best:** Reels, Shorts, TikTok and vertical micro drama, anything built on a face, speech and close movement. The shots that work are a full standing figure, a big face, or something travelling top to bottom through the frame.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Music Video, Commercial / TVC, Kids Content, Meme / Comedy Edit, Vlog / YouTube Long-Form, Explainer, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography | genres: Comedy, Drama, Romance, Horror, Thriller / Suspense, Family, Preschool / Early Learning, Slice of Life, Dark Comedy / Satire  
**Avoid when:** Wide scenes, crowds and horizontal architecture are simply lost. Keep anything important out of the reserved bands at the top and bottom, where the app interface sits — **the figures are owned by `vertical.safe_zones` and are not repeated here**, because they are platform measurements that move and this card carried a stale pair of them until September 2026.  
**Prompt:** `9:16 vertical frame, single subject filling the height, tight background, key action kept in the centre safe area`  
**Yields to:** `look.ratio_4x5` — You need context around the subject, not only a face.  
`look.ratio_9x16`

### Aspect Ratio Switching

**Also called:** shifting aspect ratio, ratio as a timeline, expanding frame  
**What it is:** Changing the frame ratio inside one piece to separate two time periods, two worlds or two states of mind. The change lands either on a hard cut or as the bars gradually opening.  
**Effect on the audience:** The strongest temporal signal available without a single word. The viewer immediately understands that we have moved, and even without naming it they feel the shift.  
**Used for and where it works best:** The flashback narrow and the present wide, or the trapped character in a tight frame that opens when they break free. Very strong in heritage documentary: archive in its own ratio, new photography wide.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Heritage / Historical Documentary, Music Video, Short Film, Trailer / Teaser, AI-Generated Clip | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Psychological / Arthouse, Coming of Age, Tragedy, Mystery / Whodunit, Romance  
**Avoid when:** Without a clear rule behind it the audience assumes a playback fault, and in vertical short-form the moving bars waste the screen and read as that fault anyway — `scene.flashback_ratio_change` hands vertical to a colour shift. The count is not the limit: every switch has to follow the one rule the audience has learned - this ratio is that era, or the frame opens at the moment of release - and a switch outside that rule reads as a fault however few there are.  
**Prompt:** `the frame opens from a narrow boxed ratio to full widescreen as the character steps outside`  
**Example:** Mommy (2014), the 1:1 frame that opens wide.  
**Source:** reference — checked 2026-09-23: no published cap on the number of switches exists, and the examples the two ratio cards cite both pass any small cap — *The Grand Budapest Hotel* changes ratio at least four times (Anderson: *"the different aspect ratios tell viewers where they are in the timeline"*, No Film School), and *Mommy* opens its frame twice and closes it twice (Dolan, *The Hollywood Reporter*). What they share is a rule the audience can learn.  
**Yields to:** `color.flashback_tint` — The two eras must separate without moving the frame.  
`look.ratio_switch`

### Letterbox

**Also called:** letterboxing, black bars top and bottom  
**What it is:** Black bars above and below the image so a wider ratio can play inside a less wide container. It can be a delivery necessity or an aesthetic decision.  
**Effect on the audience:** It tells the viewer "this is a film". The bars create a viewing ritual before the content even starts.  
**Used for and where it works best:** Publishing a cinema framed shot on a platform of another shape, and any trailer or music video you want to read as cinema. In documentary, carrying wide material inside a 16:9 timeline without cropping it.  
**Best in:** formats: Trailer / Teaser, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Title Sequence / Opening Credits, Commercial / TVC, Video Essay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Action, Drama, Sci-Fi, Thriller / Suspense, Historical / Biopic, Romance, Noir / Neo-Noir, Fantasy / Epic  
**Avoid when:** On a small screen the bars eat real estate and shrink faces. Avoid them on fast feed content, where the viewer scrolls straight past; a vertical piece that wants the cinema claim for one dramatic section is `look.fake_letterbox`, which keeps the bars to that section and returns to the full frame.  
**Prompt:** `cinematic letterbox bars top and bottom, 2.39:1 image inside a 16:9 container`  
**Yields to:** `vertical.reframe_169` — Fast feed content, where bars shrink the picture.  
`look.letterbox`

### Pillarbox

**Also called:** pillarboxing, side bars, windowbox  
**What it is:** Black bars at the sides when a narrow image plays inside a wider container, such as 4:3 material inside 16:9. The flanks stay empty.  
**Effect on the audience:** It announces that this material comes from another time or another device. The viewer reads "archive" without being told.  
**Used for and where it works best:** Presenting archive and old photographs in heritage documentary without stretching or cropping, and any flashback shot in an older ratio. The columns can also be filled with a blurred enlargement of the same frame instead of black.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Documentary Series, Video Essay, News Report / Reportage, Drama Series Episode, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Historical / Biopic, Heritage (civilisation-focused), True Crime, Drama, Verite / Observational, Political Thriller, Science / Educational  
**Avoid when:** Stretching the image instead of pillarboxing distorts faces and counts as a professional error. Do not pillarbox an entire piece, it ends up feeling small.  
**Prompt:** `4:3 archival image pillarboxed inside a 16:9 frame, black columns at both sides, period photograph feeling`  
**Yields to:** `look.ratio_133` — The whole piece is narrow; commit, do not column it.  
`look.pillarbox`

### Fake Letterbox on Vertical

**Also called:** faux cinematic bars, vertical letterbox, bars inside 9:16, black bar overlay  
**What it is:** You place black bars top and bottom inside a 9:16 frame so a wide strip sits in the middle of a vertical screen. The image did not become cinema, but its shape claims it did.  
**Effect on the audience:** It instantly raises the perceived production value and it opens space for text above and below the strip.  
**Used for and where it works best:** Horizontal material that must be published vertically, or one short dramatic section whose reduced picture has passed a phone-size readability test. Use the top bar for a scene title and the bottom one for subtitles, and do not run it through the whole video: return to the full frame for talking parts. It is a bounded exception to `look.letterbox`'s fast-feed warning, not a general production-value overlay for native vertical footage.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Trailer / Teaser, Commercial / TVC, Music Video, Meme / Comedy Edit, Heritage / Historical Documentary, Video Essay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography | genres: Action, Drama, Thriller / Suspense, Romance, Horror, Comedy, Sci-Fi, Heritage (civilisation-focused), Historical / Biopic, Mystery / Whodunit  
**Avoid when:** You give away a large share of an already small screen and faces shrink, and it is heavily overused, so skip it when the content does not earn it. If the shot was framed vertically in the first place, the bars crop the part that mattered.  
**Prompt:** `vertical 9:16 frame with black bars top and bottom creating a wide cinematic strip in the middle, title text below the strip`  
**Yields to:** `look.ratio_9x16` — The shot was framed vertically; bars crop what mattered.  
`look.fake_letterbox`

### The Letterbox Reveal

**Also called:** opening bars, bars pulling away, frame expansion  
**What it is:** The image starts boxed between black bars, then the bars slide away, or close in, as a move, so the picture changes size in front of the viewer.  
**Effect on the audience:** Opening feels like an intake of breath: the world suddenly widens. Closing feels like a door sealing shut.  
**Used for and where it works best:** The moment of release: a door opens, a tunnel ends, a city appears. Or the inverse in horror: the bars squeeze inward as the danger approaches. Strong in trailers, title sequences, and in vertical work when a strip grows into the full screen.  
**Best in:** formats: Trailer / Teaser, Title Sequence / Opening Credits, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Feature Film, Short Film, Commercial / TVC, AI-Generated Clip | genres: Adventure, Action, Drama, Fantasy / Epic, Horror, Thriller / Suspense, Sci-Fi, Historical / Biopic  
**Avoid when:** Untied to a sound or a story event it is just an edit trick. Do not repeat it; once in a piece is enough.  
**Prompt:** `black letterbox bars sliding away to reveal the full frame as the doors open onto the city`  
**Yields to:** `look.ratio_switch` — The change marks two time periods, not one release beat.  
`look.letterbox_reveal`

### 35mm Film

**Also called:** 35mm, photochemical, film negative  
**What it is:** The standard of cinema for over a century: fine grain, forgiving colour, and highlights that roll off gently instead of clipping. Its colour and contrast simply do not behave like digital.  
**Effect on the audience:** It gives warmth and psychological depth. The viewer reads the image as memory rather than as documentation.  
**Used for and where it works best:** Drama, period work, music video and premium advertising, and anywhere you want faces alive and skin reading as flesh. Emulating it digitally needs three things together: grain, halation and a soft highlight rolloff.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Short Film, Heritage / Historical Documentary, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Romance, Noir / Neo-Noir, War, Tragedy, Gothic / Vampire, Coming of Age  
**Avoid when:** Adding grain alone, with no halation and no rolloff, just gives a digital image with noise on it. In explainer and corporate work it adds nothing.  
**Prompt:** `shot on 35mm film, fine organic grain, gentle highlight rolloff, warm halation around the practicals, rich skin tones`  
**Yields to:** `look.digital_cinema` — Explainer and corporate work, where film adds nothing.  
`look.film_35mm`

### 16mm / Super 16

**Also called:** 16mm, Super 16, documentary film gauge  
**What it is:** A smaller gauge than 35mm, so its grain is bigger and more visible and its resolution lower. It was the gauge of documentary, television and independent film.  
**Effect on the audience:** It gives honesty, roughness and proximity. The viewer feels the image was stolen from reality rather than manufactured.  
**Used for and where it works best:** Documentary, war, kitchen sink drama and memory, plus the short film that wants texture instead of polish. It pairs naturally with handheld, because the grain and the movement build one shared credibility.  
**Best in:** formats: Documentary Feature, Documentary Series, Feature Film, Short Film, Music Video, Docudrama / Reenactment, Drama Series Episode, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: War, Verite / Observational, Drama, True Crime, Coming of Age, Survival, Crime / Procedural, Psychological / Arthouse, Historical / Biopic  
**Avoid when:** In luxury or product advertising it reads as cheap. In dark scenes the grain explodes and takes the detail with it.  
**Prompt:** `shot on Super 16mm, visible grain structure, slightly soft resolution, handheld documentary energy, natural colour`  
**Example:** The Hurt Locker (2008), shot on Super 16mm.  
**Yields to:** `look.film_35mm` — Luxury or product advertising, where 16mm reads cheap.  
`look.film_16mm`

### Super 8

**Also called:** super 8mm, home movie film  
**What it is:** The home movie gauge: heavy grain, warm and drifting colour, an unsteady frame, and usually no synchronised sound.  
**Effect on the audience:** It delivers instant nostalgia. The viewer reads the shot as a family memory even when they recognise nobody in it.  
**Used for and where it works best:** Childhood flashbacks, the family reel a character discovers, the wedding and summer montage. Music video and advertising use it to manufacture a past in seconds.  
**Best in:** formats: Music Video, Feature Film, Short Film, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Wedding / Event Film, Title Sequence / Opening Credits, Docudrama / Reenactment, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography | genres: Coming of Age, Drama, Romance, Family, Tragedy, Psychological / Arthouse, Horror, Found Footage  
**Avoid when:** It is badly overused in advertising, so it means nothing unless the past is really part of the story. Keep it short; a minute is plenty.  
**Prompt:** `Super 8 home movie look, heavy grain, warm faded colour, unstable gate, soft focus, no sound`  
**Yields to:** `look.vhs` — The home recording belongs to the tape era.  
`look.film_super8`

### 65mm and 70mm Film

**Also called:** 65mm, 70mm, large gauge film  
**What it is:** A negative area far larger than 35mm, so grain nearly disappears, detail becomes enormous and tonal transitions turn very smooth. Photography happens on 65mm, presentation on 70mm.  
**Effect on the audience:** It gives physical presence: you feel you could touch the cloth, the stone, the face. It also makes the work feel important before it says anything.  
**Used for and where it works best:** The epic, the period piece, the monumental portrait, the scene where the location is a character. Excellent in heritage work because relief, clay and weave read with a detail no smaller format delivers.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Trailer / Teaser, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, Drama, War, Faith / Biblical Epic, Western, Tragedy, Adventure  
**Avoid when:** In fast handheld coverage none of its advantage survives. In explainer and social work the difference never reaches the viewer.  
**Prompt:** `shot on 65mm film, almost invisible grain, immense detail in fabric and stone, smooth tonal gradation, large format depth`  
**Example:** The Master (2012), shot on 65mm.  
**Yields to:** `look.film_16mm` — Fast handheld coverage; large-format advantage does not survive.  
`look.film_65_70`

### IMAX 15/70

**Also called:** IMAX film, 15 perforation 70mm  
**What it is:** The largest photographic format used in cinema: 70mm film running horizontally at fifteen perforations per frame, giving an enormous negative and a 1.43:1 frame. The camera is huge and noisy.  
**Effect on the audience:** It engulfs the viewer completely. The image passes the edge of their vision, so they feel placed in the location rather than watching it.  
**Used for and where it works best:** The shots that justify the cost: flight, battle, the monument, space, and a close face at a pivotal beat. It is normally used as sequences inside a film, with the jump from the normal ratio into IMAX doing narrative work.  
**Best in:** formats: Feature Film, Documentary Feature, Trailer / Teaser, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography, Documentary Photography | genres: Adventure, War, Sci-Fi, Space Opera, Historical / Biopic, Heritage (civilisation-focused), Nature / Wildlife, Disaster, Action  
**Avoid when:** Camera noise ruins synchronised dialogue, so quiet talking scenes are the wrong place for it. On a home screen the entire reason for it evaporates.  
**Prompt:** `IMAX 15/70 format, 1.43:1 immersive frame, overwhelming resolution and scale, viewer placed inside the location`  
**Example:** Dunkirk (2017), large sections shot in IMAX 15/70.  
**Yields to:** `look.film_65_70` — Quiet synchronised dialogue; the IMAX camera is too loud.  
`look.imax_1570`

### Digital Cinema

**Also called:** digital capture, log footage, modern sensor look  
**What it is:** Digital capture with wide dynamic range recorded to a log file that protects detail for the grade. Sharp, clean and grainless, and its noise behaves nothing like film grain.  
**Effect on the audience:** It gives clarity, neutrality and present tense credibility. The viewer feels this is happening now rather than in the past.  
**Used for and where it works best:** Documentary, contemporary drama, low light work and anything carrying visual effects. Right when you need total grading latitude or the freedom to change the look after the shoot.  
**Best in:** formats: Drama Series Episode, Documentary Feature, Documentary Series, Feature Film, Corporate / Training, Explainer, News Report / Reportage, Interview / Video Podcast, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography | genres: Drama, Crime / Procedural, Thriller / Suspense, Verite / Observational, Medical Drama, Legal Drama, Science / Educational, Political Thriller, True Crime  
**Avoid when:** Excessive cleanliness makes a period scene feel like costumed theatre. In anything meant to read as memory, the clarity works against you.  
**Prompt:** `modern digital cinema capture, clean sharp image, wide dynamic range, neutral colour, no grain`  
**Yields to:** `look.film_35mm` — Period scenes and memory, where cleanliness works against you.  
`look.digital_cinema`

### Film Grain

**Also called:** grain, grain structure, added grain  
**What it is:** The random silver structure of film that appears as a moving texture over the image. Its size depends on the gauge and the stock speed, and it is emulated digitally with a grain plate scanned from real film.  
**Effect on the audience:** It makes the image feel like a substance rather than a file. It also softens hard digital edges and puts life into flat areas.  
**Used for and where it works best:** Anything you want to read as film: heritage, period, music video, flashback. As a practical tool, grain also hides banding in skies and gradients.  
**Best in:** formats: Feature Film, Music Video, Heritage / Historical Documentary, Drama Series Episode, Short Film, Commercial / TVC, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, War, Noir / Neo-Noir, Gothic / Vampire, Tragedy, Psychological / Arthouse, Coming of Age  
**Avoid when:** Heavy grain on a clean digital image reads as noise rather than film. Social compression also turns it into blotches, so dial it back for vertical delivery.  
**Prompt:** `fine 35mm film grain over the image, organic moving texture, subtle in the highlights and stronger in the shadows`  
`look.grain`

### Gate Weave

**Also called:** film weave, frame instability, registration drift  
**What it is:** A tiny drift of the whole frame left, right, up and down, caused by the film not sitting perfectly still in the camera or projector gate. It is emulated digitally with a small random offset.  
**Effect on the audience:** It removes digital perfection. The image feels like it passed through a mechanical device, so you believe it is old.  
**Used for and where it works best:** Faking archive in heritage documentary, the flashback, the scene supposedly running from a projector inside the story. With grain and scratches it completes the illusion; without it the picture gives itself away.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Feature Film, Music Video, Title Sequence / Opening Credits, Docudrama / Reenactment, Short Film, AI-Generated Clip | genres: Historical / Biopic, Heritage (civilisation-focused), Found Footage, Horror, Psychological / Arthouse, Drama, True Crime, War  
**Avoid when:** Too much of it genuinely shakes the picture and tires the eye. Keep it off shots with locked on screen text, where the drift becomes obvious.  
**Prompt:** `subtle gate weave, the whole frame drifting a few pixels, mechanical projector instability, film grain over it`  
`look.gate_weave`

### Dust and Scratches

**Also called:** film damage, print wear, emulsion scratches  
**What it is:** Black and white specks and vertical lines running through the image, sometimes with burns or damage at the edges. It is the mark of a print worn by use or storage.  
**Effect on the audience:** It ages the image and says this print lived and time passed over it. In horror it suggests that whatever was recorded is cursed.  
**Used for and where it works best:** Faked archive, the distant flashback, the reel a character finds in a box. In horror and found footage, damage and burn just before the event builds dread without showing anything.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Music Video, Short Film, Title Sequence / Opening Credits, Mockumentary, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Horror, Found Footage, Historical / Biopic, Heritage (civilisation-focused), Psychological / Arthouse, Supernatural Horror, True Crime, Gothic / Vampire  
**Avoid when:** Too much makes it read as a preset rather than a print, and a scratch repeating in the same place exposes the trick. On genuine archive material it is usually the wrong move, because you are faking damage on a document that carries its own; the exception is a declared restoration where you match a missing reel to the ones around it.  
**Prompt:** `aged film print, dust specks, vertical emulsion scratches, occasional frame damage at the edges, heavy grain`  
**Example:** Grindhouse (2007), the deliberately damaged print look.  
`look.dust_scratches`

### Light Leak

**Also called:** film leak, flash frame leak, edge fogging  
**What it is:** Light reaching the film through a gap in the camera or during loading, burning the edge of the image orange or red for a few frames. It differs from the Light Leak Transition, where the leak sweeps the frame from edge to edge to cover a cut: here the leak is a texture inside the shot itself.  
**Effect on the audience:** It gives fragility and accident, as if the film itself was not protected. It suggests a memory nobody planned to keep.  
**Used for and where it works best:** The head or tail of a flashback, the move between two memories in a music video, wedding and summer montages. In vertical work it doubles as a fast transition landing on the beat.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Wedding / Event Film, Feature Film, Short Film, Title Sequence / Opening Credits, Commercial / TVC, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Romance, Coming of Age, Drama, Family, Psychological / Arthouse, Tragedy, Surreal / Absurdist, Melodrama  
**Avoid when:** Preset packs have worn it out, so only use it when the story gives it a reason. Keep it out of serious drama and honest documentary.  
**Prompt:** `warm orange light leak burning in from the edge of frame for a few frames, film grain, faded colour`  
**Yields to:** `trans.light_leak` — The leak sweeps across to cover a cut.  
`look.light_leak`

### Changeover Cue

**Also called:** cigarette burn, reel change mark, projection cue dot  
**What it is:** A small circle appearing in the top right corner of the screen for a moment, originally the signal telling the projectionist to switch to the next reel. It comes twice near the end of a reel.  
**Effect on the audience:** It reminds the viewer that what they are watching is a strip running through a machine, not a window on reality. A deliberate break in the illusion.  
**Used for and where it works best:** A piece about cinema itself, or the beat where you want the audience aware that they are watching. In heritage and faked archive it completes the old print illusion alongside grain and weave.  
**Best in:** formats: Feature Film, Short Film, Title Sequence / Opening Credits, Video Essay, Music Video, Experimental / Art Film, Heritage / Historical Documentary, AI-Generated Clip | genres: Psychological / Arthouse, Dark Comedy / Satire, Surreal / Absurdist, Drama, Horror, Historical / Biopic, Comedy  
**Avoid when:** Most younger viewers do not know what it means, so it is usually a weak place to carry information; the exception is an audience of film people, for whom the cue reads instantly. Anywhere but the top right corner it stops being a changeover cue and becomes a stray mark.  
**Prompt:** `small circular changeover cue mark flashing in the top right corner of the frame, film grain, projected print look`  
**Example:** Fight Club (1999), the changeover cues pointed out by the narrator.  
`look.changeover_cue`

### Countdown Leader

**Also called:** Academy leader, film leader, 5 4 3 2 countdown  
**What it is:** The numbers counting down on the head leader before a film starts, with a sweeping circle, lines and technical marks. It belongs to the projection process, not to the film.  
**Effect on the audience:** It builds anticipation in seconds. The viewer knows something is about to start and braces without thinking about it.  
**Used for and where it works best:** The opening of a piece pretending to be an old reel, the head of a section in a heritage documentary, the start of a music video. In vertical work a fast countdown with sound works as a scroll stopping hook.  
**Best in:** formats: Title Sequence / Opening Credits, Music Video, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Video Essay, Experimental / Art Film, AI-Generated Clip | genres: Historical / Biopic, Heritage (civilisation-focused), Psychological / Arthouse, Comedy, Dark Comedy / Satire, Drama, Surreal / Absurdist  
**Avoid when:** Editors have worn it out as decoration, so skip it without a reason. Keep it short, two seconds is enough.  
**Prompt:** `academy countdown leader, numbers ticking down with a sweeping circle, scratched film, projector light flicker`  
`look.countdown_leader`

### VHS / Camcorder Look

**Also called:** VHS, camcorder, tape look, tracking noise  
**What it is:** Low resolution analogue video: colour bleeding at the edges, tracking noise rolling through the picture, horizontal jitter and broken contrast. Often with a date and time burned on screen. It differs from the VHS Transition, where tracking lines sweep past at the moment of the cut to hide the join: here the texture sits on the whole image for the length of the shot.  
**Effect on the audience:** It delivers the nineties instantly and the feeling that this recording was private and not meant to be seen. In horror it makes the viewer search the noise.  
**Used for and where it works best:** The old family tape, the recording of the accident, the horror of an unlabelled cassette. In music video and vertical work it serves as a complete nineties visual identity.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Short Film, Mockumentary, Title Sequence / Opening Credits, Meme / Comedy Edit, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Horror, Found Footage, Psychological Horror, Coming of Age, Drama, Supernatural Horror, True Crime, Dark Comedy / Satire  
**Avoid when:** The low resolution loses facial detail, so do not carry a subtle performance on it. Preset filters have also flogged it to death.  
**Prompt:** `VHS camcorder look, tracking noise bars rolling through frame, bleeding colour, low resolution, timestamp in the corner`  
**Yields to:** `trans.vhs` — Tracking lines sweep past at the cut, hiding the join.  
`look.vhs`

### CRT Scanlines

**Also called:** scanlines, tube screen look, phosphor glow  
**What it is:** Fine horizontal lines, a phosphor glow and a slight curve at the corners: the look of an image displayed on an old tube screen and rephotographed from it.  
**Effect on the audience:** It makes the viewer feel they are looking at a screen inside the story rather than at the image directly. A layer of mediation that creates distance and doubt.  
**Used for and where it works best:** The screen inside the scene: a television, a monitor, an old computer, a game. In cyberpunk and horror, a face on a tube screen feels trapped and observed.  
**Best in:** formats: Feature Film, Music Video, Game Cinematic / Gameplay, Title Sequence / Opening Credits, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Drama Series Episode, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Cyberpunk, Horror, Sci-Fi, Psychological Horror, Found Footage, Thriller / Suspense, Dystopia / Post-Apocalyptic, Coming of Age  
**Avoid when:** Do not put it on a shot meant to be a direct view; it becomes a logic error. Social compression also eats the lines and leaves what looks like noise.  
**Prompt:** `filmed off a CRT tube screen, fine horizontal scanlines, phosphor glow, slight screen curvature and refresh flicker`  
**Yields to:** `look.screenlife` — The screen inside the story is modern, not a tube.  
`look.crt_scanlines`

### CCTV / Surveillance Look

**Also called:** security camera look, surveillance footage, fixed cam  
**What it is:** A fixed high camera on a wide lens, low resolution, washed or absent colour, a stuttering frame rate and usually a clock and date in the corner. No camera movement and no deliberate composition.  
**Effect on the audience:** It gives the sense that somebody was watching and the event was captured by accident. What is in frame starts to feel like evidence rather than a scene.  
**Used for and where it works best:** Crime and investigation, the moment the recording exposes. In horror, the empty corridor held long enough for something to pass in the background. In thriller, cutting between cinematic coverage and surveillance builds the idea that somebody is tracking.  
**Best in:** formats: Feature Film, Drama Series Episode, Mockumentary, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Documentary Series, Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Crime / Procedural, True Crime, Thriller / Suspense, Horror, Found Footage, Mystery / Whodunit, Psychological Horror, Dystopia / Post-Apocalyptic, Spy / Espionage  
**Avoid when:** The low resolution loses faces, so a must read detail usually dies on it; the exception is when failing to read the face is itself the point of the scene. Do not move the camera either; the movement breaks the illusion instantly.  
**Prompt:** `fixed high angle CCTV camera, wide lens, low resolution, desaturated, stuttering frame rate, timestamp in the corner`  
**Example:** Cache (2005), the surveillance tapes that open the film.  
`look.cctv`

### Burned-In Timestamp

**Also called:** date stamp, time code burn, camera OSD  
**What it is:** Time and date numerals burned into the picture, sometimes with a red record symbol or a battery indicator. They come from the camera itself, not from the edit.  
**Effect on the audience:** It turns the shot into a document. The viewer reads the numbers without meaning to and believes the event happened at that time.  
**Used for and where it works best:** Horror and found footage building a night by night chronology, crime fixing the time of an act, documentary asserting that this is the original recording. A clock advancing inside a long locked shot builds tension on its own.  
**Best in:** formats: Feature Film, Mockumentary, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Series, Short Film, Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Horror, Found Footage, True Crime, Crime / Procedural, Thriller / Suspense, Psychological Horror, Mystery / Whodunit, Supernatural Horror  
**Avoid when:** If the numbers do not match the story chronology somebody will notice and trust is gone. Do not add it to ordinary cinematic coverage.  
**Prompt:** `burned-in white timestamp in the corner reading date and time, red REC symbol, low resolution video look`  
**Example:** Paranormal Activity (2007), the timestamped night recordings.  
`look.timestamp`

### Phone Footage Look

**Also called:** smartphone video, filmed on a phone, vertical phone clip  
**What it is:** The phone image: deep depth of field, heavy digital sharpening and colour processing, exposure that hunts and resets by itself, usually vertical and handheld. Sometimes with the app interface visible.  
**Effect on the audience:** It gives total immediacy. The viewer reads it as something that just happened, filmed by a person who was there rather than by a crew.  
**Used for and where it works best:** The bystander shot inside a film, the breaking news beat, the character recording themselves. In modern drama and vertical micro drama, cutting to the phone image inside cinematic coverage declares whose point of view this is.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Feature Film, Drama Series Episode, News Report / Reportage, Mockumentary, Vlog / YouTube Long-Form, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Thriller / Suspense, Drama, Horror, Found Footage, True Crime, Comedy, Political Thriller, Crime / Procedural, Coming of Age  
**Avoid when:** Used for a whole piece it stops working as a signal. The hunting exposure also ruins long static scenes.  
**Prompt:** `shot on a phone, vertical handheld, deep focus, over sharpened digital processing, auto exposure shifting mid shot`  
**Yields to:** `look.shot_on_iphone` — The whole piece is shot on the phone.  
`look.phone_footage`

### Found-Footage Look

**Also called:** found footage, recovered tape, first person camera  
**What it is:** The whole piece pretends to be material shot from inside the story and recovered later: the camera is in a character's hand, the frame lurches, sound drops out and the recording starts and stops in the middle of events.  
**Effect on the audience:** It removes the protection a normal film gives. There is no director shielding the viewer any more, so anything becomes possible.  
**Used for and where it works best:** Horror, mystery and mockumentary, plus any story whose subject is the act of recording. Its power lies in what is missed: the camera drops, the viewer hears without seeing, and the frame arrives late to the event.  
**Best in:** formats: Feature Film, Mockumentary, Short Film, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography | genres: Found Footage, Horror, Psychological Horror, Supernatural Horror, Thriller / Suspense, Mystery / Whodunit, Survival, True Crime  
**Avoid when:** You need a convincing reason for the character to keep filming; without it the whole contract collapses. Excessive shake also exhausts the audience and loses them.  
**Prompt:** `found footage style, handheld camera held by a character, frame lurching and missing the action, sound cutting in and out`  
**Example:** The Blair Witch Project (1999).  
**Yields to:** `look.phone_footage` — No convincing reason for a character to keep filming.  
`look.found_footage`

### Screen-Life Look

**Also called:** screenlife, desktop film, webcam look  
**What it is:** The story plays entirely inside a computer or phone screen: windows, chat threads, video calls and a moving cursor. The screen is the camera, and faces arrive through a webcam.  
**Effect on the audience:** It gives a strange intimacy: the viewer reads the character's mind from the typing, the hesitation and the deleting before sending. Every lag in a call becomes suspense.  
**Used for and where it works best:** Mystery, investigation and contemporary horror, plus any story about digital relationships, disappearance and surveillance. It works vertically too when the story lives inside a phone rather than a laptop.  
**Best in:** formats: Feature Film, Short Film, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Explainer, Video Essay, AI-Generated Clip | genres: Mystery / Whodunit, Thriller / Suspense, Horror, Crime / Procedural, True Crime, Drama, Coming of Age, Psychological Horror  
**Avoid when:** Small text is unreadable on a phone, so you must enlarge and steer the eye. Without cursor movement and typing mistakes it feels dead.  
**Prompt:** `screen-life composition, laptop desktop with chat windows and a webcam call, cursor moving, typing and deleting`  
**Example:** Searching (2018).  
**Yields to:** `look.phone_footage` — Phone delivery, where on-screen text will not read.  
`look.screenlife`

### Action Cam Look

**Also called:** GoPro look, body cam, helmet cam  
**What it is:** A tiny camera on an ultra wide lens mounted to a body, a helmet or a piece of equipment. Everything is sharp, the edges bow, and movement turns violent because the camera is strapped to a body.  
**Effect on the audience:** It puts the viewer inside the body. Speed doubles and distances stretch, so even small movement feels like risk.  
**Used for and where it works best:** Action sports, the chase, first person combat, the descent or the jump. In vertical work and gaming it is the default language of thrill, and in documentary it reaches places a big camera cannot.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, Documentary Feature, Game Cinematic / Gameplay, Feature Film, Vlog / YouTube Long-Form, Travel / Real Estate / Hospitality, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography | genres: Action, Adventure, Survival, War, Thriller / Suspense, Disaster, Martial Arts / Wuxia, Sports Drama  
**Avoid when:** The violent motion makes long stretches nauseating, so keep them short. In dialogue or emotional scenes it simply does not belong.  
**Prompt:** `action cam mounted on the chest, ultra wide bowed edges, everything sharp, violent body motion, first person perspective`  
**Example:** Hardcore Henry (2015), shot from a first person body mounted rig.  
`look.actioncam`

### Night Vision Look

**Also called:** infrared look, green nightvision, IR camera  
**What it is:** An infrared image: everything in shades of green or grey, eyes flaring white, heavy noise, and the light coming from an infrared source the eye cannot see.  
**Effect on the audience:** It produces helplessness and threat. The viewer can see while knowing the characters in the dark cannot, and that knowledge becomes a weight.  
**Used for and where it works best:** The scene where the power fails, the chase in total darkness, night horror and found footage. In wildlife documentary it films nocturnal animals without disturbing them with light.  
**Best in:** formats: Feature Film, Mockumentary, Documentary Feature, Documentary Series, Drama Series Episode, Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Horror, Thriller / Suspense, Found Footage, Survival, War, Nature / Wildlife, Psychological Horror, Spy / Espionage, Crime / Procedural  
**Avoid when:** Faces lose their features and start to look alike, so do not carry fine performance on it. Do not use it in a scene with visible light either; it becomes a logic error.  
**Prompt:** `infrared night vision look, green monochrome image, eyes glowing white, heavy noise, darkness beyond the IR range`  
**Example:** The Silence of the Lambs (1991), the night vision finale in the basement.  
**Yields to:** `look.thermal` — The watcher is a machine or predator, not human.  
`look.night_vision`

### Thermal Imaging Look

**Also called:** thermal camera, heat vision, FLIR look  
**What it is:** An image that reads heat rather than light: a living body glows while the cold surroundings go dark, rendered either as a heat map of white, yellow, red and blue or as grey.  
**Effect on the audience:** It strips a person of identity and reduces them to a heat signature. It feels as if whatever is looking is not human.  
**Used for and where it works best:** The point of view of a predator, a machine or a drone, and the dark chase where the hunt is for bodies rather than faces. In science and documentary it presents heat as real information about buildings or animals.  
**Best in:** formats: Feature Film, Game Cinematic / Gameplay, Documentary Feature, Documentary Series, News Report / Reportage, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Sci-Fi, Action, War, Thriller / Suspense, Horror, Monster / Kaiju, Science / Educational, Spy / Espionage, Survival  
**Avoid when:** It fails when the audience must identify who the person is. In an emotional beat it cancels sympathy entirely.  
**Prompt:** `thermal imaging look, glowing white hot body against a cold dark background, heat map colours, machine vision overlay`  
**Example:** Predator (1987), the creature's heat vision point of view.  
**Yields to:** `look.night_vision` — A human observer with an IR device.  
`look.thermal`

### Datamoshing

**Also called:** datamosh, compression glitch, pixel bleed  
**What it is:** A deliberate corruption of the video compression held inside one shot: the frame stops refreshing, so every movement drags the old pixels with it and the image melts and smears as it moves. It differs from the Glitch / Datamosh Transition (`trans.glitch`), where the corruption joins two shots at the cut: here it is the texture of the shot itself, for as long as the shot lasts.  
**Effect on the audience:** It makes a moment feel like memory dissolving or reality failing. Organic and digital at the same time.  
**Used for and where it works best:** The beat where a character transforms or comes apart, a dream or a memory that will not hold its shape, and the performance shot in music video and experimental advertising. In cyberpunk and digital horror it signals that the system itself is no longer reliable.  
**Best in:** formats: Music Video, Experimental / Art Film, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Commercial / TVC, Game Cinematic / Gameplay, Meme / Comedy Edit, AI-Generated Clip | genres: Cyberpunk, Surreal / Absurdist, Psychological / Arthouse, Horror, Sci-Fi, Dystopia / Post-Apocalyptic, Psychological Horror, Musical  
**Avoid when:** On every transition it becomes noise and tires the eye. In realistic or documentary work it reads as a corrupt file rather than a style.  
**Prompt:** `datamosh texture inside the shot, every movement dragging smeared pixels behind it, colours bleeding through the moving figure, melting compression artefacts`  
**Example:** Welcome to Heartbreak (2009), the Kanye West video built on datamoshing.  
**Yields to:** `trans.glitch` — The effect is the cut itself, not the shot.  
`look.datamosh`

### Shot on iPhone Look

**Also called:** iPhone cinema, smartphone feature look  
**What it is:** Shooting an entire piece on a phone with professional handling: adapter lenses, stabilisation and a proper grade. The result is a clean image with more depth of field than cinema and a hard digital sharpness.  
**Effect on the audience:** It gives closeness and lightness: the camera can go anywhere, so the film feels like it travels with the characters instead of waiting for them.  
**Used for and where it works best:** Independent film, street work, scenes inside a car, a lift or any tight space, and projects with small budgets and high speed. Excellent for vertical micro drama, where the device and the platform already belong to the same world.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Feature Film, Short Film, Vlog / YouTube Long-Form, Documentary Feature, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Drama, Comedy, Coming of Age, Crime / Procedural, Thriller / Suspense, Slice of Life, Romance, Verite / Observational  
**Avoid when:** In low light it shows noise and heavy processing that ruins skin. The deep field also keeps everything sharp, so isolation has to be built with light and distance instead.  
**Prompt:** `shot on a phone with pro handling, clean stabilised image, deep focus, slightly over sharpened digital rendering, natural light`  
**Example:** Tangerine (2015), shot on iPhone.  
**Yields to:** `look.digital_cinema` — Low-light work, where phone processing ruins skin.  
`look.shot_on_iphone`

### Black and White

**Also called:** monochrome, B and W, greyscale  
**What it is:** An image without colour, so everything is built on contrast, texture and the shape of shadow. It has two poles: hard, with high contrast and deep blacks, or soft, with a long grey scale and no true black.  
**Effect on the audience:** It lifts the image out of daily reality into memory or myth. The hard version reads as danger and decisiveness; the soft version reads as grief and stillness.  
**Used for and where it works best:** Period, biography and memory, plus noir that lives on shadow. Choose the hard version for crime and conflict and the soft one for mourning, childhood and rural life, and remember that the decision changes the shoot itself, because costume and set get chosen for their grey value rather than their hue. In heritage documentary it unifies genuine archive with new material with no visible seam, and it makes clay and stone feel older — but where the viewer must still be able to tell the record from the new footage, let the seam show: `look.pillarbox` keeps the archive in its own ratio so it announces itself.  
**Best in:** formats: Feature Film, Short Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Music Video, Title Sequence / Opening Credits, Video Essay, Experimental / Art Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography | genres: Noir / Neo-Noir, Historical / Biopic, Drama, War, Tragedy, Crime / Procedural, Gothic / Vampire, Heritage (civilisation-focused), Psychological / Arthouse, Romance, Surreal / Absurdist, Faith / Biblical Epic  
**Avoid when:** Do not drop the colour to rescue a weak image; monochrome exposes composition and lighting rather than hiding them. When colour carries information, a uniform, a flag, blood, you lose it.  
**Prompt:** `black and white cinematography, deep blacks and bright specular highlights, strong shadow shapes, rich texture in skin and stone`  
**Example:** Roma (2018), shot in black and white.  
**Yields to:** `color.accent` — Colour carries information: a uniform, a flag, blood.  
`look.black_white`

### Orthochromatic Look

**Also called:** ortho film look, early emulsion look  
**What it is:** Early emulsions were blind to red, so lips and ruddy skin print dark while a blue sky burns out white. Today it is emulated with a blue or cyan filter over black and white photography.  
**Effect on the audience:** It makes faces look strange, hard and unfamiliar, so the image reads as genuinely predating modern photography.  
**Used for and where it works best:** Work pretending to come from the nineteenth or early twentieth century, period horror, and photographic reenactment in documentary. It is strongest with a narrow ratio and single source lighting.  
**Best in:** formats: Feature Film, Short Film, Heritage / Historical Documentary, Docudrama / Reenactment, Title Sequence / Opening Credits, Experimental / Art Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography | genres: Gothic / Vampire, Horror, Historical / Biopic, Psychological Horror, Heritage (civilisation-focused), Tragedy, Folk Horror, Drama  
**Avoid when:** Skin prints dark and uneven, so watch casting and makeup. In a contemporary piece it just reads as a grading mistake.  
**Prompt:** `orthochromatic black and white look, red lips and skin rendering dark, blue sky blown to white, hard period emulsion feel`  
**Example:** The Lighthouse (2019), the orthochromatic style photography.  
**Yields to:** `look.black_white` — A contemporary piece, where ortho reads as a mistake.  
`look.orthochromatic`

### Sepia

**Also called:** sepia tone, brown monochrome, toned print  
**What it is:** A monochrome image toned throughout in warm brown. It comes from an old chemical process that also protected prints from fading.  
**Effect on the audience:** It says "the past" faster than anything else, and it adds a warmth and longing that cold monochrome does not carry.  
**Used for and where it works best:** Memory sections, old family photographs, the historical opening, and the split between two worlds inside one piece: brown here, colour there. In heritage documentary put it on maps, manuscripts and excavation photographs rather than on live footage, because on live material it reads as a cheap filter while on archive it reads as authentic.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Documentary Series, Feature Film, Title Sequence / Opening Credits, Docudrama / Reenactment, Video Essay, Music Video, Wedding / Event Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Western, Drama, Family, Tragedy, Faith / Biblical Epic, Romance, Melodrama, War, Mythology / Ancient Epic  
**Avoid when:** Educational video has worn it out as a symbol of the past, so skip it when lighting and design can carry the period instead. Held for a long sequence it tires the eye.  
**Prompt:** `sepia toned monochrome, warm brown highlights and shadows, aged photographic feel, soft contrast`  
**Example:** The Wizard of Oz (1939), the sepia toned Kansas scenes.  
**Yields to:** `look.black_white` — Live footage, where sepia reads as a cheap filter.  
`look.sepia`

### Three-Strip Technicolor

**Also called:** Technicolor, dye transfer, three strip  
**What it is:** An older process that exposed three negatives at once through a beam splitter and printed them with dyes. The result is intensely saturated, stable colour, especially reds and greens, over rich blacks.  
**Effect on the audience:** It makes colour feel painted and deliberate rather than photographed. The world comes out more beautiful and more intense than reality, so it reads as a tale.  
**Used for and where it works best:** This is the look-selection card: choose and approve a three-strip or dye-transfer reference for musicals, fairy tales, fantasy and designed studio colour, then hand its measured palette to `color.technicolor` for finishing. Costume, set and lighting design belong here; grade controls belong on the colour shelf.
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Title Sequence / Opening Credits, 2D Animation (Western / Cartoon), Short Film, 3D CG Animation, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Musical, Fairy Tale, Fantasy / Epic, Romance, Family, Historical / Biopic, Adventure, Melodrama  
**Avoid when:** It suits neither realism nor documentary; the excess colour makes the image untrue. It also needs designed sets and costumes, without which it just looks loud.  
**Prompt:** `three strip Technicolor look, hyper saturated reds and greens, rich blacks, glossy studio lighting, painterly colour`  
**Example:** The Wizard of Oz (1939), photographed in three-strip Technicolor.  
**Yields to:** `look.kodachrome` — Strong period colour without designed sets and costumes.  
`look.technicolor`

### Kodachrome Look

**Also called:** Kodachrome, colour reversal look, slide film look  
**What it is:** A colour reversal film Kodak produced from 1935 until it was discontinued in 2009, known for dense reds and oranges, clean blues, fine grain and colour that held for decades.  
**Effect on the audience:** It gives the feeling of a genuine photograph from the sixties or seventies: strong colour that never turns synthetic, with the sun clearly present in it.  
**Used for and where it works best:** Travel and family memory sections in documentary, flashbacks to that era, and stills drifting slowly inside a montage. Pair it with fine grain and high contrast: it was a slide film made to be projected, with dense blacks. When the job is a grade laid over existing footage rather than a frame that reads as shot on the slide film itself, the card is `color.kodachrome`.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Music Video, Feature Film, Title Sequence / Opening Credits, Video Essay, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Coming of Age, Drama, Family, Road Movie, Nature / Wildlife, Romance  
**Avoid when:** Do not mix it into a scene set today; the saturation dates it immediately. An overcooked emulation also pushes reds until skin detail disappears.  
**Prompt:** `Kodachrome slide film look, dense reds and oranges, clean blue sky, fine grain, high contrast, sunlit nostalgia`  
**Source:** reference — checked 2026-09-23: every description of the stock that speaks of contrast calls it high (Wikipedia, *Kodachrome*, the Contrast section; camera-wiki.org, *Kodachrome*: *"a fairly contrasty nature"*); Kodak's own data sheet E-55 (2009) confirms the fine grain and does not describe contrast in words.  
**Yields to:** `look.digital_cinema` — The scene is set today.  
`look.kodachrome`

### Polaroid Look

**Also called:** instant film look, integral print, instant photo  
**What it is:** An instant print with an uneven white border and a wide bottom margin, cool or green leaning colour, low contrast and uneven patches from the chemistry.  
**Effect on the audience:** It feels like a moment grabbed fast and never repeatable. The picture reads as a private piece of evidence rather than a work of art.  
**Used for and where it works best:** The character who keeps photographs so they will not forget, the investigation wall, the end of a scene where the image freezes and becomes a print. In music video and vertical work, a Polaroid frame inside the vertical frame adds a layer and nostalgia.  
**Best in:** formats: Feature Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Drama Series Episode, Short Film, Wedding / Event Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Mystery / Whodunit, Thriller / Suspense, Drama, Romance, Coming of Age, Psychological / Arthouse, Crime / Procedural, Horror  
**Avoid when:** The ready made border is a worn out social media fashion. On material set before instant photography existed it usually reads as an anachronism, because the frame carries a date with it; the exception is an openly playful piece that is not pretending to be of its period.  
**Prompt:** `Polaroid instant photo look, thick uneven white border with a wide bottom margin, cool green shifted colour, low contrast`  
**Yields to:** `look.wet_plate` — The photograph predates instant film.  
`look.polaroid`

### Wet Plate Look

**Also called:** collodion look, tintype look, nineteenth century photography  
**What it is:** An emulation of nineteenth century wet collodion photography: long exposures, a sharp centre with soft edges, chemical stains and flaws around the border, and a sky that prints empty white.  
**Effect on the audience:** It gives gravity and weight. The face feels like it held still for minutes to be captured, so it reads as a document rather than a shot.  
**Used for and where it works best:** The character portrait in a period piece, the opening of a documentary about the nineteenth century, the ancestral photograph a scene turns around. Strongest as a locked frame with one small movement inside it.  
**Best in:** formats: Heritage / Historical Documentary, Feature Film, Title Sequence / Opening Credits, Docudrama / Reenactment, Experimental / Art Film, Short Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography, Travel Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Gothic / Vampire, Western, Folk Horror, Drama, Tragedy, Faith / Biblical Epic  
**Avoid when:** It is wrong for any subject after the early twentieth century and becomes a historical error. Heavy movement inside the frame also breaks the logic of a long exposure.  
**Prompt:** `wet plate collodion look, sharp centre with soft edges, chemical stains around the border, blown white sky, still formal pose`  
**Yields to:** `look.orthochromatic` — The subject is past the collodion era.  
`look.wet_plate`

### Hand-Cranked Look

**Also called:** silent era look, undercranked silent film, 16fps look  
**What it is:** Silent era cameras were cranked by hand at roughly sixteen to eighteen frames per second, so played back at twenty four the motion runs fast and uneven with a flicker in the exposure.  
**Effect on the audience:** It gives the feeling of genuinely old time rather than imitation. In comedy it makes movement funny all by itself.  
**Used for and where it works best:** A section pretending to come from the early twentieth century, physical comedy quoting silent cinema, and the very distant dream or memory. With monochrome, scratches and flicker the illusion is complete.  
**Best in:** formats: Feature Film, Short Film, Title Sequence / Opening Credits, Heritage / Historical Documentary, Music Video, Experimental / Art Film, Meme / Comedy Edit, AI-Generated Clip | genres: Comedy, Dark Comedy / Satire, Historical / Biopic, Surreal / Absurdist, Psychological / Arthouse, Family, Horror, Gothic / Vampire  
**Avoid when:** It is wrong for any beat you want felt as real, because the speed turns gravity into comedy. Do not combine it with modern synchronised sound.  
**Prompt:** `hand cranked silent film look, slightly fast uneven motion, exposure flicker, black and white with scratches`  
**Yields to:** `look.orthochromatic` — The early-period beat must feel real, not comic.  
`look.hand_cranked`

### 24 fps

**Also called:** twenty four frames, cinema frame rate  
**What it is:** The standard cinema frame rate since the arrival of sound. It is low enough that motion carries a faint strobe and a natural blur trail.  
**Effect on the audience:** That exact feel is what the viewer reads as "film". Movement becomes a slight dream instead of live reality.  
**Used for and where it works best:** The default for anything dramatic or cinematic: the film, the series, the premium commercial, the music video, the documentary built as cinema. Choose it when you want the audience to feel they are watching a story rather than a broadcast.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Trailer / Teaser, Short Film, Heritage / Historical Documentary, Documentary Feature, AI-Generated Clip | genres: Drama, Romance, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), Horror, Crime / Procedural, Fantasy / Epic, Tragedy  
**Avoid when:** Fast horizontal movement strobes badly, so watch your pan speeds. For sports and live broadcast it is simply not enough.  
**Prompt:** `24 fps cinematic motion cadence, natural motion blur on movement, filmic judder on the pans`  
**Source:** reference — NVIDIA Corporation, "Case Study: Billy Lynn's Long Halftime Walk", November 2016, p. 2, https://images.nvidia.com/content/quadro/quadro-case-studies/pdf/247952-BillyLynn-Case-Study-US-R6-fnl-WEB.pdf, checked 2026-09-24; states that the industry-standard frame rate for feature films is 24 fps, which supports 24 fps as the cinema standard. The dating to the arrival of sound is not stated in this source.  
**Yields to:** `look.fps_60` — Sports and live broadcast; fast pans strobe.  
`look.fps_24`

### 25 and 30 fps

**Also called:** PAL 25, NTSC 30, broadcast frame rates  
**What it is:** The broadcast rates: twenty five across Europe and the Middle East, thirty (29.97 in practice) in the United States and the other 525-line countries. Motion is a little smoother than twenty four and less dreamlike.  
**Effect on the audience:** They read as more present and factual than cinema, closer to the feel of television and news.  
**Used for and where it works best:** News, studio programming, interviews, corporate and explainer work, and anything going out over broadcast. In work full of screens and artificial light, the rate is also chosen against the mains frequency so the picture does not flicker.  
**Best in:** formats: News Report / Reportage, Interview / Video Podcast, Corporate / Training, Explainer, Drama Series Episode, Sports Broadcast / Sports Film, Vlog / YouTube Long-Form, Documentary Series | genres: Verite / Observational, Science / Educational, Political Thriller, Medical Drama, Legal Drama, Comedy, True Crime, Sports Drama  
**Avoid when:** If you want a cinematic feel, the extra smoothness removes it. Mixing rates in one timeline also produces stuttering motion.  
**Prompt:** `25 fps broadcast cadence, slightly smoother motion than cinema, clean television presentation`  
**Source:** reference — ITU-R Recommendation BT.470-6 "Conventional television systems" (1998; superseded 2005 by BT.1700 and BT.1701), https://www.itu.int/dms_pubrec/itu-r/rec/bt/r-rec-bt.470-6-199811-s!!pdf-e.pdf, checked 2026-09-24; Table 1 (p. 2) gives 625-line systems a 50 Hz field rate (25 frames) and 525-line system M 60 Hz nominal, 59.94 Hz in colour (30 frames nominal, 29.97 in practice); the country table (pp. 30–31) lists European and Middle East countries on 625/50 and the United States on M/NTSC.  
**Yields to:** `look.fps_24` — You want a cinematic feel, not broadcast smoothness.  
`look.fps_25_30`

### 48 fps HFR

**Also called:** HFR, high frame rate, double rate cinema  
**What it is:** Twice the cinema rate: motion becomes extremely clean with no strobing, and every detail inside fast movement stays readable.  
**Effect on the audience:** It increases clarity and reduces the dream. Some viewers read it as heightened realism, others as filmed theatre.  
**Used for and where it works best:** Broad action, long fast moving sequences and stereoscopic presentation, plus content made for very large screens. Right when the clarity of the movement is itself the pleasure: a battle, a race, a flight.  
**Best in:** formats: Feature Film, Game Cinematic / Gameplay, Sports Broadcast / Sports Film, 360 / VR, Trailer / Teaser, AI-Generated Clip | genres: Action, Adventure, Fantasy / Epic, Space Opera, War, Sports Drama, Sci-Fi, Martial Arts / Wuxia  
**Avoid when:** The extra clarity exposes makeup, costume and set, so the production has to be flawless. In close emotional work it strips away the mystery.  
**Prompt:** `48 fps high frame rate, ultra clean motion with no strobing, every detail readable inside fast action`  
**Example:** The Hobbit (2012), released in 48 fps HFR.  
**Source:** reference — IMAX Corporation press release, "Warner Bros. Pictures', Metro-Goldwyn-Mayer Pictures' And New Line Cinema's The Hobbit: An Unexpected Journey To Open In IMAX Theatres Around The World Starting Dec. 12", PR Newswire, 12 December 2012, https://www.prnewswire.com/news-releases/warner-bros-pictures-metro-goldwyn-mayer-pictures-and-new-line-cinemas-the-hobbit-an-unexpected-journey-to-open-in-imax-theatres-around-the-world-starting-dec-12-183256722.html, checked 2026-09-24; supports that HFR 3D presents the picture at 48 fps, twice the standard 24 fps cinema rate, and that The Hobbit (2012) was released in it.  
**Yields to:** `look.fps_24` — Close emotional work, or a production that is not flawless.  
`look.hfr_48`

### 60 fps

**Also called:** sixty frames, live look, gaming frame rate  
**What it is:** A high rate that makes motion extremely smooth and immediate. It is the rate of sports broadcast outside the 50 Hz regions (European broadcasters usually require 50 for sport), gaming and most live platform content.  
**Effect on the audience:** It removes the distance between viewer and event. You feel you are seeing the thing now with your own eyes rather than a recording of it.  
**Used for and where it works best:** Sports, live streaming, gameplay capture, fast moving vertical content, and close product motion. It also protects material you may want to slow down later, because the frames are there.  
**Best in:** formats: Sports Broadcast / Sports Film, Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), Concert / Live Event, Vlog / YouTube Long-Form, Product Video / Motion Design, Explainer, News Report / Reportage | genres: Action, Sports Drama, Comedy, Science / Educational, Adventure, Family, Martial Arts / Wuxia  
**Avoid when:** In drama it reads like a cheap daytime serial and kills the cinematic feel. Do not intercut it with twenty four frame material inside one scene.  
**Prompt:** `60 fps capture, very smooth immediate motion, live broadcast feeling, crisp fast movement`  
**Source:** reference — EBU, Technical Report 014, What follows HDTV? A status report on 1080p/50 and '4k', June 2012, p. 15, https://tech.ebu.ch/docs/techreports/tr014.pdf, checked 2026-09-24; supports that European broadcasters usually require 50 Hz for sports, so 60 fps is the sports rate only outside the 50 Hz regions; the gaming and live-platform claims remain the package's working description.  
**Yields to:** `look.fps_24` — Drama, where 60 reads as a daytime serial.  
`look.fps_60`

### 120 fps

**Also called:** 120 frames per second, extreme high frame rate  
**What it is:** A very high capture rate. Played at speed it gives absolute motion clarity; played slower it yields smooth slow motion. This record is about the texture; the decision to slow the material belongs to the time category.  
**Effect on the audience:** Played at speed the image feels more real than reality, and you see detail inside movement that the eye normally misses.  
**Used for and where it works best:** Advanced theatrical presentation and scenes where motion clarity is the event, plus commercials selling a physical instant: spray, detonation, impact. In sports, the replay that reveals what normal speed hid.  
**Best in:** formats: Feature Film, Commercial / TVC, Sports Broadcast / Sports Film, Product Video / Motion Design, Trailer / Teaser, Game Cinematic / Gameplay, 360 / VR, AI-Generated Clip | genres: Action, Sports Drama, Sci-Fi, Thriller / Suspense, War, Science / Educational, Martial Arts / Wuxia, Disaster  
**Avoid when:** Everything in frame has to be perfect because there is no blur left to hide behind. The files are also punishing on a long project.  
**Prompt:** `120 fps capture, hyper clear motion with almost no blur, every droplet and spark resolved`  
**Example:** Billy Lynn's Long Halftime Walk (2016), presented at 120 fps.  
**Source:** reference — NVIDIA Corporation, "Case Study: Billy Lynn's Long Halftime Walk", November 2016, p. 2, https://images.nvidia.com/content/quadro/quadro-case-studies/pdf/247952-BillyLynn-Case-Study-US-R6-fnl-WEB.pdf, checked 2026-09-24; supports the film being captured at 120 fps in 3D at 4K and shown in 120 fps screenings.  
**Yields to:** `look.hfr_48` — 120 unaffordable, or the set cannot survive the clarity.  
`look.fps_120`

### Cinema Motion versus Video Motion

**Also called:** soap opera effect, motion smoothing, film versus video feel  
**What it is:** The difference between cinema motion, a low rate with natural blur, and video motion, a high rate with total clarity. Television sets insert invented frames and convert film into video motion, which is what people call the soap opera effect.  
**Effect on the audience:** Cinema motion makes the viewer feel they are watching a story; video motion makes them feel they are standing on set watching actors in costume.  
**Used for and where it works best:** An early decision on any project: for story and emotion choose cinema motion, for presence and live event choose video motion. Used deliberately, the present tense in video motion and the memory in cinema motion separates two worlds with no explanation.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Music Video, Corporate / Training, AI-Generated Clip | genres: Drama, Thriller / Suspense, Verite / Observational, Historical / Biopic, Sci-Fi, Sports Drama, Romance, Psychological / Arthouse  
**Avoid when:** Do not mix them inside one scene without a narrative reason; the cut between them reads as a technical fault. Remember also that the viewer's television may add the smoothing on its own.  
**Prompt:** `filmic 24 fps motion cadence with natural blur, deliberately avoiding the smooth interpolated video look`  
**Source:** reference — UHD Alliance, FILMMAKER MODE "About" page, https://www.filmmakermode.com/about/, checked 2026-09-24; supports that televisions apply motion smoothing/interpolation as post-processing and that the mode switches it off to keep the source frame rate; the 24 fps cinema cadence is the package's working figure and is not stated there.  
`look.cinema_vs_video_motion`

### 180 Degree Shutter

**Also called:** standard shutter, the 180 rule, half frame exposure  
**What it is:** The shutter stays open for half the frame interval, giving a moderate blur trail on every movement. This is the standard state the viewer's eye has been trained on for a century.  
**Effect on the audience:** It produces natural, comfortable motion. Nobody notices it, and that is exactly its job.  
**Used for and where it works best:** The default for everything: drama, dialogue, walking, ordinary action. Make it your baseline and change it only when you want the motion itself to say something.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Music Video, Commercial / TVC, Short Film, Heritage / Historical Documentary, AI-Generated Clip | genres: Drama, Romance, Crime / Procedural, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), Comedy, Mystery / Whodunit, Family  
**Avoid when:** In very fast action the blur hides detail you may want read. Against flickering sources it can also produce banding.  
**Prompt:** `standard 180 degree shutter, natural motion blur on movement, neutral filmic cadence`  
**Yields to:** `look.shutter_45` — Very fast action, where blur hides detail.  
`look.shutter_180`

### Short Shutter / 45 Degree

**Also called:** 45 degree shutter, 90 degree shutter, staccato shutter  
**What it is:** The shutter opens for a much shorter time, so blur drops away and every frame is sharp on its own. Motion turns staccato and jarring.  
**Effect on the audience:** It produces anxiety, violence and edge. The event feels chopped and abrupt, and the viewer cannot quite digest the movement.  
**Used for and where it works best:** Battle, detonation and impact, and the chase you want to feel painful rather than fun. In horror, the fast attack. It pairs with handheld because both build the same anxiety.  
**Best in:** formats: Feature Film, Trailer / Teaser, Music Video, Game Cinematic / Gameplay, Short Film, Drama Series Episode, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip | genres: War, Action, Horror, Thriller / Suspense, Survival, Slasher, Disaster, Martial Arts / Wuxia  
**Avoid when:** In calm scenes it reads as a playback fault. Over long stretches it genuinely tires the eye, so use it in doses.  
**Prompt:** `short 45 degree shutter, minimal motion blur, every frame crisp, staccato jarring movement, handheld`  
**Example:** Saving Private Ryan (1998), the beach landing shot with a short shutter.  
**Yields to:** `look.shutter_180` — Calm scenes, where staccato reads as a fault.  
`look.shutter_45`

### Open Shutter / 360 Degree

**Also called:** 360 degree shutter, long shutter, smeared motion  
**What it is:** The shutter stays open for the whole frame interval or longer, so movement leaves a long stretched trail and anything moving becomes a coloured streak.  
**Effect on the audience:** It dissolves time. Movement feels like a dream, intoxication or loss of consciousness, and faces turn into ghosts.  
**Used for and where it works best:** The dream, the dizzy spell and the high, time passing in the city at night with cars reduced to light streaks, and the move between two scenes. In music video it gives a fluid layer that rides the rhythm.  
**Best in:** formats: Music Video, Experimental / Art Film, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Short Film, Commercial / TVC, AI-Generated Clip | genres: Psychological / Arthouse, Surreal / Absurdist, Psychological Horror, Drama, Romance, Cyberpunk, Horror, Musical  
**Avoid when:** All detail in motion is gone, so a shot that must be read usually cannot survive it; the exception is when the smear is the information, exhaustion, a drug state, a dream. Held long it becomes exhausting.  
**Prompt:** `open 360 degree shutter, heavy motion smear, moving figures dissolving into ghost trails, city lights stretching into lines`  
**Yields to:** `look.shutter_180` — The shot must be read; smear is not the information.  
`look.shutter_360`

### Interlaced Look

**Also called:** interlacing, 50i, 60i, combing artefacts  
**What it is:** An older video system that records half the lines at a time and interleaves them. When something moves fast the edges tear into comb teeth, and that is the signature of old broadcast video.  
**Effect on the audience:** It says "television" instantly: a news bulletin, a sports broadcast, a daily serial, a family tape. It removes cinematic prestige and replaces it with something live and dated.  
**Used for and where it works best:** Faking nineties broadcast material inside a modern piece, the flashback to something that aired on television, the horror that claims to be a tape. Pair it with 4:3 and low resolution to complete the illusion.  
**Best in:** formats: Mockumentary, Feature Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, Short Film, Documentary Series, AI-Generated Clip | genres: Found Footage, Horror, Coming of Age, True Crime, Drama, Psychological Horror, Dark Comedy / Satire, Political Thriller  
**Avoid when:** On modern displays it reads as a fault rather than a style when there is no context. Delivered as a platform master it usually breaks, because the encoder tears the fields apart; the exception is a broadcast chain that still expects interlaced and handles it properly.  
**Prompt:** `interlaced video look, comb tearing on fast movement, 4:3 frame, low resolution broadcast texture`  
**Yields to:** `look.vhs` — Delivery is a platform master that tears the fields.  
`look.interlaced`

### Resolution as Texture

**Also called:** low res look, pixelation, resolution choice  
**What it is:** Resolution is not only a quality number, it is a texture: low resolution gives pixels and breakup, high resolution gives unforgiving detail in skin, cloth and stone.  
**Effect on the audience:** Low resolution makes the viewer search and fill the gaps with imagination; high resolution hands them everything and leaves nothing to imagine.  
**Used for and where it works best:** Choose low resolution deliberately for surveillance, memory and old tape, and when the frightening thing should stay unresolved. Choose high resolution for heritage, nature and product work where the detail is the subject: a carving, a weave, the skin of an old hand.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Mockumentary, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Horror, Found Footage, Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Science / Educational, Thriller / Suspense, Psychological Horror  
**Avoid when:** High resolution in a period scene exposes makeup and costume, so balance it with lens and light. Low resolution on important material loses it permanently.  
**Prompt:** `deliberately low resolution image, visible pixel structure and compression breakup, detail dissolving in the shadows`  
`look.resolution_texture`

### HDR versus SDR

**Also called:** high dynamic range, SDR, HDR grade  
**What it is:** Standard range confines brightness to a narrow window and clips the top, while high dynamic range lets highlights climb far higher and carries a wider colour volume. The same shot delivers two different experiences.  
**Effect on the audience:** In HDR, fire, sun and neon feel like actual light sources instead of white patches, so the image becomes physical and immersive.  
**Used for and where it works best:** Night, fire, a temple lit by candles, space, and any work headed for a platform that supports it. Grade two versions, one for HDR and one for SDR, because the same image does not translate between them.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Trailer / Teaser, Game Cinematic / Gameplay, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Abstract Photography, Portrait Photography, Landscape Photography, Street Photography | genres: Sci-Fi, Fantasy / Epic, Historical / Biopic, Heritage (civilisation-focused), Horror, Thriller / Suspense, Nature / Wildlife, Space Opera  
**Avoid when:** An aggressive HDR grade turns washed out and flat when it is converted down. Do not hang story detail in the extreme highlights if most of the audience will watch the SDR version.  
**Prompt:** `HDR grade, specular highlights blazing far above the mid tones, deep shadows retained, wide colour volume, candlelit interior`  
`look.hdr_sdr`
