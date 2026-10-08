# GIFgen Sticker Maker — skills-only plugin

Separate plugin, same brand. `gifgen-local` makes GIFs; this makes **a set
of images of one subject** from a single generation.

Listed as **GifGen - Sticker Maker**. The word "sticker" is everywhere a
person reads, and nowhere the image model does.

```
plugin.json                                manifest — no mcp.json, no server
scripts/check_prompts.py                   repo-side guard, not shipped behaviour
skills/
  make-image-set/
    SKILL.md                               when, the four steps, delivery
    references/prompt-template.md          the prompt, both modes, axis presets
    references/troubleshooting.md          what each failure means
    scripts/detect.py                      find the subjects
    scripts/sheet_to_set.py                cut them out
    scripts/make_primer.py                 escape hatch for a stubborn grid
  remove-green/
    SKILL.md                               key an image the user already has
    scripts/green_to_alpha.py
```

## The design, in one idea

**Ask for wide transparent gaps, then find the subjects instead of slicing
a grid.**

Everything else follows. Gaps make each image its own island of alpha, so
`detect.py` labels the islands and cuts each on its own bounds. The layout
can drift, the canvas can come back the wrong shape, the gaps can be
uneven — none of it matters, because nothing is measured against an assumed
lattice. Grid slicing survives only as the fallback for an opaque sheet
whose subjects touch.

This replaced a much harder approach: demand an edge-to-edge grid with no
gutters, pin it with a reference lattice image, then divide the canvas.
That inheritance came from the GIF pipeline, where frames genuinely must
tile. For separate images it bought nothing and cost alignment.

The prompt went from 213 words to 83 in the same change.

## The three failures this prevents

**The white outline.** Image models draw a die-cut keyline around a subject
sitting alone on a flat uniform background. It is a visual prior, not a
vocabulary problem — it appears with no prompting at all. The prompt
negates it explicitly in both modes.

It also leaked through a slot once. The skill used to say *"SUBJECT carries
the user's words through"*, so "a sticker pack of my dog" put the word
straight into the prompt, past a ban covering only the template. SUBJECT is
now what the thing **is**, format words stripped, the rest verbatim.
`scripts/check_prompts.py` asserts this across every `>` line of every
markdown file under `skills/`, and is negation-aware: "no labels" passes,
"a sticker of a dog" fails.

**The wrong cell count.** A number in the AXIS makes the model resize the
grid to fit the theme, so the count lives in the layout clause only — the
rule the repo already learned once. `make_primer.py` builds a reference
lattice for the rare sheet that still will not comply.

**Distorted subjects.** A non-square cell resized straight to 512×512 is
stretched; a 341×512 cell made every circle 50% too wide. Cells are cropped
or padded now, never stretched.

## Backgrounds are a toggle

Default is **keep the background**. Transparency happens only when the user
asks, and then the cutter decides *how* by measuring:

| what the sheet is | what happens |
|---|---|
| came back transparent | used as is — the model cut it out itself |
| opaque and genuinely chroma green | keyed whole-sheet, one shared matte |
| neither | says so, keeps the background, damages nothing |

The green screen is now the **fallback**, not the route. Asking the model
for transparency directly works, so the green directive lives in
`troubleshooting.md` for when it does not.

"Genuinely chroma green" is load-bearing: greenness alone flags grass,
foliage and olive skin, and a scenic test sheet keyed its own lawn away
until the check required a bright green channel too.

## What it writes

`images.zip` — PNGs plus WebP copies under 100KB. A transparent set of 3 to
30 also gets `tray.png` and `contents.json` per
`src/lib/image/whatsapp-pack-spec.ts`, which is what a phone needs to
install the set.

## Submitting

platform.openai.com/plugins → **Skills only** → upload this file tree. No
server URL, no domain verification.

Package name is **`gifgen-stickers`** and must stay that way — the portal
locked it at the first upload and rejects any ZIP whose `name` differs. Do
not "tidy" it to match the display name.

**Listing copy** lives in `COPY.md` — drafted, awaiting the owner's sign-off.
