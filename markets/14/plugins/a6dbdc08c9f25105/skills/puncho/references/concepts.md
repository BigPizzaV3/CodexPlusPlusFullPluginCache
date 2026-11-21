### 2. Concepts

Use `get_generation_context`, write the concepts yourself, then `store_specs`.
Prefer this over `generate_specs` — you can look at the reference images, and
`generate_specs` cannot. A batch belongs to a brief: `create_brief` makes one,
`list_brands` lists a project's briefs with their ids, and `list_specs` lists
the concepts already written, by brief or status.

**Ask what the campaign sells on before the first concept.** A brief names one
or more leads: an offer (a real deal, or the price as the argument), a feeling
(a moment, a mood, who you are with it), proof (reviews, numbers, press), the
product (how it is made, what it does), a problem it removes, or something new
(a launch, a season). People want things for more than one reason, so several
is normal. Suggest the ones the goal points to, in a sentence, and let the
person choose: it is their campaign. If they tell you to go ahead without
choosing, record the ones you suggested, say which, and that they can change
them under Sells on. Record them in `create_brief` (`leads`) or,
for a brief that has none, `set_brief_leads`. Every concept then records the
one it leads with (`lead`), a batch covers each of them, and the words on the
image follow `leadPlan` in `get_generation_context`: a price only under an
offer. The brief's `offer` is a real deal or nothing, never the product's
price.

**Load the `ad-copy` skill before you draft.** It carries the substitution test,
the paraphrase test, the symmetry rule, the deficit-framing rule, and real
rejected copy from this project with the reason each one failed. It is a better
bar than anything you will reconstruct from memory, and the failures in
`references/anti-examples.md` were produced by a model reasoning exactly the way
you are about to.

Then, specifically:

- **Actually open the reference images.** Pass `InspoItem.imageUrl` and
  `OrganicPost.mediaUrl` to `view_image`. The stored classification is someone's summary; the
  image is the evidence. You cannot borrow a format you have not seen.
- **Experiment.** The copy rules are defaults, not laws. Every batch of five has
  at least two `EXPERIMENT` concepts that break a default on purpose, labelled
  and explained, and `get_attribute_rollup`'s `byBet` reports whether they beat
  the core ones. Freedom is in the creative only: nothing about approval,
  pausing or spending changes.
- **The look comes before any ad is built.** `get_generation_context` and
  `list_design_requests` return `look`. When `look.warning` is set, say what
  `look.missing` lists once, before designing: designs built in no look (the
  fallback font, a white field, no product palettes) were judged as ads and sank
  good copy. Nothing refuses; it is on you to say it, and a person who says to
  go ahead gets the design in the fallbacks, with what was missing noted. Propose what is missing: a
  palette per product taken from its pack (`save_palette`, after a yes), fonts,
  the background.
- **Keep the human's decisions.** When they say something in chat that should
  hold for every future batch ("no production numbers", "«полезен» is
  allowed", a confirmed fact), call `record_decision` at once with their words,
  one rule per call, and tell them it is on the board. Do not ask first: it is
  their decision, and a decision kept only in this conversation is lost to the
  next one. Never record your own conclusions or a one-off pick for this batch.
- **The human outranks the brief and the skill.** Board notes, their edits to
  concepts and what they say in chat win over the brief and every copy rule;
  the brief wins over the skill's defaults. Legal risk (health claims,
  certified terms) is said once, with the rule, and written into the concept's
  rationale for whoever approves it, then you follow the human. Never "correct"
  a human's edit back to a rule. The `ad-copy` skill's "Who decides" has this.
- **Read the board notes.** They are written by a human after the brief and
  usually correct it. A note that contradicts the brief wins — and say so out
  loud, so the brief gets fixed rather than silently overridden every run.
- **Cite what you borrowed** in `sources`, using the ids from the context.
  `SHAPE` for a layout, `VOICE` for a register, `MECHANISM` for the persuasion
  move, `SUBJECT` for the claim. A concept citing nothing is a concept written
  from the category average, which is the failure the whole pipeline exists to
  prevent.
- **Cross your sources.** Take the layout from one reference and the persuasion
  move from another. The strongest concept in the last batch put a POV framing
  borrowed from a food-delivery ad inside a screen-capture layout borrowed from
  a software ad, and neither parent is recognisable in the result — which is the
  point. When `SHAPE` and `MECHANISM` both come from one competitor ad you have
  translated it rather than built on it, and it reads like the thing it came
  from. `store_specs` warns you when this happens.

  Taking both from the **brand's own organic** is a different thing and is
  fine — that is voice transfer, and material the brand already owns and already
  knows works is exactly what should be ported wholesale.
- **Name what each hook pushes against**, in `tension`, and spread *that* across
  the batch before you worry about anything else. Five concepts can carry five
  angles and five shapes and still all push against the same thing — the tension is the
  argument, the angle is only how it is dressed. A batch with one tension has
  tested typography, not strategy.

  Never the reader. Deficit framing — you have no project, you missed it last
  time — is the nearest available tension and the easiest to reach for. It tests
  as relatable and it makes the reader the loser of an ad they did not ask to be
  in. Same antagonist, opposite direction: write from their potential.
- **Read `rejectedConcepts` before you draft.** A human already refused those,
  and the rejection is of the *mechanism*, not the wording — coming back with a
  reworded near-miss is the same concept. They are judgements made about real
  creative rather than intentions written down in advance.
- **Read `voice` before you draft, and run the voice pass and the read-aloud
  pass before you store.** `voice.edits` are a person's own rewrites of your
  lines, the strongest evidence of how the brand talks: turn them into rules
  and apply them to every line. `setup.answers` shows how the human rewrites
  standard copy, trait by trait. Then read every line out loud as a person in
  that market would say it, and rewrite what nobody would say. Writing in
  Bulgarian, read `ad-copy/references/languages/bg` first. The `ad-copy` skill
  has the details.
- **Spread the batch.** Across angles and across shapes. Five variations on one
  angle is one test; five POSTERs is one visual test. `store_specs` warns you
  when a batch collapses — take the warning seriously rather than explaining it.
- **Label `angle` and `hookType` honestly.** They are what the rollup groups by.
  A mislabelled angle corrupts the only feedback this system has, and it is the
  easiest thing in the world to get wrong by picking the one that sounds best.

### Voice

The human sets up the voice once, on the canvas: twelve lines of standard ad
copy to say their way. After that, the voice is yours to apply — the voice pass
above — and you never ask them to rewrite lines.

If `voiceWarning` is set in the generation context, the setup is not done or not
finished. Say so once and suggest they do it first (Voice frame, Set up your voice,
about five minutes); if they would rather go on, draft without it. You cannot do it for them, and there is no
tool that would let you: a model answering the setup would be inventing the
voice it is meant to learn.

When the human pastes emails or messages into the conversation, store them with
`add_voice_samples` — only the part the brand wrote, one message per item, no
addresses — and set `audienceSegment` to who each was written to. Mute one
that is the wrong register for ads with `set_reference_active` (`VOICE`).

### 3. Ideas: the hook, the words, the visual idea

**Load the `ad-design` skill** before choosing formats or writing visual
ideas, and again before building any design. It holds the format playbook, the
product modes, the type and appetite rules, and how to judge a preview; this
file only says how the tools fit together.

Every idea carries an `adFormat` and a `productMode` (typed; the rollup
compares them). Spread a batch across at least three formats: Meta treats ads
of one format and setting as one creative. A product that is shown stands in
its scene (`IN_SCENE`, built with `build_scene`), never laid over a photo;
`NO_PACK` is for an idea better without it. `store_specs` makes you choose one
for every idea.

A concept you store is an **idea**, not an ad yet. Nothing is drawn. It carries
the hook and copy, **every word that will appear on the image** in `texts`, and
the art direction in `visualIdea`. The human reads the ideas on the board and
picks the ones worth building by pressing **Design this**, with a budget. Ideas
can be stored before the look is set.

**Write `visualIdea` as a designer's brief**, because it is what you, or anyone,
will assemble the ad from:

- What the eye hits first, and what is in the picture and where.
- The background, the light, the materials, the palette colours by hex.
- How big the type sits against the picture: "the headline huge across the top
  third, the product filling the lower half".
- What is **placed** as it is (the product shot by its label, the logo) and what
  is **generated** as a part ("a hand pressing a cracker into hummus, cut out",
  "a dark slate surface with crumbs, top-down").
- Words by role ("the badge, tilted, over the jar's shoulder"), never quoted.
- **Where the words live in the picture**: on a generated object (a note, a
  tag, a label), behind the product, along a surface. Never "headline at the
  top, photo below".

**With nothing to place** (a school, a service, an event: no product shot),
the picture is the thing the headline is about as a real object with material
and light, filling the frame or cropped by it, or the word itself as the
picture. Never a small flat illustration centred in an empty field with the
headline under it, and never a border round a white panel. The `ad-design`
skill says why, under "When there is nothing to place".

**Sharpen before storing.** For every idea the human liked, write three harder
versions of the hook and of the visual idea: more specific (a real moment, a
real number from the product's details), more tension (name what it pushes
against), shorter. Show them side by side, say which you would run and why,
and store that one. The first version that works is rarely the best one.

**The picture is the idea.** Decide what the eye sees that makes the headline
true before polishing the words: a stopwatch stopped at 4:00 for "dinner in four
minutes", a struck-through price tag for "what it used to cost", the real product
mid-use. A picture that only decorates the headline is a stock photo. Spread
compositions across a batch the way you spread shapes: five "product centre,
headline above" ads are one visual test.

**A product brand's ad shows the real product.** Name a product shot from
`productShots` in the visual idea; the design places that file. An image model
redraws a product it is shown, and a redrawn product is one the store does not
sell. No product shots yet? Ask the human to paste them into Brand assets and
mark them Product.

Each product shot carries what the human wrote about it: `price` exactly as the
store shows it, `productUrl`, and `details`. Copy about a product states those
facts and quotes the price as written. Never invent a price, size or material;
if a concept needs a fact that is not there, ask for it.

### 3b. Every word on the image is a field

`texts` holds **every word that will appear on the image**: headline, captions,
badges, small print. Exactly one is the `HEADLINE`, and it is the hook. Once the
idea is designed, the design's text layers are those words, and the concept
reads them back on every save.

This is the one contract most worth getting right, because breaking it is
invisible. Six lines of Bulgarian ad copy were once found living inside an
`imagePrompt` as `three short lines exactly: "…", "…"`. They were good copy. No
human ever reviewed them, the brief's constraint list never read them, and they
rendered into an image that was shown for approval as though the only copy was
the hook. A word in a generated picture is the same failure: never ask a model
to draw lettering, and never put quoted words in `visualIdea`.

Run `lint_specs` with the batch's `briefId` after storing it; it catches banned
terms, over-length copy and a headline that has drifted from the hook the
rollup credits. A clean lint
does not mean the copy is good. The bar is the `ad-copy` skill.
