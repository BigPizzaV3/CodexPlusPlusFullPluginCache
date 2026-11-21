---
name: plan-event-trip
description: Plan a visit to one specific concert, game or show with TicketSea - tickets, where to stay, parking and directions. Use when the user is travelling to an event or asks for hotels, parking or directions for it.
---

Use this skill when the user is going to a specific event and wants help with
the visit, not just the ticket.

The user's own instructions come first. If they only want hotels, or only
directions, give only that.

## Steps

1. Identify the event. If you do not already have its `slug`, call
   `search_events` with the performer or event name and the city or date the
   user gave. If more than one performance matches, ask which one.
2. Call `prepare_event_visit` with the `slug`. One call returns the event
   details, the seller links, the venue address, suggested stay dates and
   search links for hotels, parking, directions and things to do.
3. If `visit.planningAvailable` is false, the event is canceled, past or its
   listing is out of date. Say so, and do not present ticket or travel links.

## What to give the user

- The event: name, date, local time, venue and its address
  (`visit.venueAddress`), with a link to its `url`, the event's page on
  ticketsea.com.
- Tickets: each entry in `links`, by seller name, saying which are resale. Each
  link opens the seller's page for this performance. Then each entry in
  `otherSellers`, by `seller` name with its `detail` in a few words; some of
  those open a search for the event rather than its own page.
- Stay: the suggested check-in and check-out dates (`visit.suggestedStay`), and
  the hotel search link from `visit.travelLinks`. Tell the user to adjust the
  dates and number of guests.
- Getting there: the parking and directions links from `visit.travelLinks`.
- Anything else in `visit.travelLinks`, by its `title`.

Use each link's `title` and `detail` as given. End with one short line: nothing
has been booked, the travel links are searches rather than confirmed rooms or
parking spaces, price and availability are confirmed on each seller's site, and
some links are affiliate links that may earn TicketSea a commission.

## Do not

- Do not say a room, a parking space or a ticket is available or reserved.
  Nothing is booked or saved by these tools.
- Do not invent hotels, prices, distances or travel times that are not in the
  result.
- Do not ask for the user's home address or exact location. A departure city is
  enough if they want general travel advice, and that advice is yours, not
  TicketSea's.
