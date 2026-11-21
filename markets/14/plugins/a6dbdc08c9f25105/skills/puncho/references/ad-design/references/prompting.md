# Prompting parts

From the OpenAI GPT Image guide, Google's Nano Banana Pro guides and Recraft's
prompt guide, adapted to parts that are assembled, not finished ads.

Write every part prompt **in English**, whatever language the brand writes
in. The models are best in English, and Bulgarian is not among Gemini's
best-performing languages. The ad's words are text layers and never in a
prompt anyway.

## Every photographic part

1. **Photography first.** The brand's `photoDirection`, word for word (the tool
   adds it). The same words across parts are what make them one shoot.
2. **Then the scene, the subject, the details, the constraints**, in short
   labelled sentences rather than one paragraph:
   "Scene: … Subject: … Light: key from the left, soft, warm. Camera: 45°,
   50mm, f/4. Empty: the upper third is clean plain wall. Use: an advertisement."
3. **Say what is empty, positively.** "The upper third is clean empty wall",
   not "no clutter"; "an empty, deserted street", not "no cars". Google's
   guide for Nano Banana asks for exactly this ("semantic negative
   prompts"), and Recraft V4.1 has no negative prompt at all. The empty
   area is where the headline goes.
   For a scene with several elements, give Nano Banana the order it builds
   in: "First, the background … Then, in the foreground … Finally, place …".
4. **Name the light direction**, and keep it the same as the product shot's.
   Studio pack shots are usually soft front-left light; a scene lit from the
   right will never take that pack convincingly.
5. **Name the material behaviour**: matte linen, glossy glaze, wet slate,
   crumbly, sticky, molten.
6. **Appetite words** where they are true: a drip down the side, crumbs, a
   bitten edge, steam, a swirl in the spread.
7. **No words.** The tool forbids lettering; never ask for any. An object that
   carries writing in life (an exam sheet, a notebook page, a letter, a
   receipt) is asked for blank: "blank lined paper", never "covered in
   handwriting with no readable letters". Asked for writing that cannot be
   read, a model writes readable words anyway, often in English. The marks
   that make it look used are added in the design: red rings and underlines
   as vector icons, the readable notes as text layers in a handwriting face.
8. **A part that came back with letters on it is generated again**, blank. It
   is never kept under a fade, a scrim or another layer: covered writing
   still shows through, and a washed-out object reads as a mistake. A marked
   exam sheet was kept that way, its fake English words dimmed under a grey
   rectangle, and the whole sheet looked faded.

## Parts with references (Nano Banana Pro, GPT Image 2)

- Give each reference a job, by number: "Image 1 is the hand pose to follow.
  Image 2 is the light and colour to match." Recraft takes references only as a
  style, never a layout.
- For a change to an earlier part: say the one change, then list everything to
  keep unchanged, and repeat that keep-list on every round — drift accumulates
  otherwise.
- Never pass the product shot to have it redrawn. The pack is placed, and
  `relight_product` is the only path where a model sees it, with its version
  thrown away.

## Which model

- **Recraft V4.1**: illustration, clean backdrops, graphic textures, flat
  colour grounds, isolated objects for cut-out. A strict palette works ("strict
  two-tone palette: #… and #…"). Do not describe the style when passing a style
  reference. V4.1 has no negative prompt and no "no text" switch (those are
  V3's): what to leave out is said positively in the prompt, like every other
  model. Lead with the subject; earlier words weigh more. For an illustration,
  say how it is drawn (line, how colour is laid, grain), or it comes back as
  flat vector.
- **Nano Banana Pro**: photographs with hands, food in use, scenes that must
  follow a reference, edits. A person only with no face, and never a child
  (SKILL.md, *People: real, or generated without a face*).
- **GPT Image 2**: photographic scenes with complex arrangement; precise edits.
  It is the model `build_scene` uses for `around`: of the edit models it
  holds a product's shape and place best, which is what lets the real one go
  back over it cleanly.
- **Nano Banana Pro** in `build_scene`'s `settle`: the best light and
  shadow on a product, and the least respect for it (it resizes and recolours
  it), which is why only its light is kept.
- **Muse Image** (Meta's): follows edit instructions and takes references as
  pictures, like the edit models. No seed, so a variant cannot be reproduced
  from one. Cheap, about 1 credit a picture.

Keep one model across ads that test hooks against each other, or the rollup
credits the hook with what the model changed.

## Cut-outs

`cutout: true` adds an isolated plain background to the prompt and removes it.
With GPT Image 2 it asks instead for a transparent background, which that
model draws itself (in preview), so there is no grey ground to remove and no
rim left from one; if a picture comes back opaque anyway, its background is
removed as usual. Whether it cuts cleaner than the other models has not been
compared yet: choose the model for the picture, not for this.
Ask for the subject whole with space around it; check the edges at full size
(fingers, crumbs, steam do not cut cleanly). A cut-out placed on a scene needs
`integrate_image`.

**Many loose pieces are not one cut-out.** A trail of crumbs or a spill of
nuts generated as one part comes back lying on the grey it was drawn on, and
the removal keeps that grey between the pieces: a pale plate under the pile
and a rim round the crumbs, in a scene that has neither. Put scattered pieces
in the scene itself (in the scene's prompt, or round the product with
`build_scene`), and keep cut-outs for one to three pieces, each its own part.

**Pieces of the product look like the product.** Never prompt with the
category word alone: "crackers" comes back as round, scalloped crackers, and
the reader sees someone else's snack. Look at the product shot first and
describe what is in it (the pack usually shows the food): shape, size, colour,
surface, what is on it ("square, pillow-shaped wheat crackers, golden brown,
flecked with dark green dried herbs"). The shot itself is never a reference:
a model shown a product redraws it.

## When a provider is down

No single model is required. Gemini (Nano Banana Pro) out of credit is not a
block: use GPT Image 2 for photographic parts and for `relight_product`, and
Recraft for the rest. Gemini also reads every part back for stray lettering;
while it is down that check returns `UNCHECKED` and the part is kept, so open
each part and look for letters yourself. Report a provider as BLOCKED only when
no model that can do the job is available.
