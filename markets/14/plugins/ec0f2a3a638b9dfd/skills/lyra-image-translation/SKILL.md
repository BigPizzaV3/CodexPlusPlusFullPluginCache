---
name: lyra-image-translation
description: "Use when the user wants the text on an ad image in other languages, e.g. \"translate this ad into German and Japanese\", \"localize the banner for Brazil\", \"the same static in 5 languages\", \"translate the carousel\", \"Arabic version\". Writes the copy per market and rebuilds the images in Lyra, keeping the design."
---

# lyra-image-translation

Image helper skill. Takes an image that is already approved (a static ad, carousel cards, an end card, a store screenshot set) and makes it speak another language: the same ad, the same design, the same promise, with every word written for the new market and checked letter by letter. One output per language, labelled and named so the media buyer can upload them as one multi-language ad.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

**Translation is copywriting first, rendering second.** The hard part is not getting letters onto the image, it's having the right words: a headline that sounds native, fits the zone, keeps the hook and says nothing the Brand Kit doesn't allow. So the words are written and approved **before** any credits are spent, in a Localization sheet, and only then rendered. A node that translates on its own is a tool, never the author.

**Base skill first.** Everything not written here follows `lyra-static-image-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, on-image text rules, realism, models (Reference A), layout library (B), edits (F), UI and logo (G), sizes and languages (H), errors (I), de-slop (J), Meta statics (K), Brand Kit (L). This file adds what is specific to languages and markets. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.**
- Other **sizes** of the translated images → `lyra-image-resize` (Image Resize) or a Pro recompose (base Reference F, H). Order: languages first, sizes second (below).
- An image with **app UI** → UI fidelity from `lyra-ui-motion-video`: the interface is never machine-translated; other markets use the localized app's screenshots.
- A **market version** where the person, the room, the props or the voice should change too (a local face for Brazil, a Japanese apartment) → `lyra-audience-variations` (mode B, market markers). This skill changes only words; the moment the picture must change, it is an audience version.
- **Carousels** → `lyra-carousel` (Story Bible, script, Text Split); this file says how a carousel is localized.
- The **headline as a hook** in the new language → the line checks of `lyra-video-hooks` (one idea, simple, specific, true) apply in every language.
- **Video**: voiceover and captions in other languages are in the video skills (`lyra-video-ad-generation` Reference C: one VO script per language, its own voice, length checked). This skill covers only the images inside a video (an end card, a text card, a keyframe with a sign).
- A competitor's ad in another language as the reference → `lyra-copy-competitor-static` (their words are never translated into ours; ours are written from the Brand Kit).

**This is a way of thinking, not a script.** The rules are defaults and good practice; use judgment and say why in one line when you choose differently. Fixed: truth (no claim, price or offer a market's Brand Kit doesn't approve), the Brand Kit's facts and forbidden claims, UI fidelity (localized screenshots only, never a translated interface), the do-not-translate list, Lyra's technical limits (the language codes the node accepts), and the user's explicit choices.

---

## How to think about image translation

**Four things change, in this order of importance:**

| Layer | What it means | Who decides |
|---|---|---|
| **1. Words** | the headline, subline, CTA, labels, bubbles, counters, written natively for the market (not word for word) | Claude writes, the user (ideally a native speaker) approves |
| **2. Fit** | the new text fits its zone at the same size feel: length, line breaks, script, direction (RTL), font support | Claude plans in the sheet, checks after the run |
| **3. Market facts** | price, currency, offer, store name, date and number format, legal lines, the app's name in that market | the Brand Kit per market, or the user |
| **4. The picture** | the person, the place, gestures, objects that don't fit the market | not this skill: `lyra-audience-variations`, if the user wants it |

**Translate, transcreate or rewrite.** Decide per text block and write it in the sheet:
- **Translate** (meaning kept closely): labels, feature names, counters, plain CTAs, anything that must match the app or store wording.
- **Transcreate** (same job, same feeling, new words): headlines, hooks, puns, rhymes, idioms, questions in the customer's voice. "2 am. Brain won't stop." becomes what a tired student in Lisbon would actually think, not a dictionary sentence.
- **Keep** (never translated): the app name, the brand name, trademarked feature names (unless the Brand Kit has a localized name), the logo, store badges (the official localized badge file instead).

**Final test for every language:** would a native speaker in that market read it as an ad made for them, not a translated one? Does every word fit, read at phone size and say only what the Brand Kit allows there?

---

## The build: four routes

Every image × language goes one of four ways. The **route is picked per image** in the plan (Best way to build it), and the user sees why.

| Route | What it is | Control over words | Best for | Weak at |
|---|---|---|---|---|
| **A. Image Translation node** | Lyra's own node (action `image_translation`, model **Nano Banana 2**): the source image connected, a list of language codes, one output per language; it translates only the ad's communication text (hook, headline, value line, CTA, offer, captions) and keeps logos, brand and product names, environment text and UI text as they are (its system prompt, below) | **medium**: it adapts the meaning by itself; a user instruction can steer it (the approved words, the glossary) when the node's instruction field is reachable | statics with short text, many languages at once, fast and cheap first pass; also images with UI when the app has no localized version (the UI stays as is) | exact hooks and puns without an instruction, pt-BR vs pt-PT, long text, small text, complex scripts, layout that needs to move |
| **B. Text-replace edit (Pro)** | a Nano Banana Pro Image Generation node with the approved source connected, `match_input_image`, prompt: "Change only the text…" with every new line in quotes | **full**: the exact approved words | headlines and hooks, every language not in the node's list, regional variants, any image where Route A got a word wrong, the hero ads | very long text (more than ~3 blocks), images where the layout must change |
| **C. Rebuild** | a new Pro node from the original concept card: the same layout map and prompt, the texts in the new language, **localized screenshots** connected | full, plus layout | images with **app UI**, RTL layouts that should be mirrored, text that no longer fits and needs a new layout, carousel sets in the split pipeline | costs a full generation; the scene can shift (connect the original as a reference with its job stated) |
| **D. Clean plate + designer** | the image with the text zones left empty (a Pro edit: "Remove all text…"), the localized text set by the user's designer in Figma | exact, pixel-perfect type and fonts | legal lines, disclaimers, price tables, long copy, scripts the model keeps breaking (small Thai, Devanagari, Arabic), pixel-exact brand fonts | needs a designer; outside Lyra |

**How to choose (defaults):**
- **1 to 3 short text blocks, language in the node's list** → A with an instruction carrying the approved words and the glossary (when the instruction field is reachable), or A as a fast first pass; fix the misses with B.
- **The headline is a hook, a pun or a customer-voice line; the hero ad of the campaign; the user approved exact words and the node takes no instruction** → B.
- **The image shows the app's screen** (a phone, a UI card, a store screenshot) **and the app is localized in that market** → C with the localized app's screenshots, so the ad shows what the viewer will see after install. **The app is not localized** → A is fine: the node keeps UI text unchanged by default. Never instruct the node to translate the UI (it would rewrite the interface "realistically", which breaks UI fidelity).
- **A language or variant the node doesn't list** (pt-BR vs pt-PT, es-MX vs es-ES, fr-CA, Catalan, Croatian…): regional variants of a listed language (pt-BR, es-MX, fr-CA) → A with the variant named in the instruction, when the field is reachable, otherwise B; languages not in the list at all (Catalan, Croatian, Slovak, Bulgarian, Serbian, Kazakh…) → B (or C).
- **RTL** (`ar`, `he`, `fa`, `ur`) → B for a simple headline over a scene; C when the layout has a reading order (chat bubbles, arrows, a list, a CTA corner) that should mirror.
- **Text that must be pixel-exact or legally reviewed** → D.
- **Two failed tries on one block** → D for that block (base rule: clean zone for the designer).

---

## Lyra facts: the Image Translation node (Oct 2026)

From `list_node_configs` and the MCP tools; re-check at the start of every build.

- **Action** `image_translation` on the image node type; **preferred model `google/nano-banana-2`** (Nano Banana 2 params: resolution 1K / 2K / 4K, default 1K; aspect ratio incl. `match_input_image`). Whether the translation node shows these settings is checked after creating it (`get_workflow`); when it does, set **2K** (4K for small text) and **`match_input_image`**, so the output keeps the source's size.
- **Tool:** `create_image_translation_node` (workflow_uuid, `languages`, `model_name`, label). Then `connect_nodes` source → translation node **without a role**. One output per language. It generates nothing until `run_node`.
- **Language codes** (exact, case-sensitive; only these): `ar` Arabic · `be` Belarusian · `bn` Bengali · `zh-CN` Chinese (Simplified) · `zh-TW` Chinese (Traditional) · `cs` Czech · `da` Danish · `nl` Dutch · `en` English · `tl` Filipino (Tagalog) · `fi` Finnish · `fr` French · `de` German · `el` Greek · `he` Hebrew · `hi` Hindi · `hu` Hungarian · `id` Indonesian · `it` Italian · `ja` Japanese · `ko` Korean · `ms` Malay · `mr` Marathi · `no` Norwegian · `fa` Persian (Farsi) · `pl` Polish · `pt` Portuguese · `pa` Punjabi · `ro` Romanian · `ru` Russian · `es` Spanish · `sw` Swahili · `sv` Swedish · `ta` Tamil · `te` Telugu · `th` Thai · `tr` Turkish · `uk` Ukrainian · `ur` Urdu · `vi` Vietnamese.
- **No regional variants**: one `pt`, one `es`, one `fr`, one `en`. Brazil vs Portugal, Mexico vs Spain, Canada vs France, US vs UK spelling → Route B with the exact words.
- **The source must have a result.** If the image node made several, the user selects one in Lyra first; the translation uses the selected result. If the source is regenerated later, the translations are stale: rerun them.
- **What the node does: its system prompt** (Lyra's `image_translation` system prompt), in short:
  - **Translates only communication text:** hooks, headlines, value propositions, CTA, offer text, captions and short messaging overlays.
  - **Never translates brand elements:** logos, brand names, product names and identity slogans, unless explicitly instructed.
  - **Ignores non-communication text:** environment text (street signs, packaging, decor), decorative text.
  - **UI:** keeps app or product UI text unchanged **unless the user instruction explicitly asks** to translate it (then it keeps layout and hierarchy). Our rule: never ask; localized screenshots instead (Route C).
  - **Preserves the visual:** no change to layout, composition or design; keeps text length visually balanced (no overflow, no awkward wrapping); adapts phrasing for meaning, native sound and the original tone rather than word for word.
- **Consequences for the skill.** The node is a decent transcreator on its own, and it takes **user instructions** ("unless explicitly instructed"). So the approved words, the glossary, the market variant ("Brazilian Portuguese, informal você") and "translate the slogan too" can be given to it as an instruction. The MCP create tool has no instruction field: after `create_image_translation_node`, `get_workflow` and check whether the node has a prompt field that `update_node` can fill. Write in the project notes what the first build shows, so the next build skips the check. No field reachable → Route A runs on the node's own judgment, and exact words go through Route B.
- **One instruction for several languages.** The node runs all its languages from one instruction, so an instruction with exact words per language is written as a short list ("de: headline '…', button '…' · fr: …"). If the outputs mix the languages up, split the languages into one node each.
- **Price** shows on the node next to Run, one generation per language; read it and say it before running (base Step 6).

---

## Step 1 additions: the source, the markets, the glossary

1. **The source images.** `get_workflow` on the user's workflow (or `list_uploads` for an uploaded file): which image nodes, which selected result, the concept card and the original prompt (they hold the exact English texts and the layout map). An image from outside Lyra → `create_upload` + `attach_upload`; Claude also looks at it in the chat if the user attaches it, to read every text block.
2. **The text inventory.** For each image, every text block in reading order with its zone, job (hook, headline, subline, label, bubble, counter, CTA, legal), word and character count, and whether it is on the image or inside a screen (UI). Write it into the Localization sheet. Text Claude can't read → ask; never guess.
3. **The markets, not only the languages.** Ask for the market behind each language: `pt` for Brazil or Portugal? `es` for Spain, Mexico or the US? `en` for the UK? `zh-TW` for Taiwan or Hong Kong? A market decides spelling, words, currency, price and the store.
4. **The Brand Kit per market** (base Reference L): localized app name and feature names, approved claims and **forbidden claims per market** (health and finance claims differ by country), the offer and price per market, tone of voice in that language, localized store badges, localized screenshots. Several kits (one per market) → ask which; never mix two kits in one image.
5. **The glossary (do-not-translate and fixed terms).** App name, brand name, feature names as they appear in the localized app, the CTA as it appears in that store ("Get" / "Install" are the store's own words per language), terms the brand already uses in that market. If the app is localized, its own UI strings are the glossary: a feature is called on the ad what it is called in the app.
6. **Who checks.** Is there a native speaker on the user's side for each language? If not, say once that Claude's translation is a strong draft, not a sign-off, and offer back-translations for the user to judge meaning.
7. **Ask only what's needed**, in one message: the languages and markets (with Claude's recommendation if the user asks "which markets"), the screenshots of the localized app if any image shows UI, prices and offers per market if the image shows one, the native reviewers, how many images.

**Defaults (state, don't ask):** every text block localized, nothing left in English unless it is on the glossary · the same ratio as the source, sizes after languages · Route A for images with short text (with the approved words as its instruction when possible), Route B for hero ads and hooks when the node takes no instruction, Route C for images with UI when the app is localized in that market · Nano Banana 2 at 2K for Route A (if the node shows resolution), Nano Banana Pro at 2K for B and C (4K for small text) · count 1 per language · one Section "Languages" in the same workflow (a Lyra variation per market only when the picture changes too) · the ad copy outside the image (primary text, headline field) localized in the same sheet.

**Recommended first run:** A. Pilot language (below).

## Step 2 addition: the Localization sheet

The concept the user approves. A user text node "Localization sheet" (a note for the user; it feeds nothing), and the same table in the chat:

**1. Per image: route and why**, one line each: "C1 hero static · B for de, fr, pt-BR (hook line transcreated); A for it, nl, pl (short headline, fast)", "C2 phone shot · C (UI: localized screenshots)".

**2. The copy table**, one row per text block × language:

| Image · block | Job | Source (EN) | Chars | Target (de) | Chars · ratio | Back-translation | Mode | Notes |
|---|---|---|---|---|---|---|---|---|
| C1 · headline | hook | "2 am. Brain won't stop." | 23 | "2 Uhr nachts. Kopf ist an." | 26 · 113% | "2 at night. Head is on." | transcreate | fits the top 22% on 2 lines |
| C1 · CTA | CTA | "Try it tonight" | 14 | "Heute Nacht testen" | 18 · 129% | "Test tonight" | translate | button widens ~15%; OK |

**3. The glossary** (do not translate / fixed terms) and the **market facts** (price, currency, offer, store wording) per language.

**4. The fit check**: every block with a length ratio over about **120%** is shortened (transcreated tighter), never shrunk to fit; over **140%** → the zone is rethought (two lines, Route C) and said in the plan.

**5. The ad copy outside the image**, per language: primary text (~125 characters before "more" on Instagram), headline field (~27 to 40 characters), CTA button (Meta's own localized buttons).

**6. The plan table** (base Step 2) and the credits, in the one approval question (base Step 6).

### Writing the copy

- **Write in the language, don't translate the English.** Start from the block's job and the audience's words in that market (store reviews in that language are the best source: customer words). Then check the meaning against the source.
- **The hook stays a hook.** The same feeling, the same mechanism (a question stays a question, a confession stays first person), the same short length. The line checks of `lyra-video-hooks`: one idea, simple, specific, true, natural said aloud.
- **Formal or informal "you".** Decide per market and keep it across every image, card and the ad copy: German du / Sie, French tu / vous, Spanish tú / usted, Portuguese você / tu, Russian ты / вы, Japanese register, Korean speech level. Default: the informal form for consumer apps unless the Brand Kit's tone says otherwise; write the choice in the sheet.
- **Same claims, same strength.** A translation never makes a claim stronger ("helps you sleep" never becomes "cures insomnia"); health, money and result words are checked against that market's approved claims.
- **Numbers, dates, prices, units in the local format:** decimal comma (1,99 €) or point ($1.99), currency symbol position, 24-hour time ("2 Uhr", "2h"), date order, metric units. Prices and offers come from the Brand Kit per market, never converted by Claude.
- **Local punctuation and typography:** French spaces before ! ? : ; and « guillemets » · German „quotes“ · Russian «ёлочки» · Spanish ¿ ¡ · Japanese and Chinese full-width punctuation 。、「」 · no italics or uppercase for CJK · Turkish dotted İ / dotless ı in capitals ("İNDİR", not "INDIR") · German nouns capitalised, ß kept in lower case (or SS in caps) · Greek drops accents in all caps.
- **Line breaks are part of the copy.** Write where the line breaks in the sheet ("2 Uhr nachts. / Kopf ist an."); never break a word, a number from its unit, or a particle from its word (French "!" never alone on a line; Japanese breaks at phrase boundaries).
- **Length guide** (against English, directional): German, Dutch, Finnish, Russian, Ukrainian, Polish, Greek often **+20 to 35%** (German and Finnish long compounds can break a narrow zone) · French, Spanish, Italian, Portuguese, Romanian **+15 to 30%** · Japanese, Chinese, Korean **fewer characters** but each glyph needs more height: keep the same size feel, don't shrink · Arabic, Hebrew, Farsi, Urdu about the same length, **right to left** · Thai no spaces between words (line breaks need a native speaker) · Hindi, Bengali, Marathi, Punjabi, Tamil, Telugu: complex scripts with stacked forms, the riskiest for image models. Short lines grow the most: a 2-word CTA can double.

---

## Fit, scripts and direction

**Fonts per script.** The source's type style may not exist in the target script (many display fonts have no Cyrillic, Greek, Vietnamese, Arabic or CJK). In Routes B and C describe the style **for that script**: "a heavy rounded sans-serif, Cyrillic", "a bold Japanese gothic (sans-serif) typeface", "a bold modern Arabic sans-serif, right-aligned". If the Brand Kit has a font per script, name it (the model may not match it exactly: say so once). Check the result for mixed fonts (one word in another style) and missing diacritics (ä ö ü ß, é è à ç, ą ę ł ś ż, ă ș ț, đ ơ ư and Vietnamese tone marks, ё й).

**RTL (Arabic, Hebrew, Farsi, Urdu).**
- The text reads right to left and is right-aligned; numbers and Latin brand names stay left to right inside the line.
- The **reading order of the layout** flips when it carries meaning: chat bubbles (the user's bubble moves to the left, the app's to the right), arrows and "→ swipe" cues, progress counters, a CTA corner, before / after (before on the right). A photo with a headline usually doesn't need mirroring; a layout with an order does (Route C, the layout map mirrored in words). Never mirror a photo with text, a logo, a phone or a face (it looks wrong).
- Check every RTL output with a native reader: models often reverse letter order, break the joins between Arabic letters, or put the punctuation on the wrong side.

**CJK (Japanese, Chinese, Korean).** Fewer characters, so lines get short and the zone can look empty: keep the size feel and the zone, not the line count. Vertical text only if the source is vertical. Simplified vs Traditional Chinese are different scripts and audiences (`zh-CN` mainland and Singapore, `zh-TW` Taiwan; Hong Kong uses Traditional with Cantonese wording). Japanese mixes kanji, kana and Latin: the app name often stays in Latin or uses the app's own katakana name.

**Complex Indic scripts and Thai.** Highest risk of broken letters in generation. Keep the text short, large, on a clean zone; check with a native reader; after one failed fix go to Route D for that block.

**Text over the picture.** A longer line can grow over a face, the phone or the product. The safe zones and clean zones of the base skill (layout map) still hold in every language; if the text no longer fits its clean zone, it's Route C (the zone re-planned), not a smaller font.

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the image is | Graph | Models |
|---|---|---|
| **A static with short text (default)** | approved source (selected result) → **Image Translation node** with the languages of that route (codes from the list), the instruction filled from the Localization sheet when the field is reachable → one output per language → check → misses fixed with a Pro text-replace node per language | nano-banana-2 · nano-banana-pro |
| **A hero ad, a hook or pun headline, exact approved words, or a regional variant** | approved source → **one Pro text-replace node per language** (`match_input_image`, 2K), the source connected as [Image1] | nano-banana-pro |
| **An image with app UI** (phone shot, UI card, in-app proof) | localized screenshots uploaded (one per screen per language) → **one Pro rebuild node per language**: the original prompt with the texts in that language and the localized screenshot connected; the original approved image connected as a scene reference with its job stated ("keep the person, light, framing and layout; not its text or screen") → word-by-word screen check | nano-banana-pro |
| No localized app (the UI exists only in English) | the screen stays in English (it is what the user will see after install), or the screen faces away / is replaced by a non-UI visual; say it in the plan; never translate the UI in the image | nano-banana-pro |
| **RTL with a reading order** (chat, arrows, list, before / after) | Pro rebuild with the layout map mirrored in words, the texts in quotes, right-aligned | nano-banana-pro |
| **Carousel** (N cards) | per card the same route; terms, formality and the counter identical across cards; split pipeline: a localized carousel script per language (the anchors identical, only the quoted texts change) → Text Split → cards, the persona and card 1 of the same language as references | nano-banana-2 / nano-banana-pro |
| **End card or text card for a video** | the end card image through Route B or C; the localized store badge file as a layer in the Video Editor; VO and captions by the video skills | nano-banana-pro · video_composer |
| **Store screenshot set** (App Store / Google Play) | the localized app's screenshots + the caption written in that language, one Pro node per slot (`lyra-ui-motion-video`, Store screenshot sets); never Image Translation | nano-banana-pro |
| **Legal line, disclaimer, price table, long copy** | Pro clean-plate edit ("Remove all text, keep everything else exactly") → the user's designer sets the localized text in Figma | nano-banana-pro |
| **Languages × sizes** | languages first at the master ratio, approved, then each language resized or recomposed (`lyra-image-resize`, base Reference H); count languages × ratios and say the total before running | nano-banana-2 · nano-banana-pro |
| **The picture should change for the market too** | `lyra-audience-variations` (mode B, a Lyra variation per market); this skill writes its texts | as that skill |
| **Many languages, tight budget** | Route A for all in one node → only the misses get a Pro node; Pro rebuild only for UI images | nano-banana-2 → nano-banana-pro |

**Plan example** (base Step 2 table, fictional app Calmly, one static, 4 markets):

| # | Node label | Node · model · key settings | Inputs (role) | Stage |
|---|---|---|---|---|
| 1 | Localization sheet | user text (note) | — | — |
| 2 | Ad C1: 2 am POV · 4:5 (approved, EN) | image · nano-banana-pro (existing) | — | — |
| 3 | Translate C1 · it, nl, pl | image translation · google/nano-banana-2 · languages it, nl, pl | 2 | 1 |
| 4 | C1 · de · 4:5 | image · nano-banana-pro · match_input_image · 2K | 2 ([Image1] source) | 1 |
| 5 | C1 · pt-BR · 4:5 | image · nano-banana-pro · match_input_image · 2K | 2 | 1 |
| 6 | C1 · ar · 4:5 (rebuild, RTL) | image · nano-banana-pro · 4:5 · 2K | 2 (scene reference) | 2 |
| 7 | C1 · de · 9:16 + 1:1 (after approval) | image resize · google/nano-banana-2 | 4 | 3 |

Stages for translation: **1** = the pilot language and Route A (fast) · **2** = the other languages and the rebuilds · **3** = sizes.

**Canvas.** Section "Languages" to the right of the approved ads: the Localization sheet note first, then one row per source image, its language outputs left to right in the order of the sheet. Labels with the code: "C1 · de · 4:5", "Translate C1 · it, nl, pl", "C2 · ja · 4:5 (rebuild, UI ja)". The approved English images are never edited or overwritten.

## Run options (translation)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option:

| Option | Runs | Results | Credits | Time |
|---|---|---|---|---|
| **A. Pilot language (recommended)** | the hardest language of the set (the longest, e.g. `de`, or an RTL one), every image | one language, all images: shows whether the route, fit and fonts work | {x} | ~1 min |
| B. Fast pass | Route A for all its languages in one node + the Pro nodes | every language | {x} | ~1 to 2 min |
| C. Everything | all languages → sizes | languages × ratios | {x} total | ~3 to 5 min |

- Recommend A when there are more than two languages or any RTL / CJK / Indic script: a fix found on the pilot is applied to every language before credits go on them.
- C has no pause to check: a wrong word is resized into every format. Only when the user accepts that.
- Route A charges one generation per language even when only one word was wrong; fixes go to Route B for that one language.

## Prompt rules (translation)

| Node | Write | Avoid |
|---|---|---|
| Localization sheet (text) | route per image and why; the copy table (source, job, chars, target, ratio, back-translation, mode, line breaks); glossary; market facts; ad copy outside the image | prompts meant for the model; untraced prices or claims |
| Image Translation node | the language codes from the list only; the source connected without a role; a label with the image and the codes; the instruction (when the field is reachable): the market variant and formality, the exact approved texts per language and block, the glossary, what stays in English | codes not in the list (`pt-BR`, `es-MX`); several sources into one node; "translate the UI"; a long brief (the node only needs the words and the rules) |
| **Text-replace edit (Pro)** | "Change only the text." → "[Image1] is the approved ad: keep the person, face, pose, the phone, the background, the light, the layout, the colors and the button shape exactly." → each block: its zone, the old text and the new text in quotes, the type style for this script, alignment, color, size feel → "The only text in the image is …" → "Avoid: extra text, mixed fonts, missing accents, changed layout." | re-describing the scene; "translate the text" without the words (the model would write its own); two changes at once (text and light) |
| Rebuild (Pro) | the original prompt word for word with only the quoted texts replaced, the type style for the script, the localized screenshot "exactly as supplied" with its key texts in that language, the original image's job stated if connected | a new layout or scene by accident; the English screenshot |
| Clean plate (Pro) | "Remove all text from [Image1]: the headline, the subline and the button label; keep the button shape, every color, the person, the scene and the layout exactly; leave the text areas as clean, empty background." | removing the logo or the button with the text |

**Pattern: instruction for the Image Translation node (Route A, languages de and pt).**

> Use exactly these texts. de (German, informal du): headline "2 Uhr nachts. / Kopf ist an." on two lines; button "Heute Nacht testen". pt (Brazilian Portuguese, informal você): headline "2 da manhã. / A cabeça não para." on two lines; button "Teste hoje à noite". Keep "Calmly" and the logo as they are. Keep the phone screen unchanged. No other text.

**Pattern: text replace, German (Nano Banana Pro, `match_input_image`).**

> Change only the text. [Image1] is the approved app ad: keep Mia, her face, pose and grey hoodie, the dark bedroom, the phone and its screen, the lamp light, the framing, the colors and the violet button shape exactly. Top 22%, on the dark wall: replace the headline "2 am. Brain won't stop." with "2 Uhr nachts. / Kopf ist an." on two lines, in the same heavy white sans-serif, very large, left-aligned. Bottom: replace the button text "Try it tonight" with "Heute Nacht testen", white, centered on the violet #8B7CF6 button; the button may be slightly wider. The only text in the image is the headline, the button and the phone screen, which stays exactly as it is. Avoid: extra text, English words left over, mixed fonts, missing umlauts, changed layout.

**Pattern: text replace, Arabic headline over a photo (Nano Banana Pro).**

> Change only the text. [Image1] is the approved app ad: keep the woman, her face and pose, the bedroom, the light, the framing and the colors exactly; do not mirror the photo. Top 22%: replace the headline "2 am. Brain won't stop." with the Arabic headline "[approved Arabic text from the Localization sheet]", written right to left and right-aligned, in a bold modern Arabic sans-serif, white, very large, the letters correctly joined. Bottom: replace the button text with "[approved Arabic CTA]", centered. The only text in the image is the headline and the button. Avoid: reversed letters, disconnected Arabic letters, Latin text, extra text.

(The bracketed parts are filled from the sheet before the node is built: no placeholders in a final prompt, base rule.)

**The 6 rules that matter most here:** (1) words first: the Localization sheet approved before any run; (2) transcreate the hook, translate the labels, keep the glossary; (3) the route per image: A for simple and fast, B for exact words, C for UI and layouts with an order, D for legal and long copy; (4) never translate an interface: localized screenshots or no screen; (5) fit by rewriting, never by shrinking; (6) every letter checked in every language, by a native reader where possible, before sizes or uploads.

---

## Truth, markets and brand safety

- The base skill's Truth and disclosure applies in every language. A translation adds no claim, number or offer and never strengthens one.
- **Claims and offers per market.** A claim approved in the US may not be allowed in Germany or Brazil (health, finance, "free", "#1"); a price or trial length can differ by market. Only what the market's Brand Kit or the user approves; no price conversion by Claude.
- The Brand Kit's **forbidden claims are enforced absolutely** in every language, including in words that only become a forbidden claim in translation.
- **Brand safety** (Lyra's System Preamble): no profanity, no political or religious statements, no unsubstantiated health claims, no competitor disparagement; slang and idioms checked for second meanings in that market (a native reader catches what Claude may not).
- **Store wording and badges:** the localized official badge files ("Laden im App Store", "Disponible sur Google Play"), never generated, never translated by a model.
- Local ad rules differ (alcohol, gambling, health, finance, children, and in some countries required language versions or disclaimers): name them once when the category is sensitive; not legal advice, the user's team checks.
- Remind the user once, in the final report, about the platform's AI label for photoreal synthetic people (every language version carries it).

## Deliverable and naming

1. A "Localization sheet" note: routes, the copy table with back-translations, glossary, market facts, the ad copy outside the image.
2. One image per source × language (× ratio, when sizes are made), in Section "Languages"; the source untouched.
3. For the media buyer: which images form one multi-language ad, the default language, the primary text and headline per language.

Names: the source's code + `-{lang}` (the market when it matters): `B4-A:2amBrain-F:Static-PainPOV-C1-4x5-de`, `…-C1-4x5-pt-BR`, `…-C1-4x5-ar`; carousels `…-Card3-4x5-ja`; sizes after the language: `…-C1-9x16-de`. Node labels: "C1 · de · 4:5".

## Meta and TikTok setup notes (for the media buyer)

- **Meta multi-language ads** (language customization): one ad with a default language and versions per language (image, primary text, headline, description, CTA); Meta shows each person the version that matches their language. All versions should share the format, the ratio set and the message; only the language changes. Ads Manager can also auto-translate the **text fields**, never the text **on the image**: that is this skill's job. Check the current setup in Meta's guide (it changes).
- Separate ad sets per country are still common when prices, offers or claims differ by market.
- TikTok: one ad per language, targeted by language or country.
- Test the translated winner against a native-made concept in the bigger markets: a translated winner is a hypothesis there, not a proven ad.

---

## Common mistakes (translation)

| Mistake | Prevention |
|---|---|
| Image Translation run before the words were agreed | Localization sheet first; Route A only where wording is flexible |
| The hook translated word for word, flat and long | Transcreate the hook: same job, same feeling, native words, line checks |
| The app name or feature name translated | Glossary: do-not-translate list; check Route A outputs for it |
| The node instructed to translate the UI, or an English screen left in an ad for a market where the app is localized | Never instruct UI translation; localized app → Route C with localized screenshots; not localized → the node keeps the UI unchanged by default |
| A brand slogan expected to be translated, but the node kept it | The node keeps identity slogans by default; say it explicitly in the instruction if the Brand Kit has a localized slogan |
| `pt` used for Brazil and Portugal alike, `es` for Spain and Mexico | Market per language; regional variants by Route B with exact words |
| Code not in the list sent to the node | Codes from `list_node_configs` only; others by Route B |
| Text shrunk to fit | Rewrite tighter; over ~140% re-plan the zone (Route C) |
| A longer headline grows over the face or the phone | Clean zones of the layout map hold in every language |
| Formal and informal "you" mixed across images or cards | One choice per market, written in the sheet |
| Price converted or offer copied from the US kit | Market facts from the Brand Kit per market |
| Missing accents, mixed fonts, wrong quote marks, "INDIR" in Turkish | Typography rules per language; check every letter |
| Arabic letters disconnected or reversed, bubbles not mirrored | RTL rules; native check; Route C when the layout has an order |
| One wrong word fixed by rerunning the whole translation node | Route B for that language only |
| Sizes made before the language was checked | Languages first, approved, then sizes |
| Translations left stale after the source was regenerated | Rerun them; say it in the report |
| The English image overwritten | Every language is a new node; the source untouched |
| Claude's translation presented as final for a language it can't fully judge | Back-translation in the sheet; native reviewer named or offered |
| Store badge redrawn in the new language | Official localized badge files only |

## Quality gates (translation)

Claude can't open Lyra result links, so after each stage it sends the checklist and asks the user (or the native reviewer) what works and what doesn't. If the user downloads the results and sends them in the chat, Claude can also read every text block itself and compare it with the sheet, letter by letter.
- **Stage 0 (Localization sheet, Claude checks before sending):** every text block of every image inventoried? Market per language decided? Route per image with the reason? Hooks transcreated, labels translated, glossary kept? Back-translation for every line? Length ratios checked, nothing over ~120% without a rewrite? Formality, number, date, currency and punctuation per market? Claims, prices and offers traced to the market's Brand Kit, forbidden claims absent? Codes from the node's list for Route A? UI images on Route C with localized screenshots (or the screen plan)?
- **Stage 1 (pilot language):** every word identical to the sheet, nothing English left (except the glossary)? Accents and special letters right? One font style, the same size feel? Text inside its clean zone, nothing over a face, the phone or the product? Layout, colors and scene unchanged? RTL: right to left, letters joined, order mirrored where planned?
- **Stage 2 (all languages):** the same checks per language; brand and app names untouched; the screens identical to the localized screenshots; the carousel's terms and counters identical across cards; a native reader's yes where available?
- **Stage 3 (sizes and delivery):** nothing cropped, texts re-checked in each ratio; names with language codes; the multi-language set listed for the media buyer; the ad copy per language handed over; AI label reminder given?

Pass = every point that applies holds for every language. Fix only the failing language and block, with its credits.

## After the test

Read each language by its own market's numbers (cost per install, trial, payer; enough results per market before calling it), not against the English average: markets have different CPMs and conversion. A language that underperforms is a hypothesis: the words (try a second transcreation of the hook), the market (the picture may need a local version: `lyra-audience-variations`), or the offer. Save the Localization sheet and the glossary to the project: the next ad in that market starts from the approved terms, formality and tone.
