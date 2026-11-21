# Type ideas: what the words do in the ad

The strongest statics are not a photograph with a headline over it. In most
of them the words are the design: a number so big it is the picture, a photo
seen through the letters, words printed on a ribbon in the scene, a line
pointing at the thing it names. Our ads came out one way for months, the
headline stacked over the photograph with a line under it, ad after ad, and
read as a template however good each picture was.

Each finished ad records its type idea (`finish_design` `typeIdea`). **No two
ads on a brief share one**: the finish is refused unless `repeatReason` says
why the repeat is the point. `get_design` lists the ideas the brief's other
ads took (`typeIdeasTaken`): read it before you start, not at the finish.

These are ideas, not layouts. Each says what the words do; where they go, how
big, in what face and against which picture is this ad's own, from its hook
and its photograph. Two ads with one idea built two ways are still one idea
twice. An idea not on this list is welcome (`OTHER`, and say what it is in
the note); the list is a vocabulary, never a menu to fill.

**Choose from the hook, then the picture.** A hook that turns on a number
wants the number big. A hook about a feeling wants a calm editorial page. A
hook about what is in the product wants words pointing at it. Write the idea
in your brief before the first paid call, with the one thing it must get
right.

**Every idea is built in code, never drawn.** No image model is asked for
letters, so a model never draws the number, the paper type or the words on
the ribbon. The picture inside the letters, the ribbon, the tag and the paper
are parts with no words on them; the words are text layers set on them.

---

## NUMBER_AS_PICTURE

A number, or one or two short words, set so big it is the picture: two thirds
of the frame's height or its whole width, in the heaviest weight, tight. The
rest is small beside it: what the number counts, in two or three short lines
("години опит" beside a "20"), the offer on a sticker, the product in front.

- **Seen in:** "20" with "years of experience" beside it; "87%" in mint on
  violet, cut by the right edge, the claim in three small lines to its left
  and a starburst sticker over its foot; "14+" white on black with "days on
  the wrist" under it; "-15%" in a condensed face, the offer under it.
- **Build:** a HEADLINE of up to six characters at 200px and up. It may run
  off one edge by up to a fifth of its letters (`bleed.ts`): the crop says
  "bigger than the frame". Tracking -40 to -80. The small lines hang off the
  number's edge, never centred under it as a caption.
- **When:** the hook is a number a reader would repeat: a count, a share, a
  duration, an age, a price drop. A real number from the evidence only.
- **Ruins it:** a number that means nothing without a sentence; a second big
  thing competing with it; the number in the middle with space all around (it
  must feel too big for the frame).

## PHOTO_IN_LETTERS

A photograph or texture seen through big letters, usually a number: the house
inside the zero of "20".

- **Build:** `fillImage` on the text layer: a picture the design already
  holds (a part, a scene, a product photo). It covers the text's box, so a
  photo whose subject is in its middle lands in the middle letters. The face
  must be heavy and wide enough for the picture to read: 800-900, 300px and
  up. The ground behind is calm and dark or light against the photo's tone
  (the contrast check reads the photo's average colour).
- **When:** the hook is about a place, a material or a result you can show,
  and a number or short word carries it ("20" years and the house built).
- **Ruins it:** thin letters (the photo becomes noise); a busy photo with no
  middle; a picture that has nothing to do with the word.

## TYPE_AS_MATERIAL

Letters that read as made of something: paper cut-outs standing on a desk,
card letters casting a shadow, letters textured like the product.

- **Seen in:** "90 000" as thick white paper numbers on violet card, a pink
  ribbon across the corner carrying the offer.
- **Build:** the letters filled with a texture part (`fillImage`: paper,
  card, concrete, the product's own surface, generated with no words) and a
  shadow cast on the ground (`shadow`, offset down and soft). The ground is a
  surface part in the same light. Never a model asked for the letters.
- **When:** a number or short word that should feel physical and crafted:
  a milestone, a count, a launch.
- **Ruins it:** a shadow in a different direction from the scene's light; a
  texture so strong the word does not read.

## PRODUCT_THROUGH_TYPE

The product in front of the type, breaking it: a band wrapped through the
"14", the laptop resting over the foot of the "87%", a can standing in front
of a giant word.

- **Build:** the headline huge, then the product cut out above it in the
  stack, overlapping one part of the letters and leaving the rest readable.
  `set_type` GIANT_WORD does this with a depth cut; by hand it is the cut-out
  placed over the text layer.
- **When:** a product-hero ad whose hook is a word or a number.
- **Ruins it:** the product covering a whole letter or digit; the word so
  pale it reads as wallpaper behind it.

## POSTER_CAPS

Capitals stacked into a block, each line set to fill the width, heavy and
condensed: a protest sign, a gig poster.

- **Seen in:** "YOUR SYLLABUS CHOSE VIOLENCE" white on red, four lines, each
  as wide as the frame, the product small in a corner with its name.
- **Build:** `caps`, a condensed heavy face, leading 0.85-0.9, each line its
  own size so it runs the full width (one text layer a line, or one layer
  with the breaks where the meaning breaks). The product is small and late.
- **When:** a hook with attitude, said loud: a joke, a provocation, a slogan
  the audience would put on a shirt. Short words, four lines at most.
- **Ruins it:** a long or careful sentence; a polite face; the product big
  enough to compete.

## WORDS_ON_OBJECT

The words printed on, written on or stuck to a thing in the scene: a ribbon,
a tag hanging from the product, an oval label pinned to the ground, a strip
of torn paper, a receipt, a sticker, a note.

- **Seen in:** a pink satin ribbon running diagonally across the corner with
  the offer on it; an oval paper label held by a pin with the date of the
  offer; a torn mint paper strip with the plan's name; a starburst sticker
  "try it free".
- **Build:** the carrier as a part with no words (a ribbon, a tag, torn
  paper), lit like the scene; the words as a text layer turned and slanted
  with it (`rotation`, `skewX`). The starburst is an icon. Choose the carrier
  from where the product lives, and one carrier a brief.
- **When:** an offer, a date, a plan's name or a small claim that should feel
  physical, not printed over the picture.
- **Ruins it:** a carrier floating on nothing; words not following the
  carrier's angle; the same sticker on every ad.

## POINTING

Words that point at the picture: callouts with thin leaders and dots on the
product, a handwritten note with a drawn arrow, labels standing over things.

- **Seen in:** a dark card on green, three callouts ("card limits", "merchant
  rules", "automatic blocking"), each a short label on a thin line ending in
  a dot on the card's edge; a spoon of almond butter with "dark and glossy"
  handwritten beside it and a curved arrow to the spoon.
- **Build:** the label a text layer; the line an icon (`line-down`,
  `line-up`, `line-flat`, or `leader-right-down` and its three mirrors, which
  run flat under the words and then bend to the point), `weight` 2-3 px; the
  dot a small ellipse in the accent where the line ends. Labels on both sides
  of the product, never all in one column. A handwritten note uses
  `arrow-curved` or `arrow-loop` and a handwriting face.
- **When:** the hook is about what is in or on the product: features,
  ingredients, the texture, three reasons.
- **Ruins it:** more than four callouts; lines that cross; lines ending in
  empty air near the product instead of on it.

## EDITORIAL

A face with character, set calm, with the photograph leading: a food
magazine's page. Big serif or characterful display headline in two or three
lines in a corner, a full-bleed photograph close on the food or its texture,
the product placed, almost nothing else.

- **Seen in:** a spoon of almond butter on olive green under a big warm serif
  headline; yoghurt's texture filling the frame under a cream serif headline;
  peppers on a board with the headline in a green serif low on the wood.
- **Build:** the brand's heading face when it has character (a serif, a
  rounded display, a slab); if the brand has only a system face, choose a
  serif or a display face with character for this ad (`set_type`'s `face`). Headline 80-120px, leading 1.0,
  in a palette colour lifted from the photograph. One supporting line at
  most. The photograph is the best you can make.
- **When:** appetite, craft, origin: the feeling of the thing.
- **Ruins it:** a neutral grotesk (it becomes HEADLINE_OVER_PHOTO); a busy
  page; a flat or stock photograph.

## NATIVE

The type of the object the ad copies: a chat, a note, a review, a search box.
Its own rules: `formats.md`, NATIVE_SCREEN, STICKY_NOTE, PERSON_NOTE.

## HEADLINE_OVER_PHOTO

The headline stacked over the photograph with a line under it and the call
to action at the foot: what every ad was. It is allowed, once a brief, when
the photograph is strong enough to carry the ad alone. It is never the
default.
