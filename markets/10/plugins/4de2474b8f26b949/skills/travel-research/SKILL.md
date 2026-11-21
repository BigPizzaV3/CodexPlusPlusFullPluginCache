---
name: travel-research
description: Coordinate a travel comparison combining flights and accommodation or several explicitly requested travel sources with HasData. Use for multi-part trip research; single flights, hotels and Airbnb tasks have dedicated skills.
---

# Coordinate a bounded trip comparison

Read `../hasdata-research/SKILL.md`. Use `../flight-research/SKILL.md` for fixed-date fares or flexible deals, `../hotel-research/SKILL.md` for Google Hotels/Booking, and `../airbnb-research/SKILL.md` for short-term stays. A single-component request uses that component only; do not automatically add flights, hotels and Airbnb.

Collect materially missing route, dates and traveler details for the requested priced itinerary. An explicitly flexible-date deals search must not be turned into an invented fixed stay. Preserve supplied airports and sources; never manufacture geographic IDs.

Source schemas differ. Booking search and details require rooms, adults and children; when children > 0, collect one age 0-17 per child and pass childrenAges as a comma-separated list. Never silently substitute adults-only. For other sources, follow their own required party/age fields. Keep requested filters distinct from actually applied source context.

Do not use one zero-count encoding across providers. Booking requires children:0 for no children. Google Flights/deals reject optional zero children or infant counts, Google Hotels rejects children:0, and Airbnb rejects optional zero children/infants/pets; omit those absent groups instead, preserving positive supplied counts. Google Hotels cannot apply rooms in the checked schema. Read the selected component skill before its call.

Compare returned currency and price basis alongside dates, travelers/rooms, stops or amenities. Nightly, per-person and total-party prices cannot be silently added into a final trip total. Calculate only compatible returned components whose taxes/fees and inclusion rules are established; otherwise show them separately.

Retain actual source links, observations and continuation tokens. No automatic pagination/retries, payment, reservation, traveler-document entry or guaranteed live inventory. A shortlist supports planning, not a confirmed booking.
