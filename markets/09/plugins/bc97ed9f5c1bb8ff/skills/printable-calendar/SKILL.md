---
name: printable-calendar
description: Make printable calendar PDFs (year on one page, 12-month wall calendar, single month, or a month range such as a school year) with public holidays for a country and state, birthdays and events, week numbers and notes, using generate_calendar; list a country's public holidays with find_holidays.
---

# Printable Calendar Maker

Use `generate_calendar` whenever the user wants a calendar to print or download: "printable calendar", "2027 calendar", "monthly calendar template", "wall calendar", "school year calendar", "calendar with holidays".

1. Pick the layout: `year` (whole year on one page, default), `wall` (cover plus one month per page), `month` (one month, `month: "YYYY-MM"`), or `range` (`start`/`end` as `YYYY-MM`, at most 24 months; a school year is usually `2026-08` to `2027-06`). For an academic wall calendar, use `wall` with `start_month: 8`.
2. Pass `country` (ISO code or name) and `subdivision` (state or region, e.g. `TX`, `BY`, `SCT`) when the user names a place, so public holidays are marked. Without a country no holidays are shown. Add `include_observances: true` only when the user asks for days like Mother's Day or Valentine's Day.
3. Put every birthday, anniversary or event the user mentions in `events`: `MM-DD` repeats every year, `YYYY-MM-DD` is one date.
4. Map wishes directly: Monday weeks -> `week_start: "monday"`; week numbers -> `week_numbers: true`; space to write -> `notes: true`; A4 or Letter -> `paper`; a language -> `language` (en, pl, de, es, fr, it, pt, nl, ja); a colour -> `accent`.
5. If the request has the year or months, call the tool right away; do not ask follow-up questions for optional settings.
6. After the result, give the layout and page count, the number of holidays marked (name a few), any notes verbatim, and the PDF download link.

Use `find_holidays` when the user only wants the list of public holidays for a country and year, without a PDF.

Do not use these tools to add events to Google, Outlook or Apple calendars, to count business days, or to convert dates to lunar, Hijri or Hebrew calendars.
