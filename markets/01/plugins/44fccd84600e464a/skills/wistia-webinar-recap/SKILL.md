---
name: wistia-webinar-recap
description: Turn a finished Wistia webinar into a shareable recap — a short performance summary for the team, social clips with suggested copy, and a ready-to-publish blog post with the webinar embedded. Runs on the /wistia-webinar-recap command, or when Sam asks to "recap my last webinar", wants a webinar performance breakdown, show-rate/engagement numbers, or post-event assets. Step 3 of the webinar workflow (create → registration updates → recap), and is also handed off from the registration-updates skill once an event ends.
author: Wistia
version: 1.0.0
---

# Wistia Webinar Recap

The morning-after deliverable: how the webinar performed, packaged as a shareable performance page (short summary + charts), a grid of social clips with suggested copy, and a ready-to-publish recap blog post with the webinar embedded. Final skill in the sequence (`webinar-event-creation` → `webinar-registration-updates` → **this**), coordinating via **`webinar-state.json`**.

## When this skill starts

Open with this welcome message, verbatim:

> Once you finish a webinar in Wistia, run this skill to get a short performance summary to share with the team, social clips with suggested copy, and a ready-to-publish blog post with highlights and the webinar embedded inside.
>
> Make sure this skill is saved for later use, and then just type /wistia-webinar-recap when you want to run it again.
>
> So, what webinar would you like to start with?

Then wait for the user to name a webinar. If they already named one in the same message (a title, a Wistia link, or a hashed ID), skip straight to "Identify the webinar" and proceed. Don't dump the steps below into chat — just run them.

## Identify the webinar

Take whatever the user provides — a title, a `home.wistia.com/live/events/<id>` link, or a hashed ID — and resolve it with `get-webinars`. If they're vague ("my last one"), read `webinar-state.json` (handed off from step 2, usually `stage: "recapped_pending"`), or auto-detect the most recently **ended** real webinar via `get-webinars` (`lifecycle_status` `ended`/`vod_ready`, recent past, excluding test titles) and confirm. Pull the `goal` from state if present.

## Pull the data (Wistia MCP)

1. **`show-webinar-analytics`** — `registrations`, `attendance`, `engagement_rate`, `engaged_attendees`, `average_watch_time`, `total_watch_time`, `event_time`, `chats`, `chatted_attendees`, `qa_questions`, `poll_questions[]`.
2. **`show-webinar-histograms`** — `attendees_histogram` (retention curve), `chat_histogram`, `visual_focus_played_histogram`. Cheap, no pagination — prefer this for retention/watch-depth.
3. **`show-webinar-audience`** *(only if needed)* — per-registrant rows for channel tally or exact watch-depth. Token-heavy (embedded histograms); don't pull just for headline metrics.

`show-webinar-traffic-breakdown` is unreliable (frequent 500s) — derive channels from audience `referrer_domain`/`utm_source` instead.

## Compute the metrics

| Metric | How |
|---|---|
| Show rate | attendance / registrations (flag if < ~20%) |
| % to goal | registrations / goal |
| Avg watch depth | average_watch_time / event_time (>70% is excellent) |
| Retention to end | attendees_histogram[-1] / max(...) |
| Retention at 75% mark | attendees_histogram[int(0.75·len)] / max(...) |
| Active engagement | engaged_attendees / attendance; also engagement_rate |
| Chat participation | chatted_attendees / attendance; total chats |
| Satisfaction | rating poll in poll_questions[] (% 4–5★, weighted avg) |

On "% watched past 75%": the aggregate has no true per-attendee distribution cheaply — use **avg watch depth** + **retention at the 75% mark** as labeled proxies. Only paginate `show-webinar-audience` if Sam wants the exact distribution.

## Clips (Remix)

If clips for this event don't exist yet, offer to create them with Remix (Wistia's agentic editor): a mix of horizontal (16:9) and vertical (9:16) cuts across the strongest moments, each with a title, short description, and suggested social copy. Poll `get-remix` to completion, then confirm each export is a fully-rendered permanent media (`status: ready`, `progress: 1`) before embedding — instant previews expire and render blank. Save the permanent `hashed_id`s for the page.

## Output 1 — the performance page (primary)

A standalone **HTML performance page**. **Use the bundled template — don't rebuild it:** `assets/recap-page-template.html` (the polished Wistia-branded version; `assets/clip-picker-template.html` is the companion clip browser). Copy it to a new output file and swap in this webinar's data:

- **Nav + title & source:** `<title>`, `<h1>`, and the `.source` line (partner · live date · duration).
- **KPIs** (4): registrations, average engagement %, average watch time, average rating.
- **Charts** (bottom `<script>`): registrations-vs-average bar `data:[<regs>,<avg>]`; engagement gauge (doughnut) `data:[<eng>,<100-eng>]` with the `fillText('<eng>%')` center label; proportional star rating (`.stars-fg` width = rating/5); plus the chart-caption prose quoting those numbers.
- **Clips grid + blog embeds:** Wistia iframe `src` IDs and titles from the clips generated for this event. Blog body uses **horizontal 16:9 only** (brand rule); verticals live in the clip grid.
- **Recap blog post:** left-aligned, headline, byline date, body paragraphs (from the transcript), gated full-session video ID, CTA link, and the copy/download tools (Copy as Markdown / rich text / Download .md).

Keep the structure, Poppins/Inter fonts, and Wistia palette intact — it's already on-brand (https://wistia.github.io/brand/).

**Build as a standalone `.html`, NOT a Cowork artifact** — the artifact sandbox blocks Wistia embeds and Google Fonts, so players render blank. A standalone file opened in a browser loads everything.

## Output 2 — the short summary (closing message)

End with a tight summary linking to the page:

```
📋 Webinar Recap — <Title>
<turnout headline + the single strongest metric>
<3–4 metric lines: show rate · watch depth · engagement · rating>
Takeaway: <one honest sentence — what worked + the biggest lever next time>

📊 Full performance page → <link to the .html>
Get a full event performance breakdown plus post-event assets like social clips and a webinar recap blog post.
```

Keep the CTA line (or a close variant). Adapt metric lines to the data; drop any you don't have.

## Validated example (Pipeline webinar, pb4hqzr1dz)

469 regs (94% of 500), 81 attendees (17% show rate — low), 80% avg watch depth, 76% of peak retained at the 75% mark, 79% engagement, 94 chats / 24 chatters, 15 Q&A, 88% rated 4–5★ (avg 4.3). Verdict: small but deeply engaged audience; the lever next time is **attendance**, not content. `assets/recap-page-template.html` is this exact event, fully rendered.

## Wrap-up

After delivering, set `webinar-state.json` `stage: "recapped"`. This completes the workflow — note that to Sam. If the person hasn't saved the skill yet, remind them they can save it and re-run it anytime with **/wistia-webinar-recap**.
