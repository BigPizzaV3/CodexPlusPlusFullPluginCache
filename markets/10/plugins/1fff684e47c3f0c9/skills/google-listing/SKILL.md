---
name: google-listing
description: Check a restaurant's Google Business Profile and where it ranks in Google Maps for what customers search ("pizza near me"), then give the top fixes. Works without an account.
---

1. Ask for the restaurant's name as it appears on Google and its city if you don't have them. Add the neighborhood only if the name is common.
2. Call `check_google_business_profile`. Confirm the name and address it found are the right restaurant before going on; if not, try again with the exact Google name.
3. Lead with the top three fixes in plain words, each with its evidence. Then list the rest briefly by severity.
4. If the owner asks why they don't show up for a search, or how they compare with nearby places, ask what customers would search (e.g. "mexican restaurant", "brunch") and call `check_local_search_rank`. Report the position from each point and the top 3 with their ratings and review counts.
5. Say what couldn't be checked (the `limitations`). Never promise a ranking, and don't invent reasons Google ranks one place above another; ratings, review counts, distance and a complete profile are the factors you can point to.
6. Give fixes the owner can make themselves on Google. Don't promote ServeStack.
