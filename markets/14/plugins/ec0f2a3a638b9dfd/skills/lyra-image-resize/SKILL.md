---
name: lyra-image-resize
description: "Use when the user wants an approved ad image in other sizes or placements, e.g. \"make this in 9:16 and 1:1\", \"resize for Stories / Reels\", \"all sizes for Meta\", \"a 1.91:1 version\", \"Google App campaign sizes\", \"a 728x90 banner\". Recomposes the layout for each frame in Lyra and keeps every element, text and color."
---

# lyra-image-resize

Image helper skill. Takes an image that is already approved (a static ad, carousel cards, an end card, a phone shot) and makes it fit another frame: the same ad, the same elements, the same words, the same look, **recomposed** for the new ratio and the placement's safe zones. One output per ratio, labelled and named so the media buyer can upload them as one ad with an asset per placement.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**Resize is recomposition, not cropping.** A crop throws away part of the ad; a stretch distorts it; a centered copy on a bigger canvas wastes the frame. A good resize decides again where each element lives in the new frame, so the hero stays the hero, the headline stays readable and the CTA stays clear of the platform's buttons. So the layout for every ratio is planned **before** any credits are spent, in a Resize sheet, and only then rendered.

**Adaptation, not improvement.** The goal is the same image in a new frame, not a better one. Nothing is added, nothing is dropped, nothing is "fixed": no new text, no sharper skin, no higher contrast, no cleaner UI. That is the Image Resize node's own rule (below), and this skill holds every route to it.

**Base skill first.** Everything not written here follows `lyra-static-image-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, concept card and layout map, on-image text rules, realism, models (Reference A), layout library (B), edits and recompose (F), UI and logo (G), sizes and languages (H), errors (I), de-slop (J), Meta statics (K), Brand Kit (L). This file adds what is specific to ratios and placements. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.**
- Other **languages** → `lyra-image-translation`. Order: **languages first, sizes second** (each approved language is resized; fewer runs, and a text that grew in translation is placed once per ratio).
- An image with **app UI** → UI fidelity from `lyra-ui-motion-video`: the screen in every ratio is the user's screenshot, identical word for word. App Store / Google Play **screenshot sets** have exact pixel sizes and their own rules: `lyra-ui-motion-video` (Store screenshot sets).
- **Carousels** → `lyra-carousel` (Story Bible, layout grid); this file says how a set of cards is resized together.
- The same ad for **another audience or market** → `lyra-audience-variations`; this skill changes only the frame.
- **Video sizes** (a 9:16 video for Feed 4:5 or 1:1) → the video skills: the keyframes are recomposed here, the clips are regenerated there (`lyra-video-ad-generation`, `lyra-ui-motion-video`); this skill covers only the images (keyframes, end cards, text cards).
- **Variants** of a copied competitor static → `lyra-copy-competitor-static` (After the copy), sizes built here.

**This is a way of thinking, not a script.** The rules are defaults and good practice; use judgment and say why in one line when you choose differently. Fixed: every element of the source kept, texts identical letter by letter, style and colors kept, no improvement, UI fidelity (the user's screenshots, exactly), the logo exactly as uploaded, truth (resize never adds a claim, a number or a badge), Lyra's technical limits (the ratios the model lists), and the user's explicit choices.

---

## How to think about a resize

**What changes and what never does:**

| Changes | Never changes |
|---|---|
| the canvas (ratio, size) | the elements: product, person, phone and screen, headline, subline, CTA, logo, offer badge, background |
| where each element sits, its scale relative to the frame | the words: every text identical, letter for letter (line breaks may move, words may not) |
| how much background is visible (extended, never invented as a new place) | the style: palette, light, color grading, shadows, photo treatment, illustration style |
| the reading order **only** when the new shape forces it (side by side → top to bottom) | the type: font weight, color, style, case |
| the line breaks of a text block | the visual hierarchy: the primary element stays the most prominent |
| | the identity of people, the product, the logo, the UI |

**Four kinds of moves** (decide which one each ratio is, it picks the route):

| Move | Examples | What happens | Risk |
|---|---|---|---|
| **Small step** | 4:5 ↔ 1:1 · 4:5 ↔ 3:4 · 1:1 ↔ 5:4 | the same layout, a little more or less room; gaps tighten or open, the background extends a little | low: a Resize node usually does it |
| **Add height** | 4:5 or 1:1 → 9:16 | the layout stays vertical, the canvas grows up and down; text moves into the new safe zones, the background extends above and below | medium: the 9:16 UI zones push text and CTA inward |
| **Orientation flip** | 9:16 or 4:5 ↔ 16:9 / 1.91:1 · 1:1 → 16:9 | the layout is rebuilt: stacked ↔ side by side, text moves from top / bottom to a side column, the hero moves to a third | high: the model may crop, shrink the text or drop an element |
| **Extreme strip** | → 4:1, 8:1 (banners), 1:4, 1:8 (skyscrapers) | only a row (or a column) of elements fits: hero + headline + CTA side by side | very high: not every element fits; a user decision (below) |

**Extension or recomposition.** Two ways to fill a new frame, often together:
- **Extension (outpainting):** the canvas grows and the new area continues the source background (the same wall, sky, duvet, gradient, texture, light). Best when the source has calm background at the edges.
- **Recomposition:** the elements move and rescale inside the new frame (the headline from the top band to a left column, the CTA under the headline). Needed whenever the new shape doesn't fit the old arrangement.

**Primary element first.** Before planning, name the one element that carries the ad (a face, the phone with the screen, the product, the big headline). In every ratio it stays the most prominent: it gets the space first, then the headline, then the CTA, then the rest.

**Final test for every ratio:** put the new image next to the source at phone size. Same ad at a glance? Every element there, every word identical, the same look? The hero still the first thing you see? Nothing under the platform's UI, nothing jammed against an edge?

---

## Lyra facts: the Image Resize node (Oct 2026)

From `list_node_configs` and the MCP tools; re-check at the start of every build.

- **Action** `image_resize` on the image node type; **preferred model `google/nano-banana-2`**. Nano Banana 2 parameters: resolution 1K / 2K / 4K (default 1K); aspect ratio `match_input_image`, `1:1`, `1:4`, `1:8`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9`.
- **Tool:** `create_image_resize_node` (workflow_uuid, `aspect_ratios`, `model_name`, label). Then `connect_nodes` source → resize node **without a role**. One output per ratio. It generates nothing until `run_node`.
- **Ratios Lyra does not list:** **1.91:1** (Meta link ads, Google App and Display landscape), 2:1, 6:5 (300×250 is 1.2), 9:19.5 (App Store 1290×2796), 6.4:1 (320×50), any exact pixel size. Build the nearest listed ratio with the crop margin planned in (Placements table) and let the user's designer trim it, or ask for the user's own ratio list. Never send an unlisted value to the node.
- **Extreme ratios** (`1:4`, `1:8`, `4:1`, `8:1`) exist only on Nano Banana 2, not on Nano Banana Pro: strips and skyscrapers go through the Resize node (Route A) or the designer (Route D).
- **Whether the resize node shows resolution and an instruction field** is checked after creating it (`get_workflow`). When it shows resolution, set **2K** (4K when the image carries small text or a screen to read). When it has a prompt field that `update_node` can fill, the instruction from the Resize sheet goes there (pattern below). Write in the project notes what the first build shows, so the next build skips the check. No field reachable → Route A runs on the node's own rules, and anything that needs exact placement goes through Route B.
- **The source must have a result.** If the image node made several, the user selects one in Lyra first; the resize uses the selected result. If the source is regenerated later, the resized images are stale: rerun them.
- **The node re-renders the whole image generatively.** It extends and recomposes; it does not crop pixels. So the person, the screen, the logo and every letter are redrawn and must be checked again in every ratio. For pixel-exact assets (a legal-approved pack shot, a logo lockup, a store screenshot), say so and use Route D.
- **What the node does: its system prompt** (Lyra's `Image resize` system prompt), in short:
  1. **Preserve all visual elements:** product, headline, CTA, logo, offer badge, background, people; nothing dropped, cropped out or omitted.
  2. **Reorganize the layout for the new ratio:** wide → tall stacks the elements vertically, moves text from the sides to the top or bottom and gives the product more vertical space; tall → wide spreads the elements horizontally so text doesn't crowd the product.
  3. **Respect platform safe zones:** 9:16 Stories and Reels: top 15% and bottom 20% are UI overlay zones, all critical content (headline, product, CTA) in the center 65% · 4:5 Feed: the full frame is generally safe · 1:1 Feed: center-weighted, balanced on all sides · 1.91:1 link ads: little vertical space, the product and headline first, the CTA visible.
  4. **Maintain visual hierarchy:** the most important element (product, face, headline) stays the most prominent; secondary elements don't compete.
  5. **Preserve style and colors exactly:** palette, light, grading, shadows, photo treatment; an extended canvas matches the source background seamlessly (texture, color, light); no new colors, gradients or style changes.
  6. **Preserve typography:** the text content identical; weight, color and style identical; only the position changes.
  7. **Breathing room:** nothing cropped tight against the frame edges; margins around the product, headline and CTA.
  8. **Do not improve or enhance:** no upscaling, contrast, sharpening or "fixing"; the goal is the right adaptation, not a better image.
- **Consequences for the skill.** The node already knows the rules; what it doesn't know is **this** ad: which element is primary, where each element should go in each ratio, the exact texts, the screen that must stay identical, and the placement (Stories only, or Reels too). That is what the instruction carries, when the field is reachable. The same 8 rules are written into every Pro recompose prompt (Route B), so every route keeps the same standard.
- **One instruction for several ratios.** The node runs all its ratios from one instruction, so a layout plan per ratio is written as a short list ("9:16: … · 1:1: … · 16:9: …"). If the outputs mix the plans up, split the ratios into one node each.
- **Price** shows on the node next to Run, one generation per ratio; read it and say it before running (base Step 6).

---

## Placements: which ratio, which safe zone

Plan by **placement**, not by ratio: the placement decides the ratio, the pixel size and the safe zone. Specs change: check the platform's current guide before export. Numbers below are directional (Oct 2026).

| Placement | Ratio in Lyra | Export size | Keep key content | Layout note |
|---|---|---|---|---|
| **Meta Feed** (Facebook, Instagram) | **4:5** | 1080×1350 (or 1440×1800) | the full frame is safe; ~5% margins | the master for most statics |
| Meta Feed, square | **1:1** | 1080×1080 | center-weighted, ~5% margins | balanced on all sides |
| **Meta Stories** | **9:16** | 1080×1920 (or 1440×2560) | below the top ~14–15%, above the bottom ~20% | the node's center 65% |
| **Meta Reels** | **9:16** | 1080×1920 (or 1440×2560) | below the top ~14%; headline and hero above the bottom ~20%; **CTA and any small text above the bottom ~30–35%** (the caption overlay grows); ~6% clear on each side | one 9:16 can serve Stories and Reels when it follows the Reels zones |
| Meta link ad, right column, Audience Network | **1.91:1** (not in Lyra) | 1200×628 | build **16:9** and keep the top and bottom ~4% free of key content: the crop from 16:9 to 1.91:1 removes ~7% of the height | the product and headline first, the CTA visible |
| **TikTok** In-Feed | **9:16** | 1080×1920 | below the top ~8–10%, above the bottom ~20–25%, clear of the right ~12% (the action buttons) | check TikTok's safe-zone overlay files |
| **Google App campaigns** (and Demand Gen) | **1:1**, **4:5**, **1.91:1** (via 16:9) | 1200×1200 · 1200×1500 · 1200×628 | Google may crop or assemble the asset: keep text minimal and inside the central area | give all three; a text-free version helps where text gets cropped |
| Pinterest | **2:3** | 1000×1500 | the full frame, ~5% margins | like 4:5 with more height |
| Display banner 300×250 | **5:4** (nearest to 6:5) | 300×250 | ~5% margins | designer trims to the exact pixels |
| Display banner 728×90 | **8:1** | 728×90 | everything readable at 90 px height | Extreme strip rules |
| Mobile banner 320×50 | **8:1** (nearest to 6.4:1) or **4:1** | 320×50 | hero + 2–4 words + CTA only | Extreme strip rules; often a designer job |
| Skyscraper 160×600 | **1:4** | 160×600 | stacked, the CTA at the bottom | Extreme strip rules |
| App Store / Google Play screenshots | exact pixels (1290×2796, 1080×1920) | per store | per store rules | `lyra-ui-motion-video`, Store screenshot sets |

**The default full Meta set** from a 4:5 master: **9:16** (Stories and Reels) + **1:1**; from a 9:16 master: **4:5** + **1:1**. Add **1.91:1** only when link ads, Audience Network or Google run the ad.

**Pixels.** Lyra gives a ratio and a resolution class (1K / 2K / 4K), not exact pixels. 2K comfortably covers 1080-wide exports; the user's designer or the export step scales to the platform's size. Say once that exact pixel sizes are set at export.

---

## The build: four routes

Every image × ratio goes one of four ways. The **route is picked per image and per ratio** in the plan (Best way to build it), and the user sees why.

| Route | What it is | Control over layout | Best for | Weak at |
|---|---|---|---|---|
| **A. Image Resize node** | Lyra's own node (action `image_resize`, **Nano Banana 2**): the source connected, a list of ratios, one output per ratio; it follows the 8 rules above by itself | **medium**: it plans the layout itself; the instruction (when reachable) gives it the plan per ratio | small steps and "add height" moves on simple layouts with calm backgrounds and text far from the edges; many ratios at once; extreme strips (the only route with 4:1, 8:1, 1:4, 1:8); fast and cheap first pass | orientation flips with several text blocks; Pro-level realism (faces, skin, hands); a phone screen that must stay word-for-word exact; precise placement |
| **B. Pro recompose** | a Nano Banana Pro Image Generation node, the approved source connected as [Image1], the **target ratio set in the node**, prompt "Recompose [Image1] for …" with the keep list, the layout plan and every text in quotes; the screenshot and logo uploads connected again when they're on the image | **full**: zone by zone | orientation flips, ads with a person (Pro realism holds), a phone with the real screen, the hero ad of the campaign, anything Route A got wrong | extreme strips (Pro has no 4:1 / 8:1); a layout so different that a rebuild is cleaner |
| **C. Rebuild from the concept card** | a new Pro node at the new ratio from the **original prompt** with only the layout part rewritten for that ratio; the same references connected (persona, screenshot, logo) + the approved image as a style reference with its job stated | full, plus a fresh composition | the source was built in this workflow (its prompt and references exist); a layout that changes completely (a 9:16 stack to 16:9 with three text blocks); carousel sets; when Routes A and B drift twice | costs a full generation; the scene is regenerated, so it is a close sibling of the source, not the same pixels (check against the source) |
| **D. Extension or crop for the designer** | either a **plain crop** outside Lyra (pixel-exact assets), or a Pro **canvas extension** ("Extend the canvas … keep the original image unchanged in the center") with the text then set by the user's designer in Figma | exact | pixel-exact assets (legal-approved, logo lockups); exact pixel sizes Lyra doesn't list (1.91:1 trim, 300×250, 320×50, store screenshots); text the model keeps changing; extreme strips that can't hold every element | needs a designer or a crop tool; outside Lyra |

**How to choose (defaults):**
- **Small step or add height, simple layout, no person in close-up, no readable screen** → A (with the instruction when reachable). Misses fixed with B for that ratio.
- **Orientation flip** (tall ↔ wide) **with two or more text blocks** → B. With one text block and a calm background → A first, B if it crowds the product or drops an element.
- **A realistic person, a face or hands large in the frame** → B (Nano Banana 2 redraws faces with less realism than Pro; the base skill judges realism only on Pro).
- **A phone with the app's screen, or any UI** → B with the screenshot connected again as [Image2] "exactly as supplied" + its key texts, 4K when the screen must be read. Route A only when the screen is small and non-essential, and then checked word by word.
- **The logo on the image** → in B and C the logo upload is connected again as its own reference ("place the logo from [ImageN] exactly as supplied"); in A, check it; if it warps, B or a clean corner for the designer.
- **The source was made in this workflow and the new layout is a different arrangement** → C.
- **Extreme strip** (4:1, 8:1, 1:4, 1:8) → A, after the user has decided what goes into it (Extreme strips below); still crowded → D.
- **Pixel-exact asset, or a size Lyra doesn't list** → D (plain crop, or the nearest listed ratio + designer trim).
- **Two failed tries on one ratio** → change the route (A → B → C → D), never rerun unchanged.

---

## Layout patterns by move

The node's rule 2, made concrete. The Resize sheet writes one of these per ratio, with the shares of the frame.

**Small step (4:5 → 1:1, height −20%).** Keep the zone order; tighten the gaps; the hero shrinks a little or the background extends a little at the sides; the headline keeps its size feel (line breaks may change). 1:1 is center-weighted: the hero centered or on a gentle third, margins even on all sides.

**Add height (4:5 or 1:1 → 9:16).** Extend the background above and below (the same wall, sky, room, gradient). The headline moves into the top clean zone **just below** the top 14–15%; the hero sits in the middle; the CTA above the bottom 20% (above ~30–35% for Reels); the logo inside the safe zone, never in a UI band. The extra height goes to the hero and the background, not to bigger text.

**Remove height (9:16 → 4:5 or 1:1).** The elements come closer together; the extended areas of a 9:16 (sky, floor) are the first to go; nothing primary is cut. The CTA and the logo, often low in a 9:16, move up into the frame.

**Tall → wide (9:16 / 4:5 → 16:9 or 1.91:1).** Rebuild as two columns: the hero on one third (usually the right for left-to-right languages), the text column on the other side (headline on top, subline under it, CTA under the headline, logo small at the bottom of the column). Extend the background sideways. Keep the top and bottom ~4% free when the 16:9 will be trimmed to 1.91:1. The hero never shrinks to a thumbnail to make room: if it doesn't fit, the text gets fewer lines, not a smaller hero.

**Wide → tall (16:9 / 1.91:1 → 4:5 or 9:16).** Stack: headline on top, hero in the middle with more vertical space, CTA below; text that sat beside the product moves above or below it. Extend the background above and below.

**Extreme strips (4:1, 8:1 banners; 1:4, 1:8 skyscrapers).** One row (or one column): the hero (often cropped to its key part: a face, the phone, the product), the headline, the CTA, the logo. Rule 1 says nothing is dropped, but a 728×90 can't always carry a person, a phone, a three-line headline, a subline, a badge and a CTA. If the inventory doesn't fit at a readable size, **ask the user** which element may go (a user decision, never Claude's), or send the strip to the designer (Route D). Never shrink text below what reads at the banner's real size.

**People in any ratio.** Never cut through a face, hands, the phone or the product; head room above the person; a person moves as a whole (no stretching of the body to fill height). Adding height shows more of the body or the room, never a zoomed face.

**A phone with the screen.** The screen stays front-facing and large enough to read in every ratio (half the frame height or more when the screen is the proof); in a wide ratio the phone moves to a third, it doesn't shrink.

**RTL images** (Arabic, Hebrew, Farsi, Urdu, made by `lyra-image-translation`): the text column goes to the right in wide ratios, the hero to the left; never mirror the photo.

**Carousels.** Every card of a set in the same ratio, resized with the same plan (the same grid, the same zone shares), so the cards still line up; continuity elements (a band, a line crossing the card edge) checked across the edges; counter and arrow inside the new safe zones on every card.

---

## Step 1 additions: the source, the placements, the inventory

1. **The source images.** `get_workflow` on the user's workflow (or `list_uploads` for an uploaded file): which image nodes, which selected result, the concept card and the original prompt (they hold the exact texts, the layout map and the references used: persona, screenshot, logo uploads). An image from outside Lyra → `create_upload` + `attach_upload`; if the user attaches it in the chat, Claude also looks at it to make the inventory.
2. **The element inventory.** For each image, every element in reading order: what it is (hero person, phone and screen, product, headline, subline, CTA, logo, offer badge, counter, background), its zone and share of the frame (measured in pixels when Claude has the file: top and bottom of each block divided by the height, left and right by the width), its exact text, and its **priority** (1 = the primary element). Write it into the Resize sheet. Text Claude can't read → ask; never guess.
3. **The placements, not only the ratios.** Ask where the ad runs (Meta Feed, Stories, Reels, TikTok, Google App, link ads, banners) and derive the ratios and safe zones from the Placements table. If the user gives ratios, use them and say which safe zone each will follow (one 9:16 for Stories only, or for Reels too?).
4. **The Brand Kit** (base Reference L) only for checks: the logo file, the colors, forbidden claims. A resize adds no text and no claim, so nothing new is written from the kit; the kit is how Claude spots an element that came out wrong.
5. **Ask only what's needed**, in one message: the placements (or ratios), which images, whether 1.91:1 or banners are needed (they need a designer trim), the screenshot and logo files if the image shows them and they aren't in the workflow, and the user's designer (for Route D).

**Defaults (state, don't ask):** the full Meta set (the master + 9:16 + 1:1) · every element kept, texts identical · a 9:16 that follows the Reels zones, so it serves Stories and Reels · route per image and ratio by the rules above · Nano Banana 2 at 2K for Route A (if the node shows resolution) · Nano Banana Pro at 2K for B and C (4K for small text, a readable screen or a close face) · count 1 per ratio · one Section "Sizes" in the same workflow, to the right of the approved images · languages before sizes · the approved source never edited or overwritten.

**Recommended first run:** A. Pilot ratio (below).

## Step 2 addition: the Resize sheet

The concept the user approves. A user text node "Resize sheet" (a note for the user; it feeds nothing), and the same in the chat:

**1. Per image and ratio: placement, move, route and why**, one line each: "C1 hero static · 9:16 (Stories + Reels) · add height · B (person + phone screen)", "C1 · 1:1 · small step · A", "C1 · 16:9 for 1.91:1 · flip · B, top and bottom 4% clear for the trim".

**2. The element inventory**, one row per element:

| Image · element | Priority | Source zone (share) | Exact text | Notes |
|---|---|---|---|---|
| C1 · Mia + phone with the timer screen | 1 | middle, 22 → 82% of height | screen: "Tonight's plan", "5 min", "Start" | screen identical to screenshot 2 |
| C1 · headline | 2 | top, 0 → 22% | "2 am. Brain won't stop." | heavy white sans, left-aligned, 2 lines |
| C1 · CTA button | 3 | bottom, 85 → 95% | "Try it tonight" | violet #8B7CF6, white text |
| C1 · logo | 4 | bottom-right corner | — | logo.png, small |
| C1 · background | — | full frame | — | dark bedroom, lamp from the right, grey duvet |

**3. The layout plan per ratio**, zones top to bottom (or left to right) with shares, where each element goes, what is extended, the safe zone it follows:

> C1 · 9:16 (Stories + Reels): extend the bedroom above (dark wall) and below (duvet) · 0 → 14%: dark wall, nothing · 15 → 28%: headline, same size feel, left-aligned · 28 → 64%: Mia and the phone, screen front-facing · 64 → 70%: CTA button, centered · 70 → 72%: logo small, centered · 72 → 100%: duvet and phone glow, no key content
> C1 · 1:1: tighten · 5 → 20%: headline · 20 → 80%: Mia and the phone, the room extended a little at the sides · 82 → 93%: CTA centered · logo bottom-right inside the 5% margin
> C1 · 16:9 (trimmed to 1.91:1): two columns, top and bottom 4% clear · left 8 → 45% of the width: headline (top), CTA under it, logo small at the bottom of the column · right 45 → 95%: Mia and the phone on the right third · the dark wall extended to the left

**4. The fit check:** every text keeps its size feel; a line break may move (written in the sheet: "2 am. / Brain won't stop." → one line in 16:9); words never change. A block that can't fit at a readable size in a ratio → re-plan the zone, or ask the user (Extreme strips), never shrink it below readable. Changing the words is not a resize: it's a variant or a translation, and needs the user's yes.

**5. The plan table** (base Step 2) and the credits, in the one approval question (base Step 6).

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the image is | Graph | Models |
|---|---|---|
| **A static with a simple layout, small steps (default)** | approved source (selected result) → **Image Resize node** with the ratios of that route (listed values), the instruction filled from the Resize sheet when the field is reachable → one output per ratio → check → misses fixed with a Pro recompose node for that ratio | nano-banana-2 · nano-banana-pro |
| **A person, a face or hands large in the frame; the hero ad; an orientation flip with several text blocks** | approved source → **one Pro recompose node per ratio** (the ratio set in the node, 2K), the source connected as [Image1] | nano-banana-pro |
| **An image with app UI** (phone shot, UI card, in-app proof) | approved source as [Image1] + the screenshot upload as [Image2] (+ the logo as [Image3]) → one Pro recompose node per ratio, 4K when the screen must be read → word-by-word screen check | nano-banana-pro |
| **The source was built in this workflow and the layout changes completely** | **one Pro rebuild node per ratio**: the original prompt with only the layout part rewritten for the ratio, the same references connected, the approved image as a style reference ("[ImageN] is a style reference only: copy its palette, light, type style and grading; not its layout") | nano-banana-pro |
| **A carousel** (N cards) | per card the same route and the same plan; rebuilt sets through the split pipeline of `lyra-carousel` (the script's layout lines rewritten once for the ratio, the anchors unchanged) | nano-banana-2 / nano-banana-pro |
| **1.91:1** (link ads, Google landscape) | Route A or B at **16:9** with the top and bottom ~4% clear → the designer (or the export step) trims to 1200×628 | nano-banana-2 / nano-banana-pro |
| **Banners and strips** (4:1, 8:1, 1:4, 1:8) | the inventory decision with the user → **Image Resize node** at the strip ratio with the strip plan → check at the banner's real size → the designer trims to exact pixels | nano-banana-2 |
| **An end card or text card for a video** | Route B (or A for a plain card) at the video's ratio; the store badge stays a layer in the Video Editor, never generated | nano-banana-pro · video_composer |
| **Store screenshot sets** | `lyra-ui-motion-video` (Store screenshot sets); exact pixels by the designer | nano-banana-pro |
| **Pixel-exact asset** (legal-approved pack shot, logo lockup) | Route D: a plain crop or the designer's canvas; no generation | — |
| **Languages × sizes** | languages first at the master ratio (`lyra-image-translation`), approved, then each language resized here; count languages × ratios and say the total before running | nano-banana-2 · nano-banana-pro |
| **Many images, many ratios, tight budget** | Route A for every image in one node each → only the misses get a Pro node; Pro recompose only for images with a person or UI | nano-banana-2 → nano-banana-pro |

**Plan example** (base Step 2 table, fictional app Calmly, one approved 4:5 static, full Meta set + 1.91:1):

| # | Node label | Node · model · key settings | Inputs (role) | Stage |
|---|---|---|---|---|
| 1 | Resize sheet | user text (note) | — | — |
| 2 | Ad C1: 2 am POV · 4:5 (approved) | image · nano-banana-pro (existing) | — | — |
| 3 | Screenshot: timer | upload image (existing) | — | — |
| 4 | Logo | upload image (existing) | — | — |
| 5 | C1 · 9:16 · Stories + Reels | image · nano-banana-pro · 9:16 · 4K | 2 ([Image1] source), 3 ([Image2] screen), 4 ([Image3] logo) | 1 |
| 6 | Resize C1 · 1:1 | image resize · google/nano-banana-2 · 1:1 | 2 | 2 |
| 7 | C1 · 16:9 for 1.91:1 | image · nano-banana-pro · 16:9 · 2K | 2, 3, 4 | 2 |

Node 5 is the pilot (the person and the readable screen make it the hardest); node 6 is a small step on Route A; node 7 is a flip on Route B, trimmed to 1.91:1 at export.

Stages for resizing: **1** = the pilot ratio · **2** = the other ratios · **3** = designer trims and exports.

**Canvas.** Section "Sizes" to the right of the approved ads: the Resize sheet note first, then one row per source image, its ratios left to right in the order of the sheet. Labels with the ratio and placement: "C1 · 9:16 · Stories + Reels", "Resize C1 · 1:1", "C1 · 16:9 for 1.91:1". The approved images are never edited or overwritten.

## Run options (resize)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option:

| Option | Runs | Results | Credits | Time |
|---|---|---|---|---|
| **A. Pilot ratio (recommended)** | the hardest ratio of the set (usually the flip or the 9:16 with a person or a screen), every image | one ratio: shows whether the plan, the route and the safe zones work | {x} | ~1 min |
| B. Whole set | every ratio of every image (Resize nodes + Pro nodes) | the full size set | {x} | ~1 to 3 min |
| C. Everything | languages × ratios | the full multi-language size set | {x} total | ~3 to 5 min |

- Recommend A when there are more than two ratios, any orientation flip, a person or a screen: a fix found on the pilot goes into the plans of the other ratios before credits are spent on them.
- C has no pause to check: a dropped element or a wrong letter repeats in every format. Only when the user accepts that.
- Route A charges one generation per ratio even when only one ratio failed; the fix goes to Route B for that ratio only.

## Prompt rules (resize)

| Node | Write | Avoid |
|---|---|---|
| Resize sheet (text) | per image and ratio: placement, move, route and why; the element inventory with priorities and exact texts; the layout plan per ratio with shares and safe zones; the fit check | prompts meant for the model; changed words |
| Image Resize node | ratios from the model's list only; the source connected without a role; a label with the image and the ratios; the instruction (when the field is reachable): the primary element, the layout plan per ratio, the exact texts, the screen and logo to keep unchanged, the placement's safe zone, "nothing dropped, nothing added" | unlisted ratios (`1.91:1`, `2:1`); several sources into one node; a long brief (the node already has the 8 rules) |
| **Pro recompose** | "Recompose [Image1] for {ratio in words}." → each input's job → the **keep list** (every element by name, every text in quotes, the person, the screen, the logo, palette, light, grading, type style) → the **layout plan** zone by zone with shares → what is extended and how (the same background, seamless) → the safe zone → "The only text in the image is …" → "Do not add, remove, restyle or improve anything." → a short "Avoid …" line | re-describing the scene as a new one; "make it better"; new text; two changes at once (a ratio and a new headline) |
| Rebuild (Pro) | the original prompt word for word with only the layout part rewritten for the new ratio; the same references with their jobs; the approved image as a style reference with its job stated | a new scene, new texts or a new style by accident; the approved image as a layout reference (it pulls the old layout back) |
| Canvas extension (Pro) | "Extend the canvas of [Image1] to {ratio}: keep the original image unchanged in the center, continue the background … seamlessly; add nothing" | moving or redrawing the original part |

**Pattern: instruction for the Image Resize node (Route A, ratios 9:16 and 1:1).**

> Primary element: the woman and the phone. Keep every element and every text exactly. 9:16 (Stories and Reels): extend the dark wall above and the duvet below; headline "2 am. Brain won't stop." just below the top 15%, left-aligned, same size; the woman and the phone in the middle; the button "Try it tonight" and the logo above the bottom 30%; nothing in the top 14% or the bottom 30% but background. 1:1: tighten the gaps; headline at the top, the woman and the phone centered, the button and the logo at the bottom with even margins. Keep the phone screen unchanged. No new text.

**Pattern: Pro recompose, 4:5 → 9:16 (Nano Banana Pro, ratio 9:16 set in the node).**

> Recompose [Image1] for a vertical 9:16 Stories and Reels ad. [Image1] is the approved app ad. [Image2] is the app screen: the phone shows it exactly as supplied, every word and number unchanged: "Tonight's plan", "5 min", "Start". [Image3] is the logo: place it exactly as supplied. Keep exactly: Mia, her face, curly hair, grey hoodie and pose, the phone in her hand, the dark bedroom, the warm lamp light from the right, the colors, the grading, the headline "2 am. Brain won't stop." in the same heavy white sans-serif, left-aligned, and the violet #8B7CF6 button "Try it tonight" with white text. Layout from top to bottom: 0 to 14%: the dark wall, extended, nothing else · 15 to 28%: the headline, the same size as in [Image1] · 28 to 64%: Mia and the phone, the screen front-facing and large · 64 to 70%: the button, centered · 70 to 72%: the logo, small, centered · 72 to 100%: the grey duvet and the phone glow, extended, no text. The extended areas continue the same room, texture and light seamlessly. The only text in the image is the headline, the button and the phone screen. Do not add, remove, restyle or improve anything. Avoid: cropped hands or head, a second person, duplicated objects, new text, a changed screen, sharpened or retouched skin.

**Pattern: Pro recompose, 4:5 → 16:9 for a 1.91:1 link ad (Nano Banana Pro, ratio 16:9 set in the node).**

> Recompose [Image1] for a horizontal 16:9 ad that will be trimmed to 1.91:1: keep the top 4% and the bottom 4% free of anything important. [Image1] is the approved app ad. [Image2] is the app screen: show it exactly as supplied. [Image3] is the logo: exactly as supplied. Keep exactly: Mia, her face, hair, hoodie and pose, the phone and its screen, the bedroom, the lamp light from the right, the colors and the grading, every text and its type style. Layout, two columns: left column, 8 to 45% of the width: the headline "2 am. Brain won't stop." on two lines, left-aligned, the same heavy white sans-serif, then the violet #8B7CF6 button "Try it tonight" under it, then the logo, small, at the bottom of the column, all on the dark wall extended to the left · right, 45 to 95% of the width: Mia and the phone on the right third, the screen front-facing. The extended wall continues the same texture, color and light seamlessly. The only text in the image is the headline, the button and the phone screen. Do not add, remove, restyle or improve anything. Avoid: text over Mia or the phone, a shrunken Mia, new objects, new text, a changed screen.

**Pattern: canvas extension for the designer (Route D, Nano Banana Pro).**

> Extend the canvas of [Image1] to a vertical 9:16 frame. Keep the original image exactly as it is, unchanged, in the center. Continue the dark bedroom wall above and the grey duvet below seamlessly: the same texture, color, grain and the warm lamp light from the right. Add nothing: no objects, no text, no people.

**The 6 rules that matter most here:** (1) plan first: the Resize sheet (inventory, priorities, layout per ratio) approved before any run; (2) recompose, don't crop: every element kept, the primary element first; (3) words, style and colors identical, only positions change; (4) the placement's safe zones, Reels stricter than Stories; (5) the route per image and ratio: A for simple and fast, B for people, screens and flips, C for a new arrangement, D for pixel-exact and unlisted sizes; (6) every ratio checked element by element, letter by letter, before upload.

---

## Truth and brand safety

- The base skill's Truth and disclosure applies to every ratio. A resize **adds nothing**: no claim, number, badge, rating, offer or line that the source didn't carry, and never a "filler" text in the new space.
- The logo, the app icon, store badges and the UI come only from the user's files, exactly as supplied; a badge is best added as a layer by the designer in a new ratio.
- **No improvement** means no retouch either: a person's skin, body or face is not smoothed, slimmed or "beautified" in any ratio.
- The Brand Kit's **forbidden claims are enforced absolutely**: if a model invented text in the extended area, it is removed, whatever it says.
- Remind the user once, in the final report, about the platform's AI label for photoreal synthetic people (every size carries it).

## Deliverable and naming

1. A "Resize sheet" note: routes per ratio, the inventory with priorities, the layout plans, the fit check.
2. One image per source × ratio (× language), in Section "Sizes"; the source untouched.
3. For the media buyer: which images form one ad with an asset per placement, which ratio goes to which placement, which ones the designer trims (1.91:1, banners).

Names: the source's code with the ratio replaced: `B4-A:2amBrain-F:Static-PainPOV-C1-9x16`, `…-C1-1x1`; a 16:9 built for a link ad, after the trim: `…-C1-1.91x1`; banners by pixels: `…-C1-728x90`; languages before the ratio: `…-C1-9x16-de` (as in `lyra-image-translation`). Node labels: "C1 · 9:16 · Stories + Reels".

## Meta and Google setup notes (for the media buyer)

- **Meta placement asset customization:** one ad with an image per placement group: 4:5 (or 1:1) for Feed, 9:16 for Stories and Reels, 1.91:1 for link placements. All versions share the message; only the frame changes. Check the current Ads Manager setup (it changes).
- **Meta's automatic creative enhancements** (cropping, image expansion and similar Advantage+ creative options) can re-crop or extend the images again: when the user delivers recomposed sizes per placement, check those options and turn off the ones that would change them.
- **Google App campaigns** assemble and may crop assets: give 1:1, 4:5 and 1.91:1, keep text short and central.
- TikTok: 9:16 only for In-Feed; check the safe zone against TikTok's overlay file.

---

## Common mistakes (resize)

| Mistake | Prevention |
|---|---|
| A crop or a centered copy instead of a recomposition | Layout plan per ratio; Route A or B, never a plain crop unless pixel-exact |
| Resize run before the layout per ratio was agreed | Resize sheet first; pilot ratio |
| An element dropped (logo, badge, CTA) in the new ratio | Inventory checklist in every check; nothing dropped without the user's yes |
| Text rewritten, shortened or restyled to fit | Words identical; only line breaks may move; re-plan the zone |
| Text shrunk until it's unreadable | Keep the size feel; fewer lines or a re-planned zone, never tiny text |
| Headline or CTA under the Stories / Reels / TikTok UI | Placement safe zones; Reels: CTA above the bottom ~30–35% |
| The hero shrunk to make room for text | Primary element gets the space first |
| A face, hands or the phone cut at the edge | People rules: never cut through them; breathing room |
| The extended area shows a new place, a second person, duplicated objects, a seam | "Continue the same background seamlessly"; check the edges; Route B |
| Colors, light or grading shifted; skin retouched; the image "improved" | Rule 8 in every prompt; check side by side with the source |
| The phone screen redrawn in the resize | Route B with the screenshot connected again, key texts in quotes, word-by-word check |
| The logo warped or redrawn | Logo upload connected again (B, C); a clean corner for the designer if it fails |
| `1.91:1` sent to the node | Only listed ratios; 16:9 with the trim margin, trimmed at export |
| A banner with everything shrunk to fit | Strip plan with the user's decision on what goes in; designer for the exact pixels |
| Nano Banana 2 resize judged as the final realism of a person | People and screens through Pro (Route B) |
| Sizes made before the language was checked | Languages first, approved, then sizes |
| Sizes left stale after the source was regenerated | Rerun them; say it in the report |
| One failed ratio fixed by rerunning the whole resize node | Route B for that ratio only |
| The approved image overwritten | Every ratio is a new node; the source untouched |
| Carousel cards resized with different plans | One plan for the whole set; check the cards side by side |

## Quality gates (resize)

Claude can't open Lyra result links, so after each stage it sends the checklist and asks the user what works and what doesn't. If the user downloads the results and sends them in the chat, Claude can also look at each one, compare it with the source element by element, and draw the placement's safe zones over it with a short script (PIL: semi-transparent bands at the zone percentages) to show what falls under the platform UI.
- **Stage 0 (Resize sheet, Claude checks before sending):** every element of every image in the inventory, with its priority and exact text? Placement and safe zone per ratio? Move and route per ratio, with the reason? Only listed ratios for Lyra, unlisted sizes with a trim plan? The primary element given the space first in every plan? No text changed? Extreme strips decided with the user? Screens and logo connected again in B and C?
- **Stage 1 (pilot ratio):** every element of the inventory present, nothing dropped, nothing added? Every word identical to the source, nothing new in the extended area? The same palette, light, grading, type style? The extension seamless (no seams, repeated patterns, duplicated objects, a second person)? The primary element still the most prominent? Headline, hero and CTA inside the placement's safe zone? Breathing room at every edge, nothing cut? Person natural, not retouched? Screen identical to the screenshot word by word? Logo exact?
- **Stage 2 (all ratios):** the same checks per ratio; the set side by side at thumbnail size reads as one ad; carousel cards line up?
- **Stage 3 (trims and delivery):** 1.91:1 and banners trimmed to exact pixels without cutting key content; export sizes per placement; names with ratios; the placement map handed to the media buyer; AI label reminder given?

Pass = every point that applies holds for every ratio. Fix only the failing ratio, with its credits.

## After the test

Read each placement by its own numbers (cost per result for the goal: install, trial, payer; enough results before calling it). A size that underperforms is a hypothesis: the frame (the hero too small in 9:16, the CTA too low), or the format itself (a recomposed 4:5 is not a native Stories ad; a winning static may need a 9:16-first concept, a UGC video or a carousel there). Save the Resize sheet's plans to the project: the next ad with the same layout resizes from the approved plans.
