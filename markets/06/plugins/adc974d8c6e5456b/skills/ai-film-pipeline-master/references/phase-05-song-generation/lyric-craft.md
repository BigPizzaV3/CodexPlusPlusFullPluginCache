# Lyric Craft & Song-to-Visual Architecture

8 cards. Writing singable lyrics, prosody, syllable rhythm, and mapping song structures into visual sequences.

---

### Name the Shape Before the Words

**Also called:** the lyric-craft selector, shape before words, which way does the song travel  
**What it is:** The card at the head of the `lyr.` shelf. It does not write a line. It asks the two questions the shelf's own boundaries ask — **is this a move some song would refuse, or a check every song takes, and which way does the song travel over its length** — and hands back the card for each answer. The axes were read off the shelf's `Avoid when:` fields and the one condition its `Yields to:` fields repeat; they were not invented. Every card named here is named by id.  
**Effect on the audience:** None. This card never reaches a listener. It exists so the shape that does reach the listener was chosen against where the song is going, rather than inherited from the last chorus that worked.  
**Used for and where it works best:** Answer the two questions **in order, out loud, one sentence each, before you open the shelf.** The first answer splits the file into the moves you choose between and the checks you run anyway; the second picks one move. Where a song wants two shapes at once — a chorus that comes back word for word and louder — that is two cards and both are legitimate; the shelf's commonest pairing is exactly that. **The three checks run on every draft whatever the two answers were.**  
**Best in:** formats: Song Lyric, Music Video, Lyric Video, Children's Song, Folk Anthem, Ballad | genres: All  
**Avoid when:** **You need more than one question answered.** This map can see very little: of the shelf's four pair fields, one stays on the shelf and three leave it, and a family many times its size, `lyric.`, holds the alternatives it cannot. On any question beyond *which way does the song travel*, the answer is one family over. Also avoid it when the song goes through without returning or stays deliberately level: both exits leave the shelf, and the map then has nothing to hand you but three checks. And **distrust its *check every song takes* value for `lyr.prosody` whenever a voice is meant to stumble** — a child singing, a drunk, a character losing control. The package holds a near-twin of that card, `lyric.stress_alignment`, that permits exactly the deliberate misplaced stress this one forbids, and this map files the stricter of the two as a law. Finally, **do not run the shelf's two halves at the same moment**: `lyr.prosody` and `lyr.concrete_nouns` shape lines while they are being written, while `lyr.structure_map` and `lyr.opening_image_returns` work on a song whose sections and images already exist. When the song and its video are both being made, finish the writing pass first, then run the picture pass against the locked structure.  
**Example:** `selector_run: first "chosen — a named song would refuse it" -> second "it comes back, the same words" -> card: lyr.repetition_as_feature; then run lyr.prosody, lyr.concrete_nouns and lyr.tied_to_this_song on the draft.`  

---

**The axes**

**Axis 1 — Would any song refuse it, or does every song take it?**
Asked first, because the shelf's `Avoid when:` fields answer it themselves and split cleanly. **Four cards name a song that refuses them:** *"When the visual edit deliberately runs in aggressive counterpoint against the song, which must be declared as a deliberate concept"* (`lyr.structure_map`), *"The song's own structure is circular with zero emotional movement"* (`lyr.opening_image_returns`), *"Complex through-composed avant-garde art music where thematic disorientation is the artistic point"* (`lyr.repetition_as_feature`), *"Flat-line ambient tracks where dynamic changes are intentionally suppressed"* (`lyr.dynamic_energy_ramp`). **Three name no song at all.** `lyr.prosody`'s `Avoid when:` is the failure itself — *"Forcing an unstressed syllable (like "the" or "of") onto an accented musical downbeat"*; `lyr.tied_to_this_song`'s is the failure itself — *"Generic party or dancing footage that possesses zero narrative relation to the lyrics being sung"*; and `lyr.concrete_nouns` refuses only what is not a song — *"Academic essays or complex theoretical discourse."* A field that forbids *not using* the card is *always do this* written backwards, and a fork cannot be built on it. **Checked against `PAIR-AUDIT.md`, the split falls on exactly the same line:** the four carry a `Yields to:`; the three are filed as having no alternative. Two instruments, one boundary.

**Axis 2 — Which way does the song travel over its length?**
The only condition on the shelf that repeats — four times, counting the one that arrives from outside: *"The song is circular with no emotional movement for a return to transform"* (`lyr.opening_image_returns`, which yields to the verbatim repeat), *"Through-composed work where thematic disorientation is the artistic point"* (`lyr.repetition_as_feature`, which yields out of the shelf), *"Flat-line ambient beds where dynamic change is deliberately suppressed"* (`lyr.dynamic_energy_ramp`, which yields out of the shelf), and from the hook shelf, `hook_psych.motif_inversion_recontextualization` sending a reader to `lyr.repetition_as_feature` on *"Static loop grooves: repeat the motif, do not re-harmonise."* Every one of them is a statement about **movement** — does the song come back, climb, or stand still — and not about how the song feels. `lyr.structure_map` belongs on this axis too: its question is whether the picture travels with the song's sections or against them.

---

**The map**

**Axis 1 — refused by some song, or taken by every song**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Chosen — a named kind of song would refuse it** (four) | `lyr.structure_map` · `lyr.opening_image_returns` · `lyr.repetition_as_feature` · `lyr.dynamic_energy_ramp` |
| **Checked — every song takes it, and it runs on the draft whatever you chose** (three) | `lyr.prosody` · `lyr.tied_to_this_song` · `lyr.concrete_nouns` |

**Axis 2 — which way the song travels**

| Answer | The card, by id |
| :--- | :--- |
| **It comes back changed — the same image, a different meaning** | `lyr.opening_image_returns` |
| **It comes back the same — the same words, and the return is the pleasure** | `lyr.repetition_as_feature` |
| **It climbs — each chorus arrives higher and denser than the verse before it** | `lyr.dynamic_energy_ramp` |
| **It goes where its own sections go, and the picture is cut to them** | `lyr.structure_map` |
| **Any way at all — these hold whatever the shape** (three) | `lyr.prosody` · `lyr.tied_to_this_song` · `lyr.concrete_nouns` |

**And the three ways out, each named by a card that leaves.** A song that never comes back is `lyric.through_composed`, on another shelf. A song that stays level is `score.minimalist_suspense_drone`, on another shelf too, in Phase 4. A picture that fights the song is `sound_realize.counterpoint_test`, in a family `SHELVES.md` excludes from the shelves as rules — a boundary, not a route.

*A card appears once per axis. On the chosen side the answer is one card wide; the checked cards are not answers, they are what every answer is checked against.*

**One card in this map disagrees with its twin in the next family, and the map routes to it anyway.** `lyr.prosody` holds that stress on the beat is *"Non-negotiable in anthems and children's songs."* `lyric.stress_alignment` does the same job by the same method and says it *"can be deliberately violated for one word to signal strain, drunkenness, a child singing, or a character whose control is slipping."* They collide on the children's song. **Not settled here** — but a writer giving a child's voice a stumble should know both cards exist and which one they are obeying.

---

**The default, and the one against it**

**The default is `lyr.repetition_as_feature` with `lyr.dynamic_energy_ramp` — the chorus that comes back word for word and hits harder — and the measurement does not earn it.** `lyr.repetition_as_feature` is the only card on this shelf that anything routes to, and it is reached twice: from `lyr.opening_image_returns` (*"The song is circular with no emotional movement"*) and from `hook_psych.motif_inversion_recontextualization` (*"Static loop grooves"*). **Both fire on one condition — the song has stopped moving.** By the rule that counts distinct conditions rather than edges, that makes it a door, not a fallback: the place a reader is sent when a song stalls. **No card on the shelf earns the default by in-degree**, because only one card has any. It is named on the cards' own authority instead: `lyr.repetition_as_feature` claims the widest home on the shelf — *"Pop singles, anthems, folk choruses, and educational songs"* — and `lyr.dynamic_energy_ramp` claims *"All verse-to-chorus transitions."* **The stated runner-up is `lyr.structure_map`**, whose `Used for` claims *"Every song lyric and music video"* — it loses because it governs the picture laid on a song, not the song.

**The one against it is `lyr.opening_image_returns`.** Nothing routes to it anywhere in the package. It keeps the default's return and moves its meaning: the default brings back the same words so the listener arrives home; this brings back the same image so the listener finds home changed — the warrior by the cold river becomes the warrior at the rebuilt gate. Its stated cost is its own boundary, a circular song. **And it has a cost it does not state, which a card in the next family does:** `lyric.refrain_mutation` warns that *"a congregation or a crowd cannot follow a refrain that changes."* So on a sing-along the two are not rivals — **keep the default's words verbatim and let this card move the picture.** The chorus the crowd sings stays the same; what it means by the last one does not.

---

**The unasked**

**Six of the shelf's working cards are the target of no `Yields to:` field anywhere in the package.** By id:

`lyr.structure_map` · `lyr.tied_to_this_song` · `lyr.opening_image_returns` · `lyr.prosody` · `lyr.concrete_nouns` · `lyr.dynamic_energy_ramp`

**And the shape of that list is the finding: the only thing anyone is ever sent to on this shelf is the verbatim repeat, and only when a song has stalled.** Everything that makes a song *move* — the climb, the changed return, the sections carried into the picture — is unasked. The package consults this shelf as a repair for a song that has stopped, and never as a plan for a song that is going somewhere.

The second thing the list shows: **the three checks are unreachable by construction.** A law is not an alternative to anything, so no reader holding one card ever writes *not this — that one* toward it.

The third: **the card this shelf wants already exists, one family over, and nothing here points at it.** Between the verbatim repeat and the transformed final return there is a middle — a refrain that changes one element on every return, so the repetition itself carries the story — and that is `lyric.refrain_mutation`, which also carries the crowd boundary the changed-return card lacks. It is the clearest case of a pattern that runs through the whole shelf: at least three of these cards have a near-twin in `lyric.` — `lyr.prosody` and `lyric.stress_alignment` (which disagree), `lyr.repetition_as_feature` and `lyric.verse_chorus_bridge` (which leave by the same exit, for different reasons), `lyr.opening_image_returns` and `lyric.refrain_mutation`. **This shelf is sparse not because it is small but because its alternatives live next door.**

`lyr.shape_before_the_words`

---

### Map the Song, Not the Location

**Also called:** the song structure map, musical architecture blueprint  
**What it is:** Organizing visual and emotional movements strictly by the song's musical architecture (intro, verse, pre-chorus, chorus, bridge, outro) rather than geographical locations.  
**Effect on the audience:** Prevents jarring cuts that fight the music; camera movements and scene shifts land in harmony with musical phrase changes.  
**Used for and where it works best:** Every song lyric and music video. The song is already a structured architectural foundation; borrowing it is free.  
**Best in:** formats: Song Lyric, Music Video, Lyric Video, Trailer | genres: All  
**Avoid when:** When the visual edit deliberately runs in aggressive counterpoint against the song, which must be declared as a deliberate concept.  
**Example:** `timeline_spec: Section 1 (0:00-0:15) Intro -> Section 2 (0:15-0:45) Verse 1 -> Section 3 (0:45-1:10) Chorus.`  
**Yields to:** `sound_realize.counterpoint_test` — The edit deliberately runs in aggressive counterpoint against the song.  
`lyr.structure_map`

---

### Tied to This Song

**Also called:** the swap test, bespoke song concept  
**What it is:** Testing that every lyric line and visual concept is inextricably tied to the specific melody and emotional core of this individual track.  
**Effect on the audience:** The audience feels the work was born from genuine inspiration rather than generic stock imagery pasted over audio.  
**Used for and where it works best:** The swap test: if the concept could be swapped onto three other random songs without friction, it has failed and must be rewritten.  
**Best in:** formats: Song Lyric, Music Video, Single Track | genres: All  
**Avoid when:** Generic party or dancing footage that possesses zero narrative relation to the lyrics being sung.  
**Example:** `concept_audit: Every metaphor in Verse 2 directly mirrors the Akkadian myth recounted in the chorus lyrics.`  
`lyr.tied_to_this_song`

---

### The Opening Image, Transformed

**Also called:** the cyclical return, transformed refrain, narrative bookend  
**What it is:** Returning to the visual image or lyrical hook of the opening during the final chorus or outro, fundamentally transformed by what occurred between.  
**Effect on the audience:** Triggers profound recognition; the audience perceives the entire emotional arc without requiring clumsy exposition.  
**Used for and where it works best:** Heroic anthems, epic ballads, and narrative concept albums.  
**Best in:** formats: Song Lyric, Music Video, Ballad | genres: Epic, Drama, Folk  
**Avoid when:** The song's own structure is circular with zero emotional movement.  
**Example:** `opening: Solitary warrior sitting by cold river; outro: Same warrior standing among rebuilt city gates.`  
**Yields to:** `lyr.repetition_as_feature` — The song is circular with no emotional movement for a return to transform.  
`lyr.opening_image_returns`

---

### Stress on the Beat (Prosody)

**Also called:** poetic prosody, singability law, metric alignment  
**What it is:** Aligning the natural spoken stress of syllables with the strong musical beats, long notes and melodic peaks so the melody pronounces the words correctly.  
**Effect on the audience:** The line sings effortlessly and feels completely natural; the listener can sing along on second listen without stumbling.  
**Used for and where it works best:** Every lyric in every language. Non-negotiable in anthems and children's songs.  
**Best in:** formats: Song Lyric, Musical Theatre, Commercial Jingle | genres: All  
**Avoid when:** Forcing an unstressed syllable (like "the" or "of") onto an accented musical downbeat. The one exception, outside anthems and children's songs, is a single word misplaced on purpose to signal strain or a slipping voice, which `lyric.stress_alignment` allows only when the rest of the song is clean.  
**Example:** `line_test: "RÍ-ver of wá-ter, bún-dle of réeds" (natural trochaic meter matching 4/4 drum downbeats).`  
`lyr.prosody`

---

### Repetition as a Core Feature

**Also called:** the predictable chorus, mnemonic anchor, anthemic hook  
**What it is:** Repeating the chorus lyrics verbatim, using recurring melodic motifs, and echoing key lyrical hooks across song sections.  
**Effect on the audience:** Provides psychological comfort, memorability, and shared communal singing; anticipation of the chorus is the main pleasure.  
**Used for and where it works best:** Pop singles, anthems, folk choruses, and educational songs.  
**Best in:** formats: Pop Song, Folk Anthem, Children's Song | genres: Pop, Folk, Anthem  
**Avoid when:** Complex through-composed avant-garde art music where thematic disorientation is the artistic point.  
**Example:** `chorus: "Nineveh falls, the river remains. / Nineveh falls, the river remains." (hypnotic verbatim repetition).`  
**Yields to:** `lyric.through_composed` — Through-composed work where thematic disorientation is the artistic point.  
`lyr.repetition_as_feature`

---

### Concrete Nouns & Short Words

**Also called:** the one-and-two-syllable rule, tactile lyricism  
**What it is:** Building lyrics primarily from tangible, concrete nouns (stone, bread, river, fire, shield) and 1-to-2 syllable action verbs.  
**Effect on the audience:** Creates immediate visual cinema in the listener's imagination; prevents lyrics from sounding like a dry academic lecture.  
**Used for and where it works best:** Emotional folk songs, epic historical ballads, and bilingual songs.  
**Best in:** formats: Song Lyric, Folk Ballad, Anthem | genres: Folk, Heritage, Epic  
**Avoid when:** Academic essays or complex theoretical discourse.  
**Example:** `lyric: "He held the stone. He drank the rain. He watched the fire take the grain." (100% concrete monosyllables).`  
`lyr.concrete_nouns`

---

### Dynamic Energy Ramp

**Also called:** song dynamics curve, verse-to-chorus lift, power swell  
**What it is:** Ensuring the chorus possesses significantly higher dynamic energy, wider vocal range, and denser instrumentation than the preceding verse.  
**Effect on the audience:** Delivers an involuntary physical rush of excitement (goosebumps) when the chorus hits.  
**Used for and where it works best:** All verse-to-chorus transitions. Raise vocal melody by a third or fourth, add drums, and thicken vocal harmonies.  
**Best in:** formats: Pop Single, Epic Anthem, Rock Ballad | genres: Pop, Rock, Epic  
**Avoid when:** Flat-line ambient tracks where dynamic changes are intentionally suppressed.  
**Example:** `verse: Intimate acoustic Oud + single quiet male vocal; chorus: Thundering frame drums + full choir, melody up a fourth, harmonies stacked. The lift is written into the arrangement, not added with a fader.`  
**Yields to:** `score.minimalist_suspense_drone` — Flat-line ambient beds where dynamic change is deliberately suppressed.  
`lyr.dynamic_energy_ramp`
