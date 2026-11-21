---
name: tubegrade-script-writer
description: Write a researched YouTube script — study how the top-performing videos on the topic hook, structure and pace it (from their transcripts), then write an original script with timestamped source citations and flagged claims to verify. Use for "write a script about X", "research and script this video idea".
---

# Research-backed script writer

Read `references/tubegrade-tools.md` first.

Goal: an original, ready-to-record script whose structure is learned from
videos that actually over-performed, with every borrowed fact traceable.

## 1. Scope
Ask only what you don't have: topic, target length (minutes), audience,
channel voice (a handle lets you check their style), long-form or Short.

## 2. Find the reference videos — ≈ 15–25 credits
- `tubegrade_find_outliers` on the topic (`days` 365, `min_ratio` 2), and/or
  `tubegrade_search_videos` (`upload_date` year, `video_type` long) keeping
  results with `outlierRatio` ≥ 2.
- Shortlist the 3 most relevant strong performers (on-topic beats biggest).
  Tell the user which three you picked and why.

## 3. Study them — 30 credits (hard cap: 4 transcripts without asking)
`tubegrade_get_transcript` for each of the 3. If one is unusable (no speech,
music only, wrong topic), replace it once — a 4th transcript. Anything beyond
that, ask first. From each usable transcript, extract:
- the **hook** (first ~30–45 seconds): how it earns attention
- the **structure**: sections with timestamps, and where the payoff lands
- **retention devices**: open loops, previews, pattern breaks, stakes
- **facts and claims** worth using, with their `[MM:SS]` timestamp
Optional: `tubegrade_get_comments` (5) on the strongest video to catch what
viewers felt was missing — fill that gap in the new script.

## 4. Write
- Original wording throughout. Learn the structure; never paraphrase a
  transcript line by line.
- Open with a hook that states the promise and the stakes within ~20 seconds.
- Sections with on-screen/B-roll notes in [brackets].
- After any fact, technique or statistic taken from a reference, add a
  citation line: `Source: <video title> — <link> at [MM:SS]`.
- Mark anything that needs outside verification (health, money, legal,
  statistics) with **[VERIFY]** — transcripts are not proof.
- Match the requested length (~140–160 spoken words per minute).

## 5. Deliver
1. The 3 reference videos (link, views, outlier ratio) and what each taught.
2. The script.
3. A **[VERIFY] checklist** of claims to confirm before recording.
4. Offer packaging next → **tubegrade-packaging-studio**.

## Don't
- Don't present a reference video's script, jokes, or unique stories as the
  user's.
- Don't state medical, financial, or legal claims as settled — flag them.
