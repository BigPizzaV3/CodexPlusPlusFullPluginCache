---
name: timeline-maker
description: Turn dated events into a to-scale or evenly spaced timeline chart with SVG, PDF and CSV downloads using the generate_timeline tool. Handles years, months, full dates, approximate dates and BC years.
---

Use `generate_timeline` when the user wants a timeline, a chronology or a history chart from dated events, and wants to see or download it.

How to call it:
- Send all events in one call (1 to 200). Each event needs `date` and `label`. Add `end_date` for spans (a war, a reign, a project phase), `category` for color groups, and `detail` for a note shown on click.
- Dates: `1969`, `1969-07`, `1969-07-20`, `July 1969`, `20 July 1969`, `c. 1500`, `500 BC` or `-500` (both mean 500 BC). There is no year 0.
- Slashed dates such as `03/04/2025` are ambiguous. Ask the user which part is the month, then pass `date_order`, or convert to YYYY-MM-DD yourself.
- Use `periods` for eras drawn as bands, for example the Republic and the Empire.
- `scale`: `to_scale` (default) or `even`. `orientation`: `horizontal` (default) or `vertical` for long lists. `page_size`: `letter` or `a4`.

After the call, give the user the PDF, SVG and CSV links from the result and mention any notes. Only use dates the user gave or confirmed; the tool does not look up history.

Do not use it for project schedules with task dependencies or for date arithmetic alone.
