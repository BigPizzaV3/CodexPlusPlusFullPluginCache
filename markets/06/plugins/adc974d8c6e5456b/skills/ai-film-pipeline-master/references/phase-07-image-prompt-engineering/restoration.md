# Correction, Restoration and Extension

10 cards. These decide a frame: what is in it, how it is lit, and what it is made of.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.

---

### Inpaint a Region

**Also called:** masked regeneration, local fix, region repair  
**What it is:** Masking one area of a finished image and regenerating only that area, with a prompt describing what should be there, leaving everything outside the mask untouched.  
**Effect on the audience:** A single fault is corrected without losing the image. Regenerating the whole frame to fix one hand throws away everything that was already right.  
**Used for and where it works best:** Fixing hands, faces, objects and small continuity errors in an otherwise finished plate, and the standard route once an image is ninety percent correct. Best in keyframe plates, product stills and posters.  
**Best in:** formats: Generated Keyframe Feeding Video, Product Still / Packshot, Poster / Static Design, General Reference Plate, Character Sheet / Turnaround, Editorial / Magazine Image, Thumbnail / Social Card, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually leaves a visible seam when the masked region needs lighting that the surrounding area does not provide. The exception is masking generously, including some of the correct surroundings so the repair has context to match.  
**Prompt:** `mask the right hand and its immediate surroundings only, regenerate with the fingers wrapped around the staff, match the existing light direction and skin tone exactly`  
**Yields to:** `repair.relight_pass` — The masked region needs light the plate cannot supply.  
`repair.inpaint_region`

### Outpaint and Extend the Frame

**Also called:** uncrop, canvas extension, frame widening  
**What it is:** Growing the canvas beyond the original edges and generating the new area so it continues the existing scene, perspective and light.  
**Effect on the audience:** A ratio change without a crop. A 16:9 plate becomes a 9:16 keyframe with the subject intact rather than cut in half.  
**Used for and where it works best:** Converting a delivered image to another ratio, adding motion headroom to a frame that has none, and recovering a composition shot too tight. Best in keyframe plates and social delivery.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Thumbnail / Social Card, Vertical Short-Form (Reels, Shorts, TikTok), General Reference Plate, Editorial / Magazine Image, Commercial / TVC, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually invents architecture that does not follow the original perspective when the extension is large. The exception is extending in small steps, each one anchored to what already exists, rather than doubling the canvas in one pass.  
**Prompt:** `extend the canvas to the left by one third, continuing the corridor wall and floor in the same perspective, same light direction, same haze, no new figures`  
**Yields to:** `kf.native_ratio` — The extension is large; generate natively at the delivery ratio.  
`repair.outpaint_extend`

### Upscale as a Separate Stage

**Also called:** resolution pass, detail enhancement, super resolution  
**What it is:** Generating at the resolution the model handles best and enlarging afterwards in a dedicated pass, rather than asking for the final delivery size directly.  
**Effect on the audience:** Better composition and better detail. Asking for very large output directly usually costs coherence, while a good generation enlarged afterwards keeps both.  
**Used for and where it works best:** Print delivery, large-format display, and any keyframe that must survive being pushed into in a video stage. Best in posters, exhibition work and keyframe plates.  
**Best in:** formats: Poster / Static Design, Generated Keyframe Feeding Video, Editorial / Magazine Image, Multi-Screen Installation, Product Still / Packshot, Heritage / Historical Documentary, General Reference Plate, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually invents detail that was not there when the enlargement factor is large, producing fake texture in skin and fabric. The exception is a moderate factor with a model chosen for faithfulness rather than for invention.  
**Prompt:** `generate at the native tile size and treat enlargement as a separate pass afterwards; do not request the final print dimensions from the generation itself`  
`repair.upscale_stage`

### Face Restoration With Caution

**Also called:** face enhancement, portrait restore, identity risk  
**What it is:** Applying a face-specific repair pass only when the identity is not carried by the image, because face restoration tends to normalise features toward an average.  
**Effect on the audience:** Protects likeness. A restoration pass often improves technical quality while quietly making the person less themselves.  
**Used for and where it works best:** Background faces and crowd figures where identity does not matter, and archive restoration where the original is the authority. Best in crowd plates and archive work.  
**Best in:** formats: Generated Keyframe Feeding Video, Heritage / Historical Documentary, General Reference Plate, Poster / Static Design, Documentary Feature, Editorial / Magazine Image, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: Heritage (civilisation-focused), Historical / Biopic, Verite / Observational, Drama, War  
**Avoid when:** It usually destroys a locked character when applied to a principal, because the restored face no longer matches the reference. The exception is restoring at low strength and comparing against the canonical reference before accepting.  
**Prompt:** `apply face repair to the background figures only; the two principals are identity-held and must not be passed through any face enhancement`  
**Yields to:** `ai.reference_sheet_lock` — A principal whose identity is held by a reference sheet.  
`repair.face_restore_caution`

### Artefact and Intrusion Removal

**Also called:** cleanup, object removal, plate cleaning  
**What it is:** Removing an unwanted element, a stray limb, an invented watermark, a modern intrusion, and regenerating the area behind it consistently with its surroundings.  
**Effect on the audience:** A plate that can be used. Small intrusions are the most common reason an otherwise finished image is discarded.  
**Used for and where it works best:** Heritage reconstruction where a modern element intruded, product work where a reflection shows the setup, and any plate destined for a video stage. Best in heritage work and product stills.  
**Best in:** formats: Generated Keyframe Feeding Video, Product Still / Packshot, Heritage / Historical Documentary, General Reference Plate, Location Sheet / Master Plate, Poster / Static Design, Editorial / Magazine Image, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually leaves a smear when the removed object sat across a strong pattern or a face. The exception is rebuilding the pattern deliberately in a second pass rather than expecting one removal to solve it.  
**Prompt:** `remove the stray object at the left edge and rebuild the wall behind it, continuing the brick courses and the same raking light, no blur patch`  
**Yields to:** `repair.inpaint_region` — The removal crossed a pattern or a face; rebuild it deliberately.  
`repair.artefact_removal`

### Colour Match Across a Set

**Also called:** batch grade, set consistency pass, palette alignment  
**What it is:** Passing every image in a set through the same correction so that the whole group sits in one colour world, rather than grading each image to look good alone.  
**Effect on the audience:** A set that reads as one body of work. Images each perfect in isolation frequently clash when placed side by side.  
**Used for and where it works best:** Campaigns, social sets, photo essays, and any sequence of keyframes that will be cut together. Best in campaigns, editorial sets and keyframe sequences.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Thumbnail / Social Card, Editorial / Magazine Image, Commercial / TVC, Brand Film, Comics / Webtoon / Photo Essay, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually flattens an image that earned its own distinct look. The exception is holding one image deliberately outside the match as an accent, with the exception declared rather than accidental.  
**Prompt:** `apply the same correction to all nine images so the set sits in one colour world; do not grade any single image to look best alone`  
`repair.colour_match_pass`

### Know When to Repair and When to Reroll

**Also called:** repair threshold, sunk-cost check  
**What it is:** Judging whether a fault is local, which repair fixes, or structural, which repair cannot, and reaching for a new generation when the composition or the pose is wrong rather than the detail.  
**Effect on the audience:** Time saved in both directions. Repairing a wrong composition wastes an hour; rerolling a nearly perfect plate for one hand wastes the plate.  
**Used for and where it works best:** Every image that comes back imperfect, which is most of them. A light fault is repairable when it is a modest shift of key direction or colour, by `repair.relight_pass`; a light whose shadows would have to move is structural and a reroll. Best across all generated still work.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Product Still / Packshot, General Reference Plate, Character Sheet / Turnaround, Thumbnail / Social Card, Editorial / Magazine Image, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually goes wrong in the direction of over-repairing, because the finished plate feels valuable and the fault feels small. The exception is a plate whose value is genuinely irreplaceable, such as one that matched a locked identity unusually well.  
**Prompt:** `not a prompt line but a decision: is the fault inside one region, or is it the pose, the composition or the light. Only the first is worth repairing, and a light fault only when it is a modest shift of key or colour`  
`repair.regenerate_vs_repair`

### Keep the Superseded Version

**Also called:** version retention, no destructive edit  
**What it is:** Saving every accepted state before repairing it, so a repair that turns out worse can be reversed without regenerating from nothing.  
**Effect on the audience:** Repairs become safe to attempt. Without retention, every correction risks losing a plate that was already acceptable.  
**Used for and where it works best:** All commissioned work, long projects, and any plate that took several attempts to reach. Best in campaigns and heritage libraries.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, Product Still / Packshot, General Reference Plate, Character Sheet / Turnaround, Location Sheet / Master Plate, Editorial / Magazine Image, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually accumulates clutter on a small project finished in one sitting. The exception is keeping only the accepted states rather than every attempt, which holds the safety without the sprawl.  
**Prompt:** `not a prompt line but a habit: save the accepted plate under its own version before any repair pass touches it`  
**Yields to:** `retouch.non_destructive_chain` — One-sitting project; reversible layers instead of version sprawl.  
`repair.version_and_keep`

### Relight Rather Than Regenerate

**Also called:** lighting correction, directional repair  
**What it is:** Correcting the light on a finished plate by a dedicated relighting pass, changing the key direction or the colour, instead of regenerating the whole scene for a lighting fault.  
**Effect on the audience:** Continuity recovered cheaply. A sequence whose third image has the key on the wrong side can be fixed without losing the figures that already match.  
**Used for and where it works best:** Sequence continuity repair, and matching a plate generated on a different day to the set it belongs to. Best in keyframe sequences and campaign sets.  
**Best in:** formats: Generated Keyframe Feeding Video, Poster / Static Design, General Reference Plate, Editorial / Magazine Image, Commercial / TVC, Brand Film, Product Still / Packshot, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually produces implausible shadows when the new direction is far from the original, because the shadows in the plate cannot move. The exception is a modest shift, or a subject whose shadows are mostly outside the frame.  
**Prompt:** `relight the plate so the key reads from camera left at the same warmth as the rest of the sequence; keep the figures, the wardrobe and the composition exactly as they are`  
`repair.relight_pass`

### Record What Was Repaired

**Also called:** repair log, edit provenance  
**What it is:** Noting which images were repaired, where and why, so that a later question about an image has an answer and a repeated fault is recognised as a pattern.  
**Effect on the audience:** Faults stop recurring. A log turns twenty separate hand repairs into one visible problem with the prompt that causes them.  
**Used for and where it works best:** Commissioned and published work, long projects, and any image that will be questioned later. Best in heritage documentary and client work.  
**Best in:** formats: Generated Keyframe Feeding Video, Heritage / Historical Documentary, Poster / Static Design, Product Still / Packshot, General Reference Plate, Editorial / Magazine Image, Commercial / TVC, Portrait Photography, Landscape Photography, Architectural Photography, Food Photography, Real Estate Photography, Fine Art Photography, Wedding Photography, Documentary Photography | genres: all  
**Avoid when:** It usually feels like bureaucracy on a single image made in a minute. The exception is that the log is what reveals systematic faults, which is worth more on a long project than any individual repair.  
**Prompt:** `not a prompt line but a record: image id, region repaired, reason, method, date, and whether the underlying prompt was corrected as well`  
`repair.record_the_fix`
