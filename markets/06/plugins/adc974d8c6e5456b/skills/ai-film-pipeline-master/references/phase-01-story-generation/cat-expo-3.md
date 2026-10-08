# Exposition and World Delivery — Part 3

Category `expo`, continued. Parts 1 and 2 are in `cat-expo.md` and `cat-expo-2.md` — read them first; their 61 cards cover how a story hands over facts, rules and world without stopping to explain, from the iceberg and the need-to-know ladder through diegetic delivery, serial re-entry and the eight ways exposition fails. Nothing here repeats them.

**Part 3 of 4.** 12 cards across 5 sections: instruction as a designed sequence; explaining why a thing works; instruction written for children and learners; declaring what the piece is doing, and writing for the return visit; and one named failure.

These cards close gaps the database reported about itself: each was reached for by a kit or by the intents router and could not be cited because no card existed. Parts 1 and 2 hold everything the database knows about exposition *inside a story*. Almost nothing in them covers exposition as its own written form — the procedure, the worked example, the warning, the author's note — which is the commonest paid writing there is and which the Instruction intent had to route through explainer cards that do not fit it.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Instruction as a designed sequence](#instruction-as-a-designed-sequence)
- [Explaining why a thing works](#explaining-why-a-thing-works)
- [Instruction written for children and learners](#instruction-written-for-children-and-learners)
- [Declaring what the piece is doing, and writing for the return visit](#declaring-what-the-piece-is-doing-and-writing-for-the-return-visit)
- [A named failure](#a-named-failure)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## Instruction as a designed sequence

### The Numbered Step List

**Also called:** the procedure, step-by-step, the task topic, the ordered list, the recipe method
**What it is:** Instruction written as a numbered sequence in which each item is exactly one action the reader performs, in the order they perform it, and everything that is not an action has been moved out of the numbers.
**Effect on the audience:** The reader can stop and restart without losing their place, and can hold the whole task in their hands while looking at only one line of it. A step list is the only prose form that survives being read one line at a time by someone whose eyes are mostly on something else.
**Used for and where it works best:** Anything the reader will do with their hands while reading — assembly, cooking, software setup, a safety drill, a craft tutorial, a game tutorial's on-screen text. Three craft rules carry it. **One action per step**, because the reader's finger marks the step and there is only one finger; two actions in a step means the second one gets performed later, or not at all. **Location before action** — say where they are before you say what to press, since a reader who cannot find the thing stops reading at the verb. And **end the steps that need it with a state check**, one clause naming what the reader should now be looking at, because a step list has no other way to tell someone they have gone wrong. Keep the run to seven steps or fewer and break longer tasks into named stages; beyond seven the reader stops counting and starts skimming, which is the condition the form exists to prevent. Everything else — why, what it costs, what else it could do — goes beside the steps, not inside them: `expo.procedural_exposition` is the narrative cousin of this card and puts explanation in action order, which is the right move in a scene and the wrong one in a procedure.
**Best in:** formats: Explainer, UX Writing, Corporate, Educational, Product Video, Game Narrative | genres: Educational, Science, Workplace, Medical, Lifestyle
**Avoid when:** The order genuinely does not matter, or the reader will make choices between items. Numbers promise sequence and dependency; putting a menu in them tells the reader to do all of it in that order. Use a bulleted set of options instead, and say plainly that it is a set. Also avoid numbering a process the reader will never perform — a numbered list is a contract that the reader is about to act, and using it to summarise is the fastest way to teach an audience that your numbers mean nothing.
**Example:**
> Two actions and no state check:
> 1. Open Settings, scroll to Network, and set the gateway to manual, then enter the address from the sticker on the router and save.
>
> One action per step, location first, state check where it earns its place:
> 1. On the handset, open **Settings**.
> 2. Scroll to **Network**.
> 3. Set **Gateway** to **Manual**. The address field turns from grey to white.
> 4. Type the address printed on the underside of the router.
> 5. Tap **Save**. The Wi-Fi symbol disappears for about five seconds and comes back with a dot under it. If it comes back without the dot, the address is wrong — go back to step 4.

**Yields to:** `expo.procedural_exposition` — Reader will never perform the process.  
`expo.numbered_step_list`

---

### The Prerequisite Block

**Also called:** before you start, what you'll need, the requirements section, mise en place
**What it is:** Everything the reader must already have, be, or have done before step one, gathered into a single named block above the steps rather than discovered inside them.
**Effect on the audience:** A reader who cannot do the task finds that out in ten seconds instead of in twenty minutes, and a reader who can do it starts with both hands free. It is also the clearest trust signal a piece of instruction has: a writer who tells you what you need before you begin is a writer who has done this.
**Used for and where it works best:** Every procedure longer than three steps, and every recipe, tutorial, setup guide, workshop handout and onboarding document. The craft rule is a sorting rule, and it is what makes the block worth writing rather than just worth having: prerequisites come in three kinds that must be listed separately, because they fail at different times. **Things** the reader can go and fetch. **Permissions and states** they may not be able to get at all — admin rights, an account of a particular tier, someone else's approval. **Prior tasks** that are themselves procedures. Put the permissions first, because that is the one that ends the reader's afternoon, and name the person or the place they get it from. Second rule: nothing enters the block that the steps do not use. A prerequisite block padded with the plausible teaches readers to skip it, and a skipped prerequisite block is worse than none, because you wrote it and now believe the reader has read it.
**Best in:** formats: Explainer, UX Writing, Corporate, Educational, Immersive, Live Event | genres: Educational, Science, Workplace, Medical, Lifestyle, Advocacy
**Avoid when:** There genuinely are no prerequisites. An empty or nearly-empty block ("You will need: this page") is worse than nothing; it reads as a template being filled in, and it is the first thing that makes a reader suspect the rest was too. Also avoid in a piece whose whole appeal is that you can start right now — a sixty-second tutorial that opens on a requirements list has spent its hook on admin.
**Example:**
> Buried, which is the commonest instruction failure there is:
> 4. Upload the certificate. *(Note: you'll need admin access on the domain. If you don't have it, ask your IT team — this usually takes a couple of days.)*
>
> Surfaced, and sorted so the expensive one is first:
> **Before you start**
> **You need permission for:** admin access on the domain. If you don't have it, request it now — it takes two working days, and nothing below this line will work without it.
> **You need to have done:** registered the domain (separate guide, 10 minutes).
> **You need to hand:** the certificate file, and the passphrase you set when you generated it.

**Yields to:** `expo.unread_instruction` — in a piece whose whole appeal is that you can start right now. A sixty-second tutorial opening on a requirements list has spent its hook on admin; let them start, then catch them where they get stuck.  
`expo.prerequisite_block`

---

### The Warning Notice

**Also called:** the caution, the safety message, the signal-word panel, the hazard statement
**What it is:** A short fixed-shape message that interrupts instruction to name a hazard — its severity, what it will do, and the one action that avoids it — written for a reader who is not reading carefully, because by definition nobody reads a warning at leisure.
**Effect on the audience:** Attention bought for exactly as long as the message lasts, and then returned. Done properly it also does something the rest of the document cannot: it tells the reader that this writer distinguishes between the steps that matter and the steps that merely matter, which makes every unmarked step more believable.
**Used for and where it works best:** Product manuals, safety films, PSAs, workshop and set documentation, kitchen and workshop instruction, and any interface that can lose someone's work. Four craft rules, and they are the whole card. **Severity is a word, not a tone** — a fixed ladder where the top word means death or serious injury, the next means serious injury, the next minor injury, and a separate word entirely means damage to the thing rather than to the person. Use them at their real values and never for emphasis; a writer who uses the top word on a data-loss risk has spent the only word they had. **Hazard, consequence, avoidance, in that order** — what the danger is, what it does to you, what to do instead. Readers under load act on the last clause, so the last clause must be the instruction. **Embed it at the step it applies to**, not in a safety section at the front that the reader met eleven minutes and forty steps ago. **Write it shorter than everything around it.** A warning that runs to a paragraph has been written by someone protecting an organisation rather than a reader, and reads as such.
**Best in:** formats: Explainer, UX Writing, Corporate, PSA, Educational, Live Event | genres: Educational, Workplace, Medical, Survival, Advocacy, Science
**Shelf life:** dated — review 2028-09. The four-word severity ladder and the hazard/consequence/avoidance order come from the ANSI Z535 family, which is revised periodically and differs from the ISO and EU conventions a piece may be delivered under. The craft rule is durable; the exact words and their order of precedence are a standard, and standards move.
**Avoid when:** The risk is ordinary. A document with a warning on every fourth step has no warnings — the reader's eye learns the shape and stops stopping. Budget them: if you have more than one per page, at least one of them is really a note. Also avoid the freestanding "safety first" preamble as a substitute for embedded warnings; it is the single commonest way a hazard message gets published and never read.
**Example:**
> General, front-loaded, and invisible by the time it matters:
> *Safety information: This appliance contains components that may remain electrically live after disconnection. Always observe appropriate precautions when servicing.*
>
> Embedded, severity named, and the instruction last, where a reader under load will act on it:
> 6. Remove the four case screws.
>
> **WARNING**
> The capacitor holds a lethal charge for up to ten minutes after the plug is pulled.
> Touching it will stop your heart.
> Wait ten minutes by the clock before you put a hand inside the case.
>
> 7. Lift the case straight up.

`expo.warning_notice`

---

## Explaining why a thing works

### The Mechanism Statement

**Also called:** the unique mechanism, the reason-why, naming the how, the because clause
**What it is:** One plain sentence naming the physical or causal reason a claim is true — not a demonstration of it, not a proof of it, a *naming* of it — placed at the hinge of the argument so that everything before it is a promise and everything after it is a consequence.
**Effect on the audience:** It converts a claim into a reason. An audience that has heard your claim from four competitors has stopped grading claims; a mechanism gives them something new to weigh, and the act of weighing it is the act of believing it. The specific sensation is *oh, that's why* — and an audience that has felt it will forgive a great deal of ordinary writing afterwards.
**Used for and where it works best:** Direct response of every length, from a fifteen-second product video to a forty-minute sales letter, and equally in an explainer, a PSA and a piece of advocacy. Use it the moment your market has heard the claim before — which is nearly always. Three craft rules. **Name one mechanism, not a system.** "It works because the enzyme is already broken down" is a mechanism; "it works because of our proprietary four-stage process" is a brochure. **Put it in the reader's physical world**, in nouns they can see, because a mechanism the reader cannot picture is just a longer claim. **Never make the mechanism the benefit.** The mechanism earns the benefit; stating them as one sentence collapses the hinge and you are back to a claim. This is deliberately distinct from `expo.rule_by_demonstration`, and the difference is the whole point: demonstration *shows* the rule operating and lets the audience infer the reason, which is the stronger move in fiction and the wrong move here, because a demonstration takes screen time a direct-response piece does not have and leaves the reason unnamed, where it cannot be repeated to a spouse. The mechanism statement is what the audience quotes to somebody else. Pair it with `expo.coined_term_in_context` when the mechanism deserves a name it can be remembered by, and with `expo.jargon_threshold` so the naming does not cost you the room.
**Best in:** formats: Advertising, Product Video, Explainer, UGC Ad, PSA, Carousel | genres: Advocacy, Science, Educational, Lifestyle, Medical, Political
**Avoid when:** There is no mechanism, or you do not know it. An invented one is the most expensive lie in the form, because it is the sentence the audience repeats, and it is the sentence a regulator reads first. Also avoid where the audience is unaware they have the problem: a mechanism delivered to someone who has not yet agreed there is anything to fix is an answer to a question nobody asked (`info.answer_to_unasked_question`).
**Example:**
> Claim, restated louder, which is what a saturated market sounds like:
> "Our sunscreen lasts longer. Stays on in water. Dermatologist tested. Won't run into your eyes."
>
> Claim, then mechanism, then consequence:
> "Every sunscreen you've used comes off in water, and none of them are lying to you. They're oil. Water lifts oil.
> Ours is a powder. It binds to the top layer of skin and there's nothing for water to lift.
> Which is why you can swim for an hour, and the only reason you'd reapply is habit."

**Yields to:** `expo.rule_by_demonstration` — Fiction, where showing beats naming.  
`expo.mechanism_statement`

---

### The Worked Example

**Also called:** teaching by doing it once, the solved problem, the walkthrough case, show your working
**What it is:** The whole task performed once, end to end, with real values, in front of the reader — every step shown including the ones the writer finds obvious — before the reader is asked to do it themselves.
**Effect on the audience:** A novice who has watched the thing run once carries a shape they can imitate, and imitation costs them almost nothing. Being asked instead to derive the shape from a rule costs them nearly everything they have, and most of them stop. The measured effect is large and it is specific to novices: the same worked example given to someone who already knows the task actively slows them down.
**Used for and where it works best:** Any instruction whose reader is genuinely new — a tutorial, a course, a craft book, a game's first level, an internal handover document, the first chapter of a textbook. The craft rules are about honesty and about fading. **Use real values, not placeholders.** "Enter your API key" teaches nothing; a made-up key with the right shape and length teaches the reader what a right answer looks like, which is the only thing they actually need. **Do not clean up the example.** A worked example that hits no snags teaches the reader that snags mean they have failed; put one real snag in it and recover from it on the page. **Fade the guidance**: the first example is complete, the second omits the steps the reader has now seen twice, the third is a bare problem. The fading is the teaching — a chapter of complete worked examples produces a reader who can follow and cannot do. And **run the example on a case the reader would actually have**, not the simplest one; the simplest case is the one where all the hard decisions happen to be absent. This differs from `expo.competent_walkthrough`, which is a fiction technique for making a world feel real by watching an expert work; here the reader is expected to reproduce it afterwards, which changes every choice.
**Best in:** formats: Educational, Explainer, Long-Form Non-Fiction, Corporate, Game Narrative, Interactive Fiction | genres: Educational, Science, Workplace, Lifestyle, Medical
**Avoid when:** Your reader is already competent. Experts read a worked example as padding, and there is good evidence they learn *worse* from it than from being handed the problem — so a document serving both needs the example in a collapsible or a clearly-marked section they can step over, not woven through the prose. Also avoid where the task has genuine variety and one case would mislead; there, two short contrasting examples beat one long correct one.
**Example:**
> Rule only, which is how most instruction is written and why most instruction fails:
> "To price a job, multiply your day rate by the estimated days, add materials at cost plus 15%, and include a contingency."
>
> Worked, with real numbers and one real snag:
> "Say it's the Karrada shopfront. My day rate is 150. I walked it and I think it's four days — so 600.
> Materials came to 340 at the merchant, plus 15% for my time fetching them: 391.
> 600 + 391 = 991.
> Now the snag, because there's always one. The client asked for the sign in two languages. That's not more days, it's one more day of *setting out*, which is the slow part. So five days, not four: 750 + 391 = 1,141.
> Contingency is 10% on the labour only, never on materials, because materials you've already bought: 75. Quote 1,216, round it down to 1,200 and say so out loud — 'I've rounded it down' is worth more than sixteen dinars.
>
> Now do the same for the café. Day rate 150, you walked it, and the wall is brick."

**Yields to:** `expo.competent_walkthrough` — Fiction; reader will not reproduce it.  
`expo.worked_example`

---

### The Demo as a Scene

**Also called:** the product demonstration with a turn, before-and-after demo, the workflow scene
**What it is:** A product demonstration written as a scene with a want, an obstacle and a turn, rather than as an ordered tour of what the product contains — so that what the audience watches is a situation changing, and the features arrive as the means by which it changes.
**Effect on the audience:** They remember what the product *did* rather than what it has, and they remember it as something that happened to a person. A feature tour produces recognition at the moment of viewing and nothing at the moment of buying; a demo with a turn produces the one thing a buyer needs, which is a picture of themselves afterwards.
**Used for and where it works best:** Product video, software demo, app-store preview, trade-stand loop, crowdfunding video, and any B2B film whose subject is a workflow. The craft rules are dramatic rules applied to a commercial form. **Open in the messy before, and make it specific enough to be embarrassing** — the eleven browser tabs, the spreadsheet named final_FINAL_v3, the phone call at 19:40. General pain is not pain. **One workflow, not the product.** A demo that shows three things shows none; the second workflow is a second film. **Put a turn in it** — a moment where the situation reverses rather than merely improves — and put it two thirds of the way through, not at the end, so there is time to see the consequence. **The features are unnamed until they are used.** A feature named before it is needed is a feature list wearing a costume. Apply `scene.dead_scene_test` to the cut you have: if the situation at the end is the situation at the start with a better mood, there is no scene, and that is the true diagnosis of most demo footage. `scene.reversal_of_expectation` and `scene.button` are the two structural cards worth reading before writing one.
**Best in:** formats: Product Video, Advertising, Explainer, Corporate, Brand Film, UGC Ad | genres: Workplace, Lifestyle, Educational, Science, Comedy
**Avoid when:** The audience has already bought and is trying to learn the thing. A returning user who wants to know how to do step four is badly served by a narrative — give them `expo.numbered_step_list` and a timestamp. Also avoid when the product is genuinely a set of unrelated tools with no common workflow; forcing a scene onto it produces a fictional user whom real users recognise as fictional, which costs more credibility than a plain list would have.
**Example:**
> Feature tour, which is what most demo scripts are:
> "Meet Ledger. Ledger gives you real-time sync, custom approval chains, multi-currency support and a full audit trail. Everything your finance team needs, in one place."
>
> A scene, with the turn at two thirds:
> "It's the 3rd. Yusra has forty-one receipts, six of them in Turkish lira, and a director who approves things from an airport.
> *[She photographs a receipt. It lands in a list.]*
> She's done this bit before. It's the next bit that ruins her week — she has to work out what 840 lira was worth on the day, and the day was in August.
> *[She doesn't. The line already reads $26.10, and underneath it, in grey: rate on 14 Aug.]*
> She stops. She actually stops, and checks it against her phone. It's right.
> *[Sends. 19:40 becomes 16:12 on the clock behind her. She leaves.]*
> Ledger. The receipts still arrive. You just stop being the exchange rate."

**Yields to:** `expo.numbered_step_list` — where the audience has already bought and is trying to learn the thing. A returning user who wants step four is badly served by a narrative; give them the list and a timestamp.  
`expo.demo_as_scene`

---

## Instruction written for children and learners

### The Curriculum Hook

**Also called:** the standards line, the classroom angle, the teacher-facing sentence, curriculum alignment
**What it is:** One stated learning objective, named in the language the education market uses, that a children's non-fiction book or educational piece can be bought against — and the structural pressure that objective then applies upstream to the story.
**Effect on the audience:** On the child, none, which is the test. On the adult buyer — a teacher, a librarian, a curriculum lead, a parent — it converts a nice book into a purchasable one, because it answers the only question they are allowed to answer with a budget: what will this be used *for*.
**Used for and where it works best:** Children's non-fiction, educational animation, museum and heritage content made for schools, and any kids' piece with an institutional buyer. Three craft rules, and the third is the one that saves the work. **Name one objective, not four.** A book aligned to one standard is bought for that lesson; a book aligned to seven is bought for none, because no teacher has seven lessons spare. **Put the objective in the back matter and the sell sheet, never in the text.** The moment the objective appears in the story the story is a worksheet, and children can smell it from the cover. **Write the story first and find the hook second, then check it honestly** — if the hook you found requires a chapter the story does not want, the hook is wrong, not the story. The failure this card exists to prevent has a name already: `theme.explained_theme` and its sibling `theme.tacked_on_moral` are what a curriculum hook becomes when it is allowed to move forward into the text. And a child's book that teaches by repetition still needs `expo.kids_repetition_ladder` to do it; the hook is what the adult reads, the ladder is what the child experiences.
**Best in:** formats: Picture Book, Kids Story, Educational, Middle Grade, Animated Series, Explainer | genres: Educational, Kids, Science, Nature, Heritage, Historical
**Shelf life:** dated — review 2028-09. Which standards framework a buyer cites, and how explicitly a publisher expects it named, is a live market convention that differs by country and is periodically rewritten. The craft rule — one objective, kept out of the text, found after the story — is durable.
**Avoid when:** The book's buyer is a parent in a shop and its subject is pleasure. A curriculum hook on a bedtime book is a warning label. Also avoid when the objective and the subject are the same sentence — a book about the water cycle aligned to "understands the water cycle" has no hook, it has a title, and a teacher choosing between two others is given nothing.
**Example:**
> Objective eating the story, which is what happens when the hook is written first:
> "'Now, children,' said Miss Farah, 'who can tell me the three states of water?' Sami put up his hand. 'Solid, liquid and gas!' 'Very good, Sami.'"
>
> Story intact, hook living in the back matter where the buyer finds it:
> *Text:* "The puddle by the gate was there on Monday. On Tuesday it was smaller. On Wednesday there was only a dark ring, the shape of where it used to be, and Sami sat down beside it and asked it where it had gone."
> *Back matter:* "**For teachers.** This book supports work on evaporation and the water cycle for ages 5–7. The puddle on pages 4–17 changes across six days; the observation chart on page 30 can be copied for classroom use."

`expo.curriculum_hook`

---

### Back Matter as Craft

**Also called:** the author's note, the afterword, what's true in this book, further reading, the source list
**What it is:** The apparatus after the last page of the story — author's note, glossary, timeline, "what is true and what I made up", source list, further reading — written as writing, with a voice and an argument, rather than assembled as an appendix.
**Effect on the audience:** On a child, a second and quieter book, often the one they return to. On an adult reading aloud, the answer to the question the child has just asked, which is the single most valuable thing you can hand that adult. On a teacher or librarian, the reason to buy it. And on the reader who has just been moved by the story, the thing that makes the story *land as true* — a note that says plainly which parts happened is worth more to belief than any amount of authenticating detail inside the narrative.
**Used for and where it works best:** Children's non-fiction, biography and history for young readers, heritage picture books, and any book based on a real person or event. The craft rules are what separate this from `expo.optional_appendix`, which is the fiction version and is written to be optional. Back matter in non-fiction is not optional; it is uncounted in the word budget, is often longer than the text, and is frequently where the best writing in the book is. **Write it in your own voice and admit your stake** — an author's note that begins "I first heard this story from my grandmother, who got two of the dates wrong" does more for credibility than a page of citations. **Write the "what is true" page as a list of specific claims, not as a general disclaimer.** "Some details have been imagined" tells a reader nothing; "Nabil's letters are real and are quoted exactly. The dog is invented. Nobody knows what was said at the door" tells them how to hold the whole book, and is the only honest way to publish an invented scene inside a true one — see `info.true_story_frame`. **Write glossary entries as sentences a child would say**, not as dictionary definitions; a glossary is prose with a different indent. **Make the further-reading page a recommendation with a reason attached**, one clause each, because an unannotated list is a list and an annotated one is a gift.
**Best in:** formats: Picture Book, Kids Story, Middle Grade, Long-Form Non-Fiction, Educational, Memoir | genres: Educational, Kids, Heritage, Historical, Biography, Science
**Avoid when:** The book is fiction with no factual claim, where `expo.optional_appendix` is the right card and the right warning — apparatus there is a reward, not an obligation. Also avoid using back matter to carry material the text needed: a glossary explaining a word the story required is `expo.glossary_crutch` moved to a safer page, and it fails in exactly the same way.
**Example:**
> Appendix, which is how back matter is usually produced:
> **Glossary**
> *Qanat (n.):* An underground channel used for irrigation.
> **Note:** This book is based on true events. Some details have been fictionalised for narrative purposes.
>
> Written:
> **Words in this book**
> *Qanat* — a tunnel for water, dug by hand, sometimes for miles, so that the water can travel underground where the sun can't drink it. You say it *ka-NAAT*.
>
> **What's true in this book**
> Everything about the tunnel is true. The men really did dig it in nineteen years, and the shafts really are still there in the ground, one every thirty metres, like buttons.
> Hana is invented. There were no girls on the digging teams, and I have wanted there to be a girl in this story since I was eight, so I put one in.
> The argument on page 22 is true, but nobody wrote down what was said. I made up the words. I did not make up the argument.

**Yields to:** `expo.optional_appendix` — in fiction with no factual claim, where apparatus is a reward rather than an obligation.  
`expo.back_matter_craft`

---

### The Decodability Specification

**Also called:** the levelled text, controlled vocabulary, writing to the reading level, the phonics constraint
**What it is:** Writing to a published specification — a fixed word list, a phonics scope and sequence, a sentence-length ceiling, a syllable limit — where the specification determines not only how a thing may be said but which things may be said at all.
**Effect on the audience:** A child reads a whole book alone, and the experience of having finished it is the entire point. Every craft decision in the form is subordinate to that: a beautiful sentence the child cannot decode costs more than a dull one they can, because the dull one ends with a reader and the beautiful one ends with a child being corrected.
**Used for and where it works best:** Early readers, decodable phonics texts, levelled school readers, subtitle and caption work to a reading-age target, and plain-language public information written to a stated grade level. **The specification is a subject filter before it is a style filter** — if the permitted sound set has not reached long vowels, the subject itself may be unavailable. Check vocabulary against subject first, spend the off-list allowance on necessary nouns, and make every returning phrase change meaning or action. This patterned repetition is a reading specification, not the redundant narrative-rule delivery diagnosed by `expo.over_taught_rule`. `voice.kids_register` covers how the voice should sound; this card covers what the specification forbids.
**Best in:** formats: Kids Story, Picture Book, Preschool, Educational, UX Writing, Voiceover Script | genres: Educational, Kids, Preschool, Advocacy
**Shelf life:** dated — review 2028-09. There is no single agreed threshold for what counts as decodable, and levelling schemes, phonics sequences and the publishers who own them differ by market and are revised. Get the actual specification for the actual imprint before writing a line; a card cannot hold the numbers.
**Avoid when:** The book will be read *to* a child rather than by one. A picture book for a lap has no decodability constraint at all and every word in the language available to it, and writing one to a word list is the commonest way a first picture book comes out lifeless. Also avoid applying a reading-level target to dialogue in a story for older children, where register is characterisation and levelling it flattens the cast into one voice.
**Example:**
> Same fact, unconstrained:
> "The enormous creature surfaced beside the boat, exhaled a plume of vapour, and vanished beneath the swell."
>
> Same fact, to a short-vowel set, with the one off-list word spent on the thing the book is about:
> "It came up. It was big.
> It was next to the boat. It was BIG.
> It let out a puff. The puff went up and up.
> Then it went down. The **whale** went down, and the sea shut."
>
> The last four words are the entire craft difference. Nothing in them is off-list.

**Yields to:** `expo.kids_repetition_ladder` — where the book will be read *to* a child rather than by one. A picture book for a lap has no decodability constraint and every word in the language available to it.  
`expo.decodability_spec`

---

## Declaring what the piece is doing, and writing for the return visit

### The Disclosed Staging Note

**Also called:** the reconstruction label, the per-shot declaration, the captive-shot caption, "dramatisation"
**What it is:** A line — spoken, supered, or written into the narration — that declares a particular shot or sequence to be re-staged, composited, filmed in captivity or otherwise arranged, delivered inside the film's own grammar at the moment it applies, rather than as a line in the end credits.
**Effect on the audience:** Trust bought, at a price you choose, at a moment you choose. An audience told plainly that this is a reconstruction watches it as a reconstruction and is not betrayed later; an audience that finds out afterwards re-reads the whole film as a lie, including the parts that were true. The second outcome is the more common one and it is not recoverable.
**Used for and where it works best:** True crime, historical and heritage documentary, nature film, reportage, and any factual piece that re-stages, composites or simulates. The craft rules are writing rules, not legal ones — the legal minimum is an end credit, and an end credit is the failing version. **Declare it in the same channel as the deception.** If the audience is being misled by pictures, the label must be visible; if by voice, audible. A caption under a narrated sequence does not undo what the narration said. **Declare it at the shot, not at the film.** A card at the top saying "some scenes have been reconstructed" spreads doubt evenly across everything, including your real footage, which is the worst possible distribution. **Write the label in the film's voice.** "Reconstruction" in Helvetica is the legal answer; "Nobody filmed this. This is how the file says it happened." is the answer that also works as a line. **Anchor the re-staging to evidence out loud** — naming the source the reconstruction is built from converts the label from an apology into a claim, and it is the one move that makes a re-staged sequence stronger than an unlabelled one. `expo.doc_narration_contract` sets what narration is permitted to know across the whole film; this card is the per-shot exception to it, and the two must agree.
**Best in:** formats: Documentary, Documentary Series, True Crime, Heritage Documentary, Reportage, Essay Film | genres: Journalism, Historical, Heritage, Crime, Testimony, Nature
**Shelf life:** dated — review 2027-09. The obligation to label reconstruction, and what counts as sufficient labelling, sits in broadcaster and regulator codes that are revised — the UK position and the US one already differ — and the labelling of AI-generated and AI-altered factual imagery is being written into law and platform policy right now. The craft rule survives all of it; the compliance floor does not.
**Avoid when:** The staging is obvious and the declaration would be an insult — a silhouetted actor, a hand pouring tea, a map animating. Labelling those trains the audience to think you would otherwise have cheated. Also avoid where the sequence is openly and consistently a formal device rather than a claim about a moment; an essay film in its own register does not need to announce that it is not news.
**Example:**
> End credit, which is the legal answer and the one an audience never sees:
> *Certain scenes have been dramatised for the purposes of this programme.*
>
> In the film's voice, at the shot, anchored to the evidence:
> *[Wide. A stairwell. A man's back going up.]*
> NARRATOR: "This is not him. Nobody filmed that night, and the only person who was on those stairs is dead.
> What we have is the statement he gave nine days later — forty minutes, typed, and he corrected it in pen in two places. Both corrections are about the stairs.
> So: this is his second version. The one he went back and changed."

`expo.disclosed_staging_note`

---

### Writing for the Return Visit

**Also called:** re-onboarding, the lapsed-learner problem, welcome back, resuming cold
**What it is:** Instruction written for someone who did part of this months ago, has forgotten the state they left it in but not the concept, and has come back needing to know where they are rather than what the thing is.
**Effect on the audience:** They resume in under a minute instead of restarting, which is the actual alternative — a returning reader who cannot locate themselves does not re-read the earlier material, they abandon the task, and their report of it is that the product is hard.
**Used for and where it works best:** Multi-session courses, long setup guides, apps with a long first task, annual or seasonal procedures, project handovers, and any documentation for a task performed once a year — tax, renewals, migrations, the thing you do each time you start a shoot. The craft rule is a sorting rule and it is counter-intuitive: **concepts survive a gap, state does not.** Somebody who set up a server six months ago still knows what a certificate is and has entirely lost which of the four they generated is the live one, whether they finished step nine, and what they called the thing. So the re-entry section restates the *state*, never the concept. Second rule: **give them a way to check where they are from the outside**, one observable fact per stage — "if the badge in the corner is amber, you stopped at step six" — because a returning reader cannot be trusted to remember and can always be trusted to look. Third: **put the re-entry section at the top and let the first-time reader skip it**, marked so plainly that skipping costs nothing; the returning reader is arriving from a search result and will not scroll to find it. This is the instruction case. The narrative case is already covered and covered better: `info.between_episode_memory` holds the decay model — emotional states survive, names decay, plot mechanics collapse, and binge audiences invert the middle two — `expo.season_two_reteach` holds the delivery, and `expo.re_entry_exposition` holds the weekly form.
**Best in:** formats: Explainer, UX Writing, Corporate, Educational, Interactive Fiction, Game Narrative | genres: Educational, Workplace, Science, Lifestyle
**Avoid when:** The task is short enough to redo. A re-entry section on a four-step procedure is longer than the procedure; tell them to start again and they will. Also avoid where the state has genuinely expired — if what they set up six months ago no longer works, say that in the first line rather than helping them resume into a wall.
**Example:**
> Useless, because it restates the concept a returning reader never lost:
> **Welcome back!** Remember, a certificate proves your domain is yours. You'll need one for each subdomain. Ready to continue?
>
> Useful, because it restates the state and gives an outside check:
> **Coming back to this?**
> Look at the domain row in your dashboard.
> **Grey dot** — you generated a certificate and never uploaded it. It's in your downloads folder, called **domain.pem**. Go to step 7.
> **Amber dot** — you uploaded it and it hasn't been verified. Nothing for you to do until it goes green; this takes up to 48 hours, and it has been longer than that for you, so go to step 9 and re-request.
> **Green dot** — you finished. The only reason to be here is renewal, which is step 12.
> *First time here? Start at the top; none of the above applies to you.*

**Yields to:** `info.between_episode_memory` — The returning audience is a story audience.  
`expo.lapsed_learner_re_entry`

---

## A named failure

### The Instruction Nobody Reads

**Also called:** the unread manual, the skipped tutorial, documentation written for the writer
**This is a named failure, not a recommendation.**
**What it is:** Instruction structured so that the reader must consume it before they can begin — a preamble, a concepts chapter, a compulsory tutorial, a terms-and-scope section — written on the assumption that a person facing a task will first sit down and learn. They will not. They begin immediately, fail, and then look for the one sentence that unblocks them; and by then your document has spent its credibility and they are searching a forum.
**Effect on the audience:** Not confusion — contempt. The reader concludes that the thing is badly made, because the evidence available to them is that it did not work and there was a lot of writing. They do not conclude that they should have read the writing. This is the best-attested finding in the whole of instruction research and it is forty years old: users do not read manuals, they act, and they will pay a large cost in failure rather than a small cost in reading up front.
**Used for and where it works best:** It does not — but it is worth knowing where it hurts most, because the cost is not evenly spread. It bites hardest where the reader is under time pressure and where failure is silent: enterprise software documentation, safety procedure, an app's first run, a handover document written by someone leaving on Friday, and the assembly instruction that opens on a parts inventory nobody counts. Note the distinction from the technique it resembles: `expo.prerequisite_block` also asks to be read before step one, and is not this failure, because it is short, it is sorted by what will cost the reader their afternoon, and it contains nothing the steps do not use.
**Best in:** formats: — | genres: —
**Avoid when:** Not applicable. The repairs, in order of power: **let them start, then catch them** — put the first action in the first screen or the first line and hang the explanation off the point where they get stuck; **write for entry at any point**, since every heading is somebody's first sentence, which means no section may depend on having read the one above it; **move every prerequisite into a named block** (`expo.prerequisite_block`) so that the one thing which really must be read first is the only thing claiming to be; **embed warnings at the step** (`expo.warning_notice`) rather than in a front section; and **cut the concepts chapter to the two sentences the task actually needs**, which is nearly always what it turns out to be. The last one is the hard one, because the concepts chapter is the part the writer enjoyed writing, and `expo.deletion_test` is the tool for it.
**Example:**
> The version that gets skipped — and all of it gets skipped, including the sentence that mattered:
> **Chapter 1: Understanding Sync**
> "Before using Sync, it is important to understand the underlying model. Sync operates on a two-phase reconciliation basis, in which local state is compared against a remote manifest… *(1,400 words)* …Note that sync will not run while a file is open in another application."
>
> The version that survives contact:
> **Start syncing**
> 1. Press **Sync**.
> That's it — the first run takes a few minutes.
> **If nothing happens:** you have a file open somewhere else. Sync won't touch a file another app is holding. Close it and press **Sync** again.
> *Why it works this way, and what to do about shared drives →*

**Yields to:** `expo.prerequisite_block` — Put what must be read first in one sorted block.  
`expo.unread_instruction`

---

## Coverage

**What the research showed that the brief did not anticipate.**

**The intents router listed two instruction gaps that are one card.** `intents.md` records "the warning or caution notice" and "instruction read under stress, which is the case that matters most" as separate missing cards. They are one: a warning notice is *defined* by the reading condition, and every craft rule it has — the fixed severity word, consequence before instruction, embedding at the step, brevity — exists because nobody reads a hazard message at leisure. Written apart they would have produced a rules card and a conditions card that each needed the other to be usable. They are `expo.warning_notice`.

**The mechanism statement and rule by demonstration are opposites, not neighbours.** the commissioned-advert material (`symptoms-commissioned-and-applied-work.md` here, and `../phase-03-shooting-script/ads-trailers.md`) records the mechanism statement as "distinct from `expo.rule_by_demonstration`, which shows rather than states", which is right but understates it. The reason direct response states rather than shows is not brevity — it is that the audience has to be able to *repeat the reason to somebody else*, and a demonstration leaves the reason unnamed. That is why the card insists the mechanism be one causal sentence in visible nouns, and why an invented mechanism is the most expensive lie in the form.

**Not written, because it lives elsewhere.** The fiction expert-at-work scene is `expo.competent_walkthrough`, and the worked-example card defers to it. Explanation in action order inside a scene is `expo.procedural_exposition`. Fiction's optional apparatus is `expo.optional_appendix`, which back matter explicitly does *not* extend, because non-fiction back matter is not optional. The objective leaking into the text is `theme.explained_theme` and `theme.tacked_on_moral`. The levelled reader's licensed over-teaching is `expo.over_taught_rule`, already ranked in that kit as an exception. Kids' register is `voice.kids_register`.

**Still missing after this file**, found while writing it and named in prose above with no id because no card exists: **the call to action as a written line**, which `intents.md` records as a Purchase Intent gap and which `expo.demo_as_scene` has to stop short of; **the cutdown ladder**, building a six, a fifteen and a thirty from one idea, recorded as a gap by three promotional kits; **writing to a locked picture**, narration written second, to the frame, at a fixed word rate, which `formats-doc.md` records and which the disclosed staging note brushes against without covering; **lip-sync and mouth-flap adaptation**, the central craft of dubbing children's animation; and **the parent-facing purchase layer**, distinct from `sub.dual_audience`, which the curriculum hook covers only for institutional buyers and not for the adult standing in a shop.

Named failures in this file: `expo.unread_instruction`.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Verified 2026-09-17.

- [Writing step-by-step instructions — Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/procedures-instructions/writing-step-by-step-instructions)
- [Procedures and instructions checklist — Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/checklists/procedures-and-instructions-checklist)
- [Procedures — Google developer documentation style guide](https://developers.google.com/style/procedures)
- [Federal Plain Language Guidelines, March 2011 Revision 1](https://wid.org/wp-content/uploads/2022/03/FederalPLGuidelines.pdf)
- [An introduction to plain language — Digital.gov](https://digital.gov/resources/an-introduction-to-plain-language)
- [Paradox of the Active User — Nielsen Norman Group](https://www.nngroup.com/articles/paradox-of-the-active-user/)
- [Carroll and Rosson, "Paradox of the Active User" — full text](https://research.cs.vt.edu/ns/cs5724papers/4.mental.mental.carroll.paradox.pdf)
- [A Guide to ANSI Z535.6: safety information in product manuals — Clarion Safety Systems](https://www.clarionsafety.com/safety-resources/machinery/understanding-ansi-z535-6-a-guide-to-safety-information-in-product-manuals-and-materials/)
- [ANSI Z535.6 — Manuals in Focus, In Compliance Magazine](https://incompliancemag.com/ansi-z535-6-manuals-in-focus/)
- [ANSI Z535.4-2023: Product Safety Signs and Labels — The ANSI Blog](https://blog.ansi.org/ansi/ansi-z535-4-2023-product-safety-sign-or-label/)
- [11 Lessons from Eugene Schwartz to Become a Better Copywriter — Lynn M. Swayze](https://swayze.medium.com/11-lessons-from-eugene-schwartz-to-become-a-better-copywriter-a5bf2d9164bc)
- [What Eugene Schwartz's *Breakthrough Advertising* Teaches About Modern Funnels — Rob Palmer](https://robpalmer.com/blog/eugene-schwartz-breakthrough-advertising-lessons)
- [What is Market Sophistication? — NordicCopy](https://nordiccopy.com/market-sophistication/)
- [Worked Examples: Manage Cognitive Load and Simplify Complex Concepts — Eduaide](https://www.eduaide.ai/blog/worked-examples-manage-cognitive-load-and-simplify-complex-concepts)
- [Effects of worked examples, example–problem and problem–example pairs on novices' learning — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0361476X1000055X)
- [Does working memory moderate the effect of fading on math performance? — British Journal of Educational Psychology](https://bpspsychub.onlinelibrary.wiley.com/doi/full/10.1111/bjep.12781)
- [Decodable text — Wikipedia](https://en.wikipedia.org/wiki/Decodable_text)
- [Decodable / Leveled Text Comparison — Colorado Department of Education](https://www.cde.state.co.us/coloradoliteracy/decodable_leveled_text)
- [The what, why and when of decodable and leveled texts — NWEA](https://www.nwea.org/blog/2024/the-what-why-and-when-of-decodable-and-leveled-texts/)
- [Leveled, Decodable, Readable: what does research say about the right texts for beginning readers? — Great Minds](https://greatminds.org/english/blog/geodes/leveled-decodable-readable-what-does-research-say-about-the-right-texts-for-your-beginning-readers)
- [Writers' Questions About Back Matter — Annette Whipple](https://www.annettewhipple.com/2022/01/writers-questions-about-back-matter.html)
- [A Closer Look: What's the Deal with Back Matter? — Lerner Books](https://lernerbooks.blog/2021/02/a-closer-look-whats-the-deal-with-back-matter.html)
- [Exploring the Purposes of Backmatter in Nonfiction Picturebooks for Children: A Typology — The Reading Teacher](https://ila.onlinelibrary.wiley.com/doi/abs/10.1002/trtr.2154)
- [How to Write Nonfiction Children's Books — Mary Kole Editorial](https://www.marykole.com/nonfiction-childrens-books)
- [Ofcom Broadcasting Code, Section Two: Harm and Offence](https://www.ofcom.org.uk/tv-radio-and-on-demand/broadcast-standards/section-two-harm-offence)
- [Ofcom Guidance Notes, Section 2: Harm and Offence, Issue Twelve](https://www.ofcom.org.uk/siteassets/resources/documents/tv-radio-and-on-demand/broadcast-guidance/programme-guidance/broadcast-code-guidance/section-2-guidance-notes.pdf?v=322622)
- [Article 50: Transparency Obligations for Providers and Deployers of Certain AI Systems — EU Artificial Intelligence Act](https://artificialintelligenceact.eu/article/50/)
- [How to Write a Product Demo Script — Content Beta](https://www.contentbeta.com/blog/how-to-write-product-demo-script-examples-template/)
- [SaaS Video Script Framework: A Practical Guide to Writing Better Scripts — What A Story](https://www.whatastory.agency/blog/saas-video-script-framework)
- [SaaS Product Demo Videos: Tips and Examples That Convert — Levitate Media](https://levitatemedia.com/learn/saas-product-demo-videos)
