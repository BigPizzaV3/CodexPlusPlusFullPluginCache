---
name: find-a-registry-and-choose-a-gift
description: Use when someone is a guest looking for a friend's or family member's EasyRegistry gift registry — a wedding, baby shower, birthday or fundraiser — and wants to see what is on it and what is still available. Works without signing in. Not for adding or buying gifts; purchases and contributions happen on the public registry page.
---

# Find a registry and choose a gift

Use this when the user is a guest: "find Sam and Riley's wedding registry", "what's left on Priya's baby shower list", "what can I get them". No sign-in is needed.

## Workflow

1. **Get the two things search needs.** `find_registry` requires the event date (or a close approximation) and at least three characters of the couple's or host's name, or the registry title or slug. Search matches registries within one month either side of the date and will not accept a date more than a month in the past. If the user only has the year or the season, ask for the month.
2. **Search.** Call `find_registry`. It returns up to ten matches. If there is one clear match, continue. If there are several, show title, names and event date and ask which one. If there are none, suggest checking the spelling, the date, or asking the host for the registry link (the slug at the end of the link can be used as the search text).
3. **Show the registry.** Call `view_registry` for the public details: title, event date, location, description and any message from the hosts. Respect the host's settings; if a detail is not returned, do not guess it.
4. **Browse gifts.** Call `view_gifts` and present what is available, grouped sensibly (by price range or category if obvious). Note that some items may already be partly funded or bought; only present what the tool returns as available.
5. **Help them choose.** If the user gives a budget or a preference, filter the list and recommend two or three options with prices.
6. **Hand off to buy.** Give the public registry page link so they can buy or contribute there. The app cannot purchase, reserve or contribute on their behalf.

## Boundaries

- Only use these three public tools; never attempt owner tools for a guest.
- Do not reveal or speculate about the owner's private data (contributions, contributor names, totals, bank details). These tools do not return them.
- Do not fabricate registries, gifts or prices when a search is empty.
- If the registry is password-protected or closed, say so and suggest the guest contact the host.

## Output

The matched registry (title, date, location), a short list of available gifts with prices, and the public page link for purchasing.
