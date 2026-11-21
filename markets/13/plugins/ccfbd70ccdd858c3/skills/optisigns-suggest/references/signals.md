# Signals: what each thing you can see tells you

## Screen names → purpose

| Name contains | Purpose | Ideas that fit |
|---|---|---|
| menu, counter, drive-thru, bar, cafe | Menu board | dayparts, specials, new item, combo |
| lobby, reception, entrance, front desk | Welcome | hours, today's events, weather, welcome message |
| break room, floor, warehouse, plant | Staff comms | safety, recognition, shift notes, KPIs |
| waiting room, clinic, patient | Waiting room | wait time, reminders, seasonal health notices |
| classroom, hall, library, campus | Schedules | exams, events, countdowns, extended hours |
| window, storefront, checkout, retail | Promotion | offers, featured product, reviews, hours |
| gym, studio, class | Class schedule | today's classes, spots left, challenges |
| conference, meeting, ballroom | Rooms | room status, today's agenda, wayfinding |

## Content and age

- An asset or playlist item whose name or text carries a past date or event → retire or refresh.
- A customer-facing playlist unchanged for 60+ days → refresh.
- Only static images, no app → one self-refreshing item (weather, clock, calendar, reviews, social,
  news) fits most screens.
- A schedule with nothing past this week → fill the gap.

## Industry → what their peers actually show

| Industry | Commonly chosen |
|---|---|
| restaurant, retail, hospitality | Instagram, Google Reviews, Facebook |
| education | Google Calendar, Google Slides, Countdown |
| manufacturing, warehouse | dashboards (Power BI), News/RSS, safety, days without incident |
| IT, corporate, professional services | calendars, announcements, News/RSS, KPI boards |
| healthcare | wait time, seasonal health campaigns, services offered |

## Showing a data source (first that fits)

Built-in app for it (Power BI, Slides, Sheets, calendars, social) → structured data in a Designer
template (OptiSync) → public web page (Website app) → login-protected page (Web Scripting, or Secured
Dashboard for heavy pages and MFA).

## Calendar classes (the dates are yours to compute and check)

- Civic holidays for the user's country and region.
- Commercial moments: Mother's and Father's Day (dates differ by country), Valentine's, July 4,
  back-to-school, Black Friday, Boxing Day, New Year.
- Season and time changes: daylight saving start and end (not every region observes it), first
  frost, heat waves, flu season.
- Workplace cycles: open enrollment, quarter and fiscal year end, performance reviews, payroll dates.
- Industry: tax season, graduation, restaurant week, inventory, conference season.
- The user's own events, when their calendar is connected.
