---
name: get-started
description: Introduce Arketa after the studio connects, confirm which studio is connected, and suggest first questions.
---

Call `get_studio_context` and tell the user which studio they are connected to (name, timezone, locations).

Then explain in two or three sentences what they can ask: revenue, attendance and sales reports; the class schedule and how full classes are; client lookups with bookings, purchases and forms; and the memberships, packs and class types the studio sells. Mention that Arketa is read-only here, so it can answer questions but cannot book, cancel, refund or change anything.

Finish by offering three example questions tailored to what `get_studio_context` returned, for example last month's revenue by week, this Saturday's schedule, or the top clients by visits.
