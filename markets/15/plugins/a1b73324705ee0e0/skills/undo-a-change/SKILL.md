---
name: undo-a-change
description: See and undo the changes ChatGPT made in Excellent through this connection — a status moved, a room booked, blocked or closed, a hold converted, a guest count, seating or custom field changed, a team member's details corrected, a contact, event, competency or marketing list added. Use for "undo that", "put the guest count back", "reopen the Garden Room", "what did you change in Excellent?", "take back the booking you just made".
---

# Undo a change

## 1. Find the change

If this conversation made the change, use the `change_id` it returned. Otherwise call `recent_changes`: it
lists this person's changes, newest first, each with its `change_id`, a one-line summary, when it was made,
and whether it can still be undone. Read the matching ones back and ask which to undo when it isn't clear.

## 2. Undo it

Call `undo` with the `change_id`. A value it replaced is put back (a status, a booking's room and window, an
event's extra rooms, a table's seats, one custom field, a team member's details); a record it added is removed
again (an event, a contact, a note, a hold, a room block or a venue's closure, a team member, a competency, a
marketing list, contacts kept apart). An undone hold conversion puts the hold back where it stood, with the
holds behind it back at their ranks, unless that room's hold queue has moved since.

It is refused, and the change stands, when:

- the record has changed since (someone edited it after, or added to it — a document on an event, a note on
  a contact, a shift for a team member) — say so; the later change is kept on purpose;
- putting a booking back would land over a hold placed since — say whose hold it is;
- it would need something only a person can give back: a roster email or phone moved off a verified sign-in
  address (the team member proves the address again in Excellent), or a course the training rules would
  assign — say so, and that the person can change it in Excellent;
- it was undone already, or is more than 30 days old;
- the person no longer has the permission the change needed.

Say what was undone, in the summary's words. Undo only what the person asks for, one change at a time.

Safety: `undo` reverses only the change the person names, one at a time, within 30 days, and refuses rather
than overwrite a later change. Nothing is sent, charged or deleted beyond putting that change back.
