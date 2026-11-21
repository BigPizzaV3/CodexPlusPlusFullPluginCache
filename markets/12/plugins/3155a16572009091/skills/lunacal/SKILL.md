---
name: lunacal
description: Use when the user asks to view, create, modify, cancel, reschedule, or otherwise manage Lunacal bookings, event types, or availability. Always use the connected Lunacal MCP tools rather than guessing or reproducing Lunacal data locally.
---

# Lunacal

Use the connected Lunacal MCP server at `https://mcp.lunacal.ai/mcp` as the source of truth for all scheduling data and actions.

## Authentication

The MCP server handles authentication on behalf of the connected user. Never ask the user to paste access tokens, API keys, or credentials into chat. If tools return an auth error, tell the user to reconnect their Lunacal account through the plugin settings.

## Rules

- Always use the Lunacal MCP tools for every read or write operation. Never invent or estimate availability, bookings, event types, or profile data.
- Before creating or rescheduling a booking, check availability with the appropriate Lunacal tool when the server exposes an availability operation.
- For destructive actions, state what will change and ask the user to confirm when the request is ambiguous. That includes cancelling a booking, rescheduling a booking, overwriting an event type, and hiding an event type from the public booking page.
- If a requested feature is not exposed by the MCP server, say so rather than pretending it exists.
- Prefer the server's current tool schemas over any assumptions about Lunacal's API.
- When a tool returns paginated results, offer to fetch the next page rather than silently truncating.

## Tool Categories

### Bookings
- **List bookings** — use when the user asks to see upcoming, past, or all bookings. Apply date filters to narrow results.
- **Get booking** — there is no separate get-booking tool. Call list bookings and match the uid, attendee, or time the user named.
- **Cancel booking** — confirm the booking details before cancelling. State what will be cancelled. Lunacal emails the attendees, and cancellation cannot be undone.
- **Reschedule booking** — check availability for the new slot, then confirm before rescheduling. Rescheduling overwrites the current time and emails the attendee.

### Availability
- **Find available slots** — use whenever the user asks "am I free on X" or "what slots do I have". Include the date range and timezone. This does not create a booking.
- Always state the timezone when reporting availability slots.

### Event Types
- **List event types** — show the user all their current event types (name, duration, and id).
- **Get event type** — use before creating a booking when the event type has required questions.
- **Create event type** — ask for name, slug, and duration at minimum. Confirm settings before creating. This adds a record and does not email anyone.
- **Update event type** — ask which field to change and confirm the new value. locations, booking fields, and metadata replace the whole stored value.
- **Publish or hide event type** — confirm before hiding an event type, because that removes it from the public booking page.

## Common Prompts and How to Handle Them

| User says | What to do |
|---|---|
| "What's on my calendar today/this week?" | Call the list-bookings tool with a date filter |
| "Am I free Thursday afternoon?" | Call the availability tool for Thursday |
| "Create a 1-hour consultation event type" | Call create-event-type with name and 60-min duration |
| "Cancel my 3pm appointment" | Identify the booking, confirm with user, then cancel |
| "Reschedule my meeting with Alice" | Find the booking, check new slot availability, reschedule |
| "Show me all my event types" | Call list-event-types |
| "What's my Lunacal booking link?" | Look up the user's profile or event type booking links |

## Out of Scope

These features are managed in the Lunacal dashboard and are **not** available via MCP tools:

- Payment processing and Stripe/PayPal configuration
- Coupon and discount creation
- Website embed code generation
- Billing and subscription management
- SMS/email reminder templates
- Weekly working hours and schedule editing
- Team member management and round-robin setup
