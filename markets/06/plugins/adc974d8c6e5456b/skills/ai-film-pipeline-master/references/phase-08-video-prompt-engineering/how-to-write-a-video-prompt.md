# How a video prompt is written

Every rule here is craft: what a generative model does with a prompt, and what it does with a careless one. Nothing in it routes to another module, so it can be read on its own.

The last place a good plan can still be destroyed. Everything upstream can be
right and a careless video prompt will still return a shot with a drifting face,
a hovering object, or a cut the plan never asked for.

The craft rules and model conditioning methods live in
[video-conditioning-modalities.md](./video-conditioning-modalities.md), which is the
authority. This file owns what the pipeline needs: how a shot row becomes a
prompt, what must be carried verbatim, and the failure modes that come from the
generation itself.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Purpose](#1-purpose)
- [2. When It Opens, When It Is Skipped](#2-when-it-opens-when-it-is-skipped)
- [3. Inputs](#3-inputs)
- [4. Method](#4-method)
- [5. Decision Rules](#5-decision-rules)
- [6. Research Protocol](#6-research-protocol)
- [7. Output Contract](#7-output-contract)
- [8. Quality Bar And Failure Modes](#8-quality-bar-and-failure-modes)
- [9. Worked Example](#9-worked-example)
- [10. Fast Path](#10-fast-path)

<!-- /GENERATED:toc -->

## 1. Purpose

Turn each shot in the shot list into a prompt that produces that shot, with the
locks intact, the motion described rather than the scene, and the clip landing
inside the model's real limits.

---

## 2. When It Opens, When It Is Skipped

> **The conditions below describe when this guide is needed. Nothing outside this file overrides
> them, and a project that thinks it needs an exception records the reason rather than assuming
> one.**

Opens on every route that produces motion, after the shot plan and normally after the stills,
because a generated start frame is usually the strongest way to hold continuity.

**Skipped entirely on a stills-only delivery** — a poster, key art, a set of reference sheets, a
carousel, a storyboard deck that nobody will animate. If the project delivers no moving picture,
this phase has nothing to do. Anything that ends in a video file, however short, runs it.

For an **audio-driven** piece it runs against the song map timecodes, using clip durations
established in Phase 3 / Phase 6 so cuts land on the beat rather than where the model is comfortable.

It must not run before the engine-selection step, because the prompt shape depends on which model is
being used and what that model actually supports today.

---

## 3. Inputs

| What the prompt needs | Where it comes from | When it is missing |
|---|---|---|
| The approved still, or the pair of stills | The image stage | On a references-to-video branch there is no keyframe, and this prompt decides the frame itself |
| The movement the shot is for | The shot plan, or the storyboard | A clip with no stated movement returns a photograph that breathes |
| Duration, and what the clip has to deliver by its last frame | The shot plan | Take the length the shot's content needs, record it under `decisions`, and carry on; a clip generated to no length is generated twice |
| Continuity locks, and the character sentence if a person appears | The continuity record and the character record | Not left waiting: a `project_scoped` sentence is quoted and marked pending approval, as the image guide's §3 says; a look the brief leaves open is decided by the agent the same way. Wardrobe is not carried here: it is written in image and character-sheet prompts and reaches the clip through the keyframe |
| The model, its syntax, its clip length and its native resolution | The dated record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) | The prompt is written in full either way; without the record those cells read `pending_engine_check` and travel with the handoff |
| The project's standing prohibitions, `forbidden_global` — the first of the three sources of the negative list | The list at the root of the project brief, defined in [`FORBIDDEN-GLOBAL.md`](../FORBIDDEN-GLOBAL.md) | The prompt is written in full either way; the first source reads `pending_forbidden_global` and travels with the handoff. A project that genuinely forbids nothing says so, and it reads `none, per the project brief` instead — the slot is never left blank and unmarked |

The continuity record and the character record are the same `project.yaml` entries the image
guide names in its §3: the `locks` block with the Phase 6 handoff list, and `frozen_sentence` with
`frozen_sentence_status`.

The still this clip starts from must be approved before the clip is generated. Generating video
from an unapproved frame is the most expensive mistake available in this pipeline.

## 4. Method

### 4.0a The jobs, in order

| # | The job | You are doing this when | Sections | It produces |
|---|---|---|---|---|
| J1 | Verify foundational laws and compute prompt element budgets | Enforcing core video generation laws, computing token budgets, and handling missing inputs | 4.0, 4.1b, 4.1c | prompt |
| J2 | Structure motion descriptions, camera vectors, and object paths | Directing kinematic actions, camera moves - single or developing, per law 1 - with speed qualifiers and physical trajectories | 4.1, 4.2, 4.4 | camera_move |
| J3 | Embed verbatim character and location locks | Injecting immutable physical continuity locks without paraphrasing | 4.3 | locks_quoted |
| J4 | Bind conditioning assets and calculate clip join transitions | Grouping reference sheets, start frames, and configuring multi-clip anchor joins | 4.5, 4.6 | join |
| J5 | Configure text geometry, audio flags, and negative exclusion tokens | Managing in-frame text, native audio expectation, and model-specific negative exclusions | 4.7, 4.8, 4.9 | negative_prompt |

### 4.0 The nine laws of this module

Laws marked **** restate a rule that already governs the whole package — one of the owner's standing rules in [`heritage-rules.md`](../phase-07-image-prompt-engineering/mesopotamia-canon/heritage-rules.md) Part A, or an order set in [`PRECEDENCE.md`](../PRECEDENCE.md) — repeated here so it is visible where it bites. The unmarked laws are the ones only this module can break, and they are what this module's depth is measured by.

Each one is falsifiable, and each one names a failure that has cost real money in
generated production.

1. **One camera intention per clip is a craft default, not a model limit.** A shot that says one
   thing says it clearly, and naming a move with a speed - "slow push in" rather than "push in" -
   gets a better clip because the qualifier carries the intent. **It is not enforced on the
   grounds that a model cannot manage two moves.** Current models handle compound
   and changing camera work. Where a shot genuinely wants a move that develops - a push that
   becomes an orbit, a crane that settles into a track, a whip that lands on a hold - **write it,
   describe the trajectory as one continuous path with one start and one end state, and declare
   it.** What is still worth avoiding is the accidental stack: a push plus an unrelated tilt, an
   orbit plus a pedestal, two intentions sharing one clip because neither was worth its own shot.
   That is a directing problem and the shooting script owns it; a developing move chosen on purpose is a different
   thing and it passes.
   **This law is scoped to a clip of roughly six seconds or less, where one clip and one shot are
   the same object.** Above that the clip is a container for a sequence, not a single gesture, and
   **section 4.2b governs**: either real cuts inside one generation where the engine supports them,
   or a long take whose move develops through named phases. A twenty-second uniform push-in is not
   this law being obeyed; it is an unfilled container.
   **A named single technique is always one intention.** The dolly zoom is one move, documented in
   [`camera-moves.md`](./camera-moves.md): name it as itself - "dolly zoom in",
   "dolly zoom out", "Vertigo effect" - never as "dolly in while zooming out". Models trained on
   film vocabulary recognise the named technique and fail on the assembled description. The same
   holds for any single named move whose mechanics involve two axes: a crane or drone following
   one continuous curved path is one trajectory with one start and one end state, not two moves.
   The model conditioning guides record which models document which named techniques; an unverified one is
   still written as the named technique and handed to the engine-selection step as a nomination, **never rewritten into a
   smaller move.** If no available engine documents it, that is an engine-selection problem to solve, not the
   shot's.
2. **A lock is quoted whole or the prompt is invalid.** The identity lock is the face-and-build
   sentence; wardrobe is not a video lock, it arrives with the keyframe. This holds on a clip animated
   from an approved keyframe too: `ai.image_to_video` narrows what is re-described, not the lock.
   **A clip that shows only part of a character** (hands only, from behind) **quotes only the parts
   that are visible** — the clauses the frame shows, verbatim; the wardrobe on them arrives with the
   keyframe — **never the face clauses**, writes `face out of frame`, and quotes the whole sentence
   again the moment the face can be seen (4.3).
   Never paraphrased, never
   shortened to make room, and **there is no "room" to make**: per 4.1b there is no element cap
   and no word cap, so a long prompt is simply a long prompt. **Nothing is ever removed from the
   shot to shorten it**. Put the lock first so that a weaker engine dropping late
   instructions still holds the identity.
3. **The model has no memory between clips.** "The same character as before" is
   not merely useless, it sometimes introduces a second person into the frame.
4. **Anything that moves has a path.** A start, an end, and what it rests on.
   Without all three, generated objects hover, slide, or pass through solids.
5. **Text is carved geometry or it is an edit layer.** Never described as text to
   be read. Lettering morphs under motion, and a locked camera only slows it.
6. **Nothing runs without approval.** `paid_generation_approved_by` null means
   nothing generates, including one sample to check the settings. A test
   generation is a generation.
7. **Prompts are ordered by importance and written in the target engine's dialect.** The lock first,
   verbatim; then the motion; then frame, look, audio and exclusions. **There is no element cap.**
   The real mechanism is positional adherence decay - late instructions get dropped first - so the
   remedy is order, never amputation, and **nothing is ever removed from the shot to shorten a
   prompt.** Format strictly in the verified dialect of the target engine:
   natural-language prose, positional reference tags, or parameter flags for Wan.
8. **A generation request never exceeds the verified clip ceiling. The shot it serves is untouched.**
   Never ask for 8 seconds from a 5-second engine - that is a malformed request, and it boils. **But
   the ceiling governs the request, never the shot list**: a shot longer than the ceiling
   arrives here with a designed join from the Phase 3 shot plan or Phase 6 animatic and is generated as chained clips through dual-frame
   anchors, still one shot. A shot shorter than the engine's comfortable minimum is generated long
   and trimmed to its real duration. **Phase 8 never returns a shot to Phase 3 asking for it to be shortened,
   lengthened, split or simplified to suit an engine.** If no available engine can serve the shot as
   designed, that is a note for the engine-selection step to pick a different engine.
9. **This module refuses to determine shot durations, focal lengths, and the design of sound. It
   does write spoken lines into the prompt where the engine speaks them.** Shot sizes, lens choices
   and timeline durations are owned by the shot plan (`cinematography_shot`). **Voice casting, delivery
   direction, synthesis, music and the acoustic mix are owned by the audio stage**
   (`audio_voice_music_sfx`) wherever the route opens it, and none of that is decided here.
   **What this module does own is the prompt**, and on an engine with native audio the spoken line
   is part of the prompt: this stage quotes the words the screenplay and dialogue stage wrote,
   verbatim, into the `[AUDIO]` block of 4.2d.
   Writing them is transcription into a field, not audio design - see 4.8b, which decides once,
   before any prompt is written, whether speech is native or synthesised.

**When these conflict**, the priority order is 2, 6, 8, 1, 4, 7, 3, 5, 9. Verbatim locks (2)
and financial approval (6) outrank model clip boundaries (8), which outrank single camera moves (1),
physical motion paths (4), prompt ordering (7), cross-clip memory (3), text geometry (5), and
ownership refusal (9). You sacrifice from the bottom.

### 4.0b The Mesopotamia canon

On a Mesopotamian project the canon at the Mesopotamia canon is open. It opens only on a Mesopotamian subject.

**What this module needs from it:** Grimoire heading 7 for how anything moved, and heading 8 for
armies, weapons and formations. Motion taken from the canon removes the commonest heritage error,
which is modern movement in ancient clothes.

### 4.1 Describe motion, not the scene

This is the single most common mistake, and it is worth stating first.

A video prompt is not a longer image prompt. If a start frame exists, the scene
is already established by that frame. Re-describing the scene at length fights
the frame and often produces a different scene that happens to resemble it.

Write, in this order. **The order is the point, not a preference** - late instructions are what a
weaker engine drops first, so the identity goes where nothing can drop it:

1. **The locks** - character and object identity sentences, quoted verbatim, first.
2. **The motion** - what moves and how, subject motion before camera, then the camera's
   trajectory with its speed word and its landing state.
3. **The frame** - size, angle, height, where things sit.
4. **The look** - light, palette, optics, and anything that changes over the clip.
5. **The audio** - including silence.
6. **The exclusions** - the negative list, or positive phrasing where negatives are unsupported.

This is the same six-slot order stated at 4.1b and filled out by the nine blocks of the template in
4.2d. **One order, three levels of detail** - if they ever disagree, 4.2d is what ships.

When there is no start frame, a brief scene establishment comes first, but it
stays brief. The motion is still the point.

### 4.1b Write for the strongest engine, and order the prompt so a weaker one degrades well

**The governing principle for every prompt this module writes.** A prompt is written for the most
capable engine available, carrying everything the shot actually needs. **It is never written down to
the weakest engine in the list.** A strong engine uses the whole thing; a weak one, at worst,
ignores an instruction it cannot act on - and an ignored instruction costs nothing, while an
instruction never written costs the shot.

**Writing to the weakest engine is the expensive mistake**, because it is invisible: every prompt
comes back looking fine, and nobody ever sees the film that was not asked for.

#### The real mechanism is order, not count

What actually happens is **positional adherence decay.** Instructions
late in a prompt get dropped first. The character caps are large on current engines - the figure for yours is a line of its record in
[`ENGINE-CHECK.md`](../ENGINE-CHECK.md) - so **length is almost never the binding constraint. Position is.**

That changes the remedy completely. **Do not cut the prompt down to a safe number. Order it so that
whatever gets dropped is the part you could afford to lose.**

```
1. The locks           character and object identity sentences, verbatim
2. The motion          what moves, the camera trajectory, the landing state
3. The frame           size, angle, height, where things sit
4. The look            light, palette, optics
5. The audio           including silence
6. The exclusions      negatives, or positive phrasing where unsupported
```

**A weak engine reading that list top-down keeps the identity and the motion and loses some of the
grade.** The same list written in the reverse order loses the face. That is the whole of the
technique, and it costs nothing on a strong engine.

#### What replaced the old budget

This section used to compute `budget = lock_lines + motion_lines + negative_lines` and declare a
shot **overloaded above 14**, with three remedies in order: **remove a subject from the frame**,
split the shot, move the text out. **The first two are void** - they change the film
to suit a tool, and they were the only rule in this module that did. The observation underneath was
real; the remedy was aimed at the wrong thing.

**What survives, because it was always true:**

- **Never shorten or paraphrase a lock.** It is the one line that must reach the engine whole. A
  paraphrased lock is how a face drifts, and a drifted face costs a regeneration.
- **A prompt carrying everything carries nothing** - but the cure is **hierarchy, not amputation**.
  Say the important things first and say them plainly; let the rest follow.
- **Where a prompt genuinely runs long**, prefer numbered beats over one dense paragraph. Structuring
  as `Beat 1 / Beat 2` or timestamps partially defeats positional decay, which is why every engine
  that supports multi-beat prompting wants it.
- **If a specific engine truly cannot hold the shot**, that is a note for the engine-selection step to pick a different
  engine. It is never a reason to take a person out of the frame.

#### The check

Before a prompt leaves this module: the lock is verbatim and first; the motion is second; nothing
was removed from the shot to make the prompt shorter. **A prompt is judged by whether it asks for
the whole shot, never by its length.**

### 4.1c What this module does when it does not know

This module writes the last thing before money is spent, so a guess here is paid
for immediately.

**Search before relying on a model parameter.** Look it up in the model's own current
documentation; confirmed, use it. Not confirmed, write `not documented, verify on the model page`,
write the prompt so it does not depend on it, note the choice under `decisions`, and carry on.

**Never guess a clip limit.** A prompt written to an assumed limit comes back
truncated, and the whole shot is regenerated. If [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) has not
been filled for this project, write the clip at the shot's designed length and mark the cell
`pending_engine_check`. Never shorten the move to fit a ceiling nobody has checked.

**What gets written instead of a guess:**

| Unknown | What is written | Who resolves it |
|---|---|---|
| A model capability | `not documented, verify on the model page` | the engine record, before anything is generated |
| The clip limit | `pending_engine_check`, and the clip is written at the shot's designed length | the engine record |
| A lock for a subject in frame | one placeholder lock line marked `assumed` | the continuity record, before anything is generated |
| Whether the model produces audio | `speech_mode: pending_engine_check`: write both branches, the `[AUDIO]` block complete with the `[SILENT-ENGINE SUBSTITUTION]` block beneath it (4.8b) | the engine record |
| Whether a negative token is supported | include it anyway. An unsupported negative is ignored, a missing one is not | nobody, this is settled |

**Nothing in this table stops the prompt.** Every unknown has something written in its place that
travels with the handoff, because a visible open cell costs a minute and a guessed one costs a
re-render. The engine record is [`ENGINE-CHECK.md`](../ENGINE-CHECK.md); §3 there is the rule.

**The asymmetry that decides the safe direction.** An unnecessary negative token
costs nothing. A missing one costs a regeneration. When uncertain about a
negative, include it. When uncertain about a capability, do not rely on it.

### 4.2 The measured camera move

One camera intention per clip is the default, because a shot that says one thing
says it clearly. It is **not** a model limit: a move that develops
on purpose - a push that opens into an orbit, a crane that settles into a track -
is written as one continuous trajectory and declared. What still produces an
unusable clip is two unrelated moves thrown together with no intent behind either.
Name the move with a speed. "Slow push in" produces a different and better
result than "push in". "Slight drift left" is better than "pan". The models
respond to the qualifier more than to the verb.

If the shot genuinely needs a move that develops - a push that becomes an orbit,
a track that rises into a crane - **write it as one continuous trajectory and
declare it** (law 1). It is one shot, it stays one shot, and if it runs
past the clip ceiling 4.2b chunks the generation without touching the design.
Sending it back to the Phase 3 shot plan to be halved is the reversed rule and it is void. What
still goes back is the *accidental* stack: two unrelated intentions sharing one
clip because neither was worth its own shot. That is a directing problem, and Phase 3
owns it.

### 4.2b How much film goes in one clip

**"One camera intention per clip" was written when a clip was three to five seconds.** At that
length, one clip and one shot are the same object and the rule is sound. **Engines now render up to
thirty seconds**, and at thirty seconds the rule becomes nonsense: it asks for a single push-in that
travels for half a minute and then stops. Nobody has ever shot that, and nobody wants to watch it.

**The clip's length decides how much film goes in it, not how little.** Read the ceiling from the
verified engine capability record, then fill it deliberately:

| Clip length | What it holds |
|---|---|
| **Up to about 6 seconds** | **One shot, one intention.** The classic case. This is where the original rule belongs and it still applies here |
| **About 6 to 30 seconds** | **A sequence.** Never one move stretched to fit. Two legitimate fillings, below. **How many shots go in it is in 4.2c, and it is never one by default** |

**Filling A: native multi-shot - real cuts inside one generation.** Where the engine conditioning guide
documents the mode for the endpoint in use, write **several shots inside the clip**, each with its
own size, angle, move and duration. How the engine takes them - shot headers, a prompt and a
duration per shot, timestamp ranges, a multi-clip switch, explicit cuts - and how many shots of
what length, is provider syntax, recorded and dated in its record in
[`ENGINE-CHECK.md`](../ENGINE-CHECK.md) (§5). **In that verified mode, naming the cut is correct, not forbidden.** Unverified means the
engine renders continuous motion and will turn a requested cut into a morph - there, use Filling B
or generate the shots separately and cut them in the post-production edit.

**Filling B: a designed long take.** One unbroken shot whose movement **develops through named
phases**, which is what a long take has always actually been. A thirty-second Steadicam in a real
film is never one move; it is a series of moves inside one continuous take, each with a reason.
Write it as phases with durations:

```text
0.0-4.0   crane descends from the rooftop line to street level, settling
4.0-9.0   settle into a track, following the runner from behind
9.0-14.0  the runner turns; the camera loses them and holds on the empty alley
14.0-18.0 slow push into the doorway they entered
```

That is **one shot** - one row in the shot list, one unbroken take to the audience - carrying a
developing move declared per law 1. **It is not a stack**, because the phases are consecutive and
motivated, and each hands to the next.

**What is never right at any length:** one move applied uniformly across a long clip because the
rule said one move. A twenty-second slow push-in is not restraint, it is an unfilled container.

**A held performance is a filling, not a gap.** Where the script holds on a face or a still exchange,
Filling B's phases are the performance beats the script already wrote (a look, a breath, a line
landing) under a still or near-still camera, declared as a long take. Never invent business to fill
a hold: the script is locked, and a clip is filled from what it already contains.

**Choosing between them.** Use A when the moment wants cuts - coverage, escalation, a reveal that
needs a reaction. Use B when the moment wants continuity - a space revealed as someone crosses it,
a tension that a cut would release, a performance that should not be interrupted. **Both are
declared in `declared_decisions`**, because both are directing choices and neither is a default.

**The pipeline consequence.** A clip is a container this stage fills; it is never a shape the
shooting script must design around. If the script hands down a scene of eight shots and the engine
renders fifteen seconds, this stage may pack several of those shots into one generation using
Filling A - **the shot list does not change**, only the generation plan does. The clip never
reshapes the direction, upward or downward.

### 4.2c The clip-length question, and everything it decides

**Settle this once, here, before the first prompt is written.** The scenes exist, the shot list exists,
[`ENGINE-CHECK.md`](../ENGINE-CHECK.md) has named the model and recorded its real ceiling. This is the first moment the question can be
answered well, and the last moment before it silently answers itself.

The clip length is the brief's call. **If the brief states one, use it.** If it does not, this stage
chooses and records the choice under `decisions`; nobody is asked:
- on a `flexible` engine, each clip at the length its content wants, to the nearest second;
- on a `fixed_set` engine, the allowed value that best fits the grouping below;
- with no engine named yet, every clip at its designed length under `pending_engine_check` (4.1c),
  regrouped when the engine is chosen.

#### Two kinds of engine, and they are handled differently

**Most current engines take any whole number of seconds in a range**; some expose only **a fixed
set** of lengths. Both are
recorded in the engine's row in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md), which supplies the
verified value; **never assume which kind an engine is.**

| Mode | Field | What it means for the prompts |
|---|---|---|
| `flexible` | `clip_duration_mode: "flexible"`, `clip_range_seconds: [3, 30]` | Each clip is written at **the length its content wants**, to the nearest second. A 4-second clip and a 19-second clip in the same piece is normal and correct |
| `fixed_set` | `clip_duration_mode: "fixed_set"`, `clip_durations_allowed: [5, 10]` | Every clip is written at one of the allowed values. **Nothing is written at a length the engine cannot produce** |

**A shot shorter than the engine's shortest clip** — a 2-second shot on an engine whose range starts
at 3, or a shot under the smallest allowed value of a `fixed_set` engine — **is generated at the
engine's minimum and trimmed to its designed length in the edit**, wherever it is not grouped with
its neighbours into one clip (below). The shot is never lengthened to suit the engine: the action is
written to land inside the designed seconds, the rest of the clip is handle, and the plan records
both lengths, designed and generated. Law 8 says the same from the ceiling's side.

#### What a fixed length obliges, and this is where pieces break

When the length is fixed - say every clip is 10 seconds - **every prompt is built to fill exactly
10 seconds, and so is everything inside it.**

- **Dialogue and narration are written to the clip, not truncated by it.** The commonest failure in
  generated work is a line still being spoken when the video stops. **Count the delivery before
  writing the prompt**: at normal pace roughly 2.2 to 2.8 words per second, slower for weight, faster
  for urgency. A 10-second clip holds roughly 20 to 26 spoken words plus the breath around them.
  Write the line to land **inside** that, with the last syllable finishing before the last frame, not
  on it.
- **A line that will not fit is split at a breath, across clips** - never clipped mid-word, and never
  rushed to fit. Where a clip must end mid-thought, it ends **on a breath or a beat the edit can
  carry**, and the join rules in 4.6 carry the delivery across. The writing is untouched; only the
  delivery is divided — the words themselves belong to the screenplay and dialogue stage, and law 8
  above is why it is the clip that bends and never the writing.
- **Action is timed to fill it too.** A 10-second clip carrying three seconds of action and seven of
  nothing is a wasted generation. Fill it with the shots that belong in it, below.

#### How many shots go in one clip: the length decides, and it is never one by default

**This is the most important line in this section.** The clip is a container. Its length decides how
much film goes inside it, and **"one shot per generation" is not the rule and never was** - it was an
accident of the era when a clip was three seconds long.

| Clip length | What goes in it |
|---|---|
| 3-6 s | One shot, usually. One intention, one action |
| 7-12 s | **Two to four shots**, or one shot whose move develops through named phases |
| 13-20 s | **Three to seven shots**, or a designed long take, or a mix |
| 21-30 s | **A full sequence.** A whole small scene can live inside one generation |

Fill it one of the two ways in 4.2b: **real cuts inside one generation** where the engine documents
the mode, or **a long take written as named phases with durations**. Both are declared. **What is
never right is one shot loosely occupying a long clip because nobody asked what else could be in
there.**

**When the length is flexible, the shot list leads.** Read the shot list from the Phase 3 shot plan and group its shots
into clips at natural seams - a continuous action, a single location beat, a run of shots sharing one
camera position. Let each clip be as long as its group needs, to the nearest second. **The shot list
does not change**; only the grouping does.

**When the length is fixed, the grouping does the work.** Pack the shot list into equal containers,
cutting at the seams that survive a hard boundary. A 30-second piece at 10-second clips is three
generations, and each of those three may hold two, three or four shots. **Three generations does not
mean three shots.**

#### Written into the Plan, and who writes which half

**The engine-selection step records the engine's capability** at its capability pass, before this module opens:
`clip_duration_mode`, and `clip_range_seconds` or `clip_durations_allowed`, each with the date verified.
**Phase 8 never guesses those** - it reads them from the engine specification.

**Phase 8 writes the choice made inside that range:** `target_clip_seconds` and `clip_length_source`.
```text
"target_clip_seconds": 10,
"clip_duration_mode": "fixed_set",          # read from engine selection, not written here
"clip_durations_allowed": [5, 10],          # read from engine selection, not written here
"clip_length_source": "stated",
"_clip_plan_note": "Every prompt is built to fill its clip exactly. Dialogue is counted against the duration before the prompt is written, never truncated by it. The number of shots inside a clip follows its length and is never assumed to be one."
```

**The check before any prompt leaves this skill:** every clip has a length the engine can actually
produce; every spoken line finishes before its clip does; and **no clip longer than six seconds
contains a single shot unless that was a declared long take.**

### 4.2d The video prompt template

**This is the shape every video prompt takes in pipeline mode.** It is written for the most capable
engine available, ordered so a weaker one degrades well, and it holds as many shots as the
clip's length allows (4.2c). Blocks marked *conditional* are written only when their input exists;
an absent block is deleted, never left as an empty heading.

**The animation carve-out applies here, exactly as it does in the image stage.**

On flat 2D, cel-shaded or cartoon work the whole optical and photographic vocabulary is replaced,
not softened: focal lengths, f-stops, apertures, sensor formats, depth-of-field calls and the Kelvin
figure. None of them exists in drawn animation, and writing one there sends a photographic
instruction to line art, which either does nothing or returns a haze sitting on top of the drawing.
What goes in their place is the art style, the line weight, the ink and colour treatment, the
**drawn light direction in words** and the **palette temperature in words**. The requirement does
not relax; the units change. 3D and rendered CG keep the photographic values, because there is a
virtual camera with a real focal length behind the frame.

**Stop motion and other physically-made looks are a third answer, and the motion is where they differ.** A puppet moved frame by frame has its own temporal signature — a very slightly uneven cadence, the small held stillness at the extremes of a move, the absence of true motion blur, and a camera that moves in increments rather than continuously. Those are the qualities that make it read as made by hand, and a prompt that asks for smooth interpolated motion removes all of them. The package has the craft in `time.stop_motion` and `time.go_motion`; direct the cadence explicitly rather than letting the default supply it. On surfaces, this register keeps its handmade texture as a positive and does **not** strip the glossy-default negatives — see the 3D branch of Tier 1.

**What does not change is the motion on drawn and rendered work.** A camera move in animation is a real move — the multiplane
pushes, the pan is drawn, the parallax is built — so every movement field in this template is filled
the same way on drawn work as on live action. The lens is what goes; the movement stays. That is the
one difference from the image stage, and it is why this phase needed the rule written out rather
than inherited.

This is law 5 of [`../phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md`](../phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md),
which owns the carve-out for the package.

**Which mode this clip is in is a field, not an assumption.** The carve-out above tells you what
changes; the `[RENDER MODE]` block below is what tells you *which branch this clip takes*, and it is
required on every prompt including a single-look one. Take it from the **Mode & Look** cell of the
Phase 3 shot table and from `render_mode` on the Phase 7 output contract, both of which carry it per
row and per prompt for exactly this reason. On a film that alternates two looks — a reconstruction
documentary cutting between photographed footage and drawn rebuilds — **it changes between clips**,
and a prompt that does not state it hands the next reader a guess. This block used to be absent from
this phase entirely: the mode was threaded carefully through Phases 3, 6 and 7 and then stopped, and
a test agent carried it by hand across 48 clips.

```text
[RENDER MODE]                                        required, always first
<built - a chart, map or diagram assembled from data; this clip is NOT generated, and the block
 below describes the motion for whoever builds it |
 photoreal | 3D / rendered CG, and the surface it is made of | flat 2D / cel, and the art style,
 line weight and ink treatment>
<on a two-look piece, the look this clip is in, taken from the shot table's Mode & Look cell>
<this block decides which vocabulary every block below uses: optical values on photoreal and 3D,
 drawn values on flat 2D - and the motion blocks are filled the same way either way>

[IDENTITY LOCKS]                                     required
<the verbatim 30-45 word character sentence from the identity-consistency record (ident.frozen_sentence), quoted in full, once per
 character in frame - never paraphrased, never shortened, never "as before"; a character only partly in
 frame (hands, back): its visible clauses only, never the face clauses, and `face out of frame` (4.3)>
<the verbatim object or motif lock, where one is in frame>

[REFERENCES]                                         conditional: engine supports references
Core subject:  @Character1 - <what to take from it, and its current state; the costume comes from the image>
Props:         @Prop1 - <what to take>, @Image2 - <what to take>
Environment:   @Location1 - <what to take>
Do not copy:   <what each reference must NOT contribute>

[ENVIRONMENT]                                        required
<location, time of day, weather, and the dynamic elements - dust, rain, smoke,
 crowd - that must be alive in frame>

[VISUAL LOOK]                                        required
Optics:    <focal length in mm>, <stop or depth behaviour>     live action, 3D and rendered CG
           <art style, line weight, ink and colour treatment>  flat 2D, cel-shaded, cartoon
Lighting:  <direction, quality, colour temperature, named source>   live action, 3D, CG
           <direction and quality in words, palette temperature in words>  drawn work
Palette:   <the base_look_lock for this scene>
Grade:     <named stock or render register - never "cinematic", never "8K">

[TIMELINE]                                           required; one entry per shot in this clip
00:00 - 00:05 | SHOT 1: <its job in three words>
  CAMERA:   <size, height, angle, lens - on drawn work omit the lens>; <one named move with a
            speed word and an end state>
  ACTION:   <visible movement with a physical start and a physical finish>
  PERFORMANCE: <eye shift, micro-expression, jaw, breath, weight change>
  VFX:      <conditional> at the moment of <action>, <effect> appears at <position>,
            behaves through <movement>, and <dissipates / transforms / settles>

00:05 - 00:15 | SHOT 2: <its job>
  TRANSITION: <cut | continuous take | pan into>
  CAMERA / ACTION / PERFORMANCE / VFX as above

[AUDIO]                                              conditional: engine generates audio
Dialogue:  <Character>: "<exact words>" - <delivery, accent, volume>
Ambience:  <background that persists for the whole clip>
SFX:       at <time>: <source, spatial position, intensity>

[ENDING]                                             required
Final frame: <the exact composition and facial state the clip ends on>

[CONSISTENCY]                                        required
Keep identical throughout: <face, light direction, palette,
 the things that must not drift>

[NEGATIVE]                                           conditional: engine has a negative field
<built per shot from the three sources in 4.9 - never boilerplate>
<where the engine has no negative field, phrase these as positives in CONSISTENCY>
<the list branches by RENDER MODE, exactly as the image stage's tiers do: the photographic
 failure tokens belong to photoreal work; a stylised render KEEPS `CGI 3D sheen` and the
 plastic-shader tokens, because that glossy default is precisely what a clay, felt or carved
 surface must not look like, and drops only `plastic skin` and `wax figure`, which describe a
 human face; drawn work forbids photographic texture, lens blur and grain leaking into the line
 art. The image stage owns this fork and this line follows it>
```

#### The five things that make this template strong, and why each is there

1. **The timeline is the point.** A clip is a container and its length decides how many shots go in
   it (4.2c). This template makes that visible: **one `SHOT` entry per shot, with real timecodes
   that sum to the clip length.** A 5-second clip has one entry. A 15-second clip usually has three
   or four. **A long clip with one `SHOT` entry is the unfilled container 4.2b names**, and the
   template shows it at a glance.
2. **Every action has a start and a finish, and every effect has four parts** - trigger, position,
   behaviour, ending. A described effect with no end state is where generations go soft.
3. **Performance is written, not hoped for.** An eye shift, a jaw, a breath. This is the layer that
   separates a moving photograph from a performance, and no model invents it unasked.
4. **The final frame is stated.** It gives the motion somewhere to land, and it is what the next
   clip chains from when a shot spans several generations (4.6).
5. **Consistency is positive, negatives are per shot.** "Keep the face and the key direction
   identical" works on every engine. The negative block is built from the three sources in 4.9 and
   dropped entirely where the engine has no field for it.

#### How it flexes

- **Shots grow and shrink with the clip length.** Read `target_clip_seconds`; write as many `SHOT`
  entries as the clip holds and make the timecodes sum exactly. On a `fixed_set` engine every clip
  has the same total; on a `flexible` one each clip is as long as its content needs.
- **Tags appear and disappear with the sheets.** `[REFERENCES]` carries only the sheets that exist:
  a character sheet gives `@Character`, a location plate gives `@Location`, a props sheet gives
  `@Prop`. **No sheet, no tag** - and then `[IDENTITY LOCKS]` carries the whole burden in words,
  which is why it is required and first even when references are available.
- **Blocks are deleted, not emptied.** An engine with no audio gets no `[AUDIO]` block, and nothing
  in the prompt mentions sound (see the failure table in section 8).

#### What is never done to this template

**Nothing is removed from the shot to make the prompt shorter.** If it runs long, that is
what it costs. If a specific engine cannot hold it, that is a note for the engine-selection step to name a different
engine - never a reason to drop a character, a shot entry, or an effect.

### 4.3 Carrying the locks

Every locked character or object in frame carries its mandatory sentence from the identity-consistency record (`ident.frozen_sentence`),
**quoted verbatim, not paraphrased, in every single prompt**. Check `frozen_sentence_status` in `project.yaml` first:
`locked` from the identity record, or `project_scoped` where operating without an upstream identity record, may be quoted. A
`lockable` sentence has not been frozen and is not quoted yet.

**A shot that shows only part of a character** (hands only, from behind) **quotes only the parts that are visible** —
the clauses the frame shows, verbatim, with the wardrobe on them taken from the keyframe — **never the face clauses**.
Write `face out of frame`, and quote the whole sentence again the moment the face can be seen. This is the image
guide's law 4 ([`how-to-write-an-image-prompt.md`](../phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md)),
carried to the clip: a hands-only keyframe animated under a full face sentence invites a face into the frame.

Never write "the same man as before", "the character from the previous shot", or
any reference to another generation. The model has no memory of the previous
clip. Such a phrase is not just useless, it consumes prompt space and sometimes
introduces a second person into the frame.

If the mandatory sentence is long, it still goes in whole. Shortening it is how
faces drift.

### 4.4 Objects need a path

Any object that moves needs a stated path, a start position and an end position,
and a statement of what it rests on or is attached to. Without these, generated
objects hover, slide, or pass through things.

The phrase "no hovering" earns its place in the negative list whenever anything
is falling, thrown, carried or placed.

### 4.4b Flashing light

A clip that carries a deliberate strobe or rapid flash sequence (a strobe, flash frames, fast cutting
on a white frame, a rapid run of lightning) is written **without a rate**.
The shot table row already carries `pending_photosensitivity_check`; carry it into the clip's notes
unchanged. How fast it may repeat and when it must stop belong to `safety.photosensitive_flash`, and
a person whose profession it is sets them (root `SKILL.md` §0). This module writes neither.
**Ordinary light is never a flash question**: firelight, candles, a lamp, a sunset, a sweeping beam or
a flickering bulb in a scene is written as the scene wants it, with no marker.

### 4.5 Reference sheets, grouping, and the panel trap

When a multi panel reference sheet is used, the model may read the panels as
separate shots and produce a cut. Group them explicitly: state that all panels
show the same single subject or place, that the output is one continuous shot,
and that labels, borders and panel divisions are to be ignored.

Never crop a reference sheet to avoid this. Cropping loses the information the
sheet exists to carry. Group it in words instead.

### 4.6 Clip length and joins

**The shot's length is the shot's. The clip's length is the engine's.** The shot plan never
splits a shot to fit a clip - it keeps the shot whole and hands over a generation
plan. This module then writes that shot across as many clips
as the plan needs, at the length 4.2c settled. Where one shot spans
two or more clips with designed joins, every clip carries:

- The same locks, quoted identically.
- The same light direction and palette.
- An explicit continuity anchor, which is usually the end position of the first
  becoming the start position of the second.
- The join method, usually a matched move, so the cut is invisible.

### 4.7 Text in frame

Assume generated text will morph. If lettering must appear:

- Describe it as carved, embossed, woven or printed geometry, never as text to
  be read.
- Lock the camera hard. Motion multiplies the morphing. Where Phase 3's shot table designed a move
  across the lettering, keep the move at its slowest and treat the lettering as seen, not read
  (`ai.text_carved_geometry`); Phase 8 may not re-decide the shot.
- Do not state what the letters say if it does not matter.
- If it must be legible and correct, do not generate it. Plan it as an edit
  layer and hand it to post-production editing.

### 4.8 Audio

If the model generates native audio, say what should be heard and what should
not. Silence is a choice worth stating. If the model does not generate audio,
say nothing about sound in the prompt and hand the sound design to Phase 4 (Audio & SFX) instead,
because sound words in a silent model sometimes leak into the image as
implausible motion.

**When the route has no Phase 4.** The commissioned-advert route — Phase 1 → 2 → 3 → 6 → 7 → 8 — never
opens Phase 4, and neither does the storyboard-only or the prompts-from-stills route. On those the
sentence above hands the sound to a stage that will not run, and the foley the package makes the
default for a silent brief ends up owned by nobody. **The sound intent is still recorded; it is
recorded here instead.** Write it per clip, into the stage deliverable's `sound_intent` field beside
`audio_expected`, as one line naming what the clip should be heard to do — *three footfalls on
gravel, the cap turning, room tone only, silence held to the cut*. It is an intent, not a mix: no
levels, no cues, no track layout, because none of that is this stage's craft.

That line is what the editor works from when there is no audio stage between this phase and the
timeline, and it costs a sentence. **Writing nothing is the one option that is not available**, because
a clip that arrives with no stated sound intent gets whatever the edit happens to reach for, and on a
silent-engine advert that is usually nothing at all. Where Phase 4 *does* run, this field is a note
to it and Phase 4 still owns the sound; the field never becomes a second sound design competing with
the first.

### 4.8b Native speech or synthesised speech. Decide once, before the first prompt.

**This decision is made before any prompt in the batch is written, and it is never revisited
mid-batch.** Getting it wrong costs the whole batch twice: prompts written silent that then need
dialogue added, or prompts carrying dialogue that a silent engine turns into implausible mouth
movement. **Writing the batch twice is the failure this section exists to prevent.**

Two facts decide it, and both are already in the project brief:

1. **Does the piece have speech at all, and of what kind?** Stated audio mode from the intake menu -
   narration, dialogue, narration and dialogue, no speech, or music and SFX only.
2. **Does the named engine generate audio?** From the verified engine capability record. Never from
   memory: it changes per engine and per version.

| Piece has | Engine generates audio | What Phase 8 does |
|---|---|---|
| Dialogue, on camera | Yes | **Write the lines into `[AUDIO]`**, verbatim from Phase 2 (Screenplay & Dialogue), with the delivery note. The engine speaks and lip-syncs them. Phase 4 / Phase 5 still owns the mix, the ambience bed and any music laid over the finished clip |
| Dialogue, on camera | No | Write no speech in the prompt. Direct the mouth movement as performance - *"speaking, the last word landing as the head turns"* - and Phase 4 synthesises the line and post-production syncs it |
| Narration, voice over picture | Either | **Never in the video prompt.** Narration is not tied to a mouth in frame, Phase 4 owns it entirely, and putting it in a clip prompt binds it to a five-second boundary it should never have |
| A song sung on camera, from the music stage | Either | **Never in the video prompt as audio.** Direct the mouth as singing performance timed to the song's timing map; the song is laid under and synced in the edit. `speech_mode` is `none` for the engine, with `sung_on_camera` noted beside it |
| No speech | Yes | Say so: ambience and effects only, or explicit silence. An engine with audio left undirected invents a voice |
| No speech | No | Say nothing about sound at all, per 4.8 |

**Where the lines come from.** Phase 2 Dialogue Performance wrote them; Phase 8 quotes them **verbatim**,
exactly as it quotes a character lock. **Phase 8 never rewrites, shortens or paraphrases a line to fit a
clip** - if a line does not fit, 4.2c governs: the delivery is divided at a breath across clips and
the writing is untouched.

**What travels with the line.** The words in quotation marks, then the delivery: language and
accent, volume, pace, emotional state, and whether the character is facing camera. A line with no
delivery note gets read flat, which is the commonest disappointment with native-audio engines and
is entirely preventable. On a native-audio engine the voice is a lock too: quote the voice
description from `voice_cast` identically in every clip that character speaks in. Where the engine
speaks the language but not the dialect, that character takes the synthesised branch, recorded under
`decisions`.

**When no engine has been named — the normal case on a prompts-only brief — write
`speech_mode: pending_engine_check` and write both branches.** Keep the `[AUDIO]` block complete and
add a `[SILENT-ENGINE SUBSTITUTION]` block directly beneath it, one or two lines, saying what
replaces it: the mouth directed as performance, the speech handed to the audio stage. It costs a
couple of lines per prompt and it means **neither answer requires the batch to be rewritten**, which
is the failure this section exists to prevent. Delete the branch that does not apply the moment the
record is filled. Every other engine-dependent value in the package has this path, and the rule in
[`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §3 is explicit: a missing input never stops the work and
never gets guessed. This decision was the one exception, and demanding an answer that a zero-spend
brief cannot have is how a marker system develops a hole.

**Write it down.** The choice goes in the stage deliverable as
`speech_mode: "native" | "synthesised" | "none" | pending_engine_check` with the engine and date it was verified against,
so audio, editing and quality control all know which contract they are working under without inferring it from whether
a prompt happens to contain quotation marks.

### 4.9 The negative list

Build it from three sources, every time:

1. The project's `forbidden_global`. It lives at the root of the project brief, owned by the canon and world rules, and it is append-only. **What it holds, who may add to it, and what it is not is
   defined in [`FORBIDDEN-GLOBAL.md`](../FORBIDDEN-GLOBAL.md).** **When the project has not supplied
   one, the prompt is still written in full** and this source reads `pending_forbidden_global`, which
   travels with the handoff exactly as `pending_engine_check` does. Nothing waits on it. What must
   never happen is this source coming out empty with no marker: an unsupplied list and a project that
   genuinely prohibits nothing read identically on the page, and only one of them is a decision
   somebody made. A project that prohibits nothing records that, and this source then reads
   `none, per the project brief`. Both the marker and that note live on the prompt record and the
   handoff line, never in the negative string pasted into the engine (`FORBIDDEN-GLOBAL.md` §5).
2. The world negatives from the canon and world-building phase.
3. The generation negatives that apply to this shot type: hovering, extra
   limbs, duplicated subjects, morphing text, watermarks, and for heritage work
   specifically any modern or later-period element. **"A second camera move" and
   "a cut" are not on this list** - a developing move is legitimate under law 1,
   and a cut inside a long clip is legitimate under 4.2b. Negate them only on the
   clips where you actually want neither, never as a standing default.

   **Religious content is not on this list and is never a default negative.** It
   is a per-project decision and it reaches you only through this project's own
   `forbidden_global`, per the project's canon and editorial rules. Some work forbids it — a heritage
   channel that frames the ancient world as heritage rather than as faith; other
   work is built on it — a Christian children's song channel, or a documentary
   about a theological school where monks and a bishop are the subject. A blanket
   negative here would make those pieces impossible to generate.

The negative list is not boilerplate. A negative that does not apply to this
shot wastes attention that a real constraint could be using.

---

## 5. Decision Rules

```
IF the model or its verified clip limit is unknown
  THEN write the prompt in full at the shot's designed length, and mark the clip-length cell
  pending_engine_check. The engine record is what fills it, and the marker travels with the
  handoff until it does. Nothing stops (4.1c)

IF a start frame exists
  THEN describe motion and change, not the scene

IF the shot needs a move that develops
  THEN write it as one continuous trajectory with one start and one end state, declared (law 1).
  Only an accidental stack of two unrelated moves goes back to the Phase 3 shot plan, and that is a directing note,
  never a split

IF a locked subject is in frame
  THEN quote its mandatory sentence verbatim, always, in full

IF the prompt would say "same character as before"
  THEN delete it, the model has no memory

IF an object moves
  THEN state its path, its start, its end, and what it rests on

IF a multi panel reference is used
  THEN group it in words as one subject and one continuous shot

IF text must be legible and correct
  THEN do not generate it, hand it to post-production editing as an edit layer

IF the model has no native audio
  THEN write nothing about sound

IF the shot exceeds the clip limit
  THEN it is two prompts with a designed join, both carrying the same locks. **It remains one shot**:
  two generations serving one row in the shot list, never two shots
```

---

## 6. Research Protocol

Run before every batch, and date the result. Model behaviour changes faster than
anything else in this pipeline.

```text
<model> maximum clip duration <current year>
<model> prompt structure guidance official <current year>
<model> start frame end frame reference image support <current year>
<model> native audio <current year>
<model> known failure modes character consistency <current year>
<model> negative prompt support <current year>
```

Rules:

- Official model documentation outranks community advice.
- A limit older than one month is re-verified before a paid run.
- A parameter the documentation does not confirm is not relied on: the prompt
  is written without it and the choice noted under `decisions`.

---

## 7. Output Contract

```json
{
  "status": "submitted",
  "produced": ["phase_08_video_prompt_deliverable"],
  "locked": {
    "video_prompts": [
      {
        "shot_id": "S01-SH05",
        "model": "",
        "model_limits_verified_on": "",
        "clip_seconds": 5,
        "start_frame_asset_id": "",
        "end_frame_asset_id": null,
        "_frame_note": "start_frame_asset_id points at the kf-start asset, end_frame_asset_id at the kf-end asset from Phase 7 Keyframe Generation. On a single-frame model end_frame_asset_id is null. On a dual-frame model both are required: a dual-frame model given only a start frame invents the ending, which is the failure dual keyframes exist to prevent.",
        "prompt": "",
        "camera_move": "",
        "move_speed": "",
        "locks_quoted": [],
        "object_paths": [],
        "negative_prompt": "",
        "audio_expected": false,
        "sound_intent": "",
        "_sound_intent_note": "One line per clip naming what it should be heard to do - three footfalls on gravel, room tone only, silence held to the cut. An intent, not a mix. It is required on any route that does not open Phase 4 (Audio & SFX) - the commissioned-advert route, storyboard-only, prompts-from-stills - because on those the sound has no other owner and the editor works from this line. Where Phase 4 does run it is a note to Phase 4, which still owns the sound.",
        "speech_mode": "native | synthesised | none",
        "speech_mode_verified_against": "",
        "dialogue_lines": [],
        "join": { "with_shot": "", "anchor": "", "method": "" },
        "text_in_frame": { "present": false, "handled_by": "generation | edit" },
        "reference_assets": [],
        "reference_grouping_note": ""
      }
    ],
    "batch_notes": {
      "awaiting_spend_approval": true,
      "_note": "Set true because this batch is fully written and reviewed and now waits for the owner's go-ahead on spend. paid_generation_approved_by is filled by the owner alone; this stage never fills it.",
      "total_clips": 0,
      "estimated_cost_note": ""
    }
  },
  "open": [],
  "forbidden": [],
  "assumptions": [],
  "declared_decisions": [],
  "_decisions_note": "Creative choices this stage made where nothing dictated one. Each entry is {what, why, alternative_offered}. Whoever reviews the batch reads this field to tell a declared decision from an unsourced claim: a choice listed here is never a finding, and a choice nobody listed looks exactly like an invention nobody sourced. A stage that made real choices and declared none has removed the only evidence it was creating rather than guessing. One line per decision.",
  "updated_at": "",
  "_shape_note": "The seven keys the pipeline's stage-object contract requires of every stage object. The prompts and the batch note sit inside locked, because they are decisions that whatever runs the batch, once the owner has given the go-ahead on spend, must not reinterpret. An older draft of this contract carried video_prompts and batch_notes at the top level with none of the seven, which made this the one stage object a strict runner could not read."
}
```

`awaiting_spend_approval` is true while this batch is written and reviewed and waiting for the
owner's go-ahead. `paid_generation_approved_by` is filled by the owner alone; this stage never
fills it.

---

## 8. Quality Bar And Failure Modes

Good looks like: each prompt could be run by someone who has never seen the
project, and the clip would cut into the sequence without adjustment.

| Failure | How it shows up | Fix |
|---|---|---|
| Scene re-described in conflict with the start frame | The clip is a different scene that resembles the frame | Describe the scene as the frame shows it; new content only as motion and change. |
| Two unrelated camera moves | Unusable clip, or the model picks one at random | One intention with a speed qualifier, or a developing move written in order (law 1). |
| Lock paraphrased | The face drifts across shots | Quote the mandatory sentence verbatim, in full. |
| "Same character as before" | Sometimes a second person appears | Delete it. There is no memory between clips. |
| Object hovers or slides | Physics look wrong | State the path, the ends, and what it rests on. Add "no hovering". |
| Reference sheet read as a cut | The clip contains an unwanted edit | Group the panels in words. Never crop the sheet. |
| Text morphs | Lettering changes mid clip | Carved geometry, locked camera, or move it to the edit. |
| Sound words in a silent model | Implausible motion appears | Say nothing about sound unless the model generates it. |
| Boilerplate negatives | Real constraints get diluted | Build the negative list per shot from the three sources. |
| Stale model limits | Clips come back truncated | Section 6, verified and dated, every batch. |
| Generation without approval | Money spent without a decision | `paid_generation_approved_by` must be filled first. |

---

## 9. Worked Example

Shot S01-SH05 from the heritage example: the human figure enters for scale, seen
from behind, five seconds, 9:16, start frame generated by Phase 7, model produces five
second clips with start frame support and no native audio.

The prompt, written to the template in 4.2d. Five seconds holds one shot, so the
timeline has one entry. No character sheet exists for an anonymous figure seen
from behind, so `[REFERENCES]` carries only the gate plate. The engine generates
no audio, so `[AUDIO]` is deleted rather than left empty:

```text
[IDENTITY LOCKS]
The gate motif: deeply cut limestone, the same repeating rosette-and-palmette
band at the same height, the same weathering along the lower third, the same
chipped corner on the left jamb.

[REFERENCES]
Environment: @GateLocation1 - the gate geometry, the carving depth, the stone
colour and the weathering pattern.
Do not copy: the reference's overcast light or its camera height.

[ENVIRONMENT]
The gate approach, late afternoon, dry still air with fine dust hanging low in
the raking light.

[VISUAL LOOK]
Optics:   35mm, deep focus, the gate and the figure both legible
Lighting: low raking sun from the left, hard-edged, warm
Palette:  limestone ochre, shadow violet, one warm highlight
Grade:    natural daylight negative, mild halation in the highlights

[TIMELINE]
00:00 - 00:05 | SHOT 1: the figure gives the gate its scale
  CAMERA: wide, eye level, straight on, 35mm; one slow steady pull back at a
          constant speed, ending with the full gate height inside the frame
  ACTION: a single figure walks in from off screen at the lower left, seen from
          behind, crosses to the centre and stops facing the gate
  PERFORMANCE: the walk slows over the last two steps and the head tilts back
          as the figure stops, reading the height of the gate

[ENDING]
Final frame: the figure small and centred, seen from behind, head tilted back,
the full gate above them, the low sun still raking from the left.

[CONSISTENCY]
Keep identical throughout: the carved motif exactly as in the reference, the
light direction and quality, the figure seen from behind with the face never
visible, the figure in contact with the ground at every step.

[NEGATIVE]
face visible, figure turning toward camera, hovering or sliding feet, second
person entering frame, change of light direction, lettering on the stone
```

**Why it is shaped this way.** The lock is first and verbatim, so a weak engine
that drops late instructions still holds the motif. The move is one intention
with an explicit end state. The action has a physical start and a physical
finish. `[AUDIO]` is absent rather than empty, because naming sound to an engine
that cannot generate it invites implausible motion (section 8). The negative list
is built from this shot's three real risks, not from boilerplate.

**At fifteen seconds this becomes three `SHOT` entries**, not one stretched pull
back - the approach, the stop, and a detail of the carving at eye height - with
the timecodes summing to fifteen. The shot list from the Phase 3 shot plan is unchanged; only the
grouping into clips changes (4.2c).

**A note on that `[NEGATIVE]` block.** On the real heritage-channel version of this shot the list also
carries `no religious symbols` and `no flags`, because **that project put them in its own
`forbidden_global`**. They are not defaults and they are not printed in the template above. Copy the
entries the project in front of you actually carries, never the ones printed in an example.

Notes carried in the handoff: `locks_quoted` holds the gate motif sentence and
the from-behind sentence, both verbatim from the Phase 7 identity-consistency record. `object_paths` records the
figure's entry point and stopping point. `audio_expected` is false because the
model produces no audio, so Phase 4 (Audio & SFX) owns everything heard here.
The batch is complete, reviewed, and ready for execution through the spend gate.

## 10. Fast Path

For a single video prompt or rapid motion directive:
1. **Intake conditioning frames:** Identify the `kf-start` keyframe, and on a dual-frame model the `kf-end` keyframe beside it, then verify spatial continuity vectors across both.
2. **Order the prompt:** lock verbatim first, motion second, then frame, look, audio, exclusions. **No element cap** - nothing is cut from the shot to shorten a prompt. Keep motion to one camera intention and one subject action unless a developing move was deliberately designed and declared, in which case write it as one trajectory (law 1).
3. **Select model syntax dialect:** Format motion tokens into the dialect verified for the chosen model, and reported in the engine profile. This module never hardcodes a proprietary model name: the engine-selection step chooses it based on verified capability.
4. **Bind owned inputs and author physics:** Copy the shot duration from the shot plan, and the clip ceiling and model syntax from the dated record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md); author only camera trajectory speed and physical environmental forces. If the record is missing, write the prompt at the shot's designed length and mark the clip-length cell `pending_engine_check` — a move is never shortened to fit a ceiling nobody has checked.
5. **Output model-ready prompt:** Produce the finalized video prompt string with verified motion controls. Seed and other generation parameters belong to the engine adapter in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md) §5 and are not emitted here.
Skips multi-clip continuity chaining and automated fallback reaction matrices; these must be completed before paid video generation in the spend gate.
