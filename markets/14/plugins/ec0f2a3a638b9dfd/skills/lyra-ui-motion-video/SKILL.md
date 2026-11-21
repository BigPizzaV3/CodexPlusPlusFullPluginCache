---
name: lyra-ui-motion-video
description: "Use when the user wants their app's real screens in a creative, e.g. \"animate my app screens\", \"UI motion ad\", \"floating phone video\", \"show the app in the video\", \"end card with install button\", \"packshot like the App Store\", \"App Store / Google Play screenshots\", \"screenshot set\". Builds UI motion videos, store-style end cards and store screenshot sets in Lyra with UI text kept exact."
---

# lyra-ui-motion-video

Mini skill for everything where **the app's interface is on screen**: UI motion video ads, UI moments inside other videos, the store-style end card, and App Store / Google Play screenshot sets. Its one job above all: **the UI the viewer sees is the UI the user sent**, with every word, number, icon and color the same.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**Our UI is almost always a mobile app.** Most Lyra users are mobile apps, so "UI" here means the app's own screens on a phone (iOS or Android), its icon, its logo and its store presence. Websites, dashboards and desktop software follow the same rules.

**This is a way of thinking, not a script.** The rules below are defaults and good practice; use judgment and say why in one line when you choose differently. Fixed: **UI fidelity** (the rules in the next section), truth (no features, numbers, ratings or badges the app doesn't have), the Brand Kit's facts, Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-video-ad-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, prompt rules, models (Reference A), audio (C), app UI (D), consistency (E), prompt craft (F), errors (G), de-slop (H), Brand Kit (I), Meta app ads (J). This file adds what is specific to UI. If the two disagree, the user wins, then this file, then the base skill.

**Other skills point here for UI.** A hook that shows the app (`lyra-video-hooks`), a UGC creator with a phone moment (`lyra-ugc-video`), any base-skill ad with a screen: their UI moments follow this file's fidelity rules, model choice and checks. This skill itself owns videos where **the interface and the brand are the main character**, the end card, and store screenshot sets.

---

## UI fidelity rules (hard)

1. **Never invent or change anything in the UI.** No new screens, buttons, labels, numbers, icons, colors, fonts or layout; no "cleaning up", simplifying, translating or modernising the app. If it isn't in the user's screenshots, it isn't on screen.
2. **Every text that appears on a screen is identical to the user's screenshot**, letter for letter, number for number, including small labels, tab names, prices and dates. Maximum accuracy, every frame.
3. **Screenshots only** as the source (never ask for a screen recording). No screenshot for a moment → the screen faces away, is dark, or is blurred.
4. **No text generated into a video.** No subtitles, captions, headlines, stickers, price tags or overlays in a video prompt. Any text the ad needs (headline, caption, CTA, offer) is added **in the Video Editor** on top of the finished clips. The only text a video model may show is the UI text already inside the frame image it animates, and the prompt tells it to keep that text unchanged.
5. **Every image that combines the screenshot with something else** (the character holding the phone, a phone on a backdrop, an end card, a store screenshot) **is checked against the screenshot before any video is made from it**: every word, number and icon. A wrong letter in a frame becomes a wrong letter in the whole video.
6. **The more UI, the shorter and simpler the clip.** A lot of UI is split into several small clips (one screen or one state each), joined in the Video Editor.
7. **When in doubt, lay the real file on top.** Anything that must be read word for word and keeps failing in generation goes into the Video Editor as the original screenshot, logo or end card image.

## Screens: ask first, then work with what you get

**Always ask about the screens before planning a UI video**, in one message (with the other Step 1 questions):
- Which screens should be in the video, and how many? Please send a screenshot of each.
- In what order should they appear?
- What should happen on screen: **where to tap** (which button or element), what scrolls, what opens, what appears after the tap? For every action, a screenshot of the screen **after** it.
- Anything on the screens that must not be shown (personal data, unreleased features)?

**Work with exactly what the user gives. Never invent.**
- **One screenshot → one-screen video.** Build it on that screen alone: float, slow push-in, light sweep, button glow, card lift, the end card. A tap only as a press effect on the same screen; **no next screen, no new state, no new element** that isn't in the screenshot. Say once in the plan that more screenshots (with the after-state) would allow a tap-through demo; if the user says one screen is enough, do one screen, without pushing.
- **The user says "only one screen"** → one screen, done well.
- **Several screens** → help the user get the best result with all of them: order them as a story (the pain or the start → the action → the result), one clip per screen or state, a tap as the cause between two states (first + last frame), every frame checked.
- **An action without its after-screenshot** → ask for it; if there is none, show only the start state (the tap lands, nothing new appears) or cut away from the screen.

**Check the screenshot quality as soon as they arrive.** Look (when you can see them) or ask: is the resolution enough (ideally the short side about 1080 px or more), is it sharp, without heavy compression, cropped edges, personal data, notifications or a cluttered status bar?
- Not good enough → ask once: "Do you have sharper originals? A PNG export straight from the phone or from the design file (Figma) works best."
- No better ones → **improve the screenshot in Nano Banana Pro** before using it: an Image Generation node with the screenshot connected, same ratio, the highest resolution: "Upscale and sharpen this app screenshot. Keep it exactly as supplied: the same layout, every word, number, icon and color. Do not redesign, translate, add or remove anything; only remove blur, noise and compression artifacts." Then **check the improved version word by word against the original with the user**; it becomes the source only after that check. It never "fixes" content; anything unreadable in the original stays as it is or is asked for.

## Setting expectations: UI is hard for AI video

Say it once, in the plan, in plain words: **an app screen is one of the hardest things for AI video.** When the screen moves, small letters and numbers can drift or change for a moment. That's why the build is careful: clean sharp screenshots, checked frames, Seedance 2.0 frames for screen shots, small motion, short clips, and a check of every result. The aim is a **good result on the first or second run**; when a letter still drifts, only that piece is fixed (rerun with less motion, a Seedance 2.0 insert, or the exact screenshot laid on top), not the whole video. Never promise pixel-perfect UI in a moving shot; pixel-perfect is what layers in the Video Editor give.

## The fidelity ladder

Put every element on the lowest rung it can live on:

| Rung | How the element gets into the video | Exactness | Motion | Use for |
|---|---|---|---|---|
| **1. Layer** | the original file (screenshot, logo, icon, end card, text card) as an **image layer in the Video Editor** (position, size, duration) | pixel-perfect, no model touches it | none on the layer itself; motion comes from the clip under it and from the cut | logo, CTA, offer, store badges, headlines, any screen that must be read word for word |
| **2. Frame** | the screenshot or a checked design frame as **first frame**, and a second exact state as **last frame** if the screen changes, on **Seedance 2.0** | the picture is kept; small drift possible | small: glow, pulse, float, slow push-in, a tap, a short slide | **the default for UI**: hero screens, UI inserts, state changes, the end card coming alive |
| **3. Reference** | the screenshot or phone image as a **reference** on Seedance 2.5 (or 2.0) | layout kept, small text can drift | free | the phone moment inside a person-led video on Seedance 2.5 (checked; fixed with a 2.0 frame insert if needed); screens that are small or supporting |
| **4. Prompt only** | the model draws it from text | none | free | only abstract brand motion: gradients, light, shapes, particles in brand colors. **Never** UI, text or a logo |

**Rule of thumb:** the more readable text an element carries, the less it moves and the lower its rung.

## Which model for UI

**Two models, chosen by who leads the shot:**

- **The screen leads → Seedance 2.0.** Lyra's own model for UI/UX and moving text; it takes images as **frames** (kept exactly). Use it for UI motion, floating phones, cards, demos, UI inserts and the end card.
- **A person leads → Seedance 2.5.** When the video is mostly a realistic person (UGC, talking head, lifestyle, a scene with a lot of human action), the main clip is **Seedance 2.5** with references: the character image and the phone shot (character + screenshot). Seedance 2.5 is the best model for people and also handles a phone moment well.

**Person + UI: the two-step method.**
1. Make the person's clip on **Seedance 2.5** with the phone shot as a reference, and **check how the UI behaves** in it with the user: the screen identical to the screenshot through the whole moment (first, middle, last frame), no morphing text, the tap in the right place.
2. **If the UI breaks** (or the UI moment is long or important, so plan it from the start): make a **separate UI-only clip on Seedance 2.0** with the phone shot (or the screenshot) as **frame**, a few seconds of the screen with a finger tap or a small move, and lay it over that moment in the Video Editor (layer above the main clip, trimmed to the moment). The person's acting stays from 2.5, the exact UI comes from 2.0.

| Situation | Model | How images connect | Clip |
|---|---|---|---|
| **The screen leads** (UI motion, floating phone, cards, demo) | **Seedance 2.0** | **frames** (first, + last for a state change) | 4 to 6 s, one screen or one state |
| **A separate screen or UI insert** to lay over the main video in the Video Editor | **Seedance 2.0** | **frames, never references** | 3 to 5 s, trimmed to the moment |
| **A video mostly with a realistic person**, UI in it (UGC, talking head, lifestyle) | **Seedance 2.5** for the main clip | references only (character image + phone shot) | as the scene; **check the UI**; if it breaks, a separate **Seedance 2.0 UI-only clip with frames** laid over that moment |
| **A short phone moment where the screen matters more than the person** | **Seedance 2.0** | frames | 3 to 5 s, cut into the person's video |
| **A lot of UI** (several screens, many small texts, a flow) | **Seedance 2.0** | frames | **split**: one clip per screen or state, 4 to 6 s each, joined in the Video Editor |
| An exact change from state A to state B (tap, toggle, result appears) | **Seedance 2.0** (Kling 3.0 Pro as the alternative) | first frame = A, last frame = B | 4 to 5 s, one tap |
| The end card coming alive | **Seedance 2.0** | frame | 3 to 4 s |
| Brand motion background behind layered UI | Seedance 2.0 | prompt only (no text) | 8 to 10 s |

Never: an image as first/last frame on Seedance 2.5 (error) · frames and references mixed in one node · one long busy clip carrying the whole UI story · 1080p without the user choosing it (720p by default; Seedance 2.0 Fast and Mini can't do 1080p).

**How much UI is "a lot".** Split when a clip would show more than one screen, more than one state change, a scroll through a list, or small text the viewer is supposed to read. Keep it in one clip when the UI is a single screen glimpsed for 1 to 3 s inside a bigger scene.

---

## How to think about UI motion

**What it is.** A short ad where the app is shown as designed objects in motion: a phone with the real screen floating in a brand-colored space, screens sliding in as cards, a button pulsing, a finger tapping and the result appearing, the icon bouncing into the end card, a headline landing between screens. It sells by showing **what the app looks like and what it does**, cleanly and fast. It works for apps whose UI is attractive or whose result is visible on the screen (a plan, a chart, a scan, a finished edit, a balance).

**Motion that keeps text safe vs motion that breaks it:**

| Safe (default) | Risky (only with frames and a check, or as a layer) | Breaks text (avoid on anything with text) |
|---|---|---|
| locked camera · slow push-in or pull-out · gentle float or drift · fade · slide in from an edge and stop · small scale from center · light sweep or glow across the glass · soft shadow and depth · button pulse · small icon bounce · one finger tap · a card lifting a little off the screen · background motion behind the UI | A → B with first + last frame · a short scroll of a few rows · a card fanning out of a stack · the screen expanding to fill the frame · a toggle or check mark switching | rotation, flips, orbits around the phone · deep 3D perspective · heavy bounce or elastic stretch · one screen morphing into another without both states given · letter-by-letter typing · counting numbers · several text elements moving at once · long fast scrolls · whip pans across UI · the phone turning so the screen goes out of view and back |

**Principles:**

- **Real screens, not redrawn ones.** Real screens build trust and show what the viewer will actually get.
- **One product moment per video.** One key screen or one "aha" (the plan appears, the chart fills, the scan finds it), not a walkthrough. A second feature is a second video.
- **One primary movement + one supporting movement per shot.** Everything else is still, and the prompt says so.
- **Describe stillness as much as motion.** What isn't mentioned gets guessed: "the screen content and all text stay perfectly still and sharp" is as important as the motion line.
- **Let the screen rest.** A screen that must be read stays still for at least 1.5 to 2 s.
- **One look.** Light or dark, not both; flat 2D or 2.5D depth over heavy 3D (3D only when it shows a real object); the brand palette; glass, glow and gradients only if they match the brand.

---

## Lifehacks for UI in AI video and images

What practitioners and Lyra's own templates do to keep UI exact (2026):

1. **Start from the sharpest possible source.** Full-resolution PNG screenshots of the current version; small type blurs and shifts first, so the screen should take a large part of the frame (about half the frame height or more for a read moment).
2. **Clean the screenshot before anything else:** no personal data, notifications, carrier names, debug bars or placeholder text; full battery and signal icons. Ask the user for a clean one rather than letting a model "fix" it.
3. **Crop and compose at the video's ratio** (9:16) with margin around anything that will move, so the model never has to extend the picture by inventing content.
4. **Give every image one job, and say it.** "[the first frame] is the exact start of the clip; [the last frame] is the exact end"; "[Image2] is the phone screen; reproduce it exactly". An image without a stated job leaks or gets redrawn.
5. **Name the anchors, briefly.** "keep the layout, every text, icon and color exactly as in the image"; then list the 3 to 5 most important visible texts in quotes so the model and the checker know them.
6. **Lock the camera, then add one move.** Test in steps: first the UI still with only light moving; then one slow push-in; then one small action (a tap). If the UI drifts, reduce motion before changing anything else.
7. **Use a carrier.** Let one stable element (the phone outline, the logo, a light source) persist through the shot; viewers track it and small artifacts hide.
8. **Hard change → two passes.** For a big transformation, generate a stable midpoint first (A → mid, then mid → B with first + last frame) and cut them together, instead of one clip that morphs.
9. **Short beats long.** UI clips around 4 s (Lyra's own tip); a 4 to 6 s clip is trimmed to the 1.5 to 3 s that look perfect.
10. **Overlay what must be exact.** Generated footage carries the scene, motion and light; the exact screenshot, logo, price or legal line goes on top as a layer for the moment it must be read (the phone static or nearly static under it).
11. **Change one variable per rerun** (motion, wording, or the frame), never several, and never rerun an unchanged prompt.
12. **Check three frames of every clip:** the first, the middle and the last. Text that is right at the ends can still wobble in the middle.
13. **End every prompt with "no new text, no captions, no subtitles, no watermark, no UI redesign".**

---

## Step 1 additions: assets and fidelity map

1. **Brand Kit** as in base Reference I, plus what UI work needs most: brand colors (hex), positioning, the offer and CTA, store links, the real store rating if one may be shown, must include / must exclude, forbidden claims.
2. **Ask for the assets in one message** (screenshots only), together with the screen questions above (which screens, order, where to tap, what appears after):
   - **2 to 5 clean screenshots** of the key screens, current version, full resolution (PNG).
   - For a state change (button pressed, toggle, result appears): **two screenshots, before and after**.
   - For other markets: **screenshots of the localized app**, one set per language (UI is never machine-translated).
   - **Logo** (transparent PNG), **app icon**, the **end card** if they have one, the brand font name.
   - **Official store badges** ("Download on the App Store", "Get it on Google Play") as files, if the end card uses them; never generated.
3. **Fidelity map** (a user text node "Fidelity map"): for every element, one line: element · source file · rung · model · allowed motion · the exact texts on it. Example:
   > Hero screen "Tonight's plan" · screenshot 2 · frame · seedance-2.0 · float + slow push-in · texts: "Tonight's plan", "Wind down", "5 min", "Start"
   > Button "Start" pressed · screenshots 2 → 3 · first + last frame · seedance-2.0 · one tap · texts: "Start" → "Breathing", "5:00"
   > End card · end-card.png · frame, then layer · seedance-2.0 · icon bounce, button pulse · texts: "Calmly", "Sleep in 5 minutes", "Install"
   > Logo · logo.png · layer · none
4. **Defaults (state, don't ask):** Reels / TikTok · 9:16 · **15 s** (6 to 20 s for social) · English · no person on camera unless the concept needs one · voiceover on, or music-led with captions added in the Video Editor · music on, instrumental · **Seedance 2.0 with frames, 720p** (1080p on the user's choice), sound on · Nano Banana Pro for every design frame, 9:16, 2K · clips 4 to 6 s joined in the Video Editor · **store-style end card** 2 to 3 s at the end.

**Recommended first run:** A. Design frames (every frame the clips start or end on, the phone shots and the end card; cheap, and they decide whether the UI is right).

## Step 2 addition: the concept

Per video: **product moment** (one screen or result) · **style** (style library) · **look** (light / dark, palette, depth) · **shot list** with timing, each shot's element, rung, model and motion · **text plan** (every headline, caption and CTA line word for word, all marked "Video Editor") · **audio** (VO words counted, or music-led) · **end card** (iOS, Android or both).

> C1 · floating hero phone · Calmly · dark navy, violet glow, 2.5D · 0 to 2 s: the phone already drifting up into frame, screen "Tonight's plan" (frame, 2.0) · 2 to 6 s: slow push-in, a finger taps "Start", the screen switches to "Breathing, 5:00" (first + last frame, 2.0) · 6 to 9 s: the timer card lifts slightly off the screen (frame, 2.0) · 9 to 12 s: brand motion background, three lines land one by one in the Video Editor: "5 min", "No ads", "Works offline" · 12 to 15 s: store-style end card, icon bounce, "Install" pulses (frame, 2.0; badge as a layer) · VO 30 words · music: soft electronic, 90 BPM, hit on the tap.

The first frame is already moving and reads as a thumbnail. For a test with several openings, take hooks from `lyra-video-hooks`.

---

## Style library

A reference, not a menu. Combine and adapt.

| Style | What it looks like | Good for | Build note |
|---|---|---|---|
| **Floating hero phone** (default) | a phone with the real screen in a clean brand-colored space, slow push-in, light sweep on the glass | any app with one strong screen | design frame → Seedance 2.0 first frame, 5 s, micro-motion |
| **Hand or robotic hand showcase** | a hand holds the phone to camera, only micro-movements, the screen stays front-facing | premium, tech | Lyra template "Robotic Hand Showcase"; the hand barely moves |
| **Tap-through micro-demo** | a finger taps one button, the screen changes to the result | the core action | screenshot A and B as first + last frame; one tap; 4 to 5 s |
| **Card stack / fan-out** | several screens as floating cards in depth, sliding in one after another | several features at a glance, one per card | one clip per card (frames), or cards as layers over a brand motion background |
| **UI pop-out** | one element (a card, a chart, a badge) lifts out of the screen toward camera | the "aha" result | first frame flat, last frame with the element lifted; small distance; its text checked |
| **Kinetic type + UI** | short bold headlines land between screens or beside the phone | a big idea, sound-off viewing | headlines in the Video Editor; screens as frame clips; one line at a time |
| **Brand motion background** | gradients, waves, shapes, particles in brand colors behind layered UI and logo | end cards, transitions, budget builds | the only prompt-only clip; no text, no logo; everything readable laid on top |
| **Screen to world** | the UI expands from the phone onto a billboard, a wall, a sky screen | launches, scale | the screenshot placed into the scene with Nano Banana Pro ("replace the image on the billboard with the second reference image"); Lyra template "Global Billboard Swipe" |
| **Person + phone moment** | a realistic person uses the phone, the screen is the hero for a moment | when a human reaction sells it | `lyra-ugc-video` for the person; the phone shot and UI insert by this file |
| **Store-style end card** | the closing 2 to 3 s: icon, name, benefit line, rating, install button, store badge | **the end of almost every app ad** | see below |

**Lyra templates that fit** (re-check `list_templates`; search by title): **Robotic Hand Showcase** · **Phone Screen Reveal** · **Global Billboard Swipe** · **Billboard App Reveal** · **Swipe Away the Chaos**. When adapting: keep 720p by default, 1080p on the user's choice (some run at 720p), switch UI clips to Seedance 2.0 with frames, replace the template's uploads with the user's screenshots and logo, remove stacks like "8K, hyper-detailed", keep the fidelity lines.

---

## The phone shot: screenshot + character or scene in one image

Whenever the screenshot is combined with a person, a hand, a phone on a backdrop or a place (base Reference D, UGC phone moments, screen to world), the combining happens in **one Image Generation node** (Nano Banana Pro) with the character or scene image and the screenshot connected:

- The prompt gives each input its job: "[Image1] is the woman: face, hair, hoodie, room and light. [Image2] is the app screen: display it on the phone exactly as supplied."
- Fidelity line, always: "Preserve the screen exactly: the same layout, typography, spacing, icons, colors and every word and number. Do not redesign, simplify, translate or add anything to the interface."
- Then list the key visible texts in quotes ("Tonight's plan", "5 min", "Start").
- Phone almost front-facing to camera (tilt up to about 15°), the screen large, no fingers or reflections covering text, a generic modern phone without a brand logo.
- **Check with the user before any clip:** "Compare the phone screen with your screenshot word by word: titles, buttons, numbers, small labels, icons, colors. Anything different?" Even one wrong character → rerun the image (cheap), with the wrong text named in the prompt ("the button reads exactly 'Start', not 'Stat'").
- After two failed reruns: make the screen larger in the frame and simplify the pose; if it still fails, keep the screen turned away in the person's shot and show the UI as a separate Seedance 2.0 frame insert or as the screenshot layer.

## The store-style end card (packshot)

Most app ads end on a short **back shot / end card styled like the app's store page**: the app icon, the app name, a short benefit line, the rating, an **Install / Get** button and the App Store or Google Play badge, in the brand's colors. It is the CTA moment, 2 to 3 s, and it should be on almost every ad.

**What goes on it (all from real data):**
- App icon and app name exactly as in the store.
- One benefit line or the offer (≤40 characters), from the Brand Kit ("Sleep in 5 minutes", "7 days free").
- Rating and review count **only if real** and the user or Brand Kit gives them; otherwise leave the rating out.
- Button: "Install" (Google Play style) or "Get" (App Store style), or the brand's CTA ("Try it free"). One CTA.
- The **official** store badge files from the user, as a layer; never generated, never redrawn.

**Platform versions.** Make an **iOS version** (App Store badge, "Get") and an **Android version** (Google Play badge, "Install") when the campaign runs on both; everything else identical. The card is styled *like* a store page (clean white or brand background, rounded icon, button shape), not a copy of the real store screen, and never shows fake numbers, fake reviews or the OS system UI.

**How to build it:**
1. **The user has an end card file** → it goes in as an image layer for the last 2 to 3 s (rung 1); for a little life, the same file as **first frame on Seedance 2.0**, 3 to 4 s: "the app icon bounces in slightly and settles, the Install button pulses softly once; every text and the layout stay exactly as in the image", then the original file as a layer for the final hold if any letter drifted.
2. **No end card** → design it as an image (Nano Banana Pro, 9:16): the uploaded app icon connected, every text written in the prompt in quotes, brand colors, generous space; the store badge left out of the image and added as a layer. **Check every letter with the user**; then animate it as above.
3. Text the end card needs that isn't in the image (a price, a disclaimer) → Video Editor text, never generated.

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the video is | Best approach (graph) | Models |
|---|---|---|
| **Default: 15 s UI motion ad** | uploads (screenshots, logo, icon, badges) → one design frame per shot (screenshot connected, "exactly as supplied") → **one Seedance 2.0 clip per shot, 4 to 6 s, design frame as first frame** (+ last frame for a state change), motion-only prompt → end card (frame clip) → Video Editor: clips in order + text and layers + VO + music | nano-banana-pro · seedance-2.0 |
| **A lot of person, some UI** (UGC, talking head, lifestyle) | character image + phone shot → main clip on **Seedance 2.5** (both as references) → UI check with the user → if the screen came out wrong (or the UI moment is planned as important), a **separate UI-only clip on Seedance 2.0 with the phone shot as frame**, laid over that moment in the Video Editor | seedance-2.5 + seedance-2.0 |
| A lot of UI in one ad | split: one clip per screen or state, Seedance 2.0 frames, joined in the Video Editor; no clip carries more than one screen change | seedance-2.0 |
| A state change | screenshot A and B (or checked design frames of both) → first + last frame, one tap | seedance-2.0 (kling-v3-video Pro as alternative) |
| A screen that must be read word for word | the clip moves the phone; for the read moment, the exact screenshot laid over the screen area (phone still), or a 1.5 to 2 s hold of the design frame as an image clip | video_composer |
| Headlines, offer, CTA, captions | Video Editor only (text tool, or a transparent PNG text card from the user's designer); never in a generation prompt | video_composer |
| Animate an existing static ad or end card | the image as first frame on Seedance 2.0; the prompt says what moves when and what stays | seedance-2.0 |
| Many variants, tight budget | design frames for all; clips on seedance-2.0-fast (720p) for tries; the winner rerun on seedance-2.0 (720p, or 1080p on the user's choice) | seedance-2.0-fast |
| Store screenshot set | see "Store screenshot sets" below | nano-banana-pro |

**Why several clips here, not the base skill's one clip.** UI needs exact frames per shot, one of the base skill's reasons to split (Step 2); say it in one line of the plan. **Connections (base Step 4):** connect the whole graph at build time. An uploaded screenshot can be a first or last frame right away; a generated design frame becomes a frame link right after it has a result (say this in the plan and make the link automatically before running the clip). Keep count 1 on design frames when the user picks option C.

**Design frames.** The exact picture a clip starts (or ends) on, made before any video: Nano Banana Pro, 9:16, 2K, the screenshot connected; the screen shows **the reference image exactly as supplied**; the phone almost front-facing, the screen large; the background from the brand palette; space left for the text that comes later in the Video Editor, inside the safe zone. When the shot is just the screen itself (no phone), the uploaded screenshot can be the frame directly, with no image generation at all: the safest option.

**Video Editor.** One `video_composer` per final. Video tracks in playback order; image tracks above for screenshots, text cards, logo, badges (position x/y/width/height, duration, opacity). Layers are static. Clip sound muted or lowered under VO and music. All headlines, captions and the CTA are added here; tell the user exactly which text to add or check and where. End card 2 to 3 s at the end.

**Layout.** Section "Assets" (uploads + "Fidelity map") → Section "Design frames" (phone shots, end card) → Section "Clips" → Section "Audio" → Section "Final". Labels: "Frame: hero phone · Tonight's plan", "Clip 2: tap Start (A→B)", "End card: iOS", "Final: C1 · floating hero phone".

## Run options

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option. **A. Design frames (recommended):** phone shots, design frames and end card, count 1 (2 for the hero frame if the user wants a choice) · **B. Clips** for the frames the user approved, with VO and music · **C. Everything** → the Video Editor. C only if the user accepts unchecked frames; the fidelity check is why A comes first.

---

## Store screenshot sets (App Store / Google Play)

Static images, not video: a set of store screenshots built around the app's real screens, plus variants to test. Same fidelity rules; here the screenshot is the product.

**Specs (check App Store Connect and Play Console before export; they change):**

| | App Store (iPhone) | Google Play (phone) |
|---|---|---|
| Size | 6.9" base: **1320 × 2868** or **1290 × 2796** px portrait (6.5": 1284 × 2778); exact pixels required | **9:16**, at least **1080 × 1920** for recommendation eligibility; any side 320 to 3840 px, long side ≤ 2× short side |
| Count | up to **10** per localization | **2 to 8** per device type (at least 4 for large-format eligibility) |
| Format | PNG (best for UI text) or JPEG, RGB, no transparency | JPEG or 24-bit PNG, no alpha |
| Content | must show the real in-app UI; device frames optional but must not misrepresent the UI; no "#1" / "best", no "Download now", no mention of other platforms, no URLs or QR codes | the real in-app experience; text ≤ 20% of the image, no small text; **no** "Best", "#1", "Top", "New", "Discount", "Sale", "Million downloads"; **no** "Download now", "Try now"; **no** store badges, device imagery or third-party logos; clean status bar |

**What a good set does:** the first 2 to 3 screenshots carry the main value (most visitors never scroll); one message per screenshot: one short caption (2 to 6 words, large, high contrast) + one UI focus; the set tells a story from the main benefit to supporting features; one consistent style (background, type, caption position); localized per market from localized app screenshots.

**How to build it in Lyra:**
1. Plan the set in a text node "Store set": per slot, the screenshot file, the caption word for word, the background, device or no device (Google Play: no device frame).
2. One Image Generation node per slot (Nano Banana Pro, the screenshot connected, the tallest ratio `list_node_configs` offers for the App Store, 9:16 for Google Play, the highest resolution): "Place the supplied app screen exactly as supplied, unchanged, [in a modern phone / as a flat screen with rounded corners] on a [brand background]. Caption at the top, exactly: '…'. No other text." The caption is the only text the image model writes; everything on the screen comes from the screenshot.
3. **Check every slot with the user**: the screen identical to the screenshot, the caption spelled right. Rerun what fails, naming the wrong text.
4. Exact pixel sizes: adapt with the Image Resize node (`lyra-image-resize`) where it gives the target ratio; for exact App Store pixels the final crop or canvas is set in a design tool by the user's designer. Say this up front.
5. Never use the Image Translation node on screenshots with UI: it would translate the interface. Other languages = the localized app's screenshots + the caption written in that language.

**Variants to test** (Apple Product Page Optimization, Google Play store listing experiments): change one thing per variant: the **first screenshot** (which screen leads) · the **caption angle** (outcome "Sleep in 5 minutes" vs feature "Guided wind-down timer") · the **style** (light vs dark, device vs flat screen) · the **order** of the set. Different ideas = different nodes; more takes of one idea = `count`.

---

## Prompt rules (UI)

| Node | Write | Avoid |
|---|---|---|
| Fidelity map (text node) | every element with source, rung, model, motion and its exact texts; the shot list; every Video Editor text line word for word | text meant to be generated |
| Design frame / phone shot (image) | each input's job → the device and how it's held or placed → "the screen displays [ImageN] exactly as supplied; preserve the layout, typography, spacing, icons, colors and every word and number; do not redesign, simplify, translate or add anything" → the key texts in quotes → backdrop from the brand palette → soft light, controlled glass reflections → composition (screen front-facing, large, legible, space for editor text, central 65%) → "no other text, no captions, no watermark" | "8K, hyper-detailed" stacks; a phone brand logo; extra UI or widgets; strong tilt; fingers or glare over text |
| UI clip with a frame (Seedance 2.0) | task line → "Treat the image as frame 0; keep the layout, every text, icon and color exactly as in the image" → timeline: what moves, when, one element at a time, small amplitudes → **what stays still** → camera (locked, or one slow push-in) → end state, "holds in final position" → sound line → avoid line → the list of texts visible in the last frame | re-describing the look; rotation, flips, orbits; any new text, numbers or captions; several elements at once |
| Clip with first + last frame | "The first image is the exact start, the last image is the exact end. Continuous transition: …" one physical cause (a tap, a slide); what stays identical in both | a third state; motion the two frames don't explain |
| Brand motion background | abstract shapes, gradients, light and particles in the brand colors, slow looping motion, empty center | any text, letters, numbers, logos, icons, UI |
| Sound line (every clip) | "Sound: only soft UI sounds (a light click on the tap, a soft whoosh); no music, no speech, no voice" | leaving it open |
| End card image | the icon connected; app name, benefit line, button label in quotes; brand colors; space for the badge layer | generated badges, ratings that aren't real, more than one CTA |
| VO and music | base Reference C | artist names; VO repeating what the viewer reads |

**Pattern: UI clip from a frame (Seedance 2.0, first frame).**

> Short motion design shot for an app ad. Treat the image as frame 0: keep the phone, the screen layout and every text, icon and color exactly as in the image. 0 to 1 s: the phone drifts up a few centimeters and settles. 1 to 3 s: the camera makes one slow push-in toward the screen. 3 to 4 s: the "Start" button glows softly once. 4 to 5 s: a gentle light sweep crosses the glass; everything holds in its final position. The screen content, all text and the icons stay perfectly still and sharp the whole time; only the phone, the light and the button glow move. Sound: only a soft airy whoosh and a light click; no music, no speech. Avoid: new text, captions, subtitles, text morphing, letters changing, extra icons, UI redesign, rotation, perspective distortion, flicker, warping, watermark. Text visible in the last frame: "Tonight's plan", "Wind down", "5 min", "Start".

**Pattern: phone shot (Nano Banana Pro, two inputs).**

> UGC phone photo. [Image1] is Mia: her face, curly hair in a loose bun, grey hoodie, her dark bedroom and warm lamp light. [Image2] is the app screen. Mia holds a modern smartphone close to the camera, screen facing us, almost straight on, her thumb at the lower edge away from any text. The phone screen displays [Image2] exactly as supplied: preserve the layout, typography, spacing, icons, colors and every word and number; do not redesign, simplify, translate or add anything. Visible on screen: "Tonight's plan", "Wind down", "5 min", "Start". Natural skin texture, phone-camera look, deep focus, soft lamp light, no glare over the screen. No other text, no captions, no watermark, no phone brand logo.

---

## Truth and fidelity

- UI only from real, current screenshots; no screen, feature, number, result or badge the app doesn't have. The ad promise matches the store page.
- Ratings, review counts, awards, "#1", user counts: only real, from the Brand Kit or the user, and only on the end card or as editor text.
- Store badges: only the official files; no OS system UI copies; no third-party logos or real phone brand marks.
- **Ads, not store previews.** A generated motion video is a paid ad. Apple's App Store preview videos must use real screen captures of the app; Google Play's preview video should show the real in-app experience. If the user wants a store preview video, say so and suggest a cut from real captures.
- **Brand safety** (Lyra's System Preamble, base Reference B): no profanity, no political statements, no unsubstantiated health claims, no competitor disparagement. The Brand Kit's **forbidden claims are enforced absolutely**, in every headline, caption, end card, visual and VO; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.

## Common mistakes (UI)

| Mistake | Prevention |
|---|---|
| The model "fixes", simplifies or redraws the UI | Screenshots only; "exactly as supplied" in every prompt; check before clips |
| A UI video planned without asking which screens, in what order, where to tap | Screen questions first (Screens: ask first) |
| The next screen or a new state invented when there is only one screenshot | One screenshot → one-screen video; ask for the after-screenshot |
| More screens pushed after the user said one is enough | One screen, done well |
| A blurry or compressed screenshot used as is | Ask for better originals, or improve in Nano Banana Pro and check word by word |
| Pixel-perfect UI promised in a moving shot | Say once that UI is hard; aim for the first or second run; fix only the broken piece |
| A wrong letter in the phone shot carried into the video | Word-by-word check of every combined image before any clip |
| Text morphs during the motion | Seedance 2.0 frames, smaller motion, shorter clip, or a layer for the read |
| Subtitles, headlines, price or CTA written into a video prompt | Video Editor only |
| Seedance 2.5 or references used for a UI insert | Seedance 2.0 with frames |
| Seedance 2.0 forced on a person-led video | Person leads → Seedance 2.5; UI fixed with a 2.0 insert if needed |
| UI in a 2.5 person clip not checked | Check the screen on the first, middle and last frame with the user before the edit |
| Image connected as a frame on Seedance 2.5 (error) | 2.5 = references only |
| One long clip carrying the whole UI story | One screen or state per clip, 4 to 6 s, joined in the Video Editor |
| Screen-to-screen morph with only one state given | First + last frame, one tap as the cause |
| Rotation, orbit or deep 3D around a readable screen | Push-in, drift, slide, glow |
| Store badge, rating or review count generated or invented | Official badge files as layers; real numbers or none |
| No end card, or an end card with three CTAs | Store-style end card on every ad, one CTA |
| Image Translation used on UI screenshots | Localized app screenshots; only captions are written per language |
| Store screenshot with "Download now", "#1", badges (Google Play) | The store rules table |
| 1080p without the user choosing it | 720p by default; 1080p on Seedance 2.0 when the user picks it |

## Quality gates (UI)

- **Stage 0 (concept, Claude checks before sending):** screens, order and tap points confirmed with the user, and nothing planned beyond the screenshots received? Screenshot quality checked (better originals asked for, or improved and checked)? The "UI is hard" line said once? One product moment? Every element on the lowest rung it can live on? Seedance 2.0 with frames for every screen-led shot and insert, Seedance 2.5 for person-led clips with a UI check planned? A lot of UI split into short clips? No text in any video prompt except the "keep exactly" lines? Every editor text line written word for word? End card planned?
- **Stage 1 (design frames, phone shots, end card):** every word, number and icon on the screen identical to the screenshot? Nothing added, nothing missing? Screen large and legible at phone size? End card texts spelled right, rating real or absent? Look on brand?
- **Stage 2 (clips):** pause on the first, middle and last frame: does any letter, number or icon change? Only the planned elements move? Smooth, no flicker or warping? State changes match the after-screenshot? Ends held on the planned frame?
- **Stage 3 (final):** first frame moving and readable? One product moment clear in one watch? Readable screens rest long enough? Editor text one line at a time, in the safe zone, the same words as the VO? End card 2 to 3 s with the right badge per platform? Music under VO, no clip music? 9:16, planned resolution (720p by default), planned length? Named with its code?
- **Store sets:** every screen identical to its screenshot? Captions spelled right and within the store rules? Sizes exact for each store? First 3 slots carry the main value?

## Deliverable and naming

1. A "Fidelity map" text node.
2. Design frames, phone shots, the end card (iOS / Android), clips and the Video Editor.
3. One finished video per concept; or a store set per platform and variant.

Videos: `B{batch}-A:{angle}-F:UIMotion-{style}-C{concept}` (add `H{n}` when a hook from `lyra-video-hooks` opens it; add `-iOS` / `-Android` for end card versions), e.g. `B4-A:PlanInOneTap-F:UIMotion-HeroPhone-C1-iOS`. Store sets: `Store-{iOS|GP}-{locale}-V{variant}`, e.g. `Store-GP-en-V2`.

## After the test

Read it as in `lyra-video-hooks` (After the test). The style, the product moment and the end card are hypotheses: say which won. Store sets: judge by store conversion (page view → install) in Product Page Optimization or store listing experiments. Then offer: the winning style on another feature, a UGC version of the same moment (`lyra-ugc-video`), new hooks on the winner, other sizes (recompose 4:5 or 1:1, don't crop) or languages (localized screenshots, new editor text).

---

## Store requirements

Store requirements (sizes, counts, content rules) change: check them in App Store Connect and Google Play Console before export.
