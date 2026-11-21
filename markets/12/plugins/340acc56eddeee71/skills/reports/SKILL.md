---
name: reports
description: Use when someone asks for a chart, graph, spreadsheet, report, summary page, infographic or export of their Gyroscope history, or wants their data in a file or a custom format.
---

# Charts, spreadsheets, reports and infographics from Gyroscope history

The Gyroscope tools provide the data. ChatGPT makes the chart, the file or
the page from it. If no Gyroscope tools are available, follow the
connect-gyroscope skill instead.

## 1. Agree the shape

- Settle three things before loading anything: the date range, the kinds
  of data (sleep, meals, workouts, lifts, steps, weight, heart rate, screen
  time, places), and the output (a chart, a spreadsheet, a one-page report, an
  infographic, a CSV). Default to the last 30 days and one page when they
  have not said.
- Call `gyroscope_status` once for the member's timezone, then use explicit
  YYYY-MM-DD dates.

## 2. Load the data

- Weekly or monthly numbers for a chart or a summary: `load_trend` with one
  metric (steps, sleep, calories, protein, weight, workouts, rhr, hrv) over
  up to a year. One call per metric.
- Rows for a spreadsheet or a detailed chart: `load_history` with one kind
  or a bundle (fitness, nutrition, sleep_all, places) for one month, or a
  start and end date. Walk a longer span month by month, and keep calling
  with `page = next_page` while `has_more` is true. The rows come as CSV
  text under a `columns` header.
- A short period in full: `load_day` (7 days per call) or the single-topic
  reads for the same dates.
- Screen time by day, week or month with the top apps: `load_screen_time`
  over up to a year. One app over time: `load_app_usage` with `app`.
- Lifts by exercise over time: `load_lift_progress`, with `exercise` for one
  line per session.
- Places need the Places permission. On `insufficient_scope`, give them the
  link and leave places out until they allow it.
- Load what the output needs and no more. A one-page review of a month does
  not need a year of heart rate samples.

## 3. Build the output in ChatGPT

- Chart or infographic: use ChatGPT's own data analysis and image tools on
  the loaded rows. One chart per question, labelled axes, the unit in the
  label, the date range in the title.
- Spreadsheet or CSV: write the rows as loaded, one sheet or file per kind,
  with the `columns` header as the first row and the member's local times
  as given.
- Report or summary page: lead with the two or three numbers that changed
  most, then one short section per kind, each resting on the loaded data.
  Say how many days each figure covers.
- Durations of an hour or more in decimal hours, shorter ones in minutes.
  Weight in the units the member uses.
- Every number in the output comes from a tool answer. Never fill a gap with
  an estimate. Say which days have no data instead.

## 4. Hand it over

- Give the file or image, name the date range and the kinds it covers, and
  offer one follow-up, such as the same report for the month before.
