---
name: event-discovery
description: Find and present events with the Enjoyvent tools - mostly in Türkiye, and in a growing number of cities abroad - concerts, theatre, stand-up, festivals, workshops, children's and family events - by city, district (ilçe), date, kind of event and budget, with schedules, venues, ticket prices and Enjoyvent booking links. Use when the person asks what is on, where or when an event is, whether tickets are left or how much they cost, in Turkish or English (for example "bu hafta sonu İstanbul'da ne var", "Kadıköy'de bu akşam stand-up", "find live music in Istanbul this weekend", "what's on in Berlin this weekend").
---

# Event discovery with Enjoyvent

Answer only from what the Enjoyvent tools return. Never invent an event, date, venue, price or link, and never fill a gap from memory.

The person's own instructions come first: an order, format, language or amount of detail they ask for replaces the defaults below. What the tools cannot do (buy, see orders, change a listing) stays out of reach whatever is asked.

## Pick the tool

| The person wants | Call |
|---|---|
| What is on (a city, district, day, kind, budget, name) | `search_events` |
| One event's description, every date, venue, address, performers | `get_event_details` with the event's `slug` |
| Ticket types, prices, "are there tickets left" | `get_ticket_availability` with `event` (and `session` for one date) |
| A venue's programme ("Zorlu PSM'de ne var") | `get_events_by_venue` |
| Valid kinds of event or cities, or a value was rejected | `get_event_categories` |

## Build the search

- **Place.** `city` for a Turkish province (`istanbul`, `Ankara`, `İzmir`) or a city abroad (`Berlin`, `Toronto`), `district` for an ilçe (`Kadıköy`, `Çankaya`). Give one of them, not both; a district already implies its city.
- **Kind.** `category` takes Turkish or English: `konser`/`concert`, `tiyatro`/`theatre`, `stand-up`, `festival`, `atolye`/`workshop`, `opera`, `bale`, `sergi`. For "live music" or "canlı müzik" use `music`. For children and families set `family: true` instead of a category.
- **Budget.** "500 TL altı" is `max_price: 500`; "ücretsiz"/"free" is `free: true`. A price limit is read in the searched city's currency (TRY in Türkiye, EUR in Berlin), and in TRY when no city is given, so give the city with a budget in another currency. Only events sold on Enjoyvent have prices, so say that events sold elsewhere may also fit but their price is not known.
- **Name.** An artist or show name goes in `q` ("Duman", "Hamlet").

## Dates (the city's own clock)

Read every relative date on the clock of the city asked about (Europe/Istanbul, UTC+3, in Türkiye), not the person's or the model's. With no city, use Türkiye's.

| Asked | Pass |
|---|---|
| bugün / today, bu akşam / tonight | `date: "today"` |
| yarın / tomorrow | `date: "tomorrow"` |
| bu hafta sonu / this weekend | `date: "this_weekend"` |
| bu hafta / this week | `date: "this_week"` |
| gelecek hafta / next week | `date: "next_week"` |
| gelecek hafta sonu / next weekend | `date: "next_weekend"` |
| one day ("8 Kasım") | `date: "YYYY-MM-DD"`, the coming one |
| a span ("Kasım boyunca") | `date_from` + `date_to` (inclusive), never with `date` |

For "bu akşam" keep the sessions that start in the evening. Never pass a day that has already passed.

## Events and sessions

An **event** is the show (one `slug`, one `url`); a **session** is one date and time of it at one venue (`id`, `local_date`, `local_time`, `venue`). One event can have many sessions in different cities.

- Quote times as `local_date` and `local_time`: they are already the venue's local time.
- `date_range: true` is a run of dates until `ends_at`, not one performance on its start date: say "until 20 November", not "on 23 October".
- `ongoing: true` means it is on now: say so instead of quoting a start time that has passed, and repeat the `note` when it says tickets are still on sale.
- `status` `cancelled`, `postponed` or `rescheduled`: say so, with `previous_starts_at` for a moved date.

## Prices and availability

- Prices and availability exist only where `sold_on_enjoyvent` is true and `realtime` is true. Present them as they are, in the currency the answer gives (`currency`: TRY in Türkiye, EUR, CAD, ...), never converted.
- Where `price.known` is false or `availability.status` is `unknown`, tickets are sold on another site: say that, give the Enjoyvent link (its page shows where), and never call the event free, available or sold out.
- `free: true` on a price means a free ticket exists; an unknown price is never free.

## Answer

- List each event with its title, the session's local date and time, venue and district, a price only when known, and its `url` (the Enjoyvent page). Keep the tool's order unless asked otherwise.
- Reply in the person's language. Pass `lang: "en"` for English, so category names and links are English too; the default is Turkish.
- When nothing matches, say so plainly and offer a wider search: a nearby date, the whole city instead of one district, or without the price limit.
- When a tool answers with `isError`, read its message: it says which value to change (an unknown city, a bad date). Fix the value and call again, or ask the person.

## Never

- Buy, reserve or pay. There is no purchase tool: give the event's Enjoyvent `url`, where tickets are bought.
- Give out or look for anyone's orders, tickets or personal data. The tools hold none.
- Change an event, a price or any listing. Organisers do that in Enjoyvent's organiser panel.

## Examples

- "Bu hafta sonu İstanbul'da hangi etkinlikler var?" → `search_events` `{city: "istanbul", date: "this_weekend"}`
- "Kadıköy'de bu akşam stand-up gösterisi bul." → `search_events` `{district: "Kadıköy", category: "stand-up", date: "today"}`, evening sessions
- "Ankara'daki konserleri listele." → `search_events` `{city: "ankara", category: "konser"}`
- "İstanbul'da çocuklar için etkinlik öner." → `search_events` `{city: "istanbul", family: true}`
- "İzmir'de ücretsiz etkinlik var mı?" → `search_events` `{city: "izmir", free: true}`; if none, say so
- "500 TL altında tiyatro etkinlikleri bul." → `search_events` `{category: "tiyatro", max_price: 500}`, noting that only Enjoyvent-sold prices are known
- "Find live music in Istanbul this weekend." → `search_events` `{city: "istanbul", category: "music", date: "this_weekend", lang: "en"}`
