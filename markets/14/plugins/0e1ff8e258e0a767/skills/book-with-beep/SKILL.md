---
name: book-with-beep
description: Find, compare and prepare a car rental in Poland with BEEP.rent, then hand the user the link that completes the booking on beep.rent.
---

Use the BEEP.rent tools when the user wants to rent a car in Poland.

1. Ask only for what is missing: the pickup place (a city, an airport, a station or an address), the pickup and
   return date and time, and anything that changes the price (an automatic gearbox, a car type, insurance, an
   additional driver, a child seat, driving abroad). Without driver details, the tools assume a driver aged 31
   or older with a licence held for at least five years.
2. Call `search_offers`. Compare offers by their full price, which already includes the options the user picked,
   and by the deposit, the mileage limit and the cancellation rule. Quote prices only from tool results.
3. Call `get_offer` for the offer the user likes and present its price, deposit and policies before any booking step.
4. When the user wants to book, call `create_checkout` and give the user its `continue_url`. The booking is
   completed on beep.rent: the user enters their details, accepts the terms and confirms by paying or with a code
   sent to them there.
5. Never ask for, accept or repeat card details or confirmation codes. If the user pastes one, tell them to enter
   it on beep.rent instead.
6. A booking is confirmed only when `get_reservation_status` says so.
