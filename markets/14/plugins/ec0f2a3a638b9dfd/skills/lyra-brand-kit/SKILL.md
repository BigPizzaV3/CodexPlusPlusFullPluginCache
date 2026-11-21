---
name: lyra-brand-kit
description: "Use when the user shares or asks about their app's brand, e.g. \"here's our brand kit\", \"set up my brand in Lyra\", \"create a brand kit from our website / store page / deck\", \"onboard this app\", \"update the brand kit\", \"what's in our brand kit\", \"find the pains in the brand kit\", or before any ad when no Brand Kit exists. Builds and fills the Lyra Brand Kit and holds the rules other Lyra skills use to read it."
---

# lyra-brand-kit

Foundation skill. Two jobs:

**Canvas layout → `lyra-workflow-layout`.** Every workflow this skill builds or changes is laid out by `lyra-workflow-layout`: sections in reading order with a STEP note above each one, the team's color code, clear node labels and the final check. The layout lines in this file only say which sections this creative needs.

1. **Set up a brand.** The user sends whatever they have about the app. Claude turns it into a complete Brand Kit in the team's standard, fills it into Lyra, creates the first workflow, assigns the kit to it and puts the brand's assets on the canvas. The user ends with a ready workspace: one kit, one starter workflow, and the first ideas for ads.
2. **Use a brand.** Every Lyra skill (video, UGC, hooks, short drama, UI motion, statics, carousels, competitor copies, variations, translation, resize) builds on the Brand Kit. This file is the one place that says how a kit is found, read, turned into an app card and a pain map, used field by field, kept true, and updated after tests. Base skills' Brand Kit references (`lyra-video-ad-generation` Reference I, `lyra-static-image-generation` Reference L) follow this file.

**Why it matters.** Generic ads come from missing product context. Lyra's nodes read the assigned kit to understand the brand's tone, value and audience ("Write as much as you can, in any format", says the Brand Kit page), and every skill takes its person, pain, words, feature, claims, offer, tone and colors from it. A thin kit gives thin ads in every skill; a wrong fact in the kit repeats in every ad.

**This is a way of thinking, not a script.** The rules are defaults and good practice; use judgment and say why in one line when you choose differently. Fixed: truth (nothing in the kit the sources don't support, no invented claims, numbers, reviews, prices or awards), the user's confirmation before a hypothesis becomes a fact, forbidden claims enforced absolutely, one kit per brand per ad (never mixed), Lyra's technical limits, and the user's explicit choices.

---

## The 6 steps (setup)

1. **Intake:** collect and read everything the user sent; research the store page and site if there's a link.
2. **Fact sheet:** sort what was found into facts, gaps and hypotheses; ask once for what only the user knows.
3. **Write the kit** in the Brand Kit standard (below), facts only, hypotheses marked.
4. **Approve:** the user sees the kit and the open questions, and says yes or corrects.
5. **Fill it into Lyra** (route by what this session can do) and check it with `list_brand_kits`.
6. **Starter workflow:** create it, assign the kit, upload the assets, add the Brand Kit notes, offer the first ads.

Steps 1 to 4 spend no credits. Step 6 spends none either: the starter workflow generates nothing.

---

## Step 1. Intake

**What the user may send, and what to take from it:**

| Source | Take |
|---|---|
| Brand book, style guide, one-page brand sheet (often an image), deck, PDF, Notion or Docs page | name, slogan, positioning, audience, tone of voice with examples, colors (hex), fonts, logo rules, do's and don'ts, legal lines |
| Product or marketing brief, notes typed in the chat | what the app does, who it's for, pains, features, offer, claims, markets |
| **App Store / Google Play link** | title, subtitle, category, description, feature list, screenshot captions, rating and number of ratings, price and trial, languages; the store promise the ads must match |
| **Reviews** (store, Trustpilot, Reddit, comments, support) | customer words in four kinds: **pain** (before the app), **outcome** (the relief), **objection** (why they hesitated), **discovery** (what surprised them); repeating patterns only |
| Website, landing page | positioning, headline promises, proof (press, partners, numbers), pricing, FAQ (objections) |
| Logo, app icon | the logo files (main, light, dark, white, black), the icon; colors measured from the pixels |
| App screenshots | the real UI: feature names as written in the app, key screens, UI colors |
| Past ads, winning creatives, performance notes | what already works (concepts, hooks, formats, segments), the tone actually used |
| Competitors named by the user | what the app does differently; claims every app in the category repeats (to avoid) |
| An existing Lyra kit (`list_brand_kits`) | the current text, colors and logo, to update instead of starting over |

**How to read:**
- Read **every** file fully. Look at every image yourself (logo, screenshots, ads). Files that exist only inside Lyra can't be seen: ask for them in the chat.
- A store link or website: open it if you can browse (web fetch or a browser); read the page, the description and the latest reviews. Can't browse → say so once and work from what was sent.
- **Colors:** take hex from the brand book when it gives them. Otherwise measure from the logo and screenshots (when you have the files and a shell: PIL, the most frequent non-white, non-black colors, then the accent), never guess from memory. Give each a role: primary, accent / CTA, background, text, secondary.
- **Fonts:** only names the brand book or the user gives. Otherwise describe the style (heavy geometric sans, rounded, serif) in the Visual identity section, without a font name.
- Several apps or brands in one pack → one kit per app; ask which first if unclear.
- A brand that exists in several markets with different offers or claims → one kit per market, or a market section in one kit; ask the user which they want (`lyra-image-translation` reads kits per market).

**Real brand or demo brand.** Ask (or read from the request) whether the brand is real or a fictional demo (for a webinar, a template, a test). Real → facts only, hypotheses marked and confirmed. Demo → Claude may invent everything, consistently, and writes "Demo brand: fictional, all details invented" as the first line of the description so no skill treats it as real proof.

## Step 2. Fact sheet and questions

Sort everything into three lists before writing:

- **Facts:** stated in a source; note the source next to each one ("store page", "brand book p. 4", "user").
- **Gaps:** a field of the standard nobody covered.
- **Hypotheses:** what Claude infers to fill a gap (a segment, a pain, an objection, a USP option, a trigger), written in the audience's words and marked **(hypothesis)**.

**Ask once, in one message, only what only the user knows** and what the ads can't do without. Propose hypotheses in the same message so work keeps moving:

1. Real brand or demo?
2. Who the app is for, if the sources disagree or say nothing; which segment matters most.
3. Approved claims and proof (ratings, numbers, awards, press, partners) and **forbidden claims** (health, finance, kids, "#1", "free", guaranteed results, competitors). Health, finance and kids apps: always ask.
4. The offer and CTA (free trial length, price, discount), per market if it differs.
5. Markets and languages.
6. Must include / must exclude (a disclaimer, a word the brand never uses, a mascot rule).
7. Is AI-generated content allowed, and is there a disclosure rule?
8. Missing files: the logo (vector or PNG on transparent), the app icon, 3 to 6 key screenshots (screenshots only, never a screen recording), product photos if physical, past winning ads.

**Defaults (state, don't ask):** the team standard below · the brand name exactly as on the store page · English (the kit's language follows the brand's main market or the user's choice) · colors from the logo and screenshots with roles · hypotheses marked until confirmed · the starter workflow named "{Brand} · Start".

## Step 3. The Brand Kit standard

Lyra's Brand Kit has these fields: **Brand Name**, **Website**, **Brand Description** (one free text field, Markdown works, "write as much as you can"), **Color Palette** (hex + label per color), **Main logo**, **Logo variations** (light, dark, white, black, custom), **Brand Assets** (reference files for the team and the generators).

Almost everything the skills need goes into **Brand Description**, written in this order with these exact headings (the team's existing kits use them, and every skill looks for them). Bold headings, short paragraphs, one fact per line; no fluff.

```
Category: {store category}
Demo brand: fictional, all details invented   ← only for demo brands

**Slogan**
*{one line}*

**One-liner**
{App} helps {who} {do what / get what} by {how}.

**Marketing Description / Positioning**
What the app is and what it is not (vs the category). The core belief. The level: mass, premium, wellness, playful, expert. 4 to 6 sentences.

**Target Audience & Pain Points**
**{Segment 1 name}**
Who: age range, situation, daily life, where and when the problem shows up.
Main pain point: in their words; what they already tried and why it failed.
What they actually want: the outcome and the identity ("someone who…").
Objections: why they hesitate to install or pay.
Customer words: 2 to 4 short real phrases from reviews (only real ones).
(repeat for 2 to 4 segments)

**Psychological Triggers**
**{Trigger name}**
What it is and how an ad uses it, in 1 to 2 lines. (3 to 5 triggers)

**USP Options**
Option 1: … Option 2: … Option 3: …

**Key Features / Value Proposition**
**{Feature name exactly as in the app}**
What it does for the user, in one line. (4 to 6 features; mark the hero feature)

**Proof & Approved Claims**
Real ratings, number of ratings, downloads, users, awards, press, partners, studies, with the source. "None approved" if none.

**Forbidden Claims**
What ads must never say or show. Category rules (health: no diagnosis, no cure, no body before/after; finance: no guaranteed returns; kids: no child in distress). "None stated" if none, never left out.

**Offer & CTA**
Trial, price, discount per market; the CTA lines the brand uses.

**Tone of Voice**
3 to 5 adjectives; we are / we are not; 2 rewrites: off brand "…" → on brand "…".

**Visual Identity**
Colors with roles and hex; the usage ratio if known. Fonts (names only from the brand). Photo or illustration style, the look of the people, the polish level (raw UGC, elevated, stylized). Logo rules. Mascot, if the brand has one (never invent one).

**Markets & Languages**
Countries, store languages, ad languages; market-specific names or offers.

**Must Include / Must Exclude**
Disclaimers, mandatory phrases, words the brand never uses, topics to avoid, AI disclosure rule.

**Template Hooks**   ← only when the brand gives its own hooks or proven ones exist
The brand's lines word for word; proven winners marked.

**Core Product Narrative**
How every ad tells the brand: the familiar moment → the turn → the after-state; the tone; what the proof is and what the point is. 4 to 6 sentences.

**Links**
Store links, website, socials.
```

**Writing rules:**
- **Facts only.** Every claim, number, rating, price, review line and award comes from a source or the user. A gap stays a gap ("None approved", "None stated") rather than a plausible guess.
- **Hypotheses** may sit in Target Audience, Psychological Triggers and USP Options, marked "(hypothesis)", until the user confirms them; confirmed → the mark is removed. Never in Proof, Forbidden Claims, Offer or Features.
- **Pains in the audience's words**, concrete moments, not categories ("snaps at her partner over nothing", not "stress").
- **Feature names exactly as in the app** (from the screenshots or store page): the skills put them on screen and in VO.
- **Length:** as much as is true. The existing team kits run about 5,000 to 9,000 characters. If the field rejects a long paste, shorten Customer words and Psychological Triggers first, never Forbidden Claims.
- The **Color Palette** field gets every brand color with a label (Primary, Accent / CTA, Background, Text, Secondary); the same hex codes and roles are repeated in Visual Identity, because skills read the text.
- **Logo and assets:** the main logo in Main logo; light / dark / white / black versions in Logo variations; the app icon, key screenshots, product photos, mascot sheets, the brand book PDF in Brand Assets.

## Step 4. Approve

Send the user, in one message:
1. The full Brand Description as it will be pasted (in the kit's language).
2. The palette (hex, role), the logo and asset files that will be uploaded.
3. **Open questions:** each hypothesis to confirm, each gap that matters, in one short list.
4. The plan for Step 5 and 6 in two lines.

Nothing is filled into Lyra before the user's yes, unless the user said "just do it": then fill it, and still list the hypotheses and gaps in the report.

## Step 5. Fill it into Lyra

**Lyra facts (Oct 2026).** The Lyra MCP tools can **list** brand kits (`list_brand_kits`: uuid, name, description, website, logo URL, palette), **assign** one to a workflow (`assign_brand_kit`, replaces any assigned one, on the workflow's main variation) and **unassign** it. They can't create or edit a kit yet. Check the tool list at the start of every build: when a create or update brand kit tool appears, it is Route 1 and this paragraph is out of date.

Pick the route by what the session can do:

| Route | When | How |
|---|---|---|
| **1. MCP tool** | a create / update brand kit tool is in the Lyra tools | create the kit with name, website, description, palette; upload the logo and assets as the tool asks; then check |
| **2. Browser** | Claude can drive a browser where the user is signed in to Lyra | fill the Brand Kit page (below) |
| **3. User pastes** | neither | give the user copy-ready blocks per field and short steps; the user fills and says "done"; then check |

**Route 2, the Brand Kit page** (app.lyra.splitmetrics.com → sidebar **Brand Kits**):
1. **Update, don't duplicate.** `list_brand_kits` with `search` = the brand name first. A kit exists → open it and edit, after the user's yes.
2. **Create brand kit** (top right) creates the kit **at once**, named after the workspace, and opens it; the page **autosaves** ("Saved" top right), there is no Save button. Click it **once**; a second click makes a second empty kit.
3. **Brand Name:** replace the default name first. **Website:** the site or store link.
4. **Brand Description** is a rich text editor (TipTap with a Markdown extension), not a plain textarea: form-fill tools fail on it, and typing Markdown character by character leaves literal asterisks. Set it in one go from the page: `document.querySelector('.tiptap').editor.commands.setContent(md, {contentType: 'markdown', emitUpdate: true})` with the approved Markdown as a template string (check it has no backticks or `${`), then click outside the editor, wait for "Saved", and read it back with `list_brand_kits`: Lyra stores it as Markdown (bold headings come back as `**Heading**`). No script access → paste the text by hand from the copy-ready block.
5. **Color Palette:** **Add color** adds a swatch at #000000 → select the hex text field (triple click), type the hex, Tab → click **Label**, type the role, Tab. Add all swatches first, then fill them in order. **Presets** offers ready palettes: not for real brands.
6. **Main logo** (one image), **Logo variations** (several images) and **Brand Assets** (any files, several) are file inputs: with a browser file-upload tool, upload straight into each input (no click on the box: that opens the system file picker). Brand Assets takes the brand book PDF, the brand sheet, screenshots, product photos, mascot sheets. Without such a tool, tell the user exactly which file goes in which box and wait.
7. Never delete a kit or a file in it; if something was created by mistake, tell the user which one and let them delete it (or reuse an empty kit created by mistake for this brand).

**Route 3, copy-ready blocks:** one block per field, in the order of the page (Brand Name · Website · Brand Description · colors as "hex · label" lines · which file goes to Main logo, Logo variations, Brand Assets), plus: "Lyra → Brand Kits → Create brand kit (once, it saves itself) → rename it → paste each block → Add color per line → upload the files". Ask the user to say "done" and the kit's name.

**Check (every route):** `list_brand_kits` with `search` = the name → the uuid; the name exact, the description complete (start and end match), the palette hex codes and labels, the logo URL present. A difference → fix it (Route 2) or tell the user exactly what to fix (Route 3).

## Step 6. The starter workflow

The first workflow is a ready canvas for every next skill. It generates nothing and spends no credits.

1. `create_workflow` titled "{Brand} · Start".
2. `assign_brand_kit` with the kit's uuid. Check the result shows the `brand_kit_uuid`.
3. **Assets on the canvas:** `list_uploads` first (the user may have uploaded them); otherwise `create_upload` (a public link, or the file posted with the upload descriptor), `complete_upload` with the returned file id, then `attach_upload` for each. Lyra media links (the kit's logo URL) don't work as `{url}` sources: they need a sign-in. If the shell can't reach the upload host (a proxy refuses it) but Claude drives a browser signed in to Lyra, post the file from the Lyra page itself: `fetch` the file (a Lyra media URL of the kit's logo or asset works there), build the FormData with every field of the descriptor, POST it with the descriptor's Authorization header, then `complete_upload`. No way to send it → `open_upload_widget`, or ask the user to drop the files on the canvas. Label each node: "Logo", "Logo · white", "App icon", "Screenshot 1 · {screen name}", "Product photo", "Past ad · {name}". Screenshots, logo and icon are what the image and video skills connect as references.
4. **Notes** (`create_user_text_node`, notes for the user and the next skills; they feed nothing yet):
   - **"App card"**: the one-paragraph card every skill keeps (format in Using a Brand Kit).
   - **"Pain map"**: per segment: pains in their words, desires, objections, the moment where the pain shows up, the feature that answers it; marked (hypothesis) where not confirmed.
   - **"Open questions"**: gaps and hypotheses still waiting for the user, if any.
5. `create_frame_node` around the assets: "STEP 1 · Brand assets — your logo, icon and screenshots" (pink); around the notes: "NOTES · Brand Kit notes" (slate). STEP notes, colors and placement follow `lyra-workflow-layout`.
6. `get_workflow` to check: the kit assigned, every node present and labelled.
7. If the user has the workflow open in a browser while it's being edited through the tools, the canvas may not refresh: ask them to reload it, or reopen it for them when you drive the browser.

**Then offer the first ads** (no build without a yes): 3 to 4 ideas, one line each, each tied to a segment and a pain from the pain map and to the skill that would build it, one recommended:
- "UGC, {segment}, {pain moment} → `lyra-ugc-video`"
- "4 hooks on {pain} → `lyra-video-hooks`"
- "A static, {layout} on {feature} → `lyra-static-image-generation`"
- "Animate the {screen} screen → `lyra-ui-motion-video`"
- "A 90 s story, {hero} → `lyra-short-drama`"
- "Copy a competitor's ad you like → `lyra-copy-competitor-ad` / `-static`"

## Report

One short message: the kit's name and what it holds (segments, features, claims status, colors), the route used and anything the user still has to do (files to upload, a stray kit to delete), the starter workflow's name and what's on it, the open questions, and the first ad ideas.

---

## Using a Brand Kit (rules for every Lyra skill)

Every Lyra skill follows this section before any concept, script, prompt or plan. A skill's own Brand Kit table (what UGC or short drama takes from it) adds to this, never replaces it.

### 1. Find the kit

Source order:
1. The user's words in this chat (always win).
2. A Brand Kit sent in the chat (text, file, link).
3. The kit assigned to the workflow (`get_workflow` → `brand_kit_uuid`), then the workspace's kits (`list_brand_kits`).
4. **One** candidate → confirm in one line: "I'll make it for {kit name}, right?" **Several** → ask which, by name. **None** → offer to set one up with this skill (Steps 1 to 6), or ask for the essentials in one message: app name, what it does, audience, pains, the feature to show, approved claims, forbidden claims, offer, tone, colors (hex), logo, icon, screenshots.
5. Once chosen, `assign_brand_kit` on the workflow if it isn't assigned. **Never mix two kits** in one ad. One kit per market → the market's kit.

### 2. Read it fully, every time

The whole description, not the first lines: the segments, Forbidden Claims and Must Exclude are usually near the end. Also the palette and the logo. A kit read in an earlier session may have changed: read it again at the start of every build.

### 3. Keep an app card for the session

> App card: {App} · {what it does in 8 words} · for {main segment} · pain: {main pain} · may show: {2 to 3 features, real names} · claims: {approved, or "none approved"} · forbidden: {short list, or "none stated"} · offer: {…} · tone: {3 words} · colors: {hex primary / accent} · assets: {logo, icon, N screenshots} · source: Brand Kit "{name}"

### 4. Build the pain map

From Target Audience & Pain Points, per segment:
- **Audience:** who, the situation, the daily moments where the problem shows up.
- **Pains:** in their words; what they tried and why it failed.
- **Desires:** the outcome and the identity they want.
- **Objections:** why they hesitate.
- **Product truth:** the feature that answers each pain, the claims, the offer, proof, tone, must include / exclude, forbidden claims.
- **Motivation layers** (for angles): what they fear, what frustrates them, what they want.

Pains missing, vague or generic ("stress", "busy life") → write 3 to 5 **pain hypotheses** in the audience's words, ask the user to confirm, and keep working in the same message. With a store link: the review research (pain, outcome, objection, discovery words) sharpens the map. Reuse a pain map already made for this app (the "Pain map" note in the starter workflow, or an earlier round).

### 5. What each part of the kit is for

| Brand Kit part | Used for |
|---|---|
| Category, One-liner | the app card; which category guide a skill uses |
| Positioning (mass, premium, wellness, playful) | the polish level: raw UGC, elevated, stylized; the realism and finish of statics |
| Segments: who, daily life | the persona (age, look, market), the place and moment of the pain, casting for audience variations |
| Pains, customer words | hook lines, the "old way" beat, the speech, headlines, carousel card 1, the pain chain in a story |
| Desires, outcomes | the result beat, the after-state, the payoff, identity triggers |
| Objections | skeptic and honest-review formats, objection-first spines, FAQ cards |
| Psychological Triggers | the concept mechanism and the hook type |
| USP Options, Slogan | headline and end card lines, the value proposition in the brief |
| Key Features (exact names) | the one feature per ad, the demo beat, what is shown on screen, the turn in a story |
| Proof & Approved Claims | the **only** numbers, ratings, reviews, awards and results an ad may say or show |
| Forbidden Claims | hard rule for every line, caption, visual, VO, card and ad copy |
| Offer & CTA | the CTA line, the end card, the offer card; never a price or trial not listed here |
| Tone of Voice | word choice, humour, energy of every line and the persona's voice |
| Visual Identity, Color Palette | palette anchors in every prompt, CTA and type colors, the world of a story; UGC uses brand colors only as subtle accents |
| Logo, icon (Main logo, variations, assets) | end cards and statics, exactly as supplied, never redrawn |
| Screenshots (assets) | every phone screen and UI insert, identical word for word |
| Mascot | only when the kit has one; never invented |
| Markets & Languages | the persona's market, the spoken language and accent, which kit or section per market for translation |
| Must Include / Must Exclude | hard rules in every plan and prompt |
| Core Product Narrative | the arc of the ad and the place of the app and the proof in it |

### 6. Truth and brand safety

- **Claims only from the kit or the user:** no invented numbers, ratings, reviews, durations of use, results, prices, offers, awards or press. AI-generated people are never presented as real customers or real experts; testimonials only from real reviews.
- **Forbidden claims are enforced absolutely**, in every line, caption, visual, VO and ad copy, including words that only become a forbidden claim in translation. If the user asks for one: say once that it is on the kit's forbidden list and leave it out, unless the user confirms the kit is outdated (then offer to update the kit).
- Brand safety (Lyra's System Preamble): no profanity, no political statements, no unsubstantiated health claims, no competitor disparagement.
- A demo brand's invented facts stay inside its own ads and are never used as proof for a real brand.

### 7. Conflicts and gaps

- **The user's words win over the kit;** name the conflict in one line ("The kit says calm and ironic; you asked for loud and hype: going with yours").
- **Sources disagree** (the app's UI is blue, the kit's main color is violet) → say it and ask which wins; default: kit colors for backgrounds, type and CTA, the screens exactly as they are.
- **A gap** is filled by asking or by a marked hypothesis, never from a competitor's ad and never from imagination. No approved claim → no claim. No real review → no review card. No screenshots → no readable screen. No mascot → a person, an object or an original illustration.

### 8. Feed learnings back

After a test, what was learned belongs in the kit: a winning pain, segment, hook type or angle; a losing one; new customer words; a corrected fact. Offer the update in one line ("Add 'exam-week brain' as a proven pain for Students?"), and on a yes update the kit (Step 5 route) and the "Pain map" note. Never change a kit silently, never remove a forbidden claim without the user.

---

## Updating a kit

"Update the brand kit", new materials, a new market, a rebrand: `list_brand_kits` → read the current kit → show a short diff (what is added, changed, removed, with the source) → the user's yes → fill it in (Step 5 route) → check. A rebrand or a new market with different claims or offers → ask whether to edit this kit or make a new one; workflows already assigned keep the old kit until reassigned.

## Common mistakes

| Mistake | Prevention |
|---|---|
| A plausible number, rating or review written into the kit | Facts only, each with its source; "None approved" when nothing is |
| Hypotheses saved as facts | "(hypothesis)" until the user confirms; never in Proof, Forbidden Claims, Offer, Features |
| Forbidden Claims left out because nobody mentioned them | Always ask; "None stated" written explicitly; category rules added |
| Generic pains ("stress", "no time") | Concrete moments in the audience's words; review research |
| Feature names paraphrased | Exact names from the app's screens or store page |
| Colors guessed | Hex from the brand book or measured from the logo and screenshots, with roles |
| Two empty kits from two clicks on Create brand kit | Click once; rename first; check `list_brand_kits` |
| A new kit made while one already exists | Search by name first; update instead |
| Long description cut on paste, nobody noticed | Read it back; compare start and end |
| Description pasted with literal asterisks | Set it through the editor's Markdown command, never typed character by character |
| Starter workflow without the kit assigned | `assign_brand_kit`, then `get_workflow` to check |
| A skill wrote ads from the first lines of the kit | Read it fully every time; Forbidden Claims and Must Exclude are at the end |
| Two kits mixed in one ad | One kit per ad; ask which |
| A kit changed or a forbidden claim removed without asking | Diff and the user's yes, always |

## Quality gates

- **Stage 0 (before showing the kit):** every source read? Every fact with a source? Every heading of the standard present (gaps written as such)? Pains concrete, in the audience's words? Feature names exact? Proof, Forbidden Claims, Offer free of hypotheses? Colors with hex and roles? Real or demo stated?
- **Stage 1 (after filling):** `list_brand_kits` shows the exact name, the full description, every color with its label, the logo? No duplicate kit?
- **Stage 2 (starter workflow):** the kit assigned? Logo, icon, screenshots on the canvas and labelled? App card, Pain map, Open questions notes in place? Frames? First ad ideas offered, each tied to a pain and a skill?
