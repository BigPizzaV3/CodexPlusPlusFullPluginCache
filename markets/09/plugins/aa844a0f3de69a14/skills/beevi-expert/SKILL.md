---
name: beevi-expert
description: >
  Fundamentals of Beevi for agents driving it through the Beevi MCP tools. Beevi is an
  AI branding agency for SMBs — it learns a business's brand and creates, schedules, and
  publishes social content (posts, campaigns, cover images, carousels, videos) across
  LinkedIn (personal profile and Company Page), X, Instagram, Facebook, TikTok, YouTube,
  Google Business Profile. Use this skill whenever a request
  involves a business's social content or brand: creating or scheduling posts, generating
  cover images or other visuals, planning campaigns, brainstorming post ideas, using or
  improving the brand identity/voice, or working with the business's visual collections
  (products, characters, properties). Trigger even when Beevi isn't named — e.g. "make a
  post about our main dish", "generate a cover for the jacuzzi post", "plan a campaign
  about our menu", "help me think of something to post".
---

# Beevi Expert — operating a brand through Beevi

Beevi is a SaaS branding agency for small businesses. The business's brand identity,
knowledge, and visual references are **already in Beevi** — your job is never to invent
content from thin air, but to *retrieve what the brand already knows about itself* and
generate from that. An agent that skips retrieval produces generic, off-brand content
and wastes the user's money.

## The one economic rule

**Reads are free — spend them lavishly. Writes cost the user credits — never spend one
on an unresolved ambiguity.**

Every `list_*` / `get_*` tool is free. Every `generate_*` / `create_*` / `publish_*`
tool costs real credits and/or posts publicly. So: search first, ground everything,
ask when genuinely ambiguous, and only then generate. An agent that internalizes this
rule derives the rest of this skill on its own.

## The object model (what everything is)

### Know which workspace you're in (do this first)

Your API key is scoped one of two ways, and it changes your first move:

- **Workspace-scoped** — every tool call operates on that one workspace automatically;
  `workspace_id` args are ignored. `list_workspaces` returns exactly one entry.
- **Organization-scoped** — always the case when you connected through a directory
  (Claude's or ChatGPT's "connect" button runs OAuth, which mints an organization key). You
  can reach several workspaces and must pass
  `workspace_id` explicitly. If the user's request doesn't unambiguously name which
  brand (or `list_workspaces` returns more than one), **confirm the workspace with the
  user before doing anything else** — every read you make and every credit you spend
  lands in a specific brand's account, and operating on the wrong client's brand is the
  worst mistake available to you.

Either way, call `list_workspaces` once at the start so you know whose brand you're
speaking for — don't infer it from the user's phrasing.

| Object | What it is | Read with |
|---|---|---|
| **Workspace / business** | One brand. All tools are scoped to a workspace (business). | `list_workspaces`, `get_workspace` |
| **Brand profile** | The brand's identity: description, voice, tone, preferred/banned phrases, colors, fonts, target audience, competitors, goals, cover-image guidelines, **language**. | `get_brand_profile` |
| **Photo rules** ("What Beevi can show") | The owner's standing rules for what a COVER may show: `place` (real / imagine / hidden — their own space, the `location` items tagged `My business`), `owner` (ai_scenes / real_only / hidden — their face), `product_style`, `work` (real / hidden), `ai_people` (yes / no). Absent = never chosen. They limit what an image shows, never which topics get planned; covers, carousels and Compass obey them on their own. Change them only with `update_photo_rules`, and only when the owner explicitly asks ("don't put me in posts") — never infer one. | `photoRules` in `get_brand_profile` |
| **Memory** | A stored fact the brand wants recalled when generating — menu items, pricing, awards, taglines, policies. The richest source for "post about our X". | `list_memories`, `get_memory` |
| **Weekly Compass** | The brand's weekly "what to consider this week" signals: rising `search_trends` (each with a `post_angle`), recent `relevant_content` articles, `calendar_events`, and a markdown `overview` digest. The best source for "what should I post about right now?" / trend-driven ideas. Read-only; may be empty if the brand hasn't opted in. | `get_compass` |
| **Performance** | How published posts actually did, per platform (views, engagements, engagement rate, followers, best times to post). `get_analytics_summary` is the overview: `status` + `next_step` when there are no numbers (`connect`, `reconnect`, `unavailable` or `waiting` — say the next step), a `summary` per metric with `change` / `change_kind`, top and lowest posts, `best_times` and `unavailable` notes (add `include_daily: true` only if you need the daily series). `list_post_performance` ranks posts (`sort`: `usual`, `usual_asc`, `views`, `engagements`, `engagement_rate`, `date`); `vs_usual` 1.0 = a typical post for that account, above 1 beat it. `vs_usual` and `change` can also be `null` when there is not enough history to compare. `get_post_performance` takes a `published_post_id` or a `post_id` and returns the numbers plus the growth curve (with a `post_id`, platforms without numbers come back in `missing`: `not_synced_yet` or `not_tracked`). `last_synced_at: null` (or a "Not synced yet" note in `unavailable`) means the first sync is still pending — numbers arrive within a few hours of publishing. On a synced post a `null` metric means the platform did not report it, never 0 — do not average it in or say "no engagement". Call `get_analytics_summary` before recommending what to post more of; use `list_post_performance` with `sort: usual` for the best posts. Free on every plan; `get_post` / `list_posts` (with `include_content`) also carry a `performance` block. | `get_analytics_summary`, `list_post_performance`, `get_post_performance` |
| **Post idea** | One unit of content as the user thinks of it: prompt, cover image, schedule time, status. | `list_posts`, `get_post` |
| **Social post** | A per-platform variant of a post idea (LinkedIn copy ≠ Instagram copy). Each has its own status: drafted / pending_approval / approved / scheduled / sent / failed. | inside `get_post` |
| **Campaign** | A themed sequence of posts over a duration (e.g. "2-week menu campaign" → ~8 posts). | `list_campaigns`, `get_campaign` |
| **Collection** (Visuals) | A named group of visual reference items: products, characters, properties, locations. Comes in two kinds, and every item carries free-text `tags` — see below. | `list_collections`, `list_collection_items`, `get_collection_item` |
| **Asset** (Brand Media) | A Brand Media file. `origin` says who put it there: `user` (the customer) or `generated` (a model). `list_assets` filters on it, and on `unused` (never in a post yet — entries that have been carry a `used` tag; `get_asset` prints **Last used**). | `list_assets`, `get_asset` |
| **Style** | A saved visual style (e.g. "Watercolor") referenced by name+description in prompts. | `list_styles` |
| **Visual template** | A reusable cover *overlay* (text/logo/badges) — the business's saved templates + built-in starter presets. Apply one onto a post cover with `apply_visual_template`. | `list_visual_templates` |
| **Carousel** | A multi-slide image post for LinkedIn/Instagram. You can let the AI plan the deck, or write each slide yourself. | `list_carousels`, `get_carousel`, `generate_carousel`, `edit_carousel_slide`, `attach_carousel` |
| **Recipe** (post format) | A proven post format for the brand's niche (idea, angle, cover look; carousel recipes also carry a slide arc). Owners browse them on the Inspiration page and Compass plans from them. `list_recipes` lists them (8 per page, `niche` for another kind of business); `generate_post` with a `recipe_id` makes a post in one, always with an AI cover (costs credits). See "Post ideas from formats" below. | `list_recipes`, `generate_post` (`recipe_id`) |
| **Job** | Long-running generation runs asynchronously; poll with `get_jobs`. | `get_jobs` |

### The two kinds of collection (the key Visuals distinction)

- **Reference sheet** (`reference_style: sheet`) — each item is ONE identity-locked
  image of a character or product. Tagging it keeps that subject looking identical
  across generations. An item is usable **only when its sheet status is `ready`**.
- **Gallery** (`reference_style: multi_image`) — each item is a BUNDLE of real photos
  of one thing (a property, a store). Tagging the item spreads ALL its photos in as
  references; you can also tag one specific photo.

**A collection's name is not evidence. Only a listed, ready item is.** Businesses often
have an empty "Characters" collection — always `list_collection_items` and check status
before promising or tagging anything.

### Item tags

Every item carries up to 10 free-text `tags`, returned by both `list_collection_items` and
`get_collection_item`. They are labels you can reason about — the suggested vocabulary per
collection type is spelled out in those tools' own descriptions.

- **`My business`** is the one tag code keys on: it marks the location item that IS the
  business's own premises (written during onboarding, when the owner is asked "which of these
  is your business?"). That is how you find "our shop" / "our office" for a post — read the tag,
  don't guess from item names.
- `manage_collection_item` writes them **replace-not-merge**, same as `metadata` — call
  `get_collection_item` first and send back the full list, or you will silently drop tags.

## @-mentions: how you wire brand material into generation

Prompts passed to generation tools support `@[Name](scheme:uuid)` mentions. This is how
retrieved material actually reaches the model — a mention is not decoration, it attaches
the real reference:

| Mention | Attaches | Use for |
|---|---|---|
| `@[Maya](item:uuid)` | The item's reference sheet (1 image) or, for a gallery item, ALL its photos | Consistent characters/products; real property/location photos, app screenshots |
| `@[Photo 3](item_image:uuid)` | One specific gallery photo | When only one photo of a place is wanted |
| `@[Products](collection:uuid)` | Every ready sheet in the collection | "Show our whole product line" — sheet collections only, never gallery collections |
| `@[Brand Logo](asset:00000000-0000-0000-0000-000000000001)` | The brand logo image | Putting the logo in a generated image |
| `@[Photo](asset:uuid)` | That asset (either origin) | Any Brand Media file as visual reference |
| `@[Watercolor](style:uuid)` | **Text only** (name + description, no images) | Visual style direction |
| `@[Pricing](memory:uuid)` | **Text only** (the fact, inlined) | Grounding copy in a stored fact |

Surface limits worth knowing. A whole gallery item attaches **every photo it has**, so where
it may go depends on how many references that surface can hold:

- **image / cover / video** — fine, it spreads.
- **carousel deck `prompt`** — fine, and it is the good move: the item becomes a *catalogue*
  and the planner puts the photo that fits onto each slide. This is how you say "use our real
  photos".
- **a single carousel slide, or `edit_carousel_slide`** — refused (every photo onto one image).
  Tag ONE photo there with `@[Name](item_image:UUID)` from `get_collection_item`.
- **post body / campaign text** — refused; that text is written from words, not pictures.

`item_image:` is one reference, so it is welcome anywhere an image is rendered. Image models
cap total references (~14) — tag the few that matter.

## The loop: Resolve → Ground → Gate → Execute

Run this loop for every content request. The common failure mode is skipping straight
to Execute.

### 1. Resolve the subject (free)

"The jacuzzi", "our main dish", "the new sunscreen" — the subject almost always already
exists somewhere in Beevi. Search, in parallel:

- `list_memories` — facts ("Joe's is known for 18-inch NY-style pies")
- `list_collections` + `list_collection_items` — visual references (a "Radiance Serum"
  product sheet, a property gallery)
- `list_posts` — existing posts ("the post about the jacuzzi" → find that actual post). Also
  filterable by `lifecycle` — `needs_attention` (awaiting approval / overdue / declined / failed
  generation / partially published — a platform leg failed), `upcoming` (scheduled), `drafts` (draft or
  still generating), `published` (fully published) — to answer "what needs my attention" or "what's
  going out next" in one call instead of scanning everything. A post whose scheduled time passed
  without ever generating (e.g. the org ran out of credits) shows up here as `generation_failed`
  with `publish_error`: *"Not generated before its scheduled time (e.g. out of credits). Open it and
  click Generate."* — explain that plainly and offer to `generate_post` it now, or point at a top-up
  if credits are the actual cause.
- `list_assets` — the customer's photos (`origin: 'user'`) or model output (`origin: 'generated'`); `unused: true` narrows to photos that have never been on a post — the pool to pick a fresh cover reference from, so the same product shot is not reused week after week (a photo counts as used once a post carries it, or carries an AI image made from it)

Search results are shallow — **open the top candidates with `get_post` /
`get_collection_item` before concluding something doesn't exist.** The subject often
lives inside a platform variant's body text, not in the title or search index, and a
"no such post exists" verdict you didn't verify is worse than a wrong guess: it sends
the user to re-explain something you already had.

While you're in `list_posts`, also check for **existing content about the same
subject** — an unsent draft about the same product means your job may be to revive or
update it, not to pay for a duplicate.

The subject may live in one, several, or none of these. Multiple plausible matches
(three sunscreen products) → that's a question for the user, not a guess.

### 2. Ground in the brand (free, never skip)

Call `get_brand_profile` before generating anything. (Generation tools do inject brand
context server-side, but that doesn't replace reading the profile yourself — you need
it to write the prompt in the right language, honor banned phrases, and know the cover
rules *before* you spend, not discover them in the output.) Apply:

- **Language** — generate in the brand's language. A Hebrew brand gets Hebrew posts.
  The voice_description may itself be written in that language — that IS the voice;
  don't translate it away or default to English.
- **Voice & tone** — write like the brand, not like an assistant.
- **Banned/preferred phrases** — hard constraints on copy.
- **Cover guidelines, colors, logo position** — hard constraints on cover images.
- **Target audience & goals** — pick angles that serve them.

### 3. Gate: the pre-spend checklist (this is where you ask)

Before ANY credit-spending call, you must be able to name all three:

1. **The resolved subject, with evidence** — a specific memory / item / post / asset ID,
   or an explicit "nothing found — proceeding on brand identity plus the user's words".
2. **The target** — which platforms, or which existing post the cover is for.
3. **The visual grounding** — which mentions you'll attach, or an explicit
   "no relevant visuals exist".

Any of the three missing or ambiguous → ask the user. Bundle everything into **one
message with at most ~2 questions**; offer the concrete options you found ("I found
three sunscreens: PROTECT ME, PROTECT BODY, GLOW ME+ — which one?"). If all three are
resolved, do NOT ask permission to proceed — act.

**Show your grounding** as you proceed, in one line: *"Found the jacuzzi in the
rooftop-spa memory and 4 photos in the 'Amenities' gallery — using those."* This is the
cheapest way for the user to catch a wrong resolution before credits burn.

### 4. Execute (costs credits)

Pick the narrowest tool that does the job, wire in the mentions, then poll `get_jobs`
if the run is async, and report what was created (with links/IDs).

## Per-intent playbooks

### "Generate a cover image for the post about X"
1. `list_posts` → find the actual post about X (it usually exists — that's why they said "the post").
2. Resolve X's visuals: gallery photos of the real thing beat AI imagination — a real
   jacuzzi photo tagged as reference makes a truthful cover.
3. `get_brand_profile` → cover guidelines, colors, logo position.
4. Gate, then `generate_cover_image` for that post with the mentions attached.
5. If the post **already has a cover**, replacing it is a destructive-ish edit — say
   you're replacing it (or ask, if the user only said "make a cover" without naming
   the post confidently).

### "Create a post about our X" (main dish, new product, a property…)
1. Resolve X across memories / collections / assets. The best post copy is grounded in
   a real fact ("late-night weekend hours", "$340/year") — tag the memory.
2. `get_brand_profile` → language + voice.
3. Gate (platforms? one product or several matches?).
4. `generate_post` (full agent run: copy + platform variants + cover) or `create_post`
   (you write the content). Prefer `generate_post` unless the user dictated exact copy.
   To make it a **carousel**, pass `post_type: 'carousel'` — the one post job also generates
   and attaches a branded multi-slide carousel on carousel-capable platforms (costs extra
   carousel credits; falls back to a plain post if the platforms can't host one).

### "Make a carousel with these slides" (the user dictates the content)
**First check whose pictures these are.** If the user handed you actual photos, they want those
photos posted — see the next playbook. `generate_carousel` *invents* artwork and costs credits;
reach for it only when new pictures are what's wanted.

`generate_carousel` has two modes. Given only a topic, an AI planner writes the deck.
But when the user tells you what the slides should say — or you have researched the
subject and know — pass `slides[]` and write them yourself; the planner is skipped and
their wording survives verbatim.

Each slide is `{ text, visual }`:
- `text` — every word to render ON the slide, in quotes, with placement where it
  matters: `"Best in town" large in the middle, "Guaranteed" small bottom-left`. Write
  the words, never a label for them ("Headline: …" renders the word "Headline").
- `visual` — what the slide SHOWS, subject only. Don't put palette or fonts here; those
  come from `visual_style` (deck-level, optional — omit it and the brand profile
  supplies one). Per-slide styling is how a deck ends up looking like three decks.
- Tag a product with `@[Name](item:UUID)` inside `visual` to put its real photo on that
  slide. Sheet items only.

**Where the words live — `text_mode`.** By default the image model paints the words into
each picture. Pass `text_mode: 'dynamic'` and it shoots the photographs text-free instead,
then lays the copy over them as real text in the brand font: crisp type at any size, no
misspelled words, and the user can retype or move it afterwards in the Carousel Maker. Good
for a wordy deck, a brand that cares about its typography, or any language the image model
spells badly. It cannot be combined with `slides[]` or `template_id` — a dynamic deck's copy
is written by the planner alongside the photographs it has to fit, and a template already
defines where text sits. Pass `prompt` alone.

To change a deck afterwards, `edit_carousel_slide` handles one slide: `instruction`
for the look ("make it darker"), `text` for new words, or both. Changing several slides
means several calls — in the in-app chat they run in parallel when emitted in one turn.
An edit keeps the references the slide already has, and a mention in `instruction` attaches
its photo too — `@[Name](item:UUID)` for a sheet product, `@[Name](item_image:UUID)` for one
real photo (this is how "use the actual photo of our entrance" is honoured), `asset:` for
Brand Media. Say how to use it: "as the background, exactly as-is". Tag sparingly — the
slide's own references and yours share one per-model budget, so tagging several can push the
slide's existing subjects out of the frame.

On a **dynamic** deck `text` is refused — the words are a layer over the photo, not part of
it, so rewriting them through the image model would leave the slide with two headlines.
`instruction` works normally there and is usually all you need: it replaces the picture and
the existing words re-fit themselves to it. To change the *words*, use `set_cover_text` with
the `carousel_id` and `slide_number` — free, instant, no new picture.

### Saving the user's photos to Brand Media — always describe them yourself

`upload_asset` (a URL) and `get_upload_token` (local files via curl) put the user's own photos into
Brand Media. You have usually SEEN the photo, so pass **`visual_description`**: 2-4 factual
sentences, and say FIRST if the photo carries any text, logo or signage. Then it costs the user
nothing. Without it, a workspace that uses its own photos as covers pays for Beevi to look at the
photo (about 1 credit per 70 photos) and the tool result carries a `note` saying so. With curl, put
each `-F visual_description=…` immediately after its `-F file=@…`. To describe a photo that is
already uploaded, `update_asset({ asset_id, visual_description })`.

### "Put these photos on the post" (the user's OWN pictures) — `set_post_photos`

When the user hands you photos — chat attachments, which arrive with an `asset_id`, or ids from
`list_assets` — and wants them published, that is `set_post_photos`. **Free and instant.** It
does not generate, edit or restyle anything; the photos go up exactly as supplied. This is the
answer to "make a carousel out of these", "post these five shots", "use my photos instead".

```
set_post_photos({ post_id | social_post_ids, photo_asset_ids: [...] })
```

- **The order you pass IS the slide order.** Nothing re-sorts them.
- Target `post_id` for every photo-capable platform of the post, or `social_post_ids` for
  specific platform versions. Exactly one of the two — not both, not neither. All the ids must
  belong to one post.
- **REPLACE, not append.** It swaps out whatever media those posts have. To *add* photos, call
  `get_post` first and pass the existing ones plus the new ones.
- **Photos only.** A post holds photos OR one video, never both — a video in the set is refused.
  To set a video cover, use `update_social_post`'s `cover_media`.
- Each platform version is trimmed to its own limit (x 4, google_business 1, facebook/instagram
  10, linkedin 20, tiktok 35) and the result reports `trimmed_from`. Published posts and
  platforms that can't take photos come back in `skipped[]` with a reason. **Tell the user in
  one line what was trimmed or skipped** — the card doesn't show it.
- Editing a post this way **re-opens its approval** if it was scheduled.

### Changing the words ON a cover — `get_cover_text` / `set_cover_text`

A **dynamic** cover carries its headline as real text over the photo, so rewording it is a
database write: free, instant, no image regeneration, no credits. An **embedded** cover has
the words painted into the pixels and nothing can edit them in place.

`get_cover_text({ post_id | social_post_id | carousel_id, slide_number? })` **is the test for
which one you have** — call it first on any "change what the cover says" request:

- `text_nodes` present → editable. Reword with `set_cover_text`.
- `text_nodes` **empty** → baked into the photo. The only way to change them is to
  regenerate the picture (`update_post({ generate_cover_prompt })` for a post cover,
  `edit_carousel_slide({ slide_number, text })` for a deck slide). Both cost credits and
  produce a *different* picture — say so and get a go-ahead first.

`set_cover_text` takes either `find` + `replace` (prefer it when the user quoted the wording
— it cannot rewrite the words around the ones they asked about) or `edits: [{node_id, text}]`
addressed by ids `get_cover_text` returned. **Never invent a node id**, and note it can only
reword lines that already exist — adding a new subheadline is an editor job. Defaults to
every platform of a post / every slide of a deck; narrow with `social_post_id` or
`slide_number`. Refused on published posts and video covers.

**Order matters:** edit the deck *before* `attach_carousel`. Attaching copies the slides
into the post, and later slide edits don't flow through to a post already attached.

### The first comment under a post — `get_auto_comments` / `set_auto_comments`

Beevi can publish a comment under its own post the moment that post goes live — the
"link in first comment" play. `set_auto_comments({ post_id | social_post_id, comments:
[{content, delay_minutes}] })` **REPLACES the whole list**, so call `get_auto_comments`
first when editing one of several; use `mode: 'append'` to add one without touching the
rest. No comment id ever crosses the wire, which is deliberate — there is none to invent.

Write each platform in its own idiom, and note these are platform facts, not house style:
a real clickable URL on LinkedIn, Facebook and X (keep X under 280 characters); on
Instagram a URL in a comment is dead text, so point at the bio instead. TikTok, YouTube and
Google Business cannot take one at all, and Facebook/Instagram are gated off in production
pending Meta's review — the tool says which when it refuses.

**Only before the post publishes.** The comment's timer starts at the real publish moment,
so a post that is already live can no longer take one and the tool will refuse. Schedule
the comment while you schedule the post. `delay_minutes: 0` is right for a link — it should
be there when readers arrive.

### "Generate a campaign about our X" (menu, product line, event series)
1. Resolve X — a campaign needs *enough material*: several memories/items to spread
   across posts. List what you found and how it maps to a sequence.
2. Gate: duration, cadence/post count, platforms, content types (text / +carousel /
   +video) — these are exactly the ambiguities worth one bundled question.
3. `create_campaign`. Report the plan, don't just say "done". Two modes: for an open
   ask, use `brief` mode (put the cadence wording in `brief`, compute `post_count`
   yourself) so the campaign agent plans it; if the plan was already shaped in chat,
   pass pre-planned `posts[]` instead for an instant, no-planning-credit create.

### "Rename / pause / delete the campaign" · "move this post into the campaign"
- `manage_campaign` action `update`: title, description, period, and pause/resume
  (`status` — only active↔paused transitions are allowed).
- `manage_campaign` action `delete` is PERMANENT — confirm with the user first, and
  state what happens to its posts: `delete_posts=false` (default) keeps them detached;
  `=true` also deletes them and is refused if any is already published.
- Move a post in/out of a campaign: `update_post` with `campaign_id` (a campaign id
  attaches, `null` detaches). Campaign dates do NOT auto-adjust to the moved post.
- Delete a whole post (all platforms): `delete_post` — permanent, confirm first;
  refused if any platform is already published (use `delete_social_post` for the
  unpublished platforms instead).

### "Help me think of what to post" (ideation — reads only, free)
1. Pull broadly: brand profile, memories, collections, recent posts (to avoid
   repeating), upcoming season/dates.
2. Offer ~5 concrete, brand-specific angles, each naming its grounding ("Your 'Top 10
   rooftop bars' award memory → a 'golden hour at Top of the Gate' reel").
3. Generate nothing until the user picks.

### "Post ideas from formats" (inspiration — reads only until the user picks)
When the user asks for post ideas or inspiration, call `list_recipes` (proven post formats for
their niche). Show a few and let them pick. Before generating, ask up to 3 short questions about
what the chosen format needs (their product, a photo, a detail), and say the AI cover costs
credits. Then `generate_post` with that format's `recipe_id` and their answers in `prompt`.

### "Does this sound like us?" / "Make it more our voice"
`get_brand_profile` → check against voice_description, tone, banned phrases — quote
which rule the draft violates. Rewriting copy text is free (it's your text edit);
regenerating a post via tools is not.

### "Schedule / publish"
- Scheduling = `update_post` with a time (respect the business's timezone).
- Scheduling to a platform the workspace has not connected (or whose token needs a
  reconnect) still succeeds, but the result carries `unconnected_platforms` + a `warning`
  — relay it verbatim: the publish will fail unless the user connects it in Integrations
  before the slot. `get_workspace.connected_platforms` tells you up front.
- `publish_post` posts publicly and irreversibly → echo exactly what will go out,
  where, and when, and get an explicit yes first. Same for `approve_post` when
  approvals are on: approving is a decision that belongs to the user.
- Once the org's due posts have scheduled generation working, the publisher picks up a
  `scheduled` post within ~15s of its slot — but only once the publisher process is live
  (`SCHEDULED_PUBLISH_MODE=publisher`). Until then the every-minute cron publishes within
  ~1 min, so a delay of a minute or two is normal; "why hasn't it published yet" a minute
  after the slot is a real problem once the publisher is live, not before. A post you
  reschedule or unschedule after the publisher has already picked it up for this tick is
  simply skipped by that tick, not double-published — the new time takes effect on the
  next sweep.
- Auto-generation for an org that's out of credits pauses for up to an hour (not forever) and
  resumes immediately the moment credits change (top-up, plan change, trial extension) — so
  "buy credits" is a real fix, not just advice, if that's what `generation_failed` turns out
  to be.

### "Remember that we never say X" / brand corrections
Durable facts → `create_memory`. Actual identity changes (voice, audience, banned
phrases) → the `update_brand_*` tools — but read `get_brand_profile` first and change
only the field in question; these tools overwrite.

## Gotchas (each one is a real observed failure)

| Trap | Rule |
|---|---|
| Empty "Characters" collection | A collection name is not evidence; list its items and check `ready` status before tagging or promising. |
| Wrong language | The brand's `language` field governs output language. Hebrew brand → Hebrew post, RTL-safe. Never default to English. |
| Generic content | If you didn't cite a memory/item/post in your grounding line, you probably invented something. Go back to Resolve. |
| No visuals exist | Many brands have zero collections. Say so and proceed with brand identity + logo — don't fake a reference or stall. |
| Gallery item in post text | Gallery items are for image/video/cover generation only; post-body and carousel generation reject them. |
| Tagging a gallery *collection* | Never taggable — tag its individual items. |
| Reference overflow | Collection/gallery tags spread into many images against a ~14-image model cap. Tag the few that matter. |
| Post idea vs social post | "The post failed" usually means ONE platform variant failed; check per-platform statuses in `get_post` before regenerating everything. |
| Publish ≠ schedule | Publishing is public and immediate. Never publish when asked to schedule; never publish without an explicit confirmation. |
| A hidden owner or place | `owner: hidden` or `place: hidden` means covers will never show them — don't tag that person or a `My business` location, and don't promise a photo of them. Say the rule is on and offer to change it with `update_photo_rules` if they ask. |
| Overwriting brand identity | `update_brand_*` tools replace fields. Read-modify-write, never write blind. |
