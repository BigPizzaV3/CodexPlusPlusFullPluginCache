---
name: lyra-copy-competitor-static
description: "Use when the user wants to remake a competitor's or reference static ad, banner or carousel for their app, e.g. \"copy this competitor static\", \"make a banner like this one\", \"remake this image ad\", \"do this carousel for us\", \"a static from this competitor video\", or a Meta Ad Library screenshot. Analyses the reference and builds the new static and its variants in Lyra."
---

# lyra-copy-competitor-static

Image mini skill. Takes a static ad that works for someone else, finds out **why** it works, and rebuilds that mechanism as a new static for the user's app: their pain, their feature, their person, their words, their brand. Six jobs in order:

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

1. **Analyse** the reference (Step 1a): the team's static standard (Reference L) plus a production breakdown with the layout map.
2. **Go to the Brand Kit** (Step 1b) and take every fact from it.
3. **Ask the user** how to retell the reference: close remake, free adaptation, or both, with 2 to 3 variations (Step 1c).
4. **Write the new static** (Step 2): transfer map, new texts, side by side, concept card.
5. **Write the new prompt** (Step 2): zone by zone, for Nano Banana Pro.
6. **Generate** the static in Lyra, then offer variants (sizes, languages, persona, headline, animation).

**The Brand Kit is never skipped.** Remake or adaptation, the new static always gets its name, audience, pain, feature, person, words, claims, offer, colors and CTA from the user's Brand Kit (and the user's words in this chat). The reference gives only the mechanism.

**Brand Kit at every step.** The kit is not one step at the start; it is checked at every step:

| Step | What the Brand Kit decides |
|---|---|
| 1. Context | which kit (chat → the workflow's kit → the workspace's kits → ask); `assign_brand_kit` on the workflow so every Lyra node works with it |
| 1a. Analysis | nothing yet: the teardown describes only the reference, so their facts never mix with ours; the kit comes right after |
| 1b. Brand Kit sheet | every field read and written down; gaps marked as hypotheses to confirm |
| 1c. Questions | every mode and variation told with the kit's name, audience, pain, feature and offer |
| 2. Transfer map | every cell in the "Ours" column has its **kit source** (the field, or "user, in chat"); no source → it doesn't go into the ad |
| 2. New texts | tone of voice, customer words, approved claims; forbidden claims and must exclude checked line by line |
| 2. Prompt | palette (kit hex), type style (kit fonts), logo, icon and screenshots from the kit's assets, positioning → polish level, must include |
| 4. Build | the kit assigned to the workflow (and to every Lyra variation made for a variant) |
| 8. Quality | trace check: every word, number, color, claim and asset on the static traced to the kit or the user |
| Variants | other segments, markets and languages come from the kit |

**This is a way of thinking, not a script.** The rules below are defaults and good practice. Use judgment: when a different layout, subject or line serves the user's app better, do it and say why in one line. Fixed: the line between mechanism and identity (next section), truth (no invented claims, reviews or numbers; the competitor's claims are never ours), the Brand Kit's facts, UI fidelity (the user's screenshots, exactly), Lyra's technical limits, and the user's explicit choices.

**Base skill first.** Everything not written here follows `lyra-static-image-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, concept card and layout map, on-image text, realism, styles, models (Reference A), layout library (B), styles (C), realism toolkit (D), persona (E), edits and swaps (F), UI and logo (G), sizes and languages (H), errors (I), de-slop (J), Meta statics (K), Brand Kit (L). This file only adds what is specific to copying a static reference. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.**
- The reference is a **video** and the user wants a video → `lyra-copy-competitor-ad`. A static from a competitor video is built here (Step 1a, static from a video).
- The app's UI in the static, store screenshot sets → `lyra-ui-motion-video` (UI fidelity, phone shot, store rules).
- A persona or a world built for the audience → realism and casting from `lyra-ugc-video`; versions for other segments → `lyra-audience-variations` (its layers and one-story test apply to statics, built with the edit patterns of the base skill).
- Headline lines: the line checks, awareness levels and hook base of `lyra-video-hooks` apply to a static headline (it is the hook of a static).
- New angles on the copied concept → `lyra-ad-concept-multiplier`. Other sizes → `lyra-image-resize`, other languages → `lyra-image-translation`. An animated version → `lyra-ui-motion-video` (UI-led) or `lyra-video-ad-generation`.

---

## What we copy, what we never copy (hard)

A competitor's static is a **proof that a mechanism works on this audience**, not material to reuse. We copy the mechanism, never the identity.

| Copy (the mechanism) | Never copy (the identity) |
|---|---|
| the concept and the angle (the bet the ad makes on the audience) | their brand name, app name, logo, icon, slogan, catchphrases |
| the hook mechanism (`hook_type`: a question, a stat, a before/after, a self-blame line) and the headline's job and shape | their exact headline, subline, labels, chat lines, CTA text (rewritten every time) |
| the composition and the layout map: zones, their order, their rough shares of the frame, the reading order | their photo, illustration, 3D render or any part of their image: never traced, cropped, outpainted or used as a reference for generation by default |
| the text hierarchy and the word budget per block | their people: faces, look; no lookalike; their mascot or characters |
| the type of visual subject (a chat, a result card, a person in the pain moment, a split before/after) | their UI, screens and features (ours come only from our screenshots) |
| the production level (`visual_production`: UGC raw, vector, 3D, collage) | their claims, numbers, ratings, reviews, awards, offer and price |
| the CTA position and type, the offer slot (filled only from our kit) | their palette and trade dress as a whole look; a distinctive typeface; their exact illustration style |

**Rewrite test for every text block.** A block keeps its **job** (callout, question, reframe, proof row, CTA) and may keep its **shape** (a question in the user's voice, three short sentences, "here's your…" + a plan), but its words are new and built from the Brand Kit. No line of ours shares a run of about five words with theirs, unless it is an ordinary phrase anyone would say ("try it free"). If a line only works with their product, it doesn't go in.

**Look test for the whole static.** Put both side by side at phone size (or as thumbnails). Would a viewer think ours is theirs, or made by them? Then too close: change the subject, the palette, the illustration style, the type or the lines until the answer is no. The layout mechanism can be the same; the ad must look like the user's brand.

---

## Two modes: close remake or free adaptation

Both are offered by default (Step 1c); the user picks one or both. **Both run as an A/B on one teardown when the user wants**: same app card, one remake, one adaptation, named so the media buyer sees which is which. Both are built on the Brand Kit.

| | **A. Close remake** | **B. Free adaptation** |
|---|---|---|
| What stays | the same composition and zones in the same order, zone shares within about ±5% of the frame, the same text hierarchy and number of blocks, word count per block within about ±20%, the same type of visual subject, the same production level, the same CTA position and type | the idea, the angle, the hook mechanism, the reading order; everything else is redesigned for the brand |
| What changes | the app name, pain, feature, person or subject, words, palette, type, UI, CTA, offer (all from the Brand Kit) | everything the remake changes, plus the composition, the subject, the production style (often a native phone-real photo for cold traffic), the number of blocks, a layout from the base layout library if one fits better |
| Pick it when | the reference is a proven winner (running a long time, often 60 days or more in Meta Ad Library), the same audience and category, and the mechanism fits the app truthfully | a different audience, category or positioning; the mechanism depends on something the user doesn't have; the reference's look clashes with the brand; or the user wants "the idea, not a copy" |
| Risk | too close to the competitor (run the look test) | losing what made it work (keep the hook mechanism and the reading order) |
| Test value | isolates execution: "does this format work for us too?" | tests the concept in our own voice and look |

---

## Step 1 additions: the reference and the request

1. **The reference.** Ask for it if missing. Accepted sources:
   - **an image file** in the chat, in a connected folder, or a public direct link to the file. JPEG, PNG, WebP. The clean ad image beats a screenshot of the whole feed (small text gets unreadable);
   - **a Meta Ad Library, TikTok or Instagram page link**: a web page, not a file, so it can't be fetched. Ask the user for a screenshot or the downloaded image. Don't retry the page link;
   - **a carousel**: every card, in order, each as its own image;
   - **several statics** for one idea (3 to 5 of the same competitor, or several competitors in the category): all of them, with which one runs longest if known;
   - **a competitor video** to make a static from: the video file (MP4, WebM, MOV) or screenshots of the frames the user likes (Step 1a, static from a video).
   Check `list_uploads` first: the user may have uploaded it already in Lyra.
2. **Why this ad.** In the same message, one line each, all optional: what do you like in it (the layout, the headline, the chat, the look)? How long has it been running; a known winner? Whose ad is it (their app name stays out of everything)? The ad copy, if they have it (title, caption, body, description from Meta Ad Library): it only fills gaps the image doesn't show.
   **Signals of a winner in Meta Ad Library** (signals, not proof): still active after 30 to 60 days or more · the same concept in several versions from the same advertiser (sizes, languages, headlines, people), which usually means it is being scaled · used across several placements. A new ad with no history is a hypothesis, not a proven mechanism: say so, and lean to mode B.
3. **The request.** What the user wants changed or kept ("same but for students", "in Portuguese", "as a carousel", "our mascot instead of a person", "9:16 for Stories"). The user's request wins over the reference.

**Defaults (state, don't ask):** both modes offered, Claude recommends one · the same ratio and placement as the reference (4:5 Feed if unknown; 9:16 when it's a Stories or Reels static; 1:1 when the reference is square) · English, or the language the user asks for · **Nano Banana Pro** for every final, 2K (4K when the static carries small text, a UI screen or a close-up face) · count 2 per concept (the user picks) · the reference **analysed only**, never connected to generation · competitor's name only inside the "Reference teardown" note · variants offered after the first results (After the copy).

**Recommended first run:** A. Finals first (the base skill's option A), remake and adaptation side by side when both were picked. The analysis runs before the plan and costs no credits on Path 2.

---

## Step 1a: analyse the reference

The result is always one **teardown** with two layers, saved in the user text node "Reference teardown":

- **Layer 1, creative classification:** one JSON object in the team's static ad analysis standard (Reference L at the end of this file; the same standard as Lyra's "Ad creative analysis (image)" prompt). It says what the ad **is**, in fixed categories the team can compare across many ads.
- **Layer 2, production breakdown:** what Claude needs to **rebuild** it: the layout map with zone shares, text hierarchy and word counts, subject, style, the bet, why it works, the don't copy list. Layer 1 alone isn't enough for a remake.

### Order of evidence

- **The image is the source of truth.** Ad copy (title, caption, body, description) only fills gaps not visible on the image and never overrides what the image shows.
- Every field rests on evidence. Nothing is invented: a gap in layer 2 is written "not readable" or "not visible"; in layer 1 the source field says `inferred` where the schema allows it.
- Look at the whole image before classifying: the visible headline or hook text, the layout and spatial composition, the main objects, subjects or characters, UI elements, lists, panels, charts, the CTA button, the amount of text against imagery.

### Path 2: Claude's own analysis (default for statics)

Claude can see images, so this is the default and costs no credits.
- **The file is in Claude's environment** (attached in the chat, or staged from a connected folder): open it and look at it directly.
- **Small text:** crop and enlarge the zone before transcribing (a short script, for example PIL: `img.crop((x0,y0,x1,y1)).resize((w*3,h*3))`), or ask the user for a sharper original. Never guess a word: write "not readable" and ask.
- **Zone shares:** measure the zones in pixels (top and bottom of each block divided by the image height), so the layout map has real numbers, not impressions.
- **Colors:** the 2 to 3 dominant colors as hex from the pixels, most dominant first (a short script: downscale, k-means with 3 to 5 clusters, sort by pixel count, drop near-duplicates).
- **No file, only a description:** ask for the image. A static can't be copied from a description.

### Path 1: Lyra's Creative Analysis node

Lyra's analysis node, **Creative Analysis** (action `pattern_import`), can take an image. The MCP tools can **run** and **read** it, but can't **create** it.
1. `get_workflow` on the user's workflow: a Creative Analysis node on the canvas → connect the uploaded reference to it if it isn't (`connect_nodes`), read its price next to Run, say it, run it after a yes, read the output.
2. No such node → don't wait: Path 2. Mention once that the user can add an Upload Image and a Creative Analysis node if they want Lyra's own breakdown next to Claude's.
3. **Output already in the standard** (Reference L) → becomes layer 1 after a check: exact property names, exact enum values, all required fields, `visual_summary` first, `cta_custom_text` when `cta_type` is `custom`, 2 to 5 `key_claims` in the claim format, 2 to 3 hex colors, no extra properties. **Output in another shape** (Lyra's Creative Anatomy: Source, Structure, Message, Execution, Concept Summary) → map it into the standard; fill what it doesn't say from Path 2.
4. The node's output is a source, not the new static. The rewrite is still written by Claude, by this file's rules, from the Brand Kit.

### Layer 1: creative classification (JSON)

Written exactly by Reference L: one valid JSON object, the schema matched literally (exact names, exact enums, no additional properties, all required fields), `visual_summary` first, `key_claims` in the format `"[exact element from creative] — [why it works / what it communicates]"`, `cta_custom_text` when `cta_type` is `custom`, `color_palette` 2 to 3 hex codes. In a pipeline that expects the raw object, return only the JSON, nothing before or after it. In this skill the JSON goes into the "Reference teardown" note, and the user gets a short readable version in Step 1c.

### Layer 2: static production breakdown (template)

Short, factual, one line per field, in the same note under the JSON:

1. **Header:** platform and placement · ratio and pixel size · single image or carousel (number of cards) · whose ad (internal only) · how long it has run, if known.
2. **The bet (one line):** "They bet [audience] will [action] because [concept] addresses [pain] through [mechanism]." This is what we copy.
3. **Layout map** (the heart of a static copy), top to bottom and left to right:

| Zone | From → to (% of height) | What is in it | Exact text | Type: weight, size feel, case, color | Notes |
|---|---|---|---|---|---|
| 1 | 0 → 22% | chat: user bubble right, app bubble left | "…" / "…" | rounded sans, regular, white on grey / on pink | bubbles stylised, not iOS |

4. **Reading order:** what the eye reads first, second, third (and why: size, contrast, position, a face).
5. **Text hierarchy and budget:** each block (hook, headline, subline, rows, CTA) with its word count; total words; share of the frame covered by text.
6. **Visual elements:** the hero (person, mascot, product, phone, chat, table, result) · props · background · light and camera if it's a photo (phone-real or camera-real, lens feel, light source).
7. **Style:** `visual_production` in words, palette, typography style, level of polish, what makes it look native or designed.
8. **The app in the ad:** UI shown or not, which screen, phone or flat card, the result shown, how much of the frame.
9. **CTA and offer:** button text, shape, color, position; offer if any.
10. **Their claims** (from `key_claims` and anything else on the image), listed so we never reuse them.
11. **Why it works:** 2 to 3 short reasons.
12. **Don't copy list:** the identity of this ad by name (their app name, mascot, slogan, illustration style, photo, palette, typeface, exact layout trade dress).
13. **Can't be reproduced truthfully:** what depends on something the user doesn't have (a real review, a rating, a personalised number, a feature, a physical product, a celebrity) and the nearest truthful version.

### Carousels

- **Layer 1 per card:** one JSON per card (the standard reads one image), `format: "carousel"` on each, in the card order.
- **Layer 2 for the set**, plus a **card list:** # · role (hook, problem, feature, proof, offer, CTA) · main visual · exact text · what carries over between cards (the shared anchors: background, type, persona, frame).
- What makes the set work: card 1 is the hook and must stand alone; the swipe promise ("3 reasons…", a story to finish); the last card closes with the CTA. These are mechanism; copy them.
- Remake: the same number of cards and the same role per card. Adaptation: the number may change (2 to 10), the arc stays.

### Several references

1. One teardown per reference (layer 1 and a short layer 2 each), labelled R1, R2, R3.
2. A **pattern sheet** (user text node "Pattern sheet"): the layer 1 fields they share (that shared part is the mechanism the category bets on), what varies between them, which one runs longest. Example: "all three: `hook_type: question`, `composition: chat_ui_layout`, `visual_production: illustration_vector`, CTA as a custom plan button; varies: mascot, palette, offer".
3. The copy is built on the pattern: usually mode B (the shared mechanism in our own execution), or mode A of the strongest single reference. Say which, in one line.
4. Never stitch elements of several competitors into one ad (a headline from R1, a layout from R2, a mascot from R3): that copies three identities. Take the shared mechanism, execute it once in the brand's look.

### Static from a competitor video

When the user wants a static from a competitor's video ad (to test the same concept across placements):
1. **Frames:** with the video file in Claude's environment and ffmpeg: frames every 1 s, plus about 2 per second in the first 3 s (`ffmpeg -i ref.mp4 -vf "fps=1,scale=1080:-1" frames/%03d.png`); without a shell, ask the user for screenshots of the moments they like (at least the first frame, the proof moment, the end card).
2. **Pick the key frame with the user:** usually the hook frame (the first frame, the thumbnail), the proof moment (the result on screen, the reaction), or the end card. Recommend one in one line.
3. **Analyse the key frame with Reference L** (`format: "static_image"`), plus a one-line summary of the video's arc in layer 2, so the static keeps the video's bet. The full video teardown, if the user wants a video too, is `lyra-copy-competitor-ad`.
4. A frame is not a static ad yet: it usually has no headline and no CTA. The copy adds the headline (the video's hook line, rewritten as on-image text, 2 to 8 words) and a CTA from the kit, in clean zones.

---

## Step 1b: the Brand Kit (always, in both modes)

Right after the teardown, before a single line is rewritten. The reference says **how** the static works, the Brand Kit says **what** the new static is about and **who** it talks to. Nothing is taken from the competitor's brand, and nothing is invented to fill a gap.

**Which Brand Kit** (base Reference L):
1. A Brand Kit given in the chat → use it.
2. Otherwise `get_workflow` (the kit assigned to the workflow) and `list_brand_kits` (the kits in the workspace).
3. **Exactly one** candidate → confirm in one line: "I'll make it for {kit name}, right?"
4. **More than one** → ask which, with their names. Never mix two kits in one ad.
5. **None** → ask once: send it here, or should I check and connect one of the workspace's kits? Or type the essentials: app name, what it does, audience, pains, the feature to show, approved claims, forbidden claims, offer, tone, colors (hex), logo, icon and screenshots.
6. Once chosen, `assign_brand_kit` on the workflow if it isn't assigned yet.

**Brand Kit sheet** (top of the "Transfer map" note), one line per field: app name exactly as written · what it does · audience and segments · pains in their words · desires · objections · features (mark the one that answers the reference's pain) · approved claims and proof (real reviews, real ratings, real numbers) · forbidden claims · offer and CTA · tone of voice · positioning (sets the polish level) · colors (hex) and fonts · mascot, if the brand has one · assets (logo, icon, screenshots, product photos, store badges) · markets and languages · must include / must exclude.

**Gaps.** A missing pain → 3 to 5 pain hypotheses in the audience's words, to confirm. Missing screenshots → no screen in the static, or ask for them. No approved claim → no claim. No real review → no review card. No mascot → a persona, an object or an original spot illustration, never a mascot invented to look like theirs. A gap is never filled from the competitor's ad.

**Conflicts.** The user's words win over the kit; name the conflict in one line. If the reference's mechanism clashes with the kit (a meme template for a premium finance brand, a body before/after for a health app, a must exclude), say so and propose the version that keeps the mechanism inside the brand's rules.

## Step 1c: ask the user, and offer variations

One message, after the teardown and the Brand Kit sheet, before any build. Every option is written with the Brand Kit's real name, audience, pain, feature and offer, so the user sees their own static.

1. **The reference in 3 to 4 lines:** the bet, the hook (`hook_type`, the hook text), the layout and look (`composition`, `visual_subject`, `visual_production`), why it works (`key_claims`). Several references: the shared pattern.
2. **The two modes**, told in Brand Kit terms, one recommended:
   - **A. Close remake:** "the same layout zone by zone, but it's {app name}: {pain from the kit}, {feature}, {subject}, {CTA}, in your colors."
   - **B. Free adaptation:** "the same idea and hook, retold for {audience} in {tone}, as {another subject or production style}, ending on {CTA}."
   - **Both as an A/B** (one remake + one adaptation from the same teardown).
3. **2 to 3 variations**, one line each, each built on the Brand Kit, one recommended. Ways to vary (pick what fits):
   - another pain or segment from the kit (the same layout for "students" and for "night-shift nurses");
   - another subject (a person in the pain moment instead of a mascot, the real app screen instead of a chat, a result card);
   - another production level (vector → phone-real photo for cold traffic, raw → elevated for premium);
   - another headline angle on the same layout (question → statement → stat from the kit);
   - another layout from the base layout library with the same bet;
   - another medium: the static as a short animated version (first frame of a video), or a carousel of the same concept.
4. **The CTA and the app.** Unless the reference already carries it in a way that fits: the CTA button with the kit's offer, the real app screen (from a screenshot), the logo or icon small in a corner, or no logo (most native statics don't need one). Ask which.
5. **Only the questions still open**, in the same message: missing kit fields, screenshots, language, ratio, number of cards.

Each variation the user picks becomes its own concept (`C1`, `C2`…) with its own transfer map and node; more takes of one concept are `count`, not new nodes (base rule).

**Example (short, fictional app Calmly, reference R1 = the fasting chat static in Reference L).**
> Reference: a pink vector static, a chat where the user asks "Why does nothing work for me?" and the app answers warmly, then a plan headline, a personal stats row and a green plan button. It works because the self-blame question is the viewer's own thought, and the answer removes the blame.
> Brand Kit: Calmly, the only kit in this workspace. Make it for Calmly, right?
> A. Close remake: the same chat layout, but it's Calmly: "Why can't I switch off at night?" answered by "Because your brain never gets a wind-down.", then "here's your 5-MINUTE WIND-DOWN", a row with the real texts of your timer screen, a violet button "START TONIGHT". Navy, violet and cream, our own small moon illustration instead of their raccoon.
> B. Free adaptation: the same question and warm answer as two stylised bubbles over a phone-real photo of Mia, 21, awake in bed at 2 am; CTA "Try it tonight".
> Variations: V1 both as an A/B (recommended: proven layout plus a native photo version) · V2 the remake for the kit's second segment, night-shift nurses ("Why can't I sleep after a shift?") · V3 the adaptation as a 3-card carousel (question → the timer screen → CTA).
> Open: the timer screenshot (for the row and V3), and 4:5 Feed or 9:16 Stories?

---

## Step 2 addition: transfer map, new texts, new prompt

### The transfer map

Before writing a line, map each part of the reference to the user's app, for the mode and variation picked. The "Ours" column comes **only** from the Brand Kit sheet and the user's words. One row per zone and per element: **reference → ours · keep / translate / drop · why**. It goes into the "Transfer map" text node.

| Element | Reference | Ours (from the Brand Kit) | Kit source | Action |
|---|---|---|---|---|
| Bet | dieters who failed will try because a warm answer removes self-blame | students who can't switch off will try because a warm answer says it's not their fault | audience, pains (segment 1) | translate |
| Zone 1 (0 → 22%): chat | "Why does nothing work for me?" / "Because you never gave your body a break." | "Why can't I switch off at night?" / "Because your brain never gets a wind-down." | pains, customer words; tone | translate (same job: self-blame question, warm reframe) |
| Zone 2 (22 → 55%): mascot | raccoon with a tea cup | small original illustration: a crescent moon asleep on a pillow, in Calmly's palette | none needed (original element in kit palette) | translate (their mascot never kept) |
| Zone 3 (55 → 70%): headline | "here's your FASTING START" | "here's your 5-MINUTE WIND-DOWN" | feature: wind-down timer; screenshot 2 | translate (shape kept: lowercase lead + caps plan name) |
| Zone 4 (70 → 80%): stats row | Height, Weight, Goal (personalised numbers) | "Tonight's plan · 5 min · Lights off" (the real texts of the timer screenshot) | screenshot 2 (timer screen) | translate (no personal numbers: Calmly doesn't ask for them) |
| Zone 5 (80 → 86%): tagline | "Same foods. Different timing. Different results." | "Same bed. Same night. Five calm minutes." | tone of voice | translate (rhythm kept, no claim) |
| Zone 6 (86 → 100%): CTA | green button "CALCULATE YOUR PLAN" | violet #8B7CF6 button "START TONIGHT" | offer and CTA; colors | translate |
| Claim | fasting results | none approved → no result claim | approved claims: none | drop |
| Palette | #F5D7D1 pink, #2ECC71 green, #1A1A1A | #1B1F3B navy, #8B7CF6 violet, #F4F1EA cream | colors | translate |
| Style | flat vector, pastel, warm | flat vector, the same polish level, Calmly's palette, rounded type | positioning (mass, calm) | keep level, change look |

**Rules for the map:**
- Every zone of the reference has a row. A zone we drop is written as dropped, with the reason.
- Every "Ours" cell names its **kit source** (a Brand Kit field, an uploaded asset, or "user, in chat"). A cell without a source is either confirmed with the user or left out.
- Their pain becomes the **closest real pain** in the user's pain map, in the audience's words. None is close → the mechanism doesn't transfer: say so, offer mode B or another reference.
- Their feature becomes **one real feature** of the user's app. Never borrow a feature the app doesn't have.
- **Personalisation, data rows, results, ratings:** only what the app really does and really shows. A stats row is kept only if the app really builds something from those inputs, filled with an example that is clearly an example or with the texts of a real screenshot; never a number that reads as a claim.
- Their claims are dropped by default; a claim comes back only if the Brand Kit has its own approved one.
- Their person becomes a persona from the user's audience (base Reference E, `lyra-ugc-video` casting), different in look from theirs. Their mascot becomes the kit's own mascot, an original spot illustration, a persona or an object.
- Their palette and look become the brand's palette at the same polish level.

### The new texts

Written by Claude, from the transfer map, into the "Transfer map" note under the map:
- **Word budget per block.** Remake: each block within about ±20% of the reference's word count, the same number of blocks. Adaptation: the base skill's budget (headline 2 to 8 words, subline ≤ 10, CTA 1 to 4, up to 3 blocks), unless the format needs rows (chat, list, stats).
- **Same job, new words.** Each block keeps its job and may keep its shape; the words come from the Brand Kit and customer words. Run the rewrite test on every block.
- **The headline is the hook.** Write it with the line checks of `lyra-video-hooks` (one idea, simple, specific to this app and moment, true). The picture and the headline say one idea together (base Concept and layout).
- **Another language:** the texts written in that language by Claude, not translated word for word; check length against the zone (translations run longer).
- **Side by side**, part of the concept the user approves:

| Zone | Reference (what it does) | Ours (what it shows and says) | Words ref / ours | Kept | Changed |
|---|---|---|---|---|---|

### The concept card

As in the base skill (Concept and layout), one per concept, written from the transfer map: hypothesis in one line · visual · **layout map top to bottom with each zone's share and every text in quotes** · style · palette · text total. Plus: mode (A or B), reference code (R1), Brand Kit used. The concept the user approves has: the Brand Kit, the mode and variation, the transfer map in short, the side by side, the concept card, the plan table and the model question (base Step 2).

### Writing the new prompt

The prompt is built **from our layout map, never from their image**. The model never sees the competitor's static.

**Field → prompt part:**

| From the teardown | Goes into the prompt as |
|---|---|
| `composition` + layer 2 layout map | "Layout from top to bottom:" each zone with its share of the frame, what is in it and its exact new text in quotes |
| `visual_production` | the style line: phone-real or camera-real photo (base Realism), or the illustration style described fully (line, fill, texture, palette, proportions), or the collage, infographic or type-only look |
| `visual_subject` | the hero: our persona (character card), our product shot, our real screen, our stylised chat, our result card |
| `hook_type`, `hook_text` | the headline's job and shape, with our text in quotes |
| `copy_structure`, `text_to_visual_ratio` | the number of text blocks, their hierarchy, the share of the frame for text |
| `cta_type`, `cta_source` | the CTA button: position, shape, color (brand hex), our text in quotes |
| `color_palette` | replaced by the Brand Kit hex codes |
| `has_human_face` | a persona with a face or no face, as in the reference (remake), or by choice (adaptation) |
| `format: carousel` | one node per card, shared anchors word for word |

**Prompt order** (base Prompt rules, static ad): format and ratio in words → each connected input's job ("[Image1] is the app logo", "[Image2] is the app screen") → the scene or the illustrated world → **the layout from top to bottom**, zone by zone, with shares and every text in quotes, type style, color, size feel → the screen "exactly as supplied" + its key texts, if any → palette (hex) → style line → "The only text in the image is …" → a short "Avoid …" line. 100 to 220 words; non-negotiables early.

**Never in a copy prompt:** "like the reference", "in the style of [competitor]", their app name, their mascot's description, their slogan, their exact lines, their hex codes, their typeface name.

**Pattern: close remake, vector chat layout (Nano Banana Pro, 4:5).**

> Static app ad, vertical 4:5, flat vector illustration style with soft shapes and gentle grain. [Image1] is the app screen: its texts are used only as labels below. Background: cream #F4F1EA. Layout from top to bottom: top 22%: two stylised rounded chat bubbles, generic, not any real messenger: on the right a grey bubble with dark text "Why can't I switch off at night?", on the left a navy #1B1F3B bubble with white text "Because your brain never gets a wind-down." · 22 to 55%: centered, a small original illustration of a crescent moon asleep on a soft pillow, navy and violet, rounded shapes, no face details beyond closed eyes · 55 to 70%: headline in two lines, centered: "here's your" in a light rounded sans, then "5-MINUTE WIND-DOWN" in a heavy rounded sans, navy, very large · 70 to 80%: one row of three small rounded pills with dark text: "Tonight's plan", "5 min", "Lights off" · 80 to 86%: small centered line "Same bed. Same night. Five calm minutes." · bottom 14%: a wide rounded button in violet #8B7CF6 with white bold text "START TONIGHT". Generous margins, about 5% on every side. The only text in the image is the two bubbles, the headline, the three pills, the small line and the button. Avoid: extra text, logos, real messenger UI, gradients, clutter.

**Pattern: free adaptation, phone-real photo (Nano Banana Pro, 4:5).**

> Static app ad, vertical 4:5, UGC phone-photo style. Mia, 21, light brown skin, freckles, dark curly hair in a loose bun, oversized grey hoodie, lies awake on her side in a dark bedroom at 2 am, phone light on her tired face, looking past the camera. Shot on a 24mm phone camera, deep focus, warm bedside lamp from the right, natural skin texture, visible pores, slight dark circles, rumpled grey duvet, a charger cable on the nightstand. Layout from top to bottom: top 25%, over the dark wall: two stylised rounded chat bubbles, generic, not any real messenger: right, a white bubble "Why can't I switch off at night?"; left, a violet #8B7CF6 bubble with white text "Because your brain never gets a wind-down." · middle: Mia · bottom 15%: a rounded button "Try it tonight" in violet #8B7CF6 with white text, centered. The only text in the image is the two bubbles and the button. Avoid: beauty filter, studio lighting, extra text, logos, real app interfaces.

### Optional: a layout wireframe for a close remake

When a remake's layout keeps drifting (zones in the wrong place, wrong proportions), give the model the layout as an image without any of the competitor's identity: Claude draws a **neutral wireframe** in its environment (grey boxes for the zones at the measured shares, a white background, labels like "HEADLINE", "CHAT", "BUTTON", no colors, no text from the reference, no shapes from their image), uploads it (`create_upload` + `attach_upload`) and connects it with its job stated first: "[Image3] is a layout wireframe only: place the zones where its grey boxes are; do not copy its grey color, its labels or any text from it." Check the result for label leaks ("HEADLINE" printed in the image) and drop the wireframe if it leaks.

---

## Best way to build it

The format of the reference decides the build. The user's explicit choices override any row. Models and prices: base Reference A.

| If the reference is | Graph | Models |
|---|---|---|
| **Single static (default)** | Brand Kit assigned → uploads the static needs (logo, icon, screenshots) → one Image Generation node per concept (remake, adaptation), the reference's ratio, 2K (4K for small text, UI or a close face), count 2 → the user checks every letter | nano-banana-pro |
| A person in the pain moment (`person_*`) | persona node first when the person appears in several statics (count 2, the user picks), connected as reference; otherwise the person described in the ad prompt | nano-banana-pro |
| The app's UI (`app_screen_demo`, `screenshot_UI`) | our screenshots uploaded → the screen "exactly as supplied" in the prompt + key texts; a separate phone-shot node when the screen is the hero (base Reference G, `lyra-ui-motion-video`) | nano-banana-pro |
| A chat, a comment, a social post (`text_message_chat`, `social_post_embed`) | stylised generic bubbles or post frame, our texts in quotes; never a copy of iOS, WhatsApp, Instagram or system UI; a fictional chat never presented as real | nano-banana-pro |
| A review card, a rating, a user count (`review_quote_card`, social proof) | only a real review, rating or number from the Brand Kit, attributed; none → the slot becomes a demo or a result from a real screen | nano-banana-pro |
| A mascot (`character_mascot`) | the kit's own mascot uploaded as reference; no mascot → a persona, an object or an original spot illustration; never a lookalike of theirs | nano-banana-pro |
| Illustration or 3D (`illustration_*`, `AI_art_stylized`) | the same style family, described fully in words, in our palette; Flux 2 or Wan 2.7 Pro only as a second look to compare | nano-banana-pro |
| Type-only or text-heavy (`text_only`, `infographic_data`) | Pro first; a block that keeps failing → Ideogram 3.0 Quality test, or a clean zone for the designer | nano-banana-pro · ideogram-v3-quality |
| A meme format (`meme_template`) | only an original or free format (a lo-fi caption over our own scene); never a copyrighted meme image or a known meme character | nano-banana-pro |
| **Carousel** | one node per card, the shared anchors (palette, type, persona, background, frame) word for word in every prompt; persona or style reference shared; card 1 = hook, last card = CTA | nano-banana-pro |
| Several references | pattern sheet → one concept per picked direction (usually the shared mechanism in mode B, plus a mode A of the strongest) | nano-banana-pro |
| A key frame of a competitor video | the frame analysed (Step 1a) → our static built like a single static, headline and CTA added in clean zones | nano-banana-pro |
| Many directions, tight budget | drafts on nano-banana-2 at 1K, count 2 to 3 → the user picks → winners rerun on Pro (base row) | nano-banana-2 → nano-banana-pro |

**Plan example** (base Step 2 table, the Calmly example, both modes):

| # | Node label | Node · model · key settings | Inputs (role) | Stage |
|---|---|---|---|---|
| 1 | Ref R1: chat fasting static (analysis only) | upload image | — | — |
| 2 | Reference teardown | user text | — | — |
| 3 | Transfer map (Brand Kit sheet, texts, side by side) | user text | — | — |
| 4 | Concept cards C1 remake, C2 adapt | user text | — | — |
| 5 | Screenshot: timer | upload image | — | 1 |
| 6 | Ad C1: remake · chat wind-down · 4:5 | image · google/nano-banana-pro · 4:5 · 2K · count 2 | 5 (screen texts) | 2 |
| 7 | Ad C2: adapt · Mia 2 am chat · 4:5 | image · google/nano-banana-pro · 4:5 · 2K · count 2 | — | 2 |
| 8 | C1 · 9:16 + 1:1 (after approval) | image resize · google/nano-banana-2 | 6 | 3 |

Node 1 is connected to nothing; nodes 2 to 4 are notes for the user and feed nothing.

**The reference in the workflow.** The competitor's image is uploaded into Section "Reference" for the record and analysis (and for Path 1), labelled "Ref R1: chat fasting static (analysis only)", and **never connected to an image generation node**. A competitor image as a generation reference leaks their mascot, palette, type and text into ours; the layout comes from our layout map in words (and, if needed, from a neutral wireframe).

**Layout.** Section "Reference" (uploaded reference, Creative Analysis node if any, "Reference teardown", "Pattern sheet", "Transfer map" notes; nothing here feeds generation) → then the base layout: Sources (concept cards, uploads) → Persona / product → Ads → Sizes and languages. Labels: "Ad C1: remake · chat wind-down · 4:5", "Ad C2: adapt · Mia 2 am chat · 4:5", "Card 2: timer screen · 4:5".

## Run options (copy)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option. The analysis comes first and on its own: **Path 2** costs no credits · **Path 1** costs what the Creative Analysis node shows next to Run (say it before running). Then: **A. Finals first (recommended):** every concept on Nano Banana Pro, count 2 · **B. Drafts first:** Nano Banana 2, 1K, count 2 to 3, winners rerun on Pro · **C. Everything:** ads → sizes → languages (count 1, no pause to pick). Remake and adaptation together: the same options, both concepts.

---

## After the copy: variants

The user asked for variants right away, so when the first results are approved, offer 2 to 4 next steps in one message, each with what it changes, what stays, which skill builds it and its credits. Change **one variable per variant** and list what is held constant (Lyra's Ad Variation rule), so each variant is a clean test:

| Variant | What changes | How it's built |
|---|---|---|
| **Headline** | the headline (another angle on the same pain: question → statement → a stat from the kit) | an edit node on the approved static: "Change only the headline to '…'; keep everything else exactly"; or a new node with the same prompt and only the headline replaced |
| **Persona or world** | the person, their wardrobe, the room, a prop, the time of day, for another segment from the kit | the edit patterns of the base skill (Reference F: person swap, world swap), the layers and the one-story test of `lyra-audience-variations` |
| **Subject or production level** | mascot ↔ persona ↔ real screen; vector ↔ phone-real photo | a new node (a new concept), same layout map |
| **Remake ↔ adaptation** | the other mode on the same teardown | a new node |
| **Sizes** | 9:16, 1:1, 4:5 | `lyra-image-resize`: Image Resize for simple layouts, a Pro recompose node when text or the hero must move (recompose, don't crop) |
| **Languages** | the texts in another language | `lyra-image-translation`: Image Translation for statics without UI; with UI → the localized app's screenshots + texts written in that language, a new Pro node |
| **New angle** | the argument of the ad, same concept | `lyra-ad-concept-multiplier` |
| **Animated version** | the static becomes the first frame of a short video | `lyra-ui-motion-video` (UI-led) or `lyra-video-ad-generation` |

Variants of an approved static live in the same workflow (one node per variant, next to the original, labelled with its code) or, for a whole new version of the canvas, in a Lyra variation (`create_variation` copied from the original; the original stays Main as the control). Never overwrite the approved static.

---

## Prompt rules (copy static)

| Node | Write | Avoid |
|---|---|---|
| Reference teardown (text) | layer 1: one JSON object by Reference L (per card for a carousel); layer 2: the production breakdown with the measured layout map; facts only, gaps marked "not readable" / "not visible" | guesses; enum values not in the schema; paraphrased claims; long praise of the ad |
| Pattern sheet (text) | shared fields across references, what varies, which runs longest, the mechanism in one line | elements stitched from several competitors |
| Transfer map (text) | Brand Kit sheet; one row per zone and element: reference → ours → keep / translate / drop → why; the new texts with word counts; the side by side | their lines copied in as "ours"; their claims, numbers or offer |
| Concept card (text) | as the base skill, plus mode, reference code and Brand Kit | prompts meant for the model |
| Static ad (image) | the base static ad prompt, with the layout from our map, zone shares and every text in quotes; inputs with stated jobs; "The only text in the image is …" | "like the reference"; their name, mascot, lines, palette, typeface; a competitor image connected; generated logos, badges, UI |
| Carousel card (image) | the shared anchors word for word → this card's role and zones → its text | a different palette, type or persona per card |
| Edit for a variant (image) | verb first, keep list, one change (base Reference F) | two changes at once; re-describing the whole static |
| Layout wireframe (upload) | grey boxes at the measured shares, neutral labels, its job stated first in the prompt | any color, shape or text from the competitor's image |

Every prompt is self-contained (base rule): describe the static itself, never "like the reference".

---

## Truth, rights and brand safety

- The competitor's static is a reference for analysis. Their image, illustration, photo, mascot, text and logo are never part of our ad, and never a generation reference.
- No competitor name, logo or product in our ad, and no comparison with them by name. A comparative ad that names a competitor is a legal question for the user's team, not a default; this is not legal advice.
- Their claims, numbers, ratings, reviews, user counts and awards are theirs. Ours come only from the Brand Kit or the user. Review cards and ratings only real and attributed; personalised data only as the app really produces it.
- No lookalike of their person, no copy of their mascot or characters, no copyrighted meme images or known meme characters, no copies of iOS, WhatsApp, Instagram or system UI (stylised bubbles and cards only).
- Formats and layouts are free to use; a specific illustration, photo or trade dress isn't. When in doubt, move further from the reference (mode B).
- AI people are creative scenes, never real customers (base Truth and disclosure); remind the user once, in the final report, about the platform's AI label for photoreal synthetic people.
- **Brand safety** (Lyra's System Preamble): no profanity, no political statements, no unsubstantiated health claims, no digs at the competitor even without its name. The Brand Kit's **forbidden claims are enforced absolutely**, in every headline, bubble, row, card and CTA, even when the reference makes that claim; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated. No body before/after for health or weight-loss apps, even if the reference has one.

---

## Deliverable and naming

1. Section "Reference": the uploaded reference(s) (analysis only), "Reference teardown" (one per reference), "Pattern sheet" (several references), "Transfer map" with the Brand Kit sheet, the new texts and the side by side.
2. A "Concept card" per concept.
3. All planned uploads, persona or product shots, the new statics (remake and/or adaptation), carousel cards, and the variants the user picked.

Name every final with a code the media buyer can paste into Ads Manager: `B{batch}-A:{angle}-F:CopyStatic-{visual_subject}-{Remake|Adapt}-R{reference}-C{concept}-{ratio}`, e.g. `B5-A:CantSwitchOff-F:CopyStatic-Chat-Remake-R1-C1-4x5`. Carousels add `-Card{n}`; variants `-V{n}{what changed}` (`-V2Headline`, `-V3Persona`); other languages `-{lang}`. Several references: `R1+R2` when the concept comes from the pattern. The competitor's name stays out of the code; `R1` points to the teardown note.

---

## Common mistakes (copy static)

| Mistake | Prevention |
|---|---|
| Prompt written before the reference is understood | Teardown first, then the Brand Kit, then the questions, then the map, then the prompt |
| Brand Kit skipped "because it's a close remake" | Step 1b in both modes; every name, pain, feature, claim, offer and color from the kit |
| Several kits, one picked silently or two mixed | Ask which kit; one kit per ad |
| Gaps in the kit filled from the competitor's static | Pain hypotheses, no screen, no claim, no review card |
| Modes asked as an abstract choice | Both modes and 2 to 3 variations told with the kit's real name, audience, pain and offer |
| Layout described by impression ("text at the top") | Measured zone shares in the layout map, copied into the prompt |
| Small text guessed | Crop and enlarge, or ask for a sharper original; "not readable" |
| Enums invented, claims paraphrased, ad copy overriding the image | Reference L exactly; the image first; ad copy only for gaps |
| A carousel analysed as one image | One JSON per card + the card list |
| Elements stitched from several competitors | Pattern sheet; the shared mechanism executed once in our look |
| The competitor's image connected to the generation node | Analysis only; layout in words, a neutral wireframe if needed |
| "Like the reference" or their name in a prompt | Self-contained prompt from our layout map |
| Their headline lightly reworded | Same job, new words; rewrite test on every block |
| Their mascot redrawn, their palette and typeface kept | Our mascot, persona or object; brand palette; look test at thumbnail size |
| Their stats row, rating or review reused with our name | Real data from the kit only; otherwise the slot becomes a real screen or a result |
| Fake chat presented as a real conversation, iOS or WhatsApp look copied | Stylised generic bubbles; fictional, never claimed as real |
| Copyrighted meme image or known meme character | Original format only |
| Static from a video with no headline or CTA | Add the hook line as on-image text and the kit's CTA in clean zones |
| Remake drifts (zones moved, three extra lines) | Zone shares ±5%, block count and word counts kept; wireframe if it keeps drifting |
| Adaptation loses the hook mechanism | Keep the bet, the hook mechanism and the reading order |
| Text not checked letter by letter | Base rule: every word with the user; a failing block → clean zone for the designer |
| Variants changing several things at once | One variable per variant, held-constant list |
| Competitor's name in the node label or the final's code | Teardown note only; `R{n}` in the code |
| Page link from Ad Library retried as a file | Ask for the image or a screenshot |

## Quality gates (copy static)

- **Stage 0 (teardown, Brand Kit, map, texts, prompt; Claude checks before sending):** the Brand Kit chosen and confirmed? Its sheet filled, gaps marked? Mode, variation and CTA picked by the user, told in the kit's terms? Layer 1 a valid JSON object by Reference L (exact names and enums, all required fields, `visual_summary` first, claims in the claim format, per card for carousels)? Layer 2 filled, the layout map measured? The bet in one line? Every zone mapped (keep, translate, drop), every "Ours" cell with its kit source? Pain and feature real for our app? Their claims dropped? Every block passes the rewrite test? Word counts fit (remake ±20%, adaptation the base budget)? Don't copy list written? The prompt self-contained, built from our map, no competitor image connected?
- **Stage 1 (sources: persona, product, phone shot):** the base Stage 1 checks; our persona clearly not their person; the screen identical to our screenshot word by word.
- **Stage 2 (the statics), side by side with the reference at phone size:** the same mechanism lands in half a second (remake: the same reading order and zones; adaptation: the same bet)? Every letter and number identical to the transfer map, nothing extra? Our palette, our subject, our type; nothing that still says "competitor" (a phrase, a mascot, a color, an illustration style)? Clear in one look what **our** app does? CTA from the kit? Trace check: every word, number, color and asset traced to the kit or the user, nothing from the forbidden list? Ratio and safe zones right? Plus the base Stage 2 checks (light, hands, logo, realism or style).
- **Stage 3 (variants, sizes, languages):** only the intended variable changed? Nothing cropped, headline and CTA in the safe zones, texts re-checked in every language, named with codes? AI label reminder given?

## After the test

A static that wins for a competitor is a hypothesis for us, not a promise: judge ours by our own KPIs (cost per result for the goal: trial, payer; CTR alone proves nothing; enough conversions before calling a winner). Say what won: the mechanism (the copy works → more on this bet: headline variants, personas, sizes, languages, an animated version) or not (the mechanism doesn't transfer to our audience → note it, try the other mode or another reference). Statics fatigue fast at scale (often 7 to 14 days): plan the next round. Save the teardown, the transfer map and the result to the project's creative repository, so the next copy starts from what the team already learned.

---

## Reference L. Static ad creative analysis standard (layer 1)

The team's standard for classifying a static ad (the same as Lyra's "Ad creative analysis (image)" system prompt). Claude follows it word for word for layer 1 of every static teardown, and checks the Creative Analysis node's output against it.

**Role and objective.** A performance marketing creative analyst for STATIC ads: extract structured classification data from the IMAGE (primary source of truth) and ad copy text fields (secondary support only). Operational priority: return exactly one valid JSON object, follow the schema exactly, and keep outputs strictly limited to evidence supported by the provided creative inputs and the classification rules below.

**Inputs.** One image plus optional ad copy text fields: title, caption, body, description.

**Core requirements.** Respond only with valid JSON · no preamble, markdown backticks or explanation · exactly one JSON object that conforms to the schema · no text before or after the JSON object · match the schema literally: exact property names, exact enum values, no additional properties · `visual_summary` always the first field in the output object.

**Critical priority rule.** The IMAGE is the source of truth · use title, caption, body ONLY to fill gaps not visible in the image · if information is visible on the image, do NOT override it with title, caption or body.

**Visual analysis: what to examine.** Before classifying any field, examine the image carefully: visible headline or hook text on the image · layout and spatial composition · main objects, subjects or characters · presence of UI elements, lists, panels, charts or graphics · presence of CTA buttons or action prompts · amount of on-image text vs imagery.

**Rules for `visual_summary`.** Describe what is shown and how the message is visualized: a concrete visual-mechanical description, not a generic marketing summary. Name specific visual elements and their arrangement ("coins lined up with prices next to each", "ranking list layout", "phone UI screenshot", "big headline + small subtext", "CTA button on bottom") · if there is a demonstrated action or implied interaction, name it ("scan", "tap", "compare", "before/after") · transcribe any key on-image text exactly · avoid generic phrasing like "encourages users to…" unless combined with the concrete visual mechanic.

**Rules for `key_claims`.** For each claim: (1) quote or closely reference the **exact language, phrase or visual element** present in the creative, never paraphrase, never invent; (2) explain the **rhetorical mechanism**: how this specific language or visual choice communicates value or overcomes resistance. Format: `"[exact element from creative] — [explanation of why this works / what it communicates]"`. If a visual element (not text) is doing the persuasion work, describe what is shown and why it functions as a claim. Never include claims not present in the image.

### Taxonomy

**`hook_type`** (the primary persuasion mechanic of the opening): `problem_solution` opens by naming a pain point, then frames product as the fix · `before_after` shows or implies a state change, improvement or transformation · `social_proof` leads with others' behavior, ratings or adoption as the hook · `UGC_testimonial` first-person user voice or real person sharing their experience · `curiosity_gap` withholds information to create a knowledge gap that demands resolution · `fear_urgency` triggers anxiety, loss aversion or threat of missing out · `question` opens with a direct question aimed at the target audience · `statistic_claim` leads with a specific number, percentage or data point · `POV_first_person` places viewer in the scenario using "you" or first-person perspective · `tutorial_how_to` opens with a promise to show how to do something · `unboxing_reveal` sequential discovery or unwrapping as the hook mechanic · `comparison_vs` directly contrasts two options, brands or states · `transformation` focuses on the journey or change process, not just the endpoint · `day_in_life` follows a character through a scenario to create identification · `GRWM_get_ready` get-ready-with-me structure, product integrated into a routine · `reaction` someone's visible emotional reaction to a product or situation · `myth_busting` opens by challenging a common belief or assumption · `listicle` numbered or bulleted list format as the primary structure · `controversy_hot_take` provocative or polarizing opening designed to stop the scroll · `authority_expert` credentials, expertise or professional context as the opening signal · `emotional_story` narrative with emotional arc as the primary hook · `product_demo` product shown in use or in action as the immediate hook · `challenge` invites viewer to participate in or attempt something.

**`hook_source`** (where the hook text was found): `on_screen_text` text visible directly on the image · `visual_description` hook is conveyed through the visual itself, no text · `title` from the ad title/headline metadata field · `caption` from the ad caption metadata field · `body` from the ad body copy metadata field · `description` from the ad description metadata field · `inferred` hook inferred from overall creative intent, no explicit source.

**`offer_framing`** (how the economic proposition is framed): `price_anchor` shows a high reference price to make the actual price feel cheap · `free_trial` leads with a no-cost trial period · `percentage_discount` discount expressed as a percentage off · `dollar_discount` discount expressed as a specific dollar/currency amount · `BOGO` buy one get one or similar quantity deal · `limited_time_urgency` offer is available only for a restricted time window · `scarcity` limited quantity or availability drives action · `value_stack` lists multiple inclusions to make total value feel large · `money_back_guarantee` reduces risk by promising a refund · `free_shipping` removes delivery cost as a conversion barrier · `bundle_deal` multiple products packaged together at a combined price · `subscription_savings` frames recurring billing as cheaper than alternative · `no_offer_brand_only` no economic proposition present, pure brand or product message · `comparison_pricing` shows competitor price alongside own price · `pay_what_you_want` user controls the price within a range.

**`cta_type`** (the call to action type): `learn_more` directs to more information, low commitment · `shop_now` direct purchase intent · `try_free` free trial or no-cost start · `get_started` onboarding or activation, often for apps or SaaS · `download` app or file download · `sign_up` account creation or registration · `subscribe` ongoing subscription commitment · `buy_now` immediate purchase, higher urgency than shop_now · `book_now` appointment or reservation · `get_offer` claim a specific deal or promotion · `claim_deal` similar to get_offer, deal-focused · `see_more` expand content or view additional items · `send_message` opens a chat or messaging flow · `watch_more` video content continuation · `swipe_up` story-format upward swipe action · `custom` any CTA text not covered by the above; extract exact text into `cta_custom_text`.

**`cta_source`** (where the CTA was found): `on_screen_text` CTA button or text visible on the image · `title` · `caption` · `body` · `description` (the ad copy metadata fields) · `inferred` no explicit CTA visible; inferred from landing intent.

**`visual_production`** (how the image was created, its source): `studio_photo` professional photography, controlled lighting, clean or neutral background · `lifestyle_photo` professional photo in a real-world context (home, street, gym, outdoors) · `UGC_raw` shot on a phone, unpolished, authentic feel, non-directed · `stock_photo` recognizable stock aesthetic, clearly not proprietary or brand-specific content · `AI_photo_realistic` AI-generated image that is photorealistic; may not be immediately obvious · `AI_art_stylized` AI-generated art that is visibly stylized and does not pretend to be a photo · `illustration_vector` flat or clean vector illustration style, digital · `illustration_hand` hand-drawn or painterly style, sketchy or expressive · `illustration_3d` 3D render of objects, characters or scenes · `screenshot_UI` actual screenshot of an app interface, website or digital product · `collage_mixed` combination of photo + graphics + text layered together in one frame · `infographic_data` data visualization, charts or tables as the primary visual element · `text_only` pure typography with no imagery at all · `meme_template` a recognizable internet meme format adapted for the ad.

**`visual_subject`** (the primary object or subject shown): `person_selfie` self-shot angle, close framing, camera below eye level · `person_talking_head` person faces camera, upper body visible, direct address to viewer · `person_lifestyle_action` person in context doing something relevant to the product · `person_transformation` human before/after change shown (weight, skin, appearance) · `product_hero_clean` product shown alone, isolated, nothing else in frame · `product_in_use` product being used by hands or shown in an environment · `product_transformation` result generated by the product shown (room redesign, photo edit, output) · `app_screen_demo` app UI shown as the primary content, not merely as a compositional element · `before_after_split` two states shown simultaneously side by side or top/bottom · `data_table_list` rows of data, attributes, scores or comparison table as hero element · `character_mascot` illustrated or animated character as the dominant visual element · `environment_scene` a place, room or setting with no person as the focus · `text_message_chat` simulated chat, DM, SMS or notification UI as the main visual · `social_post_embed` a fake or real social media post shown as a visual element · `review_quote_card` a testimonial or review as the visual centerpiece · `result_proof` outcome shown as the hero: score, stat, before/after metric, transformation result.

**`composition`** (spatial layout structure): `single_hero` one dominant element centered or prominently placed, everything else is secondary · `split_screen` two distinct panels dividing the frame (left/right or top/bottom) · `collage_grid` multiple images or elements arranged in a grid or mosaic · `editorial_layered` overlapping elements, magazine or poster style, asymmetric · `full_bleed_text` image fills the entire frame with text overlaid on top · `data_table_layout` structured rows and columns dominate the layout · `chat_ui_layout` layout mimics a messaging or chat interface with bubbles and replies.

**`format`**: `static_image` a single non-moving image · `carousel` multiple swipeable image cards.

**`emotional_tone`** (the dominant emotional register): `aspirational` projects an idealized future state the viewer wants to reach · `fear_based` triggers anxiety, threat or loss aversion · `humorous_playful` uses comedy, wit or lightheartedness · `educational_informative` calm, factual, teaches something without emotional pressure · `urgent_FOMO` creates pressure to act now or miss out · `calm_trust` measured, reassuring, builds confidence and credibility · `provocative_edgy` intentionally provocative, boundary-pushing or controversial · `empathetic_relatable` mirrors the viewer's feelings or situation without judgment · `luxurious_premium` signals exclusivity, quality and high status · `nostalgic` evokes warmth or longing for the past · `inspirational_motivational` motivates action through positivity and empowerment · `casual_conversational` friendly, low-pressure, feels like a message from a peer.

**`copy_structure`** (how the text on the image is structured): `headline_only` a single dominant text element, nothing else · `headline_plus_subtext` main headline supported by one or more lines of secondary text · `long_form_story` extended paragraph or narrative text block · `minimal_no_text` no text or only a logo/brand mark · `bullet_benefits` unordered list of features or benefits · `story_arc_narrative` text tells a mini story with a beginning, middle and resolution · `question_answer` question posed then answered within the same creative · `listicle_numbered` numbered list format as the primary copy structure · `social_proof_quote` a quote from a user, expert or third party as the primary copy · `data_driven_stats` statistics or data points as the primary copy element.

**`social_proof_type`** (type of social proof present, even as a secondary element): `none` no social proof of any kind present · `user_quote` a direct quote from a real or simulated user · `star_rating` numerical star rating or review score shown · `user_count` number of users, downloads, customers or reviews displayed · `award` third-party award, badge, certification or "App of the Year" type signal · `celebrity` a known public figure, influencer or verified creator featured.

**`text_to_visual_ratio`** (balance between text and imagery): `text_heavy` text dominates the frame; imagery is minimal or absent · `balanced` text and imagery occupy roughly equal visual weight · `visual_dominant` imagery dominates; text is minimal (logo, short CTA, or none) · `no_text` no text present anywhere in the image.

Plus: **`color_palette`** 2 to 3 dominant colors as hex codes, ordered most dominant to least · **`has_human_face`** true if a human face is visible anywhere in the image · **`key_claims`** 2 to 5 claims, each `"[exact element from creative] — [rhetorical mechanism explanation]"`, based only on what is visible in the image, never invented · **`hook_text`** exact text of the hook as it appears on the image, or the closest description if visual-only (used for pattern matching) · **`cta_custom_text`** required when `cta_type` is `custom`: the exact CTA text as it appears.

### Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Static Ad Creative Analysis",
  "type": "object",
  "properties": {
    "visual_summary": {
      "type": "string",
      "description": "Concrete visual-mechanical description of the creative. First field in output. Describe what is shown, how it is arranged, what text is visible on the image, and how the message is visualized. Transcribe key on-image text exactly."
    },
    "hook_type": {
      "type": "string",
      "enum": ["problem_solution","before_after","social_proof","UGC_testimonial","curiosity_gap","fear_urgency","question","statistic_claim","POV_first_person","tutorial_how_to","unboxing_reveal","comparison_vs","transformation","day_in_life","GRWM_get_ready","reaction","myth_busting","listicle","controversy_hot_take","authority_expert","emotional_story","product_demo","challenge"]
    },
    "hook_text": {
      "type": "string",
      "description": "Exact text of the hook as it appears on the image, or closest description if visual-only. Used for pattern matching."
    },
    "hook_source": {
      "type": "string",
      "enum": ["on_screen_text","visual_description","title","caption","body","description","inferred"]
    },
    "offer_framing": {
      "type": "string",
      "enum": ["price_anchor","free_trial","percentage_discount","dollar_discount","BOGO","limited_time_urgency","scarcity","value_stack","money_back_guarantee","free_shipping","bundle_deal","subscription_savings","no_offer_brand_only","comparison_pricing","pay_what_you_want"]
    },
    "cta_type": {
      "type": "string",
      "enum": ["learn_more","shop_now","try_free","get_started","download","sign_up","subscribe","buy_now","book_now","get_offer","claim_deal","see_more","send_message","watch_more","swipe_up","custom"]
    },
    "cta_custom_text": {
      "type": "string",
      "description": "Required when cta_type is 'custom'. Exact CTA text as it appears."
    },
    "cta_source": {
      "type": "string",
      "enum": ["on_screen_text","title","caption","body","description","inferred"]
    },
    "visual_production": {
      "type": "string",
      "enum": ["studio_photo","lifestyle_photo","UGC_raw","stock_photo","AI_photo_realistic","AI_art_stylized","illustration_vector","illustration_hand","illustration_3d","screenshot_UI","collage_mixed","infographic_data","text_only","meme_template"]
    },
    "visual_subject": {
      "type": "string",
      "enum": ["person_selfie","person_talking_head","person_lifestyle_action","person_transformation","product_hero_clean","product_in_use","product_transformation","app_screen_demo","before_after_split","data_table_list","character_mascot","environment_scene","text_message_chat","social_post_embed","review_quote_card","result_proof"]
    },
    "composition": {
      "type": "string",
      "enum": ["single_hero","split_screen","collage_grid","editorial_layered","full_bleed_text","data_table_layout","chat_ui_layout"]
    },
    "format": {
      "type": "string",
      "enum": ["static_image","carousel"]
    },
    "emotional_tone": {
      "type": "string",
      "enum": ["aspirational","fear_based","humorous_playful","educational_informative","urgent_FOMO","calm_trust","provocative_edgy","empathetic_relatable","luxurious_premium","nostalgic","inspirational_motivational","casual_conversational"]
    },
    "copy_structure": {
      "type": "string",
      "enum": ["headline_only","headline_plus_subtext","long_form_story","minimal_no_text","bullet_benefits","story_arc_narrative","question_answer","listicle_numbered","social_proof_quote","data_driven_stats"]
    },
    "key_claims": {
      "type": "array",
      "description": "2–5 claims. Each item: '[exact element from creative] — [rhetorical mechanism explanation]'. Base only on what is visible in the image. Never invent.",
      "items": { "type": "string" },
      "minItems": 2,
      "maxItems": 5
    },
    "social_proof_type": {
      "type": "string",
      "enum": ["none","user_quote","star_rating","user_count","award","celebrity"]
    },
    "color_palette": {
      "type": "array",
      "description": "2–3 dominant colors as hex codes, ordered most dominant to least.",
      "items": { "type": "string", "pattern": "^#[0-9A-Fa-f]{6}$" },
      "minItems": 2,
      "maxItems": 3
    },
    "has_human_face": {
      "type": "boolean",
      "description": "True if a human face is visible anywhere in the image."
    },
    "text_to_visual_ratio": {
      "type": "string",
      "enum": ["text_heavy","balanced","visual_dominant","no_text"]
    }
  },
  "required": ["visual_summary","hook_type","hook_text","hook_source","offer_framing","cta_type","cta_source","visual_production","visual_subject","composition","format","emotional_tone","copy_structure","key_claims","social_proof_type","has_human_face","text_to_visual_ratio"],
  "if": {
    "properties": { "cta_type": { "const": "custom" } },
    "required": ["cta_type"]
  },
  "then": {
    "required": ["cta_custom_text"]
  },
  "additionalProperties": false
}
```

### Example output

```json
{
  "visual_summary": "Pink background with a centered illustrated raccoon mascot holding a tea cup. Top section shows a simulated chat exchange — user message 'Why does nothing work for me?' answered by app bubble 'Because you never gave your body a break.' Below that: bold headline 'here's your FASTING START', a user stats row showing Height 5'6'', Weight 205 lbs, Goal 175 lbs, then the tagline 'Same foods. Different timing. Different results.' in small text. Bottom: bright green CTA button 'CALCULATE YOUR PLAN'. Dense but warm — pastel color keeps the hard weight-loss data from feeling clinical.",
  "hook_type": "question",
  "hook_text": "Why does nothing work for me?",
  "hook_source": "on_screen_text",
  "offer_framing": "no_offer_brand_only",
  "cta_type": "custom",
  "cta_custom_text": "CALCULATE YOUR PLAN",
  "cta_source": "on_screen_text",
  "visual_production": "illustration_vector",
  "visual_subject": "text_message_chat",
  "composition": "chat_ui_layout",
  "format": "static_image",
  "emotional_tone": "empathetic_relatable",
  "copy_structure": "headline_plus_subtext",
  "key_claims": [
    "'Why does nothing work for me?' as the opening — borrows the user's own internal monologue as hook. Self-blame framing creates instant recognition before the ad reframes it.",
    "'Because you never gave your body a break' — the app answers the user's question in a warm, non-judgmental tone. Positions the product as a coach that explains failure, not judges it.",
    "'Same foods. Different timing. Different results.' — classic blame reframe: your choices weren't wrong, your system was. Removes willpower from the equation, lowers resistance to trying again.",
    "Height / Weight / Goal stats row — fake personalization showing specific user data signals 'this plan is built for you specifically', even in a static ad with no real input."
  ],
  "social_proof_type": "none",
  "color_palette": ["#F5D7D1", "#2ECC71", "#1A1A1A"],
  "has_human_face": false,
  "text_to_visual_ratio": "balanced"
}
```

**How the copy of this ad goes** (worked through in Step 1c and Step 2): the chat mechanism (the user's self-blame question, the app's warm answer), the plan headline, the row and the plan button stay as a structure; the raccoon, the pink and green palette, every line and the fasting claim don't. The stats row is the one element that is "fake personalization" in their ad: ours keeps the slot only with the texts of a real screen (or a real personalised output, if the app has one), never invented personal numbers.
