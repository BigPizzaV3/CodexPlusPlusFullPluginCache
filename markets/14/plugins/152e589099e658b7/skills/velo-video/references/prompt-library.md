# Velo sample prompts

Sample prompts for `message` in `create_video` and `edit_video`. Velo's video creation is intent and outcome driven: it works best from a simple explanation of what the finished video should achieve. Start from that outcome in the user's own words, then customise the closest sample as needed: keep what the user gave, shorten or drop the rest, and never fill a [bracket] with a guess, such as a timestamp, component, emphasis or style the user didn't give.

## For a first video (`create_video`)

### Ground it in real sources

Add this to any brief with screenshots, a document or a connected source:

```text
Use the screenshots I've attached of [feature name] as the real UI. Pull the steps from [our help-centre article, connected], and follow that exact flow. If anything I haven't given you is needed, ask; don't guess the screen.
```

### Product demo

```text
Create a product demo of [product] for [audience, e.g. new trial users]. Use the screenshots I've attached as the real UI, and follow the flow at [URL or connected doc]. In order, show the user: [step 1], [step 2], [step 3], [step 4]. Done when a first-time viewer could repeat all four steps unaided. Emphasise [what to remember, e.g. how little setup it takes]. Keep it jargon-free; if a step isn't in the source, ask rather than invent it.
```

### Support or how-to explainer

```text
Create a support explainer answering exactly: "[the question, e.g. How do I reset my password?]" Show the full path as it appears in [product], grounded in [the help-centre article, connected] and the screenshots I've attached. Spend the most time on the step people get wrong: [the common mistake]. Done when someone stuck could follow along and finish. Stay on this one task only.
```

### Training or onboarding video

```text
Create a training video for [role] on [process], from [doc or recording, connected]. Cover [concept 1], [concept 2], [concept 3], simplest to most involved, each with a real on-screen example. Emphasise [what they must never skip]; call out [the common pitfall]. Assume the viewer is [starting level]. Done when the viewer could carry out [the process] correctly on their first real attempt.
```

### Feature announcement

```text
Announce [new feature] in [product] to [audience], based on [changelog or feature page, connected]. Open on the problem it removes, then show it working with one real on-screen example from the attached screenshots. Make one benefit unmistakable: [the single thing to remember]. One feature, one takeaway.
```

### Style lines

Add a line or two for the style the user named:

- **Narration:** pace ("slow and clear" for training, "brisk" for a short demo); tone (calm, friendly, matter-of-fact or upbeat); address (speak to the viewer as "you", or neutral and descriptive); density (a line per step, or lighter narration that lets the screen do the work).
- **Visuals:** effect intensity ("subtle zooms" or "punchy, obvious emphasis"); cut pace (let each screen breathe, or tight and fast); overlays (heavy on-screen labels and callouts, or clean and minimal); overall feel ("clean and professional", "warm and approachable", "energetic").

## For a change (`edit_video`)

### Focus and emphasis

Bounding box:

```text
When the narration says "[choose the report type]" at [2:23], draw a bounding box around [the "Report type" field]. Size the box to that component's actual height and width, built from its centre with 5px padding so it never overlaps. Thin border, colour #242424, no label text. Show only this one box (remove any previous box first) and time it to that exact narration line.
```

Cursor grounded to the boxes and narration:

```text
Add a cursor that follows the bounding boxes and narration. As each box appears, move the cursor to [the same component] and have it POINT to the component without covering or overlapping it. Keep the movement smooth between components; the cursor is never idle over content it's hiding.
```

Zoom on a named component:

```text
When the narration reaches "[narration line]", zoom to [180%] on [the component], sized from the component's centre so it stays fully in frame, hold while it's discussed, then ease back to 100%. Leave all other zooms exactly as they are.
```

Pan:

```text
From [0:20] to [0:24], pan smoothly from [one component] to [another component], keeping both readable. Don't change the zoom level or anything else.
```

Spotlight, dimming the rest:

```text
When the narration says "[narration line or word]", spotlight [the component] and dim everything else to about [40%], centred on the component, held while it's discussed. Only one spotlight at a time. Change nothing outside that moment.
```

Emphasis pulse:

```text
When the narration says "[narration line or word]", add a single gentle pulse on [the component], anchored on its centre, so it draws the eye without moving anything else. Remove it after the line.
```

### On-screen graphics

Text or title overlay:

```text
At [0:03], add the title "[step 1]" in [the component], held [3s], then fade out. Match the existing title style. Don't move or restyle any other text.
```

Image or logo overlay (add the logo with `upload_file` first):

```text
From [0:00] to [0:05], place [our logo] in the [position] at a small size so it doesn't cover content, kept within that corner. Remove it after. Leave everything else as is.
```

Mask or blur sensitive information:

```text
Wherever [the customer's email and account number] appear on screen, blur them, kept tight to each field. Blur nothing else, and don't blur the opening frames; leave the rest fully visible and unchanged.
```

Motion graphics for a section:

```text
Make [the 0:00-0:06 intro] a motion-graphics sequence: [the logo builds from its own shapes, then the title slides in]. Keep it [clean and on-brand]; leave the screen-recording sections untouched.
```

### Narration

Rewrite the narration's words:

```text
Rewrite the narration for [0:12-0:20]. It currently says "[quote the line]"; change it to convey [the point], in [one short sentence]. Keep all other narration and its timing as it is.
```

Narration tone and pace:

```text
Regenerate the narration for [the intro, 0:00-0:15] in a [calm, matter-of-fact] tone at a [slow] pace, addressing the viewer as "you". Don't make it salesy. Keep the rest unchanged.
```

Narration voice (also pass the chosen voice's ID as `voice_id`; see Voices and avatars):

```text
Change the narration voice for the whole video to [the voice's name]. Keep the script, timing and pacing exactly as they are: voice only.
```

### Captions

```text
Turn on captions for the whole video. Fix the caption reading "[on boarding]" to "[onboarding]", and change nothing else about the captions or their timing.
```

### Structure and timing

Re-time an effect to the narration:

```text
The bounding boxes are landing [2 seconds] before their narration lines. Shift each box so it appears exactly when its line is spoken: for example, the box on [the component] should appear at [2:28], not [2:25]. Keep the boxes and everything else the same; fix the timing only.
```

Trim a dead section:

```text
Remove [the pause between 0:48 and 0:52] where nothing happens. Close the gap cleanly so [the click at 0:47] runs into [the next screen] with no jump. Don't re-time anything else.
```

Change a section's speed:

```text
Speed up [the loading section, 1:02-1:10] to about [2x], keeping the narration in sync. Leave every other section at its current speed.
```

Reorder:

```text
Move [the section, 1:30-1:50] to play right after [the intro]. Keep each section's own narration and edits intact; only change the order.
```
