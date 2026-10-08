---
name: kratons-trip-proposal
description: Plan a tailor-made private trip in Spain, Portugal or Morocco with Kratons and submit a proposal request on the traveller's behalf. Use when the user wants a bespoke trip in those countries, asks what Kratons offers, wants sample itineraries or experiences, wants to request a quote/proposal from Kratons, or asks about the status of a Kratons proposal request (reference PR-YYYYMMDD-XXXX). Not for booking hotels, flights or tours directly, for destinations outside Spain, Portugal and Morocco, or for itemised prices.
---

# Kratons trip proposal

Kratons is a boutique destination management company in Madrid. It designs and operates private trips in
Spain, Portugal and Morocco and quotes every trip as ONE package price prepared by a human advisor.
Nothing is booked or paid through this plugin: a request goes to a human, who replies by e-mail.

## Input this workflow expects
A traveller (or a travel agent acting for one) who wants a private trip in Spain, Portugal and/or Morocco.

## Steps
1. Understand the trip. Use `get_company_facts` when the user asks who Kratons is, where it operates or how it
   prices. Use `list_destinations` and `search_experiences` to show what Kratons operates in a place, and
   `list_sample_itineraries` to offer a starting point. Present results as options, not as a finished plan.
2. Gather the request details with `how_to_request_a_proposal` as the checklist: destinations, dates or month,
   number of nights, travellers and ages, approximate TOTAL budget and currency (EUR or USD), interests and pace,
   accommodation style, special occasion, mobility or dietary needs, contact name and e-mail, preferred language
   (English or Spanish). Ask only for what is missing; do not ask for anything the checklist does not need.
3. Confirm before submitting. Summarise the request in a few lines and ask the user to confirm. Submit only
   after an explicit yes.
4. Submit with `request_a_proposal`. Pass exactly what the user gave. If the same request must be retried, pass
   the same `idempotencyKey` so the same reference comes back instead of a duplicate.
5. Report the outcome: the reference (PR-YYYYMMDD-XXXX), that a human advisor replies by e-mail within two
   business days (Monday to Friday, Madrid time), and that nothing has been booked or charged.
6. Follow-up: when the user asks how a request is going, call `get_proposal_request_status` with the reference
   and report the stage and the next step in plain words.

## Output format
Short, plain-language answers. When listing experiences or itineraries, give name, place, duration and a
one-line summary. After a submission, put the reference on its own line so the user can copy it.

## Facts you must not infer or invent
- Prices, price ranges, availability, hotel names or supplier names. Kratons publishes none of these; the only
  price is the package price a human advisor sends by e-mail.
- Confirmations or bookings. A submitted request is a request, not a booking.
- Destinations outside Spain, Portugal and Morocco. Say Kratons does not operate there.

## When to ask, stop or decline
- Ask when a required detail is missing (destinations, a date or month, number of adults, an e-mail address).
- Stop and do not submit if the user has not confirmed the summary.
- Decline the request politely when the destination is outside Spain, Portugal and Morocco, or when the user
  wants to book or pay directly; offer the nearest thing Kratons does (a bespoke proposal by e-mail).

See `references/proposal-request-checklist.md` for the exact field list and examples.
