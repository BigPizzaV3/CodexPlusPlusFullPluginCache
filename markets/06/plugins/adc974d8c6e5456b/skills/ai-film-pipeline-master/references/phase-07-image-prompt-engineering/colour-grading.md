# Colour and Grading

58 cards. Also in the other stage: a shot has a frame too. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name the Job Before the Look

**Also called:** the colour selector, job before look, what is this palette arguing  
**What it is:** The card at the head of the `color.` shelf. It does not describe a grade. It asks the three questions the shelf's own pair graph asks over and over — **is this colour carrying information or is it the weather, where does the difference live, and do you control what is in front of the lens** — and hands back a named shortlist for each answer. The axes were read off the fifty `Yields to:` conditions the cards carry and the `Avoid when:` boundaries underneath them; the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so the grade that does reach the screen was chosen against the story, the cut and the production, rather than reached for because it is what a film looks like.  
**Used for and where it works best:** Answer the three questions **in order and out loud, in one sentence each, before you open the shelf**. Question one is not about the picture, it is about the script: does anything in the story stop working if the audience cannot name the colour? **If the answer to question one is *a job*, you are not choosing from this shelf yet — you are subject to `access.not_colour_alone` first**, and the test it sets is the one to run here: *if this frame were greyscale, would it still say the same thing?* If not, the colour needs a second channel — lightness, shape, position or a label — and the card you eventually pick from this shelf has to survive that addition. Roughly a sixth of this shelf is not a choice at all: `color.primary_grade`, `color.continuity`, `color.secondary`, `color.skin_protection`, `color.split_toning`, `color.lut`, `color.film_emulation`, `color.hdr` and `color.color_script` are a **chain that runs over whatever the three questions returned**, in that order, and they are listed once under every value rather than forked, because a palette, a contrast move and a skin-tone protection all belong in one grade.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The palette is not yours to choose** — a locked brand system, a series already on air, a plate you are matching, or a second season that has to cut against the first. There the colour is measured off the reference rather than picked from a shelf, and `color.continuity` says so in its own terms: the right decision comes from comparison with the neighbouring shots, not from grading a clip alone on its own screen. Also **distrust axis three on generated material**, which is most of the work this package is written for: there you control neither the set nor a real grade, you control a prompt, so the honest answer to *do you control what is in front of the lens* is *neither*, the axis stops sorting, and the map is down to two questions. And **distrust axis one whenever your honest answer is *a job***: that answer routes out of this shelf before it routes into it, and a real share of the time the finding is that the meaning should not have been carried by hue at all — in which case this shelf has nothing to sell you and a label, a shape or a position is the answer.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Is this colour carrying information, or is it the weather?**
Asked first, because it is the fork the neighbouring shelf states outright: `access.not_colour_alone` yields to `color.warm_cold` *and the grading cards generally, wherever colour is atmosphere rather than information*, and says of itself that it governs colour that has a job. The shelf then repeats the same boundary in its own words — *"The whole frame is red, so it is mood and not signal"* (`color.red`), *"Colour carries information: a uniform, a flag, blood"* (`look.black_white`, pointing in), *"if the colour does not mean something in the story it reads as an empty visual trick"* (`color.accent`), *"Applied to an element with no meaning it feels cheap immediately"* (`color.selective`), *"if the whole piece is green the purpose is lost because there is no second world to compare it with"* (`color.matrix_green`), *"if the whole piece is dreams the look stops functioning as a signal"* (`color.dream_tint`), *"If the difference is subtle it does not register"* (`color.traffic_yellow_blue`), *"If the assigned colours sit close together they do not read"* (`color.character_coding`).

**Axis 2 — Where does the difference live: inside one frame, across a cut, or nowhere?**
The largest cluster of conditions on the shelf, and every one of them is a fact about the edit rather than a feeling: *"if no scene carries the opposite temperature, the contrast disappears and the decision means nothing"* (`color.temperature`), *"With no opposing accent the frame goes flat in colour"* (`color.analogous`), *"with no warmth against it, it reads as ordinary night rather than as isolation"* (`color.blue_isolation`), *"If the subject's colour sits close to the background no amount of lighting will rescue it"* (`color.contrast_separation`), *"if the hue sits close to skin tone the faces dissolve"* (`color.monochromatic`), *"if the sand tone covers everything the characters dissolve inside the colour"* (`color.villeneuve_sand_blue`), *"without rain, haze or reflective surfaces the neon does not spread"* (`color.cyberpunk_night`), *"Break the rule in a single scene and you confuse the viewer more than if you had no rule at all"* (`color.day_night_tint`). A colour with nothing to be different from is not a decision.

**Axis 3 — Do you control what is in front of the lens, or were you handed the footage?**
Asked last, and it is the axis the shelf argues with itself about most explicitly: `color.accent` and `color.selective` are the same idea and yield to each other on nothing but this — *"No control of costume or set, archive material"* one way, *"The accent can be built in camera instead of post"* the other. It repeats: *"Documentary footage you cannot art-direct; unify in the grade"* (`color.limited_palette`), *"Imitating it without the same discipline in set and costume"* (`color.wes_pastel`), *"it has to be planned before the shoot, because set and costume are part of the arc and not just the grade"* (`color.arc`), *"decide it before you shoot"* (`color.sickly_green`), *"Removing blue makes any sky or water scene look wrong, so plan the shots around it"* (`color.amelie_red_green`), *"It needs large compositions and empty space"* (`color.villeneuve_sand_blue`).

---

**The map**

**Axis 1 — information, or the weather**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A job — a hue stands for a person, a world, a time or a state, and the audience is expected to decode it.** `access.not_colour_alone` applies before anything here is chosen | `color.accent` · `color.selective` · `color.contrast_separation` · `color.character_coding` · `color.red` · `color.blue_isolation` · `color.yellow_madness` · `color.sickly_green` · `color.purple_otherworld` · `color.matrix_green` · `color.traffic_yellow_blue` · `color.day_night_tint` · `color.flashback_tint` · `color.dream_tint` · `color.arc` · `color.drain` · `color.return` |
| **The weather — nothing in the story stops working if the viewer cannot name the colour** | `color.temperature` · `color.warm_cold` · `color.mixed_temp` · `color.complementary` · `color.analogous` · `color.triadic` · `color.monochromatic` · `color.limited_palette` · `color.desaturation` · `color.saturation_high` · `color.duotone` · `color.crushed_blacks` · `color.teal_orange` · `color.technicolor` · `color.kodachrome` · `color.vintage_faded` · `color.cross_process` · `color.bleach_bypass` · `color.amelie_red_green` · `color.wes_pastel` · `color.steel_blue_winter` · `color.fincher_green` · `color.villeneuve_sand_blue` · `color.refn_neon` · `color.cyberpunk_night` · `color.golden_heritage` · `color.clinical_white` · `color.pastel_preschool` · `color.doc_desaturated` · `color.trailer_contrast` |
| **Neither — it is the chain, and it runs under both answers above in this order** | `color.primary_grade` · `color.continuity` · `color.secondary` · `color.skin_protection` · `color.split_toning` · `color.lut` · `color.film_emulation` · `color.hdr` · `color.color_script` |

**Axis 2 — where the difference lives**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Inside one frame — two colour masses in the same image, sorted by the eye in a single glance** | `color.warm_cold` · `color.complementary` · `color.triadic` · `color.teal_orange` · `color.mixed_temp` · `color.contrast_separation` · `color.accent` · `color.selective` · `color.split_toning` · `color.skin_protection` · `color.secondary` · `color.red` · `color.blue_isolation` · `color.amelie_red_green` · `color.villeneuve_sand_blue` · `color.refn_neon` · `color.cyberpunk_night` |
| **Across a cut — the difference exists only by comparison with another shot, strand, era or chapter** | `color.temperature` · `color.matrix_green` · `color.traffic_yellow_blue` · `color.flashback_tint` · `color.dream_tint` · `color.day_night_tint` · `color.character_coding` · `color.arc` · `color.drain` · `color.return` · `color.color_script` · `color.continuity` |
| **Nowhere — one condition holds the whole piece, and the only comparison left is the audience's memory of ordinary colour** | `color.analogous` · `color.monochromatic` · `color.limited_palette` · `color.desaturation` · `color.saturation_high` · `color.duotone` · `color.crushed_blacks` · `color.technicolor` · `color.kodachrome` · `color.film_emulation` · `color.lut` · `color.hdr` · `color.vintage_faded` · `color.cross_process` · `color.bleach_bypass` · `color.wes_pastel` · `color.steel_blue_winter` · `color.fincher_green` · `color.golden_heritage` · `color.clinical_white` · `color.pastel_preschool` · `color.doc_desaturated` · `color.trailer_contrast` · `color.yellow_madness` · `color.sickly_green` · `color.purple_otherworld` · `color.primary_grade` |

**Axis 3 — who controls the colour**

| Answer | The shortlist, by id |
| :--- | :--- |
| **You do — set, costume and location are yours, and the decision is made before the camera turns over** | `color.limited_palette` · `color.accent` · `color.contrast_separation` · `color.character_coding` · `color.wes_pastel` · `color.amelie_red_green` · `color.villeneuve_sand_blue` · `color.cyberpunk_night` · `color.refn_neon` · `color.pastel_preschool` · `color.technicolor` · `color.red` · `color.mixed_temp` · `color.warm_cold` · `color.complementary` · `color.triadic` · `color.analogous` · `color.arc` · `color.color_script` · `color.sickly_green` |
| **Either way — it can be built in front of the lens or applied afterwards, and the choice is a budget, not a look** | `color.temperature` · `color.monochromatic` · `color.desaturation` · `color.saturation_high` · `color.split_toning` · `color.crushed_blacks` · `color.golden_heritage` · `color.steel_blue_winter` · `color.fincher_green` · `color.matrix_green` · `color.blue_isolation` · `color.yellow_madness` · `color.purple_otherworld` · `color.day_night_tint` · `color.dream_tint` · `color.drain` · `color.return` · `color.clinical_white` · `color.skin_protection` · `color.secondary` · `color.primary_grade` · `color.continuity` |
| **You do not — archive, an interview you did not light, a generation that came back how it came back** | `color.selective` · `color.lut` · `color.doc_desaturated` · `color.film_emulation` · `color.hdr` · `color.vintage_faded` · `color.cross_process` · `color.bleach_bypass` · `color.kodachrome` · `color.teal_orange` · `color.duotone` · `color.traffic_yellow_blue` · `color.flashback_tint` · `color.trailer_contrast` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and it is normally two to five cards wide — narrower than the lighting shelf's, because the chain is named once instead of competing.*

---

**The default, and the one against it**

**The default is `color.warm_cold` in the frame, with the chain under it, and it is measured rather than asserted.** Three cards from three different conditions fall back to it — `color.temperature` (*"No opposing scene; put the contrast inside one frame"*), `color.blue_isolation` (*"Ordinary night unless a warm source opposes it"*), and `access.not_colour_alone` itself, which hands colour back to this shelf at exactly this card whenever the colour turns out to be atmosphere and not information. It is the only palette answer here that needs no era, no second strand, no named film and no art department: one warm source and one cool one, which most real locations already contain. **On the other side of axis one the default is `color.accent`**, and that is the stronger measurement of the two — four inbound conditions, more than any card on the shelf, and they are four genuinely different reasons: a flat frame with no point of focus (`color.analogous`), too many separated elements shouting at once (`color.contrast_separation`), an accent that can be built in camera rather than in post (`color.selective`), and a frame where the colour carries information (`look.black_white`, pointing in from off the shelf). Asked four times from four directions, the shelf answers *quiet everything and let one thing carry it*.

**And the most-yielded-to card on this shelf is neither of them, which is the point.** `color.doc_desaturated` takes five inbound edges, more than any other card here, and **all five fire on one condition** — the material claims to be true: *"Honest documentary, where built contrast exposes the lighting"*, *"Serious drama and documentary, where it reads childish"*, *"Serious drama and documentary, where vividness breaks belief"*, *"Documentary and archive, where lost detail is lost information"*, *"True crime that must read as testimony, not as style"*. Five edges, one reason. **It is a genre escape hatch, not a fallback**, and a selector that read in-degree without reading the conditions behind it would have made a documentary grade the default answer for a shelf that is mostly fiction.

**The one against it is `color.limited_palette`.** Nothing on the shelf routes to it. Every other card here is a treatment applied to a frame; this one says the treatment is the wrong unit — you fix a small set of permitted colours across set, costume and location, and no colour outside that set ever enters the image, so the frame arrives already graded and most of this shelf becomes unnecessary. Its cost is stated and it is a production cost rather than an aesthetic one: *if wardrobe does not hold the line one shot destroys it*, and on material you did not shoot it cannot be enforced at all, which is why it yields to `color.lut`. That is the trade the grade-first default hides: a look bought in post is reversible and weak, a palette bought on set is irreversible and total. Its cousin against the grain is `color.return`, the only card here whose entire power is an absence somebody paid for earlier — it does nothing unless `color.drain` ran long before it, so it is the one card on this shelf that cannot be decided in the frame it appears in.

---

**The unasked**

**Twenty-one of the fifty-six are the target of no `Yields to:` field anywhere in the package.** They can be chosen but nothing ever sends you to them. By id:

`color.amelie_red_green` · `color.arc` · `color.character_coding` · `color.complementary` · `color.continuity` · `color.cross_process` · `color.drain` · `color.duotone` · `color.hdr` · `color.limited_palette` · `color.matrix_green` · `color.purple_otherworld` · `color.red` · `color.return` · `color.sickly_green` · `color.split_toning` · `color.steel_blue_winter` · `color.teal_orange` · `color.technicolor` · `color.trailer_contrast` · `color.yellow_madness`

**The shape of that list is the finding, and it has two halves.**

**First: nothing that governs colour across time is reached from inside this shelf.** `color.arc`, `color.drain`, `color.return`, `color.character_coding`, `color.limited_palette` and `color.continuity` take no inbound edge at all, and `color.color_script` takes two — **both from other shelves**, from the data-visualisation card that governs encoding and from the identity card that locks a palette. Every card that decides what the colour does across a runtime is either unreached or reached from outside. The pair graph on this shelf is a graph of **states**: each reader was holding one frame and comparing it with another frame, so a palette that *changes* never registers as an alternative to a palette that *holds*. That is why axis two carries an *across a cut* value at all, and why it is asked second rather than not at all.

**Second, and it is the more useful one: this shelf can talk you out of a hue but never into one.** `color.red`, `color.yellow_madness`, `color.sickly_green` and `color.purple_otherworld` all yield outward and take nothing inward; of the whole single-hue-means-something block only `color.blue_isolation` is ever a destination, and only for an in-frame contrast rather than for its meaning. So the meaning cards are exits. **The card this shelf wants is the one that asks what the hue means to the audience actually watching** — because the meanings here are stated as universal and they are not. Red is given as danger and desire, white as clinical and neutral, green as sickness, and those readings are local: white is the colour of mourning across much of Asia, green is the colour of paradise in Islamic material, and the shelf carries heritage instructions inside `color.golden_heritage`, `color.limited_palette`, `color.traffic_yellow_blue`, `color.flashback_tint` and `color.skin_protection` that are written for exactly the audience those readings would fail on. Nothing on the shelf records it, nothing routes to it, and it is the same failure `access.not_colour_alone` names from the other direction: **a meaning the audience does not share is a meaning carried by hue alone.**

The third thing the list shows is smaller and worth one line: the borrowed-signature block is almost entirely unasked — `color.teal_orange`, `color.technicolor`, `color.cross_process`, `color.duotone`, `color.amelie_red_green`, `color.steel_blue_winter`, `color.matrix_green`, `color.trailer_contrast`. The shelf warns you off other people's looks in eight separate `Avoid when:` lines and never once routes you into one.

`color.job_before_the_look`

---

### Colour Temperature as Mood

**Also called:** white balance as a choice, warm or cool balance  
**What it is:** Choosing the white balance not to correct colour but to tilt the whole scene warm or cool. The same shot leaning warm feels like a home and leaning cool feels like a hospital.  
**Effect on the audience:** The viewer reads temperature as a bodily state: warm means safety, life and human presence; cool means isolation, threat and absence.  
**Used for and where it works best:** Decide the temperature for each scene before you shoot and map it across the script: home scenes warm, work scenes cool. In series and drama it is the cheapest tool that gives an episode visual unity at no extra cost.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Commercial / TVC, Music Video, Documentary Feature, Soap Opera / Telenovela, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Romance, Thriller / Suspense, Crime / Procedural, Family, Sci-Fi, Melodrama, Psychological / Arthouse, Historical / Biopic  
**Avoid when:** A very strong tilt in either direction destroys skin tone and leaves faces looking sick or scorched. And if no scene carries the opposite temperature, the contrast disappears and the decision means nothing.  
**Prompt:** `warm colour temperature throughout, amber tungsten balance, skin tones golden against a cool exterior`  
**Yields to:** `color.warm_cold` — No opposing scene; put the contrast inside one frame.  
`color.temperature`

### Warm and Cold Contrast

**Also called:** warm cool contrast, temperature contrast  
**What it is:** Both temperatures present in the same frame at the same time: one warm side and one cool side, or a warm foreground against a cool background. It differs from scene temperature in that the contrast lives inside a single image.  
**Effect on the audience:** Instant depth and separation between a character and their world. The eye sorts the layers easily and the meaning reads as a conflict between two places or two states.  
**Used for and where it works best:** A character inside a warm house with a blue night outside, or inside a cold office with a golden window. It is the cleanest way to make an interior look cinematic, and in commercials and music video it delivers colour richness from a simple setup.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Music Video, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Soap Opera / Telenovela, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Romance, Thriller / Suspense, Crime / Procedural, Coming of Age, Sci-Fi, Noir / Neo-Noir, Melodrama  
**Avoid when:** If the contrast lands on the face itself, half of it goes orange and half blue and the look becomes excessive. In honest documentary a manufactured contrast exposes the fact that you lit the room.  
**Prompt:** `warm interior lamp light in the foreground against cold blue night through the window behind`  
**Yields to:** `color.doc_desaturated` — Honest documentary, where built contrast exposes the lighting.  
`color.warm_cold`

### Mixed Colour Temperature

**Also called:** mixed white balance, competing sources  
**What it is:** Sources at different temperatures working in one space: warm tungsten inside, cool daylight through the window, green fluorescent from the corridor. You balance for one and let the others drift on purpose.  
**Effect on the audience:** Rich realism. The space feels genuine because real spaces actually are like this, and the competing colours build layers without effort.  
**Used for and where it works best:** The evening interior, the hospital at night, the kitchen with a window, the office. Balance for the face and let everything else drift, because the one thing that has to stay right is skin tone.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Vertical Micro-Drama, Short Film, Soap Opera / Telenovela, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Drama, Crime / Procedural, Medical Drama, Thriller / Suspense, Slice of Life, Coming of Age, Verite / Observational, Romance  
**Avoid when:** Three or more temperatures with no plan and the image becomes coloured noise. In clean commercial work it is better to unify temperature so the product keeps its true colour.  
**Colour temperature:** tungsten, daylight and fluorescent all at once — take all three rows from `light.kelvin_reference`; the gap between them is what this card is about  
**Prompt:** `mixed colour temperature, warm tungsten lamps inside and cold daylight through the window, green corridor light spilling in`  
**Yields to:** `color.clinical_white` — Clean commercial work where product colour must stay true.  
`color.mixed_temp`

### Complementary Colour Scheme

**Also called:** opposite colours, complementary harmony  
**What it is:** Building the image on two opposing colours from the wheel: blue and orange, red and green, purple and yellow. Each one strengthens the other and makes it read more intensely.  
**Effect on the audience:** Energy, tension and clean separation. The eye finds the subject instantly because its colour differs from everything around it.  
**Used for and where it works best:** Any shot where the subject or the product has to cut out of the background: a hero in a red shirt inside a green space, or a warm product on a cool backdrop. In advertising, posters and trailers it is the default system because it works at the smallest display size.  
**Best in:** formats: Commercial / TVC, Trailer / Teaser, Product Video / Motion Design, Music Video, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Title Sequence / Opening Credits, 3D CG Animation, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Action, Adventure, Sci-Fi, Superhero, Fantasy / Epic, Thriller / Suspense, Musical, Comedy  
**Avoid when:** With both colours at the same strength and area the frame fights itself and tires the eye, so let one dominate and keep the other as an accent. Applied mechanically it gives an image that looks more like a poster than a film.  
**Prompt:** `complementary colour scheme, warm orange subject against a deep blue environment, clean colour separation`  
**Yields to:** `color.analogous` — Opposition tires the eye and harmony is wanted.  
`color.complementary`

### Teal and Orange

**Also called:** orange and teal, blockbuster grade  
**What it is:** A specific version of complementary colour: skin is pushed toward orange while shadows and background are pushed toward teal, achieved in the grade rather than in the design. It became the default look of commercial Hollywood cinema.  
**Effect on the audience:** Faces separate automatically from any background and look healthy and warm. The image feels expensive and polished even when the location is plain.  
**Used for and where it works best:** Trailers, action, commercials and any content that plays across many different screens, because it keeps the image readable everywhere. It is useful in vertical short-form where the face has to separate quickly from any street background.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Game Cinematic / Gameplay, Product Video / Motion Design, Sports Broadcast / Sports Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Action, Thriller / Suspense, Adventure, Superhero, Sci-Fi, Spy / Espionage, Heist, Disaster  
**Avoid when:** It is the most exhausted look in modern cinema, so in any work that wants its own identity it is the first thing to avoid. It also makes every location look the same, which erases the specific character of a historical or local place.  
**Prompt:** `teal and orange grade, warm skin tones against cyan leaning shadows and background`  
**Yields to:** `color.golden_heritage` — Historical or local place whose character it erases.  
`color.teal_orange`

### Analogous Colour Scheme

**Also called:** analogous harmony, neighbouring colours  
**What it is:** Building the image from neighbouring colours on the wheel: yellow, orange and red, or blue, cyan and green. There is no opposition; every colour belongs to the same family.  
**Effect on the audience:** Harmony, calm and immersion. The viewer feels no colour conflict, so the scene passes as one continuous state.  
**Used for and where it works best:** The dream sequence, the desert, the sea, the forest, and any place you want to feel like a closed world. In heritage work the yellow, orange and brown family gives earth, mud brick and stone with no intruding colour, which suits a Mesopotamian scene held on earth, brick and stone; where sky or river is in frame their blue belongs to the place, and `color.golden_heritage` (blue held in the sky only) or, on a large establishing wide, `color.villeneuve_sand_blue` is the card.  
**Best in:** formats: Heritage / Historical Documentary, Feature Film, Music Video, Travel / Real Estate / Hospitality, Commercial / TVC, 3D CG Animation, Anime (Japanese 2D), Documentary Feature, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Romance, Nature / Wildlife, Fantasy / Epic, Drama, Surreal / Absurdist  
**Avoid when:** With no opposing accent the frame goes flat in colour and the eye finds no point of focus. And if the skin falls inside the same family the character disappears into the background.  
**Prompt:** `analogous palette of amber, ochre and deep brown, no opposing colours in frame, unified earth tones`  
**Yields to:** `color.accent` — Flat frame with no opposing point of focus.  
`color.analogous`

### Triadic Colour Scheme

**Also called:** triad palette, three point harmony  
**What it is:** Three colours spaced evenly around the wheel: red, yellow and blue, or orange, green and purple. One dominates and the other two act as accents.  
**Effect on the audience:** Liveliness and variety without chaos. The image feels designed and playful and the eye moves comfortably between three points.  
**Used for and where it works best:** Kids content, animation, cheerful advertising and motion design. In kids content it is the best way to let every character be known by their colour without the screen turning noisy.  
**Best in:** formats: Kids Content, 2D Animation (Western / Cartoon), 3D CG Animation, Commercial / TVC, Explainer, Product Video / Motion Design, Title Sequence / Opening Credits, Vertical Short-Form (Reels, Shorts, TikTok), Stop Motion, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Preschool / Early Learning, Family, Comedy, Fairy Tale, Musical, Adventure, Fantasy / Epic, Magical Girl (anime)  
**Avoid when:** With all three at equal area and strength the frame looks like a paint box with no hierarchy. In serious drama and documentary it reads as childish.  
**Prompt:** `triadic palette, dominant warm yellow with red and blue accents, clean designed colour blocks`  
**Yields to:** `color.doc_desaturated` — Serious drama and documentary, where it reads childish.  
`color.triadic`

### Monochromatic Colour Scheme

**Also called:** single hue palette, tonal palette  
**What it is:** The whole frame built on one hue with variation only in brightness and saturation: a scene entirely in shades of blue, or entirely in shades of red. It is not black and white; it is one hue at different depths.  
**Effect on the audience:** Total immersion in one state. The viewer has no second colour to rest on, so they stay fully inside the mood.  
**Used for and where it works best:** The dream, the hallucination or the memory, and the fight or dance sequence in a music video. Use it as one chapter inside the piece rather than as a whole style: a single monochrome scene among colour scenes becomes an unforgettable marker.  
**Best in:** formats: Music Video, Feature Film, Short Film, Title Sequence / Opening Credits, Experimental / Art Film, Anime (Japanese 2D), Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Psychological / Arthouse, Surreal / Absurdist, Horror, Thriller / Suspense, Musical, Fantasy / Epic, Tragedy, Romance  
**Avoid when:** A long scene in one hue tires the eye and loses its effect after a minute. And if the hue sits close to skin tone the faces dissolve and the characters vanish.  
**Prompt:** `monochromatic red palette, everything in shades of the same hue, variation only in brightness and saturation`  
**Yields to:** `look.black_white` — The piece wants no hue at all, only tone.  
`color.monochromatic`

### Limited Palette

**Also called:** restricted palette, controlled colour design  
**What it is:** A production decision that fixes a small set of permitted colours across set, costume and location, so no colour outside that set enters the frame. The decision is made before the shoot, not in the grade.  
**Effect on the audience:** The piece feels designed and identifiable. More importantly, any colour entering from outside the palette becomes a major visual event without you doing anything else to it.  
**Used for and where it works best:** A film that needs a strong visual identity, animation, and brand advertising. In heritage work fix the palette to mud, bronze, natural wool and indigo, and any modern synthetic colour entering the frame exposes the period at once.  
**Best in:** formats: Feature Film, 2D Animation (Western / Cartoon), 3D CG Animation, Commercial / TVC, Heritage / Historical Documentary, Music Video, Title Sequence / Opening Credits, Stop Motion, Short Film, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Drama, Sci-Fi, Fairy Tale, Mythology / Ancient Epic, Dystopia / Post-Apocalyptic  
**Avoid when:** It needs discipline from every department, so if wardrobe does not hold the line one shot destroys it. And in genuine documentary footage you cannot enforce it, so do not plan around it there.  
**Prompt:** `restricted palette of mud brown, bronze and indigo only, no other colours anywhere in the frame`  
**Yields to:** `color.lut` — Documentary footage you cannot art-direct; unify in the grade.  
`color.limited_palette`

### Monochrome with One Accent Hue

**Also called:** accent colour, pop of colour  
**What it is:** The image is drained or held in one quiet hue while a single element keeps a saturated colour: a red door, a blue shawl, a green light. The entire frame exists to serve that one element.  
**Effect on the audience:** Absolute control of the eye. You cannot look at anything else, so whatever meaning you attach to that colour arrives directly with no explanation.  
**Used for and where it works best:** Tracking a person or an object inside a crowd, and marking danger or hope in a single shot. In advertising it makes the product cut out of any background, and in vertical short-form it works as a hook because it stops the thumb on the first frame.  
**Best in:** formats: Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Feature Film, Music Video, Trailer / Teaser, Product Video / Motion Design, Short Film, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Thriller / Suspense, Crime / Procedural, Romance, Fantasy / Epic, Tragedy, Mystery / Whodunit, War  
**Avoid when:** Use it on more than one element and the idea collapses into confusion. And if the colour does not mean something in the story it reads as an empty visual trick. And the element the frame singles out is colour doing a job, so the hue must not be the only thing that singles it out: set it apart by lightness and position as well, as `access.not_colour_alone` requires wherever colour carries meaning.  
**Prompt:** `desaturated frame with one saturated red element, everything else neutral grey, the red element also set apart from the grey by its lightness and its place in the frame, drawing the eye immediately`  
**Yields to:** `color.selective` — No control of costume or set, archive material.  
`color.accent`

### Selective Colour

**Also called:** spot colour, colour isolation  
**What it is:** Isolating one colour in the grade and stripping colour from everything else inside the same shot, so the red stays red and the rest goes grey. It is a grading operation rather than a shooting decision.  
**Effect on the audience:** The isolated colour becomes an explicit symbol. The viewer knows the director is telling them something on purpose, and the element stays in memory long after the film.  
**Used for and where it works best:** The single element carrying the whole meaning of the film, and its presence and absence across the story. It differs from an in-camera accent in being achieved in post, so it can work even on existing archive footage with no design of costume or set.  
**Best in:** formats: Feature Film, Documentary Feature, Music Video, Commercial / TVC, Title Sequence / Opening Credits, Short Film, Trailer / Teaser, Video Essay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Tragedy, War, Historical / Biopic, Thriller / Suspense, Melodrama, Mystery / Whodunit, Faith / Biblical Epic  
**Avoid when:** It has become one of the most worn tricks in wedding and social video, so it holds its power when kept to one or two moments in a whole piece; the exception is a work built on the colour returning as a motif, where the repetition itself is the structure. Applied to an element with no meaning it feels cheap immediately. And an element that carries the whole meaning is colour doing a job, so it must not rest on hue alone: in greyscale the kept colour is one more grey, so set it apart by its place in the frame or its lightness as well, as `access.not_colour_alone` requires wherever colour carries meaning.  
**Prompt:** `black and white frame with one element kept in full red, all other colour removed, the element also set apart by its place in the frame and its lightness`  
**Example:** Schindler's List (1993), the girl in the red coat inside a black and white sequence.  
**Yields to:** `color.accent` — The accent can be built in camera instead of post.  
`color.selective`

### Split Toning

**Also called:** split tone, warm highlights cool shadows  
**What it is:** You add one colour to the highlights and a different one to the shadows: warm highlights with cool shadows, or the reverse. The colour is applied by brightness level rather than across the whole image.  
**Effect on the audience:** The image gains depth without losing skin tone. It feels cinematic and polished because the tone changes inside a single surface.  
**Used for and where it works best:** It is the basis of nearly every modern cinematic look: blue leaning shadows with yellow leaning highlights read as film immediately. It is very useful on AI generated material because it unifies clips that came from different generations.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, Documentary Feature, AI-Generated Clip, Product Video / Motion Design, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Thriller / Suspense, Romance, Action, Crime / Procedural, Sci-Fi, Noir / Neo-Noir, Historical / Biopic  
**Avoid when:** Push the shadow tint too far and the black becomes coloured and you lose your reference point. On darker skin, blue shadows turn unnatural very quickly.  
**Prompt:** `split toned grade, cool blue shadows and warm yellow highlights, neutral skin tones held in the middle`  
`color.split_toning`

### Desaturation

**Also called:** muted palette, low saturation grade  
**What it is:** Lowering colour saturation across the whole image or in selected ranges, so the colours remain but sit low, quiet and close to grey.  
**Effect on the audience:** Harshness, realism and despair. The brain links low colour with low life, so the world looks worn out and tired.  
**Used for and where it works best:** War, survival, dystopia and hard crime, and the scenes that follow a loss. In serious documentary a light desaturation gives gravity, and in drama apply it to the present against a saturated past so the difference reads without a word.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Limited Series, Short Film, News Report / Reportage, Game Cinematic / Gameplay, Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: War, Survival, Dystopia / Post-Apocalyptic, Crime / Procedural, Tragedy, True Crime, Thriller / Suspense, Drama, Zombie  
**Avoid when:** Full desaturation leaves a dead image that loses even its realism, so keep some colour in the skin. And it has become so overused in war films that it now reads as a preset.  
**Prompt:** `desaturated grade, muted low saturation colours, grey leaning world with only faint colour left in the skin`  
**Yields to:** `color.bleach_bypass` — War material where flat desaturation now reads as a preset.  
`color.desaturation`

### High Saturation

**Also called:** hyper saturated, vivid palette  
**What it is:** Pushing saturation above natural levels so colours read purer and stronger than reality. It is usually achieved first through design and costume and only then in the grade.  
**Effect on the audience:** Joy, energy and imagination. The world looks better than the real one, so the viewer accepts it as a story world rather than a real one.  
**Used for and where it works best:** Musicals, kids content, animation, advertising and fantasy. In heritage work saturation is useful for festivals, markets and dyed textiles, because it corrects the mistaken idea that the past had no colour.  
**Best in:** formats: Kids Content, 2D Animation (Western / Cartoon), 3D CG Animation, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Product Video / Motion Design, Stop Motion, Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Musical, Preschool / Early Learning, Family, Fairy Tale, Fantasy / Epic, Comedy, Rom-Com, Magical Girl (anime), Adventure  
**Avoid when:** Too much saturation on skin turns it orange or red and it looks scorched. In serious drama and documentary it breaks belief and makes the subject look lighter than it is.  
**Prompt:** `highly saturated vivid colours, pure strong hues in the costumes and the set, bright joyful palette`  
**Yields to:** `color.doc_desaturated` — Serious drama and documentary, where vividness breaks belief.  
`color.saturation_high`

### Duotone

**Also called:** two tone, bi-colour treatment  
**What it is:** Converting the image to a gradient between two colours only: shadows in one hue and highlights in another, with the rest of the spectrum gone. It is like monochrome except the greys are replaced by two chosen colours.  
**Effect on the audience:** Style, graphic quality and a strong identity. The image looks printed and designed, so it reads as a poster or a brand rather than as reality.  
**Used for and where it works best:** Title sequences, motion design, advertising, posters and music video, and any sequence you want to sit outside the narrative. As a divider inside a documentary it gives a clean chapter or theme marker.  
**Best in:** formats: Title Sequence / Opening Credits, Product Video / Motion Design, Commercial / TVC, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Video Essay, Explainer, Trailer / Teaser, Experimental / Art Film, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Musical, Sci-Fi, Cyberpunk, Comedy, Thriller / Suspense, Action, Surreal / Absurdist, Science / Educational  
**Avoid when:** On real faces in a dramatic scene it strips all empathy and turns the face into a shape. In serious documentary it contradicts the claim that the footage is real.  
**Prompt:** `duotone treatment, shadows in deep navy and highlights in hot orange, no other colours in the image`  
**Yields to:** `look.black_white` — Real faces in drama, where two tones strip empathy.  
`color.duotone`

### Colour Separation

**Also called:** subject background colour separation, colour contrast for focus  
**What it is:** Choosing the colour of the subject or the product so it differs from everything around it, which separates it for the eye with no need for shallow focus or special lighting.  
**Effect on the audience:** The eye knows immediately where to go. Colour separation works even on small screens and even in deep focus, unlike shallow depth of field.  
**Used for and where it works best:** Any crowded or wide shot: the hero wearing a colour nobody else in the crowd is wearing. In vertical short-form it is one of the fastest subject-legibility tools, because the screen is small and the viewer has little time to find the subject. It answers where the eye goes inside a frame; the overall promotional grade is `color.trailer_contrast`.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Feature Film, Sports Broadcast / Sports Film, Trailer / Teaser, Product Video / Motion Design, Kids Content, Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Action, Adventure, Thriller / Suspense, Drama, Comedy, Sports Drama, Family, War  
**Avoid when:** If the subject's colour sits close to the background no amount of lighting will rescue it. And if you separate too many elements at once, everything in the frame shouts and nothing is heard. And separating the subject is colour doing a job, so hue must not be the only difference: make the subject lighter or darker than what surrounds it as well, since lightness is the channel `access.not_colour_alone` says survives every colour deficiency.  
**Prompt:** `the subject in a colour that exists nowhere else in the frame, clean colour separation from the crowd behind, the subject also lighter or darker than the crowd`  
**Yields to:** `color.accent` — Too many separated elements; let one carry the eye.  
`color.contrast_separation`

### Crushed Blacks

**Also called:** crushed shadows, deep blacks, black point pulled down  
**What it is:** Pulling the black point down so detail in the dark areas is lost and they become pure black. It is a deliberate grading decision and the opposite of lifting the blacks in a faded look.  
**Effect on the audience:** Power, decisiveness and a modern feel. The image feels heavy and deep, and the darkness becomes a wall rather than a space.  
**Used for and where it works best:** Trailers, action, noir and premium advertising, and any material that plays on a high contrast display. It is very useful on AI generated footage because it hides noise and broken detail in the dark areas.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Music Video, Feature Film, Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, AI-Generated Clip, Product Video / Motion Design, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Action, Noir / Neo-Noir, Thriller / Suspense, Crime / Procedural, Sci-Fi, Horror, Cyberpunk, Superhero  
**Avoid when:** Crushed detail does not come back once it is baked in, so in documentary and archive it costs you real information; the exception is a piece where the darkness itself is the meaning, and there it is worth keeping an uncrushed master. And in night scenes it leaves the characters shapeless on cheaper displays.  
**Prompt:** `crushed blacks, deep pure black shadows with no detail, high contrast modern grade`  
**Yields to:** `color.doc_desaturated` — Documentary and archive, where lost detail is lost information.  
`color.crushed_blacks`

### Colour Script

**Also called:** colour board, colour key sequence  
**What it is:** A small board laying out the colour of every scene in the piece from beginning to end in one row, so you can see the entire colour journey at a glance. It is a standard animation tool and is now used in live action too.  
**Effect on the audience:** It prevents the biggest visual mistake of all: every scene looking good on its own while the whole piece has no direction. With the board you see repetition or monotony before you spend a single shooting day.  
**Used for and where it works best:** Build one for any project longer than five minutes: a row of swatches, one per scene, arranged in edit order. In animation and kids content it is a mandatory step, and in heritage documentary it guarantees the whole episode is not one continuous shade of sand.  
**Best in:** formats: 2D Animation (Western / Cartoon), 3D CG Animation, Feature Film, Drama Series Episode, Heritage / Historical Documentary, Kids Content, Music Video, Stop Motion, Limited Series, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Fantasy / Epic, Family, Drama, Heritage (civilisation-focused), Historical / Biopic, Preschool / Early Learning, Adventure, Mythology / Ancient Epic, Fairy Tale  
**Avoid when:** If the colour script becomes a rigid rule that cannot change in the edit it turns from a tool into a constraint. And drawing one before you know the final scene order is wasted work.  
**Prompt:** `a sequence of scenes moving from cold grey through amber into deep blue, the colour journey planned across the whole piece`  
`color.color_script`

### Bleach Bypass

**Also called:** silver retention, skip bleach, ENR  
**What it is:** A lab process that leaves the silver in the negative instead of washing it out, producing a black and white layer sitting on top of the colour: very high contrast, low saturation and heavier grain. It is now reproduced digitally in the grade.  
**Effect on the audience:** A metallic harshness. The image feels as though it survived the event, skin goes pale and metal reads hard.  
**Used for and where it works best:** War, survival, dystopia and hard crime, and the shock sequence. It is strongest on battle, metal and rain because it lifts texture and removes any surplus beauty.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Game Cinematic / Gameplay, Short Film, Music Video, Limited Series, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: War, Survival, Dystopia / Post-Apocalyptic, Crime / Procedural, Thriller / Suspense, Action, Horror, Zombie, Disaster  
**Avoid when:** The high contrast crushes detail in both shadow and highlight, so in a bright location you lose information. On emotional faces it leaves skin dead and pushes the viewer away.  
**Prompt:** `bleach bypass look, very high contrast with desaturated colour, heavy texture and pale metallic skin tones`  
**Yields to:** `color.desaturation` — Emotional faces in the same war and survival material.  
`color.bleach_bypass`

### Cross Processing

**Also called:** cross-processed look, wrong chemistry look  
**What it is:** Developing film in chemistry meant for a different stock, so the colours shift unpredictably: green or blue shadows, yellow highlights and raised contrast. Digitally it is recreated by bending the individual channel curves.  
**Effect on the audience:** A beautiful malfunction. The image feels like it came from another era or a broken machine, giving instant identity and a deliberate wrongness.  
**Used for and where it works best:** Music video, fashion, short-form and experimental sequences, and a disturbed flashback. Apply it to a defined stretch inside the piece so it marks a mental state rather than becoming a general style.  
**Best in:** formats: Music Video, Fashion Film, Vertical Short-Form (Reels, Shorts, TikTok), Experimental / Art Film, Title Sequence / Opening Credits, Short Film, Commercial / TVC, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Psychological / Arthouse, Surreal / Absurdist, Cyberpunk, Musical, Horror, Coming of Age, Thriller / Suspense, Dark Comedy / Satire  
**Avoid when:** It distorts skin tone strongly and unpredictably, so it fails in drama that needs honest faces. Applied to a whole piece it tires quickly and starts to look like a phone app filter.  
**Prompt:** `cross processed look, green shifted shadows and yellow highlights, raised contrast and unnatural colour crossover`  
**Yields to:** `color.dream_tint` — Altered mental state in drama that needs honest faces.  
`color.cross_process`

### Three-Strip Technicolor Look

**Also called:** Technicolor, classic dye transfer look  
**What it is:** An old capture system recording three separate negatives for red, green and blue and printing them with dyes, producing extremely pure saturated colour and warm pink skin. It is emulated digitally with selective saturation and channel separation.  
**Effect on the audience:** The magic of the old studios. The colours read purer than reality, so the world feels lovingly manufactured rather than real, and that is exactly its charm.  
**Used for and where it works best:** Musicals, fairy tales, the period from the nineteen thirties to the fifties, and the fantasy world inside a modern film. It is excellent in advertising when you want nostalgia for classic cinema. This card is the grade laid over the footage; when the frame must read as shot on the stock itself, with the designed sets and costumes that needs, the card is `look.technicolor`.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Title Sequence / Opening Credits, Short Film, 2D Animation (Western / Cartoon), Stop Motion, Experimental / Art Film, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Musical, Fairy Tale, Fantasy / Epic, Romance, Comedy, Melodrama, Family, Adventure  
**Avoid when:** In any serious or realist subject the purity of the colour contradicts the material. And on darker skin a crude emulation pushes an incorrect redness, so skin has to be treated separately.  
**Prompt:** `three strip Technicolor look, ultra pure saturated primaries, warm rosy skin tones, glowing storybook colour`  
**Example:** The Wizard of Oz (1939), the Oz sequences in three-strip Technicolor.  
**Yields to:** `color.kodachrome` — Realist period material that pure dye colour contradicts.  
`color.technicolor`

### The Kodachrome Grade

**Also called:** Kodachrome look, vintage slide film look  
**What it is:** An emulation of Kodachrome slide film: strong reds and oranges, deep blues, high contrast, solid blacks and fine grain. It is the film of mid twentieth century family photographs and magazines.  
**Effect on the audience:** A living colour memory. Unlike sepia, here the past reads vivid and strong rather than faded, so the nostalgia arrives as joy rather than sorrow.  
**Used for and where it works best:** Childhood scenes in the nineteen seventies and eighties, old travel, the family archive, and any flashback you want to feel warm and beloved. In advertising it works beautifully on long established products. This card is the grade laid over the footage; when the frame must read as shot on the slide film itself, the card is `look.kodachrome`.  
**Best in:** formats: Feature Film, Commercial / TVC, Music Video, Documentary Feature, Heritage / Historical Documentary, Short Film, Video Essay, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Coming of Age, Family, Drama, Road Movie, Historical / Biopic, Romance, Melodrama, Slice of Life  
**Avoid when:** It carries a specific era, so applied to a modern scene it sends the wrong time signal. And the strong red saturation pushes skin toward red very quickly.  
**Prompt:** `Kodachrome film look, strong saturated reds and deep blues, high contrast with fine grain, vintage slide film feel`  
**Source:** reference — checked 2026-09-23: every description of the stock that speaks of contrast calls it high (Wikipedia, *Kodachrome*, the Contrast section; camera-wiki.org, *Kodachrome*: *"a fairly contrasty nature"*); Kodak's own data sheet E-55 (2009) confirms the fine grain and does not describe contrast in words.  
**Yields to:** `look.sepia` — The past should read faded and sorrowful, not vivid.  
`color.kodachrome`

### Film Print Emulation

**Also called:** print film emulation, PFE, Kodak 2383, Fuji 3513  
**What it is:** Applying a curve that mimics the behaviour of a cinema print stock: Kodak 2383 gives richer contrast and warmth while Fuji 3513 gives gentler skin and cooler shadows. It sits at the end of the grading chain on top of everything else.  
**Effect on the audience:** The digital image loses its artificial cleanliness and starts behaving like film: highlights roll off gently and saturated colours stop clipping.  
**Used for and where it works best:** Put one on any digital project you want to feel cinematic and pick by subject: Kodak for warm heritage material, Fuji for quiet drama and delicate skin. It matters most on AI generated material because it gives every clip the same highlight behaviour.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Heritage / Historical Documentary, Short Film, AI-Generated Clip, Trailer / Teaser, Documentary Feature, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Romance, Thriller / Suspense, War, Crime / Procedural, Melodrama  
**Avoid when:** Placed before the rest of the grade the result is unpredictable; it belongs at the end of the chain. And in explainer, corporate and product work where colour accuracy matters, the emulation distorts the true colour.  
**Prompt:** `film print emulation, gentle highlight rolloff and rich contrast, warm Kodak print character`  
**Yields to:** `color.clinical_white` — Explainer, corporate and product work needing true colour.  
`color.film_emulation`

### LUT as a Look

**Also called:** look up table, creative LUT, show LUT  
**What it is:** A prepared conversion table that maps every colour in the image to another one consistently. A technical LUT converts between colour spaces while a creative LUT imposes a complete look in one step.  
**Effect on the audience:** Instant unification. Every clip starts belonging to the same world, which matters more than whether the look itself is beautiful.  
**Used for and where it works best:** Lock one LUT for the whole project from day one and show it on the monitor while shooting so everyone sees the target. On AI projects it is the one look laid over clips from different models after they have been pulled to one reference shot (`color.continuity`), not a substitute for that match: clips that come back with different balance and exposure are the badly balanced shots it would amplify.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, AI-Generated Clip, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Trailer / Teaser, Corporate / Training, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Action, Thriller / Suspense, Sci-Fi, Romance, Crime / Procedural, Historical / Biopic, Comedy  
**Avoid when:** A LUT never fixes a badly exposed or badly balanced shot; it amplifies the error. And if you lean on it instead of doing the primary correction you end up with a broken image you cannot recover later.  
**Prompt:** `consistent cinematic LUT applied across every shot, unified colour response and contrast curve`  
**Yields to:** `color.primary_grade` — A badly exposed or badly balanced shot, before any look.  
`color.lut`

### HDR and Tone Mapping

**Also called:** high dynamic range, HDR grade, tone mapping  
**What it is:** Display with a far wider brightness range than standard, so highlights can genuinely be brighter instead of being clipped. Tone mapping is the process of bringing that range down to a normal display without losing the detail.  
**Effect on the audience:** A sense of real light. The sun feels like the sun, fire feels like fire, and a night scene keeps its darkness while holding its detail.  
**Used for and where it works best:** Material delivered to streaming and modern televisions, and scenes with a large brightness range: a window inside a room, fire at night, desert at noon. In heritage work it makes sun on stone feel physically real.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Sports Broadcast / Sports Film, Concert / Live Event, Travel / Real Estate / Hospitality, Limited Series, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Nature / Wildlife, Heritage (civilisation-focused), Historical / Biopic, Drama, Sci-Fi, Adventure, War, Science / Educational  
**Avoid when:** Aggressive tone mapping produces a flat strange over processed image. And you must build a separate standard version, because most of your audience will watch on a phone and not on a modern display.  
**Prompt:** `high dynamic range grade, bright specular highlights holding detail, deep shadows with real range between them`  
**Yields to:** `look.hdr_sdr` — The phone audience that needs the standard-range deliverable.  
`color.hdr`

### The Vintage Faded Grade

**Also called:** faded film look, lifted blacks, milky shadows  
**What it is:** Lifting the black point so black becomes a tinted grey, with low saturation and a warm or greenish cast. It mimics an old print that has aged and been exposed to light.  
**Effect on the audience:** Temporal distance. The image feels like a memory kept in a box rather than an event happening now.  
**Used for and where it works best:** Flashback, the family video tape, the archive section, and any shot standing for the past inside a sharp present. In music video and short-form it delivers instant nostalgia with no words.  
**Best in:** formats: Music Video, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature, Video Essay, Title Sequence / Opening Credits, Short Film, Wedding / Event Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Coming of Age, Drama, Romance, Melodrama, Historical / Biopic, Psychological / Arthouse, Family, Tragedy  
**Avoid when:** Lifting the blacks kills depth, so applied to the present day scenes it makes the whole piece look weak. And it is one of the most overused filters on social platforms, so it usually needs a time meaning behind it; the exception is a piece whose whole surface is openly nostalgic.  
**Prompt:** `faded vintage grade, lifted milky blacks, low saturation with a warm cast, aged print feel`  
**Yields to:** `color.crushed_blacks` — Present-day scenes needing depth, not milky blacks.  
`color.vintage_faded`

### The Digital Green Tint

**Also called:** the Matrix green, code green  
**What it is:** A visible green cast across the whole image standing for a digital or simulated world. It became famous through The Matrix, where scenes inside the simulation were graded green and scenes outside it were not.  
**Effect on the audience:** The viewer knows where they are without dialogue. The colour becomes a map: green means inside the system, no green means the truth.  
**Used for and where it works best:** Any story with two worlds or two states of consciousness: the simulation, the dream, the implanted memory, inside the game. Apply the principle to your own world: assign a colour to each world and hold it from the first shot.  
**Best in:** formats: Feature Film, Drama Series Episode, Game Cinematic / Gameplay, Music Video, Trailer / Teaser, Short Film, Anime (Japanese 2D), 3D CG Animation, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Sci-Fi, Cyberpunk, Dystopia / Post-Apocalyptic, Thriller / Suspense, Psychological / Arthouse, Action, Isekai (anime), Surreal / Absurdist  
**Avoid when:** Green makes skin look unwell, so face tones have to be protected separately. And if the whole piece is green the purpose is lost because there is no second world to compare it with. Which world the viewer is in is colour doing a job, so the green must not be the only sign of it: give each world a second channel as well - its own set, its own sound, its own texture - as `access.not_colour_alone` requires wherever colour carries meaning.  
**Prompt:** `digital green tint across the whole frame, green leaning shadows and highlights, cold simulated world with its own hard geometry and screen texture as a second sign of the world`  
**Example:** The Matrix (1999), the green cast on the scenes set inside the simulation.  
**Yields to:** `color.traffic_yellow_blue` — Both worlds need their own coded grade.  
`color.matrix_green`

### The Traffic Yellow and Blue

**Also called:** location coded grade, two world colour split  
**What it is:** Each storyline or location takes an entirely different colour treatment: one strand in hot burnt yellow and another in cold hard blue. Steven Soderbergh used it across the separate strands of Traffic.  
**Effect on the audience:** The viewer knows which strand they are in within half a second of the cut, so you can jump between three stories without anyone getting lost.  
**Used for and where it works best:** The multi-strand film, the series with two timelines, and the documentary that moves between two countries or two eras. In heritage work assign one grade to the present day site and another to the reenactment, and the transition explains itself with no caption.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Video Essay, Trailer / Teaser, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Crime / Procedural, Political Thriller, Drama, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused), True Crime, War  
**Avoid when:** If the difference is subtle it does not register and you lose the whole benefit, so make it explicit - and explicit in more than colour: which strand the viewer is in is colour doing a job, so give each strand a second channel as well - its own locations, its own lens or texture - as `access.not_colour_alone` requires wherever colour carries meaning. And if both looks are ugly the audience spends the film with an image they dislike.  
**Prompt:** `two distinct grades across the piece, one strand in hot burnt yellow and the other in cold hard blue, each strand also carried by its own locations and its own lens or texture so the cut still reads in greyscale`  
**Example:** Traffic (2000), the Mexico strand in yellow and the Ohio strand in cold blue.  
**Yields to:** `color.flashback_tint` — Two timelines where a full strand grade is too loud.  
`color.traffic_yellow_blue`

### The Amelie Red and Green

**Also called:** storybook red and green palette  
**What it is:** A palette built on red and green with blue almost entirely removed from the frame, so the world becomes warm, rich and handmade. It comes from Amelie, directed by Jean-Pierre Jeunet.  
**Effect on the audience:** The viewer feels they have stepped into an illustrated book. The world is more beautiful than reality without becoming fantasy, so the characters read as beloved from the first shot.  
**Used for and where it works best:** Romantic comedy, the gentle tale and any sequence describing the world of an eccentric character. In advertising it gives warmth and humour, and in kids content it gives a rich safe world without cartoon over saturation.  
**Best in:** formats: Feature Film, Commercial / TVC, Short Film, Music Video, Kids Content, Drama Series Episode, 2D Animation (Western / Cartoon), Title Sequence / Opening Credits, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Rom-Com, Comedy, Fairy Tale, Family, Romance, Slice of Life, Surreal / Absurdist, Fantasy / Epic  
**Avoid when:** Removing blue makes any sky or water scene look wrong, so plan the shots around it. And in a serious or sad subject it makes the sorrow look decorated.  
**Prompt:** `warm red and green palette with blue removed, rich storybook colour, glowing amber interiors`  
**Example:** Amelie (2001), the red and green palette across the whole film.  
**Yields to:** `color.wes_pastel` — Sky and water scenes that must keep their blue.  
`color.amelie_red_green`

### The Wes Anderson Pastel

**Also called:** pastel symmetrical palette, storybook pastel  
**What it is:** A quiet tightly defined pastel palette of pink, pale yellow, powder blue and cream, with total control of set and costume so no outside colour enters, usually paired with symmetrical composition. It is the style of Wes Anderson.  
**Effect on the audience:** A world entirely constructed and openly admitting it. The viewer enjoys the design itself, and sad feelings delivered in that gentle register land harder for it.  
**Used for and where it works best:** Gentle dark comedy, a story inside a story, and advertising that wants an instantly recognisable identity. In kids content pastel gives visual calm, and in motion design it gives elegance with no colour shouting.  
**Best in:** formats: Feature Film, Commercial / TVC, Title Sequence / Opening Credits, Short Film, 2D Animation (Western / Cartoon), Stop Motion, Kids Content, Product Video / Motion Design, Music Video, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Dark Comedy / Satire, Comedy, Fairy Tale, Family, Drama, Romance, Surreal / Absurdist, Adventure  
**Avoid when:** Imitating it without the same discipline in set and costume gives an image that looks washed out rather than designed. And on realist or documentary subjects the palette reads as if it were mocking the material.  
**Prompt:** `controlled pastel palette of pink, pale yellow and powder blue, symmetrical framing, storybook art direction`  
**Example:** The Grand Budapest Hotel (2014), the pastel palette and symmetrical staging.  
**Yields to:** `color.pastel_preschool` — Kids work without full set and costume discipline.  
`color.wes_pastel`

### The Cold Steel-Blue Winter Grade

**Also called:** winter blue grade, cold steel look  
**What it is:** A cold grade with muted contrast: steel blue shadows, cyan leaning midtones and desaturated highlights sitting close to grey white. The blacks are not crushed and the whites are not blown.  
**Effect on the audience:** A physical cold and isolation. The viewer feels the weather in their body, and the muted contrast gives weight and slowness instead of sharp drama.  
**Used for and where it works best:** Winter, the north, the mountain and the cold sea, and scenes of mourning or long waiting. In Nordic thriller and northern crime it is the standard look, and in war it gives a static front with no heroism.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Short Film, Trailer / Teaser, Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Crime / Procedural, Thriller / Suspense, Tragedy, War, Survival, Drama, Mystery / Whodunit, True Crime, Psychological / Arthouse  
**Avoid when:** In a warm or emotional scene it kills empathy. And on pale skin it looks lifeless, so you must protect the skin with a little warmth held inside the cold grade.  
**Prompt:** `cold steel blue grade, muted contrast, cyan midtones and desaturated near white highlights, winter light`  
**Yields to:** `color.blue_isolation` — One cold character inside a scene that stays warm.  
`color.steel_blue_winter`

### The Fincher Green-Yellow

**Also called:** muted yellow green grade, procedural grade  
**What it is:** A low saturation look leaning yellow green in the midtones, with deep blacks and strict control of any intruding colour. It is associated with the films of David Fincher.  
**Effect on the audience:** A cold precision and the sense of a world that is orderly and unforgiving. The image looks too controlled, and that control is itself unsettling.  
**Used for and where it works best:** Crime, investigation and institutional thriller, and scenes in offices, labs and archives. It is excellent in true crime because it delivers the feeling of a case file rather than an adventure.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Trailer / Teaser, Video Essay, AI-Generated Clip, Short Film, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Crime / Procedural, True Crime, Thriller / Suspense, Mystery / Whodunit, Political Thriller, Psychological / Arthouse, Legal Drama, Noir / Neo-Noir, Drama  
**Avoid when:** Green in the midtones makes skin look unwell, so protecting it is mandatory. And on warm or family material the look delivers a coldness the story never asked for.  
**Prompt:** `muted yellow green grade, low saturation midtones, deep controlled blacks, clinical precise colour`  
**Yields to:** `color.doc_desaturated` — True crime that must read as testimony, not as style.  
`color.fincher_green`

### The Villeneuve Sand and Blue

**Also called:** epic sand and blue palette, monolithic grade  
**What it is:** A look built from two large colour masses with little chromatic detail between them: dusty sand orange fields set against cold blue or metallic grey. It is associated with the films of Denis Villeneuve.  
**Effect on the audience:** Scale and silence. A large mass of a single colour makes the location look bigger than the people in it, so the viewer feels a mythic sense of scale.  
**Used for and where it works best:** The desert, the future city, the temple and space, and large establishing shots. For Mesopotamian heritage it is a strong choice because mud brick, sand and stone deliver that same warm mass while the blue comes from the sky and the river.  
**Best in:** formats: Feature Film, Trailer / Teaser, Heritage / Historical Documentary, 3D CG Animation, Game Cinematic / Gameplay, Title Sequence / Opening Credits, Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Sci-Fi, Heritage (civilisation-focused), Mythology / Ancient Epic, Historical / Biopic, Space Opera, Dystopia / Post-Apocalyptic, Adventure, War, Drama  
**Avoid when:** It needs large compositions and empty space, so in a crowded interior it does not work. And if the sand tone covers everything the characters dissolve inside the colour.  
**Prompt:** `monolithic palette, vast dusty sand orange against cold blue grey, minimal colour detail, epic scale`  
**Example:** Dune (2021), the sand tones of Arrakis against the cold blues of the other worlds.  
**Yields to:** `color.mixed_temp` — Crowded interiors, where two colour masses fail.  
`color.villeneuve_sand_blue`

### The Refn Neon Magenta and Cyan

**Also called:** saturated neon palette, dreamlike neon grade  
**What it is:** Extremely high saturation in two opposing neon hues, magenta or crimson against cyan, with deep blacks and no neutral colour anywhere in the frame. It is associated with the films of Nicolas Winding Refn.  
**Effect on the audience:** Dream, danger and a toxic beauty. The image feels drugged and slow, and violence inside it reads as ritual rather than as reality.  
**Used for and where it works best:** Psychological thriller, fashion, music video and dream sequences. Use it for a complete scene rather than a single shot, because its power lies in sustained immersion rather than in contrast with what surrounds it.  
**Best in:** formats: Music Video, Fashion Film, Feature Film, Short Film, Experimental / Art Film, Trailer / Teaser, Title Sequence / Opening Credits, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Psychological / Arthouse, Thriller / Suspense, Surreal / Absurdist, Crime / Procedural, Cyberpunk, Horror, Noir / Neo-Noir, Musical  
**Avoid when:** The extreme saturation erases skin tone completely and faces lose their humanity. In any story that needs realistic empathy it pushes the viewer away instead of drawing them in.  
**Colour temperature:** neon has none. Balance the ambient and write the neon colour in words — `light.kelvin_reference`  
**Prompt:** `heavily saturated neon palette, magenta and cyan filling the frame, deep blacks, no neutral colour anywhere`  
**Example:** The Neon Demon (2016), the saturated magenta and cyan sequences.  
**Yields to:** `color.cyberpunk_night` — A neon world that still needs human empathy.  
`color.refn_neon`

### Cyberpunk Neon Night

**Also called:** neon noir palette, blade runner night  
**What it is:** A city night built on saturated neon reflecting off wet surfaces, with haze and a deep blue background, and multi coloured signage inside the same frame.  
**Effect on the audience:** A crowded cold future. The human looks small beneath enormous advertising, and the beautiful colour hides poverty and threat beneath it.  
**Used for and where it works best:** Sci-fi, cyberpunk and dystopia, and music video and vertical short-form. It is one of the most successful looks in vertical because upright signage and reflections fill a tall frame naturally.  
**Best in:** formats: Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay, Feature Film, Trailer / Teaser, Commercial / TVC, 3D CG Animation, Anime (Japanese 2D), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Cyberpunk, Sci-Fi, Dystopia / Post-Apocalyptic, Thriller / Suspense, Noir / Neo-Noir, Action, Crime / Procedural, Mecha (anime), Seinen (mature anime)  
**Avoid when:** It is heavily overused in generated content, so give it local specifics or it reads as a template. And without rain, haze or reflective surfaces the neon does not spread and half the power is lost.  
**Colour temperature:** neon and gas-discharge have none; the figure belongs to whatever ambient the scene balances to — `light.kelvin_reference`  
**Prompt:** `cyberpunk neon night, saturated signage reflecting on wet asphalt, deep blue haze, small figures under huge screens` Text treatment: the signage is seen, not read (`textimg.read_or_seen`); no legible word is asked of the generator.  
**Yields to:** `color.refn_neon` — No rain, haze or reflective surface to spread the neon.  
`color.cyberpunk_night`

### The Golden Heritage Grade

**Also called:** warm ancient grade, amber heritage look  
**What it is:** A warm look built on amber, gold and earth brown at moderate contrast, with blue protected in the sky only so the whole frame does not go yellow. It is designed so mud brick, stone, bronze and wool all read at their best.  
**Effect on the audience:** Dignity, longing and belonging. The past looks alive and warm rather than extinct, and the viewer feels they are seeing a civilisation and not a ruin.  
**Used for and where it works best:** Heritage and historical documentary, reenactment, and shots of sites and museum objects. Set it at the start of the project and build every clip on it, because stock and archive material has to be unified into the same look.  
**Best in:** formats: Heritage / Historical Documentary, Docudrama / Reenactment, Documentary Feature, Documentary Series, Feature Film, Trailer / Teaser, AI-Generated Clip, Video Essay, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, Drama, War, Adventure, Tragedy  
**Avoid when:** Push the gold too far and everything turns yellow, so mud, bronze and actual gold stop being distinguishable, which damages the accuracy of the subject itself. And in night scenes warmth alone makes the night read as day.  
**Prompt:** `warm golden heritage grade, amber and earth brown tones, blue held only in the sky, sunlit stone and bronze`  
**Yields to:** `color.day_night_tint` — Night scenes that warmth alone makes read as day.  
`color.golden_heritage`

### The Clinical White Grade

**Also called:** clean white grade, product white look  
**What it is:** A clean white look at low contrast and moderate saturation, where white is truly white with no cast and the shadows are pale and colourless. The only colour allowed is the colour of the subject itself.  
**Effect on the audience:** Confidence, clarity and cleanliness. The viewer feels nothing is being disguised, so the product or the information arrives with nothing between.  
**Used for and where it works best:** Product video, technology, medical advertising, explainer and corporate work, and anything that needs accurate colour. It is very useful in educational kids content because clarity matters more than mood.  
**Best in:** formats: Product Video / Motion Design, Commercial / TVC, Explainer, Corporate / Training, Kids Content, Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, News Report / Reportage, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Science / Educational, Comedy, Family, Preschool / Early Learning, Medical Drama, Legal Drama  
**Avoid when:** In any drama it is a look with no mood and no point of view, so the scene starts feeling like an advertisement. And if the white carries no gradient at all the forms flatten and the product loses its shape.  
**Prompt:** `clean clinical white grade, neutral true whites, low contrast pale shadows, accurate product colour`  
**Yields to:** `color.temperature` — Drama, where a neutral look gives no point of view.  
`color.clinical_white`

### Colour as a Story Arc

**Also called:** colour journey, colour progression  
**What it is:** The piece opens in one colour register and ends in a completely different one, with the change arriving gradually across the acts rather than as a jump. The colour travels with the character's transformation.  
**Effect on the audience:** The viewer feels the transformation without noticing it. They leave with the sense that something changed, and that sense came from colour rather than from dialogue.  
**Used for and where it works best:** Any piece with an internal journey: warm to cold as a character loses their faith, or grey to colour as they are freed. In a series apply it across the whole season so the finale carries a colour we never saw in the premiere. A colour change across a piece is declared as a new fixed grade line that governs from its first shot to the end of its chapter (`ai.colour_grade_lock`); it is never allowed to drift shot by shot.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Music Video, 2D Animation (Western / Cartoon), 3D CG Animation, Heritage / Historical Documentary, Documentary Feature, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Tragedy, Coming of Age, Romance, War, Fantasy / Epic, Historical / Biopic, Psychological / Arthouse, Melodrama  
**Avoid when:** If the change arrives suddenly in one scene it reads as a grading error rather than an arc. And it has to be planned before the shoot, because set and costume are part of the arc and not just the grade.  
**Prompt:** `the palette shifting gradually from warm amber in the opening to cold desaturated blue by the end`  
**Yields to:** `ai.colour_grade_lock` — as the mechanism. The arc is declared as a new fixed grade line per chapter, never allowed to drift shot by shot.  
`color.arc`

### Colour-Coding Characters

**Also called:** character palette, colour identity  
**What it is:** Each character is assigned a colour in their costume or in the space they inhabit and holds it across the piece. Later you can swap two characters' colours in the final act to say an exchange has taken place.  
**Effect on the audience:** The viewer recognises a character out of the corner of their eye and reads relationships from colour: who is close to whom and who has turned into whom.  
**Used for and where it works best:** Any piece with a large cast, animation and kids content, and the long running series. The swap in the third act delivers the strongest dramatic information available without a word: the hero is now wearing the villain's colour.  
**Best in:** formats: 2D Animation (Western / Cartoon), 3D CG Animation, Kids Content, Drama Series Episode, Feature Film, Limited Series, Game Cinematic / Gameplay, Stop Motion, Music Video, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Family, Fantasy / Epic, Preschool / Early Learning, Drama, Adventure, Superhero, Mythology / Ancient Epic, Shonen Battle (anime), Fairy Tale  
**Avoid when:** If the assigned colours sit close together they do not read and the idea is wasted, so keep the differences clear. And in realist drama a rigid one colour per character rule looks contrived. Telling two characters apart is colour doing a job, so colour must not be the only way to do it: give each a second channel as well - silhouette, a prop, a position - as `access.not_colour_alone` requires wherever colour carries meaning.  
**Prompt:** `each character locked to a distinct costume colour and a distinct silhouette, the hero in deep red and the rival in cold green throughout, the two also far apart in lightness`  
**Yields to:** `color.contrast_separation` — Assigned character colours too close to read apart.  
`color.character_coding`

### Colour Drain

**Also called:** progressive desaturation, colour loss  
**What it is:** Progressively removing saturation across a piece or a scene, so the image loses colour little by little until it is almost grey at the lowest point of the story.  
**Effect on the audience:** The viewer feels life draining away. They do not notice the technique, only that they have become heavier and colder without knowing why.  
**Used for and where it works best:** The collapse of a character, illness, loss, and the move from peacetime into war. In a documentary about a disaster or a war, drain the colour chapter by chapter and the progression itself becomes the narration. Each step down is declared as a new fixed grade line that governs from its first shot to the end of its chapter (`ai.colour_grade_lock`); the drain is never allowed to drift shot by shot.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Limited Series, Short Film, Music Video, Heritage / Historical Documentary, Video Essay, AI-Generated Clip | genres: Tragedy, War, Drama, Survival, Melodrama, Dystopia / Post-Apocalyptic, Psychological / Arthouse, Medical Drama, True Crime  
**Avoid when:** A fast drain looks like a filter being switched off. And you must keep a little colour in the skin all the way down, otherwise you lose empathy before the story ends.  
**Prompt:** `colour draining away across the sequence, saturation falling scene by scene toward near grey`  
**Yields to:** `ai.colour_grade_lock` — as the mechanism. The drain is declared as a new fixed grade line per chapter, never allowed to drift shot by shot.  
`color.drain`

### Colour Return

**Also called:** colour restoration beat, the colour comes back  
**What it is:** The opposite move to the drain: after a long grey stretch, colour returns in a single moment or across a short ramp. It is usually attached to one dramatic event.  
**Effect on the audience:** A genuine physical relief. The viewer has been deprived of colour for a long stretch, so its return produces a joy they cannot explain.  
**Used for and where it works best:** The moment of healing, reconciliation, homecoming or birth, and the ending after a war. It has to be preceded by a long drain, because its entire power comes from the deprivation before it.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Music Video, Short Film, 2D Animation (Western / Cartoon), 3D CG Animation, Heritage / Historical Documentary, AI-Generated Clip | genres: Drama, Tragedy, War, Romance, Family, Fantasy / Epic, Survival, Faith / Biblical Epic, Melodrama  
**Avoid when:** If the colour returns with no clear dramatic reason it reads as a mistake. And if the grey before it was short, the return delivers nothing.  
**Prompt:** `colour flooding back into a near grey world, saturation rising across the shot as the sun reaches the room`  
`color.return`

### Red for Danger and for Love

**Also called:** red as signal, the red accent  
**What it is:** Using red as a carrier of meaning rather than decoration: one red element in the frame, or red light flooding the scene. Red is the only colour that works as an alarm and as desire at the same time.  
**Effect on the audience:** It raises the pulse. The human eye goes to red faster than to any other colour, so anything red in the frame becomes the most important thing in it.  
**Used for and where it works best:** The point of danger in a quiet scene, the dress, the blood, the door that must not open. Define what red means the first time it appears in the piece, and every return after that carries the same meaning with no explanation - though not by hue alone: a meaning defined in red is colour doing a job, so tie it to a second channel as well - the same object, the same place, the same sound - as `access.not_colour_alone` requires wherever colour carries meaning.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Trailer / Teaser, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Game Cinematic / Gameplay, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Horror, Thriller / Suspense, Romance, Crime / Procedural, Melodrama, Action, Gothic / Vampire, Shojo (anime romance), Tragedy  
**Avoid when:** If the whole frame is red the colour loses its function as a signal and becomes only a mood. And red as an alarm is worn out, so without a meaning of your own it reads as automatic.  
**Prompt:** `one saturated red element inside an otherwise neutral frame, the element also set apart by its lightness and its place in the frame, the eye pulled straight to it`  
**Yields to:** `color.monochromatic` — The whole frame is red, so it is mood and not signal.  
`color.red`

### Blue for Isolation

**Also called:** blue as loneliness, cold blue character  
**What it is:** Flooding the scene or the character in cold blue with no warm source against it, whether through lighting, grading or design and costume.  
**Effect on the audience:** Distance, cold and solitude. The viewer feels the character is far away from them even in a close-up.  
**Used for and where it works best:** The night after a loss, the empty room, the person in a crowd nobody sees, the call that goes unanswered. In thriller and drama put it on one character inside an otherwise warm scene and the isolation reads in a single shot.  
**Best in:** formats: Feature Film, Drama Series Episode, Vertical Micro-Drama, Music Video, Short Film, Limited Series, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Tragedy, Thriller / Suspense, Psychological / Arthouse, Melodrama, Romance, Coming of Age, Noir / Neo-Noir, Seinen (mature anime)  
**Avoid when:** Blue has become the default for any night scene, so with no warmth against it, it reads as ordinary night rather than as isolation. And on skin it turns lifeless very fast.  
**Prompt:** `cold blue light isolating the figure, no warm source anywhere, everyone else in the scene lit warm`  
**Yields to:** `color.warm_cold` — Ordinary night unless a warm source opposes it.  
`color.blue_isolation`

### Yellow for Madness and Fever

**Also called:** sickly yellow, fever yellow, oppressive heat yellow  
**What it is:** A strong yellow push in the midtones with suffocating contrast, making the air feel hot and unwell. Unlike warm gold, this yellow has nothing to do with sun and everything to do with sickness and pressure.  
**Effect on the audience:** Constriction and physical tension. The viewer feels heat and sweat, and time starts to feel slow and heavy.  
**Used for and where it works best:** Fever, delirium, confinement in the heat, the long interrogation, and the city in summer before something breaks. In psychological thriller and war apply it to one scene so it reads as a state rather than as a general look.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Music Video, Game Cinematic / Gameplay, Trailer / Teaser, Anime (Japanese 2D), AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Psychological / Arthouse, Psychological Horror, Thriller / Suspense, War, Crime / Procedural, Survival, Tragedy, Dystopia / Post-Apocalyptic, Seinen (mature anime)  
**Avoid when:** It genuinely makes skin look ill, so in a scene that needs sympathy it works against you. And it is easily confused with a warm desert look, so keep the difference clear in the contrast.  
**Prompt:** `oppressive yellow cast in the midtones, hot airless feel, sweat on the skin, suffocating contrast`  
**Yields to:** `color.villeneuve_sand_blue` — Heat and desert wanted, not sickness.  
`color.yellow_madness`

### The Sickly Green

**Also called:** poison green, illness green, nausea green  
**What it is:** Pushing a pale or yellowed green into skin and neutral surfaces so the scene feels unhealthy. It is achieved through lighting, grading or both together.  
**Effect on the audience:** Nausea and suspicion. The brain links green on a face with illness, poison and rot, so it rejects the character or the place instinctively.  
**Used for and where it works best:** Illness, poisoning, moral corruption, and the place where something has gone wrong. In body horror and psychological thriller it is the light of transformation, and in dark comedy it makes a character look mean without a line of dialogue.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Game Cinematic / Gameplay, Trailer / Teaser, Anime (Japanese 2D), Music Video, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Body Horror, Psychological Horror, Horror, Thriller / Suspense, Dark Comedy / Satire, Crime / Procedural, Dystopia / Post-Apocalyptic, Supernatural Horror  
**Avoid when:** Green on skin is very heavy and hard to reverse in the grade, so decide it before you shoot. And in any emotional scene it destroys empathy completely.  
**Prompt:** `sickly pale green cast on the skin and the walls, unhealthy tint, faint nausea in the colour`  
**Yields to:** `color.fincher_green` — Wrongness in a place, not illness on a face.  
`color.sickly_green`

### Purple for the Otherworld

**Also called:** violet magic, otherworldly purple  
**What it is:** Using violet or indigo as the dominant colour of a scene or a being. It is rare in nature, so the viewer has no real world reference for it.  
**Effect on the audience:** Magic and strangeness. The viewer accepts immediately that this place or creature is not from our world, because the colour itself belongs to nowhere they know.  
**Used for and where it works best:** Magic, the dream, the spirit world, the portal and space, and the appearance of a supernatural being. In kids content and fantasy it is the colour of the fairy and the spell, and in supernatural horror it is the colour of the creature.  
**Best in:** formats: 2D Animation (Western / Cartoon), 3D CG Animation, Kids Content, Feature Film, Music Video, Game Cinematic / Gameplay, Anime (Japanese 2D), Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Fantasy / Epic, Supernatural Horror, Magical Girl (anime), Fairy Tale, Sci-Fi, Isekai (anime), Surreal / Absurdist, Gothic / Vampire, Space Opera  
**Avoid when:** In realist drama and documentary it has no justification and reads as a filter. And on skin it turns unnatural fast, so keep it in the background and the glow rather than on the face.  
**Prompt:** `deep violet light filling the space, otherworldly purple glow, indigo shadows around the figure`  
**Yields to:** `color.dream_tint` — Unreality inside a realist piece.  
`color.purple_otherworld`

### Day and Night Tint Separation

**Also called:** day night colour split, time of day grading  
**What it is:** A fixed rule across the piece that day is graded one way and night the opposite way: neutral warm days and blue nights, or the reverse. The rule repeats in every scene with no exception.  
**Effect on the audience:** The viewer knows the time of the scene within a fraction of a second, even with no window and no sky in frame. That frees the edit from needing an establishing shot every time.  
**Used for and where it works best:** Series, long drama and any documentary that jumps in time. In vertical micro-drama it is essential because there is no time for an establishing shot, so colour has to do most of the job, though never all of it: the time of day is colour doing a job, so give it a second channel as well - a lit lamp, a sound of the hour, a prop - as `access.not_colour_alone` requires wherever colour carries meaning.  
**Best in:** formats: Drama Series Episode, Soap Opera / Telenovela, Vertical Micro-Drama, Limited Series, Feature Film, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Documentary Series, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Drama, Crime / Procedural, Thriller / Suspense, Romance, Melodrama, Mystery / Whodunit, Coming of Age, Slice of Life  
**Avoid when:** Break the rule in a single scene and you confuse the viewer more than if you had no rule at all. And overdoing the night blue makes every night look identical with no variety.  
**Prompt:** `a consistent rule across the piece, neutral warm daylight scenes against cool blue night scenes, each scene also placing its hour without the tint: a lit practical lamp, a sound of the hour or a prop`  
**Yields to:** `color.mixed_temp` — Night scenes that must not all look identical.  
`color.day_night_tint`

### Flashback Tint

**Also called:** past tense grade, memory colour  
**What it is:** A dedicated look for past scenes, clearly and consistently different from the present: warmer, more faded or more saturated, the important thing being that it is identical every time the past returns.  
**Effect on the audience:** The viewer knows they are in the past with no caption and no explaining dialogue. Consistency is what teaches them the rule within the first two uses.  
**Used for and where it works best:** Any piece with two timelines, and any documentary mixing present day interviews with reenactment. In heritage work assign one look to the reenacted past and another to the site today, and make the gap wide enough that nobody can confuse them.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Heritage / Historical Documentary, Docudrama / Reenactment, Documentary Feature, Music Video, Short Film, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Mystery / Whodunit, Tragedy, War, Melodrama, True Crime, Romance  
**Avoid when:** Too subtle and it does not read; too loud and it looks like a filter. And the warm past look is worn out, so consider inverting it: a cold past against a warm present when the story allows.  
**Prompt:** `a distinct warmer slightly faded grade for every past scene, held identical each time the story returns there`  
**Yields to:** `color.vintage_faded` — The worn warm past; the faded print reads instead.  
`color.flashback_tint`

### Dream Tint

**Also called:** dream grade, unreality colour  
**What it is:** A look for unreal scenes that breaks the rules of natural colour: a cast that could not exist, an odd saturation, or colours that shift inside the shot itself.  
**Effect on the audience:** The viewer knows this is not real without being told, and accepts whatever happens next. The colour works as a contract between you and them.  
**Used for and where it works best:** The dream, the hallucination, the vision, the symbolic scene inside a realist piece. In anime and fantasy use a look that shifts inside the shot, and in drama use a stable but strange look so the viewer never loses track of which state they are in.  
**Best in:** formats: Feature Film, Anime (Japanese 2D), Music Video, Short Film, 3D CG Animation, Game Cinematic / Gameplay, Experimental / Art Film, Drama Series Episode, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Surreal / Absurdist, Psychological / Arthouse, Fantasy / Epic, Horror, Supernatural Horror, Isekai (anime), Magical Girl (anime), Shojo (anime romance), Drama  
**Avoid when:** If the dream look sits too close to the reality look the viewer gets lost and feels they missed something. And if the whole piece is dreams the look stops functioning as a signal.  
**Prompt:** `unreal dream grade, impossible colour cast shifting slowly within the shot, saturation drifting away from natural`  
**Yields to:** `color.monochromatic` — Dream too close to reality; a monochrome chapter marks it.  
`color.dream_tint`

### Pastel Preschool Palette

**Also called:** nursery palette, soft kids colour  
**What it is:** Light low saturation colours at very low contrast: soft pink, cream yellow, powder blue and mint green on pale backgrounds with no strong black anywhere.  
**Effect on the audience:** Safety and calm. A very young child is neither startled nor overstimulated, so they can follow the action and learn instead of being occupied by the image.  
**Used for and where it works best:** Preschool songs and learning, bedtime content and animated picture books. It is excellent for religious or heritage material aimed at children, because it makes the subject feel gentle and near rather than solemn.  
**Best in:** formats: Kids Content, 2D Animation (Western / Cartoon), 3D CG Animation, Stop Motion, Explainer, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Product Video / Motion Design, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Preschool / Early Learning, Family, Fairy Tale, Fantasy / Epic, Comedy, Slice of Life  
**Avoid when:** Low contrast means important elements do not separate, so give the main character slightly more saturation so they read. And for older children, above about seven, pastel reads as babyish and they reject it.  
**Prompt:** `soft pastel palette, low contrast pale pink, cream and powder blue, gentle nursery colour with no hard black`  
**Yields to:** `color.triadic` — Children over about seven, who reject pastel.  
`color.pastel_preschool`

### The Moody Desaturated Documentary Grade

**Also called:** observational grade, restrained doc look  
**What it is:** A restrained grade: saturation slightly below natural, moderate contrast, honest colour with no loud cast, and full protection of skin tone. It looks as though nothing was done to it.  
**Effect on the audience:** Credibility and gravity. The viewer believes what they are seeing is real, because the image is not trying to persuade them of anything.  
**Used for and where it works best:** Serious documentary, investigation, interview and true crime. In heritage work use it for the interview and present day site sections and keep the golden look for the reenactments, so the gap between the two grades separates testimony from imagination.  
**Best in:** formats: Documentary Feature, Documentary Series, News Report / Reportage, Interview / Video Podcast, Video Essay, Heritage / Historical Documentary, Vlog / YouTube Long-Form, Limited Series, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Verite / Observational, True Crime, War, Science / Educational, Political Thriller, Historical / Biopic, Drama, Nature / Wildlife  
**Avoid when:** Drop the saturation too far and the image loses the very honesty you wanted and starts looking treated. And on celebratory or nature subjects a muted grade cheats the material and makes it look poorer than it is.  
**Prompt:** `restrained documentary grade, slightly desaturated honest colour, moderate contrast, protected natural skin tones`  
**Yields to:** `color.saturation_high` — Celebratory or nature subjects a muted grade cheats.  
`color.doc_desaturated`

### The High-Contrast Trailer Grade

**Also called:** trailer look, punchy promo grade  
**What it is:** Raised contrast, deep blacks and selective saturation on two hues only, with high clarity. It is built so a shot reads within one second at any screen size.  
**Effect on the audience:** Energy and decisiveness. Every shot looks like the most important shot in the film, which is precisely what a trailer is for.  
**Used for and where it works best:** Trailers, teasers, commercials and title openings, and any material that plays between other content and has to cut through it. In vertical short-form it is an effective **overall promo look** when the piece can tolerate deep blacks and selective saturation; it does not guarantee subject legibility, which still belongs to `color.contrast_separation`, silhouette and position.  
**Best in:** formats: Trailer / Teaser, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Title Sequence / Opening Credits, Product Video / Motion Design, Sports Broadcast / Sports Film, Game Cinematic / Gameplay, Music Video, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography, Fine Art Photography | genres: Action, Thriller / Suspense, Superhero, Horror, Sci-Fi, Adventure, Heist, Disaster  
**Avoid when:** Applied to the film itself it exhausts the viewer within ten minutes. And the high contrast destroys detail in night shots, so check every night shot individually.  
**Prompt:** `high contrast promo grade, deep blacks, punchy selective saturation on two hues, maximum clarity`  
**Yields to:** `color.film_emulation` — The feature itself, where a promo grade exhausts.  
`color.trailer_contrast`

### Skin-Tone Protection

**Also called:** skin tone qualifier, protecting flesh tones  
**What it is:** Isolating the skin tone range during the grade and keeping the overall look off it, so you can push the whole image without turning faces green, blue or orange.  
**Effect on the audience:** The viewer accepts any look however extreme as long as the faces are right. Skin is the one reference the human eye knows without thinking.  
**Used for and where it works best:** Mandatory with any strong look: the digital green, neon, the blue night, the fever yellow. In heritage work it is decisive, because brown skin shifts fast under warm looks and turns orange, so it has to be isolated and returned to its true value.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Music Video, Heritage / Historical Documentary, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), AI-Generated Clip, Trailer / Teaser, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Sci-Fi, Cyberpunk, Thriller / Suspense, Romance, War  
**Avoid when:** Too wide a qualifier catches wood, mud and sand as well and the correction becomes random. And keeping skin perfectly neutral inside a fully coloured scene makes the face look cut out and separate from the shot.  
**Prompt:** `strong stylised colour grade with natural protected skin tones, faces held true inside the coloured world`  
**Yields to:** `color.secondary` — The hue qualifier catches wood, mud and sand too.  
`color.skin_protection`

### Primary Grade

**Also called:** lift gamma gain, primary correction, balance pass  
**What it is:** The first step in grading: setting the black point, the white point, the midtone exposure and the colour balance across the entire image with no isolation. It has to be finished before any creative look.  
**Effect on the audience:** The viewer never notices it, yet it decides whether the image will feel professional at all. Every good look is built on top of it.  
**Used for and where it works best:** Start here on every clip before you consider any look: set the black, set the white, balance the skin. On AI projects this step matters more than anywhere else, because every clip arrives with a completely different exposure and balance from the next.  
**Best in:** formats: all | genres: all  
**Avoid when:** Jumping to the creative look before the primary is done usually costs you the shot, because a LUT amplifies every error underneath it; the exception is a quick look test you throw away before the real work starts. And if you push the black and white points to extremes at this stage there is no range left to work with afterwards.  
**Prompt:** `correctly balanced image, clean black point and white point, neutral colour balance, accurate mid exposure`  
`color.primary_grade`

### Secondary Grading and Power Windows

**Also called:** secondaries, power window, qualifier, vignette shaping  
**What it is:** Adjusting only part of the image: a specific colour such as sky, skin or a shirt, or a geometric region that tracks with the movement. The rest of the image stays untouched.  
**Effect on the audience:** Invisible steering of the eye. You can lift a face slightly and darken the edges, so the viewer looks where you want without sensing that anyone directed them.  
**Used for and where it works best:** Rescuing a blown sky, calming a shirt whose colour steals attention, lifting a face in post, and gently darkening the edges. In heritage documentary use it to lift a carving sitting in shadow without changing the rest of the wall.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Documentary Feature, Heritage / Historical Documentary, Music Video, Product Video / Motion Design, Trailer / Teaser, AI-Generated Clip, Generated Keyframe Feeding Video, Poster / Static Design, Portrait Photography, Landscape Photography, Food Photography, Fashion Photography | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Thriller / Suspense, Romance, Science / Educational, War, Crime / Procedural  
**Avoid when:** If the isolation does not track properly the edge of the window becomes visible and floats, which is the most obvious error an audience can catch. And too many windows leave the image looking assembled rather than real.  
**Prompt:** `subtle secondary shaping, the face lifted slightly and the frame edges gently darkened, sky brought back down`  
`color.secondary`

### Colour Continuity Across Shots

**Also called:** shot matching, clip to clip matching, AI clip matching  
**What it is:** Making every shot in a scene feel as if it came from the same moment: the same exposure, the same balance, the same direction and quality of light. It is done by comparing shots side by side rather than one at a time.  
**Effect on the audience:** The viewer never notices the edit. Any colour jump between two shots breaks immersion even when the audience cannot name what went wrong.  
**Used for and where it works best:** Every scene in every piece. It is the number one problem with AI generated clips: each one comes back with a different balance, exposure and temperature, so pick one reference shot, pull every other clip to it before any look, then apply the final LUT over all of them at once.  
**Best in:** formats: AI-Generated Clip, Feature Film, Drama Series Episode, Documentary Feature, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary, Commercial / TVC, Vertical Micro-Drama | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Thriller / Suspense, Action, Romance, War, Mythology / Ancient Epic  
**Avoid when:** Grading a clip alone on its own screen usually misleads you, because the right decision comes from comparison with its neighbours; the exception is a standalone image with no cut on either side. And if you correct each shot to look good in isolation you end up with a scene that will never cut together.  
**Prompt:** `all shots matched to one reference, identical exposure balance and colour temperature across the whole sequence`  
`color.continuity`

### Never Colour Alone

**Also called:** colour-blind safe encoding, redundant encoding, dual channel
**What it is:** The rule that any information a frame carries in colour is also carried by something that is not colour — position, shape, a label, a texture, a line style, a number. It matters most wherever colour is doing a *job* rather than setting a mood: a chart, a map, a diagram, a key, a status, a team, a before-and-after, a highlighted element.
**Effect on the audience:** For roughly one viewer in twelve, the most common deficiency makes red and green hard to separate — and red-against-green is the single most-used encoding in exactly the places colour is load-bearing. The piece does not look wrong to them; it looks like it is withholding the answer.
**Used for and where it works best:** Anywhere colour encodes meaning. **Ask the frame one question: if this were greyscale, would it still say the same thing?** If not, add the second channel. **Direct labelling beats a key**, and it is better design for everyone, not only an accommodation — `dataviz.direct_labelling` is that card. **Separate by lightness, not only by hue**, because a lightness difference survives every colour deficiency and every bad projector. And **prefer shape, position and label to a second colour** when a chart or a map needs a distinction: adding hues is the instinct and it makes the problem worse. Where the piece is graded rather than built, the equivalent is not to let a story point rest on a hue the viewer must notice — a character identified only by the colour of their coat is the same failure in a drama.
**Best in:** formats: Explainer, Documentary Feature, Documentary Series, Corporate / Training, Museum Installation, Product Video / Motion Design, News Report / Reportage, Kids Content, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Educational, Documentary, Journalism, Science / Educational, Children's
**Avoid when:** Colour is carrying mood rather than meaning. A grade is not an encoding, and a warm-to-cold emotional arc does not need a redundant channel — applying this there produces a diagram where a feeling was wanted.
**Yields to:** `color.warm_cold` and the grading cards generally, wherever colour is atmosphere rather than information. This card governs colour that has a job.
**Prompt:** `every colour-coded element also distinguished by shape, position or a direct label; separations readable in greyscale`
`access.not_colour_alone`
