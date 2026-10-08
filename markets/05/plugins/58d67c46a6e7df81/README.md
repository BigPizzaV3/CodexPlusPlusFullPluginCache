# Stymie Golf

Read-only golf course discovery and trip planning through the public Stymie MCP server.
Start with `find_nearby_courses` for a location, then `build_golf_trip` with the returned center. Copy returned course URLs. Use `search_courses` for a named course.

No authentication or private Stymie account access. No bookings, purchases, alert enrollment, writes or live tee-time inventory. Equipment links may be affiliate links.

Portable hosts use `plugin.json` and `mcp.json`. Codex-compatible hosts can use `.codex-plugin/plugin.json` and `.mcp.json`; both declare the same single remote server. Course cards are supplied by that MCP server at runtime.

Support: https://stymie.golf/mcp (contact anthony@stymie.golf)
Privacy: https://stymie.golf/privacy
Terms: https://stymie.golf/terms
