---
name: search-yacht-charters
description: Find and compare yacht and boat charter offers on Boatscribe for a destination and dates. Use when the user wants to charter, rent or book a sailing yacht, catamaran, motor yacht or gulet.
---

# Search yacht charters with Boatscribe

Use the `search_yachts` tool of the Boatscribe MCP server to find charter offers.

## Before searching

- Ask for what the search needs and the user has not said: where (a country, region, city
  or marina) and when (a start date, a week, or a month). Do not guess dates.
- Pass the place as the user names it. Boatscribe decides which place a name means.
- Pass the user's language as `locale` (`en`, `ru` or `de`; `en` for any other).
- Map what the user asks for onto the filters: boat type, number of people (berths),
  cabins, toilets, length, year built, price, equipment, crewed or bareboat, a skipper.
  Leave out filters the user did not ask for.

## After searching

- The offers are shown as Boatscribe cards. Reply with a short summary, not a list that
  repeats the cards.
- If the place name fits several places, the cards let the user choose. Ask which one
  they mean; do not pick one yourself.
- The dates the user asked for are the ones searched. When the result has `canWidenDates`
  (an exact week with fewer than five offers), ask whether to also look one or two weeks
  before and after, and search again with `weeksAround` only after the user agrees. For a
  month search, suggest another month or a looser filter instead.
- Prices are in EUR for the whole boat and the whole stay.
- Offers come only from the tool. Do not invent yachts, prices or availability.
- Booking happens on boatscribe.com through each offer's link. Do not take payment
  details or personal data in the conversation.
