---
name: choose-a-hotel
description: Choose where to stay - the luxury hotel or resort that fits a trip (honeymoon, family, friends, divers, a budget), the better of named hotels, or whether one is worth it for these travellers. Not for flights or bookings.
---

# Choose a hotel with Lumina

The traveller's explicit instructions in the conversation take priority over this skill. For one question about one
named hotel, with no choice to make (a fact, a price for dates, a photo), use `lumina:check-a-hotel` instead.

## The trip

1. Collect what the traveller has already said: destination, month or dates, nights, who travels (adults, children's
   ages), budget per night, how they want to arrive, what each person wants and what each person worries about, hotels
   they named, hotels they ruled out, diet. Do not ask for anything the tools can work without; if the destination is unknown, help interpret what attracts them first. A photo is a starting point: distinguish visible features from inferred wishes, and ask only a question that materially changes the search. Do not identify an unknown place or infer privacy from a photograph.
2. Call `plan_destination_stay` with all of it. Write each wish or worry as a need, one person at a time (someone who
   gets bored needs things to do; someone afraid of water needs a calm lagoon). The tool accepts a nightly budget in USD. For another currency, use a current sourced exchange rate and state the approximation; if none is available, omit the numeric budget and compare documented prices in their own currencies. Never silently treat EUR, CHF or GBP as USD. Named hotels go in `named_hotels`, so they are judged against each
   other and against every other hotel there for the same trip.
3. `plan_destination_stay` already shows its shortlist in the chat (the hotels the traveller named first, then the best four), on a map by default. Pass `layout` from what the traveller asked: `map` when they want to see where the hotels are, the islands, distances or transfers; `table` when they ask to compare side by side; `cards` for a quick look at photos. Call `show_comparison` only to show other hotels or another layout. Prices, reviews and photos of one hotel, or of two to four side by side, open with `show_prices`, `show_reviews` and `show_photos`; one part of one to three hotels (villas, arrival, sea, food, children, days) with `show_hotel`; when to go with `show_destination`. One view per reply.
4. After the view opens, answer in a few sentences in the traveller's language: your pick and why, its cost with the condition that decides it (a transfer free only with a meal plan, a fare whose direction is not stated), the trade-off, what is not established, and a supported alternative they did not name. The view carries the rest; do not redraw it as a table. Never present one end of a cost range as the price.

If Lumina says it does not cover the destination, say so and answer as you normally would.

## Never infer

Room and villa names and numbers, prices, distances, transfer times, age limits and meal-plan inclusions come only
from what a Lumina tool returned in this conversation. Lumina's plan already carries the room quotes collected for the
traveller's dates, the transfer fares and their conditions, the meal plans and the guest evidence it holds: read them there
before reaching for anything else, and say the date each price was collected. When a tool says a value is unknown or unconfirmed, keep it
that way. Prices are collected references, not live availability; booking is on the hotel's site or with a travel
agent. Say "Lumina" only about what Lumina returned; anything from a web search is the web's.

## Changes to the trip

When the traveller changes dates, party, budget or priorities, run the plan again with the updated complete trip and refresh `show_comparison`. Preserve explicit exclusions. A cheaper hotel that meets the requirements is worth showing; do not spend the whole budget by default. Keep the exact room, quoted dates, guest party and tax coverage attached to every price. Never present a rate for other dates as the price of this trip.

## Conversation and saved journeys

The scene is a visual companion to the conversation. Use the explicit hotel, villa, scene and revision in model context when resolving “this”. If absent or ambiguous, ask briefly; never assume a favorite is the currently viewed villa. A map movement or favorite does not require another recommendation. Answer a new question with the relevant fact/proof tool; replan only when the trip changes. When the traveller wants to look deeper at one hotel, `show_prices`, `show_reviews` and `show_photos` open what Lumina holds on it in the view: prices by month, night and seller; the guests' words by topic and party; every photo by space and video scenes at their second.

Give a recommendation and comparison from the first useful result. Assess named hotels and explain the least-cost documented option meeting the requirements, plus what an upgrade buys. Missing prices are not evidence of value. Write in full, human sentences, tied to sourced scenes; never invent sensory details.

Favorites, a saved journey and a booking are separate states. Lumina saves a journey only where its trip tools (`get_trip_capabilities`, `save_trip`) are listed in this conversation: if they are not, say that this connection cannot save a trip and that the comparison's «Keep link» reopens the same selection. Where they are listed, use `save_trip` only for explicit save or update intent and report success only from a confirmed result. Never interpret a heart as permission to share or contact someone. On a date change, preserve favorites and the previous variant; the UI updates without rewriting prior chat messages.
