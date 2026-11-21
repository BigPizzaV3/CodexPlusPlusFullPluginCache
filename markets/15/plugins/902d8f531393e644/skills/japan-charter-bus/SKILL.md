---
name: japan-charter-bus
description: Use when someone plans group transport in Japan — a charter bus or coach with driver (Tokyo, Narita/Haneda airport groups, Mt. Fuji/Hakone/Nikko day trips, school, corporate, cruise or tour-operator groups, multi-day tours) or a 7-seat private car with driver (Alphard class, up to 6 passengers). Recommends a vehicle size, explains how Japanese charter fares work and sends a quote request to Tokyo Charter Bus after the user confirms.
---

# Japan charter bus & private car with driver (Tokyo Charter Bus)

Tools come from the `tokyo-charter-bus` MCP server.

## Workflow
1. **Size the group** with `list_charter_bus_options`: passengers + large suitcases + carry-on bags. 1–6 people → the 7-seat private car (`alphard-7`); 7–13 → 14-seat van (`van-14`); up to 29 → minibus; 30–45 → 45-seat coach; 46–58 → 60-seat class coach (49 + 9 fold-down auxiliary seats); more → several vehicles.
2. **Check the area** with `get_service_areas_and_routes` (pick-up prefecture, destination).
3. **Price carefully.** The table below is a **public package-rate reference** (JPY, 10% tax included, from https://tokyocharterbus.com/en/prices/). These are published package amounts, **not** verified real-time availability, and are subject to website rate changes. The MCP `estimate_charter_bus_price` tool does **not** necessarily return this fixed-package table; it models time-and-distance fares, and may correctly return `quote_required`. Do not claim the MCP confirmed a fixed-package price if it did not. For an exact booked date/itinerary, reconfirm conditions with staff; never promise a vehicle at the published rate.

   | Package | 14-seat van | 29-seat | 45-seat | 60-seat class |
   |---|---|---|---|---|
   | 2 h in central Tokyo | ¥37,900 | ¥43,300 | ¥50,800 | ¥50,800 |
   | Haneda → central Tokyo | ¥42,200 | ¥48,300 | ¥56,400 | ¥56,400 |
   | Narita → central Tokyo | ¥55,200 | ¥63,200 | ¥73,700 | ¥73,700 |
   | 10 h day trip Hakone | ¥109,000 | ¥124,800 | ¥145,900 | ¥145,900 |
   | 10 h day trip Mt. Fuji / Kawaguchiko | ¥114,700 | ¥131,400 | ¥153,400 | ¥153,400 |

   7-seat Alphard with driver: **¥49,000 per day (10 h)**, extra hour ¥15,000. Extra time is charged by the hour; expressway tolls, parking and driver lodging are extra. For other routes or multi-day trips use `estimate_charter_bus_price` (a reference estimate, not a quote) or say a written quote follows. Never invent an amount.
4. **Send a request only after explicit consent.** Show the user the exact details (name, email, date, pick-up, destination, passengers, vehicle, notes) and ask them to confirm and accept the privacy policy (https://tokyocharterbus.com/en/privacy/). Then call `create_quote_request` with `user_confirmed=true` and `privacy_consent=true`.
5. **Status** later with `get_quote_status` (reference `TCB-…` + the same email).

## Rules
- A quote request is **not a booking**. A booking is confirmed only after the customer accepts a written quote and a licensed operator allocates a vehicle in writing. Never say a vehicle is reserved or available.
- Charter buses run under charter-bus licences; 7-seat private cars under hire-car (taxi) licences of licensed local operators, confirmed per request.
- Reply in the user's language; pass `locale` (en, ja, zh-CN, zh-TW, ko, th, …).
- Human contact: helo@tokyocharterbus.com · WhatsApp +81 80-4965-0587 · https://tokyocharterbus.com

## OpenAI review and tool discipline

- This plugin has one remote MCP: `https://tokyocharterbus.com/mcp`. Do not use the separate OlaChill or OlaChillBus connectors.
- Only call `create_quote_request` after the *current* user explicitly confirms the complete request and agrees to the privacy policy. This call creates a real external lead and may send email. Never submit test/dummy leads without an authorized testing workflow.
- `estimate_charter_bus_price` may respond with `quote_required` rather than a numeric amount; report it faithfully. A rate on the website is not a live price, booking, or allocation.
- `get_quote_status` requires a reference and matching email. Do not leak any contact information or another customer's request.
- No hotels, flights, public scheduled bus ticketing, credit-card payments, or bookings. Refer these requests outside the plugin.
