# The static formats

Nine formats, each typed as `adFormat`. Top food and CPG accounts run six to
eight at once; variety across formats beats volume of one. Each entry: what it
proves, when to choose it, how it is built with this pipeline's tools, and what
ruins it.

## HEADLINE_PRODUCT — one line, the product as hero

- **Proves:** one specific claim, said with confidence, and what the product is.
- **Choose when:** the hook is strong alone and the pack is good-looking.
- **Build:** the photograph first, in the pack's signature colour: the real
  pack placed big, then `build_scene` makes the surface, the wall and the
  light round it in that colour (a pink box on a pink tiled counter, a dark
  pouch on dark slate), with its contents spilled at its foot as part of the
  same photograph. Headline huge, top third, on the scene's quietest plane.
  Under the headline, a second level: the product's one reason, and two or
  three short facts or a price sticker, set on the scene or a carrier. Never
  the product's name and weight: the pack says them. The product is big: half the frame's width or more, no wall of
  nothing between it and the headline. Never the pack cut out onto a flat
  colour with props pasted round it: that is a catalogue page.
- **Ruins it:** a second claim competing with the first; the pack small; the
  headline alone over an empty field, which says nothing to a stranger.

## CALLOUTS — the product with facts pointing at it

- **Proves:** what is in it, checkably. Reads as information, not promotion.
- **Choose when:** the product has 3–5 concrete facts buyers ask about
  (ingredient, origin, weight, what it lacks).
- **Build:** pack centre on its colour field. Each fact: a short number or word
  big, a two-word label small, an `icon` arrow (`arrow-curved` or `arrow-loop`,
  turned to aim) from the fact to the part of the pack it is about. Headline top,
  short. This is the batch's one ad with devices; no other ad in the batch
  uses arrows or rings.
- **Ruins it:** more than five callouts; arrows all the same angle; facts the
  label does not support.

## US_VS_THEM — ours against the default

- **Proves:** why this one, by contrast with what the reader buys now.
- **Choose when:** there is a checkable difference (butter vs vegetable fat,
  five ingredients vs a list).
- **Build:** two columns or a table with heavy rules. Ours: the real pack, warm
  material or the signature colour. Theirs: a blank generic pack (generated,
  unbranded, cut out) labelled "обикновени …" — a category, never a named
  rival. Rows of short lines with a full stop; `tick` and `cross` icons. Make the
  last row the punchline, a joke instead of a fact.
- **Ruins it:** naming a competitor; claims about them you cannot prove; rows
  that are adjectives.

## INGREDIENT_EXPLOSION — what is inside, flying out

- **Proves:** real ingredients, with motion and appetite on a still image.
- **Choose when:** the ingredients are visual (nuts, cocoa, berries, herbs).
- **Build:** pack centre, front-on or slightly turned, on a plain ground from its
  colours. Generate the ingredients flying outward from a clear centre, same
  light as the pack's shot, with the centre empty, then add several cut-out
  pieces as separate parts in front of the pack, at different sizes and with
  slight blur, for depth. Headline top. `add_grain` last.
- **Ruins it:** ingredients the product does not contain; a cluttered frame
  with no clear centre.

## STICKY_NOTE — words written by a person, stuck in a real moment

- **Proves:** a human truth, said like a note at home. Low polish reads as
  real and gets past the reader's ad filter.
- **Choose when:** the hook sounds like something a person would write on a
  note: a warning, a reminder, an instruction to a housemate.
- **Build:** a generated scene in natural light (a kitchen counter, a bowl, a
  fridge door, a gift bag) with the food in it and the note's spot visible.
  Generate the blank note as its own part (cut out, same light), place it on the
  object, turn and slant it to sit on the surface, and set the words on it in
  the handwriting face. A crumb or a piece of the food in the foreground, as
  another cut-out part, adds depth. Pack: `IN_SCENE`, the real product on
  the counter beside the food and built into the scene with `build_scene`, or
  `NO_PACK` with the food recognisable (drawn with `foodFrom`, so it is the
  brand's own food). When the note is stuck on the
  product itself: place the real product, generate the blank note (cut out, flat, straight on) and lay it on
  the product's face, then `build_scene` with both in `layerIds`, so the
  photograph is made round the product with the note already on it. Set the
  words on the note after.
- **Ruins it:** typed-looking words on the note; a note floating off the
  surface; a polished studio scene.

## FOOD_IN_HAND — appetite in motion, the pack in the scene

- **Proves:** that it is irresistible, by showing someone unable to resist.
- **Choose when:** the hook is an exclamation or a confession.
- **Build:** the real pack placed first, standing on the surface in a lower
  third, then `build_scene` around it: a hand reaching into the bowl or lifting
  a spoon beside it, the food close, two-plane background (wall and surface)
  in the pack's colours, side light, the top third clean wall for the
  headline. Add foreground food (a crumb, a drip, a piece mid-fall) as cut-out
  parts in the same light, with `integrate_image`. Headline huge, chunky,
  top-left, the hand reaching into it if possible.
- **Ruins it:** the hand's anatomy (check the fingers); the pack so big the
  food is lost, or laid over the photo instead of standing in it; the headline
  on the busy part of the photo.

## DATA_HERO — one number

- **Proves:** a single fact so specific it is persuasive by itself.
- **Choose when:** there is one striking, true number (one ingredient, 3
  spoons, 0 added sugar, 250 g of only nuts).
- **Build:** the number enormous (a quarter of the frame or more), what it
  means in one small line under it, pack beside it. Flat field from the pack.
  Nothing else.
- **Ruins it:** two numbers; a number that needs an asterisk.

## PERSON_NOTE — someone's own words

- **Proves:** trust, through a real person's voice (a founder, a customer).
- **Choose when:** there is a real quote with a surprising specific, or a
  founder's line only they could say. Never invented.
- **Build:** the words large, as a handwritten note, a card or a plain quote with
  the name small under it; a real photo of the person or their hands with the
  product; stars as `star` icons only for a real review.
- **Ruins it:** generic praise; an invented customer; a stock face.

## NATIVE_SCREEN — a chat, a note, a notification

- **Proves:** a relatable moment in the reader's own interface; reads as
  content, not as an ad.
- **Choose when:** the hook is dialogue, a list someone would keep, or a
  message someone would get.
- **Build:** the screen as the whole picture (full-bleed, the platform's own
  look: real bubble shapes, real spacing, system font sizes) or a phone held in
  a real moment with the screen as a separate layer. The product appears in the
  conversation itself (a photo sent in the chat) or as the real moment behind.
  Never a mock-up floating on white above a separate photo.
- **Ruins it:** a fake-looking interface; a fabricated post presented as real;
  words laid outside the screen, such as a footer of dates, an address or a
  URL printed on the scene round the phone. What the screen does not say goes
  in the primary text.

### Building a chat that reads as real

Two ways, both real-looking. The chat itself, its header, bubbles and words,
is built the same way in both.

**A phone in a real moment.** A photograph of a phone propped up on the
counter or held in a hand beside the product, with our chat on its screen.
The phone and its chat are drawn by the image model, the words written on the
screen itself: a flat screen of layers on a photographed phone never looked
real (no glass, no glow, square to the camera in a scene that was not). In
this order:
1. Place the real product (cut_out_image) at its final size beside where
   the phone will stand, and build the photograph with build_scene method
   photo: the model draws the product into the place, its label read back.
   Describe the place, the surface and the light; leave room for the phone
   and the headline. The phone comes after: photo replaces what is under the
   product with the photograph.
2. draw_screen with the conversation (the contact's first name, the status
   bar's time, three to six messages typed the way people text, who sends
   each), `phone` (how it stands: "upright, screen to the camera") and `at`,
   the phone's box in the frame: big, its screen at least half the frame's
   height. The model draws the phone alone with the chat written big on its
   screen, read back blind word for word; it is cut out and stood in `at`.
   One draw a call, three a design request: a failure is paid for and comes
   back to you. Change what made it fail before another (shorter messages, a
   bigger box), never draw again for layout.
3. Then the phone stands in that photograph: build_scene method settle with
   the phone alone in `layerIds` gives it its shadow and the scene's light.
   The product is never settled or built the old way: it is already in the
   photograph.
4. The headline stays a text layer beside the phone. Never cover the screen
   with a text layer or a shape: to change a word, draw the screen again.
5. derive_story_version makes the 9:16 from it: the feed's scene continued
   above and below (about a credit), the phone and the product at their feed
   size on their own shadows, the words and the logo laid out clear of them.
   draw_screen refuses a second phone there. Adjust the words with edit_design
   only where the preview asks; never build_scene again at 9:16.

The green screen (a phone generated with a pure #00FF00 screen, built into the
scene, then fit_screen and set_chat) is the older way, kept for designs built
with it.

**With a phone, the ad can carry a headline beside it.** The phone holds the
conversation; the ad round it can say the hook in the brand's display face,
above or beside the phone, at headline size, set like any headline (a
treatment from the skill's Type section). Then the chat on the screen carries
the moment in UI_CONTENT lines typed the way people text, and the headline is
never repeated inside it. The preview judges only the lines on the screen as
messages, and a headline outside it as a headline. Without a headline outside,
the hook is the message that matters, inside the chat, at the chat's size.

**The conversation as the whole picture.** A screenshot cropped to the
conversation, zoomed to fill the frame, on the chat's own plain light ground.
No scene behind it, and no phone outline.

The chat, in both:
- **A status bar at the very top** of the screen: the time on the left
  ("21:14"), signal and battery on the right, small and grey or black.
- **The newest message at the bottom.** A messenger fills from the bottom
  up: the last message sits just above the field you type in, and earlier
  ones above it. Never a short chat floating mid-screen with empty white
  under it.
- **A header across the top**, as the app draws it: a small round avatar (an
  ellipse with an initial, or a cropped photo with `radius`), the contact's
  first name, and "на линия" or a last-seen line in small grey type. No real
  app's name or logo: the look of a messenger, never a brand's.
- **Bubbles are rounded rects that hug their words**: as wide as the text
  plus an even padding of about half the type size each side, `radius` about
  the type size, never one bubble width for all:
  - the other person's on the left, in light grey or white;
  - the reader's own on the right, in one colour, from the brand's palette
    when it reads as a messenger colour, otherwise a plain messenger blue or
    violet.
  - **Every message is one size and one weight**, as a messenger sets them:
    fit_screen's size on a phone, 56–72 px for a whole-picture chat, one
    plain face (the brand's body face) at regular or medium weight. The hook is the HEADLINE layer only because it
    is the message that matters. It is never set bigger or bolder than the
    others: a chat with one huge message reads as a poster in bubbles.
  - **A conversation, not a line.** Three to five short messages. Often the
    reply comes split in two ("има" / "ела довечера"). Add them as UI_CONTENT
    lines with edit_design when the concept gave fewer.
  - **The contact has a first name**, often shortened ("Мими", "Ники",
    "мамо"), never a role like "Friend".
  - **No empty input bar** or keyboard taking a third of the frame: crop to
    the conversation.
- **The small things that make it real:** a time under or beside each bubble
  (24–28 px, grey, like "21:14"), and "Видяно" or ticks under the last one
  sent. A typing indicator (three dots in a bubble) where the reply is coming.
- **The product is in the conversation:** the real product shot sent as a
  photo, an image layer inside a bubble with `radius`, on its own clean ground.
  Or a photo of the real moment sent, built with build_scene round the real
  product and placed as that photo.
- **The logo** is small, outside the conversation: a corner of the frame, as
  a signature. Never inside a bubble.
- **The words in the bubbles are typed, not written.** The concept's lines
  are set the way people text in that language. Set them that way with
  edit_design, even where the concept wrote them as ad copy; the meaning stays.
  - Lowercase at the start is normal.
  - No full stop at the end of a short message: it reads cold. A question
    mark stays.
  - Spoken forms (Bulgarian "оня", not "онзи").
  - A reply often split into two short bubbles.
  - No emoji: no face draws one, and set_chat takes them out.
  - The product named the way a person would ("оня мед"), never with its
    weight.

  The ad-copy skill's language reference has the rest (for Bulgarian,
  `ad-copy/references/languages/bg`).

Never draw a phone from shapes, and never lay bubbles straight on a
photograph: both read as a mock-up, and the preview holds it twice ("Reads as
real"). The chat always stands on a screen: a phone drawn with draw_screen, the
fitted "Phone screen", or the chat's own ground filling the frame.

**Never:**
- a phone cut out and laid over a scene;
- a phone drawn from shapes;
- a phone bigger than the frame, or turned away from the camera;
- a product floating over the screen;
- a model asked for the chat's words any other way than draw_screen, which
  reads them back;
- message boxes with headline-size type and no chat around them.

The preview reports a cut-out running off the frame and a large one laid over
a built scene. On a NATIVE_SCREEN design, its "Reads as real" check holds the
finish on any of these:
- messages of different sizes, in display weight, too few or too small;
- a closing full stop or a written form in a typed message;
- a contact named for a role, or an avatar whose letter is not theirs;
- a bubble that does not hug its words;
- a chat not pinned to the top and filled from the bottom of its screen;
- a chat over a photograph with no screen under it.
