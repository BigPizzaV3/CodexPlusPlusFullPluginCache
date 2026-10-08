# Formats — animation

Entry point into the database. Each kit lists technique ids; open the matching `cat-*.md` for the full card.

One fact governs this whole family: **animation is priced by the frame.** A page is not a page here — it is a commissioned drawing count, a rig build, a background paint, a puppet, a week of an animator's life. A live-action writer who adds a location adds a scout. An animation writer who adds a location adds an asset that did not exist in the universe and now has to be designed, approved, built, lit and maintained for every episode it appears in. Shot count, cast count, location count and crowd size are budget decisions before they are creative ones, and they are made at script stage because after board lock they cannot be made at all.

The second fact follows from the first: **voice is recorded before the picture exists.** In most animation pipelines the performance is locked months before anyone sees a frame, which reverses the live-action order of operations. You cannot fix it in the edit, because there is no coverage to cut to. The rewrite happens on the page or it does not happen.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Animated Series (kids)](#animated-series-kids)
- [Animated Series (adult)](#animated-series-adult)
- [Anime](#anime)
- [Short Animation](#short-animation)
- [Stop Motion and Craft Animation](#stop-motion-and-craft-animation)
- [Motion Graphics and Explainer Animation](#motion-graphics-and-explainer-animation)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## Animated Series (kids)

**Constraints:** The dominant unit is the 11-minute episode, two paired into a half-hour block — a 52 x 11 or 26 x 22 order. An 11-minute script runs roughly 14 to 18 pages, longer than the one-page-per-minute rule because action lines must specify what the artists will draw. Preschool work is frequently board-driven: the writer delivers a premise and outline and the story artist writes the episode in pictures. Older-skewing kids' series stay script-driven. Cast, locations and props are a fixed library set in the series bible; anything outside it is a design request with a cost and an approval chain. Voice records before board, so a joke that does not work in the room is dead on the page, not in the edit. Broadcasters attach curriculum or pro-social requirements and a standards pass that will cut peril, ingestion gags and anything imitable.

**Grammar:** One problem per episode, visible in the first ninety seconds, solved by the child character using something a child could plausibly do. The series is a machine that must run 52 times, so the engine is the cast's fixed contradictions, not the individual plot — you are writing a system that generates episodes, and every episode restores the starting state. Arcs sit in the characters' unchanging shapes, not in change. Comedy is physical first, because physical comedy costs the same to draw as standing still and reads in any language and any dub. Reuse is craft, not laziness: the returning refrain, the returning location and the returning gag are what let the budget go to the one big new thing this episode needs. Write the episode so its emotional turn is legible in behaviour, because a four-year-old reads action long before they read a face.

**Palette:** 11 minutes · 14–18 pages · 1 problem · 4–6 standing locations · 5–7 regulars · 1 new asset · resolved by the child

**Rules:** Budget your locations on page one and do not exceed the bible | Solve it with a character the child already knows, never a guest | Put the problem on screen inside ninety seconds | Make the turn visible as behaviour, not as a face | Reuse a refrain deliberately so the child can join in | Physical gag before verbal gag, always | Never resolve by an adult arriving to fix it | Restore the world at the end — the next episode assumes it | Write the record session, not the picture: if it does not play in a reading, it will not play animated | Ask what one asset this episode is worth building, and spend it there

**Examples:** preschool 11-minute series, 7–11 comedy-adventure blocks, heritage and folktale series for children, YouTube-native kids' series

**Avoid:** Scripts that quietly triple the asset count — a new town, a new vehicle, a crowd — because nobody costed the page. Writing the lesson as a speech instead of a consequence; children hear the register change and disengage on the spot. Jokes that need a specific line reading you have not heard yet, because the record is where they die. Adult-facing irony placed where it steals the child's beat rather than sitting above it. And the flat, safe episode where the character wants nothing until the plot arrives — eleven minutes are too few to spend three on setup.

**The kit (ranked):**

1. **The Story Spine** (Structures) `struct.story_spine`
   Eleven minutes will not carry a loose chain. Every link earns "because of that" or the episode has an inert middle.
2. **Because of That** (Structures) `struct.spine_because`
   The single test to run on the outline before it goes to board, where changes stop being free.
3. **The Flat Arc** (Arcs) `arc.flat`
   A 52-episode order needs characters who do not change, only reveal. This is the design choice, not a fallback.
4. **The Ensemble Grid** (Character) `char.ensemble_grid`
   Fixed cast, fixed contradictions — the grid is what generates fifty-two plots without fifty-two ideas.
5. **The Ensemble as a System** (Relationships) `rel.ensemble_as_system`
   Which pair produces conflict, which produces comfort. Episodes fall out of the wiring.
6. **Comedy in Kids' Content** (Comedy) `comedy.kids_comedy`
   What actually makes a six-year-old laugh, as opposed to what an adult finds charming about children.
7. **Physical Comedy Written for the Page** (Comedy) `comedy.physical_on_page`
   The gag that costs the same to draw as a static shot, survives dubbing into eleven languages, and needs no read.
8. **The Rule of Three** (Comedy) `comedy.rule_of_three`
   Three attempts is the episode's spine at this age, not merely a joke shape.
9. **The Scene Beat Budget** (Beat) `beat.scene_beat_budget`
   Eleven minutes is roughly five to seven scenes. Count them at outline, not at board.
10. **Goal, Conflict, Disaster** (Scene) `scene.goal_conflict_disaster`
    The cheapest reliable scene engine, and cheap matters when every scene is a build.
11. **The Value Turn** (Scene) `scene.value_turn`
    One per episode, expressed in what the character does differently, because the audience cannot read an interior.
12. **Repetition with Variation** (Dialogue) `dial.repetition_variation`
    The refrain that returns with one word changed. The change is the story and the child catches it.
13. **The Kids' Register** (Voice) `voice.kids_register`
    Simple words, unsimplified feeling. Record days punish anything written above the cast's mouth.
14. **Subtext a Child Can Actually Read** (Subtext) `sub.kid_readable_subtext`
    Physical, repeated, never explained by a grown-up in the room.
15. **The Two-Audience Layer** (Subtext) `sub.dual_audience`
    The parent layer, placed above the child's beat rather than inside it.
16. **Rule by Demonstration** (Exposition) `expo.rule_by_demonstration`
    Show the world's rule once in action; a kids' series cannot afford a page of explaining and does not need one.
17. **The Running Gag** (Comedy) `comedy.running_gag`
    In a 52-episode order, the gag that recurs across episodes is a retention device, not a crutch.
18. **Building a Joke That Survives Translation** (Comedy) `comedy.translation_resistance`
    Kids' animation is sold into dozens of territories. A pun-dependent script loses its comedy in every one of them.
19. **The Episode Opening** (Openings) `open.episode_opening`
    Ninety seconds to state the problem, when the viewer may be three years old and the remote is in reach.
20. **The Explained Theme** (Theme) `theme.explained_theme`
    This card names a failure — theme stated aloud instead of dramatised. Preschool and young-skewing kids' series are the real exception: restatement at the close is pedagogy the broadcaster has commissioned, and children of this age genuinely need the idea named once *after* they have seen it. Above about seven it becomes a failure again.

---

**The visual kit (ranked):**

1. **One Subject On A Clean Background** (Composition) `kids.clean_background_subject`
   An eleven-minute episode teaches or tells, and a young viewer cannot do both parsing and following. The clean background is comprehension, not style.
2. **Flat Cel Shading** (Render) `anime.flat_cel_shading`
   Declared once for the series. Fifty-two episodes are made by many hands and the shading rule is what makes them one show.
3. **Layered Background Parallax** (Composition) `kids.bg_parallax`
   The depth a kids' series can actually afford: two or three layers moving at different rates, reused across the whole order.
4. **Squash and Stretch** (Animation) `anime.squash_stretch`
   The physics of the school being drawn. Removed, an eleven-minute episode reads as a slideshow with dialogue on it.
5. **Wide, Clean, Countable** (Composition) `kids.wide_clean_count`
   Inside a teaching or counting beat the wide wins over the tight frame, because the child has to see the objects. This outranks the usual pressure to fill the frame.
6. **Colour Temperature as Mood** (Colour) `color.temperature`
   Stated as palette rather than Kelvin. In kids' work it is also a safety rail: the warm register is where the reassurance lives, and it has to be reachable in every episode.
7. **Eye Level** (Angle) `angle.eye_level`
   At the child's height, not the adult's. A kids' series shot from adult eye level is a series about being looked down at.
8. **Turn to Camera** (Blocking) `block.turn_to_camera`
   The direct address the form is built on, and the beat where the child is asked something and given time to answer.
9. **Cut on Action** (Cuts) `cut.on_action`
   Holds in drawn work and can be tested on the animatic, which is the only stage where a cut is still cheap to change.
10. **Pastel Preschool Palette** (Colour) `color.pastel_preschool`
   Ranked last because it is the default that gets applied without a decision. It suits the youngest band and flattens everything made for the top of the age range.

## Animated Series (adult)

**Constraints:** 22 minutes of content, with scripts running from the high twenties into the forties of pages depending on house style and how much action description the board artists need. The pipeline is the defining fact: nine to fifteen months from table read to delivery, with voice recorded first, animatic second, animation third. Nothing topical survives that gap. There is no reshoot and no coverage — a joke that dies at the animatic is retimed or rewritten and re-recorded, both of which cost weeks. Writers' rooms are standard, and a script passes through table read, punch-up, record, animatic and retake record. Animation lets you draw anything, which means the budget line is not the impossible image but the number of distinct characters and sets in the episode. Streaming orders commonly run 8 to 10 episodes; broadcast blocks still run 13 to 22.

**Grammar:** The engine is character-generated joke density sitting on a plot that closes. Adult animation is comedy with a plot skeleton, not drama with jokes — the A-story must land a real turn or the half-hour reads as stapled sketches. The cast are fixed comic engines whose responses are predictable in kind and unpredictable in specific, which is what makes a twelfth season possible. Jokes are built on the page, in punctuation and word order, because no performer will save a badly ordered line and no editor can fix its timing afterwards. The format licenses the impossible — the visual non sequitur, the cutaway, the scale gag — and that licence is its only real advantage over live-action comedy, so a script that never uses it has chosen the most expensive way to shoot a sitcom. The B-story exists to give the A-story a second angle and to buy a break in joke rhythm.

**Palette:** 22 minutes · 28–45 pages · A-story + B-story · 4–6 regulars · 3–5 jokes per page · 1 impossible image

**Rules:** Kill every topical reference — it ships a year from now | Build the joke on the page, in word order, not in the read | Give each regular a fixed appetite and let the plot poke it | Use one thing live action cannot do, or you are shooting a sitcom the hard way | Close the A-story with an actual turn, not with a joke | Cap distinct sets and speaking parts, and know the number before the table read | Write the cutaway as a paid setup, not as filler | Punch up after the read-through, not before | Make the tonal shift a rule of the show, not an accident of the week

**Examples:** prime-time animated family comedy, streaming adult animated comedy, workplace and genre-parody animated series, late-night 11-minute adult blocks

**Avoid:** Topicality — the single most common wasted page in the format, obsolete before the animatic. Cast bloat, where the room invents four new speaking characters for one runner and the casting and design budget absorbs it silently. Jokes written as attitude rather than as constructed setups, which read fine in the room and die at the table. Ugliness mistaken for edge: the transgressive beat with no target underneath it is expensive noise. And the half-hour with no story at all, where four sketches are stapled to a title card — the audience feels the absence even when individual jokes land.

**The kit (ranked):**

1. **Comic Character Construction** (Comedy) `comedy.comic_character_engine`
   A twelve-season show is not a plot machine, it is six appetites that never resolve. Build the engines first.
2. **Setup and Punchline** (Comedy) `comedy.setup_punchline`
   Density is the format's currency, and every joke is a built object with a load-bearing setup you must actually write.
3. **Comic Timing Written, Not Performed** (Comedy) `comedy.timing_on_the_page`
   The voice record comes before the picture. Timing that exists only in the delivery is timing that does not exist.
4. **The Funny Word Goes Last** (Comedy) `comedy.funny_word_last`
   Word order is the whole of a line's timing when no editor can trim the frames after it.
5. **The Topper** (Comedy) `comedy.topper`
   The beat past the punchline. Adult animation lives on toppers, and it is the first thing a nervous draft cuts.
6. **Escalation and the Comic Spiral** (Comedy) `comedy.escalation_spiral`
   The structure of the 22-minute story: one bad decision compounding, not a series of incidents.
7. **The Straight Man** (Comedy) `comedy.straight_man`
   Without a character measuring the absurdity, the impossible image costs nothing and means nothing.
8. **The Callback Payoff** (Comedy) `comedy.callback_payoff`
   Cheap in animation, enormously effective, and the thing that makes act three feel like a build rather than a stop.
9. **Satire With a Target** (Comedy) `comedy.satire_target`
   The difference between edge and noise is whether something is actually being aimed at.
10. **The Rule of Three** (Comedy) `comedy.rule_of_three`
    The gag shape that holds through the animatic, where looser shapes go slack.
11. **The Never List** (Character) `char.never_list`
    A long-running animated cast is defined by its prohibitions. Break one and the fans notice before the network does.
12. **The Flat Arc** (Arcs) `arc.flat`
    The characters end each episode as they started. Not a limitation — the licence to run a hundred episodes.
13. **The Cold Open** (Openings) `open.cold_open`
    Two minutes that must be funny before the title card, and often the only two minutes a scroller sees.
14. **The Value Turn** (Scene) `scene.value_turn`
    The one thing separating a half-hour from four sketches: something in the A-story actually changes.
15. **The Ensemble as a System** (Relationships) `rel.ensemble_as_system`
    Which pair is funny together and why. The B-story is chosen from this wiring, not invented beside it.
16. **The Wrong-Sized Reaction** (Comedy) `comedy.wrong_reaction`
    Animation draws any magnitude of response at the same cost. Mismatched scale is nearly free here and expensive everywhere else.
17. **The Non Sequitur** (Comedy) `comedy.non_sequitur`
    The format's native licence — the image that has no business existing. Use it deliberately, not as a shrug.
18. **Dark Comedy and Its Rules** (Comedy) `comedy.dark_comedy`
    Adult animation's default register. The rules are what keep it from curdling into contempt.
19. **The Crosscut Sequence** (Sequence) `seq.crosscut_sequence`
    A-story against B-story. Crosscutting is free in animation, and it is how the half-hour manages its joke rhythm.
20. **The Joke That Stops the Story** (Comedy) `comedy.joke_that_stops_story`
    This card names a failure — the gag that halts forward motion. Cutaway-driven adult animation is the genuine exception: some shows contract with the audience that the digression *is* the show and the A-story is a rail to hang it on. That works only if the contract is declared in act one and each digression is a paid setup. Everywhere else in this family, including inside those same shows' finales, it stays a failure.

---

**The visual kit (ranked):**

1. **Flat Cel Shading** (Render) `anime.flat_cel_shading`
   The house style, locked before the first board. Adult animation's identity is almost entirely line and flat colour, and it is decided at series level.
2. **Symmetry** (Composition) `comp.symmetry`
   The deadpan frame. Adult animation's comedy is mostly a composed frame holding still while something absurd is said inside it.
3. **Wide Shot / Long Shot** (Shot size) `size.ws`
   The joke needs the room and the bodies. Drawn coverage is expensive, so the wide has to be the shot that works rather than the shot you cut away from.
4. **Squash and Stretch** (Animation) `anime.squash_stretch`
   Rationed rather than removed. Adult series run a limited-animation budget, so the deformation is saved for the two or three beats an episode where it is the joke.
5. **The Wide Joke** (Cuts) `cut.wide_joke`
   Hold through the joke and cut after it lands, which in animation also saves a drawn reaction nobody needed.
6. **Depth Layers: Foreground, Midground, Background** (Composition) `comp.depth_layers`
   Priced per layer, so the layering is a board decision. Two layers that move well beat four that were drawn because the software allows it.
7. **Colour Temperature as Mood** (Colour) `color.temperature`
   Palette, per sequence. It is the fastest way an adult series signals a register change without animating one.
8. **Eye Level** (Angle) `angle.eye_level`
   The observational register the humour needs. Animation can put the camera anywhere, which is exactly why doing so stops meaning anything.
9. **Reaction Cut** (Cuts) `cut.reaction`
   One drawn reaction, placed correctly, does the work of three. Which face it lands on is the whole editorial decision.
10. **Lighting Change Within a Shot** (Lighting) `light.light_change`
   In flat animation this is a colour change rather than a light change, and it is the cheapest reversal the form has.

## Anime

**Constraints:** A broadcast slot of about 24 minutes, of which roughly ninety seconds of opening and ninety of ending leave around 20 minutes of story, usually split into an A-part and a B-part around a mid-episode eyecatch. The default order is one cour — 12 or 13 weekly episodes inside a three-month broadcast block beginning in January, April, July or October — with a second cour greenlit by the production committee only if discs, streaming and merchandise perform. A 12-episode series routinely takes more than a year end to end. Most series adapt manga or light novels, so the writer's real job is selection and compression: which arc fits twelve episodes, and where it can be made to stop. Key animation is the budget, and the standout episode is a deliberate allocation the rest of the cour pays for with limited animation, held frames and pans.

**Grammar:** Structure runs on turn rather than on conflict — the episode's satisfaction often comes from a reframe that recontextualises what you were watching, not from a protagonist defeating an obstacle. Each episode wants a small closed shape plus one unclosed thread; the cour wants a shape that either resolves at 12 or lands hard enough on an unresolved image to sell the next one. Silence and stillness are dramatic instruments, not gaps — the held reaction shot is the format's signature, and it is also cheap, which is part of why it became the signature. Names, terms and systems arrive fast and the audience will tolerate it, but only if each one is anchored to something concrete when it lands. The A-part establishes and complicates; the B-part turns and closes. Emotion is played under its true size and released once, late.

**Palette:** ~20 story minutes · A-part + B-part · 1 eyecatch · 12–13 episodes per cour · 1 showcase episode · 1 open thread per week

**Rules:** Pick where the cour stops before you write episode one | Give each episode a closed shape and one open thread | Put the turn in the B-part, not the A-part | Anchor every invented term to a concrete object or action the first time it appears | Budget your showcase episode and write the others to afford it | Use stillness as a beat, not as a hole | Underplay the emotional peak and pay it once | Let the opening and ending sequences carry mood so the episode need not | Adapt by cutting, not by compressing everything equally

**Examples:** single-cour seasonal adaptations, original-work anime, shonen and slice-of-life series, streaming-commissioned anime

**Avoid:** Adapting an arc that does not end inside twelve episodes and then stopping mid-air, with no image strong enough to justify it. The proper-noun avalanche in episode one, where six factions and nine honorifics arrive before any of them matter. Spending the animation budget evenly and therefore having no peak at all. Recap padding that eats the B-part. And the reverse mistake — treating the form's stillness as licence for scenes in which nothing turns, which is how a cour grows four dead episodes in its middle.

**The kit (ranked):**

1. **Kishōtenketsu** (Structures) `struct.kishotenketsu`
   The native four-part shape. An anime built on Western three-act conflict often feels translated; this does not.
2. **Ten — the turn** (Structures) `struct.kishoten_ten`
   The third movement, where something unexpected reframes the first two. This is the episode's actual engine.
3. **Ketsu — the reconciliation** (Structures) `struct.kishoten_ketsu`
   The close that makes the turn retroactively inevitable, and the beat most often botched at minute twenty-one.
4. **Sequences in Television Acts** (Sequence) `seq.tv_act_sequence`
   A-part and B-part are two sequences with separate questions. Write them that way and the eyecatch has a job.
5. **The Episode Opening** (Openings) `open.episode_opening`
   After a ninety-second OP, you have seconds to re-establish where the week left off without recapping it.
6. **The Cliffhanger Reveal** (Information) `info.cliffhanger_reveal`
   Weekly broadcast with a seven-day gap. The last twenty seconds are the retention mechanism for the whole cour.
7. **The Serial Clock** (Time) `time.serial_clock`
   Twelve weeks of real time separate episode one from episode twelve. What the audience may forget is a design decision.
8. **Familiar Anchor, One Strange Word** (Exposition) `expo.familiar_anchor`
   How to introduce an invented system without a lore dump: one unfamiliar term inside an entirely familiar action.
9. **The Proper Noun Budget** (Exposition) `expo.proper_noun_budget`
   Episode one has room for about three names that matter. Adaptations routinely spend fifteen.
10. **Coined Term in Context** (Exposition) `expo.coined_term_in_context`
    The technique that lets an audience absorb a magic system by watching it used rather than hearing it described.
11. **Understate at the Peak** (Emotion) `emo.understate_at_peak`
    The form's emotional signature. The held, quiet reaction lands harder than the shout and costs a fraction of the frames.
12. **The Beat of Silence** (Beat) `beat.silent_beat`
    Stillness is a written beat in anime, deliberately placed. Limited animation made it necessary; the form made it beautiful.
13. **Emotion Through Task** (Emotion) `emo.emotion_through_task`
    Cooking, walking, cleaning, repairing — the anime scene that carries feeling through ordinary physical work.
14. **The Set Piece** (Sequence) `seq.set_piece`
    Your showcase episode. Choose it at outline, because it determines what the other eleven can afford.
15. **The Breather Sequence** (Sequence) `seq.breather_sequence`
    The beach episode, the festival episode. Structurally load-bearing, not filler, and where the cast is actually built.
16. **The Physical Signature** (Character) `char.physical_signature`
    A cast of twelve read at a glance by silhouette and one repeated gesture. A design requirement, not a flourish.
17. **The Opponent Is Right About Something** (Antagonist) `anta.right_about_something`
    The format's most durable antagonist shape, and the reason its villains get quoted for decades.
18. **The Thematic Motif** (Theme) `theme.thematic_motif`
    A returning image across twelve episodes — how a cour feels unified despite episodic plots.
19. **The Season Ending** (Endings) `end.season_ending`
    Episode 12 must close enough to satisfy and open enough to justify a committee funding cour two.
20. **The Positive Change Arc** (Arcs) `arc.positive_change`
    Twelve episodes is precisely enough for one genuine change in one character. Attempt it for three and you get none.

---

**The visual kit (ranked):**

1. **Flat Cel Shading** (Render) `anime.flat_cel_shading`
   The baseline the whole vocabulary sits on, and the thing every other card here modifies rather than replaces.
2. **Silhouette Action Against Flat Colour** (Animation) `anime.silhouette_flat_action`
   The form's answer to an action beat it cannot afford to animate in full - and it reads as a stylistic choice rather than as an economy, which is why it survived.
3. **The Beam Clash** (Animation) `anime.beam_clash`
   The held confrontation the A-part builds to. It is a structural beat in this format, not an effect.
4. **Bloom on the Hair** (Render) `anime.bloom_hair`
   One of the few places the form spends light, and it is spent on the character rather than the scene - which is the whole of anime's priority order.
5. **Talking Heads with a Background Pan** (Composition) `anime.talking_heads_bg_pan`
   Twenty minutes of story on a broadcast budget: the pan is how a dialogue scene keeps moving without animating anyone.
6. **Squash and Stretch** (Animation) `anime.squash_stretch`
   Held to the impact frames. Anime's limited animation makes the deformed frame an event, which is why it hits harder here than in full animation.
7. **Low Angle** (Angle) `angle.low`
   The stance shot, and the reason it works is that the surrounding twenty minutes are level. A series angled throughout has no arrival.
8. **Extreme Close-Up** (Shot size) `size.ecu`
   The eye. It is the form's punctuation mark and it is placed on the beat before the turn, not on the turn.
9. **Colour Temperature as Mood** (Colour) `color.temperature`
   The A-part and B-part split is often carried by palette alone, which is the cheapest structural signal the format has.
10. **Flashback Desaturation** (Colour) `anime.flashback_desaturation`
   Ranked low because it is the most automatic choice in the form. It works, and it works so reliably that it stops being read as a decision.

## Short Animation

**Constraints:** Festivals define a short generously — Annecy accepts up to 59 minutes 59 seconds, and its graduation category runs 2 minutes to 29 minutes 59 seconds — but programmers build blocks, and a block wants films of 5 to 12 minutes. A 15-minute short with a 7-minute idea is rejected by curation, not by jury. Annecy 2026 selected 141 shorts from 43 countries across seven competitive sections; at that ratio the first two minutes are what a selection committee actually watches. Production is often a single artist or a tiny team over one to three years, or a graduation film against a school deadline. There is usually no money for dialogue recording, none for crowds, and none to fix a structural mistake discovered at animatic. Many shorts travel to non-English festivals, which makes dialogue a distribution liability.

**Grammar:** One idea, fully executed, ending on an image. A short animation is closer to a poem than to a small film: it establishes a rule or a world, runs one complication through it, and turns. It has no room for a second character with a want, and usually none for a second location. Because the medium is drawn, the world's logic can be stated visually in the first fifteen seconds and the whole film can then live inside it — the one structural advantage animation holds over live-action shorts, and the reason shorts are where the form's real innovation happens. The final frame does more work than the final line. Silence, or music with no dialogue, is the default rather than the exception, and it roughly doubles the festival circuit available to the film.

**Palette:** 5–12 minutes · 1 idea · 1–2 characters · 1–2 locations · no dialogue · 1 final image

**Rules:** State the world's rule in the first fifteen seconds, visually | Cut to one idea and execute it completely | Write the last frame before you write the middle | Prefer no dialogue — it doubles the festivals you can enter | Give the film one object and let it carry the meaning | Put the turn at roughly two-thirds, not at the end | Do not explain the ending inside the film | Count your locations; each one is weeks of your own life | Make the first ninety seconds survive a committee watching at speed

**Examples:** Annecy and Ottawa competition shorts, graduation films, commissioned art shorts, anthology and streaming short-form animation

**Avoid:** The short that is really a feature's first act, which programmers identify in thirty seconds. Dialogue written because the story was structured like a live-action scene — it subtitles badly, dubs worse, and usually exists to explain something the image already said. The ending that arrives twice, once as an image and again as a caption. Padding to reach a length someone told you was standard; a five-minute film in competition beats a nine-minute version of itself. And the technically dazzling piece with no turn, which wins craft prizes and is forgotten by the next block.

**The kit (ranked):**

1. **Sequence as Short Film** (Sequence) `seq.short_film_model`
   A short is one sequence with a complete shape, not a compressed feature. Get this right and the rest follows.
2. **Kishōtenketsu** (Structures) `struct.kishotenketsu`
   The four-part turn shape, which is what most great animated shorts actually are, whatever the maker called it.
3. **The Controlling Idea** (Theme) `theme.controlling_idea`
   One sentence. If the film cannot be reduced to one, it is two films, and the block has room for one.
4. **Opening Image, Answered** (Openings) `open.opening_image_answered`
   First frame and last frame as a rhyme. In a wordless short this is the entire architecture.
5. **The Final Image** (Endings) `end.final_image`
   The frame that *is* the film's meaning. Write it first; everything upstream is construction toward it.
6. **The Value Turn** (Scene) `scene.value_turn`
   One turn, placed around two-thirds. A short without one is an exercise, however beautiful.
7. **The Rule of the World** (Openings) `open.rule_of_the_world`
   Animation's cheapest superpower: fifteen seconds of image establishes a physics the whole film then obeys.
8. **Worldbuilding by Implication** (Exposition) `expo.implication_worldbuilding`
   The short has no room to explain, and every explained thing costs a shot you needed for the turn.
9. **The Iceberg Principle** (Exposition) `expo.iceberg_principle`
   The constructed world the audience feels and never sees. This is what makes a six-minute film feel large.
10. **The Object That Carries It** (Emotion) `emo.object_carrier`
    With no dialogue, an object is your only reliable vehicle for interior state.
11. **The Object Opening** (Openings) `open.object_opening`
    Open on the thing, not the character. A programmer's attention is on the frame before it is on the person.
12. **The Specific Detail** (Emotion) `emo.specific_detail`
    One precisely observed detail buys more feeling in a wordless film than any amount of expression animation.
13. **Ellipsis** (Time) `time.ellipsis`
    The cut that removes the years. Shorts live on ellipsis, and audiences fill it faster than makers expect.
14. **Non-Human Viewpoint** (POV) `pov.nonhuman_pov`
    Animation is the only form where this is free, and the short is where it is actually worth doing.
15. **The Held Final Beat** (Endings) `end.held_final_beat`
    Hold the last image past comfort. Two extra seconds is the difference between an ending and a stop.
16. **The Iceberg** (Subtext) `sub.iceberg_omission`
    What you leave out. In a form this short, omission is the primary compositional act.
17. **The Wrongness Detail** (Tension) `tens.wrongness_detail`
    One thing slightly off in an ordinary frame. Cheaper than a monster and far more durable.
18. **The Plant and the Payoff** (Information) `info.plant_and_payoff`
    In six minutes a single plant can be set, forgotten and paid, and that arc is most of what a short short has room for.
19. **The Open Ending** (Endings) `end.open_ending`
    Legitimate here in a way it rarely is at feature length — but open means unresolved, not unfinished.
20. **Withhold the Reaction Shot** (Emotion) `emo.withhold_reaction`
    Stay on the object or the empty room instead of cutting to the face. Cheaper to animate and far stronger, and it is what stops a wordless short from over-explaining its own ending.

---

**The visual kit (ranked):**

1. **Flat Cel Shading** (Render) `anime.flat_cel_shading`
   One look, declared, and no second register. A short animation that changes style mid-way has spent its only structural signal on decoration.
2. **Frame Within a Frame** (Composition) `comp.frame_within_frame`
   Establishes by implication, which is all a short animation has time for and all a drawn frame needs.
3. **Negative Space** (Composition) `comp.negative_space`
   The most economical thing an animator can draw, and the most expressive. An empty half-frame costs nothing per frame and states an absence.
4. **Squash and Stretch** (Animation) `anime.squash_stretch`
   The form's argument for existing. A short animation that could have been filmed has not used the medium.
5. **Colour Temperature as Mood** (Colour) `color.temperature`
   One shift, on the turn. Palette is the fastest structural tool a wordless short has.
6. **Wide Shot / Long Shot** (Shot size) `size.ws`
   The world in one drawing. Draw it once, well, and the audience carries it for the rest of the film.
7. **Layered Background Parallax** (Composition) `kids.bg_parallax`
   Depth for the price of two layers, which is the depth a festival short can actually afford.
8. **Extreme Close-Up** (Shot size) `size.ecu`
   The single object the whole short turns on. In a drawn film it can be the only fully rendered thing in the piece.
9. **Silhouette Lighting** (Lighting) `light.silhouette`
   Shape without detail: the cheapest frame to produce and often the strongest image in the film.
10. **Cut on Action** (Cuts) `cut.on_action`
   Tested on the animatic, where a short's entire structure can still be rebuilt in an afternoon.

## Stop Motion and Craft Animation

**Constraints:** The hardest schedule in animation. Laika's stated target is around 4.3 seconds of finished animation per animator per week, with real output often nearer 3; on *ParaNorman* each animator carried roughly four seconds a week. A feature takes years, and a single complex shot can absorb a week of motion-control setup before a frame is exposed. Everything is physical: a set is built, a puppet is fabricated, a replacement-face library is printed, a location is a table in a studio with a floor an animator stands on. A rewrite after build is not a rewrite, it is a construction request. Crowds are expensive in a way no other animation form is, because each body in frame is an object someone made by hand. Lighting cannot change between shooting days without visible continuity breaks.

**Grammar:** Write for the hand. The form's entire claim on an audience is tactility — the fingerprint in the clay, the seam in the fabric, the sense that someone touched this — so the script's job is to give physical work to the hands and physical texture to the world. Scenes are built around objects and tasks, because objects and tasks are what the medium renders best and CG renders worst. Set count is the budget line, so a stop-motion script consolidates relentlessly: two conversations become one, three locations become one room used three ways. Speed is expensive and stillness is cheap, which inverts the usual economics and pushes the form toward dread, ritual and held tension rather than action. Dialogue is costly in replacement faces, which is why good stop motion talks less than its scripts originally did.

**Palette:** 3–4 seconds per animator-week · 1 set used three ways · objects over faces · tasks over speeches · stillness as tension · no crowds

**Rules:** Consolidate locations before you consolidate anything else | Give every scene a physical task the hands can perform | Cut a crowd to three figures and a sound | Lock the script before the build — after fabrication, changes are demolition | Write the object that carries the film and put it in the first scene | Use stillness and slowness; this medium makes them read as deliberate, not dead | Budget dialogue by face count, not by page count | Write ritual and repetition, which this medium performs better than any other | Merge any two scenes that share the same value turn

**Examples:** stop-motion features, puppet and clay shorts, cut-out and paper animation, mixed-media craft animation, model-animation title sequences

**Avoid:** The action sequence written as if it were CG — a chase across four sets is a year nobody has. Crowd scenes, which read fine on a page and cost a fabrication department its sanity. A script that adds a location for one line of dialogue; that line belongs in the room you already built. Late structural notes, which in this medium arrive after the puppets exist and are therefore not notes but demolition. And underwriting the tactile: a script that could just as well be shot in live action has thrown away the only reason to shoot it this way.

**The kit (ranked):**

1. **Merge Two Scenes** (Scene) `scene.merge_two_scenes`
   The most valuable technique in this format. Every merge is a set you do not build and weeks you get back.
2. **Transplant the Scene** (Scene) `scene.transplant`
   Move the scene into a set you already have. The scene almost always improves, and it costs nothing.
3. **Emotion Through Task** (Emotion) `emo.emotion_through_task`
   Hands doing work. This is what the medium is for, and the scene type it performs better than any other.
4. **The Physical Beat** (Beat) `beat.physical_beat`
   Beats expressed as movement rather than line. In a form that animates bodies frame by frame, this is the native unit.
5. **What the Hands Are Doing** (Subtext) `sub.hands_business`
   Puppet hands are the most articulated thing in frame. Write for them and the subtext plays without a word.
6. **The Object That Carries It** (Emotion) `emo.object_carrier`
   An object in stop motion is a real object somebody made. It carries a weight no rendered prop can.
7. **The Object as Confession** (Subtext) `sub.object_as_confession`
   The thing handled, turned over, put down. Cheaper than dialogue and truer.
8. **Theme Carried by an Object** (Theme) `theme.object_carrier`
   One object threaded through the film — and in this medium the audience believes in its physical existence.
9. **The Scene Beat Budget** (Beat) `beat.scene_beat_budget`
   Beats are seconds and seconds are animator-weeks. Counting beats here is literally counting money.
10. **Absorb and Delete** (Scene) `scene.absorb_and_delete`
    Fold a scene's function into an adjacent scene and cut it. In stop motion this is the highest-value pass you can run.
11. **The Interrupted Ritual** (Scene) `scene.interrupted_ritual`
    The medium performs repeated physical process beautifully, which makes breaking one devastating.
12. **Corrupting the Mundane** (Tension) `tens.corrupting_the_mundane`
    Why stop motion is natively unsettling — familiar objects, moved by nobody. Write toward it, not against it.
13. **The Beat of Silence** (Beat) `beat.silent_beat`
    Stillness costs almost nothing here and reads as intent rather than as a gap.
14. **Environmental Exposition** (Exposition) `expo.environmental_detail`
    The set is a handmade object the audience will study. Put the information in it and delete the dialogue.
15. **The Object That States the Rule** (Exposition) `expo.object_tells_rule`
    A built prop can declare a world's law in one shot — exactly the kind of shot this medium excels at.
16. **The Physical Signature** (Character) `char.physical_signature`
    Puppets are read by silhouette and gait. Specify the movement signature in the script and the fabricators will build to it.
17. **Silence as Reply** (Dialogue) `dial.silence_as_reply`
    Every line of dialogue is a face library. The unanswered line is free and usually stronger.
18. **The Sequence Unit** (Sequence) `seq.sequence_unit`
    Think in sequences, because sequences map to shooting units, stages and crews in a way scenes do not.
19. **Iterative Time** (Time) `time.iterative_habit`
    The thing that happens every day, shown once. Reuses a built set and buys months of story time for one shot.
20. **The Choreography List** (Beat) `beat.choreography_list`
    This card names a failure — action written as a list of physical moves with no exchange underneath. Stop motion is the narrow exception, and only in one place: in a purely physical sequence with no dialogue, the animation director genuinely needs the move-by-move breakdown on the page, because there is no coverage and no second take. Write the list *and* keep the tactic underneath it. In any scene with dialogue it remains a failure here as everywhere.

---

**The visual kit (ranked):**

1. **Contact Shadow and Ground Truth** (Materials) `material.contact_and_shadow`
   The whole illusion. A puppet that is not convincingly resting on the surface reads as a puppet, and nothing later in the pipeline repairs it.
2. **Stop Motion Cadence** (Time) `time.stop_motion`
   The slightly uneven rhythm and the held extremes are what make it read as made by hand. Smoothed out, the format loses the only thing it has that nothing else does.
3. **Motivated Lighting** (Lighting) `light.motivated`
   Three seconds of finished animation a week means a lighting setup stands for days. It has to be right at build, because relighting costs the shot.
4. **Depth Layers: Foreground, Midground, Background** (Composition) `comp.depth_layers`
   Built physically rather than composited, so the layering is a set-construction decision made before a frame is shot.
5. **Surface Material and Its Imperfections** (Materials) `material.drape_weight`
   Cloth on a puppet moves at puppet scale and looks wrong doing it. The weight of the fabric is a casting decision, not a finishing one.
6. **Macro Lens** (Lens) `lens.macro`
   The format's native register. The audience is being invited to see that the thing is real and small, and the macro is the invitation.
7. **Shallow Depth of Field** (Lens) `lens.shallow_dof`
   Here it is doing real work rather than decorating: it sells scale, because a miniature shot deep looks exactly like a miniature.
8. **Eye Level** (Angle) `angle.eye_level`
   At the puppet's height. The commonest error in the form is a camera at human eye level looking down at a world built at ten inches.
9. **Lighting Ratio** (Lighting) `light.ratio`
   A handmade set holds a hard ratio better than a real one does, because every surface was chosen. It is the format's most underused strength.
10. **Cut on Action** (Cuts) `cut.on_action`
   Decided on the animatic and never after. At three seconds a week, a cut discovered in the edit is a week of somebody's life.

## Motion Graphics and Explainer Animation

**Constraints:** 60 to 90 seconds is the commercial default for an animated explainer, with 30-second cutdowns for paid social. English voice-over lands at roughly 140 to 150 words per minute, so a 90-second explainer is about 220 words of script — under one page. Push past about 180 wpm and the read audibly rushes. The script is written first and the animation is built to it frame by frame, so every word added is seconds of motion someone must design. Revision rounds are contractually capped, usually at two or three, and a script change after animatic is a change order. There is a client, the client has a legal team, and claims in the voice-over must survive that review. Most of this work autoplays muted in a feed, which makes on-screen text and captions the primary channel rather than an accessibility extra.

**Grammar:** One promise, made in the first five seconds and kept in the last five. The form is an argument with a shape: here is the situation you recognise, here is the friction in it, here is the mechanism that removes the friction, here is what to do next. Abstraction is the enemy, because motion graphics are literally pictures of nouns — every abstract phrase is either an unbuildable shot or a generic one. Each sentence should be a thing that can be drawn. Rhythm is the script's only performance tool: sentence length controls tempo, and the voice artist will breathe where your punctuation tells them to. The strongest explainers name a specific number or a specific object early, because specificity is what separates this from every other video in the feed.

**Palette:** 60–90 seconds · ~220 words · 140–150 wpm · 5-second promise · 1 mechanism · 1 call to action · muted-first

**Rules:** Write the promise in the first sentence and keep it in the last | Budget words, not pages — count them and read aloud against a stopwatch | Every sentence must name something that can be drawn | Replace every abstract noun with a concrete one or cut the sentence | Explain one mechanism; do not list three features | Write the on-screen text as its own layer, because most viewers hear nothing | Vary sentence length deliberately; it is your only pacing control | Cap jargon at the terms the viewer will meet again | End on the single action you want taken | Run the deletion test on every sentence before the client does

**Examples:** SaaS product explainers, animated brand films, onboarding and training modules, public-information animation, data and process motion graphics

**Avoid:** The feature list disguised as a story, which tests badly and is the thing clients ask for by default. Abstract voice-over over abstract imagery — "empowering seamless collaboration" is not a shot, and the animator will deliver floating geometric shapes because you gave them nothing else. Overwriting to 300 words and asking the voice artist to read fast, which destroys comprehension for the sake of a word count nobody outside the room cares about. A script that assumes sound, when most impressions are muted. And the ending that trails off without an action, wasting the only ninety seconds of attention the product will get.

**The kit (ranked):**

1. **The Explainer Scaffold** (Exposition) `expo.explainer_scaffold`
   The form's load-bearing structure: recognition, friction, mechanism, action. Everything else here sits on it.
2. **Need-to-Know Ladder** (Exposition) `expo.need_to_know_ladder`
   Order the information by what the next sentence requires. Ninety seconds does not survive a wrong order.
3. **Short-Form Front-Loading** (Exposition) `expo.short_form_frontload`
   The promise goes in the first five seconds, before the viewer decides. Everything else is negotiable.
4. **The Stated Promise** (Openings) `open.stated_promise`
   Say what the viewer will know by the end. In paid media this is what buys the remaining eighty seconds.
5. **The Deletion Test** (Exposition) `expo.deletion_test`
   Cut the sentence and see whether anything breaks. At 220 words this removes a third of most first drafts.
6. **Concrete Nouns Over Abstract** (Rhythm) `rhythm.concrete_nouns`
   The highest-leverage rule in motion graphics: an abstract noun is an unanimatable shot.
7. **Rhythm in Voice-Over and Audio** (Rhythm) `rhythm.vo_breath_line`
   You are writing one breath at a time. Punctuation is a performance instruction the artist will obey literally.
8. **Sentence Length as Tempo** (Rhythm) `rhythm.length_as_tempo`
   Your only pacing control. Length sets the read speed, which sets the animation's cutting rhythm.
9. **Short, Short, Long** (Rhythm) `rhythm.short_short_long`
   The pattern that makes a 220-word script feel designed instead of recited.
10. **Rule by Demonstration** (Exposition) `expo.rule_by_demonstration`
    Show the mechanism working, once. This is the shot the whole video exists to deliver.
11. **The Jargon Threshold** (Exposition) `expo.jargon_threshold`
    How many unfamiliar terms an audience carries in ninety seconds. A smaller number than the client believes.
12. **The Proper Noun Budget** (Exposition) `expo.proper_noun_budget`
    Product names, feature names, tier names. Spend three; every one after that is dead weight.
13. **Coined Term in Context** (Exposition) `expo.coined_term_in_context`
    If the brand insists on its invented word, this is how to make it stick rather than bounce off.
14. **Authority by Specificity** (Voice) `voice.authority_by_specificity`
    One real number or one exact object does more for credibility than every superlative in the brief.
15. **Verb Strength and the Passive** (Rhythm) `rhythm.verb_load`
    Passive constructions are the default register of corporate copy, and they have no picture attached.
16. **The Confiding Voice** (Voice) `voice.confiding_voice`
    The register that works here — one person explaining to one person, not a brand addressing a market.
17. **Rhythm in Captions and Subtitles** (Rhythm) `rhythm.subtitle_beat`
    Autoplay is muted. Your captions are the script for most of the audience, and they have their own rhythm.
18. **Diegetic Text** (Exposition) `expo.diegetic_text`
    On-screen words as part of the design, carrying what the voice-over should not have to say twice.
19. **Answer the Question That Was Asked** (Endings) `end.answer_the_question_asked`
    The close must resolve the promise made at second five, not pivot into a different sell.
20. **Theme in Non-Fiction** (Theme) `theme.theme_in_nonfiction`
    Even a product explainer has a controlling idea. The ones that get remembered are the ones where it was chosen.

---

**The visual kit (ranked):**

1. **Build It, Do Not Generate It** (Data) `dataviz.build_do_not_generate`
   Ranked first because it is the one that stops the piece being wrong. A chart assembled from real values is a chart; a chart asked for from a generator is plausible nonsense with numbers on it.
2. **Pick the Chart from the Question** (Data) `dataviz.chart_from_the_question`
   The form is an argument made in shapes. Choose the shape from the sentence you are proving, not from what the data happens to look like.
3. **Colour That Carries Meaning** (Data) `dataviz.colour_encodes_one_thing`
   In sixty seconds a viewer can learn one colour code. Two codes is a piece that has to be watched twice.
4. **Never Colour Alone** (Access) `access.not_colour_alone`
   Roughly one viewer in twelve has a colour vision deficiency, and an explainer that encodes its only distinction in hue has excluded them silently.
5. **The Transition Is the Argument** (Data) `dataviz.transition_is_the_argument`
   In motion graphics the movement between two states is the claim. A transition chosen for smoothness rather than for meaning argues something nobody checked.
6. **Symmetry** (Composition) `comp.symmetry`
   The layout grammar the form reads fastest, and the one that survives being cut to a square and a vertical for paid social.
7. **Legible at the Size It Is Actually Watched** (Access) `access.legible_at_size`
   Most of this is watched on a phone in a feed. Type judged on the editing monitor is type the audience never read.
8. **Negative Space** (Composition) `comp.negative_space`
   An explainer's density is its main failure mode. The empty area is what gives a viewer somewhere to put the last idea while the next arrives.
9. **Text Safe Zone Planned in the Image** (Text) `textimg.text_safe_zone`
   Cut once, delivered at sixty, thirty and fifteen seconds in three ratios. Type placed without the reframes in mind survives one of them.
10. **Sound Sync** (Sound) `vertical.sound_sync`
   Every element that enters carries its own sound, placed slightly early. It is what raises the perceived value of a piece whose visuals are deliberately simple.

## Coverage

6 kits: Animated Series (kids), Animated Series (adult), Anime, Short Animation, Stop Motion and Craft Animation, Motion Graphics and Explainer Animation.

## Sources

Verified 2026-09-17.

- [Page count for animation scripts — John August](https://johnaugust.com/2004/page-count-for-animation-scripts)
- [How Long is a TV Show Script — Half-Hour and Hour Formats — StudioBinder](https://www.studiobinder.com/blog/how-long-is-a-tv-show-script/)
- [How to Launch a Kids Animated Series in 2026 — Whizzy Studios](https://www.whizzystudios.com/post/how-to-launch-a-kids-animated-series-in-2026)
- [You Asked For It: Structure and Format in Animation Writing — Canimation](https://canimation.wordpress.com/2010/03/27/you-asked-for-it-structure-and-format-in-animation-writing/)
- [How Writing Animation Differs From Live Action — Andy Guerdat, Film Courage](https://medium.com/film-courage/how-writing-animation-differs-from-live-action-andy-guerdat-3ec5f12c6ac8)
- [Anime Format — At a Glance Anime](https://ataglanceanime.com/2019/07/15/anime-format/)
- [12-Episode Anime — TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/TwelveEpisodeAnime)
- [Cour: A Definition of the Term as It Relates to Anime — LiveAbout](https://www.liveabout.com/the-origins-of-cour-144802)
- [Anime Production Process Explained — ViewersPoint](https://viewerspoint.com/anime/anime-production-process/)
- [How does Laika produce stop motion animation? — DeeDee Studio](https://www.deedeestudio.net/en/post/laika-produce-stop-motion-animation)
- [Two Years in the Making — Focus Features](https://www.focusfeatures.com/article/two__years_in_the_making)
- [Behind the scenes with Aardman Animation's stop-motion team — The Kid Should See This](https://thekidshouldseethis.com/post/aardman-animation-robin-robin-stop-motion-bts-video)
- [Explainer Video Length: How Long Should It Be? (2026) — Yum Yum Videos](https://www.yumyumvideos.com/blog/explainer-video-length/)
- [How Many Words Do You Need for a 60-Second Video Script? — Breadnbeyond](https://breadnbeyond.com/articles/how-many-words-does-a-60-seconds-explainer-video-needs/)
- [Ideal Word Count for a 1 Minute Video Script — Verstiuk](https://verstiuk.com/blog/ideal-word-count-one-minute/)
- [Annecy Festival Short Animation Film Selections 2026 — Zippy Frames](https://www.zippyframes.com/festivals/annecy-short-animation-selections-2026)
- [Annecy 2026 Official Short Film Selections Announced — Animation World Network](https://www.awn.com/news/annecy-2026-official-short-film-selections-announced)
- [Submit a film — Annecy Festival HelpDesk](https://helpdesk.annecyfestival.com/en/category/submit-a-film-112ytul/)
