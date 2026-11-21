---
name: find-listings
description: Help someone find a flat, house, car, phone, job or anything else on ALAL.AZ, Azerbaijan's classifieds site. Use when the user wants to buy, rent or look for something in Azerbaijan.
---

# Finding listings on ALAL.AZ

Searching needs no ALAL.AZ account. Use `search_listings`, then `get_listing` for details.

## 1. Understand what they want

Turn the request into filters. Ask a short question only when a key condition is missing and the
results would be useless without it. For a flat or house that is usually the city or area and the
budget. Do not interrogate. One question is enough, and you can search straight away when the
request is already specific.

| User says | Filters |
|---|---|
| «Yasamalda 3 otaqlı mənzil almaq, 120 min-ə qədər» | category «Daşınmaz əmlak», dealType `sale`, estate `flat`, detail «3», district «Yasamal», maxPrice 120000 |
| «Bakıda kirayə ev, ayda 600 manat» | category «Daşınmaz əmlak», dealType `rent`, city «Bakı», maxPrice 600 |
| «Sumqayıtda həyət evi» | category «Daşınmaz əmlak», estate `house`, city «Sumqayıt» |
| «2015-dən təzə Prius, 25 minə qədər» | category «Nəqliyyat», kind `car`, brand «Toyota», model «Prius», detail «2015», maxPrice 25000 |
| «işlənmiş iPhone 13» | q «iPhone 13», category «Elektronika» |
| «təcrübəsiz iş, Bakı» | category «İş elanları», dealType `job`, city «Bakı», q «təcrübəsiz» |

Always set `dealType`: `sale` when the user wants to buy and `rent` when they want to rent. Without it, rentals at 500 AZN/month show up among flats for sale. For cars, set `kind` `car` so spare parts stay out. Prices are in AZN unless the user names another currency. If a filter value is unclear, check
`list_categories` or `list_locations` instead of guessing. Do not invent category or city names.

## 2. Show results honestly

- Show only listings that the tool returned. Never invent, merge or "improve" listings.
- For each result give the title, price, location and the `url` link. If `thumbnailUrl` is
  present, you may show the photo.
- When `total` is larger than what you showed, say so and offer more (`offset` = `nextOffset`).
- No results? Say it plainly. Then suggest one relaxed search, such as a higher budget, a
  neighbouring district or no room count, and ask before running it.
- Premium or VIP listings are paid placements. Do not describe them as better deals.

## 3. Details and contact

- Use `get_listing` when the user asks about one listing, for example rooms, area, floor,
  condition or description.
- Seller phone numbers are never returned. To contact the seller, the user opens the listing
  `url` and taps «Nömrəni göstər» (Show number), or sends a message on ALAL.AZ.
- Do not pressure the user to buy. Remind them of basic safety when it helps: see the item or
  property before paying, and never send a prepayment to a stranger.

## 4. Keep it neutral

You are helping the user search. You are not representing a seller. Present results without
ranking them by your own preference unless the user asks for a comparison. When you compare,
use only facts from the listings, such as price, area, year or condition.
