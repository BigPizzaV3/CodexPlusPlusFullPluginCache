# Structure systems

The competing whole-story frameworks, and every one of their beats as an addressable card.

There is no equivalent file in the Visual Creativity Database, because the camera has no whole-story layer. This is the top of the writing ladder: `STORY → ACT → SEQUENCE → SCENE → BEAT → LINE`.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [How to use this file](#how-to-use-this-file)
- [A. Three-Act Paradigm](#a-three-act-paradigm)
- [B. Save the Cat Beat Sheet](#b-save-the-cat-beat-sheet)
- [C. Story Circle](#c-story-circle)
- [D. The Hero's Journey](#d-the-heros-journey)
- [E. The 22 Building Blocks](#e-the-22-building-blocks)
- [F. The Sequence Approach](#f-the-sequence-approach)
- [G. Freytag's Pyramid](#g-freytags-pyramid)
- [H. Kishōtenketsu](#h-kishōtenketsu)
- [I. The Story Spine](#i-the-story-spine)
- [J. Four-Act Structure](#j-four-act-structure)
- [K. McKee's Story Hierarchy](#k-mckees-story-hierarchy)
- [Coverage](#coverage)
- [Sources](#sources)

<!-- /GENERATED:toc -->

## How to use this file

**These systems disagree with each other, and that is the most important fact in this file.** Each defines story around a different primary unit: Campbell around myth, McKee around conflict, Truby around moral need, Snyder around visible plot events. A draft built on two of them at once produces notes that contradict each other — a Snyder midpoint asks for a false victory at page 55, a Truby second revelation asks for an obsessive change of motive, and a writer trying to satisfy both writes a scene that does neither.

**Choose one system per project.** Read the others to steal a diagnostic, never to run two spines.

Two card types live here:

- **System cards** carry the full eight fields plus a beat list. Id form: `struct.<system>`
- **Beat cards** are compact: what the beat does, how it fails, and its id. A beat has no independent format or genre tags, because it inherits them from its system. Id form: `struct.<system>_<beat>`

---

## A. Three-Act Paradigm

### Pick the System, Then Take Its Beats

**Also called:** the structure selector, system before beats, which spine is this
**What it is:** The card at the head of the `struct.` shelf. It does not describe a shape. It asks the two questions the shelf's own pair graph asks over and over — **what moves this story forward, and how big is the piece the audience takes in one go** — and hands back a named shortlist of whole-story systems. **It routes to systems only, never to beats**, and that is not an editorial preference: 97 of the 110 beat entries in `structures.md` are filed `additive` in `PAIR-AUDIT.md`, not one of them carries `Avoid when:`, `Best in:` or `Yields to:`, and `structures.md` says in its own preamble that *a beat has no independent format or genre tags, because it inherits them from its system.* A beat inside Save the Cat is not an alternative to a beat inside Three-Act. You choose the system; the beats arrive with it, in its order, already named on its card's `**The beats:**` line.
**Effect on the audience:** None. This card never reaches the page. It exists so that the one system a project runs on was chosen against the engine and the runtime, rather than adopted because it is the one the writer last read about.
**Used for and where it works best:** Answer both questions **out loud, in one sentence each, before you open `structures.md`** — and answer them at the start of the project, because `structures.md`'s own first rule is *choose one system per project; read the others to steal a diagnostic, never to run two spines.* Two answers give a cell of one to five systems. Where the two answers land in an empty cell, that is a real finding about the shelf and not about your story — see **The unasked**. Run `struct.mckee_hierarchy` alongside whatever you choose rather than instead of it; it is filed `additive` for the reason its own card gives, that it measures scale rather than sequence and is *the one system worth learning in addition*.
**Best in:** formats: all | genres: all
**Avoid when:** **The structure was already chosen for you and this map only invites you to relitigate it** — a commissioned script whose notes will arrive in three-act vocabulary, a network act map, a series bible. There the decision was made before you arrived and re-opening it costs you the draft. Also avoid it **on a broken draft**: this map hands you a whole second system, when what a stalled script usually needs is `struct.mckee_hierarchy` measuring the one it already has — and because that card is `additive` it appears under no value here, so the map will silently send a diagnostic problem to a generative answer. And **distrust the map entirely once you are past the outline.** It chooses the spine and then falls silent: the 98 beats are its payload, not its output, so if the question you are actually holding is *where in the beat list does this scene go*, this card has nothing to say and will answer anyway.
**Example:**
> *A 30-second heritage spot about a shoemaker whose street changed around him.*
> Question 1 — what moves it? Nothing opposes anything; the photograph reframes the man. **Adjacency.**
> Question 2 — how big, and do they get out? Thirty seconds, taken whole. **One sitting, you set the length.**
> The cell holds three: `struct.kishotenketsu`, `struct.flash_fiction`, `struct.unity_of_effect`. It is a moving picture, so the first governs and the third is run over it as a cutting rule.

---

**The axes**

**Twelve `Yields to:` conditions exist on this shelf and they fall into exactly two clusters of four, plus four singletons.** That measurement is why there are two questions here and not three. The count:

| Cluster | Conditions | The cards carrying them |
| :--- | ---: | :--- |
| **What drives it** | 4 | `struct.three_act`, `struct.save_the_cat`, `struct.truby_22`, `struct.kishotenketsu` |
| **How big the unit is** | 4 | `struct.sequence_approach`, `struct.story_spine`, `struct.linked_collection`, `struct.unity_of_effect` |
| Singletons (leaves) | 4 | `struct.story_circle`, `struct.heros_journey`, `struct.freytag`, `struct.four_act` |

**Axis 1 — What moves this story forward: something opposing, something lacking, or nothing at all?**
Asked first, because it is the only condition on the shelf written in **both directions**, which is the mark of a real fork rather than a preference. `struct.three_act` yields away on *"Accumulation, mood or simultaneity instead of escalation"*; `struct.save_the_cat` yields away on *"Non-Western tradition; development without conflict"*; and `struct.kishotenketsu` yields straight back on *"Material is genuinely a contest, or commissioner expects acts."* The fourth condition splits the opposing half in two: `struct.truby_22` yields to `struct.save_the_cat` on *"No moral question: spectacle, procedural, brand film"* — the exact boundary between a story driven by an external problem and one driven by the protagonist's own lack.

**Axis 2 — How big is the piece the audience takes in one go, and do they get out in the middle?**
Four conditions, and all four are about the size and separability of the consumed unit rather than about content: *"Short formats; eight sequences become arithmetic"* (`struct.sequence_approach`), *"Finished long-form structure; stems will not hold a feature"* (`struct.story_spine`), *"Work too long to read at one sitting"* (`struct.unity_of_effect`), *"Linkage too tight; stories cannot stand alone"* (`struct.linked_collection`). The first two are the same boundary approached from opposite sides, which is the cleanest evidence on the shelf that this is a fork and not a filter. Cross-checked against `Avoid when:`, which gives the floor from below — `struct.flash_fiction` stops where *"the idea needs accumulated time."*

**The four leaves, and what they are good for.** Each separates one or two cards, so none is promoted to a question. They are tie-breakers **inside** a cell and that is where they are used:

| Leaf condition | From | Breaks the tie between |
| :--- | :--- | :--- |
| *"Ensemble with no single traveller"* | `struct.story_circle` | Sends the reader **off this shelf** to `rel.ensemble_as_system` |
| *"Small, compromised or comic story; monomyth inflates it"* | `struct.heros_journey` | `struct.heros_journey` and `struct.story_circle` |
| *"Contemporary screen work; climax belongs near the end"* | `struct.freytag` | `struct.freytag` and `struct.three_act` |
| *"Passivity is the point: tragedy, literary adaptation"* | `struct.four_act` | `struct.four_act` and `struct.freytag` |

---

**The map**

**Axis 1 — what moves it forward**

| Answer | The shortlist, by id |
| :--- | :--- |
| **An external problem that escalates — something is wrong, and pressure applied to it makes it worse** (7) | `struct.three_act` · `struct.save_the_cat` · `struct.sequence_approach` · `struct.four_act` · `struct.freytag` · `struct.freytag_climax` · `struct.story_spine` |
| **The protagonist's own lack — the opposition exists to attack it, and the story is a becoming** (3) | `struct.truby_22` · `struct.heros_journey` · `struct.story_circle` |
| **Nothing opposes — the parts sit beside each other and the turn is a change in what is understood** (4) | `struct.kishotenketsu` · `struct.flash_fiction` · `struct.unity_of_effect` · `struct.linked_collection` |

**Axis 2 — how big the unit is, and whether they get out**

| Answer | The shortlist, by id |
| :--- | :--- |
| **One sitting, taken whole, and the length is yours to set — fifteen seconds to an hour** (5) | `struct.kishotenketsu` · `struct.story_circle` · `struct.story_spine` · `struct.flash_fiction` · `struct.unity_of_effect` |
| **One continuous body at feature or novel size — 90 to 120 minutes, or 300 pages** (7) | `struct.three_act` · `struct.save_the_cat` · `struct.truby_22` · `struct.sequence_approach` · `struct.heros_journey` · `struct.freytag` · `struct.freytag_climax` |
| **Segmented — there is a real exit between parts and the audience has to be brought back** (2) | `struct.four_act` · `struct.linked_collection` |

**The nine cells, which is where the answer actually is**

| | **One sitting** | **Feature / novel** | **Segmented** |
| :--- | :--- | :--- | :--- |
| **External escalation** | `struct.story_spine` | `struct.three_act` · `struct.save_the_cat` · `struct.sequence_approach` · `struct.freytag` · `struct.freytag_climax` | `struct.four_act` |
| **The protagonist's lack** | `struct.story_circle` | `struct.truby_22` · `struct.heros_journey` | **— empty —** |
| **Adjacency** | `struct.kishotenketsu` · `struct.flash_fiction` · `struct.unity_of_effect` | **— empty —** | `struct.linked_collection` |

*A card appears once per axis, so every one of the fourteen sits in exactly one cell. The two empty cells are a finding about the shelf and are argued in **The unasked**.*

---

**The default, and the one against it**

**The default is `struct.save_the_cat`, and it is measured rather than asserted.** Four cards on this shelf receive two inbound `Yields to:` each — `struct.kishotenketsu`, `struct.three_act`, `struct.save_the_cat` and `struct.story_circle` — and counting yields arriving from other shelves as well, `struct.kishotenketsu` leads outright with three. So the raw count does not pick a default; it picks a four-way tie. **What separates `struct.save_the_cat` is that it is the only one of the four whose two senders arrive on different axes.** `struct.truby_22` sends a reader here on Axis 1 (*"No moral question"*); `struct.story_spine` sends them here on Axis 2 (*"stems will not hold a feature"*). Kishōtenketsu's two senders both arrive on the same Axis-1 condition. Three-act's two both arrive on the same one. Story circle's two both arrive on size and occupancy. **A card reached by two unrelated roads is the shelf's floor**, and `struct.save_the_cat` also sits in the most crowded cell on the map, where a default is what a default is for. Its cost is printed on its own card, which is precisely why it is a default and not a recommendation: *a script that hits all fifteen marks can still be dead — the sheet measures pace, not meaning.*

**The one against it is `struct.freytag`.** It is the only system here that puts the climax at the **centre**, so more than half the runtime is consequence rather than suspense — the one shape a contemporary audience is not trained to sit through, and the shelf apologises for it in its own `Yields to:` (*"Contemporary screen work; climax belongs near the end"*). Nothing on the shelf recommends it except `struct.four_act`, and only on the narrow condition that the protagonist's passivity is the point.

**It is the against-the-grain pick because its stated defect is already true of the work.** Freytag is *"the correct shape for any story whose power is inevitability rather than uncertainty — a historical account whose ending is known, a heritage piece, a documentary about an event the audience already remembers."* Every other system on this shelf spends its second half withholding an outcome from an audience that already holds it, and the audience reads that as the piece pretending. Freytag stops pretending at the midpoint and spends the rest of the runtime on the thing that is actually interesting — the town learning what it did. Its named failure, *"a modern audience reads that descent as the film failing to stop"*, is paid off by length and nothing on the card forbids paying it: a long falling action at 90 minutes is a problem, at nine it is a form.

**Its near cousin against the grain is `struct.unity_of_effect`**, which nothing on the shelf routes to and which is not a sequence at all. It is the only card here that tells you what to **remove** rather than what to put in order, and the only one whose unit of measurement is the state the reader is in an hour later. It can be run over any of the other thirteen.

---

**The unasked**

**Six of the fourteen reachable cards are the target of no `Yields to:` field anywhere in the package.** They can be chosen; nothing ever sends you to them:

`struct.heros_journey` · `struct.truby_22` · `struct.sequence_approach` · `struct.story_spine` · `struct.unity_of_effect` · `struct.freytag_climax`

**And the shape of that list is the finding, not its length.** Every one of the six is a system chosen for something it uniquely **supplies** — Truby's opponent who wants the same thing as the protagonist, Campbell's resonance that survives translation, Daniel's eight short films inside one feature, the Spine's two-minute test for whether a story exists at all, Poe's deletion rule, and the single instruction to put the climax in the middle. Meanwhile **every one of the twelve conditions on this shelf is written as a deficiency of the card the reader is already holding**: *accumulation instead of escalation*, *no moral question*, *no single traveller*, *short formats*, *too long to read at one sitting*, *linkage too tight*. A yield is written by a reader with one card in hand naming what it cannot do.

> **The pair field can say what a system fails at. It has no grammar for what another system is for.** So a system whose whole claim is a positive capability can never be the destination of a yield, however good it is — it is unreachable by construction, not by neglect. That is why `struct.truby_22`, the one system on this shelf that welds meaning to plot, is routed to by nothing.

**The second thing the list shows is the two empty cells, and they are the same defect seen from the other side.**

- **Adjacency at feature length is empty.** The shelf has a non-conflict system that scales *down* brilliantly — `struct.kishotenketsu` fits a fifteen-second spot — and nothing at all for the 110-minute film with no antagonist, which is a large and living tradition (the observational feature, the essay film, the slow family drama). A writer answering *adjacency* and *feature* is handed Kishōtenketsu stretched over two hours with no card saying how, or pushed back into three acts by the only question that reaches them. **The card this shelf wants is the one that says what four movements do when each one has to run twenty-five minutes.**
- **The protagonist's lack, serialised, is empty.** `struct.four_act` names act breaks but runs on external pressure; `struct.story_circle` is need-driven and explicitly holds *one occupant*; `struct.truby_22` is need-driven and explicitly continuous. Prestige television is precisely a moral-need structure with real exits in it, and this shelf has no card for it — which is also why `struct.story_circle`'s only `Yields to:` points **off the shelf entirely**, to `rel.ensemble_as_system`. The shelf knows the gap and outsources it.

**And the 98 beats are unasked in a stricter sense: nothing inside the shelf routes to a single one of them.** Three are reached from other shelves — `struct.stc_midpoint` from `arc.midpoint_peak`, `struct.seq_h` from the endings file, `struct.truby_14_apparent_defeat` from the tension file — and in all three cases the yield is a **repair instruction** (*"Repair: demote the midpoint change to partial"*), never an option. The pair graph, asked 3,346 times across the package, never once offers a beat as an alternative to another beat. That is the evidence for the shape of this card.

`struct.system_before_beats`

---

### The Three-Act Paradigm

**Also called:** the Field paradigm, classical three-act
**System:** Syd Field, *Screenplay*, 1979. Unit: the act, hinged by two plot points.
**What it is:** The screenplay is divided into Setup, Confrontation and Resolution in a roughly 1:2:1 proportion, with a Plot Point — an incident that spins the action in a new direction — at the end of Act One and again at the end of Act Two.
**The beats:** Setup · Inciting Incident · Plot Point One · Confrontation · Midpoint · Plot Point Two · Resolution
**Effect on the work:** A shape the reader recognises without being told. Its real function is not creative but contractual: it is the shared vocabulary in which notes are given, and a writer who cannot say where their plot points are will receive notes they cannot use.
**Used for and where it works best:** Anything that will be read by a producer, a commissioner or a script editor. It is the lowest common denominator of the trade and the right choice when the project needs to be discussed more than it needs to be innovative. It is also the correct first structure for a writer who has never finished anything, because it is the only one simple enough to hold in the head while drafting.
**Best in:** formats: Feature Film, TV Pilot, Short Film, Corporate, Explainer | genres: all
**Avoid when:** The work runs on accumulation, mood or simultaneity rather than escalation — an essay film, a concept music video, a lyric, most observational documentary. Also avoid treating it as sufficient: three acts describe where the corners are, not what happens in the long middle, and the writers who struggle most are those who have three acts and nothing else. That gap is exactly what Snyder and Daniel were built to fill.
**Example:**
> *Plot Point One:* she boards the train. The story can no longer be about whether she will go.
> *Plot Point Two:* she learns the address was wrong from the start. The story stops being a search and becomes a reckoning.

**Yields to:** `struct.kishotenketsu` — Accumulation, mood or simultaneity instead of escalation.  
`struct.three_act`

#### Beats

**Setup** — Establishes who, where, and the rule of the world that the story will break. Fails when it establishes situation but not want.
`struct.three_act_setup`

**Inciting Incident** — The event that makes the ordinary arrangement unworkable. Fails when it happens *to* the protagonist without requiring a response from them.
`struct.three_act_inciting`

**Plot Point One** — The protagonist commits, and the commitment costs something they cannot recover. Fails when the protagonist is pushed through the door rather than walking through it.
`struct.three_act_pp1`

**Confrontation** — Sustained opposition in which the first plan proves insufficient. Fails when it becomes a sequence of obstacles that do not change the protagonist's understanding.
`struct.three_act_confrontation`

**Midpoint** — The middle of the middle turns, so the second half of Act Two is not the same as the first. Fails when it is merely the biggest event so far rather than a reversal of direction.
`struct.three_act_midpoint`

**Plot Point Two** — The last door closes; the protagonist must finish it themselves. Fails when help arrives.
`struct.three_act_pp2`

**Resolution** — The dramatic question is answered and the cost is shown. Fails when it answers the plot question but not the character one.
`struct.three_act_resolution`

---

## B. Save the Cat Beat Sheet

### Save the Cat Beat Sheet

**Also called:** the Snyder beat sheet, STC 15
**System:** Blake Snyder, *Save the Cat!*, 2005. Unit: the beat — a visible plot event at a named page.
**What it is:** Fifteen beats page-numbered across a 110-page screenplay, built specifically to manage the second act, which is where most scripts collapse.
**The beats:** Opening Image (p.1) · Theme Stated (p.5) · Set-Up (pp.1–10) · Catalyst (p.12) · Debate (pp.12–25) · Break into Two (p.25) · B Story (p.30) · Fun and Games (pp.30–55) · Midpoint (p.55) · Bad Guys Close In (pp.55–75) · All Is Lost (p.75) · Dark Night of the Soul (pp.75–85) · Break into Three (p.85) · Finale (pp.85–110) · Final Image (p.110)
**Effect on the work:** Reliable pace and a second act with a spine. The midpoint false victory or false defeat raises stakes at the exact place scripts usually sag.
**Used for and where it works best:** Studio features, genre work, animation features, and any commissioned script that will be read by someone counting pages. It is also the best repair tool in the craft: lay the sheet over a broken draft and the missing beat is usually visible in one pass.
**Best in:** formats: Feature Film, Animation Feature, Novel (via Brody), TV Pilot | genres: Action, Comedy, Romance, Coming of Age, Superhero, Family, Thriller
**Avoid when:** Non-Western structural traditions — Kishōtenketsu develops without conflict and will fight the sheet the whole way. Also avoid mixing it with Truby: Snyder organises around visible plot events and Truby around moral need, and a draft built on both produces contradictory notes. The honest caution: the page numbers are a diagnostic, not a target, and a script that hits all fifteen marks can still be dead — the sheet measures pace, not meaning.
**Example:**
> *Catalyst, p.12:* the letter arrives.
> *Break into Two, p.25:* she gets on the train.
> *Midpoint, p.55:* she finds him — and he is not what the letter said. **False victory.**
> *All Is Lost, p.75:* the return ticket expires.

**Yields to:** `struct.kishotenketsu` — Non-Western tradition; development without conflict.  
`struct.save_the_cat`

#### Beats

**Opening Image** — The first visual, set against the Final Image to measure the whole distance travelled. Fails when it is atmosphere instead of a statement of the starting condition.
`struct.stc_opening_image`

**Theme Stated** — Someone says the story's argument out loud, usually to a protagonist not ready to hear it. Fails when the protagonist agrees.
`struct.stc_theme_stated`

**Set-Up** — Six things that need fixing, planted for later payoff. Fails when it is only introduction and plants nothing.
`struct.stc_setup`

**Catalyst** — The news, the knock, the letter. Fails when it is reversible.
`struct.stc_catalyst`

**Debate** — The protagonist resists, and the resistance is reasonable. Fails when it is short enough that the audience never believes refusal was possible.
`struct.stc_debate`

**Break into Two** — The protagonist chooses the new world actively. Fails when they are carried into it.
`struct.stc_break_two`

**B Story** — The relationship that will carry the theme, usually a new character. Fails when it is a subplot with no thematic load.
`struct.stc_b_story`

**Fun and Games** — The promise of the premise: what the audience bought a ticket for. Fails when plot advances here instead of pleasure.
`struct.stc_fun_and_games`

**Midpoint** — False victory or false defeat; stakes are raised and the clock usually starts. Fails when it is neither false nor a turn.
`struct.stc_midpoint`

**Bad Guys Close In** — Internal dissent and external pressure tighten together. Fails when only external pressure rises.
`struct.stc_bad_guys_close_in`

**All Is Lost** — The lowest point, often carrying a "whiff of death". Fails when the loss is recoverable by trying harder.
`struct.stc_all_is_lost`

**Dark Night of the Soul** — The protagonist sits in the loss before responding. Fails when it is skipped, which makes the recovery unearned.
`struct.stc_dark_night`

**Break into Three** — A and B stories fuse, and the answer comes from the relationship. Fails when the solution arrives from outside the story's own material.
`struct.stc_break_three`

**Finale** — The protagonist transforms and dismantles the opposition. Fails when they win using the same self they started with.
`struct.stc_finale`

**Final Image** — The mirror of the Opening Image. Fails when it merely repeats it instead of answering it.
`struct.stc_final_image`

---

## C. Story Circle

### The Story Circle

**Also called:** the Harmon circle, the embryo
**System:** Dan Harmon. Unit: the station — eight positions on a circle divided into an ordered and a chaotic half.
**What it is:** A compressed monomyth in eight steps: **You · Need · Go · Search · Find · Take · Return · Change.** The top half is the world the character knows; the bottom half is the world they do not. The vertical axis is order against chaos, the horizontal is consciousness against the unconscious.
**The beats:** You · Need · Go · Search · Find · Take · Return · Change
**Effect on the work:** Structure without page numbers. Because the circle is proportional rather than timed, it holds at any length — a 90-second episode and a 10-hour season take the same eight steps at different scales.
**Used for and where it works best:** Television above all, where it was built, and anything episodic or short. It is the best system for a writer working in a format with no fixed runtime: sketches, reels, micro-drama, a single-character short. Its other strength is that steps 5 and 6 — Find and Take — name the thing most systems leave vague: getting what you wanted *is* the moment the price appears.
**Best in:** formats: One-Hour Drama, Half-Hour Comedy, Web Series, Vertical Micro-Drama, Short Film, Animation Series, Reels/Shorts | genres: Comedy, Drama, Science Fiction, Adventure, Coming of Age, Satire
**Avoid when:** Ensemble stories with no single traveller — the circle has one occupant, and forcing four characters around it at once produces four thin arcs rather than one deep one. Also weak for mysteries, where the protagonist's want is information rather than change, and the circle's "Take" beat has nothing to charge them.
**Example:**
> **You** — he runs the shop his father left him.
> **Need** — he has not opened the back room in two years.
> **Go** — a buyer arrives.
> **Search** — he learns what the shop is actually worth.
> **Find** — the offer is enough to leave.
> **Take** — accepting means the back room gets cleared by strangers.
> **Return** — he clears it himself.
> **Change** — he sells, and keeps one thing.

**Yields to:** `rel.ensemble_as_system` — Ensemble with no single traveller.  
`struct.story_circle`

#### Beats

**You** — A character in a zone of comfort, defined by what they are used to rather than what they like. Fails when comfort is written as happiness.
`struct.circle_you`

**Need** — Something is missing, and the character usually cannot name it. Fails when the character states it clearly, which converts a need into a want.
`struct.circle_need`

**Go** — They enter an unfamiliar situation. Fails when the new situation is not genuinely unfamiliar to *them*, whatever it looks like to the audience.
`struct.circle_go`

**Search** — They adapt, and the adaptation costs. Fails when it becomes a montage of competence instead of a sequence of adjustments.
`struct.circle_search`

**Find** — They get what they wanted. Fails when it arrives too late to be paid for.
`struct.circle_find`

**Take** — They pay the price. Fails when the price is paid by someone else, which is the single most common collapse of this system.
`struct.circle_take`

**Return** — They head back, carrying what they took. Fails when the return is only physical.
`struct.circle_return`

**Change** — They are no longer the same. Fails when the change is announced rather than demonstrated by a choice they could not have made in step one.
`struct.circle_change`

---

## D. The Hero's Journey

### The Hero's Journey

**Also called:** the monomyth, the Vogler twelve, the Campbell cycle
**System:** Joseph Campbell, *The Hero with a Thousand Faces*, 1949; adapted for screen by Christopher Vogler, *The Writer's Journey*, 1992. Unit: the stage, arranged as a departure, an initiation and a return.
**What it is:** Twelve stages a protagonist passes through from an ordinary world to a transformed return, with named functional roles — Mentor, Threshold Guardian, Shapeshifter, Shadow, Trickster — attached to the figures they meet.
**The beats:** Ordinary World · Call to Adventure · Refusal of the Call · Meeting the Mentor · Crossing the First Threshold · Tests, Allies and Enemies · Approach to the Inmost Cave · The Ordeal · Reward (Seizing the Sword) · The Road Back · Resurrection · Return with the Elixir
**Effect on the work:** Resonance that is difficult to obtain any other way. The pattern is old enough that an audience recognises its shape before they recognise its content, which is why it survives translation between cultures better than any other system here.
**Used for and where it works best:** Myth, fantasy, epic, adventure, animation features, and any story whose subject is becoming rather than solving. It is also the right frame for heritage and origin material, where the audience is being asked to receive something as inheritance rather than as plot.
**Best in:** formats: Feature Film, Animation Feature, Novel, Game Narrative, Heritage Documentary, Series | genres: Myth, Fantasy/Epic, Adventure, Science Fiction, Coming of Age, Heritage, Historical
**Avoid when:** Contemporary domestic drama, satire, most comedy, and any story about a character who should *not* be ennobled — the monomyth confers heroism structurally, and applying it to a small or compromised story inflates it. The honest caution: Campbell described a pattern found in myth after the fact; Vogler turned it into a template to be followed in advance. Those are different claims, and a great deal of weak writing comes from treating the first as licence for the second.
**Example:**
> *Refusal:* he says the river is not his to cross.
> *Threshold:* he crosses at night so no one sees him decide.
> *Ordeal:* he is asked to name his father in front of people who knew him.
> *Elixir:* he returns with nothing in his hands and the name in his mouth.

**Yields to:** `struct.story_circle` — Small, compromised or comic story; monomyth inflates it.  
`struct.heros_journey`

#### Beats

**Ordinary World** — The life to be measured against. Fails when it is merely dull rather than specifically insufficient.
`struct.hj_ordinary_world`

**Call to Adventure** — The disturbance that proposes a journey. Fails when it is an order rather than an invitation.
`struct.hj_call`

**Refusal of the Call** — Fear, duty or good sense argues against going. Fails when the refusal is not genuinely reasonable.
`struct.hj_refusal`

**Meeting the Mentor** — Someone gives knowledge, an object or permission. Fails when the mentor solves rather than equips.
`struct.hj_mentor`

**Crossing the First Threshold** — Committing to the unknown world. Fails when return remains easy.
`struct.hj_threshold`

**Tests, Allies and Enemies** — The rules of the new world are learned through use. Fails when allies are acquired without cost.
`struct.hj_tests_allies_enemies`

**Approach to the Inmost Cave** — Preparation for the central ordeal, and the last chance to turn back. Fails when it is skipped, which removes the dread.
`struct.hj_approach`

**The Ordeal** — A confrontation with death, literal or symbolic. Fails when survival requires no surrender.
`struct.hj_ordeal`

**Reward (Seizing the Sword)** — Taking what the ordeal was for. Fails when the reward is given rather than seized.
`struct.hj_reward`

**The Road Back** — Committing to return, usually pursued. Fails when the journey home is uncontested.
`struct.hj_road_back`

**Resurrection** — The final test, at the highest level, proving the transformation is real. Fails when it repeats the Ordeal instead of exceeding it.
`struct.hj_resurrection`

**Return with the Elixir** — Coming home with something that benefits the ordinary world. Fails when the elixir helps only the hero.
`struct.hj_elixir`

---

## E. The 22 Building Blocks

### The 22 Building Blocks

**Also called:** Truby's 22 steps, the anatomy of story
**System:** John Truby, *The Anatomy of Story*, 2007. Unit: the step, organised around moral need rather than plot event.
**What it is:** Twenty-two steps in which the protagonist's **weakness** produces a **need**, a **desire** drives them into conflict with an **opponent** who attacks that exact weakness, and the story ends in a **self-revelation** followed by a **moral decision** the character could not have made at the start.
**The beats:** 1 Self-revelation, need and desire · 2 Ghost and story world · 3 Weakness and need · 4 Inciting event · 5 Desire · 6 Ally or allies · 7 Opponent and/or mystery · 8 Fake-ally opponent · 9 First revelation and decision · 10 Plan · 11 Opponent's plan and main counterattack · 12 Drive · 13 Attack by ally · 14 Apparent defeat · 15 Second revelation and decision · 16 Audience revelation · 17 Third revelation and decision · 18 Gate, gauntlet, visit to death · 19 Battle · 20 Self-revelation · 21 Moral decision · 22 New equilibrium
**Effect on the work:** Meaning welded to plot. Because the opponent is designed to attack the protagonist's specific weakness, the external conflict and the internal one become the same conflict, which is the thing most structures leave to luck.
**Used for and where it works best:** Character-driven drama, literary adaptation, and any story that has plot but feels weightless. Truby's distinguishing move is the **designing principle** — one sentence naming how the story is told, not what happens — and it is the most useful single question in this entire file. It is also the strongest system for antagonist construction: step 7 requires the opponent to want the same thing as the protagonist, which converts a villain into an argument.
**Best in:** formats: Feature Film, Novel, One-Hour Drama, Stage Play, Limited Series | genres: Drama, Crime, Tragedy, Psychological, Historical, Social Drama, Literary
**Avoid when:** The work has no moral question — pure spectacle, most comedy of manners, procedural episodes, product and brand films. Also avoid running it beside Save the Cat: Truby's revelations do not sit at Snyder's page numbers and never will. And the honest caution: three staged revelations can become mechanical, producing characters who narrate their own growth on schedule.
**Example:**
> *Designing principle:* a forger discovers his talent by authenticating his own fakes.
> *Weakness:* he believes skill is the same as worth.
> *Opponent:* the dealer who agrees with him completely.
> *Self-revelation:* the forgeries were never the lie.

**Yields to:** `struct.save_the_cat` — No moral question: spectacle, procedural, brand film.  
`struct.truby_22`

#### Beats

**Self-revelation, need and desire** — The end stated first, so the whole story can be designed backwards from it. Fails when written last.
`struct.truby_01_end_first`

**Ghost and story world** — The past wound and the world built around it. Fails when the ghost is dramatic backstory rather than an active present constraint.
`struct.truby_02_ghost`

**Weakness and need** — The flaw hurting the protagonist and others. Fails when the weakness is charming.
`struct.truby_03_weakness`

**Inciting event** — The event that produces the desire. Fails when it produces only a situation.
`struct.truby_04_inciting`

**Desire** — The specific external goal driving the plot. Fails when it is not concrete enough to be achieved or lost.
`struct.truby_05_desire`

**Ally or allies** — Someone the protagonist talks to, which is how the audience hears the plan. Fails when the ally only agrees.
`struct.truby_06_ally`

**Opponent and/or mystery** — Someone who wants the same thing, so the conflict is necessary rather than arranged. Fails when the opponent merely opposes.
`struct.truby_07_opponent`

**Fake-ally opponent** — An opponent who appears to be a friend. Fails when the reveal is a twist rather than a pressure.
`struct.truby_08_fake_ally`

**First revelation and decision** — New information changes the desire and motive. Fails when it changes the plan but not the motive.
`struct.truby_09_first_revelation`

**Plan** — The strategy for reaching the goal. Fails when it is not specific enough to fail interestingly.
`struct.truby_10_plan`

**Opponent's plan and main counterattack** — The opposition is shown to have a strategy of its own. Fails when the opponent only reacts.
`struct.truby_11_opponent_plan`

**Drive** — Escalating attempts, in which the protagonist begins using immoral means. Fails when the protagonist stays clean.
`struct.truby_12_drive`

**Attack by ally** — The friend names the moral cost out loud. Fails when the ally is wrong.
`struct.truby_13_attack_by_ally`

**Apparent defeat** — The protagonist believes the goal is lost. Fails when the audience does not believe it too.
`struct.truby_14_apparent_defeat`

**Second revelation and decision** — Obsessive drive: desire and motive change again, harder. Fails when it reads as repetition of the first.
`struct.truby_15_second_revelation`

**Audience revelation** — The audience learns something the protagonist does not. Fails when it is withheld information rather than reframing information.
`struct.truby_16_audience_revelation`

**Third revelation and decision** — The last turn before the end. Fails when it arrives too close to the battle to be absorbed.
`struct.truby_17_third_revelation`

**Gate, gauntlet, visit to death** — Compression, pressure, and a brush with mortality. Fails when it is action rather than narrowing.
`struct.truby_18_gate_gauntlet`

**Battle** — The final conflict, with both goals crystal clear. Fails when the audience cannot state what either side wants.
`struct.truby_19_battle`

**Self-revelation** — The protagonist sees what they have been doing wrong. Fails when someone tells them.
`struct.truby_20_self_revelation`

**Moral decision** — They act on it, choosing what they could not have chosen at the start. Fails when the decision costs nothing.
`struct.truby_21_moral_decision`

**New equilibrium** — The world settles at a new level. Fails when it settles at the old one.
`struct.truby_22_new_equilibrium`

---

## F. The Sequence Approach

### The Sequence Approach

**Also called:** the eight-sequence method, the Frank Daniel sequence paradigm
**System:** Frank Daniel, taught at AFI, Columbia and USC; codified by Paul Gulino. Unit: the sequence — eight segments of 10 to 15 minutes, each a short film with its own protagonist, tension, rising action and resolution.
**What it is:** Three acts subdivided into eight sequences: two in Act One establishing the status quo and the inciting incident, four in Act Two in which the protagonist repeatedly fails, and two in Act Three resolving the central dramatic question and the subplots. The method descends from early cinema, when films were distributed on reels of roughly that length.
**The beats:** Sequence A Status quo and inciting incident · Sequence B Predicament and lock-in · Sequence C First obstacle and raised stakes · Sequence D First culmination and midpoint · Sequence E Subplot and rising action · Sequence F Main culmination and the end of Act Two · Sequence G New tension and the highest point · Sequence H Resolution and false ending
**Effect on the work:** It solves the specific problem the three-act paradigm creates — a sixty-page middle with nothing said about it. Eight sequences turn one impossible act into six manageable short films.
**Used for and where it works best:** Feature scripts that stall in the second act, and any writer who can finish a short but not a feature. Its hidden strength is production-facing: a sequence is roughly a block of shooting, so a script built this way schedules and budgets more cleanly than one built on beats alone.
**Best in:** formats: Feature Film, Limited Series, Animation Feature, Game Narrative | genres: all narrative
**Avoid when:** Short formats, where eight sequences will not fit and the method becomes arithmetic. Also weaker for ensemble and mosaic films, where tension does not belong to one protagonist per segment.
**Example:**
> *Sequence D culminates* on the promotion he has chased for forty minutes. He gets it. The midpoint is that the office he inherits is his father's.

**Yields to:** `struct.story_circle` — Short formats; eight sequences become arithmetic.  
`struct.sequence_approach`

#### Beats

**Sequence A — Status quo and inciting incident** — The world, and the disturbance. Fails when the disturbance arrives before the world is legible.
`struct.seq_a`

**Sequence B — Predicament and lock-in** — The problem is defined and escape closes. Fails when the lock is not plausible.
`struct.seq_b`

**Sequence C — First obstacle, raised stakes** — The first real attempt and its resistance. Fails when the obstacle is not caused by the attempt.
`struct.seq_c`

**Sequence D — First culmination and midpoint** — A genuine result that changes the question. Fails when it is a setback rather than a turn.
`struct.seq_d`

**Sequence E — Subplot and rising action** — The relationship line carries the load while the main line regroups. Fails when the subplot is unconnected to the theme.
`struct.seq_e`

**Sequence F — Main culmination, end of Act Two** — The largest failure, from which the old plan cannot recover. Fails when the protagonist still has the same plan afterwards.
`struct.seq_f`

**Sequence G — New tension and highest point** — A new approach at maximum pressure. Fails when the new approach was available earlier.
`struct.seq_g`

**Sequence H — Resolution and false ending** — Resolution, usually preceded by an ending that turns out not to be one. Fails when the false ending is not believable on its own.
`struct.seq_h`

---

## G. Freytag's Pyramid

### Freytag's Pyramid

**Also called:** the dramatic arc, the five-act pyramid
**System:** Gustav Freytag, *Die Technik des Dramas*, 1863. Unit: the act, arranged as a rise and a fall around a central climax.
**What it is:** Exposition, Rising Action, Climax, Falling Action, Catastrophe or Dénouement — with the climax at the centre rather than near the end, which is the detail most modern summaries get wrong.
**The beats:** Exposition · Rising Action · Climax · Falling Action · Catastrophe/Dénouement
**Effect on the work:** A long descent. Because the climax sits in the middle, the second half is consequence rather than suspense, and the reader watches an outcome arrive that they can already see.
**Used for and where it works best:** Tragedy, where the audience's foreknowledge is the point, and stage drama, for which it was written. It is also the correct shape for any story whose power is inevitability rather than uncertainty — a historical account whose ending is known, a heritage piece, a documentary about an event the audience already remembers.
**Best in:** formats: Stage Play, Feature Film, Novel, Heritage Documentary, Opera/Libretto | genres: Tragedy, Historical, Heritage, Melodrama, Literary
**Avoid when:** Contemporary screen storytelling, which puts the climax near the end and cannot absorb a long falling action — a modern audience reads that descent as the film failing to stop. Apply it deliberately or not at all. The honest caution: Freytag was describing five-act German tragedy of his own century, not prescribing a universal shape, and its routine use as a school diagram for all narrative is a misreading.
**Example:**
> The climax is the killing, at the centre. Everything after is the town learning what it did, which takes as long as the approach did.

**Yields to:** `struct.three_act` — Contemporary screen work; climax belongs near the end.  
`struct.freytag`

#### Beats

**Exposition** — The situation and the standing conflict. Fails when it delivers history rather than pressure.
`struct.freytag_exposition`

**Rising Action** — Complication accumulating toward the centre. Fails when complications do not compound.
`struct.freytag_rising`

**Climax** — The turn, at the centre of the work. Fails when placed near the end, which converts the form into three acts.
`struct.freytag_climax`

**Falling Action** — Consequence unfolding with the outcome already visible. Fails when it introduces new uncertainty.
`struct.freytag_falling`

**Catastrophe / Dénouement** — The final state. Fails when it offers relief the work has not earned.
`struct.freytag_catastrophe`

---

## H. Kishōtenketsu

### Kishōtenketsu

**Also called:** 起承転結, the four-act turn, development without conflict
**System:** Classical Chinese and Japanese poetics, carried into prose, manga, anime and advertising. Unit: the part — four movements in which the third is a turn that is not a conflict.
**What it is:** **Ki** introduction · **Shō** development · **Ten** the turn — an unexpected element that reframes what came before · **Ketsu** the reconciliation that shows how the first two and the third belong together. The engine is juxtaposition, not opposition: nothing needs to want to stop anything.
**The beats:** Ki (introduction) · Shō (development) · Ten (turn) · Ketsu (reconciliation)
**Effect on the work:** Meaning through adjacency. The audience is not held by wanting to know who wins, but by wanting to know how two things relate — a quieter grip, and a durable one.
**Used for and where it works best:** Anime and manga, four-panel comics, picture books, ambient and lyrical film, commercials, music videos, essay work, and prose flash, whose turn is a revelation rather than a conflict (`struct.flash_fiction`). It is the correct structure for anything about a place, a season, a craft or a relationship with no antagonist, and it is the honest answer for writers who keep being told to "add more conflict" to work that does not want any. It also scales down better than any other system: four movements fit a fifteen-second spot.
**Best in:** formats: Anime, Comics, Short Animation, Picture Book, Flash Fiction, TVC, Music Video, Essay Film, Reels/Shorts, Poetry | genres: Slice of Life, Family, Heritage, Comedy, Surreal, Nature, Preschool, Literary
**Avoid when:** A commissioner is expecting three acts and will read the absence of conflict as an absence of story — that is a political problem, not a craft one, and it is real. Also avoid when the material genuinely is a contest: forcing a competition into a non-conflict frame drains it.
**Example:**
> **Ki** — a man repairs shoes in a narrow shop.
> **Shō** — the street around him fills with new signage, year by year.
> **Ten** — a photograph shows the same street in 1961; his shop is the only thing in both frames.
> **Ketsu** — he is not the one who stayed behind. He is the one who stayed.

**Yields to:** `struct.three_act` — Material is genuinely a contest, or commissioner expects acts.  
`struct.kishotenketsu`

#### Beats

**Ki — Introduction** — The subject and its setting, offered without a problem attached. Fails when a conflict is smuggled in to reassure a Western reader.
`struct.kishoten_ki`

**Shō — Development** — The subject deepens along its own line. Fails when it escalates instead of deepening.
`struct.kishoten_sho`

**Ten — Turn** — A new element arrives that recontextualises the first two parts. Fails when it is a twist about the plot rather than a shift of frame.
`struct.kishoten_ten`

**Ketsu — Reconciliation** — The relation between the parts becomes visible. Fails when it explains the turn instead of completing it.
`struct.kishoten_ketsu`

---

## I. The Story Spine

### The Story Spine

**Also called:** the Pixar spine, the once-upon-a-time frame
**System:** Brian McDonald, popularised through Pixar and often miscredited to it as its fourth storytelling rule. Unit: the sentence stem.
**What it is:** Eight fill-in-the-blank stems: *Once upon a time there was ___. Every day ___. One day ___. Because of that ___. Because of that ___. Because of that ___. Until finally ___. And ever since that day ___.*
**The beats:** Once upon a time · Every day · One day · Because of that (×3) · Until finally · And ever since that day
**Effect on the work:** Enforced causality. The repeated *because of that* makes it structurally impossible to write a sequence of events that merely follow one another, which is the most common defect in a first draft.
**Used for and where it works best:** Pitching, story-breaking, animation development, children's stories, brand films, and any moment when a writer needs to find out in two minutes whether they have a story at all. The single most valuable diagnostic in the file: if you cannot fill the *because of that* lines without writing "and then", your plot is a list.
**Best in:** formats: Animation Feature, Short Animation, Kids Story, Picture Book, Brand Film, Explainer, Pitch Document, Reels/Shorts | genres: Family, Adventure, Comedy, Preschool, Fable, Heritage
**Avoid when:** Finished long-form structure — eight stems will not hold a novel or a feature, and treating the spine as an outline produces work that is merely causal, which is not the same as being good. The last stem, *and ever since that day*, is the one most often dropped and the one that carries the meaning; a spine without it stops rather than ends.
**Example:**
> Once upon a time there was a girl who kept every letter she was sent.
> Every day she added one to the box and read none of them.
> One day the box would not close.
> Because of that she opened the oldest.
> Because of that she learned it was not addressed to her.
> Because of that she went to find who it belonged to.
> Until finally she gave it away, and the box closed.
> And ever since that day she has answered on the day she receives.

**Yields to:** `struct.save_the_cat` — Finished long-form structure; stems will not hold a feature.  
`struct.story_spine`

#### Beats

**Once upon a time** — The protagonist defined by a standing habit. Fails when it gives a trait instead of a behaviour.
`struct.spine_once`

**Every day** — The repeated state, which establishes what "one day" will break. Fails when the routine is not specific.
`struct.spine_every_day`

**One day** — The disturbance. Fails when it does not directly contradict the "every day".
`struct.spine_one_day`

**Because of that (×3)** — Consequence chained to consequence. Fails the moment one of them could be written as "and then".
`struct.spine_because`

**Until finally** — The consequence that resolves the chain. Fails when it arrives from outside the chain.
`struct.spine_until_finally`

**And ever since that day** — The changed permanent state. Fails when omitted, which is the most common error in this system.
`struct.spine_ever_since`

---

## J. Four-Act Structure

### Four-Act Structure

**Also called:** the midpoint split, the two-act-two model
**System:** Common industry practice rather than one author; formalised in television by act breaks. Unit: the act, with the midpoint promoted to a full act boundary.
**What it is:** Act Two is split in half at the midpoint, producing four roughly equal acts: Setup, Reaction, Action, Resolution. The protagonist is reactive across Act Two-A and becomes active across Act Two-B.
**The beats:** Act One Setup · Act Two-A Reaction · Midpoint · Act Two-B Action · Act Three Resolution
**Effect on the work:** It names the change most useful to a writer: the exact point where the protagonist stops responding to the story and starts causing it. Three-act language hides that shift inside a long middle.
**Used for and where it works best:** Television, where act breaks are structural rather than conceptual, and any feature whose protagonist is passive for too long. This is the fastest fix for the most common note in the trade — "the character is reactive" — because it locates precisely where the change was supposed to happen.
**Best in:** formats: One-Hour Drama, Limited Series, Feature Film, Web Series, Vertical Micro-Drama (at series level) | genres: Drama, Thriller, Crime, Procedural, Melodrama, Coming of Age
**Avoid when:** The passivity is the point — some tragedies and most literary adaptation require a protagonist who never takes the wheel, and forcing the Two-B turn on them falsifies the material.
**Example:**
> Two-A: he answers every summons from the family.
> Midpoint: he learns the summonses were never from the family.
> Two-B: he starts sending them.

**Yields to:** `struct.freytag` — Passivity is the point: tragedy, literary adaptation.  
`struct.four_act`

#### Beats

**Act One — Setup** — World, want, disturbance, commitment. Fails when commitment is missing.
`struct.four_act_one`

**Act Two-A — Reaction** — The protagonist responds to pressure applied by others. Fails when it runs past the halfway mark.
`struct.four_act_two_a`

**Midpoint** — The information or event that converts reaction into action. Fails when it does not change who is driving.
`struct.four_act_midpoint`

**Act Two-B — Action** — The protagonist sets the agenda and the opposition responds. Fails when the protagonist is still being summoned.
`struct.four_act_two_b`

**Act Three — Resolution** — The confrontation the protagonist chose. Fails when it is one they were dragged to.
`struct.four_act_three`

---

## K. McKee's Story Hierarchy

### McKee's Story Hierarchy

**Also called:** the story triangle, beat-scene-sequence-act
**System:** Robert McKee, *Story*, 1997. Unit: nested — beat, scene, sequence, act, story — each defined by a change in value at its own scale.
**What it is:** Not a beat sheet but a hierarchy. A **beat** is an exchange of action and reaction. A **scene** turns a value. A **sequence** turns a value more strongly than any scene inside it. An **act** turns it more strongly than any sequence inside it. The **story** turns it irreversibly. Above them sits the **controlling idea** — one sentence naming the value and the cause that delivers it.
**The beats:** Beat · Scene · Sequence · Act · Story climax · Controlling idea
**Effect on the work:** Proportion. Most structural failure is not a missing beat but a scale error — a scene carrying an act-sized turn, or an act ending on a scene-sized one. This system is the only one here that measures that directly.
**Used for and where it works best:** Diagnosis above all, and it is compatible with every other system in this file because it describes scale rather than sequence — you can run Snyder's fifteen beats and still use McKee to check whether your act climax outweighs your sequence climaxes. It is the one system worth learning *in addition* rather than instead.
**Best in:** formats: all narrative | genres: all narrative
**Avoid when:** Drafting. The hierarchy is an analytic instrument and applying it while writing a first draft produces paralysis. Use it on the second.
**Example:**
> Scene: she refuses the money. *Pride, up.*
> Sequence: she refuses it three times, and the third costs her the flat. *Pride up, security down — stronger.*
> Act: she takes it, from the one person she swore she would not ask. *Pride, irreversibly down.*

`struct.mckee_hierarchy`

#### Beats

**Beat** — An exchange of action and reaction in character behaviour. Fails when a line of dialogue is mistaken for a beat.
`struct.mckee_beat`

**Scene** — A unit that turns a value through conflict. Fails when nothing turns, which makes it an event.
`struct.mckee_scene`

**Sequence** — Two to five scenes climaxing in a stronger turn than any of them. Fails when its climax is no larger than its scenes.
`struct.mckee_sequence`

**Act** — A series of sequences climaxing in a major reversal. Fails when the act climax is a sequence climax in disguise.
`struct.mckee_act`

**Story climax** — The irreversible turn of the story's central value. Fails when it is reversible.
`struct.mckee_story_climax`

**Controlling idea** — One sentence: the value, and the cause that brings it about. Fails when it is a theme word rather than a causal statement.
`struct.mckee_controlling_idea`

---

## Coverage

All cards in this file are `durable`. None carries a review date.

*Build notes from when this file was drafted — targets, running totals and what remained to be written — are kept verbatim in the [coverage history](../tools/history/coverage-history.md). They were true of the draft, not of the file, so they no longer sit here as if they were measurements.*

## Sources

Verified 2026-09-17.

- [11 Storytelling Structures for Screenwriters — GL Coverage](https://glcoverage.com/2025/02/28/storytelling-structures-for-screenwriters/)
- [Save the Cat Beat Sheet — Reedsy](https://reedsy.com/blog/guide/story-structure/save-the-cat-beat-sheet/)
- [Save the Cat Story Structure: The 15 Beats — Alan Watt](https://alanwatt.com/how-to-write/how-to-write-a-screenplay/save-the-cat-story-structure/)
- [Dan Harmon Story Circle — Reedsy](https://reedsy.com/blog/guide/story-structure/dan-harmon-story-circle/)
- [Dan Harmon Story Circle 8 Steps — Kindlepreneur](https://kindlepreneur.com/dan-harmon-story-circle/)
- [Truby's 22 Steps in order — Decoding Creativity](https://www.decodingcreativity.com/trubys-22-steps/)
- [22 Building Blocks — Arc Studio](https://www.arcstudiopro.com/blog/22-building-blocks-john-truby)
- [The Sequence Approach — The Story Department](https://www.thestorydepartment.com/the-sequence-approach/)
- [Frank Daniel — Wikipedia](https://en.wikipedia.org/wiki/Frank_Daniel)
- [The Story Spine — Aerogramme Studio](https://www.aerogrammestudio.com/2013/03/22/the-story-spine-pixars-4th-rule-of-storytelling/)
- [Screenwriters' Quick Guide to Storytelling Formulas — FilmDaft](https://filmdaft.com/storytelling-and-narrative-structures/)
- [Screenplay Structure: 6 Proven Frameworks — Free Screenwriter](https://freescreenwriter.com/learn/screenplay-structure-guide)
