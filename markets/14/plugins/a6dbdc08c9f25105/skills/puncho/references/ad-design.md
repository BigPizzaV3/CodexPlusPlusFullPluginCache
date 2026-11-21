# Designing ads that stop the thumb

The copy gets an ad read; the picture gets it seen. Most AI-made ads fail in
the same few ways — a product pasted into a room it was never in, a headline
floating in a band over a photo, five things of equal weight, colours from
nowhere — and every one of them is a choice, not a limit of the tools.

Read `references/formats.md` before choosing a format,
`references/examples.md` before the first design of a batch (it shows the
level to reach, never a layout), and `references/prompting.md` before writing
any part prompt.

## The recipe: start here

The strongest food and product statics this pipeline has made came from the
same five moves, made in this order. Everything below refines them; none of
it replaces them.

**`compose_ad` makes them in one call.** Its `photography` is move 1's
light (BOLD, FLASH, MIDDAY_SUN, WINDOW_STEAM, LAMP_NIGHT, COLOUR_BLOCK), its
`scene` and `inside` the rest of the brief, `wordsAt` the empty part,
`treatment` move 2 (STACKED_CAPS, STRUCK_WORD with `struck`, ITALIC_SERIF,
SCALE_JUMP: one word half as big again, MIXED_FACE: one word in an italic
serif; `accent` picks the word), `line` move 3. Never the same treatment as
the brief's other ads (`typeIdeasTaken`). `line` and `note` are the
concept's own planned lines, word for word; the build never writes copy. `note`
sets the concept's CAPTION (two to four words) handwritten under the words with
a drawn arrow down to the product: use it whenever the concept planned one. `finish` (its type idea) hands the ad over in the same
call when the checks pass. Build with it first; the step tools are for
revisions. It carries a headline, one line and a note, so a concept planning
more (a list of steps, CALLOUTS' facts) is built with the step tools: it
refuses rather than delete a planned line. Keep the words' part of the scene
bare: nothing standing there, not even the food. A photograph that puts
something under the headline is not handed over. STRUCK_WORD strikes only
words the ad argues against (a claim it refutes, the word it corrects): struck
words read as "not this", and striking what the concept holds true is refused.
Detail lines that belong on a thing in the photograph (steps on a note by the
jar, a line on a recipe card) are written by the model, not laid on it:
`build_scene` method `photo` with `writeOn` (the thing, as the prompt names
it) and `writeLines` (those text layers). It writes them in big marker, reads
them back blind letter for letter, and keeps none that is wrong. Type laid as a
layer over a drawn note never follows its tilt or light and reads as a sticker,
so never ask the scene for a blank card to lay layers on. The headline, a price
and an offer always stay layers, on the plain ground. A
list's items (steps, numbered or bulleted lines) are one rank: one size, the
same air between each, whatever the visual idea says.

1. **The photo brief has four lines** (`build_scene` method `photo`, its
   `prompt`):
   - **Photography:** one line naming the light and the look, chosen for the
     moment: "bold, saturated food photography, hard light from the upper
     right, deep shadows, glossy textures"; "casual direct-flash food
     photography, high contrast, a little grain, the look of a late-night
     snack"; "hard midday sun, crisp shadows, saturated colours"; "warm
     documentary kitchen photography, morning window light, steam catching
     the light"; "one warm lamp in a dark room". Never soft daylight or a
     calm room alone: that is the beige that reads as stock.
   - **Scene:** one moment of action with the product. A spoon lifting a
     ribbon that drips, a hand dipping, squeezing, snapping, pouring, a bite
     taken, steam rising. The food big and close, the product large beside
     it. The set coloured like the pack: a table and wall in the label's
     colour, or the colour it stands out on.
   - **The product's real look:** when it is opened, cut, broken or poured,
     describe its inside and its texture from the product's own details
     (`productShots` details, the product page), never from a guess, as one
     solid texture (never loose grains: they read as worms). Often the
     whole product is better than a cut one. A
     chocolate ball whose inside was guessed as "puffed rice" came out as
     loose grains that read as worms; "one airy crisp core, like the inside
     of a rice cake" came out right.
   - **Empty:** where the words go, said as what it is ("the top third is the
     plain pink wall, with nothing on it").
2. **The headline is 2 to 6 words, set huge, with one treatment:**
   - stacked capitals in a condensed face (`set_type` `face` Oswald; `caps`
     on the layer), the last word in a second colour (`marks` fill);
   - a struck-through word, then the answer (`marks` with `strike` on the
     first word: "~~Филия.~~ Соленка.");
   - an italic serif in the pack's colour (`face` Playfair Display, `italic`
     on the layer);
   - the words on an object in the photograph, or one giant word.
   The colour comes from the pack or the photograph, never grey.
3. **One short line under it, or none:** the reason, the moment or the
   offer. Never the product's name, its weight or a list; a list is its own
   format (CALLOUTS, US_VS_THEM).
4. **The logo small in a corner.** Nothing else on the image.
5. **Look once, fix once, finish.** `preview_design` returns the pictures
   with its findings. Look, make every fix in one `edit_design`, preview
   again, then `derive_story_version`, preview the 9:16 and finish. Never a
   preview after each small change: a design took 27 to 44 steps when it
   did, and most of them were looks between nudges.

## Rules are defaults; the idea decides

Everything below describes what has worked in strong statics. Almost none of
it is a law. Rules written one failure at a time add up to a checklist, and an
ad built to tick a checklist gets a footer, a second level and a third part it
never needed. So, as in `ad-copy`: a default may be broken when the ad's idea
needs it, and the note you hand over says which one and why. The human reads
that note before approving.

**Hard limits, for every design:** the product is the real one, placed, never
drawn; no words in a generated picture; no invented claim, number, rating or
customer; every word on the image is a text layer the human approves; the
words and the logo can be read (contrast, size, the 9:16 safe area); one light
across a photograph; no generated face, and no generated child at all. Findings about these are fixed, never explained away.
Everything else is a default.

## The three decisions, in this order

1. **The format** (`adFormat`). Pick from `references/formats.md` by what the
   idea needs to prove. Meta asks advertisers to diversify their creative and
   publishes no threshold for when two ads count as one. That ads of one
   format and setting are delivered as one creative is a claim agencies make,
   not one Meta has made. Our own rule stands on its own reason: a batch
   spreads across at least three formats, because a new headline on the same
   layout is not a new ad and tests nothing new. Meta's other half: keep one
   brand look (colours, logo, type) across concepts that differ.
2. **The product mode** (`productMode`). How the real pack appears. **A
   product that is shown stands in its scene**: on the surface, in the hand,
   worn, beside the food it goes with, in the scene's own light. Every mode
   carries a photograph. A brand with nothing to place (a school, a service,
   an event) uses `NO_PACK`. The product shots are usually the store's own
   catalogue photos, all from one angle, so the variety has to come from the
   format, the place, the scale (small in a wide scene, or cropped so close it
   becomes texture), a pair or one, and the light, not from the photo or from
   how the product is laid on.
   - `GRAPHIC_FIELD` — the pack cut out onto a flat field of its own
     colours. **Retired: never written for a new concept.** It was nearly
     half of every brand's ads, and a packshot on a colour reads as a
     catalogue page however good the type is: there is nothing to look at
     but the pack. The pack's colours now go into the photograph instead (the
     surface, the wall, the light).
   - `CORNER_PACK` — the pack laid flat in a corner over a photograph, like a
     sticker. **Retired: never written for a new concept.** It was the cheap
     way round building a scene, and it read as pasted: a shoe dropped on a
     generated street at dusk, lit by daylight, standing on a floor seen from
     another height, with two drawn ellipses for its shadow. Even the jar
     beside the toast is better on the same table, in the same light.
   - `IN_SCENE` — the pack physically in the moment. Built with
     `build_scene`: the real pack placed first, the photograph made around
     it. See *Build the photograph around the product* below. One way to do
     it is the **brand selfie**: the product held in a hand, seen from the
     holder's own eyes, the reader's view, with no face in the picture, in a
     real place (a bus seat, a desk, a kitchen). It is the one static pattern
     with published evidence of higher purchase intent, and a face in it
     lowered that. The real pack is placed where the grip will be, and the
     hand and the place are made round it; never a hand and a pack on white.
   - `NO_PACK` — the food, the words or the moment carry it; the logo signs it.
     When the brand sells that food, it must be its food: generate it with
     `foodFrom` set to the product shot, so the model sees the real colour,
     shape and coating (and draws no pack). Drawn from words alone, a pink
     raspberry ball came back white. The same holds for the food beside the
     pack in `IN_SCENE`: crumbs, a bitten piece, a bowl of it.
3. **Where the words live.** Never "headline in a band, photo underneath",
   and never a header strip across the top with the picture below it, on a
   photo or a flat field.
   Words go on their own colour plane, on an object made for them, or behind
   the product. See *Type* below.

## Colour comes from the pack

The best food ads are extensions of their packs: the field is the box's own
pink, the wall and table are the pouch's brown and cream. Run
`product_colours` on the product shot first. Ground = the signature colour (or
two planes: signature and paper); type = paper or ink, whichever reads; one
accent at most. Previews flag flat colours from neither the pack nor the
palette. A different colour is a decision you can defend, not a default.

## People: real, or generated without a face

A product worn or used by someone sells better than one standing alone, and
most brands' own photographs show it on a body. So a generated adult may be in
an ad, **with no face**: seen from behind or walking away, turned away, cropped
at the shoulders or the neck, or the face out of the frame. Never a generated
face, even small or out of focus, and never a generated child or teenager, in
any style that could pass for a photo. A face is where a generated picture
fails first (eyes, teeth, skin), it reads as a customer who does not exist, and
it can look like a real person who never agreed to be in an ad.

- **The product stays the hero.** Frame it waist down, or low and close at the
  feet or hands: the product at least as large as the hero rule asks. A whole
  figure in a wide street is a lifestyle picture with the product lost in it.
- **Worn or held: the person decides.** A photo of an empty product cannot
  be worn: asked to keep the real shoe and draw a leg into it, a model draws
  its own shoe on the leg, and the real one never lines up. So the product is
  drawn only where a person ticked "Let the model draw the product" on the
  concept. Then place the product where and as big as it should be worn, and
  call `build_scene` with method `worn`, `wornBy` (who, what they wear, how
  they stand, cropped with no face) and `productPhotos` (other angles of the
  same product, when the store has them). Its colour is corrected toward the
  photo and the drift reported: compare it with the product shot at full size,
  material, laces and sole, and build again when it does not read as the same
  product. Left out, `productPhotos` is the product's own angles (its file and
  `angles` in `productShots`).
- **Without the tick, suggest it.** When the idea needs the product worn or
  held, call `suggest_product_draw` with why, and how many photos of the
  product there are. One photo is enough to suggest it: say what may differ
  (the toe, the back) and let the person decide. Then finish the design with
  the product placed from its photo; once they allow it, they ask again.
- **The brand's own photographs of people come first** when they show the
  product; a generated person is for when they do not.

## The product is real, always

- Placed from its photo (`add_design_image`), never drawn. A drawn pack is a
  pack the store does not sell, and its label will be wrong.
- What an image model may draw freely is the **contents**: the spread, the
  crackers, the chocolate, crumbs, drips, the hand holding them. Food has no
  label to misspell. Generate it in the product's own light.
- **Clear glass or plastic is drawn in, never cut out.** A bottle or jar shot
  on white keeps that white inside its glass, in its own solid pixels: on any
  other ground the neck reads as milky plastic, and no edge cleaning reaches
  it. Build it with `build_scene` method `photo`, which draws it from its photo
  with the scene seen through the glass and reads its label back blind.
- Check the product shot at the size you will use it. A soft, oversharpened or
  haloed shot shows at full screen; use it smaller in a wider scene, or say plainly
  that a better photo is needed (verdict BLOCKED). No composite hides a bad
  source.
- The product gets `build_scene` (below), always. Never a photograph made
  first with the product dropped on it: previews flag a cut-out laid over a
  photograph no `build_scene` made, and finish is held for it. A part placed
  after the scene (a crumb, a leaf in the foreground) gets `integrate_image`
  (tone, contact and cast shadow).
- Never a plain box drawn behind the product: a "white card", a plate, a
  panel it stands on. It frames the cut-out as a cut-out, and the ad reads as
  a catalogue page. The product stands in the photograph. Previews flag the
  box, and finish is held for it.
  `relight_product` is for a scene that was built the old way, scene first.

## Build the photograph around the product

The pasted look has one cause: a scene generated first, then a packshot
dropped on it. The scene's floor, camera height and light were invented
before anyone knew what would stand there, so a pack shot from the side
stands on a floor seen from above, in a light that falls the other way. No
shadow or tone fixes that. So the order is reversed:

0. **Look at the brand's own photographs first.** `list_design_requests`
   gives them under `brand.photographs`: its key visuals and its organic
   posts. Open three with `view_image` and name what they share: the kind
   of place, the light and time of day, the lens and the distance, whether
   the product is worn or placed, any marks drawn over the photo. The ad's
   photograph is shot that way, in the brand's world. A brand whose feed is
   sunlit grass and moss does not get a dusk street or a studio grey, however
   well the headline fits it. Pass two or three of them as `lookFrom` to
   `build_scene`, so the model shoots the scene the way the brand does.
   **When the request has a `structure`, build to it.** It is the measured
   geometry of the ad the concept borrowed its shape from: the hero's box and
   crops, each prop's place, size and depth, the blocks of words. Place the
   product at the hero's box, describe each prop in the scene prompt where
   and how big the structure puts it, and set the words in its text boxes.
   Its proportions are what made that ad work, and a layout invented fresh
   came out as two objects side by side under a dead band. The scene, the
   light, the props themselves and the type stay this concept's.
1. **Place the real product first**: the cut-out, straight, where it should
   stand and a little larger than you want it, because it comes back up to a
   quarter smaller or larger. Anything stuck to it (a tag, a ribbon, a
   label) is its own layer on it, and goes in `layerIds` after the
   product so the scene is made around both.
2. **`build_scene`, method `photo`, first.** The model draws the whole
   photograph with the product in it, from its photos (the layers you placed),
   so the light, the camera and the scale are one shoot. A packshot pasted into
   a photographed place keeps its own studio light, camera height and size, and
   it read as pasted every time, whatever was done to it after. The label is
   not left to trust: each drawing is read back blind and held to the
   product's own photo, and one with a word added or changed (an invented
   "110" on a pouch), the name missing, an extra product, or a product standing
   where the words are set is not kept. Four are drawn a round and the best
   that passes is kept; if none passes in three rounds nothing is placed and
   it says why.
   So: set the words first (their places are kept calm and clear), place the
   products about where and as big as they should stand, then describe the
   photograph in `prompt` like a photographer (the place, the surface, what
   else is there and how big against the product: "a glass about half the
   carton's height", the light, the camera height), with `lookFrom` two of the
   brand's photographs and `wornBy` for a hand with it (no face). The product
   layers become the picture; the concept is marked as having a drawn product,
   and whoever approves it is told. Look at the product at full size in the
   preview against its photo before finishing. Use it for every photograph:
   a room, a table, a shelf, a studio light, a flat lay seen from above (the
   model draws the product from above too, which a front packshot laid flat
   never was).
   **`photo` is the only way a product gets into a photograph.** When it
   refuses (a changed label, the product over the words, too big), it says
   why and keeps the drawings to look at: read them, fix what it names (a
   simpler scene, fewer props, the product clear of the words) and build
   with `photo` again. It learns the size the model draws the product at
   and asks for less next time. If it still cannot, stop and say why in your
   reply. `plate`, `around` and `settle` lay the real cut-out on a scene
   and paint light round it, and `around` leaves the model's own copy of
   the product behind it as a smudge: they are refused for any ad that shows
   its product, and stay only for props in an ad with no product (NO_PACK).
   **Whatever stands beside the product is built with it, never pasted after.**
   A glass of the drink, a cup, a bowl: say it in the prompt, or place its
   part before `build_scene` and pass its layer in `layerIds` after the
   product, so the scene lights and shadows both. A glass generated and laid
   beside a built carton came back small and stuck on. Give a prop its size
   against the product ("a glass about half the carton's height"): left out,
   the model drew a glass as big as the carton beside it.
   **After the scene is built, the product stays where it is**, at its size.
   The scene's shadows were made for that place; moved, it stands off them.
   To move it, place it and build again.
   **A hand holding the product** is `photo` with `wornBy` ("a hand
   round the pack, from the right edge, no face"): the model draws the hand
   and the product together.
3. **The weather on the product** (`dress_product`): when the scene has snow,
   rain, sand or dust, the product should carry a little of it, or it reads
   as placed. Ask for a little and say where ("a light dusting of fresh snow
   on the toe and along the laces"). Only what the model added is kept, as a
   layer over the untouched product; delete that layer to undo.
4. Then the rest of the ad on top: foreground parts, the carrier's words, the
   headline (tucked behind the product if the idea wants depth), the logo.

Text layers under the product stay where they are. Words that belong on the
product (on the note) do not move with it: set them back on it after.

- **Place it at its final size, whole inside the frame.** The model often
  draws it smaller; place it a little large. Never move or enlarge it after
  the scene is built, and never `integrate_image` it: the shadows, the
  reflection and the light were made for that size and place, and a moved
  product floats. Too small: place it larger and build again.
- **A pair is placed as a pair before the build** (see *Say enough*), and
  both layers go in `layerIds`.
- **The 9:16 keeps the feed's scene.** `derive_story_version` covers the
  taller frame with the feed's photograph and takes everything standing in it
  along, at its place and size in it, enlarging and raising the photograph a
  little to lift the product out from under Reels' caption; only the words
  and the logo go into the safe band. Never build a second scene or generate
  a second backdrop for the 9:16: it is another photograph, paid for twice,
  and the product no longer matches it. Build at 9:16 only when the derived
  one cuts the product off at a side, or the preview says the product stands
  under Reels' caption and the feed ad cannot place it higher. A product
  standing low in the feed is the usual cause: where the idea allows, stand
  it in the middle of the feed frame, not on its bottom edge.

## When there is nothing to place

A school, a service, an event, software: no pack, and often no photograph of
its own. The usual way out is a small flat illustration of the subject in the
middle of an empty field with the headline under it, and it is the weakest ad
there is. It reads as a slide, and any brand's logo could sign it.

- **The picture is the thing the headline is about, as a real object.** The
  page with the mistake circled, the exam sheet, the ticket, the notebook, the
  chalkboard, a hand mid-gesture, the tool the work is done with. Generated as
  a photograph or a made thing with material and light, filling the frame or
  cropped by it. A subject can also be the word itself: see *Type as a picture*.
- **Fill the frame.** The hero covers at least half of it, bleeds off an edge
  or sits behind the type. Something small centred in a field of paper, with
  the same empty margin all round, is not a composition.
- **Every ad carries a photograph, and it fills the frame.** The product cut
  out onto a flat colour is not one, and neither is a pile of cut-out props
  around it: that is a catalogue page. The photograph is a scene built round
  the real product (`build_scene`), or, with no product in the ad, a
  generated photo of the food, the hands or the moment, covering at least
  half the frame. Finish is held while nothing does.
  "No stock photography" rules out
  stock, not pictures, and a flat brand look decides how a photo is treated
  (black and white, cropped, pixel blocks over its edge), never whether
  there is one. Use photographs of the brand's own people, place or moment
  (asked of the human; verdict BLOCKED when there are none and the idea
  needs them), or a generated scene or object in the brand's photo style.
  A design of rectangles and type with no picture is the weak ad this
  section describes, whatever the notes say: it is built only when a person
  asked for no picture, and the finish note says so.
- **The photograph is a moment, not an object.** It shows the thing the
  headline promises happening: the screen lit up in a dark room, hands on
  the keyboard at 2 a.m., the one lamp on in an empty lab. A switched-off
  monitor on grey is a product listing with nothing for sale. Light is what
  makes it a moment: one source, named in the prompt, and the subject large
  enough to read at a thumb's width.
- **The subject stays whole, or is cropped on purpose.** Generate the
  photograph at the shape of the area it fills, with room around the
  subject, and place it so no edge of the frame or of a panel slices it: a
  monitor with its top cut off, a head under the frame's edge, read as an
  accident. A tight crop into a detail (the keys, a hand, one corner of the
  screen) is a choice, and it is made in the prompt, not by where the
  picture happens to land.
- **A graphic device is one built shape, placed with intent.** The brand's
  blocks, rings or stickers make one cluster on one edge (where the photo
  meets the field, or a corner), sized to the grid. Never scattered like
  confetti, and never touching the words: a block that meets a letter reads
  as part of it. The preview flags it.
- **Illustration only when the brand's own material is illustrated** (its
  site, its posts, its key visuals), and then in that style, described from
  what you looked at: line, texture, how colour is laid. Never generic flat
  vector shapes, which is what an image model draws when it is told nothing.
- **A part never shows its own edges.** A generated picture that is not cut
  out carries its background with it. Placed on a field it becomes a
  rectangle on a rectangle, or disappears into paper of the same colour and
  leaves a small drawing in a void. Either it is the ground (full bleed), or
  it is cut out and integrated, or it sits in a shape made for it.
- **No frame for the sake of one.** A coloured border round a white panel is
  decoration added because the middle was empty. Fix the middle.

## Say enough, and use the frame

The default is the headline and **one** supporting level, over a picture the
eye goes to first. Meta's own guidance says the same thing four ways: images
with little text perform better, most of the words belong in the primary text
and not on the image, don't spread text over the picture, and ask people to
"look at one thing". So dates, an address, the details and the second and
third facts go in the primary text, two or three lines read right under the
picture. Dense layouts (`CALLOUTS`, `US_VS_THEM`, a stat bar) are formats
chosen because the idea is the facts, not a baseline for every ad.

Saying too little fails too. One line over a product on an empty wall often
reads as a mood board, and a stranger scrolling past learns nothing: not what
the thing is, not why it is better. The one supporting level is what fixes
that: the product's one reason, or the offer as a badge. The pack in the
picture already names the product: never set its name and weight again as a
line. Quiet
can also be the idea (one object, a calm field), and then the note says so.

- **Empty space is there on purpose, or it goes.** A wall of nothing left
  between the headline and the product is dead space: make the product
  bigger or higher, bring the camera closer, set the headline larger or into
  the scene, or put the supporting words there. `preview_design` points out
  a band over a sixth of the height with nothing in it (`CONTENT`) and asks
  whether it is doing something. Quiet around one thing is a choice; leftover
  space is not.
- **The second level follows what the ad sells on** (the concept's `lead`). A
  feeling: one line, and the picture carries the rest.
  Proof: a real review as its card, the rating. The product: three or four
  facts as callouts or a stat bar. An offer: the deal as a badge or sticker,
  the price when it is the argument. A problem: the problem in the reader's
  words, the fix in one line. Something new: what is new, and since when.
- **A second level, on a designed frame.** By default a designed frame (a
  field, a split, a product on a ground) carries one level of the concept's
  words beyond the headline: a KICKER or a BADGE. A format whose idea is one
  thing (a phone screen, a note, a person's words, one huge number) does not:
  its words are inside the object, and the preview does not ask for more.
  When a designed frame has only a headline, add what the evidence gives: its one
  reason, a detail from `productShots` or the product page (a price only when
  the concept is about price or an offer), and
  say in your note what you added. Never invent a claim, a rating, a discount
  or a number. Words you add go to the concept with the design and a human
  approves them with the ad.
- **An object in a real moment carries its own words.** When the ad is a
  phone screen, a note, a letter, a receipt or a label in a photographed
  moment, its second level lives inside that object (the alarm's label, the
  last line of the note), and nothing is set on the scene around it: words
  printed on a table or floating over a bedroom cannot exist in that photo,
  and they turn the moment back into an ad. Dates, an address and the
  website go in the primary text, which is read right under the picture
  beside Meta's own link and button. An alarm on a bedside table had a
  footer of dates, address and URL set on the wood below it.
- **A container is a real thing or a zone, never a plate.** Strong statics
  use boxes all the time, and every one of them is something: a review card
  with its avatar, name, stars and "verified"; a comment, a notification, a
  notes page, a news headline; a stat bar split by thin rules with each number
  big over its small label; a full-width band the headline sits in, edge to
  edge, when the idea is a label (a news ticker, a ticket stub), in one ad of
  a batch at most; a round seal, a starburst, a price sticker, a button. A rounded or
  see-through rectangle floating on a photo with a caption in it is none of
  these, and reads as a template. Either set the words straight on a clean
  plane of the picture (sky, sand, wall, the pack's field, planned when the
  scene is built), or build the real thing with its parts. `preview_design`
  reports a plain plate round words.
- **The second level is a size of its own.** Under the headline, the product's
  name and its reason at about a third of the headline's size; facts smaller
  again. Two lines of one size stacked together are not two
  levels.
- **Show the product as it is sold.** A pair of shoes is a pair. From a
  side-on shot: the same shot twice facing the same way, the second slightly
  behind, higher and offset, a little smaller, overlapping the first. Mirror
  (`flipX`) only a shot taken from above or straight on: a mirrored side view
  points its toes away from its partner. As the hero it
  is at least 45% of the frame's width; the preview measures it.
- **One thing to look at.** One focal point, at most three type levels, the
  headline at least 1.6x the next size. Forty words of equal weight is a
  leaflet.

## Where the words go

How the strongest statics place their words. Pick one arrangement per ad, by
what the words are, and build it whole.

### Type layouts: `set_type`

An ad is not a photograph with a title above it. Strong statics compose the
words and the picture together, and they do it in a handful of layouts, again
and again. `set_type` sets every word and the logo in one of them, at both
sizes, measured: run it once the picture is built and the 9:16 made, then
preview. Choose the layout by the picture and the hook, and give a brief's
designs different layouts.

**Choose the arrangement before you build the picture.** The words go where
the idea puts them, and the photograph is built for that: set the words first,
where they will stand, and `build_scene` keeps that spot calm. Placing the
headline at the top by habit is what makes every ad "text above, product
below". Pick one of these for each ad, and a different one for each ad of a
batch (the preview holds a headline in the same third as half the batch):

- **Behind the product:** the headline huge across the middle, the product
  standing in front of the letters (`set_type` GIANT_WORD).
- **On the scene:** the words on an object the photograph holds (a board, a
  window, a napkin, a label), turned with it.
- **At the foot:** the picture fills the top two thirds, the headline sits on
  the calm surface at the bottom.
- **Beside it:** the product on one side, the words in a column on the other,
  the picture built with that side quiet.
- **The product huge and cropped**, with a short headline small in a corner.
- **Top headline:** at most once a batch, and only when the idea is a
  statement read before the picture.

**A batch is not one template.** Seven ads each with an eyebrow, one orange
phrase and an underlined call to action, stacked top-left over a photo, are
one ad seven times, however good each looks alone. Before setting a brief's
type, decide each ad's one trick and write it down: one giant word, the words
naming things in the picture, a tag on the pack, a quiet caption, a centred
stack. No two ads on a brief share a layout, and the preview holds a finish
that does (BATCH, "the same layout as").

| Layout | Use it when |
|---|---|
| `TOP_STACK` | A calm top to the picture and the product low: eyebrow, headline, sub-line, the call to action in a free lower corner |
| `CENTRED_STACK` | A centred product on a calm ground: the logo small on top, everything centred, the call to action at the foot. Calm, premium, food |
| `SIDE_COLUMN` | The product stands to one side and leaves the other empty: the words in a column there (pass `side`, or it takes the empty one) |
| `GIANT_WORD` | The hook is one word or a number ("3 PM", "14+", "MEGA"): it fills the width and the product stands in front of it. Pass `subject` (the product in a word); it is cut out of its own photo |
| `FOOT_CAPTION` | The photograph does the work: a small centred headline low on a calm area |
| `STAT_BAR` | The argument is facts: two to four short `COLUMN_LINE`s set in a row with dividers at the foot |
| `OFFER_TAG` | The ad sells on a real offer: it is printed on a tag hanging on the product (the brief's offer, never invented) |

What it adds, and what you choose. Each is an option for the ad that needs
it, not a default: most ads use one or two of them, never all.

- **An eyebrow** (`eyebrow`): a few words in small letter-spaced capitals above
  the headline that tell a stranger what kind of thing this is, in words the
  picture does not say: "Protein you sprinkle on dinner", "New this winter".
  Never the product's name, its label or the brand alone: the pack and the
  logo already say those, and `preview_design` reports a line that only
  names the product.
- **One accent in the headline** (`accent`, `accentStyle`): words set apart in
  the brand's accent, as a colour or a marker behind them, or in its accent
  face (`face`, when its type style names one). The words that carry the
  argument ("20% off.", "It's still cold."), once.
- **A call to action** (`cta`): a short line with an arrow ("Shop the 12-pack →"),
  set as an underlined link. Never a pill or a button drawn as a box: the
  preview reads that as a template plate. Meta puts its own button under every
  ad, so leave it off where the picture needs the room.
- **Labels** (`labels`): one or two words standing just above things in the
  picture: "Water", "Oat milk", "Tonic" over three glasses, a name over each
  product. The words point at the picture, so the picture is read with them,
  and they are often the best idea an ad has. Give each label the box of what
  it names (`over`, in the feed's frame, read off the preview); left out,
  labels go on the recorded products, left to right. A label whose words are
  already a line of the concept moves that line.
- Each line takes the palette's dark or light, whichever reads against the
  picture behind it; the headline is set as big as the room above the product
  allows, in two lines where it can.

A layout that does not fit the picture is refused with why, and nothing
changes: choose another, or pass `storyLayout` when only the 9:16 cannot take
it (a stat bar or a caption at the foot sits under Stories' reply bar). The
words stay ordinary text layers: adjust them with `edit_design` after, and run
`set_type` again only to change the layout, which replaces what it set.

- **The frame is planned in zones, by share.** "Top 15%: the headline. Middle
  55%: the photo. Bottom 25%: three benefits." Decide the zones before the
  first part is generated. Set the text layers where they go before
  `build_scene`: it tells the scene model to keep those places calm (open sky,
  a plain wall, nothing important) and says what it kept clear in
  `keptClear`. For a part generated on its own, say the clean zone in its
  prompt.
- **The headline fills its zone.** Across 85-95% of the width, two or three
  lines, tight leading, the frame's margin on both sides (about 5% of the
  width; the same margin for everything). Centred over a symmetric layout,
  left-aligned in a split one.
- **The subhead hangs from the headline.** Directly under it, one sentence, a
  third to a half of its size. Never floating halfway down the frame.
- **Numbers are units.** A number big (two or three times its label) over a
  short label, as one block. Three or four of them: around the product with
  arrows pointing in, or in one bar divided by thin rules. Never a sentence
  with a number in it.
- **Lists stand beside the product.** In a split frame (product 40-55%, words
  the rest), four or five short lines, each with the same mark (a tick in a
  filled circle, a cross for the rival), the same gap between every line.
- **Proof is an object.** A quote is set as the platform shows it: the card,
  the avatar, the name with a flag or tick, the stars, "Read more", the
  helpful count. The card overlaps the product's edge or the product overlaps
  it; never both floating apart. A real review only (`PERSON_NOTE` rules).
- **Things overlap on purpose.** A seal or burst over the product's corner, the
  product breaking the headline, a hand entering the frame toward the words.
  Elements that float with gaps between them all read as separate stickers.
- **Small things live at the edges.** The logo in a bottom corner, on the
  margin the words keep (its outer edges as far from the frame's edges as the
  words are), set straight on a calm part of the picture: never in a box or
  tab of its own, and never pushed into the corner. The disclaimer and fine
  print go along the bottom edge, smallest of all. The
  website goes on the image only when the idea needs it as the call to
  action: Meta shows the link and its button under every ad, and the address
  is already in the primary text. An object in a real moment keeps only the
  logo.
- **Words on a photo sit on its calmest part**, or on a band that runs edge to
  edge (a solid bar, a gradient from transparent to dark over the bottom half),
  never on a box that stops short of the edges.

## The visual idea is a brief, not a blueprint

The concept's `visualIdea` says what the ad should do. It was written before
anything was drawn, often quickly, and it can describe one of the defaults
below. When it does, building it faithfully produces a weak ad on purpose.
Keep its subject and its point, and compose it properly: change the scale,
the ground, the crop, how many parts. Say what you changed, and why, in the
note you hand over. The concept's words (`texts`) are never rewritten this way;
adding a supporting level from the evidence is the one exception (*Say enough*).

Spend what the idea needs, and nothing to look busy. A type-only ad that
spends no credits is a real ad; a photograph that needs its hero generated
twice is worth the second try. Stop when the picture is right, not when the
first preview has no findings: the findings measure contrast and spacing, not
whether anyone would stop for it.

## One scene, one light

A collage of parts each lit differently reads as a collage. The rule is one
**light**, not one picture. For a photographic ad, the hero scene (the bowl,
the hand, the surface) is one picture, built around the pack when the pack is
in it (`build_scene`), with the empty area for type described in the prompt. Everything else that would
look better drawn than built is its own part, briefed in the same light:

- the carrier the words sit on, cut out: an object from the product's own
  world (see Words on objects);
- foreground pieces that give depth: a cut-out cracker, crumbs, a drip, a
  splash, a leaf, placed at different sizes and some slightly blurred. One to
  three pieces, each its own part, shaped like the real product as its shot
  shows it; a whole trail or spill belongs in the scene, not in one cut-out
  (`references/prompting.md`, Cut-outs);
- a backdrop or surface, when the hero part is a cut-out rather than a scene.

The 9:16 version is cut from the feed's backdrop, so it never needs one of
its own.

Use as many parts as the idea needs: one is often enough, and a part added
because the design "should have more" is clutter. A part that would look
better generated is not faked with rectangles and gradients to save money.
Vector devices (arrows, ticks, stars) are the exception; they stay `icon` layers.

Open every photographic prompt with the brand's `photoDirection`, word for
word. When it is not set, do not stop for it: write one yourself from the
brand's own pictures (its key visuals, its product photos, what its website
shows), one or two sentences of light, surface and colour, and open every
photographic prompt of the batch with the same words. Say in your report that
you did, quote it, and suggest the human saves it to the brand kit on the
board so the next batch matches. Repeat the light in every part's prompt ("soft window light from the
left, warm") so the pieces match, and the scene's colours in words ("a soft
milky brown, like the spread on the toast"): a colour code in a prompt
overshoots, and a part briefed in no colour comes back in its own. Lay `add_grain` over a photographic
composite last.

## Type

**Choose the ad's type idea first: `references/type-ideas.md`.** What the
words do in this ad (a number as the picture, a photo inside the letters,
words on a ribbon in the scene, lines pointing at the product, poster
capitals, an editorial page) is decided before any line is set, from the
hook and the picture. No two ads on a brief share one: `get_design` lists the
ones taken (`typeIdeasTaken`), and `finish_design` records this ad's and
refuses a repeat without a reason. The headline stacked over the photograph
is one idea among them, used once a brief at most. Everything below is how to
set the words well once the idea is chosen.

- **Three levels.** One clearly biggest (the headline, at least 1.6x the
  next), one second, the rest small. Headline at least 90px on the 1080 frame;
  in the strongest ads it fills half the width or more. Five or six words.
- **Words on a plane, not on texture.** A flat colour area, a plain wall, a
  dark slate, sky: generate the photo with that area empty ("the upper third
  is clean empty wall"). Never over wood grain, crumbs or a busy shelf without
  a carrier.
- **Words on objects.** Detail lines on a thing in the photograph are written
  by the model (`build_scene` method `photo`, `writeOn` and `writeLines`),
  read back letter for letter; the headline stays a layer. Choose the carrier from where the product lives: a recipe card or the pack's
  own cooking instructions for food, a till receipt or price tag for a shop, a
  chalk menu board for a café, a gift tag for a present, a phone notification
  for an app, a label on a jar, a luggage tag, a ticket stub. A sticky note is
  the `STICKY_NOTE` format's carrier, not a default: on an ad of another
  format it reads as the same trick again. Each ad in a batch gets its own
  carrier, or none; the preview flags a second ad with the one another
  already uses.
- **Every line says what the picture cannot.** A line that only names the
  product (a shoe's model and colour, "the latest" and its model, the jar's
  own label set again under the headline) tells a reader nothing the
  photograph has not: cut it, or make it the reason, the offer or the moment.
  The name goes on the ad only beside something that needs it (the model and
  its price, in an ad about the price). `preview_design` reports a line that only names a product.
- **Words in a few places, with an order.** The headline and its supporting
  lines read as one block; a callout stands next to the one thing it names;
  the logo signs from a corner of the frame on the words' margin (a bottom
  corner, or the top), never hanging under the headline mid-frame. Words in every
  corner of the frame (the headline top, a callout right, another
  bottom-left, the logo bottom-right) leave the eye no path. `preview_design`
  reports words that take all four corners.
- **No banner in the photograph.** When a scene leaves the words a place,
  make it an open part of the scene (a wall, the sky, a table seen from
  above), not a dark shelf or a strip with a straight edge across the whole
  frame under the words: that reads as a band laid behind them, the same as a
  drawn one. `preview_design` reports a hard edge across the frame beside the
  headline's block.
- **Depth.** The headline behind the product: the cut-out sits above the
  letters in the stack and breaks through them.
- **Devices**: arrows and rings from a fact to the product, ticks and
  crosses for a comparison, a starburst under a short word, stars for a
  rating. **Over a photograph, an arrow is hand-drawn** with `draw_arrow`:
  the model draws one arrow on paper and it is laid in the brand's accent
  (or the colour you pass) with its tail at `from`, beside the callout's
  words, and its point at `to`, on the thing they name.
  A vector arrow (`icon`) laid over a photograph is one even line square to
  the frame and reads as pasted on; the preview reports it. Set the words
  first, then draw each arrow from their edge to the thing, at each size.
  On a flat designed field, the `icon` devices (ticks, crosses, stars, a
  starburst) stay crisp vectors.
  **At most one ad in a batch uses devices**, and it is the one whose idea is
  about pointing (CALLOUTS, a comparison, a rating). Elsewhere they are the
  cheapest way to make words "belong" to a picture, which is why they turn up
  on every ad when nothing stops them. Make the link with scale, placement,
  depth or a carrier instead. Ask of every device: would the ad still work
  with it removed? If yes, remove it. `preview_design` reports a second ad in
  the batch that uses them.
  **An arrow points at what its words are about.** A claim about the
  product ("doesn't separate", "roasted longer") points at the product, never
  at a prop beside it (the glass, the spoon, the banana); a line about the
  prop points at the prop. Read each callout with its arrow before you
  finish: if the words would be true of the thing it hits, it stays.
  Icon arrows on a flat field keep their proportions whatever their box: give one a square box at
  the size you want and aim it with `rotation`. A stretched box only leaves
  empty space around it.
- **Emphasis** with `marks`: one word in the accent colour, a marker
  highlight, the brand's accent face, italic against the line, or struck
  through. One per ad.
- No glow, no outline, no gradient on type unless the idea is about it. No
  emoji in the image. An outline reaches the preview as a finding: it is
  contrast bought on the letters, and the picture should give it instead.
- **The logo reads too.** The preview measures its contrast like words. A
  dark wordmark on a dark seat or a wooden table is not there: move it to a
  quieter, lighter or darker area, or use the brand's other version of it.

### Setting it

**Start from the brand's type style.** `get_design` and `list_design_requests`
return `brandFonts`: the heading and body faces, and how the brand sets its
headlines (`style`: weight, capitals, italic, spacing, labels in capitals, an
accent face), with a sentence of it in `says`. A new design's headline and
`set_type` already follow it. It is a person's choice, read from the brand's
website or set on the board: keep it on every ad of the batch, and spend the
variety on treatments, never on changing how the brand's headlines are set.
When `says` reports it unset, say so in your finish note; never set it
yourself. **When the brand has no headline face of its own** (its heading
is a system face such as Roboto or Inter, and `says` tells you so), choose
one for each ad from the installed faces (`list_fonts`): a face that fits
that ad's idea and carries its language (Cyrillic for Bulgarian). Pass it
as `set_type`'s `face`, vary it across the batch (a serif for appetite, a
condensed grotesk for a bold claim, a rounded display for something
playful), and name it in your finish note so a person can make one the
brand's under Fonts. A brand with its own face keeps it on every ad.

The same face looks twice as good set the way a designer sets it:

- **Tight leading on big type.** Line height 0.9-1.0 at headline size; 1.2-1.35
  only for small lines. Default leading on a 120px headline reads as a gap.
- **Tracking by size.** At 100px and up, tighten: about -20 to -40
  (`charSpacing`, thousandths of an em). Small caps labels open up: +60 to +120.
  Condensed faces need less.
- **Break lines on meaning.** Put the break in the text ("Не ги изяждай /
  преди гостите."), never wherever the width runs out. No headline ends on one
  stranded word under a full line; a deliberate stack of one word per line is
  fine.
- **Scale contrast.** The biggest level at least 1.6x the next. Three levels.
  If everything is medium, nothing is read.
- **Even rhythm.** A list or a recipe is spaced like one: every group the same
  distance from the next, label tight to its own number.
- **Type as a picture.** A word so big the frame crops it; one word per line
  stacked into a block the width of the frame; a number a quarter of the frame.
- **Weight contrast within a line** only through `marks`, once.
- **Faces.** Display face for the headline, body face for the rest, the brand's
  accent face (`brandFonts.accent`) only for words set apart inside a line,
  handwriting only for something a hand wrote (a note, a tag). Never a face the
  brand did not choose. Suggest a better one to the human with `list_fonts`,
  never install or switch on your own.
- **Italic and capitals are drawn, never typed.** `italic` sets a layer in its
  family's own italic, offered only where one is installed (`italics` in
  `get_design`, `list_fonts`); there is no fake slant. `caps` draws the words
  in capitals while the concept keeps them as written: never type a line in
  capitals yourself, or the approved words change. Capitals want open spacing
  (`charSpacing` +60 to +120 small, 0 to +40 large), never tight.

### Treatments: choose one per ad

Setting the words well is the floor. A treatment is what makes the type part
of the idea. Choose the one the headline asks for, build it with `edit_design`,
and use a different one from the other ads in the batch.

- **Block.** The headline in short lines of one or two words, stacked into a
  block as wide as its space: leading 0.85-0.95, `charSpacing` -30 to -50,
  weight 800-900. Each line's break carries meaning ("Кафето / ти / изстина."). *When:* a short, punchy hook with a product beside it. *Ruins
  it:* lines that do not fill the block; a stranded short word.
- **One giant word.** The word that carries the hook set so big the frame
  crops it at one edge (a third of the frame tall or more), the rest of the
  headline small beside it. *When:* the hook turns on one word ("Хрупка.",
  "Неделя."). *Ruins it:* cropping that loses the word; two giant words.
- **Through the product.** The headline set big behind the product, the
  product above it in the stack, so it breaks through the letters. Every word
  stays readable around it. *When:* a product-hero ad. *Ruins it:* the product
  covering a word whole; the type so pale it reads as wallpaper.
- **Pack colour on one word.** One word of the headline in the pack's own
  strongest colour (`marks` with `fill`, from product_colours), the rest
  in ink. *When:* the hook names the thing the pack is about ("ягоди").
  *Ruins it:* two coloured words; a colour from neither the pack nor the
  palette.
- **Marker.** One word or phrase under a highlight (`marks` with
  `highlight` in a pack or palette colour at about 60% strength behind ink
  type). *When:* the line answers a question or makes a promise. *Ruins it:*
  a highlight on the whole line.
- **Struck through.** What the line says no to set with `strike`, the answer
  beside it in the headline's weight or the accent face: the old price beside
  the new, the habit beside the product. *When:* the struck-through past or a
  real offer. *Ruins it:* a strike on words the reader needs to read; an
  invented old price.
- **Spaced capitals.** A short headline of two to four words in `caps` with
  open spacing, as a sign or a label is set. *When:* the brand sets its
  headlines in capitals, or the hook is a name, a place or a time. *Ruins it:*
  a long sentence in capitals; capitals tracked tight.
- **Weight contrast in one line.** The headline's key words at 900 and the
  rest of the line at 400 in the same face (`marks` with `fontWeight`).
  *When:* a two-part hook where one part is the point ("Без захар. **Само мед**."). *Ruins it:* more than one switch.
- **A hand's aside.** A short handwritten line (Caveat, Pangolin) beside the
  display headline, slightly turned (`rotation` -4 to -8), with a drawn
  arrow when it points at something. It is what a person scribbled on the ad:
  "опитай го топло". *When:* a warm, personal brand voice. *Ruins it:* a long
  aside; handwriting as the headline itself; on the same ad as devices.
- **Quiet type, big picture.** The headline at its minimum size, one line, in
  a corner with generous margin, the photograph carrying the ad. *When:* the
  picture is the hook. Say so in the finish note, since the preview reports a
  narrow headline.

A chat, a note or a review card keeps the type of its object (NATIVE_SCREEN,
STICKY_NOTE, PERSON_NOTE): no treatment on its words.

Previews measure what can be measured here: collisions and lines that almost
touch (by the drawn letters, not the boxes), uneven spacing in a stack, loose
leading on a big headline, a stranded last word, two biggest sizes too close.
They also report flat type, as craft findings a finish does not wait on:
- a headline in a system face;
- default letter spacing at 100 px and up;
- a headline under 40% of the frame's width;
- a headline no heavier than the lines beside it;
- a third face.

Fix them, or say in the finish note why the setting is the idea.
- At 9:16 every word and the logo stay between y 270 and 1250, 65px from the
  sides, and out of the band's lower-right corner (right of x 920, below
  y 1000), where Reels' like, comment, share and save buttons run up the
  edge; the product's middle stays above y 1250. Stories puts its profile
  line over the top, and Reels its caption and Shop-now bar over the bottom
  35%. A picture may run to the edges; the thing the ad sells
  may not sit under the caption. The derived 9:16 keeps the words at the
  feed's size (smaller only when they cannot fit), the top lines pinned under
  the top of the safe area and the foot lines above its foot; on a flat
  ground the product fills the room between them, larger than in the feed
  where there is room. It is a starting point: look at it, place each line
  against the taller picture, and fix what the preview reports. A 9:16 that
  is the feed ad in miniature is not done.

## Appetite

Side or back light, never flat front light: it shows texture, gloss, steam.
Close enough to see the snap, the swirl, the crumb. Imperfection reads real: a
drip down the jar, a bitten piece, crumbs. Hands and motion: a hand reaching
in, a spoon lifting, a piece mid-dip. The product in use next to the pack, not
the pack alone. Overhead for spreads and bowls, 45 degrees for most food,
straight on for stacks.

## Defaults to break (they read as AI)

The headline band across the top, over a photo or a flat field: the header
strip. It is the first layout a model reaches for, it makes the ad a
letterhead, and a reference that has one is no reason to use one: three of
one brief's four designs opened with it. A product line in small grey at the
foot as an afterthought ("Product, 250 g"): Meta does not ask for it and the
pack already says it; leave it off. One line and a product on
an empty field. Everything medium-sized. A small flat illustration floating in a white
field with the headline under it. A coloured border round a white panel. A
generated picture dropped in as a square. A warm cream background with a serif and a
terracotta accent. A generic hand-holding-product on white. Stock window
light on a desk. A centred product with text above and below in every ad of a
batch. Five elements of equal weight. Spend boldness in one place and keep
everything around it quiet.

## The brief, before anything is generated

Write it out for yourself before the first paid call:

- **Goal**: the one thing the reader must get in half a second.
- **Locks**: the product shot (as is), the exact words (`texts`), the logo.
- **Freedom**: everything else — and say what you will use it for.
- **References and their jobs**: which board reference gives the layout,
  which the light, which the material.
- **Composition**: focal point, reading order, where the empty areas are.
- **Light**: the photography direction plus the direction of the key light.
- **Pass criteria**: what the preview must show to be done.
- **Example**: which principle from `references/examples.md` this ad takes,
  and how it differs from that example. Both go in the finish note.

## Judging the preview

`preview_design` returns findings and the critique questions. A finding about
a hard limit is fixed. One about a default is fixed, or, when the ad breaks
that default on purpose, answered in your note in one line.
Answer each against the picture, not against your intention. Then one
verdict, in your report to the human:

- **PASS** — you would put your name to it.
- **TARGETED FIX** — one named change, made, then preview again.
- **REGENERATE** — a part is wrong; say which and the new prompt.
- **BLOCKED** — what only the human can supply (a better product photo, a
  font, more budget).

Make every change a preview calls for in one `edit_design` call (it takes a
list of operations), then preview once: each call is a step, and every step
re-reads the whole conversation. Two or three rounds is normal. Reporting PASS on something you would not run
is the one unforgivable result.
