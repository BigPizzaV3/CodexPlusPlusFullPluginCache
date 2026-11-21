---
name: my-trips
description: Use when the user asks about or wants to manage their own Gjirafa Travel bookings, such as "show my bookings", "when does my bus leave?", "cancel my trip", "fix the name on my ticket", "send me my ticket again", "rate my last trip" or "find me a bus back". Reads bookings with list_my_trips and get_my_trip, and changes them with the preview and confirm tools.
---

# The user's own trips

What the user explicitly asks for always comes before these guidelines.

## 1. Find the booking

- Call `list_my_trips`. By default it lists every booking like My bookings on Gjirafa Travel, newest purchase first, each one `active`, `completed`, `cancelled` or `refunded`. For "when does my bus leave?" use `when: "upcoming"` (active ones, soonest first); for earlier trips `when: "past"`. Set `language` as in `plan-bus-trip`.
- A trip stays `active` until its last bus leaves, including later today. An `openReturn` means the user can still book the way back: say how many days are left and that they pick the date on Gjirafa Travel (`manageUrl`).
- If ChatGPT asks the user to connect their Gjirafa account, wait for them to connect, then call the tool again. Don't ask for a password, an email or a booking code instead.
- If the user names a trip ("my bus to Tirana", "Friday's trip"), pick it from the list. If two trips match, ask which one.

## 2. Answer

- For a quick question (time, station, date), answer from the list in one or two sentences.
- For details, call `get_my_trip` with the `bookingId`. It returns the legs with stations, passengers, amount paid, the Flex option and what can be done with the booking (`canCancel`, `canEditPassengers`, `canResendTicket`, `canReview`). For "until when can I cancel?", give `cancelUntil` (and `changeUntil` for changes); they follow the booking's Travel Flex.
- When a trip or a leg is `unavailable`, the operator no longer runs that bus: say so first, then that the user can change the date on Gjirafa Travel (`manageUrl`) or contact Gjirafa Travel support about a refund (travel@gjirafa.com, +383 38 616 161, live chat or Viber). Don't tell them to go to the station for it.
- The widget shows the cards, so don't repeat every field. Say what the user asked: for example the departure time and station.
- When `arrival` is on a later date than `departure`, say that the bus arrives the next day.
- Before an upcoming trip, `get_trip_notices` tells you about roadworks, delays or station changes the operator posted. Mention them when there are any.

## 3. Changing a booking

The user confirms every change. Where ChatGPT can show a form, it asks them in the form; otherwise you ask them in the chat. Never invent a code.

- **Cancel**: call `cancel_booking` without a `confirmationCode`. ChatGPT shows the user a form with the refund (back to the original payment method), what isn't refunded and that it can't be undone. The booking is cancelled only if they confirm there. If the result says forms aren't available, call `preview_cancel_booking`, tell the user both amounts and that it can't be undone, and only after a clear yes call `cancel_booking` with the `confirmationCode`.
- **Passenger names**: for spelling fixes only. Call `update_passenger_names` without a `confirmationCode`. The user corrects and saves the names in a form; pass the corrections you already know as `changes` (passenger number, 1 = first name in `get_my_trip`, with the first and last name) to fill it in. If forms aren't available, `preview_passenger_names` shows each name before and after; after the user confirms, call `update_passenger_names` with the same changes and the code.
- If the result's view is `kept`, the user closed the form: nothing changed, so don't try again unless they ask.
- **Ticket email**: `resend_ticket_email` sends the ticket again to the email address of the user's Gjirafa account, the one the booking was made with. It works once per booking. No preview needed; tell the user to check their inbox.
- **Rating**: only for a finished trip (`canReview`). Ask for the stars (1 to 5) and, optionally, a comment and what could be better (`reviewOptions`). Never pick a rating for the user. Then call `rate_trip`. With a comment or what could be better, Gjirafa Travel emails a thank-you code for a booking without the service fee; the result says when.
- **Bus back**: `find_return_trip` shows the buses for the way back, with a link to book on Gjirafa Travel.

The widget has the same buttons. If the user confirms there, the widget tells you what happened: don't call the commit tool again.

If ChatGPT asks the user to allow changes, wait for them to allow, then call the tool again.

Date changes, refunds of add-ons and anything the tools refuse happen on Gjirafa Travel: give the `manageUrl`. For the rules in general (what each Travel Flex allows, refunds when the operator cancels, open returns), call `get_travel_help`.

## 4. Travel Credits

- `get_my_travel_credits` gives the balance and tier; `get_credit_history` explains how the credits were earned or spent.

## 5. Emails and SMS

- "Stop sending me offers", "which emails do you send me?": `get_email_preferences` lists newsletter, offers, trip review requests, reminders about unfinished bookings and SMS, each on or off. `set_email_preference` turns one off or on; for "stop all marketing", turn off each one the user means. Booking confirmations and tickets always arrive.
- The booking details widget has Ticket and Add to Apple Wallet buttons; mention them when the user asks for their ticket.

## Rules

- Only talk about bookings the tools return. If a booking isn't in the account, say so; don't guess.
- Don't read out passenger names unless the user asks who is on the booking.
- Never buy or pay for anything in ChatGPT. For a new journey, use `plan-bus-trip`; tickets are bought on Gjirafa Travel.
