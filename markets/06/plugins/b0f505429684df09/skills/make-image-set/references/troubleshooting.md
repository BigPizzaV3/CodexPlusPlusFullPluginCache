# When it comes back wrong

Regenerate rather than salvage. These all cost one generation; a bad set
costs the user's trust in the plugin.

## It is one big picture, not a grid

Regenerate. The layout clause is the first thing in the prompt for a
reason — check it survived, and that the grid and total agree.

## The cell count is wrong

Two causes, in order of likelihood:

1. **A number in the AXIS.** "nine chaotic spells" in the theme makes the
   model expand the grid to fit the theme. The count belongs to the layout
   clause only.
2. **The model ignored the layout.** Build a reference lattice and attach
   it, so image and text reinforce each other:

   ```
   python3 scripts/make_primer.py --grid 4x4 --out primer.png
   ```

   Then add: *"The reference image is laid out as a 4×4 grid of 16 cells —
   produce your output in that exact same layout."* This is the escape
   hatch, not the default; the gaps usually make it unnecessary.

## The subjects are touching, or the gaps vanished

The cutter falls back to grid slicing and needs `--grid`. Ask for wider
gaps and regenerate — a set cut on a rigid grid is only as good as the
model's alignment.

## Every subject has a white outline

The prompt's negation clause is missing or got shortened, **or** a format
word reached the model. Check SUBJECT: "a sticker pack of my dog" must
become `my dog`. A subject alone on a flat uniform field is the die-cut
prior, so the negation has to be present in both modes.

## The canvas came back non-square

The script says so. Subjects found in gaps are cut on their own bounds, so
a non-square canvas is survivable — but the images will be framed
inconsistently. Regenerate with `size="1024x1024"` passed explicitly.

## Transparency was asked for but did not happen

The script reports which route it took. If the sheet came back opaque with
no green to key, it says so and keeps the background rather than damaging
the image. Regenerate; if it fails twice, fall back to the green-screen
route by appending:

> Render the subject on a FLAT, UNIFORM, solid chroma-key green (#00FF00)
> background — perfectly even, no gradients, no shadows cast onto the
> background, no vignette. Keep that green OUT of the subject itself.

The cutter detects and keys that automatically. Nothing in the subject may
be green — including teal, lime and mint, which key half-way and read as a
rendering fault.

## Some cells are good and some are not

`--keep 0,2,3,5,8` keeps the good ones. A pack needs at least 3.
