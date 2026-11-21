---
name: weekly-owner-report
description: The owner's weekly read and Monday recap for a restaurant group on Excellent — revenue booked, collected and outstanding, booking pace against goal, pipeline and win rate, lead sources and the per-venue rollup, plus the week ahead by day (events, holds to decide, payments due, unanswered inquiries and shifts nobody is on). Use for "weekly report", "Monday recap", "what's this week look like", "what needs me this week", "how are we pacing against goal", "which location is behind", "owner update".
---

# Weekly owner report

Read-only. This skill changes nothing in Excellent.

## 1. Collect

1. `report` with `period: "month"`, and again with `period: "year"` (or the window the person asks for:
   month, quarter, year or all). It returns revenue (booked, collected, outstanding), pace against the last
   period with an on-track verdict and the percentage of the annual goal, the pipeline by stage and win rate,
   the lead funnel, booking sources and the per-location rollup.
2. `overview` — the group's headline figures and venues.
3. `agenda` with `days: 7` (or the window the person names; one venue with `location`) — the week ahead by
   day: bookings with time, rooms, host and balance; holds that lapse this week; payments owed or overdue;
   inquiries nobody has answered; and its ranked `suggestions`, most urgent first, each with its link into
   Excellent.
4. `schedule_week` — the stretches of opening hours nobody is scheduled for, open shifts, and whether each
   venue's week is still a draft staff can't see. If the module is not switched on, skip it and say so.

Read `dataBasis` and `dataBasisNote`: say at the top whether the figures count real records, sample records,
or real records with sample rows set aside. Booked and outstanding include draft invoices; say so once.

## 2. Write the report

Keep it to one screen:

- **Headline** — the on-track verdict in one sentence, with the percentage to goal.
- **Money** — booked, collected, outstanding for the month and the year to date.
- **Pipeline** — events by stage, win rate, the lead funnel.
- **Where bookings come from** — top sources.
- **By venue** — one line each; name the venue that is behind and by how much.
- **The week ahead** — event count, the biggest events, holds to decide, payments due, inquiries waiting,
  and the top few `suggestions`.
- **Staffing** — uncovered stretches and open shifts on the busy days.

Amounts arrive in minor units (cents): divide by 100. Use the report's figures as given; don't recompute
them. Then offer the next step: answer an inquiry (`lead-follow-up`), staff the gaps (`staff-schedule-check`) or
chase what is owed (`money-owed`).

Safety: this skill only reads. Nothing is drafted, changed, sent, charged or deleted.
