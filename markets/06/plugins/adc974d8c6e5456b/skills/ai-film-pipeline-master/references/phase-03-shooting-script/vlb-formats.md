# 12 — Formats

From the Visual Language Bible. Start from `./vlb-decision-tables.md`: name the change you want in the scene, take the technique it hands you, and read its card here.

---

## 12 — Formats


Format decides **structure, rhythm and ratio**. Genre decides **visual language**. They are
independent — a horror feature and a horror Reel share a genre and share almost nothing else.

For each format: average shot length (ASL), ratio, dominant shots, and the characteristic transition.

---

### Feature Film
**Length:** 90–180 min · **ASL:** 3–6 s · **Ratio:** 2.39:1 or 1.85:1
**Dominant shots:** a wide master then full coverage, OTS, MCU, long reaction shots.
**Structure:** three acts, 40–60 scenes.
**Characteristic transition:** fade between acts, J-cut within them.
**The secret of the format:** a feature can carry patience. A long silent shot is strength here and
death in short-form.

---


`vlb.format.feature_film`

### Short Film
**Length:** 3–20 min · **ASL:** 3–5 s
**Structure:** one idea, one turn, no acts.
**The secret of the format:** begin as close to the crisis as possible. There is no time to
establish — establish *during* the event.

---


`vlb.format.short_film`

### Series Episode
**Length:** 22–60 min · **ASL:** 2.5–4.5 s
**Structure:** cold open → titles → four acts (ad breaks) → closing hook.
**Dominant shots:** more efficient coverage than a feature — fewer masters, more OTS and MCU.
**Characteristic transition:** every act ends on an open question.

---


`vlb.format.series_episode`

### Documentary
**Length:** 20–120 min · **ASL:** 5–9 s
**Dominant shots:** a locked MS interview, wide B-roll, macro detail, archive, aerials.
**Lighting:** available or natural for the most part.
**Characteristic transition:** sound bridge, dissolve, graphic match between archive and present.
**The secret of the format:** the interview carries the information, the B-roll carries the feeling.
Do not ask them to do both in the same moment.

---


`vlb.format.documentary`

### Heritage Documentary
**As documentary, plus:** slow aerial establishers, tilt-ups on architecture, macro on carving and
script, golden hour, volumetric light inside temples.
**Option:** silhouette and rear azimuth where the brief wants the figures anonymous or the performance restrained; where it wants faces, show them — the brief decides.
**Characteristic transition:** graphic match between an ancient motif and a modern form.

---


`vlb.format.heritage_documentary`

### Music Video
**Length:** 2–5 min · **ASL:** 1–3 s
**Dominant shots:** performance, narrative, the conceptual image.
**The law:** **cut on the beat** - except on children's content, where `kids.no_fast_cuts` and its 1.5-second floor outrank beat multiples, as that card states. The structure is the song's structure — verse, chorus, bridge.
**Characteristic transition:** flash, speed ramp, whip pan, a full colour change at the chorus.
**The secret of the format:** the chorus must read *as* a chorus. Change something large — wardrobe,
location, colour, or the number of people in frame.

---


`vlb.format.music_video`

### Commercial / Ad
**Length:** commonly 6 / 15 / 30 / 60 s — references, not slots: a 45-second or two-minute ad is built at the length the brief names · **ASL:** 0.8–2 s
**Structure:** problem → product → resolution → endline.
**Dominant shots:** macro on the product, product orbit, a use shot, a satisfied reaction, the logo frame.
**Lighting:** always ideal, rim light on the product.
**The secret of the format:** the final three seconds *are* the commercial. Everything else is setup.

---


`vlb.format.commercial_ad`

### Product & Motion Design
**Dominant shots:** 360 orbit, macro, extreme slow motion on liquid and spray, repeatable
motion-control moves, freeze.
**Lighting:** studio, rim light, gradient background.
**Prompt:** `product on a seamless background, slow 360 orbit, rim-lit edges, ultra slow motion`

---


`vlb.format.product_motion_design`

### Trailer
**Length:** 90–150 s · **ASL:** starts at 3 s, ends at 0.4 s
**Classic structure:** three movements — introduce the world → escalate the problem → a rapid
percussive sequence, a silence, and a final image.
**Characteristic transition:** cut on a drum hit, black frames punched between shots.

---


`vlb.format.trailer`

### Vertical Short-Form (Reels, Shorts, TikTok)
**Length:** commonly 7–60 s, and any length the brief names · **ASL:** 0.8–2 s · **Ratio:** 9:16 — a reel or feed video on Facebook or YouTube may also be 16:9, and the brief's aspect wins
**Structure:** hook (0–3 s) → promise → payoff → loop or close.
**Dominant shots:** mostly MCU and CU — a wide reads small on a phone, so give it a reason. Movement in every shot.
**Safe zones:** the numbers live on `vertical.safe_zones` in [`../phase-07-image-prompt-engineering/vertical-short-form.md`](../phase-07-image-prompt-engineering/vertical-short-form.md), which owns them for the whole package and also carries the right-edge rule and the TikTok exception. Do not restate a figure here; open the card.
**Characteristic transition:** whip pan, object wipe, flash, speed ramp, cut on the beat.
**The secret of the format:** the first frame must be the strangest frame in the video. Do not open
on an establisher — open on the result.

---


**Yields to:** `vertical.safe_zones` — Safe-zone figures; that card owns them (authority yield).  
`vlb.format.vertical_short_form`

### Kids Content
**Length:** 2–8 min · **ASL:** 2–4 s
**Dominant shots:** camera at child height, full shots (they want to see the whole body), centred
framing, high key.
**Usually avoided:** dutch angles, low key, disorienting fast cutting, darkness — defaults for a young audience; a brief that asks for a spooky or night episode gets it, gently.
**Characteristic transition:** wipe, iris, a playful morph, a character crossing frame.
**The secret of the format:** repetition is a feature, not a flaw. The same shot at the same angle
each verse means safety and learning.

---


`vlb.format.kids_content`

### Animation
**ASL:** 2–4 s (anime slower: 3–8 s)
**Dominant shots:** anything — the camera has no physical constraints. Impossible orbits, movement
through solid objects.
**Special law:** animation needs **character-lock frames** far more than live action, or the
features drift.
**Anime specifically:** long held statics punctuated by explosions of motion. Speed lines, the eye
ECU, a slow pan across a landscape.

---


`vlb.format.animation`

### Explainer
**Length:** 60–180 s · **ASL:** 2–4 s
**Dominant shots:** graphics, kinetic type, simple symbolic images.
**The law:** the image illustrates the sentence being spoken *right now* — not before it, not after it.

---


`vlb.format.explainer`

### Lyric Video
**Dominant shots:** a slow-moving background plus synchronised type.
**The secret:** the text is the subject. The background must not compete — one slow move is enough.

---


`vlb.format.lyric_video`

### Live Event
**Dominant shots:** a main wide plus two side cameras plus a handheld plus a cable cam.
**The secret:** the audience shot sells the event, not the stage shot.

---


`vlb.format.live_event`

### Sports
**Dominant shots:** long tracking wides, extreme slow motion on the moment, cable cam, macro on the
face, a four-angle replay.
**Characteristic transition:** freeze plus analytical overlay.

---


`vlb.format.sports`

### Corporate
**ASL:** 3–5 s · **Shots:** MS interview, a slow slider across the office, hands working, a building aerial.
**Lighting:** clean, high key, undramatic.

---


`vlb.format.corporate`

### Game Cinematic
**Dominant shots:** impossible moves, hero orbits, long cranes, the low-angle hero shot.
**The secret:** it always ends on a *ready to play* image — the hero facing camera, or advancing
toward the objective.

---


`vlb.format.game_cinematic`

### 360 / VR
**The law:** there is no frame, so there is no composition. You direct with sound and light instead.
**Usually avoided:** fast cutting — it can induce nausea; cut slowly unless the brief wants otherwise.

---


`vlb.format.vr`

### Meme / Comedy Edit
**Shots:** snap zoom, freeze, large type, smash cut.
**The secret:** timing is the joke. One frame too many kills it.

---

`vlb.format.meme_comedy_edit`

