---
name: byway-travel
description: Plan European train trips with the Byway connector - city breaks, multi-city trips and trips to fixed-date events. Creates fully priced, fully bookable trips.
---

# Planning trips with Byway

Byway builds complete overland trips across Europe: the trains between places, a hotel at each stay, and a total price, saved as a trip the traveller can open, adjust and book. The Byway connector (the MCP server) does the planning, so a trip from it is real, current and bookable, whereas trips built purely from search are often guesses.

The connector has two tools:

- **buildTrip** builds and saves a trip and returns a link plus a summary of what was built.
- **listPlaces** looks up the place names Byway knows. You rarely need it.

If neither tool is available, the Byway connector isn't connected in this chat. Say so, and suggest the user turns it on.

## Building a trip

Call buildTrip straight away with what the user has told you. Plain city names work (case and accents don't matter), so don't call listPlaces first.

- **origin** is where the trip starts, usually a UK city such as London. If Byway rejects it as an origin, call listPlaces with `originsOnly=true` to see the choices.
- **stayPlaces** are the places to stay, up to 9. Byway chooses the order from its routing, so it may not keep the order the user gave, and it may add an overnight stop on a long journey.
- **finalDestination** makes the trip one-way. Leave it out for a trip that returns to the origin.
- **Dates** are YYYYMMDD. With no dates, Byway starts the trip about three months ahead and gives each stay 3 nights. If the user gives a length ("a week in Italy"), pass a start and end date.
- **tripTitle** is optional. A short title that fits the request ("Rome and Florence in spring") reads better than the default, which is the stay names.

A build takes up to a minute, so tell the user it's being planned rather than going quiet.

### Trips around an event

When the user has something fixed to get to, give all four event fields:

- **eventPlace**: the city the event is in.
- **eventStartDate**: the first night they stay there.
- **eventEndDate**: the day they check out, which is the morning after the last night. An event running 1 to 3 November with nights on the 1st, 2nd and 3rd gives `eventEndDate` 4 November.
- **eventNeedsAccommodation**: `false` if their hotel is already arranged (for example, the organiser provides it), otherwise `true`.

Other stays are fitted around the event. If one can't fit, Byway drops it and says so in the warnings.

## Telling the user about their trip

On success, the result's `summary` describes what was actually built. Use it rather than restating the request:

- `stays` lists each stay in order with its nights and dates. `chosen: false` marks an overnight stop Byway added on a long journey, which is worth pointing out.
- `items` lists every train (operator, stations, departure and arrival times) and stay in order.
- `totalPrice` with `currencyId` is the price of the whole trip. Individual items have no prices, so don't invent any.

Always mention anything in `warnings`, such as a stay dropped or moved to fit an event: the user needs to know their plan changed. Then give them the link (`url`) to see the full trip.

The trip is saved, not booked. Nothing has been paid for and no seats or rooms are held, so don't say it's booked.

Every trip is planned for two adults sharing one room, and the total price is for them. Before booking, the user can change the trip on the linked page: the number of nights, the travellers, the hotels, the rooms and the class of travel, and the price updates to match. So if they ask for something buildTrip can't set, like a trip for four or first class, build it anyway, then say what it was planned with and that they can change it on the trip page. The one thing neither buildTrip nor the trip page can change is the order of the stays, which Byway chooses, so don't promise a particular order. The user books from the link if they want it.

## When the build fails

`errors` says why. An unknown or ambiguous place says so: use listPlaces to find the right name, or ask the user which one they meant, then call buildTrip again. For anything else, explain the error in plain words and offer to try different places or dates.
