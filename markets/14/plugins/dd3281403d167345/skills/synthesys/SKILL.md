---
name: synthesys-video-production
description: "Produce finished AI videos with the Synthesys MCP tools: pick the right template, write briefs that make good ads, quote costs before spending, poll at the right cadence, and handle the build agent's questions. Use whenever the user wants a video — an ad, product clip, UGC-style creator video, faceless story, explainer, sales video, animated story ad, an ad recreated from a competitor's link or a product page, or a restyle of their own footage — and the Synthesys connector is connected. Also use when the user asks what videos Synthesys can make or what one would cost."
---

# Synthesys video production

You have access to Synthesys — an AI video production agent — through its MCP tools. Synthesys doesn't just
generate clips: from one brief it scripts, casts, voices, scores and composites a finished
multi-scene video. Your job is to be a good producer: pick the right format, feed it a strong
brief, keep the user in charge of money, and be patient while it renders.

## The fifteen tools at a glance

| Tool | Cost | Use it to |
|---|---|---|
| `list_templates` | free | See every template + style, duration clamps, aspect ratios |
| `get_credits` | free | Balance, price list, today's remaining limit (100 credits = $1) |
| `generate_clip` | **paid** (quote-first with a `model`) | ONE short clip (4–15 s) from a prompt (8–13 min render) |
| `create_video` | **paid, quote-first** | A full multi-scene production (usually a 10–25 min build) |
| `recreate_from_url` | **10-credit** analysis · render **quote-first** | Recreate a specific existing ad from its link — or build an ad from a product page |
| `get_video_status` | free | Poll a build; get the quote, questions, and the final URL |
| `answer_question` | free | Reply when the build agent asks something mid-run |
| `upload_reference` | free | Ingest the user's images/videos by URL for the build |
| `list_files` | free | Browse the images/videos already in the user's Synthesys library |
| `create_upload_link` | free | A page where the user adds a file from their own device |
| `list_actors` | free | The people who can be on camera — the user's twins, then stock actors |
| `list_voices` | free | The narrator voices — the user's own, then the library |
| `list_brand_kits` | free | The user's Brand Kits (logo, colours, fonts, tagline) |
| `list_models` | free | The image or video models, what each offers, and its exact price |
| `generate_image` | **paid, quote-first** (exact) | Generate or edit an image with a chosen model |

## The core workflow

1. **Understand the ask.** Product/topic, audience, platform (drives aspect ratio), target
   length, tone, anything that must be said or shown.
2. **`list_templates`** — always, before any paid call. Pick the template whose positioning
   matches (guide below); respect its `max_duration_seconds` and default aspect.
3. **Gather the real assets.** If the video is about the USER'S product or brand, get a product
   image, logo, or footage first and collect the `asset_url`s. Three ways, pick by where the
   file is:
   - **At a public link** → `upload_reference` each URL. Always ingest through it rather than
     pasting a raw link into `reference_asset_urls`: that call is where Synthesys determines
     whether the file is an image or a video (a link it can't classify is attached as unknown and
     may be ignored, with a warning).
   - **Already in Synthesys** ("it's in my library", "the one I uploaded") → `list_files`.
   - **On their device, or attached in this chat** → `create_upload_link`. **A file attached in
     the chat does not reach Synthesys** — you can see it, the tools cannot. Give the user the
     `upload_url`, wait for them to say it's uploaded, then `list_files` (newest first).
   **Never invent a brand name, product label, or claim.** If no image and no concrete
   description exists, ask for one before building.
4. **`get_credits`** — check the balance (and `remaining_today`, when the account has a daily
   limit) so you can warn before quoting something unaffordable.
5. **Build:**
   - Quick single shot → `generate_clip`.
   - Anything with scenes, voiceover, captions, or music → `create_video` (two calls: quote,
     then confirm).
6. **Poll `get_video_status`** at the documented cadence until `complete`, then deliver
   `video_url` with a one-line description of what was made.

## Casting, voice and brand (optional picks)

Synthesys casts a presenter, picks a narrator and builds without a brand unless told otherwise —
so only reach for these when the user cares.

- **Who is on camera** → `list_actors`, show a few (name, plus `preview_url` for stock actors), pass
  the chosen `actor_id` to `create_video`. `my_twin` entries are the user's own recorded twin —
  listed by name only (no picture of their face is shared); offer those first when they want to
  appear themselves. Not with `no_people`.
- **Who narrates** → `list_voices` (each has an audio `preview_url`), pass `voice_id`.
  `my_voice` entries are voices the user cloned. Voices they made for Studio speak only there, so
  they are not listed and can't narrate a video.
- **On-brand** → `list_brand_kits`, pass `brand_kit_id`: the video closes on the brand's end card
  and follows its colours, fonts, tagline and call to action. A Brand Kit can only be attached
  when the video is created, never to a finished one. If it answers `available: false`, Brand
  Kit isn't on the user's plan — say so and build without it.

An id that isn't from these lists is refused before anything is created, so nothing is wasted.

## Images and choosing a model

- **An image** (a product shot, a scene, a thumbnail, an edit of the user's photo) →
  `generate_image`. It is two calls like `create_video`: the first returns the exact price and a
  `quote_id` and spends nothing; after an explicit yes, call again with the same inputs plus
  `confirm: true`, that `quote_id` and `quoted_credits` (the price you showed). The charge is
  exactly that price, and an image that fails costs nothing. One quote pays for ONE press: if the
  confirm errors or times out, call again with the SAME `quote_id` (it returns that press, never a
  second charge) — never ask for a new quote to retry. Every image lands in the user's library, so its `asset_url` can feed
  `create_video` — "make a product shot, then build the ad around it" is two tools, not a dead end.
- **"Which models are there?" / "use the best one" / "what does it cost?"** → `list_models` with
  `category` `image` or `video`. Show name, maker and the credits for the settings the user wants.
  Do not guess a model name — pass a `model_id` from the list, or omit `model` for the default.
- **A clip from a specific model** → `generate_clip` with `model`. That path is quote-first too
  (the plain template clip is not): quote, yes, then `confirm: true` with the `quote_id` and
  `quoted_credits` — the same retry rule applies. Use `start_frame_url` to animate a picture.
- If a confirm comes back `quote_changed`, the quote no longer matches (other settings, a new
  price, or it expired after 30 minutes) — nothing was charged. Show the new price and, on a yes,
  confirm with the new `quote_id` it returns.
- Full productions (`create_video`) pick their own models; do not offer a model choice there.

## Clip, production, or recreate?

- **`generate_clip`** — one continuous shot, no voiceover, 4–15 s: product beauty shots,
  b-roll, a cinematic mood piece. Without a `model` it starts spending immediately (that is its
  point), so state the approximate cost BEFORE calling it: ~40–50 credits/second at default quality, about 200
  for 4 s (the response also returns `approx_cost_credits`). If the user gave a budget, check it fits. Tell
  them it takes **8–13 minutes**. It takes `reference_asset_urls` too (the user's product shot),
  and its default template is product-only — pass `no_people: true` when the user wants nobody
  on camera.
- **`recreate_from_url`** — the user points at a SPECIFIC existing ad ("make me this, but for
  my product", a competitor link, a TikTok that's winning), or at their PRODUCT PAGE ("make an
  ad from this listing" → `mode: "page"`). Synthesys watches the real creative and
  copies what works — its hook, beat structure, pacing — instead of guessing from a
  description, so prefer it over `create_video` whenever a link (or video file URL) to the
  ad exists. Details below.
- **`create_video`** — everything else: the user describes what they want from scratch. It is
  structurally safe: the first call only plans (free) and returns a quote; nothing renders
  until you confirm.

## Recreating an existing ad (`recreate_from_url`)

1. Get the **link**: a direct video file (.mp4/.mov/.webm) works everywhere; ad pages and
   TikTok/Meta/YouTube links usually resolve. If resolution fails, the error says what to do —
   usually "get a direct video link or the file". A file the user has locally can be hosted
   anywhere public, or ingested via `upload_reference` first and the resulting `asset_url`
   passed as the `url`. For a **product / landing / app-store page** pass `mode: "page"`: the
   real photos, copy and product facts are captured and an ad is planned for that product.
2. Ask what to **adapt** — their product, brand, offer — and pass it as `notes`
   ("sell our espresso maker instead, keep the pacing"). Without notes Synthesys adapts to the
   account's default Brand Kit.
3. **Tell the user the analysis costs 10 credits (~$0.10)** — it is charged when the analysis
   completes (a refused or failed one costs nothing) — and that it takes a few minutes: the ad is
   downloaded, transcribed, and analyzed beat-by-beat before the plan comes back. Then call
   `recreate_from_url` ONCE and wait; never re-send the same link while it runs (a duplicate is
   refused, and re-sending after it finished pays for a second analysis).
4. The response is a producer's gift — show it: `ad_analysis` (hook, labeled beats, pacing,
   why it wins) explains WHAT the reference does — or, for a page, what was captured — and the
   quote prices the render. The original stays reference-only: Synthesys rebuilds the structure
   for the user's brand, it never splices the competitor's footage in.
5. Money etiquette is identical to `create_video`: show the quote, get an explicit yes, then
   confirm with `create_video {project_id, confirm: true}` and poll. Recreates follow the
   reference clip's length (capped at 60 s).

## Money etiquette (non-negotiable)

- **Always show the quote and get an explicit yes** before calling
  `create_video {project_id, confirm: true}`. Present it plainly: "4 scenes, ~30 s,
  1,040 credits ≈ $10.40 — build it?" Never treat the original request as pre-approval; never
  confirm on your own judgment.
- **`confirm` is the user's decision, not your bookkeeping.** `confirm: true` is the ONLY input
  that spends. If they say no, send `create_video {project_id, confirm: false}` — that declines
  the pending step and spends nothing. If you just want to know where a build is, call
  `create_video {project_id}` with no `confirm` (a read-only status check) or, better,
  `get_video_status`.
- If the quote exceeds the balance (the quote carries a `balance_warning`), say so and stop —
  the account's plan and credits are managed at app.synthesys.io, not through you. Say that
  plainly; never tell the user to buy, upgrade or top up.
- The account may have a **daily limit** for assistant/API spending (`get_credits` shows
  `daily_cap`, `spent_today`, `remaining_today`; credits reserved by runs still in progress count
  too). A quote over what is left carries a `daily_cap_warning` — relay it before asking for a yes:
  an image or a model clip over the limit is refused whole (nothing charged), and a production may
  be refused at the confirm or at a later approval until 00:00 UTC. A refusal for the limit says so
  plainly; relay it and do not retry before the reset.
- Other refusals say what to do: not enough credits → say the balance won't cover it and that the
  plan and credits are managed in the Synthesys app; too many videos building at once → wait for one to finish (adding
  credits won't help). Nothing is charged for a refusal.
- If a confirm comes back `gate_changed`, the step changed (or got pricier) before your yes
  landed — nothing was approved. Show the user the new step and ask again.
- **A cost quote covers the production it prices** — approve one (`awaiting_confirmation`) and
  the remaining paid steps of that build run without gating. That's why the yes must be
  explicit.
- **Not every pause is a bill.** `awaiting_review` (an artifact — creator portrait, storyboard
  sheet, deck — waiting to be looked at) and `awaiting_approval` (a step with no price quoted)
  cost nothing, and approving them does NOT unlock the budget: the build still stops at the
  next paid step with its own quote. Check `pending_approval.is_cost_quote` before you tell the
  user a number, show `pending_approval.artifact_url` when there is one, and confirm/decline
  them the same way (`confirm: true` / `confirm: false`).
- **Free settings are handled for you.** When the brief itself asks for a setting ("no
  voiceover", a caption style), Synthesys applies it and the quote you get back is the real
  price; `applied_free_settings` lists what was applied. You do not confirm those.
- When a build is `complete`, `spend` says what it actually cost — mention it when you deliver.

## Choosing the template

Match the *feel* the user asks for, not just the subject:

| They want | Template | Notes |
|---|---|---|
| Authentic creator/selfie ad, "filmed on a phone", testimonial, unboxing, GRWM | `ugc-ad` | 9:16, ≤30 s. Deliberately raw — do not ask Synthesys to polish it. Always casts a creator |
| A cinematic, high-end brand or product film | `commercials-ad` | Polished, camera-language-driven, minimal text. Product-only (no people) unless an actor is asked for. Also the default for `generate_clip` |
| Narrated story over fast b-roll, no one on camera | `faceless-story` | Viral story/documentary shorts, ~30–60 s vertical |
| A presenter pitching an app/SaaS to camera | `app-promo` | Premium-minimal captions and app-screen cutaways |
| A direct-response sales video / VSL | `sales` | 1–3 min, presenter + b-roll + offer graphics |
| An animated, character-driven story ad | `animation-story-ad` | 3D-cartoon short film with an emotional arc; 40 s–3 min |
| Presenter + slide deck (webinar, pitch, training) | `presentation` | Long-form, one presenter narrating designed slides |
| A person teaching to camera intercut with b-roll | `educational` | How-to / explainer; can feature the user's own footage |
| Their OWN clip restyled / captioned / remixed | `restyle` | `create_video` only (it quotes first): upload the clip (≤2 min) with `upload_reference` and pass its `asset_url` in `reference_asset_urls` — without a video the call is refused. `styled-short` is made in the Synthesys app: it has no price to approve, so the tools refuse it |

The live catalog from `list_templates` is the source of truth — templates gain styles and new
keys over time. When several fit, say which you picked and why in one sentence; when none
clearly fits, omit `template` and let Synthesys auto-route the brief.

**No people on camera?** Use `commercials-ad` (or `faceless-story` for narrated stories) and pass
`no_people: true` — nothing human appears then, hands included (without it, a product-only
commercial may still show hands). `ugc-ad`, `presentation`, `educational`, `avatar-short`,
`app-promo`, `animation-story-ad`, `sales`, `whiteboard`, `interview` and `podcast` always put a
person on camera, so the tools refuse `no_people` with them.

## Writing briefs that produce good videos

A strong brief is concrete and short — a paragraph, not a script (Synthesys writes the script):

- **Name the product and what it does** in plain words, plus the audience and the ONE feeling
  or claim the video should land.
- **Give the hook** if the user has one ("hook: 3am doomscrolling"); otherwise ask for — or
  propose — one. The first two seconds decide everything on social.
- **State duration and format explicitly** ("Duration: 20 seconds. Format: 9:16.") — the
  planner honors these tokens, and `duration_seconds` / `aspect_ratio` args reinforce them.
  Supported aspects: 16:9, 9:16, 1:1, 4:5, 21:9, 9:21, 4:3, 3:4. Results echo the
  `aspect_ratio` the project actually uses — check it matches what the user asked for.
- **Name a style when the template has a catalog**: pick from `list_templates` and write
  "Style: <style name>" in the brief.
- **Point at the references**: pass `asset_url`s in `reference_asset_urls` AND say what each is
  in the brief ("the attached photo is the product — keep its label exact").
- **Carry the user's voice**: must-say lines verbatim, banned words, tone ("casual, no
  ad-speak"). For UGC-style ads, real beats polished: conversational lines sell better than
  slogans.
- Don't over-specify camera work or scene counts — that's Synthesys's craft. Trust the template.

## Polling discipline

- Clips: poll `get_video_status` every **30–60 s**; typical total **8–13 min**.
- Productions: poll every **30–60 s**; usually **10–25 min** in total. **Do not give up before
  30 minutes**, and don't poll faster — it won't speed anything up and can hit rate limits
  (a 429 tells you to wait ~60 s).
- Tell the user the expected wait when the build starts, and give a progress touch when
  something changes (`scenes.rendered` climbing is your progress bar).
- Polling is safe and read-only (it never starts or resumes anything; Synthesys resumes an
  interrupted build on its own). When in doubt, poll — never start a duplicate build because a
  poll looked slow.
- **Never re-send a brief after an error that names a `project_id`.** If `create_video` or
  `recreate_from_url` fails once the project exists, the error says so and gives you the id —
  the build is already running server-side. Poll that id; retrying makes a second project (and
  re-runs a finished ad ingest).

## When the build agent asks a question

`state: "awaiting_answer"` means the build is paused on a real clarification (e.g. which
product variant to feature). **Relay the question to the user verbatim** (with its options, if
any), send their reply via `answer_question`, and resume polling. Use `skip: true` only when
the user has told you to let Synthesys decide. If the question changed before the answer
landed, the result is `question_changed` with the NEW question — the answer was not sent; relay
the new question and answer that one.

## Delivering

When `state` is `"complete"`, share `video_url` directly with one line on what was made
("20 s UGC-style ad, 9:16, creator testimonial with your product shots — 699 credits"). Offer the natural
next steps: a variation, a different aspect for another platform, or a restyle. If `state` is
`"error"`, relay the reason, and retry with a fresh `create_video` only if the user wants to.

## If the tools are missing or failing

- No Synthesys tools listed → the connector isn't connected; point the user to
  https://synthesys.io/mcp/ for the one-minute setup (add the Synthesys MCP URL and sign in —
  nothing to install).
- Every call returns 401 → the sign-in expired or the API key is missing/revoked; the error
  text says which fix applies (keys are created at app.synthesys.io). Never ask the user to
  paste a key into chat.
