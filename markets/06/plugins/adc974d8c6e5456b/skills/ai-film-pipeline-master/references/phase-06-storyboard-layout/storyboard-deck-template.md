# Storyboard deck template

The poster: one image showing every panel in a grid, with cinematic stills, captions, camera
notes and audio notes. This is a presentation output rather than a stage, and it is optional.
The shot plan is what the production runs on; this is what you put in front of someone.

> [!NOTE]
> **Pitch Artifact Exemption**: The Storyboard Deck Poster is a pitch and presentation artifact, not a delivered video generation frame, so its captions and labels are typeset on it. Frames for actual video production in Phase 7/8 carry no captions, labels or subtitles; lettering that belongs to the scene — a sign, an inscription, a label on a product — keeps the treatment the in-frame text routing selected for it (root `SKILL.md` §4 item 5, `textimg.read_or_seen`), which may be generated, composited or set in the edit.

---

The premium visual storyboard deck poster — single image showing all panels in grid with cinematic stills, captions, camera notes, audio notes, ending on a final story beat (no logo, no brand reveal) — or, on a commissioned advert, product video or brand film, ending on the endline and lock-up that the client is paying for, drawn where the film itself carries it (rule 5 of §2.4).

<!-- GENERATED:toc — do not edit by hand. Generated in the source package -->

## Contents

- [Master deck assembly specification](#master-deck-assembly-specification)
- [2.1 When to use this template](#21-when-to-use-this-template)
- [2.2 The master text-table template](#22-the-master-text-table-template)
- [2.3 Filled example — Coffee story 15 seconds, 8 panels](#23-filled-example-coffee-story-15-seconds-8-panels)
- [2.4 Rules for text-table output](#24-rules-for-text-table-output)
- [2.5 When user asks for both modes](#25-when-user-asks-for-both-modes)
- [2.6 Multi-part text storyboards](#26-multi-part-text-storyboards)

<!-- /GENERATED:toc -->

## Master deck assembly specification

The deck is **built, not generated as one image**. Generate or source only the image cells, without
captions or interface text, then assemble the six-column grid in a deterministic layout tool. The
deck record therefore carries `render_mode: built`, `engine: none - built` and `text_owner: built`.
The image cell keeps its own source render mode. Exact spelling, panel count, row order, timecodes and
typography are verified from the source table after export; no image model is asked to reproduce them.

```yaml
storyboard_deck:
  render_mode: built
  engine: none - built
  text_owner: built
  deck_format: null
  panel_aspect: null
  panel_count: null
  source_table: null
  image_cells: []          # generated, captured or drawn separately; no burned-in labels
  columns: [cut_time, image, visual_action, camera_shot, dialogue, audio_sfx]
  on_screen_text_header: ON-SCREEN TEXT
  final_panel_kind: null   # story_beat / commissioned_lockup
  typography:
    title: null
    section: null
    body: null
  colours:
    background: null
    accent: null
    body_text: null
  export:
    size_px: null
    format: null
    checked_against_source_table_by: null
```

### Assembly order

1. Freeze the shot table and the exact panel count.
2. Prepare each image cell at the declared panel aspect, carrying the shot's own render mode and no text.
3. Place the cells into the fixed order `CUT/TIME | image | VISUAL/ACTION | CAMERA/SHOT | DIALOGUE | AUDIO/SFX`.
4. On a piece whose words appear on screen rather than being spoken, rename `DIALOGUE` to `ON-SCREEN TEXT` for every row, and on a sung piece to `LYRIC`; do not add a seventh column.
5. Typeset every string from the source table in the layout layer. Dialogue cells stay empty where nobody speaks; audio cells list only sound that exists.
6. End a story piece on its final story beat. End a commissioned advert, product video or brand film on the approved endline and lock-up — as its own panel only where the film has a separate end card, and inside the last story panel where the lock-up sits over the final live shot (`promo.end_card`).
7. Export, then compare panel count, timecodes, spelling, row order and final-panel kind against the source table. Record the checker in `checked_against_source_table_by`.

**DECK FORMAT fill**: 9:16 stills → "4:5 vertical" | 16:9 → "3:2 landscape" | 1:1 → "1:1 square" | 4:5 → "4:5 vertical"
**ORIENTATION-WORD**: 9:16 → "VERTICAL" | 16:9 → "LANDSCAPE" | 1:1 → "SQUARE" | 4:5 → "PORTRAIT"
**[LENS OR DRAWN LOOK] fill**: on photoreal, 3D or rendered-CG work, the lens intent Phase 3 wrote for the shot (period texture, clean sharpness, a long lens that separates the subject), and a focal length and stop only where Phase 7 has already set them — Phase 6 invents nothing optical (HOW-PHASE-3-WORKS.md §1). **On flat 2D, cel-shaded or cartoon work there is no lens**, so this slot takes the drawn look instead: the line weight and the ink and colour treatment, per [anime-2d.md](../phase-07-image-prompt-engineering/anime-2d.md). The field is never left empty and never filled with a focal length on drawn work — an empty slot on an animated deck is what makes a downstream default fire and put a 50mm lens on a cel frame. Whichever is chosen is identical across all panels on a single-look piece, exactly as [RENDER MODE] is — and on a piece that alternates two looks, it is filled per panel from that panel's MODE cell.

**[DEPTH CUE] fill**: "shallow depth of field" on photoreal work — that is the default, and it is what a deck of camera-made stills wants | on flat 2D, cel-shaded or cartoon work, "background held one flat tonal step back from the subject, foreground elements simplified" instead. There is no aperture in drawn animation, so a blur instruction there either does nothing or returns a photographic haze sitting on top of line art. Depth in a cel frame is made by tonal separation and by dropping detail, not by an f-stop. On 3D or rendered-CG work the photographic default applies, because there is a virtual lens. Whichever is chosen is identical across all panels on a single-look piece, exactly as [RENDER MODE] is — and on a piece that alternates two looks, it is filled per panel from that panel's MODE cell.
**Image-cell `[RENDER MODE]` fill**: use the exact machine enum from [`ENGINE-CHECK.md`](../ENGINE-CHECK.md): `built` for a chart, map, counter or diagram; `photoreal` for photographed-looking work; `flat_2d` for drawn work; `rendered_cg` for virtual-camera geometry; `stop_motion` for physically made frame-by-frame work. The deck around those cells remains `built`. A 3D render keeps optical values because it has a virtual camera; a drawn cell takes line weight, ink, colour treatment and tonal depth instead of a lens.

**One look or two.** Most pieces have one image-cell render mode and it is identical across all panels. The deck's own render mode stays `built` either way.

**A piece that deliberately alternates two looks uses `multi_look` and declares each constituent mode per sequence instead**, and the panel row carries which one it is in. A reconstruction documentary that cuts between photographed site footage and drawn reconstruction is the standard case; so is a live-action frame story around an animated memory. Write the machine modes as a list at the top of the deck — `RENDER MODES: A = photoreal · B = flat_2d` — give every panel row a **MODE** cell carrying `A` or `B`, and fill [LENS OR DRAWN LOOK] and [DEPTH CUE] from that panel's mode. The cut between the two modes is usually the point of that film, so the mode is a storytelling value and belongs in the row where it can be read. `medium.register_mixing` in Phase 3 covers how the two are cut together; this is how the deck records it.

**Image-cell generator choice**: when an image cell is generated, choose its engine from the dated
record in [`ENGINE-CHECK.md`](../ENGINE-CHECK.md). The assembled deck itself never names an image
engine because it uses `engine: none - built`.

---

<a id="50-storyboard-text-template"></a>
# 1. STORYBOARD TEXT TEMPLATE (Per-Shot Block Writeout)

When the user picks text mode instead of image mode, output structured blocks the user can hand directly to a video AI:

```
=========================================
SHOT [N] — [TIMECODE] — [BEAT NAME]
=========================================

Style: [genre + look]
Scene Goal: [what this shot accomplishes]
Character Lock: [identity, props, state — wardrobe is written only in the image and character-sheet prompts]
Environment Lock: [location, props, lighting]

Timeline and Camera:
[START - END] [Shot size + camera angle + camera movement + character action + emotion + small background motion]

Camera Rules:
[Motivated cinematic movement. Simple and controlled. Don't combine high subject motion with high camera motion.]

Motion Rules:
[Physical action verbs. Visible, easy to animate. No vague "transforms beautifully".]

Audio / SFX:
[The piece's actual music and sound: its track where it has one, then natural foley + ambient + dialogue if needed. Nothing the piece does not have.]

Performance:
[Specific micro-beats: blink, breath, head, eyes, hand, weight shifts. Background extras animated naturally.]

Lighting and Look:
[Physical light source description. Where it comes from, soft/hard, shadow direction, color temp, grain. On `flat_2d` work: the light direction and the palette temperature in words — no Kelvin figure, no grain.]

Negative:
No extra characters, no duplicate people, no changed face, no changed outfit, no warped hands, no frozen body, no random camera cuts, no flickering identity, no floating objects, no modern objects unless requested, no subtitles, no text the scene does not carry (in-scene lettering keeps its `in-frame-text.md` treatment), no UI, no watermark, no logo that the scene does not actually contain (a brand mark present in the real scene, on a kit, a package or a sign, stays).
```

---

<a id="50-5-storyboard-text-table"></a>
# 2. STORYBOARD TEXT-TABLE TEMPLATE (SIFU Layout Mirror in Text)

When user wants a **written storyboard that mirrors the SIFU visual layout** (instead of generating an image), output this exact markdown/ASCII table format. This is the **text equivalent** of the built storyboard deck above — same structure, same columns, same hierarchy, but readable in chat or markdown.

## 2.1 When to use this template

Use Text-Table Template when:
- User says "ستوريبورد نصي" / "text storyboard" / "بدون صورة"
- User wants to copy-paste the storyboard into a document, email, or production deck
- The chosen generator fails to produce deck-quality output after 2 attempts
- User wants the storyboard for review/notes before image generation
- Multi-language project needs translation per cell

## 2.2 The master text-table template

```
═══════════════════════════════════════════════════════════════════════════════
[BRAND NAME on commercial work, else PROJECT TITLE] (typeset uppercase)   [Tagline in italic on right — commercial work only]
[RUNTIME SECONDS]-SECOND [STORY TYPE] STORYBOARD ([ASPECT RATIO])
═══════════════════════════════════════════════════════════════════════════════

CUT │ TIME             │ VISUAL / ACTION       │ CAMERA / SHOT      │ DIALOGUE           │ AUDIO / SFX
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 1  │ 0:00 - 0:0X.X    │ [SCENE TITLE]         │ [SHOT TYPE]        │ [Line + speaker,   │ Music: [genre]
    │                  │ [Action sentence 1.]  │ [Framing detail.]  │ empty where nobody │ SFX: [foley]
    │                  │ [Action sentence 2.]  │ [Camera move.]     │ speaks.]           │ [Narrator VO
    │                  │ [Action sentence 3.]  │ [Lens intent.]     │                    │  if any.]
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 2  │ 0:0X.X - 0:0X.X  │ [SCENE TITLE]         │ [SHOT TYPE]        │ [Line or empty]    │ Music: [genre]
    │                  │ [Action.]             │ [Framing.]         │                    │ SFX: [layer]
    │                  │ [Action.]             │ [Movement.]        │                    │ [Audio note]
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 3  │ 0:0X.X - 0:0X.X  │ [SCENE TITLE]         │ [SHOT TYPE]        │ [Line or empty]    │ [Audio]
    │                  │ [Beat]                │ [Camera]           │                    │ [SFX]
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
... [continue for all panels] ...
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 N  │ 0:XX.X - 0:XX.X  │ [FINAL SCENE TITLE]   │ [SHOT TYPE]        │ [Final line or     │ Music resolves.
    │                  │ [Final action.]       │ [Framing.]         │  empty]            │ SFX: [final].
    │                  │ [Emotional close on   │ [Slow push/pull or │                    │ [Optional final
    │                  │  the subject.]        │  hold on frame.]   │                    │  line.]
────┴──────────────────┴───────────────────────┴────────────────────┴────────────────────┴──────────────────

TOTAL RUNTIME: [RUNTIME SECONDS] SECONDS │ FORMAT: [ASPECT RATIO] [ORIENTATION] │ STYLE: [MOOD] │ DIRECTOR LOOK: [optional]
═══════════════════════════════════════════════════════════════════════════════

CHARACTER LOCK: [Role and what must not change across all panels — the frozen character sentence itself is authored in Phase 7 (`ident.frozen_sentence`), and wardrobe is written there, in the image and character-sheet prompts]
OBJECT LOCK: [The recurring object — material, marks, scale — only where one recurs; otherwise omit the line]
ENVIRONMENT LOCK: [Location, props, lighting, atmosphere — consistent across panels]
CONSISTENCY NOTES: [Color grade across all panels, same lens character, same atmospheric haze]
```

## 2.3 Filled example — Coffee story 15 seconds, 8 panels

```
═══════════════════════════════════════════════════════════════════════════════
SIFU COFFEE                              A light, surreal coffee dimension.
15-SECOND COMMERCIAL STORYBOARD (9:16)   Awaken your best.
═══════════════════════════════════════════════════════════════════════════════

CUT │ TIME             │ VISUAL / ACTION       │ CAMERA / SHOT      │ DIALOGUE           │ AUDIO / SFX
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 1  │ 0:00 - 0:01.8    │ AWAKENING             │ MEDIUM CLOSE-UP    │                    │ Soft ambient
    │                  │ Model lifts SIFU cup. │ Slight low angle.  │                    │ swell.
    │                  │ Steam rises.          │ Golden rim light.  │                    │ Gentle steam
    │                  │ World transforms.     │ Shallow DOF.       │                    │ hiss.
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 2  │ 0:01.8 - 0:03.5  │ COFFEE DIMENSION      │ WIDE SHOT          │                    │ Rising
    │                  │ Space opens up.       │ Slow dolly out.    │                    │ orchestral
    │                  │ Espresso rivers float │ Floating particles │                    │ texture.
    │                  │ around him.           │ surround him.      │                    │ Liquid whoosh.
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 3  │ 0:03.5 - 0:05.2  │ MILKY GALAXY          │ TOP-DOWN WIDE      │                    │ Whispered wind.
    │                  │ Milk and creamer      │ Spinning motion.   │                    │ Soft chime.
    │                  │ swirl into galaxy.    │ Slow motion.       │                    │
    │                  │ Beans orbit as stars. │ High contrast.     │                    │
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 4  │ 0:05.2 - 0:06.8  │ THE AROMA             │ CLOSE-UP           │                    │ Deep breath SFX.
    │                  │ He inhales deeply.    │ Side light.        │                    │ Warm airy pad.
    │                  │ Steam wraps like silk.│ Steam wisps front. │                    │
    │                  │ Pure satisfaction.    │ Soft focus.        │                    │
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 5  │ 0:06.8 - 0:08.3  │ FLOW OF FOCUS         │ FULL BODY          │                    │ Rhythmic riser.
    │                  │ Steps forward on      │ Low angle tracking.│                    │ Crisp liquid
    │                  │ stream of espresso.   │ Coffee streams     │                    │ flow.
    │                  │ Confidence in motion. │ flow past.         │                    │
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 6  │ 0:08.3 - 0:10.0  │ THE PERFECT POUR      │ EXTREME CLOSE-UP   │                    │ Rich espresso
    │                  │ Espresso pours slow.  │ Macro detail.      │                    │ pour.
    │                  │ Crema blooms.         │ Golden highlights. │                    │ Deep satisfying
    │                  │ Perfection captured.  │ Steam and crema.   │                    │ rumble.
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 7  │ 0:10.0 - 0:12.0  │ SIP. FUEL. INSPIRE.   │ MEDIUM SHOT        │                    │ Uplifting beat.
    │                  │ He takes a sip.       │ Slight push in.    │                    │ Heroic tone.
    │                  │ Energy ignites.       │ Backlight glow.    │                    │
    │                  │ Ready to create.      │ Beans in motion.   │                    │
────┼──────────────────┼───────────────────────┼────────────────────┼────────────────────┼──────────────────
 8  │ 0:12.0 - 0:15.0  │ AWAKENED              │ MEDIUM WIDE        │                    │ Music resolves
    │                  │ He stands calm in the │ Slow pull-out.     │                    │ warmly.
    │                  │ glowing dimension,    │ Warm rim light.    │                    │ Soft steam
    │                  │ cup in hand, steady.  │ Hold on frame.     │                    │ hiss, fade.
────┴──────────────────┴───────────────────────┴────────────────────┴────────────────────┴──────────────────

TOTAL RUNTIME: 15 SECONDS │ FORMAT: 9:16 VERTICAL │ STYLE: CINEMATIC, SURREAL, WARM GOLDEN TONE
═══════════════════════════════════════════════════════════════════════════════

CHARACTER LOCK: Male model, late 20s, short black hair, slim build, glowing skin, calm confident expression. Same identity across all 8 panels; the wardrobe is written in the image prompts.
ENVIRONMENT LOCK: Surreal coffee dimension with floating espresso ribbons, suspended coffee beans, warm golden light source, atmospheric haze, deep charcoal void background with amber highlights.
CONSISTENCY NOTES: Same WARM GOLDEN palette throughout. Same shallow DOF 85mm lens character. Same liquid particle atmosphere across all panels.
```

## 2.4 Rules for text-table output

1. **Use box-drawing characters** (─ │ ┼ ┐ ┘ ┌ └) for clean ASCII tables. They render correctly in markdown, plain text, and most chat windows.
2. **Equal column widths** within a row. Use spaces to pad. Visual/Action column gets ~23 chars, Camera column ~20, Dialogue column ~20, Audio column ~18.
3. **Wrap text within cells** at column width. Continue on next line with proper indent.
4. **Exactly N rows** — the count the brief asks for, or else the panel count formula from `storyboard-panel-architecture.md` (`board_arch.panel_count_runtime_formula`).
5. **On a story piece the last row is always a final story beat** that closes the story on emotion or action, never a logo, brand reveal, or end card — unless routing question 5 in the package's root `SKILL.md` names a required final frame; then the card overlays or follows the last story row, and the story beat stays. **On a commissioned advert, product video or brand film the last row carries the endline and lock-up** — its own row, with the emotional beat in the row before it, where the film has a separate end card; written into the last story row where the lock-up sits over the final live shot, as a feed piece usually does (`promo.end_card`). The board draws the rows the film has, never one it does not.
5b. **The columns are the master grid's, less the image cell.** A DIALOGUE column always sits between CAMERA / SHOT and AUDIO / SFX (line plus speaker), its cells empty where nobody speaks, exactly as in the assembly order above; on a piece whose words appear on screen rather than being spoken, it is headed ON-SCREEN TEXT for every row, and on a sung piece it is headed LYRIC (the sung line, with the singer where there is more than one). Both templates above draw it. List in AUDIO / SFX only the music and sound the scene actually has.
6. **Footer with technical specs** matching SIFU layout exactly.
7. **Append Lock blocks** at the bottom (CHARACTER LOCK, OBJECT LOCK where a recurring object carries the piece, ENVIRONMENT LOCK, CONSISTENCY NOTES) — these are unique to text-table mode.
8. **Fence the table in a code block.** A box-drawn table keeps its columns only in a monospace block; outside a fence Markdown collapses the padding. A plain-text destination may take it unfenced.
9. **Color hex codes optional** — if mood matters, add a line under footer: "PALETTE: #0A0805 + #D4A55C accents + #F0E6D2 text"
10. **Direction/mood block at end** acts as production note for whoever generates the video/images.
11. **Right-to-left lines (Arabic, Syriac, Hebrew) break a box table's alignment** in most monospace renderers, because bidirectional text reorders the padding. Keep the table left-to-right and put each right-to-left line under it instead: the DIALOGUE / LYRIC cell carries the line's cue (`L1`, `L2`), and a numbered list after the table gives each line in full, in its own script, keyed to that cue and its CUT number.

## 2.5 When user asks for both modes

If user wants visual AND text:
1. First build the visual deck (the Master deck assembly specification above)
2. Then output the text-table (§2)
3. They mirror each other in content but differ in delivery format

## 2.6 Multi-part text storyboards

If user wants the storyboard split (e.g., "2 text tables covering 0:00-0:15 and 0:15-0:30"):
- Output 2 separate text-table blocks
- Each with its own header labeled "PART 1 OF 2" / "PART 2 OF 2"
- Continue panel numbering across parts (1-4 in part 1, 5-8 in part 2)
- Each part has its own complete header + table + footer
- Last panel of last part = final story beat (no logo, no brand reveal) — or, on a commissioned advert, product video or brand film, the endline and lock-up, drawn as rule 5 of §2.4 says

---

<a id="51-character-sheet-image"></a>
# 3. CHARACTER SHEET IMAGE TEMPLATE (Museum-Catalog Turnaround Style)

The authoritative panel schema lives only in
[`../phase-07-image-prompt-engineering/sheet-character.md`](../phase-07-image-prompt-engineering/sheet-character.md):
`CHARACTER_SHEET_SCHEMA: full_body=front,back,left_side,right_side; face=front_neutral,smile_open_mouth,three_quarter_left,three_quarter_right`.
Build the presentation from those eight required cells plus its accessories and palette. Labels and
identity text are typeset in the layout layer under `text_owner: built`; this deck does not restate
or redefine the panel set.

---

<a id="52-location-sheet-image"></a>
# 4. LOCATION SHEET IMAGE TEMPLATE (Uruk Style)

The full location sheet workflow lives in [`../phase-07-image-prompt-engineering/sheet-location.md`](../phase-07-image-prompt-engineering/sheet-location.md). This is the deck's presentation version of it. The image prompt template:

```
Create a location reference sheet poster in 16:9 horizontal landscape, dark moody charcoal background or cream depending on scene mood ([USER PICK]).

HEADER: LEFT small caps "LOCATION SHEET" | CENTER large serif "[LOCATION NAME]" typeset uppercase | RIGHT serif "[PROJECT TITLE]" + "[EPISODE/TIME OF DAY]"

ROW 1 — 4 equal cells showing the same location from 4 angles:
1. HERO WIDE (full establishing dramatic angle, deep focus)
2. REVERSE ANGLE (camera flipped 180°)
3. DOORWAY DETAIL (mid shot, focal architecture)
4. CAMERA CORNER (alternative shooting angle)
Labels in tiny serif caps below each: HERO WIDE, REVERSE ANGLE, DOORWAY DETAIL, CAMERA CORNER

ROW 2 LEFT (60% width):
Hero shot, final wide cinematic plate, matching the time of day and weather

ROW 2 RIGHT (40% width):
SET DETAILS grid 4x2, 8 close-up texture and prop cells, each isolated and captioned in tiny serif caps below: [LIST 8 DETAILS WITH MATERIAL NAMES]
Section header "SET DETAILS" at top right of this column

BOTTOM STRIP:
8 color swatches captioned in tiny serif caps: [LIST 8 COLOR NAMES]

[LOCATION DETAILS]:
- Name: [LOCATION NAME]
- Setting / era: [DATE]
- Architecture / materials: [WALLS, FLOORS, ROOFS, WINDOWS, DOORS]
- Atmospheric: [TIME OF DAY, WEATHER, LIGHT SOURCES]
- Practical lights visible: [TORCHES, LAMPS, FIRE PITS, WINDOWS]
- Flora / props: [PLANTS, JARS, FABRICS, TOOLS]
- Mood: [EMOTIONAL TONE OF THIS LOCATION]

[RENDER MODE] cinematic quality, the same value used on the deck. Consistent color grade across all 4 angle plates. Museum-catalog presentation.

Typography: elegant serif headers, tiny serif caps labels, clean alignment, generous margins.

AVOID: modern signage, anachronistic objects, cluttered text, broken letters, inconsistent lighting between plates, distorted geometry, watermarks. LAYOUT LOCK: reproduce the full sheet (4 angle-plate row, large hero plate, set-details grid, color palette strip), never collapse to a single establishing shot and never drop a section.
```

---

<a id="53-props-sheet-image"></a>
# 5. PROPS SHEET IMAGE TEMPLATE (Palace Style)

The full props sheet workflow lives in [`../phase-07-image-prompt-engineering/sheet-props.md`](../phase-07-image-prompt-engineering/sheet-props.md). This is the deck's presentation version of it. The image prompt template:

```
Create a set dressing reference sheet poster in 16:9 landscape format, on warm dark background (#1A0F08) or cream depending on the location mood.

HEADER: LEFT "SET DRESSING SHEET" | CENTER serif "[LOCATION NAME] DECOR & PROPS" | RIGHT "[PROJECT TITLE]" + "[SCENE TITLE]"

ROW 1 — 4 mood cells:
1. ROYAL/INTERIOR MOOD (full wide of dressed space)
2. ARCHITECTURAL DETAIL (close on relief, column, carving)
3. CEREMONIAL OBJECTS (still life of key ritual props)
4. TEXTILES & FURNISHINGS (cushions, drapes, rugs)

ROW 2 LEFT (40%): large hero interior shot, all props in place
ROW 2 RIGHT (60%): PROP DETAILS grid 6x3 = 18 prop close-ups, each captioned

BOTTOM: 10-11 color + material swatches with captions

[INCLUDE FULL PROP LIST AND MATERIAL LIST FROM PROJECT BIBLE]

[RENDER MODE] cinematic museum-catalog quality, the same value used on the deck. Consistent lighting on all props. Typography matches character sheet style.

LAYOUT LOCK: reproduce the full sheet (4 mood-cell row, large hero interior plate, the prop-detail grid, color and material palette strip), never collapse to a single interior shot and never drop the prop grid.
AVOID: a single-image output, a missing prop grid, broken letters, watermarks, cluttered text.
```
