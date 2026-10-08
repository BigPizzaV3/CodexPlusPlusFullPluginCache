---
name: easy-cardz-nba-scout
description: Find, track, and classify NBA trading-card buying opportunities for fast resale, especially CardHobby listings priced EUR 10-250 all-in. Use when the user asks to discover or monitor active NBA card deals, return every in-scope candidate with a direct auction URL, compare recent sales comps, estimate resale profit, calculate a shipping-inclusive maximum bid, maintain a bid tracker, or classify cards as Buy, Watch, Too Expensive, or Pass. Search public CardHobby pages without login first and use user-provided Card Ladder screenshots or copied comps, or a licensed pricing source.
---

# Easy Cardz NBA Scout

## Goal

Find promising NBA cards instead of waiting for the user to supply individual listings. Optimize for fast resale and a meaningful net margin, not for long-term speculation.

Read [references/easy-cardz-profile.md](references/easy-cardz-profile.md) and use that profile unless the user overrides it.

- All-in acquisition cost: EUR 10-250.
- Minimum expected ROI on all-in acquisition cost: 20%.
- Do not apply a separate minimum euro-profit gate unless the user supplies one.
- Preferred liquidity: high or medium.
- Action mode: research only; never bid, buy, message a seller, or change an account.
- Reporting mode: show every requested in-scope candidate, not only favorites or Buy recommendations.

Treat all recommendations as estimates. State assumptions and uncertainty clearly.

## Access boundaries

- Search CardHobby's publicly accessible pages without login first. Do not require or probe for a signed-in session when public discovery is sufficient.
- Use `@Chrome` with a signed-in CardHobby session only if a concrete search or listing detail is blocked by an observed sign-in wall and the user authorizes that site access.
- Never ask the user to paste passwords, one-time codes, session cookies, or API secrets into chat.
- Use CardHobby through its normal user interface only when its terms and permissions allow the requested browsing. Do not bypass rate limits, CAPTCHAs, geographic restrictions, or navigation controls.
- Do not bulk scrape, systematically download, or build a database of platform content.
- Do not automate Card Ladder retrieval without express written permission or a licensed integration. Card Ladder prohibits automated gathering in its current terms. Accept user-provided screenshots, copied sales, exports, or a licensed comp source instead.
- Do not publish or redistribute raw paid-source data. Return only the limited analysis needed for the user's current decision.
- Stop and explain the limitation if a site blocks automation or its terms do not permit the requested workflow.
- Never guess, reconstruct, shorten, or invent a CardHobby listing URL. Copy the canonical URL from the opened listing and verify that it resolves to the same card.

## Start a run

Collect only inputs that materially affect the recommendation:

1. Player list or discovery theme.
2. Optional card preferences or exclusions.
3. Current budget if different from EUR 10-250 per card.
4. Resale channel only when different from the saved Easy Cardz profile.
5. Desired result count; default to the best 10 candidates.

If the player list is missing, ask for it. Do not invent a current popularity list without researching current NBA and hobby demand.

## Discover CardHobby candidates

Read [references/cardhobby-search-terms.md](references/cardhobby-search-terms.md) before searching.

1. Open CardHobby's basketball category or normal search interface.
2. Search each supplied player using the English name, Chinese name when known, common hobby aliases, and the relevant attribute terms from the reference. Inspect active auctions and fixed-price listings.
3. Estimate all-in acquisition cost before comp research. Retain out-of-range or financially weak requested candidates for reporting and label the reason instead of silently removing them.
4. Prioritize recognizable rookie cards, liquid parallels, autos, numbered cards, SSPs, case hits, and graded cards with repeat sales.
5. Deprioritize vague listings, poor-condition cards, cards with unclear variants, obscure college products, common base cards with weak spreads, and cards whose only apparent appeal is a low serial number.
6. Respect the user's requested result count. Use a manageable first pass and avoid bulk collection, but do not reduce the final list to favorites only.
7. Open every reported listing and record its canonical CardHobby URL, end time, current price, visible shipping, seller, and exact card attributes. Do not retain unrelated account or personal information.
8. Keep financially weak, low-confidence, or out-of-budget cards in the results with a clear status. Put unverifiable URLs in a separate rejected section because they cannot be safe tracker entries.

## Resolve and verify CardHobby URLs

When the user explicitly requests a search on the CardHobby website, use CardHobby's normal public user interface for discovery.

1. Start signed out unless the requested page is visibly blocked by a sign-in wall.
2. Select Basketball and active Auction or Buy It Now listings.
3. Search the player's English name, Chinese name when known, common hobby aliases, and relevant attribute terms.
4. Open every plausible candidate in its individual CardHobby detail page.
5. Copy the exact URL displayed after the detail page has loaded. Preserve hash routes, query parameters, and listing IDs unchanged.
6. Record the visible listing number, full title, status, end time, current price, shipping, seller, and exact card attributes.
7. Reopen the saved URL once and verify that it resolves to the same listing, player, card, and listing number.
8. Mark the URL as Verified only when all fields match and the listing is active.
9. Exclude search-result pages, seller pages, expired listings, unstable URLs, and URLs that cannot be reopened.
10. Never derive, reconstruct, shorten, or guess a listing URL from an item ID.

If an individual detail page is blocked by a visible sign-in wall, stop and ask the user to sign in manually. Continue only after the user asks to resume. If CardHobby presents a CAPTCHA or automation block, follow the site's controls and the browser safety rules; do not bypass it.

## Identify the exact card

Resolve all of these fields before valuing the card:

- Season/year and manufacturer.
- Product, set, insert, and card number.
- Player and team shown.
- Base versus exact parallel or variation.
- Serial numbering and whether the copy is a special first, last, or jersey number.
- Auto, memorabilia, patch type, and authentication wording.
- Raw versus grader, grade, qualifiers, and label generation when relevant.
- Rookie designation and actual rookie relevance.
- Visible condition issues or listing ambiguity.

Never compare Raw with PSA 10, a base card with a parallel, or materially different serial-number tiers as if they were exact matches. Mark the identification as Exact, Near, or Uncertain.

## Analyze comps

Read [references/evaluation-rubric.md](references/evaluation-rubric.md) before evaluating candidates.

Use exact recent completed sales first. Keep near comps separate and explain every adjustment. Prefer the median of the most recent five reliable exact sales. Show sale dates and source names when provided.

Treat an estimated value, active listing, unsold listing, best-offer asking price, or player index as supporting context rather than a completed sale.

For sparse cards, lower confidence instead of manufacturing precision. Use nearby serial tiers or related parallels only as explicitly labeled secondary evidence.

## Calculate economics

Run `scripts/evaluate_deal.py` for every shortlisted candidate. Supply monetary values in EUR and include every known acquisition and sale cost.

Example:

```bash
python3 scripts/evaluate_deal.py - <<'JSON'
{
  "listing_price": 120,
  "buyer_fee_rate": 0,
  "buyer_fee_fixed": 0,
  "inbound_shipping": 6,
  "import_cost": 0,
  "estimated_resale": 190,
  "seller_fee_rate": 0,
  "outbound_shipping": 6.19,
  "other_sale_cost": 0,
  "min_profit": 0,
  "min_roi": 0.20,
  "min_total_cost": 10,
  "max_total_cost": 250,
  "liquidity": "high",
  "comp_confidence": 0.9
}
JSON
```

Do not hide missing costs. If customs, combined shipping allocation, payment conversion, or selling fees are unknown, show a range or provisional result.

## Decide

- **Buy:** Meet both financial thresholds, remain inside the EUR 10-250 all-in range, have high or medium liquidity, and have sufficiently reliable identification and comps.
- **Watch:** Miss one threshold narrowly, have low liquidity, depend on near comps, or have a current price within roughly 10% of the calculated maximum.
- **Pass:** Exceed the maximum bid, fall outside the budget, rely on weak or mismatched comps, have poor resale liquidity, or contain material listing risk.

Classify every requested in-scope card. Do not hide or discard a card because it is a Watch or Pass.

## Track prices and maximum bids

- Treat the user's maximum bid as the maximum all-in CardHobby acquisition cost unless the user explicitly requests a hammer-price limit.
- Include visible CardHobby shipping, buyer fees, import costs, and currency costs in the all-in amount.
- Preserve each listing by its verified URL and listing ID so later checks update the same row rather than create duplicates.
- On a later check, update current price, visible shipping, time remaining, active status, and checked-at time.
- Mark a card **Too Expensive** when its current all-in acquisition cost exceeds the user's maximum all-in bid. Keep it visible unless the user explicitly asks to archive or remove it.
- Mark ended listings as Won, Lost, or Outcome Unknown only from information the user supplies or the visible authorized account state. Never infer a win from the final price alone.
- Do not bid automatically.

## Report

Return every requested in-scope card in a table with one clickable CardHobby link per row:

| Rank | Card | CardHobby auction | CardHobby price | All-in | Recent comps | Comp median | Max bid | Net profit | ROI | Liquidity | Confidence | Decision |
|---|---|---|---:|---:|---|---:|---:|---:|---:|---|---|---|

Format the auction cell as a descriptive Markdown link such as `[Auktion öffnen](verified canonical URL)`. Also repeat the direct link in each Buy or Watch explanation so it remains easy to open on mobile.

Sort Buy and Watch cards first for convenience, but keep Too Expensive and Pass cards in the same result set. Then add:

- One-line reason for every Buy and Watch.
- Key risks or mismatches.
- Assumptions used for fees, shipping, currency, and resale channel.
- A verified direct CardHobby listing link for every reported candidate.
- A short best-opportunities summary without removing the remaining cards.

Use the user's language. Keep the result decision-focused and avoid hype or guaranteed-return language.
