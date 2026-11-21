---
name: wedding-timeline
description: Work out what to do and when before a wedding, invitation and RSVP dates, and when vendor payments fall due. Use when someone asks for a wedding checklist or timeline, when to send invitations, or what is due when.
---

Run the tool for this and answer from its result: its amounts add up exactly and its dates count back from their day.

Use this for anything about dates before the wedding.

- **What to do and when:** run `build_wedding_checklist` with the wedding date, what is already
  booked (`venue`, `catering`, `photographer`), and `destination: true` for a destination
  wedding. Name the next two or three tasks and when; the view lists the rest by month. If the
  date is close, say that overdue tasks have been spread from today.
- **Invitations and RSVPs:** run `rsvp_dates` with the wedding date, and the caterer's headcount
  date if they know it. Give the send date, the RSVP date to print, and the headcount date.
- **Payments:** run `plan_vendor_payments` with each vendor's total, deposit and due dates. Point
  out the heaviest month and anything overdue.

Dates are worked out from typical lead times, not their contracts. When a contract says
otherwise, the contract wins; tell them so if it matters.
