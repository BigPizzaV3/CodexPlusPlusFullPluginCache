# Workflow: Market Mapping

Goal: build a reviewed, segmented company landscape against an explicit thesis and screening mandate.

## Procedure

1. Translate the thesis into no more than three proposed sub-verticals based on buyer, product, use case, and business model. Show the segment definitions in the deliverable so the user can correct them.
2. Resolve each unique category and location once. Resolve all predicate and order fields on the current session, preferably with one collection-level fields reference. Use a targeted field reference only when the collection response does not expose a needed operator, enum, or value shape. Projection-only output fields do not need reference calls.
3. Apply the complete mandate before text refinement: company facet, geography, funding boundary, all target stages including pre-seed when applicable, operating status, and private IPO status.
4. Query each sub-vertical once. Request canonical identifier, description, categories, location, funding total, latest funding date/type/amount, employee band, founding date, investors, and website.
   - Prioritize a valid first search over optional default predicates or enrichment. Run the first search no later than Crunchbase call 12. Keep a read-only landscape to 16 Crunchbase calls and a build-and-save landscape to 20; after a successful result, render or proceed directly through the authorized list write and reconciliation.
5. If a broad text match produces more than 50 results or more than three times the segment target, use one combined distinctive-phrase predicate for the highest-noise segment. Never run one query per keyword or synonym. Keep the landscape to four `cb_search_query` calls total unless the user explicitly asks for exhaustive expansion.
6. Retry with the full description field when a short-description phrase set does not represent the intended segment. Do not loosen mandate constraints without user approval.
7. Review descriptions before excluding candidates. Place a company in its best-fit segment once and retain a concise exclusion log.
8. Compute full months since the latest funding date using `calculation-spec.md`. Apply timing labels only; do not infer fundraising intent or company health.
9. Obtain and preserve each organization profile URL.
   - Reuse the search projections. Do not call `cb_entity_get` for a candidate when the search already returned the fields needed for the landscape row.
10. Present the reviewed universe before any saved-list write. Follow `saved-lists.md` only if the user explicitly asks to save it.
    - Once `cb_list_get` reconciles an authorized write, stop calling tools and render the final result immediately. Do not reopen discovery or enrichment after the write.

## Output

One table per segment:

| Company | What it does | Total raised | Latest round (type, amount, date) | Full months since | Timing signal | Investors | Relevance confidence |
|---|---|---:|---|---:|---|---|---|

Then include:

- **Review priorities:** candidates ranked against the supplied mandate, with conditional reasons
- **Segment observations:** density and differentiation within the returned, reviewed universe
- **Exclusions and uncertainty:** concise reasons
- **Query audit:** segment definitions, resolved identifiers, structured filters, counts, refinements, and denominator
- **Source notes:** use `—` conventions from `output-contract.md`

The target count is a quality guide, not a quota. Do not pad a segment with weak matches.
