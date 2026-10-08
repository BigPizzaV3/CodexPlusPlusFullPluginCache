---
name: nowistay-direct-bookings
description: Create or update direct Nowistay bookings with availability checks, minimum required guest details, pricing, status, operational notes, and optional payment links. Use for manual reservations, direct booking quotes, payment-request bookings, date changes, guest-count changes, and booking corrections.
---

# Nowistay Direct Bookings

Use the booking workflow that matches the user's intent and avoid duplicate lookups.

## Create a booking

1. Resolve the property once with `list_properties`.
2. Check the exact stay dates with `get_calendar_ari` before staging the booking.
3. Reuse details the user already supplied. Do not search the guest base by default. Use `list_guests` only when the user explicitly asks to reuse an existing guest record, and search with information the user already provided.
4. Collect only missing required values: property, arrival, departure, and guest email. Explain that email is required to create and service a direct booking. Ask for optional phone, pricing, guest count, or notes only when the user wants or needs them for this booking.
5. Call `create_booking_preview` with the complete intended booking.
6. Show a compact summary: property, dates, guest, occupancy, price, currency, status, and whether payment will be requested.
7. If the user asked only to prepare the booking, stop. If the user explicitly asked to create it, continue through platform confirmation with `create_booking_confirm` and only the approval token.

When `request_payment=true`, provide a positive amount. Explain that the booking is created as pending, does not hold inventory while unpaid, and auto-confirms after successful payment. Do not promise that a payment link was sent until the confirm result says so.

Never request or accept payment-card data, bank credentials, government identifiers, medical or biometric data, account passwords, access tokens, or unrelated personal information. Keep free-text notes short and strictly operational.

## Update a booking

1. Find the booking with `list_bookings` and read it with `get_booking`.
2. Update only direct bookings created in Nowistay. If the booking came from an OTA, explain that it cannot be edited through this workflow.
3. Check calendar availability before changing dates.
4. If a payment request already exists, do not attempt to change dates or pricing.
5. Stage with `update_booking_preview`, summarize the exact differences, then use `update_booking_confirm` only after the requested confirmation.

Do not retrieve guest contact details or private booking notes unless the user explicitly asks for that information and it is necessary for the requested booking operation.

Never reconstruct a confirm payload. Confirm tools receive only the one-time approval token returned by their matching preview.
