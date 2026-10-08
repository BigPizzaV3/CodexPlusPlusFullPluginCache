# Pronunciation, Accents & Phonetic Directing

17 cards. Directing generative TTS engines on ancient languages, cuneiform names, phonetic transliteration, Semitic consonants, and accent authority.

---

### Phonetic Respelling for Generative TTS

**Also called:** phonetic guide, phonetic spelling, syllables for AI  
**What it is:** The art of breaking complex historical, foreign, or ancient words into hyphenated, capitalization-stressed phonetic syllables in the prompt.  
**Effect on the audience:** Eliminates painful, laughable AI mispronunciations of heritage names, ensuring flawless professional authority.  
**Used for and where it works best:** Every historical script containing Akkadian, Sumerian, Assyrian, Babylonian, Greek, or Arabic names. Use the same respelling keys that `pronounce.mesopotamian_names` and the project dictionary record, so one name is spelled one way everywhere.  
**Best in:** formats: All historical and cultural narration | genres: Heritage (civilisation-focused), History  
**Avoid when:** Common English words where phonetic respelling causes unnatural robotic vowel elongation.  
**Example:** `text: "King ash-ur-BAH-nee-pahl commanded the scribes to gather every tablet in NIN-eh-veh."`  
**Yields to:** `pronounce.homograph_disambiguation` — A common English word that is a heteronym.  
`pronounce.phonetic_spelling_tts`

---

### Mesopotamian Royal & Geographic Names

**Also called:** cuneiform name guide, Assyrian/Babylonian names  
**What it is:** Standardized phonetic pronunciation keys for major Mesopotamian kings, cities, and landmarks for ElevenLabs models.  
**Effect on the audience:** Preserves historical dignity and authentic scholarship across international audiences.  
**Used for and where it works best:** Scripts featuring Ashurbanipal, Tiglath-Pileser, Sennacherib, Nebuchadnezzar, Hammurabi, Sargon, Esarhaddon, Sin-shar-ishkun, Ur, Uruk, and Nineveh.  
**Best in:** formats: Heritage / Historical Documentary, Epic Film | genres: Heritage (civilisation-focused), History  
**Avoid when:** Inventing a respelling from the English letters alone when the skill or a quick search gives one.  

**This card is a starting set, not a closed list**, and a script will run past it almost immediately —
twelve names is a fraction of the Mesopotamian corpus, and any real documentary carries kings, cities,
gods, canals and titles that are not here. That is expected and it is not a defect in the card. What
matters is what you do at the thirteenth name, because the failure mode is silent: an invented
phonetic spelling looks exactly like a researched one on the page, and it is only wrong out loud,
after it has been recorded.

So, for any name not on this card:

1. **Look before you respell.** Not from the English letters, not from a name that looks
   similar, and not from another card — a Syriac or Arabic-layer name is a different language and
   takes `pronounce.syriac_christian_names` instead.
2. **Take it in this order, before it is recorded:** the skill (this card, the canon), then a web
   search — a cuneiform dictionary, an Assyriological reference, a museum's own audio guide, a
   scholar's recorded talk, a speaker of the living language — then, when nothing turns up, the
   closest reasonable respelling built from the name's known parts. The order matters: after the
   render, a wrong name costs a re-record and every shot cut to that line. Record the choice under
   `decisions` and continue; where the respelling still wants a native check,
   `pending_pronunciation_source` travels beside it as a note in the handoff, never as a hold (the
   marker: [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) §3).
3. **Write down where it came from** beside the spelling — which source, which page or which person,
   and the date. A phonetic key with no provenance is indistinguishable from a guess the next time
   somebody reads it.
4. **Add it to the project's own pronunciation sheet, not to this card.** The sheet travels with the
   project and is handed to whoever records; the card is the shared starting set and stays stable.
   A name added here on one project's authority becomes a package-wide claim nobody checked.  
**Unsourced, pending a source, name by name.** A search today — for a British Museum or Penn Museum audio guide, an Assyriologist's published pronunciation guide (including Karen Radner, *Ancient Assyria: A Very Short Introduction*, Oxford University Press, 2015), and for each of the twelve names below plus Nimrud, Khorsabad, Ashurnasirpal and *lamassu* — found no museum audio guide and no Assyriologist's pronunciation guide covering any of them. What does exist for some of these names (Cambridge Dictionary, PronounceNames.com and similar sites) is general-purpose English pronunciation, not a source on the ancient name, so it is not used here. So the respellings below are working choices: use them, record them under `decisions`, and let `pending_pronunciation_source` travel beside them as a note, per step 2 above — never a hold.  
**Example:** `guide: Ashurbanipal -> ash-ur-BAH-nee-pahl | Tiglath-Pileser -> TIG-lath pih-LEE-zer | Sennacherib -> seh-NAK-er-ib | Nebuchadnezzar -> neb-yoo-kud-NEZ-er | Hammurabi -> ham-oo-RAH-bee | Sargon -> SAR-gon | Esarhaddon -> ee-sar-HAD-on | Sin-shar-ishkun -> sin-shar-ISH-koon | Gilgamesh -> GILL-guh-mesh | Enkidu -> EN-kee-doo | Uruk -> OO-rook | Nineveh -> NIN-eh-veh.`  
**Example, a name that is not on the card:** `sheet_row: Dur-Sharrukin -> <respelling> | source: <the named source or native speaker it came from, and the date> | note, if it still wants a native check: pending_pronunciation_source | added to: project pronunciation sheet, not to pronounce.mesopotamian_names`  
**Yields to:** `pronounce.syriac_christian_names` — A Syriac or Arabic-layer name, a different linguistic layer.  
`pronounce.mesopotamian_names`

---

### Syriac, Chaldean and Late-Antique Christian Names

**Also called:** Syriac name guide, Church of the East names, late-antique place names
**What it is:** Phonetic keys for the names a Syriac Christian subject actually carries — the schools, the monasteries, the teachers, the sees — which are a different linguistic layer from the cuneiform kings and cannot be taken from the same card.
**Effect on the audience:** A Syriac, Chaldean or Assyrian audience hears a mispronounced saint or a mispronounced city as ignorance, in a way a general audience never notices. Getting these right is what tells them the piece was made by someone who knows them.
**Used for and where it works best:** Anything on the School of Nisibis, Edessa, the Church of the East, Syriac Orthodox subjects, the lives of teachers and saints, and modern Assyrian, Chaldean and Syriac stories.
**Best in:** formats: Documentary, Heritage Short, Kids Song | genres: Late-Antique Christian, Syriac Heritage, Religious History
**Avoid when:** A pre-330 BC Mesopotamian subject — those names take `pronounce.mesopotamian_names`. And never guess: where a name is not on this card, take the pronunciation from a Syriac source or from a native speaker before it is recorded, and write down where it came from.

**This card is a starting set, not a closed list.** Fourteen names does not cover the Church of the
East, and a script on the schools, the sees or the lives of the teachers will pass the end of it
quickly. That is expected. The procedure at the name that is not here is the same four steps the
Mesopotamian card states, and it is worth repeating because this is the layer where a wrong name is
most audible to the audience that cares: **do not guess a phonetic spelling**; **take it from a named
Syriac source or from a native speaker, before it is recorded** — a priest, a deacon, a Syriac
scholar, a liturgical recording; **write down where it came from**, which source or which person and
the date; and **add it to the project's own pronunciation sheet, not to this card**, because the
sheet travels with the project while the card is the shared set that stays stable. A name added here
on one project's authority becomes a package-wide claim nobody checked.
**Example:** `guide: Nisibis -> NISS-ih-biss | Nusaybin (modern Turkish) -> noo-sigh-BEEN | Edessa -> eh-DESS-uh | Urhoy (Syriac) -> OOR-hoy | Narsai -> NAR-sigh | Barsauma -> bar-SAW-ma | Ephrem -> EF-rem | Mar (title) -> MAR | Mopsuestia -> mop-soo-ESS-tee-uh | Ctesiphon -> TESS-ih-fon | Seleucia -> seh-LOO-shuh | Qenneshre -> ken-NESH-reh | Tur Abdin -> toor ab-DEEN | Beth Zabdai -> beth ZAB-die.`
**Yields to:** `pronounce.mesopotamian_names` — A pre-330 BC Mesopotamian subject.  
`pronounce.syriac_christian_names`

---

### Semitic Consonant Transliteration

**Also called:** Arabic and Akkadian consonants, gutteral handling  
**What it is:** Adapting Semitic phonemes (`ʿAyn`, `Hah`, `Qaf`, `Khah`) into English phonetic equivalents that generative TTS engines can articulate smoothly.  
**Effect on the audience:** Balances authentic cultural sound with broad listener intelligibility, avoiding awkward glottal chokes in the AI model.  
**Used for and where it works best:** Mesopotamian deity names (Inanna, Shamash), Arabic geographical locations (Ahwar, Baghdad, Mosul, Euphrates).  
**Best in:** formats: Cultural Documentaries, Middle Eastern Heritage | genres: Heritage (civilisation-focused), Documentary  
**Avoid when:** Overloading English TTS models with raw Arabic Unicode characters that cause the engine to crash or speak Arabic unexpectedly. And a Syriac, Chaldean or Church of the East name: its audience hears an adapted saint or city as ignorance, so it takes the source-exact form `pronounce.syriac_christian_names` requires, not a smoothed English equivalent. And the spoken target comes from the skill, then a search (a native speaker's recording, a dictionary), then the closest reasonable form; the respelling encodes that choice, recorded under `decisions`.  
**Example:** `text: "Across the reed marshes of al-AH-wahr, the fishermen sang the ancient hymns."`  
`pronounce.arabic_transliteration`

---

### Iambic vs Trochaic Stress Calibration

**Also called:** historical syllabic stress, metre preservation  
**What it is:** Ensuring the correct syllable receives the primary pitch accent (e.g. `BAB-ih-lon`, not `bab-ee-LON`; `mes-oh-poh-TAY-mee-uh`).  
**Effect on the audience:** Prevents the awkward, jarring cadence of amateur text-to-speech engines that misplace word stress.  
**Used for and where it works best:** Polysyllabic ancient names and archaeological terminology.  
**Best in:** formats: All voiceover | genres: All  
**Avoid when:** Leaving four-syllable foreign words un-hyphenated in the prompt.  
**Example:** `text: "The kingdom of E-lam [EE-lahm] surrendered after seven days."`  
`pronounce.stress_and_meter`

---

### Regional Accent Authority Selection

**Also called:** accent casting, regional credibility, cultural voice  
**What it is:** Consciously choosing the accent profile (e.g., Cultured British RP, Neutral Mid-Atlantic, Warm Middle Eastern English) to match project authority.  
**Effect on the audience:** Establishes cultural proximity and dramatic legitimacy; British RP signals classical museum authority; Middle Eastern English signals native heritage custody.  
**Used for and where it works best:** Choosing ElevenLabs voice clones based on audience expectation and historical authenticity.  
**Best in:** formats: Documentary Feature, Video Essay | genres: Heritage (civilisation-focused), History, Travel  
**Avoid when:** Generic mid-western American broadcast voice on ancient Near Eastern sacred epics.  
**Example:** `casting: "Middle Eastern English (refined, educated, resonant)" for Iraqi heritage series.`  
**Yields to:** `voice.cast_epic_mythological` — An ancient Near Eastern sacred epic, not a broadcast accent.  
`pronounce.accent_regional_authority`

---

### Foreign Term Integration Without Pedantry

**Also called:** seamless foreign integration, naturalized terminology  
**What it is:** Introducing foreign cultural terms (e.g. *Ziggurat*, *Cuneiform*, *Stele*) with naturalized fluency rather than pausing with academic pedantry.  
**Effect on the audience:** Treats the viewer as an insider; avoids breaking narrative immersion with awkward linguistic apologies.  
**Used for and where it works best:** Narrative history where archaeological terms must flow seamlessly as part of living speech.  
**Best in:** formats: Documentary, Narrative Podcast | genres: Historical, Cultural  
**Avoid when:** Exaggerated hyper-correct pronunciation that sounds pompous and stops the sentence cold.  
**Example:** `text: "The ziggurat rose sixty meters into the desert sky." (fluent, unhesitating read)`  
`pronounce.foreign_term_integration`

---

### Cuneiform Deity Titles & Invocations

**Also called:** divine epithets, god names, sacred titles  
**What it is:** Phonetic and vocal directing for ancient Mesopotamian pantheon invocations: Marduk, Enlil, Ishtar, Ea, Shamash, Sin, Nergal.  
**Effect on the audience:** Conveys the divine terror, awe, and cosmic authority associated with Bronze Age deities.  
**Used for and where it works best:** Temple scenes, omens, battle curses, and mythological retellings.  
**Best in:** formats: Epic Film, Mythology Series, Animation | genres: Mythology / Ancient Epic, Faith / Biblical Epic  
**Avoid when:** Speaking god names with casual, dismissive modern inflection. And guessing the key for a god not in this card's example: the same four steps as `pronounce.mesopotamian_names` apply — a named source or a native speaker, recorded with its date, on the project's own sheet.  
**Example:** `text: "By the command of MAR-dook, sovereign lord of the heavens, the foundations were laid."`  
`pronounce.cuneiform_deity_titles`

---

### Geographic Landmark Pronunciation Guide

**Also called:** river and mountain keys, topographical accuracy  
**What it is:** Explicit phonetic keys for ancient and modern topographical features: Tigris, Euphrates, Zagros, Mount Ararat, Persian Gulf, Diyala.  
**Effect on the audience:** Grounds the physical journey in accurate geographic reality.  
**Used for and where it works best:** Documentary maps, military campaign narratives, and trade route breakdowns.  
**Best in:** formats: Historical Documentary, Educational Video | genres: History, Geography, Heritage  
**Avoid when:** Mispronouncing Euphrates or Zagros on a historical broadcast. And guessing a key for a river, mountain or site not in this card's example: take it from a named source or a native speaker, record where it came from, and put it on the project's own sheet, as `pronounce.mesopotamian_names` sets out.  
**Example:** `guide: Euphrates -> yoo-FRAY-teez | Tigris -> TY-gris | Zagros -> ZAH-gros.`  
`pronounce.geographic_landmarks`

---

### Archaic Diction Without Pomposity

**Also called:** biblical register, epic cadence, solemn vocabulary  
**What it is:** Using elevated, archaic syntactic structures without degenerating into unreadable "thee/thou" renaissance-faire parody.  
**Effect on the audience:** Imparts timeless, epic weight to the narration while maintaining 100% contemporary comprehension.  
**Used for and where it works best:** Epic myth narration, translation of royal cuneiform inscriptions, and tragic memorials.  
**Best in:** formats: Feature Film Prologue, Heritage Audio | genres: Mythology, Heritage, Tragedy  
**Avoid when:** Cramming archaic pronouns into casual character dialogue.  
**Example:** `text: "He saw the secret things. He knew the hidden ways. He brought back tales of the days before the flood."`  
`pronounce.archaic_diction_rhythm`

---

### Homograph Disambiguation Protocol

**Also called:** TTS word disambiguation, heteronym correction  
**What it is:** Resolving words spelled identically but pronounced differently depending on part of speech (e.g. read/read, tear/tear, lead/lead, live/live).  
**Effect on the audience:** Eliminates absurd TTS mistakes where the AI picks the wrong tense or noun form.  
**Used for and where it works best:** Pre-flight script sanitization: replace ambiguous spellings with phonetic equivalents (e.g. `he red the tablet`, `a tier fell from her eye`).  
**Best in:** formats: All TTS audio generation | genres: All  
**Avoid when:** Leaving homographs unverified before paid API batch execution.  
**Example:** `prompt_sanitization: change "The lead soldier" -> "The leed soldier" or "The led soldier" based on meaning.`  
`pronounce.homograph_disambiguation`

---

### Number, Date & Era Spoken Expansion

**Also called:** date spelling rules, era formatting for TTS  
**What it is:** Writing all dates, currencies, and numbers in fully spelled-out spoken English rather than digits (e.g. "twenty-four hundred B-C", not "2400 BC").  
**Effect on the audience:** Prevents the AI model from awkwardly pronouncing "two thousand four hundred bee-see" or "two four zero zero".  
**Used for and where it works best:** Every historical documentary script before feeding to ElevenLabs or voice talent.  
**Best in:** formats: All voiceover scripts | genres: All  
**Avoid when:** Leaving raw numerical digits in the audio column of the shooting script.  
**Example:** `text: "In the year six hundred and twelve B-C, Nineveh was consumed by flame."`  
`pronounce.number_and_date_handling`

---

### Acronym & Initialism Spelling

**Also called:** initialism expansion, letter-by-letter directing  
**What it is:** Directing the model whether to spell out initials (hyphenated letters: `U-N-E-S-C-O`) or pronounce as an acronym (`UNESCO`).  
**Effect on the audience:** Guarantees institutional terms and archaeological registries are read according to standard professional convention.  
**Used for and where it works best:** Institutional names, museum inventory codes, and scientific terminology.  
**Best in:** formats: Documentary, Educational | genres: Documentary, Science  
**Avoid when:** Inconsistent pronunciation of the same organisation within the same video.  
**Example:** `text: "Registered under U-N-E-S-C-O World Heritage protocol."`  
`pronounce.acronym_and_spelling`

---

### Syntactic Breath Commas

**Also called:** breathing commas, prosodic phrasing  
**What it is:** Inserting commas at syntactic phrasing boundaries specifically to give the generative model an auditory inhalation and reset point.  
**Effect on the audience:** Eliminates robotic runaway sentences, providing clean, human-sounding paragraph delivery.  
**Used for and where it works best:** Long compound sentences in documentary voiceover.  
**Best in:** formats: All TTS scripts | genres: All  
**Avoid when:** Over-commaing every two words, which produces a stuttering, asthma-like performance.  
**Example:** `text: "When the waters receded, and the mud dried beneath the sun, they laid the first brick."`  
`pronounce.breath_pause_commas`

---

### Dialectical Consistency Across Takes

**Also called:** dialect locking, pronunciation continuity  
**What it is:** Maintaining identical pronunciation of character names and geographic terms across multiple scenes, episodes, and takes.  
**Effect on the audience:** Protects narrative continuity; prevents the jarring distraction of a name changing pronunciation halfway through a film.  
**Used for and where it works best:** Multi-scene projects, series, and multi-day generation sessions. Maintain a shared project pronunciation dictionary.  
**Best in:** formats: All serialized or multi-scene projects | genres: All  
**Avoid when:** Allowing different voice models or regeneration takes to invent their own syllable stress.  
**Example:** `project_dictionary: {Enheduanna: "En-hed-oo-AN-na", Ashurbanipal: "ash-ur-BAH-nee-pahl", Uruk: "OO-rook", Tigris: "TY-gris"}.`  
**Source:** owner decision, 2026-09-23 - the package's canonical respellings of Enheduanna (`En-hed-oo-AN-na`) and Ashurbanipal (`ash-ur-BAH-nee-pahl`). Until then the package spelled the first three ways and the second two, and no reference inside it gave a pronunciation, so the owner chose. Every respelling of either name in the package uses these; a change starts here.  
`pronounce.dialect_consistency`

---

### Vocal Frequency Separation for Dialogue

**Also called:** character voice contrast, acoustic casting separation  
**What it is:** Casting two voices in a scene with distinct fundamental frequencies (e.g. low baritone vs bright tenor, or warm alto vs crisp soprano).  
**Effect on the audience:** Enables the audience to instantly distinguish who is speaking without glancing at the screen or checking subtitles.  
**Used for and where it works best:** All two-person dialogue scenes and multi-character audio dramas.  
**Best in:** formats: Audio Fiction / Audio Drama, Feature Film, Drama Series | genres: Drama, Mystery, Comedy  
**Avoid when:** Casting two actors with identical vocal timbre and pitch in a fast-paced dialogue scene.  
**Example:** `casting: Speaker A: 110Hz fundamental baritone; Speaker B: 210Hz fundamental tenor.`  
**Yields to:** `char.idiolect_sheet` — Separate the speakers by how they speak, when timbres cannot differ.  
`pronounce.character_voice_contrast`

---

### Recurring Name Re-Anchoring

**Also called:** the phonetic shelf, name re-introduction  
**What it is:** Re-anchoring the correct pronunciation and title of a complex historical figure when they reappear after an absence of several scenes.  
**Effect on the audience:** Refreshes the listener's memory and confirms they are tracking the same historical actor.  
**Used for and where it works best:** Long-form documentaries and complex historical epics with dozens of royal names.  
**Best in:** formats: Documentary Feature, Limited Series, Book | genres: Historical / Biopic, Heritage (civilisation-focused)  
**Avoid when:** Assuming the audience remembers a minor king's name introduced 45 minutes earlier.  
**Example:** `text: "The Assyrian king, Ashurbanipal — whose grandfather had marched to Egypt — now turned eastward."`  
`pronounce.name_repetition_shelf`
