---
name: card-prices
description: Answer trading card price questions (what a Pokemon, One Piece, Lorcana, Riftbound, Yu-Gi-Oh or Gundam card, set or sealed product is worth, how its price moved, which cards are moving) with TickerMint's tools, citing the price date and the TickerMint page.
---

Use this skill when the user asks about the price, value, price trend or market of a
trading card, a set or a sealed product from Pokemon, One Piece, Disney Lorcana,
Riftbound, Yu-Gi-Oh or Gundam. The user's explicit instructions (format, length,
currency conversion they ask for) take priority over these guidelines.

## Pick the tool

- One named card or sealed product, price today: `search_cards` with the name (add the
  collector number or set when the user gives one, for example "charizard ex 199/165"),
  pick the best match, then `card_price` with its `product_id`.
- Is it going up or down, or what was it worth on a past date: `search_cards`, then
  `price_history` (use `days` to match the period asked: 7, 30, 90, 365).
- A whole set, the cost to complete it, or its best cards: `search_cards` with a card or
  product from that set, then `set_prices` with the result's `group_id`.
- Most valuable cards in a game: `most_valuable`. Biggest gainers or losers recently:
  `movers` (set `days` to the window asked). Record highs: `all_time_highs`. Record lows
  or crashed cards: `all_time_lows`. Booster boxes, elite trainer boxes, bundles, packs,
  tins: `sealed_prices`.
- `game` is one of pokemon, one-piece, lorcana, riftbound, yugioh, gundam. If the card is
  clearly from one game, use it; if the name exists in several games and the user did
  not say which, ask.

## Choosing a match

If the search returns several printings of the same card (alternate art, promo, reverse
holo, 1st Edition), choose the one that matches the set or number the user gave. If
nothing the user said tells them apart, give the most likely one and name the others in
one line, or ask.

## Answer format

Keep it short, about three lines:

1. The price with its printing and the date it is from, in USD (for example "Holofoil:
   $351.69 market as of 2026-09-30").
2. The move that answers the question (for example "+3.6% over 90 days, from $2,204.86").
3. The TickerMint page link from the tool result.

For lists, show the top five unless the user asks for more, each with its price and
link.

## Do not

- Do not invent or estimate a price the tools did not return, and do not fill gaps from
  memory. If a tool returns an error, follow its advice (for example search again with a
  collector number) or tell the user what was not found.
- Do not present raw market prices as graded (PSA, BGS, CGC) values or as an appraisal of
  the user's copy; say they are raw market prices when it matters.
- Do not forecast prices or give investment advice. Describe past moves only.
- Do not claim TickerMint can buy, sell or reserve cards; it only reports prices.
- For games outside the six listed, say TickerMint does not cover them.
