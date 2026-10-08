---
name: wistia-language-audit
description: >
  Audits which languages the audience of Wistia's top-performing videos actually watches
  in, checks whether transcript translations (captions/subtitles) and video dubs already
  exist in those languages, and reports the gaps ranked by measured audience demand. Use
  this skill whenever the user asks for a "language audit," wants to know "what languages
  should I dub/translate my videos into," asks to "audit my video languages," "find
  missing translations/dubs," or anything about matching video localization to viewer
  language demand. Do NOT trigger for one-off single-video captioning/dubbing requests
  with no audience-analysis component — use the Wistia tools directly for those.
---

# Wistia Language Audit

## Welcome message

Show this to the user before starting the workflow:

> Let's find out what languages your viewers actually speak, and where your captions and dubs have gaps.
>
> Nothing to prepare. I'll pull your analytics and existing translations myself.
>
> You'll get a coverage report showing exactly which translations and dubs are missing, ranked by real audience demand.

---

Finds the account's top-performing videos, figures out what languages their viewers
actually speak (from analytics, not guesses), and audits existing transcript translations
and dubs against that language demand.

All Wistia actions use the Wistia MCP tools — call `tool_search` for the relevant tool
name before each new tool family, since these are deferred tools and their exact
parameters aren't in context by default. Read `references/language-codes.md` before Step
3 — the analytics, captions, and dub tools use different language code formats and this
skill fails silently (comparing the wrong codes) if you skip that step.

**This skill is read-only.** It audits and reports; it never creates translations or
dubs or makes any other changes to the account. Filling the gaps is done by the user in
the Wistia app.

---

## Step 1: Parameters (ask, don't assume)

Ask the user, using `ask_user_input_v0` where helpful:

1. **Date range** for "top performing" and "audience language" — default to last 90 days
   if they have no preference, but confirm.
2. **How many top videos** (N) to audit — e.g. top 5 / top 10 / top 20.
3. **How many top languages** (or a minimum share threshold, e.g. "languages with ≥5% of
   plays") to target per the aggregate audience — this determines what counts as a "gap."

Top videos are ranked by **plays, tie-broken by engagement rate** (the account's
established default — don't re-ask this each run unless the user wants to change it).

---

## Step 2: Identify top videos with a transcript

Only consider videos that already have a transcript (i.e. at least one caption track,
almost always the source-language one auto-generated on upload). This is a deliberate
filter, not an optimization to skip — Wistia accounts reliably surface non-content media at
the top of raw play counts: UI loop assets, "don't delete" test/synthetic media, silent
B-roll, short onboarding-flow snippets. None of that is a sensible localization candidate,
and a transcript is the cheapest reliable proxy for "this is spoken content someone should
watch in their own language." Do this filtering **before** ranking, not as a post-hoc
cleanup step — it changes which N videos qualify, not just how they're displayed.

1. Call `show-account-top-content` with `group_by: media`, `sort_by: plays`,
   `sort_direction: desc`, the chosen date range, and a generous `per_page` (150–200) to
   get a large candidate pool — the qualifying N will be a subset of this, and how large a
   subset varies a lot by account.
2. Walk the candidates in ranked order and check each one for an existing transcript via
   `get-captions` with `media_id` set to that candidate's hashed_id. `returned_count > 0`
   means it has a transcript; qualifies. `returned_count == 0` means no transcript; skip it
   without spending further calls on it.
   - Note: `get-captions` returns full caption text per language, not just a summary — this
     is unavoidable but fine; you only need `returned_count` from each response, don't
     dwell on the text.
   - Do **not** use the account-wide `get-captions` call (omitting `media_id`) to try to
     shortcut this — it returns full SRT text for every caption track on the account with
     no media-linking field, so it can't be matched back to a specific video and is far
     more expensive than checking candidates one at a time.
3. Stop once you have N qualifying videos. If there are ties on plays at the cutoff among
   qualifying videos, break them using `engagement_rate` from the same top-content
   response.
4. This can take a lot of individual `get-captions` calls on accounts with a lot of
   non-content media mixed into top plays (dozens, sometimes) — that's expected, not a
   sign something's wrong. Keep going without narrating each check; report the final
   qualifying list, not the rejected candidates.

Keep the full analytics row per qualifying video (plays, engagement_rate, played_time,
media_duration) — you'll want it in the final report, and `media_duration` feeds the
report's duration column directly (skip the separate `get-medias` duration lookup in Step
4 when this is already present; only fall back to `get-medias` if `media_duration` came
back null).

---

## Step 3: Identify top audience languages

For each of the N videos, call `show-media-languages` over the same date range. This
returns viewer plays broken down by browser language.

- **Normalize codes first** — see `references/language-codes.md`. Collapse regional
  variants (e.g. `es-MX`, `es-ES`) to the base language unless a variant has meaningfully
  distinct volume and the user cares about the distinction.
- **Aggregate** play counts per language across all N videos to get one account-wide
  ranked list of audience languages.
- Apply the threshold/count from Step 1 to get the **target language set** — the
  languages this audit will check every top video against.

Always exclude the video's own source/original language from the target set (no point
"translating" a video into the language it's already in).

---

## Step 4: Audit existing coverage

For each of the N videos, against the target language set:

- Call `get-captions` (filtered to that `media_id`) to see which transcript/caption
  languages already exist.
- Call `gets-localizations` for that `mediaHashedId` to see which dubbed languages already
  exist.
- Map each result's 3-letter code back to a language name using the reference table, and
  mark each (video × target language) cell as:
  - ✅ have both transcript translation + dub
  - 📝 transcript translation only, dub missing
  - 🎙️ dub only, transcript translation missing (unusual, but possible)
  - ❌ have neither — both needed

Duration for the report should already be in hand from Step 2's `media_duration` field
(seconds). Only call `get-medias` here if that came back null for a particular video —
flag it as a fallback lookup, not the default path.

---

## Step 5: Report the gaps

**Present both a targeted and a full-coverage gap list, and recommend targeted.**
Applying the account-wide target language set uniformly to every video (full coverage)
routinely produces a materially larger, wasteful list — a video with zero measured plays
in a target language still gets flagged for a dub in it. Targeted means: only flag a
(video, language) dub gap where that specific video shows meaningful demand for that
language (default threshold: ≥5 plays over the date range; mention the threshold used and
let the user move it). Show both lists so the user can see the difference and pick, but
lead with targeted as the default recommendation. Transcript translation gaps stay listed
for any language with >0 plays regardless of threshold — there's no reason to be
conservative there.

Flag videos with **zero plays across every target language** separately and recommend
deprioritizing them, even if they're missing every transcript/dub — being missing isn't
the same as being wanted; a video with no demonstrated audience in any target language
has nothing to localize into yet.

Present a clear table: video title | duration | language | what's missing | plays in that
language. Rank by plays in the missing language so the biggest gaps lead.

---

## Step 6: Final summary

Recap what was found:

```
📊 Audit: top [N] videos, [date range], target languages: [list]
🌍 Coverage gaps found: [X transcript translations, Y dubs]
🎯 Recommended first: [the targeted gaps with the most measured demand]
❓ Flagged: [any videos with unknown duration, ambiguous codes, or no demand in any target language]
```

Note that transcript translations, dubs, and captions are added from the Wistia app, and
that the audit can be re-run after changes to confirm the gaps are closed.

---

## Handling gaps and edge cases

- **Video has no clear source language** (e.g. no primary transcript) → note it in the
  audit rather than guessing.
- **Ambiguous language code** not in the reference table → look it up, state the mapping
  you used in the audit output, don't silently assume.
- **User wants to re-run with different N/date range/threshold** → just re-run Steps 1–5.
- **Duration unavailable for a video** → show its duration as unknown in the report,
  don't guess a number.
- **Very few or no videos qualify with a transcript** → say so plainly rather than quietly
  lowering N or substituting non-transcript videos; ask whether to widen the candidate pool
  (larger `per_page` in Step 2) or proceed with fewer than N videos.
- **A qualifying video has a transcript but shows zero plays in every target language** →
  keep it in the audit for completeness but exclude it from the recommended list
  (see Step 5); don't silently drop it from the report either.
