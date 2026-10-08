# Point of view complaints

Part of the symptom router. Open this file when the complaint is about point of view. Each complaint below is followed by the cards that repair it, best first; `LOOKUP.md` says which file holds each card.

---

### "I don't know whose story this is"

1. Assign each scene to the character with the most to lose in it
   `pov.scene_ownership` · `pov.multi_pov_architecture`
2. Set the contract early and break it only with a licence
   `pov.contract` · `pov.licensed_break`
3. Handle the transitions deliberately
   `pov.handoff`

### "The POV keeps slipping"

1. This is the named failure, and it is not the same as omniscience
   `pov.head_hopping` · `pov.omniscient`
2. Check for observations the viewpoint character could not make
   `pov.impossible_observation` · `pov.mirror_description`
3. Cut the filter words — *she saw, he felt, she noticed*
   `pov.filter_word_removal`
4. If the slips keep coming back, the underlying confusion is usually **who speaks** versus **who sees** — they are two questions and English craft talk jams them into one. Separating them fixes slips that no line edit reaches
   `pov.focalisation`
5. Then run the repair as its own pass rather than catching them one at a time
   `pov.distance_audit`

### "The narration feels distant when it should be close"

1. Psychic distance is a slider, not a setting. Learn the rungs
   `pov.psychic_distance_ladder` · `pov.distance_slide`
2. Free indirect style gets you inside without first person
   `pov.free_indirect_style` · `voice.free_indirect_style`
3. Choose the position knowingly
   `pov.close_third` · `pov.distant_third` · `pov.first_person_central`

### "The viewpoint character just watches"

1. The named failure, and a common one in first-person framing
   `pov.inert_viewpoint`
2. A peripheral narrator must want something of their own
   `pov.peripheral_narrator`
3. Otherwise move the camera to whoever is acting
   `pov.scene_ownership`

### "I want an unusual viewpoint"

1. Second person, the collective, a child, a non-human, an institution, a document
   `pov.second_person` · `pov.collective_we` · `pov.child_pov` · `pov.nonhuman_pov` · `pov.institutional_pov` · `pov.found_document`
1b. Or refuse interiority entirely and report only what is observable
   `pov.objective_camera` · `pov.reportage_stance`
1c. In interactive work the viewpoint belongs to someone who acts
   `pov.playable_pov` · `inter.player_character_voice`
1d. Translation moves the viewpoint whether you intend it or not
   `pov.translation_shift`
2. In screenwriting there is no interiority at all — that is the constraint to design around
   `pov.screen_no_interiority`
3. In comics the caption and the panel can hold different viewpoints
   `pov.comics_caption_panel`
4. The same event from two viewpoints, done deliberately
   `pov.same_event_twice` · `pov.retrospective_distance`


### "There's a story inside the story and I've lost who's telling it"

1. A narrator who introduces a second narrator is a structure with layers, each with its own distance, its own audience and its own reason to shade the account
   `pov.nested_tellers`
2. Decide who the telling is aimed at. It exists in every narrated text and most writers never choose it — a court, a child not yet born, a stranger, nobody in particular
   `pov.narratee`
3. If the piece is going to acknowledge the telling as a telling, do that on purpose and early
   `pov.direct_address`
4. And the thing readers actually assemble from all of it is not the narrator — it is the set of judgements that chose this narrator
   `pov.implied_author`

### "The newcomer is explaining her own world to me"

1. That is `pov.tour_guide_narrator`: an insider glossing her own terms, dating her own festivals, describing her own rituals as though seeing them for the first time
2. The repair is to make the ignorance real rather than borrowed — hand the viewpoint to the character who genuinely knows least, and let the world be explained *to* them
   `pov.reader_surrogate`
3. If the position is one you do not hold, the card that names what you will get wrong by default is the one to read first
   `pov.positionality`

### "The narrator can't be trusted about himself"

1. One body, more than one narrating self — or a narrator who plainly does not know what he did
   `pov.split_narrator`
2. If the telling comes from after the death, that is a property of the narration and not of the plot; no ghost need appear
   `pov.posthumous_narrator`
3. If the mind itself is built differently — autism, psychosis, dementia, aphasia, an artificial mind, extreme pain — the difference is structural, in perception and time sense, not a layer of odd diction
   `pov.divergent_cognition`

### "The short story spends its first page setting up the viewpoint"

1. It has no room to. The reader must know who is telling it, how close and how trustworthy inside two sentences, and there is no space to teach a second position
   `pov.short_form_pov`
2. The related trap: a prologue in a voice the book then abandons, which silently teaches a contract the novel does not intend to keep
   `pov.prologue_pov`

### "Book three and my viewpoint character already knows everything"

1. The original POV character's ignorance is a consumable resource, and a series spends it by book two
   `pov.series_pov`
2. In a room, the equivalent discipline is assigning each strand to the character who owns it, so an ensemble still has a person whose episode it is
   `pov.episode_ownership`

### "Viewpoint in something that isn't a book"

1. In audio there is no image, so position is built from three things only — who narrates, whose acoustic space the microphone occupies, and what the listener is allowed to hear
   `pov.audio_pov`
2. In song, the choice between an "I" who is the artist, an "I" who is plainly a character, a "you" and a "we" sets the whole distance
   `pov.song_pov`
3. In commercial copy, whether the brand is "we", the customer is "you", or nobody is named
   `pov.brand_pov`
4. Told aloud to a present audience, the teller is visibly relaying rather than inventing, and the chain of transmission is spoken as part of the telling
   `pov.oral_narration`

### "I can't tell whether the distance is right"

1. Write the same opening page once at each rung, changing nothing about the events, then choose — and then write a sixth version that moves deliberately between rungs
   `pov.opening_page_exercise`
2. On an existing draft, run viewpoint and distance as their own revision layer, separately from plot and line editing
   `pov.distance_audit`

### "I'm in the piece and I don't know how much"

A non-fiction question rather than a fictional one. The stance is decided before the first sentence — present and named, present and invisible, or absent — and the commonest failure is not the choice but the **drift**: a piece that begins as observation and becomes advocacy in the middle third, at the point where the writer got angry.

1. Fix the stance and hold it. There are three legitimate reasons to appear and no others: you caused what happened, you are the only witness to it, or the reader needs to know how you know
   `scene.writer_in_the_scene`
2. Use "I" for the transaction, not for the feeling. *I asked him three times* earns its place; *I felt a chill* spends the reader's trust on something they cannot check
3. The hard prohibition that separates this from fiction: you may not furnish the scene beyond the evidence. The weather nobody recorded and the expression nobody described read as vividness and function as invention
4. If you are appearing in order to prove you were there, put the proof in the reporting instead. The first person is a claim on attention and it is earned by consequence, not by effort — a paragraph explaining why you took the assignment is the standard tell
5. What your access does to the shape of the whole piece is the larger question behind this one
   `info.access_as_structure`
6. The fiction-side move, where the narrator addresses the reader by design rather than by necessity
   `pov.direct_address` · `voice.addressing_the_reader`

---
