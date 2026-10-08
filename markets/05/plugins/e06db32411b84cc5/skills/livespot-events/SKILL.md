---
name: livespot-events
description: Find things to do in Sweden with LiveSpot. Use when the user asks about events, concerts, theatre, musicals, comedy, sport, festivals or family activities in Sweden or a Swedish city (Stockholm, Gothenburg, Malmo, Uppsala and more), including "what's on", weekend plans, date-night ideas, or events under a budget. Not for events outside Sweden and not for booking or buying tickets - LiveSpot is read-only and links out to ticket sellers.
---

# LiveSpot: Swedish event discovery

LiveSpot is an MCP app that searches upcoming public events across Sweden, refreshed daily from 13 ticketing providers. It is free, read-only, and needs no account or API key. Coverage is Sweden only.

## Trigger conditions

Use this skill when the user wants to find, compare, or get details about events in Sweden: "what's on in Gothenburg this weekend", "concerts in Stockholm under 500 SEK", "family activities in Malmo", "is there any theatre in Uppsala in October", or "more events like this one".

Do not use it for events outside Sweden, past events, or for completing a ticket purchase. For purchases, give the user the event's ticket link.

## Workflow

1. **Search first.** Call `search_events` with whatever the user gave you: free text, city, category, date range, or max price (SEK). Leave filters out when the user did not specify them.
2. **Resolve slugs when unsure.** Call `list_cities` for covered cities and `list_categories` for the category catalog. City slugs are lowercase ASCII without spaces or diacritics (Gothenburg is `goteborg`, Malmo is `malmo`). Category filters accept both Swedish and English slugs.
3. **Open details.** When the user picks an event or asks for more about one, call `get_event` with its id or slug from the search results. Details include description, venue, date and time, price, availability, and ticket links.
4. **Shortcut for one city.** For "what's on in <city>" with no other filter, `browse_city` lists upcoming events in that city, optionally narrowed by one category.
5. **Recommend similar events.** For "more like this", call `get_related_events` with the event id (limit is at most 12).
6. **Paginate.** Search results are paged; ask before loading more, and pass the next `page` when the user wants more.

The `search` and `fetch` tools are Deep Research shims. Use them only inside a Deep Research run; for normal chat, use the tools above.

See [references/tools.md](references/tools.md) for the full parameter list of every tool.

## Presenting results

- Keep the markdown event links the tools return so the user can open the event page on LiveSpot; never strip or rewrite them.
- Include the essentials per event: title, date, venue, city, and price in SEK (say when entry is free).
- When the user wants to attend, point them to the event's ticket link - LiveSpot cannot book or sell tickets.
- If a search returns nothing, say so plainly and suggest broadening the date range, city, or price instead of guessing at events.
