# Writing shot lists

The `prompt` feeds a planner. Each `Shot N: …` entry becomes exactly one shot; the planner preserves your count, order, and intent while adding generation detail. Give every shot a **Visual** (the still frame) and an **Animation** (the movement).

Decide and create the references first (SKILL.md steps 1–2), then write the list around their exact `@Name`s.

**These rules govern shot lists you draft.** For user-supplied lists, preserve the wording — weaving in `@Name`s is the only edit that skips approval.

## Visual — becomes a still image

- Specify concrete subjects, objects, and placement. Avoid abstract or mood words (vibrant, breathtaking, symbolic) and style / camera / format words (cinematic, teal grade, 35mm). Style lives elsewhere; describe things, not vibes.
- **Every shot must stand alone.** The image model sees one shot with no memory of the others. Re-name and re-describe recurring people and props every time: "@Maria pours a latte", never "she pours" or "the same barista". Repetition is correct.
- **Be prescriptive with references.** The image model knows exactly how to use a reference to `@YourLogo`; it has no idea what "your logo" means. Use the exact library `@Name` every time an entity appears, and never invent an `@Name` that is not in the library.
- Treat a logo as a graphic, not an object: put it on packaging, a sign, or an end-card, and never stand it in the scene like a product.
- **Text in a shot is fine — sparingly, and specified exactly.** The models will happily cover a frame in text if you let them, so keep rendered text to a few words in a few deliberate shots, and prescribe the exact string with its styling and placement: 'An old-fashioned end-card from a silent film that says "Fin." in flowy script in the center, over a rough film-grain black background, with white line accents around the edges of the frame.' A vague ask ("a sign with the company name") invites garbled or rambling text. For spoken words, use narration and let captions render them. "Say it on screen" means text, not dialogue; do not turn it into quoted Animation speech.

## Animation — motion for the clip

- Give each shot one clear motion with matching energy: decisive for action ("the camera whips in as she spins"), subtle for calm ("steam curls off the cup"). Avoid gentle drift on every shot, and avoid chaos in quiet scenes.
- **For on-screen speech, lead the Animation with the exact quoted line**: `"Always add salt," the chef says as he stirs.` Unquoted speech verbs ("the chef explains", "she talks energetically") produce silent mouth movement. Without a line to quote, use silent action instead (gestures, nods, raises a glass).
- Put speed and time effects (slow-motion, time-lapse, freeze-frame) in the Animation, never the Visual — a still image cannot show elapsed time.

## Structure

- Interleave quoted narration between shots where the voiceover should land. Never repeat on-screen dialogue as voiceover.
- **Give every shot an explicit duration label** — `Shot 2 (3s):` — never shorter than 3 seconds.
- Size each to its content: 3s for a quick cut, longer where dialogue or action needs room.
- Preserve explicit user timing (`(5s)` labels, timecodes, or qualitative timing words) when given.
- After creation, ask for pacing changes in words ("quick cuts on shots 1–3, let shot 4 linger") because narration can refit durations.

## Worked example

User has library character `@Maria`, reference object `@Fresco Bag`, and wants a short café ad.

```
Shot 1 (4s): Visual: @Maria steams milk behind a sunlit café counter, @Fresco Bag on the
shelf beside the espresso machine. Animation: "This is how mornings should start,"
she says, swirling the milk pitcher.

Narration: "Small-batch. Roasted this week."

Shot 2 (3s): Visual: A white ceramic cup with tulip latte art on a wooden counter,
@Fresco Bag standing behind it. Animation: Steam curls slowly off the cup.

Shot 3 (5s): Visual: @Maria hands a to-go cup across the counter to a customer in a
denim jacket. Animation: "See you tomorrow," she says with a nod as the customer
turns to leave.

Shot 4 (5s): Visual: @Fresco Bag centered on a rustic wooden shelf between two potted
coffee plants. Animation: The camera pushes in slowly toward the bag.

Narration: "Fresco Coffee — small batches, roasted weekly."
```

Why it works: each shot re-names its subjects and stands alone; exact `@Name`s mark every entity appearance; quoted speech leads the Animation; silent shots still move; there are no style words; narration is interleaved, not duplicated; every shot carries an explicit duration sized to its content.
