---
name: lyra-static-image-generation
description: "Use when the user wants a static image ad, banner or creative for a mobile app, e.g. \"a static ad for my app\", \"4 statics to test\", \"an image ad\", \"a realistic photo of...\", \"a persona image\", \"a phone shot\". Builds it end to end in Lyra (concept, layout, on-image text, model, generation). Core image skill the other Lyra image skills build on."
---

# lyra-static-image-generation

The main image skill for Lyra. It holds the core rules for every image: concept and layout, on-image text, realism, styles, models, references, consistency across a series, de-slop and error handling. Smaller image skills (resize and translation, store screenshots, competitor statics, audience swaps, and the image mini skills still to come) point here for these rules. Video skills use this skill's realism and image prompt craft for their keyframes, character images and phone shots; the role of those images in the video stays with the video skill.

Part 1 is shared by every Lyra skill (the same 8 steps as `lyra-video-ad-generation`, written for images). Part 2 is what's specific to static images. The Reference library at the end has the details (models, layout library, text, realism, styles, consistency, UI, errors, de-slop, Meta statics).

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**This is a way of thinking, not a script.** The rules are defaults and good practice; use judgment and say why in one line when you choose differently. Fixed: truth (no invented claims, reviews, numbers, UI or logos), the Brand Kit's facts, UI fidelity (the user's screenshots, exactly), Lyra's technical limits, and the user's explicit choices.

---

# Part 1. [SHARED] How every Lyra skill works

**Deliverable:** a Lyra workflow in which every planned node has been generated. The user opens the canvas and finds the results, the prompts that produced them, and a graph they can edit and rerun for the next app, angle, size or market.

A full creative always follows these steps, in order:
1. **Context.** Collect the app context and task inputs; make sure you have everything before proposing anything.
2. **Concept and plan.** A very short concept with its layout, plus a short plan of nodes, models and connections, based on "Best way to build it".
3. **Approval.** One message: concept, plan, open questions and the cost in credits; the user approves or corrects. Nothing is created before this; the yes also starts the run.
4. **Build.** Create the workflow and nodes with the chosen models, write every prompt into the node's prompt field, upload and connect the assets. Nothing runs yet.
5. **Pre-run check.** Right before every run, read the workflow back and restore anything lost (connections, settings); keep the user's own edits.
6. **Credits and run.** The cost is part of the plan; after the one yes, build and run everything without asking again.
7. **Run and report.** Run, report with the right links (workflow, video or image) and the real spend, offer the next step.
8. **Verify quality.** Check with the user against the quality gates.

## Whose instructions win
1. The user's explicit instructions in this chat.
2. This skill's best practices and defaults.
3. The brand kit: real app facts, claims, value proposition, features, audience, colors.

Best practices are defaults, not rules for the user. When a user's choice will likely hurt the result, follow it and say once in the plan what you'd do instead and why; don't argue twice. When a choice breaks a hard limit (transparent background on Nano Banana Pro, a ratio the model doesn't list), explain and offer the closest build that works.

## Step 1. Context

**App.** Every concept starts from the app. Generic ads come from missing product context, so never fill gaps from imagination.
1. Brand kit given in the chat → use it. Otherwise `list_brand_kits`: one kit → "Make this for {kit name}?"; several → ask which. The user may add or override details in chat.
2. No kit → ask once: send it here, or should I check / connect one of the kits already in your workspace? If the user prefers to type it: app name, what it does, who it's for, the pain it solves, 2–3 features the ad may show, approved claims and offer, forbidden claims, tone, brand colors (hex), assets (logo, app icon, **screenshots only**, product photos if the app has a physical product).
3. Keep the result as an **app card** for the whole session:
   > App card: Calmly · 5-minute wind-down sessions for sleep · for students 18–25 · pain: can't switch off at night · may show: wind-down timer, sleep sounds · claims: none approved · offer: 7 days free · tone: calm, a bit ironic · colors: #1B1F3B navy, #8B7CF6 violet, #F4F1EA cream · assets: logo, icon, 3 screenshots · source: brand kit

**Ask only what only the user knows.** Lyra's own nodes never ask and fill every gap with reasonable assumptions (System Preamble). This skill asks once, in Step 1, only for what can't be assumed (the app, the screenshots and logo, the idea if they have one); for everything else it assumes, states the default in the plan and proceeds.

**Task.** Ask for the inputs in Part 2 → Inputs and defaults; state the defaults instead of asking. Ask for everything missing in one message; never re-ask what the user said. Call `list_workspaces` (credits) and `list_node_configs` (models, ratios, resolutions) now.

## Step 2. Concept and plan

Short: readable in under a minute.

**Concept:** per deliverable, the concept card (Part 2 → Concept and layout): hypothesis in one line, the visual idea, the layout map with every text in quotes, style and palette. N deliverables = N distinct ideas; more takes of one idea is `count` on a node, not more nodes.

**Plan:** name the matching row of Part 2 → Best way to build it in one line, then list the nodes:

| # | Node label | Node · model · key settings | Inputs (role) | Stage |
|---|---|---|---|---|
| 1 | Concept card (note for the user) | user text | — | — |
| 2 | Logo | upload image | — | 1 |
| 3 | Screenshot: timer | upload image | — | 1 |
| 4 | Persona: Mia | image · google/nano-banana-pro · 4:5 · 2K · count 2 | — | 1 |
| 5 | Ad C1: 2 am POV · 4:5 | image · google/nano-banana-pro · 4:5 · 2K | 4 (person), 3 (screen), 2 (logo) as references | 2 |
| 6 | Ad C2: proof shot · 4:5 | image · google/nano-banana-pro · 4:5 · 4K | 3, 2 as references | 2 |
| 7 | C1 · 9:16 + 1:1 | image resize · google/nano-banana-2 | 5 | 3 |

**One image by default.** A static ad is usually one Image Generation node that renders the whole ad: scene, person, phone with the real screen, headline and CTA. Add a separate source node only when: the same person appears in several images (carousel, a series, a later video) · the user wants to pick the face or the product shot first · the screenshot must sit in a phone shot that is checked on its own · a layout keeps failing and is easier in two passes (scene first, then text). Say in one line of the plan why you split or don't.

Stages: **1** = sources (uploads, persona, product or phone shot; fast) · **2** = the ad images · **3** = adaptations (other ratios, other languages, variants).

**Cost:** the plan's total in credits, from Reference A → Credit prices (count and duration included), next to the balance: "≈ 181 credits · balance 47 424".

## Step 3. Approval
**One message, one question.** Everything the user has to decide goes into one message: the concept, the plan with models and quality, any question you still have, and the **cost in credits** with the balance (Step 6). It ends with one question that covers all of it, e.g. "Do the 3 concepts, Nano Banana Pro 2K and ≈ 181 credits (of your 47 424) work for you? After your yes I build the workflow and run everything." Never a separate question about money or about running.

On corrections, show only what changed, with the new cost, and ask again. Don't create anything in Lyra before a clear yes. This yes also starts the run: after it, build and run everything without asking again (Step 6).

## Step 4. Build the workflow
1. `create_workflow` (or `use_template`, or the user's own workflow, or a variation of an existing one: Variations below), then `assign_brand_kit`.
2. Upload the assets the images need (`list_uploads` first, then `create_upload` + `attach_upload`, or `open_upload_widget`): logo, app icon, screenshots, product photos, style or layout references. Never generate a logo, icon, store badge or UI.
3. Write every prompt (Part 2 → Prompt rules). The concept card goes into a user text node (`create_user_text_node`) as a note for the user, connected to nothing. A user text node feeds its text into any node it is connected to, so keep this one unconnected (a Note on the canvas can't be connected at all, but the tools can't create one). The text doesn't keep the style or the person consistent: consistency comes only from images connected as references, plus the anchors written into every prompt.
4. Create every node from the plan with its prompt, its model, ratio and resolution from `list_node_configs`, and a label that says what it's for ("Ad C1: 2 am POV · 4:5", "Persona: Mia"), never "Image 1".
5. **Connect the whole graph now** (`connect_nodes`): uploads and persona → every image that uses them (reference) · the approved ad → resize and translation nodes. References connect before anything is generated, so "run all" works.
6. Lay out the canvas by `lyra-workflow-layout` (STEP notes, sections in reading order, colors, check), one section per stage: **Sources** (concept card, uploads) → **Persona / product** → **Ads** → **Sizes and languages**. An upload sits next to the node it feeds.
7. Check `is_valid` and `validation_error` on every node; fix with `update_node` using listed values.

## Variations, not new workflows
A new version of something that already lives in a workflow goes into a **variation of that workflow** (Lyra's **Create variation**), never into a new workflow, unless the user asks for a new one.
- **When:** a new version of a video (another story with the same characters, another angle, hook, person, setting, length or language, a remake of a failed take), more room for another round, splitting the work, or the user asks for several variations.
- **How:** `create_variation` (it copies the whole canvas: nodes, connections and results) with a clear title ("D2 · Dan's turn") → `switch_variation` to it (the tools and runs work on the main variation; Lyra also renames the workflow after it) → `delete_node` the nodes this version doesn't need → update the prompts and add the new nodes → connect → pre-run check → run. Nodes kept as they are keep their results and cost nothing (characters, places, the end card clip). The variation keeps the canvas layout: update the section titles and labels that name what changed (`lyra-workflow-layout`).
- Deleting inside a variation you just made for this version is part of the build and needs no extra ask. Never delete in the original variation or in one the user made.
- **Report:** the workflow link, the name of the variation with the new version, and that the original is untouched in its own variation (to show it again: `switch_variation`, which renames the workflow back).
- **Images:** new statics, sizes or languages can stay in the same variation as new nodes, one Section per set, unless the user asks for a separate workflow or the canvas gets crowded; then a variation, as for video.
- **Open canvas:** before editing an existing workflow through the tools, ask the user to close its tab or switch away (an open canvas can write its old state over the tool edits), and tell them when it's safe to open it again.

## Step 5. Pre-run check
Right before **every** `run_node` (the first run, each next stage, reruns, follow-ups). The canvas changes between build and run: the user edits it, and an edit on the canvas can drop or overwrite connections. A run with a missing input spends credits for nothing, so never trust what you built a few minutes ago.
1. `get_workflow` now, not from memory.
2. Compare it with the plan: every planned edge (source → target) is there · every node that takes images has them as planned (`image_inputs_usage`: references or frames; a frame points to an existing result) · every node `is_valid`, no `validation_error` · no empty prompt · settings as planned (model, ratio, duration, resolution, count).
3. Lost or changed by accident → restore it (`connect_nodes`, `update_node`) and say it in one line ("the link Character → Clip 1 was gone, reconnected"). Changed by the user on purpose (their prompt, model, a node they added) → keep it and use the workflow as it is now; never overwrite their edits. Not sure which → ask before running.
4. Inputs ready: a node runs only when every node it takes from has a result. Never run a node with a missing input.

After the build, tell the user once that the workflow is built and running and that they can edit any prompt on the canvas and rerun.

## Step 6. Credits and run
**Where the prices are.** `get_workflow` returns `credits` on every node: the estimated credits of one run of it (null = free: uploads, Video Editor, notes, user text; a Section shows the sum of its nodes; null on a paid node means a setting is missing, e.g. no resolution on Nano Banana 2: set it). Before the build, estimate with Reference A → Credit prices; after the build, read the real numbers off the nodes.

1. **In the plan (Steps 2–3):** the estimated total and the balance (`list_workspaces`), inside the one approval message.
2. **After the build, before running:** add up `credits` of every node that will run. Within ~15% of the approved estimate and within the balance → run everything, stage by stage (sources → ads → sizes and languages, Step 7), with no question. More than ~15% over, or over the balance → one short message: the new total, why, and a cheaper option (fewer concepts, lower count, 2K instead of 4K, Nano Banana 2); run after the answer.
3. **Reruns and follow-ups:** give the rerun's credits in the same message as the change ("Changed the headline; rerunning Ad C1 and its 9:16, 46 credits") and run, unless the user asked to check first.
4. **After the run:** the real spend (balance before − after) and the new balance.
5. A source image with count 2 (a character, a persona) feeds the next stage with its selected result; say in the report which one went on and that the user can switch (Step 7).
6. The smaller skills' **Run options** sections give the run order and what each stage holds: run all of it in that order, without offering the options. A staged run (the look first, then the rest) only when the user asks for it, or when the plan is expensive and the look should be approved first: then say so in the approval message, with each stage's credits, and run the next stage on the user's yes to the look.
7. No `credits` on the nodes at all (the field is gone): estimate with Reference A, say it's an estimate, and keep the same one-question flow.

## Step 7. Run and report
1. `run_node` on every node whose inputs are ready stage by stage: sources → ads → sizes and languages. Pre-run check (Step 5) before each stage. Keep each `run_uuid` and `variation_uuid`; call `get_run_results`; while `in_progress`, call it again. **Never call run_node on a running node** (second paid run).
2. **Picking a result.** A node with several results: when the user names one ("take the second", "the first one"), set it yourself on every node that uses it; don't send the user to tick it in Lyra. On a node with `image_inputs_usage` (video nodes): `update_node` with its whole `image_inputs_usage` from `get_workflow` and one field changed: references → `reference_result_image_uuids: [picked uuid]` (or the other results in `exclude_reference_result_image_uuids`); frames → `first_frame` / `last_frame` = `{"node_uuid": source node, "image_result_uuid": picked uuid}`. The results' uuids and their order (first, second…) come from `get_run_results` of the source node's run. Then `get_workflow` to check it held, and rerun what comes after it (pre-run check first). Only when the node has no such setting or the tool refuses: ask the user to tick it in Lyra and say why. Without a pick, the next stage uses Lyra's selected result; say which one went on.
3. Run a stage only after its inputs have results.

**Links in every report.** Never only file links. Two kinds of link, nothing else:
- **Workflow:** `https://app.lyra.splitmetrics.com/workflows/{workflow_uuid}` (opens for anyone signed in to Lyra with access to the workspace; results in a variation: name the variation to open).
- **Result:** the `url` from `get_run_results`, exactly as returned.
- one video → the video link + the workflow link
- several videos → the workflow link only
- one image → the image link + the workflow link
- several images → the workflow link only

Report:
> Calmly · statics · 3 concepts: done. Workflow: https://app.lyra.splitmetrics.com/workflows/{uuid} (3 ads, 9:16 and 1:1 each). Spent {x} credits · balance {X}. Open it to edit any prompt and rerun.

- Name failed nodes: label, what it was asked to do, why if known, the fix you suggest.
- When every node has a result, offer 2–3 next steps (variants of the winner, other sizes, other languages, an animated version).
- After the final images, run `lyra-result-check` straight away, without asking (free): it opens every image in a browser, checks faces, hands, text and logo, and reports the problems with pictures and fixes. Never describe or grade a result you haven't seen; without a browser send the stage checklist (Part 2 → Quality gates) and ask what works and what doesn't. Refer to nodes by label, never by uuid.

## Step 8. Verify output quality
Check final assets, not only job status: completeness (every concept, ratio, language) · message (one promise, hook, claims, offer, CTA match the brief) · text (every letter, every number, hierarchy, nothing extra) · visuals (realism or the chosen style, hands, faces, logo and UI exact) · layout (reads at phone size, safe zones, one focal point) · delivery (ratio, resolution, naming) · variations (intended difference visible) · reusability (prompts editable). Use Part 2 → Quality gates. Suggest fixes only for identified defects, within authorized scope and cost.

## Follow-ups
- One change ("make her older", "bigger headline", "warmer light"): `update_node` on that node, show the new prompt, pre-run check, rerun it and the nodes that depend on it (the rerun's credits in the same message, Step 6).
- A new angle, persona, size or language: hand over to the matching skill.
- Never delete or overwrite results the user may want: a new version goes into a variation (Variations above). `delete_node` only inside a variation you just made for this version, or when the user asks.

## Runtime failures
See Reference I. In short: validation_error → fix with listed values · run failed → name it, one retry with a changed prompt or model and its credits · in_progress → poll again · not enough credits → stop, show the balance and what's missing, offer cheaper (Step 6) · model refused content → tell the user, don't rephrase around it · file without public link → ask for a link or upload in Lyra.

## Base prompt rules
You write every prompt, and each lives in its node's prompt field, where the user reads, edits and reruns it. Write for the model and for the person.
- Self-contained: no "same as above", no references to the chat.
- Concrete and renderable: things the model can show, not marketing concepts.
- The user's own words for the subject and anything they specified stay as given.
- Settings (ratio, resolution, count) go in node settings, not in the prose.
- English, unless text must appear in another language. Exact on-image text in quotes.
- No placeholders, alternatives or "if" branches in a final prompt.

## Common mistakes (every skill)
| Mistake | Prevention |
|---|---|
| Builds or runs before concept and plan are approved | Steps 1–3 first, always |
| Asks about the price or the run as a separate question | Cost goes into the one approval message; the yes starts the run (Steps 3, 6) |
| run_node on a running node | Poll get_run_results |
| Plan without a cost, or a run without reading the nodes' credits | Reference A → Credit prices in the plan; node `credits` before the run |
| Runs with lost connections, or over the user's canvas edits | Step 5 pre-run check before every run |
| Sends the user to tick a result in Lyra | Step 7: set the picked result yourself |
| A new workflow for a new version of the same ad | Create variation of the same workflow, delete what this version doesn't need (Variations) |
| Only file links, or no workflow link | Step 7 links |
| Invents app features, UI, numbers or reviews | Only the app card; without screenshots keep the screen out of view |
| Swaps the user's explicit choice for a default | Instruction order; mention the trade-off once |
| Values the model doesn't list | Copy from list_node_configs |
| Nodes for takes of one idea, or count for different ideas | Ideas → nodes; takes → count |
| Prompts that point back to the chat | Self-contained prompts |
| Reruns an unchanged prompt as a fix | Change prompt, reference or model; say what changed |
| Describes or grades results it can't see | Ask the user with the stage checklist |

---

# Part 2. Static image generation: what's specific

## Description
Creates static ads and images for mobile app paid ads in Lyra, SplitMetrics' node-based creative canvas, leaving a generated, reusable workflow on the canvas.
Use when the user asks for "a static ad", "an image ad / banner", "statics to test", "a carousel", "a realistic photo of…", "a persona / character image", "a product or phone shot", "an illustration in our style", or hands over a layout, a sketch or a reference image.
Works from a Lyra brand kit or app details in chat, app screenshots, logo and icon, product photos, a reference static (through `lyra-copy-competitor-static`), or an existing workflow.
Not for: other sizes or languages of a finished image (`lyra-image-resize` and `lyra-image-translation`, rules from Reference H here) · App Store / Google Play screenshot sets and store-style end cards (`lyra-ui-motion-video`) · copying a competitor's static (`lyra-copy-competitor-static`, which builds on this skill) · the same image for another audience (`lyra-audience-variations`) · video (`lyra-video-ad-generation`).

## Quality bar
Reads in half a second at phone size (one focal point, one promise, a short headline), stops the scroll because it looks native and specific, shows only real app features and the user's real screens, every letter and number exactly right, one CTA, on brand, and no AI look: when the brief asks for a photo, it looks **taken by a camera, not generated**.

## Inputs and defaults
**Required (ask if missing):** the app (brand kit or app card) · the idea or the angle, if the user has one · app screenshots, if the ad shows the app · the logo file, if the ad shows the logo.
**Defaults (don't ask; state them in the plan):** Meta (Facebook / Instagram) · **4:5** master for Feed (9:16 when the user says Stories / Reels; 1:1 when asked) · other ratios as a follow-up, **recomposed, not cropped** · English · **photo-real** style unless the brand or the brief says otherwise · **Nano Banana Pro** for every final (`google/nano-banana-pro`) · **2K** (4K when the image carries small text, a UI screen to read, or a close-up face) · count 1 (2 for the hero or the persona when the user wants a choice) · one CTA · headline 2–8 words · text on ≤ ~20% of the canvas.
**In the plan, always say which model and resolution you recommend and why, and ask whether the user prefers another.**
**Run:** everything after the one yes, in stage order (Step 6).

## Image types: what we make

| Type | What it is | Default build |
|---|---|---|
| **Static ad** (the main job) | one finished ad: visual + headline + CTA (+ logo, UI) | one Pro node, the whole layout in the prompt, references connected |
| **Carousel** | 2–10 cards that read as one story, card 1 carries the hook | one Pro node per card, the same anchors in every prompt; persona / style reference shared |
| **Persona / character** | a person (or mascot) reused across ads, a carousel or a later video | Pro, front-facing or three-quarter, the pain place, count 2; Character Generation rules (Reference E) |
| **Product or phone shot** | the user's screenshot on a phone in a hand or on a backdrop; the app icon; a physical product from the user's photos | Pro with the screenshot / photo connected, fidelity line (Reference G) |
| **Scene / background plate** | a place or backdrop with a clean zone, no text, for the user's designer or for other images | Pro, "clean empty area for text in the upper third" |
| **Keyframe for video** | the first (or last) frame of a clip | built here for realism, at the video's ratio; its role follows the video skill |
| **Illustration / mascot / 3D** | a non-photo style: vector, hand-drawn, watercolor, kawaii, clay 3D | Pro (style described fully) or the style model of Reference A; the brand's own mascot only |
| **Typographic / text card** | type is the hero: a question, a statement, a list, a quote from a real review | Pro, every line in quotes with its style; Ideogram 3.0 as an alternative to test |
| **Cutout / sticker / icon-like element** | an object on a transparent background for a designer | GPT Image 2 with `background: transparent` (only 1:1, 3:2, 2:3) |
| **Edit of an existing image** | change one element, swap the person, change the light, remove a thing | Pro with the image connected, "change only…" (Reference F, edit pattern) |

## Concept and layout

A static has no time: the concept and the layout must be clear in one look. Every concept is written as a **concept card** before any prompt:

> **C1 · Pain POV · 4:5.** We believe students who can't switch off at night will start a trial because a relatable 2 am phone-photo shows the wind-down timer working. **Visual:** Mia, 21, lying in bed at 2 am, phone light on her tired face, holding the phone toward us with the real timer screen. **Layout (top → bottom):** top 22%: headline "2 am. Brain won't stop." white bold sans, left-aligned · middle 60%: Mia and the phone, screen large and front-facing · bottom 18%: CTA button "Try it tonight" in #8B7CF6, logo bottom-right small. **Style:** UGC phone photo, lamp light, deep focus. **Palette:** navy night, warm lamp, violet CTA. **Text total:** 7 words.

**What makes a static concept work:**
- **One promise, one focal point.** One pain or one benefit, one hero (a face, a phone, a result, a big line). A second idea is a second ad.
- **The hook is the picture plus the headline.** They say one idea together (the tired face + "2 am. Brain won't stop."). A picture and a headline that say different things fight; pick one.
- **Specific beats generic.** An exact moment, an exact object, the audience's own words. Stock-photo lifestyle reads as an ad and gets scrolled.
- **Native beats designed.** For cold traffic, a believable phone photo, an in-app proof shot or an apparent post usually beats a glossy billboard layout. Polished brand design is for premium or warm audiences.
- **Show the app only from real screens.** One key screen, large and readable, or no screen at all.
- **CTA names the action** ("Try it tonight", "Start free"), one per ad.
- **Hypothesis is a whole concept**, not one cosmetic change (Lyra's Creative Brief rule): "before/after + 7-day trial addresses doubt", not "a green button". Every concept connects to a testable idea and says **why** it should work: the user is trying to learn what works and why (System Preamble).

**Layout map rules** (written for every concept, copied into the prompt):
- Zones from top to bottom (and left to right), each with what's in it, roughly what share of the frame it takes, and its exact text.
- One reading order: the eye goes 1 → 2 → 3 (usually visual or headline → proof → CTA).
- Text in clean zones with enough contrast (sky, wall, a solid band, a darkened area), never over faces, hands or the screen.
- Safe zones: 9:16 keeps the top ~14% and bottom ~20% free of key content (platform UI); 4:5 and 1:1 keep ~5% margins. The hero sits in the central 65%.
- Logo small (about 8–12% of the height), in a corner, never the hero. Most native statics need no logo at all; the ad account shows the brand.

The **layout library** (Reference B) has the formats that work for apps, each with zones and a build note. The concept picks one and adapts it.

## On-image text

Unlike video, a static carries its text in the image, and Nano Banana Pro renders text well when it is told exactly.
- Every text block in **quotes**, with its zone, size feel (huge / large / small), weight, case, color (hex or name) and alignment: `headline at the top, left-aligned: "2 am. Brain won't stop." in a heavy white sans-serif, very large`.
- **Few words:** headline 2–8 words, subline ≤ 10, CTA 1–4. Up to 3 text blocks per ad. Text on ≤ ~20% of the canvas (Meta no longer rejects more, but text-heavy statics deliver worse).
- Say what text is **not** there: "The only text in the image is: …". Otherwise the model adds signs, labels and fake brand names.
- Another language: the prompt in English, the text in quotes in that language, written by you (not machine-translated word for word).
- Numbers, prices, ratings, offers: only from the Brand Kit or the user.
- **Check every letter with the user** after the run. One wrong letter → rerun naming the right spelling ("the button reads exactly 'Try it tonight'"). Two failed reruns → generate the image with that zone left clean and tell the user to set the text in their design tool (Figma), or move the text to a typography-led model (Reference A).
- Fonts: describe the style ("heavy geometric sans-serif", "handwritten marker"); the brand font name helps when the Brand Kit has one, but exact font matching isn't guaranteed: say so once if the user expects pixel-exact brand type.

## Realism (Nano Banana Pro)

**Nano Banana Pro is our model for the most realistic images.** Every photo-real final (people, rooms, hands, phones, products) is made on Pro at 2K or 4K. Drafts on Nano Banana 2 or Nano Banana are fine for direction, but realism and text are judged only on Pro.

**Realism is coherence, not detail.** Light explains form, materials react to light, the pose obeys anatomy, the camera matches the distance and the composition. "Photorealistic", "ultra realistic", "8K" only state intent; describe the **observable signs of a photograph** instead. When everything serves one scene, the image starts to feel like a real frame.

**Decide first: what camera "took" this photo?** Two families, never mixed:
- **Phone-real (UGC, native, most app ads):** "shot on a 24mm smartphone camera", deep focus with a sharp, readable background, the light that is really there (lamp, window, phone screen, car daylight), slight noise in low light, casual off-center framing, no grading. Portrait bokeh reads as a camera ad, not a phone.
- **Camera-real (lifestyle, editorial, product, campaign):** a lens and its perspective (35mm environmental, 50mm natural, 85mm portrait, macro for detail), controlled depth of field with a reason, one main light with a named source, restrained grading, subtle grain.

**The formula** (in this order): scene and action → appearance and styling → location → composition → camera → light → materials → color and finish → mood → targeted exclusions.

**What makes it real (short):**
- **Skin:** natural tone variation, fine pores, soft texture, natural creases, real asymmetry, live expression; makeup named separately (bare skin, sheer, editorial). Highlights on raised areas, shadows in hollows, no lacquer. Never "flawless", "perfect", "porcelain", "glowing".
- **Light:** one main source with a direction and a reason ("soft overcast daylight from a window at camera left"); shadows and reflections on clothes and background follow it; contact shadows under chin, feet, objects and folds. Don't mix sources without saying where each comes from.
- **Optics:** the lens fits the distance (no wide lens for a close portrait); shallow depth only on purpose; natural focus falloff, natural bokeh, mild optical imperfection.
- **Materials:** name the substance and how it behaves: silk (long soft highlights), cotton (matte, visible weave, creases), leather (uneven sheen, bends), metal (clean reflections), glass (thickness, refraction, edge highlights), concrete and stone (pores, wear, color variation). Pick 2–4 materials that will be visible.
- **Physics:** one phase of one action ("mid-stride, weight shifting onto the front foot, the coat hem swinging"); hair, fabric and objects obey the same movement; a hand visibly touches what it holds.
- **Places:** lived-in, 2–3 specific details that tell the story; never a showroom or an empty minimalist room (unless that is the concept).
- **Edges of the frame:** no randomly cut hands, feet or objects; the crop looks chosen.

**Exclusions:** the Lyra image node has no negative field, so describe the wanted state first ("natural skin texture, subtle pores" rather than only "no plastic skin"), then one short, scene-specific "Avoid …" line at the end. Only the risks of this scene, not the whole list.

The full realism toolkit (skin, light setups, lens table, materials, phrase bank, fixes table, worked prompts, checklist): Reference D.

## Styles

The style comes from the brief and the Brand Kit, not from habit. Choose **one leading style + at most one supporting influence**, and describe it in words (if you name an artist or a director, also describe the look; the model needs the description, and the name can be refused). Full table with cues and risks: Reference C.

| Family | Styles | Default model |
|---|---|---|
| **Photo-real** | UGC phone photo · lifestyle candid · documentary / street · studio product · commercial lifestyle · editorial / fashion · cinematic still · analog film | Nano Banana Pro |
| **Designed** | in-app proof shot · typographic · collage / mixed media · infographic / data · apparent screenshot / native post · retro (Y2K, office-core, 90s print) | Nano Banana Pro (Ideogram 3.0 to test for type-led) |
| **Illustrated** | flat vector · hand-drawn / doodle · watercolor · kawaii · comic / anime-inspired (original characters) · clay / soft 3D · 3D render | Nano Banana Pro; Flux 2 / Wan 2.7 Pro as alternatives to test |
| **Surreal / metaphor** | minimal surrealism · hyperbole (giant notification, tiny person in an inbox) · impossible scale | Nano Banana Pro, photo-real execution |

## Best way to build it
The user's explicit choices override any row. Model choice: Reference A.

| If the request has | Best approach (graph) | Models | Why |
|---|---|---|---|
| **Nothing specific (default)**: 1–4 static ads | concept card → one Pro node per concept, 4:5, 2K, whole layout and every text in the prompt; logo / screenshot uploads as references | nano-banana-pro | fewest nodes; Pro renders people, text and UI best |
| The same person in several images (carousel, series, video later) | persona node first (count 2, user picks) → connected as reference to every image with the person | nano-banana-pro | consistency comes from the reference, not from text |
| The app's UI in the ad | screenshot uploads → in the ad prompt, the screen "exactly as supplied" + key texts in quotes; a separate phone-shot node when the screen is the hero or keeps failing | nano-banana-pro | the UI is never redrawn (Reference G) |
| Carousel | one node per card, same anchors (palette, type, persona, background) word for word; card 1 = hook; last card = CTA | nano-banana-pro | one look across cards |
| Many directions / tight budget | drafts on nano-banana-2 at 1K, count 2–3 → the user picks → winners rerun on Pro at 2K | nano-banana-2 → nano-banana-pro | spend on the winners |
| Text-heavy or type-only poster | Pro first; if a block keeps failing, an Ideogram 3.0 Quality test, or a clean zone for the designer | nano-banana-pro · ideogram-v3-quality | exact type |
| Transparent cutout, sticker, element for the designer | GPT Image 2, `background: transparent`, 1:1 / 3:2 / 2:3 | openai/gpt-image-2 | the only listed model with transparency |
| Edit an existing image (swap person, change one element, relight) | the source image connected → Pro, "change only…" prompt | nano-banana-pro | keeps everything else |
| A reference static to adapt (competitor's static, carousel, several statics, a key frame of their video) | `lyra-copy-competitor-static` → built on this skill's rules | nano-banana-pro | keeps the mechanism, not the identity |
| Other ratios of an approved ad | `lyra-image-resize` (Image Resize, Nano Banana 2) for simple layouts; a Pro **recompose** node with the ad connected when the layout or text must move | nano-banana-2 · nano-banana-pro | recompose, don't crop |
| Other languages | Image Translation (Nano Banana 2) for ads without UI; ads with UI → localized screenshots + text written in that language, new Pro node | nano-banana-2 · nano-banana-pro | the UI is never machine-translated |
| An animated version of the winner | the approved image as first frame → `lyra-ui-motion-video` (UI-led) or `lyra-video-ad-generation` | seedance-2.0 / 2.5 | the static becomes a keyframe |

**Lyra image nodes and the tools.** Lyra has image actions `image_generation`, `character_generation`, `product_screen_placement`, `change_element_on_image`, `image_resize`, `image_translation`, `upload_image`. The MCP tools create **Image Generation** (`create_image_generation_node`), **Image Resize** and **Image Translation** nodes; Character Generation, Product Screen Placement and Change Element come only from templates or the user's canvas (then `update_node` their prompt). Without them, an Image Generation node with the right images connected and a prompt written by their rules does the same job (Reference E, G, F).

## Prompt rules

| Node | Write | Avoid |
|---|---|---|
| Concept card (text) | hypothesis, visual, layout map with exact texts, style, palette, text count | prompts meant for the model; claims not in the Brand Kit |
| **Static ad** (image) | format and ratio in words ("static app ad, vertical 4:5") → each reference's job ("[Image1] is …") → the scene: subject, action, place, camera, light, materials (Realism) → **layout top to bottom** with every text in quotes, style, color, size → the screen "exactly as supplied" + its key texts, if any → palette (Brand Kit hex) → style line → "The only text in the image is …" → short "Avoid …" | "like the reference"; "8K, masterpiece, hyper-realistic"; extra text; generated logos, badges, UI; two promises |
| Photo (no layout) | the realism formula: scene and action → appearance → location → composition → camera → light → materials → color and finish → mood → targeted exclusions | keyword stacks; contradicting lights; "flawless" |
| Persona | "UGC phone photo" or the chosen style → the character card word for word → in the pain place, mid-moment → looking into the camera (selfie / front POV) unless the scene needs otherwise → framing by shot and ratio → realism line → no text | model-like posing; stereotypes; a real person or lookalike |
| Phone shot / product shot | each input's job → device and how it's held or placed → fidelity line → key texts in quotes → backdrop → soft controlled reflections → screen front-facing, large | phone brand logos; fingers or glare over text; strong tilt |
| Edit | strong verb first ("Replace", "Change", "Remove") → what stays exactly (person, pose, framing, light, phone, text) → the one change, concrete → realism → no new text | re-describing the whole scene; two changes at once |
| Carousel card | the shared anchors word for word → this card's role and layout → its text | a different palette, type or persona per card |
| Illustration | the style described fully (line, fill, texture, palette, character proportions) → the scene → layout and text | naming a living artist as the only style cue; known characters |

**Prompt length:** a photo 60–150 words; a full static ad with layout and texts 100–220 words. Over ~250 words, later details get lost: cut adjectives before cutting layout or text. Non-negotiables (identity, the screen, the exact texts) early.

**The 6 rules that matter most here:** (1) one promise, one focal point; (2) the layout map with zones and exact texts, in the prompt; (3) every text in quotes, and "the only text in the image is…"; (4) logo, icon, badges and UI only from uploads, exactly as supplied; (5) realism through observable photographic signs and one coherent light, on Nano Banana Pro; (6) check every letter and every screen with the user before anything is built on the image.

**Pattern: static ad, photo-real with UI (Nano Banana Pro, 4:5).**

> Static app ad, vertical 4:5, UGC phone-photo style. [Image1] is Mia: her face, curly hair in a loose bun, grey hoodie. [Image2] is the app screen. Mia, 21, lies on her side in a dark bedroom at 2 am, holding a modern smartphone toward the camera, screen facing us almost straight on, her thumb at the lower edge away from any text. The phone screen displays [Image2] exactly as supplied: preserve the layout, typography, icons, colors and every word and number; visible on screen: "Tonight's plan", "5 min", "Start". Shot on a 24mm phone camera, deep focus, warm bedside lamp from the right, cool phone light on her face, natural skin texture, visible pores, slight dark circles, rumpled grey duvet, a charger cable and a half-empty glass of water on the nightstand. Layout from top to bottom: top 22%, on the dark wall: headline "2 am. Brain won't stop." in a heavy white sans-serif, very large, left-aligned · middle: Mia and the phone · bottom 15%: a rounded button "Try it tonight" in violet #8B7CF6 with white text, centered. The only text in the image is the headline, the button and the phone screen. Avoid: beauty filter, studio lighting, extra text, logos, warped fingers.

**Pattern: realistic portrait, no layout (Nano Banana Pro).**

> Photorealistic environmental portrait of an adult man in a simple off-white shirt, seated near a window in a lived-in apartment, a candid pause between moments, relaxed shoulders and a natural expression. Eye-level camera, medium close-up, 50mm lens perspective. Soft side daylight with a gentle shadow transition and subtle reflected fill from the room. Realistic skin texture, slight under-eye detail, individual hair strands, natural cotton weave and believable folds. Neutral warm-gray palette, understated documentary feel, authentic photographic tonality. Avoid beauty-filter skin, exaggerated bokeh and artificial symmetry.

**Pattern: edit, one change (Nano Banana Pro).**

> Change only the light. [Image1] is the approved ad: keep the woman, her face, pose, the phone and its screen, the framing, the headline "2 am. Brain won't stop." and the button "Try it tonight" exactly. New light: early morning daylight through half-closed blinds from the left, soft stripes across the duvet, the lamp off. Natural skin texture. No new text.

## Consistency across a series

- **Anchors** written once in the concept card and repeated word for word in every prompt of the series: persona (age, face, hair, skin, outfit), place (room, time, light direction and color), style (production type, palette hex, grading, lens feel), type (headline font style, color, position), device (generic modern phone, case color).
- **Images over words:** the persona, the product shot and any style sample are connected as references to every image that needs them. State each reference's job; an unassigned reference leaks its light or framing.
- One model for the whole series (Pro); one ratio per set; the same resolution.
- In a carousel or A/B set, change only what the test changes; list what's held constant (Lyra's Ad Variation rule).
- Details: Reference E.

## Common mistakes (this skill)
| Mistake | Prevention |
|---|---|
| Two promises or two heroes in one static | One promise, one focal point; the second idea is a second ad |
| Layout left to the model | Layout map with zones, shares and exact texts in the prompt |
| Text garbled, extra words, fake signs | Quotes, few words, "the only text is…"; check every letter; clean zone after two fails |
| Generated logo, icon, store badge or rating | Uploads only, exactly as supplied; real numbers or none |
| UI redrawn or "improved" | Screenshot connected, fidelity line, key texts in quotes, word-by-word check (Reference G) |
| Plastic skin, glossy everything, stock look | Realism section; phone-real for native ads; no "flawless, 8K, masterpiece" |
| Portrait bokeh on a "phone photo" | Phone-real = deep focus, sharp background |
| Light that doesn't match (face lit from the left, shadows to the left) | One named source; shadows and reflections follow it |
| Text over a face, hands or the screen | Clean zones in the layout map; contrast band if needed |
| A crop for another ratio cuts the headline | Recompose for the new ratio; check safe zones |
| Image Translation on an ad with UI | Localized screenshots + text written in that language |
| Persona changes between carousel cards | Persona node connected as reference to every card; same anchors |
| Draft model's result judged as final realism | Realism and text judged only on Pro |
| "Like the reference" in a prompt | Describe the layout and style in words; references only with a stated job |
| Transparent background asked on Pro | GPT Image 2 with `background: transparent` |

## Quality gates
After each intermediate stage Claude sends the stage checklist (the final images are checked by `lyra-result-check`) and asks the user what they like and what they don't (Reference J has the full slop list):
- **Stage 0 (concept, Claude checks before sending):** one promise and one focal point per ad? Layout map with zones and every text word for word? Text short (headline ≤ 8 words, ≤ 3 blocks)? Claims, numbers, offer traced to the Brand Kit? Real screens only, logo from the upload? Style and model stated with why? Safe zones for the ratio?
- **Stage 1 (persona, product, phone shot):** looks like a real person photographed (skin, hair, hands)? Place lived-in? Screen identical to the screenshot, word by word? Style right?
- **Stage 2 (ads):** at phone size (shrink it or look from a distance), does it read in half a second: what it is, for whom, what to do? Every letter and number right, nothing extra? Light, shadows and reflections coherent? Hands, fingers, phone natural? Logo exact and small? Text clear of faces and the screen, inside the safe zone? One CTA? On brand?
- **Stage 3 (sizes, languages, variants):** nothing cropped, headline and CTA inside safe zones, text re-checked in every language, the intended difference visible between variants, files named.
Pass = the user is happy with every point that applies. Fix only what fails, within the agreed budget, with its credits.

## Truth and disclosure
- No invented claims, numbers, ratings, awards, pricing, user counts, reviews or results. A claim may appear only if it is in the inputs (Brand Kit or the user): "clinically tested" in the kit can be used; not in the kit, it can't. Testimonial cards only with real reviews from the Brand Kit, attributed as reviews.
- **Brand safety** (Lyra's System Preamble): nothing that could damage the advertiser's reputation; no profanity, no political statements, no unsubstantiated health claims, no competitor disparagement (an old way vs app comparison never names or mocks a competitor). The Brand Kit's **forbidden claims are enforced absolutely**: they never appear in a headline, a subline, a chat bubble or a visual; if the user asks for one, say once that it is on the kit's forbidden list and leave it out unless the user confirms the kit is outdated.
- An AI person is a creative scene, never a real customer, a verified user or a real expert; no credentials the persona doesn't have (white coat, "Dr."). No body before/after for health or weight-loss apps.
- No real people, celebrities, creators or lookalikes; no known characters, mascots or memes the user doesn't own; no third-party logos or brand marks on clothes, phones, cars or shelves; no copies of iOS, WhatsApp, Instagram or system UI (stylised bubbles and cards only).
- Platforms label AI content: tell the user once, in the final report, to turn on the AI label where the platform asks for it for photorealistic synthetic people. Not legal advice; they check current platform rules.

## Deliverable and naming
1. A "Concept card" text node per concept (or one for the set).
2. Uploads, persona / product / phone shots, the ads, sizes and languages, each labelled.
3. Names: `B{batch}-A:{angle}-F:Static-{format}-C{concept}-{ratio}` (+ `-{lang}` for other languages, `-V{n}` for variants), e.g. `B4-A:2amBrain-F:Static-PainPOV-C1-4x5`, `B4-A:2amBrain-F:Carousel-C2-card3-4x5`.

## After the test
Statics fatigue fast at scale (often 7–14 days): plan refreshes. Read a test by the goal's cost per result (trial, payer), not CTR alone; give it enough conversions before calling a winner. Then offer: variants of the winner one variable at a time (the headline, the visual hook, the person, the proof), other sizes (recomposed), languages, an audience version (`lyra-audience-variations`), new angles (`lyra-ad-concept-multiplier`), or an animated version of the winner (the image as first frame).

---

# Reference library

## A. Image models, settings and price

Always call `list_node_configs` first: it is the live source of image models, ratios, resolutions and actions. **New models will be added**: when a new image model appears, offer it only for what its config and the user's tests show it does well, and keep Nano Banana Pro as the default for realism until the team says otherwise.

**How to offer a model.** Recommend **Nano Banana Pro** for every final, and say plainly: "This is our best model for realistic people, text and UI; it costs more than the drafts, but it gives the best result." Give the cost in the plan (Credit prices below). Always ask which model the user prefers before building.

**Model cards (Lyra, Oct 2026)**
- **★ Nano Banana Pro** (`google/nano-banana-pro`, Google's Gemini 3 Pro Image): **the default for finals and the most realistic frames.** Best in Lyra for photo-real people, skin, hands, rooms, product and phone shots, on-image text, real UI placed from a screenshot, and edits that keep everything else. Resolution 1K / **2K (default)** / 4K; ratios match_input_image, 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9. Takes many reference images (Google's guide: up to 14 in one prompt); keep the set small and give each a job. ~35–50 s per image.
- **Nano Banana 2** (`google/nano-banana-2`, Gemini 3.1 Flash Image): **drafts**, and the default model of Lyra's Image Resize and Image Translation nodes. 1K / 2K / 4K; all Pro ratios plus extreme ones (1:4, 4:1, 1:8, 8:1) for banners and strips. Faster and cheaper; realism and text are checked again on Pro.
- **Nano Banana** (`google/nano-banana`, Gemini 2.5 Flash Image): the original, cheapest and fastest; no resolution setting. Quick tries, simple edits, high volume.
- **GPT Image 2** (`openai/gpt-image-2`): the only listed model with **transparent background** (`background: transparent`): cutouts, stickers, elements for designers. Ratios 1:1, 3:2, 2:3 only. Slow (up to ~90 s).
- **Ideogram 3.0** Quality / Balanced / Turbo (`ideogram-ai/ideogram-v3-*`): typography-led designs and posters; a test option when a text block keeps failing on Pro. Many ratios (1:3 to 3:1) and fixed pixel sizes.
- **Flux 2** Pro / Max / Flex (`black-forest-labs/flux-2-*`): alternatives for photo and stylized looks; Max allows a custom ratio and up to 4 MP. Offer when the user asks or wants a second look to compare.
- **Wan 2.7** / **Wan 2.7 Pro** (`wan-video/wan-2.7-image*`): alternatives; Pro up to 4K (4096×4096) with fixed sizes. Offer when the user asks.

**Task → model:** realistic people, UGC photos, lifestyle, product, phone with real UI, text on the image, edits → Nano Banana Pro · drafts, directions → Nano Banana 2 (or Nano Banana) · resize, translation → Nano Banana 2 (Lyra's default) · transparent cutouts → GPT Image 2 · type-only poster that keeps failing → Ideogram 3.0 Quality test · a second look to compare → Flux 2 Pro / Max.

**Settings in the Image Generation node:** model → aspect ratio (the placement: 4:5 Feed, 9:16 Stories / Reels, 1:1 square; `match_input_image` when editing an image) → resolution (2K; 4K for small text, UI to read, close-up skin) → count (1; 2 for the hero or persona when the user wants a choice) → references connected with their job written in the prompt.

**Cheaper ladder** (one step at a time, show the new price): Pro 4K → Pro 2K → Pro 1K → Nano Banana 2 2K → Nano Banana 2 1K → Nano Banana. Drafts first, finals later: test directions cheaply, rerun only the winners on Pro.

**Credit prices** (Lyra, Oct 2026; credits per run, rounded up; a node's `credits` in `get_workflow` is always the final word):

| Node | Price |
|---|---|
| Nano Banana Pro 2K | 23 per image (1K and 4K not measured yet: read the node) |
| Nano Banana 2 1K | 11 per image |
| GPT Image 2 | 20 per image |
| Ideogram 3.0 Turbo | 5 per image |
| Image Resize (Nano Banana 2, 1K) | 11 per target ratio |
| Image Translation (Nano Banana 2, 1K) | 11 per language |
| Edit / change element | as one generation on that model |
| AI text node · Text Split · user text, uploads, notes | 1 · 0 · 0 |

Count multiplies the price; the ratio doesn't change it. Example: persona (count 2) 46 + 3 ads on Pro 2K 69 + 9:16 and 1:1 of each by Image Resize 66 ≈ **181 credits**. Models or settings not in the table: build, read the node, then tell the user.

**Reference policy.** A technical maximum is not a target: every extra reference makes the result less predictable. Default references = the user's uploads (logo, screenshots, product photos) and the images you generated (persona, product shot). A style sample only when the user brings one or the series needs one look; then say its job ("[Image3] is a style reference only: copy its palette, light and grain; not its people, objects or text").

## B. Layout library: static formats that work for apps

A reference, not a menu. Each format with its zones (top → bottom for vertical) and a build note.

| Format | Layout | Works for | Build note |
|---|---|---|---|
| **Pain POV photo** (default for cold traffic) | headline (the pain in the audience's words) in a clean top zone · the person in the pain moment, phone-real · small CTA band | most apps | Pro, UGC phone photo; the face carries the pain |
| **In-app proof shot** | benefit headline top · the real screen on a phone, 55–65% of the frame · one high-contrast CTA | apps with a clean UI or a visible result | screenshot connected, fidelity line, 4K |
| **Apparent screenshot / native post** | looks like a note, a story or a post with a short first-person text, styled, not a copy of a real app's UI | Gen Z, habits, productivity | stylised generic UI; no platform logos; never presented as a real user's post |
| **Before / after split** | two panels, same framing and light, a short label on each, CTA under | situations that change visibly (messy → organised, late → on time) | never a body before/after for health apps |
| **Result proof** | the result as the hero (a plan, a chart, a score from the real app) · one line why · CTA | finance, fitness, learning, any app with a visible outcome | real numbers and screens only |
| **Comparison: old way vs app** | two columns or rows: the old way (crossed) vs the app's way; short labels | apps replacing a habit or another tool | no competitor names or logos |
| **Listicle / reasons why** | "3 reasons…" headline · 3 short rows with small icons or mini-scenes · CTA | feature-rich apps, considered purchases | ≤ 3 rows, ≤ 6 words each |
| **Chat / comment card** | stylised bubbles: the user's question in their words, the app's warm answer · CTA | coaching, health habits, learning, finance | stylised bubbles, no WhatsApp / iOS copy; fictional chat never shown as real |
| **Review card** | a real review quote large, stars only if real, the reviewer's first name as in the review · CTA | warm traffic, trust categories | only real reviews from the Brand Kit |
| **Starter pack / grid** | "The [audience] starter pack" · 4–6 objects of their life, the app as one of them | lifestyle, habits, hobbies | objects generic, no brand marks |
| **Visual metaphor / hyperbole** | one impossible image of the pain (a giant notification crushing the desk) · short headline | unaware audiences, scroll-stopping | photo-real execution of the impossible; one idea |
| **Big question / statement** | type is the hero on a brand color or a texture · small CTA | bold brands, sound-off feeds | every line in quotes with its style |
| **Offer card** | the offer large ("7 days free") · the app icon (upload) · the product moment small · CTA | warm traffic, real risk reversal | offer from the Brand Kit only |
| **Mascot / illustrated story** | the brand's own mascot in one scene of the pain → fix · headline · CTA | brands with a mascot, kids & family, casual | the brand's mascot as reference; style described |
| **Lo-fi / meme-like original** | deliberately simple, a relatable caption over a scene | Gen Z, casual apps | original format only, never a copyrighted meme image |

**Ratios and placements (Meta):** Feed 4:5 (1080×1350) preferred for direct response, 1:1 (1080×1080) works · Stories / Reels 9:16 (1080×1920), keep the top ~250 px and bottom ~340 px clear of key content · ship 1:1, 4:5 and 9:16 for a full set, each **recomposed**. Check the current specs in Meta's guide before export; they change.

## C. Styles: cues and risks

| Style | Cues for the prompt | Risk to avoid |
|---|---|---|
| UGC phone photo | shot on a 24mm smartphone camera, deep focus, motivated light, casual off-center framing, slight noise in low light, no grading | portrait bokeh, studio light, beauty filter |
| Lifestyle candid | candid moment, available light, 35mm, natural color, unposed gesture | stock-photo smiles, everything clean |
| Documentary / street | documentary photography, available light, real street depth, subject slightly off-center, muted urban colors | frozen mannequin pose, glossy CGI surfaces |
| Studio product | controlled studio lighting, large softbox, bounce card, seamless backdrop, precise shadow shaping, accurate geometry, natural contact shadow | floating objects, impossible reflections, warped lettering |
| Commercial lifestyle | soft directional light, brand palette, clean but lived-in, 50mm | glossy over-saturation |
| Editorial / fashion | high-end fashion editorial, art-directed styling, sculptural pose, 85mm, restrained contrast, subtle grain | waxy skin, impossible garments |
| Cinematic still | cinematic still, motivated practical lighting, restrained color grade, atmospheric depth | teal-orange cliché, haze over the face |
| Analog film | subtle film grain, gentle highlight roll-off, organic color response | fake light leaks everywhere |
| In-app proof / tech | the phone large and front-facing, brand gradient or clean backdrop, controlled glass reflections | fake UI, phone brand logos |
| Typographic | the type described line by line, brand color field or paper texture, generous margins | more than 3 text blocks |
| Collage / mixed media | cut-paper edges, photo + paint + type, layered, slightly imperfect | chaos without a focal point |
| Flat vector | flat shapes, limited palette (brand hex), clean outlines, no gradients or soft gradients | generic corporate "Alegria" people |
| Hand-drawn / doodle / watercolor | visible strokes, paper texture, soft washes, imperfect lines | mixing with photo realism |
| Kawaii / cute | soft pastel palette, round shapes, big expressive eyes, simple backgrounds | known characters |
| Clay / soft 3D | soft clay material, rounded forms, studio light, tactile surface | plastic CGI look when "real" was asked |
| Retro (Y2K, office-core, 90s print) | era-true materials, colors and type, a slight print or screen texture | real logos of the era's brands |
| Minimal surrealism | one impossible idea, photo-real execution, calm composition | stacking several surreal ideas |

## D. Realism toolkit

**Principle:** frame first, beautiful words later. Before writing, decide: the main subject · the action and the exact moment · the place · camera and composition (shot size, height, distance, perspective, placement) · light (source, direction, softness, contrast, color temperature) · materials and textures · mood.

**Universal formula:** [main subject] + [concrete action] + [appearance / styling] + [location] + [composition and angle] + [a logical light source] + [physical textures] + [color and mood] + [photographic character] + [what to exclude].
Short daily version: **SCENE + ACTION + STYLING + LOCATION + COMPOSITION + CAMERA + LIGHT + TEXTURES + COLOR + MOOD + TARGETED EXCLUSIONS.**

**Skin and face:** natural unevenness of tone, fine pores, soft texture, natural folds and micro-details · real asymmetry (small differences between the sides, live expression, natural line of lips and eyelids) · makeup type stated separately (bare skin, sheer makeup, editorial makeup) · no over-retouching, waxy smoothness, uniform shine or over-sharp pores · skin reacts to light: highlights on raised areas, shadows in hollows, no lacquer effect.

**Light setups:** natural daylight: soft window light, overcast daylight, late-afternoon sunlight · studio: large softbox, beauty dish, strip light, bounce fill, controlled shadow falloff · cinematic: motivated practical lighting, warm practical lamps, cool ambient fill, subtle rim light · phone-real: bedside lamp, phone screen glow, car daylight, office fluorescent, bathroom mirror light. Don't mix many sources without saying where each comes from. Ask for natural contact shadows under the chin, feet, objects and fabric folds.

**Optics:** 24mm wide interiors and dynamic perspective (watch edge distortion) · 35mm reportage, environment visible, close involvement · 50mm universal, natural sense of space · 85mm classic portrait, calmer perspective, background separation · macro for tiny details. A close portrait on a wide lens distorts features. Shallow depth of field only with a reason; real optics allow soft focus falloff, natural bokeh, mild imperfections. Camera and lens names are guidance, not magic commands.

**Materials:** silk (soft elongated highlights, fluid folds) · cotton (matte, visible weave, natural creases) · leather (uneven sheen, fine grain, bends where it moves) · metal (clear environment reflections, controlled highlights, believable edges) · glass (reflections and refraction, visible thickness, edge highlights) · stone and concrete (surface variation, small pores, wear, color differences) · phone (glass screen reflections controlled, matte case, no fingerprints over text).

**Motion and physics in a still:** the phase of the action stated (a step at the moment of weight transfer, fabric in flight, hair answering the wind, drops with a clear direction); body, clothes, hair and objects obey one movement; no incompatible simultaneous movements.

**Photographic language (a few precise tags, not dozens):**

| Task | Phrases |
|---|---|
| Fashion campaign | high-end fashion editorial, art-directed styling, sculptural pose, luxury campaign |
| Live reportage | documentary photography, candid moment, available light, unposed gesture |
| Clean studio | controlled studio lighting, seamless backdrop, precise shadow shaping |
| Cinematic atmosphere | cinematic still, motivated lighting, restrained color grade, atmospheric depth |
| Analog photo | subtle film grain, gentle highlight roll-off, organic color response |
| Catalog product | accurate product geometry, clean reflections, precise material rendering, commercial product photography |
| Natural portrait | natural skin texture, realistic catchlights, relaxed expression, believable lens perspective |
| UGC phone photo | shot on a 24mm smartphone camera, deep focus, natural window light, casual, unpolished, no beauty filter |

**Composition:** one main point of attention, the rest supports it · shot size named (extreme close-up, close-up, waist-up, full body, wide environmental portrait) · placement named (centered, off-center, profile, three-quarter view, looking away) · foreground, middle and background when depth matters · negative space when the frame must work as a cover or an ad layout · watch the edges: cut hands, feet, accessories and objects break the feeling of a planned shoot.

**Exclusions bank** (pick only this scene's risks): waxy skin, excessive beauty retouching, plastic texture, uncanny facial symmetry, malformed hands, extra fingers, duplicated limbs, distorted anatomy, floating objects, inconsistent shadows, impossible reflections, warped geometry, over-sharpening, oversaturated colors, fake HDR, excessive bokeh, random text, watermark, logo artifacts. Negative wording doesn't always work literally: also describe the wanted result ("natural skin texture, subtle pores, realistic tonal variation").

**Fixes:**

| Problem | Change |
|---|---|
| Skin looks plastic | Less gloss and retouch; describe pores, tonal variation and natural light |
| Looks like a 3D render | Photographic context, real light sources, contact shadows, physical materials |
| Too many details, chaos | One main subject, one idea of light, a limited palette |
| Face or body unnatural | Simpler pose, a named angle, natural weight distribution, no complex twisting |
| Light doesn't add up | One main source; explain the reflected or back light |
| Background steals attention | Simpler surroundings, lower background contrast, precise depth of field |
| Everything over-sharp | Natural sharpness falloff, soft detail roll-off, moderate processing |
| Too glossy | Replace "luxury / ultra detailed" with concrete textures, calm contrast, restrained grading |
| Text garbled | Fewer words, quotes, size and position named, "the only text is…"; clean zone after two fails |
| Hands wrong | One simple hand action, one object, hand visibly touching it, fewer visible fingers |

**Workflow:** one idea ("quiet luxury in overcast daylight", not cyberpunk + vintage + baroque) → subject and action → composition and camera → light (source and direction; shadows and reflections follow) → 2–4 materials → the image's character (documentary, editorial, studio product, cinematic still) → targeted exclusions → generate a few takes and compare composition, light and believability, not only overall appeal → change **one group of parameters at a time** (composition, then light, then materials or color) → fix locally with an edit, keeping what worked.

**Worked prompts:**
- *Product photo:* "Premium product photograph of a clear glass perfume bottle with a brushed metal cap on a pale travertine surface. Three-quarter product view, carefully controlled reflections, softbox key light from camera left and a subtle white bounce card on the right. Physically plausible glass thickness, clean refraction, accurate label alignment, natural contact shadow and realistic stone pores. Minimal luxury campaign, warm neutral palette, high detail without oversharpening. No duplicated cap, no warped lettering, no floating object, no impossible reflections."
- *Street candid:* "Candid street-style photograph of an adult woman crossing a quiet European city street after light rain, wearing a long trench coat and worn-in leather loafers. Mid-stride, weight visibly shifting onto the front foot, coat hem responding naturally to motion. Shot from sidewalk height with a 35mm lens, subject slightly off-center, real street depth and understated background activity. Overcast daylight mixed with soft reflections from wet pavement, consistent shadow direction, natural skin and fabric texture. Muted urban colors, documentary fashion mood, authentic camera rendering, no glossy CGI surfaces or frozen mannequin pose."
- *Editorial portrait:* "A high-end fashion editorial portrait of an adult woman wearing a sharply tailored charcoal wool coat and minimal silver earrings, standing beside a large rain-streaked window in a quiet modern apartment. Three-quarter portrait, camera at eye level, natural relaxed posture, subtle asymmetry in the expression. Soft overcast daylight from camera left, believable falloff and delicate shadows across the face. Natural skin texture with fine pores and subtle tonal variation, realistic individual hair strands, visible wool fibers and naturally formed fabric creases. 85mm portrait lens, restrained depth of field, crisp focus on the eyes, soft but legible background. Muted charcoal, stone and cool beige palette, refined filmic color, subtle grain, realistic highlight roll-off. No waxy skin, no excessive retouching, no distorted hands, no artificial halo lighting, no over-sharpening."

**Pre-generation checklist:** main subject clear? Action or pose concrete? Place clear and background logical? Shot size, angle and composition set? Light source clear, and shadows and reflections match it? Skin, fabric and key materials described? Lens, distance and perspective agree? Palette and mood serve one idea? Exclusions specific to this scene? Any words that add no visual information (cut them)?

## E. Persona and consistency

**Persona (Lyra's Character Generation and Character Brief rules).** If the canvas has a Character Generation or Character Brief node, `update_node` its prompt; otherwise a Pro Image Generation node written to the same rules:
- Exact identifiers: age range, gender, ethnicity, hair (color, length, style), face details with small imperfections, build, distinctive marks. Clothing is the main consistency anchor.
- Natural, not model-like; slightly imperfect; looks directly into the camera (selfie or front POV) unless the scene needs otherwise; in a believable real place tied to the product context; feels like a real person from Stories or TikTok.
- Framing by shot: full body (lifestyle, action, with footwear) · waist up (conversational, product holding, testimonial) · close-up (emotional hooks, reactions). Framing by ratio: 9:16 person in the central 65% with space for text top and bottom · 4:5 and 1:1 waist up, centered · 16:9 off-center on the thirds.
- Expression by the moment: caught or excited for a hook, tired or annoyed for the problem, relieved for the solution.
- No text in the persona image. No stereotypes, no real people or lookalikes; adults only as the speaking or main persona.
- Character card written once, repeated word for word: "Mia · 21 · student · light brown skin, freckles, dark curly hair in a loose bun · no makeup, slight dark circles · oversized grey hoodie, thin silver hoops".

**Across a series:** the persona image connected as reference to every image with the person ("[Image1] is Mia: use her face, hair and hoodie"); the place, light and style anchors repeated word for word; the same model and ratio. **When it drifts:** move the identity line to the start, shorten the prompt, simplify the pose; a reference leaking light or framing → state its job or drop it; after two fails, regenerate the persona with a clearer front view and reconnect.

## F. Edits and swaps

Edits keep what works and change one thing. Pro, the source image connected, `match_input_image` ratio.
- **Verb first**: Replace, Change, Remove, Add, Relight, Recompose.
- **Keep list** before the change: person, face, pose, framing, camera angle, phone and screen, every text.
- **One change per edit**, described concretely (class, age, material, light direction).
- **Person swap:** the original frame + the new persona connected; "replace only the person in [Image1] with the woman from [Image2]".
- **World swap:** change the room, outfit, car, prop or light; "keep the person, face, hair, pose, phone and framing exactly".
- **Recompose for a new ratio:** "Recompose [Image1] for vertical 9:16: keep the person, the phone screen, the headline '…' and the button '…' exactly; extend the bedroom naturally above and below; move the headline into the top clean zone below the top 14%; keep the button above the bottom 20%."
- Check for **bleed** (traces of the old face, outfit or room), hands, the screen and the text. Bleed → "change only…" moved to the start; after two tries, generate fresh with the new element as the only reference for that layer.

## G. App UI, logo and icon in images

Full rules: `lyra-ui-motion-video` (UI fidelity, screens, store sets, end card). The essentials for statics:
- **Never invent or change anything in the UI.** Screenshots only (never a screen recording), current version, full resolution; no screenshot → the screen faces away, is dark or out of frame.
- In the prompt: each input's job ("[Image2] is the app screen") → "The phone screen displays [Image2] exactly as supplied: preserve the layout, typography, spacing, icons, colors and every word and number; do not redesign, simplify, translate or add anything" → the 3–5 key visible texts in quotes.
- Phone almost front-facing (tilt up to ~15°), screen large (half the frame height or more for a read moment), generic modern phone without a brand logo, no fingers or glare over text, 4K when the screen must be read.
- **Check word by word with the user** before anything is built on it. A wrong letter → rerun naming the right text. After two fails: larger screen, simpler pose; still failing → the clean screenshot placed flat (as a card, not in a hand), or the screen left for the designer.
- A blurry screenshot: ask for sharper originals; otherwise improve it on Pro ("Upscale and sharpen this app screenshot. Keep it exactly as supplied…") and check it word by word before use.
- **Logo and app icon:** only the uploaded files, connected as references, "place the logo from [Image3] exactly as supplied, small, bottom-right"; check it; if it warps, leave the corner clean for the designer. Store badges, ratings, awards: official files and real numbers only; badges are best added by the designer.
- **Image Translation never on images with UI** (it would translate the interface). Other markets = the localized app's screenshots.

## H. Sizes and languages (for `lyra-image-resize` and `lyra-image-translation`)

- Other ratios: **recompose, don't crop.** Simple layouts with text far from the edges → Image Resize node (Nano Banana 2, one output per ratio). Layouts where text or the hero must move, or Pro-level realism must hold → a Pro recompose node (Reference F). Check headline, CTA and hero inside the new safe zones.
- Other languages: ads without UI → Image Translation node (Nano Banana 2, one output per language); check every word with a speaker of that language if possible and check length (translations run longer; the layout may need a shorter line). Ads with UI → localized screenshots + the text written in that language, new Pro node.
- Every adapted image is checked again: text, cropping, safe zones.

## I. Errors

| Problem | Fix |
|---|---|
| `validation_error` on a node | update_node with values from list_node_configs (ratio and resolution differ by model) |
| Ratio not available on the model | Pick a listed ratio or a model that has it (GPT Image 2: only 1:1, 3:2, 2:3; Nano Banana: no resolution) |
| Text garbled or misspelled | Fewer words, quotes, size and position, "the only text is…"; rerun naming the right spelling; clean zone after two fails |
| Extra text, fake signs, fake brand names | "The only text in the image is…"; blank surfaces described ("plain wall") |
| UI redrawn or changed | Fidelity line, key texts, larger screen, 4K; flat screenshot card as fallback (G) |
| Logo warped or invented | Upload connected with its job; leave a clean corner for the designer |
| Plastic skin, CGI look | Realism section; phone-real or camera-real cues; remove "8K, flawless, hyper-realistic" |
| Hands and fingers wrong | One simple hand action, one object, visible contact; fewer fingers visible |
| Persona drifts across images | Persona connected to every image; identity line first; same anchors (E) |
| Reference leaks its light, colors or framing | State its job in the prompt or drop it |
| Resize cut the headline | Recompose on Pro, or move the text zone (H) |
| Translation changed the UI | Never translate UI images; localized screenshots |
| Transparent background ignored | Only GPT Image 2 with `background: transparent` |
| Model refused (a real person, a brand) | Tell the user; don't rephrase around it; offer an original persona or generic object |
| Image ignores a reference | Connect it; name it ([Image1]) and give it a job in the prompt |
| Two failed tries | Simplify the concept (fewer elements, fewer words), change one variable, or change the model; never rerun unchanged |

## J. De-slop for images

**Prevent:** style from the brief, not "premium" by default · real skin, real hair, real hands · lived-in places with 2–3 specific details · one light logic · no "stunning, 8K, masterpiece, hyper-realistic, flawless" · one focal point · text short, in quotes, nothing extra · real UI, real logo, real numbers only · a short scene-specific "Avoid …" line.

**Slop signs:** faces (plastic or waxy skin, uncanny symmetry, dead eyes, teeth melting, too-perfect makeup) · hands (extra or merged fingers, a phone held impossibly, fingers through objects) · text (garbled letters, fake words, extra signs, wrong spelling of the app name) · UI and logo (invented screens, changed text, warped logo, generated badges) · light (shadows in two directions, halo, no contact shadows, fake HDR) · scene (floating objects, warped straight lines, impossible reflections, duplicated items) · look (over-glossy, over-saturated, stock vibe, everything perfectly clean, wrong style for the brief) · layout (two heroes, text over the face, CTA outside the safe zone, cluttered).

## K. Static ads on Meta (what works)

- Statics still carry a large share of app spend and are cheap to iterate; video wins for some categories (casual games, dating, social, demos that need motion). Test both; a winning static is also a ready keyframe for a video.
- Native beats designed for cold traffic: phone-real photos, in-app proof shots, apparent posts. Logo-and-headline-only designs and stock lifestyle photos tend to convert worst.
- One promise, one CTA, a hook that names a friction the viewer feels; the subject readable in the first half second (median fixation on a feed static is under 2 s).
- Text on ≤ ~20% of the canvas (the old rule is gone, text-heavy statics still deliver worse). Meta's headline field (separate from the image) ~27 characters.
- Sizes: 4:5 (1080×1350) Feed, 1:1 (1080×1080), 9:16 (1080×1920) Stories / Reels with top and bottom clear; a full set ships all three, recomposed.
- Volume and fatigue: statics at scale often fatigue in 7–14 days; refresh concepts, not only colors. Test one variable at a time inside a concept (headline, visual hook, person, proof), several different concepts across a campaign.
- Judge by trials, payers and day-7 retention, not CTR or CPI alone.

## L. Brand Kit

Every concept, text, prompt and palette is built on the Brand Kit: audience first, then product, value, tone, colors (hex), claims, forbidden claims (enforced absolutely), offer, must include / exclude. Source order: the chat → the kit connected to the workspace / workflow → ask (send it, or check and connect one of the workspace's kits). The user's chat request always wins; the kit fills everything they didn't say; mention a conflict in one line.
