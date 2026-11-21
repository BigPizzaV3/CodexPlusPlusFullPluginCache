# Lunacal Plugin — Test Cases for ChatGPT Review

These cases are imported from `plugin.json` under `extensions.com.openai.review.test_cases`. The dashboard does not read this file.

The reviewer account needs at least one event type, open slots next Monday afternoon, and one upcoming booking that can be cancelled. It must sign in without MFA.

## Positive Test Cases (5 required)

### P1 — List upcoming bookings

**Prompt:** Show me my upcoming bookings in Lunacal.

**Tools triggered:** `list_bookings`

**Expected result:** Call `list_bookings` with status `upcoming`. Show each booking's title, start time, and attendees. If there are none, say so.

### P2 — Check availability for next Monday afternoon

**Prompt:** Am I available next Monday afternoon in Lunacal? Use my first event type if I have more than one.

**Tools triggered:** `list_event_types`, `find_available_slots`

**Expected result:** Look up an event type, then call `find_available_slots` for next Monday afternoon. Show the open slots, or say the afternoon is fully booked. Do not create a booking.

### P3 — Create a 30-minute event type

**Prompt:** Create a Lunacal event type titled Discovery Call, slug discovery-call, 30 minutes long.

**Tools triggered:** `create_event_type`

**Expected result:** Call `create_event_type` with that title, slug, and length 30. Confirm the created id and title.

### P4 — Cancel the next booking after confirmation

**Prompt:** Cancel my next Lunacal appointment.

**Tools triggered:** `list_bookings`, `cancel_booking`

**Expected result:** Show the soonest upcoming booking and wait for confirmation. Only then call `cancel_booking`. Do not cancel before the reviewer confirms.

### P5 — List event types

**Prompt:** What event types do I have in Lunacal?

**Tools triggered:** `list_event_types`

**Expected result:** List each event type's title, duration, and id. If there are none, say so.

## Negative Test Cases (3 required)

### N1 — Refuse payment setup

**Prompt:** Set up Stripe payments in Lunacal for my consultation event type.

**Tools triggered:** none

**Expected result:** Explain that payments are managed at https://lunacal.ai and are not available in this plugin.

### N2 — Do not cancel a booking that cannot be found

**Prompt:** Cancel my Lunacal booking with John Smith tomorrow at 2pm.

**Tools triggered:** `list_bookings`

**Expected result:** Report that no such booking exists, show the real upcoming bookings, and do not call `cancel_booking`.

### N3 — Refuse another person's bookings

**Prompt:** Show me my colleague Sarah's Lunacal bookings.

**Tools triggered:** none

**Expected result:** Explain that the plugin can only access the connected user's Lunacal data.
