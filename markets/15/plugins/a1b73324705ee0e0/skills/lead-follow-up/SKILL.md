---
name: lead-follow-up
description: Triage the private-event and catering inquiries waiting on a reply in Excellent — who asked, for what date and party size, whether a room fits — and draft replies into Excellent for a person to review and send. Use for "which leads haven't we answered", "follow up on new inquiries", "lead triage", "draft replies to the new inquiries", "answer the new inquiry", "reply to the Garcia rehearsal dinner request", "do we have room for 40 on the 14th?", "write back to that lead".
---

# Lead follow-up triage

This skill reads, and drafts replies. It never contacts a guest: each reply is staged as a draft on the
inquiry, and a person reads it, can edit it, and sends it in Excellent, signed in as themselves.

## 1. Collect

For one inquiry the person names, `search` it (`kind: "lead"`), read back who is asking, the date, the party
size and what they wrote, check its rooms as in step 3 below, and go straight to drafting its reply. Otherwise:

1. `list_leads` with `status: "new"` (and, if the person asks, a second call with `status: "contacted"`).
   Keep paging with the answer's `next_offset` until it is null.
2. `agenda` (default 7 days) — its `leads_waiting` names the inquiries nobody has answered yet, which is the
   most urgent set.
3. For each inquiry that names a date and a party size, call `space_availability` with that `date` and
   `party_size` (for a group with several venues, the venue's `location` from `overview`). Each room says
   `fits_party` and lists its `free` stretches. A free stretch is not a reservation: only a person books, in
   Excellent.
4. If an inquiry looks like a returning host, `search` their name or email to find past events.

## 2. Write the triage

Sort oldest first. For each inquiry, one line: name, event type, date asked for, party size, source, days
waiting, and one of:

- **Room fits and is free** — name the rooms.
- **Fits, but the date is busy** — name what is in the way (a booking, a hold or a block).
- **No room fits the party size.**
- **No date given** — the reply needs to ask for one.

## 3. Draft replies

If the person asks, write a short reply per inquiry in the venue's voice: thank them, answer the date and
room question with what the tools showed, and ask for anything missing (date, headcount, budget). Write in the
guest's language (English or Spanish). Never promise a room is held or booked, and quote no price, deposit or
minimum unless the person gives it to you. Ask the person anything you would otherwise guess. Show the wording
first.

Then stage each one the person wants with `draft_lead_reply` (`lead_id`, `subject`, `body`; `locale: "es"` for
a guest who wrote in Spanish). It needs an inquiry with an email address; for one with none, say so and draft
nothing. Give back each review link: the person opens it in Excellent, can edit the reply, and sends it there —
a new inquiry then moves to contacted. To find a link again later, `get_review_link` with `kind` `reply` and the
draft's `id`.

Say plainly that nothing is sent until they send it. To book a room for an inquiry, use the
`book-this-inquiry` skill.

Safety: this skill reads and drafts. Each reply waits in Excellent behind its review link; nothing is sent to a
guest from ChatGPT, and nothing is booked, held, charged or deleted.
