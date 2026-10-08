# Dialogue complaints

Part of the symptom router. Open this file when the complaint is about dialogue. Each complaint below is followed by the cards that repair it, best first; `LOOKUP.md` says which file holds each card.

---

### "The dialogue is on the nose"

Characters are saying exactly what they mean and feel. The fix is not to make them vaguer — it is to give them a reason not to say it.

1. Understand the failure before fixing it
   `dial.on_the_nose`
2. Give the character something they will not say, and a cost for saying it
   `dial.strategic_withholding`
3. Let them answer sideways
   `dial.deflection` · `dial.topic_change`
4. Move the whole conversation onto an unimportant subject
   `dial.trivial_surface`
5. Put a witness in the room so neither can speak plainly
   `scene.third_party_arrival` · `scene.public_scene`

### "The dialogue is just exposition"

Characters are telling each other things they both already know.

1. Apply the diagnostic: if a character could reply "I know", cut the line
   `dial.known_information`
2. Deliver the fact as ammunition inside an argument
   `dial.exposition_accusation`
3. Or as the correction of a wrong version — best for technical material
   `dial.exposition_correction`
4. Or let an expert explain it badly first and be asked again
   `dial.expert_explains_badly`
5. If everyone in the room already knows the material and is clever, make it a contest
   `dial.rapid_fire`
6. If the whole scene exists to deliver information, redistribute and delete it
   `scene.absorb_and_delete`

### "The argument doesn't escalate"

1. Change tactic each time the previous one fails
   `scene.tactic_change`
2. Track who is allowed to finish a sentence, and reverse it across the scene
   `dial.interruption` · `dial.question_control`
3. Try raising the register instead of the volume
   `dial.polite_aggression`
4. Let one of them end it by agreeing
   `dial.concession_that_wins`

### "There's no tension in the conversation"

1. The audience must know something one character does not
   `dial.half_truth` · `dial.strategic_withholding`
2. Let both sides pursue different conversations without noticing
   `dial.talking_past`
3. Break a social pair — a refused greeting, an unanswered question
   `dial.adjacency_break` · `dial.silence_as_reply`
4. With three or more in the room, aim a line at one person through another
   `dial.talking_to_the_room`

### "Every character sounds like me"

1. The named failure, and the hardest to see from inside a draft
   `dial.writer_voice_uniformity` · `voice.narrator_vs_character`
2. Give each one a different lexical field and a different thing they notice
   `voice.lexical_field` · `char.what_they_notice`
3. Cover the names in a printed scene and see whether you can still tell who is speaking
4. The build that survives a rewrite is a specification rather than a resolution, and it is a procedure done before drafting: six countable parameters per principal, one of them grammatical rather than lexical — the person who never uses the first person as a subject, the person who answers questions with questions
   `char.idiolect_sheet`
5. Then give each of them something they will not say. A prohibition held for a whole draft and broken once is the cheapest way to make a long piece feel designed — and it is enforced in the second draft with a search, not from memory, because it always leaks around page sixty
   `char.never_says`

### "The group scene reads as a queue"

1. Not everyone needs a line. The named failure is giving each person one in turn
   `dial.everyone_gets_a_line`
2. Let some speak at once and some not at all
   `dial.overlap` · `rel.pair_off_the_room`

### "The accent is doing the characterisation"

1. Spelling it out is the named failure — carry it in syntax and word choice instead
   `dial.phonetic_accent_spelling` · `voice.eye_dialect` · `voice.dialect_by_syntax`

### "The comedy scene loses the plot"

1. Dialogue that chases the laugh past the point the scene needed
   `dial.talking_past_the_laugh` · `comedy.joke_that_stops_story`

### "I need a specific kind of speech"

**Voice and idiolect:** signature vocabulary `dial.signature_vocabulary` · a verbal tic with a condition `dial.conditional_tic` · register shifting mid-scene `dial.register_shift` · the job showing in the syntax `dial.job_syntax` · professional argot, dosed `dial.argot_dose` · generational speech `dial.generational_speech` · second-language rhythm `dial.second_language_rhythm` · fluency dropping under stress `dial.fluency_under_stress` · code-switching mid-line `dial.code_switch_midline`

**Comedy of dialogue:** the literal answer `dial.literal_answer` · escalating agreement `dial.escalating_agreement` · the non-sequitur reply `dial.non_sequitur_reply` · the undercut `dial.undercut` · the deflating reply `dial.deflating_reply` · the comic triple in speech `dial.comic_triple`

**Monologue:** when a speech is earned `dial.earned_speech` · the interrupted monologue `dial.interrupted_monologue` · the confession speech `dial.confession_speech` · the toast `dial.the_toast` · the pitch `dial.the_pitch` · the eulogy `dial.the_eulogy` · the rant and its shape `dial.rant_shape`

**Groups:** three people `dial.three_hander` · the table `dial.table_scene` · who is silent `dial.who_is_silent` · someone spoken about who is present `dial.spoken_about_present`

**Mediated:** the intercut call `dial.intercut_call` · one side only `dial.one_sided_call` · the video call `dial.video_call` · the voice note `dial.voice_note` · lag as drama `dial.lag_as_drama`

**Across languages:** the untranslated line `dial.untranslated_line` · on-screen text `dial.text_on_screen` · subtitle constraints `dial.subtitle_constraint` · the interpreter scene `dial.interpreter_scene`

### "The dialogue sounds written"

1. Cut the front off the lines
   `dial.dropped_first_words`
2. Strip every name and put back only the two that matter
   `dial.name_weapon`
3. Let people speak at once where they know each other well
   `dial.overlap`
4. Replace speech tags with physical business
   `dial.action_beat`
5. For menace in a closed hierarchy, build the rhythm from repeating the other person's own words back at them
   `dial.clipped_line`

### "I need the piece to feel whole, not like a sequence"

1. Return a phrase from early in the work, altered by one word or by who says it
   `dial.repetition_variation`
2. Plant a line that is functional on first appearance and let it return at distance
   `dial.callback_line`
3. Play an early scene again, changing exactly one thing
   `scene.played_twice`

### "The plot turns on a misunderstanding and it feels contrived"

1. The error must cost less to accept than to question, in that moment, for that character
   `dial.misheard_line`
2. If the audience thinks "he would have just asked", the mishearing is not yet plausible — give the circumstances a reason: a bad line, a crowded room, a second language

---
