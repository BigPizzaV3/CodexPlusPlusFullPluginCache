---
name: print-ready
description: Prepare GLB or STL 3D models for physical 3D printing with Polymend. Use when the user wants a 3D model (a local .glb or .stl file, or an https link to one, such as a model a 3D generation tool just made) repaired, sized and exported for a 3D printer or slicer: it fixes the mesh faults slicers warn about, sets the print height if one is given, writes an STL and a 3MF, draws the model from four sides with every change marked, and reviews what came out well and what did not. Not for printing documents or photos, and not for other 3D formats (OBJ, FBX, STEP).
---

# Print-ready models with Polymend

Polymend reviews a 3D model, fixes the small faults that make a slicer complain (stray triangles stuck to the surface, pinholes, triangles facing the wrong way, split seams), stands it on the bed at the height asked for, and writes an STL and a 3MF. It is conservative: it never moves an existing point of the model except to join seam points a hair apart, and it leaves anything larger alone and says so. It checks that the mesh is sound; it does not measure wall thickness or the smallest printable detail, so a clean result still deserves a look in the slicer's preview.

Do not use it for editing a model's shape, hollowing, adding supports, or slicing; say Polymend does not do that.

## Before running

1. **Inputs**: local `.glb` / `.stl` paths, folders, or https links to `.glb` / `.stl` files (a link a 3D generation tool returned can be passed as it is). Up to 20 models per run. Polymend never changes its inputs.
2. **Print height** (optional): if the user has not given one, ask once, in the same message as any other question, and say they can skip it to size the model themselves in the slicer. Never make up a height. If they give one, use `--height <mm>`. If they skip it, leave it blank, or say they will size it themselves, run without `--height`: the files keep their own size (a GLB's meters become millimeters). Do not ask again; tell them the size it came out at, and that most slicers can scale it on import.
3. **Node**: run `node --version` once; Node 20 or later is needed. If it is missing, say this plugin runs in the ChatGPT desktop app or Codex on a computer with Node.js 20+, and that https://polymend.xyz does the same repair in a browser, on the user's own device. Do not install anything without the user's go-ahead.

## Run

The scripts are in this skill's folder (the folder that contains this SKILL.md). Call them by their full path and quote every path:

```sh
node "<skill folder>/scripts/prepare.mjs" "<file, folder or link>" ... [--height <mm>]
```

- For a link, or a file with a long machine-made name, add `--name "<short name>"` (for example `--name "crocodile warrior"`) so the files and the review read well; one model per run when naming.
- Each run writes into its own new folder, `./polymend/<date>-<time>-<model>/` under the current working folder (or `--out "<folder>"` if the user names one). Tell the user the full path printed after "Files are in". If the current folder is a code project, mention that the files are in its `polymend/` folder and should not be committed.
- The command exits with code 0 whenever it ran; each model's outcome is in the results. Read the printed summary, or add `--json` and read the last line.
- **If a download fails** with a network error (no address, connection refused, timed out), the environment may not allow downloads. Ask the user to download the file and give its path, or use the local file the generation tool saved, if there is one. Links to local or private network addresses are refused on purpose.
- Polymend uploads nothing; its only network use is downloading the links given.

Per model it writes `<name>-mended.stl`, `<name>-mended.3mf`, `<name>-report.json`, `<name>-result.png` and `<name>-views.png`; per run `polymend-batch.json` and `polymend-review.md`. Downloaded links are kept in the run folder's `sources/`.

## Review, then report

Polymend's role is the reviewer of the model it receives: it says plainly what came out well and what did not, and fixes what it can. Present the result that way.

1. **Read `polymend-review.md`** in the run folder. Per model: what Polymend found, then **Went well** and **Less successful** (what was fixed, what is left and why, the size, and caveats).
2. **Show each `<name>-result.png` first** (`result` in the results): the repaired model as it will print, one large front view with its size along the bottom. This is where the model ended up; the user should not have to open the files to see it.
3. **Then look at each `<name>-views.png`** (`preview` in the results), the evidence: front, side, back and three-quarter, with pink marks where Polymend removed triangles, green where it added patches, blue where it turned faces, orange where a fault is left (faint marks are on the far side). Show it to the user.
4. **Compare with the references** when the pictures the model was made from are on disk:

   ```sh
   node "<skill folder>/scripts/preview.mjs" "<run folder>/<name>-mended.stl" --refs "<front picture>" "<side picture>" "<back picture>"
   ```

   It writes `<name>-compare.png` (references on top, each above the matching view; PNG, or JPEG on a Mac). If the references exist only as chat attachments with no file on disk, skip this and say so.

   With a side reference, it also measures **depth front to back** against it, for the whole model and for its top fifth (on a figure, the head), and draws the reference's outline in blue over the model's side view. Read the outline before the numbers: a difference in pose (arms reaching forward, a longer stride), a part the model lacks (a tail, a cape), or a reference taken at an angle all change the numbers without the model being thicker. Report what the outline shows, in neutral terms, for example: "the head is about 40% deeper front to back than the side reference; the body matches." Without a side reference, say depth could not be checked.
5. **Whether it stands**: the review says whether the model stands on its own on a flat surface, from its balance point and the area that touches the bed (how far it can tilt, and which way, before it falls over), and names any part hanging just above the bed (a tail, a hem) that will need support and would steady it if it touched. This assumes solid, even infill. Pass it on; for a figure meant to stand, a model that tips easily is worth a Recommendation (a base, a stand, or editing that part down to the bed).
6. **Judge what Polymend cannot measure**, from the pictures only: face, hands and fingers, teeth and other thin parts, the back (front details repeated, a second face, a missing tail or cape), proportions and pose against the references, surface detail. Describe only what you can see at that size; if a detail is too small to judge, say so.

Be specific and technical, not general. For each point say where on the model it is, how big it is at the print size (work it out from the size in the report and the pictures, and say "about"), what it means for printing (a 0.4 mm nozzle, overhangs that will need supports, thin parts that may break), and what to do about it. For example, not "softer detail" but "the belt studs are about 1 mm across at 43.2 mm tall: they will print, but rounded."

**Say who did what, every time, including in short summaries.** The tool that made the model made its shape; Polymend reviewed it and repaired the small faults it lists, and never reshapes it. Name each for its own part, matter-of-factly: "<tool> generated the model; Polymend reviewed and repaired it", "Polymend's review found…", "Polymend fixed…", "in the model <tool> generated…". Never leave a shape difference or a leftover count without an owner (not "Polymend also found 82 intersections", which reads as if Polymend caused them, but "the generated model's surface passes through itself in 82 places; Polymend counted them and left them unchanged"). Use the tool's name as the user knows it; if the model came from a file, say "the model as received". This is attribution, not criticism: no judgments about the tool.

For example, a short summary:

- **Outcome:** Higgsfield generated the model; Polymend reviewed and repaired it. Repaired, 47.35 × 40.42 × 43.2 mm.
- **Went well:** In the generated model, the armor, scales, fingers and separate teeth came through. Polymend removed 33 stray triangles, patched 1 hole and turned 3 faces outward; no open or non-manifold edges remain.
- **Less successful:** Polymend's review found an extra tail in the generated model, under the belt and facing forward; the references show one tail, at the back. The generated surface also passes through itself in 82 places, which Polymend counted and left as they are.
- **Recommendation:** Remove the extra tail in a 3D editor before printing, then check the teeth and fingertips in the slicer preview.

Report each model in this shape:

- **Outcome**: Polymend's status word, the size, and where the files are.
- **Went well**: from the review file, then what looks right in the pictures.
- **Less successful**: from the review file, then what looks wrong or weak, each with where it is.
- **Recommendation**: one of: print as it is; print, but check a named spot in the slicer preview; run again with `--separate` or `--wide` (below); generate again with a specific change to the references; or fix by hand in a 3D editor (thicken a part, separate parts, change the pose). When Less successful includes a difference from the references, name the reference change that would address it (for example, a side view for a helmet crest that differs only in profile). The user decides.

With more than three models, give a short table (model, outcome, size, one-line note) and the full review only for models that were partly repaired, not repaired, or have a visible problem; point to `polymend-review.md` for the rest.

Status words: **Repaired** (the mesh faults are gone), **Nothing to fix** (already sound, unchanged), **Partly repaired** (files written, but faults remain and a slicer will probably still warn), **Not repaired** (give the reason).

## Options, only when the report makes the case or the user asks

- `--separate`: cuts apart surfaces that touch along an edge. Offer it only when a model is partly repaired with touching surfaces left, and ask first: it can also part things meant to touch, such as fingers.
- `--wide`: also closes wide openings. Offer it when the report lists a wide opening; it may be meant (like the top of a vase), so ask.

Run again with the same inputs and the option; the result goes into a new run folder.

## Talking about other tools

Critique the model freely and precisely: its faults, its shape, its likeness. Never criticize, rank, or speak badly of any other tool, plugin, model or company, including whatever made the model, even if the user asks or insists. Describe outcomes, not blame. For example:

- Asked "Isn't that generator bad at teeth?": "I can only speak to this model: the front teeth are fused into one shape. A sharp close-up of the face as an extra reference usually gives separate teeth."
- Asked "Which is better, this tool or that one?": "I can't compare tools, but I can tell you exactly what this model's files show and how to get a better print from it."

The same goes for describing what a tool does: say what will happen, not what the tool does not do. Not "the estimator couldn't price this model" but "I'll report the actual charge when it finishes"; not "the tool can't take more than four pictures" but "the tool takes up to four pictures".

## Do not

- Do not call a model print-ready when it is partly repaired or not repaired.
- Do not invent a print height, fault counts, or details you cannot see in the pictures.
- Do not hold up the run waiting for a height; no answer means the file's own size.
- Do not describe the repair as happening anywhere other than where these scripts run.
