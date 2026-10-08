# Retouching and Post-Capture Treatment

13 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Name the Fault Before the Fix

**Also called:** the retouching selector, what is actually wrong with this picture, fault before tool  
**What it is:** The card at the head of the `retouch.` shelf. It asks the three questions this shelf's own cards keep asking — **whose face is it and whose line is it to draw, where does the answer actually live, and is this one image or a set that has to match something** — and hands back a named shortlist for each answer. The axes were read off the shelf's `Avoid when:` lines and the conditions its cards use to send a reader elsewhere. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches the screen. It exists so that a correction was made against a named fault, rather than because a tool was open and the picture could be pushed a little further.  
**Used for and where it works best:** Say what is wrong **before you say what you will do about it**, in one sentence, and then ask the three questions in order. Question one comes first because on this shelf it is the only one whose wrong answer cannot be undone by a better version: everything else here is reversible, and a change to a real person's face is a change to a picture of a person who did not ask for it. Question two is the exit check — most of this shelf's alternatives are not on this shelf. Question three decides how much of the work is worth doing at all.  
**Best in:** formats: all | genres: all  
**Avoid when:** **The fault is in how the picture was made rather than in the picture.** A plate whose key light is wrong, a composite whose element was lit under a light that cannot be reconciled, a building whose tilt was too large to crop back — those leave this shelf entirely, and axis two's second answer is deliberately empty of cards to say so out loud. Also **distrust axis one, because the shelf does**: three of its cards are the only ones here that touch a real person, all three are reached by nothing, and the one card that makes the subject's agreement the deciding line is reached by nothing either. **The map is routing on a question the shelf never routes on**, which is a claim about the shelf and not a report of it, and a reader who disagrees with the sort should back the card.  
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**Axis 1 — Is it a real person's face or skin, and is the line yours to draw?**
The shelf answers this itself, in one card, and the answer is unusually blunt. `retouch.blemish_versus_feature` keeps what is permanent — a scar, a mole, a line — *unless the subject asked otherwise*, and when a commercial brief asks for idealisation it does not yield to another card at all. It yields to **the subject's prior agreement, stated in the brief**, which *turns an ethical question into a specification*. That is a routing condition, not a sentiment: the brief carries the line, and where the brief is silent the card's own default holds (what is permanent stays) and the work carries on. `retouch.skin_tone_protection` is the same axis from the other side — the viewer knows what skin looks like and will accept error everywhere else first — and it too routes out, to the grading shelf, the moment the look wants to move skin deliberately.

**Axis 2 — Where does the answer live: in these pixels, upstream of them, or in how you are working?**
Three of this shelf's `Avoid when:` exceptions and most of its outward pointers say the same thing: the fix is not here. *The plate's key light is wrong, not merely weak* (`retouch.dodge_and_burn`, out to a relight pass). *The element's light cannot be reconciled; generate it into the plate* (`retouch.composite_light_match`). *The tilt is large; a higher camera removes the convergence* (`retouch.perspective_correction`). *Brand colour or a print run; the proof decides, not the screen* (`retouch.calibrated_viewing`). And a third value that is easy to miss: three cards here change nothing in the image at all — they decide whether the other nine stay reversible, judgeable and honest.

**Axis 3 — Is this one image, or a set that has to match something after you finish?**
Four cards state their boundary as a fact about the batch or the delivery rather than about the picture. *It costs time on a large batch — check the first and the last* (`retouch.restraint_check`). *It adds file size on a one-off finished in minutes; the exception is any image that might be reused, which in practice is most of them* (`retouch.non_destructive_chain`). *It feels unnecessary for social-only delivery where every viewer sees something different anyway* (`retouch.calibrated_viewing`). *Halos and banding when the selection is narrow and the image is compressed* (`retouch.selective_colour`). Asked last, because it changes how far you go rather than which card you open.

---

**The map**

**Axis 1 — whose face, and whose line**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A real person, and you are changing what the camera saw of them** (three) | `retouch.blemish_versus_feature` · `retouch.frequency_separation` · `retouch.dodge_and_burn` |
| **A real person, and you are shielding them from a move aimed at the whole frame** (one) | `retouch.skin_tone_protection` |
| **No person, or none that your correction lands on** (five) | `retouch.selective_colour` · `retouch.sharpen_last_and_local` · `retouch.noise_and_grain_discipline` · `retouch.perspective_correction` · `retouch.composite_light_match` |
| **Not about the picture at all** (three) | `retouch.non_destructive_chain` · `retouch.calibrated_viewing` · `retouch.restraint_check` |

**Axis 2 — where the answer lives**

| Answer | The shortlist, by id |
| :--- | :--- |
| **In these pixels — correct it here** (nine) | `retouch.dodge_and_burn` · `retouch.frequency_separation` · `retouch.blemish_versus_feature` · `retouch.selective_colour` · `retouch.skin_tone_protection` · `retouch.sharpen_last_and_local` · `retouch.noise_and_grain_discipline` · `retouch.perspective_correction` · `retouch.composite_light_match` |
| **Upstream — the fault is in how the picture was made, and the shelf hands off** (none) | *No card of this shelf. The exits, by id, are `repair.relight_pass`, `repair.inpaint_region`, `repair.version_and_keep`, `angle.balcony_height`, `color.skin_protection` and `print.proof_before_run`. The value is on the map because an empty answer is information: this shelf's most common alternative is not on it* |
| **In how you are working — so the first answer stays checkable and reversible** (three) | `retouch.non_destructive_chain` · `retouch.calibrated_viewing` · `retouch.restraint_check` |

**Axis 3 — one image, or a set**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One image, seen once, answerable to nothing** (four) | `retouch.dodge_and_burn` · `retouch.frequency_separation` · `retouch.blemish_versus_feature` · `retouch.perspective_correction` |
| **A set that has to match itself** (four) | `retouch.skin_tone_protection` · `retouch.noise_and_grain_discipline` · `retouch.composite_light_match` · `retouch.restraint_check` |
| **A set that has to match something outside it — a brand value, a print, real footage** (three) | `retouch.selective_colour` · `retouch.calibrated_viewing` · `retouch.sharpen_last_and_local` |
| **An image that will be asked for again in another form** (one) | `retouch.non_destructive_chain` |

*A card appears once per axis. The answer is the intersection of the three shortlists, and on this shelf it is normally one or two cards wide.*

---

**The default, and the one against it**

**This shelf has no measured default.** Three edges arrive, at three different cards, each on one condition, and two of the three start outside the shelf: a restoration procedure sending a reader to reversible layers on a one-sitting project, and a packshot card sending one to the restraint check because the product was cleaned until it read as digitally assembled. Nothing here is reached twice for two reasons. **In-degree measures how often a shelf runs out of room, and this shelf almost never does — it runs out of jurisdiction instead**, which is the same finding read off axis two.

**The argued default is `retouch.blemish_versus_feature`, with `retouch.restraint_check` closing every session.** The first is the only card on the shelf that states a *line* rather than a *technique*: it separates what is temporary from what is permanent, and it is the only card here whose pointer is not a card at all but a fact somebody else holds. **A shelf of tools with one card that says where the tools stop should default to that card**, because the tools do not need choosing — each of the other eight is the obvious answer to a fault only it addresses — and the only genuinely open question on the shelf is how far to go. `retouch.restraint_check` is the same question asked at the end instead of the beginning, and its own text applies it to every finished image.

**The stated runner-up, so the ranking is not silent:** `retouch.non_destructive_chain`, which is second because it makes every other answer on the shelf provisional. It is not first only because it decides nothing about the picture; it decides whether a decision about the picture can be taken back.

**The one against it is `retouch.perspective_correction`.** Nothing routes to it, and it is against the grain of its own shelf twice. It is the only card here that changes the **geometry** of a picture rather than its tone, texture or colour — every other card leaves the drawing alone and argues about the surface. And it is the only one whose own exception concedes that the correct answer was to not need the card: *generating or shooting from a higher position removes the convergence rather than correcting it*. A retouching shelf containing one card that says the best retouch is the one that was never required is a shelf with a conscience, and that card is worth choosing on purpose. **Its near cousin is `retouch.calibrated_viewing`**, likewise unreached, and the only card on the shelf that changes nothing in the image whatsoever — it changes the eye, on the argument that a judgement made on an unknown screen is not a judgement.

---

**The unasked**

**Nine of the twelve cards are the target of no pair condition anywhere in the package.** By id:

`retouch.frequency_separation` · `retouch.blemish_versus_feature` · `retouch.selective_colour` · `retouch.skin_tone_protection` · `retouch.sharpen_last_and_local` · `retouch.noise_and_grain_discipline` · `retouch.perspective_correction` · `retouch.composite_light_match` · `retouch.calibrated_viewing`

**And the shape of that list is the finding.** **Every card on this shelf that touches a real person is on it** — the one that shapes a face, the one that smooths skin, the one that decides which marks stay — and so is the one that shields skin from a grade. Nothing in the package sends a reader to any of them. The card that owns the shelf's own deciding line is reached by nobody, and it is the only card here whose pointer leaves the craft entirely and lands on a person.

That explains the thing worth recording rather than arguing about. Two cards on this shelf prescribe changing a real person's face and skin and do not mention that person anywhere: one shapes the form of a face by lightening and darkening it, the other evens the tone of skin across a cheek and forehead. Neither is wrong about its technique and neither is a policy failure. **It is a graph fact: there is no edge in this package that would carry the question from the card that owns it to the cards that need it.** The consent line exists, it is written, it is stated as a route — and the shelf has no way to route to it. **The shelf has already answered its own question and cannot deliver its own answer.** Routing on it is what this card does about that; deciding what the cards should say is the owner's, and the arithmetic below records it for them.

The second thing the list shows: **the whole judging region is unasked.** `retouch.calibrated_viewing`, `retouch.restraint_check` and `retouch.non_destructive_chain` are the three cards about whether you can trust what you are looking at, whether you went too far, and whether you can go back — and two of the three are reached only from other shelves, by readers who had already gone too far. **On a repair shelf, every route in starts at damage.** The card this shelf wants and does not have is the one that says **a retouch has a brief**: a stated list of what this image is allowed to become, agreed before the first correction, against which the restraint check is a comparison rather than an opinion. The nearest thing that exists, `retouch.blemish_versus_feature`, names it exactly once, in its own exception — *agreeing the line with the subject beforehand, which turns an ethical question into a specification* — and nothing routes a reader there to read it.

`retouch.fault_before_fix`

---

### Dodge and Burn

**Also called:** local lightening and darkening, D and B  
**What it is:** Lightening and darkening small areas by hand to shape form, following the light that is already in the image rather than imposing a new one.  
**Effect on the audience:** Form and dimension without a lighting change. It is how a flat face gains structure and how a fabric fold gains depth, and it is invisible when done well.  
**Used for and where it works best:** Portrait and beauty finishing, product work where a surface needs shaping, and any generated image whose lighting is correct but weak. On a real person it models the face that is there and does not reshape it: changing how the face itself reads is a change to the person, so it goes only as far as the brief asks, per `retouch.blemish_versus_feature`; where the brief is silent, the face stays as it is. Best in beauty, portrait and product work.  
**Best in:** formats: Portrait Photography, Beauty Photography, Headshot, Product Still / Packshot, Editorial / Magazine Image, Fashion Photography, Generated Keyframe Feeding Video, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually looks sculpted and artificial when the shaping ignores the direction of the existing key light. The exception is a deliberately graphic treatment where the modelling is meant to be seen, and on a real person the subject has agreed to that treatment.  
**Prompt:** `local lightening along the top of the cheekbone and darkening beneath it, following the existing key from camera left, no new light direction introduced`  
**Yields to:** `repair.relight_pass` — The plate's key light is wrong, not merely weak.  
`retouch.dodge_and_burn`

### Frequency Separation

**Also called:** texture and tone separation, high and low frequency  
**What it is:** Treating texture and tone as two layers so that colour and shading can be evened out without destroying pores, weave or grain.  
**Effect on the audience:** Clean skin and fabric that still has surface. The alternative, blurring, removes the texture that made the image believable in the first place.  
**Used for and where it works best:** Beauty and portrait finishing, fashion, and product work with fabric or skin. On a real person, evening the tone stops at what is permanent — a birthmark, the colour of a scar — which stays unless the subject agreed otherwise, per `retouch.blemish_versus_feature`. Best in beauty and fashion.  
**Best in:** formats: Beauty Photography, Portrait Photography, Fashion Photography, Headshot, Editorial / Magazine Image, Product Still / Packshot, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually produces plastic skin when the tone layer is smoothed too far and the texture layer cannot carry the difference. The exception is a deliberately graphic beauty register where the plastic finish is the style, and on a real person the subject has agreed to it.  
**Prompt:** `even the tone across the cheek and forehead while leaving the pore texture untouched, no blurring of the surface`  
**Yields to:** `retouch.dodge_and_burn` — Even the tone without smoothing texture to plastic.  
`retouch.frequency_separation`

### Remove Blemishes, Keep Features

**Also called:** temporary versus permanent, retouch ethics  
**What it is:** Removing what is temporary, a spot, a stray hair, a crease from clothing, and keeping what is permanent, a scar, a mole, a line, unless the subject asked otherwise.  
**Effect on the audience:** The person stays themselves. Removing permanent features is what makes retouched portraits read as strangers, and it is the commonest complaint from sitters.  
**Used for and where it works best:** All portrait, headshot and editorial work, and any image of a real person. Best in portraits and editorial.  
**Best in:** formats: Portrait Photography, Headshot, Editorial / Magazine Image, Beauty Photography, Documentary Photography, Fashion Photography, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually conflicts with a commercial brief that asks for idealisation. The exception is agreeing the line with the subject beforehand, which turns an ethical question into a specification.  
**Prompt:** `remove the temporary blemish on the left cheek and the stray hair across the brow; keep the scar, the mole and the lines at the eyes exactly as they are`  
**Yields to:** The subject's prior agreement, stated in the brief — A commercial brief asks for idealisation.  
`retouch.blemish_versus_feature`

### Selective Colour Correction

**Also called:** secondary grade, targeted hue shift  
**What it is:** Adjusting one colour range without moving the others, usually to correct a cast in a specific material or to bring a brand colour to its exact value.  
**Effect on the audience:** Precision without collateral damage. Correcting a green cast globally will also move skin, while a targeted correction leaves the face alone.  
**Used for and where it works best:** Product work with brand colours, food where one ingredient reads wrong, and any image with mixed light sources. Best in product and food work.  
**Best in:** formats: Product Still / Packshot, Food Photography, Commercial / TVC, Editorial / Magazine Image, Still Life Photography, Fashion Photography, Generated Keyframe Feeding Video, Portrait Photography, Beauty Photography, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually produces halos and banding when the selection is narrow and the image is compressed. The exception is a generous selection with a soft falloff, which is invisible even on difficult material.  
**Prompt:** `shift only the green range in the glaze toward its correct value, leaving skin, wood and background untouched`  
`retouch.selective_colour`

### Protect the Skin Tones

**Also called:** skin range lock, memory colour  
**What it is:** Excluding skin from any global colour or contrast move, because the viewer knows what skin should look like and will accept error everywhere else first.  
**Effect on the audience:** Faces stay believable through aggressive grading. Skin is a memory colour, and a small error in it is more visible than a large error in anything else.  
**Used for and where it works best:** All portrait, fashion, documentary and heritage work, and any graded sequence with people in it. Best in portraits and any human subject.  
**Best in:** formats: Portrait Photography, Headshot, Fashion Photography, Editorial / Magazine Image, Documentary Photography, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Beauty Photography, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually limits a strong stylised grade that wants to take everything with it. The exception is a grade that moves skin deliberately and by a stated amount, rather than as a side effect.  
**Prompt:** `apply the cool grade to the whole frame except the skin range, which holds its warmth and its original saturation`  
**Yields to:** `color.skin_protection` — A strong stylised look; skin moved deliberately by a stated amount.  
`retouch.skin_tone_protection`

### Sharpen Last, and Only Where It Matters

**Also called:** output sharpening, local sharpening  
**What it is:** Leaving sharpening to the final step, sized for the output, and applying it to the areas that carry the read rather than to the whole frame.  
**Effect on the audience:** Detail where the eye goes and no crunch anywhere else. Global sharpening amplifies noise in skies and shadows, which is where it is least wanted.  
**Used for and where it works best:** Every finished image, and especially anything upscaled or destined for print. Best in print and product work.  
**Best in:** formats: Product Still / Packshot, Poster / Static Design, Editorial / Magazine Image, Portrait Photography, Landscape Photography, Generated Keyframe Feeding Video, Fine Art Photography, Beauty Photography, Fashion Photography, Food Photography, Architectural Photography, Real Estate Photography | genres: all  
**Avoid when:** It usually produces halos along high-contrast edges when applied strongly. The exception is a deliberately crisp graphic register, where the halo reads as style rather than as error.  
**Prompt:** `sharpen the eyes and the fabric edge only, at the final output size, leaving the background and the sky untouched`  
`retouch.sharpen_last_and_local`

### Noise Removal and Grain Restoration

**Also called:** denoise, add grain back  
**What it is:** Removing digital noise and then adding a controlled grain back, because a completely clean image reads as synthetic while raw noise reads as a fault.  
**Effect on the audience:** The image sits in a believable register. Grain is one of the strongest signals that something was photographed rather than generated.  
**Used for and where it works best:** Any generated image intended to read as photographic, all upscaled work, and anything matched to real footage. Best in keyframe plates and heritage work.  
**Best in:** formats: Generated Keyframe Feeding Video, Heritage / Historical Documentary, Portrait Photography, Editorial / Magazine Image, Poster / Static Design, General Reference Plate, Fine Art Photography, Beauty Photography, Fashion Photography, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography | genres: all  
**Avoid when:** It usually reads as a filter when the grain is uniform across the whole frame including the blacks. The exception is grain weighted toward the midtones, which is how film actually behaves.  
**Prompt:** `remove the digital noise, then add a fine film grain weighted to the midtones and absent from the deepest blacks`  
`retouch.noise_and_grain_discipline`

### Correct the Verticals

**Also called:** keystone correction, perspective straightening  
**What it is:** Straightening converging vertical lines so that buildings and interiors stand upright, and deciding deliberately when to leave the convergence in.  
**Effect on the audience:** Architecture that reads as built. Falling verticals are the single most noticeable fault in architectural and interior images.  
**Used for and where it works best:** Architectural, interior and real estate work, and any image with strong built verticals. Best in architecture and interiors.  
**Best in:** formats: Architectural Photography, Interior Photography, Real Estate Photography, Travel Photography, Editorial / Magazine Image, Heritage / Historical Documentary, Generated Keyframe Feeding Video, Portrait Photography, Beauty Photography, Fashion Photography, Food Photography, Landscape Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually crops away too much of the frame when the original tilt was large. The exception is generating or shooting from a higher position, which removes the convergence rather than correcting it.  
**Prompt:** `verticals corrected to true, the building standing upright, the crop planned in advance so the correction does not lose the roofline`  
**Yields to:** `angle.balcony_height` — The tilt is large; a higher camera removes the convergence.  
`retouch.perspective_correction`

### Match the Light When Compositing

**Also called:** element integration, composite discipline  
**What it is:** Making every composited element share the same key direction, quality, colour and contrast as the plate, and giving it the plate's grain and its own contact shadow.  
**Effect on the audience:** The element belongs. Composite failures are almost never about edges; they are about light direction and grain mismatch.  
**Used for and where it works best:** Any assembled image, all outpainted extensions, and every repair large enough to be a composite. Best in keyframe plates and heritage reconstruction.  
**Best in:** formats: Generated Keyframe Feeding Video, Heritage / Historical Documentary, Poster / Static Design, Product Still / Packshot, General Reference Plate, Editorial / Magazine Image, Commercial / TVC, Portrait Photography, Beauty Photography, Fashion Photography, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually fails when the added element was made under light that cannot be reconciled with the plate. The exception is regenerating the element specifically for this plate rather than adapting one that already exists.  
**Prompt:** `the added figure lit from camera left at the same hardness and warmth as the plate, carrying the same grain, with its own contact shadow on the stone`  
**Yields to:** `repair.inpaint_region` — The element's light cannot be reconciled; generate it into the plate.  
`retouch.composite_light_match`

### Keep the Chain Non-Destructive

**Also called:** layered edit, reversible workflow  
**What it is:** Making every adjustment as a separate reversible step over the original rather than baking corrections into the pixels.  
**Effect on the audience:** Any decision can be revisited weeks later, including by someone else. It is also what makes a second delivery ratio or a second stock version cheap instead of a rebuild.  
**Used for and where it works best:** All commissioned work and anything delivered in more than one version. Best in campaigns and print work.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Generated Keyframe Feeding Video, Fine Art Photography, Heritage / Historical Documentary, Portrait Photography, Beauty Photography, Fashion Photography, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography | genres: all  
**Avoid when:** It usually adds file size and complexity on a one-off image finished in minutes. The exception is any image that might be reused, which in practice is most of them.  
**Prompt:** `not a prompt line but a workflow: every correction as its own reversible step, the original untouched beneath`  
**Yields to:** `repair.version_and_keep` — One-off image; keep the accepted states instead of a layer stack.  
`retouch.non_destructive_chain`

### Judge on a Calibrated Screen

**Also called:** monitor calibration, viewing condition  
**What it is:** Making colour and contrast decisions on a profiled display under controlled ambient light, rather than on whatever screen is available.  
**Effect on the audience:** The decisions transfer. Work graded on an uncalibrated screen arrives at the client, the printer and the platform looking like a different image.  
**Used for and where it works best:** All commissioned colour work, print delivery and campaign sets. Best in print and brand work.  
**Best in:** formats: Poster / Static Design, Editorial / Magazine Image, Product Still / Packshot, Commercial / TVC, Fine Art Photography, Props Sheet, Portrait Photography, Beauty Photography, Fashion Photography, Food Photography, Architectural Photography, Landscape Photography, Real Estate Photography | genres: all  
**Avoid when:** It usually feels unnecessary for social-only delivery where every viewer sees something different anyway. The exception is brand colour, which is checked against a specification rather than against a screen.  
**Prompt:** `not a prompt line but a condition: colour judged on a profiled display in controlled ambient light before any delivery`  
**Yields to:** `print.proof_before_run` — Brand colour or a print run; the proof decides, not the screen.  
`retouch.calibrated_viewing`

### The Restraint Check

**Also called:** step back, compare with the original  
**What it is:** Placing the finished version beside the untouched one at full size before delivery, and asking whether each change earned itself.  
**Effect on the audience:** Over-retouching gets caught. Work drifts during a long session and the drift is invisible from inside it, which is how plastic skin and neon food happen.  
**Used for and where it works best:** Every finished image, and especially after a long session on one file. Best across all still work.  
**Best in:** formats: Portrait Photography, Beauty Photography, Food Photography, Product Still / Packshot, Editorial / Magazine Image, Fashion Photography, Generated Keyframe Feeding Video, Architectural Photography, Landscape Photography, Real Estate Photography, Fine Art Photography | genres: all  
**Avoid when:** It usually costs time on a large batch. The exception is checking the first and the last image of the batch, which catches the drift without reviewing everything.  
**Prompt:** `not a prompt line but a step: put the original beside the finished version at full size and justify each change before delivering`  
`retouch.restraint_check`
