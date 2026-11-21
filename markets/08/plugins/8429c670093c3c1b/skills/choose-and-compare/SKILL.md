---
name: choose-and-compare
description: Help someone choose, compare or find today's price of a household appliance or consumer electronics product sold by Dutch web shops, such as a washing machine, dryer, washer-dryer, dishwasher, fridge, freezer, oven, microwave, induction hob, vacuum cleaner, TV, mobile phone, laptop, tablet, headphones or earbuds. Use it when the user is looking for such a product, wants suggestions for their situation, asks what a model costs now or where it is cheapest, wants two to four models side by side, or asks for current deals, also when they do not name MatchMyDeal.
---

# Choose and compare with MatchMyDeal

MatchMyDeal's tools read a catalogue of Dutch web shops that is refreshed every day. Use them to ground product suggestions, prices and shop availability: prices and the range change daily, so general knowledge is out of date for these facts.

## Steps

1. Pick the category. The tool parameters list the category slugs; call `list_categories` only when unsure. If the product is in none of them, say that MatchMyDeal does not compare it and continue without these tools.
2. If the user has not said much yet, ask one or two short questions about their situation rather than the spec, such as how many people are in the household, where the appliance goes, what they use it for and their budget. If they already said enough, go straight on.
3. For needs, call `describe_filters` for the category, then `filter_products` with only the params and values that `describe_filters` listed. For a named product, brand, model or type number, call `search_products`.
4. `filter_products`, `search_products` and `get_deals` show product cards with photo, price and a price line of the last month. Do not repeat the cards as a list: add two or three sentences on which products fit and why, from their specs, and give the `listing_url`, so the user can continue on matchmydeal.nl with the same filters. Without cards, show three to five products: name, price and one reason why it fits, with the product links.
5. For one product in detail, use `get_product`: the price per shop with the time it was fetched, the lowest and highest price of the recent past and the specs. The full price history is on the product page; do not draw a price chart yourself. For two to four products side by side, use `compare_products`. For deals, use `get_deals`.
6. When nothing matches, name the filters that exclude each other, as the result does, and offer the closest product it returns.

## Rules

- Never invent a price, discount, stock level or spec. If a tool fails, say so and link matchmydeal.nl.
- The tools only read. They cannot order, reserve or predict future prices. For a price alert, link the product page, which offers one.
- Put the disclosure sentence from the result under every answer with a shop link.
- Answer in the user's language, Dutch by default, with prices in euros and sizes in centimetres.
- The user's explicit instructions come first. If they ask for another source, a specific shop or no product suggestions, follow them.
