# Character Arcs — Part 2

Part 1 is in `arcs.md` — read it first. Its 41 cards hold the five arc shapes, the eight components every arc is assembled from, the mechanics of running one, the arc shapes outside the five, arcs sized to an episode or a lyric, ensemble and secondary arcs, working method, and five named failures. Nothing here repeats them.

**Part 2 of 2.** 12 cards across 5 sections: Whose Arc Is It; Arcs Found Rather Than Designed; Arcs That Do Not Complete; Arcs Under Production Pressure; Named Failure.

Part 1 assumed one thing throughout: that the arc belongs to a fictional character the audience watches, that the writer designed it, and that the piece runs long enough to finish it. This part is everything that happens when one of those four assumptions fails. The first four cards close the four gaps `arcs.md` recorded about itself and described as having no card anywhere in the database.

Durable except where a card says otherwise. **One home per technique** — where an arc-shaped idea already lives in `char`, `rel`, `anta` or `end`, it is cited here and not rewritten; the Coverage section lists every one of those decisions.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Whose Arc Is It](#whose-arc-is-it)
- [Arcs Found Rather Than Designed](#arcs-found-rather-than-designed)
- [Arcs That Do Not Complete](#arcs-that-do-not-complete)
- [Arcs Under Production Pressure](#arcs-under-production-pressure)
- [Named Failure](#named-failure)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## Whose Arc Is It

### The Narrator's Arc

**Also called:** the telling arc, the arc of the act of narration, frame-level change, the narrator who learns while speaking, discovered narration
**What it is:** The person telling the story changes across the telling, on a curve distinct from — and sometimes opposed to — the curve of the character they are narrating. The events are fixed; what moves is the teller's relationship to them, visible in the prose itself.
**Effect on the audience:** Two stories for the price of one, and the second is usually the better one. The audience begins reading the account and ends reading the accountant, and the moment they notice the switch is the moment the piece acquires a subject it never stated.
**Used for and where it works best:** First-person novels and memoir above all, and any retrospective narration — a documentary presenter following a story that implicates them, a monologue, a testimony, a podcast host whose investigation turns. The craft rules. **Change the prose, not the facts.** The arc must be legible in diction, hedging, tense and distance before it is ever stated: a narrator who begins with certainty and ends with qualification has arced, and no line of dialogue is needed. **Fix three positions and write the narration from inside each one** — where the teller stands at the start, at the point they can no longer maintain the account, and at the end. **Make the middle position untenable rather than wrong**, because a narrator who is simply lying arcs by being caught, which is a reveal, not a change. **Decide whether the narrator knows the ending**, and hold that decision absolutely: a teller who knows and withholds is a different person from one who is finding out, and drafts routinely contain both. The prose-side machinery is `voice.retrospective_narrator`, `pov.retrospective_distance` and `voice.self_correcting_narrator`; the reliability question is `info.unreliable_narrator` and `sub.narrator_self_deception`; the structural container is usually `time.frame_narrative` or `pov.nested_tellers`.
**Best in:** formats: Novel, Memoir, Monologue, Audio Drama, Documentary, Essay Film, Podcast, Limited Series | genres: Literary, Psychological, Testimony, Migration, Crime, Biography, Faith, Drama
**Avoid when:** The narrated character already carries a full arc of the same shape. Two arcs pointing the same way at two altitudes is redundancy the reader experiences as slowness, and the narrator's version always wins because it is closer. Also avoid it in tightly plotted genre work with a cool narrator: the arc requires the reader to attend to the telling, and a thriller has trained them to attend to the events.
**Example:**
> CHAPTER 1: "My father worked at the tannery for thirty-one years and never once complained about it, which I have always thought was the most impressive thing about him."
>
> CHAPTER 9: "My father worked at the tannery for thirty-one years and never complained, and I have written that sentence in three different letters, to three different people, always in the same admiring way."
>
> CHAPTER 14: "He didn't complain. I want to be careful here, because I have said this so often that I can no longer tell whether I am reporting it or defending it. He didn't complain to *me*."
>
> *(The father does not move. The tannery does not move. The narrator moves from a fact, to a noticed habit, to a redefinition of the word she built her father out of — and nobody in the book ever mentions it.)*

`arc.narrator_arc`

---

### The Arc That Belongs to the Player

**Also called:** the player's arc, the arc of the person holding the controller, complicity design, the arc outside the fiction, playing as the subject
**What it is:** The designed change belongs to the player, not to the protagonist. The character may be flat, fixed, silent or entirely absent; what has a beginning, a turn and an end is the player's own relationship to what they are doing — from willing, to uneasy, to unwilling to continue.
**Effect on the audience:** The only change an audience cannot argue with, because it happened to them. A player who has stopped enjoying an action they were enjoying two hours ago has been given a self-revelation that no cutscene can manufacture, and the discomfort is the payoff rather than a defect.
**Used for and where it works best:** Games and interactive pieces with a repeated mechanic — the shooting, the stamping, the sorting, the scrolling — where the repetition is what makes the turn possible. The craft rules, and they are strict. **Make the mechanic pleasurable first, honestly**, for long enough that the player owns the pleasure; an experience that is uncomfortable from the opening minute produces a critique the player watches rather than an arc they have. **Withhold the accusation.** The piece must never tell the player what they have become — `arc.told_revelation` is even more fatal here than in linear work, because the player can simply disagree and stop. **Let the game keep rewarding them past the turn**, because the moment the mechanic stops paying, the player reads the piece as having switched off rather than as having implicated them. **Put the turn in the interface, not the script**: a counter that starts naming what it is counting, a menu option that quietly disappears, an animation that gets one frame slower. And **give them a way to stop that the game acknowledges** — an arc that can only be completed by continuing is a corridor with a lecture at the end. This is not `inter.player_driven_arc`, where an authored character's arc branches under player behaviour; here there may be no character arc at all. The tension machinery is `tens.interactive_tension`, the emotional handling is `emo.interactive_emotion`, and the design failure this card sits closest to is `inter.ludonarrative_dissonance` — which is what happens when this arc is produced by accident.
**Best in:** formats: Game Narrative, Interactive Fiction, XR, Immersive, Visual Novel | genres: War, Psychological, Dystopia, Horror, Political, Satire, Social Drama
**Avoid when:** The piece is short, or the mechanic is not repeated. The arc is made entirely of repetition and the player's growing fluency at something; under about two hours there is no fluency to turn. Avoid it, too, where the audience is a spectator — a streamed playthrough hands the arc to the person with the controller and gives the chat a sermon.
**Example:**
> A BORDER BOOTH. THE PLAYER STAMPS PASSPORTS. DAY 4:
> > DISCREPANCY DETECTED — ISSUING CITY
> > Deny? [Y/N]
> > *(The player denies. +5. They are getting fast. They have started reading the city line before the name line, which nobody taught them.)*
>
> DAY 19:
> > DISCREPANCY DETECTED — ISSUING CITY
> > Deny? [Y/N]
> > *She is the fourth from the same town this week and she says it burned.*
> > *(The player denies. +5. The pay is the same. The sound the stamp makes is the same. Nothing in the game has commented.)*
>
> DAY 26:
> > *The player's hand is already on Y before the document has finished loading.*
> > *(That is the arc. The game never says a word about it, and the player will describe it afterwards in the first person.)*

**Yields to:** `arc.decision_arc` — Short interactive piece with no repeated mechanic.  
`arc.player_arc`

---

### The Institution as Arc-Bearer

**Also called:** the institutional arc, the company's arc, the arc of a house, organisational change as story, the firm as protagonist
**What it is:** The thing that changes is an institution — a company, a family, a regiment, a parish, a newspaper, a village — which begins holding a shared operating belief, is put under pressure it cannot meet on its own terms, and ends either transformed or dead, while the individuals inside it may not move at all.
**Effect on the audience:** Recognition of a kind fiction rarely offers: the sense of a thing larger than anyone in it, changing by increments none of them chose, with no author and no villain. It also produces grief for something that was never alive, which is a specific and useful feeling.
**Used for and where it works best:** Workplace and political drama, family sagas, war, heritage and industrial history, long-form non-fiction, and any story whose real subject is a system. The craft rules. **Give the institution one sentence it says about itself**, in its own register — a motto, a standing order, a line in the induction talk, a phrase everyone repeats in the kitchen — and change *that* sentence, once, visibly. That is the arc; everything else is evidence. **Change the institution's documents**, because an institution's interior life is its paperwork: the form gets a new box, the letter loses the signature, the rota is now printed rather than handwritten. `voice.institutional_voice`, `voice.bureaucratic_register` and `expo.diegetic_text` are how you write it. **Give it a body count of roles, not people** — the job that stops existing, the room that becomes a storeroom — so change is felt as subtraction. **Anchor it in exactly one person whose fate runs against the institution's**, so the audience has somewhere to stand; this is the same proxy rule as `arc.group_arc`, and a story without it is a thesis. And **decide the direction and commit**: an institution that ends improved is a rare and difficult story, and most drafts that attempt it end up sentimental. The related cards are all about the institution in other roles — `anta.institutional` when it opposes, `rel.institutional_bond` when a person loves it, `pov.institutional_pov` when it narrates. None of them is this one, which is the institution as the thing that moves.
**Best in:** formats: Limited Series, Novel, Feature Film, Documentary Series, Long-Form Non-Fiction, Stage Play, Heritage Documentary | genres: Workplace, Political, Social Drama, War, Faith, Historical, Heritage, Journalism
**Avoid when:** A family or a village can bear either this arc or `arc.group_arc`: if the members turn together by an act, it is a group arc; if the change arrives through pressure nobody chose, it is this one. And avoid it where one person runs the place. The moment the institution has an author, its change becomes that person's decision and the arc collapses into an ordinary character arc with a large office attached — the whole value of this shape is that nobody chose it. Also avoid it as a subplot: it is slow, it is made of small evidential beats, and at subplot scale it reads as background texture rather than as movement.
**Example:**
> THE SENTENCE, SAID IN THE INDUCTION TALK, EPISODE 1:
> > "We print what we can stand behind. If we can't stand behind it by six, it waits for tomorrow."
>
> EPISODE 4 — the same talk, to a new intake, same speaker:
> > "We print what we can stand behind. Obviously the web desk's a bit different."
>
> EPISODE 9 — a printed card, laminated, by the door. Nobody gives the talk any more:
> > WE PUBLISH FIRST. WE CORRECT FAST. WE NEVER GO QUIET.
>
> *(Three beats, two of them furniture. No character in the series argues about the wording, and the man who wrote the first version is still employed and has not changed his mind about anything.)*

**Yields to:** `arc.corruption` — One person runs the place; it is their arc.  
`arc.institutional_arc`

---

### The Arc Carried by a Role

**Also called:** the role arc, the arc of the chair, positional arc, the anthology arc, the office not the officer
**What it is:** The arc belongs to a *position* rather than to a person — the detective on this beat, the wife in this house, the king, the night nurse — and is carried across an anthology, a generational novel or a long series by successive occupants, each of whom serves one stretch of a curve none of them completes.
**Effect on the audience:** The unnerving pleasure of watching a shape survive its occupants. It makes an argument about determinism without stating one: the audience sees a new person arrive certain they will be different, and recognises the position bending them, which is more persuasive than any character's speech about the same idea.
**Used for and where it works best:** Anthology series, generational sagas, heritage work spanning centuries, procedurals that recast, and portmanteau structures where nothing but the setting carries over. The craft rules. **Define the role by a repeated action, not by a job title** — who signs the thing, who is called at 3 a.m., who tells the family. The repeated action is what the audience recognises across the cut. **Give each occupant a complete small arc and one inherited beat**, so each part is satisfying alone and the series-level curve is assembled from the inherited beats only. **Vary what the role costs, not what it demands**: the demand must be identical every time or there is no role, and the cost must differ every time or there is no story. **Let one occupant refuse**, once, late, and show the position absorbing the refusal — that is the role's own climax and the only place the large arc can land. Sits next to `arc.borrowed_arc`, which gives the weekly arc to a guest so the lead can stay fixed; here it is the reverse — the guests are the leads and the fixture is the chair. The ensemble-scale cousin is `arc.group_arc`; the format-level machinery is `theme.series_consistency` and `char.protected_static_role`.
**Best in:** formats: Series, Limited Series, Novel, Anime, Comics, Audio Drama, Documentary Series, Short Story | genres: Historical, Heritage, Crime, Political, Faith, Family Drama, Science Fiction, Migration
**Avoid when:** The audience is being asked to love somebody. Affection is built by continuity of person, and a form that replaces its lead every hour spends its whole emotional budget on re-establishment. Also avoid it where the role is genuinely neutral — a position that does not deform its occupant has no arc, only a rota.
**Example:**
> 1919 — He is twenty-six and he writes in the margin of the ledger: *Approved, but I don't like it.*
> 1954 — His nephew, forty, writes: *Approved. (Precedent: 1919, p.211.)*
> 1988 — A woman who has never met either of them writes: *Approved per standing practice.*
> 2011 — The margin is a tick-box. It is ticked.
> 2024 — The new one asks what the box is for. Nobody in the building knows, and she ticks it, and she is the first of the five who felt anything about it at all.
>
> *(Five occupants, five complete small arcs elsewhere in the book. The role's arc is these five lines: from a man who objected, to a system where objection has no field to be written in, to a woman whose objection is the only thing that survives — as a question nobody can answer.)*

**Yields to:** `arc.borrowed_arc` — The audience must love a continuing lead.  
`arc.role_arc`

---

## Arcs Found Rather Than Designed

### The Real Person's Arc

**Also called:** the documentary subject's arc, the biographical arc, the found arc, arc as finding, the evidenced change
**What it is:** In biography, documentary and reportage the subject's change is not a design decision but a claim about a real life — so the arc has to be *found* in the material, stated at the strength the evidence supports, and left incomplete where the evidence is.
**Effect on the audience:** Trust, which is the only currency non-fiction has. An audience that can feel the difference between what the film knows and what it is guessing will follow it a very long way; one that catches a fabricated turn stops believing the parts that were true.
**Used for and where it works best:** Documentary, heritage film, memoir about other people, long-form non-fiction, biopics, true crime, testimony. The craft rules. **Find the arc in the transcripts before you write it**, by locating the two or three moments where the subject's own account of themselves changes — the story they tell about the same event in 1987 and in 2019. That shift is the evidence, and it is also the scene. **Differences between sources are evidence, not an inconvenience to erase**: two relatives who remember the turning point differently is a better sequence than one who remembers it cleanly, and `info.contradictory_sources` and `info.disputed_history` are how it is built. **State the strength of your claim in the grammar.** "He changed" and "he began saying he had changed" and "the letters from that year sound different" are three different assertions, and only one of them may be true. **Leave the unresolved unresolved.** A real life will refuse a turn at least once; that refusal is usually the most interesting thing you have, and `arc.acceptance` is often the honest shape where a change arc is not available. And **decide what you owe a living subject before you start cutting** — `info.withholding_from_the_subject` and `sub.documentary_subject` cover that ground. Composite and fictionalised figures are `char.real_person_composite`; the frame that declares the piece true is `info.true_story_frame`.
**Best in:** formats: Documentary, Heritage Documentary, Long-Form Non-Fiction, Memoir, Documentary Series, Reportage, Podcast, Feature Film | genres: Biography, Testimony, Journalism, Historical, Heritage, True Crime, Migration, Advocacy
**Avoid when:** The subject is alive, close, and still inside the change. An arc requires an end position, and a person mid-recovery, mid-trial or mid-grief has not got one; imposing it publishes a verdict on someone's unfinished life. Wait, or restructure around a question rather than a curve.
**Example:**
> ON SCREEN — the same man, two interviews, twenty-two years apart, cut together with no narration between them:
>
> 1997: "I left because the work dried up. That's the whole of it. People make a big thing of it."
>
> 2019: "I left because the work dried up." *(pause)* "That's what I've always said. My sister says I left in the March and the yard didn't close until the September, and she's right, I've checked, so I don't know what to tell you."
>
> NARRATION, IMMEDIATELY AFTER, CLAIMING NO MORE THAN IT CAN:
> > We could not find out why he left in the March. We know he began to wonder about it, on camera, at seventy-four.
>
> *(The arc is real, it is evidenced, and it is small: not "he came to terms with his exile" but "he stopped believing his own sentence about it." That is what the material supports, and nothing more is asserted.)*

**Yields to:** `arc.acceptance` — No end position; the change is not available.  
`arc.real_person_arc`

---

### The Arc Assembled From Witnesses

**Also called:** the reported arc, change by testimony, the absent subject, the contested account, the arc in other people's mouths
**What it is:** A character who is never a viewpoint and is rarely alone on the page, whose change exists only as an assembly of other people's accounts of them — so the arc the audience builds is an artefact of *who testifies in what order*, and may not match anything the character actually did.
**Effect on the audience:** Active reading. The audience becomes the jury, forced to weigh sources, and the figure they end up with is one they built, which they hold more firmly than any narrated character. The best version produces a second effect at the end: the suspicion that the arc belongs to the witnesses.
**Used for and where it works best:** Novels and films built around an absent or dead centre, oral-history structures, courtroom and inquiry pieces, heritage work about a figure the record barely holds, and mockumentary. The craft rules. **Order the witnesses by interest, not by chronology** — put the person with the most to gain from a particular version early and the person with nothing to gain last, and let the late testimony bend everything before it. **Make at least two accounts incompatible on a checkable detail**, so the audience learns the accounts can be wrong before the account that matters arrives. **Give the subject no more than three direct appearances**, and make them ordinary: the power of the form collapses the moment the audience can see the person clearly and compare. **Decide whether the arc is real**, in your own notes, and never tell the reader; the piece works either way, but a writer who has not decided writes vague witnesses. The viewpoint machinery is `pov.peripheral_narrator`, `pov.nested_tellers` and `info.rumour_chain`; the reveal ordering is `info.credibility_ladder`. Distinct from `char.offstage_change`, which elides *one* transition in a character the audience otherwise watches directly — here the character is never watched at all.
**Best in:** formats: Novel, Limited Series, Documentary, Audio Drama, Stage Play, Podcast, Short Story, Comics | genres: Literary, Mystery, True Crime, Testimony, Historical, Heritage, Psychological, Journalism
**Avoid when:** The audience must feel what the character feels. This form guarantees distance — that is its mechanism — and a piece that needs interiority at the climax will have to break its own rules to get it, which reads as a cheat. Also avoid it for a subject the audience already knows well from elsewhere: testimony about a famous figure is received as commentary rather than as construction.
**Example:**
> HIS BROTHER, first: "He was never political. Whatever anyone tells you. He went because his friends went."
>
> HIS FOREMAN, second: "He asked me for the Tuesday off, and he asked properly, in writing, which he'd never done in nine years. I've still got the note."
>
> THE WOMAN FROM THE PRINT SHOP, last, twenty pages later: "He'd been in four times that month. He always paid cash and he always waited for it, which I thought was strange, because most people come back."
>
> *(Nobody describes a change. The brother's certainty, the written note and the cash are three artefacts in an order the reader assembles into a man deciding something over four weeks — and the brother, who loved him, is now the least reliable person in the book, which is the arc the novel actually has.)*

`arc.reported_arc`

---

## Arcs That Do Not Complete

### The Arc That Ends Before the Change

**Also called:** the withheld completion, the arc at the threshold, stopping at the decision, the unresolved arc, the open-arc ending
**What it is:** The piece runs the full machinery of an arc — the Lie, the pressure, the collapse of the old position — and then ends at the moment the character is standing at the change, with the change itself unwritten and the audience left holding it.
**Effect on the audience:** A particular kind of ache and a long afterlife. The audience finishes the arc in their own head, which means they finish it in their own terms, and a piece completed by the reader is rarely forgotten. It also produces a real minority who feel cheated, and that is a price, not an accident.
**Used for and where it works best:** Short film, short story, literary novels, stage plays, documentary where the subject's future is genuinely open, and any piece whose subject is the difficulty of change rather than change itself. The craft rules. **Everything except the final beat must be complete.** The withheld ending only reads as a choice if the Lie was fully built, fully attacked and fully collapsed; withhold the ending of an under-built arc and you have simply stopped. **Show the character at the cost, not before it.** They must know exactly what the change will take, out loud or in behaviour, so the audience can price the decision even without seeing it made. **End on an action, not a stare** — a hand on a door, a number dialled, a coat picked up — because a physical commitment implies a decision while a face implies a writer who did not have one. **Answer the piece's stated question and withhold only the outcome**; `end.answer_the_question_asked` is the boundary, and a piece that withholds the *question* is not doing this, it is failing. The related shapes are `end.open_ending` at ending scale and `tens.suspended_ending` at tension scale; this card is the arc-level version and the difference matters, because an open ending can sit on a completed arc and this cannot.
**Best in:** formats: Short Film, Short Story, Stage Play, Novel, Novella, Limited Series, Documentary, Monologue | genres: Literary, Social Drama, Migration, Psychological, Coming of Age, Faith, Addiction, Testimony
**Avoid when:** The audience contract promises a landing — romance, kids' work, redemption, most genre fiction, anything commissioned as uplift. Also avoid it in series television at anything other than a season end: an arc left at the threshold across an episode break is not withholding, it is a cliffhanger, and it will be judged as one.
**Example:**
> She has the phone in her hand. She has had it in her hand since the second act, and the audience knows what the call costs, because her brother priced it for her on page fifty-one: *"If you ring them, you will not be welcome in that house again, and neither will the boy."*
>
> LAST PAGE:
> > She puts the boy's coat on him, and does the top button, which he hates, and he lets her.
> > "Are we going out?"
> > "In a minute."
> > She picks up the phone.
> >
> > *END.*
>
> *(Coat on, top button done, phone in hand — three physical commitments. The audience is not guessing what she will do; they are holding the cost of it, which is the thing the play was actually about.)*

**Yields to:** `arc.proof_scene` — The audience contract promises a landing.  
`arc.unfinished_arc`

---

### The Arc Cut Short by the Character

**Also called:** the interrupted arc, death mid-change, the inherited arc, the transferred completion, the arc somebody else finishes
**What it is:** The character dies, leaves or is removed partway through their own arc, and the completion is transferred — carried out by somebody else, or left as a debt the survivors now owe.
**Effect on the audience:** Grief with a specific shape: not only that a person is gone but that a *change* is gone, which is a loss the audience can name and which gives their grief somewhere to act. It is also the only way to make a death structurally load-bearing rather than merely upsetting.
**Used for and where it works best:** War, crime, family saga, historical and heritage work, long series that must lose cast, and true stories where the subject died before their story finished. The craft rules. **Complete the first two turns before you take them.** A character removed before their Lie has been seriously challenged has not had an arc interrupted; they have had a function ended, and the audience feels the difference immediately. **Hand the remaining turn to a specific named person**, and stage the handover as an ordinary scene *before* the removal, so it is not retrospectively invented — a request, an argument, a job half-explained. **The inheritor must complete it differently**, and slightly worse, because an heir who completes it perfectly turns a tragedy into a relay. **Never let anyone in the story say what was inherited.** The word "legacy" in dialogue is the sound of this card failing. Build the removal with `char.exists_to_be_lost`, which covers how to construct a character worth losing; this card covers what happens to their unfinished curve. The whole-cast version is `arc.collision`; the negative case, where the interruption is the thesis, is `arc.fall`.
**Best in:** formats: Limited Series, Novel, Feature Film, One-Hour Drama, Series, Anime, Heritage Documentary, Comics | genres: War, Crime, Family Drama, Tragedy, Historical, Heritage, Migration, Medical
**Avoid when:** The removed character existed to motivate somebody else. Then this is a mechanism for laundering that move, and audiences read it within a scene: an arc invented in order to be interrupted is worse than no arc, because it advertises the intention. Also avoid it twice in one piece — the second transfer teaches the audience that nobody will be allowed to finish anything, and they stop investing in the third.
**Example:**
> BEFORE — episode 3, an ordinary scene, nobody signalling anything:
> > "You do the March returns. I'll do them with you once and then you do them."
> > "I don't want to do the March returns."
> > "No. Nobody wants to do the March returns."
>
> AFTER — episode 7. He has been dead eleven days:
> > She does the March returns. She gets the third column wrong and has to start again, twice, and she is still at it when the cleaners come round, and at no point does she cry or say his name or think about him in any way the camera can see.
>
> *(His arc was learning to let go of the work; it was two-thirds run when he died. She completes it, badly, in a spreadsheet, and the word "legacy" appears nowhere in the series.)*

**Yields to:** `arc.fall` — The interruption is the thesis, not an accident.  
`arc.interrupted_arc`

---

### The False Arc

**Also called:** the performed change, the arc that is a lie, counterfeit transformation, the reversion, the convincing recovery
**What it is:** A character is given every visible marker of a completed arc — the apology, the humility, the new routine, the proof scene — and has not changed at all, and the piece is built so the audience believes it first and discovers it second.
**Effect on the audience:** Two distinct hits. First the satisfaction of a change arc, delivered in full and not withheld. Then the retroactive reorganisation of everything they were relieved about, which is the same pleasure a good reveal produces and lands harder because they were emotionally invested rather than merely curious.
**Used for and where it works best:** Addiction and recovery stories, domestic abuse, crime and con narratives, family drama, corporate and political work, psychological thrillers. It is the honest shape for a very common real pattern, which is why it matters. The craft rules. **Write the change as though it were real.** Every beat must be genuinely earned on the first read — do not hedge it, do not have a wise character squint at it, do not score it with unease. Hedged, it is a telegraphed reveal; unhedged, it is devastating. **Plant exactly one thing that does not move**, small, physical and repeated: the same lie told about a trivial matter, the same person never apologised to, the same drawer. It must be present before the change, during it and after it. **Make the false change cost him something real**, because an audience prices sincerity in sacrifice, and a performance that costs nothing does not convince. **Reveal it through a decision under pressure, not a confession**, and the decision must be the same one he made in Act One — `arc.proof_scene` run in reverse. And **decide whether he knows**, because the character who is sincerely performing a change he is incapable of is a tragedy, and the one who is running a con is a thriller, and they need different scenes. Not to be confused with `char.unearned_change`, which is the writer failing to earn a change they meant sincerely, or `char.informed_attribute`, which is a change asserted and never staged. Here the staging is complete and the change is the lie — a distinction the Avoid line below depends on.
**Best in:** formats: Limited Series, Novel, Feature Film, One-Hour Drama, Stage Play, Audio Drama, Novella | genres: Psychological, Family Drama, Crime, Addiction, Thriller, Social Drama, Noir, Political
**Avoid when:** The audience has no independent way to check. This arc requires at least one character who was present for the original behaviour and is still present at the end; without that witness the reveal is an assertion, and the audience will suspect the writer changed their mind rather than that the character was lying. Also avoid it in work aimed at people living the same pattern unless you intend the piece to say that change is not available — which is a serious claim, and `theme.arc_carries_claim` is where to check whether you meant it.
**Example:**
> THE THING THAT DOES NOT MOVE — planted three times, forty pages apart, always about nothing:
> > p.31 "There's no milk." / "There's milk." / There is no milk.
> > p.94 — after the meetings, after the ninety days, after the apology to his daughter that made his sister cry — "There's no petrol in it." / "I filled it Tuesday." / He did not fill it Tuesday.
> > p.203 "I've eaten." / He has not eaten.
>
> THE REVEAL, A DECISION AND NOT A CONFESSION:
> > The hospital rings at ten past two. He takes it in the hall, exactly as he took the call in chapter one, and he says exactly what he said in chapter one, which is: "Tell her I'm on the motorway."
> > He is in the hall.
>
> *(Ninety days, a genuine apology that cost him his sister's good opinion of herself, and a small lie about milk that never once stopped.)*

`arc.false_arc`

---

## Arcs Under Production Pressure

### Reopening a Closed Arc

**Also called:** the sequel problem, the second-book arc, re-arcing, the earned regression, giving him something new to be wrong about
**What it is:** The technique for giving a character a second full arc after the first one finished — by finding the *new* problem their completed change created, rather than by taking the change away.
**Effect on the audience:** Continuity that reads as growth rather than as a reset. The audience gets the pleasure of a fresh arc and keeps the earlier one, which is the entire commercial and emotional premise of a sequel.
**Used for and where it works best:** Sequels, second and third books, renewed seasons, franchise continuations, any piece commissioned after its ending was written. The craft rules. **The new Lie is the old Truth applied where it does not fit.** This is the whole card. A man who learned to stop running now cannot leave a situation he should leave; a woman who learned to trust her instinct now trusts it about something she knows nothing about; someone who found independence now cannot be loved. Each is a complete new arc that *requires* the first one to have happened. **Never cost-free the first change.** Undoing it offstage — the marriage failed between films, he is drinking again on page two — is the single most reliable way to make an audience feel their time was wasted, and it is the note that sinks more sequels than any other. **If regression is genuinely the story, dramatise the force that caused it**, at full strength, on the page: `arc.padding_relapse` names what happens when you do not. **Change the pressure, not the person.** A sequel that reruns the original situation asks the character to relearn what they know, and the audience watches someone who has gone backwards while time has gone forwards. **Let one thing be permanently fixed**, and refer to it once, lightly — the audience needs proof the first arc was real before they will invest in a second.
**Best in:** formats: Feature Film, Novel, Series, Limited Series, Animation Feature, Comics, Game Narrative, Anime | genres: Action, Adventure, Crime, Drama, Fantasy, Superhero, Family Drama, Thriller
**Avoid when:** The first arc ended in `arc.acceptance` or in a death, real or symbolic. There is no second arc in an accepted unchangeable situation without unaccepting it, which is a betrayal of the first ending. Also avoid it where the ending you wrote was a full stop and you know it: the honest options are a different protagonist, a prequel, or `arc.role_arc`. Advertising a second arc you do not have produces `end.sequel_bait_close`.
**Example:**
> FILM ONE ENDED HERE: "I'm not going anywhere." — and he stayed, and it cost him the job, and it was right.
>
> FILM TWO, WRONG — the change undone offstage:
> > "Where's Dad?" / "He left in April."
>
> FILM TWO, RIGHT — the same Truth, now a Lie, in one exchange on page nine:
> > "The unit's being moved to Doncaster. Everyone's going."
> > "I'm not going anywhere."
> > "Nobody's asking you to leave *her*, Frank. They're asking you to get on a bus."
> > "I'm not going anywhere."
>
> *(The line that was his victory is now his prison, and the audience hears it as both in the same second. Nothing from film one has been taken away; it has been moved somewhere it does not work.)*

**Yields to:** `arc.role_arc` — First arc ended in acceptance or in death.  
`arc.sequel_reopening`

---

### The Arc Under Many Hands

**Also called:** the room's arc, the arc bible, arc continuity across staff, the handed-over character, long-run arc drift
**What it is:** Running a single character arc across a production long enough that the people writing it change — a multi-season room, a live-service game, a long-running serial — by fixing the arc's non-negotiables in writing so the curve survives the turnover of the writers.
**Effect on the audience:** They never see this card, which is the point. What they see when it is absent is a character who seems to have several different pasts, relearns the same lesson in season four, and whose big moment lands on somebody who was not set up for it.
**Used for and where it works best:** Series and serialised work above about twenty episodes, live-service games, long comics runs, soaps, and any project where the originating writer will not finish it. The craft rules. **Write the arc down as four sentences, not as a plan**: the Lie, the act the character will not do, the moment they will do it, and the price. Four sentences survive a handover; a forty-page document does not get read. **Name the arc's owner**, one person, and make every script pass through them for that character only; an arc with a committee has no `arc.moral_line`, because a line nobody owns gets crossed by whoever needs the scene. **Keep a ledger of what has been spent** — which turns have been used, which confrontations have already happened — because the commonest long-run failure is not contradiction but repetition, the same realisation played three times by three writers who each thought they were doing it first. **Bank the endings early.** Write the character's final beat in year one and keep it in the bible; if the show ends abruptly you have it, and if it runs long you can move it. **And plan the exits**: people leave productions, actors leave shows, and a character whose arc cannot survive their departure is a liability — `end.retiring_a_character` is the honest exit and `arc.interrupted_arc` is the shape when there is no time for one. Consistency at theme level is `theme.series_consistency`; voice-level continuity is `voice.series_voice_match` and `voice.inherited_character_voice`.
**Best in:** formats: Series, Soap, Serialised Fiction, Game Narrative, Comics, Animated Series, Web Series, Procedural | genres: Drama, Crime, Fantasy, Science Fiction, Medical, Workplace, Family Drama, Superhero
**Shelf life:** dated — review 2028-09. The craft — write it short, name an owner, keep a ledger — is durable; the production shapes it assumes, the multi-season writers' room and the live-service content calendar, are current industry structures and are changing.
**Avoid when:** One writer will finish the piece. The apparatus costs real time and produces a rigidity that a single author does not need and should not accept — a novelist who locks an arc statement in chapter two has given up the discovery that makes the second half better.
**Example:**
> THE FOUR SENTENCES, PINNED IN THE ROOM, YEAR ONE — unchanged through four showrunners:
>
> > **RAFI — LIE:** "If I am useful enough to them, they cannot get rid of me."
> > **WILL NOT DO:** name a colleague to the board.
> > **WILL DO IT:** S4, and not because he is threatened — because he is *asked nicely* by someone he admires.
> > **PRICE:** the colleague is fine. Rafi is not. Nobody ever finds out he did it.
>
> THE LEDGER, SAME WALL:
> > SPENT — S1E7 refused a promotion (want). S2E3 first challenge (Hana's speech in the car park). S3E9 win that rewards the Lie (the Kessler account). **DO NOT REPLAY THE CAR PARK.**
> > BANKED — final beat, written 2021, sealed: he is asked to say a few words at Hana's leaving do and cannot do it.
>
> *(Two index cards. Every writer who joins reads them in ninety seconds, and the one instruction in capitals is the one that prevents the failure this card exists for.)*

`arc.arc_under_many_hands`

---

## Named Failure

### The Imposed Arc

**Also called:** the clean arc on a real life, granting a reckoning that never happened, the tidy biopic, retrospective absolution, the invented turn
**This is a named failure, not a recommendation.**
**What it is:** A real person is given a change the record does not support — a reckoning they never had, a reconciliation that did not occur, a moral failure softened into a stage they moved through — because the material refused to produce a third act and the arc shape demanded one.
**Effect on the audience:** Short-term satisfaction and long-term damage. The piece plays well and then becomes the version people believe, which is a specific harm to a real person and to everyone the real events happened to. The distortions that do this are almost never the obvious ones — the merged character, the invented scene — but the quiet ones: the deathbed apology, the moment he understood, the line where she forgives.
**Used for and where it works best:** As a diagnostic, and it is a short one. Take every turn in the arc and ask what document, interview or contemporaneous account it rests on. A turn with no source is either cut, or moved into someone's mouth and attributed — "his daughter believes he understood, at the end; his son does not" — which is stronger drama than the invented version and is true. The two reliable warning signs: the subject arrives at insight in the final ten minutes having shown none for two hours, and nobody in the film is left angry with them. Real forgiveness is uneven and partial; unanimous forgiveness is always an authorial decision. The honest alternatives are all available — `arc.real_person_arc` for a change the evidence supports at the strength it supports it, `arc.acceptance` where the situation could not be fixed, `arc.reported_arc` where the record only holds other people's accounts, and `arc.flat` where the person genuinely did not change and the world around them did.
**Best in:** formats: — | genres: — (hurts most in biopic and heritage film, where the piece becomes the popular memory of someone who cannot answer; in Documentary, where the form's whole claim is that it did not invent; and in advocacy work, where an imposed redemption converts a case into a fable and the opposition will say so)
**Avoid when:** — the case routinely confused with this failure is legitimate compression. Merging three colleagues into one, moving two conversations into one room, inventing dialogue for a documented meeting — these are conventions of the form, declared by `info.true_story_frame`, and they are not this. The failure is specifically the invented *change*: compressing how a person got somewhere is craft, inventing that they arrived is not. Its mirror image, equally dishonest, is the imposed refusal — flattening a real person who did change into someone who could not, because the film prefers them tragic.
**Example:**
> WHAT THE RECORD HOLDS: he gave evidence in 1974, he was not believed, he never spoke publicly again, and he died in 1996. There is one letter, to his brother, which says: "I have stopped thinking about it."
>
> IMPOSED — the version that shoots well:
> > *(Hospital. He takes his daughter's hand.)*
> > "I should have kept going. I should have made them listen. I know that now."
> > "You did everything you could, Dad."
>
> HONEST — same scene, same emotion available, nothing invented:
> > *(Hospital. She reads him the letter. He listens.)*
> > "'I have stopped thinking about it.'" She looks up. "Had you?"
> > He doesn't answer. He is looking at the window, and he might be asleep, and she waits about a minute and then folds the letter up.
>
> *(One of these two scenes is what a viewer will remember as a fact about a real man. The second one is the only one that is.)*

**Yields to:** `arc.real_person_arc` — Repair: claim only what the record supports.  
`arc.imposed_arc`

---

## Coverage

**12 cards** in this file, across 5 sections: Whose Arc Is It (4), Arcs Found Rather Than Designed (2), Arcs That Do Not Complete (3), Arcs Under Production Pressure (2), Named Failure (1).

**All four gaps `arcs.md` recorded are closed.** Its Coverage section ended by naming four techniques with no card anywhere in the database: the narrator's arc as distinct from the narrated character's (`arc.narrator_arc`), the interactive case where the player rather than the character changes (`arc.player_arc`), the real person's arc where change is a matter of evidence rather than design (`arc.real_person_arc`), and the institution treated as the thing that changes (`arc.institutional_arc`). Each is now a card and each names the boundary against the adjacent cards that already existed.

**Deliberately not written, because it already lives elsewhere.** One home per technique:

- **The relationship's arc.** `rel.relationship_arc` already covers it completely — the pair's own change curve, running independently of both character arcs and able to resolve against them, with the four-position rule and the "no two consecutive scenes at the same position" test. It is the right card and it is in the right file. Cited, not duplicated. The pair as the unit of protagonism is `rel.relationship_as_protagonist`.
- **The character who is right at the start.** This is `arc.flat`, which is precisely the Truth-driven arc of a character who holds the correct belief and converts the world instead of changing. A second card would have split one technique across two files.
- **The moment the audience decides the change is real.** `arc.proof_scene` owns this: the post-climax scene that replays a first-act situation and lets the audience verify. A separate "credibility moment" card would have been the same technique under a different name.
- **The arc that reverses late** as an *ending* is `end.reversed_arc`, a named failure about a piece that returns the protagonist to their starting condition without arguing that change was impossible. The legitimate arc-level versions are `arc.fall`, `arc.corruption` and `arc.disillusionment`, all in Part 1.
- **The opponent's own arc** is `anta.antagonist_arc`; **change elided into a gap** is `char.offstage_change`, which `arc.reported_arc` explicitly distinguishes itself from; **change asserted without cost** is `char.unearned_change` and **a quality asserted and never staged** is `char.informed_attribute`, both of which `arc.false_arc` marks its boundary against; **the character built to be lost** is `char.exists_to_be_lost`, which `arc.interrupted_arc` builds on rather than repeats.

Named failures in this file: `arc.imposed_arc`.

Cards carrying a review date: `arc.arc_under_many_hands`.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Verified 2026-09-17.

- [Retrospective Narration — ResearchGate](https://www.researchgate.net/publication/308835596_Retrospective_Narration)
- [Unreliable Narrators and Perspective Shifts — Fiveable](https://fiveable.me/advanced-screenwriting/unit-4/unreliable-narrators-perspective-shifts/study-guide/delsmfEtkPkA7khR)
- [What Are Unreliable Narrators and How Do They Affect Stories? — Greenlight Coverage](https://glcoverage.com/2024/12/25/unreliable-narrators/)
- [The Unreliable Narrator: When the Voice Telling the Story Cannot Be Fully Trusted — eduKate](https://edukatesg.com/2026/08/29/how-literature-works-unreliable-narrator/)
- [The Positive Discomfort of Spec Ops: The Line — Game Studies](https://gamestudies.org/1602/articles/jorgensenkristine)
- [Papers, Please and Ludic Narrative — Game Developer](https://www.gamedeveloper.com/art/papers-please-and-ludic-narrative)
- [How Games Tell Tales, Part 4: Unreliable Narration, Militainment, and Spec Ops: The Line — Interactive Pasts](https://interactivepasts.com/blog-posts/how-games-tell-tales-part-4-unreliable-narration-militainment-and-spec-ops-the-line)
- [How to create a documentary character — Sight and Sound, BFI](https://www.bfi.org.uk/sight-and-sound/how-create-documentary-character)
- [What Makes a Biopic Truthful Even When It Takes Liberties With the Facts — Every Movie Has a Lesson](https://everymoviehasalesson.com/blog/2026/5/what-makes-a-biopic-truthful-even-when-it-takes-liberties-with-the-facts)
- [Biography & Narrative — Paul Kelly: Stories of Me](https://paulkellythemovie.com.au/education/representing-artist/biography-narrative/)
- [Difference Between Biopic and Documentary — StudyMassCom](https://studymasscom.com/film-studies/difference-between-biopic-and-documentary/)
- [What Is a Biopic? Meaning, Types, Examples and How They Work — Vancouver Film School](https://vfs.edu/news/biopics)
- [The Collective Protagonist: Multiple Points of View and the Search for Truth in Familial Narratives — University of Washington](https://digital.lib.washington.edu/researchworks/items/a4ad3ae6-b0e9-4743-8d33-378393c500e5)
- [Building Fictional Organizations — Scribes & Archers](https://rmarcher.com/2024/09/building-fictional-organizations/)
- [Distributed Agency in the Novel — Columbia University Narrative Intelligence Lab](https://nil.columbia.edu/projects/distributed-agency-in-the-novel)
- [Sequel Reset — TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/SequelReset)
- [How Movie Sequels Succeed or Fail at Character Arcs — Forefront](https://forefrontfestival.com/movie-sequel-character-arcs/)
- [How to Write a Sequel Without Repeating Yourself — Celtx Blog](https://blog.celtx.com/how-to-write-a-sequel/)
- [FAQ: How to Write Character Arcs in a Series — Helping Writers Become Authors](https://www.helpingwritersbecomeauthors.com/character-arcs-in-a-series/)
- [TV Characters Don't Change — Erik Bork](https://www.flyingwrestler.com/2021/07/tv-characters-dont-change/)
- [Anthology series — Wikipedia](https://en.wikipedia.org/wiki/Anthology_series)
- [Secondary Character Arcs, and How to Write Them — Scribophile](https://www.scribophile.com/academy/secondary-character-arcs-and-how-to-write-them)
- [What Are Live Service Games? Everything You Need to Know in 2026 — Magic Media](https://magicmedia.studio/news-insights/what-are-live-service-games/)
