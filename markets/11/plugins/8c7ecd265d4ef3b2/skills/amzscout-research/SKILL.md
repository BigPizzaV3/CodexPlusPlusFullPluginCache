---
name: amzscout-research
description: >
  Research Amazon products, niches and brands with AMZScout's live Amazon data.
  Use when the user wants to check whether a product is worth selling, analyze a
  niche or its competition, find product ideas, look up a listing's keywords and
  ads, or review a brand's Amazon catalog.
---

# AMZScout research

This skill teaches you to orchestrate the granular AMZScout tools yourself: pick
the right tool(s), chain them into a workflow, and turn the raw data into a
clear seller-facing answer. The tools come from the `amzscout` MCP server.

If the AMZScout tools are not available in this session, say so — do not
fabricate AMZScout data.

## How to use AMZScout

- **The granular `amzscout_*` tools** (below) are the building blocks, and on a
  direct MCP connection they are ALL you get. You choose the workflow, chain the
  steps, and compose the answer yourself. This skill is about using them well.


## Granular tools (MCP)

| Tool | Args | Returns |
|------|------|---------|
| `amzscout_locate_asin` | `asins` (1–5) | Where an ASIN is listed: each marketplace's link, title, local price, sales. Uses 14 000 tokens of the account's data allowance per ASIN — only when the user asks where a product is sold (see Marketplaces). |
| `amzscout_analyze_product` | `asin`, `marketplace?`, `focus?` | Full audit of ONE product: verdict, demand/trend, pricing, competition, maturity, listing quality, GO/NO-GO. |
| `amzscout_reseller_amazon` | `asin`, `marketplace?`, `sections?` | Reseller / online-arbitrage view of ONE ASIN: buy box owner and price, FBA vs FBM offer counts, whether Amazon sells it, live offers, price levels 30/90/180/365 days, rank drops, out-of-stock share, buy box history. Call WITHOUT `sections` first — the summary usually answers; add sections (`buybox`, `competition`, `pricing`, `rank`, `availability`, `history`) only if it does not. Not for demand/revenue — that is `amzscout_analyze_product`. |
| `amzscout_compare_products` | `asins` (2–5), `marketplace?` | Side-by-side comparison of 2–5 ASINs — which is the stronger opportunity. |
| `amzscout_compare_niches` | `keywords` (2–5), `marketplace?`, `count?` | Head-to-head comparison of 2–5 niches/keywords — which niche is the better opportunity. |
| `amzscout_analyze_product_set` | `asins` (2–25), `focus?`, `marketplace?` | Market overview across an explicit set of ASINs (you already have the list). |
| `amzscout_analyze_niche` | `keyword`, `marketplace?`, `filters?`, `count?` | Niche/category overview: segments, top products, demand concentration, signals. |
| `amzscout_search_products` | `query`, `marketplace?`, `sort?`, `count?`, `filters?` | Discovery: a list of products for a keyword (no deep analysis). |
| `amzscout_find_by_brand` | `brand`, `marketplace?`, `sort?`, `count?`, `filters?` | Products listed under a brand on Amazon. |
| `amzscout_get_keywords` | `asin?`, `keyword?` (one or both), `marketplace?` | Keyword / SEO / PPC data — ASIN-scope (terms a product ranks for), keyword-scope (search data around a niche term), or **both** = the product's position for exactly that keyword. |
| `amzscout_search_knowledge` | `query`, `topK?` | AMZScout knowledge-base passages (how-to, AMZScout tool/feature info). |
| `amzscout_usage` | — | The user's AMZScout token balance (remaining / used / limit). Free. Use for "how many tokens do I have left", "my usage/balance". |

## When to use which

- Specific product — ASIN (`B0XXXXXXXX`) or Amazon link → `amzscout_analyze_product`. Bare ASIN with no marketplace known in this chat → ask the user once which marketplace (see Marketplaces).
- Reselling / online arbitrage / wholesale about a specific ASIN — "who has the buy box", "how many FBA/FBM sellers", "does Amazon sell it", "is this worth reselling", buy box price history → `amzscout_reseller_amazon`. Private-label "should I sell something like this" stays `amzscout_analyze_product`.
- "Where / on which Amazon marketplaces is B0… sold" → `amzscout_locate_asin` (uses data allowance).
- A niche / category / keyword phrase, or "is X worth entering / how saturated is X" → `amzscout_analyze_niche`.
- Product-design / attribute question about a niche ("what materials / sizes / packaging work for X") → `amzscout_analyze_niche` shows what the top sellers in the niche use — ground the design advice in that.
- 2–5 ASINs to compare head-to-head → `amzscout_compare_products`. A set of ASINs you want one combined overview of → `amzscout_analyze_product_set`.
- 2–5 niches/keywords to compare ("yoga mat vs resistance bands") → `amzscout_compare_niches`.
- Keyword / search-term / SEO / "does it have ads / what does it rank for" → `amzscout_get_keywords` (use `asin` for a product, `keyword` for a niche term).
- "What is the organic rank / position of B0… for <keyword>?" → `amzscout_get_keywords(asin, keyword)` — both at once. Pass the keyword exactly as the user wrote it. Answer with the **EXACT MATCH** row only; rows listed as variants (the same words with extra symbols, e.g. `standing lamp'`) are different keywords — never report their rank for the requested one. If there is no exact match, say the product has no tracked position for that exact keyword.
- "How do I… / what is…" educational, or "which AMZScout tool/feature for X" → `amzscout_search_knowledge`.
- Brand / company question → `amzscout_find_by_brand` (see Brand workflow below).
- Open-ended discovery ("find me top 10 yoga mats", "newest pet supplies", "cheapest kitchen items") → `amzscout_search_products`. (Differs from `amzscout_analyze_niche`: this is just a list; `amzscout_analyze_niche` is the full overview.)
- Vague exploration ("what should I sell", "I'm new to Amazon") → ask 1-2 short clarifying questions FIRST (marketplace, budget, business model). Don't fire tools blindly with a junk keyword.

## Workflows (chain tools)

- **Validate an idea:** `amzscout_analyze_niche(keyword)` → if crowded, `amzscout_search_products(query, filters:{maxReviews:100})` to find low-competition (few-review) entries → `amzscout_analyze_product(asin)` on the best 1-2 → optionally `amzscout_get_keywords(asin)` for SEO.
- **Audit a product:** (no marketplace known in this chat → ask the user once) → `amzscout_analyze_product(asin, marketplace)` → optionally `amzscout_get_keywords(asin)` for keyword/PPC depth.
- **Research a brand:** `amzscout_find_by_brand(brand, sort:"revenue")` → build a structured brand overview (below) → optionally `amzscout_analyze_product` on a standout ASIN.
- **Check a listing for reselling:** (no marketplace known in this chat → ask the user once) → `amzscout_reseller_amazon(asin, marketplace)` without `sections` → judge room on the listing: Amazon or one seller holding most of the buy box = little room, many FBA offers = price competition, high out-of-stock share = supply gap, frequent rank drops = fast sales → only if the user asks for more detail, call again with the needed `sections`.
- **Keyword/PPC question:** `amzscout_get_keywords(asin)` (product) or `amzscout_get_keywords(keyword)` (niche term).

## Brand workflow (important)

1. Always call `amzscout_find_by_brand(brand, sort:"revenue", count:25)` first.
2. Synthesize a structured BRAND OVERVIEW — hit each section when data allows:
   - **Catalog scope** — "Found N products under '<brand>' on <marketplace>" + inferred category mix.
   - **Performance bracket** — top performer's monthly sales + revenue, total visible revenue, BSR range.
   - **Top 3 best-sellers** — ASIN, short name, price, monthly sales, BSR, rating + reviews (table, never raw JSON).
   - **Pricing strategy** — low / median / high price + one-line interpretation.
   - **Notable signals** — highest rating, freshest listings (`sort:"newest"`), best-reviewed (`sort:"reviews"`), gaps.
3. **Honesty:** our tools only see Amazon marketplace data. NEVER invent founding year, HQ, parent company, founder, history, or socials. If asked, say: "I can only see this brand's Amazon catalog — not company history. From Amazon: …".

## Marketplaces

Codes: `COM` (US), `CO_UK` (UK), `DE`, `FR`, `IT`, `ES`, `CA`, `COM_MX`, `COM_BR`,
`IN`, `CO_JP`, `COM_AU`, `AE`, `SA`. Pass `marketplace` whenever the user named a
country / Amazon domain (or pasted an amazon.<domain> link), or a marketplace was
already settled earlier in the conversation. Keep the same `marketplace` across a
chain of calls or the data won't line up.

**ASIN without a country → ask once per chat, never assume US.** The same ASIN is a
separate listing on every marketplace it exists on (own price, sales, reviews, sellers).

1. **Already known?** Use that marketplace, without asking, when the user named a country
   ("in Italy", "UK"), pasted an Amazon link (take the code from its domain, table below),
   or it was settled earlier in THIS conversation. The user's language is NOT a signal —
   German speakers sell on UK/US too.
2. **Otherwise ask once** — in the user's language, before any ASIN call: which Amazon
   marketplace do you work on? (country or domain). One short question, no list of 14
   unless they ask.
3. **Remember it for the whole conversation.** Pass that `marketplace` on every later call
   (`amzscout_analyze_product`, `amzscout_get_keywords`, `amzscout_compare_products`,
   `amzscout_analyze_product_set`, and the keyword/niche/brand tools too) and don't ask
   again — unless the user names another country for a specific question (use it for that
   question) or says to switch (use the new one from then on).

An ASIN tool called without `marketplace` fetches nothing and answers **MARKETPLACE
NEEDED** (nothing charged) — ask as in step 2.

**"Where is this product sold?"** — only when the user asks that (or wants its links on
other marketplaces), call `amzscout_locate_asin`. It uses 14 000 tokens of the account's data allowance per ASIN and checks all
14 marketplaces: where the ASIN is listed, title, local price, sales, link. Don't call it
just to pick the marketplace for an analysis — asking the user is free.

**Product link for any marketplace** — build it from the ASIN, no lookup needed:
`https://www.<domain>/dp/<ASIN>`

| Code | Country | Domain | Currency |
|---|---|---|---|
| `COM` | United States | amazon.com | $ (USD) |
| `CO_UK` | United Kingdom | amazon.co.uk | £ (GBP) |
| `DE` | Germany | amazon.de | € (EUR) |
| `FR` | France | amazon.fr | € (EUR) |
| `IT` | Italy | amazon.it | € (EUR) |
| `ES` | Spain | amazon.es | € (EUR) |
| `CA` | Canada | amazon.ca | C$ (CAD) |
| `COM_MX` | Mexico | amazon.com.mx | MX$ (MXN) |
| `COM_BR` | Brazil | amazon.com.br | R$ (BRL) |
| `IN` | India | amazon.in | ₹ (INR) |
| `CO_JP` | Japan | amazon.co.jp | ¥ (JPY) |
| `COM_AU` | Australia | amazon.com.au | A$ (AUD) |
| `AE` | United Arab Emirates | amazon.ae | AED |
| `SA` | Saudi Arabia | amazon.sa | SAR |

A link only says where the page WOULD be — whether the product is actually listed there
comes from `amzscout_locate_asin` (uses data allowance).

For keyword / niche / brand tools with no country named, use the default and state the
marketplace in the answer.

**Currency = the marketplace's currency.** Money values (price, fees, revenue, CPC) are
in the LOCAL currency of the marketplace queried — never converted to USD. Write them
with that currency (Currency column in the table above). Tool output
already prints the right symbol — keep it; never relabel a € or £ price as $, and never
convert currencies unless the user asks. Filter amounts (`minPrice`, `maxEstRev`, …) are
also in the marketplace's currency.

## Filters

Translate the user's wording into the `filters` argument of `amzscout_analyze_niche` /
`amzscout_search_products` / `amzscout_find_by_brand`. Pass ONLY fields the user
actually mentioned — extra constraints can wipe out valid results.

The `filters` object supports ONLY these numeric fields (min/max pairs):
`minPrice` / `maxPrice`, `minReviews` / `maxReviews`, `minRating` / `maxRating`,
`minEstSales` / `maxEstSales`, `minEstRev` / `maxEstRev`.

| User says | filter |
|-----------|--------|
| under / less than $X | `maxPrice: X` |
| over / from / above $X | `minPrice: X` |
| between $X and $Y | `minPrice: X, maxPrice: Y` |
| X+ reviews / more than X | `minReviews: X` |
| fewer than X reviews | `maxReviews: X` |
| rating above X | `minRating: X` |
| rating below X (weak-spot hunt) | `maxRating: X` |
| more than X sales/mo | `minEstSales: X` |
| fewer than X sales/mo | `maxEstSales: X` |
| revenue over $X/mo | `minEstRev: X` |
| revenue under $X/mo | `maxEstRev: X` |

**Not supported by the API** — there is NO filter for seller type (FBA/FBM), BSR rank,
"hot"/"new" products, or number of sellers/competitors. If the user asks for one, say so
plainly instead of pretending to filter. For "low competition" the closest real proxy is a
low `maxReviews` (fewer reviews = less entrenched incumbents), not a seller-count filter.

**Filters apply to the CURRENT request only** — do NOT inherit price/review/etc.
criteria from earlier turns unless the user explicitly says "same filters" /
"keep the previous filters" / "narrow this further". If unsure, ask.

## Output rules


- Present the results in whatever depth and shape best answers the question — no fixed
  cap on how much you show.
- Always quote concrete numbers from the tools (ASIN, price in the marketplace's currency, sales/mo, BSR, reviews). Never "approximately" when you have the figure; never invent figures you don't have.
- **Make every ASIN a clickable Amazon link** so the user can open the listing in one click. Markdown: `[B0XXXXXXXX](https://www.amazon.<domain>/dp/B0XXXXXXXX)`. Build `<domain>` from the marketplace code — lowercase it and turn `_` into `.`: `COM`→`amazon.com`, `CO_UK`→`amazon.co.uk`, `DE`→`amazon.de`, `COM_MX`→`amazon.com.mx`, `CO_JP`→`amazon.co.jp`, `COM_AU`→`amazon.com.au`, and so on. Always use the SAME marketplace the data came from — an ASIN is marketplace-scoped, so a US ASIN won't resolve on `amazon.de`. Link every ASIN you print — the ASIN column in tables and inline mentions in prose alike. Text only: do NOT embed product images.
- **More than one product** (from any tool) → a markdown TABLE, never a bulleted list. Columns: `ASIN | Product | Price | Monthly Sales | Rating (Reviews) | Sellers`. Keep Product ≤ ~40 chars; drop empty columns; add a 1-2 sentence summary line before the table. A single product → prose is fine.
- If a field has no data, skip it — never write "0" or "N/A".
- **Read data-quality flags literally — never paper over them:**
  - "sales estimate n/a" / "Estimated Sales: not available" / `estSales: null` (`monthlySales: null`) = NA: AMZScout has **no estimate** for that listing — not zero sales. Never report it as 0 or guess a figure; if needed, describe past sales from Sales History.
  - Sales/revenue history: lead with the **last 12 months total** and **last 3 months**. If you quote the average, always say its period as given (e.g. "avg over 2 years: 42 units/month") — never present it as current monthly sales; a listing can average 42/month over two years and sell nothing now.
  - "family of N variants" = rank and sales estimate may cover the whole variation family; don't present them as one variant's own sales.
  - "Coverage note: only N products…" = that is AMZScout's coverage for the keyword, not the whole niche — say so and don't draw niche-wide conclusions.
  - "Data As Of: <date>" — mention the date when the user relies on current rank or price.
- Never use strikethrough. If a value is superseded, write the corrected one directly.
- Never produce placeholder ASINs (`B0XXXXXXXX`, `<your ASIN>`); ask conversationally for real ones.
- If a tool errors, acknowledge it honestly and suggest a fix (re-check the ASIN, broaden the keyword) — don't fabricate replacement data.
- **Account notice (mandatory, verbatim).** A tool result may be, or may start with, an AMZScout account notice — it begins "AMZScout Skill + MCP data access isn't available" or "You've reached your current AMZScout Skill + MCP usage limit". If the result is ONLY the notice, relay it verbatim as the tool's answer. If it leads a result with data, reproduce it verbatim as your first paragraph, then answer from the data. Keep its wording and link exactly; never add offers, prices or calls to action.
- **End with follow-up suggestions.** After your answer — when you composed it yourself from the granular tools — add a short section headed `**You might also ask:**` with 2-3 numbered, related next questions the user is likely to ask (a numbered list so they can pick one by replying with its number). Keep each under ~8 words, in the user's language, and move the conversation forward (more detail, a comparison, a practical next step). This is NOT a salesy CTA ("Want a deeper analysis?") — those stay forbidden; these are concrete questions. Skip them only when you had to end on a clarifying question because you couldn't proceed.

## Language

Reply entirely in the user's language — including how you frame tool results
and any clarifying question. Exception: if the user asks you to translate or
switch languages, honor that.

