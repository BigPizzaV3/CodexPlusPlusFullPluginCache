---
name: scene-to-video
description: >-
  Generate cinematic multi-shot video prompts (Kling or Seedance 2.0/2.5) from a script scene and reference images. Use this skill whenever the user provides a script or scene description and wants video prompts generated from it — especially when they also upload reference images showing characters, environments, or visual style. Trigger when the user says things like "make a video prompt from this scene", "create shots for this script", "Seedance prompt for this", "Kling prompt for this", or uploads images alongside a scene description expecting video output. Also trigger when the user pastes a script excerpt and asks for cinematic shots, a shot list with video prompts, or multi-shot sequences. This skill is specifically for script-driven, image-referenced video prompt generation — not general video prompts from scratch (use video-prompt-builder for that). NOTE: a script with NO reference images is context-loading only — do not generate prompts yet.
---

# Scene-to-Video Prompt Builder

> ## ⛔ HARD GATE — READ FIRST, NO EXCEPTIONS
> Before producing ANY shot prompt, both conditions must be true. If either fails, STOP and ask.
>
> **GATE 1 — Phase check.** A script, screenplay, or narrative document by itself is **Phase 1 (context loading) ONLY**. When the user sends a script, do NOT generate shot prompts. Acknowledge that context is loaded, then wait for individual scenes.
>
> **GATE 2 — Reference images required.** Do NOT generate prompts unless reference images are attached to the scene. **No frames = no prompts.** A scene's text alone is not enough.
>
> **GATE 3 — Never invent visuals.** Every visual detail of a character or environment (hair, skin, beard, scars, clothing, build, architecture, color, lighting) MUST come from an attached reference image. If a detail is not visible in a frame, do NOT write it. Inventing canon is the #1 failure of this skill — it is forbidden.
>
> **If no images are attached:** reply that the script context is loaded, then ask the user to send the scene WITH its reference frames. Then stop. Do not draft, preview, or "show what it might look like."

Generate cinematic multi-shot video prompts from a script scene and reference images. The user provides a script for narrative context, then feeds you scenes (often with reference images) one at a time. Each output is a self-contained video prompt ready for AI video generation.

## Workflow

The user operates in two phases:

### Phase 1: Context Loading
The user shares a script, screenplay, or narrative document. This is your story bible. Absorb the characters, setting, tone, emotional arc, and visual world. **You won't generate prompts yet — you're building context.** Confirm the context is loaded and wait for the user to send a scene with reference images.

### Phase 2: Scene-by-Scene Prompts
The user sends individual scenes — usually a paragraph or two of script text, **accompanied by reference images**. For each scene, generate a multi-shot video prompt. If a scene arrives without reference images, do not generate — ask for the frames first (see Hard Gate above).

Reference images lock in the visual look. When the user uploads an image of a character, that face, skin texture, costume, and lighting become canon. When they upload an environment, that architecture, color palette, and atmosphere become canon. Describe what you see in the images — don't invent details that contradict them, and don't invent details that aren't there at all.

## Choosing the Format: Kling vs. Seedance 2.0

Two target engines, two very different prompt structures:

- **Kling format** — the compact timestamped shot-list below. Use it when the user asks for Kling, or when they don't name an engine (this is the established default in Victor's workflow).
- **Seedance format (2.0 / 2.5)** — the long-form sectioned director's treatment. Use it whenever the user asks for Seedance. See the "Seedance Format (2.0 / 2.5)" section further down, and read `references/seedance-examples.md` before writing your first Seedance prompt of a session.

Everything in the Hard Gate, Workflow, and Standing Workflow Rules applies to both formats.

---

## Kling Format

Each prompt is either a **multi-shot sequence** or a **single shot**, depending on what the scene needs or what the user requests.

### Multi-Shot Format

```
**SHOT N (timestamp) — Shot Description**
Effect/speed info. What happens visually — subject, action, camera behavior, lighting, atmosphere. Concise but specific. Every sentence earns its place.
```

### Single-Shot Format

When the user requests a single shot (or the scene calls for it — a single powerful moment, a held composition, a contained action), output one continuous shot of 5–15 seconds. Single shots must have dynamic internal life — the camera and the action both move. Describe the camera's journey through the shot (e.g., starts wide tracking, pushes into close-up, orbits around the subject). Describe how the action evolves across the duration (e.g., a charge that builds, a collapse that unfolds). Speed ramps, focus shifts, and camera transitions within the single shot keep it cinematic. A single shot is not a static hold — it is a miniature film with a beginning, middle, and end inside one unbroken take.

```
**SINGLE SHOT (0:00–0:XX) — Description**
Duration, effects, speed. The full visual journey — what the camera does, what the subject does, how both evolve across the shot. Camera movement and action movement described together, beat by beat.
```

### Kling Output Rules

- **Up to 5 shots per sequence** (or 1 for single-shot mode) — could be 2, could be 5. Let the scene dictate. A slow, dramatic moment might need one 8-second shot and one 7-second shot. A fast action sequence might need 5 quick cuts.
- **Up to 15 seconds total duration** — again, context-driven. A quiet scene might be 10 seconds. An intense sequence might push to 15.
- **Shot duration follows the scene's rhythm** — slow, dramatic, contemplative scenes call for longer holds (5–8 seconds per shot). Fast, kinetic, action-driven scenes call for shorter cuts (3 seconds). Don't force quick cuts on a scene that needs to breathe, and don't force long holds on a scene that needs pace.
- **Under 2100 characters total** — this is a hard ceiling for Kling prompts. Count the characters before delivering; if the draft runs over, cut detail until it fits rather than shipping it long. The prompts must be tight and dense, not sprawling. Every word must pull its weight. (This ceiling does NOT apply to Seedance prompts.)
- **Shot composition follows the scene's needs** — for dramatic, emotional, or sacred scenes, favor close-ups and ECUs to capture texture, expression, and intimacy. For action, battle, or high-energy scenes, favor dynamic wides, tracking shots, and faster pacing over close-up detail. Read the scene's energy and match the composition to it.
- **One SIGNATURE SHOT per sequence** — mark it. This is the image the audience remembers.
- **Slow-motion is the primary tool for dramatic scenes** — specify percentages (e.g., "slow-motion 15%"). Range from 10% (deepest, for signature moments) to 30% (standard cinematic slow). For action scenes, use speed ramps and normal speed more liberally — not everything needs to be slow.
- **No hype language** — no "stunning", "breathtaking", "incredible". Describe what happens. The visuals speak.
- **Transitions between shots** — note how each shot exits (hard cut, dissolve, bloom flash, etc.)

### Shot Header Format

Keep headers compact:
```
**SHOT 1 (0:00–0:03) — ECU: Description**
```

Types: ECU (extreme close-up), CLOSE-UP, WIDE, HERO (final shot).

### Kling Example

**User provides:** A scene description about an ox being led to a sacrificial altar, plus reference images showing the environment and characters.

**Output:**

**SHOT 1 (0:00–0:03) — WIDE: The Ox Approaching**
Slow-motion 25%, static hold. A massive ox led forward — dark hide, muscular shoulders. The stone altar ahead, rough-hewn, stained with offerings. Dust rises from each hoofstep. Priests in white linen flanking. The ox walks without resistance. Head low — not defeat, calm.

**SHOT 2 (0:03–0:06) — ECU: The Ox's Eye**
Slow-motion 15%, static hold. Shallow depth of field. The eye fills the frame — large, dark, wet, reflecting the altar. No panic. Lashes blink once at 15% speed. The reflection shifts as the priest draws closer.

**SHOT 3 (0:06–0:09) — CLOSE-UP: Priest's Hand on the Head**
Slow-motion 20%, static hold. Weathered hand rests on the broad plane between the ox's ears. Fingers settle into coarse dark hair. A blessing. The ox does not flinch. Warm sunlight catches the white linen sleeve.

**SHOT 4 (0:09–0:12) — ECU: The Ox Breathing**
Slow-motion 10%. Ribcage filling the frame. Ribs expand slowly, hide stretching. A pause at the top. Then release — ribs contracting, faint dust cloud from the hide. SIGNATURE SHOT. Sacred surrender in a single breath.

**SHOT 5 (0:12–0:15) — WIDE: The Moment Before**
Slow-motion 20% + glacial dolly push-in. Full composition — ox at the altar, priest's hand on its head, white-robed figures. Stone altar solid. Smoke curling upward. The dolly narrows on the hand and the head. Cut to black.

Note: this example is ~1500 characters. Room to add detail, but the ceiling is 2100. Stay under it. **Note also: this example only works because the user supplied reference images. With no frames, none of these visual details could be written.**

---

## Seedance Format (2.0 / 2.5)

When the user asks for Seedance, switch to this structure entirely. The structure is identical for 2.0 and 2.5 — only the duration ceiling differs (see "Duration — 2.0 vs. 2.5" below). A Seedance prompt is a **long-form director's treatment** in plain text with ALL-CAPS section headers — no markdown shot headers, no timestamped shot list, no character ceiling. Prompts typically run 3,000–6,000+ characters. Before writing your first Seedance prompt of a session, read `references/seedance-examples.md` — three gold-standard examples that carry the exact tone and density.

### Duration — 2.0 vs. 2.5

The engine version sets the ceiling. Ask which version if it matters and the user hasn't said; default to 2.0 when there's no signal.

- **Seedance 2.0 — maximum 15 seconds.** Never write a treatment whose beats can't play inside 15 seconds.
- **Seedance 2.5 — maximum 30 seconds.** Only go past 20 seconds when the user explicitly asks for that length.
- **No duration given by the user** — let the action decide. Write the beat at the length it actually needs to land, nothing padded to fill a ceiling. A single held moment might be 6 seconds; a multi-cut sequence might be 12. On 2.5 with no stated duration, treat **20 seconds** as the working ceiling.
- **State the duration** in OUTPUT SETTINGS whenever the beat has a target length, and make sure the CUT count and beat pacing actually add up to it — a 5-cut treatment does not fit in 8 seconds.

### Section Order

Output the sections in this order. Sections marked optional appear only when the scene needs them.

```
SCENE CONTEXT
ACTIVE REFERENCES
LOCATION MAP          (or STAGE — <NAME> when one composition serves multiple cuts)
FIRST FRAME / BLOCKING
FORMAT MODE
CUT 1 … CUT N         (multi-cut mode; omitted in continuous-shot mode)
OPTICS
CAMERA
ACTION                (may merge with PHYSICS as "ACTION & PHYSICS" in action scenes)
PERFORMANCE
PHYSICS
LIGHTING
COLOR GRADE           (optional — when the palette is a feature of the shot)
AUDIO
STYLE
OUTPUT SETTINGS       (optional — aspect ratio, total duration, speed)
POSITIVE LOCKS
```

### What Each Section Does

**SCENE CONTEXT** — 2–4 sentences: where, when, who, and the beat's full arc from first frame to last. A producer reading only this should know exactly what the clip contains.

**ACTIVE REFERENCES** — one entry per reference image, each with a descriptive `@tag` (`@eduardo`, `@parrot_sheet`, `@ocean_location` — snake_case, named for what it is). Each entry contains: (1) a physical description sourced from the frame, (2) the phrase "100% matches the reference", (3) a scope note when the reference should control only part of the image ("controls hull, deck, masts and rigging only", "water and sky atmosphere only", "studio sheet layout NOT inherited" for character sheets), and (4) exactly where and when it appears ("appears ONLY inside the zoomed spyglass view of CUT 3", "on camera only in CUT 2"). Scoping is what stops a character sheet's studio background or a location's full frame from bleeding into the shot.

**LOCATION MAP / STAGE** — the spatial world as a map: what sits screen-left vs. screen-right, distances in real units (meters, km), foreground/midground/background layers, horizon height, sun direction, atmosphere ("haze visible at the horizon distance"). Everything that exists in the world goes here even if the camera reveals it later — the model needs the geography before the choreography. When one exact composition serves multiple cuts, name it as a STAGE ("STAGE — THE RAISED STERN DECK (serves CUTS 1 and 3)") and describe the full frame once; the cuts then reference it.

**FIRST FRAME / BLOCKING** — the literal opening frame: who stands where, mid-what-action, the camera's framing and angle. Seedance weighs the first frame heavily; pin it down completely.

**FORMAT MODE** — one line, verbatim per mode:
- Multi-cut: `Sequence of cuts, no timecodes — cuts only at the specified points, the camera does not cut on its own.`
- Continuous: `One continuous shot, the camera does not cut on its own.`

**CUT 1…N** — each cut opens with framing and lens ("MS, 47°", "SPYGLASS POV, MONOCULAR", "PROJECTILE-FOLLOW, 63°", "HARD CUT into SLOW MOTION"), then the beat-by-beat action: screen directions on every movement, dialogue verbatim in quotes (shouts in CAPS: "HARD A-PORT!"), and how the cut ends. In continuous-shot mode there are no CUT blocks — instead the ACTION section carries timestamped beats ("0.0s to 1.0s, blink one: …").

**OPTICS** — lens FOV in degrees per cut (84° rectilinear wide / 63° observational / 47° neutral / 8° tele compression), depth of field, speed regime (real time vs. slow motion — **speed changes only on hard cuts**, never mid-segment), special optics (monocular POV, anamorphic character). End with "No drift mid-segment." when framing must hold.

**CAMERA** — the operator as a character: handheld vs. rigid mount, shake and sway amplitudes in centimeters ("2–3 cm shake", "a 1–2 cm breath"), where the camera sits relative to the light ("camera stays on the shadow side"), and how its behavior changes across the beat ("the sway stops dead when focus lands").

**ACTION** — the physical choreography with real numbers: speeds ("covering the deck at 10 km/h"), gaits, hand-offs, which hand does what. In heavy action scenes this may merge with physics as ACTION & PHYSICS.

**PERFORMANCE** — face and emotion, beat by beat: what the eyes, jaw, breath do. Close with realism anchors: "Pore-level skin realism, sun catch-lights" (adapt to the scene — spray-damp sheen, water beading through grime).

**PHYSICS** — mass and material truth: ships displace tonnage, birds compress shoulders on landing, cloth soaks and clings, splinters fly ballistically, silk strands dip under a spider's weight. This section is what keeps Seedance output from floating.

**LIGHTING** — sun position as a screen direction, color temperature in Kelvin (5600K daylight), key/fill logic, atmosphere density as percentages ("powder smoke 20% on the enemy deck, 40% by CUT 3"), and which color reads as the frame's saturated accent.

**COLOR GRADE** (optional) — the palette in one paragraph: dominant hues, where they live, and the single sharpest color accent.

**AUDIO** — sound design per cut: ambience, hard effects, and every dialogue line repeated verbatim exactly as written in the cuts. Note silences and transitions ("the world's sound thins to wind"). If a character says nothing, say so ("No spoken line from Eduardo.").

**Every AUDIO section MUST end with an explicit no-music line.** Seedance scores the clip by default — it lays a generic orchestral or ambient music bed under the output, and that bed buries the sound design you just specified. A prompt that does not forbid music will come back with music. Close the section with a sentence of this shape, adapted to the scene:

> NO MUSIC of any kind — no score, no soundtrack, no orchestral bed, no ambient pads, no drones, no percussion, no melodic or tonal instrumentation anywhere in the clip. Diegetic sound only: [list what the frame actually contains — wind, fire, footfalls, breath, iron, water].

Two things make this hold. Name the forbidden thing in several forms — "music", "score", "soundtrack", "pads", "drone", "instrumentation" — because forbidding only "music" leaves the model free to add a swell it does not classify as music. And say positively what the audio bed IS ("diegetic sound only", then the actual list), since a purely negative instruction leaves the bed undefined and the model fills it. If the scene calls for a designed non-melodic element — a rising sub-bass under a reveal, a single sustained tone — name it as a sound-design element and say it is non-melodic and non-instrumental, or the model will hear permission for a score.

**STYLE** — one line: "Photoreal live-action, [scene's light character], fine film grain, crisp highlights, 8K master." Adjust to the project's look; keep it short.

**OUTPUT SETTINGS** (optional) — aspect ratio, total duration, speed ("21:9 aspect ratio, 5 seconds total, real-time"). Keep the duration inside the engine's ceiling: 15 seconds on Seedance 2.0, 30 on 2.5 (20 unless the user asked for more). See "Duration — 2.0 vs. 2.5" above.

**POSITIVE LOCKS** — the constraint wall that closes every prompt. Restate every consistency-critical fact as a standing rule: wardrobe details, screen-direction assignments, who touches what ("HANDS LOCK: only the helmsman touches the wheel"), frame-size limits ("under 5% of the frame height"), where each reference may and may not appear, count limits ("Only two ships exist", "Exactly five waking blinks"), and named locks for the fragile stuff (STAGE LOCK, FLIGHT LOCK). Always end with the invariants: "Same sun direction, same wardrobe in every cut. Cuts only at the specified points." (or "One continuous shot with no cuts."). Phrase locks positively where possible — say what IS true ("the spyglass stays lowered in his right hand") rather than only what isn't.

### Seedance Craft Rules

- **Screen-direction discipline.** Every position, movement, and glance gets an explicit direction: screen-left/right, LEFT/RIGHT hand and shoulder, frame corners, frame-height percentages. Ambiguity is the enemy — anything unlocked can mirror-flip between frames.
- **Redundancy is a feature, not a flaw.** Critical constraints appear three times: in the LOCATION MAP (the world), in the CUT (the moment), and in POSITIVE LOCKS (the rule). Kling wants density; Seedance wants explicit repetition. Do not "tighten" a Seedance prompt by deduplicating its locks.
- **Numbers over adjectives.** Lens FOV in degrees, camera sway in cm, distances in meters/km, speeds in km/h, temperatures in Kelvin, sizes as % of frame height, smoke as % density, beats in seconds. Every number replaces a paragraph of ambiguity.
- **Distance vs. focus vs. size.** When something must stay the same size in frame, say all three: distance constant, frame size constant, only focus changes. The model conflates them unless separated.
- **Speed changes only on hard cuts.** A cut is either real time or slow motion start-to-finish. Announce slow motion in the cut header ("HARD CUT into SLOW MOTION").
- **Dialogue lives twice.** Verbatim in the CUT where it's spoken, and verbatim again in AUDIO. Shouts in CAPS.
- **Never leave music unforbidden.** Seedance adds a music bed unless told not to, and that bed ruins the SFX. Every AUDIO section ends with an explicit multi-form no-music line plus a positive statement of what the bed is (diegetic sound only, then the list). Restate it in POSITIVE LOCKS as a NO MUSIC LOCK — this is one of the constraints that genuinely needs saying twice.
- **No character ceiling.** The Kling 2100-character limit does not apply. A Seedance prompt earns its length — but every sentence must still be doing work. No hype language here either: describe what happens, never how amazing it looks.
- **Reference scoping prevents bleed.** Character sheets: "sheet layout NOT inherited." Locations used only for atmosphere: "controls water and sky atmosphere only." Objects that exist in only one cut: say so in ACTIVE REFERENCES and again in POSITIVE LOCKS.

### Moderation-Safe Phrasing

Video engines run safety classifiers over the WHOLE prompt, not just quoted dialogue — and they trigger on grammar and framing, not on a keyword blacklist. A prompt can be rejected while containing nothing you'd consider objectionable. When a beat involves danger, death, sacrifice, violence or self-endangerment, write it so the classifier reads craft rather than intent.

- **Imperatives requesting harm are the highest-risk pattern.** First person + imperative to another person + a lethal action reads as solicited self-harm regardless of source material. "Pick me up and throw me into the sea" trips; "Let the sea have me" usually clears; splitting the line so the request is never spoken clears best. Give agency to the environment or to fate instead of to a person.
- **Split dialogue across cuts when a line is the problem.** Have the character speak the safe fragments on camera and carry the risky clause as an off-screen reaction shot the user can voice in post. Write that cut with an explicit silence lock and a clean audio bed, and say so in AUDIO ("NO VOICES AT ALL — the audio bed stays clear of dialogue").
- **Sanitize the prose around the line too.** Phrases like "destroying themselves", "backs breaking", "tearing themselves apart", "no one is killed" feed the same classifier as the dialogue. Replace them with physical craft description: "spending everything they have", "backs bent to the looms", "every man stays on his bench".
- **Say each risky idea once.** If the same phrase appears in SCENE CONTEXT, in the CUT and again in AUDIO, you have tripled its weight for no benefit. State it in the cut where it happens.
- **Never name a forbidden thing in a lock.** "No ship's wheel" plants the token; describing the stern positively ("steered by her two side steering oars, one sailor at each loom") removes it. This applies to anachronisms, weapons, injuries and deaths alike — write what IS in frame.
- **Watch verbs that smuggle nouns.** "The sail wheels past" reintroduced a banned object in a prompt whose locks forbade it. Read the draft once hunting for the banned word in any grammatical form.

### The Locks Library

POSITIVE LOCKS is where most failures get fixed. Beyond the wardrobe and screen-direction basics, these named locks earn their place because each one corresponds to a failure mode models reliably produce. Use the ones a beat needs; name them in caps so they read as rules.

- **TAKE LOCK** — for single-shot beats: one continuous take, every phase inside one unbroken camera move, and any flash or light event named as a light event inside the take rather than an edit.
- **ORBIT LOCK** — arcs need degrees, radius, height, duration and direction ("a 180° arc, front-left to front-right, constant 2 m radius, chest height, over 4 seconds"). Without numbers, models substitute a zoom or a pan.
- **FACE LOCK** — an expression change needs its own protected beat with nothing else happening in frame, and it must complete BEFORE any camera move begins. Expression changes buried under a move get skipped entirely.
- **SPACING LOCK** — groups render as huddles unless separation is explicit: clear ground visible between every pair, nobody touching, leaning on or embracing, staggered at different depths.
- **DISTINCT LOCK** — crowds render as clones. Give each background figure a different age, build, hairline, facial hair and one distinguishing item, then restate the roster in the lock.
- **OFF-FRAME LOCK** — when a character is deliberately out of frame, say it absolutely: not in frame, not in the background, no silhouette, no reflection, and the camera never pans or tilts toward them.
- **SILENCE LOCK** — for reaction shots: no man speaks and no mouth forms words — no lip movement, no mouthed syllables — and the audio bed carries ambience alone.
- **NO MUSIC LOCK** — required in every prompt, no exceptions. Seedance scores the clip by default and the score buries the sound design. Forbid the thing in several forms and then state what the bed is: "NO MUSIC LOCK: no music, score, soundtrack, orchestral bed, ambient pad, drone, percussion or melodic instrumentation of any kind exists in this clip. The audio bed is diegetic sound only — [the scene's actual sources]." If a designed sub-bass or sustained tone is wanted, name it here as non-melodic sound design so it does not read as licence for a score.
- **AFLOAT LOCK** — vessels in heavy weather sink unless forbidden to: whole, upright, floating high in every frame, never listing past a stated angle, never burying bow or stern, never taking water over the rail, not holed or dismasted.
- **ORDER LOCK** — when beats must happen in sequence inside one cut, list them and say "in that order, nothing skipped and nothing reordered".
- **SETTLING LOCK vs INSTANT LOCK** — weather changes need one or the other named explicitly. Gradual: name the visible stages it must pass through. Instant: one single frame, no dissolve, no fade, no morph, with camera shake stopping on the same frame.
- **SHEET LOCK** — every reference built as a character sheet or annotated prop sheet needs its layout disowned: three views, grey backdrop, name titling, callout lines, arrows, scale bars and annotation text NOT inherited — only the single living subject or object exists in the scene.

---

## Writing the Prompts (both formats)

### What Makes These Prompts Work

The prompts are **director's notes**, not prose poetry. They read like a cinematographer describing exactly what the camera sees, what the light does, and how time behaves. The tone is direct, technical, and confident.

**Specificity over vagueness:**
- "Slow-motion 15%" not "slow motion"
- "Dolly push-in" not "camera moves closer"
- "Shallow depth of field — face sharp, background collapsed into golden bokeh" not "blurry background"
- "Dust ejects in tiny plumes catching throne-light" not "dust in the air"

**Physical detail grounds the sacred:**
When describing characters, environments, or objects, anchor in tactile, physical detail — skin texture, fabric weight, stone grain, feather barbs, dust particles. The more grounded the physical description, the more powerful the spiritual or emotional weight becomes. (Source these details from the reference frames, not your imagination.)

**Contrast drives impact:**
Alternate between intimate and wide, between stillness and motion, between silence and force. A static hold after a dolly push-in. A deep slow-motion ECU after a wide establishing shot. The contrast is what creates the feeling.

**The hero shot earns its place:**
The final shot is typically the most compositionally complete — often the widest, pulling together the elements the previous shots established in detail. It works because the earlier shots gave the audience context. But this isn't a rigid rule — if the scene calls for ending on an intimate close-up, do that. Let the scene's emotional logic decide what the final frame should be.

### Camera and Effects Vocabulary

Use these terms precisely:

**Speed:** slow-motion [percentage] (Kling) / real time vs. slow motion per cut (Seedance), speed ramp (acceleration/deceleration)
**Camera:** static hold, dolly push-in, dolly pull-back, tilt-up/down, tracking, orbital drift, crane, handheld follow, rigid chase mount, projectile-follow
**Focus:** rack focus, shallow depth of field, crash zoom (optical)
**Light:** bloom flash, light intensification, rim-light, god-rays, volumetric light
**Transitions:** hard cut, dissolve, fade to black/white, bloom flash entry

### Reading Reference Images

When the user uploads images:
1. Study the visual details — skin texture, costume, lighting direction, color palette, environment architecture
2. Carry these details into your prompts verbatim — if the image shows weathered olive skin, say "weathered olive skin," not "dark skin"
3. Note lighting setups — where is the key light, what color temperature, what quality (hard/soft)
4. Note the color grade — warm gold, cool blue, desaturated, high contrast
5. These details become canon for all subsequent prompts in the session until the user provides new references

### Character Descriptions from Reference Images

When the user uploads reference images of characters, build a short visual description **from what you see in the image** and use that description in the prompts. Keep the description consistent across all prompts in the session. **Do not describe a character whose appearance you have not seen in a reference image.**

### Tags

**Both formats use the same convention: descriptive snake_case @tags.** Every reference image gets a tag named for what it actually is — `@eduardo`, `@altar_location`, `@ox_sheet`, `@elisha` — and that tag is used consistently across every prompt in the session. Never use generic numbered tags (`@Element1`, `@Element2`); a reader should know what a tag points to from the tag alone.

- **Seedance** — declare each tag in ACTIVE REFERENCES with its description and scope, then use it through every section.
- **Kling** — introduce the tag with a short visual description on its first appearance in a sequence, then use the bare tag on later mentions to save characters against the 2100 ceiling.

## Standing Workflow Rules (Victor's preferences)

These apply to **both formats**.

1. **Full script in every answer** — every response containing a video prompt must include the complete episode script at the top of the answer, with a "**← YOU ARE HERE**" marker on the script line the current frame covers, so the user never has to scroll up to check what comes next.
2. **One prompt per image** — when multiple reference images arrive in one message, output a separate self-contained prompt for each image, in story order.
3. **Follow explicit shot instructions exactly** — when the user specifies shots ("shot 1 X, shot 2 Y…"), build precisely those shots in that order. Do not add, remove, or reorder shots.
4. **Tone: dramatic and cinematic** — heavy emotional weight, sadness, strong feelings. Favor slow-motion, close-ups, and dramatic light. Match the script's mood beat by beat.
5. **Descriptive @tags everywhere** — every reference image gets a snake_case tag named for its subject (`@elisha`, `@altar_location`), used identically in Kling and Seedance prompts. Describe every character from what is visible in the reference frames.
6. **Include dialogue** — when the scene covers script dialogue, write the line into the relevant shot verbatim, attributed to the speaker. (In Seedance: verbatim in the CUT and again in AUDIO.)
7. **Transitions as tools** — use creative in-camera transitions: dip-to-black through a body walking into the lens, match cuts for time jumps (e.g., baby's face → same framing six years later), single black-frame stutters as foreshadowing, and SLAM TO BLACK with a sound cue (dull thud, thunderclap) on collapse beats.
