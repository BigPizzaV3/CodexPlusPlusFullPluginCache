# Tailor.ai

**Find clothes from real shops.**

Tailor.ai finds clothes you can actually buy. Ask for what you're after, such as a white
linen shirt under R600, an outfit for a summer wedding, or a warm coat for a week in
London, and Tailor.ai searches the retailers' own online shops and shows the pieces as
cards, with photos, prices and a link to the product page.

![Tailor.ai](assets/logo.png)

## Shops

| Country | Stores | Prices in |
| --- | --- | --- |
| South Africa | H&M, Cotton On, Zara, Mango | Rand (R) |
| United States | Zara, Cotton On | US dollars ($) |
| United Kingdom | Zara, Cotton On | Pounds (£) |

Women's, men's, kids' and baby clothes, plus shoes, bags and accessories. Prices are in
each shop's own currency and aren't converted, and retailers ship only within their own
country, so Tailor.ai searches the shop where you live.

## What you can ask for

- Clothes by description, budget, store, colour, size or sale
- A change to a piece you like: "same, but in navy" or "but cropped"
- Look-alikes, cheaper alternatives, or the same look at another store
- A complete outfit for an occasion or dress code, within a budget
- A mix-and-match capsule wardrobe for a trip or a new season

Every card has **Tailor** and **Similar** buttons, so you can change a piece or see more
like it straight from the results. **Buy** opens the product on the retailer's site.

Some things to try:

- "I'm in South Africa. Find me a white linen shirt for men under R600."
- "I need an outfit for a summer wedding in London: a dress, shoes and a bag, about
  £150 in total."
- "Pack me a 5-day capsule wardrobe for New York in autumn, women's, under $300."
- "Show me cheaper coats that look like that one."

Say where you shop and who it's for, and describe what you want the way a product page
would. More tips: <https://www.tailor.ai/docs>.

## What's in the plugin

- **The Tailor.ai connector** (`https://mcp.tailor.ai/mcp`). It has six read-only tools:
  search products, find similar products, tailor a product, show a set of products, get
  one product's details, and a catalogue overview. Connect it when the plugin asks; there
  is no account or sign-in.
- **Three skills** that teach the assistant to shop like a stylist:
  - `build-an-outfit`: a complete look for an occasion, dress code or budget
  - `capsule-wardrobe`: a mix-and-match set for a trip or a new season
  - `find-a-cheaper-version`: look-alikes for less, at another store or on sale

## Data and privacy

The skills are instructions only: they run no code and send nothing themselves. The
connector sends the searches the assistant makes (search text and filters such as
country, department, store and price) to `mcp.tailor.ai`, operated by Light Bulb Research
(Pty) Ltd. Tailor.ai never sees your conversation, name or account.

Tailor.ai logs those searches, without your IP address or identity, to improve results.
Product links go through `www.tailor.ai/go/…`, which records the click (with a hash of
your IP address that changes daily, never the address itself) and redirects you to the
retailer. Logs are deleted after two years. Tailor.ai has no accounts and sets no cookies.

Tailor.ai only reads its own index of public product listings: it can't buy
anything, see your orders or sign in to a store. You buy on the retailer's site, and
stock and prices can change, so the retailer's page is always the final word.

- Privacy policy: <https://www.tailor.ai/privacy>
- Terms of service: <https://www.tailor.ai/terms>

## Support

Questions, bugs, or a store you'd like added: <tailor@lightbulbresearch.com>.

Building or releasing the plugin: see [DEVELOPING.md](DEVELOPING.md).

## License

MIT, see [LICENSE](LICENSE).
