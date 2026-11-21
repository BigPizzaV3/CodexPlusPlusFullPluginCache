---
name: tubegrade-packaging-studio
description: Write titles and design thumbnail concepts for a video, grounded in proven viral title/thumbnail formats and the actual thumbnails of breakout videos on the same topic. Also compares the user's own title or thumbnail options. Use for "title ideas for my video", "thumbnail concept", "which title is better", "improve my thumbnail".
---

# Packaging studio — titles and thumbnails

Read `references/tubegrade-tools.md` first.

Goal: titles and thumbnail concepts that use patterns which demonstrably
produce breakouts — adapted, never copied.

## 1. Scope
You need the video's topic and its core promise (what the viewer gets). If
the user has a draft title, thumbnail, or a published video link, start from
it. Ask about the audience only if it changes the packaging.

## 2. Evidence — budget ≈ 30–50 credits
1. `tubegrade_viral_formats` with `kind` title (default sort, no filters) —
   one call; a second with `kind` thumbnail if thumbnails are in scope. Among
   the results, prefer formats whose `state` is emerging or rising.
2. `tubegrade_find_outliers` on the topic (`min_ratio` 2) — breakouts whose
   packaging you'll study.
3. `tubegrade_thumbnails` on the 5–8 strongest of those (1 credit each) —
   LOOK at the images.
4. If the user gave a published video: `tubegrade_find_similar_thumbnails`
   (20 credits) only if they want to see lookalikes; say the cost first.

## 3. Analyse what wins here
From the formats and the images, note what repeats among the winners:
- title structure (number, contrast, "how/why", time-box, stakes, curiosity gap)
- title length and the words that carry the promise
- thumbnail: face/no face and expression, text (how many words), focal
  object, colour contrast, before/after or comparison layouts

Cite the videos each observation comes from.

## 4. Deliver
**Titles** (8–10): grouped by format. For each: the title, the format it uses,
and one line on why it suits this video. Keep each one truthful to the video's
actual content — no promise the video won't keep.

**Thumbnail concepts** (3): for each — layout, focal subject, text (≤4 words),
colours/contrast, and the winning thumbnail(s) it learns from (linked).
Concepts must be original compositions, not recreations.

**Pairing**: the best title + thumbnail combo, and why they work together
(the thumbnail shows, the title tells — don't repeat the same words).

**If comparing the user's own options**: rank them against the evidence,
say what each does well/poorly, and suggest one improvement each. Be direct.

## Don't
- Don't reuse a competitor's exact title or describe a thumbnail recreation.
- Don't promise click-through numbers — say which option has more evidence.
