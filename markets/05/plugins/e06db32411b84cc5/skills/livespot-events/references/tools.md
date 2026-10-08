# LiveSpot tool reference

All eight tools are read-only, open-world, and non-destructive. Public endpoint, no auth.

## search_events
Search upcoming events across Sweden.
- `text` (string, optional): free-text search over titles, artists, venues, descriptions.
- `city` (string, optional): city slug from `list_cities` (ASCII, e.g. `goteborg`, `malmo`).
- `category` (string, optional): category slug from `list_categories`; Swedish and English slugs both work.
- `date` (string, optional): date or date range filter.
- `maxPrice` (number, optional): maximum ticket price in SEK.
- `limit` (number, optional): page size.
- `page` (number, optional): page number for pagination.

Returns a paginated list of events with id, slug, title, date, venue, city, price, and a markdown link.

## get_event
Full detail for one event.
- `id` (string): event id, slug, or short id (e.g. `gransen-karlskrona-47154d83` or `47154d83`).

Returns description, venue with address, date and time, price, availability, and ticket links.

## list_cities
No parameters. Returns covered cities with slugs, regions, and current event counts.

## list_categories
No parameters. Returns the static category catalog with Swedish and English slugs (concerts, theatre, musicals, dance, comedy, sport, festivals, family).

## browse_city
Upcoming events in one city.
- `city` (string, required): city slug.
- `category` (string, optional): narrow to one category.

## get_related_events
Events similar to a given event by city, date, and category overlap.
- `id` (string, required): event id or slug.
- `limit` (number, optional): at most 12.

## search (Deep Research shim)
- `query` (string, required): maps a natural-language query to matching event ids, titles, and URLs.

## fetch (Deep Research shim)
- `id` (string, required): returns the full text of one event resource by id.
