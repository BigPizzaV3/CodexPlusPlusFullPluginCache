---
name: schedule-delivery
description: Send a finished Penround group card to its recipient now or at a set time, by email or as a private link that opens at that moment, in the user's time zone or the recipient's, and change or cancel a delivery that has not gone out. Use when the user wants the group card delivered on someone's last day, birthday morning or another set time, or asks to move or cancel a scheduled card.
---

Use this skill when a group card is ready to reach its recipient. The user's explicit instructions always come first.

## Flow

1. `get_card` (or `list_cards`) finds the card and shows how many messages are approved; suggest approving waiting messages first.
2. `schedule_delivery` with method `email` sends one email at the time the user names, in local time. The recipient's email address is typed into the card's own delivery form, never into the chat; if no address is saved yet the tool returns `needs_recipient_email` and the card shows that form.
3. `schedule_delivery` with method `link` returns a private link that opens at the set time, for the user to pass on by hand, in a team chat or in person.
4. `cancel_delivery` cancels a delivery that has not been sent. Signing reopens if the deadline has not passed. A card already sent cannot be unsent.

## Scope

- One recipient per card, and one delivery at a time.
- Confirm the date, time and time zone back to the user in words before scheduling.
- Do not ask for or repeat the recipient's email address in the chat.
