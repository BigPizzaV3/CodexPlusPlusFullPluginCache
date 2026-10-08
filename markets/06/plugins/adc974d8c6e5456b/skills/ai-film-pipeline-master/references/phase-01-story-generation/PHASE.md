---
name: phase-01-story-generation
description: "Phase 1: Story Generation & Narrative Architecture. Directs worldbuilding, character arcs, plot structures, tension ladders, and the genre bibles, across 1,332 core craft cards (1,672 total headings). Use when the user starts a project from a raw idea, needs story development, plot beats, character design, or world lore before screenwriting. Trigger on: write a story, plot outline, story beats, worldbuilding, character arc, قصة، حبكة، فكرة فيلم، بناء عالم، شخصيات، بداية قصة."
---

# Phase 01: Story Generation & Narrative Engine

> **When two cards disagree:** open [PRECEDENCE.md](../PRECEDENCE.md) at the package root. It states
> which rule outranks which and why, how to tier a card by its own stated reason, and what to do when
> both sides land on the same tier. Open it only when two cards you are actually holding cannot both be
> obeyed in the same shot — not for a card that has no opponent in front of it, and not for two
> techniques offered as a choice.

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Overview](#overview)
- [Inputs](#inputs)
- [Operating Modes & Spend Control](#operating-modes-spend-control)
- [Input Mode (Polish vs Generation)](#input-mode-polish-vs-generation)
- [Workflow Steps](#workflow-steps)
- [Reference Architecture (Progressive Disclosure)](#reference-architecture-progressive-disclosure)
- [Files in this phase](#files-in-this-phase)
- [The contract for this phase](#the-contract-for-this-phase)

<!-- /GENERATED:toc -->

## Overview
Phase 01 determines project foundations, extracts core production constraints, researches historical detail where the user wants the piece realistic, and constructs narrative beats and retention hooks. It operates as an uncoupled engine that outputs a self-contained Story Foundation Brief to Phase 02 without mutual dependencies.

## Inputs
- User initial request, idea, topic, or draft.
- Project destination (heritage / historical channel, children's content channel, general / client work).

## Operating Modes & Spend Control
1. `Prompts only` (Default): Zero credit spend. Generates text structures, prompts, and plans only.
2. `Auto with images`: Generates text and static images/character sheets.
3. `Auto with images and video`: Generates images and video clips end-to-end.
4. `Auto, best choice from the story`: AI decides still vs motion per shot.
5. `Interactive Director Review`: review pauses the owner opted into, not gates; with the owner absent the run falls back to prompts only (HOW-1 Q1).

> **Spending Confirmation Rule:** Before generating any assets in spending modes, announce one line:  
> *"This project will generate [X] images and [Y] video clips."* and require one confirmation.

## Input Mode (Polish vs Generation)
- **Draft provided by User -> POLISH MODE:** "A story from the owner is polished, never replaced. Characters, events, ending, and order are his. Polish works on execution: dialogue, rhythm, clarity, and force." (If a core decision is unworkable, note it once in the Warning List and keep polishing the owner's version.)
- **Idea from scratch -> GENERATION MODE:** Full creative build using the 1,332 core craft cards (1,672 total headings).

## Workflow Steps

### 1. Upfront Project Intake
Extract the answers to the six intake questions in [`HOW-PHASE-1-WORKS.md`](HOW-PHASE-1-WORKS.md) §1 (never re-ask what the user already stated):
1. Operating & Spending Mode
2. Destination & Channel Profile (heritage / historical channel, children's content channel, general / client work)
3. Audio Format (Narration, Dialogue, Song, Silent)
4. Aspect Ratio & Platform, asked per deliverable (9:16 Vertical, 16:9 Horizontal, 1:1 Square, 4:5 Portrait, Other — state it, None — the piece has no picture)
5. Starting Material (Draft -> Polish, Topic -> Generation)
6. Language (with any subtitle language and the dialect), Runtime, Genre — and the Age Band on children's work

### 2. Research & Period Gate (Stage 1)
- **Ancient Mesopotamia (Pre-330 BC):** Open [`../phase-07-image-prompt-engineering/mesopotamia-canon/canon-rules.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/canon-rules.md), then the canon's [`INDEX.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/INDEX.md), which lists every chapter and wardrobe file with its period and dates, turns a date or a period into the one or two files to read; [`CANON-LOOKUP.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/CANON-LOOKUP.md) is the id table, for a card you already have a name for. Apply [`heritage-rules.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md) as well: its Part B covers the ancient subject as much as the modern one. **The canon verifies the visual and material world** — the place, the building, the garment, the object, the god as depicted, the army in the field. **It does not verify king names, regnal dates or event chronology**; those come from a quick web search, recorded under `decisions`. Full wording in [`HOW-PHASE-1-WORKS.md`](HOW-PHASE-1-WORKS.md) §2.1.
- **Modern Assyrian Heritage:** Open [`../phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md). That file is the only copy of those rules and they are not restated here: apply its **Part A** as that file scopes it under *Which of these apply*, and its **Part B only when the subject is Mesopotamian or Assyrian heritage as heritage**. A Syriac Christian subject falls under Part A rule 4, not under the Part B heritage-frame rule.
- **Foundation Correction Rule:** If research breaks the premise on a piece the user wants accurate, choose the fix that keeps the brief's intent — a correction, a change of direction, a reduced scope, a real substitute or a partial return — record it under `decisions`, and carry on. The options are the agent's to choose between, never a question for the user.

### 3. Story Engineering & Card Activation
- **Interactive or branching piece?** Consult [`interactive-and-branching.md`](interactive-and-branching.md) — every `inter.*` card: branching shape, agency, in-world writing, the ethics of a nonfiction branch, second person, choice framing, string budgets, and what a platform will and will not allow. The count is in the file registry below, which is generated; it is not repeated here.
- **Hook Engineering (First 3 Seconds, interrupted arrivals only):** The three-second hook is a rule about one delivery situation, not a Phase 1 principle. It applies when the viewer **did not choose this piece** — a feed scroll, a pre-roll, a paid social advert, an autoplaying next item — and a paid ad is the hardest case, not an exception. It does **not** apply when the viewer chose it: a search result, a subscription, a link someone sent, a documentary put on deliberately. There the opening move is the first thirty seconds that earn the next five minutes. Full sort in [`HOW-PHASE-1-WORKS.md`](HOW-PHASE-1-WORKS.md) §3.A. Consult [`short-form-craft.md`](short-form-craft.md). Enforce dual-hook (`sf.first_line_both_ways`), front-loading (`sf.front_load`), and single idea (`sf.one_point`). The line-writing half of those three is `sfl.*` in [`../phase-02-screenplay-dialogue/script-craft/short-form-lines.md`](../phase-02-screenplay-dialogue/script-craft/short-form-lines.md); the `sf.` cards are the authority.
- **Structure & Beat Skeletons:** Consult [`structures.md`](structures.md) and the format kits. For a 45-to-60-second piece the beat skeleton is `sf.four_beat_reel` in [`short-form-craft.md`](short-form-craft.md), and that card is the only authority for its timings — read them there. The brief's runtime is never changed to fit the grid; [`HOW-PHASE-1-WORKS.md`](HOW-PHASE-1-WORKS.md) §3.B gives the shapes for other lengths.
- **Character & Conflict:** Consult [`cat-char.md`](cat-char.md) and [`cat-anta.md`](cat-anta.md).

### 4. Produce Deliverable: Story Foundation Brief
Format the final output:
- Working Title & Logline
- Destination, Platform, Aspect Ratio & Audio Profile
- Arrival (Interrupted / Chosen) — which decides whether the next line is a hook or an opening move
- The Hook Specification (Spoken text & on-screen text), or the Opening Move on a chosen arrival
- Character Dossier & Opposing Force
- Appearance, one optional line per recurring character (build, apparent age, hair, one distinguishing thing, what they wear) — a decision carried forward, **not** a frozen prompt sentence; that is `ident.frozen_sentence` and it belongs to Phase 7. Spec in [`HOW-PHASE-1-WORKS.md`](HOW-PHASE-1-WORKS.md) §5.
- Step Outline / Beat Sheet (Chronological narrative events)
- Retention & Engagement Strategy
- Warning List (Collected non-blocking advisory notes)

## Reference Architecture (Progressive Disclosure)
- Master Index: [`INDEX.md`](INDEX.md)
- Card Search Directory: [`LOOKUP.md`](LOOKUP.md) (1,332 cards)
- Detailed Specification: [`HOW-PHASE-1-WORKS.md`](HOW-PHASE-1-WORKS.md)
- Short-Form Craft: [`short-form-craft.md`](short-form-craft.md)
- Mesopotamia Canon: [`mesopotamia-canon-reference.md`](mesopotamia-canon-reference.md)

<!-- GENERATED:file-registry — do not edit by hand. Generated in the source package -->

## Files in this phase

**81 craft files, 1,332 cards** in this phase directory, every one linked below, so nothing is more than one hop away. Card-level lists are in [`INDEX.md`](INDEX.md); the searchable id table is in [`LOOKUP.md`](LOOKUP.md), with 16 per-family shards beside it, generated from the same source. Any id in the package, from any phase, resolves in [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers | Cards |
| :--- | :--- | ---: |
| [`interactive-and-branching.md`](interactive-and-branching.md) | **Interactive and branching narrative** — **Every `inter.*` card** - every piece the viewer navigates, on a feed or not: branching shape, agency, in-world writing, interactive nonfiction and testimony, generated and conversational pieces, second person, choice framing and option order, timed choices, string budgets, the meaningful-choice test. <br>*Cards scoped to: any format* | 74 |
| [`short-form-craft.md`](short-form-craft.md) | **Short-Form Craft & Scripting Cards — Master Edition** — High-retention hooks, micro-narratives, and vertical short-form beat compression <br>*Cards scoped to: any format* | 87 |
| [`structures.md`](structures.md) | **Structure systems** — Classic story structures: Three-Act, Hero's Journey, Save the Cat, and 5-Act forms <br>*Cards scoped to: any format* | 110 |
| [`cat-char.md`](cat-char.md) | **Character Design, Desire, Wound and Lie** — Fundamental character design: desire, core wound, lie believed, and primary motivation <br>*Cards scoped to: mostly Feature Film, Novel, Limited Series / Drama, One-Hour Drama, among 12 formats* | 34 |
| [`cat-char-2.md`](cat-char-2.md) | **Character Design — Part 2** — Character flaws, secret wounds, psychological contradictions, and internal stakes <br>*Cards scoped to: mostly Feature Film, Novel, Limited Series, One-Hour Drama, among 16 formats* | 40 |
| [`cat-char-3.md`](cat-char-3.md) | **Character Design — Part 3** — Advanced character craft: disguises, double identities, crowd roles, and moral drift <br>*Cards scoped to: any format* | 45 |
| [`cat-char-4.md`](cat-char-4.md) | **Character Design — Part 4** — Writing real and non-actor subjects: sayable lines, class tells, representative burden, audience review, language, and memory <br>*Cards scoped to: mostly Feature Film, Limited Series, Novel, Heritage Documentary, among 19 formats* | 10 |
| [`cat-anta.md`](cat-anta.md) | **Antagonist, Opposition and Obstacle Design** — Antagonist design, nemesis profiles, opposing forces, and obstructive barriers <br>*Cards scoped to: any format* | 27 |
| [`cat-anta-2.md`](cat-anta-2.md) | **Antagonist and Opposition — Part 2** — Antagonist depth: justified motivations, philosophical foils, and systemic opposition <br>*Cards scoped to: any format* | 31 |
| [`cat-beat.md`](cat-beat.md) | **Beat Exchange, Action and Reaction** — Action-reaction beat exchanges, micro-negotiations, and momentum shifts <br>*Cards scoped to: mostly novel, screenplay, stage play, teleplay, among 11 formats* | 32 |
| [`cat-beat-2.md`](cat-beat-2.md) | **Beat Exchange, Action and Reaction — Part 2** — Ensemble, mediated and off-screen beats; beats in song and other media; handoffs, pressure, notation, and testing <br>*Cards scoped to: any format* | 39 |
| [`arcs.md`](arcs.md) | **Character Arcs** — Core character transformation arcs, positive/negative changes, and tragic trajectories <br>*Cards scoped to: any format* | 41 |
| [`arcs-2.md`](arcs-2.md) | **Character Arcs — Part 2** — Complex arc architectures: flat arcs, corrupted arcs, and collective community arcs <br>*Cards scoped to: mostly Limited Series, Novel, Comics, Feature Film, among 33 formats* | 12 |
| [`cat-end.md`](cat-end.md) | **Endings, Payoff and Resolution** — Climax resolution, thematic payoffs, poetic justice, and emotional aftermath <br>*Cards scoped to: any format* | 24 |
| [`cat-end-2.md`](cat-end-2.md) | **Endings — Part 2** — Ending choices by genre and form, final-season and interactive endings, credits, short-form closes, and ending rewrites <br>*Cards scoped to: any format* | 40 |
| [`cat-end-3.md`](cat-end-3.md) | **Endings and Last Lines — Part 3** — The chapter ending as a prose-specific close and continuation device <br>*Cards scoped to: mostly Long-Form Non-Fiction, Memoir, Middle Grade, Novel, among 6 formats* | 1 |
| [`cat-expo.md`](cat-expo.md) | **Exposition and World Delivery** — Exposition delivery: invisible exposition, scenic embedding, and lore distribution <br>*Cards scoped to: any format* | 33 |
| [`cat-expo-2.md`](cat-expo-2.md) | **Exposition and World Delivery — Part 2** — Exposition by genre and apparatus: casualties, jokes, incidents, canon assumptions, voiceover, interviews, graphics, framing text, and found documents <br>*Cards scoped to: mostly Series, Feature Film, Novel, Documentary, among 48 formats* | 28 |
| [`cat-expo-3.md`](cat-expo-3.md) | **Exposition and World Delivery — Part 3** — Complex world exposition: esoteric magic, deep lore, and multi-generational history <br>*Cards scoped to: mostly Educational, Explainer, Corporate, UX Writing, among 29 formats* | 12 |
| [`cat-expo-4.md`](cat-expo-4.md) | **Exposition and World Delivery — Part 4** — Written-form exposition: re-entering a novel after a gap and the framing furniture around a page <br>*Cards scoped to: mostly Comics, Novel, Audiobook, Essay, among 10 formats* | 2 |
| [`cat-info.md`](cat-info.md) | **Information Control, Reveal and Withholding** — Information withholding, delayed disclosure, clues, and mystery architecture <br>*Cards scoped to: mostly Feature Film, Novel, Limited Series, One-Hour Drama, among 13 formats* | 32 |
| [`cat-info-2.md`](cat-info-2.md) | **Information Control — Part 2** — Information control: reveals, secrets, dramatic irony, and audience knowledge asymmetry <br>*Cards scoped to: any format* | 38 |
| [`cat-info-3.md`](cat-info-3.md) | **Information Control, Reveal and Disclosure — Part 3** — Compelled information, trust and credibility budgets, corrections, sourcing, attribution, and unverifiable allegations <br>*Cards scoped to: mostly Podcast, Documentary Series, Reportage, Documentary, among 32 formats* | 12 |
| [`cat-info-4.md`](cat-info-4.md) | **Information Control — Part 4** — Fact-check passes and handling a source whose name cannot be published <br>*Cards scoped to: mostly Documentary, Long-Form Non-Fiction, Podcast, Reportage, among 8 formats* | 2 |
| [`cat-open.md`](cat-open.md) | **Openings, Hooks and First Pages** — First scene craft, initial status quo, inciting incidents, and call to adventure <br>*Cards scoped to: any format* | 28 |
| [`cat-open-2.md`](cat-open-2.md) | **Openings — Part 2** — Advanced opening hooks, cold opens, in-media-res entry points, and curiosity gaps <br>*Cards scoped to: any format* | 39 |
| [`cat-open-3.md`](cat-open-3.md) | **Openings — Part 3** — The nut graf: opening a reported or explanatory piece by stating why it matters <br>*Cards scoped to: mostly Documentary, Essay, Explainer, Long-Form Non-Fiction, among 6 formats* | 1 |
| [`cat-rel.md`](cat-rel.md) | **Relationship and Ensemble Dynamics** — Relationship dynamics, alliances, power struggles, and relational polarity shifts <br>*Cards scoped to: any format* | 33 |
| [`cat-rel-2.md`](cat-rel-2.md) | **Relationship and Ensemble Dynamics — Part 2** — Ensemble cast dynamics, conflicting loyalties, trios, and institutional pressure <br>*Cards scoped to: mostly Novel, Feature Film, Stage Play, Limited Series, among 20 formats* | 28 |
| [`cat-seq.md`](cat-seq.md) | **Sequence and Mid-Level Movement** — Mid-level sequence architecture, mission segments, and narrative blocks <br>*Cards scoped to: any format* | 33 |
| [`cat-seq-2.md`](cat-seq-2.md) | **Sequence and Mid-Level Movement — Part 2** — Sequence planning and placement: outlines, mid-run turns, entries, payoff ledgers, runtime counts, subplots, thematic runs, transposition, and embedded runs <br>*Cards scoped to: mostly Feature Film, Limited Series, Novel, One-Hour Drama, among 36 formats* | 28 |
| [`cat-struct-2.md`](cat-struct-2.md) | **Structure — Forms and Doctrines** — Short written forms: flash fiction, linked collections, and Poe's unity of effect <br>*Cards scoped to: mostly Short Story, Flash Fiction, Poetry, Advertising, among 12 formats* | 3 |
| [`cat-tens.md`](cat-tens.md) | **Tension, Suspense, Surprise and Dread** — Core narrative tension, conflict sources, anticipation, and threat mechanics <br>*Cards scoped to: mostly Feature Film, Limited Series, Novel, One-Hour Drama, among 12 formats* | 31 |
| [`cat-tens-2.md`](cat-tens-2.md) | **Tension and Dread — Part 2** — Tension escalation, suspense mechanics, ticking clocks, and pressure amplification <br>*Cards scoped to: any format* | 39 |
| [`cat-tens-3.md`](cat-tens-3.md) | **Tension and Dread — Part 3** — Soft and dropped deadlines, visible consequences, confined pressure, sub-thirty-second tension, and instructions read under stress <br>*Cards scoped to: mostly Feature Film, Novel, One-Hour Drama, Limited Series, among 23 formats* | 10 |
| [`cat-tens-4.md`](cat-tens-4.md) | **Tension, Suspense, Surprise and Dread — Part 4** — Deep psychological dread, paranoia, claustrophobic suspense, and unavoidable doom <br>*Cards scoped to: mostly Novel, Stage Play, Feature Film, Limited Series, among 29 formats* | 20 |
| [`cat-tens-5.md`](cat-tens-5.md) | **Tension, Suspense, Surprise and Dread — Part 5** — Pursuits that pause, dream-logic suspense, tension against known outcomes, child-readable jeopardy, and subtitles that precede speech <br>*Cards scoped to: mostly Feature Film, Limited Series, Animation Feature, Documentary, among 21 formats* | 5 |
| [`cat-theme.md`](cat-theme.md) | **Theme, Controlling Idea and Moral Argument** — Central theme definition, thematic premises, and moral choices testing characters <br>*Cards scoped to: any format* | 25 |
| [`cat-theme-2.md`](cat-theme-2.md) | **Theme and Meaning — Part 2** — Thematic resonance, symbolic motifs, moral arguments, and subtextual weight <br>*Cards scoped to: any format* | 31 |
| [`cat-time.md`](cat-time.md) | **Time, Chronology and Flashback** — Pacing time, story vs plot duration, ellipsis, and chronological progression <br>*Cards scoped to: mostly novel, feature film, short story, stage play, among 38 formats* | 32 |
| [`cat-time-2.md`](cat-time-2.md) | **Time, Chronology and Flashback — Part 2** — Temporal manipulation: non-linear timelines, flashbacks, memory frames, and time jumps <br>*Cards scoped to: mostly Novel, Limited Series, Feature Film, Short Story, among 33 formats* | 33 |
| [`rights-and-permissions.md`](rights-and-permissions.md) | **Rights and permissions — optional craft for when a brief raises rights** — **What has to be settled before a shot list exists** - permission to film a protected site and who owns what an excavation produced, the provenance and licence terms of found material, the rights and the caption limits on a picture of an object, and the sequencing rule that puts all three before the design rather than before the delivery. States requirements and where the work hands over; no procedure. <br>*Cards scoped to: mostly Documentary Feature, Documentary Series, Heritage / Historical Documentary, Museum Installation, among 16 formats* | 6 |
| [`secondary-world.md`](secondary-world.md) | **An invented world drawn from a real culture** - what may never be borrowed (every proper noun), what may (the materials, the light, the mass), and how an invented pantheon, calendar and script stay coherent across a series. Not the same job as fiction set inside the documented period, which is the canon's. <br>*Cards scoped to: mostly Animated Series, Comics, Game Narrative, Novel, among 12 formats* | 3 |
| [`situations.md`](situations.md) | **Dramatic Situations and Narrative Functions** — Universal dramatic situations, catalytic conflicts, and crisis generators | 98 |

### Kits and routers — they rank cards, they do not define them

These carry no card of their own, which is why a card count is not the way to find them. They are usually the fastest way in: a kit names the shape you are making and hands you a ranked list. Take the paths from [`../CARD-INDEX.md`](../CARD-INDEX.md).

| File | What it covers |
| :--- | :--- |
| [`by-format-animation.md`](by-format-animation.md) | Animation narrative adaptations: visual metaphor, physical logic, and character elasticity |
| [`by-format-doc.md`](by-format-doc.md) | Documentary narrative structure: thesis building, subject trust, and truth discovery |
| [`by-format-film.md`](by-format-film.md) | Feature film pacing: midpoint reversal, all-is-lost moment, and climax orchestration |
| [`by-format-kids.md`](by-format-kids.md) | Children's storytelling: clarity of stakes, emotional safety, and joyful discovery |
| [`by-format-social.md`](by-format-social.md) | Social video structure: hook pacing, continuous micro-rewards, and seamless loops |
| [`by-format-tv.md`](by-format-tv.md) | Television episodic architecture: A/B/C plotting, commercial breaks, and season arcs |
| [`formats-animation.md`](formats-animation.md) | Animation formats: Animated Series (kids), Animated Series (adult), Anime, Short Animation, Stop Motion and Craft Animation, Motion Graphics and Explainer Animation |
| [`formats-doc.md`](formats-doc.md) | Documentary formats: Feature Documentary, Documentary Series, Heritage and Historical Documentary, Reportage and Current Affairs, Essay Film, Interview-Led Documentary, True Crime, Observational and Vérité Feature, Archive-Only Film, Nature and Natural History, Sports Documentary, Music Documentary, First-Person Diary Film, Personal-Archive Family Film, The Documentary Short, Interactive Documentary, Interactive Testimony and Oral History, Museum and Installation Narrative |
| [`formats-film.md`](formats-film.md) | Film formats: Feature Film, Short Film, Animation Feature, Trailer and Teaser |
| [`formats-kids.md`](formats-kids.md) | Children's formats: Preschool (2–5), Kids' Song, Children's Picture Book, Educational and Explainer for Children, Middle Grade and Older Children (8–12), Early Reader and Chapter Book (5–9), Young Adult, Kids' Non-Fiction, Interactive and App-Based Children's Content, Kids' Content Across Translation and Dubbing, Faith and Heritage Content for Children |
| [`formats-social.md`](formats-social.md) | Social and short-form formats: Vertical Micro-Drama, Reels, Shorts and TikTok, Long-Form Video (YouTube), Web Series and Serialised Short-Form, Carousel, Thread and Text Post, Podcast Clip, Livestream Script, Branded Serial, Creator Brand Partnership (Organic), Community Post, Instagram Reel, TikTok, YouTube Shorts |
| [`formats-tv.md`](formats-tv.md) | Television formats: One-Hour Drama, Half-Hour Comedy, Limited Series, Television Pilot, Procedural / Case of the Week, Soap and Continuing Drama |
| [`genres-bond.md`](genres-bond.md) | Bonding genres: Love Story, Romantic Comedy, Buddy Love, Family Drama, Ensemble |
| [`genres-form.md`](genres-form.md) | Genres of form and tone: Comedy, Satire, Tragedy, Melodrama, Psychological and Arthouse, Surreal and Absurdist, Horror-Comedy |
| [`genres-growth.md`](genres-growth.md) | Growth genres: Coming of Age, Rites of Passage, Sports, Redemption, Fool Triumphant, Underdog |
| [`genres-inquiry.md`](genres-inquiry.md) | Inquiry genres: Detective, Mystery, Whydunit, Courtroom and Legal, Investigation and Journalism |
| [`genres-nonfiction.md`](genres-nonfiction.md) | Non-fiction genres: Memoir, Biography, Personal Essay, Reportage, Advocacy, Instructional and How-To, Nature and Science |
| [`genres-primal.md`](genres-primal.md) | Primal genres: Horror, Thriller, Action, Crime, Gangster, War, Survival |
| [`genres-world.md`](genres-world.md) | Worldbuilding and period genres: Myth, Fantasy and Epic, Science Fiction, Dystopia, Western, Heritage (civilisation-focused), Historical and Biopic |
| [`intents.md`](intents.md) | Authorial narrative intent, thematic focus, and audience emotional targeting |
| [`mesopotamia-canon-reference.md`](mesopotamia-canon-reference.md) | Mesopotamia Canon & Heritage Worldbuilding Reference — Department Owner: **Art & Visual Look Bible (Phase 7: Image Prompt Engineering)** |
| [`reels-engagement-and-dilemmas.md`](reels-engagement-and-dilemmas.md) | **Pointer only.** Its cards moved to `interactive-and-branching.md`; a filename is a routing signal and this one sent branching work to the short-form route. |
| [`symptoms-antagonist-and-opposition.md`](symptoms-antagonist-and-opposition.md) | Antagonist diagnostic: toothless villains, arbitrary obstacles, and weak stakes |
| [`symptoms-beat-and-sequence.md`](symptoms-beat-and-sequence.md) | Beat & sequence diagnostic: dead time, repetitive action, and pacing lag |
| [`symptoms-character.md`](symptoms-character.md) | Character diagnosis: flat motivations, inconsistent agency, and arc stalls |
| [`symptoms-commissioned-and-applied-work.md`](symptoms-commissioned-and-applied-work.md) | Commissioned and applied-work complaints — Part of the symptom router. Open this file when the complaint is about commissioned and applied-work. |
| [`symptoms-exposition-and-world.md`](symptoms-exposition-and-world.md) | Exposition diagnostic: talking heads, encyclopedic info dumps, and world drift |
| [`symptoms-information.md`](symptoms-information.md) | Information diagnostic: plot confusion, obvious twists, and unearned revelations |
| [`symptoms-misc.md`](symptoms-misc.md) | Small complaint families — Families holding one or two complaints, kept together rather than shipped as files with a single entry each. |
| [`symptoms-opening.md`](symptoms-opening.md) | Opening diagnostic: slow starts, exposition dumps, and unhooked audience |
| [`symptoms-relationship-and-ensemble.md`](symptoms-relationship-and-ensemble.md) | Ensemble diagnostic: indistinct voices, redundant characters, and shallow chemistry |
| [`symptoms-short-form-and-serial.md`](symptoms-short-form-and-serial.md) | Short-form diagnostic: second-3 drop-offs, weak loop-backs, and low shareability |
| [`symptoms-structural.md`](symptoms-structural.md) | Structural diagnostics: saggy middles, missed act turns, and weak climaxes |
| [`symptoms-tension.md`](symptoms-tension.md) | Tension diagnostics: low stakes, premature resolution, and unearned relief |
| [`symptoms-theme.md`](symptoms-theme.md) | Thematic diagnostic: preachy dialogue, didactic lessons, and hollow moral arcs |
| [`symptoms-time-and-chronology.md`](symptoms-time-and-chronology.md) | Chronology diagnostic: disorienting timeline jumps and pacing flatlines |
| [`symptoms.md`](symptoms.md) | Master narrative symptom diagnostic index for story ailments and quick remedies |

<!-- /GENERATED:file-registry -->

## The contract for this phase

<!-- GENERATED:stage-contract — do not edit by hand. Generated in the source package -->

**This phase's contract.** Generated from the table in [`PROJECT-STATE.md`](../PROJECT-STATE.md), which is the authority — a decision is read from `project.yaml` and never from another phase's document, and a lock this phase may not re-decide is one it takes as given even when it disagrees — and where it finds the value wrong, it sends it back to the phase that owns it (rule 2 of that file) rather than changing it here.

| | |
| :--- | :--- |
| **Required reads** | `format`, `genre`, `language`, `duration_s`, `audio_profile` |
| **One-of read groups** | — |
| **Optional reads** | `age_band` |
| **External inputs allowed** | — |
| **Writes** | `story_brief`, `branch_map`, `forbidden_global`, `render_mode`, `looks` |
| **May not re-decide** | `format`, `genre`, `duration_s` |
| **Execution gate** | — |

A required key that is empty **never stops the work**: fill it by the working rule in the root [`SKILL.md`](../../SKILL.md) §0 (the brief, the skill, the web, then the most suitable choice) and record the choice under `decisions`. `render_mode` and `looks` are defined in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set. An execution gate blocks a paid or quota-consuming tool call; it does not block writing the prompt or the handoff.

<!-- /GENERATED:stage-contract -->

<!-- GENERATED:route-handoffs — do not edit by hand. Generated in the source package -->

**Route-specific handoffs.** Generated from the route-profile table in [`PROJECT-STATE.md`](../PROJECT-STATE.md). This table, not a phase number or a prose sentence elsewhere, decides what comes before and after this phase.

| Route profile | Receives from | Hands to |
| :--- | :--- | :--- |
| `full_narrative` | `external / intake` | `phase-02-screenplay-dialogue` |
| `narrated_documentary` | `external / intake` | `phase-02-screenplay-dialogue` |
| `music_video` | `external / intake` | `phase-05-song-generation` |
| `commercial` | `external / intake` | `phase-02-screenplay-dialogue` |
| `commercial_narrated` | `external / intake` | `phase-02-screenplay-dialogue` |
| `storyboard_only` | `external / intake` | `phase-02-screenplay-dialogue` |
| `one_still` | `external / intake` | `phase-07-image-prompt-engineering` |
| `audio_only` | `external / intake` | `phase-02-screenplay-dialogue` |
| `audio_with_cover` | `external / intake` | `phase-02-screenplay-dialogue` |
| `interactive_branching_silent` | `external / intake` | `phase-02-screenplay-dialogue` |
| `interactive_branching_audio` | `external / intake` | `phase-02-screenplay-dialogue` |
| `data_led_built` | `external / intake` | `phase-02-screenplay-dialogue` |

The rows show each profile as declared. When the story itself contains a song that sets timing, Phase 5 is added after Phase 4 and before Phase 3 on any route that runs Phase 3, and the neighbours shift accordingly ([`PROJECT-STATE.md`](../PROJECT-STATE.md) §2).

<!-- /GENERATED:route-handoffs -->

---
