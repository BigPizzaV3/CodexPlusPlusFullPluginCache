---
name: find-a-home
description: Help someone find a home to buy or rent in Portugal with Portal Imobiliário - turn their wishes into filters, compare prices with the market, and set an alert.
---

# Find a home in Portugal

Use this when someone describes the home they want in Portugal.

1. Gather the essentials, asking only for what is missing: buy or rent, place (district, municipality or parish), type, budget, bedrooms. Features (pool, garage, garden, terrace, sea view...) and condition are optional.
2. Run `search_properties`. If the place is ambiguous, the result lists other places with the same name (`outras_localizacoes`): ask which one.
3. Present the best matches briefly: price, price per m², bedrooms, area, parish, and the `face_ao_mercado` comparison (asking price per m² against the market value of the municipality, INE). Give each listing's link and the link to the full search.
4. For context on price, call `area_prices` for the same place and type.
5. With no or few results, suggest widening the budget or area, or offer `create_alert` so the person is told when a match appears or a price drops. Confirm the filters before creating an alert.
6. Never invent listings, prices or contacts. Contact with the advertiser is through the form on the listing page.
