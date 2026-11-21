---
name: staff-schedule-check
description: Check a restaurant group's staff schedule in Excellent — who is on today, the week's coverage per venue, open shifts, stretches of opening hours nobody covers, scheduling warnings and what staff can't see yet — add draft shifts, and correct a team member's role, venue or contact details (undoable). Use for "who's on tonight", "is the week covered", "any open shifts", "check next week's schedule", "add a closing server on Friday", "fill the open Saturday brunch shift", "staff next week", "build the schedule for the patio party", "Ana works at the Mission venue now".
---

# Staff schedule check

This skill reads, can add draft shifts, and on request corrects a team member's details (an undoable change).
It never publishes a week or tells staff anything: shifts it adds stay in the week's draft until a person
publishes the week in Excellent.

## 1. Collect

- Today (or one named day): `schedule_today`, with `date` and `location` if given. Per venue it lists who is
  on (person, role, start and end on the venue's clock, break), the open shifts and each shift's warnings.
- A week: `schedule_week` with any `date` in the week wanted (default this week). Per venue and day it gives
  shifts, people, open shifts, planned minutes, shifts by role and the `uncovered` stretches of opening hours
  (null when the venue has no hours on file).
- If events are on, `agenda` for the same days shows the bookings and party sizes the staff is there for.

If the tool answers that this part of Excellent is not switched on, say so and stop.

## 2. Write the check

Per venue:

- **Publish state** — draft (staff can't see it), published, or published with changes staff don't see yet
  (`unpublished_changes`). Say how many.
- **Gaps** — open shifts and uncovered stretches, by day and time on the venue's clock.
- **Warnings** — in plain words: overlap, double booked at another venue, short rest between shifts,
  inactive or archived staff still scheduled.
- **Busy days** — days with large events next to the people scheduled by role.

End with the three most important fixes for a person to make in Excellent, most urgent first.

## 3. Fill a gap (if asked)

Propose the shifts as a list first: day, start and end on the venue's clock (24-hour), role, and the person
from the roster `schedule_week` returns, or open when nobody is named yet. Ask the person to adjust it, and
don't schedule anyone they haven't agreed to.

Then, once per agreed shift, `draft_shift` with the `location`, the venue `date`, `start` and `end` (HH:MM; an
end at or before the start runs past midnight), the `role`, the person's `staff_id` (leave it out for an open
shift), and an optional `break_minutes` and `note`. Call `schedule_week` again to show the week as it now
stands. Give back the review link, and say staff see nothing until someone publishes the week in Excellent.

## 4. Correct a team member (if asked)

When a role or home venue on file is wrong ("Ana works at the Mission venue now", "Leo is a bartender, not a
server"), find the person's id with `training_roster` (`match` their name), say the old and new values, and
on a yes call `set_staff_details` with the `staff_id` and only the fields that change (`full_name`, `email`,
`phone`, `role`, `location`). Give back the `change_id` and say it can be undone.

- A new role or venue can assign the courses the group's standing rules give it: say so before.
- Moving an email or phone off a verified sign-in address retires that proof, and such a change cannot be
  undone here: say so and ask again before making it.

To add someone, build or assign a course, or define and assign a competency, use the `train-the-team` skill.

Safety: shifts go into the week's draft behind its review link; nobody sees them until a person publishes the
week. A correction to a team member is made only on the person's yes and returns a `change_id` that `undo`
puts back, once, for 30 days. Nothing is sent to staff, published, paid or deleted from ChatGPT.
