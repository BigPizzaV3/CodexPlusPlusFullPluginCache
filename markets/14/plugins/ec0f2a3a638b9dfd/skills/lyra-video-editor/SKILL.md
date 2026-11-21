---
name: lyra-video-editor
description: "Use when assembling or editing a Lyra video, e.g. \"add captions\", \"add an end card\", \"change the music mix\", \"faster pacing\", \"add sound effects\", \"make 30 s and 15 s cutdowns\". The assembly stage of every Lyra video skill (mix, end card, text, captions, pacing, SFX, render check)."
---

# lyra-video-editor

The assembly and finishing skill for every Lyra video. The video skills (`lyra-video-ad-generation`, UGC, hooks, UI motion, short drama, copy competitor, variations, concept multiplier, fix) make the pieces: clips, voiceover, music, end card. This skill puts them together in the Video Editor. It mixes the sound, adds text, captions and SFX, sets the pace, renders, checks the render and cuts the short versions.

Use for "edit / assemble the video", "stitch the clips", "add captions / subtitles", "music quieter", "fade the music", "add an end card", "make it more dynamic", "add a sound effect", "cut a 30 s / 15 s version", "make cutdowns", "Remotion render failed", or as the assembly stage of every Lyra video skill.

**This file is the only source for the Video Editor and captions.** Every other Lyra skill points here for them.

**Core rules come from the base skill.** Part 1 of `lyra-video-ad-generation` holds the shared steps: one approval message, pre-run check, credits, picking a result, links, variations, open canvas, runtime failures. Canvas changes (new Video Editor nodes for cutdowns, a "Final" section) follow `lyra-workflow-layout`.

**When it runs.**
- **As stage 3 of a video skill.** The video skill's plan already has the Video Editor node, and its approval message already carries the captions question (with the style choice, Captions below). Run this file from Step 2.
- **On its own.** The user asks to edit, assemble, add captions, change the music, add an end card, make it more dynamic or cut short versions of an existing video. Start at Step 1.

---

## The Video Editor in Lyra (checked in Lyra, Oct 2026)

- **Node:** `video_composer` (`create_video_composer_node`), label "Final: …". **0 credits.** Lyra renders it with Remotion; a render takes ~20 to 40 s.
- **The edit lives in `video_rendering_composition`**, read with `get_workflow`, written with `update_node`. **The whole edit can be built by the tools, without opening the editor:** a composition sent with `update_node` renders as is, even with no node connected. Always read the whole composition first, change only what's needed, send it back whole, then `get_workflow` to check it held.
- **Opening the editor in the UI** (Claude's browser or the user) is needed only for what the tools can't do: the **Captions** button (transcription). Everything else is a composition field.

### Composition fields (as Lyra saves them)

```
canvas: { fps: 24, width: 1080, height: 1920, durationMs }
safeZone: "instagramReels" | … (editor guide only, not rendered)
tracks: [
  { kind: "video", name, locked, visible, clips: [
      { id, kind: "video", assetUrl, sourceNodeId, sourceResultUuid, sourceDurationMs,
        startMs, durationMs, trim: { sourceStartMs, sourceEndMs }, volume,
        position: { x, y, width, height },          // zoom / crop / split screen
        speed: 2,                                    // 0.25 to 4
        freezeAtMs: 3052.5,                          // freeze frame: its own clip, trim start = end
        transitionOut: { kind: "whipLeft", durationMs: 450 } } ] },
  { kind: "audio", name: "Music" | "Voiceover" | "Audio", role: "music", volume, muted, sourceNodeId, clips: [
      { id, kind: "audio", assetUrl, startMs, durationMs, trim, volume, sourceNodeId, sourceResultUuid } ] },
  { kind: "text", name, clips: [
      { id, kind: "text", content, startMs, durationMs, position: { x, y }, align: "center",
        font: { family: "Inter", sizePx: 75, weightPx: 800 }, color: "#1f2937",
        style: { presetId, strokeColor, strokeWidthEm, backgroundColor },
        effects: [ { id, kind: "popIn" } ] } ] },
  { kind: "caption", name: "Captions", font: { family, sizePx }, styleId: "outline",
    animation: { kind: "activeWordColor" }, highlightColor: "#8FB8FF",
    position: { x: 540, y: 1440 }, sourceCaptionUuid,
    clips: [ { id, kind: "caption", startMs, durationMs,
               words: [ { text, startMs, endMs } ] } ] }
]
```

Field values seen so far: transition `whipLeft`; effect `popIn`; caption styles `outline` (white text with an outline, no box) and `blackBox` (a box), caption animations `activeWordColor` (the spoken word changes colour, no box) and `activeWordHighlight` (a coloured box behind the spoken word), `highlightColor` on the caption track (Lyra's default is yellow `#FDE047`); text preset `karaoke`. For any other kind or preset, set it once in the editor UI and read back the name Lyra saves. Never invent a value.

### What the editor offers (UI names)

- **Speed** 0.25× to 4× (slider, presets). The clip's length follows; the clips after it shift.
- **Freeze**: holds the frame under the playhead for 2 s; drag its edge to lengthen it.
- **Layers** (on the timeline labels): mute (audio only), hide, lock, delete, rename (double-click), reorder (drag or arrows); **+ Layer** adds an empty track. The top layer is in front. Audio layers are named after their source (Music, Voiceover, Audio); each music result gets its own layer.
- **Sources** dropdown: every connected input, with a count; a source already in use can't be added twice.
- **Effects** (Effects tab, preview cards): Motion / Camera (shake, bounce, float…), Entrance (fade, slide, scale / zoom, pop, bounce, blur, spin, drop in), Exit (the same out), Reveal (typewriter, word by word, line by line, wipe, mask), Attention (pulse, flash, glow, RGB split, glitch, blur…). Each has a duration; some have start time, intensity, direction and colour.
- **Transitions** (19): fade, fade to black, cross dissolve, dip to white, slide left / right / up / down, push, zoom in, zoom out, pull in, whip pan left / right, blur, flash, glitch, spin, swipe / wipe. Length 0.25, 0.5 or 1 s. A transition belongs to the right edge of the clip on its left and overlaps the two clips. It also works across tracks and gaps. Not on a locked layer. The old node field `transition_effect` is not used by the timeline: use `transitionOut`.
- **Text**: the same styles as captions, plus outline, shadow, background, caps, italic, letter spacing; 12 extra fonts; default size 75.
- **Captions**: Captions button, style presets (about 26), animations (style default, active word highlight, active word pop, karaoke highlight, word by word, phrase by phrase, active word bounce, active word colour), highlight colour, an Edit tab to fix the words.
- **Canvas**: resolution 480p to 4K, framing Fit / Fill / Zoom.
- **Safe zones**: TikTok, Instagram Reels, Instagram Stories, YouTube Shorts guides, saved per node, not rendered. The Reels guide in Lyra marks the clear area at about 14% to 65% of the height.
- **Results** (left of Render): past renders; opens by itself when a render finishes.

### Known behaviour (check every time)

| Behaviour | What to do |
|---|---|
| **A variation plus an opened editor gives an empty edit.** In a new variation the results get new ids, and opening the editor deletes every track while marking the sources as added, so nothing comes back. The render then fails ("Remotion render failed") or is empty | After `create_variation`, read the Video Editor's composition. If its tracks are empty or point to old results, rebuild it with `update_node`: the same clips, each with its `sourceNodeId` and the variation's own `sourceResultUuid` (the ids now listed in `absorbedSourceNodeIds`). Say it in one line. |
| **An empty edit doesn't render** ("Remotion render failed"): no clips on the tracks, inputs without results, lost connections | Never run it empty. Pre-render check below. |
| **A black tail after speed, transitions or trims.** Clips get shorter; `canvas.durationMs` doesn't always follow, and the render ends on black | Set `canvas.durationMs` = the end of the last clip (startMs + durationMs), in whole seconds where possible. Check the last frame of the render. |
| **A clip is pinned to one result** (`sourceResultUuid`, `assetUrl`). After a clip is rerun or another result is picked, the edit still plays the old one | After any rerun, compare each clip's `assetUrl` with the result you want (`get_run_results`) and update it. |
| **A node connected after the edit exists isn't added.** The editor adds new inputs only when it is opened | Add the clip (a new VO, music, insert) to the composition yourself with its `assetUrl`, `sourceNodeId`, `sourceResultUuid`. |
| **A deleted clip comes back** while its node is still connected | To drop a source for good, also `disconnect_nodes` on the canvas. |
| **Edit Video is disabled** when no video node is connected | Connect at least one video node, or build the edit by the tools. |
| **Captions on a video without speech** stay "Parsing…" forever. **With speech** they take about a minute | Captions only on speech; wait up to ~90 s; no track after that → tell the user. |
| **Whispered or quiet speech is transcribed in part** (whole lines missing) | Word check against the script, always (Captions below). |
| **The editor may cut clips to 5 s on opening** (reported, not reproduced) | After any opening of the editor, read the composition and restore clip lengths and trims. |
| **An open canvas or editor tab writes its old state over tool edits** | Before `update_node`, the workflow tab (the user's and Claude's) is moved off the workflow; reopen it after to show the result. |
| **Black preview at 00:00** in the editor | A preview bug, not the render. |

---

## Step 1. Read what's there

1. `get_workflow`: the Video Editor node(s), their inputs and each input's selected result. No Video Editor yet → `create_video_composer_node`, label "Final: {length}", in the "Final" section on the right (`lyra-workflow-layout`), inputs connected in playback order. **Every new Video Editor gets its own rose section and STEP note right away**, by `lyra-workflow-layout`, also when Claude only came to edit. In the user's own workflow nothing else is moved or renamed without a yes: add the editor's section, then offer the full tidy-up in one line (sections, STEP notes, "(copy)" labels, stray nodes).
2. Read the composition. Empty or stale (variation, rerun) → rebuild it (Known behaviour). **No composition yet and the clips were made in another chat** (so `get_run_results` can't give their file links): open the Video Editor once in the browser; it imports the connected clips with their `assetUrl`, `sourceResultUuid` and real lengths. Do the Captions step in the same opening if captions are wanted, then close it and work by the tools.
3. From the script, collect: playback order, each scene's start and end second inside each clip (cut points), the VO text and length, the music length, the end card, the on-screen text lines (marked for post), the keywords, the CTA.
4. A missing result (a clip still running or failed) → finish or fix that node first (`lyra-fix`); never edit around a gap.

## Step 2. Plan the edit

A short timeline, readable in under a minute:

| Time | Video | Above | Sound |
|---|---|---|---|
| 0–3 s | Clip 1, 0–3 s (hook), punch-in at 1.5 s | Text "POV: 2 am, brain won't stop" (pop in) | VO from 0.3 s · music 0.15 |
| 3–11 s | Clip 1, 3–11 s, punch-in at 6 s | UI insert 6–9 s · keyword "1 minute" at 7.2 s | VO · music 0.15 |
| 11–13 s | Clip 1, 11–13 s | — | VO ends 13.8 s |
| 13–15 s | End card 2 s | — | music resolves, fade-out 1 s |

Plus one line each: captions (yes / no; no box, the highlight colour and where it comes from), transitions (cuts by default), resolution and framing (1080p, Fill), cutdowns if asked.

**Approval.** The editor is free, so a plan with only edits runs straight after it. Captions yes / no is always the user's choice, asked once (Captions below). New paid nodes (a short VO or music for a cutdown) go into one message with their credits (base Steps 3 and 6).

## Step 3. Build the edit

1. **Composition by the tools** (`update_node`): order, trims, splits for punch-ins, speed, freeze, transitions, text and keyword clips, audio tracks (and SFX only if asked), volumes, mute, canvas length.
2. **Captions** (only if the user said yes): the one UI step. Open the Video Editor in Claude's browser, press Captions, wait for the words (up to ~90 s), apply the house style (outline, active word colour) or the box the user asked for, set the highlight colour from the video or Brand Kit, set size 80, leave the editor (or set `styleId`, `animation`, `highlightColor` by the tools afterwards). **Captions are timed to the source clip.** When the edit cuts or moves the clips, shift every caption clip and word by the same offset as the clip it sits on (`startMs` and each word's `startMs` / `endMs`), and drop the words that fall in cut-out parts. Then read the composition again: set `position {540, 1440}` on the caption track (there is no height field in the UI), restore any clip lengths that changed, `update_node`, `get_workflow`. Without a browser, ask the user to press Captions and say when the track is there; then set the rest by the tools.
3. Pre-render check, render, edit check, then `lyra-result-check` (Steps 4 to 6).

### Video: order, trims, pace

- **Order:** clips in the script's order; `startMs` of each = the end of the one before. No gaps or black frames unless planned.
- **Trims:** `trim.sourceStartMs / sourceEndMs` to the planned seconds; `durationMs` = the trimmed length (÷ speed). Cut on action, at a scene boundary or at the end of a spoken line, never mid-word.
- **Pace (default for ads):** the picture changes every **2 to 3 s**. A change is any of: a cut inside the clip, a punch-in, a text or keyword pop, a UI insert or B-roll, a transition. In the **7 to 10 s** window put one stronger interrupt (a punch-in plus a keyword, a new angle, the app moment): viewers decide around then whether to stay. For Google App campaigns, at least two changes in the first 5 s. A slow, calm concept (ASMR, meditation, luxury) keeps its slow pace; follow the concept, say it in the plan.
- **Punch-in zoom (cheap cut without a new generation):** split the clip into two clips with the same `assetUrl` (the first trimmed to the cut point, the second starting there) and give the second a larger `position`, centered on the face or the subject: scale 1.15 to 1.3 (scale around the face point P = (px, py) from the clip's current `position`: width × s, height × s, x = px − s × (px − x), y = py − s × (py − y); e.g. s 1.25 on a face at (540, 620) gives x −135, y ≈ −165, 1350 × 2421). Alternate normal and punched-in on a talking head. Not when the zoom would crop the hands, the phone screen or the text in the frame.
- **Layers:** the main video at the bottom; UI inserts, logo, B-roll, text above, trimmed to their moment. A UI insert covers the broken screen moment exactly (base Reference D). Split screen: two video clips side by side with their `position` (e.g. 540 × 1920 each, Fill).
- **Speed:** 1.1× to 1.5× to tighten a slow clip or land a beat, instead of a new generation. Not on clips with speech (the voice changes with it).
- **Freeze:** to hold the last frame under the CTA, or to stretch a clip short by 1 to 2 s.
- **Transitions:** hard cuts by default. A transition only between different places or times, one kind per ad, 0.25 to 0.5 s; whip pan or zoom for energy, cross dissolve for calm. Every transition shortens the total: fix `canvas.durationMs`.
- **Effects:** for a reason: an entrance on text, a slow push-in (Motion / Camera) on a still image or the end card, an attention pulse on the CTA. No effects on faces in UGC.
- **Canvas:** 1080×1920, 1080p (720p for drafts, 4K only when asked); Fill by default, Fit when a clip of another ratio must stay whole.

### Audio: voiceover, music, clip sound, SFX

- **Voice first.** VO at full volume, starting 0.2 to 0.5 s in, ending ~1 s before the video (base Reference C). Too long → shorter text or a faster voice; never stretch the video.
- **Music:** under speech 0.1 to 0.2 (default 0.15); without speech it can lead (about 0.6 to 0.8). Trimmed to the video, ending on a musical resolve, ~1 s fade-out on the last frame (in the editor on the music clip; no fade field seen in the composition yet). One music track per ad.
- **Clip sound:** a clip with speech keeps its sound and must have no music inside (one that has it is rerun, base Reference C); a clip without speech is muted (or ~0.2 ambience) under our music.
- **Sound effects (SFX).** Not added by default and not asked about every time. Where they come from, in this order:
  1. **In the video itself (default).** Sounds of the action (a bubble pop, a phone buzz, a door, a splash, a whoosh of a fast camera move) are written into the clip's video prompt in the sound line, and Seedance generates them with the clip (sound on). The video skills do this when they write the prompts (base Reference C); the editor adds nothing.
  2. **The user asks for a specific sound at the editing stage** (or a sound the clip didn't get): generate it in Lyra with an audio music node on **ElevenLabs** (`create_audio_music_generation_node`, `elevenlabs/music`). The prompt describes only the sound, e.g. "a single short soft whoosh, airy, no music, no melody, no rhythm", `force_instrumental` on, `music_length_ms` 5000 (the minimum, ≈ 7 credits). Trim it to the sound in the editor and place it on its own audio track named "SFX" at the planned moment, volume 0.3 to 0.6, never on top of a key spoken word. Its credits go in the same message as the plan.
  3. **The ElevenLabs sound doesn't work for the user:** say so and ask the user to send the sound file; upload it (`create_upload` / `open_upload_widget`, `attach_upload`) and place it the same way. Never invent a link.
- Several languages: one Video Editor per language, each with its own VO and captions.

### End card

- The last **2 to 4 s** (2 s in 15 s, 3 s in 30 s and longer), whole seconds, ending exactly on `canvas.durationMs`.
- From the video skill (an end card clip or image; `lyra-ui-motion-video` makes store-style ones). Text missing from the image (price, disclaimer) is a text clip, never generated. The CTA said in the VO and shown on screen in the last 2 to 3 s. Inside the safe zone.

### On-screen text and keywords

- **Lines marked for post** in the script (hook ≤40 characters, key message, CTA). Never generated inside a clip. Hook text from frame 0 of the hook.
- **Keywords:** 1 to 3 words of the VO or dialogue that carry the message (a number, the pain, the benefit, the app name) pop up as their own text clip **right after the word is spoken**: `startMs` = the word's start + ~0.1 s (from the caption words' timing or the VO script pace), on screen 0.8 to 1.5 s, an entrance effect (pop in, scale in). 2 to 4 per 15 s ad. With captions on, pick a keyword the captions don't show at that moment, or let the caption highlight carry it: the same words twice on screen at once read as noise.
- **Placement:** inside the safe zone (about 14% to 65% of the height on Reels), never over a face, never on the caption band (captions sit at 75%): keywords and headlines in the upper half (y ≈ 300 to 900); when the face fills that band (a centered talking head), between the face and the captions (y ≈ 1100 to 1250, on the chest, never on the hands holding the phone).
- **Style:** one text preset per ad, brand fonts and colours from the Brand Kit, high contrast; size 75 to 110 for keywords, 75 for longer lines. The same colour rule as captions: a keyword box or text colour from the Brand Kit, the logo or the video (e.g. white text on the video's own dark blue), never the default yellow.

## Captions

- **Ask first, never by default.** Captions yes or no is the user's choice, in the one approval message. Recommend yes for any ad with speech (most people watch muted).
- **House style: no box.** White text with a thin outline (`styleId: "outline"`), the spoken word in colour (`animation: activeWordColor`). A box (`blackBox`, or `activeWordHighlight`, which puts a box behind the spoken word) only when the user asks for one, or when the text can't be read without it (a busy, bright background), said in the plan.
- **The colour is never Lyra's default yellow.** Set `highlightColor` (and the box colour, if there is a box) to fit the video: the Brand Kit's accent colour or the logo's colour first; no Brand Kit → a colour taken from the video itself (its key object, UI, light) or a neutral (white, light grey, a soft tint of the video's palette). Yellow only when it is the brand's or the video's own colour. It must read clearly on the frames where captions sit; check it in the edit check. Say the colour and where it comes from in the plan ("captions white, spoken word light blue from the Windows title bar").
- **Made only by the Captions button** (Step 3). Only on speech.
- **Size 80** on 1080×1920 (Lyra creates 115). Max 2 lines.
- **At 75% of the height** (the house default): caption track `position {x: 540, y: 1440}` (0.75 × height on other canvases). Lyra's own default is lower (~88%), so always set it. On close-ups this lands under the mouth, on wide shots at chest level. Never over a face or the mouth: if a face sits there, move the captions lower (y ≈ 1530, at most 1650). If the user wants them elsewhere, place them there. Don't pull them up into the red Reels frame.
- **Word check against the script, every time**, in the Edit tab or in the composition's `words`: the app name, names, numbers, punctuation, ellipses, and missing lines (whispers and quiet speech drop whole phrases). Missing words are added with their timing from the script pace.
- The first word visible from its first frame (an entrance animation can hide it).
- After any change to the VO or the clips, captions are made again and checked again.

## Step 4. Pre-render check

Right before every Video Editor run (base Step 5 plus these):
- every input has a result; each clip's `assetUrl` / `sourceResultUuid` is the result agreed (not an old one);
- the composition is not empty: a video track with clips;
- clip lengths and trims as planned, none cut to 5 s; `startMs` in a row; no gaps or overlaps except transitions;
- `canvas.durationMs` = the end of the last clip; no black tail;
- VO ends ~1 s before the end; music trimmed, at its volume, fade on the last frame; clips without speech muted, clips with speech not; any SFX not on key words;
- picture changes every 2 to 3 s (unless the concept is slow), an interrupt at 7 to 10 s;
- captions as answered: no box (unless asked), highlight colour from the Brand Kit or the video (not the default yellow), size 80, `position` y 1440, words checked;
- text, keywords and end card inside the safe zone, off faces and off the caption band;
- 1080×1920, 1080p, Fill / Fit as planned.

## Step 5. Render

`run_node` on the Video Editor; `get_run_results` until it is done (never run it twice while it runs). "Remotion render failed" → almost always an empty or stale composition: Pre-render check, fix, render again (free).

## Step 6. Edit check, then the full check

**Edit check (this skill, before the report).** A quick look only at what the edit itself can break, in Claude's browser signed in to Lyra: open the result `url` in its own tab, hide the controls, seek with JavaScript and look at:
- 0.1 s: the hook frame and its text;
- 0.2 s before the end: no black tail, the end card whole;
- one frame inside each caption phrase: no box (unless asked), the highlight colour readable and fitting the video, at 75%, the words right;
- each punch-in and keyword: faces still in frame, keywords off faces and off the caption band.
An edit problem found here (black tail, wrong caption place, a keyword over a face) is fixed in the composition straight away (free) and rendered again. Close the tab. No browser → skip to the full check.

**Full check → `lyra-result-check`.** Faces, hands, phone screen and logo, cuts, all text, and the measured sound (levels, music under the voice, hard stop) are checked by `lyra-result-check`, which runs automatically after every final render and goes into the final report. Don't repeat its checks here.

## Step 7. Report

Base link rules: one video → the video link + the workflow link; several (cutdowns, languages) → the workflow link and the label of each Video Editor.

> Calmly · "2 am" · final 15 s: done. Video: {url} · Workflow: https://app.lyra.splitmetrics.com/workflows/{uuid}. Edit: 6 picture changes, punch-ins at 1.5 and 6 s, keywords "2 am" and "1 minute", captions (no box, the spoken word in the brand's teal) at 75%, end card 2 s. Editor renders are free. (The full check from `lyra-result-check` follows in the same report.)

---

## Short versions: 59, 30 and 15 s

One finished ad gives several lengths. Make only versions shorter than the master. 59 s (not 60) fits every Meta placement; 30 s and 15 s are the main test lengths.

**How.** Each version is **its own Video Editor node** (no new video credits), label "Cut: 30 s", in the "Final" section next to the master, its composition built by the tools from the master's clips. Same variation as the master, unless the user asks for another one.

| Version | Structure | Rule |
|---|---|---|
| **59 s** | the master minus the weakest scenes: one pain or problem scene and one payoff or proof scene | hook, the app moment and the end card stay whole |
| **30 s** | hook 3 s · problem 6 to 8 s · the app / turn 8 to 10 s · result 5 to 7 s · end card 2 to 3 s | one beat per part, the strongest take of each |
| **15 s** | hook 3 s · the app or result in one beat 9 to 10 s · end card 2 s | the hook and the app in the same ad, nothing else |

- **The same hook** opens every version. A new hook is `lyra-video-hooks`, not a cutdown.
- **Cut only at scene boundaries** or at the end of a spoken line, from the script's scene times (none → write them first and check with the user).
- **Voiceover:** a VO across scenes doesn't survive cuts. Each version gets **its own short VO** on the same voice, ~1 s shorter than the version (≈ 2 credits). In-clip dialogue: cut between lines.
- **Music:** the master's track trimmed with a 1 s fade, ending on a resolve; or a short music node (version + 5 s, 1.25 credits per second) when the cut lands badly.
- **Pace, keywords and any SFX** re-placed for the version's timing; **end card** in every version; **captions** made again (Captions per Video Editor) and checked.
- Each version gets the Pre-render check, the edit check and `lyra-result-check`.
- **Plan in one message:** the versions, what each drops, the new VO / music nodes and their credits (editors are free), the captions answer. After the yes, build and render all versions.
- **Names:** the master's code with the length (`…-59cut`, `…-30cut`, `…-15cut`); node labels "Cut: 59 s", "Cut: 30 s", "Cut: 15 s".

---

## Common mistakes (Video Editor)

| Mistake | Prevention |
|---|---|
| Opens the editor in a new variation and renders an empty edit | Read the composition after `create_variation`; rebuild it by the tools |
| Runs an empty Video Editor ("Remotion render failed") | Pre-render check: clips on the tracks |
| Adds a Video Editor and leaves it outside any section, with no STEP note | Step 1: its own rose section and STEP note by `lyra-workflow-layout`; offer the tidy-up of the rest |
| A black tail at the end after speed, transitions or trims | `canvas.durationMs` = the end of the last clip; check the last frame |
| The edit plays an old take after a rerun | Update each clip's `assetUrl` / `sourceResultUuid` |
| Connects a new VO after the edit exists and expects it to appear | Add it to the composition yourself |
| Rebuilds the composition from memory, drops captions or volumes | Read the whole composition, change only the needed fields |
| Invents a transition, effect or style name | Use the names seen in Lyra, or set it once in the UI and read it back |
| Uses `transition_effect` on the node for transitions | `transitionOut` on the clip |
| Captions added without asking | Ask yes / no in the approval message |
| Captions with a box by default, or left in Lyra's yellow | No box; highlight colour from the Brand Kit, the logo or the video |
| Captions left at 115 or at Lyra's ~88% default | Size 80, `position {540, 1440}` |
| Caption words not checked (whispers drop lines, app name, punctuation) | Word check against the script every time |
| Presses Captions on a video without speech | Captions only on speech |
| A static talking head for 15 s | A change every 2 to 3 s; punch-ins; an interrupt at 7 to 10 s |
| A punch-in that crops the hands, the phone screen or the text | Pick another moment or a smaller scale |
| Keywords over a face or on the caption band | Upper half, inside the safe zone |
| Adds or asks about SFX on every ad | Action sounds go into the video prompt; editor SFX only when the user asks |
| SFX on top of a key word, or too loud | On edit points, volume 0.3 to 0.6 |
| Invents an SFX file or link | ElevenLabs music node; if it doesn't work, ask the user for the file |
| Music over the voice, ending early or stopping hard | 0.1 to 0.2 under speech, trimmed, 1 s fade |
| A clip with speech muted to kill its music | Rerun it with the no-music sound line |
| Speed on a talking clip | Avoid; the voice changes |
| Edits with the workflow open in a tab | Move the tab off first, reopen after |
| Reports a render without looking at it | Edit check (Step 6), then `lyra-result-check` |
| A 30 s cut made by cutting the master's VO mid-sentence | Its own short VO per version |

## Quality gates (final video)

**Edit check (Step 6):** no black tail, the planned length · the hook frame and its text at 0 s · captions without a box, the highlight colour from the brand or the video, size 80, at 75%, the words as in the script · punch-ins keep faces in frame · keywords off faces and off the caption band · the end card complete.

**Everything else** (faces, hands, screen, logo, cuts, text, the measured sound, and the questions to the user about pronunciation and voice) → `lyra-result-check`.

**Versions:** each cutdown keeps the hook, the app moment and the end card, with its own VO and captions.

Pass = every point that applies is fine. Fix only what fails; editor fixes are free and render again at once.
