---
name: generate-report
description: Export an in-depth training report as a PDF, in the Lion Lift visual theme, with charts, graphs, tables, trends, and analysis across a user-specified time period and page count. Use when the user asks for a report, export, or PDF summary of their training.
---

# Generate a training report PDF

Produce a polished, multi-page PDF report of the user's training — not a plain data dump. This connector has no PDF-rendering tool of its own; it only supplies the data. Build the report using whatever document/file-creation capability is available in this conversation.

## Scope the report

- Confirm the time period, which sports to include (swim, bike, run, lift, or all), and the target page count before gathering data. A 1-page report and a 10-page report need very different amounts of detail — over- or under-filling a requested length is worse than asking first.
- Gather data the same way `lion-lift-analyzer` does: use available Lion Lift read tools for completed workouts in the selected sports and period. Include sleep/work context or goals only when those collections exist. Ask the user for age, height, weight, sex, or training experience only when a specific interpretation needs that context; never imply a profile tool returned it.

## Build it correctly, not just completely

- When grouping or charting lifts by muscle group, use the `muscleGroups` array field, not the legacy single joined `muscleGroup` string — a multi-group session like "Chest, Back, Shoulders" must count once toward each of Chest, Back, and Shoulders individually, not as one combined bucket of its own.
- Use real charts and tables, not prose pretending to be one: volume or trend over time as a line or bar chart, sport or muscle-group distribution as a pie or bar chart, a session log as an actual table. Pick the chart type the data actually supports — don't force a trend line onto three data points.
- A forecast is a short, clearly-labeled projection from the recent trend, not a guaranteed outcome. State the assumption behind it, and skip it entirely (say why, in the report) if there's too little history to support one.
- Call out, in the report itself — not just in conversation — any contributing factor found in the sleep/work logs and any missing context (age/height/weight, or missing performance data) that limits confidence in a conclusion. Same honesty `lion-lift-analyzer` applies, just surfaced to the reader directly.

## Match the Lion Lift look

- Use Lion Lift's actual palette, not a generic report style: a dark navy primary (approximately `#1F3B5E`, derived from the app's own `Color(red: 0.12, green: 0.23, blue: 0.37)`) for headers and accents. When breaking anything out by sport, use the app's own per-sport colors: run red, bike orange, swim blue, lift near-black, core purple. Keep layout clean and legible — this is a personal report, not a marketing document.

## Deliver it

- State the exact period, sports, and page count the report covers before presenting it. If the actual content came out meaningfully shorter or longer than the requested page count, say so and why, rather than silently padding or cutting it.
- This skill only reads and reports. Never call a scheduling tool from here.
