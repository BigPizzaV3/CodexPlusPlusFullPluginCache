# Pacing, Cadence & WPM Calibration

21 cards. Word count formulas, speaking rates, breath durations, and syntactic rhythm structures tailored across film, documentary, social media, and drama.

---

### Documentary Baseline Tempo

**Also called:** 125 WPM standard, unhurried documentary delivery  
**What it is:** The planning rate for serious documentary narration: **125 words per minute**, the speed that balances clarity against the time an eye needs to inspect a picture.  
**This card is the only place in the package that carries a documentary rate for English narration; an Arabic read takes its word-count conversion and its rate band from `pacing.wpm_arabic`, which owns every Arabic speaking rate and is applied first.** Everywhere else — the
Phase 4 protocol, the Phase 3 timing note, the voiceover format kit — cites `pacing.wpm_documentary`
and does not restate a figure. That rule exists because the figure had drifted: the same rate was
written as 120–135 in one file, as a 110–130 band in another and as a flat 125 in a third, and on a
twelve-minute film the ends of that spread are about 360 words apart. Three hundred and sixty words
is not a rounding difference, it is a different script. One number, in one place, cited by id.

Real reads do spread either side of 125 — a heavy archival section runs slower, a montage of dates
runs faster — but that spread is an *observation about a delivered read*, not a second planning
figure, and it is never the number you write a script against.  
**Effect on the audience:** Gives the audience room to inspect images, read archival details, and digest historical arguments without feeling rushed.  
**Used for and where it works best:** All historical, scientific, and heritage documentary narration. Ensures script length translates exactly to airtime (1 page = ~1 min).  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Video Essay | genres: Historical / Biopic, Documentary  
**Avoid when:** High-energy vertical shorts where 125 WPM feels sluggish and leads to immediate swipe-away.  
**Every rate on this card is an estimate for planning, and the real duration comes from the rendered
audio file, measured — never from the arithmetic.** A
synthesiser does not hold a fixed words-per-minute: the same script comes back at different lengths
depending on the voice, the stability setting, the emotional direction and how it chooses to
breathe. So `words ÷ 125` is how you decide roughly how much to write, and the rendered file is how
you learn what you actually have. **Measure the audio, then build the picture to it** — never the
reverse, and never trust the arithmetic over the waveform.

That is also why a requested runtime is a target rather than a contract: a twenty-minute film whose
narration lands at 20:12 has landed. Write the full word count for the stated runtime, then let the
act-break silences (`pacing.pause_act_break`) and the caesuras extend it, because a silence that was
designed is part of the piece, and cutting words to protect a round number spends the writing to
protect the arithmetic.

**The one exception is express mode.** When the skill is running end to end on a single upfront
confirmation, nobody is standing by to accept a twelve-second overrun, so there the pauses are
subtracted from the budget instead: `words = (runtime − total planned silence) × 125`, and the piece
holds its stated length.  
**Yields to:** `pacing.wpm_arabic` — Arabic narration, whose word count and rate band that card owns. Otherwise nothing: this card sets the rate; `pacing.pause_act_break` sets the silences, and the
two are added in **question-led runs** and netted in express mode. *(This used to read "interactive work", meaning a run where the skill asks and you answer. In this package **interactive** belongs to the genre — a branching piece the viewer navigates, the `inter.*` cards — and a writer of one read this line as a rule about their film, added durations that should have been netted, and put a branch over its contractual cap with every closing check passing.)*  
**Example:** `formula: total_words / 125 = duration_in_minutes | e.g. 250 words ≈ 2 minutes of speech, plus any written pauses.`  
**Source:** reference — the long-standing documentary narration convention; the figure is the trade's, not this package's  
`pacing.wpm_documentary`

---

### Social Media High-Retention Pacing

**Also called:** 170 WPM reel velocity, retention pace, sprint cadence  
**What it is:** An accelerated speaking rate of 160 to 185 words per minute, stripped of dead air and long pauses, optimized for mobile attention spans.  
**Effect on the audience:** Creates an urgent flow of incoming information that keeps the brain occupied and eliminates impulse to swipe away.  
**Used for and where it works best:** TikToks, Instagram Reels, and YouTube Shorts; fast educational explainers and viral hooks.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok) | genres: Informational, Viral Science, Entertainment  
**Avoid when:** Complex grief, theological philosophy, or scenes requiring visual reverence.  
**Example:** `spec: target: 175 WPM | 60-second reel = exactly 165-175 words total script.`  
**Source:** assumption — the package's working figure, not a published standard; set it against the rendered audio.  
**Yields to:** `pacing.wpm_vertical_heritage` in [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) — Vertical heritage or history work needing reverence, not sprint velocity. A quiet vertical piece that is neither - a narrated fiction, a storytelling reel - takes its rate from `pacing.wpm_narrated_fiction`, not from a heritage register, and its length from the measured render.  
`pacing.wpm_social_reels`

---

### Vertical Heritage Reel Cadence

**Also called:** 145 WPM heritage reel standard, mobile antiquities cadence, reverent vertical pacing  
**What it is:** A speaking rate of 140 to 150 words per minute (target: 145 WPM), chosen for short feed heritage and historical storytelling in any aspect (a 16:9 feed reel included). Bridges the gap between traditional documentary reverence (`pacing.wpm_documentary`, which carries that figure) and social media sprint velocity (`pacing.wpm_social_reels`, which carries that one).  
**Effect on the audience:** Holds high mobile viewer retention against swipe-away while maintaining acoustic dignity, historical authority, and articulatory clarity for complex ancient proper nouns (Ashurbanipal, Sennacherib, Nineveh).  
**Used for and where it works best:** Heritage reels for a feed, 9:16 or 16:9, TikTok/Instagram historical deep-dives, ancient civilization reels, and archaeological short-form explainers (especially an established heritage channel with a large, returning audience).  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Heritage / Historical Documentary | genres: Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic  
**Avoid when:** Traditional horizontal 90-minute broadcast documentaries (use `pacing.wpm_documentary`, which carries the figure) or rapid comedic/trend dance reels (use `pacing.wpm_social_reels`, which carries that figure).  
**Example:** `formula: 60-second vertical heritage reel = about 135 words of script (56 spoken seconds at the 145 WPM target), leaving 2s opening visual lock and 2s ending musical ringout.`  
**Source:** assumption — a reasonable default sitting between the documentary rate and the social rate. **Nothing calibrated it.** It read as "calibrated" and "specifically engineered" until September 2026, which is the claim this field exists to stop  
**Yields to:** `pacing.wpm_documentary` in [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) — Horizontal broadcast documentary (also social_reels for trend reels).  
`pacing.wpm_vertical_heritage`

---

### Dramatic Scene Dialogue Cadence

**Also called:** 115 WPM dramatic space, subtext pacing, dialogue breathing  
**What it is:** A slower speaking rate of 110 to 130 words per minute that incorporates natural reaction pauses, subtextual glances, and emotional friction.  
**Effect on the audience:** Elevates drama by proving the characters are thinking, processing threats, and deciding what to conceal before they speak.  
**Used for and where it works best:** Character confrontations, courtroom cross-examinations, whispered conspiracies, and romantic admissions. Where the scene is lip-synced on screen, the take length the lip-sync engine can hold limits one unbroken speech, as `pacing.wpm_to_camera` notes; where no engine is named yet, plan the speeches at the scene's natural length and note the choice under `decisions`.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film | genres: Drama, Thriller / Suspense, Tragedy  
**Avoid when:** Patter comedy or screwball dialogue where rapid-fire overlap is the comedic engine.  
**Example:** `dialogue_rate: 115 WPM + 400ms inter-character pause gap between turns.`  
**Source:** assumption — a working default for dramatic dialogue, untested; the 400 ms turn gap in the example is the same kind of figure  
**Yields to:** `pacing.interruption_overlap` — Patter or screwball, where overlap is the engine.  
`pacing.wpm_dramatic_dialogue`

---

### Commercial Promotional Cadence

**Also called:** 155 WPM commercial read, pitch tempo, call-to-action drive  
**What it is:** A brisk, energetic rate of 145 to 165 words per minute designed to fit 30-second or 60-second broadcast time-slots with crystal clarity. **This card owns the commercial rate for the whole package** — except the language step: an Arabic read takes its word-count conversion and its promotional band from `pacing.wpm_arabic` first, in the order `pacing.wpm_to_camera` states (language, then audience, then delivery mode); where another file needs it, it cites this id rather than restating a figure. A harder-sell retail read runs faster still, up to about 190, and that is the top of the range rather than a second standard — above it the claim stops being heard. As with every rate here, the number is a planning estimate and the real duration comes from the rendered file, measured.  
**Effect on the audience:** Delivers product benefits or event details with crisp enthusiasm before listener attention wanders.  
**Used for and where it works best:** 30-second TV commercials, radio spots, event promos, and sponsor endorsements.  
**Best in:** formats: Commercial / TVC, Radio Promo | genres: Commercial, Promo  
**Avoid when:** Solemn institutional memorials or contemplative art documentaries.  
**Example:** `slot: 30-second TVC = 53-60 words maximum (22 seconds of voice at 145-165 WPM) to allow 5s intro music and 3s legal tag.`  
**Source:** assumption — the package's working figure, not a published standard; set it against the rendered audio, measured.  
**Yields to:** `pacing.wpm_epic_mythology` in [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) — Solemn memorial or contemplative reads; and `pacing.wpm_arabic` — an Arabic read, whose conversion and band that card owns.  
`pacing.wpm_commercial_promo`

---

### To-Camera Dialogue Rate

**Also called:** speaking to the lens, direct address tempo, presenter rate  
**What it is:** **A character speaking to camera is not narrating, and the narration rates do not apply to them.** Narration sits over a picture and is paced against it; direct address *is* the picture, so it runs at the tempo of someone actually talking to you — **roughly 130 to 150 words per minute** for an ordinary conversational delivery, slower for a character whose weight or age is the point, faster for an excited or comic one. **This card owns the to-camera rate for the whole package.** **It is a delivery mode, not an audience or a language, so it combines rather than competes.** Where the speaker is a child or is addressing children, take the tempo from `pacing.wpm_children` and the *direct-address* shape from here — the audience rate wins on the number. Where the speech is Arabic, take the word-count conversion and the rate band from `pacing.wpm_arabic`, for the same reason: the language changes what a word costs. **Order: language, then audience, then delivery mode.** Three cards in this file each said they owned the answer for the whole package and none named the others, which left an Arabic child speaking to camera with three owners and no rule. It is a range rather than a figure on purpose: unlike a narrator, a character's tempo is characterisation, so it is chosen per character and written into their voice record, not taken from here as a default.  
**Effect on the audience:** A person, rather than a voice. Read at a documentary rate, direct address sounds like someone reciting at you; read at a social-reel rate, it sounds like an advert.  
**Used for and where it works best:** A presenter, a host, a character addressing the lens, a vertical episode with no narrator, a testimony delivered straight down the barrel. **Two things it changes downstream.** The runtime is set by this rate and not by a narration rate, so the shot table's provisional timings come from here. And where the piece is lip-synced, the **take length the lip-sync engine can hold** is a hard limit on how long one unbroken speech can be — that figure is in the engine record, and it is a structural input, not a finishing one.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Explainer, Kids Content, Museum Installation, Brand Film, Animated Series | genres: all  
**Avoid when:** The voice is over a picture rather than in it — that is narration, and its register's own card owns the rate.  
**Example:** `rate: to-camera, 140 wpm conversational; 45-second episode ≈ 105 words; take length capped by the lip-sync engine record, pending_engine_check.`  
**Source:** assumption — the package's working figure, not a published standard; set it per character by measuring the recorded take.  
**Yields to:** `pacing.wpm_children` in [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) — A child speaker: the audience rate wins the number.  
`pacing.wpm_to_camera`

*(Markers are defined in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set and the rule that each one closes two ways — resolved, or `unobtainable`, with what was done instead.)*

---

### Arabic Narration Rate

**Also called:** Arabic words per minute, MSA read tempo, the Arabic word-count conversion  
**What it is:** **The rate for Arabic is not the English rate, and the word count is not the English word count.** An Arabic word carries more than an English one — the definite article, prepositions, pronoun suffixes and possessives attach to the word rather than standing separately — so the same content is roughly **0.8 to 0.85 of the English word count**, and the words are longer to say. A Modern Standard Arabic narration read lands around **115 to 130 words per minute** for documentary and heritage work, and around **140 to 155** for a social or promotional read. **This card owns every Arabic speaking rate in the package**, and it is applied *before* the register cards, because it changes what a word costs rather than how fast the words go: take the word-count conversion from here, then the tempo from the register — `pacing.wpm_children` for a young audience, `pacing.wpm_to_camera` for direct address, `pacing.wpm_documentary` for narration, `pacing.wpm_dramatic_dialogue` for scene dialogue, `pacing.wpm_narrated_fiction` for a told story, `pacing.wpm_commercial_promo` for a sell, or whichever other register card in this file the piece is. **Those register cards carry English rates; an Arabic read takes its figure from the two bands here:** a calm, told or reverent register — documentary, heritage, a told story, scene dialogue — reads in 115 to 130, and a young audience at the low end of it or under; a brisk or selling register — social, promotional, an energetic presenter — reads in 140 to 155. Pick a figure inside the band, record it under `decisions`, and continue. A colloquial read — Baghdadi, Egyptian, Levantine — changes the word count, because its forms are shorter; whether it also runs faster is not settled: the one study that measured both found Jordanian speakers faster reading aloud (141.4 words per minute) than in conversation (140.1 without pauses) (Damhoureyeh et al. 2020, cited on this card). If the piece is in a dialect, say which one on the page, and measure the take. **There is no published words-per-minute figure for Iraqi or Gulf Arabic (none found on 2026-09-24), and this card is not going to invent one.** The nearest published colloquial figures are Levantine, and they come from spontaneous conversation, not from a narration read: Syrian adults (65 university students) ran **117.6 words per minute (244.5 syllables per minute)** with pauses included, and 153.6 words (317.9 syllables) per minute with silences over 150 ms taken out (Marie et al., 2026); Jordanian adults (51 students aged 18 to 25) ran **124.5 words per minute** with silences under 2 seconds included, and 140.1 with silences taken out (Damhoureyeh et al., 2020). Reading a written-Arabic passage aloud, the same groups ran 103.8 (Syrian) and 141.4 (Jordanian) words per minute, so the two studies disagree on whether conversation outpaces reading, and neither figure is a narration tempo. Use them as a sanity check on the speaker's own recorded take, not in place of it. Derive it instead: record thirty seconds of the actual speaker reading the actual script, count the words, multiply. That takes two minutes and is worth more than any published figure would be, because dialect speech rate varies more by speaker and register than by language. Until you have it — and on a prompts-only run, or with no speaker to record, that is the whole run — plan from the MSA band above: choose a figure, record it under `decisions`, carry `pending_measured_duration` as a note, and continue. The work never waits for the recording.  
**Effect on the audience:** Stops the two standard failures: an Arabic script written to an English word count, which overruns, and an Arabic script timed at an English rate, which is read too fast and loses the formality the register depends on.  
**Used for and where it works best:** Any Arabic-language narration, and — the case that bites hardest — any bilingual piece where one language is spoken and the other is on screen. English voice with Arabic subtitles and Arabic voice with English subtitles are different problems and neither one is solved by translating at the same length.  
**Best in:** formats: Documentary, Heritage Reel, Commercial, Podcast | genres: All Arabic-language work  
**Avoid when:** Never avoided on Arabic material. On a sung line, the melody sets the timing and this card does not apply — see the lyric craft in Phase 5.  
**Example:** `rate: MSA heritage narration at 120 wpm; English source 760 words → Arabic target ≈ 625 words ≈ 5:12, pending_measured_duration.`  
**Source:** assumption — the word-count conversion and both MSA bands are working defaults with no publication named; the card says itself that no published figure exists for Iraqi Arabic, and the measured read it prescribes replaces them. The Levantine conversation figures are reference — Marie, AlSwaiti, Ghanem, Suliman & Natour, 'Speech Rate in Adult Syrian Arabic Speakers: Preliminary Data', Journal of Language Teaching and Research 17(1), 12-21, January 2026, https://doi.org/10.17507/jltr.1701.02 ; Damhoureyeh, Darawsheh, Qa'dan & Natour, 'Preliminary Speech Rate Normative Data in Adult Jordanian Speakers', Journal of Language Teaching and Research 11(2), 204-211, March 2020, http://dx.doi.org/10.17507/jltr.1102.08 (both read 2026-09-24).  
**Yields to:** Authority: the melody, via the Phase 5 lyric craft — A sung line, where this card does not apply.  
`pacing.wpm_arabic`

---

### Children's Narration Rate

**Also called:** kids read tempo, young-listener pacing  
**What it is:** A slower, more articulated read of **95 to 115 words per minute** for preschool and early-primary listeners, and **115 to 130** for roughly ages seven to eleven. The figures follow the listener's age, not the speaker's: a child character narrating a piece made for adults is read at the rate of that audience's register. **This card owns the children's rate for the whole package**, and it outranks the delivery-mode card `pacing.wpm_to_camera` on the number where both apply — a child is a child whether narrating or addressing the lens. Where the speech is also non-English, `pacing.wpm_arabic` supplies the word-count conversion first. The slowing is not only tempo: the pauses are longer and more frequent, because a young listener processes a sentence after it lands rather than during it, and the gap is where that happens. Sentences run shorter, one idea each, and a new word is given a beat of silence after it rather than before. A child reading subtitles is slower again, and that limit is a separate one — the reading-rate ceiling, not the speaking rate.  
**Effect on the audience:** Comprehension rather than compliance. A children's script read at an adult rate is not understood, and nothing in the delivery signals that it was not.  
**Used for and where it works best:** Children's narration that is spoken rather than sung — a story, an explainer, an alphabet or counting piece, a museum family track. Kids craft in this package is written mostly for hosted and sung content, and a spoken children's read had no rate of its own.  
**Best in:** formats: Kids Content, Educational, Museum Family Track | genres: Children's, Educational  
**Avoid when:** The piece is a song. The melody governs and the lyric craft in Phase 5 sets the timing.  
**Example:** `rate: preschool story narration at 105 wpm, one idea per sentence, a full beat of silence after each new word.`  
**Source:** assumption — the package's working figure, not a published standard; set the rate against the rendered audio and a test listener of the target age.  
**Yields to:** Authority: the melody, via the Phase 5 lyric craft — The piece is a song, melody governs timing.  
`pacing.wpm_children`


### Narrated Fiction Rate

**Also called:** storytelling voice-over rate, audiobook pace, the story-read tempo  
**What it is:** The planning rate for a story read aloud — a first-person or third-person narration of fiction, at any length, from a sixty-second storytelling reel to a full audiobook. **The figure is ACX's published average: "On average, most performers narrate about 9,300 words per hour."** 9,300 ÷ 60 = **155 words per minute**, about 2.58 words a second. It is the pace of *finished* audio — the pauses are inside it and the retakes are out of it — so it describes what a listener actually hears, and it is an average, not a ceiling and not a speed to push. **This card owns the narrated-fiction rate for the whole package**; where another file needs it, it cites this id rather than restating a figure. It combines in the order `pacing.wpm_to_camera` states — language, then audience, then delivery mode: an Arabic read takes its word-count conversion from `pacing.wpm_arabic` first, and a story told to children takes its number from `pacing.wpm_children`. As with every rate in this file, it is a planning estimate: `words ÷ 155` tells you roughly how much to write, and the length of the piece comes from the rendered audio file, measured (`pacing.locked_audio_timing`).  
**Effect on the audience:** A story told at the pace listeners are used to hearing stories told: unhurried enough to follow who is speaking and what just changed, quick enough that the scene keeps moving. Read at a sprint rate the scenes blur into a synopsis of themselves; read at a slow, reverent rate a story starts to sound like a ceremony about a story.  
**Used for and where it works best:** A narrated short story, a storytelling reel told in the first or third person, a fable or folk tale read over pictures, the narrator of an audio drama, an audiobook chapter. Dialogue quoted inside the narration is planned at the same rate; a scene played out by several voices instead of narrated takes its tempo from `pacing.wpm_dramatic_dialogue`. The silences a story needs beyond its ordinary breathing — a scene break, the held beat before a reveal — are designed with `pacing.pause_act_break` and `pacing.pause_dramatic_caesura`, and are measured in the render with everything else.  
**Best in:** formats: Short Film, Narrative Podcast, Audio Drama, Vertical Short-Form (Reels, Shorts, TikTok), Animated Series | genres: Drama, Mystery / Whodunit, Thriller / Suspense, Tragedy, Comedy, Horror, Mythology  
**Avoid when:** The piece is not a story. A documentary or heritage narration takes `pacing.wpm_documentary` or `pacing.wpm_vertical_heritage`, an explainer or a hook takes `pacing.wpm_social_reels`, and a presenter speaking to the lens takes `pacing.wpm_to_camera`. Also avoid treating 155 as a speed every line must hit: it is an average over a whole finished book, and inside it a chase runs faster and a death runs slower — plan the total from it and direct the scene by ear. A recited passage inside the story takes `pacing.wpm_epic_mythology`, and a sung one is timed by its melody, per the Phase 5 lyric craft.  
**Example:** `formula: total_words / 155 = duration_in_minutes | e.g. a 60-second storytelling reel ≈ 155 words; a 3,100-word short story ≈ 20 minutes read aloud; both pending_measured_duration until the render is measured.`  
**Source:** reference — ACX Help Center (Amazon / Audible), "Narrate an audiobook", under the heading "How long will my narrated audiobook be?", help.acx.com/s/article/producing-and-recording-your-audiobook, read 2026-09-23; the page shows no date. The per-minute and per-second figures are this card's arithmetic on ACX's per-hour average  
**Shelf life:** dated — review 2027-03. The figure is a marketplace's published planning average, not a craft fact; if ACX revises or withdraws it, this card follows the page.  
**Yields to:** `pacing.wpm_children` — the listener is a child: the audience rate wins the number, whatever the story. `pacing.wpm_social_reels` — the piece is an explainer or a hook, facts in a sequence rather than a story: it takes the sprint rate. `pacing.wpm_arabic` — an Arabic read: the word-count conversion and the band are that card's, applied first.  
`pacing.wpm_narrated_fiction`
---

### Ancient Epic & Hymnal Gravitas

**Also called:** 105 WPM epic weight, monumental cadence, liturgical pace  
**What it is:** A deliberate, slow cadence of 100 to 115 words per minute with heavy downbeats on operative nouns, evoking carved temple stone.  
**Effect on the audience:** Induces solemnity, historical scale, and sacred awe; makes words feel ancient, irreplaceable, and monumental.  
**Used for and where it works best:** Recitations from the Epic of Gilgamesh, opening prologues of biblical/historical epics, and ancestral memorials.  
**Best in:** formats: Feature Film Prologue, Heritage Audio Experience | genres: Heritage (civilisation-focused), Mythology, Faith / Biblical Epic  
**Avoid when:** Contemporary urban settings, quick technical summaries, or modern dialogue.  
**A piece may carry two registers, and on a vertical heritage reel it usually should.** A recitation
that opens a reel runs at this pace and the body that follows runs at
`pacing.wpm_vertical_heritage`; reading the whole script at 105 makes a sixty-second slot impossible,
and reading the recitation at 145 removes the one thing that made it sound ancient. Hold this pace
for the opening lines only — ten to fifteen seconds is usually the whole of it — and mark in the
script where the register changes, so the synthesis is directed rather than guessed. The length that
results is measured from the rendered file, not calculated.  
**Source:** assumption — the package's working figure, not a published standard; set it against the rendered audio.  
**Yields to:** the register the rest of the piece is in, for everything after the recited passage — `pacing.wpm_vertical_heritage` on a feed heritage reel in any aspect, `pacing.wpm_documentary` on horizontal long-form **and on a piece with no picture at all**, where there is no aspect ratio to choose by. This used to name the vertical card alone, which handed a picture-less piece to a card whose own text requires a shape it does not have.  
**On a long piece the recited register is not confined to the opening.** The ten-to-fifteen-second figure above is sized for a short-form hook. In a long-form or audio-only piece the same register recurs — every quoted tablet, every incantation — and each occurrence is marked in the script the same way, entered and left the same way. The rule is that the register is *declared at every change*, not that it happens once.  
**Example:** `pacing: 105 WPM | pauses: 800ms after major royal titles and geographic names. Register change marked at the end of the recitation.`  
`pacing.wpm_epic_mythology`

---

### Micro-Beat Comma Pause

**Also called:** the syntactic breath, 250ms comma pause, clause divider  
**What it is:** A tight, 200ms to 300ms pause built into the speech line to separate clauses and clarify semantic relationships.  
**Effect on the audience:** Prevents cognitive overload by allowing the listener's ear to group words into intelligible grammatical units.  
**Used for and where it works best:** Inside complex historical sentences involving lists of kings, cities, or dates.  
**Best in:** formats: All narration and dialogue | genres: All  
**Avoid when:** Frantic panic dialogue where commas should be deleted to force an breathless runaway read.  
**Example:** `text: "He conquered the northern valleys, rebuilt the canal, and crowned himself in Babylon."`  
**Source:** assumption — a working default for a clause divider, untested  
**Yields to:** `pacing.acceleration_build` — Frantic panic, commas deleted for a runaway read.  
`pacing.pause_micro_beat`

---

### Dramatic Caesura Pause

**Also called:** the revelatory pause, the silence before the drop, 1-second silence  
**What it is:** A deliberate 750ms to 1500ms silence inserted immediately before a shocking fact, unexpected twist, or tragic name is spoken.  
**Effect on the audience:** Suspends time; the audience leans forward subconsciously expecting the blow, magnifying the revelation's emotional impact.  
**Used for and where it works best:** Documentary act climaxes, murder reveals in true crime, and the discovery of lost cities or catastrophic betrayals.  
**Best in:** formats: Documentary Feature, Narrative Podcast, True Crime | genres: Mystery / Whodunit, True Crime, Drama  
**Avoid when:** Casual filler narration or low-stakes transitional sentences.  
**Example:** `text: "The seal did not belong to a scribe... [pause: 1.2s] It belonged to the queen."`  
**Source:** assumption — a working range for a revelatory pause, untested  
**Yields to:** `pacing.pause_micro_beat` — Low-stakes transitional lines needing a clause divider.  
`pacing.pause_dramatic_caesura`

---

### Act-Break Reset Silence

**Also called:** the chapter pause, 2-second breath, cognitive reset  
**What it is:** A full 2.0-second silence in narration accompanied by sustained music or ambience to mark the completion of a narrative movement.  
**Effect on the audience:** Allows emotional residue from the preceding scene to settle before demanding attention for the next chapter.  
**Used for and where it works best:** End of major documentary chapters, post-battle silences, and commercial act breaks.  
**Best in:** formats: Feature Film, Documentary Feature, Limited Series | genres: All  
**Avoid when:** Rapid montage sequences or frenetic social media reels.  
**These silences extend the runtime; they do not come out of the word count.** A requested duration
is an estimate, so a twenty-minute film with six act breaks finishing at 20:12 is correct, and the
picture is cut to the measured audio. In express mode, where the run completes on one upfront
confirmation and no one can accept the overrun, the total planned silence is subtracted from the
word budget instead — see `pacing.wpm_documentary`.  
**Example:** `timeline: [Narration line ends] -> 2000ms ambient wind bed -> [Next act narration begins]`  
**Source:** assumption — the package's working figure, not a published standard; set it by measuring the rendered audio.  
**Yields to:** `pacing.wpm_social_reels` in [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) — Frenetic reels and montage, stripped of dead air.  
`pacing.pause_act_break`

---

### Syllable Stress Mapping

**Also called:** operative word emphasis, rhetorical accentuation  
**What it is:** Marking the single most important word in a sentence to ensure the generative model puts dynamic weight on the idea rather than the syntax.  
**Effect on the audience:** Directs listener attention to the actual dramatic point, eliminating robotic flatline delivery.  
**Used for and where it works best:** In generative TTS, capitalise or italicize operative words (e.g. "He built *three* libraries, not one.") to enforce pitch peak.  
**Best in:** formats: All voiceover and dialogue | genres: All  
**Avoid when:** Over-stressing every adjective, which sounds like an aggressive infomercial.  
**Example:** `text: "They did not flee the fire. They ran *into* it."`  
`pacing.syllable_stress_mapping`

---

### Sentence Length Alternation

**Also called:** 3-speed rhythm, Gary Provost cadence, anti-monotony law  
**What it is:** Alternating short, medium, and long sentences (e.g., 5 words, 18 words, 3 words) to create musical variety in prose.  
**Effect on the audience:** Prevents auditory fatigue and hypnosis; keeps the listener's brain constantly re-engaging with varying cadence lengths.  
**Used for and where it works best:** Every paragraph of narration. A short sentence punches. A long sentence paints a complex landscape. A short one closes it.  
**Best in:** formats: All writing for audio and video | genres: All  
**Avoid when:** Staccato-only military checklists or unbroken Victorian run-on prose.  
**Example:** `pattern: "Nineveh stood. For two centuries, no army on earth dared to challenge her walls. Then came the flood."`  
**Yields to:** `pacing.acceleration_build` — When a deliberate staccato run is itself the effect.  
`pacing.sentence_length_variety`

---

### Locked Audio Measurement

**Also called:** audio-locked timebase, frame-accurate timing  
**What it is:** Deriving visual editing durations strictly from the measured duration of the approved audio master rather than arbitrary script estimates.  
**Effect on the audience:** Eliminates awkward visual holds or rushed cuts; ensures every visual transition lands on natural vocal pauses or musical beats.  
**Used for and where it works best:** Core pipeline handoff: Stage 4 renders the master WAV, extracts exact timestamps for every line, and hands them to Stage 5/6.  
**Best in:** formats: All video production | genres: All  
**Avoid when:** Editing video visuals first without locking audio, forcing voiceover to be artificially stretched or squashed.  
**Example:** `audio_master: line_1: 00:00.000 - 00:04.350 (Shot 1 duration = 4.35s / 104 frames @ 24fps).`  
**Source:** assumption — the example's figures are illustrative arithmetic (4.35 s at 24 fps = 104.4, rounded to 104 frames), not a published standard; take the real durations from the rendered audio.  
`pacing.locked_audio_timing`

---

### Inter-Character Turn Calibration

**Also called:** conversational gap, dialogue latency, turn-taking timing  
**What it is:** Calibrating the natural silence between one character finishing a line and the next character replying: 250ms to 450ms for normal conversation.  
**Effect on the audience:** Eliminates robotic instant snapping between speakers while avoiding dead air that drags the dramatic tension down.  
**Used for and where it works best:** All two-person dialogue scenes. Compress to 50ms for arguments; expand to 800ms for hesitant confessions.  
**Best in:** formats: Audio Drama, Feature Film, Drama Series Episode | genres: Drama, Comedy, Thriller  
**Avoid when:** Keeping a uniform 500ms gap for every single exchange regardless of emotional heat.  
**Example:** `scene_gap: speaker_a: "Where was he?" -> [gap: 150ms] -> speaker_b: "In the palace."`  
**Source:** assumption — the 250-450 ms band and the 50 ms and 800 ms extremes are working defaults, untested  
`pacing.dialogue_gap_calibration`

---

### Interruption and Overlap Engineering

**Also called:** dialogue collision, pre-emptive cut-off, speech clash  
**What it is:** Scripting a character's speech to collide with another character's final syllables (overlap of 200ms to 500ms) to simulate authentic friction.  
**Effect on the audience:** Conveys intense power struggle, impatience, or panic; pulls the audience into a chaotic, living argument.  
**Used for and where it works best:** Arguments, panic scenes in command centers, and rapid banter in screwball comedy.  
**Best in:** formats: Drama Series, Feature Film, Audio Drama | genres: Drama, Action, Comedy  
**Avoid when:** Formal courtroom procedures or educational documentaries where both lines must be clearly understood.  
**Example:** `track_1: "If we don't open the gates—" | track_2 (starts at -300ms): "The gates stay shut!"`  
**Source:** assumption — the package's working figure, not a published standard; set the overlap by ear on the mixed dialogue.  
**Yields to:** `pacing.dialogue_gap_calibration` — Courtroom or teaching, both lines must stay clear.  
`pacing.interruption_overlap`

---

### Sentence Tail Decay Control

**Also called:** vocal fry prevention, ending drop-off, terminal clarity  
**What it is:** Ensuring the final 2 to 3 words of a sentence maintain sufficient volume and pitch energy instead of trailing off into unintelligible mumbling.  
**Effect on the audience:** Guarantees critical punchlines, names, and dramatic conclusions are clearly audible above background foley and music.  
**Used for and where it works best:** Scripting terminal words with open vowel sounds or strong consonants; adding terminal punctuation that prevents TTS drop-off.  
**Best in:** formats: All voiceover | genres: All  
**Avoid when:** Deliberately scripting a dying breath or fainting character.  
**Example:** `technique: avoid ending with soft whispered monosyllables under loud music; end on resonant nouns.`  
`pacing.vocal_fry_and_tail_decay`

---

### Rhythmic Acceleration Build

**Also called:** tempo accelerando, tension crescendo, runaway beat  
**What it is:** Progressively shortening phrase lengths and increasing vocal delivery speed leading into a major revelation or catastrophe.  
**Effect on the audience:** Artificially elevates heart rate and anxiety in parallel with on-screen danger; creates an irresistible climax.  
**Used for and where it works best:** Chases, countdown sequences, battle preparations, and frantic investigative breakthroughs.  
**Best in:** formats: Feature Film, Trailer / Teaser, Short Film | genres: Thriller / Suspense, Action, Horror  
**Avoid when:** Calm analytical conclusions or serene landscape sequences.  
**Example:** `sequence: 14-word setup -> 8-word complication -> 4-word trigger -> 1-word detonation.`  
**Yields to:** `pacing.deceleration_landing` — Calm analytical conclusions, serene landscape endings.  
`pacing.acceleration_build`

---

### Philosophical Deceleration Landing

**Also called:** tempo ritardando, moral landing, meditative fade  
**What it is:** Gradually expanding vowel duration and doubling pause lengths on the final two sentences of a film or documentary.  
**Effect on the audience:** Signals the narrative journey has reached its profound conclusion; invites reflective contemplation on the universal meaning.  
**Used for and where it works best:** Final closing voiceover over wide landscape shots, monument ruins, and end-credit transitions.  
**Best in:** formats: Documentary Feature, Heritage Film, Drama | genres: Heritage (civilisation-focused), Philosophy, Tragedy  
**Avoid when:** Mid-credits teaser sequences or upbeat sequel hooks.  
**Example:** `text: "The stone crumbled... The rivers shifted course... But the clay tablets [pause: 1s] still speak."`  
**Source:** assumption — the package's working figure, not a published standard; set the pause by ear against the rendered audio.  
**Yields to:** `pacing.acceleration_build` — A mid-credits teaser or upbeat sequel hook.  
`pacing.deceleration_landing`
