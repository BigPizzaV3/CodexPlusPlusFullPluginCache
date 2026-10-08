# Flow comparison picker and dashboard contract

Use this reference for the selection experience and final comparison artifact. Do not depend on a
specific visualization plugin, external JavaScript library, remote font, or CDN asset.

## Picker behavior

When an interactive picker is available, render:

1. A flow-type selector with published counts for Flow, Checklist, Announcement, Launcher, Banner,
   and Resource center.
2. Two searchable flow selectors scoped to the chosen type. Hide the first selected flow from the
   second selector and vice versa. Changing type clears both selections.
3. Date-range choices: Last day, Last 1 week, Last 15 days, Last 1 month, Last quarter, Last 6 months,
   and Last year. Default to Last 1 month.
4. A Compare action disabled until two distinct flows are selected.

The resulting prompt must include both flow names, UUIDs, the common flow type, and date range. Cap a
visible result list at 30 matches and rely on search for larger accounts.

When interactive controls are unavailable, show a concise numbered list grouped by type, offer the
same ranges in text, and ask the user to reply with two numbers and a range. Never resolve duplicate
names without confirming UUIDs.

## Artifact requirements

Create one portable `.html` file in the current task's designated user-facing output directory. Keep
CSS, JavaScript, and data inline. Embed only the normalized metrics needed by the dashboard; do not
embed credentials, raw API responses, emails, or full user identifiers.

Escape every API-derived string before inserting it into HTML, SVG, or JavaScript, including flow
names, step names, timestamps, and warnings.

## Shared visual system

- Flow 1: solid `#2a78d6`.
- Flow 2: dashed `#eb6834`, so color is not the only distinction.
- Use system fonts, high contrast, visible keyboard focus, and a maximum content width near 1100px.
- Avoid gradients and decorative shadows. Use sentence case and rounded displayed numbers.
- Start with a screen-reader summary containing the headline comparison.
- Provide a custom HTML legend above charts.
- Include responsive and print styles; avoid horizontal overflow on narrow screens.

Use inline SVG for charts, or canvas code fully included in the file. Do not load Chart.js or any
other library from a CDN. Every chart must have `role="img"`, a descriptive `aria-label`, and an
adjacent static text summary so the comparison remains understandable without JavaScript.

## Guide-flow and checklist layout

Render, in order:

1. Header with the two flow names, type, exact date window, interval, and environment.
2. Metric cards for Views, Unique viewers, Completion rate, and Missing element errors.
3. One step funnel per flow that has views. For each row, show the step name, view count, and
   step-over-step drop percentage. Size the bar relative to the first step, enforce a small visible
   minimum for nonzero values, and highlight the largest percentage-drop step in red.
4. A views trend chart with aligned time buckets for both flows.
5. Method and coverage notes, including any retry, missing-series, or window-clipping warning.

Skip a funnel whose steps are all zero and explain dormancy in the written insights. Missing-element
errors are flow-level, not step-level.

## Announcement layout

Render the same header and legend, then metric cards for Views, Reactions, Comments, and Engagement
per 100 views. Compute engagement as `(reactions + comments) / views * 100`, use one decimal place,
and return zero when views are zero. Add the aligned views trend chart. Do not render a funnel,
completion-rate card, or missing-element card.

For long windows, trim leading buckets only when both flows are zero in those buckets. State the
first displayed date and disclose that earlier all-zero periods were removed.

## Data rules

- Align both series to the same timestamps and fill genuinely missing buckets with zero.
- Preserve a distinction between unavailable data and a measured zero; disclose unavailable fields.
- Use one counting basis per metric and label it.
- Compare the window start with each flow's `first_published_at` and show a clipping warning when the
  selected range omits a launch.
- Treat a published flow with zero views as dormant, not as an API error.

## Verification

Before delivery, open or render the HTML and verify:

- card values and funnel counts match source metrics;
- each trend uses aligned timestamps and the correct flow style;
- the largest percentage drop is highlighted correctly;
- zero and unavailable states are not conflated;
- accessibility labels and static summaries are present;
- the page works at desktop and mobile widths and prints cleanly;
- no network request is required to view the report.
