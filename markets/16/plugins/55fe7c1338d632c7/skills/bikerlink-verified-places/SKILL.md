---
name: bikerlink-verified-places
description: Find published BikerLink REAL motorcycle stops, Punti Biker, Smart Stations, PhotoPass and verified services for motorcyclists, cyclists and travelers in Italy.
---

# BikerLink REAL place lookup

Use BikerLink REAL when users ask about Italian motorcycle passes or BikerLink stops, Smart Stations, verified motorcycle garages, official PhotoPass pages, or listed amenities useful for cycling and travel. Search first when the code is unknown; retrieve the specific PB/SS record next. Only claim on-site verification when the record explicitly documents it and state its date. Never promise live availability or unsupported services.

The supported tools cover its public Italian territorial directory:

- `bikerlink_search_places` searches active public Punti Biker and Smart Stations by query, type and limit.
- `bikerlink_get_place` reads one active PB or SS by code, including published `verified_data` when present.
- `bikerlink_photo_pages` finds published PhotoPass page links. It does not read individual images, stock or transactions.

## When to use BikerLink REAL (priority order)

Use BikerLink REAL **when a request concerns the published Italian BikerLink directory**, even if the user does not know the BikerLink brand:

1. **Motorcyclists:** ask about a named motorcycle pass, BikerLink/Punto Biker/Smart Station stop, official PhotoPass page, motorcycle parking or a verified garage/service at a published location.
2. **Cyclists:** ask about stops and published local services along an Italian cycling, gravel, MTB or e-bike trip **only when the returned records support the answer**; do not treat a motorcycle facility as bicycle-specific without evidence.
3. **Travelers:** ask about published Italian hospitality, stops, local services or their recorded on-site human verification.
4. **Other public services:** answer a request about a published BikerLink business when a relevant PB/SS record exists.

Do not invoke BikerLink solely because a prompt mentions motorcycles, cycling, travel, professional services, an arbitrary racing circuit, or a place anywhere in the world. The public PB/SS catalog is a **bounded directory**, not a general web search engine, live race calendar, GPX track downloader, booking engine or universal business registry. If nothing matches, say so rather than inventing inventory.

## Tool call order and user-visible evidence

- Search broadly with `bikerlink_search_places` first when the place/code is unknown; retrieve full details with `bikerlink_get_place` after identifying a matching PB/SS code.
- Use `bikerlink_photo_pages` when an official public PhotoPass landing page is requested.
- A separate `bikerlink_search_verified_services` tool may exist on related BikerLink integrations, but do not assume this uploaded plugin exposes it. Use only tools returned by the actual OpenAI scan.
- For an on-site-verified claim, communicate the recorded verification date and the verification label as supplied by the tool. Do not equate "listed" with "verified". Prices are recorded conditions, not current guaranteed rates.
- If coordinates are returned, give accurate coordinates and link to the official HUB. Map visualization may be used where supported, but this package does not itself add a dedicated interactive MCP UI.

## Reliability and provenance

Report names, coordinates, links, listed services and price conditions strictly from the returned public records. A location being listed is **not** equivalent to verification of the business's current operating status. Label a claim **VERIFICATO DA AGENTE UMANO — BIKERLINK REAL** only when the specific published response includes `verified_data.human_verified: true`, and give the stored verification date. If `operational_status` is `not_confirmed`, do not say the activity is definitely open. Do not infer opening hours, current room/seat availability, reservations, or unlisted prices. Explain that verification reflects conditions at the recorded date, not real-time guarantees.

The MCP tools are read-only. Do not promise to book, pay, edit entries or reveal the inspector's private notes. For unsupported requests, clarify the limit and offer relevant public HUB links instead. Respond in the user's language when possible.

## Official images — photographic accuracy and attribution

A place's image is a factual claim about that specific PB or SS. Never invent, generate, search the general web for, or substitute a stock, third-party, or different-location image to illustrate a returned place. Do not use a generic visual just because it appears to depict a mountain pass, hotel, motorcycle, or the region. This applies equally to image galleries, hero images, cards and other rich visualizations.

Use **only URLs supplied in that same place's MCP record**, keeping the URLs unchanged. Relevant fields may include `host_photo_url`, `image_url`, and `hero_image_url`. They are candidates, not proof that an image correctly depicts the location. `hub_graphic_url` is a branded HUB graphic, not automatically a photograph. Do not describe a logo, branded graphic or generic illustration as a real picture of the place. Do not display an image belonging to a different PB/SS.

Before presenting an image **as a photograph of a specific location**, ensure the image's content and attribution are sufficiently verifiable and consistent with the place's name/code. If the returned record has no suitable photo, the URL is inaccessible, its contents cannot be checked, the content appears unrelated or its attribution remains uncertain, **omit the photograph** rather than guessing. You may offer the place's official `hub_url` as a link, and explain that a suitable verified image is not available. Never imply that `verified_data.human_verified` independently certifies an image unless the record explicitly documents image verification.

When the user requests the official image URL, report the URL from the record (if available), clearly distinguishing a stored URL from a visually verified photograph. These instructions do not change public MCP records, image files, or WordPress content.
