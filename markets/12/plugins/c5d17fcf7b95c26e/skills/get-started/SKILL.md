---
name: get-started
description: Introduce Assetfy and run a first property check for a German address or Flurstück — parcel, buildings, planning law, Bodenrichtwert and aerial image.
---

# Get started with Assetfy

Assetfy answers questions about a single German property from official cadastral and planning data. Use it when the user names an address, a Flurstück (Gemarkung, Flur, Flurstücksnummer) or a property listing and wants to know what is on the site and what may be built there.

## First check

1. Ask for an address or a Flurstück if the user has not given one. A street address can go straight into the `address` parameter; no outside geocoding is needed.
2. Call `assetfy_get_parcel_profile` for the full picture of one parcel: size, shape, actual use, buildings, Bebauungsplan or §34/§35 BauGB, Bodenrichtwert.
3. Go deeper only where the user asks:
   - Bebauungsplan and plan documents: `assetfy_db_planning_at_point`, then `assetfy_get_plan_document`
   - Buildings, Traufhöhe and Firsthöhe: `assetfy_db_buildings`
   - Land value: `assetfy_db_land_values`
   - Aerial image: `assetfy_get_aerial_image`
   - Listings for sale: `assetfy_search_real_estates`, `assetfy_get_real_estate`
4. Give the `assetfy_url` from the result so the user can open the parcel on the Assetfy map.

## How to answer

- Answer in the user's language. Keep the German legal terms as they are: Flurstück, Gemarkung, Flur, Bebauungsplan, Bodenrichtwert, GRZ, GFZ, BGF, Traufhöhe, Firsthöhe.
- Building potential (GRZ, GFZ, BGF) is an indicative first assessment, not a legal opinion or a building permit. Say so when you report it.
- When a result reports that the data does not cover a state or a municipality, say that plainly. A missing hit is not proof that there is nothing.
- All tools are read-only. To save a place or a listing, the user opens the `assetfy_url` and saves it in the Assetfy app.

## Account

Area searches across many parcels — screening by use, size, building coverage or Bebauungsplan — are not available on every Assetfy account. When a tool reports that, tell the user and offer to answer for a specific address instead.
