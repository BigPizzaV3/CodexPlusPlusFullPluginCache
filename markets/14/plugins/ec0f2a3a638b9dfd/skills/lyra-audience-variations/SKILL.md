---
name: lyra-audience-variations
description: "Use when the user wants the same app video ad for another audience, e.g. \"swap the character\", \"same video with another person / outfit / room\", \"a version for moms / men / 40+\", \"localize for Brazil\", \"new faces for this winner\", \"persona A/B test\". Builds each change as a Lyra variation. New angles or messages go to lyra-ad-concept-multiplier."
---

# lyra-audience-variations

Mini skill. Takes a video ad that works (a Lyra workflow, a finished video, or a concept about to be built) and makes versions of it for other parts of the app's audience by changing **what the viewer sees and hears**: the person, their clothes, the room, the car, the time of day, the market, the voice. The message, the angle, the script, the beats, the camera and the edit stay. One version = one Lyra **variation** of the original workflow.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**Why it works.** In app ads, the visible world is targeting. In the first second the viewer reads who this is about from the face, the clothes, the room and the things around the person, and decides "that's me" or scrolls. The same proven message in a world that looks like another segment's life can reach people the original never stopped. And because the message stays identical, each version is a clean test of one visible thing.

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different layer, bundle or build serves the audience better, do it and say why in one line. Only a few things are fixed: truth (no invented claims, reviews or numbers; an AI person is never a real customer), the Brand Kit's facts, casting ethics (no real people or lookalikes, no stereotypes, adults only as speakers), the product and its real UI, Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file only adds what is specific to audience variations. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.**
- Person, place, voice, speech, camera setups, character card and realism → `lyra-ugc-video`.
- A phone moment or any UI → `lyra-ui-motion-video`: the screen never varies; a rebuilt phone shot keeps the same screenshot, checked word by word.
- New openings on a version (version × hook tests) → `lyra-video-hooks`.
- A new angle, message or story on the same concept → `lyra-ad-concept-multiplier`.
- A competitor's video as the source → `lyra-copy-competitor-ad` (their actor or world is never kept: that is a copy, not a variation).

---

## Audience variations or concept multiplier

Both keep what worked and make more versions; they answer different questions.

| | **Audience variations** (this skill) | **Ad concept multiplier** |
|---|---|---|
| Question | Who is it for? Whose life does it show? | What else can this concept say? |
| Changes | the visible layers and the voice; words only where they are tied to the person or the place | the angle (another pain, benefit or motivation), the situation as a new story, the script |
| Stays | the message, the angle, the script, the beats, the timing, the camera | the concept's mechanism: format, structure, hook mechanism, pacing, look |
| The test reads | which person or world pulls which segment | which angle sells |

**The border rule.** If the script's words change beyond the identity-bound ones (line audit, Step 2), it is the multiplier. A setting stays here when it is **the same situation re-dressed** for another audience (a bedroom in São Paulo, a nurse's bedroom at 9 am); it goes to the multiplier when it is **a new situation where another pain happens** (bed → gym).

**The ladder of iterations:** hooks (the first 3 s, `lyra-video-hooks`) → audience variations (who and where) → concept multiplier (a new angle) → a new concept (base skill).

---

## How to think about an audience variation

**Every version is a hypothesis**, written as one line: "We think [segment] stops and installs more when the ad shows [what changed], because [reason from the Brand Kit]."

**Two ways a person works** (archetypes from `lyra-ugc-video`): a **mirror** (the viewer sees themselves) or a **trusted guide** (a friend a step ahead, a converted skeptic, an insider, a parent). The world around the person works the same way: it is either the viewer's own world, or the world they want.

### The layers: everything visible that can vary

| Layer | What changes | What it tells the viewer | What reruns (cost) |
|---|---|---|---|
| **1. Person** (character swap) | face, age, gender, body type, energy, archetype | "that's me" or "I'd listen to her" | the character → every image and clip with the person |
| **2. Wardrobe and styling** | clothes, hair, makeup, nails, glasses, jewelry, bag | occupation, income, subculture, season, how put-together they are | the character (the outfit is part of the card) → every image and clip with the person |
| **3. Setting and background** | the room, the building, the street, the city; its lived-in details | life stage, living situation, market | every image and clip that shows the place |
| **4. Props and vehicles** | the car (class, age, interior), laptop or tablet, mug or mate, stroller, pet, sports gear, the phone's body | lifestyle, status, life stage, hobby | only the scenes where the prop appears |
| **5. Time, season, weather, light** | night or morning, winter coat or summer heat, rain, daylight or lamp | rhythm of life (shift worker, parent, student), market and season | every image and clip of the scene; wardrobe often follows |
| **6. Market markers** | architecture, window views, sockets, food, interiors, street look; no readable text | "this is here, this is us" | the scenes that show them |
| **7. Voice and language** | the voice (age, gender, accent, texture), the language, the identity-bound words, captions | market, age, warmth or authority | native speech: the clips with speech; a separate VO: only the VO node (the cheapest layer) |
| **8. Polish and palette** | raw or elevated, light quality, grading, palette inside the brand | mass or premium, playful or calm | almost everything |

**What never changes in an audience variation:** the product and the feature, the UI (only the user's screenshots, the same screen in every version), claims, offer and CTA, the angle and the message, the beat structure and timing, the hook mechanism. A change there is a new concept or the multiplier.

### One layer or a bundle

- **Clean variation (mode A, for tests):** one layer changes, everything else is copied word for word. The result teaches which visible thing moves the numbers: "the scrubs pulled nurses", "the premium car lowered cost per trial", "the man in his 40s beat the student".
- **Audience version (mode B, for a segment or a market):** the coherent bundle that belongs to that audience changes together (person + wardrobe + setting + time + voice and language) and is named as a version, not a clean test.

| | **A. Clean variation** | **B. Audience version** |
|---|---|---|
| What changes | one layer | the bundle that belongs to the segment or market, plus the identity-bound words |
| What stays | everything else, word for word | the message, the angle, beats and timing (about ±0.5 s per beat), camera setup, feature, CTA and offer, music, end card |
| Pick it when | testing which person, outfit, setting or prop works; refreshing a fatigued winner | a new segment from the Brand Kit, a new market or language |
| Reads as | "V2 (person) vs control V1" | "the C1 ad for nurses", "the C1 ad for Brazil" |

Both can run in one round: the original as control + 1 to 2 clean variations + 1 audience version.

**Coherence: the one-story test** (`lyra-ugc-video`). The layers still tell one life. A nurse needs the scrubs, the morning daylight and the tiredness; a student in a premium car, or a 55-year-old man with a 20-year-old's voice, breaks the story. When one layer changes, check the others: in mode A, change only what can change alone; in mode B, change everything the new life needs.

**Different enough to count.** The change must read at thumbnail size in the first second. A new T-shirt color is not a variation: it teaches nothing, and Meta's delivery tends to treat near-identical creatives as one (check the current behaviour). Make the tested difference visible at a glance.

**Final test for every version:** would someone from this segment see the first frame and think "that's me" (or "that's the life I want")? Is the tested difference obvious, and everything else the same? Is every word still true for the app?

---

## Step 1 additions: the source, the audience, the variation map

1. **The source.**
   - **A Lyra workflow** (built with our skills, or the user's own): `list_variations` and `get_workflow` on the original. Find every node by the layer it carries: the person (character, keyframes, phone shots, B-roll with hands, clips, talking head), the place and time (every image and clip prompt's environment line), props, voice (clip voice anchors, VO node), style. Read the prompts: they give the original world.
   - **A finished video, the user's own ad** (a file or a public direct link): `create_upload` → `attach_upload`. Analyse it as in `lyra-copy-competitor-ad` Path 2 (frames every 3 s and at each cut, transcript with timestamps); only the production breakdown is needed: shots with times, person, wardrobe, place, props, light, camera setup, voice, speech, sound, UI moments, end card. It is the user's footage, so it may serve as an editing or motion reference (Best way to build it).
   - **A concept not built yet** → build it with the matching skill and plan the versions from the start; this file gives the variation map.
   Check `list_uploads` first.
2. **The original world card ("V1, control").** One note in the `lyra-ugc-video` format plus the world: **person** (age, look, hair, skin, energy, archetype) · **wardrobe** · **setting** (place, 2 to 3 lived-in details) · **props** (including any vehicle) · **time, season, light** · **market markers** · **voice** (anchor, language) · **polish and palette**. Every version is written against it, layer by layer.
3. **Brand Kit and audience** (base Reference I; several kits → ask which; never mix two). Read: segments and their daily life, pains in their words, desires, objections, markets and languages, positioning, must include / must exclude, forbidden claims. Reuse the pain map (`lyra-video-hooks` Step 1). No segments in the kit → 3 to 5 segment hypotheses from the app card, to confirm, and keep moving in the same message.
4. **Variation map** (user text node "Variation map"). One line per candidate: code · segment · mode A (the one layer) or B (the bundle) · what changes, layer by layer · hypothesis · why this segment matters. Offer 3 to 5, recommend 2 with one line why.
   > V2 · students (same segment as V1) · A: person only (a converted skeptic, Leo, 22) · a doubting peer earns more trust than a tired one
   > V3 · students · A: setting only (a shared dorm room instead of her own bedroom) · a cheaper, louder room is closer to most students' nights
   > V4 · night-shift nurses (kit segment 2) · B: person, wardrobe (scrubs on the chair, mask marks), time (9 am, daylight through blinds), 4 words · nurses stop for someone who sleeps at the wrong time like them
   > V5 · Brazil, students · B: person, setting, market markers, voice and language (Brazilian Portuguese) · a local face, room and voice beat a dubbed import
5. **Intake quiz** (base Step 1 format: one message, multiple choice, options from the Brand Kit, the recommended option first): which segments, markets or layers (with your recommendation) · mode A or B per version · how many (default 2 + the original as control) · language per version · screenshots, if a phone moment must be rebuilt and they aren't in the workflow · anything the brand doesn't want on screen (an age group, a car class, a look).

**Defaults (state, don't ask):** 2 versions + the original as control · **one variation per version**, copied from the original, which stays Main and untouched · mode A for tests, B for a new segment or market · cheapest informative layer first when the user has no preference (voice on a separate VO, a prop, wardrobe) · same length, ratio and platform as the original · real people: Seedance 2.5, references only, the original's resolution (720p by default), sound on · Nano Banana Pro for every image, 9:16, 2K (4K for close selfies) · captions changed only where words changed · same music, end card, CTA and hook.

**Recommended first run:** A. The changed images (portraits, wardrobe or world frames for every version; images are cheap, and they show whether the variation reads in one glance).

---

## Step 1a: casting and world-building from the audience

**Start from the segment's life, not from a label.** Write the situation first (a nurse after a night shift, a dad with a toddler, a freelancer between clients, a student in a shared dorm), then derive every layer from it: who they are, what they wear at the pain moment, where they are, what's around them, what time it is, how they sound.

**Person.** Casting follows `lyra-ugc-video` "Person" (archetypes, character card, realism):
- Markets look and sound local: a version for Brazil is a person from there, not the original person re-dressed.
- Respect, not stereotypes: no caricature of age, gender, ethnicity, body, religion or class; no accent played for a laugh; no costume of an identity. A persona is a specific person, not a demographic.
- Adults speak (18+); in kids and family apps the parent speaks. No real people, creators, celebrities, lookalikes or cloned voices.

**Wardrobe and styling.** What this person really wears at that moment (home clothes at 2 am are not an outfit). Occupation signals are accurate and generic: scrubs without a hospital name, a uniform without a real employer's logo. No visible brand logos on clothes, bags or shoes. Styling carries income and taste quietly (fabric, fit, wear), never as a joke.

**Setting and background.** The same situation, re-dressed for this life: lived-in, 2 to 3 specific details, light that is really there. Market-accurate interiors and streets. Never a showroom; never readable signage or text (blur or avoid it).

**Props and vehicles.** One hero prop per scene, chosen because this segment really has it (a stroller, a hospital lanyard without a name, a work laptop, a gym bag). Cars: the class and age signal the life (a used hatchback with a child seat, a company sedan, a delivery scooter); generic, no badges or plates, interior details instead of the logo; phone in a mount or the car parked. The phone's body may change (a generic modern phone of the kind this market uses), **the screen never does**.

**Time, season, light.** The pain moment's real time for this segment (a shift worker's "night" is 9 am); the season of the market at launch; wardrobe and light follow.

**Market markers.** Architecture, window views, sockets, food, interior style, street life, without text. Enough to feel local, not a postcard.

**Voice and language.** Rewrite the voice anchor for the person and the market; another language = the speech written in that language (not translated word for word), new captions.

**Words and the platform.** The person may talk about their own life in first person ("I'm on nights this week"). The ad never tells the viewer they have a personal attribute ("Are you over 50?", "Drowning in debt?"): Meta restricts ads that assert or imply personal attributes such as age, health, finances, religion, ethnicity or sexual orientation. Callouts by situation or habit ("Night owls, listen") are the safer form. Check current platform rules; this is not legal advice.

---

## Step 2 addition: the variation sheet

Before building, a user text node "Variation sheet", part of the concept the user approves:

1. **Lock list:** what stays identical in every version (message, beats and timing, camera setup, action, the phone screen, music, CTA, end card, hook, and in mode A every layer except the tested one).
2. **World cards:** V1 (control) and every version, the same eight layers, voice anchor included.
3. **Line audit** (mode B, or a new language): every spoken line and caption marked **universal** (stays) or **identity-bound** (adapts: a time, an occupation, a place name), with the new words. Same job, same length (about ±10% words), same claims. More than identity-bound words changing → it is the multiplier, say so.

   | Beat | Time | V1 line | Bound? | V4 line | Words V1 / V4 |
   |---|---|---|---|---|---|
   | Hook | 0 to 3 s | "Two a.m. and my brain won't shut up." | yes (the time) | "Nine a.m. and I still can't sleep." | 8 / 7 |
   | Old way | 3 to 6 s | "Tea, podcasts, counting sheep… nothing." | no | same | 5 / 5 |

4. **Side by side:**

   | Layer | V1 (control) | V2 (A: person) | V3 (A: setting) | V4 (B: nurses) |
   |---|---|---|---|---|
   | Person | Mia, 21, student | Leo, 22, student, skeptic | Mia | Ana, 29, nurse |
   | Wardrobe | grey hoodie | black hoodie | grey hoodie | navy t-shirt, scrubs on the chair |
   | Setting | own bedroom | own bedroom | shared dorm room, roommate's bed in the background, string lights | own bedroom, small flat |
   | Time, light | 2 am, phone light, lamp | same | same | 9 am, daylight through blinds |
   | Voice | young woman, soft American, sleepy | young man, dry, flat | same as V1 | woman, late 20s, warm, low, tired |
   | Words changed | — | none | none | hook (the time) |
   | Hypothesis | — | a doubter earns more trust | a louder, cheaper room is closer to their nights | nurses stop for wrong-time sleep |

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the source is | Best approach (graph) | Models |
|---|---|---|
| **A Lyra workflow with a finished creative** (default) | **one variation per version** (below): `create_variation` copies the whole canvas with its results → `switch_variation` → `update_node` only on the nodes that carry the changed layers (layer map below) → rerun only those and what depends on them → Video Editor | as the original |
| The scene must stay exactly as in the original except the changed layer (strict mode A) | in the variation, a **frame swap** image node: the copied frame (still holding the original result) + the new element (portrait, outfit, car, room) → the clip takes the swapped frame instead of the old one | nano-banana-pro · as the original |
| A workflow on frame models (Seedance 2.0, Kling) | as the default; the new or swapped frame becomes the clip's first (and last) frame, linked right after it has a result and the user selected one | nano-banana-pro · seedance-2.0 / kling-v3-video |
| A version that needs its own workflow (another app or client, shared separately) | the workflow menu (⋮ next to the name) → **Save as a new workflow**; no MCP tool does this, so ask the user to click it (or do it in their browser if they allow), then work there as in the default row | as the original |
| **A finished video, the person speaks** | frames + transcript → the new portrait and world frames (frame swaps on the key frames) → **one Seedance 2.5 clip** with them as references, the speech in quotes (same or audited lines), the shot plan from the breakdown as "cut to" with lengths → optional: the original video as **[Video1], editing reference only**, when the timing must match closely (it can leak the old person or place: check) → Video Editor with the original's music, end card and UI inserts, if the user has the files | nano-banana-pro · seedance-2.5 |
| A finished video, no speech or a separate VO, the movement matters (a walk, a dance, a gesture) | new portrait + frame swap of the first frame → **Kling 3.0 Motion Control** with the original video as the motion source (the user's own footage only) → VO and music in the Video Editor | kling-v3-motion-control · elevenlabs/v3 |
| Voice or language only, with a separate VO | the cheapest version: a new VO node or voice (`list_voices`), the text in the new language if needed, new captions; no images or clips rerun | elevenlabs/v3 |
| Hands only (POV) | the hands are the person: skin tone, age of the hands, nails, rings, sleeves, watch; plus the surface and props under them; UI on screen → Seedance 2.0 frames | nano-banana-pro · seedance-2.0 |
| Car formats (car vlog, parked confession) | the car is a strong layer on its own: class, age, interior, what lies on the seat; swap it on the frames, keep the person and the mount | nano-banana-pro · seedance-2.5 |
| Two people | vary one or both, each with its own card and voice anchor; lines tied to [ImageN] | seedance-2.5 |
| A stylized character or mascot | a new original character, outfit or world in the same style family; the brand's own mascot is never replaced without the user's yes (it is brand identity) | nano-banana-pro · seedance-2.0 |
| A talking head node in the original | new face image and/or background + new voice audio | veed/fabric-1.0 |
| A new market | mode B: person, setting, market markers, voice and language; the speech written in that language; screenshots of the localized app for the phone moment | seedance-2.5 |
| Many versions, tight budget | the changed images for all; clips only for the 1 to 2 the user picks; cheapest layers first | nano-banana-pro · seedance-2.5 |

### Variations: the way to make a version

In Lyra every version of a finished creative is a **variation** of its workflow: the **Create variation** button above the canvas (the `create_variation` tool) duplicates the whole space (every node, prompt, connection and result) into a new version. The original stays **Main** and untouched as the control; the change is written into the copy.

**Make a variation when:** the Brand Kit has two or more audience segments (one variation per segment) · the user wants another language or market · a person, wardrobe, setting or prop test · a fatigued winner gets a new look · the user names a change ("same, but a man in his 40s", "same, but in a car"). One variation = one version (one layer in mode A, one bundle in mode B).

**Step by step:**
1. `list_variations` → find the original (the main one, unless the user names another). Rename it if needed: `rename_variation` "V1 · Mia · students (control)".
2. `create_variation` with `copy_from_variation_uuid` = the original and `title` = code, what changed, segment, language: "V4 · Ana · nurses · EN", "V3 · dorm room · students · EN". The copy carries the original's results, so everything that doesn't change is already there and never reruns.
3. `switch_variation` to it (Lyra renames the workflow after the main variation; tell the user which one is open), then `get_workflow`.
4. Write the change in with `update_node`, only on the nodes that carry the changed layers (layer map below). Everything else stays word for word. Another segment or market with its own kit → `assign_brand_kit` on this variation (each variation has its own).
5. Read the price on the nodes that will rerun and put it in the approval message (base Step 6: one question, then run everything). Unchanged nodes keep the copied results.
6. Repeat from step 2 for the next version (always copy from the original, not from another version).
7. When done, `switch_variation` back to the original if the user wants it shown first, and say which variation holds which version.

### The layer map: which nodes to update, what to rerun

| Layer changed | `update_node` on | Rerun |
|---|---|---|
| Person | the character node (new card, opening with "A different person from the original:"); the identity line in every image and clip that shows the person; the voice anchor | character → images with the person → clips → Video Editor |
| Wardrobe and styling | the outfit and styling in the character card; the same words in every image and clip prompt that names the outfit | character → images with the person → clips → Video Editor |
| Setting and background | the environment line in the character node (if it shows the place) and in every image and clip prompt | every image and clip that shows the place → Video Editor |
| Props and vehicles | the prompts of the scenes where the prop appears | those images and clips → Video Editor |
| Time, season, light | the light and time line everywhere; wardrobe if it follows | every image and clip of the scene → Video Editor |
| Market markers | the environment details everywhere they show | those images and clips → Video Editor |
| Voice and language | the voice anchor and the audited lines in clips with speech; or the VO node's voice and text | native speech: the clips with speech; separate VO: only the VO → Video Editor; captions in the editor |
| Polish and palette | the style line everywhere | almost everything |

After `update_node`, `get_workflow` on the variation and search every prompt for the old value (the old name, the old outfit, the old room): one forgotten node puts two worlds in one ad.

### The portrait: Lyra's Character Generation rules

When the person or the wardrobe changes, the new character follows the rules of Lyra's own **Character Generation** node, so it feels like a real person from Instagram Stories or TikTok. If the canvas has a Character Generation or Character Brief node (from a template), `update_node` its prompt (the tools can't create these nodes); otherwise the character is an Image Generation node (Nano Banana Pro) with a prompt written to the same rules:

- **Natural, not polished or "model-like"**; slightly imperfect: skin texture, asymmetry, natural posture.
- **Looks directly into the camera**: selfie or front-facing POV.
- **A believable real-life place tied to the product context** (the pain moment), not a staged production.
- **No text** in the image: no captions, no watermark; text is added in the Video Editor.
- **Matches the scene context**: pose, expression and framing fit the scene; the identity stays.
- **Framing by shot:** full body for lifestyle, action or environment (with footwear) · waist up for conversational, product-holding or testimonial · close-up for emotional hooks, reactions, hero frames.
- **Expression by the scene's mood:** excited or caught for a hook frame, thoughtful or tired for the problem, relieved or confident for the solution.
- **Framing by ratio:** 9:16 → the person in the central 65%, space for text top and bottom · 1:1 → waist up, centered · 4:5 → like 1:1 with a little more vertical space · 16:9 → full body or environment, off-center on the thirds.
- **The user's direction comes first** (scene, pose, expression, outfit, place).

### Frame swaps (when everything else must stay exactly)

Rerunning from the changed node down usually gives the same scene with the new element, because every other word of the prompts is unchanged. When the rest must stay exactly as in the original (strict mode A, or a finished video as the source), swap inside the frame itself:

- **Person swap** (keep the world, change the person): portrait first (by the rules above, count 2, the user picks), then one Image Generation node per key frame with the original frame (in a variation: the copied frame, before it is rerun) and the new portrait connected.
- **World swap** (keep the person, change the outfit, room, car, prop or light): one Image Generation node per key frame with the original frame connected, plus a reference image of the new element if there is one; the prompt keeps the person, pose, framing and phone exactly and changes only the named layer.

Check every swapped frame for **bleed** (traces of the old face, outfit, room or car), hands, the phone and the screen. Bleed → rerun with the "change only…" line moved to the start; still there after two tries → describe the scene in words and generate it fresh with the new element as the only reference for that layer.

### Voice

- **Native speech** (Seedance 2.5): rewrite the voice anchor for the person and market; keep the pace, so the timing holds.
- **Separate VO:** a new voice from `list_voices` (language, accent, gender, age, use case) with the same or audited text; check the real audio length (~1 s shorter than the video).
- **Exact words or a fixed brand voice:** VO as an audio reference in the Seedance 2.5 clip (base Reference C).

**Connections.** A variation copies the original's connections, so the graph already runs end to end. Only new nodes need links (base Step 4): a frame swap node → the clip instead of the old frame; a swapped frame on a frame model, right after it has a result. The "Variation map" and "Variation sheet" text nodes are notes for the user: they don't feed generation; consistency comes from the images connected as references plus the anchors written into every prompt.

**Layout and labels.** Each variation keeps the original's layout, Sections and order, so the user can flip between versions and see the same canvas. Put the "Variation map" and "Variation sheet" notes in the original's Sources Section before creating the variations, so every variation carries them. Relabel the nodes that changed with the version code: "V4 Ana: character", "V3: dorm room (frame)", "V4 Ana: clip", "Final: C1 · V4 nurses".

---

## Prompt rules (audience variations)

| Node | Write | Avoid |
|---|---|---|
| Variation map, variation sheet (text) | codes, segments, modes, layers changed, hypotheses, world cards, lock list, line audit, side by side | versions without a segment or a hypothesis; "a different vibe" without naming the layer |
| Portrait (character node) | "UGC phone photo" → "A different person from the original:" + the new card word for word → looking directly into the camera → a real place tied to the product context → framing by shot and ratio, expression by mood (Character Generation rules) → realism line → no text | details of the old card left in; "flawless", "editorial", model-like posing; a stereotype; text |
| Person swap (image edit) | each input's job first → keep list (room, light, angle, framing, pose, action, phone, objects) → replace only the person → mode B: other changed layers named → realism → no text | "the same woman, but older" (keeps the old face); re-describing the whole scene (it drifts) |
| World swap (image edit) | "[Image1] is the original frame: keep the person, face, hair, pose, the phone and the framing exactly" → change only the named layer, described concretely (class, age, materials, details) → realism → no text, no logos, no plates | changing two layers in a mode A swap; brand names, badges, readable signs |
| Clip | the original prompt; only the lines of the changed layers replaced (identity, wardrobe, environment, prop, light, voice anchor, audited lines); roles first | the old value left anywhere in the prompt; another camera, action or timing than the original |
| Clip with [Video1] (the user's own footage) | "[Video1] is an editing reference only: copy its cuts, shot lengths, camera movement and the person's actions. Do not copy the person's face, hair, body, clothing, the place or the voice; the person is [Image1]." | connecting it without a stated job; skipping the leak check |
| VO | the same text (mode A) or the audited text (mode B); a voice picked for the version | changing words in mode A; a voice that doesn't fit the face |

**Pattern: person swap (Nano Banana Pro, mode B).**

> UGC phone photo, same scene with a new person. [Image1] is the original frame: keep the bed, the duvet, the camera angle, the framing, her pose lying on her side and the phone held at arm's length exactly. [Image2] is the new person: use her face, hair, skin and build. Replace only the person in [Image1] with the woman from [Image2]: Ana, 29, warm olive skin, dark straight hair in a low messy ponytail, faint marks from a face mask on her cheeks, oversized navy t-shirt. The room changes only in light and two details: morning daylight through half-closed blinds instead of the lamp, light blue scrubs folded on the chair. Shot on a 24mm phone front camera, deep focus, natural skin texture, visible pores, slight dark circles, no beauty filter. No text, no captions, no watermark, no visible phone screen.

**Pattern: world swap, the car (Nano Banana Pro, mode A).**

> UGC phone photo, same person in a different car. [Image1] is the original frame: keep the woman, her face, hair, outfit, pose, expression, the phone in the dashboard mount, the framing and the camera angle exactly. Change only the car: a ten-year-old compact hatchback, worn grey fabric seats, a child seat visible in the back, a water bottle and a parking receipt in the door pocket, a scuffed plastic dashboard; daylight through the side window as before. Generic car, no logos, no badges, no readable text or plates. Phone-camera look, deep focus, natural skin texture. No captions, no watermark.

**Pattern: what changes in a clip prompt (Seedance 2.5).** Only the lines of the changed layers are replaced: the identity line ("[Image1] is Ana: her face, ponytail, navy t-shirt, and her bedroom in morning daylight"), the voice anchor ("Voice: woman, late 20s, warm low voice, neutral American accent, tired, unhurried") and the audited lines ("Nine a.m. and I still can't sleep."). Camera, action order, cuts, sound line, end state and the avoid line stay word for word. One fix is allowed: if someone speaks and the original's sound line lets music in, add "no music, no background music, no soundtrack, no score" (base Reference C); music stays the original's track in the Video Editor.

---

## Run options (audience variations)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option, multiplied by the number of versions. **A. Changed images (recommended):** portraits (count 2 per person), wardrobe or world frames · **B. Frame swaps and phone shots** for the picked images · **C. Clips and Video Editors** · or **D. Everything** at once (count 1; no pause to pick). Voice-only versions on a separate VO cost only the VO. When an image has several results, the user selects one in Lyra before the next stage (references pin to the selected result).

---

## Truth, casting and brand safety

- An AI person is a creative performance, never a real customer, user or reviewer (`lyra-ugc-video`, Truth and disclosure). Remind the user once to turn on the AI-generated label.
- **Claims stay identical across versions.** A new person, car or room never brings a new claim or result ("as a nurse I now sleep eight hours"); everything comes from the Brand Kit.
- No real people, creators, celebrities or lookalikes; no cloned voices.
- No stereotypes or caricatures of age, gender, ethnicity, body, religion or class; no accent or status as a joke; speaking persons are adults.
- No third-party brands: no logos on clothes, cars, laptops or mugs, no car badges or plates, no readable signs, no real employers on uniforms, no landmarks used as brands.
- No personal-attribute callouts to the viewer (Meta's personal attributes policy); the person speaks about their own life.
- Health, fitness and weight-loss apps: the person's body is never the result; no body before/after.
- **Brand safety** (Lyra's System Preamble, base Reference B): no profanity, no political statements, no unsubstantiated health claims, no competitor disparagement. The Brand Kit's **forbidden claims are enforced absolutely**, in every version's line, caption, visual and VO; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.

---

## Deliverable and naming

1. "Variation map" and "Variation sheet" text nodes.
2. One variation per version (named with its code, what changed, segment and language), with the changed images, clips and its own Video Editor; the original untouched as Main, the control.

The original keeps its name as V1. Versions add `V{n}{Layer}{Segment}`, and the locale for a market version: `B6-A:CantSwitchOff-F:UGC-Storytime-C1H3-V2Person-Students`, `…-V3Setting-Students`, `…-V4Bundle-Nurses`, `…-V5Bundle-Students-BR-pt`. Node label: "Final: C1H3 · V4 nurses".

---

## Common mistakes (audience variations)

| Mistake | Prevention |
|---|---|
| Versions invented without reading the Brand Kit's audience | Variation map from the kit's segments; hypotheses to confirm when the kit has none |
| A version as a demographic label ("woman 35") | Start from the segment's life, derive every layer from it |
| Several layers changed in a "test" | Mode A: one layer; more is a mode B version, named as one |
| The message or angle changed "while we're at it" | Line audit; more than identity-bound words → the multiplier |
| The nurse still says "between lectures" | Line audit in mode B |
| A student in a premium car, a 55-year-old with a young voice | One-story test across all layers |
| A change too small to read (a shirt color) | The tested difference reads at thumbnail size in the first second |
| The original edited instead of a variation | Original untouched as Main, the control; `create_variation` per version |
| A variation copied from another version | Always copy from the original |
| Everything rerun, credits spent on unchanged nodes | Layer map: rerun only the nodes that carry the changed layer |
| One node left with the old person, outfit or room | `get_workflow` on the variation and search every prompt for the old value |
| Traces of the old face, room or car in a swapped frame | Portrait first; "change only…" at the start; bleed check |
| Portrait posed, glossy, looking away, or with text | Character Generation rules |
| Logos on the car, hoodie or laptop; readable signs | No third-party brands; generic objects, no text |
| The phone screen changed with the world | The screen is always the user's screenshot, identical in every version |
| A new version brings a new claim | Claims identical across versions, from the Brand Kit only |
| Stereotype, caricature, accent or status as a joke, a minor speaking | Casting and brand safety rules |
| "Are you over 40?" in the hook | First person about their own life; situation callouts only |
| A competitor's video used as the source | `lyra-copy-competitor-ad` |

## Quality gates (audience variations)

- **Stage 0 (variation map and sheet; Claude checks before sending):** every version tied to a segment from the Brand Kit (or a confirmed hypothesis) and a one-line hypothesis? Mode and layers named per version, one layer in mode A? World cards complete, voice anchors included? Lock list written? Line audit done for mode B and new languages, only identity-bound words changed, word counts within about ±10%, same claims? One-story test passed? No personal-attribute callouts, no brands, casting respectful?
- **Stage 1 (images):** the tested difference reads in one glance at thumbnail size? Everything else the same as the original (mode A)? The person and world read as the segment (mode B)? Portraits natural, imperfect, looking into the camera, no text? No bleed? Hands, phone and screen right (the screen identical to the screenshot)? No logos or readable text? Phone-real, not glossier than V1?
- **Stage 2 (clips):** voice fits the face, age and market? Lip-sync right, app name pronounced right? Beats and timing match the original (about ±0.5 s)? Same camera behaviour? Person and world stable through the cuts? If [Video1] was used: no trace of the old person or place?
- **Stage 3 (finals), side by side with the original:** only the intended differences visible? Captions match the new words? Same music, CTA and end card? 9:16, the original's resolution, planned length? Named with its V code? AI label reminder given?

## After the test

- Launch the control and the versions the same day, with the same setup and budget, so only the visible world differs.
- Read: hook rate first (the visible world decides the first second), then hold rate, CTR, cost per trial and payers. Then the age, gender and country breakdowns in Ads Manager: did each version pull the segment it was made for? A version that wins its segment but loses overall is still a result: a segment ad.
- The learning is the layer: person, wardrobe, setting, prop, time, market or voice. The next round pushes the winning layer further, combines winning layers into one audience version, or keeps the winning world and tests new hooks (`lyra-video-hooks`) or new angles (`lyra-ad-concept-multiplier`) in it. A winning person can become the campaign's recurring face.
- Save to the project's creative repository: version, layers changed, segment, hypothesis, result.
