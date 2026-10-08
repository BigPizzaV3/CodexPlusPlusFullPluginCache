# Recipes

## Deck prompt template

Send this as `create_ai_deck.prompt`. It reliably beats forwarding the user's one-liner.

```
<Subject>, for <audience>.
Goal: <the one thing the audience should do or believe afterwards>.
Tone: <confident / warm / academic / playful>.
Cover the following, in order: <beat 1>, <beat 2>, <beat 3>, …
Use these facts verbatim where relevant: <numbers, names, quotes the user gave>.
Close with: <call to action>.
```

Rules: keep every fact the user supplied, never invent numbers or customer names, and drop the beats section when the user wants the narrative decided for them.

## Style source

Before `generate_ai_deck_style`, say whether this is a **brand URL** style or a **topic** style. Never silently pick.

- Brand URL: `source: "url"`, `brandUrl` — real logo, colors, fonts from the site.
- Topic: `source: "topic"`, `topic` — invented look from the visual brief below.

If a company site is available and they have not chosen, ask once. Echo the source when generation starts.

## Style topic template

Send this as `generate_ai_deck_style.topic`. Describe the **look**, never the slide order. Stay under 50 words.

```
<industry / product domain>, <2–3 vibe words>: <background and color direction>,
<type direction>, <decoration or imagery direction>.
```

| Vibe asked for | Topic wording that produces it |
|---|---|
| Minimal | `lots of white space, restrained decoration, clean hierarchy, few elements` |
| Bold | `strong contrast, confident large type, impactful shapes, high visual energy` |
| Dark | `deep near-black backgrounds, light text, premium low-light palette` |
| Colorful | `rich multi-color palette, playful accents, vibrant blocks and shapes` |
| Corporate | `restrained corporate palette, structured grid, muted charts, no gradients` |
| Editorial | `magazine layout, large serif headlines, generous margins, photo-led` |

Fold explicit brand colors into the same sentence: `deep navy #0B1F3B with mint #4FD1A5 accents`.

## Deck type presets

| Ask | Format | slideCount | Prompt emphasis |
|---|---|---|---|
| Investor pitch | presentation | 10–12 | Problem, market size, product, traction, business model, team, ask. Numbers on every claim. |
| Sales / proposal | presentation | 8–10 | Customer's pain first, solution, proof, pricing, next step. Second-person voice. |
| Training / course | presentation | 12–20 | Learning objectives up front, one concept per slide, recap at the end. |
| Quarterly review | presentation | 8–12 | Results against targets, what moved, risks, next quarter's plan. Data-heavy. |
| Webinar / talk | presentation | 15–25 | Narrative arc, sparse text per slide, memorable closing slide. |
| Conference keynote | presentation | 20–30 | One idea per slide, very large type, image-led. |
| LinkedIn carousel | carousel | 7–9 | Hook on slide 1, one insight per slide, CTA on the last. Short lines. |
| Instagram carousel | carousel | 6–8 | Visual hook, minimal text, punchy, emoji-free unless asked. |
| Product update | presentation | 6–8 | What shipped, why it matters, screenshots, how to start. |

## Carousel specifics

- Vertical 4:5. Text must survive a phone screen: aim for headline plus one short line per slide.
- Structure: hook → payoff promise → one point per slide → call to action.
- Generate a dedicated carousel-format style. A presentation style's layouts are built for 16:9 and crop badly.
- Say so in the prompt: `Format as a vertical social carousel: bold hook, one idea per slide, minimal text.`

## Grounding in real content

When the user has a source document, pass `fileUrls` so the deck cites their real data instead of plausible-sounding invention.

- The URLs must be publicly reachable without a login; a Google Drive "anyone with the link" export URL works, a private SharePoint link does not.
- Say in the prompt what the file is for: `Base the market and revenue figures on the attached Q3 report; do not estimate.`
- Ingestion adds roughly a minute before the plan is written.

## Reusing styles

The style is the slow artifact; reusing one skips the one-to-three-minute wait and keeps every deck in a workspace consistent. Once a workspace has a good style, offer it for every later deck:

> You already have "Acme — Sales (presentation)". I'll reuse it, so this deck stays on brand and starts rendering right away.

Naming convention that keeps `list_ai_deck_styles` readable: `<Brand or subject> — <use case> (<format>)`.

## Deck follow-up requests

| User says | Do |
|---|---|
| "Make it longer / shorter" | New `create_ai_deck` with the same `styleId` and a new `slideCount`. Slide count cannot be changed on an existing deck. |
| "Same look, different topic" | Reuse the `styleId`, new `prompt`. |
| "Change the colors" | Generate a new style; a style's palette is fixed once rendered. |
| "Fix slide 4" | Per-slide edits live in the Decktopus editor. Send the `shareUrl` and say what to click. |
| "Also as a carousel" | New carousel-format style, then a new deck with the carousel prompt shape. |
| "Export to PowerPoint" | Available from the editor at the `shareUrl`. |

## Worked example — creation

User: *"I need a pitch deck for Acme, we're at acme.com, raising a seed round."*

```
1. list_organizations
   → { count: 1, organizations: [{ id: 42, name: "Acme Inc", isActive: true }] }
2. Ask: "Acme Inc, or your personal workspace?" → Acme Inc (organizationId 42)
3. Format: presentation (default; nothing suggests a carousel)
4. check_ai_credits { organizationId: 42, resolution: "2K", slideCount: 11 }
   → tell the user the balance, per-slide cost, and estimated total
5. list_ai_deck_styles { organizationId: 42, format: "presentation" } → count 0
6. Ask: "I'll generate the style from acme.com (real brand), or from a visual brief. Which do you want?"
   → brand URL
7. generate_ai_deck_style {
     source: "url", brandUrl: "https://acme.com",
     name: "Acme — Pitch (presentation)", organizationId: 42, format: "presentation"
   } → styleId
8. Poll list_ai_deck_styles every 25s until that styleId appears
9. create_ai_deck {
     prompt: "<pitch template, seed round, investor audience>",
     styleSource: "existing", styleId, format: "presentation",
     slideCount: 11, organizationId: 42
   } → deckId, shareUrl
10. Poll get_ai_deck_status until isTerminal, then:
    "Deck ready — 11/11 slides: <shareUrl>"
```

## Reporting analytics

`get_ai_deck_analytics` returns more than anyone wants read aloud. Compress it into three beats.

```
<Deck name>, last <period>: <uniqueViewers> viewers, <totalVisits> visits,
averaging <avgTimePerVisitSeconds as minutes> each — <up/down X%> on the period before.

Who: <name or email> (<visits> visits, <total time>, last seen <when>),
<name> (…), plus <n> anonymous viewers.

Where they stop: everyone reaches slide <n>, <seenPercent>% get to slide <m>,
and the deck loses them at slide <k> ("<title>"). Slide <j> ("<title>") holds
attention longest at <avgDwellSeconds>s.
```

Rules: minutes not seconds for anything over 90s, name slides by number **and** title, and never editorialize a viewer's motive — report the dwell time, not what it supposedly means about them.

### The empty case

```
Nobody has opened "Acme — Seed round" in the last 14 days. Want me to check
all time instead, or is the link still sitting unsent?
```

Say it in one line and offer a wider `range`. Do not explain tracking, do not apologize, do not speculate about broken analytics.

### Question → call

| User asks | Call |
|---|---|
| "Did anyone look at it?" | `get_ai_deck_analytics` — default 14d, lead with `uniqueViewers`. |
| "Who viewed it?" | Same, then read `viewers.items`. Raise `viewerLimit` if they want everyone. |
| "How did it do this week / today?" | `range: "7d"` / `"24h"`. |
| "Has anyone ever opened it?" | `range: "all"`. |
| "Where do people drop off?" | Same call, read `slides` — the `seenPercent` cliff. |
| "Did the investors see it?" | `linkId` of the Investors link, so other audiences do not muddy it. |
| "Is the new version doing better?" | `sinceLastEdit: true`. |
| "What did Dana read?" | `get_ai_deck_viewer_analytics` with Dana's `viewerId`. |
| "Just the headline" | `includeActivity: false, includeSlides: false`. |

## Share links per audience

One link per audience is what makes "where did the views come from" answerable. Name the link after the audience, because the name **is** the source label in analytics.

```
Good: "Investors", "LinkedIn post", "Acme Corp", "Warm intros — March"
Bad:  "Link 2", "Copy", "New link", "test"
```

Recipe when the user is about to send a deck to several groups:

1. `list_ai_deck_share_links` — the default link already exists; use it for the largest or catch-all audience.
2. `create_ai_deck_share_link` once per remaining audience.
3. Hand the URLs over labelled, one line each, and say explicitly that each one is tracked separately.
4. Later, `get_ai_deck_analytics` with that link's `linkId` answers per-audience questions.

```
Here are three tracked links for the same deck:
- Investors → https://…/present?code=abc123
- LinkedIn  → https://…/present?code=def456
- Acme Corp → https://…/present?code=ghi789
Views through each are counted separately, so I can tell you later which audience actually read it.
```

Revoking beats deleting: `isActive: false` kills the URL and keeps the history. Delete only when the user asks for it outright, and confirm first.

## Analytics follow-up requests

| User says | Do |
|---|---|
| "Send them a reminder" | Out of scope — no email tool here. Give them the viewer list and the share URL to send themselves. |
| "Stop that person seeing it" | Links are per audience, not per person. Deactivate the link they were given and issue a fresh one to everyone else. |
| "Why is this viewer anonymous?" | They never entered an email in the deck. Not fixable retroactively. |
| "Two viewers look like the same person" | Likely one person on two devices or browsers — viewers are per browser until they identify themselves. Say so rather than merging them yourself. |
| "Export this" | No export tool. Offer the numbers as a table in chat, or point at the analytics screen in Decktopus. |
| "Why does the count differ from the editor?" | Check the period — the tools default to 14 days, the screen may be showing all time. |

## Worked example — analytics

User: *"Did anyone actually read the Acme pitch I sent the investors?"*

```
1. list_ai_decks { search: "Acme" }
   → { deckId: 987, name: "Acme — Seed round", updatedAt: … }   confirm the name back
2. list_ai_deck_share_links { deckId: 987 }
   → default link + "Investors" link (id inv-uuid)
3. get_ai_deck_analytics { deckId: 987, linkId: "inv-uuid", range: "30d" }
   → 6 viewers, 9 visits, avg 3m 40s, +50% on the previous 30 days
4. Report: headline, then the four identified viewers, then the slide-8 drop-off
5. User: "what did dana@acme.com do?"
   get_ai_deck_viewer_analytics { deckId: 987, viewerId: "…" }
   → 3 visits, longest 6m, exited on slide 11 both recent times
```
