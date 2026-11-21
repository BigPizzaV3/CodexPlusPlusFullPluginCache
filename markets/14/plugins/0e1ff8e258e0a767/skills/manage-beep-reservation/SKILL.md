---
name: manage-beep-reservation
description: Show, check, cancel or extend the user's BEEP.rent reservations through their linked BEEP.rent account.
---

Use these tools when the user asks about a car rental they booked with BEEP.rent.

1. `list_my_reservations` lists the reservations of the linked account. If the account is not linked yet,
   ChatGPT asks the user to sign in to BEEP.rent; after that, call the tool again.
2. `get_reservation_status` tells whether a reservation is confirmed, awaits the user or awaits the rental company.
3. To cancel, call `cancel_reservation` with the reservation number first: it returns the refund the user would
   get. Show the refund and the fact that cancelling cannot be undone, ask for an explicit yes, and only then call
   it again with `confirm=true` and the `confirmation_token`.
4. To extend a rental in progress, call `quote_extension` with the reservation number and the new return time and
   present the new price. `request_extension` first previews the request; call it again with `confirm=true` and
   the `confirmation_token` only after the user agrees. The rental company may still decline by e-mail.
5. Never promise a refund, a price or a confirmation that a tool did not return.
