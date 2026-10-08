---
name: decktopus-presentation
description: Creates AI presentations and social carousels with Decktopus, and reports on the ones that already exist. Always generates the visual style first, then the deck, asks which organization workspace to use when the user belongs to one, confirms whether the style comes from a brand URL or a topic, and reports credit cost before generating. Also hands out per-audience share links and reads viewer analytics — who opened a deck, how long they stayed, which slide they stopped on. Use when the user asks for a presentation, deck, slides, pitch deck, slide design, or a LinkedIn/Instagram carousel, or asks who viewed a deck, how a deck is performing, where people drop off, or for a share link, or mentions Decktopus.
---

# Decktopus Presentation

Two different jobs live here. Decide which one the request is before touching a tool.

| Request | Go to |
|---|---|
| "Make me a deck / carousel / pitch" | [Making a deck](#making-a-deck) — style first, then deck |
| "Who viewed it?", "How did it do?", "Give me a share link" | [Sharing and analytics](#sharing-and-analytics) — no style, no credits |

## Making a deck

Every creation request is a two-phase job: **style first, then deck.**

- A **style** is the reusable visual identity (colors, fonts, logo, layout templates). It is generated once and can be reused for many decks.
- A **deck** is the slides rendered inside that style.

Never create a deck before a style exists and has finished generating.

### Tools

| Tool | Use |
|---|---|
| `list_organizations` | Workspaces the user can create in. Call first, always. |
| `check_ai_credits` | Workspace credit balance, cost per slide, how many slides they can afford. Call before generating a style or creating a deck. |
| `list_ai_deck_styles` | Existing finished styles. Only completed styles appear here. |
| `generate_ai_deck_style` | Create a style from a topic brief or a brand URL. Returns immediately. |
| `create_ai_deck` | Create the deck. Returns `deckId` + `shareUrl` once queued. |
| `get_ai_deck_status` | Poll render progress. |

Sharing and analytics have their own tools; the table is in [Sharing and analytics](#sharing-and-analytics).

If the Decktopus creation tools are unavailable, use the REST endpoints in [reference.md](reference.md). Analytics has no REST fallback.

### Workflow

Track progress against this checklist:

```
- [ ] 1. Intake: subject, audience, goal, length, language
- [ ] 2. Workspace: list_organizations, then ask
- [ ] 3. Format: presentation (default) or carousel
- [ ] 4. Credits: check_ai_credits, tell the user the balance and estimated cost
- [ ] 5. Style: confirm brand URL vs topic, then reuse or generate
- [ ] 6. Wait until the style is completed
- [ ] 7. create_ai_deck with styleSource "existing"
- [ ] 8. Poll get_ai_deck_status, hand over the shareUrl
```

#### Step 1: Intake

Ask for anything missing in **one** batched message, then stop asking. Needed:

- Subject and the single takeaway the audience should leave with
- Audience (investors, customers, students, team)
- Format and length
- Language, if not obvious from the conversation
- Brand: a company website URL, or a described look. The user must later know whether the style is from the URL or from a topic brief.

If the user gives a one-line request and clearly wants speed, make sensible assumptions, state them in one sentence, and proceed. Never block intake on brand details; confirm the style source in step 5 before generating.

#### Step 2: Workspace — always look up organizations

Call `list_organizations` before any create tool, once per session.

- **No active organizations** → use the personal workspace silently. Do not ask.
- **One or more active organizations** → ask which one, listing each organization by name plus a personal-workspace option. Ask even when there is exactly one; do not guess.
- Ignore organizations with `isActive: false`; they cannot be used.

```
Which workspace should I create this in?
1. Acme Inc (organization)
2. My personal workspace
```

Then pass the chosen `organizationId` to **every** later call in the session (`check_ai_credits`, `list_ai_deck_styles`, `generate_ai_deck_style`, `create_ai_deck`). Styles and credits are scoped per workspace: a personal style is invisible under an organization, and organization credits are spent instead of the user's own.

If a call fails with a no-access error, re-run `list_organizations` and re-ask instead of retrying the same id.

#### Step 3: Format

Default to `presentation`. Never silently produce a carousel.

| Format | Ratio | Typical length | Pick when |
|---|---|---|---|
| `presentation` | 16:9 | 8–15 slides | Default. Pitch, sales, training, report, webinar, class. |
| `carousel` | 4:5 vertical | 6–10 slides | LinkedIn/Instagram carousel, social post, "swipe", vertical, "for my feed". |

If the signals are mixed ("a deck for LinkedIn"), ask once with the two options.

The style and the deck must use the **same** format. A presentation style cannot be reused for a carousel — generate a carousel style instead.

#### Step 4: Credits — tell the user before spending

Call `check_ai_credits` with the chosen `organizationId`, the intended `resolution` (default `2K`), and `slideCount` when the length is known. Then **say the numbers out loud** before generating a style or creating a deck. Do not skip this, and do not invent a balance.

```
This workspace has 80 credits. At 2K that's 5 credits per slide, so about 55
credits for 11 slides (you can afford 16). Style generation is free, but the
workspace needs at least 5 credits available or the style stalls.
```

Use the values the tool returned — never hardcode per-slide cost.

- **`canGenerateStyle: false`** (not enough for even one slide) → stop. Do not call `generate_ai_deck_style` or `create_ai_deck`. Explain they need more credits, and that organization workspaces have a separate pool.
- **`hasEnoughCredits: false`** (they asked for more slides than they can afford) → warn and wait: offer a shorter deck at `affordableSlides`, a different workspace, or adding credits. Do not silently truncate.
- **Enough credits** → state the cost in one sentence and continue. Do not extra-confirm unless they asked.

If they later change slide count, resolution, or workspace, check again.

#### Step 5: Style — always before the deck

1. Call `list_ai_deck_styles` with the chosen `organizationId` and `format`. If matching styles exist, offer them by name alongside "generate a new one". Reuse is instant and keeps decks visually consistent. Reusing a style skips the source confirmation below.
2. **Name the source before generating.** Never silently pick brand URL vs topic. The user must know which path you are taking.

| Source | Tool args | What it does |
|---|---|---|
| Brand URL | `source: "url"`, `brandUrl` | Pulls the real logo, colors, and fonts from the website. More on-brand. |
| Topic | `source: "topic"`, `topic` | Invents a look from a **visual** brief (not a slide outline). Keep it under 50 words; anything longer is truncated. |

Say it in one sentence, then generate only when the source is explicit:

- They said to use the brand / website: *"I'll generate the style from https://acme.com so the deck uses the real logo, colors, and fonts."* Proceed.
- No site, or they described a vibe only: *"I'll generate a topic style from a visual brief (minimal fintech, navy and mint) — not from a brand website. Share a company URL if you want the real brand pulled in."* Proceed unless they want to wait for a URL.
- A URL or company is present but they have not chosen the source: ask once with the two options, then stop until they pick.

```
I'll generate the visual style in one of two ways:
1. From https://acme.com — real brand colors, logo, and fonts
2. From a described look I write (not pulled from a website)
Brand URL is more on-brand. Which do you want?
```

After they pick, echo it back when you start: *"Generating the style from acme.com…"* or *"Generating a topic style: …"*.

```
Good topic: "Fintech B2B SaaS, minimal and trustworthy: lots of white space,
deep navy and mint accents, clean geometric sans, subtle data visuals."

Bad topic: "Slide 1 intro, slide 2 market size, slide 3 our product..."
```

Always pass `format`, and pass a `name` that makes the style reusable later, such as `"Acme — Sales (presentation)"`.

On a free personal workspace only one generated style is allowed per source. If that error appears, offer to reuse the existing style or to create inside an organization.

#### Step 6: Wait for the style

`generate_ai_deck_style` returns a `styleId` with `status: "generating"`. Generation usually takes one to three minutes.

Poll `list_ai_deck_styles` (same `organizationId` and `format`) every 20–30 seconds until the `styleId` appears — that list contains only completed styles. Give up after about ten minutes.

Say what is happening between polls; do not go silent. If the style never appears, generation failed: offer a retry with a different brief or a brand URL.

`create_ai_deck` with `styleSource: "existing"` also waits for a still-generating style, so going straight to step 7 works. Prefer confirming completion first so a long tool call cannot time out.

#### Step 7: Create the deck

Call `create_ai_deck` with `styleSource: "existing"`, the confirmed `styleId`, the matching `format`, and the chosen `organizationId`.

- `prompt`: send the enriched brief from step 1, not the user's one-liner. Include audience, goal, tone, the narrative beats, and any real numbers or names the user gave. See [recipes.md](recipes.md) for templates.
- `slideCount`: omit or `"auto"` unless the user asked for a length. Range is 1–30.
- `language`: pass explicitly whenever the content language is anything other than obvious English.
- `resolution`: MCP defaults to `2K`. `1K` and `2K` cost the same; `4K` costs more and requires an `organizationId`.
- `fileUrls`: pass publicly accessible URLs (report, spreadsheet, PDF) to ground the content in real data instead of invented facts.

**Call `create_ai_deck` exactly once per deck.** If it times out or fails ambiguously, do not retry — poll `get_ai_deck_status` or ask the user. A retry spends credits again and creates a duplicate deck.

Share the returned `shareUrl` immediately. The deck opens right away and fills in as slides render.

#### Step 8: Poll and hand over

Call `get_ai_deck_status` with the `deckId` every 20–30 seconds, backing off to 60 seconds after five minutes. Stop when `isTerminal` is true.

- Report progress as slides land: `8/12 slides rendered`.
- On completion, lead with the link: `Deck ready — 12/12 slides: <shareUrl>`.
- If `slides.failed > 0`, say how many and note that individual slides can be regenerated in the editor.
- If `slides.total` is 0 and the status is `in_queue`, the deck is still queued — keep polling.

Rendering usually finishes within a few minutes, longer for big decks. Past about fifteen minutes, stop polling: hand over the `shareUrl` and explain that rendering continues in the background.

## Sharing and analytics

For a deck that **already exists**. No style step, no workspace question, no credits — these tools never spend any. Everything is addressed by `deckId`; the workspace is read off the deck itself.

### Tools

| Tool | Use |
|---|---|
| `list_ai_decks` | Turn a deck name into a `deckId`. Start here whenever the user names a deck instead of giving an id. |
| `list_ai_deck_share_links` | The deck's share URLs and their view counts. Creates the default link on first call. |
| `create_ai_deck_share_link` | An extra, separately tracked URL for one audience. |
| `update_ai_deck_share_link` | Rename a link, or revoke / re-enable it. |
| `delete_ai_deck_share_link` | Remove a link permanently. Confirm first. |
| `get_ai_deck_analytics` | Who opened the deck, for how long, and how far they read. |
| `get_ai_deck_viewer_analytics` | One viewer, visit by visit and slide by slide. |

Track progress against this checklist:

```
- [ ] 1. Deck: list_ai_decks with search, confirm the match before reporting numbers
- [ ] 2. Period: pick range / from-to / sinceLastEdit from what the user asked
- [ ] 3. get_ai_deck_analytics
- [ ] 4. Report it as a story: headline → viewers → drop-off
- [ ] 5. Drill in with get_ai_deck_viewer_analytics only when a person is asked about
```

### Step 1: Find the deck

Every tool here needs a `deckId`. If the user names a deck ("how did the Acme pitch do?"), call `list_ai_decks` with `search` and confirm the match by name before reporting any numbers — reporting the wrong deck's viewers is worse than asking.

- Two or more plausible matches → list them with their `updatedAt` and ask which one.
- No match → say so and offer to list recent decks without a search term. Never guess an id.
- Only AI Decks (nano-banana) have analytics. A deck from the classic editor is rejected with a clear error; do not retry it against another tool.

Reuse the `deckId` from `create_ai_deck` when the deck was made in this same session.

### Step 2: Share links

Every deck has one **default link**, materialized on the first `list_ai_deck_share_links` call. Extra links exist for one reason: attribution. A link's **name is the source label** in analytics, so name it after the audience — `"Investors"`, `"LinkedIn"`, `"Acme Corp"` — never `"Link 2"`.

| User wants | Do |
|---|---|
| A link to send | `list_ai_deck_share_links`, hand over the existing `shareUrl`. Do not create another. |
| To know where views came from | `create_ai_deck_share_link` per audience, hand each URL out separately. |
| To cut off access | `update_ai_deck_share_link` with `isActive: false`. The URL dies, past visits stay in analytics. Prefer this over deleting. |
| To rename an audience | `update_ai_deck_share_link` with `name`. Analytics relabels with it. |
| It gone for good | `delete_ai_deck_share_link` — **confirm first**, anyone holding the URL loses access. The default link cannot be deleted, only deactivated. |

The tracked URL is the one the share-link tools return (`/nano/<deckId>/present?code=…`). The `shareUrl` from `create_ai_deck` and the `editUrl` from `list_ai_decks` are editor deep links — opening those records nothing. If the user wants views counted, give them a share link.

Decktopus emails the deck owner the first time each new viewer opens a deck. That notification is already live and is not switched by a link's `emailOnFirstOpen` flag — the flag is stored for a future per-link setting. Never tell the user that toggling it turns notifications on or off.

### Step 3: Pull the numbers

Call `get_ai_deck_analytics` with the `deckId` plus whichever filters the question implies:

| The user asked | Pass |
|---|---|
| Nothing about time | Nothing — the period defaults to the last **14 days** |
| "today", "this week", "this month", "ever" | `range: "24h"` / `"7d"` / `"30d"` / `"all"` |
| A specific window | `from` / `to` as ISO 8601. These override `range`. |
| "since I changed it" | `sinceLastEdit: true` |
| About one audience | `linkId` from `list_ai_deck_share_links` |

Set `includeActivity: false` or `includeSlides: false` when the user only wants a headline; leave both on by default. `viewerLimit` defaults to 10 — raise it when they ask for the full list.

### Step 4: Report it like a person, not a JSON dump

Read the numbers back as a story, in this order:

1. **Headline** — unique viewers, total visits, average time per visit, and `visitTrendPercent` against the previous period of the same length.
2. **Who** — the viewers who matter, identified ones (with an email) first: how long they spent and when they were last seen.
3. **Drop-off** — where `seenPercent` falls off is where people leave; a high `avgDwellSeconds` is where they linger. Name the slide numbers.

Rules that keep the report honest:

- **All zeros means nobody opened it in that period.** Say that plainly and offer a wider `range`. Never dress it up as a tracking problem.
- Viewers who never identified themselves are `Anonymous #n` with no email. That is normal, not missing data.
- `source` is the share link name, else a UTM source, else `Direct`.
- Round times into human units ("about 4 minutes"), and never invent a viewer, an email, or a number that no tool returned.

Templates for the write-up are in [recipes.md](recipes.md).

### Step 5: One viewer

Call `get_ai_deck_viewer_analytics` with the `deckId` and a `viewerId` from the analytics response — only when the user asks about a specific person. It takes the same period and `linkId` filters, and returns every visit with per-slide dwell time and `exitedOnSlideNumber`.

Use it to answer "what did they actually read" and "where did they stop". Do not run it over every viewer in a loop to build a summary; the deck-level response already carries the aggregate.

Viewer detail is personal data about a named individual. Report what the tools return, and leave motive out of it — say "they spent 3 minutes on the pricing slide", not "they are hesitating about price".

## Guardrails

- Never invent a `styleId`, `deckId`, or `shareUrl`. Only use values a tool returned.
- Credits are spent per rendered slide. Always call `check_ai_credits` and tell the user the balance and estimated cost before generating a style or creating a deck. Style generation itself costs nothing, but the workspace still needs at least one slide's worth of credits or the style stalls. Create one style and one deck per request unless asked for more.
- Never start `generate_ai_deck_style` without the user knowing whether it is a **brand URL** style or a **topic** style.
- Do not switch workspace, format, or style mid-flow without saying so.
- Never invent a viewer, an email, a view count, or a share URL. Every number reported comes from a tool response.
- Confirm before `delete_ai_deck_share_link`; it breaks the URL for everyone holding it. Deactivating is the reversible option.
- Always say which period the numbers cover. Analytics defaults to the last 14 days, so an unqualified "3 viewers" is misleading on an older deck.
- Translate errors into plain language plus a concrete next step. Error table is in [reference.md](reference.md).

## Additional resources

- Tool schemas, enums, statuses, error handling, REST fallback → [reference.md](reference.md)
- Prompt and style templates per deck type, carousel recipes, analytics write-up templates → [recipes.md](recipes.md)
