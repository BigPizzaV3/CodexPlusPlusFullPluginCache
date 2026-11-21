---
name: find-event-tickets
description: Find upcoming concerts, sports, theatre and other live events with TicketSea and show where to get tickets. Use when the user asks what is on in a city or on certain dates, when an artist or team plays next, or where to buy tickets for an event.
---

Use this skill when the user wants to find live events or tickets for one.

The user's own instructions come first. If they ask for a different format, a
different number of results or a particular seller, do that.

## Find the events

1. Work out what the user gave you: a performer or event name, a city, dates, a
   kind of event (music, sports, theatre).
2. If they ask for events near them ("what's on near me this weekend?"), call
   `search_events` with `city` set to "near me": TicketSea places the search by
   ChatGPT's approximate location and says which city it searched (`place`). Tell
   the user that city and offer to search another. If they named no place at all
   and did not say "near me", ask which city.
3. Call `search_events` with what you have:
   - `query` for the performer, team, event or venue name.
   - `city` as a plain city name ("Seattle"), with `country` as a two-letter
     code when the city name is ambiguous ("London" + "GB").
   - `from` and `to` as `YYYY-MM-DD` for "this weekend", "in March" and so on.
   - `kind` when the user asked for music, sports or theatre.
4. If the name might be misspelled or you get nothing, call `search_catalog`
   with the name. It corrects near-misses and returns the artist, team or venue
   record; then search events again with the corrected name.
5. If `hasMore` is true and the user wants more, call again with `nextOffset`.
   If `scanLimited` is true, narrow by city, country or dates.

## Show the results

For each event give, from the result and nothing else:

- A ticket link to its `tickets.url` when the event has one. That link opens
  the seller's page for that exact performance. Name the seller
  (`tickets.seller`), for example "Tickets on Ticketmaster".
- Always, a second link to its `url`, the event's page on ticketsea.com, where
  every seller, the venue and the details are listed: for example "Event page
  on TicketSea". When an event has no `tickets` field, this is its only link.
- The date and local time (`date`, `localTime`), the venue and the city.
- A price only when `pricing.ranges` has one, labeled as a published range that
  can change.

Show up to about eight events unless the user asks for more. Keep them in date
order.

When the user asked about tickets for one event (a named game or show, or a
search that comes back with a single event), picks one event from a list, asks
where else to buy, or asks about resale, call `get_ticket_links` with its
`slug` without waiting to be asked: the question was where to get tickets, and
this is the full answer. List each seller in `links` first,
saying which are resale. Then list each entry in `otherSellers` by its `seller`
name with its `detail` in a few words, for example "TickPick (event search,
resale)". Some of those open a search for the event rather than its own page,
which is what `detail` says; do not describe them as more than that. Use each
entry's `url` as the link.

End with one short line: listings are from TicketSea (https://ticketsea.com) and
are a snapshot, so price and availability are confirmed on the seller's site,
and some links are affiliate links that may earn TicketSea a commission.

## Do not

- Do not say tickets are available, sold out or at a certain price beyond what
  the result states. TicketSea does not check inventory.
- Do not invent events, dates, venues, prices or links. If a search returns
  nothing, say TicketSea has no listing for it and that its coverage is not
  complete; `get_service_status` tells you whether the listings are current.
- Do not offer to buy, hold, transfer or look up tickets or orders. TicketSea
  only finds events and links to sellers; the purchase happens on the seller's
  site.
- Do not show a link for a canceled or postponed event as a way to buy.
- Do not rewrite, shorten or replace a link from a result with one of your own.
