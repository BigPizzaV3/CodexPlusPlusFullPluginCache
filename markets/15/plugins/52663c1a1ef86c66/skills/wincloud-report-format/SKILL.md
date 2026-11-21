---
name: wincloud-report-format
description: How to present any WinCloud data so a hotel manager can read it at a glance. Use for every WinCloud answer that has more than one number or row, such as stats, statistics, KPIs, summaries, insights, analytics, reports, trends, comparisons, forecasts, "how are we doing", bookings or reservations by month, location, status or room type, even when the user never says "chart". Makes the answer a headline, KPI row, real chart and detail table, in RBS colours. The other wincloud-* skills follow it.
---

# Presenting WinCloud data

Managers skim these answers between tasks. A chart shows a pattern in a second where a table takes a minute, so draw one by default; nobody should have to ask for it. A KPI table alone is not enough: it supports a chart and never replaces it.

## Order of every answer

Every response, even a single fact, a list or "WinCloud can't do that", opens with a one-sentence summary of at most 25 words. The reader gets the answer in seconds and reads the rest only if they want the detail. For answers with numbers, that sentence is the headline below.

1. **Headline.** One or two sentences: the number, the direction and what it means ("Hotel A took 150 bookings in Q1, 100 fewer than Hotel B").
2. **KPI row.** The 3 to 6 headline figures, labelled, in one small table (labels on top, values below).
3. **Chart.** At least one real chart of the pattern, and one more per further comparison. Several locations, months or statuses means a chart that shows them side by side. Two or three charts at most; each shows one comparison, so none is crowded.
4. **Detail table.** The numbers behind the charts, 20 rows at most.
5. **Basis and caveats.** Hotel, date range, which date field was used, whether all pages were read, and anything estimated. A few lines.
6. **What to look at.** For analysis, forecast and report answers, up to 3 specific items the numbers support (a weak date, a rising no-show count). Offer them as things to consider, not decisions.

Skip the chart only for a single value or yes/no (a sentence), or a list of individual bookings, guests or rate plans (a table, newest first). If a query returns no rows, say so and name the filters you used; don't draw an empty chart.

## Pick the chart

| The data is… | Chart (`type` in `scripts/chart.py`) |
|---|---|
| Trend over dates or months | `line`; `bar` when each point is a count |
| Several locations, statuses or years compared (a vertical bar chart) | `bar`, grouped, one series per location or status |
| Categories (room types, rate plans, sources), many or long names | `hbar`, sorted high to low |
| Share of a whole, 5 parts or fewer (status mix, cancellations versus no-shows). A request for a pie chart gets this. | `donut` |
| Prices or status across dates and room types | Table with the odd cells flagged |

Figures on different date bases, such as bookings by booking date and no-shows by arrival date, go in separate charts. Never one chart that implies a single cohort.

## Drawing the chart

Work down this list and stop at the first that works. Finish the chart before writing the headline, so the words match it. Charts belong in the conversation, so show them inline where you can.

1. **An inline visualizer or chart tool, when your environment has one** (in Claude, `show_widget`, after reading its `chart` guidance with `read_me`). Pass the SVG or HTML straight to it. Don't write a file first.
2. **`scripts/chart.py`** in this skill's folder. It needs only Python. Write a small JSON spec (`type`, `title`, `subtitle`, `unit`, `categories`, `series` with `name` and `values`; `"dashed": true` on a forecast series), run `python3 <this folder>/scripts/chart.py spec.json chart.svg`, then show the picture inline (a file-sharing tool set to render in the conversation, if you have one). It writes a PNG too when it can. `references/chart-recipes.md` has the spec for each type and the next steps.
3. **Your own tool.** matplotlib, another plotting library, or a chart your environment renders, in the colours below.
4. **Hand-written SVG or HTML**, shown inline or as an artifact. `references/chart-recipes.md` has a template.

Where you must write a file, use the session's scratchpad directory if the environment gives you one, never `/tmp`, and name the file by its full absolute path. Offer a downloadable file only when the user asks for one.

Try them all before giving up. Only if none can work, say in one line why ("this chat can't draw images"), then show the KPI row and a table with a text bar beside each row (`▇▇▇▇ 24`). Never describe a chart you did not produce.

Before showing a chart, check its title, categories, series names and values against the figures in your answer, and fix any mismatch.

## Style

- Colours: primary #003352 (navy), secondary #63e7a4 (green). Navy for the main series, green for the comparison or forecast, then tints of navy and grey for more series. One meaning per colour for the whole conversation.
- Font: Century Gothic where the environment lets you choose one.
- Title says what and where, with the location as `list_companies` returns it ("Bookings by month, Grand Hotel, Q1 2026"). Label axes with units, print the values on the bars or points, start bar charts at zero.
- **Hotel names, never codes.** Wherever a location appears (headline, KPI row, chart title, series names, legend, table rows and columns, attention items) use its name from `list_companies`, such as "Grand Hotel", not "WS". When comparing hotels, name each series and row by hotel. The code may appear once, in brackets, in "Basis and caveats".
- Before showing a chart or table, check that no label is a bare company code, and replace any you find with the name.
- Forecasts are a dashed line or lighter bars, with the actual part solid. Say which part is which.
- Make it readable without colour alone: legend and direct labels.

## Numbers

- State the unit and the hotel's currency exactly as the tools return it. Never assume a currency symbol.
- Percentages: one decimal at most. Money: whole units unless the tool gives decimals.
- Compare like with like: same length of period, same hotel.
- Round only for display; do the sums on the full values.

## Check the data before reporting

Look for records that would mislead the reader, and list any you find under "Basis and caveats" so the manager can check them in WinCloud. Don't drop or correct them yourself.

- A booking still `CheckedIn` whose departure date has passed, or still expected whose arrival date has passed.
- A room count far above the hotel's usual (for example one no-show of 18 rooms at a 40-room hotel).
- Room counts that don't add up (occupied plus vacant less than total rooms).

## Honesty

- Report what the tools returned. Mark every derived figure ("calculated from…") and every projection "estimate".
- Money figures are the **booked rate** stored on the reservation, not money charged or collected; WinCloud's payments are not available here. Label them so ("ADR from booked rates"), with the currency and how the average was weighted.
- If you stopped before the last page of results, say the figure covers only what you read.
- Figures from this plugin support decisions; they don't replace the hotel's own reports. Remind the user to verify before using them for pricing, budgeting or anything contractual.
- Never show payment details. Guest contact details are never returned, so never show or guess them.