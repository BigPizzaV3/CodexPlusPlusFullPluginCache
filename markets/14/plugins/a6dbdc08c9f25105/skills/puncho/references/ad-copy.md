# Writing ads worth spending on

Generic ad copy is the default output of any model asked to write an ad, because
the training data is mostly bad ads. Avoiding that is not a matter of trying
harder or of adding adjectives to the prompt. It is a matter of writing from
evidence the brand already owns, and killing anything that could have been
written without it.

## Who decides

Rules in this skill, the brief and the human's word conflict. In order:

1. **The human decides.** Board notes, their edits to concepts, and what they
   tell you in conversation win over the brief and over every rule in this
   skill. An edit that uses a word this skill or the brief bans is not a
   mistake to correct: it is a decision, and the word is allowed for this
   brand from then on.
2. **The brief** wins over this skill's heuristics. Much of a brief is written
   by an agent from its own research, so it is a starting point, not a law: if
   a constraint looks like taste rather than fact or law, say so and ask.
3. **This skill's heuristics** (the tests, the crowded claims, the symmetry
   rule) are defaults. They decide only where nobody has.

**The law is flagged, not enforced.** Health and nutrition claims, certified
terms and fake reviews carry real risk. Say it once, with the rule ("«полезен»
is a general health claim under EU Reg. 1924/2006"), put it in the concept's
`rationale` so whoever approves it sees it, and then follow the human. Never
silently drop their line, and never raise the same flag again after they have
decided.

## Rules are defaults; results decide

Everything below describes what has worked. None of it is a law except the
few hard limits at the end of this section. The best ads are usually found by
someone breaking a default and the results proving them right, and this
pipeline measures results. So:

- **Every batch has two kinds of concept,** recorded in `bet`. Most are
  `CORE`: built from the brand's evidence and these defaults. **At least two in
  a batch of five are `EXPERIMENT`**: each breaks one default on purpose, and
  its rationale names which and what a result would teach. The rollup reports
  experiments against core (`byBet`), so the next batch knows whether breaking
  rules paid here.
- **What an experiment can break:** no reference at all; a tone the brand has
  never used in ads (deadpan, absurd, tender, blunt, long); a composition no
  reference on the board shows; a line one of the tests below would cut; a hook
  with no antagonist; a format the category never uses; the product as a
  character; one word on the image; a question with no answer. Anything that is
  not a hard limit.
- **The tests are warnings, not cuts.** A core concept should pass them. An
  experiment may fail one on purpose, and says so.

**Hard limits, for every concept:** a false or invented fact (unconfirmed is a
question to the human, not a cut); an invented customer, review or testimonial;
a mechanism a human has already rejected. Legal risk is flagged, not enforced
(see "Who decides"). The safety rules of the pipeline never move: everything is
paused, a human approves every ad, and nothing is spent without asking.
Freedom is in the creative, never in the money.

## Before you write a word

1. **`get_generation_context`** for the brief, brand kit, references, board notes
   and any winning attributes.
2. **Actually look at the reference images.** Open each with `view_image`
   (`InspoItem.imageUrl`, `OrganicPost.mediaUrl`). The stored classification is a
   summary someone else wrote; the image is the evidence. You cannot borrow a
   format you have not seen.
3. **Read the board notes.** They are written by a human after the brief and
   usually correct it. A note that contradicts the brief wins — and say so, so
   the brief gets fixed rather than silently overridden on every future run.

If the references are untagged, classify them first. Generating from an empty
reference set produces category-average copy every time, which is exactly the
output that gets deleted.

### Go and find out what the thing actually is

A brief is a summary written by someone who already knows the answer, which is
why it leaves out the concrete mechanics — the ones a stranger needs and the ones
hooks are made of. Before drafting, research the product itself: the client's own
site, the previous edition, local press, their social. Ask specifically:

- **What physically happens?** What does a buyer do with it, in what order?
- **What do they end up with?** A thing that works, a meal, a feeling?
- **What is the surprising detail?** The number, the constraint, the mechanic
  that makes someone say "wait, really?"

The surprising detail is usually not in the brief, and it is worth more than
every line written without it. `references/categories/` has a worked example
per category.

**When the brief takes away the brand's best move, say so.** A brand whose
voice is "name the specific thing: the person, the village, the month" cannot
write in that voice if every specific is still unconfirmed. Do not write around
the gap with blander lines. Tell the human which specifics would unlock the
voice, one short question each ("Which month are the hazelnuts roasted?",
"Whose recipe is it?"). Facts the client can confirm in a minute are the
cheapest material there is.

Record what you find back into the brief so the next run starts from it. And when
research turns up a strong fact the brief's constraints forbid, do not use it —
raise it. A ban usually exists because the fact was unconfirmed for this edition,
and confirming it is a question for the client, not a decision for you.

## Who is reading, and what they already know

A paid ad to a cold audience is read by people who have never heard of the
brand. Decide what they already know before choosing what the hook does
(Schwartz's levels of awareness, reduced to what matters here):

| The reader… | The hook leads with | The brand's story goes |
|---|---|---|
| has never heard of the brand (almost every first campaign) | the product, experienced: the taste, the moment, the thing it does | in the primary text, as proof |
| knows the brand, has not bought | the one reason to try it now | in the hook, if it is the reason |
| has bought | what is new, or the occasion to buy again | anywhere |

The mistake this table prevents: leading a cold ad with the brand's origin story
(the founder, the farm, the year it started). To a stranger, a brand talking
about itself is a brand talking about itself. Provenance, farmers, founders and
certifications are proof. They make a claim believable once the reader wants
the thing. They rarely make the reader want it.

Which awareness level the concept is written for goes in `rationale`.

## The bar: three tests every hook must pass

1. **Can you see it?** A reader should picture something: an object, a hand, a
   place, a time of day. "Natural goodness" draws nothing.
   Concrete nouns and verbs, not adjectives.
2. **Is it checkable?** "Roasted on Tuesday, shipped on Wednesday" is a claim a
   reader could check, which is why it is believed. "The best coffee" cannot be
   checked, so nobody believes it. This test *rewards* a specific claim. It is
   not a reason to cut one: a strong claim you have not confirmed yet goes to
   the human as a question ("is the first ingredient of the usual chocolate
   spread sugar?"), and lives if they say yes. Cutting it instead is how the
   only hook with a real opponent was lost in one batch.
3. **Could only this brand sign it?** The substitution test, below.

Then the paraphrase test and the out-loud test. Tests 1 and 2 are Harry Dry's
(Marketing Examples); they catch the pretty, empty line that the substitution
test lets through.

### The substitution test

Swap the brand for its nearest competitor. If the hook still works, it is dead —
you have written the category, not the product.

| Hook | Swap | Verdict |
|---|---|---|
| "Fresh coffee, delivered to your door." | Any coffee subscription | **Dead.** True of the category, not this brand. |
| "Now in our second year." | Any second-year anything | **Dead.** A fact, not a hook. |
| A line making an argument no competitor is making | Nobody else could run it | **Alive,** if it is tied to the brand's own positioning. |

Worked examples in real copy: `references/categories/`.

The test is unforgiving on purpose. Most first drafts fail it, including drafts
that feel fine. Run it on every hook before it reaches a human.

## The paraphrase test: does it actually say anything?

A hook can pass the substitution test and have a clear antagonist and still be
empty. Say it as a plain sentence to a friend, without the line break and without
the rhythm. If you cannot finish the paraphrase, it is a rhetorical shape rather
than a hook.

| Hook | Paraphrase | Verdict |
|---|---|---|
| "It's free. The rest isn't." | "It's free, but the rest of… what?" | **Fake.** Nothing survives the paraphrase. |
| "Nothing ever happens here. Until now." | "There is finally something happening here." | **Real,** if it is true and the brand would say it. |

### A caption is not a hook

Cover the picture and read the headline alone. If it names a time, a place, a
number, a weather or the product, and claims nothing about any of them ("Sunday,
7 AM.", "Twelve hours.", "Out in the rain."), it is a caption:
it labels the photograph instead of saying something the photograph cannot.
Captions came out of batch after batch looking finished, because the picture
under them was good and lent them a meaning they did not have. The paraphrase
gives them away: "it is seven on a Sunday" is not a reason to do anything.
Real ones, with what they were missing: `references/anti-examples.md`.

A number or a moment can carry a hook, joined to its "so what": not "twelve
hours" but what twelve hours does that ten minutes cannot, in words the
reader would use.

Watch the two-beat reversal especially — "X. Not Y.", "X. The rest isn't." It is
the easiest shape to generate and the easiest to fill with nothing, because the
rhythm supplies a feeling of insight that the words do not. If a batch contains
two of them, at least one is probably hollow.

### Symmetry reads as cringe, even when it is true

A matched pair — same verb shape, same rhythm, both halves the same length —
survives the paraphrase test and still lands badly ("Made by hand. Loved by
heart."). It can say something real and still be rejected on sight, because
symmetry sounds *composed*, and composed sounds like a slogan on a wall: the
register of an institution, which is the voice most brands are trying not to
have.

The good references are not clever. Wise says "Spend on holiday without unfair
fees" — a flat benefit, with the layout doing the arguing. Blunt beats balanced.

A quick check: would a person say this out loud to a friend, or does it only
work written down and centred? If it needs the line break to land, it is a
slogan. Aim for something said, not something inscribed.

Then check which way the implication runs. "It's free. The rest isn't." tells
the reader there is a hidden cost. If there is none, that is a fabricated claim
like any other, and it points directly at the objection you most need to
remove.

## Voice is transferred, never invented

**The brand's own words are the voice spec.** Not "evidence of what the audience
responds to" in the abstract — the actual register, the actual slang level, the
actual amount of cheek. `get_generation_context` returns them in `voice`, and in
order of how far to trust them:

1. **`edits`** — a human's changes to lines you wrote on earlier concepts. The
   strongest evidence there is: your own habits, corrected by the person who
   knows the brand. Each edit is a decision: if it breaks a rule here or in
   the brief, the edit wins (see "Who decides"). Before drafting, write down
   what the edits change, as rules in your notes ("turned a fragment into a
   question", "finished a half-sentence", "cut a word nobody says"), and apply
   every rule to every line you write. A batch that repeats a habit a person
   already corrected has ignored them.
2. **`setup.answers`** — the voice setup: twelve lines of standard ad copy, each
   breaking one habit of voice (`trait`), and what a human did to each. It is
   the checklist for the voice pass below.
3. **`samplesByAudience`** — what the brand wrote to real readers, grouped by
   who they were. Match the group your concept's `audienceSegment` points at.
   Never quote an email in an ad: it shows how the brand talks, not what it may
   claim.
4. **Organic hooks** — quote them verbatim into your working notes before
   drafting.

### The voice pass

Your first draft of every line is standard copy — the same copy the setup's
standard lines are. Before a batch is stored, rework every hook, headline,
primary text and on-image text against `setup.answers`, trait by trait:

- **REWRITTEN** — make the change they made, everywhere it applies. If they
  turned the formal "you" into the familiar one, every line uses the familiar
  one. If they cut the emoji, there are none. If they split the long sentence,
  yours are short.
- **KEPT** — the standard form was already right for that trait. Leave it —
  except that the standing bans below and the brief's constraints still win. A
  kept "unlock your potential" does not unban it.
- **REFUSED** — nothing like that line appears, for any reader. The reason, if
  there is one, says what to avoid.

Then check each line against `edits`. The point of the setup is that a human
never has to rewrite your copy again, so do this yourself and never ask them to.

### The read-aloud pass

Last, every hook, headline, on-image line and primary text is read out loud in
the language it is written in, as a person in that market would say it to a
friend. A line nobody would say is rewritten the way they would say it; a line
that needs a second reading to make sense is rewritten until it does not. Clever
and cryptic is a fail: "the fat is one" means nothing to anyone.

Writing in a language other than English, the danger is a translated line: an
English template with local words (see "the sentence shapes" below). **Writing
in Bulgarian, read `references/languages/bg.md` before drafting** (the playbook
topic `ad-copy/references/languages/bg`) and use its checklist in this pass.
store_specs refuses the mechanical tells of a translated line (fragments in a
row, a verb standing alone, "is one") before anything is stored; the rest is
yours to hear.

**If `voiceWarning` is set, the setup is unfinished** and the pass has gaps.
Tell the human before drafting: it takes about five minutes on the canvas.

Read for:

- **Register** — formal or peer? A brand writing in familiar slang and one
  writing institutional prose are different brands.
- **Cheek** — is the brand willing to be funny, rude, provocative? Most are
  braver in organic than anyone lets them be in paid, because paid feels
  official. That gap is where generic copy comes from.
- **Words they actually use.** Slang in an organic post tells you the register
  the brand lives in. Borrowing the register is the point — borrowing the exact
  word often is not. See below.
- **The audience's word, not the institution's.** Where a language has a formal
  term and a spoken one for the same thing, the spoken one is almost always
  right. The formal word is not neutral — it is the register of the
  institution and the form you fill in, which is exactly the voice a peer brand
  is trying not to have. Ask the client which word they would use out loud, and
  record the answer in the brand kit.

### Not everything in organic transfers to paid

Match the register, not necessarily the vocabulary. A joke works once in a feed,
where it is a post among posts and the reader moves on. The same line under paid
frequency is seen repeatedly by the same people, next to a Sign Up button, and
what read as funny reads as a slogan the brand has decided to have.

The client is the authority on which of their own jokes survive that. Ask before
building a batch on one piece of brand slang, and record the answer in the brand
kit's tone notes so the next run does not re-suggest it. Often a word is fine in
organic and off-limits in paid, and the register it signals is what to carry
across instead.

If a single hook is the only thing carrying the brand's voice, the batch is
fragile anyway. Voice should be in how all five are written, not in one word.

If the organic posts have no hook recorded, transcribe it from the image before
you draft. An empty `hook` column is the single most common reason generated copy
reverts to category-average.

## Every hook needs something to push against

This is the mechanism the good references share, and the one weak copy is always
missing. A hook without an antagonist is a statement, and statements do not stop
a scroll.

Look at what each reference pushes against:

| Reference | Pushes against |
|---|---|
| Wise — "Spend on holiday without unfair fees" | Your bank, shown losing |
| Lovable — "It used to cost $10K+ … now you can do it yourself" | A price, struck through |
| Uber Eats — "POV: a hell of a week and it's only Tuesday" | A feeling the viewer already had |

Something to push against:

- **A status the reader doesn't have yet** — who they become.
- **A named enemy** — a price, an institution, an incumbent, a waiting list, a
  category default.
- **A feeling they already had**, named precisely enough to feel spied on.
- **A belief they hold that is wrong**, contradicted flatly.
- **A specific number or fact** — only with something real behind it.

Which comes first depends on the category: status leads for young people
buying an experience, and barely registers for someone buying food. Before
drafting, read the brand's file in `references/categories/` (food,
events). If there is none, work out the order for the category and say so in
your report, so a file for it can be added.

If you cannot say what a hook pushes against, it is not a hook yet.

### A fact is not a hook until you ask "so what?"

Research produces facts, and facts feel like hooks because they are specific.
Ask "so what?" of each one until the answer reaches the reader's own life, and
write from there:

> The beans are roasted on Tuesday and shipped on Wednesday.
> So what? They arrive a week after roasting, not three months.
> So what? The coffee in your cupboard went stale before you opened it.
> The hook lives at the last line, not the first.

Three levels is usually enough. A fact that never reaches the reader belongs in
the primary text as proof, or nowhere.

### The reader is never the antagonist

This rule is the one most likely to go wrong, because the reader's deficit is
always the nearest available tension and it is easy to reach for. Resist it.

Deficit framing is: you have no experience, you missed it last time, you eat
badly, you do not know what this is, someone is disappointed in you. Every line
of it can be true, all of it tests as "relatable", and it makes the reader the
loser of an ad they did not ask to be in. Nobody buys to be told what they are
not.

Write from the reader's side instead. Same tension, opposite direction:

| Deficit | The reader's side |
|---|---|
| "Never cooked a proper dinner?" | "Dinner in four minutes. Nobody needs to know." |
| "You missed it last year." | "This year you're in." |

The second column has the same antagonist as the first. It just does not seat
the reader on the losing side.

**So find who the brand punches at, and punch there.** It is usually written
down already in the tone notes: an institution, a category default, the people
who make you wait. Aim there and the reader is your ally. Aim at the reader and
they are someone else's customer.

Aspiration is allowed to be audacious. A big promise the brand can keep beats
the careful, modest, deficit-framed lines that feel safer to write.

## Take the structure and the move, never the arrangement or the sentences

A reference gives four things, and only two of them travel:

| From a reference | Example | Take it? |
|---|---|---|
| **The structure**: the device the eye follows, which makes the argument | the pack in the middle with facts pointing at it; three items on one scale where the last one breaks it | Yes. Structure transfers across categories and languages |
| **The move**: why it persuades | "it tastes good, and the facts pointing at the pack prove it" | Yes, written as one plain sentence with none of its words |
| **The arrangement**: what sits around the structure | a white box holding the headline across the top, a navy field, stars, small captions in a row, the handle bottom-left | No. That is how that ad dressed its idea. This ad's idea decides where its headline goes and what surrounds it |
| **The sentence shapes**: the rhythm of its lines | a short claim, a full stop, a twist | No. That is the reference's language and market |

The arrangement is the part that is easiest to describe, so it is the part a
borrowed concept copies. A headline strip lifted from a reference becomes the
white header band every AI ad has; the structure it sat on is lost under it.
Write the visual idea from this ad's own idea, and let a borrowed reference
reach it only as its structure.

The failure this prevents is subtle: no word is copied, but the rhythm is.
American direct-to-consumer copy ("The only problem is…", "X. Nothing else.",
"Fair trade.", "That's the whole label.") translated word for word into
another language reads as translated, and a native reader hears it at once
even when they cannot say why. Check every line: would someone who writes ads
natively in this language write it, or is it an English template with local
words in it?

Sentence shapes come from the brand's own writing (organic captions, blog,
voice samples, the human's edits) or from how people in the market actually
talk; for Bulgarian, `references/languages/bg.md` lists the native shapes and
the translated ones. A brand whose organic asks questions and runs guessing games has told
you its sentence shapes.

See `references/formats.md` for the library of layouts, what each requires,
and when it fails. In `rationale`, name the structure you borrow, and say in a
sentence how this ad arranges it in its own way.

### Write the plain sentence first

Before a hook, write what the ad says as one plain sentence you would say to a
friend: "it was roasted this week, and you can smell it when you open the bag".
Then make the hook. Show the human the plain sentence next to every hook: they
can judge the idea separately from the wording, and fix the wording themselves
when the idea is right.

## Ideas before lines

The rules in this skill filter. None of them generates anything, and a batch
written straight from the rules is whatever offends least: the safest survivor
of a long kill list. One batch went three rounds on the only twist in a
product's description, rewording it each time, because nothing made it look
for a second idea.

So before writing a single hook, write down **at least three ideas per
product**, each one sentence, each from a different place:

| Where the idea comes from | Ask |
|---|---|
| **The product's own truth** | What does it do, contain or cost that the category's usual version does not? |
| **The moment** | When, where and with whom is it actually used? What was the reader doing a minute before? |
| **The category default** | What does the reader use now instead, and what is wrong with it that they already half know? |
| **The brand's own behaviour** | What does the brand do in its organic that no rival would: the joke, the confession, the question? |
| **The culture** | What local habit, dish, phrase or argument does this product walk into? |

**Moments are not fabrications.** A situation the product is plainly used in
(breakfast, a guest arriving, the last spoon in the jar) is a scene, not a
claim, and needs no confirmation. What needs confirming is a fact: a number, an
ingredient, an origin, a result, a customer's words. Customer words (reviews,
comments) are welcome evidence when the board has them; the method does not
depend on them.

Pick the strongest idea per product, the one with a real opponent, before
polishing any wording. If all three ideas are weak, say so: the product has too
little on the board to write from, and the fix is a question to the human about
the product, not more lines.

## Write freely first, then edit

Writing and judging are two jobs, and doing them at once is why batches come
out timid: with every rule in view while drafting, the only lines that get
written are the ones that break none, which are the ones nobody remembers. A
good copywriter writes thirty lines, most of them bad, and then edits.

**Pass 1, the writer.** Per product, write **at least 30 lines** from the
chosen ideas, the facts, the scene and the brand's own writing, and nothing
else. Do not apply a single test from this skill while writing. Bad lines are
the price of good ones. At least ten of the thirty in forms the brand has
never run in an ad:

- a two-line dialogue (who says what, at the moment it happens)
- a phone notification or a text message from someone
- a deadpan list, or instructions written very seriously
- one word, or one name
- a question that is not a poll
- a children's-book sentence, a weather report, a recipe card, a label
- a confession, a complaint that is really praise, a rumour
- the product speaking, or someone speaking about it behind its back
- something nearly too long, or nearly too short

**Pass 2, the editor.** Now open the rules: hard limits, near-duplicates, the
warnings below. Keep the strongest, mark the rest, and make the experiments
from the strangest lines that survive, not from the safest.

Show the human a sample of pass 1 as well, five or so of the wildest lines,
even the ones you would not run: a human often sees the ad in a line the
editor would have dropped.

**Pass 3, promote the strongest line.** Write each surviving concept out
whole: the hook, the kicker, the first sentence of the body text, the Meta
headline. Then read the four against each other and ask which one you would
stop for. In batch after batch it was not the hook: the body opened on the
sharp observation (a moment every reader has had, a comparison with a food
everyone knows) while the headline above it was a caption. When
another line is stronger, it becomes the hook, and the old hook goes or takes
that line's place if it does that place's job. Then rewrite the rest of the
ad around the new hook: the image's words and the body text are no longer the
same ad.

The strongest line is the one a reader stops for, which is rarely the
product's spec. Promoting the specs made a batch of fact hooks: the brew time
led three hooks of seven, and was in six.

### The brief wins, and each idea has its own moment

**Every concept answers its own brief.** Before drafting, write the brief's one
claim in a sentence ("brewed slowly, in Sofia"). Every concept on the brief
carries it, through its own idea. An idea that answers another brief (a
concentrate ad on a brief about where the latte is made) is not written here,
however good: a batch drifted that way once the rules pushed it off facts, and
the brief about origin got an office joke and another brief's product.

**One idea each, and the moment it shows.** `moment` is the situation the ad
shows (at work, a shared fridge, the commute, home in the morning, outdoors,
an occasion, where it is made, or the product alone): record the one it
really shows, because the results compare them. Two ideas worded differently
are one idea when they show one situation with one joke or one argument: the
same office-fridge theft carried a concept in every batch for a day. An
editor who did not write the batch reads it against the brief and the brand's
live concepts before it is stored, and sends back an idea that repeats one or
misses the brief. Rewrite the idea, not its label: a relabelled repeat is
sent back again.

**The brand's story is material.** Facts and lines the brief gives as the
brand's story (how it started, where it is made, how long it takes) may be
used in more than one ad, and a brief about one of them may lead its hooks
with it.

### Hooks lead with the reader, not the spec

**Unless the brief is about the fact.** A brief whose claim is a fact (where it
is made, how long it takes, what is in it) may lead its hooks with that fact,
because then the fact is the reason to buy. Everywhere else:

A product fact (a duration, a weight, a count, a volume) is proof. It makes a
hook believable once the reader wants the thing; it rarely makes them want it.
So in a batch:

- **At most one hook leads with a product fact,** and only one hook on a brief
  leads with any one fact: `store_specs` refuses a second, whatever the
  wording ("steeped 18 hours", "18-hour cold brew" and "18 hours of steeping"
  are one fact). The others lead with a moment, a feeling, a
  person, a tension or a claim about the reader, and the fact goes where it
  makes that hook true: the kicker, a line, the body.
- **A fact is in a few of the ads, not all of them.** A brief's batch where one
  fact is in most of the concepts is the product's description reworded.
- **A comparison's other side is a fact too.** "Not 18 seconds" says
  something about cafés that nobody checked. A comparison names a number for
  the other side only when it is true and known; otherwise it compares
  without one.
- **Never another concept's ad.** The same ad built on the same facts, on any
  brief, is refused at `store_specs`. A line another concept already says is
  pointed out, not refused, since the brand's own story may recur; anything
  else, write fresh. Earlier concepts are evidence of what was tried.

## Spread the survivors across families

Across both passes, spread the lines over at least five of these families:

| Family | What it does | The move |
|---|---|---|
| The moment | names when it gets eaten or used | a time and place the reader recognises as theirs |
| The senses | a sound, texture or temperature you can picture | one physical detail, named exactly |
| Confession | the brand admits something human | owning up to a habit the buyers share |
| Challenge | the reader does something now | a check they can make in their own home, today |
| Comparison | a visible winner, never a named rival | one ingredient or fact against the category default |
| Named feeling | a feeling precise enough to feel spied on | Uber Eats' "only Tuesday" |
| Split the room | a question people take sides on | a choice the brand's own organic already asked |
| Fact, so-whatted | a real fact carried to the reader's life | see "so what?" above |
| Status / potential | who the reader becomes | the reader as the kind of person they admire |

These are moves, not lines. Never reuse the wording of an example in this skill
or its references: an example copied into a batch is a hook nobody wrote for
this product, and it was. The first batch after this table was added reused
three of its example lines almost word for word.

Then cut the hard limits (false facts, invented customers, rejected
mechanisms) and the near-duplicates: two hooks on one mechanism is one test,
keep the stronger. Everything else is **marked, not cut**. Note against each
hook the warnings it trips:

1. one of the three tests (see it, checkable, only us);
2. no antagonist;
3. a claim competitors already own;
4. reads like the brand's website rather than its organic feed;
5. only works written down and centred (the out-loud test);
6. a translated template (the sentence-shapes check above).

A core concept should trip none. A marked hook is still a candidate for an
experiment, if breaking that default is the point.

**Then rank the survivors by nerve, not by safety.** Ask of each: would we be
slightly nervous to run this? Would anyone screenshot it, or say it out loud to
someone else? The hook that broke no rule and makes no one feel anything is
the one to drop first. Always show the human the bravest survivor next to the
safest, and say which is which.

**Show the kill.** Report the cut and marked hooks to the human in one line
each, with the limit or warning against it. It proves the volume happened, and a human
sometimes rescues a line for a reason you could not know.

**Ask what would unlock the rest.** List the hooks that died only for want of
a fact, each with the one question that would bring it back ("Confirm the usual
spread lists sugar first and this one lives"). A question costs the human ten
seconds; a lost hook costs the batch its best line.

`references/anti-examples.md` has real rejected copy from this pipeline with the
specific reason each one failed. Read it before drafting — the failures are more
instructive than the successes, and they were produced by a model reasoning
exactly the way you are about to.

## Spread across angles, deliberately

Five variations on one angle is one test. The batch exists to find out which
angle wins, so the angles must actually differ — and the `angle` you record must
be the one the copy really uses, because that column is what the rollup groups
by later. Mislabelling it corrupts the only feedback the loop has.

## Output contract

Every concept is a `CreativeSpec` — see `src/lib/creative/spec.ts`. Notes on the
fields that are routinely got wrong:

- **`hook`** — the line rendered INTO the image. Short enough to read at a glance
  on a phone: **2 to 6 words**, set huge. This is the ad. The strongest are a
  turn on what the reader expects ("Eggs, but louder.", "~~Ketchup.~~ Chili
  crisp.", "This one's for the pan."), said the way this language says it,
  never a translated rhythm. What it needs explaining goes in `primaryText`.

**Four places for words, four jobs.** An ad is read in the order the feed
shows it, and each place is there to do what the others cannot. Batches kept
saying one thing four times: the hook, a kicker of the product's name and
specs, body text of the name, the specs and the price, and a Meta headline
repeating the hook. `lintCopy` flags a Meta headline that repeats the hook and
a phrase said in three places on one ad; `store_specs` warns when a brief's
concepts share one phrase. Neither is a reason to reword the phrase: give the
place its own job.

| Place | Its job | Never |
|---|---|---|
| `hook` (the image's headline) | stops the scroll with a claim | a caption of the picture |
| KICKER | answers what the hook set up (the reason, the moment, the offer), so the two read as one thought | the product's name, its weight or size, or a list of specs: the pack in the picture already says them |
| CAPTION (optional, about one ad in three) | two to four handwritten words beside the product, an arrow drawn to it: names one thing you can see that makes the hook true ("still dry inside", "до последната лъжица") | the product's name, or the hook again |
| `primaryText` | opens on the reader's moment or the claim, gives the one fact that makes the hook true, ends on why now | the hook again, or a fact the image already said |
| `headline` (Meta's, under the picture) | the offer, what they get, or the next step | the hook again |

A fact lives in one place on an ad: the one where it makes the hook true,
usually the kicker or the body, rarely the hook itself. The rest of a brief's
ads stand on other things entirely: the moment, the reader, another fact. The product's description pasted into every ad (one store's
five-word product line in thirteen concepts of thirteen) is read by someone
who scrolls past three of them as one ad shown three times.

- **`primaryText`** — Meta truncates around 125 characters. Write for the
  truncation: the first line is all most people read.
- **`headline`** — about 40 characters, set bold beside the button. It may
  rightly be the same across a campaign's ads when the offer is.
- **`lead`** — which of the brief's leads this concept sells on (OFFER, FEELING,
  PROOF, PRODUCT, PROBLEM, NEW). One the brief names; spread a batch across all
  of them. It decides the words beside the headline (`leadPlan` in the
  context): a feeling needs one line or none, proof a real review or
  number, the product its facts, an offer its deal. Price is an offer's
  alone. **Never a line of the product's name and weight** ("Бадемово масло,
  250 г"): Meta does not ask for it, the pack in the picture already says it,
  and it is the line a reader skips. A FOOTER is only real fine print: a
  date, an address, an offer's terms.
- **`texts`** — every word that will appear on the image, each with its role.
  Exactly one HEADLINE, and it is the hook. **On a designed frame the headline
  is usually not the only one.** A cold reader sees the image before the
  primary text, often instead of it, so the image itself says what the thing
  is and why it is better: the pack in the picture says what it is, and a
  KICKER answers the hook with why (the table above), a few short facts (COLUMN_LINE or KICKER, a few words each), a BADGE with a
  real offer or rating. A price
  only when it is the argument (an offer, a comparison, "less than you
  think"): a bare price is a catalogue line, not a reason. How many words go
  beside the headline is the idea's call: a few for most designed frames,
  none outside the object for a phone screen, a note, a person's words or one
  huge number, whose words live inside the thing. A chat idea (NATIVE_SCREEN) writes the
  conversation itself: three to five short messages, typed the way people
  text in that language (for Bulgarian, the language reference's "Messages on
  a screen"). The hook is one of them, the HEADLINE, and the others are
  UI_CONTENT. The contact's first name is a text too. The product's name and
  weight stay out of the bubbles. With a phone in the picture, the hook may instead be
  the ad's headline beside the phone, in display type, and the conversation on
  the screen acts out the moment in UI_CONTENT lines; never the same words in
  both. Dates, an address and the
  website belong in `primaryText` unless the idea needs them on the image. Every one of them passes the same bar as the hook:
  concrete, checkable, from the evidence. A fact the brief cannot back is not
  written to fill the space.
- **`visualIdea`** — the art direction, as a designer's brief: what the eye hits
  first, what is in the picture and where, the background and light, how big the
  type sits, which product shot is placed and which parts are generated. Words by
  role, never quoted: no model ever draws a word. Composed from this ad's idea:
  a reference's headline strip, field colour or decorations are never carried in.
  It names the photograph: what it shows, how it is lit, where it sits in
  the frame. Nearly every ad carries one. A brand note against stock
  photography rules out stock, not a photo, and a flat brand look decides
  how the photo is treated, never whether there is one: a real photograph
  the brand has, or a scene generated in its photo style. An idea of shapes
  and type alone is written only when a person asked for it.
- **`rationale`** — which reference this draws on, which structure it borrows and
  how this ad arranges it in its own way, what
  it pushes against, and which awareness level it is written for. A human reads
  this to decide whether to spend money, so "engaging and relatable" is worse
  than useless.

**Propose whole ads, never bare hooks.** Show each concept with its hook, the
first 125 characters of `primaryText`, the `headline` and the visual idea. A hook read on its
own is judged as a slogan. In the feed it is read with the line above it and
the picture under it, and weak copy often turns out to be a strong hook with
nothing behind it.

## Standing bans

No "unlock", "elevate", "game-changer", "revolutionize", "незабравимо",
"отключи", "издигни". No em-dash-joined abstractions. No invented statistics,
prices, dates, durations, prizes, participant counts or partner names — if you
want a number and do not have one, write the hook so it does not need one.

**No invented customers.** No review, star rating, testimonial or quote styled
as coming from a real customer unless one exists and the client has supplied
it. The EU bans fake consumer reviews, and a joke review with a name and stars
reads as a real one at a glance. A joke in the brand's own voice ("the only
problem with these crackers…") is fine; one signed by a made-up customer is not.

**Direct-response habits don't transfer.** Most copywriting playbooks online
come from weight-loss and info-product ads. Leave these out: "power words"
("secret", "shocking", "miracle"), invented precise numbers ("47,312 people"),
curiosity bait that hides the product, "experts say", fake urgency. Borrow
their discipline instead: volume, the "so what?" chain, and writing for
whoever is reading. Their exact-number advice is the one to watch. A made-up
number is a fabricated claim, however specific it sounds.
