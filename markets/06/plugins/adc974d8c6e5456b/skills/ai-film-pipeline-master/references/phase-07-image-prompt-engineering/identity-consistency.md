# Identity Consistency Across Images

14 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Frozen Identity Sentence

**Also called:** locked sentence, character lock, verbatim description  
**What it is:** A single written description of the subject, agreed once, quoted into every prompt word for word and never paraphrased, shortened or replaced with a back-reference. Typically thirty to forty-five words covering bone structure, build, colouring and the two or three features that make the subject recognisable. A prop the subject holds is not in it; a recurring object gets a sentence of its own (`ident.object_card`).  
**Effect on the audience:** The same person arrives every time. Paraphrasing produces a cousin, and a back-reference such as the same character as before produces a stranger, sometimes a second person in the frame.  
**Used for and where it works best:** All series and episodic work, any project with recurring characters, and every generation where a face must match one made earlier. It is the foundation of this whole category. A subject shown at two ages carries one frozen sentence per age, each standalone and repeating the structural features verbatim (`ident.age_change`); within an age the sentence is never paraphrased or replaced. A shot that shows only part of the subject (hands only, from behind) quotes only the visible parts of the sentence, never the face clauses, and writes face out of frame (`HOW-PHASE-7-WORKS.md` law 4). Best in character sheets, keyframe plates and long-form series.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Poster / Static Design, Comics / Webtoon / Photo Essay, Brand Film, 2D Animation (Western / Cartoon), Heritage / Historical Documentary, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: all  
**Avoid when:** It usually crowds a short prompt when the subject is incidental and appears once. The exception is a background figure who later becomes important, which is why the sentence is cheap insurance written early.  
**Prompt:** `a man of about fifty, heavy-boned and broad through the shoulders, deep brown eyes set wide, a thick greying beard cut square, a pale scar through the left eyebrow, skin weathered dark by sun`  
**Yields to:** `ident.distinguishing_mark` — Subject is incidental and the prompt is short.  
`ident.frozen_sentence`

### Character Turnaround Sheet

**Also called:** model sheet, rotation sheet, multi-view plate  
**What it is:** A single generated image showing the subject from several fixed angles, front, both profiles and back, with a three-quarter as an optional extra — the two sides are not mirrors (`sheet.char.full_body_four_views_not_three`) — at the same scale, on a neutral ground, in the same lighting. Produced once and used as a reference thereafter.  
**Effect on the audience:** Identity that survives angle changes. A character held only by front-facing references becomes a different person the first time a shot needs a profile.  
**Used for and where it works best:** Any production with more than a handful of shots of one character. It is standard practice in animation and now the standard way of holding a generated character. Best in character sheets, animation and episodic work.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, 2D Animation (Western / Cartoon), 3D CG Animation, Comics / Webtoon / Photo Essay, Brand Film, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: all  
**Avoid when:** It usually wastes effort on a subject appearing in one or two frames. The exception is a subject who carries the piece, where even two appearances justify the sheet because the cost of a mismatch is the whole film.  
**Prompt:** `character sheet, one figure shown from four angles on one row, front, left profile, right profile, back, left and right sides drawn separately and not mirrored, identical scale, identical neutral grey ground, identical flat even lighting, no background elements`  
**Yields to:** `ident.frozen_sentence` — Subject appears in only one or two frames.  
`ident.turnaround_sheet`

### Expression Set

**Also called:** emotion sheet, face panel, performance plate  
**What it is:** A generated set of the same face carrying several defined states, neutral, alert, grieving, laughing, closed, produced as one image so that the underlying face is provably identical across all of them.  
**Effect on the audience:** Emotional range without identity drift. Generating each expression separately produces a slightly different face for each feeling.  
**Used for and where it works best:** Dialogue-heavy pieces, character-driven drama, and any project where reaction frames matter. Best in character sheets, animation and drama series.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, 2D Animation (Western / Cartoon), Comics / Webtoon / Photo Essay, Brand Film, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Drama, Tragedy, Comedy, Romance, Thriller / Suspense, Historical / Biopic, Heritage (civilisation-focused)  
**Avoid when:** It usually flattens performance when the set becomes a menu and shots are cast from it rather than directed. The exception is treating the set as identity evidence rather than as the performance itself.  
**Prompt:** `expression sheet, the same face in six panels, identical lighting and angle throughout, neutral, alert, grief held back, open laugh, cold refusal, exhaustion`  
`ident.expression_set`

### Scale and Proportion Reference

**Also called:** height chart, comparison plate, relative scale sheet  
**What it is:** One image placing every recurring character together at true relative height and build, used whenever two of them share a frame.  
**Effect on the audience:** Characters who keep their physical relationship. Without it the tall one is tall in some shots and not in others, which quietly destroys the sense that these people occupy one world.  
**Used for and where it works best:** Ensemble work, any story with a child and an adult, and heritage work where status is shown through physical presence. Best in character sheets, animation and ensemble drama.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, 2D Animation (Western / Cartoon), 3D CG Animation, Comics / Webtoon / Photo Essay, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Drama, Family, Fantasy / Epic, Historical / Biopic, Adventure, Comedy, Mythology / Ancient Epic  
**Avoid when:** It usually does nothing for a single-character piece. The exception is a single character opposite a recurring animal or object whose scale also has to hold.  
**Prompt:** `scale reference, all four figures standing in a line on a common ground line, true relative heights, neutral grey ground, flat lighting, front view only`  
**Yields to:** `ident.object_card` — Single character with a recurring object to scale.  
`ident.scale_reference`

### Wardrobe State Log

**Also called:** costume continuity, dress state, wardrobe timeline  
**What it is:** Recording which garment state a character is in for each scene, clean, travelled, torn, wet or bloodied, and naming that state explicitly in every prompt for that scene.  
**Effect on the audience:** Clothing that remembers what happened. Wardrobe that silently repairs itself between shots is one of the most common and most noticeable generated continuity failures.  
**Used for and where it works best:** Any story where time passes or events mark the characters, and critical in journey, battle and survival narratives. Best in historical drama, heritage work and adventure series. A new wardrobe state is written as a new fixed wardrobe line (`ai.wardrobe_lock`) from the shot it begins, and quoted identically in every shot after it; it is never a one-shot variation on the locked line.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Heritage / Historical Documentary, Comics / Webtoon / Photo Essay, Brand Film, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Drama, Historical / Biopic, Adventure, Action, War, Survival, Heritage (civilisation-focused)  
**Avoid when:** It usually over-specifies in a piece that occupies one continuous moment with no damage or change. The exception is a single scene long enough for weather or sweat to alter the garment within it.  
**Prompt:** `wardrobe state: the wool cloak now soaked through and dark at the hem, the left sleeve torn at the shoulder from the earlier fall, this state holds for the rest of the sequence`  
**Yields to:** `ai.wardrobe_lock` — as the mechanism. A state change is a re-lock, written as a new fixed wardrobe line quoted identically from the shot it begins, never a one-shot exemption from the locked line.  
`ident.wardrobe_state`

### Location Identity Plate

**Also called:** place lock, set reference, environment continuity  
**What it is:** The same discipline as a character sheet applied to a place: one generated plate establishing the architecture, materials, ground and scale of a location, referenced in every shot set there.  
**Effect on the audience:** A place the audience learns. Locations regenerated from description alone rearrange themselves between shots and the audience never builds a mental map.  
**Used for and where it works best:** Any location visited more than once, heritage reconstruction of a real site, and series work where the world persists. Best in location sheets, heritage documentary and episodic drama.  
**Best in:** formats: Location Sheet / Master Plate, General Reference Plate, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Comics / Webtoon / Photo Essay, Brand Film, Portrait Photography, Headshot, Character Sheet / Turnaround, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Heritage (civilisation-focused), Historical / Biopic, Drama, Verite / Observational, Mystery / Whodunit, Adventure  
**Avoid when:** It usually constrains when a location is deliberately dreamlike or unstable. The exception is establishing the stable version first so that the instability reads as a departure from something the audience knows.  
**Prompt:** `location plate, the courtyard seen from the entry, mudbrick walls with the palm line beyond, packed earth floor, the well at the centre right, flat midday light, no figures`  
`ident.location_plate`

### Object Identity Card

**Also called:** prop lock, artefact plate, hero object reference  
**What it is:** A dedicated reference image of a recurring object, shot clean, from the angle it will most often be seen, with its distinguishing marks clearly visible. The agent decides by the object's weight in the story: an object that recurs and carries meaning also gets a frozen object sentence, written and quoted like a character's, in the same thirty to forty-five words; a passing prop gets neither.  
**Effect on the audience:** An object that is the object. A sword described in words is a different sword in every shot; a sword with a reference card becomes a character.  
**Used for and where it works best:** Any story where an object carries meaning, heritage work built on a researched artefact, and product work where the item must be exact. Best in props sheets, product stills and heritage documentary.  
**Best in:** formats: Props Sheet, Product Still / Packshot, General Reference Plate, Generated Keyframe Feeding Video, Heritage / Historical Documentary, Poster / Static Design, Commercial / TVC, Portrait Photography, Headshot, Character Sheet / Turnaround, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Heritage (civilisation-focused), Historical / Biopic, Fantasy / Epic, Mythology / Ancient Epic, Mystery / Whodunit, Adventure, Drama  
**Avoid when:** It usually over-invests in an object seen once in passing. The exception is an object whose single appearance is the turning point of the story.  
**Prompt:** `object card, the bronze dagger alone on neutral grey, three-quarter view, the crescent inlay on the pommel and the notch in the blade edge both clearly visible, even flat lighting`  
`ident.object_card`

### Palette Lock

**Also called:** colour lock, three-tone discipline, base look  
**What it is:** Fixing a small set of governing colours, typically three, given as exact values, for a project or a sequence, and naming them in every prompt.  
**Effect on the audience:** A body of work that looks like one thing. Colour is the fastest signal of belonging, and it drifts faster than anything else across separate generations.  
**Used for and where it works best:** Series, campaigns, any multi-image deliverable, and sequences that must survive being cut together. Best in posters, social sets, brand films and comics.  
**Best in:** formats: Poster / Static Design, Thumbnail / Social Card, Brand Film, Comics / Webtoon / Photo Essay, Generated Keyframe Feeding Video, Commercial / TVC, Editorial / Magazine Image, Portrait Photography, Headshot, Character Sheet / Turnaround, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually fights a story that changes register deliberately, a warm past against a cold present. The exception is locking two palettes and naming which one governs each sequence.  
**Prompt:** `palette: deep clay red, dust ochre, and a single cold blue held for the sky only, no other saturated colour enters the frame`  
**Yields to:** `color.color_script` — The story changes register between sequences.  
`ident.palette_lock`

### Render Register Lock

**Also called:** medium lock, style discipline, look consistency  
**What it is:** Stating how the image is made, photographic with a named stock behaviour, painted with a named brush character, or rendered with a named surface quality, identically across every generation in the set.  
**Effect on the audience:** Images that belong to one hand. Register drift is subtler than colour drift and harder to spot until several images sit together.  
**Used for and where it works best:** All series and campaign work, illustrated pieces, and any project mixing generated images made in different sessions. Best in posters, comics, editorial sets and brand films.  
**Best in:** formats: Poster / Static Design, Comics / Webtoon / Photo Essay, Editorial / Magazine Image, Brand Film, Thumbnail / Social Card, 2D Animation (Western / Cartoon), Generated Keyframe Feeding Video, General Reference Plate, Portrait Photography, Headshot, Character Sheet / Turnaround, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually reads as sameness when a long piece needs variation to hold attention. The exception is varying composition and light while holding the register, which gives variety without breaking belonging.  
**Prompt:** `render register: photographic, fine grain, slightly soft highlight roll-off, no digital sharpening halo, identical across the set`  
`ident.render_register`

### Regenerate From Source, Not From Output

**Also called:** no generational copying, clean-source rule  
**What it is:** Always building a new image from the original references rather than from a previously generated image. Each generation introduces small deviations, and using output as input compounds them.  
**Effect on the audience:** Identity that holds at image forty as well as at image four. Chains built on their own output drift steadily and the drift is invisible until an early image is placed beside a late one.  
**Used for and where it works best:** Every long project, and the single most important habit in this category. It is the reason most generated series lose their characters by the second half. Best in episodic work, campaigns and any library that grows over weeks.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Generated Keyframe Feeding Video, Comics / Webtoon / Photo Essay, Brand Film, Poster / Static Design, 2D Animation (Western / Cartoon), Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: all  
**Avoid when:** It usually costs a needed attribute when a generated image improved on the reference and that improvement is worth keeping. The exception is promoting that output to a new canonical reference deliberately, once, with the decision recorded.  
**Prompt:** `not a prompt line but a rule: every new image is generated from the canonical reference set, never from a previously generated frame, unless that frame has been formally promoted to canonical`  
**Yields to:** `ident.canonical_promotion` — A generated frame improved on the reference.  
`ident.clean_source`

### Canonical Promotion Record

**Also called:** reference versioning, canon update, promoted output  
**What it is:** When a generated image is good enough to become the new reference, promoting it explicitly, recording what it supersedes and why, and from that point using only the new one.  
**Effect on the audience:** Improvement without ambiguity. Without the record the old and new references coexist and the subject flickers between two versions of itself.  
**Used for and where it works best:** Long projects where the reference set improves over time, which is all of them once the work runs past a few weeks. Best in episodic series, campaigns and heritage libraries.  
**Best in:** formats: Character Sheet / Turnaround, General Reference Plate, Location Sheet / Master Plate, Props Sheet, Generated Keyframe Feeding Video, Comics / Webtoon / Photo Essay, Brand Film, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: all  
**Avoid when:** It usually adds ceremony to a very short piece finished in one sitting. The exception is any piece that may have a sequel, where the record is what makes the sequel possible at all.  
**Prompt:** `not a prompt line but a record: this frame replaces the previous facial reference as canonical, dated, with the superseded file retained but marked superseded`  
`ident.canonical_promotion`

### Distinguishing Mark

**Also called:** identity anchor, recognition detail, signature feature  
**What it is:** Giving each recurring subject one specific, describable, unmistakable feature, a scar, a broken tooth, a particular ring or a torn ear, and carrying it in every prompt.  
**Effect on the audience:** Recognition at a glance and at small sizes. General descriptions produce generically similar faces, while one sharp detail does more identity work than five soft ones.  
**Used for and where it works best:** Ensemble pieces where several characters share a physical type, and any work delivered at thumbnail size where fine likeness is lost. Best in social sets, comics and ensemble drama. On a faceless, back-view or silhouette shot (`ai.hidden_faces`) facial marks are dropped from the prompt entirely and identity is carried by the non-facial markers — ring, posture, garment silhouette — because naming a facial scar makes the engine turn the head.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, Thumbnail / Social Card, Comics / Webtoon / Photo Essay, Poster / Static Design, General Reference Plate, Brand Film, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: all  
**Avoid when:** It usually cheapens a subtle character study when the mark is dramatic and unearned. The exception is a quiet mark, a habitual posture or a particular way of holding the hands, which carries the same function without the melodrama.  
**Prompt:** `the pale scar running through the left eyebrow, always present, always on the left`  
**Yields to:** `ai.hidden_faces` — on a faceless, back-view or silhouette shot, where facial marks are dropped from the prompt entirely and the non-facial markers carry the identity.  
`ident.distinguishing_mark`

### Identity Under Age Change

**Also called:** ageing continuity, same-person-across-time  
**What it is:** Holding the structural features that do not change with age, eye spacing, nose bridge, jaw width and ear shape, while allowing the ones that do: skin, hair, weight and posture.  
**Effect on the audience:** A believable same person at two ages, which is otherwise one of the hardest things to generate. Naming which features must hold is what makes it work.  
**Used for and where it works best:** Biography, generational stories, flashback structures and heritage pieces covering a whole life. Best in historical drama, documentary and family sagas. Write the older state as its own standalone frozen sentence (`ident.frozen_sentence`), repeating the structural features verbatim; never use "the same man twenty years older" or any other back-reference, which the Self-Containment Law forbids because the model has no memory of the earlier shot and builds a stranger instead.  
**Best in:** formats: Character Sheet / Turnaround, Generated Keyframe Feeding Video, General Reference Plate, Poster / Static Design, Documentary Feature, Heritage / Historical Documentary, Brand Film, Portrait Photography, Headshot, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Historical / Biopic, Drama, Heritage (civilisation-focused), Family, Tragedy, Verite / Observational  
**Avoid when:** It usually fails across very large age gaps where the structure genuinely does change, particularly child to adult. The exception is casting the two ages as related rather than identical, and letting a distinguishing mark carry the connection.  
**Prompt:** `a man of sixty-two, wide-set eyes, straight narrow nose bridge, square jaw of medium width, ears set close to the head with attached lobes, hair grey and thinning, skin loosened at the neck, shoulders carried lower` (the same structural features written out verbatim as a standalone sentence, never as a reference back to the younger shot)  
**Yields to:** the Self-Containment Law and `ident.frozen_sentence` — always. The older state is written as its own standalone frozen sentence, never as a back-reference to the younger one.  
`ident.age_change`

### Crowd Identity Discipline

**Also called:** background consistency, extras rule  
**What it is:** Deciding deliberately which figures in a crowd are identity-held and which are free, and stating it, so the model does not attempt and fail to keep forty faces consistent.  
**Effect on the audience:** Principal characters who hold while the crowd behaves like a crowd. Attempting to lock everyone produces a field of near-clones, and locking no one loses the principals inside their own scene.  
**Used for and where it works best:** Crowd scenes, processions, battles, markets and any heritage reconstruction with population. The unheld crowd is described by silhouette, posture and action, never by facial detail, because that is what makes crowd faces collapse (`rescue.faces_in_crowd`). Best in heritage documentary, epic sequences and historical drama.  
**Best in:** formats: Generated Keyframe Feeding Video, Heritage / Historical Documentary, Documentary Feature, Poster / Static Design, Brand Film, General Reference Plate, Portrait Photography, Headshot, Character Sheet / Turnaround, Documentary Photography, Wedding Photography, Event Photography, Fine Art Photography, Editorial / Magazine Image | genres: Heritage (civilisation-focused), Historical / Biopic, War, Drama, Verite / Observational, Mythology / Ancient Epic  
**Avoid when:** It usually under-serves a scene where a specific secondary figure must be findable in the crowd. The exception is naming that one figure as held and letting the rest remain free.  
**Prompt:** `two figures are identity-held and carry their locked descriptions; the remaining crowd is unheld, varied in age, build and dress, reading by silhouette, posture and direction rather than by face`  
**Yields to:** `rescue.faces_in_crowd` — Background faces still collapse; resolve the crowd by silhouette or a separately generated plate rather than adding face detail.  
`ident.crowd_discipline`
