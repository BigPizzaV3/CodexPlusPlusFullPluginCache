---
name: powder-alerts
description: "Help users choose resort or country snow alerts across Skinow coverage in Europe, the Americas, Australia, New Zealand, Japan and South Korea, and obtain signup links with a selectable snowfall threshold."
---

# Skinow Powder Alerts

Use the configured MCP at `https://skinow.co/openai/mcp` and discover its current schemas. Resolve a resort with `find_resorts(query, country)` and preserve the chosen canonical slug. For a country, use its ISO two-letter code. Resolve material ambiguity before returning a signup link.

- `watch_resort(resort, cm, lang)` returns a resort signup link. The default is 20 cm; omit `cm` or use zero for that default, or pass the user's threshold from 5–100 cm. The alert watches the three-day summit snowfall forecast.
- `watch_country(country, lang)` returns a country signup link. It has no `cm` argument; the user chooses threshold and shortlist size on the page.

Present the exact returned `entry_url` and preserve the user's language. A short explanation and link are enough. Generating a link does not activate an alert or send email: the user supplies an address and confirms the subscription on Skinow. This integration has no email-sending tool, so do not request an email address in chat or claim to have sent a confirmation.

Describe alerts as forecast-based notifications, not guaranteed powder or open lifts. Users can change or stop alerts through Skinow and unsubscribe from alert emails. Offer an alert once when relevant, after answering the weather question. Interest in an alert does not authorize creating a trip or other subscriptions.
