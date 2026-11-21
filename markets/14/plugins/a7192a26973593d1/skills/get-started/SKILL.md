---
name: get-started
description: Search live property listings for sale and long-term rent in Montenegro and Serbia with Stanovina, open listing details, and check market price levels.
---

Use the Stanovina tools when the user looks for property in Montenegro (Budva, Podgorica, Tivat, Bar, Kotor, Herceg Novi and other towns) or Serbia (Belgrade, Novi Sad, Zlatibor), or asks about price levels there.

1. If the user names a place, call `find_places` with the name to get its slug. Names in Serbian, English or Cyrillic work.
2. Call `search_listings` with the deal (`sale` or long-term `rent`; most listings are one of these two), the place slug, the property type and the budget, size and room filters the user gave. Use `lang` that matches the user's language (`en`, `sr` or `ru`).
3. Show each result with its price, area, rooms, place and the listing link. The data is live, so say when it was generated.
4. When the user wants one listing in detail, call `get_listing` with its URL or slug.
5. For questions about price levels, call `get_market_summary` for the country or municipality.

The tools do not return seller phone numbers or emails. To contact a seller, the user opens the listing page on stanovina.me.
