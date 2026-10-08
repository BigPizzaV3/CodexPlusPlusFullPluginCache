# Prose Rhythm — Part 3

Category `rhythm`, continued. Parts 1 and 2 are in `cat-rhythm.md` and `cat-rhythm-2.md` — read them first; their 73 cards cover sentence length as tempo, the figures and the punctuation, paragraph and chapter pace, rhythm across registers and across languages, the read-aloud and the audiobook, the revision pass, and ten named failures. Nothing here repeats them.

**Part 3 of 3.** 10 cards across 3 sections: writing to a fixed duration, the read-aloud and the levelled text, and rhythm under commercial constraint.

These cards close gaps the database reported about itself: each one was reached for by a kit and could not be cited because no card existed. Parts 1 and 2 assume a writer who chooses a sentence's length. Part 3 covers the large part of professional writing where somebody else chose it first — a mouth already moving, a cut that will not change, a legal line that must appear, six seconds of airtime that have already been bought.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Writing to a Fixed Duration](#writing-to-a-fixed-duration)
- [The Read-Aloud and the Levelled Text](#the-read-aloud-and-the-levelled-text)
- [Rhythm Under Commercial Constraint](#rhythm-under-commercial-constraint)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## Writing to a Fixed Duration

### The Line Written for a Fixed Duration

**Also called:** writing to time, writing to length, the timed line, word-rate writing, writing to the clock
**What it is:** A line whose length is decided before its content. The duration arrives from outside — a slot, a cut, a mouth, a slide, a character count — and the writer's job is to find the sentence that both means the right thing and occupies exactly that much time.
**Effect on the audience:** They notice nothing, which is the whole point. A line written to time lands with the picture and leaves air after it. A line written to meaning and then squeezed arrives rushed, and the audience reads rushing as anxiety in the narrator, or as a mistake, and in either case stops listening to the content.
**Used for and where it works best:** Do the arithmetic first and write second. English narration runs about 140 words a minute for corporate and documentary work and about 130 when the pictures need room — so roughly 150 words per minute of energetic read, 75 per thirty seconds, 37 per fifteen, and 15 for a six-second sting. For documentary and heritage narration the rate is 125 WPM and is owned by `pacing.wpm_documentary`; the 140 and 150 figures here are drafting numbers for commercial, corporate, explainer and trailer work only. Then subtract: **pauses are not free and word count cannot see them**, so a 150-word script with three real pauses runs nearer seventy seconds than sixty. The method that works is always the same and is counter-intuitive: **write it long, then cut to the number — never write to the number and then pad.** A padded line is detectable within two words; a compressed one usually improves. Cut in this order: the connective ("and so", "of course", "as we can see"), then the qualifier, then the second example, then the adjective, then — last and only if you must — the clause. Read it aloud at performance pace with a stopwatch, because the only accurate script timer is a voice (`rhythm.read_aloud_test`). The most useful single habit: put the fixed number in the script, next to the line, so every later reader knows the line is a measurement and not a preference. Specific cases: `rhythm.lip_sync_adaptation`, `rhythm.locked_picture_narration`, `rhythm.cutdown_ladder`, and `rhythm.subtitle_beat` for the same problem at reading speed.
**Best in:** formats: Voiceover Script, Advertising, Explainer, Motion Graphics, Trailer, Corporate | genres: Journalism, Educational, Advocacy, Lifestyle, Science
**Avoid when:** The form has no external clock — prose, a stage play, anything a reader sets their own pace through. Writing a novel to a word-rate produces `rhythm.monotone_length`. And do not apply it to a line that carries the piece's single most important fact: if the fact does not fit the slot, the slot is wrong, and the honest move is to take the time from a neighbouring line rather than to compress the one that matters. The real failure mode is the writer who hits the number by removing the pauses, producing a script that is exactly sixty seconds on paper and unreadable at performance pace.
**Example:**
> *The slot: a five-second lower-third caption over an establishing shot. Budget at read pace, with a pause at the end: 11 words.*
>
> *Draft, written to meaning — 34 words:*
> "The city of Nimrud, which was known in antiquity as Kalhu, served as the capital of the Assyrian empire for roughly a hundred and fifty years before the court relocated further north."
>
> *Cut in order. Connectives and qualifiers go, then the second name, then the adjective, then the clause:*
> — 24: "Nimrud, known in antiquity as Kalhu, was the Assyrian capital for a hundred and fifty years."
> — 17: "Nimrud was the Assyrian capital for a hundred and fifty years, then the court moved."
> — **11: "For a hundred and fifty years, this was the capital."** `[:05 — 11 words]`
>
> The last version fits, and it is also the only one that lets the picture say *this*. The cut improved it; padding an eleven-word line up to thirty-four never does.

*(Speaking rates are owned by [`../phase-04-audio-narration/pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md); this file cites them and does not restate them.)*

**Source:** assumption — the package's working figure, not a published standard; the 140 and 150 words-a-minute drafting rates are set against a stopwatch read of the take, and the 125 WPM documentary rate is owned by `pacing.wpm_documentary`.  
**Yields to:** `pacing.wpm_documentary` — on documentary and heritage narration, where the rate is 125 WPM. The 140 and 150 figures here are drafting numbers for commercial, corporate, explainer and trailer work.
`rhythm.duration_locked_line`

---

### Lip-Sync and Mouth-Flap Adaptation

**Also called:** dub writing, dubbing adaptation, lip-sync writing, flap matching, the adaptation pass, localisation dialogue writing
**What it is:** Writing a line of dialogue in a second language to fit a performance that already exists — a fixed duration, a fixed syllable budget, and fixed moments where an animated or filmed mouth visibly closes — while keeping the sense, the character and the joke. It is not translation and translators are not usually the ones who do it; a translator supplies the meaning and an adapter writes the line.
**Effect on the audience:** Total when it works, because the audience forgets they are watching a dub within about a minute and then forgets for two hours. When it fails they cannot say why the film feels false, and they blame the acting. Children are the least forgiving audience for this and the most dubbed.
**Used for and where it works best:** Work the three levels of synchrony in this order, because they cost different amounts and buy different things. **(1) Isochrony** — the line must start when the original starts, end when it ends, and observe the pauses inside the turn; this is non-negotiable and it is where most rewriting happens. **(2) Kinesic synchrony** — the line must be plausible against the body: a character shrugging on a word cannot be delivering the subject of a sentence there, and a character shaking their head needs a negation under it. **(3) Phonetic (lip) synchrony** — only where the mouth is actually visible; in close-up and extreme close-up the visible closures matter, and in practice that means the bilabials /p/, /b/, /m/, the labio-dentals /f/ and /v/, and the big open vowels, while in a wide shot, an over-the-shoulder or a cut away it does not apply at all — and knowing that is half the craft, because it is where the adapter buys back the freedom the close-ups take away. The craft rule: **count the syllables, mark the closures, then write from the closures outward.** Find the word that must sit on the visible /m/ and build the line around it; do not write a good line and then try to slide it onto the mouth. What an adapter is allowed to change is wider than most people expect and narrower than it looks: **word order, idiom, the image inside a metaphor, register, the level of politeness, and the distribution of information across two adjacent lines are all fair game.** Adding hesitations, repetitions and breath to fill time is legitimate, because it is performance texture rather than content. What may not change is what the character wants, what they now know, and anything the picture will contradict. Read every line aloud against the picture while writing it — dub writers do this continuously, not at the end. Related: `lyric.singable_translation`, which solves a different fixed constraint with the same discipline; `rhythm.translationese_scan` for what a badly adapted line sounds like; `voice.kids_register` for who is listening.
**When the mouth is generated from the line, the constraint runs backwards — and most of this card comes off.** Everything above assumes a performance that already exists and a line that has to fit it. In generated work where a character speaks to camera, the line is written first and the mouth is made from it, so there is no fixed duration, no syllable budget and no closure to hit: **isochrony and phonetic synchrony both disappear**, and the line is free to be the best line. Four things replace them. Write for the **voice** — the take is synthesised, so sentence length, comma placement and the words at the ends of phrases are what the breath and the emphasis are built from, and a clause that is hard to say aloud comes back hard to listen to. Keep each **take within whatever length the lip-sync engine actually holds**, which is a number from `ENGINE-CHECK.md` and often far shorter than the speech; a 45-second monologue may have to be three takes joined on a cut, and that is a writing decision, not an editing one, because the joins want to fall at sentence ends. Expect the **mouth to be weakest on the same sounds** the adapter's craft is built around — bilabials and wide open vowels — so a line whose meaning sits on a *p*, *b* or *m* is the line that will read wrong, and it is worth moving the load elsewhere. And **check that the engine has been trained on the language you are writing**, because a mouth driven by a model that has not seen Arabic produces a plausible mouth saying nothing. Related: `dubbing.bilabial_lipsync_alignment` for the alignment itself.

**Best in:** formats: Animated Series, Anime, Animation Feature, Feature Film, Series, Preschool, Vertical Short-Form (Reels, Shorts, TikTok), Explainer | genres: Kids, Family Drama, Comedy, Adventure, Fantasy
**Avoid when:** The piece will be subtitled rather than dubbed — a different constraint entirely, governed by reading speed and line length, not by mouths (`rhythm.subtitle_beat`). Avoid the full phonetic pass on anything that is not in close-up; matching bilabials in a wide shot costs sense and buys nothing anybody can see. And avoid it wholesale on documentary voice-over and UN-style overlay, where the convention is deliberate non-sync and forcing lip-sync reads as fabrication. The honest limit: at some ratios the languages simply do not fit — German and Spanish run long against English, Japanese runs short — and past a certain gap the adapter is choosing what to lose, not how to keep it. Pretending otherwise produces `rhythm.lip_lock`.
**Example:**
> *Source, Japanese, a child in close-up. 7 morae, mouth closes on the first beat (/b/), open vowels through the middle, one closure near the end:*
> **BO-KU-NO-I-E-DA-YO** — 7 · closures at **1** and **6**
>
> *Literal translation — accurate, unusable:*
> "It's my house!" — **3** syllables. Four short, no closure at 1, nothing at 6. The mouth keeps moving after the line has stopped.
>
> *Fits the count, misses the closures:*
> "This is the house I live in!" — **7** ✓ · closures at — and — ✗. The /ð/ at beat 1 leaves the mouth open on a visible /b/.
>
> *Adapted — count, closures and sense all met:*
> **"But this — this is my house. Mine."**
> But(1·/b/ ✓) this(2) this(3) is(4) my(5·/m/) house(6·/h/) mine(7·/m/)
> — 7 syllables ✓ · /b/ on beat 1 ✓ · labial on beat 6–7 ✓ (the closure lands a beat late and reads as the child's emphasis, which the picture supports)
>
> The repetition of "this" is added, not translated. It is legitimate: it buys a syllable, it puts the /b/ where the mouth needs it, and a child insisting is a child who repeats themselves.

**Yields to:** `rhythm.subtitle_beat` — where the piece will be subtitled rather than dubbed. That is a different constraint entirely, governed by reading speed and line length rather than by mouths.  
`rhythm.lip_sync_adaptation`

---

### Lip Lock

**Also called:** dub padding, the stretched line, flap-filling, the line that fits and means nothing
**This is a named failure, not a recommendation.**
**What it is:** Dialogue mangled to fit the mouth — padded with filler to reach the syllable count, stressed on the wrong word to land a closure, or reworded until the sense has quietly gone — so that the line synchronises perfectly and stops being something a person would say.
**Effect on the audience:** A specific and recognisable falseness. The audience hears characters who over-explain, repeat themselves, use everyone's full name, and answer questions nobody asked. They conclude that the original writing is bad, which is the cruellest part of it: the failure is invisibly attributed to the wrong writer.
**Used for and where it works best:** — There is no legitimate version. It is worth knowing that near-misses of it are sometimes *deliberate* in comedy dubbing, where the over-formality becomes the joke; that is a style choice, not this failure, and it announces itself. Where it hurts most is children's animation, because it is the register in which children learn what natural dialogue sounds like, and because nobody in the chain has the authority to say the line is bad.
**Best in:** formats: — | genres: —
**Avoid when:** Always, and the defence is to spend the freedom you have rather than the sense you do not. Before padding a line, check three things in order: is the mouth actually visible in this shot (usually it is not); can the information move to the adjacent line, which may have room; and can the *other* character's next line absorb a syllable. Only after those three fail is compression legitimate, and then you cut sense deliberately and record what you cut. The diagnostic is brutally simple and works in any language: read the dubbed line aloud with the picture off. If it is not a sentence a person would say out loud, it is lip lock, however well it fits. It is the dubbing form of `rhythm.empty_music` — perfect surface, no content.
**Example:**
> *Source, 9 syllables, one visible /p/ near the end. The meaning: "Don't."*
>
> *Lip-locked — fits, and nobody has ever said this:*
> "I would prefer it if you did not proceed with the plan, Peter."
>
> *Adapted — same count, same closure, an actual sentence:*
> "Peter. Listen to me. Put it down. Please."
> — 9 syllables · /p/ on "Put" and "Please," both landing on visible closures · and it is what a frightened person says.
>
> The first version reached the count by adding words. The second reached it by adding *beats* — a name, a command, a plea — which is the move that is always available and almost never taken.

**Yields to:** `rhythm.lip_sync_adaptation` — always. Spend the freedom you have before the sense you do not: check whether the mouth is even visible, whether the information can move to the adjacent line, and whether the other character's next line can absorb a syllable.  
`rhythm.lip_lock`

---

### Writing to a Locked Picture

**Also called:** writing second, narration to picture, post-lock scripting, writing to the cut, VO to timecode
**What it is:** Writing narration after the edit is finished, to a cut that will not move, where every line has a start timecode, an end timecode and a maximum word count set by the shot underneath it. The film is the brief and the sentences are the variable.
**Effect on the audience:** It is the only way narration ever feels inevitable. A line written to picture lands on the frame that proves it and gets out before the next one; a line written first and laid over the cut arrives early, explains what is about to be shown, and steadily converts the film into an illustrated essay.
**Used for and where it works best:** Use it as the default for documentary, heritage, promo, corporate and any film whose footage was gathered rather than staged. The discipline is a set of hard habits. **Write the gaps first**: mark every place narration must *not* speak — a sync line, an archive voice, a piece of sound the film is about, the four seconds after a revelation — and only then write into what is left. **Take the word budget per gap from the arithmetic, not from the feel**, at the documentary rate `pacing.wpm_documentary` owns — the only card that carries one, with an Arabic read taking `pacing.wpm_arabic` — and replace the estimate with the measured voice once a rendered read exists. Write the number beside the line. **Never write over a picture that is already speaking**: if the shot shows a flooded street, the line does not say the street is flooded — it says the year, or the name, or the thing the audience cannot see. **Let the picture take the subject.** The commonest gain in this mode is a line losing its opening clause because the cut already supplied it. And say out loud what each line is *for* before writing it: identify, date, contradict, connect, or hand over. A line that does none of those five is a line the film is better without. Cross-refs: `expo.doc_narration_contract` for what narration is permitted to claim, `rhythm.vo_breath_line` for the breath inside the line, `lyric.spotting_session` for the same negotiation on the music side.
**Best in:** formats: Documentary, Heritage Documentary, Documentary Series, Voiceover Script, Brand Film, Corporate | genres: Heritage, Historical, Journalism, Science, Nature, Advocacy
**Avoid when:** The script drives the shoot — a scripted film, an explainer animated from a board, an ad built from a storyboard. There the words come first and the picture is cut to them, and applying this card produces narration that abdicates. Avoid it also as a rescue: a film with a structural hole cannot be narrated shut, and the attempt is audible as a voice working very hard over a cut that is not going anywhere. The honest failure mode is narration written to fill every gap the edit left, which produces a film with no silence in it and an audience that has stopped hearing the voice by minute four.
**Example:**
> *Written first, laid over the cut — 41 words, and it explains the picture:*
> "In the winter of 1963, the village of Qaraqosh was cut off by the worst flooding in living memory. Families who had farmed the plain for generations found themselves trapped, and for eleven days no supplies could reach them."
>
> *Written to the locked cut. The gaps come first:*
> `01:14:02–01:14:09` — *aerial, water to the rooflines.* **SILENT.** The shot is the flood; saying so is redundant.
> `01:14:09–01:14:13` — *pan to the ridge road.* `[4s · 9 words]` → **"Eleven days. Nothing came up this road for eleven days."**
> `01:14:13–01:14:22` — *sync: the old man, "we ate the seed corn."* **SILENT.**
> `01:14:22–01:14:27` — *a bare field, present day.* `[5s · 11 words]` → **"Seed corn is next year's harvest. They knew what they were eating."**
>
> The date went into a caption, the flood went unmentioned because it is on screen, and the narration now says only the two things the picture cannot.

**Yields to:** `rhythm.vo_breath_line` — where the script drives the shoot. On a scripted film or a board-animated explainer the words come first and the picture is cut to them, and writing to a locked picture there produces narration that abdicates.  
`rhythm.locked_picture_narration`

---

### The Cutdown Ladder

**Also called:** the cutdown, multi-duration build, the duration ladder, the :06/:15/:30/:60 set, building the shorts first
**What it is:** Building one piece so that its six-, fifteen-, thirty- and sixty-second versions are each a complete idea, rather than producing the long one and trimming it three times. The ladder is designed in the writing, before the shoot, not discovered in the edit.
**Effect on the audience:** Nobody sees the ladder; everybody sees the rung they are served. A trimmed six is recognisably an amputation — it starts mid-thought, ends before an idea closes, and reads as an advert for a longer advert. A built six is a complete small thing and outperforms it consistently.
**Used for and where it works best:** Use it on any campaign with more than one duration, which in 2026 practice is all of them. Build it in this order, and the order is the whole technique: **write the six first.** One image, one line, one brand. Whatever survives at six seconds is the campaign's actual idea, and discovering at the edit that it has none is the most expensive way to find out. Then build outward, where each longer version *adds a whole beat* rather than lengthening the existing ones: **:06 = the idea** · **:15 = the idea plus its proof** · **:30 = a problem before the idea, and a call to action after it** · **:60 = a person it happened to.** Write the piece in discrete named beats — hook, problem, product, proof, ask — so a beat can be lifted whole, and make sure every beat has a clean head and tail that can stand as a start and an end. Two practical consequences for the shoot: capture the alternate takes and the clean transitions the short versions will need, and **put the brand and the ask inside the first rung**, because the ladder's bottom step is the one most people will be served. A hook at eight seconds does not exist in a six-second cut. Related: `lyric.jingle_micro_hook` for the same problem in music, `open.first_second_hook`, `seq.shortform_serial`.
**Best in:** formats: Advertising, Product Video, Trailer, Reels/Shorts, Brand Film, Motion Graphics | genres: Lifestyle, Advocacy, Sports, Educational, Underdog
**Shelf life:** dated — review 2027-09. The build-short-first principle is durable. The specific rungs are not: six, fifteen, thirty and sixty are 2026 buying conventions, and the vertical and square variants of each are a platform fact rather than a craft one.
**A compelled line is not a rung.** Where a legal qualifier, a sponsorship disclosure, an AI-use line or a health caveat attaches to the claim, it travels with that claim down every step of the ladder and is *never* the thing dropped to make the six fit — the obligation does not scale with duration. So if the disclosure cannot be delivered properly at six seconds, **the claim that compels it comes out of the six-second version**, and the rung carries a different idea. Cutting the line instead is the failure `info.disclosure_as_content` describes, arrived at by arithmetic rather than by carelessness.  
**Avoid when:** There is genuinely one duration and one placement — a cinema spot, a single festival film, a piece with no paid media behind it. Building a ladder nobody will climb costs shoot days. Avoid it too where the idea is *inherently* long: a piece whose whole effect is accumulation or duration has no honest six-second version, and the correct answer is a different six-second film, not a compression of this one. The honest failure mode is the ladder built downward from a beautiful sixty — every rung reads as a summary of something better that the viewer was not shown, which is the exact feeling a trailer for a trailer produces.
**Example:**
> *One campaign, four complete pieces. The subject: a bakery that opens at four in the morning.*
>
> **:06** — *A dark street. One lit window.* → "Somebody is already awake." `[logo]`
> **:15** — the same, plus the proof beat: *hands on dough, 4:02 on the clock.* → "Somebody is already awake. / Four in the morning, every morning, since 1974." `[logo]`
> **:30** — a problem in front, an ask behind: *an empty shelf at a supermarket, 8am.* → "Most bread is made yesterday. / Somebody is already awake. / Four in the morning, every morning, since 1974. / **Ask for the one that's still warm.**"
> **:60** — a person it happened to: *Amira, who took over from her father and has never once opened late.* → the same four beats, with sixteen seconds of her in the middle saying why she has not changed the time.
>
> Each rung is a finished piece. The six has the idea, the brand and an image. Nothing at sixty seconds was cut down to get there, and the shoot list was written from the six upward.

**Yields to:** `rhythm.duration_locked_line` — where there is genuinely one duration and one placement, such as a cinema spot or a single festival film. Building a ladder nobody will climb costs shoot days.  
`rhythm.cutdown_ladder`

---

## The Read-Aloud and the Levelled Text

### Decodability and the Levelled Text

**Also called:** the decodable reader, controlled vocabulary, the phonics scope and sequence, writing to level, the levelled reader
**What it is:** An early-reading specification that fixes the writer's word choice before the story exists. A **decodable** text may use only the letter-sound patterns the child has already been taught, plus a named list of high-frequency words; a **levelled** text is graded instead by word frequency, word length and sentence length. They are different systems with different rules, and a publisher will hand you one or the other.
**Effect on the audience:** The child reads it *themselves*, which is the entire product. A single untaught word breaks the experience in a way no adult reader can feel from the outside: the child stops, guesses, is wrong, and learns that reading is guessing.
**Used for and where it works best:** Get the specification in writing before drafting — the phonics scope and sequence for a decodable, or the sentence-length and frequency bands for a levelled reader — and treat it as a hard wall, because a manuscript that misses it is not edited, it is rejected. The craft problem is this: **the constraint takes away vocabulary, so all your rhythm has to come from the two things it left you — sentence length and repetition-with-change.** That is the whole technique. Vary the sentence lengths against each other, because short-short-short is the default failure of every decodable text ever written (`rhythm.short_short_long` still works and is the most valuable card in Part 1 for this format). Build a refrain and change one word in it — the child gets fluency from the repetition and a story from the change. Put the one permitted hard word where the picture can carry it. And use the page turn as your punctuation, because in this format it is stronger than any mark. A decodable text is also allowed to over-teach, deliberately: `expo.over_taught_rule` is a named failure everywhere else and a requirement here. Register comes from `voice.kids_register`; the read-aloud sibling of this card is `rhythm.read_aloud_line`.
**Best in:** formats: Kids Story, Picture Book, Educational, Preschool, Middle Grade | genres: Kids, Preschool, Educational, Fable, Slice of Life
**Shelf life:** dated — review 2028-09. The craft is durable. The specifications are commercial and national: phonics scope-and-sequences differ by programme, levelling systems differ by publisher and by country, and both are revised. Never write to a remembered spec.
**Avoid when:** The book is a read-aloud rather than a read-alone — a picture book an adult performs is under no vocabulary constraint at all, and applying one to it strips the language a four-year-old is perfectly able to *hear*. This is the most common category error in children's writing: the listening vocabulary of a five-year-old is years ahead of their decoding vocabulary, and a decodable constraint applied to read-aloud text produces a flat book for no reason. Avoid it also for anything read on screen with audio support. The honest failure mode is the writer who satisfies the specification and stops there, producing a compliant text with no story in it — a wordlist arranged into sentences, which is what most decodable readers are, and the reason a good one is worth so much.
**Example:**
> *Off-spec. Level: short vowels, CVC words, and the taught sight words `the · a · is · said · to`:*
> "Nan's enormous ginger cat leapt through the doorway and vanished into the night."
>
> *On-spec, and flat — every sentence the same length, which is the default failure:*
> "Nan has a cat. The cat is big. The cat is in the bin. Nan is mad. The cat is sad."
>
> *On-spec, with rhythm built from length and repetition-with-change:*
> "Nan has a cat.
> *(turn)*
> The cat is in the bin.
> The cat is in the bag.
> The cat is in the hat!
> *(turn)*
> 'Get that cat,' said Nan.
> *(turn)*
> The cat is on Nan's lap.
> The cat is not sad."
>
> Same wordlist, same constraint. The refrain gives fluency, the one changed word each time gives the story, the exclamation breaks the pattern at exactly the right place, and the last line is short after a run of equal lengths — which is the only joke the specification permitted and it is enough.

**Yields to:** `rhythm.read_aloud_line` — where the book is a read-aloud rather than a read-alone. A picture book an adult performs is under no vocabulary constraint at all: the listening vocabulary of a five-year-old is years ahead of their decoding vocabulary.  
`rhythm.decodable_text`

---

### The Read-Aloud Line

**Also called:** read-aloudability, performance prose, the cold-read line, boxed read-aloud text, writing for the mouth
**What it is:** Prose written on the assumption that someone will say it out loud, once, without rehearsal — a parent reading a picture book, a teacher reading to a class, a games master reading a boxed description to a table, a narrator reading a cold script.
**Effect on the audience:** Two audiences at once, and this is what makes it hard. The listener gets rhythm, sound and story. The *reader* gets the experience of performing well without having practised, and a book that makes an adult sound good is a book that gets read again on Thursday. A text that trips the reader is remembered as a bad book by both of them.
**Used for and where it works best:** The rule is absolute and everyone skips it: **read every sentence aloud, in your real voice, at the pace a tired adult reads at nine in the evening.** A sentence that looks brisk on the page is frequently a mouthful. Then apply four working habits. **Give the mouth a pattern** — a beat the reader can find in the first line and trust for the rest, varied enough that it is not a chant. **Put the surprise at the end of the sentence and the sentence at the end of the page**, so the page turn does the timing (`rhythm.end_weight`). **Never write a sentence whose meaning depends on punctuation the reader has to see coming** — a long subordinate front-load ambushes a cold reader, who has already committed to an intonation by word four (`rhythm.periodic_sentence` is the wrong tool here for exactly that reason). And **vary the beats per sentence and the sentences per paragraph**, because an unvaried read-aloud becomes a lullaby whether or not it is one. For a cold read specifically — a narrator, a games master — add one more: front-load the name of the thing, because the reader is deciding how to say the sentence while saying it and needs to know what it is about before they need to know anything else. Related: `rhythm.read_aloud_test` for the revision pass, `rhythm.performed_breath`, `rhythm.narrator_paragraph`, and `sub.dual_audience` for the joke pitched over the child's head at the adult doing the reading.
**Best in:** formats: Picture Book, Kids Story, Preschool, Audiobook, Voiceover Script, Game Narrative | genres: Kids, Preschool, Fable, Family Drama, Adventure
**Avoid when:** The text is for silent reading by an adult, or is a reference text people scan rather than perform, or is deliberately difficult on the page — a modernist novel, a legal document, poetry that works typographically. And avoid the pattern discipline in anything an actor will interpret: strongly rhythmic prose in a screenplay removes the actor's choices, which is `rhythm.audible_technique`. The honest failure mode is prose so rhythmically locked that the reader cannot put emphasis anywhere the metre did not allow — technically read-aloudable, and it performs itself while the reader recites.
**Example:**
> *Written for the eye. Every clause is fine and the mouth cannot get through it:*
> "Bear, who had been sleeping since the first frost and had not, in all that time, so much as turned over, opened one eye."
>
> *Written for the mouth — and for a parent who has never seen this page before:*
> "Bear was asleep.
> Bear had been asleep since the first frost.
> He had not rolled over. He had not stretched. He had not, in all that time, so much as sniffed.
> *(turn)*
> Bear opened one eye."
>
> The subject arrives in word one, so the reader knows the tune before they need it. The triple gives the mouth a pattern. The turn holds the payoff, and the payoff is four words long — which is what makes a tired adult do the voice.

**Yields to:** `rhythm.action_line_rhythm` — Screenplay prose an actor will interpret.  
`rhythm.read_aloud_line`

---

## Rhythm Under Commercial Constraint

### Writing for a Loop With No Entry Point

**Also called:** the entryless loop, mid-loop entry, in-store and signage writing, the glance medium, always-on content
**What it is:** Writing a piece whose audience arrives at a random second and leaves at another one. Retail and in-store screens, airport and lobby displays, trade-stand walls, exhibition monitors and anything that runs unattended and unmuted-by-nobody. There is no beginning, because nobody is there for it.
**Effect on the audience:** Attention in this environment lasts a glance — the working figure in the trade is roughly 1.5 to 4.6 seconds of genuine attention per passer-by, mostly without sound, because store staff mute everything within a week. A conventional piece that builds is therefore encountered as a random four seconds from its middle, which is why so much signage content reads as meaningless: it is not meaningless, it is being met at second 38 of 90.
**Used for and where it works best:** Stop writing a piece with a shape and start writing a sequence of **independently legible states**. The rule: **every second must be a legible entry.** Concretely — hold one complete idea on screen for four to six seconds before changing anything; never let a sentence span a transition; put the subject of every card in its first two words; and repeat the name of the thing in every state rather than once at the top, because "it" refers to something the viewer did not see. Design the loop at two to four minutes maximum and assume nobody experiences more than one state of it. Then add the one move that makes the format worth having: **write the loop so that a second viewing adds something**, because the people who will see it fifteen times are the staff, and content the staff hate gets turned off. Note that this is the inverse of a narrative loop — `open.loop_opening` and `end.loop_close` cover the seam where the end meets the beginning, and this card is about the requirement that the seam does not matter. Cross-refs: `rhythm.duration_locked_line`, `expo.framing_text_furniture`.
**Best in:** formats: Motion Graphics, Product Video, Advertising, Live Event, Explainer, Carousel | genres: Lifestyle, Educational, Heritage, Advocacy, Science
**Shelf life:** dated — review 2027-09. The craft requirement is durable — random entry has been the condition of public screens since the first shop window. The dwell figures, the two-to-four-minute loop convention and the silent-by-default assumption are 2026 retail practice.
**Avoid when:** The audience is seated, captive, or has chosen to start the piece — a cinema pre-roll, a museum theatre with benches, a piece behind a play button. There the entryless discipline costs you every tool that depends on setup, and the result is a film with no build, which is the failure mode: a piece of content that is legible from any second and worth watching from none. Do not apply it to a piece with a queue in front of it either; a queue is captive and is one of the few public-screen situations where a three-minute build genuinely works.
**Example:**
> *Written as a film. Met at second 38, it is a shot of hands and the word "them":*
> `0:00` "Every loaf we sell is made the night before." · `0:20` "Our bakers start at four." · `0:38` *hands, dough* "…and they do it seven days a week." · `0:55` "Ours is different." · `1:10` `[logo]`
>
> *Written as states. Any four seconds is a complete message:*
> `[5s]` **"This bread was made at 4am. Today."**
> `[5s]` **"The bakery you're standing in starts at 4am."**
> `[5s]` **"4am. Seven days a week. Since 1974."**
> `[5s]` **"Ask for the warm one. It's on the left."**
> `[5s]` **"Made at 4am. Today. Like every day since 1974."**
>
> No state depends on the one before it. Every state names the subject. And the fourth one is the only one that asks for anything, which is what makes the loop bearable for the person working under it.

**Source:** assumption — a trade rule of thumb, no study behind it  
**Yields to:** `open.loop_opening` — Audience captive and starting the piece.  
`rhythm.entryless_loop`

---

### The Disclosure Written as Content

**Also called:** the in-voice disclosure, the integrated disclaimer, the paid-partnership line, compelled text as copy, writing the legal line
**What it is:** A disclosure the law or a platform requires — a paid-partnership label, a sponsorship credit, a results disclaimer, a risk warning — written so that it belongs to the piece's own voice and rhythm instead of being bolted on at the top or buried at the bottom.
**Effect on the audience:** A disclosure in a different voice from everything around it is the single most reliable tell that a piece is an advertisement, and audiences detect it instantly even when they could not explain how. Written in voice, it does the opposite: an early, plain admission of payment *buys* credibility, because the audience has already assumed it and is waiting to see whether you will say so.
**Used for and where it works best:** Start from the fact that the disclosure is not optional and not movable, and work forward from there. Under the FTC's Endorsement Guides a material connection must be disclosed **clearly and conspicuously** — prominent, unavoidable, before the audience engages with the content, not behind a "more" link and not fifteenth in a hashtag stack; the FTC expects it in the creator's own content, in caption, on screen, or spoken, because a platform's built-in tag renders inconsistently and is not always understood. The UK's ASA is stricter about wording than placement: **"Ad", "Advert", "Advertisement" and "Ad Feature" are acceptable and prominent-and-upfront is required**, and the ASA specifically advises against "sponsored" as too ambiguous. So: **write the disclosure as the first sentence of the piece, in the piece's own voice, and never as a separate register** — of the piece when the whole piece is the paid content, and of the segment when only a segment is, which is the moment it applies in `info.disclosure_as_content`. Three rules make it work. **Say the relationship, not the category** — "they sent me this and paid me to talk about it" beats "#ad" for trust and satisfies both regimes as long as it is genuinely prominent. **Put it before the hook pays off, not before the hook** — the first line, not the zeroth. And **write a version you are willing to say out loud**, because the on-screen text alone is the weakest of the three surfaces. Note the inverse case worth knowing: a UK broadcast sponsorship credit may *not* contain a call to action or an advertising message, so there the discipline is the opposite — the ask has to live somewhere else entirely. Related: `voice.advertising_register`, `tens.credibility_economy`, `info.credibility_ladder`, `theme.implicit_ad_claim`, and `expo.framing_text_furniture` for on-screen furniture generally.
**Best in:** formats: UGC Ad, Vlog, Reels/Shorts, Advertising, Podcast, Brand Film | genres: Lifestyle, Advocacy, Journalism, Educational, Testimony
**Shelf life:** dated — review 2027-09. The craft rule — compelled text in the piece's own voice, early, plain — is durable. The specific requirements are not: the FTC Guides were last substantially revised in 2023, ASA guidance is updated continuously, and both are jurisdictional. Check the live regime for the territory the piece will run in, and never write to a remembered rule.
**Avoid when:** Reading "first sentence" as the first sentence of the entire piece: it means the first disclosure-bearing sentence, before the qualified claim, so a non-claim hook may precede it where the live regime permits and the disclosure stays prominent and unavoidable. The disclosure is legally prescribed **verbatim** — a financial risk warning, a medicines line, a regulated claim — where the words are the words and integration is not on offer. There the craft moves to placement and to writing the sentence *before* it so the required text lands as a beat rather than an interruption. Avoid integration so smooth the disclosure stops being noticeable, too: that is not craft, it is a compliance failure with good rhythm, and it is the exact thing "clear and conspicuous" exists to catch. The honest failure mode is a disclosure delivered in a different voice from the rest of the piece — the confiding creator who suddenly reads a legal notice — which is the most reliable single indicator that the whole script was written by a brand team.
**Example:**
> *Bolted on. The register changes twice in eleven seconds and the ad announces itself:*
> On-screen card: `#ad #sponsored #gifted #partner`
> "Hi guys! So — *[flat, faster]* this video is a paid partnership with Northfield and contains a sponsored product. *[back to normal]* Anyway, so I've been having this problem with—"
>
> *Written as content. Same fact, first line, one voice:*
> "Northfield paid me to try this for a month, which is why I actually finished the month. Here's what I'd tell you if they hadn't."
> `[on-screen, held 5s: **Paid partnership with Northfield**]`
>
> The disclosure is the first sentence, it is prominent, it is spoken and on screen, it names the relationship rather than a category — and it sets up the hook instead of delaying it, because "here's what I'd tell you if they hadn't" is the only reason to keep watching and it is only available to a script that admitted the payment.

**Yields to:** `expo.warning_notice` — where the disclosure is legally prescribed **verbatim** and you have no authority over the wording. There the craft moves to placement and to the sentence before it, never to the compelled text.  
`rhythm.disclosure_as_content`

---

### The Call to Action as a Written Line

**Also called:** the CTA, the ask, the close, the action line, the direct-response close
**What it is:** The sentence that asks. Treated as craft rather than as a field to fill: its length, its verb, its position relative to the payoff, and the rhythm that makes an ask land instead of embarrassing everyone.
**Effect on the audience:** An ask that arrives after a reason feels like a reasonable next step. The same ask arriving before the reason feels like being sold to, and the audience's response is not refusal but withdrawal — they stop believing the preceding ninety seconds retroactively. The cost of a badly placed CTA is not a lost conversion, it is a lost piece.
**Used for and where it works best:** Use it wherever the piece wants something, and write it to five rules. **One ask.** A CTA stacked with a discount code, a link and a follow request converts worse than any one of them alone, because three asks read as need. **Open on an imperative verb** and put the outcome in the same breath — "Download the map" beats "Learn more" every time, and "Learn more" is usually a sign the writer did not know what they were asking for. **Two to five words for a button, one sentence for a spoken close.** **Put it after the payoff, never stacked on top of it** — the audience must have been given the reason before they are given the ask, and one beat of air between them is worth more than any adjective. And **make it something they can do before the end of the day**: an action nobody can take from where they are sitting is not a call to action, it is a wish, which is why a cinema spot that ends on "visit our website" has spent a captive audience on nothing. The rhythm rule under all of it: **the ask is the shortest sentence in the piece.** After a long line, a four-word imperative is heard as a decision rather than as a request — `rhythm.short_after_long` doing commercial work. Related: `end.brand_film_close`, `end.explainer_close`, `sub.direct_address`, `voice.addressing_the_reader`, and `rhythm.disclosure_as_content` for the other compelled line in the same thirty seconds.
**Best in:** formats: Advertising, UGC Ad, Explainer, Product Video, PSA, UX Writing | genres: Lifestyle, Advocacy, Educational, Sports, Faith
**Avoid when:** The piece is not asking for anything — a brand film building recognition, a documentary, a piece of editorial with a sponsor but no offer. A CTA welded onto a film with no offer behind it converts the whole film into an advertisement in the last four seconds and is the cheapest way to lose the goodwill the other fifty-six earned. Avoid it also where the regime forbids it: a UK broadcast sponsorship credit may not contain one. And avoid the second ask, always. The honest failure mode is the CTA that names the medium instead of the action — "check out the link in bio", "visit our website" — which asks the audience to do the writer's work of deciding what for.
**Example:**
> *Stacked, plural, and on top of the payoff:*
> "So if you want to find out more about how Northfield can help your family sleep better, head to the link in our bio, use code SLEEP20 at checkout for twenty percent off, and don't forget to follow for more tips!"
>
> *One ask, after the payoff, with a beat of air:*
> "She slept through for the first time in four months."
> *(beat)*
> "**Try one night.**"
> `[on-screen: northfield.com/onenight]`
>
> Twelve words to four. The imperative opens it, the outcome is inside the ask, the code and the follow are gone, and the shortest sentence in the piece is the one doing the asking — which is why it sounds like an invitation rather than a plea.

**Shelf life:** dated — review 2027-03. The craft is durable: one ask, an imperative, the outcome inside it. The platform particulars are not — where the ask may point, what the interface calls the action, and how much of the frame its own furniture occupies have all moved more than once, and the frame figures are owned by `vertical.safe_zones` rather than restated here.

**Yields to:** `end.brand_film_close` — The piece has no offer behind it.  
`rhythm.call_to_action_line`

---

## Coverage

**10 cards** in this file, across 3 sections: Writing to a Fixed Duration (5), The Read-Aloud and the Levelled Text (2), Rhythm Under Commercial Constraint (3).

**What the research showed that the brief did not anticipate.**

*The lip-sync card had to become two.* The three sync levels, the closure-first method and the permission list are one card. What a dub writer does when the line will not fit is a different card, it is a named failure, and the literature names it: **lip lock**. Writing it inside the technique card would have buried the thing a writer most needs to recognise, since lip lock is the failure nobody in the chain has the authority to flag. The technique card says where the freedom is; the failure card says what happens when you spend sense instead.

*Decodable and levelled texts are two systems and most sources conflate them.* A decodable text is controlled by the phonics scope and sequence; a levelled text is graded by word frequency and sentence length. They are written to different specifications by different publishers and the distinction is load-bearing — a writer who gets it wrong writes a compliant manuscript for the wrong system. One card names both and says which is which, because a writer meets whichever one the contract specifies and needs to know it is not the other.

*The read-aloud card serves two gaps at once, from different kits.* `formats-kids.md` needed it for picture books; [`../phase-01-story-generation/interactive-and-branching.md`](../phase-01-story-generation/interactive-and-branching.md) recorded **boxed read-aloud text** — the tabletop module's direct-to-the-table register, performed cold by a non-actor — as a separate gap. They are the same craft problem, cold reading by an unrehearsed reader, and the card covers both explicitly rather than pretending the tabletop case away.

*The disclosure card is the most jurisdictionally exposed card in the database and says so twice.* It cites two named regimes, in two countries, that agree on the principle and differ on the wording, and it carries the one case that inverts the whole card: a UK broadcast sponsorship credit may not contain a call to action, so there the disclosure and the ask must be kept apart rather than integrated.

**Still missing, and recorded rather than hidden.** Part 2's outstanding list is largely untouched, because this file spent its ten cards on kit-reported gaps rather than on category-reported ones. Still uncovered: headline, deck and standfirst rhythm; first-person against third-person rhythm and close third borrowing a character's sentence length; present-tense rhythm; comic timing at sentence level; pace across a serialised release; typography and measure as pacing; email and chat register; assonance and vowel colour; the repeated word across a page; the callback line's rhythm; scene-and-sequel alternation heard as pace. Outstanding named failures: the stacked prepositional phrase, the buried verb, throat-clearing openings, the comma-comma-comma sentence, over-punctuation, the false-profound short paragraph, and accidental sing-song metre. Two further gaps surfaced while writing this file and belong to no existing list: **the string-length budget** — writing to a hard character count a UI imposes, which [`../phase-01-story-generation/interactive-and-branching.md`](../phase-01-story-generation/interactive-and-branching.md) also reports and which is a rhythm problem rather than a localisation one — and **subtitle reading speed as a rhythm constraint**, distinct from `rhythm.subtitle_beat`, which covers the beat and not the characters-per-second ceiling.

Named failures in this file: `rhythm.lip_lock`.

Carrying a review date: `rhythm.cutdown_ladder` (review 2027-09), `rhythm.decodable_text` (review 2028-09), `rhythm.entryless_loop` (review 2027-09), `rhythm.disclosure_as_content` (review 2027-09). The other six are durable craft — arithmetic, mouths, cold readers and the shape of an ask do not expire.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Verified 17 September 2026.

- [Voiceover Script Length: Word Count to Duration Calculator — GoTeleprompter](https://goteleprompter.com/blog/voiceover-script-word-count-calculator/)
- [Script Timer for Videos & Films — Word-Timer](https://word-timer.com/video-script-timer/)
- [Script Timer Voiceover Calculator for Perfect Timing — Lance Blair VO](https://lanceblairvo.com/voiceover-script-timer/)
- [Mastering Voice-Over Narration for Documentary Impact — Journalism University](https://journalism.university/electronic-media/voice-over-narration-documentary-tips/)
- [Should Narration Be Added During Documentary Production? — Rick Lance Studio](https://www.ricklancestudio.com/narration-be-added-during-documentary-production/)
- [Dubbing in Practice: A Large Scale Study of Human Localization With Insights for Automatic Dubbing — TACL (MIT Press)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00551/115968/Dubbing-in-Practice-A-Large-Scale-Study-of-Human)
- [The Perception of Isochrony and Phonetic Synchronisation in Dubbing — Universitat Autònoma de Barcelona (PDF)](https://ddd.uab.cat/pub/tfg/2014/123379/TFG_gonzaloiturregui.pdf)
- [Dubbing Adaptation Accuracy in Translation: The Ins and Outs — ATA Audiovisual Division](https://www.ata-divisions.org/AVD/dubbing-adaptation-accuracy-in-translation-the-ins-and-outs/)
- [Dubbing Script Translation and Adaptation for Lip-Sync — Lipsie](https://www.lipsie.com/gb/services/dubbing-script-translation.htm)
- [Lip-Sync Techniques for Perfect Animation Dubbing — DubNSub](https://dubnsub.com/lip-sync-techniques-for-perfect-animation-dubbing/)
- [Mouth Flaps — TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/MouthFlaps)
- [Lip Lock — TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/LipLock)
- [Lip Synchrony of Rounded and Protruded Vowels and Diphthongs in Dubbed Animation — Redalyc](https://www.redalyc.org/journal/6944/694474400017/html/)
- [Decodable text — Wikipedia](https://en.wikipedia.org/wiki/Decodable_text)
- [The Role of Decodable Readers in Phonics Instruction — Iowa Reading Research Center](https://irrc.education.uiowa.edu/blog/2020/11/role-decodable-readers-phonics-instruction)
- [Decodable / Leveled Text Comparison — Colorado Department of Education](https://www.cde.state.co.us/coloradoliteracy/decodable_leveled_text)
- [The What, Why, and When of Decodable and Leveled Texts — NWEA Teach. Learn. Grow.](https://www.nwea.org/blog/2024/the-what-why-and-when-of-decodable-and-leveled-texts/)
- [Leveled, Decodable, Readable: What Does Research Say About the Right Texts for Beginning Readers? — Great Minds](https://greatminds.org/english/blog/geodes/leveled-decodable-readable-what-does-research-say-about-the-right-texts-for-your-beginning-readers)
- [Read-Aloudability: Ensuring Your Picture Book Sings When Read — Emma Walton Hamilton](https://emmawaltonhamilton.com/blog/read-aloudability-ensuring-your-picture-book-sings-when-read)
- [Rhythm and the Read-Aloud — Aaron Shepard](http://www.aaronshep.com/kidwriter/A66.html)
- [The Best Picture Books Are Built, Not Just Written — Rachel Bachman](https://bachmanrachel.substack.com/p/the-best-picture-books-are-built)
- [Picture Book Writing Style — Kidlit](https://kidlit.com/picture-book/)
- [Cutdowns That Convert: Turning a :90 Video into Platform-Native Ads — SWNG Productions](https://swngproductions.com/cutdowns-that-convert/)
- [Leveraging Cutdowns and Aspect Ratios for Maximum Impact — Image Studios](https://imagestudios.com/leveraging-cutdowns-and-aspect-ratios-for-maximum-impact/)
- [Companion Cutdowns: Turning One CTV Ad Into a Reels Library — Influencers Time](https://www.influencers-time.com/companion-cutdowns-turning-one-ctv-ad-into-a-reels-library/)
- [How Dwell Time in Digital Signage Affects Your Business — ScreenCloud](https://screencloud.com/digital-signage/importance-of-dwell-time)
- [Digital Signage Content That Doesn't Get Ignored in Retail Environments — AVNation](https://www.avnation.tv/2025/12/31/digital-signage-content-that-doesnt-get-ignored/)
- [Perfect Your Digital Signage Loop for Maximum Impact — 21st Century AV](https://21stcenturyav.com/digital-signage-loop-best-practices/)
- [FTC's Endorsement Guides: What People Are Asking — Federal Trade Commission](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking)
- [Guides Concerning the Use of Endorsements and Testimonials in Advertising — Federal Register, 2023](https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising)
- [Recognising Ads: Social Media and Influencer Marketing — ASA / CAP](https://www.asa.org.uk/advice-online/recognising-ads-social-media.html)
- [Recognising Ads: Advertisement Features — ASA / CAP](https://www.asa.org.uk/advice-online/recognising-ads-advertisement-features.html)
- [15 CTA Best Practices to Increase Conversions — Venture Harbour](https://ventureharbour.com/15-call-action-best-practices-increase-conversions/)
- [How to Write a Killer Call to Action: 8 Super Effective Tips — WordStream](https://www.wordstream.com/blog/ws/2014/10/09/call-to-action)
- [How to Craft the Perfect Copywriting Call to Action — Daniel Doan](https://danieldoan.net/copywriting-call-to-action/)
