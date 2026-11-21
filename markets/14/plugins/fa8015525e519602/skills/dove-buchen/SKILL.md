---
name: dove-buchen
description: Use when a user wants to find, price or book a Dove Living apartment in Schwandorf (Bavaria, Germany).
---

# Book a Dove Living apartment

Dove Living rents three self-catering apartments (up to 8 or 6 guests) at Bahnhofstraße 9, 92421 Schwandorf, Germany.
All availability and prices come live from the operator's calendar through the Dove Living MCP tools. Never invent
or calculate prices yourself.

1. Ask for arrival date, departure date and number of guests if they are missing. Dates use `YYYY-MM-DD`.
2. Call `verfuegbarkeit_suchen(von, bis, gaeste)`. Show free apartments with their final price (cleaning and VAT
   included). If nothing is free (e.g. minimum stay), explain the reason and offer `belegungskalender(listing, von)`
   to find free dates.
3. Call `angebot_berechnen(listing, von, bis, gaeste)` for the price breakdown. Before a booking, tell the user the
   cancellation terms exactly as returned in `stornobedingungen.text` (concrete deadlines for their arrival) and the
   deposit (`kaution`).
4. Only when the user explicitly wants to book, collect first name, last name and e-mail (phone optional) and call
   `buchung_anfragen`. It reserves the dates for 30 minutes and returns a link to the operator's payment page on
   buchen.dove-living.de. Tell the user that the booking becomes binding only when they click "Zahlungspflichtig
   buchen" there and complete the card payment. You cannot pay for the user.
5. After payment, `buchung_status(buchungs_id)` shows the confirmation and reservation number.

Changes and cancellations are handled by e-mail: info@dove-living.de. Answer in the user's language.
