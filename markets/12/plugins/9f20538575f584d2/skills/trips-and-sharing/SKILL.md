---
name: trips-and-sharing
description: Find, open, keep and share the traveller's Adónde trips. Use when the traveller asks for their trips, wants to reopen or continue a trip, keep it, invite friends to build it together, show it off with a link, or turn a public link off.
---

# Trips and sharing

## Their trips

- `list_trips` returns the signed-in account's trips, newest first. Use a `trip_id` from it with `get_trip` to reopen one and continue planning.
- Every trip made through this connection is already in the traveller's Adónde account. Hand over the `open_trip` link from the result so they can open it in the app or on the web.
- `keep_trip` is for a "Keep this trip" card line (call it with that `intent_ref`).

## Sharing, offered once

When the days have been built and shown, offer once: "Want to build this with friends or show it off? Give me their emails." Never ask twice, and never share without the traveller's yes and the addresses they gave.

- **Build it together:** `share_trip` with `mode: "together"` and `emails`. Each friend gets an invitation to join the trip; it works for 14 days.
- **Show it off:** `share_trip` with `mode: "show"` and `emails`. A read-only link on getadonde.com that anyone can open for 7 days. It is emailed to the addresses given and always returned in the result: hand it over to copy.
- **Turn it off:** `share_trip` with `mode: "show"` and `revoke: true`.
- Up to 10 addresses per call and 20 invitations per trip per day.

## The app

After the offers for stays, tours and the flight are done (or declined), and only when the result's `premium.member` is false, say the result's `premium_moment` once in plain words: the trip is already in Adónde, and the first trip comes with the in-app extras (live interpreter, offline phrases and maps, location sharing, calendar and Excel export, flight monitoring, price watching). Give the App Store or Google Play link from the result. No prices, never twice.
