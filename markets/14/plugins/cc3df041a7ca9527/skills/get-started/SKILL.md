---
name: get-started
description: First use of Portal Imobiliário - sign in, then what the person can ask (search homes in Portugal, prices per m², alerts, favourites; listings for agencies).
---

# Getting started with Portal Imobiliário

Portal Imobiliário (https://portalimobiliario.com.pt) is a free real estate portal for Portugal.

1. The first call asks the person to sign in on portalimobiliario.com.pt (email link, password or Google). A new account is created on the first sign-in, free.
2. After sign-in, call `whoami` once to learn the account: a person looking for a home sees search, prices and alerts tools; an agency or owner also sees the listing tools.
3. Offer what fits, in the person's language (Portuguese from Portugal by default):
   - search homes: `search_properties` (place, type, price, bedrooms, features, `mercado: ["abaixo"]` for below market value);
   - prices per m² of an area: `area_prices`;
   - a listing: `get_listing`;
   - alerts for new listings and price drops: `create_alert`, then `alert_updates`;
   - favourites: `list_favorites`, `add_favorite`, `remove_favorite`;
   - calculators: `simulate_imt`, `simulate_mortgage`, `simulate_capital_gains`, `estimate_value`.
4. Always share the `url` returned by the tools: it opens the same search or page on the portal.
5. Advertisers' contact details are not available through the app. To contact an advertiser or book a visit, the person uses the form on the listing page.
