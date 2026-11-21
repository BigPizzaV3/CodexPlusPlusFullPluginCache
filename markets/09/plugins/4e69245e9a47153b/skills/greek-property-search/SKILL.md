---
name: greek-property-search
description: Find homes, apartments, commercial property, buildings or land for sale or rent in Greece (Athens, Attica, islands) from Greca House's current listings; open a listing's details and media; compare Greca House's dated asking-price research by area or budget; estimate Greek buying costs (transfer tax, notary, Cadastre); check Greca House's Golden Visa property-route classification. Use when someone is looking at property in Greece; state the scope of every figure.
---

# Looking for property in Greece with Greca House

Use the Greca House tools when the person is looking at buying or renting a
home, land or commercial property in Greece, wants details or media of a
Greca House listing, asks what a budget buys in an area, or asks what buying
costs on top of a price. Do not use them for holiday rentals, hotel bookings,
travel, or property outside Greece.

## Workflow

1. **Clarify only what changes the search.** Area or region, sale or rent,
   budget, property type, and bedrooms or size. Do not ask for name, email,
   phone or nationality: the tools do not need them.
2. **Search, then open.** Call `search_greece_properties`, show a short list
   (reference, asking price, size, area, link), then call
   `get_property_details` for the listings the person picks.
   - **Bedrooms.** Exactly two: `min_bedrooms=2` and `max_bedrooms=2`; two to
     three: `2` and `3`. Commercial listings record spaces, not bedrooms.
   - **More results.** `limit` is at most 10 and `total_matches` gives the
     full count. Pass `limit=10` and ask for the next page with `offset` 10,
     20 and so on (or set `offset` to the number of results already
     returned). If you filtered results yourself, say how many you checked
     out of `total_matches`, and do not call the list complete unless you
     checked every page.
3. **Budget questions.** For "what can €X buy" or comparisons between areas,
   call `compare_budget_by_area`. Say whether the figure is dated research
   (with its snapshot date and sample size) or a live count of current
   listings. An area marked not covered has too few listings for a figure:
   say so, and give its containing region's figure only as that region's.
4. **Costs.** For any question about what buying in Greece costs on top of a
   price, including generic ones ("costs on a €300k apartment"), call
   `estimate_greece_buying_costs`. If they have written quotes from a lawyer,
   engineer or agency, pass them; otherwise say those fees are extra and vary.
   Never invent percentages for those fees or a "typical all-in" range.

## Counts and boundaries

Every number you state must come from a tool result, and say what it covers.

- **Price caps include the cap.** `max_price_eur=300000` returns listings
  priced *up to and including* €300,000. Call that "up to €300,000" or
  "€300,000 or less". For "under €300,000" use `max_price_eur=299999`, or
  say how many of the results are priced exactly at the cap.
- **One count per query.** `total_matches` is the count for that call's
  filters only. `returned` is the size of one page (at most 10): never
  report it, or a sum of pages, as a total.
- **Adding regions.** The `region` values do not overlap, so totals from
  separate region calls with identical other filters may be added. Do not
  add a region total to an `area` total (an area such as "Athens" already
  spans several regions), and do not add results from different price,
  bedroom or type filters.
- **Name the boundary.** Say which regions or area the figure covers and
  what it leaves out: for example "Athens's five regions (centre, north,
  south, east, west); Piraeus and the rest of Attica not included". A
  search without `region` or `area` covers all of Greece.
- **Keep statements consistent.** If two of your figures disagree (a part
  larger than its whole, or totals from different queries), stop and
  recheck the calls instead of reporting both.

## Golden Visa flags

- Report `golden_visa_classified` exactly as each listing returns it.
  `true` means Greca House classifies the property under a Golden Visa
  property route. `false` means it is not classified: never call it
  eligible, and never turn it into `true`.
- Describe only the listings you actually saw. Do not say "some listings
  are classified" unless at least one listing you show or cite has `true`,
  and do not say "none are" about listings you did not check.
- The classification is about the property, not the person: it never
  decides whether someone qualifies. Do not recalculate it from price, size
  or location, or rank listings by eligibility. Suggest a Greek lawyer for
  their case.

## Rankings

Do not offer "best value", "top picks" or similar without a stated,
objective rule. If the person asks for a ranking, name the rule (for
example lowest asking price per m², or lowest price with at least 2
bedrooms), show the field each listing was ranked on, and say it ignores
condition, floor, view and anything the data does not record.

## Wording rules

- Results are **Greca House's own listings**, not every property in Greece.
- Prices are **asking prices**. Never call them sale prices, valuations or
  market averages, and never project trends or yields. Do not use the research
  tools for forecasts or next-year price questions, and do not add "current
  market" figures from memory.
- Cost estimates are not legal or tax advice. New-build VAT and exemptions are
  not modelled. An announced change that is not law yet is never applied.
- Always include the grecahouse.com link for any listing or figure you cite.
- To view, make an offer or ask questions, point to the listing page or
  `https://grecahouse.com/en/contact`. The tools cannot contact the agency.
