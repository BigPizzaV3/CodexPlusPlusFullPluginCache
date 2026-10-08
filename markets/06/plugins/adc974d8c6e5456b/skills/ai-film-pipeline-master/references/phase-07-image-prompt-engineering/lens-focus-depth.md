# Lens, Focus and Depth

53 cards. Also in the other stage: a shot has a frame too. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Ask What the Frame Must Hold

**Also called:** the lens selector, frame before glass, three settings one shot
**What it is:** The card at the head of the `lens.` shelf. It does not describe a look. It asks the three questions the shelf's own pair graph asks over and over — **how much world comes with the subject, how much of what is in frame is resolved, and whether the glass is allowed to be seen** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the forty-three `Yields to:` conditions the cards carry, sorted by what repeats, and every card cited here is cited by id. Unlike a lighting shelf, the three answers are not intersected. **A shot takes one card from each axis**, because a shot is on one focal length, at one aperture, behind one piece of glass.
**Effect on the audience:** None. This card never reaches the screen. It exists so the lens was chosen against the room, the face and the schedule, rather than picked because it was the last one that worked.
**Used for and where it works best:** Answer the three questions **in that order, out loud, one sentence each, before you open the shelf.** Axis one is asked first because the shelf's own text makes axis two depend on it: shallow depth is defined here as *a wide aperture or a long focal length*, and deep focus as *a small aperture with a wide lens*. Answer them the other way round and you will write a prompt asking for an ultra-wide frame with a melted background, which nothing on this shelf can give you. Axis three is asked last and is allowed to be answered **nothing** — that is a real answer and it is the commonest right one.
**Best in:** formats: all | genres: all
**Avoid when:** **You are matching an existing plate, a reference still or a graded frame.** There the focal length is measured off the picture and the glass is identified rather than chosen, and `lens.zoom_vs_prime` says as much in its own terms — the character of the glass dates the image on its own. Also **distrust axis three on a generated still**: there is no aperture and no front element, so a card from that axis is a style word rather than a setting, and style words stack where real filters fight — `lens.veiling_glare` and `lens.polariser` cannot both be true of one exposure, and a model will happily give you both. And **this map cannot hold an answer that changes during the take.** Four cards on the shelf are about focus moving rather than focus placed, one of them hands the reader off the shelf entirely, and nothing routes inward to any of them; if your honest answer to axis two is *it changes*, you are choosing a move, not a lens.
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — How much world comes into the frame with the subject, and which of them wins?**
Asked first, because it is the condition the shelf repeats most and because axis two is written in terms of it. Sixteen of the forty-three `Yields to:` lines turn on it, and they are stated as facts about the frame rather than feelings about the picture: *"The location or the whole body carries the information"* (`lens.portrait_65_85`), *"You want the viewer inside the room, not outside it"* (`lens.tele_100_200`), *"Close on a face, romance or portrait coverage"* (`lens.ultra_wide`), *"Intimate close-up or formal portraiture"* (`lens.wide_18_24`), *"The audience must feel the ground actually covered"* (`lens.tele_compression`), *"A scene that needs honest, readable geography"* (`lens.super_tele`), *"The crowd itself is the information"* (`lens.long_lens_isolation`), *"Close on a human face, where macro turns cruel"* (`lens.macro`).

**Axis 2 — How much of what is in the frame is resolved, and is the sharp part a distance or a shape?**
Twelve conditions turn on this. *"Information sitting on two planes at once"* (`lens.shallow_dof`), *"An intimate close beat that must hold the face"* (`lens.deep_focus`), *"The shot wants isolation and bokeh"* (`lens.hyperfocal`), *"No natural edge to bury the seam"* (`lens.split_diopter`), *"The shot needs disciplined, repeatable focus placement"* (`lens.selective_focus_optic`), *"A key beat that must be repeatable and safe"* (`lens.lens_whacking`), *"The information must stay readable while still soft"* (`lens.soft_focus`), *"Flat background with no highlights to swirl"* (`lens.swirly_bokeh`). **It is not free of axis one.** The wide end of the ladder buys depth and the long end spends it, so on either end this question is already half answered; it is genuinely open only in the middle.

**Axis 3 — May the glass be seen, and if it is seen, can it be taken back?**
Fifteen conditions, and every one of them is about permission and permanence rather than look: *"The glow must stay recoverable, not baked in"* (`lens.diffusion_filter`), *"The scene still needs its shadow detail"* (`lens.veiling_glare`), *"A clean modern context where film red reads false"* (`lens.halation`), *"A realistic scene that still wants a gentle halo"* (`lens.bloom`), *"A serious beat where sparkle would trivialise the lights"* (`lens.star_filter`), *"Period or honest material needing period optics"* (`lens.streak_filter`), *"An old imperfect feel that must still look expensive"* (`lens.chromatic_aberration`), *"A grieving or heavy beat a bright flare would lift"* (`lens.flare`), *"Interview or plain documentary, where scope feels affected"* (`lens.anamorphic`). Asked last, because it is the only axis whose right answer is often none at all.

---

**The map**

**Axis 1 — how much world, and who wins**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The place presses in and beats the person** (five) | `lens.ultra_wide` · `lens.wide_18_24` · `lens.fisheye` · `lens.wide_distortion` · `lens.wide_close_face` |
| **Person and place both readable; the lens says nothing** (three) | `lens.wide_27_35` · `lens.normal_40_50` · `lens.dolly_vs_zoom` |
| **The person cut out of the place** (five) | `lens.portrait_65_85` · `lens.tele_100_200` · `lens.super_tele` · `lens.tele_compression` · `lens.large_format` |
| **The geometry of the frame is itself the subject** (five) | `lens.anamorphic` · `lens.spherical` · `lens.shift_perspective_control` · `lens.tilt_shift` · `lens.barrel_pincushion` |
| **Nearer than the eye reaches — the subject is an object, not a person** (three) | `lens.macro` · `lens.probe` · `lens.diopter` |

**Axis 2 — how much is resolved**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One thin plane, and the rest of the world may go** (six) | `lens.shallow_dof` · `lens.long_lens_isolation` · `lens.fast_glass` · `lens.nd_filter` · `lens.bokeh_texture` · `lens.swirly_bokeh` |
| **All of it, front wall to back wall** (two) | `lens.deep_focus` · `lens.hyperfocal` |
| **Two named planes and nothing between them** (two) | `lens.split_diopter` · `lens.focus_reveal` |
| **The sharp part is placed by hand, not by distance** (two) | `lens.selective_focus_optic` · `lens.lens_whacking` |
| **Nothing is fully resolved, and that is the content** (four) | `lens.soft_focus` · `lens.defocus_pov` · `lens.out_of_focus_opening` · `lens.focus_breathing` |

**Axis 3 — may the glass be seen**

| Answer | The shortlist, by id |
| :--- | :--- |
| **No. The filter only rescues an exposure the sky broke** (two) | `lens.polariser` · `lens.grad_nd` |
| **Yes, as glow — the light is allowed to eat into the image** (five) | `lens.flare` · `lens.veiling_glare` · `lens.diffusion_filter` · `lens.halation` · `lens.bloom` |
| **Yes, as fault — the image admits it was recorded on something** (five) | `lens.vintage_uncoated` · `lens.chromatic_aberration` · `lens.vignette` · `lens.zoom_vs_prime` · `lens.mirror_lens` |
| **Yes, as ornament — the glass performs in front of the scene** (three) | `lens.star_filter` · `lens.streak_filter` · `lens.prism` |

*Every card appears once in the whole map, under one value of one axis. The answer is one card from axis one, one from axis two, and one or none from axis three — not an intersection. Two answers fighting for one frame on the same axis is two shots.*

---

**The default, and the one against it**

**The default is `lens.wide_18_24` for the angle and `lens.deep_focus` for the sharpness, with nothing at all on axis three — and it is measured, not asserted.** Those two are the only cards on the shelf reached by four inbound edges that fire on **more than one distinct condition each**. `lens.wide_18_24` is reached for four different reasons: the room is too tight to stand back (`lens.normal_40_50`), the place or the whole body carries the information (`lens.portrait_65_85`), the viewer must be inside the room rather than outside it (`lens.tele_100_200`), and the ground actually covered must be felt (`lens.tele_compression`). `lens.deep_focus` is reached for four more: the crowd is the information (`lens.long_lens_isolation`), the brief needs everything sharp (`lens.large_format`), there is no edge to hide a seam along (`lens.split_diopter`), and the information sits on two planes (`lens.shallow_dof`). A card reached four times for four reasons is a fallback.

**And the card that ties them on edges is not one.** `lens.portrait_65_85` is also reached four times — from `lens.ultra_wide`, `lens.wide_18_24`, `lens.wide_close_face` and `lens.macro` — and **all four fire on the same condition: a close-up of a human face.** In-degree there measures how often the rest of the ladder runs out of face, not what the shelf falls back on. It is a portrait escape hatch, and mistaking it for the default is how every frame in a piece ends up at the same length.

**The card that calls itself the default is worth naming for the opposite reason.** `lens.wide_27_35` carries *the modern default* among its own alternative names and states in its own words that it is the most used focal length in modern cinema. **The pair graph never mentions it in either direction** — nothing yields to it and it yields to nothing. Its own `Avoid when:` is the argument against it: shoot the whole film there and the images stop having an opinion.

**The one against it is `lens.split_diopter`.** Every other card on this shelf accepts the premise that sharpness falls off with distance and then either spends that falloff (`lens.shallow_dof`, `lens.long_lens_isolation`, `lens.bokeh_texture`) or buys it back with light (`lens.deep_focus`, `lens.hyperfocal`). Split diopter refuses the premise: two distances razor sharp, nothing between them, and a seam that must be buried along an edge in the composition. It is the only card here where **the lens pushes a decision back into the blocking** — you cannot add it after the frame is built, you have to build the frame around it, which is also why it is the one optical choice that survives being asked for in a still. Its stated cost is the seam, and its only escape is `lens.deep_focus` when there is no edge to hide it along, which is a staging failure rather than a lens failure. Nothing on the shelf ever routes a reader to it. Its cousin against the grain is `lens.dolly_vs_zoom`, which is not a lens at all but the rule about whether to change the length or move the camera, and which likewise sits outside the graph in both directions.

---

**The unasked**

**Thirty-two of the fifty-two cards are the target of no `Yields to:` field anywhere on this shelf.** They can be chosen, but nothing ever sends a reader to them. By id:

`lens.wide_27_35` · `lens.tele_100_200` · `lens.tele_compression` · `lens.fisheye` · `lens.wide_distortion` · `lens.wide_close_face` · `lens.large_format` · `lens.probe` · `lens.diopter` · `lens.barrel_pincushion` · `lens.dolly_vs_zoom` · `lens.mirror_lens` · `lens.long_lens_isolation` · `lens.split_diopter` · `lens.hyperfocal` · `lens.bokeh_texture` · `lens.swirly_bokeh` · `lens.lens_whacking` · `lens.fast_glass` · `lens.nd_filter` · `lens.focus_breathing` · `lens.out_of_focus_opening` · `lens.focus_reveal` · `lens.defocus_pov` · `lens.flare` · `lens.star_filter` · `lens.streak_filter` · `lens.chromatic_aberration` · `lens.vignette` · `lens.grad_nd` · `lens.prism` · `lens.zoom_vs_prime`

**And the shape of that list is the finding, not its length. It is not spread evenly across the three axes, and the way it leans says what the readers were holding when they wrote the pairs.** Ten of the twenty-one cards on axis one are reachable; only four of the sixteen on axis two are, and six of the fifteen on axis three. **The ladder is reachable because it is a ladder** — a reader comparing two focal lengths is comparing two rungs of one object and naturally names the neighbouring rung. Sharpness has no ladder, so the readers named the four they could hold in mind at once, shallow, deep, soft and the hand-placed sweet spot, and left twelve cards with nothing pointing at them.

**Inside that, one group is complete, and it is the same absence a second shelf already recorded.** Every card whose content is *focus moving during the take* is unasked: `lens.focus_breathing`, `lens.out_of_focus_opening`, `lens.focus_reveal` and `lens.defocus_pov` — and `lens.focus_reveal`'s only pair points **off this shelf altogether**, to a camera move, which is the shelf conceding the point in writing. A pair field is written by a reader holding one frame. A frame that resolves is not an alternative to a frame that is sharp; it is a different kind of answer, and the field has no grammar for it. That this turns up here, on optics, having already turned up on lighting, makes it a property of the pair field rather than of either shelf.

**The second thing the list shows is a valve.** The whole added-artefact region — `lens.nd_filter`, `lens.grad_nd`, `lens.star_filter`, `lens.streak_filter`, `lens.flare`, `lens.chromatic_aberration`, `lens.vignette`, `lens.prism`, `lens.mirror_lens` — yields outward or not at all, and **nothing ever yields inward to any of them.** The only destinations on axis three are the glow cards and `lens.vintage_uncoated`. The shelf routes a reader away from ornament and toward glow, every time, and never back. **What it has no card for is the question that decides between them:** how much of this look is committed in the glass, and how much can still be taken out afterwards. The nearest thing that exists is a sentence buried inside a pair field — `lens.diffusion_filter` saying the glow must stay recoverable rather than baked in — with the other half recorded in `lens.veiling_glare`'s own `Avoid when:`, that it cannot be removed later and an overdone frame is gone for good. **The card this shelf wants is the one that asks that out loud before any artefact card is chosen**, and nothing routes a reader to either half of it.

`lens.frame_before_glass`

---

### Ultra-Wide Lens (8 to 16mm)

**Also called:** ultra wide angle, 12mm, 14mm, rectilinear ultra-wide  
**What it is:** A very short focal length that takes in a huge angle of view while keeping straight lines straight, unlike a fisheye. It stretches distance: whatever is close looms large and whatever is far falls away.  
**Effect on the audience:** It swallows the character inside the space and lets the walls and ceiling press in. It also feels invasive, because the camera has to get physically close to fill the frame.  
**Used for and where it works best:** Entering a vast space (a temple, a throne room, a factory) when you want the architecture to beat the human being. In horror the room reads wider than it should and the empty corner becomes a threat. In vertical short form and action sports, close movement explodes in frame and the speed reads multiplied.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, 3D CG Animation, Game Cinematic / Gameplay, Travel / Real Estate / Hospitality, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Horror, Psychological Horror, Sci-Fi, Dystopia / Post-Apocalyptic, Heritage (civilisation-focused), Historical / Biopic, Action, Fantasy / Epic, Surreal / Absurdist, Cyberpunk  
**Avoid when:** Close on a face it bulges the nose and forehead, so keep it away from romance and straight portrait coverage; in portrait photography it belongs to the environmental portrait, where the figure stays small and the space carries the picture. Across a long dialogue scene it tires the eye.  
**Prompt:** `ultra wide 14mm lens, camera close to the subject, walls and ceiling sweeping into frame, strong converging lines, deep focus`  
**Yields to:** `lens.portrait_65_85` — Close on a face, romance or portrait coverage.  
`lens.ultra_wide`

### Wide Lens (18 to 24mm)

**Also called:** 18mm, 21mm, 24mm, wide angle  
**What it is:** The working wide: it keeps the whole environment in frame with the character and still holds a usable face shape as long as you do not get too close. Any camera movement on it reads stronger and faster.  
**Effect on the audience:** It tells the viewer "you are standing here with them". It gives energy, presence and immediacy, and it gives walking and running real weight.  
**Used for and where it works best:** The establishing shot you want alive rather than static, and action where the camera travels with the bodies. In documentary, the cramped room, the market, the interview where the place is part of the testimony. In heritage work, the monument with a small figure in it so the scale reads.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Game Cinematic / Gameplay, Travel / Real Estate / Hospitality, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Action, Adventure, Drama, Verite / Observational, Heritage (civilisation-focused), Historical / Biopic, War, Survival, Road Movie, Comedy  
**Avoid when:** On an intimate close-up it pushes the viewer away instead of pulling them in. For formal portraiture it wrecks the proportions; in portrait photography it serves the environmental portrait, where the place is part of the testimony.  
**Prompt:** `24mm wide lens, character grounded inside the environment, camera moving with them, natural perspective, sharp background detail`  
**Yields to:** `lens.portrait_65_85` — Intimate close-up or formal portraiture.  
`lens.wide_18_24`

### Moderate Wide (27 to 35mm)

**Also called:** 28mm, 32mm, 35mm, the modern default  
**What it is:** The most used focal length in modern cinema: slightly wider than the eye, so it keeps context without obvious distortion. The face stays honest and the background stays readable.  
**Effect on the audience:** Intelligent neutrality. The viewer sees the character and their world at once and never notices the lens at all.  
**Used for and where it works best:** The master and the dialogue in modern drama, the walk and talk, the over the shoulder where you still want the room alive behind the face. In series work it is the safe length that lets you cut around a scene without the sense of place changing.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Documentary Feature, Interview / Video Podcast, Music Video, 3D CG Animation, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Drama, Crime / Procedural, Thriller / Suspense, Comedy, Coming of Age, Slice of Life, Mystery / Whodunit, Political Thriller, Legal Drama, Romance  
**Avoid when:** Shoot the whole film at this length and the images stop having an opinion. Change the focal length when the character's state changes.  
**Prompt:** `35mm lens, medium shot, character and room both readable, natural perspective, soft but present background`  
`lens.wide_27_35`

### Normal Lens (40 to 50mm)

**Also called:** 40mm, 50mm, standard lens, the human eye lens  
**What it is:** The focal length whose perspective sits closest to human sight: it neither stretches distance nor compresses it. What lands in frame is roughly what your own eye would see.  
**Effect on the audience:** Honesty. You feel no intervention from the camera, so you trust the image and believe the character.  
**Used for and where it works best:** Serious dialogue, the confession, the documentary interview, any beat where you want the audience to judge the character with the lens neither flattering nor exposing them. In heritage documentary, the statue or the relief seen from an honest distance with no exaggeration.  
**Best in:** formats: Feature Film, Short Film, Documentary Feature, Interview / Video Podcast, Heritage / Historical Documentary, Drama Series Episode, Stop Motion, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Drama, Verite / Observational, Historical / Biopic, Heritage (civilisation-focused), Tragedy, Mystery / Whodunit, Crime / Procedural, Faith / Biblical Epic, Slice of Life, Psychological / Arthouse  
**Avoid when:** When you want a loud stylistic signature, the normal lens gives you none. In tight locations it also forces you back further than the room allows.  
**Prompt:** `50mm lens, eye level, natural human perspective, no distortion, medium close-up, clean and honest framing`  
**Yields to:** `lens.wide_18_24` — Tight location that forces the camera too far back.  
`lens.normal_40_50`

### Portrait Lens (65 to 85mm)

**Also called:** 65mm, 75mm, 85mm, beauty lens  
**What it is:** A slightly long focal length that flattens facial features in a flattering way and melts the background behind them. The camera stays back while the face still fills the frame.  
**Effect on the audience:** It isolates the character from their world and makes them the only truth in the picture. Intimacy without invasion.  
**Used for and where it works best:** The emotional close-up, the beat of the tear or the decision, the love scene, and any fashion or commercial work selling a face. In romantic series and shojo anime it is the default language of feeling.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Fashion Film, Anime (Japanese 2D), 3D CG Animation, Soap Opera / Telenovela, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Romance, Melodrama, Drama, Shojo (anime romance), Rom-Com, Tragedy, Musical, Coming of Age, Gothic / Vampire  
**Avoid when:** In a scene where the location carries information you lose the location entirely. In physical comedy it severs the body from the gag.  
**Prompt:** `85mm portrait lens, tight close-up, background fully melted into soft bokeh, flattering flat facial perspective`  
**Yields to:** `lens.wide_18_24` — The location or the whole body carries the information.  
`lens.portrait_65_85`

### Telephoto (100 to 200mm)

**Also called:** 100mm, 135mm, 180mm, 200mm, long lens  
**What it is:** A long focal length that brings the far close, stacks the planes on top of each other and lets depth fall off fast. It needs real distance between camera and subject.  
**Effect on the audience:** It turns the viewer into an observer rather than a participant. It feels like surveillance or like a siege, and the character has no idea you are there.  
**Used for and where it works best:** The surveillance shot, the beat of loneliness inside a crowd, the character who walks and never seems to advance because the background stays put behind them. In wildlife and sports documentary it is the only way to reach the subject without spooking it.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, News Report / Reportage, Sports Broadcast / Sports Film, Trailer / Teaser, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Thriller / Suspense, Crime / Procedural, Spy / Espionage, Mystery / Whodunit, Drama, War, Nature / Wildlife, Sports Drama, Noir / Neo-Noir, Political Thriller  
**Avoid when:** In a tight location you simply cannot use it. In a scene where you want the viewer inside the room, the long lens puts them outside it.  
**Prompt:** `135mm telephoto, subject isolated from a busy background, compressed layers, shallow depth of field, camera far from the subject`  
**Yields to:** `lens.wide_18_24` — You want the viewer inside the room, not outside it.  
`lens.tele_100_200`

### Super-Telephoto (300mm and up)

**Also called:** 300mm, 400mm, 600mm, long glass  
**What it is:** The far end of the ladder: compression becomes extreme and foreground and background glue together like stacked cut-outs. Heat haze and dust become visible as a shimmering wave.  
**Effect on the audience:** It kills distance, and distance is hope. The character moves and never arrives, so you feel entrapment or despair.  
**Used for and where it works best:** The desert walk, the escape that never ends, the crowd dissolving in sun, the huge sun disc sitting behind a figure at dusk. In sports and wildlife, the impossible closeness on an athlete's face or an animal.  
**Best in:** formats: Feature Film, Documentary Feature, Documentary Series, Sports Broadcast / Sports Film, Trailer / Teaser, Heritage / Historical Documentary, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Western, War, Survival, Nature / Wildlife, Drama, Thriller / Suspense, Dystopia / Post-Apocalyptic, Historical / Biopic, Tragedy, Sports Drama  
**Avoid when:** The smallest shake becomes an earthquake in frame, so it demands real support. Do not use it in a scene that needs clear geography, because it lies about distance.  
**Prompt:** `400mm super telephoto, extreme compression, heat haze shimmering between the camera and a walking figure, giant sun disc behind them`  
**Yields to:** `lens.normal_40_50` — A scene that needs honest, readable geography.  
`lens.super_tele`

### Fisheye Lens

**Also called:** 8mm fisheye, circular fisheye, full frame fisheye  
**What it is:** An extreme wide optic that makes no attempt to correct curvature, so straight lines bow and the edges pull away. The angle of view approaches a hemisphere.  
**Effect on the audience:** It breaks the realism of the image instantly. The world turns rubbery, so it reads as madness, intoxication or mockery.  
**Used for and where it works best:** Dreams and hallucination, the drunk or drugged scene, and the mockery of court and power when you want the room itself to feel sick. In skate, vertical short form and action sports, going close on the board or the bike gives an energy no other lens delivers.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Feature Film, Experimental / Art Film, Game Cinematic / Gameplay, Meme / Comedy Edit, Anime (Japanese 2D), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Surreal / Absurdist, Psychological / Arthouse, Dark Comedy / Satire, Comedy, Horror, Psychological Horror, Cyberpunk, Fantasy / Epic, Action  
**Avoid when:** Used without a reason it turns the film into amateur video. Keep it out of any serious beat you want the audience to believe.  
**Prompt:** `8mm fisheye lens, heavy barrel curvature, straight walls bowing outward, subject close to the glass, wide distorted room behind them`  
**Example:** The Favourite (2018), the wide and fisheye lenses that warp the palace interiors.  
**Yields to:** `lens.ultra_wide` — A serious beat that still needs a huge angle of view.  
`lens.fisheye`

### Wide-Angle Distortion as Style

**Also called:** wide-angle stretch, Gilliam look, distorted perspective  
**What it is:** Deliberately placing a wide lens at a close, odd angle so proportions stretch: a big head, a shrunken body, leaning walls. Here the distortion is the message, not a flaw.  
**Effect on the audience:** It makes the viewer uncomfortable and suspicious of everything inside the frame. Authority becomes grotesque and bureaucracy becomes a nightmare.  
**Used for and where it works best:** Dark comedy and dystopia when you want the world itself to feel broken, and psychological horror when the character loses their balance. Strongest in the office, the courtroom or the palace scene you intend to ridicule.  
**Best in:** formats: Feature Film, Short Film, Music Video, Experimental / Art Film, Trailer / Teaser, 2D Animation (Western / Cartoon), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Dark Comedy / Satire, Dystopia / Post-Apocalyptic, Surreal / Absurdist, Psychological / Arthouse, Psychological Horror, Horror, Comedy, Cyberpunk  
**Avoid when:** Applied to every scene it loses its bite and becomes wallpaper. Keep it away from any beat that asks for honest sympathy with the character.  
**Prompt:** `18mm wide lens very close to the face from a low angle, head large and body receding, walls leaning inward, exaggerated perspective`  
**Example:** Brazil (1985), Terry Gilliam's distorted wide-angle interiors.  
**Yields to:** `lens.normal_40_50` — A beat asking for honest sympathy with the character.  
`lens.wide_distortion`

### Wide Lens Close to the Face

**Also called:** wide close-up, horror close-up, invasive wide  
**What it is:** Bringing a wide lens to within inches of the face, so the face reads huge while the entire room behind it stays visible and sharp.  
**Effect on the audience:** It breaks social distance. The viewer feels closer than they are allowed to be, and at the same time sees the empty space behind the character.  
**Used for and where it works best:** The horror beat where you want the face close and the open door behind it, or the moment of breakdown and screaming. In thriller, the interrogation where the audience should feel the breath. In vertical short form it is the hook that stops the scroll.  
**Best in:** formats: Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Trailer / Teaser, Music Video, Drama Series Episode, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design | genres: Horror, Psychological Horror, Slasher, Thriller / Suspense, Supernatural Horror, Dark Comedy / Satire, Crime / Procedural, Survival
**Avoid when:** It rarely works on a romantic or dignified beat, because the distortion cancels the tenderness; the exception is when you want the romance itself to look grotesque. Repeated inside the same scene the shock evaporates.  
**Prompt:** `21mm wide lens inches from the face, face filling frame with visible distortion, the room and an open door still sharp behind them`  
**Yields to:** `lens.portrait_65_85` — A romantic or dignified close beat.  
`lens.wide_close_face`

### Telephoto Compression

**Also called:** lens compression, stacking, flattening  
**What it is:** A long lens makes distant planes look adjacent, so a person, a car and a building sit on almost the same plane. This is not about size, it is about the relationship between distances.  
**Effect on the audience:** It cancels progress. The character runs and never gets nearer, and the danger behind them stays glued to their back.  
**Used for and where it works best:** The desperate run, the chase you want to feel hopeless, the crowd packed with no air in it, the queue that never ends. In heritage work, a row of columns or palms compresses into a single solid wall.  
**Best in:** formats: Feature Film, Trailer / Teaser, Music Video, Documentary Feature, Drama Series Episode, Heritage / Historical Documentary, Sports Broadcast / Sports Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Thriller / Suspense, Drama, War, Survival, Dystopia / Post-Apocalyptic, Sports Drama, Tragedy, Crime / Procedural, Historical / Biopic  
**Avoid when:** When you need the audience to feel the ground the character actually covered, compression lies to them. It also needs a long shooting distance that is not always available.  
**Prompt:** `200mm telephoto, runner moving toward camera but never getting closer, background layers stacked flat behind them, compressed perspective`  
**Example:** The Graduate (1967), the long-lens run toward the church.  
**Yields to:** `lens.wide_18_24` — The audience must feel the ground actually covered.  
`lens.tele_compression`

### Long-Lens Isolation in a Crowd

**Also called:** crowd isolation, picking a face out of a crowd  
**What it is:** A long lens wide open on one face inside a mass of people, so that face is the only sharp thing and everyone else becomes blocks of colour drifting in front and behind.  
**Effect on the audience:** Loneliness inside noise. The viewer feels the character does not belong to the place even though they are standing in the middle of it.  
**Used for and where it works best:** The beat where a character hears the news in a market, a station or a wedding, or the watcher tracking a target through a crowd. In music video, the singer holds still while the crowd streams past as melted colour.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Documentary Feature, Trailer / Teaser, News Report / Reportage, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Drama, Thriller / Suspense, Spy / Espionage, Crime / Procedural, Romance, Tragedy, Melodrama, Political Thriller, Coming of Age  
**Avoid when:** If the crowd itself is the information, isolation hides the story. It also needs distance, so it fails in a tight room.  
**Prompt:** `180mm lens wide open, one sharp face in a dense moving crowd, foreground and background bodies blurred into drifting colour`  
**Yields to:** `lens.deep_focus` — The crowd itself is the information.  
`lens.long_lens_isolation`

### Macro Lens

**Also called:** macro optics, 1:1 magnification, close focus lens  
**What it is:** An optic that magnifies a small object until it reaches life size on the sensor or larger. Working distance is tiny and depth of field collapses to millimetres.  
**Effect on the audience:** It opens a world the eye cannot see, so it delivers wonder and discovery, and it puts the texture of the material into your fingertips.  
**Used for and where it works best:** Product, food and craft commercials selling texture, plus science and nature documentary. In heritage documentary, a finger tracking a cuneiform wedge or a thread in a weave. The difference from the macro shot as a size is that this record is the optical tool and its problems: paper thin focus and lighting that has nowhere to go.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), 3D CG Animation, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Still Life Photography, Wildlife Photography | genres: Nature / Wildlife, Science / Educational, Heritage (civilisation-focused), Historical / Biopic, Surreal / Absurdist, Body Horror, Horror, Family
**Avoid when:** The smallest vibration throws the subject completely out of focus, so it demands a locked platform. On a human face the result turns strange and cruel.  
**Prompt:** `macro lens at life size magnification, razor thin plane of focus across the surface texture, slow focus drift, soft directional light`  
**Yields to:** `lens.portrait_65_85` — Close on a human face, where macro turns cruel.  
`lens.macro`

### Probe Lens

**Also called:** snorkel lens, borescope lens, Laowa probe  
**What it is:** A long thin tube of glass whose front element enters places a camera body never could: inside a glass, between plants, through a small hole. It combines macro magnification with a wide angle and surprising depth.  
**Effect on the audience:** It shrinks the viewer and sends them travelling inside the world. It gives a magical transition between two scales.  
**Used for and where it works best:** Food and drink commercials where the camera dives into the glass and out again, close nature work, and the transition that enters a hole and emerges somewhere else. In heritage documentary, travelling between the columns of a model or into a carved recess.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Explainer, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Nature / Wildlife, Science / Educational, Heritage (civilisation-focused), Surreal / Absurdist, Family, Comedy, Horror, Fantasy / Epic  
**Avoid when:** It needs a lot of light because it is optically slow, and in low light it falls apart. Do not deploy it as a stunt inside a quiet dramatic scene.  
**Prompt:** `probe lens travelling low through the tabletop, entering the narrow gap, wide angle with macro magnification, everything sharp front to back`  
**Yields to:** `lens.macro` — Low light, where the slow probe optic falls apart.  
`lens.probe`

### Tilt-Shift / Miniature Faking

**Also called:** perspective control lens, miniature effect, diorama look  
**What it is:** A lens whose focal plane can be tilted or shifted relative to the sensor. Tilting leaves one sharp band with everything else melting away; shifting straightens converging building lines.  
**Effect on the audience:** Tilt plus a high angle turns a city into a plastic toy. The viewer becomes a small god looking down.  
**Used for and where it works best:** The city time montage, the playful opening title sequence, the documentary beat that wants to lighten its own seriousness. Shift is the architectural tool: shooting a facade or a ziggurat without the verticals converging — and where that is the whole job, with no miniature tilt, the card is `lens.shift_perspective_control`.  
**Best in:** formats: Documentary Feature, Documentary Series, Title Sequence / Opening Credits, Commercial / TVC, Explainer, Travel / Real Estate / Hospitality, Vertical Short-Form (Reels, Shorts, TikTok), Corporate / Training, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Comedy, Family, Science / Educational, Heritage (civilisation-focused), Historical / Biopic, Slice of Life, Dark Comedy / Satire, Surreal / Absurdist  
**Avoid when:** It has been worn out by city videos, so use it only when shrinking the world means something in the story. On a serious beat it trivialises the event.  
**Prompt:** `tilt-shift lens from a high angle over the city, one narrow band in focus, everything above and below melting, miniature diorama feeling`  
**Yields to:** `lens.shift_perspective_control` — A serious beat that must not read as a toy.  
`lens.tilt_shift`

### Anamorphic Lens

**Also called:** scope lens, 2x squeeze, 1.8x squeeze, CinemaScope glass  
**What it is:** A lens that squeezes the image horizontally onto the sensor and is unsqueezed in post to give a wide frame. Its signature is oval bokeh, horizontal flare, softer edges and a slight stretch when you get close.  
**Effect on the audience:** It delivers instant cinematic scale. Without knowing why, the viewer registers a big film rather than a video.  
**Used for and where it works best:** Epic, science fiction, music video and trailer work, anything you want to feel larger than the screen. The shot that gains the most is a single figure at one edge with a wide emptiness beside them.  
**Best in:** formats: Feature Film, Trailer / Teaser, Music Video, Commercial / TVC, Title Sequence / Opening Credits, Game Cinematic / Gameplay, 3D CG Animation, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Sci-Fi, Space Opera, Fantasy / Epic, Mythology / Ancient Epic, Western, Action, Historical / Biopic, Heritage (civilisation-focused), Noir / Neo-Noir, Musical  
**Avoid when:** In interviews and simple documentary work it feels affected. In a 9:16 vertical the wide frame is gone anyway, so there is nothing to gain.  
**Prompt:** `shot on anamorphic lenses, 2.39:1 frame, oval bokeh, horizontal blue flare streaking across the lights, soft falloff at the edges`  
**Example:** Star Wars (1977), shot in Panavision anamorphic.  
**Yields to:** `lens.spherical` — Interview or plain documentary, where scope feels affected.  
`lens.anamorphic`

### Spherical Glass / Spherical versus Anamorphic

**Also called:** spherical lens, flat lens, non-anamorphic  
**What it is:** The ordinary lens that does not squeeze: circular bokeh, round flare, even sharpness, and any wide frame comes from cropping rather than from the glass. It is faster, lighter and more precise than anamorphic.  
**Effect on the audience:** Cleanliness and neutrality. The image does not announce itself, so the viewer sees the scene rather than the lens.  
**Used for and where it works best:** Grounded drama, documentary, horror that lives on believability, and any work in tight spaces or low light. Choose spherical when you want the audience to forget the camera, anamorphic when you want them to notice it.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Interview / Video Podcast, News Report / Reportage, Short Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Drama, Verite / Observational, Horror, Crime / Procedural, Historical / Biopic, Heritage (civilisation-focused), Mystery / Whodunit, Legal Drama, Medical Drama, Tragedy  
**Avoid when:** If the brief asks for an epic visual signature, spherical can read as plain. Do not mix the two systems inside one scene without a reason.  
**Prompt:** `spherical prime lens, clean neutral rendering, circular bokeh, even sharpness across the frame, no flare artefacts`  
**Yields to:** `lens.anamorphic` — The brief asks for an epic visual signature.  
`lens.spherical`

### Large Format

**Also called:** full frame, 65mm sensor, LF, Alexa 65  
**What it is:** A larger sensor lets you use a longer lens for the same framing, so you get the same angle of view with less depth of field and a softer transition from sharp to soft.  
**Effect on the audience:** The face feels sculpted and lifted off the background, and the image reads both intimate and expansive at once.  
**Used for and where it works best:** Epics, prestige drama and luxury advertising, and any shot where you want a close face and a wide environment in the same frame. It is strong in heritage work when you want the monument and the face together without losing separation.  
**Best in:** formats: Feature Film, Commercial / TVC, Fashion Film, Trailer / Teaser, Heritage / Historical Documentary, Music Video, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Mythology / Ancient Epic, Drama, Sci-Fi, Fantasy / Epic, War, Romance, Tragedy  
**Avoid when:** Focus becomes unforgiving, so in fast action and live documentary you will lose takes. Skip it when the brief actually needs deep focus.  
**Prompt:** `large format look, wide field of view with shallow separation, sculpted face lifted off a vast background, gentle focus falloff`  
**Example:** The Revenant (2015), shot on the Alexa 65 large format camera.  
**Yields to:** `lens.deep_focus` — The brief actually needs everything sharp.  
`lens.large_format`

### Split Diopter

**Also called:** split-field diopter, split-field filter, split focus  
**What it is:** Half a close-up lens placed in front of the taking lens, so one half of the frame focuses close and the other half focuses far. Between them sits a soft seam you must hide along an edge in the composition.  
**Effect on the audience:** Two pieces of information separated in space become sharp at the same instant, creating a locked tension: the near face and the far threat in a single decision.  
**Used for and where it works best:** Thriller and crime: a near face at the edge of frame and a figure entering a far door, both razor sharp. It shines when you refuse to cut or pull focus, because either would break the simultaneity. In mystery, a clue on the near table with a witness far behind it.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Trailer / Teaser, Music Video, Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Thriller / Suspense, Crime / Procedural, Mystery / Whodunit, Noir / Neo-Noir, Horror, Psychological Horror, Spy / Espionage, Drama  
**Avoid when:** With no natural edge to bury the seam it becomes visible and throws the audience out of the scene. Do not use it purely to show off.  
**Prompt:** `split diopter shot, near face at the left edge razor sharp, distant doorway across the room equally sharp, seam hidden along a vertical wall line`  
**Example:** Blow Out (1981), Brian De Palma's split diopter compositions.  
**Yields to:** `lens.deep_focus` — No natural edge to bury the seam.  
`lens.split_diopter`

### Close-Up Diopter

**Also called:** plus diopter, close-up filter, achromatic diopter  
**What it is:** A magnifying element that screws in front of any lens and shortens its minimum focus distance, giving you magnification without changing lenses. It trades away infinity focus.  
**Effect on the audience:** It makes the small object feel large, close and personal, and it melts the background more than you expect.  
**Used for and where it works best:** The insert shot in commercials and food work: the ring, the bullet, the grain of salt, without swapping glass mid setup. It is strong in documentary and vertical work because it is cheap, fast and light in the bag.  
**Best in:** formats: Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Explainer, Corporate / Training, Drama Series Episode, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Crime / Procedural, Mystery / Whodunit, Family, Science / Educational, Nature / Wildlife, Romance, Thriller / Suspense, Comedy  
**Avoid when:** Cheap ones smear the corners and fringe the edges with colour. Remember that infinity focus is gone while it is mounted.  
**Prompt:** `close-up diopter on a 50mm, extreme close focus on the small object, background dissolved, shallow plane and warm key light`  
**Yields to:** `lens.macro` — You need clean corners or infinity focus kept.  
`lens.diopter`

### Mirror Lens / Catadioptric

**Also called:** reflex lens, donut bokeh lens, 500mm mirror  
**What it is:** A very long lens built with mirrors instead of glass alone, so it stays short and light. Its unique signature is that out of focus highlights render as rings, hollow in the middle.  
**Effect on the audience:** Ring shaped bokeh feels strange, dated and slightly unsettling, like a memory that did not record correctly.  
**Used for and where it works best:** Music video and experimental work when you want an optical signature nothing else gives, and the nineteen seventies surveillance look. Trees behind the subject or sun on water break into drifting rings.  
**Best in:** formats: Music Video, Experimental / Art Film, Short Film, Documentary Feature, AI-Generated Clip, Feature Film, Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Psychological / Arthouse, Surreal / Absurdist, Noir / Neo-Noir, Thriller / Suspense, Spy / Espionage, Romance, Drama  
**Avoid when:** It has no working aperture and low contrast, so a scene that needs clean rendering will feel weak. The rings become noisy against a background full of highlights.  
**Prompt:** `catadioptric mirror lens, long focal length, out of focus highlights rendering as bright hollow rings behind the subject`  
**Yields to:** `lens.super_tele` — Long reach that needs clean contrast and a real aperture.  
`lens.mirror_lens`

### Soft Focus Lens

**Also called:** soft focus optic, glamour lens, Imagon  
**What it is:** A lens designed on purpose to be soft: it carries the detail but wraps a gentle halo around it instead of cutting hard. Unlike an out of focus image, this one is focused, just soft.  
**Effect on the audience:** It gives dream, memory and old time. The face feels revered or beloved rather than documented.  
**Used for and where it works best:** The tender flashback, the face of the mother or the beloved in memory, the dream sequence in melodrama. In fashion and premium advertising it delivers flawless skin with no digital intervention.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Fashion Film, Drama Series Episode, Soap Opera / Telenovela, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Romance, Melodrama, Gothic / Vampire, Fairy Tale, Musical, Drama, Fantasy / Epic, Faith / Biblical Epic  
**Avoid when:** On a realistic scene it reads as a lie and it hides the actor's work. On a shot whose information must be read it usually takes that information with it, because the softness eats the edges; the exception is when the blur itself is the information, a memory or a failing eye.  
**Prompt:** `soft focus lens, gentle halo blooming around the highlights, detail retained but softened, dreamy skin rendering, warm light`  
**Yields to:** `lens.diffusion_filter` — The information must stay readable while still soft.  
`lens.soft_focus`

### Selective Focus Optic

**Also called:** Lensbaby, sweet spot optic, tilting optic  
**What it is:** An optic you tilt by hand so a small sharp sweet spot lands wherever you aim it while everything around it pulls into softness and swirl. Like tilt-shift but wilder and far less disciplined.  
**Effect on the audience:** It forces the viewer's eye onto one point and lets the rest of the frame feel like a hallucination.  
**Used for and where it works best:** The dream, the memory and the dizzy beat in music video and experimental work, and the title sequence you want to feel handmade. In wedding and fashion coverage, one strange frame among clean ones gives variety.  
**Best in:** formats: Music Video, Experimental / Art Film, Wedding / Event Film, Short Film, Title Sequence / Opening Credits, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Psychological / Arthouse, Surreal / Absurdist, Romance, Fantasy / Epic, Gothic / Vampire, Drama, Coming of Age  
**Avoid when:** It is useless on any shot that needs focus discipline or must cut with conventional coverage. Overused it becomes an obvious gimmick.  
**Prompt:** `selective focus optic, one small sharp sweet spot on the eyes, the rest of the frame smearing and swirling outward`  
**Yields to:** `lens.tilt_shift` — The shot needs disciplined, repeatable focus placement.  
`lens.selective_focus_optic`

### Lens Whacking / Free-Lensing

**Also called:** free lensing, lens wobble, detached lens  
**What it is:** You unseat the lens slightly from the body and hold it by hand, letting light leak through the gap while the focal plane tilts and drifts. No two takes come out the same.  
**Effect on the audience:** It gives fragility and human randomness. The image feels like a memory rather than a recording.  
**Used for and where it works best:** Flashbacks, music video and sensory title work, and the breakdown scene where you want the image itself to come apart. It is strong on nature and sun material because the leak becomes part of the beauty.  
**Best in:** formats: Music Video, Experimental / Art Film, Short Film, Wedding / Event Film, Title Sequence / Opening Credits, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Psychological / Arthouse, Surreal / Absurdist, Romance, Drama, Coming of Age, Tragedy, Fantasy / Epic  
**Avoid when:** It invites dust onto the sensor and the result cannot be repeated, so it is a risky place to put a key story beat; the exception is when you can shoot it many times and choose, because the accident is the whole appeal. In dialogue coverage it simply distracts.  
**Prompt:** `free-lensed look, tilted drifting plane of focus, warm light leaking in from the edge of frame, organic unstable softness`  
**Yields to:** `lens.selective_focus_optic` — A key beat that must be repeatable and safe.  
`lens.lens_whacking`

### Vintage Uncoated Glass

**Also called:** uncoated lenses, period glass, low contrast vintage optics  
**What it is:** Older lenses with no anti-reflective coating or only a simple one, so they give lower contrast, lifted blacks, easy flare and soft corners with a sharp centre.  
**Effect on the audience:** It takes the digital hardness out of the image and makes it feel photographed in another era.  
**Used for and where it works best:** Period work and drama you want intimate rather than clinical, and heritage material you want to feel pulled out of an archive. It is excellent on faces because the softness handles skin without digital smoothing.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Music Video, Short Film, Commercial / TVC, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Romance, Noir / Neo-Noir, Gothic / Vampire, Tragedy, Western, War  
**Avoid when:** In a shot that needs fine detail or fights a strong backlight it collapses and loses contrast. Do not intercut it with modern glass inside the same scene.  
**Prompt:** `vintage uncoated lenses, lifted blacks, low contrast, gentle edge softness, easy blooming flare from the practical lamps`  
**Yields to:** `lens.spherical` — Fine detail, or a strong backlight it cannot fight.  
`lens.vintage_uncoated`

### Swirly Bokeh

**Also called:** Petzval swirl, Helios swirl, cat eye bokeh  
**What it is:** Certain older optical designs drag the out of focus highlights at the edges into a spiral around the centre of frame while the middle stays calm and sharp.  
**Effect on the audience:** It drags the viewer's eye to the centre by force and lends a sense of magic, dream and old time.  
**Used for and where it works best:** The love scene in a garden or among trees, where leaves and light behind the subject turn into a vortex. Strong in fantasy, fairy tale and music video, and in the flashback you want enchanted rather than factual.  
**Best in:** formats: Music Video, Feature Film, Short Film, Wedding / Event Film, Fashion Film, Title Sequence / Opening Credits, Experimental / Art Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Romance, Fantasy / Epic, Fairy Tale, Gothic / Vampire, Melodrama, Surreal / Absurdist, Drama, Shojo (anime romance)  
**Avoid when:** It needs a background full of highlights or foliage; against a flat wall you will see nothing. In a realistic scene it feels put on.  
**Prompt:** `vintage Petzval style lens, swirling bokeh spiralling around the edges of frame, sharp centre, backlit leaves behind the subject`  
**Yields to:** `lens.soft_focus` — Flat background with no highlights to swirl.  
`lens.swirly_bokeh`

### Diffusion Filters

**Also called:** Pro-Mist, Black Pro-Mist, Glimmerglass, Black Satin, Hollywood Black Magic  
**What it is:** Glass in front of the lens holding fine particles that scatter light a little: highlights grow a halo, blacks lift slightly and skin softens without losing detail. Each family has its own character.  
**Effect on the audience:** It removes digital hardness and gives warmth, dream and luxury. The viewer feels the atmosphere before they understand why.  
**Used for and where it works best:** Romance, flashback and premium advertising, and the city night scene where every practical lamp grows a halo. In heritage work, firelight and candles inside a temple gain an older breath. Pick the strength per shot: light for dialogue, heavy for memory.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Fashion Film, Wedding / Event Film, Soap Opera / Telenovela, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Romance, Melodrama, Drama, Gothic / Vampire, Historical / Biopic, Heritage (civilisation-focused), Noir / Neo-Noir, Musical, Fantasy / Epic  
**Avoid when:** Too much strength turns the image milky and buries shadow detail, and that cannot be taken out later. In serious documentary and news it costs you credibility.  
**Prompt:** `light diffusion filter on the lens, gentle halation around the practical lights, slightly lifted blacks, soft creamy skin, cinematic haze`  
**Yields to:** `lens.halation` — The glow must stay recoverable, not baked in.  
`lens.diffusion_filter`

### ND Filter as a Creative Tool

**Also called:** neutral density, ND, variable ND  
**What it is:** Neutral grey glass that cuts the amount of light entering without shifting colour. It lets you shoot wide open in full sun, or drag the shutter until movement smears.  
**Effect on the audience:** It frees your aesthetic decision from the available light. You choose the depth and the motion you want instead of the ones the sun dictates.  
**Used for and where it works best:** The midday desert or rooftop shot when you want the background melted and the figure isolated. For daylight long exposure, water turns to silk and passers by turn into drifting ghosts, which works beautifully in heritage, travel and commercial work.  
**Best in:** formats: Feature Film, Commercial / TVC, Music Video, Travel / Real Estate / Hospitality, Documentary Feature, Heritage / Historical Documentary, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Romance, Nature / Wildlife, Survival, Western, Surreal / Absurdist  
**Avoid when:** Cheap ND throws a green or magenta cast that is painful to correct. In fast changing live coverage the swapping costs you the moment.  
**Prompt:** `heavy ND filter, wide aperture in bright midday sun, shallow depth of field, slow shutter smearing the passing crowd into ghosts`  
`lens.nd_filter`

### Graduated ND Filter

**Also called:** grad ND, hard grad, soft grad  
**What it is:** Glass that is dark at one end, clear at the other, with a graded transition between them. You place the dark half over the sky so the ground can hold its own exposure.  
**Effect on the audience:** It gives the sky back the drama it was about to lose to a blown white. The image reads balanced and large.  
**Used for and where it works best:** The exterior establishing shot in desert, river or ruins when you want the clouds to survive. Strong in western, heritage and travel work, and at sunset when you want the figure in silhouette against a coloured sky.  
**Best in:** formats: Feature Film, Documentary Feature, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Commercial / TVC, Trailer / Teaser, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Western, Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Adventure, War, Survival, Drama  
**Avoid when:** If the horizon is broken by a mountain or a building, the transition prints a grey band across it. On a very wide lens the graduation becomes visible.  
**Prompt:** `graduated ND holding the sky, dramatic clouds retained above a balanced foreground, silhouetted figure on the horizon line`  
**Yields to:** `lens.polariser` — Broken horizon, where a grad prints a grey band.  
`lens.grad_nd`

### Polariser

**Also called:** circular polariser, CPL, pola  
**What it is:** A filter you rotate in front of the lens to select which angle of reflected light passes. Rotating it kills reflections on glass and water, darkens the sky and deepens colour saturation.  
**Effect on the audience:** It lets the viewer see inside things: into the car, under the surface of the water, behind the shop window. The image reads cleaner and richer.  
**Used for and where it works best:** The car scene where you want the driver's face rather than a mirror of the sky, and the river or pool shot where you want the stones under the water. In heritage work, killing the shine on museum vitrine glass so the tablet can be read.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Commercial / TVC, Product Video / Motion Design, Feature Film, News Report / Reportage, Corporate / Training, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Nature / Wildlife, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Drama, Crime / Procedural, Adventure, Verite / Observational  
**Avoid when:** On a very wide lens the sky darkens unevenly and looks fake. It also eats light, which becomes a burden in low light.  
**Prompt:** `circular polariser, reflections removed from the glass, deep saturated sky, stones visible under the clear water`  
`lens.polariser`

### Star Filter

**Also called:** cross screen filter, 4 point star, 6 point star  
**What it is:** Glass etched with fine lines that turns every point of light into a star with crossing rays. The number of points depends on the filter. A natural sunstar comes from stopping the iris down instead.  
**Effect on the audience:** It gives instant festive sparkle. Lights become jewellery and the scene starts to feel like an occasion.  
**Used for and where it works best:** The musical number, the music video, the wedding and the nightclub beat, plus the chandelier or candelabra in a hotel shot. It is the right tool for nineteen seventies and eighties variety television nostalgia.  
**Best in:** formats: Music Video, Concert / Live Event, Wedding / Event Film, Commercial / TVC, Title Sequence / Opening Credits, Dance Film, Vertical Short-Form (Reels, Shorts, TikTok), Soap Opera / Telenovela, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Musical, Romance, Comedy, Melodrama, Family, Fantasy / Epic, Dark Comedy / Satire  
**Avoid when:** On a serious or grieving beat it kills the emotion and turns it into an advert. Do not put it on a shot with many highlights or the frame turns to chaos.  
**Prompt:** `star filter on the lens, every practical light bursting into a four point star, festive sparkle across the night interior`  
**Yields to:** `lens.diffusion_filter` — A serious beat where sparkle would trivialise the lights.  
`lens.star_filter`

### Streak Filter

**Also called:** blue streak filter, anamorphic fake, flare filter  
**What it is:** Glass carrying a single etched line that stretches every highlight into a coloured horizontal bar, giving an anamorphic style flare on an ordinary spherical lens.  
**Effect on the audience:** It adds a cinematic science fiction layer in one move and turns any background light into an event.  
**Used for and where it works best:** Music video, trailer and commercial work when you want the anamorphic feeling without the cost of the glass. Strong in city night, laboratory and vehicle scenes, and in vertical work because the streak grabs attention fast.  
**Best in:** formats: Music Video, Trailer / Teaser, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Game Cinematic / Gameplay, Product Video / Motion Design, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Sci-Fi, Cyberpunk, Action, Thriller / Suspense, Musical, Space Opera, Superhero, Noir / Neo-Noir  
**Avoid when:** It wears out fast and on every shot it becomes noise. In period or honest documentary work it rarely belongs, because it puts a modern lens on old material; the exception is a stylised reconstruction that has already declared itself as one.  
**Prompt:** `blue streak filter, horizontal light streaks stretching from every practical, wet night street, neon reflections`  
**Yields to:** `lens.vintage_uncoated` — Period or honest material needing period optics.  
`lens.streak_filter`

### Shallow Depth of Field

**Also called:** shallow focus, wide open, f/1.4 look  
**What it is:** A wide aperture or a long focal length leaves a very thin sharp band with everything in front and behind it melting. The distance between a nose and an ear can matter.  
**Effect on the audience:** It dictates where the viewer looks, and it delivers separation, luxury and emotion. It can also read as isolation or dream, and it is the language of portraiture.  
**Used for and where it works best:** The emotional close-up, the confession, the beloved's face, and the commercial selling a product cut out of its world. It is very strong in vertical work because the chaotic street behind the face dissolves and stops competing.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Music Video, Fashion Film, Vertical Short-Form (Reels, Shorts, TikTok), Wedding / Event Film, Product Video / Motion Design, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Romance, Drama, Melodrama, Thriller / Suspense, Coming of Age, Tragedy, Shojo (anime romance), Crime / Procedural  
**Avoid when:** Overdone it removes the world entirely and the whole film starts to feel like a car commercial. In a scene carrying information on two planes you will lose one of them.  
**Prompt:** `shallow depth of field at f/1.4, eyes tack sharp, ears already soft, background dissolved into smooth bokeh`  
**Yields to:** `lens.deep_focus` — Information sitting on two planes at once.  
`lens.shallow_dof`

### Deep Focus

**Also called:** deep staging, everything sharp, f/11 look  
**What it is:** A small aperture with a wide lens holds everything sharp from the foreground to the back wall at the same time. It usually needs strong light or a sensitive sensor.  
**Effect on the audience:** It gives the viewer freedom to choose where to look, so they become a partner in the scene rather than a receiver. The relationship between a near figure and a far one reads without a single cut.  
**Used for and where it works best:** The layered scene where two events share one shot: somebody speaking in the foreground while somebody listens at a far doorway. Strong in legal and period drama and in documentary where the location is part of the truth. Orson Welles built whole scenes on it.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Docudrama / Reenactment, Stop Motion, 2D Animation (Western / Cartoon), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Drama, Legal Drama, Historical / Biopic, Heritage (civilisation-focused), Mystery / Whodunit, Crime / Procedural, Political Thriller, Tragedy, War  
**Avoid when:** It is expensive in light, and in low light you end up raising ISO until the image breaks. On an intimate close beat it scatters the eye away from the face.  
**Prompt:** `deep focus, foreground hands and the far doorway both sharp, f/11, wide lens, layered staging front to back`  
**Example:** Citizen Kane (1941), Gregg Toland's deep focus staging.  
**Yields to:** `lens.shallow_dof` — An intimate close beat that must hold the face.  
`lens.deep_focus`

### Hyperfocal Distance

**Also called:** hyperfocal focus, set and forget focus, zone focusing  
**What it is:** You set focus at a calculated distance for the lens and aperture, and everything from half that distance to infinity reads acceptably sharp. No focus pulling during the take.  
**Effect on the audience:** It buys total freedom of movement. Camera and subject can go anywhere and nothing falls out of focus.  
**Used for and where it works best:** Live documentary, street work and demonstrations, drone and FPV shots, and handheld action in tight spaces. Perfect for vertical work when you are shooting alone with nobody pulling focus.  
**Best in:** formats: Documentary Feature, Documentary Series, News Report / Reportage, Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, Travel / Real Estate / Hospitality, Game Cinematic / Gameplay, Sports Broadcast / Sports Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Verite / Observational, True Crime, Action, Adventure, Survival, War, Political Thriller, Nature / Wildlife  
**Avoid when:** If the shot wants isolation and bokeh this is its opposite. In low light you cannot stop down far enough to make it work.  
**Prompt:** `wide lens set to hyperfocal distance, everything from two metres to infinity acceptably sharp, handheld run through the street`  
**Yields to:** `lens.shallow_dof` — The shot wants isolation and bokeh.  
`lens.hyperfocal`

### Bokeh as Texture

**Also called:** bokeh shape, out of focus rendering, background texture  
**What it is:** The shape and quality of everything out of focus: soft circles, anamorphic ovals, hexagons from the iris blades, rings from a mirror lens. The background you choose is what creates the bokeh.  
**Effect on the audience:** It gives the background a mood without letting it be read. The viewer cannot identify what is back there but they feel it. The shape reads too: round discs soft and romantic, stretched ovals anamorphic and cinematic.  
**Used for and where it works best:** The city night scene where street lamps become coloured discs, and the forest or palm grove with sun broken through the leaves. In advertising, place highlights behind the product on purpose so you build sparkle rather than inherit a messy street.  
**Best in:** formats: Commercial / TVC, Music Video, Feature Film, Product Video / Motion Design, Wedding / Event Film, Fashion Film, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Romance, Drama, Noir / Neo-Noir, Cyberpunk, Thriller / Suspense, Musical, Melodrama, Coming of Age  
**Avoid when:** Hexagonal or clipped edge bokeh cheapens the picture. Do not lean on bokeh to hide a background you should have dressed properly.  
**Prompt:** `wide open lens, background city lights rendering as large soft circular bokeh, warm and cool highlights layered behind the subject`  
`lens.bokeh_texture`

### Focus Breathing

**Also called:** lens breathing, focus zoom  
**What it is:** Some lenses shift their angle of view slightly as focus changes, so the frame appears to breathe in and out during a pull. Cine lenses minimise it; stills lenses show it plainly.  
**Effect on the audience:** A small amount feels organic and alive; a large amount reads as a fault and points at the camera.  
**Used for and where it works best:** You can lean into it on purpose in a dream, a fever or the beat where reality turns, because the frame moves without the camera moving. That is the large, leaned-into amount; the slight breath asked for alongside a rack reads instead as a real lens with a body behind it, which is how `move.focus_breathing` uses it for documentary and archival texture. On serious work, know which lens does it so it does not ruin an important focus pull.  
**Best in:** formats: Feature Film, Music Video, Short Film, Experimental / Art Film, Drama Series Episode, AI-Generated Clip | genres: Psychological / Arthouse, Psychological Horror, Surreal / Absurdist, Horror, Drama, Thriller / Suspense, Supernatural Horror  
**Avoid when:** On a locked shot with a clean pull it reads as a mistake. Cut against other lenses and the mismatch shows.  
**Prompt:** `focus pull with visible lens breathing, frame subtly expanding as focus travels from the foreground to the far wall`  
`lens.focus_breathing`

### Out-of-Focus Opening

**Also called:** soft open, abstract open, unresolved first frame  
**What it is:** The shot begins entirely out of focus: colour and blocks of light with no shape, and resolves a moment later, often after a sound has already landed. It is the same opening as the camera-move card `move.focus_reveal`; where the resolve itself has to be written into a video prompt, that card carries it.  
**Effect on the audience:** It makes the viewer work to understand what they are seeing, so they lean in more than on a normal shot. It also feels like waking from sleep or unconsciousness.  
**Used for and where it works best:** The first shot after a time cut, the character waking in a hospital, or the opening of a music video. In vertical work, one blurred second under a strange sound resolving into the image works as a hook.  
**Best in:** formats: Feature Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Drama Series Episode, Short Film, Trailer / Teaser, AI-Generated Clip | genres: Drama, Thriller / Suspense, Psychological / Arthouse, Surreal / Absurdist, Medical Drama, Horror, Romance, Mystery / Whodunit  
**Avoid when:** Held past a couple of seconds with no sound pulling the ear, the audience assumes the video is broken. Do not repeat it at every scene head.  
**Prompt:** `shot opens completely out of focus, abstract blobs of colour and light, then resolves slowly into a sharp face`  
`lens.out_of_focus_opening`

### Focus Reveal

**Also called:** focus revelation, planted second plane  
**What it is:** You build the shot on two planes and keep the second piece of information hidden because it sits out of focus, then let sharpness move to it so something that was always there is revealed. The staging is the technique here, which separates it from the Focus Reveal in the camera moves, where a fully dissolved frame simply resolves onto the same subject with no second plane.  
**Effect on the audience:** A quiet shock. The viewer realises the danger was on screen the whole time and they did not notice it.  
**Used for and where it works best:** Horror and suspense: something soft in the background hardens into a standing figure that never moved. In investigation, a name on a page in the foreground resolves right after the line lands. In heritage work, the relief behind resolves and a detail completes the narration.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Heritage / Historical Documentary, Short Film, Music Video, Game Cinematic / Gameplay, AI-Generated Clip | genres: Horror, Thriller / Suspense, Mystery / Whodunit, Crime / Procedural, Supernatural Horror, Psychological Horror, Drama, Heritage (civilisation-focused)  
**Avoid when:** With nothing worth revealing the move is empty. Revealing something the audience already saw in the previous shot usually wastes it, because there is nothing left to discover; the exception is when the point is that they missed it the first time.  
**Prompt:** `two plane composition, foreground face sharp while a blurred figure stands far behind, focus then shifts to the figure`  
**Yields to:** `move.focus_reveal` — No planted second plane, just a frame resolving.  
`lens.focus_reveal`

### Defocus as Point of View

**Also called:** blurred POV, drunk vision, failing eyesight  
**What it is:** You let the image sit out of focus, or half focused, because the character themselves cannot see properly: drunk, dizzy, concussed, failing sight, crying.  
**Effect on the audience:** It moves the viewer inside the character's body instead of watching from outside. The fear comes from being unable to see rather than from the thing itself.  
**Used for and where it works best:** The drunk or drugged scene, waking after a blow, the character losing their sight, and the instant before tears fall. It is strongest when you pair it with muffled sound coming back up.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Music Video, Game Cinematic / Gameplay, Vertical Micro-Drama, AI-Generated Clip | genres: Drama, Psychological Horror, Thriller / Suspense, Horror, War, Medical Drama, Coming of Age, Tragedy  
**Avoid when:** Held too long it genuinely irritates the eye and the scene is lost. Without a reason inside the character it reads as a technical mistake.  
**Prompt:** `point of view shot drifting in and out of focus, doubled soft edges, unstable framing, muffled world`  
**Yields to:** `lens.soft_focus` — Dream softness with no in-character reason to be blind.  
`lens.defocus_pov`

### Lens Flare

**Also called:** flare, sun flare, artificial flare  
**What it is:** A strong light enters the lens off axis and bounces inside its elements, printing flare shapes: discs, columns, streaks or a general wash. You control it with the camera angle and the position of the source.  
**Effect on the audience:** It softly breaks the fourth wall: you sense there is a real camera, so the image feels alive and present in a real place.  
**Used for and where it works best:** Sunset, sun raking between columns or palms, the beat of coming out of a tunnel into light. In science fiction, flares deliberately fired from hard sources off frame create a bright hard world. In commercials it buys instant warmth.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Trailer / Teaser, Travel / Real Estate / Hospitality, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Sci-Fi, Action, Adventure, Romance, Heritage (civilisation-focused), Historical / Biopic, Western, Space Opera, Drama  
**Avoid when:** Flare on every shot becomes a dated fashion and it hides faces. On a grieving or serious beat it lightens a weight that should stay heavy.  
**Prompt:** `strong backlight just outside frame creating a warm lens flare across the shot, sun raking between the columns`  
**Example:** Star Trek (2009), the heavy on-set flares fired across the lens.  
**Yields to:** `lens.veiling_glare` — A grieving or heavy beat a bright flare would lift.  
`lens.flare`

### Veiling Glare

**Also called:** stray light wash, lifted blacks from flare, milking the image  
**What it is:** Stray light enters the lens and washes the whole image with a grey veil, lifting the blacks and dropping contrast without printing a recognisable flare shape.  
**Effect on the audience:** It makes the image feel dusty, aged and tired, and it takes the psychological edge off.  
**Used for and where it works best:** Heat, dust and desert scenes, the memory that is fading, the faked archive. Strong in heritage work when you want the image to feel older than clean cameras.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Music Video, Short Film, Docudrama / Reenactment, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: War, Historical / Biopic, Heritage (civilisation-focused), Survival, Western, Drama, Dystopia / Post-Apocalyptic, Tragedy  
**Avoid when:** It cannot be removed later, so overdo it and the image is gone for good. In a scene that needs shadow detail it destroys it.  
**Prompt:** `stray light veiling the frame, lifted milky blacks, low contrast dusty air, sun just off the edge of the lens`  
**Yields to:** `lens.halation` — The scene still needs its shadow detail.  
`lens.veiling_glare`

### Halation

**Also called:** red halation, film glow, highlight halo  
**What it is:** On film, a strong highlight passes through the emulsion and reflects off the base, printing a red orange halo around bright sources. It is emulated digitally in the grade or with a filter.  
**Effect on the audience:** It gives warmth and instant nostalgia. Light starts to feel hot and physical rather than numeric.  
**Used for and where it works best:** Neon night scenes, candle and fire in a period setting, and anything reaching for the nineteen seventies or eighties. Strong in heritage work, music video and anything you want to read as thirty five millimetre film.  
**Best in:** formats: Feature Film, Music Video, Drama Series Episode, Heritage / Historical Documentary, Title Sequence / Opening Credits, Commercial / TVC, Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Romance, Noir / Neo-Noir, Gothic / Vampire, Drama, Cyberpunk, Coming of Age  
**Avoid when:** In a clean modern or scientific context it feels added on and false. Pushed too far every light looks like it is on fire.  
**Prompt:** `film style halation, warm red glow bleeding around the bright practicals, soft highlight bloom, 35mm feel`  
**Yields to:** `lens.bloom` — A clean modern context where film red reads false.  
`lens.halation`

### Bloom

**Also called:** highlight bloom, glow, overexposure spill  
**What it is:** Overexposed highlights spill into what surrounds them, creating a soft white halo that eats the edges of shapes. It comes from the lens, from diffusion or from the grade.  
**Effect on the audience:** It gives softness, dream and a sense of holy light or fever.  
**Used for and where it works best:** Visions, dreams, apparitions and childhood memory, and the window pouring white light into a dark room. In music video and advertising it lays a beauty layer over the face.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Title Sequence / Opening Credits, Anime (Japanese 2D), 3D CG Animation, Short Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Faith / Biblical Epic, Fantasy / Epic, Romance, Fairy Tale, Psychological / Arthouse, Drama, Shojo (anime romance), Magical Girl (anime)  
**Avoid when:** In a realistic or investigative scene it destroys credibility. Overdone it eats faces and loses detail permanently.  
**Prompt:** `soft highlight bloom, white light spilling from the window and wrapping around the silhouette, dreamlike glow`  
**Yields to:** `lens.diffusion_filter` — A realistic scene that still wants a gentle halo.  
`lens.bloom`

### Chromatic Aberration

**Also called:** colour fringing, purple fringing, CA  
**What it is:** The lens fails to bring every colour to the same point, so a purple or green fringe appears along high contrast edges. Older and cheaper glass shows it more.  
**Effect on the audience:** It makes the image feel imperfect and human, and pushed further it reads as a technical fault or a broken world.  
**Used for and where it works best:** Imitating old video, cheap cameras and memory, plus cyberpunk and the glitching screen. Strong in vertical work when faking old footage, and in horror when the image itself should feel infected.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Experimental / Art Film, Game Cinematic / Gameplay, Title Sequence / Opening Credits, Meme / Comedy Edit, Short Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Cyberpunk, Horror, Psychological Horror, Surreal / Absurdist, Sci-Fi, Found Footage, Dystopia / Post-Apocalyptic, Coming of Age  
**Avoid when:** In clean professional work it is a defect that gets removed in post. Do not add it to a serious beat you want to feel expensive.  
**Prompt:** `visible chromatic aberration, purple and green fringing along the high contrast edges, slightly degraded lo-fi optics`  
**Yields to:** `lens.vintage_uncoated` — An old imperfect feel that must still look expensive.  
`lens.chromatic_aberration`

### Vignette

**Also called:** edge darkening, optical vignette, natural falloff  
**What it is:** The corners of the frame sit darker than the centre, either naturally from a lens shot wide open or added in the grade. The corners pull toward black.  
**Effect on the audience:** It fences the viewer's eye into the centre and gives a sense of watching, of remembering, or of being closed in.  
**Used for and where it works best:** The scope or hidden camera shot, the flashback, the portrait where you want the face to separate from the wall. In horror, the darkened corners invite the audience to search them.  
**Best in:** formats: Feature Film, Music Video, Drama Series Episode, Title Sequence / Opening Credits, Documentary Feature, Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Horror, Noir / Neo-Noir, Thriller / Suspense, Gothic / Vampire, Historical / Biopic, Psychological / Arthouse, Mystery / Whodunit, Drama  
**Avoid when:** Overdone it makes every shot look like a preset filter. In vertical framing it swallows a face that is not dead centre.  
**Prompt:** `natural lens vignette, corners falling into shadow, attention pulled to the centre of frame, slight edge softness`  
**Yields to:** `lens.shallow_dof` — Vertical framing with an off-centre face.  
`lens.vignette`

### Barrel and Pincushion Distortion

**Also called:** barrel distortion, pincushion distortion, geometric distortion  
**What it is:** A geometric lens error: barrel bows straight lines outward, common on wide lenses, while pincushion bends them inward, common at the long end of zooms.  
**Effect on the audience:** A little bowing makes a space feel unstable without the viewer knowing why. That is a quiet psychological weapon.  
**Used for and where it works best:** A room full of straight lines, tiles, shelves, a window frame, when you want the room to feel sick. In architecture and documentary work the opposite applies: correct it so the ziggurat and the wall stand straight.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Experimental / Art Film, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Corporate / Training, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Psychological Horror, Horror, Surreal / Absurdist, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Dystopia / Post-Apocalyptic  
**Avoid when:** On any architectural or product shot the distortion looks cheap and wrong. Do not mix corrected and uncorrected shots inside one scene.  
**Prompt:** `slight barrel distortion, tile lines and window frames bowing outward at the edges, unsettling geometry`  
**Yields to:** `lens.shift_perspective_control` — Architectural or product work needing straight geometry.  
`lens.barrel_pincushion`

### Ultra-Fast Glass

**Also called:** f/0.7, f/0.95, available light lens, candlelight lens  
**What it is:** A lens with an enormous aperture that allows shooting on candles or a single lamp with no added lighting. Depth of field becomes paper thin and edge sharpness falls apart.  
**Effect on the audience:** It delivers total historical honesty: the scene feels lit the way the people of that period actually lit their nights.  
**Used for and where it works best:** The period interior lit by candles, the monastery, the temple and the tent at night, any beat where darkness should stay dark. In heritage and period drama it is the difference between a scene lit by candlelight and a scene pretending to be.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Docudrama / Reenactment, Short Film, Drama Series Episode, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Faith / Biblical Epic, Gothic / Vampire, Drama, Tragedy, Mythology / Ancient Epic, War  
**Avoid when:** Focus is brutally hard and any movement costs you takes, so it is wrong for mobile performance. In daylight it means nothing at all.  
**Prompt:** `ultra fast lens shot wide open on candlelight only, paper thin focus on the eyes, warm falloff into total darkness`  
**Example:** Barry Lyndon (1975), the Zeiss f/0.7 candlelit interiors.  
`lens.fast_glass`

### Zoom versus Prime as a Look

**Also called:** zoom look, prime look, glass character  
**What it is:** A prime has one fixed focal length: cleaner, faster, higher in contrast. A zoom covers a range: a little slower, more prone to flare, lower in contrast, and its rendering shifts across the range. This record is about image character, not about the zoom move.  
**Effect on the audience:** A prime gives a deliberate, sculpted image; a zoom carries the feeling of live coverage, old television and reportage.  
**Used for and where it works best:** Choose primes for drama and designed images, choose zooms for live documentary, reportage and any scene that should feel stolen. In period work, the character of a nineteen seventies zoom dates the image on its own with no set dressing.  
**Best in:** formats: Documentary Feature, News Report / Reportage, Feature Film, Drama Series Episode, Sports Broadcast / Sports Film, Documentary Series, Vlog / YouTube Long-Form, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography | genres: Verite / Observational, True Crime, Historical / Biopic, Political Thriller, Drama, War, Sports Drama, Crime / Procedural  
**Avoid when:** Do not intercut clean prime images with old zoom images inside one scene unless the story asks for it. In low light the zoom loses.  
**Prompt:** `shot on a period zoom lens, slightly lower contrast and softer rendering, documentary coverage feeling, handheld`  
`lens.zoom_vs_prime`

### Perspective: Dolly versus Zoom

**Also called:** move the camera or zoom, perspective change versus magnification  
**What it is:** Moving the camera actually changes perspective: the relationship between foreground and background shifts. Zooming changes only magnification: the same perspective, larger. The compound dolly zoom move belongs with the signature moves.  
**Effect on the audience:** A camera move feels like the viewer walking into the space; a zoom feels like someone watching and magnifying. One takes you in, the other reminds you that you are outside.  
**Used for and where it works best:** Decide by meaning: for drama and emotional approach move the camera, for surveillance, espionage and live documentary zoom, because the zoom itself says somebody is watching. In anime and animation the same law applies between moving the layers and scaling the drawing.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, News Report / Reportage, Anime (Japanese 2D), 2D Animation (Western / Cartoon), Game Cinematic / Gameplay, AI-Generated Clip | genres: Drama, Thriller / Suspense, Spy / Espionage, Crime / Procedural, Verite / Observational, Mystery / Whodunit, Political Thriller, War  
**Avoid when:** Zooming because you cannot be bothered to move the camera looks lazy on screen. The reverse is also true: a camera move inside a surveillance beat breaks the idea of a distant watcher.  
**Prompt:** `static camera slowly zooming in on the doorway from far away, surveillance feeling, background scale unchanged`  
`lens.dolly_vs_zoom`

### Shift Lens / Perspective Control

**Also called:** PC lens, rise and fall, architectural shift  
**What it is:** A lens that moves parallel to the sensor, upward or sideways, without tilting the focal plane, so the top of a building enters the frame while the camera stays level and the verticals stay parallel. This is the shift function alone, and it is distinct from the tilt function used for miniature faking.  
**Effect on the audience:** The building stands upright instead of falling away backward. The viewer reads the architecture the way an architect reads it: correct proportions and a calm authority.  
**Used for and where it works best:** Facades, towers, ziggurats and churches in heritage documentary and property work, and copy work on paintings and reliefs with no geometric distortion. It also lets you shoot a mirror or a polished surface from a side position without the camera appearing in the reflection.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Travel / Real Estate / Hospitality, Corporate / Training, Poster / Static Design, Product Video / Motion Design, Video Essay, Explainer, Generated Keyframe Feeding Video, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography, Architectural Photography, Still Life Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Faith / Biblical Epic, Mythology / Ancient Epic, Drama, Nature / Wildlife  
**Avoid when:** It usually delivers an image that is geometrically correct and emotionally cool, because without converging lines the sense of looming scale disappears. The exception is when dignity is the goal, presenting a temple or a palace that should read as order rather than as threat.  
**Prompt:** `shift lens architectural shot, camera level at ground height, lens raised to include the full tower, vertical lines perfectly parallel, no keystone distortion`  
**Yields to:** `lens.ultra_wide` — Looming scale matters more than correct geometry.  
`lens.shift_perspective_control`

### Prisms and Distortion Optics

**Also called:** prism filter, crystal ball, kaleidoscope optics, lens texture tricks  
**What it is:** A piece of glass, crystal or metal held in front of the lens to bend, reflect or repeat part of the image. The effect changes as the piece is rotated and as it moves closer to the front element.  
**Effect on the audience:** It puts an unreal layer inside a real image. The viewer feels a mental fog or a psychological fracture without locating where the distortion comes from.  
**Used for and where it works best:** The breakdown, the drunk beat or the dream state in drama, the opening of a music video, and fashion work that wants a rich optical texture. In horror, repeating the face along the frame edge so the viewer senses a second presence. It is a cheap tool that lands in camera instead of in effects.  
**Best in:** formats: Music Video, Fashion Film, Experimental / Art Film, Trailer / Teaser, Title Sequence / Opening Credits, Commercial / TVC, Short Film, Music Visualizer, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Street Photography, Wildlife Photography | genres: Psychological / Arthouse, Surreal / Absurdist, Horror, Psychological Thriller, Romance, Musical, Gothic / Vampire, Magical Realism  
**Avoid when:** The refraction usually lands across the face and the performance the scene was built on disappears. The exception is when hiding the face is the point, a character losing their identity in front of us.  
**Prompt:** `prism held at the edge of the lens, the subject sharp in the centre with a refracted double of her face smeared along the left edge, slow rotation of the prism, warm practical light`  
**Yields to:** `lens.selective_focus_optic` — The performance on the face must survive the optical layer.  
`lens.prism`
