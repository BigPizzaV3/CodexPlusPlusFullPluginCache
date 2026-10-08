# NPS time-range picker and comment-report contract

Use this reference for the selection experience and final report. Do not depend on a specific
visualization plugin, remote font, external JavaScript library, or CDN asset.

## Time-range picker

When interactive controls are available, render:

1. A confirmation label containing the verified flow name and “NPS question found”.
2. Choices for Last 1 week, Last 15 days, Last 1 month, Last quarter, Last 6 months, and Last year.
   Default to Last quarter.
3. A Summarise action whose resulting prompt includes the flow name, UUID, and selected range.

When interactive controls are unavailable, show the verified flow and the same ranges as a numbered
text list, then ask the user to reply with one number.

## Portable report

Create one standalone `.html` file in the current task's designated user-facing output directory.
Keep CSS, JavaScript, and normalized data inline. Do not make network requests from the report.

Start with a screen-reader summary containing total response and comment counts plus the dominant
positive and negative themes. Then render a context line with flow name, exact date window, and
“N comments from M responses”.

Render two native `<details open>` sections so expansion works without JavaScript:

- Positive, with heading color `#348452`.
- Negative, with heading color `#e34948`.

Each section contains:

- a short thematic summary with bold theme labels and counts;
- one row per comment with score badge, shortened internal user ID, response date, and comment;
- an explicit empty-state message when no comments fall in that section.

Classify sections by comment sentiment, not score bucket. Style score badges independently: score
9–10 uses `#348452`, 7–8 uses `#d97917`, and 0–6 uses `#e34948`. This preserves visible divergence
between score and written sentiment.

## Privacy and escaping

- Show internal user IDs as the first eight characters plus an ellipsis. Never attempt to infer a
  name or email from an internal UUID.
- Escape all API-derived strings before inserting them into HTML or JavaScript, including flow names,
  question names, comments, dates, and IDs.
- Do not embed raw API responses, access tokens, credentials, or identity fields not required by the
  report.
- Preserve the substantive meaning of comments. If shortening is necessary, label it as a paraphrase
  and retain concrete product, pricing, and bug details.

## Design and accessibility

- Use system fonts, high contrast, visible keyboard focus, and a maximum width near 1000px.
- Avoid gradients and decorative shadows. Use generous spacing and responsive row layouts.
- Make each `<summary>` understandable without color and include comment counts in its text.
- Add print styles and prevent horizontal overflow on narrow screens.
- Keep both Positive and Negative sections visible even when one is empty.

## Deliberate exclusions

Do not add an NPS score card, promoter/passive/detractor split, or trend chart. This artifact is a
comment-theme report only.

## Verification

Before delivery, open or render the HTML and verify:

- joined comments use the score from the same `session_id`;
- skipped or empty text answers are excluded from comment counts;
- positive and negative totals match the rendered rows;
- every user ID is shortened and every API-derived string is escaped;
- the report works without network access and remains readable with JavaScript disabled;
- desktop, mobile, and print layouts have no horizontal overflow.
