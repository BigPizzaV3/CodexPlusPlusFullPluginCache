---
name: lyra-fix
description: "Use when the user wants to change one part of a finished Lyra ad, e.g. \"regenerate scene 3\", \"change her sweater\", \"another ending\", \"she has six fingers\", \"the logo is warped\", \"fix the headline on card 4\", \"louder music\", \"go back to the old one\". Fixes only that part, reruns what depends on it and reports the credits. Not for new variations."
---

# lyra-fix

Repair skill for every Lyra creative, video and image. The creative skills build the ad; this one fixes a part of it after it exists. It works the same way on a scene in a video ad, a card in a carousel and a banner in a static set: find where the problem is born, change that one thing, check that nothing else moved, rerun only what depends on it, put the new piece back, report.

**The goal.** The user says what is wrong in their own words ("she has six fingers in scene 3") and gets back the same ad with only that fixed, the price named before anything runs, and the old version still there to go back to.

**The one thing to understand.** Changing one word in a prompt and running the node again does **not** change one thing. It makes a new take: Lyra's models have no fixed seed, so the face, pose, light and framing come out different too. Only an **edit of the finished image** (the old image connected to a new Nano Banana Pro node, "change only…") keeps everything else. So a fix of one element is an edit of the image, not a rerun; in a video, the clip is then generated again from the fixed image, so the look stays and the motion is a new take. A rerun of the original prompt is for problems where a new take is fine or wanted (a glitch in the whole frame, a bad composition, the user asks for "another one").

**Core rules come from the base skills.** Part 1 of `lyra-video-ad-generation` (video) or `lyra-static-image-generation` (images) holds the shared steps: pre-run check, credits, picking a result, links, open canvas, runtime failures, base prompt rules. The Video Editor, captions and on-screen text follow `lyra-video-editor`. Canvas changes (a new edit node, an insert, a renamed label) follow `lyra-workflow-layout`.

**This is a way of thinking, not a script.** Fixed: change only what was asked, edit the result instead of regenerating it, fix at the source, compare old and new before calling it fixed, the cost in the same question, never an unchanged rerun, the old results kept, the right links.

---

## Fix or variation (hard line)

A fix keeps the ad and changes a detail. When the request changes what the ad *is*, it is a variation and goes to its skill. Say so in one line and hand over; don't stretch a fix into a remake.

| Request | It is | Goes to |
|---|---|---|
| A glitch: fingers, hands, face drift, morphing, flicker, a warped phone | fix | this skill |
| One detail in a scene or image: sweater, color, prop, light, expression, camera move, background object | fix | this skill |
| Another ending of the same story (another last shot, another CTA moment) | fix | this skill |
| Wrong text: a letter in the headline, the app name, a number, a caption, screen text not matching the screenshot | fix | this skill |
| Warped logo or icon | fix | this skill |
| Audio: music louder or softer, VO line reworded, a mispronounced app name, the music cut too early | fix | this skill |
| Edit: scene order, trims, a scene shorter or longer, captions size or position | fix (often free) | this skill + `lyra-video-editor` |
| Another person in the whole ad | variation | `lyra-audience-variations` |
| Another outfit, room or car through the whole ad, for another audience | variation | `lyra-audience-variations` |
| Another story, angle, reason, pain | variation | `lyra-ad-concept-multiplier` |
| A new opening (first 3 s) to test | variation | `lyra-video-hooks` |
| Another size or ratio | variation | `lyra-image-resize` |
| Another language or market | variation | `lyra-image-translation` (images) · `lyra-audience-variations` (video voice and language) |

**Rule of thumb:** if the fix touches more than about half of the generation nodes, or the user would call the result "a different ad", it is a variation. Unsure → ask in the same message as the plan: "This changes the person in every scene, so it's a new version rather than a fix: I'll make it as a variation with lyra-audience-variations. OK?"

---

## Step 1. Find the node

1. `get_workflow` now, not from memory. Read the labels, the edges and the Video Editor's `video_rendering_composition`.
2. Map the user's words to nodes:
   - "scene 3", "the second shot", "the ending" → the node labelled with that scene; no labels → the clip in that position in the Video Editor (playback order, by `startMs`).
   - "banner C2", "card 4", "the 9:16 one" → the label or the Section that names it.
   - "her sweater", "the phone", "the room" → the earliest node that draws it (a character, a keyframe, a phone shot).
   - "the music", "the voice", "the captions", "the text on screen" → the audio node or the Video Editor.
3. **Inside one multi-shot clip.** The base skill builds one Seedance clip with several shots by default, so "scene 3" may be a shot inside one clip, not its own node. Find the shot's time range from the script and the composition, then pick a route in Step 2 → Video.
4. **Fix at the source.** A defect shows where it is born. Walk back along the edges from the node the user named to the earliest node that has the problem:
   - wrong in the keyframe or character image too → fix the image; the clip after it reruns from the fixed image;
   - right in the image, wrong only in the clip (fingers merge while moving, the face drifts) → fix the clip only;
   - wrong in every scene with this person (the sweater everywhere) → every node that draws it, with the same words (Step 2 → One element in several nodes); many nodes → maybe a variation (above).
   Claude can see images and videos only with a browser signed in to Lyra or after `lyra-result-check`. Without either, ask in one line: "Is it already wrong in the image 'Scene 3: kitchen', or only in the video?"
5. Several problems at once → collect them all into one fix round: one plan, one cost, one rerun of the shared nodes after them (one Video Editor render, not three).

---

## Step 2. The change

**Change only what was asked.** The picked results of the other nodes stay picked. In every prompt that stays, the anchors (character, place, style, phone), the user's own words, settings, references and frames stay word for word.

**Edit or new take.** Two ways to change a result, and they keep different things. Pick per problem and say which in the plan:

| | Edit of the result | New take |
|---|---|---|
| How | a new image node on Nano Banana Pro with the finished image connected, "change only…"; for video, the clip is then generated again from the fixed image | the same node, prompt or setting changed, run again |
| What stays | everything except the element: face, pose, framing, light (in a video the look; the motion is a new take) | the anchors in the prompt; face, pose, light and framing can shift |
| Use for | one element: sweater, prop, color, a hand, text, an object in the background | a glitch in the whole frame, a bad composition, another ending, "give me another one" |

**Cheapest fix first.** Go down the list and stop at the first that does the job:

| # | Fix | Cost |
|---|---|---|
| 1 | Another result that already exists (count 2, an earlier run): pin it (base Step 7) | 0 |
| 2 | A Video Editor change (`lyra-video-editor`): order, trims, a clip's own sound muted, music volume, speed, freeze frame, captions text, size and position, on-screen text, a logo or screenshot laid over a broken moment | 0 |
| 3 | A settings change on one node (duration, resolution, a reference's job, a frame instead of a reference where the model allows it) | that node's rerun |
| 4 | An image edit on Nano Banana Pro (Images below) | one image (+ the clip after it) |
| 5 | A clip generated again from the fixed image, or an insert clip for one shot (Video below) | one clip or one short clip |
| 6 | A new take: prompt change on one node | that node's rerun + its dependents |
| 7 | Another model for that node (base Reference A ladder, up or down) | that node's rerun + its dependents |

### Writing the change

Find the words that cause the problem and replace only them. Add the request as concrete, renderable words, and a short constraint if it's a glitch.
- "change her sweater to a green one" → an edit: "Change only her grey hoodie to an oversized moss-green knit sweater…"; in the prompts of the nodes that stay, "grey hoodie" → "oversized moss-green knit sweater" so later reruns don't bring the grey one back.
- "six fingers" → an image edit of that hand ("Fix only her right hand: five fingers, natural anatomy, holding the mug…"), or in a new take simplify the hand action (one object, visible contact, fewer fingers in view) and add "five fingers on each hand, natural hand anatomy" to the constraints line. Never an unchanged rerun "for luck" (base rule).
- "another ending" → a new take of the ending only: rewrite the ending beat and the final frame line; the earlier beats, timing and VO stay unless the VO speaks over the ending (then the VO line too, its length checked).
- "the screen text is wrong" → base Reference G of the image skill: the screenshot connected, the fidelity line, the 3–5 key texts in quotes, a larger screen; in a video, the cheapest is often the screenshot or a phone shot laid over that moment in the Video Editor.
- In the plan show only the change: `before: "grey hoodie" → after: "oversized moss-green knit sweater"`, never the whole prompt.

### Images: the edit on Nano Banana Pro

The house way to change one element on an image. **Always Nano Banana Pro.** Never Lyra's `change_element_on_image` node (it runs on Nano Banana 2 and changes too much).
1. **A new image node** next to the source (`create_image_generation_node`), model `google/nano-banana-pro`, label "{source label} · fix: {what}" ("Scene 3: kitchen · fix: sweater").
2. **Connect the picked result of the source image** to it as a reference: it is [Image1]. Ratio `match_input_image`, resolution as the source (2K, or 4K when a screen must be read). Other references only when the change needs them (the screenshot for screen text, the logo file, the persona for a face fix).
3. **The prompt:** verb first, the one change, then the keep list in words, then "everything else exactly as in [Image1]":
   > Change only her grey hoodie in [Image1] to an oversized moss-green knit sweater with a ribbed collar. Keep everything else exactly as in [Image1]: the same woman, face, hair, skin and expression, the same pose and hands, the mug, the framing and camera angle, the kitchen, the light direction and color, the phone and its screen, every text. Do not add, remove or move anything else.
4. **Run, then compare** the new image with [Image1] side by side, at full resolution (a browser signed in to Lyra: open both image files and draw them next to each other into a canvas, as in `lyra-result-check` Step 3; Lyra's files can't be downloaded into a shell). Zoom into the face and hands. Check, one by one: the change happened, and fully (the whole sweater, both sleeves) · face, hair, skin, age, expression the same · pose, hands, fingers the same · framing, crop and camera angle the same · light direction, color and shadows the same · background, props and colors the same · phone screen, logo and every text the same, letter by letter · no bleed (traces of the old sweater, a half change).
5. **Not right on the first try** (the sweater didn't change, or something else moved): run the same node once more, with what drifted named in the keep list and "change only…" kept at the start ("…keep her face exactly as in [Image1], the same eyes and nose"). Then compare **both takes with [Image1]** and pick the one where only the element changed. Pin it on every node after it (base Step 7) and say which one went on.
6. **Two takes, neither right** → change the way: a smaller change in words, the element described more concretely, a crop where the element is larger, or a new take of the image (it will look different; say so). Still failing → leave it for the designer and say exactly what.
7. **No browser to look:** say the image is ready and ask the user to compare it with the old one by the check in point 4.
8. **Several changes on one image** (the sweater and the mug): one change per edit, in a chain. Each next edit takes the **best result so far** as [Image1], not the original, or the earlier change comes back. Compare after every step. Keep the chain short (two or three edits); a longer one → a new take of the image from the fixed prompt.

**Other image cases.**
- **Rerun the original node** (a new take) only when the problem is in the whole composition, or the user wants another version.
- **Text on the image:** an edit on Pro naming the exact spelling ("Change only the headline text to 'Sleep in 5 minutes', same font, size, color and place"); after two fails leave a clean zone for the designer (image skill Reference I).
- **Children of the image.** A fixed static may have resized or translated versions made from it. List them in the plan and ask in the same question whether to redo them too, with their credits; default yes when the fix shows in them.
- **Carousel card:** edit only that card; the card keeps the Story Bible anchors word for word (`lyra-carousel`).

### Video

**The main way: fix the picture, then generate the clip again.** A clip is not edited directly. The image the clip is made from is fixed by the Nano Banana Pro edit above, compared with the old one, and then the clip is generated again from the fixed image with the same prompt. The image holds the look (person, outfit, place, light); the motion is a new take. Say so in the plan: "the look stays, the movement will be a new take".

1. **The problem is in the image the clip is made from** (the keyframe, the phone shot, the character): edit that image on Pro, compare, then generate the clip again from the fixed image: on Seedance 2.0 or Kling as the first frame (re-pointed to the new result, base Reference E), on Seedance 2.5 as the reference in place of the old one. The clip's prompt stays word for word, except the words of the change ("grey hoodie" → "moss-green knit sweater"); the same model, duration, ratio, resolution and sound settings.
2. **The problem is only in the clip** (the image is right, the clip got the sweater wrong, a background object appeared): take the frame of that shot (Lyra's `extract_frames`, an image node action, up to 10 timestamps; or the keyframe if the shot has one), edit the frame on Pro, compare, and generate the clip again from it on a frame model (Seedance 2.0, Kling) with the same prompt. Clips made from references only (Seedance 2.5): fix the element in the prompt and generate a new take with the same references; the look stays, the details of the frame can shift.
3. **A shot inside a multi-shot clip:** offer the insert in the plan, recommended for a small fix:
   - **A. Insert clip (recommended):** take the shot's frame (`extract_frames`), fix it on Pro, generate a new short clip only for that shot from it (a frame model, the same anchors, the shot's length from the script), and lay it over the original in the Video Editor at the shot's time. The rest of the ad stays exactly as it is. Cheaper.
   - **B. New take of the whole clip:** the fixed prompt for the whole clip. Every shot is generated again and can come out different, the good ones too. Costs the whole clip.
4. **A glitch in motion** (fingers merging while moving, morphing, a jump): a new take of that clip or an insert, with the hand action simplified and the constraint line; for continuity across the cut, start from the last frame of the clip before it (`extract_frames`) on a frame model.
5. **Text and logo in a video are cheaper in the edit.** On-screen text and captions live in the Video Editor: fix them there for free (`lyra-video-editor`), never regenerate a clip for them. A warped logo in a clip → the uploaded logo laid over that moment as an image layer, or the moment covered by the end card. Wrong phone screen text → a UI insert (base Reference D): the phone shot on Pro with the screenshot connected, laid over the moment.

**Backup: a reference video** (only when the movement itself must stay exactly: a perfect take, a long gesture, lip sync that must not change). A new video node with the finished clip connected as a reference video ([Video1]) and, when the new element must look a certain way, the fixed image as [Image1]. The model watches the old clip and generates a new one that repeats its motion, camera and timing with the one change:
   > In [Video1], replace only her grey hoodie with the moss-green knit sweater from [Image1]. Keep the same person and face, the same hand movements, camera movement, timing, lighting and background exactly as in [Video1].
   It is still a generation and costs a clip of the same length. Models: Seedance 2.5 (reference videos up to 30 s in total) or Seedance 2.0 (up to 15 s), same duration, ratio and resolution; Gemini Omni video for a 4–10 s piece of a clip (`reference_video_trim_start` / `_end`); Kling Video 3.0 Omni for 3–10 s clips. One change per run; small artifacts can appear next to the changed area. Offer it only as a second option in the plan, after the main way, and say it is not tested yet. *Not tested in Lyra yet (lyra-fix-test-plan F05, F08): whether a video can be connected to a video node through the tools, and how much the model keeps. If the test fails, this route is removed.*

**Talking clips (UGC, dialogue, in-clip speech).** A new take of a clip with speech makes the voice, the lips and the line again, and can bring music inside the clip back. So:
- a change off the face (outfit, background, prop) → the main way (fix the frame, new take) with the same line word for word, the same voice description and the no-music sound line (base Reference C); check the line still fits the length at a calm pace; if the voice must stay exactly, the backup reference video, and keep the original clip's sound in the Video Editor when the lips still match;
- a changed line → a new take of that clip (in-clip speech), or only the VO node (separate voiceover), then the Video Editor and the captions again.

### One element in several nodes

The sweater in three scenes, the logo on four cards: edit every node that shows it, with the same words in every prompt, in one fix round. Then compare the results with each other, not only with the old ones: the same sweater (color, knit, collar) in every scene. One of them differs → one more edit of that one, with the others as references for the element.

---

## Step 3. What reruns

Build the rerun list from the edges, not from memory: the fixed node (or the new edit node), then every node downstream of it, in run order.

| Fixed | Reruns |
|---|---|
| Character or persona image | every image and clip it feeds → Video Editor (big: check the variation line) |
| Keyframe or phone shot (edited) | the clip(s) that take it, re-pointed to the edit → Video Editor |
| Clip (new take) | Video Editor |
| Insert clip (new) | Video Editor (the insert laid in) |
| Voiceover | Video Editor (the new VO length checked against the clip) + captions |
| Music | Video Editor |
| Video Editor only | Video Editor (0 credits) |
| Static image (edited) | that image (+ its resized and translated children if agreed) |
| Carousel card | that card |

Nodes not in the list are not run. Their results stay and cost nothing. An edit node feeds the next node instead of the source: move the connection from the source to the edit (`disconnect_nodes`, `connect_nodes`), and keep the source on the canvas with its results. When the source fed the Video Editor directly, disconnect it from the Video Editor too, or its clip comes back into the edit (`lyra-video-editor` → Known behaviour).

---

## Step 4. Plan and cost: one question

One short message, one question (base Step 3), with:
1. **What I found:** the node and why there ("the fingers are already wrong in the image 'Scene 3: kitchen', so I fix the image, not only the clip").
2. **What changes and how:** the before → after words, and the route: "an edit of the image, everything else stays" or "a new take of the clip, the pose and face may shift a little".
3. **What reruns:** the list from Step 3 with each node's credits (read from `get_workflow`, base Step 6) and the total, next to the balance. A second take of an edit, if it may be needed, named with its price ("+23 if the first try changes her face").
4. For a shot inside a multi-shot clip: options A and B with their credits.
5. Variation instead of in place, if it applies (Step 5).

> Scene 3 · six fingers: the hand is already wrong in the image "Scene 3: kitchen". I edit only her right hand on Nano Banana Pro (five fingers, both hands on the mug), the rest of the image stays; then the clip reruns from it. Reruns: hand fix 23 (+23 if a second try is needed) · Clip 3 338 · Video Editor 0 = **361 credits** of your 40 120. Run it?

**Free fixes run straight away** (another existing result, a Video Editor-only change): say what you did and send the new render. Everything that costs credits waits for the yes. The yes runs the whole rerun list, including the second take of an edit named in the plan; don't ask again between stages unless the real cost is more than ~15% over (base Step 6).

---

## Step 5. In place or a variation

`update_node` keeps every result already generated, a rerun adds new results next to the old ones, and an edit is a new node next to its source. So a fix of one or two nodes is made **in place**, in the variation the user is working in: the old results stay, and the user can go back.

Make a **variation** first (base Variations: `create_variation` "{name} · fix: {what}", `switch_variation`) when: the user wants to compare old and new side by side · the fix touches many generation nodes (the character, the whole clip) · the user asks. Never edit a variation the user made for something else without saying so. Right after `create_variation`, read the Video Editor's composition and the frame pins: in a new variation the edit can come out empty or pointing to old results; rebuild it by `lyra-video-editor` before any render.

The old prompt is overwritten by an in-place new take: quote the changed words, old and new, in the report so it can be put back.

**Going back** ("go back", "the old one was better"): pin the old result again on every node after it (base Step 7), or move the connection back from the edit node to the source; put the old words back in the prompt if it was changed (`update_node`); render the Video Editor again (free). The edit node stays on the canvas with its result unless the user asks to remove it.

**Open canvas.** Before editing through the tools, ask the user to switch their tab away from the workflow (an open canvas can write its old state over the edits). With a browser under Claude's control, move the tab off the workflow yourself while editing, then open the workflow again at the end to show the result.

---

## Step 6. Run and put it back

1. **Pre-run check** (base Step 5) before every run: connections, references, frames, settings, valid nodes, inputs ready.
2. `run_node` in run order; `get_run_results` until done; never `run_node` on a running node.
3. **Compare before going on.** After an edit or a new take, look at the new result next to the old one (Step 2 → Images, point 4; for clips, frames at the same times). Only then run the nodes after it. Without a browser, ask the user to compare, or run `lyra-result-check` on that part.
4. **Pin the new result.** After a rerun the node holds old and new results. Make sure every node after it uses the new one: on video nodes set `reference_result_image_uuids` or the frame's `image_result_uuid` to the new result (base Step 7), then `get_workflow` to check it held. Then run the next node.
5. **Video Editor** (`lyra-video-editor`). Read `video_rendering_composition` first and change only what's needed:
   - **the edit plays the result it was pinned to.** Each clip in the composition points to one result (`sourceNodeId`, `sourceResultUuid`, `assetUrl`). After a rerun, a new take or an edit node, the editor still plays the old clip: set the new result's `sourceNodeId`, `sourceResultUuid` and `assetUrl` (from `get_run_results`) on that clip yourself, then `get_workflow` to check;
   - the new clip in its place, at the same `startMs`; a different length → adjust its `trim` or `durationMs` and the clips after it, so the ad keeps its planned length and the cuts stay where the VO expects them; `canvas.durationMs` = the end of the last clip, or the render ends on black;
   - an insert clip: a node connected after the edit exists is not added on its own, so add it to the composition yourself (`assetUrl`, `sourceNodeId`, `sourceResultUuid`) as an overlay layer above the main video at the shot's `startMs`, its own sound muted if the main clip carries the sound;
   - music volume under the voice, muted clip sound, captions size 80 at 75% of the height: kept exactly as they were;
   - captions after a changed line: made again (`lyra-video-editor` → Captions) and checked against the new script;
   - after anyone opens the editor, the 5-second check (`lyra-video-editor` → Known behaviour).
   Then run the Video Editor.
6. **Failure.** A failed run → name it, one retry with a changed prompt or model and its credits (base Runtime failures).

**When to stop.** Two fix rounds on the same problem without a clean result → stop before spending again. One message: what was tried, the total spent on this fix so far, and 2–3 other ways (a simpler shot, another model, an insert or overlay in the edit, leave it for the designer, keep the best take so far). Run only on the user's pick.

---

## Step 7. Report

> Scene 3 fixed: five fingers, the rest of the ad unchanged (compared with the old frame: same face, light and pose). Video: {video url} · Workflow: https://app.lyra.splitmetrics.com/workflows/{uuid}. The fix cost {x} credits · balance {X}. New node "Scene 3: kitchen · fix: hand" (take 2 went on). The old image and clip are still there; say "go back" to switch.

- **Links by the base rules:** one video → the new Video Editor result + the workflow · one image → the new image + the workflow · several → the workflow only. Name the variation if the fix went into one.
- **Real spend:** balance before − after.
- **What changed,** in one line: the route, the new node or the old and new words, which take went on.
- **What was compared,** in one line (or that the user still has to compare).
- **Next step:** run `lyra-result-check` on the new render straight away (free), only on the frames of the fixed part and the cuts around it, and the sound when the fix touched it (music volume, VO, a fade). No browser and no check skill → send the check list for the fixed part (Quality gates) and ask the user to look.

---

## Common mistakes (fix)

| Mistake | Prevention |
|---|---|
| Changes one word and reruns the node, the whole image comes out different | One element = an edit of the result on Nano Banana Pro (Step 2) |
| Uses Lyra's `change_element_on_image` node | Always a new image node on Nano Banana Pro with the source connected |
| Calls it fixed without comparing with the old result | Compare face, pose, light, background, screen, text (Step 2 → Images, point 4) |
| One try, something else moved, sent anyway | A second take with the drift named, then pick the take where only the element changed |
| Rewrites the whole prompt for a one-word change | Replace only the words that cause the problem; anchors and the user's words stay |
| Fixes the clip when the defect is already in its image | Fix at the source: walk back along the edges (Step 1) |
| Reruns the whole multi-shot clip for one shot | Offer the insert clip first (Step 2 → Video) |
| Regenerates a clip for on-screen text, captions or a logo | Fix them in the Video Editor or as an overlay, for free |
| New take of a talking clip, the line or voice changes, music sneaks in | The same line word for word, the same voice, the no-music line; the reference video only when the lips must stay |
| The sweater fixed in one scene, still grey in the next | Every node that shows it, same words, compared with each other |
| Reruns nodes the fix doesn't touch | Rerun list from the edges only (Step 3) |
| Runs a paid fix before saying the price | Cost in the same question (Step 4); only free fixes run straight away |
| A separate question for the price | One message, one question |
| The next node still uses the old result | Pin the new result, or move the connection to the edit node, and check with `get_workflow` |
| A new clip of another length breaks the edit | Adjust trims and the clips after it in the composition |
| The new render still shows the old clip | Set the new result's `sourceResultUuid` and `assetUrl` on the clip in the composition |
| The insert clip is missing from the render | Add it to the composition yourself; a node connected later isn't added |
| Several changes in one edit, or each edit from the original | One change per edit, each from the best result so far |
| Captions, music volume or muted sound lost in the new render | Read the composition first, change only the clip |
| Reruns an unchanged prompt "for luck" | Change the prompt, a setting or the model; say what changed |
| Keeps spending round after round | Two rounds → stop, the total so far, other ways (Step 6) |
| Turns a new person or story into a "fix" | Fix or variation table; hand over to the variation skill |
| Grades the new result without seeing it | Look with a browser or `lyra-result-check`; otherwise ask the user with the check list |
| Three fixes, three renders | One fix round: all changes, one cost, one Video Editor run |
| "Go back" with nothing to go back to | Old results stay, edits are new nodes, old words quoted in the report |

---

## Quality gates (fix)

- **Before sending the plan (Claude checks):** the right node, at the source? Edit or new take chosen, and said what may shift? Only the asked thing changes, shown as before → after? A free route in the Video Editor checked first? The rerun list from the edges? Every node's credits, a possible second take, and the total next to the balance? A fix, not a variation? For a shot inside a clip, options A and B?
- **After each edit or new take:** compared with the old result: the change is there and complete · face, hair, pose, hands, framing, light, background, screen, logo and text the same · no bleed · the same element the same in every node that shows it.
- **After the render:** the asked thing is fixed · no new defect in the fixed part · the new piece sits in the edit at the right time, the cuts and the VO still line up · music, captions and volume as before · the planned length · the old result still there.

Pass = the user is happy with the fixed part and nothing else changed. A new problem in the fixed part → one more fix round with its cost (and the stop rule); a problem elsewhere that was already there → a separate fix, named as such.
