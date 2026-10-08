# Still Photography and Static Visual Arts

18 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### The Slot or the Shutter

**Also called:** the stills selector, which decision first, slot before shutter  
**What it is:** The card at the head of the `photo.` shelf. It asks first **which of two decisions you are making** — what the finished picture has to fit, or how the picture is made — and then one question on each side: *what is the thing in the frame that is not the picture*, and *where does the time in this frame come from*. It hands back a named shortlist for each answer. Unlike the other selectors in this package, its axes are not read off the shelf's exceptions, because this shelf's exceptions cannot carry one: every `Avoid when:` here is written to the same template — *it usually fails this way, and the exception is when that failure is the point* — which produces a craft warning about the card you already chose and never a hand-off to a different card. The axes were read off the bodies instead, and then checked against the few pair conditions that exist.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that a still is made against the job it has to do, rather than against the technique that was interesting that week.  
**Used for and where it works best:** Answer question one before anything else, out loud, in one sentence. **The two halves of this shelf do not compete, they compose** — a product listing image is a slot answer and a focus-merged exposure is a shutter answer, and the same job routinely needs one of each. So question one is not *which card*, it is *which of the two things am I settling right now*, and most briefs settle the slot first and the shutter second, on different days and sometimes by different people. On the slot side the return is a checklist rather than a choice. On the shutter side it is a genuine fork and the return is one card.  
**Best in:** formats: all | genres: all  
**Avoid when:** **You are choosing a technique in order to have chosen one.** Nothing on this shelf is required: a plain, well-composed frame is the honest answer far more often than the shelf's spread suggests, and every card here carries a named cost. Also avoid it where another shelf owns the decision — focal length, depth, grade, retouch and type all have their own shelves, and more than half of this shelf's hand-offs leave for them, which is the shelf admitting where the real choice lives. And **distrust the first fork itself.** The package's own shelf register records this family as one decision; this card splits it into two on measurement, because the two halves share no pair edge in either direction and their bodies describe each other as compatible rather than as alternatives. That is a judgement made on a very small number of edges, and if it is wrong it is not repairable by adding a question later — the whole map would be laid out wrong. **On the slot side, distrust the word *choice* as well**: a single campaign wants a poster and a thumbnail and a packshot at once, so that half of the map returns a list of things to make, and reading it as a fork will lose you two of the three.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Which decision are you making: what the picture must fit, or how the picture is made?**
Asked first because the two halves of this shelf never once refer to each other. Of the shelf's seven `Yields to:` fields, one runs inside the shutter half (`photo.panning` → `photo.icm`, *"Subject moves on several axes; impressionistic chaos instead"*), none runs inside the slot half, and **none crosses between them in either direction**. The bodies say the same thing more directly than the graph does: `photo.focus_stacking` describes its own use as *"the product still where the logo and the far edge must both be sharp"*, which is a packshot — a card in the other half, named as a companion rather than as a rival. Two halves that never yield to each other and describe each other as compatible are two decisions, not one.

**Axis 2, on the slot side — What is in this frame that is not the picture, and does it live inside the frame or outside it?**
Read off the bodies, because there is nothing else to read: *"the type lives with the picture: a quiet area for the title, room for the logo and the credit block… The empty space is designed before the photograph is chosen"* (`photo.poster_composition`), *"here the type is a structural part of the design"* (`photo.thumbnail_composition`), *"Its purpose is to settle a decision, not to make a pretty picture"* (`photo.storyboard_frame`), *"the store product page, the printed advert, the last card of a video commercial, the marketplace listing image"* (`photo.packshot`). The pair graph corroborates it from an unexpected direction: four of this shelf's six off-shelf hand-offs start in this half, and each one leaves for the shelf that owns the intruding thing — the type shelf, the vertical-cover shelf, the retouch shelf, the documentary shelf. **The slot cards yield off-shelf because their real alternative is the slot's own shelf, not another photograph.**

**Axis 3, on the shutter side — Where does the time in this frame come from?**
Also read off the bodies, and it is the one thing every card in that half states plainly: *"one exposure lasting from a fraction of a second to minutes or hours"* (`photo.long_exposure_still`), *"several frames of the same composition while stepping the focal plane"* (`photo.focus_stacking`), *"the same composition at several exposures from dark to bright"* (`photo.exposure_blending`), *"more than one image onto the same frame"* (`photo.multiple_exposure`), *"a set of photographs selected and ordered"* (`photo.photo_essay`), *"the fraction of a second in which every element locks"* (`photo.decisive_moment`), *"still in every part except one small region that moves in an endless loop"* (`photo.cinemagraph`). The two remaining pair conditions on the whole shelf both turn on exactly this question: `photo.long_exposure_still` hands off when *"A run of frames is wanted, not one final image"*, and `photo.panning` hands off when the motion will not resolve. Nothing else on this shelf repeats.

---

**The map**

**Axis 1 — which decision**

| Answer | Go to |
| :--- | :--- |
| **The slot — something that is not the photograph is already in the frame or already waiting for it** (six cards) | Axis 2 |
| **The shutter — the picture is the whole deliverable** (eleven cards) | Axis 3 |

**Axis 2 — the slot side. This returns a checklist, not a choice**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Type has to live on the picture, and the space for it is designed before the picture is** (two) | `photo.poster_composition` · `photo.thumbnail_composition` |
| **A commercial or editorial slot, and the subject alone has to carry it** (three) | `photo.packshot` · `photo.key_art_hero_pose` · `photo.environmental_portrait_still` |
| **No audience but the crew — the frame is an instrument for settling a decision** (one) | `photo.storyboard_frame` |

**Axis 3 — the shutter side. This returns one card**

| Answer | The shortlist, by id |
| :--- | :--- |
| **An instant, and it will not come twice** (one) | `photo.decisive_moment` |
| **A duration, printed into one exposure** (four) | `photo.panning` · `photo.icm` · `photo.long_exposure_still` · `photo.light_painting` |
| **Several exposures, merged into one frame** (three) | `photo.focus_stacking` · `photo.exposure_blending` · `photo.multiple_exposure` |
| **More than one finished image, and the order or the gap between them is the content** (two) | `photo.photo_essay` · `photo.diptych_triptych` |
| **It never stops** (one) | `photo.cinemagraph` |

*Two of the five values on Axis 3 hold one card each. That is the shelf's real shape and it has not been padded: nothing else on it catches an instant, and nothing else on it moves.*

---

**The default, and the one against it**

**The default is `photo.decisive_moment`, and it is argued rather than measured, because the measurement on this shelf points at a card that must not have it.** The most-yielded-to card here is `photo.packshot`, with two inbound edges — and both come from **outside** the shelf, from `material.water_glass` (*"Busy background behind glass; use a clean controlled ground"*) and `staging.human_trace` (*"Clinical frame where any trace reads as contamination"*), and both fire on one condition wearing two coats: **the surround is contaminating the subject, so delete the surround.** Two edges, one condition. That is a door out of somebody else's problem, not a fallback, and making it the default would install *put it on a seamless background* as this package's standing advice for stills.

So the default is argued from the bodies: **`photo.decisive_moment` is the only card on the shelf that builds nothing.** Every other shutter answer spends something — time in the exposure, frames to be merged, images to be sequenced, a loop to be masked — and this one spends neither, which makes it the thing all the others are additions to. Its cost is named on its own card and it is a real one: it tempts you to wait through the whole event chasing the frame and come back with nothing. On generated stills that cost inverts into a different one, and it is worth saying plainly — **you cannot wait for an instant you are writing**, so the card becomes an instruction to specify the peak of the gesture rather than the gesture, which is harder and better than it sounds.

**The one against it is `photo.photo_essay`.** Nothing routes to it. It is the only card on the shelf where the deliverable is not an image, and the only one whose meaning lives in what was never photographed: *"The gap between one image and the next makes them build what was not photographed."* It is against the grain of the entire shelf, which otherwise spends seventeen cards putting more into one frame — more time, more exposures, more layers, more type. It takes things out and puts the work between the frames. Its cost is stated and payable: it collapses into an album the moment pictures are picked for their individual quality instead of their role in the run, which is a discipline problem rather than a craft one. For heritage and craft subjects it is the card that turns a set of generated stills into a finished piece with no video in it at all. Its cousin against the grain is `photo.storyboard_frame`, likewise never yielded to, and likewise not trying to be a good picture.

---

**The unasked**

**Fourteen of the seventeen cards are the target of no `Yields to:` field anywhere in the package.** By id:

`photo.light_painting` · `photo.long_exposure_still` · `photo.focus_stacking` · `photo.exposure_blending` · `photo.photo_essay` · `photo.diptych_triptych` · `photo.cinemagraph` · `photo.decisive_moment` · `photo.environmental_portrait_still` · `photo.poster_composition` · `photo.thumbnail_composition` · `photo.storyboard_frame` · `photo.key_art_hero_pose` · `photo.multiple_exposure`

**And the shape of that list is the finding. Every card on the slot side is on it except `photo.packshot`, and the whole shutter side is on it except `photo.icm`** — so the three cards this shelf can be arrived at through are: a packshot reached twice from other shelves when a background has gone wrong, a pan reached once from a pose card when a body will not hold still, and an abstract blur reached once from the pan when the pan fails. **Every inbound edge in the package is somebody else's surface failing.** Nothing anywhere recommends a photographic technique; the shelf is entered from the top by someone who already opened it, or sideways as an escape, and it is never traversed. That is why its axes had to come from the bodies, and it is also why the shelf is not one choice set: **a family nothing routes into has not been read as a family.**

The second thing the list shows, and it is the gap worth filling: **every card on this shelf lists *Generated Keyframe Feeding Video* in its `Best in:` formats — all seventeen, without exception — and not one of them says how a still is made to sit inside a cut.** The shelf has a card for the frame before the shot is filmed and cards for the frame on a page, in a grid, on a listing and on a wall, and nothing at all for the frame that has to match the grade, the lens, the light direction and the motion of the two clips either side of it. The nearest thing that exists, `photo.storyboard_frame`, is explicitly the frame made *before* there is anything to match, and its own warning is that too much detail tempts a team to defend a shot never tested. The card this shelf wants is its opposite: **the still made to a plate that already exists**, where the technique is chosen by what the neighbouring frames already did and not by what would make the best picture alone.

`photo.slot_or_shutter`

---

### Panning Photography

**Also called:** pan blur, follow-through panning, speed blur  
**What it is:** A relatively slow shutter combined with turning the camera at the subject's own speed during the exposure. The subject stays sharp while the background smears into long horizontal streaks.  
**Effect on the audience:** Speed becomes visible inside a still image. The eye reads the length of the streaks as a speed gauge and locks onto the subject because it is the only sharp region in the frame.  
**Used for and where it works best:** The key image for a car or motorcycle campaign, the cover of a sports feature, a portrait of a runner or a horseman at the instant of the launch. It also serves the still that travels with a film when you want to announce motion before a single clip is seen. Best in posters, advertising and sports journalism.  
**Best in:** formats: Poster / Static Design, Commercial / TVC, Product Video / Motion Design, Sports Broadcast / Sports Film, Comics / Webtoon / Photo Essay, Travel / Real Estate / Hospitality, Brand Film, Fashion Film, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Action, Chase, Sports Drama, Adventure, Drama, Slice of Life  
**Avoid when:** It usually fails when the subject itself changes speed or moves on several axes at once, because then nothing lands sharp. The exception is when partial loss is the point: an impressionistic image about chaos, shot at a deliberately slower shutter.  
**Prompt:** `still photograph, panning shot of a motorcycle crossing the frame left to right, rider sharp, background streaked into horizontal motion blur, low camera height, late afternoon light`  
**Yields to:** `photo.icm` — Subject moves on several axes; impressionistic chaos instead.  
`photo.panning`

### Intentional Camera Movement / ICM

**Also called:** ICM, deliberate camera blur, abstract motion stills  
**What it is:** Moving the camera deliberately during a fairly long exposure so that nothing stays sharp, turning the scene into fields of colour and streaks. The direction and the speed decide the shape of the marks.  
**Effect on the audience:** The image loses recognition and keeps mood. The viewer stops at colour and rhythm instead of naming objects, so the place reads as a memory rather than as a report.  
**Used for and where it works best:** Chapter breaks in a photo book, an album cover, an opening plate for a contemplative series, or a treatment for a place that resists a literal picture such as a forest or a sea in a storm. It works in gallery work and in any piece that runs on feeling rather than information.  
**Best in:** formats: Poster / Static Design, Experimental / Art Film, Comics / Webtoon / Photo Essay, Multi-Screen Installation, Music Visualizer, Music Video, Travel / Real Estate / Hospitality, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography, Night and Astrophotography | genres: Psychological / Arthouse, Surreal / Absurdist, Nature / Wildlife, Drama, Magical Realism, Tragedy  
**Avoid when:** It usually becomes an excuse for a weak picture when there is no intention behind the colour and the direction, and then it reads as a technical mistake. The exception is a whole series built on the same gesture and the same direction, where the repetition declares itself as style.  
**Prompt:** `still photograph, intentional camera movement, vertical sweep during a half second exposure across an autumn forest, no sharp edges, amber and deep green colour bands`  
`photo.icm`

### Light Painting

**Also called:** light drawing, painting with light, torch painting  
**What it is:** A long exposure in a dark space while a small light source moves inside the frame or lights parts of the subject one after another. The camera stays fixed and only the light travels.  
**Effect on the audience:** The result feels impossible: luminous lines hanging in air with no visible source, or a subject lit in a way no single lamp could deliver. The viewer senses a maker's hand behind the picture.  
**Used for and where it works best:** A product still for a large or metallic object that resists a single lighting hit, such as a car or a statue, a key visual for a night campaign, or a signature image at an archaeological site where the wall is lit section by section. It also suits music video work built on luminous trails.  
**Best in:** formats: Poster / Static Design, Commercial / TVC, Product Video / Motion Design, Music Video, Brand Film, Experimental / Art Film, Heritage / Historical Documentary, Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Fantasy / Epic, Sci-Fi, Heritage (civilisation-focused), Surreal / Absurdist, Mystery / Whodunit, Musical, Magical Realism  
**Avoid when:** It usually exposes the human doing the painting when that person is not fully dark, leaving transparent ghosts that spoil the cleanliness. The exception is when the ghost is wanted, standing for a spirit or a memory inside the picture.  
**Prompt:** `still photograph, thirty second exposure in a dark hall, a handheld light traced along the carved relief so the stone is lit panel by panel, camera locked on a tripod, deep black background`  
`photo.light_painting`

### Long Exposure Still

**Also called:** slow shutter still, silky water, star trails  
**What it is:** One exposure lasting from a fraction of a second to minutes or hours, so everything that moved during it prints as an extended trace while the static parts stay sharp. Unlike the video version, the result is a single final image, not a run of frames played in sequence.  
**Effect on the audience:** Time piles up inside one frame. The viewer does not see a moment but a duration, and reads from the length of the trace how much time passed in front of the camera.  
**Used for and where it works best:** A river or a waterfall turning to silk, stars wheeling above a ziggurat or a church, car trails on a night street as the bed for a cover. Best for posters, photo books, and location stills that set up a heritage or documentary piece.  
**Best in:** formats: Poster / Static Design, Comics / Webtoon / Photo Essay, Travel / Real Estate / Hospitality, Heritage / Historical Documentary, Brand Film, Multi-Screen Installation, Experimental / Art Film, Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Nature / Wildlife, Heritage (civilisation-focused), Science / Educational, Noir / Neo-Noir, Cyberpunk, Psychological / Arthouse, Mystery / Whodunit  
**Avoid when:** It usually erases the very detail that was the subject, so leaves, faces and a flying flag dissolve into a smear. The exception is when the dissolving is the message: a place that endures while everyone in it is passing through.  
**Prompt:** `still photograph, four minute exposure at blue hour, the river surface smoothed into a single soft plane, the stone bridge razor sharp, tripod locked, low ISO`  
**Yields to:** `time.long_exposure` — A run of frames is wanted, not one final image.  
`photo.long_exposure_still`

### Focus Stacking

**Also called:** focus bracketing, depth merge  
**What it is:** Shooting several frames of the same composition while stepping the focal plane through the subject, then merging the sharp zone of each frame into one image. The camera and the subject do not move between frames.  
**Effect on the audience:** A depth of sharpness no single lens can deliver. The viewer feels an uncanny clarity, and senses that the object is presented for inspection rather than for contemplation.  
**Used for and where it works best:** The product still where the logo and the far edge must both be sharp, macro work on an insect, a gem or a ring, and the documentation of a small artefact whose every detail a researcher needs. It is standard in catalogue work and in museum documentation.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Poster / Static Design, Corporate / Training, Heritage / Historical Documentary, Explainer, Comics / Webtoon / Photo Essay, Tutorial / Instructional Video, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Science / Educational, Heritage (civilisation-focused), Nature / Wildlife, Historical / Biopic, Family, Slice of Life  
**Avoid when:** It usually kills the poetry, because with no soft zones the eye loses the hierarchy it likes to rest in. The exception is when total clarity is the meaning: a technical presentation, or a visual proof that is supposed to hide nothing.  
**Prompt:** `still photograph, focus stacked macro of a carved cylinder seal, every groove sharp from the near edge to the far edge, soft top light, black seamless background`  
**Yields to:** `lens.shallow_dof` — The frame needs a focus hierarchy, not total clarity.  
`photo.focus_stacking`

### Exposure Blending / HDR Merge

**Also called:** bracketing and blending, tone mapped still, HDR photograph  
**What it is:** Shooting the same composition at several exposures from dark to bright, then blending them so the sky comes from the darker frame and the shadows from the brighter one. The aim is an image that keeps detail at both ends.  
**Effect on the audience:** The scene moves closer to what the eye sees than to what the sensor records. The viewer does not notice the technique, only that the room and the window exist in the same instant.  
**Used for and where it works best:** Interiors with a bright window in real estate and hospitality, a landscape at sunset with the sun inside the frame, and the inside of a temple or a church where a shaft from a high opening meets a dark floor. It is standard in property, travel and architectural stills.  
**Best in:** formats: Travel / Real Estate / Hospitality, Corporate / Training, Poster / Static Design, Product Video / Motion Design, Heritage / Historical Documentary, Comics / Webtoon / Photo Essay, Explainer, Commercial / TVC, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Science / Educational, Family, Faith / Biblical Epic, Slice of Life  
**Avoid when:** It is usually pushed too far, every zone ends up the same brightness, the image loses direction and grey halos appear along the edges. The exception is when the flattened look is the intent, in digital painting or a fantastical piece that wants the strangeness.  
**Prompt:** `still photograph, three exposures blended, a dark stone hall with a bright doorway, detail held in both the shadowed floor and the daylight outside, tripod, natural colour`  
`photo.exposure_blending`

### Photo Sequence / Photo Essay

**Also called:** photo story, picture essay, image series  
**What it is:** A set of photographs selected and ordered to carry a process, an event or an idea, so that the meaning comes from the order rather than from any single picture. It usually holds an opening image, a middle of varied sizes, and a closing image.  
**Effect on the audience:** The viewer reads instead of looking. The gap between one image and the next makes them build what was not photographed, so they become a partner in the telling.  
**Used for and where it works best:** Covering a trade or a craft from start to finish, following a day in someone's life, documenting a season or the restoration of a site. It works as a press package, as an ordered run of posts on an account, and as a chapter inside a documentary book.  
**Best in:** formats: Comics / Webtoon / Photo Essay, Poster / Static Design, News Report / Reportage, Video Essay, Heritage / Historical Documentary, Corporate / Training, Travel / Real Estate / Hospitality, Vertical Short-Form (Reels, Shorts, TikTok), Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Verite / Observational, Social Drama, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Nature / Wildlife, True Crime, Slice of Life  
**Avoid when:** It usually collapses into an album when pictures are chosen for their individual quality rather than their role in the run, so sizes repeat and nothing advances. The exception is when repetition is the subject, such as a daily labour that never changes.  
**Prompt:** `still photo series brief, six images on one craft: wide establishing of the workshop, hands at the tool, a detail of the material, the maker's face, the finished object, the empty bench at dusk`  
`photo.photo_essay`

### Diptych and Triptych

**Also called:** paired images, three panel image, side by side  
**What it is:** Two or three images presented side by side as one unit on the same sheet or screen. The gap between them is part of the design, and their order decides how they are read.  
**Effect on the audience:** Adjacency builds a sentence. The viewer compares automatically and pulls out a cause, a consequence or a contrast that was in neither picture on its own.  
**Used for and where it works best:** Before and after in restoration, construction or a personal change, a comparison between two generations or between a site today and its archive photograph, and two faces of one character on a film poster. Strong in exhibition, in a static post and on a chapter cover.  
**Best in:** formats: Poster / Static Design, Comics / Webtoon / Photo Essay, Heritage / Historical Documentary, Corporate / Training, Video Essay, Multi-Screen Installation, Travel / Real Estate / Hospitality, Product Video / Motion Design, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Social Drama, Science / Educational, Drama, Tragedy, Nature / Wildlife, Family  
**Avoid when:** It usually loses its force when the two pictures are too alike, because the viewer reads them as two options nobody chose between. The exception is when the likeness is the point, two nearly identical views of two distant places.  
**Prompt:** `still image layout, diptych, left panel the ruined wall in 1932 archive tone, right panel the same wall today in colour, thin white gutter between them, matching horizon height`  
`photo.diptych_triptych`

### Cinemagraph

**Also called:** living photograph, partial motion loop  
**What it is:** An image still in every part except one small region that moves in an endless loop, such as the steam off a cup, the edge of a robe or a surface of water. It is built with a mask over a clip shot on a completely locked camera.  
**Effect on the audience:** The contradiction between stillness and motion holds the eye. The viewer returns to the moving region on every loop and stays inside the picture far longer than a plain photograph would keep them.  
**Used for and where it works best:** A moving cover for an article or an album, a display advert in a shop window or an airport, and the hero panel of a luxury brand site. It also serves as an opening plate for a heritage piece: a motionless site where only smoke or sand moves.  
**Best in:** formats: Commercial / TVC, Brand Film, Product Video / Motion Design, Poster / Static Design, Title Sequence / Opening Credits, Music Visualizer, Heritage / Historical Documentary, Fashion Film, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Fantasy / Epic, Mystery / Whodunit, Heritage (civilisation-focused), Gothic / Vampire, Romance, Surreal / Absurdist, Slice of Life, Magical Realism  
**Avoid when:** The loop usually gives itself away at the return point with a visible jump that breaks the spell, especially with water and smoke. The exception is when that break is designed as a deliberate pulse inside an art piece.  
**Prompt:** `cinemagraph, locked camera on a seated woman in a lamplit room, everything frozen except the steam rising from the cup, seamless loop, no camera movement`  
**Example:** The term was introduced in 2011 by the photographers Jamie Beck and Kevin Burg.  
`photo.cinemagraph`

### The Decisive Moment

**Also called:** the peak instant, Cartier-Bresson moment  
**What it is:** Choosing the fraction of a second in which every element locks into one meaningful composition: the body at the peak of its gesture, the background and the light exactly in place. It is not arranged, it is waited for and caught.  
**Effect on the audience:** The viewer feels the picture was impossible and happened only once. That sense of rarity carries the image further than its subject does.  
**Used for and where it works best:** Street photography, press, weddings and match coverage, the craftsman at the instant the hammer falls, a child at the top of a jump. In heritage work it is the moment the shaft of light reaches the opening, or a hand touching a relief, and those are waited for rather than requested.  
**Best in:** formats: News Report / Reportage, Comics / Webtoon / Photo Essay, Poster / Static Design, Wedding / Event Film, Sports Broadcast / Sports Film, Travel / Real Estate / Hospitality, Heritage / Historical Documentary, Video Essay, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Verite / Observational, Social Drama, Slice of Life, Sports Drama, Historical / Biopic, Heritage (civilisation-focused), Coming of Age, Drama  
**Avoid when:** It usually tempts the photographer to wait through the whole event chasing one perfect frame and to come back with nothing. The exception is an event that repeats and is guaranteed, where waiting is an investment rather than a gamble.  
**Prompt:** `still photograph, street scene, the man caught mid stride with his heel just above the puddle and his reflection complete, 35mm look, available light`  
**Example:** Henri Cartier-Bresson, Behind the Gare Saint-Lazare, Paris, 1932.  
`photo.decisive_moment`

### The Environmental Portrait (Still)

**Also called:** contextual portrait, portrait in place  
**What it is:** A portrait built as a single image, with the person inside their own place and among their tools, composed and lit for a printed page or a cover. It differs from the documentary version because it does not serve an interview: it stands alone and usually carries a direct look into the lens.  
**Effect on the audience:** The place introduces the person before a word is said. The frontal stance gives them authority inside their own world, so they read as someone who owns the space rather than a witness passing through it.  
**Used for and where it works best:** The cover of a press feature on a craftsman, a scientist or a farmer, a team page on a company site, and the picture of a scholar in front of the object she studied in a heritage book. It also serves as a character reference before production: one image that explains who this is and where they come from.  
**Best in:** formats: Poster / Static Design, News Report / Reportage, Corporate / Training, Heritage / Historical Documentary, Video Essay, Comics / Webtoon / Photo Essay, Travel / Real Estate / Hospitality, Brand Film, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Social Drama, Science / Educational, Verite / Observational, Drama, Political Thriller, Family  
**Avoid when:** The place usually swallows the person when the frame is too wide or the background too busy, and the picture becomes a photograph of a shop. The exception is when smallness is the meaning: one person dwarfed by their life's work.  
**Prompt:** `still photograph, environmental portrait of a weaver standing at her loom, direct look to camera, soft window light from the left, the finished cloth visible behind her, medium wide framing`  
**Yields to:** `doc.environmental_portrait` — The portrait has to serve an interview.  
`photo.environmental_portrait_still`

### The Studio Packshot

**Also called:** packshot, catalogue still, hero product shot  
**What it is:** The product alone on a clean or graded background, lit so that its shape, edges, material and lettering all read. The angle and the height are chosen so the product is understood at once, not so it looks decorated.  
**Effect on the audience:** The product becomes an object independent of the world, so it reads as a clean promise. With no context, the viewer concentrates on quality and detail and trusts the maker.  
**Used for and where it works best:** The store product page, the printed advert, the last card of a video commercial, and the marketplace listing image. Its backbone is two hits: one large soft key that builds the form, and a rim from behind that separates the product from the background.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Poster / Static Design, Corporate / Training, Food Video, Fashion Film, Explainer, Brand Film, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Family, Comedy, Science / Educational, Slice of Life, Romance, Adventure  
**Avoid when:** It is usually cleaned so far that the product looks digitally assembled and loses credibility, especially with food and fabric. The exception is when perfection is the promise itself, as with electronics and jewellery.  
**Prompt:** `still photograph, studio packshot of a glass bottle on a light grey gradient, large soft key from the upper left, two rim lights on the edges, label fully legible, no visible reflections of the studio`  
**Yields to:** `retouch.restraint_check` — Cleaned until the product reads as digitally assembled.  
`photo.packshot`

### Poster Composition

**Also called:** key art layout, one sheet composition  
**What it is:** Building one image where the type lives with the picture: a quiet area for the title, room for the logo and the credit block, and a clear first, second and third element. The empty space is designed before the photograph is chosen.  
**Effect on the audience:** The viewer takes a poster in under two seconds and leaves with three things: what it is, how it feels and when. With no hierarchy they pass by and remember nothing.  
**Used for and where it works best:** A film or series poster, an episode cover, a print advert, a concert bill. In heritage work: a face or a site in the upper third, a title with a carved weight in the lower third, and the bottom band left clear for the credit strip.  
**Best in:** formats: Poster / Static Design, Trailer / Teaser, Title Sequence / Opening Credits, Commercial / TVC, Brand Film, Music Video, Product Video / Motion Design, Corporate / Training, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Drama, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), Fantasy / Epic, Horror, Action, Romance, Musical  
**Avoid when:** The poster is usually chosen as the prettiest frame from the film, so the type collides with detail and becomes hard to read. The exception is a frame composed from the start with empty space at the top, which then needs no surgery.  
**Prompt:** `still poster layout, single hero figure low in the frame against an open sky, upper two thirds kept clean for the title, wide margins, bottom strip reserved for the credit block`  
**Yields to:** `textimg.text_safe_zone` — The frame is composed with title space from the start.  
`photo.poster_composition`

### Thumbnail Composition

**Also called:** YouTube thumbnail, click image, preview card  
**What it is:** A horizontal image designed to be read very small: a face with one readable expression, a single object that names the topic, hard colour contrast and two or three words in heavy type. It differs from the vertical cover frame in ratio, and because here the type is a structural part of the design.  
**Effect on the audience:** The decision happens in a fraction of a second inside a crowded grid. The face pulls the eye first, and the gap between what is visible and what is not yet explained is what drives the click.  
**Used for and where it works best:** Explainers, reviews and documentary uploads on horizontal platforms, and series episodes where the template stays fixed and only the central element changes. In kids content: saturated colour, one character and zero complexity.  
**Best in:** formats: Explainer, Vlog / YouTube Long-Form, Video Essay, Tutorial / Instructional Video, Documentary Series, Kids Content, Corporate / Training, Trailer / Teaser, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography | genres: Science / Educational, True Crime, Heritage (civilisation-focused), Historical / Biopic, Comedy, Family, Preschool / Early Learning, Drama  
**Avoid when:** The type usually promises more than the video delivers, so clicks rise while watch time and trust fall together. The exception is a promise that is real and settled inside the first thirty seconds of the video.  
**Prompt:** `still image, horizontal thumbnail, a face on the right with a wide eyed reaction, the carved tablet on the left, strong warm to cool colour separation, three heavy words across the lower left, clean margins`  
**Yields to:** `vertical.cover_frame` — Vertical ratio rather than horizontal grid.  
`photo.thumbnail_composition`

### The Storyboard Frame as a Still

**Also called:** boardomatic panel, concept frame, previs still  
**What it is:** One panel standing for a whole shot before it is filmed: the shot size, the angle, where everyone stands, the direction of the light, and an arrow for the movement if there is one. Its purpose is to settle a decision, not to make a pretty picture.  
**Effect on the audience:** The team sees the same thing in their heads. Disagreement moves from talk to paper and is settled early at no cost.  
**Used for and where it works best:** Preparing any scene with movement, effects or a crowd, presenting the framing decision to a client before approval, and deciding what has to be generated when the work is made with AI. The working panel stays decision-first and may remain rough; selected approved panels can later take `board_arch.client_pitch_presentation_finish` as a presentation layer without being mislabelled as final art. In generative work the panel itself becomes the reference frame the model is asked to repeat.  
**Best in:** formats: Feature Film, Commercial / TVC, Trailer / Teaser, Anime (Japanese 2D), 3D CG Animation, Music Video, AI-Generated Clip, Comics / Webtoon / Photo Essay, Corporate / Training, Generated Keyframe Feeding Video, Poster / Static Design, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography | genres: Action, Fantasy / Epic, Historical / Biopic, Heritage (civilisation-focused), Sci-Fi, Horror, Adventure, Musical  
**Avoid when:** It is usually drawn with too much detail, which eats time and tempts the team to defend a shot that was never tested on location. The exception is generative and effects work, where the extra detail is precisely the contract that is needed; and a pitch to investors, a brand or a committee, where the board is selling the piece rather than settling a shot and the finish is the point (`board_arch.client_pitch_presentation_finish`).  
**Prompt:** `storyboard panel, black and white, medium wide of two figures at a stone gate, camera low, light from the right, arrow showing the camera pushing in, 16 by 9 frame border`  
`photo.storyboard_frame`

### The Key Art Hero Pose

**Also called:** hero pose, character key art, one sheet pose  
**What it is:** A designed stance for a character inside one still image that sums up who they are: the angle of the body, where the hands sit, the direction of the look and the object they carry. The background is deliberately simplified so the silhouette stays readable.  
**Effect on the audience:** The viewer judges the character before seeing them move. The silhouette alone tells them whether this person threatens, protects or waits.  
**Used for and where it works best:** The character poster in a series or game campaign, the episode cover, and the character card inside a production bible. In heritage work: the king holding the symbol rather than a weapon, with the stance taken from a real relief so the image stays historically honest.  
**Best in:** formats: Poster / Static Design, Trailer / Teaser, Game Cinematic / Gameplay, Title Sequence / Opening Credits, Anime (Japanese 2D), 3D CG Animation, Brand Film, Comics / Webtoon / Photo Essay, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Fantasy / Epic, Superhero, Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, Action, Sci-Fi, Samurai / Chanbara  
**Avoid when:** The pose usually slides into a template that looks like every other poster and the character loses its distinction. The exception is when the template is the promise, in a campaign that deliberately declares its genre.  
**Prompt:** `still photograph, full length hero pose of a figure in patterned robes, three quarter body angle, chin level, one hand holding a staff, plain dark background, rim light on both shoulders`  
`photo.key_art_hero_pose`

### Multiple Exposure

**Also called:** double exposure, in camera layering  
**What it is:** Recording more than one image onto the same frame, or merging them afterwards, so both pictures appear together and their light and dark areas interlock. Usually one frame holds a face and the other a landscape.  
**Effect on the audience:** The image says the person and the place are one thing. The viewer reads the relationship as memory or inner thought rather than as an external event.  
**Used for and where it works best:** The cover of a book or album about identity, exile or memory, a title sequence for a series that lives in the past, and a portrait of a character who carries their place inside them. In heritage work: a contemporary face holding the wall of an ancient site inside the shadows of its features.  
**Best in:** formats: Poster / Static Design, Title Sequence / Opening Credits, Music Video, Comics / Webtoon / Photo Essay, Experimental / Art Film, Brand Film, Heritage / Historical Documentary, Music Visualizer, Generated Keyframe Feeding Video, Fine Art Photography, Landscape Photography, Street Photography, Still Life Photography, Portrait Photography, Abstract Photography | genres: Psychological / Arthouse, Drama, Heritage (civilisation-focused), Historical / Biopic, Surreal / Absurdist, Tragedy, Magical Realism, Romance  
**Avoid when:** It usually turns to mush when both pictures are busy, because the blend needs an empty dark area to receive the second image. The exception is when that visual noise is exactly the mental state you want.  
**Prompt:** `still photograph, double exposure, a profile portrait against a bright plain background with a ruined brick wall exposed inside the dark side of the face, muted warm tones`  
`photo.multiple_exposure`
