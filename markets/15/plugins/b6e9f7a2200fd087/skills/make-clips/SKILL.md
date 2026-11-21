---
name: make-clips
description: Turn the user's videos (15 seconds to 45 minutes, e.g. talking-head videos, webinars, podcasts, lives, interviews; up to 5 videos combined into one clip, also reusing videos uploaded before) into a short 9:16 clip of a chosen target length with captions, a chosen cut pace, soft transitions and an optional hook at the start. Use when the user wants to edit or cut a video, make a clip/Reel/Short/TikTok, shorten a long video, combine several takes, remove "ähm" and pauses, add subtitles/captions, or asks "Turn my video into a clip" (or "Mach aus meinem Video einen Clip").
---

Oracut analyses, cuts and renders; you guide the user and check the result.

Words: **captions** (Untertitel) are the subtitles burned into the clip, made from the spoken words – no AI text. The **hook** is a short, catchy line of the clip (no set length) that plays once more at the very start – never the line the clip opens with.

1. Get the videos in: `open_oracut` – the user uploads 1 to 5 videos there or picks videos uploaded before (they become one clip; the order does not matter – the AI finds the best take of each part and the best order) and picks the target length (15–180 s, default 60), captions on/off, the cut pace (slow, medium – default –, fast), soft transitions (on by default), the hook (on by default) and optionally what the clip should focus on (typed or spoken). Videos attached in the chat cannot be used – always send the user to the upload window. A clip costs 1 credit per started minute of all its videos, at least 2 credits, and 4K costs extra (`get_account` shows the balance). Landscape videos either become 9:16 with the frame following the speaker or stay landscape on a blurred or coloured background, optionally with a headline at the top. Ask for the target length only if the user gave none and it matters; otherwise use 60 seconds.
2. Poll `get_reel` (at most every 20 seconds) until `status` is `ready`. If it failed, the credits came back automatically.
3. Tell the user in plain words what happened: length before → after, removed filler words and repeated sentences, the hook if there is one, and – for a planned clip (`kind` short) – the core message and which take of which video was used for each part (`plan` in `get_reel`).
4. For a shortened clip check the selection:
   - Does the first sentence (or the hook) grab attention (question, problem, surprising statement)?
   - Is the clip understandable on its own (no "wie vorhin gesagt", no greeting or goodbye)?
   - Does it end with a clear last sentence?
   If not, or if the user wants another passage, pick better sentence ids from `get_reel` (`sentences`, `plan`: another take of a part, another part, or another order) and call `update_reel` with `selectSentences` in play order (near the target length). Pace, transitions and the hook change with `update_reel` too. A changed cut costs credits (`get_reel` `editCredits`, the first fine cut of a clip is free) – tell the user the number and get their OK first. Never invent text: a clip can only contain what was said.
5. A completely new cut with other wishes ("focus on the pricing part", "calmer"): `recut_reel` with `instructions`. It costs credits (`get_reel` `recutCredits`) – tell the user the number and get their OK first.
6. Repeated sentences: check them with `get_duplicate_takes`; ask briefly only if the better take is unclear, then `update_reel` with `keepTakes`.
7. Captions: the editor (`show_reel_editor`) lets the user fix words, pick a caption template, colours (also saved colour presets) and position, then press "Fertigstellen". If the user asks you, use `get_captions` + `update_captions` (presets: `list_color_presets`, `save_color_preset`), then `render_reel_final` (exports in full resolution; after caption changes only it costs credits – `get_reel` `editCredits`, ask first).
8. Download: `export_content` with format `mp4` (or `srt`/`vtt` for the captions). Oracut never posts anything.
