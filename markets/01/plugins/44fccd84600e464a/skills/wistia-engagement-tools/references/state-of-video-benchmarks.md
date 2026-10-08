# State of Video Benchmarks (2025 + 2026 reports)

Primary source: **Wistia 2026 State of Video Report** (quantitative placement data).
Secondary source: **Wistia 2025 State of Video Report** (qualitative placement rules,
used only where 2026 doesn't cover the same ground — e.g. exact CTA quarter-by-quarter
data isn't repeated in 2026, so 2025's rule-of-thumb guidance fills that gap).

Don't directly compare numbers across the two reports as if they were the same metric —
2026 mostly reports **click-through rate**, 2025 mostly reports **conversion rate**.
They're related but not identical measures. Use 2025 for direction and rules of thumb,
2026 for the hard numbers.

---

## Fixed video type taxonomy

Use these 11 types (2026 report's own categories) when classifying a video. This is a
closed set — always map the video to one of these, even if the fit is imperfect, so it
can be matched against the benchmark tables below:

`Company update`, `Course`, `Company culture`, `Customer testimonial`, `Educational`,
`Podcast`, `Product demo`, `Promotional`, `Sales outreach`, `Tutorial`, `Webinar`

## Fixed goal taxonomy

`Lead generation` (→ recommend lead gen form), `Conversion / drive action` (→ recommend
CTA), `Engagement / authority-building` (→ recommend annotation link)

Length buckets used throughout: `<1 min`, `1-3 mins`, `3-5 mins`, `5-30 mins`,
`30-60 mins`, `60+ mins`.

---

## 1. Engagement rate by video type × length (2026)

Percent of the video the average viewer watches, by type and length bucket.

| Video type           | <1 min | 1-3 min | 3-5 min | 5-30 min | 30-60 min | 60+ min |
|-----------------------|--------|---------|---------|----------|-----------|---------|
| Company update         | 52%    | 51%     | 49%     | 38%      | 25%       | 15%     |
| Course                 | 55%    | 49%     | 47%     | 40%      | 27%       | 16%     |
| Company culture        | 51%    | 47%     | 41%     | 30%      | 26%       | 12%     |
| Customer testimonial   | 46%    | 38%     | 33%     | 22%      | 14%       | 11%     |
| Educational             | 56%    | 53%     | 50%     | 37%      | 26%       | 17%     |
| Podcast                 | 44%    | 45%     | 46%     | 29%      | 20%       | 15%     |
| Product demo            | 50%    | 46%     | 40%     | 28%      | 17%       | 12%     |
| Promotional             | 46%    | 39%     | 32%     | 24%      | 18%       | 14%     |
| Sales outreach          | 48%    | 44%     | 37%     | 26%      | 17%       | 14%     |
| Tutorial                | 54%    | 53%     | 49%     | 38%      | 21%       | 12%     |
| Webinar                 | 46%    | 45%     | 44%     | 29%      | 22%       | 17%     |

Use this row as the video's **expected engagement rate**. Compare it to the video's
actual engagement rate (from `show-media-aggregated-stats` / `show-media-analytics`) to
tell the user whether it's under- or over-performing its type/length cohort before
recommending anything.

## 2. Play rate by video length (2026)

| Length     | Play rate |
|------------|-----------|
| <1 min     | 24%       |
| 1-3 mins   | 12%       |
| 3-5 mins   | 18%       |
| 5-30 mins  | 34%       |
| 30-60 mins | 37%       |
| 60+ mins   | 52%       |

## 3. Play rate by page type (2026)

Home 24%, Video gallery 20%, Product 15%, Contact 10%, Thank you 10%, Careers 6%,
Resources 6%, Landing page 6%, News 5%, Blog 5%, About 2%, Case study 2%, Events 2%.

Only use this if the skill can determine embed page type; otherwise skip — don't guess.

## 4. Click-through rate by interactive element (2026)

| Feature         | Click-through rate |
|------------------|--------------------|
| Annotation link  | 2%                 |
| Call to action   | 15%                |
| Lead gen form    | 19%                |

Lead gen forms ask the most of a viewer (their contact info) but convert best — don't
let a lower "ask" bias the recommendation toward CTA/annotation if the user's stated
goal is lead generation.

## 5. Click-through rate by video length (2026)

| Length     | Click-through rate |
|------------|---------------------|
| <1 min     | 1%                  |
| 1-3 mins   | 3%                  |
| 3-5 mins   | 7%                  |
| 5-30 mins  | 9%                  |
| 30-60 mins | 23%                 |
| 60+ mins   | 21%                 |

Longer videos get more click-throughs — viewers who stick around are further along.

## 6. Lead gen form click-through by placement × video length (2026) — core table

This is the primary quantitative table for recommending **where** to place a feature.

| Placement    | <1 min | 1-3 min | 3-5 min | 5-30 min | 30-60 min | 60+ min |
|--------------|--------|---------|---------|----------|-----------|---------|
| Start        | 5%     | 10%     | 29%     | 10%      | 26%       | 33%     |
| 1st quarter  | 10%    | 14%     | 20%     | 53%      | 50%       | 49%     |
| 2nd quarter  | 19%    | 6%      | 4%      | 55%      | 38%       | 67%     |
| 3rd quarter  | 1%     | 9%      | 16%     | 27%      | 24%       | 38%     |
| 4th quarter  | 40%    | 18%     | 35%     | 54%      | 51%       | 75%     |
| End          | 2%     | 2%      | 2%      | 3%       | 18%       | 33%     |

**How to use this table:** for a given video length bucket, find the column, then
recommend the placement (row) with the highest click-through rate. General pattern:
late placement (4th quarter) tends to outperform for most lengths, and the very start
also does surprisingly well on longer videos — but the "End" position is consistently
weak. Always name the actual best row for the video's specific length bucket rather
than reciting the general pattern, since it isn't perfectly monotonic (e.g. <1 min peaks
at 4th quarter, not gradually building toward it).

This table is specifically about lead gen forms. Apply it to CTA and annotation
placement too, treated as a reasonable proxy, but say so explicitly when you do —
the 2026 report doesn't provide a separate quarter-by-quarter table for those two.

## 7. 2025 supplemental: CTA placement rules of thumb (qualitative)

From the 2025 report (LaQuita Cleare, CEO, quoted directly — paraphrased here):

- **Presentation-style videos:** place the CTA at the end so it feels like a natural
  next step rather than an interruption.
- **Shorter videos:** put the CTA within the first minute.
- **Longer videos (over ~30 minutes):** put a CTA around the 20-minute mark, and
  consider adding a second CTA somewhere in the middle for videos on the longer side.

Use these as a sanity check / tiebreaker alongside table 6, not a replacement for it —
prefer the 2026 quantitative table when the two disagree.

## 8. 2025 supplemental: conversion rate by interactive feature (overall)

Lead gen form ~24%, Call to action ~16%, Annotation link ~3%. Directionally consistent
with the 2026 click-through numbers (table 4) — lead gen form > CTA > annotation in
both reports, even though the exact metric differs.

## 9. 2025 supplemental: conversion rate by video type

Original series 30%, Webinar 25%, Sales 20%, Customer testimonial 17%, Product 17%,
Educational 16%, Promotional 12%, Company culture 8%, Social media 4%.

Note: this uses a slightly different, non-exhaustive type list than the fixed taxonomy
in this file. Use it only as loose supporting color (e.g. "webinars have historically
converted well") — always classify against the fixed 11-type taxonomy above for the
actual recommendation logic.
