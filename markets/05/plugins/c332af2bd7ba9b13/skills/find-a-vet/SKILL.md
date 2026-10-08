---
name: find-a-vet
description: Find, check and book veterinary care in the United States with PawsRx. Use when the user wants to find or choose a vet, animal hospital, emergency or urgent-care vet, or a vet for a particular animal (including exotics such as rabbits, birds, reptiles, ferrets and guinea pigs); asks about a practice's hours, open appointment times, whether it sees their animal or takes new patients; or wants to request, check or cancel a vet appointment.
---

# Find a vet with PawsRx

PawsRx is a directory of 26,000+ US veterinary practices with the species each one treats, its hours and the prices it publishes. The veterinarians are independent practices. PawsRx is not a veterinary provider.

## If it cannot wait

If the owner says it is urgent or an emergency, tell them to go to an emergency vet now, and call `find_vets` with `q: "emergency"` and their city or ZIP to find the nearest one. Do not request an appointment or send an Ask a Vet question instead.

## Finding a vet

1. Call `find_vets` with what the user gave: `city` and `state` (a code or full name) or `zip`, and `species` if they named the animal. If they said "near me" and you know their city, use it; otherwise ask for a city or ZIP.
2. If they asked about a time ("open Saturday morning", "tonight"), pass `day` (a weekday, today, tomorrow or YYYY-MM-DD) and `period` (morning, midday, afternoon or evening).
3. Present the practices returned: name, address, phone, hours, the species it treats, and its PawsRx page link. These are matches to what was asked, not a ranking: never call one "the best".
4. If nothing matches, say so and pass on the note (it may name the nearest listed city). Never invent a practice that is not in the results.

## A practice the user picked

- Contact details or hours: `practice_details` with its `practice_id` from `find_vets`.
- "Do they see rabbits?" or "are they taking new patients?": `check_eligibility` with `practice_id` and `species`. A null answer means the practice has not published it: say it is unknown and suggest asking them. Do not turn unknown into yes or no.
- "When can they see my dog?": `check_availability`. If it returns open times, offer them. If `has_calendar` is false, there are no times to pick, and an appointment can still be requested.

## Requesting an appointment

1. Collect: the owner's name, email and a 10-digit phone number, the pet's name and species, the reason for the visit, and when they would like to come. Ask for anything missing; never make up contact details.
2. Call `request_appointment`. It returns a reference and the status "requested".
3. Tell the owner the request is in and PawsRx will email them when the practice confirms. It is not a confirmed appointment: never say it is booked or confirmed.
4. Later, `check_booking_status` with the reference gives the status; `cancel_booking` cancels it when the owner asks.

## Related

- A question for a veterinarian rather than a visit: `ask_a_vet` (see the ask-a-vet skill).
- What a visit costs: `price_lookup` (see the pet-care-costs skill).

## Always

- Leave questions about the animal itself to the veterinarian or the practice.
- Refer to "the independent veterinarians who answer on PawsRx" or "the practice", never to PawsRx as the vet.
- The directory and booking cover the United States only. Outside it, say so and do not invent practices; Ask a Vet still works in any country.
