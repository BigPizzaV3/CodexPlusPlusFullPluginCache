---
name: wistia-video-performance-report
description: >
  Builds a video performance report for a set of Wistia videos — a single video, a
  channel, a folder, or every video embedded at a shared location — comparing actual
  performance against both this account's own internal average and Wistia's State of
  Video report benchmarks, then produces a chart and a stylized downloadable report with
  insights and recommendations. Use whenever the user asks for a "performance report,"
  "performance review," "performance dashboard," wants to know "how are my videos
  performing," "how's this video doing," "how does this compare to benchmark," asks to
  "audit performance across a channel/folder," or references comparing videos to the
  State of Video report. Also trigger for "compare these videos" or "which of my videos
  is underperforming" type requests. Do NOT trigger for single-video engagement/CTA
  placement questions with no reporting angle — use wistia-engagement-tools for those
  instead (this skill can hand off to it for flagged videos in Step 7).
---

# Wistia Video Performance Report

Produces an account-aware performance report: pulls real stats for the requested videos,
benchmarks them against both the account's own historical average (internal) and
Wistia's State of Video report (external), then renders a comparison chart and a
polished, savable report.

All Wistia actions use the Wistia MCP tools — call `tool_search` for the relevant tool
family before using it, since these are deferred tools and their exact parameters aren't
in context by default.

This skill reuses the benchmark data already bundled with the `wistia-engagement-tools`
skill rather than duplicating it — read
`/mnt/skills/user/wistia-engagement-tools/references/state-of-video-benchmarks.md` in
Step 4. **If that file is present, never ask the user to re-upload the State of Video
report** — it's already available. Only ask them to provide it if that file is genuinely
missing.

---

## Step 0: Welcome message

Open with a short welcome line in Wistia's voice before asking anything — warm, direct,
conversational, encouraging. Not hype-y, not dry, no corporate throat-clearing ("We're
excited to..."). Plain verbs, no filler. One or two sentences, then move straight into
the scope question in Step 1 — don't make the welcome its own separate turn.

Examples of the tone (write your own, don't reuse verbatim):
- "Let's see how your videos are doing. First, tell me what you'd like to look at."
- "Happy to pull a performance report together. Which videos should I look at?"

Avoid: "I'd be delighted to assist you with a comprehensive analysis..." (too stiff) and
"🎉 Let's dive into your amazing video stats!" (too hype-y — also no emoji per house
style elsewhere in these skills).

---

## Step 1: Scope — which videos

Ask using `ask_user_input_v0`:

**Question:** "What would you like to analyze?"
**Options:** "A single video", "A channel", "A folder", "Videos at a shared embed
location"

Resolve into a concrete list of `hashed_id`s before moving on:

- **Single video** — ask which one (name, URL, or hashed_id) if not already given.
  Resolve via `get-medias` or `Wistia:search`.
- **Channel** — ask which channel if there's more than one (`get-channels`), then list
  its videos with `get-channel-episodes`.
- **Folder** — ask which folder if there's more than one (`get-folders`), then list its
  videos with `get-medias` filtered to that folder.
- **Shared embed location** — ask the user for the domain or page URL. Check
  `show-account-embed-locations` for a matching location and its top content. If the
  tool's response doesn't break the location down to individual media (granularity
  varies), say so plainly and ask the user to confirm the specific video titles instead
  of guessing — don't silently narrow to "whatever look right."

If a scope resolves to an unusually large number of videos (30+), tell the user the
count and confirm they want the full set before pulling stats for all of them — offer to
narrow to top-N by plays instead, since a 30-video report is unwieldy to read.

---

## Step 2: Timeframe

Ask using `ask_user_input_v0`:

**Question:** "What time period should the report cover?"
**Options:** "Last 7 days", "Last 30 days", "Last 90 days", "Custom range"

If "Custom range," ask directly in chat for start and end dates (free text — the
elicitation tool only supports fixed options). Convert the choice to `start_date`/
`end_date` values for the analytics calls in Step 3.

---

## Step 3: Pull performance data

For each video (`mediaId` = hashed ID):

- **Actual stats** — `show-media-aggregated-stats` and/or `show-media-analytics` for the
  chosen date range: plays, play rate, engagement rate (% watched), average view time,
  and any conversions if a lead capture form or CTA is active.
- **Length and type** — pull duration and metadata via `get-medias`. Classify the video's
  type using the same fixed 11-type taxonomy as `wistia-engagement-tools` (see the
  benchmarks reference file for the list) — best-guess from title/description/folder
  name, no need to stop and confirm with the user for a report (unlike the engagement
  skill, this isn't modifying anything live). Note the guess plainly in the report rather
  than presenting it as certain if it's a stretch.
- **Length bucket** — map duration to one of: `<1 min`, `1-3 mins`, `3-5 mins`,
  `5-30 mins`, `30-60 mins`, `60+ mins`.

Then compute the two benchmarks:

- **Internal benchmark** — this account's own average over the same date range, across
  videos *outside* the requested scope where possible (so a video isn't partly
  benchmarked against itself). Use `show-account-top-content` (or
  `show-current-account-stats` / `show-account-analytics` if it exposes the same
  figures) for the date range to compute an average play rate and engagement rate. If
  the account has too few other videos to form a meaningful average (e.g. fewer than 5),
  say so and lean more heavily on the external benchmark in the narrative.
- **External benchmark** — read
  `/mnt/skills/user/wistia-engagement-tools/references/state-of-video-benchmarks.md` and
  look up table 1 (engagement rate by type × length) and table 2 (play rate by length)
  for each video's own (type, length) cell.

Report all three figures (actual / internal / external) per video plainly before moving
to the chart — this is what Step 5's chart and Step 6's report are built from.

---

## Step 4: Read the benchmarks reference

If you haven't already this session, read
`/mnt/skills/user/wistia-engagement-tools/references/state-of-video-benchmarks.md` now.
Don't try to recall the benchmark numbers from memory — they're specific and the whole
point is comparing against the real published figures.

---

## Step 5: Chart

Call `visualize:read_me` with `modules: ["chart"]` if you haven't loaded it this session,
then use `assets/performance-comparison-chart-template.html` as the base for
`visualize:show_widget`. Fill in the video labels and the actual/internal/external arrays
for both engagement rate and play rate from Step 3 — the template ships a toggle between
the two metrics so both need real data, even if your prose below leads with one.

Don't repeat the chart's numbers in your prose afterward — narrate the story (who's
ahead of benchmark, who's behind, and roughly by how much), not a recitation of every
figure already visible on screen.

---

## Step 6: Stylized report

Build the downloadable report as a real `.html` file (not a `visualize` widget — this is
a saved deliverable). Use `assets/report-template.html` as the base:

1. Copy its structure, fill every `{{PLACEHOLDER}}`.
2. Duplicate the video-card block once per video in scope, filling it fresh each time.
3. Write the "Insights & recommendations" section fresh — 3-6 bullets, each naming a
   specific video, its benchmark gap (internal and/or external, whichever is more
   striking), and one concrete next step. Ground every claim in a number that also
   appears elsewhere on the page. No generic advice that could apply to any account (see
   the template's own comments for what "specific" looks like).
4. Pick badge classes (`up`/`down`/`flat`) per the template's own guidance — don't assume
   higher is always better for every metric.
5. Save to `/mnt/user-data/outputs/` and share it with `present_files`.

For a **single video**, this report is still worth generating (it's a nicely formatted
one-card version) — but ask first whether the user wants the saved file or just the chat
summary, since a single-video report is optional overhead. For **multiple videos**,
default to producing the file without asking, since that's the point of a report.

---

## Step 7: Wrap-up and handoff

After sharing the report:

- If any video is meaningfully behind both benchmarks (say, more than ~10 points below
  on engagement rate), mention that `wistia-engagement-tools` can do a deeper dive on
  that specific video — where to place a CTA or lead capture form based on its own
  drop-off data — rather than duplicating that analysis here.
- Don't proactively offer to re-run the report on a different timeframe or scope unless
  the user seems like they want to iterate; a simple "let me know if you'd like this for
  a different set of videos or time period" is enough.

---

## Handling gaps and edge cases

- **Video has too few plays to be meaningful** (rule of thumb: under 10) — still include
  it in the report, but flag the low sample size prominently next to its numbers rather
  than silently reporting a noisy percentage as if it were solid.
- **Video doesn't fit any of the 11 fixed types well** — pick the closest and say so in
  the report rather than forcing a bad fit silently.
- **Folder/channel/embed location resolves to zero videos** — say so plainly, don't
  fabricate a report from nothing, and ask the user to double check the name or try a
  different scope.
- **Account has no other videos to build an internal benchmark from** (new account, or
  the requested scope *is* the whole account) — say so, drop the internal-benchmark
  column/badge for that report, and rely on the external State of Video benchmark alone.
- **State of Video benchmarks reference file is missing** — this would only happen if
  `wistia-engagement-tools` isn't installed or its reference file moved. In that case,
  tell the user you don't have the benchmark data bundled and ask them to provide the
  State of Video report (don't guess numbers from memory — these are specific published
  figures).
- **Custom date range longer than the account's data history** — clamp to whatever data
  actually exists and say so, rather than silently returning a partial-period average
  labeled as the full requested range.
