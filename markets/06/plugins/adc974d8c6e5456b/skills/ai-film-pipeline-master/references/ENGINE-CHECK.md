# ENGINE-CHECK — the dated model record

Phases 5, 6, 7 and 8 all ask for the same thing before they will write a resolution, a clip length, a
piece of provider syntax: a **dated model record** for the engine this project is actually going to
use. This file is where that record is made. It is the only place in the package that is allowed to
carry a model's numbers, and it is deliberately short, because it is meant to be refilled rather
than read.

**Why it is not written into the craft files.** Engine limits move every few months. A resolution
baked into a prompt guide is correct for one season and quietly wrong afterwards, and the failure is
invisible — the prompt still looks right. So the guides describe the shot, and this file describes
the machine, and the two meet once, at the top of a project.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. When to run it](#1-when-to-run-it)
- [2. The record](#2-the-record)
- [3. What happens when the record is missing](#3-what-happens-when-the-record-is-missing)
- [4. The rule that governs all of this](#4-the-rule-that-governs-all-of-this)
- [5. Provider syntax lives here too, dated](#5-provider-syntax-lives-here-too-dated)
- [6. Where this file is referenced](#6-where-this-file-is-referenced)
- [7. Adapters on file](#7-adapters-on-file)

<!-- /GENERATED:toc -->

## 1. When to run it

At the start of a project, before the first prompt is compiled. It takes a few minutes: open the
engine's own current documentation or its interface, read what it offers today, and write the row.

**Filling this record is the engine-selection step the guides name:** choosing the engine and writing
its row, including the fields the guides read from it (`prompt_family`, `clip_duration_mode`,
`clip_range_seconds` or `clip_durations_allowed`). Where the brief names no engine, the agent chooses the most
suitable one (§3) — nobody is waited for — and a cell reads `pending_engine_check` only when no search
can fill it.

**A row older than about ninety days is a memory, not a record** — or sooner, where the package card for that engine gives a shorter Shelf life. Refill it rather than trusting it.
This is not caution for its own sake — the whole reason the record is dated is that the date is the
part that expires.

**Where the vendor's own pages cannot be read** — no browsing on this run — the package card's date
does not become the project's check. Copy the package card's figures into the project record, write
`checked on: from the package card dated <date>, not rechecked`, and use them: the row is usable, and
the note travels with the handoff until the vendor's pages can be read.

---

## 2. The record

Copy this block into the project folder and fill it. One block per engine the project will call.

```
ENGINE RECORD
  checked on:            YYYY-MM-DD
  checked by:            (name, or the interface/doc page you read)
  engine and version:    
  what it is used for:   (stills / motion / voice / music / sound effects / lip-sync /
                          upscale — and which shots, lines or cues)

  native generation tiles, by aspect:
    16:9    ____ x ____
    9:16    ____ x ____
    1:1     ____ x ____
    other   ____ x ____   (aspect: ______)

  maximum clip length:   ____ s          (motion engines only)
  clip_duration_mode:    flexible / fixed_set   (motion engines only)
    clip_range_seconds:      [____, ____]  (flexible)
    clip_durations_allowed:  [____, ...]   (fixed_set)
  frame rate offered:    ____ fps
  start frame accepted:  yes / no
  end frame accepted:    yes / no        — and at which resolutions: ______
  generates native audio: yes / no       (motion engines only)
    - speech:            yes / no        — and which languages, if it speaks
    - ambience and SFX:  yes / no
  prompt length limit:   ____ characters
  identity reference:    none / image / trained identity
  references per call:   ____
  prompt_family:         natural_prose / keyword_mix / dual_encoder / typographic   (image engines)

  cost per run, and on which route:      
  unlimited tier applies on this route:  yes / no / not applicable
```

### The spend authorisation, which is not an engine fact

Law 6 of [`how-to-write-a-video-prompt.md`](phase-08-video-prompt-engineering/how-to-write-a-video-prompt.md)
says *`paid_generation_approved_by` null means nothing generates, including one sample to check the
settings* — **and until September 2026 that field existed in no other line of this package.** Nothing
created it, nothing carried it, and nothing said who fills it, so the law rested on a value that had
no source. It is a project fact rather than an engine fact, which is why it sits beside the record
rather than inside it:

```
  paid_generation_approved_by:   (who authorised spend, and on what date)
  approved for:                  (stills only / stills and motion / a named batch)
  approved ceiling:              (runs, or a figure, or "no ceiling stated")
```

**Empty is the correct state until somebody fills it, and empty means nothing generates.** It is not a
marker and does not close two ways: a missing engine value leaves a `pending_engine_check` cell and
the work continues, because writing a prompt costs nothing. This one gates *spend*, so an unfilled
cell is a stop rather than a note — one of the three waits in root `SKILL.md` §0, and the only one on
spend, named in
[`phase-01-story-generation/HOW-PHASE-1-WORKS.md`](phase-01-story-generation/HOW-PHASE-1-WORKS.md) §4.
The operating mode chosen at intake says what the project *intends* to spend; this line is the
authorisation itself, and a test generation is a generation.

**Some material is not generated at all, and the record says so rather than staying blank.** Where a deliverable uses captured footage, a recorded interview, archive or a library track, write
`engine: none - captured` on its row with one line saying what it is and who holds it. **And where a deliverable is *built* rather than captured or generated** — a chart, a map, a counter, a title sequence assembled from values and type — write `engine: none - built`, because that shot needs no image engine at all and sending it to one produces an invented chart. A blank row and a row for something nobody is generating look identical otherwise, and the second is a fact worth carrying: it is the material no prompt will ever fix.

```
  PROJECTED DISPLAY FIELDS
  surface and size:        ____ (wall, screen, building; metres)
  projector brightness:    ____ lumens        room light: dimmable / fixed / daylight
  surface colour and texture: ____           (a white wall is not a screen)
  viewing distance:        ____ m
```

```
  SELF-LIT SCREEN FIELDS   (a monitor, a kiosk, a touchscreen, a video wall)
  screen size and orientation: ____ (diagonal; portrait / landscape)
  brightness:              ____ nits        ambient light: gallery / daylight / dim
  finish:                  matte / glossy   (glossy reflects the room and the viewer)
  mount height to screen centre: ____ m
  viewing distance:        ____ m           touch: yes / no
```

**A self-lit screen is not a projection and not a phone.** It makes its own black, so the projection grade does not apply and would flatten it; but it is read in room light at a fixed distance, which the phone rules do not cover. A glossy screen in a lit gallery loses its darkest third to reflections of the room, and a touchscreen carries fingerprints across whatever is in the lower half of the frame — both are composition constraints, not cleaning problems.

**Fill this wherever the piece is projected**, because a projector cannot make black — the darkest part of the image is whatever the wall already is, and in any ambient light that is a mid grey. The craft answer is `print.projection_grade`; these are the numbers it needs. Without them the two darkest passages of a piece arrive as flat rectangles and nobody reports it as a fault.

### RENDER MODE SET

Every value the render-mode field takes, and what each one means. **This table is the
authority**; the phases that ask for a render mode carry a generated copy of it, so
widening a definition here widens it everywhere rather than in one file out of seven.

| Value | What it means |
| :--- | :--- |
| `photoreal` | Made to read as photographed. Real optical values: focal length, aperture, depth of field, Kelvin, and a film stock or sensor look where one is wanted. |
| `rendered_cg` | 3D / rendered CG: rendered geometry with a virtual camera, so the optical values apply — but no film gate, so grain is an added effect rather than a property. State the **surface** as well as the optics: what the thing is made of. |
| `flat_2d` | Flat 2D / cel: drawn or painted: cel, ink, watercolour, gouache, a painterly animated look. No lens, no aperture, no Kelvin, no stock. The art style, line weight, ink and colour treatment replace them, and the light direction and palette temperature are stated in words. |
| `stop_motion` | Stop motion / physically made: photographed objects moved frame by frame. Real optics, handmade surface, and a motion signature of its own — uneven cadence, held extremes, no true motion blur. |
| `built` | **Assembled in a graphics or motion layer rather than generated at all** — a chart, map, counter or diagram built from real values; an animated diagram; **a typographic or kinetic-text sequence**; a title card. It reaches no image or video engine, carries no optical values and no art style, and a prompt written for it returns plausible nonsense. Where a shot is `built`, the engine record reads `engine: none - built`. |
| `multi_look` | Two or more looks: the piece deliberately alternates. Declare each constituent look by its machine value, say what the cut between them means, and tag every row and every prompt with the one it is in. |

The first column is a machine value, not display prose. `project.yaml`, tables and handoffs carry
exactly one of those six values. Human labels such as "rendered CG" or "flat 2D / cel" belong in
descriptions; they are never alternate spellings of the stored value. A `multi_look` project also
records the constituent values under `looks` rather than inventing a seventh combined spelling.

**An edit-layer overlay is not a look.** Captions, a logo, or an end card laid over or after the last
shot are recorded as `built` elements of the edit, not as a second look, so they do not make a piece
`multi_look`. `multi_look` is for shots whose whole picture alternates.

**Captured and generated material in one register is not a second look either.** Museum photographs
cut against generated photoreal reconstructions are `photoreal`, single look; each row carries its
source (captured / generated / built) beside it, and `engine: none - captured` covers the photographs.
**A brief that no value fits** — a drawn character composited into a photographed shop in the same
shot — takes the nearest value (here `multi_look`, both constituents under `looks`, the composite
described in words on each row) and records the choice under `decisions`. There is no seventh value
and no dead end.

**The three audio lines are in the picture block on purpose**, because they are a property of the
*video* engine: some generate speech and ambience with the picture and some return silence.
`how-to-write-a-video-prompt.md` §4.8b reads them before the first video prompt is written, and calls
that the most expensive decision in the phase — it cannot be revisited part-way through a batch. They
are not the same thing as the audio block below, which describes a separate voice, music or lip-sync
engine.

**The picture fields above are blank on an audio engine, and that is correct — leave them blank
rather than writing `n/a` into every line.** A voice, music, sound-effects or lip-sync engine fills
the header lines and then this block instead:

```
  AUDIO / LIP-SYNC FIELDS
  languages offered:       (and which of them the project actually needs)
  voices available:        (library / cloned / designed — a clone of a real person waits for
                            that person's recorded consent; a real child's, for the parent's)
  maximum characters or seconds per call:   ____
  output format and sample rate:            ____
  pronunciation control:   none / phonemes / tags / a lexicon you can supply
  can it hold one voice consistent across separate calls:  yes / no / with what
  music:                   a music engine fills the SONG ENGINE RECORD below instead
  lip-sync: what it drives (a still / an existing clip / generated motion):  ____
  lip-sync: languages it is trained on, and whether yours is one:  ____
  lip-sync: maximum take length:   ____ s
```

**A music engine fills this record**, because what it returns, and at what length, decides the
Phase 5 timing map; `phase-05-song-generation/HOW-PHASE-5-WORKS.md` (*The Song Engine Record*) says
why, and what to do while it is unfilled.

```
SONG ENGINE RECORD
  checked on:            YYYY-MM-DD
  checked by:            (name, or the interface/doc page you read)
  engine and version:    
  what it is used for:   (full song / instrumental bed / stems only / score cue)
  plan and whose account: ______   (on client work, the client's plan; the owner's plan is never assumed)

  maximum length returned in one generation:   ____ (m:ss)
  can it end rather than fade:                 yes / no
  can it extend or continue a track:           yes / no
    if yes, maximum total length:              ____ (m:ss)
    and does the seam land on a bar line:      yes / no / not stated
  takes returned per run:                      ____
  lyric input limit:                           ____ (characters, or sections)
  structural metatags honoured:                yes / partly / no — which: ______
  instrumental-only supported:                 yes / no
  stems returned:                              none / ____ stems — which: ______
  file format and sample rate returned:        ______
  languages or scripts confirmed working:      ______

  cost per run, and on which route:            
  unlimited tier applies on this route:        yes / no / not applicable
```

**A deliverable that ends on paper fills this block instead**, because none of the fields above
describe it and the ones that do are not properties of the engine at all:

```
  PRINT / PHYSICAL FIELDS
  final trim size:         ____ x ____ mm   (A1 is 594 x 841; the A series is 1:1.4142)
  viewing distance:        ____ m           (it decides the type size, not the paper size)
  resolution at final size: ____ ppi        (300 ppi at A1 is 7016 x 9933 px; large-format
                                             work read from metres away takes far less)
  colour space and profile: ____            (CMYK for offset, and which profile)
  bleed / trim / safe margin: ____ mm       (3 mm bleed is typical; the safe margin on a
                                             poster is set by the viewing distance, not by
                                             a book's inner margin)
  stock and finish:        ____
  how the pixels get there: generate natively at the nearest offered tile, then upscale
                            by ____ x in a dedicated pass — never by cropping a wider frame
```

**No image engine offers an A-series tile, and that is not a limit to design around.** The rule
everywhere else in this package is *a limit is a reason to change the engine, not the shot* — here
there is no other engine, because the constraint is a paper size and not a model. So the shot does
not shrink: generate at the engine's nearest native ratio with the composition built for the A-series
crop, then enlarge in a dedicated upscale pass to the pixel dimensions the trim size and viewing
distance require. `print.resolution_at_size` owns that arithmetic; this record is where the project's
actual numbers go.

**Why the lip-sync lines are their own class.** On a piece where a character speaks on camera, to the
lens or inside a scene, the
lip-sync engine is the one that decides the shape of the production: whether a take can run 45
seconds or has to be cut at 10, whether the mouth is driven from the generated video or the video is
generated from the mouth, and whether it has ever seen the language being spoken. That is a
structural question, not a finishing one, and answering it after the shot list is written is the
wrong order. **Singing on camera counts:** a music video whose characters sing in frame reads this
block at intake, before Phase 3, exactly as a dialogue piece does.

**On the last two lines.** Where an unlimited tier exists it is usually attached to the account, not
to the model, and calling the same model through a different route — an API instead of the
interface, a wrapper instead of the account — can draw credits instead. Confirm the route the run
will actually use, not the route the plan assumed.

---

## 3. What happens when the record is missing

**Fill it, and keep going.** The engine is the one the brief names; where the brief names none, the
agent picks the most suitable current engine for the job, searches its own pages on the web today, and
writes the values it finds — resolution, clip length, frame rate, take length, reference count. The
choice and the date go under `decisions`. The prompt is written in full either way.

Only a value that no search can give stays marked `pending_engine_check`, so whoever renders sees it.
That is a note that travels with the handoff, never a stop.

### The rest of the marker set, and why it is a set

**Every marker is a note, never a stop.** A marker is written only after the working rule in the
root `SKILL.md` §0 has run — the brief, the skill, the web, the most suitable choice — and something
still has to be confirmed by whoever delivers. The work continues around it. The set:

| Marker | Stands in for | Owned by |
| :--- | :--- | :--- |
| `pending_engine_check` | a resolution, a clip length, a take length, a voice limit | this file |
| `pending_forbidden_global` | the project's standing prohibitions | [`FORBIDDEN-GLOBAL.md`](FORBIDDEN-GLOBAL.md) |
| `pending_measured_duration` | a runtime that is not yet measured — whether it is waiting on a render, or on a recording of speech nobody wrote | the render or the recording, once it exists |
| `pending_quote_source` | the publication a quoted ancient line comes from, on a history piece the user wants realistic | the search; the closest attested wording is used meanwhile |
| `pending_archive_source` | where a piece of found material came from, when a search has not found it | a note for the caption and the credit; the material is used meanwhile |
| `pending_figure_source` | the publication a figure stated as fact comes from, on a history piece the user wants realistic or a factual piece | the search; the closest supported figure is used meanwhile |
| `pending_reference_image` | the visual reference a historical element is supposed to be built from | the search; none found, the element is generated from the closest thing and noted |
| `pending_language_check` | a line in a language nobody on the project reads — including one invented for the piece | a native reader, whenever one sees it; for a constructed language, whoever wrote its rules — a note, never a wait |
| `pending_pronunciation_source` | the spoken form of a name that no named source or native speaker has yet supplied — a respelling that would otherwise be guessed | the named source or native speaker `pronounce.mesopotamian_names` asks for, once someone finds one; the best-supported respelling is used meanwhile |
| `pending_permission` | a real person's consent before their voice or likeness is cloned — for a real child, the parent's (root `SKILL.md` §0) | that person or parent; only the cloning step waits, and nothing else in the project |
| `pending_keyframe_render` | a clip prompt written, in prompts-only mode, against an approved keyframe *prompt* whose still has not been rendered yet | the still, once rendered and checked against its approved prompt |
| `pending_measured_figure` | a number that has to be measured, sampled or counted *for this film*, because no published source holds it | whoever does the measuring, and it is budgeted like a shoot day |
| `pending_supplied_spec` | the official file for something the brief's owner holds — a brand identity, an attested figure, a required line | the closest public version is used meanwhile (the brand's own site, the brief); the official file replaces it when it arrives |
| `pending_photosensitivity_check` | whether a deliberate strobe or rapid flash sequence is safe to show — a measurement this package does not make. Ordinary light (fire, candles, lamps, a sunset, a flickering bulb in a scene) never takes it | whoever delivers, measuring against the standard the destination enforces; the rule is `safety.photosensitive_flash` |

**`pending_figure_source` and `pending_measured_figure` are not the same marker.** The first says the number exists and someone must go and cite it; the second says the number does not exist yet and someone must go and *produce* it. Filing the second as the first is worse than leaving it blank, because the handoff then looks like a morning in an archive when it is actually a sampling run with a cost and a lead time. The same distinction separates it from `pending_supplied_spec`, which is for a thing that already exists in somebody else's hands.

**Every marker has two closing states, not one.** The obvious one is **resolved** — the answer
arrived. The other is **closed as unobtainable**, and it is just as finished: nobody can supply this,
here is what was done instead. Write it as `pending_x: unobtainable — <why>, <what was done>`.

Without the second state a marker can be *permanently* open, and a permanently open marker is
indistinguishable in a handoff from one nobody has got to yet — which inverts the whole point of the
system, since the point is that a gap is visible rather than silent. Each of these has a real case
with no possible answer, and each of them closes:

| Marker | The case with no answer | What closing it looks like |
| :--- | :--- | :--- |
| `pending_permission` | the person cannot be asked — they have died, or cannot be reached | the voice or likeness is not cloned; a designed voice or a non-identifying likeness is made instead, and the piece carries on |
| `pending_archive_source` | a genuine orphan work: there is nobody left to ask | the search, written down, and the material used with what is known of it |
| `pending_reference_image` | an object attested only in a text, or destroyed | what the reconstruction was built from instead, and the fact that it is a reconstruction |
| `pending_quote_source`, `pending_figure_source` | the claim has no traceable source at all | **that finding, stated on screen.** "The figure comes from the ministry and has never been traced to a count" is better television than the number was. |
| `pending_language_check` | a constructed language, no native reader | whoever wrote the language's rules checked the line against them |
| `pending_photosensitivity_check` | no analyser, no adviser, no budget to reach either | the note travels with the handoff to whoever delivers, who measures before release; this package writes the sequence as designed and writes no threshold (root `SKILL.md` §0) |

**"Unobtainable" is a finding, not a failure.** In the evidence rows above, what closes the marker
is worth more than what it was waiting for — and the one thing that is never acceptable is deleting
the marker because it could not be resolved. **The flash row is handed on rather than closed here:**
the measurement is made by whoever delivers, before release, because this package writes no
brightness or rate threshold (root `SKILL.md` §0).

**The table is the list, and no count is written above it.** The sentence introducing it used to say
*"there are three"*, and stayed at three when a fourth marker was added — which is the same defect
this file exists to prevent, one level up. A number is not written where a list can be counted.

**`pending_measured_duration` covers two different unknowns, and the second is easy to miss.** The first is a runtime waiting on a render: the words exist, the arithmetic gives an estimate, and the file will replace it. The second is a runtime waiting on a **recording of speech nobody wrote** — an interview answer, a piece of testimony, anything captured rather than scripted. There is no estimate to replace there, because there is no script to count, and the cell is marked from the start rather than filled with a guess dressed as a plan. Write the intended *shape* — 'roughly two minutes, three answers' — beside the marker, so the shot table has something to hold, and treat the number as absent until the tape exists.

It exists at all because every timing rule in the package says the same thing —
the duration comes from the rendered audio, measured, and the word count is only a planning estimate
— and until that file exists there was no honest way to write the cell. A number written from
arithmetic and a number measured off a waveform look identical on the page and routinely differ by
several minutes: one test run estimated 2,604 words and the machine counted 3,936, turning a
22-minute episode into 31:29 without anything on the page looking wrong. So a timecode derived from
arithmetic is written **with the marker beside it** — `04:12 pending_measured_duration` — and the
marker is cleared when the render replaces the estimate. Every provisional timecode in a shot table
carries it, which is also why the first pass of that table is labelled provisional. When every row is
provisional, the marker may be written once in the table header instead of beside each timecode, and
it comes off the header only when the whole table is measured.

**`pending_quote_source`** applies on a history piece the user wants realistic. A piece that puts an
ancient line in a mouth — a tablet, a letter, an inscription — searches for the real line first: the
skill, then the web. Found, it is used with its publication beside it. Not found, the closest attested
wording is written, marked `pending_quote_source`, and the piece carries on; the mark tells whoever
delivers that the wording is the closest found rather than a verified quotation. The line is never
cut for want of a source, and on any other piece the marker is not used at all.

**`pending_archive_source`** is for material the project did not make: archive footage, a photograph, a scanned document, a library track, a recording of someone else's performance. What matters for the piece is **where it is from** — for the caption, the date on screen and the credit. Search for it, **write what you do know beside it** — the collection, the catalogue number, the approximate date — because a partly identified item is findable and an unlabelled one is not, and use the material either way. The marker is a note for the credit, never a reason to leave the material out, and it carries no licence question (root `SKILL.md` §0).

**`pending_figure_source`** is the quotation marker applied to numbers, and it applies where the piece states a figure as fact on a history piece the user wants realistic, or on a factual piece the brief wants checked. Search for the figure's source: found, cite it; not found, use the closest supported figure and mark it. **A number that sits on screen for four seconds in silence is the one most worth that search**, which is what the run that produced this row found. On any other piece a figure is the brief's or the writer's and carries no marker.

**`pending_reference_image`** exists because the heritage rules generate a historical element from a real reference on a history piece the user wants realistic. Search the canon, then the web: a reference found is used; none found, the element is generated from the closest thing, and the marker notes what the reference should have shown — the garment, the object, the building, the pose. It never holds a prompt back.

**`pending_language_check`** is the one that catches what nobody else can. A line written in a language the team does not read looks exactly as convincing when it is wrong: a test run's first draft had **three of ten Sureth numerals wrong** and nothing in the package would have found it. Every line of non-English dialogue, lyric, on-screen text or transliteration carries this marker as a note until a native reader has seen it — the line is written in the language and dialect the brief asked for, and nothing waits for the reader — and *seen it set*, in the font, at the size it will appear, because a script can be correct in a document and broken in a render. **A constructed language has no native reader, and the marker still closes:** what clears it is the person who wrote the language's rules checking the line against them — its sounds, its spelling, whether it uses letters the real tongue it gestures at never had. Write those rules down before the first line is spoken, because a marker with no possible clearing condition is a design fault rather than a standing warning, and the failure it is there to catch — the invented language drifting between shots — happens anyway.

**`pending_permission`** covers one thing: a real person's consent before their voice or likeness is cloned — for a real child, the parent's or guardian's, recorded in `child_voice_clone_consent`. It is the only marker that holds a step, and the step it holds is the cloning; every other part of the project carries on. This skill has no other permission, rights or licence step (root `SKILL.md` §0).

**A figure the canon states is used as the canon states it.** Where the canon entry carries a
publication citation, that citation is the source, and citing it closes `pending_figure_source` on a
history piece the user wants realistic. Where it carries none, the figure is still used — it is the
house's settled answer — and on a realistic history piece a quick search for the publication behind
it is worth making: a source found is cited, and none found is noted, never a stop. The corrective
shape (*"it is this, not that"*) reads as already checked, which is why that note is worth writing.

**`pending_supplied_spec`** covers what someone else owes you: a brand's identity rules with its clear space and minimum size, an audited figure, an approved legal line. It is not research and it is not an engine limit — it is a thing that exists, in someone else's hands. The piece is finished with the closest public version, and the official file replaces it when it arrives.

All of them work the same way and for the same reason: **a missing input never stops the work.** It is
searched, the most suitable answer is chosen and recorded, and a mark travels only where that choice
still needs confirming.

This is a change from how the guides used to read. They said compilation *stops* when the record is
missing, which meant the package could not finish a single prompt on its own — a prompt-only brief,
which is most briefs, had no way through. Stopping protected against a guessed number and cost
everything else. The marker protects against the same guess and costs nothing.

---

## 4. The rule that governs all of this

**A limit is a reason to change the engine, not the shot.**

If the record comes back and the engine cannot hold a ten-second continuous move, or cannot take an
end frame at the resolution the piece needs, or loses the face by the third clip — that is a fact
about the engine. It is not a fact about the shot, and the shot does not shrink to fit it. Find the
engine that can do it, or split the move across two generated keyframes; where neither is possible,
choose the nearest the engine can do and record the choice under `decisions`. What must never happen is a piece quietly designed downward around a machine, because nobody
downstream can see the shot that was never written.

The same holds for a limit that has *lifted*. A shot avoided last year because the engine could not
hold it may be available now, and the only way to find that out is to check rather than remember.

---

## 5. Provider syntax lives here too, dated

The prompt phases write the shot in plain description, on purpose — a prompt built around one
provider's keywords is worth nothing the day the project moves. Where an engine needs its own
wording, that wording is an adapter, and it belongs in this file beside the record that dates it:

```
ADAPTER — <engine>, checked YYYY-MM-DD
  parameter style:        (flags / JSON / plain prose / other)
  negative prompt:        supported / not supported — how it is passed: ______
  motion or camera terms: the engine's own vocabulary, if it has one
  seed:                   how it is set
  known quirks:           (one line each, only what was observed)
```

The prompt is written once, for the shot. The adapter is what dresses it for a particular engine on
a particular day, and it is the part that is expected to go stale.

---

## 6. Where this file is referenced

- `phase-05-song-generation/HOW-PHASE-5-WORKS.md` — the song engine record: what the engine returns,
  at what length, and whether it gives stems. The block is in §2 above; HOW-5 says why Phase 5 needs
  it and what to do while it is unfilled.
- `phase-06-storyboard-layout/storyboard-deck-template.md` — generator choice for the deck
- `phase-07-image-prompt-engineering/HOW-PHASE-7-WORKS.md` — law 7, native tile
- `phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md` — law 7, the owned-inputs
  table, and the resolution table
- `phase-08-video-prompt-engineering/how-to-write-a-video-prompt.md` — owned inputs, clip ceiling,
  seed and parameter ownership

If a guide sends you here and the record for this project does not exist yet, §1 is a ten-minute
job. If nobody can run it right now, §3 is the way through.

---

## 7. Adapters on file

The adapters §5 describes, filled for the engines the package's own engine shelves were written for. **Each was checked against the vendor's own pages on the date in its heading, and each is expected to go stale**: a project refills the one it uses under §1 before relying on it. For ElevenLabs and the image families, the cards carry the craft in engine-neutral words and point here for the syntax. **Suno and Lyria 3.5 are the exception, by the owner's ruling of 2026-09-23**: their syntax and vendor facts live on the `suno.` and `lyria.` cards themselves, each with its official source and date, and their blocks below are dated verification records that point to those cards and restate no figure.

<!-- adapter:elevenlabs -->

### ADAPTER — ElevenLabs text-to-speech, checked 2026-09-23

Checked against the vendor's own pages on 2026-09-23. Every figure below is the vendor's and is
expected to go stale; the cards in `phase-04-audio-narration/elevenlabs-engine-craft.md` carry the
craft and point here for the syntax.

```
ADAPTER — ElevenLabs text-to-speech, checked 2026-09-23
  parameter style:        JSON over the text-to-speech API — model_id, text, voice_settings
                          {stability, similarity_boost, style, use_speaker_boost, speed}, seed,
                          previous_text / next_text, previous_request_ids / next_request_ids,
                          output_format, pronunciation-dictionary locators. The web interface
                          exposes the same settings as sliders and toggles.
  negative prompt:        not supported on text-to-speech
  motion or camera terms: none (voice engine). Its own delivery vocabulary:
                          - audio tags in square brackets, e.g. [whispers] [laughs] [sarcastic] — Eleven v3 only
                          - <break time="x.xs" /> pauses, up to 3 s — not on v3
                          - SSML phoneme tags (CMU Arpabet or IPA) — eleven_flash_v2 only
                          - inline IPA between /slashes/ — v3, 80-90% consistency
                          - alias tags through pronunciation dictionaries — up to 3 locators per request
  seed:                   seed, an integer 0 to 4294967295; "best effort to sample
                          deterministically ... Determinism is not guaranteed."
  known quirks:           style: default 0, vendor recommends keeping it at 0 at all times; above 0 is
                            "slightly less stable" and adds latency
                          use_speaker_boost: default true, boosts similarity to the original speaker,
                            effect "generally rather subtle", adds latency, not available on v3
                          similarity_boost, speaker boost and speed are not available on v3; v3's
                            stability is a Creative / Natural / Robust choice
                          speed: default 1.0, range 0.7 to 1.2
                          similarity_boost set too high on poor audio "may reproduce artifacts or
                            background noise"
                          on models without audio tags, bracketed or dialogue-tag direction "will
                            still speak out the emotional delivery guides" — cut it in post
                          too many break tags "can cause instability"; dashes and ellipses "are less
                            consistent"
                          Multilingual v2 "doesn't support phoneme tags"
                          default output_format is mp3_44100_128; PCM output is 16-bit, no 24-bit
                            option; 44.1 kHz PCM/WAV needs Pro or higher; 48 kHz PCM listed with no
                            plan restriction
                          cloning: IVC about 1-2 minutes (over 3 minutes can be detrimental); PVC at
                            least 1 hour, ideally 2-3 hours, Creator plan or higher and voice
                            verification; record at -23 to -18 dB RMS, true peak -3 dB; MP3 at
                            192 kbps or above; consent must be confirmed
                          billing: Free plan 10k credits a month, no commercial licence, no cloning;
                            Multilingual v2 1 credit per character, Flash/Turbo 0.5 to 1
```

| card id | what the card asks for | the engine's own syntax or setting | status | source URL |
| :--- | :--- | :--- | :--- | :--- |
| `elevenlabs.model_multilingual_v2` | the long-form narration model | `eleven_multilingual_v2` — "most lifelike", "most stable on long-form generations", 29 languages, 10,000 characters per request; the API default `model_id` | CONFIRMED | https://elevenlabs.io/docs/models<br>https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| `elevenlabs.model_multilingual_v2` | the most emotionally expressive model | `eleven_v3` is now the vendor's "most emotionally rich, expressive" model (70+ languages, 5,000 characters per request); the card's earlier claim that v2 was the premier emotional model | CHANGED | https://elevenlabs.io/docs/models |
| `elevenlabs.model_turbo_v2_5` | a fast, lower-cost tier for volume | `eleven_turbo_v2_5` (and `eleven_turbo_v2`) deprecated: "functionally equivalent" to `eleven_flash_v2_5`, which has lower latency; Flash recommended "in all use cases" | CHANGED | https://elevenlabs.io/docs/models |
| `elevenlabs.model_turbo_v2_5` | "three times the speed and reduced cost" | not documented by the vendor; pricing groups Flash and Turbo together at 0.5 to 1 credit per character | NOT FOUND | https://elevenlabs.io/pricing |
| `elevenlabs.model_flash_v2_5` | the lowest-latency draft model | `eleven_flash_v2_5` — "our fastest speech synthesis model", about 75 ms (model inference time only), 32 languages, 40,000 characters per request; `eleven_flash_v2` is English only | CONFIRMED | https://elevenlabs.io/docs/models |
| `elevenlabs.stability_tuning` | the range-versus-consistency control | `voice_settings.stability`, default 0.5 (interface default "50"); lower gives "broader emotional range", too low gives "overly random" delivery and a character that speaks too quickly, higher "can result in a monotonous voice". On v3 it is a Creative / Natural / Robust choice | CONFIRMED | https://elevenlabs.io/docs/api-reference/voices/settings/update<br>https://elevenlabs.io/docs/api-reference/text-to-speech/convert<br>https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech<br>https://elevenlabs.io/docs/best-practices/prompting/eleven-v3 |
| `elevenlabs.stability_tuning` | a scale and working bands (the card's earlier 0.0–1.0, 0.35–0.55, >0.75, <0.25) | not documented by the vendor; the only official figure is the default | NOT FOUND | https://elevenlabs.io/docs/api-reference/text-to-speech/convert<br>https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech |
| `elevenlabs.similarity_boost` | adherence to the original voice | `voice_settings.similarity_boost`, default 0.75 (interface "75"); set too high on poor audio it "may reproduce artifacts or background noise"; not available on v3 | CONFIRMED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert<br>https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech |
| `elevenlabs.similarity_boost` | working bands (the card's earlier 0.75–0.85, 0.65 for noisy sources) | not documented by the vendor | NOT FOUND | https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech |
| `elevenlabs.style_exaggeration` | an intensity amplifier | `voice_settings.style` "attempts to amplify the style of the original speaker" | CONFIRMED | https://elevenlabs.io/docs/api-reference/voices/settings/update |
| `elevenlabs.style_exaggeration` | a working band (the card's earlier 0.10–0.30, >0.40 destabilises) | default 0; the vendor recommends "keeping this setting at 0 at all times"; any value above 0 makes the model "slightly less stable" and adds latency | CHANGED | https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech<br>https://elevenlabs.io/docs/api-reference/voices/settings/update |
| `elevenlabs.speaker_boost` | a toggle toward the original speaker | `voice_settings.use_speaker_boost`, default true | CONFIRMED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| `elevenlabs.speaker_boost` | what the toggle does (the card's earlier presence and crispness claim) | "boosts the similarity to the original speaker"; the effect is "generally rather subtle", it adds latency, and it is not available on v3 | CHANGED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert<br>https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech |
| `elevenlabs.voice_cloning_hygiene` | the cloning tiers, a reverb-free sample, and consent | Instant Voice Cloning and Professional Voice Cloning; reverb-free confirmed; the user must "confirm that you have the right and consent", and PVC also needs voice verification | CONFIRMED | https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning<br>https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning |
| `elevenlabs.voice_cloning_hygiene` | sample length (the card's earlier 1 to 5 minutes) | IVC "Approximately 1-2 minutes"; over 3 minutes gives "little improvement" and can be "detrimental". PVC "at least an hour", ideally about three hours; PVC needs the Creator plan or higher | CHANGED | https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning<br>https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning<br>https://elevenlabs.io/pricing |
| `elevenlabs.voice_cloning_hygiene` | sample level (the card's earlier -16 LUFS) | "between -23 dB and -18 dB RMS with a true peak of -3 dB" | CHANGED | https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning<br>https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning |
| `elevenlabs.voice_cloning_hygiene` | sample file format (the card's earlier 24-bit 48kHz WAV) | "We strongly recommend MP3 at 192kbps or above"; recording quality matters more than codec | CHANGED | https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/instant-voice-cloning<br>https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning/professional-voice-cloning |
| `elevenlabs.prompt_tags_emotion` | inline delivery direction | audio tags in square brackets such as `[whispers]`, `[laughs]`, `[sarcastic]` are an Eleven v3 feature only. On other models emotion comes from narrative context or dialogue tags, and "the model will still speak out the emotional delivery guides" — remove them in post. The card's earlier claim that Multilingual v2 reads bracket tags | CHANGED | https://elevenlabs.io/docs/best-practices/prompting/controls<br>https://elevenlabs.io/docs/best-practices/prompting/eleven-v3 |
| `elevenlabs.prompt_tags_pacing` | a pause of exact length | `<break time="x.xs" />`, up to 3 seconds; not supported on v3; too many break tags "can cause instability". Dashes and ellipses work but "are less consistent" | CONFIRMED | https://elevenlabs.io/docs/best-practices/prompting/controls |
| `elevenlabs.prompt_tags_pacing` | pause lengths per mark (the card's earlier 400 ms, 250 ms, 1 s) | not documented by the vendor | NOT FOUND | https://elevenlabs.io/docs/best-practices/prompting/controls |
| `elevenlabs.breath_insertion` | a breath before a line | inline bracket tags are the v3 audio-tag mechanism; on other models bracketed direction may be spoken aloud. A specific breath tag is not documented by the vendor in the pages checked. The card's earlier `[sharp intake of breath]` as a general inline tag | CHANGED | https://elevenlabs.io/docs/best-practices/prompting/controls<br>https://elevenlabs.io/docs/best-practices/prompting/eleven-v3 |
| `elevenlabs.ssml_phoneme_fallback` | phonetic respelling in the text | "try writing words more phonetically" — capital letters, dashes, apostrophes | CONFIRMED | https://elevenlabs.io/docs/best-practices/prompting/eleven-v3 |
| `elevenlabs.ssml_phoneme_fallback` | a phoneme-level override | SSML phoneme tags (CMU Arpabet or IPA) work only with `eleven_flash_v2`; Multilingual v2 "doesn't support phoneme tags"; v3 reads inline IPA between /slashes/ with 80–90% consistency; alias tags go through pronunciation dictionaries, up to 3 locators per request. The card's earlier IPA phonemes as a general fallback | CHANGED | https://elevenlabs.io/docs/best-practices/prompting/eleven-v3<br>https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| `elevenlabs.seed_locking` | a seed to pin | `seed`, an integer from 0 to 4294967295 | CONFIRMED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| `elevenlabs.seed_locking` | what pinning guarantees (the card's earlier "guarantee consistent vocal delivery") | "best effort to sample deterministically ... Determinism is not guaranteed." | CHANGED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| `elevenlabs.chunking_strategy` | neighbouring text as context | `previous_text` / `next_text` and `previous_request_ids` / `next_request_ids` (at most 3 IDs each), to "improve the speech's continuity" | CONFIRMED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert |
| `elevenlabs.chunking_strategy` | a words-per-call band (the card's earlier 40–70 words) | not documented by the vendor; the only official figures are per-request character limits: v3 5,000, Multilingual v2 10,000, Flash v2.5 40,000 | NOT FOUND | https://elevenlabs.io/docs/models |
| `elevenlabs.bitrate_and_mastering` | uncompressed output at 48 kHz | `output_format` `wav_48000` or `pcm_48000`; 48 kHz PCM is listed with no plan restriction; PCM and WAV at 44.1 kHz need the Pro plan or higher; the default is `mp3_44100_128`, so it must be overridden | CONFIRMED | https://elevenlabs.io/docs/api-reference/text-to-speech/convert<br>https://elevenlabs.io/docs/help-center/troubleshooting/what-audio-formats-do-you-support |
| `elevenlabs.bitrate_and_mastering` | 24-bit output (the card's earlier claim) | PCM output is listed as 16-bit, with no 24-bit option; the project's 24-bit delivery file is a conversion made at delivery | CHANGED | https://elevenlabs.io/docs/help-center/troubleshooting/what-audio-formats-do-you-support |
| `elevenlabs.free_vs_paid_gateway` | which calls cost credits | Free plan: 10k credits a month, no commercial licence, no cloning; Starter adds Instant Voice Cloning; Creator adds Professional Voice Cloning; Multilingual v2 costs 1 credit per character; Flash and Turbo 0.5 to 1 credit per character | CONFIRMED | https://elevenlabs.io/pricing |

**Models, as of 2026-09-23.** Current text-to-speech models: `eleven_v3` (most expressive, 70+
languages, 5,000 characters per request), `eleven_v3_conversational` (about 280 ms, 70+ languages),
`eleven_multilingual_v2` (most stable on long-form, 29 languages, 10,000 characters; the API default),
`eleven_flash_v2_5` (about 75 ms, 32 languages, 40,000 characters) and `eleven_flash_v2` (English
only). Deprecated: `eleven_turbo_v2_5` and `eleven_turbo_v2`, "functionally equivalent" to the Flash
models, which the vendor recommends "in all use cases". Sources: https://elevenlabs.io/docs/models ,
https://elevenlabs.io/docs/api-reference/text-to-speech/convert

<!-- adapter:lyria -->

### ADAPTER — Lyria 3.5 (Google), checked 2026-09-23

A dated verification record, not a fact store. Every Lyria vendor fact now lives once, on the `lyria.` card that uses it, with its official URL and the date it was read; this block records what was checked, when, against which pages, and where each fact went. It restates no figure. Re-check before a paid run and at least every 30 days (§1).

```
ADAPTER — Lyria 3.5 (Google), checked 2026-09-23
  checked on:             2026-09-23, against Google's official pages only (list below)
  model in use:           Lyria 3.5, in the Gemini app first; API, AI Studio, Flow Music and
                          Vertex AI labelled by surface on the cards
  parameter style:        plain prose, one prompt            -> lyria.semantic_natural_prompting
  negative prompt:        written in the prompt, not a field -> lyria.semantic_natural_prompting
  own vocabulary:         Lyrics:, section tags, timestamps  -> lyria.syllable_timing_sync
                          tempo in the prompt                -> lyria.controllable_tempo_curves
                          genre fusion                       -> lyria.stylistic_hybridization
                          texture and space words            -> lyria.spatial_acoustic_staging,
                                                                lyria.intimate_acoustic_proximity
  seed:                   -> lyria.api_batch_synthesis
  surfaces, models, architecture, length, limits, price, age, terms, SynthID
                          -> lyria.foundational_architecture
  inputs (image, video, audio by surface)
                          -> lyria.conditioning_audio_input
  stems                   -> lyria.native_multitrack_stems
  output files and formats -> lyria.high_res_broadcast_delivery
  extend / continue        -> lyria.dynamic_energy_progression
  languages, Arabic        -> lyria.syllable_timing_sync
  maqam vocabulary         -> lyria.qasida_orchestration
  microtones               -> score.microtonal_quarter_tone_tension
  key change at a time     -> score.harmonic_modulation_pivot
  one melody, variations   -> score.thematic_variation_acts
  known quirks:           where Google's own pages disagree, both are written on the card with
                          their URLs (the model card vs the launch blog on surfaces; guide vs
                          model page on WAV; Help vs overview on video input; Vertex vs AI
                          Studio on the Lyria 3 Pro sample rate; the Vertex prompt guide vs the
                          Lyria 3 spec on negative prompts)
```

| Checked | Where the fact now lives | Status on 2026-09-23 |
|---|---|---|
| model name, architecture, surfaces and channels, launch dates, Gemini app steps, lengths per surface, plan limits, price, age and account, rights, SynthID, RealTime fields | `lyria.foundational_architecture` | CHANGED: now Lyria 3.5 by name, Gemini app first |
| prompt formula, keyword lists, short vs detailed prompts, exclusions, negative-prompt status | `lyria.semantic_natural_prompting` | CHANGED |
| audio, image and video input by surface | `lyria.conditioning_audio_input` | CHANGED: Flow Music takes audio |
| stems | `lyria.native_multitrack_stems` | CONFIRMED: none |
| genre fusion | `lyria.stylistic_hybridization` | CONFIRMED |
| lyrics syntax, timestamps, intensity, languages, Arabic | `lyria.syllable_timing_sync` | CHANGED: Arabic beta on Lyria 3; on 3.5 not documented by Google, works in the Gemini app by the owner's test (2026-09-23) |
| tempo written in the prompt; tempo curve | `lyria.controllable_tempo_curves` | CONFIRMED (fixed tempo); curve NOT FOUND |
| space and decay | `lyria.spatial_acoustic_staging` | NOT FOUND (figures); texture words CONFIRMED |
| crescendo, extend | `lyria.dynamic_energy_progression` | CONFIRMED; extend in Flow Music only |
| output formats, sample rates, bit depth | `lyria.high_res_broadcast_delivery` | CHANGED |
| close, dry texture | `lyria.intimate_acoustic_proximity` | CONFIRMED |
| maqam and Arabic percussion vocabulary | `lyria.qasida_orchestration` | NOT FOUND |
| tempo in a choral prompt | `lyria.battle_choral_invocations` | pointer to `lyria.controllable_tempo_curves` |
| batch, flex, priority, seed, repeat runs | `lyria.api_batch_synthesis` | CHANGED |
| microtones | `score.microtonal_quarter_tone_tension` | NOT FOUND |
| key change at a timestamp | `score.harmonic_modulation_pivot` | NOT FOUND |
| melody reuse across variations | `score.thematic_variation_acts` | CHANGED: Flow Music Remix route added |
| key and instrumental in a drone prompt | `score.minimalist_suspense_drone` | pointer to `lyria.semantic_natural_prompting` |

**Sources read 2026-09-23:**
- https://blog.google/innovation-and-ai/products/gemini-app/better-tracks-lyria-gemini/
- https://blog.google/innovation-and-ai/models-and-research/google-labs/lyria-3-5/
- https://gemini.google/overview/music-generation/
- https://support.google.com/gemini/answer/16901237
- https://support.google.com/gemini/answer/16275805
- https://ai.google.dev/gemini-api/docs/music-generation
- https://ai.google.dev/gemini-api/docs/lyria-prompt-guide
- https://ai.google.dev/gemini-api/docs/models/lyria-3.5
- https://ai.google.dev/gemini-api/docs/models/lyria-3-pro-preview
- https://ai.google.dev/gemini-api/docs/changelog
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/realtime-music-generation
- https://support.google.com/flow/answer/17084348
- https://deepmind.google/models/lyria/
- https://deepmind.google/models/model-cards/lyria-3-5/
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-002
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/lyria-music-generation
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/music/music-gen-prompt-guide
- https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-lyria-3-pro
- https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/
- https://blog.google/products-and-platforms/products/gemini/tips-prompting-lyria-3/
- https://blog.google/innovation-and-ai/technology/ai/lyria-3-pro/
- https://blog.google/intl/en-mena/product-updates/explore-get-answers/lyria-3-arabic-google-gemini-ramadan/
- https://policies.google.com/terms
- https://policies.google.com/terms/generative-ai/use-policy

<!-- adapter:suno -->

### ADAPTER — Suno, checked 2026-09-23

This is a verification record, not a copy of the facts. Suno's syntax and vendor facts now live on the `suno.` cards in `phase-05-song-generation/suno-engine-craft.md` and on the Suno part of `song_handoff.stem_separation_protocol`. Each fact there carries its official URL and the date it was read. This block says what was checked, when, against which pages, and which card holds each answer. It restates no figure. A project re-checks the cards it relies on under §1 before a paid run.

```
ADAPTER — Suno, checked 2026-09-23
  checked on:             2026-09-23, against Suno's official pages only (suno.com, help.suno.com,
                          suno.com/blog, suno.com/release-notes, suno.com/terms, suno.com/pricing)
  parameter style:        plain prose in fields  -> suno.style_prompt_formula
  negative prompt:        supported, own field   -> suno.negative_style_tags
  engine vocabulary:      documented section tags -> suno.structural_metatags
                          community tags (not documented by Suno) are labelled on each card
                          that uses them
  seed:                   not documented         -> suno.reroll_variation_control
  known quirks:           see the pointer table below; none observed on a run
```

| What was checked | Where the answer lives now |
|---|---|
| Current models, retirement of every pre-v6 model, plan access, Max Mode, model picker | `suno.v6_engine_architecture`, `suno.v55_fast_iteration` |
| Download formats, download quotas, Studio export, rights on Free and paid plans | `suno.v6_engine_architecture` |
| Custom Mode and Simple Mode fields, Style Influence, field character limits | `suno.style_prompt_formula` |
| Exclude field | `suno.negative_style_tags` |
| Documented structure tags, glossary structure terms, Song Editor sections | `suno.structural_metatags` |
| Chorus-lift, solo, drop, ending, whisper, casting, call-and-response and battle tags (community practice) | `suno.dynamic_energy_chorus`, `suno.instrumental_solo_tags`, `suno.drop_and_bass_impact`, `suno.outro_and_ending_tags`, `suno.whispered_vocal_directing`, `suno.vocal_arrangement_tags`, `suno.call_and_response_tags`, `suno.guttural_battle_directing` |
| Vocal Gender control and glossary vocal-technique words | `suno.vocal_arrangement_tags` |
| Maximum length per generation, Extend, Replace Section, Song Editor | `suno.extension_continuity` |
| Takes and credits per generation, sliders, Variety, seed | `suno.reroll_variation_control` |
| Instrumental toggle, Add Vocals | `suno.instrumental_scratch_audition` |
| Personas, Voices, Custom Models, artist-name moderation | `suno.consistent_artist_persona` |
| Lyric languages, Arabic, in-lyrics prompting | `suno.multilingual_phonetic_spacing` |
| Lyric layout rule (the project's own, not Suno's) | `suno.hallucination_prevention` |
| Stem Separation modes, plans and credits | `song_handoff.stem_separation_protocol` |

**Official pages disagreeing with each other on 2026-09-23** (both sides are written on the card named):
- v6 and v6-wild plan access: help centre vs pricing page — `suno.v6_engine_architecture`.
- Voices plan access, and the Voices FAQ still requiring v5.5 — `suno.consistent_artist_persona`.
- Add Vocals plan access: help page vs pricing page — `suno.instrumental_scratch_audition`.

**The owner's reports, 2026-09-23** (written on the cards named): his plan is Premier, which every disputed page includes, and new models reach Premier first (`suno.v6_engine_architecture`); section tags and bracketed directions in English, lyrics in their own script (`suno.structural_metatags`, `suno.multilingual_phonetic_spacing`).

**Re-checked 2026-09-24 for `suno.instrumental_solo_tags`:** no official page names an [Instrumental], [Break], [Interlude] or solo bracket tag, or a way to write an instrumental or silent bar inside a lyric; the glossary's Break is vocabulary, and the Instrumental toggle covers a whole song. Those tags stay community practice, as that card says.

**Not stated on any official page on 2026-09-23:** the default model, a seed, sample rate or bit depth for generation, field character limits, a list of supported languages (Arabic included), exact Max Mode credit cost, add-on credit pack prices.

**Sources read 2026-09-23:**
https://suno.com/blog/introducing-v6 ;
https://help.suno.com/en/articles/13924801 ;
https://suno.com/release-notes ;
https://help.suno.com/en/articles/13924481 ;
https://help.suno.com/en/articles/13924993 ;
https://help.suno.com/en/articles/13924737 ;
https://help.suno.com/en/articles/5782977 (404) ;
https://help.suno.com/en/articles/11362433 ;
https://help.suno.com/en/articles/2462273 ;
https://suno.com/hub/how-to-make-a-song ;
https://help.suno.com/en/articles/3197377 ;
https://help.suno.com/en/articles/3161921 ;
https://help.suno.com/en/articles/6141377 ;
https://help.suno.com/en/articles/9010177 ;
https://help.suno.com/en/articles/3484161 ;
https://help.suno.com/en/articles/6141505 ;
https://help.suno.com/en/articles/10153473 ;
https://help.suno.com/en/articles/13924929 ;
https://help.suno.com/en/articles/2409601 ;
https://help.suno.com/en/articles/3271873 ;
https://suno.com/blog/v5-5 ;
https://about.suno.com/blog/v5-5 ;
https://suno.com/terms ;
https://help.suno.com/en/articles/11362497 ;
https://help.suno.com/en/articles/6882817 ;
https://suno.com/pricing ;
https://help.suno.com/en/articles/12702337 ;
https://help.suno.com/en/articles/13670529 ;
https://help.suno.com/en/articles/13926081 ;
https://help.suno.com/en/articles/13876865 ;
https://help.suno.com/en/articles/13926145 ;
https://help.suno.com/en/articles/9601601 ;
https://help.suno.com/en/articles/3198209

<!-- adapter:imagefamilies -->

<!-- adapter:image-prompt-families -->

### ADAPTER — image prompt families, checked 2026-09-23

Checked against the makers' own pages on 2026-09-23: Black Forest Labs (docs and GitHub), Stability AI (model cards and API spec), OpenAI, Google (Gemini API), Midjourney and Ideogram (docs, API reference and GitHub). Every line is the maker's and is expected to go stale; where no official page states it, the entry reads *not documented*. The card `prompt.rule.model_specific_syntax_adapters` in `phase-07-image-prompt-engineering/how-to-write-an-image-prompt.md` carries the four families in engine-neutral words and points here for the syntax. A project refills this block under §1 before relying on it.

```
ADAPTER — image prompt families, checked 2026-09-23
  parameter style:        differs by maker, and it is the model that decides, not the family:
                          - FLUX.2 (Black Forest Labs): plain prose in one `prompt` field; JSON
                            prompts documented; hex colour codes in the prompt; "Word order
                            matters - FLUX.2 pays more attention to what comes first"
                          - GPT Image (OpenAI): prose in `prompt`; model, quality, size and
                            background are API parameters, "Set API parameters separately
                            from the prompt"; tags, paragraphs and JSON-like prompts all work
                          - Gemini image / Nano Banana (Google): conversational prose, text and
                            images in, via the Interactions API
                          - Midjourney: short phrases, then parameters as flags at the very
                            end of the prompt (--v, --no, --seed, --ar ...)
                          - Stability API (Stable Image Ultra, Core, SD3.5): multipart form
                            fields prompt, negative_prompt, seed, style_preset (17 presets),
                            model (SD3.5 endpoint only)
                          - Ideogram 4.0 API: `text_prompt` (plain text, magic prompt turned on
                            automatically) OR `json_prompt` (the structured caption, magic
                            prompt off) — mutually exclusive. The open weights are trained
                            "exclusively on structured JSON captions"
                          - Ideogram 3.0 API: prompt, negative_prompt, magic_prompt,
                            style_type (AUTO, GENERAL, REALISTIC, DESIGN, FICTION), seed
  negative prompt:        - FLUX.2: "does not support negative prompts"; "Most FLUX models do
                            not support negative prompts" — describe what should be there
                          - GPT Image: no negative-prompt parameter documented; "State
                            exclusions such as unwanted text, logos, or watermarks" in the prompt
                          - Gemini image: no negative field documented; use "semantic
                            negative prompts" ("an empty, deserted street with no signs of
                            traffic" instead of "no cars")
                          - Midjourney: --no a, b, c; the same as a multi-prompt weight of -0.5
                          - Stability Ultra, Core and SD3.5: negative_prompt, "an advanced
                            feature"
                          - Ideogram 3.0: negative_prompt; "Descriptions in the prompt take
                            precedence to descriptions in the negative prompt"
                          - Ideogram 4.0 API: no negative_prompt field listed
  weights:                - Stability Ultra and Core: (word:weight), weight "a value between
                            0 and 1", e.g. (blue:0.3) and (green:0.8); not stated for SD3.5
                          - Midjourney: word::2 multi-prompt weights, negatives allowed if the
                            total stays positive — versions 1 to 6.1 only; not on V7, V8.1 or
                            the default V8.2
                          - FLUX.2, GPT Image, Gemini image, Ideogram 4.0: none documented
  on-image text:          - quotation marks around the exact words: FLUX ("place the exact
                            wording in quotation marks"), GPT Image ("Put required wording in
                            quotes"; the cookbook adds "or ALL CAPS" and letter-by-letter
                            spelling for hard words), Midjourney (double quotes only, V6 and
                            later; "single quotes or apostrophes (' ') won't work"), Ideogram
                            plain-text prompts ("Enclose Text in Quotation Marks", "Position
                            Text Early in the Prompt"), Gemini (template: with the text
                            "[text to render]")
                          - Ideogram 4.0 JSON: a text element, `type: "text"`, whose `text`
                            field holds the literal words, placed by `bbox`
  seed:                   - FLUX.2 [pro]: seed, "Optional seed for reproducibility"
                          - Stability: seed 0 to 4294967294; 0 or omitted = random
                          - Midjourney: --seed; on V8.1 and V8.2 "99% identical"
                          - Ideogram 3.0: seed, "Set for reproducible generation"; Ideogram
                            4.0 API lists seed in the response, not as a request field
                          - GPT Image, Gemini image: no seed documented on the pages checked
  text encoder:           not a prompt field, but the card's claims rest on it:
                          - FLUX.1: google/t5-v1_1-xxl plus openai/clip-vit-large-patch14
                          - FLUX.2 [dev]: Mistral-Small-3.2-24B-Instruct-2506; FLUX.2 [klein]:
                            Qwen3 4B or 8B
                          - SDXL base 1.0: "two fixed, pretrained text encoders
                            (OpenCLIP-ViT/G and CLIP-ViT/L)"
                          - SD3.5 Large: OpenCLIP-ViT/G and CLIP-ViT/L (77 tokens) plus
                            T5-xxl (77/256 tokens)
                          - Ideogram 4: Qwen3-VL-8B-Instruct, "Instead of a text-only encoder
                            like CLIP or T5"
                          - Gemini image: "Gemini's native image generation capabilities"
                          - GPT Image: not documented by the vendor
  known quirks:           FLUX.2 [klein] "does not include prompt upsampling. Write detailed,
                            descriptive prompts"; FLUX.2 [dev] "benefits significantly from
                            prompt upsampling"
                          BFL's own style page recommends "explicit tags at the end of your
                            prompt" for style and mood, after the prose
                          Midjourney: "Short and simple prompts typically generate the best
                            images"; "Avoid making long lists or detailed instructions"
                          Midjourney moderation "reads every word you add to the --no parameter
                            independently" ("--no modern clothing" reads as "no clothing")
                          Midjourney text "works best with the standard Latin alphabet";
                            Ideogram: "a non-Latin alphabet or accented Latin characters may
                            have some difficulty being generated correctly, if at all" — test
                            Arabic or Syriac lettering before relying on it
                          Ideogram 4 open weights: plain-text prompts "will not work and will
                            likely trigger a safety warning" — run them through magic prompt
                          GPT Image 2.5 quality: low, medium, high, xhigh, max; gpt-image-2:
                            low, medium, high
                          Gemini image best languages include ar-EG
                          SD3.0 API calls are re-routed to SD3.5 "As of April 17, 2025"
```

| card claim | status | source URL |
| :--- | :--- | :--- |
| T5 is one of the text encoders image models use | CONFIRMED — FLUX.1 loads `google/t5-v1_1-xxl`; SD3.5 Large lists "T5-xxl" | https://github.com/black-forest-labs/flux/blob/main/src/flux/util.py<br>https://huggingface.co/stabilityai/stable-diffusion-3.5-large |
| CLIP-L is one of them | CONFIRMED — FLUX.1 loads `openai/clip-vit-large-patch14`; SDXL and SD3.5 list "CLIP-ViT/L" | https://github.com/black-forest-labs/flux/blob/main/src/flux/util.py<br>https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0<br>https://huggingface.co/stabilityai/stable-diffusion-3.5-large |
| CLIP-G is one of them | CONFIRMED — SDXL and SD3.5 list "OpenCLIP-ViT/G" | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0<br>https://huggingface.co/stabilityai/stable-diffusion-3.5-large |
| some families use a proprietary multimodal LLM (Gemini image) | CONFIRMED — "Nano Banana is the name for Gemini's native image generation capabilities"; it takes "text, images, video, or a combination" | https://ai.google.dev/gemini-api/docs/image-generation |
| some families use a proprietary multimodal LLM (OpenAI GPT Image) | NOT FOUND — the image pages describe parameters and prompting, not the model's architecture or encoder | https://developers.openai.com/api/docs/guides/image-generation<br>https://developers.openai.com/api/docs/guides/image-prompting |
| the encoders are T5, CLIP-L, CLIP-G or a proprietary multimodal LLM (the full set) | CHANGED — current open-weight models use open LLM or VLM encoders: FLUX.2 [dev] Mistral-Small-3.2-24B-Instruct-2506, FLUX.2 [klein] Qwen3 4B/8B, Ideogram 4 Qwen3-VL-8B-Instruct "Instead of a text-only encoder like CLIP or T5" | https://github.com/black-forest-labs/flux2/blob/main/src/flux2/text_encoder.py<br>https://github.com/black-forest-labs/flux2/blob/main/src/flux2/util.py<br>https://github.com/black-forest-labs/flux2<br>https://github.com/ideogram-oss/ideogram4 |
| "Modern T5-based diffusion models" are the natural-prose family | CHANGED — T5 is in FLUX.1 and SD3.5; BFL's current text-to-image line, FLUX.2 ("the recommended model for text-to-image generation"), uses Mistral Small or Qwen3, not T5 | https://github.com/black-forest-labs/flux/blob/main/src/flux/util.py<br>https://huggingface.co/stabilityai/stable-diffusion-3.5-large<br>https://github.com/black-forest-labs/flux2/blob/main/src/flux2/text_encoder.py<br>https://docs.bfl.ai/llms.txt |
| natural_prose: write full descriptive sentences | CONFIRMED — FLUX: "FLUX works best when your prompt reads like a clear description of the image"; Gemini: "Describe a scene in rich detail"; Ideogram: "write your prompt using complete sentences and punctuation" | https://docs.bfl.ml/guides/prompting_unified_basics<br>https://ai.google.dev/gemini-api/docs/image-generation<br>https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/2-prompting-fundamentals/text-and-typography |
| natural_prose: avoid comma tag lists | CHANGED — OpenAI: "Short prompts, descriptive paragraphs, JSON-like structures, instructions, and tags can all express the same intent"; BFL itself recommends "explicit tags at the end of your prompt" for style and mood; Ideogram 4 is trained on JSON captions | https://developers.openai.com/api/docs/guides/image-prompting<br>https://docs.bfl.ml/guides/prompting_unified_style<br>https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md |
| keyword_mix: usually supports token weighting | CHANGED — Midjourney multi-prompt weights work only on versions 1 to 6.1, not on V7, V8.1 or the default V8.2; weighting is documented only for Stability Ultra and Core; none documented for FLUX.2, GPT Image, Gemini image or Ideogram 4.0 | https://docs.midjourney.com/hc/en-us/articles/32658968492557-Multi-Prompts-Weights<br>https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version<br>https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference) |
| keyword_mix: lighting prefixes | NOT FOUND — no maker documents a lighting prefix syntax; lighting is described in words (Midjourney lists "Lighting: What kind?" among details; BFL gives lighting vocabulary) | https://docs.midjourney.com/hc/en-us/articles/32023408776205-Prompt-Basics<br>https://docs.bfl.ml/guides/prompting_unified_style |
| dual_encoder: two text encoders | CONFIRMED for SDXL — "two fixed, pretrained text encoders (OpenCLIP-ViT/G and CLIP-ViT/L)" | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 |
| dual_encoder describes the current Stability line | CHANGED — SD3.5 Large has three encoders (two CLIPs plus T5-xxl); SDXL is not among the current v2beta generate endpoints, which are Ultra, Core and SD3.5 (`sd3.5-large`, `sd3.5-large-turbo`, `sd3.5-medium`) | https://huggingface.co/stabilityai/stable-diffusion-3.5-large<br>https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference) |
| dual_encoder: split the tokens across the two encoders | NOT FOUND — the publisher's model card and API describe one prompt; no instruction to send different text to each encoder | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0<br>https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference) |
| dual_encoder: comma-delimited prompt | NOT FOUND — Stability's prompt field asks for "A strong, descriptive prompt that clearly defines elements, colors, and subjects" | https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference) |
| numerical token weights written (word:1.2) | CHANGED — the vendor's format is `(word:weight)` with weight "a value between 0 and 1", e.g. `(blue:0.3)`, on the Ultra and Core endpoints; 1.2 is outside the documented range; not stated for SD3.5; not mentioned on the SDXL model card | https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference)<br>https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 |
| dedicated positive and negative slots | CONFIRMED for the Stability API — `negative_prompt` on Ultra, Core and SD3.5, "an advanced feature"; the SDXL model card does not mention negative prompts | https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference)<br>https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 |
| typographic: put the exact signage wording in quotes | CONFIRMED — Ideogram (plain-text prompts), FLUX, GPT Image, Midjourney (double quotes, V6 and later) and Gemini (template) all document it; Ideogram 4.0 JSON puts the words in a text element's `text` field instead | https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/2-prompting-fundamentals/text-and-typography<br>https://docs.bfl.ml/guides/prompting_unified_basics<br>https://developers.openai.com/api/docs/guides/image-prompting<br>https://docs.midjourney.com/hc/en-us/articles/32502277092109-Text-Generation<br>https://ai.google.dev/gemini-api/docs/image-generation<br>https://docs.ideogram.ai/using-ideogram/getting-started/prompting-guide/4.-json-prompting-ideogram-4.0 |
| typographic: a text rendering mode | NOT FOUND as a named mode. Nearest documented: Ideogram 3.0 `style_type` DESIGN; FLUX.2 [flex] is a separate model "Specialized for typography and text rendering" | https://developer.ideogram.ai/api-reference/generate-images/generate-v3<br>https://docs.bfl.ai/llms.txt |

**Models, as of 2026-09-23.**
- **Black Forest Labs:** FLUX.2 [max], [pro] ("the recommended default model for image editing and generation"), [flex], [klein] 4B and 9B, [dev]; "FLUX.2 is the recommended model for text-to-image generation". FLUX.1 Kontext: "For new projects, we recommend FLUX.2". FLUX 3 is on the API for video with synchronized audio; bfl.ai lists it for "Image, Video, Audio and Action-Prediction", but the checked docs give no FLUX 3 text-to-image endpoint. Sources: https://docs.bfl.ai/llms.txt , https://docs.bfl.ml/flux_2/flux2_overview , https://bfl.ai/models
- **OpenAI:** `gpt-image-2.5-sunburst` (base model, quality first) and `gpt-image-2.5-flare` (small model, speed first) — "For new integrations, use one of the GPT Image 2.5 models". `gpt-image-2` is the earlier model. Shutdowns: `gpt-image-1` 2026-10-23; `gpt-image-1-mini`, `gpt-image-1.5`, `chatgpt-image-latest` 2026-12-01; `dall-e-2` and `dall-e-3` removed 2026-05-12. Sources: https://developers.openai.com/api/docs/guides/image-generation , https://developers.openai.com/api/docs/guides/image-prompting , https://developers.openai.com/api/docs/deprecations
- **Google:** Nano Banana 2 Lite `gemini-3.1-flash-lite-image`, Nano Banana 2 `gemini-3.1-flash-image`, Nano Banana Pro `gemini-3-pro-image`, and the legacy Nano Banana `gemini-2.5-flash-image`. Imagen: "Imagen is shut down and no longer available through the Gemini API". Sources: https://ai.google.dev/gemini-api/docs/image-generation , https://ai.google.dev/gemini-api/docs/imagen
- **Midjourney:** "The current default Midjourney version is V8.2" (default since 2026-07-24); V8.1 was the default from June 10 to July 23, 2026; V8.0 "is no longer available for use"; V6 and V7 still appear in the feature chart. Source: https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version
- **Stability AI:** API — Stable Image Ultra, Stable Image Core, and SD3.5 (`sd3.5-large`, `sd3.5-large-turbo`, `sd3.5-medium`; `sd3.5-flash` priced in the model description); SD3.0 calls re-routed to SD3.5. SDXL base 1.0 is open weights on Hugging Face. Sources: https://api.stability.ai/v2alpha/openapi (the spec behind https://platform.stability.ai/docs/api-reference) , https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 , https://huggingface.co/stabilityai/stable-diffusion-3.5-large
- **Ideogram:** Ideogram 4.0 (API, and open weights released 2026-06-03, 9.3B parameters), Ideogram 3.0 still on the API, plus P-Image. Sources: https://developer.ideogram.ai/api-reference/generate-images/generate-v4 , https://developer.ideogram.ai/api-reference/generate-images/generate-v3 , https://github.com/ideogram-oss/ideogram4

**Which families these fit (this check's reading, not a vendor statement; the engine-selection step assigns `prompt_family`).** natural_prose: FLUX.2, GPT Image 2.5, Gemini image, and Ideogram through magic prompt. keyword_mix: Midjourney V8.2 (short phrases plus flags; no weights on V8) and Stability Ultra/Core (weights 0 to 1, negative field). dual_encoder: SDXL open weights; SD3.5 has three encoders, so the family name no longer describes the current Stability line. typographic: Ideogram (quotes in plain text, a `text` element in 4.0 JSON), FLUX.2 [flex], GPT Image; every maker checked documents quoted on-image wording.
