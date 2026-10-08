---
name: wistia-engagement-tools
description: >
  Audits a Wistia video's engagement (play rate, avg view time, drop-off point,
  re-watched segments), classifies its type and goal, and recommends where to add or
  move an interactive feature — lead capture form, CTA, or annotation link — using
  Wistia's State of Video benchmark data. Use whenever the user asks to "audit
  engagement," wants to know "where should I put a CTA / lead capture form /
  annotation link," asks "why are people dropping off this video," wants to "improve
  conversion," or references an "engagement audit/report/tools" workflow. Applies to
  videos meant to drive leads, conversion, or engagement, with 10+ plays (fewer is a
  caveat, not a blocker). Also trigger for a bulk/account-wide version ("audit
  engagement across my videos," "which videos need a CTA"). Do NOT trigger for general
  analytics questions with no engagement-feature angle — use Wistia tools directly.
---

# Wistia Engagement Tools

## Welcome message

Show this to the user before starting the workflow:

> Let's see how your video is really being watched: play rate, where people drop off, what they rewatch. Then I'll recommend where a lead capture form, call-to-action (CTA), or annotation link would do the most good.
>
> Point me to the video (or say "all videos"). Works best at 10+ plays; below that, I'll just flag it as a caveat, not a dealbreaker.
>
> You'll get a placement recommendation, backed by that video's own data and Wistia's benchmarks.

---

Diagnoses how a video is actually being watched, then recommends where to place a lead
capture form, CTA, or annotation link based on that video's own drop-off/re-watch data
*and* Wistia's State of Video benchmarks for videos like it.

All Wistia actions use the Wistia MCP tools — call `tool_search` for the relevant tool
family before using it, since these are deferred tools and their exact parameters aren't
in context by default. Read `references/state-of-video-benchmarks.md` before Step 4 —
it has the exact tables this skill's recommendations are built from; don't try to recall
the numbers from memory. `assets/retention-chart-template.html` has the retention-curve
chart used in Step 5 — read it when you get there rather than rebuilding the chart from
scratch each time.

**This skill can modify a live video's engagement features in Step 6.** Never call an
`update-*-customizations` tool without explicit, per-change confirmation — see Step 6.

---

## Step 0: Scope — single video or bulk scan

Default to a single video (the user names it, pastes a URL, or you're mid-conversation
about a specific one). If the user asks for an account-wide or multi-video audit
instead:

1. Ask for a date range (default: last 90 days) and how many candidate videos to
   consider (default: top 25 by plays).
2. Call `show-account-top-content` with `group_by: media`, `sort_by: plays`, the date
   range, and that `per_page`.
3. Run Steps 1–5 for each video that clears the qualification bar (below). Skip Step 6
   (applying changes) in a loop — surface all recommendations together at the end and
   let the user pick which video(s) to act on, then apply one at a time per Step 6.
4. Bulk runs default to a saved artifact (see Step 7) rather than a chat report — there's
   no need to ask when there's more than one video.

For a single video, continue below directly.

---

## Step 1: Qualify the video

Confirm the video is meant to drive leads, conversion, or engagement — if that's not
obvious from context, ask the user rather than assuming. This skill isn't useful for
purely informational or internal-only videos with no engagement goal.

Check play count via `show-media-aggregated-stats`. **10 plays is a soft floor, not a
hard gate**: below it, continue the audit but flag prominently in the report that the
sample size is small and the recommendation is lower-confidence.

---

## Step 2: Pull current engagement data

For the target video (`mediaId` = hashed ID), gather:

- **Play rate, average view time (percent watched), plays** — `show-media-aggregated-stats`
  and/or `show-media-analytics` (needs `start_date`/`end_date`; default to all-time or
  last 90 days if the user has no preference — ask if ambiguous).
- **Drop-off point and re-watched segments** — `show-media-engagement`. This returns a
  per-second (or per-bucket) retention curve:
  - **Drop-off time** = the point where the retention curve falls off sharply (not just
    the very end — look for the steepest sustained decline, which is often earlier than
    where the curve finally bottoms out).
  - **Drop-off rate** = the percentage of viewers lost by that point (100% minus
    retention at that timestamp).
  - **Re-watched areas** = any segment where the curve rises or plateaus above the
    surrounding trend (viewers replaying that section) — report timestamp ranges, not
    just "yes/no."

Report these five figures plainly before moving on:
1. Play rate
2. Average view time
3. Drop-off rate
4. Drop-off time
5. Re-watched areas (if any — it's fine to report "none detected")

---

## Step 3: Classify type and goal, confirm with the user

Determine the video's likely type from two sources:

- **Metadata** — title, description, folder/project name via `get-medias` or the
  media's existing details.
- **Transcript** — pull captions via `get-captions` (`media_id` = the video's hashed
  ID) and skim for content cues (e.g. "welcome to our webinar," "here's how to set
  up...," testimonial-style first-person praise).

Map your best guess to one of the **11 fixed video types** in the reference file (don't
invent new categories — pick the closest fit). Then ask the user to confirm, using
`ask_user_input_v0` where available:

1. **Video type** — present your best guess plus 2-3 plausible alternatives from the
   fixed taxonomy.
2. **Goal** — Lead generation / Conversion (drive action) / Engagement (authority-
   building), defaulting to your best guess based on type (e.g. testimonials often lean
   conversion, tutorials often lean engagement) but let the user override.

Don't proceed to Step 4 with an unconfirmed type/goal — the recommendation logic depends
on both.

---

## Step 4: Recommend placement

Read `references/state-of-video-benchmarks.md` now if you haven't already this session.

1. Determine the video's **length bucket** (<1 min, 1-3, 3-5, 5-30, 30-60, 60+).
2. Look up **expected engagement rate** for this video's (type, length) cell in table 1.
   Compare to the video's actual engagement rate from Step 2 — say plainly whether it's
   under/over/in-line with the benchmark.
3. Map the confirmed **goal** to a feature: Lead generation → lead gen form, Conversion
   → CTA, Engagement → annotation link.
4. Use table 6 (lead gen form click-through by placement × length) to find the
   best-performing placement row for this video's length bucket. Apply this table to
   whichever feature was chosen in step 3, and say explicitly that table 6 is built from
   lead-gen-form data being used as a proxy when the feature isn't a lead gen form.
5. Cross-check against the video's **own** drop-off point from Step 2 — if the
   benchmark-recommended placement lands after the video's typical drop-off point, flag
   this tension explicitly rather than silently picking one. In that case recommend
   placing the feature at or just before the drop-off point instead, and explain why
   you're overriding the raw benchmark.
6. For CTAs specifically, also sanity-check against the 2025 qualitative rules (table 7)
   as a tiebreaker.
7. If there's a re-watched segment from Step 2, call it out as a secondary candidate
   spot for an annotation link regardless of the primary recommendation — high
   re-watch usually means high interest, which is exactly where a clickable link
   performs best.

State the recommendation as a specific timestamp or range (e.g. "around 4:10, in the
video's 4th quarter"), not just a vague zone.

---

## Step 5: Report

Render the retention curve as an inline chart before the text summary. Call
`visualize:read_me` with `modules: ["chart"]` if you haven't loaded it this
session, then use `assets/retention-chart-template.html` as the base for
`visualize:show_widget` — fill in its placeholders from the `engagement_data`
array (Step 2), the video duration, any re-watch zones, and the recommended
placement from Step 4. Skip the recommendation marker only if Step 4 hasn't
run yet (e.g. reporting mid-workflow before type/goal confirmation). Don't
repeat the chart's content in your prose afterward — narrate the
recommendation and reasoning, not the numbers already on screen.

Single video, chat report by default:

```
📹 [Video title] — [type] · [goal] · [length bucket]
📊 Plays: [N] [⚠️ below 10 — low-confidence flag if applicable]
▶️ Play rate: [X]%
⏱️ Avg view time: [X]% watched
📉 Drop-off: [X]% of viewers by [timestamp]
🔁 Re-watched: [timestamp range(s), or "none detected"]

Benchmark comparison: [actual]% vs [expected]% engagement for [type] at this length
([above/below/in line with] benchmark)

💡 Recommendation: Add a [feature] at [timestamp] ([placement label], based on [X]%
click-through for [length bucket] videos at that position)
[Secondary note on re-watched segment, if any]
[Note on any tension between benchmark placement and actual drop-off point, if any]
```

After the report, offer to save it as an artifact even for a single video (per Step 0,
artifacts are the default for bulk but always optional for single-video runs — just
ask).

---

## Step 6: Apply (only with explicit per-change confirmation)

If the user wants to act on the recommendation, confirm the exact change before calling
anything — restate feature, timestamp/placement, and any text/URL needed, and get a
clear yes. Never batch-apply without confirming each one, even in a bulk run.

- **Lead gen form**: `update-lead-capture-customizations` — `provider: wistia_form` (or
  the account's CRM provider if they use HubSpot/Marketo/Pardot), `settings.time` set to
  the recommended placement.
- **CTA**: `update-engagement-customizations` with `plugin.postRoll-v1` — set `on: true`,
  `time` to the recommended placement (or `"end"`), plus `text`/`link` from the user.
- **Annotation link**: `update-engagement-customizations` with `plugin.midrollLink-v1` —
  set `on: true` and add an entry to `links` with `time`, `text`, `url`, `duration`.

After applying, confirm success and remind the user these changes are live immediately.

---

## Handling gaps and edge cases

- **Video has no transcript** → classify from metadata alone, flag lower confidence on
  the type guess, still ask the user to confirm.
- **`show-media-engagement` returns sparse/noisy data** (very low plays) → say so
  plainly rather than inventing a precise drop-off timestamp; give a rough zone instead
  ("somewhere in the first third") and lean harder on the play-count caveat from Step 1.
- **Video doesn't fit any of the 11 types well** → pick the closest and say so
  explicitly when confirming with the user, rather than silently forcing a bad fit.
- **User's stated goal doesn't match the feature they explicitly asked for** (e.g. goal
  is "lead generation" but they asked specifically about annotation links) → go with
  what the user explicitly asked for, but note the mismatch and mention the benchmark
  case for the goal-aligned feature instead.
- **Video already has an engagement feature in place** → check current state via
  `show-lead-capture-customizations` / the engagement customizations before
  recommending — recommend *moving* it if placement is suboptimal rather than assuming
  none exists.
- **Bulk run with no qualifying videos** (none meet the "drive leads/conversion/
  engagement" intent) → say so, don't force recommendations onto videos with no
  engagement goal.
