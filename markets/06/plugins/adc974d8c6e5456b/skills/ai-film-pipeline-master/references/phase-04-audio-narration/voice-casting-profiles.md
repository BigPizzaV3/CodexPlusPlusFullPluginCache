# Voice Casting & Archetypal Profiles

19 cards. Archetypal vocal profiles engineered for generative TTS, defining pitch range, resonant placement, age color, breathing style, and emotional stance across all genres.

---

### Authoritative Historical Narrator

**Also called:** the museum voice, David Attenborough register, elder statesman of truth  
**What it is:** A deep, resonant, unhurried baritone or warm mature alto with measured cadence and absolute factual credibility.  
**Effect on the audience:** Disarms skepticism immediately; the audience assumes every statement has been verified across archaeological archives.  
**Used for and where it works best:** Monumental history, civilization documentaries, museum guides, and serious investigative retrospectives.  
**Best in:** formats: Documentary Feature, Heritage / Historical Documentary, Video Essay | genres: Historical / Biopic, Heritage (civilisation-focused), Science  
**Avoid when:** High-energy social media hooks, frenetic comedies, or teenage character dialogue.  
**Example:** `profile: age: 55-65 | pitch: low baritone | speed: the rate on the register's pacing card | timbre: rich, warm, slight chest resonance | steadiness: high (even)`  
**Yields to:** `voice.cast_hook_retention_reels` — High-energy social hooks.  
`voice.cast_authoritative_historian`

---

### Mythological Ancient King

**Also called:** the bronze sovereign, epic monarch, Gilgamesh voice  
**What it is:** A commanding, gravelly, thunderous voice that carries the weight of decree, divine lineage, and tragic hubris.  
**Effect on the audience:** Evokes ancient stone palaces, monumental inscriptions, and terrifying royal power; commands awe and dread.  
**Used for and where it works best:** Sumerian, Akkadian, and Assyrian mythological epics, declarations of war, temple prayers, and tragic king monologues.  
**Best in:** formats: Feature Film, Cinematic Animation, Trailer / Teaser | genres: Mythology / Ancient Epic, Tragedy, Fantasy  
**Avoid when:** Casual modern conversations or underplayed naturalist slice-of-life scenes.  
**Example:** `profile: age: 45-55 | pitch: very deep | speed: the rate on the register's pacing card | timbre: gravelly, cavernous, iron weight | style amplifier: as its adapter advises`  
**Yields to:** `voice.cast_intimate_memoir` — Casual modern conversation, naturalist slice-of-life.  
`voice.cast_epic_mythological`

---

### Intimate First-Person Confessor

**Also called:** bedside voice, microphone proximity read, diary speaker  
**What it is:** A close-mic, soft, breathy vocal delivery with audible inhalations and vulnerability, speaking as if inches from the listener's ear.  
**Effect on the audience:** Creates an unbreakable emotional bond; makes the viewer feel like a trusted confidant receiving a secret never meant for public air.  
**Used for and where it works best:** Personal memoirs, post-trauma reflections, inner monologues, and tender romantic moments.  
**Best in:** formats: Narrative Podcast, Short Film, Drama Series Episode | genres: Memoir, Drama, Psychological / Arthouse, Romance  
**Avoid when:** Large public crowds, battlefield speeches, or corporate promotional videos.  
**Example:** `profile: proximity: 2 inches | pitch: mid-soft | speed: the rate on the register's pacing card | breathiness: high | steadiness: low (expressive)`  
**Yields to:** `voice.cast_corporate_visionary` — Crowds, battlefield speeches, projection required.  
`voice.cast_intimate_memoir`

---

### High-Retention Social Hook Narrator

**Also called:** retention master, dopamine cadence, TikTok alpha voice  
**What it is:** A punchy, forward-placed, high-energy delivery with zero warm-up, sharp consonants, and immediate dynamic attack on the first syllable.  
**Effect on the audience:** Halts thumb-scrolling within the first 400 milliseconds; prevents drop-off during the critical 3-second hook window.  
**Used for and where it works best:** Opening lines of YouTube Shorts, TikToks, and Instagram Reels; high-impact facts and mystery hooks.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok) | genres: Informational, True Crime, Viral Science, Entertainment  
**Avoid when:** Contemplative endings, funeral scenes, or serious academic discussions.  
**Example:** `profile: attack: instant | pitch: bright tenor | speed: the rate on the register's pacing card | dynamics: compressed, punchy | steadiness: medium`  
**Yields to:** `voice.cast_scholarly_analyst` — Serious academic or contemplative material.  
`voice.cast_hook_retention_reels`

---

### Warm Pedagogical Guide

**Also called:** the beloved educator, patient instructor, Sagan cadence  
**What it is:** A gentle, enthusiastic, reassuring voice that smiles through the syllables, breaking complex concepts into wonder-filled discoveries.  
**Effect on the audience:** Eliminates intellectual intimidation; makes learning feel thrilling, accessible, and deeply comforting.  
**Used for and where it works best:** Children's educational media, astronomy/nature documentaries for families, and gentle historical introductions.  
**Best in:** formats: Children's Series, Educational Short, Family Documentary | genres: Educational / Science, Family, Kids / Animation  
**Avoid when:** Gritty crime scenes, horrific warfare descriptions, or sarcastic satire.  
**Example:** `profile: age: 40-50 | tone: smiling, curious | speed: the rate on the register's pacing card | cadence: melodic upward lilt | steadiness: medium`  
**Yields to:** `voice.cast_cynical_noir` — Gritty crime, horrific warfare.  
`voice.cast_child_warm_educator`


### Designed Child Voice

**Also called:** synthetic child character, generated young voice, the designed child  
**What it is:** A child character voiced by a **fully synthetic voice, designed from a written description and built on no real child's voice** — no recording, no sample and no clone of any real minor anywhere in its making. It is one of three ways this phase can voice a child; the others are an adult performer playing young and a real child's own voice, recorded or cloned. The design brief describes the character, never a person: apparent age, placement, brightness, and how this child breathes and hesitates.  
**Effect on the audience:** A child who sounds like a child, without the adult weight a grown narrator carries into the part. Done badly it lands in the uncanny middle — too clean, too even, a child who never stumbles — and the audience hears a product instead of a character.  
**Used for and where it works best:** A child character in animation, an animated kids series, a family story, a narrated fable, a heritage piece told through a child's eyes. **Design, do not borrow**: write the voice description from the character sheet, generate candidates, and keep the one that fits the character. **A child's read is not an adult's read pitched higher**: give it breath in odd places, small restarts and uneven stress, and let steadiness sit in the middle rather than high. Where a designed voice has to be moved younger, the shift is `dubbing.formant_shifting_calibration`'s; where two children, or a child and an adult, share a scene, keep them apart with `pronounce.character_voice_contrast`. The speaking rate follows the audience, not the character: `pacing.wpm_children` in [`pacing-cadence-wpm.md`](pacing-cadence-wpm.md) when the piece is made for children, the register's own pacing card when it is not.  
**Best in:** formats: Children's Series, Educational Short, Cinematic Animation, Short Film, Audio Fiction / Audio Drama, Folklore Short | genres: Kids / Animation, Family, Folklore, Fantasy, Drama  
**Avoid when:** The brief names a real child — a son, a niece, a child actor, a child heard in a clip — and wants that voice: then the voice is not designed but recorded or cloned, and it is cast from that recording like any other voice; only the cloning step waits for the parent's or guardian's consent, recorded in `child_voice_clone_consent` in `project.yaml`, and the rest of the work carries on, under `elevenlabs.voice_cloning_hygiene`. Also avoid it for an adult voice speaking to children, which is `voice.cast_child_warm_educator`.  
**Example:** `profile: apparent age: the character's, as the script gives it | pitch: light, high placement | speed: the rate on the register's pacing card | timbre: clear, unforced, no adult chest resonance | breath: audible, in odd places | steadiness: medium | source: designed from a written description, no real child's recording`  
**Yields to:** `elevenlabs.voice_cloning_hygiene` — the brief wants a real child's own voice, recorded or cloned, rather than a designed one. `voice.cast_child_warm_educator` — the voice is an adult speaking to children, not a child character.  
`voice.cast_designed_child`
---

### World-Weary Noir Detective

**Also called:** cynical investigator, cigarette gravel, midnight monologist  
**What it is:** A dry, raspy, exhausted baritone speaking between teeth, marked by rhythmic cynicism and a refusal to be surprised by human depravity.  
**Effect on the audience:** Envelopes the scene in shadows, moral ambiguity, and inescapable melancholy; sets an immediate hardboiled tone.  
**Used for and where it works best:** Neo-noir thrillers, detective voiceovers, crime scene investigations, and dystopian cyberpunk narratives.  
**Best in:** formats: Feature Film, Audio Fiction / Audio Drama, Short Film | genres: Crime / Procedural, Film Noir, Mystery / Whodunit  
**Avoid when:** Optimistic corporate ads, children's content, or bright romantic comedies.  
**Example:** `profile: age: 48-58 | pitch: low, dry | speed: the rate on the register's pacing card | inflection: flat, unamused | steadiness: medium`  
**Yields to:** `voice.cast_warm_commercial_guide` — Optimistic corporate ads, bright material.  
`voice.cast_cynical_noir`

---

### Archaic Chieftain / Sovereign

**Also called:** imperious lawgiver, iron tongue, the Code of Hammurabi  
**What it is:** An unyielding, stone-faced delivery that speaks with the finality of engraved granite; lacks vocal hesitation or pleading.  
**Effect on the audience:** Instills the dread of an empire where commands are absolute and mercy must be bought with submission.  
**Used for and where it works best:** Proclaiming ancient laws, royal edicts, demanding vassal tribute, and pronouncing judgment.  
**Best in:** formats: Historical Epic, Cinematic Game Cutscene | genres: Heritage (civilisation-focused), War, Historical  
**Avoid when:** Friendly banter, light-hearted scenes, or vulnerable romantic moments.  
**Example:** `profile: cadence: unyielding, metric | pitch: resonant bass | speed: the rate on the register's pacing card | pauses: long, heavy | steadiness: high (even)`  
**Yields to:** `voice.cast_intimate_memoir` — Friendly, light-hearted or vulnerable moments.  
`voice.cast_ancient_ruler`

---

### Traumatized Eyewitness

**Also called:** frantic survivor, broken rhythm, panic recall  
**What it is:** A fragile, erratic voice characterized by shallow breathing, broken sentence fragments, and involuntary pitch jumps.  
**Effect on the audience:** Pulls the audience directly into the horror of an ongoing or recently witnessed catastrophe; eliminates emotional detachment.  
**Used for and where it works best:** Disaster recollections, wartime civilian accounts, horror reveals, and intense trial depositions.  
**Best in:** formats: Documentary Series, Found Footage Horror, Drama | genres: Horror, War, Tragedy, True Crime  
**Avoid when:** Composed institutional summaries or promotional corporate voiceovers.  
**Example:** `profile: breathing: shallow, rapid | pitch: unsteady | speed: fluctuating around the rate on the register's pacing card | steadiness: low (expressive)`  
**Yields to:** `voice.cast_scholarly_analyst` — Composed institutional summary.  
`voice.cast_frenzied_eyewitness`

---

### Crisp Academic Dissector

**Also called:** forensic analyst, clinical scholar, oxford seminar tone  
**What it is:** A clear, precise, analytical delivery with razor-sharp diction, neutral detachment, and surgical pacing.  
**Effect on the audience:** Establishes intellectual superiority and clinical neutrality; lets grim or shocking facts speak without melodrama.  
**Used for and where it works best:** Forensic documentaries, strategic military breakdowns, archaeological decipherment, and medical exposés.  
**Best in:** formats: Video Essay, Analytical Documentary, True Crime | genres: Documentary, True Crime, Science  
**Avoid when:** Passionate romantic pleas or high-action kinetic trailers.  
**Example:** `profile: diction: impeccable | emotion: 0.05 | speed: the rate on the register's pacing card | pauses: precise 300ms | steadiness: high (even)`  
**Source:** assumption — the package's working figure, not a published standard; set it by ear against the rendered audio.  
**Yields to:** `voice.cast_corporate_visionary` — High-action kinetic trailers.  
`voice.cast_scholarly_analyst`

---

### Warm Commercial Brand Ambassador

**Also called:** lifestyle narrator, approachable companion, friendly guide  
**What it is:** A bright, resonant, warmly smiling mid-register voice that radiates positivity, reliability, and effortless comfort.  
**Effect on the audience:** Builds immediate trust, warmth, and affinity; makes the viewer receptive to the message or product.  
**Used for and where it works best:** Brand films, lifestyle commercials, tourist heritage invitations, and community spotlights.  
**Best in:** formats: Commercial / TVC, Brand Film, Tourism Campaign | genres: Commercial, Lifestyle, Travel / Heritage  
**Avoid when:** Severe tragedy, dark horror, or solemn memorial pieces.  
**Example:** `profile: pitch: bright mid | tone: uplifting, warm | speed: the rate on the register's pacing card | smiles: audible | steadiness: medium`  
**Yields to:** `voice.cast_intimate_memoir` — Severe tragedy, solemn memorial.  
`voice.cast_warm_commercial_guide`

---

### Silky Cold Antagonist

**Also called:** polite menace, calculating villain, silk over razor  
**What it is:** A quiet, beautifully modulated, almost musical voice that delivers monstrous ultimatums with terrifying elegance and calm.  
**Effect on the audience:** Elicits chills far deeper than shouting; makes the villain feel intellectual, unstoppable, and completely in control.  
**Used for and where it works best:** Antagonist monologues, high-stakes psychological confrontations, and aristocratic conspiracies.  
**Best in:** formats: Feature Film, Drama Series, Cinematic Game | genres: Psychological Thriller, Mystery, Drama, Sci-Fi  
**Avoid when:** Crass comedic antagonists or brute mindless monsters.  
**Example:** `profile: volume: soft, controlled | pitch: smooth baritone | speed: the rate on the register's pacing card | menace: understated | steadiness: high (even)`  
`voice.cast_dramatic_villain`

---

### The Opposed Pair: Two Voices in Conflict

**Also called:** the antagonist pair, the argument cast, casting by contrast, the two-hander that collides  
**What it is:** Casting the two sides of a conflict as one decision rather than two separate profiles: the second voice is chosen against the first, apart in pitch and apart in the size of the voice (vocal-tract length, heard as timbre), so the ear can keep each line with its speaker while the lines overlap, interrupt and cut each other off.  
**Effect on the audience:** When the voices separate cleanly, overlap becomes drama and the audience tracks who is winning line by line. When they do not, overlap becomes noise, the listener stops following the fight, and the scene loses the one thing it was built for.  
**Used for and where it works best:** Arguments, interrogations, rival kings, a parent against a grown child, any scene where one line lands on top of the other, and every audio drama or narration-over-dialogue scene where no face shows who is speaking. Three levers, in the order of strength the study below measured: a pitch gap of more than two semitones helps; a vocal-tract difference of about 8 percent (one voice audibly bigger) helps; both together, the shift that reads as a change of sex, helps more than either alone, and a different-sex pair separates best of all. So a same-sex pair needs both levers, not one. `pronounce.character_voice_contrast` sets the pitch gap for any two-hander; this card adds the second lever for the case where the two voices collide. Keep each side's delivery apart too (steady against unsteady, slow against fast), because the study found that separation fell for talkers whose intonation varied most between utterances.  
**Best in:** formats: Audio Fiction / Audio Drama, Feature Film, Drama Series, Animated Series | genres: Drama, Thriller, Historical, Mythology  
**Avoid when:** The two characters are meant to be heard as one voice split in two (twins, a doubled self, a conscience) and the confusion is the point.  
**Example:** `pair: A: low, large, slow, steady | B: 4 semitones higher, shorter vocal tract (smaller, brighter), faster, unsteady | overlap: B cuts in on A's last word | check: both lines readable with the picture off`  
**Source:** reference — Darwin, Brungart and Simpson, "Effects of fundamental frequency and vocal-tract length changes on attention to one of two simultaneous talkers", Journal of the Acoustical Society of America 114(5):2913-2922 (2003), https://doi.org/10.1121/1.1616924, abstract at https://pubmed.ncbi.nlm.nih.gov/14650025/, checked 2026-09-24; supports F0 differences greater than 2 semitones improving attention to one of two simultaneous talkers, vocal-tract length ratios of 1.08 or greater improving it, the combined shift improving it more than either alone, a different-sex talker improving it most, and the gain being smallest for talkers with the most variable intonation. The four-semitone example is the package's margin over that threshold.  
**Yields to:** `pronounce.character_voice_contrast` — The two speakers never overlap and the picture always shows who is talking, so a pitch gap alone separates them.  
`voice.cast_opposed_pair`

---

### Hypnotic Bedtime Bard

**Also called:** sleep storyteller, dream weaver, meditative cadence  
**What it is:** An ultra-soothing, deep, rhythmic voice with descending inflections at phrase endings and warm acoustic diffusion.  
**Effect on the audience:** Lowers heart rate, induces deep relaxation, and invites the mind into meditative, dream-like suspension.  
**Used for and where it works best:** Bedtime stories, mythological origin tales, guided meditations, and atmospheric dream sequences.  
**Best in:** formats: Audio Meditation, Sleep Story, Atmospheric Essay | genres: Fantasy, Mythology, Relaxation  
**Avoid when:** Fast-paced tutorials, urgent calls to action, or high-stakes action scenes.  
**Example:** `profile: pitch: deep, soft | speed: the rate on the register's pacing card | inflection: downward glides | steadiness: high (even)`  
**Yields to:** `voice.cast_hook_retention_reels` — Urgent calls to action, fast tutorials.  
`voice.cast_bedtime_storyteller`

---

### Relentless Investigative Journalist

**Also called:** Woodward cadence, relentless seeker, questioning voice  
**What it is:** A driven, focused vocal delivery that leans forward on every line, characterized by rising questioning inflections and steady moral urgency.  
**Effect on the audience:** Makes the audience feel like co-investigators uncovering a conspiracy that cannot be ignored.  
**Used for and where it works best:** Investigative podcast series, political corruption exposés, and true crime deep dives.  
**Best in:** formats: Narrative Podcast, Investigative Documentary | genres: Political Thriller, True Crime, Journalism  
**Avoid when:** Lyrical poetry, mindless escapist entertainment, or celebratory brand reels.  
**Example:** `profile: tempo: forward-leaning | speed: the rate on the register's pacing card | inflection: questioning, incisive | steadiness: medium`  
**Yields to:** `voice.cast_warm_commercial_guide` — Celebratory brand reels.  
`voice.cast_investigative_reporter`

---

### Dry Satirical Commentator

**Also called:** ironic deadpan, arched eyebrow, satirical wit  
**What it is:** A crisp, deliberately understated delivery that presents absurdity with complete gravity, letting the irony explode in the listener's head.  
**Effect on the audience:** Provokes intellectual laughter and sharp agreement; flatters the viewer's intelligence by avoiding obvious joke punches.  
**Used for and where it works best:** Political satire, dark comedies, social critiques, and wry essayist pieces.  
**Best in:** formats: Video Essay, Dark Comedy Short, Satirical Sketch | genres: Comedy, Satire, Essay  
**Avoid when:** Sincere emotional memorials or unironic heroic tributes.  
**Example:** `profile: tone: absolute deadpan | pitch: dry mid | speed: the rate on the register's pacing card | irony: implicit | steadiness: high (even)`  
**Yields to:** `voice.cast_corporate_visionary` — Unironic heroic tributes.  
`voice.cast_satirical_cynic`

---

### Village Elder Oral Historian

**Also called:** campfire custodian, tribal memory, ancient grandfather  
**What it is:** An aged, weathered voice with a slight rasp, deliberate pauses, and the organic musicality of oral storytelling passed down generations.  
**Effect on the audience:** Connects the audience to ancestral heritage; feels like sitting at the knee of a grandfather who remembers what the books forgot.  
**Used for and where it works best:** Folklore, indigenous oral histories, Mesopotamian flood myths, and generational sagas.  
**Best in:** formats: Cultural Documentary, Folklore Short, Heritage Film | genres: Heritage (civilisation-focused), Folklore, Drama  
**Avoid when:** Modern high-tech product launches or slick urban dramas.  
**Example:** `profile: age: 70+ | texture: weathered rasp | speed: the rate on the register's pacing card | rhythm: oral narrative pulse | steadiness: low (expressive)`  
**Yields to:** `voice.cast_corporate_visionary` — Modern high-tech product launches.  
`voice.cast_folkloric_elder`

---

### Regional Iraqi Dialect Voice (Maslawi and Baghdadi)

**Also called:** Maslawi voice, Mosul Arabic, Baghdadi voice, qeltu and gelet casting, city-dialect casting  
**What it is:** Casting a voice for one Iraqi city's dialect by the features a native listener checks first, rather than by a general "Iraqi accent". Iraqi Arabic splits into two broad groups named for how each says "I said": the qeltu dialects of the north, Mosul's among them, and the gelet dialects of the south and of Baghdad's Muslims. Qeltu keeps qaf as [q] and the -tu ending; gelet turns qaf into [g] and ends in -it. Traditional Mosul speech also has a uvular r, a throaty r near gh, where gelet has a tongue-tip r, and an o-like vowel where other dialects say u.  
**Effect on the audience:** A native listener places the speaker within a word, and places a wrong one just as fast: a Mosul character with a Baghdadi [g] is heard as an actor, not as a man from Mosul.  
**Used for and where it works best:** Characters whose city is part of who they are; heritage and diaspora pieces; a scene between a Mosul and a Baghdad character, where the two dialects do the separating work of `voice.cast_opposed_pair`. Age is part of the cast: in Mosul the uvular r and the traditional vowels are receding among younger speakers while [q] holds at every age, so a grandmother and a grandson from the same house can differ in the r and share the q, and a young Maslawi with a plain r is accurate, not a slip. Religion was once part of it in Baghdad: its Christian and Jewish communities spoke qeltu dialects, closer to Mosul than to their Muslim neighbours. Cast a native speaker of that city, or have one hear a generated voice before it is locked.  
**Best in:** formats: Drama Series, Feature Film, Documentary, Audio Fiction / Audio Drama, Animated Series | genres: Drama, Heritage (civilisation-focused), Family, Comedy  
**Avoid when:** The line must reach every Arabic speaker rather than place the speaker in one city, which is the choice `dubbing.fusha_vs_dialect_cadence` owns. Also when the character comes from nowhere in particular and a city accent would give him a biography the story does not.  
**Example:** `profile: dialect: Maslawi (qeltu) | qaf: [q] | "I said": qeltu | r: uvular for the elder, tongue-tip for the grandson | vowel: o where Baghdad says u, elder only | check: a native Mosul speaker hears the first take`  
**Source:** reference — Abdulkareem Yaseen Ahmed, "Phonological variation and change in Mesopotamia: a study of accent levelling in the Arabic dialect of Mosul", PhD thesis, Newcastle University, 2018, https://theses.ncl.ac.uk/jspui/bitstream/10443/4345/1/Ahmed%20A%20Y%202018.pdf, checked 2026-09-24; supports the qeltu/gelet split after Blanc, Communal Dialects in Baghdad (Harvard University Press, 1964): [q] and -tu in qeltu, [g] and -it in gelet, gelet spoken by the Muslims of Baghdad and Lower Mesopotamia, Christian and Jewish Baghdadi Arabic among the qeltu dialects, uvular r as a qeltu feature; and, for Mosul, the uvular r and the traditional [o] vowel receding in younger speakers while [q] is maintained by all speakers.  
**Yields to:** `dubbing.fusha_vs_dialect_cadence` — The line must reach every Arabic speaker, not place the speaker in one city.  
`voice.cast_regional_iraqi_dialect`

---

### Inspiring Visionary Founder

**Also called:** keynote leader, inspiring pioneer, manifest destiny  
**What it is:** An energetic, resonant, forward-looking delivery combining passion, unshakable conviction, and rhythmic pauses for dramatic applause.  
**Effect on the audience:** Inspires collective optimism, ambition, and excitement about the future or grand historical achievements.  
**Used for and where it works best:** Civilizational triumph pieces (building the Ishtar Gate, conquering space), brand manifestos, and inspirational shorts.  
**Best in:** formats: Trailer / Teaser, Brand Manifesto, Epic Documentary | genres: Epic, Inspirational, Technology  
**Avoid when:** Intimate funeral laments or quiet reflective poetry.  
**Example:** `profile: tone: triumphant, bold | speed: the rate on the register's pacing card | projection: stadium resonance | steadiness: medium`  
**Yields to:** `voice.cast_intimate_memoir` — Intimate funeral laments, quiet reflective poetry.  
`voice.cast_corporate_visionary`
