# Structure — Forms and Doctrines

Category `struct`, continued. Part 1 is `structures.md`, which holds the eleven whole-story systems and all of their beats.

**This file is deliberately a `cat-` file rather than a second structures file.** The reachability audit excludes `structures.md`, because a system's beats are reached through their parent system card rather than through a complaint. These are ordinary craft cards and must be routed from `symptoms.md` like any other, so they live where the audit can see them.

**On the field names.** `structures.md` uses its own shape — its whole-story system cards carry a `**System:**` field and `**Effect on the work:**` rather than `**Effect on the audience:**`, because a whole-story system is chosen by a writer rather than felt by a reader. The beat entries those systems are made of carry a name and a line, and are reached through their system. The cards here use the standard card schema, which is what a `cat-` file must carry and what the build parses. Do not normalise one to the other. Nothing here repeats them.

**Part 2 of 2.** 3 cards.

These cards close gaps the database reported about itself: each was named as missing by an agent that needed it and could not cite it.

---

### Flash Fiction

**Also called:** the short-short, sudden fiction, micro fiction, microfiction, the drabble, flash prose, the hundred-word story, the one-page story, sub-thousand-word fiction
**What it is:** A complete story told in roughly a thousand words or fewer, built on a situation that is already true when the reader arrives, so that the only movement available is a change in what the reader understands rather than a change in what happens. The title is inside the machine, the implied story is larger than the told one, and the last line carries the load a whole final act carries elsewhere.
**Effect on the audience:** The reader finishes in under four minutes and then sits still, because the piece has handed them a story they assembled themselves and can only now see the shape of. A short story is experienced during; flash is experienced in the second after the last word, when the told part reorganises into the larger implied one.
**Used for and where it works best:** Literary magazines and contests, the single-screen read, a closed moment inside a longer project, and any idea whose whole value is one reversal of understanding. **The craft rule that makes it work: there is no room to establish and then change, so flash changes what the reader understands, not what happens.** Build it from four parts. *One situation already in motion* — arrive after the premise is true, never in time to watch it become true, which is Open Mid-Situation `open.open_mid_situation` applied to the whole piece rather than to a scene. *A title doing structural work* — it is free of the word count and is therefore the cheapest sentence you own; spend it on information the prose then cannot afford, or on a phrase the last line turns, per The Title That Changes Meaning `open.title_changes_meaning`. A decorative title in flash is a wasted line of text. *An implied story larger than the told one* — what you omit is the story; see The Iceberg `sub.iceberg_omission`. *A load-bearing last line* — The Last Line `end.last_line`, and hold exactly one beat after the turn, The Held Final Beat `end.held_final_beat`, never a paragraph of explanation, The Explained Ending `end.explained_ending` *(failure)*. Because the turn is usually a revelation and not a conflict, the whole-story system that fits is Kishōtenketsu `struct.kishotenketsu`, and the turn itself is still a value turn, The Value Turn `scene.value_turn`, not an event. **The word bands are real and each permits something different.** The *drabble* is exactly 100 words, no more and no less, a fandom convention formalised in 1980s British SF circles: it permits one image and one reversal, and nothing that requires a named second character. *Micro fiction*, under 300, permits one situation, one speaker and one turn — no scene change, no backstory, no second location. *Flash* at the anthology convention of roughly 750 words — "usually no more than 750 words" in the Norton flash anthologies Thomas and Shapard co-edit — permits two characters, one exchange of dialogue and a turn you can prepare for; it is the widest band most magazines actually buy. *Flash* to the full 1,000 permits a second beat in time, one flashback clause or one jump, and a genuine second presence with a want of their own. Above 1,000 you have a short story with the compression habits of flash, which is a fine thing and a different set of problems.
**Best in:** formats: Flash Fiction, Short Story, Carousel, Poetry, Serialised Fiction | genres: Literary, Slice of Life, Surreal, Horror, Fantasy
**Avoid when:** The idea needs accumulated time — a character arc built from repetition, a mystery that must plant clues and pay them fairly, or two people who both change. Those need a short story, and shrinking them produces a synopsis. Two failures kill most submissions. **The anecdote with no turn:** something happened, it was well observed, and the reader understands nothing at the end that they did not understand in line three. This is the commonest rejection in the form, and it is not fixed by better sentences; it is fixed by deciding what the reader is wrong about on arrival. **The joke whose punchline would have been a paragraph in a longer piece:** a setup engineered backwards from a last-line gag, in which the characters exist to be walked to the gag and nothing is true before it. Editors call it a twist and reject it on sight, because a twist changes the plot while a turn changes the reader. Also, do not route a prose flash piece through this database's short-form video cards — Short-Form Compression `time.shortform_compression`, A Person in Ten Seconds `char.ten_second_person`, The Arc Under Sixty Seconds `arc.sub_minute`, The Two-Second Beat `beat.shortform_beat`, Subtext in Under Sixty Seconds `sub.short_form`, Short-Form Front-Loading `expo.short_form_frontload` and Tension Under Thirty Seconds `tens.micro_form_tension` are all clock-and-scroll cards written for vertical video, and they do not apply to prose flash, whose reader chose the piece, controls the pace, and can re-read the first line.
**Example:**
> **Next of Kin**
>
> The hospital asks who to call and I write my brother's name, because I have written it on every form for thirty years and my hand does it before I do.
>
> The nurse asks for a number.
>
> I give her the one I still know, the house on Palmer Street, the phone in the hall with the cord.
>
> She dials it in front of me. It rings.
>
> A woman answers. I hear her say hello twice, then, patiently, the way you speak to the old — can I help you, love?
>
> "Sorry," the nurse says. "Wrong number."
>
> I take the pen back and cross him out, and the crossing out takes longer than the writing did.

**Source:** reference — W. W. Norton, *Flash Fiction International*, ed. James Thomas, Robert Shapard and Christopher Merrill, 2015, publisher's description, https://wwnorton.co.uk/books/9780393346077-flash-fiction-international, checked 2026-09-24; supports the flash band of roughly 750 words ("usually no more than 750 words"). Open Library record, *The Drabble Project*, ed. Rob Meades and David B. Wake, Beccon Publications, Harold Wood, Essex, 1988, https://openlibrary.org/isbn/9781870824125, checked 2026-09-24; supports the drabble's British 1980s date. The 300 and 1,000 bands are the package's working figures.  
`struct.flash_fiction`

---

### The Linked Collection

**Also called:** the short story cycle, the story sequence, the composite novel, the novel-in-stories, linked stories, the story composite
**What it is:** A book of stories each of which is complete and publishable on its own, ordered so that reading them together produces a meaning none of them contains. The working definition the criticism has never improved on: a set of stories so linked that the reader's experience of each one is modified by the experience of the others.
**Effect on the audience:** Two pleasures at once that no other prose form gives together — the short story's ending every twenty pages, and the novel's accumulation. The specific pleasure, the one the form exists for, is retroactive: story seven changes what story two meant, and the reader feels a book close behind them that they did not notice being built.
**Used for and where it works best:** There are exactly four things that can link a cycle, and each is paid for. **A place** is the cheapest link and the weakest: it is the one an agent can describe in a sentence, and it is furniture — it costs you mobility, because every story must now justify itself in one town, and the third kitchen scene is where a reader starts skipping. **A recurring cast seen from different angles** gives the most and costs the most: it buys you the mosaic where the woman who is the subject of story one is a minor irritant in story four, but it forbids you from giving that character a full arc inside any single story, so you must ration what each story is allowed to know about her, and you accept that the reader who meets only one story meets a flat person. **A time span** is the most seductive and the most dangerous: the moment a reader feels chronology, they begin reading a novel, and every year you skip becomes a hole they blame you for rather than a white space you chose. **A single question asked repeatedly** is the strongest link and the only one invisible on the contents page — which is its cost, because no marketing copy can state it, and you will be asked to lay a town or a surname over the top of it. Pick one to carry the weight and let the others be decoration; two load-bearing links is how a cycle becomes airless.

The craft rule is this: **the order is an argument, and the reader's memory of story three is a working part of story nine.** That memory is the only structural instrument the form has. You cannot cross-cut, you cannot hold a thread live across the break, you cannot plant in chapter two and pay off in chapter nine while the reader is still inside the same act — the white space between stories is a real exit and many readers take it. So the sequence must be designed the way a scene order is designed: state the claim, contradict it, complicate it, answer it. Refuse chronological order unless chronology *is* the argument; a book arranged by the years the stories happen in is a filing system, and a book arranged by the years they were written in is a confession.

The first and last stories carry jobs the middles do not. **The opening story is a contract, not a showcase.** It must be complete enough to survive being anthologised out of the book, it must teach the rule of linkage or announce that there is one, and — the part most writers get wrong — it must be *representative*, not merely best. Lead with your one atypical masterpiece and every reader who stays is reading the wrong book. Put contrast at story two so the reader learns the collection has range, and keep the strongest story around the two-thirds mark, where a book of any kind lifts or dies. **The closing story must land the book rather than end the run.** It answers the opening's question instead of repeating its subject, it resolves only what it owns — a cycle that ties off eight protagonists in its last twenty pages has become a finale, and finales are what this form is free of — and it is usually the story with the longest time jump or the greatest distance from the link, because the reader has to be let out of the place. Related: `seq.thematic_run` and `seq.length_variation` for the shape of the middle, `pov.same_event_twice` and `sub.second_reading` for the retroactive move, `rel.rotating_spotlight` and `pov.series_pov` for rotating whose story it is, `char.half_remembered_return` for the cast-angle link, `beat.distant_callback` and `end.value_landed` for the last story, `theme.thematic_motif` for the one recurring thing and `theme.competing_themes` for what happens when there are three.

**Boundary.** This is prose fiction, and the difference from a record is absolute: an album track may be a fragment, a mood or a fifty-second interlude, and a story may not — every piece here must stand entirely alone. `lyric.album_sequencing` shares the running-order logic and nothing else; `lyric.segue` and `lyric.interlude_track` are the two moves this form cannot make, because there is no crossfade in prose and a connective half-story is just a weak story. `seq.chapter_cluster` is its opposite from the other side: a cluster is invisible on the contents page and works by refusing the reader an exit, where a cycle prints every exit and dares them to leave.
**Best in:** formats: Short Story, Flash Fiction, Novel, Novella, Memoir | genres: Literary, Family Drama, Migration, Heritage, Coming of Age
**Avoid when:** The stories already exist. A cycle retrofitted in revision onto eight years of unrelated work is the commonest failure in the form, and it is invisible to the author because the links are in his head — he knows the man in story two is the brother in story six, and the page never says so. The test is mechanical: shuffle the running order at random, read the contents page, and see whether anything has been lost. If nothing has, you have a collection, which is a legitimate book and not the one your pitch is claiming. The opposite failure is worse and rarer: linkage so tight that story five cannot be read without story four. That is a novel with gaps in it. It pays the novel's setup cost, denies the reader the novel's continuity, and earns the form's most damning review — *I wish she had just written the novel*. Avoid also on a debut with no prior magazine publication: editors buy linked collections on the strength of stories that have already placed, and the link is what makes the book saleable rather than what makes it good.
**Example:**
> **The Long Water** — eight stories. The village was flooded for a reservoir in 1963. The link is one question: *what is owed to a thing that is already gone.* The place is decoration; the question is the spine.
>
> 1. **Low Water** — 1976, drought. The church tower surfaces and a boy photographs it. Teaches the rule: this book is about looking at water. Complete alone; the one I would send to a magazine.
> 2. **The Compensation Clerk** — 1963. The man who priced every house, door by door. First contradiction: he believed he was doing good, and the prose does not disagree with him.
> 3. **Swimming Lessons** — 1989. A mother who will not let her daughter near the reservoir. The question asked as fear, by someone who was never there.
> 4. **What the Diver Said** — 1994. First person, one night's work. The tower in story 1 was dynamited before the water came; the photograph is of something else.
> 5. **Two Fields** — 1963 again. The neighbour who took the money, moved forty miles, and was happy for the rest of his life. The story that refuses the book's grief, placed before the book can turn pious.
> 6. **The Planning Inquiry** — 2001. The boy from story 1, now fifty, arguing for a memorial, using the photograph he has known was a lie since 1994. Strongest story, at two-thirds, where the lift has to come.
> 7. **His Daughter Clears the House** — 2011. The clerk's daughter finds the letters he wrote to the families and never posted. Story 2 turns over.
> 8. **High Water** — 2019. The reservoir is full, nothing is visible, and a granddaughter who came to find the village gives up before lunch and drives home.
>
> **Why 8 is last.** Not because it is the best — 6 is. Because it is the only story that stops asking the question. Every other piece is someone owing the drowned village something; story 8 is the first person to decide she owes it nothing, and she is not punished for it. It answers story 1 exactly — something surfaced, now nothing does — it takes the longest time jump, it stands furthest from the water, and it lets the reader out of the county. Shuffle this book and stories 4 and 7 stop working, which is the proof that it is linked.

**Yields to:** `seq.chapter_cluster` — Linkage too tight; stories cannot stand alone.  
`struct.linked_collection`

---

### Unity of Effect

**Also called:** the single effect, the single-effect doctrine, totality, unity of impression, the preconceived effect, Poe's rule
**What it is:** Edgar Allan Poe's doctrine, set out reviewing Hawthorne's *Twice-Told Tales* in 1842 and elaborated in "The Philosophy of Composition" in 1846: the writer conceives one unique effect first, then invents only the incidents and only the tone that establish it, and deletes everything that does not. Its dropped half is the length clause — the work must be readable at one sitting, because a reader who puts it down loses the accumulation, and Poe is explicit that "simple cessation in reading" is by itself enough to destroy the totality.
**Effect on the audience:** The reader finishes carrying one thing rather than several, and carries it out of the room. A piece built this way feels shorter than it is and stays longer than it should, because every element has been rhyming with every other element for the whole reading and the reader has been accumulating without noticing.
**Used for and where it works best:** Name the effect in one word before you draft — *dread*, *complicity*, *relief*, *shame*, *wonder* — and write the word at the top of the page. Then test every element against it: does this sentence, this character, this joke, this flashback push toward the word or away from it? Anything that does neither is the thing to cut, and in a first draft it is usually the second-best idea in the piece. The craft rule that makes the doctrine usable rather than pious: **the effect is not the theme and not the mood — it is what the reader is left holding when they look up.** Mood is what the reading feels like while it is happening; theme is what the piece is about; effect is the residue, and you test it by asking a reader an hour later what state they were in, not what happened. The boundary with the argument cards matters and is easy to blur: The Controlling Idea `theme.controlling_idea` is what the work **argues** — a value plus a cause, provable against the plot, checkable scene by scene with The Thematic Audit `theme.thematic_audit`. An effect is what the work **does to the reader**, which no scene can be audited against because it lives in the reading rather than in the story. A piece can prove its controlling idea perfectly and leave the reader holding nothing. The two passes are different passes and should be run separately: the audit asks *does this scene advance the claim*, the effect pass asks *does this sentence deepen the state*. The Single Organising Idea `theme.organising_idea` is a third thing again — an upstream brand claim, written to brief agencies, not to be felt. In practice the doctrine earns its keep in anything short enough to be consumed whole and chosen for a sensation: flash fiction, the horror or ghost story, the short film, the 30-second ad, the vertical video, the song lyric, the podcast cold open, the single-scene monologue, the title sequence. Its two best companions are The Deletion Test `expo.deletion_test`, which is the doctrine's cutting half operationalised, and The Held Final Beat `end.held_final_beat`, which is where the effect actually lands in any format with the seconds to hold it — that card excludes reels, micro-drama and advertising, so there the effect has to land without the hold.
**Best in:** formats: Short Story, Short Film, Poetry, Monologue, Reels/Shorts, Advertising | genres: Horror, Cosmic Horror, Literary, Tragedy, Surreal, Mystery
**Avoid when:** Any work too long to read at one sitting — which means the doctrine's own length clause disqualifies the novel, and applying it there anyway produces thin books, a single sustained impression stretched over 90,000 words with the variety starved out of it. Three further honest limits. First, it was written by a working magazinist for a magazine market: Poe edited *Graham's*, was paid by the page, and was arguing the tale's case against the serialised novel, so the doctrine is partly a commercial position dressed as an aesthetic law. Second, it under-rates the story that changes register deliberately — the piece that begins comic and ends elegiac, or Munro's decade-spanning collages that slide between periods and are better for refusing a single impression. A change of register is not a failure of unity; it is a second instrument, and the doctrine has no way to say so. Third, the effect is not in the writer's gift. Readers arrive with different knowledge and read on different levels, and even Poe's own tales exceed their intended impression — "The Purloined Letter" is routinely read as an allegory of interpretation rather than as a detective story. Treat the named word as a discipline for cutting, not as a guarantee of reception. Finally, do not use it to justify monotony: unity of effect is not uniformity of tone, and a piece with no contrast has not achieved the doctrine, it has flattened under it.
**Example:**
> **Shirley Jackson, "The Lottery."** Effect in one word: **complicity**.
> *Kept — the boys gathering stones before anyone knows why.* It arms the ending two pages early and makes the reader an accomplice who has already read past it.
> *Kept — the shabby black box, and the villagers fussing about tradition while refusing to repair it.* Banality is the effect's delivery system; a sinister box would produce dread instead, which is a different word.
> *Kept — Tessie objecting only after she is chosen.* Complicity requires that the protest be self-interested; a principled objector would convert the effect into injustice.
> *Cut — any account of where the ritual came from.* An origin makes the village explicable, and an explicable village is somebody else's village. See `end.explained_ending`.
> *Cut — a second strand about the town's history.* It is a good idea and a whole other story, and two good ideas in 3,000 words starve each other; see `theme.competing_themes`.

**Yields to:** `theme.controlling_idea` — Work too long to read at one sitting.  
`struct.unity_of_effect`

---

## Coverage

**3 cards** in this file: `struct.flash_fiction`, `struct.linked_collection`, `struct.unity_of_effect`.

## Sources

Verified 2026-09-17.

- [Flash fiction — Wikipedia](https://en.wikipedia.org/wiki/Flash_fiction)
- [Flash fiction as a distinct literary form: some thoughts on time, space, and context — New Writing (Taylor & Francis)](https://www.tandfonline.com/doi/full/10.1080/14790726.2023.2293767)
- [Flash Fiction vs Sudden Fiction — Anoka-Ramsey Community College](http://webs.anokaramsey.edu/stankey/Literat/Fiction/FlashSud.htm)
- [Origins of the Drabble: A Brief History — Drablr](https://drablr.com/history-of-the-drabble)
- [Flash Fiction: What Not to Do — Litro Magazine](https://www.litromagazine.com/on-writing/flash-fiction-what-not-to-do/)
- [An Interview with Flash Fiction Online's Editor-in-Chief Suzanne Vincent and Publisher Anna Yeatts — Flash Fiction Online](https://www.flashfictiononline.com/article/an-interview-with-flash-fiction-onlines-editor-in-chief-suzanne-vincent-publisher-anna-yeatts/)
- [How to Write Flash Fiction Stories (with Examples) — Writers.com](https://writers.com/how-to-write-flash-fiction)
- [How to Write Flash Fiction: Tips from the Experts — The Writer](https://www.writermag.com/improve-your-writing/fiction/how-to-write-flash-fiction/)
- [Short story cycle — Wikipedia](https://en.wikipedia.org/wiki/Short_story_cycle)
- [One Story, Many Voices: Problems of Unity in the Short-Story Cycle — CORE](https://files01.core.ac.uk/download/pdf/213827438.pdf)
- [The short story cycle: broadening the perspective — Short Story Cycles](https://www.shortstorycycles.com/the-short-story-cycle-broadening-the-perspective/)
- [The Composite Novel: The Short Story Cycle in Transition — Dunn and Morris](https://books.google.com/books/about/The_Composite_Novel.html?id=msRZAAAAMAAJ)
- [How Should You Order A Short Story Collection? — Electric Literature](https://electricliterature.com/how-should-you-order-a-short-story-collection/)
- [The Set List: How to Order Short Stories in a Collection — Writer's Digest](https://www.writersdigest.com/write-better-fiction/the-set-list-how-to-order-short-stories-in-a-collection)
- [So You Want to Write a Short Story Collection — Agents and Books](https://www.agentsandbooks.com/so-you-want-to-write-a-short-story/)
- [Don't Call It a Novel (It's Been Here for Years) — The Millions](https://themillions.com/2016/10/dont-call-it-a-novel-its-been-here-for-years.html)
- [5 Tips for Crafting a Novel-in-Stories — Writer's Digest](https://www.writersdigest.com/write-better-fiction/5-tips-for-crafting-a-novel-in-stories)
- [Everything is Connected: A Reading List of Linked Stories — Literary Hub](https://lithub.com/everything-is-connected-a-reading-list-of-linked-stories/)
- [The Importance of the Single Effect in a Prose Tale (Poe's 1842 Hawthorne review) — COVE Editions](https://editions.covecollective.org/content/edgar-allen-poes-importance-single-effect-prose-tale-1842)
- [The Philosophy of Composition (full text) — Edgar Allan Poe Society of Baltimore](https://www.eapoe.org/works/essays/philcomp.htm)
- [The Philosophy of Composition — The Poetry Foundation](https://www.poetryfoundation.org/articles/69390/the-philosophy-of-composition)
- [The Philosophy of the Short-Story (Brander Matthews, full text) — Internet Archive](https://archive.org/stream/philosophyshort01mattgoog/philosophyshort01mattgoog_djvu.txt)
- [Brander Matthews on the short story's unity of impression — eNotes](https://www.enotes.com/topics/brander-matthews/criticism/criticism/brander-matthews-essay-date-1885)
- [Against the Single Effect (Aatif Rashid) — Kenyon Review](https://kenyonreview.org/2018/06/against-the-single-effect/)
- [Poe's Critical Theories — CliffsNotes](https://www.cliffsnotes.com/literature/p/poes-short-stories/critical-essays/poes-critical-theories)
- [Graham's Magazine — Wikipedia](https://en.wikipedia.org/wiki/Graham%27s_Magazine)
- [Alice Munro's Magic (Hermione Lee) — The New York Review of Books](https://www.nybooks.com/articles/2015/02/05/alice-munros-magic/)
