# PROJECT-STATE — where a decision lives, and how it survives the next phase

A decision made in one phase and written only into that phase's prose is a decision the next phase
must re-read, re-derive, or guess. This package has lost three that way, and all three were found by
a person rather than by a check:

- **`render_mode` reached Phase 8 and never reached the Phase 6 guide.** The mode was threaded
  carefully through Phases 1, 3, 7 and 8, and the one phase between the shot table and the prompt did
  not mention it, so a test agent carried it across 48 clips by hand.
- **Three rate cards each claimed sole ownership of the same value**, so a figure copied into a
  second file drifted and rewrote a shot list without anyone editing it.
- **A heading said "three"** while the marker set had grown to five.

This file is the fix: **one place a decision lives, and a contract per phase saying what it may read
and what it may not decide again.**

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. `project.yaml` — the only place a decision lives](#1-projectyaml-the-only-place-a-decision-lives)
- [2. The stage contracts](#2-the-stage-contracts)
- [3. The check, and what it would have caught](#3-the-check-and-what-it-would-have-caught)
- [4. What this file does not do](#4-what-this-file-does-not-do)

<!-- /GENERATED:toc -->

## 1. `project.yaml` — the only place a decision lives

One file per project, beside the brief. Copy this and fill it. **Nothing downstream reads a decision
from another phase's document.**

```yaml
route:
  profile:         narrated_documentary # one id from the route-profile table in §2
  phases:          [1, 2, 4, 3, 6, 7, 8]
  timing_authority: measured_audio # designed / measured_audio / locked_music / existing_picture / external
  supplied_inputs: []             # keys supplied by the user rather than produced by a phase
  craft_only:      []             # phases opened for their craft only, outside the stage sequence: 5 for Phase 5 Route C score direction; its cue map goes under decisions as score_cue_map (a path), never into timing_map; Phase 3 reads it as advisory: where Phase 4's measured voice sets the runtime, the shot table follows the voice

brief:                            # the intake, answered once before execution
  format:          vertical_9x16  # vertical_9x16 / horizontal_16x9 / square_1x1 / portrait_4x5 / other:<ratio> / none (intake Q4)
  genre:           heritage_and_historical_documentary # two kits joined with + when the piece needs both (HOW-1 Q6); free snake_case: the Phase 1 format or genre kit the piece is built on (a commercial: nearest delivery kit + vlb.format.commercial_ad, HOW-1 Q6)
  language:        en
  duration_s:      300
  audio_profile:   narrated       # narrated / dialogue / song_led / silent / audio_only
  mode:            prompts_only   # intake Q1: prompts_only / express_stills / express_full / hybrid / director_review
  subtitle_language: null         # intake Q6: the subtitle language beside `language`, or null
  dialect:         null           # intake Q6: where the language has one that changes rate or casting
  age_band:        null           # intake Q6: children's work only
  # anything else the brief names word for word (end-card text, page name, subtitle burn spec, a required line) is copied under decisions as brief_<name>, in the brief's own words

inputs:                           # only what arrived from outside the pipeline; a phase's own result goes under outputs:, never here
  story_brief:     null
  branch_map:      null
  script:          null
  lyrics:          null
  speaker_map:     null
  source_audio:    null
  source_stills:   []
  still_brief:     null
  motion_brief:    null
  timing_map:      null
  existing_picture_timing: null

locks:                            # decided once, never re-derived
  render_mode:     photoreal      # one of: photoreal / rendered_cg / flat_2d / stop_motion / built / multi_look (the RENDER MODE SET in ENGINE-CHECK.md)
  looks:           single         # or the LOOKS: declaration when the piece alternates
  frozen_sentence: {}             # one entry per recurring character or recurring object, keyed by name: <name>: "30-45 words", quoted whole or not at all; a shot showing only part of the character quotes its visible clauses, never the face ones (HOW-PHASE-7 law 4)
  frozen_sentence_status: {}      # the same names, each: lockable / locked / project_scoped; only locked or project_scoped is quoted. Express run: the agent locks its own sentence and continues; otherwise project_scoped, quoted, pending the owner's approval; the keyframe approval (keyframes_approved_by, either form) locks every project_scoped sentence it covers
  palette:         []             # exact values, as many as the piece needs; a piece with two periods or looks keys them: {NOW: [...], THEN: [...]}
  rate_wpm:        {value: null, register: null, source: card}   # song-led piece: {value: null, register: melody_governs, source: the pacing card that hands the timing to the melody}
  forbidden_global: []            # from FORBIDDEN-GLOBAL.md
  engine_record:   ""             # path to the filled ENGINE-CHECK block
  paid_generation_approved_by: null   # null means nothing generates. A test is a generation
  keyframes_approved_by: null         # the owner's name and date at the keyframe gate (prompts-only: '<name>, prompts-only, <date>'); Phase 8 does not start while null
  child_voice_clone_consent: null     # only when a real child's voice is cloned from a recording: the parent's or guardian's name and the date

outputs:                          # phase-owned results; paths unless the value is intentionally inline
  story_brief:     null
  branch_map:      null
  script:          null
  speaker_map:     null
  lyrics:          null
  timing_map:      null
  stems:           []
  measured_duration: null
  voice_cast:      null
  mix_intent:      null
  shot_table:      null
  size_angle:      null
  timing_src:      null
  durations:       null
  panels:          null
  blocking:        null
  composition:     null
  keyframe_prompts: null
  clip_prompts:    null

decisions:                        # every choice, with where, why, and what it beat
  shot_31_cut:
    value:     cut.on_impact
    from:      phase-03
    reason:    "law 5 - a cut on movement disappears"
    runner_up: cut.reaction
    pool:      173                # candidates the shelf held
    survivors: 12                 # what the axes left

markers:
  open:     []
  blocking: []                    # markers the closing check lists first; a note for whoever delivers, never a stop
```

`paid_generation_approved_by: null` blocks **execution**, not design work. Phases may still write
prompts, timing plans and engine-ready handoffs while it is null. They may not call an image,
video, voice or music generator, including for a sample. A value records the person who approved
that spend; it is not a boolean inferred from the existence of an account or API key.

`keyframes_approved_by: null` stops **Phase 8 itself**, not only its spend. The keyframe approval
gate between Phase 7 and Phase 8 (`phase-01-story-generation/HOW-PHASE-1-WORKS.md`, the operating
modes) holds in every mode, and this field is how it is recorded: the owner looks at the approved
still deck and writes their name and the date here. Until then Phase 8 writes nothing, not even a
prompt, because a clip prompt written against an unapproved still is built on a frame that may
change. **In prompts-only mode**, where no still is ever rendered, the owner approves the keyframe
*prompt* deck instead and writes `<name>, prompts-only, <date>`; Phase 8 then writes the clip prompts,
and each one carries `pending_keyframe_render` until its still exists and has been checked against
the approved prompt. **Only the owner's own answer fills it.** An agent writes a name here only when the owner gave that
approval — in the conversation, or relayed in so many words — and writes it as given, adding where it
came from (`<name>, prompts-only, <date> — relayed in <message or file>`). It never infers approval
from silence, from an Express run or from `paid_generation_approved_by`, and reports the empty field
as the reason Phase 8 has not started. On `supplied_stills_video` the stills are the owner's own and the name is
written at intake, when they are handed over.

`child_voice_clone_consent` governs **one step and nothing else**: cloning a real, named child's
voice from a recording. That step waits until the parent's or guardian's consent is recorded here,
with their name and the date, because the voice platforms require it. Everything else in the
project carries on while it is null, and the field is never needed for a designed child voice or
for an adult performer playing a child (`phase-04-audio-narration/HOW-PHASE-4-WORKS.md`, Step 1).

**Three rules, and they are the whole point of the file:**

1. **A phase reads a decision only from `project.yaml`**, never from another phase's document. A
   phase's document says *how* to decide; the yaml says *what was decided*.
2. **A phase may not re-decide anything under `locks`.** Its contract below names which. A phase
   that finds a locked upstream value wrong does not edit it in its own file: it reopens the phase
   that owns the value, records the revision there, and re-runs what stood on it (PRECEDENCE.md,
   tier 4).
3. **An empty lock never stops the work.** It is filled by the working rule in the root `SKILL.md`
   §0 — the brief, the skill, the web, then the most suitable choice — and the choice is recorded under
   `decisions`. Three things wait for the user, as root `SKILL.md` §0 names them:
   `paid_generation_approved_by`, because generating costs money; `keyframes_approved_by`, which
   Phase 8 needs before it starts; and a real person's recorded consent before their voice or likeness
   is cloned (for a real child, the parent's, in `child_voice_clone_consent`).

## 2. The stage contracts

**This table is the authority.** Each phase's own `PHASE.md` carries its row inside a
`GENERATED:stage-contract` fence, written from here, so a phase cannot disagree with its contract and
nobody retypes one.

`intake` is phase 0: the intake questions in
[`phase-01-story-generation/HOW-PHASE-1-WORKS.md`](./phase-01-story-generation/HOW-PHASE-1-WORKS.md)
§1, plus the two project records. It reads nothing and writes the keys in its row below.

The first version of this table treated the union of everything a phase could read as one
mandatory list, which made valid routes impossible on paper — a voiceover from a supplied script
"required" a story brief nobody would ever write. This table separates four different facts:

- **Required** — every route that runs the stage must provide it.
- **One-of groups** — each semicolon-separated group needs one available key, not every key.
- **Optional** — consumed when the route produces it; its absence is valid.
- **External allowed** — a shortcut route may supply it directly and records that fact under
  `route.supplied_inputs`.

| Stage | Required reads | One-of read groups | Optional reads | External allowed | Writes | May not re-decide | Execution gate |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `intake` | — | — | — | — | `format`, `genre`, `language`, `duration_s`, `audio_profile`, `mode`, `subtitle_language`, `dialect`, `age_band`, `rate_wpm`, `engine_record`, `paid_generation_approved_by`, `keyframes_approved_by`, `child_voice_clone_consent` | — | — |
| `phase-01-story-generation` | `format`, `genre`, `language`, `duration_s`, `audio_profile` | — | `age_band` | — | `story_brief`, `branch_map`, `forbidden_global`, `render_mode`, `looks` | `format`, `genre`, `duration_s` | — |
| `phase-02-screenplay-dialogue` | `story_brief`, `language`, `audio_profile` | — | `branch_map`, `render_mode`, `rate_wpm`, `dialect` | `story_brief`, `branch_map` | `script`, `speaker_map` | `story_brief`, `branch_map`, `render_mode`, `looks` | — |
| `phase-04-audio-narration` | `language`, `audio_profile`, `rate_wpm`, `engine_record` | `script` or `source_audio` | `branch_map`, `speaker_map`, `child_voice_clone_consent`, `dialect`, `subtitle_language` | `script`, `branch_map`, `speaker_map`, `source_audio` | `measured_duration`, `voice_cast`, `mix_intent` | `script`, `branch_map`, `speaker_map` | `paid_generation_approved_by` |
| `phase-05-song-generation` | `genre`, `duration_s`, `engine_record` | `story_brief` or `existing_picture_timing` or `source_audio` | `script` | `story_brief`, `existing_picture_timing`, `source_audio` | `timing_map`, `lyrics`, `stems` | `story_brief`, `genre` | `paid_generation_approved_by` |
| `phase-03-shooting-script` | `render_mode`, `looks`, `audio_profile`, `duration_s` | `script` or `timing_map` or `existing_picture_timing`; `timing_map` or `measured_duration` or `durations` or `existing_picture_timing` or `duration_s` | `branch_map`, `lyrics`, `speaker_map` | `script`, `branch_map`, `timing_map`, `existing_picture_timing`, `durations` | `shot_table`, `size_angle`, `timing_src`, `durations` | `script`, `branch_map`, `render_mode`, `looks` | — |
| `phase-06-storyboard-layout` | `shot_table`, `size_angle`, `timing_src`, `render_mode`, `looks` | `timing_map` or `measured_duration` or `durations` | `branch_map` | `branch_map`, `shot_table`, `size_angle`, `timing_src`, `durations` | `panels`, `blocking`, `composition` | `branch_map`, `shot_table`, `size_angle`, `render_mode`, `looks`, `durations` | — |
| `phase-07-image-prompt-engineering` | `render_mode`, `looks`, `forbidden_global`, `engine_record` | `shot_table` or `still_brief` or `story_brief` | `branch_map`, `size_angle`, `panels`, `blocking`, `composition`, `durations`, `mode` | `still_brief`, `story_brief`, `branch_map`, `shot_table`, `size_angle`, `panels`, `blocking`, `composition` | `frozen_sentence`, `frozen_sentence_status`, `palette`, `keyframe_prompts` | `branch_map`, `shot_table`, `size_angle`, `render_mode`, `looks`, `durations`, `panels` | `paid_generation_approved_by` |
| `phase-08-video-prompt-engineering` | `render_mode`, `looks`, `forbidden_global`, `engine_record`, `keyframes_approved_by` | `keyframe_prompts` or `source_stills`; `durations` or `timing_map` or `measured_duration` or `existing_picture_timing` | `branch_map`, `shot_table`, `timing_src`, `voice_cast`, `frozen_sentence`, `frozen_sentence_status`, `palette`, `motion_brief`, `mode` | `source_stills`, `motion_brief`, `branch_map`, `durations`, `existing_picture_timing`, `render_mode`, `looks`, `forbidden_global` | `clip_prompts` | `branch_map`, `shot_table`, `durations`, `frozen_sentence`, `palette`, `render_mode`, `looks`, `size_angle` | `paid_generation_approved_by` |

The execution gate is read only at the moment a tool call would spend money or quota. Its presence in
the contract does not make it a prerequisite for writing the prompt package — which is why
`paid_generation_approved_by` moved out of Phase 8's reads and into its gate, and why every stage
that can call a voice, music, image or video generator carries the same gate.

### Route profiles checked before production

`intake` always runs and is omitted from the stage sequences below. An external key is valid only
when the route names it here **and** the receiving stage lists it under `External allowed` above.

| Route profile | Stage sequence | Externally supplied inputs |
| :--- | :--- | :--- |
| `full_narrative` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `narrated_documentary` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `music_video` | `phase-01-story-generation` -> `phase-05-song-generation` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `commercial` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `commercial_narrated` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `storyboard_only` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` | — |
| `one_still` | `phase-01-story-generation` -> `phase-07-image-prompt-engineering` | — |
| `audio_only` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` | — |
| `audio_with_cover` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` -> `phase-07-image-prompt-engineering` | — |
| `supplied_script_voiceover` | `phase-04-audio-narration` | `script`, `speaker_map` |
| `supplied_audio_cleanup` | `phase-04-audio-narration` | `source_audio` |
| `supplied_stills_video` | `phase-08-video-prompt-engineering` | `source_stills`, `motion_brief`, `durations`, `render_mode`, `looks`, `forbidden_global` |
| `score_existing_film` | `phase-05-song-generation` | `existing_picture_timing` |
| `interactive_branching_silent` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `interactive_branching_audio` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |
| `data_led_built` | `phase-01-story-generation` -> `phase-02-screenplay-dialogue` -> `phase-04-audio-narration` -> `phase-03-shooting-script` -> `phase-06-storyboard-layout` -> `phase-07-image-prompt-engineering` -> `phase-08-video-prompt-engineering` | — |

The six-question router in the [root entry point](../SKILL.md) reduces to these same dependency
shapes: no picture uses `audio_only`, or `audio_with_cover` when one still is also required; one
still uses `one_still`; moving picture uses `full_narrative`, `narrated_documentary` or
`music_video` according to its timing authority, `commercial` or `commercial_narrated` for an
advert without or with a measured voice, and `data_led_built` for a piece built from data; a board
with no motion uses `storyboard_only`; interactive work uses the silent or audio
branching profile; supplied material uses the matching script, audio or stills shortcut. The root
shortcut table cites these ids rather than retyping the sequences, so the two cannot drift apart.
Adding a new answer shape means adding a route profile here, so the validator executes it before a
reader can rely on it. **One extension is the agent's call, not a new profile:** when the story
itself contains a song that sets timing — sung or played inside a scene — any route that runs Phase 3
takes Phase 5 for that song, in the settled order (after Phase 4, before Phase 3), and records the
extended sequence in `route.phases` and the reason under `decisions`. The song's timing map governs
only the movement it plays under.

**Terminal keys** — written here and consumed outside the eight phases, by the edit or the delivery.
Nothing downstream reads them and that is correct: `mix_intent`, `stems`, `clip_prompts`,
`keyframe_prompts`.

**The row order is the dependency order, and it is not the file numbering: 1, 2, 4, 5, 3, 6, 7, 8.**
Phases 4 and 5 sit above Phase 3 because speech or a song that sets the runtime is made and measured
first, and the shot table is built to it (the route test of 2026-09-23 settled this). **It is a
relative order, not a list every route runs.** Each route profile keeps the phases it contains in
this order and drops the rest: `one_still` runs 1 and 7, `music_video` runs 1, 5, 3, 6, 7, 8, and the
supplied-material shortcuts start at the phase their input feeds. Dropping a phase is correct; running
two in the wrong order is not, and `route-order-drift` holds both the profiles and these rows to it.
A route that skips a phase skips its row, and the contract of a phase that does not run is not a
claim about that project.

**`rate_wpm` is written at intake, not by Phase 4.** It looks like a Phase 4 value and it is not: the
figure lives on a `pacing.*` card and the *register* is chosen when the piece is briefed, because
Phases 2 and 3 both estimate against it long before Phase 4 runs. Phase 4 writes
`measured_duration`, which is the thing that replaces the estimate. Writing the rate at Phase 4 was
the first version of this table and the check below rejected it.

## 3. The check, and what it would have caught

`contract-key-unwritten` reads the table above and reports two things **before production starts**:

- **A stage reads a key that no earlier stage writes.** This is the `render_mode` failure stated as a
  fact about the files rather than as something a reader has to notice. It fires at build time, not
  at round nine.
- **A stage writes a key nothing downstream reads.** A dead decision: work done, carried, and never
  used. Harmless to the piece and a reliable sign that either the key is obsolete or a phase is
  quietly re-deriving it.

A key having *some* producer somewhere is not the same as a route being runnable, so the route
profiles are executed as well, each one on its own:

- `contract-route-unsatisfied` — a profile reaches a stage without a required key or without any
  key of a one-of group, or supplies an input no stage on that route accepts from outside.
- `generation-stage-missing-spend-gate` — a stage that can call a voice, music, image or video
  generator lacks `paid_generation_approved_by` as its execution gate.
- `interactive-route-state-loss` — a branching profile reaches a stage that does not read
  `branch_map`, so the piece could be flattened without breaking any contract.
- `root-route-profile-drift` — the root shortcut table and this file disagree about which profiles
  exist, or the `project.yaml` example names phases its own profile does not run.

the source package's build tools then dry-runs every profile against the product behaviour it promises —
its terminal artifact, the phases it must not invoke, and the null/approved spend transition —
and calls no generator.

**Its teeth are a deliberately broken fixture**, not a `--against` run on an older copy of the package. The frozen baseline has
no contract table at all, so the check reads nothing there and returns zero — which is blindness, and
would look exactly like a pass. the source package's build tools plants a stage that reads a key nobody
writes, on every run. This is the same trap `template-token-unexpanded` and `kelvin-source-no-value`
documented.

## 4. What this file does not do

**It does not decide anything.** Every value in §1 is produced by a phase doing its craft; this file
says where the value is kept and who may change it afterwards. A key here is a shelf for an answer,
never the answer.

**It is not a schedule.** The row order is the dependency order, which is usually also the running
order, but a route that skips a phase skips its row: an audio-only piece never writes `shot_table`,
and the contract of a phase that does not run is not a claim about that project.

**And it does not replace the markers.** A value that still needs confirming after the brief, the
skill and the web have been tried is a marker, and travels with the handoff as a note
([`ENGINE-CHECK.md`](./ENGINE-CHECK.md) §3). The choice made meanwhile lives here — a run chooses rather
than waits. The difference matters: a marker is a visible note, and this file is the record of what
was chosen.
