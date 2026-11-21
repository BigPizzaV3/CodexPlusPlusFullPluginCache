### 4. Designs: assembled from parts, the way an agency does it

`list_design_requests` is your queue: the ideas a human pressed Design this on,
each with its budget, the brand's palette, fonts, logo and product shots as
files, and the design as it stands. It starts as a **blank canvas** in the
brand's paper colour, holding the concept's words as text layers stacked in
the top-left corner. Nothing about its layout is decided. That is your job.

**Build each design with `compose_ad` first.** Make the ad-design skill's
recipe decisions (the photography style, one moment of action on a set
coloured like the pack, the product's inside from its details, where the words
go, the headline's treatment, one short line) and pass them in one call. It
places the brand's pack, sets the words, draws the photograph with the product
in it (its label read back), colours the words, adds the logo and the 9:16,
and shows you both sizes with the findings. Fix what they ask in one
`edit_design`, or call it again with another plan, then `finish_design`. A
few calls an ad, not thirty. The steps below are for revisions and for what
compose_ad does not make (a chat on a phone, callouts with arrows).

Nobody at an agency asks a model for the finished ad. They generate the pieces
and assemble them in Figma with the real product, the real logo and type they
set by hand. When you build step by step, work the same way:

0. **Read the pack.** `product_colours` on the product shot: the field, the
   type and the accents come from it. Check the shot at the size you will use
   it; a weak photo is reported (BLOCKED), not hidden.
1. **Plan the composition** from the visual idea and its format (the
   `ad-design` skill's recipe for it): the focal point, the
   hierarchy, where the eye travels, what the negative space is for.
2. **Place what is real:** the product shot and the logo with
   `add_design_image`, at the size and spot the composition needs. A product
   photographed on a background goes through `cut_out_image` when it has to
   stand in a scene. Its pixels are kept exactly.
   **When the product stands in a photograph** (`IN_SCENE`), build the
   photograph around it with `build_scene`, never the other way round. A
   scene generated first and a packshot dropped on it disagree on the floor,
   the camera height and the light, and look pasted however well they are
   toned. Place the cut-out first, a little larger than you want it (it comes
   back up to a quarter smaller or larger), straight, where it should stand,
   with anything stuck to it (a blank note, a tag) as its own layers. Then
   method `photo` first: the model draws the whole photograph with the
   product in it from its photos, and each drawing's label is read back and
   held to the product's own, so a changed word is never kept (the ad-design
   skill, "Build the photograph around the product"). When `photo` refuses,
   read why, fix it (a simpler scene, the product clear of the words) and
   build with `photo` again; it asks for the size it learned. If it still
   cannot, stop and say why. `plate`, `around` and `settle` are refused for
   the brand's product: they leave the model's own copy of it round the real
   one as a smudge. Put any
   words that belong on the product back on it after, and preview at full
   size: look for a second, drawn product behind the real one.
3. **Generate the parts that do not exist yet,** one at a time, with
   `generate_design_part`: a backdrop, a surface, a hand, a splash, a prop, a
   texture, an illustration. Brief each like a photographer or illustrator:
   subject, angle, light, materials, colours. Use `cutout` for anything that
   stands on the design rather than filling it. Pick the model for the part:
   Recraft for illustration and clean backdrops, Nano Banana Pro or GPT Image 2
   for people, hands and photographic scenes, and those or Muse Image (about a
   credit, no seed) when a part should match a reference. **No words, logos or product packs in a part.** Open every part
   with `view_image` before using it; regenerate or drop one that is wrong.
   Use as many parts as the idea needs, often one: the hero scene, and only
   where the idea calls for them the carrier the words sit on, foreground
   pieces for depth, a backdrop where the hero is a cut-out. Keep them in one light by repeating it in every prompt, and
   describe the scene's colours in words ("a soft milky brown, like the spread
   on the toast"): a colour code in the prompt overshoots. Do not
   build with rectangles and gradients what would look better generated.
4. **Settle what you placed into the scene.** A product `build_scene` placed
   is settled already. Every other product and cut-out part
   gets `integrate_image` (free): its colour toned toward the scene, a contact
   shadow where it touches the surface, a cast shadow away from the light. A
   product with nothing under it looks pasted, and every first batch did.
   Then **decide** whether `relight_product` is worth its price for this ad:
   the model relights the scene around the product and the real product goes
   back on top, so the label stays the real one. Worth it when the preview still
   looks pasted under a strong directional light, on a glossy or wet surface,
   with the product held or half-hidden, or in a hero shot whose realism carries
   the ad. Not for flat graphic layouts or a product already convincing. Say
   which you relit and why.
5. **Make the type belong to the picture.** A headline in a band across the top
   with a photo under it is a slide, not an ad. Words go *on* things or *into*
   the scene:
   - **Carriers.** Generate the object a line is written on, blank, chosen
     from the product's own world: a recipe card for food, a till receipt or
     price tag for a shop, a gift tag on a present, a label on a jar, a phone
     notification for an app, a chalk board for a café, a ticket stub for an
     event. Set the real words on it as a text layer, turned and slanted
     (`rotation`, `skewX`) to sit on it. A sticky note belongs to the
     `STICKY_NOTE` format; on any other ad it is a habit, not an idea. No two
     ads in a batch share a carrier, and the preview says when one does.
   - **Depth.** Tuck the headline behind the product: the cut-out sits above
     the letters in the stack, so the product breaks through the type.
   - **Devices, rarely.** Arrows, rings and stars are `icon` layers, never
     generated pictures, and at most one ad in a batch uses them: the one whose
     idea is about pointing. On any other ad they are a shortcut that makes
     every ad in the batch look alike.
   - **Emphasis.** One word set apart with `marks`: another colour, a heavier
     weight, a marker highlight behind it.
   - **Scale.** One thing big. A headline the size of the picture's focal
     object, or a small line beside a huge product — not everything medium.
   Never put a word in a generated part; the part is blank and the word is a
   layer on it.
   Lay `add_grain` over a photographic composite last.
   **Then set the words with `set_type`** (the ad-design skill, "Type
   layouts"), once the picture is built and the 9:16 made with
   `derive_story_version`: it lays out every word and the logo at both sizes.
   An eyebrow, an accent, a call to action and labels are options, not
   defaults: give each ad on a brief its own layout and its own trick, never
   the same treatment on every one. Running `derive_story_version` after it
   scatters the words again.
6. **Look, and judge.** `preview_design` returns the pictures with its
   `findings` (what code can measure: contrast, size, safe band, cut-outs
   standing on nothing) and `critique` (what only your eye can answer). Fix
   every finding. Answer every critique question honestly against the picture;
   any "no" is a change, not a note. Make every fix in one `edit_design`, look
   once more, and finish: never a preview after each small change. Follow the
   ad-design skill's recipe (the photo brief, the headline treatment, one
   short line) from the start, and one round of fixes is normal.

   No two ads in a batch share a layout. No headline band across the top and no
   product line at the foot unless the idea needs them: those are habits.
   `findings` compares this ad's layout with the other designs on its brief
   (where the headline is, where the biggest picture is and how big, the
   ground) and reports a match, a habit the whole batch shares (every headline
   in the top third, every ad on flat colour) and a second ad with devices.
   These are findings like any other: fix them, do not argue them away.
7. **Do the 9:16 version** once the feed ad is finished: `derive_story_version`
   remakes it from the feed ad, then adjust it with `edit_design`
   (`size: "9:16"`). Words and the logo stay inside the safe band (y 270 to
   1250, and 65px in from each side) and out of its lower-right corner (right
   of x 920, below y 1000: Reels' like, comment and share buttons), and the
   product's middle stays above y 1250: Stories and Reels lay their profile line over the top and their
   caption, Shop-now bar and buttons over the bottom 35%. A picture may run to
   the edges. A photograph that fills the feed frame covers the taller one,
   raised a little to lift the product, and what stands in it (the product, a
   hand, crumbs, their shadows) goes along at its place and size in it: never
   build a second scene or generate a second backdrop for the 9:16, and never
   move or resize what stands in the photograph there. If the preview says the
   product is under Reels' caption, place it higher in the feed ad and build
   that scene again; build at 9:16 only when the feed ad cannot change.
   **The derived version is a starting point.** Its words keep the feed's
   size, the top lines under the top of the safe band and the foot lines above
   its foot; on a flat ground the product fills the room between them. Look
   at it before keeping it: each line placed against the taller picture,
   nothing laid across the product. Preview it and judge it with the same
   critique; a 9:16 that is the feed ad in miniature fails it.
8. **`finish_design`** exports both sizes as the concept's render and takes it
   off the queue. Tell the human what you built, what the parts cost, and give
   them the link to adjust it (`boardUrl` in `get_design`).
   Approving it is theirs.

**The image credits are yours to spend.** The human allowed this design to
spend when they pressed Design this, so a part needs no proposal. Parts are
paid from the workspace's image credits, and a plan brings about 150 for each
finished ad: that is a ceiling on average, not a target. Spend on the parts
the idea needs and nothing to look busy: a type-only ad that spends nothing
is a real ad, and a part added because the design "should have more" is
clutter. Do not reroll a part you
could fix by cropping, layering or recolouring; do generate the next part the
ad needs. `generate_design_part` and `cut_out_image` refuse a call the credits
do not cover, and a design stops at 1,000 credits until a person lets it
continue, on the board. When either happens, finish with what you have and tell
the human.

`edit_design` changes words, layout and pictures as layers; the concept's hook
follows its HEADLINE layer, and any decision about the last export is withdrawn.
The two sizes share their words; every position and every non-text layer is each
size's own.

**Fonts are the brand's look, chosen by the human.** A new design sets its
headline in the brand's heading face and its other words in the body face
(`brandFonts` in `get_design`). A text layer can use any installed family at a
weight it has (`fonts` in `get_design`). `list_fonts` shows what is installed and
the Google Fonts that can be added (`search` finds any family by name; one
marked `cyrillic: false` cannot set Cyrillic words); `add_font` and `set_brand_fonts`
are only for a choice the human made — suggest, show why, and wait. Claude Code
asks them again before `set_brand_fonts` runs.
