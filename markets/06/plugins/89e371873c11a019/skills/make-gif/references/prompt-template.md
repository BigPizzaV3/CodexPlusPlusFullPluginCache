# The animation-grid prompt

The canonical shape, matching what GIFgen's own web app generates so GIFs
made in ChatGPT look like GIFs made on gifgen.ai. Source of truth for the
web app is `src/lib/prompts/animation-grid-prompt.ts`; this is the compact
variant tuned for ChatGPT's image generator.

## Template

```
A SQUARE image containing a {N}×{N} grid of {TOTAL} panels of {SUBJECT}{, {STYLE} style}, each panel
showing the same subject at a slightly later moment of motion. The {TOTAL}
panels form one looping cycle (panel {TOTAL} returns to panel 1). Identical
subject, camera, lighting in every panel. All panels are exactly the same size, tiled edge to edge with no gaps,
margins or gutters — the image divides evenly into equal columns and rows. No text,
no numbers, no borders.{ Motion: {MOTION}.}
```

| grid_size | N | TOTAL | character |
|---|---|---|---|
| `3x3` | 3 | 9 | sharpest per frame |
| `4x4` | 4 | 16 | **default** — balanced |
| `5x5` | 5 | 25 | smoothest motion |

Always `size="1024x1024"`.

## Worked examples

**Bare concept, nothing else given**

User: *"make me a gif of a fox jumping over a log"*

```
A SQUARE image containing a 4×4 grid of 16 panels of a fox jumping over a log, each panel showing the
same subject at a slightly later moment of motion. Consecutive panels differ
only slightly, so the motion advances in small, even steps and the whole grid
reads as one continuous action rather than separate poses. The 16 panels form
one looping cycle (panel 16 returns to panel 1). Identical subject, camera,
lighting in every panel. All panels are exactly the same size, tiled edge to edge with no gaps,
margins or gutters — the image divides evenly into equal columns and rows. No text, no numbers, no
borders.
```

**With style and motion**

User: *"animated logo for a coffee shop called Drift, steam curling up, flat
vector, make it smooth"*

```
A SQUARE image containing a 5×5 grid of 25 panels of a coffee shop logo for "Drift", flat vector style,
each panel showing the same subject at a slightly later moment of motion.
Consecutive panels differ only slightly, so the motion advances in small, even
steps and the whole grid reads as one continuous action rather than separate
poses. The 25 panels form one looping cycle (panel 25 returns to panel 1). Identical
subject, camera, lighting in every panel. All panels are exactly the same size, tiled edge to edge with no gaps,
margins or gutters — the image divides evenly into equal columns and rows. No text,
no numbers, no borders. Motion: steam curling upward from the cup.
```

Note the logo's own wordmark is allowed — "no text" governs *labels on the
grid* (panel numbers, captions, watermarks), not lettering that is part of
the subject. If a subject is lettering, say so explicitly in the subject
clause so the constraint is not read as forbidding it.

## Failure modes, and why each rule exists

**Restating the count outside the layout clause.** Writing "16 frames of a
fox" in the subject, or "16 consistent panels" in the style, makes models
hedge the geometry and fall back to 3×3. The count appears exactly once, in
the opening layout clause. Nowhere else.

**Narrowing the subject.** Rewriting "a fox jumping over a log" as "an animal
character" or "characters in motion" loses the thing the user asked for.
Carry their words through.

**Dropping "no text, no numbers, no borders."** Given a grid, image models
add panel numbers, captions, or a title bar remarkably often. Every one of
those is burned into a frame and survives into the GIF.

**Letting the scene drift.** If camera, lighting, or palette change between
panels, playback strobes. "Identical subject, camera, lighting in every
panel" is what makes 16 stills read as one motion.

**Big jumps between panels.** Without the small-even-steps clause, models tend
to produce a handful of distinct poses spread across the grid instead of one
motion sampled evenly. It still looks like the right subject, but it strobes on
playback instead of flowing — the single most common reason a finished GIF feels
wrong rather than broken.

**Gutters between panels.** Any margin becomes a visible border flashing in
every frame. "All panels are exactly the same size, tiled edge to edge with no gaps,
margins or gutters — the image divides evenly into equal columns and rows."

## If a size-agnostic phrasing is needed

When the exact count must be reinforced, a symmetric bound reads better than
a one-sided demand and does not bias the model toward over- or under-filling:

> …produce no more and no fewer than {TOTAL} panels…

Use sparingly, and still only inside the layout clause.
