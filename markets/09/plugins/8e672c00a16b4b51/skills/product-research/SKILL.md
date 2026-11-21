---
name: product-research
description: Use when researching an e-commerce product idea, sizing up an existing Amazon listing, or looking up who sells a product, once the 1Product MCP connector is available in this conversation. Triggers on phrasings like "is there demand for X", "should I sell Y", "who else is selling this", "how contested is this listing", "what keywords does this ASIN rank for", "how many people bought this", "expand this keyword into more ideas", "look up this seller".
---

# 1Product — live Amazon/e-commerce research

This connector does live Amazon/e-commerce research: demand, price, competition, keyword and
seller lookups, all fetched fresh at call time. Every tool except `browse_categories` (free) uses
the signed-in account's credits and charges only if data actually comes back. Nothing requires
setup first — no prior call and no existing report — but the account must be email-verified and
needs credits to use the credit-using tools. **A new account starts with no credits.** If a call
comes back with a `trial_required` or `insufficient_credits` status, tell the user plainly that
the account has no credits for this tool, rather than treating it as a finding about their
product. Do not offer to start a purchase, trial, upgrade or checkout, and stop calling tools until
the user says the account's credit balance has changed. Once an account has credits, most tools cost 5–35 credits. Three cost more:
`amazon_get_seller_details` (65), a large `amazon_get_bulk_search_volume` call (up to 45 for 1,000 keywords),
and `get_competition` (185 — the single most expensive tool here).

This file is guidance for you, the model — it is not itself a tool. Every claim it makes about a
tool's name, cost, or return shape should still match what `tools/list` actually reports; if the
two ever disagree, trust the live tool list.

If `tools/list` also shows an unprefixed name that looks like one of the `amazon_`-prefixed tools
below with the prefix removed (`get_offers`, `get_seller_details`, and so on), that is a
deprecated alias kept only for connections made before those tools were renamed — it behaves
identically, but always prefer the `amazon_`-prefixed name in this file for a fresh decision.

## Recognize the ask

| The user says (roughly) | Start with |
|---|---|
| "Is there demand for X" / "should I sell Y" | `get_demand` |
| "What would this sell for" / "what's the price range" | `get_price` |
| "How contested is this listing" / "who's fulfilling this" | `amazon_get_offers` |
| "What keywords does this ASIN rank for" | `amazon_get_ranked_keywords` (full list) or `amazon_get_rank_overview` (aggregate) |
| "Who else is selling this" / "who are the competitors" | `get_competition` |
| "Tell me about this seller" | `amazon_get_seller_details` |
| "Is anyone buying this" / "does this actually sell" | `amazon_get_purchase_signals` |
| "Give me more keyword ideas from X" | `amazon_get_related_keywords` |
| "Which keyword variants should I target, and how hard is each one" | `amazon_search_keywords` |
| "Check search volume for this list of keywords" | `amazon_get_bulk_search_volume` |
| "Show me what's actually on the search results page" | `amazon_search_products` |
| "What categories exist" / just exploring | `browse_categories` (free) |

## Route by what you have

- **A product idea, not yet listed** (a plain-language name): `get_demand` first. Widen to
  `get_price`, `get_trends`, `get_ad_activity`, or `get_competition` only once the demand read
  justifies spending more.
- **An Amazon listing already live** (an ASIN): `amazon_get_product_details`, `amazon_get_offers`,
  `amazon_get_rank_overview`, `amazon_get_ranked_keywords`, `amazon_get_product_competitors`.
- **A specific Amazon seller** (a seller id): `amazon_get_seller_details`.
- **A keyword or a list of keywords**: `amazon_search_keywords` to expand one seed term into a
  table of search-term variants with volume/CPC/ranking-challenge/trend per row, when the ask is
  which variants to target; `amazon_get_related_keywords` to expand one seed term into adjacent
  product/niche ideas instead (Amazon's own "related searches" strings, no per-idea metrics),
  when the ask is what else to sell; `amazon_get_bulk_search_volume` to size up to 1,000
  candidates in one call; `amazon_get_purchase_signals` to
  see which listings on a keyword are actually selling. `amazon_search_products` overlaps heavily
  with `amazon_get_purchase_signals` (same asin/title/price/rating/reviewCount/boughtPastMonth/
  sponsored fields) but costs 7x more — default to `amazon_get_purchase_signals`, and reach for
  `amazon_search_products` only when you need every listing on the page (not just the top 20
  ranked ones) or a listing's image/URL.
- **Nothing yet, just exploring categories**: `browse_categories` — free, costs nothing.

## The one chain that isn't obvious from the tool list

`get_competition`'s `topSellers` list is the only place a `sellerId` appears in this
conversation. No other tool produces one, and `amazon_get_seller_details` has no other way to be
reached than a `sellerId` from that list, or one the user already supplied directly. **Never
guess or invent a sellerId** — if you don't have one, get one from `get_competition` first.

## Spend cheap first

Default to the cheapest tool that could answer the question in front of you. Treat
`get_competition` (185 credits, the single most expensive tool here) as a deliberate escalation
once a cheaper signal already justifies it, never a default first step.
Don't call every tool for one idea "to be thorough" — that burns an account's credits on a
single question and is the outcome this connector most wants you to avoid. Stop as soon as you
can actually answer what the user asked.

The one deliberate exception: if the user's ask is specifically "who sells this" / "find the
seller," go straight to `get_competition` — it's the only tool that resolves seller identity, so
there is no cheaper tool to screen with first.

<!--
  Keep this table's costs and return shapes in sync with CreditOptions.cs (the source of truth),
  McpServerInstructions.cs, and ProductResearchPrompts.cs by hand — see their own doc comments
  for the reverse pointers. Nothing automated checks this file.
-->

## Full tool reference

| Tool | Cost | Input | Returns |
|---|---|---|---|
| `get_demand` | 10 | `query`, `countryCode?` | Search volume, CPC, difficulty, trend slope, related keywords |
| `get_price` | 35 | `query`, `countryCode?` | Median/min/max price across channels, per-channel breakdown |
| `get_competition` | 185 | `query`, `countryCode?` | Brand concentration, seller/store counts, top sellers (with `sellerId`), top independent stores |
| `get_ad_activity` | 5 | `query`, `countryCode?` | Advertiser count, shopping-result count, who's advertising (partial coverage — read `coverageNote`) |
| `get_trends` | 20 | `query`, `countryCode?` | Search-interest slope + confidence, mention volume/velocity, breakout read |
| `amazon_get_seller_details` | 65 | `sellerId` | Seller profile, rating, feedback, a preview of their other listings |
| `amazon_get_product_details` | 35 | `asin` | Price, availability, rating, category, bestseller rank(s), A+ content, feature bullets |
| `amazon_get_ranked_keywords` | 20 | `asin` | Up to 100 keywords this ASIN ranks for — volume, position, listing title/price/rating/badges/delivery, CPC, and a search trend (peak month, season impact) |
| `amazon_get_product_competitors` | 10 | `asin` | Other ASINs competing for the same keywords in real search results |
| `amazon_get_rank_overview` | 5 | `asin` | Keyword counts per rank bucket (#1, #2-3, #4-10, #11-100), organic and paid |
| `amazon_get_purchase_signals` | 5 | `keyword` | "Bought in past month" badge, Amazon's Choice / Best Seller flags, per listing |
| `amazon_get_offers` | 35 | `asin` | Every offer on a listing: price, condition, Prime, FBA/FBM, Buy Box winner |
| `amazon_get_related_keywords` | 10 | `keyword` | Amazon's own "related searches" expansion from a seed term |
| `amazon_search_keywords` | 10 | `keyword` | Up to 100 search-term variants of a seed keyword — volume, CPC, ranking-challenge score, and a search trend (peak month, season impact) per row |
| `amazon_get_bulk_search_volume` | scales with list size (floor 5) | `keywords[]` (up to 1,000) | Search volume per keyword — a screening tool for a shortlist, not one `get_demand` call per idea |
| `amazon_search_products` | 35 | `query` | Every listing on an Amazon search-results page: ASIN, title, price, rating, reviews, sponsored flag, bought-past-month |
| `browse_categories` | free | `categoryCode?` | A vertical category taxonomy for ideation (not Amazon's own browse tree) |

## Starting points, if your client surfaces MCP prompts

This connector also exposes three prompts that each pre-load one of the chains above:
`research_product_idea`, `size_up_listing`, `find_the_seller`. If your client's UI offers prompts
from a connector, these are equivalent shortcuts to the routing above, not different guidance.

## Worked examples

**"Is a foldable laptop stand worth making?"** → `get_demand(query: "foldable laptop stand")`.
If volume and difficulty look promising, widen to `get_price` and `get_trends`. Only call
`get_competition` if the user specifically wants to know who's already selling it, or if the
demand/price read alone can't settle the question.

**"How does B07HD3CRG2 stack up?"** → `amazon_get_product_details(asin: "B07HD3CRG2")`, then
`amazon_get_offers` for Buy Box contest, then `amazon_get_rank_overview`. Call `amazon_get_ranked_keywords` only if
the overview shows something worth digging into, and `amazon_get_product_competitors` only if the user
specifically wants the competing ASINs.

**"Who's dominating the knee pillow market?"** → `get_competition(query: "knee pillow")`
directly — this is the one case where the expensive tool is the right first call. Read
`topSellers`, then `amazon_get_seller_details(sellerId: ...)` on whichever seller the user wants more on.

## Rules

- Never name a specific data source or provider in anything you say to the user — describe what
  a number *means* ("search interest is trending up"), never where it was purchased from.
- Never invent a `sellerId` or an ASIN that wasn't returned by a tool or supplied by the user.
- If a tool returns `insufficient_credits`, tell the user plainly and stop calling tools until
  they say the account's credit balance has changed — retrying will fail identically. Do not offer to
  start a purchase, upgrade or checkout; just state the situation.
- If a tool returns `email_not_verified`, tell the user to verify their email before continuing.
