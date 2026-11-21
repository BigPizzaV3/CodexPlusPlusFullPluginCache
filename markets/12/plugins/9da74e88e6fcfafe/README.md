# UVLens

UVLens gives AI assistants UV index forecasts for anywhere in the world. Use it to check UV now or hour by hour, find the lowest-UV time for a walk or other outdoor plan, and check UV during calendar events. With a Fitzpatrick skin type, it also estimates how long until unprotected skin burns.

Burn times are estimates for unprotected skin and the skin type supplied. They are not safe exposure times and do not account for sunscreen, shade, reflection or photosensitivity.

## What it includes

- A remote MCP server at `https://mcp.uvlens.com/mcp`, with no sign-in. Its tools are read-only:
  - `search_places`: finds places matching a name the user typed.
  - `get_uv_forecast`: hourly UV for a place on a local date, with the peak, times UV is 3 or higher, and optional burn times.
  - `find_lower_uv_windows`: ranks lower-UV windows of a given length, or checks an activity at its own times.
- A skill that tells the assistant how to use the tools.

## Data sent to UVLens

Each tool call sends only what the request needs:

- Place search: the place name the user typed and an optional country code. UVLens passes the name to the [Open-Meteo](https://open-meteo.com) geocoding API.
- Forecasts: the coordinates of a place the user chose, a local date and times, and, when given, a skin type from 1 to 6.

UVLens does not use device location, and has no user accounts. It rounds coordinates to 0.1° for forecast lookup, and does not write tool arguments to its logs.

To answer quickly, the server keeps two caches in memory. Neither records who made a request:

- Place-search results, by place name, for up to 24 hours.
- Forecasts, by rounded coordinates, until the next forecast run and for no more than 24 hours.

Skin type is used only to calculate the response and is not cached or logged. Google Cloud's request logs record the time, the calling server's IP address and user agent for each request, but not its contents, and are kept for 30 days.

See the [privacy policy](https://uvlens.com/plugin-privacy) and the [terms](https://uvlens.com/license). For help, contact [support@uvlens.com](mailto:support@uvlens.com).

## Data sources

UV forecasts are based on NOAA UV index forecasts and include forecast cloud cover. Place search uses data from [Open-Meteo](https://open-meteo.com) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
