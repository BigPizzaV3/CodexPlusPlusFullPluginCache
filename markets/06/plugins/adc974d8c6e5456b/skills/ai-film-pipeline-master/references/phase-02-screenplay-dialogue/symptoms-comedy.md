# Comedy complaints

Part of the symptom router. Open this file when the complaint is about comedy. Each complaint below is followed by the cards that repair it, best first; `LOOKUP.md` says which file holds each card.

---

### "It isn't funny"

Comedy is engineering. Check the machine before blaming the material.

1. Is there a setup and a punchline, in that order, with nothing after it
   `comedy.setup_punchline` · `comedy.funny_word_last`
2. Is the funniest word last in the sentence
   `comedy.funny_word_last` · `comedy.timing_on_the_page`
3. Is there a misdirection, or is the joke going where expected
   `comedy.misdirection` · `comedy.audience_gets_there_first`
4. Is anyone playing it straight
   `comedy.straight_man` · `comedy.wrong_reaction`

### "The audience gets there before the joke does"

1. The named failure. The repair is the sharpest move in comedy: hand them the answer they guessed and make the joke whatever lies past it
   `comedy.audience_gets_there_first`
2. Add a topper that carries no new information
   `comedy.topper`

### "The jokes stop the story"

1. The named failure
   `comedy.joke_that_stops_story`
2. A comic character needs an engine, not a joke supply
   `comedy.comic_character_engine` · `comedy.only_funny_character`
3. Never explain it
   `comedy.explained_joke`

### "The comedy has no engine"

1. Status is the engine. Who is up, who is down, and when it flips
   `comedy.status_engine` · `char.status_transaction` · `char.status_flip`
2. Escalate in a spiral rather than a line
   `comedy.escalation_spiral` · `comedy.overstatement` · `comedy.understatement`
3. Pick the mode deliberately
   `comedy.farce_engine` · `comedy.comedy_of_manners` · `comedy.satire_target` · `comedy.cringe` · `comedy.dark_comedy`

### "The running gag died"

1. Stop at three or commit past seven; there is nothing in between
   `comedy.repetition_turn` · `comedy.running_gag`
1b. And the reason three is the number: it is the smallest count that can hold a pattern and a betrayal of it in the same breath
   `comedy.rule_of_three`
2. Pay it at the end
   `comedy.callback_payoff` · `end.callback`

### "The funny character isn't funny"

1. Give them a comic flaw rather than a set of jokes
   `comedy.comic_flaw` · `comedy.quirk_as_character`
2. The strongest comic engine is a logic that is airtight and wrong
   `comedy.airtight_wrong_logic` · `comedy.maintained_delusion`
3. Expertise in something useless is free comedy for a whole series
   `comedy.useless_expertise`
4. Or build a pair whose difference generates jokes without anyone writing one
   `comedy.generative_pairing`

### "The comic scene has no engine"

1. Build it on one misunderstanding and let nobody resolve it
   `comedy.one_misunderstanding`
2. Or on an obligation that keeps growing
   `comedy.escalating_obligation`
3. Put the scene in the wrong place for it
   `comedy.wrong_place`
4. Get the entrance and the exit right; they carry more than the middle
   `comedy.comic_entrance` · `comedy.exit_joke`
5. And know where the scene stops being funny on purpose
   `comedy.deliberate_stop`

### "The improv thing — how does it transfer to the page?"

1. Find the game of the scene and then play it
   `comedy.game_of_the_scene`
2. Find the first unusual thing and explore it rather than adding a second
   `comedy.first_unusual_thing` · `comedy.heighten_and_explore`
3. Yes-and on the page is agreement plus escalation, not politeness
   `comedy.yes_and_on_page`

### "The wordplay is groaning"

1. A pun is legitimate under conditions; the card names them
   `comedy.pun_legitimacy` · `comedy.malapropism`
2. A cliché used deliberately is a different move from a cliché used lazily
   `comedy.deliberate_cliche`
3. Register collision does more work than any pun
   `comedy.register_collision` · `comedy.technically_correct`

### "The comic premise ran out"

1. Every premise has a shelf life; know yours before episode four
   `comedy.premise_shelf_life` · `comedy.season_engine`
2. In a sitcom the A and B stories must collide, not run parallel
   `comedy.ab_collision`
3. The reset button has a cost, and it is different for binge and for syndication
   `comedy.reset_cost`
4. The comic ending is the hardest one in the form
   `comedy.comic_ending`

### "The tone keeps slipping"

1. Turning serious and back is a technique with rules
   `comedy.turn_serious_and_back` · `comedy.when_to_stop`
2. The last joke before a death has a specific job
   `comedy.last_joke_before_death`
3. Comedy inside tragedy and tragedy inside comedy are different problems
   `comedy.comedy_in_tragedy` · `comedy.tragedy_in_comedy`

### "Is this joke going to be a problem?"

1. Audit who the joke is actually aimed at — a craft question before it is an ethical one
   `comedy.joke_target_audit` · `comedy.punch_direction`
2. A joke at a character's expense can cost the audience's sympathy for the whole piece
   `comedy.sympathy_cost_joke`
3. Comedy that only works if the audience already agrees is not comedy
   `comedy.requires_agreement`
4. And some jokes have a shelf life that is shorter than the work's
   `comedy.joke_shelf_life`

### "The joke is a reference"

1. The named failure. A reference is recognition, not a joke
   `comedy.reference_not_joke`

### "It doesn't survive translation"

1. Some comedy cannot cross, and knowing which kind saves a rewrite
   `comedy.cross_cultural_comedy` · `comedy.translation_resistance`

`comedy.translation_resistance` · `comedy.literal_answer` · `comedy.non_sequitur` · `comedy.observational_truth`


### "The physical gag only works if someone funny performs it"

1. Then it is not written yet. Specify it as geometry and consequence — what moves, where, and what it collides with — so the joke exists on the page before anyone is cast
   `comedy.physical_on_page`

### "The joke doesn't fit in fifteen seconds"

1. Compress to the short-form shape: about a tenth hook, three-quarters build, a fifth payoff, with the hook landing in the first two seconds
   `comedy.short_form_shape`
2. That leaves no room for a second joke, so pick the one that survives and cut the other
   `comedy.deliberate_stop`

---
