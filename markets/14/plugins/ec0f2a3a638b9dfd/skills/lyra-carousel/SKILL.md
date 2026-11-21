---
name: lyra-carousel
description: "Use when the user wants a carousel ad for an app, e.g. \"a carousel for my app\", \"5 cards that tell a story\", \"swipe ad\", \"feature carousel\", \"step by step carousel\", \"before / after carousel\", \"photo dump\", \"TikTok photo carousel\", \"split this text into cards\". Builds 2-10 consistent cards in Lyra from one carousel script."
---

# lyra-carousel

Image mini skill. Builds a carousel ad as **one story told in N cards**: a hook card that stops the scroll and makes people swipe, middle cards that each carry one idea, and a last card that closes with the CTA. Every card looks like it belongs to the same set (same person, same world, same palette, same type, same layout grid), and the text reads as one voice from card 1 to card N.

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

The story is written once, as one **carousel script**, and Lyra's **Text Split** node cuts it into one part per card. Each part is a complete card prompt that feeds its card's image node. One script = one source of truth: the user edits the story in one place, reruns the split and the cards follow.

**Base skill first.** Everything not written here follows `lyra-static-image-generation`: the 8 steps, instruction order, app card, plan table and stages, run options with credits, run and report, concept card and layout map, on-image text, realism, styles, models (Reference A), layout library (B), styles (C), realism toolkit (D), persona and consistency (E), edits (F), UI and logo (G), sizes and languages (H), errors (I), de-slop (J), Meta statics (K), Brand Kit (L). This file only adds what is specific to carousels and to the split pipeline. If the two disagree, the user wins, then this file, then the base skill.

**Other skills for their parts.**
- Card 1 is the hook of the carousel: the line checks, awareness levels, hook base and "Final test" of `lyra-video-hooks` apply to its picture and its line.
- A person across the cards: casting, place and the one-story test from `lyra-ugc-video`; the persona image rules from the base skill (Reference E).
- Real app screens on cards (steps, features, proof): UI fidelity from `lyra-ui-motion-video` (screenshots only, exactly as supplied, word by word check).
- A competitor's carousel as the reference: `lyra-copy-competitor-static` analyses it (one JSON per card + card list); this skill builds the new set.
- The same carousel for another segment or market: `lyra-audience-variations` (layers, one-story test); new angles on a winning carousel: `lyra-ad-concept-multiplier`; other sizes: `lyra-image-resize`; other languages: `lyra-image-translation`; the carousel as a video: `lyra-video-ad-generation` or `lyra-ui-motion-video` (the cards become keyframes, the same script split into scenes).

**This is a way of thinking, not a script.** The rules are defaults and good practice; use judgment and say why in one line when you choose differently. Fixed: truth (no invented claims, reviews, numbers, UI or logos), the Brand Kit's facts, UI fidelity, Lyra's technical limits, the Text Split node's rules, and the user's explicit choices.

---

## How to think about a carousel

**What it is.** A swipeable set of 2 to 10 cards (Meta), up to 35 slides (TikTok photo mode), all in one ratio. The feed shows card 1 and a glimpse of card 2; everything else is earned by swipes. So a carousel is a **sequence of promises**: each card pays off the last one and gives a reason to see the next.

**Three jobs, in order.**
1. **Card 1 stops the scroll and opens a loop.** It must work alone (many people see only card 1), and it **teases, not completes**: a question, a number of steps, a "before", a pain moment, an unfinished story. A card 1 that tells the whole message gives no reason to swipe.
2. **Middle cards carry one idea each**: proof, mechanism, one step, one feature, one reason. Two ideas on one card lower the swipe rate.
3. **The last card closes.** It resolves the loop and asks for one action. No new information: it sees only a fraction of the people who saw card 1.

**How many cards.** Default **5** for a story (hook, pain or proof, mechanism, payoff, CTA). **3** when the idea is simple (hook, value, CTA: the "sweet spot" for installs). 6 to 7 for step by step or listicles that need it; past 8, drop off is steep. More cards are never a goal; every card must earn the next swipe.

**Story or showcase.** Decide this first, because it changes the build and the Meta setup:

| | **Story carousel** (default for this skill) | **Showcase carousel** |
|---|---|---|
| What it is | one arc, card order matters (hook → … → CTA) | independent cards, each a complete mini ad (a feature, a persona, a use case) |
| Card 1 | an open loop | the strongest single card |
| Consistency | one person, one world, one voice across cards | one visual system (palette, type, grid); people and scenes may differ |
| Meta setting | **"show best performing cards first" off**, order locked | the auto-ordering may stay on |
| Split | the script is the story | the script is a list of cards |

**Final test for every carousel:** would the right person stop at card 1, feel a reason to swipe, understand one idea per card, and reach the last card knowing what the app does for them and what to do next? And does the whole set look like one carousel at thumbnail size, not five different ads?

---

## Consistent storytelling: the Story Bible

Consistency in a carousel has two layers: **what the viewer sees** and **what the viewer reads**. Both are fixed once, in a Story Bible, before any card is written. The Story Bible lives in a user text node "Story Bible" (a note for the user, connected to nothing) and its anchors are **copied word for word into every card** of the script.

| Anchor | What is fixed | Example (fictional app Calmly) |
|---|---|---|
| **Narrator and voice** | who speaks (I / you / the app / a friend), tense, tone, word budget per card | first person, Mia speaking, present tense, short and honest, ≤ 12 words per card |
| **Character** | the character card from the base skill (Reference E): age, face, hair, skin, outfit, accessories | "Mia · 21 · student · light brown skin, freckles, dark curly hair in a loose bun · no makeup, slight dark circles · oversized grey hoodie, thin silver hoops" |
| **World** | the place, its 2 to 3 lived-in details, the time of day and its progression | her small dorm room: grey duvet, string lights, a charger cable on the nightstand; night at card 1, morning at card 5 |
| **Camera and light** | phone-real or camera-real, lens feel, the main light source and how it changes with time | phone-real, 24mm, deep focus; bedside lamp + phone glow at night, soft window daylight in the morning |
| **Palette** | hex codes from the design sources (the client's images and screenshots → Brand Kit → the option the client picked), each with its role and source | navy #1B1F3B backgrounds and text bands, violet #8B7CF6 accents and CTA, cream #F4F1EA type |
| **Type system** | headline style, body style, size feel, case, color, position; from the client's references, screenshots or the kit's fonts | headline: heavy rounded sans, cream, very large, left-aligned in the top band; body: regular rounded sans, small |
| **Layout grid** | the same zones on every card, at the same shares of the frame | top 22% text band · middle 63% scene · bottom 15% footer with the progress counter (the CTA button only on the last card) |
| **Continuity devices** | what tells the eye "this goes on" | a progress counter "1/5" bottom-left, a small arrow "→" bottom-right on cards 1 to 4, the string lights running across every card |
| **Device** | the phone and how the screen appears | a generic modern phone in a navy case, screen front-facing, the user's screenshots exactly as supplied |

**Rules for the anchors.**
- **Images over words.** The character comes from a persona image connected as a reference to every card with the person; the look of the set can come from the approved card 1, connected to cards 2 to N as a style reference with its job stated ("[Image2] is a style reference only: copy its palette, type style, light, grain and frame; not its text, not its pose"). Words alone never guarantee the same face.
- **Word for word.** The anchor lines are pasted identically into every card of the script, never paraphrased. Claude checks this with a diff before building.
- **What may change, card to card, is planned.** Time of day, the expression, the action, the camera distance, the screen shown: write it in the card ("allowed to change") so the change reads as story, not as drift.
- **One voice.** The narrator and the tense stay the same; a carousel that starts with "I" and ends with "Your…" breaks the story unless the switch is the payoff.

**Story devices that make people swipe:**
- **Open loop:** card 1 asks or shows something unfinished; the answer arrives later (never left open).
- **Numbered promise:** "3 things…", "5 steps…" with a counter; people swipe to finish the list.
- **Time arc:** 2 am → 7 am, day 1 → day 7, before → after, the change visible on the same person in the same place.
- **Cliffhanger per card:** each card ends on a small question the next one answers ("So I tried one thing." → next card).
- **Continuity across the edge:** a shape, a line or an object that runs off the right edge of a card and continues on the next (a string of lights, a desk, a road). It invites the swipe; build it with the panorama option (Best way to build it) or keep it to a simple band that repeats.
- **Payoff:** the last card closes the loop with the app as the reason, and the CTA.

---

## Story arcs for app carousels

A reference, not a menu. Each arc with its card roles (5 cards unless stated) and when it fits. The concept picks one and adapts it.

| Arc | Cards | Works for | Notes |
|---|---|---|---|
| **Hook → proof → mechanism → stack → CTA** (default) | 1 hook (claim or outcome, ≤ 8 words) · 2 proof (a real screen, a result) · 3 how it works (the feature) · 4 a second proof or three variants to pick from · 5 CTA with a fallback line (offer from the kit) | most apps, cold traffic | the proof is a real screen or a real number from the kit, never a fake review |
| **Problem → agitate → solution → result → CTA** | 1 the pain moment on the person · 2 why it keeps happening · 3 the app as the fix (real screen) · 4 the change, same person, same place · 5 CTA | problem aware audiences | the agitate card never shames the viewer |
| **POV story / time arc** | 1 "POV: 2 am, brain won't stop" · 2 what she tried · 3 she opens the app (real screen) · 4 the next morning · 5 CTA | sleep, habits, wellbeing, learning | one person, one place, time moves; strongest consistency test |
| **Step by step** (Nubank pattern) | 1 "Your card in 5 steps" · 2 to 5 one step each on a real screen, numbered · last CTA | fintech, onboarding-heavy apps, anything that feels hard to start | shows the process before the click; lowers the trust barrier |
| **Feature walkthrough / use cases** (Notion pattern) | 1 a pain or outcome hook (not a logo header) · 2 to 4 one use case each on a real screen · 5 "Start free" | multi-feature apps | every middle card can stand alone; replace a branded header card 1 with a real hook |
| **Problem / solution stack** (Linear pattern) | 1 headline · 2 to 3 pain vs fix side by side, same frame · 4 offer | apps replacing a habit or an old tool | never name or mock a competitor (brand safety) |
| **Before / after** | 1 before (the situation, not a body) · 2 to 3 the change · 4 after · 5 CTA | organising, finance, learning, home, productivity | no body before/after for health or weight-loss apps |
| **Listicle / reasons why** | 1 "3 reasons nurses switched…" · 2 to 4 one reason each · 5 CTA | feature-rich apps, considered decisions | reasons from the kit's features and approved claims only |
| **Myth vs fact** | 1 the myth · 2 why people believe it · 3 the fact (from the kit) · 4 what the app does about it · 5 CTA | education, health habits, finance | the fact is a real, approved claim, or a common-sense one |
| **Persona gallery** (showcase) | 1 "Who it's for" · 2 to 4 one segment each with its use · 5 CTA | apps with several clear segments | showcase: auto-ordering can stay on |
| **Photo dump / UGC deck** | 4 to 7 phone-real photos of one person's day, short captions in their voice, the app in one or two of them, CTA last | Gen Z, lifestyle, habits; TikTok photo mode | looks like a real person's post; never presented as a real user |
| **Chat story** | 1 the first message (the pain in the user's words) · 2 to 4 the conversation · 5 the answer and the CTA | coaching, learning, AI companions | stylised generic bubbles; a fictional chat is never shown as real |
| **Comic / illustrated story** | 4 to 6 panels with one character in the brand's style | brands with a mascot, kids and family, casual apps | the brand's own mascot or an original character, described fully |

---

## The split pipeline: one script → Text Split → cards

### What the Text Split node does

Lyra's **Text Split** node (action `text_split`, model `openai/gpt-5-structured`) receives a text and returns it as an array of parts. Its own system prompt, word for word in effect:
1. It must split into multiple parts, never one.
2. It splits at every major structural boundary: headings ("##"), scene breaks, chapter markers, dividers ("---").
3. Each part is a complete section; it never splits mid-sentence or mid-paragraph.
4. It **drops the dividers** ("---"); they are separators, not content.
5. It **copies the text exactly** into each part: no rewriting, summarising or adding.
6. At least 2 parts.
7. **A target part count written before the text** makes it aim for about that many parts, still respecting the boundaries.

Two consequences shape everything below: **whatever sits between two dividers becomes one card's prompt, exactly as written**, and **anything before the first card becomes its own part** (and shifts every card by one).

### Writing the carousel script for the splitter

The script is a user text node "Carousel script", written by Claude, connected to the Text Split node.

1. **The target count goes in the Text Split node, not in the script.** Rule 7 reads a count "provided before the text": when the canvas node has a field for it (a part count or a prompt), set it to N there. Don't write "Target: 5 parts" as the first line of the script: the splitter copies text exactly, so the line can end up inside card 1 and be printed on the image. The dividers already make N parts.
2. **The script is the cards only.** No title, no intro, no Story Bible section, no notes: they would become parts. The Story Bible lives in its own note node.
3. **Cards separated by a line with only `---`.** N cards = N − 1 dividers. No `---` and no `##` anywhere inside a card.
4. **No markdown headings on the cards.** A heading is copied into the part and the image model may print it ("Card 1", "Hook"). Each card starts with its format line instead: `Static app ad, carousel card 1 of 5, vertical 4:5, …`.
5. **Every card is a complete, self-contained image prompt** (base Prompt rules, static ad): format and ratio in words → each reference's job → the **anchor lines word for word** (character, world, camera and light, palette, type system, layout grid, continuity devices) → this card's role, moment and allowed changes → the layout top to bottom with every text in quotes → the screen "exactly as supplied" + its key texts, if any → "The only text in the image is …" → a short "Avoid …" line. 100 to 220 words per card.
6. **References are named the same way in every card** ([Image1] = the persona, [Image2] = the style reference, [Image3] = the screenshot of this card), and each card's image node gets the same inputs in the same order, so the names stay true.
7. **One paragraph per card** where possible (the splitter never cuts inside a paragraph; one paragraph per card makes a wrong cut impossible).

**Pattern: carousel script (fictional app Calmly, POV time arc, 5 cards; cards 2 to 4 shortened here with […] for space, written in full in a real script).**

```
Static app ad, carousel card 1 of 5, vertical 4:5, UGC phone-photo style. [Image1] is Mia: use her face, curly hair in a loose bun and grey hoodie exactly. Mia, 21, light brown skin, freckles, dark curly hair in a loose bun, no makeup, slight dark circles, oversized grey hoodie, thin silver hoops. Her small dorm room at night: rumpled grey duvet, warm string lights along the wall, a charger cable on the nightstand. Shot on a 24mm phone camera, deep focus, warm bedside lamp from the right, cool phone glow on her face, natural skin texture, visible pores. Moment: 2 am, she lies on her side wide awake, staring at the ceiling, phone face down on the duvet. Layout from top to bottom: top 22%: a navy #1B1F3B band with the headline "2 am. Brain won't stop." in a heavy rounded sans-serif, cream #F4F1EA, very large, left-aligned · middle 63%: Mia in bed, the string lights running off the right edge of the frame · bottom 15%: navy band, small cream counter "1/5" bottom-left and a small violet #8B7CF6 arrow "→" bottom-right. The only text in the image is the headline, "1/5" and the arrow. Avoid: beauty filter, studio lighting, extra text, logos.
---
Static app ad, carousel card 2 of 5, vertical 4:5, UGC phone-photo style. [Image1] is Mia: […same anchor lines word for word…] Moment: 2:40 am, she scrolls her phone in bed, eyes tired, the room the same. Layout from top to bottom: top 22%: navy band, headline "Scrolling made it worse." […] bottom 15%: counter "2/5", arrow "→". The only text in the image is the headline, "2/5" and the arrow. Avoid: […]
---
Static app ad, carousel card 3 of 5, […] [Image3] is the app screen. Moment: she opens the wind-down timer; the phone faces us, the screen displays [Image3] exactly as supplied […] visible on screen: "Tonight's plan", "5 min", "Start". Headline "So I tried 5 minutes of this." […] counter "3/5" […]
---
Static app ad, carousel card 4 of 5, […] Moment: 7 am, soft window daylight from the left, the lamp off, she stretches in bed, rested, a small smile. Headline "Asleep before the timer ended." […] counter "4/5" […]
---
Static app ad, carousel card 5 of 5, […] Moment: morning, she holds the phone toward us with the timer screen [Image3]. Layout: top 22%: headline "Your 5-minute wind-down." · middle: Mia and the phone · bottom 15%: a wide rounded violet #8B7CF6 button "Try it tonight" with cream text, centered, counter "5/5" small bottom-left, no arrow. The only text in the image is the headline, the button, "5/5" and the phone screen. Avoid: […]
```

**Check before building (Claude, Stage 0):** the script starts directly with card 1; count the dividers (N − 1); no `##`, no title, no notes in the script; the anchor lines identical in every card (diff them); every card ends with "The only text in the image is …"; every quoted text matches the concept; total length of each card 100 to 220 words.

### Connecting it in Lyra

`Carousel script` (user text) → `Text Split` (`text_split`, `openai/gpt-5-structured`) → `Card 1` … `Card N` (Image Generation, Nano Banana Pro). The persona, the style reference and the uploads (screenshots, logo) connect to the cards that use them, in the same order on every card.

**What the MCP tools can and can't do (Oct 2026).** `list_node_configs` lists `text_split` with `openai/gpt-5-structured` as its preferred model, but there is **no create tool for it** (as with Creative Analysis). So:
1. `get_workflow`: a Text Split node already on the canvas (the user added it, or a template has it) → `update_node` its model and settings if needed, `connect_nodes` script → split → cards, read its price next to Run.
2. No Text Split node → ask the user once to add one from Lyra's node menu (one click on the canvas), then continue. Don't wait in silence: build everything else meanwhile.
3. **How the parts reach the cards must be checked on the first build** (which part goes to which image node, whether a connected text replaces or joins the image node's own prompt). Until the team has confirmed it, every card's image node **also gets its full card prompt in its own prompt field** (the same text as its part), so the carousel runs correctly either way. Write down what the first run shows in the project notes, so the next build skips this check.
4. Connect the split's outputs to the cards **in card order**, left to right on the canvas.

**Two modes, said in the plan:**
- **A. Split driven (recommended once confirmed):** the script is the source; the user edits the story in "Carousel script", reruns the split, reruns the cards. Best for iterating the story, changing N, testing new hook cards.
- **B. Direct (fallback):** the script stays as a note; each card's prompt lives in its image node. Use when no Text Split node is available or the routing isn't confirmed yet.

### The user's own text as the source

The split also turns **text the user already has** into a carousel: a blog post, a video script, a list of features, real reviews from the Brand Kit, a story, a lesson. Claude:
1. reads it and finds the arc in it (the hook, the beats, the payoff), proposes N cards and the arc in plain words;
2. restructures it into cards: the user's own words stay where they are the on-image text (the base rule: the user's words stay as given), shortened only with the user's yes; the anchors and the layout are added around them;
3. writes it as a carousel script (rules above), never feeding the raw text to the splitter: raw text would be cut at its own paragraph breaks and give cards without anchors, layout or the "only text" line.

---

## Step 1 additions: the carousel brief

**Ask first, build later.** Before any concept, Claude asks the client everything only they can give, in one message, and waits for the answers. Nothing about the look is decided before this. Ask for:
1. **The app:** name, store link, what it does, who it's for (or the Brand Kit, which covers it).
2. **The Brand Kit:** which kit (or `list_brand_kits` and confirm the one in the workspace), or the brand basics if there is none: colors (hex), fonts, tone, logo, icon.
3. **App screenshots:** the screens the carousel may show, current version, full resolution (screenshots only, never a screen recording).
4. **Style and design references:** images the client wants it to look like: their own past ads, brand photos, a mood board, a design system, a carousel they like. And in words: what style they want (photo, illustration, typographic, UGC, premium), and what they don't want.
5. **The story or the idea**, if they have one (or their text to turn into cards).
6. **Where it runs:** Meta Feed · Stories · TikTok photo mode; the language.

If the client answers only part of it, ask once more only for what's still missing; never re-ask what they said.

### Design sources: where the look and the colors come from

The look of the carousel (palette, type, style, graphic elements) is taken from what the client gives, in this order:

| Order | Source | What we take from it |
|---|---|---|
| 1 | **The client's words in this chat** | any explicit choice (a color, a style, "no illustrations") wins over everything below |
| 2 | **Reference images the client sent** (their own ads, brand photos, mood board, design system) | style, palette, type feel, composition, graphic elements, polish level |
| 3 | **The app's screenshots** | the app's real palette, type style, corner radius, icon and button style, so the cards match the app people will open |
| 4 | **The Brand Kit** | hex colors, fonts, tone, logo, icon; also fills everything the images don't show |
| 5 | **Nothing sent** | Claude proposes **2 to 3 style and palette options** that fit the audience and the category, one recommended; the client picks; never decided silently |

**How to read the images.**
- Claude looks at every reference and screenshot itself (attached in the chat or staged from a connected folder). Files that exist only inside Lyra can't be seen by Claude: ask the client to also send them in the chat, or work from the Brand Kit for that part.
- **Colors as hex from the pixels**, not by eye: a short script (downscale, k-means with 3 to 5 clusters, sort by pixel count, drop near duplicates), 2 to 4 colors with their role (background, text, accent, CTA).
- **Type:** describe the style (heavy geometric sans, rounded, serif, handwritten), weight, case; the font name only from the Brand Kit.
- **Style:** name it in the base skill's words (phone-real, lifestyle, typographic, flat vector, 3D…) and write what makes it that style.
- Write the result into the Story Bible (palette, type, style, layout grid) with its source next to each line ("violet #8B7CF6, source: Brand Kit; card background #F4F1EA, source: screenshot 2").

**Conflicts.** The images and the Brand Kit disagree (the app's UI is blue, the kit's main color is violet) → say it in one line and ask which wins. Default if the client doesn't care: brand colors from the kit for backgrounds, type and CTA; the screens exactly as they are.

**Whose images can feed generation.** The client's own images (their ads, their photos, their design system) may be connected to the card nodes as a **style reference with its job stated** ("[Image4] is a style reference only: copy its palette, light, type feel and grain; not its people, objects or text"). A competitor's or a third-party image is **analysis only**: never connected to generation (see `lyra-copy-competitor-static`). Unknown source → treat it as third-party and ask.

**Defaults (state, don't ask; only what the client didn't answer):** a **story carousel** · **5 cards** (3 when the idea is simple) · **4:5** (1080×1350) for Meta Feed, the same ratio on every card; **9:16** (1080×1920) for Stories and TikTok photo mode; 1:1 only when asked · English · style and palette from the design sources above (phone-real photo only when nothing points elsewhere and the client picked it from the options) · **Nano Banana Pro**, 2K (4K for a card with a readable screen or small text) · count 1 per card (2 for card 1 and the persona) · one persona connected to every card with the person · card 1 approved first, then connected as a style reference to the other cards · split driven when a Text Split node is available, direct otherwise · progress counter on, CTA only on the last card.

**Recommended first run:** A. Anchor first (Run options below).

## Step 2 addition: the carousel concept

Part of the concept the user approves, readable in a minute:
1. **Concept card** (base format) for the whole set: hypothesis in one line (why this story should work for this audience), the arc, story or showcase, N, ratio, style, palette.
2. **Story Bible** in short: narrator and voice, character card, world and time arc, camera and light, palette, type, layout grid, continuity devices.
3. **Card list**, one line per card: # · role · moment (what we see) · on-image text in quotes (with its word count) · screen, if any · what changes from the previous card.
   > 1 · hook · Mia awake at 2 am, phone face down · "2 am. Brain won't stop." (5) · — · —
   > 2 · pain · 2:40 am, scrolling, tired · "Scrolling made it worse." (4) · — · phone up, later time
   > 3 · fix · opens the wind-down timer · "So I tried 5 minutes of this." (7) · timer screen · the screen appears
   > 4 · result · 7 am, daylight, rested · "Asleep before the timer ended." (5) · — · morning light, smile
   > 5 · CTA · holds the timer to camera · "Your 5-minute wind-down." + button "Try it tonight" (4 + 3) · timer screen · button appears
4. **The swipe test**, one line: what makes people go from card 1 to card 2 (the open loop), and how the last card closes it.
5. **The plan table** (base Step 2) and the model question.

The full carousel script is written after approval, at build time (Step 4), from this card list. Card 1 gets the most care: it is the hook, the thumbnail and the only card many people see.

**Text budget per card:** card 1 headline ≤ 8 words (it's a hook: one idea, the audience's words); middle cards ≤ 12 words in total; the last card a headline + a CTA of 1 to 4 words; at most 2 text blocks per card besides the counter. The ad's primary text (outside the image, ~125 characters before "more") and the per-card headline field (≤ ~40 characters) are written too, in the concept, and handed to the media buyer.

---

## Best way to build it

The user's explicit choices override any row. Models and prices: base Reference A.

| If the carousel has | Graph | Models |
|---|---|---|
| **A person across the cards (default story)** | Story Bible (note) · Carousel script → Text Split → Card 1 … N · persona node first (count 2, the user picks) connected as reference to every card with the person · card 1 run and approved first, then connected to cards 2 to N as a style reference | nano-banana-pro |
| No person (typographic, product, illustrated) | the same, without the persona; card 1 is the style anchor for the others | nano-banana-pro (Ideogram 3.0 Quality as a test for type-only cards that keep failing) |
| The client's own style references (their ads, photos, design system) | upload them (`list_uploads` first) → connect as a style reference to every card, job stated first; palette and type from them written into the anchors | nano-banana-pro |
| Real app screens (steps, features, proof) | one screenshot upload per screen card, connected only to its card; the screen "exactly as supplied" + key texts in the card; a separate phone-shot node when a screen keeps failing (base Reference G) | nano-banana-pro, 4K for screen cards |
| Showcase (independent cards) | the same graph; the visual system (palette, type, grid) as anchors, people and scenes may differ; no style reference from card 1 when the scenes must differ | nano-banana-pro |
| A continuous scene across cards (panorama) | **option 1 (safer):** a repeating band or object at the same height on every card, so the cards line up when swiped · **option 2:** one wide image (21:9) of the whole scene, cut into cards by the user's designer in Figma (Claude can't open Lyra results to cut them) · **option 3 (risky):** each next card with the previous card connected as reference, "continue the scene from the right edge of [Image2]"; check the seams | nano-banana-pro |
| The user's own text (article, script, reviews) | Claude restructures it into a carousel script → Text Split → cards | nano-banana-pro |
| A competitor's carousel as the reference | `lyra-copy-competitor-static` teardown (one JSON per card, card list) → the arc and roles kept, our story and look → this skill's build | nano-banana-pro |
| 9:16 for Stories / TikTok | a separate set at 9:16, **recomposed** card by card (keep top ~14% and bottom ~20% free), never cropped from 4:5 | nano-banana-pro (or `lyra-image-resize` for simple layouts) |
| Many directions / tight budget | drafts of card 1 only on nano-banana-2 at 1K, count 2 to 3 → the user picks the direction → the full set on Pro | nano-banana-2 → nano-banana-pro |
| A video version of the carousel | the approved cards as keyframes, the same script split into scenes → `lyra-video-ad-generation` (people) or `lyra-ui-motion-video` (UI-led) | seedance-2.5 / 2.0 |

**Plan example** (base Step 2 table, Calmly, POV time arc, 5 cards):

| # | Node label | Node · model · key settings | Inputs (role) | Stage |
|---|---|---|---|---|
| 1 | Concept card + card list | user text (note) | — | — |
| 2 | Story Bible | user text (note) | — | — |
| 3 | Carousel script (5 cards) | user text | — | — |
| 4 | Text Split · 5 parts | text · text_split · openai/gpt-5-structured | 3 | 1 |
| 5 | Persona: Mia | image · nano-banana-pro · 4:5 · 2K · count 2 | — | 1 |
| 6 | Screenshot: timer | upload image | — | 1 |
| 7 | Card 1: hook · 2 am · 4:5 | image · nano-banana-pro · 4:5 · 2K · count 2 | 4 (part 1), 5 (person) | 2 |
| 8 | Card 2: pain · scrolling · 4:5 | image · nano-banana-pro · 4:5 · 2K | 4 (part 2), 5, 7 (style) | 3 |
| 9 | Card 3: fix · timer · 4:5 | image · nano-banana-pro · 4:5 · 4K | 4 (part 3), 5, 7, 6 (screen) | 3 |
| 10 | Card 4: result · morning · 4:5 | image · nano-banana-pro · 4:5 · 2K | 4 (part 4), 5, 7 | 3 |
| 11 | Card 5: CTA · 4:5 | image · nano-banana-pro · 4:5 · 4K | 4 (part 5), 5, 7, 6 | 3 |

Stages for a carousel: **1** = sources (split, persona, uploads) · **2** = card 1, the anchor · **3** = cards 2 to N · **4** = sizes, languages, variants.

**Canvas layout.** Section "Story" (concept card, Story Bible, Carousel script, Text Split) → Section "Sources" (persona, uploads next to the cards they feed) → Section "Cards" with the cards **in one row, left to right in card order**, so the user reads the carousel on the canvas like the feed shows it → Section "Sizes and languages". Labels: "Card 3: fix · timer · 4:5", never "Image 3".

## Run options (carousel)

**Run order, not a menu** (base Step 6): after the user's yes, run all of it in this order without offering options. Stop between stages (the look first, then the rest) only when the user asked for it, or when the plan is expensive and that was said in the approval message.

As in the base skill, credits read from the nodes, per option:

| Option | Runs | Results | Credits | Time |
|---|---|---|---|---|
| **A. Anchor first (recommended)** | Text Split + persona + card 1 (count 2) | the parts, 2 personas, 2 hook cards: the user picks the person and the look | {x} | ~1 to 2 min |
| B. Whole set | split → persona → all cards (count 1) | N cards | {x} | ~3 to 5 min |
| C. Drafts of card 1 | card 1 on nano-banana-2, 1K, count 3 | 3 directions for the hook card | {x} | ~30 s |

- Recommend A: the person and the look of card 1 decide the whole set; spending on cards 2 to N before they are right wastes credits.
- After A, the next pick is "cards 2 to N", with its credits, once the user has selected the persona and card 1 in Lyra (the references use the selected result).
- B has no pause to pick: keep count 1 everywhere; the style reference then comes from card 1's only result.

---

## Prompt rules (carousel)

| Node | Write | Avoid |
|---|---|---|
| Concept card (text) | the base concept card for the set + arc, story or showcase, N, the card list, the swipe test, primary text and per-card headlines | prompts meant for the model |
| Story Bible (text, note) | narrator and voice, character card, world and time arc, camera and light, palette (hex), type, layout grid, continuity devices, device | anything only in words that must be identical in images (that's what the persona and style references are for) |
| Carousel script (text → split) | N complete card prompts separated by `---`, anchors word for word in each, one paragraph per card | a title, an intro, notes, `##` headings, `---` inside a card, "same as card 1", references to the chat |
| Text Split | its own model and system prompt; the target count N in its own field, when the node has one | rewriting its rules; the count written inside the script |
| Card (image) | format line "carousel card k of N" → each reference's job → anchors word for word → this card's moment and allowed changes → layout top to bottom with every text in quotes → screen exactly as supplied → "The only text in the image is …" → "Avoid …" | a different palette, type, grid or narrator; "like the previous card"; more than one idea; a CTA button before the last card (unless showcase) |
| Persona (image) | base persona rules (Reference E), in the story's world, no text | a model look, a real person or lookalike |
| Edit of one card | base edit pattern: verb first, keep list, one change | regenerating the whole set for one card's fix |

**The 6 rules that matter most here:** (1) card 1 works alone and opens a loop; (2) one idea per card, the last card closes with one CTA; (3) the Story Bible's anchors word for word in every card, and the persona (and card 1) connected as references; (4) the script is cards only, separated by `---`, each a complete prompt; (5) the same layout grid and type on every card, counter and arrow as continuity; (6) every letter and every screen checked with the user, card by card, before anything is built on them.

---

## Truth and brand safety

The base skill's Truth and disclosure applies to every card. In addition:
- **Steps and features only as the app really works.** A step-by-step carousel shows the real order of the real screens; never a step the app doesn't have, never a screen redrawn.
- **The story is a creative scene.** Mia is an AI persona, never presented as a real user; a photo dump or a chat story never claims to be a real person's post or conversation.
- **Results and time claims** ("asleep before the timer ended", "fluent in 30 days") only when they are an honest, ordinary description of the scene and don't read as a promised result, or when the Brand Kit approves the claim. When in doubt, move the line to a feeling ("finally calm") rather than a result.
- **Comparisons** (problem / solution stack, old way vs app) never name, show or mock a competitor; no competitor UI.
- The Brand Kit's **forbidden claims are enforced absolutely** on every card, in the primary text and in the per-card headlines.
- Remind the user once, in the final report, about the platform's AI label for photoreal synthetic people.

## Deliverable and naming

1. Section "Story": concept card with the card list, Story Bible, Carousel script, Text Split.
2. Sources: persona, uploads. Cards in one row, in order. Sizes and languages.
3. The ad copy for the media buyer: primary text, per-card headlines, the CTA button, "order locked" (story) or "auto-order allowed" (showcase).

Names: `B{batch}-A:{angle}-F:Carousel-{arc}-C{concept}-Card{n}-{ratio}` (+ `-{lang}`, `-V{n}{what changed}`), e.g. `B6-A:2amBrain-F:Carousel-POV-C1-Card3-4x5`. The whole set shares the code up to `Card{n}`, so the media buyer uploads it as one carousel.

## Meta and TikTok setup notes (for the media buyer)

- Meta: 2 to 10 cards, all one ratio; 4:5 (1080×1350) or 1:1 (1080×1080) for Feed, 9:16 (1080×1920) for Stories with ~250 px clear at the top and bottom. Primary text truncates around 125 characters on Instagram, ~80 on Facebook; card headline ~40 characters; description ~18 to 30 characters (Facebook only). Keep key text inside the central 80%.
- **Story carousels: turn off "automatically show the best performing cards first"**, so the order stays. Showcase carousels can keep it on.
- The same CTA button on every card; vary the per-card headline so each card gives a reason.
- TikTok photo mode: up to 35 slides, 5 to 7 is the usual sweet spot, 9:16.
- Specs change: check Meta's and TikTok's current guides before export.

---

## Common mistakes (carousel)

| Mistake | Prevention |
|---|---|
| Card 1 tells the whole story, nobody swipes | Card 1 teases (question, steps, before, pain); the payoff comes later |
| Card 1 is a logo or a branded header | A real hook in the audience's words, with the `lyra-video-hooks` line checks |
| Two ideas on one card | One idea per card; the second idea is the next card |
| New information or a second offer on the last card | The last card closes the loop and asks for one action |
| Face, outfit or room changes between cards | Persona connected to every card; anchors word for word; card 1 as style reference |
| Palette, type or layout grid drift | The same anchor lines in every card; diff before building |
| Story Bible or a title placed in the script, the split shifts every card by one | Script = cards only; the Bible lives in its own note |
| `##` headings in the script, "Card 1" printed on the image | No headings; each card starts with its format line; "the only text is…" |
| A `---` inside a card, or a missing one | Count dividers = N − 1; one paragraph per card |
| Raw user text fed straight into the split | Restructure it into card prompts with anchors and layout first |
| Claims the split routing works before it was checked | Prompts also in each card node until the first build confirms it |
| A CTA button on every card of a story | Counter and arrow on cards 1 to N−1; the button only on the last card |
| 4:5 cards cropped to 9:16 | Recompose each card for 9:16 |
| Steps or screens the app doesn't have | Real screens only, in the real order |
| Concept written before asking for the kit, screenshots and style | Ask first (Step 1), one message, wait for the answers |
| Colors guessed by eye or picked by Claude while the client sent images | Design sources in order; hex measured from the pixels; source written next to each color |
| A style chosen silently when nothing was sent | 2 to 3 options, the client picks |
| A competitor's or unknown image connected as a style reference | Only the client's own images feed generation; others are analysis only |
| Auto card ordering left on for a story | Tell the media buyer: order locked |
| Ten cards "because Meta allows it" | 3 to 5 for installs; every card must earn the next swipe |

## Quality gates (carousel)

Claude can't see the results, so after each stage it sends the stage checklist and asks the user what works and what doesn't.
- **Stage 0 (concept and script, Claude checks before sending and before building):** the client was asked for the Brand Kit, screenshots, style references and the story before the concept? Palette, type and style traced to a design source (client's images, screenshots, kit, or an option the client picked), hex measured from pixels? Only the client's own images connected as style references? Arc named, story or showcase decided, N justified? Card 1 standalone, teasing, ≤ 8 words, passes the hook line checks? One idea per card? The last card closes the loop, one CTA, no new info? Text budgets kept? Every claim, number, offer and screen traced to the Brand Kit or the user? Script: cards only, target N set on the split node if it has the field, N − 1 dividers, no headings, anchors identical (diff), each card a complete prompt ending with "The only text in the image is …"?
- **Stage 1 (split, persona, uploads):** the split returned exactly N parts? Each part starts with its format line "carousel card k of N" and is complete (nothing cut, nothing merged)? Persona: a real-looking person in the story's world? Screens identical to the screenshots?
- **Stage 2 (card 1):** stops the scroll at phone size? Makes you want card 2? Every letter right? The look is the one the whole set should have?
- **Stage 3 (cards 2 to N), seen side by side in one row:** same person, outfit, room (except the planned changes)? Same palette, type, grid, counter and arrow on every card? The story reads when swiping, one idea per card, the time arc visible? Every letter, number and screen right? The last card's CTA clear and inside the safe zone? Looks like one carousel at thumbnail size?
- **Stage 4 (sizes, languages, variants):** 9:16 recomposed, nothing cut; texts re-checked in every language; variants change only the intended card or layer; names with codes; AI label reminder given.

## After the test

Read the carousel by the goal's cost per result (trial, payer), not CTR alone, and by its card-level drop off when the platform shows it: a big drop after card 1 → the hook card; after card 2 → the proof is weak; people swipe to the end but don't install → the last card or the offer. Refresh by **replacing the weakest card** (often every 10 to 14 days), not the whole set. Then offer 2 to 4 next steps, each with what changes, what stays and its credits:
- **Hook card test:** 2 to 3 new card 1s, cards 2 to N held constant (only the first part of the script changes; rerun split and card 1).
- **Audience version:** the same story for another segment from the kit (`lyra-audience-variations`: persona, wardrobe, world; the one-story test).
- **New angle:** the same arc with another reason to care (`lyra-ad-concept-multiplier`).
- **Languages and sizes:** `lyra-image-translation` and `lyra-image-resize` per card (Image Translation only on cards without UI; cards with UI get the localized screenshots and texts written in that language).
- **Video version:** the cards as keyframes, the script split into scenes (`lyra-video-ad-generation`, `lyra-ui-motion-video`).

Variants live next to the original in the same workflow (one row per version) or in a Lyra variation (`create_variation`, the original stays Main as the control). Save the arc, the card list and the result to the project, so the next carousel starts from what the team learned.

---

## Reference: what the research says (Oct 2026)

**Three documented carousels from app and software brands** (from adlibrary.com's 2026 teardowns; all observed running 60+ days, which signals a working ad but is not proof of performance; public libraries don't show reach or results for commercial ads, so "most popular" can't be measured from the outside):
1. **Nubank (fintech app), step by step, 5 cards, Meta, Brazil and Mexico.** Card 1 announces five steps; the next cards walk through download, form, selfie check, card delivery and first purchase as phone screens. Works because it shows the whole process before the click and lowers the trust barrier of a high-commitment product. Our use: the Step by step arc; real screens only; numbered counter.
2. **Notion, feature walkthrough, 5 cards, Instagram, knowledge workers.** Card 1 a branded header; cards 2 to 4 meeting notes, project tracker and wiki as phone-scale screenshots; card 5 "Start free". Works because concrete use cases make an abstract "all-in-one" claim tangible. Our use: the Feature walkthrough arc, but with a real hook on card 1 instead of a logo header.
3. **Linear, problem / solution stack, 4 cards, LinkedIn and Meta.** Card 1 a headline; cards 2 and 3 pain vs fix side by side in the UI; card 4 a 14-day free trial. Works because the contrast is visible in one look. Our use: the Problem / solution arc, without naming any competitor.

**How much apps use carousels** (sprites.ai reads of Meta Ad Library samples, Sept to Oct 2026): Headway 33% carousels in the creatives read (a library of many books fits a swipe), Duolingo 17%, Calm 10%, BetterMe 0% (all video). Carousels are a main format for some subscription apps and absent for others: test, don't assume.

**Benchmarks (third-party, directional):** median swipe from card 1 to card 2 about 62%, card 5 reached by about 22% (adlibrary.com citing Klaviyo); viewers who reach card 3 convert several times more often; a steep drop after card 4; 3 to 5 cards recommended for installs (RocketShip HQ); carousels fatigue at a lower frequency than video, so plan card refreshes. On TikTok, photo carousels reported about 1.8x the engagement of videos but fewer shares (Stack Influence, Dec 2025).

**Structures the sources agree on:** card 1 stands alone and teases · one idea per card · proof as a receipt (a screen, a result), not a testimonial · the last card adds no new info · continuity devices (counters, numbered steps, panoramas, a shared band) signal "more" · lock the order for stories · refresh by swapping the weakest card · vary one card at a time in tests.
