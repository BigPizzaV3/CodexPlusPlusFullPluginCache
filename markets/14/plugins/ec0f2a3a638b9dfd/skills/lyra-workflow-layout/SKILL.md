---
name: lyra-workflow-layout
description: "Use whenever a Lyra workflow is created or edited, and for \"tidy up the canvas\", \"sign the sections\", \"make the workflow clear\", \"add notes for the user\", \"the canvas is confusing\", \"lay it out like the templates\". Lays out nodes in sections in run order with STEP notes, the team's color code and clear labels."
---

# lyra-workflow-layout

Helper skill for every Lyra skill. The other skills decide **what** to build; this one decides **how it reads on the canvas**. Every workflow Claude builds or changes is laid out by this file.

**The goal.** Anyone who opens the workflow (the user tomorrow, a teammate, a client) understands in ten seconds what it makes, in which order it runs, and where to change something by hand. A canvas of unlabelled nodes in one row is a black box. A canvas split into colored sections, each with its own small STEP note, reads like a recipe, the way Lyra's own templates do: first the idea, then what the user brought, then the heroes, the scenes, the clips, and the final video.

**Who decides what.** The creative skill decides which sections its creative needs (its "Layout" lines). This file decides how they are placed, numbered, explained, colored, labelled and checked. The user's explicit wishes win over both.

**This is a way of thinking, not a script.** Use judgment when a canvas needs something different, and say why in one line. Fixed: every node in a section, one STEP note per section, steps in run order, the color code, labels a person understands, no empty or stray nodes, and Lyra's technical limits below.

---

## The house style: how Lyra's templates are laid out

Lyra's templates (Creators workspace, Templates) are made by the creative producers, and they all follow one pattern:

- **A reading path.** The script on the left, the work sections in the middle stacked top to bottom, the Video Editor on the right. The eye goes left to right, and top to bottom inside a column.
- **A small STEP sticky note above every section**, in the section's color, numbered in the order the user goes through it:
  - "STEP 1 · Check the script"
  - "STEP 2 · Insert a screenshot/video of your app."
  - "STEP 3 · Generate Image & Video"
  - "STEP 4 · Generate Music · You can create your own music and combine it with the video in the Video Editor"
  - "STEP 5 · Combine scenes"
- **Each note is short:** the step number, a 2 to 5 word action, at most one helper sentence. Plain instructions, no explanations of the tech. One note per section, never one big note with all the steps.
- **Color by kind of step:** lime for the script, pink for the user's own app assets, violet for every generation, rose for the final assembly.
- **One section per kind of work, with its nodes side by side**, flowing left to right inside it.

The templates also have slips that Claude's canvases never repeat: "Gerate", duplicate or missing step numbers, a STEP 0, "STEP 3&4", notes in the wrong color, "(copy)" and "Note (" labels, the editor called Composer in one note and Video Editor in the next, a "Generate Music" note in a workflow with no music node, empty leftover notes and empty upload nodes.

---

## What the tools can do (Lyra, Oct 2026)

Re-check at the start of a build: tools change.

| Need | How | Notes |
|---|---|---|
| A section | `create_frame_node` (workflow_uuid, node_uuids, label) | The label is the section's title, shown in one line above it. **The size is fixed at creation** from where its nodes are at that moment, plus padding; it never shrinks later. So place the nodes first, create the frame second. |
| Section color | `update_node` on the frame: `{"note_style": {"background_color": "#c4b5fd80"}}` | Width and height can't be set. |
| Add nodes to a section later | `update_node` on the frame: `{"node_uuids": [the full list]}` | The whole list. If the section must change size, delete the frame (its nodes stay) and create it again. |
| A STEP sticky note | **Not in the MCP tools.** In a browser signed in to Lyra: the **+** button in the bottom toolbar → Tools → **Note** adds one. Then `update_node` on the note: `{"content": "…", "note_style": {"background_color": "…"}}` | The note's size stays 240×200, enough for a STEP note. Existing notes (in a workflow from a template) are edited the same way. |
| Positions | **Not in the MCP tools.** In a browser signed in to Lyra, a short script on the workflow page can move nodes through the canvas's own change handlers (`onNodesChange` with position changes, then `onNodeDragStop` with the moved nodes); Lyra saves it like a drag. Read the nodes' sizes from the page first | New nodes otherwise land in one row in creation order. Keep the user's tab off the workflow while the MCP tools edit it, and close the page before MCP edits, or the page can save an older canvas over them. |
| Tidy automatically | The **Organize nodes** button (bottom toolbar, four squares) | Lays the graph out by its connections. Unconnected nodes (the script, notes) go to the end, so the script lands far from the start and **notes are thrown to the edges**. Use it only on a canvas without notes and only when hand placement isn't possible. |
| A text card | `create_user_text_node` | A real text node: never connect it to anything, or its text feeds the next node. Only the fallback for a STEP note when no browser is available. |
| Run one step | The **Run** button on a section's top right corner | Runs every node of that section. |
| Remove an empty or stray node | `delete_node` | Only nodes that hold nothing and feed nothing (an empty upload), or Claude's own leftovers; say which in the report. Anything with content: ask first. |

---

## Layout: the reading path

Place the sections on a grid, like the templates:

```
 column L          column M1                  column M2                 column R
┌───────────┐   ┌─────────────────────┐    ┌─────────────────────┐   ┌──────────────┐
│ note ST1  │   │ note ST2            │    │ note ST6            │   │ note last    │
│ SCRIPT    │   │ YOUR APP (pink)     │    │ KEYFRAMES           │   │ VIDEO EDITOR │
│ (lime)    │   ├─────────────────────┤    ├─────────────────────┤   │ (rose)       │
└───────────┘   │ note ST3            │    │ note ST7            │   └──────────────┘
                │ CAST                │    │ CLIPS               │
                ├─────────────────────┤    ├─────────────────────┤
                │ note ST4  PLACES    │    │ END CARD · MUSIC    │
                └─────────────────────┘    └─────────────────────┘
```

- **Column L:** the idea: script, brief, concept card (lime), at the top.
- **Middle columns:** the steps in order, top to bottom, then the next column: the user's own materials first (pink), then the heroes, the places, keyframes, clips, end card, voiceover, music.
- **Column R:** the Video Editor or the final outputs (rose), at the height of the clips.
- **Each section:** its STEP note on top (left-aligned with the section, ~40 px gap), then the section with its nodes in one row, left to right in their own order (keyframe → clip, clip 1 → clip 4). More than 5–6 nodes → two sections ("Clips 1–3", "Clips 4–6").
- **Spacing:** 40 px between nodes, ~140 px between a section and the next note below it, columns wide enough that nothing overlaps (a row of 4 image nodes is ~1600 px).

---

## Sections

1. **One section per step of work, in run order.** Every node sits in exactly one section. Nothing floats outside, nothing is kept "just in case".
2. **One STEP note per section**, above it, in the section's color. Numbering STEP 1, 2, 3… with no gaps, no repeats, no STEP 0, no "3&4", no "2.1".
3. **The section title is short**, because the note carries the step: "Story script", "Your app & style", "Cast", "Keyframes", "Video clips 1–3", "Music", "Video Editor".
4. **Size:** 1 to 6 nodes per section. A section with one node only for the script, the Video Editor, the music or a single upload.
5. **Never** the whole graph in one section, never a section per node, never an "unused" section: empty nodes are removed (see the tools table), real content gets a real step.

### Color code

Always the 50% transparent hex (ending in `80`). The note and its section have the same color; the same kind of step has the same color across the canvas.

| Color | Hex | Kind of section | What goes in |
|---|---|---|---|
| Lime | `#bef26480` | The idea, text to read and check | Script, brief, concept card, story, hook bank, carousel script, Text Split |
| Pink | `#f9a8d480` | The user's own materials | Screenshots, logo, app icon, packshot, end card or app video, product photo, style reference, brand assets |
| Violet | `#c4b5fd80` | Generation | Characters, places, keyframes, phone shots, clips, voiceover, music, Image Resize, Image Translation |
| Rose | `#fda4af80` | The result | The Video Editor; the final ads or sizes the user downloads |
| Slate | `#cbd5e180` | Reference kept for analysis (nothing runs) | A competitor's ad, a teardown, prompt tips, when the creative needs them |

### STEP notes

The pattern, the same as the templates:

```
STEP 2

Your app & style

Added: Lull Home screen, Lull logo and the art style reference. Swap them to change the app.
```

- Line 1: `STEP N`. Line 3: the action in 2 to 5 words ("Check the script", "Our heroes", "Generate keyframes", "Generate video", "Generate music", "Combine scenes"). Line 5: one sentence: what's in the section or what the user can do ("You can…", "Edit a prompt and press Run.", "Added: …").
- For the user's materials, the note lists what was added ("Added: logo, 3 screenshots").
- In the user's language (English when the canvas and the audience are English); the words the user sees in Lyra: section, node, prompt, Run, Video Editor, Edit Video, Render. Never tool names, uuids or connection roles.
- Short: it must fit 240×200 without scrolling.

**Examples** (video): "STEP 1 · Check the story script · The idea, every line of dialogue and the timing of all clips." · "STEP 3 · Our heroes · Emma and Dan. Every scene uses them as references." · "STEP 5 · Generate keyframes · One image per clip. Edit a prompt and press Run." · "STEP 7 · Generate music · You can create your own music and combine it with the video in the Video Editor." · "STEP 9 · Combine scenes · Open Edit Video to trim and add captions, then Render."

### Standard sections by creative

The creative skill's own Layout lines say which sections it needs; these are the defaults.

| Creative | Sections in reading order (color) |
|---|---|
| Video ad (base, UGC, short drama, UI motion) | Script (lime) → Your app (pink, when there are uploads) → Cast (violet, when there is a person) → Places / Keyframes → Clips → Voiceover → Music (violet) → Video Editor (rose) |
| Hooks | Hook bank and script (lime) → Your app (pink) → one section per hook with its keyframe and clip (violet) → shared body, voiceover, music → the Video Editors (rose) |
| Short drama | Story (lime) → Your app & style (pink) → Cast → Places → Phone shots → Clips per act → End card → Music (violet) → Video Editor (rose) |
| Static ads | Concept (lime) → Your app (pink) → Persona / product (violet) → Ads (violet, or rose when last) → Sizes and languages (rose) |
| Carousel | Story and Text Split (lime) → Your app and persona → Cards in one row in card order (rose when last) |
| Competitor copy | Competitor reference, analysis only (slate, first, its own note "Reference · not connected") → the normal set |
| Variations, multiplier, audience variations | The original layout kept in each variation; notes and labels updated where the person, setting or angle changed |
| Resize, translation added later | A new section with the next STEP number, placed after the last step |
| Brand Kit starter | Brand assets (pink) · Brand Kit notes: app card, pain map, open questions (slate) |

---

## Node labels

- **Say what it is and where it belongs:** "Scene 2 · app demo · keyframe", "Scene 2 · app demo · clip", "Character · Mia", "Screenshot · timer screen", "Logo", "VO · full script", "Music · lo-fi", "Hook A · clap + pain · clip", "Ad C1 · 2 am POV · 4:5", "Card 3 · fix · 4:5".
- **Default labels only for the single node of its kind:** "Video Script", "Music Brief", "Voiceover Script", "Video Editor". The final assembly node is always called **Video Editor**.
- **No step numbers in node labels** (the note carries the step), no "(copy)", no "Image 1", no "Upload Image", no empty label.
- **One pattern per kind of node**; the same scene, card or hook number in its keyframe, clip and caption.

---

## Build order

1. **Plan.** The plan table (the base skill's Step 2) gets a Section column; the approval message lists the steps in one line ("STEP 1 Script → STEP 2 Your app → STEP 3 Cast → … → Video Editor").
2. **Nodes and connections** as the creative skill says. Remove Claude's leftovers and empty nodes.
3. **Notes:** one per section. In the browser: **+** → Note, once per section; then close the workflow page and set each note's text and color with `update_node`.
4. **Positions:** open the workflow, place every note and node on the grid (Layout above) with the page script, check that it saved (reload), close the page.
5. **Sections:** `create_frame_node` for each section **after** its nodes are in place, then `update_node` for its color. Notes stay outside the frames, above them.
6. **Look:** open the workflow, Fit view, screenshot, check the reading path and that nothing overlaps.
7. **Check** (below), fix, check again.
8. **Report** the steps in the chat with the same words as the notes, plus what the user does next.

**No browser available** (only the MCP tools): put a text card with the STEP text as the first node of each section (label "STEP N"), create the frames, and tell the user once: "Press Organize nodes in the bottom toolbar, then drag the Script section to the left." Offer to finish the layout when a browser is available.

---

## Templates, variations and the user's own workflows

**A workflow made from a template (`use_template`).** Keep the template's own layout: its notes and sections were placed by the producers. Fix the notes with `update_node` (typos, continuous numbers, colors from the code, "Video Editor", notes that no longer match their nodes). Never press Organize nodes there. Nodes Claude adds get their own note and section, placed at the right step with the page script.

**Variations** (`create_variation`) copy the whole canvas with its layout. Keep it; update the notes and labels that name what changed. Each variation has its own nodes: lay out each one.

**The user's own workflow.** Don't rearrange or delete without asking; add Claude's nodes in new noted sections and offer the tidy-up in one line.

**Follow-ups on a workflow Claude built** (a new hook, a size, a language): a new note and section with the next STEP number, placed after the last step.

---

## Check before handing over

`get_workflow` and a screenshot:
- [ ] Every node that isn't a frame or a note appears in exactly one frame's `node_uuids`.
- [ ] One note per section, above it, same color; STEP 1 to N continuous, in reading order.
- [ ] The script section is first (left, top); the Video Editor last (right).
- [ ] No empty nodes, no "unused" section, no one big note with all the steps.
- [ ] No "(copy)", "Image 1", "Upload Image" or empty labels; the editor is "Video Editor".
- [ ] Text cards (if any) are connected to nothing.
- [ ] Nothing overlaps; every section hugs its nodes (no big empty frames).
- [ ] All connections, prompts and results the same as before the layout.

## Common mistakes

- One big note with every step instead of a note per section.
- Organize nodes on a canvas with notes, or the script left wherever Organize put it.
- Frames created before the nodes are placed (they keep the old, huge size).
- An "unused" section full of empty uploads.
- Editing through MCP while the workflow page is open (the page saves an older canvas).
- STEP 0, gaps, repeats, "3&4"; a note that says one thing while the nodes do another.
- Step numbers in node labels; titles in a language the user doesn't use.
