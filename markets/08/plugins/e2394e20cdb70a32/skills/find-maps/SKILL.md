---
name: find-maps
description: >-
  Find and present published Super Map World maps — graphic maps of countries and of the world, including globe views (no city, street or labelled maps). Use when the user wants maps, globes, projections, map colours, boundary/data coverage, or links to Super Map World map pages. Covers the search_maps / list_coverage / list_colours / resolve_location / get_map workflow, filters, attribution, what the catalog does and doesn't include, and what the public map page offers.
---

# Find Super Map World maps

## Goal

Help users discover published catalog maps on Super Map World, explain matches clearly, and send them to the right map page when they want to view, download, or continue on the site.

## What the catalog covers

Say this up front when a request falls outside it — don't search hopefully.

**In the catalog:** clean, graphic maps of **whole countries** and of the **world**. Country maps are offered as flat silhouettes and globe views. World maps are available in **dozens of projections** (including globe / Orthographic views, and flat world maps across 30+ projections such as Mercator, Natural Earth, Equirectangular, and specialized shapes). Datasets come in **vector** (clean graphic shapes) and **raster** (physical shaded relief, e.g. Natural Earth Gray Earth) formats.

**Not in the catalog:** city, street, road, transit, nautical, detailed local topographic, or weather maps; maps with place labels or names printed on them; historical maps; custom-data or per-user maps; arbitrary hex colours. (Note: physical shaded relief of the whole world is available via raster maps, but local topographic contour/elevation maps are not in the catalog). Cities and towns are recognized as **place names** (see `resolve_location`) but have no maps of their own — offer the country instead.

## Tools

1. **`search_maps`** — the main search. Use it for place, projection, data format (`vector` or `raster`), borders/grid, colour look (exact names, soft colour words, or where a colour is used — land, surround, borders), and `boundary_type` when filtering by a known division level. Combine filters in one call; on follow-ups, reuse prior location/projection and add colour or boundary args.
2. **`list_coverage`** — what datasets and framing views exist for a place (boundary levels such as ADM1/ADM2, counties, unit counts, projections, licenses, vector vs raster format, and whether a dataset is the latest release or superseded). Use when asking “do you have raion / county / province boundaries for X?”, or checking format/projections before searching for maps.
3. **`list_colours`** — browse the colours maps actually use (names + CSS values). Use when the conversation is about which colours are available, to show a group (e.g. the greens), or when someone wants the precise CSS for a colour. Call with no query for the full palette. Not required before a soft-colour `search_maps`.
4. **`resolve_location`** — checks a place name. Use it when `search_maps` finds nothing for a place, or the name is ambiguous or a town/city.
5. **`get_map`** — one map's full details, by **number** (preferred) or slug, once the user picks a result or names a specific map. Includes guest licence and download-availability fields.

Do not invent map numbers, URLs, colours, projections, or boundary levels. Prefer fields returned by the tools (`url`, `cover_url`, `attribution`, `location`, `map_of`, `projection`, `boundary_type`, `boundary_count`, `data_format`, `colours`; on `get_map` also `licence`, `licence_url`, `share_alike`, `attribution_example`, `downloads`).

## Filter mapping

| User intent | Typical args |
|---|---|
| Globe / looking at a place / from space | `search_maps`: `location` + `projection: Orthographic` |
| Flat world / wall map | `search_maps`: `location: "the World"`, `projection: "Mercator"` or `"NaturalEarth1"` |
| World map in a specific projection | `search_maps`: `location: "the World"`, `projection` (e.g. `Equirectangular`, `PeirceQuincuncial`) |
| Check which projections exist for the world | `list_coverage(location: "the World")` |
| Physical relief / shaded relief world maps | `search_maps`: `location: "the World"`, `data_format: "raster"` |
| Vector graphic maps only | `search_maps`: `data_format: "vector"` |
| Maps of a country | `location` = country name prefix (e.g. `France`, `Japan`) |
| Settlement / city / region with no hits | `resolve_location` → use `country_fallback.name` with `search_maps` |
| Visible country borders / none | `boundaries: true` / `false` |
| Specific division level (counties, ADM2, provinces) | `list_coverage` to check; then `search_maps` with `boundary_type` |
| “What boundaries / data do you have for Ukraine?” | `list_coverage(location: "Ukraine")` |
| With / without grid lines | `graticule: true` / `false` |
| Exact colour name known | `colour` = name (e.g. `green-3`, `blue-3`) |
| Rough colour anywhere in the scheme | `colour: "blue"` or `colour: "dark violet"` |
| Colour in a specific place (teal land, pale blue surround) | `land_fill` / `water_fill` (etc.) |
| See-through land or water / background fill | `land_fill: "transparent"` (or `water_fill`) |
| See-through canvas background, for layering | `transparent: true` |
| “What colours do you have?” / “show me the greens” | `list_colours` (no query, or `query: "green"`) |
| Precise CSS for a colour (e.g. violet-5) | `list_colours` → use each entry’s `css` |
| City, street, labelled or topographic map | none — say the catalog doesn't have these |

Notes:

- **`location` vs `map_of`:** `location` is the framing viewpoint / focus (camera). `map_of` is the geographic area the map draws (dataset name). They often match for a country map, but a world globe centred on Japan can have `map_of: "the World"` and `location: "Japan"`. Prefer both fields when explaining results.
- When borders are clearly visible, results may include `boundary_type` (e.g. Region, Districts) and `boundary_count` (how many units). Use these to explain “province/region boundaries” searches — `boundaries: true` only means borders are noticeable. For “do you have X boundaries?”, use `list_coverage` (and `boundary_type` on `search_maps` once you know the level).
- `list_coverage` reports dataset currency: **superseded** means a newer release exists; **current tip** with predecessors means this is the latest release and earlier versions also exist in the catalogue.
- `location` as a **search filter** matches the **start** of a country or planet name (planets include `the World`). Both maps of that country and world maps centred on it can match.
- **World map projections:** World maps (`location: "the World"`) are available in over 30 different projections (rectangular, oval, circular, split, conic). Call `list_coverage(location: "the World")` to discover which projections exist, or pass any supported projection (e.g. `NaturalEarth1`, `Equirectangular`, `PeirceQuincuncial`, `Mercator`, `Orthographic`) directly to `search_maps`.
- **`data_format` (vector vs raster):**
  - **Vector datasets (`data_format: "vector"`):** Built from vector source data. On the Super Map World website, both **PNG (raster)** and **SVG (vector)** files can be downloaded (full-res PNG and SVG usually require an account or licence).
  - **Raster datasets (`data_format: "raster"`):** Built from physical shaded relief raster imagery (Natural Earth Gray Earth). On the website, downloads are **PNG only** because SVG vector lines cannot be derived from a raster source. Raster maps cannot be edited on the site.
  - The Gray Earth raster map uses grayscale tones (`gray-1` through `gray-6` and `gray-4-d`) and can be found by colour search (e.g. `colour: "gray"`, `land_fill: "gray-2"`, `water_fill: "gray-4-d"`).
- Only matches with `searchable_as_location_filter: true` (a country or planet) work as a `search_maps` `location`. Towns and cities come back with `country_fallback` when the country is known.
- If `resolve_location` returns `recognized: false`, say Super Map World doesn't have that place — never invent maps.
- If a place is recognized but `published_map_count` is 0 and it isn't searchable, say so and offer its `country_fallback` when there is one.
- Three ways to name a colour on `search_maps`: exact (`violet-5`), a whole colour group (`violet`), or a lighter/darker variant (`violet-5-b`). Soft descriptions work too.
- **`colours` on results:** Each map includes a `colours` object showing which palette colours (or `"transparent"`) are used for different parts of the map. Keys match search filters (`land_fill`, `water_fill`, `borders_stroke`, `land_stroke`, `land_shadow`, `graticule_stroke`, `highlight_fill`). Use these to explain why a colour match fits (e.g. land is `teal-5`, surround is `azure-1`). Unused map elements are omitted.
- **`water_fill`** is ocean/sea on globes, and the surround behind a country silhouette on flat country maps (even when that surround is not real water).
- **Two different meanings of transparent.** As a colour value (`land_fill: "transparent"`) it means that part of the map is see-through. As the boolean `transparent: true` it means the whole canvas background is see-through, for layering over other images. Never pass `transparent` as `colour=`.
- Ask for more maps with `page`, reusing the `seed` from the previous result.

## Presenting results

- Summarize how many maps matched and which filters applied.
- Prefer **links from tool results** (`url`) over paraphrased paths.
- Include **attribution** when present.
- When useful, mention `map_of`, (if present) `boundary_type` / `boundary_count`, and `colours` (e.g. land fill / surround).
- When the ChatGPT cover grid UI is shown, still keep text useful for clients without UI: short list with titles and links.
- For a single pick, call `get_map` and lead with description + Super Map World URL.

## Licence and downloads

Policy overview: [Help & FAQs](https://supermap.world/help) (Pro licence text: [SMW Licence](https://supermap.world/licence)).

- Published catalog maps are free to use commercially **with attribution** (CC-BY or share-alike).
- Share-alike: adaptations must stay under the same licence.
- Prefer `get_map` fields (`licence`, `licence_url`, `share_alike`, `attribution_example`, `downloads`) over inventing policy — search results stay slim.
- HD / SVG / no-attribution need an account + licence on the site; MCP does not purchase or unlock.

## What the Super Map World map page provides

Each result `url` opens that map’s public page on Super Map World (not an MCP download). On the page, users can typically:

- See a **large preview** of the map
- Read **description**, **location**, **projection**, **colour scheme**, and **data source / attribution**
- **Download** preview PNG sizes; **full PNG** and **SVG** (when the data source is vector) usually need an account with access / licence. For raster datasets (physical relief), downloads are **PNG only** (SVG is not possible from a raster source).
- Start **Edit** (custom map from this base) when the map is vector (raster maps cannot be customised)
- Open **Animate** templates when the map supports animation
- Follow related filters (same colour, projection, or location)

Do **not** claim MCP can download full-resolution files, edit maps, or create animations in chat. Point the user to the map URL for those actions.

## When not to call tools

- General geography trivia with no map or catalog intent
- Anything in the "Not in the catalog" list above — say what's available instead
- Someone's private, unpublished or custom maps (only public published maps here)
- Billing, account or licence changes (no tools for these; point at the site)

## Example flows

**“Maps of France”** → `search_maps(location: "France")` → list with links; optional `get_map` for one number.

**“World map looking at Japan”** → `search_maps(location: "Japan", projection: "Orthographic")`.

**“Maps of Tokyo”** (or a location search with no hits) → `resolve_location(query: "Tokyo")` → if it's a town/city with a `country_fallback`, `search_maps(location: "Japan")`, saying there are maps of Japan rather than of Tokyo itself.

**“A street map of Berlin”** → no tool call. Say the catalog is country and world maps only, then offer `search_maps(location: "Germany")`.

**“What colours do you have?”** → `list_colours()` → summarise the palette (or offer a few groups).

**“Show me the greens”** → `list_colours(query: "green")` → list matching names (and CSS if useful), then offer `search_maps` if they want maps.

**“What’s the CSS for violet-5?”** → `list_colours(query: "violet-5")` → answer with the entry’s `css` value.

**“Teal land and pale blue surround”** → `search_maps(land_fill: "teal", water_fill: "pastel azure")` (add `location` / `projection` if known).

**“See-through land with a blue outline”** → `search_maps(land_fill: "transparent", land_stroke: "blue")` (add `location` / `projection` if needed).

**“Maps of France with province boundaries” then “in blue with white borders”** → first `list_coverage(location: "France", boundary_type: "province")` (or `search_maps` with `boundary_type: "province"` if confident); then `search_maps(location: "France", boundary_type: "province", land_fill: "blue", borders_stroke: "white")`.

**“Are there maps of Ukraine showing raion boundaries?”** → `list_coverage(location: "Ukraine", boundary_type: "raion")` → if none, explain what *is* available from `available` (e.g. ADM1), and offer `search_maps` with that level.

**“What boundary data do you have for the UK?”** → `list_coverage(location: "United Kingdom")` → summarise datasets, levels, unit counts, licenses, and version notes.

**“What projections do you have for world maps?”** → `list_coverage(location: "the World")` → summarise the projections available (e.g. NaturalEarth1, Mercator, Equirectangular, Orthographic, PeirceQuincuncial).

**“Physical relief maps of the world”** → `search_maps(location: "the World", data_format: "raster")` → explain it's Natural Earth Gray Earth shaded relief available across 30+ projections, with PNG downloads on the site (SVG is only available for vector maps).

**“Tell me more about map #654496”** → `get_map(number: 654496)` → describe and share `url` for preview / download / edit on the site.
