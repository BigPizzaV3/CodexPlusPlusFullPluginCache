# Adoption Agent topic report HTML contract

Use this contract when creating the final report. Produce one portable `.html` file with inline CSS and JavaScript and no network-loaded fonts, libraries, images, or tracking.

## Page structure

1. Header: agent name, exact date window, environment, and a one-line scope statement.
2. KPI row: total conversations, unanswered conversations and rate, disliked conversations and rate, and analyzed coverage.
3. Method note: explain that topics are clustered from user messages; define unanswered; state full-read or sampled coverage.
4. Couldn't answer: ranked topic cards.
5. Negative feedback: ranked topic cards.
6. Asked most often: ranked customer-topic cards, followed by a visually separate internal/test subsection when applicable.
7. Footer: generation date, exact coverage, counting basis, and known limitations.

## Topic cards

Render every topic as a native `<details>` element so the report works without JavaScript. Its `<summary>` must contain:

- rank and plain-language topic name;
- one-sentence description;
- count and correctly labeled denominator;
- badges such as `Test`, `Frustration chain`, `Also #1 unanswered`, or `Sampled`.

Inside the expanded card, render each source conversation in chronological order. Include a short conversation ID, shortened user ID when available, timestamp, and messages sorted by `inserted_at`. Clearly distinguish user and assistant turns. Highlight unanswered user messages, disliked messages, and escalation turns. Show dislike feedback verbatim in a styled quote block.

## Visual design

- Use a restrained, accessible palette with high contrast and a maximum content width around 1100px.
- Make the three report sections visually distinct without relying on color alone.
- Use readable system fonts, generous spacing, and sticky-free layouts that print cleanly.
- Add visible keyboard focus styles to `<summary>` elements.
- Include responsive CSS so KPI cards and metadata stack on narrow screens.
- Add `@media print` rules that remove decorative shadows and avoid splitting a topic header from its first conversation.

## Data and safety

- Escape all API-derived text before inserting it into HTML, including topic labels, messages, feedback, names, IDs, and timestamps.
- Do not embed access tokens, raw API responses, email addresses, or full user UUIDs.
- Do not round small counts into percentages that imply more precision than the sample supports.
- Use one counting basis per displayed number and label it as conversations or messages.
- Never fabricate missing message text or metadata. Render an explicit em dash for missing optional values.

## Interaction

Native `<details>` expansion is required. Optional inline JavaScript may add only progressive enhancements such as Expand all, Collapse all, and print controls. The full report must remain readable when JavaScript is disabled.

## Final verification

Before delivery, open or render the HTML and verify:

- every transcript is chronological;
- section rankings descend by the stated metric;
- repeated topics use the same canonical name;
- badges and cross-section references are accurate;
- totals and rates match their labeled denominators;
- coverage and sampling disclosures are present;
- no horizontal overflow occurs at desktop or mobile widths.
