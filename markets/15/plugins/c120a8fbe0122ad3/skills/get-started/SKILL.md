---
name: get-started
description: Help someone make their first Mapsemble map for their website, from what the map is for and where its places come from to how it looks and how to put it on their site.
---

# Get started with Mapsemble

Mapsemble builds interactive maps that people put on their websites: a map of shops, holiday homes, cafés, hiking routes or anything else with a place. Use this when someone has just connected Mapsemble or asks how to begin.

1. Ask what the map is for and what kind of places it shows, unless they have said so already.
2. Ask where the places come from: a list they paste, addresses, a public Google Sheet, a data file on the web (GeoJSON or CSV), or places they would like suggested.
3. Make the map with `create_map`, then add the places:
   - a list or addresses: `add_locations`
   - CSV text: `import_csv`
   - a Google Sheet shared with "Anyone with the link": `preview_google_sheet`, then `connect_google_sheet`
   - a data file on the web: `preview_data_url`, then `import_data_url`
4. Show the result with `show_map`, then offer the next steps: colors or icons for the pins (`set_feature_style`), filters for visitors (`update_filters`), another look (`update_map_design`), or the code to put the map on their website (`get_embed_code`).

Make only the changes they ask for: no filters, colors or styles they did not ask for. Every change is also in the Mapsemble builder at https://app.mapsemble.com, where they can carry on.
