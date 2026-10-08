# Medium, Style and Render Register

19 cards. Also in the other stage: a shot has a frame too. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name the Claim Before the Look

**Also called:** the register selector, claim before look, what is this image saying it is  
**What it is:** The card at the head of the `medium.` shelf. It does not describe a surface. It asks the three questions the shelf's own pair graph asks over and over — **what may this image claim about how it came to exist, does the frame need one continuous tonal field, and does a particular face or a precise detail have to survive the surface** — and hands back a named shortlist for each answer. The axes were not invented: they were read off the shelf's own `Yields to:` conditions, and the conditions that repeated became the questions. Every card cited here is cited by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so the register that does reach the screen was chosen against the subject's date and the frame's job, rather than reached for because it is the one the model does best.  
**Used for and where it works best:** Answer the three questions **in order and out loud, one sentence each, before you write the register into the prompt**. This shelf is an exclusive choice set and behaves like one: almost every card here names a situation another card on this shelf owns, so the first answer that is honestly *no* eliminates most of the file and the remaining two questions leave a shortlist of two or three. Answer question one first even when you already know the look you want, because question one is the only one of the three that can be wrong in a way the audience cannot see and a historian can.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The register is already fixed by something upstream — a series bible, a locked look, a plate you are matching, or a client's brand.** There the register is inherited and this map only invites you to relitigate it. Also avoid it on any piece that alternates two registers throughout: this map returns one answer, and an alternation needs two full answers plus a stated rule joining them, which is `medium.register_mixing` and not a shortlist. And **distrust this map on heritage and ancient subjects, which is exactly where it is most often opened.** Its default and its period rule contradict each other in the package as written: the default claims heritage reconstruction as its home ground, and the period rule says a photographic finish on a subject no camera could have seen asserts a witness that never existed. Both sentences are on the shelf and neither was written to lose. On any subject that predates the camera, answer question one with *the date rules* and let `medium.period_appropriate_register` hand the choice back to you — but know that you are choosing a side of an open argument, not reading off a settled one.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — What may this image claim about how it came to exist?**
Asked first, because it is the condition the shelf repeats most and the only one with a cost outside the frame. Six of the shelf's seventeen conditions turn on it: *"The story is openly imagined; photoreal reads as a claim"* (`medium.photographic`), *"The image must be taken as evidence"* (`medium.stylised_cg_handmade`), *"The subject must be believed as real"* (`medium.anime_cel`), *"The story needs one continuous world"* (`medium.collage`), *"The subject predates the process being imitated"* (`medium.era_process`), *"Immediacy needed and the reconstruction is declared"* (`medium.period_appropriate_register`). The `Avoid when:` lines say the same thing from the other side — a photographic finish *"makes the invention look like a claim"*, a period process *"creates a false claim"*, a clay figure *"is honest about being made"*.

**Axis 2 — Does the frame need one continuous tonal field, or may tone be flat, light-only or per-element?**
Four conditions turn on it and all four are statements about what the surface can physically do, not about what a viewer feels: *"The frame must carry weight or threat"* (`medium.watercolour`, whose own reason is that the medium reads as soft), *"Mood depends on gradation and air"* (`medium.ink_line`, because hatching describes surface rather than space), *"The image must carry nuance and atmosphere"* (`medium.flat_vector`, because flatness removes the means), *"The piece must look finished and paid for"* (`medium.charcoal`). Three of those four land on the same card, which is the tell that this is one question and not three.

**Axis 3 — Does a particular face, or a precise detail, have to survive the surface?**
Five conditions: *"The detail must be read precisely"* (`medium.oil_painting`), *"The frame must hold a likeness"* (`medium.woodcut`), *"Fine photographic tone must survive"* (`medium.risograph`), *"A modern emotional close-up must feel present"* (`medium.mosaic_relief`), *"A human subject needs warmth, not perfect surfaces"* (`medium.threed_render`). It is asked last because it only ever narrows: it cannot overturn an answer to question one, and a register that fails it is usually failing it by design.

**Two conditions are leaves and are recorded as such**, not promoted: *"The shot needs scale a miniature cannot carry"* separates one card from one card, and *"Unusual register; one sentence cannot carry it"* is about how long the declaration is, not about which register it declares.

---

**The map**

**Axis 1 — what the image may claim about its own origin**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A record — a camera could have made this, and the piece wants it read as evidence** (two) | `medium.photographic` · `medium.era_process`, and the second only for a subject of the process's own era |
| **A made object — the piece is content to say a hand or a machine made it** (thirteen) | `medium.oil_painting` · `medium.watercolour` · `medium.ink_line` · `medium.woodcut` · `medium.charcoal` · `medium.threed_render` · `medium.stylised_cg_handmade` · `medium.collage` · `medium.flat_vector` · `medium.anime_cel` · `medium.stop_motion` · `medium.risograph` · `medium.mosaic_relief` |
| **The claim is not yours to choose, and none of these is a look** (three) | `medium.period_appropriate_register` — the subject's date decides, and hands you back to a card in one of the two rows above · `medium.register_mixing` — two claims alternating under one rule the viewer can learn in the first two cuts · `medium.material_honesty` — you have already answered, and this governs how the answer is written into the prompt |

*The third row is a governor, not a fork. Nothing in it is an alternative to anything in the first two rows: each one tells you how to hold, date or break whichever register the other two axes return. That is why they take no answer on axis two or axis three.*

**Axis 2 — does the frame need one continuous tonal field**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Yes — it must reach black, hold air and gradate across the whole frame** (eight) | `medium.photographic` · `medium.era_process` · `medium.oil_painting` · `medium.charcoal` · `medium.threed_render` · `medium.stylised_cg_handmade` · `medium.stop_motion` · `medium.mosaic_relief` |
| **No — the register is flat, light-only, or tonal only inside each element** (seven) | `medium.watercolour` · `medium.ink_line` · `medium.woodcut` · `medium.flat_vector` · `medium.anime_cel` · `medium.risograph` · `medium.collage` |

**Axis 3 — does a particular face or a precise detail have to survive**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A named person, and the viewer must recognise them** (four) | `medium.photographic` · `medium.era_process` · `medium.charcoal` · `medium.oil_painting` |
| **A figure, deliberately not a real person** (six) | `medium.stylised_cg_handmade` · `medium.anime_cel` · `medium.stop_motion` · `medium.watercolour` · `medium.flat_vector` · `medium.threed_render` |
| **No face that has to be read — the shape, the seam or the cut surface is the subject** (five) | `medium.ink_line` · `medium.woodcut` · `medium.mosaic_relief` · `medium.risograph` · `medium.collage` |

*A look card appears once per axis and the answer is the intersection of the three shortlists, normally two or three cards wide. The three governors appear on axis one only, and they apply on top of whatever the intersection returns.*

*`medium.oil_painting` is filed under a named person because it can hold a likeness, but it paints an imagined figure just as well: it is the card other looks yield to when the story is openly imagined. A painted look for a fictional figure takes it from axes one and two, whatever axis three returned.*

---

**The default, and the one against it**

**The default is `medium.photographic`, and it is measured rather than asserted.** Six cards on this shelf send a reader to it — `medium.stylised_cg_handmade` (*"The image must be taken as evidence"*), `medium.anime_cel` (*"The subject must be believed as real"*), `medium.collage` (*"The story needs one continuous world"*), `medium.risograph` (*"Fine photographic tone must survive"*), `medium.mosaic_relief` (*"A modern emotional close-up must feel present"*) and `medium.period_appropriate_register` (*"Immediacy needed and the reconstruction is declared"*). That survives the test the in-degree alone would fail: the six edges fire on **four** distinct conditions — believability, world continuity, tonal fidelity, present-tense immediacy — so this is a shelf falling back, not a shelf running out of room through one door. Nothing else here is named more than three times, and the only card named three times, `medium.charcoal`, is named three times for three different reasons and is therefore the drawn side's own default: reach for it whenever axis one says *made* and axis two says *yes*.

**And the default is where the shelf contradicts itself, which is recorded here rather than resolved.** `medium.photographic` claims documentary and heritage reconstruction as its home ground, and `medium.era_process` claims historical drama, archive reconstruction and ancient-facing heritage work — while `medium.period_appropriate_register` says in plain words that a photoreal image of an event three thousand years old asserts a witness that never existed, and `medium.era_process` says in its own `Avoid when:` that imitating a process on a subject that predates it creates a false claim. Two cards claim the ground the third forbids. **Nothing on this shelf settles it and this card does not pretend to**: on a pre-camera subject, answer axis one with *the claim is not yours to choose*, and take the return from `medium.period_appropriate_register` knowing it is one side of an argument the package has not closed.

**The one against it is `medium.mosaic_relief`.** Nothing on the shelf routes to it; it yields outward to `medium.photographic` and nothing yields inward. Every other register here is a way of **depicting** a subject; this one makes the image **be an artefact** — tesserae, cut stone, moulded brick, raking light revealing the cut depth — so the frame is no longer a picture of the thing but a thing of the same kind as the thing. On the heritage work this package exists to serve, that is the one register on the shelf which cannot make a false witness claim at all, because a carved relief has never once been mistaken for a photograph. It is against the grain in the exact place the default is weakest. Its cost is stated and payable: it cannot carry a modern emotional close-up, so it takes the wide, the object and the ceremonial and hands the face back. Its cousin against the grain is `medium.woodcut`, likewise never yielded to, likewise refusing a likeness, and likewise printing rather than depicting.

---

**The unasked**

**Eleven of the eighteen cards are the target of no `Yields to:` field anywhere in the package.** They can be chosen but nothing ever sends you to them. By id:

`medium.woodcut` · `medium.threed_render` · `medium.collage` · `medium.flat_vector` · `medium.anime_cel` · `medium.stop_motion` · `medium.risograph` · `medium.mosaic_relief` · `medium.era_process` · `medium.material_honesty` · `medium.register_mixing`

**And the shape of that list is the finding, not its length. The pair graph on this shelf is a one-way valve, and it runs out of flat and into tone.** Take axis two's second row — the seven registers with no continuous tonal field. Five of the seven are on the unasked list, and the two that are not, `medium.watercolour` and `medium.ink_line`, are each reached exactly once, from inside the flat block itself: `medium.flat_vector` sends you to watercolour, and that is the only inbound edge watercolour has. Of the shelf's seventeen edges, **exactly one crosses from the tonal side into the flat side** — `medium.oil_painting` to `medium.ink_line` — and its condition is not about tone at all, it is *"The detail must be read precisely"*. So a reader who has answered *yes, one continuous tonal field* will never once be told by this shelf that the flat answer exists. **A flat register is not a degraded tonal one, and the pair field cannot say so**: the seventeen readers who wrote these fields were each comparing two surfaces holding the same subject, and a woodcut and a photograph are not two surfaces holding the same subject.

The second thing the list shows: **the whole made-object block is entered and never arrived at.** `medium.threed_render` and `medium.stop_motion` both yield into `medium.stylised_cg_handmade` and nothing yields into either of them, so the handmade family has one door and two rooms the shelf never sends anybody to. And `medium.era_process` is unasked, which is the sharpest item on the list — nothing anywhere says *the subject is of that era, so use that era's process*, so the only card that can date an image by its chemistry can only ever be reached by someone who already knew it was there. The card the shelf wants and does not have is the one that would route into it: **a register whose reconstruction is declared inside the frame rather than in the caption.** `medium.period_appropriate_register` is the closest thing that exists, and its own prompt puts the declaration *in the caption* — outside the picture, where every phase downstream of this one drops it.

`medium.claim_before_look`

---

### Photographic Register

**Also called:** photoreal, camera-made look, lens register  
**What it is:** Asking for an image that behaves like a photograph: a real focal length, a real aperture, sensor or film grain, and the small imperfections a camera leaves. The register is declared once and the rest of the prompt describes the scene, not the medium.  
**Effect on the audience:** The viewer reads the image as evidence rather than as illustration. Believability comes from the optical behaviour, not from detail count.  
**Used for and where it works best:** Documentary, heritage reconstruction that is declared as a reconstruction — before the camera existed, a photographic finish presented as a record is what `medium.period_appropriate_register` rules out — product and editorial work, anything presented as a record, and every keyframe intended to feed video that must match photographed material. Best in documentary, editorial and brand work.  
**Best in:** formats: Generated Keyframe Feeding Video, Editorial / Magazine Image, Product Still / Packshot, Heritage / Historical Documentary, Poster / Static Design, Commercial / TVC, General Reference Plate, Travel / Real Estate / Hospitality, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: all  
**Avoid when:** It usually fights a story that is openly imagined, where photographic finish makes the invention look like a claim. The exception is deliberate false documentary, where the tension between real look and unreal content is the point.  
**Prompt:** `photographic register, 50mm, f2.8, fine sensor grain, natural falloff at the edges, no illustration or painted finish`  
**Yields to:** `medium.oil_painting` — The story is openly imagined; photoreal reads as a claim.  
`medium.photographic`

### Oil Painting Register

**Also called:** painterly, impasto, classical painting look  
**What it is:** Visible brush loading, edge softness that varies with the stroke, and colour mixed on the surface rather than rendered. The named tradition, Dutch, Venetian or academic, sets the palette and the light behaviour.  
**Effect on the audience:** The image reads as made by a hand across time rather than caught in an instant. It invites contemplation and moves the subject out of the present.  
**Used for and where it works best:** Heritage and mythological work where no photograph could exist, title sequences, book and album covers, and any piece that wants the authority of the museum. Best in posters, covers and heritage documentary.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Comics / Webtoon / Photo Essay, Heritage / Historical Documentary, Title Sequence / Opening Credits, Brand Film, Thumbnail / Social Card, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Heritage (civilisation-focused), Mythology / Ancient Epic, Historical / Biopic, Fantasy / Epic, Tragedy, Faith / Biblical Epic, Gothic / Vampire  
**Avoid when:** It usually loses information when the subject needs to be read precisely, because painterly edges soften the very details a viewer is being asked to examine. The exception is a deliberate contrast where one element stays sharp inside a painted field.  
**Prompt:** `oil painting register, visible brush loading in the highlights, soft blended shadow edges, warm earth palette, canvas tooth showing through the thinnest passages`  
**Yields to:** `medium.ink_line` — The detail must be read precisely.  
`medium.oil_painting`

### Watercolour Register

**Also called:** aquarelle, wash, transparent watercolour  
**What it is:** Transparent layered washes on paper, with the white of the paper doing the lighting, hard blooms where wet meets dry, and pigment settling into the grain.  
**Effect on the audience:** Lightness and impermanence. The viewer feels the image could still change, which reads as memory, childhood or gentleness.  
**Used for and where it works best:** Children content, storybook and educational work, gentle travel and food pieces, and any sequence that wants to feel handmade rather than produced. Best in kids content, comics and editorial illustration.  
**Best in:** formats: Kids Content, Comics / Webtoon / Photo Essay, Editorial / Magazine Image, Poster / Static Design, Thumbnail / Social Card, Explainer, 2D Animation (Western / Cartoon), Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Family, Preschool / Early Learning, Fairy Tale, Slice of Life, Romance, Comedy, Nature / Wildlife  
**Avoid when:** It usually cannot carry weight or threat, because the medium itself reads as soft. The exception is using that softness against the content, where a gentle medium makes a hard subject land harder.  
**Prompt:** `watercolour register, transparent layered washes, the paper white carrying the highlights, a hard bloom where two wet areas met, pigment settled into the paper grain`  
**Yields to:** `medium.charcoal` — The frame must carry weight or threat.  
`medium.watercolour`

### Ink Line and Hatching

**Also called:** pen and ink, line art, crosshatch  
**What it is:** Form built from line weight and hatching density rather than from tone, with black ink on a light ground and no continuous greys except those made by the lines themselves.  
**Effect on the audience:** Clarity and graphic force. The eye reads structure immediately and the image survives reproduction at any size, including very small.  
**Used for and where it works best:** Comics and webtoon, technical and explanatory work, editorial illustration, and any image that must stay legible printed small or on a poor screen. Best in comics, explainers and editorial.  
**Best in:** formats: Comics / Webtoon / Photo Essay, Editorial / Magazine Image, Explainer, Poster / Static Design, Thumbnail / Social Card, Kids Content, 2D Animation (Western / Cartoon), Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: all  
**Avoid when:** It usually loses atmosphere where mood depends on gradation and air, because hatching describes surface rather than space. The exception is heavy black spotting used as shadow mass, which restores weight without adding tone.  
**Prompt:** `ink line register, confident varied line weight, crosshatched shadow, no grey tone, pure black on warm paper white`  
**Yields to:** `medium.charcoal` — Mood depends on gradation and air.  
`medium.ink_line`

### Woodcut and Relief Print

**Also called:** linocut, block print, relief carving  
**What it is:** High-contrast shapes cut from a block, with the cut marks visible, no halftone, and an ink coverage that is either full or absent.  
**Effect on the audience:** Force and antiquity. The image feels struck rather than drawn, and it carries the authority of something printed before printing was easy.  
**Used for and where it works best:** Heritage and folk work, festival and protest posters, title cards, and any piece that wants an old printed voice. Best in posters, titles and heritage pieces.  
**Best in:** formats: Poster / Static Design, Title Sequence / Opening Credits, Comics / Webtoon / Photo Essay, Editorial / Magazine Image, Thumbnail / Social Card, Heritage / Historical Documentary, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Folk Horror, Fairy Tale, War, Faith / Biblical Epic  
**Avoid when:** It usually cannot hold a likeness, because the medium simplifies faces into shapes. The exception is a subject already known by silhouette, where the simplification reads as iconography rather than as loss.  
**Prompt:** `woodcut register, bold carved shapes, visible gouge marks, pure black ink on cream paper, no halftone, no grey`  
**Yields to:** `medium.charcoal` — The frame must hold a likeness.  
`medium.woodcut`

### Charcoal and Dry Media

**Also called:** conte, graphite, dry drawing  
**What it is:** Tone built by rubbing and erasing rather than by brush or line, with a granular surface, smudged transitions and highlights lifted out rather than painted in.  
**Effect on the audience:** Weight and unfinished feeling. The image reads as a study, which brings the viewer closer to the process and further from the product.  
**Used for and where it works best:** Storyboards and concept plates, mourning and memory sequences, and portrait work that wants gravity without colour. Best in storyboard frames, editorial and heritage work.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Comics / Webtoon / Photo Essay, Heritage / Historical Documentary, Generated Keyframe Feeding Video, General Reference Plate, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Tragedy, Drama, Historical / Biopic, Heritage (civilisation-focused), Gothic / Vampire, War, Psychological / Arthouse  
**Avoid when:** It usually reads as provisional when the piece needs to look finished and paid for. The exception is a deliberate contrast where the rough register signals a memory or a plan inside an otherwise finished work.  
**Prompt:** `charcoal register, granular tone rubbed into the paper, smudged transitions, highlights lifted with an eraser, deep velvet blacks`  
**Yields to:** `medium.oil_painting` — The piece must look finished and paid for.  
`medium.charcoal`

### 3D Render Register

**Also called:** CG render, offline render, path-traced look  
**What it is:** Surfaces described as materials with roughness, metalness and subsurface behaviour, lit by named sources, with the clean geometry and perfect falloff that render engines produce.  
**Effect on the audience:** Precision and manufacture. The viewer reads the object as designed rather than found, which is exactly right for products and wrong for people.  
**Used for and where it works best:** Product and packaging work, architectural and archaeological reconstruction where geometry must be exact, and title design. Best in product stills, explainers and brand work.  
**Best in:** formats: Product Still / Packshot, Poster / Static Design, Explainer, Commercial / TVC, Title Sequence / Opening Credits, Brand Film, 3D CG Animation, Heritage / Historical Documentary, Fine Art Photography, Editorial / Magazine Image, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography | genres: Science / Educational, Sci-Fi, Heritage (civilisation-focused), Historical / Biopic, Verite / Observational  
**Avoid when:** It usually reads as cold on human subjects, because perfect surfaces remove the small asymmetries a face needs. The exception is when that coldness is the subject, in synthetic or clinical work.  
**Prompt:** `3D render register, physically based materials, roughness and metalness described per surface, single key area light with a soft fill, clean geometry, no camera grain`  
**Yields to:** `medium.stylised_cg_handmade` — A human subject needs warmth, not perfect surfaces.  
`medium.threed_render`

### Stylised CG With a Handmade Surface

**Also called:** clay render, fake stop-motion, digital puppet, felt and fabric CG  
**What it is:** **Rendered in 3D but made of something a hand touched** — clay with thumb-marks, felt with visible fibre, knitted wool, painted wood, plasticine. It is neither of the two registers either side of it: it has a virtual camera and real geometry like `medium.threed_render`, and the tactile, imperfect surface of `medium.stop_motion`, and the whole effect lives in holding both at once. This is a distinct register and not a variant, because the two halves pull in opposite directions and the default pulls one way on its own.  
**Effect on the audience:** Warmth without documentary weight. A clay figure can say something a photographed person cannot — it is plainly a made object, so a modern voice coming out of an ancient subject reads as a device rather than as a claim, and a child watches it without being frightened by it.  
**Used for and where it works best:** Museum and heritage explainers with a recurring character, children's work, a talking presenter who must not be mistaken for a reconstruction of a real person, and any subject where photoreal would be either impossible or tasteless. Two things decide whether it works. **State the material and its imperfections explicitly and early** — *matte unglazed clay, visible thumb-marks and tool drag, one small crack at the shoulder* — because a render engine's idea of a surface with no instruction is smooth plastic with a glossy highlight. And **keep the optics**: this register has a camera, so focal length, aperture and Kelvin all apply, exactly as they do on any other 3D work.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Kids Content, Explainer, Museum Installation, Heritage / Historical Documentary, Brand Film, Animated Series, 3D CG Animation | genres: Children's, Educational, Heritage (civilisation-focused), Comedy, Science / Educational  
**Avoid when:** The piece needs to be believed as evidence. A clay reconstruction is honest about being made, which is a virtue everywhere except where the audience must take the image as a record. Also avoid mixing it with photoreal inserts unless the cut between them is the point — see `medium.register_mixing`.  
**Prompt:** `stylised clay-render character, matte unglazed surface with visible thumb-marks and tool drag, slight asymmetry, soft area key with a warm bounce, shot on a 50mm equivalent at f/4, no glossy plastic sheen and no film grain`  
**Yields to:** `medium.photographic` — The image must be taken as evidence.  
`medium.stylised_cg_handmade`

> **Its negative block is not the standard one.** Take the 3D branch of Tier 1 in [`how-to-write-an-image-prompt.md`](how-to-write-an-image-prompt.md): it keeps the anatomy tokens, keeps `CGI 3D sheen` and adds the shader tokens, and drops only `plastic skin` and `wax figure` — those two describe a *human face* going waxy, which on a clay figure names the wrong fault. **`CGI 3D sheen` stays.** It does not mean "looks computer-made", it means "has the glossy CG sheen", and suppressing that sheen is the whole job here — this card's own prompt line ends `no glossy plastic sheen` for exactly that reason.

### Collage and Cut Paper

**Also called:** cutout, montage, paper assembly  
**What it is:** Elements with visible edges assembled on a surface, each carrying its own texture and lighting, with the seams left rather than blended.  
**Effect on the audience:** The viewer sees construction. Meaning comes from the juxtaposition, and the honesty of the seams makes the argument feel made rather than found.  
**Used for and where it works best:** Essay and editorial work, protest and campaign pieces, title sequences, and children content where the handmade quality is the appeal. Best in editorial, titles and kids work.  
**Best in:** formats: Editorial / Magazine Image, Poster / Static Design, Title Sequence / Opening Credits, Kids Content, Comics / Webtoon / Photo Essay, Explainer, Thumbnail / Social Card, 2D Animation (Western / Cartoon), Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: all  
**Avoid when:** It usually fragments a story that needs one continuous world. The exception is when the fragmentation is the argument, in work about memory, evidence or contested history.  
**Prompt:** `cut paper collage register, torn and cut edges visible, each element carrying its own paper texture and its own light, assembled on a flat ground, seams left unblended`  
**Yields to:** `medium.photographic` — The story needs one continuous world.  
`medium.collage`

### Flat Vector Register

**Also called:** flat design, geometric illustration, vector art  
**What it is:** Solid fills, limited palette, geometric simplification and no gradients or texture, with meaning carried by shape and colour relationship alone.  
**Effect on the audience:** Instant reading at any size. The viewer understands the image before examining it, which is why it dominates interface and explanatory work.  
**Used for and where it works best:** Explainers, interface and product illustration, social cards and thumbnails, and educational content for young children. Best in explainers, thumbnails and kids content.  
**Best in:** formats: Explainer, Thumbnail / Social Card, Poster / Static Design, Kids Content, Editorial / Magazine Image, Corporate / Training, Commercial / TVC, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Science / Educational, Preschool / Early Learning, Family, Comedy, Slice of Life  
**Avoid when:** It usually cannot carry nuance or atmosphere, because flatness removes the means. The exception is a single textured or photographic element placed inside the flat field, which becomes the focus by contrast.  
**Prompt:** `flat vector register, solid fills only, four-colour palette, geometric simplification, no gradients, no texture, no outline`  
**Yields to:** `medium.watercolour` — The image must carry nuance and atmosphere.  
`medium.flat_vector`

### Anime Cel Register

**Also called:** cel shading, 2D animation look, hand-painted cel  
**What it is:** Flat colour areas separated by a drawn line, with shadow as a second flat shape rather than a gradient, and backgrounds painted more softly than the figures.  
**Effect on the audience:** Figures read as drawn characters against a place, which is the grammar an audience already knows from animation. Emotion is carried by line and shape rather than by rendering.  
**Used for and where it works best:** Anime and 2D animation work, kids content, music video, and any project whose audience reads that visual language natively. Best in anime, kids content and music video.  
**Best in:** formats: Anime (Japanese 2D), 2D Animation (Western / Cartoon), Kids Content, Music Video, Poster / Static Design, Thumbnail / Social Card, Comics / Webtoon / Photo Essay, Generated Keyframe Feeding Video, Fine Art Photography, Editorial / Magazine Image, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography | genres: Shonen Battle (anime), Shojo (anime romance), Isekai (anime), Magical Girl (anime), Mecha (anime), Sports Anime, Seinen (mature anime), Family, Fairy Tale  
**Avoid when:** It usually loses documentary weight where the subject needs to be believed as real. The exception is animated documentary, where the drawn register protects an identity or reconstructs what no camera recorded.  
**Prompt:** `anime cel register, flat colour fills with a clean drawn line, shadow as a second flat shape, softly painted background behind sharply drawn figures`  
**Yields to:** `medium.photographic` — The subject must be believed as real.  
`medium.anime_cel`

### Stop Motion and Handmade Object

**Also called:** puppet look, claymation, tabletop miniature  
**What it is:** Real materials photographed under real light, with fingerprints, seams, fabric weave and the slight imperfection of objects made by hand.  
**Effect on the audience:** Tactility. The viewer believes the thing exists and could be picked up, which produces a warmth that neither photography nor rendering reaches.  
**Used for and where it works best:** Children content, craft and food work, title sequences, and any piece that wants charm and evidence of labour. Best in kids content, titles and brand films.  
**Best in:** formats: Kids Content, Title Sequence / Opening Credits, Commercial / TVC, Brand Film, Poster / Static Design, Thumbnail / Social Card, Stop Motion, Fine Art Photography, Editorial / Magazine Image, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Family, Preschool / Early Learning, Fairy Tale, Comedy, Slice of Life, Fantasy / Epic  
**Avoid when:** It usually undercuts scale and threat, because the eye reads the miniature. The exception is horror that uses the miniature deliberately, where the doll quality becomes unsettling instead of charming.  
**Prompt:** `stop motion register, felt and wire puppet under real tungsten light, visible fabric weave and seam, slight fingerprints in the clay, shallow tabletop depth of field`  
**Yields to:** `medium.stylised_cg_handmade` — The shot needs scale a miniature cannot carry.  
`medium.stop_motion`

### Risograph and Limited Print

**Also called:** riso, spot colour print, screen print  
**What it is:** Two or three spot inks printed in separate passes, with visible misregistration, coarse halftone dots and colours that overlay rather than blend.  
**Effect on the audience:** A printed object rather than a screen image. The imperfection signals independence and craft, and the limited palette forces graphic decisions.  
**Used for and where it works best:** Posters, zines and editorial covers, music and event work, and any piece that wants to look printed in a small run. Best in posters, editorial and music work.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Comics / Webtoon / Photo Essay, Thumbnail / Social Card, Music Video, Title Sequence / Opening Credits, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: all  
**Avoid when:** It usually corrupts photographic detail, because the coarse screen destroys fine tone. The exception is a portrait deliberately reduced to two inks, where the loss becomes the style.  
**Prompt:** `risograph register, two spot inks printed in separate passes, visible misregistration at the edges, coarse halftone dots, colours overlaying into a third where they cross`  
**Yields to:** `medium.photographic` — Fine photographic tone must survive.  
`medium.risograph`

### Mosaic, Relief and Carved Surface

**Also called:** tessera, bas relief, carved stone register  
**What it is:** The image built from a physical craft surface, cut stone tesserae, carved relief or moulded brick, with the material grid and the raking light that reveals depth.  
**Effect on the audience:** Permanence and ceremony. The subject is presented the way civilisations presented their own subjects, which makes any content read as commemorated.  
**Used for and where it works best:** Heritage and mythological work, museum and exhibition pieces, title sequences for historical projects, and any image standing in for an artefact. Best in heritage documentary, exhibition and titles.  
**Best in:** formats: Heritage / Historical Documentary, Poster / Static Design, Title Sequence / Opening Credits, Editorial / Magazine Image, Multi-Screen Installation, Thumbnail / Social Card, Product Still / Packshot, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, War, Tragedy  
**Avoid when:** It usually cannot carry a modern emotional close-up, because the craft surface holds the viewer at the distance of an object. The exception is an intentional distancing, where the subject is meant to be read as already historical.  
**Prompt:** `carved stone relief register, shallow bas relief in limestone, hard raking light from the left revealing the cut depth, chisel marks visible, no colour beyond the stone`  
**Yields to:** `medium.photographic` — A modern emotional close-up must feel present.  
`medium.mosaic_relief`

### Register Mixing With Intent

**Also called:** mixed media, deliberate medium break, hybrid register  
**What it is:** Holding one register for the body of the work and breaking to another for a declared reason, with the break named rather than drifting.  
**Effect on the audience:** The medium itself becomes a signal. A single painted frame inside a photographic sequence marks that moment as memory, imagination or myth without a word of explanation.  
**Used for and where it works best:** Documentary that reconstructs what was not filmed, drama with memory or dream layers, and educational work separating fact from model. Best in documentary, heritage work and essays.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Video Essay, Brand Film, Comics / Webtoon / Photo Essay, Poster / Static Design, Generated Keyframe Feeding Video, Fine Art Photography, Editorial / Magazine Image, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Verite / Observational, Heritage (civilisation-focused), Historical / Biopic, Drama, Psychological / Arthouse, Magical Realism, Science / Educational  
**Avoid when:** It usually reads as inconsistency when the break has no rule the viewer can learn. The exception is a break used exactly once, where the singularity itself declares the intent.  

**When the two registers alternate throughout, this card changes shape.** Everything above describes
the *single break* — one painted frame inside a photographic film. A piece built on a repeated cut
between two registers is a different construction, and it is common: a reconstruction documentary
that alternates site footage with drawn rebuilds, a biography that cuts between interview and
animated memory, an explainer that leaves the real world for a diagram and comes back. Four things
govern it.

- **The alternation needs one rule, stated once, that the viewer can learn in the first two cuts.**
  Photographed = what survives, drawn = what is gone. Photographed = now, drawn = then. Whatever it
  is, it must hold for the whole film: the moment one drawn sequence means something different from
  the others, the audience stops reading the medium as a signal and starts reading it as budget.
- **Neither register is the exception.** On a single break, one register is the body of the work and
  the other is the departure, which is why the guidance above is written as *hold and break*. In an
  alternation both are the body, so both get full design attention — its own lighting logic, its own
  palette discipline, its own negative block — and the second one is not treated as an insert.
- **Design the joint, not just the two sides.** The cut between registers is the film's argument, so
  decide how it is made and keep it consistent: a hard cut, a match on a shape or a movement that
  crosses the change, a dissolve where one becomes the other. A match cut across the registers is
  the strongest version and it has to be planned in both sequences at once, from the shot list.
- **Every downstream field answers per sequence.** The optical values, the depth cue, the surface
  description and Tiers 1 and 2 of the negative block all differ by register, so a piece like this
  declares its looks at the top of the shot table and tags every row — the **Mode & Look** cell in
  the Phase 3 table, the **MODE** cell on the storyboard panel, and `render_mode` on each prompt in
  the Phase 7 output contract. Without those tags the alternation is a fact in the writer's head, and
  every phase after this one has to guess it again.

*(The render-mode set and its definitions are owned by [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md).)*

**Prompt:** `the sequence holds a photographic register; this single frame is painted, marking it as remembered rather than witnessed`  
`medium.register_mixing`

### Historical Photographic Process

**Also called:** wet plate, daguerreotype, orthochromatic look  
**What it is:** Reproducing the behaviour of an early photographic process: its colour sensitivity, its exposure length, its plate edges and its characteristic failures.  
**Effect on the audience:** The image dates itself. The viewer places the subject in a period before being told, and the process failures read as authenticity rather than as error.  
**Used for and where it works best:** Historical drama and documentary, archive reconstruction, and portrait work that wants the weight of an early photograph. Best in heritage documentary, posters and editorial.  
**Best in:** formats: Heritage / Historical Documentary, Poster / Static Design, Editorial / Magazine Image, Documentary Feature, General Reference Plate, Generated Keyframe Feeding Video, Thumbnail / Social Card, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Historical / Biopic, Heritage (civilisation-focused), Gothic / Vampire, Tragedy, Drama, Verite / Observational, War  
**Avoid when:** It usually creates a false claim when it is applied to a subject that could not have been photographed in that era, and the viewer reads it as a real archive image. The exception is when the work openly declares the reconstruction.  
**Prompt:** `wet plate collodion register, orthochromatic response with dark skies and pale skin, long exposure stillness, plate edge irregularity and chemical streaks at the borders`  
**Yields to:** `medium.period_appropriate_register` — The subject predates the process being imitated.  
`medium.era_process`

### Name the Medium Once, Then Stop

**Also called:** register discipline, single declaration  
**What it is:** Declaring the register in one clear statement, in Slot 7 where the seven-slot order of how-to-write-an-image-prompt.md puts it, and then describing only the scene, instead of repeating medium words through every clause.  
**Effect on the audience:** Stronger adherence and a cleaner image. Repeating the medium through the prompt makes the model produce a picture about the medium rather than a picture in it.  
**Used for and where it works best:** Every generation with a declared register, and the usual fix when an illustrated prompt returns something that looks like an advertisement for paint. Best across all still work.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Editorial / Magazine Image, Comics / Webtoon / Photo Essay, Thumbnail / Social Card, General Reference Plate, Commercial / TVC, Product Still / Packshot, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: all  
**Avoid when:** It usually under-specifies when a register is unusual enough that one sentence cannot carry it. The exception is adding a second short declaration at the head rather than sprinkling medium words through the description.  
**Prompt:** `A woman stands at a shuttered window, morning light across her hands, the room behind her in shadow. Oil painting register.`  
**Yields to:** `medium.stylised_cg_handmade` — Unusual register; one sentence cannot carry it.  
`medium.material_honesty`

### Register Chosen by Period Logic

**Also called:** medium as evidence, period-truthful register  
**What it is:** Choosing the register from what could plausibly have recorded the subject: a painted register for anything before photography, a process register for its own era, and a photographic register only for what a camera could have seen.  
**Effect on the audience:** The image stops making a false claim. A photoreal image of an event from three thousand years ago quietly asserts a witness that never existed.  
**Used for and where it works best:** Heritage and ancient-history work, religious and mythological subjects, and educational content where the difference between evidence and reconstruction matters. Best in heritage documentary and museum work.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Poster / Static Design, Editorial / Magazine Image, Explainer, Multi-Screen Installation, Generated Keyframe Feeding Video, Fine Art Photography, Portrait Photography, Abstract Photography, Landscape Photography, Travel Photography, Documentary Photography, Still Life Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Faith / Biblical Epic, Science / Educational, Verite / Observational  
**Avoid when:** It usually costs immediacy, since a painted register holds the viewer further away than a photograph would. The exception is a declared reconstruction, where a photoreal image is labelled as a model rather than presented as a record.  
**Prompt:** `painted register rather than photographic, because no camera existed at this date; the reconstruction is declared in the caption rather than disguised by the finish`  
**Yields to:** `medium.photographic` — Immediacy needed and the reconstruction is declared.  
`medium.period_appropriate_register`
