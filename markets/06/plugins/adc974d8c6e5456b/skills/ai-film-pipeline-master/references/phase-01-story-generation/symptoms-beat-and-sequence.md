# Beat and sequence complaints

Part of the symptom router. Open this file when the complaint is about beat and sequence. Each complaint below is followed by the cards that repair it, best first; `LOOKUP.md` says which file holds each card.

---

### "The scene has good lines and no movement"

1. Count the beats. If there are two, that is the problem
   `beat.beat_count` · `beat.scene_beat_budget`
2. Find where the beat changes and make sure it changes
   `beat.beat_change` · `beat.micro_turn`
3. Name each beat with a verb — what is this person *doing* to the other
   `beat.verb_naming` · `beat.tactic_beat`
4. Run a beat-marking pass on the whole draft
   `beat.beat_marking_pass` · `beat.action_reaction_exchange`
5. A scene beat sheet and a story beat sheet are different documents
   `beat.scene_sheet_vs_story_sheet`
6. Prose and screenplay carry beats differently, at different densities
   `beat.prose_vs_screenplay` · `beat.prose_beat_density`

### "The exchange feels mechanical"

1. Vary beat length; identical beats are a metronome
   `beat.length_variation` · `beat.repeated_beat`
2. Let some beats be physical or land on an object rather than on a line
   `beat.physical_beat` · `beat.object_beat` · `beat.silent_beat`
3. Hold one beat past comfort
   `beat.held_beat` · `beat.beat_after_line`
4. Cut the beats that do nothing
   `beat.dead_beat`
5. Echo a beat from earlier, changed — the beat-level version of a callback
   `beat.beat_rhyme` · `beat.comic_third`
6. End the scene on the right beat, and let one be cut off from outside
   `beat.exit_beat` · `beat.interrupted_beat`

### "The reactions feel thin"

1. The reaction beat is the one most often cut too early
   `beat.reaction_beat` · `beat.clipped_reaction`
2. Carry subtext across the beat rather than inside the line
   `beat.subtext_carry`
3. Stop writing `(beat)` and write the action that fills the pause
   `beat.notation` · `beat.beat_spam`

### "The action sequence is a list of moves"

1. Each action must create the conditions for the next
   `beat.action_sequence_beats` · `beat.choreography_list`
2. Escalate step by step rather than by volume
   `beat.escalation_step` · `beat.redirect`
3. At sequence scale, the same rule with a bigger unit
   `seq.action_sequence` · `seq.internal_escalation`
4. If it is a fight between people who know each other, write the row in plain words first and then convert each line into a physical beat, keeping the order. The tactic changes then fall where the argument would have turned, and one of the two must not want to be there
   `sub.fight_as_argument` · `scene.tactic_change`

### "The middle is a run of scenes going nowhere"

This is the sequence level — the one most writers skip and where most second acts fail.

1. Find the sequence boundaries and map them
   `seq.boundary_test` · `seq.sequence_map` · `seq.sequence_unit`
2. Every sequence needs its own question and its own climax
   `seq.sequence_question` · `seq.sequence_climax` · `seq.climaxless_run`
3. A sequence resolves *partially* — one that closes fully stops the film
   `seq.partial_resolution`
4. Join the scenes with a dangling cause rather than with chronology
   `seq.dangling_cause` · `seq.scene_welding` · `seq.spanning_tension`
5. If the run is a series of errands, that is the named failure
   `seq.errand_run`

### "The sequence is too long / too short"

1. Diagnose which
   `seq.inflated_sequence` · `seq.crushed_sequence`
2. Vary length across the act; identical sequences flatten an act
   `seq.length_variation` · `seq.act_rhythm`
3. Put a breather where the audience needs one
   `seq.breather_sequence`
4. In television the sequence climax and the act break are the same beat
   `seq.tv_act_sequence`

### "I need a specific kind of sequence"

`seq.set_piece` · `seq.investigation_sequence` · `seq.preparation_sequence` · `seq.journey_sequence` · `seq.montage_sequence` · `seq.crosscut_sequence` · `seq.convergence_sequence` · `seq.unifying_frame` · `seq.short_film_model` · `seq.sequence_spine` · `seq.sequence_handoff` · `seq.chapter_cluster` · `seq.shortform_serial`

**And by medium, where the form itself changes what a run can be:** a children's episode, usually one run of two or three scenes, limited by attention rather than page count `seq.kids_run` · an interactive run, where you control the order and the content but not the duration `seq.player_paced_run` · a factual run, built in the paper edit from real material in ascending order of surprise `seq.documentary_sequence`


### "There are three people in the room and only two of them are in the scene"

The moment most ensemble scenes go slack is the moment a two-hander opens up to three. The repair is geometry, not extra lines.

1. Bend the beat: aim the action at one person and take the reaction that matters from a different one
   `beat.triangulated_beat`
2. Then ration the reactions. An action carries one significant reaction before the scene stalls, and it belongs to whoever has most to lose from it — not whoever has most to say about it
   `beat.reactor_choice`
3. Above five or six at one table, track which *pair* is holding the beat and hand custody on before they exhaust it
   `beat.beat_custody`
4. If the group is genuinely one body — a court, a terrace, a classroom — write it as one movement with one verb, then cut to a single face
   `beat.crowd_reaction`

### "Everyone reacts to the news in turn and none of it lands"

1. That is `beat.round_robin`: the beat paid for five times, in seating order, landing none of them
2. The repair is the reaction economy — choose one carrier and give the rest of the room a single collective clause
   `beat.reactor_choice`
3. If the reaction went to the viewpoint character out of habit rather than to the person with the stake, that is a different named failure with the same look
   `beat.wrong_character_beat`

### "Two people are talking on the phone and it's dead on the page"

1. Start from what the form gives you: the reaction half cannot be seen by whoever caused it, and showing both ends, one end or neither makes three different beats
   `beat.phone_beat`
2. Then pick the scene shape that matches the one you chose
   `scene.phone_call_split` · `scene.one_sided_call`

### "The message thread has no tension"

1. The gap is the beat. A channel that puts real time between action and reaction — a text, a voice note, a message marked read and not answered — does the work a look would do in a room
   `beat.lag_beat`
2. At relationship scale that becomes its own structure, where every silence is readable as a message
   `rel.correspondence_bond`
3. And if the thread *is* the piece, the interface conventions are the prose
   `inter.chat_thread_fiction`

### "The big thing happens off screen and lands as nothing"

1. Off-screen is a beat, not an absence: it is registered by its noise, its aftermath, or the faces of the people who can see it
   `beat.offscreen_beat`
2. If a character narrates it instead, it now arrives shaped by the teller's interest in it — which is usually the reason to do it that way
   `beat.reported_beat`

### "The scene ends and the next one just starts"

1. Treat the last beat of one scene and the first of the next as a single designed unit
   `beat.scene_handoff`
2. The strongest version puts the action at the end of one scene and the reaction as the first image of the next, so the cut performs the beat and no line closes it
   `beat.edit_carried_beat`

### "The line explains the blow while it lands it"

1. That is `beat.preempted_beat` — the action half already contains its own reaction, so the second half has nothing left to do
2. Its sibling is `beat.announced_beat`: *something shifted in the room*, *this was the moment everything turned*. A report of a beat instead of a beat
3. The repair for both is to write the second half as an act — and to let it be physical or silent rather than spoken
   `beat.reaction_beat` · `beat.silent_beat`

### "The narration is saying what the scene already showed"

1. Split the halves across the two layers: the image acts and the narrator reacts, or the narrator asserts and the image contradicts
   `beat.narrated_beat`
2. Check first that the narration is not simply naming the beat, which is the failure above
   `beat.announced_beat`

### "The poem is a run of statements"

1. In verse the unit is line and stanza, not speech and reply — the line makes a claim and the break takes it back, qualifies it, or raises it
   `beat.verse_beat`

### "I don't know why the character starts singing here"

1. Because speech ran out. That is the beat — the tactic exhausts dialogue and the song is the next move, not a convention to be got through
   `beat.song_entry_beat`
2. Once inside the song the beat is a section, not a line: the verse moves, the pre-chorus reacts, the chorus states the consequence, the bridge reverses
   `beat.lyric_beat`

### "The comic page has no timing"

1. The reaction half is often not drawn at all. Action in panel one, consequence in panel three, and the reader performs the beat in the gutter
   `beat.panel_gutter`
2. That is the timing inside a spread. The timing *between* them is the page turn, which is the only hard cut in the form and is planned at thumbnail stage before a line of dialogue is written — and a book has perhaps six real turns in it, so do not spend one on information a caption could have carried
   `tens.page_turn`

### "The game is holding on the player's line and the writing sags"

1. An interactive beat can stay open indefinitely, so the writing has to survive being paused inside it
   `beat.player_held_beat`
2. And where the player supplies the action half, you are only ever authoring the reaction — several times over
   `beat.branch_beat`

### "In audio the beat needs a look and there isn't one"

1. Both halves must be audible: a sound acts, and a voice, a movement or a changed ambience answers. Nothing can be carried by a face
   `beat.audible_beat`

### "The vertical cut feels slow and I can't see why"

1. Action and reaction have to complete inside a couple of seconds, which puts the beat count per minute at three to five times a feature's
   `beat.shortform_beat`

### "The real-time scene drags"

1. When story time equals screen time, every beat is paid at full length and the count is fixed by the clock rather than chosen
   `beat.real_time_beat`
2. The nearby instrument, and usually the better one: put a live deadline in the scene and let the characters truncate their own reactions
   `beat.clock_compression`

### "The character is alone and nothing is happening"

1. Give the reaction half to the character's own body, memory or intention — they try something and something in themselves answers
   `beat.solo_beat`
2. Or let the place answer: the weather, the building, the machine, held to the same action/reaction discipline as a person
   `beat.environment_beat`
3. The most reliable of the three is a task that answers back — the knot holds, the engine catches, the dough is wrong
   `beat.task_beat`

### "The joke lands and then the scene deflates"

1. Break the break: a fourth beat that reframes the joke that just landed
   `beat.double_topper`
2. Across a whole episode, reintroduce one beat shape at intervals, modified each time, so it accumulates rather than repeats
   `beat.runner_beat`
3. And the version that pays best is the one brought back after the audience stopped waiting for it
   `beat.distant_callback`

### "The character decides between scenes"

1. Show the choosing as an act rather than reporting it as a conclusion — the option presented is the action half, the choice is the reaction
   `beat.decision_beat`

### "The scene that carries the information has facts and no exchange"

1. Make every fact the *reaction* half of a beat in which somebody wanted it, resisted it, or paid for it
   `beat.exposition_beat`

### "I can't find the beats in my own draft"

1. Hear it read by other people at speed. Hesitations, two readers taking the same beat, and a page that produces no reaction at all are visible only out loud
   `beat.table_read_test`
2. In a room, divide the scene into units collectively and name each one, so everybody is playing the same units
   `beat.beat_map`
3. And know that `(beat)` is a US screenwriting convention rather than a universal one, before auditing a script that does not use it
   `beat.notation_traditions`

### "Every exchange in the scene is the same size"

1. That is `beat.symmetry_fatigue` — same shape, same length, same pitch, so the reader predicts the rhythm and stops hearing it
2. The repair is the length-variation card run as a pass rather than held as a preference
   `beat.length_variation`

### "Someone reacts hard to something I never showed"

1. That is `beat.orphaned_reaction`: the action half exists in your notes, or was cut, or was implied too faintly to reach anyone

### "The run of scenes is three things happening and I can't say what it's about"

A run without a question is not a sequence. This is the level at which most middles fail, and the diagnosis is almost always that the writer never wrote the run down as a unit.

1. Reduce the whole story to one block per sequence — the question, the scenes in a line each, the climax, and the cost. Two to four pages, before drafting
   `seq.sequence_outline`
2. Then check the run's first page delivers exactly the minimum a reader must hold, and nothing else
   `seq.run_entry_context`
3. If the run is meant to carry the story's claim, it is the *price it charges* that states it, not anything anyone says inside it
   `seq.thematic_run`

### "The sequence only turns at the very end"

1. Put a reversal about two-thirds in that changes how the goal must be pursued or what it will cost — while leaving the run's question open
   `seq.mid_run_turn`

### "I planted things and never paid them"

1. Two columns and nothing else: every plant with the sequence that plants it, every payoff with the sequence that pays it
   `seq.payoff_ledger`

### "I don't know how many sequences this should have"

1. There is a working ratio between running time and sequence count, used as a planning budget rather than a rule of form
   `seq.count_vs_runtime`
2. The subplot's runs come out of that same budget — cut them in so two mid-level questions are live at once without either losing its shape
   `seq.subplot_interleave`

### "The adaptation came out eighty pages over"

1. Because the scenes were converted one for one. Carry each source sequence's *question and climax* across instead, and rebuild its scenes from scratch in the new medium
   `seq.media_transposition`

### "The character has options and the run is just weighing them"

1. That run's question is *which*, not *whether* — so its scenes close options one at a time and the climax is a choice made rather than a goal won
   `seq.decision_run`

### "The pre-title sequence is just a taste of the film"

1. It should be a complete small sequence whose climax is the question the rest of the piece answers
   `seq.cold_open_sequence`

### "The flashback is long enough to be its own film"

1. Then build it as one: three or more scenes with their own question and climax, dropped inside the present-tense run
   `seq.embedded_past_run`
2. The same holds for what never happened — a dream, a fantasy, a rehearsal in the head — played at full length rather than flagged as unreal
   `seq.imagined_sequence`

### "The wedding is a list of things that happen at weddings"

1. Let the ceremony's fixed steps supply the scene order, then assign a private conflict to each step. The form does the structuring; you only supply the drama
   `seq.ritual_sequence`
2. If what you want is for the ceremony to be unbearable rather than merely structured, that is the tension complaint "The wedding goes perfectly and it's the worst thing in the film", and a third card
   `tens.ritual_that_must_continue`

### "The trial is a row of speeches"

1. Use the proceeding's own order — testimony, cross, submission, verdict — and make each witness move the outcome. The climax is the moment the verdict becomes inevitable, not the moment it is read out
   `seq.hearing_sequence`
2. If the scene is a deal rather than a judgement the engine is different: concessions traded across scenes, and the climax is the moment one side's alternative to a deal is destroyed
   `seq.negotiation_sequence`

### "They're under siege and it's just waiting"

1. Structure it by what is taken away from them rather than by what attacks them — water, light, a radio, a person
   `seq.siege_sequence`

### "The undercover stretch has no pressure"

1. Bring a more expert observer into each scene, so the run's question is whether the cover holds
   `seq.infiltration_sequence`
2. Its inverse, if they are already known to be inside: capabilities stripped rather than acquired, and improvisation from whatever is physically present
   `seq.escape_sequence`

### "The horror section isn't frightening"

1. One space, one ordinary objective, a dread that ratchets on a short cycle, and the exits closing
   `seq.stalk_sequence`

### "The comic set piece runs out halfway"

1. Build the run on a gag that returns across its scenes, each return larger or more inappropriate, with the topper as the sequence climax
   `seq.comic_run`

### "The second half repeats the first"

1. That is `seq.repeated_sequence`: two runs asking the same question and answering it the same way, usually because the first one did not feel like it landed
2. The honest fix is to cut one and let the other land, not to make both bigger

### "I cut the whole section and nothing changed"

1. That is `seq.orphaned_sequence` — well built, and never referred to again
2. The version that hurts most is the one that promised a meeting: threads converge, exchange information, and separate roughly as they were
   `seq.false_convergence`

### "The run peaks and then keeps going"

1. That is `seq.premature_climax`; the biggest beat arrived before the last scene, so the rest plays as descent
2. The repair is at act level — vary the run lengths and put the peak where the act's rhythm wants it
   `seq.act_rhythm`

### "After that stretch the story has to start again from a standstill"

1. That is `seq.full_resolution_stop`: an internal run that answered its question completely and left nothing open
2. A sequence resolves *partially*. The card that states the rule is the one to work from
   `seq.partial_resolution`

---
