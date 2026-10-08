# Phase 01: Story Generation & Narrative Engine — Specification & Instructions

Written directly from the core rules, intake protocols, and craft databases this skill was built from.
This document governs how Phase 1 initializes, asks questions, executes research, and builds narrative structures before handing off to the next phase its route names (Phase 2 on most routes, Phase 5 on `music_video`).

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Upfront Project Intake (Asked Once Before Execution)](#1-upfront-project-intake-asked-once-before-execution)
- [2. Automatic Research & Period Gate (Stage 1)](#2-automatic-research-period-gate-stage-1)
- [3. Story Engineering Engine (Phase 1 Execution)](#3-story-engineering-engine-phase-1-execution)
- [4. Architectural Bridges & Governance Laws](#4-architectural-bridges-governance-laws)
- [5. Phase 1 Deliverables (The Handoff to Phase 2)](#5-phase-1-deliverables-the-handoff-to-phase-2)

<!-- /GENERATED:toc -->

## 1. Upfront Project Intake (Asked Once Before Execution)

Before searching craft cards or drafting beats, the skill asks only the essential decisions. If the user provides this information in their opening prompt, extract it immediately without asking again.

### Question 1: Operating, Spending & Review Modes
1. **Prompts only (Default - Zero Spend):** Generates complete scripts, shot plans, prompts, and templates. Spends zero generation credits.
2. **Auto with images (Express Stills):** Generates prompts and executes static keyframes, character model sheets, and location plates.
3. **Auto with images and video (Express Full):** Generates prompts and executes both images and video clips end-to-end automatically.
4. **Auto, best choice from the story (Hybrid):** The engine determines which shots require motion versus still keyframes based on narrative intensity.
5. **Interactive Director Review (Phase-by-Phase Follow-Up):** The pipeline pauses at the completion of each major phase, presenting the milestone deliverables (Story -> Script -> Audio/Music -> Storyboard & Keyframes -> Video Prompts) for user inspection and approval before advancing.

> [!NOTE]
> **Spending Confirmation vs. The Keyframe Approval Gate**:
> - **In Express / Auto Modes (2, 3, 4):** To prevent annoying repetitive pauses during automated rendering, the engine states upfront:  
>   *"This project will generate [X] images and [Y] video clips."*  
>   The user confirms the allocation once upfront.
> - **The Keyframe Approval Gate (the Phase 8 gate):**  
>   *The director reviews and approves the still keyframe deck at the end of Phase 7 before any video is generated in Phase 8.*  
>   The approval is recorded, not assumed: the owner writes their name and the date in `keyframes_approved_by` in `project.yaml`, and Phase 8 does not start while that field is null (`../PROJECT-STATE.md`).  
>   This one holds in every mode, including the automated end-to-end run, because it is not a quality checkpoint — it is the point where money starts being spent and where a weak frame becomes an expensive one. Motion never repairs weak composition, and generating video from an unapproved still is the most expensive mistake available in this pipeline.  
>   It is the **only** gate that stops a stage from starting. Three things wait for a person, all named in root `SKILL.md` §0 and recorded in `../PROJECT-STATE.md` §1: `paid_generation_approved_by` stops every generator call and no writing; `keyframes_approved_by` stops Phase 8 itself, not only its spend; and a real person's consent is recorded before their voice or likeness is cloned (a real child: the parent's). Nothing else waits (see law 2 under *Architectural Bridges* below).  
>   **The Mode 5 pauses are not gates.** They are review pauses the owner opted into. When the owner is absent, a Mode 5 run falls back to the Q1 default, prompts only, rather than waiting.

> **When the brief does not answer a question, and cannot be asked.** A client brief typically
> answers the format, the destination, the runtime and the subject, and says nothing about the audio.
> Do not stop, and do not leave the field blank — **choose, write the choice into the brief as a
> declared assumption, and carry it forward.** The defaults that cost least to be wrong about:
> Q1 **prompts only**, Q3 **no voiceover — on-screen text plus foley**, because adding a voice later
> is cheap and removing one that the whole edit was built around is not. A declared assumption is
> visible and can be corrected in one line; an invented answer nobody flagged cannot.

### Question 2: Destination & Channel Profile
- **Heritage / historical channel:** Heritage and historical work — historical accuracy where the user wants the piece realistic (root `SKILL.md` §0: found, searched, or the closest thing; never a stop), the standing rules in `heritage-rules.md`, and narration in one language with separate subtitles in another.
  **The aspect and the cadence are not part of the destination.** A heritage channel publishes vertical reels *and* long horizontal documentaries, and the two do not share a rate: a feed reel, 9:16 or 16:9, runs at the vertical heritage cadence (`pacing.wpm_vertical_heritage`), while a 16:9 documentary takes the documentary rate from Phase 4 and is measured against the rendered narration, not calculated. Take the aspect from Question 1 and the cadence from the piece, never from this row. **A short feed piece takes the short-form cadence whatever its aspect** — a 16:9 reel posted to a feed is still a reel.
- **Children's content channel:** Children's animated songs and narrative shorts. Stylized animation, and whichever language the channel publishes in.
- **General / client work:** Social media reels, commercial ads, cinematic shorts, or YouTube documentaries.

### Question 3: Audio & Voice Format
- **Narration / Voiceover:** Single authoritative or poetic voice driving the visual pacing.
- **Spoken Dialogue:** Character-driven dramatic interaction.
- **Song / Music Video:** Lyrics in Suno-ready format with musical timing.
- **Silent / Ambient:** Visual-only storytelling with atmospheric sound effects.

**What each answer actually changes downstream** — this question decides more than which voice gets
cast, and for a while only the first three answers were read by anything:

| Answer | What it changes |
| :--- | :--- |
| Narration / Voiceover | Phase 4 runs before the picture phases and the **measured** narration sets the shot table. Take the rate from the owner card for the register. |
| Spoken Dialogue | Same as above for timing, plus Phase 2's dialogue craft leads. On any on-camera speaker, to the lens or inside a scene, the lip-sync engine's take length is a structural input — record it before the shot list. |
| Song / Music Video | Phase 5 runs **before** Phase 3 and its timing map governs. Where characters sing on camera, the lip-sync engine's take length is a structural input here too — record it at intake ([`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §2, the lip-sync fields). |
| **Silent / Ambient** | **There is no speech to render, so nothing downstream may cut the picture to measured audio.** The durations are **designed** in Phase 3 and everything else is built to them: Phase 4 runs *reduced* — foley, ambience and mix intent, no casting, no narration render — and its Step 8 handoff inverts, which that step now says. Phase 2 runs for structure and action, not for lines. The picture is the clock. |

**On a silent piece the sound is not less written, it is written differently.** A wordless film puts
the whole channel on foley, ambience and score, so those are specified shot by shot rather than left
to the mix — the same discipline Pipeline C in Phase 2 applies to an audio-only piece, pointing the
other way.

**The craft for a wordless piece is in Phase 2, and nothing routes you there.** A brief with no
dialogue reads "Phase 2 is the dialogue phase" and skips it, which loses the four cards that do most
of the work on exactly this kind of film. Open them: **`scene.wordless_channel_discipline`** — the
central one, on deciding what each channel carries when none of them is words — with
`scene.silent_scene`, `emo.emotion_through_task` for feeling carried on an action rather than a
face, and `emo.someone_else_feels_it`. All four are in
[`../phase-02-screenplay-dialogue/cat-scene-2.md`](../phase-02-screenplay-dialogue/cat-scene-2.md)
and its neighbours. **A route decides which deliverables get made, never which craft you may read**
— and a wordless film needs the scene craft more than a talkative one does, not less.

### Question 4: Aspect Ratio & Target Platform

**Ask it once per deliverable, not once per project.** A campaign is normally several shapes of one
idea — a wide film, a vertical cutdown, a square still, a printed poster — and answering this
question with a single value throws away the fact that there are four. Where the brief names more
than one output, list them all and fill the deliverables table in the Story Foundation Brief below;
each row carries its own ratio, its own duration or size, and its own surface.

- **9:16 Vertical:** Instagram Reels, TikTok, YouTube Shorts. Phone-first, muted autoplay standard.
- **16:9 Horizontal:** YouTube, Film Festivals, Desktop/TV documentary.
- **Facebook and YouTube carry both.** A feed video on either can be vertical or horizontal; take the
  aspect the brief names, and never assume a reel is 9:16 when the brief says otherwise.
- **1:1 Square:** feed post, album or podcast cover, profile art.
- **4:5 Portrait:** feed-optimised social, and the standard for a storyboard deck page.
- **Other — state it:** a fixed wall panel, a projection surface, a screen someone measured. Write the
  actual ratio and the physical size if there is one.
- **None — the piece has no picture:** an audio episode, a podcast, an audio drama, a score, a
  listening post. Answer *none* and this question is closed. **Any still deliverable the piece does
  have — cover art, key art, a thumbnail — takes its own ratio in the still-image design record at
  Phase 7**, named separately, because a cover is not the piece's aspect ratio.

This list ends in *other* and *none* on purpose. A closed list of platform names is a taxonomy, and
this package's own routing section argues at length that a taxonomy always has a hole in it — the
next brief is a kind nobody listed. The six routing questions were given that escape hatch; for a
while this question was not, and a two-option list at the first question of the first phase is the
earliest possible place to lose a brief.

### Question 5: Starting Material & Input Mode
- **Draft / Story provided by User -> POLISH MODE:**
  *Rule:* "A story from the owner is polished, never replaced. Characters, events, ending, and order are his. Polish works on execution: dialogue, rhythm, clarity, and force."  
  *One Exception:* If polishing finds a critical flaw in a core decision (e.g. unworkable ending), it reports it once, in a single line in the Warning List, and keeps polishing the owner's version. It never pauses for it and never raises it again.
- **Premise / Idea from scratch -> GENERATION MODE:**
  Full creative build using the 1,332 core craft cards (1,672 total headings).

### Question 6: Language, Runtime, Genre — and the Age Band on Children's Work
The project record's `brief` block (`../PROJECT-STATE.md` §1) needs three facts the questions above do not ask for, and a children's piece needs a fourth. Extract them from the brief where it gives them; otherwise choose and declare the choice as an assumption, as the note under Question 1 describes. They are the user's call, written as asked.
- **Language** (`language`, `subtitle_language`, `dialect`): the language the piece is performed in, any subtitle language beside it, and the dialect, where the language has one that changes rate or casting.
- **Runtime** (`duration_s`): the target duration in seconds, one per deliverable where Question 4 lists more than one.
- **Genre** (`genre`): the Phase 1 format or genre kit the piece is built on. **A piece that needs two
  kits records both**, joined with + — a feed reel on a heritage subject takes the Reels kit and the
  Heritage and Historical Documentary kit: the delivery kit governs form, the subject kit governs
  content. **A kit's lengths, ratios and counts are its defaults**; the brief's own length, aspect and
  size govern, so a 16:9 feed reel takes the Reels kit at 16:9. **A commercial has no
  Phase 1 kit of its own:** it takes the nearest delivery kit (for a feed advert, Instagram Reel, Branded
  Serial or Creator Brand Partnership (Organic) in [`formats-social.md`](formats-social.md)) plus Phase 3's
  `vlb.format.commercial_ad`, and records both.
- **Age band** (`age_band`), **on children's work only:** asked before the premise, because [`formats-kids.md`](formats-kids.md) makes it the first decision. Where the brief's band straddles two bands on a card (a 3–6 piece against a tempo card split at 2–4 and 5–7), take the band that serves the youngest viewer and record the choice.

`format` is Question 4's answer, `audio_profile` is Question 3's and `mode` is Question 1's. **`rate_wpm` is not asked**: it is taken from the owner card in [`../phase-04-audio-narration/pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md) for the register Questions 2 and 3 chose, and recorded with that card as its source. **Where no card holds a band for this language and register** — a told Arabic story, a regional dialect — take the nearest card's figure, record the choice under `decisions`, and let the measured audio replace it; nothing waits for a recording. On a song-led piece that card hands the timing to the melody (`pacing.wpm_children` says so for a children's song): the value stays null, the register reads melody_governs, and the card is still the source. `engine_record` is the path of the engine block opened from [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) for this project; where the brief names no engine, the agent chooses one and fills it (that file's §3).

---

## 2. Automatic Research & Period Gate (Stage 1)

**Research is a tool, not a gate.** It opens when the piece shows or says something real that the
brief wants right — a real place, a real company, a real event, a history piece the user wants
realistic. It follows the working rule in the root `SKILL.md` §0: take the fact from the brief, then
the skill, then a web search; take the most reliable answer found; if nothing turns up, choose the
most plausible and carry on. Record what was used under `decisions`. **Nothing here stops the work,
and a fiction or a stylised piece skips it.**

What is usually worth a quick search on a real subject: what the thing actually is, what it looks
like now (photographs, not memory), and whether the specific year or event the piece names happened.
What only the client holds — their name, phone number, logo, claims about their business — comes from
the brief; where it is missing, write a clearly marked placeholder (`[PHONE]`, `[LOGO]`) and carry on.

### 1. The Mesopotamia Period Gate (Pre-330 BC)
If the project is set in ancient Mesopotamia (Sumer, Akkad, Babylon, Assyria):
- Open `../phase-07-image-prompt-engineering/mesopotamia-canon/canon-rules.md` first — it decides whether the canon opens at all — then `../phase-07-image-prompt-engineering/mesopotamia-canon/INDEX.md`, which lists every chapter and wardrobe file with its period and dates and so turns a date or a period name into the one or two canon files that answer it (`CANON-LOOKUP.md` beside it is the id table, for a card you already have a name for). The canon is no longer two monolithic files and is not read whole.
- **Scope Division — what the canon settles.** The canon is a **visual world**, and that is the class of question it answers: what a place looked like, what grew and lived there, what the buildings and streets were made of, how people looked and what they wore down to the construction of the garment, what they ate, traded, rode and carried, which gods were depicted and with what symbols, and what an army looked like on the field. On those, quote it rather than research them again.
- **What the canon does not hold** — king and commander names, regnal dates, the order of events — comes from a quick web search; take the most reliable answer and record it.
- Search technique: Specific keywords beat generic (e.g. `Ashurbanipal lion hunt relief Room 10a` instead of `Assyrian art`).

### 2. The Modern Assyrian Heritage Rules
If the project addresses modern Assyrian heritage:
- Open `../phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md`.
- **Heritage constraints:** Do not restate them here. Open `../phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md` and apply **Part A** as that file scopes it under *Which of these apply* and **Part B only when the subject is Mesopotamian or Assyrian heritage as heritage**. A Syriac Christian subject — a kids song, a saint, a monastery, a theological school — is governed by Part A rule 4, not by the Part B heritage-frame rule. That file is the only copy; this line must never restate its contents.

### 3. Foundation Correction Rule
If research contradicts the premise on a piece the user wants accurate, choose the fix that keeps the
brief's intent — correct the detail, or swap in the nearest real equivalent — record it under
`decisions`, and carry on. Do not stop the story to ask.

---

## 3. Story Engineering Engine (Phase 1 Execution)

### A. Hook Engineering (First 3 Seconds — interrupted arrivals only)

> The three-second hook is **not a general principle of Phase 1.** It is a rule about one delivery
> situation: a viewer who did not ask for this piece and can leave at no cost. On a piece the viewer
> chose, it is the wrong rule and applying it damages the opening. The two arrivals are defined
> immediately below, and nothing else in Phase 1 restates this — if you meet "hook at 0:00" as a bare
> principle anywhere, read it against this scope.

**This section is about feed work** — reels, Shorts, TikTok, anything a viewer scrolled into rather than chose.

**The test is how the viewer arrived, not whether money was spent.** Sort the piece into one of two arrivals before deciding anything about its opening:

- **Interrupted** — a feed scroll, a pre-roll or mid-roll, a paid social advert, an autoplaying next item. The viewer did not ask for this and can leave at no cost, so **the three-second rule applies and applies hardest here.** A paid social ad is the clearest case in the whole category: it is bought placement in somebody else's feed, it interrupts, and it needs the hook *more* than an organic reel does, because the organic reel at least reached someone the algorithm thought wanted it. Do not let the word "commissioned" or a client's involvement move an interrupted piece out of this bucket — a thirty-second advert that opens on a logo and a mission statement has spent its only three seconds proving it is an advert.
- **Chosen** — a search result, a subscription, a link someone sent, a title clicked from a shelf, a documentary put on deliberately, an episode of a series already being watched. The viewer has already decided to be here and a scroll-stopper reads as distrust of them. The three-second rule does not apply, and forcing it produces a piece that opens like an advert for itself. There the opening move is the **first thirty seconds that earn the next five minutes**: a question worth the runtime, or an image that will be paid off at the end.

A piece can have both arrivals — the same cut runs as a paid pre-roll and sits on a channel page — in which case build the interrupted opening, because it survives being chosen and the chosen opening does not survive being interrupted.

Take from the cards below only what is craft rather than platform behaviour.

Governed by [`short-form-craft.md`](short-form-craft.md) — the `sf.*` cards. **If the piece branches — the viewer chooses and the piece changes — open [`interactive-and-branching.md`](interactive-and-branching.md), whether or not it is short-form or on a feed.** Every `inter.*` card is there. Sixteen of them used to sit in a file named for reels and were reachable only through this short-form paragraph, so a branching piece that was not social never found them. (`reels-engagement-and-dilemmas.md` is **not** a hook file despite its name; it holds interactive and choice-based fiction. See its header.)
1. **The First Line Works Twice (`sf.first_line_both_ways`):** The hook's promise must land both as spoken audio and in the muted frame; any separate hook text adds to the line and takes its own seconds, never the same words at the same time.
2. **Front-Load the Payoff (`sf.front_load`):** Never save the premise for the end. Deliver the startling hook immediately.
3. **One Point, Not Three (`sf.one_point`):** A short-form piece carries exactly one central idea.
4. **Every Word Earns Its Place (`sf.every_word_earns`):** Cut every word that does not carry narrative weight.

### B. Story Architecture & Beat Skeletons
- **For Reels & Shorts (45s - 60s)** — this is `sf.four_beat_reel` in
  [`short-form-craft.md`](short-form-craft.md), which owns the grid and scopes it to a 45–60 second
  piece. The timings are reproduced here for reading convenience only; when the two differ, the card
  is right. The grid does not stretch and it does not shrink — a beat given fifteen seconds instead
  of three is a different film, which is why the lengths either side of this band get their own
  shapes below.
  - `0:00 - 0:03`: The Ignition Hook (Sensory shock, paradox, or dilemma).
  - `0:04 - 0:25`: Narrative Escalation & Development (Context & rising stakes).
  - `0:26 - 0:40`: The Climax / Twist / Dilemma Peak.
  - `0:41 - End`: The Button / Engagement Loop (Lingering question or comment trigger).
- **For a 30-second piece — three beats, not four.** Thirty seconds is the common length of a paid
  social advert and of a cutdown, and the four-beat grid has no room to land in it: compressing
  complication and spike into the same eight seconds gives a reel that escalates and peaks in one
  breath and reads as a jump cut. At this length the four beats collapse into **three — hook, turn,
  close**: the hook takes `0:00 - 0:03` and is unchanged, because the reason for it is the feed and
  not the runtime; the turn runs `0:04 - 0:22` and carries the complication and the spike as one
  continuous rise with a single reversal at its top; the close takes `0:23 - End`. There is one
  value turn, as there is at sixty seconds, but it arrives earlier and is not preceded by a separate
  development passage. For an advert this is usually where the product or the claim lands.
  Below about twenty seconds, stop treating this as a beat grid at all — a fifteen-second cutdown is
  one image and one line, and `time.shortform_compression` is the card for it rather than a skeleton.
- **For Documentaries & Narrative Films:**
  - Consult [`structures.md`](./structures.md), [`cat-beat.md`](./cat-beat.md) and [`cat-beat-2.md`](./cat-beat-2.md) for multi-act pacing.
  - Pacing standards: the rate is not written here. `pacing.wpm_documentary` owns the documentary figure and `pacing.wpm_vertical_heritage` the vertical heritage one, both in [`../phase-04-audio-narration/pacing-cadence-wpm.md`](../phase-04-audio-narration/pacing-cadence-wpm.md). Open the card. Every rate there is a planning estimate, and the duration comes from the rendered file, measured.

### C. Character, Conflict & Stakes
- Flaws, contradictions, and distinct motivations via `cat-char*.md`.
- Antagonistic forces and pressure via `cat-anta*.md` and `cat-tens*.md`.

---

## 4. Architectural Bridges & Governance Laws

1. **A Bridge, Not Mutual Coupling:**  
   Phase 1 finishes its work completely and passes a clear, self-contained Story Brief to the next phase its route names (Phase 2 on most routes, Phase 5 on `music_video`). It does not depend on downstream phases.
2. **No Stage Stops the Work — with one exception.**  
   Each phase completes without arbitrary blocking gates. Advisory notes and non-blocking issues are placed in a single `Warning List` at the end; a missing input is recorded and carried forward rather than halting the pipeline, and an unfilled engine record produces a `pending_engine_check` cell rather than a stop.  
   **The one stage that waits is Phase 8, for the keyframe approval**, described under the operating modes above; the spend approval and a real person's consent before a clone wait only at their own step (root `SKILL.md` §0). The difference is what a stop protects: a gate that waits for a *judgement* costs momentum and buys nothing, while a gate that waits for *spend approval* is the only thing standing between a bad frame and a bill.
3. **Sources Never Enter Prompts:**  
   Historical sources and archive links stay in the research record; they are never pasted into image or video prompts.

---

## 5. Phase 1 Deliverables (The Handoff to Phase 2)

Phase 1 concludes by outputting the **Story Foundation Brief**:
```markdown
# Phase 1: Story Foundation Brief

- **Project Title:** [Working Title]
- **Destination:** [Heritage / historical channel | Children's content channel | General / client work]
- **Operating Mode:** [Prompts Only / Auto Images / Auto Images & Video / Hybrid / Director Review]
- **Deliverables.** One row per thing that gets handed over. **Most projects have one row and fill
  it in a line; a campaign has four, and this table is the only place that fact is written down.**

  | # | Deliverable | Ratio | Duration or size | Surface it lives on |
  | :--- | :--- | :--- | :--- | :--- |
  | 1 | *(e.g. website film)* | 16:9 | 30 s | museum site, sound on |
  | 2 | *(e.g. social cutdown)* | 9:16 | 15 s | feed, muted autoplay |
  | 3 | *(e.g. feed still)* | 1:1 | — | feed |
  | 4 | *(e.g. street poster)* | A1, 594 × 841 mm | — | printed, read at 2–4 m |

  - **Ratio** takes any of 9:16 / 16:9 / 1:1 / 4:5 / a stated physical size / **none — audio-only**.
  - **Surface** is what decides the safe areas, and they are different problems: a platform
    interface (`vertical.safe_zones`), **a broadcast transmission (`comp.safe_areas`, which owns the
    action-safe and title-safe figures)**, a wall or panel (`print.fixed_panel_safe_zones`), or
    **a horizontal video for the web or a feed** — a YouTube upload, a Facebook feed video, a 16:9 reel —
    which takes the web case of `comp.safe_areas` (type off the outer 5%, off the player's control band
    and the end-screen area) and keeps captions clear of the feed's lower overlay; or neither — a square
    feed still or a festival screen has no reserved band at all, which is a real answer and worth writing. **A broadcast piece is not the "neither" case.** Television has reserved margins that
    no platform interface causes and that look perfectly normal on every monitor in the building
    until the broadcaster's QC rejects the delivery; this list omitted them until September 2026,
    which routed a whole television series to "no reserved band at all".

  - **If a row's ratio is *none*, the piece has no picture** — see routing question 1 — and any still
    it still owes (cover, key art, thumbnail) is its own row here with its own ratio.
  - **Every row is generated natively at its own ratio.** Nothing is cropped out of a master; the
    craft for this is `kf.native_ratio`, `ai.aspect_native` and `control.aspect_reframe`, and they
    all agree. A shorter version of a longer film is a **subset of its shots, not a new shot list
    and not the same shots sped up** — `promo.cutdown_15s`.
  - **Carry this table forward whole.** Phases 3, 6, 7 and 8 each need to know how many deliverables
    there are, because the safe areas, the type sizes and the negative block all differ per row. A
    project that records one ratio hands every later phase a piece of information that is wrong for
    three of its four outputs, and nothing downstream can recover what was never written.

- **Is this one piece or several?** If several — a series, a set of episodes, a campaign released over
  weeks — say so here and write **one shared record** that every episode is generated against, because
  the episodes are made in separate runs and nothing else carries continuity between them. The
  mechanisms all exist and nothing collects them, which is the gap: put in one place the **frozen
  character sentence** (`ident.frozen_sentence`), the **object and prop locks**
  (`ident.object_card`) for anything that recurs or is called back to, the **palette and lighting
  lock**, the **voice** — casting, engine, settings, and the seed if the engine has one
  (`elevenlabs.seed_locking`) — the **register and language decisions**, and the **engine record**
  itself, since an episode generated three weeks later on a different model will not match.
  - **Quote that record verbatim into every episode's prompts**, exactly as the frozen sentence is
    quoted into Slot 1. Do not re-derive it per episode; re-deriving is how episode three stops
    looking like episode one.
  - **A callback needs its own line.** Where a later episode refers to a prop from an earlier one,
    the prop's lock is what makes it the same object, and matching the *framing* of its first
    appearance is what makes the audience recognise it. Write both down when you write the arc.
  - Serial **story** craft is well covered in Phase 1 — arcs across episodes, what returns, what
    escalates. This record is the serial **production** half, which is the part that goes wrong
    silently.
- **Audio Profile:** [Narration / Dialogue / Song / Silent]
- **Render Mode:** [photoreal / 3D or rendered CG — name the surface too / flat 2D or cel — name the art style / **stop-motion or another physically-made look** — name what it is made of and that it is moved frame by frame / **built** — graphics, charts and maps made from data rather than generated / **other — state it** / **two or more looks** — name each and say what the cut between them means]
  - **This list ends in *other* for the same reason the aspect question does.** A named list of render modes is a taxonomy, and the next brief is a kind nobody listed — a stop-motion puppet, a pinscreen, a scanned physical model, a hybrid. State it in words and the phases downstream fork on what you wrote rather than on which box you ticked. The project record still stores one of the six machine values in the RENDER MODE SET ([`../ENGINE-CHECK.md`](../ENGINE-CHECK.md)): the nearest one, with the words beside it — a drawn character composited into a photographed shot is `multi_look` with both values under `looks` — and the choice goes under `decisions`.
  - **This is where the look is written down, and until it is written here it is nowhere.** The brief
    usually declares it in its first sentence, and every later phase forks on it: the optical values in
    Phase 7, the surface slot, the motion law in Phase 8, and which branch of the negative tiers
    applies. A piece that never records it makes each phase infer it again from the prose.
- **Core Premise (Logline):** [1-2 sentences capturing hook, protagonist, and stakes]
- **Arrival:** [Interrupted (feed, pre-roll, paid social) / Chosen (search, subscription, a link someone sent)]
- **The Hook (First 3 Seconds — interrupted arrivals only):** [Dual-hook line for audio and text. On a chosen arrival write the opening move instead: the first thirty seconds that earn the next five minutes.]
- **Characters & Forces:** [Protagonist want/flaw, opposing force, core dilemma]
- **Appearance (optional, one line per recurring character):** [Build, apparent age, hair, one distinguishing thing, what they wear. Not a prompt sentence — see the note under this template.]
- **Step Outline (Beat Sheet):** *— the four beats below are the short-form shape, sized for a
  piece of 45 to 60 seconds. At 30 seconds they compress to three — hook, turn, close — per §3.B.
  For anything longer, keep the fields and replace the grid; see the note under this template.*
  - Beat 1 (0:00 - 0:03): [Ignition Hook]
  - Beat 2 (0:04 - 0:25): [Escalation & Tension]
  - Beat 3 (0:26 - 0:40): [Climax / Conflict Peak]
  - Beat 4 (0:41 - End): [Resolution / Button / Loop]
- **Engagement & Audience Retention Strategy:** [Why they stay, why they comment]
- **Warning List:** [Non-blocking research notes or craft recommendations]
```

**Sizing the beat sheet to the piece.** The grid above is a 45-to-60-second shape and it does not
stretch. Below that band it does not simply squeeze either: a thirty-second advert or cutdown takes
the three-beat shape in §3.B — hook, turn, close — because four beats in thirty seconds puts the
escalation and the peak in the same breath. **Between 60 and about 90 seconds the four beats still hold and only the middle grows** - ignition and button stay where they are, and the extra time goes into the complication as one more turn rather than as slower versions of the same beats. `sf.four_beat_reel` carries that band. Above about 90 seconds the piece needs movements rather than beats: a five-minute explainer, a twenty-minute documentary or
a thirty-minute episode needs a beat sheet built for its own length — for long-form nonfiction, something like eight to twelve
movements across the runtime, each one a question opened and closed, with the timings written as
ranges rather than as a locked grid because **the narration has not been measured yet** and the
audio is what will finally set them.

Two fields above also read as short-form and are not: the **Hook (First 3 Seconds)** is an
*interrupted-arrival* rule, not a rule about every piece, and §3.A above is where the two arrivals
are defined. On a **chosen** arrival — a documentary, a search result, a subscription, a link
someone sent, an episode of something already being watched — it becomes *the opening move*, the
first thirty seconds that earn the next five minutes, and the three-second dual-hook rule does not
apply. On an **interrupted** arrival it does apply, and **a paid social advert is interrupted**: a
client-approved opening does not exempt it, because the viewer still did not ask for it. Where a
client has locked an opening that cannot carry a hook, record it in the Warning List rather than
quietly filing the piece as chosen. **Characters & Forces** is written for drama; on
nonfiction the opposing force is often a system, a climate, an institution or the passage of time,
and `anta.documentary_opposition` and `anta.absent` are the cards for it rather than a protagonist
dossier.

**The Appearance line, and what it is not.** Fill it in only where a character recurs — across
shots, across episodes, across a series. On a piece with no recurring character, or where the
subject is a place, an object or an institution, leave it out; it is optional and an empty field is
better than an invented one.

The reason it exists: Phase 1 is where a character is built, and until now no phase before Phase 7
had anywhere to put what that character looks like. So the design was either invented early and
never written down, in which case it arrives at Phase 7 as a fresh invention, or invented late, in
which case it contradicts something the screenplay already said — a scar the dialogue refers to, a
coat somebody takes off, an age a line depends on. Both failures are cheap to prevent here and
expensive to repair once keyframes exist.

Keep it to one line and keep it *narrative*: build, apparent age, hair, one distinguishing thing,
and what they wear. Five facts, written as a person would describe someone, because the point is to
carry a decision forward rather than to render an image.

**It is explicitly not a frozen prompt sentence.** The 30-to-45-word verbatim sentence that locks a
face for an image model is `ident.frozen_sentence`, it belongs to Phase 7, and it is produced at the
Phase 6 → Phase 7 boundary — see
[`../phase-07-image-prompt-engineering/identity-consistency.md`](../phase-07-image-prompt-engineering/identity-consistency.md).
Do not write one here. Phase 7 builds it from this line plus the shot, the lighting and the
reference material it has and Phase 1 does not, and a sentence frozen too early gets quoted verbatim
into every prompt downstream with whatever was wrong in it. What this line owes Phase 7 is the
*decisions* — that she is in her fifties, that the hands are burned, that he never takes the coat
off — not the wording.

One carry-over from the heritage rules, for a history piece the user wants realistic: on a real
historical person whose likeness is unknown, the Appearance line records what the record supports,
and the rest is the closest period type, noted as a choice. On any other piece the face is a design
decision like any other.

`short-form-craft.md` is consulted **on short-form work**.
On long form, take only what transfers — a card like `sf.deadpan_gravity` is craft, while anything
about feed behaviour, scroll-stopping or the three-second rule is a rule about a platform this piece
is not on.
