---
name: check-a-hotel
description: Check one named hotel or resort - a fact (reef from the beach, transfer, children, meals, villa), its prices (sellers, months, nights, how they moved), what guests wrote about it, or its photos and video scenes - from sourced, dated records. Not for booking.
---

# Check a hotel with Lumina

The traveller's explicit instructions in the conversation take priority over this skill. When the traveller is
choosing between hotels, or asks whether one is right for their trip, use `lumina:choose-a-hotel` instead.

A hotel's name works as its id in every Lumina tool.

- **A fact** ("can you swim to the reef from the beach?", "is there a kids' club?", "how long is the transfer?"): call
  `check_hotel_fact` with the hotel and the question. Quote the source sentence and the date it was read. If Lumina says
  the answer is not established, say so; anything you add from a web search is labelled as the web's.
- **A price** for given dates and party: call `get_stay_price_references`. These are rates collected on the date shown,
  never live availability; confirm and book on the hotel's site or with a travel agent.
- **Its prices** ("is February expensive there?", "who sells it cheapest?", "has it gone up?"): call `show_prices`. Lumina
  holds dated observations by month, by night and by seller; the view lays them out and returns a brief to answer from.
- **What guests say** ("all the reviews", "the bad ones about the food", "what do honeymooners think?"): call
  `show_reviews` with the topic, sentiment, party, dates or language asked. Quote a guest only from a review Lumina
  returned, with its date.
- **Its photos** ("show me all the photos", "the bathrooms", "a video of the jetty"): call `show_photos`, with the kind of
  place when one is asked. For one specific thing to prove ("show me the reef from the beach"), call `show_hotel_proof`,
  then describe what each photo or video scene shows and credit it.
- **One part of it** (its villas, the arrival, the sea and reef, the food, children, a day there), or that part of two or
  three hotels side by side: call `show_hotel` with the `topic` (`villa`, `arrival`, `sea`, `food`, `family`, `days`). The
  view shows the saved facts with their source and date, that part's photos, and what is not established; for one of
  those gaps, `check_hotel_fact` reads the resort's own site now.
- **Everything about it** before deciding: call `get_hotel_dossier`.
- **The destination itself** (when to go, the wet months, the sea and marine life by season, entry, taxes, flights): call
  `show_destination`, with the month when the traveller has one.
- **Something Lumina does not hold** (flights, a booking, an Instagram profile, a recipe): answer as you normally would,
  with no Lumina view.

One Lumina view per reply: if the question needs another, the traveller opens it from the view or asks next.

Answer in a few sentences. Never infer a value Lumina did not return: when a tool says it is unknown or unconfirmed,
keep it that way.
