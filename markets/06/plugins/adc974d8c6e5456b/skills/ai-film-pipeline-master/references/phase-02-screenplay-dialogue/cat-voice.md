# Voice, Register and Narrative Authority

Category: `voice`

**Part 1 of 2.** 32 cards across the narrating persona, register and diction, authority and its instability, institutional and non-human voices, irony and understatement, dialect and code-switching, and voice in production.

Voice is not style and it is not tone. Style is the writer's habits, tone is the mood of a passage, voice is *who is allowed to speak here and with what authority*. This file covers that last thing. Dialogue technique lives in `cat-dial.md`; the mechanics of who sees and what they can know live in the POV file.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [The Narrating Persona](#the-narrating-persona)
- [Register and Diction](#register-and-diction)
- [Authority and Its Instability](#authority-and-its-instability)
- [Institutional, Ceremonial and Non-Human Voices](#institutional-ceremonial-and-non-human-voices)
- [Irony, Understatement and Comic Register](#irony-understatement-and-comic-register)
- [Dialect, Translation and Code-Switching](#dialect-translation-and-code-switching)
- [Voice in Production](#voice-in-production)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## The Narrating Persona

### The Narrating Persona

**Also called:** the teller, narrative persona, the voice behind the voice
**What it is:** Deciding who is telling this, to whom, from what distance in time, and with what stake — before you write a line. Every sentence afterwards inherits those four answers.
**Effect on the audience:** The reader stops reading prose and starts listening to someone. Trust, patience and interest attach to a person; they do not attach to information.
**Used for and where it works best:** First move on anything longer than a page, and the thing to fix when a draft is technically clean and dead on the page. The craft rule: write the persona as four answers on one card — who / to whom / how long after / why they are bothering to tell it — and flag any sentence that could not have come from that card. "Why they are bothering" is the answer most writers skip, and it is the one that produces voice; a narrator with no reason to speak produces prose with no pressure in it.
**Best in:** formats: novel, memoir, essay, documentary VO, podcast | genres: literary, memoir, historical, true crime
**Avoid when:** The piece is a reference document, a spec, a legal notice or an API doc. There a personality in the prose is noise the reader has to filter out before they can get at the fact.
**Example:**
> Persona card: a retired coroner, telling a young reporter, thirty years after, because the official file is wrong.
> "They wrote drowning. I signed it. You should know what a drowned man's hands look like, and his didn't."

**Yields to:** `voice.suppressing_your_voice` — Reference doc, spec, legal notice, API doc.  
`voice.narrating_persona`

---

### The Psychic Distance Ladder

**Also called:** narrative distance, authorial distance, Gardner's ladder, camera height
**What it is:** A graded scale running from the wide historical summarising sentence down to a sentence made of nothing but the character's own interior words — and the deliberate choice of which rung you are standing on in any given paragraph.
**Effect on the audience:** Distance decides whether the reader assesses the character or *is* the character. High rungs let them judge; low rungs strap them in and remove the exit.
**Used for and where it works best:** Shape a scene with it, not a book. Come in high to place the reader, step down one rung at a time toward the moment that hurts, then stay down. The craft rule: never move more than one rung inside a paragraph, and never step down and back up in the same beat — the reader reads the retreat as the author losing nerve, which is usually exactly what it is.
**Best in:** formats: novel, short story, screenplay | genres: literary, drama, thriller, horror
**Avoid when:** Tight comic writing and fast commercial chapters, where holding one rung for a whole scene reads as confidence and visible ladder work reads as dithering.
**Example:**
> It was January, and the town had been cold for eleven days.
> Henry Cole walked down to the river with his coat open.
> The coat was open because his hands would not do buttons any more.
> Buttons. Forty years of other people's buttons and now this.

**Yields to:** `voice.free_indirect_style` — Tight comic or fast commercial; hold one rung instead.  
`voice.psychic_distance_ladder`

---

### Free Indirect Style

**Also called:** free indirect discourse, FID, close third, deep POV
**What it is:** Third-person grammar carrying first-person idiom. The narration keeps "he" and "she" and the past tense but borrows the character's vocabulary, priorities and judgements, with no reporting clause attached.
**Effect on the audience:** The reader is inside the head without being told they are inside the head. It is the cheapest intimacy in prose because it costs no machinery.
**Used for and where it works best:** The main engine for closing distance in third person, and the correct default for most contemporary commercial and literary fiction. The craft rule: the tell is an evaluative word no neutral narrator would use — *of course*, *vulgar*, *bloody typical* — and then you delete the thought tag entirely. The tag is what pushes the reader back out; keeping both is writing the technique and its safety net at the same time.
**Best in:** formats: novel, short story, serialised fiction | genres: literary, domestic drama, comedy of manners, crime
**Avoid when:** The narrator is meant to hold authority independent of the character — a moral witness, an ironic historian, a narrator whose function is to know better. Also avoid mixing it with omniscient judgement in the same paragraph: the reader cannot tell whose opinion is on offer, and that ambiguity is a bug unless you designed it as `info.unreliable_narrator`.
**Example:**
> Tagged: She looked at the cake and thought it was a vulgar cake.
> Free indirect: She looked at the cake. Three tiers. Of course three tiers, from a woman who had never once in her life known when to stop.

**Yields to:** `voice.psychic_distance_ladder` — Narrator must hold authority independent of the character.  
`voice.free_indirect_style`

---

### The Confiding Voice

**Also called:** the intimate address, told-in-confidence, buttonholing
**What it is:** A narrator who speaks as though to one listener across a table, and who admits slightly more than the occasion requires.
**Effect on the audience:** The reader is promoted from audience to confidant, and a confidant forgives a great deal — digression, unlikeability, slow plot.
**Used for and where it works best:** Openings, memoir, first-person crime, VO-led documentary. It pairs directly with `open.voice_hook`. The craft rule: intimacy is bought with one small admission against the narrator's own interest inside the first hundred words. It is not bought with the word "you", and it is never bought by announcing that the narrator is being honest.
**Best in:** formats: memoir, novel, personal essay, podcast, VO | genres: memoir, literary, comedy, true crime
**Avoid when:** The piece needs the reader to judge the narrator coldly — confiding buys sympathy you may not want to spend later. And it fails instantly in corporate copy: manufactured intimacy from an institution reads as a sales move, because it is one.
**Example:**
> "I have told this story at dinner parties for eleven years and I always get the same laugh in the same place. I want to tell it properly once, because the laugh is in the wrong place."

**Yields to:** `voice.authority_by_specificity` — Reader must judge coldly, or institutional copy.  
`voice.confiding_voice`

---

### The Retrospective Narrator

**Also called:** the looking-back voice, double vision, older-self narration
**What it is:** The story told by a version of the character far enough along to know how it ended, so two voices run at once — the self who acted and the self who now judges that acting.
**Effect on the audience:** Dramatic irony without a plot device. Everything in the scene is shadowed by the sense that it has already been decided.
**Used for and where it works best:** Coming-of-age, memoir, confessional crime, heritage VO. The craft rule: the later self must pay rent. Every intrusion has to supply information or a judgement the younger self could not have had. If the line only restates what the scene already showed, cut it — that is the failure mode of ninety percent of retrospective narration.
**Best in:** formats: memoir, novel, feature film, documentary | genres: coming-of-age, memoir, literary, war
**Avoid when:** The suspense depends on whether the narrator survives or breaks. A narrator who lived to tell it has already capped your jeopardy, and no amount of tension writing buys it back.
**Example:**
> "I thought he was being kind. I was fourteen, and I thought a lot of things were kindness."

**Yields to:** `voice.free_indirect_style` — Suspense depends on whether the narrator survives.  
`voice.retrospective_narrator`

---

### Narrator Voice Against Character Voice

**Also called:** the voice separation test, who is speaking here
**What it is:** Keeping the narration's diction measurably different from every character's diction, so the reader always knows which authority is currently on the page.
**Effect on the audience:** Characters come off the page as separate people instead of one person in several costumes. When it fails the reader cannot say why the book feels thin — they just feel it.
**Used for and where it works best:** Any first person or close third with more than two strong speakers, and every ensemble screenplay. The craft rule: run the separation test — strip the tags and attributions from three pages and hand them to someone else. If they cannot sort narration from dialogue, or one character from another, you have one voice wearing hats. `dial.clipped_line` and `dial.rapid_fire` are the dialogue-side levers; `voice.lexical_field` is the narration-side one.
**Best in:** formats: novel, ensemble feature, audio drama | genres: all
**Avoid when:** A first-person narrator who is meant to sound exactly as they talk. There narration and dialogue *should* match, and forcing separation makes one person sound like two. The same holds in close third written in free indirect style (`voice.free_indirect_style`), where the narration borrows the focal character's idiom by design: there the test sorts the narration from every other character, not from the one it is inside.
**Example:**
> Narration: The kitchen had been repainted, badly, in a yellow that would not have survived a second opinion.
> The same man, aloud: "Yeah, I did the kitchen. Yellow. Don't start."

**Yields to:** `voice.confiding_voice` — First-person narrator meant to sound exactly as they talk; and `voice.free_indirect_style` — close third that borrows the focal character's idiom by design.  
`voice.narrator_vs_character`

---

## Register and Diction

### Setting the Register

**Also called:** pitching the voice, formality band
**What it is:** Choosing the formality band — ceremonial, formal, neutral, colloquial, slang — and understanding that the band, not any individual word, is what the reader actually hears.
**Effect on the audience:** In one sentence the reader learns what kind of thing they are holding and how seriously to take it, and they will resist any later evidence that contradicts it.
**Used for and where it works best:** Every piece, decided in the first paragraph. The craft rule: pick the band, then write your three test words in it — a verb for moving, a noun for money, a verb for dying — and pin them above the draft. Register breaks show up in those three before they show up anywhere else.
**Best in:** formats: all | genres: all
**Avoid when:** You are still discovering the material. Pinning a register in a genuinely exploratory first draft can lock you out of the voice the material wanted. Set it on the second pass, from the best page of the first — taking its band, not its cadence, which `rhythm.first_draft_cadence` decides before drafting because an unsupervised first draft falls into the writer's resting rhythm, not the material's.
**Example:**
> Ceremonial: He was carried from the field and did not rise again.
> Neutral: He died on the way to the hospital.
> Colloquial: He didn't make it.

`voice.register_setting`

---

### The Diction Shift

**Also called:** register break, the deliberate wrong word
**What it is:** Holding one register long enough to build an expectation, then placing a single word from a different band.
**Effect on the audience:** The shifted word carries more weight than any amount of emphasis could give it. The floor moves under one syllable.
**Used for and where it works best:** The exact sentence where the emotional truth arrives, and the punchline of a comic paragraph. The craft rule: one word, not a clause, and never twice on the same page — the second break tells the reader the first was an accident rather than a decision.
**Best in:** formats: literary fiction, essay, speeches, lyric | genres: literary, comedy, drama, satire
**Avoid when:** The surrounding register is not established yet. A break on page one is not a break, it is inconsistency. And never in instructional or technical writing, where the reader takes it for a typo and loses the step.
**Example:**
> "The committee reviewed the submissions, weighed the evidence, considered the precedent, and then did the stupid thing anyway."

`voice.diction_shift`

---

### Latinate Against Anglo-Saxon

**Also called:** the two vocabularies, Germanic versus Romance diction
**What it is:** English keeps two words for most things — a short blunt one from Old English and a long abstract one from Latin or French. Choosing between them sets the temperature of the sentence.
**Effect on the audience:** Anglo-Saxon words land on the body; Latinate words land on the mind. *He bled* and *he sustained a haemorrhage* describe one event and produce two different readers.
**Used for and where it works best:** Wherever you want physical impact, and equally wherever you want clinical distance as characterisation or as institutional camouflage. The craft rule: put the Latinate words in the part of the sentence that describes systems and the Anglo-Saxon words in the part that describes bodies, then let the collision carry the argument without stating it.
**Best in:** formats: prose, speeches, VO, journalism | genres: war, political, medical drama, satire, literary
**Avoid when:** You are blanket-applying "always use short words". In a legal, scientific or bureaucratic narrator the Latinate register *is* the characterisation, and simplifying it deletes the person you were writing.
**Example:**
> "The operation resulted in the neutralisation of four individuals."
> He meant they shot a family in a car.

**Yields to:** `voice.legal_register` — Legal or bureaucratic narrator whose Latinate diction is characterisation.  
`voice.latinate_vs_anglo`

---

### The Lexical Field

**Also called:** occupational vocabulary, the metaphor source, what the voice reaches for
**What it is:** Giving a voice one consistent well — the sea, the kitchen, the courtroom, the farm, the ward — and drawing all its comparisons and idioms from it.
**Effect on the audience:** The reader learns who this person is without a paragraph of biography, and the voice acquires a texture no adjective can fake.
**Used for and where it works best:** First person, close third, and every brand or institutional voice. The craft rule: a voice's metaphors must come from what the speaker has physically handled. A fisherman does not compare a storm to a symphony. It pairs directly with `char.what_they_notice` — the field decides both what gets seen and what it gets compared to.
**Best in:** formats: novel, monologue, VO, brand film | genres: literary, historical, crime, workplace drama
**Avoid when:** The field is specialised enough that the reader needs a gloss to feel the comparison. Then the image fails and only the flavour survives. Cap it at roughly one field-specific image per page and let the syntax carry the rest.
**Example:**
> The nurse, on her brother-in-law: "He talked for forty minutes and I kept waiting for him to get to the bleed."

**Yields to:** `voice.sentence_rhythm` — Field too specialised to feel; let syntax carry it.  
`voice.lexical_field`

---

### Sentence Rhythm as Voice

**Also called:** the prose signature, cadence, sentence-length pattern
**What it is:** The voice's characteristic sentence length and, more importantly, its pattern of variation — where it runs long, where it stops dead.
**Effect on the audience:** Rhythm is heard before meaning is understood. A voice with no rhythm reads as competent and is forgotten within a day.
**Used for and where it works best:** Every draft, on the pass after the argument is right. The craft rule: write the paragraph, then count the words in each sentence and look at the numbers. If they all cluster within a few words of each other, the voice is flat. A real voice shows a spread, and the shortest sentence sits next to the longest one. Then read it aloud — the tongue finds what the eye forgives.
**Best in:** formats: all prose, VO, speeches, lyrics | genres: all
**Avoid when:** The thought underneath is not finished. Cadence work on a paragraph that says the wrong thing is wasted labour, and beautifully rhythmic long prose is the easiest place in writing to hide an idea you have not actually had.
**Example:**
> Flat (18, 22, 19, 21): The room was warm and the windows had been open since morning, and someone had left a glass on the sill where the light came through it.
> Shaped (26, 3): He had been in that room every day of his life since the year his father died, and in all that time he had never once looked at the glass. He looked now.

`voice.sentence_rhythm`

---

### Register Creep

**Also called:** author intrusion by vocabulary, the essay voice leaking in
**This is a named failure, not a recommendation.**
**What it is:** The narration's register drifting upward toward the writer's own analytical voice whenever the writer becomes more interested in the idea than in the scene.
**Effect on the audience:** The reader feels the author walk into the room. Trust in the persona drops and does not fully come back, because they now know there is someone behind it.
**Used for and where it works best:** Diagnosis only. It shows up most in third paragraphs and in the passages the writer is proudest of. The craft rule: the flag phrases are *essentially*, *a kind of*, *the very idea that*, *which is to say*, *something like*. Search for them. Almost every hit marks a place where the writer stopped being the narrator and started being clever.
**Best in:** formats: — | genres: —
**Avoid when:** Do not "fix" abstraction in a narrator whose job is to think on the page. An essayistic or omniscient voice is entitled to its analysis. Judge each hit against the persona card, never against the word list alone.
**Example:**
> Crept: She poured the tea, which is to say she performed the small ritual by which the household maintained its fiction of order.
> Held: She poured the tea. Nobody in that house had ever once said what was wrong.

**Yields to:** `voice.essayistic_voice` — A narrator whose job is thinking on the page.  
`voice.register_creep`

---

## Authority and Its Instability

### Unstable Authority

**Also called:** cracked narration, the narrator you start to doubt
**What it is:** Narration that keeps every outward form of a reliable account while leaking evidence — a contradiction, an over-precision, a detail told twice differently — that the teller cannot be fully trusted.
**Effect on the audience:** The reader begins reading *against* the narrator, which converts passive reading into detective work and roughly doubles their attention.
**Used for and where it works best:** Stories whose real subject is self-deception. The craft rule: the leaks must be verifiable inside the text — a date that moves, a wound that changes sides, a name the narrator says he never knew and then uses. Three planted contradictions is usually enough, and the first should read as a slip and only later as a lie. This card is the *sound* of it; `info.unreliable_narrator` is the information architecture underneath.
**Best in:** formats: novel, short story, VO | genres: psychological thriller, literary, noir, horror
**Avoid when:** The reader needs stable ground for another reason — a procedural where the facts are the pleasure, or children's content, where a narrator who might be lying is not delicious, only confusing. For children the honest version is `info.naive_narrator`: a teller who is wrong without meaning to be.
**Example:**
> "I was not angry. I want that understood. I have said so to everyone who asked, and to several people who did not."

**Yields to:** `info.naive_narrator` — Children's content, where a lying narrator only confuses.  
`voice.unstable_authority`

---

### The Hedge

**Also called:** epistemic marking, calibrated uncertainty, "as far as I know"
**What it is:** Letting the voice mark how sure it is — *I think*, *the records say*, *she told me this later* — instead of narrating everything at one flat certainty.
**Effect on the audience:** It raises trust rather than lowering it. A voice that admits the edge of its knowledge gets believed about the middle of it.
**Used for and where it works best:** Documentary VO, memoir, history, narrative journalism — anything non-fiction with real gaps in it. The craft rule: hedge the specific claim, never the paragraph. "He was, I think, about forty" is a working hedge. "Some of this may be wrong" is an abdication that voids everything after it. Where the gap is tactical rather than honest, you want `dial.strategic_withholding` instead.
**Best in:** formats: documentary VO, memoir, essay, journalism, podcast | genres: history, true crime, memoir, science
**Avoid when:** In an omniscient fictional narrator, hedging is simply weak writing — if the narrator can know, they should say. In advertising and instructional copy it reads as the writer covering themselves, and nobody follows an instruction they suspect you doubt.
**Example:**
> Flat: The city fell in three days.
> Hedged: The chronicle says three days. The chronicle was written by the men who took it.

**Yields to:** `dial.strategic_withholding` — The gap is tactical rather than honest.  
`voice.the_hedge`

---

### Authority by Specificity

**Also called:** earned expertise, the load-bearing detail
**What it is:** Establishing the narrator's right to speak by producing one exact, unshowy detail that only someone who was actually there would still be carrying.
**Effect on the audience:** Authority is granted instantly and retroactively — everything before and after the detail is now covered by it.
**Used for and where it works best:** The opening of any expert-narrator non-fiction, and the first page of first-person fiction. The craft rule: the detail must be useless to the plot. A fact the story needs reads as setup; a fact the story does not need reads as memory, and memory is the thing you are trying to prove.
**Best in:** formats: memoir, documentary VO, journalism, novel | genres: war, medical, procedural, historical
**Avoid when:** You cannot source it. Invented specificity in non-fiction is the fastest permanent way to lose a reader, and one wrong technical detail in front of a specialist audience retroactively destroys every true thing standing near it.
**Example:**
> "The ward smelled of the orange hand-gel they stopped buying in 2011."

**Yields to:** `voice.the_hedge` — You cannot source the detail; mark the uncertainty.  
`voice.authority_by_specificity`

---

### The Self-Correcting Narrator

**Also called:** revision on the page, "no — that's not it"
**What it is:** A narrator who visibly amends their own sentence, leaving the first version standing.
**Effect on the audience:** The reader watches a thought happen. The corrected version arrives with more force because they saw it chosen over the comfortable one.
**Used for and where it works best:** Memoir, confession, and any moment where the plain account is a lie the narrator cannot hold for a whole sentence. The craft rule: correct toward the more damaging version, never the more flattering one. A narrator who revises himself upward is performing humility, and readers smell that instantly.
**Best in:** formats: memoir, novel, monologue, personal essay | genres: memoir, literary, comedy
**Avoid when:** More than two or three times in a piece. Past that it becomes a tic and reads as a style rather than a struggle. Never in VO or instructional copy that has to be understood on one pass.
**Example:**
> "He asked me to come and I was busy. I wasn't busy. I didn't want to see what he looked like."

**Yields to:** `voice.write_for_the_ear` — VO or instructional copy understood on one pass.  
`voice.self_correcting_narrator`

---

## Institutional, Ceremonial and Non-Human Voices

### The Institutional Voice

**Also called:** bureaucratese, the agentless register, corporate passive
**What it is:** Writing in the register organisations use to describe themselves: passive constructions, nominalisations, and no responsible human being anywhere in the sentence.
**Effect on the audience:** Chilling, when set beside a human voice. The reader hears a system declining to have a body.
**Used for and where it works best:** Satire, dystopia, war, corporate and medical drama — any story about a person against a process. The craft rule: it only works in contrast. One paragraph of it against one plain sentence about one person. Run it alone for pages and it simply becomes unreadable, which may be thematically true but is not an effect.
**Best in:** formats: novel, film, sketch | genres: dystopia, political, satire, workplace, war
**Avoid when:** You are the institution and you meant to be trusted. In your own brand or public-service copy this register is the thing you are escaping, not a tool.
**Example:**
> "A decision was taken that the facility would no longer be resourced at previous levels."
> Marta read it twice, then went out to tell eleven people they had no jobs.

**Yields to:** `rhythm.legal_sentence` — You are the institution and want to be understood.  
`voice.institutional_voice`

---

### The Found Document

**Also called:** epistolary register, documentary insert, in-world text
**What it is:** Breaking the narration to present an object from inside the world — a letter, an incident report, a transcript, a school essay, a receipt — written in its own correct register.
**Effect on the audience:** They believe it more than they believe the narration, because nobody in it appears to be selling anything.
**Used for and where it works best:** Delivering information the narrator cannot or will not give, which makes it the natural partner of `info.restricted_narration`. The craft rule: the document must be formally right down to its furniture — reference numbers, the date format of its era, the sign-off, the letterhead phrasing — and it must contain exactly one thing its author did not intend to reveal.
**Best in:** formats: novel, ARG, podcast, documentary | genres: horror, mystery, historical, sci-fi, literary
**Avoid when:** The document is doing work a scene would do better; readers skim inserts, and they skim harder each time. It is also risky past a page — a stiff in-world register that long and the audience stops decoding and starts scanning for the next line of narration.
**Example:**
> "INCIDENT REPORT 114-B. Three of four team members accounted for. Weather conditions as previously reported. Recommend no further deployment at this location. Recommend this report not be circulated."

`voice.found_document`

---

### The Incantatory Register

**Also called:** liturgical voice, ceremonial register, the invocation
**What it is:** Prose built on repetition, parallel clauses and a deliberately simple grammar, so it scans as ritual speech rather than as description.
**Effect on the audience:** It slows their breathing. An ordinary statement starts to feel like something that has been said before and will be said again after everyone present is dead.
**Used for and where it works best:** Openings and endings of mythic, heritage and ceremonial pieces; oaths, curses, blessings, the naming of the dead. The craft rule: the engine is anaphora and a three-beat clause, not archaic vocabulary. You can get the entire effect with plain modern words — *thee* and *hath* buy nothing but costume, and a modern audience hears pastiche.
**Best in:** formats: VO, novel, poetry, live event, heritage documentary | genres: myth, epic, fantasy, historical, religious
**Avoid when:** Modern realist scenes, where it reads as pretension. And never run it past about ninety seconds of continuous VO — the ear stops parsing repetition as meaning and starts hearing it as music, which is a pleasant way to understand nothing.
**Example:**
> "They took the river. They took the grain. They took the names of the streets, and then they took the streets."

**Yields to:** `voice.liturgical_register` — Modern realist scenes, where incantation reads as pretension.  
`voice.incantatory_register`

---

### The Voice of a Place or an Object

**Also called:** non-human narrator, prosopopoeia, the house speaks
**What it is:** Assigning the narration to a city, a river, a house, a coat — something whose time-scale and interests are not human.
**Effect on the audience:** Centuries compress without a summary paragraph, and human urgency is made to look small, which is usually the entire argument of the piece.
**Used for and where it works best:** Heritage, generational and ecological stories; anything where a human lifespan is too short for the subject. The craft rule: the narrator's limits must derive from what it physically is. A house cannot follow anyone outdoors. A river knows only what floats. Those limits *are* the voice — a non-human narrator that happens to know everything is just omniscience wearing a hat.
**Best in:** formats: literary fiction, heritage documentary, picture book, short film | genres: literary, historical, nature, children's, magical realism
**Avoid when:** The story needs interior psychology from a character. An object can only infer, and long stretches of inference are thin. It also goes twee in commercial work faster than almost any other device.
**Example:**
> "I have been a granary, a barracks, a school, and a granary again. The children were the loudest and stayed the shortest time."

**Yields to:** `voice.free_indirect_style` — The story needs interior psychology from a character.  
`voice.voice_of_a_place`

---

### The Collective We

**Also called:** first-person plural, the chorus narrator, the town speaks
**What it is:** Narration by an undefined group — a class, a town, a crew, a generation — that observes and judges together and never fully resolves into individuals.
**Effect on the audience:** Unsettling in a productive way. The modern reader keeps hunting for the single consciousness behind it and cannot find one, and that hunt is the experience.
**Used for and where it works best:** Stories about how a group builds and defends a shared misunderstanding — a neighbourhood's version of a death, a school's version of a girl, a country's version of a war. The craft rule: the "we" must be capable of being wrong *as a group*, and the story should be impossible to tell any other way. Define its edges early — who is inside it, who is outside — because an undefined "we" reads as evasion. Give it one moment where an "I" almost escapes and is pulled back.
**Best in:** formats: novel, short story, VO, documentary | genres: literary, historical, gothic, satire
**Avoid when:** You need interiority or a personal arc. The collective voice flattens individual quirk by design and cannot carry `arc.the_lie` for one person. It also turns gimmicky fast when it is chosen for novelty rather than because the subject is genuinely collective.
**Example:**
> "We agreed, afterwards, that we had always known. None of us had said so at the time, and we did not hold that against each other."

**Yields to:** `voice.free_indirect_style` — You need interiority or one person's arc.  
`voice.collective_we`

---

## Irony, Understatement and Comic Register

### The Understating Voice

**Also called:** flat register, deadpan narration, restraint; litotes when it works by negation
**What it is:** Describing a catastrophe in mild, unemphatic language so the gap between the event and the wording does all the work. Litotes is the negated form of the same move — *not an easy neighbour*, of a man who has killed sixty people.
**Effect on the audience:** The reader supplies the emotion themselves, and nobody argues with a feeling they generated. It also characterises the teller as someone with something to hold in.
**Used for and where it works best:** Grief, violence, disaster, and the driest comedy. The craft rule: strip the intensifiers and the emotion-naming words and let the fact stand alone. If you have written *unbearable*, you have done the reader's job for them and they will resent it.
**Best in:** formats: prose, VO, journalism | genres: war, literary, comedy, noir, crime
**Avoid when:** The audience does not yet know the event is a catastrophe — understatement only works over information they already hold. It is also weak across translation: litotes in particular collapses into literal meaning in subtitles, so if the piece will be subtitled, build the flat register out of plain statements rather than negations.
**Example:**
> "The house had gone, and most of the street with it. Mrs Nasser said she would need somewhere to put the shopping."

**Yields to:** `rhythm.write_for_translator` — Subtitled or translated work, where litotes collapses.  
`voice.understating_voice`

---

### Mock Formality

**Also called:** mock-heroic, the elevated trivial, bathetic register
**What it is:** Applying a grand, ceremonial, military or technical register to something completely small.
**Effect on the audience:** Comic, and quietly affectionate — the joke lives in the register rather than in the event, so nobody in the scene is being mocked.
**Used for and where it works best:** Domestic comedy, family memoir, children's writing, and brand voice with a light hand. The craft rule: play the register absolutely straight. One wink — *if I may be dramatic* — kills it outright. And always elevate the trivial rather than deflating the serious; the other direction reads as contempt no matter what you intended.
**Best in:** formats: novel, VO, sketch, advertising, kids story | genres: comedy, children's, satire, memoir
**Avoid when:** The subject is a real loss or a real injustice. Bathos applied to genuine suffering lands as sneering, and the audience will not give you the benefit of the doubt.
**Example:**
> "At oh-seven-hundred the cat took the stairs, secured the landing, and held it for the remainder of the day against a force of two adults and a delivery man."

**Yields to:** `voice.understating_voice` — The subject is a real loss or injustice.  
`voice.mock_formality`

---

### Tonal Whiplash

**Also called:** the unearned gear-change, comedy-drama collision
**This is a named failure, not a recommendation.**
**What it is:** Swinging between comic and serious register without preparing the audience for the move.
**Effect on the audience:** They stop trusting the piece and start holding back emotionally, because they have just learned they may be about to be embarrassed for caring.
**Used for and where it works best:** Diagnosis. The craft rule: a register change needs a transition object — a beat of silence, a scene break, or one line that honestly belongs to both tones. The fix is almost never to cut the comedy; it is to give the audience half a second of warning. Note the difference from `voice.diction_shift`: that is one word inside a held register, and the jolt is the design.
**Best in:** formats: — | genres: —
**Avoid when:** In tragicomedy and horror-comedy the collision is the form, and there the rule inverts — the whiplash must be constant from page one so the audience calibrates early. What fails is the single unprepared swerve inside an otherwise stable piece.
**Example:**
> Whiplash: The chemo made her funny in a way she'd never been. Anyway, the parking at that hospital is a scandal.
> Prepared: The chemo made her funny in a way she'd never been. We laughed in the car park for a long time. It is a terrible car park. We were not really laughing about the car park.

**Yields to:** `voice.diction_shift` — You wanted a designed jolt inside a held register.  
`voice.tonal_whiplash`

---

## Dialect, Translation and Code-Switching

### Dialect by Syntax

**Also called:** dialect without phonetic spelling, rhythm-first dialect
**What it is:** Rendering a regional or social way of speaking through word order, idiom, verb forms and cadence, while spelling every word normally.
**Effect on the audience:** They hear the accent without doing any decoding work, and the voice reads as a person rather than as a performance of a person.
**Used for and where it works best:** Any character or narrator from a specific place, which is most of them. The craft rule: make the minimum change that carries the effect. "I'm telling you now", placed where that speaker would place it, does more than "Ah'm tellin' ya" and costs the reader nothing. Add one or two genuine regional idioms per scene and then stop. Research the culture, not only the sounds — the idiom is where the place actually lives.
**Best in:** formats: novel, screenplay, audio drama, VO | genres: all, literary, historical, crime
**Avoid when:** You do not know the speech community from the inside or from real research. The failure is not inaccuracy, it is that a half-known dialect reproduces only its most stereotyped features. Then check the distribution across the whole draft: if every low-prestige speaker is a fool, a victim or a villain and every standard-English speaker is not, the dialect is not the problem, the casting is.
**Example:**
> Phonetic: "Ah dinnae ken whit yer on aboot, son."
> Syntactic: "I don't know what you're on about, son, and I've a feeling you don't either."

`voice.dialect_by_syntax`

---

### Eye Dialect

**Also called:** respelling, phonetic caricature, "wuz" and "sez"
**This is a named failure, not a recommendation.**
**What it is:** Respelling words to signal accent when the respelling does not change the pronunciation at all — *wuz* for was, *sez* for says, *enuff* for enough. Everyone says "wuz".
**Effect on the audience:** It carries no sound information, so all it can carry is class. The reader is told the character is uneducated, in the narrator's own spelling, by a writer who has arranged to be the only person on the page spelling correctly.
**Used for and where it works best:** Diagnosis. The craft rule: separate the two things being conflated. Genuine phonetic notation — *gonna*, a dropped g, a clipped vowel — can earn a small place. Eye dialect proper, the respelling of a standard pronunciation, never does. Practical test: count the apostrophes in a page of dialogue; past a handful the page is unreadable regardless of intent.
**Best in:** formats: — | genres: —
**Avoid when:** Period pastiche that is deliberately quoting the convention, and single affectations belonging to one specific character, are both legitimate. Where the respelling marks a character's accent rather than an affectation, `dial.phonetic_accent_spelling` governs, and it allows one word, once, where the mispronunciation is the plot. The failure is the systematic respelling of one group's speech while another group's is left clean.
**Example:**
> Eye dialect: "I sez to him, I sez, that wuz enuff."
> Fixed: "I said to him, I said, that's enough now."

**Yields to:** `voice.dialect_by_syntax` — Rendering a real accent without respelling anyone.  
`voice.eye_dialect`

---

### Code-Switching

**Also called:** selective lexical fidelity, bilingual voice, macaronic writing
**What it is:** Moving between two languages inside one voice and leaving some words untranslated, because translating them would destroy what they mean to the speaker.
**Effect on the audience:** Recognition for the bilingual reader; for the monolingual reader, a deliberate and productive sense of standing slightly outside a room they are being allowed into anyway.
**Used for and where it works best:** Diaspora, migration and family stories, and any voice whose interior language is not the language of the page. The craft rule: never gloss in line. "She called me habibti, which means my love" converts a living word into a footnote and tells the reader they are a guest. Carry the meaning in the surrounding action, or let it stay unresolved. Switch where real speakers switch: emotion, food, insults, family, prayer, money.
**Best in:** formats: novel, poetry, memoir, screenplay, song | genres: literary, diaspora, historical, YA
**Avoid when:** You are sprinkling a language you do not speak for flavour. Native speakers catch it in one word and the whole voice dies with it. Also check the delivery pipeline early — a burned-subtitle or dubbing workflow can flatten the second language back out and undo the entire design.
**Example:**
> Glossed: She called me habibti, which means my love.
> Working: She called me habibti and put the plate down harder than she needed to.

**Yields to:** `voice.second_language_voice` — You do not speak it, or subtitling will flatten it.  
`voice.code_switching`

---

### The Second-Language Voice

**Also called:** translated consciousness, the non-native narrator, translated texture
**What it is:** A narrator thinking in one language and writing in another, so the English carries the other language's grammar, formality level, proverbs and sense of what is polite.
**Effect on the audience:** Freshness in the images and a strange formality where a native speaker would be casual. Done well it is the most distinctive voice texture available in English.
**Used for and where it works best:** Immigrant and diaspora narrators, translated-world historical fiction, and any story set among people who are not speaking the language of the page. The craft rule: the marker is over-correctness, not error. Second-language speakers are typically more formal, more grammatical and more idiom-literal than natives — "I am not agreeing with you" — so build the voice from formality and calqued idiom. Broken English as a voice marker is `voice.eye_dialect` with a different hat on.
**Best in:** formats: novel, memoir, screenplay, VO | genres: diaspora, historical, war, literary
**Avoid when:** The character is a fluent bilingual, which most bilingual people are. Marking every non-native speaker as linguistically strange is precisely the error this technique exists to avoid.
**Example:**
> "He said we should let the matter sleep. In my language it is a good expression. In English he only looked at me."

**Yields to:** `voice.code_switching` — The character is a fluent bilingual.  
`voice.second_language_voice`

---

## Voice in Production

### Writing for the Ear

**Also called:** VO register, spoken-word drafting, the read-aloud pass
**What it is:** Drafting for a listener who cannot go back: short sentences, the subject in front, no nested clauses, information arriving in the order the ear can take it.
**Effect on the audience:** They stay with it. Page prose read aloud loses most listeners at about the second subordinate clause, and they do not come back for the rest of the paragraph.
**Used for and where it works best:** Documentary VO, podcast, ad, explainer, and anything a synthetic or human read will voice. The craft rule: read every line aloud, out loud, at pace. If you have to re-read a line to parse it, rewrite it. Subject first, numbers rounded, and never make the ear hold a clause open across a comma. Then script the silences — mark where picture carries it and no narration is needed, or the film flattens under a continuous voice.
**Best in:** formats: documentary VO, podcast, ad, explainer, kids story, audiobook | genres: all
**Avoid when:** Literary prose meant for the page, where a long controlled sentence is a legitimate pleasure and ear-first rules would sand it flat. Do not let a VO habit colonise your prose.
**Example:**
> Page: Following the collapse of the eastern wall, which had been under repair since the previous autumn, the excavation was suspended.
> Ear: The eastern wall had been under repair since autumn. In March it came down. They stopped digging.

**Yields to:** `voice.sentence_rhythm` — Literary prose for the page, where long sentences please.  
`voice.write_for_the_ear`

---

### The Kids' Register

**Also called:** children's voice, age-pitched register
**What it is:** A register set by sentence length, concrete nouns and one idea per line — not by baby vocabulary, and not by a narrator who has decided children are stupid.
**Effect on the audience:** Children follow it without feeling talked down to, and the adult reading it aloud for the fortieth time does not wince.
**Used for and where it works best:** Picture books, kids' songs and videos, educational content. The craft rule: pitch the syntax young and the vocabulary slightly old — short sentences carrying one real, unusual word per page is how children acquire words and how the reading adult stays awake. Structure by repetition with exactly one variable changing per verse; prediction is the pleasure. Say the line out loud to a real child before you keep it.
**Best in:** formats: picture book, kids' song, animated short, educational video | genres: children's, educational, musical
**Avoid when:** You are actually writing for the parent. A knowing wink over the child's head is a different product — family comedy — and mixing the two makes something neither audience owns. Avoid irony entirely with young children; they read it literally, which is the whole reason `dial.on_the_nose` is not a defect in this format.
**Example:**
> Talking down: The little bird was very, very sad because he had lost his nest. Oh no!
> Pitched: The nest was gone. The branch was bare. Seven small feathers, and nobody there.

**Yields to:** `sub.dual_audience` — You are winking over the child's head.  
`voice.kids_register`

---

### The Voice Bible

**Also called:** tone-of-voice guidelines, style sheet, voice charter
**What it is:** A written document that fixes one voice for everyone who will write in it — the register band, the vocabulary in and out, the sentence habits, and a set of before/after pairs.
**Effect on the audience:** Continuity. The series, channel or brand sounds like one person across many hands, and the audience relaxes into it without knowing why.
**Used for and where it works best:** Series, channels, teams, any project that outlives one writer — and any project handed to a language model, which will default to a generic house register unless the bible overrides it with examples. The craft rule: rules do not transfer, examples do. A bible made of adjectives ("warm, confident, human") produces nothing. Build it from twenty before/after pairs plus a banned-word list, and settle the small mechanical questions — contractions or not, numerals or words, how the audience is addressed — because those are where inconsistency is actually visible to a reader.
**Best in:** formats: series, vlog, brand film, corporate | genres: all
**Avoid when:** A single-author piece that is still finding its voice. Codifying early locks in the first thing you found rather than the best thing. Write the bible after the pilot, out of the pilot.
**Example:**
> "Warm and human." — unusable, and every writer will read it differently.
> "Not: *We are pleased to announce enhanced functionality.* Instead: *It's faster now. Here's what changed.* Contractions always. Second person. Never 'utilise'."

**Yields to:** `voice.finding_your_voice` — Single-author piece still finding its voice.  
`voice.voice_bible`

---

### Tonal Drift

**Also called:** voice slippage, series drift, episode nine syndrome
**This is a named failure, not a recommendation.**
**What it is:** A voice migrating gradually across a long work or a series until the late material no longer sounds like the early material — usually drifting toward whatever register the writer has been reading or writing elsewhere that month.
**Effect on the audience:** They cannot name it, but they feel the show has changed and they stop defending it to other people. Long-form audiences leave over this more often than they leave over plot.
**Used for and where it works best:** Diagnosis. The craft rule: keep a calibration sample — two pages of the earliest material that sound exactly right — and read it aloud before each writing session. That costs ten minutes and saves a rewrite. On a team, drift compounds at every handoff, so send writers back to the bible's *examples*, not its rules. Distinguish it from earned evolution: a voice that changes because the narrator changed is arc, and belongs with `arc.the_lie`; drift has no in-story cause.
**Best in:** formats: — | genres: —
**Avoid when:** Do not chase it in a deliberately evolving narrator, and do not sand a series down to uniformity — a small amount of per-writer variation reads as life. What you are hunting is a one-directional slide in register, not local variety.
**Example:**
> Episode 1: "He came back in March. Nobody asked where from."
> Episode 9: "His return in March represented, for the family, an unresolved question that none of them felt equipped to address."

**Yields to:** `arc.the_lie` — The voice changed because the narrator changed.  
`voice.tonal_drift`

---

## Coverage

**32 cards in this file**, all ids in the `voice.` namespace. Four of them catalogue defects: `voice.register_creep`, `voice.tonal_whiplash`, `voice.eye_dialect`, `voice.tonal_drift`.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Consulted 17 September 2026.

- [Psychic Distance — Stanford TeachingWriting](https://teachingwriting.stanford.edu/psychic-distance)
- [Writing Psychic Distance (Authorial Distance) with John Gardner — Eckleburg](https://www.eckleburg.org/psychic-distance/)
- [Narrative Distance: AP English Literature Review — Albert](https://www.albert.io/blog/narrative-distance-ap-english-literature-review/)
- [Narrative Distance Definition, With Examples For Fiction Writers — Jericho Writers](https://jerichowriters.com/narrative-distance-definition-with-examples-for-fiction-writers/)
- [Mastering Diction Shift: How to Change Voice and Tone in Writing — Literary Devices](https://literarydevices.net/mastering-diction-shift-how-to-change-voice-tone-in-writing/)
- [What is Diction? How to Write Vivid Voices — Now Novel](https://nownovel.com/what-is-diction/)
- [Developing a Distinct Narrative Voice — Fiveable](https://fiveable.me/introduction-creative-writing/unit-4/developing-distinct-narrative-voice/study-guide/7TtUNWDCdC3dpCv0)
- [How to Write Accents and Dialects: 6 Tips — Now Novel](https://nownovel.com/how-to-write-accents-dialects/)
- [Dialect in Dialogue: How to Write Authentic Dialect and Foreign Accents — PenUltimate Editorial Services](https://penultimateword.com/fiction/dialect-in-dialogue-how-to-write-authentic-dialect-and-foreign-accents/)
- [Writing in Dialect: Balancing Authenticity and Readability — Famous Writing Routines](https://famouswritingroutines.com/writing-tips/writing-in-dialect-balancing-authenticity-and-readability/)
- [Eye dialect — Wikipedia](https://en.wikipedia.org/wiki/Eye_dialect)
- [Craft Essay: The First-Person Plural — The Masters Review](https://mastersreview.com/craft-essay-the-first-person-plural/)
- [Collective Narrators: The Best Uses of the First-Person Plural in Literature — CrimeReads](https://crimereads.com/collective-narrators-the-best-uses-of-the-first-person-plural-in-literature/)
- [Changing Me to We: We Should All Try Writing in the First Person Plural — Literary Hub](https://lithub.com/changing-me-to-we-we-should-all-try-writing-in-the-first-person-plural/)
- [Understatement — Oregon State Guide to Literary Terms](https://liberalarts.oregonstate.edu/wlf/what-understatement)
- [Understatement: Definition and Examples — Grammarly](https://www.grammarly.com/blog/literary-devices/understatement/)
- [Litotes — Literary Devices](https://literarydevices.net/litotes/)
- [Craft Corner: Code-Switching as Shapeshifting in Poetry — Mid-American Review](https://casit.bgsu.edu/marblog/craft-corner-code-switching-as-shapeshifting-in-poetry/)
- [Codes Across Languages: On the Translation of Literary Code-switching — University of Cambridge Repository](https://www.repository.cam.ac.uk/bitstreams/c7881636-d8f6-4b28-bf14-42760ebc5109/download)
- [Mastering Voice-over Narration for Documentary Impact — Journalism University](https://journalism.university/electronic-media/voice-over-narration-documentary-tips/)
- [How to Write a Voice-Over Script — Voquent](https://www.voquent.com/blog/how-to-write-a-voice-over-script/)
- [How to Create Tone of Voice Guidelines for Content Teams — Multicollab](https://www.multicollab.com/blog/how-to-create-tone-of-voice-guidelines/)
- [How to Write Your Brand Tone of Voice Guidelines — MOO](https://www.moo.com/blog/success-stories/how-to-write-your-tone-of-voice-guidelines)
- [The Secret to Consistent Voice, Tone and Style — DK Consulting](https://dkconsultingcolorado.com/2024/09/30/the-secret-to-consistent-voice-tone-and-style-in-technical-content/)
