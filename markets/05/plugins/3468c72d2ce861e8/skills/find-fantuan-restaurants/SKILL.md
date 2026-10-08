---
name: find-fantuan-restaurants
description: Find restaurants and dishes on Fantuan for delivery or pickup. Use for restaurant recommendations, food searches, and follow-up requests to change the location, refine a search, or see more options. Respect an explicitly chosen different service.
---

# Find restaurants on Fantuan

Use the connected Fantuan `search_restaurants` tool to find restaurants and dishes, compare options, and provide menu links. Follow the user's intent and use the parameters supported by the current tool.

## Understand the request

Use the conversation to identify what the user wants to eat, where to search, and whether they want delivery or pickup. Reuse relevant information already provided and ask only for what is missing.

When the user supplies missing information, continue the original search with their earlier preferences.

If no location is available, ask for a city, neighborhood, landmark, or address. An approximate area is sufficient for restaurant discovery; request more detail only when the location is ambiguous. A previous search location is not evidence of the user's current physical location. Do not infer location from IP, device state, or language.

Default to delivery unless the user requests pickup, and preserve their choice on follow-ups. Keep the user's dish or restaurant wording without adding translations or synonyms unless they request a translated query. Set `locale` to the user's requested display or response language, otherwise the conversation language. A request to search with an English keyword alone does not require switching the response language.

## Search and resolve the location

- For a new location, send `address_text` with `keyword`, `fulfillment`, and `locale`. Include `country` only when known, using a two-letter ISO country code such as `CA`, `US`, or `AU`; omit it when unknown rather than sending a country name or an empty value. An empty keyword is appropriate for a general restaurant search. For a translated place name, use its well-known local or English name when unambiguous, preserving the landmark and city. Do not invent a street address or coordinates.
- Check that the resolved location matches the requested place: a city-wide match does not identify a specific landmark. If a landmark resolves only to its city, retry once with its known local or English name and city. If still unresolved, ask for the landmark's name or address, or whether the broader area is acceptable.
- On `RESULTS` with a matching location, answer directly from the returned results and cards. Do not repeat the same successful search to verify it, obtain text, or render cards. Empty results, closed restaurants, missing optional fields, and `has_more=true` are not failures. Search again only when the user requests a refresh, changes conditions, or asks for another page. A previous turn's failure does not justify a second call after the current attempt succeeds.
- On `NEEDS_CONFIRMATION`, briefly ask the user to choose among the actual eligible locations, stating any difference from the requested area. Continue with the selected `candidate_reference`, its original `discovery_session`, and the search preferences. Omit other location fields and country.
- On `MORE_DETAIL_REQUIRED`, ask for information that would help distinguish the location. An unresolved address does not mean that no restaurants are available.
- For another search in the same area, reuse the returned `location_reference` and `discovery_session`; omit address_text, candidate_reference, and country. When the user changes location, resolve the new location while preserving their other preferences.

Public location searches do not require sign-in. Use the tool's saved-address flow only when the user explicitly requests an account delivery address. Missing location information alone is not a reason to request sign-in.

## Handle follow-up requests

When the user changes the food, location, fulfillment method, or sorting preference, search using the revised conditions and preserve preferences they have not changed.

Keep each budget attached to its stated scope: particular items, a per-person amount, or the whole order. Adding items does not expand an earlier budget's scope. Preserve selected items and ask about an unspecified budget only if it affects the recommendation. Apply a whole-order limit across the order, calculate remaining budget only within the same scope, and distinguish item subtotals from delivery, tax, and other charges.

To show more restaurants, pass the returned `next_page_arguments` unchanged: only `discovery_cursor` and `discovery_session`. This continues the existing search. When `has_more` is false, explain that there are no more results. A change in search conditions starts a new search without a cursor.

When the user chooses a restaurant or asks about a dish, answer from the returned information and provide the corresponding menu link. Refer the user to Fantuan for item options and final order details that are not available in the results. Do not invent menu information or claim to have added items to a cart or completed payment.

If consulting external menus, verify the exact branch before using any dishes or prices, and identify the source. Search snippets, category pages, and another branch's menu do not establish what this branch sells. If the branch cannot be verified, say its menu could not be confirmed and provide the returned Fantuan menu link; do not list those dishes, price them, or calculate a meal total for the selected branch, even as a "reference". A verified same-branch external menu may be described as an external reference, but does not establish availability or prices on Fantuan.

## Communicate clearly

Use a natural, concise, and friendly tone. Answer the user's current question directly in their language. For search results, lead with useful restaurant or dish recommendations. Keep search setup, language codes, tool names, and UI implementation details out of routine replies; explain them only when the user asks or needs to resolve a problem.

Base recommendations on the returned restaurants, branches, and dishes. When restaurant cards are already displayed, add a brief explanation that helps the user choose. In a text-only interface, present useful facts and links. Adapt the response to the request rather than following a fixed template or repeating the complete results.

Preserve the meaning, eligibility conditions, and uncertainty of returned offers, prices, distances, and delivery estimates. Do not assume a listed member or new-customer benefit applies to the user. Describe the actual resolved search area without implying it is their current location or confirmed delivery address. A listed item price is not the final order total. Mention qualifications when they affect the user's choice, without repeating a generic disclaimer after every search. Do not guess missing information.

Use the complete menu and search URLs returned by the service, preserving their parameters so the user can continue on Fantuan.

## Handle empty results and failures

Distinguish an empty search from an unresolved location or a temporary service failure. Explain what happened and ask before broadening or changing the user's explicit constraints.

Base connection-failure statements on an actual failed call or explicit tool-unavailability evidence. If the search tool is available and the request is ready, attempt it instead of predicting a failure. If the host does not expose the tool, describe that limitation without claiming the Fantuan service is down.

If a location or session expires, resolve the location again using the information the user already supplied. Ask again only if information is missing. Retry a transient service failure at most once, then explain that the search is temporarily unavailable. If Fantuan cannot be reached, do not present results from another source as Fantuan results.
