---
name: choose-esim-plan
description: Use when the user wants mobile data, an eSIM or an alternative to roaming for a trip. Finds plans with search_esim_packages and helps the user pick one that fits the trip's length and their data use.
---

# Choose an eSIM plan

What the user explicitly asks for always comes before these guidelines.

## 1. Get the destination

- Resolve a city to its country before searching (Tirana → Albania, Munich → Germany).
- For a trip through several countries in one region, search the region (Europe, Balkans). For several continents, search "Global".
- If the trip length isn't known, ask once, together with how they use their phone (maps and messages, or also video and calls). Don't ask more than that; if the user doesn't say, search anyway.

## 2. Search

Call `search_esim_packages` with `location` (the country or region in English) and `language` (the user's language as a 2-letter code).

## 3. Answer

The widget already shows the plans, so don't repeat them as a list. In two to four sentences:

- Suggest the plan that fits: its validity should cover the whole trip, and its data should fit their use. As a rough guide, maps, messages and browsing use about 0.5 GB a day, and video or video calls 1 to 2 GB a day or more. Say that this is an estimate.
- Mention the plan marked recommended (`isRecommended`) when it fits.
- Mention an unlimited plan when the user expects heavy use.
- End with the `detailsUrl` link: all plans for the destination are there, and the eSIM is bought there.

## 4. When nothing is found

- `LOCATION_NOT_FOUND`: ask for the country, or offer the region ("Europe", "Balkans") or "Global".
- `NO_PACKAGES`: offer the region or "Global", and give the `detailsUrl` link.
- `API_ERROR` or `NOT_FOUND`: say the search isn't available right now and give the result's `detailsUrl` (the eSIM page on travel.gjirafa.com in the user's language).

## Rules

- Never say that a plan is bought, reserved or activated. Purchase happens only on travel.gjirafa.com.
- If the user asks whether their phone supports eSIM, call `check_esim_compatibility` with the brand and model. When it says `not_listed`, say the model isn't on Gjirafa's list and how to check on the phone; don't claim it works. If several models match, ask for the exact one.
- For general questions about a destination's eSIM (coverage, how it works there) or what travellers say, call `get_esim_destination_info`.
- For how eSIMs work, installing one, or an eSIM that doesn't connect, call `get_esim_help` (topics `install`, `troubleshoot`, `usage`) and pass on its steps in order. Never ask the user for an ICCID, a QR code or an activation code.
- Quote prices as the results give them. Don't promise discounts or that prices won't change.
- Don't invent plans that aren't in the results.
