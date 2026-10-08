---
name: ai-film-pipeline-master
description: "Master autonomous end-to-end 8-phase AI film and video production pipeline. From an initial idea, brief, or script, autonomously directs Story Generation (1,332 cards), Screenplay & Dialogue (585 cards), Shooting Script (768 cards), Audio Narration (260 cards), Song & Music Generation (340 cards), Storyboard Layout (194 cards), Image Prompt Engineering (889 cards, the Mesopotamia Canon included), and Video Prompt Engineering (394 cards). Contains 4,762 standardized craft cards. Use this whenever the user wants to develop, write, direct, storyboard, score, or generate an AI film, short, reel, ad, music video, or commercial. Trigger on any request to create a movie, film, short, reel, commercial, music video, documentary, screenplay, storyboard, voiceover, Suno music track, image prompt, or AI video motion prompt, or any Arabic phrasing: سويلي فيلم، سويلي فيديو، اكتبلي سيناريو، ستوري بورد، برومت صور، برومت فيديو، ريلز، اعلان، اغنية سونو، تعليق صوتي، اخراج سينمائي."
---

# Master Autonomous AI Film & Video Production Pipeline

A complete, production-grade 8-phase creative framework engineered for autonomous AI agents (Antigravity, Claude Code, Hermes Agent, OpenAI Codex, and Cursor). 

From a single prompt or creative brief, this pipeline executes the full Hollywood and frontier AI studio workflow across **8 sequential phases** comprising **4,762 standardized craft cards** (and **5,386 total searchable headings**).

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [0. The working rule — nothing stops the work](#0-the-working-rule-nothing-stops-the-work)
- [1. Quick Route & Project Diagnosis](#1-quick-route-project-diagnosis)
- [2. The 8 Sequential Production Phases](#2-the-8-sequential-production-phases)
- [3. The 8-Field Standardized Craft Card Schema](#3-the-8-field-standardized-craft-card-schema)
- [3a. When Two Cards Disagree](#3a-when-two-cards-disagree)
- [3b. Two things to fill before the first prompt](#3b-two-things-to-fill-before-the-first-prompt)
- [3c. How to read this installed skill](#3c-how-to-read-this-installed-skill)
- [4. Master Agent Execution Instructions](#4-master-agent-execution-instructions)

<!-- /GENERATED:toc -->

## 0. The working rule — nothing stops the work

**This skill exists to speed production up.** Whatever is missing, unclear or in conflict — a fact, a
figure, a source, a reference image, a speaking rate, a length, a card that disagrees with another —
is settled in this order, and the work never waits for it:

1. **The brief.** What the user asked for is the answer: language, dialect, length, format, aspect,
   size, colour, style, how real or how stylised. It is written as asked, with no argument.
2. **The skill.** Search [`references/CARD-INDEX.md`](./references/CARD-INDEX.md) and the canon for a card or a reference.
3. **The web.** Search it and take the most suitable, current answer.
4. **Your own best choice.** When nothing turns up, choose what best serves the piece.

**Then record the choice under `decisions` in `project.yaml` and carry on.** Never stop, never ask
the user a craft, taste, fact or timing question, and never leave a gap as a question.

**Sources and historical accuracy matter only on a history piece the user wants realistic** — built
the way it looks on the reliefs and in the museums. Even there it is the same order: a reference that
exists is used; none found in the skill, search the web; none found there, generate with the closest
thing. It is never a condition and never a stop. On any other piece, facts and sources are not part
of the job.

**Only three things wait for a person, and all three are the user's own:** the spend approval
(`paid_generation_approved_by`), the keyframe approval before video prompts (`keyframes_approved_by`),
and a real person's consent before their voice or likeness is cloned (for a real child, the parent's —
`references/phase-04-audio-narration/HOW-PHASE-4-WORKS.md`, Step 1). Nothing else holds the work: there are no
rights, permission or licence steps in this skill.

**Two methods this skill does not write, and neither is a stop.** It writes no concealment technique
for a person who must not be identified, and no brightness or rate threshold for a strobe or a rapid
flash sequence (`safety.photosensitive_flash`). Everything else in the piece is written; the note goes
in the handoff for whoever delivers. Ordinary light — firelight, candles, a lamp, a sunset — is never a
flash question.

## 1. Quick Route & Project Diagnosis

When a user provides a brief, work out the route in two moves: the six questions below, which
every brief can answer, and then the table, which is a shortcut for the shapes that come up often.

### The six questions — these have no gap

A table of named product types always has a hole in it, because the next brief is a kind nobody
listed. These are questions instead, and **every piece answers every one of them.** Start with all
eight phases, then let the answers take phases out and put phases in.

| Ask | If yes | If no |
| :--- | :--- | :--- |
| **1. Is there a picture at all?** | go to question 1b | drop Phases 3, 6 and 8 — a podcast, an audio documentary, an audio drama, a listening post, a guided audio walk. Phase 2 uses its **Pipeline C**, the audio-only script, and the format kits for this work are in Phase 4's [`formats-audio.md`](./references/phase-04-audio-narration/formats-audio.md) — Narrative Podcast, Interview Podcast, Radio and Audio Drama, Audiobook Narration, Voiceover Script — not in Phase 1, whose format kits are all picture formats. Phase 7 still runs **if there is any single still to make** — cover art, a thumbnail, a poster — and only for that still |
| **1b. Does it end in a moving picture?** | keep Phase 8 | drop Phase 8 — a poster, key art, sheets, a deck nobody animates |
| **2. Is there a song the picture has to cut to?** | Phase 5 comes **before** Phase 3, and its timing map governs — including a song sung or played inside a scene: Phase 5 runs for that song after Phase 4 and before Phase 3 ([`references/PROJECT-STATE.md`](./references/PROJECT-STATE.md) §2) | Phase 5 runs only for score direction (after Phase 4, before Phase 3) — its Route C in [`HOW-PHASE-5-WORKS.md`](./references/phase-05-song-generation/HOW-PHASE-5-WORKS.md), recorded under `route.craft_only` — or is skipped |
| **3. Is there any speech whose length sets the runtime?** | Phase 4 comes **before** the picture phases, and the measured audio sets the shot table — **unless the picture is found rather than made.** Archive footage, a filmed performance, a recorded interview: those shots have real lengths nobody can change, so the picture is fixed and **the narration is written to fit it**, not the reverse. `rhythm.locked_picture_narration` is that job. Cutting found footage to fit a voice is the one place this question does real damage, and it does it invisibly. A real object shown by its photograph — a museum piece, a relief — is found picture too (`engine: none - captured`); a still has no length of its own, so its duration is designed. A reconstruction generated from a reference is made picture | the durations are designed, and Phase 3 says so |
| **4. Does the viewer choose what happens next, *or* choose when to arrive and leave?** | **If they choose what happens:** open [`interactive-and-branching.md`](./references/phase-01-story-generation/interactive-and-branching.md) first, and add Phase 2 for the on-screen text. **If they only choose when** — a gallery loop, a museum wall, a shop window, a listening post, anything a passer-by enters mid-way and leaves at will — you are not making branching work, but the **walk-up craft is the same craft**: `inter.walk_up_entry` and the three kits at the end of [`formats-doc.md`](./references/phase-01-story-generation/formats-doc.md), which carry the measured word counts for an audience that sets its own clock | no branching and no walk-up material needed |
| **5. Is an element in a specific frame contractually required, or named by the brief?** | Phase 2 is not optional — the line's rhythm decides whether it lands. **On a song-led route (`music_video`, `score_existing_film`) the lyric sheet does that job and Phase 2 does not run**: a sign, caption or end card the brief names takes its words from the brief and goes straight to [`in-frame-text.md`](./references/phase-07-image-prompt-engineering/in-frame-text.md). **For a brand lock-up, pack shot or end card**, the lock-up rules in [`references/phase-03-shooting-script/ads-trailers.md`](./references/phase-03-shooting-script/ads-trailers.md) govern the last frame. On any end card, a page name or credit card on a non-commercial piece included, those rules govern its form and hold, and the credit and call-to-action material below governs the words written on it. **For any other required final frame** — a credit, a legal line, a funder's logo, a call to action, or a loop point that must join the opening — those rules do not apply and Phase 1's ending craft does not cover a *compelled* frame either. The material that does: `rhythm.disclosure_as_content` in Phase 2 for making a required disclosure part of the piece rather than an appendix to it, `info.source_on_screen` for a credit or attribution that has to be legible, and the epilogue and end-card craft in Phase 3's documentary and ads files. For a loop point that must join the opening, the join is in Phase 8's `time.loop` | the ending is a story beat |
| **6. Is the subject Mesopotamia between roughly 4000 BC and 330 BC?** A present-day piece with an ancient flashback or sequence answers yes for those frames only | the canon opens, for the frames it covers: [`references/phase-07-image-prompt-engineering/mesopotamia-canon/canon-rules.md`](./references/phase-07-image-prompt-engineering/mesopotamia-canon/canon-rules.md), then Part B of [`heritage-rules.md`](./references/phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md) | the canon stays shut, and only Part A applies, as `heritage-rules.md` scopes it under *Which of these apply*. **Below about 4000 BC it stays shut too** — the canon holds no Neolithic material, its earliest chapter is Uruk, and a Göbekli Tepe or Çatalhöyük brief is researched from the site literature |

**Phase 1 runs on every route that builds a piece from a brief**, even when the table below looks
like it skips it: every other phase needs a spine, and ten minutes there is cheaper than a piece
with no centre. The supplied-material shortcuts (`supplied_script_voiceover`,
`supplied_audio_cleanup`, `supplied_stills_video`, `score_existing_film`) start where their input
feeds and have no Phase 1; that is their design, not a skipped step. **Phase 6 runs wherever a
sequence of frames will be generated** — it is the staging and panel phase, so it has nothing to
stage on a piece with no picture, and a single still is laid out in Phase 7's own still-image design
record rather than boarded. That is a condition, not an exception: question 1 is what decides it.

**Why questions and not only a table.** A table of named types is a taxonomy, and a taxonomy always has a hole in it — the next brief is a kind nobody listed. Three separate end-to-end test runs hit that hole. This follows Anthropic's own skill guidance, which routes by decision point rather than by name and says to give a default with an escape hatch: the table is the default, the questions are the escape hatch, and the escape hatch is the part that cannot fail.

**One rule under all six:** a route decides which *deliverables* get made. It never decides which
craft you may read. Any card in the package is one hop away in [`references/CARD-INDEX.md`](./references/CARD-INDEX.md),
whatever route you are on.

### The table — a shortcut, not the authority

These are the shapes that come up often, already worked through the six questions. If your brief is
one of them, take the row. If it is not, the questions above are the answer — and that is the normal
case, not a failure.


| Project Brief / Goal | Execution Route | Contract profile(s) |
| :--- | :--- | :--- |
| **Full Cinematic Film (Director Review)** | Review pauses the owner opted into (not gates); with the owner absent the run falls back to prompts only (HOW-1 Q1) | `full_narrative` or `narrated_documentary`; use `music_video` when the song owns timing |
| **Express Auto Film / Short** | Automated End-to-End — the row to take when a film brief names no mode | The same three profiles; automation changes gates, not dependencies |
| **Music Video / Song Track** | Song & Visual Clip Route | `music_video` |
| **Commercial / Ad / Promo / TVC** | High-Impact Ad Route | `commercial` |
| **Commercial with a voice-over** | Narrated Ad Route: the voice is recorded and measured before the shot table | `commercial_narrated` |
| **Historical / Heritage Documentary** | Heritage Canon Route — in Phase 7, open the Mesopotamia canon ([its index](./references/phase-07-image-prompt-engineering/mesopotamia-canon/INDEX.md)) before any heritage prompt | `narrated_documentary` |
| **Storyboard & Concept Art Only** | Visual Pre-Production | `storyboard_only` |
| **One Still / Poster / Key Art** | Still Design Route | `one_still` |
| **AI Video Prompts from Stills** | Motion Kinetic Route | `supplied_stills_video` |
| **Audio Piece from This Pipeline** | Audio-Only Route | `audio_only`, or `audio_with_cover` when one still is required |
| **Voiceover from a Supplied Script** | Vocal Casting Shortcut | `supplied_script_voiceover` |
| **Cleanup or Mix of Supplied Audio** | Audio Restoration Shortcut | `supplied_audio_cleanup` |
| **Interactive / Installation / Branching** | Branching Route — open [`interactive-and-branching.md`](./references/phase-01-story-generation/interactive-and-branching.md) and the three installation kits in [`formats-doc.md`](./references/phase-01-story-generation/formats-doc.md) first | `interactive_branching_silent` or `interactive_branching_audio` |
| **Score for a Film That Already Exists** | Score Direction Route | `score_existing_film` |
| **Explainer / Data-Led Piece** | Information Route — open [`data-visualisation.md`](./references/phase-07-image-prompt-engineering/data-visualisation.md) first | `data_led_built` |

**Where a row and a question disagree, the question wins.** Two rows above used to run Phase 3 before Phase 4 on narrated pieces, which is the opposite of what question 3 answers — and this table's own header says these rows are *already worked through the six questions*, so a reader taking the shortcut got the wrong order with no sign that anything was wrong. The rows are the questions' output; they are never a second opinion.

**No row fits? That is expected.** Go back to the six questions above — they cover every brief,
including the ones nobody thought to name. Write down the route they gave you and why, the same way
you would record any other decision the package did not make for you.

---

## 2. The 8 Sequential Production Phases

> **Measurement Rule**: A **Core Craft Card** is defined as a `###` heading carrying a unique backticked identifier (`prefix.name`) specifying an actionable technique, prompt syntax, or cinematography setup. **Total Searchable Headings** includes diagnostic symptom questions in router files (`symptoms-*.md`), genre primers, and visual bridge tables (`vlb-*.md`). All numbers are verified directly from disk.

| Phase | Directory | Focus | Core Craft Cards | Total Searchable Headings |
| :--- | :--- | :--- | :---: | :---: |
| **Phase 1** | `phase-01-story-generation` | Dramatic Architecture | 1,332 cards | 1,672 headings |
| **Phase 2** | `phase-02-screenplay-dialogue` | Script & Character Voice | 585 cards | 781 headings |
| **Phase 3** | `phase-03-shooting-script` | Shot Breakdown & Audio | 768 cards | 773 headings |
| **Phase 4** | `phase-04-audio-narration` | Voiceover & Performance | 260 cards | 268 headings |
| **Phase 5** | `phase-05-song-generation` | Suno v6 / Lyria 3.5 | 340 cards | 349 headings |
| **Phase 6** | `phase-06-storyboard-layout` | Staging, Panels, Timing | 194 cards | 195 headings |
| **Phase 7** | `phase-07-image-prompt-engineering` | Optical Stills & Canon | 889 cards | 896 headings |
| **Phase 8** | `phase-08-video-prompt-engineering` | Temporal Motion Vectors | 394 cards | 414 headings |
| **Root files** | `SKILL.md`, `references/README.md`, `references/PRECEDENCE.md`, `references/ENGINE-CHECK.md`, `references/FORBIDDEN-GLOBAL.md`, `references/COLLISIONS.md` | Routing, precedence, project inputs | 0 cards | 38 headings |
| **TOTAL** | | **Master Production Pipeline** | **4,762 cards** | **5,386 headings** |

*(That total includes the Visual Language Bible bridge files and the Mesopotamia Canon; every card in the package is counted once, in the phase whose folder holds it.)*

**Before you re-count these and file a defect, read this.** Four independent testers have measured
this package and all four first reported it roughly four hundred short, and all four had the same
bug. **A card id can carry three dot-separated segments**, not only two — the Mesopotamia Canon and
the Visual Language Bible bridge both use that shape — and a regex allowing only two silently misses
every one of them. Subtract that many from the total and you get precisely the figure each of those
testers filed. Two smaller traps sit beside it: `<!-- GENERATED -->` blocks contain `###` headings,
which inflates a naive heading count, and a few cards are bold sub-card lead-ins under `####` rather
than `###`. Use the source package's build tools, which is what wrote these numbers. The counts have been right every
time; the counters have not.

**How to read these numbers.** Every figure in the table is measured from disk by the source package's build tools and written back, so none of them is typed by hand. **Cards** counts `###` headings carrying a unique backticked id; **headings** counts every `###` heading in the hand-written craft files — which is the larger number because the router files, genre primers and bridge tables carry headings that are not cards. It excludes the build's own the source package's build tools directory, the generated files (`INDEX.md`, the `LOOKUP` shards, `CANON-LOOKUP.md`) and any heading inside a `GENERATED:` block, because those are this system's output rather than its craft, and counting them would mean the number counted itself. Two testers have measured a discrepancy here and found their own counter at fault both times; the count is right and this sentence used to describe it wrongly. The card column includes the Phase 3 Visual Language Bible bridge, the Phase 6 bridge card and the Phase 7 Mesopotamia Canon, each counted once in the phase whose folder holds it. The Phase 7 row therefore runs ahead of that phase's own file registry, because the row counts the phase *and* its Mesopotamia Canon subfolder while the registry counts the folder alone. The difference is the canon, which is indexed separately because it has its own router and its own audience — not drift. **Both figures are generated, and neither is repeated here**, because a third copy of a number in a paragraph explaining the first two is how this paragraph went stale the first time it was written.

This paragraph used to claim a second, larger count of **4,760** distinct identifiers — smaller than the 4,761 it was offered as a fuller version of, which is a contradiction on its face. The cause was that the old counter also counted the schema's own worked example, `prefix.unique_card_id`, printed in the README and in this file to show the card shape. It is an illustration, not a card. The two routes now agree, and the source package's build tools reproduces the figure and reports `files that would change: 0`.

**Nothing in the package depends on any of these totals being exact** — no rule, no route and no card reads them. They say how much craft is in the box, and that is all they are for. The reason they are still generated rather than left approximate is that a stated number invites a reader to check it, and a number that does not survive being checked costs more trust than it was ever worth.

### Phase Directory Index & Core Manuals
1. **[Phase 1: Story Generation](./references/phase-01-story-generation/PHASE.md)** (1,332 core craft cards, 1,672 total headings)
   - Operational Guide: [HOW-PHASE-1-WORKS.md](./references/phase-01-story-generation/HOW-PHASE-1-WORKS.md) | [INDEX.md](./references/phase-01-story-generation/INDEX.md) | [LOOKUP.md](./references/phase-01-story-generation/LOOKUP.md)
   - *Directs*: Narrative architecture, the genre bibles, world-building grimoires, character archetypes, narrative tension engines, and thematic premises.
2. **[Phase 2: Screenplay & Dialogue](./references/phase-02-screenplay-dialogue/PHASE.md)** (585 core craft cards, 781 total headings)
   - Operational Guide: [HOW-PHASE-2-WORKS.md](./references/phase-02-screenplay-dialogue/HOW-PHASE-2-WORKS.md) | [INDEX.md](./references/phase-02-screenplay-dialogue/INDEX.md) | [LOOKUP.md](./references/phase-02-screenplay-dialogue/LOOKUP.md)
   - *Directs*: Screenplay formatting, dialogue rhythms, subtext layers, argument dynamics, linguistic registers, pauses, and character mannerisms.
3. **[Phase 3: Shooting Script](./references/phase-03-shooting-script/PHASE.md)** (768 core craft cards, 773 total headings)
   - Operational Guide: [HOW-PHASE-3-WORKS.md](./references/phase-03-shooting-script/HOW-PHASE-3-WORKS.md) | [INDEX.md](./references/phase-03-shooting-script/INDEX.md) | [LOOKUP.md](./references/phase-03-shooting-script/LOOKUP.md)
   - *Directs*: Two-column AV shooting script, shot numbers, coverage strategy, camera setups, cut transitions, and audio-visual bridge queues.
4. **[Phase 4: Audio Narration & Voice](./references/phase-04-audio-narration/PHASE.md)** (260 core craft cards, 268 total headings)
   - Operational Guide: [HOW-PHASE-4-WORKS.md](./references/phase-04-audio-narration/HOW-PHASE-4-WORKS.md) | [INDEX.md](./references/phase-04-audio-narration/INDEX.md) | [LOOKUP.md](./references/phase-04-audio-narration/LOOKUP.md)
   - *Directs*: Voiceover delivery styles, pacing, breathing pauses, emotional resonance, voice timbre casting, and TTS prompts (ElevenLabs, Cartesia).
5. **[Phase 5: Song & Music Generation](./references/phase-05-song-generation/PHASE.md)** (340 core craft cards, 349 total headings)
   - Operational Guide: [HOW-PHASE-5-WORKS.md](./references/phase-05-song-generation/HOW-PHASE-5-WORKS.md) | [INDEX.md](./references/phase-05-song-generation/INDEX.md) | [LOOKUP.md](./references/phase-05-song-generation/LOOKUP.md)
   - *Directs*: Song-engine prompt engineering for Suno v6 and Lyria 3.5, with the ready-to-paste syntax and each vendor fact on the `suno.` and `lyria.` cards themselves, sourced and dated. Structural metatags (`[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Bridge]`, `[Outro]`), global maqam systems, Near Eastern/Mesopotamian heritage modes, commercial sync supervision, and score direction for a film that already exists.
   - *Note on scoring*: a narrated documentary needs **score direction**, not a song, and the heritage route above does not list Phase 5. Open it anyway for the score — `HOW-PHASE-5-WORKS.md` has the short route for that, and it produces mood, instrumentation and where the music gets out of the narration's way, with no lyric.
6. **[Phase 6: Storyboard Layout](./references/phase-06-storyboard-layout/PHASE.md)** (194 core craft cards, 195 total headings)
   - Operational Guide: [HOW-PHASE-6-WORKS.md](./references/phase-06-storyboard-layout/HOW-PHASE-6-WORKS.md) | [INDEX.md](./references/phase-06-storyboard-layout/INDEX.md) | [LOOKUP.md](./references/phase-06-storyboard-layout/LOOKUP.md)
   - *Directs*: Multi-panel deck architecture, spatial composition, 180-degree rule blocking, character eyelines, shot sizes (EWS to ECU), Dutch angles, and animatic beat timing.
7. **[Phase 7: Image Prompt Engineering](./references/phase-07-image-prompt-engineering/PHASE.md)** (889 core craft cards, 896 total headings)
   - Operational Guide: [HOW-PHASE-7-WORKS.md](./references/phase-07-image-prompt-engineering/HOW-PHASE-7-WORKS.md) | [INDEX.md](./references/phase-07-image-prompt-engineering/INDEX.md) | [LOOKUP.md](./references/phase-07-image-prompt-engineering/LOOKUP.md)
   - Specialized Assets: [how-to-write-an-image-prompt.md](./references/phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md), Master Character/Location/Prop turnaround sheets, and the authoritative **Mesopotamia Canon** (`canon-rules.md`, `heritage-rules.md`, the router `CANON-LOOKUP.md`, the world in `grimoire-01` … `grimoire-20`, the wardrobe in `clothing-01` … `clothing-11`).
   - *Directs*: The 7-Slot Universal Prompt Order, physical sensor optics, Panavision/Cooke lenses, Kelvin lighting physics, film stocks, material textures, and frontier model syntax.
8. **[Phase 8: Video Prompt Engineering](./references/phase-08-video-prompt-engineering/PHASE.md)** (394 core craft cards, 414 total headings)
   - Operational Guide: [HOW-PHASE-8-WORKS.md](./references/phase-08-video-prompt-engineering/HOW-PHASE-8-WORKS.md) | [INDEX.md](./references/phase-08-video-prompt-engineering/INDEX.md) | [LOOKUP.md](./references/phase-08-video-prompt-engineering/LOOKUP.md)
   - Specialized Assets: [how-to-write-a-video-prompt.md](./references/phase-08-video-prompt-engineering/how-to-write-a-video-prompt.md).
   - *Directs*: Universal camera kinematics, 6-axis spatial coordinates, speed qualifiers, temporal continuity checks, and failure recovery.

---

## 3. The 8-Field Standardized Craft Card Schema

Every card across all 8 phases conforms to this exact schema:
```markdown
### Title

**Also called:** [Synonyms, cinema keywords]
**What it is:** [Precise mechanical definition]
**Effect on the audience:** [Psychological & emotional impact]
**Used for and where it works best:** [Narrative context, scene type]
**Best in:** [Formats: ... | Genres: ...]
**Avoid when:** [Misuse warnings, negative conditions]
**Prompt:** [Prompt syntax string for visual/audio/kinematic phases] OR **Example:** [Full script lines or illustrative dialogue for writing/narrative phases]
**Source:** [Required on any card stating a working value. One of three words, then where it came from]
**Outranks:** [Optional. Card ids this card beats, and in what case]
**Yields to:** [Optional. Card ids that beat this card, and in what case]
`prefix.unique_card_id`
```

The last two fields are optional and usually absent. They record a collision that has actually been
found and settled between two named cards, and each one always names the case in which it applies —
a bare id with no condition is not usable, because both cards are right somewhere. See
[PRECEDENCE.md](./references/PRECEDENCE.md) for how they are written and what decides them.

### The field that sorts is the one that forbids

**When you are choosing one card from many, the discriminating information is in `**Avoid when:**`,
not in `**Effect on the audience:**`.** This was measured rather than assumed. A fresh agent given a
brief and one 89-card file, with no selector and no idea what was being looked for, read the whole
file and reported:

> *"The **Avoid when** and **Colour temperature** lines were where nearly all the real information
> was. The **What it is** and **Effect on the audience** lines mostly restated what the title
> implied."*

It then named three decisions that the **Avoid when** line reversed — two cards that looked correct
from their titles and subjects, and which the file itself rules out for that scene.

**The reason is structural.** *Effect on the audience* says what a card does when it works, and on a
well-built shelf most cards in a family do something worth having — so the field describes them all
and separates none. *Avoid when* says where the card stops. **A field that praises cannot sort; a
field that forbids can**, because the scene in front of you either meets its condition or does not.

**What this changes in practice.** Build the questions from what a card *does*, because that is how a
person thinks about a scene. Then **sort the survivors on what the cards forbid**, and quote the
forbidding line rather than paraphrasing it — on the lighting shelf roughly a quarter of the cards
name a condition in that field which disqualifies them outright, and it is a quarter removable by
reading one line each.

### `**Source:**` — where a value came from

**A card that states a working value states where the value came from.** Not a number in a sentence —
a *working value*, the kind a reader copies into a plan or a prompt: a rate, a duration, a percentage,
a dimension, a threshold, a setting.

**Three permitted words and no others**, so the field can be checked rather than read:

```
**Source:** measured — my own 12 reels, September 2025
**Source:** reference — BBC subtitle guidelines, 2024 edition
**Source:** assumption — a reasonable default, untested
```

**When a correction lands, date it inside the card.** *"It read as calibrated and specifically
engineered until September 2026"* — one clause, in the field, naming what the card used to say. It
costs a line and it earns two things: a reader a year from now knows the field is load-bearing rather
than decorative and does not strip it as clutter, and anybody who finds the old wording quoted
somewhere else can see it was corrected rather than that two sources disagree. **Do it for a
correction of a rare kind** — a claim that was false, a figure that was the wrong shape, a rule that
contradicted a card — and not for ordinary edits, which would drown the signal. The same habit is
already in `vertical.safe_zones`, which records that it stated a platform figure backwards, and in
`light.kelvin_reference`, which records that law 8 demanded a number no card supplied.

**`assumption` is a perfectly good answer and it is the most common one.** The field does not exist to
force research; it exists so that a reader can tell a figure somebody checked from a figure somebody
chose. Both are usable. Only one of them is safe to build a series on. **The field is a label on the card, never a step in a run:** a run does not stop to source a figure, and a card's figure is a default the brief can override (§0).

**What this prevents.** The package already knows a value can go stale — 123 cards carry
`**Shelf life:**` — and until now it had no way to say a value was never sourced in the first place.
`pacing.wpm_vertical_heritage`, in
[`pacing-cadence-wpm.md`](./references/phase-04-audio-narration/pacing-cadence-wpm.md) which owns every speaking
rate, read *"a calibrated speaking rate… specifically engineered for vertical heritage"*. Nothing calibrated it and nothing engineered it; it was a sensible guess wearing the
vocabulary of a measurement, and a reader had no way to know. `vertical.safe_zones` shows the cost of
the same shape: it stated a platform figure backwards and four files copied it before anyone checked.

**The claim and the source may not contradict each other**, and `value-claims-unearned-provenance`
enforces exactly that: a card whose prose says *calibrated*, *engineered*, *measured*, *proven*,
*tested* or *verified* about its own figure, while its `**Source:**` reads `assumption`, is a finding.
A guess is allowed. A guess dressed as a measurement is not.

---

## 3a. When Two Cards Disagree

Cards are written to be obeyed, not weighed against each other, and almost every card you will use
stands on its own. When two cards you are actually holding cannot both be obeyed in the same shot —
not two techniques offering a choice, but two rules in genuine collision — open
**[PRECEDENCE.md](./references/PRECEDENCE.md)**, which states which rule outranks which and why. Do not open it
before then: it decides nothing about a card that has no opponent in front of it.
Where it does not settle the case, the working rule in §0 does: choose what serves the brief,
search the web when a fact decides it, record the choice, and continue.

---

**Looking for one card by its id?** [`references/CARD-INDEX.md`](./references/CARD-INDEX.md) lists every id in the
package and the file that holds it. It is generated from the cards, so it cannot fall behind
them. Search it; do not read it.

---

## 3b. Two things to fill before the first prompt

Both are project-level, both are filled once at the top of a job, and both are the kind of input a
phase asks for four stages later, when it is too late to go and get it.

| File | What it holds | If it is empty |
| :--- | :--- | :--- |
| [`references/ENGINE-CHECK.md`](./references/ENGINE-CHECK.md) | what the chosen engine can actually do today — native tiles by aspect, clip ceiling, whether an end frame is accepted, what a run costs and on which route | the agent picks the engine when the brief names none and fills the row from the engine's own pages today; only a value no search gives reads `pending_engine_check`, a note that travels with the handoff |
| [`references/FORBIDDEN-GLOBAL.md`](./references/FORBIDDEN-GLOBAL.md) | what must never appear anywhere in this piece, decided once for the whole project. It is Tier 0 of every negative block | Phase 1 fills it from the brief and the canon; a brief that forbids nothing gives `none, per the project brief`, recorded under `decisions` |

**Engine limits move every few months**, so nothing about them is written into the craft files and
nothing is taken from memory. And the rule that governs all of it: **a limit is a reason to change
the engine, not the shot.**

**A project that forbids nothing writes that down.** `none, per the project brief` is an answer; an
empty cell is not, and the whole reason that file exists is that a decided-nothing used to be
indistinguishable from an unsupplied-nothing.

Neither of them stops the work. Both make the gap visible instead of silent.

---

## 3c. How to read this installed skill

This `SKILL.md` is the skill's only entry point. Everything it routes to lives under
`references/`: the eight phase folders, each opened through its `PHASE.md` and its
`HOW-PHASE-*-WORKS.md`, and the root reference files beside them. The phase manifests are ordinary
reference documents here, not skills of their own.

Route the brief with section 1 first, then read only the phase the route names, its guide, and the
craft files its index points to. Look a technique up in
[`references/CARD-INDEX.md`](./references/CARD-INDEX.md) rather than reading every file into context.

Every index, lookup and card count in this copy was generated from the cards in the source package
and checked there before this copy was built; this copy is read, not edited. Backticks mean a thing
exists: a backticked card id or file name is a citation you can look up.

## 4. Master Agent Execution Instructions

When acting as the Master Director:
0. **Open the project record before Phase 1 writes anything.** Copy the `project.yaml` block from [`references/PROJECT-STATE.md`](./references/PROJECT-STATE.md) §1 into the project folder beside the brief, fill what the intake answered, and write every later decision there: every phase's contract reads its decisions from that file and from no other phase's document.
1. **Search before you invent.** Before writing a decision this package does not appear to cover, search [`references/CARD-INDEX.md`](./references/CARD-INDEX.md) for the *concept* — not the phrase you would use for it, but two or three words a card title might use. Only when that search comes back empty is it a gap. **A decision made from your own knowledge while a card for it exists is a defect, even when the result is good**, because the piece ships fine and nobody ever finds out that the package's own material went unused. This is the one failure mode here that leaves no trace: a missing card produces a visible hole, and a card nobody looked for produces a competent improvisation that quietly replaces it. A real run wrote its own cutting rhythm for an action sequence — and `cut.accelerate`, `cut.hold_then_fast`, `seq.action_sequence`, `beat.action_sequence_beats`, `move.chase`, `block.chase_geography` and `block.fight_geography` were all already there, reachable, with better numbers in them.
2. **Never Skip Phase Context**: Read that phase's HOW-PHASE file before executing it — every phase directory has one.
3. **Preserve Identity & Wardrobe**: When moving from Phase 6 to Phase 7, author the character sentence (quoted from then on as `project_scoped`, and locked by the keyframe approval — `frozen_sentence_status` in [`references/PROJECT-STATE.md`](./references/PROJECT-STATE.md)) via `references/phase-07-image-prompt-engineering/identity-consistency.md` (`ident.frozen_sentence`) and `references/phase-07-image-prompt-engineering/sheet-character.md`, maintaining it across all downstream image and video prompts.
4. **Keyframe Conditioning for Video**: In Phase 7/8, generate dual keyframes (Start Frame + End Frame) where the target engine supports first-and-last-frame interpolation, and a single high-fidelity start frame paired with a precise camera-move kinematic prompt where it does not. **Which engines support it, and at which resolution, is checked when the project starts rather than assumed** — the answer changes every few months, and a shot designed around a limit that has since lifted costs a regeneration, as does one designed around a limit that has since appeared. **With no engine chosen yet**, write the start frame for every shot and an end frame for each shot with one clear change of state, marked conditional on the engine.
5. **Route visible text; never infer its rendering method.** Whenever a frame involves visible text, lettering, a logo, an inscription, a glyph, a label, a book, a magazine, a tablet, a mural, a sign, a screen or packaging, open [`references/phase-07-image-prompt-engineering/in-frame-text.md`](./references/phase-07-image-prompt-engineering/in-frame-text.md), apply its three-axis selector (`textimg.read_or_seen`), and record the selected treatment before writing an image or video prompt or making a generation call. Phrases such as *on-screen text*, *brand name fully legible*, *end card* and *fold the logo and the line into the last live shot* specify content, timing or composition; they do not decide whether lettering is generated as physical geometry, preserved from approved artwork, composited, or set in the edit. A text-bearing keyframe cannot be marked **PASS** until that treatment is recorded. Do not replace this routing step with a blanket no-text rule: period inscriptions, carved tablets, murals, books, magazines, signs, screens and packaging keep the treatment selected for their actual role.
6. **Pure English Files — with one carve-out, and it is not optional.** All generated production documents, prompt scripts, shot lists, storyboards and markdown files are authored strictly in professional English: the metadata, the headings, the structural notes, the prompt strings, the file names. **The spoken and sung lines themselves are written in the language the piece is performed in** — Arabic, Sureth, Syriac, whatever the brief says — inside the Audio column of the script, the lyric sheet and the subtitle track. So is on-screen text that the audience is meant to read in that language. This is the rule that [`references/phase-02-screenplay-dialogue/HOW-PHASE-2-WORKS.md`](./references/phase-02-screenplay-dialogue/HOW-PHASE-2-WORKS.md) already states under *Language Governance*; it is repeated here because **this list outranks a phase, and read without the carve-out it forbids the dialogue the brief asked for.** Everything around the line is English; the line is the line.
7. **Run the closing check before you hand anything over**, whatever route you took and whatever the last phase was: [`references/phase-08-video-prompt-engineering/HOW-PHASE-8-WORKS.md` §6](./references/phase-08-video-prompt-engineering/HOW-PHASE-8-WORKS.md). It reads the original brief back against what was actually produced and asks what has no deliverable, what the delivery needs that nobody asked for, and which `pending_` markers are still open. It is the only check in the package that looks for something missing rather than something wrong, and every phase can be complete while the piece is not. **It is listed here, at the root, because a route that drops Phase 8 — anything with no moving picture — would otherwise never reach it.**
