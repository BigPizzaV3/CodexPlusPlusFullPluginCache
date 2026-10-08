# Lyric, Verse, Refrain and Song Structure

Category: `lyric`

**Part 1 of 4.** 32 cards across form and architecture, the hook and the repeating parts, prosody and singability, rhyme, song types and their jobs, language and re-versioning, and named failure modes.

A lyric is not a poem with a tune attached. It is text built to survive being sung once, at speed, by a body with lungs, to a listener who cannot rewind. Every card below is judged against that.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Form and Architecture](#form-and-architecture)
- [The Hook and the Repeating Parts](#the-hook-and-the-repeating-parts)
- [Prosody and Singability](#prosody-and-singability)
- [Rhyme](#rhyme)
- [Song Types and Their Jobs](#song-types-and-their-jobs)
- [Language, Version and Screen](#language-version-and-screen)
- [Named Failure Modes](#named-failure-modes)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## Form and Architecture

### Verse-Chorus-Bridge Spine

**Also called:** VCB, the modern pop spine, verse/chorus/bridge form
**What it is:** Verses carry new information, the chorus returns unchanged as the emotional home, and a single contrasting bridge arrives after the second chorus to break the cycle before the last one.
**Effect on the audience:** Gives the listener a place they already know to come back to, so new lines in the verse cost them no effort. The bridge arriving late feels like the song finally admitting something.
**Used for and where it works best:** The default when the song has one central feeling and two or three pieces of evidence for it. The craft rule: verse lines should be the only place new facts enter, and every verse must earn the same chorus differently — if chorus 2 lands identically to chorus 1, the verse between them did no work. Related: `scene.value_turn` applies inside a verse as much as inside a scene.
**Best in:** formats: pop single, worship song, kids song | genres: pop, country, rock, gospel
**Avoid when:** The story genuinely moves in one unbroken line — a ballad of a death, a confession — where returning to the same chorus makes the narrator sound stuck. The failure mode is a chorus that becomes a wall the story keeps bouncing off.
**Example:**
> Verse 1: I kept your coat behind the door all winter.
> Chorus: And I'm still not cold, I'm still not cold, I'm still not cold without you.
> Verse 2: I gave the coat away in June to a stranger.
> Chorus (same words, new weight): And I'm still not cold, I'm still not cold, I'm still not cold without you.

**Yields to:** `lyric.through_composed` — One unbroken irreversible line; a returning chorus strands the narrator.  
`lyric.verse_chorus_bridge`

---

### AABA Thirty-Two Bar Form

**Also called:** 32-bar form, standard song form, ballad form, the Tin Pan Alley form
**What it is:** Eight bars of A, the same A again with new words, eight bars of contrasting B (the release or middle eight), then A once more. There is no separate chorus — the title and hook live inside A.
**Effect on the audience:** Feels like a complete thought spoken twice, interrupted by a doubt, then reasserted. Very close to the shape of an argument someone actually makes.
**Used for and where it works best:** Reach for it when the song is one idea examined from three angles rather than a story with events, and when the singer is the main instrument. The craft rule: A3 must use the same words as A1 in at least its last line but mean something different, because B has changed what the words cost. This is the same turn-then-return logic as `struct.kishotenketsu` compressed into thirty-two bars.
**Best in:** formats: song lyric, musical theatre, kids song | genres: traditional pop, musical theatre, soul
**Avoid when:** The arrangement needs a big repeated chorus for a crowd to shout. AABA has no room for that and forcing one on top produces a song with two competing hooks. Also weak on streaming openings — the hook sits at the end of A, not at second five.
**Example:**
> A1: I said I'd travel light, and I did.
> A2: I said I'd leave by noon, and I did.
> B: Nobody asked me why the door stayed open, why the lamp burned through the afternoon —
> A3: I said I'd travel light. And I did.

**Yields to:** `lyric.verse_chorus_bridge` — A crowd needs a big repeated chorus to shout.  
`lyric.aaba_form`

---

### Through-Composed Lyric

**Also called:** no-repeat form, continuous form, durchkomponiert
**What it is:** No section returns. Every stretch of the song has its own words and usually its own melodic material, so the form is the shape of the events rather than a container for them.
**Effect on the audience:** Removes the safety of return. The listener leans forward because nothing tells them where they are in the song, and the ending genuinely cannot be predicted.
**Used for and where it works best:** Use it when the subject is a single irreversible sequence — a journey, a trial, a night that ends badly — and when repeating any line would be a lie about time. The craft rule that makes it survivable: replace structural repetition with a repeated *image* rather than a repeated section, so the listener still has a thread. That thread is `theme.thematic_motif` doing the job a chorus would otherwise do.
**Best in:** formats: song lyric, musical theatre, documentary | genres: hip-hop, musical theatre
**Avoid when:** The song has to be learnable, singable back, or licensable as a hook-driven single. The real failure mode is a four-minute piece nobody can recall one line of ten minutes later — impressive while playing, gone on arrival.
**Example:**
> He counted the bridge lamps. Eleven.
> He counted the boats. None.
> By the twelfth lamp he was not counting anything,
> and the river had already made its decision without him.
> (no section here returns; the count is the thread)

**Yields to:** `lyric.verse_chorus_bridge` — Song must be learnable, singable back, hook-driven.  
`lyric.through_composed`

---

### The Pre-Chorus Lift

**Also called:** the climb, the rise, the ramp, the channel, the B-section
**What it is:** Four to eight bars between verse and chorus whose only job is to raise pressure — usually shorter lines, rising pitch, tighter rhyme, and a syntax that does not finish.
**Effect on the audience:** Physically braces the listener. They know something is about to land even on a first listen, which makes the chorus feel inevitable rather than merely next.
**Used for and where it works best:** Add one when the verse is conversational and the chorus is large — the gap between those two registers is where songs die. The craft rule: the pre-chorus should end on an unresolved grammatical unit ("and every time you —", "so if it's true that —") so the chorus completes the sentence. Shorten line lengths as you climb; long lines cannot lift.
**Best in:** formats: pop single, anthem, trailer | genres: pop, rock
**Avoid when:** The chorus is quiet or the song's power is understatement — a lift then a whisper reads as a mixing error. And never add one just because a section feels missing; a pre-chorus with no pressure to add is the most obvious filler in modern pop.
**Example:**
> Verse ending: We talked about the weather like adults.
> Pre-chorus: And the room got small,
> and the room got loud,
> and every single thing I didn't say —
> Chorus: — is still in this house.

**Yields to:** `lyric.delayed_rhyme` — Chorus is quiet; bind it by holding a rhyme instead.  
`lyric.prechorus_lift`

---

### The Bridge's Job

**Also called:** middle eight, the release, the turn, the B-section of a VCB
**What it is:** A single non-repeating section, usually after the second chorus, that changes the vantage point — new information, a confession, a time jump, or a switch of who is being addressed.
**Effect on the audience:** Breaks the loop just as the pattern was becoming furniture, and sends the listener back into the final chorus hearing it differently.
**Used for and where it works best:** Write the bridge last and only after you can say in one sentence what the listener still does not know. The craft rule: a bridge must either reveal, reverse, or re-address — new fact, opposite position, or turning to speak to someone else. If it does none of those it is a third verse in a hat. Pairing it with `info.delayed_decoding` is the strongest version: the bridge finally explains an image the verses used without explaining.
**Best in:** formats: pop single, musical theatre, worship song | genres: pop, country, rock, soul, gospel
**Avoid when:** The song is under two minutes, or the chorus is already doing the reveal. Forcing a bridge into a short song produces the classic failure: eight bars of restated theme that every listener uses to check their phone.
**Example:**
> (after chorus 2, first time the song addresses the mother directly)
> You were twenty-three. You had a coat like mine.
> Nobody told me that. I found it in a drawer.
> — and back into the final chorus, which now means something else.

**Yields to:** `lyric.aaba_form` — Song under two minutes; use the compressed B release.  
`lyric.bridge_turn`

---

### Title Line Placement

**Also called:** hook line siting, title position, the money line
**What it is:** Deciding exactly where the title phrase falls inside a section — first line of the chorus, last line, both, or hidden at the end of each verse — because its position decides whether it functions as a heading or a punchline.
**Effect on the audience:** Title first announces and is easy to learn. Title last resolves and pays off the lines that set it up. Title first and last brackets the chorus and is the hardest to forget.
**Used for and where it works best:** Put the title first when the phrase is the idea and the rest of the chorus explains it. Put it last when the phrase only means something after a setup — especially when it is a common phrase you are twisting. The craft rule: say the title out loud alone. If it needs context to land, it must be last; if it lands cold, it can be first.
**Best in:** formats: single, worship song, kids song, title sequence, jingle | genres: pop, country, worship, rock, hip-hop
**Avoid when:** The title is abstract and the melody at that position is weak — a title line sitting on a throwaway note gets skipped by the ear no matter how many times it repeats. Also avoid burying a title mid-chorus, where it neither announces nor resolves.
**Example:**
> Title last (setup then payoff):
> You can keep the photographs, keep the garden, keep the name —
> I'm taking back the quiet.
>
> Same title, first (announcement):
> I'm taking back the quiet.
> You can keep the photographs, the garden and the name.

`lyric.title_line_placement`

---

## The Hook and the Repeating Parts

### Hook Siting

**Also called:** hook placement, the catch, front-loading the hook
**What it is:** The hook is the shortest fully memorable unit of the song — often the title phrase on its melodic figure. Siting it means choosing how early the listener meets it and how often it returns.
**Effect on the audience:** Early contact buys patience; the listener who has already heard the payoff will sit through a verse to get back to it. Late contact buys weight but only holds an audience that has already committed.
**Used for and where it works best:** On streaming and short-form platforms, get the hook — or an unmistakable fragment of it — inside the first ten to fifteen seconds, which is the lyric version of `open.first_second_hook`. In a theatre or album context you can afford to delay it. The craft rule: the hook must be sayable in one breath and must contain a concrete word, not only abstractions.
**Best in:** formats: single, reels/shorts, title sequence, jingle, worship song | genres: pop, hip-hop, dance, country, worship
**Avoid when:** The song's whole effect is a slow reveal — a lament, a narrative ballad — where meeting the hook cold in bar one spends the ending early. Note the honest limit: front-loading is a distribution tactic, not a craft law, and it has produced a generation of songs with no first verse worth hearing.
**Example:**
> Cold open, hook before any verse:
> Don't wait up. Don't wait up. I'm not the one who's coming home.
> (verse 1 then explains who is)

**Yields to:** `lyric.lament` — Slow-reveal grief song; a bar-one hook spends the ending.  
`lyric.hook_placement`

---

### Writing a Chorus That Survives Repetition

**Also called:** repetition-proofing, the durable chorus, wear-test
**What it is:** Building chorus lines out of language that gains rather than loses on the fourth hearing — concrete nouns, a small unresolved ambiguity, and no line whose whole value is surprise.
**Effect on the audience:** The chorus deepens across the song instead of flattening. By the last chorus the listener is supplying the meaning themselves.
**Used for and where it works best:** Any chorus that will be heard three or more times in one play, which is nearly all of them. The craft rule: cut every joke and every clever inversion from the chorus — wit is single-use, and a chorus is multi-use. Keep the wit in verse 2. Test by singing it four times in a row out loud; the line that starts to embarrass you on pass three is the line to replace. `emo.specific_detail` is the reliable substitute: a coat, a bus number, a name survives repetition where "my broken heart" does not.
**Best in:** formats: single, worship song, kids song, anthem, musical theatre | genres: pop, worship, country, rock, folk
**Avoid when:** A section is designed to be heard once — a bridge, a final tag. There you should spend the clever line. The failure mode of over-applying this rule is a chorus so plain it has nothing to survive.
**Example:**
> Fails the wear test: You're the punchline of a joke I never got.
> Survives it: You're the light I leave on for nobody.
> (second line means slightly more, not less, the fourth time)

**Yields to:** `lyric.bridge_turn` — Section heard once; spend the clever line there.  
`lyric.repeatable_chorus`

---

### Mutating Refrain

**Also called:** incremental repetition, the changing refrain, refrain variation, the moving tag
**What it is:** A repeated line whose words shift by one deliberate element each return — a number, a tense, a pronoun, a single noun — so the repetition itself carries the plot.
**Effect on the audience:** The listener recognises the line and hears the change at the same moment, which lands harder than any new line could, because they measure the distance themselves.
**Used for and where it works best:** The strongest device in narrative and folk songwriting, and the cheapest way to make a three-verse song feel like it moved. The craft rule: change exactly one thing per return, and make it the smallest thing that alters everything — usually a tense or a pronoun, not an adjective. This is `dial.repetition_variation` applied to sung lines, and the final mutation is often a `end.callback` to the opening image.
**Best in:** formats: ballad, folk song, kids song, musical theatre, heritage song | genres: folk, country, musical theatre, children's music, indie
**Avoid when:** The audience needs to sing along — a congregation or a crowd cannot follow a refrain that changes, and neither can a child singing a kids' song back, where `end.last_chorus` keeps the sung words fixed; a kids' song the child listens to rather than sings keeps this device. And avoid mutating more than three times; past that the listener stops tracking and hears random variation.
**Example:**
> V1: There are four of us walking the road to the river.
> V2: There are three of us walking the road to the river.
> V3: There is one of us walking. There is still a river.

**Yields to:** `lyric.congregational_lyric` — A room must sing it back together.  
`lyric.refrain_mutation`

---

## Prosody and Singability

### Stress-to-Downbeat Alignment

**Also called:** prosody, scansion, syllable stress matching, word stress on strong beats
**What it is:** Placing the stressed syllable of each important word on a strong beat, a long note, or a melodic peak, so the melody pronounces the word the way a speaker would.
**Effect on the audience:** When it is right the listener hears meaning with no effort. When it is wrong they hear a foreign accent, a mispronunciation, or nothing at all — and they blame the singer.
**Used for and where it works best:** Every sung line, in every language, always. The craft rule: speak the line in your natural voice, mark the stresses, then check the melody puts length or height on those same syllables. Longer notes belong on stressed syllables; the word that matters most in a line should sit at the melodic high point. Multi-syllable words are where it breaks first — a three-syllable name landing wrong ruins a whole chorus.
**Best in:** formats: song lyric, kids song, musical theatre, opera | genres: all
**Avoid when:** Never avoided, but it can be deliberately violated for one word to signal strain, drunkenness, a child singing, or a character whose control is slipping — and it only reads as intentional if the rest of the song is clean.
**Example:**
> Wrong: "for-GOT-ten" with the long note on "for" — sings as FOR-gotten, and the line dies.
> Right: shift the phrase so the long note lands on GOT: "and I / for-GOT-ten how to / ask"
> Cleaner still: rewrite to a word whose stress fits — "and I forgot the way to ask."

`lyric.stress_alignment`

---

### Vowel and Consonant Casting

**Also called:** phonetic casting, singability, open vowels on high notes, consonant clearance
**What it is:** Choosing words by sound as well as sense — open vowels (ah, oh, ay) on high or sustained notes, and no consonant clusters on fast runs or at the top of the range.
**Effect on the audience:** Open vowels at the peak read as release and power; closed vowels (ee, ih) at the top read as pinched or strained. Clustered consonants at speed read as mumbling.
**Used for and where it works best:** Apply it at exactly two places — the highest note and the longest note of each section — and leave the rest alone. The craft rule: the last word of a chorus, if held, must end on an open vowel or an easy nasal; a held "-tsk", "-cts" or "-sks" is unsingable and every singer will silently change it. Match the phonetic palette to the mood too: soft consonants and long vowels for a ballad, hard stops and short vowels for something angry.
**Best in:** formats: song lyric, musical theatre, opera, kids song | genres: pop, opera, musical theatre, worship, children's music
**Avoid when:** Naturalism is the point — a conversational indie or rap vocal that is carefully vowel-optimised sounds written rather than said. Real limit: chasing open vowels is how writers end up with a chorus of "oh" and "away" that means nothing.
**Example:**
> Unsingable at the top: "and it's the facts that stopped us"
> Singable at the top: "and it's the truth that broke us"
> Held note: "...so let me go-o-o" (open) beats "...so let me shift" (closed and clipped)

`lyric.vowel_casting`

---

### Line Length and Breath

**Also called:** breath planning, phrase length, air management
**What it is:** Writing each line so it can be sung in one breath at tempo, with a place to take the next one, and varying line lengths to control how urgent a section feels.
**Effect on the audience:** Short lines with gaps feel calm or clipped; long lines with no breathing room feel panicked or breathless — an effect you can use on purpose. A line that genuinely cannot be breathed just sounds like bad singing.
**Used for and where it works best:** Use it as a tension dial: shorten lines through the pre-chorus to accelerate, lengthen them in verse 3 to make the narrator sound like they are unravelling. The craft rule: sing the section aloud at final tempo, standing, and mark where you actually breathe — then check the breath falls at a comma, not inside a phrase. If you have to breathe mid-word, the line is wrong regardless of how it reads on the page.
**Best in:** formats: live event, musical theatre, song lyric, kids songs | genres: musical theatre, folk, rock, worship
**Avoid when:** The vocal will be comped and punched in the studio and never performed live — then you can write past the breath deliberately. But note the cost: the song becomes unperformable, and unperformable songs do not get covered.
**Example:**
> Breathless by design (verse 3, narrator losing control):
> and I called the house and I called the phone and I called the man who sold the car and nobody —
> Then one short line, with air: I stopped.

`lyric.breath_line_length`

---

### Writing for a Specific Voice

**Also called:** casting the lyric, range-writing, tailoring, writing to the instrument
**What it is:** Building the lyric around one singer's actual range, diction, accent and vocabulary — where their voice breaks, which vowels they carry best, which words they would never say.
**Effect on the audience:** The song sounds inevitable rather than assigned. Listeners cannot name why, but they hear that these words belong to this person.
**Used for and where it works best:** Any song written for a named artist, a musical theatre character, a child performer, or a specific dub voice. The craft rule: find the top three notes of their comfortable range and put only open, easy words there; find their break and either avoid it or put the most emotional word exactly on it. Also do a vocabulary pass — remove any word the singer would not use in speech, because listeners detect borrowed vocabulary instantly.
**Best in:** formats: single, musical theatre, dubbing, live event | genres: musical theatre, pop, country, worship, opera
**Avoid when:** The song is meant for anyone — a worship song, an anthem, a kids song sung by classrooms. Tailoring it to one voice guarantees it sits wrong for everyone else. The failure mode is a congregation song pitched for a soloist, which the room simply stops singing.
**Example:**
> For a singer with a strong break at the top of the chest voice, put the line's confession right on it:
> I was — (break) — fine.
> The crack is not a flaw in the take. It is the lyric.

**Yields to:** `lyric.congregational_lyric` — Song is meant for anyone, not one singer.  
`lyric.written_for_the_voice`

---

## Rhyme

### Perfect Rhyme

**Also called:** true rhyme, full rhyme, exact rhyme
**What it is:** The stressed vowel and everything after it match exactly — *stay / away*, *hollow / follow*. The most complete closure a line ending can have.
**Effect on the audience:** Lands like a door shutting. Signals control, finish, wit and often formality; in comedy it is the sound of a punchline arriving on time.
**Used for and where it works best:** Musical theatre, comedy, children's songs and any lyric where the writer's competence is part of the pleasure — a sloppy rhyme in a theatre lyric reads as a mistake, not a choice. The craft rule: reserve perfect rhyme for the line you want the listener to believe is final, and use weaker rhyme everywhere else so that closure means something when it arrives.
**Best in:** formats: musical theatre, kids song, jingle, patter song | genres: musical theatre, traditional pop, comedy, children's music
**Avoid when:** The song is about something unresolved. Perfect rhyme on a line about grief closes a feeling that should stay open — and the listener hears the tidiness as insincerity. It is also the shortest road to cliché: *fire/desire*, *heart/apart*, *rain/pain* are all perfect rhymes and all dead.
**Example:**
> I packed the kettle and I packed the plates,
> I packed the letters that arrived too late.
> (full closure — right for a character who is decided)

**Yields to:** `lyric.slant_rhyme` — Subject is unresolved; closure reads as insincerity.  
`lyric.perfect_rhyme`

---

### Slant Rhyme

**Also called:** near rhyme, imperfect rhyme, family rhyme, half rhyme, assonance and consonance
**What it is:** Endings that share some but not all of their sound — matching vowel with different consonant (*home / alone*), or matching consonant with different vowel (*dark / work*). Not a failed perfect rhyme; a different setting on the same dial.
**Effect on the audience:** Leaves the line ajar. The ear registers a rhyme and simultaneously registers that it did not resolve, which keeps the section moving forward and reads as honest rather than composed.
**Used for and where it works best:** Almost every contemporary lyric about a real feeling. The craft rule: think of rhyme as a scale of resolution — perfect at the top, then vowel-matched, then consonant-matched, then bare assonance — and choose the rung that matches how settled the character is at that moment. Loosen the rhyme as the character loses certainty; tighten it when they decide. It also frees you to say what you actually mean, which is the real argument for it.
**Best in:** formats: single, ballad, folk song | genres: indie, folk, hip-hop, country
**Avoid when:** Writing comedy or a patter lyric, where the audience is waiting for the exact hit and a near miss kills the laugh. Also avoid in a lyric to be translated or sung by children, where the loose ending gives no landing.
**Example:**
> I told them I was fine and I was home,
> I told them there was nothing left to hold.
> (home / hold — close enough to rhyme, open enough to be true)

**Yields to:** `lyric.perfect_rhyme` — Comedy, patter, translation, children; the ear needs a landing.  
`lyric.slant_rhyme`

---

### Internal Rhyme

**Also called:** mid-line rhyme, interior rhyme, leonine rhyme
**What it is:** Rhyme placed inside a line rather than only at its end — within one line, or between the middle of one line and the end of another.
**Effect on the audience:** Speeds the line up and glues it together. The ear feels density and momentum without hearing a stop, which is why it reads as skill rather than pattern.
**Used for and where it works best:** Long lines that would otherwise sag, and any section that needs to accelerate — pre-choruses, rap verses, patter sections. The craft rule: an internal rhyme should fall on a weak beat, not a strong one, or it competes with the end rhyme and the line stutters. Use it to disguise a weak end rhyme: a strong internal chime buys forgiveness for a loose ending.
**Best in:** formats: song lyric, patter song | genres: hip-hop, musical theatre, folk
**Avoid when:** The line is meant to be plain and heavy. Internal rhyme makes everything sound deft, and deftness is wrong for a lyric about a hospital corridor. Overused, it becomes the sound of a writer enjoying themselves in a song about someone else's pain.
**Example:**
> I counted every lamp and every lamp was burning late,
> and the gate was open wide enough to let the whole street wait.

**Yields to:** `lyric.breath_line_length` — Line must stay plain; accelerate by shortening instead.  
`lyric.internal_rhyme`

---

### Rhyme Scheme and the Deliberate Break

**Also called:** scheme choice, breaking the pattern, the unrhymed line, pattern violation
**What it is:** Choosing a scheme (AABB, ABAB, AAAA, ABCB) for its behaviour, then deliberately failing to complete it at one chosen moment.
**Effect on the audience:** Schemes train the ear within two lines. AABB feels closed and childlike; ABAB feels conversational and suspends the listener; ABCB gives one landing per stanza and lets the unrhymed lines carry plot. Breaking a trained pattern makes the ear jump — the listener notices without knowing why.
**Used for and where it works best:** Match the scheme to the job: ABCB for narrative verses, AABB for kids and comedy, ABAB for pop verses that must feel like speech. The craft rule for the break: you get one per song, and it must land on the line that means the most. Withhold the expected rhyme entirely rather than substituting a weak one — silence where a rhyme should be is louder than any word. This pairs naturally with `emo.understate_at_peak`.
**Best in:** formats: ballad, single, musical theatre | genres: folk, country, pop, musical theatre, indie
**Avoid when:** The audience must sing along or memorise — a broken pattern in a kids song or a congregational song just makes people fumble the line. And never break the scheme twice; the second break tells the listener there was never a pattern.
**Example:**
> He came back in the spring the way he said. (A)
> He put his boots beside the kitchen door. (B)
> He asked about the garden and the dog. (C — pattern expects B)
> Nobody had told him about the dog. (B, late — and the missing C is the point)

**Yields to:** `lyric.kids_repetition_contract` — Children must sing along; rhyme perfectly, never break.  
`lyric.rhyme_scheme_break`

---

## Song Types and Their Jobs

### The Narrative Song

**Also called:** story song, ballad, the murder ballad, event song
**What it is:** A song whose verses carry a sequence of events with a protagonist, a change and an outcome, usually anchored by a refrain the story keeps returning to.
**Effect on the audience:** The listener stops evaluating the song and starts following what happens. Attention behaves like it does in fiction — they want to know the end.
**Used for and where it works best:** When you have one concrete incident and the feeling is a consequence of it rather than a subject in itself. The craft rule: one verse, one event, and never more than three events total; a song has room for about sixty seconds of plot. Name one object and bring it back — the coat, the coin, the bus ticket — because `emo.specific_detail` is what makes a sung story believable where summary never will. The ending belongs in the last verse, not the last chorus.
**Best in:** formats: folk song, heritage song, musical theatre | genres: folk, country, hip-hop
**Avoid when:** The song is for dancing, a crowd, or a short-form clip. Narrative needs sequence, and a clip has no sequence. Real failure mode: the writer compresses too much plot and produces a synopsis with a melody, where nothing is felt because everything is reported.
**Example:**
> V1: He sold the boat in March and told nobody.
> V2: In June the harbour master asked about the boat.
> V3: He said it sank. It did — but not in March, and not alone.

**Yields to:** `lyric.anthem` — Written for a crowd; a clip has no sequence.  
`lyric.narrative_song`

---

### The List Song

**Also called:** catalogue song, laundry list, the enumeration number
**What it is:** A song whose verses are an accumulating list — things, people, reasons, places — held inside a repeated frame, with escalation from item to item.
**Effect on the audience:** Comic momentum, or in a serious register, a rising sense of scale. The listener starts predicting the next item, which is exactly the pleasure — and exactly what the last item should defeat.
**Used for and where it works best:** Comedy, children's songs, love songs of exaggeration, and protest songs of accumulation. The craft rule: order the list by size, never randomly, and make the final item break the category — twelve concrete nouns then one abstract, or eleven jokes then one true thing. The last item is the whole song; if it belongs on the list, there is no song.
**Best in:** formats: musical theatre, kids song, patter song, protest song | genres: musical theatre, comedy, children's music, folk
**Avoid when:** The subject requires interiority. A list is a surface form; it cannot show a person changing, only a person cataloguing. Failure mode: a list with no escalation, which is a verse that could be shuffled in any order — always a sign the writer had no argument.
**Example:**
> I'll carry the ladder, the lamp and the letters,
> the dog and the dog's ridiculous bed,
> the table your father made badly in springtime,
> and every single thing I never said.

**Yields to:** `lyric.character_song` — Subject needs interiority; a list cannot show change.  
`lyric.list_song`

---

### The "I Want" Song

**Also called:** the I Wish song, the want number, the opening number of desire
**What it is:** An early song in which the protagonist states what is missing from their life, in their own words, in a way that sets the whole story's engine running.
**Effect on the audience:** Creates allegiance. Once an audience knows what someone wants, they start wanting it too, and will follow that character for two hours to find out if they get it.
**Used for and where it works best:** Placed in the first ten to fifteen minutes of a musical, or as the opening song of any story-driven video or animated piece. The craft rule: the want must be concrete and visible — not "to be happy" but "to get off this island", "to hear my name said properly once". Name the obstacle inside the song, and let the character be wrong about what they actually need; that gap is what the ending fixes. See `emo.earn_the_situation` — a want stated before we believe the life it comes from lands as declaration, not desire.
**Best in:** formats: musical theatre, animated feature, kids series | genres: musical theatre, children's music
**Avoid when:** The character's want is the mystery of the piece, or the protagonist is meant to be unreadable. Also avoid in ensemble stories with no single lead. The failure mode is the generic want song — "I know there's something more out there" — which is a placeholder every writer writes once and should then delete.
**Example:**
> They gave my grandmother's name to me and then
> they cut it short so strangers wouldn't stumble.
> I want it back. All four of its syllables.
> I want someone to have to slow down saying it.

**Yields to:** `lyric.character_song` — The want must stay a mystery.  
`lyric.i_want_song`

---

### The Character Song

**Also called:** book song, dramatic lyric, in-character writing, the show song
**What it is:** A lyric written in the voice of a specific person inside a story — their vocabulary, their evasions, their level of self-knowledge — rather than in the writer's own voice.
**Effect on the audience:** The audience hears a person, not an author. They also hear what the character will not say, which is where most of the drama lives.
**Used for and where it works best:** Any musical, animated film, concept album or heritage piece with named characters. The craft rule: give each character a vocabulary limit and keep to it — a dockworker does not reach for "ephemeral", and breaking the limit is the single most common way a show song collapses. Second rule: the song must end the character somewhere different from where it found them, or it is a monologue with chords. That movement is `scene.value_turn`.
**Best in:** formats: musical theatre, animation feature, song lyric, radio drama, kids series | genres: musical theatre, opera, children's music
**Avoid when:** You are writing an artist's own single. Audiences come to a pop record for the singer's actual voice, and an in-character lyric there often reads as inauthentic unless the frame is unmistakable.
**Example:**
> (The father, who never says the word "sorry", at the end of Act I)
> I kept the receipts. I kept every one.
> I can prove what I paid for and when.
> Ask me the cost of the roof, of the coat, of the doctor —
> Don't ask me the other question again.

**Yields to:** `lyric.written_for_the_voice` — An artist's own single, not a story voice.  
`lyric.character_song`

---

### The Kids' Song Repetition Contract

**Also called:** child-directed song rules, sing-along design, predictability contract
**What it is:** A set of hard constraints for songs aimed at young children: heavy repetition, a small vocabulary, predictable rhyme, a fixed frame per verse, and one element that changes so the child can guess it.
**Effect on the audience:** A child who can predict the next line joins in by the second listen. Prediction plus a small surprise is the entire pleasure mechanism, and it is also how the song teaches.
**Used for and where it works best:** Any song for under-sevens, including educational, alphabet and counting songs. The craft rules that actually matter: keep one idea per verse; keep the frame identical and change exactly one slot — in the verse frame, never in the last pass of the chorus the child sings back, which `end.last_chorus` keeps unchanged; leave a gap for the child to fill (call and response); rhyme perfectly, because a slant rhyme gives a child nothing to land on — except where the perfect rhyme would cost the chorus its concrete noun (`lyric.repeatable_chorus`), which is common in Arabic: then the concrete word wins and the near rhyme stays; and put a physical action in the lyric — clap, jump, point — so the body has a part. A counting or alphabet structure gives the sequence for free.
**Best in:** formats: kids music video, kids song, educational | genres: children's music, kids, educational, faith
**Avoid when:** The audience is 8+, where the same repetition reads as babyish and they disengage fast. Adults judge these songs by adult criteria and call them simple; that judgement is wrong, but do not let it push you into complexity the child cannot hold.
**Example:**
> One little bird in the old tall tree — (clap, clap!)
> Where did she go? Can you see? Can you see?
> Two little birds in the old tall tree — (clap, clap!)
> Where did they go? Can you see? Can you see?

**Yields to:** `lyric.lullaby` — Bedtime; prediction-plus-surprise wakes the child.  
`lyric.kids_repetition_contract`

---

### The Anthem

**Also called:** the we-song, stadium lyric, the communal chorus, crowd song
**What it is:** A lyric written in the first person plural, or in a second person that a crowd can adopt, built so a large group of strangers can sing it together on a first hearing.
**Effect on the audience:** Converts an audience into a body. The listener stops being addressed and starts being included, which is a different and much stronger feeling than sympathy.
**Used for and where it works best:** Sport, national and cultural pieces, worship, protest, and any song intended to end a live set. The craft rules: short chorus lines, no more than six or seven syllables; open vowels held long; no proper nouns a crowd might not share; and a rhythm simple enough to be shouted slightly behind the beat, because crowds always lag. The verses may be personal — the chorus may not.
**Best in:** formats: anthem, heritage song, worship song, protest song, feature film | genres: rock, worship, folk, pop, traditional
**Avoid when:** The subject is private grief or ambivalence. An anthem asserts; it cannot doubt. Real failure mode: a chorus of "we" that names nothing anyone shares, producing the empty motivational song that plays over every montage and moves nobody.
**Example:**
> We were never asked, and we came.
> We were never named, and we stayed.
> Sing it loud enough to shake the water —
> we were here, we were here, we were here.

**Yields to:** `lyric.lament` — Private grief or ambivalence; an anthem cannot doubt.  
`lyric.anthem`

---

### The Lament

**Also called:** the grief song, dirge, elegy, keening song, the mourning lyric
**What it is:** A song of loss that does not argue, resolve or console — it states, repeats, and lets the repetition carry what statement cannot.
**Effect on the audience:** Permission. The listener is not being persuaded to feel something; they are being kept company in something they already feel.
**Used for and where it works best:** Funerals, heritage and memorial pieces, film scenes of loss, and the third act of almost anything. The craft rules: no explanation of the feeling, only the circumstances of it — `emo.understate_at_peak` is not optional here; a lament that reaches for big language becomes a performance of grief. Second rule: let the form stay simple and let the repetition do the work; grief is repetitive and the lyric should be. Name one ordinary object. Do not end on comfort unless the song earned it.
**Best in:** formats: song lyric, heritage song, feature film | genres: folk, traditional, gospel, country
**Avoid when:** The piece must give hope by its end — a memorial designed to send an audience out standing needs a turn the lament will not provide. Also avoid when the loss is not yours to sing; a lament written from outside reads as tourism and audiences detect it instantly.
**Example:**
> The kettle still boils for two.
> I have not changed the setting.
> I do not intend to change the setting.
> The kettle still boils for two.

**Yields to:** `lyric.anthem` — Memorial must send the room out standing.  
`lyric.lament`

---

## Language, Version and Screen

### Writing in a Second Language

**Also called:** non-native lyric writing, L2 lyric, cross-language songwriting
**What it is:** Writing a lyric in a language you do not think in, which changes what you can hear — idiom, register, stress placement and connotation all sit outside your instinct.
**Effect on the audience:** Native listeners hear register errors long before they hear meaning. A single wrong-register word — too formal, too archaic, too street — resets their read of the whole song.
**Used for and where it works best:** Worth doing when the audience is in that language, or when the language carries the subject (a heritage song, a diaspora piece). The craft rules: write plainer than you would in your first language, because simple lines are hard to get wrong; check every idiom against a native speaker rather than a dictionary; and verify stress placement out loud, since word stress is the first thing non-native writers get wrong and the thing that makes a line unsingable. Never rhyme on a word you have only read.
**Best in:** formats: heritage song, single, dubbed song, worship translation | genres: pop, worship, folk, children's music, diaspora
**Avoid when:** The song depends on wordplay, slang or comedy. Humour is the last thing a second language gives you, and a joke that misses in a lyric is unrecoverable. Be honest about the limit: fluency in speech does not mean fluency in sung register.
**Example:**
> Too literary for a pop chorus (a common L2 slip):
> I shall not forsake the promise that we rendered.
> Right register, same meaning:
> I'm not going back on what we said.

`lyric.second_language_lyric`

---

### Singable Translation

**Also called:** the Pentathlon approach, re-versioning, localised lyric, dubbing a song
**What it is:** Rebuilding a lyric in another language so it can actually be sung to the same melody — balancing five demands at once: singability, sense, naturalness, rhythm and rhyme, and trading between them consciously.
**Effect on the audience:** Done well, listeners in the target language never think about translation. Done literally, they hear a stilted cover of something that presumably worked elsewhere.
**Used for and where it works best:** Dubbing animated songs, releasing an international version, and localising worship or children's material. The craft rules: singability and natural word order win every trade — meaning must bend first. Rhymes need not fall in the same places or the same density as the original; move them where the target language offers them. Keep the title phrase's syllable count and stress shape even if you must change its literal meaning, because that is the shape the melody was built on. Translate the function of an idiom, never the idiom.
**Best in:** formats: dubbing, kids song, worship translation | genres: children's music, musical theatre, worship, pop
**Avoid when:** The original's power is specific wordplay or a culturally locked reference. Then re-write rather than translate and say so. The failure mode is the accurate translation that no singer can phrase — every syllable correct, every line unsingable.
**Example:**
> Literal (unsingable — stress lands wrong, too many syllables):
> The morning has arrived and it is beautiful today
> Re-versioned (same melody, same function, new words):
> The sun is up. The day is ours.

**Yields to:** `lyric.second_language_lyric` — Original is wordplay or culturally locked; re-write instead.  
`lyric.singable_translation`

---

### Writing to an Existing Melody

**Also called:** topline writing, dummy lyric method, vowel mapping, the nonsense-lyric pass
**What it is:** The melody exists first, so you sing gibberish or placeholder words over it, capture the exact rhythm, stress and vowel shapes it wants, then find real words that fit that shape.
**Effect on the audience:** Nothing — they never hear the process. What they hear is a lyric that sits on the melody as if it were born there, which is the point.
**Used for and where it works best:** Any track-first collaboration, any song built on a beat, and any time a melody arrived before the idea. The craft rules: transcribe the dummy lyric's stresses and vowels before you throw it away, and treat that map as a constraint, not a suggestion. Keep the dummy's vowels at the peaks — the melody chose them for a reason. And read the dummy lyric before deleting it; the accidental phrase you sang without thinking is often the title.
**Best in:** formats: song lyric, feature film, dubbed song | genres: pop, dance, hip-hop
**Avoid when:** The lyric content is the commission — a heritage piece, a memorial, a story song with facts to deliver. The melody will fight the information, and you will end up cutting the facts. Lyrics-first is the correct order whenever the words have a job.
**Example:**
> Dummy pass: "naa-na hollow, saa-na follow" — logs two open-o peaks and a trochaic fall.
> Final: "Wait in the doorway, stay in the shadow."
> (same stress, same peak vowels, actual meaning)

**Yields to:** `lyric.writing_to_brief` — The content is the commission; lyrics come first.  
`lyric.dummy_lyric_topline`

---

### On-Screen Lyric Text

**Also called:** lyric video design, kinetic typography, karaoke text, burned lyric
**What it is:** Putting the words on screen in time with the vocal, where the lyric is now read as well as heard and every line break becomes a visual decision.
**Effect on the audience:** Reading reinforces the hook and rescues unclear diction, but it also exposes weak lines — a filler line the ear forgives, the eye will not.
**Used for and where it works best:** Lyric videos, kids songs where children are learning the words, second-language releases, and any release to muted-autoplay feeds. The craft rules: break lines where the singer breathes, never where the page would break them; hold the hook line longer than its sung duration; animate selectively — motion on every line means emphasis on none, so save the movement for the hook and the turn; and check it on a phone, because most viewing is on a phone and weak contrast and cramped breaks only show up there.
**Best in:** formats: lyric video, kids music video, reels/shorts | genres: pop, children's music, worship, hip-hop, heritage
**Avoid when:** The lyric relies on a mishearing, a slow reveal, or a phrase that means two things until the last line — text kills all three, because the eye gets there before the ear. `info.delayed_decoding` and on-screen text are direct enemies.
**Example:**
> Sung as one breath: "I left the light on for a man who isn't coming"
> Wrong break (reads like a list): I left the light on / for a man / who isn't coming
> Right break (matches the breath and holds the turn): I left the light on for a man — / who isn't coming

`lyric.on_screen_lyric_text`

---

## Named Failure Modes

### The Filler Line

**Also called:** the syllable-count line, padding, the "just" line
**This is a named failure, not a recommendation.**
**What it is:** A line present only to fill a melodic slot or reach a rhyme — usually detectable by a meaningless intensifier ("just", "really", "oh so") doing the work of a real word.
**Effect on the audience:** A small drop in attention that the listener does not consciously register but absorbs as boredom. Four filler lines in a song and the song is background.
**Used for and where it works best:** — Its only legitimate use is as a placeholder during drafting, marked and replaced before anyone hears it.
**Best in:** formats: — | genres: —
**Avoid when:** Always. The fix: delete the line and see whether the song misses it. If the melody needs those syllables, say a new thing there rather than restating the previous line with "just" in front of it. Every filler line is a free slot you already paid for.
**Example:**
> Filler: I just really want to say I'm here for you tonight
> Fix (same syllable count, actual content): I moved the chair so you could see the street

`lyric.filler_line`

---

### The Forced Rhyme

**Also called:** rhyme-driven writing, the tail wagging the song, rhyme-first syntax
**This is a named failure, not a recommendation.**
**What it is:** A word chosen because it rhymed rather than because it meant what the writer needed — often visible in inverted word order ("the night that came so cold") bent to land the sound.
**Effect on the audience:** The listener feels the compromise even when they cannot name it. They hear the pattern being served instead of the story, and they stop trusting the narrator.
**Used for and where it works best:** — Only in comedy, where an absurdly forced rhyme is the joke and the audience is invited to see the strain.
**Best in:** formats: — | genres: —
**Avoid when:** Always, outside comedy. Two fixes, in order: loosen to a slant rhyme and keep the true word; or rewrite the *earlier* line so the rhyme you need becomes reachable. Most writers only ever try to fix the second line, which is why the problem persists — the fault is usually upstream.
**Example:**
> Forced: I watched you from the balcony above / my hands were full of everything but love
> Fixed by loosening the rhyme: I watched you from the balcony above / my hands were full of nothing I could hold

**Yields to:** `lyric.slant_rhyme` — Loosen the rhyme and keep the true word.  
`lyric.forced_rhyme`

---

### The Page Lyric

**Also called:** reads well sings badly, the poem problem, the unsingable lyric
**This is a named failure, not a recommendation.**
**What it is:** A lyric whose quality is entirely visual — dense clauses, subordinate structure, precise multi-syllable vocabulary — that collapses the moment it is sung at tempo by one voice with lungs.
**Effect on the audience:** They hear approximately nothing. Sung language is received once, in order, at the performer's speed; anything requiring re-reading is lost, and the listener blames themselves before blaming the song.
**Used for and where it works best:** — Nowhere as a finished lyric. As a drafting stage it is useful: write the prose truth first, then convert.
**Best in:** formats: — | genres: —
**Avoid when:** Always. The test is mandatory and simple: sing the lyric aloud, at final tempo, standing, from memory. Every line you stumble on is broken — not your performance, the line. Convert by cutting subordinate clauses into separate lines, replacing polysyllables with one-syllable words at the peaks, and putting the most important word at the end of the phrase rather than buried inside it.
**Example:**
> Page lyric: Although I had intended to remain until the morning, circumstances I could hardly have predicted intervened.
> Sung version: I meant to stay till morning. / Something got there first.

**Yields to:** `lyric.breath_line_length` — Line cannot be sung at tempo in one breath.  
`lyric.page_lyric`

---

### The Chorus That Says Nothing

**Also called:** the empty chorus, the placeholder hook, the montage chorus
**This is a named failure, not a recommendation.**
**What it is:** A chorus built entirely from abstractions and borrowed uplift — fire, higher, tonight, forever, alive — that could be transplanted into a hundred other songs without changing either one.
**Effect on the audience:** Momentary energy, zero retention. The listener enjoys it while it plays and cannot recall a word an hour later, because there was nothing specific to attach a memory to.
**Used for and where it works best:** — It has one real commercial use: a sync-friendly bed designed to carry any brand's message. Even there it is a product, not a song.
**Best in:** formats: — | genres: —
**Avoid when:** Any time the song is meant to be someone's. Diagnostic: cover the verses and read the chorus alone — if you cannot say who is singing, to whom, and about what one thing, it is empty. Fix by importing one concrete noun from the verse into the chorus. A single real object (`emo.specific_detail`) turns a generic chorus into a particular one without touching the melody.
**Example:**
> Empty: We're burning brighter, we're alive tonight, we'll never let it go
> Fixed with one object from verse 2: We're burning your father's letters, we're alive tonight, and we are never going home

**Yields to:** `emo.specific_detail` — Import one concrete object from the verse.  
`lyric.empty_chorus`

---

## Coverage

---

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Researched 17 September 2026.

- [Prosody in Music and Songwriting — Berklee Online](https://online.berklee.edu/takenote/prosody-in-music-and-songwriting/)
- [Prosody in Songwriting 101 — The Song Foundry](https://thesongfoundry.com/prosody-songwriting-101/)
- [Fitting Lyrics to a Melody: Why Words Don't Sing — Song Cage](https://songcage.com/blog/fitting-lyrics-to-a-melody/)
- [Understanding the Role of Phonetics in Songwriting — Speed Songwriting](https://speedsongwriting.com/phonetics-in-songwriting/)
- [Songwriting 101: Learn Common Song Structures — MasterClass](https://www.masterclass.com/articles/songwriting-101-learn-common-song-structures)
- [Song Structure: 6 Common Forms and When to Use Each — Orphiq](https://orphiq.com/resources/song-structure-guide)
- [Parts of a Song: 8 Common Sections and What Each Does — Orphiq](https://orphiq.com/resources/parts-of-a-song-explained)
- [Song Structure Explained: Verse, Chorus, Bridge & Forms — Song Cage](https://songcage.com/blog/song-structure/)
- [Lyrically Speaking: A Q&A on Rhyme with Pat Pattison — American Songwriter](https://americansongwriter.com/q-and-a-on-rhyme-with-pat-pattison/)
- [Different Journeys with Rhyme Schemes — Pat Pattison](https://www.patpattison.com/copy-of-pov-verse-development)
- [Rhyme Schemes for Songwriters (With Real Data) — Song Cage](https://songcage.com/blog/rhyme-scheme/)
- [Rhyme Schemes for Songwriters — ASCAP / Jordan Reynolds](https://www.ascap.com/help/career-development/15-rhyme-schemes-jordan-reynolds)
- [Musical Theatre Lyric Writing Tips, Part 1 — YouthPLAYS](https://www.youthplays.com/blog_details.php?blog_id=87)
- [On Lyric Writing For Theater — The Playwrights Realm](https://www.playwrightsrealm.org/aspiring-playwrights-articles/lyric-writing-theater)
- [Discovering "I Want" Songs in Context — MusicalWriters.com](https://www.musicalwriters.com/writing-a-musical/i-want-songs-in-context/)
- [Five "I Want" Songs That Work — MusicalWriters.com](https://www.musicalwriters.com/writing-a-musical/five-i-want-songs-that-work/)
- [Songwriting for Ages 0–6 — Music for Kiddos](https://www.musicforkiddos.com/blog/podcast11)
- [Temporal patterns in the complexity of child-directed song lyrics — Communications Psychology](https://www.nature.com/articles/s44271-025-00219-4)
- [40 Call & Response Songs and Games for Elementary Music — Ashley Danyew](https://www.ashleydanyew.com/posts/2017/40-call-and-response-songs-and-games-for-childrens-choir)
- [Singable translations of songs (Peter Low) — ResearchGate](https://www.researchgate.net/publication/232950682_Singable_translations_of_songs)
- [Song Lyrics Translation: An Approach on Peter Low's Pentathlon Principle — ResearchGate](https://www.researchgate.net/publication/357752411_Song_Lyrics_Translation_An_Approach_on_Peter_Low's_Pentathlon_Principle)
- [Lyric Writing Tips: How to Use Dummy Lyrics in Your Song — iZotope](https://www.izotope.com/en/learn/lyric-writing-tips-how-to-use-dummy-lyrics-in-your-song)
- [Lyrics or Music: Which Comes First? — eMastered](https://emastered.com/blog/lyrics-or-music-first)
- [Avoid These Dangerous Lyrical Clichés — The Essential Secrets of Songwriting](https://www.secretsofsongwriting.com/2022/08/09/avoid-these-dangerous-lyrical-cliches/)
- [3 Avoidable Lyric Mistakes — EpicSongWriting](https://epicsongwriting.com/3-avoidable-lyric-mistakes/)
- [The Role of Typography in High-Quality Lyric Videos — Lyrics Video 4 U](https://lyricsvideo4u.com/blog/the-role-of-typography-in-high-quality-lyric-videos/)
- [From boring text to karaoke gold: visual tricks for lyric videos — TensorPix](https://tensorpix.ai/blog/visual-tricks-lyric-videos)
- [A songwriter's guide to understanding song form — Jeffrey Pepper Rodgers](https://www.jeffreypepperrodgers.com/blog/songwriting-lesson-understanding-song-form)
- [What Is a Ballad? Structure, Themes & Classic Examples — Literary Devices](https://literarydevices.net/what-is-a-ballad-structure-themes-classic-examples/)
- [Music 101: What Is a Ballad? — MasterClass](https://www.masterclass.com/articles/music-101-what-is-a-ballad-learn-to-write-a-ballad-with-examples)
