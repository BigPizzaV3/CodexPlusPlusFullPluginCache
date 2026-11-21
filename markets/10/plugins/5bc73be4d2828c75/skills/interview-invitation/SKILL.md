---
name: interview-invitation
description: "Draft a clear interview invitation or rescheduling message with confirmed stage, time zone, duration, format, participants, and preparation."
license: MIT
metadata:
  version: "0.2.4"
---

# Interview invitation

## Inputs

Confirm candidate and role, interview stage, host, duration, format, time zone, available slots or an approved scheduling link, location/video link, preparation, and contact for changes. An interview invitation differs from cold opportunity outreach.

## Procedure

1. Determine whether the message proposes times or confirms a booking. Do not say “confirmed” unless the booking exists and all required parties have agreed.
2. Use explicit dates with a year when ambiguity is possible. Include the time zone and UTC offset for that date when known. Check daylight-saving conversion with an authoritative calendar/time tool; do not rely on recalled offsets.
3. Explain who the candidate will meet, the purpose, and what to expect. Keep preparation proportionate and supplied by the hiring team. Never invent an assessment or unpaid work requirement.
4. Offer one clear action: choose a slot, use a supplied scheduling link, or confirm attendance. Include a contact for rescheduling and a discreet way to request access arrangements without asking for medical details.
5. For rescheduling, acknowledge the change, show the new proposed details, and avoid implying the old calendar event has been canceled unless it has.

## Output

Return subject, body, a logistics checklist, and unresolved booking details. Distinguish proposed, booked, and sent states.

## Fictional example

Confirmed inputs: Jordan has agreed to a first interview for Northbank's backend role; 45-minute video conversation with Priya; the recruiter supplied a booking link and no fixed date.

Subject: First interview for the backend engineer role

Hi Jordan,

We'd like to arrange a 45-minute video conversation with Priya about the backend engineer role at Northbank. You'll discuss your recent work, the team's reliability challenges, and your questions about the role.

Please choose a time using the scheduling link below. The scheduler will display the time in your selected time zone. No presentation is needed.

If none of the times work, or you'd like an adjustment to the interview format, reply and we'll help.

Use the actual supplied scheduling link in the final message. This example does not create or imply a booking.

## With Vitae

Read the candidate and job with available tools. Inspect the live catalog for booking and email tools. Use them only for the specific action authorized by the user, with confirmed logistics and Vitae's approval requirements. If the action is unavailable, return the invitation and a precise handoff for the recruiter to send or book in Vitae. Never invent a meeting URL or claim an event exists.

## Completion and handoff

The invitation is ready once all required logistics are confirmed or explicitly proposed. Pass the job, interview stage, and agreed assessment scope to `interview-kit`.
