---
name: lyra-workflow-review
description: "Use when the user asks about an existing Lyra workflow, e.g. \"review my workflow\", \"explain this workflow\", \"what does this workflow do\", \"why doesn't it run\", \"is anything broken\", \"check my canvas\", \"how much to rerun it\", \"how much does this template cost\", \"audit this workflow\", or a Lyra workflow link with a question. Explains it, finds problems, prices reruns and fixes on request. Read-only by default."
---

# lyra-workflow-review

Core skill for reading a Lyra workflow the way a creative producer would. The creative skills build workflows; `lyra-fix` repairs one part of a finished ad; `lyra-workflow-layout` decides how a canvas reads. This one opens any workflow (the user's own, a teammate's, a template copy, one Claude built last week), says what it does, what is wrong with it and what a run costs, and only then offers to change anything.

**The goal.** The user sends a link and gets back, in one message: what this workflow makes, its steps in order, a short list of problems with how to fix each one, and the price of running it all again or only a part. Nothing on their canvas has moved.

**Core rules come from the base skills.** Credits, pre-run check, picking a result, links and the open canvas rule live in Part 1 of `lyra-video-ad-generation` (video) and `lyra-static-image-generation` (images). Canvas rules (sections, STEP notes, colors, labels) live in `lyra-workflow-layout`. Fixing a scene or an image goes to `lyra-fix`. This file only adds what is specific to a review.

**This is a way of thinking, not a script.** Fixed: read before saying anything, plain words, every problem with its fix, prices from the nodes, never guess a result you haven't seen, and the hands-off rule below.

---

## The hands-off rule

A review **reads**. It does not change the workflow.

- **A workflow Claude did not build in this chat** (the user's own, a teammate's, a template copy, an older one): nothing is deleted, moved, renamed, reconnected, rerun or tidied without the user's yes to that exact change. Not even an empty upload node, not even a typo in a note.
- **A workflow Claude built in this chat:** Claude may fix its own leftovers (an empty node, a lost connection) and say so in one line; anything the user touched stays as they left it.
- **A yes covers what was listed,** nothing more. "Fix the connections" is not a yes to tidy the layout.
- **Big changes go into a variation** (`create_variation` "{name} · review fixes", `switch_variation`) so the original stays as it was: a tidy-up of the whole canvas, deleting nodes, changing many prompts. Offer it in the same message; small fixes (one setting, one connection) can go in place.
- **What the tools do behind the scenes** (say it before the yes, not after):
  - `switch_variation` makes that variation the one Lyra shows and runs **and renames the whole workflow after it**. After the work, say which variation is now main and offer to switch back.
  - `delete_node` **cannot be undone** and also clears every frame or reference setting that used the node. Content is never deleted without a yes naming the node; when in doubt, disconnect instead of deleting.
  - `disconnect_nodes` clears the target's frame or reference settings that used the source: name them in the plan.
  - `update_node` keeps old results; nothing is lost by changing a setting, but the old prompt is overwritten: quote old → new in the report.
- **Never run nodes to check them.** A run costs credits; a review costs nothing.

---

## Step 1. Find and read the workflow

1. **Which workflow.** A link `app.lyra.splitmetrics.com/workflows/{uuid}` (or the older `lyra.splitmetrics.com/workflows/{uuid}`) → the uuid. A name → `list_workflows` with `search`; several matches → list them (title, last updated) and ask which. Nothing given → the most recently updated one, named in the first line so the user can correct it.
2. **Which variation.** `get_workflow` reads the main variation. If the user is asking about another one (`list_variations`), `switch_variation` only with their yes, because it changes which version Lyra shows and runs and renames the workflow after it; otherwise review the main one and name it.
3. **Read it now, not from memory:** `get_workflow` (nodes, `data`, `is_valid`, `validation_error`, `credits`, `estimated_generation_time`, edges, the Video Editor's `video_rendering_composition`), `list_workspaces` (credits), `list_node_configs` (models and allowed settings), and the Brand Kit if one is assigned (`brand_kit_uuid`; `null` = no kit, say so). There is no tool to read one kit by its uuid: find it in `list_brand_kits` (page through) by `uuid`.
   - **Which balance.** Lyra works in the workspace the user last selected, and `list_workspaces` doesn't mark which one that is (and can fail: "Could not load workspaces"). With a browser, read it off the Lyra sidebar: the workspace name at the top, **Credits** at the bottom. Otherwise: one workspace → its credits; several → name the one you assume ("balance in {workspace}") or ask once; never show a number from another workspace as "your balance".
   - **The Video Editor** is the node with `action: video_composer`, whatever its label ("Video Composer", "Video Editor", or a custom name).
4. **A big canvas.** A library canvas with many creatives can return 60 000+ characters and come back as a saved file. Read all of it (jq or a short script), never review from the part that fit. Count nodes by type first to see what you're dealing with.
5. **Several creatives on one canvas.** Split the graph into groups that are connected to each other (each usually ends in its own Video Editor or final images). Name each group from its section title or STEP notes. First send a short list: each creative in one line (what it makes, its node count, the number of problems found, its full rerun price), plus the nodes connected to nothing. Then ask which ones to review in full, and review each picked group as its own creative (Steps 2–5).
6. **Results and pictures.** `get_workflow` does not list each node's results, and no tool lists them without a run uuid. What `get_workflow` does show:
   - the Video Editor's composition: every clip on a track has `sourceNodeId` and `sourceResultUuid`; **no `video_rendering_composition` at all = the Video Editor was never opened or assembled**. Read the clips' ids only: a track has its own `sourceNodeId` too, which doesn't point to a node. **A copied edit:** a workflow made from a template (or copied) can carry the template's whole edit, with clip `sourceNodeId`s that are not nodes on this canvas and asset urls from the template's runs. None (or almost none) of the clip ids on the canvas → one finding, not one per clip: "the edit was copied from the template and shows the template's video; it needs re-assembling after this workflow's own runs". A clip id that is on the canvas means the edit used that node's result at some point, not that the node has a result now;
   - frames in `image_inputs_usage`: `image_result_uuid` (a pinned result) or `null` (Lyra's selected one);
   - uploads: `files` with the file's url and name; **no `files` = an empty upload**;
   - nothing else.
   For generated nodes, open the workflow in a browser signed in to Lyra (read only, nothing clicked): a screenshot after Fit view shows which nodes have an image, video or audio result; `get_page_text` returns the text results (the script a Video Script node wrote, with its scenes, timing and lines), every prompt, the count on each node ("x1") and the run history ("3 runs"). Read the text result before explaining what a script node makes. No browser → ask the user. Never write "no result" for a node you couldn't see: write "not checked".
7. **Open canvas.** Reading is safe with the workflow open. Before any edit later (Step 6), the workflow page must be closed: with a browser under Claude's control, move the tab off the workflow while editing and open it again at the end to show the result; otherwise ask the user to switch their tab away.

---

## Step 2. Explain it in plain words

Build the picture from the edges, not from the node list order (that is creation order, not run order).

1. **What it makes.** The last node(s): a Video Editor → one video ad of {length} s in {ratio}; image nodes with nothing after them → {N} images; several Video Editors → {N} videos (hooks, versions). One line.
2. **The run order.** Sort the nodes by their edges: sources first (uploads, scripts, text), then what takes from them, the Video Editor last. Group by section when there are sections (a frame's `node_uuids`), in the order of the STEP notes when they exist.
3. **Each step in one line,** in the user's words, not the tech:
   - what goes in and what comes out ("a photo of the heroine on the sofa → it becomes the first and last frame of the video");
   - the model in plain words, by its name in `list_node_configs` ("Nano Banana Pro, the most realistic image model", "Kling 3.0 Pro, 10 s with its own sound");
   - what the user can change there ("her outfit is in this prompt").
4. **The user's own materials:** uploads, screenshots, logo, the Brand Kit, and what each one feeds.
5. **Text on the canvas.** Three kinds, say which:
   - **Note** (`action: note`, the sticky note with "Write a note..."): can't be connected to anything and never changes a generation. STEP notes and tips live here.
   - **User Text** (`user_text`, free): text written by a person. Connected to a generation node (image, video, audio, another text node), it goes into that node's generation as it is: say "this text feeds {node}". It still doesn't keep a character consistent by itself; that comes from the character image connected as a reference.
   - **Text generation nodes** (Video Script, Voiceover Script, Music Brief, Creative Analysis, Character Prompt, Text Split…: they have a `model_name` and `credits`): a language model writes a new text from the node's prompt and its inputs, and that text goes to the next node. The prompt on the canvas is the instruction, not the final words; the real text is the node's result. Rerunning it writes a new text.
   A User Text or text generation node connected to nothing is only for reading, like a Note.
6. **Short.** 5 to 10 lines for a normal workflow. Long prompts are summed up in a few words, never pasted. Text only, no diagram: the canvas already shows the connections.

> **Microphone UGC** makes one 10 s vertical UGC video with music.
> 1. **Script** (Video Script, GPT): from the brief (she taps her microphone once and says a 3-line testimonial) it writes the video's prompt.
> 2. **The heroine** (Image G/ STEP 1, Nano Banana Pro): her on a beige sofa in a sunny living room, holding a clip-on mic.
> 3. **Second frame** (Image G/ STEP 2): the same shot, her finger on the mic; made from image 1.
> 4. **The video** (Video G/ STEP 3, Kling 3.0 Pro, 10 s with sound): starts on image 2, ends on image 1, speaks the script.
> 5. **Music** (lo-fi, 10 s) and **Video Composer** (the Video Editor): the clip with the music under it at 26%.
> (The edit was most likely copied with the template: the workflow was never updated after it was created. And the labels say STEP 3 for the video while the notes put image and video together in STEP 2: both go to Problems.)

---

## Step 3. Find the problems

Go through every check. Each problem gets: **where** (the node label, in quotes), **what** in plain words, **why it matters**, **the fix**, and its weight:

- **Blocks** — the node won't run, or runs with something missing.
- **Wastes credits** — it runs, but spends on nothing or makes the wrong thing.
- **Confusing** — it works, but a person reading the canvas gets lost.

### Connections

| Check | How to see it | Weight |
|---|---|---|
| An edge to or from a node that no longer exists | edge uuid not in `nodes` | Blocks |
| A frame or reference set but not connected | `image_inputs_usage.first_frame / last_frame.node_uuid` with no edge from that node | Blocks |
| A pinned result that's gone | `image_result_uuid` set, the source node rerun or cleared (check in the browser) | Blocks |
| A video node that needs images but gets none | `use: frames / references`, no image edge in | Blocks |
| Frames chosen, but no frame set | `use: frames`, `first_frame` and `last_frame` both `null` (Lyra still says valid) | Blocks |
| An image connected to a video with no role | an image edge in, no `image_inputs_usage` on the video node: the model decides (most start from the image) | Confusing (say what will likely happen; offer to set frame or reference) |
| The Video Editor uses a clip from a node that is gone or disconnected | a clip's `sourceNodeId` not in `nodes`, or in `nodes` but not connected (all of them gone → the copied edit, Step 1.6: one line) | Blocks (that clip is a dead copy) |
| A node is connected to the Video Editor but not in the edit | edge in, no clip with that `sourceNodeId` | a paid node: Wastes credits (paid, not used) · an upload: Confusing (often an optional logo or screenshot slot) |
| A text node connected by accident | a script, brief or note-like text feeding a generation node it shouldn't (its text becomes the prompt) | Wastes credits |
| Two prompts fight | the node has its own prompt and a text node feeds it too, with different content | Wastes credits |
| A dead end | a paid node that feeds nothing and isn't a final output. Final outputs: every Video Editor; in a creative with no Video Editor, the last image or video nodes. In a creative that has a Video Editor, a clip, voiceover or music with nothing after it is a dead end | Wastes credits (ask: an alternative take kept on purpose?) |
| An island | a group of nodes connected to nothing else on the canvas | Confusing (ask: kept on purpose?) |
| Wrong order | scene, card or hook numbers in the labels out of order along the edges ("Scene 3" feeds "Scene 1 · clip"), or clips in the edit not in the order of their numbers | Confusing or Wastes credits |

### Invalid nodes

**`is_valid: true` is not enough.** Lyra's check misses a lot: an upload with no file, a node with no prompt, and a setting value the model doesn't list (e.g. `duration: -1` on Seedance 2.5, which takes `"adaptive"`) all come back valid. Check every node against `list_node_configs` yourself.

| Check | How to see it | Weight |
|---|---|---|
| `is_valid: false` | read `validation_error` and translate it ("no resolution set", "this model doesn't take a last frame") | Blocks |
| A model Lyra no longer offers, or a setting not in `list_node_configs` | compare `model_name` and every value with the model's allowed ones. When `list_node_configs` contradicts itself (Seedance 2.0: the description allows `-1`, the minimum says 4), mark it "unverified", not Blocks | Blocks |
| `credits: null` on a paid node | a setting is missing (e.g. no resolution) | Blocks |
| The model can't use what it's given | read the model's parameters in `list_node_configs`: references on a model with no `reference_images` (Kling 3 Pro, Veo 3.1 Fast, Sora 2) · frames and references together (Seedance: one or the other) · a last frame without a first frame · Veo 3.1 references with a ratio other than 16:9 or a length other than 8 s · a motion-control model without its reference video · a Sora first frame in another ratio than the video · a ratio set on a model that ignores it when a first frame is given (Kling) | Wastes credits (the input is ignored) or Blocks |
| Settings don't fit together | a 16:9 clip from a 9:16 frame · a clip shorter than its voiceover · music shorter than the video · the Video Editor canvas a different ratio or length than its clips | Wastes credits |
| A voiceover with no voice or language chosen | no `voice` / `language_code` in `data` (Lyra's default voice will be used) | Confusing (ask if that's on purpose) |
| The prompt says one thing, the settings another | "10-second" in the prompt, `duration: 5`; "vertical" with 16:9; "no music" with music connected | Wastes credits |
| A clip where someone speaks has no music ban | speech in the clip (a spoken line in the script or prompt, `generate_audio: true`) and no "no music, no background music" sound line: the model may lay its own music under the voice, which can't be removed (`lyra-video-ad-generation` → Reference C) | Wastes credits |
| Speech that doesn't fit the clip | the lines in the script (its text result) need more time than the clip's `duration` at a calm pace (~2.5 words/s) | Wastes credits |
| A prompt or script asks for something that isn't there | "use the provided voiceover script" with no voiceover node; "the logo from [Image2]" with one image connected | Wastes credits |

### Empty nodes

| Check | How to see it | Weight |
|---|---|---|
| An upload with no file, connected to something | no `files` in `data` | Blocks (or a blank layer in the edit) |
| An upload with no file, connected to nothing | no `files`, no edges | Confusing |
| A generation node with no prompt and no text fed in | no `prompt` in `data`, no text node edge in | Blocks |
| A text generation node with no prompt | it writes from its inputs only; say what it will write from | Confusing |
| An empty note, an empty section (a frame with no `node_uuids`), a User Text with no text | | Confusing |
| An ad with no app | no Brand Kit, no app name in any prompt, and the script talks about "the app" | Wastes credits (the ad sells nothing) |
| A placeholder left in a prompt: "[App Name]", "(app name)", "{product}", "<app>", "TBD", "XXX", "Lorem" | search every `prompt` and note, case-insensitive, even when a Brand Kit is assigned (the kit doesn't fill a placeholder in a prompt) | Wastes credits (the model draws or says the placeholder) |
| Markdown left in a prompt (`**`, `*`, `#`) | search every `prompt` | Confusing (the model may read the stars literally) |

### Nodes without a result

| Check | How to see it | Weight |
|---|---|---|
| A node never run | the browser shows no result; no clip in the composition | — (say it; it's the cost in Step 4) |
| A node waits for an input that has no result | its source has no result | Blocks (run the source first) |
| The Video Editor was never assembled | no `video_rendering_composition` in `data` | — (say it: the video isn't made yet) |
| The Video Editor's edit is empty, or holds old clips | no clips on the tracks; or a clip's `sourceResultUuid` is an older take than the one picked on the node (browser) | Blocks / Confusing |
| A failed run | the browser shows an error on the node | Blocks (the fix by base Runtime failures) |

### Inside the edit (when there is a composition)

| Check | How to see it | Weight |
|---|---|---|
| A placeholder clip left in the edit | a "Text" or empty clip with no content | Confusing |
| Clips overlap on one track, or gaps between them | `startMs` + `durationMs` of neighbouring clips | Confusing |
| The edit is shorter than its clips, or music shorter than the edit | `canvas.durationMs` vs the clips; the music clip's `durationMs` | Wastes credits (cut off) |
| Music too quiet or too loud | the music track's `volume` against `lyra-video-editor` → Audio | Confusing (ask) |
| An older take in the edit | the clip's length doesn't match the node's `duration` now | Confusing |
| Old asset links | asset urls on another domain (e.g. `muse.splitmetrics.com`) | Confusing (check they still play) |

### Canvas (by `lyra-workflow-layout`)

Only the points that make the canvas hard to read; full layout checks belong to the tidy-up (Step 7). Typos in notes ("Gerate"), leftovers in note text (`&nbsp;`, `**`, a STEP pasted twice: "Combine scenesSTEP 5"), steps missing, repeated or out of order, a note that names a node that isn't there (a "Generate Music" note with no music node), the editor called Composer in one place and Video Editor in another, step numbers in labels ("Image G/ STEP 2"), default labels ("Upload Image", "Image 1", "(copy)"), nodes outside any section, overlaps. All **Confusing**.

### What a review does not judge

Whether the idea is good, the script is strong or a picture looks right is a creative opinion: give it only when the user asks, in a separate short block, or hand over (`lyra-result-check` to look at a finished video or image for defects, `lyra-fix` to repair one, the creative skill for a new angle). The Brand Kit: point out only a clear mismatch (another app's name in a prompt, a claim the kit forbids). **No Brand Kit** (`brand_kit_uuid: null`): say it in one line and offer in Step 5 to assign one (`list_brand_kits` → `assign_brand_kit`) or build it with `lyra-brand-kit`; assigning changes the workflow, so it waits for a yes like any fix.

---

## Step 4. What a rerun costs

Prices come from `credits` on the nodes (one run of the node; an Image Resize with two ratios already counts both). Never guess; a paid node with `credits: null` is priced "unknown until {setting} is set". A video on adaptive or auto length (`adaptive`, `-1`) is priced at the model's longest length (Seedance 2.5: 30 s, 855 credits at 720p): say "up to".

**Text nodes in a rerun.** Rerunning a text generation node (Video Script, Voiceover Script, Music Brief…) writes a **new** text, so everything after it can change, not only the picture. Price "everything" both ways when the workflow has text generation nodes: with the texts rewritten, and keeping the texts (only the media nodes). Keeping them is the default for "rerun the same ad".

1. **Everything.** The sum of `credits` of every node that generates (images, video, audio, resize, translation), without the text generation nodes by default (above), plus a second line with them. Skip: frames (a Section's `credits` is already the sum of its nodes; counting both doubles it), notes, uploads, user text, the Video Editor (free).
2. **By section.** The Section's `credits`, or the sum of its nodes when there are no sections, per step.
3. **From a node on.** For the parts the user is likely to redo (each clip, the character, the music): that node plus every node downstream of it along the edges, the Video Editor last. This is the price `lyra-fix` will quote, so the user sees it before they ask.
4. **Only what has no result yet** — when some nodes were never run: the price to finish the workflow.
5. **Time:** add up `estimated_generation_time` along the longest chain of nodes (nodes of the same stage run side by side), min to max. A Section's time is its slowest node, not the time of the whole section.
6. **Balance** of the right workspace (Step 1.3), and whether the full rerun fits.

> | Rerun | Nodes | Credits |
> |---|---|---|
> | Everything, same script | Heroine 23 · Frame 2 23 · Video 504 · Music 13 | **563** |
> | Everything, new script | + Video Script 1 | 564 |
> | From the heroine on | Heroine → Frame 2 → Video → Video Editor | 550 |
> | Only the video | Video → Video Editor | 504 |
> | Only the music | Music → Video Editor | 13 |
> Balance {X} in {workspace} · the full run takes about 3.5–6 min (heroine → frame 2 → video).

---

## Step 5. The review message

One message, in the user's language, in this order:

1. **The workflow:** name, link `https://app.lyra.splitmetrics.com/workflows/{uuid}`, the variation, the Brand Kit (or "none").
2. **What it does** (Step 2).
3. **Problems** (Step 3), heaviest first: Blocks → Wastes credits → Confusing. One line each with its fix. Nothing found → say so in one line ("No broken connections, no invalid or empty nodes"), and what wasn't checked ("results not checked: no browser").
4. **Costs** (Step 4).
5. **One question** with the offers, each with its cost and where it goes (in place or a variation):
   > Want me to fix it? I can: (1) put your logo into the empty "Upload Image" (it's the template's logo slot) or leave it as it is, (2) replace "[App Name]" in the script with Lull, (3) tidy the canvas by the Lyra template style in a variation, so your version stays as it is. The fixes are free; after (2) the script and the video need a rerun, 505 credits. Which ones?

No changes in this message. Several problems of the same kind → one line ("4 upload nodes with no file: …").

---

## Step 6. Fix what the user picked

Only what the yes covered, by the hands-off rule.

1. **Open canvas** (Step 1.7): tab off the workflow before editing.
2. **Variation first** if the fix is big or the user chose it.
3. **Make each change:** `connect_nodes` / `disconnect_nodes`, `update_node` with values from `list_node_configs`, `delete_node` only for nodes the user named. For a video node change the whole `image_inputs_usage` from `get_workflow` with one field changed (`lyra-video-ad-generation` → Step 7, Picking a result).
4. **A fix in a result** (six fingers, a warped logo, a wrong ending) → `lyra-fix`; a new person, angle or size → its variation skill. Say it in one line and hand over.
5. **Check:** `get_workflow` again; every fixed node `is_valid`, every planned edge there, nothing else changed (other prompts, settings, connections, picked results). Lost something by accident → put it back and say so.
6. **Runs** only on a separate yes with the price (Step 4), by the base pre-run check and run order.
7. **Report:** what changed, node by node, old → new in a few words; what's left; the link. Then open the workflow again for the user to see.

---

## Step 7. Tidy the canvas (on request)

Offered in Step 5, done only on a yes, by `lyra-workflow-layout`:

- **A template copy:** keep the producers' layout; fix the notes (typos, continuous numbers, colors, "Video Editor") and the labels; never Organize nodes.
- **The user's own canvas:** a full tidy-up moves every node, so do it in a variation by default ("{name} · tidy"), unless the user says "in place". Notes, sections, colors, labels and positions by the layout skill; connections, prompts, settings and results untouched.
- **Labels the user wrote** are renamed only when they break the pattern badly or the user agrees; list the renames before doing them.
- Finish with the layout skill's check list and a screenshot.

---

## Common mistakes (review)

| Mistake | Prevention |
|---|---|
| Deletes an "empty" node in someone's workflow without asking | Hands-off rule: list it, fix only on a yes |
| Tidies the canvas because it looked messy | The tidy-up is an offer; in a variation by default |
| Explains in node order | Run order from the edges |
| Reports every clip of a copied edit as a broken link | One line: the edit came with the template |
| Offers to delete an empty upload that is an optional slot | Offer to fill it or leave it |
| Trusts `is_valid: true` | Check uploads (`files`), prompts and every setting against `list_node_configs` |
| Reviews ten creatives in one wall of text | A short list first, then full reviews of the picked ones |
| Reviews half of a big canvas | Read the whole saved output |
| "Rerun everything" rewrites the scripts unasked | Price it with the texts kept and with new texts |
| Switches a variation without saying it renames the workflow | Say it first; offer to switch back |
| Pastes long prompts into the explanation | A few words per step |
| "No result" on a node Claude never saw | "Not checked"; look in the browser or ask |
| Runs a node to see if it works | Never run during a review |
| Counts a Section and its nodes, doubling the total | Skip frames in the sum |
| Prices a rerun from memory or an old table | `credits` on the nodes now |
| A problem without a fix | Every problem: where, what, why, fix |
| A list of 20 small things | Group the same kind into one line; heaviest first |
| Judges the idea or the pictures unasked | Only on request, separately |
| Changes more than the yes covered | Each change named before it's made; check with `get_workflow` after |
| Edits while the workflow page is open | Tab off the workflow first |

---

## Quality gates (review)

- **Before sending the review:** read with `get_workflow` now? The final output named? Steps in run order, in plain words? Every check in Step 3 done, "not checked" where Claude couldn't see? Each problem has where, what, why, fix and weight? The costs from `credits`, sections not double counted, the balance next to them? One question, no change made? A canvas with several creatives: the short list first?
- **After fixes:** only the agreed changes made · everything else the same (prompts, settings, connections, picked results, positions unless a tidy-up was agreed) · every fixed node valid · the old version kept where it was a variation · the workflow opened again for the user.
