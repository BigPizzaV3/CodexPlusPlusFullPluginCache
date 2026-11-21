---
name: kallax-board-games
description: Use Kallax.io to search its public board-game catalogue and public collections, and to find nearby public board-game events and communities. Use when a user asks for Kallax.io games, collections, wishlists, events, cafés, clubs, stores, groups, or local board-game activities.
---

# Kallax.io board games

Use the connected Kallax.io MCP server. All Kallax.io tools are read-only and expose only information available to visitors who are not signed in.

## Tools and behavior

- `find_games`: Find catalogue games. Optional filters are combined with AND: `title`, `players` (int), `playtime` (minutes), `designer`, `complexity` (Simple, Low, Medium, High, Extreme), and `type` (Base, Standalone, Expansion). It returns at most the 10 most popular matches. If the user needs different results, narrow the filters rather than implying pagination.
- `search_collection`: Search a public user's or public community's owned games, or wishlist when `wishlist=true`. Requires at least `username` or `community`. Supports the same filters as `find_games`. Results are ordered by title. If the user asks about “my collection” without giving a Kallax.io username, ask for their Kallax.io username. If no username/community is supplied, do not invent one.
- `find_events_nearby`: Requires latitude and longitude. Optional `radiusKm` defaults to 25 and has a maximum of 100; `type` may be Meetup, OpenPlay, Tournament, TradeShow, Convention, Virtual, or GameNight. `fromDate`/`toDate` use yyyy-MM-dd and default to today through 30 days ahead. Results are the 10 closest and are ordered by start time.
- `find_communities_nearby`: Requires latitude and longitude. Optional `radiusKm` defaults to 25 and has a maximum of 100; `type` may be Cafe, Club, Group, Community, Store, Library, Bar, or Other. Results are the 10 closest and include up to 3 upcoming events per community.

## Location

The location tools need coordinates. When the user gives a city or address, convert it to latitude/longitude using an appropriate location/geocoding capability available to the host. When the user says “near me”, use the user's available precise location if permitted; otherwise ask for a city or address. If no location is known, ask for one rather than guessing.

## Time

Kallax event timestamps are UTC. Convert `startsAt` and `endsAt` to the user's local time when presenting them. Preserve the Kallax.io event URL for each event.

## Links

Always include the Kallax.io link for every returned game, collection item, event, and community. Prefer the URL returned by the Kallax.io tool; do not invent URLs.

## Safety and scope

Do not claim access to private/signed-in information. Do not perform write actions because the available Kallax.io interface is read-only. Be explicit when a result is limited to the public Kallax.io view.
