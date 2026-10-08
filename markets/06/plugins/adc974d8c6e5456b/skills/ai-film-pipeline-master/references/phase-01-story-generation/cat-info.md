# Information Control, Reveal and Withholding

Category `info`. The management of what the audience knows, when, and relative to whom — as distinct from how a line of dialogue carries a fact (`cat-dial.md`) or how a scene is built (`cat-scene.md`).

**Part 1 of 4.** 32 cards across the three information positions, planting and payoff, misdirection and the false trail, narration and point of view, reveal staging, fairness and the cheat, and reveals in serial and short-form.

Every card here answers one question: *who knows this, and who is watching them not know it?* Get that wrong and no amount of good dialogue rescues the scene.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The Three Positions](#the-three-positions)
- [Plant, Payoff and Foreshadowing](#plant-payoff-and-foreshadowing)
- [Misdirection and the False Trail](#misdirection-and-the-false-trail)
- [Narration, Point of View and Inference](#narration-point-of-view-and-inference)
- [Staging the Reveal](#staging-the-reveal)
- [Fairness and the Cheat](#fairness-and-the-cheat)
- [Serial and Short-Form Reveals](#serial-and-short-form-reveals)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## The Three Positions

### Dramatic Irony

**Also called:** audience-ahead position, superior position, the bomb under the table, tragic irony
**What it is:** The audience holds a fact one or more characters do not, then watches those characters act on an incomplete picture of their own situation. Hitchcock's formulation: show the audience the bomb under the table and four minutes of small talk becomes unbearable.
**Effect on the audience:** Dread plus helplessness. The viewer stops asking "what happens?" and starts asking "when do they find out, and what will it cost?" That is a stronger engine because it runs continuously through the scene instead of firing once at the end.
**Used for and where it works best:** Reach for it when a scene's surface content is mundane but its stakes are enormous — a family meal, a job interview, a customs desk, a wedding toast. It is the cheapest way to make a quiet scene unwatchable in the right way, and it is what lets you afford a slow scene at all. The craft rule that makes it work: the ignorant character must keep making *reasonable* choices. The moment they behave stupidly, irony collapses into contempt and the audience roots against them. Second rule: write one line that is innocent to the speaker and lethal to us. That line is the scene.
**Best in:** formats: Feature Film, One-Hour Drama, Stage Play, Novel, Limited Series | genres: Tragedy, Thriller, Comedy, Family Drama, Historical
**Avoid when:** The pleasure of the piece is the puzzle. Tell the audience who the killer is and you have written suspense, not mystery — legitimate, but decide it on purpose rather than by accident. Also avoid holding the gap past its natural life: irony stretched too far stops being tension and becomes irritation at a character who "should have noticed by now."
**Example:**
> *We watched him bury the ring in the garden in scene four.*
> MOTHER: You've been so good to me this month.
> SON: Don't say that.
> MOTHER: I'm leaving you the house. And your grandmother's ring — I want it on your wife's hand, not in a bank.

**Yields to:** `info.mystery_audience_behind` — The pleasure of the piece is the puzzle.  
`info.dramatic_irony`

### Suspense Through Shared Knowledge

**Also called:** level position, audience-with-character, co-discovery, the walk-alongside
**What it is:** The audience and the protagonist learn everything at the same instant. Nobody is ahead. Tension comes from the shared not-knowing plus a visible clock or threat.
**Effect on the audience:** Identification rather than dread. The viewer feels *inside* the character rather than above them, and their pulse tracks the character's pulse instead of running ahead of it.
**Used for and where it works best:** The default for investigation, horror, and any story whose emotional point is "what it feels like to be this person in this hour." Use it when you want the audience to make the same mistake the protagonist makes, so the correction lands on both at once. The craft rule: with no information advantage, you must supply pressure from somewhere else — a deadline, a diminishing resource, a door that will open in ninety seconds. Level position plus no clock equals a scene that is merely vague. Pair it with a hard `scene.scene_question` so the audience always knows what they are waiting to learn.
**Best in:** formats: Feature Film, Short Film, One-Hour Drama, Game Narrative, Novel | genres: Horror, Thriller, Mystery, War, Psychological
**Avoid when:** You need the audience to feel a character's blindness. Level position cannot deliver the dread of watching a character miss what you can see — only the shock of learning it with them, or the character's own fear shared at full strength, which is what `info.restricted_narration` sustains — so you are giving up the most reliable tension source you have. It is also weak across a long serial: forty episodes of pure co-discovery flattens, because nobody in the audience ever gets to feel clever.
**Example:**
> She opens the third box. Old invoices. Fourth box. Invoices.
> Fifth box: her own name, in her father's hand, on a form she has never seen.
> *We read it as she reads it. Downstairs, a car door shuts.*

**Yields to:** `info.dramatic_irony` — You need the audience to feel a character's blindness.  
`info.suspense_shared_knowledge`

### Mystery — The Audience Behind

**Also called:** audience-behind position, inferior position, withheld-fact structure, whodunnit engine
**What it is:** Characters in the story know something the audience does not, and the story is shaped so the audience wants to close that gap. The reader knows *less* than the people in the book.
**Effect on the audience:** Active curiosity. The viewer becomes a participant — building theories, assigning suspicion, arguing with the screen. This is the only position that turns an audience into a detective.
**Used for and where it works best:** Use it when you want the audience working, not merely feeling. It is the right choice for crime, for a family secret, and for any story whose theme is "the truth is not what it looked like." The craft rule that separates real mystery from mere confusion: every withheld fact must sit behind a clearly posed question. "Who killed him?" is mystery. "What is going on in this film?" is confusion. Pose the question out loud, early, in a character's mouth. Note the pairing — a mystery for the audience is often `dial.strategic_withholding` for the character holding the answer.
**Best in:** formats: Novel, Feature Film, Limited Series, Podcast, Game Narrative | genres: Mystery, Crime, Noir, Psychological, Drama
**Avoid when:** The scene is about a relationship rather than a fact. Withholding inside an intimate scene reads as coyness, and the audience disengages from people they cannot read. Also avoid stacking more than two open mysteries at once in short form — the audience drops all of them.
**Example:**
> DETECTIVE: Your sister was at the house that night.
> WOMAN: She wasn't.
> DETECTIVE: Her car was.
> WOMAN: *(a beat too long)* Then someone else was driving it.

**Yields to:** `info.suspense_shared_knowledge` — The scene is a relationship, not a fact.  
`info.mystery_audience_behind`

### Surprise

**Also called:** the shock, the ambush, the unprepared reversal
**What it is:** The audience is given no advance signal and the event arrives without warning. Hitchcock's fifteen seconds of surprise against fifteen minutes of suspense.
**Effect on the audience:** A hard, short spike — then nothing. Surprise does not accumulate; it discharges. Its afterlife depends entirely on whether the audience can look back and see it was possible.
**Used for and where it works best:** Use surprise sparingly and structurally, not decoratively. It belongs at exactly the moments where the *unexpectedness itself* is the meaning: a death meant to feel arbitrary, a betrayal whose point is that nobody saw it, a first-act inciting event. The craft rule: a surprise must be retroactively inevitable. The audience should get four seconds of shock, then a cold second of "of course." If they cannot construct that second, you have written randomness. Build the "of course" out of a plant they did not weight at the time (`info.buried_plant`).
**Best in:** formats: Feature Film, Short Film, Reels/Shorts, Novel, Vertical Micro-Drama | genres: Horror, Thriller, War, Crime, Tragedy
**Avoid when:** You have more than sixty seconds of scene to fill. Surprise cannot carry a scene — it can only end one. Writers reach for it when they should have reached for dramatic irony, and end up with a flat four minutes followed by a bang nobody feels.
**Example:**
> He signs the last page. Slides it across.
> LAWYER: Congratulations. It's yours.
> He stands, shakes her hand, turns — and the glass behind him is already spidering, and the sound arrives after.

**Yields to:** `info.dramatic_irony` — More than sixty seconds of scene to fill.  
`info.surprise`

### The Knowledge Ledger

**Also called:** the who-knows-what grid, information audit, the knowledge map
**What it is:** A working document, not a device: for every beat, a row per party — audience, protagonist, antagonist, each supporting character — recording what each one knows at that moment. You build it before you write and audit against it after.
**Effect on the audience:** Indirect but decisive. It is what stops the audience feeling that a character "forgot" something, or that the film told them a fact twice, or that a reveal arrived without anyone in the room being changed by it.
**Used for and where it works best:** Mandatory the moment you have three or more parties holding different versions of the truth, and mandatory for any multi-episode story. Two rules come straight out of the ledger. One: any beat where no row changes is a beat you should question. Two: the instant two rows equalise, that thread's tension is over — so either end the thread or open a new asymmetry in the same scene. The ledger is also the fastest way to catch the commonest structural bug in a rewrite: a character reacting to information the ledger says they do not yet have.
**Best in:** formats: Limited Series, One-Hour Drama, Feature Film, Novel, Game Narrative | genres: Crime, Mystery, Thriller, Drama, Psychological, Social Drama
**Avoid when:** Never avoid it — but do not confuse it with the story. A ledger tells you where tension is available, not what the scene is about. Writers who plot from the ledger alone produce mechanically clever, emotionally inert work.
**Example:**
> Beat 14 — the funeral.
> AUDIENCE: knows the will was forged. PRIEST: knows. WIDOW: does not. BROTHER: suspects, wrongly, the daughter.
> *Three different scenes are now available in the same room, and only the widow's is free of irony.*

`info.knowledge_ledger`

---

## Plant, Payoff and Foreshadowing

### The Plant and the Payoff

**Also called:** setup and payoff, seeding, the deposit and the withdrawal
**What it is:** A fact, object, skill or phrase is introduced early with low emphasis, then becomes decisive later. The plant buys the payoff its credibility.
**Effect on the audience:** At payoff, a distinct pleasure that is neither surprise nor satisfaction but both — the sense that the story was built rather than improvised. It is the strongest single signal to an audience that they are in competent hands.
**Used for and where it works best:** Any time a late turn depends on something the audience did not previously know, you owe them a plant. The rule that actually matters is distance and disguise: plant it at least two scenes away from the payoff, and give it a *different reason to exist* in its own scene — a joke, a character detail, a piece of friction. A plant that exists only to be planted announces itself. Second rule: plant the *capability*, pay off the *choice*. Show that she can pick a lock; the payoff is that she chooses to, on her mother's door.
**Best in:** formats: Feature Film, Novel, One-Hour Drama, Animation Feature, Short Film | genres: Thriller, Crime, Comedy, Drama, Mystery, Coming of Age
**Avoid when:** The payoff is emotional rather than plot-mechanical. You do not plant a feeling; you build it. Writers who try to "set up" an emotional turn with an early object end up with a symbol they have to keep explaining.
**Example:**
> *Scene 6, played for laughs:* "You still can't swim? You grew up on a river."
> *Scene 41, no laugh:* He goes in after the boy anyway, and the river takes them both to the bend before he gets a hand on the shirt.

**Yields to:** `info.foreshadowing` — The payoff is emotional, not plot-mechanical.  
`info.plant_and_payoff`

### Chekhov's Gun

**Also called:** the loaded rifle rule, the obligation of the object, no idle props
**What it is:** The stricter, inverted form of planting: if you conspicuously introduce a loaded element, you are obliged to fire it. Chekhov's own phrasing — if a pistol hangs on the wall in act one, it must go off in act two; otherwise do not hang it there.
**Effect on the audience:** A conspicuous object creates a low-level expectation running in the background. Paid off, it feels like design. Unpaid, it feels like a loose thread, and audiences register the debt even when they cannot name it.
**Used for and where it works best:** Use it deliberately as a *promise* when you want the audience leaning toward an object — a locked drawer, a gun in a glovebox, an unopened letter, a name on a tablet nobody will translate. The craft rule: the obligation is created by *emphasis*, not by presence. A rifle in the background of a hunting lodge owes you nothing; a rifle the camera holds on for three seconds owes you everything. Control your emphasis budget and know exactly which objects you have put in debt.
**Best in:** formats: Stage Play, Feature Film, Short Film, One-Hour Drama, Game Narrative | genres: Thriller, Crime, Tragedy, Horror, Drama
**Avoid when:** You are writing a dense, textured world — historical, heritage, procedural — where objects exist because the world does. Taken as a universal law, Chekhov's gun strips atmosphere and turns every prop into a plot token. The real misuse, though, is the reverse: firing a gun that was never hung. That is not a gun problem, that is `info.the_cheat`.
**Example:**
> Act one, she shows him the drawer: "That stays locked. My husband's, not mine."
> Act two, she is gone and the drawer is open, and there is nothing in it but a photograph of the man now sitting in her kitchen.

**Yields to:** `info.buried_plant` — Dense textured world where objects exist anyway.  
`info.chekhovs_gun`

### The Buried Plant

**Also called:** camouflaged setup, hidden in plain sight, planting under cover
**What it is:** A plant deliberately disguised by burying it inside a moment that is interesting for another reason, so the audience receives the fact without weighting it.
**Effect on the audience:** They do not remember being told — but they recognise it instantly when the payoff names it. That gap between "I wasn't told" and "yes I was" is the exact sensation of a well-built twist.
**Used for and where it works best:** Essential any time the payoff is a reversal the audience must not predict. Three reliable burial sites: inside a laugh, inside an argument about something else, and inside information the audience is busy dismissing as routine exposition. The craft rule: bury the plant *under the audience's attention*, not out of sight. Put it in the second half of a line whose first half is more interesting, or hand it to a character the audience is not currently trusting. If you dim the lights on the plant instead, you have not buried it — you have withheld it, and you will pay for that at the reveal.
**Best in:** formats: Feature Film, Novel, Limited Series, Short Film | genres: Mystery, Thriller, Crime, Psychological, Noir
**Avoid when:** The audience is already overloaded. In the first ten minutes of a dense ensemble piece a buried plant is lost, not stored. Bury late-ish — after the audience has a stable map of who is who.
**Example:**
> *Buried, in a row about money:* "—and don't tell me about my brother, my brother has been dead eleven years, so pick another lecture."
> *Paid off, ninety pages later:* The signature on the transfer is dated last March, and it is her brother's.

`info.buried_plant`

### Foreshadowing

**Also called:** anticipation, seeding tone, the shadow ahead, prefiguring
**What it is:** Signalling the *shape* of what is coming without specifying it — an image, a line, a weather, a minor echo that conditions the audience to accept an outcome when it arrives. Distinct from planting: a plant supplies a fact, foreshadowing supplies a mood and a permission.
**Effect on the audience:** Unconscious preparation. When the outcome lands it feels like the story's nature rather than the writer's decision — which is the difference between a tragic ending and a cruel one.
**Used for and where it works best:** Use it wherever an ending would otherwise feel imposed, particularly deaths, breakups, and any ending that denies the audience what they were rooting for. The craft rule: foreshadow the *category*, never the event. "Someone will not come back from this river" is a shadow; "he will drown at the bend" is a spoiler. A second, harder rule: the strongest foreshadowing is a false reassurance, because audiences remember reassurance more sharply than warning. Read alongside `struct.mckee_controlling_idea` — foreshadowing is where the theme first shows its teeth.
**Best in:** formats: Feature Film, Novel, Limited Series, Stage Play, Animation Feature | genres: Tragedy, Drama, Horror, Historical, Family Drama, Coming of Age
**Avoid when:** The story's power depends on the ending being unthinkable. Some endings must arrive with no shadow at all — atrocity, accident, the arbitrary. Foreshadow those and you have made them meaningful, which may be exactly the lie you did not want to tell.
**Example:**
> FATHER: The river's low this year. It's when it's low that people drown — you can see the bottom and you stop respecting it.
> BOY: I respect it.
> FATHER: Everyone respects it in June.

**Yields to:** `info.surprise` — The ending must be unthinkable: atrocity, accident, the arbitrary.  
`info.foreshadowing`

### Telegraphing

**Also called:** over-signposting, the flagged setup, tipping the hand, the flashing prop
**What it is:** The failure mode of planting and foreshadowing — putting so much emphasis on a setup that the audience solves the story on the spot. Named here as a technique because you must be able to diagnose it, and because a controlled dose is occasionally the right tool.
**Effect on the audience:** Instant loss of altitude. They stop watching the story and start waiting for the story to catch up to them, which is the worst position an audience can occupy, because it is boredom disguised as comprehension.
**Used for and where it works best:** Deliberate telegraphing has exactly two legitimate uses. One: comedy, where the pleasure is watching the inevitable arrive — flag the banana skin hard, then delay it. Two: tragedy, where you *want* the audience ahead of the character, which converts a twist into dramatic irony on purpose. The diagnostic rule for the unwanted kind: if a detail is receiving emphasis disproportionate to its current story function — a held shot, a musical sting, a character repeating it, a scene that exists only to deliver it — it is telegraphed. The fix is almost never to cut the plant; it is to give the plant's scene a different reason to exist.
**Best in:** formats: Animation Feature, Feature Film, Stage Play, Reels/Shorts | genres: Comedy, Tragedy, Family Drama
**Avoid when:** Anywhere the surprise is the product. In mystery, thriller and any twist-dependent short form, one telegraphed beat costs you the entire back half. Test it on a cold reader and ask them to guess the ending at the midpoint — if they get it, you have a signal problem, not a structure problem.
**Example:**
> *Telegraphed:* He pauses at the cabinet. Music swells. He takes out the pills. Looks at them. Puts them back. Closes the cabinet slowly.
> *Buried:* "Grab my bag, would you? Everything's in it, I never unpack it." She tosses it to him — it rattles.

**Yields to:** `info.buried_plant` — The surprise is the product; bury the setup.  
`info.telegraphing`

### The Rule of Three Placements

**Also called:** the triple plant, plant-echo-payoff, the three-touch rule
**What it is:** A setup placed three times: once to establish, once to normalise, once to pay off. The middle touch is the whole technique — it converts a fact from "something the story told me" into "something that is just true about this world."
**Effect on the audience:** Removes the suspicion of authorial hand. One mention feels like a clue and puts them on alert; two makes it furniture; the third can then carry enormous weight without feeling engineered.
**Used for and where it works best:** Use it whenever a payoff must be both unpredictable and unarguable — alibis, physical capabilities, a character's habit, a rule of a fantasy or historical world. The craft rule: the three placements must sit in three *different emotional registers* — say, a joke, a complaint, and a crisis. Three placements in the same register is repetition, and the audience reads it as the writer nudging. In serial work, spread them across episodes: establish in one, normalise in another, pay off in a third.
**Best in:** formats: Feature Film, Limited Series, Novel, One-Hour Drama, Animation Feature | genres: Crime, Thriller, Comedy, Mystery, Drama, Science Fiction
**Avoid when:** The runtime is short. In a five-minute short or a sixty-second vertical there is no room for the middle touch, and forcing it makes the piece feel padded — plant once, hard, and pay off fast.
**Example:**
> *Touch 1, a joke:* "She counts the cutlery after guests leave. Every time."
> *Touch 2, a complaint:* "Mother, please. Nobody has stolen a fork in this house in forty years."
> *Touch 3:* "Twenty-three forks. There were twenty-four on Tuesday." And she names who sat where.

**Yields to:** `info.plant_and_payoff` — Runtime too short for the middle touch.  
`info.rule_of_three_placements`

---

## Misdirection and the False Trail

### The Red Herring

**Also called:** false lead, decoy suspect, the planted wrong answer
**What it is:** A piece of genuinely persuasive evidence that points confidently at a false conclusion, so the audience spends their attention in the wrong direction while the truth walks past.
**Effect on the audience:** Confident wrongness, which is far more useful to you than uncertainty. An audience with a theory is engaged; an audience with no theory is merely waiting.
**Used for and where it works best:** Mandatory in any fair-play mystery and useful in any story with a late reversal. The rule that separates a good herring from a cheap one: the herring must have its own honest reason to exist. The suspicious man is suspicious because he is hiding an affair, a debt, an illegal job — something true and human, just not the crime. If your decoy behaves oddly for no reason but to fool the reader, they will smell the author's hand, and worse, the exoneration will feel like a cheat rather than a clearing. Second rule: resolve every herring. An unexplained false lead is just a plot hole with an alibi.
**Best in:** formats: Novel, Feature Film, Limited Series, Podcast, Game Narrative | genres: Mystery, Crime, Thriller, Noir, Psychological
**Avoid when:** You have fewer than three plausible parties. With two candidates a red herring is a coin flip and half your audience gets it right by accident. Also avoid in short form: a sixty-second piece cannot afford to plant a lie and then correct it.
**Example:**
> He burned something in the yard the night she died. He lies about it twice.
> In act three it comes out: army discharge papers. Forged. He has not been a captain for nine years, and his wife does not know.

**Yields to:** `info.double_meaning_clue` — Fewer than three plausible parties.  
`info.red_herring`

### The Double-Meaning Clue

**Also called:** the two-way clue, the reversible detail, the honest lie
**What it is:** A single true detail that supports two complete readings — the false one the audience takes now and the real one they will take later. Nothing is hidden and nothing is added; only the frame changes.
**Effect on the audience:** The specific, addictive pleasure of the re-read. This is the mechanism behind every twist that makes an audience immediately want to watch the film again, because the second pass genuinely plays differently.
**Used for and where it works best:** The most valuable single technique in twist construction, because it never violates fair play — the audience was told the truth. Build at least three for any major reversal. The craft rule: let a character voice the *wrong* reading out loud, confidently, and let no one contradict it. The audience adopts the stated interpretation and stops examining the fact. Related to `dial.half_truth`, but the difference matters: a half-truth is a character choosing to deceive; a double-meaning clue can be spoken by someone entirely sincere.
**Best in:** formats: Feature Film, Novel, Limited Series, Short Film, Stage Play | genres: Mystery, Psychological, Thriller, Noir, Drama, Horror
**Avoid when:** The second meaning requires specialist knowledge the audience has no way to hold — medical, legal, linguistic. Then it is not a double meaning, it is a private joke, and the reveal will feel arbitrary no matter how fair it technically was.
**Example:**
> NURSE: He asks for her every morning. Every single morning, first thing.
> *We hear: devotion.*
> *Later: he has no memory past 1998. He asks every morning because every morning he has just been told, and every morning he is hearing it for the first time.*

**Yields to:** `info.buried_plant` — Second meaning needs specialist knowledge.  
`info.double_meaning_clue`

### Misdirection by Attention

**Also called:** the magician's move, misdirection by excess, loud truth quiet truth
**What it is:** Rather than concealing the key fact, you give the audience *more* information elsewhere and make that other information more interesting. Attention, not access, is what you are controlling.
**Effect on the audience:** They feel fully informed — which is the point. A reader who suspects something is being kept from them starts hunting. A reader who is being generously fed relaxes and stops auditing.
**Used for and where it works best:** The correct default whenever you are tempted to withhold. Ask: instead of hiding X, what can I make louder than X? Reliable louder-than options are a fight, a deadline, a sexual current, a physical danger, and a comic embarrassment. The craft rule: deliver the fact you must conceal *during* the audience's peak interest in something else — the line lands, the eye is elsewhere, and the fact is filed without a flag. This is why the best concealments so often sit inside arguments.
**Best in:** formats: Feature Film, Novel, One-Hour Drama, Limited Series, Game Narrative | genres: Crime, Thriller, Mystery, Comedy, Psychological, Noir
**Avoid when:** The competing attention is so strong that the buried fact is not merely unweighted but unregistered. If a test reader cannot find the plant *when told it is there*, you did not misdirect, you deleted.
**Example:**
> *The loud thing:* she has just told him she is leaving, and he is trying not to cry in a restaurant.
> *The quiet thing, his line, mid-collapse:* "Take the car. I can't drive it anyway, not since the licence thing."
> *Forty minutes later, that licence is the alibi that fails.*

`info.attention_misdirection`

### The Lesser Guilt

**Also called:** guilty of something else, the secondary secret, the wrong crime
**What it is:** A suspect behaves exactly like a guilty person because they *are* guilty — of a different, smaller, usually shameful thing. Their evasions are real, their motive to lie is real, and the audience misreads all of it.
**Effect on the audience:** Total conviction, followed by a reveal that plays as poignant rather than trick-like, because the decoy turns out to be a person rather than a device.
**Used for and where it works best:** The single best upgrade to a flat red herring, and the way to get misdirection and characterisation out of the same page. Use it when you need a suspect who can survive close scrutiny. The craft rule: the lesser guilt must be something the character would protect *more fiercely than an alibi* — an affair, an addiction, an immigration status, a child they never declared, money taken from a dying parent. If the audience thinks "just tell them where you were," the mechanism is dead. Give the secret a cost that outranks suspicion.
**Best in:** formats: Limited Series, Novel, Feature Film, One-Hour Drama, Podcast | genres: Crime, Mystery, Social Drama, Family Drama, Noir, Drama
**Avoid when:** Your story has no room to resolve the second secret with dignity. Exposing someone's private shame purely to clear them of murder is cheap, and audiences feel used on the character's behalf.
**Example:**
> DETECTIVE: You were seen leaving at eleven. You told us midnight.
> *He says nothing.*
> DETECTIVE: A man is dead.
> *He says nothing.* In act three: at eleven he was at the clinic with his daughter, under a name that is not his, in a country he entered illegally.

**Yields to:** `info.red_herring` — No room to resolve the second secret with dignity.  
`info.lesser_guilt`

---

## Narration, Point of View and Inference

### The Unreliable Narrator

**Also called:** untrustworthy narration, the deceiving teller, narrative bias
**What it is:** The voice telling the story misrepresents it — by lying, by self-deception, by limited understanding, or by selective omission — and the audience must eventually read past the narration to the events underneath.
**Effect on the audience:** Double vision. Once they suspect the teller, every sentence acquires a second track, and reading becomes investigation rather than reception.
**Used for and where it works best:** Use it when the *distortion itself* is the subject — grief, addiction, ideology, shame, a person who cannot afford to know what they did. It is the natural home of `arc.the_lie`: the narrator's unreliability is the lie the character lives by, expressed as prose. The craft rule that makes it fair: plant the unreliability early through small verifiable inconsistencies — a date that shifts, a detail another character contradicts, an emotion that does not match its event — so the audience feels something is off long before they can name it. The narrator may be wrong about meaning; be very careful about letting them be wrong about *observable fact*, and never let them be wrong about a fact the solution depends on.
**Best in:** formats: Novel, Feature Film, Limited Series, Podcast, Game Narrative | genres: Psychological, Noir, Mystery, Drama, Horror, Crime
**Avoid when:** The story needs the audience to trust a factual account — procedural, historical, documentary-adjacent work. Also avoid the version where the narrator simply never mentions the central fact until page 300: that is not unreliability, that is `info.the_cheat` wearing a coat.
**Example:**
> "I was calm that night. I want that on the record. I made tea, I read for an hour, and I went to bed at ten."
> *Two chapters later, a neighbour, in passing:* "You were out in the road at midnight in your nightclothes. I waved. You didn't see me."

**Yields to:** `info.naive_narrator` — The audience must trust the factual account.  
`info.unreliable_narrator`

### The Naive Narrator

**Also called:** the innocent eye, the child witness, the under-comprehending teller
**What it is:** A narrator who reports accurately but cannot interpret. They describe exactly what happened and draw the wrong conclusion, leaving the correct conclusion assembled entirely in the audience's head.
**Effect on the audience:** Dramatic irony delivered through prose rather than staging — plus tenderness, because the audience's superior understanding is inseparable from their pity.
**Used for and where it works best:** The strongest tool available for writing about abuse, war, poverty and family collapse without editorialising, because the reader does the condemning and therefore believes it. Use it for comedy too, where the same gap produces laughter instead. The craft rule: the naive narrator must be *reliable about detail and unreliable about meaning* — get that ratio backwards and you lose the audience's trust in the evidence, which is the only thing holding the device up. Second rule: never let them become wise for a line. One insightful sentence destroys the whole construction.
**Best in:** formats: Novel, Feature Film, Short Film, Animation Feature, Stage Play | genres: Coming of Age, Social Drama, War, Family Drama, Comedy, Historical
**Avoid when:** The plot requires the narrator to act decisively on correct information. A narrator who cannot understand cannot drive, so you need someone else supplying momentum — otherwise you have a beautiful, static book.
**Example:**
> "Mama was happy that week because Papa was away for work again, and she sang in the kitchen, and we had bread with sugar for supper three nights, which is what we have when the money is good."

**Yields to:** `info.dramatic_irony` — The narrator must act on correct information.  
`info.naive_narrator`

### The Withheld Point of View

**Also called:** the missing POV, the unentered head, camera-outside, the closed character
**What it is:** A character whose interiority the story never enters, in a story that enters other people's freely. What they think is structurally unavailable, so the audience reads them from the outside only.
**Effect on the audience:** Unease and fascination directed at one specific person. The audience notices the asymmetry without being able to articulate it, and leans toward whoever they cannot hear.
**Used for and where it works best:** The cleanest fair-play way to hold a secret in a story that otherwise grants wide access — including the killer, the betrayer, the one who knows. Knox's rule for detective fiction points at exactly this: the culprit must be present early but must not be someone whose thoughts the reader has been allowed into. The craft rule: establish the exclusion as a *pattern from page one*, not from the moment it becomes convenient. If chapter one is inside everyone's head and chapter nineteen suddenly steps outside one person's, you have flagged them. Consistent exclusion reads as style; selective exclusion reads as a tell.
**Best in:** formats: Novel, Limited Series, Feature Film, Stage Play | genres: Mystery, Crime, Psychological, Noir, Horror, Drama
**Avoid when:** The withheld character is your protagonist and their choice is the climax. An audience cannot invest in a decision they have no access to; you will get a resolved plot and an unsatisfied room.
**Example:**
> *We are inside the wife's fear and the son's exhaustion, all book.*
> *The husband we only ever see:* He put his glasses on the table, lens-down, the way he always did, and said, "I'll go tomorrow, then." Nobody could tell whether he meant it as a concession or a threat.

**Yields to:** `info.unreliable_narrator` — The withheld character is the protagonist.  
`info.withheld_pov`

### Delayed Decoding

**Also called:** deferred comprehension, the misread moment, impression-before-meaning
**What it is:** An event is delivered as raw sensory impression — what was seen, heard, felt — before it is delivered as understanding. The audience experiences the effect for several seconds or several sentences before learning the cause.
**Effect on the audience:** Immersion at the speed of real perception, then a small internal jolt as the picture snaps into sense. It is the closest prose and film get to putting an audience inside a moment of shock.
**Used for and where it works best:** Violence, accident, betrayal, and any instant that in life is understood only afterwards. Use it to replace the flat report of an event with the experience of it. The craft rule: the interval must be *short* — seconds on screen, one paragraph on the page — and the raw impression must be accurate enough that on a re-read it obviously described the true event. Stretched too long, delayed decoding becomes coyness. Also: do not decode in narration if a character can decode out loud; the line where someone finally names what happened is usually the best line in the sequence.
**Best in:** formats: Novel, Feature Film, Short Film, Game Narrative, One-Hour Drama | genres: War, Horror, Thriller, Psychological, Crime, Drama
**Avoid when:** The audience needs to act on the information immediately, as in procedural or comedy. Also avoid stacking it: two delayed decodings in a row and the audience stops trusting their own eyes, which is exhausting rather than gripping.
**Example:**
> Something struck the wall beside him and plaster came off it in a puff, and he thought, absurdly, that the building was very old and badly built.
> Then the second one, and the sound arrived with it, and he was already on the floor.

`info.delayed_decoding`

### Restricted Narration

**Also called:** focalisation lock, the single-lens rule, tight third, we-only-know-what-she-knows
**What it is:** A hard rule that the story never presents information the focal character does not have — no cutaways, no meanwhile, no scene they are not in.
**Effect on the audience:** Claustrophobia and total identification. Every limitation of the character becomes a limitation of the audience, so the character's paranoia is not described, it is inflicted.
**Used for and where it works best:** The right structure when the subject is not-knowing: a hostage, a new arrival, an investigator with no institutional backing, someone losing their memory or their grip. It is also the honest way to sustain a mystery over a long runtime without the audience feeling manipulated — you are not hiding anything, you are standing where she stands. The craft rule: declare the lock in the first ten minutes and never break it, not once. A single cutaway to the antagonist mid-film retroactively converts every earlier restriction from an honest constraint into a choice to withhold, and the audience feels it.
**Best in:** formats: Feature Film, Novel, Game Narrative, Short Film, Limited Series | genres: Horror, Thriller, Psychological, Mystery, War, Noir
**Avoid when:** You need dramatic irony, which restricted narration makes structurally impossible — you cannot show the bomb without leaving her side. It is also hard in ensemble and serial drama, where audiences expect to follow several fronts.
**Example:**
> She hears the car pull in. She does not go to the window.
> Two doors. Two voices, one of them her husband's and one of them not. Twenty minutes of nothing. Then the car leaves, and he comes up, and he says, "Wrong house," and washes his hands for a long time.

**Yields to:** `info.dramatic_irony` — You need the bomb under the table.  
`info.restricted_narration`

### The Secret the Reader Holds

**Also called:** audience-only knowledge, the private fact, complicity
**What it is:** Information given to the audience and to no character at all — not the protagonist, not the antagonist. The audience becomes the sole holder.
**Effect on the audience:** Complicity, which is a different and stickier feeling than ordinary dramatic irony. When only *you* know, you are not watching the story, you are in it — and this is where guilt, superiority and dread all become available at once.
**Used for and where it works best:** Use it to make an audience implicated rather than merely informed: they know the child is in the cupboard, they know which brother took the money, they know the informer's name. The craft rule: an audience-only secret must eventually be transferred to a character, and the *transfer* is your climax, not the secret. Decide early who receives it and in what scene, because that choice determines the whole third act. Excellent in heritage and historical work, where the audience's knowledge of how history went is itself the secret the characters cannot hold.
**Best in:** formats: Feature Film, Limited Series, Stage Play, Novel, Documentary | genres: Tragedy, Historical, War, Heritage, Thriller, Horror
**Avoid when:** You never plan to pay the transfer off. A secret held by the audience alone from beginning to end is a trick, not a structure, and the ending feels withheld from everyone including them.
**Example:**
> *We saw the note go into the fire in scene two. Nobody in the house did.*
> DAUGHTER: She left without a word. Not one word, after thirty years.
> BROTHER: Then that's your answer about her.
> *And we sit there holding the only word she left.*

`info.audience_only_secret`

---

## Staging the Reveal

### The Recontextualising Reveal

**Also called:** the reframe, the retroactive twist, the second-reading reveal
**What it is:** A reveal that adds no new event but changes the meaning of events already shown. Nothing that happened is undone; everything that happened now reads differently.
**Effect on the audience:** The strongest single effect available in this category — a simultaneous forward shock and backward re-sort, with the compulsion to immediately re-watch. The reaction you want is not "the writer lied to me" but "the writer outplayed me."
**Used for and where it works best:** Use it when your theme is about perception — what a family refused to see, what a nation tells itself, what a man cannot admit. The craft rule: the reveal must change *relationships and meaning*, not merely facts. "He was dead the whole time" only works because it reframes every conversation he had. Build it out of `info.double_meaning_clue` units, three minimum, then test by replaying the piece from the new position: if a single earlier scene now plays as nonsense rather than as newly meaningful, the reveal is not clean.
**Best in:** formats: Feature Film, Novel, Limited Series, Short Film, Stage Play | genres: Psychological, Mystery, Drama, Thriller, Tragedy, Noir
**Avoid when:** The audience's emotional investment is in a relationship the reframe invalidates. Reveal that a loving marriage was a decade of manipulation and you may have produced a clever ending nobody wants to have watched. Reframes should deepen investment, not confiscate it.
**Example:**
> SON: Every week for a year you drove four hours to see him.
> MOTHER: I drove four hours to make sure he stayed there.

`info.recontextualising_reveal`

### The Staged Reveal

**Also called:** the reveal ladder, layered disclosure, drip-feed, tiered truth
**What it is:** One large truth broken into ordered fragments, each released at a separate beat, each complete enough to satisfy and incomplete enough to raise the next question.
**Effect on the audience:** Sustained forward pull with regular payment. The audience is never in debt for long, which is what lets you keep them for eight episodes rather than eight minutes.
**Used for and where it works best:** Essential in anything longer than a feature, and in any story with one central secret that must last. The craft rule: order the rungs by *escalating personal cost*, not by logical sequence. Reveal what happened, then who did it, then who knew, then that the protagonist was told once and forgot. Each rung should move closer to the protagonist's own culpability. Second rule: each rung must answer the previous question fully. A rung that deflects instead of answering is a stall, and audiences feel a stall within two beats. A major rung belongs at the `struct.stc_midpoint`.
**Best in:** formats: Limited Series, One-Hour Drama, Novel, Podcast, Game Narrative | genres: Crime, Mystery, Drama, Social Drama, Family Drama, Thriller
**Avoid when:** The runtime is short or the secret is small. A three-rung ladder on a thin secret is the commonest cause of a series that feels padded — if the final rung is not worth the wait, the ladder itself becomes the disappointment.
**Example:**
> Ep 2: the money is gone.
> Ep 4: the accountant moved it.
> Ep 6: the accountant moved it on her mother's instruction.
> Ep 8: her mother signed that instruction the week after the diagnosis, and it was meant to pay for her.

**Yields to:** `info.micro_reveal_ladder` — Short runtime or a thin secret.  
`info.staged_reveal`

### The Double Reveal

**Also called:** the twist behind the twist, the false bottom, the second door
**What it is:** A reveal that appears to resolve everything, followed closely by a second reveal that reframes the first. The audience gets to be right, briefly, and is then moved again.
**Effect on the audience:** Relief immediately withdrawn. Used well it produces the best reaction in the form, because the guard drops completely between the two — nobody defends themselves twice in ten seconds.
**Used for and where it works best:** Use it when your audience is genre-literate and will decode a single twist early. The first reveal is the one you let them win. The craft rule: the first reveal must be *genuinely true and genuinely satisfying* — not a fake-out. If the first turns out to be a lie, you have written one twist plus a cheat. If the first is true and the second recontextualises it, you have written two. Second rule: keep the gap tight, thirty seconds to two minutes on screen. Let the audience settle any longer and the second reveal reads as an extra ending rather than a completion.
**Best in:** formats: Feature Film, Limited Series, Short Film, Novel, Vertical Micro-Drama | genres: Thriller, Crime, Mystery, Noir, Horror, Psychological
**Avoid when:** The audience is already saturated. Two twists on top of a twisty film is where the room stops believing anything, and a story nobody believes cannot be moved. One double reveal per piece, at the end, or none.
**Example:**
> Reveal one: the brother forged the will. He admits it, and he is crying, and it is true.
> Reveal two, ninety seconds later: their mother dictated it to him, because the real will left everything to a man none of them has ever heard of.

`info.double_reveal`

### Let the Reveal Land on a Character

**Also called:** the witnessed reveal, reaction-carries-reveal, the receiver
**What it is:** Staging a reveal so the audience learns it by watching a character learn it, rather than being told it directly by the story.
**Effect on the audience:** Emotion instead of information. They take their reading from the face in front of them, which is why the same fact can play as devastation, relief or triumph depending only on who is standing there.
**Used for and where it works best:** The default staging for any reveal that is supposed to hurt. Choose the receiver deliberately — usually the person with the most to lose, not the person the fact is about. The craft rule: a reveal delivered to an empty room is data; a reveal delivered to someone who must now do something is drama. Second rule: do not write the receiver's reaction as a speech. Play it in behaviour and let `dial.unanswered_line` do the work — the reveal lands hardest in the silence after it. If you have a reveal with no receiver, you have almost certainly put it in the wrong scene.
**Best in:** formats: Feature Film, One-Hour Drama, Stage Play, Limited Series, Short Film | genres: Drama, Family Drama, Tragedy, Crime, Social Drama, Romance
**Avoid when:** The reveal is purely structural and belongs to the audience alone — a jump in time, a hidden identity no character is present to discover. Forcing a receiver into those produces a bystander with nothing to play.
**Example:**
> DOCTOR: We found it in both lungs.
> *He is not looking at the doctor. He is looking at his daughter, who has stopped writing.*
> HE: Write it down. Write down what she said — we'll need it for the insurance.

**Yields to:** `info.audience_only_secret` — The reveal belongs to the audience alone.  
`info.reveal_lands_on_character`

### The Midpoint Reveal

**Also called:** the halfway truth, the mirror-moment disclosure, the second-act turn
**What it is:** Placing the story's largest information shift at the centre rather than the end — so the back half is not about discovering the truth but about living with it.
**Effect on the audience:** The story audibly changes gear. Curiosity converts into dread or resolve, and the audience stops predicting the answer and starts predicting the consequence.
**Used for and where it works best:** Use it whenever the *aftermath* is more interesting than the puzzle — which in character drama it almost always is. A reveal at the end buys one moment; a reveal at the midpoint buys forty minutes. The craft rule: a midpoint reveal must force an irreversible decision within the same sequence. If the protagonist learns the truth and does nothing different, you have moved the reveal without moving the story. See `struct.stc_midpoint` for placement, and note the trade: you are converting the audience from mystery position into dramatic irony position, so make sure the remaining characters' ignorance is worth watching.
**Best in:** formats: Feature Film, Limited Series, Novel, One-Hour Drama | genres: Drama, Crime, Social Drama, Family Drama, Thriller, Historical
**Avoid when:** The reveal is the entire product — a whodunnit, a twist short, a vertical hook piece. Give away the murderer at the midpoint of a fair-play mystery and you have no second half.
**Example:**
> Page 58: the letters in the attic are in her own handwriting. She wrote every one of them to herself, for nine years.
> Page 59: she burns none of them. She packs them, drives to her sister's, and puts them on the table.

**Yields to:** `info.mystery_audience_behind` — The reveal is the entire product.  
`info.midpoint_reveal`

### Information Asymmetry Between Characters

**Also called:** intra-character asymmetry, the uneven table, who-knows-what blocking
**What it is:** Two or more characters in a scene holding different pieces of the truth, none of them holding all of it — the audience watching the mismatch produce misunderstanding, manoeuvre or catastrophe.
**Effect on the audience:** Layered engagement. Rather than one gap to track, they hold several at once and enjoy the mechanics of the collision. This is the engine of both farce and tragedy, with only the consequences differing.
**Used for and where it works best:** The most underused tension source in dialogue scenes. Before writing any three-hander, assign each character exactly one thing they know and one thing they wrongly assume. The craft rule: let each character *act* on their wrong assumption rather than state it, and never let two characters explain themselves to each other unless the collapse of asymmetry is the point of the scene. Pairs directly with `dial.known_information` and `dial.exposition_correction` — a correction lands hardest when it destroys someone's operating assumption mid-manoeuvre. The scene's `scene.value_turn` is usually the moment one asymmetry closes.
**Best in:** formats: Stage Play, Feature Film, One-Hour Drama, Limited Series, Novel | genres: Comedy, Crime, Family Drama, Tragedy, Drama, Historical
**Avoid when:** The scene's job is emotional intimacy. Two people finally telling each other the truth is the payoff you have been building toward; asymmetry there is just a writer refusing to let a scene arrive.
**Example:**
> *She knows the company is folding. He knows she has been offered his job. Neither knows the other knows.*
> HE: I put your name forward. For the Cairo posting.
> SHE: That's generous.
> HE: I'd want it done properly, is all. A clean handover.
> SHE: There won't be anything to hand over.

`info.character_asymmetry`

---

## Fairness and the Cheat

### The Cheat

**Also called:** the withheld fact, the unearned twist, lying by omission, the authorial trick
**This is a named failure, not a recommendation.**
**What it is:** A reveal that depends on a fact the story never made available — not disguised, not reframed, simply absent — or on a narration that lied about something it had no reason to lie about. Named here so you can identify it in your own draft, because writers rarely see it from the inside.
**Effect on the audience:** Retrospective betrayal. They do not feel outsmarted, they feel cheated, and that feeling contaminates everything they enjoyed up to that point. It is the only failure in this category that damages the whole work rather than one scene.
**Used for and where it works best:** It does not work. The value of this card is the diagnostic. Three tests, run on every major reveal. One: could an exceptionally attentive audience member have reached this? If not, it is a cheat. Two: on a second pass, does every scene still play honestly, or does at least one require a character to behave in a way that made no sense at the time? Three: did a narrator or POV character silently omit something they were thinking about constantly? That last is the commonest cheat in first-person fiction and the hardest to forgive. The fix is never a late explanation — it is to go back and plant, using `info.buried_plant` and `info.double_meaning_clue`.
**Best in:** formats: — | genres: — (most damaging in Feature Film, Novel and Limited Series, and in Psychological, Mystery and Thriller, where the audience has invested most in reasoning)
**Avoid when:** Always — with one narrow exception: a story whose declared subject is the unreliability of storytelling itself, where the cheat is exposed *as* a cheat and becomes the theme. That is a hard trick and it fails far more often than it lands.
**Example:**
> *Cheat:* "What I didn't tell you — what I've never told anyone — is that I was holding the knife."
> *Fair, same twist:* Chapter 2: "My hands smelled of onions for two days and I scrubbed until they bled, which my wife found funny." Chapter 30: the knife was on the board with the onions, and only he had been at that board.

**Yields to:** `info.buried_plant` — The repair is to go back and plant (also double_meaning_clue).  
`info.the_cheat`

### The Fair-Play Contract

**Also called:** the detection club rules, Knox's decalogue, clue availability, the solvable mystery
**What it is:** The explicit promise that every fact required to solve the puzzle has been shown to the audience before the solution, in a form they could actually have used. Codified for detective fiction by Knox and Van Dine, but the underlying contract governs any twist.
**Effect on the audience:** Trust, which converts passive viewing into active play. A reader who believes the game is fair reads twice as hard — and reads the *next* thing you write.
**Used for and where it works best:** Binding in mystery and crime, and worth honouring in every genre that reverses. Practical implementation: before the final draft, list every fact the solution needs, then find the page number where each was made available and whether it was legible there. Anything with no page number is a repair job. The craft rule is about form, not mere presence: a clue "available" inside a paragraph of technical description is not available. Give it to a character to say, in a scene with heat, and let someone dismiss it. Knox's most useful surviving rule is the one about interiority — do not spend chapters inside the head of the person you intend to expose (`info.withheld_pov`).
**Best in:** formats: Novel, Limited Series, Feature Film, Podcast, Game Narrative | genres: Mystery, Crime, Noir, Thriller, Psychological
**Avoid when:** The piece is a psychological drama where "solving" is beside the point, or deliberately anti-solution literary work. Also: do not let the contract make you timid. Fair play sets the floor for what must be present, not a ceiling on how hard the puzzle may be.
**Example:**
> *Clue, page 40, inside an argument about something else:* "You can't even reach the top shelf, Mother, don't pretend."
> *Solution, page 260:* The poison was on the top shelf. She could not have reached it. Her son is six foot two, and he has been in that kitchen every Sunday for eleven years.

**Yields to:** `info.deliberate_unanswered_question` — Solving is beside the point.  
`info.fair_play_contract`

---

## Serial and Short-Form Reveals

### The Cliffhanger Reveal

**Also called:** the episode-out, the button, the act break, the hook-out
**What it is:** Placing a reveal in the last seconds of an episode or act, so the new information arrives with no time to process it and the story stops on an open question.
**Effect on the audience:** An unresolved information gap held across a gap in time — the most reliable continuation mechanism in serialised storytelling. They are not waiting for more story, they are waiting for an answer they already hold half of.
**Used for and where it works best:** Every episode out in a serialised drama, and every act break in commercial television. The craft rule: end on a *new question*, never on a new threat. "He's behind her" is a threat and it expires; "the man behind her is her brother" is a question and it compounds. Second rule: the reveal must concern a character the audience is currently invested in, not the plot at large — a revelation about the conspiracy pulls far less than one about the person we just spent forty minutes with. Third: pay it in the first ninety seconds of the next episode, not the last. Audiences punish a delayed cash-out harder than a weak hook.
**Best in:** formats: One-Hour Drama, Limited Series, Vertical Micro-Drama, Podcast, Game Narrative | genres: Crime, Thriller, Drama, Mystery, Social Drama, Science Fiction
**Avoid when:** The episode has an emotional resolution worth sitting in. Some episodes should end on quiet, and a series that buttons all ten the same way trains the audience to stop believing any of them.
**Example:**
> She opens the door. It is the detective, holding an evidence bag, and inside it is her son's phone.
> DETECTIVE: He said you'd want to explain it yourself.
> *Cut to black.*

**Yields to:** `end.quiet_ending` — The episode has an emotional resolution worth sitting in.  
`info.cliffhanger_reveal`

### The Micro-Reveal Ladder

**Also called:** stacked micro-cliffhangers, the short-form drip, beat-level reveals
**What it is:** Short-form structure in which small reveals arrive every fifteen to twenty-five seconds inside a single sixty-to-ninety second episode, rather than one reveal at the end.
**Effect on the audience:** Prevents mid-scroll drop-off. The viewer is repeatedly re-paid before their attention can migrate, and each small payment resets tolerance for the next wait.
**Used for and where it works best:** The core structural technique for vertical micro-drama and short-form serial, and increasingly for any platform-native piece under three minutes. The craft rule: two or three tension beats per ninety seconds, with the largest held for the final five. Each micro-reveal must change the viewer's understanding of a *relationship*, because relationships are the only thing that reads fast enough at this length — who is lying, who is related to whom, who owns what. Plot mechanics do not land in fifteen seconds. Second rule: no setup scene. The first reveal arrives before the eight-second mark or the piece is already lost, so open with `scene.late_entry` and let the ladder supply the context.
**Best in:** formats: Vertical Micro-Drama, Reels/Shorts, Short Film, Podcast | genres: Romance, Crime, Drama, Thriller, Family Drama, Comedy
**Avoid when:** You are writing long form. Imported wholesale into a feature, the ladder produces a film with no subtext and no scene longer than a minute — busy, exhausting, impossible to invest in. Also avoid where a slow burn is the product, such as heritage and historical work.
**Example:**
> 0:04 — "You're the new housekeeper?" "I'm the new wife."
> 0:26 — She unlocks a door with a key she should not have.
> 0:51 — The photograph in the drawer is her, aged nine, in this house.
> 1:08 — The woman on the stairs: "You came back."

**Yields to:** `info.staged_reveal` — Long form, or a slow burn is the product.  
`info.micro_reveal_ladder`

### The Cold-Open Reveal

**Also called:** open on the consequence, the flash-forward hook, in medias res reveal, the teaser
**What it is:** Beginning with a fragment of a later, more charged moment — an arrest, a body, a burning room — then cutting back to the ordinary beginning, so the audience watches the first act knowing where it arrives but not how.
**Effect on the audience:** Converts an inevitably slow setup into dramatic irony. Every mundane early scene is now read against a known destination, and the audience supplies tension you have not yet earned.
**Used for and where it works best:** The standard fix for a first act that is necessary but inert — biographical work, heritage and historical pieces, slow-build character drama, and any short whose premise takes thirty seconds to establish. The craft rule: the fragment must raise a *how* or *why*, never a *what*. Show her at the police desk with blood on her sleeve; do not show whose it is. Second rule: cut out of the fragment early — `scene.early_exit` applied to the whole device. The longer you play the teaser, the more of your climax you have spent. Third: when you return to that moment in full, it must play differently than it did cold, or the device was decoration.
**Best in:** formats: Feature Film, Limited Series, One-Hour Drama, Reels/Shorts, Short Film, Documentary | genres: Crime, Thriller, Drama, Historical, Noir, Social Drama
**Avoid when:** The story's pleasure is discovery of the premise — most comedy, most romance, most science fiction with a concept to unveil. Also avoid when the flash-forward gives away who survives: you can trade a mystery for irony, but do it knowingly, and never trade away the one question holding the piece up.
**Example:**
> Black. A woman's hands under a tap, the water running pink, and someone off-screen saying, "Leave it, leave it, they're here."
> CUT TO: TWO MONTHS EARLIER. She is signing a lease, and she is laughing, and the man beside her is holding the keys.

**Yields to:** `info.suspense_shared_knowledge` — The pleasure is discovery of the premise.  
`info.cold_open_reveal`

---

## Coverage

**This file contains exactly 32 cards.**

Covered here — the three information positions and the knowledge audit (5): `info.dramatic_irony`, `info.suspense_shared_knowledge`, `info.mystery_audience_behind`, `info.surprise`, `info.knowledge_ledger`. Plant, payoff and foreshadowing (6): `info.plant_and_payoff`, `info.chekhovs_gun`, `info.buried_plant`, `info.foreshadowing`, `info.telegraphing`, `info.rule_of_three_placements`. Misdirection and the false trail (4): `info.red_herring`, `info.double_meaning_clue`, `info.attention_misdirection`, `info.lesser_guilt`. Narration, point of view and inference (6): `info.unreliable_narrator`, `info.naive_narrator`, `info.withheld_pov`, `info.delayed_decoding`, `info.restricted_narration`, `info.audience_only_secret`. Reveal staging (6): `info.recontextualising_reveal`, `info.staged_reveal`, `info.double_reveal`, `info.reveal_lands_on_character`, `info.midpoint_reveal`, `info.character_asymmetry`. Fairness (2): `info.the_cheat`, `info.fair_play_contract`. Serial and short-form (3): `info.cliffhanger_reveal`, `info.micro_reveal_ladder`, `info.cold_open_reveal`.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Research conducted 2026-09-17.

- [Alfred Hitchcock and Francois Truffaut Explain Surprise vs. Suspense — No Film School](https://nofilmschool.com/alfred-hitchcock-and-francois-truffaut-explain-surprise-vs-suspense)
- [Narrative Drive: mystery, suspense and dramatic irony as information positions — Story Grid](https://storygrid.com/narrative-drive/)
- [Mystery versus Suspense: Do You Really Know the Difference? — Carol Potenza](https://carolpotenza.com/mystery-versus-suspense-do-you-really-know-the-difference/)
- [Inducing narrative tension in the viewer through suspense, surprise, and curiosity — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304422X22000262)
- [What is Dramatic Irony in Film? Definition, Examples & How To Use It — FilmDaft](https://filmdaft.com/how-to-use-dramatic-irony-in-film/)
- [Chekhov's Gun: The Art of the Plant and Payoff — Backstage](https://www.backstage.com/magazine/article/chekhovs-gun-explained-examples-75529/)
- [What is Chekhov's Gun? 5 Ways to Skilfully Use One in Your Screenplay — Industrial Scripts](https://industrialscripts.com/chekhovs-gun/)
- [Chekhov's Gun, Foreshadowing & the Secret of Tension — Sudowrite](https://sudowrite.com/blog/chekhovs-gun-foreshadowing-the-secret-of-tension-you-cant-look-away-from/)
- [Red Herrings: How to Mislead and Surprise Readers — Story Grid](https://storygrid.com/red-herrings/)
- [Mastering Misdirection: Red Herring Examples — Sudowrite](https://sudowrite.com/blog/mastering-misdirection-20-red-herring-examples-to-fool-your-readers-every-time/)
- [Literary Misdirection: Using Reader Expectations Against Them — Writer's Digest](https://www.writersdigest.com/literary-misdirection-using-reader-expectations-against-them)
- [5 Storytelling Tricks Movies Use to Surprise the Audience — No Film School](https://nofilmschool.com/storytelling-tricks-movies-use-to-surprise-the-audience)
- [Withholding Information is Not a Good Writing Technique — Vera Kurian](https://medium.com/@verakurian/withholding-information-is-not-a-good-writing-technique-994caf6a0761)
- [Reveal (narrative) — Wikipedia](https://en.wikipedia.org/wiki/Reveal_(narrative))
- [Unreliable narrator — Wikipedia](https://en.wikipedia.org/wiki/Unreliable_narrator)
- [When the Narrator Doesn't Get It: 10 Shades of Deception — CrimeReads](https://crimereads.com/when-the-narrator-doesnt-get-it-10-shades-of-deception/)
- [Ronald Knox: 10 Commandments of Detective Fiction — Gotham Writers Workshop](https://www.writingclasses.com/toolbox/tips-masters/ronald-knox-10-commandments-of-detective-fiction)
- [The "Rules" of Detective Fiction (Knox and Van Dine) — Agatha Christie Wiki](https://agathachristie.fandom.com/wiki/The_%E2%80%9CRules%E2%80%9D_of_Detective_Fiction)
- [Fair-Play Mystery Clues and Solution Audit — NovelOS](https://novelos.studio/blog/fair-play-mystery/)
- [Viewer-character information asymmetry as a cultural-creative strategy in global cinema — Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/25785273.2026.2714690)
- [Point of View in Film: Definition, Types & Movie Examples — FilmDaft](https://filmdaft.com/point-of-view-in-film-meaning-definition-examples/)
- [What are Verticals and Micro-Dramas? — Final Draft](https://www.finaldraft.com/blog/what-are-verticals-and-micro-dramas)
- [Vertical Dramas: The Mobile-First Format Changing Serialized Screen Storytelling — Stage and Cinema](https://stageandcinema.com/2026/05/01/mobile-first-format-changing-storytelling/)
- [What Are The Characteristics Of Vertical Micro Dramas — Film Threat](https://filmthreat.com/features/what-are-the-characteristics-of-vertical-micro-dramas-key-insights-on-length-and-format/)
