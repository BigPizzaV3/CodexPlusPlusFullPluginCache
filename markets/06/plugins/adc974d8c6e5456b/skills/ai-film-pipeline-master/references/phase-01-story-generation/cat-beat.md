# Beat Exchange, Action and Reaction

Category `beat`.

**Part 1 of 2.** 32 cards across what a beat is, its shape and weight, where beats sit, escalation and pattern, format and genre, working the draft, and the named failure modes.

A beat is one exchange of behaviour: an action, and the reaction it provokes. It is bigger than a sentence and smaller than a scene. `scene.value_turn` tells you whether the whole unit moved; a beat is the individual push that moved it. If you cannot point at the beat where the scene turned, the scene did not turn.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [What a Beat Is](#what-a-beat-is)
- [Shape, Length and Weight](#shape-length-and-weight)
- [Placement](#placement)
- [Escalation and Pattern](#escalation-and-pattern)
- [Format and Genre](#format-and-genre)
- [Working the Draft](#working-the-draft)
- [Failure Modes](#failure-modes)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## What a Beat Is

### The Action/Reaction Exchange

**Also called:** beat, behavioural beat, McKee beat, unit, bit, stimulus/response
**What it is:** One character does something — a line, a look, a move — and another character reacts to it. That pair is the beat. Robert McKee's phrasing is the standard: an exchange of behaviour in action/reaction.
**Effect on the audience:** It is the unit at which the audience actually feels story happening. Plot is understood afterwards; beats are experienced live, in the gap between what one person does and how the other takes it.
**Used for and where it works best:** Every dramatised scene. The craft rule: a beat is not complete until someone has been changed by it, however slightly. If A speaks and B answers with an unaffected line, you have two speeches, not a beat. Write the action, then write the landing — the flinch, the pause, the countermove — before moving on.
**Best in:** formats: screenplay, stage play, novel, short story, audio drama | genres: drama, thriller, romance, comedy, literary
**Avoid when:** Summary narration, montage, or any passage deliberately compressing weeks into a paragraph. Beats need real time; forcing them into summary produces a scene you did not intend to write.
**Example:**
> **Beat 1 — action:** He put the keys on the table between them.
> **Beat 1 — reaction:** She didn't look at the keys. She looked at his hand, at how long it stayed there.
> **Beat 2 — action:** "You can keep the car," he said.
> **Beat 2 — reaction:** "I know," she said, and picked the keys up, and the sound they made was louder than either of them expected.

**Yields to:** `scene.montage_time_compression` — Summary or montage compressing weeks into a paragraph.  
`beat.action_reaction_exchange`

---

### The Beat Change

**Also called:** beat shift, unit break, new beat, "new beat, new energy"
**What it is:** The point where the current exchange stops working and someone has to try something else. Motivation, tactic, mood or the physical situation changes, and a new beat begins.
**Effect on the audience:** A felt gear change. The audience does not name it, but they register the scene turning a corner, and their attention resets.
**Used for and where it works best:** Use it to segment a scene before you write it or to audit one you have written. The craft rule from acting practice: a new beat starts when the old approach fails. If nobody's approach has failed, you are still inside the same beat, no matter how many lines have passed. Mark the changes first; write the lines second.
**Best in:** formats: screenplay, stage play, novel, teleplay | genres: all
**Avoid when:** You are chopping beats by line count rather than by change. Beats are not paragraphs. A six-line speech can be one beat; a two-word answer can be three.
**Example:**
> INT. KITCHEN — NIGHT
>
> NADIA: You're home early.
> SAM: The meeting ended.
> NADIA: Ended, or you left?
> — *beat change: her tactic fails to get an answer, so she stops asking and starts doing* —
> She takes his coat off the hook and checks the pockets. He lets her.
> SAM: There's nothing in there.
> NADIA: I know.
> — *beat change: he stops defending and goes on the attack* —
> SAM: Then what are you looking for?

`beat.beat_change`

---

### Counting the Beats

**Also called:** beat count, beat breakdown, unit breakdown, beating out a scene
**What it is:** Going through a written scene and numbering each action/reaction exchange, so you can see how many distinct moves the scene actually contains.
**Effect on the audience:** Indirect — the audience never counts. But a scene with three beats stretched over four pages reads slow, and a scene with eleven beats in half a page reads frantic, and the count is where you diagnose both.
**Used for and where it works best:** On any scene that feels wrong and you cannot say why. The craft rule: number the beats in the margin, then read only your numbers and their verbs. If the list reads as a sensible sequence of moves, the scene works and the problem is line-level. If the list is repetitive or arbitrary, the problem is structural and rewriting the dialogue will not fix it.
**Best in:** formats: screenplay, stage play, novel | genres: all
**Avoid when:** Drafting hot. Counting mid-draft turns a scene into an accounting exercise. Count on the pass after.
**Example:**
> Marked-up margin of a two-page argument:
> 1. She asks about the money — he deflects with a joke
> 2. She asks again, flatly — he gives a partial number
> 3. She asks again — he gives a partial number
> 4. She names the real figure — he goes silent
> 5. She offers him a way out — he takes it too fast
> 6. She sees him take it too fast — she withdraws the offer
>
> Beats 2 and 3 are the same beat written twice. Cut one, and the scene moves.

`beat.beat_count`

---

### The Beat as Tactic

**Also called:** tactic beat, playable action, objective unit, intention change
**What it is:** Each beat is a character trying one specific tactic to get what they want. The beat lasts as long as the tactic does; when the tactic dies, the beat dies with it.
**Effect on the audience:** Characters read as intelligent and alive, because they adapt. A character who plays one tactic for a whole scene reads as a mouthpiece.
**Used for and where it works best:** Any scene where two people want incompatible things. The craft rule: each beat gets one transitive verb aimed at the other person — *shames*, *bribes*, *charms*, *threatens*, *begs* — and the next beat must use a different one. This is the same engine as `scene.tactic_change`, seen from inside the exchange instead of across the whole scene.
**Best in:** formats: stage play, screenplay, novel, audio drama | genres: drama, courtroom, thriller, romance, satire
**Avoid when:** The character genuinely has no agenda in the scene — a bystander, a witness to someone else's crisis. Forcing tactics onto them makes them scheming when you wanted them helpless.
**Example:**
> Beat 1 — *she flatters him*: "You were the only one in that room who understood it."
> Beat 2 — *flattery bounces; she shames him*: "Which is why watching you nod along was interesting."
> Beat 3 — *shame lands; he retreats, so she reassures*: "I'm not angry. I'd have nodded too."
> Beat 4 — *he relaxes; she strikes*: "Now tell me what they offered you."

`beat.tactic_beat`

---

### The Micro-Turn Inside a Beat

**Also called:** internal turn, beat polarity flip, the small reversal
**What it is:** A beat that does not end where it started — the reaction inverts the charge of the action, so a beat that opened positive closes negative or the reverse.
**Effect on the audience:** Constant small motion. The scene never sits still even when nothing plot-relevant occurs, because every exchange lands somewhere other than where it left.
**Used for and where it works best:** Long dialogue scenes that must hold without external event. The craft rule: give each beat a sign, plus or minus, from the point of view of one character, and never let two consecutive beats carry the same sign. `emo.emotional_turn` handles the arc of feeling across the scene; the micro-turn is that same movement at beat scale, and it is what makes the arc believable rather than announced.
**Best in:** formats: stage play, screenplay, novel, short story | genres: drama, romance, literary, chamber thriller
**Avoid when:** Action sequences at speed, or comic runs built on accumulation. Flipping the charge every beat there kills momentum.
**Example:**
> **+ to −:** "They said yes." She grinned. "They said yes to the smaller version."
> **− to +:** "It's gone." He held up the burnt corner. "Except this. Which is the only page they can't explain."

**Yields to:** `beat.action_sequence_beats` — Action at speed: change a condition, not the charge.  
`beat.micro_turn`

---

### Naming Beats with Transitive Verbs

**Also called:** verbing the beat, actioning, labelling units
**What it is:** Writing a single active verb beside each beat that names what one character does *to* the other — not how they feel, not what the beat is about.
**Effect on the audience:** None directly. This is a writer's and actor's instrument, and its effect on the page is that the beats stop blurring.
**Used for and where it works best:** Revision, and any scene you suspect is mush. The craft rule: the verb must be transitive and playable — *corners*, *disarms*, *deflects*, *surrenders*, *baits*. If the best verb you can find is "talks about" or "explains", the beat is not dramatic yet and no amount of dialogue polish will make it so.
**Best in:** formats: screenplay, stage play, novel | genres: all
**Avoid when:** The verb list becomes the goal. Writers who love their verb column sometimes write beats to fit a label instead of following the characters.
**Example:**
> Bad labels: *discusses the inheritance / feels guilty / explains the will*
> Rewritten as playable verbs: *baits him with the house / traps him into naming a price / forgives him, expensively*
>
> Same scene, three lines of dialogue changed. The second list can be acted; the first can only be summarised.

`beat.verb_naming`

---

## Shape, Length and Weight

### The Scene Beat Budget

**Also called:** beats per scene, scene density
**What it is:** The rough number of distinct exchanges a scene can carry before it either feels thin or feels crowded. There is no fixed figure; the useful figure is the one you set deliberately.
**Effect on the audience:** Pace. Few beats reads as weight and dread; many beats reads as friction and speed.
**Used for and where it works best:** Planning a sequence where several scenes sit side by side. The craft rule: most working dramatic scenes land between three and seven beats, and the ones outside that range should be outside it on purpose. Two beats means the scene is a single exchange and probably belongs inside another scene. Twelve beats usually means two scenes wearing one slugline.
**Best in:** formats: screenplay, teleplay, stage play, novel | genres: all
**Avoid when:** You start treating the range as a quota. A one-beat scene is legitimate when it is one hammer blow — a phone call that delivers a death and ends.
**Example:**
> Same information, two budgets.
>
> **Seven beats:** she arrives, he doesn't stand; she asks after his mother, he answers too briefly; she mentions the lawyer, he laughs; she doesn't laugh; he asks what she wants; she says nothing; he tells her.
> **Two beats:** she sits down. "Your mother left me the house." He puts down his fork and does not pick it up again.
>
> Both work. The first is a marriage; the second is a guillotine.

`beat.scene_beat_budget`

---

### Beat Length Variation

**Also called:** beat rhythm, varied beat duration, long-short-long
**What it is:** Deliberately making some beats several lines long and others a single word, so the scene has an uneven pulse.
**Effect on the audience:** Unpredictability. Uniform beat length is soporific even when the content is tense; the reader's ear predicts the shape of the next exchange and stops listening.
**Used for and where it works best:** Any scene longer than a page. The craft rule: put your shortest beat immediately after your longest. The compression reads as a slap. This is beat-level rhythm, distinct from sentence-level rhythm, and a scene can be perfect at the sentence and still monotonous here.
**Best in:** formats: novel, screenplay, stage play, audio drama | genres: all, thriller, comedy
**Avoid when:** Ritual or ceremonial scenes where the evenness is the point — a liturgy, an interrogation designed to grind, a formal negotiation.
**Example:**
> He explained the schedule. The truck came Tuesdays, always Tuesdays, and the driver had a key to the side gate because of the dogs, and the dogs knew him, and that was the whole system and it had worked for eleven years and nobody had ever once —
>
> "Tuesday," she said.
>
> He stopped.

**Yields to:** `seq.ritual_sequence` — Ritual or ceremony where the evenness is the point.  
`beat.length_variation`

---

### The Held Beat

**Also called:** the hold, sustained beat, letting it sit, the long moment
**What it is:** Refusing to move to the next beat when the reader expects you to — holding inside a single exchange past its natural length.
**Effect on the audience:** Pressure. Held long enough, discomfort becomes the content; the audience starts supplying meaning to fill the space you left.
**Used for and where it works best:** The single most important exchange in a scene, and never more than one per scene. The craft rule: a hold only works if the beat has already landed. Holding a beat nobody cares about is just slowness. Hold after the revelation, not before it.
**Best in:** formats: screenplay, stage play, novel, literary short story | genres: drama, horror, literary, war
**Avoid when:** Comedy at pace, procedural sequences, or anywhere the reader is still assembling information. A hold on an unclear beat reads as a mistake in the writing.
**Example:**
> "Say it again," she said.
>
> He didn't.
>
> She waited. The kettle finished and clicked off. Somewhere under the floor the pipes moved and were still. She kept waiting, and the not-saying went on so long it stopped being a refusal and became an answer.
>
> "All right," she said.

**Yields to:** `beat.comic_third` — Comedy at pace, where hesitation kills the run.  
`beat.held_beat`

---

### The Beat of Silence

**Also called:** the pause, the non-answer, the empty beat, the dropped reply
**What it is:** A beat whose reaction half is nothing — no line, no gesture worth naming. The silence is the reaction, and it carries more than a line would.
**Effect on the audience:** The audience does the work. They read the silence as refusal, or shame, or contempt, according to what the scene has taught them, and their reading feels like their own discovery.
**Used for and where it works best:** After a question that cannot be answered honestly and cheaply. The craft rule: a silent beat needs a clock — something in the scene marking that time is passing, or the reader will not register duration. See also `dial.silence_as_reply` for the dialogue-level technique; here the interest is that the silence still occupies a full beat of the scene's structure and must be counted as one.
**Best in:** formats: screenplay, stage play, novel, audio drama | genres: drama, thriller, romance, literary
**Avoid when:** Every second exchange is a silence. Silence is only loud against speech; a scene of pauses is a scene of nothing.
**Example:**
> "Did you know?" she said.
>
> The waiter came, filled both glasses, asked if everything was all right, was told it was, and went away.
>
> "Did you know?"

`beat.silent_beat`

---

### The Physical Beat

**Also called:** business, stage business, the body beat, blocking beat
**What it is:** A beat carried entirely by physical change — someone enters, someone stands, the light goes out, a chair is moved — and by the others reacting to it.
**Effect on the audience:** It breaks the trance of talking heads and reminds the reader that the scene has a room, bodies, and gravity.
**Used for and where it works best:** Scenes that are going verbal for too long, and any moment where a character's body should betray what their words deny. The craft rule: the physical act must change the balance of the scene, not decorate it. Standing up is a beat when it ends the conversation; it is furniture when it doesn't. `char.stress_tell` is the involuntary version — the body leaking under pressure — while the physical beat is usually chosen.
**Best in:** formats: stage play, screenplay, novel | genres: all
**Avoid when:** You are using movement to avoid writing the hard line. A character who crosses to the window, looks out, turns back, and crosses to the table has performed no beats at all.
**Example:**
> He was still explaining the contract when she stood, picked up her coat, and sat back down with it on her lap.
>
> He stopped explaining the contract.

**Yields to:** `char.stress_tell` — The body leaking involuntarily rather than moving by choice.  
`beat.physical_beat`

---

### The Beat That Lands on an Object

**Also called:** object beat, the prop turn, displaced beat, the thing between them
**What it is:** An exchange where the reaction is directed at a physical object rather than at the other person — the object absorbs the emotion and becomes the scene's meter.
**Effect on the audience:** Intensity without declaration. Watching someone fold a napkin into quarters while being told their father is dying is worse than watching them cry.
**Used for and where it works best:** Scenes between people who cannot say what they feel — family, subordinates, the recently bereaved, anyone bound by manners. The craft rule: introduce the object early and neutrally, so that when the beat lands on it the reader already knows its normal state and can measure the change against it.
**Best in:** formats: novel, short story, screenplay, stage play | genres: literary, drama, domestic, war, period
**Avoid when:** The object has no prior existence in the scene. Producing a meaningful object at the moment of meaning is a writer's trick, and it shows.
**Example:**
> She had been peeling the label off the bottle since he sat down — one long strip, patiently, the way she did everything.
>
> "They're not reopening it," he said. "There's no evidence left to reopen it with."
>
> The strip tore. She looked at the torn end for a while, then started again lower down, on the part that was still whole.

`beat.object_beat`

---

## Placement

### The Reaction Beat

**Also called:** the response half, the take, the landing, reaction shot
**What it is:** The second half of the exchange — how the receiving character absorbs what just happened. It is the half writers habitually skip.
**Effect on the audience:** It tells them how to feel. The action supplies the event; the reaction supplies the size of the event. Without it the audience has facts and no scale.
**Used for and where it works best:** After every significant action, and especially after the scene's worst news. The craft rule, and it is the most useful rule in this category: the reaction beat is almost always cut one line too early. Writers reach the reaction, write a single gesture, and hurry to the next line of dialogue. Give the reaction its own full beat — action, absorption, and only then the reply. `scene.reaction_dilemma_decision` is the scene-scale version of the same instinct; at beat scale it costs you two lines and buys the whole moment.
**Best in:** formats: screenplay, novel, stage play, teleplay | genres: all
**Avoid when:** Farce and rapid comic exchange, where the joke is that nobody is absorbing anything. Also in deliberate shock cuts, where denying the reaction is the effect.
**Example:**
> **Cut too early:**
> "Your brother signed it too."
> She blinked. "When?"
>
> **Given its beat:**
> "Your brother signed it too."
> She looked at the page, at the two names, at the space between the two names where the date should have been and wasn't. Somewhere behind her a printer started and she let it finish.
> "When?"

**Yields to:** `beat.interrupted_beat` — Deliberate shock cut that denies the reaction.  
`beat.reaction_beat`

---

### The Beat After the Line

**Also called:** the tail, post-line beat, the afterward
**What it is:** A short beat placed immediately after a strong line — usually a small physical or observational moment — instead of another line of dialogue.
**Effect on the audience:** It makes the line land. A powerful line answered instantly by another line is stepped on; the reader never gets to hear it.
**Used for and where it works best:** After the best line in the scene, and after any line meant to be quoted back later. The craft rule: the tail must be small and concrete, and it must not comment on the line. "That was cruel, and he knew it" destroys the line. "He put his cup down in the saucer without any noise at all" protects it.
**Best in:** formats: novel, short story, screenplay, stage play | genres: all
**Avoid when:** Overlapping dialogue scenes and argument at speed, where the point is that nobody gets a tail — see `dial.interruption` for the opposite instrument.
**Example:**
> "I never asked you to stay."
>
> Outside, a car door. Voices, then not. The radiator ticked twice and settled.
>
> "No," he said. "You didn't."

**Yields to:** `dial.interruption` — Overlapping dialogue at speed; nobody gets a tail.  
`beat.beat_after_line`

---

### The Beat Before the Exit

**Also called:** the exit beat, door beat, the turn at the threshold, button
**What it is:** The last beat before a character leaves the scene — one final exchange placed at the door, after the conversation is apparently finished.
**Effect on the audience:** It decides what the scene is remembered as. Audiences retain the last exchange far out of proportion to its length.
**Used for and where it works best:** Any scene where someone departs, which is most scenes. The craft rule: the exit beat should reverse or complicate what the scene appeared to settle, not summarise it. If the exit line restates the scene's point, cut it and let them leave in silence. A scene that has already achieved its `scene.value_turn` and then adds a summarising exit beat has turned twice and landed nowhere.
**Best in:** formats: screenplay, teleplay, stage play, novel | genres: drama, thriller, comedy, crime
**Avoid when:** The scene's power is in the abruptness of the departure — a walk-out, a hang-up, a death. Adding a door beat there is a writer refusing to let a scene end.
**Example:**
> **Summarising, cut it:**
> She opened the door. "So that's it, then. Twenty years."
>
> **Complicating, keep it:**
> She opened the door, and stopped, and said without turning round: "The dog's yours. I never liked him."
> "You bought him."
> "I bought him for you," she said, and went.

**Yields to:** `beat.scene_handoff` — Abrupt departure: design the join, not a door beat.  
`beat.exit_beat`

---

### The Interrupted Beat

**Also called:** broken beat, aborted exchange, the beat that never closes
**What it is:** An action whose reaction never arrives, because something cuts in — another character, an event, a scene break — leaving the exchange structurally open.
**Effect on the audience:** Unease that persists past the scene. An unclosed beat stays live in the reader's head the way an unresolved chord does.
**Used for and where it works best:** Just before a hard cut, and in scenes with three or more people where the third party's job is to prevent an exchange from completing. The craft rule: the reader must clearly register that a reaction was owed. If they do not know what was about to happen, the interruption reads as sloppiness, not suspense. Pay the beat off later or make the non-payment the point — do not simply forget it.
**Best in:** formats: screenplay, teleplay, novel, stage play | genres: thriller, drama, farce, crime
**Avoid when:** You are using interruption to escape a line you cannot write. Readers can tell the difference between a withheld answer and an absent one.
**Example:**
> "Before you sign it, there's something about the second year that you should —"
>
> The door opened. His daughter came in with the cake, and everyone sang, and the pen stayed where it was on the table between them, and nobody mentioned the second year again that night.

`beat.interrupted_beat`

---

### Subtext Carried Across a Beat

**Also called:** beat subtext, the line under the exchange, double transaction
**What it is:** The surface exchange is about one thing and the real exchange is about another, and the beat change happens on the hidden level while the surface conversation continues undisturbed.
**Effect on the audience:** The pleasure of reading two scenes at once, and the flattery of being trusted to do it.
**Used for and where it works best:** Negotiations, flirtation, family meals, any scene where the true subject is forbidden. The craft rule: the surface conversation must be genuinely functional — a real argument about a real kitchen renovation — or the subtext has nothing to hide behind and becomes coy. Track the hidden beats separately in your notes; the surface beats can look almost static while the real ones turn twice.
**Best in:** formats: stage play, screenplay, novel, short story | genres: drama, romance, literary, espionage, satire
**Avoid when:** The reader lacks the context to decode it. Subtext is only subtext if the audience holds the key; otherwise it is a scene about a kitchen.
**Example:**
> **Surface:** the sale of a boat. **Under:** whether he is going to leave.
>
> "She needs a new keel before spring."
> "So sell her in autumn."
> "In autumn she's worth nothing."
> "Then don't sell her."
> "I didn't say I was selling her."
> "No," she said. "You've been not-saying it since June."

`beat.subtext_carry`

---

## Escalation and Pattern

### The Escalation Step

**Also called:** raising the beat, the ratchet, stakes step
**What it is:** Each successive beat costs the characters more than the last — a larger admission, a worse risk, a more expensive tactic — so the scene climbs instead of circling.
**Effect on the audience:** Forward pull. The audience senses a ceiling being approached and wants to see it hit.
**Used for and where it works best:** Confrontation scenes, and any scene built on `scene.goal_conflict_disaster`. The craft rule: something must be spent in each beat that cannot be recovered — a secret told, a threat made that cannot be unmade, a person named. If a beat costs nothing, the scene has paused even if the volume went up.
**Best in:** formats: screenplay, stage play, novel, teleplay | genres: drama, thriller, crime, courtroom, war
**Avoid when:** The scene is a plateau by design — the calm before, the aftermath, the tender middle. Not every scene should climb, and relentless escalation flattens as surely as none.
**Example:**
> 1. "You were seen at the yard." — a place. Deniable.
> 2. "At eleven, with Farid." — a time and a name. Less deniable.
> 3. "Farid's already made a statement." — a betrayal. Cannot be unmade.
> 4. "So has your wife." — the last thing he had. Nothing left to spend.

**Yields to:** `seq.breather_sequence` — The scene is a plateau by design.  
`beat.escalation_step`

---

### The Beat Rhyme

**Also called:** beat callback, repeated gesture with a difference, echo beat
**What it is:** A beat deliberately built to repeat an earlier beat's shape — the same action, the same words, the same object — while the circumstances have changed underneath it.
**Effect on the audience:** Recognition, then reappraisal. The second instance measures exactly how far things have moved, without a word of explanation.
**Used for and where it works best:** Across a script or novel, at the two ends of a relationship arc. The craft rule: repeat the form precisely and change one element only. Two changes and the audience reads it as a new beat rather than a rhyme; nothing changed and it reads as an error.
**Best in:** formats: novel, screenplay, teleplay, stage play | genres: drama, romance, literary, tragedy
**Avoid when:** The gap between the two instances is short enough that it reads as repetition rather than rhyme, or when the first instance was too minor to be remembered.
**Example:**
> **Page 12:** He held the door. She went through without looking at him, because she always did, because it was nothing.
> **Page 240:** He held the door. She stopped in it, and looked at him for a long time, and it was not nothing.

`beat.beat_rhyme`

---

### The Redirected Beat

**Also called:** the deflected reaction, wrong-target beat, reacting sideways
**What it is:** A character reacts to an action, but aims the reaction at a third party or at themselves instead of at the person who caused it.
**Effect on the audience:** A clean read on power. Who you are allowed to be angry at tells the audience the whole hierarchy of the room in one beat.
**Used for and where it works best:** Workplaces, armies, families, any ensemble scene with rank. The craft rule: the redirected reaction must be disproportionate to its new target — the shouting-at-the-waiter principle — or the audience will not notice it has been displaced.
**Best in:** formats: screenplay, stage play, novel, teleplay | genres: drama, workplace, war, satire, domestic
**Avoid when:** Two-handers with equal power, where there is nowhere to deflect to and the deflection would read as evasion by the writer.
**Example:**
> The director said the campaign was being shelved, and thanked them for their long hours, and left.
>
> Rania turned on the junior. "Whose idea was the yellow? I asked three times whose idea was the yellow."
>
> The junior said it was hers. It wasn't. Everyone in the room knew it wasn't.

**Yields to:** `beat.object_beat` — Two-hander of equal power, no third party to deflect toward.  
`beat.redirect`

---

### The Comic Third Beat

**Also called:** rule of three, the topper, triple, set-set-twist
**What it is:** Two beats establish a pattern and the third breaks it. The break is the joke; the first two are the price of the joke.
**Effect on the audience:** Laughter, which is what surprise feels like when there is no danger. The audience must have privately predicted the third beat for the twist to pay.
**Used for and where it works best:** Comic runs, character introductions, and any place a repeated action needs a button. The craft rule: the second beat must be near-identical to the first, and it must come fast. Hesitation between beats one and two lets the audience get ahead of you, and the third then lands on people who are already waiting for it.
**Best in:** formats: screenplay, teleplay, stage play, novel, sketch | genres: comedy, satire, farce, children's, romcom
**Avoid when:** In drama the same three-part structure exists but escalates rather than twists — the third instance should be heavier, not funnier. Using a comic topper in a dramatic run reads as the writer breaking character.
**Example:**
> He checked the gas. He checked the door. He checked the gas again.
>
> He got in the car, drove four streets, came back, and checked the door.

**Yields to:** `beat.escalation_step` — In drama the third instance escalates rather than twists.  
`beat.comic_third`

---

## Format and Genre

### Beats in an Action Sequence

**Also called:** action beats, fight beats, set-piece beats
**What it is:** Breaking a fight, chase or heist into discrete exchanges where each beat changes a condition — distance, weapon, footing, an exit, an injury — rather than listing blows.
**Effect on the audience:** Comprehension, which is the scarce resource in action. An audience that can follow the geography feels tension; an audience that cannot feels noise.
**Used for and where it works best:** Every physical sequence longer than four lines. The craft rule: each beat must create the conditions for the next. A punch that changes nothing is not a beat. Track one variable per beat — the knife is gone, the door is blocked, his left arm stops working — and the sequence will read even at speed. Reversals are what make it a scene rather than choreography.
**Best in:** formats: screenplay, novel, comics, teleplay | genres: action, thriller, war, crime, fantasy, adventure
**Avoid when:** Deliberate chaos — a riot, a bombing, a panic seen from inside. There the incomprehension is the effect, and beat-clean staging works against it.
**Example:**
> **Choreography, unreadable:** He punched, she blocked, he punched again, she ducked and swung, he caught her arm, she twisted free and kicked.
>
> **Beats, each changing a condition:** She got the table between them. He went round it, which cost him three seconds and gave her the drawer. The drawer had no knife in it — he had taken the knives out on Tuesday, and she understood on Tuesday now, far too late, with the drawer open in her hand.

**Yields to:** `char.panic_behaviour` — Deliberate chaos or panic seen from inside.  
`beat.action_sequence_beats`

---

### Beats in Prose Versus Screenplay

**Also called:** the two beat traditions, medium-specific beating
**What it is:** The same unit, made of different materials. In screenplay a beat is external and visible — line, look, move — because the camera can only photograph behaviour. In prose the reaction half may be entirely interior, and interiority counts as a full beat.
**Effect on the audience:** Prose can make the smallest event enormous, because the reaction lives inside the head. Screenplay must externalise or lose it.
**Used for and where it works best:** Adaptation in either direction, and for any prose writer who learned structure from screenwriting books. The craft rule: when adapting prose to script, every interior reaction beat must be converted into something photographable or given to another character to notice; when adapting script to prose, resist filling every silence with thought, because the withheld interior is often what made the beat work.
**Best in:** formats: novel, screenplay, short story, teleplay | genres: all
**Avoid when:** Treating one tradition's rules as universal. A novel written in pure screenplay beats reads thin; a script written in prose beats is unshootable.
**Example:**
> **Prose:** He said the flight was at six. Six meant she had lied about the meeting, and about last Thursday, and probably about her sister, and Hamid understood all of it in the time it took to set down the glass. "Six," he said. "Good."
>
> **Script:** HAMID sets the glass down. Sets it down again, a half inch to the left, squaring it with nothing.
> HAMID: Six. Good.

`beat.prose_vs_screenplay`

---

### Beat Notation on the Page

**Also called:** (beat), the beat parenthetical, marking pauses, scene margin notation
**What it is:** How writers physically indicate beats — the `(beat)` parenthetical inside dialogue, double spacing, a line of white space, or numbered margin notes in a working copy.
**Effect on the audience:** On a reader of the script, rhythm. On an audience, nothing directly — but a director and actor who read the intended rhythm will produce it.
**Used for and where it works best:** Sparingly, where a pause carries meaning that the line alone cannot convey. The craft rule the industry has converged on: `(beat)` is the weakest available option, because it tells an actor to pause without telling anyone why. Replace it with the action that fills the pause. Keep parentheticals rare enough that their appearance signals importance. Margin beat numbers belong in your working copy only and never go out with the draft.
**Best in:** formats: screenplay, teleplay, stage play | genres: all
**Avoid when:** You are using `(beat)` as punctuation. Three on a page and directors start ignoring all of them, including the one that mattered.
**Example:**
> **Weak:**
> ELIAS
> (beat)
> I'll do it.
>
> **Better:**
> ELIAS reads the name on the folder. Reads it again. Closes the folder.
> ELIAS
> I'll do it.

**Yields to:** `beat.notation_traditions` — Outside the US market, or in translation.  
`beat.notation`

---

### Beat Density in Prose Dialogue

**Also called:** beat spacing, attribution beats, the every-line problem
**What it is:** How often a spoken line is accompanied by a physical or interior beat rather than standing alone or taking a plain tag.
**Effect on the audience:** Tempo. Dense beats slow a conversation to a crawl and make it feel weighted; sparse beats make it feel fast and light.
**Used for and where it works best:** Any prose conversation over half a page. The craft rule: beat the opening exchange so the reader can see the room and the bodies, then strip beats out as the conversation accelerates, then bring one back at the turn — the returning beat marks the turn without announcing it. Note the terminology overlap: `dial.action_beat` covers the same device viewed as dialogue attribution; here the interest is the rate, not the individual instance.
**Best in:** formats: novel, short story, memoir | genres: all prose
**Avoid when:** Every line has a gesture attached. Nodding, smiling, sighing and looking away after each speech is the commonest symptom of an inexperienced prose scene, and it makes characters look like they are twitching.
**Example:**
> **Over-beaten:** "I'm not going," she said, folding her arms. He sighed. "You are," he said, running a hand through his hair. She shook her head. "No," she said, looking away.
>
> **Rated:** She folded her arms. "I'm not going."
> "You are."
> "No."
> "Nadia."
> She looked away, and that was the first thing she had done all evening that he recognised.

`beat.prose_beat_density`

---

## Working the Draft

### The Beat-Marking Pass

**Also called:** beating out the draft, margin pass, unit audit
**What it is:** A revision pass where you read a finished scene and mark every beat boundary and its verb, without changing a word, purely to see the scene's skeleton.
**Effect on the audience:** None. This is diagnosis, and its value is that it finds problems dialogue-polishing cannot.
**Used for and where it works best:** On any scene that readers call "slow" or "fine" — fine being the worse report. The craft rule: read the verb list alone, out of context. Three symptoms are visible instantly — two adjacent identical verbs, a verb you could only write as "talks about", and a scene whose last verb is the same as its first, meaning nobody moved. Against that list check whether the scene delivers a `scene.value_turn` at all, and at which beat.
**Best in:** formats: screenplay, novel, stage play, teleplay | genres: all
**Avoid when:** First drafts. Beat-marking a draft that is still finding itself will convince you to cut material you have not yet understood.
**Example:**
> Verb list from a five-beat scene that readers found slow:
> *deflects / deflects / deflects / concedes / deflects*
>
> Three deflections is one deflection written three times, and the scene ends where it began. Fix: cut two, and make the final beat cost him the thing he was protecting.

`beat.beat_marking_pass`

---

### Scene Beat Sheet Versus Story Beat Sheet

**Also called:** micro beats versus macro beats, the two beat sheets, terminology collision
**What it is:** Two different professional meanings of "beat sheet". The story beat sheet lists the major structural events of a whole film or novel — fifteen or so, each possibly spanning several scenes. The scene beat sheet lists the action/reaction exchanges inside one scene. They share a word and nothing else.
**Effect on the audience:** Indirect, but the confusion causes real damage: writers apply structural templates at scene level and produce scenes with an inciting incident and a dark night of the soul, which is absurd at that scale.
**Used for and where it works best:** Whenever you are working with collaborators or reading craft books. The craft rule: state which sheet you mean before the conversation starts. `struct.mckee_beat` and `struct.mckee_scene` sit at the structural end; everything in this category sits at the exchange end. A story beat is a *what happened*; a scene beat is a *what was done to whom*.
**Best in:** formats: screenplay, teleplay, novel | genres: all
**Avoid when:** Never avoid the distinction — but do avoid pedantry about it in a room. Ask which one they mean and move on.
**Example:**
> **Story beat, one line covering four scenes:** *Catalyst — the father's will is read and Hamid learns the house is not his.*
>
> **Scene beats inside the reading of the will:** solicitor stalls / Hamid presses / solicitor names the sister / Hamid laughs / nobody laughs with him / Hamid asks to see the signature.
>
> Same event, two scales, two documents.

`beat.scene_sheet_vs_story_sheet`

---

## Failure Modes

### The Dead Beat

**Also called:** the null exchange, the flat beat
**This is a named failure, not a recommendation.**
**What it is:** An exchange in which nothing changes — an action is performed, a reaction is given, and the scene's balance, information and emotional state are identical afterwards.
**Effect on the audience:** Attention drops. They cannot say why, because nothing bad happened; nothing happened at all.
**Used for and where it works best:** Diagnosis only. Find dead beats by asking of each one: what is different now? If the honest answer is "they have said hello", cut it or load it. Greetings, arrivals and pleasantries are where they cluster, because they are the beats writers write on autopilot.
**Best in:** formats: — | genres: —
**Avoid when:** Note the one legitimate use: a deliberately dead beat placed between two loaded ones as a rest. That is a choice, and it is exactly one beat long.
**Example:**
> **Dead:**
> "Coffee?"
> "Please."
> "Milk?"
> "Just black."
> He made the coffee. She sat down.
>
> **Loaded, same furniture:**
> "Coffee?"
> "Please."
> He reached for the second mug — the one with the chip, the one that had been hers — and stopped, and took down a clean one instead.
> "Black," she said. "I still take it black."

**Yields to:** `beat.object_beat` — Loading the empty exchange onto an already-present object.  
`beat.dead_beat`

---

### The Repeated Beat

**Also called:** the stuck beat, beat loop, arguing in a circle
**This is a named failure, not a recommendation.**
**What it is:** The same tactic played twice or more in a row with different words, so the scene circles instead of advancing. It is the single commonest structural fault in dialogue scenes.
**Effect on the audience:** Impatience, and a suspicion that the characters are stupid. Real people escalate or withdraw; only badly written ones ask the same question four ways.
**Used for and where it works best:** Diagnosis. Spot it in a `beat.beat_marking_pass` — two identical verbs adjacent in the list. The fix is almost never to rewrite both; it is to cut one and let the surviving beat carry the weight.
**Best in:** formats: — | genres: —
**Avoid when:** Deliberate repetition is a different device. Interrogation scenes and obsessive characters repeat on purpose, and there the repetition must be flagged as strategy — see `dial.question_control` — and must escalate in pressure even when the words are identical.
**Example:**
> **Looped:**
> "Where were you?" / "Out." / "Out where?" / "Just out." / "I'm asking you where." / "And I'm telling you, out."
>
> **Fixed — the second attempt changes tactic:**
> "Where were you?" / "Out."
> She put his phone on the table, face up, still showing the map.
> "Try again."

**Yields to:** `beat.tactic_beat` — The repair: the second attempt must change tactic.  
`beat.repeated_beat`

---

### The Clipped Reaction

**Also called:** the swallowed beat, rushing the landing, no-take
**This is a named failure, not a recommendation.**
**What it is:** The reaction half of the beat is truncated to a single reflex — a blink, a swallow, a "What?" — and the scene moves on before the audience has absorbed the action.
**Effect on the audience:** Emotional under-delivery. The plot lands, the feeling does not, and the reader concludes the event was minor because the text treated it as minor.
**Used for and where it works best:** Diagnosis. It is epidemic around revelations, because writers are excited to get to the next revelation. Test: find the worst news in your draft and count the lines between it and the next line of dialogue. If the answer is under two, you have probably clipped it.
**Best in:** formats: — | genres: —
**Avoid when:** As with all these, the deliberate version exists — the shock cut that denies reaction on purpose. The difference is whether the denial is paid for later.
**Example:**
> **Clipped:** "He's dead." She gasped. "How?"
>
> **Paid:** "He's dead."
> She heard it and then, a moment later, heard it again, the way you hear your own name shouted across a station. Her hand was still on the kettle. The kettle was still hot. She took her hand off the kettle.
> "How?"

**Yields to:** `beat.reaction_beat` — The repair: give the reaction its own full beat.  
`beat.clipped_reaction`

---

### The Choreography List

**Also called:** the blow-by-blow, the recap fight, beatless action
**This is a named failure, not a recommendation.**
**What it is:** An action sequence written as a sequence of moves rather than exchanges — punched, blocked, ducked, swung — with no beat changing any condition of the fight.
**Effect on the audience:** Boredom during violence, which is the hardest boredom to forgive. Nothing is at stake beat to beat because nothing is ever different.
**Used for and where it works best:** Diagnosis. Test: delete any one sentence from the sequence. If nothing downstream breaks, it was not a beat. Repeat until only load-bearing beats remain, then rebuild the gaps as reversals — advantage flipping, a tactic revealed, a body failing.
**Best in:** formats: — | genres: —
**Avoid when:** Never a recommendation, though brief flurries of unspecified violence are legitimate as connective tissue between real beats. The fault is a whole sequence made of them.
**Example:**
> **List:** He swung. She dodged. He swung again. She caught his wrist. He pulled free. She stepped back. He came forward.
>
> **Beats:** He swung and hit the shelf instead, and the shelf came down, and now there was glass on the floor and she was the only one wearing shoes.

**Yields to:** `beat.action_sequence_beats` — The repair: rebuild as beats that change conditions.  
`beat.choreography_list`

---

### Beat Parenthetical Spam

**Also called:** (beat) disease, pause-stuffing, directing from the page
**This is a named failure, not a recommendation.**
**What it is:** Using `(beat)` repeatedly to manufacture significance, marking pauses that the line already implies or that the actor would find without being told.
**Effect on the audience:** On a reader, irritation and a sense of being managed. On production, the reverse of the intention — once the parentheticals are everywhere, directors and actors stop reading them entirely.
**Used for and where it works best:** Diagnosis. Count them: more than two or three in a ten-page scene is a symptom. Most can be deleted with no loss; the ones that cannot should become an action line describing what fills the pause.
**Best in:** formats: — | genres: —
**Avoid when:** Note the legitimate minority case — a pause that inverts a line's meaning and would otherwise be misread. That one earns its parenthetical, and it survives precisely because the others were cut.
**Example:**
> **Spam:**
> MAYA
> (beat)
> I read it.
> (beat)
> All of it.
> (beat)
> Twice.
>
> **Cut to one, and that one earns it:**
> MAYA
> I read it. All of it.
> (beat)
> Twice.

**Yields to:** `beat.notation` — The repair: an action line that fills the pause.  
`beat.beat_spam`

---

## Coverage

Covered here: the action/reaction definition and beat change; counting and naming beats; beats as tactics and the micro-turn; scene beat budget and length variation; the held, silent, physical and object beats; the reaction beat, the beat after the line, the exit beat, the interrupted beat; subtext across a beat; escalation, beat rhyme, redirection, the comic third; beats in action sequences, in prose versus screenplay, on the page as notation, and at density in prose dialogue; the beat-marking diagnostic pass and the scene-versus-story beat sheet distinction; five named failure modes.

Remaining for Part 2: beats in ensemble and three-plus-handed scenes; beats across a phone call and across mediated communication; the off-screen beat; beats in voiceover and narration; beats in verse, song lyric and musical numbers; beats in comics panels and in interactive/branching writing; beat handoff between scenes (the out-beat / in-beat pair); beats under time pressure and in real-time scenes; beats in solo scenes with no second character; beats between a character and an environment; comic beat forms beyond the third (the topper on the topper, the runner, the callback at distance); the beat of a decision; beats in exposition-carrying scenes; rehearsal-room and table-read methods for testing beats; beat notation across international script traditions; and the remaining failure modes — the pre-empted beat, the announced beat, the beat given to the wrong character, and beat symmetry fatigue.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Accessed 2026-09-17.

- [What Is a Beat in Screenwriting? — SoCreate](https://www.socreate.it/en/blogs/screenwriting/what-is-a-beat-in-screenwriting)
- [How to Use a Beat in a Screenplay — SoCreate](https://www.socreate.it/en/blogs/screenwriting/how-to-use-a-beat-in-a-screenplay)
- [Understanding Beats Analysis for Scripts — Dramatics Magazine](https://dramatics.org/beat-analysis/)
- [What Are "Beats" in Acting? How to Level Up Your Script Analysis — Backstage](https://www.backstage.com/magazine/article/what-are-beats-in-acting-76101/)
- [Script Analysis: How to Get the Most Out of a Scene — StageMilk](https://www.stagemilk.com/script-analysis/)
- [Use Beats to Move Characters within Scenes — Storm Writing School](https://stormwritingschool.com/beats/)
- [What Is a Beat, Anyway? — Storm Writing School](https://stormwritingschool.com/beats-disambiguation/)
- [Learn About Beats in Screenwriting: How to Create a Beat Sheet — MasterClass](https://www.masterclass.com/articles/what-is-a-beat-in-screenwriting)
- [What Does a Beat Mean in a Script? — Kino Lime](https://blog.kinolime.com/articles/what-does-a-beat-mean-in-a-script)
- [Unit of action — Wikipedia](https://en.wikipedia.org/wiki/Unit_of_action)
- [Units and Objectives (Stanislavski) — Student Theatre](https://sites.google.com/view/b4-b6studenttheatre/stanislavski/stanislavski-methods/units-and-objectives)
- [Using Beats to Improve Dialogue and Action in Scenes — Writer's Digest](https://www.writersdigest.com/write-better-fiction/using-beats-to-improve-dialogue-and-action-in-scenes)
- [On the Beaten Path: How to Use Beats in Fiction — The Darling Axe](https://darlingaxe.com/blogs/news/beats)
- [Action Beats, Dialogue Beats and Beat Variation — Katherine Cowley](https://www.katherinecowley.com/blog/action-beats-dialogue-beats-and-beat-variation/)
- [What Are Action Beats and How Can You Use Them in Fiction Writing? — Louise Harnby](https://www.louiseharnbyproofreader.com/blog/what-are-action-beats-and-how-can-you-use-them-in-fiction-writing)
- [Screenwriter's Guide to Using Parentheticals in Screenplays — Final Draft](https://www.finaldraft.com/blog/lets-talk-about-parentheticals)
- [Parentheticals in Scripts: Definition, Examples, and Advice — Backstage](https://www.backstage.com/magazine/article/parentheticals-screenplay-examples-advice-76523/)
- [Screenplay Format Guide: Parentheticals — Story Sense](https://www.storysense.com/format/parentheticals.htm)
- [What is the "Rule of Three" in Screenwriting? — No Film School](https://nofilmschool.com/rule-of-the-three)
- [Rule of three (writing) — Wikipedia](https://en.wikipedia.org/wiki/Rule_of_three_(writing))
- [How to Write a Fight Scene in a Screenplay — Final Draft](https://www.finaldraft.com/blog/how-to-write-a-fight-scene-in-a-screenplay)
- [Five Principles For Writing Kick Ass Action Scenes — Career Authors](https://careerauthors.com/five-principles-for-writing-kick-ass-action-scenes/)
- [Save the Cat Beat Sheet Explained — StudioBinder](https://www.studiobinder.com/blog/save-the-cat-beat-sheet/)
- [Beat Sheets — Save the Cat!](https://savethecat.com/beat-sheets)
