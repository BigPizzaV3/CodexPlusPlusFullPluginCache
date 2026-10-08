---
name: nowistay-guest-messaging
description: Find guest conversations, read recent messages, summarize context, draft replies, and send messages through Nowistay. Use for "show the last messages", "reply to this guest", booking-based conversation lookup, follow-up replies, and multilingual guest communication.
---

# Nowistay Guest Messaging

Keep the conversation natural and hide implementation details from the host.

## Find and read

1. Resolve a guest or booking with `list_guests`, `list_bookings`, or `get_booking` using information already supplied by the user. Prefer a booking reference, property plus stay dates, or name. Do not ask for email or phone merely to disambiguate when operational context can identify the stay.
2. Use `list_threads` with `booking_id` when a booking is known; otherwise narrow by property.
3. Use `get_thread_messages` once with the exact requested message count. Preserve chronology when presenting the exchange.
4. For a follow-up such as "tell them...", reuse the guest and conversation already established in the current task unless it became ambiguous.

Say "I did not find a conversation" when none exists. Do not mention missing thread IDs, channel IDs, database records, or other private implementation details. Do not retrieve or expose a guest's email, phone, postal address, private notes, or unrelated booking data unless the host explicitly asks for the specific information and it is needed for the requested operation.

## Draft and send

1. Base the reply on the actual conversation, booking, and property context. Do not invent policies, promises, prices, or availability.
2. Match the guest's language and the host's requested tone. Keep the reply ready to send, without technical commentary.
3. Use `send_guest_message_preview` with either `thread_id` or `booking_id`, never both. If no conversation exists but a booking is known, use `booking_id`; Nowistay can prepare the appropriate conversation through its existing flow.
4. Show the recipient in conversational terms and the exact message.
5. If the user asked only for a draft, stop before the preview or after staging as appropriate. If the user explicitly asked to send, continue through platform confirmation with `send_guest_message_confirm` and only the approval token.

Do not recommend switching to personal email or phone merely because no conversation was found. First use the booking-based Nowistay send flow when available.

Never copy sensitive or guest-specific message content into a welcome guide, property knowledge base, mission, or booking note unless the user explicitly requests that exact transfer and the content is appropriate for the destination.
