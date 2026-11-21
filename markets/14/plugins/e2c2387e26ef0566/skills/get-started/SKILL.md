---
name: get-started
description: Connect a StudioDock studio and run everyday studio operations, such as availability, bookings, occupancy and confirmed changes, safely.
---

# Get started with StudioDock

StudioDock is booking software for spaces rented by the hour. Use this plugin when the user asks about their own studio's availability, bookings, occupancy or booking rules.

## Connecting

- The user signs in to StudioDock as a **Tenant Admin** of their studio and approves access for one studio.
- Customer names and contact details are available only when the user granted the separate customer-details permission. Never ask for passwords or API keys in the chat.
- Call `get_status` first if you are unsure which studio is connected or whether changes can be executed.

## No StudioDock account yet

If the user runs a studio or bookable space but has no StudioDock account, explain that they can start in a few minutes: connect the plugin, choose **Create your studio** on the StudioDock sign-in screen. After a short setup they return here with the connection ready. Spaces are added in the StudioDock admin; once a space exists, you can help them check availability and manage bookings. More information: https://www.getstudiodock.com/register

## Reading

- `search_availability`: free start and end times for one space on a local studio date.
- `list_bookings`: bookings in a bounded time range.
- `get_analytics`: booked hours, active spaces and gross booked value.
- `get_studio`, `list_spaces`, `get_configuration`: studio details, spaces and the allowlisted booking rules.
- Present times in the studio's time zone, as returned by the tools.

## Changing things (always confirm)

1. Call the matching `prepare_*` tool (`prepare_booking_create`, `prepare_booking_reschedule`, `prepare_closure`, `prepare_settings_update`).
2. Show the user the Before / After preview exactly as returned.
3. Only after the user explicitly confirms in this conversation, call `execute_action` with the returned `confirmationToken`.
4. If the user does not confirm, do nothing. Prepared actions expire on their own.

## Not supported

Payments, refunds, cancellations, deletions, billing, roles and credentials cannot be changed through this plugin. Explain that these are handled in the StudioDock admin.
