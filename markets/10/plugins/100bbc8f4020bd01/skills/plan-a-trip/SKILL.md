---
name: plan-a-trip
description: "Turn someone's plans for a trip, wedding weekend, busy week or event (a pasted itinerary, an email, or a description) into a Be Well Packed Plan of the moments they need outfits for."
---

The job: take what's ahead and turn it into the handful of moments that need an outfit, so the person can dress each one from their own clothes in Be Well Packed. You start the Plan here; they finish it in the app.

1. Read what they shared. A pasted itinerary is enough. Ask one short question only if the dates or the place are missing and you can't work them out. Don't ask for clothes or photos first.
2. Pick the moments. About one or two a day, never more than three. Merge anything that shares an outfit: a flight and an afternoon in town, or a pool day and a quiet evening at the hotel. Travel days count: the outfit they arrive and leave in is a moment, and the trip home can rewear the trip there. Name each moment the way they'd say it ("Dinner at Il Gatto Nero", "Train to Como"), and give each a note of a few words on what to wear ("Dressy: heels and a light layer"). A lazy day at home base can go without a moment.
3. If you know the destination and dates, call get_trip_weather first and let it shape the notes.
4. Call plan_trip_outfits with the trip and its moments. Leave pieces empty unless they've shown or described clothes they own. Never invent pieces. If something is worth buying, add up to three gaps.
5. The trip appears above your reply. Answer in one or two sentences, for example: "Here's your week: 9 moments to dress for, and Thursday's dinner is the dressiest." Don't list the days again. Offer to save it.
6. When they ask to save, or press the button, call save_trip_to_well_packed. Tell them to open the link and sign in to keep it. Don't say it's in their account until they've done that.

To change the trip, call plan_trip_outfits again with the same draftId and the whole revised trip.

If they've connected their Be Well Packed account and want outfits picked from their saved Closet, use style-my-closet once the trip is saved.

These tools don't book travel, buy clothes, or edit a Plan already saved in the app.
