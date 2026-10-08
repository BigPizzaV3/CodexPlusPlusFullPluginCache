# Commissioned and applied-work complaints

Part of the symptom router. Open this file when the complaint is about commissioned and applied-work. Each complaint below is followed by the cards that repair it, best first; `LOOKUP.md` says which file holds each card.

---

These arrive as job problems rather than as draft problems. The piece may be working and the constraint still makes it unwritable — a clearance, a duration, a legal line, a reader who will never read. Nothing here is a lower grade of craft; several of these are the hardest writing in the database, and the reason they have their own section is that a writer meeting them is not looking under "scene" or "structure".

### "They want it at sixty, thirty, fifteen and six"

1. A procedure, not a repair, and it happens in the writing rather than in the edit: design the piece so each length is a complete idea in its own right, before the shoot
   `rhythm.cutdown_ladder`
2. The failure it exists to prevent is the ladder built downward from a beautiful sixty. Every rung then reads as a summary of something better the viewer was not shown, which is exactly the feeling a trailer for a trailer produces
3. Do not build one where there is genuinely one duration and one placement — a cinema spot, a festival film, anything with no paid media behind it. A ladder nobody climbs costs shoot days
4. And where the idea is inherently long, because its whole effect is accumulation, the honest six-second answer is a *different* film rather than a compression of this one
5. For the individual line inside any of those slots, the constraint is its own card
   `rhythm.duration_locked_line`

### "Every line has to be exactly as long as the slot"

1. The content of the line is decided after its length: the duration arrives from outside — a slot, a cut, a mouth, a slide, a character count — and the job is to find the sentence that both means the right thing and occupies that much time
   `rhythm.duration_locked_line`
2. The real failure mode is hitting the number by removing the pauses. That produces a script which is exactly sixty seconds on paper and unreadable at performance pace
3. Never compress the line carrying the piece's single most important fact. If the fact does not fit the slot, the slot is wrong, and the honest move is to take the time from a neighbouring line
4. And do not import the discipline into prose or stage, where the reader sets the pace — writing to a word-rate there produces monotony with a reason
   `rhythm.monotone_length`

### "The dub has to be the same length and mean the same thing"

1. It is not translation and a translator is not usually the person who does it: a translator supplies the meaning and an adapter writes the line, to a fixed duration, a fixed syllable budget and fixed moments where a mouth visibly closes
   `rhythm.lip_sync_adaptation`
2. Spend only the freedom you have. Before padding anything, check three things in order — is the mouth actually visible in this shot (usually not), can the information move to the adjacent line, can the *other* character's next line absorb a syllable. Only after all three fail is compression legitimate, and then you cut sense deliberately and write down what you cut
3. The named failure is `rhythm.lip_lock`: a line padded to reach the count, stressed on the wrong word to land a closure, or reworded until the sense has quietly gone — perfect sync, and not a sentence a person would say. The diagnostic works in any language: read it aloud with the picture off
4. Do not run the full phonetic pass on anything that is not in close-up; matching bilabials in a wide shot costs sense and buys nothing anybody can see
5. And the honest limit, which is a producer's problem before it is a writer's: at some ratios the languages do not fit, and past a certain gap the adapter is choosing what to lose rather than how to keep it
6. If the piece will be subtitled instead, the constraint is reading speed and line length, not mouths
   `rhythm.subtitle_beat`
7. And if what the cue is costing you is a reveal or a punchline rather than legibility, that is a tension problem with its own complaint
   `tens.subtitle_preempt`

### "The cut is locked and I'm writing the words to it"

1. The film is the brief and the sentences are the variable: every line has a start timecode, an end timecode and a word ceiling set by the shot underneath it
   `rhythm.locked_picture_narration`
2. The failure to guard against is narration written to fill every gap the edit left. That produces a film with no silence in it and an audience that has stopped hearing the voice by minute four
3. It is the wrong card whenever the script drives the picture — a scripted film, an explainer animated from a board, an ad built from a storyboard. There the words come first, and applying this produces narration that abdicates
4. And it is not a rescue. A film with a structural hole cannot be narrated shut, and the attempt is audible as a voice working very hard over a cut that is not going anywhere
5. Where the narration is also doing work the scenes should be doing, that is a separate complaint, and in documentary it is governed by its own contract
   `expo.doc_narration_contract`

### "It plays on a screen in a shop and nobody is there for the start"

1. Write for an audience that arrives at a random second and leaves at another one. There is no beginning, because nobody is present for it
   `rhythm.entryless_loop`
2. The failure the discipline produces if you over-apply it is exact and worth naming in advance: a piece legible from any second and worth watching from none
3. So do not apply it to an audience that is seated, captive, or has chosen to press play — a cinema pre-roll, a museum theatre with benches. And a queue counts as captive, which is one of the few public-screen situations where a three-minute build genuinely works
4. For the sibling problem — a short piece meant to be watched twice — the card is elsewhere
   `open.loop_opening`

### "They've given me the look and I can't change it"

A client hands over models, a palette, a type family, a style guide, or an existing campaign the
piece has to sit beside. It is the commonest constraint in commissioned work and the one most likely
to be argued with, because it arrives looking like a preference when it is actually a decision that
has already been paid for.

**Take the supplied identity as settled and spend the argument elsewhere.** What it governs is the
*look*; what it does not govern is the research underneath it, the structure, the order of
information or the shot. Those are still yours, and they are where the piece gets better.

**Where it genuinely collides with something the work needs — an accuracy the canon settles on a
piece the user wants realistic, a legibility floor, an accessibility minimum — choose the nearest
version that keeps the supplied look's intent and record it under `decisions`**, not absorbed
silently; `PRECEDENCE.md` settles the order. A supplied look that makes the piece less to your taste
is simply followed.

Receiving one properly is its own small job: take the clear space, the minimum size, the variants and
the colour values from the brief or the brand's own published guide *before* the first frame; where
none is found, choose the closest and note `pending_supplied_spec` so the official file can replace it. `voice.brand_voice_intake` is the same intake on the writing side.

*(Markers are defined in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set and the rule that each one closes two ways — resolved, or `unobtainable`, with what was done instead.)*

### "Legal has given me a line and it kills the opening"

1. Name what is happening first: a compelled line treated as not-writing, dropped at the end at minimum size or maximum speed in a register borrowed from whoever demanded it, on the theory that the obligation is satisfied by presence rather than by reception. That is `info.bolted_on_disclaimer`
2. The repair is four moves. Put the line *before* the claim it qualifies rather than after; deliver it in the channel the claim arrived in, spoken if spoken; write it in the piece's own grammar rather than the lawyer's; and let it cost you something small and visible, because a disclosure allowed to be slightly awkward is the one the audience believes
   `info.disclosure_as_content`
3. If the wording is fixed verbatim and cannot be touched, say the true thing in your own voice *and then* carry the fixed text. The audience has already been told, so the required furniture lands as a formality rather than as a reveal
4. The rhythm side of the same job — where the disclosure sits in the line, and what the sentence before it has to do so the required text lands as a beat instead of an interruption
   `rhythm.disclosure_as_content`
5. Two limits. Integration so smooth the disclosure stops being noticeable is not craft, it is a compliance failure with good rhythm. And a creator who opens every piece by announcing a sponsorship has converted an honesty move into a format beat, after which the audience discounts everything they say about anything

### "The end asks for something and it's embarrassing"

1. Treat the ask as a written line rather than a field to fill: its length, its verb, its position relative to the payoff, and the rhythm that lets it land
   `rhythm.call_to_action_line`
2. The commonest fault is the ask that names the medium instead of the action — *check out the link in bio*, *visit our website* — which hands the audience the writer's job of deciding what for
3. Never ask twice, and never weld one onto a film with no offer behind it. That converts fifty-six seconds of goodwill into an advertisement in the last four
4. If the ask is to a room rather than to a feed — stand, answer, choose, carry, write back — the moment has to be small, refusable, legible and consequential
   `inter.audience_asked_to_act`
5. And the room version has a hard line: nothing that gathers something you then keep. Names, addresses, confessions written on cards and collected are a data transaction dressed as a ritual, and the room can feel it. If the ask is emotional, the artefact goes home with the person who made it

### "The film has become something else and I have to go back to them"

Write it as a scene with a real value turn, because that is what it is, whether or not it ever appears on screen. A film that has had this conversation is cut differently from one that has not.

1. Say what changed before you say what you want — one sentence, in their words rather than yours: *when we filmed you this was a film about the school; it is now a film about your brother*
   `scene.reconsent_scene`
2. Offer the specific material, not the cut. Nobody can consent to a ninety-minute film they watch once; anyone can respond to the four minutes they are in, watched twice
3. Name what you cannot undo — what has screened, what is archived, what a broadcaster now owns — because a promise you cannot keep is what ends the relationship, not the film
4. Ask a question that can be answered no. "Are you still happy with this?" cannot be; "Do you want this out of the film?" can. And write the answer down in their words while you are still in the room
5. The turn is not permission, it is standing. Somebody who agrees reluctantly has told you something the film now has to carry
6. Do it on a *structural* change and not on every edit, and never once the cut is locked and the question is cosmetic. Asking a person to bless a decision you will not reverse converts them from a contributor into an accomplice, and they will know
7. Where the piece has no final version to show at all — because every user assembles it differently — the consent problem is a design problem with its own card
   `inter.consent_without_a_cut`
8. And for what may and may not be merged when the person is one of several
   `char.real_person_composite`

### "The subject has approval and I'm writing around it"

The scene you are actually in is not about the work's quality. It is a negotiation about control, conducted by two people who are both pretending to discuss craft.

1. Write both walk-aways before you go in — what happens to you if they refuse, what happens to them if they refuse — because the party with the worse alternative concedes, regardless of who is right
   `scene.approval_conversation` · `seq.negotiation_sequence`
2. Decide in advance which two notes you will take and which one you will not, and take the two early. A reviewer who has won twice is measurably harder to refuse the third time, and you get to choose which three the fight is about
3. Never screen to a group. Approval in a room becomes performance for the others present, and somebody will object in order to be seen objecting
4. Separate the note from its proposed fix. "Cut the whole section" is usually a report that one line in it is wrong
5. What this becomes when the walk-away was never written is subject capture, and it is recognisable from outside: the difficult question stops being asked somewhere in the second act, and the film becomes authorised without anyone deciding that it should. If you cannot make the piece without a veto, say in the piece that there was one — a disclosed veto is a fact the audience can weigh, and an undisclosed one is what discredits the work later
   `info.access_as_structure`
6. The card carries a review date on the paperwork rather than the craft: approval and access clauses are moving fast, and the contracts will have changed before the position does

### "I have to give them a right of reply and it deflates the piece"

It does the opposite. A reader who sees the subject was asked, and sees what they said, is reading a report; a reader who never sees the approach is reading an argument, and will discount it accordingly whether or not it is true.

1. Put the allegation, not the subject. A letter saying you are making a film about their company produces a press officer; a letter naming three invoices dated 4 March and a publication date produces an answer
   `scene.right_of_reply`
2. One specific claim per numbered paragraph, with the evidence named. A subject who cannot tell which claim to deny will deny everything generally, and a general denial is worth nothing to the reader
3. Give a real deadline and honour it. And print the refusal verbatim, because "declined to comment" throws away the difference between silence, a lawyer's letter and *no one by that name has ever worked here*
4. The reply changes the piece even when it is nothing, because the paragraph it sits in now has to be written to survive it
5. The ambush dressed as a right of reply — a camera at a car door and four seconds to hear the question — is a scene about the reporter, and audiences have stopped reading it as courage. The one real exception to approaching at all is a source endangered by it, and that has to be reasoned on the page rather than assumed
6. For the claim you cannot stand up and will not drop, and for the fact you are barred from stating
   `info.unverified_allegation` · `info.embargoed_fact`

### "It's all true as far as I know, and that isn't good enough"

A procedure rather than a repair: a separate pass over a finished draft, run against notes, recordings and documents rather than against your memory of them. It belongs at the end of a *draft* and not at the end of the schedule — checked after lock, the only fix left is a hedge, and a piece full of hedges has fact-checked itself into being unbelievable.

1. **Mark the draft.** Line by line, mark every claim that could in principle be wrong — every number, date, name, title, place, quotation, attribution, causal statement and superlative — including the ones inside quotes, because a contributor's error published unmarked is your error
   `info.fact_check_pass`
2. **Attach a source to each mark, at the claim rather than to the piece.** A bibliography is not a check, and a claim whose source is another sentence in your own draft is unsourced
3. **Check the ones you are most confident about.** Errors do not live where you felt uncertain; you already looked those up. They live in the facts you have known for years, which is where the check should start
4. **Walk a familiar claim back down through popular repetition to a real source, because a repeated claim passes a naive check.** Hold three tiers apart and never let a claim move up one. A primary source is the tablet, the inscription, the chronicle, the excavation report. A scholarly reading is what a named specialist concluded from it, and it is evidence of a reading rather than of the event. A popular repetition — a documentary, a museum caption, a coffee-table book, a line quoting the reading — is not a source at all, because circular citation means the popular version often ends up cited back to a "reliable source" that was itself repeating it. **A claim repeated in ten videos, including your own previous ten, is one unchecked claim with nine echoes.** Two-thirds of a heritage check is this step
   `expo.heritage_specificity`
5. Know the five classes that fail most: the number that drifted while being retold, the date converted between calendars by formula or silently read as absolute, the transliterated spelling that has no single right answer and must be chosen once and never drifted, the quotation whose famous wording appears in no primary text, and the correlation that became a cause at the sentence where you compressed
6. **A claim you cannot source does not get softened, it gets cut or attributed.** *Widely believed to be*, *some say*, *possibly the first* keep the assertion and remove your accountability, which is worse than either option. Either it goes, or it becomes somebody's named position — not *the fire saved the tablets* but *the excavator's explanation was that the fire saved them*
7. When the check breaks the story, the check wins, and the moves are, in order: restructure so the piece is about what is actually known; make the uncertainty itself the material; publish the claim with the state of the checking attached; or drop the sequence. Keeping it with a softer verb is not on the list
   `info.disputed_history` · `info.contradictory_sources` · `info.unverified_allegation`
8. Separate judgements from facts before you start and check only the facts. Running an interpretation through this produces a sourced-looking sentence that is really your reading wearing a citation, which is the more dangerous error because it is now armoured
9. It is not a legal read, and it catches errors rather than the absence of context — a piece can survive a perfect check and still be untrue in the way that matters
10. What you publish afterwards when this pass missed something, and the separate decision about what the audience is told about a source you have already verified
   `info.the_correction` · `info.source_on_screen`
11. Distribution enforces it whether or not you value it: broadcasters and distributors require errors-and-omissions cover, and the insurer wants the annotated script

### "The source won't be named and the piece feels weaker for it"

It is weaker, measurably, and that cost does not go away — stories carrying only unnamed sourcing are rated less credible, and specific attribution rates higher than vague attribution on the same sentence. What a description recovers is not the authority but the *grounds*: a reader told nothing tests the claim against the publisher's reputation, a reader told how this person came to know it tests the claim against the claim.

1. Describe the person by what makes them credible for this exact claim, not by their proximity to it. "A source close to the matter" is a hole in the sentence; "a woman who had worked in the building for nineteen years" is an argument. The test is mechanical — the description answers *how would they know?* and nothing else. Rank, tenure and duty answer it; adjectives never do
   `info.anonymity_decision`
2. Decide granularity claim by claim. Anonymity is not one switch: a name, a role, a date, a department, a gender are each separately costed. Audit in both directions — strip what identifies, because the jigsaw problem is real, then keep and *use* everything that survives. A writer who redacts by instinct deletes the nineteen years along with the name and has nothing left to write
3. Give the reason in the sentence and make it a reason rather than a formula. "Who was not authorised to speak" is a category; "who still works there and is a witness in the pending case" hands the reader the motive to weigh, which they will look for anyway
4. Put the claim to the subject without handing over the source. An approach specific enough to get an answer can be specific enough to identify who gave it to you, and that collision rewrites the letter rather than excusing skipping it
   `scene.right_of_reply`
5. On screen it is a different craft problem. A silhouette, a pixelated face, a re-voiced line or a synthetic stand-in is a visible admission for as long as the contributor is, and it costs the thing a documentary interview runs on — a face doing something while it speaks. So earn it: say early, in words, why this person is disguised; keep the disguise consistent so the audience stops re-solving it; and shoot what the face was doing, in hands, the room, the pause before the answer. Label a synthetic mask, or you have imported an unmarked reconstruction into your interview
   `scene.reconstruction_unmarked`
6. When the reason is danger rather than preference, the problem becomes structural. You lose the right to be interesting about the details — the specific duty and the quotable turn of phrase are exactly what identify them — so the weight moves onto corroboration: the document, the second account, the thing the claim predicts that you can check yourself. Never let the anonymous account be the load-bearing beam, and say plainly that you have done this
   `info.credibility_ladder`
7. The failure is anonymity used to make a claim unfalsifiable, and one question settles it: *if this claim were solid, would I have kept the name?* A yes means the anonymity is protecting the claim from being checked rather than protecting a person — and the second-order damage is worse than the first, because the honest use gets discounted along with the lazy one
8. Do not composite your way out. Merging two informants into one "source" is fabrication in reportage
   `char.real_person_composite`
9. Avoid it where the description you can safely publish identifies the person anyway to the only audience that matters — a village, a department of six, a congregation. You have then paid the full cost and delivered none of the protection
10. The neighbouring problems are not this one: the claim you cannot prove, the named person who will certainly read it, and consent where there is no final version to show
   `info.unverified_allegation` · `char.living_subject_reader` · `inter.consent_without_a_cut`
11. And a checked claim is not rescued by a citation — what the audience is told about a source is a separate decision from whether the thing is true
   `info.source_on_screen`

### "I'm building something interactive and I want it to still exist in ten years"

**For a documentary or a testimony archive, losing the work is a broken promise to a contributor rather than platform rot.** Somebody agreed to be recorded on the understanding that the record would exist. They were not agreeing to a browser plugin, and the fact that a vendor made the decision does not move the obligation off the person who made the promise.

1. Produce a complete, self-contained, linear version as a document *alongside* the build, never reconstructed from it afterwards: a reading order, the authored text, and a sentence for every asset
   `inter.outlive_the_platform`
2. Separate authored text from generated text. Anything assembled at runtime — from a database, a model, a user's route — is a possibility rather than a document and cannot be deposited. Keep the authored strings in one plain file that is the source of truth
3. Every photograph, clip, map and recording gets one authored sentence saying what it shows and why it is there, written for a reader who will never see it. That sentence is the asset's survivor, and it is neither alt text nor a catalogue entry
4. Every call to somebody else's map, player, chart library or model is a paragraph of your piece written by a company with no commitment to you. If a fact from it is load-bearing, write the fact down, dated, at the time
5. Name one canonical path through the node graph and write its linking sentences, so the piece has a reading order that is authored rather than averaged — and deliver a linear cut wherever there is picture and sound
   `inter.archive_way_in`
6. Put the deposit copy in the contract and the budget in year one, because the money for it never exists in year five. And tell the contributors the piece is deposited, in the same conversation where the withdrawal route is already being explained
   `inter.consent_without_a_cut`
7. The honest rule, and it is a hard test: **if the piece cannot be described in writing to someone who cannot run it, it will not survive**
8. Two real failure modes. **The linear version eats the piece** — draft the safe linear cut first and the interactive version becomes an ornamented linear documentary whose branches decorate an argument already settled; write them as twins, not as an original and a copy. And **preservation theatre**, a screen-recorded walkthrough filed as the deposit copy, which captures one route and the interface chrome and preserves almost none of the writing
   `inter.canon_ending_problem`
9. Skip it where the ephemerality is the work — a live ARG, a season-bound live-service story, a piece whose subject is its own disappearance. The honest output there is documentation of what happened, not a cut-down
10. Distinct from the brief-writing discipline next door. That one is about your *writing* surviving a spec change; this is about the *artefact* surviving its own runtime, and you can hold a perfectly dated, platform-neutral brief for a piece that no longer exists anywhere
   `inter.platform_contract` · `inter.interactive_adaptation`
11. The card carries a review date on the tooling and the funding conditions rather than on the obligation, which is permanent. Re-check what your archive will accept before writing the deliverable into a contract

### "The demo is a list of features"

1. Write it as a scene — a want, an obstacle, a turn — so what the audience watches is a situation changing and the features arrive as the means by which it changes
   `expo.demo_as_scene`
2. Then find the one plain sentence naming the causal reason the thing works, and put it at the hinge, so everything before it is a promise and everything after it is a consequence
   `expo.mechanism_statement`
3. Never invent that sentence. It is the most expensive lie in the form, because it is the sentence the audience repeats and the sentence a regulator reads first
4. Both are wrong for a returning user trying to do step four. Give them a numbered list and a timestamp
   `expo.numbered_step_list`
5. And a product that is genuinely a set of unrelated tools with no common workflow should not be forced into a scene — it produces a fictional user whom real users recognise as fictional, which costs more than a plain list would have
6. If the audience has not yet agreed they have the problem, the mechanism is an answer to a question nobody asked
   `info.answer_to_unasked_question`

### "Nobody follows the instructions"

1. They never will, and the structure assuming they would is the named failure: `expo.unread_instruction` — a preamble, a concepts chapter, a compulsory tutorial, written on the belief that a person facing a task will first sit down and learn. They begin immediately, fail, and go looking for the one sentence that unblocks them, by which point they are on a forum
2. Let them start, then catch them: the first action in the first screen or the first line, and the explanation hung off the point where they get stuck. Write for entry at any point, because every heading is somebody's first sentence
3. Move everything that genuinely must be known first into one named block above the steps, so that the one thing claiming to be read first is the only thing claiming it
   `expo.prerequisite_block`
4. Make each numbered item exactly one action the reader performs, in the order they perform it, and take everything that is not an action out of the numbers
   `expo.numbered_step_list`
5. Numbers promise sequence and dependency, so a menu inside them tells the reader to do all of it in that order — and numbering a process nobody will perform teaches an audience that your numbers mean nothing
6. If they are failing rather than skipping, perform the whole task once in front of them with real values, including the steps you find obvious
   `expo.worked_example`
7. Experts learn worse from a worked example than from the bare problem, so in a document serving both, put it somewhere they can step over rather than weaving it through the prose
8. And cut the concepts chapter to the two sentences the task needs. It is the part you enjoyed writing, which is why it is still there
   `expo.deletion_test`
9. If the reader will be frightened or hurried rather than merely impatient, the whole register changes and there is a separate card for it
   `tens.instruction_under_stress`

### "The reader is panicking and my instructions assume they aren't"

1. Write for comprehension that has collapsed — narrowed attention, no working memory, no tolerance for a subordinate clause — which is the state of every reader who actually needs the instruction
   `tens.instruction_under_stress`
2. It is the wrong format for a calm reader on a complex task. Stripping the *why* leaves them unable to adapt the instruction to a situation you did not anticipate, and the unhurried forms are separate cards
   `rhythm.instruction_step` · `expo.explainer_scaffold`

### "The warning is right there and people walk straight past it"

1. Write it to be obeyed rather than to satisfy whoever required it — severity, what it will do, and the one action that avoids it, in a fixed shape, for a reader who is not reading carefully
   `expo.warning_notice` · `tens.warning_notice`
2. Then count them, because the likelier diagnosis is `tens.warning_fatigue`: warning so often, so loudly or about so little that the reader stops reading warnings at all, including the one that matters. The repair is subtraction and grading rather than rewording — rank every warning one user meets in a session by real severity and delete or demote everything below the top tier
3. A document with a warning on every fourth step has no warnings. Budget them: more than one per page means at least one of them is really a note
4. Never use a freestanding "safety first" preamble as a substitute for warnings embedded at the step. It is the single commonest way a hazard message gets published and never read
5. Where the wording is compelled and you have no authority over it, the honest move is to add a readable instruction beside the compelled text rather than to rewrite it
6. And inside drama the rule inverts: a formally perfect warning is a signal that nobody will heed it
   `tens.threat_with_rules`

### "They did half of this months ago and have come back to it"

1. Write for someone who has forgotten the state they left it in but not the concept, and who needs to know where they *are* rather than what the thing is
   `expo.lapsed_learner_re_entry`
2. Skip it where the task is short enough to redo — a re-entry section on a four-step procedure is longer than the procedure, and they will start again anyway
3. And if the state has genuinely expired, say so in the first line rather than helping them resume into a wall
4. The serial-fiction version of the same problem is a different complaint with different cards
   `info.between_episode_memory`

### "The publisher has given me a word list"

1. Find out which specification you are actually under, because they are two systems with different rules: a **decodable** text may use only the letter-sound patterns the child has been taught plus a named high-frequency list, while a **levelled** text is graded by word frequency, word length and sentence length
   `rhythm.decodable_text`
2. The specification determines not only how a thing may be said but which things may be said at all, which is why it belongs to the outline rather than to the line edit
   `expo.decodability_spec`
3. The honest failure mode is satisfying the specification and stopping there: a wordlist arranged into sentences, which is what most decodable readers are and the reason a good one is worth so much
4. And the category error that costs the most: applying any of it to a book an adult will read *aloud*. A five-year-old's listening vocabulary is years ahead of their decoding vocabulary, and a picture book for a lap has every word in the language available to it
5. Do not level dialogue in a story for older children either. Register is characterisation, and levelling it flattens the cast into one voice

### "The book has to be sellable to a school"

1. Name one learning objective in the language the education market uses, and accept the structural pressure it then applies upstream to the story
   `expo.curriculum_hook`
2. The hook is wasted when the objective and the subject are the same sentence. A book about the water cycle aligned to "understands the water cycle" has a title rather than a hook, and gives a teacher choosing between three books nothing
3. And it is a warning label on a bedtime book bought by a parent for pleasure
4. Write the apparatus after the last page as writing — author's note, what is true and what was invented, timeline, sources — with a voice and an argument, rather than assembling an appendix
   `expo.back_matter_craft`
5. Never use back matter to carry material the text needed. A glossary explaining a word the story required is the same failure moved to a safer page
   `expo.glossary_crutch` · `expo.optional_appendix`

### "Three other writers will have this character after me"

1. A procedure rather than a repair, and it is the only thing that keeps a curve intact across a multi-season room, a live-service game or a long serial: fix the arc's non-negotiables in writing so they survive the turnover of the people writing them
   `arc.arc_under_many_hands`
2. Do not run the apparatus on a piece one writer will finish. It costs real time and produces a rigidity a single author should refuse — a novelist who locks an arc statement in chapter two has given up the discovery that makes the second half better
3. The one-writer version of the same instrument is a working test you keep out of the bible
   `arc.arc_statement`
4. The behaviour half is a separate procedure and it is the one that decides whether the character survives the turnover. Enforce behaviour, not facts — a continuity error about a birthday is cheap and an out-of-character *decision* is expensive and permanent — route every episode's biggest choice for that character through one named owner, and read the character's lines in sequence across episodes, stripped of everything else, once per season. Nothing else finds drift as fast
   `char.behavioural_continuity`
5. What that owner works from is a per-character bible page, and it has to be *operational* rather than biographical: what they want that the format cannot grant, what they will never do, the three tactics they use in order, how they say no, and the two or three continuity facts a writer can get wrong and be embarrassed by. Two pages maximum. A page of childhood generates nothing; "she answers a direct question with a question, always, including under oath" generates dialogue
   `char.bible_entry` · `voice.voice_bible`
6. Give each character a two-line note on *how they lose an argument*, because that is where drift shows up first. And take over an inherited character deliberately rather than by imitation
   `voice.inherited_character_voice`

---
