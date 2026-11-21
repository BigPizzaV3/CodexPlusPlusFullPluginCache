---
name: sparkl
description: Answer trading card questions about card prices, set values, release dates, price trends and rankings using Sparkl's public catalog for Pokemon, One Piece, Lorcana, Riftbound, Gundam, Fusion World, Sorcery, Grand Archive and Cyberpunk.
---

# Sparkl trading card catalog

Use Sparkl for supported trading card catalog questions. The connection is public and read-only and needs no account.

- Search with `search_cards` using `query` and, when known, `game`. Include the card name, collector number or set code in `query`; use `language` when a particular print language is requested.
- Get prices by finish with `get_card`, passing the exact `card_id` returned by search. Clarify ambiguous printings instead of guessing.
- For a set, call `get_set` with `game`, `set` (name or code), and `language` when appropriate. Its most valuable cards are not a complete card list.
- For announced sets, use `upcoming_releases`; for daily rises and falls, `price_trends`.
- Use `most_valuable_cards` for rankings in Pokemon, One Piece, Lorcana or Riftbound. Other supported games do not currently have this ranking.

Name each price source and currency: TCGplayer market price in USD, Cardmarket price in EUR, or an eBay estimate only when the result labels it that way. Include the returned Sparkl page link and observation dates. Prices are Near Mint, ungraded market references refreshed daily, not guaranteed sale prices. Distinguish daily trends from 30-day changes.

Do not invent missing prices or results. If a request exceeds available data, explain the limitation. Sparkl cannot access or modify personal collections, place purchases or sales, retrieve graded prices or sold listings, or provide catalogs for unsupported games. Do not invoke its tools to perform those actions.
