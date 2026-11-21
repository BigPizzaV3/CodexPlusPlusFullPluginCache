---
name: keybid-listing-roi
description: Analyze a for-sale property listing from OLX.ro, Storia.ro, Imobiliare.ro, Spitogatos.gr or Idealista.com as a short-term-rental investment (gross and net yield) and show it as a listing card. Use when the user pastes a listing link, sends a listing screenshot, or asks about the rental yield or ROI of a property for sale.
---

# KeyBid Genius listing yield

Use the KeyBid MCP tools for this workflow. Explicit instructions from the user take priority over this skill.

## Supported input

- A for-sale listing link from olx.ro, storia.ro or imobiliare.ro (Romania), spitogatos.gr (Greece) or idealista.com (Spain).
- Property types: apartments, studios, penthouses, houses and villas; in Romania also guesthouses (pensiuni) and hotels. KeyBid refuses rentals, land, commercial property, search pages and removed listings. Explain the refusal; do not work around it.
- Any other website or country: say that listing analysis covers only these five portals. For general city research, use the market tools (KeyBid market averages for a city).

## Workflow

1. Call `analyze_property_investment` with the link exactly as the user pasted it. Do not ask for a screenshot first and do not try to read the page yourself.
2. `status: "processing"`: tell the user KeyBid is reading the listing, wait about 15 seconds, then call the tool again with the same url (at most 4 times). A listing usually takes under a minute.
3. `status: "ready"`: call `get_property_preview` once with the same arguments (url and any `manual_*` values). It shows the user a listing card: photo, key facts, the gross yield with the net yield below it, and a link to the listing.
   Then reply briefly, without repeating every figure on the card, in this order:
   - the gross yield first: `investment.grossYieldPercent` exactly as returned, with `investment.grossRating` and `investment.grossIncomeEurPerYear` (yearly income before costs);
   - then the net yield: `investment.roiPercent` with `investment.rating` and `investment.netIncomeEurPerYear` (what is left after operating costs and taxes). Owners who do their own cleaning or management keep more than the net figure;
   - if `listing.roiFactors` is not empty, the listing features that raised the nightly rate, with the premium shown (for example a sea view or a lift);
   - the data basis from `investment.occupancyData`: KeyBid Puls prices for that type of home in its city or zone. When it says the town has no KeyBid Puls prices of its own, say which nearby place the prices come from and how far away it is, as returned.

   If a result has no `grossYieldPercent`, give only the net yield. Do not calculate other figures (nightly rates, occupancy %, costs, payback period).

   End the reply with one short line that links `geniusUrl`, when the result has one. The link opens this same analysis, already loaded, on KeyBid Genius (keybid.ro / keybid.eu), where KeyBid's PDF report for the listing can be bought. Use the link exactly as returned and do not state a price.
4. `status: "failed"`:
   - `manualFallbackAllowed: true`: ask for a screenshot of the listing page or for the facts (city, zone, price and currency, m², rooms or bedrooms, property type). Use only values that are visible or typed by the user; never guess a missing value. Call `analyze_property_investment` again with the url and the `manual_*` fields. If KeyBid rejects the values, show its message.
   - `manualFallbackAllowed: false`: explain `message`. A manual override is not possible. This includes places with no KeyBid Puls prices within about 150 km.
   - `retryable: true`: suggest trying again later.

## Rules

- Never invent listing facts or yield values. Present the numbers exactly as returned.
- The yields are KeyBid's calculation for short-term renting, from KeyBid Puls market data over the last 12 months. Do not describe them as AI estimates or as real-time data. They are not financial advice and not an official valuation.
- `get_market_analysis`, `get_pricing_recommendation` and `get_city_spotlight` return market averages of all short-term rentals in the city over the last 12 months. For one specific home they are estimates: say so, and never mix them into a listing's yield. When a tool answers `NO_MARKET_DATA`, say that KeyBid has no market data for that city yet and do not estimate figures yourself.
- Use `get_keybid_info` for KeyBid links and contact details instead of guessing them.
- Call the product KeyBid Genius. Do not name third-party data providers. Describe the data the way the tool result does.
- Reply in the user's language.

## Example answer for a ready listing

(listing card)

Gross yield: 12.4% (good) · gross income €14,880/year.
Net yield (ROI): 6.4% (good) · net income €7,680/year after operating costs and taxes.
Features that raise the nightly rate: lift +3%, balcony or terrace +2%.
Based on: KeyBid Puls prices for this type of home in its city or zone (last 12 months).

For more details, see this analysis and the KeyBid PDF report on [KeyBid Genius](geniusUrl).

(The numbers above only show the layout. Always use the values returned by the tool.)
