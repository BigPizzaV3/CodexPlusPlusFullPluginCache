---
name: randevu-takvimim
description: Find hair and beauty businesses in Turkey (hair salons, bridal hair, barbers, nail studios, beauty centers, spas, laser hair removal, makeup), compare ratings, prices, services and reviews, and book an appointment at registered businesses. Use when the user wants such a business in a Turkish city or district, asks about a specific one, or wants to book an appointment.
---

# Randevu Takvimim

Search and compare hair and beauty businesses across Turkey and book at the ones
registered on Randevu Takvimim. All data comes from the Randevu Takvimim MCP tools.

Coverage today is hair and beauty. Other categories (clinics, veterinarians, auto
services…) have no listings yet: if `list_categories` shows `count: 0` for what the
user wants, say so plainly instead of suggesting unrelated businesses.

## When to use

- "Find a barber in Kadıköy", "best-rated bridal hair salon in Pendik", "nail studio in İzmir"
- Questions about one business: services, prices, hours, location, reviews
- "Is there a free slot tomorrow at …", "book me a haircut at …"

Do not use for product advice, travel, or businesses outside Turkey.

## Workflow

1. **Search** with `search_salons`. A plain-language `query` works
   ("kadıköy berber"); city, district and category are parsed from it. Use
   `list_categories` and `list_cities` only when you need valid keys or coverage.
2. **Details** with `get_salon` (services with `service_id`, prices, hours, photos,
   map link) and `get_reviews` for customer reviews.
3. **Availability** with `get_available_slots` (date as `YYYY-MM-DD`, plus the
   chosen `service_ids`). Works only for businesses with `verified: true`.
4. **Confirm** — before booking, show the user the business, date and time, service,
   price, and the name and phone number to be used, and wait for an explicit yes.
5. **Book** with `create_booking`, copying `start_at` and `employee_id` from the
   chosen slot exactly. At least one `service_id` is required.

## Rules

- **Keep the `verified` distinction.** `true` = registered business: it manages its
  own listing, online booking works, ratings come from this platform.
  `false` = directory entry compiled from public sources: unverified, no online
  booking, reach it by phone. Say this plainly and never present its rating as
  confirmed. Reviews with `source: "public"` are likewise compiled, not verified.
- **Never call `create_booking` without the user's explicit confirmation**, and never
  book on behalf of someone who did not ask for it.
- **Times are Turkey local time (+03:00).** Show slot times to the user as returned
  and pass them to `create_booking` unchanged. Do not convert to UTC or add hours.
- If a slot is taken or the booking is rejected, relay the error message and offer
  other slots from `get_available_slots`.
- Cancelling or changing an appointment is not supported. Send the user to the
  business page (`url`) or its phone number.
- Prices, hours and availability can change. Cite each result's `url` as the source.
