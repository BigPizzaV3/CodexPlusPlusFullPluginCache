# How Phase 3 Works: Shooting Script, Technical Breakdown & Single Decision Ownership

Phase 3 is the Director & DP's technical command center. It bridges the dramatic screenplay (from Phase 2, or from Phase 5's lyric and timing map on a song-led route) into an actionable, numbered Two-Column AV Shooting Script.

---

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [1. Single Decision Ownership: The Law of Shot Setup](#1-single-decision-ownership-the-law-of-shot-setup)
- [2. Cross-Phase Architecture & Links](#2-cross-phase-architecture-links)
- [3. The 6 Cinema Modes (M1 to M6)](#3-the-6-cinema-modes-m1-to-m6)
- [4. The Technical Shooting Script Table Format](#4-the-technical-shooting-script-table-format)
- [5. Master File Reference](#5-master-file-reference)

<!-- /GENERATED:toc -->

## 1. Single Decision Ownership: The Law of Shot Setup

Phase 3 is the **Sole and Exclusive Creator** of:
1. **Shot Scale & Size**: Selected directly from [shot-sizes.md](./shot-sizes.md) (EWS, WS, MS, MCU, CU, ECU).
2. **Camera Angle & Elevation**: Selected directly from [angle-height.md](./angle-height.md) and [framing-named-shots.md](./framing-named-shots.md) (Low angle, High angle, Dutch tilt, Eye-level).
3. **Dramatic Shot Intention**: Why this shot exists in the scene.

> [!IMPORTANT]
> **The Law of Single Ownership & Downstream Inheritance**:
> - Phase 3 **locks** the Shot Size and Camera Angle in the Technical Shooting Script Table.
> - Phase 6 **inherits** these decisions to draw the storyboard panels. It does NOT re-decide or alter shot size.
> - Phase 7 **inherits** these decisions for Slot 3 in the prompt. It does NOT make new framing choices.
> - There is exactly **one decision owner** for shot size: Phase 3.
>
> **And one for the lens: Phase 7.** Phase 3 may write the *intent* — "long lens, subject separated
> from the crowd", "wide, the room is the subject" — because that is a directing decision and it
> belongs with the shot. The focal length, the glass and the sensor are optical decisions and they
> are set in Phase 7 under its Slot 3. Phase 6 writes whatever intent it inherited into the CAMERA
> column and **invents nothing optical**; where the storyboard template asks for a lens and Phase 7
> has not run, write the intent or leave the cell open. An invented focal length in Phase 6 is a
> decision made by the phase least equipped to make it, and every downstream prompt inherits it.
>
> **A movement direction written here** — "walks in from frame right" — is read from
> `comp.screen_direction` in [composition.md](../phase-06-storyboard-layout/composition.md) when it is
> written, so the line holds across the cut; Phase 6 inherits it with the rest of the shot table.

---

## 2. Cross-Phase Architecture & Links

| Downstream Phase | What it Inherits from Phase 3 | Cross-Link |
| :--- | :--- | :--- |
| **Phase 6: Storyboard** | Inherits Shot Size & Angle; applies composition & actor blocking | [Phase 6 Storyboard](../phase-06-storyboard-layout/PHASE.md) |
| **Phase 7: Image Prompts** | Inherits Shot Size & Angle into Slot 3; adds optical lens focal length | [Phase 7 Image Prompts](../phase-07-image-prompt-engineering/PHASE.md) |
| **Phase 8: Video Prompts** | Inherits Camera Movement Intent; translates into 6-axis vectors | [Phase 8 Video Prompts](../phase-08-video-prompt-engineering/PHASE.md) |

---

## 3. The 6 Cinema Modes (M1 to M6)

All six modes are in one table. **A mode owns the movement and the grade**; the two columns before
them are a starting point, and the lens column in particular is a suggestion this phase does not get
to enforce — see the two notes underneath.

| Mode | Scene Type | Body (default) | Lens intent — *Phase 7 sets the glass* | Movement — *the mode owns this* | Grade / Texture — *the mode owns this* |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1 Narrative** | Real-world drama | Alexa 35 | Period texture — vintage anamorphic by default (Panavision Ultra Vintage 2x) | Handheld breath, subtle dolly | Kodak Vision3 250D (EI 250) |
| **M2 Studio** | Clean editorial, fashion | Alexa Mini LF | Clean and sharp — spherical prime by default (Cooke S4/i) | Locked tripod + slow push | Saturated, deep blacks |
| **M3 Action** | Combat, stunts, chase | Alexa 35 | Period texture or clean sharpness — vintage anamorphic, or a modern spherical set (ARRI Signature Prime) where the piece wants sharpness rather than texture | Reactive handheld + shake | Gritty realism, atmospheric haze |
| **M4 Performance** | Concert, stage, dance | Alexa 35 | Nostalgic or contemporary — vintage anamorphic for a filmic performance; modern spherical primes or a broadcast zoom (Cooke S4/i, Angenieux) for a stage, arena or sports piece | Orbital handheld passes | Cool tones, highlight bloom |
| **M5 Atmospheric** | Ruins, ziggurats, vistas | Alexa Mini LF | Period texture — vintage anamorphic by default | Locked or slow survey push | Deep shadow detail, palette-driven |
| **M6 Animation — drawn** | Flat 2D, cel, anime, cartoon, kids | **None — a drawn mode has no camera body.** The render is digital cel or vector | **None optical — no glass, no film stock, no aperture.** A virtual focal length may be named as a *framing* instruction and nothing more; do not write an f-stop or a Kelvin figure | Dynamic 2D pans, kinetic keyframe snap, multiplane parallax (`kids.bg_parallax`) | Cel shading, clean vector lines, anime watercolor (from [anime-2d.md](../phase-07-image-prompt-engineering/anime-2d.md)) |
| **M6-R Animation — rendered** | 3D and CG, including stylised and clay-render work | **None physical, but there is a virtual camera** | **Optical values apply**, because a virtual camera has a real focal length. Phase 7's Slot 3 sets them, as on any live-action mode. What does *not* apply is a film stock: a render has no gate | Full 3D camera moves — dolly, crane, orbit — plus held stylised beats | The render school **and the surface**: what the geometry is lit like and what it is made of (`medium.stylised_cg_handmade`, `medium.threed_render`) |

**Why animation is two rows and not one.** It used to be a single **M6** covering *"2D/3D cartoon,
anime, kids"*, and that row's movement column, grade column and lens note were all written for flat
drawn work — so a 3D or stylised-CG piece had exactly one mode available to it and that mode denied
it the virtual camera it actually has. The split follows the same line the image and video phases
draw: **this is about whether there is a camera, not about whether the work is animated.** Drawn work
has none; rendered work has one. Everything downstream — the optical values, the depth cue, the
surface description and the negative tiers — forks on that and nowhere else.

**M6 carried a second problem worth naming**: its lens note said "roughly 35mm equivalent" while the
image phase's fallback says 50mm, so the two files handed a reader different numbers for the same
absent lens. Neither is a default any more — on drawn work a focal length is a framing word or it is
nothing, and on rendered work Phase 7's Slot 3 owns it, as it does for every live-action mode.

**Neither animation row has a camera body or a film stock**, because nothing is photographed: the
frame is drawn or rendered, so there is no sensor to choose and no emulsion to grade toward. That is a real difference and it is written into
the row rather than left for the reader to infer. It is not a reason to lift M6 out of the table —
an animation piece needs a mode for exactly the same reasons a live-action one does, and a reader
scanning five rows and a paragraph misses the sixth mode entirely, which is how a kids piece ends up
shot as M1 with a film stock it cannot have.

**On the lens column, and who owns it.** The vintage anamorphic is a default, not a law. It carries
oval bokeh, blue horizontal streaks and a soft falloff at the edges — beautiful on a period drama or
a ruin at dusk, and wrong on a modern stadium, a clean product film or anything that wants to read
as broadcast. A contemporary subject takes modern spherical glass, and the mode still applies,
because **what a mode actually specifies is the movement and the grade, not the glass.** Those two
columns are this phase's to set and they travel down the pipeline as written.

The lens column is not. It is written here as *intent* — "period texture", "clean and sharp",
"long, subject separated from the crowd" — and the intent is a directing decision that belongs with
the shot. **The focal length, the glass and the sensor are optical decisions and they are set in
Phase 7, under its Slot 3**, which is the same single-ownership rule stated in §1 of this document.
So name the intent in the shot plan and say why; do not hand Phase 7 a focal length it did not ask
for, and do not read the body column as a lock — the Alexa entries are a texture reference for the
grade, not a requirement that the piece be photographed on one.

---

## 4. The Technical Shooting Script Table Format

Every scene is converted into this authoritative shooting script table:

| Shot ID | Script / Audio Ref | Mode & Look | Scale & Angle (from Phase 3 Cards) | Camera Movement & Motivation | Timing src | Time In / Time Out | Duration (s) | Lyric / Audio Cue | Transition In/Out |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SH-001` | Sc. 1, L. 1 (or Verse 1) | M5 Atmospheric | Extreme Wide, High Angle (`size.ews`, `angle.high`) | Slow survey pan across Nineveh city wall | narration | 00:00.00 – 00:04.00 | 4.0s | Intro drum swell | Fade In / Hard Cut |
| `SH-002` | Sc. 1, L. 2 (or Verse 1) | M1 Narrative | Medium Close-Up, Low Angle (`size.mcu`, `angle.low`) | Handheld breath tracking royal procession | narration | 00:04.00 – 00:07.00 | 3.0s | "On the walls of the great city..." | Cut on Action |
| `SH-003` | Sc. 1, L. 3 (or Chorus 1) | M1 Narrative | Extreme Close-Up, Eye Level (`size.ecu`, `angle.eye_level`)| Locked push on carved cuneiform clay tablet | song | 00:07.00 – 00:09.50 | 2.5s | "Gold turned to ash in the fire" | Whip Pan Out |

> [!NOTE]
> **Audio-Visual & Music Route Integration**:
> - **Script / Audio Ref**: Accepts screenplay scene/line coordinates (e.g. `Sc. 1, L. 1`) or musical section markers (e.g. `Verse 1, Bars 1-4`, `Chorus 1`). It also carries every `TEXT: "…"` item Phase 2 wrote in that line's Visual cell — hook copy, a lower third, a label, what an advert's end must carry — with the seconds it holds, so on-screen text reaches Phases 6 to 8 already timed. Phase 2 records only what the end carries (logo, name, phone); its form — a separate static card, or the logo and number folded into the last live shot on a feed advert — is decided here by `promo.end_card`. On a route with no Phase 2 (a song-led piece), the text comes straight from the brief — a sign, a title, a name — and is entered here the same way.
> - **Mode & Look**: the cinema mode (M1 Narrative, M5 Atmospheric …) always. **On a piece that
>   deliberately alternates two render modes, the same cell also carries which look the row is in** —
>   `M1 Narrative · Look B (drawn reconstruction)`. A reconstruction documentary cutting between
>   photographed site footage and drawn rebuilds is the standard case. Without it, the look lives only
>   in whoever's head wrote the row, and Phases 6, 7 and 8 each guess again: the optical values, the
>   depth cue and the negative block all answer differently per look, and a row that does not say
>   which look it is in cannot be prompted correctly by anyone downstream. Declare the looks once at
>   the top of the table (`LOOKS: A = photoreal · B = flat 2D reconstruction`) and tag every row.
>   **The same goes for period.** A piece that cuts between two periods in one render mode — a
>   NOW/THEN heritage reel, a present-day site against its ancient rebuild — carries the period in
>   the same cell, `M1 Narrative · THEN`, declared once at the top of the table (`PERIODS: NOW =
>   present day · THEN = <the reconstructed period>`), because the image prompt's Tier 2
>   anachronism list is taken from this cell and a row with no period cannot say whether it wants it.
>   A single-look, single-period piece leaves both off and the cell is just the mode, as in the examples above.
> - **Timing src**: which clock this row is on. **A row, not a table.** Most pieces have one answer
>   for the whole film and this cell is the same on every row, so write it once at the top and leave
>   the column off. **A piece whose timing authority changes partway through needs the column**, and
>   that is not exotic: a documentary with a three-minute sung passage in the middle is scored by the
>   narration at both ends and by the song in between, and a music video with a spoken cold open is
>   the same shape reversed. The two clocks do not merely differ, they are measured from different
>   files — one from the rendered narration, one from the locked song — so a table that can hold only
>   one answer silently reports one of its sections as timed when it is not.
>   Declare the sections at the top of the table, the same way `LOOKS:` declares the render modes:
>   `BOUNDARIES: 00:00–02:30 narration · 02:30–05:30 song · 05:30–08:00 narration`,
>   then tag each row `narration` or `song`. **The boundary timecodes are themselves provisional**
>   until both sources are rendered, and they move — which is exactly why they are written down in
>   one place rather than implied by where the rows happen to change.
> - **Timing src also takes `captured`, and that row behaves unlike the other two.** Where the shot is
>   found or filmed rather than generated — archive footage, a recorded interview, a live performance —
>   **its length is a fact about the material, not a decision.** You cannot shorten it by writing less,
>   and nothing downstream may trim it to fit a voice: the narration is written into the gaps instead
>   (`rhythm.locked_picture_narration`). Until the item is in hand its length is unknown rather than
>   estimated, so the cell reads `pending_measured_duration` from the start and carries the intended
>   shape beside it — *"roughly 40 seconds, the trench sequence"* — rather than a guess dressed as a
>   plan. Where a found item's origin is not yet named, write what is known beside it and let
>   `pending_archive_source` travel as a note in the handoff; it never holds the table.
>   **A still is the exception inside `captured`.** A photograph of an object, a scan, a painting or a
>   relief shot in a museum is found material with no running length of its own, so its duration is
>   designed, as on a generated row: write the designed seconds, not `pending_measured_duration`.
> - **This phase owns every duration cell in the package and never used to name those markers.** It
>   does now: a provisional timecode is written with its marker beside it, on every route.
> - **Time In / Time Out**: absolute timecode. **On a branching piece there is no absolute timecode** — a shot's position depends on the path taken to reach it — so these become *offset within the node*, and the table carries a `Node` column and a `Path` column beside them. **Duration then sums two different ways and both are real:** per-path runtime, which is what a viewer experiences and what any contractual cap applies to, and total footage, which is what gets made and paid for. Name which one a total is, every time, and compute the **longest path** explicitly — it is the number a cap binds, it is not the largest node, and nothing else in this package computes it for you. **Where it comes from depends on the row's Timing src.
>   In route order the source runs before this phase** — Phase 5 first on a music route, Phase 4 first
>   on a narrated one (root routing questions 2 and 3) — so the cells take the measured file. **Where it
>   does not exist yet** (this phase was entered first, or the script is still changing), **the first pass
>   is provisional:**
>   - **Music route** — from the locked song, once Phase 5 exists. Before that, the BPM and metre grid.
>   - **Narrated route** — from the rendered narration, once Phase 4 exists. Before that, estimate from
>     the word count at the cadence the piece is written to (`words ÷ rate`) and distribute across the
>     shots. **Take the rate from the card, not from this page.** Phase 4 owns every speaking rate in
>     the package, one card per register, and the full list is generated into
>     [`../phase-04-audio-narration/HOW-PHASE-4-WORKS.md`](../phase-04-audio-narration/HOW-PHASE-4-WORKS.md)
>     step 2 rather than retyped here — a register added there used to be missing from this
>     sentence, and a two-hander taking a narration rate is about ninety seconds of error on an
>     eleven-minute film. No figure is repeated here, deliberately: a rate copied into a second file
>     drifts, and a drifting rate rewrites a shot list without anyone editing it.
>     **The estimate is never the answer.** Every rate is a planning estimate, and the real duration
>     comes from the rendered audio file, measured — never from the arithmetic. Re-cut these cells
>     against the measured file the moment it exists, and build the picture to what was measured,
>     never the reverse. A Phase 5 Route C cue map, where there is one, sits under `decisions` as
>     `score_cue_map` and is advisory here: the rows follow the measured voice, and the music is
>     fitted to them in the edit.
>   - **No audio at all** — a silent piece, a text-and-foley ad — the durations are the designed
>     durations, quantised to whole frames at the delivery frame rate.
>
>   Mark a provisional row as provisional. A timecode nobody flagged as an estimate is indistinguishable
>   from a measured one, and that is how a shot list survives into an edit it does not fit.
> - **Lyric / Audio Cue**: Anchors the visual cut to sung lyrics or sonic transients, enforcing `mv.cut_on_beat` and preventing cuts across sung words. A row where a character sings or speaks on camera is marked *on-lip* in this cell, so the lip-sync need is known before the clips are written; the take length it can hold is read from the engine record in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md) §2, and where no engine is named yet, choose the shot lengths, note the choice under `decisions`, and continue.
> - **A deliberate flash sequence is decided here, so it is noted here.** A row that sets out to strobe
>   or flash — a strobe, a run of flash frames, a storm of repeated lightning, a fast cut run that
>   alternates dark and bright frames on purpose — carries `pending_photosensitivity_check` as a note
>   for delivery. The shot is still designed and written; this skill writes no rate or threshold for it
>   (root `SKILL.md` §0, `safety.photosensitive_flash`), and the note travels in the handoff.
>   **Ordinary light is never a flash question** — firelight, candles, an oil lamp, a sunset, a
>   flickering bulb in a scene, a single lightning strike, a beam that sweeps past once. Write it as
>   light and carry no marker.

*(Markers are defined in [`../ENGINE-CHECK.md`](../ENGINE-CHECK.md), which owns the set and the rule that each one closes two ways — resolved, or `unobtainable`, with what was done instead.)*

---

## 5. Master File Reference
- **Shot Sizes**: [shot-sizes.md](./shot-sizes.md) (21 cards)
- **Angles & Elevation**: [angle-height.md](./angle-height.md) (58 cards)
- **Named Framing Setups**: [framing-named-shots.md](./framing-named-shots.md) (61 cards)
- **Cuts & In-Scene Grammar**: [cuts-in-scene.md](./cuts-in-scene.md) (69 cards)
- **Scene Transitions**: [scene-transitions.md](./scene-transitions.md) (134 cards)
- **Shot Transitions**: [shot-transitions.md](./shot-transitions.md) (67 cards)
- **Documentary Coverage**: [documentary.md](./documentary.md) (123 cards)

**Format bibles — these were missing from this list, and they are the files a real brief opens first:**

- **Vertical / 9:16**: [vertical-short-form.md](./vertical-short-form.md) (46 cards) — framing for the phone
- **Commercial, promo, trailer**: [ads-trailers.md](./ads-trailers.md) (59 cards) — pack shots, end cards, cut-rate ramps
- **Music video**: [music-video.md](./music-video.md) (31 cards)
- **Children's content**: [kids-content.md](./kids-content.md) (27 cards) — including the 1.5-second cut floor
- **Sound as a visual decision**: [sound-as-visual.md](./sound-as-visual.md) (26 cards)
- **Camera modes**: [cinema-modes.md](./cinema-modes.md) — §3 of this document depends on it

**Visual Language Bible bridge** — [vlb-ten-laws.md](./vlb-ten-laws.md), [vlb-formats.md](./vlb-formats.md),
[vlb-genres.md](./vlb-genres.md), [vlb-decision-tables.md](./vlb-decision-tables.md),
[vlb-shot-sizes.md](./vlb-shot-sizes.md), [vlb-angle-height.md](./vlb-angle-height.md),
[vlb-cuts-in-scene.md](./vlb-cuts-in-scene.md), [vlb-scene-transitions.md](./vlb-scene-transitions.md),
[vlb-speed-timing.md](./vlb-speed-timing.md).
**The 9:16 safe-zone numbers are owned by `vertical.safe_zones` in [../phase-07-image-prompt-engineering/vertical-short-form.md](../phase-07-image-prompt-engineering/vertical-short-form.md)**, which is the only place a figure is written. The reserved bands belong to the platform's own interface — the caption stack, the action rail, the profile strip — and they move when the platform moves, which is why the numbers live on one dated card instead of in this file. They are a delivery rule, so they outrank craft — but the figure is read from the card, never copied here. **They apply to a 9:16 delivery.** A feed video on Facebook or YouTube can be horizontal as easily as vertical, and the aspect is the brief's: a 16:9 feed piece takes no 9:16 band, and keeps type off the outer edge and off the player's control band as `comp.safe_areas` in [`../phase-06-storyboard-layout/composition.md`](../phase-06-storyboard-layout/composition.md) sets out.

- **Full Card Catalog**: [INDEX.md](./INDEX.md) & [LOOKUP.md](./LOOKUP.md) (768 cards)
