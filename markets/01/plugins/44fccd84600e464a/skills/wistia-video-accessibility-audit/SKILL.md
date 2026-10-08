---
name: wistia-video-accessibility-audit
description: Audit a Wistia account's most-seen videos for accessibility — captions, multi-language subtitles, AI dubbing, and audio descriptions — using the account's own audience data, and report the gaps ranked by audience impact. Use when the user asks for an accessibility audit, caption/subtitle coverage check, or wants to find accessibility gaps in their Wistia videos.
author: Wistia
version: 1.0.0
---

# Wistia Video Accessibility Audit

A portable AI skill that audits a Wistia account's most-seen videos for accessibility — captions, multi-language subtitles, AI dubbing, and audio descriptions — using the account's own audience data, and reports the gaps ranked by audience impact.

**Works with any LLM that supports the Wistia MCP connector** (Claude, ChatGPT, Cursor, or any MCP-capable client). To use: connect the Wistia MCP, then paste this file as a system prompt, project instructions, custom agent instructions, or install it as a skill. No other dependencies.

---

## First run — welcome message

If this is the user's first audit (no saved site profile from a previous run), greet them with this message verbatim and wait for answers:

> 👋 **Welcome to Wistia's Video Accessibility Audit**
>
> In Wistia's 2026 State of Video report, **71% of teams caption their videos — but only 23% subtitle in multiple languages**, leaving most audiences behind. This skill finds your most-seen videos and spots the caption, dubbing, and audio description gaps using your own audience data.
>
> Two quick things before your first audit:
>
> 1. **What's your website URL?** (e.g. yourcompany.com — so I can tell your pages apart from third-party embeds and group videos by the pages they live on)
> 2. **Any pages you'd call high-value?** (homepage, product, pricing — or just say "you pick" and I'll use traffic + common patterns)

Remember the answers (save to a state file if your environment supports files; otherwise carry them in conversation) so they're never asked twice. Use the domain for the owned-page rule below.

## Why this matters (context for the output)

- 71% of teams add closed captions; 69% use AI captioning; 36% add on-screen transcripts; only 23% add subtitles in multiple languages (Wistia 2026 State of Video).
- Top localization languages, in order: Spanish, French, German, Japanese, Portuguese.
- AI users are 50% more likely to use audio descriptions; the European Accessibility Act is raising the legal stakes.
- Captions also drive engagement (sound-off viewing) and SEO (transcripts are indexable).

## Workflow

### 1. Scope: top videos by impressions

Rank by **impressions (player loads), not plays** — accessibility is about who *sees* the player, and a homepage video with a 2% play rate can have 30× more impressions than plays.

- Call `show-account-top-content` (trailing 30 days, `sort_by: plays`, `per_page: 100`, `group_by: media`) — each record includes **`unique_loads`**. Re-rank by that locally and take the top 20. (The API can't sort by loads; the wide pull guards against high-load/low-play videos hiding below the plays cutoff.)
- Filter out test/synthetic media (names containing: synthetic, playwright, test, "don't delete").

### 2. Exclude videos with no speech

Silent loops can't be captioned or dubbed; including them creates false "missing captions" alarms. There's no has-audio flag in the API, so detect in layers:

1. **Has caption tracks → has speech.** Include.
2. **No captions + loop signals → assume silent. Exclude.** Signals: name or folder/subfolder/section contains loop/looping/header/banner/b-roll/time lapse/montage/background (check via `get-medias` with `hashed_ids` — the `subfolder.name` field is often the giveaway, e.g. "Home Looping Videos"), or duration under ~10 seconds.
3. **No captions + no loop signals → ambiguous. Don't guess** — ask the user to confirm with a quick listen before scoring it as a caption gap.

### 3. Find each video's hosting page

- Per video: `show-media-embed-locations` (**trailing ~90-day window** — longer ranges can return empty) → `embed_url`, `page_title`, plays per page. Skip localhost, `127.0.0.1`, `*.vercel.app`, staging/preview domains, and the Wistia app itself.
- **Only include videos hosted on a page the user controls** (matching their website domain). Videos with no embeds or only third-party/customer embeds are excluded from the tables — but if one carries a big insight (high impressions, big language gap), mention it in one line below the tables.

### 4. Pull accessibility status per video

| Check | Tool | Extract |
|---|---|---|
| Captions + languages | `get-captions` with `media_id` | language per track only — **ignore the `text` field** |
| Dubbed versions | `gets-localizations` | language, enabled |
| Player settings | `show-accessibility-customizations` | captions on, audio description control, extended audio description |
| Audience language demand | `show-media-languages` (trailing ~6 months) | viewer language, % of plays, `captions_support` flag |

Account-wide, once: `get-media-extended-audio-descriptions` (`per_page: 100`) → which media have audio description tracks.

A video's **uncovered languages** = viewer browser languages ≥2% of plays with no matching caption track or dub. If `captions_support: false` for a language (e.g. Chinese), captions can't cover it — dubbing is the only fix; say so.

### 5. Deliver in chat

Markdown tables directly in the chat response — no HTML file, no Slack formatting.

- **Group by page type** of the hosting page, one small table per group with a bold heading: Homepage, Product pages, Demo, Learn, Explore, Series (adapt groups to the site's actual structure).
- **Columns**: Video | Hosted on | Impressions (30d) | Captions | Dub | Audio desc. | Uncovered languages (with percentages, ⚠️ for big gaps)
- **Both link columns clickable**: Video → its Wistia media page (`https://<account-subdomain>.wistia.com/medias/<hashed_id>`; get the account URL from `get-current-account`); Hosted on → the full page URL (display without the scheme).
- Fully covered videos still get listed — they show the playbook works.
- **Summary line below the tables**: totals for gaps found (videos missing captions, uncovered languages, missing audio descriptions). Close with the bright spot (e.g. "every talking video already has English captions").
- Formatting: blank line before every table and list (CommonMark).

### 6. Recommend priorities

Close by recommending which gaps to tackle first: the languages with the biggest uncovered viewer share on the highest-impression pages. Recommend languages from each video's own audience data first, then the report top-5 (es, fr, de, ja, pt). Captions, caption translations, dubs, audio descriptions, and player accessibility settings are all managed from the Wistia app — this skill reports and recommends only; it does not make changes to the account.

## API pitfalls (learned from live runs)

- **Never call `get-captions` without `media_id`** — account-wide it returns every caption file's full text (millions of characters on large accounts). Even per-media, read only the language fields.
- **Embed-location endpoints are flaky over long ranges.** Use ~90 days; an empty result means "no recent embed data," not "not embedded."
- **Don't paginate the whole library** on large accounts (10k+ media) — scope via top-content.
- **`show-media-languages`** is viewer *browser* language (demand), not content language.
- **`show-accessibility-customizations`** returns strings ("true"/"false"), not booleans.
- **No has-audio flag exists** anywhere — hence the layered speech heuristic in step 2.
