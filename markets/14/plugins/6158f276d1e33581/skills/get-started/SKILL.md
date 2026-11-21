---
name: get-started
description: How to use iQuota to find and book independent hotels, apartments and villas directly with the property, with payment at the property.
---

# Getting started with iQuota

iQuota connects you with independent hotels, apartments and villas that publish their own official rates. Bookings go directly to the property: the guest pays at the property, never through the assistant.

## Typical flow

1. **Search** with `search_hotels`: destination, check-in and check-out dates (YYYY-MM-DD), number of adults, children's ages and, optionally, the currency.
2. **Details** with `get_hotel` when the traveller wants photos, amenities, location or payment terms.
3. **Re-check** the chosen option with `check_rate` just before booking (quotes are valid for 30 minutes).
4. **Book** with `book_hotel` only after showing the traveller the property, dates, room, board, total price, cancellation policy and payment terms, and getting their explicit confirmation plus their name, email and phone.
5. **Manage** an existing booking with `get_booking` or `cancel_booking` (booking reference and guest email are required; cancellation shows the fee first).

## Good to know

- Never ask for card details: payment is collected by the property.
- Local tourist taxes, if any, are paid at the property.
- Properties marked as demo show real-looking prices but cannot be booked.
