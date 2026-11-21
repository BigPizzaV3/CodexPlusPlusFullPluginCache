---
name: book-this-inquiry
description: Turn one private-event or catering inquiry in Excellent into a booking — convert the lead to an event, check which rooms fit and are free, book the room (or queue a hold), or turn the guest's hold into the event, and draft the reply to the guest for a person to send. Use for "book this inquiry", "book the Adler inquiry into the Garden Room", "turn this lead into an event", "hold the terrace for the Kim party", "the Kims are ready, book their hold", "put a hold on the patio for Friday", "pencil them in".
---

# Book this inquiry

This skill makes changes in Excellent, each one undoable, and drafts the guest's reply. It never sends the
reply, takes a payment or confirms anything to the guest: a person sends the reply from Excellent.

**Before every change,** say exactly what you will change and wait for a yes, unless the person already asked
for that exact change. **After every change,** give the `change_id` it returned and say it can be undone.

## 1. Find the inquiry

`search` the name or email the person gives (`kind: "lead"`), or `list_leads` with `status: "new"`. Read back
who asked, the date, the party size and the event type. If the inquiry has no date, ask for one before
looking at rooms.

## 2. Check the rooms

`space_availability` with the inquiry's `date`, its `party_size`, and the venue (`location`, ids from
`overview`'s `locationList`) if the inquiry or the person names one. Offer the rooms that fit and are free
for the time asked, each with its free stretch on the venue's clock. If a hold is in the way, name the holder
and when it lapses. A free stretch is not a reservation until the next step.

## 3. Make the booking (on a yes)

**If the guest already holds the room** (a hold in their name from earlier), `book_room` would be refused over
it: convert the hold instead. `convert_hold_to_event` with the `hold_id` (from `space_availability` or
`agenda`), the inquiry's `party_size` and a `title` makes a tentative event in the hold's room and window,
its holder the host. Don't also convert the lead, which would make a second event; the inquiry is not linked
to the new event, so say so and offer to move it to `qualified` with `set_lead_status`. It is refused while
another hold is ahead of the guest's, or once the hold has lapsed. Otherwise:

1. `convert_lead_to_event` with the `lead_id` — the event is created at the lead stage, its host the contact
   holding the inquiry's email. A lead converted already answers its event; use that one.
2. Then one of:
   - **Book the room:** `book_room` with the `event_id`, the `space` and the window (`starts_at`, `ends_at`, ISO
     instants with the venue's offset). If it is refused for a different venue day, ask before retrying with
     `move_event: true`. If it is refused for a hold, capacity, a booking or a block, say why and offer
     another room or time — never work around a refusal.
   - **Hold it instead** (when the person wants to wait for the guest): `place_hold` on the room and window,
     with the guest's name as `holder_name`. A hold is soft and ranked, and lapses in 14 days unless the person
     names when (`expires_at`).
3. If the person says the guest has agreed, `set_event_status` to `tentative` (or `confirmed` when they say
   so). Confirming is refused while a hold sits on the room — say whose. A new party size is
   `set_event_guest_count`, only when the person gives one.

If a change is refused because the connection may not make changes, say so plainly: the person can book it in
Excellent's calendar, or reconnect the connector with changes allowed.

## 4. Draft the reply

Offer to draft the reply: thank the guest, name the room, date and time that were booked or held, and ask
for anything missing (headcount, menu, budget). Never quote a price the tools did not return. Stage it with
`draft_lead_reply` (`lead_id`, `subject`, `body`, `locale` `es` if the guest wrote in Spanish) and give the
review link: the person reads it, can edit it, and sends it in Excellent.

## 5. Wrap up

List what changed with each `change_id`, the review link for the reply, and one line: "Each change can be
undone (ask me, or say undo); the reply is not sent until you send it in Excellent." If the person wants a
proposal next, draft it with the `build-event-documents` skill.

Safety: no change is made without the person's yes, and each returns a `change_id` that `undo` puts back, once,
for 30 days unless the record has changed since (`recent_changes` lists them). The reply waits behind its review
link. Nothing is sent to the guest, no contract is signed, no deposit is charged and nothing is deleted.
