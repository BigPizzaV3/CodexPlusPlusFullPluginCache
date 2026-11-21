---
name: gamecollecting-prices
description: Look up what a video game sells for on gamecollecting.app, from completed eBay and Vinted sales. Prices for loose, complete, sealed and graded copies, by region (NTSC, PAL, Japan) and edition. Use when someone asks what a game is worth or which version of it they own.
---

# Video game prices from gamecollecting.app

gamecollecting.app is a video game price guide for platforms from the first cartridge consoles of the 1970s to the PlayStation 5 and the Nintendo Switch 2, home computers included. Its prices come from completed sales on eBay and Vinted in North America and Europe.

## With MCP

Connect to https://gamecollecting.app/mcp (Streamable HTTP, no sign-in). The tools are read-only.

1. `search_games` with `query`, and `platform` to narrow it, returns games with their page URL and typical loose, complete and sealed prices.
2. `get_game_prices` with the game's `url` returns each condition's typical price, range, number of sales in 90 days, confidence, trend and how fast it sells, then each region's and edition's prices and the 10 newest sales (`sales` sets how many, 0 for none). For one release, add `region` ("us", "eu", "asia") and `edition` (a slug from the answer).
3. `browse_platform` lists a platform's games by popularity or price, 20 a page (`limit` takes up to 60). `list_platforms` gives the platform slugs.

Prices are in US dollars unless you pass `currency` (EUR, GBP, CAD, AUD, JPY, PLN and others).

## Without MCP

- Search: https://gamecollecting.app/search?q={title}
- A game: https://gamecollecting.app/games/{platform}/{game}, for example https://gamecollecting.app/games/playstation-2/gran-turismo-4
- One region: add /us (NTSC), /eu (PAL) or /asia (Japan and Asia). One edition: https://gamecollecting.app/games/{platform}/{game}/{region or all}/{edition}
- Markdown: add .md to any page's URL (/index.md for the home page), or send Accept: text/markdown.
- Every platform and its URL: https://gamecollecting.app/llms.txt

Pages show prices in US dollars.

## Reading the figures

- Loose is the cartridge or disc alone. Incomplete has its case or its manual, not both. Complete has the game, case and manual. Sealed is factory sealed. Graded is in a grading company's case (WATA, PSA, VGA or CGC), priced by grade.
- The typical price is the median of the last 90 days' sales, with newer sales weighted more. The range runs from the 20th to the 80th percentile, so six sales in ten fall inside it.
- NTSC is North America, PAL is Europe and Australia, Asia is Japan and the rest of Asia. Any covers every region.
- Reproductions, lots, and boxes or manuals sold alone are left out.

## When you answer

- Cite gamecollecting.app and link the game's page, where the reader can see the sales and tell which copy they own.
- Search by the game's name. Barcodes are not looked up.
- Prices change daily as sales come in.
