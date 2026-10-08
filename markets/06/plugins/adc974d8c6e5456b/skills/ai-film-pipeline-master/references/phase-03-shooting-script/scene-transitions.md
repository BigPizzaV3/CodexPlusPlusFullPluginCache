# Scene-to-Scene Transitions and Visual Structure

134 cards. These decide a shot: how it moves, how it cuts, and how it sits in time.

Every card carries what it is, what it does to the audience, where it works best, what to avoid, and the prompt written out in full.


> **This file is half of a shelf.** The `scene.` cards sit in four files across two phases: the ones here join two scenes together, and the ones in Phase 2 build a scene internally. **They are two decisions, not one**, and the first thing to settle is which of the two you are making — `scene.build_or_join`, at the head of this file, asks it. The cards that have an alternative carry it in their `Yields to:` field, which names the card that takes over when their own conditions fail; the rest are listed in [`PAIR-AUDIT.md`](../PAIR-AUDIT.md) with the reason they have none.

---

### Which Scene Are You Deciding — This One, or the Seam

**Also called:** the scene selector, build or join, the two-decision fork
**What it is:** The card at the head of the `scene.` shelf — the largest family in the package, in four files across two phases. It does not describe a scene. It asks **one fork and then three questions on whichever side of the fork you landed**, and hands back a named shortlist for each answer. The fork is *are you building the inside of one scene, or joining this scene to the next*, because `SHELVES.md` §2b and the shelf's own pair graph both say these are two decisions made months apart by different phases. The axes were not invented: they were read off every `Yields to:` condition the routable cards carry, and the conditions that repeated became the questions. Every card cited here is cited by id.
**Effect on the audience:** None. This card never reaches the screen. It exists so that the scene that does reach the screen was chosen against the value, the room and the seam, rather than picked because it was the last one read.
**Used for and where it works best:** **Settle the fork out loud before opening any file.** The test is mechanical: *do you need two scenes on the desk for this decision to exist?* If the decision survives with one scene in hand it is a build decision and lives in Phase 2; if it needs the scene on either side of a cut it is a join decision and lives in Phase 3. Then answer that half's three questions in one sentence each. On the build side the first answer eliminates roughly two-thirds of the file; on the join side the first answer eliminates three-quarters. Where the same moment is genuinely both — a montage that replaces a scene, an act break that also ends a scene — **it is two decisions and you make them in order**, build first, join second, never at once.
**Best in:** formats: all narrative | genres: all narrative
**Avoid when:** **You cannot answer the fork honestly, because the commonest error on this shelf is being wrong about which decision you are making — and a wrong fork cannot be repaired by re-answering questions two and three, since the whole map under it is laid out wrong.** The tell that you forked wrong is that the card you land on keeps needing the other half's cards to work. Also distrust this map wherever your honest answer to the join half's first question is *inside the body*: sixty-six of the hundred and thirty-two on that half live there, so on an ordinary mid-film cut the map has two questions left and is doing half the work it does at an opening or an ending. And do not bring it to a scene that already exists and is dead — there the shelf has its own front door, `scene.dead_scene_test`, and diagnosis precedes choosing.
**Prompt:** `[Selector — produces no prompt. It returns card ids. The chosen card carries the prompt.]`

---

**The axes**

**The first fork — do you need two scenes on the desk for this decision to exist?**
Asked before anything, and it is the shelf's own answer rather than a filing convention. `scene-transitions.md` says it in its own line 8 — *"This file is half of a shelf"* — and the pair graph confirms it by measurement: **of the hundred and sixty-five within-shelf `Yields to:` edges, a hundred and fifty-seven stay inside their half and eight cross — fewer than one in twenty.** The two halves are eighty-five that build a scene and a hundred and thirty-two that join two, and a reader who answers this wrong is reading the wrong file for the rest of the session. The shelf even names the fork inside a condition: `scene.act_to_act` yields to `scene.prelap_join` when *"Inside an act: join without stopping the film."*

---

**BUILD — you have one scene**

**Axis B1 — What does this unit run on?**
The condition the build half repeats most; **twenty-five of its cards state it in their `Yields to:` line.** *"Form runs on accumulation, not on charge change"* (`scene.value_turn`), *"Nobody in the scene can want anything"* (`scene.goal_conflict_disaster`), *"The story runs on escalating opposition"* (`scene.kishotenketsu_scene`), *"Nothing is pending; the scene must turn"* (`scene.development_scene`), *"the scene is deliberately a sequel, which runs on weighing rather than wanting"* (`scene.give_a_want`), *"The sequence arrives at a choice"* (`scene.crosscut_acceleration`), *"Ensemble work: cutting away is the sequel"* (`scene.scene_and_sequel`), *"Three in a row: write it as a montage"* (`scene.one_line_scene`).

**Axis B2 — Who else is in the room, and what keeps them in it?**
**Twenty-five conditions turn on the population of the room and the thing that holds it shut**, and they are stated as facts: *"The third person has no stake"* (`scene.third_party_arrival`) against its exact reverse *"The third person has a stake"* (`scene.before_a_stranger`); *"Only one party may speak"* (`scene.public_scene`) against *"The room can answer back"* (`scene.aimed_through_the_room`); *"These people would simply leave"* (`scene.trap_scene`); *"Use a person with a stake, not an obstacle"* (`scene.barrier_mid_scene`); *"The far end carries precise plot"* (`scene.one_sided_call`); *"A reasonable refusal must be printed, not framed"* (`scene.interview_breaks`).

**Axis B3 — Where does it start, where do you cut it, and what does it hand over?**
**Fourteen conditions, and they are about seconds rather than shape:** *"where the arrival *is* the scene"* (`scene.late_entry`), *"where the meaning lives in the aftermath rather than the event"* (`scene.early_exit`), *"The format cannot afford the held seconds"* (`scene.held_exit`), *"Three open closes in a row"* (`scene.close_on_question`), *"Location unchanged or inferable"* (`scene.orientation_beat`), *"where the outgoing scene needs its silence"* (`scene.prelap_join`), *"Non-causal structures join by rhyme"* (`scene.cause_out_question_in`). Asked last because it is the only axis that reaches the handover cards at all.

---

**JOIN — you have two scenes**

**Axis J1 — Where does this seam sit in the piece?**
**Thirty-six conditions turn on position, not on content**, and position is the only thing that eliminates whole blocks at once: *"No room for a self-contained scene"* (`scene.cold_open`), *"Stretched, it is a weak cold open"* (`scene.teaser`), *"Vertical: the thumb moves first"* (`scene.establishing_opening`), *"Weak cold open; hold the title back"* (`scene.opening_to_titles`), *"No descent; convert energy into credits"* (`scene.climax_to_denouement`), *"Tragedy or heritage; grief needs silence"* (`scene.hard_cut_to_credits`), *"No honest reversal; mark the act plainly"* (`scene.act_break_open_question`), *"The segments need to meet"* (`scene.anthology_chapters`).

**Axis J2 — What actually changes across the cut?**
The largest axis on the shelf: **fifty-five conditions.** *"Functional joins want continuity"* (`scene.value_turn_cut`), *"Repeated drops numb; alternate the direction"* (`scene.hope_to_fear`) against *"The film wants the viewer held tight"* (`scene.fear_to_relief`), *"Not every question may be answered"* (`scene.question_to_answer`) against *"Some questions must be paid off"* (`scene.cut_on_the_question`), *"The ladder has become mechanical"* (`scene.answer_to_new_question`), *"No gap between public and private self"* (`scene.public_to_private`), *"The incoming character was never planted"* (`scene.pov_handoff`), *"The first appearance was not distinctive"* (`scene.callback_shot`).

**Axis J3 — What carries it, and will the screen let it?**
**Seventeen conditions — and every one of the ten conditions on the shelf that name the format as the thing that stops the card sits on this axis or next to it** — every one of them on this axis or adjacent to it: *"Grade cannot carry it on a phone"* (`scene.flashback_colour_shift`), *"Vertical; a ratio shift reads as a fault"* (`scene.flashback_ratio_change`), *"Phone viewing; two panels maximum"* (`scene.split_screen_multipanel`), *"Short-form reads black as empty"* (`scene.black_screen_sound_opening`), *"Muted viewing; carry the drop visually"* (`scene.loud_to_quiet`), plus *"Convey the era visually, not by card"* (`scene.flashback_hard_cut_time_card`), *"The shot already explains the time"* (`scene.time_card`), *"Nothing was planted to trigger it"* (`scene.flashback_sound_cue`), *"The montage is cliché; one match cut"* (`scene.montage_training`).

---

**The map**

**BUILD — Axis B1: what does this unit run on?**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A want that is opposed** (11) | `scene.goal_conflict_disaster` · `scene.value_turn` · `scene.scene_question` · `scene.scene_and_sequel` · `scene.mru` · `scene.tactic_change` · `scene.escalating_cost` · `scene.barrier_mid_scene` · `scene.granted_wish` · `scene.reversal_of_power` · `scene.reversal_of_expectation` |
| **Absorbing the last blow — nobody wants, they weigh** (3) | `scene.reaction_dilemma_decision` · `scene.apology_that_lands` · `scene.confirmation_scene` |
| **Accumulation — nothing turns, by design** (5) | `scene.kishotenketsu_scene` · `scene.development_scene` · `scene.silent_scene` · `scene.wordless_channel_discipline` · `scene.waiting_room` |
| **A span of time, not a room** (5) | `scene.montage_value_turn` · `scene.montage_single_theme` · `scene.one_line_scene` · `scene.single_action_scene` · `scene.length_follows_value` |
| **Two places at once** (3) | `scene.crosscut_pair` · `scene.ironic_parallel` · `scene.crosscut_acceleration` |
| **Nothing, and you cannot say why** (8) | `scene.dead_scene_test` · `scene.give_a_want` · `scene.transplant` · `scene.swap_who_wants` · `scene.merge_two_scenes` · `scene.absorb_and_delete` · `scene.change_the_shape` · `scene.third_attack` |

**BUILD — Axis B2: who else is in the room, and what keeps them there?**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Two, and nobody else** (1) | `scene.two_hander` |
| **A third who has a stake** (2) | `scene.third_party_arrival` · `scene.child_present` |
| **A third who has none** (1) | `scene.before_a_stranger` |
| **A room that can answer back** (2) | `scene.public_scene` · `scene.ensemble_scene` |
| **A room that cannot** (2) | `scene.aimed_through_the_room` · `scene.unaware_participant` |
| **A clock holds them** (1) | `scene.ticking_scene` |
| **A lock holds them — leaving is not available** (2) | `scene.trap_scene` · `scene.no_leverage` |
| **A duty or an object holds them** (2) | `scene.transaction_scene` · `scene.handover` |
| **A form holds them, and it can be broken** (3) | `scene.interrupted_ritual` · `scene.threshold_scene` · `scene.played_twice` |
| **They are not in one room** (5) | `scene.phone_call_split` · `scene.one_sided_call` · `scene.moving_vehicle` · `scene.second_language_scene` · `scene.untranslated_line` |
| **One of them is real and can withdraw** (7) | `scene.reconsent_scene` · `scene.approval_conversation` · `scene.interview_breaks` · `scene.performed_for_camera` · `scene.right_of_reply` · `scene.transcript_built` · `scene.writer_in_the_scene` |

**BUILD — Axis B3: the edges and the handover**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Start after it began** (2) | `scene.late_entry` · `scene.entering_on_the_answer` |
| **Start by orienting** (1) | `scene.orientation_beat` |
| **Start on a thing, or on a face** (2) | `scene.opening_on_object` · `scene.opening_on_reaction` |
| **Start on a coming or a going** (2) | `scene.arrival_scene` · `scene.departure_scene` |
| **Cut it hard** (3) | `scene.button` · `scene.early_exit` · `scene.interrupted_scene` |
| **Hold it** (2) | `scene.held_exit` · `scene.close_on_question` |
| **Hand it to the next scene** (3) | `scene.cause_out_question_in` · `scene.match_join` · `scene.prelap_join` |

**JOIN — Axis J1: where does the seam sit?**

| Answer | The shortlist, by id |
| :--- | :--- |
| **Before the piece has started — opening and titles** (15) | `scene.cold_open` · `scene.teaser` · `scene.in_medias_res` · `scene.hook_opening` · `scene.establishing_opening` · `scene.scale_reveal_opening` · `scene.black_screen_sound_opening` · `scene.photo_to_live_opening` · `scene.prologue_other_time` · `scene.opening_to_titles` · `scene.titles_to_first_scene` · `scene.title_drop` · `scene.smash_to_title` · `scene.credits_over_action` · `scene.previously_on` |
| **At an act, episode or chapter seam** (9) | `scene.act_to_act` · `scene.act_break_open_question` · `scene.episode_to_episode` · `scene.next_time_tease` · `scene.cliffhanger_before_ad_break` · `scene.chapter_cards` · `scene.colour_as_chapter` · `scene.location_as_chapter` · `scene.anthology_chapters` |
| **At the end** (17) | `scene.climax_to_denouement` · `scene.last_scene_to_end` · `scene.hard_cut_to_credits` · `scene.freeze_frame_ending` · `scene.cut_to_black_mid_action` · `scene.end_on_a_question` · `scene.epilogue_time_jump` · `scene.the_stinger` · `scene.mid_and_post_credits` · `scene.the_button` · `scene.silent_epilogue` · `scene.walk_into_the_distance` · `scene.door_closes_ending` · `scene.pull_back_reveal_ending` · `scene.return_to_opening_image` · `scene.bookends` · `scene.opening_image_answered` |
| **Inside the body** (92) | Go to J2. It is named by complement on purpose: listing 92 ids here would make the map longer than the shelf |

**JOIN — Axis J2: what changes across the cut?**

| Answer | The shortlist, by id |
| :--- | :--- |
| **The charge** (27) | `scene.value_turn_cut` · `scene.hope_to_fear` · `scene.fear_to_relief` · `scene.calm_to_chaos` · `scene.chaos_to_silence` · `scene.joke_to_tragedy` · `scene.comedy_to_serious` · `scene.tension_to_comedy` · `scene.loud_to_quiet` · `scene.before_to_aftermath` · `scene.promise_to_consequence` · `scene.plan_to_execution` · `scene.decision_to_result` · `scene.question_to_answer` · `scene.answer_to_new_question` · `scene.cut_on_the_question` · `scene.buildup_to_reveal` · `scene.reveal_to_aftermath` · `scene.slow_monster_reveal` · `scene.dialogue_to_fight` · `scene.dialogue_to_chase` · `scene.chase_to_capture` · `scene.set_piece_entrance` · `scene.training_to_performance` · `scene.life_to_death` · `scene.arrival_to_departure` · `scene.same_action_new_place` |
| **The clock** (14) | `scene.day_to_night` · `scene.night_to_dawn` · `scene.past_to_present` · `scene.present_to_memory` · `scene.flash_forward` · `scene.memory_pop` · `scene.dream_to_waking` · `scene.waking_to_dream` · `scene.dream_sequence` · `scene.fantasy_insert` · `scene.same_frame_time_jump` · `scene.seasons_aging_transition` · `scene.walk_past_pillar_age_change` · `scene.repeated_shot_one_change` |
| **The place, or the scale** (7) | `scene.interior_to_exterior` · `scene.tight_to_wide_release` · `scene.wide_to_tight_focus` · `scene.public_to_private` · `scene.crowd_to_alone` · `scene.rich_to_poor_contrast` · `scene.establish_then_cover` |
| **Whose story it is** (7) | `scene.storyline_handoff` · `scene.pov_handoff` · `scene.meanwhile_crosscut` · `scene.parallel_lives` · `scene.ticking_clock_crosscut` · `scene.converging_storylines` · `scene.rashomon_repeat` |
| **Nothing — it rhymes** (6) | `scene.mirror_scene` · `scene.callback_shot` · `scene.visual_rhyme` · `scene.sound_motif_return` · `scene.object_handoff` · `scene.planted_object_payoff` |
| **Nothing across the cut — you are deciding how much of each scene survives it** (5) | `scene.enter_late_leave_early` · `scene.one_scene_one_idea` · `scene.enter_on_movement_exit_on_stillness` · `scene.alternating_rhythm` · `scene.master_to_coverage_rhythm` |

**JOIN — Axis J3: what carries it?**

| Answer | The shortlist, by id |
| :--- | :--- |
| **A span replaces the cut — a montage** (15) | `scene.scene_to_montage` · `scene.montage_to_scene` · `scene.montage_intellectual` · `scene.montage_time_compression` · `scene.montage_training` · `scene.montage_travel_map` · `scene.montage_falling_in_love` · `scene.montage_getting_ready` · `scene.montage_the_plan` · `scene.montage_the_search` · `scene.montage_decline` · `scene.montage_aftermath` · `scene.montage_hands_at_work` · `scene.montage_newspaper_headlines` · `scene.map_line` |
| **A card or a caption** (2) | `scene.time_card` · `scene.flashback_hard_cut_time_card` |
| **A change of look** (4) | `scene.flashback_colour_shift` · `scene.flashback_ratio_change` · `scene.flashback_desaturation` · `scene.flashback_dissolve` |
| **Sound crosses first** (1) | `scene.flashback_sound_cue` — and note that the shelf's other two sound carriers sit elsewhere by function: `scene.prelap_join` on the build half, `scene.sound_motif_return` under J2's *rhymes* |
| **The frame splits** (4) | `scene.split_screen_depalma` · `scene.split_screen_multipanel` · `scene.split_screen_phone_call` · `scene.phone_call_intercut` |
| **One cut, picture only** (107) | Every other card named in the J1 and J2 tables. Named by complement, for the same reason as J1's fourth value |

*A card appears once per half and once per axis. On the build side the answer is the intersection of B1, B2 and B3 and is normally two to five cards wide; on the join side, J1 alone often leaves a shortlist of nine.*

---

**The default, and the one against it**

**The default on the build half is `scene.value_turn` and `scene.goal_conflict_disaster`, entered on `scene.late_entry` and cut on `scene.early_exit`.** The file argues for it in its own first card — *nothing else defines a scene* — and the four together answer B1, B3 and most of B2 in one move.

**But the shelf's own graph does not fall back there, and that is a finding rather than a contradiction.** Measured over every `Yields to:` edge on the shelf, the most-yielded-to cards on the build half are `scene.held_exit` and `scene.opening_on_reaction`, **four inbound each**, ahead of `scene.arrival_scene`, `scene.third_attack`, `scene.reaction_dilemma_decision` and `scene.two_hander` on three. `scene.value_turn` has **one**. The readers who wrote these fields fall back to the *edges* of a scene, never to its engine — because the engine is assumed and only the edges are argued about. Use the default; do not mistake it for the thing the shelf votes for.

**The default on the join half is `scene.value_turn_cut` on a hard cut**, and here the graph agrees with a caveat: the most-yielded-to card on the whole shelf is `scene.time_card`, four inbound, followed by `scene.life_to_death`, `scene.hard_cut_to_credits`, `scene.flashback_hard_cut_time_card`, `scene.same_frame_time_jump` and `scene.flashback_colour_shift` on three. **Five of those six are time cards.** When a join stops working, the shelf's instinct is to state the gap rather than to feel it — which is the correct fallback and the dullest one available.

**The one against the grain on the build half is `scene.wordless_channel_discipline`.** Nothing routes to it and it routes to nothing; it is one of the thirty-three on this shelf that neither receive nor give an alternative. It is also the only build card that begins from *there is no dialogue in this scene* and treats that as a discipline with rules — each channel carrying its own information, none repeating another — rather than as an absence to be repaired. On heritage, kids and music work the wordless scene is the normal case and the shelf files it as the exception, which is exactly the shape of a card that is never anyone's second choice.

**The one against the grain on the join half is `scene.montage_intellectual`.** Nothing routes to it either. Every other join on the shelf asks what changed in the story across the cut; this one asks what the collision of two unrelated images *means*, and it is the only card here where the two scenes need no story relation at all. Its own `Yields to:` admits the cost — *"The idea needs characters to carry it"*, handing over to `scene.parallel_lives` — which is a card that knows what it is for.

---

**The unasked**

**A hundred and one of the routable cards are the target of no `Yields to:` field anywhere on this shelf, and thirty-three of those neither receive nor give one.** The thirty-three are the true orphans — nothing sends you to them, and they send you nowhere. By id:

*Build half (fifteen):* `scene.mru` · `scene.scene_question` · `scene.escalating_cost` · `scene.dead_scene_test` · `scene.montage_single_theme` · `scene.silent_scene` · `scene.wordless_channel_discipline` · `scene.length_follows_value` · `scene.single_action_scene` · `scene.departure_scene` · `scene.reconsent_scene` · `scene.approval_conversation` · `scene.apology_that_lands` · `scene.writer_in_the_scene` · `scene.confirmation_scene`

*Join half (nineteen):* `scene.past_to_present` · `scene.rich_to_poor_contrast` · `scene.arrival_to_departure` · `scene.chase_to_capture` · `scene.scene_to_montage` · `scene.montage_to_scene` · `scene.previously_on` · `scene.opening_image_answered` · `scene.master_to_coverage_rhythm` · `scene.montage_time_compression` · `scene.montage_getting_ready` · `scene.montage_the_search` · `scene.montage_decline` · `scene.montage_aftermath` · `scene.montage_hands_at_work` · `scene.montage_newspaper_headlines` · `scene.silent_epilogue` · `scene.cliffhanger_before_ad_break` · `scene.alternating_rhythm`

**The shape of that list is the finding, not its length, and it has two shapes.**

**First: the montage region is a catalogue nobody compares.** Eight of the thirty-three are named montage subtypes — `getting_ready`, `the_search`, `decline`, `aftermath`, `hands_at_work`, `newspaper_headlines`, `time_compression`, `single_theme` — and `scene.scene_to_montage` is orphaned with them. The four montage cards that *are* in the graph are there only because something outside the region reaches in (`scene.montage_training` ↔ `scene.training_to_performance`, `scene.montage_the_plan` ↔ `scene.plan_to_execution`, `scene.map_line` ↔ `scene.montage_travel_map`, `scene.montage_falling_in_love` → `scene.two_hander`). **Inside the region nothing is an alternative to anything**, because these cards are filed by *subject* — what the montage is about — and subject is not a choice you make, it is a fact of the story. That is a filing axis wearing a card's clothes.

**Second: until September 2026 there was no way out of a montage.** `scene.scene_to_montage` covered going in and nothing covered coming out, so the join back into drama - where a montage is most often lost - was made by every editor from scratch. The rule for it already existed, twice: as a warning in `scene.scene_to_montage`'s own `Avoid when:` and as the craft rule of `seq.montage_sequence`. `scene.montage_to_scene` is now the far door and joins the two. Nothing on the shelf yields to it yet, which is why it stands in the join half's unasked list above.

**Third: the consent block is unasked entirely.** `scene.reconsent_scene`, `scene.approval_conversation` and `scene.writer_in_the_scene` are orphans, and the other four cards in that block are reached only from inside it. Nothing in the map routes a reader from an ordinary drama card into the contributor cards — so a scene becomes an ethics question only for someone who already knew it was one.

`scene.build_or_join`

---

### The Value Turn

**Also called:** value shift, charge change, scene-to-scene turn  
**What it is:** A scene change is decided by charge, not by location. Ask what value the first scene ends on (hope, fear, win, loss) and what value the next one opens on; the distance between the two picks the transition.  
**Effect on the audience:** The viewer feels the story advancing even when the location repeats, because the feeling moves. If both scenes carry the same value, the second one reads as redundant.  
**Used for and where it works best:** This is the first question in the edit, before choosing a cut or a dissolve. In features and series it is what keeps the middle from sagging; in short-form it decides where the cut that holds the thumb belongs. If the two values match, merge the scenes or drop one.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok), Music Video, Trailer / Teaser | genres: all  
**Avoid when:** Do not apply it as a formal rule to every cut. Functional scenes (an arrival, a passage, a set-up) sometimes want continuity rather than a turn.  
**Prompt:** `editor note: end scene A on its strongest value and open scene B on the opposite charge, place the cut on the first frame that carries the new value`  
**Yields to:** `scene.same_action_new_place` — Functional joins want continuity.  
`scene.value_turn_cut`

### Enter Late, Leave Early

**Also called:** late in early out, cut the handles  
**What it is:** Start the scene after it has already begun (they are seated, the argument is running) and cut out of it the moment its point lands, before it finishes logically. Arrivals, goodbyes and door business are dropped.  
**Effect on the audience:** The rhythm turns lean and the viewer feels they are catching up rather than waiting. The mind fills the missing edges, which makes the audience a partner in the scene.  
**Used for and where it works best:** The default rule for modern drama, streaming series and any dialogue scene. It matters most on connective scenes: join the car already moving, not starting; leave the office on the last real line, not on someone standing up. In short-form and vertical micro-drama it is the difference between three live seconds and ten dead ones.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Soap Opera / Telenovela | genres: Drama, Thriller / Suspense, Crime / Procedural, Comedy, Romance, Mystery / Whodunit, Legal Drama, Political Thriller  
**Avoid when:** When the arrival itself is the meaning (a man walking into a house he left twenty years ago) do not trim it. In contemplative and heritage material the length is the feeling.  
**Prompt:** `editor note: trim the head of the scene to the first line that carries information and cut the tail on the last line that changes something`  
**Yields to:** `scene.arrival_scene` — where the arrival itself is the meaning, and in contemplative or heritage material where the length is the feeling.  
`scene.enter_late_leave_early`

### Cut on the Question

**Also called:** leave the question open, forward pull cut  
**What it is:** You leave the scene at the moment a question has been planted (who is behind the door, what will he do with the money) and move on before it is answered. The answer arrives in a later scene, or never.  
**Effect on the audience:** It creates forward pull: the viewer carries the question into the next scene and stays alert instead of settling.  
**Used for and where it works best:** The backbone of any series that wants the next episode pressed, and of every trailer. In documentary, leave the question hanging so the following segment feels necessary. In short-form it is the internal hook that stops the scroll at the five second mark.  
**Best in:** formats: Drama Series Episode, Limited Series, Trailer / Teaser, Documentary Feature, Documentary Series, Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Feature Film | genres: Mystery / Whodunit, Thriller / Suspense, Crime / Procedural, True Crime, Drama, Political Thriller, Horror, Sci-Fi  
**Avoid when:** If every scene ends on a question the audience feels stalled and loses trust. Some questions must be paid off along the way, not all of them at the end.  
**Prompt:** `editor note: end the scene one beat after the question lands and before any reply, then cut straight into the next location`  
**Yields to:** `scene.question_to_answer` — Some questions must be paid off.  
`scene.cut_on_the_question`

### Hope to Fear

**Also called:** the drop, reversal cut down  
**What it is:** A scene ends with the characters winning or reassured, and the next one opens straight onto the threat: a door opening, an unknown number, an army on the move. The join is a hard cut with no cushion.  
**Effect on the audience:** The hardest value turn in cinema. The audience has not finished being glad before it is afraid, and it learns not to trust this world.  
**Used for and where it works best:** The end of act one in thriller and horror, and the "everything is fine" beat before disaster in war and disaster films. In series, place it right before the break. The power is all in the timing: cut on the first frame of the threat, not a second later.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Trailer / Teaser, Short Film, Anime (Japanese 2D), 3D CG Animation, Vertical Micro-Drama | genres: Thriller / Suspense, Horror, Drama, War, Disaster, Crime / Procedural, Sci-Fi, Survival, Tragedy  
**Avoid when:** If the threat has no planted root it reads as a cheap trick. Repeated every ten minutes it numbs the audience instead of alarming it.  
**Prompt:** `editor note: hold the smile one extra beat, then hard cut to the first frame of the threat with its sound already at full level`  
**Yields to:** `scene.fear_to_relief` — Repeated drops numb; alternate the direction.  
`scene.hope_to_fear`

### Fear to Relief

**Also called:** the exhale, release cut  
**What it is:** A scene ends on peak fear or danger and the next opens on calm: daylight, water, a child laughing, food. It usually plays as a cut with the old scene's sound bleeding a moment over the new image.  
**Effect on the audience:** It gives the audience a breath. The body unclenches, and that unclenching is exactly what makes the next blow land.  
**Used for and where it works best:** After a chase or a battle, and after a long horror sequence. Heritage documentary uses it after the siege or the fall: cut to a calm river or field and let the narration rest. In shonen anime it is the meal after the fight, a fixed convention of the genre.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), 3D CG Animation, Heritage / Historical Documentary, Documentary Feature, Short Film, Game Cinematic / Gameplay | genres: Action, Horror, Thriller / Suspense, War, Adventure, Shonen Battle (anime), Survival, Drama  
**Avoid when:** Do not stretch the relief past one scene or the energy drops and does not come back. Skip it entirely when the film wants the viewer held tight to the end.  
**Prompt:** `editor note: let the danger sound run two seconds over the first calm image, then drop to room tone and hold the wide`  
**Yields to:** `scene.hope_to_fear` — The film wants the viewer held tight.  
`scene.fear_to_relief`

### Question to Answer

**Also called:** payoff cut, the reveal join  
**What it is:** One scene poses an explicit question (where did he go, what is in the box) and the next opens directly on the answer with no line of explanation. The image is the answer.  
**Effect on the audience:** It delivers instant satisfaction and respects the audience, because nobody explained anything. It is also the fastest way to delete an entire scene from the script.  
**Used for and where it works best:** The rhythm engine of crime, procedural and explanatory documentary. In documentary, ask the question in narration and cut straight to the archive or the relief that answers it. In advertising: problem in shot one, product working in shot two, with no extra word.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Explainer, Commercial / TVC, Video Essay, News Report / Reportage | genres: Crime / Procedural, Mystery / Whodunit, True Crime, Science / Educational, Thriller / Suspense, Legal Drama, Drama, Heritage (civilisation-focused)  
**Avoid when:** Used on every question the story becomes a problem set and suspense dies. Let some questions wait two scenes before they pay.  
**Prompt:** `editor note: cut from the last word of the question straight to a clean image that answers it, no establishing shot in between`  
**Yields to:** `scene.cut_on_the_question` — Not every question may be answered.  
`scene.question_to_answer`

### Answer to New Question

**Also called:** the ladder, hydra cut  
**What it is:** The scene delivers the answer we were waiting for, then in its final second plants a detail that opens a bigger question. The cut lands on the new detail, not on the answer.  
**Effect on the audience:** It delivers satisfaction and unease in the same second. The viewer feels real progress and still cannot sit back.  
**Used for and where it works best:** The engine of long-form series and multi-episode mystery: we learn who the body is, but the clothes are not hers. In investigative documentary it ends every chapter. In a trailer it is the last three seconds: you answered what the film is and opened what happens next.  
**Best in:** formats: Drama Series Episode, Limited Series, Documentary Series, Trailer / Teaser, Feature Film, Vertical Micro-Drama, Vertical Short-Form (Reels, Shorts, TikTok), Video Essay | genres: Mystery / Whodunit, Crime / Procedural, True Crime, Thriller / Suspense, Political Thriller, Sci-Fi, Drama, Noir / Neo-Noir  
**Avoid when:** Do not plant a question you have no intention of paying; the audience remembers. If every episode ends on the same trick it becomes mechanical and transparent.  
**Prompt:** `editor note: after the answer lands, hold two seconds on the detail that contradicts it and cut on that frame`  
**Yields to:** `scene.question_to_answer` — The ladder has become mechanical.  
`scene.answer_to_new_question`

### Calm to Chaos

**Also called:** the rupture, smash into action  
**What it is:** A still, slow, quiet scene ends and without any cushion the next opens on violent movement, loud sound and handheld camera. The gap in rhythm and level is the transition itself.  
**Effect on the audience:** A hit to the chest. Eye and ear get no time to prepare, so the violence is felt in the body rather than understood.  
**Used for and where it works best:** The start of action after a domestic scene, the blast or the raid in war, the attack in horror. Double its power with a full second of silence at the tail of the calm scene. In short-form the same principle works in the first second: a still image, then a cut to motion.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Short Film, Anime (Japanese 2D), 3D CG Animation, Vertical Short-Form (Reels, Shorts, TikTok), Game Cinematic / Gameplay | genres: Action, War, Horror, Thriller / Suspense, Disaster, Survival, Crime / Procedural, Shonen Battle (anime)  
**Avoid when:** More than twice in a film it stops working and turns into noise. Do not use it if the calm scene was not given real time; without stillness there is no blow.  
**Prompt:** `editor note: mute the last 24 frames of the quiet scene, then hard cut to handheld action at full volume on a frame already in motion`  
**Source:** assumption — the package's working figure, not a published standard; set the silence by ear on the cut (24 frames is one second at 24 fps).  
**Yields to:** `scene.dialogue_to_chase` — No stillness to hit against.  
`scene.calm_to_chaos`

### Chaos to Silence

**Also called:** the aftermath cut, drop to nothing  
**What it is:** A scene at peak noise and movement cuts hard to a still, silent one: a wide frame, nobody moving, only wind or a ringing tone. It usually comes with a switch from handheld to a locked camera.  
**Effect on the audience:** The void after noise is felt in the body as loss. The viewer understands the cost without anyone saying what happened.  
**Used for and where it works best:** After the battle, after the blast, after the crash. This is the shot that counts the losses without dialogue, and its strongest form is the same location as the previous scene, now empty. In heritage documentary it is the ruin shot that follows the fall.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Documentary Feature, Heritage / Historical Documentary, Anime (Japanese 2D), Trailer / Teaser, Game Cinematic / Gameplay | genres: War, Drama, Tragedy, Action, Disaster, Survival, Heritage (civilisation-focused), Historical / Biopic  
**Avoid when:** Do not lay a sad cue over it immediately; silence is stronger than any music here. Do not clip it either: under five seconds it carries no weight. That five-second floor applies only where a bed survives — wind, a ringing tone, room tone; on true digital silence the ceiling is three seconds (`cut.to_silence`), past which the viewer reads a playback fault.  
**Prompt:** `editor note: cut from peak noise to a locked wide of the same place, drop to near silence with only wind, hold eight seconds`  
**Yields to:** `cut.to_silence` — on true digital silence with no bed surviving, where the ceiling is three seconds. Where wind, a ringing tone or room tone survives, the five-second floor stands.  
`scene.chaos_to_silence`

### Interior to Exterior

**Also called:** the door cut, inside out  
**What it is:** A move from a closed interior to an open exterior. The cleanest tool is to cut on a door opening or on light entering, so a movement motivates the cut.  
**Effect on the audience:** An immediate opening of air and sound. The ear hears a new ambience and the eye gets distance, so it reads as release or as exposure depending on the context.  
**Used for and where it works best:** After an interrogation or a fight in a closed room, and after any scene where the character feels trapped. In heritage documentary it is the step out of the museum hall onto the site itself. Bridge it with sound: let the street ambience arrive half a second before the picture.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Short Film, Travel / Real Estate / Hospitality, Commercial / TVC, Vertical Micro-Drama | genres: Drama, Crime / Procedural, Thriller / Suspense, Legal Drama, Heritage (civilisation-focused), Historical / Biopic, Romance, Coming of Age  
**Avoid when:** Without a movement or a sound to motivate it the cut is just a change of address and reads flat. Repeated every other scene it stops being an event.  
**Prompt:** `editor note: cut on the door swinging open, let exterior ambience pre-lap half a second, land on a wide of the street`  
**Yields to:** `scene.tight_to_wide_release` — Nothing motivates the door cut.  
`scene.interior_to_exterior`

### Day to Night

**Also called:** the day out, nightfall transition  
**What it is:** A passage of hours: a long dissolve, a timelapse of the sky, or the exact same camera angle with completely different light. The choice between the three sets how much time the audience feels.  
**Effect on the audience:** It delivers the feeling of a day closing, a cycle completed. Night works as a promise: everything after it reads as more dangerous, more honest and more intimate.  
**Used for and where it works best:** The end of a chapter in drama, and the run-up to any heist, escape or confession. The strongest form in heritage and travel work is the identical frame with the sun going down through it. In ads and travel, a short timelapse compresses a day into two seconds.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Travel / Real Estate / Hospitality, Documentary Feature, Music Video, Commercial / TVC, Game Cinematic / Gameplay, Anime (Japanese 2D) | genres: Drama, Crime / Procedural, Heist, Heritage (civilisation-focused), Historical / Biopic, Romance, Western, Adventure  
**Avoid when:** The sunset timelapse is a worn convention in travel and advertising; use it only when the frame itself is new. In a thriller a long dissolve bleeds the tension out.  
**Prompt:** `locked wide of the same location, timelapse from late afternoon to full night, clouds moving fast, lights coming on one by one`  
**Yields to:** `scene.time_card` — Thriller: a dissolve bleeds tension.  
`scene.day_to_night`

### Night to Dawn

**Also called:** first light, the survival cut  
**What it is:** A move from a long night to first light. The tools are a slow dissolve, a wide of the horizon with light creeping across it, or a straight cut from full darkness to a blue sky.  
**Effect on the audience:** Survival. The light alone tells the viewer the character lived and the night is over, with no line needed.  
**Used for and where it works best:** After the siege night in horror, survival or war, and after a birth or a death scene. In heritage work it is dawn breaking over the temple or the river after a dark chapter. Let sound lead the picture: birds, a call to prayer or a rooster entering before the cut.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Heritage / Historical Documentary, Documentary Feature, Anime (Japanese 2D), Music Video, Game Cinematic / Gameplay | genres: Survival, Horror, War, Drama, Adventure, Heritage (civilisation-focused), Faith / Biblical Epic, Western  
**Avoid when:** It has become a very predictable convention after any horror night. If the character did not really survive, dawn light lies to the audience and weakens the ending.  
**Prompt:** `wide static shot of the horizon in deep blue, the first orange light slowly creeping across the land, birds starting on the soundtrack`  
**Yields to:** `scene.life_to_death` — The character did not survive.  
`scene.night_to_dawn`

### Past to Present

**Also called:** return from flashback, come back cut  
**What it is:** Coming out of a flashback into the story's present. The exit must mirror the entry: if you went in on a dissolve you come out on one, if you went in on a colour shift the colour snaps back on the same frame.  
**Effect on the audience:** It puts the viewer back on solid ground. A clear, quick return converts what we learned in the past into immediate pressure on the present.  
**Used for and where it works best:** The best return point is the face of the character who was remembering, in the same body position as before the flashback, so the eye knows it is back without explanation. In documentary, return from archive to the witness's silent face. In crime series this return is the moment of understanding.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Heritage / Historical Documentary, Docudrama / Reenactment, Anime (Japanese 2D), Short Film | genres: Drama, Crime / Procedural, Mystery / Whodunit, Historical / Biopic, Heritage (civilisation-focused), Psychological / Arthouse, True Crime, War  
**Avoid when:** Do not return with a different device from the one you entered on; it confuses the timeline. And do not stay in the past so long that the viewer forgets what was happening in the present.  
**Prompt:** `editor note: mirror the entry device exactly, return on the rememberer's face in the identical body position, colour snaps back on the cut frame`  
`scene.past_to_present`

### Present to Memory

**Also called:** going into the past, memory entry  
**What it is:** Entering a past scene from the story's present. It needs at least two of three signals: a picture change (colour, ratio, grain), a sound change, and a camera rhythm slower or faster than the present.  
**Effect on the audience:** The audience accepts the jump without resistance when the signal is clear in the first frame. If it arrives late, they spend half the scene working out where they are.  
**Used for and where it works best:** The beat where a character hears a name or sees an object that opens the memory, and the testimony moment in documentary when the witness starts describing. The strongest entry is a shared object in the same frame position in both times. In heritage work: from a relief in a museum into the living scene it depicts.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Heritage / Historical Documentary, Docudrama / Reenactment, Anime (Japanese 2D), Short Film | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Psychological / Arthouse, Mystery / Whodunit, War, Romance, Tragedy  
**Avoid when:** Skip the old ripple and wavy-sound cliche; it plays as a joke now. And do not rely on a single signal if the same actor appears at the same age in both times.  
**Prompt:** `slow dissolve from a close-up of the object in the present into the identical object in the past, colour warmer and grain heavier, present ambience fading out`  
**Yields to:** `scene.flashback_hard_cut_time_card` — Same actor at the same age both times.  
`scene.present_to_memory`

### Dream to Waking

**Also called:** waking cut, the jolt awake  
**What it is:** A dream scene breaks on the moment of waking. The classic form is a smash cut to the character's face opening her eyes and drawing breath, with natural room sound snapping back in.  
**Effect on the audience:** It separates dream from reality in one blow and hands the viewer relief and unease at once: the danger was false, but the character's body is still afraid.  
**Used for and where it works best:** After a nightmare in horror and psychological drama, and after a desire scene in romance. The strongest version graphic-matches the last dream frame to the first bedroom frame, the face in the same position. In anime it is a fixed convention: the ceiling, then the face.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Anime (Japanese 2D), 3D CG Animation, Vertical Micro-Drama, Music Video, Game Cinematic / Gameplay | genres: Horror, Psychological Horror, Psychological / Arthouse, Drama, Sci-Fi, Surreal / Absurdist, Romance, Shojo (anime romance)  
**Avoid when:** The "it was all a dream" reveal at the end of an important scene is resented, because it removes the cost of everything we watched. Use it when the dream reveals something about the character, not when it cancels an event.  
**Prompt:** `smash cut from the dream's last frame to a tight close-up of her eyes snapping open, same head position, room tone returning at full level`  
**Yields to:** `scene.fantasy_insert` — Do not cancel an event; insert the wish.  
`scene.dream_to_waking`

### Waking to Dream

**Also called:** slipping under, dream entry  
**What it is:** Entering the dream without announcing it: the scene starts normal, then a single element breaks the logic (a door that was not there, a dead person seated, light with no source). The join is soft, not a cut.  
**Effect on the audience:** The viewer slips into the dream exactly as the character does, without noticing. By the time they understand, they are already inside it, so the fear becomes internal.  
**Used for and where it works best:** Psychological horror, surreal and fantasy work. The tools: widen the lens, strip ambience down to a low tone, and keep every camera move continuous and slow with no cuts. In anime and music video it is the doorway into the set-piece.  
**Best in:** formats: Feature Film, Short Film, Anime (Japanese 2D), Music Video, Experimental / Art Film, Drama Series Episode, 3D CG Animation, AI-Generated Clip | genres: Psychological Horror, Surreal / Absurdist, Horror, Fantasy / Epic, Psychological / Arthouse, Drama, Supernatural Horror, Sci-Fi  
**Avoid when:** Signalling it clearly from the start (soft focus, dream music) throws away the whole gain. The point is that the viewer notices late.  
**Prompt:** `continuous slow camera move with no cut, ambience fading to a single low tone, one impossible element entering frame naturally`  
**Yields to:** `scene.dream_sequence` — The dream must be announced.  
`scene.waking_to_dream`

### Same Action, New Place

**Also called:** match on action across scenes, action match transition  
**What it is:** You end the scene on a movement (a hand reaching, a door closing, a step) and open the next one on exactly the same movement, performed by the same person or someone else in another place and time.  
**Effect on the audience:** The eye follows the movement and never registers the cut, so a huge jump in time and place passes effortlessly. The energy does not break.  
**Used for and where it works best:** The single best tool for shortening a film: airport to hotel, a boy running to a man running. It belongs at the top of a new chapter and inside travel montages. For AI generation, design the out frame and the in frame with the same subject position, direction and speed, and the cut disappears.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Trailer / Teaser, Music Video, Commercial / TVC, Anime (Japanese 2D), 3D CG Animation, AI-Generated Clip | genres: Drama, Action, Adventure, Historical / Biopic, Heritage (civilisation-focused), Coming of Age, Road Movie, Sports Drama  
**Avoid when:** If the two movements do not share direction and speed it reads as a mistake, not a device. And avoid it when you want the audience to feel a break or a loss.  
**Prompt:** `cut on the identical gesture, same screen position and direction, from the first location to the second, continuous motion across the cut`  
**Yields to:** `scene.life_to_death` — You want a break or a loss felt.  
`scene.same_action_new_place`

### Parallel Lives

**Also called:** parallel action match, the other one doing the same  
**What it is:** You move from one character to another performing the same act in completely different circumstances: one dines at a full table, the other on dry bread; one sees his son off, the other buries his.  
**Effect on the audience:** The comparison becomes a judgement with no dialogue. The viewer builds the meaning from the likeness and the gap, and believes it more than any line could make them.  
**Used for and where it works best:** When the film runs two storylines in two different lives, and in social and heritage documentary when you compare present with past. Design both frames at the same size and angle so the only difference is content. In a public service ad this pair is the entire message.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Short Film, Commercial / TVC, Video Essay | genres: Drama, Political Thriller, Heritage (civilisation-focused), Historical / Biopic, War, Tragedy, Melodrama, Coming of Age  
**Avoid when:** A forced likeness that serves no idea reads as editing for its own sake. And explaining the comparison in narration afterwards usually kills it, because the audience has already made the connection themselves; the exception is a teaching piece where the point has to land for a young viewer.  
**Prompt:** `cut between two characters performing the same gesture in opposite circumstances, identical framing size and angle in both shots`  
`scene.parallel_lives`

### Rich to Poor Contrast Cut

**Also called:** contrast cut, the class cut  
**What it is:** A straight cut between two socially opposed scenes: a banquet then hunger, a palace then a shack, a ringed hand then a cracked one. It plays as a hard cut with no optical transition.  
**Effect on the audience:** The editor speaks, not the characters. The viewer feels anger or shame, and the film states its position without a speech.  
**Used for and where it works best:** Political film, social documentary and charity advertising. The strongest execution keeps shot size and camera movement identical across both, so content is the only variable. In heritage work: the same ritual at the court and at the farm.  
**Best in:** formats: Feature Film, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Commercial / TVC, Short Film, Video Essay, News Report / Reportage | genres: Political Thriller, Drama, Heritage (civilisation-focused), Historical / Biopic, Tragedy, Dark Comedy / Satire, Melodrama, War  
**Avoid when:** It turns preachy fast. Used more than once in a piece the audience feels lectured. In documentary, a real person cut into the comparison reads as an accusation; put one there only where the brief's story is about them.  
**Prompt:** `hard cut between two matching frames of opposite social worlds, same shot size, same camera move, no transition effect`  
**Yields to:** AUTHORITY the brief — Real people enter the comparison only where the brief's story puts them there.  
`scene.rich_to_poor_contrast`

### Loud to Quiet

**Also called:** the level drop, dynamic cut  
**What it is:** A transition built on level rather than image: a loud scene (a party, a market, a battle) cuts to one at almost zero. The drop in level is the transition.  
**Effect on the audience:** The ear needs a second to adjust, and that second is what makes the viewer notice every detail in the new scene.  
**Used for and where it works best:** Entering an intimate or dangerous scene after a public one. Best uses: from party noise into an empty bedroom, from battle noise into the wounded man's tent. Deepen it by holding the quiet shot two seconds before the first line.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Music Video, Documentary Feature, Anime (Japanese 2D), Vertical Micro-Drama, Game Cinematic / Gameplay | genres: Drama, Thriller / Suspense, War, Romance, Crime / Procedural, Psychological / Arthouse, Tragedy, Noir / Neo-Noir  
**Avoid when:** If the quiet scene is not genuinely low the trick does not work. In short-form remember that much of the audience watches muted, so support it visually.  
**Prompt:** `editor note: cut from peak crowd noise to a near-silent interior, hold two seconds of room tone before the first line`  
**Yields to:** `scene.crowd_to_alone` — Muted viewing; carry the drop visually.  
`scene.loud_to_quiet`

### Tight to Wide (Release)

**Also called:** the opening out, release cut  
**What it is:** The first scene ends on a close or tight frame and the next opens on a very wide or aerial shot. The jump in size between the two is the whole transition.  
**Effect on the audience:** A physical opening in the chest. The viewer feels lifted out of the character's head into a world larger than them, which reads as freedom or as smallness depending on what fills the frame.  
**Used for and where it works best:** The top of a new chapter, the beat after a confession or a breakdown, and the start of a travel section. In heritage and nature documentary it is the full site wide after the macro detail. In a trailer it is where the music enters.  
**Best in:** formats: Feature Film, Trailer / Teaser, Heritage / Historical Documentary, Documentary Feature, Travel / Real Estate / Hospitality, Music Video, Drama Series Episode, Game Cinematic / Gameplay | genres: Drama, Adventure, Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Fantasy / Epic, Road Movie, War  
**Avoid when:** If the wide carries no new information (empty sky with nothing in it) it wastes screen time. And avoid it when you want the audience kept locked inside the character.  
**Prompt:** `cut from an extreme close-up straight to an aerial wide of the whole landscape, music entering on the cut frame`  
**Yields to:** `scene.wide_to_tight_focus` — Keep the audience locked inside the character.  
`scene.tight_to_wide_release`

### Wide to Tight (Focus)

**Also called:** narrowing in, the funnel cut  
**What it is:** The scene ends on a wide that explains a place or a crowd, and the next opens on a very tight frame of one face or object inside that world. The size drops in a single step.  
**Effect on the audience:** It tells the audience to forget the world, this is what matters. Attention narrows instantly and the face or object becomes the subject.  
**Used for and where it works best:** After establishing at the top of a chapter, and before a decision scene. In heritage documentary: a wide of the whole city, then a macro on a carving or a craftsman's hand. In advertising it is the "the world is big, the answer is in your hand" move.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Documentary Feature, Commercial / TVC, Product Video / Motion Design, Video Essay, Trailer / Teaser | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Mystery / Whodunit, Thriller / Suspense, Science / Educational, Crime / Procedural, Nature / Wildlife  
**Avoid when:** If the tight frame carries no information that belongs to the wide, the cut reads as random. Do not repeat it twice in one sequence or it becomes a mechanical pattern.  
**Prompt:** `cut from a wide establishing shot directly to a macro close-up of one detail inside that place, sound narrowing to a single element`  
**Yields to:** `scene.tight_to_wide_release` — The tight frame carries nothing from the wide.  
`scene.wide_to_tight_focus`

### Public to Private

**Also called:** the mask off cut, backstage cut  
**What it is:** A scene where the character is in front of people (a speech, a wedding, a meeting) cuts to the same character alone: a car, a bathroom, a back stairwell. Usually in the same clothes and the same minute.  
**Effect on the audience:** The real face is exposed. The viewer sees the gap between the performance and the truth, and becomes a keeper of the character's secret.  
**Used for and where it works best:** The strongest way to expose a character without dialogue, and a foundation of political and family drama. Keep the private scene free of music and speech: just breath and silence. In vertical micro-drama it is the beat that makes the viewer stay.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Vertical Micro-Drama, Short Film, Soap Opera / Telenovela, Documentary Feature, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Drama, Political Thriller, Melodrama, Tragedy, Legal Drama, Crime / Procedural, Coming of Age, Romance  
**Avoid when:** If there is no real gap between the public and the private self the cut gives you nothing. And do not explain the gap in voice-over; the face is enough.  
**Prompt:** `cut from a wide of him performing in front of a crowd to a tight single of the same man alone, no music, only breathing`  
**Yields to:** `scene.crowd_to_alone` — No gap between public and private self.  
`scene.public_to_private`

### Crowd to Alone

**Also called:** the isolation cut, from many to one  
**What it is:** A cut from a wide full of people, movement and sound to a single figure in an empty, silent frame. The difference is not only size but the number of bodies in the frame.  
**Effect on the audience:** Loneliness is measured by comparison. The viewer only feels the character's isolation because they just saw the crowd, so the cut itself creates the emotion.  
**Used for and where it works best:** After the wedding, after the victory, after the funeral, after any group scene. In heritage and documentary: a crowd at the site, then one man alone in the same place at another hour. In music video it is the chorus wide, then the singer alone.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Documentary Feature, Heritage / Historical Documentary, Short Film, Wedding / Event Film, Anime (Japanese 2D) | genres: Drama, Tragedy, Romance, Melodrama, Heritage (civilisation-focused), War, Coming of Age, Psychological / Arthouse  
**Avoid when:** If the single is not in the same place or the same clothes the link breaks and the cut is just a scene change. Do not add a sad cue either; the emptiness is enough.  
**Prompt:** `cut from a busy wide full of people to a locked frame of one person alone in the same location, crowd sound gone, only wind`  
`scene.crowd_to_alone`

### Arrival to Departure

**Also called:** the stay skipped, come and go cut  
**What it is:** A scene opens on someone arriving somewhere and cuts straight to the same person leaving. Everything that happened inside is removed and only the two movements remain.  
**Effect on the audience:** The viewer builds the visit in their own head from the face on the way out, and that version is usually stronger than the scene would have been.  
**Used for and where it works best:** For visits whose outcome is known or that we do not want to watch: the hospital, the prison, the parents' house, a failed job interview. Best execution: the identical frame on the way in and on the way out, only the body language changed. In drama and vertical micro-drama it is the cheapest way to delete two script pages.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Vertical Micro-Drama, Soap Opera / Telenovela, Limited Series, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature | genres: Drama, Crime / Procedural, Melodrama, Tragedy, Coming of Age, Romance, Legal Drama, Medical Drama  
**Avoid when:** If what happened inside carries information the audience does not have, the ellipsis becomes confusion rather than compression. And skip it when the face cannot carry the outcome.  
**Prompt:** `identical locked frame of the doorway, cut from him walking in to him walking out, same light, body language changed`  
`scene.arrival_to_departure`

### Before to Aftermath

**Also called:** the ellipsis, skip the event  
**What it is:** You cut from the moment before the event straight to the moment after it, and the event itself is never shown: he raises his hand, cut to the victim on the floor; a door closes, cut to morning.  
**Effect on the audience:** Imagination stages the violence or the intimacy better than any execution could. The viewer feels the weight of the outcome instead of studying the detail.  
**Used for and where it works best:** Violence you do not want to show, intimacy, surgery, the moment of death. Strongest form: let the sound of the event run over the first frame of the aftermath. In heritage and historical work it is the answer to battle scenes with no budget.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Heritage / Historical Documentary, Docudrama / Reenactment, Anime (Japanese 2D), Limited Series, Trailer / Teaser | genres: Drama, Crime / Procedural, War, Horror, Tragedy, Historical / Biopic, Heritage (civilisation-focused), Thriller / Suspense  
**Avoid when:** Used on every important event the film feels evasive. Show one of them in full at least once, so the omissions carry meaning.  
**Prompt:** `editor note: cut on the frame before impact, carry the impact sound over the first frame of the aftermath, open on the still result`  
**Yields to:** `scene.dialogue_to_fight` — Show one event in full or the film reads evasive.  
`scene.before_to_aftermath`

### Promise to Consequence

**Also called:** the ironic pay, said and done  
**What it is:** A scene ends on a promise or a reassurance ("nothing will happen", "I will come back") and the next opens on its exact opposite. The cut becomes an ironic or tragic comment.  
**Effect on the audience:** The audience understands the story is stronger than the character. In tragedy it reads as fate, in comedy as a punchline, from the same device.  
**Used for and where it works best:** Tragic drama, war film and dark comedy. The condition is that the cut lands directly on the line, with no shot in between. In comic advertising it is the whole structure in five seconds: the claim, then the disaster.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, Anime (Japanese 2D), Trailer / Teaser | genres: Tragedy, Dark Comedy / Satire, War, Drama, Comedy, Crime / Procedural, Historical / Biopic, Thriller / Suspense  
**Avoid when:** If the promise was not sincere in the first scene the irony dies, because the viewer saw it coming. Do not run the device twice in the same piece.  
**Prompt:** `editor note: cut on the final syllable of the reassuring line straight into the image that contradicts it, no beat in between`  
**Yields to:** `scene.ironic_parallel` — The promise was not sincere.  
`scene.promise_to_consequence`

### The Joke to the Tragedy

**Also called:** comedy into grief, the laugh that dies  
**What it is:** A scene ends on genuine laughter and the next opens on grief or bad news with no visual or musical cushion. The cheerful cue usually stops mid-phrase.  
**Effect on the audience:** It flips the viewer in one beat and makes them feel guilty for laughing. That guilt is what drives the loss deeper than any dramatic build could.  
**Used for and where it works best:** The midpoint of a drama, the loss beat in war and family films. The laughter has to be real and long enough for the audience to forget themselves. In series, place it as the last scene before the break.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Anime (Japanese 2D), Soap Opera / Telenovela, Vertical Micro-Drama, Trailer / Teaser | genres: Drama, Tragedy, War, Melodrama, Coming of Age, Family, Dark Comedy / Satire, Historical / Biopic  
**Avoid when:** If the laughter is staged or short the flip feels mechanical. Do not use it in pure comedy; it breaks the contract with the audience.  
**Prompt:** `editor note: cut mid-laugh, stop the music on the cut frame, open on a silent static shot of the loss`  
**Yields to:** `scene.comedy_to_serious` — Pure comedy, or thin laughter.  
`scene.joke_to_tragedy`

### The Plan to the Execution

**Also called:** heist cut, plan match  
**What it is:** One scene lays out the plan (a map, a sketch, an imagined run-through) and the next repeats the exact same frames for real. The match between the drawing and the execution is the transition.  
**Effect on the audience:** It gives the pleasure of prediction: the viewer knows what is coming and becomes an accomplice, so any deviation from the plan reads as instant tension.  
**Used for and where it works best:** Heist, spy and military films, and the preparation sequence of any operational story. The condition is the same angle and the same size between plan and execution. In heritage work: an architectural drawing, then the 3D reconstruction in the identical frame.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Explainer, Heritage / Historical Documentary, Game Cinematic / Gameplay, Commercial / TVC, 3D CG Animation | genres: Heist, Spy / Espionage, Crime / Procedural, War, Action, Thriller / Suspense, Heritage (civilisation-focused), Science / Educational  
**Avoid when:** If the plan executes exactly with no deviation the second scene is dead repetition. One thing has to go wrong.  
**Prompt:** `editor note: shoot the plan and the execution in identical angles and sizes, cut between matching frames, break the pattern on the shot that fails`  
**Yields to:** `scene.montage_the_plan` — The plan executes with no deviation.  
`scene.plan_to_execution`

### The Decision to the Result

**Also called:** choice cut, jump to outcome  
**What it is:** A scene ends on the moment of choice (a still face, an eye moving, a nod) and you cut straight to the result of that choice, hours or years later. All the execution is removed.  
**Effect on the audience:** It puts the weight on the decision rather than the action. The viewer learns that in this story the decisive moment is the moment of choosing.  
**Used for and where it works best:** The strongest cut in drama and biopic: he signs, cut to the new house; he shakes his head, cut to the uniform. In advertising it is a whole conversion structure: the choice, then the better life. In heritage: the king's decision, then the built city.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Commercial / TVC, Heritage / Historical Documentary, Docudrama / Reenactment, Trailer / Teaser | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Crime / Procedural, War, Romance, Sports Drama, Coming of Age  
**Avoid when:** If the result needs explaining before we understand its link to the decision, the cut failed. The new image has to state the connection in one frame.  
**Prompt:** `editor note: hold the face for two seconds after the decision reads, then hard cut to the wide that shows the consequence years later`  
**Yields to:** `scene.time_card` — The link needs stating; card the gap.  
`scene.decision_to_result`

### Dialogue to Fight

**Also called:** the violence cut, no warning cut  
**What it is:** A dialogue scene breaks on a hard cut to the first frame of violent movement, with no preparatory shot and no music leading in. The violence enters without asking.  
**Effect on the audience:** It makes the violence honest and frightening rather than heroic. The body tenses because it was not ready, which is exactly how real violence feels.  
**Used for and where it works best:** Crime, realist drama and war, and the beat where a family argument explodes. Deepen it by making the last line of dialogue completely ordinary rather than a threat. In vertical micro-drama it is the hook at the three second mark.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Vertical Micro-Drama, Anime (Japanese 2D), Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok), Limited Series | genres: Crime / Procedural, Drama, Action, War, Gangster, Thriller / Suspense, Martial Arts / Wuxia, Shonen Battle (anime)  
**Avoid when:** Laying tension music in front of it throws away the whole surprise. And avoid it when the scene wants the audience to enjoy the fight rather than fear it.  
**Prompt:** `hard cut from a calm two shot to a handheld frame already mid-impact, no music, full impact sound on the first frame`  
**Yields to:** `scene.set_piece_entrance` — The audience should enjoy the fight.  
`scene.dialogue_to_fight`

### Dialogue to Chase

**Also called:** pre-lap into action, sound pulls first  
**What it is:** The sound of the chase (engines, running feet, sirens) enters over the last second of the dialogue scene, then the picture cuts. Sound arrives before image.  
**Effect on the audience:** It pulls the viewer forward instead of pushing them. The eye is still in the conversation while the ear has already left, which creates tension before the cut.  
**Used for and where it works best:** Every move from static to kinetic in spy, action and crime. Correct length is half a second to a second and a half of pre-lap. In a trailer it is the device that lifts the whole second section.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Short Film, Anime (Japanese 2D), Game Cinematic / Gameplay, Commercial / TVC, Limited Series | genres: Action, Spy / Espionage, Crime / Procedural, Thriller / Suspense, Heist, Martial Arts / Wuxia, Adventure, Shonen Battle (anime)  
**Avoid when:** Pre-lap longer than two seconds kills the first scene and makes the audience impatient. And do not use it when you want surprise; the pre-lap removes it.  
**Prompt:** `editor note: bring the chase sound up over the last 30 frames of the dialogue, then cut to the moving camera already at speed`  
**Source:** assumption — the package's working figure, not a published standard; set the pre-lap length on the timeline in the edit.  
**Yields to:** `scene.calm_to_chaos` — You want surprise; pre-lap removes it.  
`scene.dialogue_to_chase`

### Training to Performance

**Also called:** rehearsal to real, the proof cut  
**What it is:** You end the training scene on a movement and open the real performance on that identical movement: same angle, same size, different clothes and location.  
**Effect on the audience:** Growth becomes visible in a single frame with no line of dialogue. The viewer compares automatically and feels either pride or dread depending on the outcome.  
**Used for and where it works best:** Sports, music, military and martial arts drama. Strongest execution keeps the training sound (the coach counting, the metronome) running over the first second of the performance. In sports anime it is the standard episode transition.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Anime (Japanese 2D), Music Video, Commercial / TVC, Sports Broadcast / Sports Film, 3D CG Animation | genres: Sports Drama, Martial Arts / Wuxia, Musical, War, Drama, Sports Anime, Shonen Battle (anime), Coming of Age  
**Avoid when:** If the performance always succeeds after the training it plays as predictable. Sometimes let the match land on a failure; it hits harder.  
**Prompt:** `match cut on the identical movement, same angle and size, from the training room to the arena, training sound carrying one second over`  
`scene.training_to_performance`

### Build-Up to Reveal

**Also called:** the held breath, silence before the reveal  
**What it is:** The scene builds (a creeping camera, a rising tone), then all sound drops to nothing for half a second to two seconds, and the cut to the reveal follows. The silence is the transition.  
**Effect on the audience:** The ear snaps to the void and the coming image doubles in impact. It is the strongest free tension tool in editing.  
**Used for and where it works best:** Before the monster reveal, before the coffin opens, before the truth lands in an investigation, and before the product appears in a premium ad. The length of the silence sets the scale: half a second for shock, two seconds for awe.  
**Best in:** formats: Feature Film, Trailer / Teaser, Drama Series Episode, Short Film, Commercial / TVC, Anime (Japanese 2D), Game Cinematic / Gameplay, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Horror, Thriller / Suspense, Mystery / Whodunit, Sci-Fi, Fantasy / Epic, Monster / Kaiju, Supernatural Horror, Crime / Procedural  
**Avoid when:** If the reveal itself is weak the silence exposes it and the moment turns awkward. Do not run it more than twice; the ear learns the pattern.  
**Prompt:** `editor note: cut all audio to zero for one second at the peak of the build, then cut to the reveal with a single low impact hit`  
**Yields to:** `scene.slow_monster_reveal` — A weak reveal should stay withheld.  
`scene.buildup_to_reveal`

### Reveal to Aftermath

**Also called:** the sit with it cut, reaction scene  
**What it is:** Straight after the reveal you move to a scene of silent faces: nobody speaks, the camera is locked or creeping slowly, and the sound of the previous scene is still bleeding over it.  
**Effect on the audience:** It gives the audience time to absorb. Without this scene the reveal passes without weight, however strong it was.  
**Used for and where it works best:** After news of a death, after the test result, after the betrayal. Run it two seconds longer than feels comfortable; that is where the feeling forms. In documentary, hold the witness's face in silence after the shocking fact.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Documentary Series, Short Film, Soap Opera / Telenovela, Anime (Japanese 2D) | genres: Drama, Tragedy, Crime / Procedural, Mystery / Whodunit, Medical Drama, True Crime, Melodrama, Legal Drama  
**Avoid when:** Filling it with dialogue or music turns it into an explanation scene and kills it. And do not attach one to every small reveal; it drags the rhythm.  
**Prompt:** `editor note: after the reveal cut to locked singles of the silent faces, carry the previous sound two seconds, hold each face past comfort`  
**Yields to:** `scene.answer_to_new_question` — Small reveals: keep moving.  
`scene.reveal_to_aftermath`

### Chase to Capture

**Also called:** the stop, rhythm break on the catch  
**What it is:** A fast chase with short cuts ends on a sudden rhythm break: a freeze frame, extreme slow motion, or one long locked shot. The speed change is what announces the resolution.  
**Effect on the audience:** The audience understands it is over before they see the detail. The body releases suddenly, and that release is the meaning of the capture.  
**Used for and where it works best:** The end of any chase in crime, action or sport. In battle anime it is the held frame after the final strike; in sports coverage it is the slow motion at the line. The rhythm before it must be genuinely fast for the break to register.  
**Best in:** formats: Feature Film, Drama Series Episode, Sports Broadcast / Sports Film, Anime (Japanese 2D), Game Cinematic / Gameplay, Trailer / Teaser, Short Film, Music Video | genres: Action, Crime / Procedural, Thriller / Suspense, Martial Arts / Wuxia, Sports Drama, Shonen Battle (anime), Western, Adventure  
**Avoid when:** The freeze frame now reads as comedic, so in serious drama use slow motion or a long hold instead. And do not break the rhythm before the chase has actually resolved.  
**Prompt:** `editor note: after the fastest cut of the chase, drop to 20 percent speed on the moment of contact and hold the frame three seconds`  
**Yields to:** `time.slow_motion` — in serious drama, where the freeze frame now reads as comedic.  
`scene.chase_to_capture`

### Life to Death

**Also called:** the empty frame, absence cut  
**What it is:** A transition that announces absence: a fade to black, a frame left running after the person has left it, or the identical frame from the previous scene now empty.  
**Effect on the audience:** Emptiness carries absence better than any body could. The eye searches the frame for the person and does not find them, and that search is the grief.  
**Used for and where it works best:** After the death of a central character, and at the close of an act in tragedy and war film. Strongest execution is the exact shot where we last saw them alive, same light, now with nobody in it. In heritage work: the same hall or courtyard, empty.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Heritage / Historical Documentary, Documentary Feature, Anime (Japanese 2D), Music Video | genres: Tragedy, Drama, War, Historical / Biopic, Heritage (civilisation-focused), Melodrama, Faith / Biblical Epic, Psychological / Arthouse  
**Avoid when:** Do not lay a sad cue over the emptiness; it turns grief into a request. And do not clip it: under six seconds it does not land.  
**Prompt:** `locked wide identical to the earlier shot, same light and staging, the person absent, hold ten seconds then fade to black`  
`scene.life_to_death`

### Tension to Comedy

**Also called:** the pressure valve, comic relief cut  
**What it is:** A scene at peak tension cuts hard into something comic or completely trivial: a man eating, a dog, an advert on a television. The surprise of the contrast is the joke.  
**Effect on the audience:** The laugh detonates because the body was clenched. It is the strongest joke in editing, because the tension itself funds it.  
**Used for and where it works best:** Dark comedy, light action and comic crime. The condition is that the cut lands at the exact peak of the tension, not after it. In short-form and meme edits it is the base structure: a serious build, then a cut to something ridiculous.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit, Short Film, Commercial / TVC, Anime (Japanese 2D) | genres: Dark Comedy / Satire, Comedy, Action, Crime / Procedural, Rom-Com, Adventure, Heist, Family  
**Avoid when:** If the tense scene carries a real loss the comedy reads as disrespect. Keep it out of tragedy and serious war film.  
**Prompt:** `editor note: cut at the exact peak frame of the tension into a static wide of something completely mundane, no music bridge`  
**Yields to:** `scene.chaos_to_silence` — The tense scene carried a real loss.  
`scene.tension_to_comedy`

### Comedy to Serious

**Also called:** the tone drop, when the music stops  
**What it is:** The reverse: the sound drops out, the music leaves, and the shot is held longer than the comic rhythm allows. The next scene opens on a still, long frame.  
**Effect on the audience:** The silence flips the mood immediately. The viewer understands the rules have changed and moves from laughing to listening without resistance.  
**Used for and where it works best:** The midpoint of a comedy drama, and the beat where the funny character is exposed. The tool: hold the shot two seconds longer and remove every music element. In sitcom it is the silent tag before the credits.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Short Film, Limited Series, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), Soap Opera / Telenovela | genres: Comedy, Dark Comedy / Satire, Drama, Rom-Com, Family, Coming of Age, Tragedy, Melodrama  
**Avoid when:** If the serious turn has no root in the character it reads as emotional blackmail. Do not flip the tone more than twice in one piece.  
**Prompt:** `editor note: strip all music, extend the outgoing shot two seconds past the comic beat, open the next scene on a long locked frame`  
`scene.comedy_to_serious`

### Scene into Montage

**Also called:** entering the sequence, music takes over  
**What it is:** A move from a normal dialogue scene into a montage: the cut lands on a music beat and the track takes over from dialogue as the driver.  
**Effect on the audience:** It changes the viewer's contract with time. From here every cut passes days rather than seconds, and the eye accepts it instantly because of the music.  
**Used for and where it works best:** The opening of every montage: training, travel, preparation, decline. Cleanest tool is to let the first note of the track arrive half a second before the cut. In music video and advertising it marks the start of the second section.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Short Film, Sports Broadcast / Sports Film, Trailer / Teaser, Anime (Japanese 2D) | genres: Sports Drama, Drama, Romance, Comedy, Musical, Action, War, Coming of Age  
**Avoid when:** Entering a montage with no audio signal makes the audience feel the story broke. And do not exit the same way; the way out should be silence or a line of dialogue.  
**Prompt:** `editor note: pre-lap the first music beat half a second, cut on the downbeat into the first montage image, drop dialogue entirely`  
`scene.scene_to_montage`

### Montage into Scene

**Also called:** leaving the montage, the landing scene, music lets go
**What it is:** The move out of a montage and back into a played scene: the track that drove the fragments releases the story, and the next image runs at real time, with dialogue and a turn. It is the far door of `scene.scene_to_montage`, and it is the join where a montage is most often lost.
**Effect on the audience:** The contract with time snaps back. Cuts stop passing days and start passing seconds again, and the first held beat reads as the consequence of everything the montage compressed - the viewer feels the story resume rather than a new one begin.
**Used for and where it works best:** The end of every montage: training, travel, preparation, decline, courtship. The package states the rule twice and this card joins the two statements. The way out is silence or a line of dialogue, never the music's next downbeat - that is how `scene.scene_to_montage` says it. And the scene you land in is the montage's climax, a real scene with dialogue and a turn - that is how `seq.montage_sequence` says it. The cleanest execution lets the track resolve and die on the last fragment, holds one beat of room tone, and cuts into the first line played at real time; the alternative is a line of dialogue that arrives over the last fragment and carries the cut. Write the landing scene first: if it has no turn, no exit will save the montage.
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Commercial / TVC, Short Film, Sports Broadcast / Sports Film, Trailer / Teaser, Anime (Japanese 2D) | genres: Sports Drama, Drama, Romance, Comedy, Musical, Action, War, Coming of Age
**Avoid when:** Leaving on the music's downbeat, the same way you came in - the audience reads the landing scene as one more fragment, and the montage ends on nothing. And do not land on a scene with no turn: the fragments were the setup, and a landing that does not pay them off tells the viewer the compressed time was wasted.
**Prompt:** `editor note: let the track resolve and die on the last montage image, hold one beat of room tone, then cut into the first line of the scene played at real time`
**Yields to:** `seq.montage_sequence` — The problem is the run, not the join: the fragments carry no question and no climax, so there is nothing for the landing scene to pay off.
`scene.montage_to_scene`

### Storyline Handoff

**Also called:** A story to B story, thread switch  
**What it is:** Moving from one character's thread to another using a visual link: a graphic likeness in the frame, the same movement, or the same object. The link hides the switch.  
**Effect on the audience:** The brain accepts the switch without protest because it saw visual continuity. Without the link the viewer feels torn away from the character they were with.  
**Used for and where it works best:** Every multi-thread piece: drama series, ensemble features, multi-character documentary. The easiest tool is the same shot size and the same direction of movement across the cut. In documentary: the same shot type from one witness to the next.  
**Best in:** formats: Drama Series Episode, Limited Series, Feature Film, Documentary Series, Documentary Feature, Soap Opera / Telenovela, Anime (Japanese 2D), Video Essay | genres: Drama, Crime / Procedural, Political Thriller, Mystery / Whodunit, Historical / Biopic, Melodrama, War, Seinen (mature anime)  
**Avoid when:** Do not switch threads at a peak of tension in the first one unless you intend to torment the audience. And without a visual link the switch reads as random.  
**Prompt:** `editor note: cut between the two threads on a matching shape or matching movement, identical frame size and screen direction`  
**Yields to:** `scene.pov_handoff` — No visual link between the threads.  
`scene.storyline_handoff`

### The POV Handoff

**Also called:** perspective handoff, whose scene is it  
**What it is:** A scene ends inside one character's point of view and the next opens inside the point of view of another character who was present in the first. The handoff point is a reaction shot of that second character at the tail of the scene.  
**Effect on the audience:** The viewer moves between minds without confusion, and learns that in this story the truth changes with who is watching.  
**Used for and where it works best:** Multi-voice drama, and mysteries where the same event replays through different eyes. The condition is that the last shot of the first scene belongs to the incoming character's eyes. In anime and series it is the doorway into an episode focused on a supporting character.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Anime (Japanese 2D), Short Film, Documentary Feature, Game Cinematic / Gameplay, Video Essay | genres: Drama, Mystery / Whodunit, Crime / Procedural, Psychological / Arthouse, Seinen (mature anime), Historical / Biopic, Thriller / Suspense, Tragedy  
**Avoid when:** If the incoming character was not planted visually in the first scene the move reads as a break in the narration. And do not switch perspective more than twice inside one act.  
**Prompt:** `editor note: end the scene on a reaction close-up of the incoming character, then open the next scene on what only they can see`  
**Yields to:** `scene.storyline_handoff` — The incoming character was never planted.  
`scene.pov_handoff`

### The Object Handoff

**Also called:** object baton, prop as bridge  
**What it is:** A single object travels from scene to scene and becomes the link: a letter, a ring, a gun, a photograph. The scene ends on the object and the next opens on it in someone else's hand or in another place. It differs from the staging Object Handoff, where the object passes from hand to hand inside one shot.  
**Effect on the audience:** It creates the feeling of a causal chain: every scene is the result of the one before. And the object accumulates meaning with each handoff.  
**Used for and where it works best:** Crime, heritage, letters and inheritance stories. In heritage work: a clay tablet or a piece of jewellery passing between eras in the identical frame. In advertising: the product moving between different people's hands. Keep angle and size identical at every handoff.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Commercial / TVC, Short Film, Documentary Feature, Anime (Japanese 2D), Music Video | genres: Crime / Procedural, Heritage (civilisation-focused), Historical / Biopic, Drama, Mystery / Whodunit, Thriller / Suspense, Gangster, Fantasy / Epic  
**Avoid when:** If the object's meaning does not change at each handoff it becomes a formal trick. And do not pass it more than four times or it turns into a game instead of a device.  
**Prompt:** `editor note: identical macro framing of the object in every scene, cut between hands and eras on matching angle and size`  
**Yields to:** `scene.planted_object_payoff` — The meaning of the object never changes.  
`scene.object_handoff`

### Act to Act

**Also called:** act break, chapter join  
**What it is:** A structural marker telling the audience one part is done and another has begun: a fade to black, a completely new establishing shot, or a time card. The largest transition in the piece after the ending.  
**Effect on the audience:** It gives the audience a deliberate rest and resets their expectations. Without it a long film feels like one exhausting mass.  
**Used for and where it works best:** The end of act one and act two in a feature, and the end of every section in documentary. Pick the device by charge: fade to black after a loss, a fresh establishing shot after a decision. In broadcast series it is the ad break point.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Video Essay, Soap Opera / Telenovela | genres: all  
**Avoid when:** A fade to black inside an act stops the film for no reason. And a chapter marker every ten minutes loses all meaning.  
**Prompt:** `editor note: fade to black for one full second, then open the new act on a fresh establishing wide with new light and new ambience`  
**Yields to:** `scene.prelap_join` — Inside an act: join without stopping the film.  
`scene.act_to_act`

### Opening into Titles

**Also called:** pre-title to main title, the title drop  
**What it is:** The pre-title sequence ends on a peak (a line, a hit, a reveal) and the main title and theme enter on that same frame. The cut lands on the highest point, not after it.  
**Effect on the audience:** It converts the energy of the cold open into the energy of the title, so the name of the piece becomes part of the action rather than an interruption.  
**Used for and where it works best:** A fixed convention in spy films, action films and series. The same principle drives trailers and short-form: the brand or title card enters on the strongest hit. The strongest version makes the last line of the scene the title of the piece.  
**Best in:** formats: Feature Film, Drama Series Episode, Title Sequence / Opening Credits, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Anime (Japanese 2D), Limited Series | genres: Action, Spy / Espionage, Thriller / Suspense, Crime / Procedural, Horror, Sci-Fi, Comedy, Superhero  
**Avoid when:** If the title enters after the energy has dropped it becomes a dead break. And do not hang a title on a weak cold open; hold it back.  
**Prompt:** `editor note: cut to the title card on the peak frame of the cold open, theme music entering on that same frame at full level`  
**Yields to:** `scene.title_drop` — Weak cold open; hold the title back.  
`scene.opening_to_titles`

### Titles into the First Scene

**Also called:** coming down from the titles, into the world  
**What it is:** Coming out of the title sequence into the first scene: the theme pulls back and room ambience takes its place. The transition is primarily a sound move, not a picture move.  
**Effect on the audience:** It lowers the viewer from the designed world into the real one. Without it the first scene still feels like part of the titles and the story does not start.  
**Used for and where it works best:** Any piece with a designed title sequence: film, series, anime, documentary. Best execution brings the new location's sound (a market, rain, a fan) in under the last note of the theme. In heritage documentary it is where the real site ambience arrives.  
**Best in:** formats: Title Sequence / Opening Credits, Feature Film, Drama Series Episode, Anime (Japanese 2D), Documentary Feature, Heritage / Historical Documentary, Limited Series, Documentary Series | genres: all  
**Avoid when:** A hard cut from a full theme to total silence reads as a technical fault unless the shock is intended. And do not start the first scene with critical dialogue over the tail of the music.  
**Prompt:** `editor note: fade the theme under the last title card while the new location ambience rises, first line of dialogue only after the music is gone`  
**Yields to:** `scene.credits_over_action` — No designed title block wanted.  
`scene.titles_to_first_scene`

### Climax to Denouement

**Also called:** the wind down, coming off the peak  
**What it is:** The move from the highest point of the piece into the quiet final part. The tools are a long dissolve, a crane or aerial pulling away, or a held static wide.  
**Effect on the audience:** It draws the breath out. After a climax the audience needs a gradual descent to absorb what happened, and any hard cut here feels violent.  
**Used for and where it works best:** After the final battle, after the verdict, after the big confession. In heritage and epic work the right tool is a slow aerial pulling away from the site as a calm cue enters. In series it is the last five minutes of the finale.  
**Best in:** formats: Feature Film, Limited Series, Drama Series Episode, Heritage / Historical Documentary, Documentary Feature, Short Film, Anime (Japanese 2D), Game Cinematic / Gameplay | genres: Drama, War, Historical / Biopic, Heritage (civilisation-focused), Tragedy, Fantasy / Epic, Action, Mythology / Ancient Epic  
**Avoid when:** A denouement stretched too long makes the audience feel the film does not know how to end. And do not stage a second climax after it; that cancels the first.  
**Prompt:** `slow aerial pull back from the site of the climax, camera rising and drifting away, quiet sustained score entering as the noise fades`  
**Yields to:** `scene.hard_cut_to_credits` — No descent; convert energy into credits.  
`scene.climax_to_denouement`

### Last Scene to End

**Also called:** the final hold, the last frame  
**What it is:** The final transition: the frame keeps running after the action is over, nobody moves, then black. The last silence is part of the film, not the end of it.  
**Effect on the audience:** It leaves the viewer alone with themselves. These final seconds are what they walk out with, so they are what gets remembered.  
**Used for and where it works best:** Every dramatic piece. Set the hold by genre: two seconds in comedy, five to ten in tragedy and heritage. In heritage documentary, leave the site without people and let the natural sound run all the way to black.  
**Best in:** formats: Feature Film, Short Film, Limited Series, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Anime (Japanese 2D), Experimental / Art Film | genres: Drama, Tragedy, Heritage (civilisation-focused), Historical / Biopic, Psychological / Arthouse, War, Romance, Melodrama  
**Avoid when:** Bringing the end credits music in over the hold kills it. Let the silence or the location sound reach black first.  
**Prompt:** `editor note: hold the final frame eight seconds with only natural ambience, no music, then fade to black over two seconds`  
**Yields to:** `scene.hard_cut_to_credits` — The piece should end charged, not silent.  
`scene.last_scene_to_end`

### Episode to Episode

**Also called:** the hook out, end of episode cut  
**What it is:** The episode ends on an open question rather than an answer: a door opens and we do not see who, a phone rings and we only see the name, someone walks in and the face is withheld. The cut lands one frame before the answer.  
**Effect on the audience:** The viewer cannot leave. The open question creates a mental pressure that continues after the screen goes dark.  
**Used for and where it works best:** Every series, and above all streaming where the next episode is one second away. The strongest version is a reaction shot of a character seeing something we do not see, then cut. In vertical micro-drama it is the entire episode model.  
**Best in:** formats: Drama Series Episode, Limited Series, Soap Opera / Telenovela, Vertical Micro-Drama, Documentary Series, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit | genres: Mystery / Whodunit, Crime / Procedural, Thriller / Suspense, Drama, True Crime, Political Thriller, Horror, Shonen Battle (anime)  
**Avoid when:** If every episode ends on the same kind of cliffhanger the audience adapts and feels manipulated. Alternate: sometimes a question, sometimes a loss, sometimes silence.  
**Prompt:** `editor note: end on a reaction close-up of the character seeing something offscreen, cut to black one frame before the reverse`  
**Yields to:** `scene.life_to_death` — Alternate: sometimes a loss, not a question.  
`scene.episode_to_episode`

### Cold Open

**Also called:** teaser scene, pre-title sequence  
**What it is:** A complete scene at the top of the piece before the titles, often not tied directly to the main plot: a murder, an accident, a minor character. It ends on a peak and the title follows.  
**Effect on the audience:** It grabs the viewer before they decide to leave, and plants a puzzle that keeps working in the background through the first half.  
**Used for and where it works best:** A fixed convention in crime series, horror and spy films. The rule: make the scene work on its own as a short story and let its link to the plot surface later. In investigative documentary it is the incident scene, before we know anybody's name.  
**Best in:** formats: Drama Series Episode, Feature Film, Limited Series, Documentary Series, Documentary Feature, Trailer / Teaser, Anime (Japanese 2D), Soap Opera / Telenovela | genres: Crime / Procedural, Horror, Thriller / Suspense, Mystery / Whodunit, True Crime, Spy / Espionage, Action, Supernatural Horror  
**Avoid when:** If it never connects to the plot the audience feels cheated. And keep it under five minutes in a feature or it becomes a different film.  
**Prompt:** `editor note: open on a self-contained scene with no main characters, end it on its peak, hard cut to the title card`  
**Example:** Raiders of the Lost Ark, the temple sequence before the title.  
**Yields to:** `scene.teaser` — No room for a self-contained scene.  
`scene.cold_open`

### The Hook Opening

**Also called:** the grab, first three seconds  
**What it is:** The first three seconds carry the strangest or most charged image or line in the whole piece, even if it comes from the middle. Nothing is established and nobody is introduced; the charged thing is shown immediately.  
**Effect on the audience:** It stops the scroll. The viewer does not decide to watch; they are already watching before they decide.  
**Used for and where it works best:** The law of Reels, Shorts, TikTok, trailers and ads. The forms that work: a blunt question, the result before the cause, a big movement, a face at an extreme. In vertical micro-drama: open on the scandal, not the set-up.  
**Best in:** formats: Vertical Short-Form (Reels, Shorts, TikTok), Vertical Micro-Drama, Trailer / Teaser, Commercial / TVC, Meme / Comedy Edit, Music Video, Vlog / YouTube Long-Form, Product Video / Motion Design | genres: all  
**Avoid when:** A hook unrelated to the rest loses the viewer at the six second mark and burns trust in the source. And do not rely on text alone; many watch muted and fast.  
**Prompt:** `open on the single most extreme frame of the piece, subject already mid-action, no establishing shot, big clear motion in the first second`  
**Yields to:** `scene.in_medias_res` — The hook must come from the story.  
`scene.hook_opening`

### In Medias Res

**Also called:** start in the middle, flash-forward opening  
**What it is:** The piece opens at an advanced point in the story (the chase is running, the trial has begun) and then jumps back to explain how we got there, sometimes with a card that returns us months earlier.  
**Effect on the audience:** It gives the audience a promise: you saw where this is going, now see why. Every later scene is then read in the light of that future.  
**Used for and where it works best:** Crime, heist, biopic and courtroom drama. Choose a moment that carries a clear question, not just action. In documentary: open on the collapse, then go back to the years of building.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Documentary Series, Short Film, Trailer / Teaser, Video Essay | genres: Crime / Procedural, Heist, Thriller / Suspense, Drama, Historical / Biopic, True Crime, Noir / Neo-Noir, Legal Drama  
**Avoid when:** If the chosen moment burns an important twist you lose the ending. And do not stay in the past longer than a third of the piece without returning to that opening point.  
**Prompt:** `editor note: open mid-action at the highest tension point of act three, then cut to a time card taking us back and restart the story`  
**Yields to:** `scene.teaser` — The chosen moment would burn a twist.  
`scene.in_medias_res`

### The Teaser

**Also called:** the pre-credits tease, opening tease  
**What it is:** A very short piece at the top showing a fragment of a coming scene with no context: a sound, a hand, an ambiguous frame. Shorter than a cold open and it does not complete a story.  
**Effect on the audience:** It plants unease without information. The viewer carries an image they cannot place and waits for it the whole time.  
**Used for and where it works best:** Horror, mystery and series television, where it holds the viewer in the first seconds before they change channel. In heritage documentary: a shot of an unexplained artefact before we learn what it is.  
**Best in:** formats: Drama Series Episode, Trailer / Teaser, Feature Film, Short Film, Documentary Series, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D) | genres: Horror, Mystery / Whodunit, Thriller / Suspense, Supernatural Horror, Crime / Procedural, Sci-Fi, Heritage (civilisation-focused), True Crime  
**Avoid when:** If you never return to the ambiguous image the audience feels you forgot it. And do not stretch it; it becomes a weak cold open.  
**Prompt:** `editor note: cut a six second fragment from a later scene, remove all context, end on the most ambiguous frame and go straight to black`  
**Yields to:** `scene.cold_open` — Stretched, it is a weak cold open.  
`scene.teaser`

### The Establishing Opening

**Also called:** classic establisher, wide open  
**What it is:** The piece opens on a very wide shot that explains the world: a city, a desert, a river, a galaxy. From there we descend gradually to the location, then to the character.  
**Effect on the audience:** It gives safety and context. The viewer knows where they are before they care who, so they enter calmly instead of scrambling.  
**Used for and where it works best:** Epic, historical, heritage, western and nature work, and any world unfamiliar to the audience. In heritage documentary it is the most important shot in the film: the land before any king is named. In travel and real estate it is the default opening.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Travel / Real Estate / Hospitality, Drama Series Episode, Game Cinematic / Gameplay, 3D CG Animation, Documentary Series | genres: Historical / Biopic, Heritage (civilisation-focused), Western, Fantasy / Epic, Nature / Wildlife, Mythology / Ancient Epic, War, Adventure  
**Avoid when:** In vertical short-form this is a dead opening; the thumb moves before the shot ends. And skip it when the world is entirely familiar; it wastes screen time.  
**Prompt:** `extreme wide aerial establishing shot of the landscape at first light, slow forward drift, then cut progressively closer to the location`  
**Yields to:** `scene.hook_opening` — Vertical: the thumb moves first.  
`scene.establishing_opening`

### The Scale Reveal Opening

**Also called:** pull-back opening, macro to epic  
**What it is:** You open on an extreme close detail that is unreadable (a weave, an eye, a grain of sand) and the camera pulls back or cuts progressively out until it turns out to be part of something vast.  
**Effect on the audience:** It creates astonishment at the reveal point. The viewer moves from curiosity to awe, and it is the best way to announce the scale of a world.  
**Used for and where it works best:** Sci-fi, epic, heritage and premium advertising. In heritage work: a macro on a single cuneiform wedge, pulling back to the whole tablet and then the whole hall. In short-form the same idea works as three cuts instead of one move.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Trailer / Teaser, Commercial / TVC, Product Video / Motion Design, 3D CG Animation, Vertical Short-Form (Reels, Shorts, TikTok), Documentary Feature | genres: Sci-Fi, Fantasy / Epic, Heritage (civilisation-focused), Historical / Biopic, Mythology / Ancient Epic, Science / Educational, Space Opera, Nature / Wildlife  
**Avoid when:** If the opening detail does not become legible at the reveal the viewer feels tricked. And do not hold the mystery longer than ten seconds.  
**Prompt:** `start on an extreme macro of an unreadable texture, slow continuous pull back revealing it is part of a colossal structure, ending on an extreme wide`  
**Yields to:** `scene.establishing_opening` — The detail will not resolve legibly.  
`scene.scale_reveal_opening`

### The Slow Monster Reveal

**Also called:** withholding the creature, delayed reveal  
**What it is:** A structure spread across the whole piece: the threat is shown in parts or by its effect (a shadow, a sound, footprints, people reacting) and the full reveal is withheld until the last third.  
**Effect on the audience:** Imagination builds a bigger creature than any design could. Every partial shot adds to the account, so when the reveal comes it is funded by an hour of waiting.  
**Used for and where it works best:** Horror, monster films, sci-fi and suspense. The tools: frame lines that crop the creature, a witness's face instead of the creature, sound with no picture. In heritage and mythology the same principle works for gods and beings.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Short Film, Limited Series | genres: Horror, Monster / Kaiju, Thriller / Suspense, Sci-Fi, Supernatural Horror, Mythology / Ancient Epic, Survival, Folk Horror  
**Avoid when:** Delaying the reveal and then delivering a weak design ruins the ending. And showing it fully in the trailer usually burns two hours of build; the exception is a franchise where the creature is already the reason people buy the ticket.  
**Prompt:** `editor note: show only the effect of the creature in act one and two, cropped limbs and witness faces, hold the full body until the last third`  
**Example:** Jaws, where the shark is mostly withheld until late in the film.  
**Yields to:** `scene.before_to_aftermath` — A weak design should never resolve.  
`scene.slow_monster_reveal`

### Photo to Live Opening

**Also called:** stills into motion, the archive wakes up  
**What it is:** The piece opens on a still image (an old photograph, a drawing, a relief) which then becomes a live scene in the identical frame: the people move, the sound arrives, the colour comes in.  
**Effect on the audience:** It tells the viewer the past is about to live in front of them. In historical and heritage documentary it is the strongest statement of intent in a single shot.  
**Used for and where it works best:** The opening of heritage, historical and biographical documentary, and any archive-driven piece. The condition is that the live frame matches the still exactly in angle, size and body positions. Bridge it with sound that starts silent and arrives as full location ambience.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Documentary Series, Docudrama / Reenactment, Video Essay, Feature Film, Title Sequence / Opening Credits, AI-Generated Clip | genres: Heritage (civilisation-focused), Historical / Biopic, War, True Crime, Drama, Political Thriller, Faith / Biblical Epic, Science / Educational  
**Avoid when:** If the match is not precise the change reads as an error. And do not use it more than twice in a film or it becomes a repeated trick.  
**Prompt:** `start on a still archive photograph, hold two seconds, then the identical framing comes alive with the same people moving, colour and ambience fading in`  
**Yields to:** `scene.prologue_other_time` — No precise still-to-live match.  
`scene.photo_to_live_opening`

### The Black Screen Sound Opening

**Also called:** sound first, audio cold open  
**What it is:** The screen stays black from five seconds to half a minute while we hear only sound: breathing, rain, a gunshot, dialogue. The first image arrives after the ear has already built a whole scene.  
**Effect on the audience:** Imagination builds a picture, so whatever image follows lands as either confirmation or surprise. At the same time every ear in the room locks on.  
**Used for and where it works best:** Horror, arthouse drama and documentary, and the start of any piece that wants the audience listening. In heritage work: wind, mud and a hammer before we see the site. In short-form use a one second version only; longer loses the viewer.  
**Best in:** formats: Feature Film, Short Film, Documentary Feature, Heritage / Historical Documentary, Experimental / Art Film, Drama Series Episode, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok) | genres: Horror, Psychological / Arthouse, Drama, War, Heritage (civilisation-focused), Psychological Horror, Mystery / Whodunit, Surreal / Absurdist  
**Avoid when:** More than twenty seconds of black and the audience starts checking their screen. On short-form platforms it counts as empty content and hurts reach.  
**Prompt:** `editor note: hold black for fifteen seconds with a full sound scene playing, then fade up on a frame that contradicts what the ear expected`  
**Yields to:** `scene.hook_opening` — Short-form reads black as empty.  
`scene.black_screen_sound_opening`

### The Title Drop

**Also called:** title card on the line, naming the film  
**What it is:** The title appears at the moment it acquires meaning: after the line it was taken from is spoken, or after the image that explains it. Sometimes in the middle of the piece rather than at the top.  
**Effect on the audience:** It makes the name part of the story rather than a label on it. The viewer gets a chill because they understood the title and saw it in the same second.  
**Used for and where it works best:** Features, trailers, short-form and ads. The strongest form makes the last line of the scene the exact title and then cuts to the card. In heritage documentary, place the title after the first shot of the site, not before it.  
**Best in:** formats: Feature Film, Trailer / Teaser, Title Sequence / Opening Credits, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Drama Series Episode, Heritage / Historical Documentary, Music Video | genres: all  
**Avoid when:** A title dropped before it has earned meaning is just a card. Usually once, because the effect depends on the line landing as a discovery; the exception is a series that returns to the same line as a motif across episodes.  
**Prompt:** `editor note: cut to the title card on the frame right after the title line is spoken, black background, sound drops to a single low hit`  
**Yields to:** `scene.opening_to_titles` — The title has not earned meaning yet.  
`scene.title_drop`

### Smash to Title

**Also called:** hard cut to card, title stab  
**What it is:** A violent cut from a peak of movement or sound straight to a title card on black, with a single audio stab and then silence. The scene does not end; it is severed.  
**Effect on the audience:** It stops everything in one blow. The viewer is left suspended in the unfinished movement, and the title absorbs its energy.  
**Used for and where it works best:** Trailers, horror and action, and the end of each act in a three-part trailer. In short-form and advertising the same structure works on the brand card. The condition is that the cut lands a few frames before the movement completes.  
**Best in:** formats: Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Commercial / TVC, Feature Film, Title Sequence / Opening Credits, Product Video / Motion Design, Anime (Japanese 2D), Meme / Comedy Edit | genres: Horror, Action, Thriller / Suspense, Superhero, Sci-Fi, Crime / Procedural, Monster / Kaiju, Shonen Battle (anime)  
**Avoid when:** More than three times in one trailer and it numbs. And keep it out of quiet work, where it reads loud and cheap.  
**Prompt:** `editor note: cut mid-movement to a black title card with one low impact hit, then two frames of total silence before the next shot`  
**Yields to:** `scene.title_drop` — Quiet work; a stab reads cheap.  
`scene.smash_to_title`

### The Prologue in Another Time

**Also called:** historical prologue, the ancient opening  
**What it is:** The piece opens on a complete scene in a completely different era (centuries earlier, or in the future), then a time and place card moves us to the present. The prologue explains the rule of the world, not the plot.  
**Effect on the audience:** It gives depth and myth. The viewer reads the entire present as the consequence of something that started long ago, which gives the story historical weight.  
**Used for and where it works best:** Fantasy, folk horror, sci-fi and heritage work. Run the prologue long enough to be a real scene rather than a summary, then cut to a clean time card. In heritage documentary it is the best structure: a scene from the civilisation, then a return to the site today.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Drama Series Episode, Docudrama / Reenactment, Game Cinematic / Gameplay, 3D CG Animation, Anime (Japanese 2D), Limited Series | genres: Fantasy / Epic, Folk Horror, Sci-Fi, Heritage (civilisation-focused), Mythology / Ancient Epic, Historical / Biopic, Supernatural Horror, Faith / Biblical Epic  
**Avoid when:** If the prologue does not connect clearly to the present within the first third the audience forgets it. And do not stuff it with long narration; let the images do the work.  
**Prompt:** `editor note: open on a fully staged scene set centuries earlier, end it on an unresolved image, cut to a clean location and year card in the present`  
**Yields to:** `scene.cold_open` — The connection will not land early.  
`scene.prologue_other_time`

### The Previously On Recap

**Also called:** recap, the catch-up  
**What it is:** A fast cut of shots from earlier episodes before the episode starts, selected to remind the audience only of what matters in this one. It runs from twenty seconds to a minute.  
**Effect on the audience:** It raises comprehension without explanation inside the episode, but it also gives the game away: anything in the recap will be used today.  
**Used for and where it works best:** Every multi-episode series, especially crime and mystery. A useful trick: include at least one shot from a much older episode so today's intentions are less obvious. In documentary series it recaps the investigative thread.  
**Best in:** formats: Drama Series Episode, Limited Series, Soap Opera / Telenovela, Documentary Series, Anime (Japanese 2D), Vertical Micro-Drama, Docudrama / Reenactment, Meme / Comedy Edit | genres: Crime / Procedural, Mystery / Whodunit, Drama, Thriller / Suspense, Political Thriller, True Crime, Melodrama, Seinen (mature anime)  
**Avoid when:** A recap shot that is never used breaks the promise. And a recap that includes everything burns the twist before the episode starts.  
**Prompt:** `editor note: cut a forty second recap of only the beats this episode will pay, fast dissolves between clips, narrator or original dialogue over`  
**Example:** Lost, whose "Previously on Lost" recaps opened most episodes.  
`scene.previously_on`

### The Opening Image the Ending Answers

**Also called:** opening image and final image, the frame pair  
**What it is:** The first image of the piece is designed as a visual question and the last image answers it: the same place, object or composition, with one essential thing changed.  
**Effect on the audience:** It delivers the sense of completion. The audience does not analyse it; they simply feel the piece closed properly, and that feeling is what makes the ending hold.  
**Used for and where it works best:** Design it in the script, not in the edit. Practical pairs: an empty chair at the start and a filled one at the end, a closed door then an open one, a dry field then an irrigated one. In heritage work: a ruined site first, the reconstruction last.  
**Best in:** formats: Feature Film, Short Film, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Music Video, Commercial / TVC, Limited Series | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Tragedy, Romance, Coming of Age, Faith / Biblical Epic, War  
**Avoid when:** If the two images are identical with nothing changed, the ending states that nothing changed, which is a different meaning. Do not do it by accident.  
**Prompt:** `editor note: shoot the first and last shot with the same lens, angle and staging, change only the one element that carries the story`  
`scene.opening_image_answered`

### Establish Then Cover

**Also called:** establishing shot first, wide to coverage  
**What it is:** Every new scene opens with a shot that explains the space and the relationships (who is where, who is near whom) and only then moves into closer coverage. That first shot builds a map in the viewer's head.  
**Effect on the audience:** The audience settles geographically and is free to follow the emotion. Without it the mind keeps working in the background on where everyone is instead of listening.  
**Used for and where it works best:** Every scene with more than two people, every fight or chase, and every new location. In heritage documentary it is the wide of the site before any detail. In sitcom it is the fixed exterior before each scene.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Documentary Feature, Heritage / Historical Documentary, Short Film, Anime (Japanese 2D), Soap Opera / Telenovela | genres: all  
**Avoid when:** If the space is already known from an earlier scene the establisher is slow and redundant. In short-form it eats half your running time for nothing.  
**Prompt:** `open the scene on a wide that shows every character's position relative to each other, hold two seconds, then cut into coverage`  
**Yields to:** `scene.enter_late_leave_early` — Space known, or format short.  
`scene.establish_then_cover`

### Master to Coverage Rhythm

**Also called:** wide close wide, the coverage arc  
**What it is:** The classic scene structure: start wide, tighten progressively as the dialogue escalates, and return wide at the end or at the moment something breaks.  
**Effect on the audience:** Shot size becomes a thermometer. The audience feels the escalation physically even without noticing that the frame tightened.  
**Used for and where it works best:** Every dialogue scene in drama and series, and every interrogation, argument and confession. The working rule: each exchange tightens the frame by one step only, and you go back wide only when something actually changes.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Soap Opera / Telenovela, Short Film, Anime (Japanese 2D), Sitcom / Multi-Cam Comedy, Vertical Micro-Drama | genres: Drama, Legal Drama, Crime / Procedural, Melodrama, Political Thriller, Romance, Medical Drama, Tragedy  
**Avoid when:** Tighten too fast and you have nowhere left to go at the climax. Stay wide throughout and the audience feels no escalation.  
**Prompt:** `editor note: open on the two shot, step one size tighter every exchange, reserve the tightest single for the line that turns the scene`  
`scene.master_to_coverage_rhythm`

### Bookends

**Also called:** framing device, the outer frame  
**What it is:** A scene at the top and a scene at the end in the same place with the same character, with the whole story between them. Usually the character is remembering or telling.  
**Effect on the audience:** It gives the story a frame and a floor: the audience knows somebody survived to tell it. It also allows a reflective ending instead of an event ending.  
**Used for and where it works best:** Biopic, war, memory films and heritage documentary. In documentary: the narrator at the site at the start and again at the end, with the daylight changed. The condition is that the second scene adds meaning rather than repeating the first.  
**Best in:** formats: Feature Film, Documentary Feature, Heritage / Historical Documentary, Limited Series, Docudrama / Reenactment, Drama Series Episode, Short Film, Video Essay | genres: War, Historical / Biopic, Heritage (civilisation-focused), Drama, Tragedy, Faith / Biblical Epic, Coming of Age, Melodrama  
**Avoid when:** A framing device that tells the audience the hero survived drains the tension from every dangerous scene. And a bracket you open and do not close usually reads as a lost thread; the exception is when the missing return is the unease you want the viewer to leave with.  
**Prompt:** `editor note: shoot the first and last scene in the same location with the same blocking, change only the light and the character's state`  
**Example:** Saving Private Ryan, which opens and closes at the cemetery.  
**Yields to:** `scene.return_to_opening_image` — A framing narrator reveals who survived.  
`scene.bookends`

### Mirror Scene / Echo Scene

**Also called:** echo scene, rhyming scene  
**What it is:** A scene that repeats in the same place, the same composition and almost the same dialogue at a different point in the story, with one essential thing reversed: who speaks, who sits, who is missing. It differs from the staging Mirror Scene, where an actor and his reflection share the frame in a real mirror: here there is no mirror, it is the scene itself that returns.  
**Effect on the audience:** Change becomes visible without explanation. The viewer compares automatically and feels the distance the character has travelled.  
**Used for and where it works best:** The midpoint and the end of any character-driven drama, and family, prison and war films. The technical condition is the same lens, angle and lighting both times, so content is the only variable.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Anime (Japanese 2D), Soap Opera / Telenovela, Documentary Feature, Vertical Micro-Drama | genres: Drama, Tragedy, War, Crime / Procedural, Coming of Age, Melodrama, Family, Psychological / Arthouse  
**Avoid when:** A repeat with no change reads as an editing mistake. And if the difference is too large the mirror breaks and no comparison happens.  
**Prompt:** `editor note: reshoot the earlier scene with identical lens, angle, lighting and blocking, change one element only and let the audience find it`  
**Yields to:** `scene.callback_shot` — The scene changed too much to be recognised.  
`scene.mirror_scene`

### The Callback Shot

**Also called:** the return shot, repeated frame  
**What it is:** A specific shot seen once early in the piece returns exactly at a decisive moment: same angle, same size, same movement. The repetition is the message.  
**Effect on the audience:** The viewer remembers without knowing why, which produces a chill. The shot carries all the meaning of its first appearance and pours it onto the new moment.  
**Used for and where it works best:** Right before the ending, and at the character's decision point. In music video and advertising it is the signature frame that returns at the end. In heritage work: the same shot of the site at the start and again at the end, once we know what happened there.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Drama Series Episode, Short Film, Trailer / Teaser, Heritage / Historical Documentary, Anime (Japanese 2D) | genres: Drama, Thriller / Suspense, Tragedy, Heritage (civilisation-focused), Fantasy / Epic, Crime / Procedural, Romance, Historical / Biopic  
**Avoid when:** If the first appearance was not distinctive the callback does not register. And do not call back more than two shots in one piece or the device loses its weight.  
**Prompt:** `editor note: repeat the exact earlier frame, same lens and move, at the decision point, with the sound design changed to mark the difference`  
**Yields to:** `scene.visual_rhyme` — The first appearance was not distinctive.  
`scene.callback_shot`

### The Visual Rhyme

**Also called:** visual echo, repeated shape across the film  
**What it is:** A shape, composition or colour that recurs in distant scenes with no direct narrative link: a circle, a vertical line, a raised hand, a staircase. The repetition builds a language inside the piece.  
**Effect on the audience:** It works below awareness. The viewer does not notice it on a first watch but feels that the piece is coherent and has a personality.  
**Used for and where it works best:** Arthouse film, heritage work and music video, and anything meant to reward a second viewing. In heritage work: the ziggurat shape echoed in stairs, shoulders and compositions. In music video: a colour or geometric shape returning on every chorus.  
**Best in:** formats: Feature Film, Music Video, Heritage / Historical Documentary, Experimental / Art Film, Short Film, Anime (Japanese 2D), Title Sequence / Opening Credits, Documentary Feature | genres: Psychological / Arthouse, Heritage (civilisation-focused), Surreal / Absurdist, Drama, Historical / Biopic, Fantasy / Epic, Mythology / Ancient Epic, Tragedy  
**Avoid when:** If the rhyme becomes too obvious it turns into showing off and pulls the viewer out of the story. Keep it under the threshold of notice.  
**Prompt:** `editor note: repeat the same geometric shape or colour block in the composition of three distant scenes, never call attention to it`  
`scene.visual_rhyme`

### The Planted Object Payoff

**Also called:** the setup and payoff, the loaded prop  
**What it is:** An object is shown in an early scene casually, with no extra emphasis, and becomes decisive in a later one. The plant should sit inside an ordinary shot, not in a pointed insert.  
**Effect on the audience:** When the payoff comes the audience feels the world is logical and designed. That feeling is the difference between a plotted story and a run of coincidences.  
**Used for and where it works best:** Crime, heist, horror, comedy and heritage. The correct plant puts the object in the background or in a hand busy with something else. In heritage work: a tool or symbol shown in the daily life section that becomes the key in the final one.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Heritage / Historical Documentary, Game Cinematic / Gameplay, Anime (Japanese 2D), Limited Series, Commercial / TVC | genres: Crime / Procedural, Heist, Horror, Mystery / Whodunit, Comedy, Thriller / Suspense, Heritage (civilisation-focused), Fantasy / Epic  
**Avoid when:** A plant delivered as a pointed insert tells the audience it will be used and kills the surprise. And a plant with no payoff leaves an open question for no reason.  
**Prompt:** `editor note: place the object in the background of an unrelated wide early on, no insert, then give it its first close-up only at the payoff`  
**Yields to:** `scene.object_handoff` — The object must be seen openly.  
`scene.planted_object_payoff`

### The Set-Piece Entrance

**Also called:** entering the big sequence, the gear change  
**What it is:** The transition into the piece's big sequence (a battle, a production number, a heist): a designed establishing shot, a change in rhythm and music, and usually a large camera move announcing that the rules have changed.  
**Effect on the audience:** It gives the audience permission to enjoy. From here the piece is allowed to show off, and the viewer receives that as a promise being kept.  
**Used for and where it works best:** Before every big sequence in action, epic and musical work. The tools: an aerial pushing into the location, a door opening onto the large space, or a long single take of the preparation. In anime it is the attack announcement shot.  
**Best in:** formats: Feature Film, Anime (Japanese 2D), 3D CG Animation, Game Cinematic / Gameplay, Music Video, Drama Series Episode, Trailer / Teaser, Concert / Live Event | genres: Action, Fantasy / Epic, Musical, War, Heist, Superhero, Mythology / Ancient Epic, Shonen Battle (anime)  
**Avoid when:** If the sequence does not deliver on the promise of its entrance the disappointment is unrecoverable. And two big entrances back to back usually cancel each other, because the second has no quiet to rise out of; the exception is a comedy built on escalation.  
**Prompt:** `wide crane or aerial move descending into the location as the score enters, revealing the full scale of the space before the sequence starts`  
**Yields to:** `scene.calm_to_chaos` — No quiet to rise from.  
`scene.set_piece_entrance`

### The Repeated Shot With One Change

**Also called:** same frame one variable, controlled repeat  
**What it is:** The identical shot appears three or more times across the piece and each time exactly one element changes: a chair, a person, a colour, the light. Everything else in the frame is locked.  
**Effect on the audience:** It turns the frame into a measuring device. The audience gauges time and loss from the difference between versions instead of being told.  
**Used for and where it works best:** Films about time, family, prison and war, and heritage documentary. Execution: shoot every version on the same lens, height and distance, and lock the camera literally. In heritage work: the same site frame across four historical periods.  
**Best in:** formats: Feature Film, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Short Film, Experimental / Art Film, Video Essay, 3D CG Animation | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, War, Tragedy, Family, Coming of Age, Psychological / Arthouse  
**Avoid when:** Change more than one element and the comparison is lost; the difference becomes noise. And do not run more than four versions or it tires.  
**Prompt:** `locked identical frame repeated across the film, same lens height and distance every time, exactly one element different in each version`  
**Yields to:** `scene.same_frame_time_jump` — Only two states to compare.  
`scene.repeated_shot_one_change`

### Flashback by Dissolve

**Also called:** dissolve into the past, soft flashback entry  
**What it is:** Entering the past on a long dissolve (forty eight frames or more) from the character's face or from an object into the old scene. The dissolve says "this is inside the head" without a card.  
**Effect on the audience:** A soft, polite passage. The viewer accepts it without a jolt but also senses that the past is less solid than the present.  
**Used for and where it works best:** Emotional drama, memory and biography, and the beat where a character drifts. It suits a calm past scene rather than a violent one. In heritage documentary it is the pass from the researcher's face into the reenactment.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Docudrama / Reenactment, Soap Opera / Telenovela, Short Film, Limited Series | genres: Drama, Romance, Melodrama, Historical / Biopic, Heritage (civilisation-focused), Tragedy, War, Faith / Biblical Epic  
**Avoid when:** In thriller and horror a dissolve dilutes the tension and makes the past feel unimportant. And avoid it when the memory is traumatic; a hard cut hits harder.  
**Prompt:** `long two second dissolve from a close-up of her face into the same location decades earlier, warmer light, slower camera`  
**Yields to:** `scene.flashback_hard_cut_time_card` — in thriller and horror, where a dissolve dilutes the tension, and on a traumatic memory, where a hard cut hits harder.  
`scene.flashback_dissolve`

### Flashback by Colour Shift

**Also called:** colour coded past, warm past cool present  
**What it is:** The past lives in a different grade from the present and that grade stays consistent across the whole piece: a warm golden past against a cool blue present, or the reverse.  
**Effect on the audience:** The eye reads the timeline in a single frame with no explanation. With repetition the colour itself takes on the charge: warmth means what we lost, cool means now.  
**Used for and where it works best:** Any piece that jumps between two eras more than twice: drama, crime, war, historical documentary. The decision belongs in the grade, not on set. In heritage work: clay and copper for the past against museum grey for the present.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Heritage / Historical Documentary, Docudrama / Reenactment, Music Video, Anime (Japanese 2D) | genres: Drama, Crime / Procedural, War, Historical / Biopic, Heritage (civilisation-focused), Mystery / Whodunit, Psychological / Arthouse, Tragedy  
**Avoid when:** A grade difference that is too subtle does not reach the average viewer on a phone. Pushed too far, an obvious sepia, it reads as a nineties cliche.  
**Prompt:** `grade the flashback in warm golden tones with lifted blacks against the cool desaturated present, same lens and framing style`  
**Yields to:** `scene.flashback_ratio_change` — Grade cannot carry it on a phone.  
`scene.flashback_colour_shift`

### Flashback by Aspect Ratio Change

**Also called:** ratio shift, format change for the past  
**What it is:** The aspect ratio changes at the move into the past: a widescreen present against a squarer or narrower past. The black borders physically move on screen at the transition.  
**Effect on the audience:** The audience feels the shape change in the body before understanding it. It suggests the past is a world with different laws, not just a different time.  
**Used for and where it works best:** Pieces working across three or more eras, and arthouse and historical film. In heritage documentary: the archive's native ratio for the past against widescreen for the site today. Compose on set for it so nothing important is lost at the edges.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Limited Series, Experimental / Art Film, Video Essay, Short Film, Docudrama / Reenactment | genres: Historical / Biopic, Heritage (civilisation-focused), Drama, Psychological / Arthouse, War, Mystery / Whodunit, Surreal / Absurdist, Tragedy  
**Avoid when:** In vertical short-form a ratio change wastes half the screen and reads as a fault. And every switch must map to the rule the audience has learned - this ratio is that time; a switch outside it confuses them, however few switches there are (`look.ratio_switch`).  
**Prompt:** `change aspect ratio at the cut, present in 2.39 to 1 and the past in 1.33 to 1, borders animating in over six frames`  
**Example:** The Grand Budapest Hotel, which uses a different aspect ratio for each time period.  
**Source:** reference — checked 2026-09-23: no published cap on the number of switches exists, and the examples the two ratio cards cite both pass any small cap — *The Grand Budapest Hotel* changes ratio at least four times (Anderson: *"the different aspect ratios tell viewers where they are in the timeline"*, No Film School), and *Mommy* opens its frame twice and closes it twice (Dolan, *The Hollywood Reporter*). What they share is a rule the audience can learn.  
**Yields to:** `scene.flashback_colour_shift` — Vertical; a ratio shift reads as a fault.  
`scene.flashback_ratio_change`

### Flashback by Sound Cue

**Also called:** audio trigger flashback, the sound that opens the past  
**What it is:** A specific sound opens the past: the same song, the same bell, the same mother's voice. The sound enters over the present first and the picture follows it.  
**Effect on the audience:** It imitates real memory, where sound rather than image triggers recall. The transition therefore feels natural rather than imposed.  
**Used for and where it works best:** Psychological drama, trauma stories, war and memory films. Build it as a recurring motif: ordinary the first time, then opening the past every time after. In documentary: the witness's interview audio running over the archive image.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Docudrama / Reenactment, Heritage / Historical Documentary, Short Film, Anime (Japanese 2D), Limited Series | genres: Psychological / Arthouse, War, Drama, Psychological Horror, Historical / Biopic, Tragedy, Mystery / Whodunit, Romance  
**Avoid when:** If the sound was not planted earlier the device fails, because the ear does not recognise it. And skip the heavy echo effect; it is a worn cliche.  
**Prompt:** `editor note: bring the remembered sound up under the present scene for three seconds, then cut the picture to the past with that sound already running`  
**Yields to:** `scene.flashback_hard_cut_time_card` — Nothing was planted to trigger it.  
`scene.flashback_sound_cue`

### Flashback by Hard Cut and Time Card

**Also called:** hard cut flashback, title card jump  
**What it is:** A hard cut with no optical treatment plus a text card naming the time and place, such as a city and a year. All the clarity comes from the text, not the image.  
**Effect on the audience:** It delivers rigour and realism. The viewer does not feel they entered someone's memory; they feel the film moved them like a historian.  
**Used for and where it works best:** True crime, political, historical and documentary work, and anything crossing three or more eras. The typeface and design must stay identical on every card. In heritage work it is the cleanest way to cross a thousand years without confusion.  
**Best in:** formats: Feature Film, Limited Series, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Drama Series Episode, Docudrama / Reenactment, Video Essay | genres: True Crime, Political Thriller, Historical / Biopic, Heritage (civilisation-focused), Crime / Procedural, War, Drama, Legal Drama  
**Avoid when:** Using a card because you could not convey the time visually is an admission of directing failure. And too many cards turn the film into a slide presentation.  
**Prompt:** `hard cut with no transition, clean lower third card naming the city and the year, same typeface and position every time`  
**Yields to:** `scene.flashback_colour_shift` — Convey the era visually, not by card.  
`scene.flashback_hard_cut_time_card`

### Flashback by Desaturation

**Also called:** drained past, monochrome memory  
**What it is:** The past plays desaturated or in black and white while the present stays in colour. Sometimes a single colour is left standing inside the drained image.  
**Effect on the audience:** It states that the past is dead, or that it is a document rather than a life. If one colour is left, that colour becomes the memory itself.  
**Used for and where it works best:** War, trauma, crime and historical documentary, and anything using real archive. In heritage documentary: black and white archive against a full colour site today, or the reverse when you want the past alive and the present dead.  
**Best in:** formats: Feature Film, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Limited Series, Docudrama / Reenactment, Music Video, Video Essay | genres: War, Historical / Biopic, True Crime, Drama, Psychological / Arthouse, Heritage (civilisation-focused), Tragedy, Noir / Neo-Noir  
**Avoid when:** The single colour inside a monochrome frame has been heavily overused; only reach for it when that colour carries a specific story meaning. And full desaturation makes long scenes tiring.  
**Prompt:** `grade the past to near monochrome with only slight warmth in skin, present at full saturation, cut directly between the two`  
**Yields to:** `scene.flashback_colour_shift` — Long past scenes tire when drained.  
`scene.flashback_desaturation`

### Flash-Forward

**Also called:** flash forward, future insert  
**What it is:** A short insert from the story's future placed inside a present scene: one or two shots, with no context, usually faster or visually stranger than the rest of the piece.  
**Effect on the audience:** It creates dread rather than curiosity. The viewer has seen something coming without knowing how, so every later scene reads as a countdown.  
**Used for and where it works best:** Thriller, crime and psychological horror, and the beat where a character has a premonition. The condition: the shot must be vague enough not to burn the twist and specific enough to be recognised when it really arrives.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Trailer / Teaser, Anime (Japanese 2D), Vertical Micro-Drama, Music Video | genres: Thriller / Suspense, Crime / Procedural, Psychological Horror, Mystery / Whodunit, Sci-Fi, Drama, Supernatural Horror, Noir / Neo-Noir  
**Avoid when:** Too many of them collapse the structure and the audience loses the timeline. And do not use them to patch a scene that lacks tension of its own.  
**Prompt:** `insert a one second fragment from a later event, different texture and speed, no context, cut straight back to the present scene`  
**Yields to:** `scene.in_medias_res` — One future promise, not scattered inserts.  
`scene.flash_forward`

### The Dream Sequence

**Also called:** dream scene, oneiric sequence  
**What it is:** A full sequence running on different visual laws from the rest of the piece: a wider lens, continuous camera movement, light with no logical source, distorted or missing sound. It enters and exits on a clear marker.  
**Effect on the audience:** It gives direct access to the character's unconscious without dialogue. The viewer accepts any image however strange, because the contract has changed.  
**Used for and where it works best:** Psychological horror, surreal work, fantasy and music video. The working rule: change at least three technical elements (lens, movement, light, sound) so the difference registers without an announcement. In music video it is the licence for any visual set-piece.  
**Best in:** formats: Feature Film, Music Video, Anime (Japanese 2D), Short Film, Experimental / Art Film, Drama Series Episode, 3D CG Animation, AI-Generated Clip | genres: Psychological Horror, Surreal / Absurdist, Fantasy / Epic, Psychological / Arthouse, Horror, Sci-Fi, Supernatural Horror, Shojo (anime romance)  
**Avoid when:** A dream that changes nothing in the story is empty spectacle and breaks the rhythm. And do not use one to explain a feeling you could have delivered in a real scene.  
**Prompt:** `wide lens, continuous slow camera movement with no cuts, unmotivated coloured light, ambience replaced by a single low drone`  
**Yields to:** `scene.fantasy_insert` — The dream changes nothing in the story.  
`scene.dream_sequence`

### The Fantasy Insert

**Also called:** imagine spot, the what-if cut  
**What it is:** One or two shots showing what the character imagines rather than what happens: hitting the boss, or the other life. Then we return to reality in the identical frame.  
**Effect on the audience:** It exposes the suppressed wish in one second, and depending on the tone it either gets a laugh or hurts. The return to reality is what carries the meaning.  
**Used for and where it works best:** Comedy, rom-com, drama, anime and advertising. Technical condition: the identical frame before and after the insert so the return is unmistakable. In advertising: imagine life with the product, then come back.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Commercial / TVC, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), Short Film, Vertical Micro-Drama | genres: Comedy, Rom-Com, Dark Comedy / Satire, Drama, Family, Shojo (anime romance), Slice of Life, Coming of Age  
**Avoid when:** Returning on a different frame makes the audience unsure whether the fantasy really happened. And in serious drama too many inserts lighten the weight.  
**Prompt:** `identical locked frame before and after, one second imagined shot in between with slightly brighter grade, hard cut both ways`  
**Yields to:** `scene.dream_sequence` — Serious drama; inserts lighten the weight.  
`scene.fantasy_insert`

### The Memory Pop

**Also called:** memory flash, intrusive flashback  
**What it is:** A very short flash, four to twelve frames, of the past breaking into the present scene without warning, repeating as the reveal approaches. Sometimes silent, sometimes sound only.  
**Effect on the audience:** It imitates intrusive memory after trauma. The viewer feels the character does not control their own head, and sympathises without explanation.  
**Used for and where it works best:** Trauma drama, war, crime and psychological horror, and the beat where the character nears the truth. The structure that works: the flash is illegible the first time and gets a little longer each time until it plays in full at the end.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Anime (Japanese 2D), Trailer / Teaser, Music Video, Vertical Micro-Drama | genres: Psychological / Arthouse, War, Psychological Horror, Crime / Procedural, Thriller / Suspense, Drama, Mystery / Whodunit, Tragedy  
**Avoid when:** A flash that is legible the first time throws away the whole reveal structure. And do not repeat it more than four times or it becomes a tic.  
**Prompt:** `editor note: cut in a six frame fragment of the past with a single sharp sound hit, no fade, straight back to the present frame`  
**Yields to:** `scene.flashback_dissolve` — The memory should be legible at once.  
`scene.memory_pop`

### The Time Card

**Also called:** title card, day card, chyron  
**What it is:** Text on screen naming the day, the hour or the place between two scenes: "three years later", a weekday, a clock time. It plays on black or over the shot.  
**Effect on the audience:** It cuts time precisely and gives the feel of a report or a case file. Repeated systematically it builds a counting rhythm that creates tension by itself.  
**Used for and where it works best:** True crime, thriller, horror and documentary, and any piece running on a countdown. Strongest use: let the intervals shrink as the climax approaches. In horror a day card creates the feeling of confinement.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Feature, Documentary Series, Heritage / Historical Documentary, News Report / Reportage, Video Essay | genres: True Crime, Thriller / Suspense, Horror, Crime / Procedural, Political Thriller, Historical / Biopic, Legal Drama, War  
**Avoid when:** If the shot itself explains the time the card is redundant and signals you do not trust the audience. And decorative cards damage a documentary's credibility.  
**Prompt:** `plain white text card on black naming the day and hour, one second hold, same typeface size and position every time`  
**Example:** The Shining, which marks its sections with day and time cards.  
**Yields to:** `scene.same_frame_time_jump` — The shot already explains the time.  
`scene.time_card`

### Chapter Cards

**Also called:** chapter titles, part cards, named sections  
**What it is:** The piece is divided into named chapters by designed cards, each giving a title to the section ahead. The typography and design are part of the work's identity.  
**Effect on the audience:** It gives the feel of a book and the authority of a narrator. The audience accepts large jumps in time and place because they understand a new chapter has started.  
**Used for and where it works best:** Multi-strand and stylised features, heritage and explanatory documentary, and limited series. In heritage work: one chapter per city or per king. Its practical advantage is that it lets you reorder time without losing the audience.  
**Best in:** formats: Feature Film, Limited Series, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Video Essay, Drama Series Episode, Short Film | genres: Crime / Procedural, Dark Comedy / Satire, Historical / Biopic, Heritage (civilisation-focused), Drama, Science / Educational, Mystery / Whodunit, Gangster  
**Avoid when:** Titles that add nothing ("Part One, Part Two") are decoration. And on a simple linear piece they feel affected.  
**Prompt:** `designed full screen chapter card with a named title, held two seconds with a music sting, same design system throughout`  
**Example:** Pulp Fiction and Kill Bill, which divide the story into named chapters.  
**Yields to:** `scene.location_as_chapter` — Linear piece; divide by place.  
`scene.chapter_cards`

### Colour as Chapter

**Also called:** colour coded acts, palette per section  
**What it is:** Each act has its own palette, held for the whole act and changed at the boundary: a green act, a red act, a grey act. The change happens only at section borders.  
**Effect on the audience:** The audience feels the transition without a card and without a word. Over time the colour itself carries the psychological state of the whole section.  
**Used for and where it works best:** Arthouse film, music video, horror and fantasy, and heritage documentary where each section is a different civilisation. The decision belongs in design: sets, wardrobe and lighting before the grade, not after.  
**Best in:** formats: Feature Film, Music Video, Heritage / Historical Documentary, Limited Series, Experimental / Art Film, Anime (Japanese 2D), Short Film, Title Sequence / Opening Credits | genres: Psychological / Arthouse, Horror, Fantasy / Epic, Heritage (civilisation-focused), Surreal / Absurdist, Drama, Historical / Biopic, Mythology / Ancient Epic  
**Avoid when:** Relying on the grade alone makes the colours feel artificial and ruins skin tones. And changing mid-act destroys the whole system.  
**Prompt:** `build each act around one dominant colour in set, wardrobe and practical lighting, switch the palette only at the act boundary`  
**Yields to:** `scene.chapter_cards` — No design control over the palette.  
`scene.colour_as_chapter`

### Location as Chapter

**Also called:** place structure, one place per act  
**What it is:** The piece is divided by place rather than time: each act sits in one location, and moving between acts is moving between places. Each new location announces itself with a full establishing shot.  
**Effect on the audience:** It gives total clarity with no cards. The viewer ties each stage of the story to a place, which makes it easier to remember.  
**Used for and where it works best:** Road movies, journey films, war and heritage and travel documentary. In heritage work: one act per site with an aerial opening each. In documentary series it is the clearest structure for interrupted viewing.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Documentary Series, Travel / Real Estate / Hospitality, Drama Series Episode, Limited Series, Game Cinematic / Gameplay | genres: Road Movie, Adventure, War, Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Drama, Survival  
**Avoid when:** Returning to an earlier location without a dramatic reason breaks the system and costs you the clarity. And do not build an act around a place where nothing in the story changes.  
**Prompt:** `open every act with a distinct aerial establishing shot of the new location, same shot grammar each time, no time cards`  
**Yields to:** `scene.chapter_cards` — The story returns to earlier places.  
`scene.location_as_chapter`

### Same Frame, Time Jump

**Also called:** same angle different time, time skip in place  
**What it is:** One scene ends and the next begins on the identical camera angle and size, with only the light, the clothes and the objects changed. The camera did not move and time passed.  
**Effect on the audience:** The comparison does all the work. The audience measures the elapsed time from the difference between the two frames rather than being told.  
**Used for and where it works best:** Passing a day, a season or years, and scenes of waiting, illness and imprisonment. In heritage work: the same site frame in summer and in winter, or during excavation and after restoration. In advertising: the same room before and after the product.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Commercial / TVC, Short Film, Travel / Real Estate / Hospitality, Experimental / Art Film | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Medical Drama, Family, Tragedy, Nature / Wildlife, Coming of Age  
**Avoid when:** If the difference between the two frames is too small the audience misses that time passed. And do not move the camera even a centimetre; the match is the whole device.  
**Prompt:** `locked identical frame, cut between two times of day with completely different light and dressing, no camera move in either`  
**Yields to:** `scene.time_card` — The visual difference is too small.  
`scene.same_frame_time_jump`

### Seasons and Aging Transition

**Also called:** seasonal montage, aging transition  
**What it is:** Years pass through a change in nature or in the body: a tree greening and bare, hair going grey, a child growing. The join is a cut or a dissolve on that same element.  
**Effect on the audience:** It delivers inevitability. The audience feels that time is stronger than the characters, which is itself a subject.  
**Used for and where it works best:** Family sagas, biopics, heritage documentary and coming of age stories. Practical tool: hold one element constant (the tree, the door, the river) and change everything around it. In heritage work: the same river across four civilisations.  
**Best in:** formats: Feature Film, Drama Series Episode, Heritage / Historical Documentary, Documentary Feature, Music Video, Commercial / TVC, 2D Animation (Western / Cartoon), 3D CG Animation | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Family, Coming of Age, Melodrama, Nature / Wildlife, Faith / Biblical Epic  
**Avoid when:** It is a worn convention in advertising, so the constant element must be specific rather than a generic tree. And do not push more than twenty years through four shots; it reads as shallow.  
**Prompt:** `identical locked frame of the same tree across four seasons, matched dissolves between them, ambience changing with each season`  
**Yields to:** `scene.time_card` — More than twenty years to cross.  
`scene.seasons_aging_transition`

### The Walk-Past Age Change

**Also called:** pass behind the object transition, hidden cut age jump  
**What it is:** The character walks behind a pillar, a wall or a passing object, and comes out the other side years older, played by a different actor, or in different clothes and a different place.  
**Effect on the audience:** It passes a huge time jump inside one movement with no visible cut. It feels like sleight of hand, because time moved in front of the audience rather than between shots.  
**Used for and where it works best:** Family sagas, biopics, heritage work and music video. Execution: identical walking speed, screen direction and camera height in both halves, with the cut hidden in the frames where the view is blocked. For AI generation it is the cleanest way to join two clips.  
**Best in:** formats: Feature Film, Music Video, Heritage / Historical Documentary, Drama Series Episode, Short Film, AI-Generated Clip, 3D CG Animation, Commercial / TVC | genres: Drama, Historical / Biopic, Heritage (civilisation-focused), Family, Coming of Age, Fantasy / Epic, Melodrama, Mythology / Ancient Epic  
**Avoid when:** A change in walking speed or direction exposes the cut and turns it into a mistake. And do not spend it on a small time jump; the effort outweighs the gain.  
**Prompt:** `tracking shot following him at constant speed, he passes behind a thick pillar, emerging on the other side twenty years older, same speed and direction`  
**Yields to:** `scene.same_frame_time_jump` — A small jump does not justify it.  
`scene.walk_past_pillar_age_change`

### Intellectual Montage

**Also called:** Soviet montage, dialectical montage, concept montage, idea cut, Eisenstein montage  
**What it is:** Placing shots with no narrative connection next to each other so a third meaning forms in the viewer's mind: a face then an object, a crowd then a herd, a speaker then a statue. The meaning is in neither shot; it is in the cut.  
**Effect on the audience:** It turns pictures into an argument and the editor into an essayist. The viewer's mind engages instead of the emotions and they draw the conclusion themselves, so they are more convinced than any narration line could make them.  
**Used for and where it works best:** Political documentary, video essay, public service advertising and art film. It is also the grammar of visual poetry. The theory comes from Sergei Eisenstein. In public service advertising: the factory, then the lung, and in heritage work an ancient relief, then a contemporary scene repeating the same behaviour. The condition is that both shots are clean and simple enough for the comparison to read, and that you use it once or twice in a whole piece so it keeps its weight.  
**Best in:** formats: Documentary Feature, Documentary Series, Video Essay, Experimental / Art Film, Commercial / TVC, Heritage / Historical Documentary, Short Film, Feature Film, Music Video, News Report / Reportage, Title Sequence / Opening Credits | genres: Political Thriller, Heritage (civilisation-focused), Historical / Biopic, Science / Educational, Surreal / Absurdist, War, Drama, True Crime, Psychological / Arthouse, Dystopia / Post-Apocalyptic, Tragedy  
**Avoid when:** A comparison that is too easy becomes blunt propaganda and the audience rejects it, and if the idea is not clear the cut turns into a riddle that pushes the viewer out of the film. Explaining the idea in narration afterwards usually cancels the work the cut did; the exception is an instructional piece where comprehension outranks the effect.  
**Prompt:** `editor note: cut a clean simple shot of the subject against an unrelated clean shot that carries the judgement, no narration over either`  
**Yields to:** `scene.parallel_lives` — The idea needs characters to carry it.  
`scene.montage_intellectual`

### Time-Compression Montage

**Also called:** Hollywood montage, passage of time sequence, montage as time compression  
**What it is:** Five to fifteen short shots passing weeks or years, unified by a continuous music track and one constant visual element: the same shot size, the same camera move, or the same character.  
**Effect on the audience:** It delivers progress and accumulation. The audience accepts a long passage of time in a minute because the music has become the measure.  
**Used for and where it works best:** Training and learning, building a relationship, healing, a business expanding, a reconstruction or a long journey. The condition is that each shot shows a different step rather than the same thing from another angle, and the last shot is the result, standing opposite the first — that difference is the turn, and without it the montage only passes time (`scene.montage_value_turn`). In documentary and advertising it compresses a long process such as manufacture, farming or craft into twenty seconds, and in heritage work it carries the stages of building a temple or a canal.  
**Best in:** formats: Feature Film, Drama Series Episode, Commercial / TVC, Music Video, Documentary Feature, Heritage / Historical Documentary, Short Film, 2D Animation (Western / Cartoon), Corporate / Training, Vertical Short-Form (Reels, Shorts, TikTok), Vlog / YouTube Long-Form, Trailer / Teaser | genres: Drama, Romance, Comedy, Sports Drama, Historical / Biopic, Heritage (civilisation-focused), Family, Musical, Adventure  
**Avoid when:** If the montage passes over development we needed to watch, you dodged the drama, and it does not belong at a decisive emotional beat, where the music holds the viewer at a distance. A decisive piece of information hidden inside one is usually missed, because the viewer is reading the sequence as a summary rather than a scene.  
**Prompt:** `editor note: eight shots of two seconds each showing separate stages of progress, one continuous music cue, final shot is the result`  
`scene.montage_time_compression`

### The Training Montage

**Also called:** get strong sequence, preparation montage  
**What it is:** A sequence showing capability developing through repeated shots of the same exercises with visible improvement: failing at the start, succeeding at the end. The cutting accelerates as the sequence advances.  
**Effect on the audience:** It makes the audience feel the win was earned. When the victory arrives later it feels paid for rather than given.  
**Used for and where it works best:** Sports drama, martial arts, military stories and sports anime. The tools: macro shots of hands, feet and sweat, the same frame repeated with different results, and the counting or the coach's voice unifying the sequence.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), Music Video, Commercial / TVC, Sports Broadcast / Sports Film, Short Film, 3D CG Animation | genres: Sports Drama, Martial Arts / Wuxia, War, Shonen Battle (anime), Sports Anime, Drama, Coming of Age, Action  
**Avoid when:** It is heavily overused and reads as cliche unless you find a new angle: training at something unathletic, or training that fails. And keep it under ninety seconds.  
**Prompt:** `editor note: repeat the same three exercise frames three times with visible improvement, cutting faster each pass, coach count as the through line`  
**Example:** Rocky, whose training sequences set the pattern for the form.  
**Yields to:** `scene.training_to_performance` — The montage is cliche; one match cut.  
`scene.montage_training`

### The Travel Montage

**Also called:** journey montage, getting there sequence  
**What it is:** A sequence passing a journey through shots of transport, landscapes and arrival: a train, a road, a window, a city sign. Unity comes from a consistent screen direction and from the music.  
**Effect on the audience:** It delivers distance and a change of world. The viewer arrives at the destination feeling the road was travelled without having watched it.  
**Used for and where it works best:** Road movies, adventure, travel and heritage work. The rule that makes it work: keep every movement in the same screen direction so the viewer feels progress rather than circling. In travel and hospitality content it is the content itself.  
**Best in:** formats: Feature Film, Travel / Real Estate / Hospitality, Music Video, Commercial / TVC, Documentary Feature, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok), Drama Series Episode | genres: Road Movie, Adventure, Drama, Heritage (civilisation-focused), Nature / Wildlife, Comedy, Romance, Historical / Biopic  
**Avoid when:** Mixed screen directions make the journey feel like it is going in circles. And do not repeat the same shot type three times in a row.  
**Prompt:** `editor note: six travel shots all moving left to right, mix transport, landscape and window point of view, one continuous music cue`  
**Yields to:** `scene.map_line` — No consistent travel material.  
`scene.montage_travel_map`

### The Falling-in-Love Montage

**Also called:** romance montage, the happy sequence  
**What it is:** A sequence showing a relationship closing the distance through short situational shots: walking, eating, laughing, rain, hands. Usually soft camera movement, warm light and a full song.  
**Effect on the audience:** It passes weeks of intimacy in two minutes and builds attachment to the couple, and that attachment is the capital you spend on the break-up later.  
**Used for and where it works best:** Romance, rom-com, music video and advertising. The condition that keeps it out of cliche: every shot must carry a detail specific to these two people rather than any couple. In heritage and family work the same structure serves a father and son.  
**Best in:** formats: Feature Film, Music Video, Commercial / TVC, Drama Series Episode, Short Film, Anime (Japanese 2D), Vertical Short-Form (Reels, Shorts, TikTok), Soap Opera / Telenovela | genres: Romance, Rom-Com, Drama, Melodrama, Musical, Coming of Age, Shojo (anime romance), Family  
**Avoid when:** Rain, ice cream and the bicycle are exhausted cliches with no meaning left. And if the entire relationship lives in the montage we never see a real scene between them, so we do not believe it.  
**Prompt:** `editor note: eight intimate two second shots, each carrying a detail unique to these two people, one song running unbroken underneath`  
**Yields to:** `scene.two_hander` — The relationship needs one real scene.  
`scene.montage_falling_in_love`

### The Getting-Ready Montage

**Also called:** suit up sequence, preparation cut  
**What it is:** A sequence of close shots on the details of preparation: a button fastening, a belt tightening, a weapon assembling, makeup, shoes. Usually with no dialogue and a steady accelerating rhythm.  
**Effect on the audience:** It builds anticipation. The audience does not see the event, only the readying for it, so they imagine it and tense up before it starts.  
**Used for and where it works best:** Heist, action, sport, fashion and advertising, and the pre-battle beat. In heritage work: an Assyrian warrior or a priest being prepared for the rite. The tool: a locked macro on each detail at a constant rhythm, with every action's sound clean and loud.  
**Best in:** formats: Feature Film, Commercial / TVC, Fashion Film, Music Video, Trailer / Teaser, Anime (Japanese 2D), Sports Broadcast / Sports Film, Heritage / Historical Documentary | genres: Heist, Action, Sports Drama, War, Martial Arts / Wuxia, Spy / Espionage, Heritage (civilisation-focused), Superhero  
**Avoid when:** If the event we prepared for does not actually follow, the sequence is a broken promise. And do not repeat it twice in one film; the anticipation burns out.  
**Prompt:** `editor note: eight locked macro shots of preparation details on a steady beat, no dialogue, each action sound crisp and loud`  
`scene.montage_getting_ready`

### The Plan Montage

**Also called:** heist briefing sequence, how we do it  
**What it is:** A sequence that stages the plan visually over the character's voice explaining it: we see the steps executed in clean shots while the voice describes them. Sometimes with drawings or a model.  
**Effect on the audience:** It explains complicated information fast and with pleasure instead of a long dialogue scene. The viewer feels inducted into the crew.  
**Used for and where it works best:** Heist, spy, war and explainer video. The strongest form shows the ideal plan and then lets one element fail in execution so everything changes. In explainer and corporate work the same structure serves a process or a product.  
**Best in:** formats: Feature Film, Drama Series Episode, Explainer, Corporate / Training, Game Cinematic / Gameplay, Trailer / Teaser, Short Film, Commercial / TVC | genres: Heist, Spy / Espionage, Crime / Procedural, War, Action, Thriller / Suspense, Science / Educational, Comedy  
**Avoid when:** A plan more complicated than necessary loses the audience and the pleasure of following it. And do not explain everything: keep one piece hidden so the execution can surprise.  
**Prompt:** `editor note: clean staged shots of each step cut to the voice-over describing it, identical lighting in every step, one step deliberately withheld`  
**Yields to:** `scene.plan_to_execution` — Too complex to narrate; match the frames.  
`scene.montage_the_plan`

### The Search Montage

**Also called:** looking for it sequence, investigation montage  
**What it is:** A sequence showing a long search through repeated shots: doors knocked, pages turned, maps, faces refusing, hours passing. The repetition itself is the message: nothing found.  
**Effect on the audience:** It delivers exhaustion and persistence at once. The viewer values the discovery when it comes because they saw what the search cost.  
**Used for and where it works best:** Investigation, true crime, mystery and investigative and heritage documentary. The tool: let the last shot break the pattern (a door opening, a page stopping). In heritage work: the excavation sequence before the find.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Heritage / Historical Documentary, Limited Series, Video Essay, Game Cinematic / Gameplay | genres: Mystery / Whodunit, Crime / Procedural, True Crime, Thriller / Suspense, Heritage (civilisation-focused), Historical / Biopic, Drama, Noir / Neo-Noir  
**Avoid when:** Stretched with no escalation the audience gets as bored as the character, which is not the goal. And ending it without breaking the pattern leaves the sequence with no point.  
**Prompt:** `editor note: six repeating frames of the same search action in different places, accelerating cut, final shot breaks the pattern`  
`scene.montage_the_search`

### The Decline Montage

**Also called:** downward spiral sequence, the fall montage  
**What it is:** The inverse of the progress montage: the same repeated idea, but the result worsens with every shot. The same place, action and size, with the character visibly coming apart.  
**Effect on the audience:** The audience watches the fall without anyone announcing it. The repetition itself becomes suffocating, because each shot cancels the hope of the one before.  
**Used for and where it works best:** Addiction, illness, poverty and corruption stories, and the collapse act of a tragedy. The condition is the identical frame each time so the only variable is the person. Let the music descend rather than build.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Short Film, Documentary Feature, Music Video, Documentary Series, Anime (Japanese 2D) | genres: Tragedy, Drama, Psychological / Arthouse, Crime / Procedural, Melodrama, True Crime, Seinen (mature anime), Medical Drama  
**Avoid when:** An uplifting cue over a decline reads as accidental irony. And do not stretch it; a long decline bores rather than hurts.  
**Prompt:** `editor note: five repetitions of the identical locked frame across weeks, the subject degrading each time, score descending in pitch`  
`scene.montage_decline`

### The Aftermath Montage

**Also called:** the wreckage sequence, survey of the damage  
**What it is:** A run of still shots after a disaster, a battle or a loss: rubble, abandoned objects, faces, empty spaces. The camera is calm or locked and the sound is almost absent.  
**Effect on the audience:** It gives grief its time. The viewer measures the scale of what broke with their own eyes instead of hearing a number.  
**Used for and where it works best:** After a battle, a blast or an earthquake, and after any violent climax. In heritage documentary: shots of the site after looting or war. The rule: include at least one personal object (a toy, a shoe) rather than only general destruction.  
**Best in:** formats: Feature Film, Documentary Feature, Heritage / Historical Documentary, Documentary Series, News Report / Reportage, Drama Series Episode, Short Film, Game Cinematic / Gameplay | genres: War, Disaster, Tragedy, Drama, Heritage (civilisation-focused), Survival, Historical / Biopic, Political Thriller  
**Avoid when:** A lyrical cue over destruction aestheticises the grief, which is an ethical problem in documentary. Let the natural sound carry it.  
**Prompt:** `editor note: seven locked still shots of the damage, no camera movement, natural ambience only, one shot on a personal object`  
`scene.montage_aftermath`

### The Hands at Work Montage

**Also called:** process montage, craft sequence  
**What it is:** A macro sequence following hands at work: kneading, carving, sewing, welding, writing. The face is absent or barely seen, and the labour itself is the subject.  
**Effect on the audience:** It gives the labour dignity and creates a hypnotic pull. The viewer locks onto the detail and feels the real time of the craft.  
**Used for and where it works best:** Heritage and craft documentary, handmade product advertising and cooking content. In heritage work it is what replaces missing characters: hands throwing Assyrian pottery or pressing cuneiform. Light it from the side so texture reads.  
**Best in:** formats: Heritage / Historical Documentary, Documentary Feature, Commercial / TVC, Product Video / Motion Design, Vertical Short-Form (Reels, Shorts, TikTok), Travel / Real Estate / Hospitality, Corporate / Training, Documentary Series | genres: Heritage (civilisation-focused), Historical / Biopic, Nature / Wildlife, Science / Educational, Slice of Life, Drama, Family, Verite / Observational  
**Avoid when:** Shot at one size and angle throughout, the sequence goes flat. Alternate macro with mediums. And keep the music low; the sound of the craft matters more.  
**Prompt:** `macro shots of hands working the material, hard side light raking across the texture, shallow depth of field, craft sound in full detail`  
`scene.montage_hands_at_work`

### The Newspaper Headline Montage

**Also called:** headline spin, press montage  
**What it is:** A run of newspaper front pages or news screens passing the public arc of a story fast: a rise, a scandal, a trial. Cut quickly or with a camera move across the paper.  
**Effect on the audience:** It passes a lot of information in seconds and creates the sense that the whole world is talking. It also works as an outside viewpoint after we have been inside the character.  
**Used for and where it works best:** Biopic, true crime, political and sports stories. The modern version uses phone screens, posts and comments instead of newsprint. Every headline must be readable in half a second, so keep them short and set large.  
**Best in:** formats: Feature Film, Documentary Feature, Documentary Series, Drama Series Episode, News Report / Reportage, Video Essay, Limited Series, Trailer / Teaser | genres: True Crime, Political Thriller, Historical / Biopic, Sports Drama, Crime / Procedural, Drama, Legal Drama, Dark Comedy / Satire  
**Avoid when:** The classic spinning newspaper is a nineteen forties cliche; use it only ironically. And long headlines nobody can read mean you played empty shots.  
**Prompt:** `editor note: six front pages, each headline four words maximum in large type, quarter second holds, camera drifting slightly across each`  
`scene.montage_newspaper_headlines`

### The Line on the Map

**Also called:** travelling map line, animated route  
**What it is:** A map is shown as a shot and a line or a symbol travels across it from point to point to announce a change of place. Sometimes on an aged or hand-drawn map depending on the piece.  
**Effect on the audience:** It explains complicated geography in two seconds and delivers a sense of adventure. The viewer grasps distance and direction with no narration.  
**Used for and where it works best:** Adventure, war, historical, heritage and travel work. In heritage documentary it is a core tool: the extent of an empire, a caravan road, the course of a river. Tie it to a sound: a pen, an engine or footsteps according to the era.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Documentary Series, Travel / Real Estate / Hospitality, Explainer, Game Cinematic / Gameplay, Drama Series Episode | genres: Adventure, War, Historical / Biopic, Heritage (civilisation-focused), Science / Educational, Road Movie, Mythology / Ancient Epic, Nature / Wildlife  
**Avoid when:** A map that is not historically accurate draws expert criticism and costs the whole piece credibility. And do not spend it on a short hop; it reads as overkill.  
**Prompt:** `aged parchment map filling frame, a red line drawing itself from city to city, slight camera drift, pen scratch sound following the line`  
**Example:** Raiders of the Lost Ark, which marks travel with a line moving across a map.  
**Yields to:** `scene.montage_travel_map` — A short hop; travel shots carry it.  
`scene.map_line`

### Two-Panel Split Screen

**Also called:** De Palma split, simultaneous split screen  
**What it is:** The screen divides in two and we see two events in the same moment: one approaching, the other unaware. The two frames are composed together so the whole reads as one image.  
**Effect on the audience:** It removes the wait built into cutting. The viewer sees cause and effect in one frame, so the tension doubles and runs continuously instead of in pulses.  
**Used for and where it works best:** The run-up to a disaster in horror and thriller. Brian De Palma is the director most associated with building whole sequences on it. The condition: the screen directions inside the two panels must face each other so the eye reads a relationship rather than two pictures side by side.  
**Best in:** formats: Feature Film, Drama Series Episode, Music Video, Trailer / Teaser, Short Film, Experimental / Art Film, Game Cinematic / Gameplay, Commercial / TVC | genres: Horror, Thriller / Suspense, Crime / Procedural, Slasher, Psychological Horror, Heist, Drama, Spy / Espionage  
**Avoid when:** If the two events are not simultaneous the split is just a flourish. And in vertical it does not work side by side; stack the panels top and bottom instead.  
**Prompt:** `two panel split screen, left panel the approaching threat moving right, right panel the unaware victim facing left, both locked cameras`  
**Example:** Carrie, whose prom sequence is built on split screen.  
**Yields to:** `vertical.stacked_split` — in vertical, where side by side does not work and the panels stack.  
`scene.split_screen_depalma`

### Multi-Panel Split Screen

**Also called:** grid split, four-way split  
**What it is:** The screen divides into three or more panels, each a different thread in the same moment, and sometimes one panel expands to take the whole screen when the important beat lands.  
**Effect on the audience:** It creates the feeling of a coordinated operation under time pressure. The viewer feels like they are in an operations room watching everything and controlling nothing.  
**Used for and where it works best:** Spy, countdown, sports and concert work, and any series running on real time. In concert and live coverage it shows the whole band at once. Vary the panel sizes so it does not read as a dead grid.  
**Best in:** formats: Drama Series Episode, Feature Film, Concert / Live Event, Sports Broadcast / Sports Film, Music Video, Trailer / Teaser, Game Cinematic / Gameplay, Commercial / TVC | genres: Spy / Espionage, Thriller / Suspense, Action, Crime / Procedural, Political Thriller, Sports Drama, Musical, Heist  
**Avoid when:** More than four panels and nobody can follow. And on a small phone anything beyond two panels is lost.  
**Prompt:** `three unequal panels showing simultaneous threads, one panel growing to full screen on the key action, matched grade across all panels`  
**Example:** the television series 24, which uses multi-panel split screen throughout.  
**Yields to:** `scene.split_screen_depalma` — Phone viewing; two panels maximum.  
`scene.split_screen_multipanel`

### The Phone-Call Split Screen

**Also called:** conversation split, two sides one frame  
**What it is:** A call between two people in different places is shown on a split screen instead of intercutting. Usually both face each other inside the frame, one looking right and the other looking left.  
**Effect on the audience:** It brings the two together despite the distance, and lets the reaction land in the same instant as the line rather than waiting for a cut.  
**Used for and where it works best:** Romance, rom-com and family drama. The strongest execution gives them matching body positions or the same action (watching the same programme, reaching out). In advertising and kids content it is a playful way to show two sides.  
**Best in:** formats: Feature Film, Drama Series Episode, Sitcom / Multi-Cam Comedy, Commercial / TVC, Kids Content, Soap Opera / Telenovela, Music Video, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Romance, Rom-Com, Comedy, Family, Drama, Melodrama, Preschool / Early Learning, Slice of Life  
**Avoid when:** In thriller and serious drama it softens the tension because it removes the isolation. And in vertical, stack them rather than placing them side by side.  
**Prompt:** `split screen phone call, both characters in matching poses facing the divide, identical framing size, warm consistent grade across both halves`  
**Example:** When Harry Met Sally, which plays phone conversations in split screen.  
**Yields to:** `scene.phone_call_intercut` — in thriller and serious drama, where the split removes the isolation the call depends on; and `vertical.stacked_split` — in vertical, where the panels stack rather than sitting side by side.  
`scene.split_screen_phone_call`

### The Meanwhile Cross Cut

**Also called:** parallel action, intercutting two places  
**What it is:** Alternating between two events in different places happening at the same moment. The interval between switches shortens progressively as the two lines approach their meeting point.  
**Effect on the audience:** Mathematical tension: the shorter the intervals the higher the pressure, even with no change in content. It is the oldest and strongest climax formula in cinema.  
**Used for and where it works best:** The climax of every action, heist and chase film, and the birth and death beat in drama. Working rule: start with ten second blocks and work down to two. In documentary: the investigation thread against the victim's thread.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Documentary Feature, Anime (Japanese 2D), Game Cinematic / Gameplay, Short Film, Sports Broadcast / Sports Film | genres: Action, Heist, Thriller / Suspense, Crime / Procedural, War, Drama, Spy / Espionage, Shonen Battle (anime)  
**Avoid when:** If the two lines never meet the audience feels cheated. And do not switch at a peak inside one line; that kills the moment instead of building it.  
**Prompt:** `editor note: intercut the two locations with blocks shrinking from ten seconds to two, single continuous music cue across both`  
**Example:** The Godfather, whose baptism sequence intercuts the ceremony with the killings.  
**Yields to:** `scene.parallel_lives` — The two lines never meet.  
`scene.meanwhile_crosscut`

### The Phone-Call Intercut

**Also called:** two-location call, call coverage  
**What it is:** A call between two places shown by intercutting rather than split screen: each side in completely different light, colour and ambience, with the cutting accelerating as the call escalates.  
**Effect on the audience:** The difference in light and ambience states the difference between the two worlds. The viewer feels the distance between them even while they speak.  
**Used for and where it works best:** Thriller, crime and drama, and the danger call or the bad news call. Directing condition: a decisive lighting difference between the two sides. End the scene on silence after the line drops, on the side that lost.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Vertical Micro-Drama, Short Film, Soap Opera / Telenovela, Anime (Japanese 2D), Game Cinematic / Gameplay | genres: Thriller / Suspense, Crime / Procedural, Drama, Spy / Espionage, Melodrama, Political Thriller, Horror, Medical Drama  
**Avoid when:** Matching light and mood on both sides turns the call into an ordinary dialogue scene and wastes the device. And do not cut at even intervals; a mechanical rhythm kills the tension.  
**Prompt:** `intercut two singles with opposite lighting schemes, cool fluorescent one side and warm practical the other, cuts shortening as the call escalates`  
**Yields to:** `scene.split_screen_phone_call` — Both sides share light and mood.  
`scene.phone_call_intercut`

### The Ticking-Clock Cross Cut

**Also called:** countdown intercut, race against time  
**What it is:** Cross cutting between the danger line and the rescue line with a third constant element counting down: a clock, a bomb, a candle, a setting sun. That third element gets its own cutaway at intervals.  
**Effect on the audience:** It turns tension into something measurable. The viewer knows how much is left, does the arithmetic themselves, and tenses more than any vague threat could manage.  
**Used for and where it works best:** The climax of action, heist, disaster and medical rescue. The rule: show the counter early and clearly, and let its cutaways come closer together at the end. In heritage documentary it works on a setting sun at a site that must be filmed before dark.  
**Best in:** formats: Feature Film, Drama Series Episode, Trailer / Teaser, Game Cinematic / Gameplay, Documentary Feature, Anime (Japanese 2D), Sports Broadcast / Sports Film, Short Film | genres: Action, Heist, Disaster, Thriller / Suspense, Medical Drama, War, Survival, Spy / Espionage  
**Avoid when:** If the counter lies, the last seconds lasting longer than the number allows, the audience notices and stops trusting. And two counters in one sequence usually cancel each other, because the viewer can hold only one deadline at a time; the exception is when the second clock reveals that the first was the wrong thing to fear.  
**Prompt:** `editor note: intercut danger and rescue, insert the counter every third block, tighten counter cutaways from one every twenty seconds to one every five`  
**Yields to:** `scene.meanwhile_crosscut` — No honest counter available.  
`scene.ticking_clock_crosscut`

### Converging Storylines

**Also called:** convergence, threads meeting  
**What it is:** A whole structure: separate threads running in parallel through the piece and meeting in one place at one time. The transitions between them come closer together as the convergence point approaches.  
**Effect on the audience:** It delivers fate and architecture. The viewer feels the world is connected, and that feeling is the reward of the whole viewing.  
**Used for and where it works best:** Ensemble features, crime, disaster and limited series. What keeps it legible: give every thread its own colour, place or shot size, and plant small links between them before they meet. In heritage work: three cities converging on one event.  
**Best in:** formats: Feature Film, Limited Series, Drama Series Episode, Documentary Series, Short Film, Game Cinematic / Gameplay, Anime (Japanese 2D), Video Essay | genres: Crime / Procedural, Drama, Disaster, Political Thriller, Mystery / Whodunit, Tragedy, Historical / Biopic, Seinen (mature anime)  
**Avoid when:** A convergence built on pure coincidence with no groundwork gets rejected. And do not run more than four threads; comprehension collapses.  
**Prompt:** `editor note: give each thread a distinct palette and shot size, shorten the switches as they approach, land them all in one location in one continuous shot`  
**Yields to:** `scene.anthology_chapters` — Threads cannot plausibly meet.  
`scene.converging_storylines`

### Return to the Opening Image

**Also called:** closing the circle, first and last frame  
**What it is:** The last shot of the piece repeats the first: the same place, angle and composition in a changed state. The ending answers the beginning visually.  
**Effect on the audience:** It delivers the feeling of a closed circle. The audience leaves feeling the piece said everything it meant to, even without knowing why.  
**Used for and where it works best:** The ending of any dramatic, heritage or music piece. Design it on the shoot: record the lens, height and distance on the day of the first shot. In heritage work: the site at dawn to open and at dusk to close.  
**Best in:** formats: Feature Film, Short Film, Music Video, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Limited Series, Commercial / TVC | genres: Drama, Heritage (civilisation-focused), Tragedy, Romance, Historical / Biopic, Psychological / Arthouse, Coming of Age, Faith / Biblical Epic  
**Avoid when:** Returning to the identical image with no change and no intention is just repetition. And the change has to be readable in a single shot without explanation.  
**Prompt:** `repeat the first shot of the film exactly, same lens height and distance, with the one element that the story changed now different`  
**Yields to:** `scene.bookends` — The change is not readable in one shot.  
`scene.return_to_opening_image`

### The Pull-Back Reveal Ending

**Also called:** final pull back, the widening ending  
**What it is:** The final shot starts close on the character and the camera pulls back or rises steadily until it reveals the larger context: the city, the desert, the crowd, the ruin.  
**Effect on the audience:** It eases the viewer out of the story and gives it its true scale. The character shrinks and the meaning grows.  
**Used for and where it works best:** The ending of epic, heritage, war and social drama. In heritage work it is the best possible ending: from the craftsman's or the researcher's face to an aerial pull revealing the whole site with the river behind it. Keep the pull slow and at constant speed.  
**Best in:** formats: Feature Film, Heritage / Historical Documentary, Documentary Feature, Short Film, Music Video, Trailer / Teaser, Travel / Real Estate / Hospitality, 3D CG Animation | genres: Drama, Heritage (civilisation-focused), War, Historical / Biopic, Tragedy, Nature / Wildlife, Mythology / Ancient Epic, Survival  
**Avoid when:** If the reveal adds no new meaning the pull back is just a technical flourish. And do not speed it up; speed turns contemplation into escape.  
**Prompt:** `slow continuous aerial pull back from a close-up of his face to an extreme wide of the whole valley, constant speed, no cuts`  
**Yields to:** `scene.walk_into_the_distance` — No larger context to reveal.  
`scene.pull_back_reveal_ending`

### The Freeze-Frame Ending

**Also called:** final freeze, held frame ending, last-frame hold, ending still  
**What it is:** The image freezes on a single frame in mid-action and holds until black or the credits, sometimes with a slight push in. The sound sometimes continues past the freeze and sometimes stops with it, and Truffaut established it as an open ending.  
**Effect on the audience:** It stops time and converts the moment into a photograph. The audience never learns what came next, so the character stays suspended in their mind.  
**Used for and where it works best:** An open or inevitable ending: the hero mid-run, the child looking into the lens, an episode closing on a suspended beat. Pick a frame with movement and expression in it, not a still pose. In sports films it is the final victory frame, and in vertical short-form it works as a hard close before the next episode.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Sports Broadcast / Sports Film, Music Video, Vertical Short-Form (Reels, Shorts, TikTok), Trailer / Teaser, 2D Animation (Western / Cartoon), Anime (Japanese 2D), Documentary Feature | genres: Drama, Coming of Age, Sports Drama, Crime / Procedural, Tragedy, Western, Comedy, Adventure, Romance, Slice of Life, War  
**Avoid when:** In contemporary drama it now reads as a period convention, so use it knowingly, and if the frame is not visually strong the freeze exposes it. Do not use it on a clearly happy ending either; it is the shape of a question, not of a resolution.  
**Prompt:** `editor note: freeze on the frame with the strongest expression mid-movement, hold eight seconds, let the sound run two seconds past the freeze`  
**Example:** The 400 Blows, which ends on a freeze frame of the boy's face.  
**Yields to:** `scene.hard_cut_to_credits` — A resolved or happy ending.  
`scene.freeze_frame_ending`

### Walk Into the Distance

**Also called:** walking away ending, the back of the character  
**What it is:** The last shot: the character walks away from the camera until they shrink or disappear, with the camera locked and not following. We see the back, not the face.  
**Effect on the audience:** It ends the relationship between viewer and character physically. The departure is the goodbye, and withholding the face refuses any final answer.  
**Used for and where it works best:** The ending of westerns, road movies, drama and heritage work. The condition: a fully locked camera, and hold at least three seconds after the figure has gone. In heritage work: the figure walking into the site until it becomes a dot.  
**Best in:** formats: Feature Film, Short Film, Heritage / Historical Documentary, Music Video, Drama Series Episode, Documentary Feature, Anime (Japanese 2D), Travel / Real Estate / Hospitality | genres: Western, Road Movie, Drama, Tragedy, Heritage (civilisation-focused), Historical / Biopic, Adventure, Coming of Age  
**Avoid when:** Following with the camera cancels the goodbye and turns it into a beginning. And do not cut before they have gone; the waiting is the meaning.  
**Prompt:** `locked wide, the figure walking away from camera into the depth of the frame until small, hold three seconds after they leave frame`  
**Example:** The Searchers, which ends with the character walking away from the doorway.  
`scene.walk_into_the_distance`

### The Door-Closes Ending

**Also called:** shutting out the viewer, the closing frame  
**What it is:** The final shot: a door, a curtain or a lift closes between the camera and a character and cuts off the view. Sometimes another character is the one closing it.  
**Effect on the audience:** The viewer is shut out of the character's world. Being denied the view lands harder than any line: this person is now a stranger to you.  
**Used for and where it works best:** The ending of crime, gangster and family drama. Visual condition: frame the character inside the doorway before it closes so the loss registers. Control the speed: a slow close reads as dread, a fast one as severance.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Limited Series, Soap Opera / Telenovela, Anime (Japanese 2D), Vertical Micro-Drama, Music Video | genres: Gangster, Crime / Procedural, Drama, Tragedy, Melodrama, Noir / Neo-Noir, Family, Psychological / Arthouse  
**Avoid when:** If no relationship actually broke in the story the door is a formal trick. And keep the music down; the sound of the door is the last line.  
**Prompt:** `locked shot from the outer room, the character framed inside the doorway, the door swinging closed between camera and subject, cut to black on contact`  
**Example:** The Godfather, which ends on the office door closing on Kay.  
**Yields to:** `scene.walk_into_the_distance` — No relationship actually broke.  
`scene.door_closes_ending`

### Cut to Black Mid-Action

**Also called:** abrupt black, the severed ending  
**What it is:** The piece cuts to full black mid-movement, mid-line or mid-note with no visual or audio preparation. The sound stops on the same frame.  
**Effect on the audience:** It leaves the viewer physically suspended. The absence of an ending is the ending, and the meaning transfers entirely to the audience's imagination.  
**Used for and where it works best:** Open and fatalistic endings in drama, crime and horror. The condition is that the whole piece has prepared the idea that the answer does not matter, otherwise it reads as a technical fault. Use it once in the life of a work.  
**Best in:** formats: Drama Series Episode, Feature Film, Limited Series, Short Film, Experimental / Art Film, Vertical Micro-Drama, Anime (Japanese 2D), Music Video | genres: Crime / Procedural, Gangster, Drama, Psychological / Arthouse, Thriller / Suspense, Tragedy, Noir / Neo-Noir, Seinen (mature anime)  
**Avoid when:** An unprepared audience assumes the file broke and gets angry. And keep it out of commercial work that depends on satisfaction.  
**Prompt:** `editor note: cut picture and sound to black on the same frame in the middle of a movement, no fade, ten seconds of silent black before credits`  
**Example:** The Sopranos, whose final scene cuts to black mid-action.  
**Yields to:** `scene.end_on_a_question` — The audience was not prepared.  
`scene.cut_to_black_mid_action`

### Hard Cut to Credits on the Beat

**Also called:** straight to credits, credits on the hit  
**What it is:** The last frame of the film cuts straight into the credits with a strong music cue entering on that same frame. There is no black and no fade between them.  
**Effect on the audience:** It preserves the energy and sends the audience out charged. The ending does not stop; it converts into sound.  
**Used for and where it works best:** Action, comedy, sports and musical work, and anything that wants the audience leaving energised rather than reflective. Place the entry exactly on the song's first downbeat. In short-form the same principle applies: last frame, then the end card on the beat.  
**Best in:** formats: Feature Film, Title Sequence / Opening Credits, Music Video, Commercial / TVC, Vertical Short-Form (Reels, Shorts, TikTok), Sports Broadcast / Sports Film, 2D Animation (Western / Cartoon), Trailer / Teaser | genres: Action, Comedy, Musical, Sports Drama, Superhero, Adventure, Heist, Rom-Com  
**Avoid when:** In tragedy and heritage work it breaks the grief and feels disrespectful. And avoid it when the last scene needs silence.  
**Prompt:** `editor note: cut from the final frame straight to the main title card with the song downbeat landing on that exact frame, no black`  
**Yields to:** `scene.last_scene_to_end` — Tragedy or heritage; grief needs silence.  
`scene.hard_cut_to_credits`

### The Silent Epilogue

**Also called:** wordless coda, the last quiet scene  
**What it is:** A final scene with no dialogue and no music: the character does something ordinary (drinks water, opens a window, wipes dust) and it ends. Natural sound only.  
**Effect on the audience:** It returns life to its ordinary shape after everything that happened, and that itself hurts. The audience feels the world moved on and that the loss changed nothing outside.  
**Used for and where it works best:** After tragedy, after war, after a loss. In heritage work: the site today with ordinary people passing without noticing. Run it longer than expected; the length is the device.  
**Best in:** formats: Feature Film, Short Film, Documentary Feature, Heritage / Historical Documentary, Limited Series, Drama Series Episode, Experimental / Art Film, Anime (Japanese 2D) | genres: Tragedy, Drama, War, Heritage (civilisation-focused), Psychological / Arthouse, Melodrama, Slice of Life, Historical / Biopic  
**Avoid when:** Laying music over it turns an observation into a comment and loses its coolness. And do not close it with a line of wisdom; that cancels everything.  
**Prompt:** `locked wide, one ordinary domestic action performed in full with natural room sound only, no music, hold until it finishes and two seconds more`  
`scene.silent_epilogue`

### End on a Question

**Also called:** unresolved ending, the open close  
**What it is:** The piece ends with its most important question unanswered: who it was, what he will do, whether she lived. The last shot poses the question visually instead of answering it.  
**Effect on the audience:** It keeps the piece running after it has ended. The audience thinks about it for days and argues about it, which is the strongest form of survival a film has.  
**Used for and where it works best:** Arthouse drama, mystery, sci-fi and the short film. The ethical condition: every other question must be answered, and the one left open must be deliberate and planted. In documentary it works when the truth genuinely is not known.  
**Best in:** formats: Feature Film, Short Film, Limited Series, Documentary Feature, Drama Series Episode, Experimental / Art Film, Video Essay, Vertical Micro-Drama | genres: Mystery / Whodunit, Psychological / Arthouse, Sci-Fi, Drama, Thriller / Suspense, True Crime, Surreal / Absurdist, Tragedy  
**Avoid when:** If you left the question open because you had no answer, the audience can smell it. And more than one open question usually reads as sloppiness rather than mystery, because the viewer cannot tell which one the film meant; the exception is a piece whose subject is uncertainty itself.  
**Prompt:** `editor note: final shot frames the unanswered element in the centre, hold it six seconds, cut to black without a reverse angle`  
**Yields to:** `scene.epilogue_time_jump` — You withheld because you had no answer.  
`scene.end_on_a_question`

### The Button

**Also called:** scene button, the tag line of the scene  
**What it is:** The last beat of a scene: one line, a small gesture or a look arriving after the main event is over, closing the scene on a specific note (a joke, a threat, a sadness). The scripted last line itself is written under `scene.button`; this card is the edit's side of it: which picture closes the scene and how long it is held.  
**Effect on the audience:** It gives the scene a shape and an ending instead of letting it fade out. The viewer leaves the scene with a specific feeling rather than a general one.  
**Used for and where it works best:** Sitcom and comedy, where most scenes take one, and in television drama the scenes that end on a reversal — not every drama scene, because buttoning each one reads as a series of sketches (`scene.button`). The rule: keep it very short — hold only until its meaning lands, measured against the performance and the rhythm rather than a fixed count. In sitcom it is the last joke before the cut; in drama it is the look left behind after everyone leaves.  
**Best in:** formats: Sitcom / Multi-Cam Comedy, Drama Series Episode, Feature Film, Soap Opera / Telenovela, Vertical Micro-Drama, Short Film, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D) | genres: Comedy, Rom-Com, Drama, Dark Comedy / Satire, Crime / Procedural, Family, Melodrama, Slice of Life  
**Avoid when:** A button that runs long or explains becomes another scene and slackens the rhythm. And do not button every scene; some must be cut off without closure.  
**Prompt:** `editor note: after the scene's last line or main action, hold one small gesture or look only until its meaning lands, then cut`  
**Yields to:** `scene.cut_on_the_question` — Some scenes must close without closure.  
`scene.the_button`

### The Stinger

**Also called:** sting, the last shock  
**What it is:** A very short shot after the audience believes the piece is over, flipping the meaning or restoring the threat: an eye opening, a hand emerging, a door opening. Usually on an audio stab.  
**Effect on the audience:** It sends the viewer out unsettled. The last feeling is the one that stays, so the whole piece is re-evaluated in its light.  
**Used for and where it works best:** Horror above all, then crime and sci-fi. The condition: the audience must genuinely believe it is over, or it does not work. In short-form the same structure works as one second after the point has landed.  
**Best in:** formats: Feature Film, Drama Series Episode, Short Film, Trailer / Teaser, Vertical Short-Form (Reels, Shorts, TikTok), Anime (Japanese 2D), Game Cinematic / Gameplay, Vertical Micro-Drama | genres: Horror, Slasher, Supernatural Horror, Thriller / Suspense, Crime / Procedural, Sci-Fi, Monster / Kaiju, Psychological Horror  
**Avoid when:** On a piece that needs no sequel it feels like blackmail for a second part. And more than one shot usually turns it into a scene and spends the surprise; the exception is a comedy where the stretched joke is the payoff.  
**Prompt:** `editor note: after two seconds of black, cut in a one second shot restoring the threat with a single sharp audio stab, then black again`  
**Yields to:** `scene.mid_and_post_credits` — A longer beat belongs in the credits.  
`scene.the_stinger`

### Mid-Credits and Post-Credits Scenes

**Also called:** credit cookie, post-credits scene  
**What it is:** A short scene placed in the middle of the credits or after they finish. It usually opens a new thread, completes a joke, or introduces a coming character.  
**Effect on the audience:** It rewards the viewer who stayed and builds a loyalty contract. It also works as a promise of what comes next without imposing on the current ending.  
**Used for and where it works best:** Superhero and adventure franchises and comedy, and anything with a sequel. The practical distinction: the mid-credits scene opens a new thread, while the post-credits scene is usually a joke or a small beat.  
**Best in:** formats: Feature Film, Drama Series Episode, 2D Animation (Western / Cartoon), 3D CG Animation, Game Cinematic / Gameplay, Anime (Japanese 2D), Trailer / Teaser, Title Sequence / Opening Credits | genres: Superhero, Action, Comedy, Sci-Fi, Fantasy / Epic, Adventure, Family, Monster / Kaiju  
**Avoid when:** If the scene carries information needed to understand the ending you punish everyone who left. And do not attach one to a sad ending; it breaks it.  
**Prompt:** `editor note: place a twenty second scene at the credits midpoint that opens a new thread, and a five second comic beat after the final card`  
**Example:** Iron Man (2008), whose post-credits scene sets up a larger series.  
**Yields to:** `scene.epilogue_time_jump` — The information is needed to understand the end.  
`scene.mid_and_post_credits`

### The Next Time Tease

**Also called:** next episode preview, coming up  
**What it is:** A short piece after the episode showing shots from the next one, chosen to open questions rather than explain. Usually fast cut with fragmented dialogue.  
**Effect on the audience:** It converts the end of the episode into the start of a wait. The viewer leaves with two questions instead of one, which raises the odds they return.  
**Used for and where it works best:** Drama series, documentary series, anime and vertical micro-drama. The right selection favours reaction shots and unfinished lines over shots that reveal events. In anime it is a fixed convention with the character's voice commenting over it.  
**Best in:** formats: Drama Series Episode, Limited Series, Documentary Series, Anime (Japanese 2D), Vertical Micro-Drama, Soap Opera / Telenovela, Vertical Short-Form (Reels, Shorts, TikTok), Meme / Comedy Edit | genres: Drama, Crime / Procedural, Mystery / Whodunit, Thriller / Suspense, Melodrama, True Crime, Shonen Battle (anime), Political Thriller  
**Avoid when:** A shot that burns the next episode's twist destroys it before it starts. And do not run it after a shocking ending; it softens the shock.  
**Prompt:** `editor note: cut eight half second shots of reactions and unfinished lines from the next episode, no shot that reveals an outcome`  
**Yields to:** `scene.episode_to_episode` — After a shock, let the cliffhanger stand.  
`scene.next_time_tease`

### Act Break on an Open Question

**Also called:** act out, the break beat  
**What it is:** The last scene of an act ends on information that reverses the situation and opens a question: a door opening on someone unexpected, a message read, a name spoken. The act ends on the turn, not after it.  
**Effect on the audience:** It gives the structure a spine. The audience feels the piece has clear joints, and each joint raises the stakes above the one before.  
**Used for and where it works best:** The end of acts one and two in a feature, and the end of every section in limited series and documentary. The condition: the new question must be bigger than the one before it. In documentary: end the section on a document that contradicts everything we heard.  
**Best in:** formats: Feature Film, Drama Series Episode, Limited Series, Documentary Series, Documentary Feature, Vertical Micro-Drama, Video Essay, Soap Opera / Telenovela | genres: Thriller / Suspense, Crime / Procedural, Mystery / Whodunit, Drama, Political Thriller, True Crime, Legal Drama, Sci-Fi  
**Avoid when:** An act ending on a comfortable answer makes the next one start from zero and lose momentum. And a reversal with no planted root reads as arbitrary.  
**Prompt:** `editor note: end the act on the frame where the new information lands, cut before any reaction dialogue, one second of black before the next act`  
**Yields to:** `scene.act_to_act` — No honest reversal; mark the act plainly.  
`scene.act_break_open_question`

### Cliffhanger Before the Ad Break

**Also called:** act out for commercials, the break hook  
**What it is:** Right before the break the story stops on a moment of danger or an incomplete reveal, and after the break it resumes at that moment or seconds later. The structure is designed around the break positions rather than interrupted by them.  
**Effect on the audience:** It stops the viewer changing channel. A suspended danger makes waiting psychologically expensive, so they stay.  
**Used for and where it works best:** Broadcast television, daily drama, competition and sports formats. Know your break positions from the script stage and build to them. On ad-free platforms the same principle applies to the viewer's natural stopping points.  
**Best in:** formats: Drama Series Episode, Soap Opera / Telenovela, News Report / Reportage, Sports Broadcast / Sports Film, Vertical Micro-Drama, Limited Series, Documentary Series, Meme / Comedy Edit | genres: Melodrama, Crime / Procedural, Thriller / Suspense, Drama, Medical Drama, Legal Drama, True Crime, Sports Drama  
**Avoid when:** Returning from the break on a completely different scene makes the audience feel cheated. And do not replay the pre-break shot afterwards; it reads as a repeat.  
**Prompt:** `editor note: end the block on the frame of maximum danger, hold it half a second, resume after the break two seconds before that same moment`  
`scene.cliffhanger_before_ad_break`

### One Scene, One Idea

**Also called:** single purpose scene, one job per scene  
**What it is:** Every scene carries exactly one change: it delivers information, it turns a relationship, or it moves a decision. In narrative fiction information counts only when somebody in the scene wants something and a value turns on it; information with no want and no turn fails `scene.dead_scene_test` and moves into a scene that works. A scene doing three jobs is either split into three or stripped back to one.  
**Effect on the audience:** Clarity. The viewer leaves every scene knowing what changed, and the accumulation of those changes is what they experience as a story moving.  
**Used for and where it works best:** A practical focus test in the edit, after a narrative scene has passed `scene.dead_scene_test`: ask of every scene what the single thing that changed was. If you cannot answer in one sentence the scene needs cutting or deleting. It applies to everything: features, short-form, ads, documentary — in ads and documentary an information-only unit can be valid, because it is not pretending to be a dramatic scene; in narrative fiction information alone still fails the want-and-turn test above.  
**Best in:** formats: all | genres: all  
**Avoid when:** In large sequences (a wedding, a battle) the single idea applies to the sequence as a unit, not to every shot. And do not apply it literally to contemplative work.  
**Prompt:** `editor note: name the one thing that changes in this scene in a single sentence, cut everything that does not serve that change`  
**Yields to:** `scene.development_scene` — Contemplative work deepens without changing.  
`scene.one_scene_one_idea`

### Enter on Movement, Exit on Stillness

**Also called:** move in still out, the scene envelope  
**What it is:** The scene opens on a frame with movement in it (someone walking, a door opening, hands working) and ends on a still one: the movement has stopped and the camera is locked. The shape itself marks the start and the finish.  
**Effect on the audience:** It gives every scene an arc the audience reads unconsciously. The scene feels like it began and ended even when nothing large happened in it.  
**Used for and where it works best:** Drama, documentary, heritage and short film, and anything needing scenes of comparable length. Practical benefit in the edit: the in and out points become obvious on the shoot instead of by trial and error.  
**Best in:** formats: Feature Film, Short Film, Documentary Feature, Heritage / Historical Documentary, Drama Series Episode, Anime (Japanese 2D), Travel / Real Estate / Hospitality, Vertical Micro-Drama | genres: Drama, Heritage (civilisation-focused), Historical / Biopic, Slice of Life, Psychological / Arthouse, Romance, Tragedy, Verite / Observational  
**Avoid when:** Applied to every scene without exception the rhythm becomes monotonous and predictable. Break it with a scene severed mid-movement when you want a shock.  
**Prompt:** `editor note: choose the in point on the first frame of a movement and the out point on the first frame after everything stops`  
**Yields to:** `scene.interrupted_scene` — You want a shock; sever mid-movement.  
`scene.enter_on_movement_exit_on_stillness`

### Alternating Rhythm

**Also called:** fast slow fast, scene tempo alternation  
**What it is:** Ordering the scenes so a fast short one is followed by a slow long one, and so on. The alternation works at the level of the sequence of scenes, not inside a scene.  
**Effect on the audience:** It prevents fatigue. Eye and ear need a change of pace more than they need high pace, and the alternation is what makes a film feel balanced.  
**Used for and where it works best:** Ordering act two of a feature and structuring an episode. The practical test: chart each scene's duration as a bar, and if five bars in a row are the same height, reorder. In documentary: a long interview followed by a short archive burst.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Documentary Series, Limited Series, Heritage / Historical Documentary, Video Essay, Short Film | genres: all  
**Avoid when:** A mathematically regular alternation becomes noticeable and predictable. Vary the amount, not just the direction.  
**Prompt:** `editor note: chart every scene duration as a bar, break any run of similar lengths by reordering or trimming`  
`scene.alternating_rhythm`

### The Sound Motif Return

**Also called:** musical motif callback, leitmotif return  
**What it is:** A specific melody or sound is planted in an early scene attached to a particular state, and returns much later in a different form: the same theme on another instrument, at a slower tempo, or broken.  
**Effect on the audience:** It transmits a complete meaning in two seconds. The audience remembers the first scene in the body, so the new moment carries the whole charge of the old one.  
**Used for and where it works best:** Drama, epic, anime and heritage work. The rule: plant the motif in a happy or ordinary scene and bring it back at the loss. In heritage documentary: a theme attached to the living city, returning broken over its ruins.  
**Best in:** formats: Feature Film, Drama Series Episode, Anime (Japanese 2D), Heritage / Historical Documentary, Documentary Feature, Music Video, 3D CG Animation, Limited Series | genres: Drama, Tragedy, Fantasy / Epic, Heritage (civilisation-focused), Historical / Biopic, War, Romance, Mythology / Ancient Epic  
**Avoid when:** Planted only once, the motif is not recognised on its return. Repeated too often it becomes a jingle rather than a memory.  
**Prompt:** `editor note: plant the theme twice in full in act one, return it at the loss on a single solo instrument at half tempo`  
**Yields to:** `scene.callback_shot` — Nothing was planted in sound.  
`scene.sound_motif_return`

### The Same Event Retold

**Also called:** Rashomon structure, multiple perspective repeat  
**What it is:** The same event replays more than once in the piece, each time from a different character's viewpoint, with the details changed: who spoke first, who held the weapon, what was actually said.  
**Effect on the audience:** It turns truth itself into the subject. The viewer becomes a judge and understands that each version serves the interests of its teller.  
**Used for and where it works best:** Mystery, crime, legal drama and investigative documentary. The structure comes from Akira Kurosawa's Rashomon. Technical condition: change one technical element in each version (lighting, shot size, movement) so the difference is felt and not merely understood.  
**Best in:** formats: Feature Film, Limited Series, Drama Series Episode, Documentary Feature, Short Film, Video Essay, Documentary Series, Game Cinematic / Gameplay | genres: Mystery / Whodunit, Crime / Procedural, Legal Drama, Drama, True Crime, Psychological / Arthouse, Political Thriller, Noir / Neo-Noir  
**Avoid when:** If the versions do not differ in substance the repeat becomes tedious. And do not hand over a single clear answer at the end if the whole structure argues that truth is relative.  
**Prompt:** `editor note: reshoot the same event with a different lighting scheme and shot size for each witness, keep the blocking recognisable`  
**Example:** Rashomon, which retells one event through several conflicting accounts.  
**Yields to:** `scene.pov_handoff` — The versions differ too little to replay.  
`scene.rashomon_repeat`

### The Epilogue Time Jump

**Also called:** years later epilogue, the coda card  
**What it is:** After the plot resolves, a time card ("five years later") then a short scene showing where the characters ended up. The scene is calm and carries no conflict.  
**Effect on the audience:** It gives the audience the comfort of closure and answers the "what then" question. It also converts the story from an event into a history.  
**Used for and where it works best:** Drama, biopic, war, family films and documentary. In documentary it takes the form of text cards giving each subject's fate. The condition: the epilogue must add new meaning rather than only reassure, otherwise it can be cut.  
**Best in:** formats: Feature Film, Limited Series, Documentary Feature, Docudrama / Reenactment, Drama Series Episode, Heritage / Historical Documentary, Short Film, Soap Opera / Telenovela | genres: Drama, Historical / Biopic, War, Family, Melodrama, Coming of Age, True Crime, Sports Drama  
**Avoid when:** If the original ending was strong and open, the epilogue weakens it by answering a question that should have stayed open. And more than one jump stacked usually loses the audience, because each one asks them to rebuild the world again; the exception is a saga that has been moving through time all along.  
**Prompt:** `editor note: clean time card naming the gap, then one short calm scene with no conflict, ending on a detail that reframes the story`  
**Yields to:** `scene.end_on_a_question` — The original open ending was stronger.  
`scene.epilogue_time_jump`

### Credits Over Action

**Also called:** credits over the opening scene, running titles  
**What it is:** The opening credits run over the first scene while it plays instead of occupying their own sequence. The scene is composed with empty areas in frame to hold the type.  
**Effect on the audience:** The piece starts immediately with no delay. The viewer is inside the story from the first second and the names pass without stopping anything.  
**Used for and where it works best:** Realist drama, crime, western and documentary, and anything wanting an unceremonious start. Design note: keep the lower third or one side of frame clear in every shot that carries a name. In short-form the same principle applies to the title text over the opening shot.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Title Sequence / Opening Credits, Short Film, Limited Series, Heritage / Historical Documentary, Vertical Short-Form (Reels, Shorts, TikTok) | genres: Crime / Procedural, Drama, Western, War, Noir / Neo-Noir, Verite / Observational, Political Thriller, Historical / Biopic  
**Avoid when:** If the scene carries important dialogue the type steals attention and the information is lost. And do not place names over a visually busy shot; they will not read.  
**Prompt:** `compose the opening shots with a clean empty lower third for the credit type, slow simple camera movement, no critical dialogue under the names`  
**Yields to:** `scene.titles_to_first_scene` — The opening scene needs its dialogue.  
`scene.credits_over_action`

### Anthology Structure

**Also called:** portmanteau structure, segmented film  
**What it is:** The piece is built from complete short stories, each with its own characters, tied together by a shared theme, place or framing device. The joins are clearly marked: a card, black, or a full change of style.  
**Effect on the audience:** It permits several styles inside one work, and invites the audience to compare the stories so a meaning larger than their sum emerges.  
**Used for and where it works best:** Thematic features, horror, heritage documentary and seasonal series. In heritage work: one story per city or per craft, tied by the river or the language. Order them so the strongest is last and the second strongest is first.  
**Best in:** formats: Feature Film, Drama Series Episode, Documentary Feature, Heritage / Historical Documentary, Short Film, Documentary Series, Anime (Japanese 2D), Experimental / Art Film | genres: Horror, Drama, Dark Comedy / Satire, Heritage (civilisation-focused), Historical / Biopic, Surreal / Absurdist, Fantasy / Epic, Slice of Life  
**Avoid when:** One clearly weaker story drags the whole piece down, because the audience compares. And do not let the framing device run longer than the stories themselves.  
**Prompt:** `editor note: mark each segment with the same designed card and one second of black, give each its own palette, place the strongest segment last`  
**Yields to:** `scene.converging_storylines` — The segments need to meet.  
`scene.anthology_chapters`
