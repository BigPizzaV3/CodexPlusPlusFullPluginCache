---
name: lyra-result-check
description: "Use after every final Lyra render or fix, and when the user asks \"check the video\", \"look at the result\", \"any defects?\", \"is it ready to launch\", \"check the statics\". Looks at frames and sound (faces, hands, screen text, logo, captions, levels) and reports each problem with a fix."
---

# lyra-result-check

Quality check skill for every Lyra creative, video and image. The creative skills build the ad and `lyra-video-editor` renders it; this skill looks at the finished result the way a reviewer would, frame by frame, measures its sound, and says what is broken before the ad goes to the media buyer. Fixing is not done here: every problem goes to `lyra-fix`.

**The goal.** The user gets one short answer: "Checked 14 frames, 2 problems", each problem with its time, scene, a picture of the frame, what is wrong and how to fix it with its price. Nothing invented, nothing graded without being seen or measured.

**Core rules come from the base skills.** Part 1 of `lyra-video-ad-generation` (video) or `lyra-static-image-generation` (images) holds the shared steps: links, picking a result, open canvas, credits. The edit itself (composition, captions size and place) is described in `lyra-video-editor`. Fixes follow `lyra-fix`.

**When it runs.**
- **Automatically, after every final result.** A video skill or `lyra-video-editor` rendered the final video, or an image skill finished its images → run the check straight away, without asking (it costs no credits), and put its report into the final report.
- **After a fix:** `lyra-fix` reran a part → check only the frames of the fixed part and the cuts around it.
- **On request:** "check the video", "look at the result", "anything broken?", "can we launch it?", a link to an older render.
- Not after intermediate stages (keyframes, single clips before the edit): those are checked in the stage itself.

**This is a way of thinking, not a script.** Fixed: look before judging, frames chosen from the edit (not at random), say what was checked and what wasn't, every problem with a time, a picture and a fix, sound measured but never claimed "heard", fixes only through `lyra-fix` and only after a yes.

---

## What Claude can and can't check

| Can check | How | Can't check (asks the user) |
|---|---|---|
| Faces: identity, eyes, teeth, skin, the same person across cuts | frames | Pronunciation of the app name, voice tone, whether the voice is clear |
| Hands and fingers, objects held | frames at full resolution | Lip sync (needs sound and motion together) |
| Phone screen text, UI, the logo and icon | frames, against the user's screenshot and logo | Motion between frames: morphing, flicker, jitter (frames are still; only big ones are caught) |
| Captions: over a face, size, safe zone, words | frames, against the script | Pacing and how the ad feels |
| Text on images and on screen | frames, letter by letter | |
| Cuts: black frames, a jump of person, outfit or props, the end card | frames on both sides of each cut | |
| Sound: levels, clipping, silence at the start, a hard stop at the end, music under the voice in dB | measured in the browser (Step 4) | |

---

## Step 1. Find the result and read the workflow

1. `get_workflow` now, not from memory.
2. **The final video.** The final file is a link `https://lyra.splitmetrics.com/media/static/…mp4`. Where to get it:
   - **rendered in this chat:** the `url` from `get_run_results` of the Video Editor run;
   - **rendered earlier:** the tools return a result only for a run made in this chat. Open the workflow in the browser, press play on the node's preview and read the file link from the page (`document.querySelector('video').currentSrc`), or take the latest render from the Video Editor's **Results** drawer, or ask the user for the video link (one line: "Send me the link to the final video, from the Video Editor's Results"). Then move the tab off the workflow before any edit;
   - **no Video Editor yet** (the workflow ends on a clip): check the clip itself the same way, say that there is no edit yet (no captions, music or end card), and offer the edit by `lyra-video-editor`;
   - **the parts of the edit:** every clip, voiceover, music and image in the Video Editor's `video_rendering_composition` has a direct file link in `assetUrl`, with `startMs`, `trim`, `volume` and its track's `volume` and `muted`. Use them for the sound check (Step 4) and, when the render can't be had, to check the clips themselves (say then that captions, text layers and the end card were not checked).
   - Several Video Editors (cutdowns, languages) → check each one asked for, report each.
3. **The images.** The `url` from `get_run_results` when they were made in this chat; otherwise open the workflow in the browser and open each image node's result, or ask for the links. Statics, carousel cards, sizes, languages: every version.
4. **What it should look like,** to check against:
   - the script: the scenes, the lines (who says what and when), on-screen text marked for post, the CTA;
   - the composition: each clip's `startMs` and `durationMs`, layers (UI inserts, end card, text), the caption track (size, `position`), `canvas.durationMs`;
   - the user's app screenshots and logo (the pink section), for the screen and logo check;
   - the planned text on images (headline, offer, CTA, card text) and the Brand Kit's app name.
5. No result yet, or the render failed → nothing to check: say so and offer to finish or fix the node first.

## Step 2. Pick the frames (video)

Frames come from the edit, not at random. Build the list from the composition and the script:

| Moment | Frame | Why |
|---|---|---|
| **Start** | 0.0 s (frame 0) | hook text and first caption word visible, no black frame |
| **Every spoken line** | the middle of the line (from the script timing, the VO, or the caption track's words) | face and mouth while speaking, captions over the face, the words |
| **Every cut** | ~0.1 s before and ~0.1 s after the cut (clip boundaries from `startMs`; shot cuts inside a multi-shot clip from the script) | person, outfit, props and place match, no black frame, no half frame |
| **Phone and UI moments** | the middle of each shot where the screen is visible, and of each UI insert | screen text, UI, logo |
| **Hands in action** | the middle of every shot where a hand holds or taps something | fingers, grip |
| **End card** | its first frame and the last frame of the video | complete, logo, offer, CTA, not cut short |

- Merge frames closer than ~0.3 s.
- Usual count: 10–20 frames for 15 s, 15–30 for 30 s, up to ~40 for 60–120 s (short drama: lines and cuts first, hands and screen moments where they are).
- After a `lyra-fix`: only the fixed part, the cut before it and the cut after it.
- Write the list down as a table (time · scene · what to look at) before opening anything: it is also the user's check list if the browser fails.

## Step 3. Take and look at the frames

Needs a browser **signed in to Lyra** (Claude in Chrome or the built-in browser). The result files are protected: they open only with the Lyra sign-in cookie, so they can't be downloaded into a shell, and a browser that isn't signed in gets an XML page with `MissingKey` / "Missing Key-Pair-Id" instead of the video. Then ask the user to sign in to Lyra in that browser (never type their password yourself) and open the file again.

1. **Open the file itself** (the `.mp4` or image link) in a new tab, not the workflow page: an open canvas can write its old state over later tool edits, and on the file's own page the frames can be drawn and measured.
2. **Hide the player controls and seek** to each time on the list:
   ```js
   const v = document.querySelector('video'); v.pause(); v.controls = false;
   v.currentTime = 7.4;
   await new Promise(r => v.addEventListener('seeked', r, { once: true }));
   await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));   // let the frame paint
   ```
   The controls bar covers the bottom of the frame, exactly where captions and the end card button sit: always hide it. Without the two animation frames after `seeked`, the first drawing can come out empty: if a contact sheet is blank, draw it again.
3. **Look at full resolution.** The video in the window is small (a 1080×1920 video shows at ~420×750 px), too small for fingers and screen letters. Draw the frame, or a part of it, into a canvas over the page at its real pixels and take the screenshot of that:
   ```js
   let c = document.getElementById('qc') || Object.assign(document.body.appendChild(document.createElement('canvas')), { id: 'qc' });
   c.style.cssText = 'position:fixed;left:0;top:0;z-index:9;background:#000';
   const [sx, sy, sw, sh] = [300, 650, 480, 480];   // the part to look at, in video pixels
   c.width = c.height = Math.min(innerWidth, innerHeight);
   c.getContext('2d').drawImage(v, sx, sy, sw, sh, 0, 0, c.width, c.height);
   ```
   - **Overview first:** a contact sheet, 6–9 frames of the list drawn small side by side in one canvas, one screenshot. It shows continuity (the same face, outfit, props) at a glance.
   - **Then the details:** a crop of every face, hand, phone screen, caption and logo on the list.
   - Remove the canvas when done (`document.getElementById('qc')?.remove()`).
4. **Images:** open each image link; the same canvas crops for every text block, face, hand and logo. Carousels: every card. Sizes and languages: every version (a resize can drop or squash text; a translation can break letters).
5. **Keep the problem frames.** For every problem, save the crop that shows it (the screenshot or zoom tool's save-to-disk option) to show the user in the report.
6. Close the tabs you opened. If the workflow was open in a tab before, leave it as it was.

**No browser** → Step 7 (check list for the user).

## Step 4. Measure the sound

Claude can't hear, but it can measure. On the file's own page (the render, or a part's `assetUrl`) decode the audio and read its levels:

```js
const buf = await fetch(location.href).then(r => r.arrayBuffer());
const a = await new OfflineAudioContext(1, 44100, 44100).decodeAudioData(buf);
const d = a.getChannelData(0), win = Math.round(a.sampleRate * 0.5);
let rms = [], peak = 0, clip = 0;
for (let i = 0; i < d.length; i += win) {
  let s = 0;
  for (let j = i; j < Math.min(i + win, d.length); j++) { s += d[j] * d[j]; const x = Math.abs(d[j]); if (x > peak) peak = x; if (x > 0.99) clip++; }
  rms.push(Math.round(20 * Math.log10(Math.sqrt(s / win) + 1e-9)));
}
({ dur: a.duration, peak, clipped: clip, rms_dB_every_0_5s: rms.join(' ') })
```

Read it like this:
- **Silence at the start:** the first 0.5 s far below the rest (more than ~20 dB) → the voice or music starts late; the hook loses its first second.
- **A hard stop:** the last 0.5 s drops straight to silence (to −60 dB and lower) from a normal level, with no fade before it → the music or the voice is cut off.
- **Clipping:** samples at full scale (`clipped` > 0, peak ≈ 1.0) → distortion.
- **Too quiet overall:** the loud parts stay below about −30 dB → the whole ad is quiet.
- **Holes:** a 0.5 s block far below its neighbours in the middle → a gap in the voice or a dropout.
- **Length:** the audio ends well before the video, or the render's sound is longer than its picture.
- **Music under the voice:** measure the voice part and the music part separately from their `assetUrl` (the VO node, or the clip with speech; the music node). Apply the volumes from the composition (the clip's `volume` × its track's `volume`; a muted track counts as silent), and compare their levels during the spoken lines. The music should sit **15–20 dB under the voice** while someone speaks (20 dB is the accessibility standard for background sound under speech; 15 dB is the usual floor for social ads). Less than 15 dB → "the music may cover the voice at 0:03–0:08", with the volume to set. Rough guide when both tracks are equally loud: volume 0.1 ≈ −20 dB, 0.15 ≈ −16.5 dB, 0.2 ≈ −14 dB, 0.26 ≈ −11.7 dB.

Report sound as measured ("the music sits about 9 dB under the voice, the end stops without a fade"), never as "the sound is fine". Pronunciation, voice quality and lip sync stay questions to the user.

## Step 5. What to look for in the frames

Look only at what is in the frame; compare with the script, the screenshots and the planned text, not with taste.

**Faces**
- the same person in every scene (face shape, hair, age, skin tone) · eyes aligned and alive, looking where the shot says · teeth and mouth natural, not melted · skin real, not waxy · no extra or half faces in the background.

**Hands and fingers**
- five fingers on each visible hand · no merged, extra or missing fingers · the hand touches what it holds (no floating phone or mug) · one phone in one hand, held the way a person holds it (POV inserts: her own hand from the bottom of the frame, nobody opposite).

**Phone screen and logo**
- screen text word by word against the user's screenshot: app name, headings, buttons, numbers · no invented screens or UI that changes between frames of the same shot · the logo and icon exactly as uploaded: shape, colors, letters, not warped or redrawn · a store badge only as the official file.

**Captions**
- never over a face or the mouth (house default under the faces, ~75% of the height; `lyra-video-editor`) · size 80 on 1080×1920, max 2 lines · first word visible at frame 0 · words against the script: the app name, names, numbers, punctuation and ellipses · inside the platform's safe zone.

**Text on images and on screen**
- every letter and number as planned, the app name exactly · no warped, melted or mirrored letters, no gibberish in the background (signs, books, packaging) · nothing extra the plan didn't have · text inside the safe zone, readable at phone size · no fake system buttons (a play button, a close cross, a fake notification or pop-up): platforms reject ads with them; a store-style install button on the end card is fine.

**Safe zones on 9:16 (1080×1920)** for the hook text, the headline, the CTA, the logo and the end card (captions follow the house place in `lyra-video-editor`, not these):
- Reels and Stories (Meta): keep the top ~14% (~270 px) and the sides ~6% (~65 px) clear; the bottom ~35% (~670 px) on Reels, ~14% on Stories.
- TikTok: keep ~130 px top, ~485 px bottom, ~45 px left and ~140 px right clear (the right side holds the like and share buttons).
- These figures change; when in doubt, use the overlay in the Video Editor or the platform's own template.

**Cuts and the edit**
- no black or empty frame · no jump of person, outfit, accessories (jewellery, glasses, a bag), props, light or place where the script has one continuous scene · the end card complete, not cut, the real offer from the Brand Kit, one CTA.

**Severity**, for every problem found:
- **Blocker:** an ad shouldn't run with it (six fingers in a close-up, a wrong app name, a warped logo, captions over the mouth, a wrong price, the voice cut off).
- **Visible:** a viewer may notice (a face drifts between two cuts, bracelets vanish after a cut, a background sign with gibberish, music close to the voice).
- **Minor:** only on a paused frame (a blurry finger in a fast move at the edge).

Unsure whether it is a defect → report it as "please look at 0:07", not as a problem and not as fine.

## Step 6. Report and the fix offer

One message, short, in the user's language, with the problem frames attached as pictures (each picture captioned with its time and problem):

> Checked **14 frames** and the sound of "Calmly · 2 am · 15 s" (start, 6 lines, 5 cuts, the phone shot, the end card). **2 problems:**
> 1. **0:07, scene 3 (kitchen) · blocker:** six fingers on her right hand around the mug, already in the frame before the cut *(picture)*. Fix: simplify the hand and add "five fingers on each hand" to the image "Scene 3: kitchen", rerun the image, clip 3 and the Video Editor, 361 credits.
> 2. **0:11, phone shot · visible:** the button reads "Strat" instead of "Start" *(picture)*. Fix: an insert of the phone screen from your screenshot over 0:10–0:12, 40 credits.
>
> Clean: the same face in every scene, captions under the faces, the end card complete. Sound: no clipping, the voice starts at 0.3 s, the music sits 15 dB under the voice and fades out on the last frame.
> Please listen whether the app name sounds right, and watch 0:04–0:06 at full speed: I check still frames, so a quick morph between them can slip past.
>
> Fix both through lyra-fix for 401 credits?

- **What was checked:** the number of frames, what they covered, and the sound. Never "checked the video" without the count.
- **Each problem:** time (m:ss) · scene or node label · severity · what is wrong, in plain words · its picture · the fix in one line (the cheapest that works, `lyra-fix` Step 2) · its credits from the nodes' `credits` in `get_workflow`.
- **Clean areas:** one line, so the user knows what passed.
- **Questions for the user:** pronunciation and voice (for a video with speech) and motion in any spot that looked suspicious.
- **No problems:** "Checked 14 frames and the sound, nothing broken", plus the pronunciation question. Don't pad the report.
- **The one question:** fix them through `lyra-fix`? The yes hands over to `lyra-fix` with all problems in one fix round (one plan, one cost, one Video Editor render). Nothing is changed or run in this skill.
- **Links** by the base rules: the result checked and the workflow.

## Step 7. Without a browser: the check list

When no browser is available (no Claude in Chrome, no built-in browser, or it can't open the result):
1. Say it in one line: "I can't open the video from here, so here are the moments to look at."
2. Send the frame table from Step 2 as the user's check list: time · scene · what to look at (fingers on the mug, the button text on the phone, captions under her face…).
3. Add the short checks from Step 5 for faces, hands, screen and logo, captions, text, cuts, end card, and the sound questions (music under the voice, a hard stop at the end, the app name).
4. Ask the user to tell you the times where something is wrong (a screenshot is best). Each one they name goes to `lyra-fix` the same way.

The frame table still comes from the edit: Claude reads the composition and the script with the tools even without a browser, so the times are exact. The sound settings (volumes, muted tracks, fades) can be read from the composition too; report them as settings.

---

## Common mistakes (check)

| Mistake | Prevention |
|---|---|
| Says "looks good" without seeing the result | Look in the browser; otherwise the check list |
| Waits to be asked after a final render | Run the check automatically after every final result |
| Takes the render link from `get_run_results` for a render made in another chat | Results drawer in the Video Editor, or ask for the link |
| Random frames, or one frame per clip | Frames from the edit: every line, both sides of every cut, screen and hand moments, start and end card |
| Player controls left on, covering the captions and the end card | `v.controls = false` before every frame |
| Judges fingers and screen letters on the small video in the window | Canvas crops at the video's real pixels |
| Screen text judged by "looks right" | Word by word against the user's screenshot |
| Caption words not compared with the script | App name, numbers, punctuation, ellipses |
| Says the sound is fine | Report what was measured; pronunciation and lip sync are questions |
| Claims there is no morphing | Frames are still; say so and point to the spots to watch |
| Problems described in words only | Attach the crop of each problem frame |
| Invents a problem to have something to report | Only what is in a frame or measured; unsure → "please look at 0:07" |
| Report without times or frame count | "Checked N frames", every problem with m:ss and scene |
| Fixes the problem straight away | One question; the yes goes to `lyra-fix` |
| One fix round per problem | All problems into one `lyra-fix` round, one render |
| Checks in the workflow tab and leaves tabs open | The file in its own tab; close it after |
| Checks only the master, not the cutdowns, sizes or languages | Every version, each reported |

## Quality gates (check)

- **Before the report:** every frame on the list looked at, at full resolution where it matters? The sound measured? Every problem has a time, a scene, a severity, a picture, a fix and its price? Nothing reported that wasn't seen or measured? The pronunciation question and the motion caveat in where they matter?
- **Pass** = the user knows what was checked, what is broken, what it costs to fix, and what is left for them to listen to or watch.
