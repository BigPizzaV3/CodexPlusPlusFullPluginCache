# Genres — world

Entry point into the database. Each kit ranks a short list of techniques by `id`; open the `cat-*.md` file named for that id's prefix (or `arcs.md`, `structures.md`, `situations.md`) for the full card.

A genre kit carries something a format kit does not: **required beats.** Genre in writing is a set of obligations, not a marketing label. The reader who opens an epic fantasy has signed a contract, and the beats below are its clauses — 15 to 20 specific plot events, in order, that the story owes. Miss one and the reader registers a void they cannot name. Hit all of them and nothing else, and you have written formula: the cure is Truby's — carry two or three other genres in supporting roles, and let one of them argue against the primary.

These seven are the world end of the shelf: the genres where the setting is not a backdrop but a claim. Myth, Fantasy, Science Fiction, Dystopia, Western, Heritage and Historical all ask the reader to hold a world in their head while the plot runs, and all of them fail the same way — the writer, who has built the world, forgets that the reader has not. So every kit here states its **world budget** inside its Rules: how many proper nouns and new rules the audience can absorb in the opening, and where the rest of the exposition is allowed to go. The `expo.*` cards in `cat-expo.md` are the working tools for that budget and are ranked heavily throughout.

**Heritage** in this file is the genre, not the format. The format kit — running time, archive licensing, narration registers — is *Heritage and Historical Documentary* in `formats-doc.md`. The genre kit here is the story whose protagonist is a civilisation rather than a person, and it is written on the assumption that some of its audience are the descendants of its subject. That is not a note about tone. It changes what counts as a craft error.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Myth](#myth)
- [Fantasy and Epic](#fantasy-and-epic)
- [Science Fiction](#science-fiction)
- [Dystopia](#dystopia)
- [Western](#western)
- [Heritage (civilisation-focused)](#heritage-civilisation-focused)
- [Historical and Biopic](#historical-and-biopic)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## Myth

**What the genre argues:** Myth asks whether a person can carry more than a person's share — and what it costs the one who tries. It is the genre of the long journey outward, and its claim is that identity is not discovered by introspection but by travelling far enough that the self is worn down to what it actually is. Every myth is finally an argument about whether the old order deserves to survive the hero who was sent to save it.

**Required beats:**
1. The world is shown as two orders at once: the visible settlement and the unseen order that governs it, and one character can feel the second.
2. A broken origin — the hero is born wrong, exposed, orphaned, or loses the father before page one.
3. He is raised outside his true station, and someone in the household knows and does not say.
4. The old order fails in public, at a ritual: a harvest, a coronation, a sacrifice that does not take.
5. A talisman arrives that identifies him — an object, a name, a scar, a summons.
6. He refuses, and the refusal costs someone else their life or their place.
7. He leaves, and the leaving is witnessed and marked by a person who cannot follow.
8. A donor tests him on the road — hospitality, a riddle, a beggar — and he passes or fails on character, not strength.
9. He receives the agent of power, and it arrives with a stated prohibition attached.
10. Allies attach, each carrying one capacity the hero lacks.
11. Successive strangers oppose him, a new opponent per stage, all of them asking one question about his right to be on this road.
12. He breaks the prohibition, and the world answers immediately.
13. A marked threshold is crossed — river, gate, pass — after which the way back is closed.
14. The descent: he enters the place of the dead and meets a version of the father, or of the thing he fled.
15. He learns the true scale of the wrong: the sickness is in the order itself, not in one villain.
16. The gauntlet — trials with no gap between them, stripping him of the allies and of the agent.
17. The violent battle, against the opponent who embodies the old order in a body.
18. Self-revelation delivered in public, to a people rather than a confidant, so it lands as law and not as insight.
19. He outgrows the code he set out to serve; the new equilibrium is a changed rule for everyone, and he is usually excluded from it.

**Supporting genres:** Fantasy supplies the subworlds at beats 13 and 14, and keeps the journey from becoming a sequence of fields. Coming of Age gives beats 2, 6 and 9 an interior — without it the hero is a function. Tragedy is the one to let contradict the primary: run it under beat 19 and the hero's victory becomes the thing that makes him unhousable.

**Rules:** World budget — four proper nouns before the departure and no more, one cosmology rule per stage of the journey, and every further name introduced by a character who needs it said | Put the unseen order in a physical object before you put it in a line of dialogue | Give the donor a test the hero can fail, and let him nearly fail it | Attach a prohibition to every gift, and break exactly one | Vary the opponents but not the question — successive strangers, one interrogation | Stage the descent as a meeting, not a landscape | Deliver the self-revelation in front of witnesses | End on the new rule, not on the homecoming

**Avoid:** The journey as a list of places, which is what happens when each stage has a new location and no new pressure — the reader stops distinguishing them by the fourth. Cosmology delivered in a prologue that nobody needs until page two hundred: the rules of the unseen order belong at the moment they cost someone something, and nowhere earlier. Prophecy used as plot, which removes the hero's decisions and converts him into an errand runner. The hero who is special by birth and never by conduct — beat 8 exists precisely so that the reader watches him earn what the bloodline gave him. And the return that restores everything, which argues the journey was a detour.

**The kit (ranked):**

1. **The Hero's Journey** (Structure) `struct.heros_journey`
   The genre's structural chassis. Read it as a set of obligations here, not as a template to fill.
2. **The Quest** (Situations) `sit.booker_the_quest`
   Booker's shape supplies what the Journey card leaves out — the object, and why it is worth the road.
3. **The Ghost** (Arc) `arc.the_ghost`
   Beat 2. Myth's ghost is a birth, not an incident, and it is the only thing that makes beat 19 cost anything.
4. **Multiple Opponents, One Question** (Antagonist) `anta.multiple_one_question`
   Beat 11 exactly. Truby's successive strangers fail unless all of them are asking the same thing.
5. **First Function of the Donor** (Situations) `sit.propp_12_donor_test`
   Beat 8. Propp catalogued this a century ago and it is still the beat most often skipped.
6. **Receipt of a Magical Agent** (Situations) `sit.propp_14_magical_agent`
   Beat 9. The card's point is the transfer, not the object — who gives it, and on what terms.
7. **The Gate, the Gauntlet, the Visit to Death** (Structure) `struct.truby_18_gate_gauntlet`
   Beats 13, 14 and 16 are one movement in Truby's scheme. Plot them as one.
8. **The Journey Sequence** (Sequence) `seq.journey_sequence`
   The mid-level unit this genre is built from. It is what stops the road becoming a list.
9. **The Story Circle** (Structure) `struct.story_circle`
   Harmon's compression of the same shape — use it when the myth has to run at short length.
10. **Conflict with a God** (Situations) `sit.polti_31_conflict_with_a_god`
    Polti's situation 31 is the myth opponent in its purest form: an opponent who cannot be defeated, only answered.
11. **Mentor and Student** (Relationships) `rel.mentor_and_student`
    The donor at beat 8 often becomes this. The card's rules on when the mentor must be removed apply directly.
12. **The Incantatory Register** (Voice) `voice.incantatory_register`
    Myth tolerates — and at beats 18 and 19 requires — a register no realist genre would allow.
13. **Self-Revelation** (Structure) `struct.truby_20_self_revelation`
    Beat 18. Read the card for why the public delivery changes what the revelation *is*.
14. **Worldbuilding by Implication** (Exposition) `expo.implication_worldbuilding`
    How the second order gets into the reader without a cosmology lecture. The whole world budget rests here.
15. **The Thematic Motif** (Theme) `theme.thematic_motif`
    Myth carries meaning by repetition across stages. The motif is the thread the stages are strung on.
16. **Frame Narrative** (Time) `time.frame_narrative`
    The told-story frame is native here, and it solves beat 19: someone survived to tell it, which is itself the new equilibrium.

---

## Fantasy and Epic

**What the genre argues:** Fantasy asks what a person would do if the constraints everyone accepts as permanent turned out to be negotiable — and answers that the constraints simply move. It is the genre of exploration and of price: magic that costs nothing is decoration, and a world with no rule is a mood. The epic scale adds a second argument on top, that an order can end, that its ending is survivable, and that someone has to carry what is left.

**Required beats:**
1. Open inside the world's ordinary, with the marvellous treated as unremarkable by the people who live in it.
2. One rule of the world demonstrated inside the first pages, at someone's cost.
3. A protagonist positioned to ask: newcomer, apprentice, hidden heir, exile — someone for whom a question is not stupid.
4. The wound in the world is named — a war ending, a king dying, a season that will not turn.
5. The passageway: a door, a map, a death, a name that moves the protagonist out of the known region.
6. The first stranger on the road gives one true fact and one false one, and does not know which is which.
7. The company assembles, each member owed something different by the journey.
8. The magic exacts its first price on the protagonist — in body, in standing, or in years.
9. A subworld is entered with its own economy and its own rules, incompatible with the first.
10. A bargain or prohibition is accepted whose terms the protagonist does not fully understand.
11. Betrayal from inside the company, sourced in an older loyalty rather than in malice.
12. The scale reveal: the local problem turns out to be one face of a much larger one.
13. A defeat that loses territory, a city or a people, not merely a fight.
14. The company breaks, splitting the narrative into parallel lines that no longer share information.
15. The super-magical moment — the one scene where the world's impossible is exercised at full extent, and the reader gets what they came for.
16. A cost is paid that cannot be reversed: a death, a limb, a memory, a name.
17. The final test on the antagonist's ground, where force is insufficient and the bargain from beat 10 decides it.
18. The old order ends whether or not the heroes win.
19. Return, and the returning party cannot re-enter the ordinary life of beat 1.

**Supporting genres:** Myth carries the journey architecture and gives beats 5 and 17 their shape. War supplies beats 13 and 18 — an epic without a real war genre under it produces battles with no logistics and no grief. Love Story is the useful contradiction: run it against the quest so that beat 16 costs the protagonist the thing the quest was for.

**Rules:** World budget — five proper nouns in the first chapter, one new rule per sequence, and no term that is not used in action within two pages of being coined | Demonstrate every rule before you rely on it, and price it before you let anyone enjoy it | Give the magic a currency, and spend that currency where the reader can see the meter | Put the map in the journey, not in the front matter | Let one member of the company be wrong about the world in a way the reader can check | Make the scale reveal a recontextualisation of something already shown, never new information | Spend the super-magical moment once, late, and in full | End the order, not just the villain

**Avoid:** The lore dump wearing a cloak — a character explaining the Third Age to another character who lived through it is the genre's signature failure, and the reader's eye slides off it every time. Magic without an accounting system, which makes every rescue arbitrary and every defeat authorial. Proper noun avalanche in the first chapter: a reader will hold four or five invented names before they stop attaching them to anything, and a glossary at the back is an admission that the text failed, not a solution to it. The company where everyone agrees, which converts twelve characters into one character with twelve mouths. And the ending that restores the old order intact — beat 18 is not optional, and an epic that puts the king back on the same throne has spent nine hundred pages arguing for nothing.

**The kit (ranked):**

1. **Rule by Demonstration** (Exposition) `expo.rule_by_demonstration`
   Beat 2 and the genre's first law. Nothing is true in a fantasy until it has been done in front of the reader.
2. **Show the Rule's Price** (Exposition) `expo.rule_cost_demo`
   Beat 8. The card's argument — that the price, not the rule, is what the reader actually retains — is the whole difference between magic and decoration.
3. **The Proper Noun Budget** (Exposition) `expo.proper_noun_budget`
   This kit's world budget in card form. Read it before naming a single kingdom.
4. **Worldbuilding by Implication** (Exposition) `expo.implication_worldbuilding`
   The load-bearing technique: the world the reader infers is bigger and cheaper than the world you describe.
5. **Coined Term in Context** (Exposition) `expo.coined_term_in_context`
   How an invented word gets learned without a gloss. Three uses in three different functions.
6. **The Newcomer's Eye** (Exposition) `expo.newcomer_eye`
   Beat 3. The most natural delivery system in the genre — and the card names the trap of the newcomer who only asks.
7. **The Quest** (Situations) `sit.booker_the_quest`
   The object, the company, the road. Booker's obligations map to beats 7, 9 and 17 directly.
8. **The Gate, the Gauntlet, the Visit to Death** (Structure) `struct.truby_18_gate_gauntlet`
   Beat 17. Epic finales collapse when they are one fight; this card supplies the staged approach.
9. **The Scale Reveal Opening** (Openings) `open.scale_reveal`
   Usable at beat 12 as well as at the open — the card's mechanism is recontextualisation, not size.
10. **The Threat That Obeys Rules** (Tension) `tens.threat_with_rules`
    A magical antagonist bound by law can be feared for six hundred pages. One without law can only surprise.
11. **Multi-POV Architecture** (POV) `pov.multi_pov_architecture`
    Beat 14 makes this structural. The card's rules on strand length and handoff are what keep the split readable.
12. **Writing More Than Five** (Relationships) `rel.more_than_five`
    The company at beat 7. Above five, groups need deliberate management or they dissolve into a crowd.
13. **The Iceberg Principle** (Exposition) `expo.iceberg_principle`
    The written world should be the visible eighth. The card is about what the unwritten seven-eighths does to the eighth.
14. **The Cost Paid** (Endings) `end.cost_paid`
    Beat 16. Irreversibility is the only thing that distinguishes an epic ending from an adventure ending.
15. **Receipt of a Magical Agent** (Situations) `sit.propp_14_magical_agent`
    Beat 10. Propp's function includes the terms of transfer, which is the part modern fantasy keeps dropping.
16. **The Optional Appendix** (Exposition) `expo.optional_appendix`
    Legitimate here — but read the card's condition: an appendix is a reward for the reader who finished, never a prerequisite for the one who started.

---

## Science Fiction

**What the genre argues:** Science fiction asks what a human being still is once one condition of being human has been changed — and whether the part we call essential survives the change. Its subject is never the technology; it is the society that grew around the technology and the person shaped by that society. The genre's characteristic weakness in its protagonist is being unevolved, still carrying the old species into a world that has moved.

**Required beats:**
1. An ordinary detail of daily life shown working differently, with no comment and no explanation.
2. The society's operating rule stated by an institution doing its routine job.
3. The protagonist placed inside that system as a functionary, a user, or a product of it.
4. Weakness-need established as an unevolved trait — what he shares with the society, not what marks him out from it.
5. The novum demonstrated: the single thing this world has that ours does not, shown in use by someone competent.
6. Its first cost paid by a minor character, in front of the protagonist, and treated as normal.
7. Desire set on something the system makes difficult: go there, keep her, find out, get out.
8. The authorities revealed as the opponent, holding a mandate they can defend.
9. An expert explains the mechanism badly, incompletely, or self-servingly.
10. A subworld shows the same technology at a different social level, where it means something else entirely.
11. The first plan uses the novum as designed, and fails for exactly that reason.
12. The real function of the novum is revealed — what it was built for, as against what it is sold as.
13. A person is used by the system in a way that proves this is the design and not a malfunction.
14. The protagonist or the closest ally is revealed to be a product of the system: conditioned, manufactured, owned, or indebted.
15. The plan is rebuilt to use the novum against its design.
16. Confrontation with the authority, in which the authority makes its case and is partly right.
17. The battle turns on a rule established at beat 5, not on force.
18. Public or cosmic self-revelation: what a human is, redefined for everyone rather than for the hero.
19. New equilibrium — the technology remains, and the society has either changed around it or visibly refused to.

**Supporting genres:** Detective carries the middle, because beats 9, 11 and 12 are an investigation whether or not anyone is investigating. Myth supplies the shape when the story goes outward — the ship, the colony, the long voyage — and gives beat 18 its public register. Love Story is the productive contradiction: attach it to beat 14, so the question of what counts as a person is asked about someone the protagonist loves rather than in the abstract.

**Rules:** World budget — one novum, three proper nouns in the opening, one invented term per scene and never two in a sentence; everything else is delivered downstream, at the moment it costs someone something | Show the technology working before you show it failing | Give the authority a real mandate and a defensible case | Make the social consequence, not the device, the subject of every scene | Let the expert be wrong in a way the reader can later check | Put the same technology at two social levels before the midpoint | Decide the climax on an established rule, never on new capability | Redefine the human in public at beat 18, or the story was an adventure with hardware

**Avoid:** The "as you know" family, which in this genre arrives disguised as briefing, log entry, or news broadcast and is the same offence in all three costumes. Explaining the science to the depth the writer researched it rather than the depth the scene needs — the reader's tolerance for mechanism is roughly one paragraph, and it resets only after something happens. The novum introduced late, which turns the climax into a cheat because the reader was never given the chance to reason with it. The society that is one idea wide, where a single technology has apparently produced no subcultures, no black market and no religion. And the ending that destroys the technology, which is the genre's way of refusing to answer its own question.

**The kit (ranked):**

1. **Familiar Anchor, One Strange Word** (Exposition) `expo.familiar_anchor`
   Beat 1 in a single technique, and the cheapest world-delivery mechanism the genre has.
2. **Rule by Demonstration** (Exposition) `expo.rule_by_demonstration`
   Beat 5. The novum has to be watched in competent hands before it can be argued about.
3. **The Rule of the World** (Openings) `open.rule_of_the_world`
   Beat 2. Opening on the society's operating rule, stated by its own machinery, rather than by a narrator.
4. **Need-to-Know Ladder** (Exposition) `expo.need_to_know_ladder`
   The genre's exposition scheduler. It answers where each piece of the world goes, which is the harder half of the budget.
5. **Coined Term in Context** (Exposition) `expo.coined_term_in_context`
   One term per scene, learned by use. The card's three-function rule is the test to apply.
6. **The Institutional Antagonist** (Antagonist) `anta.institutional`
   Beat 8. Truby's authorities-as-opponent; the card supplies the mandate that keeps them from being cartoon.
7. **The Opponent Is Right About Something** (Antagonist) `anta.right_about_something`
   Beat 16. A science fiction authority with no case produces a story with no argument.
8. **Show the Rule's Price** (Exposition) `expo.rule_cost_demo`
   Beat 6. The cost is what converts a gadget into a society.
9. **The Expert Who Explains Badly** (Dialogue) `dial.expert_explains_badly`
   Beat 9, and the genre's best defence against the lecture: expertise that is partial, motivated, or defensive.
10. **The Controlling Idea** (Theme) `theme.controlling_idea`
    Science fiction is thesis-driven whether the writer admits it or not. Write the thesis before the hardware.
11. **The Recontextualising Reveal** (Information) `info.recontextualising_reveal`
    Beat 12. The real function of the novum is a reinterpretation of shown material, not a new fact.
12. **Non-Human Viewpoint** (POV) `pov.nonhuman_pov`
    Beat 14 done from inside. The card's constraints on interiority are what stop it becoming a costume.
13. **Environmental Exposition** (Exposition) `expo.environmental_detail`
    Beat 10. The subworld is delivered by what is on the walls, not by what anyone says about it.
14. **The Off-Screen World** (Exposition) `expo.offscreen_world`
    A galaxy implied by three references costs nothing and outperforms one that is described.
15. **Descriptive, Not Prescriptive** (Theme) `theme.descriptive_not_prescriptive`
    Beat 18 lands only if the film has not been instructing the reader for two hours beforehand.
16. **Answer the Question That Was Asked** (Endings) `end.answer_the_question_asked`
    The genre asks a specific question about the human. The ending is judged on whether it answered that one.

---

## Dystopia

**What the genre argues:** Dystopia asks what a system can take out of a person without killing them, and whether anything they had is genuinely theirs. It is a science fiction about consent: the society is not merely oppressive, it is *accepted*, and the horror is in the acceptance rather than in the boot. Its real claim is that the private self — the room, the diary, the person you love, the word that still means what it means — is the last territory, and that a sufficient system takes it.

**Required beats:**
1. The system shown functioning on a good day, from the viewpoint of someone who believes in it.
2. Its price displayed as routine, administered gently: a queue, a form, a ration, a ceremony.
3. The protagonist performs one small private act of noncompliance that nobody sees.
4. The official language is heard doing its work — a word used to mean its opposite, unremarked.
5. A person disappears, and the absence is handled administratively and correctly.
6. The protagonist meets someone who remembers before, or holds an object from before.
7. The forbidden thing is acquired: a book, a diary, a photograph, a song, a body.
8. A private space is built — a room, a field, a frequency — and the reader is allowed to relax inside it.
9. First proof of surveillance: the system already knew, and let it run.
10. Rebellion is chosen deliberately, with the cost stated out loud by the character before they pay it.
11. Contact with the resistance, which is smaller, meaner or more compromised than promised.
12. An architect of the system explains its origin, and it is a reasonable answer to a real catastrophe.
13. The private space is entered and destroyed.
14. Betrayal by the most trusted person, for a motive the reader can follow and does not despise.
15. Capture, and the interrogation is a conversation rather than only pain.
16. The protagonist is made to betray the one thing they said they would not.
17. Apparent restoration — returned to their place, functioning, unremarkable.
18. Proof of what was extracted: they cannot feel, or cannot say, the thing they had at beat 7.
19. A coda from outside the system — an appendix, a later voice, a document — which decides whether it fell.

**Supporting genres:** Love Story supplies beats 7, 8 and 16, and is close to mandatory — the system needs something specific to take. Detective runs the middle, because beats 9 and 12 are the protagonist finding out how the machine actually works. Myth is the useful contradiction: the reader wants the journey shape and the system is built to deny it, and that friction is the genre's engine.

**Rules:** World budget — the system's rules arrive at a rate of one per institution encountered, never as history; three proper nouns in the opening, and the regime's own vocabulary introduced by people using it sincerely | Show the system working before you show it failing | Let the true believer be intelligent | Give the private space enough pages that its loss registers as a loss | State the cost of rebellion in the character's own mouth before they pay it | Make the architect's case a real answer to a real catastrophe | Take the specific thing, not freedom in the abstract | Put the surveillance proof before the resistance contact, not after | Decide the regime's fate outside the protagonist's viewpoint

**Avoid:** The regime that is evil for the pleasure of it, which makes beat 1 impossible and therefore makes the whole genre impossible — if nobody sensible believes in it, there is nothing to explain. Exposition delivered as the history of the collapse, usually in a prologue: the reader does not need the founding war, they need to watch a form being filled in. Rebellion that arrives because the plot needed a second half, rather than being built from twelve chapters of accumulated, priced grievance. The resistance shown as clean and correct, which converts the story into a fantasy of rescue. And the ending where the system falls because the protagonist was right — the genre's characteristic strength is that the protagonist loses, and the coda at beat 19 is where the argument gets to be won instead.

**The kit (ranked):**

1. **The Rule of the World** (Openings) `open.rule_of_the_world`
   Beat 1. Open on the system working, not on the protagonist suffering.
2. **The Institutional Antagonist** (Antagonist) `anta.institutional`
   The opponent here is a procedure with people in it. The card's rules on giving it a face without shrinking it are load-bearing.
3. **The Institutional Voice** (Voice) `voice.institutional_voice`
   Beat 4. The regime's language is the regime. Write the notices, the forms and the announcements first.
4. **Diegetic Text** (Exposition) `expo.diegetic_text`
   The poster, the ration card, the transit notice. This genre's cheapest and densest exposition channel.
5. **Environmental Exposition** (Exposition) `expo.environmental_detail`
   Beat 2. Bureaucratic routine delivered as furniture rather than as speech.
6. **Revolt** (Situations) `sit.polti_08_revolt`
   Polti's situation 8 with its full apparatus — the tyrant, the conspirator, and the crucial question of who is dragged in.
7. **The Opponent Is Right About Something** (Antagonist) `anta.right_about_something`
   Beat 12. The architect's catastrophe must be one the reader concedes was real.
8. **The Disillusionment Arc** (Arc) `arc.disillusionment`
   The genre's default arc — belief to sight, and the card is explicit that sight is not the same as freedom.
9. **The Secret** (Character) `char.the_secret`
   Beats 3 and 7. The private act and the hidden object are the same mechanism, and the card is about how they leak.
10. **Social Dread** (Tension) `tens.social_dread`
    The correct tension register here: not a monster in the dark, but the wrong sentence said in the wrong room.
11. **The Group with a Shared Secret** (Relationships) `rel.group_secret`
    Beat 11. The card's seams are where the resistance breaks, and it breaks along them.
12. **Show the Rule's Price** (Exposition) `expo.rule_cost_demo`
    Every regulation the story states must be paid for by someone the reader has met.
13. **Coined Term in Context** (Exposition) `expo.coined_term_in_context`
    The regime's vocabulary, learned from sincere users. A term that is only ever mocked teaches nothing.
14. **High-Context Indirection** (Subtext) `sub.high_context_indirection`
    How people speak when the room is monitored. The genre's native dialogue mode.
15. **The Cost Paid** (Endings) `end.cost_paid`
    Beat 18. The ending is an inventory of what was extracted, itemised.
16. **The Found Document** (POV) `pov.found_document`
    Beat 19. The appendix, the transcript, the later scholar — the outside voice that settles the argument the protagonist lost.

---

## Western

**What the genre argues:** The Western asks what a violent man is for once the violence has built the thing it was needed for. It is the genre of the line between freedom and civilisation, and it argues that the two are not compatible: somebody has to do the killing that makes the town safe, and the town cannot then contain him. Its moral engine is a code — a private, unwritten, absolutely binding set of rules held by a man with no institution behind him.

**Required beats:**
1. The landscape established as an agent: distance, water, weather, and how long it takes to reach help.
2. A settlement shown mid-construction — church frame, rail line, fence, schoolhouse. Civilisation arriving, unfinished.
3. The hero enters from outside and is named by reputation before he demonstrates anything.
4. The code is stated by a minor character: what a man here does and does not do.
5. The victim group established with something they cannot defend — land, herd, water rights, a daughter.
6. The inciting attack: the villain or the land takes something, and the law is absent, bought, or two days away.
7. The hero refuses the job.
8. His shame surfaces — the past killing, the abandoned family, the war he fought on the wrong side of.
9. He accepts, for a private reason he does not state and the story does not explain.
10. A demonstration of violence that sets the genre's price on it: fast, ugly, brief, and followed by a body someone has to move.
11. The town hedges — merchant, sheriff and preacher each explain why they cannot help, and each is reasonable.
12. The bad cowboy appears: an opponent who is what the hero would be without the code.
13. An ally is killed or crippled, proving the villain will not be beaten by fairness.
14. The hero is beaten, disarmed or run out, and the settlement is left exposed.
15. He arms himself, deliberately, in a scene with no dialogue.
16. The walk — approach along the street, the town watching from doorways, nobody intervening.
17. The showdown, decided in seconds and paid for over the rest of the film.
18. The community is saved, and immediately closes around itself.
19. He rides out, or stays and is diminished by staying. The frontier he defended has no room in it for him.

**Supporting genres:** Myth supplies the arrival-and-departure frame and the sense that the hero is a figure rather than a man. Crime carries beats 6, 11 and 13 — the mechanics of who is being paid by whom. Love Story is the contradiction to run underneath: attach it to the settlement, so beat 19 costs the hero a specific person and not just a landscape. In revisionist work, swap Myth for Tragedy and every beat holds while its meaning inverts.

**Rules:** World budget — the period arrives through work and prices, not through history; six proper nouns total, most of them place names the audience will hear twice; no lecture on the year, the war, or the railroad | Establish the distance to help in the first ten minutes and never contradict it | State the code in someone else's mouth, and break it once | Make the town's cowardice reasonable | Price every killing with a body somebody has to bury | Keep the hero's motive private — the audience should infer beat 9, never be told it | Play the showdown short and the aftermath long | Let the community exclude him without malice

**Avoid:** The landscape as scenery rather than as antagonist — if the desert is only photographed, beat 1 has not happened and every later journey is free. The hero who is quick with a gun and never pays for it, which is the difference between a Western and a shooting gallery. Villains with no economic motive: the genre is about land, water and money, and a villain who simply enjoys cruelty removes the argument that civilisation is worth the cost. The code recited by the hero himself, which turns a moral position into a slogan — beat 4 belongs to a minor character for exactly this reason. And the ending where the town takes him in, which is a Western that has refused its own thesis; the revisionist route is to let him stay and show what staying does to him, not to pretend the contradiction dissolved.

**The kit (ranked):**

1. **The Flat Arc** (Arc) `arc.flat`
   The classical Western hero does not change; the town does. The card explains what the story must change instead.
2. **Reputation Before Entrance** (Character) `char.reputation_before_entrance`
   Beat 3. The most efficient character introduction in the genre, and the one it invented.
3. **Nature as Opposition** (Antagonist) `anta.nature`
   Beat 1. The land is an opponent with a schedule, not a location with a mood.
4. **The Wound as a Rule of Conduct** (Character) `char.wound_as_rule`
   Beats 8 and 9. The code is the wound, formalised. This card is the join between them.
5. **The Promise of Violence** (Tension) `tens.promise_of_violence`
   The genre runs on deferred gunfire. The card is about the deferral, not the gunfire.
6. **Waiting as a Weapon** (Tension) `tens.waiting_as_weapon`
   Beat 16. The walk works because nothing happens for longer than is comfortable.
7. **The Opponent's Better Version** (Antagonist) `anta.better_version`
   Beat 12. The bad cowboy is the hero with the code removed — build him from the hero's own sheet.
8. **The Outsider in the Group** (Relationships) `rel.outsider_in_the_group`
   Beats 3 and 18. The card's dynamics are the exact mechanism by which the town needs him and cannot keep him.
9. **The Clipped Line** (Dialogue) `dial.clipped_line`
   The genre's dialogue register. Read the card for how much can be carried under a four-word sentence.
10. **The Moral Test** (Theme) `theme.moral_test`
    Beats 7, 9 and 17 are one test asked three times, with the price rising.
11. **Crime Pursued by Vengeance** (Situations) `sit.polti_03_crime_pursued_by_vengeance`
    Polti's situation 3 is the spine of half the genre; read it for the avenger's obligations.
12. **The Voice of a Place or an Object** (Voice) `voice.voice_of_a_place`
    Land, town and gun all speak in this genre. The card keeps that from turning purple.
13. **Environmental Exposition** (Exposition) `expo.environmental_detail`
    The period budget in practice: a price on a board, a brand on a hide, a half-built wall.
14. **The Anti-Theme** (Theme) `theme.anti_theme`
    The revisionist Western's entire operation. The card is how you argue against your own genre without sneering at it.
15. **The Quiet Ending** (Endings) `end.quiet_ending`
    Beat 19. After the showdown, the genre's real ending is small, and the card is about holding the nerve for it.
16. **The Final Image** (Endings) `end.final_image`
    The rider and the doorway. This genre's last shot carries more argument than its dialogue does.

---

## Heritage (civilisation-focused)

**What the genre argues:** Heritage asks what a people leaves behind when it stops being powerful, and who is entitled to tell that story now. Its protagonist is not a person but a continuity — a language, a craft, a city, a faith, a line of descent — and its dramatic question is always survival of transmission rather than survival of a life. It argues that a civilisation is not its monuments but the chain of hands that carried something from then to now, and that the chain is still being broken.

This is the one genre in the database whose audience routinely includes the descendants of its subject. That has a craft consequence and not only a moral one: for those viewers, an inaccuracy is not a flaw in the work, it is a claim about them, and it destroys the piece's authority in the same sentence it appears. The rules below treat accuracy and the limits of dramatisation as constraints of the form.

**Required beats:**
1. A present-day access point is established: a site, an object, a living practice, or a person who still does the thing.
2. The civilisation's own name for itself is given once, in its own language, and held unchanged for the rest of the piece.
3. The material base is shown before the glory — water, grain, clay, stone, a trade route.
4. One ordinary life is reconstructed from evidence, and the evidence is named as it is used.
5. The specific contribution is demonstrated rather than asserted: the thing this civilisation actually did that others did not.
6. First external contact, told from both sides wherever both sides left a record.
7. What the sources do not say is stated out loud, and the gap is given a size.
8. An internal conflict — a succession, a schism, a reform, a class — so that the civilisation is not presented as a single mind.
9. The peak: one dated, documented moment when the system demonstrably worked.
10. A live scholarly disagreement is presented as a disagreement, with both readings named and neither smuggled in as settled.
11. The pressure that is not aimed — climate, silt, plague, a trade route moving — operating across generations.
12. The rupture: conquest, collapse, dispersal, forced conversion, partition.
13. What was destroyed, and by whom, named specifically and without expanding the perpetrator into a whole people.
14. What survived, traced through the physical chain that carried it: copyists, traders, migrants, monasteries, museums.
15. The distortion — how the story came to be told wrongly, by whom, and what they gained from telling it that way.
16. The descendant community present now, speaking in its own voice rather than being spoken about.
17. A continuity demonstrated in something small and checkable: a word, a recipe, a letterform, a wedding custom.
18. The present-day threat to the record — looting, war, a dam, a demolition, an emptying village.
19. Return to the object or site of beat 1, and hand the audience one specific thing they can now go and verify.

**Supporting genres:** Historical supplies beats 8, 9 and 12 with individual actors, without which the civilisation stays abstract. Migration and Family Drama carry beats 14 and 16 — the chain of hands is made of households. Tragedy is the contradiction worth running: the peak at beat 9 read against the rupture at beat 12 is the genre's most honest structure, and it forbids the triumphalism this genre otherwise drifts into.

**Rules:** World budget — four to six proper nouns the audience must retain across the whole piece, and one new period concept per sequence; everything else is delivered at the object, at the moment the object is on screen | Separate known, inferred and disputed audibly, and never let inference borrow the grammar of fact | Cite the evidence class in the line that uses it — tablet, chronicle, excavation, oral testimony — so the audience can weigh it | Give the dating range, not the flattering end of it | Name a destroyer specifically; never generalise a perpetrator into an ethnic group or a religion | Present live scholarly disagreement as disagreement, and say which reading you are following and why | Let the descendant community speak in beat 16 rather than being summarised | Signal every reconstruction as reconstruction, including a still image animated to imply motion it never had | Carry one anchoring object from beat 1 to beat 19

**Avoid:** Greatness asserted rather than demonstrated — the piece that opens by calling its subject the greatest civilisation of the ancient world has spent its authority before it has earned any, and the descendant viewer, who has heard the claim a hundred times, hears the hundred-and-first as advertising. Inference sliding into fact: "they would have believed" and "it must have felt" are the genre's characteristic dishonesty, and they are the sentences that get quoted back at you by the one specialist who watches. Flattening the civilisation into a single unanimous people with one costume, one god and one opinion, which is the same erasure the piece is usually protesting against. Compressing a dating range to its most impressive end, or borrowing a later period's imagery because it looks better — a five-hundred-year anachronism in a costume is legible to exactly the audience whose trust the piece needs. And ending on the ruin, which quietly argues that these people are over; beat 16 exists because they are not, and a piece that never returns to the living has made its subject into a museum with the descendants standing outside it.

**The kit (ranked):**

1. **Heritage Specificity** (Exposition) `expo.heritage_specificity`
   The genre's first law. The weight of the tool, the price of the grain, the width of the street — specificity is what replaces the footage that does not exist.
2. **The Narration Contract** (Exposition) `expo.doc_narration_contract`
   The three registers — known, inferred, disputed — held audibly apart. This card is the accuracy rule in operational form.
3. **The Object That States the Rule** (Exposition) `expo.object_tells_rule`
   Beats 1 and 19. An object survives from then to now, which makes it the only honest bridge the piece has.
4. **The Pressure That Is Not Aimed** (Antagonist) `anta.ambient_pressure`
   Beat 11. The antagonist of a civilisation is usually a climate or a trade route, and this card is how that is dramatised without a villain.
5. **The Absent Antagonist** (Antagonist) `anta.absent`
   Beats 12 and 13. The destroyer is often centuries dead and unnamed; the card handles opposition that cannot appear.
6. **The Proper Noun Budget** (Exposition) `expo.proper_noun_budget`
   This kit's world budget. Four to six names retained, not forty introduced — and a subtitled audience holds fewer.
7. **First Person Plural** (POV) `pov.collective_we`
   Beat 16, and the genre's structural question in a grammatical form: who is the *we* of this piece, and are they in the room.
8. **Real People and the Composite** (Character) `char.real_person_composite`
   Beat 4. The card's rules on what a composite may and may not do are where this genre's dramatisation limit actually lives.
9. **Nostalgia Without Sentimentality** (Emotion) `emo.nostalgia`
   The genre's most common tonal failure, addressed directly. Longing is legitimate; a greeting card is not.
10. **Dual Timeline** (Time) `time.dual_timeline`
    Beats 1, 16 and 19 against 3 to 15. The distance between then and now is the subject, so build the structure that measures it.
11. **The Voice of a Place or an Object** (Voice) `voice.voice_of_a_place`
    Beat 17. Continuity demonstrated through a word or a letterform needs a register, and this is the one.
12. **Subtext Across a Language Barrier** (Subtext) `sub.across_languages`
    Transliteration, translation and the losses in both. Decide the spellings once and hold them; the card explains the cost of not doing so.
13. **The Scale Reveal Opening** (Openings) `open.scale_reveal`
    Beat 9 and often beat 1. Scale delivered by recontextualising something small the audience has already accepted.
14. **Diegetic Text** (Exposition) `expo.diegetic_text`
    Inscription, seal, colophon, ledger. The civilisation's own writing is the strongest evidence class you can put on screen.
15. **Environmental Exposition** (Exposition) `expo.environmental_detail`
    Beat 3. The material base arrives as silt, salt, brick size and canal depth, not as a claim about greatness.
16. **The Handoff Ending** (Endings) `end.handoff_ending`
    Beat 19. Give the audience the specific verifiable thing. A heritage piece that ends on its own eloquence has kept the subject for itself.

---

## Historical and Biopic

**What the genre argues:** The historical drama asks whether a person could have acted otherwise inside the constraints of their moment, and the biopic narrows that to one life and one verdict. Both are arguments about determinism dressed as chronology. The genre's real claim is that character is what survives contact with a period's rules — and its central craft problem is that everyone in the audience knows how it ends, so the tension has to come from *why* rather than from *what*.

**Required beats:**
1. The frame is set: whose account this is, from when, and how they came to know it.
2. The controlling question is asked inside the first ten minutes — not who this person was, but the argument the piece intends to make about them.
3. The subject is introduced doing the thing they were good at, before anyone in the story calls them great.
4. The period's rules are established as a constraint on the subject specifically: what someone of their sex, class, faith, colour or nation could and could not do that year.
5. The wound or ghost is dated to a year and a place.
6. The first refusal by the world — the door that does not open, and the named person who holds it shut.
7. An ally provides access, and what that access costs the ally is shown.
8. The first real success, early enough that the audience learns what this person's capability looks like.
9. The institutional opponent appears holding a legitimate mandate.
10. Compression is declared — a montage, a title card, a jump — so the audience knows years are being skipped rather than suspecting the film forgot them.
11. The private cost is paid by a named person: a spouse, a child, a collaborator who was written out of the record.
12. The moral line is crossed — the compromise, the fabrication, the abandonment — and the piece declines to editorialise about it.
13. The event the audience bought a ticket for is staged late, and played without commentary.
14. The reversal of reputation: a court, a committee, a press, a crowd turning.
15. The record is challenged from inside the story — a letter, a testimony, a rival account contradicting what we have been watching.
16. The subject's own account of themselves, in their own sourced words.
17. The last capable act, showing what remained of the thing established at beat 3.
18. Death or withdrawal, given no more screen time than it took.
19. The afterlife of the reputation: what was named after them, what was suppressed, and who decided.
20. A closing statement of what is known, what was dramatised and what remains disputed.

**Supporting genres:** Tragedy is the default second genre, and beats 12, 14 and 18 are its property. Heritage carries beat 4 and beat 19 — the period and the posterity — and keeps the biopic from being a life lived in a vacuum. Love Story or Family Drama is where beat 11 lives, and one of the two is effectively mandatory, because a biopic with no domestic cost has agreed with its subject's own publicity.

**Rules:** World budget — the period is delivered through constraint and price, not through set dressing; six proper nouns the audience must retain, and every date that matters spoken twice | Ask the argument in the first ten minutes and answer it in the last ten | Establish capability before reputation | Declare every compression on screen | Name the person who paid the private cost, and give them a scene of their own | Play the famous event without underlining it | Put a genuine challenge to the record inside the drama, not only in the end titles | Say at the end what was invented

**Avoid:** The cradle-to-grave survey, which is a chronology rather than an argument and leaves the audience unable to say what the piece thought. Greatness announced by other characters — everyone in the room telling the subject they are a genius is the biopic's equivalent of "as you know", and it does the same damage. The composite character used to spare the piece a difficulty, as against to spare it a queue of near-identical minor figures; the first is a lie about a real event, the second is craft, and the difference is whether anyone real is made to do something they did not do. The period delivered as furniture, where the costumes are immaculate and nobody is constrained by anything. And the closing titles that quietly contradict the two hours before them — if the drama and the end cards disagree, the drama was the invention and the cards are an apology, which is a structural failure and not a disclaimer.

**The kit (ranked):**

1. **Dread of the Known Outcome** (Tension) `tens.known_outcome_dread`
   The genre's defining problem, solved. The audience knows he dies; the card is how that becomes an asset.
2. **Real People and the Composite** (Character) `char.real_person_composite`
   The dramatisation limit in card form. Read it before merging a single character.
3. **The Controlling Idea** (Theme) `theme.controlling_idea`
   Beat 2. A biopic without a thesis is a Wikipedia entry with a budget.
4. **Frame Narrative** (Time) `time.frame_narrative`
   Beat 1. Naming whose account this is converts an omniscient claim into a sourced one, which is both honest and dramatic.
5. **The Prologue of History** (Exposition) `expo.history_prologue`
   The one place a period preamble is legitimate. The card sets the conditions — and the length.
6. **Heritage Specificity** (Exposition) `expo.heritage_specificity`
   Beat 4. The period arrives as a price, a permit, a law, a distance. Never as a costume note.
7. **The Institutional Antagonist** (Antagonist) `anta.institutional`
   Beat 9. The opponent of a real life is usually a body with a mandate, and it must be allowed its mandate.
8. **The Moral Line** (Arc) `arc.moral_line`
   Beat 12. Where the subject's compromise sits, and how to stage it without prosecuting or defending.
9. **Competence Has a Price** (Character) `char.competence_cost`
   Beats 3, 11 and 17 as one through-line: what the ability took from the people around it.
10. **Ambition** (Situations) `sit.polti_30_ambition`
    Polti's situation 30 is the engine of most biopics; read it for the obligations the ambitious protagonist incurs.
11. **The Retrospective Narrator** (POV) `pov.retrospective_distance`
    The distance between the person who lived it and the person telling it is this genre's richest available irony.
12. **Summary Duration** (Time) `time.summary_duration`
    Beat 10. Compression is unavoidable; the card is about doing it visibly instead of hoping nobody notices.
13. **The Fall Arc** (Arc) `arc.fall`
    Beats 14 and 18 for the subjects who ended badly, which is most of the ones worth two hours.
14. **Dramatic Irony** (Information) `info.dramatic_irony`
    The audience's foreknowledge is permanent here. Write every scene knowing they know.
15. **The Epilogue** (Endings) `end.epilogue`
    Beats 19 and 20. The card's warning about the epilogue that argues with the film applies with unusual force.
16. **The Cost Paid** (Endings) `end.cost_paid`
    The verdict, itemised. What the life bought and who it was charged to.

---

## Coverage

Seven kits: Myth, Fantasy and Epic, Science Fiction, Dystopia, Western, Heritage (civilisation-focused), Historical and Biopic.

Adjacent kits elsewhere in the database. The primal genres — Horror, Thriller, Action, Crime, Gangster, War, Survival — are in `genres-primal.md`; War in particular sits under Historical here and supplies beats this file does not duplicate. The inquiry genres are in `genres-inquiry.md`, and Detective there carries the middle of both Science Fiction and Dystopia. Coming of Age, Memoir and Redemption are in `genres-growth.md`. Love Story, Buddy Love and Family Drama are in `genres-bond.md`, and every kit in this file names one of them as a supporting genre.

Two format kits overlap this file and are deliberately kept separate. *Heritage and Historical Documentary* in `formats-doc.md` holds the running times, the archive licensing, the reconstruction signalling and the narration registers; the Heritage kit here holds the argument and the beats. *Animation Feature* in `formats-film.md` carries the delivery constraints for Myth and Fantasy at feature length.

Exposition is the shared spine of all seven kits. `cat-expo.md` holds the cards these world budgets are built from, including the four failure cards no kit here ranks — `expo.lore_dump`, `expo.as_you_know`, `expo.proper_noun_avalanche` and `expo.glossary_crutch` — which between them account for most of what goes wrong in this half of the shelf.

## Sources

Consulted 2026-09-17.

- [John Truby's Story Beats for 14 Genres — The Elements of Writing](https://theelementsofwriting.com/truby-beats/)
- [John Truby on the New Rules of Genre Writing — The Elements of Writing](https://theelementsofwriting.com/truby/)
- [Writing Tips: The Anatomy Of Genres With John Truby — The Creative Penn](https://www.thecreativepenn.com/2022/11/28/anatomy-of-genre/)
- [Learn The Philosophies Behind 14 Major Genres — Jake Varrone](https://jakevarrone.substack.com/p/learn-the-philosophies-of-14-major)
- [Myth On-Line Class — Truby Writers Studio](https://truby.com/myth-on-line-class-product-page/)
- [Save the Cat! Genre Mapper](https://savethecat.com/genre-mapper)
- [The Ten Save the Cat! Story Genres — SceneOne](https://sceneone.app/blog/the-ten-save-the-cat-story-genres/)
- [Using SAVE THE CAT's Ten "Genres" — Script Magazine](https://scriptmag.com/columns/using-save-the-cats-ten-genres)
- [Genre Conventions: Must-Have Elements of Story — Story Grid](https://storygrid.com/genres-have-conventions-and-obligatory-scenes/)
- [Society Genre: Stories of Power and Impotence — Story Grid](https://storygrid.com/society-genre/)
- [Western and Eastern Genre: Stories of Subjugation and Freedom — Story Grid](https://storygrid.com/western-eastern-genre/)
- [Finding the Global Genre in Epic Fantasy Stories — Story Grid](https://storygrid.com/global-genre-epic-fantasy-stories/)
- [Worldbuilding in the Story Grid Methodology — Story Grid](https://storygrid.com/worldbuilding-in-the-story-grid-methodology/)
- [How to Write a Western: Morality, Myth, and the Open Range — Celtx](https://blog.celtx.com/how-to-write-a-western-movie-script/)
- [Revisionist Western — Wikipedia](https://en.wikipedia.org/wiki/Revisionist_Western)
- [Masterplots Theater: D is for Dystopia — WriteOnSisters](http://writeonsisters.com/writing-craft/masterplots-theater-d-is-for-dystopia/)
- [Planning Using the Three-Act Structure: Dystopian Novels — Duck Prints Press](https://duckprintspress.com/2022/08/28/planning-using-the-three-act-structure-dystopian-novels/)
- [What Makes Rebellion Believable in Dystopian Fiction — David Somerfleck](https://boldly.blue/rebellion-in-dystopian-fiction/)
- [How To Write A Dystopian Story: Our Guide — Jericho Writers](https://jerichowriters.com/how-to-write-a-dystopian-story/)
- [Ask an Editor: Worldbuilding in Speculative Fiction, Part II — Lee & Low Books](https://www.leeandlow.com/blog/ask-an-editor-worldbuilding-in-speculative-fiction-part-ii/)
- [The Trouble with Infodumps — The Darling Axe](https://darlingaxe.com/blogs/news/infodumps)
- [What is a Biopic? (Definition and Examples) — No Film School](https://nofilmschool.com/biopic)
- [The Accuracy of Biographical Films: Balancing Truth and Drama — Buddisystems](https://www.buddisystems.com/blog/the-accuracy-of-biographical-films-balancing-truth-and-drama)
- [Historical Drama vs. Biopic: Unraveling the Cinematic Distinction — Dark Skies](https://darkskiesfilm.com/what-is-the-difference-between-a-historical-drama-and-biopic/)
- [Indigenous Consultation and Engagement: A Primer — Alberta Society of Indigenous Heritage](https://asiheritage.ca/wp-content/uploads/2020/06/Indigenous-Consultation-and-Engagement-digital1.pdf)
- [Revisiting Indigenous "Encounters" with Colonialism, Past and Present — Organization of American Historians](https://www.oah.org/tah/rethinking-encounters/revisiting-indigenous-encounters-with-colonialism-past-and-present/)
- [Unlearning Colonial and Nation-State History in Documentary Film by and about Indigenous Peoples — alter/nativas](https://alternativas.osu.edu/en/issues/spring-6-2016/essays3/lehman.html)
